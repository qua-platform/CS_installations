# taken from the library as a backup to my version - not working because of boolean thing right now? may just use my form with int variable representing state
"""
        SINGLE QUBIT RANDOMIZED BENCHMARKING (for gates >= 40ns)
The program consists in playing random sequences of Clifford gates and measuring the state of the resonator afterwards.
Each random sequence is derived on the FPGA for the maximum depth (specified as an input) and played for each depth
asked by the user (the sequence is truncated to the desired depth). Each truncated sequence ends with the recovery gate,
found at each step thanks to a preloaded lookup table (Cayley table), that will bring the qubit back to its ground state.

If the readout has been calibrated and is good enough, then state discrimination can be applied to only return the state
of the qubit. Otherwise, the 'I' and 'Q' quadratures are returned.
Each sequence is played n_avg times for averaging. A second averaging is performed by playing different random sequences.

The data is then post-processed to extract the single-qubit gate fidelity and error per gate
.
Prerequisites:
    - Having found the resonance frequency of the resonator coupled to the qubit under study (resonator_spectroscopy).
    - Having calibrated qubit pi pulse (x180) by running qubit, spectroscopy, rabi_chevron, power_rabi and updated the config.
    - Having the qubit frequency perfectly calibrated (ramsey).
    - (optional) Having calibrated the readout (readout_frequency, amplitude, duration_optimization IQ_blobs) for better SNR.
"""
from qm.qua import *
from qm import QuantumMachinesManager
from qm import SimulationConfig
from qualang_tools.results import progress_counter, fetching_tool
from qualang_tools.plot import interrupt_on_close
from qualang_tools.bakery.randomized_benchmark_c1 import c1_table
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from qualang_tools.results.data_handler import DataHandler
from macros import multiplexed_parser, mp_result_names, mp_fetch_all, readout_macro

if False:
    from configurations.DA_5Q.OPX1000config import *
else:
    from configurations.DB_6Q.OPX1000config import *

##################
#   Parameters   #
##################
# ---- Multiplexed program parameters ---- #
multiplexed = True
qubit_keys = ["q0", "q1", "q2", "q3"]
required_parameters = ["qubit_key", "qubit_frequency", "qubit_relaxation", "resonator_key", "readout_len", "resonator_relaxation", "ge_threshold", "x180_len"]
qub_key_subset, qub_frequency, qubit_relaxation, res_key_subset, readout_len, resonator_relaxation, ge_threshold, x180_len = multiplexed_parser(qubit_keys, multiplexed_parameters.copy(), required_parameters)

# Parameters Definition
qub_relaxation = qubit_relaxation//4 # From ns to clock cycles
res_relaxation = resonator_relaxation//4 # From ns to clock cycles

num_of_sequences = 50  # Number of random sequences
n_avg = 20  # Number of averaging loops for each random sequence
max_circuit_depth = 1000  # Maximum circuit depth
delta_clifford = 10  #  Play each sequence with a depth step equals to 'delta_clifford - Must be > 0
assert (max_circuit_depth / delta_clifford).is_integer(), "max_circuit_depth / delta_clifford must be an integer."
seed = 345324  # Pseudo-random number generator seed
# Flag to enable state discrimination if the readout has been calibrated (rotated blobs and threshold)
state_discrimination = True
# List of recovery gates from the lookup table
inv_gates = [int(np.where(c1_table[i, :] == 0)[0][0]) for i in range(24)]

# Data to save
save_data_dict = {
    "n_avg": n_avg,
    "resonator_key": res_key_subset,
    "qubit_key": qub_key_subset,
    "config": config,
}
save_dir = Path(__file__).resolve().parent / "data"

###################################
# Helper functions and QUA macros #
###################################
def power_law(power, a, b, p):
    return a * (p**power) + b

def generate_sequence():
    cayley = declare(int, value=c1_table.flatten().tolist())
    inv_list = declare(int, value=inv_gates)
    current_state = declare(int)
    step = declare(int)
    sequence = declare(int, size=max_circuit_depth + 1)
    inv_gate = declare(int, size=max_circuit_depth + 1)
    i = declare(int)
    rand = Random(seed=seed)

    assign(current_state, 0)
    with for_(i, 0, i < max_circuit_depth, i + 1):
        assign(step, rand.rand_int(24))
        assign(current_state, cayley[current_state * 24 + step])
        assign(sequence[i], step)
        assign(inv_gate[i], inv_list[current_state])

    return sequence, inv_gate

