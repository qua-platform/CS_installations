import logging
import warnings
from collections import defaultdict
from abc import ABCMeta, abstractmethod
from typing import TYPE_CHECKING, Any, Dict, List, Tuple, Union, Generic, TypeVar, Optional, ContextManager

from octave_sdk.octave import ClockInfo
from octave_sdk import IFMode, ClockType, RFOutputMode, ClockFrequency, OctaveLOSource, RFInputLOSource

from qm.elements.element import Element
from qm.grpc.qua_config import QuaConfigMixInputs
from qm.elements.element_outputs import DownconvertedOutput
from qm.elements.up_converted_input import UpconvertedInput
from qm.octave.octave_manager import ClockMode, OctaveManager
from qm.octave.calibration_db import IFCalibrationDBSchema, LOCalibrationDBSchema
from qm.type_hinting.config_types import DictQuaConfig, MixerConfigType, OPX1000ControllerConfigType
from qm.octave.octave_mixer_calibration import (
    DeprecatedCalibrationResult,
    LOFrequencyCalibrationResult,
    convert_to_old_calibration_result,
)

if TYPE_CHECKING:
    from qm.api.v2.qm_api import QmApi
    from qm.api.v2.job_api import JobApi
    from qm.quantum_machine import QuantumMachine
    from qm.jobs.running_qm_job import RunningQmJob

logger = logging.getLogger(__name__)


class ElementHasNoOctaveError(Exception):
    def __init__(self, name: str):
        self._name = name

    def __str__(self) -> str:
        return f"Element {self._name} has no octave connected to it."


class NoCalibrationDbAttachedError(Exception):
    def __init__(self, name: str):
        self._name = name

    def __str__(self) -> str:
        return f"No calibration database attached to element {self._name}"


class NoCalibrationParamsError(Exception):
    def __init__(self, name: str):
        self._name = name

    def __str__(self) -> str:
        return f"No calibration parameters found for element {self._name}"


QmInstT = TypeVar("QmInstT", "QuantumMachine", "QmApi")
JobInstT = TypeVar("JobInstT", "RunningQmJob", "JobApi")


