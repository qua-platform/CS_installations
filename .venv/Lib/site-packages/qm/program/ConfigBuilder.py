import warnings
from typing import Dict, List, Tuple, Union, Literal, cast

import betterproto

from qm.type_hinting import Number
from qm.type_hinting.config_types import (
    DictQuaConfig,
    LfFemConfigType,
    MixerConfigType,
    MwFemConfigType,
    PulseConfigType,
    StickyConfigType,
    ElementConfigType,
    MwInputConfigType,
    PortReferenceType,
    MixInputConfigType,
    MwOutputConfigType,
    ControllerConfigType,
    HoldOffsetConfigType,
    OscillatorConfigType,
    SingleInputConfigType,
    DigitalInputConfigType,
    AnalogInputPortConfigType,
    DigitalWaveformConfigType,
    InputCollectionConfigType,
    AnalogOutputPortConfigType,
    ConstantWaveFormConfigType,
    DigitalInputPortConfigType,
    ArbitraryWaveFormConfigType,
    DigitalOutputPortConfigType,
    IntegrationWeightConfigType,
    OPX1000ControllerConfigType,
    CompressedWaveFormConfigType,
    MwFemAnalogInputPortConfigType,
    MwFemAnalogOutputPortConfigType,
    AnalogOutputPortConfigTypeOctoDac,
)
from qm.grpc.qua_config import (
    QuaConfig,
    QuaConfigMatrix,
    QuaConfigSticky,
    QuaConfigFemTypes,
    QuaConfigMixerDec,
    QuaConfigPulseDec,
    QuaConfigDeviceDec,
    QuaConfigMixInputs,
    QuaConfigElementDec,
    QuaConfigHoldOffset,
    QuaConfigOscillator,
    QuaConfigQuaConfigV1,
    QuaConfigSingleInput,
    QuaConfigWaveformDec,
    QuaConfigControllerDec,
    QuaConfigElementThread,
    QuaConfigOctoDacFemDec,
    QuaConfigPortReference,
    QuaConfigMultipleInputs,
    QuaConfigMicrowaveFemDec,
    QuaConfigMultipleOutputs,
    QuaConfigAdcPortReference,
    QuaConfigDacPortReference,
    QuaConfigPulseDecOperation,
    QuaConfigAnalogInputPortDec,
    QuaConfigDigitalWaveformDec,
    QuaConfigAnalogOutputPortDec,
    QuaConfigConstantWaveformDec,
    QuaConfigDigitalInputPortDec,
    QuaConfigArbitraryWaveformDec,
    QuaConfigDigitalOutputPortDec,
    QuaConfigIntegrationWeightDec,
    QuaConfigCompressedWaveformDec,
    QuaConfigSingleInputCollection,
    QuaConfigDigitalInputPortReference,
    QuaConfigDigitalOutputPortReference,
    QuaConfigOctoDacAnalogOutputPortDec,
    QuaConfigDigitalInputPortDecPolarity,
    QuaConfigMicrowaveAnalogInputPortDec,
    QuaConfigMicrowaveInputPortReference,
    QuaConfigMicrowaveAnalogOutputPortDec,
    QuaConfigMicrowaveOutputPortReference,
    QuaConfigOctoDacAnalogOutputPortDecOutputMode,
    QuaConfigOctoDacAnalogOutputPortDecSamplingRateMode,
)


def convert_msg_to_config(config: QuaConfig) -> DictQuaConfig:
    return _convert_v1_beta(config.v1_beta)


def _convert_mixers(mixers: Dict[str, QuaConfigMixerDec]) -> Dict[str, List[MixerConfigType]]:
    ret: Dict[str, List[MixerConfigType]] = {}
    for name, data in mixers.items():
        temp_list: List[MixerConfigType] = []
        for correction in data.correction:
            if correction.frequency_double:
                frequency = correction.frequency_double
            else:
                frequency = correction.frequency

            if correction.frequency_negative:
                frequency = -frequency

            if correction.lo_frequency_double:
                lo_frequency = correction.lo_frequency_double
            else:
                lo_frequency = correction.lo_frequency

            temp_dict: MixerConfigType = {
                "intermediate_frequency": frequency,
                "lo_frequency": lo_frequency,
                "correction": _convert_matrix(correction.correction),
            }
            temp_list.append(temp_dict)

        ret[name] = temp_list
    return ret


