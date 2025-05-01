# %%
from pathlib import Path
from typing import List
from qualibrate.orchestration.basic_orchestrator import BasicOrchestrator
from qualibrate.parameters import GraphParameters
from qualibrate.qualibration_graph import QualibrationGraph
from qualibrate.qualibration_library import QualibrationLibrary

library = QualibrationLibrary.get_active_library()


class Parameters(GraphParameters):
    qubits: List[str] = ["q1", "q2"]



multiplexed = True
flux_point = "joint"
reset_type = "heralding" # "thermal" / "heralding" / "active"


g = QualibrationGraph(
    name="Calibration_Graph",
    parameters=Parameters(),
    nodes={
        # "resonator_spectroscopy": library.nodes["02a_Resonator_Spectroscopy"].copy(multiplexed=multiplexed,
        #                                                                            name="resonator_spectroscopy"),
        # "resonator_spec_vs_flux": library.nodes["02b_Resonator_Spectroscopy_vs_Flux"].copy(flux_point_joint_or_independent=flux_point,
        #                                                                                    name="resonator_spec_vs_flux"),
        # "resonator_spec_vs_amplitude": library.nodes["02c_Resonator_Spectroscopy_vs_Amplitude"].copy(flux_point_joint_or_independent=flux_point,
        #                                                                                     name="resonator_spec_vs_amplitude"),
        # "qubit_spectroscopy": library.nodes["03a_Qubit_Spectroscopy"].copy(flux_point_joint_or_independent=flux_point,
        #                                                                    multiplexed=multiplexed,
        #                                                                    name="qubit_spectroscopy"),
        # "qubit_spectroscopy_weak_drive": library.nodes["03a_Qubit_Spectroscopy"].copy(flux_point_joint_or_independent=flux_point,
        #                                                                    multiplexed=multiplexed,
        #                                                                    name="qubit_spectroscopy_weak_drive"),
        "qubit_spec_vs_flux": library.nodes["03b_Qubit_Spectroscopy_vs_Flux"].copy(flux_point_joint_or_independent=flux_point,
                                                                                   multiplexed=multiplexed,
                                                                                   name="qubit_spec_vs_flux"),
        "power_rabi": library.nodes["04_Power_Rabi"].copy(flux_point_joint_or_independent=flux_point,
                                                          multiplexed=multiplexed,
                                                          name="power_rabi"),
        # "T1": library.nodes["05_T1"].copy(flux_point_joint_or_independent=flux_point,
        #                                           multiplexed=multiplexed,
        #                                           name="T1"),
        # "T2ey": library.nodes["05b_T2ey"].copy(flux_point_joint_or_independent=flux_point,
        #                                           multiplexed=multiplexed,
        #                                           name="T2ey"),
        # "ramsey": library.nodes["06_Ramsey"].copy(flux_point_joint_or_independent=flux_point,
        #                                           multiplexed=multiplexed,
        #                                           name="ramsey"),
        # "readout_frequency_optimization": library.nodes["07a_Readout_Frequency_Optimization"].copy(flux_point_joint_or_independent=flux_point,
        #                                                                                            multiplexed=multiplexed,
        #                                                                                            name="readout_frequency_optimization"),
        # "IQ_blobs": library.nodes["07b_IQ_Blobs"].copy(flux_point_joint_or_independent=flux_point,
        #                                                multiplexed=multiplexed,
        #                                                name="IQ_blobs"),
        # "readout_power_optimization": library.nodes["07c_Readout_Power_Optimization"].copy(flux_point_joint_or_independent=flux_point, multiplexed=multiplexed, name="readout_power_optimization"),
        # "readout_power_time_optimization": library.nodes["07d_Readout_Power_Time_Optimization"].copy(
        #     flux_point_joint_or_independent=flux_point, multiplexed=multiplexed, name="readout_power_time_optimization"),

        "ramsey_flux_calibration": library.nodes["08_Ramsey_vs_Flux_Calibration"].copy(flux_point_joint_or_independent=flux_point,
                                                                                       multiplexed=multiplexed,
                                                                                       name="ramsey_flux_calibration"),
        "stark_shift_calibration": library.nodes["09b_DRAG_Calibration_180_minus_180"].copy(flux_point_joint_or_independent=flux_point,
                                                                                     multiplexed=multiplexed,
                                                                                     name="stark_shift_calibration"),

        # "stark_shift_calibration": library.nodes["09a_Stark_Shift_Calibration"].copy(flux_point_joint_or_independent=flux_point,
        #                                                                              multiplexed=multiplexed,
        #                                                                              name="stark_shift_calibration"),
        #
        # "stark_shift_calibration_zoom": library.nodes["09a_Stark_Shift_Calibration"].copy(flux_point_joint_or_independent=flux_point,
        #                                                                              multiplexed=multiplexed, frequency_step_in_mhz=20,
        #                                                                              name="stark_shift_calibration_zoom"),

        "stark_shift_calibration_zoom": library.nodes["09b_DRAG_Calibration_180_minus_180"].copy(
            flux_point_joint_or_independent=flux_point,
            multiplexed=multiplexed,min_amp_factor=-0.5, max_amp_factor=0.5, amp_factor_step=0.005,
            name="stark_shift_calibration_zoom"),
        "pi_pulse_train": library.nodes["04_Power_Rabi"].copy(flux_point_joint_or_independent=flux_point,
                                                                                   multiplexed=multiplexed, operation_x180_or_any_90="x180_Cosine",
                                                                                   min_amp_factor=0.0, max_amp_factor=1.5, amp_factor_step=0.05,
                                                                                   max_number_rabi_pulses_per_sweep=40,
                                                                                   name="pi_pulse_train"),

        "single_qubit_randomized_benchmarking": library.nodes["10c_Single_Qubit_Randomized_Benchmarking_Large_Depth"].copy(flux_point_joint_or_independent=flux_point,
                                                                                                               multiplexed=multiplexed,
                                                                                                               name="single_qubit_randomized_benchmarking"),
    },
    connectivity=[
                  ("qubit_spec_vs_flux", "power_rabi"),
                  ("power_rabi", "ramsey_flux_calibration"),
                  ("ramsey_flux_calibration", "stark_shift_calibration"),
                  ("stark_shift_calibration", "stark_shift_calibration_zoom"),
                  ("stark_shift_calibration_zoom", "pi_pulse_train"),
                  ("pi_pulse_train", "single_qubit_randomized_benchmarking"),
                  ],

    orchestrator=BasicOrchestrator(skip_failed=True),
)
# %%

g.run()
# %%