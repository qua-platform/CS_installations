"""
        RF REFLECTOMETRY SPECTROSCOPY
The goal of this script is to perform the spectroscopy of the RF-reflectometry readout.
For this, the frequency of the element (pulser) used for reflectometry readout is being swept and the signal reflected
by the tank circuit is being acquired, demodulated and integrated by the OPX.

A global averaging is performed (averaging on the most outer loop) and the data is extracted while the program is running
to display the frequency response of the tank circuit with increasing SNR.

Prerequisites:
    - Connect the tank circuit to the corresponding output and input channels.

Before proceeding to the next node:
    - Update the config with the resonance frequency for reflectometry readout.
"""

from qm.qua import *
from qm import QuantumMachinesManager
from qm import SimulationConfig
from qm.qua import *
from qm import SimulationConfig
from quam_builder import Quam
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter
from qualang_tools.units import unit
from pathlib import Path
import numpy as np
from qualang_tools.results import progress_counter, fetching_tool
from qualang_tools.plot import interrupt_on_close
from qualang_tools.loops import from_array
import matplotlib.pyplot as plt
from scipy import signal
from qualang_tools.results.data_handler import DataHandler

machine = Quam.load("state.json")
u = unit(coerce_to_integer=True)


##################
#   Parameters   #
##################
# Parameters Definition
n_avg = 100  # Number of averaging loops
# The frequency axis
frequencies = np.linspace(-5 * u.MHz, 5 * u.MHz, 51)


###################
# The QUA program #
###################
with program() as reflectometry_spectro:
    I, I_st, Q, Q_st, n, n_st = machine.qua_declaration()
    df = declare(int)  # QUA variable for the frequency sweep

    with for_(n, 0, n < n_avg, n + 1):
        with for_(*from_array(df, frequencies)):
            for i, q in enumerate(machine.qubits):
                resonator = machine.qubits[q].resonator
                # Update the frequency of the tank_circuit element
                resonator.update_frequency(df + resonator.intermediate_frequency)
                # RF reflectometry: the voltage measured by the analog input 1 is recorded, demodulated at the readout
                # frequency and the integrated quadratures are stored in "I" and "Q"
                # Please choose the right "out1" or "out2" according to the connectivity
                # measure("readout", f"tank_circuit{i+1}", demod.full("cos", I[i], "out1"), demod.full("sin", Q[i], "out1"))
                resonator.measure("readout", qua_vars=(I[i], Q[i]))
                save(I[i], I_st[i])
                save(Q[i], Q_st[i])
                # Wait at each iteration in order to ensure that the data will not be transferred faster than 1 sample
                # per µs to the stream processing. Otherwise, the processor will receive the samples faster than it can
                # process them which can cause the OPX to crash.
                resonator.wait(1_000 * u.ns)  # in ns
        save(n, n_st)

    with stream_processing():
        for i, q in enumerate(machine.qubits):
            I_st[i].buffer(len(frequencies)).average().save(f"I{i+1}")
            Q_st[i].buffer(len(frequencies)).average().save(f"Q{i+1}")
        n_st.save("iteration")

#####################################
#  Open Communication with the QOP  #
#####################################
qmm = machine.connect()
config = machine.generate_config()
# Data to save
save_data_dict = {
    "n_avg": n_avg,
    "IF_frequencies": frequencies,
    "config": config,
}

#######################
# Simulate or execute #
#######################
simulate = False

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=10_000)  # In clock cycles = 4ns
    # Simulate blocks python until the simulation is done
    job = qmm.simulate(config, reflectometry_spectro, simulation_config)
    # Get the simulated samples
    samples = job.get_simulated_samples()
    # Plot the simulated samples
    samples.con1.plot()
    # Get the waveform report object
    waveform_report = job.get_simulated_waveform_report()
    # Cast the waveform report to a python dictionary
    waveform_dict = waveform_report.to_dict()
    # Visualize and save the waveform report
    waveform_report.create_plot(
        samples, plot=True, save_path=str(Path(__file__).resolve())
    )
