from qm.program.program import Program
from qm.utils.deprecation_utils import throw_warning

_Program = Program

throw_warning(
    "'qm.program._Program' is moved as of 1.1.0 and will be removed in 1.2.0. " "use 'qm.Program' instead",
    category=DeprecationWarning,
    stacklevel=2,
)
