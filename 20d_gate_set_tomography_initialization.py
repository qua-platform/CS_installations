# %%

import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
from qm import *
from qm import QuantumMachinesManager, SimulationConfig
from qm.qua import *
from qualang_tools.addons.variables import assign_variables_to_element
from qualang_tools.plot import interrupt_on_close
from qualang_tools.results import fetching_tool, progress_counter
from qualang_tools.voltage_gates import VoltageGateSequence
from macros import get_other_elements

from configuration_with_lffem import *

matplotlib.use('TkAgg')

###################
#  Util funciton  #
###################


def get_dataframe_encoded_sequence():
    path = "./encoded_parsed_dataset.csv"
    df = pd.read_csv(path, header=0)  # Use header=0 to indicate the first row is the header
    df["full_gate_sequence_duration"] = PI_HALF_LEN * df["full_native_gate_count"]
    df.reset_index(inplace=True)
    # df = df.tail(60)
    # df = df.head(10)
    return df


###################
# The QUA program #
###################

qubit = "qubit1"
plungers = "P1-P2"

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


delay_init_qubit_start = 16
delay_init_qubit_end = 16
duration_init_1q = delay_init_qubit_start + PI_LEN + delay_init_qubit_end
duration_init_2q = delay_init_qubit_start + CROT_RF_LEN + delay_init_qubit_end
assert delay_init_qubit_start == 0 or delay_init_qubit_start >= 16
assert delay_init_qubit_end == 0 or delay_init_qubit_end >= 16

delay_read_reflec_start = 16
delay_read_reflec_end = 16
duration_readout = delay_read_reflec_start + REFLECTOMETRY_READOUT_LEN + delay_read_reflec_end
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



def perform_initialization(I, Q, P, I_st, Q_st, P_st):
    qua_vars0 = I[0], Q[0], P[0], I_st, Q_st, P_st
    qua_vars1 = I[1], Q[1], P[1], I_st, Q_st, P_st

    res1_1 = read_init12(*qua_vars0)  # save_count = 2 -> 2
    # wait_after_read_init(plungers="P1-P2")

    # 1st
    res1_2 = read_init3(*qua_vars0)  # save_count = 1 -> 3
    # wait_after_read_init(plungers="P3")

    res1_3 = read_init12(*qua_vars0)  # save_count = 2 -> 5
    # wait_after_read_init(plungers="P1-P2")

    # 2nd
    res1_4 = read_init3(*qua_vars0)  # save_count = 1 -> 6
    # wait_after_read_init(plungers="P3")

    res1_5 = read_init12(*qua_vars0)  # save_count = 2 -> 8
    # wait_after_read_init(plungers="P1-P2")

    res2_1 = read_init45(*qua_vars1)  # save_count = 2 -> 10
    # wait_after_read_init(plungers="P4-P5")


def perform_readout(I, Q, P, I_st, Q_st, P_st):
    qua_vars0 = I[0], Q[0], P[0], I_st, Q_st, P_st
    qua_vars1 = I[1], Q[1], P[1], I_st, Q_st, P_st

    res1_6 = read_init12(*qua_vars0)  # save_count = 2 -> 12
    # wait_after_read_init(plungers="P1-P2")

    res1_7 = read_init3(*qua_vars0)  # save_count = 1 -> 13
    # wait_after_read_init(plungers="P1-P2")

    res2_2 = read_init45(*qua_vars1)  # save_count = 2 -> 15
    # wait_after_read_init(plungers="P4-P5")


def read_init12(I, Q, P, I_st, Q_st, P_st):
    qua_vars = I, Q, P, I_st, Q_st, P_st
    plungers = "P1-P2"
    threshold = TANK_CIRCUIT_CONSTANTS["tank_circuit1"]["threshold"]
    other_elements = get_other_elements(elements_in_use=["qubit1", "tank_circuit1"] + sweep_gates, all_elements=all_elements)

    P = measure_parity(*qua_vars, plungers=plungers, tank_circuit="tank_circuit1", threshold=threshold)
    wait(duration_readout * u.ns, "qubit1")

    play_feedback(plungers=plungers, qubit="qubit1", parity=P)    
    wait(duration_init_1q * u.ns, "tank_circuit1")

    P = measure_parity(*qua_vars, plungers=plungers, tank_circuit="tank_circuit1", threshold=threshold)
    wait(duration_readout * u.ns, "qubit1")

    wait((duration_init_1q + 2 * duration_readout) * u.ns, *other_elements)

    return P