class QmOctaveBase(Generic[QmInstT, JobInstT], metaclass=ABCMeta):
    def __init__(self, qm: QmInstT, octave_manager: OctaveManager):
        self._qm: QmInstT = qm
        self._octave_manager = octave_manager

    def _get_upconverted_input(self, name: str) -> UpconvertedInput:
        instance = self._qm._elements[name]
        if not isinstance(instance.input, UpconvertedInput):
            raise ElementHasNoOctaveError(name)
        return instance.input

    def _get_downconverted_output(self, name: str) -> DownconvertedOutput:
        instance = self._qm._elements[name]
        if not isinstance(instance.output, DownconvertedOutput):
            raise ElementHasNoOctaveError(name)
        return instance.output

    def start_batch_mode(self) -> None:
        self._octave_manager.start_batch_mode()

    def end_batch_mode(self) -> None:
        self._octave_manager.end_batch_mode()

    def batch_mode(self) -> ContextManager[None]:
        return self._octave_manager.batch_mode()

    def set_qua_element_octave_rf_in_port(self, element: str, octave_name: str, rf_input_index: int) -> None:
        """Sets the octave down conversion port for the given element.

        Args:
            element (str): The name of the element
            octave_name (str): The octave name
            rf_input_index (RFInputRFSource): input index - can be 1 or 2
        """
        inst = self._qm._elements[element]
        client = self._octave_manager.get_client(octave_name)
        rf_input_client = client.rf_inputs[rf_input_index]
        inst.output = DownconvertedOutput(rf_input_client)

    def load_lo_frequency_from_config(self, elements: Union[List[str], str]) -> None:
        """Loads into the octave synthesizers the LO frequencies specified for elements
        in the element list

        Args:
            elements: A list of elements to load LO frequencies for from the configuration
        """
        warnings.warn(
            "lo_frequency is now set directly from config when a QuantumMachine is created, no need to do it directly. "
            "If you want, you can run over the elements and do set_frequency.",
            category=DeprecationWarning,
            stacklevel=2,
        )

    def set_lo_frequency(self, element: str, lo_frequency: float, set_source: bool = True) -> None:
        """Sets the LO frequency of the synthesizer associated with the given element. Will not change the synthesizer if set_source = False

        Args:
            element (str): The name of the element
            lo_frequency (float): The LO frequency
            set_source (Boolean): Set the synthesizer (True) or just
                update the local database (False)
        """
        input_inst = self._get_upconverted_input(element)
        input_inst.set_lo_frequency(lo_frequency, set_source)

    def update_external_lo_frequency(
        self,
        element: str,
        lo_frequency: float,
    ) -> None:
        """Updates the local database on the external LO frequency (provided by the user)
        associated with element

        Args:
            element (str): The name of the element
            lo_frequency (float): The LO frequency
        """
        input_inst = self._get_upconverted_input(element)
        input_inst.inform_element_about_lo_frequency(lo_frequency)

    def set_lo_source(self, element: str, lo_port: OctaveLOSource) -> None:
        """Associate the given LO source with the given element. Always be sure the given LO source is internally connected to the element according to the Octave Block Diagram in the documentation

        Args:
            element (str): The name of the element
            lo_port (OctaveLOSource): One of the allowed sources
                according the internal connectivity
        """
        input_inst = self._get_upconverted_input(element)
        input_inst.set_lo_source(lo_port)

    def set_rf_output_mode(self, element: str, switch_mode: RFOutputMode) -> None:
        """Configures the output switch of the upconverter associated to element.
        switch_mode can be either: 'on', 'off', 'trig_normal' or 'trig_inverse':

        - 'trig_normal' mode a high trigger will turn the switch on and a low trigger will turn it off
        - 'trig_inverse' mode a high trigger will turn the switch off and a low trigger will turn it on
        - 'on' the switch will be permanently on.
        - 'off' mode the switch will be permanently off.

        Args:
            element (str): The name of the element
            switch_mode (RFOutputMode): switch mode according to the
                allowed states
        """
        input_inst = self._get_upconverted_input(element)
        input_inst.set_rf_output_mode(switch_mode)

    def set_rf_output_gain(self, element: str, gain_in_db: float) -> None:
        """Sets the RF output gain for the up-converter associated with the element.
        RF_gain is in steps of 0.5dB from -20 to +20 and is referring
        to the maximum OPX output power of 4dBm (=0.5V pk-pk) So for a value of -20
        for example, an IF signal coming from the OPX at max power (4dBm) will be
        upconverted and come out of Octave at -16dBm

        Args:
            element (str): The name of the element
            gain_in_db (float): The RF output gain in dB
        """
        # a. use value custom set in qm.octave.update_external
        # b. use value from config
        input_inst = self._get_upconverted_input(element)
        input_inst.set_rf_output_gain(gain_in_db)

    def set_downconversion(
        self,
        element: str,
        lo_source: Optional[RFInputLOSource] = None,
        lo_frequency: Optional[float] = None,
        if_mode_i: IFMode = IFMode.direct,
        if_mode_q: IFMode = IFMode.direct,
        disable_warning: bool = False,
    ) -> None:
        """Sets the LO source and frequency for the downconverter of a given element. Sets also the mode of the I and Q lines after downconversion

        - The LO source will be the one associated with the element's upconversion.
        - If only the element is given, the LO source and frequency for downconversion will be the same as those set for the upconversion of the element.
        - IFMode sets the I/Q lines mode after downconversion and can be:
            - direct: bypass
            - envelope: goes through an envelope detector for advanced applications
            - Mixer: goes through a low frequency mixer for advanced applications

        Args:
            element (str): The name of the element
            lo_source (RFInputLOSource): LO source according to the allowed LO sources
            lo_frequency (float): The LO frequency
            if_mode_i (IFMode): Sets the I channel mode of the downconverter
            if_mode_q (IFMode): Sets the Q channel mode of the downconverter
            disable_warning (Boolean): Disable warnings about non-matching LO sources and elements if True
        """
        if lo_source is None:
            up_conv = self._get_upconverted_input(element)
            lo_source = up_conv.lo_source
        inst = self._get_downconverted_output(element)
        inst.set_downconversion(lo_source, lo_frequency, if_mode_i, if_mode_q)

    def set_use_input_attenuators(self, element: str, use_input_attenuators: bool) -> None:
        """Sets the use of IQ attenuators for the downconverter associated with the element.

        Args:
            element (str): The name of the element
            use_iq_attenuators (bool): True to use IQ attenuators, False otherwise
        """
        input_inst = self._get_upconverted_input(element)
        input_inst.set_use_input_attenuators(use_input_attenuators)

    def calibrate_element(
        self,
        element: str,
        lo_if_frequencies_tuple_list: Optional[List[Tuple[int, int]]] = None,
        save_to_db: bool = True,
        offset_frequency: float = 7e6,
        **kwargs: Any,
    ) -> Dict[Tuple[int, int], DeprecatedCalibrationResult]:
        """Calibrate the up converter associated with an element for the given LO & IF frequencies.

        - Frequencies are given as a list of tuples : [(LO,IF1)(LO,IF2)...]
        - The function need to be run for each LO frequency and element separately

        - If close_open_quantum_machines is set to True one must open a new quantum machine after calibration ends
        Args:
            close_open_quantum_machines (bool): If true (default) all
                running QMs will be closed for the calibration.
                Otherwise, calibration might fail if there are not
                enough resources for the calibration
            element (str): The name of the element for calibration
            lo_if_frequencies_tuple_list (list): a list of tuples that
                consists of all the (LO,IF) pairs for calibration
            save_to_db (boolean): If true (default), The calibration
                parameters will be saved to the calibration database
        Calibrate the mixer associated with an element for the given LO & IF frequencies.
        """
        warnings.warn(
            "Calibrate element was moved to the QuantumMachine instance, please use it from there", DeprecationWarning
        )

        if lo_if_frequencies_tuple_list is not None:
            lo_if_dict_tmp: Dict[float, Tuple[float, ...]] = defaultdict(tuple)
            for _lo, _if in lo_if_frequencies_tuple_list:
                lo_if_dict_tmp[float(_lo)] += (_if,)
            lo_if_dict = dict(lo_if_dict_tmp)
        else:
            lo_if_dict = None

        calibration_result = self._qm.calibrate_element(element, lo_if_dict, save_to_db)

        return convert_to_old_calibration_result(calibration_result, self._get_upconverted_input(element).mixer)

    def set_clock(
        self,
        octave_name: str,
        clock_type: Optional[ClockType] = None,
        frequency: Optional[ClockFrequency] = None,
        clock_mode: Optional[ClockMode] = None,
    ) -> None:
        """This function sets the octave clock type - internal, external or buffered.
        It can also set the clock frequency - 10, 100 or 1000 MHz

        - Internal can only be 10 MHz
        - External can be 10, 100, or 1000 MHz
        - Buffered and External behave the same when using 1000 MHz clock
        - ClockType & ClockFrequency will be deprecated soon, users should use clock_mode: ClockMode instead

        Args:
            octave_name (str): The octave name to set clock for
            clock_type (ClockType): clock type according to ClockType
            frequency (ClockFrequency): Clock frequency according to ClockFrequency
            clock_mode (ClockMode): Clock mode according to ClockMode
        """
        self._octave_manager.set_clock(octave_name, clock_type, frequency, clock_mode)

    def get_clock(self, octave_name: str) -> ClockInfo:
        """Gets the clock info for a given octave name

        Args:
            octave_name (str): The octave name to get clock for
        :returns ClockInfo: Info about the clock as an object
        """
        return self._octave_manager.get_clock(octave_name)

    @staticmethod
    def _fetch_calibrations_from_db(
        qe: Element[QuaConfigMixInputs],
    ) -> Tuple[LOCalibrationDBSchema, IFCalibrationDBSchema]:
        assert isinstance(qe.input, UpconvertedInput)
        if qe.input._calibration_db is None:
            logger.warning(f"No calibration DB is attached for element {qe.name}, not changing anything.")
            raise NoCalibrationDbAttachedError(qe.name)
        db = qe.input._calibration_db

        lo_cal = db.get_lo_cal(qe.input.port, lo_freq=qe.input.lo_frequency, gain=qe.input.gain)
        if_cal = db.get_if_cal(
            qe.input.port, lo_freq=qe.input.lo_frequency, gain=qe.input.gain, if_freq=qe.intermediate_frequency
        )
        if if_cal is None or lo_cal is None:
            raise NoCalibrationParamsError(qe.name)
        return lo_cal, if_cal

    def set_element_parameters_from_calibration_db(self, element: str, running_job: Optional[JobInstT] = None) -> None:
        """Apply correction parameters to an element from the calibration database. The parameters will be selected
        according to the current LO and IF frequencies in the configuration. Therefore, If used when sweeping the LO,
        it is required to first set the new LO freq using qm.octave.set_lo_frequency() before updating the calibration
        parameters.

        Args:
            element (str): The name of the element for setting the calibration parameters
            running_job: Optional. If given, will update the element's parameters of the given running job
        """
        qe = self._qm._elements[element]
        assert isinstance(qe.input, UpconvertedInput)
        try:
            lo_cal, if_cal = self._fetch_calibrations_from_db(qe)
        except (NoCalibrationParamsError, NoCalibrationDbAttachedError) as err:
            logger.warning(f"Cannot change element params due to the following error: {err}")
            return

        self._update_element_parameters(qe, lo_cal, if_cal)

        if running_job:
            self._set_running_job_parameters(running_job, element, lo_cal, if_cal)

    @abstractmethod
    def _update_element_parameters(
        self, qe: Element[QuaConfigMixInputs], lo_cal: LOCalibrationDBSchema, if_cal: IFCalibrationDBSchema
    ) -> None:
        pass

    @abstractmethod
    def _set_running_job_parameters(
        self,
        job: JobInstT,
        element: str,
        lo_cal: LOCalibrationDBSchema,
        if_cal: IFCalibrationDBSchema,
    ) -> None:
        pass


