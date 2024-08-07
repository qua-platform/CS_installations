import logging
from typing import TYPE_CHECKING, Tuple, Union, Optional, Sequence

from octave_sdk.octave import RFOutput
from octave_sdk import RFOutputMode, OctaveLOSource

from qm.type_hinting import Number
from qm.api.frontend_api import FrontendApi
from qm.elements.element_inputs import MixInputs
from qm.grpc.qua_config import QuaConfigMixInputs
from qm.type_hinting.general import NumpySupportedFloat

if TYPE_CHECKING:
    from qm.octave import CalibrationDB

logger = logging.getLogger(__name__)


class UpconvertedInput(MixInputs):
    def __init__(
        self,
        name: str,
        config: QuaConfigMixInputs,
        frontend_api: FrontendApi,
        machine_id: str,
        client: RFOutput,
        port: Tuple[str, int],
        gain: Optional[float],
        calibration_db: Optional["CalibrationDB"] = None,
        use_input_attenuators: bool = False,
    ):
        super().__init__(name, config, frontend_api, machine_id)
        self._client = client
        self._lo_frequency = config.lo_frequency_double if config.lo_frequency_double else float(config.lo_frequency)
        self._port = port
        self._gain = gain
        self._calibration_db = calibration_db
        self._use_input_attenuators = use_input_attenuators

    @property
    def port(self) -> Tuple[str, int]:
        return self._port

    @property
    def lo_source(self) -> OctaveLOSource:
        return self._client.get_lo_source()

    @property
    def gain(self) -> Optional[float]:
        return self._gain

    def set_lo_frequency(self, lo_frequency: float, set_source: bool = True) -> None:
        """
        Sets the LO frequency of the synthesizer associated to element

        :param lo_frequency:
        :param set_source:
        """
        # if self.lo_source != OctaveLOSource.Internal and self.lo_source not in self._client._port_mapping:
        #     raise SetFrequencyException(f"Cannot set frequency to an external lo source {self.lo_source.name}")

        lo_source = self.lo_source
        if set_source:
            self._client.set_lo_source(lo_source, ignore_shared_errors=True)

        self._client.set_lo_frequency(lo_source, lo_frequency)
        self.inform_element_about_lo_frequency(lo_frequency)

    def inform_element_about_lo_frequency(self, lo_frequency: float) -> None:
        self._set_config_lo_frequency(lo_frequency)
        if self._gain is not None:
            self._client.set_gain(self._gain, self.lo_frequency, self._use_input_attenuators)

    def set_use_input_attenuators(self, use_input_attenuators: bool) -> None:
        """
        Allow using the 10dB attenuators in front of the up converter IQ ports (or not).

        :param use_input_attenuators: False means: never use the attenuators. True means: used it based on the desired gain.
        """
        self._use_input_attenuators = use_input_attenuators
        if self._gain is not None:
            self._client.set_gain(self._gain, self.lo_frequency, self._use_input_attenuators)
        else:
            logger.warning("Gain is not set, so the input attenuators cannot be set.")

    def set_lo_source(self, lo_port: OctaveLOSource) -> None:
        """
        Sets the source of LO going to the upconverter associated with element.
        :param lo_port:
        """
        self._client.set_lo_source(lo_port, ignore_shared_errors=True)

    def set_rf_output_mode(self, switch_mode: RFOutputMode) -> None:
        """
        Configures the output switch of the upconverter associated to element.
        switch_mode can be either: 'always_on', 'always_off', 'normal' or 'inverted'
        When in 'normal' mode a high trigger will turn the switch on and a low trigger will turn it off
        When in 'inverted' mode a high trigger will turn the switch off and a low trigger will turn it on
        When in 'always_on' the switch will be permanently on. When in 'always_off' mode the switch will
        be permanently off.

        :param switch_mode:
        """
        self._client.set_output(switch_mode)

    def set_rf_output_gain(self, gain_in_db: float) -> None:
        """
        Sets the RF output gain for the up-converter associated with the element.
        RF_gain is in steps of 0.5dB from -20 to +24 and is referring
        to the maximum OPX output power of 4dBm (=0.5V pk-pk) So for a value of -24
        for example, an IF signal coming from the OPX at max power (4dBm) will be
        upconverted and come out of Octave at -20dBm

        :param gain_in_db:
        """
        # a. use value custom set in qm.octave.update_external
        # b. use value from config
        if not -20 <= gain_in_db <= 20:
            raise ValueError(f"Gain must be between -20 and 20 dB, got {gain_in_db}")
        self._client.set_gain(gain_in_db, self.lo_frequency, self._use_input_attenuators)
        self._gain = gain_in_db


class UpconvertedInputNewApi(UpconvertedInput):
    def __init__(
        self,
        name: str,
        config: QuaConfigMixInputs,
        client: RFOutput,
        port: Tuple[str, int],
        gain: Optional[float],
        calibration_db: Optional["CalibrationDB"] = None,
        use_input_attenuators: bool = False,
    ):
        super().__init__(
            name,
            config,
            frontend_api=None,  # type: ignore[arg-type]
            machine_id=None,  # type: ignore[arg-type]
            client=client,
            port=port,
            gain=gain,
            calibration_db=calibration_db,
            use_input_attenuators=use_input_attenuators,
        )

    def set_output_dc_offset(self, i_offset: Optional[float] = None, q_offset: Optional[float] = None) -> None:
        raise NotImplementedError

    def set_output_filter(
        self,
        input_name: str,
        feedforward: Union[Sequence[NumpySupportedFloat], None],
        feedback: Union[Sequence[NumpySupportedFloat], None],
    ) -> None:
        raise NotImplementedError

    def set_mixer_correction(
        self,
        intermediate_frequency: Number,
        lo_frequency: Number,
        values: Tuple[float, float, float, float],
    ) -> None:
        raise NotImplementedError
