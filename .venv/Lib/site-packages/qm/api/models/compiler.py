import warnings
from typing import List, Optional
from dataclasses import field, dataclass

from qm.grpc.qua import QuaProgramCompilerOptions


@dataclass
class CompilerOptionArguments:
    strict: Optional[bool] = field(default=None)

    flags: List[str] = field(default_factory=list)


def get_request_compiler_options(
    compiler_options: CompilerOptionArguments,
) -> QuaProgramCompilerOptions:
    flags = compiler_options.flags
    if compiler_options.strict:
        flags.append("strict")

    return QuaProgramCompilerOptions(flags=compiler_options.flags)


def standardize_compiler_params(
    compiler_options: Optional[CompilerOptionArguments],
    strict: Optional[bool],
    flags: Optional[List[str]],
) -> CompilerOptionArguments:
    if compiler_options is not None:
        if (strict is not None) or (flags is not None):
            raise ValueError("Please remove **kwargs ('flags' and 'strict') from calling to 'simulate'")
        return compiler_options

    if (strict is not None) or (flags is not None):
        warnings.warn(
            "Using **kwargs for the compiler arguments is deprecated. "
            "Please set the options inside the object 'CompilerOptionArguments'.",
            DeprecationWarning,
            stacklevel=2,
        )
        return CompilerOptionArguments(strict=strict, flags=flags or [])

    return CompilerOptionArguments()
