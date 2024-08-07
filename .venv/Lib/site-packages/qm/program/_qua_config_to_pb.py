import uuid
import numbers
from typing import Dict, List, Type, Tuple, Union, TypeVar, Optional, cast

import betterproto
from betterproto.lib.google.protobuf import Empty
from dependency_injector.wiring import Provide, inject

from qm.utils.config_utils import get_fem_config_instance
from qm.utils.list_compression_utils import split_list_to_chunks
from qm.api.models.capabilities import OPX_FEM_IDX, ServerCapabilities
from qm.containers.capabilities_container import CapabilitiesContainer
from qm.exceptions import (
    InvalidOctaveParameter,
    NoInputsOrOutputsError,
    ConfigValidationException,
    OctaveConnectionAmbiguity,
    ElementInputConnectionAmbiguity,
    ElementOutputConnectionAmbiguity,
)
from qm.program._validate_config_schema import (
    validate_oscillator,
    validate_output_tof,
    validate_used_inputs,
    validate_output_smearing,
    validate_sticky_duration,
    validate_arbitrary_waveform,
    validate_timetagging_parameters,
)
from qm.type_hinting.config_types import (
    LoopbackType,
    StandardPort,
    DictQuaConfig,
    LfFemConfigType,
    MixerConfigType,
    MwFemConfigType,
    PulseConfigType,
    OctaveConfigType,
    ElementConfigType,
    PortReferenceType,
    ControllerConfigType,
    OscillatorConfigType,
    DigitalInputConfigType,
    OctaveRFInputConfigType,
    OctaveRFOutputConfigType,
    AnalogInputPortConfigType,
    DigitalWaveformConfigType,
    OctaveIfOutputsConfigType,
    AnalogOutputPortConfigType,
    ConstantWaveFormConfigType,
    DigitalInputPortConfigType,
    ArbitraryWaveFormConfigType,
    DigitalOutputPortConfigType,
    IntegrationWeightConfigType,
    OPX1000ControllerConfigType,
    MwFemAnalogInputPortConfigType,
    OctaveSingleIfOutputConfigType,
    MwFemAnalogOutputPortConfigType,
    AnalogOutputPortConfigTypeOctoDac,
)
from qm.grpc.qua_config import (
    QuaConfig,
    QuaConfigMatrix,
    QuaConfigSticky,
    QuaConfigFemTypes,
    QuaConfigMixerDec,
    QuaConfigMixerRef,
    QuaConfigPulseDec,
    QuaConfigDeviceDec,
    QuaConfigMixInputs,
    QuaConfigElementDec,
    QuaConfigHoldOffset,
    QuaConfigOscillator,
    QuaConfigQuaConfigV1,
    QuaConfigSingleInput,
    QuaConfigWaveformDec,
    QuaConfigOctaveConfig,
    QuaConfigOctaveIfMode,
    QuaConfigVoltageLevel,
    QuaConfigControllerDec,
    QuaConfigElementThread,
    QuaConfigOctoDacFemDec,
    QuaConfigPortReference,
    QuaConfigMultipleInputs,
    QuaConfigOctaveLoopback,
    QuaConfigCorrectionEntry,
    QuaConfigMicrowaveFemDec,
    QuaConfigAdcPortReference,
    QuaConfigDacPortReference,
    QuaConfigPulseDecOperation,
    QuaConfigAnalogInputPortDec,
    QuaConfigDigitalWaveformDec,
    QuaConfigAnalogOutputPortDec,
    QuaConfigConstantWaveformDec,
    QuaConfigDigitalInputPortDec,
    QuaConfigOctaveLoopbackInput,
    QuaConfigOctaveLoSourceInput,
    QuaConfigOctaveRfInputConfig,
    QuaConfigArbitraryWaveformDec,
    QuaConfigDigitalOutputPortDec,
    QuaConfigGeneralPortReference,
    QuaConfigIntegrationWeightDec,
    QuaConfigOctaveRfOutputConfig,
    QuaConfigDigitalWaveformSample,
    QuaConfigOctaveIfOutputsConfig,
    QuaConfigOctaveSynthesizerPort,
    QuaConfigOutputPulseParameters,
    QuaConfigSingleInputCollection,
    QuaConfigAnalogOutputPortFilter,
    QuaConfigIntegrationWeightSample,
    QuaConfigOctaveOutputSwitchState,
    QuaConfigDigitalInputPortReference,
    QuaConfigDigitalOutputPortReference,
    QuaConfigOctaveSingleIfOutputConfig,
    QuaConfigOctoDacAnalogOutputPortDec,
    QuaConfigDigitalInputPortDecPolarity,
    QuaConfigMicrowaveAnalogInputPortDec,
    QuaConfigMicrowaveInputPortReference,
    QuaConfigOctaveDownconverterRfSource,
    QuaConfigOctaveSynthesizerOutputName,
    QuaConfigMicrowaveAnalogOutputPortDec,
    QuaConfigMicrowaveOutputPortReference,
    QuaConfigOutputPulseParametersPolarity,
    QuaConfigOctoDacAnalogOutputPortDecOutputMode,
    QuaConfigOctoDacAnalogOutputPortDecSamplingRate,
    QuaConfigOctoDacAnalogOutputPortDecSamplingRateMode,
)

ALLOWED_GAINES = {x / 2 for x in range(-40, 41)}


def _analog_input_port_to_pb(data: AnalogInputPortConfigType) -> QuaConfigAnalogInputPortDec:
    analog_input = QuaConfigAnalogInputPortDec(
        offset=data.get("offset", 0.0),
        shareable=bool(data.get("shareable")),
        gain_db=int(data.get("gain_db", 0)),
        sampling_rate=int(data.get("sampling_rate", 1e9)),
    )
    return analog_input


