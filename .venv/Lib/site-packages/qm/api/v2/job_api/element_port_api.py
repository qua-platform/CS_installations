from qm.api.models.server_details import ConnectionDetails
from qm.api.v2.job_api.generic_apis import ElementGenericApi
from qm.grpc.v2 import (
    GetDigitalDelayRequest,
    SetDigitalDelayRequest,
    GetDigitalBufferRequest,
    GetInputDcOffsetRequest,
    SetDigitalBufferRequest,
    SetInputDcOffsetRequest,
    SetOscillatorFrequencyRequest,
    SetOscillatorFrequencyRequestUpdateComponentSelection,
)


class ElementPortApi(ElementGenericApi):
    def __init__(self, connection_details: ConnectionDetails, job_id: str, element_id: str, port_name: str) -> None:
        super().__init__(connection_details, job_id, element_id)
        self._port = port_name


class AnalogOutputApi(ElementPortApi):
    def set_dc_offset(self, value: float) -> None:
        request = SetInputDcOffsetRequest(job_id=self._id, qe=self._element_id, port=self._port, offset=value)
        self._run(self._stub.set_input_dc_offset(request, timeout=self._timeout))

    def get_dc_offset(self) -> float:
        request = GetInputDcOffsetRequest(job_id=self._id, qe=self._element_id, port=self._port)
        response = self._run(self._stub.get_input_dc_offset(request, timeout=self._timeout))
        return response.offset


class MwOutputApi(ElementGenericApi):
    def set_oscillator_frequency(self, frequency: float) -> None:
        request = SetOscillatorFrequencyRequest(
            job_id=self._id,
            qe=self._element_id,
            new_frequency_hz=frequency,
            update_component=SetOscillatorFrequencyRequestUpdateComponentSelection.downconverter,
        )
        self._run(self._stub.set_oscillator_frequency(request, timeout=self._timeout))


class DigitalInputApi(ElementPortApi):
    def set_delay(self, value: int) -> None:
        request = SetDigitalDelayRequest(job_id=self._id, qe=self._element_id, port=self._port, delay=value)
        self._run(self._stub.set_digital_delay(request, timeout=self._timeout))

    def get_delay(self) -> int:
        request = GetDigitalDelayRequest(job_id=self._id, qe=self._element_id, port=self._port)
        response = self._run(self._stub.get_digital_delay(request, timeout=self._timeout))
        return response.delay

    def set_buffer(self, value: int) -> None:
        request = SetDigitalBufferRequest(job_id=self._id, qe=self._element_id, port=self._port, buffer=value)
        self._run(self._stub.set_digital_buffer(request, timeout=self._timeout))

    def get_buffer(self) -> int:
        request = GetDigitalBufferRequest(job_id=self._id, qe=self._element_id, port=self._port)
        response = self._run(self._stub.get_digital_buffer(request, timeout=self._timeout))
        return response.buffer
