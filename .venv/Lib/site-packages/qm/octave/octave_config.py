import re
import logging
import warnings
import dataclasses
from typing import Any, Dict, List, Tuple, Union, Generic, TypeVar, Optional

from octave_sdk import OctaveOutput, OctaveLOSource

from qm.utils import SERVICE_HEADER_NAME
from qm.type_hinting.general import PathLike
from qm.exceptions import OctaveConnectionError
from qm.api.models.capabilities import OPX_FEM_IDX
from qm.octave.calibration_db import CalibrationDB
from qm.type_hinting.config_types import StandardPort
from qm.api.models.server_details import ConnectionDetails

logger = logging.getLogger(__name__)

ConnectionMapping = Dict[StandardPort, Tuple[str, str]]

DEFAULT_CONNECTIONS = {
    1: "I1",
    2: "Q1",
    3: "I2",
    4: "Q2",
    5: "I3",
    6: "Q3",
    7: "I4",
    8: "Q4",
    9: "I5",
    10: "Q5",
}


PortType = TypeVar("PortType", OctaveOutput, OctaveLOSource)


@dataclasses.dataclass
class LoopbackInfo(Generic[PortType]):
    name: str
    octave_port: PortType

    def __hash__(self) -> int:
        return hash((self.name, self.octave_port))


def _convert_octave_port_to_number(port: str) -> int:
    if port.startswith(tuple("IQ")) and port.endswith(tuple("12345")) and len(port) == 2:
        return int(port[-1])
    raise ValueError(f"port {port} is not a valid octave port")


def _convert_number_to_octave_port(name: str, port: int) -> List[Tuple[str, str]]:
    return [(name, f"I{port}"), (name, f"Q{port}")]


