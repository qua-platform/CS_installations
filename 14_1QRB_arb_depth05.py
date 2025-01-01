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

qubit = "qubit5"
qubit_trio1 = f"{qubit}_trio1"
qubit_trio2 = f"{qubit}_trio2"
tank_circuit = "tank_circuit1"

# Number of of averages for each random sequence
n_avg = 2
num_of_sequences = 3  # Number of random sequences
max_circuit_depth = 4000  # Maximum circuit depth
delta_clifford = 10  #  Play each sequence with a depth step equals to 'delta_clifford - Must be > 0
assert max_circuit_depth % delta_clifford == 0, "max_circuit_depth / delta_clifford must be an integer."

seed = 34553  # Pseudo-random number generator seed

# Flag to enable state discrimination if the readout has been calibrated (rotated blobs and threshold)
state_discrimination = False

ge_threshold = 0.155  # arbitrary atm, in V


# Time in ns for RB sequence to execute play_sequence(), will be buffer after ramping to idle
# Note, with low max_circuit_depth, the delay before readout will increase slightly
RB_delay = 92

minus_x90_len = PI_LEN
minus_y90_len = PI_LEN
x180_len = PI_LEN
x90_len = PI_LEN
y180_len = PI_LEN
y90_len = PI_LEN


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
    step = declare(int)
    sequence = declare(int, size=max_circuit_depth)
    inv_gate = declare(int)
    i = declare(int)
    rand = Random(seed=seed)

    with for_(i, 0, i < max_circuit_depth - 1, i + 1):
        assign(step, rand.rand_int(24))
        assign(current_state, cayley[current_state * 24 + step])
        assign(sequence[i], step)
    
    # step = 0
    assign(inv_gate, inv_list[current_state])
    assign(sequence[max_circuit_depth - 1], inv_gate)

    return sequence


def play_clifford(c_idx, qb):
    with switch_(c_idx, unsafe=True):
        with case_(0):
            wait(x180_len // 4, qb)
        with case_(1):
            play("x180_square", qb)
        with case_(2):
            play("y180_square", qb)
        with case_(3):
            play("y180_square", qb)
            play("x180_square", qb)
        with case_(4):
            play("x90_square", qb)
            play("y90_square", qb)
        with case_(5):
            play("x90_square", qb)
            play("-y90_square", qb)
        with case_(6):
            play("-x90_square", qb)
            play("y90_square", qb)
        with case_(7):
            play("-x90_square", qb)
            play("-y90_square", qb)
        with case_(8):
            play("y90_square", qb)
            play("x90_square", qb)
        with case_(9):
            play("y90_square", qb)
            play("-x90_square", qb)
        with case_(10):
            play("-y90_square", qb)
            play("x90_square", qb)
        with case_(11):
            play("-y90_square", qb)
            play("-x90_square", qb)
        with case_(12):
            play("x90_square", qb)
        with case_(13):
            play("-x90_square", qb)
        with case_(14):
            play("y90_square", qb)
        with case_(15):
            play("-y90_square", qb)
        with case_(16):
            play("-x90_square", qb)
            play("y90_square", qb)
            play("x90_square", qb)
        with case_(17):
            play("-x90_square", qb)
            play("-y90_square", qb)
            play("x90_square", qb)
        with case_(18):
            play("x180_square", qb)
            play("y90_square", qb)
        with case_(19):
            play("x180_square", qb)
            play("-y90_square", qb)
        with case_(20):
            play("y180_square", qb)
            play("x90_square", qb)
        with case_(21):
            play("y180_square", qb)
            play("-x90_square", qb)
        with case_(22):
            play("x90_square", qb)
            play("y90_square", qb)
            play("x90_square", qb)
        with case_(23):
            play("-x90_square", qb)
            play("y90_square", qb)
            play("-x90_square", qb)


def play_sequence(sequence_list, depth, qb):
    i = declare(int)
    with for_(i, 0, i <= depth, i + 1):
        play_clifford(c_idx=sequence_list[i], qb=qb)


# Macro to calculate exact duration of generated sequence at a given depth
def generate_sequence_time(sequence_list, depth):
    j = declare(int)
    duration = declare(int)
    assign(duration, 0)  # Ensures duration is reset to 0 for every depth calculated
    with for_(j, 0, j <= depth, j + 1):
        with switch_(sequence_list[j], unsafe=True):
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
    return duration




###################
# The QUA program #
###################
with program() as PROG_RB:
    depth1 = declare(int, value=max_circuit_depth)  # QUA variable for the varying depth
    depth2 = declare(int, value=max_circuit_depth)  # QUA variable for the varying depth
    # QUA variable to store the last Clifford gate of the current sequence which is replaced by the recovery gate
    saved_gate = declare(int)
    m = declare(int)  # QUA variable for the loop over random sequences
    n = declare(int)  # QUA variable for the averaging loop
    I = declare(fixed)  # QUA variable for the 'I' quadrature
    Q = declare(fixed)  # QUA variable for the 'Q' quadrature
    state = declare(bool)  # QUA variable for state discrimination
    # assign_variables_to_element(tank_circuit, I, Q)

    # The relevant streams
    m_st = declare_stream()
    I_st = declare_stream()
    Q_st = declare_stream()
    state_st = declare_stream()
    
    rep = declare(int)
    current_state = declare(int, value=0)
    saved_gate1 = declare(int, value=0)
    saved_gate2 = declare(int, value=0)
    sequence_time1 = declare(int, value=0)
    sequence_time2 = declare(int, value=0)

    with for_(m, 0, m < num_of_sequences, m + 1):  # QUA for_ loop over the random sequences
        # sequence_list, inv_gate_list = generate_sequence() # Generate the random sequence of length max_circuit_depth

        with for_(n, 0, n < n_avg, n + 1):  # Averaging loop

            with strict_timing_():

                with for_(rep, 0, rep < 5, rep + 1):
                    sequence_list1 = generate_sequence() # Generate the random sequence of length max_circuit_depth
                    assign(sequence_time1, generate_sequence_time(sequence_list1, depth1))
                    # assign_variables_to_element(qubit, sequence_list1, sequence_time1)
                    play_sequence(sequence_list1, depth1, qubit)

                with for_(rep, 0, rep < 5, rep + 1):
                    sequence_list2 = generate_sequence() # Generate the random sequence of length max_circuit_depth
                    assign(sequence_time2, generate_sequence_time(sequence_list2, depth2))
                    # assign_variables_to_element(qubit_trio1, sequence_list2, sequence_time2)
                    play_sequence(sequence_list2, depth2, qubit_trio1)

            wait(25_000)
        # Save the counter for the progress bar
        save(m, m_st)

#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(
    host=qop_ip, port=qop_port, cluster_name=cluster_name, octave=octave_config
)
qmm.clear_all_job_results()
qmm.close_all_qms()

###########################
# Run or Simulate Program #
###########################
simulate = False

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=40_000)  # In clock cycles = 4ns
    job = qmm.simulate(config, PROG_RB, simulation_config)

    plt.figure()
    job.get_simulated_samples().con1.plot()
    # Get the waveform report
    samples = job.get_simulated_samples()
    waveform_report = job.get_simulated_waveform_report()
    waveform_report.create_plot(samples, plot=True, save_path=None)
    plt.legend("")
    plt.show()

else:
    from qm import generate_qua_script
    sourceFile = open("debug_14_1QRB_arb_depth04.py", "w")
    print(generate_qua_script(PROG_RB, config), file=sourceFile)
    sourceFile.close()

    # Open the quantum machine
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(PROG_RB, compiler_options=CompilerOptionArguments(flags=["not-strict-timing"]))


# %%
