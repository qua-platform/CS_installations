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
    name="AQC_calibration",
    parameters=Parameters(),
    nodes={
        "power_rabi": library.nodes["04a_Power_Rabi"].copy(name="power_rabi"),
        "Ramsey": library.nodes["05_Ramsey"].copy(name="Ramsey"),
        "Readout_freqeuncy_optimization": library.nodes["06a_Readout_Frequency_Optimization"].copy(name="Readout_freqeuncy_optimization"),
        # "readout_power_optimization": library.nodes["07b_readout_power_optimization"].copy(name="readout_power_optimization"),
        "G_E_discrimination": library.nodes["07a_IQ_Blobs"].copy(name="G_E_discrimination", reset_type_thermal_or_active='thermal'),
        "Power_rabi_error_amplification_x180": library.nodes["08_Power_Rabi_State"].copy(name="Power_rabi_error_amplification_x180", operation_x180_or_any_90 = "x180", reset_type_thermal_or_active = "active"),
        "Power_rabi_error_amplification_x90": library.nodes["08_Power_Rabi_State"].copy(name="Power_rabi_error_amplification_x90", operation_x180_or_any_90 = "x90", reset_type_thermal_or_active = "active"),
        "Stark_detuning": library.nodes["09_Stark_Detuning"].copy(name="Stark_detuning"),
        "DRAG_calibration": library.nodes["10a_DRAG_Calibration_180_minus_180"].copy(name="DRAG_calibration"),
        "Ramsey_flux_cal": library.nodes["08a_Ramsey_flux_cal"].copy(name="Ramsey_flux_cal"),
        "Ramsey_flux_cal_2": library.nodes["08a_Ramsey_flux_cal"].copy(name="Ramsey_flux_cal_2"),
        "Randomized_benchmarking": library.nodes["11a_Randomized_Benchmarking"].copy(name="Randomized_benchmarking", reset_type_thermal_or_active = "active"),
    },
    connectivity=[("power_rabi", "Ramsey"), 
                  ("Ramsey", "Readout_freqeuncy_optimization"), 
                  ("Readout_freqeuncy_optimization", "G_E_discrimination"), 
                  ("G_E_discrimination", "Power_rabi_error_amplification_x180"), 
                  ("Power_rabi_error_amplification_x180", "Power_rabi_error_amplification_x90"), 
                  ("Power_rabi_error_amplification_x90", "Randomized_benchmarking"),
                  ("G_E_discrimination", "Ramsey_flux_cal"), 
                  ("Ramsey_flux_cal", "Ramsey_flux_cal_2"),
                  ("Ramsey_flux_cal_2", "Randomized_benchmarking"),
                  ("G_E_discrimination", "Stark_detuning"),
                  ("Stark_detuning", "DRAG_calibration"),
                  ("DRAG_calibration", "Randomized_benchmarking"),
],
    orchestrator=BasicOrchestrator(skip_failed=False),
)

g.run(qubits = ['q1','q2'])

# %%