def play_sequence(sequence_list, depth, qub_key, x180_length):
    i = declare(int)
    with for_(i, 0, i <= depth, i + 1):
        with switch_(sequence_list[i], unsafe=True):
            with case_(0):
                wait(x180_length // 4, qub_key)  # Identity gate
            with case_(1):
                play("x180", qub_key)
            with case_(2):
                play("y180", qub_key)
            with case_(3):
                play("y180", qub_key)
                play("x180", qub_key)
            with case_(4):
                play("x90", qub_key)
                play("y90", qub_key)
            with case_(5):
                play("x90", qub_key)
                play("-y90", qub_key)
            with case_(6):
                play("-x90", qub_key)
                play("y90", qub_key)
            with case_(7):
                play("-x90", qub_key)
                play("-y90", qub_key)
            with case_(8):
                play("y90", qub_key)
                play("x90", qub_key)
            with case_(9):
                play("y90", qub_key)
                play("-x90", qub_key)
            with case_(10):
                play("-y90", qub_key)
                play("x90", qub_key)
            with case_(11):
                play("-y90", qub_key)
                play("-x90", qub_key)
            with case_(12):
                play("x90", qub_key)
            with case_(13):
                play("-x90", qub_key)
            with case_(14):
                play("y90", qub_key)
            with case_(15):
                play("-y90", qub_key)
            with case_(16):
                play("-x90", qub_key)
                play("y90", qub_key)
                play("x90", qub_key)
            with case_(17):
                play("-x90", qub_key)
                play("-y90", qub_key)
                play("x90", qub_key)
            with case_(18):
                play("x180", qub_key)
                play("y90", qub_key)
            with case_(19):
                play("x180", qub_key)
                play("-y90", qub_key)
            with case_(20):
                play("y180", qub_key)
                play("x90", qub_key)
            with case_(21):
                play("y180", qub_key)
                play("-x90", qub_key)
            with case_(22):
                play("x90", qub_key)
                play("y90", qub_key)
                play("x90", qub_key)
            with case_(23):
                play("-x90", qub_key)
                play("y90", qub_key)
                play("-x90", qub_key)

###################
# The QUA program #
###################
# Data to save
save_data_dict = {
    "n_avg": n_avg,
    "config": config,
}

with program() as rb:
    depth = declare(int)  # QUA variable for the varying depth
    depth_target = declare(int)  # QUA variable for the current depth (changes in steps of delta_clifford)
    # QUA variable to store the last Clifford gate of the current sequence which is replaced by the recovery gate
    saved_gate = declare(int)
    m = declare(int)  # QUA variable for the loop over random sequences
    n = declare(int)  # QUA variable for the averaging loop
    I = [declare(fixed) for _ in range(len(qub_key_subset))]  # QUA variable for the 'I' quadrature
    Q = [declare(fixed) for _ in range(len(qub_key_subset))]  # QUA variable for the 'Q' quadrature
    state = [declare(int) for _ in range(len(qub_key_subset))]  # QUA variable for state discrimination
    # The relevant streams
    m_st = declare_stream()
    if state_discrimination:
        state_st = [declare_stream() for _ in range(len(qub_key_subset))]
    else:
        I_st = [declare_stream() for _ in range(len(qub_key_subset))]
        Q_st = [declare_stream() for _ in range(len(qub_key_subset))]

    with for_(m, 0, m < num_of_sequences, m + 1):  # QUA for_ loop over the random sequences
        sequence_list, inv_gate_list = generate_sequence()  # Generate the random sequence of length max_circuit_depth

        assign(depth_target, 1)  # Initialize the current depth to 1
        with for_(depth, 1, depth <= max_circuit_depth, depth + 1):  # Loop over the depths
            # Replacing the last gate in the sequence with the sequence's inverse gate
            # The original gate is saved in 'saved_gate' and is being restored at the end
            assign(saved_gate, sequence_list[depth])
            assign(sequence_list[depth], inv_gate_list[depth - 1])
            # Only played the depth corresponding to target_depth
            with if_(depth == depth_target):
                with for_(n, 0, n < n_avg, n + 1):  # Averaging loop
                    for j in range(len(qub_key_subset)):  # a real Python for loop so it unravels and executes in parallel, not sequentially
                        # Can be replaced by active reset
                        wait(res_relaxation[j], res_key_subset[j])
                        wait(qub_relaxation[j], qub_key_subset[j])
                        # Align the two elements to play the sequence after qubit initialization
                        align(qub_key_subset[j], res_key_subset[j])
                        # The strict_timing ensures that the sequence will be played without gaps
                        with strict_timing_():
                            # Play the random sequence of desired depth
                            play_sequence(sequence_list, depth, qub_key_subset[j], x180_len[j])
                        # Align the two elements to measure after playing the circuit.
                        align(qub_key_subset[j], res_key_subset[j])
                        # Make sure you updated the ge_threshold and angle if you want to use state discrimination -----------------------------------------------
                        state[j], I[j], Q[j] = readout_macro(resonator=res_key_subset[j], I=I[j], Q=Q[j], state=state[j], threshold=ge_threshold[j], state_boolean = False)
                        # Save the results to their respective streams
                        if state_discrimination:
                            save(state[j], state_st[j])
                        else:
                            save(I[j], I_st[j])
                            save(Q[j], Q_st[j])
                # Go to the next depth
                assign(depth_target, depth_target + delta_clifford)
            # Reset the last gate of the sequence back to the original Clifford gate
            # (that was replaced by the recovery gate at the beginning)
            assign(sequence_list[depth], saved_gate)
        # Save the counter for the progress bar
        save(m, m_st)

    with stream_processing():
        m_st.save("iteration")
        for j in range(len(qub_key_subset)):
            if state_discrimination:
                # saves a 2D array of depth and random pulse sequences in order to get error bars along the random sequences
                #state_st[j].boolean_to_int().buffer(n_avg).map(FUNCTIONS.average()).buffer( max_circuit_depth / delta_clifford ).buffer(num_of_sequences).save("state_"+str(j))
                # returns a 1D array of averaged random pulse sequences vs depth of circuit for live plotting
                #state_st[j].boolean_to_int().buffer(n_avg).map(FUNCTIONS.average()).buffer( max_circuit_depth / delta_clifford ).average().save("state_avg_"+str(j))
                # saves a 2D array of depth and random pulse sequences in order to get error bars along the random sequences
                state_st[j].buffer(n_avg).map(FUNCTIONS.average()).buffer( max_circuit_depth / delta_clifford ).buffer(num_of_sequences).save("state_"+str(j))
                # returns a 1D array of averaged random pulse sequences vs depth of circuit for live plotting
                state_st[j].buffer(n_avg).map(FUNCTIONS.average()).buffer( max_circuit_depth / delta_clifford ).average().save("state_avg_"+str(j))
            else:
                I_st[j].buffer(n_avg).map(FUNCTIONS.average()).buffer(max_circuit_depth / delta_clifford).buffer(num_of_sequences).save("I_"+str(j))
                Q_st[j].buffer(n_avg).map(FUNCTIONS.average()).buffer(max_circuit_depth / delta_clifford).buffer(num_of_sequences).save("Q_"+str(j))
                I_st[j].buffer(n_avg).map(FUNCTIONS.average()).buffer(max_circuit_depth / delta_clifford).average().save("I_avg_"+str(j))
                Q_st[j].buffer(n_avg).map(FUNCTIONS.average()).buffer(max_circuit_depth / delta_clifford).average().save("Q_avg_"+str(j))

#####################################
#  Open Communication with the QOP  #
#####################################
#qmm = QuantumMachinesManager(host=qop_ip, port=qop_port, cluster_name=cluster_name, octave=octave_config)
prog = rb
# ---- Open communication with the OPX ---- #
from warsh_credentials import host_ip, cluster
qmm = QuantumMachinesManager(host = host_ip, cluster_name = cluster)
###########################
# Run or Simulate Program #
###########################
simulate = False
if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=10_000)  # In clock cycles = 4ns
    # Simulate blocks python until the simulation is done
    job = qmm.simulate(config, prog, simulation_config)
    # Get the simulated samples
    samples = job.get_simulated_samples()
    # Plot the simulated samples
    samples.con1.plot()
    # Get the waveform report object
    waveform_report = job.get_simulated_waveform_report()
    # Cast the waveform report to a python dictionary
    waveform_dict = waveform_report.to_dict()
    # Visualize and save the waveform report
    waveform_report.create_plot(samples, plot=True, save_path=str(Path(__file__).resolve()))