def _convert_matrix(matrix: QuaConfigMatrix) -> Tuple[Number, Number, Number, Number]:
    return matrix.v00, matrix.v01, matrix.v10, matrix.v11


def _convert_integration_weights(
    integration_weights: Dict[str, QuaConfigIntegrationWeightDec]
) -> Dict[str, IntegrationWeightConfigType]:
    ret: Dict[str, IntegrationWeightConfigType] = {}
    for name, data in integration_weights.items():
        tmp: IntegrationWeightConfigType = {
            "cosine": [(s.value, s.length) for s in data.cosine],
            "sine": [(s.value, s.length) for s in data.sine],
        }
        ret[name] = tmp
    return ret


def _convert_digital_wave_forms(
    digital_wave_forms: Dict[str, QuaConfigDigitalWaveformDec]
) -> Dict[str, DigitalWaveformConfigType]:
    ret: Dict[str, DigitalWaveformConfigType] = {}
    for name, data in digital_wave_forms.items():
        temp_list: List[Tuple[int, int]] = []
        for sample in data.samples:
            value = int(bool(sample.value))
            temp_list.append((value, sample.length))

        ret[name] = {"samples": temp_list}
    return ret


def _convert_wave_forms(
    wave_forms: Dict[str, QuaConfigWaveformDec]
) -> Dict[str, Union[ArbitraryWaveFormConfigType, ConstantWaveFormConfigType, CompressedWaveFormConfigType]]:
    ret: Dict[str, Union[ArbitraryWaveFormConfigType, ConstantWaveFormConfigType, CompressedWaveFormConfigType]] = {}
    for name, data in wave_forms.items():
        key_name, curr_waveform = betterproto.which_one_of(data, "waveform_oneof")
        if isinstance(curr_waveform, QuaConfigArbitraryWaveformDec):

            arbitrary_waveform_dict: ArbitraryWaveFormConfigType = {
                "type": "arbitrary",
                "samples": curr_waveform.samples,
                "is_overridable": curr_waveform.is_overridable,
            }
            if isinstance(curr_waveform.max_allowed_error, float):
                arbitrary_waveform_dict["max_allowed_error"] = curr_waveform.max_allowed_error
            if isinstance(curr_waveform.sampling_rate, float):
                arbitrary_waveform_dict["sampling_rate"] = curr_waveform.sampling_rate
            ret[name] = arbitrary_waveform_dict

        elif isinstance(curr_waveform, QuaConfigConstantWaveformDec):
            constant_waveform_dict: ConstantWaveFormConfigType = {
                "type": "constant",
                "sample": curr_waveform.sample,
            }
            ret[name] = constant_waveform_dict
        elif isinstance(curr_waveform, QuaConfigCompressedWaveformDec):
            warnings.warn("Compressed waveform is deprecated.", DeprecationWarning)
            compressed_waveform_dict: CompressedWaveFormConfigType = {
                "type": "compressed",
                "samples": curr_waveform.samples,
                "sample_rate": curr_waveform.sample_rate,
            }
            ret[name] = compressed_waveform_dict
        else:
            raise Exception(f"Unknown waveform type - {key_name}")

    return ret


def _convert_pulses(pulses: Dict[str, QuaConfigPulseDec]) -> Dict[str, PulseConfigType]:
    ret = {}
    for name, data in pulses.items():
        temp_dict: PulseConfigType = {
            "length": data.length,
            "waveforms": data.waveforms,
            "integration_weights": data.integration_weights,
            "operation": cast(
                Literal["measurement", "control"], QuaConfigPulseDecOperation(data.operation).name.lower()
            ),
        }
        if isinstance(data.digital_marker, str):
            temp_dict["digital_marker"] = data.digital_marker
        ret[name] = temp_dict
    return ret