class QmOctave(QmOctaveBase["QuantumMachine", "RunningQmJob"]):
    def _update_element_parameters(
        self, qe: Element[QuaConfigMixInputs], lo_cal: LOCalibrationDBSchema, if_cal: IFCalibrationDBSchema
    ) -> None:
        assert isinstance(qe.input, UpconvertedInput)
        qe.input.set_output_dc_offset(i_offset=lo_cal.i0, q_offset=lo_cal.q0)
        qe.input.set_mixer_correction(
            intermediate_frequency=qe.intermediate_frequency,
            lo_frequency=qe.input.lo_frequency,
            values=if_cal.correction,
        )

    def _set_running_job_parameters(
        self, job: "RunningQmJob", element: str, lo_cal: LOCalibrationDBSchema, if_cal: IFCalibrationDBSchema
    ) -> None:
        job.set_element_correction(element, if_cal.correction)


class QmOctaveForNewApi(QmOctaveBase["QmApi", "JobApi"]):
    def _update_element_parameters(
        self, qe: Element[QuaConfigMixInputs], lo_cal: LOCalibrationDBSchema, if_cal: IFCalibrationDBSchema
    ) -> None:
        assert isinstance(qe.input, UpconvertedInput)
        update = create_dc_offset_octave_update(qe.input, lo_cal)
        update["mixers"] = {
            qe.input.mixer: [
                create_mixer_correction(qe.intermediate_frequency, qe.input.lo_frequency, if_cal.correction)
            ]
        }
        self._qm.update_config(update)

    def _set_running_job_parameters(
        self, job: "JobApi", element: str, lo_cal: LOCalibrationDBSchema, if_cal: IFCalibrationDBSchema
    ) -> None:
        job.set_output_dc_offset_by_element(element, ("I", "Q"), (lo_cal.i0, lo_cal.q0))
        job.set_element_correction(element, if_cal.correction)


