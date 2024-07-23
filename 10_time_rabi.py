# %%
"""
        TIME RABI
The sequence consists in playing the qubit pulse and measuring the state of the resonator
for different qubit pulse durations.
The results are then post-processed to find the qubit pulse duration for the chosen amplitude.

Prerequisites:
    - Having found the resonance frequency of the resonator coupled to the qubit under study (resonator_spectroscopy).
    - Having calibrated the IQ mixer connected to the qubit drive line (external mixer or Octave port)
    - Having found the rough qubit frequency and pi pulse amplitude (rabi_chevron_amplitude or power_rabi).
    - Set the qubit frequency and desired pi pulse amplitude (pi_amp_q) in the configuration.

Next steps before going to the next node:
    - Update the qubit pulse duration (pi_len_q) in the configuration.
"""

from qm.QuantumMachinesManager import QuantumMachinesManager
from qm.qua import *
from qm import SimulationConfig

from configuration import *
# from configuration_with_octave import *
import matplotlib.pyplot as plt
from qualang_tools.loops import from_array
from qualang_tools.results import fetching_tool
from qualang_tools.plot import interrupt_on_close
from qualang_tools.results import progress_counter
from macros import qua_declaration, multiplexed_readout
import warnings
import matplotlib
from qualang_tools.results.data_handler import DataHandler
import time

matplotlib.use("TKAgg")
warnings.filterwarnings("ignore")

###################
# The QUA program #
###################
t_vec = np.arange(4, 200, 2)  # In clock cycles = 4ns
cooldown_time = 1 * u.us
n_avg = 1000

with program() as rabi:
    I, I_st, Q, Q_st, n, n_st = qua_declaration(nb_of_qubits=2)
    t = declare(int)  # QUA variable for the qubit pulse duration

    with for_(n, 0, n < n_avg, n + 1):
        with for_(*from_array(t, t_vec)):
            # Play the qubit pulses
            play("x180", "q1_xy", duration=t)
            play("x180", "q2_xy", duration=t)
            # Align the elements to measure after playing the qubit pulses.
            align()
            # Start using Rotated integration weights (cf. IQ_blobs.py)
            multiplexed_readout(I, I_st, Q, Q_st, resonators=[1, 2], weights="rotated_")
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
qmm = QuantumMachinesManager(
    host=qop_ip,
    port=qop_port,
    cluster_name=cluster_name,
    octave=octave_config,
)

###########################
# Run or Simulate Program #
###########################

simulate = False
save_data = True

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=10_000)  # In clock cycles = 4ns
    job = qmm.simulate(config, rabi, simulation_config)
    job.get_simulated_samples().con1.plot()

else:
    # Open the quantum machine
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(rabi)
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
        # Progress bar
        progress_counter(n, n_avg, start_time=results.start_time)
        # calculate the elapsed time
        elapsed_time = time.time() - start_time
        # Convert the results into Volts
        I1, Q1 = u.demod2volts(I1, readout_len), u.demod2volts(Q1, readout_len)
        I2, Q2 = u.demod2volts(I2, readout_len), u.demod2volts(Q2, readout_len)
        # Plots
        plt.suptitle("Time Rabi")
        plt.subplot(221)
        plt.cla()
        plt.plot(4 * t_vec, I1)
        plt.title("Qubit 1")
        plt.ylabel("I quadrature [V]")
        plt.subplot(223)
        plt.cla()
        plt.plot(4 * t_vec, Q1)
        plt.xlabel("Qubit pulse duration [ns]")
        plt.ylabel("Q quadrature [V]")
        plt.subplot(222)
        plt.cla()
        plt.plot(4 * t_vec, I2)
        plt.title("Qubit 2")
        plt.subplot(224)
        plt.cla()
        plt.plot(4 * t_vec, Q2)
        plt.xlabel("Qubit pulse duration [ns]")
        plt.tight_layout()
        plt.pause(1.0)

    # Fit the time Rabi curves
    try:
        from qualang_tools.plot.fitting import Fit

        fit = Fit()
        fig_analysis = plt.figure()
        plt.suptitle(f"Multiplexed Time Rabi")
        plt.subplot(121)
        fit.rabi(4 * t_vec, I1, plot=True)
        plt.xlabel("Qubit pulse duration [ns]")
        plt.ylabel("I quadrature [V]")
        plt.title("Qubit 1")
        plt.subplot(122)
        fit.rabi(4 * t_vec, I2, plot=True)
        plt.xlabel("Qubit pulse duration [ns]")
        plt.title("Qubit 2")
        plt.tight_layout()
    except (Exception,):
        pass

    plt.show()

    # Close the quantum machines at the end
    qm.close()

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
            "iteration": np.array([n]),  # convert int to np.array of int
            "elapsed_time": np.array([elapsed_time]),  # convert float to np.array of float
        }
        # Save Data
        script_name = Path(__file__).name
        data_handler = DataHandler(root_data_folder=save_dir)
        data_handler.create_data_folder(name=Path(__file__).stem)
        data_handler.additional_files = {script_name: script_name, **default_additional_files}
        data_folder = data_handler.save_data(data=data)


# %%
