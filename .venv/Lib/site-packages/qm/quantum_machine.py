import json
import logging
import warnings
from typing import Any, Dict, List, Tuple, Union, Mapping, Optional, Sequence, cast

from qm.program import Program
from qm.jobs.qm_job import QmJob
from qm.octave import QmOctaveConfig
from qm.persistence import BaseStore
from qm.octave.qm_octave import QmOctave
from qm.utils import deprecation_message
from qm.api.models.devices import Polarity
from qm.api.frontend_api import FrontendApi
from qm.jobs.pending_job import QmPendingJob
from qm.jobs.job_queue_old_api import QmQueue
from qm.jobs.job_queue_mock import QmQueueMock
from qm.jobs.simulated_job import SimulatedJob
from qm.api.simulation_api import SimulationApi
from qm.grpc.frontend import JobExecutionStatus
from qm.jobs.running_qm_job import RunningQmJob
from qm.utils.config_utils import get_fem_config
from qm.octave.octave_manager import OctaveManager
from qm.simulate.interface import SimulationConfig
from qm.api.v2.job_api.job_api import OldJobApiMock
from qm.elements_db import ElementsDB, init_elements
from qm.utils.types_utils import convert_object_type
from qm.program.ConfigBuilder import convert_msg_to_config
from qm.elements.up_converted_input import UpconvertedInput
from qm._QmJobErrors import InvalidDigitalInputPolarityError
from qm.octave._calibration_names import COMMON_OCTAVE_PREFIX
from qm.api.job_manager_api import create_job_manager_from_api
from qm.api.models.capabilities import OPX_FEM_IDX, ServerCapabilities
from qm.api.models.compiler import CompilerOptionArguments, standardize_compiler_params
from qm.type_hinting.config_types import StandardPort, DictQuaConfig, PortReferenceType
from qm.elements.element_inputs import MixInputs, SingleInput, static_set_mixer_correction
from qm.type_hinting.general import Value, Number, PathLike, NumpySupportedFloat, NumpySupportedValue
from qm.octave.octave_mixer_calibration import AutoCalibrationParams, OctaveMixerCalibration, MixerCalibrationResults
from qm.grpc.qua_config import (
    QuaConfig,
    QuaConfigQuaConfigV1,
    QuaConfigPortReference,
    QuaConfigMicrowaveFemDec,
    QuaConfigDigitalInputPortDec,
    QuaConfigDigitalInputPortDecPolarity,
)
from qm.exceptions import (
    QmValueError,
    JobCancelledError,
    ErrorJobStateError,
    FunctionInputError,
    InvalidConfigError,
    AnotherJobIsRunning,
    CantCalibrateElementError,
    UnsupportedCapabilityError,
)

logger = logging.getLogger(__name__)


