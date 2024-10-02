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
    qubits: List[str] = None


g = QualibrationGraph(
    name="Demo_bringup",
    parameters=Parameters(),
    nodes={
        "Resonator_spectroscopy": library.nodes["02a_Resonator_Spectroscopy"].copy(name="Resonator_spectroscopy", flux_point_joint_or_independent="joint"),
        "Resonator_spectroscopy_vs_flux": library.nodes["02b_Resonator_Spectroscopy_vs_Flux"].copy(name="Resonator_spectroscopy_vs_flux", flux_point_joint_or_independent="joint"),
        "Resonator_spectroscopy_vs_amplitude": library.nodes["02c_Resonator_Spectroscopy_vs_Amplitude"].copy(name="resonator_spectroscopy_vs_amplitude", flux_point_joint_or_independent="joint"),
        "Resonator_spectroscopy_vs_flux_2": library.nodes["02b_Resonator_Spectroscopy_vs_Flux"].copy(name="Resonator_spectroscopy_vs_flux_2", flux_point_joint_or_independent="joint"),
        "Qubit_spectroscopy": library.nodes["03a_Qubit_Spectroscopy"].copy(name="Qubit_spectroscopy", flux_point_joint_or_independent="joint"),
        "Qubit_spectroscopy_vs_flux": library.nodes["03b_Qubit_Spectroscopy_vs_Flux"].copy(name="Qubit_spectroscopy_vs_flux", flux_point_joint_or_independent="joint"),
    },
    connectivity=[("Resonator_spectroscopy", "Resonator_spectroscopy_vs_flux"), 
                  ("Resonator_spectroscopy_vs_flux", "Resonator_spectroscopy_vs_amplitude"),
                  ("Resonator_spectroscopy_vs_amplitude", "Resonator_spectroscopy_vs_flux_2"),
                  ("Resonator_spectroscopy_vs_flux_2", "Qubit_spectroscopy"), 
                  ("Qubit_spectroscopy", "Qubit_spectroscopy_vs_flux"),
],
    orchestrator=BasicOrchestrator(skip_failed=False),
)

g.run(qubits = ['q4','q5'])

# %%