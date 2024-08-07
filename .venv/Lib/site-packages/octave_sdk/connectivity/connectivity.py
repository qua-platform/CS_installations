from dataclasses import dataclass, field
from enum import Enum
from typing import Optional, Dict, Tuple, List, Mapping

import betterproto

from octave_sdk.connectivity.exceptions import (
    InvalidIdentityException,
    LoopbackConfigException,
    ConnectivityException,
    LoSourceValueException,
)
from octave_sdk.grpc.quantummachines.octave.api.v1 import (
    SynthRfOutputOutputPort,
    IdentifyResponse,
    RfDownConvIdentity,
    RfSource,
    RfDownConvUpdateLoInput,
    SynthIdentity,
    ModuleReference,
)

from octave_sdk._octave_client import ExploreResult

from octave_sdk.connectivity.connectivity_util_private import (
    RfSourceType,
    get_rf_source_type,
    validate_rf_source_type,
    get_rf_source_name,
    get_rf_source_from_synth_panel_output,
)
from octave_sdk.connectivity.connectivity_filter import FilteredWorkingModules
from octave_sdk.connectivity.connectivity_util import RFInputRFSource

AnalyzerIndex = 6


class OctaveLOSource(Enum):
    """input to the octave, uses it for output"""

    Off = -1
    Internal = 0
    Dmd1LO = 1
    Dmd2LO = 2
    LO1 = 11
    LO2 = 12
    LO3 = 13
    LO4 = 14
    LO5 = 15
    RF_IN1 = 21
    RF_IN2 = 22
    IF1_LO_I = 23
    IF1_LO_Q = 24
    IF2_LO_I = 25
    IF2_LO_Q = 26


class OctaveOutput(Enum):
    """
    The output ports of the octave,
    each port group indexes has a different prefix:
    synth: 0X
    RF: 1X
    IF_OUT: 2X
    Dig: 3X
    """

    Synth1 = 1
    Synth2 = 2
    Synth3 = 3
    Synth4 = 4
    Synth5 = 5
    RF1 = 11
    RF2 = 12
    RF3 = 13
    RF4 = 14
    RF5 = 15
    IF_OUT1 = 21
    IF_OUT2 = 22
    Dig1 = 31
    Dig2 = 32
    Dig3 = 33


class RFInputLOSource(Enum):
    """
    input to octave, uses it for downconversion, the lo
    extending the OctaveLOSourceInput
    """

    Off = 1
    Internal = 2
    Dmd1LO = 3
    Dmd2LO = 4
    LO1 = 5
    LO2 = 6
    LO3 = 7
    LO4 = 8
    LO5 = 9
    Analyzer = 12
    RFOutput1_LO = 13
    RFOutput2_LO = 14
    RFOutput3_LO = 15
    RFOutput4_LO = 16
    RFOutput5_LO = 17


class _SynthLOInput(Enum):
    Main = 1
    Secondary = 2


def _convert_synth_lo_source_proto_name_to_rf_port_name(name: str, index: int) -> OctaveLOSource:
    if name == "demod_lo_input_index":
        return OctaveLOSource(index)
    elif name == "lo_input_index":
        return OctaveLOSource(index + 10)
    else:
        raise ConnectivityException(f"name {name} and index {index} are unknown input name")


class UpOrDownId(Enum):
    UpConv = "RFout"
    DownConv = "RFin"


@dataclass
class SynthOutputDeviceInfo:
    index: int
    up_or_down: UpOrDownId


@dataclass
class _ModuleInfo:
    synth_index: int
    synth_output_port: SynthRfOutputOutputPort
    synth_lo_input: Optional[_SynthLOInput] = None


@dataclass
class _LoopbackLoInfo:
    loopback_source: "_LoSourceInfo"
    loopback_input_port: OctaveLOSource
    loopback_output_port: OctaveOutput


@dataclass
class _LoSourceInfo:
    name: OctaveLOSource
    module_info: _ModuleInfo
    loopback_info: Optional[_LoopbackLoInfo] = None


@dataclass
class SynthPanelMapping:
    panel_port: OctaveOutput
    port_type: SynthRfOutputOutputPort


@dataclass
class SynthInputMapping:
    port_type: SynthRfOutputOutputPort
    rf_sources: Dict[OctaveLOSource, _LoSourceInfo] = field(default_factory=dict)
    output_up_down_conv: SynthOutputDeviceInfo = None


