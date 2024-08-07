from typing import Dict, List, Tuple, Optional

import betterproto
from octave_sdk.octave import RFInput
from octave_sdk import Octave, OctaveOutput, OctaveLOSource

from qm.api.frontend_api import FrontendApi
from qm.elements.element_inputs import MixInputs
from qm.utils.config_utils import get_fem_config
from qm.octave import CalibrationDB, QmOctaveConfig
from qm.api.models.capabilities import ServerCapabilities
from qm.octave.calibration_db import convert_to_correction
from qm.octave.octave_manager import logger, get_device, get_loopbacks_from_pb
from qm.elements.up_converted_input import UpconvertedInput, UpconvertedInputNewApi
from qm.exceptions import OctaveCableSwapError, OctaveConnectionError, ElementUpconverterDeclarationError
from qm.grpc.qua_config import (
    QuaConfig,
    QuaConfigMatrix,
    QuaConfigElementDec,
    QuaConfigCorrectionEntry,
    QuaConfigGeneralPortReference,
)

OptionalOctaveInputPort = Optional[Tuple[str, int]]


class OctavesContainer:
    def __init__(self, pb_config: QuaConfig, octave_config: Optional[QmOctaveConfig] = None):
        self._pb_config = pb_config
        self._octave_config = octave_config or QmOctaveConfig()

        _qua_config_opx_to_octave_i = {}
        _qua_config_opx_to_octave_q = {}
        for octave_name, octave_qua_config in self._pb_config.v1_beta.octaves.items():
            for rf_idx, rf_config in octave_qua_config.rf_outputs.items():
                i_connection, q_connection = rf_config.i_connection, rf_config.q_connection
                _qua_config_opx_to_octave_i[(i_connection.controller, i_connection.fem, i_connection.number)] = (
                    octave_name,
                    rf_idx,
                )
                _qua_config_opx_to_octave_q[(q_connection.controller, q_connection.fem, q_connection.number)] = (
                    octave_name,
                    rf_idx,
                )
        self._qua_config_opx_to_octave_i = _qua_config_opx_to_octave_i
        self._qua_config_opx_to_octave_q = _qua_config_opx_to_octave_q

    def get_upconverter_port_ref(self, element_config: QuaConfigElementDec) -> OptionalOctaveInputPort:
        if element_config.rf_inputs:
            rf_input = list(element_config.rf_inputs.values())[0]
            return rf_input.device_name, rf_input.port
        if not betterproto.serialized_on_wire(element_config.mix_inputs):
            return None

        element_i_port, element_q_port = element_config.mix_inputs.i, element_config.mix_inputs.q

        key_i = (element_i_port.controller, element_i_port.fem, element_i_port.number)
        key_q = (element_q_port.controller, element_q_port.fem, element_q_port.number)
        i_conn = self._qua_config_opx_to_octave_i.get(key_i)
        q_conn = self._qua_config_opx_to_octave_q.get(key_q)
        if i_conn is None and q_conn is None:
            if (self._qua_config_opx_to_octave_i.get(key_q) is not None) or (
                self._qua_config_opx_to_octave_q.get(key_i) is not None
            ):
                raise OctaveCableSwapError()

            return self._octave_config.get_octave_input_port(
                (element_i_port.controller, element_i_port.fem, element_i_port.number),
                (element_q_port.controller, element_q_port.fem, element_q_port.number),
            )
        if i_conn != q_conn:
            raise ElementUpconverterDeclarationError()
        return i_conn

    def _get_downconverter_client(self, outputs: Dict[str, QuaConfigGeneralPortReference]) -> Optional[RFInput]:
        if not outputs:
            return None
        for _, port_ref in outputs.items():
            if port_ref.device_name in self._pb_config.v1_beta.octaves:
                client = self._get_octave_client(port_ref.device_name)
                return client.rf_inputs[port_ref.port]
        raise OctaveConnectionError("No downconverter found for the given outputs.")

    def _get_loopbacks(self, octave_name: str) -> Dict[OctaveLOSource, OctaveOutput]:
        if octave_name in self._pb_config.v1_beta.octaves:
            pb_loopbacks = self._pb_config.v1_beta.octaves[octave_name].loopbacks
            return get_loopbacks_from_pb(pb_loopbacks, octave_name)
        return self._octave_config.get_lo_loopbacks_by_octave(octave_name)

    def create_mix_inputs(
        self,
        element_config: QuaConfigElementDec,
        name: str,
        frontend_api: FrontendApi,
        machine_id: str,
    ) -> MixInputs:
        port = self.get_upconverter_port_ref(element_config)
        if port is None:
            return MixInputs(name, element_config.mix_inputs, frontend_api, machine_id)

        octave_name, octave_port = port
        client = self._get_octave_client(octave_name)

        return UpconvertedInput(
            name,
            element_config.mix_inputs,
            frontend_api,
            machine_id,
            client=client.rf_outputs[octave_port],
            port=port,
            calibration_db=self._octave_config.calibration_db,
            gain=self._get_octave_gain(octave_name, octave_port),
            use_input_attenuators=self._get_octave_input_attenuators(octave_name, octave_port),
        )

    def create_new_api_upconverted_input(
        self,
        element_config: QuaConfigElementDec,
        name: str,
    ) -> Optional[UpconvertedInputNewApi]:
        port = self.get_upconverter_port_ref(element_config)
        if port is None:
            return None

        octave_name, octave_port = port
        client = self._get_octave_client(octave_name)
        gain = self._get_octave_gain(octave_name, octave_port)

        return UpconvertedInputNewApi(
            name,
            element_config.mix_inputs,
            client=client.rf_outputs[octave_port],
            port=port,
            calibration_db=self._octave_config.calibration_db,
            gain=gain,
            use_input_attenuators=self._get_octave_input_attenuators(octave_name, octave_port),
        )

    def _get_octave_gain(self, octave_name: str, port: int) -> Optional[float]:
        try:
            return self._pb_config.v1_beta.octaves[octave_name].rf_outputs[port].gain
        except KeyError:
            logger.warning(
                "No gain was specified. Setting gain to None. "
                "Please configure all the ports' gain values in the qua configuration"
            )
            return None

    def _get_octave_input_attenuators(self, octave_name: str, port: int) -> bool:
        try:
            return self._pb_config.v1_beta.octaves[octave_name].rf_outputs[port].input_attenuators
        except KeyError:
            return False

    def get_downconverter(self, outputs: Dict[str, QuaConfigGeneralPortReference]) -> Optional[RFInput]:
        return self._get_downconverter_client(outputs)

    def _get_octave_client(self, device_name: str) -> Octave:
        device_connection_info = self._octave_config.devices[device_name]
        loopbacks = self._get_loopbacks(device_name)
        return get_device(
            device_connection_info,
            loop_backs=loopbacks,
            octave_name=device_name,
            fan=self._octave_config.fan,
        )


