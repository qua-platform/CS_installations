import warnings
import json as _json
from io import BytesIO
from dataclasses import dataclass
from typing import Any, Dict, Union, BinaryIO, Callable, Optional

import numpy
import betterproto
import numpy.typing
from numpy.lib import format as _format
from betterproto.lib.google.protobuf import Value, Struct

from qm.persistence import BaseStore
from qm.utils import deprecation_message
from qm.utils.async_utils import run_async
from qm.api.frontend_api import FrontendApi
from qm.exceptions import QMSimulationError
from qm.waveform_report import WaveformReport
from qm.api.simulation_api import SimulationApi
from qm.jobs.running_qm_job import RunningQmJob
from qm.grpc.frontend import SimulatedResponsePart
from qm.api.models.capabilities import ServerCapabilities
from qm.results.simulator_samples import SimulatorSamples
from qm.grpc.v2 import PullSamplesResponsePullSamplesResponseSuccess
from qm.type_hinting.simulator_types import AnalogOutputsType, DigitalOutputsType, WaveformInPortsType
from qm.grpc.results_analyser import (
    SimulatorSamplesResponse,
    SimulatorSamplesResponseData,
    SimulatorSamplesResponseHeader,
)


@dataclass
class DensityMatrix:
    timestamp: int
    data: numpy.typing.NDArray[numpy.cdouble]


class SimulatorOutput:
    def __init__(self, job_id: str, frontend: FrontendApi) -> None:
        super().__init__()
        self._id = job_id
        self._simulation_api = SimulationApi(frontend.connection_details)

    def get_quantum_state(self) -> DensityMatrix:
        state = self._simulation_api.get_simulated_quantum_state(self._id)
        flatten = numpy.array([complex(item.re, item.im) for item in state.data])
        n = int(numpy.sqrt(len(flatten)))
        if len(flatten) != (n * n):
            raise RuntimeError("Quantum state matrix is not correct")
        else:
            pass

        matrix = flatten.reshape(n, n)
        timestamp = state.time_stamp
        return DensityMatrix(timestamp, matrix)


def extract_value(value: Value) -> Any:
    name, one_of = betterproto.which_one_of(value, "kind")
    if name in VALUE_MAPPING:
        return VALUE_MAPPING[name](one_of)


def extract_struct_value(struct_value: Struct) -> Any:
    output = {}
    for name, value in struct_value.fields.items():
        output[name] = extract_value(value)
    return output


VALUE_MAPPING: Dict[str, Callable[[Any], Any]] = {
    "number_value": float,
    "string_value": str,
    "bool_value": bool,
    "list_value": lambda list_value: [extract_value(value) for value in list_value.values],
    "struct_value": extract_struct_value,
    "null_value": lambda x: None,
}


