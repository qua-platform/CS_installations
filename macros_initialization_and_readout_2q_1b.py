# %%
"""
        Readout & Init
"""

from qm import *
from qm.qua import *

from configuration_with_lffem_csrack import *
# from configuration_with_lffem import *
from macros_voltage_gate_sequence import VoltageGateSequence

##################
#   Parameters   #
##################

qubit = "qubit1"
pi_len = QUBIT_CONSTANTS[qubit]["square_pi_len"]
pi_amp = QUBIT_CONSTANTS[qubit]["square_pi_amp"]

qubits = ["qubit1", "qubit2"]
sweep_gates = ["P0_sticky", "P1_sticky", "B1_sticky"]
tank_circuits = ["tank_circuit1"]
num_tank_circuits = len(TANK_CIRCUIT_CONSTANTS)
all_elements = qubits + sweep_gates + tank_circuits
do_feedback = True  # False for test. True for actual.


# duration_init = 10_000 # DO NOT USE * u.ns
duration_ramp_init = 200  # DO NOT USE * u.ns
duration_ramp_readout = 52  # DO NOT USE * u.ns
duration_ramp_barrier = 100


delay_init_start = 100  # + RF_SWITCH_DELAY
# delay_feedback = 240
delay_init_end = 100
duration_init_1q = delay_init_start + pi_len + delay_init_end
assert delay_init_start == 0 or delay_init_start >= 16
assert delay_init_end == 0 or delay_init_end >= 16


delay_read_reflec_start = 400
delay_read_reflec_end = 100
duration_readout = duration_ramp_readout + delay_read_reflec_start + REFLECTOMETRY_READOUT_LEN + delay_read_reflec_end
assert delay_read_reflec_start == 0 or delay_read_reflec_start >= 16
assert delay_read_reflec_end == 0 or delay_read_reflec_end >= 16


delay_barrier_crot = 100
delay_barrier_gate = 1000

duration_ops = delay_init_start + delay_barrier_gate + duration_ramp_barrier + delay_barrier_crot + pi_len + delay_barrier_crot + duration_ramp_barrier + delay_init_end

duration_ops_before_barrier = delay_init_start + delay_barrier_gate

duration_ops_barrier = duration_ramp_barrier + delay_barrier_crot + pi_len + delay_barrier_crot + duration_ramp_barrier

duration_ops_before_switch = delay_init_start + delay_barrier_gate + duration_ramp_barrier + delay_barrier_crot - RF_SWITCH_DELAY


# Points in the charge stability map [V1, V2]
level_init_arr = np.array(LEVEL_INIT + [0.0])
level_readout_arr = np.array(LEVEL_READOUT + [0.0])
level_init_list = level_init_arr.tolist()
level_readout_list = level_readout_arr.tolist()


set_init_as_dc_offset = True
if set_init_as_dc_offset:
    level_readout_offset_arr = level_readout_arr - level_init_arr
    level_init_offset_arr = np.array([0.0, 0.0, 0.0])  # level_init_arr - level_init_arr

    level_readout_offset_list = level_readout_offset_arr.tolist()
    level_init_offset_list = level_init_offset_arr.tolist()


seq = VoltageGateSequence(config, sweep_gates)
if set_init_as_dc_offset:
    seq.add_points("initialization_1q", level_init_offset_list, duration_init_1q)  #
    seq.add_points("operation_before_crot", level_init_offset_list, duration_ops_before_barrier)  #
    seq.add_points("operation_crot", level_init_offset_list, duration_ops_barrier)  #
    seq.add_points("operation_after_crot", level_init_offset_list, delay_init_end)  #
    seq.add_points("readout", level_readout_offset_list, duration_readout)  #
else:
    seq.add_points("initialization_1q", level_init_list, duration_init_1q)  #
    seq.add_points("operation_before_crot", level_init_list, duration_ops_before_barrier)  #
    seq.add_points("operation_crot", level_init_list, duration_ops_barrier)  #
    seq.add_points("operation_after_crot", level_init_list, delay_init_end)  #
    seq.add_points("readout", level_readout_list, duration_readout)  #


###################
#   Read & Init   #
###################


# def play_crot(qubit, parity):
#     seq.add_step(voltage_point_name=f"operation_crot", ramp_duration=duration_ramp_init)

#     wait(duration_ramp_init * u.ns, qubit)
#     wait(delay_init_start * u.ns, qubit)
#     wait(duration_ramp_init // 4, "rf_switch", qubit)
#     play("trigger", "rf_switch", duration=(RF_SWITCH_DELAY + pi_len) // 4)
#     wait(RF_SWITCH_DELAY // 4, qubit)
#     if do_feedback:
#         play("x180_kaiser", qubit, condition=parity)
#     else:
#         wait(delay_feedback * u.ns, qubit)
#         play("x180_kaiser", qubit)
#     wait(delay_init_end * u.ns, qubit)


def measure_parity(I, Q, P, I_st, Q_st, P_st, tank_circuit, threshold):
    P0 = declare(bool)

    # move to readout level
    seq.add_step(voltage_point_name="readout", ramp_duration=duration_ramp_readout)
    # measure
    wait(duration_ramp_readout * u.ns, tank_circuit)
    wait(delay_read_reflec_start * u.ns, tank_circuit)
    measure(
        "readout",
        tank_circuit,
        None,
        demod.full("cos", I, "out1"),
        demod.full("sin", Q, "out1"),
    )
    wait(delay_read_reflec_end * u.ns, tank_circuit)

    assign(P0, I < threshold)  # TODO: I > threashold is even?
    # assign(P0, P)
    if I_st is not None:
        save(I, I_st)
    if Q_st is not None:
        save(Q, Q_st)
    if P_st is not None:
        save(P0, P_st)

    return P0
