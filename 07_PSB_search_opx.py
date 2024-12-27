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
from qualang_tools.loops import from_array
from qualang_tools.plot import interrupt_on_close
from qualang_tools.results import fetching_tool, progress_counter
from qualang_tools.results.data_handler import DataHandler
from qualang_tools.voltage_gates import VoltageGateSequence
from scipy import signal

from configuration_with_lffem import *
from macros import RF_reflectometry_macro, get_filtered_voltage

matplotlib.use('TkAgg')


###################
# The QUA program #
###################
n_avg = 100  # Number of averages
n_points_detuning = 101

sweep_gates = ["P1_sticky", "P2_sticky"]
level_init = [-0.1, 0.1]
level_readout = [0.1, -0.1]
voltages_P1 = np.linspace(level_init[0], level_readout[0], n_points_P1)
voltages_P2 = np.linspace(level_init[1], level_readout[1], n_points_P2)
duration_empty = 5000

seq = OPX_virtual_gate_sequence(config, sweep_gates)
seq.add_points("initialization", level_init, duration_init)
for i, (v1, v2) in enumerate(zip(voltages_P1, voltages_P2)):
    seq.add_points(f"readout_{i}", level_readout, duration_readout)


with program() as PSB_search_prog:
    n = declare(int)  # QUA integer used as an index for the averaging loop
    n_st = declare_stream()  # Stream for the iteration number (progress bar)
    I = [declare(fixed) for _ in range(num_tank_circuits)]
    Q = [declare(fixed) for _ in range(num_tank_circuits)]
    I_st = [declare_stream() for _ in range(num_tank_circuits)]
    Q_st = [declare_stream() for _ in range(num_tank_circuits)]

    # Ensure that the result variables are assign to the pulse processor used for readout
    assign_variables_to_element("tank_circuit", I, Q)
    assign_variables_to_element("TIA", dc_signal)

    with for_(n, 0, n < n_avg, n + 1):

        for m in range(n_points_detuning):
            align()

            # Play the triangle
            seq.add_step(voltage_point_name="initialization")
            seq.add_step(voltage_point_name=f"readout_{m}")
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
                save(I[j], I_st[j])
                save(Q[j], Q_st[j])
                # Wait at each iteration in order to ensure that the data will not be transferred faster than 1 sample
                # per µs to the stream processing. Otherwise, the processor will receive the samples faster than it can
            # process them which can cause the OPX to crash.
            wait(1_000 * u.ns)  # in ns
            # Ramp the voltage down to zero at the end of the triangle (needed with sticky elements)
            ramp_to_zero("P1_sticky")
            ramp_to_zero("P2_sticky")
        # Save the LO iteration to get the progress bar
        save(i, n_st)

    # Stream processing section used to process the data before saving it
    with stream_processing():
        n_st.save("iteration")
        for j, tc in enumerate(tank_circuits):
            I_st[j].buffer(n_voltages_Px).buffer(n_voltages_Py).average().save(f"I_{tc}")
            Q_st[j].buffer(n_voltages_Px).buffer(n_voltages_Py).average().save(f"Q_{tc}")


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
    simulation_config = SimulationConfig(duration=100_000)  # In clock cycles = 4ns
    job = qmm.simulate(config, PSB_search_prog, simulation_config)
    plt.figure()
    job.get_simulated_samples().con1.plot()

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
    results = fetching_tool(job, data_list=fetch_names, mode="live")
    # Live plotting
    fig = plt.figure()
    interrupt_on_close(fig, job)  # Interrupts the job when closing the figure
    while results.is_processing():
        # Fetch results
        res = results.fetch_all()
        # Progress bar
        progress_counter(res[0], n_avg, start_time=results.get_start_time())

        plt.suptitle("Charge sensor gate sweep")
        for ind, tc in enumerate(tank_circuits):
            S = res[2 * ind + 1] + 1j * res[2 * ind + 2]
            R = np.abs(S)  # np.unwarp(np.angle(S))
            phase = signal.detrend(np.unwrap(np.angle(S)))

            # Plot results
            plt.suptitle("Charge stability diagram")
            plt.subplot(2, 2, ind + 1)
            plt.cla()
            plt.title(r"$\sqrt{I^2 + Q^2}$ [V]" + f" {tc}")
            plt.pcolor(voltages_Px, voltages_Py, R)
            # plt.xlabel(f"{Px} voltage [V]")
            plt.ylabel(f"{Py} voltage [V]")
            plt.subplot(2, 2, ind + 3)
            plt.cla()
            plt.title("Phase [rad]")
            plt.pcolor(voltages_Px, voltages_Py, phase)
            plt.xlabel(f"{Px} voltage [V]")
            plt.ylabel(f"{Py} voltage [V]")

        plt.tight_layout()
        plt.pause(1)

    # Fetch results
    res = results.fetch_all()
    for ind, tc in enumerate(tank_circuits):
        save_data_dict[f"I_{tc}"] = res[2 * ind + 1]
        save_data_dict[f"Q_{tc}"] = res[2 * ind + 2]

    # Save results
    script_name = Path(__file__).name
    data_handler = DataHandler(root_data_folder=save_dir)
    save_data_dict.update({"fig_live": fig})
    data_handler.additional_files = {
        script_name: script_name,
        **default_additional_files,
    }
    data_handler.save_data(data=save_data_dict, name="06_charge_stability_map_opx")

    qm.close()
    plt.close()

# %%
