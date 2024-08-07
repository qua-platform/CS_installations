import dataclasses
import json
import bisect
import logging
from threading import Lock
from enum import Enum, auto
from typing import Optional, Dict, Tuple, List, Mapping


from octave_sdk.batch import BatchSingleton
from octave_sdk._client_request_builder import ClientRequestBuilder
from octave_sdk.connectivity.connectivity import (
    RFInputRFSource,
    OctaveLOSource,
    RFInputLOSource,
    _LoSourceInfo,
    Connectivity,
    convert_rf_in_enum_to_octave_lo_input,
    OctaveOutput,
    _SynthLOInput,
    convert_octave_lo_input_enum_to_rf_in,
    AnalyzerIndex,
    convert_rf_in_lo_by_rf_out,
    SynthOutputDeviceInfo,
    UpOrDownId,
    ModulesSlotsFromIdentity,
)
from octave_sdk.connectivity.connectivity_util import (
    octave_module_to_module_name_mapping,
    slot_index_to_panel_mapping,
)
from octave_sdk._default_identity import default_identify_response
from octave_sdk._errors import InvalidLoSource
from octave_sdk.grpc.quantummachines.octave.api.v1 import (
    IdentifyResponse,
    SynthRfOutputOutputPort,
    RfDownConvUpdateLoInput,
    SynthUpdateMainSource,
    SynthUpdateMainOutput,
    SynthUpdateSecondaryOutput,
    RfDownConvUpdateRfInput,
    RfUpConvUpdateIfInputSelection,
    RfUpConvUpdateFastSwitchMode,
    SynthUpdateSynthOutput,
    ClockUpdate,
    ClockUpdateMode,
    SynthUpdate,
    SynthUpdateReferenceClock,
    SynthUpdateReferenceSource,
    GetVersionResponse,
    RfUpConvUpdate,
    RfDownConvUpdate,
    OctaveModule,
    SingleUpdate,
    MotherboardUpdate,
    IfDownConvUpdateMode,
    IfDownConvUpdateCoupling,
    IfDownConvUpdate,
    ModuleReference,
    SynthUpdateSynthOutputPower,
)
from octave_sdk._octave_client import OctaveClient
from octave_sdk.conflict_manager import SynthConflicts
from octave_sdk.health_monitor import HealthMonitor
from octave_sdk.octave_module_com import _get_synth_state

DEFAULT_STATE = "default"

logger = logging.getLogger("qm")


class ClockType(Enum):
    """ """

    Internal = auto()
    External = auto()
    Buffered = auto()  # for opt


class ClockFrequency(Enum):
    """ """

    MHZ_10 = auto()
    MHZ_100 = auto()
    MHZ_1000 = auto()


DEFAULT_CLOCK_FREQ = ClockFrequency.MHZ_1000


@dataclasses.dataclass(frozen=True)
class RFOutputLoSourceOption:
    label: OctaveLOSource


@dataclasses.dataclass(frozen=True)
class RFInputLoSourceOption:
    label: RFInputLOSource


class IFMode(Enum):
    """ """

    direct = 1
    envelope = 2
    mixer = 3
    off = 4


class RFOutputMode(Enum):
    """ """

    trig_normal = 1
    trig_inverse = 2
    on = 3
    off = 4
    debug = 5


@dataclasses.dataclass
class ClockInfo:
    clock_type: ClockType
    frequency: Optional[ClockFrequency]


class _OctaveContext:
    def __init__(self, client: OctaveClient, connectivity: Connectivity) -> None:
        super().__init__()
        self.client: OctaveClient = client
        self.connectivity: Connectivity = connectivity


def _turn_off_synth_output(crb, synth_index, synth_output, rf_in_index):
    if synth_output == SynthRfOutputOutputPort.OUTPUT_PORT_MAIN:
        crb.synth[synth_index].main_output = SynthUpdateMainOutput.MAIN_OUTPUT_OFF
    elif synth_output == SynthRfOutputOutputPort.OUTPUT_PORT_SECONDARY:
        crb.synth[synth_index].secondary_output = SynthUpdateSecondaryOutput.SECONDARY_OUTPUT_OFF
    elif synth_output == SynthRfOutputOutputPort.OUTPUT_PORT_SYNTH:
        pass
    else:
        raise Exception(f"could not turn off lo source of rf input {rf_in_index}")


def _set_synth_internal_mode(crb, synth_index, synth_output):
    crb.synth[synth_index].main_source = SynthUpdateMainSource.MAIN_SOURCE_SYNTHESIZER
    crb.synth[synth_index].digital_attn = 63
    crb.synth[synth_index].gain = 0xFFFF
    crb.synth[synth_index].synth_output_power = SynthUpdateSynthOutputPower.SYNTH_OUTPUT_POWER_POS5DB
    if synth_output == SynthRfOutputOutputPort.OUTPUT_PORT_MAIN:
        crb.synth[synth_index].main_output = SynthUpdateMainOutput.MAIN_OUTPUT_MAIN
    elif synth_output == SynthRfOutputOutputPort.OUTPUT_PORT_SECONDARY:
        crb.synth[synth_index].secondary_output = SynthUpdateSecondaryOutput.SECONDARY_OUTPUT_MAIN
    elif synth_output == SynthRfOutputOutputPort.OUTPUT_PORT_SYNTH:
        # no need to change any switches
        pass
    else:
        raise Exception("synth output is unknown")


def _set_synth_external_mode(crb, synth_index, synth_output, synth_lo_input):
    synth = crb.synth[synth_index]
    if synth_output == SynthRfOutputOutputPort.OUTPUT_PORT_MAIN:
        if synth_lo_input == _SynthLOInput.Main:
            synth.main_source = SynthUpdateMainSource.MAIN_SOURCE_EXTERNAL
            synth.main_output = SynthUpdateMainOutput.MAIN_OUTPUT_MAIN
        else:
            raise Exception("can not connect input to output")

    elif synth_output == SynthRfOutputOutputPort.OUTPUT_PORT_SECONDARY:
        if synth_lo_input == _SynthLOInput.Main:
            synth.main_source = SynthUpdateMainSource.MAIN_SOURCE_EXTERNAL
            synth.secondary_output = SynthUpdateMainOutput.MAIN_OUTPUT_MAIN
            synth.secondary_output = SynthUpdateMainOutput.MAIN_OUTPUT_MAIN
        elif synth_lo_input == _SynthLOInput.Secondary:
            synth.secondary_output = SynthUpdateSecondaryOutput.SECONDARY_OUTPUT_AUXILARY
        else:
            raise Exception("synth input is unknown")

    else:
        raise Exception("synth output is unknown")