def create_dc_offset_octave_update(
    qe_input: UpconvertedInput, lo_cal: Union[LOCalibrationDBSchema, LOFrequencyCalibrationResult]
) -> DictQuaConfig:
    con_i, fem_i, port_i = qe_input.i_port.controller, qe_input.i_port.fem, qe_input.i_port.number
    con_q, fem_q, port_q = qe_input.q_port.controller, qe_input.q_port.fem, qe_input.q_port.number
    controllers: Dict[str, OPX1000ControllerConfigType] = {con_i: {"fems": {}}, con_q: {"fems": {}}}
    controllers[con_i]["fems"][fem_i] = {"analog_outputs": {}}  # type: ignore[index]
    controllers[con_q]["fems"][fem_q] = {"analog_outputs": {}}  # type: ignore[index]
    controllers[con_i]["fems"][fem_i]["analog_outputs"][port_i] = {"offset": lo_cal.i0}  # type: ignore[index]
    controllers[con_q]["fems"][fem_q]["analog_outputs"][port_q] = {"offset": lo_cal.q0}  # type: ignore[index]
    update: DictQuaConfig = {"version": 1, "controllers": controllers}
    return update


def create_mixer_correction(
    intermediate_frequency: float, lo_frequency: float, correction: Tuple[float, float, float, float]
) -> MixerConfigType:
    return {
        "correction": correction,
        "intermediate_frequency": intermediate_frequency,
        "lo_frequency": lo_frequency,
    }
