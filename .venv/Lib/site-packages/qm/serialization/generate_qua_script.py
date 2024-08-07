import sys
import types
import logging
import datetime
import traceback
from typing import Any, Dict, List, Mapping, Optional

import betterproto
import numpy as np
from marshmallow import ValidationError

from qm.grpc import qua
from qm.program import load_config
from qm.grpc.qua_config import QuaConfig
from qm.utils.protobuf_utils import Node
from qm import Program, DictQuaConfig, version
from qm.program.ConfigBuilder import convert_msg_to_config
from qm.serialization.qua_node_visitor import QuaNodeVisitor
from qm.utils.list_compression_utils import Chunk, split_list_to_chunks
from qm.serialization.qua_serializing_visitor import QuaSerializingVisitor
from qm.grpc.qua import QuaProgram, QuaResultAnalysis, QuaProgramCompilerOptions
from qm.exceptions import ConfigValidationException, ConfigSerializationException

SERIALIZATION_VALIDATION_ERROR = "SERIALIZATION VALIDATION ERROR"

LOADED_CONFIG_ERROR = "LOADED CONFIG SERIALIZATION ERROR"

CONFIG_ERROR = "CONFIG SERIALIZATION ERROR"

SERIALIZATION_NOT_COMPLETE = "SERIALIZATION WAS NOT COMPLETE"


logger = logging.getLogger(__name__)


def standardize_program_for_comparison(prog: QuaProgram) -> QuaProgram:
    """There are things in the PB model that if they are different, the programs behaves exactly the same.
    These 3 things are
    1. the value of the loc field, that tells where the command was defined
    2. the names of the variables, as long as the commands are the same.
    3. the order of the variables in the result analysis
    """
    prog.result_analysis = QuaResultAnalysis().from_dict(prog.result_analysis.to_dict())
    prog.compiler_options = QuaProgramCompilerOptions()
    StripLocationVisitor.strip(prog)
    RenameStreamVisitor().visit(prog)
    prog.result_analysis.model = sorted(prog.result_analysis.model, key=str)
    return prog


def assert_programs_are_equal(prog1: QuaProgram, prog2: QuaProgram) -> None:
    prog1 = standardize_program_for_comparison(prog1)
    prog2 = standardize_program_for_comparison(prog2)
    assert prog1 == prog2


def generate_qua_script(prog: Program, config: Optional[DictQuaConfig] = None) -> str:
    if prog.is_in_scope():
        raise RuntimeError("Can not generate script inside the qua program scope")

    proto_config = None
    if config is not None:
        try:
            proto_config = load_config(config)
        except (ConfigValidationException, ValidationError) as e:
            raise RuntimeError("Can not generate script - bad config") from e
        except AttributeError:
            logger.warning("Could not generate a loaded config. Maybe there is no `QuantumMachinesManager` instance?")

    proto_prog = prog.qua_program
    return _generate_qua_script_pb(proto_prog, proto_config, config)


def _generate_qua_script_pb(
    proto_prog: QuaProgram, proto_config: Optional[QuaConfig], original_config: Optional[DictQuaConfig]
) -> str:
    extra_info = ""
    serialized_program = ""
    pretty_original_config = None

    if original_config is not None:
        try:
            pretty_original_config = _print_config(original_config)
        except Exception as e:
            trace = traceback.format_exception(*sys.exc_info())
            extra_info = extra_info + _error_string(e, trace, CONFIG_ERROR)
            pretty_original_config = f"{original_config}"

    pretty_proto_config = None
    if proto_config is not None:
        try:
            normalized_config = convert_msg_to_config(proto_config)
            pretty_proto_config = _print_config(normalized_config)
        except Exception as e:
            trace = traceback.format_exception(*sys.exc_info())
            extra_info = extra_info + _error_string(e, trace, LOADED_CONFIG_ERROR)

    try:
        visitor = QuaSerializingVisitor()
        visitor.visit(proto_prog)
        serialized_program = visitor.out()

        extra_info = extra_info + _validate_program(proto_prog, serialized_program)
    except Exception as e:
        trace = traceback.format_exception(*sys.exc_info())
        extra_info = extra_info + _error_string(e, trace, SERIALIZATION_VALIDATION_ERROR)

    return f"""
# Single QUA script generated at {datetime.datetime.now()}
# QUA library version: {version.__version__}

{serialized_program}
{extra_info if extra_info else ""}
config = {pretty_original_config}

loaded_config = {pretty_proto_config}

"""


def _validate_program(old_prog: QuaProgram, serialized_program: str) -> str:
    generated_mod = types.ModuleType("gen")
    exec(serialized_program, generated_mod.__dict__)
    new_prog = generated_mod.prog.qua_program

    try:
        assert_programs_are_equal(old_prog, new_prog)
        return ""
    except AssertionError:

        new_prog_str = _program_string(new_prog)
        old_prog_str = _program_string(old_prog)
        new_prog_str = new_prog_str.replace("\n", "")
        old_prog_str = old_prog_str.replace("\n", "")
        return f"""

####     {SERIALIZATION_NOT_COMPLETE}     ####
#
#  Original   {old_prog_str}
#  Serialized {new_prog_str}
#
################################################

        """


