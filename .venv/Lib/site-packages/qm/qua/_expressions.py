from typing import Union, TypeVar, Optional

import numpy as np
from deprecation import deprecated

from qm._loc import _get_loc
from qm.grpc import qua as _qua
from qm.exceptions import QmQuaException
from qm.serialization.expression_serializing_visitor import ExpressionSerializingVisitor
from qm.qua._type_hinting import (
    PyIntType,
    PyBoolType,
    PyArrayType,
    PyFloatType,
    PyNumberType,
    MessageVariableType,
    MessageExpressionType,
    VariableDeclarationType,
    MessageVariableOrExpression,
    fixed,
)

_ScalarExpressionType = _qua.QuaProgramAnyScalarExpression
_VariableRefType = _qua.QuaProgramVarRefExpression


def var(name: str) -> _VariableRefType:
    """A reference to a variable

    Args:
        name

    Returns:

    """
    exp = _qua.QuaProgramVarRefExpression(name=name, loc=_get_loc())
    return exp


def binary(left: _ScalarExpressionType, sop: str, right: _ScalarExpressionType) -> _ScalarExpressionType:
    """A binary operation

    Args:
        left
        sop
        right

    Returns:

    """
    if sop == "+":
        op = _qua.QuaProgramBinaryExpressionBinaryOperator.ADD
    elif sop == "-":
        op = _qua.QuaProgramBinaryExpressionBinaryOperator.SUB
    elif sop == ">":
        op = _qua.QuaProgramBinaryExpressionBinaryOperator.GT
    elif sop == "<":
        op = _qua.QuaProgramBinaryExpressionBinaryOperator.LT
    elif sop == "<=":
        op = _qua.QuaProgramBinaryExpressionBinaryOperator.LET
    elif sop == ">=":
        op = _qua.QuaProgramBinaryExpressionBinaryOperator.GET
    elif sop == "==":
        op = _qua.QuaProgramBinaryExpressionBinaryOperator.EQ
    elif sop == "*":
        op = _qua.QuaProgramBinaryExpressionBinaryOperator.MULT
    elif sop == "/":
        op = _qua.QuaProgramBinaryExpressionBinaryOperator.DIV
    elif sop == "|":
        op = _qua.QuaProgramBinaryExpressionBinaryOperator.OR
    elif sop == "&":
        op = _qua.QuaProgramBinaryExpressionBinaryOperator.AND
    elif sop == "^":
        op = _qua.QuaProgramBinaryExpressionBinaryOperator.XOR
    elif sop == "<<":
        op = _qua.QuaProgramBinaryExpressionBinaryOperator.SHL
    elif sop == ">>":
        op = _qua.QuaProgramBinaryExpressionBinaryOperator.SHR
    else:
        raise QmQuaException("Unsupported operator " + sop)

    exp = _qua.QuaProgramAnyScalarExpression(
        binary_operation=_qua.QuaProgramBinaryExpression(loc=_get_loc(), left=left, right=right, op=op)
    )
    return exp


def literal_int(value: int) -> _ScalarExpressionType:
    exp = _qua.QuaProgramAnyScalarExpression(
        literal=_qua.QuaProgramLiteralExpression(value=str(value), type=_qua.QuaProgramType.INT, loc=_get_loc())
    )
    return exp


def literal_bool(value: bool) -> _ScalarExpressionType:
    exp = _qua.QuaProgramAnyScalarExpression(
        literal=_qua.QuaProgramLiteralExpression(value=str(value), type=_qua.QuaProgramType.BOOL, loc=_get_loc())
    )
    return exp


def literal_real(value: float) -> _ScalarExpressionType:
    exp = _qua.QuaProgramAnyScalarExpression(
        literal=_qua.QuaProgramLiteralExpression(value=str(value), type=_qua.QuaProgramType.REAL, loc=_get_loc())
    )
    return exp


def io1() -> _ScalarExpressionType:
    exp = _qua.QuaProgramAnyScalarExpression(variable=_qua.QuaProgramVarRefExpression(io_number=1, loc=_get_loc()))
    return exp


def io2() -> _ScalarExpressionType:
    exp = _qua.QuaProgramAnyScalarExpression(variable=_qua.QuaProgramVarRefExpression(io_number=2, loc=_get_loc()))
    return exp


def array(
    value: _qua.QuaProgramArrayVarRefExpression,
    index_exp: Optional[_ScalarExpressionType],
) -> Union[_qua.QuaProgramArrayVarRefExpression, _ScalarExpressionType]:
    if index_exp is None:
        return value
    else:
        loc = _get_loc()
        value.loc = loc
        exp = _qua.QuaProgramAnyScalarExpression(
            array_cell=_qua.QuaProgramArrayCellRefExpression(array_var=value, index=index_exp, loc=loc)
        )
        return exp


