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
from qualang_tools.voltage_gates import VoltageGateSequence
from scipy import signal

from configuration_with_lffem import *

# matplotlib.use('TkAgg')


###################
# The QUA program #
###################
n_shots = 100  # Number of averages
n_detunings = 25

barrier_gate = "B2_sticky"
sweep_gates = ["P1_sticky", "P2_sticky", barrier_gate]
tank_circuits = ["tank_circuit1", "tank_circuit2"]
num_tank_circuits = len(tank_circuits)

voltage_B = 0.0
level_init = [-0.1, 0.1, voltage_B]
level_readout_min = [-0.05, 0.05, voltage_B]
level_readout_max = [0.1, -0.1, voltage_B]
threshold = [TANK_CIRCUIT_CONSTANTS[tc]["threshold"] for tc in tank_circuits]

duration_init = 100 * u.ns
duration_readout = 200 * u.ns
duration_compensation_pulse = 1 * u.us

voltages_Px = np.linspace(level_readout_min[0], level_readout_max[0], n_detunings)
voltages_Py = np.linspace(level_readout_min[1], level_readout_max[1], n_detunings)

seq = VoltageGateSequence(config, sweep_gates)
seq.add_points("initialization", level_init, duration_init)
for m, (v1, v2) in enumerate(zip(voltages_Px, voltages_Py)):
    # print(f"readout_{m}", v1, v2)
    seq.add_points(f"readout_{m}", [v1, v2, voltage_B], duration_readout)


tank_circuits = ["tank_circuit1", "tank_circuit2"]
num_tank_circuits = len(tank_circuits)


save_data_dict = {
    "sweep_gates": sweep_gates,
    "tank_circuits": tank_circuits,
    "n_shots": n_shots,
    "voltages_Px": voltages_Px,
    "voltages_Py": voltages_Py,
    "config": config,
}


