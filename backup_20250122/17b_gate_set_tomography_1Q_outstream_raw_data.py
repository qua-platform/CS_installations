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
from qualang_tools.plot import interrupt_on_close
from qualang_tools.results import (fetching_tool, progress_counter,
                                   wait_until_job_is_paused)

from configuration_with_lffem_csrack import *
# from configuration_with_lffem import *
from macros_initialization_and_readout_2q import *
from macros_voltage_gate_sequence import VoltageGateSequence

# # matplotlib.use('TkAgg')

###################
#  Util funciton  #
###################

def get_dataframe_encoded_sequence():
    path = "./encoded_parsed_dataset.csv"
    df = pd.read_csv(path, header=0)  # Use header=0 to indicate the first row is the header
    df["full_gate_sequence_duration"] = pi_half_len * df["full_native_gate_count"]
    df.reset_index(inplace=True)
    # df = df.head(50)
    # df = df.head(10)
    return df


def get_encoded_circuit(row):
    C = int(row["circ_idx"])
    P = int(row["P_enc"])
    G = int(row["G_enc"])
    d = int(row["d_enc"])
    M = int(row["M_enc"])
    D = int(row["full_gate_sequence_duration"])
    Ph4 = int(row["remaining_wait_num_4-pihalf"])
    Ph = int(row["remaining_wait_num_pihalf"])

    seq_len = 0
    _encoded_circuit = [C]
    if P != -1:
        _encoded_circuit.append(P)
        seq_len += 1
    if G != -1:
        _encoded_circuit.extend([G] * d)
        seq_len += d
    if M != -1:
        _encoded_circuit.append(M)
        seq_len += 1
    if Ph4 > 0:
        _encoded_circuit.extend([0] * Ph4)
        seq_len += Ph4
    if Ph > 0:
        _encoded_circuit.append(Ph)
        seq_len += 1

    # sequence length
    _encoded_circuit.insert(1, seq_len)

    return _encoded_circuit, seq_len, C, P, G, d, M, Ph4, Ph


###################
# The QUA program #
###################

qubit = "qubit1"
sweep_gates = ["P0_sticky", "P1_sticky"]
tank_circuit = "tank_circuit1"
threshold = TANK_CIRCUIT_CONSTANTS[tank_circuit]["threshold"]
num_output_streams = 2
seed = 345324  # Pseudo-random number generator seed
do_simulate = False

pi_half_len = QUBIT_CONSTANTS[qubit]["square_pi_half_len"]
pi_half_amp = QUBIT_CONSTANTS[qubit]["square_pi_half_amp"]


list_n_shots = [10, 100]
df_enc_seqs = get_dataframe_encoded_sequence()
sequence_max_len = 2 + df_enc_seqs["full_sequence_length"].max()  # 2 for circ_idx and circ_len
num_cicuits = len(df_enc_seqs)
batch_size = max(list_n_shots)
result_array_len = num_cicuits * sum(list_n_shots)
result_array_len = batch_size * math.ceil(result_array_len / batch_size)
num_batches = math.ceil(result_array_len / batch_size)


# duration_init includes the manipulation
max_gate_counts = 4 + int(df_enc_seqs["full_native_gate_count"].max())
max_gate_duration = max_gate_counts * pi_half_len
delay_ops_start = RF_SWITCH_DELAY
delay_ops_end = RF_SWITCH_DELAY
duration_ops = delay_init_qubit_start + max_gate_duration + delay_init_qubit_end


save_data_dict = {
    "sweep_gates": sweep_gates,
    "qubit": qubit,
    "config": config,
}


###################
# The QUA program #
###################


def perform_read_init(I, Q, P0_st, P1_st):
    P0 = measure_parity(I, Q, None, None, None, P0_st, tank_circuit=tank_circuit, threshold=threshold)

    # # conditional pi pulse
    # align()
    # with if_(P0):
    #     seq.add_step(voltage_point_name="initialization_1q", duration=(RF_SWITCH_DELAY + pi_len + RF_SWITCH_DELAY), ramp_duration=duration_ramp_init) # NEVER u.ns
    #     wait(duration_ramp_init // 4, "rf_switch", qubit)
    #     play("trigger", "rf_switch", duration=(RF_SWITCH_DELAY + pi_len + RF_SWITCH_DELAY) // 4)
    #     wait(RF_SWITCH_DELAY // 4, qubit)
    #     play("x180_square", qubit)
    
    align()
    P1 = measure_parity(I, Q, None, None, None, P1_st, tank_circuit=tank_circuit, threshold=threshold)
    
    return P0, P1



