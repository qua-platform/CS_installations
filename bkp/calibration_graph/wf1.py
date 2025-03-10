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
            "/Users/serwan/Repositories/CS_installations/calibration_graph"
        )
    )


class Parameters(GraphParameters):
    qubits: List[str]
    targets_name: str = "qubits"


g = QualibrationGraph(
    name="quick_recal",
    parameters_class=Parameters,
    nodes={
        "IQ_Blobs_thermal": library.nodes["07a_IQ_Blobs"].copy(
            reset_type_thermal_or_active="thermal", name="IQ_Blobs_thermal"
        ),
        "IQ_Blobs_active": library.nodes["07a_IQ_Blobs"].copy(
            reset_type_thermal_or_active="active", name="IQ_Blobs_active"
        ),
        "Ramsey_flux_cal": library.nodes["08a_Ramsey_flux_cal"].copy(
            name="Ramsey_flux_cal"
        ),
    },
    connectivity=[
        ("IQ_Blobs_thermal", "IQ_Blobs_active"),
        ("IQ_Blobs_active", "Ramsey_flux_cal"),
    ],
    orchestrator=BasicOrchestrator(skip_failed=True),
)


g.run(qubits=["q1", "q2", "q3"])
