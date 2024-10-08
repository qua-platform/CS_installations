from typing import Dict, Any, Optional, Union, List, Tuple
from dataclasses import field

from quam.core import QuamComponent, quam_dataclass
from .transmon import Transmon
from .tunable_coupler import TunableCoupler
from .gates.two_qubit_gates import TwoQubitGate

__all__ = ["TransmonPair"]


@quam_dataclass
class TransmonPair(QuamComponent):
    id: Union[int, str]
    qubit_control: Transmon = None
    qubit_target: Transmon = None
    coupler: Optional[TunableCoupler] = None
    gates: Dict[str, TwoQubitGate] = field(default_factory=dict)
    J2: float = 0
    detuning: float = 0

    extras: Dict[str, Any] = field(default_factory=dict)

    @property
    def name(self):
        """The name of the transmon pair"""
        return self.id if isinstance(self.id, str) else f"q{self.id}"
    
