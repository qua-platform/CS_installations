# %%
from pathlib import Path
from typing import List
from qualibrate.orchestration.basic_orchestrator import BasicOrchestrator
from qualibrate.parameters import GraphParameters
from qualibrate.qualibration_graph import QualibrationGraph
from qualibrate.qualibration_library import QualibrationLibrary

library = QualibrationLibrary.active_library
if library is None:
    library = QualibrationLibrary(
        library_folder=Path(
            "C:\\git\\CS_installations\\calibration_graph"
        )
    )


class Parameters(GraphParameters):
    qubits: List[str] = ["q3", "q4"]

class Parameters_2q(GraphParameters):
    qubit_pairs: List[str] = ["q3-4"]


g1q = QualibrationGraph(
    name="Joint_Readout_Calibration",
    parameters=Parameters(),
    nodes={
        "Readout_frequency_optimization": library.nodes["07a_Readout_Frequency_Optimization"].copy(name="Readout_frequency_optimization", multiplexed=True),
        "Readout_power_optimization": library.nodes["07c_Readout_Power_Optimization"].copy(name="Readout_power_optimization", multiplexed=True),
        "IQ_blobs": library.nodes["07b_IQ_Blobs"].copy(name="IQ_blobs", multiplexed=True),
    },
    connectivity=[
        ("Readout_frequency_optimization", "Readout_power_optimization"),
        ("Readout_power_optimization", "IQ_blobs"),
    ],
    orchestrator=BasicOrchestrator(skip_failed=False),
)

g2q = QualibrationGraph(
    name="CNOT_Calibration",
    parameters=Parameters_2q(),
    nodes={
        "CR_drive_phase": library.nodes["18c_CR_calib_cr_drive_phase_quick"].copy(name="CR_drive_phase", qubit_pairs=Parameters_2q().qubit_pairs),
        "2Q_Confusion_Matrix": library.nodes["19_2Q_Confusion_Matrix"].copy(name="2Q_Confusion_Matrix", qubit_pairs=Parameters_2q().qubit_pairs),
        "State_Tomography": library.nodes["20_Multi_Gates_Tomography_Zbasis"].copy(name="State_Tomography", qubit_pairs=Parameters_2q().qubit_pairs),
        "Bell_State_Tomography": library.nodes["20_Bell_State_Tomography"].copy(name="Bell_State_Tomography", qubit_pairs=Parameters_2q().qubit_pairs),
    },
    connectivity=[
        ("2Q_Confusion_Matrix", "CR_drive_phase"),
        ("CR_drive_phase", "State_Tomography"),
        ("State_Tomography", "Bell_State_Tomography"),
    ],
    orchestrator=BasicOrchestrator(skip_failed=False),
)

# for i in range(1, 9):
#     print(f"\n---------- Measure qubit {i} ----------\n")
#     g.run(qubits=[f"q{i}"])
qu_pairs = ["q1-2", "q2-3", "q3-4", "q5-4", "q5-6", "q7-6", "q7-8"]
qu_pairs = ["q3-4", "q5-4", "q5-6", "q7-6", "q7-8"]
for i in range(0,7):
    qp = qu_pairs[i]
    qc = f"q{qu_pairs[i][1]}"
    qt = f"q{qu_pairs[i][-1]}"
    g1q.run(qubits=[qc, qt])
    g2q = QualibrationGraph(
        name="CNOT_Calibration",
        parameters=Parameters_2q(),
        nodes={
            "CR_drive_phase": library.nodes["18c_CR_calib_cr_drive_phase_quick"].copy(name="CR_drive_phase",
                                                                                      qubit_pairs=[qp]),
            "2Q_Confusion_Matrix": library.nodes["19_2Q_Confusion_Matrix"].copy(name="2Q_Confusion_Matrix",
                                                                                qubit_pairs=[qp]),
            "State_Tomography": library.nodes["20_Multi_Gates_Tomography_Zbasis"].copy(name="State_Tomography",
                                                                                       qubit_pairs=[qp]),
            "Bell_State_Tomography": library.nodes["20_Bell_State_Tomography"].copy(name="Bell_State_Tomography",
                                                                                    qubit_pairs=[qp]),
        },
        connectivity=[
            ("2Q_Confusion_Matrix", "CR_drive_phase"),
            ("CR_drive_phase", "State_Tomography"),
            ("State_Tomography", "Bell_State_Tomography"),
        ],
        orchestrator=BasicOrchestrator(skip_failed=False),
    )
    g2q.run(qubit_pairs=[qp])

# g2q.run(qubit_pairs=["q1-2"])
# g.run(qubits=["q4"])

# Run the graph 4x4
# g.run(qubits=[f"q{2*i+1}" for i in range(0, 4)])
# g.run(qubits=[f"q{2*i+2}" for i in range(0, 4)])

# Run the graph 2x2x2x2
# for i in range(1, 5):
#     print(f"\n---------- Measure qubits {i} & {4 + i} ----------\n")
#     g.run(qubits=[f"q{i}", f"q{4 + i}"])
# %%