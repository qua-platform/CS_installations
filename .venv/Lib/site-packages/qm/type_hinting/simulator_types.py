from typing import Set, Dict, List, Optional, TypedDict


class PulserLocationType(TypedDict, total=False):
    controllerName: str
    pulserIndex: int
    femId: int


class IqInfoType(TypedDict, total=False):
    isPartOfIq: bool
    iqGroupId: int
    isI: bool
    isQ: bool


class ChirpInfoType(TypedDict, total=False):
    rate: List[int]
    times: List[int]
    units: str
    startFrequency: float
    endFrequency: float


class PlayedWaveformType(TypedDict, total=False):
    waveformName: str
    pulseName: str
    pulser: PulserLocationType
    iqInfo: IqInfoType
    timestamp: int
    length: int
    endsAt: int
    outputPorts: Set[int]
    quantumElements: str


class PlayedAnalogWaveformType(PlayedWaveformType, total=False):
    currentFrame: List[float]
    currentCorrectionElements: List[float]
    currentIntermediateFrequency: float
    currentGMatrixElements: List[float]
    currentDCOffsetByPort: Dict[int, float]
    currentPhase: float
    chirpInfo: ChirpInfoType


class AdcAcquisitionType(TypedDict, total=False):
    startTime: int
    endTime: int
    process: str
    pulser: PulserLocationType
    quantumElement: str
    adc: List[int]


class WaveformReportType(TypedDict, total=False):
    analogWaveforms: List[PlayedAnalogWaveformType]
    digitalWaveforms: List[PlayedWaveformType]
    adcAcquisitions: List[AdcAcquisitionType]


class WaveformPlayingType(TypedDict, total=False):
    name: str
    timestamp: int
    duration: int
    frequency: float
    phase: float


class WaveformInControllerType(TypedDict):
    ports: Dict[int, List[WaveformPlayingType]]


class WaveformInPortsType(TypedDict):
    controllers: Dict[str, WaveformInControllerType]
    elements: Dict[str, WaveformPlayingType]


class AnalogOutputsType(TypedDict):
    waveforms: Optional[WaveformInPortsType]


class DigitalOutputsType(TypedDict):
    waveforms: Optional[WaveformInPortsType]
