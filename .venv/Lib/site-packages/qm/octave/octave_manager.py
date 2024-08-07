import logging
import warnings
import contextlib
import dataclasses
from enum import Enum
from time import perf_counter
from functools import lru_cache
from collections import defaultdict
from typing import TYPE_CHECKING, Any, Dict, List, Tuple, Union, Iterator, Optional, cast

from octave_sdk.octave import ClockInfo
from octave_sdk._octave_client import MonitorResult
from octave_sdk.grpc.quantummachines.octave.api.v1 import (
    ClockUpdate,
    OctaveModule,
    SingleUpdate,
    RfUpConvUpdate,
    ClockUpdateMode,
)
from octave_sdk import (
    IFMode,
    Octave,
    ClockType,
    OctaveOutput,
    RFOutputMode,
    ClockFrequency,
    OctaveLOSource,
    RFInputLOSource,
    RFInputRFSource,
)

from qm.type_hinting import Number
from qm.utils.config_utils import get_fem_config
from qm.octave.octave_config import QmOctaveConfig
from qm.type_hinting.config_types import StandardPort
from qm.octave._calibration_config import _prep_config
from qm.program._qua_config_to_pb import build_iw_sample
from qm.api.models.capabilities import ServerCapabilities
from qm.api.models.server_details import ConnectionDetails
from qm.exceptions import OpenQmException, OctaveLoopbackError
from qm.octave._calibration_names import COMMON_OCTAVE_PREFIX, CalibrationElementsNames
from qm.octave.octave_mixer_calibration import (
    AutoCalibrationParams,
    DeprecatedCalibrationResult,
    convert_to_old_calibration_result,
)
from qm.grpc.qua_config import (
    QuaConfig,
    QuaConfigMatrix,
    QuaConfigMixerDec,
    QuaConfigPulseDec,
    QuaConfigMixInputs,
    QuaConfigElementDec,
    QuaConfigSingleInput,
    QuaConfigWaveformDec,
    QuaConfigOctaveConfig,
    QuaConfigOctaveLoopback,
    QuaConfigCorrectionEntry,
    QuaConfigAdcPortReference,
    QuaConfigDacPortReference,
    QuaConfigPulseDecOperation,
    QuaConfigDigitalWaveformDec,
    QuaConfigConstantWaveformDec,
    QuaConfigOctaveLoSourceInput,
    QuaConfigIntegrationWeightDec,
    QuaConfigDigitalWaveformSample,
    QuaConfigOctaveOutputSwitchState,
    QuaConfigOctaveDownconverterRfSource,
)

if TYPE_CHECKING:
    from qm.api.v2.qm_api import QmApi
    from qm.quantum_machine import QuantumMachine
    from qm.quantum_machines_manager import QuantumMachinesManager

logger = logging.getLogger(__name__)


class SetFrequencyException(Exception):
    pass


class MixerCalibrationException(Exception):
    pass


class ClockMode(Enum):
    Internal = (ClockType.Internal, None)
    External_10MHz = (ClockType.External, ClockFrequency.MHZ_10)
    External_100MHz = (ClockType.External, ClockFrequency.MHZ_100)
    External_1000MHz = (ClockType.Buffered, ClockFrequency.MHZ_1000)


@dataclasses.dataclass
class _ControllerPorts:
    I: QuaConfigDacPortReference
    Q: QuaConfigDacPortReference

    def valid(self) -> bool:
        if self.I is None or self.Q is None:
            return False

        return self.I.controller == self.Q.controller and self.I.fem == self.Q.fem


@dataclasses.dataclass
class _UpconvertedState:
    lo_source: Optional[OctaveLOSource] = None
    lo_frequency: Optional[float] = None
    output_mode: Optional[RFOutputMode] = None
    output_gain: Optional[float] = None


