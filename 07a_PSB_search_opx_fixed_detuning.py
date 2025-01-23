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

from configuration_with_lffem_csrack import *
# from configuration_with_lffem import *
from macros_voltage_gate_sequence import VoltageGateSequence

# matplotlib.use('TkAgg')


###################
# The QUA program #
###################

run_live = False  # True
set_init_as_dc_offset = True
amplitude_scaling = 4.7  # (DC port / AC port) of bias tee

level_init_arr = np.array([-0.02, 0.02]) * amplitude_scaling
level_readout_arr = np.array([-0.00, 0.00]) * amplitude_scaling


n_shots = 100000 if run_live else 1000
n_shots_buffer = 1000  # Number of averages
sweep_gates = ["P4_sticky", "P3_sticky"]
tank_circuit = "tank_circuit2"
threshold = TANK_CIRCUIT_CONSTANTS[tank_circuit]["threshold"]

duration_init = 10_000  # DO NOT USE * u.ns
duration_ramp_init = 200  # DO NOT USE * u.ns
duration_readout = 1_000 + REFLECTOMETRY_READOUT_LEN  # DO NOT USE * u.ns
duration_ramp_readout = 52  # DO NOT USE * u.ns


if set_init_as_dc_offset:
    level_readout_offset_arr = level_readout_arr - level_init_arr
    level_init_offset_arr = np.array([0.0, 0.0])  # level_init_arr - level_init_arr

level_readout_list = level_readout_arr.tolist()
level_init_list = level_init_arr.tolist()
level_readout_offset_list = level_readout_offset_arr.tolist()
level_init_offset_list = level_init_offset_arr.tolist()


print(f"level init: {level_init_list}")
print(f"level readout: {level_readout_list}")
print(f"level init after offset: {level_init_offset_list}")
print(f"level readout after offset: {level_readout_offset_list}")


seq = VoltageGateSequence(config, sweep_gates)
seq.add_points("initialization", level_init_offset_list, duration_init)
seq.add_points("readout", level_readout_offset_list, duration_readout)


save_data_dict = {
    "sweep_gates": sweep_gates,
    "tank_circuit": tank_circuit,
    "n_shots": n_shots,
    "config": config,
}


with program() as PSB_search_prog:
    n = declare(int)  # QUA integer used as an index for the averaging loop
    n_st = declare_stream()  # Stream for the iteration number (progress bar)
    I = declare(fixed)
    Q = declare(fixed)
    P = declare(bool)
    I_st = declare_stream()
    Q_st = declare_stream()
    P_st = declare_stream()

    current_level = declare(fixed, value=[0.0 for _ in sweep_gates])
    seq.current_level = current_level

    # Ensure that the result variables are assign to the pulse processor used for readout
    assign_variables_to_element("tank_circuit1", I, Q, P)

    if set_init_as_dc_offset:
        for sg, lvl_init in zip(sweep_gates, level_init_list):
            set_dc_offset(sg, "single", lvl_init)

    with for_(n, 0, n < n_shots, n + 1):
        # Play the triangle
        seq.add_step(voltage_point_name="initialization", ramp_duration=duration_ramp_init)
        seq.add_step(voltage_point_name="readout", ramp_duration=duration_ramp_readout)
        align()

        # Measure the dot right after the qubit manipulation
        measure(
            "readout",
            tank_circuit,
            None,
            demod.full("cos", I, "out1"),
            demod.full("sin", Q, "out1"),
        )
        assign(P, I > threshold)
        save(I, I_st)
        save(Q, Q_st)
        save(P, P_st)

        # DO NOT REMOVE: bring the voltage back to dc_offset level.
        # Without this, it can accumulate a precision error that leads to unwanted large voltage (max of the range).
        align()
        seq.ramp_to_zero()

        # Save the LO iteration to get the progress bar
        save(n, n_st)
        wait(250)

    # Stream processing section used to process the data before saving it
    with stream_processing():
        n_st.save("iteration")
        if run_live:
            I_st.buffer(n_shots_buffer).save(f"I_{tank_circuit}")
            Q_st.buffer(n_shots_buffer).save(f"Q_{tank_circuit}")
            P_st.boolean_to_int().buffer(n_shots_buffer).save(f"P_{tank_circuit}")
        else:
            I_st.buffer(n_shots).save(f"I_{tank_circuit}")
            Q_st.buffer(n_shots).save(f"Q_{tank_circuit}")
            P_st.boolean_to_int().buffer(n_shots).save(f"P_{tank_circuit}")


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
    fetch_names = ["iteration", f"I_{tank_circuit}", f"Q_{tank_circuit}", f"P_{tank_circuit}"]
    results = fetching_tool(job, data_list=fetch_names, mode="live")

    fig = plt.figure()
    # bins = np.arange(0.05, 0.30, 0.001)
    interrupt_on_close(fig, job)  # Interrupts the job when closing the figure
    while results.is_processing():
        # Fetch results
        iteration, I, Q, P = results.fetch_all()

        # Progress bar
        progress_counter(iteration, n_shots, start_time=results.get_start_time())

        # Plot I
        plt.suptitle("PSB Search")
        plt.clf()
        plt.hist(I, bins=201, color="skyblue", edgecolor="black")
        plt.tight_layout()
        plt.pause(0.2)

    # Fetch results
    iteration, I, Q, P = results.fetch_all()
    save_data_dict["I"] = I
    save_data_dict["Q"] = Q
    save_data_dict["P"] = P

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
