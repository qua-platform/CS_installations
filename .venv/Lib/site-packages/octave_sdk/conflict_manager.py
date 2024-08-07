from octave_sdk.batch import BatchSingleton
from octave_sdk.connectivity.connectivity import (
    OctaveLOSource,
    SynthOutputDeviceInfo,
    Connectivity,
)
from octave_sdk.grpc.quantummachines.octave.api.v1 import (
    SynthRfOutputOutputPort,
    SynthUpdateMainSource,
    SynthUpdateMainOutput,
    SynthUpdateSecondaryOutput,
    SynthUpdate,
)
from octave_sdk._octave_client import OctaveClient
from octave_sdk.octave_module_com import _get_synth_state
from octave_sdk.conflict_exceptions import (
    ConflictException,
    InternalShareConflictException,
    LoopbackInternalShareConflictException,
    InternalExternalOverrideException,
    CouplingConflictException,
)


def _is_synth_output_using_main_source_external(
    synth_out_port: SynthRfOutputOutputPort, synth_state: SynthUpdate
) -> bool:
    using, main_sw = _is_synth_output_using_main_source(synth_out_port, synth_state)

    return using and main_sw == SynthUpdateMainSource.MAIN_SOURCE_EXTERNAL


def _is_synth_output_using_internal(synth_out_port: SynthRfOutputOutputPort, synth_state: SynthUpdate):
    using, main_sw = _is_synth_output_using_main_source(synth_out_port, synth_state)

    return using and main_sw == SynthUpdateMainSource.MAIN_SOURCE_SYNTHESIZER


def _is_synth_output_using_main_source(
    synth_out_port: SynthRfOutputOutputPort, synth_state: SynthUpdate
) -> (bool, SynthUpdateMainSource):
    other_port_using_main_source: bool = False
    if synth_out_port == SynthRfOutputOutputPort.OUTPUT_PORT_SECONDARY:
        if (
            synth_state.secondary_output != SynthUpdateSecondaryOutput.SECONDARY_OUTPUT_OFF
            and synth_state.secondary_output != SynthUpdateSecondaryOutput.SECONDARY_OUTPUT_AUXILARY
        ):
            other_port_using_main_source = True
    elif synth_out_port == SynthRfOutputOutputPort.OUTPUT_PORT_MAIN:
        if synth_state.main_output != SynthUpdateMainOutput.MAIN_OUTPUT_OFF:
            other_port_using_main_source = True

    return other_port_using_main_source, synth_state.main_source


class Conflict:
    def __init__(self):
        self.is_conflict: bool = False
        self.conflict_up_or_down: SynthOutputDeviceInfo = None

    def is_must_raise_error(self) -> bool:
        return False

    def get_is_conflict(self):
        return self.is_conflict

    def get_exception_type(self):
        return ConflictException


class InternalShareConflict(Conflict):
    def __init__(
        self,
        connectivity: Connectivity,
        lo_source: OctaveLOSource,
        synth_index: int,
        other_port_using_internal,
        synth_out_other: SynthRfOutputOutputPort,
    ):
        super().__init__()

        if lo_source == OctaveLOSource.Internal and other_port_using_internal:
            self.is_conflict = True
            self.conflict_up_or_down = connectivity.get_rf_up_down_by_synth_output(synth_index, synth_out_other)

    def is_must_raise_error(self) -> bool:
        return False

    def get_is_conflict(self):
        return super().get_is_conflict()

    def get_exception_type(self):
        return InternalShareConflictException

    def __str__(self):
        return "share conflict"


class InternalExternalOverrideConflict(Conflict):
    def __init__(
        self,
        connectivity: Connectivity,
        synth_state: SynthUpdate,
        synth_index,
        main_source_next: SynthUpdateMainSource,
        other_port_using_main_source: bool,
        synth_out_other: SynthRfOutputOutputPort,
    ):
        super().__init__()

        if (
            other_port_using_main_source
            and synth_state.main_source != SynthUpdateMainSource.MAIN_SOURCE_UNSPECIFIED
            and main_source_next != SynthUpdateMainSource.MAIN_SOURCE_UNSPECIFIED
            and main_source_next != synth_state.main_source
        ):
            self.is_conflict = True
            self.conflict_up_or_down = connectivity.get_rf_up_down_by_synth_output(synth_index, synth_out_other)

    def is_must_raise_error(self) -> bool:
        return True

    def get_is_conflict(self):
        return super().get_is_conflict()

    def get_exception_type(self):
        return InternalExternalOverrideException

    def __str__(self):
        return "override the mode"


