from typing import Dict, Any, Optional, Union
from dataclasses import field

from quam.core import QuamComponent, quam_dataclass
from .transmon import Transmon
from .cross_resonance import CrossResonance


__all__ = ["TransmonPair"]


@quam_dataclass
class TransmonPair(QuamComponent):
    id: Union[int, str]
    qubit_control: Transmon
    qubit_target: Transmon
    cr_control: CrossResonance = None
    cr_target: CrossResonance = None

    extras: Dict[str, Any] = field(default_factory=dict)

    @property
    def name(self):
        """The name of the transmon"""
        return self.id if isinstance(self.id, str) else f"q{self.id}"
