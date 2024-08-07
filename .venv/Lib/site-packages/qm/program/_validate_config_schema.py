import logging
from typing import Collection

from marshmallow import ValidationError

from qm.exceptions import ConfigValidationException
from qm.type_hinting.config_types import ElementConfigType

logger = logging.getLogger(__name__)


def validate_timetagging_parameters(data: ElementConfigType) -> None:
    if "outputPulseParameters" in data:
        pulse_parameters = data["outputPulseParameters"]
        needed_parameters = [
            "signalThreshold",
            "signalPolarity",
            "derivativeThreshold",
            "derivativePolarity",
        ]
        missing_parameters = []
        for parameter in needed_parameters:
            if parameter not in pulse_parameters:
                missing_parameters.append(parameter)
        if len(missing_parameters) > 0:
            raise ConfigValidationException(
                "An element defining the output pulse parameters must either "
                f"define all of the parameters: {needed_parameters}. "
                f"Parameters defined: {pulse_parameters}"
            )
        valid_polarity = {"ASCENDING", "DESCENDING", "ABOVE", "BELOW"}
        if data["outputPulseParameters"]["signalPolarity"].upper() not in valid_polarity:
            raise ConfigValidationException(
                f"'signalPolarity' is {data['outputPulseParameters']['signalPolarity'].upper()} but it must be one of {valid_polarity}"
            )
        if data["outputPulseParameters"]["derivativePolarity"].upper() not in valid_polarity:
            raise ConfigValidationException(
                f"'derivativePolarity' is {data['outputPulseParameters']['derivativePolarity'].upper()} but it must be one of {valid_polarity}"
            )


def _element_has_outputs(data: ElementConfigType) -> bool:
    return bool(data.get("outputs")) or bool(data.get("RF_outputs")) or bool(data.get("MWOutput"))


def _validate_existence_of_field(data: ElementConfigType, field_name: str) -> None:
    if _element_has_outputs(data) and field_name not in data:
        raise ValidationError(f"An element with an output must have {field_name} defined")
    if not _element_has_outputs(data) and field_name in data:
        if "outputs" in data:
            logger.warning(
                f"The field `{field_name}` exists though the element has no outputs (empty dict). "
                f"This behavior is going to cause `ValidationError` in the future."
            )
            return
        raise ValidationError(f"{field_name} should be used only with elements that have outputs")


def validate_output_tof(data: ElementConfigType) -> None:
    _validate_existence_of_field(data, "time_of_flight")


def validate_output_smearing(data: ElementConfigType) -> None:
    if _element_has_outputs(data) and "smearing" not in data:
        data["smearing"] = 0
    _validate_existence_of_field(data, "smearing")


def validate_oscillator(data: ElementConfigType) -> None:
    if "intermediate_frequency" in data and "oscillator" in data:
        raise ValidationError("'intermediate_frequency' and 'oscillator' cannot be defined together")


def validate_used_inputs(data: Collection[str]) -> None:
    used_inputs = set(data) & {"singleInput", "mixInputs", "singleInputCollection", "multipleInputs"}
    if len(used_inputs) > 1:
        raise ValidationError(
            f"Can't support more than a single input type. " f"Used {', '.join(used_inputs)}",
            field_name="",
        )


def validate_sticky_duration(duration: int) -> None:
    if (duration % 4) != 0:
        raise ValidationError(
            "Sticky's element duration must be a dividable by 4",
            field_name="duration",
        )


def validate_arbitrary_waveform(is_overridable: bool, has_max_allowed_error: bool, has_sampling_rate: bool) -> None:
    if is_overridable and has_max_allowed_error:
        raise ValidationError("Overridable waveforms cannot have property 'max_allowed_error'")
    if is_overridable and has_sampling_rate:
        raise ValidationError("Overridable waveforms cannot have property 'sampling_rate_key'")
    if has_max_allowed_error and has_sampling_rate:
        raise ValidationError("Cannot use both 'max_allowed_error' and 'sampling_rate'")
