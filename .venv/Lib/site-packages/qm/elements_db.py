from typing import Dict, Union, Optional, overload

import betterproto

from qm.api.frontend_api import FrontendApi
from qm._octaves_container import OctavesContainer
from qm.octave.octave_config import QmOctaveConfig
from qm.elements.element import Element, AllElements, NewApiUpconvertedElement
from qm.elements.element_outputs import NoOutput, ElementOutput, DownconvertedOutput
from qm.elements.element_inputs import (
    NoInput,
    MixInputs,
    SingleInput,
    MicrowaveInput,
    MultipleInputs,
    ElementInputGRPCType,
    SingleInputCollection,
)
from qm.grpc.qua_config import (
    QuaConfig,
    QuaConfigMixInputs,
    QuaConfigElementDec,
    QuaConfigSingleInput,
    QuaConfigMultipleInputs,
    QuaConfigGeneralPortReference,
    QuaConfigSingleInputCollection,
    QuaConfigMicrowaveInputPortReference,
)


class ElementNotFound(KeyError):
    def __init__(self, key: str):
        self._key = key

    def __str__(self) -> str:
        return f"Element with the key {self._key} was not found."


class UnknownElementType(ValueError):
    pass


class ElementsDB(Dict[str, AllElements]):
    def __missing__(self, key: str) -> None:
        raise ElementNotFound(key)


def init_elements(
    pb_config: QuaConfig,
    frontend_api: FrontendApi,
    machine_id: str,
    octave_config: Optional[QmOctaveConfig] = None,
) -> ElementsDB:
    elements = {}
    _octave_container = OctavesContainer(pb_config, octave_config)
    for name, element_config in pb_config.v1_beta.elements.items():
        _, element_inputs = betterproto.which_one_of(element_config, "element_inputs_one_of")
        input_inst = _get_element_input(
            element_config, element_inputs, name, frontend_api, machine_id, _octave_container
        )
        rf_output = _get_element_rf_output(element_config.rf_outputs, _octave_container)

        elements[name] = Element(
            name=name,
            config=element_config,
            api=frontend_api,
            machine_id=machine_id,
            element_input=input_inst,
            element_output=rf_output,
        )
    return ElementsDB(elements)


@overload
def _get_element_input(
    element_config: QuaConfigElementDec,
    element_inputs: None,
    name: str,
    frontend_api: FrontendApi,
    machine_id: str,
    octave_container: OctavesContainer,
) -> NoInput:
    pass


@overload
def _get_element_input(
    element_config: QuaConfigElementDec,
    element_inputs: QuaConfigMixInputs,
    name: str,
    frontend_api: FrontendApi,
    machine_id: str,
    octave_container: OctavesContainer,
) -> MixInputs:
    pass


@overload
def _get_element_input(
    element_config: QuaConfigElementDec,
    element_inputs: QuaConfigSingleInput,
    name: str,
    frontend_api: FrontendApi,
    machine_id: str,
    octave_container: OctavesContainer,
) -> SingleInput:
    pass


@overload
def _get_element_input(
    element_config: QuaConfigElementDec,
    element_inputs: QuaConfigMultipleInputs,
    name: str,
    frontend_api: FrontendApi,
    machine_id: str,
    octave_container: OctavesContainer,
) -> MultipleInputs:
    pass


@overload
def _get_element_input(
    element_config: QuaConfigElementDec,
    element_inputs: QuaConfigSingleInputCollection,
    name: str,
    frontend_api: FrontendApi,
    machine_id: str,
    octave_container: OctavesContainer,
) -> SingleInputCollection:
    pass


@overload
def _get_element_input(
    element_config: QuaConfigElementDec,
    element_inputs: QuaConfigMicrowaveInputPortReference,
    name: str,
    frontend_api: FrontendApi,
    machine_id: str,
    octave_container: OctavesContainer,
) -> MicrowaveInput:
    pass


def _get_element_input(
    element_config: QuaConfigElementDec,
    element_inputs: ElementInputGRPCType,
    name: str,
    frontend_api: FrontendApi,
    machine_id: str,
    octave_container: OctavesContainer,
) -> Union[NoInput, MixInputs, SingleInput, MultipleInputs, SingleInputCollection, MicrowaveInput]:
    if element_inputs is None:
        return NoInput(name, element_inputs, frontend_api, machine_id)
    if isinstance(element_inputs, QuaConfigMixInputs):
        return octave_container.create_mix_inputs(element_config, name, frontend_api, machine_id)
    if isinstance(element_inputs, QuaConfigSingleInput):
        return SingleInput(name, element_inputs, frontend_api, machine_id)
    if isinstance(element_inputs, QuaConfigMultipleInputs):
        return MultipleInputs(name, element_inputs, frontend_api, machine_id)
    if isinstance(element_inputs, QuaConfigSingleInputCollection):
        return SingleInputCollection(name, element_inputs, frontend_api, machine_id)
    if isinstance(element_inputs, QuaConfigMicrowaveInputPortReference):
        return MicrowaveInput(name, element_inputs, frontend_api, machine_id)
    raise UnknownElementType(f"Element {name} is of unknown type - {type(element_inputs)}.")


def _get_element_rf_output(
    rf_outputs: Dict[str, QuaConfigGeneralPortReference], octave_container: OctavesContainer
) -> ElementOutput:
    downconverter = octave_container.get_downconverter(rf_outputs)
    if downconverter is not None:  # I prefer isinstace, but this allows for easier testing
        return DownconvertedOutput(downconverter)
    return NoOutput()


class UpconvertedElementsDB(Dict[str, NewApiUpconvertedElement]):
    def __missing__(self, key: str) -> None:
        raise ElementNotFound(key)


def init_octave_elements(pb_config: QuaConfig, octave_config: Optional[QmOctaveConfig]) -> UpconvertedElementsDB:
    elements = {}
    _octave_container = OctavesContainer(pb_config, octave_config)
    for name, element_config in pb_config.v1_beta.elements.items():
        _, element_inputs = betterproto.which_one_of(element_config, "element_inputs_one_of")
        if isinstance(element_inputs, QuaConfigMixInputs):
            input_inst = _octave_container.create_new_api_upconverted_input(element_config, name)
            if input_inst is not None:
                rf_output = _get_element_rf_output(element_config.rf_outputs, _octave_container)
                elements[name] = NewApiUpconvertedElement(
                    name=name,
                    config=element_config,
                    element_input=input_inst,
                    element_output=rf_output,
                )
    return UpconvertedElementsDB(elements)