def _convert_v1_beta(config: QuaConfigQuaConfigV1) -> DictQuaConfig:
    if config.control_devices:
        controllers = _convert_controller_types(config.control_devices)
    elif config.controllers:
        controllers = {name: _convert_controller(controller) for name, controller in config.controllers.items()}
    else:
        controllers = {}
    result: DictQuaConfig = {
        "version": 1,
        "controllers": controllers,
        "oscillators": _convert_oscillators(config.oscillators),
        "elements": _convert_elements(config.elements),
        "pulses": _convert_pulses(config.pulses),
        "waveforms": _convert_wave_forms(config.waveforms),
        "digital_waveforms": _convert_digital_wave_forms(config.digital_waveforms),
        "integration_weights": _convert_integration_weights(config.integration_weights),
        "mixers": _convert_mixers(config.mixers),
    }
    return result


def _convert_controller(data: QuaConfigControllerDec) -> ControllerConfigType:
    return {
        "type": cast(Literal["opx", "opx1"], data.type),
        "analog_outputs": _convert_controller_analog_outputs(data.analog_outputs),
        "analog_inputs": _convert_controller_analog_inputs(data.analog_inputs),
        "digital_outputs": _convert_controller_digital_outputs(data.digital_outputs),
        "digital_inputs": _convert_controller_digital_inputs(data.digital_inputs),
    }


def _convert_controller_types(
    controllers: Dict[str, QuaConfigDeviceDec]
) -> Dict[str, Union[ControllerConfigType, OPX1000ControllerConfigType]]:
    ret: Dict[str, Union[ControllerConfigType, OPX1000ControllerConfigType]] = {}
    for name, data in controllers.items():
        if len(data.fems) == 1 and 1 in data.fems and betterproto.serialized_on_wire(data.fems[1].opx):
            ret[name] = _convert_controller(data.fems[1].opx)
        else:
            to_attach: OPX1000ControllerConfigType = {
                "type": "opx1000",
                "fems": {fem_idx: _convert_fem(fem) for fem_idx, fem in data.fems.items()},
            }
            ret[name] = to_attach

    return ret


def _convert_fem(data: QuaConfigFemTypes) -> Union[LfFemConfigType, MwFemConfigType]:
    _, fem_config = betterproto.which_one_of(data, "fem_type_one_of")
    if isinstance(fem_config, QuaConfigOctoDacFemDec):
        return _convert_octo_dac(fem_config)
    elif isinstance(fem_config, QuaConfigMicrowaveFemDec):
        return _convert_mw_fem(fem_config)
    else:
        raise ValueError(f"Unknown FEM type - {fem_config}")


def _convert_mw_fem(data: QuaConfigMicrowaveFemDec) -> MwFemConfigType:
    ret: MwFemConfigType = {"type": "MW"}
    if data.analog_outputs:
        ret["analog_outputs"] = _convert_mw_analog_outputs(data.analog_outputs)
    if data.analog_inputs:
        ret["analog_inputs"] = _convert_mw_analog_inputs(data.analog_inputs)
    if data.digital_outputs:
        ret["digital_outputs"] = _convert_controller_digital_outputs(data.digital_outputs)
    if data.digital_inputs:
        ret["digital_inputs"] = _convert_controller_digital_inputs(data.digital_inputs)
    return ret


def _convert_mw_analog_outputs(
    outputs: Dict[int, QuaConfigMicrowaveAnalogOutputPortDec]
) -> Dict[int, MwFemAnalogOutputPortConfigType]:
    return {
        idx: {
            "sampling_rate": output.sampling_rate,
            "full_scale_power_dbm": output.full_scale_power_dbm,
            "band": cast(Literal[1, 2, 3], output.band),
            "delay": output.delay,
            "shareable": output.shareable,
        }
        for idx, output in outputs.items()
    }


