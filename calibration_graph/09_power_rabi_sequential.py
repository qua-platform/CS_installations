# %%
"""
POWER RABI WITH ERROR AMPLIFICATION
This sequence involves repeatedly executing the qubit pulse (such as x180, square_pi, or similar) 'N' times and
measuring the state of the resonator across different qubit pulse amplitudes and number of pulses.
By doing so, the effect of amplitude inaccuracies is amplified, enabling a more precise measurement of the pi pulse
amplitude. The results are then analyzed to determine the qubit pulse amplitude suitable for the selected duration.

Prerequisites:
    - Having found the resonance frequency of the resonator coupled to the qubit under study (resonator_spectroscopy).
    - Having calibrated the IQ mixer connected to the qubit drive line (external mixer or Octave port)
    - Having found the rough qubit frequency and pi pulse duration (rabi_chevron_duration or time_rabi).
    - Set the qubit frequency, desired pi pulse duration and rough pi pulse amplitude in the state.
    - Set the desired flux bias

Next steps before going to the next node:
    - Update the qubit pulse amplitude (pi_amp) in the state.
    - Save the current state by calling machine.save("quam")
"""

from pathlib import Path

from qm.qua import *
from qm import SimulationConfig
from qualang_tools.results import progress_counter, fetching_tool
from qualang_tools.plot import interrupt_on_close
from qualang_tools.loops import from_array
from qualang_tools.units import unit
from quam_libs.components import QuAM
from quam_libs.macros import qua_declaration, multiplexed_readout, node_save

import matplotlib.pyplot as plt
import numpy as np

import matplotlib
from lib.plot_utils import QubitGrid, grid_iter
from lib.save_utils import fetch_results_as_xarray
from lib.fit import fit_oscillation, oscillation

matplotlib.use("TKAgg")


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
qubits = machine.active_qubits
num_qubits = len(qubits)

###################
# The QUA program #
###################

operation = "x180"  # The qubit operation to play
n_avg = 500  # The number of averages
flux_point = "joint"  # "independent", "joint" or "zero"

# # Pulse amplitude sweep (as a pre-factor of the qubit pulse amplitude) - must be within [-2; 2)
# amps = np.arange(0.8, 1.2, 0.005)
# # Number of applied Rabi pulses sweep
# N_pi = 10  # Maximum number of qubit pulses

# Pulse amplitude sweep (as a pre-factor of the qubit pulse amplitude) - must be within [-2; 2)
amps = np.arange(0.0,2.0, 0.025)
# Number of applied Rabi pulses sweep
N_pi = 1  # Maximum number of qubit pulses

N_pi_vec = np.linspace(1, N_pi, N_pi).astype("int")[::2]

with program() as power_rabi:
    I, I_st, Q, Q_st, n, n_st = qua_declaration(num_qubits=num_qubits)
    a = declare(fixed)  # QUA variable for the qubit drive amplitude pre-factor
    npi = declare(int)  # QUA variable for the number of qubit pulses
    count = declare(int)  # QUA variable for counting the qubit pulses

    for i, qubit in enumerate(qubits):
        # Bring the active qubits to the minimum frequency point
        if flux_point == "independent":
            machine.apply_all_flux_to_min()
            qubit.z.to_independent_idle()
        elif flux_point == "joint":
            machine.apply_all_flux_to_joint_idle()
        else:
            machine.apply_all_flux_to_zero()
        wait(1000)
        
        with for_(n, 0, n < n_avg, n + 1):
            save(n, n_st)
            with for_(*from_array(npi, N_pi_vec)):
                with for_(*from_array(a, amps)):
                    # Loop for error amplification (perform many qubit pulses)
                    with for_(count, 0, count < npi, count + 1):
                        qubit.xy.play("x180", amplitude_scale=a)
                    align()
                    qubit.resonator.measure("readout", qua_vars=(I[i], Q[i]))
                    save(I[i], I_st[i])
                    save(Q[i], Q_st[i])
                    wait(machine.thermalization_time * u.ns)

    with stream_processing():
        n_st.save("n")
        for i, qubit in enumerate(qubits):
            I_st[i].buffer(len(amps)).buffer(np.ceil(N_pi / 2)).average().save(f"I{i + 1}")
            Q_st[i].buffer(len(amps)).buffer(np.ceil(N_pi / 2)).average().save(f"Q{i + 1}")


