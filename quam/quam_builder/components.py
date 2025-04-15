from typing import Optional

from quam.core import quam_dataclass
from quam.components.channels import (
    InOutIQChannel,
    InOutMWChannel,
    InOutSingleChannel,
    MWChannel,
    SingleChannel,
    DigitalOutputChannel,
)
from quam.components.ports import (
    MWFEMAnalogOutputPort,
    MWFEMAnalogInputPort,
    LFFEMAnalogOutputPort,
    LFFEMAnalogInputPort,
)

__all__ = ["TankCircuit", "XYDrive"]


@quam_dataclass
class TankCircuit(InOutSingleChannel):
    depletion_time: int = 16
    f_01: float = None
    f_12: float = None
    confusion_matrix: list = None


@quam_dataclass
class XYDrive(MWChannel):
    intermediate_frequency: float = "#./inferred_intermediate_frequency"

    @property
    def upconverter_frequency(self):
        """Returns the up-converter/LO frequency in Hz."""
        return self.opx_output.upconverter_frequency


@quam_dataclass
class PlungerGate(SingleChannel):
    level_init: float = 0.0
    level_idle: float = 0.2
    level_readout: float = 0.05


@quam_dataclass
class QDAC_trigger(MWChannel):
    pass
