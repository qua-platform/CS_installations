# %%
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

import matplotlib.pyplot as plt
from qm import (CompilerOptionArguments, QuantumMachinesManager,
                SimulationConfig)
from qm.qua import *
from qualang_tools.addons.variables import assign_variables_to_element
from qualang_tools.bakery.randomized_benchmark_c1 import c1_table
from qualang_tools.plot import interrupt_on_close
from qualang_tools.results import fetching_tool, progress_counter
from qualang_tools.voltage_gates import VoltageGateSequence
from scipy.optimize import curve_fit

from configuration_with_lffem import *


##############################
# Program-specific variables #
##############################

qubits = ["qubit1", "qubit2"]
tank_circuits = ["tank_circuit1", "tank_circuit2"]

RB_delay = 92

x180_len = PI_LEN
x90_len = PI_HALF_LEN
minus_x90_len = PI_HALF_LEN
y180_len = PI_LEN
y90_len = PI_HALF_LEN
minus_y90_len = PI_HALF_LEN


# Number of of averages for each random sequence
n_avg = 2
num_of_sequences = 3  # Number of random sequences
max_circuit_depth = 100  # Maximum circuit depth
delay_init_start = 16
delta_clifford = 10  #  Play each sequence with a depth step equals to 'delta_clifford - Must be > 0
duration_init_wo_rb = delay_init_start + RB_delay
duration_compensation_pulse = max_circuit_depth * PI_LEN
assert max_circuit_depth % delta_clifford == 0, "max_circuit_depth / delta_clifford must be an integer."

seed = 123  # Pseudo-random number generator seed

# Flag to enable state discrimination if the readout has been calibrated (rotated blobs and threshold)
state_discrimination = False


# seq = VoltageGateSequence(config, sweep_gates)
seq = VoltageGateSequence(config, sweep_gates)
seq.add_points("initialization", level_init, duration_init)
seq.add_points("idle", level_manip, duration_manip)
seq.add_points("readout", level_readout, duration_readout)

# Time in ns for RB sequence to execute play_sequence(), will be buffer after ramping to idle
# Note, with low max_circuit_depth, the delay before readout will increase slightly


###################################
# Helper functions and QUA macros #
###################################

# List of recovery gates from the lookup table
inv_gates = [int(np.where(c1_table[i, :] == 0)[0][0]) for i in range(24)]


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