def _convert_mw_analog_inputs(
    inputs: Dict[int, QuaConfigMicrowaveAnalogInputPortDec]
) -> Dict[int, MwFemAnalogInputPortConfigType]:
    return {
        idx: {
            "band": cast(Literal[1, 3, 3], _input.band),
            "shareable": _input.shareable,
            "gain_db": _input.gain_db,
            "sampling_rate": _input.sampling_rate,
        }
        for idx, _input in inputs.items()
    }


def _convert_octo_dac(data: QuaConfigOctoDacFemDec) -> LfFemConfigType:
    ret: LfFemConfigType = {"type": "LF"}
    if data.analog_outputs:
        ret["analog_outputs"] = _convert_octo_dac_fem_analog_outputs(data.analog_outputs)
    if data.analog_inputs:
        ret["analog_inputs"] = _convert_controller_analog_inputs(data.analog_inputs)
    if data.digital_outputs:
        ret["digital_outputs"] = _convert_controller_digital_outputs(data.digital_outputs)
    if data.digital_inputs:
        ret["digital_inputs"] = _convert_controller_digital_inputs(data.digital_inputs)
    return ret


def _convert_inputs(inputs: Dict[str, QuaConfigDigitalInputPortReference]) -> Dict[str, DigitalInputConfigType]:
    ret: Dict[str, DigitalInputConfigType] = {}
    for name, data in inputs.items():
        ret[name] = {"delay": data.delay, "buffer": data.buffer, "port": _port_reference(data.port)}
    return ret


def _convert_digital_output(outputs: Dict[str, QuaConfigDigitalOutputPortReference]) -> Dict[str, PortReferenceType]:
    ret = {}
    for name, data in outputs.items():
        ret[name] = _port_reference(data.port)

    return ret


def _convert_single_input_collection(data: QuaConfigSingleInputCollection) -> InputCollectionConfigType:
    temp = {}
    for name, input_info in data.inputs.items():
        temp[name] = _port_reference(input_info)

    res: InputCollectionConfigType = {"inputs": temp}
    return res


def _convert_multiple_inputs(data: QuaConfigMultipleInputs) -> InputCollectionConfigType:
    temp = {}
    for name, input_info in data.inputs.items():
        temp[name] = _port_reference(input_info)

    res: InputCollectionConfigType = {"inputs": temp}
    return res


def _convert_oscillators(oscillator: Dict[str, QuaConfigOscillator]) -> Dict[str, OscillatorConfigType]:
    ret: Dict[str, OscillatorConfigType] = {}
    for name, data in oscillator.items():
        oscillator_config_data: OscillatorConfigType = {}
        if data.intermediate_frequency_double:
            freq = data.intermediate_frequency_double
            oscillator_config_data["intermediate_frequency"] = freq
        elif data.intermediate_frequency:
            freq = int(data.intermediate_frequency)
            oscillator_config_data["intermediate_frequency"] = freq
        if betterproto.serialized_on_wire(data.mixer):
            if data.mixer.mixer:
                oscillator_config_data["mixer"] = data.mixer.mixer
            if data.mixer.lo_frequency_double:
                lo_freq = data.mixer.lo_frequency_double
                oscillator_config_data["lo_frequency"] = float(lo_freq)
            elif data.mixer.lo_frequency:
                lo_freq = data.mixer.lo_frequency
                oscillator_config_data["lo_frequency"] = int(lo_freq)
        ret[name] = oscillator_config_data
    return ret