def mw_fem_analog_input_port_to_pb(data: MwFemAnalogInputPortConfigType) -> QuaConfigMicrowaveAnalogInputPortDec:
    analog_input = QuaConfigMicrowaveAnalogInputPortDec(
        sampling_rate=data.get("sampling_rate", 1e9),
        gain_db=data.get("gain_db", 0),
        shareable=data.get("shareable", False),
        band=data["band"],
    )
    return analog_input


def _get_port_reference_with_fem(reference: PortReferenceType) -> StandardPort:
    if len(reference) == 2:
        return reference[0], OPX_FEM_IDX, reference[1]
    else:
        return reference


AnalogOutputType = TypeVar("AnalogOutputType", QuaConfigAnalogOutputPortDec, QuaConfigOctoDacAnalogOutputPortDec)


def _analog_output_port_to_pb(
    data: AnalogOutputPortConfigType,
    output_type: Type[AnalogOutputType],
) -> AnalogOutputType:
    analog_output = output_type(shareable=bool(data.get("shareable")))

    if "offset" in data:
        analog_output.offset = data["offset"]

    if "delay" in data:
        delay = data.get("delay", 0)
        if delay < 0:
            raise ConfigValidationException(f"analog output delay cannot be a negative value, given value: {delay}")
        analog_output.delay = delay

    if "filter" in data:
        analog_output.filter = QuaConfigAnalogOutputPortFilter(
            feedforward=data["filter"]["feedforward"],
            feedback=data["filter"]["feedback"],
        )

    if "crosstalk" in data:
        for k, v in data["crosstalk"].items():
            analog_output.crosstalk[int(k)] = v

    return analog_output


def create_sampling_rate_enum(
    data: AnalogOutputPortConfigTypeOctoDac,
) -> QuaConfigOctoDacAnalogOutputPortDecSamplingRate:
    sampling_rate_float = data.get("sampling_rate", 1e9)
    if sampling_rate_float not in {1e9, 2e9}:
        raise ValueError("Sampling rate should be either 1e9 or 2e9")
    sampling_rate_gsps = int(sampling_rate_float / 1e9)
    return QuaConfigOctoDacAnalogOutputPortDecSamplingRate(sampling_rate_gsps)


def _opx_1000_analog_output_port_to_pb(
    data: AnalogOutputPortConfigTypeOctoDac,
) -> QuaConfigOctoDacAnalogOutputPortDec:
    item = _analog_output_port_to_pb(data, output_type=QuaConfigOctoDacAnalogOutputPortDec)
    item.sampling_rate = create_sampling_rate_enum(data)
    if item.sampling_rate == QuaConfigOctoDacAnalogOutputPortDecSamplingRate.GSPS1:
        item.upsampling_mode = QuaConfigOctoDacAnalogOutputPortDecSamplingRateMode[data.get("upsampling_mode", "mw")]
    else:
        if "upsampling_mode" in data:
            raise ConfigValidationException("Sampling rate mode is only relevant for sampling rate of 1GHz.")
    item.output_mode = QuaConfigOctoDacAnalogOutputPortDecOutputMode[data.get("output_mode", "direct")]
    return item


def mw_fem_analog_output_to_pb(
    data: MwFemAnalogOutputPortConfigType,
) -> QuaConfigMicrowaveAnalogOutputPortDec:
    item = QuaConfigMicrowaveAnalogOutputPortDec(
        sampling_rate=data.get("sampling_rate", 1e9),
        full_scale_power_dbm=data.get("full_scale_power_dbm", 0),
        band=data["band"],
        delay=data.get("delay", 0),
        shareable=data.get("shareable", False),
    )
    return item


def digital_output_port_to_pb(data: DigitalOutputPortConfigType) -> QuaConfigDigitalOutputPortDec:
    digital_output = QuaConfigDigitalOutputPortDec(
        shareable=data.get("shareable", False),
        inverted=data.get("inverted", False),
        level=QuaConfigVoltageLevel[data.get("level", "LVTTL").upper()],
    )
    return digital_output


def digital_input_port_to_pb(data: DigitalInputPortConfigType) -> QuaConfigDigitalInputPortDec:
    digital_input = QuaConfigDigitalInputPortDec(shareable=bool(data.get("shareable")))

    if "threshold" in data:
        digital_input.threshold = data["threshold"]

    if "polarity" in data:
        if data["polarity"].upper() == "RISING":
            digital_input.polarity = QuaConfigDigitalInputPortDecPolarity.RISING
        elif data["polarity"].upper() == "FALLING":
            digital_input.polarity = QuaConfigDigitalInputPortDecPolarity.FALLING

    if "deadtime" in data:
        digital_input.deadtime = int(data["deadtime"])

    return digital_input


def controlling_devices_to_pb(data: Union[ControllerConfigType, OPX1000ControllerConfigType]) -> QuaConfigDeviceDec:
    fems: Dict[int, QuaConfigFemTypes] = {}

    if "fems" in data:
        data = cast(OPX1000ControllerConfigType, data)
        # Here we assume that we don't declare OPX as FEM
        if set(data) & {"analog", "analog_outputs", "digital_outputs", "digital_inputs"}:
            raise Exception(
                "'analog', 'analog_outputs', 'digital_outputs' and 'digital_inputs' are not allowed when 'fems' is present"
            )
        for k, v in data["fems"].items():
            if v.get("type") == "MW":
                fems[k] = _mw_fem_to_pb(cast(MwFemConfigType, v))
            else:
                fems[k] = _fem_to_pb(cast(LfFemConfigType, v))

    else:
        data = cast(ControllerConfigType, data)
        fems[OPX_FEM_IDX] = _controller_to_pb(data)

    item = QuaConfigDeviceDec(fems=fems)
    return item


