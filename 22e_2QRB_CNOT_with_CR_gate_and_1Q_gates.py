# %%
import matplotlib.pyplot as plt
from qm.qua import *
from qm.QuantumMachinesManager import QuantumMachinesManager
from macros import multiplexed_readout
from qualang_tools.bakery.bakery import Baking
from configuration_with_octave import *
from two_qubit_rb import TwoQubitRb


##############################
##  Two-qubit RB functions  ##
##############################
# assign a string to a variable to be able to call them in the functions
q1_idx_str = "1"
q2_idx_str = "2"


# single qubit generic gate constructor Z^{z}Z^{a}X^{x}Z^{-a}
# that can reach any point on the Bloch sphere (starting from arbitrary points)
def bake_phased_xz(baker: Baking, q, x, z, a):
    if q == 1:
        element = f"q{q1_idx_str}_xy"
    else:
        element = f"q{q2_idx_str}_xy"

    baker.frame_rotation_2pi(a / 2, element)
    baker.play("x180", element, amp=x)
    baker.frame_rotation_2pi(-(a + z) / 2, element)
    
    if q == 2:
        # keep track the frame for cr and cr_cancel
        baker.frame_rotation_2pi(-z / 2, "cr_c1t2")
        baker.frame_rotation_2pi(-z / 2, "cr_cancel_c1t2")


# defines the CNOT gate that realizes the mapping |00> -> |00>, |01> -> |01>, |10> -> |11>, |11> -> |10>
def bake_cnot(baker: Baking, q1, q2):
    # Play single qubit gates
    baker.frame_rotation_2pi(+0.25, "q1_xy") # +0.25 for Z(-pi/2) # -z90
    baker.play("-x90", "q2_xy")
    # Shift frames to the calibrated phases
    baker.frame_rotation_2pi(cr_c1t2_drive_phase, "cr_c1t2")
    baker.frame_rotation_2pi(cr_cancel_c1t2_drive_phase, "cr_cancel_c1t2")
    # Play cr drive and cr cancel drive
    baker.align("q1_xy", "q2_xy", "cr_c1t2", "cr_cancel_c1t2")
    baker.align("cr_c1t2", "cr_cancel_c1t2")
    baker.play("square_positive_half", "cr_c1t2")
    baker.play("square_positive_half", "cr_cancel_c1t2")
    # Play echoes for cr drive and cr cancel drive
    baker.align("q1_xy", "cr_c1t2", "cr_cancel_c1t2")
    baker.play("x180", "q1_xy")
    baker.align("cr_c1t2", "cr_cancel_c1t2", "q1_xy")
    baker.play("square_negative_half", "cr_c1t2")
    baker.play("square_negative_half", "cr_cancel_c1t2")
    baker.align("cr_c1t2", "cr_cancel_c1t2", "q1_xy")
    baker.play("x180", "q1_xy")
    # Shift back the phase of cr and cr cancel pulse so they won't be accumulated
    baker.frame_rotation_2pi(-cr_c1t2_drive_phase, "cr_c1t2")
    baker.frame_rotation_2pi(-cr_cancel_c1t2_drive_phase, "cr_cancel_c1t2")


def bake_cz():
    cnot

def prep():
    wait(thermalization_time * u.ns)  # thermal preparation in clock cycles (time = 10 x T1 x 4ns)
    align()


def meas():
    threshold1 = 0.3  # threshold for state discrimination 0 <-> 1 using the I quadrature
    threshold2 = 0.3  # threshold for state discrimination 0 <-> 1 using the I quadrature
    I1 = declare(fixed)
    I2 = declare(fixed)
    Q1 = declare(fixed)
    Q2 = declare(fixed)
    state1 = declare(bool)
    state2 = declare(bool)
    multiplexed_readout(
        [I1, I2], None, [Q1, Q2], None, resonators=[1, 2], weights="rotated_"
    )  # readout macro for multiplexed readout
    assign(state1, I1 > threshold1)  # assume that all information is in I
    assign(state2, I2 > threshold2)  # assume that all information is in I
    return state1, state2


##############################
##  Two-qubit RB execution  ##
##############################
# create RB experiment from configuration and defined functions
rb = TwoQubitRb(
    config=config,
    single_qubit_gate_generator=bake_phased_xz,
    two_qubit_gate_generators={"CNOT": bake_cnot},
    prep_func=prep,
    measure_func=meas,
    interleaving_gate=None,
    verify_generation=False,
)

qmm = QuantumMachinesManager(host=qop_ip, port=qop_port, cluster_name=cluster_name, octave=octave_config) # initialize qmm
res = rb.run(qmm, circuit_depths=[1, 2, 3, 4, 5], num_circuits_per_depth=5, num_shots_per_circuit=100)
# circuit_depths ~ how many consecutive Clifford gates within one executed circuit
# (https://qiskit.org/documentation/apidoc/circuit.html)
# num_circuits_per_depth ~ how many random circuits within one depth
# num_shots_per_circuit ~ repetitions of the same circuit (averaging)

res.plot_hist()
plt.show()

res.plot_fidelity()
plt.show()

# verify/save the random sequences created during the experiment
rb.save_sequences_to_file("sequences.txt")  # saves the gates used in each random sequence
# rb.save_command_mapping_to_file('commands.txt')  # saves mapping from "command id" to sequence
# rb.print_sequences()
# rb.print_command_mapping()
# rb.verify_sequences() # simulates random sequences to ensure they recover to ground state. takes a while...

# %%