def _convert_elements(elements: Dict[str, QuaConfigElementDec]) -> Dict[str, ElementConfigType]:
    ret: Dict[str, ElementConfigType] = {}
    for name, data in elements.items():
        element_config_data: ElementConfigType = {
            "digitalInputs": _convert_inputs(data.digital_inputs),
            "digitalOutputs": _convert_digital_output(data.digital_outputs),
            "outputs": _convert_element_output(data.outputs, data.multiple_outputs),
            "operations": data.operations,
            "hold_offset": _convert_hold_offset(data.hold_offset),
            "sticky": _convert_sticky(data.sticky),
            "thread": _convert_element_thread(data.thread),
        }
        if betterproto.serialized_on_wire(data.single_input):
            element_config_data["singleInput"] = _convert_single_inputs(data.single_input)
        if betterproto.serialized_on_wire(data.mix_inputs):
            element_config_data["mixInputs"] = _convert_mix_inputs(data.mix_inputs)
        if betterproto.serialized_on_wire(data.single_input_collection):
            element_config_data["singleInputCollection"] = _convert_single_input_collection(
                data.single_input_collection
            )
        if betterproto.serialized_on_wire(data.multiple_inputs):
            element_config_data["multipleInputs"] = _convert_multiple_inputs(data.multiple_inputs)
        if betterproto.serialized_on_wire(data.microwave_output):
            element_config_data["MWOutput"] = _convert_element_mw_output(data.microwave_output)
        if betterproto.serialized_on_wire(data.microwave_input):
            element_config_data["MWInput"] = _convert_element_mw_input(data.microwave_input)
        if data.smearing is not None:
            element_config_data["smearing"] = data.smearing
        if data.time_of_flight is not None:
            element_config_data["time_of_flight"] = data.time_of_flight
        if data.measurement_qe:
            element_config_data["measurement_qe"] = data.measurement_qe

        if data.named_oscillator:
            element_config_data["oscillator"] = data.named_oscillator
        else:
            sign = (-1) ** data.intermediate_frequency_negative
            if data.intermediate_frequency_double:
                element_config_data["intermediate_frequency"] = abs(data.intermediate_frequency_double) * sign
            elif data.intermediate_frequency is not None:
                element_config_data["intermediate_frequency"] = abs(data.intermediate_frequency) * sign

        ret[name] = element_config_data

    return ret


def _convert_mix_inputs(mix_inputs: QuaConfigMixInputs) -> MixInputConfigType:
    res: MixInputConfigType = {"I": _port_reference(mix_inputs.i), "Q": _port_reference(mix_inputs.q)}

    mixer = mix_inputs.mixer
    if mixer is not None:
        res["mixer"] = mixer

    if mix_inputs.lo_frequency_double:
        res["lo_frequency"] = mix_inputs.lo_frequency_double
    else:
        res["lo_frequency"] = float(mix_inputs.lo_frequency)

    return res


def _convert_single_inputs(single: QuaConfigSingleInput) -> SingleInputConfigType:
    return {"port": _port_reference(single.port)}


def _convert_hold_offset(hold_offset: QuaConfigHoldOffset) -> HoldOffsetConfigType:
    return {"duration": hold_offset.duration}


def _convert_sticky(sticky: QuaConfigSticky) -> StickyConfigType:
    res: StickyConfigType = {
        "analog": sticky.analog,
        "digital": sticky.digital,
        "duration": max(sticky.duration, 1) * 4,
    }
    return res


def _convert_element_mw_input(data: QuaConfigMicrowaveInputPortReference) -> MwInputConfigType:
    return {
        "port": _port_reference(data.port),
        "oscillator_frequency": data.oscillator_frequency_hz,
    }


def _convert_element_mw_output(data: QuaConfigMicrowaveOutputPortReference) -> MwOutputConfigType:
    return {
        "port": _port_reference(data.port),
        "oscillator_frequency": data.oscillator_frequency_hz,
    }


def _convert_element_thread(element_thread: QuaConfigElementThread) -> str:
    return element_thread.thread_name


