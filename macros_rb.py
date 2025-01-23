from qm.qua import *
from qualang_tools.bakery.randomized_benchmark_c1 import c1_table

from configuration_with_lffem_csrack import *
# from configuration_with_lffem import *


qubit = "qubit1"
pi_len = QUBIT_CONSTANTS[qubit]["square_pi_len"]

x180_len = pi_len
x90_len = pi_len
minus_x90_len = pi_len
y180_len = pi_len
y90_len = pi_len
minus_y90_len = pi_len

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

map_clifford_to_duration_cycles_list = (np.array([1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 3, 3, 2, 2, 2, 2, 3, 3]) * pi_len // 4).tolist()

map_clifford_numbers_to_string = {
    0: "I",
    1: "X180",
    2: "Y180",
    3: "Y180 X180",
    4: "X90 Y90",
    5: "X90 -Y90",
    6: "-X90 Y90",
    7: "-X90 -Y90",
    8: "Y90 X90",
    9: "Y90 -X90",
    10: "-Y90 X90",
    11: "-Y90 -X90",
    12: "X90",
    13: "-X90",
    14: "Y90",
    15: "-Y90",
    16: "-X90 Y90 X90",
    17: "-X90 -Y90 X90",
    18: "X180 Y90",
    19: "X180 -Y90",
    20: "Y180 X90",
    21: "Y180 -X90",
    22: "X90 Y90 X90",
    23: "-X90 Y90 -X90",
}


def power_law(power, a, b, p):
    return a * (p**power) + b


# def generate_encoded_sequence(N, current_state=0, ends_with_inv_gate=True, num_gates_total_max=0, seed=0):
#     np.random.seed(seed)
#     clifford_arr = np.random.randint(low=0, high=23, size=N).astype(int)
#     state_arr = np.zeros(N).astype(int)
#     inv_gate_arr = np.zeros(N).astype(int)

#     for i, step in enumerate(clifford_arr):
#         next_state = c1_table[current_state, step]
#         state_arr[i] = next_state
#         current_state = next_state
#         inv_gate_arr[i] = inv_gates[current_state]

#     if ends_with_inv_gate:
#         inv_gate = inv_gate_arr[-2]
#         clifford_arr[-1] = inv_gate
#         state_arr[-1] = c1_table[state_arr[-2], inv_gate]

#     clifford_list = clifford_arr.tolist()
#     state_list = state_arr.tolist()
#     inv_gate_list = inv_gate_arr.tolist()

#     num_gates_total = int(np.array([map_clifford_to_num_gates[s] for s in clifford_list]).sum())
#     num_gates_total_rest = num_gates_total_max - num_gates_total
#     duration_rb_total = num_gates_total * pi_len
#     _encoded_circuit = [duration_rb_total] + clifford_list

#     return _encoded_circuit, clifford_list, state_list, inv_gate_list, num_gates_total


def generate_sequence(depth, max_circuit_depth=0, seed=0):
    cayley = declare(int, value=c1_table.flatten().tolist())
    inv_list = declare(int, value=inv_gates)
    current_state = declare(int)
    step = declare(int)
    sequence = declare(int, size=max_circuit_depth + 1)
    # current_states = declare(int, size=max_circuit_depth + 1)
    inv_gate = declare(int)
    i = declare(int)
    rand = Random(seed=seed)

    assign(current_state, 0)
    with for_(i, 0, i < depth, i + 1):
        assign(step, rand.rand_int(24))
        assign(current_state, cayley[current_state * 24 + step])
        assign(sequence[i], step)
        # assign(current_states[i], current_state)
        assign(inv_gate, inv_list[current_state])
        with if_(i == depth - 1):
            assign(sequence[depth], inv_gate)
            # assign(current_states[depth], cayley[current_state * 24 + inv_gate])

    return sequence


# def generate_sequence(depth, max_circuit_depth=0, ends_with_inv_gate=True, seed=0):
#     cayley = declare(int, value=c1_table.flatten().tolist())
#     inv_list = declare(int, value=inv_gates)
#     step = declare(int)
#     sequence = declare(int, size=max_circuit_depth + 1)
#     inv_gate = declare(int)
#     i = declare(int)
#     rand = Random(seed=seed)
#     current_state = declare(int, value=0)

#     with for_(i, 0, i < depth, i + 1):
#         assign(step, rand.rand_int(24))
#         assign(sequence[i], step)
#         assign(current_state, cayley[current_state * 24 + step])

#     if ends_with_inv_gate:
#         assign(inv_gate, inv_list[current_state])
#         assign(sequence[depth], inv_gate)
#     else:
#         assign(step, rand.rand_int(24))
#         assign(current_state, cayley[current_state * 24 + step])
#         assign(sequence[depth], step)

#     return sequence


def play_clifford(c_idx, qb, wf_type="square"):
    with switch_(c_idx, unsafe=True):
        with case_(0):
            play(f"x180_{wf_type}", qb)
        with case_(1):
            play(f"x180_{wf_type}", qb)
        with case_(2):
            play(f"x180_{wf_type}", qb)
        with case_(3):
            play(f"x180_{wf_type}", qb)
            play(f"x180_{wf_type}", qb)
        with case_(4):
            play(f"x180_{wf_type}", qb)
            play(f"x180_{wf_type}", qb)
        with case_(5):
            play(f"x180_{wf_type}", qb)
            play(f"x180_{wf_type}", qb)
        with case_(6):
            play(f"x180_{wf_type}", qb)
            play(f"x180_{wf_type}", qb)
        with case_(7):
            play(f"x180_{wf_type}", qb)
            play(f"x180_{wf_type}", qb)
        with case_(8):
            play(f"x180_{wf_type}", qb)
            play(f"x180_{wf_type}", qb)
        with case_(9):
            play(f"x180_{wf_type}", qb)
            play(f"x180_{wf_type}", qb)
        with case_(10):
            play(f"x180_{wf_type}", qb)
            play(f"x180_{wf_type}", qb)
        with case_(11):
            play(f"x180_{wf_type}", qb)
            play(f"x180_{wf_type}", qb)
        with case_(12):
            play(f"x180_{wf_type}", qb)
        with case_(13):
            play(f"x180_{wf_type}", qb)
        with case_(14):
            play(f"x180_{wf_type}", qb)
        with case_(15):
            play(f"x180_{wf_type}", qb)
        with case_(16):
            play(f"x180_{wf_type}", qb)
            play(f"x180_{wf_type}", qb)
            play(f"x180_{wf_type}", qb)
        with case_(17):
            play(f"x180_{wf_type}", qb)
            play(f"x180_{wf_type}", qb)
            play(f"x180_{wf_type}", qb)
        with case_(18):
            play(f"x180_{wf_type}", qb)
            play(f"x180_{wf_type}", qb)
        with case_(19):
            play(f"x180_{wf_type}", qb)
            play(f"x180_{wf_type}", qb)
        with case_(20):
            play(f"x180_{wf_type}", qb)
            play(f"x180_{wf_type}", qb)
        with case_(21):
            play(f"x180_{wf_type}", qb)
            play(f"x180_{wf_type}", qb)
        with case_(22):
            play(f"x180_{wf_type}", qb)
            play(f"x180_{wf_type}", qb)
            play(f"x180_{wf_type}", qb)
        with case_(23):
            play(f"x180_{wf_type}", qb)
            play(f"x180_{wf_type}", qb)
            play(f"x180_{wf_type}", qb)


def play_sequence_by_section(sequence_list, target, qb, start, end):
    i = declare(int)
    number_of_cliffords = -1 if target < start else (end - start - 1 if target > end else target - start)
    with for_(i, 0, i <= number_of_cliffords, i + 1):
        play_clifford(c_idx=sequence_list[i], qb=qb)


def play_sequence(sequence_list, depth, qb, wf_type="square", i_from=0):
    i = declare(int)
    with for_(i, 0, i <= depth, i + 1):
        # with for_(i, i_from, i <= depth + i_from, i + 1):
        with switch_(sequence_list[i], unsafe=False):
            with case_(0):
                wait(4, qb)  # I
            with case_(1):
                play(f"x180_{wf_type}", qb)
            with case_(2):
                play(f"y180_{wf_type}", qb)
            with case_(3):
                play(f"y180_{wf_type}", qb)
                play(f"x180_{wf_type}", qb)
            with case_(4):
                play(f"x90_{wf_type}", qb)
                play(f"y90_{wf_type}", qb)
            with case_(5):
                play(f"x90_{wf_type}", qb)
                play(f"-y90_{wf_type}", qb)
            with case_(6):
                play(f"-x90_{wf_type}", qb)
                play(f"y90_{wf_type}", qb)
            with case_(7):
                play(f"-x90_{wf_type}", qb)
                play(f"-y90_{wf_type}", qb)
            with case_(8):
                play(f"y90_{wf_type}", qb)
                play(f"x90_{wf_type}", qb)
            with case_(9):
                play(f"y90_{wf_type}", qb)
                play(f"-x90_{wf_type}", qb)
            with case_(10):
                play(f"-y90_{wf_type}", qb)
                play(f"x90_{wf_type}", qb)
            with case_(11):
                play(f"-y90_{wf_type}", qb)
                play(f"-x90_{wf_type}", qb)
            with case_(12):
                play(f"x90_{wf_type}", qb)
            with case_(13):
                play(f"-x90_{wf_type}", qb)
            with case_(14):
                play(f"y90_{wf_type}", qb)
            with case_(15):
                play(f"-y90_{wf_type}", qb)
            with case_(16):
                play(f"-x90_{wf_type}", qb)
                play(f"y90_{wf_type}", qb)
                play(f"x90_{wf_type}", qb)
            with case_(17):
                play(f"-x90_{wf_type}", qb)
                play(f"-y90_{wf_type}", qb)
                play(f"x90_{wf_type}", qb)
            with case_(18):
                play(f"x180_{wf_type}", qb)
                play(f"y90_{wf_type}", qb)
            with case_(19):
                play(f"x180_{wf_type}", qb)
                play(f"-y90_{wf_type}", qb)
            with case_(20):
                play(f"y180_{wf_type}", qb)
                play(f"x90_{wf_type}", qb)
            with case_(21):
                play(f"y180_{wf_type}", qb)
                play(f"-x90_{wf_type}", qb)
            with case_(22):
                play(f"x90_{wf_type}", qb)
                play(f"y90_{wf_type}", qb)
                play(f"x90_{wf_type}", qb)
            with case_(23):
                play(f"-x90_{wf_type}", qb)
                play(f"y90_{wf_type}", qb)
                play(f"-x90_{wf_type}", qb)


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
