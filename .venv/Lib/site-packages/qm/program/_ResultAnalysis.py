from typing import TYPE_CHECKING, List, Union, Sequence

from betterproto.lib.google.protobuf import Value, ListValue

from qm.grpc.qua import QuaResultAnalysis

if TYPE_CHECKING:
    from qm.qua._dsl import _ResultSource


class _OutputStream:
    def __init__(self, input_stream: "_ResultSource", operator_array: Sequence[str], tag: str):
        self._input_stream = input_stream
        self._operator_array: Sequence[Union[List[str], str]] = operator_array
        self.tag = tag

    def to_proto(self) -> List[Union[List[str], str]]:
        return list(self._operator_array) + [self._input_stream._to_proto()]


class _ResultAnalysis:
    def __init__(self, result_analysis: QuaResultAnalysis):
        self._result_analysis = result_analysis
        self._saves: List[_OutputStream] = []

    def _add_output_stream(self, tag: str, expression: "_ResultSource", operator_array: List[str]) -> None:
        for save in self._saves:
            if save.tag == tag:
                raise Exception("can not save two streams with the same tag")
        self._saves.append(_OutputStream(expression, operator_array, tag))

    def save(self, tag: str, expression: "_ResultSource") -> None:
        self._add_output_stream(tag, expression, operator_array=["save", tag])

    def save_all(self, tag: str, expression: "_ResultSource") -> None:
        self._add_output_stream(tag, expression, operator_array=["saveAll", tag])

    def auto_save_all(self, tag: str, expression: "_ResultSource") -> None:
        self._add_output_stream(tag, expression, operator_array=["saveAll", tag, "auto"])

    def _add_pipeline(self, output: _OutputStream) -> None:
        proto_output = output.to_proto()
        value = _to_list_value(proto_output)
        self._result_analysis.model.append(value)

    def generate_proto(self) -> None:
        for save in self._saves:
            self._add_pipeline(save)


def _to_list_value(from_list: Sequence[Union[str, List[str]]]) -> ListValue:
    res = ListValue()
    for item in from_list:
        if isinstance(item, str):
            res.values.append(Value(string_value=item))
        elif isinstance(item, list):
            res.values.append(Value(list_value=_to_list_value(item)))
    return res
