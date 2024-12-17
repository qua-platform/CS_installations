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
    name="Independent_1Q_Calibration_fine_nostark",
    parameters=Parameters(),
    nodes={
        # "Resonator_spectroscopy": library.nodes["02a_Resonator_Spectroscopy"].copy(name="Resonator_spectroscopy"),
        # "Qubit_spectroscopy": library.nodes["03a_Qubit_Spectroscopy"].copy(name="Qubit_spectroscopy"),
        "T1": library.nodes["05_T1"].copy(name="T1"),
        # "power_rabi": library.nodes["04_Power_Rabi"].copy(name="power_rabi", min_amp_factor=0.001, max_amp_factor=1.99, max_number_rabi_pulses_per_sweep=1),
        "Readout_frequency_optimization": library.nodes["07a_Readout_Frequency_Optimization"].copy(name="Readout_frequency_optimization"),
        "Readout_power_optimization": library.nodes["07c_Readout_Power_Optimization"].copy(name="Readout_power_optimization"),
        "IQ_blobs": library.nodes["07b_IQ_Blobs"].copy(name="IQ_blobs"),
        "Power_rabi_error_amplification_x180": library.nodes["04_Power_Rabi"].copy(name="power_rabi", operation_x180_or_any_90="x180"),
        "Power_rabi_error_amplification_x90": library.nodes["04_Power_Rabi"].copy(name="power_rabi", operation_x180_or_any_90="x90"),
        "Ramsey": library.nodes["06_Ramsey"].copy(name="Ramsey"),
        "T2echo": library.nodes["06c_T2echo"].copy(name="T2echo"),
        # "Stark_detuning": library.nodes["09a_Stark_Detuning"].copy(name="Stark_detuning", DRAG_setpoint=None),
        "DRAG_calibration": library.nodes["09b_DRAG_Calibration_180_minus_180"].copy(name="DRAG_calibration"),
        "Randomized_benchmarking_1": library.nodes["10a_Single_Qubit_Randomized_Benchmarking"].copy(name="Randomized_benchmarking"),
        # "Randomized_benchmarking_2": library.nodes["10a_Single_Qubit_Randomized_Benchmarking"].copy(name="Randomized_benchmarking"),
        # "Randomized_benchmarking_3": library.nodes["10a_Single_Qubit_Randomized_Benchmarking"].copy(name="Randomized_benchmarking"),
        # "Power_rabi_error_amplification_x180_after_drag": library.nodes["04_Power_Rabi"].copy(name="power_rabi",
        #                                                                            operation_x180_or_any_90="x180"),
        # "Power_rabi_error_amplification_x90_after_drag": library.nodes["04_Power_Rabi"].copy(name="power_rabi",
        #                                                                           operation_x180_or_any_90="x90"),

    },
    connectivity=[
        # ("Resonator_spectroscopy", "Qubit_spectroscopy"),
        # ("Qubit_spectroscopy", "power_rabi"),
        # ("power_rabi", "T1"),
        ("Readout_frequency_optimization", "Readout_power_optimization"),
        ("Readout_power_optimization", "IQ_blobs"),
        ("IQ_blobs", "Power_rabi_error_amplification_x180"),
        ("Power_rabi_error_amplification_x180", "Power_rabi_error_amplification_x90"),
        ("Power_rabi_error_amplification_x90", "DRAG_calibration"),
        # ("Stark_detuning", "DRAG_calibration"),
        ("DRAG_calibration", "Ramsey"),
        ("Ramsey", "T1"),
        ("T1", "T2echo"),
        ("T2echo", "Randomized_benchmarking_1"),

        # ("Randomized_benchmarking_2", "Power_rabi_error_amplification_x180_after_drag"),
        # ("Power_rabi_error_amplification_x180_after_drag", "Power_rabi_error_amplification_x90_after_drag"),
        # ("Power_rabi_error_amplification_x90_after_drag", "Randomized_benchmarking_3"),
    ],
    orchestrator=BasicOrchestrator(skip_failed=False),
)

# for i in range(1, 9):
#     print(f"\n---------- Measure qubit {i} ----------\n")
#     g.run(qubits=[f"q{i}"])

g.run(qubits=["q3"])
g.run(qubits=["q4"])

# Run the graph 4x4
# g.run(qubits=[f"q{2*i+1}" for i in range(0, 4)])
# g.run(qubits=[f"q{2*i+2}" for i in range(0, 4)])

# Run the graph 2x2x2x2
# for i in range(1, 5):
#     print(f"\n---------- Measure qubits {i} & {4 + i} ----------\n")
#     g.run(qubits=[f"q{i}", f"q{4 + i}"])
# %%