import json
import warnings
from typing import List, Tuple, Union, Literal, Optional, Sequence, overload

import betterproto

from qm.api.v2.job_api import JobApi
from qm.octave import QmOctaveConfig
from qm.persistence import BaseStore
from qm.program.program import Program
from qm.utils import deprecation_message
from qm.exceptions import FunctionInputError
from qm.jobs.job_queue_mock import QmQueueMock
from qm.utils.config_utils import get_fem_config
from qm.octave.octave_manager import OctaveManager
from qm.simulate.interface import SimulationConfig
from qm.api.v2.job_api.job_api import OldJobApiMock
from qm.type_hinting.config_types import DictQuaConfig
from qm.api.models.capabilities import ServerCapabilities
from qm.api.models.server_details import ConnectionDetails
from qm.api.v2.qm_api import QmApi, IoValue, NoRunningQmJob
from qm.type_hinting import Value, Number, NumpySupportedValue
from qm.type_hinting.general import PathLike, NumpySupportedFloat
from qm.api.v2.job_api.simulated_job_api import OldSimulatedJobApiMock
from qm.api.models.compiler import CompilerOptionArguments, standardize_compiler_params
from qm.grpc.qua_config import QuaConfig, QuaConfigMicrowaveFemDec, QuaConfigAdcPortReference, QuaConfigDacPortReference


