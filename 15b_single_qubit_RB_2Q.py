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
from qualang_tools.results.data_handler import DataHandler

from configuration_with_lffem_csrack import *
# from configuration_with_lffem import *
from macros_initialization_and_readout_2q import *
from macros_rb import *
from macros_voltage_gate_sequence import VoltageGateSequence

# matplotlib.use('TkAgg')


##############################
# Program-specific variables #
##############################

qubits = ["qubit5", "qubit4"]
sweep_gates = ["P4_sticky", "P3_sticky"]
tank_circuit = "tank_circuit2"
threshold = TANK_CIRCUIT_CONSTANTS[tank_circuit]["threshold"]
num_output_streams = 2
wf_type = "square"
seed = 1234  # Pseudo-random number generator seed

n_avg = 2
num_of_sequences = 3  # Number of random sequences
circuit_depth_min = 1000
circuit_depth_max = 7000 # worked up to 15500
delta_clifford = 1000
circuit_depths = np.arange(circuit_depth_min, circuit_depth_max + 1, delta_clifford)
pi_len = QUBIT_CONSTANTS[qubit]["square_pi_len"]
assert (circuit_depth_max - circuit_depth_min) % delta_clifford == 0

save_data_dict = {
    "qubits": qubits,
    "sweep_gates": sweep_gates,
    "tank_circuit": tank_circuit,
    "seed": seed,
    "n_avg": n_avg,
    "num_of_sequences": num_of_sequences,
    "circuit_depth_min": circuit_depth_min,
    "circuit_depth_max": circuit_depth_max,
    "delta_clifford": delta_clifford,
    "config": config,
}


