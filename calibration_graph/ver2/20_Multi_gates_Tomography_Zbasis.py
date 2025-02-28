# %%
"""
Two-Qubit Readout Confusion Matrix Measurement

This sequence measures the readout error when simultaneously measuring the state of two qubits. The process involves:

1. Preparing the two qubits in all possible combinations of computational basis states (|00⟩, |01⟩, |10⟩, |11⟩)
2. Performing simultaneous readout on both qubits
3. Calculating the confusion matrix based on the measurement results

For each prepared state, we measure:
1. The readout result of the first qubit
2. The readout result of the second qubit

The measurement process involves:
1. Initializing both qubits to the ground state
2. Applying single-qubit gates to prepare the desired input state
3. Performing simultaneous readout on both qubits
4. Repeating the process multiple times to gather statistics

The outcome of this measurement will be used to:
1. Quantify the readout fidelity for two-qubit states
2. Identify and characterize crosstalk effects in the readout process
3. Provide data for readout error mitigation in two-qubit experiments

Prerequisites:
- Calibrated single-qubit gates for both qubits in the pair
- Calibrated readout for both qubits

Outcomes:
- 4x4 confusion matrix representing the probabilities of measuring each two-qubit state given a prepared input state
- Readout fidelity metrics for simultaneous two-qubit measurement
"""

# %% {Imports}
from qualibrate import QualibrationNode, NodeParameters
from quam_libs.components import QuAM
from quam_libs.macros import active_reset, readout_state
from quam_libs.lib.plot_utils import QubitPairGrid, grid_iter, grid_pair_names
from quam_libs.lib.save_utils import fetch_results_as_xarray, load_dataset
from qualang_tools.results import progress_counter, fetching_tool
from qualang_tools.loops import from_array
from qualang_tools.multi_user import qm_session
from qualang_tools.units import unit
from qm import SimulationConfig
from qm.qua import *
from typing import Literal, Optional, List
import matplotlib.pyplot as plt
import numpy as np
from quam_libs.lib.plot_utils import QubitGrid, grid_iter



# %% {Node_parameters}
class Parameters(NodeParameters):
    qubit_pairs: Optional[List[str]] = ['q3-4']
    qubits: Optional[List[str]] = []
    num_shots: int = 2000
    flux_point_joint_or_independent: Literal["joint", "independent", None] = None
    reset_type: Literal['active', 'thermal'] = "thermal"
    simulate: bool = False
    timeout: int = 100
    load_data_id: Optional[int] = None


node = QualibrationNode(
    name="20_Multi_Gates_Tomography_Zbasis", parameters=Parameters()
)
assert not (
            node.parameters.simulate and node.parameters.load_data_id is not None), "If simulate is True, load_data_id must be None, and vice versa."

# %% {Initialize_QuAM_and_QOP}
# Class containing tools to help handling units and conversions.
u = unit(coerce_to_integer=True)
# Instantiate the QuAM class from the state file
machine = QuAM.load()

# Get the relevant QuAM components
if node.parameters.qubit_pairs is None or node.parameters.qubit_pairs == "":
    qubit_pairs = machine.active_qubit_pairs
else:
    qubit_pairs = [machine.qubit_pairs[qp] for qp in node.parameters.qubit_pairs]

num_qubit_pairs = len(qubit_pairs)

# Generate the OPX and Octave configurations
config = machine.generate_config()
octave_config = machine.get_octave_config()
# Open Communication with the QOP
if node.parameters.load_data_id is None:
    qmm = machine.connect()
# %%

####################
# Helper functions #
####################

def CNOT(cr, qt, qc):
    # CNOT with CR gate --> https://arxiv.org/pdf/1904.06560 &
    # https://quantum-machines.atlassian.net/wiki/spaces/CST/pages/2814640137/Notes+on+Cross+Resonance+and+Hamiltonian+Tomography
    # control: -- Z/2 -- CR(-pi/2) ---
    # target : -- X/2 ----------------

    cr.frame_rotation_2pi(0.5)  # To play CR -pi/2
    qc.xy.frame_rotation_2pi(0.25)  # Z/2
    qt.xy.play("x90")  # X/2
    # direct + cancel
    align(qc.xy.name, cr.name, qt.xy.name)
    cr.play("square", amplitude_scale=1)
    # pi pulse on control
    align(qc.xy.name, cr.name)
    qc.xy.play("x180")
    # echoed direct + cancel
    align(qc.xy.name, cr.name)
    cr.play("square", amplitude_scale=-1)
    # pi pulse on control
    align(qc.xy.name, cr.name)
    qc.xy.play("x180")
    # align for the next step and clear the phase shift
    align(qc.xy.name, qt.xy.name)


