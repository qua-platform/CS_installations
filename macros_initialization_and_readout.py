# %%
"""
        Readout & Init
"""

from datetime import datetime
from typing import Literal

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

from configuration_with_lffem import *
from macros import get_other_elements

##################
#   Parameters   #
##################

qubits = ["qubit1", "qubit2", "qubit3", "qubit4", "qubit5"]
sweep_gates = ["P1_sticky", "P2_sticky", "P3_sticky", "P4_sticky", "P5_sticky"]
barrier_gates = ["B2"]
qp_controls = ["qp_control_c3t2"]
tank_circuits = ["tank_circuit1", "tank_circuit2"]
num_tank_circuits = len(TANK_CIRCUIT_CONSTANTS)
all_elements = qubits + sweep_gates + barrier_gates + qp_controls + tank_circuits
do_feedback = False  # False for test. True for actual.


delay_init_qubit_start = 16
delay_feedback = 240
delay_init_qubit_end = 16
duration_init_1q = delay_init_qubit_start + delay_feedback + PI_LEN + delay_init_qubit_end
duration_init_2q = delay_init_qubit_start + CROT_RF_LEN + delay_init_qubit_end
assert delay_init_qubit_start == 0 or delay_init_qubit_start >= 16
assert delay_init_qubit_end == 0 or delay_init_qubit_end >= 16


delay_read_reflec_start = 16
delay_read_reflec_end = 16
delay_stream = 100
duration_readout = delay_read_reflec_start + REFLECTOMETRY_READOUT_LEN + delay_read_reflec_end + delay_stream
assert delay_read_reflec_start == 0 or delay_read_reflec_start >= 16
assert delay_read_reflec_end == 0 or delay_read_reflec_end >= 16


duration_wait = 200
duration_compensation_pulse_readinit12 = duration_init_1q + 2 * duration_readout
duration_compensation_pulse_readinit45 = duration_init_1q + 2 * duration_readout
duration_compensation_pulse_readinit3 = duration_init_2q + duration_readout + duration_init_1q
duration_compensation_pulse_full_initialization = 4 * duration_compensation_pulse_readinit12 + 2 * duration_compensation_pulse_readinit45
duration_compensation_pulse_full_readout = 2 * duration_compensation_pulse_readinit12 + 1 * duration_compensation_pulse_readinit45


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

seq.add_points("readout_P1-P2", level_readouts["P1-P2"], duration_readout)
seq.add_points("readout_P3", level_readouts["P3"], duration_readout)
seq.add_points("readout_P4-P5", level_readouts["P4-P5"], duration_readout)

seq.add_points("wait_P1-P2", level_waits["P1-P2"], duration_wait)
seq.add_points("wait_P3", level_waits["P3"], duration_wait)
seq.add_points("wait_P4-P5", level_waits["P4-P5"], duration_wait)


###################
#  Util funciton  #
###################


def get_dataframe_encoded_sequence():
    path = "./encoded_parsed_dataset.csv"
    df = pd.read_csv(path, header=0)  # Use header=0 to indicate the first row is the header
    df["full_gate_sequence_duration"] = PI_HALF_LEN * df["full_native_gate_count"]
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


def adjust_all_elements(removes=[], adds=[], all_elements=all_elements):
    if isinstance(removes, str):
        removes = [removes]

    if isinstance(adds, str):
        adds = [adds]

    try:
        if len(removes) >= 1:
            for r in removes:
                all_elements.remove(r)

        if len(adds) >= 1:
            for a in adds:
                all_elements.append(a)
    except:
        pass

    print("all_elements = ", all_elements)
    return all_elements


###################
#   Read & Init   #
###################


