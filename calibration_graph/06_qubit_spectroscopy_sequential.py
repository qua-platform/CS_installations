# %%
"""
        QUBIT SPECTROSCOPY
This sequence involves sending a saturation pulse to the qubit, placing it in a mixed state,
and then measuring the state of the resonator across various qubit drive intermediate dfs.
In order to facilitate the qubit search, the qubit pulse duration and amplitude can be changed manually in the QUA
program directly without having to modify the configuration.

The data is post-processed to determine the qubit resonance frequency, which can then be used to adjust
the qubit intermediate frequency in the configuration under "center".

Note that it can happen that the qubit is excited by the image sideband or LO leakage instead of the desired sideband.
This is why calibrating the qubit mixer is highly recommended.

This step can be repeated using the "x180" operation instead of "saturation" to adjust the pulse parameters (amplitude,
duration, frequency) before performing the next calibration steps.

Prerequisites:
    - Identification of the resonator's resonance frequency when coupled to the qubit in question (referred to as "resonator_spectroscopy").
    - Calibration of the IQ mixer connected to the qubit drive line (whether it's an external mixer or an Octave port).
    - Set the flux bias to the minimum frequency point, labeled as "max_frequency_point", in the state.
    - Configuration of the saturation pulse amplitude and duration to transition the qubit into a mixed state.
    - Specification of the expected qubit T1 in the state.

Before proceeding to the next node:
    - Update the qubit frequency, labeled as f_01, in the state.
    - Save the current state by calling machine.save("quam")
"""
from qualibrate import QualibrationNode, NodeParameters
from typing import Optional, Literal


class Parameters(NodeParameters):
    qubits: Optional[str] = None
    num_averages: int = 20
    operation: str = "saturation"
    operation_amplitude_factor: Optional[float] = None
    operation_len: Optional[int] = None
    frequency_span_in_MHz: float = 10
    frequency_step_in_MHz: float = 0.05
    flux_point_joint_or_independent: Literal['joint', 'independent'] = "joint"
    target_peak_width: Optional[int] = None
    simulate: bool = False

node = QualibrationNode(
    name="03_Qubit_Spectroscopy",
    parameters_class=Parameters
)

node.parameters = Parameters()


from qm.qua import *
from qm import SimulationConfig
from qualang_tools.results import progress_counter, fetching_tool
from qualang_tools.plot import interrupt_on_close
from qualang_tools.loops import from_array
from qualang_tools.units import unit
from quam_libs.components import QuAM
from quam_libs.macros import qua_declaration

import matplotlib.pyplot as plt
import numpy as np

from lib.plot_utils import QubitGrid, grid_iter
from lib.save_utils import fetch_results_as_xarray

# matplotlib.use("TKAgg")


###################################################
#  Load QuAM and open Communication with the QOP  #
###################################################
# Class containing tools to help handling units and conversions.
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
resonators = [qubit.resonator for qubit in qubits]
num_qubits = len(qubits)

###################
# The QUA program #
###################

operation = node.parameters.operation  # The qubit operation to play, can be switched to "x180" when the qubits are found.
n_avg = node.parameters.num_averages  # The number of averages
# Adjust the pulse duration and amplitude to drive the qubit into a mixed state
operation_len = node.parameters.operation_len  # can be None - will just be ignored
if node.parameters.operation_amplitude_factor:
    # pre-factor to the value defined in the config - restricted to [-2; 2)
    operation_amp = node.parameters.operation_amplitude_factor
else:
    operation_amp = 1.