class OctaveManager:
    def __init__(
        self,
        config: Optional[QmOctaveConfig],
        qmm: "QuantumMachinesManager",
        capabilities: ServerCapabilities,
    ) -> None:

        self._qmm = qmm
        self._capabilities = capabilities
        self._octave_config = config or QmOctaveConfig()
        self._upconverted_states: Dict[Tuple[str, int], _UpconvertedState] = {}
        self._perform_healthcheck_at_init()

    def _perform_healthcheck_at_init(self) -> None:
        for octave_name in self._octave_config.get_devices():
            self.get_client(octave_name)

    def get_client(self, name: str) -> Octave:
        return get_device(
            connection_info=self._octave_config._devices[name],
            loop_backs=self._octave_config.get_lo_loopbacks_by_octave(name),
            octave_name=name,
            fan=self._octave_config.fan,
        )

    def get_output_port(
        self,
        opx_i_port: StandardPort,
        opx_q_port: StandardPort,
    ) -> Optional[Tuple[str, int]]:
        warnings.warn(
            "This function is deprecated since 1.1.6 and will be removed in 1.2.0.",
            DeprecationWarning,
            stacklevel=2,
        )
        return self._octave_config.get_octave_input_port(opx_i_port, opx_q_port)

    def _get_client_from_port(self, octave_port: Tuple[str, int]) -> Octave:
        return self.get_client(octave_port[0])

    def restore_default_state(self, octave_name: str) -> None:
        self.get_client(octave_name).restore_default_state()

    def start_batch_mode(self) -> None:
        for octave_name in self._octave_config.get_devices():
            self.get_client(octave_name).start_batch_mode()

    def end_batch_mode(self) -> None:
        for octave_name in self._octave_config.get_devices():
            self.get_client(octave_name).end_batch_mode()

    @contextlib.contextmanager
    def batch_mode(self) -> Iterator[None]:
        self.start_batch_mode()
        yield
        self.end_batch_mode()

    def set_clock(
        self,
        octave_name: str,
        clock_type: Optional[ClockType] = None,
        frequency: Optional[ClockFrequency] = None,
        clock_mode: Optional[ClockMode] = None,
    ) -> None:

        """This function will set the octave clock type - internal, external or buffered.
        It can also set the clock frequency - 10, 100 or 1000 MHz

        Args:
            octave_name: str
            clock_type: ClockType
            frequency: ClockFrequency
            clock_mode: ClockMode

        Returns:

        """
        if clock_mode is None:
            pass
            # warnings.warn(
            #     "set_clock is changing its API, and the 'clock_type' and 'frequency' arguments will be "
            #     "removed in the next version, please use the 'mode' parameter.",
            #     category=DeprecationWarning,
            #     stacklevel=2,
            # )
        else:
            clock_type, frequency = clock_mode.value

        client = self.get_client(octave_name)
        client.set_clock(clock_type, frequency)
        client.save_default_state(only_clock=True)

    def get_clock(self, octave_name: str) -> ClockInfo:
        """Return the octave clock type and frequency

        Args:
            octave_name: str

        Returns:
            ClockInfo
        """
        clock = self.get_client(octave_name).get_clock()
        return ClockInfo(clock.clock_type, clock.frequency)

    def set_lo_frequency(
        self,
        octave_output_port: Tuple[str, int],
        lo_frequency: float,
        lo_source: OctaveLOSource = OctaveLOSource.Internal,
        set_source: bool = True,
    ) -> None:
        """Sets the LO frequency of the synthesizer associated to element

        Args:
            octave_output_port
            lo_frequency
            lo_source
            set_source
        """
        # warnings.warn(
        #     deprecation_message(
        #         "OctaveManager.set_lo_frequency()",
        #         "1.1.0",
        #         "1.2.0",
        #         "set_lo_frequency will be removed, please use the relevant element.",
        #     ),
        #     category=DeprecationWarning,
        # )
        octave = self._get_client_from_port(octave_output_port)
        octave_name, port_index = octave_output_port

        loop_backs = self._octave_config.get_lo_loopbacks_by_octave(octave_name)

        if lo_source != OctaveLOSource.Internal and lo_source not in loop_backs:
            raise SetFrequencyException(f"Cannot set frequency to an external lo source" f" {lo_source.name}")

        if set_source:
            octave.rf_outputs[port_index].set_lo_source(lo_source)

        octave.rf_outputs[port_index].set_lo_frequency(lo_source, lo_frequency)

    def set_lo_source(self, octave_output_port: Tuple[str, int], lo_port: OctaveLOSource) -> None:
        """Sets the source of LO going to the upconverter associated with element.

        Args:
            octave_output_port
            lo_port
        """
        octave = self._get_client_from_port(octave_output_port)
        octave.rf_outputs[octave_output_port[1]].set_lo_source(lo_port)

    def set_rf_output_mode(self, octave_output_port: Tuple[str, int], switch_mode: RFOutputMode) -> None:
        """Configures the output switch of the upconverter associated to element.
        switch_mode can be either: 'always_on', 'always_off', 'normal' or 'inverted'
        When in 'normal' mode a high trigger will turn the switch on and a low
        trigger will turn it off
        When in 'inverted' mode a high trigger will turn the switch off and a low
        trigger will turn it on
        When in 'always_on' the switch will be permanently on. When in 'always_off'
        mode the switch will be permanently off.

        Args:
            octave_output_port
            switch_mode
        """
        octave = self._get_client_from_port(octave_output_port)
        index = octave_output_port[1]
        octave.rf_outputs[octave_output_port[1]].set_output(switch_mode)

        # Shuts down the second stage amplifier if the switch is off
        power_amp_enabled = switch_mode != RFOutputMode.off
        octave._client.update(
            updates=[SingleUpdate(rf_up_conv=RfUpConvUpdate(index=index, power_amp_enabled=power_amp_enabled))]
        )

    def set_rf_output_gain(
        self,
        octave_output_port: Tuple[str, int],
        gain_in_db: float,
        lo_frequency: Optional[float] = None,
    ) -> None:
        """Sets the RF output gain for the upconverter associated with element.
        if no lo_frequency is given, and lo source is internal, will use the
        internal frequency

        Args:
            octave_output_port
            gain_in_db
            lo_frequency
        """
        octave = self._get_client_from_port(octave_output_port)
        octave.rf_outputs[octave_output_port[1]].set_gain(gain_in_db, lo_frequency)

    def set_downconversion_lo_source(
        self,
        octave_input_port: Tuple[str, int],
        lo_source: RFInputLOSource,
        lo_frequency: Optional[float] = None,
        disable_warning: Optional[bool] = False,
    ) -> None:
        """Sets the LO source for the downconverters.

        Args:
            octave_input_port
            lo_source
            lo_frequency
            disable_warning
        """
        octave = self._get_client_from_port(octave_input_port)
        octave.rf_inputs[octave_input_port[1]].set_lo_source(lo_source)
        octave.rf_inputs[octave_input_port[1]].set_rf_source(RFInputRFSource.RF_in)
        internal = lo_source == RFInputLOSource.Internal or lo_source == RFInputLOSource.Analyzer
        if lo_frequency is not None and internal:
            octave.rf_inputs[octave_input_port[1]].set_lo_frequency(source_name=lo_source, frequency=lo_frequency)

    def set_downconversion_if_mode(
        self,
        octave_input_port: Tuple[str, int],
        if_mode_i: IFMode = IFMode.direct,
        if_mode_q: IFMode = IFMode.direct,
        disable_warning: Optional[bool] = False,
    ) -> None:
        """Sets the IF downconversion stage.
        if_mode can be one of: 'direct', 'mixer', 'envelope_DC', 'envelope_AC','OFF'
        If only one value is given the setting is applied to both IF channels
        (I and Q) for the downconverter associated to element
        (how will we know that? shouldn't this be per downconverter?)
        If if_mode is a tuple, then the IF stage will be assigned to each
        quadrature independently, i.e.:
        if_mode = ('direct', 'envelope_AC') will set the I-channel to be
        direct and the Q-channel to be 'envelope_AC'

        Args:
            disable_warning
            octave_input_port
            if_mode_q
            if_mode_i
        """

        octave = self._get_client_from_port(octave_input_port)
        octave.rf_inputs[octave_input_port[1]].set_if_mode_i(if_mode_i)
        octave.rf_inputs[octave_input_port[1]].set_if_mode_q(if_mode_q)

    def reset(self, octave_name: str) -> bool:
        """
        Will reset the entire Octave HW to default off state
        Warning, will block the code until reset completes

        :param octave_name: str
        :return: True on success, False otherwise
        """
        if self._capabilities.supports_octave_reset:
            return cast(bool, self.get_client(octave_name).reset())
        else:
            logger.error("QOP version do not support Octave reset function")
            return False

    def calibrate(
        self,
        octave_output_port: Tuple[str, int],
        lo_if_frequencies_tuple_list: List[Tuple[int, int]],
        save_to_db: bool = True,
        close_open_quantum_machines: bool = True,
        optimizer_parameters: Optional[Dict[str, Any]] = None,
        offset_frequency: float = 7e6,
        **kwargs: Any,
    ) -> Dict[Tuple[int, int], DeprecatedCalibrationResult]:
        """calibrates IQ mixer associated with element

        Args:
            close_open_quantum_machines: Boolean, if true (default) all
                running QMs
            octave_output_port
            lo_if_frequencies_tuple_list: A list of LO/IF frequencies
                for which the calibration is to be performed [(LO1,
                IF1), (LO2, IF2), ...]
            save_to_db
            optimizer_parameters
        will be closed for the calibration. Otherwise,
        calibration might fail if there are not enough resources for the calibration
        """
        # warnings.warn(
        #     "This function is deprecated, please use the 'calibrate_element' in the QuantumMachine instance",
        #     category=DeprecationWarning,
        # )
        if kwargs:
            logger.warning(f"unused kwargs: {list(kwargs)}, please remove them.")

        lo_to_if_mapping = _create_lo_to_if_mapping(lo_if_frequencies_tuple_list)
        lo_freq = list(lo_to_if_mapping)[0]

        if_freq_list = lo_to_if_mapping[lo_freq]
        first_if = if_freq_list[0]

        qm_inst = self._create_dedicated_qm(
            lo_freq,
            first_if,
            octave_output_port,
            close_open_quantum_machines,
        )

        calibration_result = qm_inst.calibrate_element(
            "to_calibrate",
            lo_to_if_mapping,
            save_to_db=save_to_db,
            params=AutoCalibrationParams(offset_frequency=offset_frequency),
        )

        return convert_to_old_calibration_result(calibration_result, "Correction_mixer")

    def _create_dedicated_qm(
        self,
        first_lo: Number,
        first_if: Number,
        octave_output_port: Tuple[str, int],
        close_open_quantum_machines: bool = True,
    ) -> Union["QuantumMachine", "QmApi"]:
        iq_channels = self._octave_config.get_opx_iq_ports(octave_output_port)
        controller_name = iq_channels[0][0]
        adc_channels = ((controller_name, 1), (controller_name, 2))
        config = _prep_config(
            iq_channels,
            adc_channels,
            first_if,
            first_lo,
        )
        try:
            t0 = perf_counter()
            qm_inst = self._qmm.open_qm(
                config, close_other_machines=close_open_quantum_machines, add_calibration_elements_to_config=True
            )
            logger.debug(f"Creating dedicated QM for calibration took {perf_counter() - t0}")
        except OpenQmException as e:
            raise MixerCalibrationException("Mixer calibration failed: Could not open a quantum machine.") from e

        return qm_inst

    def set_octaves_from_qua_config(self, octaves_config: Dict[str, QuaConfigOctaveConfig]) -> None:
        if not octaves_config:
            # This if serves two things - if the user uses the old API, no need to set the octaves,
            # and if there are no octaves in the qua config, but there are in the cluster,
            # we still want to skip the batch mode.
            return
        for octave_name, octave_config in octaves_config.items():
            pb_loopbacks = octave_config.loopbacks
            loopbacks = get_loopbacks_from_pb(pb_loopbacks, octave_name)
            connection_info = self._octave_config.devices[octave_name]
            octave = get_device(connection_info, loopbacks, octave_name)
            octave.start_batch_mode()
            for output_port_idx, output_config in octave_config.rf_outputs.items():
                output_client = octave.rf_outputs[output_port_idx]
                config_lo_source = output_config.lo_source
                if config_lo_source == QuaConfigOctaveLoSourceInput.internal:
                    lo_source = OctaveLOSource.Internal
                elif config_lo_source == QuaConfigOctaveLoSourceInput.external:
                    lo_source = OctaveLOSource[f"LO{output_port_idx}"]
                else:
                    raise ValueError(f"lo_source {config_lo_source} is not supported")

                output_client.set_lo_source(lo_source)

                if lo_source == OctaveLOSource.Internal or lo_source in loopbacks:
                    output_client.set_lo_frequency(lo_source, output_config.lo_frequency)
                else:
                    logger.debug(f"Cannot set frequency to an external lo source {lo_source.name}")

                output_mode = {
                    QuaConfigOctaveOutputSwitchState.always_on: RFOutputMode.on,
                    QuaConfigOctaveOutputSwitchState.always_off: RFOutputMode.off,
                    QuaConfigOctaveOutputSwitchState.triggered: RFOutputMode.trig_normal,
                    QuaConfigOctaveOutputSwitchState.triggered_reversed: RFOutputMode.trig_inverse,
                }[output_config.output_mode]
                output_client.set_output(output_mode)
                output_client.set_gain(
                    output_config.gain,
                    output_config.lo_frequency,
                    use_iq_attenuators=output_config.input_attenuators,
                )

            for input_port_idx, input_config in octave_config.rf_inputs.items():
                input_client = octave.rf_inputs[input_port_idx]
                input_source = {
                    QuaConfigOctaveDownconverterRfSource.rf_in: RFInputRFSource.RF_in,
                    QuaConfigOctaveDownconverterRfSource.loopback_1: RFInputRFSource.Loopback_RF_out_1,
                    QuaConfigOctaveDownconverterRfSource.loopback_2: RFInputRFSource.Loopback_RF_out_2,
                    QuaConfigOctaveDownconverterRfSource.loopback_3: RFInputRFSource.Loopback_RF_out_3,
                    QuaConfigOctaveDownconverterRfSource.loopback_4: RFInputRFSource.Loopback_RF_out_4,
                    QuaConfigOctaveDownconverterRfSource.loopback_5: RFInputRFSource.Loopback_RF_out_5,
                }[input_config.rf_source]
                input_client.set_rf_source(input_source)

                if input_config.lo_source == QuaConfigOctaveLoSourceInput.internal:
                    downconversion_lo_source = RFInputLOSource.Internal
                elif input_config.lo_source == QuaConfigOctaveLoSourceInput.external:
                    downconversion_lo_source = RFInputLOSource[f"Dmd{input_port_idx}LO"]
                elif input_config.lo_source == QuaConfigOctaveLoSourceInput.analyzer:
                    downconversion_lo_source = RFInputLOSource.Analyzer
                else:
                    raise ValueError(f"lo_source {input_config.lo_source} is not supported")

                input_client.set_lo_source(downconversion_lo_source)
                if (
                    downconversion_lo_source == RFInputLOSource.Internal
                    or (downconversion_lo_source == RFInputLOSource.Dmd1LO and OctaveLOSource.Dmd1LO in loopbacks)
                    or (downconversion_lo_source == RFInputLOSource.Dmd2LO and OctaveLOSource.Dmd2LO in loopbacks)
                ):
                    input_client.set_lo_frequency(downconversion_lo_source, input_config.lo_frequency)
                else:
                    logger.debug(f"Cannot set frequency to an external lo source {downconversion_lo_source.name}")

                input_client.set_if_mode_i(IFMode[input_config.if_mode_i.name])
                input_client.set_if_mode_q(IFMode[input_config.if_mode_q.name])
            octave.end_batch_mode()