def _controller_to_pb(data: ControllerConfigType) -> QuaConfigFemTypes:
    cont = QuaConfigControllerDec(type=data.get("type", "opx1"))
    cont = _set_ports_in_config(cont, data)
    return QuaConfigFemTypes(opx=cont)


def _fem_to_pb(data: LfFemConfigType) -> QuaConfigFemTypes:
    cont = QuaConfigOctoDacFemDec()
    cont = _set_ports_in_config(cont, data)
    return QuaConfigFemTypes(octo_dac=cont)


def _mw_fem_to_pb(data: MwFemConfigType) -> QuaConfigFemTypes:
    cont = QuaConfigMicrowaveFemDec()
    cont = _set_ports_in_config(cont, data)
    return QuaConfigFemTypes(microwave=cont)


ControllerConfigTypeVar = TypeVar(
    "ControllerConfigTypeVar", QuaConfigOctoDacFemDec, QuaConfigControllerDec, QuaConfigMicrowaveFemDec
)


def _set_ports_in_config(
    config: ControllerConfigTypeVar, data: Union[ControllerConfigType, LfFemConfigType, MwFemConfigType]
) -> ControllerConfigTypeVar:
    if "analog_outputs" in data:
        for analog_output_idx, analog_output_data in data["analog_outputs"].items():
            int_k = int(analog_output_idx)
            if isinstance(config, QuaConfigControllerDec):
                analog_output_data = cast(AnalogOutputPortConfigType, analog_output_data)
                config.analog_outputs[int_k] = _analog_output_port_to_pb(
                    analog_output_data, output_type=QuaConfigAnalogOutputPortDec
                )
            elif isinstance(config, QuaConfigOctoDacFemDec):
                analog_output_data = cast(AnalogOutputPortConfigTypeOctoDac, analog_output_data)
                config.analog_outputs[int_k] = _opx_1000_analog_output_port_to_pb(analog_output_data)
            elif isinstance(config, QuaConfigMicrowaveFemDec):
                analog_output_data = cast(MwFemAnalogOutputPortConfigType, analog_output_data)
                config.analog_outputs[int_k] = mw_fem_analog_output_to_pb(analog_output_data)
            else:
                raise ValueError(f"Unknown config type {type(config)}")

    if "analog_inputs" in data:
        if isinstance(config, (QuaConfigControllerDec, QuaConfigOctoDacFemDec)):
            for analog_input_idx, analog_input_data in data["analog_inputs"].items():
                analog_input_data = cast(AnalogInputPortConfigType, analog_input_data)
                config.analog_inputs[int(analog_input_idx)] = _analog_input_port_to_pb(analog_input_data)
        elif isinstance(config, QuaConfigMicrowaveFemDec):
            for analog_input_idx, analog_input_data_mw in data["analog_inputs"].items():
                analog_input_data_mw = cast(MwFemAnalogInputPortConfigType, analog_input_data_mw)
                config.analog_inputs[int(analog_input_idx)] = mw_fem_analog_input_port_to_pb(analog_input_data_mw)
        else:
            raise ValueError(f"Unknown config type {type(config)}")

    if "digital_outputs" in data:
        for digital_output_idx, digital_output_data in data["digital_outputs"].items():
            config.digital_outputs[int(digital_output_idx)] = digital_output_port_to_pb(digital_output_data)

    if "digital_inputs" in data:
        for digital_input_idx, digital_input_data in data["digital_inputs"].items():
            config.digital_inputs[int(digital_input_idx)] = digital_input_port_to_pb(digital_input_data)

    return config


def get_octave_loopbacks(data: List[LoopbackType]) -> List[QuaConfigOctaveLoopback]:
    loopbacks = [
        QuaConfigOctaveLoopback(
            lo_source_input=QuaConfigOctaveLoopbackInput[loopback[1]],
            lo_source_generator=QuaConfigOctaveSynthesizerPort(
                device_name=loopback[0][0],
                port_name=QuaConfigOctaveSynthesizerOutputName[loopback[0][1].lower()],
            ),
        )
        for loopback in data
    ]
    return loopbacks


def octave_to_pb(data: OctaveConfigType) -> QuaConfigOctaveConfig:
    connectivity = data.get("connectivity", None)
    if isinstance(connectivity, str):
        connectivity = (connectivity, OPX_FEM_IDX)
    loopbacks = get_octave_loopbacks(data.get("loopbacks", []))
    rf_modules = {
        k: rf_module_to_pb(standardize_connectivity_for_if_in(v, connectivity, k))
        for k, v in data.get("RF_outputs", {}).items()
    }
    rf_inputs = {k: rf_input_to_pb(v, k) for k, v in data.get("RF_inputs", {}).items()}
    if_outputs = _octave_if_outputs_to_pb(standardize_connectivity_for_if_out(data.get("IF_outputs", {}), connectivity))
    return QuaConfigOctaveConfig(
        loopbacks=loopbacks,
        rf_outputs=rf_modules,
        rf_inputs=rf_inputs,
        if_outputs=if_outputs,
    )


def standardize_connectivity_for_if_in(
    data: OctaveRFOutputConfigType, controller_connectivity: Optional[Tuple[str, int]], module_number: int
) -> OctaveRFOutputConfigType:
    if controller_connectivity is not None:
        if ("I_connection" in data) or ("Q_connection" in data):
            raise OctaveConnectionAmbiguity()

        data["I_connection"] = controller_connectivity + (2 * module_number - 1,)
        data["Q_connection"] = controller_connectivity + (2 * module_number,)
    return data


IF_OUT1_DEFAULT = "out1"
IF_OUT2_DEFAULT = "out2"