def perform_initialization(I, Q, P, I_st, Q_st, P_st, kind: Literal["full", "P1-P2", "P4-P5"], add_checkpoints=False, checkpoint_element=None):
    if add_checkpoints and checkpoint_element is not None:
        add_checkpoint_for_scope_test(checkpoint_element, all_elements=all_elements)

    if kind == "full":
        # RI12 -> 2 x (R3 -> R12) -> RI45
        perform_initialization(I, Q, P, I_st, Q_st, P_st)
    elif kind == "P1-P2":
        # RI12
        read_init12(I[0], Q[0], P[0], None, None, None, I_st[0], None, None, do_save=[False, True])
    elif kind == "P4-P5":
        # RI45
        read_init12(I[0], Q[0], P[0], None, None, None, I_st[0], None, None, do_save=[False, True])
    else:
        raise ValueError("kind must be from 'full', 'P1-P2', 'P4-P5'")

    if add_checkpoints and checkpoint_element is not None:
        add_checkpoint_for_scope_test(checkpoint_element, all_elements=all_elements)


def perform_readout(I, Q, P, I_st, Q_st, P_st, kind: Literal["full", "P1-P2", "P4-P5"], add_checkpoints=False, checkpoint_element=None):
    if add_checkpoints and checkpoint_element is not None:
        add_checkpoint_for_scope_test(checkpoint_element, all_elements=all_elements)

    if kind == "full":
        # RI12 -> R3 -> RI45
        perform_full_readout(I, Q, P, I_st, Q_st, P_st)
    elif kind == "P1-P2":
        # RI12
        read_init12(I[0], Q[0], P[0], I_st[1], None, None, None, None, None, do_save=[True, False])
    elif kind == "P4-P5":
        # RI45
        read_init45(I[0], Q[0], P[0], I_st[1], None, None, None, None, None, do_save=[True, False])
    else:
        raise ValueError("kind must be from 'full', 'P1-P2', 'P4-P5'")

    if add_checkpoints and checkpoint_element is not None:
        add_checkpoint_for_scope_test(checkpoint_element, all_elements=all_elements)


def add_checkpoint_for_scope_test(qubit, all_elements=all_elements):
    play("x180_square", qubit)
    other_elements = get_other_elements(elements_in_use=[qubit], all_elements=all_elements)
    wait(PI_LEN * u.ns, *other_elements)


def perform_full_initialization(I, Q, P, I_st, Q_st, P_st):
    qua_vars1 = I[0], Q[0], P[0]  # tank_circuit1
    qua_vars2 = I[1], Q[1], P[1]  # tank_circuit2
    qua_st_vars1 = I_st[0], Q_st[0], P_st[0]
    qua_st_vars2 = I_st[1], Q_st[1], P_st[1]
    qua_st_vars3 = I_st[2], Q_st[2], P_st[2]
    Nones = [None, None, None]

    read_init12(*qua_vars1, *Nones, *Nones, do_save=[False, False])  # save_count = 2 -> 2
    # wait_after_read_init(plungers="P1-P2")

    # 1st
    read_init3(*qua_vars1, *Nones, do_save=False)  # save_count = 1 -> 3
    # wait_after_read_init(plungers="P3")

    read_init12(*qua_vars1, *Nones, *Nones, do_save=[False, False])  # save_count = 2 -> 5
    # wait_after_read_init(plungers="P1-P2")

    # 2nd
    read_init3(*qua_vars1, *qua_st_vars1, do_save=True)  # save_count = 1 -> 6
    # wait_after_read_init(plungers="P3")

    read_init12(*qua_vars1, *Nones, *qua_st_vars2, do_save=[False, True])  # save_count = 2 -> 8
    # wait_after_read_init(plungers="P1-P2")

    read_init45(*qua_vars2, *Nones, *qua_st_vars3, do_save=[False, True])  # save_count = 2 -> 10
    # wait_after_read_init(plungers="P4-P5")


def perform_full_readout(I, Q, P, I_st, Q_st, P_st):
    qua_vars1 = I[0], Q[0], P[0]  # tank_circuit1
    qua_vars2 = I[1], Q[1], P[1]  # tank_circuit2
    qua_st_vars1 = I_st[3], Q_st[3], P_st[3]
    qua_st_vars2 = I_st[4], Q_st[4], P_st[4]
    qua_st_vars3 = I_st[5], Q_st[5], P_st[5]
    Nones = [None, None, None]

    read_init12(*qua_vars1, *qua_st_vars1, *Nones, do_save=[True, False])  # save_count = 2 -> 12
    # wait_after_read_init(plungers="P1-P2")

    read_init3(*qua_vars1, *qua_st_vars2, do_save=True)  # save_count = 1 -> 13
    # wait_after_read_init(plungers="P1-P2")

    read_init45(*qua_vars2, *qua_st_vars3, *Nones, do_save=[True, False])  # save_count = 2 -> 15
    # wait_after_read_init(plungers="P4-P5")