@dataclass
class SynthMapping:
    index: int = None
    synth_output_panel: Dict[OctaveOutput, SynthPanelMapping] = field(default_factory=dict)
    synth_input: Dict[SynthRfOutputOutputPort, SynthInputMapping] = field(default_factory=dict)


def convert_rf_in_enum_to_octave_lo_input(
    name: RFInputLOSource,
    synth_by_rf_out: Dict[int, int],
    synth_by_lo_source: Dict[OctaveLOSource, int],
) -> Mapping[OctaveLOSource, int]:
    if name == RFInputLOSource.Dmd1LO:
        return OctaveLOSource.Dmd1LO, synth_by_lo_source[OctaveLOSource.Dmd1LO]
    elif name == RFInputLOSource.Dmd2LO:
        return OctaveLOSource.Dmd2LO, synth_by_lo_source[OctaveLOSource.Dmd2LO]
    elif name == RFInputLOSource.LO1:
        return OctaveLOSource.LO1, synth_by_lo_source[OctaveLOSource.LO1]
    elif name == RFInputLOSource.LO2:
        return OctaveLOSource.LO2, synth_by_lo_source[OctaveLOSource.LO2]
    elif name == RFInputLOSource.LO3:
        return OctaveLOSource.LO3, synth_by_lo_source[OctaveLOSource.LO3]
    elif name == RFInputLOSource.LO4:
        return OctaveLOSource.LO4, synth_by_lo_source[OctaveLOSource.LO4]
    elif name == RFInputLOSource.LO5:
        return OctaveLOSource.LO5, synth_by_lo_source[OctaveLOSource.LO5]
    elif name == RFInputLOSource.RFOutput1_LO:
        return OctaveLOSource.Internal, synth_by_rf_out[1]
    elif name == RFInputLOSource.RFOutput2_LO:
        return OctaveLOSource.Internal, synth_by_rf_out[2]
    elif name == RFInputLOSource.RFOutput3_LO:
        return OctaveLOSource.Internal, synth_by_rf_out[3]
    elif name == RFInputLOSource.RFOutput4_LO:
        return OctaveLOSource.Internal, synth_by_rf_out[4]
    elif name == RFInputLOSource.RFOutput5_LO:
        return OctaveLOSource.Internal, synth_by_rf_out[5]
    elif name == RFInputLOSource.Off:
        return OctaveLOSource.Off, -1
    elif name == RFInputLOSource.Internal:
        return OctaveLOSource.Internal, -1
    elif name == RFInputLOSource.Analyzer:
        return OctaveLOSource.Internal, 4
    else:
        # RFInputLOSource.RF_IN1 and RFInputLOSource.RF_IN2 are not supported
        raise ValueError(f"RF input lo source {name} is unknown")


def convert_rf_in_lo_by_rf_out(name: RFInputLOSource, synth_index, rf_out_by_synth) -> RFInputLOSource:
    if rf_out_by_synth and synth_index not in rf_out_by_synth:
        return name
    elif name == RFInputLOSource.Internal and rf_out_by_synth and 1 in rf_out_by_synth[synth_index]:
        return RFInputLOSource.RFOutput1_LO
    elif name == RFInputLOSource.Internal and rf_out_by_synth and 2 in rf_out_by_synth[synth_index]:
        return RFInputLOSource.RFOutput2_LO
    elif name == RFInputLOSource.Internal and rf_out_by_synth and 3 in rf_out_by_synth[synth_index]:
        return RFInputLOSource.RFOutput3_LO
    elif name == RFInputLOSource.Internal and rf_out_by_synth and 4 in rf_out_by_synth[synth_index]:
        return RFInputLOSource.RFOutput4_LO
    elif name == RFInputLOSource.Internal and rf_out_by_synth and 5 in rf_out_by_synth[synth_index]:
        return RFInputLOSource.RFOutput5_LO
    else:
        return name


