# %%
"""
        CHIRP spectroscopy
"""

import matplotlib
import matplotlib.pyplot as plt
from qm import QuantumMachinesManager, SimulationConfig
from qm.qua import *
from qualang_tools.addons.variables import assign_variables_to_element
from qualang_tools.loops import from_array
from qualang_tools.plot import interrupt_on_close
from qualang_tools.results import fetching_tool, progress_counter
from qualang_tools.results.data_handler import DataHandler
from macros_voltage_gate_sequence import VoltageGateSequence
from scipy import signal

from configuration_with_lffem import *
from macros_initialization_and_readout_2q import *

matplotlib.use('TkAgg')


###################
# The QUA program #
###################

n_avg = 1000  # Number of averages

qubit = "qubit1"
sweep_gates = ["P0_sticky", "P1_sticky"]
tank_circuit = "tank_circuit1"
threshold = TANK_CIRCUIT_CONSTANTS[tank_circuit]["threshold"]
num_output_streams = 2

freqs = np.arange(0e6, 300e6, 1e6)

save_data_dict = {
    "sweep_gates": sweep_gates,
    "tank_circuit": tank_circuit,
    "n_avg": n_avg,
    "config": config,
}


with program() as QUBIT_CHIRP:
    f = declare(int)
    n = declare(int)  # QUA integer used as an index for the averaging loop
    n_st = declare_stream()  # Stream for the iteration number (progress bar)
    I = declare(fixed)
    Q = declare(fixed)
    P1 = declare(bool)
    P2 = declare(bool)
    I_st = [declare_stream() for _ in range(num_output_streams)]
    Q_st = [declare_stream() for _ in range(num_output_streams)]
    P_st = [declare_stream() for _ in range(num_output_streams)]
    P_diff_st = declare_stream()
    
    current_level = declare(fixed, value=[0.0 for _ in sweep_gates])
    seq.current_level = current_level

    # Ensure that the result variables are assign to the pulse processor used for readout
    assign_variables_to_element("tank_circuit1", I, Q, P1, P2)

    if set_init_as_dc_offset:
        for sg, lvl_init in zip(sweep_gates, level_init_list):
            set_dc_offset(sg, "single", lvl_init)

    with for_(n, 0, n < n_avg, n + 1):
        with for_(*from_array(f, freqs)):
            update_frequency(qubit, f)

            P1 = measure_parity(I, Q, None, None, None, None, tank_circuit, threshold)
            
            # Play the triangle
            align()
            seq.add_step(voltage_point_name="initialization_1q", ramp_duration=duration_ramp_init) # NEVER u.ns

            wait(duration_ramp_init // 4, "rf_switch", qubit)
            play("trigger", "rf_switch", duration=(RF_SWITCH_DELAY + CONST_LEN) // 4)
            wait(RF_SWITCH_DELAY // 4, qubit)
            # play("const", qubit, chirp=(19841,"Hz/nsec"))
            play("const", qubit)
            # play("x180_kaiser", qubit)

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

        # Save the LO iteration to get the progress bar
        save(n, n_st)

    # Stream processing section used to process the data before saving it
    with stream_processing():
        n_st.save("iteration")
        # for idx in range(num_output_streams):
        #     I_st[idx].buffer(len(freqs)).save_all(f"I{idx}_{tank_circuit}")
        #     Q_st[idx].buffer(len(freqs)).save_all(f"Q{idx}_{tank_circuit}")
        #     P_st[idx].boolean_to_int().buffer(len(freqs)).save_all(f"P{idx}_{tank_circuit}")
        # P_diff_st.buffer(len(freqs)).save_all(f"P_diff_{tank_circuit}")

        # for idx in range(num_output_streams):
        #     I_st[idx].buffer(len(freqs)).average().save(f"I{idx}_avg_{tank_circuit}")
        #     Q_st[idx].buffer(len(freqs)).average().save(f"Q{idx}_avg_{tank_circuit}")
        #     P_st[idx].boolean_to_int().buffer(len(freqs)).average().save(f"P{idx}_avg_{tank_circuit}")
        P_diff_st.buffer(len(freqs)).average().save(f"P_diff_avg_{tank_circuit}")


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
    simulation_config = SimulationConfig(duration=2_000)  # In clock cycles = 4ns
    job = qmm.simulate(config, QUBIT_CHIRP, simulation_config)
    plt.figure()
    job.get_simulated_samples().con1.plot()
    plt.show()

else:
    # Open the quantum machine
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(QUBIT_CHIRP)

    # Get results from QUA program
    # fetch_names = ["iteration", f"P_diff_{tank_circuit}", f"P_diff_avg_{tank_circuit}"]
    fetch_names = ["iteration", f"P_diff_avg_{tank_circuit}"]

    results = fetching_tool(job, data_list=fetch_names, mode="live")

    fig = plt.figure()
    # interrupt_on_close(fig, job)  # Interrupts the job when closing the figure
    
    while results.is_processing():
        # Fetch results
        iteration, P_diff_avg = results.fetch_all()

        # Progress bar
        progress_counter(iteration, n_avg, start_time=results.get_start_time())

        plt.suptitle("Qubit Chirp Spectroscopy")
        plt.clf()

        plt.plot(freqs / u.MHz, P_diff_avg)
        plt.xlabel("Freq [MHz]")
        plt.ylabel("Average Parity Diff")


        # ax = plt.subplot(4, 2, 1)
        # ax.plot(freqs / u.MHz, np.abs(S1))
        # plt.xlabel("Freq [MHz]")
        # plt.ylabel("R1 [V]")

        # ax = plt.subplot(4, 2, 3)
        # ax.plot(freqs / u.MHz, np.unwrap(np.angle(S1)))
        # plt.xlabel("Freq [MHz]")
        # plt.ylabel("Phase1 [rad]")

        # ax = plt.subplot(4, 2, 5)
        # ax.plot(freqs / u.MHz, P1)
        # plt.xlabel("Freq [MHz]")
        # plt.ylabel("Average Parity1")

        # ax = plt.subplot(4, 2, 2)
        # ax.plot(freqs / u.MHz, np.abs(S2))
        # plt.xlabel("Freq [MHz]")
        # plt.ylabel("R2 [V]")

        # ax = plt.subplot(4, 2, 4)
        # ax.plot(freqs / u.MHz, np.unwrap(np.angle(S2)))
        # plt.xlabel("Freq [MHz]")
        # plt.ylabel("Phase2 [rad]")

        # ax = plt.subplot(4, 2, 6)
        # ax.plot(freqs / u.MHz, P2)
        # plt.xlabel("Freq [MHz]")
        # plt.ylabel("Average Parity2")

        # ax = plt.subplot(4, 2, 7)
        # ax.plot(freqs / u.MHz, Pdiff)
        # plt.xlabel("Freq [MHz]")
        # plt.ylabel("Average Parity Diff")

        plt.tight_layout()
        plt.pause(1)

    # Fetch results
    iteration, P_diff_avg = results.fetch_all()
    # save_data_dict["P_diff"] = P_diff
    save_data_dict["P_diff_avg"] = P_diff_avg 

    # # Get results from QUA program
    # fetch_names = []
    # for idx in range(num_output_streams):
    #     fetch_names.extend([f"I{idx}_{tank_circuit}", f"Q{idx}_{tank_circuit}", f"P{idx}_{tank_circuit}"])
    # fetch_names.append(f"P_diff_{tank_circuit}")

    # results = fetching_tool(job, data_list=fetch_names)
    
    #     "(0, 0)": (P1 == 0) & (P2 == 0),
    #     "(1, 0)": (P1 == 1) & (P2 == 0),
    #     "(0, 1)": (P1 == 0) & (P2 == 1),
    #     "(1, 1)": (P1 == 1) & (P2 == 1),
    # }

    # # Prepare the plot
    # fig_analysis, axes = plt.subplots(2, 2, figsize=(10, 8))
    # axes = axes.flatten()
    # # Plot for each condition
    # for idx, (label, condition) in enumerate(conditions.items()):
    #     # Apply condition and calculate mean over axis 0
    #     masked_dR = np.where(condition, np.abs(S2) - np.abs(S1), np.nan)
    #     mean_dR = np.nanmean(masked_dR, axis=0)

    #     # Plot the result
    #     ax = axes[idx]
    #     ax.plot(mean_dR, marker='o', label=f"(P1, P2): {label}")
    #     ax.set_title(f"(P1, P2): {label}")
    #     ax.set_xlabel("Freq [MHz]")
    #     ax.set_ylabel("Mean R values")
    #     ax.legend()

    # plt.tight_layout()
    # plt.show()


    # Save results
    script_name = Path(__file__).name
    data_handler = DataHandler(root_data_folder=save_dir)
    save_data_dict.update({"fig_live": fig})
    data_handler.additional_files = {
        script_name: script_name,
        **default_additional_files,
    }
    data_handler.save_data(data=save_data_dict, name=script_name.replace(".py",""))

    qm.close()

# %%
