from typing import Dict, Any, Optional, Union, Tuple
from dataclasses import field

from quam.core import QuamComponent, quam_dataclass
from .transmon import Transmon
from .tunable_coupler import TunableCoupler


__all__ = ["TransmonPair"]


@quam_dataclass
class TransmonPair(QuamComponent):
    id: Union[int, str]
    qubit_control: Transmon = None
    qubit_target: Transmon = None
    coupler: Optional[TunableCoupler] = None
    mutual_flux_point: Tuple[float, float] = (0.0,0.0)

    extras: Dict[str, Any] = field(default_factory=dict)

    @property
    def name(self):
        """The name of the transmon pair"""
        return self.id if isinstance(self.id, str) else f"q{self.id}"
    
    def apply_mutual_flux_point(self):
        self.qubit_control.z.set_dc_offset(self.mutual_flux_point[0])
        self.qubit_target.z.set_dc_offset(self.mutual_flux_point[1])