def get_som_temp(monitor_data: MonitorResult) -> float:
    return cast(float, monitor_data.modules[OctaveModule.OCTAVE_MODULE_SOM][0].temp)


def _set_clock_in(octave: Octave, clock_in: ClockInfo) -> None:
    client = octave._client

    def _update_clock(mode: ClockUpdateMode, frequency: float) -> None:
        _update = ClockUpdate(mode=mode, clock_frequency=frequency, synthesizers_clock=125e6)
        client.update(updates=[SingleUpdate(clock=_update)])

    _update_clock(ClockUpdateMode.MODE_INTERNAL_USE_1G, 10e6)

    mon = client.monitor()
    has_1g = 0 < get_som_temp(mon) < 100

    if clock_in.clock_type == ClockType.Internal:
        if has_1g:
            # we are already have a programmed internal clock (using the internal 1G)
            return

        # An internal clock is already programmed, but it seems like the internal 1G VCO is
        # not working. Hence, we switch to use the internal 3G VCO (that's the best we can do)
        _update_clock(ClockUpdateMode.MODE_INTERNAL, 10e6)
        return

    if clock_in.clock_type == ClockType.Buffered:
        _update_clock(ClockUpdateMode.MODE_BUFFERED, 1e9)

        # The FPGA's temperature is our indication that the clock is fine. We read it again after
        # changing the clock configuration.
        mon = client.monitor()
        if 0 < get_som_temp(mon) < 100:
            # All good, the buffered clock feeds the FPGA successfully.
            return

        clock_mode = ClockUpdateMode.MODE_INTERNAL_USE_1G
        if not has_1g:
            clock_mode = ClockUpdateMode.MODE_INTERNAL
        _update_clock(clock_mode, 10e6)
        print("Not sensing any 1GHz input clock for the octave (buffered), switching to internal clock")
        return

    # Clock mode is external at this point
    clock_mode = ClockUpdateMode.MODE_EXTERNAL_USE_1G
    if not has_1g:
        clock_mode = ClockUpdateMode.MODE_EXTERNAL
    clock_in_frequency = {
        ClockFrequency.MHZ_10: 10e6,
        ClockFrequency.MHZ_100: 100e6,
        ClockFrequency.MHZ_1000: 1000e6,
    }[clock_in.frequency]
    _update_clock(clock_mode, clock_in_frequency)

    # Again, verify the clock is good...
    mon = client.monitor()
    if 0 < get_som_temp(mon) < 100:
        # All good, the buffered clock feeds the FPGA successfully.
        return

    clock_mode = ClockUpdateMode.MODE_INTERNAL_USE_1G
    if not has_1g:
        clock_mode = ClockUpdateMode.MODE_INTERNAL
    _update_clock(clock_mode, 10e6)
    print("Not sensing any 1GHz input clock for the octave (external), switching to internal clock")


