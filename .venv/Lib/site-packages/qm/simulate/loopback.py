import logging
from typing import List, Tuple, cast

from qm.simulate.interface import SimulatorInterface, SupportedConnectionTypes, get_opx_fem_number
from qm.grpc.frontend import (
    SimulationRequest,
    ExecutionRequestSimulateSimulationInterfaceNone,
    ExecutionRequestSimulateSimulationInterfaceLoopback,
    ExecutionRequestSimulateSimulationInterfaceLoopbackConnections,
)

logger = logging.getLogger(__name__)


class LoopbackInterface(SimulatorInterface[ExecutionRequestSimulateSimulationInterfaceLoopbackConnections]):
    """Creates a loopback interface for use in
    [qm.simulate.interface.SimulationConfig][].
    A loopback connects the output of the OPX into it's input. This can be defined
    directly using the ports or through the elements.

    Args:
        connections (list):
            List of tuples with loopback connections. Each tuple should represent physical connection between ports:

                    ``(from_controller: str, from_port: int, to_controller: str, to_port: int)``

        latency (int): The latency between the OPX outputs and its
            input.
        noisePower (float): How much noise to add to the input.

                ``(fromController: str, fromFEM: int, fromPort: int, toController: str, toFEM: int, toPort: int)``

            2. Virtual connection between elements:

                ``(fromQE: str, toQE: str, toQEInput: int)``
    :param int latency: The latency between the OPX outputs and its input.
    :param float noisePower: How much noise to add to the input.

    Example::

    >>> job = qmm.simulate(config, prog, SimulationConfig(
    >>>                   duration=20000,
    >>>                   # loopback from output 1 to input 2 of controller 1:
    >>>                   simulation_interface=LoopbackInterface([("con1", 1, "con1", 2)])
    """

    def __init__(self, connections: List[SupportedConnectionTypes], latency: int = 24, noisePower: float = 0.0):
        super().__init__(connections, noisePower)
        self._validate_latency(latency)
        self.latency = latency

    @property
    def connections(self) -> List[Tuple[str, int, int, str, int, int]]:
        connections = []
        for connection in self._connections:
            connections.append(
                (
                    connection.from_controller,
                    connection.from_fem,
                    connection.from_port,
                    connection.to_controller,
                    connection.to_fem,
                    connection.to_port,
                )
            )
        return connections

    @staticmethod
    def _validate_latency(latency: int) -> None:
        if (not isinstance(latency, int)) or latency < 0:
            raise Exception("latency must be a positive integer")

    @classmethod
    def _validate_and_standardize_single_connection(
        cls, connection: SupportedConnectionTypes
    ) -> ExecutionRequestSimulateSimulationInterfaceLoopbackConnections:
        if not connection:
            logger.warning("No loopback was defined, treating as no loopback.")
        if not isinstance(connection, tuple):
            raise Exception("each connection must be of type tuple")
        if len(connection) == 6:
            cls._validate_connection_type(
                connection,
                [str, int, int, str, int, int],
                "(from_controller, from_fem, from_port, to_controller, to_fem, to_port)",
            )
            tuple_6 = connection
            return ExecutionRequestSimulateSimulationInterfaceLoopbackConnections(
                from_controller=tuple_6[0],
                from_fem=tuple_6[1],
                from_port=tuple_6[2],
                to_controller=tuple_6[3],
                to_fem=tuple_6[4],
                to_port=tuple_6[5],
            )
        if len(connection) == 4:
            cls._validate_connection_type(
                connection, [str, int, str, int], "(from_controller, from_port, to_controller, to_port)"
            )
            tuple_4 = cast(Tuple[str, int, str, int], connection)
            return ExecutionRequestSimulateSimulationInterfaceLoopbackConnections(
                from_controller=tuple_4[0],
                from_fem=get_opx_fem_number(),
                from_port=tuple_4[1],
                to_controller=tuple_4[2],
                to_fem=get_opx_fem_number(),
                to_port=tuple_4[3],
            )
        if len(connection) == 3:
            cls._validate_connection_type(connection, [str, str, int], "(from_QE, to_QE, to_QEInput)")
            tuple_3 = cast(Tuple[str, str, int], connection)
            return ExecutionRequestSimulateSimulationInterfaceLoopbackConnections(
                from_controller=tuple_3[0],
                from_fem=-1,
                from_port=-1,
                to_controller=tuple_3[1],
                to_fem=-1,
                to_port=tuple_3[2],
            )
        raise Exception("connection should be tuple of length 3, 4 or 6")

    def update_simulate_request(
        self,
        request: SimulationRequest,
    ) -> SimulationRequest:
        if not self._connections:
            request.simulate.simulation_interface.none = ExecutionRequestSimulateSimulationInterfaceNone()
            return request

        request.simulate.simulation_interface.loopback = ExecutionRequestSimulateSimulationInterfaceLoopback(
            latency=self.latency, noise_power=self.noisePower, connections=self._connections
        )
        return request
