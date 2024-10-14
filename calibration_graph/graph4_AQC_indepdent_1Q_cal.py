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
    name="Independent_1Q_Calibration",
    parameters=Parameters(),
    nodes={
        # "Resonator_spectroscopy": library.nodes["02a_Resonator_Spectroscopy"].copy(name="Resonator_spectroscopy", flux_point_joint_or_independent="independent"),
        # "Resonator_spectroscopy_vs_flux": library.nodes["02b_Resonator_Spectroscopy_vs_Flux"].copy(name="Resonator_spectroscopy_vs_flux", flux_point_joint_or_independent="independent"),
        # # "Resonator_spectroscopy_vs_amplitude": library.nodes["02c_Resonator_Spectroscopy_vs_Amplitude"].copy(name="resonator_spectroscopy_vs_amplitude", flux_point_joint_or_independent="independent"),
        # "Resonator_spectroscopy_vs_flux_2": library.nodes["02b_Resonator_Spectroscopy_vs_Flux"].copy(name="Resonator_spectroscopy_vs_flux_2", flux_point_joint_or_independent="independent"),
        # "Qubit_spectroscopy": library.nodes["03a_Qubit_Spectroscopy"].copy(name="Qubit_spectroscopy", flux_point_joint_or_independent="independent"),
        # "Qubit_spectroscopy_vs_flux": library.nodes["03b_Qubit_Spectroscopy_vs_Flux"].copy(name="Qubit_spectroscopy_vs_flux", flux_point_joint_or_independent="independent"),
        "power_rabi": library.nodes["04_Power_Rabi"].copy(name="power_rabi", flux_point_joint_or_independent="independent"),
        "Ramsey": library.nodes["05_Ramsey"].copy(name="Ramsey", flux_point_joint_or_independent="independent"),
        "Readout_freqeuncy_optimization": library.nodes["06a_Readout_Frequency_Optimization"].copy(name="Readout_freqeuncy_optimization", flux_point_joint_or_independent="independent"),
        "G_E_discrimination": library.nodes["07_IQ_Blobs"].copy(name="G_E_discrimination", reset_type_thermal_or_active='thermal', flux_point_joint_or_independent="independent"),
        "Power_rabi_error_amplification_x180": library.nodes["09_Power_Rabi_State"].copy(name="Power_rabi_error_amplification_x180", operation_x180_or_any_90 = "x180", reset_type_thermal_or_active = "active", flux_point_joint_or_independent="independent"),
        "Power_rabi_error_amplification_x90": library.nodes["09_Power_Rabi_State"].copy(name="Power_rabi_error_amplification_x90", operation_x180_or_any_90 = "x90", reset_type_thermal_or_active = "active", flux_point_joint_or_independent="independent"),
        "Stark_detuning": library.nodes["09a_Stark_Detuning"].copy(name="Stark_detuning", flux_point_joint_or_independent="independent"),
        "DRAG_calibration": library.nodes["09b_DRAG_Calibration_180_minus_180"].copy(name="DRAG_calibration", flux_point_joint_or_independent="independent"),
        "Ramsey_flux_cal": library.nodes["09d_Ramsey_flux_cal"].copy(name="Ramsey_flux_cal", flux_point_joint_or_independent="independent"),
        "Ramsey_flux_cal_2": library.nodes["09d_Ramsey_flux_cal"].copy(name="Ramsey_flux_cal_2", flux_point_joint_or_independent="independent"),
        "Randomized_benchmarking": library.nodes["11a_Randomized_Benchmarking"].copy(name="Randomized_benchmarking", reset_type_thermal_or_active = "active", flux_point_joint_or_independent="independent"),
    
    },
    connectivity=[
        # ("Resonator_spectroscopy", "Resonator_spectroscopy_vs_flux"), 
        #           ("Resonator_spectroscopy_vs_flux", "Resonator_spectroscopy_vs_flux_2"),
        #           ("Resonator_spectroscopy_vs_flux_2", "Qubit_spectroscopy"), 
        #           ("Qubit_spectroscopy", "Qubit_spectroscopy_vs_flux"),
        #           ("Qubit_spectroscopy_vs_flux", "power_rabi"),
                  ("power_rabi", "Ramsey"), 
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
                  ("DRAG_calibration", "Randomized_benchmarking")
],
    orchestrator=BasicOrchestrator(skip_failed=False),
)

g.run()

# %%