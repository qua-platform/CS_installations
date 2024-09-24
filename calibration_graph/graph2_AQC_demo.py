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
            "C:\\Users\\tomdv\\Documents\\QCC_QUAM\\CS_installations\\calibration_graph"
        )
    )

class Parameters(GraphParameters):
    qubits: List[str] = None


g = QualibrationGraph(
    name="AQC_demo",
    parameters=Parameters(),
    nodes={
        "Resonator_spectroscopy": library.nodes["02a_Resonator_Spectroscopy"].copy(name="Resonator_spectroscopy"),
        "Resonator_spectroscopy_vs_flux": library.nodes["02b_Resonator_Spectroscopy_vs_Flux"].copy(name="Resonator_spectroscopy_vs_flux"),
        "Qubit_spectroscopy": library.nodes["03a_Qubit_Spectroscopy"].copy(name="Qubit_spectroscopy"),
        "power_rabi": library.nodes["04a_Power_Rabi"].copy(name="power_rabi"),
        "Ramsey": library.nodes["05_Ramsey"].copy(name="Ramsey"),
        "Readout_freqeuncy_optimization": library.nodes["06a_Readout_Frequency_Optimization"].copy(name="Readout_freqeuncy_optimization"),
        "G_E_discrimination": library.nodes["07a_IQ_Blobs"].copy(name="G_E_discrimination", reset_type_thermal_or_active='thermal'),
        "Power_rabi_error_amplification_x180": library.nodes["08_Power_Rabi_State"].copy(name="Power_rabi_error_amplification_x180", operation_x180_or_any_90 = "x180", reset_type_thermal_or_active = "active"),
        "Power_rabi_error_amplification_x90": library.nodes["08_Power_Rabi_State"].copy(name="Power_rabi_error_amplification_x90", operation_x180_or_any_90 = "x90", reset_type_thermal_or_active = "active"),
        "Ramsey_flux_cal": library.nodes["08a_Ramsey_flux_cal"].copy(name="Ramsey_flux_cal"),
        "Randomized_benchmarking": library.nodes["11a_Randomized_Benchmarking"].copy(name="Randomized_benchmarking", reset_type_thermal_or_active = "active"),
    },
    connectivity=[("Resonator_spectroscopy", "Resonator_spectroscopy_vs_flux"), 
                  ("Resonator_spectroscopy_vs_flux", "Qubit_spectroscopy"), 
                  ("Qubit_spectroscopy", "power_rabi"), 
                  ("power_rabi", "Ramsey"), 
                  ("Ramsey", "Readout_freqeuncy_optimization"), 
                  ("Readout_freqeuncy_optimization", "G_E_discrimination"), 
                  ("G_E_discrimination", "Power_rabi_error_amplification_x180"), 
                  ("G_E_discrimination", "Ramsey_flux_cal"), 
                  ("Power_rabi_error_amplification_x180", "Power_rabi_error_amplification_x90"), 
                  ("Power_rabi_error_amplification_x90", "Randomized_benchmarking")],
    orchestrator=BasicOrchestrator(skip_failed=False),
)

g.run(qubits = ['q1','q2'])

# %%