def _set_if_mode(client, index, mode, channel_id):
    crb = ClientRequestBuilder()
    if channel_id == 1:
        channel = crb.ifconv[index].channel1
    else:
        channel = crb.ifconv[index].channel2

    channel.coupling = IfDownConvUpdateCoupling.COUPLING_DC
    if mode == IFMode.direct:
        channel.mode = IfDownConvUpdateMode.MODE_BYPASS
    elif mode == IFMode.envelope:
        channel.mode = IfDownConvUpdateMode.MODE_POWER_DETECT
    elif mode == IFMode.mixer:
        channel.mode = IfDownConvUpdateMode.MODE_MIXER
    elif mode == IFMode.off:
        channel.mode = IfDownConvUpdateMode.MODE_OFF
    else:
        raise ValueError(f"IF Mode {mode} is not supported. only `IFMode` enum values" f" are supported")
    client.update(crb.get_updates())


def _get_if_mode(client, index, channel):
    response: SingleUpdate = client.aquire_modules(
        [ModuleReference(type=OctaveModule.OCTAVE_MODULE_IF_DOWNCONVERTER, index=index)]
    )
    res: IfDownConvUpdate = response.if_down_conv

    if channel == 1:
        mode = res.channel1.mode
    else:
        mode = res.channel2.mode

    if mode == IfDownConvUpdateMode.MODE_BYPASS:
        return IFMode.direct
    elif mode == IfDownConvUpdateMode.MODE_POWER_DETECT:
        return IFMode.envelope
    elif mode == IfDownConvUpdateMode.MODE_MIXER:
        return IFMode.mixer
    elif mode == IfDownConvUpdateMode.MODE_OFF:
        return IFMode.off
    else:
        raise Exception("can not get if mode")


def _interp_linear(x: float, xp: List[float], fp: List[float]) -> float:
    if not xp[0] <= x <= xp[-1]:
        raise ValueError("x is out of range")
    if x == xp[-1]:
        return fp[-1]

    right_index = bisect.bisect(xp, x)
    left_index = right_index - 1

    x_left = xp[left_index]
    x_right = xp[right_index]
    dx = x_right - x_left

    y_left = fp[left_index]
    y_right = fp[right_index]

    if dx == 0:
        return y_left

    fraction = (x - x_left) / dx
    return y_left + (y_right - y_left) * fraction


def _interp_freq_to_attenuation(freq: float, attn_map: Dict[float, float]) -> float:
    return _interp_linear(freq / 1e9, list(attn_map.keys()), list(attn_map.values()))


def _round_to_int(x: float) -> int:
    return int(x + 0.5)


def _interp_freq_to_int_attenuation(freq: float, attn_map: Dict[float, float]) -> int:
    return _round_to_int(_interp_freq_to_attenuation(freq, attn_map))


def _get_synth_attenuation(lo_freq: float) -> int:
    if lo_freq >= 16e9:
        attn_table = {
            16.0: 0,
            16.2: 0,
            16.4: 0,
            16.6: 0,
            16.8: 4,
            17.0: 4,
            17.2: 4,
            17.4: 4,
            17.6: 4,
            17.8: 8,
            18.0: 8,
            18.4: 8,
        }
        if 18e9 < lo_freq <= 18.4e9:
            logger.warning("LO frequency is above 18 GHz, this frequency is supported but performance is degraded.")
    else:
        if 1.6e9 <= lo_freq < 2e9:
            logger.warning("LO frequency is below 2 GHz, this frequency is supported but performance is degraded.")
        attn_table = {
            1.6: 32,
            1.8: 32,
            2.0: 32,
            2.2: 52,
            2.4: 52,
            2.6: 48,
            2.8: 48,
            3.0: 48,
            3.2: 48,
            3.4: 40,
            3.6: 32,
            3.8: 28,
            4.0: 24,
            4.2: 20,
            4.4: 20,
            4.6: 20,
            4.8: 16,
            5.0: 12,
            5.2: 12,
            5.4: 16,
            5.6: 16,
            5.8: 16,
            6.0: 16,
            6.2: 20,
            6.4: 20,
            6.6: 20,
            6.8: 20,
            7.0: 20,
            7.2: 20,
            7.4: 16,
            7.6: 12,
            7.8: 12,
            8.0: 16,
            8.2: 16,
            8.4: 16,
            8.6: 20,
            8.8: 20,
            9.0: 20,
            9.2: 16,
            9.4: 16,
            9.6: 16,
            9.8: 16,
            10.0: 12,
            10.2: 12,
            10.4: 12,
            10.6: 12,
            10.8: 8,
            11.0: 8,
            11.2: 8,
            11.4: 8,
            11.6: 8,
            11.8: 8,
            12.0: 8,
            12.2: 12,
            12.4: 16,
            12.6: 16,
            12.8: 16,
            13.0: 16,
            13.2: 16,
            13.4: 20,
            13.6: 24,
            13.8: 24,
            14.0: 24,
            14.2: 24,
            14.4: 24,
            14.6: 20,
            14.8: 20,
            15.0: 20,
            15.2: 20,
            15.4: 20,
            15.6: 20,
            15.8: 24,
            16.0: 24,
        }

    return _interp_freq_to_int_attenuation(lo_freq, attn_table)


class UnableToSetFrequencyError(ValueError):
    pass


