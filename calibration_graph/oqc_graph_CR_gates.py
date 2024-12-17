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
    qubits: List[str] = ["q1"]


g = QualibrationGraph(
    name="Independent_2Q_Calibration",
    parameters=Parameters(),
    nodes={
        "IQ_blobs": library.nodes["07b_IQ_Blobs"].copy(name="IQ_blobs"),
        "cr_drive_amplitude": library.nodes["18b_calib_cr_drive_amplitude"].copy(name="cr_drive_amplitude"),


    },
    connectivity=[
        ("IQ_blobs", "cr_drive_amplitude"),
    ],
    orchestrator=BasicOrchestrator(skip_failed=False),
)

# for i in range(1, 9):
#     print(f"\n---------- Measure qubit {i} ----------\n")
#     g.run(qubits=[f"q{i}"])
# g.run(qubits=[f"q{5+1}"])

# Run the graph 4x4
# g.run(qubits=[f"q{2*i+1}" for i in range(0, 4)])
# g.run(qubits=[f"q{2*i+2}" for i in range(0, 4)])

# Run the graph 2x2x2x2
for i in range(1, 5):
    print(f"\n---------- Measure qubits {i} & {4 + i} ----------\n")
    g.run(qubits=[f"q{i}", f"q{4 + i}"])
# %%