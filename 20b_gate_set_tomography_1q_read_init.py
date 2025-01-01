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
from qualang_tools.results import fetching_tool, progress_counter, wait_until_job_is_paused
from qualang_tools.voltage_gates import VoltageGateSequence
from macros import get_other_elements

from configuration_with_lffem import *

# matplotlib.use('TkAgg')

###################
#  Util funciton  #
###################


def get_dataframe_encoded_sequence():
    path = "./encoded_parsed_dataset.csv"
    df = pd.read_csv(path, header=0)  # Use header=0 to indicate the first row is the header
    df["full_gate_sequence_duration"] = PI_HALF_LEN * df["full_native_gate_count"]
    df.reset_index(inplace=True)
    df = df.head(50)
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

    return _encoded_circuit, C, P, G, d, M, Ph4, Ph


###################
# The QUA program #
###################

qubit = "qubit1"
plungers = "P1-P2"
do_feedback = False # False for test. True for actual.

qubits = ["qubit1", "qubit2", "qubit3", "qubit4", "qubit5"]
sweep_gates = ["P1_sticky", "P2_sticky", "P3_sticky", "P4_sticky", "P5_sticky"]
barrier_gates = ["B2"]
qp_controls = ["qp_control_c3t2"]
tank_circuits = ['tank_circuit1', 'tank_circuit2']
num_tank_circuits = len(TANK_CIRCUIT_CONSTANTS)
all_elements = qubits + sweep_gates + barrier_gates + qp_controls + tank_circuits


list_n_shots = [10, 100]
df_enc_seqs = get_dataframe_encoded_sequence()
sequence_max_len = 1 + 8192 + 1
num_cicuits = len(df_enc_seqs)
batch_size = max(list_n_shots)
result_array_len = num_cicuits * sum(list_n_shots)
result_array_len = batch_size * math.ceil(result_array_len / batch_size)
num_batches = math.ceil(result_array_len / batch_size)

delay_init_qubit_start = 16
delay_feedback = 240
delay_init_qubit_end = 16
duration_init_1q = delay_init_qubit_start + delay_feedback + PI_LEN + delay_init_qubit_end
duration_init_2q = delay_init_qubit_start + CROT_RF_LEN + delay_init_qubit_end
assert delay_init_qubit_start == 0 or delay_init_qubit_start >= 16
assert delay_init_qubit_end == 0 or delay_init_qubit_end >= 16


delay_read_reflec_start = 16
delay_read_reflec_end = 16
delay_stream = 1000
duration_readout = delay_read_reflec_start + REFLECTOMETRY_READOUT_LEN + delay_read_reflec_end + delay_stream
assert delay_read_reflec_start == 0 or delay_read_reflec_start >= 16
assert delay_read_reflec_end == 0 or delay_read_reflec_end >= 16


# duration_init includes the manipulation
max_gate_counts = 4 + int(df_enc_seqs["full_native_gate_count"].max())
max_gate_duration = max_gate_counts * PI_HALF_LEN
delay_gst_start = 16
delay_gst_end = 16
duration_gst = delay_init_qubit_start + max_gate_duration + delay_init_qubit_end