def play_clifford(c_idx, qb):
    with switch_(c_idx, unsafe=True):
        with case_(0):
            wait(x180_len // 4, qb)
        with case_(1):
            play("square_x180", qb)
        with case_(2):
            play("square_y180", qb)
        with case_(3):
            play("square_y180", qb)
            play("square_x180", qb)
        with case_(4):
            play("square_x90", qb)
            play("square_y90", qb)
        with case_(5):
            play("square_x90", qb)
            play("square_-y90", qb)
        with case_(6):
            play("square_-x90", qb)
            play("square_y90", qb)
        with case_(7):
            play("square_-x90", qb)
            play("square_-y90", qb)
        with case_(8):
            play("square_y90", qb)
            play("square_x90", qb)
        with case_(9):
            play("square_y90", qb)
            play("square_-x90", qb)
        with case_(10):
            play("square_-y90", qb)
            play("square_x90", qb)
        with case_(11):
            play("square_-y90", qb)
            play("square_-x90", qb)
        with case_(12):
            play("square_x90", qb)
        with case_(13):
            play("square_-x90", qb)
        with case_(14):
            play("square_y90", qb)
        with case_(15):
            play("square_-y90", qb)
        with case_(16):
            play("square_-x90", qb)
            play("square_y90", qb)
            play("square_x90", qb)
        with case_(17):
            play("square_-x90", qb)
            play("square_-y90", qb)
            play("square_x90", qb)
        with case_(18):
            play("square_x180", qb)
            play("square_y90", qb)
        with case_(19):
            play("square_x180", qb)
            play("square_-y90", qb)
        with case_(20):
            play("square_y180", qb)
            play("square_x90", qb)
        with case_(21):
            play("square_y180", qb)
            play("square_-x90", qb)
        with case_(22):
            play("square_x90", qb)
            play("square_y90", qb)
            play("square_x90", qb)
        with case_(23):
            play("square_-x90", qb)
            play("square_y90", qb)
            play("square_-x90", qb)


def add_clifford_duration(c_idx, duration):

    with switch_(c_idx, unsafe=True):
        with case_(0):
            # wait(x180_len // 4, qb)
            assign(duration, duration + x180_len)
        with case_(1):
            # play("x180", qb)
            assign(duration, duration + x180_len)
        with case_(2):
            # play("y180", qb)
            assign(duration, duration + y180_len)
        with case_(3):
            # play("y180", qb)
            # play("x180", qb)
            assign(duration, duration + y180_len + x180_len)
        with case_(4):
            # play("x90", qb)
            # play("y90", qb)
            assign(duration, duration + x90_len + y90_len)
        with case_(5):
            # play("x90", qb)
            # play("-y90", qb)
            assign(duration, duration + x90_len + minus_y90_len)
        with case_(6):
            # play("-x90", qb)
            # play("y90", qb)
            assign(duration, duration + minus_x90_len + y90_len)
        with case_(7):
            # play("-x90", qb)
            # play("-y90", qb)
            assign(duration, duration + minus_x90_len + minus_y90_len)
        with case_(8):
            # play("y90", qb)
            # play("x90", qb)
            assign(duration, duration + y90_len + x90_len)
        with case_(9):
            # play("y90", qb)
            # play("-x90", qb)
            assign(duration, duration + y90_len + minus_x90_len)
        with case_(10):
            # play("-y90", qb)
            # play("x90", qb)
            assign(duration, duration + minus_y90_len + x90_len)
        with case_(11):
            # play("-y90", qb)
            # play("-x90", qb)
            assign(duration, duration + minus_y90_len + minus_x90_len)
        with case_(12):
            # play("x90", qb)
            assign(duration, duration + x90_len)
        with case_(13):
            # play("-x90", qb)
            assign(duration, duration + minus_x90_len)
        with case_(14):
            # play("y90", qb)
            assign(duration, duration + y90_len)
        with case_(15):
            # play("-y90", qb)
            assign(duration, duration + minus_y90_len)
        with case_(16):
            # play("-x90", qb)
            # play("y90", qb)
            # play("x90", qb)
            assign(duration, duration + minus_x90_len + y90_len + x90_len)
        with case_(17):
            # play("-x90", qb)
            # play("-y90", qb)
            # play("x90", qb)
            assign(duration, duration + minus_x90_len + minus_y90_len + x90_len)
        with case_(18):
            # play("x180", qb)
            # play("y90", qb)
            assign(duration, duration + x180_len + y90_len)
        with case_(19):
            # play("x180", qb)
            # play("-y90", qb)
            assign(duration, duration + x180_len + minus_y90_len)
        with case_(20):
            # play("y180", qb)
            # play("x90", qb)
            assign(duration, duration + y180_len + x90_len)
        with case_(21):
            # play("y180", qb)
            # play("-x90", qb)
            assign(duration, duration + y180_len + minus_x90_len)
        with case_(22):
            # play("x90", qb)
            # play("y90", qb)
            # play("x90", qb)
            assign(duration, duration + x90_len + y90_len + x90_len)
        with case_(23):
            # play("-x90", qb)
            # play("y90", qb)
            # play("-x90", qb)
            assign(duration, duration + minus_x90_len + y90_len + minus_x90_len)


def play_sequence(sequence_list, depth, qb):
    i = declare(int)
    with for_(i, 0, i <= depth, i + 1):
        play_clifford(sequence_list[i], qb=qb)


# Macro to calculate exact duration of generated sequence at a given depth
def generate_sequence_time(sequence_list, depth):
    j = declare(int)
    duration = declare(int)
    assign(duration, 0)  # Ensures duration is reset to 0 for every depth calculated
    with for_(j, 0, j <= depth, j + 1):
        add_clifford_duration(sequence_list[j], duration)
    return duration


###################
# The QUA program #
###################
with program() as rb:
    depth = declare(int)  # QUA variable for the varying depth
    depth_target = declare(int)
    # QUA variable to store the last Clifford gate of the current sequence which is replaced by the recovery gate
    saved_gate = declare(int)
    m = declare(int)  # QUA variable for the loop over random sequences
    n = declare(int)  # QUA variable for the averaging loop
    I = [declare(fixed) for _ in range(2)]  # QUA variable for the 'I' quadrature
    Q = [declare(fixed) for _ in range(2)]  # QUA variable for the 'Q' quadrature
    state = [declare(bool) for _ in range(2)]  # QUA variable for state discrimination
    sequence_time = declare(int)  # QUA variable for RB sequence duration for a given depth
    # Ensure that the result variables are assigned to the measurement elements
    assign_variables_to_element(tank_circuits[0], I[0], Q[0], state[0])
    assign_variables_to_element(tank_circuits[1], I[1], Q[1], state[1])

    # The relevant streams
    m_st = declare_stream()
    I_st = [declare_stream() for _ in range(2)]
    Q_st = [declare_stream() for _ in range(2)]
    state_st = [declare_stream() for _ in range(2)]

    with for_(m, 0, m < num_of_sequences, m + 1):  # QUA for_ loop over the random sequences
        sequence_list, inv_gate_list = generate_sequence() # Generate the random sequence of length max_circuit_depth

        assign(depth_target, 1)  # Initialize the current depth to 1

        with for_(depth, 1, depth <= max_circuit_depth, depth + 1):  # Loop over the depths
            # Replacing the last gate in the sequence with the sequence's inverse gate
            # The original gate is saved in 'saved_gate' and is being restored at the end
            assign(saved_gate, sequence_list[depth])
            assign(sequence_list[depth], inv_gate_list[depth - 1])

            # Only played the depth corresponding to target_depth
            with if_(depth == depth_target):
                # Assign sequence_time to duration of idle step for generated sequence "m" at a given depth
                assign(sequence_time, generate_sequence_time(sequence_list, depth))

                with for_(n, 0, n < n_avg, n + 1):  # Averaging loop
                    
                    with strict_timing_():
                    
                        # Define voltage steps
                        seq.add_step(voltage_point_name="initialization", duration=sequence_time + duration_init_wo_rb) 
                        seq.add_step(voltage_point_name="readout", duration=REFLECTOMETRY_READOUT_LEN)
                        seq.add_compensation_pulse(duration=duration_compensation_pulse)

                        wait((duration_init >> 2), *qubits)
                        for qb in qubits:
                            play_sequence(sequence_list, depth, qb=qb)

                        wait((duration_init >> 2) + (sequence_time >> 2) + (RB_delay >> 2), *tank_circuits)  # Includes calculated RB duration as well as RB sequence processing time
                        for i, tc in enumerate(tank_circuits):
                            measure(
                                "readout",
                                tc,
                                None,
                                demod.full("cos", I[i], "out1"),
                                demod.full("sin", Q[i], "out1"),
                            )

                    # Make sure you updated the ge_threshold and angle if you want to use state discrimination
                    # Save the results to their respective streams
                    for i in range(2):
                        save(I[i], I_st[i])
                        save(Q[i], Q_st[i])
                        if state_discrimination:
                            save(state[i], state_st[i])

                    seq.ramp_to_zero()

                # Go to the next depth
                assign(depth_target, depth_target + delta_clifford)
            # Reset the last gate of the sequence back to the original Clifford gate
            # (that was replaced by the recovery gate at the beginning)
            assign(sequence_list[depth], saved_gate)
        # Save the counter for the progress bar
        save(m, m_st)

    with stream_processing():
        m_st.save("iteration")
        for i, tc in enumerate(tank_circuits):
            I_st[i].buffer(n_avg).map(FUNCTIONS.average()).buffer(max_circuit_depth / delta_clifford).buffer(num_of_sequences).save(f"I_{tc}")
            Q_st[i].buffer(n_avg).map(FUNCTIONS.average()).buffer(max_circuit_depth / delta_clifford).buffer(num_of_sequences).save(f"Q_{tc}")
            I_st[i].buffer(n_avg).map(FUNCTIONS.average()).buffer(max_circuit_depth / delta_clifford).average().save(f"I_avg_{tc}")
            Q_st[i].buffer(n_avg).map(FUNCTIONS.average()).buffer(max_circuit_depth / delta_clifford).average().save(f"Q_avg_{tc}")
            if state_discrimination:
                # saves a 2D array of depth and random pulse sequences in order to get error bars along the random sequences
                state_st[i].boolean_to_int().buffer(n_avg).map(FUNCTIONS.average()).buffer(max_circuit_depth / delta_clifford).buffer(num_of_sequences).save(f"state_{tc}")
                # returns a 1D array of averaged random pulse sequences vs depth of circuit for live plotting
                state_st[i].boolean_to_int().buffer(n_avg).map(FUNCTIONS.average()).buffer(max_circuit_depth / delta_clifford).average().save(f"state_avg_{tc}")


#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(
    host=qop_ip, port=qop_port, cluster_name=cluster_name, octave=octave_config
)

