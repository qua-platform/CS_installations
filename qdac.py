from typing import Any
from qcodes_contrib_drivers.drivers.QDevil.QDAC1 import QDac, Mode, QDacChannel


class QDACWithChannelLookup(QDac):
    """
    A thin software wrapper around the QDAC-I driver from QCoDes, allowing
    channels to be easily looked up by their index or their corresponding gate
    name.
    """
    def __init__(self, name: str, address: str, **kwargs: Any):
        super().__init__(name, address, **kwargs)
        self.qdac_channel_mapping = kwargs.get("qdac_channel_mapping")
        self.qdac_turn_on_voltages = kwargs.get("qdac_turn_on_voltages")

    def get_channel_from_gate(self, gate: str) -> QDacChannel:
        """ Returns the QDAC channel attribute corresponding to the given gate. """
        if gate.upper() in self.qdac_channel_mapping:
            gate = self.get_channel_by_index(self.qdac_channel_mapping[gate.upper()])
        else:
            raise ValueError(
                f'Expected gate to be one of {", ".join(list(self.qdac_channel_mapping.keys()))}, got {gate}')

        return gate

    def get_channel_by_index(self, i: int) -> QDacChannel:
        """ Returns the QDAC channel attribute self.chX for some integer `i` """
        return getattr(self, f"ch{i:02d}")

    def set_to_turn_on_voltage(self, gate: str):
        """ Sets specified gate to its turn-on voltage. """
        self.get_channel_from_gate(gate).v(self.qdac_turn_on_voltages[gate])