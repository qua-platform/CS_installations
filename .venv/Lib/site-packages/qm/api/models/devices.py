from enum import Enum
from typing import Dict, List, Union
from dataclasses import asdict, dataclass

from qm.grpc.qm_api import DigitalInputPortPolarity


@dataclass(frozen=True)
class MixerInfo:
    mixer: str
    frequency_negative: bool
    intermediate_frequency: int
    intermediate_frequency_double: float
    lo_frequency: int
    lo_frequency_double: float

    def as_dict(self) -> Dict[str, Union[str, bool, int, float]]:
        return {key: value for key, value in asdict(self).items() if value is not None}


@dataclass(frozen=True)
class AnalogOutputPortFilter:
    feedforward: List[float]
    feedback: List[float]


class Polarity(Enum):
    RISING = DigitalInputPortPolarity.RISING
    FALLING = DigitalInputPortPolarity.FALLING
