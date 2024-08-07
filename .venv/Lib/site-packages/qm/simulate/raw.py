from typing import List, Tuple, cast

from qm.simulate.interface import SimulatorInterface, SupportedConnectionTypes, get_opx_fem_number
from qm.grpc.frontend import (
    SimulationRequest,
    ExecutionRequestSimulateSimulationInterfaceRawInterface,
    ExecutionRequestSimulateSimulationInterfaceRawInterfaceConnections,
)


class RawInterface(SimulatorInterface[ExecutionRequestSimulateSimulationInterfaceRawInterfaceConnections]):
    """Creates a raw interface for use in [qm.simulate.interface.SimulationConfig][].
    A raw interface defines samples that will be inputted into the OPX inputs.

    Args:
        connections (list):

            List of tuples with the connection. Each tuple should be:

                ``(toController: str, toFEM: int, toPort: int, toSamples: List[float])``
    :param float noisePower: How much noise to add to the input.

    Example:
        ```python
        job = qmm.simulate(config, prog, SimulationConfig(
                          duration=20000,
                          # 500 ns of DC 0.2 V into con1 input 1
                          simulation_interface=RawInterface([("con1", 1, [0.2]*500)])
        ```
    """

    @property
    def connections(self) -> List[Tuple[str, int, int, List[float]]]:
        connections = []
        for connection in self._connections:
            connections.append(
                (connection.from_controller, connection.from_fem, connection.from_port, connection.to_samples)
            )
        return connections

    @classmethod
    def _validate_and_standardize_single_connection(
        cls, connection: SupportedConnectionTypes
    ) -> ExecutionRequestSimulateSimulationInterfaceRawInterfaceConnections:
        if not isinstance(connection, tuple):
            raise Exception("each connection must be of type tuple")
        if len(connection) == 4:
            cls._validate_connection_type(
                connection, [str, int, str, list], "(from_controller, from_fem, from_port, to_samples)"
            )
            tuple_4 = cast(Tuple[str, int, int, List[float]], connection)
            return ExecutionRequestSimulateSimulationInterfaceRawInterfaceConnections(
                from_controller=tuple_4[0], from_fem=tuple_4[1], from_port=tuple_4[2], to_samples=tuple_4[3]
            )
        if len(connection) == 3:
            cls._validate_connection_type(connection, [str, int, list], "(from_controller, from_port, to_samples)")
            tuple_3 = cast(Tuple[str, int, List[float]], connection)
            return ExecutionRequestSimulateSimulationInterfaceRawInterfaceConnections(
                from_controller=tuple_3[0],
                from_fem=get_opx_fem_number(),
                from_port=tuple_3[1],
                to_samples=tuple_3[2],
            )
        raise Exception("connection should be tuple of length of 3 or 4")

    def update_simulate_request(self, request: SimulationRequest) -> SimulationRequest:
        request.simulate.simulation_interface.raw = ExecutionRequestSimulateSimulationInterfaceRawInterface(
            noise_power=self.noisePower, connections=self._connections
        )
        return request