def load_config_from_calibration_db(
    pb_config: QuaConfig, calibration_db: CalibrationDB, octave_config: QmOctaveConfig, capabilities: ServerCapabilities
) -> QuaConfig:
    octaves_container = OctavesContainer(pb_config, octave_config)

    logger.debug("Loading mixer calibration data onto the config")

    for element_name, element in pb_config.v1_beta.elements.items():
        if not betterproto.serialized_on_wire(element.mix_inputs):
            continue
        mix_inputs = element.mix_inputs

        lo_freq = mix_inputs.lo_frequency or mix_inputs.lo_frequency_double
        if not lo_freq:
            logger.debug(f"Element '{element_name}' has no LO frequency specified")
            continue

        octave_channel = octaves_container.get_upconverter_port_ref(element)
        if octave_channel is None:
            logger.debug(f"Element '{element_name}' is not connected to Octave")
            continue

        try:
            output_gain = pb_config.v1_beta.octaves[octave_channel[0]].rf_outputs[octave_channel[1]].gain
        except KeyError:
            logger.warning(
                "No gain was specified. Setting gain to None. "
                "Please configure all the ports' gain values in the qua configuration"
            )
            output_gain = None

        lo_cal = calibration_db.get_lo_cal(octave_channel, lo_freq, output_gain)
        if lo_cal is None:
            logger.debug(
                f"the calibration db has no LO cal for element '{element_name}' (lo_freq = {lo_freq / 1e9:0.3f} GHz)"
            )
            continue

        i_port, q_port = mix_inputs.i, mix_inputs.q
        i_controller_config = get_fem_config(pb_config, i_port)
        i_controller_config.analog_outputs[i_port.number].offset = lo_cal.i0
        q_controller_config = get_fem_config(pb_config, q_port)
        q_controller_config.analog_outputs[q_port.number].offset = lo_cal.q0

        if i_port.controller in pb_config.v1_beta.controllers:
            pb_config.v1_beta.controllers[i_port.controller].analog_outputs[i_port.number].offset = lo_cal.i0
        if q_port.controller in pb_config.v1_beta.controllers:
            pb_config.v1_beta.controllers[q_port.controller].analog_outputs[q_port.number].offset = lo_cal.q0

        # Now we go over all the IF frequencies we find and set them. Not sure
        # when an IF frequency different from the element's 'intermediate_frequency'
        # will be used. Maybe when static frequency change happens, the gateway takes
        # the correction from this updated config.
        if_calibrations_for_curr_lo = calibration_db.get_all_if_cal_for_lo(octave_channel, lo_freq, output_gain)

        # We are expected to put all these calibrations in the element's mixer
        curr_mixer = mix_inputs.mixer

        if curr_mixer not in pb_config.v1_beta.mixers:
            logger.debug(f"Element '{element_name}' is using mixer '{curr_mixer}' which is not found.")
            continue

        old_if_cals = pb_config.v1_beta.mixers[curr_mixer]
        new_if_cals: List[QuaConfigCorrectionEntry] = []
        frequency_idx = int(capabilities.supports_double_frequency)  # This is to shorten many if-else in the code using
        # a trinary expression
        for if_freq, if_cal in if_calibrations_for_curr_lo.items():
            curr_new_calibration = QuaConfigCorrectionEntry(
                frequency=int(abs(if_freq)),
                frequency_double=[0.0, float(abs(if_freq))][frequency_idx],
                lo_frequency=int(lo_freq),
                lo_frequency_double=[0.0, float(lo_freq)][frequency_idx],
                correction=QuaConfigMatrix(*convert_to_correction(if_cal.gain, if_cal.phase)),
                frequency_negative=if_freq < 0,
            )
            new_if_cals.append(curr_new_calibration)

        for old_if_cal in old_if_cals.correction:
            if lo_freq not in {old_if_cal.lo_frequency, old_if_cal.lo_frequency_double}:
                continue

            sign = (-1) ** old_if_cal.frequency_negative
            old_if_freq = (old_if_cal.frequency or old_if_cal.frequency_double) * sign
            if old_if_freq in if_calibrations_for_curr_lo:
                continue

            new_if_cals.append(old_if_cal)
            logger.debug(
                f"Could not find calibration value for LO frequency {lo_freq} and intermediate_frequency {old_if_freq}"
            )

        pb_config.v1_beta.mixers[curr_mixer].correction = new_if_cals
    return pb_config
