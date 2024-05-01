"""
        SINGLE QUBIT RANDOMIZED BENCHMARKING (for gates >= 40ns)
The program consists in qua.playing random sequences of Clifford gates and measuring the state of the resonator afterwards.
Each random sequence is derived on the FPGA for the maximum depth (specified as an input) and qua.played for each depth
asked by the user (the sequence is truncated to the desired depth). Each truncated sequence ends with the recovery gate,
found at each step thanks to a preloaded lookup table (Cayley table), that will bring the qubit back to its ground state.

If the readout has been calibrated and is good enough, then state discrimination can be applied to only return the state
of the qubit. Otherwise, the 'I' and 'Q' quadratures are returned.
Each sequence is qua.played n_avg times for averaging. A second averaging is performed by qua.playing different random sequences.

The data is then post-processed to extract the single-qubit gate fidelity and error per gate
.
Prerequisites:
    - Having found the resonance frequency of the resonator coupled to the qubit under study (resonator_spectroscopy).
    - Having calibrated qubit pi pulse (x180) by running qubit, spectroscopy, rabi_chevron, power_rabi and updated the config.
    - Having the qubit frequency perfectly calibrated (ramsey).
    - (optional) Having calibrated the readout (readout_frequency, amplitude, duration_optimization IQ_blobs) for better SNR.
"""

import qm.qua as qua
import qm as qm_api
import numpy as np
from configuration import config, qop_ip, cluster_name, u, thermalization_time, drag_coef, ge_threshold, x180_len
from qualang_tools.results import progress_counter, fetching_tool
from qualang_tools.plot import interrupt_on_close
from qualang_tools.bakery.randomized_benchmark_c1 import c1_table
from macros import readout_macro
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt


##############################
# Program-specific variables #
##############################

num_of_sequences = 50  # Number of random sequences
n_avg = 20  # Number of averaging loops for each random sequence
max_circuit_depth = 1000  # Maximum circuit depth
delta_clifford = 10  #  qua.play each sequence with a depth step equals to 'delta_clifford - Must be > 1
assert (max_circuit_depth / delta_clifford).is_integer(), "max_circuit_depth / delta_clifford must be an integer."
seed = 345324  # Pseudo-random number generator seed
# Flag to enable state discrimination if the readout has been calibrated (rotated blobs and threshold)
state_discrimination = False
# List of recovery gates from the lookup table
inv_gates = [int(np.where(c1_table[i, :] == 0)[0][0]) for i in range(24)]


###################################
# Helper functions and QUA macros #
###################################
def power_law(power, a, b, p):
    return a * (p**power) + b


def generate_sequence():
    cayley = qua.declare(int, value=c1_table.flatten().tolist())
    inv_list = qua.declare(int, value=inv_gates)
    current_state = qua.declare(int)
    step = qua.declare(int)
    sequence = qua.declare(int, size=max_circuit_depth + 1)
    inv_gate = qua.declare(int, size=max_circuit_depth + 1)
    i = qua.declare(int)
    rand = qua.Random(seed=seed)

    qua.assign()(current_state, 0)
    with qua.for_(i, 0, i < max_circuit_depth, i + 1):
        qua.assign()(step, rand.rand_int(24))
        qua.assign()(current_state, cayley[current_state * 24 + step])
        qua.assign()(sequence[i], step)
        qua.assign()(inv_gate[i], inv_list[current_state])

    return sequence, inv_gate


