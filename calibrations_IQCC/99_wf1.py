from pathlib import Path
from typing import List
from qualibrate.orchestration.basic_orchestrator import BasicOrchestrator
from qualibrate.parameters import GraphParameters
from qualibrate.qualibration_graph import QualibrationGraph
from qualibrate.qualibration_library import QualibrationLibrary


library = QualibrationLibrary.get_active_library()


class Parameters(GraphParameters):
    qubits: List[str]
    targets_name: str = "qubits"


g = QualibrationGraph(
    name="single_qubit_tuneup",
    parameters_class=Parameters,
    nodes={
        "qubit_spectroscopy": library.nodes["qubit_spectroscopy"],
        "rabi": library.nodes["rabi"],
        "ramsey": library.nodes["ramsey"],
    },
    connectivity=[("qubit_spectroscopy", "rabi"), ("rabi", "ramsey")],
    orchestrator=BasicOrchestrator(skip_failed=True),
)

g.run(qubits=["q1"])
