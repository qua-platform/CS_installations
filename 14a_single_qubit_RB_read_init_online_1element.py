# %%
"""
        SINGLE QUBIT RANDOMIZED BENCHMARKING (for gates >= 40ns)
Each random seqnce is derived on the FPGA for the maximum depth (specified as an input) and played for each depth
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
from macros_initialization_and_readout import *
from macros_rb import *

# from configuration_with_opxplus import *


##############################
# Program-specific variables #
##############################

qubit = "qubit5" # choose "qubit5" for LFFEM. this is to validate the code with the scope.
qubit_trio1 = f"{qubit}_trio1"
qubit_trio2 = f"{qubit}_trio2"

# Number of of averages for each random sequence
n_avg = 1
num_of_sequences = 1  # Number of random sequences
max_circuit_depth = 1000  # Maximum circuit depth
delta_clifford = 10  #  Play each sequence with a depth step equals to 'delta_clifford - Must be > 0
assert max_circuit_depth % delta_clifford == 0, "max_circuit_depth / delta_clifford must be an integer."

seed = 0  # Pseudo-random number generator seed


###################################
# Helper functions and QUA macros #
###################################

def power_law(power, a, b, p):
    return a * (p**power) + b


###################
# The QUA program #
###################
with program() as PROG_RB:
    m = declare(int)  # QUA variable for the loop over random sequences
    n = declare(int)  # QUA variable for the averaging loop
    
    m_st = declare_stream()
    n_st = declare_stream()

    rep1 = declare(int)
    rep2 = declare(int)
    # rep3 = declare(int)

    current_state1 = declare(int, value=0)
    current_state2 = declare(int, value=0)
    # current_state3 = declare(int, value=0)

    depth1 = declare(int, value=max_circuit_depth)
    depth2 = declare(int, value=max_circuit_depth)
    # depth3 = declare(int, value=max_circuit_depth)

    sequence_time1 = declare(int, value=0)
    sequence_time2 = declare(int, value=0)
    # sequence_time3 = declare(int, value=0)

    assign_variables_to_element(qubit, *[rep1, current_state1, depth1, sequence_time1])
    assign_variables_to_element(qubit_trio1, *[rep2, current_state2, depth2, sequence_time2])
    # assign_variables_to_element(qubit_trio2, *[rep3, current_state3, depth3, sequence_time3])

    with for_(m, 0, m < num_of_sequences, m + 1):  # QUA for_ loop over the random sequences

        with for_(n, 0, n < n_avg, n + 1):  # Averaging loop

            with strict_timing_():
                
                ## elem 1
                sequence_list1, current_state1 = generate_sequence(current_state=current_state1, ends_with_inv_gate=False, max_circuit_depth=max_circuit_depth, seed=seed)
                play_sequence(sequence_list1, depth1, qubit)
                ##
                sequence_list1, current_state1 = generate_sequence(current_state=current_state1, ends_with_inv_gate=False, max_circuit_depth=max_circuit_depth, seed=seed)
                assign(sequence_time1, generate_sequence_time(sequence_list1, depth1) - 60_000)
                wait(sequence_time1 >> 2, qubit)
                ##
                sequence_list1, current_state1 = generate_sequence(current_state=current_state1, ends_with_inv_gate=False, max_circuit_depth=max_circuit_depth, seed=seed)
                assign(sequence_time1, generate_sequence_time(sequence_list1, depth1) - 60_000)
                wait(sequence_time1 >> 2, qubit)


                ## elem 2
                sequence_list2, current_state2 = generate_sequence(current_state=current_state2, ends_with_inv_gate=False, max_circuit_depth=max_circuit_depth, seed=seed)
                assign(sequence_time2, generate_sequence_time(sequence_list2, depth2) - 60_000)
                wait(sequence_time2 >> 2, qubit_trio1)
                ##
                sequence_list2, current_state2 = generate_sequence(current_state=current_state2, ends_with_inv_gate=False, max_circuit_depth=max_circuit_depth, seed=seed)
                play_sequence(sequence_list2, depth2, qubit_trio1)
                ##
                sequence_list2, current_state2 = generate_sequence(current_state=current_state2, ends_with_inv_gate=False, max_circuit_depth=max_circuit_depth, seed=seed)
                assign(sequence_time2, generate_sequence_time(sequence_list2, depth2) - 60_000)
                wait(sequence_time2 >> 2, qubit_trio1)


                # ## elem 3
                # sequence_list3, current_state3 = generate_sequence(current_state=current_state3, ends_with_inv_gate=False, max_circuit_depth=max_circuit_depth, seed=seed)
                # assign(sequence_time3, generate_sequence_time(sequence_list3, depth3) - 60_000)
                # wait(sequence_time3 >> 2, qubit_trio2)
                # ##
                # sequence_list3, current_state3 = generate_sequence(current_state=current_state3, ends_with_inv_gate=False, max_circuit_depth=max_circuit_depth, seed=seed)
                # assign(sequence_time3, generate_sequence_time(sequence_list3, depth3) - 60_000)
                # wait(sequence_time3 >> 2, qubit_trio2)
                # ##
                # sequence_list3, current_state3 = generate_sequence(current_state=current_state3, ends_with_inv_gate=False, max_circuit_depth=max_circuit_depth, seed=seed)
                # play_sequence(sequence_list3, depth3, qubit_trio2)


            wait(10_000)


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
    sourceFile = open("debug_14a_single_qubit_RB_read_init_online_1element.py", "w")
    print(generate_qua_script(PROG_RB, config), file=sourceFile)
    sourceFile.close()

    # Open the quantum machine
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(PROG_RB, compiler_options=CompilerOptionArguments(flags=["not-strict-timing"]))


# %%