class OldQmApiMock(QmApi):
    SIMULATED_JOB_CLASS = OldSimulatedJobApiMock

    def __init__(
        self,
        connection_details: ConnectionDetails,
        qm_id: str,
        store: BaseStore,
        capabilities: ServerCapabilities,
        octave_config: Optional[QmOctaveConfig],
        octave_manager: OctaveManager,
        pb_config: Optional[QuaConfig] = None,
    ):
        super().__init__(connection_details, qm_id, store, capabilities, octave_config, octave_manager, pb_config)
        self._queue = QmQueueMock(store=store, api=self, capabilities=self._caps)

    def _get_job(self, job_id: str, store: BaseStore) -> OldJobApiMock:
        return OldJobApiMock(self.connection_details, job_id, store, capabilities=self._caps)

    def get_job_by_id(self, job_id: str) -> OldJobApiMock:
        warnings.warn(
            deprecation_message(
                method="qm.get_job_by_id",
                deprecated_in="1.1.8",
                removed_in="1.2.0",
                details="This method is going to be removed, please use `qm.get_job()`.",
            ),
            DeprecationWarning,
            stacklevel=1,
        )
        return self._get_job(job_id, self._store)

    @property
    def queue(self) -> QmQueueMock:
        warnings.warn(
            deprecation_message(
                method="qm.queue",
                deprecated_in="1.1.8",
                removed_in="1.2.0",
                details="This property is going to be removed, all functionality will exist directly under "
                "`QuantumMachine`. For example, instead of `qm.queue.add(prog)` use `qm.add_to_queue(prog)`.",
            ),
            DeprecationWarning,
            stacklevel=1,
        )
        return self._queue

    def close(self) -> bool:  # type: ignore[override]
        super().close()
        return True

    def execute(
        self,
        program: Program,
        duration_limit: None = None,
        data_limit: None = None,
        force_execution: None = None,
        dry_run: None = None,
        simulate: Optional[SimulationConfig] = None,
        *,
        compiler_options: Optional[CompilerOptionArguments] = None,
        strict: Optional[bool] = None,
        flags: Optional[List[str]] = None,
    ) -> JobApi:
        if not isinstance(program, Program):
            raise Exception("program argument must be of type qm.program.Program")

        for x, name in [
            (duration_limit, "`duration_limit'"),
            (data_limit, "`data_limit'"),
            (force_execution, "`force_execution'"),
            (dry_run, "`dry_run'"),
        ]:
            if x is not None:
                warnings.warn(
                    deprecation_message(
                        method=f"The argument {name}",
                        deprecated_in="1.1.8",
                        removed_in="1.2.0",
                    ),
                )

        compiler_options = standardize_compiler_params(compiler_options, strict, flags)

        if simulate is not None:
            warnings.warn(
                deprecation_message(
                    method="The argument simulate",
                    deprecated_in="1.1.8",
                    removed_in="1.2.0",
                    details="The simulate argument is deprecated, please use the simulate method.",
                ),
            )
            return self.simulate(program, simulate, compiler_options=compiler_options)

        self.clear_queue()
        current_running_job = self._get_running_job()
        if current_running_job is not None:
            current_running_job.cancel()

        new_job_api = super().execute(program, compiler_options=compiler_options)
        new_job_api.wait_until({"Running", "Processing"}, timeout=5 * 60)
        # The timeout here is just for the backwards compatibility behaviour.
        # See that in the father function there is no `wait_until`
        return new_job_api

    def list_controllers(self) -> Tuple[str, ...]:
        warnings.warn(
            deprecation_message(
                method="qm.list_controllers",
                deprecated_in="1.1.8",
                removed_in="1.2.0",
                details="This method is going to be removed, please get data from `qm.get_config()`.",
            ),
            DeprecationWarning,
            stacklevel=1,
        )
        config = self._get_pb_config()
        return tuple(config.v1_beta.control_devices) or tuple(config.v1_beta.controllers)

    def set_mixer_correction(
        self,
        mixer: str,
        intermediate_frequency: Number,
        lo_frequency: Number,
        values: Tuple[float, float, float, float],
    ) -> None:
        warnings.warn(
            deprecation_message(
                method="qm.set_mixer_correction",
                deprecated_in="1.1.8",
                removed_in="1.2.0",
                details="This method is going to be removed, please use `job.set_element_correction()`.",
            ),
            DeprecationWarning,
            stacklevel=1,
        )
        config: DictQuaConfig = {
            "version": 1,
            "mixers": {
                mixer: [
                    {
                        "correction": values,
                        "intermediate_frequency": intermediate_frequency,
                        "lo_frequency": lo_frequency,
                    }
                ]
            },
        }
        self.update_config(config)
        job = self._get_running_job()
        if job is not None:
            pb_config = self._get_pb_config()
            for name, element_config in pb_config.v1_beta.elements.items():
                if betterproto.serialized_on_wire(element_config.mix_inputs):
                    if element_config.mix_inputs.mixer == mixer:
                        if element_config.intermediate_frequency == intermediate_frequency:
                            if element_config.mix_inputs.lo_frequency == lo_frequency:
                                job.set_element_correction(name, values)

    def set_intermediate_frequency(self, element: str, freq: float) -> None:
        warnings.warn(
            deprecation_message(
                method="qm.set_intermediate_frequency",
                deprecated_in="1.1.8",
                removed_in="1.2.0",
                details="This method is going to be moved to the job API, please use "
                "`job.set_intermediate_frequency()`.",
            ),
            DeprecationWarning,
            stacklevel=1,
        )
        job = self._strict_get_running_job()
        job.set_intermediate_frequency(element, freq)

    def get_intermediate_frequency(self, element: str) -> float:
        warnings.warn(
            deprecation_message(
                method="qm.get_intermediate_frequency",
                deprecated_in="1.1.8",
                removed_in="1.2.0",
                details="This method is going to be moved to the job API, please use "
                "`job.get_intermediate_frequency()`.",
            ),
            DeprecationWarning,
            stacklevel=1,
        )
        job = self._strict_get_running_job()
        return job.get_intermediate_frequency(element)

    def get_output_dc_offset_by_element(
        self, element: str, iq_input: Optional[Literal["I", "Q", "single"]] = None
    ) -> float:
        warnings.warn(
            deprecation_message(
                method="qm.get_output_dc_offset_by_element",
                deprecated_in="1.1.8",
                removed_in="1.2.0",
                details="This method is going to be removed, please get idle value from `qm.get_config()`"
                " or current value from job `job.get_output_dc_offset_by_element()`",
            ),
            DeprecationWarning,
            stacklevel=1,
        )
        job = self._strict_get_running_job()
        return job.get_output_dc_offset_by_element(element, iq_input)

    @overload
    def set_output_dc_offset_by_element(self, element: str, input: Literal["single", "I", "Q"], offset: float) -> None:
        pass

    @overload
    def set_output_dc_offset_by_element(
        self,
        element: str,
        input: Tuple[Literal["I", "Q"], Literal["I", "Q"]],
        offset: Union[Tuple[float, float], List[float]],
    ) -> None:
        pass

    def set_output_dc_offset_by_element(
        self,
        element: str,
        input: Union[Literal["single", "I", "Q"], Tuple[Literal["I", "Q"], Literal["I", "Q"]], List[Literal["I", "Q"]]],
        offset: Union[float, Tuple[float, float], List[float]],
    ) -> None:
        warnings.warn(
            deprecation_message(
                method="qm.set_output_dc_offset_by_element",
                deprecated_in="1.1.8",
                removed_in="1.2.0",
                details="This method is going to be removed, please set idle value with `qm.update_config()`"
                " or current value from job `job.set_output_dc_offset_by_element()`",
            ),
            DeprecationWarning,
            stacklevel=1,
        )
        if isinstance(input, str):
            if not isinstance(offset, (int, float)):
                raise FunctionInputError(f"Input should be int or float, got {type(offset)}")
            if input in {"I", "Q"}:
                ports = self._get_input_ports_from_mixed_input_element(element)
                port = ports[0] if input == "I" else ports[1]
            else:
                port = self._get_input_port_from_single_input_element(element)
            config = self._create_config_for_output_dc_offset_setting(port, offset)
            self.update_config(config)
            job = self._get_running_job()
            if job is not None:
                job.set_output_dc_offset_by_element(element, input, offset)
        elif isinstance(input, (list, tuple)):
            if not set(input) <= {"I", "Q"}:
                raise FunctionInputError(f"Input names should be 'I' or 'Q', got {input}")
            if not (isinstance(offset, (list, tuple)) and len(input) == len(offset)):
                raise FunctionInputError(
                    f"input should be two iterables of the same size," f"got input = {input} and offset = {offset}"
                )
            ports = self._get_input_ports_from_mixed_input_element(element)
            for _input, _offset in zip(input, offset):
                _port = ports[0] if _input == "I" else ports[1]
                config = self._create_config_for_output_dc_offset_setting(_port, _offset)
                self.update_config(config)
                job = self._get_running_job()
                if job is not None:
                    job.set_output_dc_offset_by_element(element, input, offset)
        else:
            raise FunctionInputError(f"Input should be str or tuple, got {type(input)}")

    def set_output_filter_by_element(
        self,
        element: str,
        input: str,
        feedforward: Sequence[NumpySupportedFloat],
        feedback: Sequence[NumpySupportedFloat],
    ) -> None:
        raise NotImplementedError

    def set_input_dc_offset_by_element(self, element: str, output: str, offset: float) -> None:
        warnings.warn(
            deprecation_message(
                method="qm.set_input_dc_offset_by_element",
                deprecated_in="1.1.8",
                removed_in="1.2.0",
                details="This method is going to be moved to the job API, please use "
                "`job.set_input_dc_offset_by_element()`.",
            ),
            DeprecationWarning,
            stacklevel=1,
        )
        port = self._get_output_port_from_element(element, output)
        config = self._create_config_for_input_dc_offset_setting(port, offset)
        self.update_config(config)

        job = self._get_running_job()
        if job is not None:
            job.set_input_dc_offset_by_element(element, output, offset)

    def get_input_dc_offset_by_element(self, element: str, output: str) -> float:
        warnings.warn(
            deprecation_message(
                method="qm.get_input_dc_offset_by_element",
                deprecated_in="1.1.8",
                removed_in="1.2.0",
                details="This method is going to be removed, please get the value from `qm.get_config()`.",
            ),
            DeprecationWarning,
            stacklevel=1,
        )
        config = self._get_pb_config()
        port = self._get_output_port_from_element(element, output)
        fem_config = get_fem_config(config, port)
        if isinstance(fem_config, QuaConfigMicrowaveFemDec):
            raise ValueError(f"Element {element} does not support dc offset.")
        return fem_config.analog_inputs[port.number].offset

    def get_digital_delay(self, element: str, digital_input: str) -> int:
        warnings.warn(
            deprecation_message(
                method="qm.get_digital_delay",
                deprecated_in="1.1.8",
                removed_in="1.2.0",
                details="This method is going to be moved to the job API, please use use "
                "`job.get_output_digital_delay()`.",
            ),
            DeprecationWarning,
            stacklevel=1,
        )
        job = self._strict_get_running_job()
        return job.get_output_digital_buffer(element, digital_input)

    def set_digital_delay(self, element: str, digital_input: str, delay: int) -> None:
        warnings.warn(
            deprecation_message(
                method="qm.set_digital_delay",
                deprecated_in="1.1.8",
                removed_in="1.2.0",
                details="This method is going to be moved to the job API, please use use "
                "`job.set_output_digital_delay()`.",
            ),
            DeprecationWarning,
            stacklevel=1,
        )
        job = self._strict_get_running_job()
        job.set_output_digital_delay(element, digital_input, delay)

    def get_digital_buffer(self, element: str, digital_input: str) -> int:
        warnings.warn(
            deprecation_message(
                method="qm.get_digital_buffer",
                deprecated_in="1.1.8",
                removed_in="1.2.0",
                details="This method is going to be moved to the job API, please use use "
                "`job.get_output_digital_buffer()`.",
            ),
            DeprecationWarning,
            stacklevel=1,
        )
        job = self._strict_get_running_job()
        return job.get_output_digital_buffer(element, digital_input)

    def set_digital_buffer(self, element: str, digital_input: str, buffer: int) -> None:
        warnings.warn(
            deprecation_message(
                method="qm.set_digital_buffer",
                deprecated_in="1.1.8",
                removed_in="1.2.0",
                details="This method is going to be moved to the job API, please use use "
                "`job.set_output_digital_buffer()`.",
            ),
            DeprecationWarning,
            stacklevel=1,
        )
        job = self._strict_get_running_job()
        job.set_output_digital_buffer(element, digital_input, buffer)

    def get_time_of_flight(self, element: str) -> int:
        warnings.warn(
            deprecation_message(
                method="qm.get_time_of_flight",
                deprecated_in="1.1.8",
                removed_in="1.2.0",
                details="This method is going to be removed, please get the value from `qm.get_config()`.",
            ),
            DeprecationWarning,
            stacklevel=1,
        )
        config = self._get_pb_config()
        tof = config.v1_beta.elements[element].time_of_flight
        if tof is None:
            raise ValueError(f"Time of flight for element {element} is not set")
        return tof

    def get_smearing(self, element: str) -> int:
        warnings.warn(
            deprecation_message(
                method="qm.get_smearing",
                deprecated_in="1.1.8",
                removed_in="1.2.0",
                details="This method is going to be removed, please get the value from `qm.get_config()`.",
            ),
            DeprecationWarning,
            stacklevel=1,
        )
        config = self._get_pb_config()
        smearing = config.v1_beta.elements[element].smearing
        if smearing is None:
            raise ValueError(f"Smearing for element {element} is not set")
        return smearing

    @property
    def io1(self) -> IoValue:
        warnings.warn(
            deprecation_message(
                method="qm.io1",
                deprecated_in="1.1.8",
                removed_in="1.2.0",
                details="This property is going to be removed, please use `job.get_io_values()[0]`",
            ),
            DeprecationWarning,
            stacklevel=1,
        )
        return self.get_io1_value()

    @io1.setter
    def io1(self, value: Value) -> None:
        warnings.warn(
            deprecation_message(
                method="qm.io1",
                deprecated_in="1.1.8",
                removed_in="1.2.0",
                details="This property is going to be removed, please use `job.set_io_values(io1=value)`",
            ),
            DeprecationWarning,
            stacklevel=1,
        )
        self.set_io1_value(value)

    @property
    def io2(self) -> IoValue:
        warnings.warn(
            deprecation_message(
                method="qm.io2",
                deprecated_in="1.1.8",
                removed_in="1.2.0",
                details="This property is going to be removed, please use `job.get_io_values()[1]`",
            ),
            DeprecationWarning,
            stacklevel=1,
        )
        return self.get_io1_value()

    @io2.setter
    def io2(self, value: Value) -> None:
        warnings.warn(
            deprecation_message(
                method="qm.io2",
                deprecated_in="1.1.8",
                removed_in="1.2.0",
                details="This property is going to be removed, please use `job.set_io_values(io2=value)`",
            ),
            DeprecationWarning,
            stacklevel=1,
        )
        self.set_io2_value(value)

    def set_io1_value(self, value_1: Value) -> None:
        warnings.warn(
            deprecation_message(
                method="qm.set_io1_value",
                deprecated_in="1.1.8",
                removed_in="1.2.0",
                details="This method is going to be moved to the job API, please use `job.set_io_values(io1=value)`",
            ),
            DeprecationWarning,
            stacklevel=1,
        )
        self.set_io_values(value_1=value_1)

    def set_io2_value(self, value_2: Value) -> None:
        warnings.warn(
            deprecation_message(
                method="qm.set_io2_value",
                deprecated_in="1.1.8",
                removed_in="1.2.0",
                details="This method is going to be moved to the job API, please use `job.set_io_values(io2=value)`",
            ),
            DeprecationWarning,
            stacklevel=1,
        )
        self.set_io_values(value_2=value_2)

    def set_io_values(
        self,
        value_1: Optional[NumpySupportedValue] = None,
        value_2: Optional[NumpySupportedValue] = None,
    ) -> None:
        warnings.warn(
            deprecation_message(
                method="qm.set_io_values",
                deprecated_in="1.1.8",
                removed_in="1.2.0",
                details="This method is going to be moved to the job API, please use `job.set_io_values()`",
            ),
            DeprecationWarning,
            stacklevel=1,
        )
        if value_1 is None and value_2 is None:
            return

        job = self._strict_get_running_job()
        job.set_io_values(value_1, value_2)

    def get_io1_value(self) -> IoValue:
        warnings.warn(
            deprecation_message(
                method="qm.get_io2_value",
                deprecated_in="1.1.8",
                removed_in="1.2.0",
                details="This method is going to be moved to the job API, please use `job.get_io_values()[0]`",
            ),
            DeprecationWarning,
            stacklevel=1,
        )
        return self.get_io_values()[0]

    def get_io2_value(self) -> IoValue:
        warnings.warn(
            deprecation_message(
                method="qm.get_io2_value",
                deprecated_in="1.1.8",
                removed_in="1.2.0",
                details="This method is going to be moved to the job API, please use `job.get_io_values()[1]`",
            ),
            DeprecationWarning,
            stacklevel=1,
        )
        return self.get_io_values()[1]

    def get_io_values(self) -> List[IoValue]:
        warnings.warn(
            deprecation_message(
                method="qm.get_io_values",
                deprecated_in="1.1.8",
                removed_in="1.2.0",
                details="This method is going to be moved to the job API, please use `job.get_io_values()`",
            ),
            DeprecationWarning,
            stacklevel=1,
        )
        running_job = self._strict_get_running_job()
        resp1, resp2 = running_job.get_io_values()
        return [
            {
                "io_number": 1,
                "int_value": resp1.int_value,
                "fixed_value": resp1.double_value,
                "boolean_value": resp1.boolean_value,
            },
            {
                "io_number": 2,
                "int_value": resp2.int_value,
                "fixed_value": resp2.double_value,
                "boolean_value": resp2.boolean_value,
            },
        ]

    def save_config_to_file(self, filename: PathLike) -> None:
        warnings.warn(
            deprecation_message(
                method="qm.save_config_to_file",
                deprecated_in="1.1.8",
                removed_in="1.2.0",
                details="This method is going to be removed.",
            ),
            DeprecationWarning,
            stacklevel=1,
        )
        with open(filename, "w") as writer:
            json.dump(self.get_config(), writer)

    def get_running_job(self) -> Optional[OldJobApiMock]:
        warnings.warn(
            deprecation_message(
                method="qm.get_running_job",
                deprecated_in="1.1.8",
                removed_in="1.2.0",
                details="This method is going to be removed, please use `qm.get_jobs(status=['Running'])`",
            ),
            DeprecationWarning,
            stacklevel=1,
        )
        return self._get_running_job()

    def _get_running_job(self) -> Optional[OldJobApiMock]:
        jobs = self.get_jobs(status=["Running"])
        if jobs:
            return self._get_job(jobs[0].id, store=self._store)
        return None

    def _strict_get_running_job(self) -> OldJobApiMock:
        job = self._get_running_job()
        if job is None:
            raise NoRunningQmJob("No running job found")
        return job

    def _get_output_port_from_element(self, element_name: str, port_name: str) -> QuaConfigAdcPortReference:
        element = self._get_pb_config().v1_beta.elements[element_name]
        return element.multiple_outputs.port_references[port_name]

    def _get_input_ports_from_mixed_input_element(
        self, element_name: str
    ) -> Tuple[QuaConfigDacPortReference, QuaConfigDacPortReference]:
        element = self._get_pb_config().v1_beta.elements[element_name]
        return element.mix_inputs.i, element.mix_inputs.q

    def _get_input_port_from_single_input_element(self, element_name: str) -> QuaConfigDacPortReference:
        element = self._get_pb_config().v1_beta.elements[element_name]
        return element.single_input.port

    @staticmethod
    def _create_config_for_input_dc_offset_setting(port: QuaConfigAdcPortReference, value: Number) -> DictQuaConfig:
        return {
            "version": 1,
            "controllers": {port.controller: {"fems": {port.fem: {"analog_inputs": {port.number: {"offset": value}}}}}},
        }

    @staticmethod
    def _create_config_for_output_dc_offset_setting(port: QuaConfigDacPortReference, value: Number) -> DictQuaConfig:
        return {
            "version": 1,
            "controllers": {
                port.controller: {"fems": {port.fem: {"analog_outputs": {port.number: {"offset": value}}}}}
            },
        }
