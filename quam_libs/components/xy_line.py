from quam.components import IQChannel
from quam.core import quam_dataclass
from typing import List, Optional


@quam_dataclass
class XYLine(IQChannel):
    mixer_calibration: Optional[List[float]] = None