class RFInput:
    """ """

    def __init__(
        self,
        context: _OctaveContext,
        index: int,
    ) -> None:
        super().__init__()
        self._context = context
        self._index = index
        self._possible_lo_sources_first: Dict[
            Tuple[OctaveLOSource, int], _LoSourceInfo
        ] = context.connectivity.get_lo_source_of_rf_input_first(index)
        self._possible_lo_sources_second: Dict[
            Tuple[OctaveLOSource, int], _LoSourceInfo
        ] = context.connectivity.get_lo_source_of_rf_input_second(index)
        self._possible_lo_sources_names = set(
            [s[0] for s in self._possible_lo_sources_first] + [s[0] for s in self._possible_lo_sources_second]
        )
        self._possible_rf_sources = context.connectivity.get_rf_source_of_rf_input(index)

        self._if_index = self._context.connectivity.get_if_by_down_conv(self._index)

    def _get_current_state(self):
        response = self._context.client.aquire_modules(
            [ModuleReference(type=OctaveModule.OCTAVE_MODULE_RF_DOWNCONVERTER, index=self._index)]
        )
        down_conv_state = response.rf_down_conv
        if isinstance(down_conv_state, RfDownConvUpdate):
            return down_conv_state
        else:
            raise Exception("could not get rf input state")

    def get_rf_source(self) -> RFInputRFSource:
        """ """
        rf_source: RfDownConvUpdateRfInput = self._get_current_state().rf_input
        if rf_source == RfDownConvUpdateRfInput.RF_INPUT_DISCONNECT:
            return RFInputRFSource.Off
        elif rf_source == RfDownConvUpdateRfInput.RF_INPUT_MAIN:
            return RFInputRFSource.RF_in
        elif rf_source == RfDownConvUpdateRfInput.RF_INPUT_DEBUG_1:
            return RFInputRFSource.Loopback_RF_out_1
        elif rf_source == RfDownConvUpdateRfInput.RF_INPUT_DEBUG_2:
            return RFInputRFSource.Loopback_RF_out_2
        elif rf_source == RfDownConvUpdateRfInput.RF_INPUT_DEBUG_3:
            return RFInputRFSource.Loopback_RF_out_3
        elif rf_source == RfDownConvUpdateRfInput.RF_INPUT_DEBUG_4:
            return RFInputRFSource.Loopback_RF_out_4
        elif rf_source == RfDownConvUpdateRfInput.RF_INPUT_DEBUG_5:
            return RFInputRFSource.Loopback_RF_out_5
        else:
            raise ValueError(f"Current RF source of rf input {self._index} is unknown")

    def set_rf_source(self, name: RFInputRFSource):
        """

        :param name:
        """

        if name not in self._possible_rf_sources:
            raise ValueError(f"RF source {name} is invalid for RF input {self._index}")

        crb = ClientRequestBuilder()
        if name == RFInputRFSource.RF_in:
            crb.down[self._index].rf_input = RfDownConvUpdateRfInput.RF_INPUT_MAIN
            crb.down[self._index].enabled = True
        elif name == RFInputRFSource.Loopback_RF_out_1:
            crb.down[self._index].rf_input = RfDownConvUpdateRfInput.RF_INPUT_DEBUG_1
            crb.down[self._index].enabled = True
        elif name == RFInputRFSource.Loopback_RF_out_2:
            crb.down[self._index].rf_input = RfDownConvUpdateRfInput.RF_INPUT_DEBUG_2
            crb.down[self._index].enabled = True
        elif name == RFInputRFSource.Loopback_RF_out_3:
            crb.down[self._index].rf_input = RfDownConvUpdateRfInput.RF_INPUT_DEBUG_3
            crb.down[self._index].enabled = True
        elif name == RFInputRFSource.Loopback_RF_out_4:
            crb.down[self._index].rf_input = RfDownConvUpdateRfInput.RF_INPUT_DEBUG_4
            crb.down[self._index].enabled = True
        elif name == RFInputRFSource.Loopback_RF_out_5:
            crb.down[self._index].rf_input = RfDownConvUpdateRfInput.RF_INPUT_DEBUG_5
            crb.down[self._index].enabled = True
        elif name == RFInputRFSource.Off:
            crb.down[self._index].rf_input = RfDownConvUpdateRfInput.RF_INPUT_DISCONNECT
            crb.down[self._index].enabled = False
        else:
            raise ValueError(f"RF source {name} is not supported. only `InputRfSource` enum values" f" are supported")

        self._context.client.update(crb.get_updates())

    def set_lo_source(self, source_name: RFInputLOSource, ignore_shared_errors: bool = False):
        """
        Set LO for the selected RFinput
        @param source_name: The LO type from RFInputLOSource
        @param ignore_shared_errors: Override shared LO error scenarios and replace with warning instead
        """
        self._set_lo_source_of_rf_in(source_name, select=True, ignore_shared_errors=ignore_shared_errors)

    def set_lo_frequency(self, source_name: RFInputLOSource, frequency: float):
        self._set_lo_source_of_rf_in(source_name, frequency=frequency)

    def get_lo_source(self) -> RFInputLOSource:
        """ """
        rf_in_source, synth_index = self._get_rf_in_lo_input()
        return convert_rf_in_lo_by_rf_out(rf_in_source, synth_index, self._context.connectivity.rf_out_by_synth())

    def get_lo_frequency(self) -> float:
        """ """
        rf_in_source, synth_index = self._get_rf_in_lo_input()
        if rf_in_source == RFInputLOSource.Internal or rf_in_source == RFInputLOSource.Analyzer:
            return _get_synth_state(self._context.client, synth_index).synth_output.frequency
        else:
            raise NotImplementedError()

    def _get_synth_external_secondary_input(self, synth_index):
        possible_sources = [
            u
            for u in self._context.connectivity.get_lo_source_by_synth_output(
                synth_index, SynthRfOutputOutputPort.OUTPUT_PORT_SECONDARY
            ).values()
            if u.module_info.synth_index == synth_index and u.module_info.synth_lo_input == _SynthLOInput.Secondary
        ]

        if len(possible_sources) != 1:
            raise ValueError(f"problem getting synth {synth_index} lo source")

        return (
            convert_octave_lo_input_enum_to_rf_in(possible_sources[0].name, synth_index),
            synth_index,
        )

    def _get_synth_external_main_input(self, synth_index):
        possible_sources = [
            u
            for u in self._context.connectivity.get_lo_source_by_synth_output(
                synth_index, SynthRfOutputOutputPort.OUTPUT_PORT_MAIN
            ).values()
            if u.module_info.synth_index == synth_index and u.module_info.synth_lo_input == _SynthLOInput.Main
        ]
        if len(possible_sources) != 1:
            raise ValueError("problem getting synth lo source")

        return (
            convert_octave_lo_input_enum_to_rf_in(possible_sources[0].name, synth_index),
            synth_index,
        )

    def _get_synth_main_lo(self, synth_state, synth_index):
        if synth_state.main_source == SynthUpdateMainSource.MAIN_SOURCE_EXTERNAL:
            return self._get_synth_external_main_input(synth_index)
        elif synth_state.main_source == SynthUpdateMainSource.MAIN_SOURCE_SYNTHESIZER:
            if synth_index == AnalyzerIndex:
                return RFInputLOSource.Analyzer, synth_index
            else:
                return RFInputLOSource.Internal, synth_index

    def _get_rf_in_lo_input(self) -> Mapping[RFInputLOSource, int]:
        lo_source = self._get_current_state().lo_input
        # validating what is connected to the synth
        (
            synth_index,
            synth_output,
        ) = self._context.connectivity.get_synth_index_of_rf_in_lo(self._index, lo_source)
        synth_state = _get_synth_state(self._context.client, synth_index)
        if synth_output == SynthRfOutputOutputPort.OUTPUT_PORT_MAIN:
            if synth_state.main_output == SynthUpdateMainOutput.MAIN_OUTPUT_MAIN:
                return self._get_synth_main_lo(synth_state, synth_index)
            else:
                return OctaveLOSource, synth_index
        elif synth_output == SynthRfOutputOutputPort.OUTPUT_PORT_SECONDARY:
            if synth_state.secondary_output == SynthUpdateSecondaryOutput.SECONDARY_OUTPUT_MAIN:
                return self._get_synth_main_lo(synth_state, synth_index)
            elif synth_state.secondary_output == SynthUpdateSecondaryOutput.SECONDARY_OUTPUT_AUXILARY:
                return self._get_synth_external_secondary_input(synth_index)
            else:
                return OctaveLOSource, synth_index
        else:
            raise ValueError("Could not get LO of RF input")

    def _set_lo_source_of_rf_in(
        self,
        name: RFInputLOSource,
        frequency: Optional[float] = None,
        select: Optional[bool] = None,
        ignore_shared_errors: bool = False,
        check_conflict: bool = False,
    ):

        (octave_lo_source, synth_index) = convert_rf_in_enum_to_octave_lo_input(
            name,
            self._context.connectivity.synth_by_rf_out(),
            self._context.connectivity.synth_by_lo_source(),
        )

        if (
            octave_lo_source == OctaveLOSource.Internal or octave_lo_source == OctaveLOSource.Off
        ) and synth_index == -1:
            synth_index = self._get_internal_synth_index()

        if (octave_lo_source, synth_index) not in self._possible_lo_sources_first and (
            octave_lo_source,
            synth_index,
        ) not in self._possible_lo_sources_second:
            possible_values = self._get_possible_lo_sources()

            unique_values = set(possible_values)
            raise InvalidLoSource(
                f"{name} is a not a valid LO source of RF input {self._index}. "
                f"possible values are: {','.join(map(str, unique_values))}"
            )

        if (octave_lo_source, synth_index) in self._possible_lo_sources_second:
            input_index = RfDownConvUpdateLoInput.LO_INPUT_2
            update_input_index = RfDownConvUpdateLoInput.LO_INPUT_2
            source_info = self._possible_lo_sources_second[(octave_lo_source, synth_index)]
        else:
            input_index = RfDownConvUpdateLoInput.LO_INPUT_1
            update_input_index = RfDownConvUpdateLoInput.LO_INPUT_1
            source_info = self._possible_lo_sources_first[(octave_lo_source, synth_index)]

        (
            synth_index,
            synth_output,
        ) = self._context.connectivity.get_synth_index_of_rf_in_lo(self._index, input_index)

        # get other input synth id so we can turn it off
        if input_index == RfDownConvUpdateLoInput.LO_INPUT_1:
            other = RfDownConvUpdateLoInput.LO_INPUT_2
        else:
            other = RfDownConvUpdateLoInput.LO_INPUT_1
        (
            other_synth_index,
            other_synth_output,
        ) = self._context.connectivity.get_synth_index_of_rf_in_lo(self._index, other)

        if select is not None and check_conflict:
            conflict_result = SynthConflicts(
                synth_index,
                synth_output,
                octave_lo_source,
                self._context.connectivity,
                self._context.client,
                request_up_or_down=SynthOutputDeviceInfo(index=self._index, up_or_down=UpOrDownId.DownConv),
                ignore_shared_errors=ignore_shared_errors,
            )
            if conflict_result.is_conflict:
                conflict_result.print_error()

        if octave_lo_source == OctaveLOSource.Internal:
            if frequency is not None:
                self._set_frequency(frequency, synth_index)

            if select is not None:
                crb = ClientRequestBuilder()
                crb.down[self._index].lo_input = update_input_index
                _set_synth_internal_mode(crb, synth_index, synth_output)

                self._context.client.update(crb.get_updates())

                if other_synth_index is not None:
                    _turn_off_synth_output(crb, other_synth_index, other_synth_output, self._index)

        elif octave_lo_source == OctaveLOSource.Off:
            crb = ClientRequestBuilder()
            _turn_off_synth_output(crb, synth_index, synth_output, self._index)

            self._context.client.update(crb.get_updates())

        elif octave_lo_source in self._context.connectivity.loopbacks:
            external_synth_output = self._context.connectivity.loopbacks[octave_lo_source]

            if frequency is not None:
                self._set_frequency(
                    frequency,
                    self._context.connectivity.get_synth_index_from_output_port(external_synth_output),
                )

            if select is not None:
                self._set_external(
                    input_index,
                    other_synth_index,
                    other_synth_output,
                    source_info,
                    synth_index,
                    synth_output,
                )

        else:
            if frequency is not None:
                raise UnableToSetFrequencyError(f"Frequency can not be set for external LO source {name}")
            if select is not None:
                self._set_external(
                    input_index,
                    other_synth_index,
                    other_synth_output,
                    source_info,
                    synth_index,
                    synth_output,
                )

    def _set_frequency(self, frequency, synth_index):
        crb = ClientRequestBuilder()
        crb.synth[synth_index].synth_output = SynthUpdateSynthOutput(frequency=frequency)
        crb.synth[synth_index].digital_attn = _get_synth_attenuation(lo_freq=frequency)
        self._context.client.update(crb.get_updates())

    def _set_external(
        self,
        input_index,
        other_synth_index,
        other_synth_output,
        source_info,
        synth_index,
        synth_output,
    ):
        crb = ClientRequestBuilder()
        crb.down[self._index].lo_input = input_index
        _set_synth_external_mode(
            crb,
            synth_index,
            synth_output,
            source_info.module_info.synth_lo_input,
        )
        self._context.client.update(crb.get_updates())
        if other_synth_index is not None:
            _turn_off_synth_output(crb, other_synth_index, other_synth_output, self._index)

    def _get_internal_synth_index(self):
        synth_index = -1
        _, analyzer_synth = convert_rf_in_enum_to_octave_lo_input(
            RFInputLOSource.Analyzer,
            self._context.connectivity.synth_by_rf_out(),
            self._context.connectivity.synth_by_lo_source(),
        )
        synth_possibilities = [
            index for source, index in self._possible_lo_sources_first.keys() if source == OctaveLOSource.Internal
        ] + [index for source, index in self._possible_lo_sources_second.keys() if source == OctaveLOSource.Internal]
        for pos in synth_possibilities:
            if pos != analyzer_synth:
                return pos

        for pos in synth_possibilities:
            return pos
        return synth_index

    def _get_possible_lo_sources(self):
        possible_values = [
            convert_rf_in_lo_by_rf_out(
                convert_octave_lo_input_enum_to_rf_in(e[0], e[1]),
                e[1],
                self._context.connectivity.rf_out_by_synth(),
            )
            for e in self._possible_lo_sources_first.keys()
        ] + [
            convert_rf_in_lo_by_rf_out(
                convert_octave_lo_input_enum_to_rf_in(e[0], e[1]),
                e[1],
                self._context.connectivity.rf_out_by_synth(),
            )
            for e in self._possible_lo_sources_second.keys()
        ]
        return possible_values

    def get_if_mode_i(self) -> IFMode:
        """ """
        return _get_if_mode(self._context.client, index=self._if_index, channel=1)

    def get_if_mode_q(self) -> IFMode:
        """ """
        return _get_if_mode(self._context.client, index=self._if_index, channel=2)

    def set_if_mode_i(self, mode: IFMode):
        """

        :param mode:
        """
        _set_if_mode(self._context.client, self._if_index, mode, channel_id=1)

    def set_if_mode_q(self, mode: IFMode):
        """

        :param mode:
        """
        _set_if_mode(self._context.client, self._if_index, mode, channel_id=2)

    def get_temperature(self) -> float:
        """

        :return: Celsius
        """
        # we have temperature for all modules, but here the important one is down conv
        return self._context.client.monitor().modules[OctaveModule.OCTAVE_MODULE_RF_DOWNCONVERTER][self._index - 1].temp

    def get_lo_sources(self) -> List[RFInputLoSourceOption]:
        return list(set([RFInputLoSourceOption(source) for source in self._get_possible_lo_sources()]))