def read_init45(I, Q, P, I_st, Q_st, P_st):
    qua_vars = I, Q, P, I_st, Q_st, P_st
    plungers = "P4-P5"
    tank_circuit = "tank_circuit2"
    threshold = TANK_CIRCUIT_CONSTANTS["tank_circuit2"]["threshold"]
    other_elements = get_other_elements(elements_in_use=["qubit5", "tank_circuit2"] + sweep_gates, all_elements=all_elements)

    P = measure_parity(*qua_vars, plungers=plungers, tank_circuit=tank_circuit, threshold=threshold)
    wait(duration_readout * u.ns, "qubit5")

    play_feedback(plungers=plungers, qubit="qubit5", parity=P)
    wait(duration_init_1q * u.ns, "tank_circuit2")

    P = measure_parity(*qua_vars, plungers=plungers, tank_circuit=tank_circuit, threshold=threshold)
    wait(duration_readout * u.ns, "qubit5")

    wait((duration_init_1q + 2 * duration_readout) * u.ns, *other_elements)

    return P


def read_init3(I, Q, P, I_st, Q_st, P_st):
    qua_vars = I, Q, P, I_st, Q_st, P_st
    plungers = "P3"
    threshold = TANK_CIRCUIT_CONSTANTS["tank_circuit1"]["threshold"]
    other_elements = get_other_elements(elements_in_use=["B2", "qp_control_c3t2", "qubit3", "tank_circuit1"] + sweep_gates, all_elements=all_elements)

    play_CNOT_c3t2(plungers=plungers)
    wait(duration_init_2q * u.ns, "tank_circuit1", "qubit3")

    P = measure_parity(*qua_vars, plungers=plungers, tank_circuit="tank_circuit1", threshold=threshold)
    wait(duration_readout * u.ns, "B2", "qp_control_c3t2", "qubit3")

    play_feedback(plungers=plungers, qubit="qubit3", parity=P)
    wait(duration_init_1q * u.ns, "B2", "qp_control_c3t2", "tank_circuit1")

    wait((duration_init_2q + duration_readout + duration_init_1q) * u.ns, *other_elements)

    return P


def play_feedback(plungers, qubit, parity):
    seq.add_step(voltage_point_name=f"initialization_1q_{plungers}")

    wait(delay_init_qubit_start * u.ns, qubit) if delay_init_qubit_start >= 16 else None
    # play("x180", qubit, condition=parity)
    play("x180", qubit)
    wait(delay_init_qubit_end * u.ns, qubit) if delay_init_qubit_end >= 16 else None


def play_CNOT_c3t2(plungers):
    seq.add_step(voltage_point_name=f"initialization_2q_{plungers}")

    wait(delay_init_qubit_start * u.ns, "B2", "qp_control_c3t2") if delay_init_qubit_start >= 16 else None
    play("step" * amp(0.1), "B2", duration=CROT_DC_LEN * u.ns)
    play("x180", "qp_control_c3t2")
    wait(delay_init_qubit_end * u.ns, "B2", "qp_control_c3t2") if delay_init_qubit_end >= 16 else None


def wait_after_read_init(plungers):
    other_elements = get_other_elements(elements_in_use=sweep_gates, all_elements=all_elements)

    seq.add_step(voltage_point_name=f"wait_{plungers}")
    wait(duration_wait * u.ns, *other_elements)


def measure_parity(I, Q, P, I_st, Q_st, P_st, plungers, tank_circuit, threshold):
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
    save(I, I_st)
    save(Q, Q_st)
    save(P, P_st)
    return P


