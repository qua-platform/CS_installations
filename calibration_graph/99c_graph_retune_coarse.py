
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
            "C:\\Users\\tomdv\\Documents\\QCC_QUAM\\qua-libs\\Quantum-Control-Applications-QuAM\\Superconducting\\calibration_graph"
        )
    )

class Parameters(GraphParameters):
    qubits: List[str] = None

multiplexed = False
flux_point = "joint"
reset_type_thermal_or_active = 'active'


g = QualibrationGraph(
    name="cal_graph",
    parameters=Parameters(),
    nodes={
        "IQ_blobs": library.nodes["07b_IQ_Blobs"].copy(flux_point_joint_or_independent=flux_point, multiplexed=multiplexed, name="IQ_blobs", reset_type_thermal_or_active="thermal"),
        "ramsey_flux_calibration": library.nodes["08_Ramsey_vs_Flux_Calibration"].copy(flux_point_joint_or_independent=flux_point, multiplexed=multiplexed, name="ramsey_flux_calibration"),
        "power_rabi_error_amplification_x180": library.nodes["04_Power_Rabi"].copy(flux_point_joint_or_independent=flux_point, multiplexed=multiplexed, operation = "x180", 
                                                                                   name="power_rabi_error_amplification_x180", reset_type_thermal_or_active=reset_type_thermal_or_active,
                                                                                   min_amp_factor = 0.99, max_amp_factor = 1.01, amp_factor_step = 0.002, max_number_rabi_pulses_per_sweep = 200),
        "power_rabi_error_amplification_x90": library.nodes["04_Power_Rabi"].copy(flux_point_joint_or_independent=flux_point, multiplexed=multiplexed, operation = "x90", 
                                                                                   name="power_rabi_error_amplification_x90", reset_type_thermal_or_active=reset_type_thermal_or_active,
                                                                                   min_amp_factor = 0.99, max_amp_factor = 1.01, amp_factor_step = 0.002, max_number_rabi_pulses_per_sweep = 200),
        "single_qubit_randomized_benchmarking": library.nodes["10a_Single_Qubit_Randomized_Benchmarking"].copy(flux_point_joint_or_independent=flux_point, multiplexed=multiplexed, name="single_qubit_randomized_benchmarking"),
    },
    connectivity=[
                  ("IQ_blobs", "ramsey_flux_calibration"),
                  ("ramsey_flux_calibration", "power_rabi_error_amplification_x180"),
                  ("power_rabi_error_amplification_x180", "power_rabi_error_amplification_x90"),
                  ("power_rabi_error_amplification_x90","single_qubit_randomized_benchmarking"),
                  ],

    orchestrator=BasicOrchestrator(skip_failed=True),
)
# %%

g.run(qubits = ["qubitC1","qubitC2","qubitC3","qubitC4"])
# %%