class RFOutput:
    """ """

    def __init__(
        self,
        context: _OctaveContext,
        index: int,
    ) -> None:
        super().__init__()
        self._context = context
        self._index = index
        self._possible_lo_sources: Dict[
            Tuple[OctaveLOSource, int], _LoSourceInfo
        ] = context.connectivity.get_lo_source_of_rf_output(index)
        self._possible_lo_sources_names = set([s[0] for s in self._possible_lo_sources])

    def _get_current_state(self):
        response = self._context.client.aquire_modules(
            [ModuleReference(type=OctaveModule.OCTAVE_MODULE_RF_UPCONVERTER, index=self._index)]
        )
        up_conv_state = response.rf_up_conv
        if isinstance(up_conv_state, RfUpConvUpdate):
            return up_conv_state
        else:
            raise Exception("could not get rf output state")

    def get_gain(self) -> float:
        """ """
        raise NotImplementedError()

    def set_gain(self, gain: float, lo_frequency: Optional[float] = None, use_iq_attenuators: bool = False):
        crb = ClientRequestBuilder()

        if lo_frequency is not None:
            frequency = lo_frequency
        else:
            try:
                frequency = self.get_lo_frequency()
            except Exception as e:
                raise Exception(
                    f"Error, set gain to RFOut[{self._index}]"
                    f" has no frequency defined for the lo source."
                    f" Set the LO freq or implicitly add freq to set_gain"
                ) from e

            if frequency is None:
                raise Exception("there is no frequency defined on the lo source")

        self._set_gain(crb, gain, frequency, use_iq_attenuators)
        self._context.client.update(crb.get_updates())

    def _set_gain(self, crb, gain: float, frequency: float, use_iq_attenuators: bool):
        """
            if no lo_frequency is given, and lo source is internal, will use the
            internal frequency
        :param gain: dB
        :param gain: lo_frequency
        :param use_iq_attenuators: bool
        """

        # The following table matches total attenuation needed for 0dB gain as a function of frequency.
        # The units are in 0.5dB (the programmable attenuators units).
        attn_table = {
            1.6: 59,
            2.4: 59,
            2.9: 56,
            3.4: 57,
            3.9: 55,
            4.4: 53,
            4.9: 50,
            5.4: 51,
            5.9: 51,
            6.4: 51,
            6.9: 50,
            7.4: 50,
            7.9: 49,
            8.4: 48,
            8.9: 48,
            9.4: 46,
            9.9: 44,
            10.4: 43,
            10.9: 42,
            11.4: 42,
            11.9: 41,
            12.4: 40,
            12.9: 40,
            13.4: 39,
            13.9: 38,
            14.4: 38,
            14.9: 36,
            15.4: 35,
            15.9: 34,
            16.4: 32,
            16.9: 30,
            17.4: 29,
            17.9: 28,
            18.4: 26,
        }

        if 18e9 < frequency <= 18.4e9:
            logger.warning("LO frequency is above 18 GHz, this frequency is supported but performance is degraded.")
        if 1.6e9 <= frequency < 2e9:
            logger.warning("LO frequency is below 2 GHz, this frequency is supported but performance is degraded.")
        total_attn_0db = _interp_freq_to_attenuation(frequency, attn_table)

        # The gain is given in dB, hence we need to multiply by 2 (to match the units)
        total_attn = total_attn_0db - 2 * gain
        # Rounding
        total_attn = _round_to_int(total_attn)

        if total_attn < 0:
            raise ValueError(f"maximum gain for frequency {frequency/1e9:.3f}GHz is {total_attn_0db/2:.2f}dB")

        # We always enable the upconverter and use the power amplifier (to keep the heating constant)
        crb.up[self._index].enabled = True
        crb.up[self._index].power_amp_enabled = True

        # We will not use the IQ attenuator if the user explicitly ask for it, or we preper not to
        if not use_iq_attenuators or total_attn < 40:
            crb.up[self._index].input_attn = RfUpConvUpdateIfInputSelection.IF_INPUT_SELECTION_PASS_THROUGH

        else:
            crb.up[self._index].input_attn = RfUpConvUpdateIfInputSelection.IF_INPUT_SELECTION_ATTENUATE_10DB
            total_attn -= 20

        if total_attn < 20:
            crb.up[self._index].mixer_output_attn = total_attn
            crb.up[self._index].power_amp_attn = 0

        else:
            crb.up[self._index].mixer_output_attn = max(20, total_attn - 63)
            crb.up[self._index].power_amp_attn = total_attn - crb.up[self._index].mixer_output_attn

    def get_output(self) -> RFOutputMode:
        """ """
        up_conv_state = self._get_current_state()
        mode = up_conv_state.fast_switch_mode
        enabled = up_conv_state.enabled

        if mode == RfUpConvUpdateFastSwitchMode.FAST_SWITCH_MODE_OFF:
            if enabled:
                return RFOutputMode.debug
            else:
                return RFOutputMode.off
        elif mode == RfUpConvUpdateFastSwitchMode.FAST_SWITCH_MODE_DIRECT:
            return RFOutputMode.trig_normal
        elif mode == RfUpConvUpdateFastSwitchMode.FAST_SWITCH_MODE_ON:
            return RFOutputMode.on
        elif mode == RfUpConvUpdateFastSwitchMode.FAST_SWITCH_MODE_INVERTED:
            return RFOutputMode.trig_inverse
        else:
            raise ValueError(f"Current mode of rf output {self._index} is unknown")

    def _set_default_if_needed(self, crb: ClientRequestBuilder):
        up_conv_state = self._get_current_state()
        # TODO enabled = up_conv_state.enabled and up_conv_state.power_amp_enabled
        enabled = up_conv_state.power_amp_enabled
        if not enabled:
            # define default -20 dB on 8Ghz
            self._set_gain(crb, -20, 8e9, True)

    def set_output(self, mode: RFOutputMode):
        """

        :param mode:
        """
        crb = ClientRequestBuilder()

        if mode == RFOutputMode.off:
            crb.up[self._index].fast_switch_mode = RfUpConvUpdateFastSwitchMode.FAST_SWITCH_MODE_OFF
            crb.up[self._index].enabled = False
        elif mode == RFOutputMode.debug:
            crb.up[self._index].fast_switch_mode = RfUpConvUpdateFastSwitchMode.FAST_SWITCH_MODE_OFF
            self._set_default_if_needed(crb)
            crb.up[self._index].enabled = True
        elif mode == RFOutputMode.on:
            crb.up[self._index].fast_switch_mode = RfUpConvUpdateFastSwitchMode.FAST_SWITCH_MODE_ON
            self._set_default_if_needed(crb)
            crb.up[self._index].enabled = True
        elif mode == RFOutputMode.trig_normal:
            crb.up[self._index].fast_switch_mode = RfUpConvUpdateFastSwitchMode.FAST_SWITCH_MODE_DIRECT
            self._set_default_if_needed(crb)
            crb.up[self._index].enabled = True
        elif mode == RFOutputMode.trig_inverse:
            crb.up[self._index].fast_switch_mode = RfUpConvUpdateFastSwitchMode.FAST_SWITCH_MODE_INVERTED
            self._set_default_if_needed(crb)
            crb.up[self._index].enabled = True
        else:
            raise ValueError(
                f"RF Output Mode {mode} is not supported. only `RFOutputMode` enum" f" values are supported"
            )

        self._context.client.update(crb.get_updates())

    def set_lo_source(self, source_name: OctaveLOSource, ignore_shared_errors: bool = False):
        """
        Set LO for the selected RFoutput
        @param source_name: The LO type from OctaveLOSource
        @param ignore_shared_errors: Override shared LO error scenarios and replace with warning instead
        """
        self._set_lo_source_of_rf_out(source_name, select=True, ignore_shared_errors=ignore_shared_errors)

    def set_lo_frequency(self, source_name: OctaveLOSource, frequency: float):
        if frequency < 2e9 or frequency > 18e9:
            raise ValueError(f"frequency {frequency} is not supported")
        self._set_lo_source_of_rf_out(source_name, frequency=frequency)

    def get_lo_source(self) -> OctaveLOSource:
        """ """
        octave_lo_source, synth_index = self._get_rf_out_lo_input()
        return octave_lo_source

    def get_lo_frequency(self) -> float:
        """ """
        octave_lo_source, synth_index = self._get_rf_out_lo_input()

        if octave_lo_source == OctaveLOSource.Internal:
            return _get_synth_state(self._context.client, synth_index).synth_output.frequency
        else:
            raise Exception(f"could not get frequency of " f"external LO source - RF input {self._index}")

    def _get_synth_external_secondary_input(self, synth_index) -> Mapping[OctaveLOSource, int]:
        possible_sources = [
            u
            for u in self._possible_lo_sources.values()
            if u.module_info.synth_index == synth_index and u.module_info.synth_lo_input == _SynthLOInput.Secondary
        ]
        if len(possible_sources) != 1:
            raise ValueError(f"problem getting synth {synth_index} lo source")

        return possible_sources[0].name, synth_index

    def _get_synth_external_main_input(self, synth_index) -> Mapping[OctaveLOSource, int]:
        possible_sources = [
            u
            for u in self._possible_lo_sources.values()
            if u.module_info.synth_index == synth_index and u.module_info.synth_lo_input == _SynthLOInput.Main
        ]
        if len(possible_sources) != 1:
            raise ValueError("problem getting synth lo source")

        return possible_sources[0].name, synth_index

    def _get_synth_main_lo(self, synth_state, synth_index) -> Mapping[OctaveLOSource, int]:

        if synth_state.main_source == SynthUpdateMainSource.MAIN_SOURCE_EXTERNAL:
            return self._get_synth_external_main_input(synth_index)
        elif synth_state.main_source == SynthUpdateMainSource.MAIN_SOURCE_SYNTHESIZER:
            return OctaveLOSource.Internal, synth_index

    def _get_rf_out_lo_input(self) -> Mapping[OctaveLOSource, int]:
        # duplicate helper functions because it uses possible values dict
        # validating whats connected to the synth
        (
            synth_index,
            synth_output,
        ) = self._context.connectivity.get_synth_index_of_rf_out_lo(self._index)
        synth_state = _get_synth_state(self._context.client, synth_index)
        if synth_output == SynthRfOutputOutputPort.OUTPUT_PORT_MAIN:
            if synth_state.main_output == SynthUpdateMainOutput.MAIN_OUTPUT_MAIN:
                return self._get_synth_main_lo(synth_state, synth_index)
            else:
                return OctaveLOSource.Off, synth_index
        elif synth_output == SynthRfOutputOutputPort.OUTPUT_PORT_SECONDARY:
            if synth_state.secondary_output == SynthUpdateSecondaryOutput.SECONDARY_OUTPUT_MAIN:
                return self._get_synth_main_lo(synth_state, synth_index)
            elif synth_state.secondary_output == SynthUpdateSecondaryOutput.SECONDARY_OUTPUT_AUXILARY:
                return self._get_synth_external_secondary_input(synth_index)
            else:
                return OctaveLOSource.Off, synth_index
        else:
            # should not happen
            raise ValueError("Could not get LO input of RF output")

    def _set_lo_source_of_rf_out(
        self,
        name: OctaveLOSource,
        frequency: Optional[float] = None,
        select: Optional[bool] = None,
        ignore_shared_errors: bool = False,
        check_conflict: bool = False,
    ):
        if name not in self._possible_lo_sources_names:
            lo_names = map(str, set([e[0] for e in self._possible_lo_sources.keys()]))
            raise InvalidLoSource(
                f"{name} is a not a valid LO source of RF output {self._index}. "
                f"possible values are: {','.join(lo_names)}"
            )

        (
            synth_index,
            synth_output,
        ) = self._context.connectivity.get_synth_index_of_rf_out_lo(self._index)

        if select is not None and check_conflict:
            conflict_result = SynthConflicts(
                synth_index,
                synth_output,
                name,
                self._context.connectivity,
                self._context.client,
                request_up_or_down=SynthOutputDeviceInfo(index=self._index, up_or_down=UpOrDownId.UpConv),
                ignore_shared_errors=ignore_shared_errors,
            )
            if conflict_result.is_conflict:
                conflict_result.print_error()

        if name == OctaveLOSource.Internal:
            # use the synth_index and synth_output_port to set internal mode
            if frequency is not None:
                self._set_frequency(frequency, synth_index)

            if select is not None:
                crb = ClientRequestBuilder()
                _set_synth_internal_mode(crb, synth_index, synth_output)
                self._context.client.update(crb.get_updates())

        elif name == OctaveLOSource.Off:
            crb = ClientRequestBuilder()
            (
                synth_index,
                synth_output,
            ) = self._context.connectivity.get_synth_index_of_rf_out_lo(self._index)
            _turn_off_synth_output(crb, synth_index, synth_output, self._index)
            self._context.client.update(crb.get_updates())

        elif name in self._context.connectivity.loopbacks:
            external_synth_output = self._context.connectivity.loopbacks[name]

            if frequency is not None:
                self._set_frequency(
                    frequency,
                    self._context.connectivity.get_synth_index_from_output_port(external_synth_output),
                )

            if select is not None:
                self._set_external(name, synth_index, synth_output)
        else:
            if frequency is not None:
                raise UnableToSetFrequencyError(f"Frequency can not be set for external LO source {name}")

            if select is not None:
                self._set_external(name, synth_index, synth_output)

    def _set_frequency(self, frequency, synth_index):
        crb = ClientRequestBuilder()
        crb.synth[synth_index].gain = 0xFFFF
        crb.synth[synth_index].synth_output = SynthUpdateSynthOutput(frequency=frequency)
        crb.synth[synth_index].digital_attn = _get_synth_attenuation(lo_freq=frequency)
        self._context.client.update(crb.get_updates())

    def _set_external(self, name, synth_index, synth_output):
        source_info = self._possible_lo_sources[(name, synth_index)]
        crb = ClientRequestBuilder()
        _set_synth_external_mode(
            crb,
            synth_index,
            synth_output,
            source_info.module_info.synth_lo_input,
        )
        self._context.client.update(crb.get_updates())

    def get_temperature(self) -> float:
        """

        :return: Celsius
        """
        # we have temperature for all modules, but here the important one is upconv
        return self._context.client.monitor().modules[OctaveModule.OCTAVE_MODULE_RF_UPCONVERTER][self._index - 1].temp

    def get_iq_channels(self):
        return self._context.connectivity.get_iq_channels_for_rf_output(self._index)

    def get_lo_sources(self) -> List[RFOutputLoSourceOption]:
        return list(set([RFOutputLoSourceOption(source[0]) for source in self._possible_lo_sources.keys()]))


