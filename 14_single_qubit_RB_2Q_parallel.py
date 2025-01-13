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
from qualang_tools.loops import from_array
from qualang_tools.plot import interrupt_on_close
from qualang_tools.results import fetching_tool, progress_counter
from scipy.optimize import curve_fit

from configuration_with_lffem import *
from macros import get_other_elements
from macros_initialization_and_readout import *
from macros_rb import *
from macros_voltage_gate_sequence import VoltageGateSequence

# from configuration_with_opxplus import *

# matplotlib.use('TkAgg')


##############################
# Program-specific variables #
##############################

target_qubits = ["qubit4", "qubit5"]
target_tank_circuit = "tank_circuit2"
plungers = "P4-P5"  # "full", "P1-P2", "P4-P5"
do_feedback = False  # False for test. True for actual.
seed = 123  # Pseudo-random number generator seed
num_output_streams = 6 if plungers == "full" else 2

n_avg = 2
seed = 0
num_of_sequences = 3  # Number of random sequences
circuit_depth_min = 1000
circuit_depth_max = 7800  # worked up to 7800
delta_clifford = 100
circuit_depths = np.arange(circuit_depth_min, circuit_depth_max + 1, delta_clifford) * u.ns
# circuit_depths = [int(_) for _ in circuit_depths]
duration_compensation_pulse_rb = circuit_depth_max * PI_LEN
assert circuit_depth_max % delta_clifford == 0, "circuit_depth_max / delta_clifford must be an integer."


# duration_init includes the manipulation
delay_ops_start = 68
delay_ops_end = 60  # 108