# Qubit detuning sweep with respect to their resonance frequencies
span = node.parameters.frequency_span * u.MHz
step = node.parameters.frequency_step * u.MHz
dfs = np.arange(-span//2, +span//2, step)
flux_point = node.parameters.flux_point_joint_or_independent  # 'independent' or 'joint'

target_peak_width = node.parameters.target_peak_width
if target_peak_width is None:
    target_peak_width = 3e6  # the desired width of the response to the saturation pulse (including saturation amp), in Hz

with program() as qubit_spec:
    # Macro to declare I, Q, n and their respective streams for a given number of qubit (defined in macros.py)
    I, I_st, Q, Q_st, n, n_st = qua_declaration(num_qubits=num_qubits)
    df = declare(int)  # QUA variable for the qubit frequency

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
            with for_(*from_array(df, dfs)):
                # Update the qubit frequency
                update_frequency(q.xy.name, df + q.xy.intermediate_frequency)

                # Play the saturation pulse
                q.xy.play(
                    operation,
                    amplitude_scale=operation_amp,
                    duration=operation_len,
                )
                align(q.xy.name, q.resonator.name)

                # # QUA macro the readout the state of the active resonators (defined in macros.py)
                # multiplexed_readout(qubits, I, I_st, Q, Q_st, sequential=False)
                # readout the resonator
                q.resonator.measure("readout", qua_vars=(I[i], Q[i]))

                # Wait for the qubit to decay to the ground state
                wait(machine.thermalization_time * u.ns)
                # save data
                save(I[i], I_st[i])
                save(Q[i], Q_st[i])
        align(*([q.xy.name for q in qubits] + [q.resonator.name for q in qubits]))      
                    
    with stream_processing():
        n_st.save("n")
        for i in range(num_qubits):
            I_st[i].buffer(len(dfs)).average().save(f"I{i + 1}")
            Q_st[i].buffer(len(dfs)).average().save(f"Q{i + 1}")


# %%
###########################
# Run or Simulate Program #
###########################
simulate = node.parameters.simulate

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=10_000)  # In clock cycles = 4ns
    job = qmm.simulate(config, qubit_spec, simulation_config)
    job.get_simulated_samples().con1.plot()
    node.results = {"figure": plt.gcf()}
else:
    # Open the quantum machine
    qm = qmm.open_qm(config)
    # Calibrate the active qubits
    # machine.calibrate_octave_ports(qm)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(qubit_spec)
    # Get results from QUA program
    data_list = ["n"] + sum([[f"I{i + 1}", f"Q{i + 1}"] for i in range(num_qubits)], [])
    results = fetching_tool(job, data_list, mode="live")
    # Live plotting
    fig = plt.figure()
    interrupt_on_close(fig, job)  # Interrupts the job when closing the figure
    while results.is_processing():
        # Fetch results
        fetched_data = results.fetch_all()
        n = fetched_data[0]
        I = fetched_data[1::2]
        Q = fetched_data[2::2]

        # Progress bar
        progress_counter(n, n_avg, start_time=results.start_time)

        plt.suptitle("Qubit spectroscopy")
        s_data = []
        for i, q in enumerate(qubits):
            s = u.demod2volts(I[i] + 1j * Q[i], q.resonator.operations["readout"].length)
            s_data.append(s)
            plt.subplot(2, num_qubits, i + 1)
            plt.cla()
            plt.plot(
                (q.xy.LO_frequency + q.xy.intermediate_frequency + dfs) / u.MHz,
                np.abs(s),
            )
            plt.grid(True)
            plt.ylabel(r"R=$\sqrt{I^2 + Q^2}$ [V]")
            plt.title(f"{q.name} (f_01: {q.xy.rf_frequency / u.MHz} MHz)")
            plt.subplot(2, num_qubits, num_qubits + i + 1)
            plt.cla()
            plt.plot(
                (q.xy.LO_frequency + q.xy.intermediate_frequency + dfs) / u.MHz,
                np.unwrap(np.angle(s)),
            )
            plt.grid(True)
            plt.ylabel("Phase [rad]")
            plt.xlabel(f"{q.name} detuning [MHz]")
            plt.plot((q.xy.LO_frequency + q.xy.intermediate_frequency) / u.MHz, 0.0, "r*")

        plt.tight_layout()
        plt.pause(0.1)

    # Close the quantum machines at the end in order to put all flux biases to 0 so that the fridge doesn't heat-up
    qm.close()

    # # Save data from the node
    # data = {}
    # for i, q in enumerate(qubits):
    #     data[f"{q.name}_frequency"] = dfs + q.xy.intermediate_frequency
    #     data[f"{q.name}_R"] = np.abs(s_data[i])
    #     data[f"{q.name}_phase"] = np.angle(s_data[i])
    # data["figure"] = fig

    # fig_analysis = plt.figure()
    # plt.suptitle("Qubit spectroscopy")
    # # Fit the results to extract the resonance frequency
    # for i, q in enumerate(qubits):
        # try:
        #     from qualang_tools.plot.fitting import Fit

    #         fit = Fit()
    #         plt.subplot(1, num_qubits, i + 1)
            # res = fit.reflection_resonator_spectroscopy(
            #     (q.xy.LO_frequency + q.xy.intermediate_frequency + dfs) / u.MHz,
            #     -np.unwrap(np.angle(s_data[i])),
            #     plot=True,
            # )
    #         plt.legend((f"f = {res['f'][0]:.3f} MHz",))
    #         plt.xlabel(f"{q.name} IF [MHz]")
    #         plt.ylabel(r"R=$\sqrt{I^2 + Q^2}$ [V]")
    #         plt.title(f"{q.name}")

    #         # q.xy.intermediate_frequency = int(res["f"][0] * u.MHz)
    #         data[f"{q.name}"] = {
    #             "res_if": q.xy.intermediate_frequency,
    #             "fit_successful": True,
    #         }

    #         plt.tight_layout()
    #         data["fit_figure"] = fig_analysis

    #     except Exception:
    #         data[f"{q.name}"] = {"successful_fit": False}
    #         pass

    # plt.show()
    # # additional files
    # # Save data from the node
    # node_save(machine, "qubit_spectroscopy", data, additional_files=True)

