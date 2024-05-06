# %%
"""
        echo-Cross-Resonance Time Rabi with single-qubit Quantum State Tomography
    The sequence consists two consecutive pulse sequences with the qubit's thermal decay in between.
In the first sequence, we set the control qubit in |g> and play a flattop with gaussian rise echo-cross-resonance pulse to
the target qubit; the echo-cross-resonance pulse has a variable duration. In the second sequence, we initialize the control
qubit in |e> and play the variable duration echo-cross-resonance pulse to the target qubit. At the end of both
sequences we perform single-qubit Quantum State Tomography on the target qubit.

To recreate the echo-cross-resonance pulse we play (CR--x180_c--CR)--x180_c if the control was initialized in |g>, or
(CR--x180_c--CR) if the control was initialized in |e>. The second x180_c in the first sequence guarantees that the
target qubit is at |g> in the limit of CR length -> zero.

Prerequisites:
    - Having found the resonance frequency of the resonator coupled to the qubit under study (resonator_spectroscopy).
    - Having calibrated qubit pi pulse (x180) by running qubit, spectroscopy, rabi_chevron, power_rabi and updated the config.
    - (optional) Having calibrated the readout (readout_frequency, amplitude, duration_optimization IQ_blobs) for better SNR.

Reference: A. D. Corcoles et al., Phys. Rev. A 87, 030301 (2013)

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
from qualang_tools.results.data_handler import DataHandler
from macros import qua_declaration, multiplexed_readout, one_qb_QST, plot_1qb_tomography_results
import warnings
import matplotlib
import time

matplotlib.use("TKAgg")
warnings.filterwarnings("ignore")


####################
# Helper functions #
####################
def play_flattop(cr: str, duration: int, sign: str):
    """
    QUA macro to play a gapless flat_top gaussian
    """
    if sign == "positive":
        wait(17, cr + "_twin")
        play("gaussian_rise", cr + "_twin")
        wait(int(cr_c1t2_rise_fall_len // 4), cr)
        play("flattop", cr, duration=duration)
        wait(duration, cr + "_twin")
        play("gaussian_fall", cr + "_twin")
    elif sign == "negative":
        wait(17, cr + "_twin")
        play("gaussian_rise" * amp(-1), cr + "_twin")
        wait(int(cr_c1t2_rise_fall_len // 4), cr)
        play("flattop" * amp(-1), cr, duration=duration)
        wait(duration, cr + "_twin")
        play("gaussian_fall" * amp(-1), cr + "_twin")


###################
# The QUA program #
###################
resonators = [1, 2] # rr1, rr2
t_vec_clock = np.arange(8, 400, 4) # in clock cylcle = 4ns
t_vec_ns = t_vec_clock # in clock cylcle = 4ns
n_avg = 1000


with program() as CR_time_rabi_one_qst:
    I, I_st, Q, Q_st, n, n_st = qua_declaration(nb_of_qubits=2)
    t = declare(int)  # QUA variable for the qubit pulse duration
    s = declare(int)  # QUA variable for the control state
    c = declare(int)  # QUA variable for the projection index in QST

    with for_(n, 0, n < n_avg, n + 1):
        save(n, n_st)
        with for_(*from_array(t, t_vec_clock)):
            with for_(c, 0, c < 3, c + 1): # bases
                with for_(s, 0, s < 2, s + 1): # states
                    with if_(s == 1):
                        play("x180", "q1_xy")
                        align()

                    # control - CR
                    play_flattop("cr_c1t2", duration=t >> 1, sign="positive")
                    align()
                    play("x180", "q1_xy")
                    align()
                    play_flattop("cr_c1t2", duration=t >> 1, sign="negative")
                    align()
                    play("x180", "q1_xy")
                    align()
                    one_qb_QST("q2_xy", pi_len, c)
                    align()
                    # Measure the state of the resonators
                    multiplexed_readout(I, I_st, Q, Q_st, resonators=[1, 2], weights="rotated_")
                    # Wait for the qubit to decay to the ground state
                    wait(thermalization_time * u.ns)

    with stream_processing():
        n_st.save("n")
        for r, rr in enumerate(resonators):
            I_st[r].buffer(2).buffer(3).buffer(len(t_vec_clock)).average().save(f"I{rr}")
            Q_st[r].buffer(2).buffer(3).buffer(len(t_vec_clock)).average().save(f"Q{rr}")


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
    job = qmm.simulate(config, CR_time_rabi_one_qst, simulation_config)
    job.get_simulated_samples().con1.plot()

else:
    # Open the quantum machine
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(CR_time_rabi_one_qst)
    # Prepare the figure for live plotting
    fig, axss = plt.subplots(3, 2, figsize=(8, 8), sharex=True)
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
        plt.suptitle("echo CR flattop Time Rabi")
        for i, (axs, bss) in enumerate(zip(axss, ["X", "y", "z"])):
            for ax, q in zip(axs, ["c", "t"]):
                I = I1 if q == "1" else I2
                ax.cla()
                for j, st in enumerate(["0", "1"]):
                    ax.plot(t_vec_ns, I[:, i, j], label=[f"|{st}>"])
                ax.legend(["0", "1"])
                ax.set_title(f"Q_{q}") if i == 0 else None
                ax.set_xlabel("cr durations [ns]") if i == 2 else None
                ax.set_ylabel(f"I quadrature of <{bss}> [V]") if q == "c" else None
        plt.tight_layout()
        plt.pause(0.1)

    if save_data:
        # Arrange data to save
        data = {
            "fig_live": fig,
            "t_vec_ns": t_vec_ns,
            "I1": I1,
            "I1": I1,
            "Q1": Q1,
            "Q2": Q2,
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
