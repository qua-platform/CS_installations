# %%
"""
        Pauli Spin Blockade search
The goal of the script is to find the PSB region according to the protocol described in Nano Letters 2020 20 (2), 947-952.
To do so, the charge stability map is acquired by scanning the voltages provided by an external DC source,
to the DC part of the bias-tees connected to the plunger gates, while 2 OPX channels are stepping the voltages on the fast
lines of the bias-tees to navigate through the triangle in voltage space (empty - random initialization - measurement).

Depending on the cut-off frequency of the bias-tee, it may be necessary to adjust the barycenter (voltage offset) of each
triangle so that the fast line of the bias-tees sees zero voltage in average. Otherwise, the high-pass filtering effect
of the bias-tee will distort the fast pulses over time. A function has been written for this.

In the current implementation, the OPX is also measuring (either with DC current sensing or RF-reflectometry) during the
readout window (last segment of the triangle).
A single-point averaging is performed and the data is extracted while the program is running to display the results line-by-line.

Prerequisites:
    - Readout calibration (resonance frequency for RF reflectometry and sensor operating point for DC current sensing).
    - Setting the parameters of the external DC source using its driver.
    - Connect the two plunger gates (DC line of the bias-tee) to the external dc source.
    - Connect the OPX to the fast line of the plunger gates for playing the triangle pulse sequence.

Before proceeding to the next node:
    - Identify the PSB region and update the config.
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
from scipy import signal

from configuration_with_lffem import *
from macros_voltage_gate_sequence import VoltageGateSequence
from macros_initialization_and_readout_2q import *

matplotlib.use('TkAgg')


###################
# The QUA program #
###################

run_live = True
set_init_as_dc_offset = True
amplitude_scaling = 4.7 # (DC port / AC port) of bias tee 

level_init_arr = np.array([-0.02, 0.02]) * amplitude_scaling
level_readout_center_arr = np.array([-0.00, +0.00]) * amplitude_scaling
level_readout_from_arr = np.array([-0.005, +0.005]) * amplitude_scaling + level_readout_center_arr
level_readout_to_arr = np.array([+0.005, -0.005]) * amplitude_scaling + level_readout_center_arr

n_shots = 1000
n_detunings = 100
sweep_gates = ["P0_sticky", "P1_sticky"]
tank_circuit = "tank_circuit1"
threshold = TANK_CIRCUIT_CONSTANTS[tank_circuit]["threshold"]

duration_init = 10_000 # DO NOT USE * u.ns
duration_ramp_init = 200
duration_readout = 1_000 + REFLECTOMETRY_READOUT_LEN # DO NOT USE * u.ns
duration_ramp_readout = 52 # DO NOT USE * u.ns


if set_init_as_dc_offset:
    level_readout_from_offset_arr = level_readout_from_arr - level_init_arr
    level_readout_to_offset_arr = level_readout_to_arr - level_init_arr
    level_init_offset_arr = np.array([0.0, 0.0]) # level_init_arr - level_init_arr

level_readout_from_list = level_readout_from_arr.tolist()
level_readout_to_list = level_readout_to_arr.tolist()
level_init_list = level_init_arr.tolist()
level_readout_from_offset_list = level_readout_from_offset_arr.tolist()
level_readout_to_offset_list = level_readout_to_offset_arr.tolist()
level_init_offset_list = level_init_offset_arr.tolist()

voltages_Px = np.linspace(level_readout_from_offset_arr[0], level_readout_to_offset_arr[0], n_detunings)
voltages_Py = np.linspace(level_readout_from_offset_arr[1], level_readout_to_offset_arr[1], n_detunings)

print(f"level init: {level_init_list}")
print(f"level readout from: {level_readout_from_list}")
print(f"level readout to: {level_readout_from_list}")
print(f"level init after offset: {level_init_offset_list}")
print(f"level readout from after offset: {level_readout_from_offset_list}")
print(f"level readout to after offset: {level_readout_to_offset_list}")

print(f"level readout on {sweep_gates[0]}: {voltages_Px}")
print(f"level readout on {sweep_gates[1]}: {voltages_Py}")


seq = VoltageGateSequence(config, sweep_gates)
seq.add_points("initialization", level_init_offset_list, duration_init)


save_data_dict = {
    "sweep_gates": sweep_gates,
    "tank_circuit": tank_circuit,
    "n_shots": n_shots,
    "voltages_Px": voltages_Px,
    "voltages_Py": voltages_Py,
    "config": config,
}


with program() as PSB_search_prog:
    Vx = declare(fixed)
    Vy = declare(fixed)
    n = declare(int)  # QUA integer used as an index for the averaging loop
    n_st = declare_stream()  # Stream for the iteration number (progress bar)
    I = declare(fixed)
    Q = declare(fixed)
    P1 = declare(bool)
    P2 = declare(bool)
    I_st = declare_stream()
    Q_st = declare_stream()
    P_diff_st = declare_stream()

    current_level = declare(fixed, value=[0.0 for _ in sweep_gates])
    seq.current_level = current_level

    # Ensure that the result variables are assign to the pulse processor used for readout
    assign_variables_to_element("tank_circuit1", I, Q, P1, P2)

    if set_init_as_dc_offset:
        for sg, lvl_init in zip(sweep_gates, level_init_list):
            set_dc_offset(sg, "single", lvl_init)

    with for_(n, 0, n < n_shots, n + 1):
        with for_each_((Vx, Vy), (voltages_Px.tolist(), voltages_Py.tolist())):
            seq.add_step(level=[Vx, Vy], duration=duration_readout, ramp_duration=duration_ramp_readout)
            wait(duration_ramp_readout * u.ns, tank_circuit)
            measure("readout", tank_circuit, None, demod.full("cos", I, "out1"), demod.full("sin", Q, "out1"))
            assign(P1, I > threshold)  # TODO: I > threashold is even?

            align()
            seq.add_step(voltage_point_name="initialization", ramp_duration=duration_ramp_init)
            align()

            seq.add_step(level=[Vx, Vy], duration=duration_readout, ramp_duration=duration_ramp_readout)
            wait(duration_ramp_readout * u.ns, tank_circuit)
            measure("readout", tank_circuit, None, demod.full("cos", I, "out1"), demod.full("sin", Q, "out1"))
            assign(P2, I > threshold)  # TODO: I > threashold is even?

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
        # I_st.buffer(n_detunings).buffer(n_shots).save(f"I_{tank_circuit}")
        # Q_st.buffer(n_detunings).buffer(n_shots).save(f"Q_{tank_circuit}")
        P_diff_st.buffer(n_detunings).average().save(f"P_{tank_circuit}")


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
    job = qmm.simulate(config, PSB_search_prog, simulation_config)
    plt.figure()
    job.get_simulated_samples().con1.plot()
    plt.show()

else:
    # Open the quantum machine
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(PSB_search_prog)

    # Get results from QUA program
    fetch_names = ["iteration", f"P_{tank_circuit}"]
    results = fetching_tool(job, data_list=fetch_names, mode="live")

    bins = np.arange(0.05, 0.30, 0.001)
    x_data_Px = np.tile(voltages_Px + level_init_list[0], (n_shots, 1)).ravel()
    x_data_Py = np.tile(voltages_Py + level_init_list[1], (n_shots, 1)).ravel()
 
    fig = plt.figure()
    interrupt_on_close(fig, job)  # Interrupts the job when closing the figure
    while results.is_processing():
        # Fetch results
        iteration, P_diff = results.fetch_all()

        # Progress bar
        progress_counter(iteration, n_shots, start_time=results.get_start_time())

        plt.suptitle("PSB Search")
        plt.clf()
        # Plot I
        ax = plt.subplot(2, 2, 1)
        ax.plot(voltages_Px + level_init_arr[0], P_diff, alpha=0.8)
        ax.set_xlabel(f"Abs. {sweep_gates[0]} [V]")
        ax.set_ylabel(f"Average Parity Diff")

        ax = plt.subplot(2, 2, 3)
        ax.plot(voltages_Py + level_init_arr[1], P_diff, alpha=0.8)
        ax.set_xlabel(f"Abs. {sweep_gates[1]} [V]")
        ax.set_ylabel(f"Average Parity Diff")

        # Plot I
        ax = plt.subplot(2, 2, 2)
        ax.plot(voltages_Px, P_diff, alpha=0.8)
        ax.set_xlabel(f"Rel. {sweep_gates[0]} [V]")
        ax.set_ylabel(f"Average Parity Diff")

        ax = plt.subplot(2, 2, 4)
        ax.plot(voltages_Py, P_diff, alpha=0.8)
        ax.set_xlabel(f"Rel. {sweep_gates[1]} [V]")
        ax.set_ylabel(f"Average Parity Diff")

        plt.tight_layout()
        plt.pause(1)

    # Fetch results
    res = results.fetch_all()
    save_data_dict["Pdiff"] = res[1]


    # # Initialize figure
    # import math
    # nbins = 100
    # nrows = math.ceil(math.sqrt(n_detunings))
    # ncols = math.ceil(math.sqrt(n_detunings))
    # fig_analysis, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=(3 * ncols, 2.4 * nrows), sharex=True)

    # # Flatten axes for easy indexing
    # axes = axes.flatten()

    # # Generate histograms for each detuning
    # for i in range(n_detunings):
    #     ax = axes[i]
    #     ax.hist(I[:, i], bins=nbins, color='skyblue', edgecolor='black')
    #     title = f"Vx={voltages_Px[i]:.3f}, Vy={voltages_Py[i]:.3f}"
    #     ax.set_title(title, fontsize=10)
    #     ax.tick_params(axis='both', which='major', labelsize=8)

    # # Set common x-axis label
    # for ax in axes[-nrows:]:
    #     ax.set_xlabel("demod reflectometry signal I [V]", fontsize=12)

    # # Hide unused subplots if n_detunings < total panels
    # for i in range(n_detunings, len(axes)):
    #     fig.delaxes(axes[i])

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

    # qm.close()

# %%
