import warnings
import dataclasses
from pathlib import Path
from typing import List, Union, Optional

from qm import DictQuaConfig
from qm.grpc.qua_config import QuaConfig
from qm.program._qua_config_schema import load_config
from qm.program._ResultAnalysis import _ResultAnalysis
from qm.program.StatementsCollection import StatementsCollection
from qm.grpc.qua import (
    QuaProgram,
    QuaProgramType,
    QuaProgramScript,
    QuaResultAnalysis,
    QuaProgramVarDeclaration,
    QuaProgramLiteralExpression,
    QuaProgramStatementsCollection,
)


@dataclasses.dataclass
class ProgramMetadata:
    uses_command_timestamps: bool
    uses_fast_frame_rotation: bool


class Program:
    def __init__(
        self,
        config: Optional[QuaConfig] = None,
        program: Optional[QuaProgram] = None,
    ):
        if program is None:
            program = QuaProgram(
                script=QuaProgramScript(variables=[], body=QuaProgramStatementsCollection(statements=[])),
                result_analysis=QuaResultAnalysis(model=[]),
            )

        self._program = program
        self._qua_config = config
        self._result_analysis = _ResultAnalysis(self._program.result_analysis)
        self._is_in_scope = False
        self._metadata = ProgramMetadata(uses_command_timestamps=False, uses_fast_frame_rotation=False)

    def _declare_var(
        self,
        name: str,
        var_type: QuaProgramType,
        size: int,
        value: Union[QuaProgramLiteralExpression, List[QuaProgramLiteralExpression]],
        dim: int,
        is_input_stream: bool,
    ) -> None:
        if not isinstance(value, list):
            value = [value]
        declaration = QuaProgramVarDeclaration(
            name=name,
            type=var_type,
            size=size,
            dim=dim,
            is_input_stream=is_input_stream,
            value=list(value),
        )
        self._program.script.variables.append(declaration)

    def add_declaration(self, declaration: QuaProgramVarDeclaration) -> None:
        self._program.script.variables.append(declaration)

    def declare_int(
        self,
        name: str,
        size: int,
        value: Union[QuaProgramLiteralExpression, List[QuaProgramLiteralExpression]],
        dim: int,
        is_input_stream: bool,
    ) -> None:
        self._declare_var(name, QuaProgramType.INT, size, value, dim, is_input_stream)

    def declare_real(
        self,
        name: str,
        size: int,
        value: Union[QuaProgramLiteralExpression, List[QuaProgramLiteralExpression]],
        dim: int,
        is_input_stream: bool,
    ) -> None:
        self._declare_var(name, QuaProgramType.REAL, size, value, dim, is_input_stream)

    def declare_bool(
        self,
        name: str,
        size: int,
        value: Union[QuaProgramLiteralExpression, List[QuaProgramLiteralExpression]],
        dim: int,
        is_input_stream: bool,
    ) -> None:
        self._declare_var(name, QuaProgramType.BOOL, size, value, dim, is_input_stream)

    @property
    def body(self) -> StatementsCollection:
        return StatementsCollection(self._program.script.body)

    @property
    def result_analysis(self) -> _ResultAnalysis:
        return self._result_analysis

    @property
    def qua_program(self) -> QuaProgram:
        return self._program

    def build(self, config: QuaConfig) -> QuaProgram:
        warnings.warn(
            "Program.build() is deprecated and will be removed in 1.2.0, " "please use the property qua_program`",
            category=DeprecationWarning,
            stacklevel=2,
        )
        copy = QuaProgram().from_dict(self._program.to_dict())
        copy.config = QuaConfig().from_dict(config.to_dict())
        return copy

    def to_protobuf(self, config: DictQuaConfig) -> bytes:
        """
        Serialize the program to a protobuf binary.
        """
        loaded_config = load_config(config)
        return bytes(self.build(loaded_config))

    @classmethod
    def from_protobuf(cls, binary: bytes) -> "Program":
        """
        Deserialize the program from a protobuf binary.
        """
        program = QuaProgram().parse(binary)
        return cls(program=program, config=program.config)

    def to_file(self, path: Union[str, Path], config: DictQuaConfig) -> None:
        """
        Serialize the program to a protobuf binary and write it to a file.
        """
        if isinstance(path, str):
            path = Path(path)
        path.write_bytes(self.to_protobuf(config))

    @classmethod
    def from_file(cls, path: Union[str, Path]) -> "Program":
        """
        Deserialize the program from a protobuf binary file.
        """
        if isinstance(path, str):
            path = Path(path)
        return cls.from_protobuf(path.read_bytes())

    def set_in_scope(self) -> None:
        self._is_in_scope = True

    def set_exit_scope(self) -> None:
        self._is_in_scope = False

    def is_in_scope(self) -> bool:
        return self._is_in_scope

    @property
    def metadata(self) -> ProgramMetadata:
        return self._metadata

    def set_metadata(
        self,
        uses_command_timestamps: Optional[bool] = None,
        uses_fast_frame_rotation: Optional[bool] = None,
    ) -> None:
        if uses_command_timestamps is not None:
            self._metadata.uses_command_timestamps = uses_command_timestamps
        if uses_fast_frame_rotation is not None:
            self.metadata.uses_fast_frame_rotation = uses_fast_frame_rotation