def _convert_controller_analog_outputs(
    outputs: Dict[int, QuaConfigAnalogOutputPortDec]
) -> Dict[int, AnalogOutputPortConfigType]:
    ret = {}
    for name, data in outputs.items():
        port_info: AnalogOutputPortConfigType = {
            "offset": data.offset,
            "delay": data.delay,
            "shareable": data.shareable,
            "filter": {"feedforward": data.filter.feedforward, "feedback": data.filter.feedback},
            "crosstalk": data.crosstalk,
        }
        ret[int(name)] = port_info
    return ret


def _convert_octo_dac_fem_analog_outputs(
    outputs: Dict[int, QuaConfigOctoDacAnalogOutputPortDec]
) -> Dict[int, AnalogOutputPortConfigTypeOctoDac]:
    ret = {}
    for name, data in outputs.items():
        port_info: AnalogOutputPortConfigTypeOctoDac = {
            "offset": data.offset,
            "delay": data.delay,
            "shareable": data.shareable,
            "filter": {"feedforward": data.filter.feedforward, "feedback": data.filter.feedback},
            "crosstalk": data.crosstalk,
            "output_mode": cast(
                Literal["direct", "amplified"], QuaConfigOctoDacAnalogOutputPortDecOutputMode(data.output_mode).name
            ),
        }
        if data.sampling_rate:
            port_info["sampling_rate"] = {1: 1e9, 2: 2e9}[data.sampling_rate]
        if data.upsampling_mode:
            port_info["upsampling_mode"] = cast(
                Literal["mw", "pulse"], QuaConfigOctoDacAnalogOutputPortDecSamplingRateMode(data.upsampling_mode).name
            )
        ret[int(name)] = port_info
    return ret


def _convert_controller_analog_inputs(
    inputs: Dict[int, QuaConfigAnalogInputPortDec]
) -> Dict[int, AnalogInputPortConfigType]:
    ret: Dict[int, AnalogInputPortConfigType] = {}
    for idx, data in inputs.items():
        port_info: AnalogInputPortConfigType = {
            "offset": data.offset,
            "gain_db": data.gain_db if data.gain_db is not None else 0,
            "shareable": data.shareable,
        }
        ret[idx] = port_info
    return ret


def _convert_controller_digital_outputs(
    outputs: Dict[int, QuaConfigDigitalOutputPortDec]
) -> Dict[int, DigitalOutputPortConfigType]:
    return {idx: _convert_controller_digital_output(data) for idx, data in outputs.items()}


def _convert_controller_digital_output(data: QuaConfigDigitalOutputPortDec) -> DigitalOutputPortConfigType:
    to_return: DigitalOutputPortConfigType = {
        "shareable": data.shareable,
        "inverted": data.inverted,
    }
    if data.level is not None:
        to_return["level"] = "TTL" if data.level == 1 else "LVTTL"
    return to_return


def _convert_controller_digital_inputs(
    inputs: Dict[int, QuaConfigDigitalInputPortDec]
) -> Dict[int, DigitalInputPortConfigType]:
    ret: Dict[int, DigitalInputPortConfigType] = {}
    for idx, data in inputs.items():
        port_info: DigitalInputPortConfigType = {
            "polarity": cast(Literal["RISING", "FALLING"], QuaConfigDigitalInputPortDecPolarity(data.polarity).name),
            "deadtime": data.deadtime,
            "threshold": data.threshold,
            "shareable": data.shareable,
        }
        ret[idx] = port_info
    return ret


def _convert_element_output(
    outputs: Dict[str, QuaConfigAdcPortReference], multiple_outputs: QuaConfigMultipleOutputs
) -> Dict[str, PortReferenceType]:
    if multiple_outputs:
        return {name: _port_reference(data) for name, data in multiple_outputs.port_references.items()}
    return {name: _port_reference(data) for name, data in outputs.items()}


def _port_reference(
    data: Union[QuaConfigAdcPortReference, QuaConfigDacPortReference, QuaConfigPortReference]
) -> PortReferenceType:
    if data.fem:
        return data.controller, data.fem, data.number
    else:
        return data.controller, data.number