# %% {QUA_program}
n_shots = node.parameters.num_shots  # The number of averages
N_gates = 12
flux_point = node.parameters.flux_point_joint_or_independent  # 'independent' or 'joint'

with program() as CPhase_Oscillations:
    n = declare(int)
    k = declare(int)
    n_st = declare_stream()
    state_control = [declare(int) for _ in range(num_qubit_pairs)]
    state_target = [declare(int) for _ in range(num_qubit_pairs)]
    state = [declare(int) for _ in range(num_qubit_pairs)]
    state_st_control = [declare_stream() for _ in range(num_qubit_pairs)]
    state_st_target = [declare_stream() for _ in range(num_qubit_pairs)]
    state_st = [declare_stream() for _ in range(num_qubit_pairs)]
    tomo_axis_control = declare(int)
    tomo_axis_target = declare(int)

    for i, qp in enumerate(qubit_pairs):
        qc = qp.qubit_control
        qt = qp.qubit_target
        with for_(k, 0, k<N_gates, k+1):
            with for_(n, 0, n < n_shots, n + 1):
                save(n, n_st)
                # reset
                if node.parameters.reset_type == "active":
                    active_reset(qc)
                    active_reset(qt)
                    qp.align()
                else:
                    qp.wait(machine.thermalization_time * u.ns)

                qp.align()
                with switch_(k):
                    with case_(0):  # I-I
                        qc.xy.wait(qc.xy.operations["x180"].length * u.ns)
                        qt.xy.wait(qt.xy.operations["x180"].length * u.ns)
                    with case_(1):  # I-X
                        qc.xy.wait(qc.xy.operations["x180"].length * u.ns)
                        qt.xy.play("x180")
                    with case_(2):  # X-I
                        qc.xy.play("x180")
                        qt.xy.wait(qt.xy.operations["x180"].length * u.ns)
                    with case_(3):  # X-X
                        qc.xy.play("x180")
                        qt.xy.play("x180")
                    with case_(4):  # I-X/2
                        qc.xy.wait(qc.xy.operations["x180"].length * u.ns)
                        qt.xy.play("x90")
                    with case_(5):  # X/2-I
                        qc.xy.play("x90")
                        qt.xy.wait(qt.xy.operations["x180"].length * u.ns)
                    with case_(6):  # X/2-X/2
                        qc.xy.play("x90")
                        qt.xy.play("x90")
                    with case_(7):  # (I-I)-CNOT
                        CNOT(qp.cross_resonance, qt, qc)
                    with case_(8):  # (X-I)-CNOT
                        qc.xy.play("x180")
                        CNOT(qp.cross_resonance, qt, qc)
                    with case_(9):  # (X/2-I)-CNOT
                        qc.xy.play("x90")
                        CNOT(qp.cross_resonance, qt, qc)
                    with case_(10):  # (H-I)-CNOT (XY)
                        qc.xy.play("y90")
                        qc.xy.play("x180")
                        CNOT(qp.cross_resonance, qt, qc)
                    with case_(11):  # (H-I)-CNOT  (Z)
                        qc.xy.frame_rotation_2pi(0.25)
                        qc.xy.play("x90")
                        qc.xy.frame_rotation_2pi(0.25)
                        CNOT(qp.cross_resonance, qt, qc)

                qp.align()

                # readout
                readout_state(qp.qubit_control, state_control[i])
                readout_state(qp.qubit_target, state_target[i])
                assign(state[i], state_control[i] * 2 + state_target[i])
                save(state_control[i], state_st_control[i])
                save(state_target[i], state_st_target[i])
                save(state[i], state_st[i])
                reset_frame(qp.qubit_control.xy.name)
                reset_frame(qp.cross_resonance.name)
        align()

    with stream_processing():
        n_st.save("n")
        for i in range(num_qubit_pairs):
            state_st_control[i].buffer(n_shots).buffer(N_gates).save(f"state_control{i + 1}")
            state_st_target[i].buffer(n_shots).buffer(N_gates).save(f"state_target{i + 1}")
            state_st[i].buffer(n_shots).buffer(N_gates).save(f"state{i + 1}")

# %% {Simulate_or_execute}
if node.parameters.simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=10_000)  # In clock cycles = 4ns
    job = qmm.simulate(config, CPhase_Oscillations, simulation_config)
    job.get_simulated_samples().con1.plot()
    node.results = {"figure": plt.gcf()}
    node.machine = machine
    node.save()
elif node.parameters.load_data_id is None:
    with qm_session(qmm, config, timeout=node.parameters.timeout) as qm:
        job = qm.execute(CPhase_Oscillations)

        results = fetching_tool(job, ["n"], mode="live")
        while results.is_processing():
            # Fetch results
            n = results.fetch_all()[0]
            # Progress bar
            progress_counter(n, n_shots, start_time=results.start_time)

