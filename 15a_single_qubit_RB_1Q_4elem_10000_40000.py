# %%
"""
        SINGLE QUBIT RANDOMIZED BENCHMARKING
The program consists in playing random sequences of Clifford gates and measuring the state of the resonator afterward.
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
from qualang_tools.loops import from_array
from qualang_tools.plot import interrupt_on_close
from qualang_tools.results import fetching_tool, progress_counter
from scipy.optimize import curve_fit

from configuration_with_lffem_csrack import *
# from configuration_with_lffem import *
from macros_initialization_and_readout_2q import *
from macros_rb import *
from macros_voltage_gate_sequence import VoltageGateSequence

##############################
# Program-specific variables #
##############################

# target_qubits = ["qubit5"]
target_qubits = ["qubit5", "qubit5_dup1", "qubit5_dup2", "qubit5_dup3"]
target_tank_circuit = "tank_circuit2"
plungers = "P4-P5"
do_feedback = False  # False for test. True for actual.
# seed = np.random.randint(2**31)  # Pseudo-random number generator seed
full_read_init = False
num_output_streams = 6 if full_read_init else 2

# n_avg = 1000
num_of_sequences = 3  # Number of random sequences
# circuit_depth_min = 0
# target = 100_000
local_depth_max = 10_000  # ~16k should work
print(f"local_depth_max = {local_depth_max}")

# Override for development
n_avg = 3
seed = 1
target = 40_000
print(f"target = {target}")

# circuit_depths = [int(_) for _ in circuit_depths]
duration_compensation_pulse = target * PI_LEN


# duration_init includes the manipulation
delay_ops_start = 68
# duration_rb = PI_LEN * circuit_depth_max * 2 # 2 is a bit bigger than 1.875 (or)
duration_rb = PI_LEN * 10 * 2
delay_ops_end = 60
# duration_ops = delay_rb_start + duration_rb + delay_rb_end


duration_compensation_pulse_rb = 800_000  # duration_rb
duration_compensation_pulse = int(0.3 * duration_compensation_pulse_full_initialization + duration_compensation_pulse_rb + duration_compensation_pulse_full_readout)
duration_compensation_pulse = 100 * (duration_compensation_pulse // 100)


seq.add_points("operation_P1-P2", level_ops["P1-P2"], delay_ops_start + delay_ops_end)
seq.add_points("operation_P4-P5", level_ops["P4-P5"], delay_ops_start + delay_ops_end)
seq.add_points("operation_P3", level_ops["P3"], delay_ops_start + delay_ops_end)


###################################
# Helper functions and QUA macros #
###################################


def calc_sequence_offline(seq_seed, target):
    a = 137939405
    c = 12345
    m = 2**28
    x = seq_seed
    _seq = []
    _seq_names = []
    cayley = c1_table.flatten().tolist()
    cur_state = 0
    for i in range(target):
        x = (a * x + c) % m
        step = np.floor((x / 2**28) * 24).astype(int)
        # step = 12
        _seq.append(step)
        cur_state = cayley[cur_state * 24 + step]
        _seq_names.append(map_clifford_numbers_to_string[step])
    _seq.append(inv_gates[cur_state])
    _seq_names.append(map_clifford_numbers_to_string[inv_gates[cur_state]])

    return _seq, _seq_names


def generate_sequence_by_section(seq_seed, target, start, end):
    end = target if end > target else end
    delta = end - start
    if delta <= 0:
        return declare(int, value=None, size=1), declare(int), declare(int)

    cayley = declare(int, value=c1_table.flatten().tolist())
    time_table = declare(int, value=map_clifford_to_duration_cycles_list)
    inv_list = declare(int, value=inv_gates)
    current_state = declare(int)
    step = declare(int)
    sequence = declare(int, value=None, size=delta + 1)
    sequence_time_before = declare(int)
    sequence_time_after = declare(int)
    i = declare(int)
    rand = Random(seed=seq_seed)

    assign(current_state, 0)
    assign(sequence_time_before, 0)
    # assign(sequence_time_after, 0)

    if start > 0:  # then, compute the total time before start
        with for_(i, 0, i < start, i + 1):
            assign(step, rand.rand_int(24))
            assign(current_state, cayley[current_state * 24 + step])
            assign(sequence_time_before, sequence_time_before + time_table[step])
    with for_(i, start, i < end, i + 1):
        assign(step, rand.rand_int(24))
        assign(current_state, cayley[current_state * 24 + step])
        assign(sequence[i - start], step)
    if end < target:  # then, compute the total time after end till target
        with for_(i, end, i < target, i + 1):
            assign(step, rand.rand_int(24))
            assign(current_state, cayley[current_state * 24 + step])
            assign(sequence_time_after, sequence_time_after + time_table[step])
    assign(sequence[delta], inv_list[current_state])
    if end < target:
        assign(sequence_time_after, sequence_time_after + time_table[inv_list[current_state]])

    return sequence, sequence_time_before, sequence_time_after


###################
# The QUA program #
###################
with program() as PROG_RB:
    depth = [declare(int) for _ in range(len(target_qubits))]  # QUA variable for the varying depth
    saved_gate = [declare(int) for _ in range(len(target_qubits))]  # QUA variable for the saved gate

    m = declare(int)  # QUA variable for the random sequence
    n = [declare(int) for _ in range(len(target_qubits))]  # QUA variable for the averages
    I = [declare(fixed) for _ in range(len(target_qubits))]  # QUA variable for the 'I' quadrature
    Q = [declare(fixed) for _ in range(len(target_qubits))]  # QUA variable for the 'Q' quadrature
    P = [declare(bool) for _ in range(len(target_qubits))]  # QUA variable for state discrimination

    # The relevant streams
    m_st = declare_stream()
    I_st = [declare_stream() for _ in range(num_output_streams)]
    Q_st = [declare_stream() for _ in range(num_output_streams)]
    P_st = [declare_stream() for _ in range(num_output_streams)]
    print(calc_sequence_offline(seed, target))

    with for_(m, 0, m < num_of_sequences, m + 1):  # QUA for_ loop over the random sequences
        align(*target_qubits)
        for i, qb in enumerate(target_qubits):
            sequence, sequence_time_before, sequence_time_after = generate_sequence_by_section(
                seed,
                target=target,  # target depth
                start=i * local_depth_max,  # start depth for this element
                end=(i + 1) * local_depth_max,  # end depth for this element
            )
            # wait((250 + 3 * (i == 0) + 9 * (i == 2)) + sequence_time_before, qb)  # Calibrated for pi=52ns, local_depth_max=10, target=25, n_avg=3
            # wait(200 - 0 * (i == 1) - 0 * (i == 2) - 0 * (i == 3) + sequence_time_before, qb)
            wait(100 - 4 * (i == 1) - 4 * (i == 2) - (131 + 1_250 + 12_500 + 118 + 125_000 + 21_000 - 8) * (i == 3) + sequence_time_before, qb)
            play_sequence_by_section(sequence, target, qb=qb, start=i * local_depth_max, end=(i + 1) * local_depth_max)
            # wait(200 - 16 * (i == 1) - 0 * (i == 2) - 0 * (i == 3) + sequence_time_after, qb) # Calibrated for pi=52ns, local_depth_max=10, target=25, n_avg=3
            wait(100 + sequence_time_after, qb)


#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(host=qop_ip, port=qop_port, cluster_name=cluster_name, octave=octave_config)

###########################
# Run or Simulate Program #
###########################
simulate = False

if simulate:
    # # Simulates the QUA program for the specified duration
    # simulation_config = SimulationConfig(duration=4_000)  # In clock cycles = 4ns
    # job = qmm.simulate(config, rb, simulation_config)

    # plt.figure()
    # job.get_simulated_samples().con1.plot()
    # # Get the waveform report
    # samples = job.get_simulated_samples()
    # waveform_report = job.get_simulated_waveform_report()
    # waveform_report.create_plot(samples, plot=True, save_path=None)
    # plt.legend("")
    # plt.show()
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=1_000_000)  # In clock cycles = 4ns
    # Simulate blocks python until the simulation is done
    job = qmm.simulate(config, PROG_RB, simulation_config, compiler_options=CompilerOptionArguments(flags=["not-strict-timing"]))
    # Plot the simulated samples
    waveform_report = job.plot_waveform_report_without_samples()
    # job.get_simulated_samples().con1.plot()
    # plt.show()

else:
    # Open the quantum machine
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(PROG_RB, compiler_options=CompilerOptionArguments(flags=["not-strict-timing"]))

# %%