###########################
# Run or Simulate Program #
###########################
simulate = False

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=40_000)  # In clock cycles = 4ns
    job = qmm.simulate(config, rb, simulation_config)

    plt.figure()
    job.get_simulated_samples().con1.plot()
    # Get the waveform report
    samples = job.get_simulated_samples()
    waveform_report = job.get_simulated_waveform_report()
    waveform_report.create_plot(samples, plot=True, save_path=None)
    plt.legend("")
    plt.show()

else:
    # Open the quantum machine
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(
        rb, compiler_options=CompilerOptionArguments(flags=["not-strict-timing"])
    )
    # # Get results from QUA program
    # if state_discrimination:
    #     results = fetching_tool(job, data_list=["state_avg", "iteration"], mode="live")
    # else:
    #     results = fetching_tool(
    #         job, data_list=["I_avg", "Q_avg", "iteration"], mode="live"
    #     )
    # # Live plotting
    # fig = plt.figure()
    # interrupt_on_close(fig, job)  # Interrupts the job when closing the figure
    # # data analysis
    # x = np.arange(1, max_circuit_depth + 0.1, delta_clifford)
    # while results.is_processing():
    #     # data analysis
    #     if state_discrimination:
    #         state_avg, iteration = results.fetch_all()
    #         value_avg = state_avg
    #     else:
    #         I, Q, iteration = results.fetch_all()
    #         value_avg = I

    #     print(job.execution_report())
    #     # Progress bar
    #     progress_counter(
    #         iteration, num_of_sequences, start_time=results.get_start_time()
    #     )
    #     # Plot averaged values
    #     plt.cla()
    #     plt.plot(x, value_avg, marker=".")
    #     plt.xlabel("Number of Clifford gates")
    #     plt.ylabel("Sequence Fidelity")
    #     plt.title("Single qubit RB")
    #     plt.pause(0.1)

