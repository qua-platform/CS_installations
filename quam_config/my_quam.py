from typing import Optional, Literal
from qm.qua import *
from quam.core import quam_dataclass
from quam.components.pulses import Pulse
from quam.components.macro import QubitPairMacro
from quam_builder.architecture.superconducting.qpu import FixedFrequencyQuam, FluxTunableQuam
from qm.qua._dsl import QuaExpression, QuaVariable


# Define the QUAM class that will be used in all calibration nodes
# Should inherit from either FixedFrequencyQuam or FluxTunableQuam
class Quam(FixedFrequencyQuam):
    pass