def var_ref(value: str, index_exp: Optional[_ScalarExpressionType]) -> _ScalarExpressionType:
    exp = _qua.QuaProgramAnyScalarExpression()

    loc = _get_loc()
    if index_exp is None:
        exp.variable = _qua.QuaProgramVarRefExpression(name=value, loc=loc)
    else:
        exp.array_cell = _qua.QuaProgramArrayCellRefExpression(
            array_var=_qua.QuaProgramArrayVarRefExpression(name=value, loc=loc),
            index=index_exp,
            loc=loc,
        )
    return exp


def lib_func(
    lib_name: str,
    func_name: str,
    *args: Union[_ScalarExpressionType, _qua.QuaProgramArrayVarRefExpression],
) -> _ScalarExpressionType:
    exp = _qua.QuaProgramAnyScalarExpression(
        lib_function=_qua.QuaProgramLibFunctionExpression(
            loc=_get_loc(), function_name=func_name, library_name=lib_name
        )
    )

    for arg in args:
        if isinstance(arg, _qua.QuaProgramArrayVarRefExpression):
            element = _qua.QuaProgramLibFunctionExpressionArgument(array=arg)
            exp.lib_function.arguments.append(element)
        else:
            element = _qua.QuaProgramLibFunctionExpressionArgument(scalar=arg)
            exp.lib_function.arguments.append(element)

    return exp


QuaExpressionType = Union["QuaExpression", MessageExpressionType]
QuaVariableType = Union["QuaVariable", MessageVariableType]

QuaGenericT = TypeVar("QuaGenericT")
QuaGenericType = Union[QuaGenericT, QuaVariableType]
QuaArrayT = TypeVar("QuaArrayT")
QuaArrayType = Union[PyArrayType[QuaArrayT], QuaVariableType]
QuaIntType = QuaGenericType[PyIntType]
QuaBoolType = QuaGenericType[PyBoolType]
QuaFloatType = QuaGenericType[PyFloatType]
QuaNumberType = QuaGenericType[PyNumberType]
QuaNumberArrayType = QuaArrayType[PyNumberType]

AllQuaTypes = Union[QuaNumberType, QuaBoolType, QuaExpressionType]
QuaGenericType = Union[QuaGenericT, QuaVariableType]


class QuaExpression:
    def __init__(self, expression: MessageVariableOrExpression):
        self._expression = expression

    def __getitem__(self, item: "QuaNumberType") -> QuaExpressionType:
        return QuaExpression(to_expression(self._expression, item))

    def unwrap(self) -> MessageVariableOrExpression:
        return self._expression

    def empty(self) -> bool:
        return self._expression is None

    def length(self) -> QuaExpressionType:
        unwrapped_element = self.unwrap()
        if isinstance(unwrapped_element, _qua.QuaProgramArrayVarRefExpression):
            array_exp = _qua.QuaProgramArrayLengthExpression(array=unwrapped_element)
            array_exp.array = unwrapped_element
            result = _qua.QuaProgramAnyScalarExpression(array_length=array_exp)
            return QuaExpression(result)
        else:
            raise QmQuaException(f"{unwrapped_element} is not an array")

    def __add__(self, other: "AllQuaTypes") -> "QuaExpression":
        other = to_expression(other)
        return QuaExpression(binary(self._expression, "+", other))

    def __radd__(self, other: "AllQuaTypes") -> "QuaExpression":
        other = to_expression(other)
        return QuaExpression(binary(other, "+", self._expression))

    def __sub__(self, other: "AllQuaTypes") -> "QuaExpression":
        other = to_expression(other)
        return QuaExpression(binary(self._expression, "-", other))

    def __rsub__(self, other: "AllQuaTypes") -> "QuaExpression":
        other = to_expression(other)
        return QuaExpression(binary(other, "-", self._expression))

    def __neg__(self) -> "QuaExpression":
        other = to_expression(0)
        return QuaExpression(binary(other, "-", self._expression))

    def __gt__(self, other: "AllQuaTypes") -> "QuaExpression":
        other = to_expression(other)
        return QuaExpression(binary(self._expression, ">", other))

    def __ge__(self, other: "AllQuaTypes") -> "QuaExpression":
        other = to_expression(other)
        return QuaExpression(binary(self._expression, ">=", other))

    def __lt__(self, other: "AllQuaTypes") -> "QuaExpression":
        other = to_expression(other)
        return QuaExpression(binary(self._expression, "<", other))

    def __le__(self, other: "AllQuaTypes") -> "QuaExpression":
        other = to_expression(other)
        return QuaExpression(binary(self._expression, "<=", other))

    def __eq__(self, other: "AllQuaTypes") -> "QuaExpression":
        other = to_expression(other)
        return QuaExpression(binary(self._expression, "==", other))

    def __mul__(self, other: "AllQuaTypes") -> "QuaExpression":
        other = to_expression(other)
        return QuaExpression(binary(self._expression, "*", other))

    def __rmul__(self, other: "AllQuaTypes") -> "QuaExpression":
        other = to_expression(other)
        return QuaExpression(binary(other, "*", self._expression))

    def __truediv__(self, other: "AllQuaTypes") -> "QuaExpression":
        other = to_expression(other)
        return QuaExpression(binary(self._expression, "/", other))

    def __rtruediv__(self, other: "AllQuaTypes") -> "QuaExpression":
        other = to_expression(other)
        return QuaExpression(binary(other, "/", self._expression))

    def __lshift__(self, other: "AllQuaTypes") -> "QuaExpression":
        other = to_expression(other)
        return QuaExpression(binary(self._expression, "<<", other))

    def __rlshift__(self, other: "AllQuaTypes") -> "QuaExpression":
        other = to_expression(other)
        return QuaExpression(binary(other, "<<", self._expression))

    def __rshift__(self, other: "AllQuaTypes") -> "QuaExpression":
        other = to_expression(other)
        return QuaExpression(binary(self._expression, ">>", other))

    def __rrshift__(self, other: "AllQuaTypes") -> "QuaExpression":
        other = to_expression(other)
        return QuaExpression(binary(other, ">>", self._expression))

    def __and__(self, other: "AllQuaTypes") -> "QuaExpression":
        other = to_expression(other)
        return QuaExpression(binary(self._expression, "&", other))

    def __rand__(self, other: "AllQuaTypes") -> "QuaExpression":
        other = to_expression(other)
        return QuaExpression(binary(other, "&", self._expression))

    def __or__(self, other: "AllQuaTypes") -> "QuaExpression":
        other = to_expression(other)
        return QuaExpression(binary(self._expression, "|", other))

    def __ror__(self, other: "AllQuaTypes") -> "QuaExpression":
        other = to_expression(other)
        return QuaExpression(binary(other, "|", self._expression))

    def __xor__(self, other: "AllQuaTypes") -> "QuaExpression":
        other = to_expression(other)
        return QuaExpression(binary(self._expression, "^", other))

    def __rxor__(self, other: "AllQuaTypes") -> "QuaExpression":
        other = to_expression(other)
        return QuaExpression(binary(other, "^", self._expression))

    def __invert__(self) -> "QuaExpression":
        other = to_expression(True)
        return QuaExpression(binary(self._expression, "^", other))

    def __str__(self) -> str:
        return ExpressionSerializingVisitor.serialize(self._expression)

    def __bool__(self):
        raise QmQuaException(
            "Attempted to use a Python logical operator on a QUA variable. If you are unsure why you got this message,"
            " please see https://qm-docs.qualang.io/guides/qua_ref#boolean-operations"
        )


