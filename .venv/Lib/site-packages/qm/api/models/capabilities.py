import dataclasses
from typing import Optional

from qm.api.models.info import QuaMachineInfo

OPX_FEM_IDX = 1


@dataclasses.dataclass(frozen=True)
class ServerCapabilities:
    has_job_streaming_state: bool
    supports_multiple_inputs_for_element: bool
    supports_analog_delay: bool
    supports_shared_oscillators: bool
    supports_crosstalk: bool
    supports_shared_ports: bool
    supports_input_stream: bool
    supports_new_grpc_structure: bool
    supports_double_frequency: bool
    supports_command_timestamps: bool
    supports_inverted_digital_output: bool
    supports_octave_reset: bool
    supports_sticky_elements: bool
    supports_fast_frame_rotation: bool
    fem_number_in_simulator: int
    set_zero_frequency_in_calibration: bool = False
    # TODO - remove set_zero_frequency_in_calibration and once we fix the bug in the OPY of the CSF allocation
    supports_api_v2: bool = False

    @staticmethod
    def build(qua_implementation: Optional[QuaMachineInfo] = None) -> "ServerCapabilities":
        caps = qua_implementation.capabilities if qua_implementation is not None else list()
        if "__qop3" in caps:
            return ServerCapabilities(
                has_job_streaming_state=True,
                supports_multiple_inputs_for_element=True,
                supports_analog_delay=True,
                supports_shared_oscillators=True,
                supports_crosstalk=True,
                supports_shared_ports=True,
                supports_input_stream=True,
                supports_new_grpc_structure=True,
                supports_double_frequency=True,
                supports_command_timestamps=True,
                supports_inverted_digital_output=True,
                supports_sticky_elements=True,
                supports_octave_reset=True,
                supports_fast_frame_rotation=True,
                fem_number_in_simulator=OPX_FEM_IDX,
                set_zero_frequency_in_calibration=True,
                supports_api_v2=True,
            )
        return ServerCapabilities(
            has_job_streaming_state="qm.job_streaming_state" in caps,
            supports_multiple_inputs_for_element="qm.multiple_inputs_for_element" in caps,
            supports_analog_delay="qm.analog_delay" in caps,
            supports_shared_oscillators="qm.shared_oscillators" in caps,
            supports_crosstalk="qm.crosstalk" in caps,
            supports_shared_ports="qm.shared_ports" in caps,
            supports_input_stream="qm.input_stream" in caps,
            supports_new_grpc_structure="qm.new_grpc_structure" in caps,
            supports_double_frequency="qm.double_frequency" in caps,
            supports_command_timestamps="qm.play_tag" in caps,
            supports_inverted_digital_output="qm.inverted_digital_output" in caps,
            supports_sticky_elements="qm.sticky_elements" in caps,
            supports_octave_reset="qm.octave_reset" in caps,
            supports_fast_frame_rotation="qm.fast_frame_rotation" in caps,
            fem_number_in_simulator=0,
        )