###################
# The QUA program #
###################
with program() as rb:
    d_ops = declare(int)
    depth1 = declare(int)  # QUA variable for the varying depth
    depth2 = declare(int)  # QUA variable for the varying depth
    duration_ops = declare(int)

    m = declare(int)  # QUA variable for the loop over random sequences
    n = declare(int)  # QUA variable for the averaging loop
    I = declare(fixed)  # QUA variable for the 'I' quadrature
    Q = declare(fixed)  # QUA variable for the 'Q' quadrature
    P0 = declare(bool)  # QUA variable for state discrimination
    P1 = declare(bool)  # QUA variable for state discrimination
    P2 = declare(bool)  # QUA variable for state discrimination
    P_diff_st = declare_stream()  #
    # The relevant streams
    i_depth = declare(int, value=0)
    i_depth_st = declare_stream()

    sequence_time1 = declare(int)  # QUA variable for RB sequence duration for a given depth
    sequence_time2 = declare(int)  # QUA variable for RB sequence duration for a given depth

    # Ensure that the result variables are assigned to the measurement elements
    assign_variables_to_element(tank_circuit, I, Q, P0, P1, P2)

    current_level = declare(fixed, value=[0.0 for _ in sweep_gates])
    seq.current_level = current_level

    if set_init_as_dc_offset:
        for sg, lvl_init in zip(sweep_gates, level_init_list):
            set_dc_offset(sg, "single", lvl_init)

    with for_(*from_array(depth1, circuit_depths)):  # Loop over the depths
        assign(depth2, depth1)
        assign(i_depth, i_depth + 1)

        with for_(m, 0, m < num_of_sequences, m + 1):  # QUA for_ loop over the random sequences
            sequence_list1 = generate_sequence(depth=depth1, max_circuit_depth=circuit_depth_max, seed=seed)
            sequence_list2 = declare(int, size=circuit_depth_max + 1)
            j = declare(int)
            with for_(j, 0, j <= circuit_depth_max, j + 1):
                assign(sequence_list2[j], sequence_list1[j])

            # Assign sequence_time to duration of idle step for generated sequence "m" at a given depth
            assign(sequence_time1, generate_sequence_time(sequence_list1, depth1))
            assign(sequence_time2, generate_sequence_time(sequence_list2, depth2))
            assign(d_ops, (RF_SWITCH_DELAY + sequence_time1 + RF_SWITCH_DELAY))

            with for_(n, 0, n < n_avg, n + 1):  # Averaging loop
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
                seq.add_step(voltage_point_name="initialization_1q", duration=d_ops, ramp_duration=duration_ramp_init) # NEVER u.ns
                # seq.add_step(voltage_point_name="initialization_1q", duration=(RF_SWITCH_DELAY + pi_len + RF_SWITCH_DELAY), ramp_duration=duration_ramp_init) # NEVER u.ns
                
                wait(duration_ramp_init // 4, "rf_switch", qubit)
                play("trigger", "rf_switch", duration=d_ops >> 2)
                wait(RF_SWITCH_DELAY // 4, qubit)
                with strict_timing_():
                    play_sequence(sequence_list1, depth1, qb=qubits[0], wf_type=wf_type)
                    play_sequence(sequence_list2, depth2, qb=qubits[1], wf_type=wf_type)

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
                wait(250)

        # Save the counter for the progress bar
        save(i_depth, i_depth_st)

    with stream_processing():
        i_depth_st.save("iteration")
        P_diff_st.buffer(n_avg).map(FUNCTIONS.average())\
            .buffer(num_of_sequences).map(FUNCTIONS.average())\
            .buffer(len(circuit_depths)).save(f"P_diff_{tank_circuit}")


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

    results = fetching_tool(job, data_list=["iteration"], mode="live")

    import time

    # data analysis
    while results.is_processing():
        iteration = results.fetch_all()
        # Progress bar
        progress_counter(iteration[0], len(circuit_depths), start_time=results.get_start_time())
        time.sleep(1)

    fetch_names = ["iteration", f"P_diff_{tank_circuit}"]
    results = fetching_tool(job, data_list=fetch_names)

    # At the end of the program, fetch the non-averaged results to get the error-bars
    iteration, P_diff = results.fetch_all()
    save_data_dict["P_diff"] = P_diff


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
    log_cov = f"A = {pars[0]:.3} ({stdevs[0]:.1}), B = {pars[1]:.3} ({stdevs[1]:.1}), p = {pars[2]:.3} ({stdevs[2]:.1})"
    print(log_cov)
    print("Covariance Matrix")
    print(cov)
    save_data_dict["log_cov"] = log_cov

    one_minus_p = 1 - pars[2]
    r_c = one_minus_p * (1 - 1 / 2**1)
    r_g = r_c / (44 / 24)  # 1.875  # 1.875 is the average number of gates in clifford operation
    r_c_std = stdevs[2] * (1 - 1 / 2**1)
    r_g_std = r_c_std / (44 / 24)  # 1.875

    print("#########################")
    print("### Useful Parameters ###")
    print("#########################")
    log_this = f"Error rate: 1-p = {np.format_float_scientific(one_minus_p, precision=2)} ({stdevs[2]:.1})\n" f"Clifford set infidelity: r_c = {np.format_float_scientific(r_c, precision=2)} ({r_c_std:.1})\n" f"Gate infidelity: r_g = {np.format_float_scientific(r_g, precision=2)}  ({r_g_std:.1})"
    print(log_this)
    save_data_dict["log_this"] = log_this

    # Plots
    fig_analysis = plt.figure()
    plt.plot(x, P_diff, marker=".")
    plt.plot(x, power_law(x, *pars), linestyle="--", linewidth=2)
    plt.xlabel("Number of Clifford gates")
    plt.ylabel("Sequence Fidelity")
    plt.title("Single qubit RB")
    plt.show()

    # Close the quantum machines at the end in order to put all flux biases to 0 so that the fridge doesn't heat-up
    # np.savez("rb_values", value)

    # Save results
    script_name = Path(__file__).name
    data_handler = DataHandler(root_data_folder=save_dir)
    save_data_dict.update({"fig_analysis": fig_analysis})
    data_handler.additional_files = {
        script_name: script_name,
        **default_additional_files,
    }
    data_handler.save_data(data=save_data_dict, name=script_name.replace(".py", ""))

    qm.close()

# %%
