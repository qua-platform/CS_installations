import matplotlib.pyplot as plt
from qm import (CompilerOptionArguments, QuantumMachinesManager,
                SimulationConfig)
from qm.qua import *
from qualang_tools.addons.variables import assign_variables_to_element
from qualang_tools.bakery.randomized_benchmark_c1 import c1_table
from qualang_tools.plot import interrupt_on_close
from qualang_tools.results import fetching_tool, progress_counter
from scipy.optimize import curve_fit

from configuration_with_lffem import *
from macros_voltage_gate_sequence import VoltageGateSequence

# from configuration_with_lffem_saas import *
# from configuration_with_opxplus import *


qubit = "qubit1"
pi_len = QUBIT_CONSTANTS[qubit]["square_pi_len"]

x180_len = pi_len
x90_len = pi_len // 2
minus_x90_len = pi_len // 2
y180_len = pi_len
y90_len = pi_len
minus_y90_len = pi_len

inv_gates = [int(np.where(c1_table[i, :] == 0)[0][0]) for i in range(24)]

def power_law(power, a, b, p):
    return a * (p**power) + b


def generate_sequence(depth, max_circuit_depth=0, seed=0):
    cayley = declare(int, value=c1_table.flatten().tolist())
    inv_list = declare(int, value=inv_gates)
    step = declare(int)
    sequence = declare(int, size=max_circuit_depth + 1)
    inv_gate = declare(int)
    i = declare(int)
    rand = Random(seed=seed)
    current_state = declare(int, value=0)

    with for_(i, 0, i < depth, i + 1):
        assign(step, rand.rand_int(24))
        assign(sequence[i], step)
        assign(current_state, cayley[current_state * 24 + step])
        assign(inv_gate, inv_list[current_state])
        with if_(i == depth - 1):
            assign(sequence[depth], inv_gate)

    return sequence


def play_sequence(sequence_list, depth, qb, i_from=0):
    i = declare(int)
    with for_(i, 0, i <= depth, i + 1):
    # with for_(i, i_from, i <= depth + i_from, i + 1):
        with switch_(sequence_list[i], unsafe=False):
            with case_(0):
                play("x90_square", qb)
                play("x90_square", qb)
                play("x90_square", qb)
                play("x90_square", qb)
            with case_(1):
                play("x90_square", qb)
                play("x90_square", qb)
            with case_(2):
                play("y90_square", qb)
                play("y90_square", qb)
            with case_(3):
                play("y90_square", qb)
                play("y90_square", qb)
                play("x90_square", qb)
                play("x90_square", qb)
            with case_(4):
                play("x90_square", qb)
                play("y90_square", qb)
            with case_(5):
                play("x90_square", qb)
                play("y90_square", qb)
                play("y90_square", qb)
                play("y90_square", qb)
            with case_(6):
                play("x90_square", qb)
                play("x90_square", qb)
                play("x90_square", qb)
                play("y90_square", qb)
            with case_(7):
                play("x90_square", qb)
                play("x90_square", qb)
                play("x90_square", qb)
                play("y90_square", qb)
                play("y90_square", qb)
                play("y90_square", qb)
            with case_(8):
                play("y90_square", qb)
                play("x90_square", qb)
            with case_(9):
                play("y90_square", qb)
                play("x90_square", qb)
                play("x90_square", qb)
                play("x90_square", qb)
            with case_(10):
                play("y90_square", qb)
                play("y90_square", qb)
                play("y90_square", qb)
                play("x90_square", qb)
            with case_(11):
                play("y90_square", qb)
                play("y90_square", qb)
                play("y90_square", qb)
                play("x90_square", qb)
                play("x90_square", qb)
                play("x90_square", qb)
            with case_(12):
                play("x90_square", qb)
            with case_(13):
                play("x90_square", qb)
                play("x90_square", qb)
                play("x90_square", qb)
            with case_(14):
                play("y90_square", qb)
            with case_(15):
                play("y90_square", qb)
                play("y90_square", qb)
                play("y90_square", qb)
            with case_(16):
                play("x90_square", qb)
                play("x90_square", qb)
                play("x90_square", qb)
                play("y90_square", qb)
                play("x90_square", qb)
            with case_(17):
                play("x90_square", qb)
                play("x90_square", qb)
                play("x90_square", qb)
                play("y90_square", qb)
                play("y90_square", qb)
                play("y90_square", qb)
                play("x90_square", qb)
            with case_(18):
                play("x90_square", qb)
                play("x90_square", qb)
                play("y90_square", qb)
            with case_(19):
                play("x90_square", qb)
                play("x90_square", qb)
                play("y90_square", qb)
                play("y90_square", qb)
                play("y90_square", qb)
            with case_(20):
                play("y90_square", qb)
                play("y90_square", qb)
                play("x90_square", qb)
            with case_(21):
                play("y90_square", qb)
                play("y90_square", qb)
                play("x90_square", qb)
                play("x90_square", qb)
                play("x90_square", qb)
            with case_(22):
                play("x90_square", qb)
                play("y90_square", qb)
                play("x90_square", qb)
            with case_(23):
                play("x90_square", qb)
                play("x90_square", qb)
                play("x90_square", qb)
                play("y90_square", qb)
                play("x90_square", qb)
                play("x90_square", qb)
                play("x90_square", qb)


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
