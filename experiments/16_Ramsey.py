# %%
"""
        RAMSEY WITH VIRTUAL Z ROTATIONS
The program consists in playing a Ramsey sequence (x90 - t_vec- x90 - measurement) for different idle times.
Instead of detuning the qubit gates, the frame of the second x90 pulse is rotated (de-phased) to mimic an accumulated
phase acquired for a given detuning after the idle time.
This method has the advantage of playing resonant gates.

From the results, one can fit the Ramsey oscillations and precisely measure the qubit resonance frequency and T2*.

Prerequisites:
    - Having found the resonance frequency of the resonator coupled to the qubit under study (resonator_spectroscopy).
    - Having calibrated qubit pi pulse (x180) by running qubit, spectroscopy, rabi_chevron, power_rabi and updated the config.
    - (optional) Having calibrated the readout (readout_frequency, amplitude, duration_optimization IQ_blobs) for better SNR.

Next steps before going to the next node:
    - Update the qubit frequency (qubit_IF_q) in the configuration.
"""

from qm.QuantumMachinesManager import QuantumMachinesManager
from qm.qua import *
from qm import SimulationConfig

# from configuration import *
from configuration_with_octave import *
import matplotlib.pyplot as plt
from qualang_tools.loops import from_array
from qualang_tools.results import fetching_tool, progress_counter
from qualang_tools.plot import interrupt_on_close
from macros import qua_declaration, multiplexed_readout
from qualang_tools.plot.fitting import Fit
import warnings
import matplotlib
from qualang_tools.results.data_handler import DataHandler
import time

matplotlib.use("TKAgg")
warnings.filterwarnings("ignore")


###################
# The QUA program #
###################
n_avg = 1000  # Number of averages
t_vec = np.arange(4, 300, 1)  # Idle time sweep in clock cycles (Needs to be a list of integers)
detuning = 1e6  # "Virtual" detuning in Hz

with program() as ramsey:
    I, I_st, Q, Q_st, n, n_st = qua_declaration(nb_of_qubits=2)
    t = declare(int)  # QUA variable for the idle time
    phi = declare(fixed)  # Phase to apply the virtual Z-rotation

    with for_(n, 0, n < n_avg, n + 1):
        with for_(*from_array(t, t_vec)):
            # Rotate the frame of the second x90 gate to implement a virtual Z-rotation
            # 4*tau because tau was in clock cycles and 1e-9 because tau is ns
            assign(phi, Cast.mul_fixed_by_int(detuning * 1e-9, 4 * t))
            align()

            # Qubit 1
            play("x90", "q1_xy")  # 1st x90 gate
            wait(t, "q1_xy")  # Wait a varying idle time
            frame_rotation_2pi(phi, "q1_xy")  # Virtual Z-rotation
            play("x90", "q1_xy")  # 2nd x90 gate

            # Qubit 2
            play("x90", "q2_xy")  # 1st x90 gate
            wait(t, "q2_xy")  # Wait a varying idle time
            frame_rotation_2pi(phi, "q2_xy")  # Virtual Z-rotation
            play("x90", "q2_xy")  # 2nd x90 gate

            # Align the elements to measure after having waited a time "tau" after the qubit pulses.
            align()
            # Measure the state of the resonators
            multiplexed_readout(I, I_st, Q, Q_st, resonators=[1, 2], weights="rotated_")
            # Reset the frame of the qubit in order not to accumulate rotations
            reset_frame("q1_xy")
            reset_frame("q2_xy")
            # Wait for the qubit to decay to the ground state
            wait(thermalization_time * u.ns)
        # Save the averaging iteration to get the progress bar
        save(n, n_st)

    with stream_processing():
        n_st.save("n")
        # resonator 1
        I_st[0].buffer(len(t_vec)).average().save("I1")
        Q_st[0].buffer(len(t_vec)).average().save("Q1")
        # resonator 2
        I_st[1].buffer(len(t_vec)).average().save("I2")
        Q_st[1].buffer(len(t_vec)).average().save("Q2")

#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(host=qop_ip, port=qop_port, cluster_name=cluster_name, octave=octave_config)

