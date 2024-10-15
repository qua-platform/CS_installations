from quam.components import IQChannel
from quam.core import quam_dataclass

__all__ = ["CrossResonanceDrive"]


@quam_dataclass
class CrossResonanceDrive(IQChannel):

    f_01: float = None
    f_12: float = None