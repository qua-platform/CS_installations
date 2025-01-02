# %%

import math
from datetime import datetime
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
from qm import *
from qm import QuantumMachinesManager, SimulationConfig
from qm.qua import *
from qualang_tools.loops import from_array
from qualang_tools.addons.variables import assign_variables_to_element
from qualang_tools.bakery.randomized_benchmark_c1 import c1_table
from qualang_tools.plot import interrupt_on_close
from qualang_tools.results import fetching_tool, progress_counter, wait_until_job_is_paused
from qualang_tools.voltage_gates import VoltageGateSequence
from macros import get_other_elements

from macros_initialization_and_readout import *
from configuration_with_lffem import *

# matplotlib.use('TkAgg')


###################
# The QUA program #
###################

qubit = "qubit1"
qubit_trio1 = f"{qubit}_trio1"
plungers = "P1-P2"
do_feedback = False # False for test. True for actual.
full_read_init = False
num_output_streams = 6 if full_read_init else 2
do_simulate = False


n_avg = 5
num_of_sequences = 3  # Number of random sequences
circuit_depth_min = 10
circuit_depth_max = 120
delta_clifford = 10
circuit_depths = np.arange(circuit_depth_min, circuit_depth_max + 1, delta_clifford).astype(int)
num_gates_total_max = int(1000 * math.ceil(circuit_depth_max * (46 / 24) // 1000))
# circuit_depths = [int(_) for _ in circuit_depths]
duration_compensation_pulse = circuit_depth_max * PI_LEN
assert circuit_depth_max % delta_clifford == 0, "circuit_depth_max / delta_clifford must be an integer."


# duration_init includes the manipulation
delay_rb_start = 92
# duration_rb = PI_LEN * circuit_depth_max * 2 # 2 is a bit bigger than 1.875 (or)
duration_rb = PI_LEN * 10 * 2
delay_rb_end = 16
# duration_ops = delay_rb_start + duration_rb + delay_rb_end


duration_compensation_pulse_rb = 800_000 # duration_rb
duration_compensation_pulse_full = int(0.7 * duration_compensation_pulse_initialization + duration_compensation_pulse_rb + duration_compensation_pulse_readout)
duration_compensation_pulse_full = 100 * (duration_compensation_pulse_full // 100)


seq.add_points("operation_P1-P2", level_ops["P1-P2"], duration_rb)
seq.add_points("operation_P4-P5", level_ops["P4-P5"], duration_rb)
seq.add_points("operation_P3", level_ops["P3"], duration_rb)


save_data_dict = {
    "sweep_gates": sweep_gates,
    "qubit": qubit,
    "config": config,
}


def generate_encoded_sequence(N, current_state=0, ends_with_inv_gate=True, num_gates_total_max=num_gates_total_max, seed=0):

    np.random.seed(seed)
    clifford_arr = np.random.randint(low=0, high=23, size=N + 1).astype(int)
    state_arr = np.zeros(N + 1).astype(int)
    inv_gate_arr = np.zeros(N + 1).astype(int)

    for i, step in enumerate(clifford_arr):
        next_state = c1_table[current_state, step]
        state_arr[i] = next_state
        current_state = next_state
        inv_gate_arr[i] = inv_gates[current_state]
    
    if ends_with_inv_gate:
        inv_gate = inv_gate_arr[N - 1]
        clifford_arr[N] = inv_gate
        state_arr[N] = c1_table[state_arr[N - 1], inv_gate]
    
    if ends_with_inv_gate:
        clifford_list = clifford_arr.tolist()
        state_list = state_arr.tolist()
        inv_gate_list = inv_gate_arr.tolist()
    else:
        clifford_list = clifford_arr.tolist()[:-1]
        state_list = state_arr.tolist()[:-1]
        inv_gate_list = inv_gate_arr.tolist()[:-1]
    
    num_gates_total = int(np.array([map_clifford_to_num_gates[s] for s in state_list]).sum())
    num_gates_total_rest = num_gates_total_max - num_gates_total 
    duration_rb_total = num_gates_total * PI_LEN
    _encoded_circuit = [duration_rb_total] + clifford_list

    return _encoded_circuit, clifford_list, state_list, inv_gate_list, num_gates_total


def play_sequence(sequence_list, depth, qb):
    i = declare(int)
    with for_(i, 1, i <= depth + 1, i + 1):
        with switch_(sequence_list[i], unsafe=True):
            with case_(0):
                wait(PI_LEN // 4, qb) # I
            with case_(1):
                play("x180_square", qb)
            with case_(2):
                play("y180_square", qb)
            with case_(3):
                play("y180_square", qb)
                play("x180_square", qb)
            with case_(4):
                play("x90_square", qb)
                play("y90_square", qb)
            with case_(5):
                play("x90_square", qb)
                play("-y90_square", qb)
            with case_(6):
                play("-x90_square", qb)
                play("y90_square", qb)
            with case_(7):
                play("-x90_square", qb)
                play("-y90_square", qb)
            with case_(8):
                play("y90_square", qb)
                play("x90_square", qb)
            with case_(9):
                play("y90_square", qb)
                play("-x90_square", qb)
            with case_(10):
                play("-y90_square", qb)
                play("x90_square", qb)
            with case_(11):
                play("-y90_square", qb)
                play("-x90_square", qb)
            with case_(12):
                play("x90_square", qb)
            with case_(13):
                play("-x90_square", qb)
            with case_(14):
                play("y90_square", qb)
            with case_(15):
                play("-y90_square", qb)
            with case_(16):
                play("-x90_square", qb)
                play("y90_square", qb)
                play("x90_square", qb)
            with case_(17):
                play("-x90_square", qb)
                play("-y90_square", qb)
                play("x90_square", qb)
            with case_(18):
                play("x180_square", qb)
                play("y90_square", qb)
            with case_(19):
                play("x180_square", qb)
                play("-y90_square", qb)
            with case_(20):
                play("y180_square", qb)
                play("x90_square", qb)
            with case_(21):
                play("y180_square", qb)
                play("-x90_square", qb)
            with case_(22):
                play("x90_square", qb)
                play("y90_square", qb)
                play("x90_square", qb)
            with case_(23):
                play("-x90_square", qb)
                play("y90_square", qb)
                play("-x90_square", qb)


inv_gates = [int(np.where(c1_table[i, :] == 0)[0][0]) for i in range(24)]
map_clifford_to_num_gates = {
    0: 1,
    1: 1,
    2: 1,
    3: 2,
    4: 2,
    5: 2,
    6: 2,
    7: 2,
    8: 2,
    9: 2,
    10: 2,
    11: 2,
    12: 1,
    13: 1,
    14: 1,
    15: 1,
    16: 3,
    17: 3,
    18: 2,
    19: 2,
    20: 2,
    21: 2,
    22: 3,
    23: 3,
}


with program() as PROGRAM_GST:
    m = declare(int)
    n = declare(int)
    depth1 = declare(int)
    depth2 = declare(int)
    duration_rb = declare(int)
    duration_ops = declare(int)
    seq_idx = declare(int)

    m_st = declare_stream()  # Stream for the iteration number (progress bar)
    n_st = declare_stream()  # Stream for the iteration number (progress bar)

    I = [declare(fixed) for _ in range(num_tank_circuits)]
    Q = [declare(fixed) for _ in range(num_tank_circuits)]
    P = [declare(bool) for _ in range(num_tank_circuits)]  # true if even parity
    I_st = [declare_stream() for _ in range(num_output_streams)]
    # Q_st = [declare_stream() for _ in range(num_output_streams)]
    # P_st = [declare_stream() for _ in range(num_output_streams)]
    # Ensure that the result variables are assign to the pulse processor used for readout
    assign_variables_to_element("tank_circuit1", I[0], Q[0], P[0])
    assign_variables_to_element("tank_circuit2", I[1], Q[1], P[1])

    if do_simulate:
        encoded_circuit = declare(int, value=[112, 8195, 9, 4, 4, 4, 4, 5] + [0] * 8188 + [1])
    else:
        encoded_circuit1 = declare_input_stream(
            int,
            name="_encoded_circuit1",
            size=circuit_depth_max + 1, # 2 to account for [circ_idx, seq_len, remaining_duraiton_case]
        )  # input stream the sequence
        encoded_circuit2 = declare_input_stream(
            int,
            name="_encoded_circuit2",
            size=circuit_depth_max + 1, # 2 to account for [circ_idx, seq_len, remaining_duraiton_case]
        )  # input stream the sequence


    with for_(*from_array(depth1, circuit_depths)):  # Loop over the depths
        assign(depth2, depth1)

        with for_(m, 0, m < num_of_sequences, m + 1):
            
            if not do_simulate:
                advance_input_stream(encoded_circuit1)  # ordered or randomized
                advance_input_stream(encoded_circuit2)  # ordered or randomized

            duration_rb1 = encoded_circuit1[0] # just a sequential index for this circuit
            duration_rb2 = encoded_circuit2[0] # just a sequential index for this circuit
            assign(duration_ops, delay_rb_start + duration_rb1 + duration_rb2 + delay_rb_end)

            with for_(n, 0, n < n_avg, n + 1):

                with strict_timing_():

                    if full_read_init:
                        # RI12 -> 2 x (R3 -> R12) -> RI45
                        perform_initialization(I, Q, P, I_st[0], I_st[1], I_st[2])
                    else:                    # RI12 -> 2 x (R3 -> R12) -> RI45
                        # RI12
                        read_init12(I[0], Q[0], P[0], None, I_st[0], do_save=[False, True])

                    # Navigate through the charge stability map
                    seq.add_step(voltage_point_name=f"operation_{plungers}", duration=duration_ops * u.ns)

                    other_elements = get_other_elements(elements_in_use=[qubit] + sweep_gates, all_elements=all_elements)
                    wait(duration_ops >> 2, *other_elements)

                    wait(delay_rb_start * u.ns, qubit) if delay_rb_start >= 16 else None
                    play_sequence(encoded_circuit1, depth1, qubit)
                    wait(duration_rb1 >> 2, qubit_trio1)
                    play_sequence(encoded_circuit2, depth2, qubit_trio1)
                    wait(delay_rb_end * u.ns, qubit) if delay_rb_end >= 16 else None

                    if full_read_init:
                        # RI12 -> R3 -> RI45
                        perform_readout(I, Q, P, I_st[3], I_st[4], I_st[5])
                    else:
                        # RI12
                        read_init12(I[0], Q[0], P[0], I_st[1], None, do_save=[True, False])

                    seq.add_compensation_pulse(duration=duration_compensation_pulse_full)
                
                # save(m, m_st)
                # save(n, n_st)
                seq.ramp_to_zero()
                wait(1000 * u.ns)

    with stream_processing():
        # m_st.buffer(n_avg).buffer(num_of_sequences).buffer(len(circuit_depths)).save("num_sequence")
        # n_st.buffer(n_avg).buffer(num_of_sequences).buffer(len(circuit_depths)).save("iterations")
        for k in range(num_output_streams):
            I_st[k].buffer(n_avg).buffer(num_of_sequences).buffer(len(circuit_depths)).save(f"I{k:d}")


#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(
    host=qop_ip, port=qop_port, cluster_name=cluster_name, octave=octave_config
)
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
    job = qmm.simulate(config, PROGRAM_GST, simulation_config)
    # Plot the simulated samples
    job.get_simulated_samples().con1.plot()
    plt.show()

else:
    from qm import generate_qua_script
    sourceFile = open("debug_19b_single_qubit_RB_read_init.py", "w")
    print(generate_qua_script(PROGRAM_GST, config), file=sourceFile)
    sourceFile.close()

    # Open the quantum machine
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(PROGRAM_GST, compiler_options=CompilerOptionArguments(flags=["not-strict-timing"]))

    # fetch_names = ["num_sequence", "iterations"]
    # fetch_names.extend([f"I{k:d}" for k in range(num_output_streams)])
    fetch_names = [f"I{k:d}" for k in range(num_output_streams)]

    if save_data:
        from qualang_tools.results.data_handler import DataHandler
        script_name = Path(__file__).name
        data_handler = DataHandler(root_data_folder=save_dir)
        data_handler.create_data_folder(name=Path(__file__).stem)


    ress = []
    start_time = datetime.now()
    for i_depth, _circuit_depth in enumerate(circuit_depths):

        for num_seq in range(num_of_sequences):
            _seed = i_depth * num_of_sequences + num_seq

            _encoded_circuit1, clifford_list1, state_list1, inv_gate_list1, num_gates_total1, = generate_encoded_sequence(_circuit_depth, ends_with_inv_gate=False, seed=_seed)
            _encoded_circuit2, clifford_list2, state_list2, inv_gate_list2, num_gates_total2, = generate_encoded_sequence(_circuit_depth, current_state=state_list1[-1], seed=_seed + 1234567890)

            current_datetime = datetime.now()
            current_datetime_str = current_datetime.strftime("%Y/%m/%d-%H:%M:%S")
            elapsed_time = current_datetime - start_time
            elapsed_time_secs = int(elapsed_time.total_seconds())
            _log_this = f"{current_datetime_str}, circuit_depth: {_circuit_depth}, num_sequence: {num_seq} / {num_of_sequences}, num_gates_total1: {num_gates_total2}, num_gates_total1: {num_gates_total2}, seed: {_seed}, elapsed_secs: {elapsed_time_secs}"
            print(_log_this)
            with open(data_handler.path / "log.txt", encoding="utf8", mode="a") as f:
                f.write(_log_this.replace("_", "") + "\n")  # Append the log message to the file

            job.push_to_input_stream("_encoded_circuit1", _encoded_circuit1)
            job.push_to_input_stream("_encoded_circuit2", _encoded_circuit2)


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
    np.savez(file = data_handler.path / f"data_circuit_depth_{_circuit_depth:08d}.npz", **data_dict)


    if save_data:
        # Save results
        script_name = Path(__file__).name
        data_dict = {name: arr for name, arr in zip(fetch_names, res)}
        data_handler = DataHandler(root_data_folder=save_dir)
        save_data_dict.update(**data_dict)
        data_handler.additional_files = {
            script_name: script_name,
            "macros_initialization_and_readout.py": "macros_initialization_and_readout.py"
            **default_additional_files,
        }
        data_handler.save_data(data=save_data_dict, name=Path(__name__).stem)

    qm.close()

# %%