###########################
# Run or Simulate Program #
###########################

simulate = False
save_data = True

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=10_000)  # In clock cycles = 4ns
    job = qmm.simulate(config, ramsey, simulation_config)
    job.get_simulated_samples().con1.plot()

else:
    # Open the quantum machine
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(ramsey)
    # Prepare the figure for live plotting
    fig = plt.figure()
    interrupt_on_close(fig, job)
    # Tool to easily fetch results from the OPX (results_handle used in it)
    results = fetching_tool(job, ["n", "I1", "Q1", "I2", "Q2"], mode="live")
    # Live plotting
    while results.is_processing():
        start_time = results.get_start_time()
        # Fetch results
        n, I1, Q1, I2, Q2 = results.fetch_all()
        # Convert the results into Volts
        I1, Q1 = u.demod2volts(I1, readout_len), u.demod2volts(Q1, readout_len)
        I2, Q2 = u.demod2volts(I2, readout_len), u.demod2volts(Q2, readout_len)
        # Progress bar
        progress_counter(n, n_avg, start_time=results.start_time)
        # calculate the elapsed time
        elapsed_time = time.time() - start_time
        # Plot
        plt.subplot(221)
        plt.cla()
        plt.plot(4 * t_vec, I1)
        plt.ylabel("I quadrature [V]")
        plt.title("Qubit 1")
        plt.subplot(223)
        plt.cla()
        plt.plot(4 * t_vec, Q1)
        plt.ylabel("Q quadrature [V]")
        plt.xlabel("Idle times [ns]")
        plt.subplot(222)
        plt.cla()
        plt.plot(4 * t_vec, I2)
        plt.title("Qubit 2")
        plt.subplot(224)
        plt.cla()
        plt.plot(4 * t_vec, Q2)
        plt.title("Q2")
        plt.xlabel("Idle times [ns]")
        plt.tight_layout()
        plt.pause(0.1)
    # Close the quantum machines at the end
    qm.close()
    try:
        fit = Fit()
        fig_analysis = plt.figure()
        plt.suptitle(f"Ramsey measurement with detuning={detuning} Hz")
        plt.subplot(221)
        fit.ramsey(4 * t_vec, I1, plot=True)
        plt.xlabel("Idle times [ns]")
        plt.ylabel("I quadrature [V]")
        plt.title("Qubit 1")
        plt.subplot(223)
        fit.ramsey(4 * t_vec, Q1, plot=True)
        plt.xlabel("Idle times [ns]")
        plt.ylabel("I quadrature [V]")
        plt.title("Qubit 2")
        plt.subplot(222)
        fit.ramsey(4 * t_vec, I2, plot=True)
        plt.xlabel("Idle times [ns]")
        plt.ylabel("I quadrature [V]")
        plt.subplot(224)
        fit.ramsey(4 * t_vec, Q2, plot=True)
        plt.xlabel("Idle times [ns]")
        plt.ylabel("I quadrature [V]")
        plt.tight_layout()
    except (Exception,):
        pass

    if save_data:
        # Arrange data to save
        data = {
            "fig_live": fig,
            "fig_analysis": fig_analysis,
            "t_vec": t_vec,
            "I1": I1,
            "I1": I1,
            "Q1": Q1,
            "Q2": Q2,
            "detuning": np.array(detuning),
            "iteration": np.array([n]),  # convert int to np.array of int
            "elapsed_time": np.array([elapsed_time]),  # convert float to np.array of float
        }

        # Initialize the DataHandler
        script_name = Path(__file__).name
        data_handler = DataHandler(root_data_folder=save_dir)
        data_handler.create_data_folder(name=Path(__file__).stem)
        data_handler.additional_files = {
            script_name: script_name,
            "configuration_with_octave.py": "configuration_with_octave.py",
            "calibration_db.json": "calibration_db.json",
            "optimal_weights.npz": "optimal_weights.npz",
        }
        # Save results
        data_folder = data_handler.save_data(data=data)

    # Close the quantum machines at the end
    qm.close()

# %%



# %%