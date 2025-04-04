from typing import Literal, Optional

from qualibrate import NodeParameters
from qualibrate.parameters import RunnableParameters
from quam_experiments.parameters import CommonNodeParameters, QubitsExperimentNodeParameters
from quam_experiments.parameters.qubits_experiment import AnyTransmon


class NodeSpecificParameters(RunnableParameters):
    num_averages: int = 100
    control_qubit: Optional[AnyTransmon] = None
    target_qubit: Optional[AnyTransmon] = None
    operation: Literal["square", "flattop"] = "square"
    cz_min_amplitude_factor: float = 0.0
    cz_max_amplitude_factor: float = 2.0
    cz_num_amplitude_factor: int = 51
    cz_duration: int = 40
    num_tomo_angles: int = 11


class Parameters(
    NodeParameters,
    CommonNodeParameters,
    NodeSpecificParameters,
):
    pass
