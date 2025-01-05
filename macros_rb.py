import matplotlib.pyplot as plt
from qm import (CompilerOptionArguments, QuantumMachinesManager,
                SimulationConfig)
from qm.qua import *
from qualang_tools.addons.variables import assign_variables_to_element
from qualang_tools.bakery.randomized_benchmark_c1 import c1_table
from qualang_tools.plot import interrupt_on_close
from qualang_tools.results import fetching_tool, progress_counter
from qualang_tools.voltage_gates import VoltageGateSequence
from scipy.optimize import curve_fit

from configuration_with_lffem import *
# from configuration_with_opxplus import *


x180_len = PI_LEN
x90_len = PI_HALF_LEN
minus_x90_len = PI_HALF_LEN
y180_len = PI_LEN
y90_len = PI_HALF_LEN
minus_y90_len = PI_HALF_LEN


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


def power_law(power, a, b, p):
    return a * (p**power) + b


def generate_encoded_sequence(N, current_state=0, ends_with_inv_gate=True, num_gates_total_max=0, seed=0):

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


def play_sequence(sequence_list, depth, qb, i_from=0):
    i = declare(int)
    with for_(i, i_from, i <= depth + i_from, i + 1):
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


def generate_sequence(current_state, depth, max_circuit_depth=0, ends_with_inv_gate=False, seed=0):
    cayley = declare(int, value=c1_table.flatten().tolist())
    inv_list = declare(int, value=inv_gates)
    step = declare(int)
    sequence = declare(int, size=max_circuit_depth)
    inv_gate = declare(int)
    i = declare(int)
    rand = Random(seed=seed)

    with for_(i, 0, i < depth - 1, i + 1):
        assign(step, rand.rand_int(24))
        assign(current_state, cayley[current_state * 24 + step])
        assign(sequence[i], step)
    
    if ends_with_inv_gate:
        assign(inv_gate, inv_list[current_state])
        assign(sequence[depth - 1], inv_gate)
    else:
        assign(step, rand.rand_int(24))
        assign(current_state, cayley[current_state * 24 + step])
        assign(sequence[depth - 1], step)

    return sequence, current_state


def play_clifford(c_idx, qb):
    with switch_(c_idx, unsafe=True):
        with case_(0):
            wait(x180_len // 4, qb)
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


def play_sequence(sequence_list, depth, qb):
    i = declare(int)
    with for_(i, 0, i <= depth, i + 1):
        play_clifford(c_idx=sequence_list[i], qb=qb)


# Macro to calculate exact duration of generated sequence at a given depth
def generate_sequence_time(sequence_list, depth):
    j = declare(int)
    duration = declare(int)
    assign(duration, 0)  # Ensures duration is reset to 0 for every depth calculated
    with for_(j, 0, j <= depth, j + 1):
        with switch_(sequence_list[j], unsafe=True):
            with case_(0):
                # wait(x180_len // 4, qb)
                assign(duration, duration + x180_len)
            with case_(1):
                # play("x180", qb)
                assign(duration, duration + x180_len)
            with case_(2):
                # play("y180", qb)
                assign(duration, duration + y180_len)
            with case_(3):
                # play("y180", qb)
                # play("x180", qb)
                assign(duration, duration + y180_len + x180_len)
            with case_(4):
                # play("x90", qb)
                # play("y90", qb)
                assign(duration, duration + x90_len + y90_len)
            with case_(5):
                # play("x90", qb)
                # play("-y90", qb)
                assign(duration, duration + x90_len + minus_y90_len)
            with case_(6):
                # play("-x90", qb)
                # play("y90", qb)
                assign(duration, duration + minus_x90_len + y90_len)
            with case_(7):
                # play("-x90", qb)
                # play("-y90", qb)
                assign(duration, duration + minus_x90_len + minus_y90_len)
            with case_(8):
                # play("y90", qb)
                # play("x90", qb)
                assign(duration, duration + y90_len + x90_len)
            with case_(9):
                # play("y90", qb)
                # play("-x90", qb)
                assign(duration, duration + y90_len + minus_x90_len)
            with case_(10):
                # play("-y90", qb)
                # play("x90", qb)
                assign(duration, duration + minus_y90_len + x90_len)
            with case_(11):
                # play("-y90", qb)
                # play("-x90", qb)
                assign(duration, duration + minus_y90_len + minus_x90_len)
            with case_(12):
                # play("x90", qb)
                assign(duration, duration + x90_len)
            with case_(13):
                # play("-x90", qb)
                assign(duration, duration + minus_x90_len)
            with case_(14):
                # play("y90", qb)
                assign(duration, duration + y90_len)
            with case_(15):
                # play("-y90", qb)
                assign(duration, duration + minus_y90_len)
            with case_(16):
                # play("-x90", qb)
                # play("y90", qb)
                # play("x90", qb)
                assign(duration, duration + minus_x90_len + y90_len + x90_len)
            with case_(17):
                # play("-x90", qb)
                # play("-y90", qb)
                # play("x90", qb)
                assign(duration, duration + minus_x90_len + minus_y90_len + x90_len)
            with case_(18):
                # play("x180", qb)
                # play("y90", qb)
                assign(duration, duration + x180_len + y90_len)
            with case_(19):
                # play("x180", qb)
                # play("-y90", qb)
                assign(duration, duration + x180_len + minus_y90_len)
            with case_(20):
                # play("y180", qb)
                # play("x90", qb)
                assign(duration, duration + y180_len + x90_len)
            with case_(21):
                # play("y180", qb)
                # play("-x90", qb)
                assign(duration, duration + y180_len + minus_x90_len)
            with case_(22):
                # play("x90", qb)
                # play("y90", qb)
                # play("x90", qb)
                assign(duration, duration + x90_len + y90_len + x90_len)
            with case_(23):
                # play("-x90", qb)
                # play("y90", qb)
                # play("-x90", qb)
                assign(duration, duration + minus_x90_len + y90_len + minus_x90_len)
    return duration


