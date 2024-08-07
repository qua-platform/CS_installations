import logging
from typing import Union, Generic

import numpy
from dependency_injector.wiring import Provide, inject

from qm.api.frontend_api import FrontendApi
from qm.elements.element_outputs import ElementOutput
from qm.api.models.capabilities import ServerCapabilities
from qm.elements.up_converted_input import UpconvertedInputNewApi
from qm.containers.capabilities_container import CapabilitiesContainer
from qm.elements.element_inputs import ElementInput, ElementInputGRPCType
from qm.grpc.qua_config import (
    QuaConfigMixInputs,
    QuaConfigElementDec,
    QuaConfigSingleInput,
    QuaConfigMultipleInputs,
    QuaConfigSingleInputCollection,
)

logger = logging.getLogger(__name__)


class Element(Generic[ElementInputGRPCType]):
    def __init__(
        self,
        name: str,
        config: QuaConfigElementDec,
        api: FrontendApi,
        machine_id: str,
        element_input: ElementInput[ElementInputGRPCType],
        element_output: ElementOutput,
    ):
        self._config = config
        self._name = name
        self._frontend = api
        self._id = machine_id
        self.input: ElementInput[ElementInputGRPCType] = element_input
        self.output = element_output

    @property
    def name(self) -> str:
        return self._name

    @inject
    def set_intermediate_frequency(
        self, freq: float, capabilities: ServerCapabilities = Provide[CapabilitiesContainer.capabilities]
    ) -> None:
        if not isinstance(freq, (numpy.floating, float)):
            raise TypeError("freq must be a float")

        freq = float(freq)
        logger.debug(f"Setting element '{self._name}' intermediate frequency to '{freq}'.")
        self._frontend.set_intermediate_frequency(self._id, self._name, freq)
        self._config.intermediate_frequency_double = float(freq) if capabilities.supports_double_frequency else 0.0
        self._config.intermediate_frequency = int(freq)

    @property
    @inject
    def intermediate_frequency(
        self, capabilities: ServerCapabilities = Provide[CapabilitiesContainer.capabilities]
    ) -> float:
        sign: int = (-1) ** self._config.intermediate_frequency_negative
        if capabilities.supports_double_frequency:
            freq = self._config.intermediate_frequency_double
        else:
            freq = float(self._config.intermediate_frequency or 0)
        return sign * freq

    def get_output_digital_delay(self, digital_input_name: str) -> int:
        try:
            return self._config.digital_inputs[digital_input_name].delay
        except KeyError:
            raise Exception(f"Digital input for {digital_input_name} was not found.")

    def get_output_digital_buffer(self, digital_input_name: str) -> int:
        try:
            return self._config.digital_inputs[digital_input_name].buffer
        except KeyError:
            raise Exception(f"Digital buffer for {digital_input_name} was not found.")

    def set_output_digital_delay(self, digital_input: str, delay: int) -> None:
        if not isinstance(digital_input, str):
            raise Exception("port must be a string")
        if not isinstance(delay, int):
            raise Exception("delay must be an int")
        logger.debug(f"Setting delay of digital port '{digital_input}' on element '{self._name}' to '{delay}'")
        self._frontend.set_output_digital_delay(self._id, self._name, digital_input, delay)
        self._config.digital_inputs[digital_input].delay = delay

    def set_output_digital_buffer(self, digital_input: str, buffer: int) -> None:
        if not isinstance(digital_input, str):
            raise Exception("port must be a string")
        if not isinstance(buffer, int):
            raise Exception("buffer must be an int.")
        logger.debug(f"Setting buffer of digital port '{digital_input}' on element '{self._name}' to '{buffer}'")
        self._frontend.set_output_digital_buffer(self._id, self._name, digital_input, buffer)
        self._config.digital_inputs[digital_input].buffer = buffer

    def set_input_dc_offset(self, output: str, offset: float) -> None:
        logger.debug(f"Setting DC offset of output '{output}' on element '{self._name}' to '{offset}'.")
        if not isinstance(output, str):
            raise TypeError("output must be a string")
        if output not in self._config.outputs:
            raise ValueError(f"output {output} was not found in the element's outputs")
        if not isinstance(offset, (numpy.floating, float)):
            raise TypeError("offset must be a float")
        offset = float(offset)
        self._frontend.set_input_dc_offset(self._id, self._name, output, offset)

    @property
    def time_of_flight(self) -> int:
        return self._config.time_of_flight or 0

    @property
    def smearing(self) -> int:
        return self._config.smearing or 0


class NewApiUpconvertedElement(Element[QuaConfigMixInputs]):
    def __init__(
        self,
        name: str,
        config: QuaConfigElementDec,
        element_input: UpconvertedInputNewApi,
        element_output: ElementOutput,
    ):
        super().__init__(
            name,
            config,
            api=None,  # type: ignore[arg-type]
            machine_id=None,  # type: ignore[arg-type]
            element_input=element_input,
            element_output=element_output,
        )

    @property
    def name(self) -> str:
        return self._name

    @inject
    def set_intermediate_frequency(
        self, freq: float, capabilities: ServerCapabilities = Provide[CapabilitiesContainer.capabilities]
    ) -> None:
        raise NotImplementedError

    def set_output_digital_delay(self, digital_input: str, delay: int) -> None:
        raise NotImplementedError

    def set_output_digital_buffer(self, digital_input: str, buffer: int) -> None:
        raise NotImplementedError

    def set_input_dc_offset(self, output: str, offset: float) -> None:
        raise NotImplementedError


AllElements = Union[
    Element[QuaConfigSingleInput],
    Element[QuaConfigMixInputs],
    Element[QuaConfigSingleInputCollection],
    Element[QuaConfigMultipleInputs],
    Element[None],
]
