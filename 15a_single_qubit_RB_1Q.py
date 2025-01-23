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

import matplotlib
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

# matplotlib.use('TkAgg')


##############################
# Program-specific variables #
##############################

qubit = "qubit5"
sweep_gates = ["P4_sticky", "P3_sticky"]
tank_circuit = "tank_circuit2"
threshold = TANK_CIRCUIT_CONSTANTS[tank_circuit]["threshold"]
num_output_streams = 2
seed = 345324  # Pseudo-random number generator seed

n_avg = 100
num_of_sequences = 16  # Number of random sequences
# circuit_depth_min = 1
circuit_depth_max = 1000  # worked up to 7800
delta_clifford = 10
circuit_depths = np.arange(1, circuit_depth_max + 0.1, delta_clifford)
pi_len = QUBIT_CONSTANTS[qubit]["square_pi_len"]
pi_amp = QUBIT_CONSTANTS[qubit]["square_pi_amp"]
assert circuit_depth_max % delta_clifford == 0, "circuit_depth_max / delta_clifford must be an integer."


def generate_sequence():
    cayley = declare(int, value=c1_table.flatten().tolist())
    inv_list = declare(int, value=inv_gates)
    current_state = declare(int)
    step = declare(int)
    sequence = declare(int, size=circuit_depth_max + 1)
    inv_gate = declare(int, size=circuit_depth_max + 1)
    i = declare(int)
    rand = Random(seed=seed)

    assign(current_state, 0)
    with for_(i, 0, i < circuit_depth_max, i + 1):
        assign(step, rand.rand_int(24))
        assign(current_state, cayley[current_state * 24 + step])
        assign(sequence[i], step)
        assign(inv_gate[i], inv_list[current_state])

    return sequence, inv_gate


