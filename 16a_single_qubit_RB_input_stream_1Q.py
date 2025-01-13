# %%

import math
from datetime import datetime

import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
from qm import *
from qm import QuantumMachinesManager, SimulationConfig
from qm.qua import *
from qualang_tools.addons.variables import assign_variables_to_element
from qualang_tools.bakery.randomized_benchmark_c1 import c1_table
from qualang_tools.loops import from_array
from qualang_tools.plot import interrupt_on_close
from qualang_tools.results import (fetching_tool, progress_counter,
                                   wait_until_job_is_paused)

from configuration_with_lffem import *
from macros import get_other_elements
from macros_initialization_and_readout import *
from macros_rb import *
from macros_voltage_gate_sequence import VoltageGateSequence

# # matplotlib.use('TkAgg')


###################
# The QUA program #
###################

qubit = "qubit5"
plungers = "P4-P5"  # "full", "P1-P2", "P4-P5"
do_feedback = False  # False for test. True for actual.
num_output_streams = 6 if plungers == "full" else 2
do_simulate = False
target_qubits = [qubit]
num_target_qubits = len(target_qubits)

all_elements = adjust_all_elements(removes=["qubit1", "qubit2", "qubit3"])

n_avg = 5
num_of_sequences = 3  # Number of random sequences
circuit_depth_min = 15000
circuit_depth_max = 16000  # works up to 16_000
delta_clifford = 1000
circuit_depths = np.arange(circuit_depth_min, circuit_depth_max + 1, delta_clifford).astype(int)
actual_circuit_depths = num_target_qubits * circuit_depths

