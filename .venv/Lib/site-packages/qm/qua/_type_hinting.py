from typing import List, Type, Tuple, Union, TypeVar

import numpy as np
import numpy.typing as npt

from qm.grpc import qua

MessageExpressionType = qua.QuaProgramAnyScalarExpression
MessageArrayVarType = qua.QuaProgramArrayVarRefExpression
MessageVarType = qua.QuaProgramVarRefExpression
MessageVariableType = Union[MessageArrayVarType, MessageVarType]
MessageVariableOrExpression = Union[MessageExpressionType, MessageVariableType]


ArrayT = TypeVar("ArrayT")
PyArrayType = Union[List[ArrayT], npt.NDArray[ArrayT], Tuple[ArrayT, ...]]

NpTypes = Union[np.floating, np.integer, np.bool_, np.longdouble]

PyIntType = Union[int, np.integer]
PyFloatType = Union[float, np.floating, np.longdouble]
PyNumberType = Union[PyFloatType, PyIntType]
PyNumberArrayType = PyArrayType[PyNumberType]
PyBoolType = Union[bool, np.bool_]

AllPyTypes = Union[PyBoolType, PyNumberType]

ForEachValuesType = Union[PyNumberArrayType, Tuple[PyNumberArrayType, ...]]

T = TypeVar("T")
OneOrMore = Union[T, PyArrayType[T]]


class fixed:
    pass


VariableDeclarationType = Union[Type[int], Type[bool], Type[float], Type[fixed]]
