from dataclasses import dataclass

from qm.grpc.qua_config import QuaConfig


@dataclass(frozen=True)
class QuantumMachineData:
    machine_id: str
    config: QuaConfig
