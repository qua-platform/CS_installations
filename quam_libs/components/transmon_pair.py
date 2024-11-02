from typing import Dict, Any, Optional, Union
from dataclasses import field
from .gates.two_qubit_gates import TwoQubitGate #added

from quam.core import QuamComponent, quam_dataclass
from .transmon import Transmon
from .tunable_coupler import TunableCoupler
from qm.qua import align


__all__ = ["TransmonPair"]


@quam_dataclass
class TransmonPair(QuamComponent):
    id: Union[int, str]
    qubit_control: Transmon = None
    qubit_target: Transmon = None
    coupler: Optional[TunableCoupler] = None
    gates: Dict[str, TwoQubitGate] = field(default_factory=dict) #added
    J2: float = 0 #added
    detuning: float = 0 #added
    extras: Dict[str, Any] = field(default_factory=dict)

    @property
    def name(self):
        """The name of the transmon"""
        return self.id if isinstance(self.id, str) else f"q{self.id}"

    def align(self):
        if self.coupler:
            align(self.qubit_control.xy.name, self.qubit_control.z.name, self.qubit_control.resonator.name, self.qubit_target.xy.name,
                  self.qubit_target.z.name, self.qubit_target.resonator.name, self.coupler.name)
        else:
            align(self.qubit_control.xy.name, self.qubit_control.z.name, self.qubit_control.resonator.name, self.qubit_target.xy.name,
                  self.qubit_target.z.name, self.qubit_target.resonator.name)