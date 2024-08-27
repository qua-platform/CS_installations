# %%
"""
RAMSEY WITH VIRTUAL Z ROTATIONS
The program consists in playing a Ramsey sequence (x90 - idle_time - x90 - measurement) for different idle times.
Instead of detuning the qubit gates, the frame of the second x90 pulse is rotated (de-phased) to mimic an accumulated
phase acquired for a given detuning after the idle time.
This method has the advantage of playing resonant gates.

From the results, one can fit the Ramsey oscillations and precisely measure the qubit resonance frequency and T2*.

Prerequisites:
    - Having found the resonance frequency of the resonator coupled to the qubit under study (resonator_spectroscopy).
    - Having calibrated qubit pi pulse (x180) by running qubit, spectroscopy, rabi_chevron, power_rabi and updated the state.
    - (optional) Having calibrated the readout (readout_frequency, amplitude, duration_optimization IQ_blobs) for better SNR.

Next steps before going to the next node:
    - Update the qubits frequency (f_01) in the state.
    - Save the current state by calling machine.save("quam")
"""
from qualibrate import QualibrationNode, NodeParameters
from typing import Optional, Literal


class Parameters(NodeParameters):
    qubits: Optional[str] = None
    num_averages: int = 200
    frequency_detuning_in_mhz: float = 1.0
    min_wait_time_in_ns: int = 16
    max_wait_time_in_ns: int = 4000
    wait_time_step_in_ns: int = 20
    flux_point_joint_or_independent: Literal['joint', 'independent'] = "joint"
    simulate: bool = False

node = QualibrationNode(
    name="05_Ramsey",
    parameters_class=Parameters
)

node.parameters = Parameters()


from qm.qua import *
from qm import SimulationConfig
from qualang_tools.results import progress_counter, fetching_tool
from qualang_tools.plot import interrupt_on_close
from qualang_tools.loops import from_array, get_equivalent_log_array
from qualang_tools.units import unit
from quam_libs.components import QuAM
from quam_libs.macros import qua_declaration, multiplexed_readout, node_save

import matplotlib.pyplot as plt
import numpy as np

import matplotlib
from lib.plot_utils import QubitGrid, grid_iter
from lib.save_utils import fetch_results_as_xarray
from lib.fit import fit_oscillation_decay_exp, oscillation_decay_exp

# matplotlib.use("TKAgg")


###################################################
#  Load QuAM and open Communication with the QOP  #
###################################################
# Class containing tools to help handle units and conversions.
u = unit(coerce_to_integer=True)
# Instantiate the QuAM class from the state file
machine = QuAM.load()
# Generate the OPX and Octave configurations
config = machine.generate_config()
octave_config = machine.get_octave_config()
# Open Communication with the QOP
qmm = machine.connect()

# Get the relevant QuAM components
if node.parameters.qubits is None:
    qubits = machine.active_qubits
else:
    qubits = [machine.qubits[q] for q in node.parameters.qubits.split(', ')]
num_qubits = len(qubits)

###################
# The QUA program #
###################
n_avg = node.parameters.num_averages  # The number of averages

# Dephasing time sweep (in clock cycles = 4ns) - minimum is 4 clock cycles
idle_times = np.arange(
    node.parameters.min_wait_time_in_ns // 4,
    node.parameters.max_wait_time_in_ns // 4,
    node.parameters.wait_time_step_in_ns // 4,
)

# Detuning converted into virtual Z-rotations to observe Ramsey oscillation and get the qubit frequency
detuning = node.parameters.frequency_detuning_in_mhz
flux_point = node.parameters.flux_point_joint_or_independent  # 'independent' or 'joint'