# %%
if not simulate:
    handles = job.result_handles
    ds = fetch_results_as_xarray(handles, qubits, {"freq": dfs})
    ds = ds.assign({'IQ_abs': np.sqrt(ds['I'] ** 2 + ds['Q'] ** 2)})

    def abs_freq(q):
        def foo(freq):
            return freq + q.xy.intermediate_frequency + q.xy.LO_frequency
        return foo
    ds = ds.assign_coords({'freq_full' : (['qubit','freq'],np.array([abs_freq(q)(dfs) for q in qubits]))})
    ds = ds.assign({'phase': np.arctan2(ds.Q,ds.I)})

    ds.freq_full.attrs['long_name'] = 'Frequency'
    ds.freq_full.attrs['units'] = 'GHz'

    node.results = {}
    node.results['ds'] = ds

# %%
if not simulate:
    from lib.fit import peaks_dips

    # search for frequency in whihc the amplitude as farthest from the mean to indicate the approximate location of the peak
    shifts = np.abs((ds.IQ_abs-ds.IQ_abs.mean(dim = 'freq'))).idxmax(dim = 'freq')

    # approximate peak freqeuency
    abs_freqs = dict([(q.name, shifts.sel(qubit = q.name).values + q.xy.intermediate_frequency + q.xy.LO_frequency) for q in qubits])

    # the roration angle to align the meaningfull data with I axis
    angle =  np.arctan2(ds.sel(freq = shifts).Q - ds.Q.mean(dim = 'freq'), ds.sel(freq = shifts).I - ds.I.mean(dim = 'freq'))

    # rotate the data to the new I axis
    ds = ds.assign({'I_rot' :  np.real(ds.IQ_abs * np.exp(1j * (ds.phase - angle)  ))})

    # find the peak with minimal prominence as defined, if no such peak found, returns nan
    result = peaks_dips(ds.I_rot,dim = 'freq',prominence_factor=5)

    # extract the qubit frequency
    abs_freqs = dict([(q.name, result.sel(qubit= q.name).position.values + q.xy.intermediate_frequency + q.xy.LO_frequency) for q in qubits])

    fit_results = {}

    for q in qubits:
        fit_results[q.name] = {}
        if not np.isnan(result.sel(qubit = q.name).position.values):
            fit_results[q.name]['fit_successful'] = True
            Pi_length = q.xy.operations["x180"].length
            used_amp = q.xy.operations["saturation"].amplitude * operation_amp
            print(
            f"Drive frequency for {q.name} is {(result.sel(qubit = q.name).position.values + q.xy.intermediate_frequency + q.xy.LO_frequency)/1e9:.6f} GHz")
            fit_results[q.name]['drive_freq'] = result.sel(qubit = q.name).position.values + q.xy.intermediate_frequency + q.xy.LO_frequency
            print(
            f"(shift of {result.sel(qubit = q.name).position.values/1e6:.3f} MHz)")
            factor_cw = float(target_peak_width/result.sel(qubit = q.name).width.values)
            factor_pi = np.pi/(result.sel(qubit = q.name).width.values * Pi_length*1e-9)
            print(f"Found a peak width of {result.sel(qubit = q.name).width.values/1e6:.2f} MHz")
            print(f"To obtain a peak width of {target_peak_width/1e6:.1f} MHz the cw amplitude is modified by {factor_cw:.2f} to {factor_cw * used_amp / operation_amp * 1e3:.0f} mV")
            print(f"To obtain a Pi pulse at {Pi_length} nS the Rabi amplitude is modified by {factor_pi:.2f} to {factor_pi*used_amp*1e3:.0f} mV")
            print(f"readout angle for qubit {q.name}: {angle.sel(qubit = q.name).values:.4}")
            print()
        else:
            fit_results[q.name]['fit_successful'] = False
            print(f"Failed to find a peak for {q.name}")
            print()

    node.results['fit_results'] = fit_results

