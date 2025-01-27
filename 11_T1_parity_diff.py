# %%
"""
        RAMSEY-LIKE CHEVRON - using standard QUA (pulse > 16ns and 4ns granularity)
The goal of the script is to acquire exchange driven coherent oscillations by sweeping the idle time and detuning.
The QUA program is divided into three sections:
    1) step between the initialization, idle and measurement points using sticky elements (long timescale).
    2) apply two delta-g driven pi-half pulses separated by a low detuning pulse to increase J, using non-sticky elements (short timescale).
    3) measure the state of the qubit using either RF reflectometry or dc current sensing via PSB or Elzerman readout.
A compensation pulse can be added to the long timescale sequence in order to ensure 0 DC voltage on the fast line of
the bias-tee. Alternatively one can obtain the same result by changing the offset of the slow line of the bias-tee.

In the current implementation, the qubit pulses are played using the real-time pulse manipulation of the OPX, which is
fast and can be arbitrarily long. However, the minimum pulse length is 16ns and the sweep step must be larger than 4ns.
Also note that the qubit pulses are played at the end of the global "idle" level whose duration is fixed.

Prerequisites:
    - Readout calibration (resonance frequency for RF reflectometry and sensor operating point for DC current sensing).
    - Setting the DC offsets of the external DC voltage source.
    - Connecting the OPX to the fast line of the plunger gates.
    - Having calibrated the initialization and readout point from the charge stability map and updated the configuration.
    - Having calibrated the delta-g driven pi-half parameters (detuning level and duration).

Before proceeding to the next node:
    - Extract the qubit frequency and T2*...
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

from configuration_with_lffem_csrack import *
# from configuration_with_lffem import *
from macros_initialization_and_readout_2q import *
from macros_voltage_gate_sequence import VoltageGateSequence

# matplotlib.use('TkAgg')


###################
# Local Macros #
###################


def perform_read_init(I, Q, P0_st, P1_st):
    P0 = measure_parity(I, Q, None, None, None, P0_st, tank_circuit=tank_circuit, threshold=threshold)

    # conditional pi pulse
    align()
    with if_(P0):
        seq.add_step(voltage_point_name="initialization_1q", duration=(RF_SWITCH_DELAY + pi_len + RF_SWITCH_DELAY), ramp_duration=duration_ramp_init)  # NEVER u.ns
        wait(duration_ramp_init // 4, "rf_switch", qubit)
        play("trigger", "rf_switch", duration=(RF_SWITCH_DELAY + pi_len + RF_SWITCH_DELAY) // 4)
        wait(RF_SWITCH_DELAY // 4, qubit)
        play("x180_square", qubit)

    align()
    P1 = measure_parity(I, Q, None, None, None, P1_st, tank_circuit=tank_circuit, threshold=threshold)

    return P0, P1


###################
# The QUA program #
###################

n_avg = 1000  # Number of averages

qubit = "qubit5"
sweep_gates = ["P4_sticky", "P3_sticky"]
tank_circuit = "tank_circuit2"
threshold = TANK_CIRCUIT_CONSTANTS[tank_circuit]["threshold"]
num_output_streams = 3
x180 = "x180_square"

# Pulse duration sweep in ns - must be larger than 4 clock cycles
tau_min = 16
tau_max = 10_000_000
tau_step = 100_000
durations = np.arange(tau_min, tau_max, tau_step)
# n_tau_steps = 101
# durations = np.geomspace(tau_min, tau_max, n_tau_steps).astype(int)

pi_len = QUBIT_CONSTANTS[qubit]["square_pi_len"]
pi_amp = QUBIT_CONSTANTS[qubit]["square_pi_amp"]

save_data_dict = {
    "sweep_gates": sweep_gates,
    "tank_circuit": tank_circuit,
    "durations": durations,
    "n_avg": n_avg,
    "config": config,
}


with program() as ramsey_with_detuning:
    d = declare(int)
    d_ops = declare(int)  # QUA variable for the qubit pulse duration
    n = declare(int)  # QUA integer used as an index for the averaging loop
    n_st = declare_stream()  # Stream for the iteration number (progress bar)

    I = declare(fixed)
    Q = declare(fixed)

    I_st = declare_stream()
    P_st = [declare_stream() for _ in range(num_output_streams)]

    current_level = declare(fixed, value=[0.0 for _ in sweep_gates])
    seq.current_level = current_level

    # Ensure that the result variables are assign to the pulse processor used for readout
    assign_variables_to_element(tank_circuit, I, Q)

    if set_init_as_dc_offset:
        for sg, lvl_init in zip(sweep_gates, level_init_list):
            set_dc_offset(sg, "single", lvl_init)

    with for_(n, 0, n < n_avg, n + 1):
        save(n, n_st)

        with for_(*from_array(d, durations)):  # Loop over the qubit pulse duration
        # with for_each_(d, durations):
            assign(d_ops, RF_SWITCH_DELAY + d + pi_len + RF_SWITCH_DELAY)

            P0, P1 = perform_read_init(I, Q, P_st[0], P_st[1])

            # Play the triangle
            align()
            seq.add_step(voltage_point_name="initialization_1q", duration=d_ops, ramp_duration=duration_ramp_init)  # NEVER u.ns

            wait(duration_ramp_init // 4, "rf_switch", qubit)
            play("trigger", "rf_switch", duration=d_ops >> 2)
            wait(RF_SWITCH_DELAY // 4, qubit)

            play(x180, qubit)
            wait(d >> 2, qubit)

            align()
            P2 = measure_parity(I, Q, None, None, None, P_st[2], tank_circuit=tank_circuit, threshold=threshold)

            # DO NOT REMOVE: bring the voltage back to dc_offset level.
            # Without this, it can accumulate a precision error that leads to unwanted large voltage (max of the range).
            align()
            seq.ramp_to_zero()

            # Save the LO iteration to get the progress bar
            wait(25_000)

        # Save the LO iteration to get the progress bar
        save(n, n_st)

    # Stream processing section used to process the dat[0, :]a before saving it.
    with stream_processing():
        n_st.save("iteration")
        # I_st.buffer(len(durations)).buffer(n_avg).save(f"I_{tank_circuit}")
        for k in range(num_output_streams):
            P_st[k].boolean_to_int().buffer(len(durations)).average().save(f"P{k:d}_{tank_circuit}")


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
    simulation_config = SimulationConfig(duration=1_000)  # In clock cycles = 4ns
    # Simulate blocks python until the simulation is done
    job = qmm.simulate(config, ramsey_with_detuning, simulation_config)
    # Plot the simulated samples
    plt.figure()
    job.get_simulated_samples().con1.plot()
    plt.show()

else:
    # Open the quantum machine
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(
        ramsey_with_detuning,
        compiler_options=CompilerOptionArguments(flags=["not-strict-timing"]),
    )

    # Get results from QUA program
    # fetch_names = ["iteration", f"P_diff_{tank_circuit}", f"P_diff_{tank_circuit}"]
    fetch_names = ["iteration"] + [f"P{k:d}_{tank_circuit}" for k in range(num_output_streams)]
    # fetch_names = ["iteration", f"I_{tank_circuit}"]

    results = fetching_tool(job, data_list=fetch_names, mode="live")
    # results = fetching_tool(job, data_list=fetch_names)
    # iteration, I2 = results.fetch_all()

    # fig = plt.figure()
    # plt.hist(I2[:, -1], bins=201, color='skyblue', edgecolor='black');
    # plt.show()

    # Live plotting
    fig = plt.figure()
    # interrupt_on_close(fig, job)  # Interrupts the job when closing the figure
    while results.is_processing():
        # Fetch results
        iteration, P0, P1, P2 = results.fetch_all()
        # Progress bar
        progress_counter(iteration, n_avg, start_time=results.get_start_time())
        # Plot results
        plt.suptitle(f"Ramsey with detuning: {tank_circuit}")
        # Plot results
        plt.clf()
        plt.plot(durations, P0)
        plt.plot(durations, P1)
        plt.plot(durations, P2)
        plt.legend(["P0", "P1", "P2"])
        plt.xlabel("Idle Time [ns]")
        plt.ylabel("Average Parity")
        plt.tight_layout()
        plt.pause(1)

    # Fetch results
    iteration, P0, P1, P2 = results.fetch_all()
    # save_data_dict["P_diff"] = P_diff

    # # Fit the data
    # try:
    #     from qualang_tools.plot.fitting import Fit

    #     fig_analyses = [] * 2
    #     for i, sgn in enumerate([-1, 1]):
    #         fit = Fit()
    #         fig_analysis = plt.figure(figsize=(6, 6))
    #         ramsey_fit = fit.ramsey(total_durations, P_diff[i, :], plot=True)
    #         qubit_T2 = np.abs(ramsey_fit["T2"][0])
    #         qubit_detuning = ramsey_fit["f"][0] * u.GHz - sgn * detuning
    #         plt.xlabel("Total Evolution Time [ns]")
    #         plt.ylabel("Average Parity Diff")
    #         print(f"Qubit detuning to update in the config: qubit_IF += {-qubit_detuning:.0f} Hz")
    #         print(f"T2h = {qubit_T2:.0f} ns")
    #         plt.legend((f"detuning = {-qubit_detuning / u.kHz:.3f} kHz", f"T2* = {qubit_T2:.0f} ns"))
    #         plt.title(f"Hahn Echo measurement for {qubit}, {tank_circuit}")
    #         fig_analyses.append(fig_analysis)
    #         save_data_dict.update({f"fig_analysis{i}": fig_analysis})
    # except:
    #     pass
    # finally:
    #     plt.show()

    # Save results
    script_name = Path(__file__).name
    data_handler = DataHandler(root_data_folder=save_dir)
    save_data_dict.update({"fig_live": fig})
    data_handler.additional_files = {
        script_name: script_name,
        **default_additional_files,
    }
    data_handler.save_data(data=save_data_dict, name=script_name.replace(".py", ""))

    qm.close()

# %%