###########################
# Run or Simulate Program #
###########################
simulate = False

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=10_000)  # In clock cycles = 4ns
    job = qmm.simulate(config, power_rabi, simulation_config)
    job.get_simulated_samples().con1.plot()

else:
    # Open the quantum machine
    qm = qmm.open_qm(config)
    # Calibrate the active qubits
    # machine.calibrate_octave_ports(qm)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(power_rabi)
    # Get results from QUA program
    data_list = ["n"] + sum([[f"I{i + 1}", f"Q{i + 1}"] for i in range(num_qubits)], [])
    results = fetching_tool(job, data_list, mode="live")
    # Live plotting
    # fig = plt.figure()
    # interrupt_on_close(fig, job)  # Interrupts the job when closing the figure
    while results.is_processing():
        fetched_data = results.fetch_all()
        n = fetched_data[0]
        I = fetched_data[1::2]
        Q = fetched_data[2::2]
        progress_counter(n, n_avg, start_time=results.start_time)
        # I_volts, Q_volts = [], []
        # # Plot results
        # for i, qubit in enumerate(qubits):
        #     if I[i].shape[0] > 1:
        #         # Convert into volts
        #         I_volts.append(u.demod2volts(I[i], qubit.resonator.operations["readout"].length))
        #         Q_volts.append(u.demod2volts(Q[i], qubit.resonator.operations["readout"].length))
        #         # Plot
        #         plt.suptitle("Power Rabi with error amplification")
        #         plt.subplot(3, num_qubits, i + 1)
        #         plt.cla()
        #         plt.pcolor(
        #             amps * qubit.xy.operations[operation].amplitude,
        #             N_pi_vec,
        #             I_volts[i],
        #         )
        #         plt.title(f"{qubit.name} - I")
        #         plt.subplot(3, num_qubits, i + num_qubits + 1)
        #         plt.cla()
        #         plt.pcolor(
        #             amps * qubit.xy.operations[operation].amplitude,
        #             N_pi_vec,
        #             Q_volts[i],
        #         )
        #         plt.title(f"{qubit.name} - Q")
        #         plt.xlabel("Qubit pulse amplitude [V]")
        #         plt.ylabel("Number of Rabi pulses")
        #         plt.subplot(3, num_qubits, i + 2 * num_qubits + 1)
        #         plt.cla()
        #         plt.plot(
        #             amps * qubit.xy.operations[operation].amplitude,
        #             np.sum(I_volts[i], axis=0),
        #         )
        #         plt.axvline(qubit.xy.operations[operation].amplitude, color="k")
        #         plt.xlabel("Rabi pulse amplitude [V]")
        #         plt.ylabel(r"$\Sigma$ of Rabi pulses")

        #     else:
        #         plt.suptitle("Power Rabi")
        #         plt.subplot(2, num_qubits, i + 1)
        #         plt.cla()
        #         plt.plot(amps * qubit.xy.operations[operation].amplitude, I_volts[i])
        #         plt.title(f"{qubit.name}")
        #         plt.ylabel("I quadrature [V]")
        #         plt.subplot(2, num_qubits, i + num_qubits + 1)
        #         plt.cla()
        #         plt.plot(amps * qubit.xy.operations[operation].amplitude, Q_volts[i])
        #         plt.xlabel("Qubit Pulse Amplitude [V]")
        #         plt.ylabel("Q quadrature [V]")

        # plt.tight_layout()
        # plt.pause(0.1)

    # Close the quantum machines at the end in order to put all flux biases to 0 so that the fridge doesn't heat-up
    qm.close()
    # data = {}
    # for i, qubit in enumerate(qubits):
    #     data[f"{qubit.name}_amplitude"] = amps * qubit.xy.operations[operation].amplitude
    #     data[f"{qubit.name}_I"] = np.abs(I_volts[i])
    #     data[f"{qubit.name}_Q"] = np.angle(Q_volts[i])

    #     # Get the optimal pi pulse amplitude when doing error amplification
    #     try:
    #         qubit.xy.operations[operation].amplitude = (
    #             amps[np.argmax(np.sum(I_volts[i], axis=0))] * qubit.xy.operations[operation].amplitude
    #         )

    #         data[f"{qubit.name}"] = {
    #             "x180_amplitude": qubit.xy.operations[operation].amplitude,
    #             "successful_fit": True,
    #         }

    #     except (Exception,):
    #         data[f"{qubit.name}"] = {"successful_fit": True}
    #         pass

    # data["figure"] = fig
    # Save data from the node
    plt.show()
    # node_save(machine, "power_rabi", data, additional_files=True)