# %% {Data_fetching_and_dataset_creation}
if not node.parameters.simulate:
    if node.parameters.load_data_id is None:
        # Fetch the data from the OPX and convert it into a xarray with corresponding axes (from most inner to outer loop)
        ds = fetch_results_as_xarray(job.result_handles, qubit_pairs, {"N": np.linspace(1, n_shots, n_shots), "gate_nb": np.arange(0, N_gates, 1)})
    else:
        ds, machine = load_dataset(node.parameters.load_data_id)

    node.results = {"ds": ds}

# %%
gate_names = ["I @ I", "I @ X", "X @ I", "X @ X", "I @ X/2", "X/2 @ I", "X/2 @ X/2", "(I @ I), CNOT", "(X @ I), CNOT", "(X/2 @ I), CNOT", "(H1 @ I), CNOT", "(H2 @ I), CNOT"]
expectations = [[1, 0, 0, 0],
                [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1],
                [0.5, 0.5, 0, 0], [0.5, 0, 0.5, 0], [0.25, 0.25, 0.25, 0.25],
                [1, 0, 0, 0], [0, 0, 0, 1], [0.5, 0, 0, 0.5],
                [0.5, 0, 0, 0.5], [0.5, 0, 0, 0.5]]
if not node.parameters.simulate:
    states = [0, 1, 2, 3]

    results = {}
    corrected_results = {}
    for qp in qubit_pairs:
        results[qp.name] = {}
        corrected_results[qp.name] = {}
        state2 = (ds.state_control * 2 + ds.state_target)
        for i, gate in enumerate(gate_names):
            results[qp.name][gate] = []
            for state in states:
                results[qp.name][gate].append((state2.sel(gate_nb=i) == state).sum().values)
            results[qp.name][gate] = np.array(results[qp.name][gate]) / node.parameters.num_shots

            conf_mat = qp.confusion
            corrected_res = np.linalg.inv(conf_mat) @ results[qp.name][gate]
            corrected_res = corrected_res * (corrected_res > 0)
            corrected_res = corrected_res / corrected_res.sum()
            corrected_results[qp.name][gate] = corrected_res
            print(f"{qp.name}: {corrected_results[qp.name][gate]}")

# %%
if not node.parameters.simulate:
    fig, ax = plt.subplots(3,4,figsize=(15,7))
    plt.suptitle(f"Quantum State Tomography for {qp.name} - with readout error correction")
    for i, gate in enumerate(gate_names):
        corrected_res = corrected_results[qp.name][gate]
        ax[int(i/4), i%4].bar(['00', '01', '10', '11'], corrected_res, color='red', edgecolor='red')
        ax[int(i/4), i%4].set_ylim(0, 1.1)
        for j, v in enumerate(corrected_res):
            ax[int(i/4), i%4].text(j, v, f'{v:.2f}', ha='center', va='bottom')
            ax[int(i / 4), i % 4].bar(['00', '01', '10', '11'], expectations[i], color='skyblue', edgecolor='navy', alpha=0.2)

        ax[int(i/4), i%4].set_title(gate)
    ax[1, 0].set_ylabel("State Probability")
    ax[2, 1].set_xlabel("Qubit Basis |qc, qt>")
    ax[2, 2].set_xlabel("Qubit Basis |qc, qt>")
    plt.tight_layout()
    plt.show()
    node.results["figure_state_tomo_corr"] = fig

    fig, ax = plt.subplots(3, 4, figsize=(15, 7))
    plt.suptitle(f"Quantum State Tomography for {qp.name} - without readout error correction")
    for i, gate in enumerate(gate_names):
        corrected_res = results[qp.name][gate]
        ax[int(i / 4), i % 4].bar(['00', '01', '10', '11'], corrected_res, color='red', edgecolor='red')
        ax[int(i / 4), i % 4].set_ylim(0, 1.1)
        for j, v in enumerate(corrected_res):
            ax[int(i / 4), i % 4].text(j, v, f'{v:.2f}', ha='center', va='bottom')
            ax[int(i / 4), i % 4].bar(['00', '01', '10', '11'], expectations[i], color='skyblue', edgecolor='navy',
                                      alpha=0.2)

        ax[int(i / 4), i % 4].set_title(gate)
    ax[1, 0].set_ylabel("State Probability")
    ax[2, 1].set_xlabel("Qubit Basis |qc, qt>")
    ax[2, 2].set_xlabel("Qubit Basis |qc, qt>")
    plt.tight_layout()
    plt.show()
    node.results["figure_state_tomo"] = fig
# %%

# %% {Update_state}

# %% {Save_results}
if not node.parameters.simulate:
    node.outcomes = {qp.name: "successful" for qp in qubit_pairs}
    node.results["initial_parameters"] = node.parameters.model_dump()
    node.machine = machine
    node.save()

