from typing import Type, Tuple, Union, Optional, overload

from qm.grpc.qm_api import Matrix
from qm.api.v2.job_api.generic_apis import ElementGenericApi
from qm.grpc.qua_config import (
    QuaConfigMixInputs,
    QuaConfigSingleInput,
    QuaConfigMultipleInputs,
    QuaConfigSingleInputCollection,
    QuaConfigMicrowaveInputPortReference,
)
from qm.grpc.v2 import (
    MixInputsDcOffset,
    SingleInputDcOffset,
    GetOutputDcOffsetRequest,
    SetOutputDcOffsetRequest,
    GetMatrixCorrectionRequest,
    SetMatrixCorrectionRequest,
    SetOscillatorFrequencyRequest,
    SetOscillatorFrequencyRequestUpdateComponentSelection,
)

InputConfigType = Union[
    QuaConfigSingleInput,
    QuaConfigMixInputs,
    QuaConfigSingleInputCollection,
    QuaConfigMultipleInputs,
    QuaConfigMicrowaveInputPortReference,
    None,
]


class UnknownElementType(ValueError):
    pass


class ElementInputApi(ElementGenericApi):
    pass


class NoInputApi(ElementInputApi):
    pass


class MultipleInputsApi(ElementInputApi):
    pass


class SingleInputCollectionApi(ElementInputApi):
    pass


class MixInputsApi(ElementInputApi):
    def set_correction(self, correction: Tuple[float, float, float, float]) -> None:
        matrix = Matrix(v00=correction[0], v01=correction[1], v10=correction[2], v11=correction[3])
        request = SetMatrixCorrectionRequest(job_id=self._id, qe=self._element_id, correction=matrix)
        self._run(self._stub.set_matrix_correction(request, timeout=self._timeout))

    def get_correction(self) -> Tuple[float, float, float, float]:
        request = GetMatrixCorrectionRequest(job_id=self._id, qe=self._element_id)
        correction = self._run(self._stub.get_matrix_correction(request, timeout=self._timeout)).correction
        return correction.v00, correction.v01, correction.v10, correction.v11

    def set_dc_offsets(self, i_offset: Optional[float] = None, q_offset: Optional[float] = None) -> None:
        request = SetOutputDcOffsetRequest(
            job_id=self._id, qe=self._element_id, mix_inputs=MixInputsDcOffset(i=i_offset, q=q_offset)
        )
        self._run(self._stub.set_output_dc_offset(request, timeout=self._timeout))

    def get_dc_offsets(self) -> Tuple[float, float]:
        request = GetOutputDcOffsetRequest(job_id=self._id, qe=self._element_id)
        response = self._run(self._stub.get_output_dc_offset(request, timeout=self._timeout))
        i, q = response.mix_inputs.i, response.mix_inputs.q
        if i is None or q is None:
            raise ValueError("Mixed DC offsets are not set")
        return i, q


class SingleInputApi(ElementInputApi):
    def set_dc_offset(self, offset: float) -> None:
        request = SetOutputDcOffsetRequest(
            job_id=self._id, qe=self._element_id, single_input=SingleInputDcOffset(offset=offset)
        )
        self._run(self._stub.set_output_dc_offset(request, timeout=self._timeout))

    def get_dc_offset(self) -> float:
        request = GetOutputDcOffsetRequest(job_id=self._id, qe=self._element_id)
        response = self._run(self._stub.get_output_dc_offset(request, timeout=self._timeout))
        return response.single_input.offset


class MwInputApi(ElementInputApi):
    def set_oscillator_frequency(self, frequency_hz: float, set_also_output: bool = True) -> None:
        request = SetOscillatorFrequencyRequest(
            job_id=self._id,
            qe=self._element_id,
            new_frequency_hz=frequency_hz,
            update_component=SetOscillatorFrequencyRequestUpdateComponentSelection.both
            if set_also_output
            else SetOscillatorFrequencyRequestUpdateComponentSelection.upconverter,
        )
        self._run(self._stub.set_oscillator_frequency(request, timeout=self._timeout))


@overload
def create_element_input_class(input_config: QuaConfigSingleInput) -> Type[SingleInputApi]:
    pass


@overload
def create_element_input_class(input_config: QuaConfigMixInputs) -> Type[MixInputsApi]:
    pass


@overload
def create_element_input_class(input_config: QuaConfigSingleInputCollection) -> Type[SingleInputCollectionApi]:
    pass


@overload
def create_element_input_class(input_config: QuaConfigMultipleInputs) -> Type[MultipleInputsApi]:
    pass


@overload
def create_element_input_class(input_config: QuaConfigMicrowaveInputPortReference) -> Type[MwInputApi]:
    pass


@overload
def create_element_input_class(input_config: None) -> Type[NoInputApi]:
    pass


def create_element_input_class(input_config: InputConfigType) -> Type[ElementInputApi]:
    if isinstance(input_config, QuaConfigSingleInput):
        return SingleInputApi
    if isinstance(input_config, QuaConfigMixInputs):
        return MixInputsApi
    if isinstance(input_config, QuaConfigSingleInputCollection):
        return SingleInputCollectionApi
    if isinstance(input_config, QuaConfigMultipleInputs):
        return MultipleInputsApi
    if isinstance(input_config, QuaConfigMicrowaveInputPortReference):
        return MwInputApi
    if input_config is None:
        return NoInputApi
    raise UnknownElementType(f"Unknown input type {type(input_config)}")