class RFInputs:
    """ """

    def __init__(self, context: _OctaveContext, indices: List[int]) -> None:
        super().__init__()
        self._context = context
        self._indices = indices
        self._rf_inputs = [RFInput(self._context, i) for i in self._indices]

    def __getitem__(self, item: int) -> RFInput:
        if item not in self._indices:
            raise IndexError(f"Index was {item} but valid RF " f"inputs are only {','.join(map(str, self._indices))}")
        return self._rf_inputs[self._indices.index(item)]

    def __iter__(self):
        return self._rf_inputs.__iter__()


class RFOutputs:
    """ """

    def __init__(self, context: _OctaveContext, indices: List[int]) -> None:
        super().__init__()
        self._context = context
        self._indices = indices
        self._rf_outputs = [RFOutput(self._context, i) for i in self._indices]

    def __getitem__(self, item) -> RFOutput:
        if item not in self._indices:
            raise IndexError(f"Index was {item} but valid RF " f"outputs are only {','.join(map(str, self._indices))}")
        return self._rf_outputs[self._indices.index(item)]

    def __iter__(self):
        return self._rf_outputs.__iter__()


class Octave:
    """ """

    def __init__(
        self,
        *,
        host: str,
        port: int,
        octave_name: str = None,
        port_mapping: Optional[Dict[OctaveLOSource, OctaveOutput]] = None,
        octave_client: Optional[OctaveClient] = None,
        fan=None,
        identity=None,
        connection_headers: Optional[Dict[str, str]] = None,
    ) -> None:
        """

        :param host:
        :param port:
        :param port_mapping: external loop backs, by the label on the box.
        """

        self._host = host
        self._port = port
        self._client = octave_client or OctaveClient(host, port, octave_name, connection_headers=connection_headers)

        self._connectivity_mutex = Lock()  # helps with debugging the health check code
        self._connectivity = None

        # temporary fix:
        self._client.debug_set(True, 1, 20, True, False, True, False, 45, 65, 75)
        if fan is not None:
            self._client.debug_set(monitor_update_fan=False)
            self._set_fan(fan)

        if identity is not None:
            self._identify_response = identity
        else:
            response = self._client.identify()
            if response is not None and len(response.rf_up_converters) > 0:
                self._identify_response: IdentifyResponse = response
            else:
                self._identify_response: IdentifyResponse = default_identify_response()

        self._port_mapping = port_mapping

        # Health check must be called for _reset_connectivity! and should be placed at the very end
        self._health = HealthMonitor(
            self._client,
            octave_name,
            self._reset_connectivity,
            ModulesSlotsFromIdentity(self._identify_response),
            interval_seconds=5,
        )

    def _reset_connectivity(self, explore_result):
        with self._connectivity_mutex:
            self._connectivity: Connectivity = Connectivity(self._identify_response, self._port_mapping, explore_result)

            self._handle_missing_modules()

            self._context = _OctaveContext(self._client, self._connectivity)

            self._rf_inputs = RFInputs(self._context, self._connectivity.rf_inputs_indices())
            self._rf_outputs = RFOutputs(self._context, self._connectivity.rf_outputs_indices())

    def _set_fan(self, fan):
        self._client.update([SingleUpdate(motherboard=MotherboardUpdate(fan))])

    def _get_fan(self):
        response: SingleUpdate = self._context.client.aquire_modules(
            [ModuleReference(type=OctaveModule.OCTAVE_MODULE_MOTHERBOARD, index=1)]
        )
        state = response.motherboard
        return state.fan_speed

    def _handle_missing_modules(self):
        for missing_module in self._connectivity.missing_modules:
            logger.warning(
                f'Octave "{self._client._octave_name}" {octave_module_to_module_name_mapping[missing_module.type]} index {slot_index_to_panel_mapping(missing_module.index, missing_module.type)} is malfunctioning!'
            )

    @staticmethod
    def start_batch_mode():
        BatchSingleton().start_batch_mode()

    @staticmethod
    def end_batch_mode():
        BatchSingleton().end_batch_mode()

    @property
    def rf_inputs(self) -> RFInputs:
        """

        :return:
        """
        return self._rf_inputs

    @property
    def rf_outputs(self) -> RFOutputs:
        """

        :return:
        """
        return self._rf_outputs

    def save_default_state(self, only_clock=False):
        modules = (
            None
            if not only_clock
            else [
                ModuleReference(OctaveModule.OCTAVE_MODULE_SOM, 1),
            ]
            + [ModuleReference(OctaveModule.OCTAVE_MODULE_SYNTHESIZER, i) for i in self._connectivity.synth_indices()]
        )
        result = self._client.save_modules(DEFAULT_STATE, modules, overwrite=True)
        if not result:
            raise Exception("Could not save state")

    def restore_default_state(self):
        self._client.recall(DEFAULT_STATE)

    def snapshot_state(self, name: str, modules: Optional[List] = None):
        if name == DEFAULT_STATE:
            raise ValueError(f"{DEFAULT_STATE} can not be the name of a snapshot")
        result = self._client.save_modules(name, modules, overwrite=True)
        if not result:
            raise Exception("Could not save state")

    def restore_state(self, snapshot_name: str):
        if snapshot_name == DEFAULT_STATE:
            raise ValueError(f"{DEFAULT_STATE} can not be the name of a snapshot")
        self._client.recall(snapshot_name)

    def set_clock(
        self,
        clock_type: ClockType,
        frequency: Optional[ClockFrequency] = None,
        synth_clock=125e6,
    ):
        """
        @param clock_type: Use external or internal or buffered mode
        @param frequency: Frequency of the system clock, not relevant for internal mode
        @param synth_clock: The clock frequency of the synth
        """

        # Not supporting MODE_INTERNAL_USE_1G/MODE_EXT_USE_1G yet
        clock_update = ClockUpdate(synthesizers_clock=synth_clock)
        if clock_type == ClockType.Buffered or (
            clock_type == ClockType.External and frequency == ClockFrequency.MHZ_1000
        ):
            clock_update.mode = ClockUpdateMode.MODE_BUFFERED
            if frequency is None:
                frequency = DEFAULT_CLOCK_FREQ
            elif frequency != DEFAULT_CLOCK_FREQ:
                raise ValueError(
                    "Buffered clock frequency must be 1000 MHz, please use External for",
                    ClockFrequency.MHZ_1000.name,
                )
        elif clock_type == ClockType.External:
            clock_update.mode = ClockUpdateMode.MODE_EXTERNAL
            if frequency is None:
                raise ValueError("Error, external clock frequency must be selected")
        elif clock_type == ClockType.Internal:
            if self.get_version() >= "1.2":
                clock_update.mode = ClockUpdateMode.MODE_INTERNAL_USE_1G
            else:
                clock_update.mode = ClockUpdateMode.MODE_INTERNAL
            if frequency is not None:
                logger.warning(f"Ignoring {frequency.name} clock setting and using internal 10MHz clock")
            frequency = ClockFrequency.MHZ_10

        if frequency == ClockFrequency.MHZ_10:
            clock_update.clock_frequency = 10e6
        elif frequency == ClockFrequency.MHZ_100:
            clock_update.clock_frequency = 100e6
        elif frequency == ClockFrequency.MHZ_1000:
            clock_update.clock_frequency = 1000e6

        # TODO if not between 100-150 - should add divider
        synths = [
            SingleUpdate(
                synth=SynthUpdate(
                    index=i,
                    reference_clock=SynthUpdateReferenceClock(
                        source=SynthUpdateReferenceSource.REFERENCE_SOURCE_EXTERNAL,
                        frequency=synth_clock,
                    ),
                )
            )
            for i in self._connectivity.synth_indices()
        ]

        self._client.update([SingleUpdate(clock=clock_update)] + synths)

    def get_clock(self) -> ClockInfo:
        response = self._client.aquire_modules([ModuleReference(type=OctaveModule.OCTAVE_MODULE_SOM, index=1)]).clock
        if isinstance(response, ClockUpdate):
            if response.mode == ClockUpdateMode.MODE_INTERNAL_USE_1G or response.mode == ClockUpdateMode.MODE_INTERNAL:
                clock_type = ClockType.Internal
            elif response.mode == ClockUpdateMode.MODE_EXTERNAL:
                clock_type = ClockType.External
            elif response.mode == ClockUpdateMode.MODE_BUFFERED:
                clock_type = ClockType.Buffered
            else:
                raise ValueError("can not validate clock mode")

            if response.clock_frequency == 10e6:
                frequency = ClockFrequency.MHZ_10
            elif response.clock_frequency == 100e6:
                frequency = ClockFrequency.MHZ_100
            elif response.clock_frequency == 1000e6:
                frequency = ClockFrequency.MHZ_1000
            else:
                raise ValueError("can not validate clock frequency")

            return ClockInfo(clock_type, frequency)

    def get_version(self) -> str:
        ver: GetVersionResponse = self._client.version()
        return json.loads(ver.version)["version"]

    def reset(self):
        """
        Will reset the entire Octave HW to default off state
        Warning, will block the code until reset completes
        """
        if self._client.reset():
            self._health.run_once()  # Reset the connectivity in case something changed after reset
            return True

        return False
