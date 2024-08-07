import random
from functools import wraps
from collections.abc import Iterable

import qm.qua._expressions as _exp
from qm.qua._dsl import assign, declare
from qm.utils import get_iterable_elements_datatype as _get_iterable_elements_datatype


def _library_function(lib_name, func_name):
    def library_decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            new_args = function(*args, **kwargs)
            return call_library_function(lib_name, func_name, new_args)

        return wrapper

    return library_decorator


def _sanitize_arg(arg):
    if isinstance(arg, Iterable):
        return declare(_get_iterable_elements_datatype(arg), value=arg)
    return arg


def call_library_function(lib_name, func_name, args):
    return _exp.QuaExpression(_exp.lib_func(lib_name, func_name, *[_exp.to_expression(_sanitize_arg(x)) for x in args]))


class Math:
    @staticmethod
    @_library_function("math", "log")
    def log(x, base):
        r"""Computes $\mathrm{log}_{base}(x)$

        Args:
            x: a QUA fixed larger than pow2(-8)=0.00390625
            base: a QUA fixed larger than pow2(1/8)=1.09051

        Returns:
            a QUA fixed
        """
        return (x, base)

    @staticmethod
    @_library_function("math", "pow")
    def pow(base, x):
        r"""Computes ${base}^{x}$.
        Does not support base=1, nor the case where both base=0 & x=0.

        Args:
            base: a non-negative QUA fixed
            x: a QUA fixed

        Returns:
            a QUA fixed
        """
        return (base, x)

    @staticmethod
    @_library_function("math", "div")
    def div(x, y):
        r"""Computes the division between two same-type variables $x/y$

        Args:
            x: a QUA parameter
            y: a QUA parameter not equal to 0

        Returns:
            a QUA fixed
        """
        return (x, y)

    @staticmethod
    @_library_function("math", "exp")
    def exp(x):
        r"""Computes $e^{x}$

        Args:
            x: a QUA fixed smaller than ln(8)=2.0794415416

        Returns:
            a QUA fixed
        """
        return (x,)

    @staticmethod
    @_library_function("math", "pow2")
    def pow2(x):
        r"""Computes $2^{x}$

        Args:
            x: a QUA fixed smaller than 3 (to avoid overflow)

        Returns:
            a QUA fixed
        """
        return (x,)

    @staticmethod
    @_library_function("math", "ln")
    def ln(x):
        r"""Computes $\mathrm{ln}(x)$

        Args:
            x: a QUA fixed larger than exp(-8)=0.0003354627

        Returns:
            a QUA fixed
        """
        return (x,)

    @staticmethod
    @_library_function("math", "log2")
    def log2(x):
        r"""Computes $\mathrm{log}_{2}(x)$

        Args:
            x: a QUA fixed larger than pow2(-8)=0.00390625

        Returns:
            a QUA fixed
        """
        return (x,)

    @staticmethod
    @_library_function("math", "log10")
    def log10(x):
        r"""Computes $\mathrm{log}_{10}(x)$

        Args:
            x: a QUA fixed larger than pow10(-8)=0.00000001

        Returns:
            a QUA fixed
        """
        return (x,)

    @staticmethod
    @_library_function("math", "sqrt")
    def sqrt(x):
        r"""Computes the square root of x

        Args:
            x: a non-negative QUA fixed

        Returns:
            a QUA fixed
        """
        return (x,)

    @staticmethod
    @_library_function("math", "inv_sqrt")
    def inv_sqrt(x):
        r"""Computes the inverse square root of x

        Args:
            x: a QUA fixed larger than 1/64

        Returns:
            a QUA fixed
        """
        return (x,)

    @staticmethod
    @_library_function("math", "inv")
    def inv(x):
        r"""Computes the inverse of x

        Args:
            x: a QUA fixed which is x<=-1/8 or 1/8<x

        Returns:
            a QUA fixed
        """
        return (x,)

    @staticmethod
    @_library_function("math", "MSB")
    def msb(x):
        r"""Finds the index of the most significant bit in the parameter x.
        Notes:

        - Result is independent of sign, for example, +3 and -3 will return the same msb
        - The returned value will be the closet log2, rounded down.

          This is given by $\mathrm{floor}(\mathrm{log}_2(|x|))$.

          For example:

          - msb(0.1) will return -4.
          - msb(5) will return 2.
        - For an integer, msb(0) will return 0.
        - For a fixed point number, msb(0) will return -28.

        Args:
            x: a QUA fixed or a QUA int

        Returns:
            a QUA int
        """
        return (x,)

    @staticmethod
    @_library_function("math", "elu")
    def elu(x):
        r"""Computes the Exponential Linear Unit activation function of x
          $\mathrm{ELU(x)} = \mathrm{max}(0, x) + \mathrm{min}(0, \mathrm{exp}(x)-1)$.

        Args:
            x: a QUA fixed

        Returns:
            a QUA fixed
        """
        return (x,)

    @staticmethod
    @_library_function("math", "aelu")
    def aelu(x):
        r"""Computes faster an approximated Exponential Linear Unit activation function of x
          $\mathrm{aELU}(x) \sim \mathrm{ELU}(x)$

        Args:
            x: a QUA fixed

        Returns:
            a QUA fixed
        """
        return (x,)

    @staticmethod
    @_library_function("math", "selu")
    def selu(x):
        r"""Computes the Scaled Exponential Linear Unit activation function of x
        $\mathrm{SELU}(x) = s*(\mathrm{max}(0, x)+a*\mathrm{min}(0, \mathrm{exp}(x)-1))$,
        $a=1.67326324$, $s=1.05070098$

        Args:
            x: a QUA fixed

        Returns:
            a QUA fixed
        """
        return (x,)

    @staticmethod
    @_library_function("math", "relu")
    def relu(x):
        r"""Computes the Rectified Linear Unit activation function of x
          $\mathrm{ReLU}(x) = \mathrm{max}(0, x)$

        Args:
            x: a QUA fixed

        Returns:
            a QUA fixed
        """
        return (x,)

    @staticmethod
    @_library_function("math", "plrelu")
    def plrelu(x, a):
        r"""Computes the Parametric Leaky Rectified Linear Unit activation function of x
          $\mathrm{PLReLU}(x, a) = \mathrm{max}(0, x)+a*\mathrm{min}(0, x)$

        Args:
            x: a QUA fixed
            a: a QUA fixed

        Returns:
            a QUA fixed
        """
        return (x, a)

    @staticmethod
    @_library_function("math", "lrelu")
    def lrelu(x):
        r"""Computes the Leaky Rectified Linear Unit activation function of x
          $\mathrm{LReLU}(x)=\mathrm{max}(0, x)+0.01*\mathrm{min}(0, x)$

        Args:
            x: a QUA fixed

        Returns:
            a QUA fixed
        """
        return (x,)

    @staticmethod
    @_library_function("math", "sin2pi")
    def sin2pi(x):
        r"""Computes $\mathrm{sin}(2 \pi x)$.
        This is more efficient than `Math.sin(2*np.pi*x)`.
        In addition, this function is immune to overflows: An overflow means that the argument gets a $\pm 16$, which does not change the result due to the periodicity of the sine function.

        Args:
            x (QUA variable of type fixed): the angle in radians

        Returns:
            a QUA fixed
        """
        return (x,)

    @staticmethod
    @_library_function("math", "cos2pi")
    def cos2pi(x):
        r"""Computes $\mathrm{cos}(2 \pi x)$.
        This is more efficient than Math.cos($2 \pi x$).
        In addition, this function is immune to overflows: An overflow means that the argument gets a :math:`\pm 16`, which does not change the result due to the periodcity of the cosine function.

        Args:
            x (QUA variable of type fixed): the angle in radians

        Returns:
            a QUA fixed
        """
        return (x,)

    @staticmethod
    @_library_function("math", "abs")
    def abs(x):
        r"""Computes the absolute value of x

        Args:
            x: a QUA variable

        Returns:
            a QUA fixed
        """
        return (x,)

    @staticmethod
    @_library_function("math", "sin")
    def sin(x):
        r"""Computes $\mathrm{sin}(x)$

        Args:
            x (QUA variable of type fixed): the angle in radians

        Returns:
            a QUA fixed
        """
        return (x,)

    @staticmethod
    @_library_function("math", "cos")
    def cos(x):
        r"""Computes $\mathrm{cos}(x)$

        Args:
            x (QUA variable of type fixed): the angle in radians

        Returns:
            a QUA fixed
        """
        return (x,)

    @staticmethod
    @_library_function("math", "sum")
    def sum(x):
        r"""Computes the sum of an array x

        Args:
            x: a QUA array

        Returns:
            the sum of the array, has same type as x
        """
        return (x,)

    @staticmethod
    @_library_function("math", "max")
    def max(x):
        r"""Computes the max of an array x

        Args:
            x: a QUA array

        Returns:
            the max value of the array, has same type as x
        """
        return (x,)

    @staticmethod
    @_library_function("math", "min")
    def min(x):
        r"""Computes the min of an array x

        Args:
            x: a QUA array

        Returns:
            the min value of the array, has same type as x
        """
        return (x,)

    @staticmethod
    @_library_function("math", "argmax")
    def argmax(x):
        r"""Return the index of the maximum of an array

        Args:
            x: a QUA array

        Returns:
            the index of maximum value of array, a QUA Integer
        """
        return (x,)

    @staticmethod
    @_library_function("math", "argmin")
    def argmin(x):
        r"""Return the index of the minimum of an array

        Args:
            x: a QUA array

        Returns:
            the index of minimum value of array, a QUA Integer
        """
        return (x,)

    @staticmethod
    @_library_function("math", "dot")
    def dot(x, y):
        r"""Calculates a dot product of two QUA arrays of identical size.

        Args:
            x: a QUA array
            y: a QUA array

        Returns:
            The dot product of x and y, has same type as x and y

        Example:
            ```python
            assign(c, dot(a, b))
            ```
        """
        return x, y