duration_wait = 200
duration_compensation_pulse_initialization = 4 * (duration_init_1q + 2 * duration_readout) + 2 * (duration_init_2q + duration_readout + duration_init_1q)
duration_compensation_pulse_readout = 2 * (duration_init_1q + 2 * duration_readout) + 1 * (duration_init_2q + duration_readout + duration_init_1q)
duration_compensation_pulse_gst = duration_gst
duration_compensation_pulse_full = int(0.3 * duration_compensation_pulse_initialization + duration_compensation_pulse_gst + duration_compensation_pulse_readout)
duration_compensation_pulse_full = 100 * (duration_compensation_pulse_full // 100)



# Points in the charge stability map [V1, V2]

level_inits = {
    "P1-P2": [-0.05, 0.05, 0.0, 0.0, 0.0],
    "P3": [0.0, 0.0, -0.05, 0.0, 0.0],
    "P4-P5": [0.0, 0.0, 0.0, -0.06, 0.04],
}
level_readouts = {
    "P1-P2": [-0.01, 0.01, 0.0, 0.0, 0.0],
    "P3": [-0.01, 0.01, 0.0, 0.0, 0.0],
    "P4-P5": [0.0, 0.0, 0.0, -0.01, 0.01],
}
level_ops = level_inits
level_waits = level_readouts


seq = VoltageGateSequence(config, sweep_gates)
seq.add_points("initialization_1q_P1-P2", level_inits["P1-P2"], duration_init_1q)
seq.add_points("initialization_1q_P4-P5", level_inits["P4-P5"], duration_init_1q)
seq.add_points("initialization_1q_P3", level_inits["P3"], duration_init_1q)

seq.add_points("initialization_2q_P1-P2", level_inits["P1-P2"], duration_init_2q)
seq.add_points("initialization_2q_P4-P5", level_inits["P4-P5"], duration_init_2q)
seq.add_points("initialization_2q_P3", level_inits["P3"], duration_init_2q)

seq.add_points("operation_P1-P2", level_ops["P1-P2"], duration_gst)
seq.add_points("operation_P4-P5", level_ops["P4-P5"], duration_gst)
seq.add_points("operation_P3", level_ops["P3"], duration_gst)

seq.add_points("readout_P1-P2", level_readouts["P1-P2"], duration_readout)
seq.add_points("readout_P3", level_readouts["P3"], duration_readout)
seq.add_points("readout_P4-P5", level_readouts["P4-P5"], duration_readout)

seq.add_points("wait_P1-P2", level_waits["P1-P2"], duration_wait)
seq.add_points("wait_P3", level_waits["P3"], duration_wait)
seq.add_points("wait_P4-P5", level_waits["P4-P5"], duration_wait)



def perform_initialization(I, Q, P, I1_st, I2_st, I3_st):
    qua_vars1 = I[0], Q[0], P[0] # tank_circuit1
    qua_vars2 = I[1], Q[1], P[1] # tank_circuit2

    read_init12(*qua_vars1, None, None, do_save=[False, False])  # save_count = 2 -> 2
    # wait_after_read_init(plungers="P1-P2")

    # 1st
    read_init3(*qua_vars1, None, do_save=False)  # save_count = 1 -> 3
    # wait_after_read_init(plungers="P3")

    read_init12(*qua_vars1, None, None, do_save=[False, False])  # save_count = 2 -> 5
    # wait_after_read_init(plungers="P1-P2")

    # 2nd
    read_init3(*qua_vars1, I1_st, do_save=True)  # save_count = 1 -> 6
    # wait_after_read_init(plungers="P3")

    read_init12(*qua_vars1, None, I2_st, do_save=[False, True])  # save_count = 2 -> 8
    # wait_after_read_init(plungers="P1-P2")

    read_init45(*qua_vars2, None, I3_st, do_save=[False, True])  # save_count = 2 -> 10
    # wait_after_read_init(plungers="P4-P5")


def perform_readout(I, Q, P, I1_st, I2_st, I3_st):
    qua_vars1 = I[0], Q[0], P[0] # tank_circuit1
    qua_vars2 = I[1], Q[1], P[1] # tank_circuit2

    read_init12(*qua_vars1, I1_st, None, do_save=[True, False])  # save_count = 2 -> 12
    # wait_after_read_init(plungers="P1-P2")

    read_init3(*qua_vars1, I2_st, do_save=True)  # save_count = 1 -> 13
    # wait_after_read_init(plungers="P1-P2")

    read_init45(*qua_vars2, I3_st, None, do_save=[True, False])  # save_count = 2 -> 15
    # wait_after_read_init(plungers="P4-P5")


def read_init12(I, Q, P, I1_st, I2_st, do_save=[False, False]):
    qua_vars = I, Q, P

    plungers = "P1-P2"
    threshold = TANK_CIRCUIT_CONSTANTS["tank_circuit1"]["threshold"]
    other_elements = get_other_elements(elements_in_use=["qubit1", "tank_circuit1"] + sweep_gates, all_elements=all_elements)

    P = measure_parity(*qua_vars, I1_st, plungers=plungers, tank_circuit="tank_circuit1", threshold=threshold, do_save=do_save[0])
    wait(duration_readout * u.ns, "qubit1")

    play_feedback(plungers=plungers, qubit="qubit1", parity=P)    
    wait(duration_init_1q * u.ns, "tank_circuit1")

    P = measure_parity(*qua_vars, I2_st, plungers=plungers, tank_circuit="tank_circuit1", threshold=threshold, do_save=do_save[1])
    wait(duration_readout * u.ns, "qubit1")

    wait((duration_init_1q + 2 * duration_readout) * u.ns, *other_elements)

    return P


def read_init45(I, Q, P, I1_st, I2_st, do_save=[False, False]):
    qua_vars = I, Q, P

    plungers = "P4-P5"
    tank_circuit = "tank_circuit2"
    threshold = TANK_CIRCUIT_CONSTANTS["tank_circuit2"]["threshold"]
    other_elements = get_other_elements(elements_in_use=["qubit5", "tank_circuit2"] + sweep_gates, all_elements=all_elements)

    P = measure_parity(*qua_vars, I1_st, plungers=plungers, tank_circuit=tank_circuit, threshold=threshold, do_save=do_save[0])
    wait(duration_readout * u.ns, "qubit5")

    play_feedback(plungers=plungers, qubit="qubit5", parity=P)
    wait(duration_init_1q * u.ns, "tank_circuit2")

    P = measure_parity(*qua_vars, I2_st, plungers=plungers, tank_circuit=tank_circuit, threshold=threshold, do_save=do_save[1])
    wait(duration_readout * u.ns, "qubit5")

    wait((duration_init_1q + 2 * duration_readout) * u.ns, *other_elements)

    return P


def read_init3(I, Q, P, I_st, do_save=False):
    qua_vars = I, Q, P

    plungers = "P3"
    threshold = TANK_CIRCUIT_CONSTANTS["tank_circuit1"]["threshold"]
    other_elements = get_other_elements(elements_in_use=["B2", "qp_control_c3t2", "qubit3", "tank_circuit1"] + sweep_gates, all_elements=all_elements)

    play_CNOT_c3t2(plungers=plungers)
    wait(duration_init_2q * u.ns, "tank_circuit1", "qubit3")

    P = measure_parity(*qua_vars, I_st, plungers=plungers, tank_circuit="tank_circuit1", threshold=threshold, do_save=do_save)
    wait(duration_readout * u.ns, "B2", "qp_control_c3t2", "qubit3")

    play_feedback(plungers=plungers, qubit="qubit3", parity=P)
    wait(duration_init_1q * u.ns, "B2", "qp_control_c3t2", "tank_circuit1")

    wait((duration_init_2q + duration_readout + duration_init_1q) * u.ns, *other_elements)

    return P


def play_feedback(plungers, qubit, parity):
    seq.add_step(voltage_point_name=f"initialization_1q_{plungers}")

    wait(delay_init_qubit_start * u.ns, qubit) if delay_init_qubit_start >= 16 else None
    # TODO:
    if do_feedback:
        play("x180_kaiser", qubit, condition=parity)
    else:
        wait(delay_feedback * u.ns, qubit)
        play("x180_kaiser", qubit)
    wait(delay_init_qubit_end * u.ns, qubit) if delay_init_qubit_end >= 16 else None


def play_CNOT_c3t2(plungers):
    seq.add_step(voltage_point_name=f"initialization_2q_{plungers}")

    wait(delay_init_qubit_start * u.ns, "B2", "qp_control_c3t2") if delay_init_qubit_start >= 16 else None
    play("step" * amp(0.1), "B2", duration=CROT_DC_LEN * u.ns)
    play("x180_kaiser", "qp_control_c3t2")
    wait(delay_init_qubit_end * u.ns, "B2", "qp_control_c3t2") if delay_init_qubit_end >= 16 else None


def wait_after_read_init(plungers):
    other_elements = get_other_elements(elements_in_use=sweep_gates, all_elements=all_elements)

    seq.add_step(voltage_point_name=f"wait_{plungers}")
    wait(duration_wait * u.ns, *other_elements)


def measure_parity(I, Q, P, I_st, plungers, tank_circuit, threshold, do_save=False):
    # Play the triangle
    # seq.add_step(voltage_point_name=f"initialization_1q_{plungers}")
    seq.add_step(voltage_point_name=f"readout_{plungers}")
    # Measure the dot right after the qubit manipulation
    wait(delay_read_reflec_start * u.ns, tank_circuit) if delay_read_reflec_start >= 16 else None
    measure(
        "readout",
        tank_circuit,
        None,
        demod.full("cos", I, "out1"),
        demod.full("sin", Q, "out1"),
    )
    wait(delay_read_reflec_end * u.ns, tank_circuit) if delay_read_reflec_end >= 16 else None

    assign(P, I > threshold)  # TODO: I > threashold is even?

    if do_save and I_st is not None:
        save(I, I_st)
        # save(Q, Q_st)
        # save(P, P_st)

    return P


with program() as PROGRAM_GST:
    n = declare(int)
    n_shots = declare(int)
    circ = declare(int)
    idx = declare(int)
    count = declare(int, value=0)
    division = declare(int, value=1)
    # encoded_circuit = declare(int, value=[52, 4, 5, 7, 16, 18])
    encoded_circuit = declare_input_stream(
        int,
        name="_encoded_circuit",
        size=sequence_max_len + 3, # 2 to account for [circ_idx, seq_len, remaining_duraiton_case]
    )  # input stream the sequence

    n_st = declare_stream()  # Stream for the iteration number (progress bar)
    n_shots_st = declare_stream()
    circ_idx_st = declare_stream()
    circ_len_st = declare_stream()
    
    I = [declare(fixed) for _ in range(num_tank_circuits)]
    Q = [declare(fixed) for _ in range(num_tank_circuits)]
    P = [declare(bool) for _ in range(num_tank_circuits)]  # true if even parity
    I_st = [declare_stream() for _ in range(2)]
    # Q_st = [declare_stream() for _ in range(15)]
    # P_st = [declare_stream() for _ in range(15)]

    # Ensure that the result variables are assign to the pulse processor used for readout
    assign_variables_to_element("tank_circuit1", I[0], Q[0], P[0])
    assign_variables_to_element("tank_circuit2", I[1], Q[1], P[1])

    with for_each_(n_shots, list_n_shots):

        with for_(circ, 0, circ < num_cicuits, circ + 1):
            advance_input_stream(encoded_circuit)  # ordered or randomized

            circ_idx = encoded_circuit[0] # just a sequential index for this circuit 
            circ_len = encoded_circuit[1] # gate sequence length for this circuit

            with for_(n, 0, n < n_shots, n + 1):
                assign(count, count + 1)

                with strict_timing_():

                    # RI12 -> 2 x (R3 -> R12) -> RI45
                    # perform_initialization((I, Q, P, I_st[0], I_st[1], I_st[2]))
                    read_init12(I[0], Q[0], P[0], None, I_st[0], do_save=[False, True])

                    # Navigate through the charge stability map
                    seq.add_step(voltage_point_name=f"operation_{plungers}")
                    wait(delay_init_qubit_start * u.ns, qubit) if delay_init_qubit_start >= 16 else None

                    other_elements = get_other_elements(elements_in_use=[qubit] + sweep_gates, all_elements=all_elements)
                    wait(duration_gst * u.ns, *other_elements)

                    with for_(idx, 2, idx < circ_len + 2, idx + 1):

                        with switch_(encoded_circuit[idx], unsafe=True):
                            # baseband operation is fixed regardless L
                            # normal:just run till the end with Null
                            # option: adjust the length accoridngly

                            with case_(0):
                                wait(4 * PI_HALF_LEN * u.ns, qubit)
                            with case_(1):
                                wait(PI_HALF_LEN * u.ns, qubit)
                            with case_(2):
                                wait(2 * PI_HALF_LEN * u.ns, qubit)
                            with case_(3):
                                wait(3 * PI_HALF_LEN * u.ns, qubit)
                            
                            # '{}': 4, # I
                            # 'Gxpi2:0': 5,
                            # 'Gypi2:0': 6,
                            # 'Gxpi2:0Gxpi2:0': 7,
                            # 'Gxpi2:0Gxpi2:0Gxpi2:0': 9,
                            # 'Gypi2:0Gypi2:0Gypi2:0': 10,
                            # 'Gxpi2:0Gypi2:0': 8,
                            # 'Gxpi2:0Gxpi2:0Gypi2:0': 11
                            
                            # prep & meas fiducials and germs
                            with case_(4): #   I = XXXX
                                play("x90_kaiser", qubit)
                                play("x90_kaiser", qubit)
                                play("x90_kaiser", qubit)
                                play("x90_kaiser", qubit)
                            with case_(5):
                                play("x90_kaiser", qubit)
                            with case_(6):
                                play("y90_kaiser", qubit)
                            with case_(7):
                                play("x90_kaiser", qubit)
                                play("x90_kaiser", qubit)
                            with case_(8):
                                play("x90_kaiser", qubit)
                                play("y90_kaiser", qubit)
                            with case_(9):
                                play("x90_kaiser", qubit)
                                play("x90_kaiser", qubit)
                                play("x90_kaiser", qubit)
                            with case_(10):
                                play("y90_kaiser", qubit)
                                play("y90_kaiser", qubit)
                                play("y90_kaiser", qubit)
                            with case_(11):
                                play("x90_kaiser", qubit)
                                play("x90_kaiser", qubit)
                                play("y90_kaiser", qubit)

                    wait(delay_init_qubit_end * u.ns, qubit) if delay_init_qubit_start >= 16 else None

                    # RI12 -> R3 -> RI45
                    # perform_readout(I, Q, P, I_st[3], I_st[4], I_st[5])
                    read_init12(I[0], Q[0], P[0], I_st[1], None, do_save=[True, False])

                    seq.add_compensation_pulse(duration=duration_compensation_pulse_full)
                
                save(n, n_st)
                save(n_shots, n_shots_st)
                save(circ_idx, circ_idx_st)

                seq.ramp_to_zero()
                wait(1000 * u.ns)

            with if_(count == division * batch_size):
                assign(division, division + 1)
                # pause to outstream the data
                pause()


    with stream_processing():
        n_st.buffer(batch_size).save("n_history")
        n_shots_st.buffer(batch_size).save("n_shots_history")
        circ_idx_st.buffer(batch_size).save("circ_idx_history")
        for k in range(2):
            I_st[k].buffer(batch_size).save(f"I{k:d}")


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
simulate = False
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

    sourceFile = open("debug_20_gate_set_tomography.py", "w")
    print(generate_qua_script(PROGRAM_GST, config), file=sourceFile)
    sourceFile.close()

    # Open the quantum machine
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(PROGRAM_GST, compiler_options=CompilerOptionArguments(flags=["not-strict-timing"]))


    fetch_names = ["n_history", "n_shots_history", "circ_idx_history"]
    fetch_names.extend([f"I{k:d}" for k in range(2)])

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
            _encoded_circuit, C, P, G, d, M, Ph4, Ph = get_encoded_circuit(row)

            current_datetime = datetime.now()
            current_datetime_str = current_datetime.strftime("%Y/%m/%d-%H:%M:%S")
            elapsed_time = current_datetime - start_time
            elapsed_time_secs = int(elapsed_time.total_seconds())
            _log_this = f"{current_datetime_str}, batch_idx: {batch_idx} / {num_batches}, no: {i_row + 1}, n_shots: {_n_shots}, circ_idx = {C}, n_circuits: P={P}, G={G}, d={d}, M={M}, Ph4={Ph4}, Ph={Ph}, elapsed_secs: {elapsed_time_secs}"
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
                np.savez(file = data_handler.path / f"data_{batch_idx:08d}.npz", **data_dict)
                batch_idx +=1
                job.resume()

    qm.close()

# %%