def create_lo_to_if_list_mapping(lo_if_frequencies_tuple_list: List[Tuple[int, int]]) -> Dict[int, List[int]]:
    lo_to_if_mapping = defaultdict(list)
    for lo_freq, if_freq in lo_if_frequencies_tuple_list:
        lo_to_if_mapping[lo_freq].append(if_freq)
    return lo_to_if_mapping


def get_loopbacks_from_pb(
    pb_loopbacks: List[QuaConfigOctaveLoopback], octave_name: str
) -> Dict[OctaveLOSource, OctaveOutput]:
    loopbacks = {}
    for loopback in pb_loopbacks:
        source_octave = loopback.lo_source_generator.device_name
        if source_octave != octave_name:
            raise OctaveLoopbackError
        lo_source_input = OctaveLOSource[loopback.lo_source_input.name]
        output_name = loopback.lo_source_generator.port_name.name
        standardized_name = output_name[0].upper() + output_name[1:]
        # we use snake case but octave_sdk is camel case
        loopbacks[lo_source_input] = OctaveOutput[standardized_name]
    return loopbacks


def _get_octave_channels_to_opx_ports(
    pb_config: QuaConfig, octave_config: QmOctaveConfig
) -> Dict[str, Dict[int, _ControllerPorts]]:
    """# octave_id -> (channel -> _OpxPorts)"""

    def is_dac_declared(dac: QuaConfigDacPortReference) -> bool:
        try:
            controller_config = get_fem_config(pb_config, dac)
        except KeyError:
            return False
        return dac.number in controller_config.analog_outputs

    all_octave_channels: Dict[str, Dict[int, _ControllerPorts]] = defaultdict(dict)
    opx_octave_port_mapping = octave_config.get_opx_octave_port_mapping()
    octave_opx_port_mapping = {v: k for k, v in opx_octave_port_mapping.items()}
    octave_names = {v[0] for v in octave_opx_port_mapping}
    for octave_name in octave_names:
        for channel_index in range(1, 6):
            i_key, q_key = (octave_name, f"I{channel_index}"), (octave_name, f"Q{channel_index}")
            if i_key in octave_opx_port_mapping and q_key in octave_opx_port_mapping:
                con_i, fem_i, idx_i = octave_opx_port_mapping[i_key]
                con_q, fem_q, idx_q = octave_opx_port_mapping[q_key]
                all_octave_channels[octave_name][channel_index] = _ControllerPorts(
                    I=QuaConfigDacPortReference(controller=con_i, fem=fem_i, number=idx_i),
                    Q=QuaConfigDacPortReference(controller=con_q, fem=fem_q, number=idx_q),
                )

    for octave_name, octave_pb_config in pb_config.v1_beta.octaves.items():
        all_octave_channels[octave_name] = {}
        for upconverter_index, upconverter_config in octave_pb_config.rf_outputs.items():
            all_octave_channels[octave_name][upconverter_index] = _ControllerPorts(
                I=upconverter_config.i_connection,
                Q=upconverter_config.q_connection,
            )

    to_return: Dict[str, Dict[int, _ControllerPorts]] = {}
    for octave_name, octave_channels in all_octave_channels.items():
        to_return[octave_name] = {}
        for channel_index, opx_ports in octave_channels.items():
            if is_dac_declared(opx_ports.I) and is_dac_declared(opx_ports.Q):
                to_return[octave_name][channel_index] = opx_ports

    return to_return


