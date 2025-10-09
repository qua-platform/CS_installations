from quam.components import *
from quam.core import quam_dataclass, QuamComponent

__all__ = ["Flux_Tunable_Transmon"]


@quam_dataclass
class Flux_Line(QuamComponent):
    id: str
    