#     # At the end of the program, fetch the non-averaged results to get the error-bars
#     if state_discrimination:
#         results = fetching_tool(job, data_list=["state"])
#         state = results.fetch_all()[0]
#         value_avg = np.mean(state, axis=0)
#         error_avg = np.std(state, axis=0)
#     else:
#         results = fetching_tool(job, data_list=["I", "Q"])
#         I, Q = results.fetch_all()
#         value_avg = np.mean(I, axis=0)
#         error_avg = np.std(I, axis=0)

#     # data analysis
#     pars, cov = curve_fit(
#         f=power_law,
#         xdata=x,
#         ydata=value_avg,
#         p0=[0.5, 0.5, 0.9],
#         bounds=(-np.inf, np.inf),
#         maxfev=2000,
#     )
#     stdevs = np.sqrt(np.diag(cov))

#     print("#########################")
#     print("### Fitted Parameters ###")
#     print("#########################")
#     print(
#         f"A = {pars[0]:.3} ({stdevs[0]:.1}), B = {pars[1]:.3} ({stdevs[1]:.1}), p = {pars[2]:.3} ({stdevs[2]:.1})"
#     )
#     print("Covariance Matrix")
#     print(cov)

#     one_minus_p = 1 - pars[2]
#     r_c = one_minus_p * (1 - 1 / 2**1)
#     r_g = r_c / 1.875  # 1.875 is the average number of gates in clifford operation
#     r_c_std = stdevs[2] * (1 - 1 / 2**1)
#     r_g_std = r_c_std / 1.875

#     print("#########################")
#     print("### Useful Parameters ###")
#     print("#########################")
#     print(
#         f"Error rate: 1-p = {np.format_float_scientific(one_minus_p, precision=2)} ({stdevs[2]:.1})\n"
#         f"Clifford set infidelity: r_c = {np.format_float_scientific(r_c, precision=2)} ({r_c_std:.1})\n"
#         f"Gate infidelity: r_g = {np.format_float_scientific(r_g, precision=2)}  ({r_g_std:.1})"
#     )

#     # Plots
#     plt.figure()
#     plt.errorbar(x, value_avg, yerr=error_avg, marker=".")
#     plt.plot(x, power_law(x, *pars), linestyle="--", linewidth=2)
#     plt.xlabel("Number of Clifford gates")
#     plt.ylabel("Sequence Fidelity")
#     plt.title("Single qubit RB")

#     # np.savez("rb_values", value)
#     # Close the quantum machines at the end in order to put all flux biases to 0 so that the fridge doesn't heat-up
#     qm.close()

# %%
