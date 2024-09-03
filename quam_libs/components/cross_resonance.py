from quam.components import IQChannel
from quam.components.ports import LFFEMAnalogOutputPort
from quam.core import quam_dataclass

__all__ = ["CrossResonance"]


@quam_dataclass
class CrossResonance(IQChannel):
    """
    Example QuAM component for a tunable coupler.

    Args:
        decouple_offset (float): the tunable coupler for which the .
        interaction_offset (float): the tunable coupler for which the .
    """
    output_mode: str = "direct"
    upsampling_mode: str = "pulse"

    def __post_init__(self):
        if isinstance(self.opx_output_I, LFFEMAnalogOutputPort):
            self.opx_output_I.upsampling_mode = self.upsampling_mode
            self.opx_output_I.output_mode = self.output_mode
        if isinstance(self.opx_output_Q, LFFEMAnalogOutputPort):
            self.opx_output_Q.upsampling_mode = self.upsampling_mode
            self.opx_output_Q.output_mode = self.output_mode