def standardize_connectivity_for_if_out(
    data: OctaveIfOutputsConfigType, controller_connectivity: Optional[Tuple[str, int]]
) -> OctaveIfOutputsConfigType:
    if controller_connectivity is not None:
        if "IF_out1" not in data:
            data["IF_out1"] = {"name": IF_OUT1_DEFAULT}
        if "IF_out2" not in data:
            data["IF_out2"] = {"name": IF_OUT2_DEFAULT}
        if ("port" in data["IF_out1"]) or ("port" in data["IF_out2"]):
            raise OctaveConnectionAmbiguity()
        data["IF_out1"]["port"] = controller_connectivity + (1,)
        data["IF_out2"]["port"] = controller_connectivity + (2,)
    return data


def _get_lo_frequency(data: Union[OctaveRFOutputConfigType, OctaveRFInputConfigType]) -> float:
    if "LO_frequency" not in data:
        raise ConfigValidationException("No LO frequency was set for upconverter")
    lo_freq = data["LO_frequency"]
    if not 2e9 <= lo_freq <= 18e9:
        raise ConfigValidationException(f"LO frequency {lo_freq} is out of range")
    return lo_freq


def rf_module_to_pb(data: OctaveRFOutputConfigType) -> QuaConfigOctaveRfOutputConfig:
    input_attenuators = data.get("input_attenuators", "OFF").upper()
    if input_attenuators not in {"ON", "OFF"}:
        raise ConfigValidationException("input_attenuators must be either ON or OFF")
    if "gain" not in data:
        raise ConfigValidationException("No gain was set for upconverter")
    gain = float(data["gain"])
    if gain not in ALLOWED_GAINES:
        raise ConfigValidationException(f"Gain should be an integer or half-integer between -20 and 20, got {gain})")
    to_return = QuaConfigOctaveRfOutputConfig(
        lo_frequency=_get_lo_frequency(data),
        lo_source=QuaConfigOctaveLoSourceInput[data.get("LO_source", "internal").lower()],
        output_mode=QuaConfigOctaveOutputSwitchState[data.get("output_mode", "always_off").lower()],
        gain=gain,
        input_attenuators=input_attenuators == "ON",
    )
    if "I_connection" in data:
        to_return.i_connection = dac_port_ref_to_pb(*_get_port_reference_with_fem(data["I_connection"]))
    if "Q_connection" in data:
        to_return.q_connection = dac_port_ref_to_pb(*_get_port_reference_with_fem(data["Q_connection"]))
    return to_return


def rf_input_to_pb(data: OctaveRFInputConfigType, input_idx: int = 0) -> QuaConfigOctaveRfInputConfig:
    input_idx_to_default_lo_source = {0: "not_set", 1: "internal", 2: "external"}  # 0 here is just for the default
    rf_source = QuaConfigOctaveDownconverterRfSource[data.get("RF_source", "RF_in").lower()]
    if input_idx == 1 and rf_source != QuaConfigOctaveDownconverterRfSource.rf_in:
        raise InvalidOctaveParameter("Downconverter 1 must be connected to RF-in")

    lo_source = QuaConfigOctaveLoSourceInput[data.get("LO_source", input_idx_to_default_lo_source[input_idx]).lower()]
    if input_idx == 2 and lo_source == QuaConfigOctaveLoSourceInput.internal:
        raise InvalidOctaveParameter("Downconverter 2 does not have internal LO")

    to_return = QuaConfigOctaveRfInputConfig(
        rf_source=rf_source,
        lo_frequency=_get_lo_frequency(data),
        lo_source=lo_source,
        if_mode_i=QuaConfigOctaveIfMode[data.get("IF_mode_I", "direct").lower()],
        if_mode_q=QuaConfigOctaveIfMode[data.get("IF_mode_Q", "direct").lower()],
    )
    return to_return


def single_if_output_to_pb(data: OctaveSingleIfOutputConfigType) -> QuaConfigOctaveSingleIfOutputConfig:
    controller, fem, number = _get_port_reference_with_fem(data["port"])
    return QuaConfigOctaveSingleIfOutputConfig(
        port=QuaConfigAdcPortReference(controller=controller, fem=fem, number=number), name=data["name"]
    )


def _octave_if_outputs_to_pb(data: OctaveIfOutputsConfigType) -> QuaConfigOctaveIfOutputsConfig:
    inst = QuaConfigOctaveIfOutputsConfig()
    if "IF_out1" in data:
        inst.if_out1 = single_if_output_to_pb(data["IF_out1"])
    if "IF_out2" in data:
        inst.if_out2 = single_if_output_to_pb(data["IF_out2"])
    return inst


@inject
def mixer_ref_to_pb(
    name: str,
    lo_frequency: int,
    capabilities: ServerCapabilities = Provide[CapabilitiesContainer.capabilities],
) -> QuaConfigMixerRef:
    item = QuaConfigMixerRef(mixer=name, lo_frequency=int(lo_frequency))
    if capabilities.supports_double_frequency:
        item.lo_frequency_double = float(lo_frequency)
    return item


@inject
def oscillator_to_pb(
    data: OscillatorConfigType, capabilities: ServerCapabilities = Provide[CapabilitiesContainer.capabilities]
) -> QuaConfigOscillator:
    oscillator = QuaConfigOscillator()
    if "intermediate_frequency" in data:
        oscillator.intermediate_frequency = int(data["intermediate_frequency"])
        if capabilities.supports_double_frequency:
            oscillator.intermediate_frequency_double = float(data["intermediate_frequency"])

    if "mixer" in data:
        oscillator.mixer = QuaConfigMixerRef(mixer=data["mixer"])
        oscillator.mixer.lo_frequency = int(data.get("lo_frequency", 0))
        if capabilities.supports_double_frequency:
            oscillator.mixer.lo_frequency_double = float(data.get("lo_frequency", 0.0))

    return oscillator