class QuaVariable(QuaExpression):
    def __init__(self, expression: MessageVariableOrExpression, t: "VariableDeclarationType"):
        super().__init__(expression)
        self._type = t

    @deprecated("1.1", "1.2", details="use: '_Variable.is_fixed()' instead")
    def isFixed(self) -> bool:
        return self.is_fixed()

    @deprecated("1.1", "1.2", details="use: '_Variable.is_int()' instead")
    def isInt(self) -> bool:
        return self.is_int()

    @deprecated("1.1", "1.2", details="use: '_Variable.is_bool()' instead")
    def isBool(self) -> bool:
        return self.is_bool()

    def is_fixed(self) -> bool:
        return self._type == fixed

    def is_int(self) -> bool:
        return self._type == int

    def is_bool(self) -> bool:
        return self._type == bool


IO1 = object()
IO2 = object()


def _fix_object_data_type(obj):
    if isinstance(obj, (np.floating, np.integer, np.bool_)):
        obj_item = obj.item()
        if isinstance(obj_item, np.longdouble):
            return float(obj_item)
        else:
            return obj_item
    else:
        return obj


def to_expression(other: "AllQuaTypes", index_exp: Optional["QuaNumberType"] = None) -> MessageVariableOrExpression:
    other = _fix_object_data_type(other)
    if index_exp is not None and type(index_exp) is not _qua.QuaProgramAnyScalarExpression:
        index_exp = to_expression(index_exp, None)

    if index_exp is not None and type(other) is not _qua.QuaProgramArrayVarRefExpression:
        raise QmQuaException(f"{other} is not an array")

    if isinstance(other, QuaExpression):
        return other.unwrap()
    elif isinstance(other, _qua.QuaProgramVarRefExpression):
        return other
    elif isinstance(other, _qua.QuaProgramArrayVarRefExpression):
        return array(other, index_exp)
    elif isinstance(other, bool):  # Since bool is a subtype of int, it must be before it
        return literal_bool(other)
    elif isinstance(other, int):
        return literal_int(other)
    elif isinstance(other, float):
        return literal_real(other)
    elif other == IO1:
        return io1()
    elif other == IO2:
        return io2()
    else:
        raise QmQuaException(f"Can't handle {other}")