class SimulatedJob(RunningQmJob):
    def __init__(
        self,
        job_id: str,
        frontend_api: FrontendApi,
        capabilities: ServerCapabilities,
        store: BaseStore,
        simulated_response: SimulatedResponsePart,
    ):
        super().__init__(job_id, "", frontend_api, capabilities, store)
        self._waveform_report: Optional[WaveformReport] = None

        self._simulated_analog_outputs: AnalogOutputsType = {"waveforms": None}
        self._simulated_digital_outputs: DigitalOutputsType = {"waveforms": None}
        if betterproto.serialized_on_wire(simulated_response.analog_outputs):
            self._simulated_analog_outputs = extract_struct_value(simulated_response.analog_outputs)
        if betterproto.serialized_on_wire(simulated_response.digital_outputs):
            self._simulated_digital_outputs = extract_struct_value(simulated_response.digital_outputs)
        if betterproto.serialized_on_wire(simulated_response.waveform_report):
            self._waveform_report = WaveformReport.from_dict(
                extract_struct_value(simulated_response.waveform_report), self.id
            )
        if simulated_response.errors:
            raise QMSimulationError("\n".join(simulated_response.errors))

        self._simulation_api = SimulationApi(self._frontend.connection_details)

    def _initialize_from_job_status(self) -> None:
        """
        Overriding this for simulated jobs to do nothing
        """
        pass

    def get_simulated_waveform_report(self) -> Optional[WaveformReport]:
        """
        Get this Job's Waveform report. If any error occurred, None will be returned.
        """
        return self._waveform_report

    def simulated_analog_waveforms(self) -> Optional[WaveformInPortsType]:
        """
        Return the results of the simulation of elements and analog outputs.

        The returned dictionary has the following keys and entries:

        - **elements**: a dictionary containing the outputs with timestamps and values arranged by elements.

        - **controllers: a dictionary containing the outputs with timestamps and values arranged by controllers.

            - **ports**: a dictionary containing the outputs with timestamps and values arranged by output ports.
                for each element or output port, the entry is a list of dictionaries with the following information:

                - **timestamp**:
                    The time, in nsec, from the start of the program to the start of the pulse.

                - **samples**:

                    Output information, with ``duration`` given in nsec and ``value`` given normalized OPX output units.

        Returns:
            A dictionary containing output information for the analog outputs of the controller.

        """
        warnings.warn(
            deprecation_message(
                method="SimulatedJob.simulated_analog_waveforms",
                deprecated_in="1.1.0",
                removed_in="1.2.0",
                details="use 'get_simulated_waveform_report' instead.",
            ),
            DeprecationWarning,
            stacklevel=2,
        )
        return self._simulated_analog_outputs["waveforms"]

    def simulated_digital_waveforms(self) -> Optional[WaveformInPortsType]:
        """
        Return the results of the simulation of digital outputs.

        - **controllers**: a dictionary containing the outputs with timestamps and values arranged by controllers.

            - **ports**: a dictionary containing the outputs with timestamps and values arranged by output ports.
                for each element or output port, the entry is a list of dictionaries with the following information:

                - **timestamp**:
                    The time, in nsec, from the start of the program to the start of the pulse.

                - **samples**:
                    A list containing the sequence of outputted values, with ``duration`` given in nsec
                    and ``value`` given as a boolean value.

        Returns:
            A dictionary containing output information for the analog outputs of the controller.
        """
        warnings.warn(
            deprecation_message(
                method="SimulatedJob.simulated_digital_waveforms",
                deprecated_in="1.1.0",
                removed_in="1.2.0",
                details="use 'get_simulated_waveform_report' instead.",
            ),
            DeprecationWarning,
            stacklevel=2,
        )
        return self._simulated_digital_outputs["waveforms"]

    async def _pull_simulator_samples(
        self, include_analog: bool, include_digital: bool, writer: BinaryIO, data_writer: BinaryIO
    ) -> None:
        async for result in self._simulation_api.pull_simulator_samples(self._id, include_analog, include_digital):
            if result.ok:
                _write_simulator_result(result, writer, data_writer)
            else:
                raise QMSimulationError("Error while pulling samples")

    def _get_np_simulated_samples(
        self, include_analog: bool = True, include_digital: bool = True
    ) -> numpy.typing.NDArray[numpy.generic]:
        writer = BytesIO()
        data_writer = BytesIO()

        run_async(self._pull_simulator_samples(include_analog, include_digital, writer, data_writer))
        return _build_np_array(writer, data_writer)

    def get_simulated_samples(self, include_analog: bool = True, include_digital: bool = True) -> SimulatorSamples:
        """
        Obtain the output samples of a QUA program simulation.

        Samples are returned in an object that holds the controllers in the current simulation,
        where each controller's name will be a property of this object.
        The value of each property of the returned value is an object with the following properties:

        ``analog``:

            holds a dictionary with analog port names as keys and numpy array of samples as values.

        ``digital``:

            holds a dictionary with digital port names as keys and numpy array of samples as values.

        It is also possible to directly plot the outputs using a built-in plot command.

        Example:
            ```python
            samples = job.get_simulated_samples()
            analog1 = samples.con1.analog["1"]  # obtain analog port 1 of controller "con1"
            digital9 = samples.con1.analog["9"]  # obtain digital port 9 of controller "con1"
            samples.con1.plot()  # Plots all active ports
            samples.con1.plot(analog_ports=['1', '2'], digital_ports=['9'])  # Plots the given output ports
            ```

        !!! Note

            The simulated digital waveforms are delayed by 136ns relative to the real
            output of the OPX.

        Args:
            include_analog: Should we collect simulated analog samples
            include_digital: Should we collect simulated digital samples

        Returns:
            The simulated samples of the job.
        """
        return SimulatorSamples.from_np_array(
            self._get_np_simulated_samples(include_analog=include_analog, include_digital=include_digital),
        )

    @property
    def simulator(self) -> SimulatorOutput:
        return SimulatorOutput(self._id, self._frontend)

    def plot_waveform_report_with_simulated_samples(self) -> None:
        self._waveform_report.create_plot(self.get_simulated_samples())

    def plot_waveform_report_without_samples(self) -> None:
        self._waveform_report.create_plot()


def _write_simulator_result(
    result: Union[SimulatorSamplesResponse, PullSamplesResponsePullSamplesResponseSuccess],
    writer: BinaryIO,
    data_writer: BinaryIO,
) -> None:
    _, value = betterproto.which_one_of(result, "body")
    if isinstance(value, SimulatorSamplesResponseHeader):
        _format.write_array_header_2_0(  # type: ignore[no-untyped-call]
            writer,
            {
                "descr": _json.loads(value.simple_d_type),
                "fortran_order": False,
                "shape": (value.count_of_items,),
            },
        )
    elif isinstance(value, SimulatorSamplesResponseData):
        data_writer.write(value.data)
    else:
        raise QMSimulationError("Error while pulling samples")


def _build_np_array(writer: BinaryIO, data_writer: BinaryIO) -> numpy.typing.NDArray[numpy.generic]:
    data_writer.seek(0)
    for d in data_writer:
        writer.write(d)

    writer.seek(0)
    ret: numpy.typing.NDArray[numpy.generic] = numpy.load(writer)
    return ret