class QmOctaveConfig:
    """
    Holds connectivity and calibrations database information
    """

    def __init__(self, fan: Any = None):
        self._devices: Dict[str, ConnectionDetails] = {}
        self._calibration_db_path: Optional[str] = None
        self._loopbacks: Optional[Dict[LoopbackInfo[OctaveLOSource], LoopbackInfo[OctaveOutput]]] = None
        self._opx_octave_port_mapping: Optional[ConnectionMapping] = None
        self._calibration_db: Optional[CalibrationDB] = None
        self._fan = fan
        self._connection_headers: Dict[str, str] = {}

    @property
    def connection_headers(self) -> Dict[str, str]:
        return self._connection_headers

    @property
    def fan(self) -> Any:
        return self._fan

    def add_device_info(
        self,
        name: str,
        host: str,
        port: int,
    ) -> None:
        """Sets the octave info  - the IP address can be either the router ip or the actual ip
        depends on the installation configuration (cluster or standalone mode)

        In order to add more than one octave run the function with different octave names ips and ports as the number of octaves in the cluster

        Args:
            name (str): The octave name
            host (str): The octave/QOP ip
            port (int): The octave port
        """
        # can be either the router ip or the actual ip (depends on what we have)
        self._devices[name] = ConnectionDetails(host, port, headers={SERVICE_HEADER_NAME: name})

    def add_device(self, name: str, details: ConnectionDetails) -> None:
        self._devices[name] = details

    def get_devices(self) -> Dict[str, ConnectionDetails]:
        return self._devices

    @property
    def devices(self) -> Dict[str, ConnectionDetails]:
        return self._devices

    def set_calibration_db(self, path: PathLike) -> None:
        """Sets the path to the calibration database

        Args:
            path (str): path to the calibration database
        """
        self._calibration_db_path = str(path)
        self._calibration_db = CalibrationDB(self._calibration_db_path)

    @staticmethod
    def _check_connection_format(connection: Tuple[str, Union[int, str]]) -> bool:
        return isinstance(connection, tuple) and len(connection) == 2 and isinstance(connection[0], str)

    def set_opx_octave_mapping(self, mappings: List[Tuple[str, str]]) -> None:
        """Sets the default port mapping for each `opx, octave` names

        Will be deprecated soon, should use the "connectivity" key in "controllers" inside the configuration

        Args:
            mappings: list of tuples of [OPX_name, octave_name] to connect
        """
        warnings.warn(
            "OctaveConfig.set_opx_octave_mapping is deprecated as of 1.1.6 and will be removed in 1.2.0. "
            "The port mapping was moved to the QUA-config. Please set the mapping there.",
            DeprecationWarning,
            stacklevel=2,
        )
        if self._opx_octave_port_mapping is None:
            self._opx_octave_port_mapping = {}

        if self._opx_octave_port_mapping:
            logger.warning("Setting a new opx-octave port mapping, your configured mapping will be overridden!")

        for opx_name, octave_name in mappings:
            self._opx_octave_port_mapping.update(self.get_default_opx_octave_port_mapping(opx_name, octave_name))

    def add_opx_octave_port_mapping(
        self, connections: Dict[Union[StandardPort, Tuple[str, int]], Tuple[str, str]]
    ) -> None:
        """
        Adds port mapping which is different from the default one. should be in the form:
        ```
        {('con1', 1): ('oct1', 'I1'),
        ('con1', 2): ('oct1', 'Q1'),
        ('con1', 3): ('oct1', 'I2'),
        ('con1', 4): ('oct1', 'Q2'),
        ('con1', 5): ('oct1', 'I3'),
        ('con1', 6): ('oct1', 'Q3'),
        ('con1', 7): ('oct1', 'I4'),
        ('con1', 8): ('oct1', 'Q4'),
        ('con1', 9): ('oct1', 'I5'),
        ('con1', 10): ('oct1', 'Q5')}
        ```

        Will be deprecated soon, should use the "connectivity" key in "controllers" inside the configuration

        Args:
            connections (ConnectionMapping): mapping of OPXs to octaves connections
        """
        # ("con1", 1): ("octave1", "I1")
        # validate structure:

        warnings.warn(
            "OctaveConfig.add_opx_octave_port_mapping is deprecated as of 1.1.6 and will be removed in 1.2.0. "
            "The port mapping was moved to the QUA-config. Please set the mapping there.",
            DeprecationWarning,
            stacklevel=2,
        )

        if self._opx_octave_port_mapping is None:
            self._opx_octave_port_mapping = {}

        standardized_connections = {}

        for key, octave_connection in connections.items():
            pattern = re.compile("([IQ])([12345])")
            if not (
                self._check_connection_format(octave_connection)
                and isinstance(octave_connection[1], str)
                and pattern.match(octave_connection[1]) is not None
            ):
                raise ValueError(
                    f"value {octave_connection} is not according to format " f'("octave_name", "octave_port")'
                )
            if len(key) == 2:
                standard_key = (key[0], OPX_FEM_IDX, key[1])
            else:
                standard_key = key
            standardized_connections[standard_key] = octave_connection
        self._opx_octave_port_mapping.update(standardized_connections)

    def get_opx_octave_port_mapping(self) -> ConnectionMapping:
        """Get the configured opx-octave connections

        Returns:
            Mapping of the configured OPXs to octaves connections
        """
        if self._opx_octave_port_mapping is None:
            return {}
        warnings.warn(
            "Setting the mapping was move to the QUA-config. "
            "It is deprecated since 1.1.6 and will be removed in 1.2.0."
            "Please set the mapping there.",
            DeprecationWarning,
            stacklevel=2,
        )
        return self._opx_octave_port_mapping

    @staticmethod
    def get_default_opx_octave_port_mapping(controller_name: str, octave_name: str) -> ConnectionMapping:
        """
        Get the default opx-octave connections

        Args:
            controller_name (str): OPX name
            octave_name (str): octave name

        Returns:
            Mapping of the given OPX to the given octave
        """
        default_connections = {}
        for opx_port, octave_port in DEFAULT_CONNECTIONS.items():
            default_connections[(controller_name, OPX_FEM_IDX, opx_port)] = (octave_name, octave_port)
        return default_connections

    @property
    def calibration_db(self) -> Optional[CalibrationDB]:
        return self._calibration_db

    def add_lo_loopback(
        self,
        octave_output_name: str,
        octave_output_port: OctaveOutput,
        octave_input_name: str,
        octave_input_port: OctaveLOSource,
    ) -> None:
        """Adds a loopback between an OctaveOutput and an OctaveLOSource

        Args:
            octave_output_name (str): octave name
            octave_output_port (OctaveOutput): octave output port
                according to OctaveOutput
            octave_input_name (str): octave name
            octave_input_port (OctaveLOSource): the LO input port
                according to OctaveLOSource
        """
        warnings.warn(
            "OctaveConfig.add_lo_loopback is deprecated as of 1.1.6 and will be removed in 1.2.0. "
            "Please set the loopbacks there.",
            DeprecationWarning,
            stacklevel=2,
        )
        if self._loopbacks is None:
            self._loopbacks = {}

        if octave_output_name != octave_input_name:
            raise ValueError("lo loopback between different octave devices are not supported")
        loop_back_source = LoopbackInfo(octave_output_name, octave_output_port)
        loop_back_destination = LoopbackInfo(octave_input_name, octave_input_port)
        self._loopbacks[loop_back_destination] = loop_back_source

    def get_lo_loopbacks_by_octave(self, octave_name: str) -> Dict[OctaveLOSource, OctaveOutput]:
        """
        Gets a list of all loop backs by octave name

        Args:
            octave_name (str): octave name to get LO loopback for

        Returns:
            Dictionary with all the LO loopbacks
        """
        if self._loopbacks is None:
            return {}

        warnings.warn(
            "Loopbacks were moved to the QUA-config, move them there",
            DeprecationWarning,
            stacklevel=2,
        )
        result = {}
        for destination, source in self._loopbacks.items():
            if destination.name == octave_name:
                result[destination.octave_port] = source.octave_port
        return result

    def get_opx_iq_ports(self, octave_output_port: Tuple[str, int]) -> Tuple[StandardPort, StandardPort]:
        conns = self.get_opx_octave_port_mapping()
        inv_conns = {v: k for k, v in conns.items()}
        octave_input_port_i, octave_input_port_q = _convert_number_to_octave_port(
            octave_output_port[0], octave_output_port[1]
        )
        if octave_input_port_i not in inv_conns:
            octave_name, octave_port = octave_input_port_i
            raise KeyError(f"Could not find opx connections to port " f"'{octave_port}' of octave '{octave_name}'")

        if octave_input_port_q not in inv_conns:
            octave_name, octave_port = octave_input_port_q
            raise KeyError(f"Could not find opx connections to port " f"'{octave_port}' of octave '{octave_name}'")
        return inv_conns[octave_input_port_i], inv_conns[octave_input_port_q]

    def get_octave_input_port(
        self,
        opx_i_port: StandardPort,
        opx_q_port: StandardPort,
    ) -> Optional[Tuple[str, int]]:
        # check both ports are going to the same mixer
        connections = self.get_opx_octave_port_mapping()
        i_octave_port = connections.get(opx_i_port)
        q_octave_port = connections.get(opx_q_port)

        if i_octave_port is None and q_octave_port is None:
            return None

        if i_octave_port is None and q_octave_port is not None:
            raise OctaveConnectionError("I port is not connected to any octave and Q port is connected to an octave")
        if i_octave_port is not None and q_octave_port is None:
            raise OctaveConnectionError("Q port is not connected to any octave and I port is connected to an octave")
        assert i_octave_port is not None
        assert q_octave_port is not None
        if i_octave_port[0] != q_octave_port[0]:
            raise OctaveConnectionError("I and Q are not connected to the same octave")
        if i_octave_port[1][-1] != q_octave_port[1][-1]:
            raise OctaveConnectionError("I and Q are not connected to the same octave input")

        return i_octave_port[0], _convert_octave_port_to_number(i_octave_port[1])