def play_sequence(sequence_list, depth):
    i = qua.declare(int)
    with qua.for_(i, 0, i <= depth, i + 1):
        with qua.switch_(sequence_list[i], unsafe=True):
            with qua.case_(0):
                qua.wait(x180_len // 4, "qubit")
            with qua.case_(1):
                qua.play("x180", "qubit")
            with qua.case_(2):
                qua.play("y180", "qubit")
            with qua.case_(3):
                qua.play("y180", "qubit")
                qua.play("x180", "qubit")
            with qua.case_(4):
                qua.play("x90", "qubit")
                qua.play("y90", "qubit")
            with qua.case_(5):
                qua.play("x90", "qubit")
                qua.play("-y90", "qubit")
            with qua.case_(6):
                qua.play("-x90", "qubit")
                qua.play("y90", "qubit")
            with qua.case_(7):
                qua.play("-x90", "qubit")
                qua.play("-y90", "qubit")
            with qua.case_(8):
                qua.play("y90", "qubit")
                qua.play("x90", "qubit")
            with qua.case_(9):
                qua.play("y90", "qubit")
                qua.play("-x90", "qubit")
            with qua.case_(10):
                qua.play("-y90", "qubit")
                qua.play("x90", "qubit")
            with qua.case_(11):
                qua.play("-y90", "qubit")
                qua.play("-x90", "qubit")
            with qua.case_(12):
                qua.play("x90", "qubit")
            with qua.case_(13):
                qua.play("-x90", "qubit")
            with qua.case_(14):
                qua.play("y90", "qubit")
            with qua.case_(15):
                qua.play("-y90", "qubit")
            with qua.case_(16):
                qua.play("-x90", "qubit")
                qua.play("y90", "qubit")
                qua.play("x90", "qubit")
            with qua.case_(17):
                qua.play("-x90", "qubit")
                qua.play("-y90", "qubit")
                qua.play("x90", "qubit")
            with qua.case_(18):
                qua.play("x180", "qubit")
                qua.play("y90", "qubit")
            with qua.case_(19):
                qua.play("x180", "qubit")
                qua.play("-y90", "qubit")
            with qua.case_(20):
                qua.play("y180", "qubit")
                qua.play("x90", "qubit")
            with qua.case_(21):
                qua.play("y180", "qubit")
                qua.play("-x90", "qubit")
            with qua.case_(22):
                qua.play("x90", "qubit")
                qua.play("y90", "qubit")
                qua.play("x90", "qubit")
            with qua.case_(23):
                qua.play("-x90", "qubit")
                qua.play("y90", "qubit")
                qua.play("-x90", "qubit")


###################
# The QUA program #
###################
with qua.program() as rb:
    depth = qua.declare(int)  # QUA variable for the varying depth
    depth_target = qua.declare(int)  # QUA variable for the current depth (changes in steps of delta_clifford)
    # QUA variable to store the last Clifford gate of the current sequence which is replaced by the recovery gate
    saved_gate = qua.declare(int)
    m = qua.declare(int)  # QUA variable for the loop over random sequences
    n = qua.declare(int)  # QUA variable for the averaging loop
    I = qua.declare(qua.fixed)  # QUA variable for the 'I' quadrature
    Q = qua.declare(qua.fixed)  # QUA variable for the 'Q' quadrature
    state = qua.declare(bool)  # QUA variable for state discrimination
    # The relevant streams
    m_st = qua.declare_stream()
    if state_discrimination:
        state_st = qua.declare_stream()
    else:
        I_st = qua.declare_stream()
        Q_st = qua.declare_stream()

    with qua.for_(m, 0, m < num_of_sequences, m + 1):  # QUA qua.for_ loop over the random sequences
        sequence_list, inv_gate_list = generate_sequence()  # Generate the random sequence of length max_circuit_depth

        qua.assign()(depth_target, 0)  # Initialize the current depth to 0
        with qua.for_(depth, 1, depth <= max_circuit_depth, depth + 1):  # Loop over the depths
            # Replacing the last gate in the sequence with the sequence's inverse gate
            # The original gate is saved in 'saved_gate' and is being restored at the end
            qua.assign()(saved_gate, sequence_list[depth])
            qua.assign()(sequence_list[depth], inv_gate_list[depth - 1])
            # Only qua.played the depth corresponding to target_depth
            with qua.if_((depth == 1) | (depth == depth_target)):
                with qua.for_(n, 0, n < n_avg, n + 1):  # Averaging loop
                    # Can be replaced by active reset
                    qua.wait(thermalization_time * u.ns, "resonator")
                    # qua.align the two elements to qua.play the sequence after qubit initialization
                    qua.align("resonator", "qubit")
                    # The strict_timing ensures that the sequence will be qua.played without gaps
                    with qua.strict_timing_():
                        # qua.play the random sequence of desired depth
                        play_sequence(sequence_list, depth)
                    # qua.align the two elements to measure after qua.playing the circuit.
                    qua.align("qubit", "resonator")
                    # Make sure you updated the ge_threshold and angle if you want to use state discrimination
                    qua.measure(
                        "readout",
                        "resonator",
                        None,
                        # qua.dual_demod.full("rotated_cos", "out1", "rotated_sin", "out2", I_g),
                        # qua.dual_demod.full("rotated_minus_sin", "out1", "rotated_cos", "out2", Q_g),
                        qua.dual_demod.full("opt_cos", "out1", "opt_sin", "out2", I),
                        qua.dual_demod.full("opt_minus_sin", "out1", "opt_cos", "out2", Q),
                    )
                    # Save the results to their respective streams
                    if state_discrimination:
                        qua.save(state, state_st)
                    else:
                        qua.save(I, I_st)
                        qua.save(Q, Q_st)
                # Go to the next depth
                qua.assign()(depth_target, depth_target + delta_clifford)
            # Reset the last gate of the sequence back to the original Clifford gate
            # (that was replaced by the recovery gate at the beginning)
            qua.assign()(sequence_list[depth], saved_gate)
        # Save the counter for the progress bar
        qua.save(m, m_st)

    with qua.stream_processing():
        m_st.save("iteration")
        if state_discrimination:
            # saves a 2D array of depth and random pulse sequences in order to get error bars along the random sequences
            state_st.boolean_to_int().buffer(n_avg).map(qua.FUNCTIONS.average()).buffer(
                max_circuit_depth / delta_clifford + 1
            ).buffer(num_of_sequences).save("state")
            # returns a 1D array of averaged random pulse sequences vs depth of circuit for live plotting
            state_st.boolean_to_int().buffer(n_avg).map(qua.FUNCTIONS.average()).buffer(
                max_circuit_depth / delta_clifford + 1
            ).average().save("state_avg")
        else:
            I_st.buffer(n_avg).map(qua.FUNCTIONS.average()).buffer(max_circuit_depth / delta_clifford + 1).buffer(
                num_of_sequences
            ).save("I")
            Q_st.buffer(n_avg).map(qua.FUNCTIONS.average()).buffer(max_circuit_depth / delta_clifford + 1).buffer(
                num_of_sequences
            ).save("Q")
            I_st.buffer(n_avg).map(qua.FUNCTIONS.average()).buffer(max_circuit_depth / delta_clifford + 1).average().save(
                "I_avg"
            )
            Q_st.buffer(n_avg).map(qua.FUNCTIONS.average()).buffer(max_circuit_depth / delta_clifford + 1).average().save(
                "Q_avg"
            )

#####################################
#  Open Communication with the QOP  #
#####################################
qmm = qm_api.QuantumMachinesManager(host=qop_ip, cluster_name=cluster_name)

###########################
# Run or Simulate Program #
###########################
simulate = False

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = qm_api.SimulationConfig(duration=10_000)  # In clock cycles = 4ns
    job = qmm.simulate(config, rb, simulation_config)
    job.get_simulated_samples().con1.plot()

else:
    # Open the quantum machine
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(rb)
    # Get results from QUA program
    if state_discrimination:
        results = fetching_tool(job, data_list=["state_avg", "iteration"], mode="live")
    else:
        results = fetching_tool(job, data_list=["I_avg", "Q_avg", "iteration"], mode="live")
    # Live plotting
    fig = plt.figure()
    interrupt_on_close(fig, job)  # Interrupts the job when closing the figure
    # data analysis
    x = np.arange(0, max_circuit_depth + 0.1, delta_clifford)
    x[0] = 1  # to set the first value of 'x' to be depth = 1 as in the experiment
    while results.is_processing():
        # data analysis
        if state_discrimination:
            state_avg, iteration = results.fetch_all()
            value_avg = state_avg
        else:
            I, Q, iteration = results.fetch_all()
            value_avg = I

        # Progress bar
        progress_counter(iteration, num_of_sequences, start_time=results.get_start_time())
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
    print("### Fitted Parameters ###")
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

    # np.savez("rb_values", value)