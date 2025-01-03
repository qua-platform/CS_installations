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

qubit = "qubit5"
qubit_trio1 = f"{qubit}_trio1"
plungers = "P4-P5"
do_feedback = False # False for test. True for actual.
full_read_init = False
num_output_streams = 6 if full_read_init else 2
do_simulate = False
target_qubits = [qubit, qubit_trio1]
num_target_qubits = len(target_qubits)

try:
    all_elements.remove("qubit1")
    all_elements.remove("qubit2")
    all_elements.remove("qubit3")
    # all_elements.remove("tank_circuit1")
    all_elements.append(qubit_trio1)
except:
    pass

n_avg = 5
num_of_sequences = 3  # Number of random sequences
circuit_depth_min = 10000
circuit_depth_max = 16000 # works up to 16_000
delta_clifford = 1000
circuit_depths = np.arange(circuit_depth_min, circuit_depth_max + 1, delta_clifford).astype(int)
actual_circuit_depths = num_target_qubits * circuit_depths

num_gates_total_max = int(1000 * math.ceil(circuit_depth_max * (46 / 24) // 1000))
# circuit_depths = [int(_) for _ in circuit_depths]
duration_compensation_pulse = circuit_depth_max * PI_LEN
assert circuit_depth_max % delta_clifford == 0, "circuit_depth_max / delta_clifford must be an integer."


# duration_init includes the manipulation
delay_rb_start_loop = 16
# duration_rb = PI_LEN * circuit_depth_max * 2 # 2 is a bit bigger than 1.875 (or)
duration_rb = PI_LEN * 10 * 2
delay_rb_end_loop = 0
# duration_ops = delay_rb_start + duration_rb + delay_rb_end


duration_compensation_pulse_rb = 800_000 # duration_rb
duration_compensation_pulse_full = int(0.7 * duration_compensation_pulse_initialization + duration_compensation_pulse_rb + duration_compensation_pulse_readout)
duration_compensation_pulse_full = 100 * (duration_compensation_pulse_full // 100)


seq.add_points("operation_P1-P2", level_ops["P1-P2"], delay_rb_start_loop + delay_rb_end_loop)
seq.add_points("operation_P4-P5", level_ops["P4-P5"], delay_rb_start_loop + delay_rb_end_loop)
seq.add_points("operation_P3", level_ops["P3"], delay_rb_start_loop + delay_rb_end_loop)


save_data_dict = {
    "sweep_gates": sweep_gates,
    "qubit": qubit,
    "config": config,
}


def generate_encoded_sequence(N, current_state=0, ends_with_inv_gate=True, num_gates_total_max=num_gates_total_max, seed=0):

    np.random.seed(seed)
    clifford_arr = np.random.randint(low=0, high=23, size=N).astype(int)
    state_arr = np.zeros(N).astype(int)
    inv_gate_arr = np.zeros(N).astype(int)

    for i, step in enumerate(clifford_arr):
        next_state = c1_table[current_state, step]
        state_arr[i] = next_state
        current_state = next_state
        inv_gate_arr[i] = inv_gates[current_state]
    
    if ends_with_inv_gate:
        inv_gate = inv_gate_arr[-2]
        clifford_arr[-1] = inv_gate
        state_arr[-1] = c1_table[state_arr[-2], inv_gate]
    
    clifford_list = clifford_arr.tolist()
    state_list = state_arr.tolist()
    inv_gate_list = inv_gate_arr.tolist()

    num_gates_total = int(np.array([map_clifford_to_num_gates[s] for s in clifford_list]).sum())
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
    # Q_st = [declare_stream() for _ in range(num_output_streams)]
    # P_st = [declare_stream() for _ in range(num_output_streams)]
    # Ensure that the result variables are assign to the pulse processor used for readout
    assign_variables_to_element("tank_circuit1", I[0], Q[0], P[0])
    assign_variables_to_element("tank_circuit2", I[1], Q[1], P[1])

    if do_simulate:
        encoded_circuit = declare(int, value=[112, 8195, 9, 4, 4, 4, 4, 5] + [0] * 8188 + [1])
    else:
        encoded_circuit = declare_input_stream(
            int,
            name="_encoded_circuit",
            size=circuit_depth_max + 1, # 2 to account for [circ_idx, seq_len, remaining_duraiton_case]
        )  # input stream the sequence


    with for_(*from_array(depth, circuit_depths)):  # Loop over the depths

        with for_(m, 0, m < num_of_sequences, m + 1):
            
            if not do_simulate:
                advance_input_stream(encoded_circuit)  # ordered or randomized

            duration_rb = encoded_circuit[0] # just a sequential index for this circuit
            assign(duration_ops, delay_rb_start_loop + duration_rb + delay_rb_end_loop)

            with for_(n, 0, n < n_avg, n + 1):

                with strict_timing_():

                    if full_read_init:
                        # RI12 -> 2 x (R3 -> R12) -> RI45
                        perform_initialization(I, Q, P, I_st[0], I_st[1], I_st[2])
                    else:                    # RI12 -> 2 x (R3 -> R12) -> RI45
                        # RI12
                        read_init45(I[0], Q[0], P[0], None, I_st[0], do_save=[False, True])

                    # Navigate through the charge stability map
                    seq.add_step(voltage_point_name=f"operation_{plungers}", duration=duration_ops * u.ns)
                    other_elements = get_other_elements(elements_in_use=[qubit] + sweep_gates, all_elements=all_elements)
                    wait(duration_ops >> 2, *other_elements)

                    wait(delay_rb_start_loop * u.ns, qubit) if delay_rb_start_loop >= 16 else None
                    play_sequence(encoded_circuit, depth, qubit)
                    # wait(duration_rb12 >> 2, qubit)
                    wait(delay_rb_end_loop * u.ns, qubit) if delay_rb_end_loop >= 16 else None

                    if full_read_init:
                        # RI12 -> R3 -> RI45
                        perform_readout(I, Q, P, I_st[3], I_st[4], I_st[5])
                    else:
                        # RI12
                        read_init45(I[0], Q[0], P[0], I_st[1], None, do_save=[True, False])

                    seq.add_compensation_pulse(duration=duration_compensation_pulse_full)
                
                # save(depth, depth)
                # save(m, m_st)
                # save(n, n_st)
                seq.ramp_to_zero()
                wait(1000 * u.ns)

    with stream_processing():
        # depth_st.buffer(num_of_sequences).buffer(len(circuit_depths)).save("actual_circuit_depths")
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
    job = qmm.simulate(config, PROGRAM_RB, simulation_config)
    # Plot the simulated samples
    job.get_simulated_samples().con1.plot()
    plt.show()

else:
    from qm import generate_qua_script
    sourceFile = open("debug_19b_single_qubit_RB_read_init.py", "w")
    print(generate_qua_script(PROGRAM_RB, config), file=sourceFile)
    sourceFile.close()

    # Open the quantum machine
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(PROGRAM_RB, compiler_options=CompilerOptionArguments(flags=["not-strict-timing"]))

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
            _log_this = f"{current_datetime_str}, circuit_depth: {_circuit_depth}, num_sequence: {num_seq} / {num_of_sequences}, num_gates_total: {num_gates_total}, seed: {_seed}, elapsed_secs: {elapsed_time_secs}"
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
    np.savez(file = data_handler.path / f"data_circuit_depth_{_circuit_depth:08d}.npz", **data_dict)


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
        data_handler.save_data(data=save_data_dict, name=Path(__name__).stem)

    qm.close()


# %%