with program() as PROGRAM_GST:
    n = declare(int)
    n_shots = declare(int)
    circ = declare(int)
    case_idx = declare(int)
    count = declare(int, value=0)
    division = declare(int, value=1)

    n_st = declare_stream()  # Stream for the iteration number (progress bar)
    n_shots_st = declare_stream()
    circ_idx_st = declare_stream()
    circ_len_st = declare_stream()

    I = declare(fixed)
    Q = declare(fixed)
    P_st = [declare_stream() for _ in range(num_output_streams)]
    # Ensure that the result variables are assign to the pulse processor used for readout
    assign_variables_to_element(tank_circuit, I, Q)

    # The relevant streams
    # i_depth = declare(int, value=0)
    m_st = declare_stream()
    P_diff_st = declare_stream()

    current_level = declare(fixed, value=[0.0 for _ in sweep_gates])
    seq.current_level = current_level

    if set_init_as_dc_offset:
        for sg, lvl_init in zip(sweep_gates, level_init_list):
            set_dc_offset(sg, "single", lvl_init)


    if do_simulate:
        encoded_circuit = declare(int, value=[112, 8195, 9, 4, 4, 4, 4, 5] + [0] * 8188 + [1])
    else:
        encoded_circuit = declare_input_stream(
            int,
            name="_encoded_circuit",
            size=sequence_max_len + 3,  # 2 to account for [circ_idx, seq_len, remaining_duraiton_case]
        )  # input stream the sequence


    with for_each_(n_shots, list_n_shots):
        with for_(circ, 0, circ < num_cicuits, circ + 1):
            if not do_simulate:
                advance_input_stream(encoded_circuit)  # ordered or randomized

            circ_idx = encoded_circuit[0]  # just a sequential index for this circuit
            circ_len = encoded_circuit[1]  # gate sequence length for this circuit

            with for_(n, 0, n < n_shots, n + 1):
                assign(count, count + 1)

                # Perform initialization
                _, P0 = perform_read_init(I, Q, None, P_st[0])

                # Navigate through the charge stability map
                align()
                seq.add_step(voltage_point_name="initialization_1q", duration=duration_ops, ramp_duration=duration_ramp_init) # NEVER u.ns

                wait(duration_ramp_init // 4, "rf_switch", qubit)
                play("trigger", "rf_switch", duration=duration_ops // 4)
                wait(RF_SWITCH_DELAY // 4, qubit)

                with strict_timing_():
                    with for_(case_idx, 2, case_idx < circ_len + 2, case_idx + 1):
                        with switch_(encoded_circuit[case_idx], unsafe=True):
                            # baseband operation is fixed regardless L
                            # normal:just run till the end with Null
                            # option: adjust the length accoridngly

                            with case_(0):
                                wait(4 * pi_half_len * u.ns, qubit)
                            with case_(1):
                                wait(pi_half_len * u.ns, qubit)
                            with case_(2):
                                wait(2 * pi_half_len * u.ns, qubit)
                            with case_(3):
                                wait(3 * pi_half_len * u.ns, qubit)

                            # '{}': 4, # I
                            # 'Gxpi2:0': 5,
                            # 'Gypi2:0': 6,
                            # 'Gxpi2:0Gxpi2:0': 7,
                            # 'Gxpi2:0Gxpi2:0Gxpi2:0': 9,
                            # 'Gypi2:0Gypi2:0Gypi2:0': 10,
                            # 'Gxpi2:0Gypi2:0': 8,
                            # 'Gxpi2:0Gxpi2:0Gypi2:0': 11

                            # prep & meas fiducials and germs
                            with case_(4):  #   I = XXXX
                                play("x90_square", qubit)
                                play("x90_square", qubit)
                                play("x90_square", qubit)
                                play("x90_square", qubit)
                            with case_(5):
                                play("x90_square", qubit)
                            with case_(6):
                                play("y90_square", qubit)
                            with case_(7):
                                play("x90_square", qubit)
                                play("x90_square", qubit)
                            with case_(8):
                                play("x90_square", qubit)
                                play("y90_square", qubit)
                            with case_(9):
                                play("x90_square", qubit)
                                play("x90_square", qubit)
                                play("x90_square", qubit)
                            with case_(10):
                                play("y90_square", qubit)
                                play("y90_square", qubit)
                                play("y90_square", qubit)
                            with case_(11):
                                play("x90_square", qubit)
                                play("x90_square", qubit)
                                play("y90_square", qubit)

                # Perform readout
                align()
                P1, _ = perform_read_init(I, Q, P_st[1], None)

                # DO NOT REMOVE: bring the voltage back to dc_offset level.
                # Without this, it can accumulate a precision error that leads to unwanted large voltage (max of the range).
                align()
                seq.ramp_to_zero()
                    
                # Save the LO iteration to get the progress bar
                wait(25_000)

                save(n, n_st)
                save(n_shots, n_shots_st)
                save(circ_idx, circ_idx_st)


            with if_(count == division * batch_size):
                assign(division, division + 1)
                # pause to outstream the data
                pause()

    with stream_processing():
        n_st.buffer(batch_size).save("n_history")
        n_shots_st.buffer(batch_size).save("n_shots_history")
        circ_idx_st.buffer(batch_size).save("circ_idx_history")
        for k in range(num_output_streams):
            P_st[k].boolean_to_int().buffer(batch_size).save(f"P{k:d}")


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
    job = qmm.simulate(config, PROGRAM_GST, simulation_config)
    # Plot the simulated samples
    job.get_simulated_samples().con1.plot()
    plt.show()

else:
    from qm import generate_qua_script

    sourceFile = open(f"debug_{Path(__file__).stem}.py", "w")
    print(generate_qua_script(PROGRAM_GST, config), file=sourceFile)
    sourceFile.close()

    # Open the quantum machine
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(PROGRAM_GST, compiler_options=CompilerOptionArguments(flags=["not-strict-timing"]))

    fetch_names = ["n_history", "n_shots_history", "circ_idx_history"]
    fetch_names.extend([f"P{k:d}" for k in range(num_output_streams)])

    if save_data:
        from qualang_tools.results.data_handler import DataHandler

        script_name = Path(__file__).name
        data_handler = DataHandler(root_data_folder=save_dir)
        data_handler.create_data_folder(name=Path(__file__).stem)

    batch_idx = 1
    ress = []
    start_time = datetime.now()
    for _n_shots in list_n_shots:
        this_df = df_enc_seqs.sample(frac=1, random_state=_n_shots)

        for i_row, (_, row) in enumerate(this_df.iterrows()):
            _encoded_circuit, seq_len, C, P, G, d, M, Ph4, Ph = get_encoded_circuit(row)

            current_datetime = datetime.now()
            current_datetime_str = current_datetime.strftime("%Y/%m/%d-%H:%M:%S")
            elapsed_time = current_datetime - start_time
            elapsed_time_secs = int(elapsed_time.total_seconds())
            _log_this = f"{current_datetime_str}, batch_idx: {batch_idx} / {num_batches}, no: {i_row + 1}, n_shots: {_n_shots}, seq_len: {seq_len}, circ_idx = {C}, n_circuits: P={P}, G={G}, d={d}, M={M}, Ph4={Ph4}, Ph={Ph}, elapsed_secs: {elapsed_time_secs}"
            print(_log_this)
            with open(data_handler.path / "log.txt", encoding="utf8", mode="a") as f:
                f.write(_log_this.replace("_", "") + "\n")  # Append the log message to the file

            job.push_to_input_stream("_encoded_circuit", _encoded_circuit)

            if job.is_paused():
                # Wait until the program reaches the 'pause' statement again, indicating that the QUA program is done
                if batch_idx == 1:
                    print("get a fetching tool")
                    results = fetching_tool(job, data_list=fetch_names, mode="live")

                # Fetch results
                print("fetch result!")
                res = results.fetch_all()
                ress.append(res)
                data_dict = {name: arr for name, arr in zip(fetch_names, res)}

                # Data to save
                print("save result!")
                np.savez(file=data_handler.path / f"data_{batch_idx:08d}.npz", **data_dict)
                batch_idx += 1
                job.resume()

    # Save results
    script_name = Path(__file__).name
    data_handler = DataHandler(root_data_folder=save_dir)
    data_handler.additional_files = {
        script_name: script_name,
        "macros_initialization_and_readout.py": "macros_initialization_and_readout.py" ** default_additional_files,
    }
    data_handler.save_data(data=save_data_dict, name=script_name.replace(".py",""))

    qm.close()

# %%
