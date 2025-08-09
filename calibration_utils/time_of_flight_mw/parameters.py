from typing import Optional
from qualibrate import NodeParameters
from qualibrate.parameters import RunnableParameters
from qualibration_libs.parameters import QubitsExperimentNodeParameters, CommonNodeParameters


class NodeSpecificParameters(RunnableParameters):
    num_shots: int = 100
    """Number of averages to perform. Default is 100."""
    time_of_flight_in_ns: Optional[int] = 28
    """Time of flight in nanoseconds. Default is 28 ns."""
    readout_amplitude_in_dBm: Optional[float] = -11
    """Readout amplitude in dBm. Default is -11 dBm."""
    readout_length_in_ns: Optional[int] = 1000
    """Readout length in nanoseconds. Default is 1000 ns."""
    readout_amp: Optional[float] = 0.5
    """Readout amplitude in (a.u.). Default is 0.5"""
    if_frequency: Optional[int] = int(10e6)
    """Readout intermediate frequency in Hz. Default is 10 MHz"""


class Parameters(
    NodeParameters,
    CommonNodeParameters,
    NodeSpecificParameters,
    QubitsExperimentNodeParameters,
):
    pass
