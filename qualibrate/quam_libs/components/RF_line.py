from quam.components import SingleChannel
from quam.components.ports import LFFEMAnalogOutputPort
from quam.core import quam_dataclass
from typing import Dict, Any
from dataclasses import field
__all__ = ["RFLine"]


@quam_dataclass
class RFLine(SingleChannel):
    """QuAM component for a flux line.

    Args:
        independent_offset (float): the flux bias corresponding to the resonator maximum frequency when the active qubits are not interacting (min offset) in V.
        joint_offset (float): the flux bias corresponding to the resonator maximum frequency when the active qubits are interacting (joint offset) in V.
        min_offset (float): the flux bias corresponding to the resonator minimum frequency in V.
        arbitrary_offset (float): arbitrary flux bias in V.
        settle_time (float): the flux line settle time in ns.
    """

    independent_offset: float = 0.0
    joint_offset: float = 0.0
    min_offset: float = 0.0
    arbitrary_offset: float = 0.0
    settle_time: float = 16
    extras: Dict[str, Any] = field(default_factory=dict)

