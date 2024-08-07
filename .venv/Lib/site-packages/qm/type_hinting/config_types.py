from typing import List, Tuple, Union, Literal, Mapping, TypedDict

from qm.type_hinting.general import Number

StandardPort = Tuple[str, int, int]
PortReferenceType = Union[Tuple[str, int], StandardPort]


# TODO: This is a placeholder while we still use dicts, once we move to pydantics we can simply change the
#  inheritance of the classes handled here and add a more robust validation to the types


class AnalogOutputFilterConfigType(TypedDict, total=False):
    feedforward: List[float]
    feedback: List[float]


class AnalogOutputPortConfigType(TypedDict, total=False):
    offset: Number
    filter: AnalogOutputFilterConfigType
    delay: int
    crosstalk: Mapping[int, Number]
    shareable: bool


class AnalogInputPortConfigType(TypedDict, total=False):
    offset: Number
    gain_db: int
    shareable: bool
    sampling_rate: float


class DigitalOutputPortConfigType(TypedDict, total=False):
    shareable: bool
    inverted: bool
    level: Literal["TTL", "LVTTL"]


class DigitalInputPortConfigType(TypedDict, total=False):
    shareable: bool
    deadtime: int
    polarity: Literal["RISING", "FALLING"]
    threshold: Number


class AnalogOutputPortConfigTypeOctoDac(TypedDict, total=False):
    offset: Number
    filter: AnalogOutputFilterConfigType
    delay: int
    crosstalk: Mapping[int, Number]
    shareable: bool
    connectivity: Tuple[str, str]
    sampling_rate: float
    upsampling_mode: Literal["mw", "pulse"]
    output_mode: Literal["direct", "amplified"]


class LfFemConfigType(TypedDict, total=False):
    type: Literal["LF"]
    analog_outputs: Mapping[int, AnalogOutputPortConfigTypeOctoDac]
    analog_inputs: Mapping[int, AnalogInputPortConfigType]
    digital_outputs: Mapping[int, DigitalOutputPortConfigType]
    digital_inputs: Mapping[int, DigitalInputPortConfigType]


Band = Literal[1, 2, 3]


class MwFemAnalogInputPortConfigType(TypedDict, total=False):
    sampling_rate: float
    gain_db: int
    shareable: bool
    band: Band


class MwFemAnalogOutputPortConfigType(TypedDict, total=False):
    sampling_rate: float
    full_scale_power_dbm: int
    band: Band
    delay: int
    shareable: bool


class MwFemConfigType(TypedDict, total=False):
    type: Literal["MW"]
    analog_outputs: Mapping[int, MwFemAnalogOutputPortConfigType]
    analog_inputs: Mapping[int, MwFemAnalogInputPortConfigType]
    digital_outputs: Mapping[int, DigitalOutputPortConfigType]
    digital_inputs: Mapping[int, DigitalInputPortConfigType]


class ControllerConfigType(TypedDict, total=False):
    type: Literal["opx", "opx1"]
    analog_outputs: Mapping[int, AnalogOutputPortConfigType]
    analog_inputs: Mapping[int, AnalogInputPortConfigType]
    digital_outputs: Mapping[int, DigitalOutputPortConfigType]
    digital_inputs: Mapping[int, DigitalInputPortConfigType]


class OctaveRFOutputConfigType(TypedDict, total=False):
    LO_frequency: float
    LO_source: Literal["internal", "external"]
    output_mode: Literal["always_on", "always_off", "triggered", "triggered_reversed"]
    gain: Union[int, float]
    input_attenuators: Literal["ON", "OFF"]
    I_connection: PortReferenceType
    Q_connection: PortReferenceType


class OctaveRFInputConfigType(TypedDict, total=False):
    RF_source: Literal["RF_in", "loopback_1", "loopback_2", "loopback_3", "loopback_4", "loopback_5"]
    LO_frequency: float
    LO_source: Literal["internal", "external", "analyzer"]
    IF_mode_I: Literal["direct", "mixer", "envelope", "off"]
    IF_mode_Q: Literal["direct", "mixer", "envelope", "off"]


class OctaveSingleIfOutputConfigType(TypedDict, total=False):
    port: PortReferenceType
    name: str


class OctaveIfOutputsConfigType(TypedDict, total=False):
    IF_out1: OctaveSingleIfOutputConfigType
    IF_out2: OctaveSingleIfOutputConfigType


class OPX1000ControllerConfigType(TypedDict, total=False):
    type: Literal["opx1000"]
    fems: Mapping[int, Union[LfFemConfigType, MwFemConfigType]]