# %%
handles = job.result_handles
ds = fetch_results_as_xarray(handles, qubits, {"amp": amps, "N": N_pi_vec})
# %%
def abs_amp(q):
    def foo(amp):
        return q.xy.operations[operation].amplitude * amp
    return foo

ds = ds.assign_coords({'abs_amp' : (['qubit','amp'],np.array([abs_amp(q)(amps) for q in qubits]))})
data = {}
data['ds'] = ds

# %%
fit_results = {}

if N_pi == 1:
    fit = fit_oscillation(ds.I, 'amp')
    fit_evals = oscillation(ds.amp,fit.sel(fit_vals = 'a'),fit.sel(fit_vals = 'f'),fit.sel(fit_vals = 'phi'),fit.sel(fit_vals = 'offset'))
    for q in qubits:
        fit_results[q.name] = {}
        f_fit = fit.loc[q.name].sel(fit_vals='f')
        phi_fit = fit.loc[q.name].sel(fit_vals='phi')
        phi_fit = phi_fit - np.pi * (phi_fit > np.pi/2)
        factor = float(1.0 * (np.pi - phi_fit)/ (2* np.pi* f_fit))
        new_pi_amp = q.xy.operations[operation].amplitude * factor
        if new_pi_amp < 0.3:
            print(f"amplitude for Pi pulse is modified by a factor of {factor:.2f}")
            print(f"new amplitude is {1e3 * new_pi_amp:.2f} mV \n")
            fit_results[q.name]['Pi_amplitude'] = new_pi_amp
        else: 
            print(f"Fitted amplitude too high, new amplitude is 300 mV \n")
            fit_results[q.name]['Pi_amplitude'] = 0.3
    data['fit_results'] = fit_results# %%

elif N_pi > 1:
    I_n=ds.I.mean(dim='N')
    if N_pi_vec[0] % 2 == 0:
        datamaxIndx = I_n.argmin(dim='amp')
    else:
        datamaxIndx = I_n.argmax(dim='amp')
    for q in qubits:
        new_pi_amp = ds.abs_amp.sel(qubit = q.name)[datamaxIndx.sel(qubit = q.name)]
        fit_results[q.name] = {}
        if new_pi_amp < 0.3:
            fit_results[q.name]['Pi_amplitude'] = new_pi_amp    
            print(f"amplitude for Pi pulse is modified by a factor of {I_n.idxmax(dim='amp').sel(qubit = q.name):.2f}")
            print(f"new amplitude is {1e3 * new_pi_amp:.2f} mV \n")
        else: 
            print(f"Fitted amplitude too high, new amplitude is 300 mV \n")
            fit_results[q.name]['Pi_amplitude'] = 0.3
# %%

grid = QubitGrid(ds, [f'q-{i}_0' for i in range(num_qubits)])
for ax, qubit in grid_iter(grid):
    if N_pi == 1:
        (ds.assign_coords(amp_mV  = ds.abs_amp *1e3).loc[qubit].I*1e3).plot(ax = ax, x = 'amp_mV')
        ax.plot(ds.abs_amp.loc[qubit]*1e3, 1e3*fit_evals.loc[qubit][0])
        ax.set_ylabel('Trans. amp. I [mV]')
    elif N_pi > 1:
        (ds.assign_coords(amp_mV  = ds.abs_amp *1e3).loc[qubit].I*1e3).plot(ax = ax, x = 'amp_mV', y = 'N')
        ax.axvline(1e3*ds.abs_amp.loc[qubit][datamaxIndx.loc[qubit]], color = 'r')
        ax.set_ylabel('num. of pulses')
    ax.set_xlabel('Amplitude [mV]')
    ax.set_title(qubit['qubit'])
grid.fig.suptitle('Rabi : I vs. amplitude')
plt.tight_layout()
plt.show()
data['figure'] = grid.fig

# %%
for q in qubits:
    q.xy.operations[operation].amplitude = fit_results[q.name]['Pi_amplitude']

# %%
node_save(machine, "power_rabi", data, additional_files=True)
# %%
