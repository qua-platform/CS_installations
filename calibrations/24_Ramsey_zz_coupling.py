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

from pathlib import Path

from qm.qua import *
from qm import SimulationConfig
from qualang_tools.results import progress_counter, fetching_tool
from qualang_tools.plot import interrupt_on_close
from qualang_tools.loops import from_array, get_equivalent_log_array
from qualang_tools.units import unit
from quam_libs.components import QuAM, Transmon
from quam_libs.macros import qua_declaration, multiplexed_readout, node_save

import matplotlib.pyplot as plt
import numpy as np

import matplotlib

matplotlib.use("TKAgg")


###################################################
#  Load QuAM and open Communication with the QOP  #
###################################################
# Class containing tools to help handle units and conversions.
u = unit(coerce_to_integer=True)
# Instantiate the QuAM class from the state file
machine = QuAM.load()
# Generate the OPX and Octave configurations
config = machine.generate_config()
# Open Communication with the QOP
qmm = machine.connect()

# Get the relevant QuAM components
num_qubits_full = len(machine.active_qubits)

q1 = machine.qubits["q4"]
q2 = machine.qubits["q5"]
coupler = (q1 @ q2).coupler
qubits = [q1, q2]
num_qubits = len(qubits)
q1_idx = machine.active_qubit_names.index(q1.name)
q2_idx = machine.active_qubit_names.index(q2.name)
states = [0, 1]

###################
# The QUA program #
###################
n_avg = 4

# Dephasing time sweep (in clock cycles = 4ns) - minimum is 4 clock cycles
idle_times = np.arange(4, 200, 4)

# The flux bias sweep in V
#dcs_coupler = np.linspace(-0.01, 0.01, 3) # -0.034
dcs_coupler = np.linspace(-0.036, -0.032, 3) # -0.034
dcs_q1 = 0.0175 + 0.05 * dcs_coupler # 0.0175 + 0.05 * -0.034
dcs_q2 = q2.z.min_offset * np.ones(len(dcs_coupler))
num_dcs = len(dcs_coupler)
assert len(dcs_q1) == num_dcs
assert len(dcs_q2) == num_dcs

# Detuning converted into virtual Z-rotations to observe Ramsey oscillation and get the qubit frequency
detuning = 1e6


def play_ramsey_zz_multiplexed(qt: Transmon, qc: Transmon, st, t):
    # Rotate the frame of the second x90 gate to implement a virtual Z-rotation
    # 4*tau because tau was in clock cycles and 1e-9 because tau is ns
    assign(phi, Cast.mul_fixed_by_int(detuning * 1e-9, 4 * t))
    align()
    # Strict_timing ensures that the sequence will be played without gaps
    # with strict_timing_():
    with if_(st == 1):
        qc.xy.play("x180")
        align()
        # for q in qubits:
        #     if q.name != qc.name:
        #         q.xy.wait(qc.xy.operations["x180"].length * u.ns)
    qt.xy.play("x90")
    qt.xy.frame_rotation_2pi(phi)
    qt.xy.wait(t)
    qt.xy.play("x90")

    # Align the elements to measure after playing the qubit pulse.
    align()
    # Measure the state of the resonators
    multiplexed_readout(machine.active_qubits, I, I_st, Q, Q_st)
    # Wait for the qubits to decay to the ground state
    wait(machine.thermalization_time * u.ns)
    # Reset the frame of the qubits in order not to accumulate rotations
    reset_frame(qt.xy.name)


with program() as ramsey:
    I, I_st, Q, Q_st, n, n_st = qua_declaration(num_qubits=num_qubits_full)
    t = declare(int)  # QUA variable for the idle time
    phi = declare(fixed)  # QUA variable for dephasing the second pi/2 pulse (virtual Z-rotation)
    dc_coupler = declare(fixed)  # QUA variable for the coupler bias
    dc_q1 = declare(fixed)  # QUA variable for q1 bias
    dc_q2 = declare(fixed)  # QUA variable for q2 bias
    st = declare(int)

    # Bring the active qubits to the minimum frequency point
    machine.apply_all_flux_to_min()

    with for_(n, 0, n < n_avg, n + 1):
        save(n, n_st)

        with for_each_((dc_coupler, dc_q1, dc_q2), (dcs_coupler, dcs_q1, dcs_q2)):
            coupler.set_dc_offset(dc_coupler)
            q1.z.set_dc_offset(dc_q1)
            q2.z.set_dc_offset(dc_q2)
            wait(100)

            with for_(*from_array(t, idle_times)):
                with for_each_(st, states):
                    # ramsey on q1 with q2 in 0 or 1
                    play_ramsey_zz_multiplexed(qt=q1, qc=q2, st=st, t=t)

                    # ramsey on q2 with q1 in 0 or 1
                    play_ramsey_zz_multiplexed(qt=q2, qc=q1, st=st, t=t)

    with stream_processing():
        n_st.save("n")
        for i in range(num_qubits_full):
            I_st[i].buffer(2).buffer(len(states)).buffer(len(idle_times)).buffer(num_dcs).average().save(f"I{i + 1}")
            Q_st[i].buffer(2).buffer(len(states)).buffer(len(idle_times)).buffer(num_dcs).average().save(f"Q{i + 1}")