class Cast:
    @staticmethod
    @_library_function("cast", "mul_int_by_fixed")
    def mul_int_by_fixed(x, y):
        r"""Multiplies an int x by a fixed y, returning an int

        Args:
            x: a QUA integer
            y: a QUA fixed

        Returns:
            a QUA int which equals x*y
        """
        return x, y

    @staticmethod
    @_library_function("cast", "mul_fixed_by_int")
    def mul_fixed_by_int(x, y):
        r"""Multiplies a fixed x by an int y, returning a fixed

        Args:
            x: a QUA fixed
            y: a QUA int

        Returns:
            a QUA fixed which equals x*y
        """
        return x, y

    @staticmethod
    @_library_function("cast", "to_int")
    def to_int(x):
        r"""Casts a variable to int. Supports int, fixed or bool

        Args:
            x: a QUA variable

        Returns:
            a QUA int
        """
        return (x,)

    @staticmethod
    @_library_function("cast", "to_fixed")
    def to_fixed(x):
        r"""Casts a variable to fixed. Supports int, fixed or bool

        Args:
            x: a QUA variable

        Returns:
            a QUA fixed
        """
        return (x,)

    @staticmethod
    @_library_function("cast", "to_bool")
    def to_bool(x):
        r"""Casts a variable to bool. Supports int, fixed or bool

        Args:
            x: a QUA variable

        Returns:
            a QUA bool
        """
        return (x,)

    @staticmethod
    @_library_function("cast", "unsafe_cast_int")
    def unsafe_cast_int(x):
        r"""Treats the given input variable, bitwise, as an integer.
        For a given fixed point number, this is equivalent to multiplying by
        $2^{28}$

        Supports int, fixed or bool.

        Args:
            x: a QUA variable

        Returns:
            a QUA int
        """
        return (x,)

    @staticmethod
    @_library_function("cast", "unsafe_cast_fixed")
    def unsafe_cast_fixed(x):
        r"""Treats the given input variable, bitwise, as a fixed point number.
        For a given integer, this is equivalent to multiplying by $2^{-28}$

        Supports int, fixed or bool.

        Args:
            x: a QUA variable

        Returns:
            a QUA fixed
        """
        return (x,)

    @staticmethod
    @_library_function("cast", "unsafe_cast_bool")
    def unsafe_cast_bool(x):
        r"""Treats the given input variable, bitwise, as a boolean.
        A boolean is determined by the right-most bit, so for a given integer, this is
        equivalent to a parity check.

        Supports int, fixed or bool.

        Warning:
            Saving a boolean number which was unsafely cast from an integer/fixed will give the wrong value in python.

        Args:
            x: a QUA variable

        Returns:
            a QUA bool
        """
        return (x,)


