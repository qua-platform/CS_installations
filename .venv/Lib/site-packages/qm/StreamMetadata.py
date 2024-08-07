from typing import Dict, List
from dataclasses import dataclass

import betterproto
import numpy as np
import numpy.typing as nt

from qm.grpc import results_analyser
from qm.grpc.results_analyser import (
    ProgramStreamMetadata,
    IterationDataForIntIterationValues,
    IterationDataForDoubleIterationValues,
    IterationDataForEachIntIterationValues,
    IterationDataForEachDoubleIterationValues,
)


@dataclass
class IterationData:
    iteration_variable_name: str
    iteration_values: nt.NDArray[np.generic]


@dataclass
class StreamMetadataError:
    error: str
    location: str


@dataclass
class StreamMetadata:
    stream_name: str
    iteration_values: List[IterationData]


def _get_numpy_array_from_proto_iteration_data(
    iteration_data: results_analyser.IterationData,
) -> nt.NDArray[np.generic]:
    name, value = betterproto.which_one_of(iteration_data, "iterationValues")
    if name in ("for_each_int_iteration_values", "for_each_double_iteration_values"):
        assert isinstance(value, (IterationDataForEachDoubleIterationValues, IterationDataForEachIntIterationValues))
        return np.array(value.values)

    assert isinstance(value, (IterationDataForDoubleIterationValues, IterationDataForIntIterationValues))
    start = value.start_value
    step = value.step
    stop = start + step * value.number_of_iterations

    if name == "for_double_iteration_values":
        stop = round(stop, 9)

    return np.arange(start=start, step=step, stop=stop)


def _get_stream_metadata_dict_from_proto_resp(
    program_metadata: ProgramStreamMetadata,
) -> Dict[str, StreamMetadata]:
    stream_metadata_dict = {
        x.stream_name: StreamMetadata(
            x.stream_name,
            [
                IterationData(
                    y.iteration_variable_name,
                    _get_numpy_array_from_proto_iteration_data(y),
                )
                for y in x.iteration_data
            ],
        )
        for x in program_metadata.stream_metadata
    }

    return stream_metadata_dict
