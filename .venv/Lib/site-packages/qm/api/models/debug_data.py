import dataclasses
from collections import deque
from typing import Deque, Union

from multidict import MultiDict

RECEIVED_HEADERS_MAX_SIZE = 10000


@dataclasses.dataclass
class DebugData:
    received_headers: Deque[MultiDict[Union[str, bytes]]] = dataclasses.field(
        default_factory=lambda: deque(maxlen=RECEIVED_HEADERS_MAX_SIZE)
    )

    def append(self, received_metadata: MultiDict[Union[str, bytes]]) -> None:
        self.received_headers.append(received_metadata)
