from quam.core import quam_dataclass
from quam.components import SingleChannel


__all__ = ["TunableCoupler"]


@quam_dataclass
class TunableCoupler(SingleChannel):
    """Example QuAM component for a tunable coupler line.

    Args:
        decouple_offset (float): the tunable coupler for which the .
        interaction_offset (float): the tunable coupler for which the .
    """

    decouple_offset: float = 0.0
    interaction_offset: float = 0.0

    def to_decouple_idle(self):
        """Set the tunable coupler to the decouple offset"""
        self.set_dc_offset(self.decouple_offset)

    def to_interaction_idle(self):
        """Set the tunable coupler to the interaction offset"""
        self.set_dc_offset(self.interaction_offset)