# %%
if not simulate:
    approx_peak = result.base_line + result.amplitude * (1 / (1 + ((ds.freq - result.position) / result.width) ** 2))

    grid_names = [f'{q.name}_0' for q in qubits]
    grid = QubitGrid(ds, grid_names)

    for ax, qubit in grid_iter(grid):
        (ds.assign_coords(freq_GHz  = ds.freq_full / 1e9).loc[qubit].I_rot*1e3).plot(ax = ax, x = 'freq_GHz')
        ax.plot([abs_freqs[qubit['qubit']]/1e9],[ds.loc[qubit].sel(
            freq = result.sel(qubit = qubit['qubit']).position.values, method  = 'nearest').
            I_rot*1e3],'.r')
        (approx_peak.assign_coords(freq_GHz  = ds.freq_full / 1e9).loc[qubit]*1e3).plot(ax = ax, x = 'freq_GHz',
                                                                                        linewidth = 0.5, linestyle = '--')
        ax.set_xlabel('Qubit freq [GHz]')
        ax.set_ylabel('Trans. amp. [mV]')
        ax.set_title(qubit['qubit'])
    grid.fig.suptitle('Qubit spectroscopy (amplitude)')

    plt.tight_layout()
    plt.show()
    node.results['figure'] = grid.fig


# %%
if not simulate:
    with node.record_state_updates():
        for q in qubits:
            fit_results[q.name] = {}
            if not np.isnan(result.sel(qubit = q.name).position.values):
                q.xy.intermediate_frequency += float(result.sel(qubit = q.name).position.values)

                prev_angle = q.resonator.operations["readout"].axis_angle
                if not  prev_angle:
                    prev_angle = 0.0
                q.resonator.operations["readout"].axis_angle = (prev_angle - angle.sel(qubit = q.name).values )% (2*np.pi)

            Pi_length = q.xy.operations["x180"].length
            used_amp = q.xy.operations["saturation"].amplitude * operation_amp
            factor_cw = float(target_peak_width/result.sel(qubit = q.name).width.values)
            factor_pi = np.pi/(result.sel(qubit = q.name).width.values * Pi_length*1e-9)
            if factor_cw*used_amp/operation_amp < 0.5:
                q.xy.operations["saturation"].amplitude = factor_cw*used_amp/operation_amp
            else:
                q.xy.operations["saturation"].amplitude = 0.5

            if factor_pi*used_amp < 0.3:
                q.xy.operations["x180"].amplitude = factor_pi*used_amp
            elif factor_pi*used_amp >= 0.3:
                q.xy.operations["x180"].amplitude = 0.3

# %%
node.results['initial_parameters'] = node.parameters.model_dump()
node.machine = machine
node.save()