num_gates_total_max = int(1000 * math.ceil(circuit_depth_max * (46 / 24) // 1000))
# circuit_depths = [int(_) for _ in circuit_depths]
duration_compensation_pulse_rb = circuit_depth_max * PI_LEN
assert circuit_depth_max % delta_clifford == 0, "circuit_depth_max / delta_clifford must be an integer."


# duration_init includes the manipulation
delay_ops_start = 16
# duration_rb = PI_LEN * circuit_depth_max * 2 # 2 is a bit bigger than 1.875 (or)
delay_ops_end = 0


duration_compensation_pulse = int(0.7 * duration_compensation_pulse_full_initialization + duration_compensation_pulse_rb + duration_compensation_pulse_full_readout)
duration_compensation_pulse = 100 * (duration_compensation_pulse // 100)


seq.add_points("operation_P1-P2", level_ops["P1-P2"], delay_ops_start + delay_ops_end)
seq.add_points("operation_P4-P5", level_ops["P4-P5"], delay_ops_start + delay_ops_end)
seq.add_points("operation_P3", level_ops["P3"], delay_ops_start + delay_ops_end)


save_data_dict = {
    "sweep_gates": sweep_gates,
    "qubit": qubit,
    "config": config,
}


with program() as PROGRAM_RB:
    m = declare(int)
    n = declare(int)
    depth = declare(int)
    duration_ops = declare(int)
    seq_idx = declare(int)

    m_st = declare_stream()  # Stream for the iteration number (progress bar)
    n_st = declare_stream()  # Stream for the iteration number (progress bar)
    depth_st = declare_stream()

    I = [declare(fixed) for _ in range(num_tank_circuits)]
    Q = [declare(fixed) for _ in range(num_tank_circuits)]
    P = [declare(bool) for _ in range(num_tank_circuits)]  # true if even parity
    I_st = [declare_stream() for _ in range(num_output_streams)]
    Q_st = [None for _ in range(num_output_streams)]  # [declare_stream() for _ in range(num_output_streams)]
    P_st = [None for _ in range(num_output_streams)]  # [declare_stream() for _ in range(num_output_streams)]
    # Ensure that the result variables are assign to the pulse processor used for readout
    assign_variables_to_element("tank_circuit1", I[0], Q[0], P[0])
    assign_variables_to_element("tank_circuit2", I[1], Q[1], P[1])

    if do_simulate:
        encoded_circuit = declare(int, value=[112, 8195, 9, 4, 4, 4, 4, 5] + [0] * 8188 + [1])
    else:
        encoded_circuit = declare_input_stream(
            int,
            name="_encoded_circuit",
            size=circuit_depth_max + 1,  # 2 to account for [circ_idx, seq_len, remaining_duraiton_case]
        )  # input stream the sequence

    with for_(*from_array(depth, circuit_depths)):  # Loop over the depths
        with for_(m, 0, m < num_of_sequences, m + 1):
            if not do_simulate:
                advance_input_stream(encoded_circuit)  # ordered or randomized

            duration_rb = encoded_circuit[0]  # just a sequential index for this circuit
            assign(duration_ops, delay_ops_start + duration_rb + delay_ops_end)

            with for_(n, 0, n < n_avg, n + 1):
                with strict_timing_():
                    # Perform specified initialization
                    perform_initialization(I, Q, P, I_st, Q_st, P_st, kind=plungers)

                    # Navigate through the charge stability map
                    seq.add_step(voltage_point_name=f"operation_{plungers}", duration=duration_ops * u.ns)
                    other_elements = get_other_elements(elements_in_use=[qubit] + sweep_gates, all_elements=all_elements)
                    wait(duration_ops >> 2, *other_elements)

                    wait(delay_ops_start * u.ns, qubit) if delay_ops_start >= 16 else None
                    play_sequence(encoded_circuit, depth, qubit, i_from=1)
                    wait(delay_ops_end * u.ns, qubit) if delay_ops_end >= 16 else None

                    # Perform specified readout
                    perform_readout(I, Q, P, I_st, Q_st, P_st, kind=plungers)

                    # Play compensatin pulse
                    seq.add_compensation_pulse(duration=duration_compensation_pulse)

                # save(depth, depth)
                # save(m, m_st)
                # save(n, n_st)
                seq.ramp_to_zero()
                wait(1000 * u.ns)

    with stream_processing():
        # depth_st.buffer(num_of_sequences).buffer(len(circuit_depths)).save("actual_circuit_depths")
        # m_st.buffer(n_avg).buffer(num_of_sequences).buffer(len(circuit_depths)).save("num_sequence")
        # n_st.buffer(n_avg).buffer(num_of_sequences).buffer(len(circuit_depths)).save("iteration")
        for k in range(num_output_streams):
            I_st[k].buffer(n_avg).buffer(num_of_sequences).buffer(len(circuit_depths)).save(f"I{k:d}")


#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(host=qop_ip, port=qop_port, cluster_name=cluster_name, octave=octave_config)
qmm.clear_all_job_results()
qmm.close_all_qms()


###########################
# Run or Simulate Program #
###########################
simulate = do_simulate
save_data = True

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=4_000)  # In clock cycles = 4ns
    # Simulate blocks python until the simulation is done
    job = qmm.simulate(config, PROGRAM_RB, simulation_config)
    # Plot the simulated samples
    job.get_simulated_samples().con1.plot()
    plt.show()

else:
    from qm import generate_qua_script

    sourceFile = open(f"debug_{Path(__file__).stem}.py", "w")
    print(generate_qua_script(PROGRAM_RB, config), file=sourceFile)
    sourceFile.close()

    # Open the quantum machine
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(PROGRAM_RB, compiler_options=CompilerOptionArguments(flags=["not-strict-timing"]))

    # fetch_names = ["num_sequence", "iteration"]
    # fetch_names.extend([f"I{k:d}" for k in range(num_output_streams)])
    fetch_names = [f"I{k:d}" for k in range(num_output_streams)]

    if save_data:
        from qualang_tools.results.data_handler import DataHandler

        script_name = Path(__file__).name
        data_handler = DataHandler(root_data_folder=save_dir)
        data_handler.create_data_folder(name=Path(__file__).stem)

    ress = []
    start_time = datetime.now()
    clifford_lists = []
    for i_depth, _circuit_depth in enumerate(circuit_depths):
        for num_seq in range(num_of_sequences):
            _seed = i_depth * num_of_sequences + num_seq

            _encoded_circuit, clifford_list, state_list, inv_gate_list, num_gates_total = generate_encoded_sequence(_circuit_depth, seed=_seed)

            clifford_lists.append(clifford_list)
            print(_encoded_circuit[:10])
            print(_encoded_circuit[-10:])

            current_datetime = datetime.now()
            current_datetime_str = current_datetime.strftime("%Y/%m/%d-%H:%M:%S")
            elapsed_time = current_datetime - start_time
            elapsed_time_secs = int(elapsed_time.total_seconds())
            _log_this = f"{current_datetime_str}, circuit_depth: {_circuit_depth}, num_sequence: {num_seq + 1} / {num_of_sequences}, num_gates_total: {num_gates_total}, seed: {_seed}, elapsed_secs: {elapsed_time_secs}"
            print(_log_this)
            with open(data_handler.path / "log.txt", encoding="utf8", mode="a") as f:
                f.write(_log_this.replace("_", "") + "\n")  # Append the log message to the file

            job.push_to_input_stream("_encoded_circuit", _encoded_circuit)

    # Wait until the program reaches the 'pause' statement again, indicating that the QUA program is done
    print("get a fetching tool")
    results = fetching_tool(job, data_list=fetch_names)

    # Fetch results
    print("fetch result!")
    res = results.fetch_all()
    ress.append(res)
    data_dict = {name: arr for name, arr in zip(fetch_names, res)}

    # Data to save
    print("save result!")
    np.savez(file=data_handler.path / f"data_circuit_depth_{_circuit_depth:08d}.npz", **data_dict)

    if save_data:
        # Save results
        script_name = Path(__file__).name
        data_dict = {name: arr for name, arr in zip(fetch_names, res)}
        data_handler = DataHandler(root_data_folder=save_dir)
        save_data_dict.update(**data_dict)
        data_handler.additional_files = {
            script_name: script_name,
            "macros_initialization_and_readout.py": "macros_initialization_and_readout.py",
            **default_additional_files,
        }
        data_handler.save_data(data=save_data_dict, name=script_name.replace(".py",""))

    qm.close()


# %%