def read_init12(I, Q, P, I1_st, Q1_st, P1_st, I2_st, Q2_st, P2_st, do_save=[False, False]):
    qua_vars = I, Q, P
    qua_st_vars1 = I1_st, Q1_st, P1_st
    qua_st_vars2 = I2_st, Q2_st, P2_st

    plungers = "P1-P2"
    threshold = TANK_CIRCUIT_CONSTANTS["tank_circuit1"]["threshold"]
    other_elements = get_other_elements(elements_in_use=["qubit1", "tank_circuit1"] + sweep_gates, all_elements=all_elements)

    P = measure_parity(*qua_vars, *qua_st_vars1, plungers=plungers, tank_circuit="tank_circuit1", threshold=threshold, do_save=do_save[0])
    wait(duration_readout * u.ns, "qubit1")

    play_feedback(plungers=plungers, qubit="qubit1", parity=P)
    wait(duration_init_1q * u.ns, "tank_circuit1")

    P = measure_parity(*qua_vars, *qua_st_vars2, plungers=plungers, tank_circuit="tank_circuit1", threshold=threshold, do_save=do_save[1])
    wait(duration_readout * u.ns, "qubit1")

    wait((duration_init_1q + 2 * duration_readout) * u.ns, *other_elements)

    return P


def read_init45(I, Q, P, I1_st, Q1_st, P1_st, I2_st, Q2_st, P2_st, do_save=[False, False]):
    qua_vars = I, Q, P
    qua_st_vars1 = I1_st, Q1_st, P1_st
    qua_st_vars2 = I2_st, Q2_st, P2_st

    plungers = "P4-P5"
    tank_circuit = "tank_circuit2"
    threshold = TANK_CIRCUIT_CONSTANTS["tank_circuit2"]["threshold"]
    other_elements = get_other_elements(elements_in_use=["qubit5", "tank_circuit2"] + sweep_gates, all_elements=all_elements)

    P = measure_parity(*qua_vars, *qua_st_vars1, plungers=plungers, tank_circuit=tank_circuit, threshold=threshold, do_save=do_save[0])
    wait(duration_readout * u.ns, "qubit5")

    play_feedback(plungers=plungers, qubit="qubit5", parity=P)
    wait(duration_init_1q * u.ns, "tank_circuit2")

    P = measure_parity(*qua_vars, *qua_st_vars2, plungers=plungers, tank_circuit=tank_circuit, threshold=threshold, do_save=do_save[1])
    wait(duration_readout * u.ns, "qubit5")

    wait((duration_init_1q + 2 * duration_readout) * u.ns, *other_elements)

    return P


def read_init3(I, Q, P, I_st, Q_st, P_st, do_save=False):
    qua_vars = I, Q, P
    qua_st_vars = I_st, Q_st, P_st

    plungers = "P3"
    threshold = TANK_CIRCUIT_CONSTANTS["tank_circuit1"]["threshold"]
    other_elements = get_other_elements(elements_in_use=["B2", "qp_control_c3t2", "qubit3", "tank_circuit1"] + sweep_gates, all_elements=all_elements)

    play_CNOT_c3t2(plungers=plungers)
    wait(duration_init_2q * u.ns, "tank_circuit1", "qubit3")

    P = measure_parity(*qua_vars, *qua_st_vars, plungers=plungers, tank_circuit="tank_circuit1", threshold=threshold, do_save=do_save)
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


def measure_parity(I, Q, P, I_st, Q_st, P_st, plungers, tank_circuit, threshold, do_save=False):
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
    wait(delay_stream * u.ns, tank_circuit) if delay_read_reflec_end >= 16 else None

    assign(P, I > threshold)  # TODO: I > threashold is even?

    if do_save and I_st is not None:
        save(I, I_st)
    if do_save and Q_st is not None:
        save(Q, Q_st)
    if do_save and P_st is not None:
        save(P, P_st)

    return P
