import ssl
import warnings
import dataclasses
from typing import Dict, Tuple, Optional

from qm.utils import deprecation_message
from qm.api.models.info import QuaMachineInfo
from qm.api.models.debug_data import DebugData
from qm.api.models.capabilities import ServerCapabilities

MAX_MESSAGE_SIZE = 1024 * 1024 * 100  # 100 mb in bytes
BASE_TIMEOUT = 60


@dataclasses.dataclass
class ConnectionDetails:
    host: str
    port: int
    user_token: Optional[str] = dataclasses.field(default=None)
    ssl_context: Optional[ssl.SSLContext] = dataclasses.field(default=None)
    max_message_size: int = dataclasses.field(default=MAX_MESSAGE_SIZE)
    headers: Dict[str, str] = dataclasses.field(default_factory=dict)
    timeout: float = dataclasses.field(default=BASE_TIMEOUT)
    debug_data: Optional[DebugData] = dataclasses.field(default=None)

    def __hash__(self) -> int:
        return hash(
            (
                self.host,
                self.port,
                self.user_token,
                self.ssl_context,
                self.max_message_size,
                tuple(sorted(self.headers.items())),
                self.timeout,
                self.debug_data,
            )
        )


@dataclasses.dataclass
class ResponseConnectionDetails:
    host: str
    port: int
    octaves: Dict[str, Tuple[str, int]]


@dataclasses.dataclass
class ServerDetails:
    port: int
    host: str
    server_version: str
    connection_details: ConnectionDetails
    octaves: Dict[str, ConnectionDetails]

    # does it implement the QUA service
    qua_implementation: Optional[QuaMachineInfo]
    capabilities: ServerCapabilities = dataclasses.field(default_factory=ServerCapabilities.build)

    @property
    def qop_version(self) -> str:
        warnings.warn(
            deprecation_message(
                method="ServerDetails.qop_version",
                deprecated_in="1.1.4",
                removed_in="1.2.0",
                details="Use ServerDetails.server_version instead.",
            ),
            DeprecationWarning,
            stacklevel=2,
        )
        return self.server_version

    def __post_init__(self) -> None:
        self.capabilities = ServerCapabilities.build(qua_implementation=self.qua_implementation)
