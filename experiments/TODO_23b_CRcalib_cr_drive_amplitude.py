# %%
"""
        echo-Cross-Resonance Time Rabi with single-qubit Quantum State Tomography
    The sequence consists two consecutive pulse sequences with the qubit's thermal decay in between.
In the first sequence, we set the control qubit in |g> and play a rectangular echo-cross-resonance pulse to
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
from macros import qua_declaration, multiplexed_readout, one_qb_QST, plot_1qb_tomography_results
import warnings
import matplotlib

from hamiltonian_tomography import CRHamiltonianTomography

matplotlib.use("TKAgg")
warnings.filterwarnings("ignore")


###################
# The QUA program #
###################

nb_of_qubits = 2
resonators = [1, 2] # rr1, rr2
thresholds = [ge_threshold_q1, ge_threshold_q2]
assert len(resonators) ==  nb_of_qubits
assert len(thresholds) ==  nb_of_qubits

a_vec = np.arange(0.1, 2.0, 0.1)
t_vec = np.arange(4, 200, 2) # in clock cylcle = 4ns
n_avg = 1000 # num of iterations

with program() as cr_calib:
    I, I_st, Q, Q_st, n, n_st = qua_declaration(nb_of_qubits=2)
    state = [declare(bool) for _ in range(nb_of_qubits)]
    state_st = [declare_stream() for _ in range(nb_of_qubits)]
    t = declare(int)
    a = declare(fixed)
    c = declare(int)
    
    with for_(n, 0, n < n_avg, n + 1):
        save(n, n_st)
        with for_(*from_array(a, a_vec)):
            with for_(*from_array(t, t_vec)):
                with for_(c, 0, c < 3, c + 1):
                    for state in [0, 1]: # states
                        if state == 1:
                            play("x180", "q1_xy")
                            align()
                        #                           ____           ____ 
                        # Control(fC): ____________| pi |_________| pi |_______________
                        #                  ________                      _____
                        #      CR(fT): ___|        |_____          _____| QST |________
                        #                                |________|            _____
                        # Readout(fR): _______________________________________|     |__
                        play("square_positive" * amp(a), "cr_c1t2", duration=t)
                        align()
                        play("x180", "q1_xy")
                        align()
                        play("square_negative" * amp(a), "cr_c1t2", duration=t)
                        align()
                        play("x180", "q1_xy")
                        align()
                        # target - QST
                        one_qb_QST("q2_xy", pi_len, c)
                        align()
                        # Measure the state of the resonators
                        # Make sure you updated the ge_threshold and angle if you want to use state discrimination
                        multiplexed_readout(I, I_st, Q, Q_st, resonators=[1, 2], weights="roated_")
                        # multiplexed_readout(I, I_st, Q, Q_st, resonators=[1, 2], weights="optimized_")
                        # Wait for the qubit to decay to the ground state
                        wait(thermalization_time * u.ns)
                        # Make sure you updated the ge_threshold
                        for q in range(nb_of_qubits):
                            assign(state[q], I[q] > threshold[q])
                            save(state[q], state_st[q])

    with stream_processing():
        n_st.save("n")
        for r, rr in enumerate(resonators):
            I_st[r].buffer(2).buffer(3).buffer(len(t_vec)).buffer(len(a_vec)).average().save(f"I{rr}")
            Q_st[r].buffer(2).buffer(3).buffer(len(t_vec)).buffer(len(a_vec)).average().save(f"Q{rr}")


#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(host=qop_ip, port=qop_port, cluster_name=cluster_name, octave=octave_config)


###########################
# Run or Simulate Program #
###########################

simulate = False

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=10_000)  # In clock cycles = 4ns
    job = qmm.simulate(config, cr_calib, simulation_config)
    job.get_simulated_samples().con1.plot()

else:
    # Open the quantum machine
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(cr_calib)
    # Prepare the figure for live plotting
    fig = plt.figure()
    interrupt_on_close(fig, job)
    # Tool to easily fetch results from the OPX (results_handle used in it)
    results = fetching_tool(job, ["n", "I1", "Q1", "I2", "Q2"], mode="live")
    # Live plotting
    while results.is_processing():
        # Fetch results
        n, I1, Q1, I2, Q2 = results.fetch_all()
        # Progress bar
        progress_counter(n, n_avg, start_time=results.start_time)
    x[0] = 1  # to set the first value of 'x' to be depth = 1 as in the experiment
    while results.is_processing():
        start_time = results.get_start_time()
        # data analysis
        if state_discrimination:
            state_avg, iteration = results.fetch_all()
            value_avg = state_avg
        else:
            I, Q, iteration = results.fetch_all()
            value_avg = I

        # Progress bar
        progress_counter(iteration, num_of_sequences, start_time=results.get_start_time())
        # calculate the elapsed time
        elapsed_time = time.time() - start_time
        # Plot averaged values
        plt.cla()
        plt.plot(x, value_avg, marker=".")
        plt.xlabel("Number of Clifford gates")
        plt.ylabel("Sequence Fidelity")
        plt.title("Single qubit RB")
        plt.pause(0.1)

        # At the end of the program, fetch the non-averaged results to get the error-bars
        if state_discrimination:
            results = fetching_tool(job, data_list=["state"])
            state = results.fetch_all()[0]
            value_avg = np.mean(state, axis=0)
            error_avg = np.std(state, axis=0)
        else:
            results = fetching_tool(job, data_list=["I", "Q"])
            I, Q = results.fetch_all()
            value_avg = np.mean(I, axis=0)
            error_avg = np.std(I, axis=0)

        # data analysis
        crht = CRHamiltonianTomography(
            ts=ts,
            xyz={
                "0": {
                    "x": pms0["x"],
                    "y": pms0["y"],
                    "z": pms0["z"],
                },
                "1": {
                    "x": pms1["x"],
                    "y": pms1["y"],
                    "z": pms1["z"],
                },
            },
        )
        crht.fit_params(random_state=5)
        coefs = {k: 1e6*v for k, v in crht.get_interaction_rates().items()}
        fig = crht.plot_fit_result()

        # Close the quantum machines at the end
        qm.close()

# %%