def convert_octave_lo_input_enum_to_rf_in(name: OctaveLOSource, synth_index) -> RFInputLOSource:
    if name == OctaveLOSource.Dmd1LO:
        return RFInputLOSource.Dmd1LO
    elif name == OctaveLOSource.Dmd2LO:
        return RFInputLOSource.Dmd2LO
    elif name == OctaveLOSource.LO1:
        return RFInputLOSource.LO1
    elif name == OctaveLOSource.LO2:
        return RFInputLOSource.LO2
    elif name == OctaveLOSource.LO3:
        return RFInputLOSource.LO3
    elif name == OctaveLOSource.LO4:
        return RFInputLOSource.LO4
    elif name == OctaveLOSource.LO5:
        return RFInputLOSource.LO5
    elif name == OctaveLOSource.Internal and synth_index == 4:
        return RFInputLOSource.Analyzer
    elif name == OctaveLOSource.Internal:
        return RFInputLOSource.Internal
    elif name == OctaveLOSource.Off:
        return RFInputLOSource.Off
    else:
        raise ValueError(f"RF input lo source {name} is unknown")


def _find_by_index(proto_list, index, error_message):
    result = [u for u in proto_list if u.index == index]

    if len(result) != 1:
        raise ValueError(error_message)

    return result[0]


class ModulesSlotsFromIdentity:
    def __init__(self, identity_response: IdentifyResponse):
        # Index from identity actually means slot and starts from 1, while monitor index start from 0
        self.rf_out_list: List[int] = [uc.index for uc in identity_response.rf_up_converters]
        self.rf_in_list: List[int] = [uc.index for uc in identity_response.rf_down_converters]
        self.if_list: List[int] = [uc.index for uc in identity_response.if_down_converters]
        self.synth_list: List[int] = [uc.index for uc in identity_response.synthesizers]