###########################
# Run or Simulate Program #
###########################
simulate = False

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=20_000)  # In clock cycles = 4ns
    job = qmm.simulate(config, ramsey, simulation_config)
    job.get_simulated_samples().con1.plot()
    plt.show()
else:
    from qm import generate_qua_script

    sourceFile = open('debug.py', 'w')
    print(generate_qua_script(ramsey, config), file=sourceFile) 
    sourceFile.close()

    # Open the quantum machine
    qm = qmm.open_qm(config)
    # Calibrate the active qubits
    # machine.calibrate_octave_ports(qm)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(ramsey)
    # Get results from QUA program
    data_list = ["n"] + sum([[f"I{i + 1}", f"Q{i + 1}"] for i in [q1_idx, q2_idx]], [])
    results = fetching_tool(job, data_list, mode="live")
    # Live plotting
    fig, axes = plt.subplots(2, 2 * num_qubits, figsize=(2 * 4 * num_qubits, 8))
    interrupt_on_close(fig, job)  # Interrupts the job when closing the figure
    while results.is_processing():
        # Fetch results
        fetched_data = results.fetch_all()
        n = fetched_data[0]
        I_data = fetched_data[1::2]
        Q_data = fetched_data[2::2]
        # Convert the results into Volts
        I_volts = [
            u.demod2volts(I, qubit.resonator.operations["readout"].length)
            for I, qubit in zip(I_data, qubits)
        ]
        Q_volts = [
            u.demod2volts(Q, qubit.resonator.operations["readout"].length)
            for Q, qubit in zip(Q_data, qubits)
        ]
        # Progress bar
        progress_counter(n, n_avg, start_time=results.start_time)
        # Plot results
        plt.suptitle("Ramsey_ZZ")
        for i, qubit in enumerate(qubits):
            for j, state in enumerate(states):
                k = 2 * i + j
                axes[0, k].cla()
                axes[0, k].pcolor(4 * idle_times, dcs_coupler, I_volts[i][:, :, j, i])
                axes[0, k].set_ylabel("coupler bias [V]")
                axes[0, k].set_title(f"I: {qubit.name} ({qubits[(i + 1) % 2].name}=|{state}>)")
                axes[1, k].cla()
                axes[1, k].pcolor(4 * idle_times, dcs_coupler, Q_volts[i][:, :, j, i])
                axes[1, k].set_xlabel("Idle time [ns]")
                axes[1, k].set_ylabel("coupler bias [V]")
                axes[1, k].set_title(f"Q: {qubit.name} ({qubits[(i + 1) % 2].name}=|{state}>)")
        plt.tight_layout()
        plt.pause(0.1)

    # Close the quantum machines at the end in order to put all flux biases to 0 so that the fridge doesn't heat-up
    qm.close()

    # Save data from the node
    data = {}
    for i, (qubit, dcs_q) in enumerate(zip(qubits, [dcs_q1, dcs_q2])):
        data[f"{qubit.name}_idle_times"] = 4 * idle_times
        data[f"{qubit.name}_dc"] = dcs_q
        data[f"{qubit.name}_I"] = I_volts[i]
        data[f"{qubit.name}_Q"] = Q_volts[i]
    data[f"{coupler.name}_dcs"] = dcs_coupler
    data["figure"] = fig

    fit_result = {
         "I": np.zeros((len(qubits), len(dcs_coupler), len(states))),
         "Q": np.zeros((len(qubits), len(dcs_coupler), len(states))),
    }
    # Fit data to extract the qubits frequency and T2*
    for i, qubit in enumerate(qubits):
        for j, dc in enumerate(dcs_coupler):
            fig_analysis1 = plt.figure()
            plt.suptitle(f"Ramsey_ZZ at coupler {dc} V")
            for k, state in enumerate(states):
                try:
                    from qualang_tools.plot.fitting import Fit

                    plt.subplot(2, 2, 2 * k + 1)
                    fit_I = Fit().ramsey(4 * idle_times, I_volts[i][j, :, k, i], plot=True)
                    fit_detuning = int(fit_I['f'][0] * u.GHz - detuning) # fit_I["f"][0] * u.GHz - detuning if detuning >= 0 else detuning + fit_I["f"][0] * u.GHz
                    fit_result["I"][i, j, k] = fit_detuning
                    plt.xlabel("Idle time [ns]")
                    plt.ylabel("I [V]")
                    plt.title(f"{qubit.name} ({qubits[(i + 1) % 2].name}=|{state}>): I")
                    plt.legend((f"T2* = {int(fit_I['T2'][0])} ns\n df = {fit_detuning / u.kHz} kHz",))

                    plt.subplot(2, 2, 2 * k + 2)
                    fit_Q = Fit().ramsey(4 * idle_times, Q_volts[i][j, :, k, i], plot=True)
                    fit_detuning = int(fit_Q['f'][0] * u.GHz - detuning) # fit_I["f"][0] * u.GHz - detuning if detuning >= 0 else detuning + fit_I["f"][0] * u.GHz
                    fit_result["Q"][i, j, k] = fit_detuning
                    plt.xlabel("Idle time [ns]")
                    plt.ylabel("Q [V]")
                    plt.title(f"{qubit.name} ({qubits[(i + 1) % 2].name}=|{state}>): Q")
                    plt.legend((f"T2* = {int(fit_Q['T2'][0])} ns\n df = {fit_detuning / u.kHz} kHz",))

                    plt.tight_layout()
                    # Update the state
                    # qubit_detuning = fit_I["f"][0] * u.GHz - detuning if detuning >= 0 else detuning + fit_I["f"][0] * u.GHz
                    # qubit.T2ramsey = int(fit_I["T2"][0])
                    # qubit.xy.RF_frequency -= qubit_detuning
                    suffix = f"{qubit.name}_with_{qubits[(i + 1) % 2].name}_coupler_bias={dc}V_state={state}".replace('.', '-')
                    # data[f"{qubit.name}_{suffix}"] = {
                    #     "q_target": qubit.name,
                    #     "q_control": qubits[(i + 1) % 2].name,
                    #     "q_control_state": state,
                    #     "coupler_bias": dc,
                    #     "T2*": qubit.T2ramsey,
                    #     "if_01": qubit.xy.intermediate_frequency,
                    #     "successful_fit": True,
                    # }
                    # print(f"Detuning to add to {qubit.name}: {-qubit_detuning / u.kHz:.3f} kHz")
                    data[f"figure_analysis_{suffix}"] = fig_analysis1
                except (Exception,):
                    # data[f"{qubit.name}"] = {"successful_fit": False}
                    pass

    data["fit_result"] = fit_result
    
    fig_analysis2, axes = plt.subplots(2, 2, figsize=(12, 6), sharey="row")
    for k, quad in enumerate(["I", "Q"]):
        legends = []
        for i, qubit in enumerate(qubits):
            for state in states:
                axes[0, k].plot(dcs_coupler, fit_result[quad][i, :, state] / u.kHz)
                legends.append(f"{qubit.name} ({qubits[(i + 1) % 2].name}=|{state}>)")
        axes[0, k].set_xlabel("Coupler Bias [ns]")
        axes[0, k].set_ylabel("Frequency [kHz]")
        axes[0, k].set_title(f"fit detuning: {quad}")
        axes[0, k].legend(legends)

        for i, qubit in enumerate(qubits):
            axes[1, k].plot(dcs_coupler, (fit_result["I"][i, :, 1] - fit_result["I"][i, :, 0]) / u.kHz)
            legends.append(f"{qubit.name}")
        axes[1, k].set_xlabel("Coupler Bias [ns]")
        axes[1, k].set_ylabel("Frequency [kHz]")
        axes[1, k].set_title(f"ZZ Coupling: {quad}")
        axes[1, k].legend([q.name for q in qubits])
    plt.tight_layout()
    data[f"figure_analysis_zz_coupling"] = fig_analysis2
    
    plt.show()
    
    # Save data from the node
    node_save(machine, "ramsey_zz_coupling", data, additional_files=True)

# %%