def _error_string(e: Exception, trace: List[str], error_type: str) -> str:
    return f"""

    ####     {error_type}     ####
    #
    #  {str(e)}
    #
    # Trace:
    #   {str(trace)}
    #
    ################################################

            """


def _program_string(prog: QuaProgram) -> str:
    """Will create a canonized string representation of the program"""
    strip_location_visitor = StripLocationVisitor()
    strip_location_visitor.visit(prog)
    string = prog.to_json(2)
    return string


def _print_config(config_part: Mapping[str, Any], indent_level: int = 1) -> str:
    """Formats a python dictionary into an executable string representation.
    Unlike pretty print, it better supports nested dictionaries. Also, auto converts
    lists into a more compact form.
    Works recursively.
    :param Dict[str, Any] config_part: The dictionary to format

    Args:
        indent_level (int): Internally used by the function to indicate
            the current
    indention
    :returns str: The string representation of the dictionary.
    """
    if indent_level > 100:
        raise ConfigSerializationException("Reached maximum depth of config pretty print")

    config_part_str = ""
    if len(config_part) > 0:
        config_part_str += "{\n"

        for key, value in config_part.items():
            config_part_str += "    " * indent_level + f'"{str(key)}": ' + _value_to_str(indent_level, value)

        if indent_level > 1:
            # add an indentation and go down a line
            config_part_str += "    " * (indent_level - 1) + "},\n"
        else:
            # in root indent level, no need to add a line
            config_part_str += "}"

    else:
        config_part_str = "{},\n"

    return config_part_str


def _value_to_str(indent_level: int, value: Any) -> str:
    # To support numpy types, we convert them to normal python types:
    if type(value).__module__ == np.__name__:
        value = value.tolist()

    is_long_list = isinstance(value, list) and len(value) > 1

    if isinstance(value, dict):
        return _print_config(value, indent_level + 1)
    elif isinstance(value, str):
        return f'"{value}"' + ",\n"
    elif is_long_list and isinstance(value[0], dict):
        temp_str = "[\n"
        for v in value:
            temp_str += "    " * (indent_level + 1) + f"{str(v)},\n"
        temp_str += "    " * indent_level + "],\n"
        return temp_str
    elif is_long_list:
        # replace it with a compact list
        is_single_value = len(set(value)) == 1

        if is_single_value:
            return f"[{value[0]}] * {len(value)}" + ",\n"
        else:
            return f"{_make_compact_string_from_list(value)}" + ",\n"
    else:
        # python basic data types string representation are valid python
        return str(value) + ",\n"


def _serialize_chunks(chunks: List[Chunk[object]]) -> str:
    return " + ".join([str(chunk) for chunk in chunks])


def _make_compact_string_from_list(list_data: List[object]) -> str:
    """
    Turns a multi-value list into the most compact string representation of it,
    replacing identical consecutive values by list multiplication.
    """
    chunks = split_list_to_chunks(list_data)
    return _serialize_chunks(chunks)


class StripLocationVisitor(QuaNodeVisitor):
    """Go over all nodes and if they have a location property, we strip it"""

    def _default_enter(self, node: Node) -> bool:
        if hasattr(node, "loc"):
            node.loc = "stripped"
        return isinstance(node, betterproto.Message)

    @staticmethod
    def strip(node: Node) -> None:
        StripLocationVisitor().visit(node)


class RenameStreamVisitor(QuaNodeVisitor):
    """This class standardizes the names of the streams, so when comparing two programs, the names will be the same"""

    def __init__(self) -> None:
        self._max_n = 0
        self._old_to_new_map: Dict[str, str] = {}

    def _change_var_name(self, curr_s: str) -> str:
        if curr_s in self._old_to_new_map:
            return self._old_to_new_map[curr_s]
        non_digits = "".join([s for s in curr_s if not s.isdigit()])
        new_name = non_digits + str(self._max_n)
        self._max_n += 1
        self._old_to_new_map[curr_s] = new_name
        return new_name

    def visit_qm_grpc_qua_QuaProgramMeasureStatement(self, node: qua.QuaProgramMeasureStatement) -> None:
        if node.stream_as:
            node.stream_as = self._change_var_name(node.stream_as)
        if node.timestamp_label:
            node.timestamp_label = self._change_var_name(node.timestamp_label)

    def visit_qm_grpc_qua_QuaProgramSaveStatement(self, node: qua.QuaProgramSaveStatement) -> None:
        if node.tag:
            node.tag = self._change_var_name(node.tag)

    def _default_enter(self, node: Node) -> bool:
        """This function is for the Value of betterproto. There is a chance we can visit the object directly"""
        if hasattr(node, "string_value") and node.string_value and node.string_value in self._old_to_new_map:
            node.string_value = self._old_to_new_map[node.string_value]
        return isinstance(node, betterproto.Message)