with program() as ramsey:
    I, I_st, Q, Q_st, n, n_st = qua_declaration(num_qubits=num_qubits)
    t = declare(int)  # QUA variable for the idle time
    sign = declare(int)  # QUA variable to change the sign of the detuning
    phi = declare(fixed)  # QUA variable for dephasing the second pi/2 pulse (virtual Z-rotation)

    for i, q in enumerate(qubits):

        # Bring the active qubits to the minimum frequency point
        if flux_point == "independent":
            machine.apply_all_flux_to_min()
            q.z.to_independent_idle()
        elif flux_point == "joint":
            machine.apply_all_flux_to_joint_idle()
        else:
            machine.apply_all_flux_to_zero()
        wait(1000)

        with for_(n, 0, n < n_avg, n + 1):
            save(n, n_st)
            with for_(*from_array(t, idle_times)):
                with for_(*from_array(sign, [-1,1])):
                    # Rotate the frame of the second x90 gate to implement a virtual Z-rotation
                    # 4*tau because tau was in clock cycles and 1e-9 because tau is ns
                    assign(phi, Cast.mul_fixed_by_int(detuning * 1e-9, 4 * t ))
                    assign(phi, Cast.mul_fixed_by_int(phi, sign))
                    align()
                    # Strict_timing ensures that the sequence will be played without gaps
                    with strict_timing_():
                        q.xy.play("x180", amplitude_scale = 0.5)
                        q.xy.frame_rotation_2pi(phi)
                        q.xy.wait(t)
                        q.xy.play("x180", amplitude_scale = 0.5)

                    # Align the elements to measure after playing the qubit pulse.
                    align()
                    # Measure the state of the resonators
                    q.resonator.measure("readout", qua_vars=(I[i], Q[i]))

                    # save data
                    save(I[i], I_st[i])
                    save(Q[i], Q_st[i])

                    # Wait for the qubits to decay to the ground state
                    wait(machine.thermalization_time * u.ns)
                    
                    # Reset the frame of the qubits in order not to accumulate rotations
                    reset_frame(q.xy.name)

    with stream_processing():
        n_st.save("n")
        for i in range(num_qubits):
            I_st[i].buffer(2).buffer(len(idle_times)).average().save(f"I{i + 1}")
            Q_st[i].buffer(2).buffer(len(idle_times)).average().save(f"Q{i + 1}")


###########################
# Run or Simulate Program #
###########################
simulate = node.parameters.simulate

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=10_000)  # In clock cycles = 4ns
    job = qmm.simulate(config, ramsey, simulation_config)
    job.get_simulated_samples().con1.plot()
    node.results = {"figure": plt.gcf()}
else:
    # Open the quantum machine
    qm = qmm.open_qm(config)
    # Calibrate the active qubits
    # machine.calibrate_octave_ports(qm)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(ramsey)
    # Get results from QUA program
    for i in range(num_qubits):
        print(f"Fetching results for qubit {qubits[i].name}")
        data_list = sum([[f"I{i + 1}", f"Q{i + 1}"] ], ["n"])
        results = fetching_tool(job, data_list, mode="live")
    # Live plotting
    # fig, axes = plt.subplots(2, num_qubits, figsize=(4 * num_qubits, 8))
    # interrupt_on_close(fig, job)  # Interrupts the job when closing the figure
        while results.is_processing():
        # Fetch results
            fetched_data = results.fetch_all()
            n = fetched_data[0]
        # I_data = fetched_data[1::2]
        # Q_data = fetched_data[2::2]
        # Convert the results into Volts
        # I_volts = [u.demod2volts(I, qubit.resonator.operations["readout"].length) for I, qubit in zip(I_data, qubits)]
        # Q_volts = [u.demod2volts(Q, qubit.resonator.operations["readout"].length) for Q, qubit in zip(Q_data, qubits)]
        # Progress bar
            progress_counter(n, n_avg, start_time=results.start_time)
        # Plot results
        # plt.suptitle("Ramsey")
        # for i, (ax, qubit) in enumerate(zip(axes, qubits)):
        #     ax[0].cla()
        #     ax[0].plot(4 * idle_times, I_volts[i])
        #     ax[0].set_ylabel("I [V]")
        #     ax[0].set_title(f"{qubit.name}")
        #     ax[1].cla()
        #     ax[1].plot(4 * idle_times, Q_volts[i])
        #     ax[1].set_xlabel("Idle time [ns]")
        #     ax[1].set_ylabel("Q [V]")
        #     ax[1].set_title(f"{qubit.name}")
        # plt.tight_layout()
        # plt.pause(0.1)

    # Close the quantum machines at the end in order to put all flux biases to 0 so that the fridge doesn't heat-up
    qm.close()

    # # Save data from the node
    # data = {}
    # for i, qubit in enumerate(qubits):
    #     data[f"{qubit.name}_amplitude"] = 4 * idle_times
    #     data[f"{qubit.name}_I"] = np.abs(I_volts[i])
    #     data[f"{qubit.name}_Q"] = np.angle(Q_volts[i])
    # data["figure"] = fig

    # fig_analysis = plt.figure()
    # plt.suptitle("Ramsey")
    # # Fit data to extract the qubits frequency and T2*
    # for i, qubit in enumerate(qubits):
    #     try:
    #         from qualang_tools.plot.fitting import Fit

    #         fit = Fit()
    #         plt.subplot(num_qubits, 1, i + 1)
    #         fit_I = fit.ramsey(4 * idle_times, I_volts[i], plot=True)
    #         plt.xlabel("Idle time [ns]")
    #         plt.ylabel("I [V]")
    #         plt.title(f"{qubit.name}")
    #         plt.legend((f"T2* = {int(fit_I['T2'][0])} ns\n df = {int(fit_I['f'][0] * u.GHz - detuning)/u.kHz} kHz",))

    #         # Update the state
    #         qubit_detuning = fit_I["f"][0] * u.GHz - detuning
    #         qubit.T2ramsey = int(fit_I["T2"][0])
    #         qubit.xy.intermediate_frequency -= qubit_detuning
    #         data[f"{qubit.name}"] = {
    #             "T2*": qubit.T2ramsey,
    #             "if_01": qubit.xy.intermediate_frequency,
    #             "successful_fit": True,
    #         }
    #         print(f"Detuning to add to {qubit.name}: {-qubit_detuning / u.kHz:.3f} kHz")
    #         plt.tight_layout()
    #         data["figure_analysis"] = fig_analysis
    #     except (Exception,):
    #         data[f"{qubit.name}"] = {"successful_fit": False}
    #         pass
    # plt.show()

    # Save data from the node
    # node_save(machine, "ramsey", data, additional_files=True)