duration_compensation_pulse = int(0.3 * duration_compensation_pulse_full_initialization + duration_compensation_pulse_rb + duration_compensation_pulse_full_readout)
duration_compensation_pulse = 100 * (duration_compensation_pulse // 100)


seq.add_points("operation_P1-P2", level_ops["P1-P2"], delay_ops_start + delay_ops_end)
seq.add_points("operation_P4-P5", level_ops["P4-P5"], delay_ops_start + delay_ops_end)
seq.add_points("operation_P3", level_ops["P3"], delay_ops_start + delay_ops_end)


###################
# The QUA program #
###################
with program() as rb:
    depth1 = declare(int)  # QUA variable for the varying depth
    depth2 = declare(int)  # QUA variable for the varying depth
    duration_ops = declare(int)
    duration_q5 = declare(int)

    m = declare(int)  # QUA variable for the loop over random sequences
    n = declare(int)  # QUA variable for the averaging loop
    I = [declare(fixed) for _ in range(2)]  # QUA variable for the 'I' quadrature
    Q = [declare(fixed) for _ in range(2)]  # QUA variable for the 'Q' quadrature
    P = [declare(bool) for _ in range(2)]  # QUA variable for state discrimination

    current_state1 = declare(int, value=0)
    current_state2 = declare(int, value=0)
    sequence_time1 = declare(int)  # QUA variable for RB sequence duration for a given depth
    sequence_time2 = declare(int)  # QUA variable for RB sequence duration for a given depth
    # Ensure that the result variables are assigned to the measurement elements
    assign_variables_to_element(tank_circuits[0], I[0], Q[0])
    assign_variables_to_element(tank_circuits[1], I[1], Q[1])

    # The relevant streams
    m_st = declare_stream()
    I_st = [declare_stream() for _ in range(num_output_streams)]
    Q_st = [declare_stream() for _ in range(num_output_streams)]
    P_st = [declare_stream() for _ in range(num_output_streams)]

    with for_(*from_array(depth1, circuit_depths)):  # Loop over the depths
        assign(depth2, depth1)

        with for_(m, 0, m < num_of_sequences, m + 1):  # QUA for_ loop over the random sequences
            sequence_list1, _ = generate_sequence(current_state1, depth=depth1, max_circuit_depth=circuit_depth_max, ends_with_inv_gate=True, seed=seed)
            sequence_list2, _ = generate_sequence(current_state2, depth=depth2, max_circuit_depth=circuit_depth_max, ends_with_inv_gate=True, seed=seed)

            # sequence_list1 = declare(int, value=[ 6, 11, 18,  1, 17, 12, 16,  8, 11,  6])
            # sequence_list2 = declare(int, value=[ 6, 11, 18,  1, 17, 12, 16,  8, 11,  6])

            # Assign sequence_time to duration of idle step for generated sequence "m" at a given depth
            assign(sequence_time1, generate_sequence_time(sequence_list1, depth1))
            assign(sequence_time2, generate_sequence_time(sequence_list2, depth2))
            assign(duration_ops, delay_ops_start + sequence_time1 + delay_ops_end)

            with for_(n, 0, n < n_avg, n + 1):  # Averaging loop
                with strict_timing_():
                    # Perform specified initialization
                    perform_initialization(I, Q, P, I_st, Q_st, P_st, kind=plungers)

                    # Navigate through the charge stability map
                    seq.add_step(voltage_point_name=f"operation_{plungers}", duration=duration_ops)
                    other_elements = get_other_elements(elements_in_use=target_qubits + sweep_gates, all_elements=all_elements)
                    wait(duration_ops >> 2, *other_elements)

                    play_sequence(sequence_list1, depth1, qb=target_qubits[0])
                    play_sequence(sequence_list2, depth2, qb=target_qubits[1])

                    # Perform specified readout
                    perform_readout(I, Q, P, I_st, Q_st, P_st, kind=plungers)

                    # Play compensatin pulse
                    seq.add_compensation_pulse(duration=duration_compensation_pulse)

                seq.ramp_to_zero()
                wait(1000 * u.ns)

        # Save the counter for the progress bar
        save(m, m_st)

    with stream_processing():
        m_st.save("iteration")
        for k in range(num_output_streams):
            I_st[k].buffer(n_avg).buffer(num_of_sequences).buffer(len(circuit_depths)).save(f"I{k + 1:d}")
            # Q_st[k].buffer(n_avg).buffer(num_of_sequences).buffer(len(circuit_depths)).save(f"Q{k + 1:d}")
            # P_st[k].boolean_to_int().buffer(n_avg).buffer(num_of_sequences).buffer(len(circuit_depths)).save(f"P{k + 1:d}")
            # I_st[k].buffer(n_avg).map(FUNCTIONS.average()).buffer(len(circuit_depths)).average().save(f"I{k + 1:d}_avg")
            # Q_st[k].buffer(n_avg).map(FUNCTIONS.average()).buffer(len(circuit_depths)).average().save(f"Q{k + 1:d}_avg")
            # P_st[k].boolean_to_int().buffer(n_avg).map(FUNCTIONS.average()).buffer(len(circuit_depths)).average().save(f"P{k + 1:d}_avg")


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
    results = fetching_tool(job, data_list=["iteration", "I1", "I2"], mode="live")
    # Live plotting
    fig = plt.figure()
    interrupt_on_close(fig, job)  # Interrupts the job when closing the figure
    # data analysis
    threshold = TANK_CIRCUIT_CONSTANTS[target_tank_circuit]["threshold"]
    while results.is_processing():
        # data analysis
        iteration, I1, I2 = results.fetch_all()
        P1 = I1 > threshold
        P2 = I2 > threshold

        P2_avg = P2.astype(int).mean(axis=2).mean(axis=1)

        print(job.execution_report())
        # Progress bar
        progress_counter(iteration, num_of_sequences, start_time=results.get_start_time())

        # Plot averaged values
        plt.cla()
        plt.plot(circuit_depths, P2_avg, marker=".")
        plt.xlabel("Number of Clifford gates")
        plt.ylabel("Sequence Fidelity")
        plt.title("Single qubit RB")
        plt.pause(1)

    # At the end of the program, fetch the non-averaged results to get the error-bars
    iteration, I1, I2 = results.fetch_all()
    P1 = I1 > threshold
    P2 = I2 > threshold
    value_avg = P2.astype(int).mean(axis=2).mean(axis=1)
    error_avg = P2.astype(int).mean(axis=2).std(axis=1)

    # data analysis
    x = circuit_depths
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
    print(f"Error rate: 1-p = {np.format_float_scientific(one_minus_p, precision=2)} ({stdevs[2]:.1})\n" f"Clifford set infidelity: r_c = {np.format_float_scientific(r_c, precision=2)} ({r_c_std:.1})\n" f"Gate infidelity: r_g = {np.format_float_scientific(r_g, precision=2)}  ({r_g_std:.1})")

    # Plots
    plt.figure()
    plt.errorbar(x, value_avg, yerr=error_avg, marker=".")
    plt.plot(x, power_law(x, *pars), linestyle="--", linewidth=2)
    plt.xlabel("Number of Clifford gates")
    plt.ylabel("Sequence Fidelity")
    plt.title("Single qubit RB")

    # np.savez("rb_values", value)
    # Close the quantum machines at the end in order to put all flux biases to 0 so that the fridge doesn't heat-up
    qm.close()

# %%