@inject
def create_correction_entry(
    mixer_data: MixerConfigType,
    capabilities: ServerCapabilities = Provide[CapabilitiesContainer.capabilities],
) -> QuaConfigCorrectionEntry:
    correction = QuaConfigCorrectionEntry(
        frequency_negative=mixer_data["intermediate_frequency"] < 0,
        correction=QuaConfigMatrix(
            v00=mixer_data["correction"][0],
            v01=mixer_data["correction"][1],
            v10=mixer_data["correction"][2],
            v11=mixer_data["correction"][3],
        ),
    )
    correction.frequency = abs(int(mixer_data["intermediate_frequency"]))
    correction.lo_frequency = int(mixer_data["lo_frequency"])
    if capabilities.supports_double_frequency:
        correction.frequency_double = abs(float(mixer_data["intermediate_frequency"]))
        correction.lo_frequency_double = float(mixer_data["lo_frequency"])

    return correction


def mixer_to_pb(data: List[MixerConfigType]) -> QuaConfigMixerDec:
    return QuaConfigMixerDec(correction=[create_correction_entry(mixer) for mixer in data])


def element_thread_to_pb(name: str) -> QuaConfigElementThread:
    return QuaConfigElementThread(thread_name=name)


def dac_port_ref_to_pb(controller: str, fem: int, number: int) -> QuaConfigDacPortReference:
    return QuaConfigDacPortReference(controller=controller, fem=fem, number=number)


def single_input_to_pb(controller: str, fem: int, number: int) -> QuaConfigSingleInput:
    return QuaConfigSingleInput(port=dac_port_ref_to_pb(controller, fem, number))


def adc_port_ref_to_pb(controller: str, fem: int, number: int) -> QuaConfigAdcPortReference:
    return QuaConfigAdcPortReference(controller=controller, fem=fem, number=number)


def port_ref_to_pb(controller: str, fem: int, number: int) -> QuaConfigPortReference:
    return QuaConfigPortReference(controller=controller, fem=fem, number=number)


def digital_input_port_ref_to_pb(data: DigitalInputConfigType) -> QuaConfigDigitalInputPortReference:
    digital_input = QuaConfigDigitalInputPortReference(
        delay=int(data["delay"]),
        buffer=int(data["buffer"]),
    )
    if "port" in data:
        digital_input.port = port_ref_to_pb(*_get_port_reference_with_fem(data["port"]))

    return digital_input


def digital_output_port_ref_to_pb(data: PortReferenceType) -> QuaConfigDigitalOutputPortReference:
    return QuaConfigDigitalOutputPortReference(port=port_ref_to_pb(*_get_port_reference_with_fem(data)))


