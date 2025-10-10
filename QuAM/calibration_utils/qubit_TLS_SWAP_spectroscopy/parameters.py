from qualibrate import NodeParameters
from qualibrate.parameters import RunnableParameters
from qualibration_libs.parameters import QubitsExperimentNodeParameters, CommonNodeParameters


class NodeSpecificParameters(RunnableParameters):
    num_shots: int = 100
    """Number of averages to perform. Default is 100."""
    min_z_duration_in_ns: int = 16
    """Minimum Z SWAP duration in nanoseconds. Default is 16."""
    max_z_duration_in_ns: int = 5000
    """Maximum Z SWAP duration in nanoseconds. Default is 5000."""
    z_duration_step_in_ns: int = 60
    """Step size for the Z SWAP pulse duration in nanoseconds. Default is 60."""
    flux_center: float = 0.0
    """Flux center value to sweep about. Default is 0.0 V."""
    flux_span: float = 0.01
    """Span of flux values to sweep in volts. Default is 0.01 V."""
    flux_num: int = 21
    """Number of flux points to sample. Default is 21."""
    min_tls_amp: float = .02
    """minimum amplitude of vacuum Rabi oscillations to consider in fitting."""


class Parameters(
    NodeParameters,
    CommonNodeParameters,
    NodeSpecificParameters,
    QubitsExperimentNodeParameters,
):
    pass
