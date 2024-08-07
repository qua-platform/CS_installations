from typing import Tuple, Union, TypeVar

from qm.grpc.qua import QuaProgramRampPulse
from qm.qua._type_hinting import MessageExpressionType
from qm.qua._expressions import QuaNumberType, QuaExpressionType, QuaNumberArrayType

ChirpType = Union[
    Tuple[QuaNumberArrayType, str],
    Tuple[QuaNumberType, str],
    Tuple[QuaNumberArrayType, QuaNumberArrayType, str],
]
AmpValuesType = Tuple[
    MessageExpressionType,
    MessageExpressionType,
    MessageExpressionType,
    MessageExpressionType,
]
MeasurePulseType = Union[str, Tuple[str, AmpValuesType]]
PlayPulseType = Union[MeasurePulseType, QuaProgramRampPulse]
E = TypeVar("E")
TypeOrExpression = Union[E, QuaExpressionType]