LoopbackType = Tuple[
    Tuple[str, Literal["Synth1", "Synth2", "Synth3", "Synth4", "Synth5"]],
    Literal["Dmd1LO", "Dmd2LO", "LO1", "LO2", "LO3", "LO4", "LO5"],
]


class OctaveConfigType(TypedDict, total=False):
    RF_outputs: Mapping[int, OctaveRFOutputConfigType]
    RF_inputs: Mapping[int, OctaveRFInputConfigType]
    IF_outputs: OctaveIfOutputsConfigType
    loopbacks: List[LoopbackType]
    connectivity: Union[str, Tuple[str, int]]


class DigitalInputConfigType(TypedDict, total=False):
    delay: int
    buffer: int
    port: PortReferenceType


class IntegrationWeightConfigType(TypedDict, total=False):
    cosine: Union[List[Tuple[float, int]], List[float]]
    sine: Union[List[Tuple[float, int]], List[float]]


class ConstantWaveFormConfigType(TypedDict, total=False):
    type: Literal["constant"]
    sample: float


class CompressedWaveFormConfigType(TypedDict, total=False):
    type: str
    samples: List[float]
    sample_rate: float


class ArbitraryWaveFormConfigType(TypedDict, total=False):
    type: Literal["arbitrary"]
    samples: List[float]
    max_allowed_error: float
    sampling_rate: Number
    is_overridable: bool


class DigitalWaveformConfigType(TypedDict, total=False):
    samples: List[Tuple[int, int]]


class MixerConfigType(TypedDict, total=False):
    intermediate_frequency: float
    lo_frequency: float
    correction: Tuple[Number, Number, Number, Number]


class PulseConfigType(TypedDict, total=False):
    operation: Literal["measurement", "control"]
    length: int
    waveforms: Mapping[str, str]
    digital_marker: str
    integration_weights: Mapping[str, str]


class SingleInputConfigType(TypedDict, total=False):
    port: PortReferenceType


class MwInputConfigType(TypedDict, total=False):
    port: PortReferenceType
    oscillator_frequency: float


class MwOutputConfigType(TypedDict, total=False):
    port: PortReferenceType
    oscillator_frequency: float


class HoldOffsetConfigType(TypedDict, total=False):
    duration: int


class StickyConfigType(TypedDict, total=False):
    analog: bool
    digital: bool
    duration: int


class MixInputConfigType(TypedDict, total=False):
    I: PortReferenceType
    Q: PortReferenceType
    mixer: str
    lo_frequency: float


class InputCollectionConfigType(TypedDict, total=False):
    inputs: Mapping[str, PortReferenceType]


class OscillatorConfigType(TypedDict, total=False):
    intermediate_frequency: float
    mixer: str
    lo_frequency: float


class OutputPulseParameterConfigType(TypedDict):
    signalThreshold: int
    signalPolarity: Literal["ABOVE", "ASCENDING", "BELOW", "DESCENDING"]
    derivativeThreshold: int
    derivativePolarity: Literal["ABOVE", "ASCENDING", "BELOW", "DESCENDING"]


class ElementConfigType(TypedDict, total=False):
    intermediate_frequency: float
    oscillator: str
    measurement_qe: str
    operations: Mapping[str, str]
    singleInput: SingleInputConfigType
    mixInputs: MixInputConfigType
    singleInputCollection: InputCollectionConfigType
    multipleInputs: InputCollectionConfigType
    MWInput: MwInputConfigType
    MWOutput: MwOutputConfigType
    time_of_flight: int
    smearing: int
    outputs: Mapping[str, PortReferenceType]
    digitalInputs: Mapping[str, DigitalInputConfigType]
    digitalOutputs: Mapping[str, PortReferenceType]
    outputPulseParameters: OutputPulseParameterConfigType
    hold_offset: HoldOffsetConfigType
    sticky: StickyConfigType
    thread: str
    RF_inputs: Mapping[str, Tuple[str, int]]
    RF_outputs: Mapping[str, Tuple[str, int]]


class DictQuaConfig(TypedDict, total=False):
    version: int
    oscillators: Mapping[str, OscillatorConfigType]
    elements: Mapping[str, ElementConfigType]
    controllers: Mapping[str, Union[ControllerConfigType, OPX1000ControllerConfigType]]
    octaves: Mapping[str, OctaveConfigType]
    integration_weights: Mapping[str, IntegrationWeightConfigType]
    waveforms: Mapping[
        str, Union[ArbitraryWaveFormConfigType, ConstantWaveFormConfigType, CompressedWaveFormConfigType]
    ]
    digital_waveforms: Mapping[str, DigitalWaveformConfigType]
    pulses: Mapping[str, PulseConfigType]
    mixers: Mapping[str, List[MixerConfigType]]