# %%
if not simulate:
    handles = job.result_handles
    ds = fetch_results_as_xarray(handles, qubits, {"sign" : [-1,1], "time": idle_times})
    ds = ds.assign_coords({'time' : (['time'], 4*idle_times)})
    ds.time.attrs['long_name'] = 'idle_time'
    ds.time.attrs['units'] = 'nS'
    node.results = {}
    node.results['ds'] = ds

# %%
if not simulate:
    fit = fit_oscillation_decay_exp(ds.I, 'time')
    fit_evals = oscillation_decay_exp(ds.time,fit.sel(fit_vals = 'a'),
                                      fit.sel(fit_vals = 'f'),fit.sel(fit_vals = 'phi'),
                                      fit.sel(fit_vals = 'offset'),fit.sel(fit_vals = 'decay'))

    within_detuning = (1e9*fit.sel(fit_vals = 'f') < 2 * detuning).mean(dim = 'sign') == 1
    positive_shift = fit.sel(fit_vals = 'f').sel(sign = 1) > fit.sel(fit_vals = 'f').sel(sign = -1)
    freq_offset = within_detuning * (fit.sel(fit_vals = 'f')* fit.sign).mean(dim = 'sign') + ~within_detuning * positive_shift * (fit.sel(fit_vals = 'f')).mean(dim = 'sign') -~within_detuning * ~positive_shift * (fit.sel(fit_vals = 'f')).mean(dim = 'sign')

    # freq_offset = (fit.sel(fit_vals = 'f')* fit.sign).mean(dim = 'sign')
    decay = 1e-9/fit.sel(fit_vals = 'decay').mean(dim = 'sign')
    fit_results = {q.name : {'freq_offset' : 1e9*freq_offset.loc[q.name].values, 'decay' : decay.loc[q.name].values} for q in qubits}
    node.results['fit_results'] = fit_results
    for q in qubits:
        print(f"Frequency offset for qubit {q.name} : {(fit_results[q.name]['freq_offset']/1e6):.2f} MHz ")
        print(f"T2* for qubit {q.name} : {1e6*fit_results[q.name]['decay']:.2f} us")

# %%
if not simulate:
    grid_names = [f'{q.name}_0' for q in qubits]
    grid = QubitGrid(ds, grid_names)
    for ax, qubit in grid_iter(grid):
        (ds.sel(sign = 1).loc[qubit].I*1e3).plot(ax = ax, x = 'time',
                                                 c = 'C0', marker = '.', ms = 1.0, ls = '', label = "$\Delta$ = +")
        ax.plot(ds.time, 1e3*fit_evals.loc[qubit].sel(sign = 1), c = 'C0', ls = '-', lw=0.5)
        (ds.sel(sign = -1).loc[qubit].I*1e3).plot(ax = ax, x = 'time',
                                                 c = 'C1', marker = '.', ms = 1.0, ls = '', label = "$\Delta$ = -")
        ax.plot(ds.time, 1e3*fit_evals.loc[qubit].sel(sign = -1), c = 'C1', ls = '-', lw=0.5)
        ax.set_ylabel('Trans. amp. I [mV]')
        ax.set_xlabel('Idle time [nS]')
        ax.set_title(qubit['qubit'])
        # ax.legend()
    grid.fig.suptitle('Ramsey : I vs. idle time')
    plt.tight_layout()
    plt.show()
    node.results['figure'] = grid.fig

# %%
if not simulate:
    with node.record_state_updates():
        for q in qubits:
            q.xy.intermediate_frequency -= float(fit_results[q.name]['freq_offset'])

# %%
node.results['initial_parameters'] = node.parameters.model_dump()
node.machine = machine
node.save()