with program() as PSB_search_prog:
    Vx = declare(fixed)
    Vy = declare(fixed)
    Vb = declare(fixed, value=voltage_B)
    n = declare(int)  # QUA integer used as an index for the averaging loop
    n_st = declare_stream()  # Stream for the iteration number (progress bar)
    I = [declare(fixed) for _ in range(num_tank_circuits)]
    Q = [declare(fixed) for _ in range(num_tank_circuits)]
    P = [declare(bool) for _ in range(num_tank_circuits)]
    I_st = [declare_stream() for _ in range(num_tank_circuits)]
    Q_st = [declare_stream() for _ in range(num_tank_circuits)]
    P_st = [declare_stream() for _ in range(num_tank_circuits)]

    # Ensure that the result variables are assign to the pulse processor used for readout
    assign_variables_to_element("tank_circuit1", I[0], Q[0])
    assign_variables_to_element("tank_circuit2", I[1], Q[1])

    with for_(n, 0, n < n_shots, n + 1):
        with for_each_((Vx, Vy), (voltages_Px.tolist(), voltages_Py.tolist())):
            # Play the triangle
            seq.add_step(voltage_point_name="initialization")
            seq.add_step(level=[Vx, Vy, Vb], duration=duration_readout)
            seq.add_compensation_pulse(duration=duration_compensation_pulse)
            # Measure the dot right after the qubit manipulation
            for j, tc in enumerate(tank_circuits):
                measure(
                    "readout",
                    tc,
                    None,
                    demod.full("cos", I[j], "out1"),
                    demod.full("sin", Q[j], "out1"),
                )
                assign(P[j], I[j] > threshold[j])
                save(I[j], I_st[j])
                save(Q[j], Q_st[j])
                save(P[j], P_st[j])

            # process them which can cause the OPX to crash.
            wait(1_000 * u.ns)  # in ns
            # Ramp the voltage down to zero at the end of the triangle (needed with sticky elements)
            seq.ramp_to_zero()

        # Save the LO iteration to get the progress bar
        save(n, n_st)

    # Stream processing section used to process the data before saving it
    with stream_processing():
        n_st.save("iteration")
        for j, tc in enumerate(tank_circuits):
            I_st[j].buffer(n_detunings).buffer(n_shots).save(f"I_{tc}")
            Q_st[j].buffer(n_detunings).buffer(n_shots).save(f"Q_{tc}")
            P_st[j].boolean_to_int().buffer(n_detunings).buffer(n_shots).save(f"P_{tc}")


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
    fetch_names = ["iteration"]
    for tc in tank_circuits:
        fetch_names.append(f"I_{tc}")
        fetch_names.append(f"Q_{tc}")
        fetch_names.append(f"P_{tc}")
    results = fetching_tool(job, data_list=fetch_names, mode="live")
    # Live plotting
    fig = plt.figure()
    interrupt_on_close(fig, job)  # Interrupts the job when closing the figure
    while results.is_processing():
        # Fetch results
        res = results.fetch_all()
        # Progress bar
        progress_counter(res[0], n_shots, start_time=results.get_start_time())

        plt.suptitle("PSB Search")
        for ind, tc in enumerate(tank_circuits):
            I, Q, P = res[3 * ind + 1], res[3 * ind + 2], res[3 * ind + 3]
            x_data = np.tile(voltages_Px, (n_shots, 1)).ravel()

            # Plot I
            ax1 = plt.subplot(3, 2, ind + 1)
            ax1.set_title(tc)
            ax1.scatter(x_data, I, alpha=0.6, s=3)
            # ax1.set_xlabel(f"{sweep_gates[0]} [V]")
            ax1.set_xticklabels([])
            ax1.set_ylabel(f"I [V]")

            # Add secondary x-axis
            ax2 = ax1.twiny()
            ax2.set_xlim(ax1.get_xlim())
            ax2.set_xticks(ax1.get_xticks())
            transformed_ticks = np.interp(
                ax1.get_xticks(),
                [level_readout_min[0], level_readout_max[0]],
                [level_readout_min[1], level_readout_max[1]],
            )
            ax2.set_xticklabels([f"{val:.2f}" for val in transformed_ticks])
            ax2.set_xlabel(f"{sweep_gates[1]} [V]")

            # Plot Q
            ax3 = plt.subplot(3, 2, ind + 3)
            # ax3.set_title(f"Q [V] {tc}")
            ax3.scatter(x_data, Q, alpha=0.6, s=3)
            ax3.set_xlabel(f"{sweep_gates[0]} [V]")
            ax3.set_ylabel(f"Q [V]")
            
            ax4 = plt.subplot(3, 2, ind + 5)
            ax4.plot(x_data, P.mean(axis=0))
            ax3.set_xlabel(f"{sweep_gates[0]} [V]")
            ax3.set_ylabel(f"even parity fraction")

        plt.tight_layout()
        plt.pause(1)

    # Fetch results
    res = results.fetch_all()
    for ind, tc in enumerate(tank_circuits):
        save_data_dict[f"I_{tc}"] = res[2 * ind + 1]
        save_data_dict[f"Q_{tc}"] = res[2 * ind + 2]


    # Initialize figure
    import math
    nbins = 100
    nrows = math.ceil(math.sqrt(n_detunings))
    ncols = math.ceil(math.sqrt(n_detunings))
    fig_analysis, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=(3 * ncols, 2.4 * nrows), sharex=True)

    # Flatten axes for easy indexing
    axes = axes.flatten()

    # Generate histograms for each detuning
    for i in range(n_detunings):
        ax = axes[i]
        ax.hist(I[:, i], bins=nbins, color='skyblue', edgecolor='black')
        title = f"Vx={voltages_Px[i]:.3f}, Vy={voltages_Py[i]:.3f}"
        ax.set_title(title, fontsize=10)
        ax.tick_params(axis='both', which='major', labelsize=8)

    # Set common x-axis label
    for ax in axes:
        ax.set_xlabel("demod reflectometry signal I [V]", fontsize=12)

    # Hide unused subplots if n_detunings < total panels
    for i in range(n_detunings, len(axes)):
        fig.delaxes(axes[i])

    plt.tight_layout()
    plt.show()

    # Save results
    script_name = Path(__file__).name
    data_handler = DataHandler(root_data_folder=save_dir)
    save_data_dict.update({"fig_live": fig, "fig_analysis": fig_analysis})
    data_handler.additional_files = {
        script_name: script_name,
        **default_additional_files,
    }
    data_handler.save_data(data=save_data_dict, name=Path(__name__).stem)

    qm.close()

# %%