with program() as PROGRAM_GST:
    n = declare(int)
    n_shots = declare(int)
    circ = declare(int)
    idx = declare(int)
    encoded_circuit = declare_input_stream(
        int,
        name="_encoded_circuit_input_stream",
        size=sequence_max_len + 3, # 2 to account for [circ_idx, seq_len, remaining_duraiton_case]
    )  # input stream the sequence
    idx_st = declare_stream()

    n = declare(int)  # QUA integer used as an index for the averaging loop
    n_st = declare_stream()  # Stream for the iteration number (progress bar)
    I = [declare(fixed) for _ in range(num_tank_circuits)]
    Q = [declare(fixed) for _ in range(num_tank_circuits)]
    P = [declare(bool) for _ in range(num_tank_circuits)]  # true if even parity
    I_st = declare_stream()
    Q_st = declare_stream()
    P_st = declare_stream()

    # Ensure that the result variables are assign to the pulse processor used for readout
    assign_variables_to_element("tank_circuit1", I[0], Q[0], P[0])
    assign_variables_to_element("tank_circuit2", I[1], Q[1], P[1])


    with for_each_(n_shots, list_n_shots):

        with for_(circ, 0, circ < num_cicuits, circ + 1):
            advance_input_stream(encoded_circuit)  # ordered or randomized

            circ_idx = encoded_circuit[0] # just a sequential index for this circuit 
            circ_len = encoded_circuit[1] # gate sequence length for this circuit

            with for_(n, 0, n < n_shots, n + 1):
                
                # play("square_const", qubit)
                # play("square_step", "P1", duration=const_len * u.ns)

                with strict_timing_():

                    # TODO:
                    perform_initialization(I, Q, P, I_st, Q_st, P_st)

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
                                # TODO: initialization step
                                wait(PI_HALF_LEN * u.ns, qubit)

                            # prep fiducials
                            with case_(1): #   I = XXXX
                                play("square_x90", qubit)
                                play("square_x90", qubit)
                                play("square_x90", qubit)
                                play("square_x90", qubit)
                            with case_(2):
                                play("square_x90", qubit)
                            with case_(3):
                                play("square_y90", qubit)
                            with case_(4):
                                play("square_x90", qubit)
                                play("square_x90", qubit)
                            with case_(5):
                                play("square_x90", qubit)
                                play("square_x90", qubit)
                                play("square_x90", qubit)
                            with case_(6):
                                play("square_y90", qubit)
                                play("square_y90", qubit)
                                play("square_y90", qubit)

                            # germs
                            with case_(7): #   I = XXXX
                                play("square_x90", qubit)
                                play("square_x90", qubit)
                                play("square_x90", qubit)
                                play("square_x90", qubit)
                            with case_(8):
                                play("square_x90", qubit)
                            with case_(9):
                                play("square_y90", qubit)
                            with case_(10):
                                play("square_x90", qubit)
                                play("square_y90", qubit)
                            with case_(11):
                                play("square_x90", qubit)
                                play("square_x90", qubit)
                                play("square_y90", qubit)

                            # meas fiducial
                            with case_(12): #   I = XXXX
                                play("square_x90", qubit)
                                play("square_x90", qubit)
                                play("square_x90", qubit)
                                play("square_x90", qubit)
                            with case_(13):
                                play("square_x90", qubit)
                            with case_(14):
                                play("square_y90", qubit)
                            with case_(15):
                                play("square_x90", qubit)
                                play("square_x90", qubit)
                            with case_(16):
                                play("square_x90", qubit)
                                play("square_x90", qubit)
                                play("square_x90", qubit)
                            with case_(17):
                                play("square_y90", qubit)
                                play("square_y90", qubit)
                                play("square_y90", qubit)

                            for c_, row in df_enc_seqs.iterrows():
                                with case_(17 + int(row["circ_idx"])):
                                    wait((max_gate_duration - int(row["full_gate_sequence_duration"])) * u.ns, qubit)

                    wait(delay_init_qubit_end * u.ns, qubit) if delay_init_qubit_start >= 16 else None

                    # TODO:
                    perform_readout(I, Q, P, I_st, Q_st, P_st)

                    seq.add_compensation_pulse(duration=duration_compensation_pulse_full)

                seq.ramp_to_zero()
                wait(1000 * u.ns)
                
                save(n, idx_st)
                save(n_shots, idx_st)
                save(circ_idx, idx_st)
                save(circ_len, idx_st)


    with stream_processing():
        idx_st.buffer(4).save_all("circuit_history")
        I_st.buffer(15).save_all("I12")
        Q_st.buffer(15).save_all("Q12")
        P_st.boolean_to_int().buffer(15).save_all("P12")



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

    sourceFile = open("debug08.py", "w")
    print(generate_qua_script(PROGRAM_GST, config), file=sourceFile)
    sourceFile.close()

    # Open the quantum machine
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(PROGRAM_GST, compiler_options=CompilerOptionArguments(flags=["not-strict-timing"]))
    # job = qm.execute(PROGRAM_GST)

    results = fetching_tool(
        job, data_list=["idx_history", "I12", "Q12", "P12"], mode="live"
    )
    # Waits (blocks the Python console) until all results have been acquired
    # results = fetching_tool(job, data_list=["circuit_history"], mode="live")

    record = []
    for _n_shots in list_n_shots:
        encoded_circuit_batch = df_enc_seqs[
            ["index", "P_enc_seq", "G_enc_seq", "d_enc_seq", "M_enc_seq", "full_gate_sequence_duration"]
            ].sample(frac=1, random_state=_n_shots)

        for i, row in encoded_circuit_batch.iterrows():
            C = int(row["circ_idx"])
            P = int(row["P_enc_seq"])
            G = int(row["G_enc_seq"])
            d = int(row["d_enc_seq"])
            M = int(row["M_enc_seq"])
            D = int(row["full_gate_sequence_duration"])

            seq_len = 0
            _encoded_circuit_input_stream = [C]
            if P != -1:
                _encoded_circuit_input_stream.append(P)
                seq_len += 1
            if G != -1:
                _encoded_circuit_input_stream.extend([G] * d)
                seq_len += d
            if M != -1:
                _encoded_circuit_input_stream.append(M)
                seq_len += 1

            # sequence duration
            _encoded_circuit_input_stream.append(C + 17)
            seq_len += 1

            # sequence length
            _encoded_circuit_input_stream.insert(1, seq_len)

            record.append([_n_shots] + _encoded_circuit_input_stream)

            print(f"n_shots: {_n_shots}, circ_idx = {i}, n_circuits: P={P}, G={G}, d={d}, M={M}")
            job.push_to_input_stream("_encoded_circuit_input_stream", _encoded_circuit_input_stream)
            print("    ---> success!")

    circuit_history, I12, Q12, P12 = results.fetch_all()

    qm.close()
# %%