else:
    # Open the quantum machine
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(reflectometry_spectro)
    # Get results from QUA program
    data_list = ["iteration"] + np.concatenate(
        [[f"I{i+1}", f"Q{i+1}"] for i in range(len(machine.qubits))]
    ).tolist()
    results = fetching_tool(job, data_list=data_list, mode="live")
    IQ_data = {}
    # Live plotting
    fig = plt.figure()
    interrupt_on_close(fig, job)  # Interrupts the job when closing the figure
    while results.is_processing():
        # Fetch results
        data = results.fetch_all()
        iteration = data[0]

        for i, q in enumerate(machine.qubits):
            IQ_data[f"tank_circuit{i+1}"] = {"I": data[2 * i + 1], "Q": data[2 * i + 2]}
            # Convert results into Volts
            S = u.demod2volts(
                IQ_data[f"tank_circuit{i+1}"]["I"]
                + 1j * IQ_data[f"tank_circuit{i+1}"]["Q"],
                machine.qubits[q].resonator.operations["readout"].length
                * (machine.qubits[q].resonator.opx_input.sampling_rate / 1e9),
                single_demod=True,
            )
            IQ_data[f"tank_circuit{i + 1}"]["R"] = np.abs(S)
            IQ_data[f"tank_circuit{i + 1}"]["phase"] = np.angle(S)
        # Progress bar
        progress_counter(iteration, n_avg, start_time=results.get_start_time())

        rows = int(np.ceil(np.sqrt(len(machine.qubits))))
        cols = int(np.ceil(len(machine.qubits) / rows))
        fig, axes = plt.subplots(rows, cols, figsize=(15, 10))
        fig.suptitle("Amplitude")
        for i, q in enumerate(machine.qubits):
            ax = axes[i // cols, i % cols]
            ax.plot(
                (frequencies + machine.qubits[q].resonator.intermediate_frequency)
                / u.MHz,
                IQ_data[f"tank_circuit{i + 1}"]["R"] / u.mV,
            )
            ax.set_xlabel("Frequency [MHz]")
            ax.set_ylabel("Demodulated amplitude [mV]")
            ax.set_title(f"tank_circuit{i + 1}")
        fig, axes = plt.subplots(rows, cols, figsize=(15, 10))
        fig.suptitle("Phase")
        for i, q in enumerate(machine.qubits):
            ax = axes[i // cols, i % cols]
            ax.plot(
                (frequencies + machine.qubits[q].resonator.intermediate_frequency)
                / u.MHz,
                signal.detrend(np.unwrap(IQ_data[f"tank_circuit{i + 1}"]["phase"])),
            )
            ax.set_xlabel("Frequency [MHz]")
            ax.set_ylabel("Demodulated phase [rad]")
            ax.set_title(f"tank_circuit{i + 1}")

    #     # Plot results
    #     plt.suptitle("RF-reflectometry spectroscopy")
    #     plt.subplot(211)
    #     plt.cla()
    #     plt.plot(frequencies / u.MHz, R)
    #     plt.xlabel("Readout frequency [MHz]")
    #     plt.ylabel(r"$R=\sqrt{I^2 + Q^2}$ [V]")
    #     plt.subplot(212)
    #     plt.cla()
    #     plt.plot(frequencies / u.MHz, signal.detrend(np.unwrap(phase)))
    #     plt.xlabel("Readout frequency [MHz]")
    #     plt.ylabel("Phase [rad]")
    #     plt.tight_layout()
    #     plt.pause(0.1)
    # # Save results
    # script_name = Path(__file__).name
    # data_handler = DataHandler(root_data_folder=save_dir)
    # save_data_dict.update({"I_data": I})
    # save_data_dict.update({"Q_data": Q})
    # save_data_dict.update({"fig_live": fig})
    # data_handler.additional_files = {script_name: script_name}
    # data_handler.save_data(data=save_data_dict, name="_".join(script_name.split("_")[1:]).split(".")[0])