###################
# The QUA program #
###################
with program() as rb:
    dwell = declare(int)
    depth = declare(int)  # QUA variable for the varying depth
    duration_ops = declare(int)

    m = declare(int)  # QUA variable for the loop over random sequences
    n = declare(int)  # QUA variable for the averaging loop
    I = declare(fixed)  # QUA variable for the 'I' quadrature
    Q = declare(fixed)  # QUA variable for the 'Q' quadrature
    P0 = declare(bool)  # QUA variable for state discrimination
    P1 = declare(bool)  # QUA variable for state discrimination
    P2 = declare(bool)  # QUA variable for state discrimination
    saved_gate = declare(int)
    depth_target = declare(int)
    sequence_time = declare(int)  # QUA variable for RB sequence duration for a given depth
    # Ensure that the result variables are assigned to the measurement elements
    assign_variables_to_element(tank_circuit, I, Q, P0, P1, P2)

    # The relevant streams
    # i_depth = declare(int, value=0)
    m_st = declare_stream()
    P_diff_st = declare_stream()

    current_level = declare(fixed, value=[0.0 for _ in sweep_gates])
    seq.current_level = current_level

    if set_init_as_dc_offset:
        for sg, lvl_init in zip(sweep_gates, level_init_list):
            set_dc_offset(sg, "single", lvl_init)

    with for_(m, 0, m < num_of_sequences, m + 1):  # QUA for_ loop over the random sequences
        sequence_list, inv_gate_list = generate_sequence()

        # ss = declare(int)
        # ss_st = declare_stream()
        # with for_(ss, 0, ss < circuit_depth_max, ss + 1):
        #     save(sequence_list[ss], ss_st)
        # save(inv_gate_list[circuit_depth_max-1], ss_st)

        assign(depth_target, 1)  # Initialize the current depth to 1

        with for_(depth, 1, depth <= circuit_depth_max, depth + 1):  # Loop over the depths
            # assign(i_depth, i_depth + 1)

            # Assign sequence_time to duration of idle step for generated sequence "m" at a given depth
            assign(sequence_time, generate_sequence_time(sequence_list, depth))
            assign(dwell, (RF_SWITCH_DELAY + sequence_time + RF_SWITCH_DELAY))

            assign(saved_gate, sequence_list[depth])
            assign(sequence_list[depth], inv_gate_list[depth - 1])

            with if_(depth == depth_target):
                with for_(n, 0, n < n_avg, n + 1):  # Averaging loop
                    # with strict_timing_():
                    # Perform specified initialization
                    P0 = measure_parity(I, Q, None, None, None, None, tank_circuit, threshold)

                    # # conditional pi pulse
                    # align()
                    # with if_(P0):
                    #     seq.add_step(voltage_point_name="initialization_1q", duration=(RF_SWITCH_DELAY + pi_len + RF_SWITCH_DELAY), ramp_duration=duration_ramp_init) # NEVER u.ns
                    #     wait(duration_ramp_init // 4, "rf_switch", qubit)
                    #     play("trigger", "rf_switch", duration=(RF_SWITCH_DELAY + pi_len + RF_SWITCH_DELAY) // 4)
                    #     wait(RF_SWITCH_DELAY // 4, qubit)
                    #     play("x180_square", qubit)

                    P1 = measure_parity(I, Q, None, None, None, None, tank_circuit, threshold)

                    # Navigate through the charge stability map
                    align()
                    seq.add_step(voltage_point_name="initialization_1q", duration=dwell, ramp_duration=duration_ramp_init)  # NEVER u.ns
                    # seq.add_step(voltage_point_name="initialization_1q", duration=(RF_SWITCH_DELAY + pi_len + RF_SWITCH_DELAY), ramp_duration=duration_ramp_init) # NEVER u.ns

                    wait(duration_ramp_init // 4, "rf_switch", qubit)
                    play("trigger", "rf_switch", duration=dwell >> 2)
                    wait(RF_SWITCH_DELAY // 4, qubit)
                    with strict_timing_():
                        play_sequence(sequence_list, depth, qb=qubit)

                    # Perform specified readout
                    align()
                    P2 = measure_parity(I, Q, None, None, None, None, tank_circuit, threshold)

                    # DO NOT REMOVE: bring the voltage back to dc_offset level.
                    # Without this, it can accumulate a precision error that leads to unwanted large voltage (max of the range).
                    align()
                    seq.ramp_to_zero()

                    with if_(P1 == P2):
                        save(0, P_diff_st)
                    with else_():
                        save(1, P_diff_st)

                    # Save the LO iteration to get the progress bar
                    wait(12_500)
                assign(depth_target, depth_target + delta_clifford)
            assign(sequence_list[depth], saved_gate)
        # Save the counter for the progress bar
        save(m, m_st)

    with stream_processing():
        m_st.save("iteration")
        # depth_st.buffer(num_of_sequences).buffer(len(circuit_depths)).save("depths")
        # ss_st.buffer(len(circuit_depths)).buffer(num_of_sequences).save("rb_sequences")
        P_diff_st.buffer(n_avg).map(FUNCTIONS.average()).buffer(circuit_depth_max / delta_clifford).average().save(f"P_diff_{tank_circuit}")


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
    simulation_config = SimulationConfig(duration=4_000)  # In clock cycles = 4ns
    # Simulate blocks python until the simulation is done
    job = qmm.simulate(config, rb, simulation_config)
    # Plot the simulated samples
    job.get_simulated_samples().con1.plot()
    plt.show()

else:
    # Open the quantum machine
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(rb, compiler_options=CompilerOptionArguments(flags=["not-strict-timing"]))
    # job = qm.execute(rb)
    # Get results from QUA program

    results = fetching_tool(job, data_list=["iteration", f"P_diff_{tank_circuit}"], mode="live")

    import time

    # data analysis
    plt.figure()
    while results.is_processing():
        iteration, P_diff = results.fetch_all()
        # data analysis
        # Progress bar
        progress_counter(iteration, num_of_sequences, start_time=results.get_start_time())
        plt.clf()
        plt.plot(circuit_depths, P_diff)
        plt.pause(1)

    # fetch_names = ["iteration", f"P_diff_{tank_circuit}", "depths", "rb_sequences"]
    fetch_names = ["iteration", f"P_diff_{tank_circuit}"]
    results = fetching_tool(job, data_list=fetch_names)

    # At the end of the program, fetch the non-averaged results to get the error-bars
    iteration, P_diff = results.fetch_all()

    # data analysis
    x = circuit_depths
    pars, cov = curve_fit(
        f=power_law,
        xdata=x,
        ydata=P_diff,
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
    r_g = r_c / (44 / 24)  # 1.875  # 1.875 is the average number of gates in clifford operation
    r_c_std = stdevs[2] * (1 - 1 / 2**1)
    r_g_std = r_c_std / (44 / 24)  # 1.875

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
    plt.plot(x, P_diff, marker=".")
    plt.plot(x, power_law(x, *pars), linestyle="--", linewidth=2)
    plt.xlabel("Number of Clifford gates")
    plt.ylabel("Sequence Fidelity")
    plt.title("Single qubit RB")
    plt.show()

    # np.savez("rb_values", value)
    # Close the quantum machines at the end in order to put all flux biases to 0 so that the fridge doesn't heat-up
    qm.close()

# %%
