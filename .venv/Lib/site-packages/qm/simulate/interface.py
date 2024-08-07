import abc
from dataclasses import dataclass
from typing import Any, List, Type, Tuple, Union, Generic, TypeVar, Optional

from dependency_injector.wiring import Provide, inject

from qm.api.models.capabilities import ServerCapabilities
from qm.containers.capabilities_container import CapabilitiesContainer
from qm.grpc.frontend import (
    SimulationRequest,
    ExecutionRequestSimulateSimulationInterfaceNone,
    ExecutionRequestSimulateSimulationInterfaceLoopbackConnections,
    ExecutionRequestSimulateSimulationInterfaceRawInterfaceConnections,
)

SupportedConnectionTypes = Union[
    Tuple[str, int, int, str, int, int],
    Tuple[str, int, str, int],
    Tuple[str, str, int],
    Tuple[str, int, int, List[float]],
    Tuple[str, int, List[float]],
]


T = TypeVar(
    "T",
    ExecutionRequestSimulateSimulationInterfaceLoopbackConnections,
    ExecutionRequestSimulateSimulationInterfaceRawInterfaceConnections,
)


class SimulatorInterface(Generic[T], metaclass=abc.ABCMeta):
    def __init__(self, connections: List[SupportedConnectionTypes], noisePower: float = 0.0):
        self.noisePower = self._validate_and_standardize_noise_power(noisePower)
        self._connections: List[T] = self._validate_and_standardize_connections(connections)

    @abc.abstractmethod
    def update_simulate_request(self, request: SimulationRequest) -> SimulationRequest:
        pass

    @staticmethod
    def _validate_connection_type(connection: Tuple[Any, ...], types: List[Type[Any]], expected_input: str) -> None:
        if not all(isinstance(c, t) for c, t in zip(connection, types)):
            raise Exception(f"connection should be {expected_input}")

    @staticmethod
    def _validate_and_standardize_noise_power(noise_power: float) -> float:
        if (not isinstance(noise_power, (int, float))) or noise_power < 0:
            raise Exception("noisePower must be a positive number")
        return float(noise_power)

    @classmethod
    def _validate_and_standardize_connections(cls, connections: List[SupportedConnectionTypes]) -> List[T]:
        if not isinstance(connections, list):
            raise Exception("connections argument must be of type list")
        standardized_connections = []
        for connection in connections:
            standardized_connections.append(cls._validate_and_standardize_single_connection(connection))
        return standardized_connections

    @classmethod
    @abc.abstractmethod
    def _validate_and_standardize_single_connection(cls, connection: SupportedConnectionTypes) -> T:
        pass


@inject
def get_opx_fem_number(capabilities: ServerCapabilities = Provide[CapabilitiesContainer.capabilities]) -> int:
    """This function is here to overcome a bug in the GW, that expects the FEM to be 0"""
    return capabilities.fem_number_in_simulator


SimulationInterfaceTypes = Union[
    SimulatorInterface[ExecutionRequestSimulateSimulationInterfaceLoopbackConnections],
    SimulatorInterface[ExecutionRequestSimulateSimulationInterfaceRawInterfaceConnections],
]


class SimulationConfig:
    """Creates a configuration object to pass to
    [qm.quantum_machines_manager.QuantumMachinesManager.simulate][]

    Args:
        duration (int): The duration to run the simulation for, in clock
            cycles
        include_analog_waveforms (bool): True to collect simulated
            analog waveform names
        include_digital_waveforms (bool): True to collect simulated
            digital waveform names
        simulation_interface (SimulatorInterface):
            Interface for to simulator. Currently supported interfaces
            - ``None`` - Zero inputs
            - [qm.simulate.loopback.LoopbackInterface][] - Loopback output to input
            - [qm.simulate.raw.RawInterface][] - Specify samples for inputs
        controller_connections (List[ControllerConnection]): A list of
            connections between the controllers in the config
        extraProcessingTimeoutInMs (int): timeout in ms to wait for
            stream processing to finish. Default is -1, which is
            disables the timeout

    """

    duration = 0
    simulate_analog_outputs = False

    def __init__(
        self,
        duration: int = 0,
        include_analog_waveforms: bool = False,
        include_digital_waveforms: bool = False,
        simulation_interface: Optional[SimulationInterfaceTypes] = None,
        controller_connections: Optional[List["ControllerConnection"]] = None,
        extraProcessingTimeoutInMs: int = -1,
    ):
        if controller_connections is None:
            controller_connections = []
        super(SimulationConfig, self).__init__()
        self.duration = duration
        self.include_analog_waveforms = include_analog_waveforms is True
        self.include_digital_waveforms = include_digital_waveforms is True
        self.simulation_interface = simulation_interface
        self.controller_connections = controller_connections
        self.extraProcessingTimeoutInMs = extraProcessingTimeoutInMs

    def update_simulate_request(self, request: SimulationRequest) -> SimulationRequest:
        if self.simulation_interface is None:
            request.simulate.simulation_interface.none = ExecutionRequestSimulateSimulationInterfaceNone()
        else:
            request = self.simulation_interface.update_simulate_request(request)
        return request


@dataclass
class InterOpxAddress:
    """Args:
    controller (str): The name of the controller
    is_left_connection (bool)
    """

    controller: str
    is_left_connection: bool


@dataclass
class InterOpxChannel:
    """Args:
    controller (str): The name of the controller
    channel_number (int)
    """

    controller: str
    channel_number: int


InterOpxPairing = Union[InterOpxAddress, InterOpxChannel]


@dataclass
class ControllerConnection:
    source: InterOpxPairing
    target: InterOpxPairing
