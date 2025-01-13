# %%
"""
        Readout & Init
"""

from typing import Literal

import matplotlib.pyplot as plt
import pandas as pd
from qm import *
from qm.qua import *
from qualang_tools.addons.variables import assign_variables_to_element
from qualang_tools.plot import interrupt_on_close
from qualang_tools.results import (fetching_tool, progress_counter,
                                   wait_until_job_is_paused)

from configuration_with_lffem import *
from macros import get_other_elements
from macros_voltage_gate_sequence import VoltageGateSequence

##################
#   Parameters   #
##################

qubits = ["qubit1", "qubit2"]
sweep_gates = ["P1_sticky", "P2_sticky"]
tank_circuits = ["tank_circuit1"]
num_tank_circuits = len(TANK_CIRCUIT_CONSTANTS)
all_elements = qubits + sweep_gates + tank_circuits
do_feedback = True  # False for test. True for actual.


delay_init_qubit_start = 16 + RF_SWITCH_DELAY
delay_feedback = 240
delay_init_qubit_end = 16
duration_ramp_init_1q = 1000
duration_init_1q = duration_ramp_init_1q + delay_init_qubit_start + delay_feedback + PI_LEN + delay_init_qubit_end
assert delay_init_qubit_start == 0 or delay_init_qubit_start >= 16
assert delay_init_qubit_end == 0 or delay_init_qubit_end >= 16


delay_read_reflec_start = 16
delay_read_reflec_end = 16
delay_stream = 1000
duration_ramp_readout = 1000
duration_readout = duration_ramp_readout + delay_read_reflec_start + REFLECTOMETRY_READOUT_LEN + delay_read_reflec_end + delay_stream
assert delay_read_reflec_start == 0 or delay_read_reflec_start >= 16
assert delay_read_reflec_end == 0 or delay_read_reflec_end >= 16


# Points in the charge stability map [V1, V2]
level_inits = {
    "P1-P2": LEVEL_INIT,
}
level_readouts = {
    "P1-P2": LEVEL_READOUT,
}
level_ops = level_inits
level_waits = level_readouts


seq = VoltageGateSequence(config, sweep_gates)
seq.add_points("initialization_1q", level_inits["P1-P2"], duration_init_1q)
seq.add_points("readout", level_readouts["P1-P2"], duration_readout)



###################
#   Read & Init   #
###################


def play_feedback(plungers, qubit, parity, init_singlet=True):
    seq.add_step(voltage_point_name=f"initialization_1q_{plungers}", ramp_duration=duration_ramp_init_1q)

    wait((duration_ramp_init_1q + delay_init_qubit_start) * u.ns, qubit) if delay_init_qubit_start >= 16 else None
    if do_feedback:
        if init_singlet:
            play("x180_kaiser", qubit, condition=parity)
        else:
            play("x180_kaiser", qubit, condition=~parity)
    else:
        wait(delay_feedback * u.ns, qubit)
        play("x180_kaiser", qubit)
    wait(delay_init_qubit_end * u.ns, qubit) if delay_init_qubit_end >= 16 else None



def measure_parity(I, Q, P, I_st, Q_st, P_st, tank_circuit, threshold):
    # move to readout level
    seq.add_step(voltage_point_name="readout", ramp_duration=duration_ramp_readout)
    # measure
    wait((duration_ramp_readout + delay_read_reflec_start) * u.ns, tank_circuit)
    measure("readout", tank_circuit, None, demod.full("cos", I, "out1"), demod.full("sin", Q, "out1"))
    wait((delay_read_reflec_end + delay_stream) * u.ns, tank_circuit)

    assign(P, I > threshold)  # TODO: I > threashold is even?
    if I_st is not None:
        save(I, I_st)
    if Q_st is not None:
        save(Q, Q_st)
    if P_st is not None:
        save(P, P_st)

    return P
