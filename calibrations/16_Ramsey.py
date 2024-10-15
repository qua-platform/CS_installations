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
from quam_libs.components import QuAM
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
qubits = machine.active_qubits
num_qubits = len(qubits)
q3 = machine.qubits["q3"]
q4 = machine.qubits["q4"]
q5 = machine.qubits["q5"]
coupler = (q4 @ q5).coupler
apply_pi = True
# qubits_wo_q5 = [q for q in machine.active_qubits if q.name != "q5"]
# qubits_wo_q3 = [q for q in machine.active_qubits if q.name != "q3"]

###################
# The QUA program #
###################
n_avg = 400

# Dephasing time sweep (in clock cycles = 4ns) - minimum is 4 clock cycles
idle_times = np.arange(4, 300, 4)

# Detuning converted into virtual Z-rotations to observe Ramsey oscillation and get the qubit frequency
detuning = 2e6

with program() as ramsey:
    I, I_st, Q, Q_st, n, n_st = qua_declaration(num_qubits=num_qubits)
    t = declare(int)  # QUA variable for the idle time
    phi = declare(
        fixed
    )  # QUA variable for dephasing the second pi/2 pulse (virtual Z-rotation)

    # Bring the active qubits to the minimum frequency point
    machine.apply_all_flux_to_min()
    coupler.set_dc_offset(0.0)
    # # measure T2* at certain flux-point
    # coupler.set_dc_offset(-0.039)
    # q4.z.set_dc_offset(q4.z.min_offset + 0.05 * -0.039)  

    with for_(n, 0, n < n_avg, n + 1):
        save(n, n_st)

        with for_(*from_array(t, idle_times)):
            # Rotate the frame of the second x90 gate to implement a virtual Z-rotation
            # 4*tau because tau was in clock cycles and 1e-9 because tau is ns
            assign(phi, Cast.mul_fixed_by_int(detuning * 1e-9, 4 * t))
            align()
            # Strict_timing ensures that the sequence will be played without gaps
            with strict_timing_():
                if apply_pi:
                    q4.xy.play("x180")
                    for qubit in qubits:
                        if qubit.name != "q4":
                            qubit.xy.wait(q4.xy.operations["x180"].length * u.ns)
                    # wait(q5.xy.operations["x180"].length * u.ns, [q.xy.operations["x180"].name for q in machine.active_qubits if q.name != "q5"])

                # for qubit in [machine.qubits["q4"]]:
                for qubit in qubits:
                    qubit.xy.play("x90")
                    qubit.xy.frame_rotation_2pi(phi)
                    qubit.xy.wait(t)
                    qubit.xy.play("x90")

            # Align the elements to measure after playing the qubit pulse.
            align()
            # Measure the state of the resonators
            multiplexed_readout(qubits, I, I_st, Q, Q_st)
            # Wait for the qubits to decay to the ground state
            wait(machine.thermalization_time * u.ns)
            # Reset the frame of the qubits in order not to accumulate rotations
            for qubit in qubits:
                reset_frame(qubit.xy.name)

    with stream_processing():
        n_st.save("n")
        for i in range(num_qubits):
            I_st[i].buffer(len(idle_times)).average().save(f"I{i + 1}")
            Q_st[i].buffer(len(idle_times)).average().save(f"Q{i + 1}")


###########################
# Run or Simulate Program #
###########################
simulate = False

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=10_000)  # In clock cycles = 4ns
    job = qmm.simulate(config, ramsey, simulation_config)
    job.get_simulated_samples().con1.plot()
else:
    # Open the quantum machine
    qm = qmm.open_qm(config)
    # Calibrate the active qubits
    # machine.calibrate_octave_ports(qm)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(ramsey)
    # Get results from QUA program
    data_list = sum([[f"I{i + 1}", f"Q{i + 1}"] for i in range(num_qubits)], ["n"])
    results = fetching_tool(job, data_list, mode="live")
    # Live plotting
    fig, axes = plt.subplots(2, num_qubits, figsize=(4 * num_qubits, 8))
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
        plt.suptitle("Ramsey")
        for i, (ax, qubit) in enumerate(zip(axes.T, qubits)):
            ax[0].cla()
            ax[0].plot(4 * idle_times, I_volts[i])
            ax[0].set_ylabel("I [V]")
            ax[0].set_title(f"{qubit.name}")
            ax[1].cla()
            ax[1].plot(4 * idle_times, Q_volts[i])
            ax[1].set_xlabel("Idle time [ns]")
            ax[1].set_ylabel("Q [V]")
            ax[1].set_title(f"{qubit.name}")
        plt.tight_layout()
        plt.pause(0.1)

    # Close the quantum machines at the end in order to put all flux biases to 0 so that the fridge doesn't heat-up
    qm.close()

    # Save data from the node
    data = {}
    for i, qubit in enumerate(qubits):
        data[f"{qubit.name}_amplitude"] = 4 * idle_times
        data[f"{qubit.name}_I"] = np.abs(I_volts[i])
        data[f"{qubit.name}_Q"] = np.angle(Q_volts[i])
    data["figure"] = fig

    fig_analysis = plt.figure()
    plt.suptitle("Ramsey")
    # Fit data to extract the qubits frequency and T2*
    for i, qubit in enumerate(qubits):
        try:
            from qualang_tools.plot.fitting import Fit

            fit = Fit()
            plt.subplot(num_qubits, 1, i + 1)
            fit_I = fit.ramsey(4 * idle_times, I_volts[i], plot=True)
            plt.xlabel("Idle time [ns]")
            plt.ylabel("I [V]")
            plt.title(f"{qubit.name}")
            plt.legend(
                (
                    f"T2* = {int(fit_I['T2'][0])} ns\n df = {int(fit_I['f'][0] * u.GHz - detuning)/u.kHz} kHz",
                )
            )

            # Update the state
            qubit_detuning = fit_I["f"][0] * u.GHz - detuning if detuning >= 0 else detuning + fit_I["f"][0] * u.GHz
            # qubit.T2ramsey = int(fit_I["T2"][0])
            # qubit.xy.RF_frequency -= qubit_detuning
            data[f"{qubit.name}"] = {
                "T2*": qubit.T2ramsey,
                "if_01": qubit.xy.intermediate_frequency,
                "successful_fit": True,
            }
            print(f"Detuning to add to {qubit.name}: {-qubit_detuning / u.kHz:.3f} kHz")
            plt.tight_layout()
            data["figure_analysis"] = fig_analysis
        except (Exception,):
            data[f"{qubit.name}"] = {"successful_fit": False}
            pass
    plt.show()

    # Save data from the node
    node_save(machine, "ramsey", data, additional_files=True)

# %%