else:
    # Open the quantum machine
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(prog)
    # Get results from QUA program
    if state_discrimination:
        result_names = mp_result_names(qub_key_subset, single_tags = ["iteration"], mp_tags = ["state_avg", "state"])
    else:
        result_names = mp_result_names(qub_key_subset, single_tags = ["iteration"], mp_tags = ["I_avg", "Q_avg", "I", "Q"])
    res_handles = fetching_tool(job, data_list = result_names, mode = "live")
    # Live plotting
    fig = plt.figure()
    interrupt_on_close(fig, job)  # Interrupts the job when closing the figure
    # data analysis
    x = np.arange(1, max_circuit_depth + 0.1, delta_clifford)
    while res_handles.is_processing():
        # data analysis
        if state_discrimination:
            iteration, state_avg, state = mp_fetch_all(res_handles, qub_key_subset, num_single_tags=1)
            value_avg = state_avg
        else:
            iteration, I_avg, Q_avg, I, Q = mp_fetch_all(res_handles, qub_key_subset, num_single_tags=1)
            value_avg = I_avg

        # Progress bar
        progress_counter(iteration, num_of_sequences, start_time=res_handles.get_start_time())
        # Plot averaged values
        plt.cla()
        for j in range(len(qub_key_subset)):
            plt.plot(x, value_avg[j], marker=".", label=f"Qubit {qub_key_subset[j]}")
        plt.xlabel("Number of Clifford gates")
        plt.ylabel("Sequence Fidelity")
        plt.title("Single qubit RB")
        plt.legend()
        plt.pause(0.1)

    # At the end of the program, fetch the non-averaged results to get the error-bars
    if state_discrimination:
        iteration, state_avg, state = mp_fetch_all(res_handles, qub_key_subset, num_single_tags=1)
        value_avg_arr = np.mean(state, axis=1)
        error_avg_arr = np.std(state, axis=1)
    else:
        iteration, I_avg, Q_avg, I, Q = mp_fetch_all(res_handles, qub_key_subset, num_single_tags=1)
        value_avg_arr = np.mean(I, axis=1)
        error_avg_arr = np.std(I, axis=1)

    for j in range(len(qub_key_subset)):
        value_avg = value_avg_arr[j]
        error_avg = error_avg_arr[j]
        # data analysis
        pars, cov = curve_fit(
            f=power_law,
            xdata=x,
            ydata=value_avg,
            p0=[0.5, 0.5, 0.9],
            bounds=(-np.inf, np.inf),
            maxfev=2000,
        )
        stdevs = np.sqrt(np.diag(cov))

        print("#########################")
        print(f"####### Qubit {qub_key_subset[j]} ######")
        print("#########################")

        print("#########################")
        print("#### Fit Parameters #####")
        print("#########################")
        print(f"A = {pars[0]:.3} ({stdevs[0]:.1}), B = {pars[1]:.3} ({stdevs[1]:.1}), p = {pars[2]:.3} ({stdevs[2]:.1})")
        print("Covariance Matrix")
        print(cov)

        one_minus_p = 1 - pars[2]
        r_c = one_minus_p * (1 - 1 / 2**1)
        r_g = r_c / 1.875  # 1.875 is the average number of gates in clifford operation
        r_c_std = stdevs[2] * (1 - 1 / 2**1)
        r_g_std = r_c_std / 1.875

        print("#########################")
        print("### Useful Parameters ###")
        print("#########################")
        print(
            f"Error rate: 1-p = {np.format_float_scientific(one_minus_p, precision=2)} ({stdevs[2]:.1})\n"
            f"Clifford set infidelity: r_c = {np.format_float_scientific(r_c, precision=2)} ({r_c_std:.1})\n"
            f"Gate infidelity: r_g = {np.format_float_scientific(r_g, precision=2)}  ({r_g_std:.1})"
        )

        # Plots
        plt.figure()
        plt.errorbar(x, value_avg, yerr=error_avg, marker=".")
        plt.plot(x, power_law(x, *pars), linestyle="--", linewidth=2)
        plt.xlabel("Number of Clifford gates")
        plt.ylabel("Sequence Fidelity")
        plt.title("Single qubit RB")

    # Save results
    script_name = Path(__file__).name
    data_handler = DataHandler(root_data_folder=save_dir)
    if state_discrimination:
        save_data_dict.update({"state_avg_data": state})
    else:
        save_data_dict.update({"I_data": I})
        save_data_dict.update({"Q_data": Q})
    save_data_dict.update({"fig_live": fig})
    data_handler.additional_files = {script_name: script_name, **default_additional_files}
    data_handler.save_data(data=save_data_dict, name="_".join(script_name.split("_")[1:]).split(".")[0])