def prep_config_for_calibration(
    pb_config: QuaConfig, octave_config: QmOctaveConfig, capabilities: ServerCapabilities
) -> QuaConfig:
    all_octave_channels = _get_octave_channels_to_opx_ports(pb_config, octave_config)
    for octave_channels in all_octave_channels.values():
        for controller_ports in octave_channels.values():
            if controller_ports.valid():
                controller_config = get_fem_config(pb_config, controller_ports.I)
                if set(controller_config.analog_inputs) != {1, 2}:
                    logger.warning(
                        f"Controller '{controller_ports.I.controller}', {controller_ports.I.fem} does not have exactly two input "
                        f"channels declared in the QUA-config and is needed for the calibration, "
                        f"not adding calibration elements"
                    )
                    return pb_config

    dummy_lo_frequency: float = 6e9
    dummy_if_frequency: float = 50e6

    dummy_down_mixer_offset: float = 7e6

    offset_amp = 0.25
    weight_amplitude = 1.0

    integration_length = 10000
    stabilization_length = 1400
    wrap_up_length = 600

    calibration_pulse_length = integration_length + stabilization_length + wrap_up_length
    calibration_amp = 0.125

    time_of_flight = stabilization_length

    frequency_idx = int(capabilities.supports_double_frequency)  # This is to shorten many if-else in the code using
    # a trinary expression

    any_valid_channels = False
    for octave_name, octave_channels in all_octave_channels.items():
        for channel_index, controller_ports in octave_channels.items():
            names = CalibrationElementsNames(octave_name, channel_index)
            if controller_ports.valid():
                any_valid_channels = True
                mix_inputs = QuaConfigMixInputs(
                    i=controller_ports.I,
                    q=controller_ports.Q,
                    lo_frequency=int(dummy_lo_frequency),
                    lo_frequency_double=[0.0, float(dummy_lo_frequency)][frequency_idx],
                    mixer=f"{COMMON_OCTAVE_PREFIX}dummy_mixer",
                )

                def create_analyzer_element(intermediate_frequency: float) -> QuaConfigElementDec:
                    return QuaConfigElementDec(
                        intermediate_frequency=abs(int(intermediate_frequency)),
                        intermediate_frequency_double=[0.0, abs(float(intermediate_frequency))][frequency_idx],
                        intermediate_frequency_negative=intermediate_frequency < 0,
                        mix_inputs=mix_inputs,
                        operations={"Analyze": f"{COMMON_OCTAVE_PREFIX}Analyze_pulse"},
                        outputs={
                            "out1": QuaConfigAdcPortReference(
                                controller=controller_ports.I.controller, fem=controller_ports.I.fem, number=1
                            ),
                            "out2": QuaConfigAdcPortReference(
                                controller=controller_ports.Q.controller, fem=controller_ports.Q.fem, number=2
                            ),
                        },
                        time_of_flight=time_of_flight,
                        smearing=0,
                    )

                # 1. Add the required elements (IQmixer, [IQ]_offset, [signal/lo/image]_analyzer)
                i_offset = QuaConfigElementDec(
                    single_input=QuaConfigSingleInput(port=controller_ports.I),
                    operations={"DC_offset": f"{COMMON_OCTAVE_PREFIX}DC_offset_pulse"},
                )
                q_offset = QuaConfigElementDec(
                    single_input=QuaConfigSingleInput(port=controller_ports.Q),
                    operations={"DC_offset": f"{COMMON_OCTAVE_PREFIX}DC_offset_pulse"},
                )
                # TODO - remove this and the capability once we fix the bug in the OPY of the CSF allocation
                if capabilities.set_zero_frequency_in_calibration:
                    i_offset.intermediate_frequency = 0
                    q_offset.intermediate_frequency = 0
                pb_config.v1_beta.elements.update(
                    {
                        names.iq_mixer: QuaConfigElementDec(
                            mix_inputs=mix_inputs,
                            intermediate_frequency=abs(int(dummy_if_frequency)),
                            intermediate_frequency_double=[0.0, abs(float(dummy_if_frequency))][frequency_idx],
                            operations={"calibration": f"{COMMON_OCTAVE_PREFIX}calibration_pulse"},
                            digital_inputs={},  # This is being added afterward
                        ),
                        names.i_offset: i_offset,
                        names.q_offset: q_offset,
                        names.signal_analyzer: create_analyzer_element(dummy_if_frequency - dummy_down_mixer_offset),
                        names.lo_analyzer: create_analyzer_element(-dummy_down_mixer_offset),
                        names.image_analyzer: create_analyzer_element(-dummy_if_frequency - dummy_down_mixer_offset),
                    }
                )

    if any_valid_channels:
        pb_config.v1_beta.pulses.update(
            {
                f"{COMMON_OCTAVE_PREFIX}calibration_pulse": QuaConfigPulseDec(
                    operation=QuaConfigPulseDecOperation.CONTROL,
                    length=calibration_pulse_length,
                    digital_marker=f"{COMMON_OCTAVE_PREFIX}ON",
                    waveforms={
                        "I": f"{COMMON_OCTAVE_PREFIX}readout_wf",
                        "Q": f"{COMMON_OCTAVE_PREFIX}zero_wf",
                    },
                ),
                f"{COMMON_OCTAVE_PREFIX}DC_offset_pulse": QuaConfigPulseDec(
                    operation=QuaConfigPulseDecOperation.CONTROL,
                    length=calibration_pulse_length,
                    waveforms={"single": f"{COMMON_OCTAVE_PREFIX}DC_offset_wf"},
                ),
                f"{COMMON_OCTAVE_PREFIX}Analyze_pulse": QuaConfigPulseDec(
                    operation=QuaConfigPulseDecOperation.MEASUREMENT,
                    length=integration_length,
                    waveforms={
                        "I": f"{COMMON_OCTAVE_PREFIX}zero_wf",
                        "Q": f"{COMMON_OCTAVE_PREFIX}zero_wf",
                    },
                    integration_weights={
                        "integW_cos": f"{COMMON_OCTAVE_PREFIX}integW_cosine",
                        "integW_sin": f"{COMMON_OCTAVE_PREFIX}integW_sine",
                        "integW_minus_sin": f"{COMMON_OCTAVE_PREFIX}integW_minus_sine",
                        "integW_zero": f"{COMMON_OCTAVE_PREFIX}integW_zero",
                    },
                    digital_marker=f"{COMMON_OCTAVE_PREFIX}ON",
                ),
            }
        )
        pb_config.v1_beta.waveforms.update(
            {
                f"{COMMON_OCTAVE_PREFIX}readout_wf": QuaConfigWaveformDec(
                    constant=QuaConfigConstantWaveformDec(sample=calibration_amp)
                ),
                f"{COMMON_OCTAVE_PREFIX}zero_wf": QuaConfigWaveformDec(
                    constant=QuaConfigConstantWaveformDec(sample=0.0)
                ),
                f"{COMMON_OCTAVE_PREFIX}DC_offset_wf": QuaConfigWaveformDec(
                    constant=QuaConfigConstantWaveformDec(sample=offset_amp)
                ),
            }
        )
        pb_config.v1_beta.digital_waveforms.update(
            {
                f"{COMMON_OCTAVE_PREFIX}ON": QuaConfigDigitalWaveformDec(
                    samples=[QuaConfigDigitalWaveformSample(value=True, length=0)]
                ),
                f"{COMMON_OCTAVE_PREFIX}OFF": QuaConfigDigitalWaveformDec(
                    samples=[QuaConfigDigitalWaveformSample(value=False, length=0)]
                ),
            }
        )
        n_samples = integration_length // 4
        pb_config.v1_beta.integration_weights.update(
            {
                f"{COMMON_OCTAVE_PREFIX}integW_cosine": QuaConfigIntegrationWeightDec(
                    cosine=build_iw_sample([weight_amplitude] * n_samples),
                    sine=build_iw_sample([0.0] * n_samples),
                ),
                f"{COMMON_OCTAVE_PREFIX}integW_sine": QuaConfigIntegrationWeightDec(
                    cosine=build_iw_sample([0.0] * n_samples),
                    sine=build_iw_sample([weight_amplitude] * n_samples),
                ),
                f"{COMMON_OCTAVE_PREFIX}integW_minus_sine": QuaConfigIntegrationWeightDec(
                    cosine=build_iw_sample([0.0] * n_samples),
                    sine=build_iw_sample([-weight_amplitude] * n_samples),
                ),
                f"{COMMON_OCTAVE_PREFIX}integW_zero": QuaConfigIntegrationWeightDec(
                    cosine=build_iw_sample([0.0] * n_samples),
                    sine=build_iw_sample([0.0] * n_samples),
                ),
            }
        )
        pb_config.v1_beta.mixers.update(
            {
                f"{COMMON_OCTAVE_PREFIX}dummy_mixer": QuaConfigMixerDec(
                    correction=[
                        QuaConfigCorrectionEntry(
                            frequency=abs(int(if_frequency)),
                            frequency_double=[0.0, abs(float(if_frequency))][frequency_idx],
                            lo_frequency=int(dummy_lo_frequency),
                            lo_frequency_double=[0.0, float(dummy_lo_frequency)][frequency_idx],
                            correction=QuaConfigMatrix(1.0, 0.0, 0.0, 1.0),
                            frequency_negative=if_frequency < 0,
                        )
                        for if_frequency in (
                            dummy_if_frequency,
                            dummy_if_frequency - dummy_down_mixer_offset,
                            -dummy_down_mixer_offset,
                            -dummy_if_frequency - dummy_down_mixer_offset,
                        )
                    ]
                )
            }
        )

    return pb_config