@inject
def element_to_pb(
    element_name: str,
    data: ElementConfigType,
    capabilities: ServerCapabilities = Provide[CapabilitiesContainer.capabilities],
) -> QuaConfigElementDec:
    validate_oscillator(data)
    validate_output_smearing(data)
    validate_output_tof(data)
    validate_timetagging_parameters(data)
    validate_used_inputs(data)

    element = QuaConfigElementDec()

    if "time_of_flight" in data:
        element.time_of_flight = int(data["time_of_flight"])

    if "smearing" in data:
        element.smearing = int(data["smearing"])

    if "intermediate_frequency" in data:
        element.intermediate_frequency = abs(int(data["intermediate_frequency"]))
        element.intermediate_frequency_oscillator = int(data["intermediate_frequency"])
        if capabilities.supports_double_frequency:
            element.intermediate_frequency_double = abs(float(data["intermediate_frequency"]))
            element.intermediate_frequency_oscillator_double = float(data["intermediate_frequency"])

        element.intermediate_frequency_negative = data["intermediate_frequency"] < 0

    if "thread" in data:
        element.thread = element_thread_to_pb(data["thread"])

    if "outputs" in data:
        for k, v in data["outputs"].items():
            element.outputs[k] = adc_port_ref_to_pb(*_get_port_reference_with_fem(v))
        element.multiple_outputs.port_references = element.outputs

    if "digitalInputs" in data:
        for digital_input_k, digital_input_v in data["digitalInputs"].items():
            element.digital_inputs[digital_input_k] = digital_input_port_ref_to_pb(digital_input_v)

    if "digitalOutputs" in data:
        for digital_output_k, digital_output_v in data["digitalOutputs"].items():
            element.digital_outputs[digital_output_k] = digital_output_port_ref_to_pb(digital_output_v)

    if "operations" in data:
        for op_name, op_value in data["operations"].items():
            element.operations[op_name] = op_value

    if "singleInput" in data:
        port_ref = _get_port_reference_with_fem(data["singleInput"]["port"])
        element.single_input = single_input_to_pb(*port_ref)

    if "mixInputs" in data:
        mix_inputs = data["mixInputs"]
        element.mix_inputs = QuaConfigMixInputs(
            i=dac_port_ref_to_pb(*_get_port_reference_with_fem(mix_inputs["I"])),
            q=dac_port_ref_to_pb(*_get_port_reference_with_fem(mix_inputs["Q"])),
            mixer=mix_inputs.get("mixer", ""),
        )

        lo_frequency = mix_inputs.get("lo_frequency", 0)
        element.mix_inputs.lo_frequency = int(lo_frequency)
        if capabilities.supports_double_frequency:
            element.mix_inputs.lo_frequency_double = float(lo_frequency)

    if "singleInputCollection" in data:
        element.single_input_collection = QuaConfigSingleInputCollection(
            inputs={
                k: dac_port_ref_to_pb(*_get_port_reference_with_fem(v))
                for k, v in data["singleInputCollection"]["inputs"].items()
            }
        )

    if "multipleInputs" in data:
        element.multiple_inputs = QuaConfigMultipleInputs(
            inputs={
                k: dac_port_ref_to_pb(*_get_port_reference_with_fem(v))
                for k, v in data["multipleInputs"]["inputs"].items()
            }
        )

    if "MWInput" in data:
        element.microwave_input = QuaConfigMicrowaveInputPortReference(
            port=dac_port_ref_to_pb(*_get_port_reference_with_fem(data["MWInput"]["port"])),
            oscillator_frequency_hz=data["MWInput"]["oscillator_frequency"],
        )
    if "MWOutput" in data:
        mw_output = data["MWOutput"]
        element.microwave_output = QuaConfigMicrowaveOutputPortReference(
            port=adc_port_ref_to_pb(*_get_port_reference_with_fem(mw_output["port"])),
            oscillator_frequency_hz=mw_output.get(
                "oscillator_frequency", element.microwave_input.oscillator_frequency_hz
            ),
        )

    if "oscillator" in data:
        element.named_oscillator = data["oscillator"]
    elif "intermediate_frequency" not in data:
        element.no_oscillator = Empty()

    if "sticky" in data:
        if "duration" in data["sticky"]:
            validate_sticky_duration(data["sticky"]["duration"])
        if capabilities.supports_sticky_elements:
            element.sticky = QuaConfigSticky(
                analog=data["sticky"].get("analog", True),
                digital=data["sticky"].get("digital", False),
                duration=int(data["sticky"].get("duration", 4) / 4),
            )
        else:
            if "digital" in data["sticky"] and data["sticky"]["digital"]:
                raise ConfigValidationException(
                    f"Server does not support digital sticky used in element " f"'{element_name}'"
                )
            element.hold_offset = QuaConfigHoldOffset(duration=int(data["sticky"].get("duration", 4) / 4))

    elif "hold_offset" in data:
        if capabilities.supports_sticky_elements:
            element.sticky = QuaConfigSticky(
                analog=True,
                digital=False,
                duration=data["hold_offset"].get("duration", 1),
            )
        else:
            element.hold_offset = QuaConfigHoldOffset(duration=data["hold_offset"]["duration"])

    if "outputPulseParameters" in data:
        pulse_parameters = data["outputPulseParameters"]
        output_pulse_parameters = QuaConfigOutputPulseParameters(
            signal_threshold=pulse_parameters["signalThreshold"],
        )

        signal_polarity = pulse_parameters["signalPolarity"].upper()
        if signal_polarity == "ABOVE" or signal_polarity == "ASCENDING":
            output_pulse_parameters.signal_polarity = QuaConfigOutputPulseParametersPolarity.ASCENDING
        elif signal_polarity == "BELOW" or signal_polarity == "DESCENDING":
            output_pulse_parameters.signal_polarity = QuaConfigOutputPulseParametersPolarity.DESCENDING

        if "derivativeThreshold" in pulse_parameters:
            output_pulse_parameters.derivative_threshold = pulse_parameters["derivativeThreshold"]
            polarity = pulse_parameters["derivativePolarity"].upper()
            if polarity == "ABOVE" or polarity == "ASCENDING":
                output_pulse_parameters.derivative_polarity = QuaConfigOutputPulseParametersPolarity.ASCENDING
            elif polarity == "BELOW" or polarity == "DESCENDING":
                output_pulse_parameters.derivative_polarity = QuaConfigOutputPulseParametersPolarity.DESCENDING

        element.output_pulse_parameters = output_pulse_parameters

    rf_inputs = data.get("RF_inputs", {})
    for k, (device, port) in rf_inputs.items():
        element.rf_inputs[k] = QuaConfigGeneralPortReference(device_name=device, port=port)

    rf_outputs = data.get("RF_outputs", {})
    for k, (device, port) in rf_outputs.items():
        element.rf_outputs[k] = QuaConfigGeneralPortReference(device_name=device, port=port)
    return element


def constant_waveform_to_protobuf(data: ConstantWaveFormConfigType) -> QuaConfigWaveformDec:
    return QuaConfigWaveformDec(constant=QuaConfigConstantWaveformDec(sample=data["sample"]))


def arbitrary_waveform_to_protobuf(data: ArbitraryWaveFormConfigType) -> QuaConfigWaveformDec:
    wf = QuaConfigWaveformDec()

    is_overridable = data.get("is_overridable", False)
    has_max_allowed_error = "max_allowed_error" in data
    has_sampling_rate = "sampling_rate" in data
    validate_arbitrary_waveform(is_overridable, has_max_allowed_error, has_sampling_rate)

    wf.arbitrary = QuaConfigArbitraryWaveformDec(samples=data["samples"], is_overridable=is_overridable)

    if has_max_allowed_error:
        wf.arbitrary.max_allowed_error = data["max_allowed_error"]
    elif has_sampling_rate:
        wf.arbitrary.sampling_rate = data["sampling_rate"]
    elif not is_overridable:
        wf.arbitrary.max_allowed_error = 1e-4
    return wf


def digital_waveform_to_pb(data: DigitalWaveformConfigType) -> QuaConfigDigitalWaveformDec:
    return QuaConfigDigitalWaveformDec(
        samples=[QuaConfigDigitalWaveformSample(value=bool(s[0]), length=s[1]) for s in data["samples"]]
    )


