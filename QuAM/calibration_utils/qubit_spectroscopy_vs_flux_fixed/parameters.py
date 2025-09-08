from typing import Optional

from qualibrate import NodeParameters
from qualibrate.parameters import RunnableParameters
from qualibration_libs.parameters import QubitsExperimentNodeParameters, CommonNodeParameters


class NodeSpecificParameters(RunnableParameters):
    num_shots: int = 50
    """Number of averages to perform. Default is 50."""
    operation: str = "saturation"
    """Operation to perform. Default is "saturation"."""
    operation_amplitude_factor: float = 0.1
    """Amplitude factor for the operation. Default is 0.1."""
    operation_len_in_ns: Optional[int] = None
    """Length of the operation in ns. Default is the predefined pulse length."""
    frequency_span_in_mhz: float = 100.0
    """Frequency span in MHz. Default is 100 MHz."""
    frequency_center_in_mhz: Optional[float] = None
    """Central frequency to sweep around. If none, defaults to qubit resonance."""
    frequency_step_in_mhz: float = 1.0
    """Frequency step in MHz. Default is 0.1 MHz."""
    flux_offset_span_in_v: float = 0.05
    """Minimum flux bias offset in volts. Default is -0.02 V."""
    flux_center_in_v: Optional[float] = None
    """Central flux bias to sweep around. If none, defaults to sweet spot flux value."""
    num_flux_points: int = 21
    """Number of flux points. Default is 51."""
    input_line_impedance_in_ohm: Optional[int] = 50
    """Input line impedance in ohms. Default is 50 Ohm."""
    line_attenuation_in_db: Optional[int] = 0
    """Line attenuation in dB. Default is 0 dB."""


class Parameters(
    NodeParameters,
    CommonNodeParameters,
    NodeSpecificParameters,
    QubitsExperimentNodeParameters,
):
    pass
