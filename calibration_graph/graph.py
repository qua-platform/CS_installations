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
            r"C:\Git\QM-CS-Michal\Customers\QUAlibrate_test\OPX+\calibration_graph"
        )
    )

class Parameters(GraphParameters):
    qubits: List[str] = None


g = QualibrationGraph(
    name="bringup",
    parameters=Parameters(),
    nodes={
        # "Resonator_spectroscopy": library.nodes["02a_Resonator_Spectroscopy"].copy(name="Resonator_spectroscopy", flux_point_joint_or_independent="joint"),
        # "Resonator_spectroscopy_vs_flux": library.nodes["02b_resonator_spectroscopy_vs_flux"].copy(name="Resonator_spectroscopy_vs_flux", flux_point_joint_or_independent="joint"),
        # # "Resonator_spectroscopy_vs_amplitude": library.nodes["02c_resonator_spectroscopy_vs_amplitude"].copy(name="Resonator_spectroscopy_vs_amplitude", flux_point_joint_or_independent="joint"),
        # # "Resonator_spectroscopy_vs_flux_2": library.nodes["02b_Resonator_Spectroscopy_vs_Flux"].copy(name="Resonator_spectroscopy_vs_flux_2", flux_point_joint_or_independent="joint"),
        # "Qubit_spectroscopy": library.nodes["03a_Qubit_Spectroscopy"].copy(name="Qubit_spectroscopy", flux_point_joint_or_independent="joint"),
        # "Qubit_spectroscopy_vs_flux": library.nodes["03b_Qubit_Spectroscopy_vs_Flux"].copy(name="Qubit_spectroscopy_vs_flux", flux_point_joint_or_independent="joint"),
        # "Power_rabi": library.nodes["04_Power_Rabi"].copy(name="Power_rabi", flux_point_joint_or_independent="joint"),
        # "Ramsey": library.nodes["05_Ramsey"].copy(name="Ramsey", flux_point_joint_or_independent="independent"),
        # "Readout_Frequency_Optimization": library.nodes["06a_Readout_Frequency_Optimization"].copy(name="Readout_Frequency_Optimization", flux_point_joint_or_independent="joint"),
        # "Readout_Power_Optimization": library.nodes["06b_Readout_Power_Optimization"].copy(name="Readout_Power_Optimization", flux_point_joint_or_independent="joint"),
        # "IQ_blobs": library.nodes["07_IQ_Blobs"].copy(name="IQ_blobs", flux_point_joint_or_independent="joint"),
        # "Qubit_Spectroscopy_E_to_F": library.nodes["08a_Qubit_Spectroscopy_E_to_F"].copy(name="Qubit_Spectroscopy_E_to_F", flux_point_joint_or_independent="joint"),
        # "Power_Rabi_E_to_F": library.nodes["08b_Power_Rabi_E_to_F"].copy(name="Power_Rabi_E_to_F", flux_point_joint_or_independent="joint"),
        # "Readout_Frequency_Optimization_G_E_F": library.nodes["08c_Readout_Frequency_Optimization_G_E_F"].copy(name="Readout_Frequency_Optimization_G_E_F", flux_point_joint_or_independent="joint"),
        # "IQ_Blobs_G_E_F": library.nodes["08d_IQ_Blobs_G_E_F"].copy(name="IQ_Blobs_G_E_F", flux_point_joint_or_independent="joint"),
        # "Power_Rabi_State": library.nodes["09_Power_Rabi_State"].copy(name="Power_Rabi_State", flux_point_joint_or_independent="joint"),
        # "DRAG_Calibration_180_minus_180": library.nodes["09b_DRAG_Calibration_180_minus_180"].copy(name="DRAG_Calibration_180_minus_180", flux_point_joint_or_independent="joint"),
        "Ramsey_flux_cal": library.nodes["10_Ramsey_flux_cal"].copy(name="Ramsey_flux_cal", flux_point_joint_or_independent="joint"),
        "T1": library.nodes["11_t1"].copy(name="T1", flux_point_joint_or_independent="joint"),
        "T2Echo": library.nodes["12_t2echo"].copy(name="T2Echo", flux_point_joint_or_independent="joint"),
        "single_qubit_RB": library.nodes["14_single_qubit_RB"].copy(name="single_qubit_RB", flux_point_joint_or_independent="joint"),
    },
    connectivity=[
        # ("Resonator_spectroscopy", "Resonator_spectroscopy_vs_flux"),
        # ("Resonator_spectroscopy_vs_flux", "Qubit_spectroscopy"),
        # ("Qubit_spectroscopy", "Qubit_spectroscopy_vs_flux"),
        # ("Qubit_spectroscopy_vs_flux", "Power_rabi"),
        # ("Power_rabi", "Ramsey"),
        # ("Ramsey", "Readout_Frequency_Optimization"),
        # ("Readout_Frequency_Optimization", "Readout_Power_Optimization"),
        # ("Readout_Power_Optimization", "IQ_blobs"),
        # ("IQ_blobs", "Qubit_Spectroscopy_E_to_F"),
        # ("Qubit_Spectroscopy_E_to_F", "Power_Rabi_E_to_F"),
        # ("Power_Rabi_E_to_F", "Readout_Frequency_Optimization_G_E_F"),
        # ("Readout_Frequency_Optimization_G_E_F", "IQ_Blobs_G_E_F"),
        # ("IQ_Blobs_G_E_F", "Power_Rabi_State"),
        # ("Power_Rabi_State", "DRAG_Calibration_180_minus_180"),
        # ("DRAG_Calibration_180_minus_180", "Ramsey_flux_cal"),
        ("Ramsey_flux_cal", "T1"),
        ("T1", "T2Echo"),
        ("T2Echo", "single_qubit_RB"),
    ],
    orchestrator=BasicOrchestrator(skip_failed=False),
)

g.run(qubits=['q1', 'q2'])

# %%