def pulse_to_pb(data: PulseConfigType) -> QuaConfigPulseDec:
    pulse = QuaConfigPulseDec()

    if "length" in data:
        pulse.length = int(data["length"])

    if data["operation"] == "control":
        pulse.operation = QuaConfigPulseDecOperation.CONTROL
    elif data["operation"] == "measurement":
        pulse.operation = QuaConfigPulseDecOperation.MEASUREMENT
    else:
        raise ConfigValidationException(f"Invalid operation {data['operation']}")

    if "digital_marker" in data:
        pulse.digital_marker = data["digital_marker"]

    if "integration_weights" in data:
        for k, v in data["integration_weights"].items():
            pulse.integration_weights[k] = v

    if "waveforms" in data:
        if "single" in data["waveforms"]:
            pulse.waveforms["single"] = data["waveforms"]["single"]

        elif "I" in data["waveforms"]:
            pulse.waveforms["I"] = data["waveforms"]["I"]
            pulse.waveforms["Q"] = data["waveforms"]["Q"]
    return pulse


def _standardize_iw_data(data: Union[List[Tuple[float, int]], List[float]]) -> List[Tuple[float, int]]:
    if len(data) == 0 or isinstance(data[0], (tuple, list)):
        to_return = []
        for x in data:
            x = cast(Tuple[float, int], x)
            to_return.append((x[0], x[1]))
        return to_return

    if isinstance(data[0], numbers.Number):
        if len(data) == 2:
            d0, d1 = cast(Tuple[float, int], data)
            return [(float(d0), int(d1))]

        data = cast(List[float], data)
        chunks = split_list_to_chunks([round(2**-15 * round(s * 2**15), 20) for s in data])
        new_data: List[Tuple[float, int]] = []
        for chunk in chunks:
            if chunk.accepts_different:
                new_data.extend([(float(u), 4) for u in chunk.data])
            else:
                new_data.append((chunk.first, 4 * len(chunk)))
        return new_data

    raise ConfigValidationException(f"Invalid IW data, data must be a list of numbers or 2-tuples, got {data}.")


def build_iw_sample(data: Union[List[Tuple[float, int]], List[float]]) -> List[QuaConfigIntegrationWeightSample]:
    clean_data = _standardize_iw_data(data)
    return [QuaConfigIntegrationWeightSample(value=s[0], length=int(s[1])) for s in clean_data]


def integration_weights_to_pb(data: IntegrationWeightConfigType) -> QuaConfigIntegrationWeightDec:
    iw = QuaConfigIntegrationWeightDec(cosine=build_iw_sample(data["cosine"]), sine=build_iw_sample(data["sine"]))
    return iw


def _all_controllers_are_opx(control_devices: Dict[str, QuaConfigDeviceDec]) -> bool:
    for device_config in control_devices.values():
        for fem_config in device_config.fems.values():
            _, controller_inst = betterproto.which_one_of(fem_config, "fem_type_one_of")
            if not isinstance(controller_inst, QuaConfigControllerDec):
                return False
    return True


def set_octave_upconverter_connection_to_elements(pb_config: QuaConfig) -> None:
    for element in pb_config.v1_beta.elements.values():
        for rf_input in element.rf_inputs.values():
            if rf_input.device_name in pb_config.v1_beta.octaves:
                if rf_input.port in pb_config.v1_beta.octaves[rf_input.device_name].rf_outputs:
                    _, element_input = betterproto.which_one_of(element, "element_inputs_one_of")
                    if element_input is not None:
                        raise ElementInputConnectionAmbiguity("Ambiguous definition of element input")

                    upconverter_config = pb_config.v1_beta.octaves[rf_input.device_name].rf_outputs[rf_input.port]
                    element.mix_inputs = QuaConfigMixInputs(
                        i=upconverter_config.i_connection, q=upconverter_config.q_connection
                    )


def _get_rf_output_for_octave(
    element: QuaConfigElementDec, octaves: Dict[str, QuaConfigOctaveConfig]
) -> Optional[QuaConfigOctaveRfOutputConfig]:
    if element.rf_inputs:
        element_rf_input = list(element.rf_inputs.values())[0]
        octave_config = octaves[element_rf_input.device_name]
        return octave_config.rf_outputs[element_rf_input.port]

    # This part is for users that do not use the rf_inputs  for connecting the octave
    element_input = element.mix_inputs
    for octave in octaves.values():
        for rf_output in octave.rf_outputs.values():
            if all(
                [
                    (rf_output.i_connection.controller == element_input.i.controller),
                    (rf_output.i_connection.fem == element_input.i.fem),
                    (rf_output.i_connection.number == element_input.i.number),
                    (rf_output.q_connection.controller == element_input.q.controller),
                    (rf_output.q_connection.fem == element_input.q.fem),
                    (rf_output.q_connection.number == element_input.q.number),
                ]
            ):
                return rf_output
    return None


@inject
def set_lo_frequency_to_mix_input_elements_that_are_connected_to_octave(
    pb_config: QuaConfig, capabilities: ServerCapabilities = Provide[CapabilitiesContainer.capabilities]
) -> None:
    for element in pb_config.v1_beta.elements.values():
        _, element_input = betterproto.which_one_of(element, "element_inputs_one_of")
        if isinstance(element_input, QuaConfigMixInputs):
            rf_output = _get_rf_output_for_octave(element, pb_config.v1_beta.octaves)
            if rf_output is None:
                continue

            if element_input.lo_frequency not in {0, int(rf_output.lo_frequency)}:
                raise ConfigValidationException(
                    "LO frequency mismatch. The frequency stated in the element is different from "
                    "the one stated in the Octave, remove the one in the element."
                )
            element_input.lo_frequency = int(rf_output.lo_frequency)
            if capabilities.supports_double_frequency:
                element_input.lo_frequency_double = rf_output.lo_frequency


I_IN_PORT = "I"
Q_IN_PORT = "Q"