class Util:
    @staticmethod
    @_library_function("util", "cond")
    def cond(condition, true_result, false_result):
        r"""Quick conditional operation. This is equivalent to a ternary operator available in some languages:
        i.e. `a ? b : c`, meaning `b` if `a` is true, or `c` if `a` is false.
        There is less computation overhead (less latency) when running this operation relative to the if conditional.

        Example:
            ```python
            assign(var, cond(a, b, c)) #where a is a boolean expression
            ```
        """
        return condition, true_result, false_result


class Random:
    def __init__(self, seed=None):
        r"""A class for generating pseudo-random numbers in QUA

        Args:
            seed: Optional. An integer seed for the pseudo-random number
                generator.
        """
        self._seed = declare(int, value=seed if seed is not None else random.randrange((1 << 28) - 1))

    def set_seed(self, exp):
        r"""Set the seed for the pseudo-random number generator

        Args:
            exp: a QUA expression
        """
        assign(self._seed, exp)

    @_library_function("random", "rand_int")
    def rand_int(self, max_int):
        r"""Returns a pseudorandom integer in range [0, max_int)

        Args:
            max_int: maximum value

        Example:
            ```python
            a= Random()
            assign(b,a.rand_int(max_int))
            ```
        """
        return self._seed, max_int

    @_library_function("random", "rand_fixed")
    def rand_fixed(self):
        r"""Returns a pseudorandom fixed in range [0.0, 1.0)

        Example:
            ```python
            a= Random()
            assign(b,a.rand_fixed())
            ```
        """
        return (self._seed,)
