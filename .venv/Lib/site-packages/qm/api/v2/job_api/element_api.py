from typing import Dict, Optional

from qm.api.v2.job_api.generic_apis import ElementGenericApi
from qm.api.v2.job_api.element_input_api import ElementInputApi
from qm.grpc.v2 import GetIntermediateFrequencyRequest, SetIntermediateFrequencyRequest
from qm.api.v2.job_api.element_port_api import MwOutputApi, AnalogOutputApi, DigitalInputApi


class PortNotFound(KeyError):
    def __init__(self, key: str):
        self._key = key

    def __str__(self) -> str:
        return f"Port {self._key} was not found."


class NoMicrowaveOutputError(KeyError):
    def __str__(self) -> str:
        return "Microwave output is not set"


class ElementApi(ElementGenericApi):
    def set_intermediate_frequency(self, frequency: float) -> None:
        request = SetIntermediateFrequencyRequest(job_id=self._id, qe=self._element_id, frequency=frequency)
        self._run(self._stub.set_intermediate_frequency(request, timeout=self._timeout))

    def get_intermediate_frequency(self) -> float:
        request = GetIntermediateFrequencyRequest(job_id=self._id, qe=self._element_id)
        response = self._run(self._stub.get_intermediate_frequency(request, timeout=self._timeout))
        return response.frequency


class DigitalInputs(Dict[str, DigitalInputApi]):
    def __missing__(self, key: str) -> None:
        raise PortNotFound(key)


class AnalogOutputs(Dict[str, AnalogOutputApi]):
    def __missing__(self, key: str) -> None:
        raise PortNotFound(key)


class JobElement:
    def __init__(
        self,
        api: ElementApi,
        input_api: ElementInputApi,
        outputs_apis: Dict[str, AnalogOutputApi],
        digital_inputs_apis: Dict[str, DigitalInputApi],
        microwave_output_api: Optional[MwOutputApi],
    ):
        self._api = api
        self._input_api = input_api
        self._outputs_apis = AnalogOutputs(outputs_apis)
        self._digital_inputs_apis = DigitalInputs(digital_inputs_apis)
        self._microwave_output_api = microwave_output_api

    def set_intermediate_frequency(self, frequency: float) -> None:
        self._api.set_intermediate_frequency(frequency)

    def get_intermediate_frequency(self) -> float:
        return self._api.get_intermediate_frequency()

    @property
    def input(self) -> ElementInputApi:
        return self._input_api

    @property
    def outputs(self) -> AnalogOutputs:
        return self._outputs_apis

    @property
    def digital_inputs(self) -> DigitalInputs:
        return self._digital_inputs_apis

    @property
    def microwave_output(self) -> MwOutputApi:
        if self._microwave_output_api is None:
            raise NoMicrowaveOutputError
        return self._microwave_output_api

    @property
    def has_mw_output(self) -> bool:
        return self._microwave_output_api is not None