class LoopbackInternalShareConflict(Conflict):
    def __init__(self, connectivity: Connectivity, client: OctaveClient, lo_source, synth_index):
        super().__init__()
        if lo_source == OctaveLOSource.Off:
            return

        # User set ext lo while the synth origin internal is used scenario
        if lo_source in connectivity.loopbacks:
            synth_loopback_source_index = connectivity.get_synth_index_from_output_port(
                connectivity.loopbacks[lo_source]
            )
            synth_state_loopback_source = _get_synth_state(client, synth_loopback_source_index)
            synth_out_other_loopback = None
            if _is_synth_output_using_internal(SynthRfOutputOutputPort.OUTPUT_PORT_MAIN, synth_state_loopback_source):
                synth_out_other_loopback = SynthRfOutputOutputPort.OUTPUT_PORT_MAIN
            if _is_synth_output_using_internal(
                SynthRfOutputOutputPort.OUTPUT_PORT_SECONDARY, synth_state_loopback_source
            ):
                synth_out_other_loopback = SynthRfOutputOutputPort.OUTPUT_PORT_SECONDARY

            if synth_out_other_loopback is not None:
                self.is_conflict = True
                self.conflict_up_or_down = connectivity.get_rf_up_down_by_synth_output(
                    synth_loopback_source_index, synth_out_other_loopback
                )

        # User set internal while the external loopback is used in another synth
        if lo_source == OctaveLOSource.Internal:
            lo_loopback = None
            for lo, synth_panel in connectivity.loopbacks.items():
                if synth_index == connectivity.get_synth_index_from_output_port(synth_panel):
                    lo_loopback = lo
                    break
            if lo_loopback is not None:
                synth_loopback_sink_index = connectivity.synth_by_lo_source()[lo_loopback]
                synth_state_loopback_sink = _get_synth_state(client, synth_loopback_sink_index)

                synth_out_other_loopback = None
                if _is_synth_output_using_main_source_external(
                    SynthRfOutputOutputPort.OUTPUT_PORT_MAIN, synth_state_loopback_sink
                ):
                    synth_out_other_loopback = SynthRfOutputOutputPort.OUTPUT_PORT_MAIN
                if _is_synth_output_using_main_source_external(
                    SynthRfOutputOutputPort.OUTPUT_PORT_SECONDARY, synth_state_loopback_sink
                ):
                    synth_out_other_loopback = SynthRfOutputOutputPort.OUTPUT_PORT_SECONDARY

                if synth_out_other_loopback is not None:
                    self.is_conflict = True
                    self.conflict_up_or_down = connectivity.get_rf_up_down_by_synth_output(
                        synth_loopback_sink_index, synth_out_other_loopback
                    )

    def is_must_raise_error(self) -> bool:
        return False

    def get_is_conflict(self):
        return super().get_is_conflict()

    def get_exception_type(self):
        return LoopbackInternalShareConflictException

    def __str__(self):
        return "loopback share conflict"


class CouplingConflict(Conflict):
    def __init__(self):
        super().__init__()
        # Not implemented at this stage

    def is_must_raise_error(self) -> bool:
        return False

    def get_is_conflict(self):
        return super().get_is_conflict()

    def get_exception_type(self):
        return CouplingConflictException


class SynthConflicts:
    synth_state: SynthUpdate = None

    def __init__(
        self,
        synth_index: int,
        synth_out_to_be_used: SynthRfOutputOutputPort,
        lo_source: OctaveLOSource,
        connectivity: Connectivity,
        client: OctaveClient,
        request_up_or_down: SynthOutputDeviceInfo,
        ignore_shared_errors: bool,
    ):
        super().__init__()
        self.is_conflict = False
        self.request_up_or_down = request_up_or_down
        self.ignore_shared_errors = ignore_shared_errors
        self.lo_source = lo_source

        if BatchSingleton().is_batch_mode:
            if SynthConflicts.synth_state is None:
                SynthConflicts.synth_state = _get_synth_state(client, synth_index)
        else:
            SynthConflicts.synth_state = _get_synth_state(client, synth_index)

        # calc the next synth main source sw state
        main_source_next = SynthUpdateMainSource.MAIN_SOURCE_UNSPECIFIED
        if lo_source == OctaveLOSource.Off:
            pass
        elif lo_source == OctaveLOSource.Internal:
            main_source_next = SynthUpdateMainSource.MAIN_SOURCE_SYNTHESIZER
        elif synth_out_to_be_used == SynthRfOutputOutputPort.OUTPUT_PORT_MAIN:
            main_source_next = SynthUpdateMainSource.MAIN_SOURCE_EXTERNAL

        # check if using internal in the other port
        if synth_out_to_be_used == SynthRfOutputOutputPort.OUTPUT_PORT_MAIN:
            synth_out_other = SynthRfOutputOutputPort.OUTPUT_PORT_SECONDARY
        else:
            synth_out_other = SynthRfOutputOutputPort.OUTPUT_PORT_MAIN
        other_port_using_internal = _is_synth_output_using_internal(synth_out_other, SynthConflicts.synth_state)
        other_port_using_main_source, _ = _is_synth_output_using_main_source(
            synth_out_other, SynthConflicts.synth_state
        )

        # Check all conflicts types
        self._conflicts = [
            InternalShareConflict(connectivity, lo_source, synth_index, other_port_using_internal, synth_out_other),
            InternalExternalOverrideConflict(
                connectivity,
                SynthConflicts.synth_state,
                synth_index,
                main_source_next,
                other_port_using_main_source,
                synth_out_other,
            ),
            LoopbackInternalShareConflict(connectivity, client, lo_source, synth_index),
            CouplingConflict(),
        ]

        for conflict in self._conflicts:
            if conflict.get_is_conflict():
                self.is_conflict = True
                break

    def print_error(self):
        """
        Prints error/warnings to the user, in case conflicts found

        @return: None
        """
        for conflict in self._conflicts:
            if conflict.get_is_conflict():
                print_string = (
                    f"{self.request_up_or_down.up_or_down.value} {self.request_up_or_down.index} set lo "
                    f"source to {self.lo_source.name} will cause {conflict} with "
                    f"{conflict.conflict_up_or_down.up_or_down.value} {conflict.conflict_up_or_down.index}"
                )
                if conflict.is_must_raise_error() or not self.ignore_shared_errors:
                    print_string = "Error, " + print_string
                    if not conflict.is_must_raise_error():
                        print_string += ". Supress this error by using ignore_shared_errors=True"
                    raise conflict.get_exception_type()(print_string)
                else:
                    print_string = "Warning, " + print_string
                    print(print_string)