class QuantumMachine:
    def __init__(
        self,
        machine_id: str,
        pb_config: QuaConfig,
        frontend_api: FrontendApi,
        capabilities: ServerCapabilities,
        store: BaseStore,
        octave_manager: OctaveManager,
        octave_config: Optional[QmOctaveConfig] = None,
    ):
        self._id = machine_id
        self._config = pb_config
        self._frontend = frontend_api

        self._capabilities = capabilities

        self._simulation_api = SimulationApi(self._frontend.connection_details)
        self._job_manager = create_job_manager_from_api(frontend_api)

        self._store = store
        self._queue = QmQueue(
            config=self._config,
            quantum_machine_id=self._id,
            frontend_api=self._frontend,
            capabilities=self._capabilities,
            store=self._store,
        )

        self._elements: ElementsDB = init_elements(
            pb_config, frontend_api, machine_id=machine_id, octave_config=octave_config
        )
        self._octave = QmOctave(self, octave_manager)

    @property
    def _octave_calibration_elements(self) -> ElementsDB:
        return ElementsDB({k: v for k, v in self._elements.items() if k.startswith(COMMON_OCTAVE_PREFIX)})

    @property
    def manager(self) -> None:
        """Returns the Quantum Machines Manager"""
        warnings.warn(
            deprecation_message(
                method="QuantumMachine.manager",
                deprecated_in="1.1.0",
                removed_in="1.2.0",
                details="QuantumMachine no longer has 'manager' property",
            ),
            DeprecationWarning,
            stacklevel=2,
        )
        return None

    @property
    def id(self) -> str:
        return self._id

    @property
    def queue(self) -> Union[QmQueue, QmQueueMock]:
        return self._queue

    @property
    def octave(self) -> QmOctave:
        return self._octave

    def close(self) -> bool:
        """Closes the quantum machine.

        Returns:
            ``True`` if the close request succeeded, raises an exception
            otherwise.
        """
        return self._frontend.close_quantum_machine(self._id)

    def simulate(
        self,
        program: Program,
        simulate: SimulationConfig,
        compiler_options: Optional[CompilerOptionArguments] = None,
        *,
        strict: Optional[bool] = None,
        flags: Optional[List[str]] = None,
    ) -> SimulatedJob:
        """Simulates the outputs of a deterministic QUA program.

        Equivalent to ``execute()`` with ``simulate=SimulationConfig`` (see example).

        Note:
            A simulated job does not support calling QuantumMachine API functions.

        The following example shows a simple execution of the simulator, where the
        associated config object is omitted for brevity.

        Example:
            ```python
            from qm.qua import *
            from qm.simulate import SimulationConfig, QuantumMachinesManager

            qmManager = QuantumMachinesManager()
            qm1 = qmManager.open_qm(config)

            with program() as prog:
                play('pulse1', 'element1')

            job = qm1.simulate(prog, SimulationConfig(duration=100))
            ```

        Args:
            program: A QUA ``program()`` object to execute
            simulate: A ``SimulationConfig`` configuration object
        Returns:
            a ``QmJob`` object (see QM Job API).
        """
        standardized_compiler_options = standardize_compiler_params(compiler_options, strict, flags)
        job = cast(
            SimulatedJob, self.execute(program, simulate=simulate, compiler_options=standardized_compiler_options)
        )
        return job

    def execute(
        self,
        program: Program,
        duration_limit: int = 1000,
        data_limit: int = 20000,
        force_execution: int = False,
        dry_run: int = False,
        simulate: Optional[SimulationConfig] = None,
        compiler_options: Optional[CompilerOptionArguments] = None,
        *,
        strict: Optional[bool] = None,
        flags: Optional[List[str]] = None,
    ) -> RunningQmJob:
        """Executes a program and returns a job object to keep track of execution and get
        results.

        Note:

            Calling execute will halt any currently running program and clear the current
            queue. If you want to add a job to the queue, use qm.queue.add()

        Args:
            program: A QUA ``program()`` object to execute
            duration_limit (int): This parameter is ignored as it is
                obsolete
            data_limit (int): This parameter is ignored as it is
                obsolete
            force_execution (bool): This parameter is ignored as it is
                obsolete
            dry_run (bool): This parameter is ignored as it is obsolete

        Returns:
            A ``QmJob`` object (see QM Job API).
        """
        if not isinstance(program, Program):
            raise Exception("program argument must be of type qm.program.Program")
        if program.metadata.uses_command_timestamps and not self._capabilities.supports_command_timestamps:
            raise UnsupportedCapabilityError("timestamping commands is supported from QOP 2.2 or above")
        if program.metadata.uses_fast_frame_rotation and not self._capabilities.supports_fast_frame_rotation:
            raise UnsupportedCapabilityError("fast frame rotation is supported from QOP 2.2 or above")

        standardized_compiler_options = standardize_compiler_params(compiler_options, strict, flags)

        if simulate is not None:
            job_id, simulated_response_part = self._simulation_api.simulate(
                self._get_pb_config(), program, simulate, standardized_compiler_options
            )
            return SimulatedJob(
                job_id=job_id,
                frontend_api=self._frontend,
                capabilities=self._capabilities,
                store=self._store,
                simulated_response=simulated_response_part,
            )

        self._queue.clear()
        current_running_job = self.get_running_job()
        if current_running_job is not None:
            current_running_job.cancel()
        pending_job = self._queue.add(program, standardized_compiler_options)
        logger.info("Executing program")
        return pending_job.wait_for_execution(timeout=5)

    def compile(
        self,
        program: Program,
        compiler_options: Optional[CompilerOptionArguments] = None,
    ) -> str:
        """Compiles a QUA program to be executed later. The returned `program_id`
        can then be directly added to the queue. For a detailed explanation
        see [Precompile Jobs](../../Guides/features/#precompile-jobs).

        Args:
            program: A QUA program
            compiler_options: Optional arguments for compilation

        Returns:
            a program_id str

        Example:
            ```python
            program_id = qm.compile(program)
            pending_job = qm.queue.add_compiled(program_id)
            job = pending_job.wait_for_execution()
            ```
        """
        if program.metadata.uses_command_timestamps and not self._capabilities.supports_command_timestamps:
            raise UnsupportedCapabilityError("timestamping commands is supported from QOP 2.2 or above")

        if program.metadata.uses_fast_frame_rotation and not self._capabilities.supports_fast_frame_rotation:
            raise UnsupportedCapabilityError("fast frame rotation is supported from QOP 2.2 or above")

        logger.info("Compiling program")

        if compiler_options is None:
            compiler_options = CompilerOptionArguments()
        return self._frontend.compile(self._id, program.qua_program, compiler_options)

    def list_controllers(self) -> Tuple[str, ...]:
        """Gets a list with the defined controllers in this qm

        Returns:
            The names of the controllers configured in this qm
        """
        config = self._get_config_as_object()
        return tuple(config.control_devices) or tuple(config.controllers)

    def set_mixer_correction(
        self,
        mixer: str,
        intermediate_frequency: Number,
        lo_frequency: Number,
        values: Tuple[float, float, float, float],
    ) -> None:
        """Sets the correction matrix for correcting gain and phase imbalances
        of an IQ mixer for the supplied intermediate frequency and LO frequency.

        Args:
            mixer (str): the name of the mixer, as defined in the
                configuration
            intermediate_frequency (Union[int|float]): the intermediate
                frequency for which to apply the correction matrix
            lo_frequency (int): the LO frequency for which to apply the
                correction matrix
            values (tuple):

                tuple is of the form (v00, v01, v10, v11) where
                the matrix is
                | v00 v01 |
                | v10 v11 |

        Note:

            Currently, the OPX does not support multiple mixer calibration entries.
            This function will accept IF & LO frequencies written in the config file,
            and will update the correction matrix for all the elements with the given
            mixer/frequencies combination when the program started.

            It’s not recommended to use this method while a job is running.
            To change the calibration values for a running job,
            use job.set_element_correction
        """
        static_set_mixer_correction(
            self._frontend,
            self._id,
            mixer,
            intermediate_frequency=intermediate_frequency,
            lo_frequency=lo_frequency,
            values=values,
        )

    def calibrate_element(
        self,
        qe: str,
        lo_if_dict: Optional[Mapping[float, Tuple[float, ...]]] = None,
        save_to_db: bool = True,
        params: Optional[AutoCalibrationParams] = None,
    ) -> MixerCalibrationResults:
        """Calibrate the up converters associated with a given element for the given LO & IF frequencies.

        - Frequencies can be given as a dictionary with LO frequency as the key and a list of IF frequencies for every LO
        - If no frequencies are given calibration will occur according to LO & IF declared in the element
        - The function need to be run for each element separately
        - The results are saved to a database for later use
        Args:
            qe (str): The name of the element for calibration
            lo_if_dict ([Mapping[float, Tuple[float, ...]]]): a dictionary with LO frequency as the key and
             a list of IF frequencies for every LO
            save_to_db (bool): If true (default), The calibration
                parameters will be saved to the calibration database
        Calibrate the mixer associated with an element for the given LO & IF frequencies.
        """
        inst = self._elements[qe]
        if not isinstance(inst.input, UpconvertedInput):
            raise CantCalibrateElementError(
                f"Element {qe} has input of type {type(inst.input)} and is not connected to an Octave. "
                f"Hence, it cannot be calibrated."
            )
        if params is None:
            params = AutoCalibrationParams()

        if self.get_running_job():
            raise AnotherJobIsRunning

        if lo_if_dict is None:
            lo_if_dict = {inst.input.lo_frequency: (inst.intermediate_frequency,)}
        client = self._octave._octave_manager._get_client_from_port(inst.input.port)
        res = OctaveMixerCalibration(quantum_machine=self, client=client).calibrate(
            element=inst,
            lo_if_dict=lo_if_dict,
            params=params,
        )

        if save_to_db:
            calibration_db = self._octave._octave_manager._octave_config._calibration_db
            if calibration_db is None:
                logger.warning("No calibration db found, can't save results")
            else:
                calibration_db.update_calibration_result(res, inst.input.port, "auto")

        key = (inst.input.lo_frequency, cast(float, inst.input.gain))
        if key in res:
            qe_cal = res[key]
            inst.input.set_output_dc_offset(i_offset=qe_cal.i0, q_offset=qe_cal.q0)

        for (lo_freq, _), lo_cal in res.items():
            for if_freq, if_cal in lo_cal.image.items():
                fine_cal = if_cal.fine
                self.set_mixer_correction(
                    mixer=inst.input.mixer,
                    intermediate_frequency=if_freq,
                    lo_frequency=lo_freq,
                    values=fine_cal.correction,
                )
        return res

    def set_intermediate_frequency(self, element: str, freq: float) -> None:
        """Sets the intermediate frequency of the element

        Args:
            element (str): the name of the element whose intermediate
                frequency will be updated
            freq (float): the intermediate frequency to set to the given
                element
        """
        element_inst = self._elements[element]
        element_inst.set_intermediate_frequency(freq)

    def get_output_dc_offset_by_element(self, element: str, iq_input: str) -> float:
        """Get the current DC offset of the OPX analog output channel associated with an element.

        Args:
            element: the name of the element to get the correction for
            iq_input: the port name as appears in the element config.
                Options:

                `'single'`
                    for an element with a single input

                `'I'` or `'Q'`
                    for an element with mixer inputs

        Returns:
            the offset, in normalized output units
        """
        config = self._get_pb_config()
        input_instance = self._elements[element].input
        if isinstance(input_instance, SingleInput):
            port = input_instance.port
        elif isinstance(input_instance, MixInputs):
            if iq_input == "I":
                port = input_instance.i_port
            elif iq_input == "Q":
                port = input_instance.q_port
            else:
                raise ValueError(f"Port must be I or Q, got {iq_input}.")
        else:
            raise ValueError(f"Element {element} of type {type(input_instance)} does not have a 'port' property.")

        port_number = port.number

        specific_fem = get_fem_config(config, port)
        if isinstance(specific_fem, QuaConfigMicrowaveFemDec):
            raise InvalidConfigError(f"Port num {port_number} is a MW-FEM port, has no offset")
        if port_number in specific_fem.analog_outputs:
            return specific_fem.analog_outputs[port_number].offset
        else:
            raise InvalidConfigError(f"Port num {port_number} does not exist")

    def set_output_dc_offset_by_element(
        self,
        element: str,
        input: Union[str, Tuple[str, str], List[str]],
        offset: Union[float, Tuple[float, float], List[float]],
    ) -> None:
        """Set the current DC offset of the OPX analog output channel associated with an element.

        Args:
            element (str): the name of the element to update the
                correction for
            input (Union[str, Tuple[str,str], List[str]]): the input
                name as appears in the element config. Options:

                `'single'`
                    for an element with a single input

                `'I'` or `'Q'` or a tuple ('I', 'Q')
                    for an element with mixer inputs
            offset (Union[float, Tuple[float,float], List[float]]): The
                dc value to set to, in normalized output units. Ranges
                from -0.5 to 0.5 - 2^-16 in steps of 2^-16.

        Examples:
            ```python
            qm.set_output_dc_offset_by_element('flux', 'single', 0.1)
            qm.set_output_dc_offset_by_element('qubit', 'I', -0.01)
            qm.set_output_dc_offset_by_element('qubit', ('I', 'Q'), (-0.01, 0.05))
            ```

        Note:

            If the sum of the DC offset and the largest waveform data-point exceed the normalized unit range specified
            above, DAC output overflow will occur and the output will be corrupted.
        """
        element_inst = self._elements[element]
        if isinstance(element_inst.input, MixInputs):
            if isinstance(input, (list, tuple)):
                if not set(input) <= {"I", "Q"}:
                    raise FunctionInputError(f"Input names should be 'I' or 'Q', got {input}")
                if not (isinstance(offset, (list, tuple)) and len(input) == len(offset)):
                    raise FunctionInputError(
                        f"input should be two iterables of the same size," f"got input = {input} and offset = {offset}"
                    )
                kwargs = {f"{k.lower()}_offset": v for k, v in zip(input, offset)}
            elif isinstance(input, str):
                if input not in {"I", "Q"}:
                    raise FunctionInputError(f"Input names should be 'I' or 'Q', got {input}")
                if not isinstance(offset, (int, float)):
                    raise FunctionInputError(f"Input should be int or float, got {type(offset)}")
                kwargs = {f"{input.lower()}_offset": offset}
            else:
                raise ValueError(f"Invalid input - {input}")
            element_inst.input.set_output_dc_offset(**kwargs)
        elif isinstance(element_inst.input, SingleInput):
            if input != "single":
                raise ValueError(f"Invalid input - {input} while the element has a single input")
            if not isinstance(offset, (int, float)):
                raise FunctionInputError(f"Input should be int or float, got {type(offset)}")
            element_inst.input.set_output_dc_offset(offset)
        else:
            raise ValueError(
                f"Element {element} with input of type {element_inst.input.__class__.__name__} "
                f"does not support dc offset setting."
            )

    def set_output_filter_by_element(
        self,
        element: str,
        input: str,
        feedforward: Sequence[NumpySupportedFloat],
        feedback: Sequence[NumpySupportedFloat],
    ) -> None:
        """Sets the intermediate frequency of the element

        Args:
            element: the name of the element whose ports filters will be
                updated
            input: the input name as appears in the element config.
                Options:

                `'single'`
                    for an element with single input

                `'I'` or `'Q'`
                    for an element with mixer inputs
            feedforward: the values for the feedforward filter
            feedback: the values for the feedback filter

        """
        logger.debug(
            f"Setting output filter of port '{input}' on element '{element}' "
            + f"to (feedforward: {feedforward}, feedback: {feedback})"
        )
        input_inst = self._elements[element].input
        if isinstance(input_inst, MixInputs):
            input_inst.set_output_filter(input, feedforward, feedback)
        elif isinstance(input_inst, SingleInput):
            input_inst.set_output_filter(feedforward, feedback)
        else:
            raise AttributeError(
                f"Element {element} of type {input_inst.__class__.__name__} " f"does not support filter setting."
            )

    def set_input_dc_offset_by_element(self, element: str, output: str, offset: float) -> None:
        """set the current DC offset of the OPX analog input channel associated with an element.

        Args:
            element (str): the name of the element to update the
                correction for
            output (str): the output key name as appears in the element
                config under 'outputs'.
            offset (float): the dc value to set to, in normalized input
                units. Ranges from -0.5 to 0.5 - 2^-16 in steps of
                2^-16.

        Note:
            If the sum of the DC offset and the largest waveform data-point exceed the normalized unit range specified
            above, DAC output overflow will occur and the output will be corrupted.
        """
        element_instance = self._elements[element]
        element_instance.set_input_dc_offset(output, offset)

    def get_input_dc_offset_by_element(self, element: str, output: str) -> float:
        """Get the current DC offset of the OPX analog input channel associated with an element.

        Args:
            element: the name of the element to get the correction for
            output: the output key name as appears in the element config
                under 'outputs'.

        Returns:
            the offset, in normalized output units
        """
        config = self._get_pb_config()

        element_obj = self._elements[element]
        outputs = element_obj._config.outputs
        if output in outputs:
            port = outputs[output]
        else:
            raise Exception("Output does not exist")

        specific_fem = get_fem_config(config, port)
        if isinstance(specific_fem, QuaConfigMicrowaveFemDec):
            raise InvalidConfigError(f"Port num {port.number} is a MW-FEM port, has no offset")

        if port.number in specific_fem.analog_outputs:
            return specific_fem.analog_inputs[port.number].offset
        else:
            raise InvalidConfigError(f"Port num {port.number} does not exist")

    def get_digital_delay(self, element: str, digital_input: str) -> int:
        """Gets the delay of the digital input of the element

        Args:
            element: the name of the element to get the delay for
            digital_input: the digital input name as appears in the
                element's config

        Returns:
            the delay
        """
        element_instance = self._elements[element]
        return element_instance.get_output_digital_delay(digital_input)

    def set_digital_delay(self, element: str, digital_input: str, delay: int) -> None:
        """Sets the delay of the digital input of the element

        Args:
            element (str): the name of the element to update delay for
            digital_input (str): the digital input name as appears in
                the element's config
            delay (int): the delay value to set to, in nsec. Range: 0 to
                255 - 2 * buffer, in steps of 1
        """
        element_instance = self._elements[element]
        element_instance.set_output_digital_delay(digital_input, delay)

    def get_digital_buffer(self, element: str, digital_input: str) -> int:
        """Gets the buffer for digital input of the element

        Args:
            element (str): the name of the element to get the buffer for
            digital_input (str): the digital input name as appears in
                the element's config

        Returns:
            the buffer
        """
        element_instance = self._elements[element]
        return element_instance.get_output_digital_buffer(digital_input_name=digital_input)

    def set_digital_buffer(self, element: str, digital_input: str, buffer: int) -> None:
        """Sets the buffer for digital input of the element

        Args:
            element (str): the name of the element to update buffer for
            digital_input (str): the digital input name as appears in
                the element's config
            buffer (int): the buffer value to set to, in nsec. Range: 0
                to (255 - delay) / 2, in steps of 1
        """
        element_instance = self._elements[element]
        element_instance.set_output_digital_buffer(digital_input, buffer)

    def get_time_of_flight(self, element: str) -> int:
        """Gets the *time of flight*, associated with a measurement element.

        This is the amount of time between the beginning of a measurement pulse applied to element
        and the time that the data is available to the controller for demodulation or streaming.

        Args:
            element (str): the name of the element to get time of flight
                for

        Returns:
            the time of flight, in nsec
        """
        element_object = self._elements[element]
        return element_object.time_of_flight

    def get_smearing(self, element: str) -> int:
        """Gets the *smearing* associated with a measurement element.

        This is a broadening of the raw results acquisition window, to account for dispersive broadening
        in the measurement elements (readout resonators etc.) The acquisition window will be broadened
        by this amount on both sides.

        Args:
            element (str): the name of the element to get smearing for

        Returns:
            the smearing, in nesc.
        """
        element_object = self._elements[element]
        return element_object.smearing

    @property
    def io1(self) -> Dict[str, Value]:
        return self.get_io1_value()

    @io1.setter
    def io1(self, value: Value) -> None:
        self.set_io1_value(value)

    @property
    def io2(self) -> Dict[str, Value]:
        return self.get_io1_value()

    @io2.setter
    def io2(self, value: Value) -> None:
        self.set_io2_value(value)

    def set_io1_value(self, value_1: Value) -> None:
        """Sets the value of ``IO1``.

        This can be used later inside a QUA program as a QUA variable ``IO1`` without declaration.
        The type of QUA variable is inferred from the python type passed to ``value_1``,
        according to the following rule:

        int -> int
        float -> fixed
        bool -> bool

        Args:
            value_1 (Union[float,bool,int]): the value to be placed in
                ``IO1``
        """
        self.set_io_values(value_1=value_1)

    def set_io2_value(self, value_2: Value) -> None:
        """Sets the value of ``IO1``.

        This can be used later inside a QUA program as a QUA variable ``IO2`` without declaration.
        The type of QUA variable is inferred from the python type passed to ``value_2``,
        according to the following rule:

        int -> int
        float -> fixed
        bool -> bool

        Args:
            value_2 (Union[float, bool, int]): the value to be placed in
                ``IO1``
        """
        self.set_io_values(value_2=value_2)

    def set_io_values(
        self,
        value_1: Optional[NumpySupportedValue] = None,
        value_2: Optional[NumpySupportedValue] = None,
    ) -> None:
        """Sets the values of ``IO1`` and ``IO2``

        This can be used later inside a QUA program as a QUA variable ``IO1``, ``IO2`` without declaration.
        The type of QUA variable is inferred from the python type passed to ``value_1``, ``value_2``,
        according to the following rule:

        int -> int
        float -> fixed
        bool -> bool

        Args:
            value_1 (Optional[Union[float, bool, int]]): the value to be
                placed in ``IO1``
            value_2 (Optional[Union[float, bool, int]]): the value to be
                placed in ``IO2``
        """

        if value_1 is None and value_2 is None:
            return

        try:
            if value_1 is not None:
                logger.debug(f"Setting value '{value_1}' to IO1")
                value_1 = convert_object_type(value_1)

            if value_2 is not None:
                logger.debug(f"Setting value '{value_2}' to IO2")
                value_2 = convert_object_type(value_2)
        except QmValueError as e:
            raise QmValueError(f"Failed to set_io_values: {e.message}") from e

        self._frontend.set_io_values(self._id, [value_1, value_2])

    def get_io1_value(self) -> Dict[str, Value]:
        """Gets the data stored in ``IO1``

        No inference is made on type.

        Returns:
            A dictionary with data stored in ``IO1``. (Data is in all
            three format: ``int``, ``float`` and ``bool``)
        """
        return self.get_io_values()[0]

    def get_io2_value(self) -> Dict[str, Value]:
        """Gets the data stored in ``IO2``

        No inference is made on type.

        Returns:
            A dictionary with data from the second IO register. (Data is
            in all three format: ``int``, ``float`` and ``bool``)
        """
        return self.get_io_values()[1]

    def get_io_values(self) -> List[Dict[str, Value]]:
        """Gets the data stored in both ``IO1`` and ``IO2``

        No inference is made on type.

        Returns:
            A list that contains dictionaries with data from the IO
            registers. (Data is in all three format: ``int``, ``float``
            and ``bool``)
        """
        resp1, resp2 = self._frontend.get_io_values(self._id)

        return [
            {
                "io_number": 1,
                "int_value": resp1.int_value,
                "fixed_value": resp1.double_value,
                "boolean_value": resp1.boolean_value,
            },
            {
                "io_number": 2,
                "int_value": resp2.int_value,
                "fixed_value": resp2.double_value,
                "boolean_value": resp2.boolean_value,
            },
        ]

    def peek(self, address: Any) -> None:
        warnings.warn(
            deprecation_message(
                method="QuantumMachine.peek", deprecated_in="1.1.0", removed_in="1.2.0", details="Not Implemented"
            ),
            DeprecationWarning,
            stacklevel=2,
        )
        raise NotImplementedError()
        # if you must use this, code below will work for a specific controller
        # request = PeekRequest()
        # request.controllerId = list(self._config["controllers"].keys())[0]
        # request.address = address

        # return self._frontend.Peek(request)

    def poke(self, address: Any, value: Any) -> None:
        warnings.warn(
            deprecation_message(
                method="QuantumMachine.poke", deprecated_in="1.1.0", removed_in="1.2.0", details="Not Implemented"
            ),
            DeprecationWarning,
            stacklevel=2,
        )
        pass

    def _get_pb_config(self) -> QuaConfig:
        return self._frontend.get_quantum_machine_config(self._id)

    def _get_config_as_object(self) -> QuaConfigQuaConfigV1:
        return self._get_pb_config().v1_beta

    def get_config(self) -> DictQuaConfig:
        """Gets the current config of the qm

        Returns:
            A dictionary with the QMs config
        """
        config = self._get_pb_config()
        self._config = config
        return convert_msg_to_config(config)

    def save_config_to_file(self, filename: PathLike) -> None:
        """Saves the qm current config to a file

        Args:
            filename: The name of the file where the config will be saved
        """
        json_str = json.dumps(self.get_config())
        with open(filename, "w") as writer:
            writer.write(json_str)

    def get_running_job(self) -> Optional[Union[QmJob, OldJobApiMock]]:
        """Gets the currently running job. Returns None if there isn't one."""

        job_id = self._job_manager.get_running_job(self._id)
        if job_id is None:
            return None

        try:
            pending_job = QmPendingJob(
                job_id=job_id,
                machine_id=self._id,
                frontend_api=self._frontend,
                capabilities=self._capabilities,
                store=self._store,
            )
            return pending_job.wait_for_execution(timeout=10.0)
        except JobCancelledError:
            # In case that the job has finished between the GetRunningJon and the
            # wait for execution
            return None

    def get_job(self, job_id: str) -> Union[QmJob, QmPendingJob, OldJobApiMock]:
        status: JobExecutionStatus = self._job_manager.get_job_execution_status(job_id, self._id)
        if status.running or status.completed:
            return QmJob(
                job_id=job_id,
                machine_id=self._id,
                frontend_api=self._frontend,
                capabilities=self._capabilities,
                store=self._store,
            )

        if status.pending or status.loading:
            return QmPendingJob(
                job_id=job_id,
                machine_id=self._id,
                frontend_api=self._frontend,
                capabilities=self._capabilities,
                store=self._store,
            )

        raise ErrorJobStateError(
            f"job {self._id} encountered an error",
            error_list=[value.string_value for value in status.error.error_messages.values],
        )

    def set_digital_input_threshold(self, port: PortReferenceType, threshold: float) -> None:
        controller_name, fem_number, port_number = _standardize_port(port)
        self._frontend.set_digital_input_threshold(self._id, controller_name, fem_number, port_number, threshold)

    def _get_digital_input_port(self, port: PortReferenceType) -> QuaConfigDigitalInputPortDec:
        config = self._get_pb_config()
        controller_name, fem_number, port_number = _standardize_port(port)
        port_obj = QuaConfigPortReference(controller=controller_name, fem=fem_number, number=port_number)
        fem_config = get_fem_config(config, port_obj)
        if port_obj.number in fem_config.digital_inputs:
            return fem_config.digital_inputs[port_number]
        raise InvalidConfigError("Digital input port not found")

    def get_digital_input_threshold(self, port: PortReferenceType) -> float:
        return self._get_digital_input_port(port).threshold

    def set_digital_input_deadtime(self, port: PortReferenceType, deadtime: int) -> None:
        controller_name, fem_number, port_number = _standardize_port(port)
        self._frontend.set_digital_input_dead_time(self._id, controller_name, fem_number, port_number, deadtime)

    def get_digital_input_deadtime(self, port: PortReferenceType) -> int:
        return self._get_digital_input_port(port).deadtime

    def set_digital_input_polarity(self, port: PortReferenceType, polarity: str) -> None:
        try:
            polarity_enum = Polarity[polarity]
        except KeyError:
            raise InvalidDigitalInputPolarityError(
                f"Invalid value for polarity {polarity}. Valid values are: 'RISING' or 'FALLING'."
            )

        controller_name, fem_number, port_number = _standardize_port(port)
        self._frontend.set_digital_input_polarity(self._id, controller_name, fem_number, port_number, polarity_enum)

    def get_digital_input_polarity(self, port: PortReferenceType) -> str:
        return QuaConfigDigitalInputPortDecPolarity(self._get_digital_input_port(port).polarity).name


def _standardize_port(port: PortReferenceType) -> StandardPort:
    if len(port) == 2:
        return port[0], OPX_FEM_IDX, port[1]
    return cast(StandardPort, port)
