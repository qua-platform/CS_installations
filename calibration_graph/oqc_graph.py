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
            r"C:\Users\tomdv\Documents\OQC_QUAM\CS_installations\calibration_graph"
        )
    )

reset_type_thermal_or_active = "active"

class Parameters(GraphParameters):
    qubits: List[str]  = ["q4", "q5", "q6", "q7", "q8"]


g = QualibrationGraph(
    name="OQC_1Q_Calibration",
    parameters=Parameters(),
    nodes={
        "Resonator_spectroscopy": library.nodes["02a_Resonator_Spectroscopy"].copy(name="Resonator_spectroscopy"),
        "Qubit_spectroscopy": library.nodes["03a_Qubit_Spectroscopy"].copy(name="Qubit_spectroscopy"),
        "power_rabi": library.nodes["04_Power_Rabi"].copy(name="power_rabi", min_amp_factor=0.001, max_amp_factor=1.99, max_number_rabi_pulses_per_sweep=1),
        "Ramsey": library.nodes["06_Ramsey"].copy(name="Ramsey"),
        "Readout_frequency_optimization": library.nodes["07a_Readout_Frequency_Optimization"].copy(name="Readout_frequency_optimization"),
        # "Readout_power_optimization": library.nodes["07c_Readout_Power_Optimization"].copy(name="Readout_power_optimization"),
        "IQ_blobs": library.nodes["07b_IQ_Blobs"].copy(name="IQ_blobs"),
        "DRAG_calibration": library.nodes["09b_DRAG_Calibration_180_minus_180"].copy(name="DRAG_calibration", reset_type_thermal_or_active=reset_type_thermal_or_active),        
        "Power_rabi_error_amplification_x180": library.nodes["04_Power_Rabi"].copy(name="power_rabi", operation_x180_or_any_90="x180", reset_type_thermal_or_active=reset_type_thermal_or_active,
                                                                                    min_amp_factor=0.95, max_amp_factor=1.05, max_number_rabi_pulses_per_sweep=200,
                                                                                    state_discrimination=True, amp_factor_step=0.001, num_averages=10),
        "Power_rabi_error_amplification_x90": library.nodes["04_Power_Rabi"].copy(name="power_rabi", operation_x180_or_any_90="x90", reset_type_thermal_or_active=reset_type_thermal_or_active,
                                                                                    min_amp_factor=0.95, max_amp_factor=1.05, max_number_rabi_pulses_per_sweep=200,
                                                                                    state_discrimination=True, amp_factor_step=0.001, num_averages=10), 
        "Randomized_benchmarking_1": library.nodes["10a_Single_Qubit_Randomized_Benchmarking"].copy(name="Randomized_benchmarking", reset_type_thermal_or_active=reset_type_thermal_or_active),

    },
    connectivity=[
        ("Resonator_spectroscopy", "Qubit_spectroscopy"),
        ("Qubit_spectroscopy", "power_rabi"),
        ("power_rabi", "Ramsey"),
        ("Ramsey", "Readout_frequency_optimization"),
        ("Readout_frequency_optimization", "IQ_blobs"),
        ("IQ_blobs", "DRAG_calibration"),
        ("DRAG_calibration", "Power_rabi_error_amplification_x180"),
        ("Power_rabi_error_amplification_x180", "Power_rabi_error_amplification_x90"),
        ("Power_rabi_error_amplification_x90", "Randomized_benchmarking_1")
    ],
    orchestrator=BasicOrchestrator(skip_failed=False),
)

g.run(qubits= ["q4", "q5", "q6", "q7", "q8"])

# %%