class Connectivity:
    def __init__(
        self,
        identity_response: IdentifyResponse,
        loopbacks: Dict[OctaveLOSource, OctaveOutput],
        explore_result: ExploreResult,
    ) -> None:

        if loopbacks is not None:
            self.loopbacks: Dict[OctaveLOSource, OctaveOutput] = loopbacks
        else:
            self.loopbacks = dict()

        if identity_response is None:
            raise InvalidIdentityException("Connectivity must get an identity response")

        self._identity_response_original = identity_response

        filter_object = FilteredWorkingModules(self._identity_response_original, explore_result)
        self._identity_response: IdentifyResponse = filter_object.identity_response_filtered
        self.missing_modules: list(ModuleReference) = filter_object.missing_modules

        # Identity message parse:
        self._synth_by_rf_out: Dict[int, (int, SynthRfOutputOutputPort)] = {
            uc.index: self._get_synth_by_rf_out(uc.index) for uc in self._identity_response.rf_up_converters
        }
        self._synth_by_rf_in: Dict[
            (int, RfDownConvUpdateLoInput), (int, SynthRfOutputOutputPort)
        ] = self._get_synths_by_rf_in()

        self._rf_outs = [uc.index for uc in self._identity_response.rf_up_converters]
        self._rf_ins = [uc.index for uc in self._identity_response.rf_down_converters]
        self._synths = [uc.index for uc in self._identity_response.synthesizers]
        self._if_down_by_rf_down = {
            item.connectivity.channel_1_input.rf_downconv_if_source.index: item.index
            for item in self._identity_response.if_down_converters
            if not item.connectivity.channel_1_input.constant_source
        }

        # from previous values:
        self._synth_connectivity: Dict[int, SynthMapping] = {}
        self._fill_synths_mapping()

        self._rf_out_by_synth: Dict[int, List[int]] = {}
        for rf_out_rf_port, synth_index_and_output_port in self._synth_by_rf_out.items():
            synth_index = synth_index_and_output_port[0]
            if synth_index not in self._rf_out_by_synth:
                self._rf_out_by_synth[synth_index] = []
            self._rf_out_by_synth[synth_index].append(rf_out_rf_port)

        self._rf_in_by_synth: Dict[int, int] = {item[1][0]: item[0][0] for item in self._synth_by_rf_in.items()}

        self._synth_by_lo_source: Dict[OctaveLOSource, int] = {
            source_info.name: synth.index
            for synth in self._synth_connectivity.values()
            for input_mapping in synth.synth_input.values()
            for source_info in input_mapping.rf_sources.values()
        }

    # region inner functions

    def _fill_synth_panel_mapping(self):
        for synth_output in self._identity_response.panel_identity.synth_outputs:
            output = get_rf_source_from_synth_panel_output(synth_output.source)
            self._synth_connectivity[output.index].synth_output_panel[
                OctaveOutput(synth_output.index)
            ] = SynthPanelMapping(
                panel_port=OctaveOutput(synth_output.index),
                port_type=output.output_port,
            )

    def _fill_synths_mapping(self):
        for synth in self._identity_response.synthesizers:
            self._synth_connectivity[synth.index] = SynthMapping(index=synth.index)
            self._fill_synth_lo_sources(synth)

        self._fill_synth_panel_mapping()
        self._fill_synth_output_up_down()
        # self._fill_final_synth_output()

    def _fill_synth_output_up_down(self):
        for rf_out in self._rf_outs:
            synth_index, output_port = self._synth_by_rf_out[rf_out]
            if synth_index is not None:
                self._synth_connectivity[synth_index].synth_input[
                    output_port
                ].output_up_down_conv = SynthOutputDeviceInfo(index=rf_out, up_or_down=UpOrDownId.UpConv)

        for rf_in in self._rf_ins:
            synth_index, output_port = self._synth_by_rf_in[(rf_in, RfDownConvUpdateLoInput.LO_INPUT_1)]
            if synth_index is not None:
                self._synth_connectivity[synth_index].synth_input[
                    output_port
                ].output_up_down_conv = SynthOutputDeviceInfo(index=rf_in, up_or_down=UpOrDownId.DownConv)
            synth_index, output_port = self._synth_by_rf_in[(rf_in, RfDownConvUpdateLoInput.LO_INPUT_2)]
            if synth_index is not None:
                self._synth_connectivity[synth_index].synth_input[
                    output_port
                ].output_up_down_conv = SynthOutputDeviceInfo(index=rf_in, up_or_down=UpOrDownId.DownConv)

    def _fill_synth_lo_sources(self, synth: SynthIdentity):
        for port_type in (
            SynthRfOutputOutputPort.OUTPUT_PORT_MAIN,
            SynthRfOutputOutputPort.OUTPUT_PORT_SECONDARY,
            SynthRfOutputOutputPort.OUTPUT_PORT_SYNTH,
        ):
            sources = self._get_synth_local_lo_sources(synth, port_type)
            self._synth_connectivity[synth.index].synth_input[port_type] = sources

    def _get_synths_by_rf_out(self) -> Dict[int, Tuple[int, SynthRfOutputOutputPort]]:
        result = {}
        for rf_out in self._identity_response.rf_up_converters:
            result[rf_out.index] = self._get_synth_by_rf_out(rf_out.index)
        return result

    def _get_synths_by_rf_in(
        self,
    ) -> Dict[Tuple[int, RfDownConvUpdateLoInput], Tuple[int, SynthRfOutputOutputPort]]:
        result = {}
        for rf_in in self._identity_response.rf_down_converters:
            result[rf_in.index, RfDownConvUpdateLoInput.LO_INPUT_1] = self._get_synth_by_rf_in(
                rf_in.index, RfDownConvUpdateLoInput.LO_INPUT_1
            )

            result[rf_in.index, RfDownConvUpdateLoInput.LO_INPUT_2] = self._get_synth_by_rf_in(
                rf_in.index, RfDownConvUpdateLoInput.LO_INPUT_2
            )
        return result

    def _get_synth_by_rf_out(
        self,
        rf_out_index: int,
    ) -> Mapping[int, SynthRfOutputOutputPort]:
        rf_output = _find_by_index(
            self._identity_response.rf_up_converters,
            rf_out_index,
            f"RF output with index {rf_out_index} was not found",
        )

        lo_input = rf_output.connectivity.lo_input
        source_type = get_rf_source_type(lo_input)
        if source_type == RfSourceType.synth_output:
            synth_port = lo_input.synth_output
            synth_output_port_type = synth_port.output_port
            synth_index = synth_port.index
        elif source_type == RfSourceType.constant_source:
            return None, SynthRfOutputOutputPort.OUTPUT_PORT_UNSPECIFIED
        else:
            raise LoSourceValueException(f"LO source 1 of RF output {rf_out_index} is unknown")

        return synth_index, synth_output_port_type

    def _get_synth_by_rf_in(
        self, rf_in_index: int, input_port: RfDownConvUpdateLoInput
    ) -> Mapping[int, SynthRfOutputOutputPort]:

        rf_input: RfDownConvIdentity = _find_by_index(
            self._identity_response.rf_down_converters,
            rf_in_index,
            f"RF input with index {rf_in_index} was not found",
        )

        if input_port == RfDownConvUpdateLoInput.LO_INPUT_1:
            lo_input = rf_input.connectivity.lo_input_1
        else:
            lo_input = rf_input.connectivity.lo_input_2

        source_type = get_rf_source_type(lo_input)
        if source_type == RfSourceType.synth_output:
            synth_port = lo_input.synth_output
            synth_output_port_type = synth_port.output_port
            synth_index = synth_port.index
        elif source_type == RfSourceType.constant_source:
            return None, SynthRfOutputOutputPort.OUTPUT_PORT_UNSPECIFIED
        else:
            raise LoSourceValueException(f"LO source 1 of RF output {rf_in_index} is unknown")

        return synth_index, synth_output_port_type

    def _get_synth_local_lo_sources(
        self,
        synth: SynthIdentity,
        synth_output_port_type: SynthRfOutputOutputPort,
    ) -> SynthInputMapping:
        # synth output can always get off and internal
        synth_input_mapping = SynthInputMapping(synth_output_port_type)
        synth_input_mapping.rf_sources = {
            OctaveLOSource.Off: _LoSourceInfo(OctaveLOSource.Off, _ModuleInfo(synth.index, synth_output_port_type)),
            OctaveLOSource.Internal: _LoSourceInfo(
                OctaveLOSource.Internal,
                _ModuleInfo(synth.index, synth_output_port_type),
            ),
        }

        # get extra external sources of the synth
        main_port_name, secondary_port_name = self._get_synth_lo_inputs(synth)
        if main_port_name and synth_output_port_type in (
            SynthRfOutputOutputPort.OUTPUT_PORT_MAIN,
            SynthRfOutputOutputPort.OUTPUT_PORT_SECONDARY,
        ):
            source_info = _LoSourceInfo(
                main_port_name,
                _ModuleInfo(
                    synth.index,
                    synth_output_port_type,
                    synth_lo_input=_SynthLOInput.Main,
                ),
            )
            synth_input_mapping.rf_sources[main_port_name] = source_info

        if secondary_port_name and synth_output_port_type == SynthRfOutputOutputPort.OUTPUT_PORT_SECONDARY:
            # secondary output can also get from the secondary input
            source_info = _LoSourceInfo(
                secondary_port_name,
                _ModuleInfo(
                    synth.index,
                    synth_output_port_type,
                    synth_lo_input=_SynthLOInput.Secondary,
                ),
            )
            synth_input_mapping.rf_sources[secondary_port_name] = source_info

        return synth_input_mapping

    def _get_synth_lo_inputs(self, synth: SynthIdentity) -> Mapping[OctaveLOSource, OctaveLOSource]:
        synth_connectivity = synth.connectivity

        rf_port_name = self._get_rf_port_name(
            synth_connectivity.main_lo_input,
            f"Main LO source of synth {synth.index} is unknown",
        )
        try:
            rf_second_port_name = self._get_rf_port_name(
                synth_connectivity.secondary_lo_input,
                f"Secondary LO source of synth {synth.index} is unknown",
            )
        except InvalidIdentityException:
            rf_second_port_name = None

        return rf_port_name, rf_second_port_name

    @staticmethod
    def _get_rf_port_name(lo_input: RfSource, message: str = None):
        validate_rf_source_type(lo_input, "external_input", message)
        one_of, value = betterproto.which_one_of(lo_input.external_input, "input")
        if value and one_of:
            rf_port_name = _convert_synth_lo_source_proto_name_to_rf_port_name(one_of, value)
        else:
            rf_port_name = None
        return rf_port_name

    def _get_external_lo_sources(
        self,
        name: OctaveLOSource,
    ) -> Optional[SynthMapping]:
        if name in self.loopbacks:
            octave_output_port = self.loopbacks[name]

            # handles only synth outputs
            synth = self._get_synth_from_output_port(octave_output_port)

            return synth
        return None

    def _get_synth_from_output_port(self, octave_output: OctaveOutput) -> SynthMapping:
        try:
            for synth in self._synth_connectivity.values():
                if octave_output in synth.synth_output_panel:
                    return synth
        except KeyError:
            raise LoopbackConfigException(f"Octave output {octave_output.name} is not supported with loopback")

    # endregion

    # region API
    def get_synth_index_from_output_port(self, octave_output: OctaveOutput) -> int:
        return self._get_synth_from_output_port(octave_output).index

    def rf_outputs_indices(self):
        return self._rf_outs

    def rf_inputs_indices(self):
        return self._rf_ins

    def synth_indices(self):
        return self._synths

    def get_lo_source_of_rf_output(self, index: int) -> Dict[Tuple[OctaveLOSource, int], _LoSourceInfo]:
        """returns dictionary from rf_output input name to rf source"""
        synth_index, port_type = self._synth_by_rf_out[index]

        result = {}
        if synth_index is not None:
            synth = self._synth_connectivity[synth_index]
            input_mapping = synth.synth_input[port_type]
            for port_name, source in input_mapping.rf_sources.items():
                result[(port_name, source.module_info.synth_index)] = source
        return result

    def get_lo_source_of_rf_input_first(self, index: int) -> Dict[Tuple[OctaveLOSource, int], _LoSourceInfo]:
        """returns dictionary from rf_output input name to rf source"""
        synth_output_to_1 = self._synth_by_rf_in[index, RfDownConvUpdateLoInput.LO_INPUT_1]

        return self.get_lo_source_by_synth_output(*synth_output_to_1)

    def get_lo_source_of_rf_input_second(self, index: int) -> Dict[Tuple[OctaveLOSource, int], _LoSourceInfo]:
        """returns dictionary from rf_output input name to rf source"""
        synth_output_to_input2 = self._synth_by_rf_in[index, RfDownConvUpdateLoInput.LO_INPUT_2]

        return self.get_lo_source_by_synth_output(*synth_output_to_input2)

    def get_lo_source_by_synth_output(self, synth_index: int, output: SynthRfOutputOutputPort):
        result = {}
        try:
            synth = self._synth_connectivity[synth_index]
        except KeyError:
            return result
        sources = synth.synth_input[output]
        for port_name, source in sources.rf_sources.items():
            result[(port_name, source.module_info.synth_index)] = source
        return result

    def get_iq_channels_for_rf_output(self, index):
        return index

    def get_rf_source_of_rf_input(self, index) -> List[RFInputRFSource]:
        rf_input: RfDownConvIdentity = _find_by_index(
            self._identity_response.rf_down_converters,
            index,
            f"RF input with index {index} was not found",
        )
        sources = []
        if betterproto.serialized_on_wire(rf_input.connectivity.rf_main_input):
            sources.append(get_rf_source_name(rf_input.connectivity.rf_main_input))
        if betterproto.serialized_on_wire(rf_input.connectivity.debug_rf_input_1):
            sources.append(get_rf_source_name(rf_input.connectivity.debug_rf_input_1))
        if betterproto.serialized_on_wire(rf_input.connectivity.debug_rf_input_2):
            sources.append(get_rf_source_name(rf_input.connectivity.debug_rf_input_2))
        if betterproto.serialized_on_wire(rf_input.connectivity.debug_rf_input_3):
            sources.append(get_rf_source_name(rf_input.connectivity.debug_rf_input_3))
        if betterproto.serialized_on_wire(rf_input.connectivity.debug_rf_input_4):
            sources.append(get_rf_source_name(rf_input.connectivity.debug_rf_input_4))
        if betterproto.serialized_on_wire(rf_input.connectivity.debug_rf_input_5):
            sources.append(get_rf_source_name(rf_input.connectivity.debug_rf_input_5))

        sources.append(RFInputRFSource.Off)

        return sources

    def get_rf_up_down_by_synth_output(self, index, output_port) -> SynthOutputDeviceInfo:
        return self._synth_connectivity[index].synth_input[output_port].output_up_down_conv

    def get_synth_index_of_rf_in_lo(
        self, index: int, lo_source_index: RfDownConvUpdateLoInput
    ) -> Mapping[int, SynthRfOutputOutputPort]:
        return self._synth_by_rf_in.get((index, lo_source_index), (None, None))

    def get_synth_index_of_rf_out_lo(self, index) -> Mapping[int, SynthRfOutputOutputPort]:
        return self._synth_by_rf_out[index]

    def rf_out_by_synth(self) -> Dict[int, List[int]]:
        return self._rf_out_by_synth

    def synth_by_rf_out(self) -> Dict[int, int]:
        return {item[0]: item[1][0] for item in self._synth_by_rf_out.items()}

    def synth_by_rf_in(self) -> Dict[Tuple[int, RfDownConvUpdateLoInput], int]:
        return {item[0]: item[1][0] for item in self._synth_by_rf_in.items()}

    def synth_by_lo_source(self):
        return self._synth_by_lo_source

    def get_if_by_down_conv(self, rf_down):
        return self._if_down_by_rf_down[rf_down] if rf_down in self._if_down_by_rf_down else -1

    # endregion
