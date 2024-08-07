import logging
import dataclasses
from typing_extensions import runtime_checkable
from typing import Dict, Union, Iterable, Protocol, cast

import betterproto

from qm.grpc.general_messages import MessageLevel

LOG_LEVEL_MAP = {
    MessageLevel.Message_LEVEL_ERROR: logging.ERROR,
    MessageLevel.Message_LEVEL_WARNING: logging.WARN,
    MessageLevel.Message_LEVEL_INFO: logging.INFO,
}


Node = Union[betterproto.Message, Iterable["Node"]]


@runtime_checkable
@dataclasses.dataclass
class DataclassProtocol(Protocol):
    pass


def list_fields(node: Node) -> Dict[str, Node]:
    fields = dataclasses.fields(cast(DataclassProtocol, node))
    output = {}
    for field in fields:
        field_value = getattr(node, field.name)
        if isinstance(field_value, Iterable) or (
            isinstance(field_value, betterproto.Message) and betterproto.serialized_on_wire(field_value)
        ):
            output[field.name] = field_value
    return output