def _create_lo_to_if_mapping(lo_if_frequencies_tuple_list: List[Tuple[int, int]]) -> Dict[float, Tuple[float, ...]]:
    lo_to_if_mapping: Dict[float, Tuple[float, ...]] = defaultdict(tuple)
    for lo_freq, if_freq in lo_if_frequencies_tuple_list:
        lo_to_if_mapping[float(lo_freq)] += (if_freq,)
    return dict(lo_to_if_mapping)


@lru_cache(maxsize=None)
def _cached_get_device(
    connection_info: ConnectionDetails,
    loop_backs: Tuple[Tuple[OctaveLOSource, OctaveOutput], ...],
    octave_name: str,
) -> Octave:
    standardized_loop_backs = {input_port: output_port for input_port, output_port in loop_backs}
    return Octave(
        host=connection_info.host,
        port=connection_info.port,
        port_mapping=standardized_loop_backs,
        octave_name=octave_name,
        connection_headers=connection_info.headers,
    )


def get_device(
    connection_info: ConnectionDetails,
    loop_backs: Dict[OctaveLOSource, OctaveOutput],
    octave_name: str,
    fan: Any = None,
) -> Octave:
    client = _cached_get_device(
        connection_info,
        loop_backs=tuple(sorted(loop_backs.items(), key=lambda u: (u[0].name, u[1].name))),
        octave_name=octave_name,
    )
    if fan is not None:
        client._set_fan(fan)
    return client