def set_octave_downconverter_connection_to_elements(pb_config: QuaConfig) -> None:
    for element in pb_config.v1_beta.elements.values():
        for _, rf_output in element.rf_outputs.items():
            if rf_output.device_name in pb_config.v1_beta.octaves:
                if rf_output.port in pb_config.v1_beta.octaves[rf_output.device_name].rf_inputs:
                    downconverter_config = pb_config.v1_beta.octaves[rf_output.device_name].if_outputs
                    outputs_form_octave = {
                        downconverter_config.if_out1.name: downconverter_config.if_out1.port,
                        downconverter_config.if_out2.name: downconverter_config.if_out2.port,
                    }
                    for k, v in outputs_form_octave.items():
                        if k in element.outputs:
                            if v != element.outputs[k]:
                                raise ElementOutputConnectionAmbiguity(
                                    f"Output {k} is connected to {element.outputs[k]} but the octave "
                                    f"downconverter is connected to {v}"
                                )
                        else:
                            element.outputs[k] = v
                            element.multiple_outputs.port_references[k] = v


def set_non_existing_mixers_in_mix_input_elements(pb_config: QuaConfig) -> None:
    for element_name, element in pb_config.v1_beta.elements.items():
        _, element_input = betterproto.which_one_of(element, "element_inputs_one_of")
        if isinstance(element_input, QuaConfigMixInputs):
            if (
                element.intermediate_frequency
            ):  # This is here because in validation I saw that we can set an element without IF
                if not element_input.mixer:
                    element_input.mixer = f"{element_name}_mixer_{uuid.uuid4().hex[:3]}"
                    # The uuid is just to make sure the mixer doesn't exist
                if element_input.mixer not in pb_config.v1_beta.mixers:
                    pb_config.v1_beta.mixers[element_input.mixer] = QuaConfigMixerDec(
                        correction=[
                            QuaConfigCorrectionEntry(
                                frequency=element.intermediate_frequency,
                                frequency_negative=element.intermediate_frequency_negative,
                                frequency_double=element.intermediate_frequency_double,
                                lo_frequency=element_input.lo_frequency,
                                lo_frequency_double=element_input.lo_frequency_double,
                                correction=QuaConfigMatrix(v00=1, v01=0, v10=0, v11=1),
                            )
                        ]
                    )


def validate_inputs_or_outputs_exist(pb_config: QuaConfig) -> None:
    for element in pb_config.v1_beta.elements.values():
        _, element_input = betterproto.which_one_of(element, "element_inputs_one_of")
        _, element_outputs = betterproto.which_one_of(element, "element_outputs_one_of")
        if (
            element_input is None
            and element_outputs is None
            and not bool(element.outputs)  # this is for backward compatibility
            and not bool(element.digital_outputs)
            and not bool(element.digital_inputs)
        ):
            raise NoInputsOrOutputsError


def load_config_pb(config: DictQuaConfig) -> QuaConfig:
    pb_config = QuaConfig(v1_beta=QuaConfigQuaConfigV1())

    def set_controllers() -> None:
        for k, v in config["controllers"].items():
            pb_config.v1_beta.control_devices[k] = controlling_devices_to_pb(v)
        if _all_controllers_are_opx(pb_config.v1_beta.control_devices):
            for _k, _v in pb_config.v1_beta.control_devices.items():
                controller_inst = get_fem_config_instance(_v.fems[OPX_FEM_IDX])
                if not isinstance(controller_inst, QuaConfigControllerDec):
                    raise ValueError("This should not happen")
                pb_config.v1_beta.controllers[_k] = controller_inst

    def set_octaves() -> None:
        for k, v in config.get("octaves", {}).items():
            pb_config.v1_beta.octaves[k] = octave_to_pb(v)

    def set_elements() -> None:
        for k, v in config["elements"].items():
            pb_config.v1_beta.elements[k] = element_to_pb(k, v)

    def set_pulses() -> None:
        for k, v in config["pulses"].items():
            pb_config.v1_beta.pulses[k] = pulse_to_pb(v)

    def set_waveforms() -> None:
        for k, v in config["waveforms"].items():
            if v["type"] == "constant":
                pb_config.v1_beta.waveforms[k] = constant_waveform_to_protobuf(cast(ConstantWaveFormConfigType, v))
            elif v["type"] == "arbitrary":
                pb_config.v1_beta.waveforms[k] = arbitrary_waveform_to_protobuf(cast(ArbitraryWaveFormConfigType, v))
            else:
                raise ValueError("Unknown waveform type")

    def set_digital_waveforms() -> None:
        for k, v in config["digital_waveforms"].items():
            pb_config.v1_beta.digital_waveforms[k] = digital_waveform_to_pb(v)

    def set_integration_weights() -> None:
        for k, v in config["integration_weights"].items():
            pb_config.v1_beta.integration_weights[k] = integration_weights_to_pb(v)

    def set_mixers() -> None:
        for k, v in config["mixers"].items():
            pb_config.v1_beta.mixers[k] = mixer_to_pb(v)

    def set_oscillators() -> None:
        for k, v in config["oscillators"].items():
            pb_config.v1_beta.oscillators[k] = oscillator_to_pb(v)

    key_to_action = {
        "version": lambda: None,
        "controllers": set_controllers,
        "elements": set_elements,
        "pulses": set_pulses,
        "waveforms": set_waveforms,
        "digital_waveforms": set_digital_waveforms,
        "integration_weights": set_integration_weights,
        "mixers": set_mixers,
        "oscillators": set_oscillators,
        "octaves": set_octaves,
    }

    for key in config:
        key_to_action[key]()

    set_octave_upconverter_connection_to_elements(pb_config)
    set_lo_frequency_to_mix_input_elements_that_are_connected_to_octave(pb_config)
    set_octave_downconverter_connection_to_elements(pb_config)
    set_non_existing_mixers_in_mix_input_elements(pb_config)
    return pb_config
