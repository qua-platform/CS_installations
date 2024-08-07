import logging
import dataclasses
import math as _math
from enum import Enum
from enum import Enum as _Enum
from dataclasses import dataclass
from collections.abc import Iterable
from typing import Set, Dict, List, Type, Tuple, Union, Optional, Sequence, overload

import betterproto
import numpy as np

import qm.grpc.qua as _qua
from qm._loc import _get_loc
from qm.program import Program
from qm.exceptions import QmQuaException
from qm.utils import is_iter as _is_iter
from qm.program._ResultAnalysis import _ResultAnalysis
from qm.utils.general_utils import create_input_stream_name
from qm.qua.DigitalMeasureProcess import DigitalMeasureProcess
from qm.qua.AnalogMeasureProcess import RawTimeTagging as AnalogRawTimeTagging
from qm.program.StatementsCollection import PortConditionedStatementsCollection
from qm.qua.DigitalMeasureProcess import RawTimeTagging as DigitalRawTimeTagging
from qm.qua.DigitalMeasureProcess import Counting as DigitalMeasureProcessCounting
from qm.program.StatementsCollection import StatementsCollection as _StatementsCollection
from qm.utils import collection_has_type_int, collection_has_type_bool, collection_has_type_float
from qm.qua._dsl_specific_type_hints import (
    ChirpType,
    AmpValuesType,
    PlayPulseType,
    QuaNumberType,
    MeasurePulseType,
    TypeOrExpression,
)
from qm.qua._type_hinting import (
    OneOrMore,
    AllPyTypes,
    MessageVarType,
    ForEachValuesType,
    PyNumberArrayType,
    MessageExpressionType,
    VariableDeclarationType,
    MessageVariableOrExpression,
    fixed,
)
from qm.qua._expressions import (
    AllQuaTypes,
    PyFloatType,
    QuaVariable,
    PyNumberType,
    QuaExpression,
    QuaVariableType,
    QuaExpressionType,
    literal_int,
    literal_bool,
    literal_real,
    to_expression,
)
from qm.qua.AnalogMeasureProcess import (
    BareIntegration,
    DemodIntegration,
    HighResTimeTagging,
    DualBareIntegration,
    ScalarProcessTarget,
    VectorProcessTarget,
    AnalogMeasureProcess,
    DualDemodIntegration,
    SlicedAnalogTimeDivision,
    AccumulatedAnalogTimeDivision,
    MovingWindowAnalogTimeDivision,
)

_Variable = QuaVariable  # This alias is for supporting an import that appears in QUA-lang tools

_TIMESTAMPS_LEGACY_SUFFIX = "_timestamps"

_block_stack: List["_BaseScope"] = []

logger = logging.getLogger(__name__)

StreamType = Union[str, "_ResultSource"]
MeasureProcessType = Union[
    AnalogMeasureProcess,
    DigitalMeasureProcess,
]
TimeDivisionType = Union[
    SlicedAnalogTimeDivision,
    AccumulatedAnalogTimeDivision,
    MovingWindowAnalogTimeDivision,
]
AnalogProcessTargetType = Union[
    ScalarProcessTarget,
    VectorProcessTarget,
]


_RESULT_SYMBOL = "@re"


DEFAULT_OUT1 = "out1"
DEFAULT_OUT2 = "out2"


def program():
    """Create a QUA program.

    Used within a context manager, the program is defined in the code block
    below ``with`` statement.

    Statements in the code block below are played as soon as possible, meaning that an instruction
    will be played immediately unless it is dependent on a previous instruction.
    Additionally, commands output to the same elements will be played sequentially,
    and to different elements will be played in parallel.
    An exception is that pulses will be implicitly aligned at the end of each [`for_`][qm.qua._dsl.for_] loop iteration.

    The generated ``program_name`` object is used as an input to the execute function of a
    [qm.QuantumMachine][] object.

    Example:
        ```python
        with program() as program_name:
            play('pulse1', 'element1')
            wait('element1')

        qm.execute(program_name)
        ```

    where ``qm`` is an instance of a [qm.QuantumMachine][]
    """
    return _ProgramScope(Program())


def play(
    pulse: PlayPulseType,
    element: str,
    duration: Optional[QuaNumberType] = None,
    condition: Optional[QuaExpressionType] = None,
    chirp: Optional[ChirpType] = None,
    truncate: Optional[QuaNumberType] = None,
    timestamp_stream: Optional[StreamType] = None,
    continue_chirp: bool = False,
    target: str = "",
) -> None:
    r"""Play a `pulse` based on an 'operation' defined in `element`.

    The pulse will be modified according to the properties of the element
    (see detailed explanation about pulse modifications below),
    and then played to the OPX output(s) defined to be connected
    to the input(s) of the element in the configuration.

    Args:
        pulse (str): The name of an `operation` to be performed, as
            defined in the element in the quantum machine configuration.
            Can also be a [ramp][qm.qua._dsl.ramp] function or be multiplied by an
            [ramp][qm.qua._dsl.ramp].
        element (str): The name of the element, as defined in the
            quantum machine configuration.
        duration (Union[int,QUA variable of type int]): The time to play
            this pulse in units of the clock cycle (4ns). If not
            provided, the default pulse duration will be used. It is
            possible to dynamically change the duration of both constant
            and arbitrary pulses. Arbitrary pulses can only be stretched,
            not compressed.
        chirp (Union[(list[int], str), (int, str)]): Allows to perform
            piecewise linear sweep of the element’s intermediate
            frequency in time. Input should be a tuple, with the 1st
            element being a list of rates and the second should be a
            string with the units. The units can be either: ‘Hz/nsec’,
            ’mHz/nsec’, ’uHz/nsec’, ’pHz/nsec’ or ‘GHz/sec’, ’MHz/sec’,
            ’KHz/sec’, ’Hz/sec’, ’mHz/sec’.
        truncate (Union[int, QUA variable of type int]): Allows playing
            only part of the pulse, truncating the end. If provided,
            will play only up to the given time in units of the clock
            cycle (4ns).
        condition (A logical expression to evaluate.): Will play the operation only if the condition is true.
        Prior to QOP 2.2, only the analog part was conditioned, i.e., any digital pulses associated
        with the operation would always play.
        timestamp_stream (Union[str, _ResultSource]): (Supported from
            QOP 2.2) Adding a `timestamp_stream` argument will save the
            time at which the operation occurred to a stream. If the
            `timestamp_stream` is a string ``label``, then the timestamp
            handle can be retrieved with
            [`qm._results.JobResults.get`][qm.results.streaming_result_fetcher.StreamingResultFetcher] with the same
            ``label``.

    Note:
        Arbitrary waveforms cannot be compressed and can only be expanded up to
        $2^{24}-1$ clock cycles (67ms). Unexpected output will occur if a duration
        outside the range is given.
        See [Dynamic pulse duration](../../../Guides/features/#dynamic-pulse-duration)
        in the documentation for further information.

    Note:
        When using chirp, it is possible to add a flag "continue_chirp=True" to the play command.
        When this flag is set, the internal oscillator will continue the chirp even after the play command had ended.
        See the `chirp documentation [chirp documentation](../../../Guides/features/#frequency-chirp)
        for more information.

    Example:
        ```python
        with program() as prog:
            v1 = declare(fixed)
            assign(v1, 0.3)
            play('pulse1', 'element1')
            play('pulse1' * amp(0.5), 'element1')
            play('pulse1' * amp(v1), 'element1')
            play('pulse1' * amp(0.9, v1, -v1, 0.9), 'element_iq_pair')
            time_stream = declare_stream()
            # Supported on QOP2.2+
            play('pulse1', 'element1', duration=16, timestamp_stream='t1')
            play('pulse1', 'element1', duration=16, timestamp_stream=time_stream)
            with stream_processing():
                stream.buffer(10).save_all('t2')
        ```
    """
    body = _get_scope_as_blocks_body()
    if duration is not None:
        duration = _unwrap_exp(exp(duration))
    if condition is not None:
        condition = _unwrap_exp(exp(condition))
    if truncate is not None:
        truncate = _unwrap_exp(exp(truncate))

    if chirp is not None:
        if len(chirp) == 2:
            chirp_var, chirp_units = chirp
            chirp_times = None
        elif len(chirp) == 3:
            chirp_var, chirp_times, chirp_units = chirp
        else:
            raise QmQuaException("chirp must be tuple of 2 or 3 values")
        chirp_times_list: Optional[List[QuaNumberType]] = (
            chirp_times.tolist() if isinstance(chirp_times, np.ndarray) else chirp_times
        )
        if isinstance(chirp_var, (list, np.ndarray)):
            chirp_var = declare(int, value=chirp_var)

        chirp_var = _unwrap_exp(exp(chirp_var))
        chirp = _qua.QuaProgramChirp()
        chirp.continue_chirp = continue_chirp
        if chirp_times_list is not None:
            chirp.times.extend(chirp_times_list)
        if isinstance(chirp_var, _qua.QuaProgramArrayVarRefExpression):
            chirp.array_rate = chirp_var
        else:
            chirp.scalar_rate = chirp_var

        if chirp_units == "Hz/nsec" or chirp_units == "GHz/sec":
            chirp.units = _qua.QuaProgramChirpUnits.HzPerNanoSec

        units_mapping = {
            "Hz/nsec": _qua.QuaProgramChirpUnits.HzPerNanoSec,
            "GHz/sec": _qua.QuaProgramChirpUnits.HzPerNanoSec,
            "mHz/nsec": _qua.QuaProgramChirpUnits.mHzPerNanoSec,
            "MHz/sec": _qua.QuaProgramChirpUnits.mHzPerNanoSec,
            "uHz/nsec": _qua.QuaProgramChirpUnits.uHzPerNanoSec,
            "KHz/sec": _qua.QuaProgramChirpUnits.uHzPerNanoSec,
            "nHz/nsec": _qua.QuaProgramChirpUnits.nHzPerNanoSec,
            "Hz/sec": _qua.QuaProgramChirpUnits.nHzPerNanoSec,
            "pHz/nsec": _qua.QuaProgramChirpUnits.pHzPerNanoSec,
            "mHz/sec": _qua.QuaProgramChirpUnits.pHzPerNanoSec,
        }

        if chirp_units in units_mapping:
            chirp.units = units_mapping[chirp_units]
        else:
            raise QmQuaException(f'unknown units "{chirp_units}"')
    timestamp_label = None
    if isinstance(timestamp_stream, str):
        scope = _get_root_program_scope()
        scope.program.set_metadata(uses_command_timestamps=True)
        timestamp_label = scope.declare_save(timestamp_stream).get_var_name()
    elif isinstance(timestamp_stream, _ResultSource):
        _get_root_program_scope().program.set_metadata(uses_command_timestamps=True)
        timestamp_label = timestamp_stream.get_var_name()
    body.play(
        pulse,
        element,
        duration=duration,
        condition=condition,
        target=target,
        chirp=chirp,
        truncate=truncate,
        timestamp_label=timestamp_label,
    )


def pause():
    """Pause the execution of the job until [qm.jobs.running_qm_job.RunningQmJob.resume][] is called.

    The quantum machines freezes on its current output state.
    """
    body = _get_scope_as_blocks_body()
    body.pause()


def update_frequency(
    element: str,
    new_frequency: QuaNumberType,
    units: str = "Hz",
    keep_phase: bool = False,
):
    """Dynamically update the frequency of the oscillator associated with a given `element`.

    This changes the frequency from the value defined in the quantum machine configuration.

    The behavior of the phase (continuous vs. coherent) is controlled by the ``keep_phase`` parameter and
    is discussed in [the documentation](../../../Introduction/qua_overview/#frequency-and-phase-transformations).

    Args:
        element (str): The element associated with the oscillator whose
            frequency will be changed
        new_frequency (int): The new frequency value to set in units set
            by ``units`` parameter. In steps of 1.
        units (str): units of new frequency. Useful when sub-Hz
            precision is required. Allowed units are "Hz", "mHz", "uHz",
            "nHz", "pHz"
        keep_phase (bool): Determine whether phase will be continuous
            through the change (if ``True``) or it will be coherent,
            only the frequency will change (if ``False``).

    Example:
        ```python
        with program() as prog:
            update_frequency("q1", 4e6) # will set the frequency to 4 MHz

            ### Example for sub-Hz resolution
            update_frequency("q1", 100.7) # will set the frequency to 100 Hz (due to casting to int)
            update_frequency("q1", 100700, units='mHz') # will set the frequency to 100.7 Hz
        ```
    """
    body = _get_scope_as_blocks_body()
    body.update_frequency(element, _unwrap_exp(exp(new_frequency)), units, keep_phase)


def update_correction(
    element: str,
    c00: QuaNumberType,
    c01: QuaNumberType,
    c10: QuaNumberType,
    c11: QuaNumberType,
) -> None:
    """Updates the correction matrix used to overcome IQ imbalances of the IQ mixer for the next pulses
    played on the element

    Note:

        Make sure to update the correction after you called [`update_frequency`][qm.qua._dsl.update_frequency]

    Note:

        Calling ``update_correction`` will also reset the frame of the oscillator associated with the element.

    Args:
        element (str): The element associated with the oscillator whose
            correction matrix will change
        c00 (Union[float,QUA variable of type real]): The top left
            matrix element
        c01 (Union[float,QUA variable of type real]): The top right
            matrix element
        c10 (Union[float,QUA variable of type real]): The bottom left
            matrix element
        c11 (Union[float,QUA variable of type real]): The bottom right
            matrix element

    Example:
        ```python
        with program() as prog:
            update_correction("q1", 1.0, 0.5, 0.5, 1.0)
        ```
    """
    body = _get_scope_as_blocks_body()
    body.update_correction(
        element,
        _unwrap_exp(exp(c00)),
        _unwrap_exp(exp(c01)),
        _unwrap_exp(exp(c10)),
        _unwrap_exp(exp(c11)),
    )


def set_dc_offset(element: str, element_input: str, offset: QuaNumberType):
    """Set the DC offset of an element's input to the given value. This value will remain the DC offset until changed or
    until the Quantum Machine is closed.
    The offset value remains until it is changed or the Quantum Machine is closed.

    -- Available from QOP 2.0 --

    Args:
        element: The element to update its DC offset
        element_input: The desired input of the element, can be 'single'
            for a 'singleInput' element or 'I' or 'Q' for a 'mixInputs'
            element
        offset: The offset to set
    """

    body = _get_scope_as_blocks_body()
    body.set_dc_offset(element, element_input, _unwrap_exp(exp(offset)))


def measure(
    pulse: MeasurePulseType,
    element: str,
    stream: Optional[StreamType] = None,
    *outputs,
    timestamp_stream: Optional[StreamType] = None,
):
    """Perform a measurement of `element` using `pulse` based on 'operation' as defined in the 'element'.

    An element for which a measurement is applied must have outputs defined in the configuration.

    A measurement consists of:

    1. playing an operation to the element (identical to a :func:`play` statement)

    2. waiting for a duration of time defined as the ``time_of_flight``
       in the configuration of the element, and then sampling
       the returning pulse.
       The OPX input to be sampled is defined in the configuration of the element.

    3. Processing the acquired data according to a parameter defined in the measure command,
        including Demodulation, Integration and Time Tagging.

    For a more detailed description of the measurement operation, see
    [Measure Statement Features](../../../Guides/features#measure-statement-features)

    Args:
        pulse (str): The name of an `operation` to be performed, as
            defined in the element in the quantum machine configuration.
            Pulse must have a ``measurement`` operation. Can also be
            multiplied by an [amp][qm.qua._dsl.amp].
        element (str): name of the element, as defined in the quantum
            machine configuration. The element must have outputs.
        stream (Union[str, _ResultSource]): The stream variable which
            the raw ADC data will be saved and will appear in result
            analysis scope. You can receive the results with
            [qm.QmJob.result_handles.get("name")][qm.jobs.running_qm_job.RunningQmJob.result_handles]. A string name
            can also be used. In this case, the name of the result
            handle should be suffixed by ``_input1`` for data from
            analog input 1 and ``_input2`` for data from analog input 2.

            If ``stream`` is set to ``None``, raw results will not be saved
            (note: must be explicitly set to ``None``).
            The raw results will be saved as long as the digital pulse that is played with pulse is high.

            !!! Warning:

                Streaming adc data without declaring the stream with `declare_stream(adc_trace=true)` might cause performance issues

        *outputs (tuple): A parameter specifying the processing to be
            done on the ADC data, there are multiple options available,
            including demod(), integration() & time_tagging().
        timestamp_stream (Union[str, _ResultSource]): (Supported from
            QOP 2.2) Adding a `timestamp_stream` argument will save the
            time at which the operation occurred to a stream. If the
            `timestamp_stream` is a string ``label``, then the timestamp
            handle can be retrieved with
            [qm.results.streaming_result_fetcher.StreamingResultFetcher][] with the same
            ``label``.

    Example:
        ```python
        with program() as prog:
            I = declare(fixed)
            Q = declare(fixed)
            adc_st = declare_stream(adc_trace=True)

            # measure by playing 'meas_pulse' to element 'resonator', do not save raw results.
            # demodulate data from "out1" port of 'resonator' using 'cos_weights' and store result in I, and also
            # demodulate data from "out1" port of 'resonator' using 'sin_weights' and store result in Q
            measure('meas_pulse', 'resonator', None, demod.full("cos_weights", I, "out1"), demod.full("sin_weights", Q, "out1"))

            # measure by playing 'meas_pulse' to element 'resonator', save raw results to `adc_st`
            # demodulate data from 'out1' port of 'resonator' using 'optimized_weights' and store result in I
            measure('meas_pulse', 'resonator', adc_st, demod.full("optimized_weights", I, "out1"))
            with stream_processing():
                adc_st.input1().save_all("raw_adc_stream")

        from qm import QuantumMachinesManager
        qm = QuantumMachinesManager().open_qm(config)
        job = qm.execute(prog)
        # ... we wait for the results to be ready...
        job.result_handles.wait_for_all_values()
        # raw results can be retrieved as follows (here job is a QmJob object:
        raw_I_handle = job.result_handles.get("raw_adc_stream")
        ```

    """
    body = _get_scope_as_blocks_body()

    measure_process = []
    for i, output in enumerate(outputs):
        if type(output) == tuple:
            if len(output) == 2:
                measure_process.append(demod.full(output[0], output[1], ""))
            elif len(output) == 3:
                measure_process.append(demod.full(output[0], output[2], output[1]))
            else:
                raise QmQuaException(
                    "Each output must be a tuple of (integration weight, output name, variable name), but output "
                    + str(i + 1)
                    + " is invalid"
                )
        else:
            measure_process.append(output)

    if stream is not None and isinstance(stream, str):
        adc_stream = _get_root_program_scope().declare_legacy_adc(stream)
    else:
        if stream is not None and (not isinstance(stream, _ResultSource)):
            raise QmQuaException("stream object is not of the right type")
        adc_stream = stream

    if adc_stream and not adc_stream._configuration.is_adc_trace:
        logger.warning(
            "Streaming adc data without declaring the stream with "
            "`declare_stream(adc_trace=true)` might cause performance issues"
        )
    timestamp_label = None
    if isinstance(timestamp_stream, str):
        scope = _get_root_program_scope()
        scope.program.set_metadata(uses_command_timestamps=True)
        timestamp_label = scope.declare_save(timestamp_stream).get_var_name()
    elif isinstance(timestamp_stream, _ResultSource):
        _get_root_program_scope().program.set_metadata(uses_command_timestamps=True)
        timestamp_label = timestamp_stream.get_var_name()
    body.measure(
        pulse,
        element,
        adc_stream,
        timestamp_label=timestamp_label,
        *[_unwrap_measure_process(x) for x in measure_process],
    )


def align(*elements: str):
    """Align several elements together.

    All the elements referenced in `elements` will wait for all the others to
    finish their currently running statement.

    If no arguments are given, the statement will align all the elements used in the program.

    Args:
        *elements (str): a single element, multiple elements, or none
    """
    body = _get_scope_as_blocks_body()
    body.align(*elements)


def reset_phase(element: str):
    r"""
    Resets the phase of the oscillator associated with `element`,
    setting the phase of the next pulse to absolute zero.
    This sets the phase of the currently playing intermediate frequency
    to the value it had at the beginning of the program (t=0).

    Note:

        * The phase will only be set to zero when the next play or align command is executed on the element.
        * Reset phase will only reset the phase of the intermediate frequency (:math:`\\omega_{IF}`) currently in use.

    Args:
        element: an element
    """
    body = _get_scope_as_blocks_body()
    body.reset_phase(element)


def ramp_to_zero(element: str, duration: Optional[QuaNumberType] = None):
    r"""Starting from the last DC value, gradually lowers the DC to zero for `duration` *4nsec

    If `duration` is None, the duration is taken from the element's config

    Warning:
        This feature does not protect from voltage jumps. Those can still occur, i.e. when the data sent to the
        analog output is outside the range -0.5 to $0.5 - 2^{16}$ and thus will have an overflow.

    Args:
        element (str): element for ramp to zero
        duration (Union[int,None]): time , `in multiples of 4nsec`.
            Range: [4, $2^{24}$] in steps of 1, or `None` to take
            value from config
    """
    body = _get_scope_as_blocks_body()
    duration = duration if not (isinstance(duration, np.integer)) else duration.item()
    body.ramp_to_zero(element, duration)


def wait(duration: QuaNumberType, *elements: str):
    r"""Wait for the given duration on all provided elements without outputting anything.
    Duration is in units of the clock cycle (4ns)

    Args:
        duration (Union[int,QUA variable of type int]): time to wait in
            units of the clock cycle (4ns). Range: [4, $2^{31}-1$]
            in steps of 1.
        *elements (Union[str,sequence of str]): elements to wait on

    Warning:

        In case the value of this is outside the range above, unexpected results may occur.

    Note:

        The purpose of the `wait` operation is to add latency. In most cases, the
        latency added will be exactly the same as that specified by the QUA variable or
        the literal used. However, in some cases an additional computational latency may
        be added. If the actual wait time has significance, such as in characterization
        experiments, the actual wait time should always be verified with a simulator.
    """
    body = _get_scope_as_blocks_body()
    body.wait(_unwrap_exp(exp(duration)), *elements)


def wait_for_trigger(
    element: str,
    pulse_to_play: Optional[str] = None,
    trigger_element: Optional[OneOrMore[str]] = None,
    time_tag_target: Optional[QuaNumberType] = None,
):
    """Wait for an external trigger on the provided element.

    During the command the OPX will play the pulse supplied by the ``pulse_to_play`` parameter

    Args:
        element (str): element to wait on
        pulse_to_play (str): the name of the pulse to play on the
            element while waiting for the external trigger. Must be a
            constant pulse. Default None, no pulse will be played.
        trigger_element (Union[str, tuple]): Available only with the
            OPD. The triggered element. See further details in the note.
        time_tag_target (QUA variable of type int): Available only with
            the OPD. The time at which the trigger arrived relative to
            the waiting start time. In ns.

    Warning:
        In the OPX - The maximum allowed voltage value for the digital trigger is 1.8V. A voltage higher than this can damage the
        controller.

        In the OPX+ and with the OPD - The maximum allowed voltage is 3.3V.

    Note:
        Read more about triggering with the OPD [here](../../../Hardware/dib/#wait-for-trigger)
    """
    body = _get_scope_as_blocks_body()
    if time_tag_target is not None:
        time_tag_target = _unwrap_exp(exp(time_tag_target)).variable
    body.wait_for_trigger(pulse_to_play, trigger_element, time_tag_target, element)


def save(var: AllQuaTypes, stream_or_tag: Union[str, "_ResultStream"]):
    """Stream a QUA variable, a QUA array cell, or a constant scalar.
    the variable is streamed and not immediately saved (see [Stream processing](../../../Guides/stream_proc#stream-processing)).
    In case ``result_or_tag`` is a string, the data will be immediately saved to a result handle under the same name.

    If result variable is used, it can be used in results analysis scope see [stream_processing][qm.qua._dsl.stream_processing]
    if string tag is used, it will let you receive result with [qm.QmJob.result_handles][qm.jobs.running_qm_job.RunningQmJob.result_handles].
    The type of the variable determines the stream datatype, according to the following rule:

    - int -> int64
    - fixed -> float64
    - bool -> bool

    Note:

        Saving arrays as arrays is not currently supported. Please use a QUA for loop to save an array.

    Example:
        ```python
        # basic save
        a = declare(int, value=2)
        save(a, "a")

        # fetching the results from python (job is a QmJob object):
        a_handle = job.result_handles.get("a")
        a_data = a_handle.fetch_all()

        # save the third array cell
        vec = declare(fixed, value=[0.2, 0.3, 0.4, 0.5])
        save(vec[2], "ArrayCellSave")

        # array iteration
        i = declare(int)
        array = declare(fixed, value=[x / 10 for x in range(30)])
        with for_(i, 0, i < 30, i + 1):
            save(array[i], "array")

        # save a constant
        save(3, "a")
        ```

    Args:
        var (Union[QUA variable, a QUA array cell]): A QUA variable or a
            QUA array cell to save
        stream_or_tag (Union[str, stream variable]): A stream variable
            or string tag name to save the value under
    """
    if stream_or_tag is not None and isinstance(stream_or_tag, str):
        result_obj = _get_root_program_scope().declare_legacy_save(stream_or_tag)
    else:
        result_obj: _ResultStream = stream_or_tag

    if result_obj._configuration.is_adc_trace:
        raise QmQuaException("adc_trace can't be used in save")

    body = _get_scope_as_blocks_body()
    body.save(_unwrap_save_source(exp(var)), result_obj)


def frame_rotation(angle: QuaNumberType, *elements: str):
    r"""Shift the phase of the oscillator associated with an element by the given angle.

    This is typically used for virtual z-rotations.

    Note:
        The fixed point format of QUA variables of type fixed is 4.28, meaning the phase
        must be between $-8$ and $8-2^{28}$. Otherwise the phase value will be invalid.
        It is therefore better to use `frame_rotation_2pi()` which avoids this issue.

    Note:
        The phase is accumulated with a resolution of 16 bit.
        Therefore, *N* changes to the phase can result in a phase (and amplitude) inaccuracy of about :math:`N \cdot 2^{-16}`.
        To null out this accumulated error, it is recommended to use `reset_frame(el)` from time to time.

    Args:
        angle (Union[float, QUA variable of type fixed]): The angle to
            add to the current phase (in radians)
        *elements (str): a single element whose oscillator's phase will
            be shifted. multiple elements can be given, in which case
            all of their oscillators' phases will be shifted

    """
    frame_rotation_2pi(angle * 0.15915494309189535, *elements)


def frame_rotation_2pi(angle: QuaNumberType, *elements: str):
    r"""Shift the phase of the oscillator associated with an element by the given angle in units of 2pi radians.

    This is typically used for virtual z-rotations.

    Note:
        Unlike the case of frame_rotation(), this method performs the 2-pi radian wrap around of the angle automatically.

    Note:
        The phase is accumulated with a resolution of 16 bit.
        Therefore, *N* changes to the phase can result in a phase inaccuracy of about :math:`N \cdot 2^{-16}`.
        To null out this accumulated error, it is recommended to use `reset_frame(el)` from time to time.

    Args:
        angle (Union[float,QUA variable of type real]): The angle to add
            to the current phase (in $2\pi$ radians)
        *elements (str): a single element whose oscillator's phase will
            be shifted. multiple elements can be given, in which case
            all of their oscillators' phases will be shifted

    """
    body = _get_scope_as_blocks_body()
    body.z_rotation(_unwrap_exp(exp(angle)), *elements)


def reset_frame(*elements: str):
    """Resets the frame of the oscillator associated with an element to 0.

    Used to reset all the frame updated made up to this statement.

    Args:
        *elements (str): a single element whose oscillator's phase will
            be reset. multiple elements can be given, in which case all
            of their oscillators' phases will be reset

    """
    body = _get_scope_as_blocks_body()
    body.reset_frame(*elements)


def fast_frame_rotation(cosine, sine, *elements: str):
    r"""Shift the phase of the oscillator associated with an element by applying the
    rotation matrix [[cosine, -sine],[sin, cosine]].

    This is typically used for virtual z-rotations.

    -- Available from QOP 2.2 --

    Note:
        The phase is accumulated with a resolution of 16 bit.
        Therefore, *N* changes to the phase can result in a phase (and amplitude) inaccuracy of about :math:`N \cdot 2^{-16}`.
        To null out this accumulated error, it is recommended to use `reset_frame(el)` from time to time.

    Args:
        cosine (Union[float,QUA variable of type real]): The main
            diagonal values of the rotation matrix
        sine (Union[float,QUA variable of type real]): The bottom left
            rotation matrix element and minus the top right rotation
            matrix element value
        *elements (str): A single element whose oscillator's phase will
            be shifted. multiple elements can be given, in which case
            all of their oscillators' phases will be shifted
    """
    _get_root_program_scope().program.set_metadata(uses_fast_frame_rotation=True)
    body = _get_scope_as_blocks_body()
    body.fast_frame_rotation(_unwrap_exp(exp(cosine)), _unwrap_exp(exp(sine)), *elements)


def assign(var, _exp):
    """Set the value of a given QUA variable, or of a QUA array cell

    Args:
        var (QUA variable): A QUA variable or a QUA array cell for which
            to assign
        _exp (QUA expression): An expression for which to set the
            variable

    Example::
        ```python
        with program() as prog:
            v1 = declare(fixed)
            assign(v1, 1.3)
            play('pulse1' * amp(v1), 'element1')
        ```
    """
    body = _get_scope_as_blocks_body()
    _exp = exp(_exp)
    _var = exp(var)
    body.assign(_unwrap_assign_target(_var), _unwrap_exp(_exp))


def switch_(expression: QuaExpressionType, unsafe: bool = False) -> "_SwitchScope":
    """Part of the switch-case flow control statement in QUA.

    To be used with a context manager.

    The code block inside should be composed of only ``case_()`` and ``default_()``
    statements, and there should be at least one of them.

    The expression given in the ``switch_()`` statement will be evaluated and compared
    to each of the values in the ``case_()`` statements. The QUA code block following
    the ``case_()`` statement which evaluated to true will be executed. If none of the
    statements evaluated to true, the QUA code block following the ``default_()``
    statement (if given) will be executed.

    Args:
        expression: An expression to evaluate
        unsafe: If set to True, then switch-case would be more efficient
            and would produce fewer gaps. However, if an input which does
            not match a case is given, unexpected behavior will occur.
            Cannot be used with the ``default_()`` statement. Default is
            false, use with care.

    Example:
        ```python
        x=declare(int)
        with switch_(x):
            with case_(1):
                play('first_pulse', 'element')
            with case_(2):
                play('second_pulse', 'element')
            with case_(3):
                play('third_pulse', 'element')
            with default_():
                play('other_pulse', 'element')
        ```
    """
    body = _get_scope_as_blocks_body()
    return _SwitchScope(expression, body, unsafe)


def case_(case_exp: TypeOrExpression[AllPyTypes]) -> "_BodyScope":
    """Part of the switch-case flow control statement in QUA.

    To be used with a context manager.

    Must be inside a ``switch_()`` statement.

    The expression given in the ``switch_()`` statement will be evaluated and compared
    to each of the values in the ``case_()`` statements. The QUA code block following
    the ``case_()`` statement which evaluated to true will be executed. If none of the
    statements evaluated to true, the QUA code block following the ``default_()``
    statement (if given) will be executed.

    Args:
        case_exp: A value (or expression) to compare to the expression
            in the ``switch_()`` statement

    Example:
        ```python
        x=declare(int)
        with switch_(x):
            with case_(1):
                play('first_pulse', 'element')
            with case_(2):
                play('second_pulse', 'element')
            with case_(3):
                play('third_pulse', 'element')
            with default_():
                play('other_pulse', 'element')
        ```
    """
    switch = _get_scope_as_switch_scope()
    condition = _unwrap_exp(switch.expression == case_exp)
    if switch.if_statement is None:
        body = switch.container.if_block(condition, switch.unsafe)
        switch.if_statement = switch.container.get_last_statement()
        return _BodyScope(body)
    else:
        else_if_statement = _qua.QuaProgramElseIf(
            loc=switch.if_statement.if_.loc,
            condition=condition,
            body=_qua.QuaProgramStatementsCollection(statements=[]),
        )
        switch.if_statement.if_.elseifs.append(else_if_statement)
        return _BodyScope(_StatementsCollection(else_if_statement.body))


def default_() -> "_BaseScope":
    """Part of the switch-case flow control statement in QUA.

    To be used with a context manager.

    Must be inside a ``switch_()`` statement, and there can only be one ``default_()``
    statement.

    The expression given in the ``switch_()`` statement will be evaluated and compared
    to each of the values in the ``case_()`` statements. The QUA code block following
    the ``case_()`` statement which evaluated to true will be executed. If none of the
    statements evaluated to true, the QUA code block following the ``default_()``
    statement (if given) will be executed.

    Example:
        ```python
        x=declare(int)
        with switch_(x):
            with case_(1):
                play('first_pulse', 'element')
            with case_(2):
                play('second_pulse', 'element')
            with case_(3):
                play('third_pulse', 'element')
            with default_():
                play('other_pulse', 'element')
        ```
    """
    switch = _get_scope_as_switch_scope()
    if switch.if_statement is None:
        raise QmQuaException("must specify at least one case before 'default'.")

    if betterproto.serialized_on_wire(switch.if_statement.if_.else_):
        raise QmQuaException("only a single 'default' statement can follow a 'switch' statement")

    else_statement = _qua.QuaProgramStatementsCollection(statements=[])
    switch.if_statement.if_.else_ = else_statement
    return _BodyScope(_StatementsCollection(else_statement))


def if_(expression: QuaExpressionType, **kwargs) -> "_BodyScope":
    """If flow control statement in QUA.

    To be used with a context manager.

    The QUA code block following the statement will be
    executed only if the expression given evaluates to true.

    Args:
        expression: A boolean expression to evaluate

    Example:
        ```python
        x=declare(int)
        with if_(x>0):
            play('pulse', 'element')
        ```
    """
    if type(expression) == bool:
        expression = exp(expression)
    body = _get_scope_as_blocks_body()

    # support unsafe for serializer
    if_kwargs = {}
    unsafe_name = "unsafe"
    if kwargs.get(unsafe_name):
        if_kwargs[unsafe_name] = kwargs.get(unsafe_name)

    if_body = body.if_block(_unwrap_exp(expression), **if_kwargs)
    return _BodyScope(if_body)


def elif_(expression: QuaExpressionType) -> "_BodyScope":
    """Else-If flow control statement in QUA.

    To be used with a context manager.

    Must appear after an ``if_()`` statement.

    The QUA code block following the statement will be executed only if the expressions
    in the preceding ``if_()`` and ``elif_()`` statements evaluates to false and if the
    expression given in this ``elif_()`` evaluates to true.

    Args:
        expression: A boolean expression to evaluate

    Example:
        ```python
        x=declare(int)
        with if_(x>2):
            play('pulse', 'element')
        with elif_(x>-2):
            play('other_pulse', 'element')
        with else_():
            play('third_pulse', 'element')
        ```
    """
    body = _get_scope_as_blocks_body()
    last_statement = body.get_last_statement()
    if last_statement is None or betterproto.serialized_on_wire(last_statement.if_) is False:
        raise QmQuaException(
            "'elif' statement must directly follow 'if' statement - Please make sure it is aligned with the corresponding if statement."
        )

    if betterproto.serialized_on_wire(last_statement.if_.else_):
        raise QmQuaException("'elif' must come before 'else' statement")

    elseif = _qua.QuaProgramElseIf(
        loc=last_statement.if_.loc,
        condition=_unwrap_exp(expression),
        body=_qua.QuaProgramStatementsCollection(statements=[]),
    )
    last_statement.if_.elseifs.append(elseif)
    return _BodyScope(_StatementsCollection(elseif.body))


def else_() -> "_BodyScope":
    """Else flow control statement in QUA.

    To be used with a context manager.

    Must appear after an ``if_()`` statement.

    The QUA code block following the statement will be executed only if the expressions
    in the preceding ``if_()`` and ``elif_()`` statements evaluates to false.

    Example:
        ```python
        x=declare(int)
        with if_(x>0):
            play('pulse', 'element')
        with else_():
            play('other_pulse', 'element')
        ```
    """
    body = _get_scope_as_blocks_body()
    last_statement = body.get_last_statement()

    if last_statement is None or betterproto.serialized_on_wire(last_statement.if_) is False:
        raise QmQuaException(
            "'else' statement must directly follow 'if' statement - "
            "Please make sure it is aligned with the corresponding if statement."
        )

    if betterproto.serialized_on_wire(last_statement.if_.else_):
        raise QmQuaException("only a single 'else' statement can follow an 'if' statement")

    else_statement = _qua.QuaProgramStatementsCollection(statements=[])
    last_statement.if_.else_ = else_statement
    return _BodyScope(_StatementsCollection(else_statement))


def for_each_(var: OneOrMore[QuaVariableType], values: ForEachValuesType) -> "_BodyScope":
    """Flow control: Iterate over array elements in QUA.

    It is possible to either loop over one variable, or over a tuple of variables,
    similar to the `zip` style iteration in python.

    To be used with a context manager.

    Args:
        var (Union[QUA variable, tuple of QUA variables]): The iteration
            variable
        values (Union[list of literals, tuple of lists of literals, QUA array, tuple of QUA arrays]):
            A list of values to iterate over or a QUA array.

    Example:
        ```python
        x=declare(fixed)
        y=declare(fixed)
        with for_each_(x, [0.1, 0.4, 0.6]):
            play('pulse' * amp(x), 'element')
        with for_each_((x, y), ([0.1, 0.4, 0.6], [0.3, -0.2, 0.1])):
            play('pulse1' * amp(x), 'element')
            play('pulse2' * amp(y), 'element')
        ```

    Warning:

        This behavior is not exactly consistent with python `zip`.
        Instead of sending a list of tuple as values, the function expects a tuple of
        lists.
        The first list containing the values for the first variable, and so on.
    """
    body = _get_scope_as_blocks_body()
    # normalize the var argument
    if not _is_iter(var) or isinstance(var, QuaExpression):
        var = (var,)

    for i, v in enumerate(var):
        if not isinstance(v, QuaExpression):
            raise QmQuaException(f"for_each_ var {i} must be a variable")

    # normalize the values argument
    if isinstance(values, QuaExpression) or not _is_iter(values) or not _is_iter(values[0]):
        values = (values,)

    if _is_iter(values) and len(values) < 1:
        raise QmQuaException("values cannot be empty")

    arrays = []
    for value in values:
        if isinstance(value, QuaExpression):
            arrays.append(value)
        elif _is_iter(value):
            has_bool = collection_has_type_bool(value)
            has_int = collection_has_type_int(value)
            has_float = collection_has_type_float(value)

            if has_bool:
                if has_int or has_float:
                    raise QmQuaException("values can not contain both bool and number values")
                # Only booleans
                arrays.append(declare(bool, value=value))
            else:
                if has_float:
                    # All will be considered as fixed
                    arrays.append(declare(fixed, value=[float(x) for x in value]))
                else:
                    # Only ints
                    arrays.append(declare(int, value=value))
        else:
            raise QmQuaException("value is not a QUA array neither iterable")

    var = [_unwrap_var(exp(v)) for v in var]
    arrays = [a.unwrap() for a in arrays]

    if len(var) != len(arrays):
        raise QmQuaException("number of variables does not match number of array values")

    iterators = [(var[i], ar) for (i, ar) in enumerate(arrays)]

    foreach = body.for_each(iterators)
    return _BodyScope(foreach)


def while_(cond: QuaExpressionType = None) -> "_BodyScope":
    """While loop flow control statement in QUA.

    To be used with a context manager.

    Args:
        cond (QUA expression): an expression which evaluates to a
            boolean variable, determines if to continue to next loop
            iteration

    Example:
        ```python
        x = declare(int)
        assign(x, 0)
        with while_(x<=30):
            play('pulse', 'element')
            assign(x, x+1)
        ```
    """
    return for_(None, None, cond, None)


def for_(
    var: QuaVariableType = None,
    init: TypeOrExpression[PyNumberType] = None,
    cond: QuaExpressionType = None,
    update: QuaExpressionType = None,
) -> Union["_BodyScope", "_ForScope"]:
    """For loop flow control statement in QUA.

    To be used with a context manager.

    Args:
        var (QUA variable): QUA variable used as iteration variable
        init (QUA expression): an expression which sets the initial
            value of the iteration variable
        cond (QUA expression): an expression which evaluates to a
            boolean variable, determines if to continue to next loop
            iteration
        update (QUA expression): an expression to add to ``var`` with
            each loop iteration

    Example:
        ```python
        x = declare(fixed)
        with for_(var=x, init=0, cond=x<=1, update=x+0.1):
            play('pulse', 'element')
        ```
    """
    if var is None and init is None and cond is None and update is None:
        body = _get_scope_as_blocks_body()
        for_statement = body.for_block()
        return _ForScope(for_statement)
    else:
        body = _get_scope_as_blocks_body()
        for_statement = body.for_block()
        if var is not None and init is not None:
            for_statement.init = _qua.QuaProgramStatementsCollection(
                statements=[
                    _qua.QuaProgramAnyStatement(
                        assign=_qua.QuaProgramAssignmentStatement(
                            target=_unwrap_assign_target(exp(var)),
                            expression=_unwrap_exp(exp(init)),
                            loc=_get_loc(),
                        )
                    )
                ]
            )
        if var is not None and update is not None:
            for_statement.update = _qua.QuaProgramStatementsCollection(
                statements=[
                    _qua.QuaProgramAnyStatement(
                        assign=_qua.QuaProgramAssignmentStatement(
                            target=_unwrap_assign_target(exp(var)),
                            expression=_unwrap_exp(exp(update)),
                            loc=_get_loc(),
                        )
                    )
                ]
            )
        if cond is not None:
            for_statement.condition = _unwrap_exp(exp(cond))
        return _BodyScope(_StatementsCollection(for_statement.body))


def infinite_loop_() -> "_BodyScope":
    """Infinite loop flow control statement in QUA.

    To be used with a context manager.

    Optimized for zero latency between iterations,
    provided that no more than a single element appears in the loop.

    Note:
        In case multiple elements need to be used in an infinite loop, it is possible to add several loops
        in parallel (see example).
        Two infinite loops cannot share an element nor can they share variables.

    Example:
        ```python
        with infinite_loop_():
            play('pulse1', 'element1')
        with infinite_loop_():
            play('pulse2', 'element2')
        ```
    """
    body = _get_scope_as_blocks_body()
    for_statement = body.for_block()
    for_statement.condition = _unwrap_exp(exp(True))
    return _BodyScope(_StatementsCollection(for_statement.body))


def port_condition(condition: QuaExpressionType = None) -> "_BodyScope":
    body = _get_scope_as_blocks_body()
    return _BodyScope(PortConditionedStatementsCollection(body._body, condition=_unwrap_exp(exp(condition))))


def L(value) -> MessageExpressionType:
    """Creates an expression with a literal value

    Args:
        value: int, float or bool to wrap in a literal expression
    """
    if type(value) is bool:
        return literal_bool(value)
    elif type(value) is int:
        return literal_int(value)
    elif type(value) is float:
        return literal_real(value)
    else:
        raise QmQuaException("literal can be bool, int or float")


class DeclarationType(_Enum):
    EmptyScalar = 0
    InitScalar = 1
    EmptyArray = 2
    InitArray = 3


def _declare(
    t: VariableDeclarationType,
    is_input_stream: bool,
    value: Optional[OneOrMore[AllPyTypes]] = None,
    size: Optional[PyNumberType] = None,
    name: Optional[str] = None,
) -> QuaVariableType:
    if size is not None:
        size = size.item() if isinstance(size, np.integer) else size
        if not (isinstance(size, int) and size > 0):
            raise QmQuaException("size must be a positive integer")
        if value is not None:
            raise QmQuaException("size declaration cannot be made if value is declared")
        dec_type = DeclarationType.EmptyArray
    else:
        if value is None:
            dec_type = DeclarationType.EmptyScalar
        elif isinstance(value, Iterable):
            dec_type = DeclarationType.InitArray
        else:
            dec_type = DeclarationType.InitScalar

    expression_value: OneOrMore[_qua.QuaProgramLiteralExpression] = []

    if dec_type == DeclarationType.InitArray:
        mem_size = len(value)
        new_value = []
        for val in value:
            new_value.append(to_expression(val).literal)
        expression_value = new_value
        dim = 1
    elif dec_type == DeclarationType.InitScalar:
        mem_size = 1
        expression_value = to_expression(value).literal
        dim = 0
    elif dec_type == DeclarationType.EmptyArray:
        mem_size = size
        dim = 1
    else:
        mem_size = 1
        dim = 0

    scope = _get_root_program_scope()

    if dec_type == DeclarationType.EmptyArray or dec_type == DeclarationType.InitArray:
        if is_input_stream:
            if name is not None:
                var = create_input_stream_name(name)
                if var in scope.declared_input_streams:
                    raise QmQuaException("input stream already declared")
                scope.declared_input_streams.add(var)
            else:
                raise QmQuaException("input stream declared without a name")
        else:
            scope.array_index += 1
            var = f"a{scope.array_index}"
        result = _qua.QuaProgramArrayVarRefExpression(name=var)
    else:
        if is_input_stream:
            if name is not None:
                var = create_input_stream_name(name)
                if var in scope.declared_input_streams:
                    raise QmQuaException("input stream already declared")
                scope.declared_input_streams.add(var)
            else:
                raise QmQuaException("input stream declared without a name")
        else:
            scope.var_index += 1
            var = f"v{scope.var_index}"
        result = _qua.QuaProgramAnyScalarExpression(variable=_qua.QuaProgramVarRefExpression(name=var))

    prog = scope.program
    if t == int:
        prog.declare_int(var, mem_size, expression_value, dim, is_input_stream)
    elif t == bool:
        prog.declare_bool(var, mem_size, expression_value, dim, is_input_stream)
    elif t == float:
        t = fixed
        prog.declare_real(var, mem_size, expression_value, dim, is_input_stream)
    elif t == fixed:
        prog.declare_real(var, mem_size, expression_value, dim, is_input_stream)
    else:
        raise QmQuaException("only int, fixed or bool variables are supported")

    return QuaVariable(result, t)


def declare(
    t: VariableDeclarationType,
    value: Optional[OneOrMore[AllPyTypes]] = None,
    size: Optional[PyNumberType] = None,
) -> QuaVariableType:
    r"""Declare a single QUA variable or QUA vector to be used in subsequent expressions and assignments.

    Declaration is performed by declaring a python variable with the return value of this function.

    Args:
        t: The type of QUA variable. Possible values: ``int``,
            ``fixed``, ``bool``, where:

            ``int``
                a signed 32-bit number
            ``fixed``
                a signed 4.28 fixed point number
            ``bool``
                either ``True`` or ``False``
        value: An initial value for the variable or a list of initial
            values for a vector
        size: If declaring a vector without explicitly specifying a
            value, this parameter is used to specify the length of the
            array

    Returns:
        The variable or vector

    Warning:

        some QUA statements accept a variable with a valid range smaller than the full size of the generic
        QUA variable. For example, ``amp()`` accepts numbers between -2 and 2.
        In case the value stored in the variable is larger than the valid input range, unexpected results
        may occur.

    Example:
        ```python
        a = declare(fixed, value=0.3)
        play('pulse' * amp(a), 'element')

        array1 = declare(int, value=[1, 2, 3])
        array2 = declare(fixed, size=5)
        ```
    """
    return _declare(t, is_input_stream=False, value=value, size=size)


def declare_input_stream(t: VariableDeclarationType, name: str, **kwargs) -> QuaVariableType:
    """Declare a QUA variable or a QUA vector to be used as an input stream from the job to the QUA program.

    Declaration is performed by declaring a python variable with the return value of this function.

    Declaration is similar to the normal QUA variable declaration. See [declare](qm.qua._dsl.declare) for available
    parameters.

    See [Input streams](../../../Guides/features/#input-streams) for more information.

    -- Available from QOP 2.0 --

    Example:
        ```python
        tau = declare_input_stream(int)
        ...
        advance_input_stream(tau)
        play('operation', 'element', duration=tau)
        ```
    """

    return _declare(t, is_input_stream=True, name=name, **kwargs)


def advance_input_stream(input_stream: QuaExpressionType):
    """Advances the input stream pointer to the next available variable/vector.

    If there is no new data waiting in the stream, this command will wait until it is available.

    The variable/vector can then be used as a normal QUA variable.

    See [Input streams](../../../Guides/features/#input-streams) for more information.

    -- Available from QOP 2.0 --
    """

    body = _get_scope_as_blocks_body()
    body.advance_input_stream(_unwrap_exp(input_stream))


def declare_stream(**kwargs) -> "_ResultSource":
    """Declare a QUA output stream to be used in subsequent statements
    To retrieve the result - it must be saved in the stream processing block.

    Declaration is performed by declaring a python variable with the return value of this function.

    Note:
        if the stream is an ADC trace, declaring it with the syntax ``declare_stream(adc_trace=True)``
        will add a buffer of length corresponding to the pulse length.

    Returns:
        A :class:`_ResultSource` object to be used in
        [`stream_processing`][qm.qua._dsl.stream_processing]

    Example:
        ```python
        a = declare_stream()
        measure('pulse', 'element', a)

        with stream_processing():
            a.save("tag")
            a.save_all("another tag")
        ```
    """
    is_adc_trace: bool = kwargs.get("adc_trace", False)

    scope = _get_root_program_scope()
    scope.result_index += 1
    var = f"r{scope.result_index}"
    if is_adc_trace:
        var = "atr_" + var

    return _ResultSource(
        _ResultSourceConfiguration(
            var_name=var,
            timestamp_mode=_ResultSourceTimestampMode.Values,
            is_adc_trace=is_adc_trace,
            input=-1,
            auto_reshape=False,
        )
    )


class _PulseAmp:
    def __init__(
        self,
        v1: MessageExpressionType,
        v2: MessageExpressionType,
        v3: MessageExpressionType,
        v4: MessageExpressionType,
    ):
        if v1 is None:
            raise QmQuaException("amp can be one value or a matrix of 4")
        if v2 is None and v3 is None and v4 is None:
            pass
        elif v2 is not None and v3 is not None and v4 is not None:
            pass
        else:
            raise QmQuaException("amp can be one value or a matrix of 4.")

        self.v1 = v1
        self.v2 = v2
        self.v3 = v3
        self.v4 = v4

    def value(self) -> AmpValuesType:
        return self.v1, self.v2, self.v3, self.v4

    def __rmul__(self, other: str) -> Tuple[str, AmpValuesType]:
        return self * other

    def __mul__(self, other: str) -> Tuple[str, AmpValuesType]:
        if type(other) is not str:
            raise QmQuaException("you can multiply only a pulse")
        return other, self.value()


def amp(
    v1: QuaNumberType,
    v2: Optional[QuaNumberType] = None,
    v3: Optional[QuaNumberType] = None,
    v4: Optional[QuaNumberType] = None,
) -> _PulseAmp:
    """To be used only within a [play][qm.qua._dsl.play] or [measure][qm.qua._dsl.measure] command, as a multiplication to
    the `operation`.

    It is possible to scale the pulse's amplitude dynamically by using the following syntax:

    ``play('pulse_name' * amp(v), 'element')``

    where ``v`` is QUA variable of type fixed. Range of v: -2 to $2 - 2^{-16}$ in steps of $2^{-16}$.

    Moreover, if the pulse is intended to a mixedInputs element and thus is defined with two waveforms,
    the two waveforms, described as a column vector, can be multiplied by a matrix:

    ``play('pulse_name' * amp(v_00, v_01, v_10, v_11), 'element'),``

    where ``v_ij``, i,j={0,1}, are QUA variables of type fixed.
    Note that ``v_ij`` should satisfy -2 <= ``v_ij`` <= $2 - 2{-16}$.

    Note that scaling in this manner, rather than in the configuration, might result
    in a computational overhead.
    See [QUA Best Practice Guide](../../../Guides/best_practices/#general) for more information.

    Args:
        v1: If only this variable is given, it is the scaler amplitude
            factor which multiples the `pulse` associated with the
            `operation`. If all variables are given, then it is the
            first element in the amplitude matrix which multiples the
            `pulse` associated with the `operation`.
        v2: The second element in the amplitude matrix which multiples
            the `pulse` associated with the `operation`.
        v3: The third element in the amplitude matrix which multiples
            the `pulse` associated with the `operation`.
        v4: The forth element in the amplitude matrix which multiples
            the `pulse` associated with the `operation`.
    """
    variables: List[MessageExpressionType] = [_unwrap_exp(exp(v)) if v is not None else None for v in [v1, v2, v3, v4]]
    return _PulseAmp(*variables)


def _assert_scalar_expression(value: QuaExpression):
    if not isinstance(_unwrap_exp(value), _qua.QuaProgramAnyScalarExpression):
        raise QmQuaException(f"invalid expression: '{value}' is not a scalar expression")


def _assert_not_lib_expression(value: QuaExpression):
    expression = _unwrap_exp(value)
    if (
        isinstance(expression, _qua.QuaProgramAnyScalarExpression)
        and betterproto.which_one_of(expression, "expression_oneof")[0] == "lib_function"
    ):
        raise QmQuaException(
            f"library expression {str(value)} is not a valid save source."
            f" Assign the value to a variable before saving it"
        )


def ramp(v) -> _qua.QuaProgramRampPulse:
    """To be used only within a [`play`][qm.qua._dsl.play] command, instead of the `operation`.

    It’s possible to generate a voltage ramp by using the `ramp(slope)` command.
    The slope argument is specified in units of `V/ns`. Usage of this feature is as follows:

    ``play(ramp(0.0001),'qe1',duration=1000)``

    .. note:
        The pulse duration must be specified if the ramp feature is used.

    Args:
        v: The slope in units of `V/ns`
    """
    value = _unwrap_exp(exp(v))
    _assert_scalar_expression(exp(v))
    result = _qua.QuaProgramRampPulse(value=value)
    return result


def exp(value: AllQuaTypes) -> QuaExpressionType:
    return QuaExpression(to_expression(value))


class _BaseScope:
    def __enter__(self):
        global _block_stack
        _block_stack.append(self)
        return None

    def __exit__(self, exc_type, exc_val, exc_tb):
        global _block_stack
        if _block_stack[-1] != self:
            raise QmQuaException("Unexpected stack structure")
        _block_stack.remove(self)
        return False


class _BodyScope(_BaseScope):
    def __init__(self, body: Optional[_StatementsCollection]):
        super().__init__()
        self._body = body

    def body(self) -> _StatementsCollection:
        return self._body


class _ProgramScope(_BodyScope):
    def __init__(self, _program: "Program"):
        super().__init__(_program.body)
        self._program = _program
        self.var_index = 0
        self.array_index = 0
        self.result_index = 0
        self.declared_input_streams: Set[str] = set()
        self._declared_streams: Dict[str, _ResultSource] = {}

    def __enter__(self) -> "Program":
        super().__enter__()
        self._program.set_in_scope()
        return self._program

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._program.result_analysis.generate_proto()
        self._program.set_exit_scope()
        return super().__exit__(exc_type, exc_val, exc_tb)

    @property
    def program(self) -> "Program":
        return self._program

    def declare_legacy_adc(self, tag: str) -> "_ResultSource":
        result_object = self._declared_streams.get(tag, None)
        if result_object is None:
            result_object = declare_stream(adc_trace=True)
            self._declared_streams[tag] = result_object

            ra = _get_scope_as_result_analysis()
            ra.auto_save_all(tag + "_input1", result_object.input1())
            ra.auto_save_all(
                tag + "_input1" + _TIMESTAMPS_LEGACY_SUFFIX,
                result_object.input1().timestamps(),
            )
            ra.auto_save_all(tag + "_input2", result_object.input2())
            ra.auto_save_all(
                tag + "_input2" + _TIMESTAMPS_LEGACY_SUFFIX,
                result_object.input2().timestamps(),
            )

        return result_object

    def declare_legacy_save(self, tag: str) -> "_ResultSource":
        result_object = self.declare_save(tag, add_legacy_timestamp=True)
        return result_object

    def declare_save(self, tag: str, add_legacy_timestamp: bool = False) -> "_ResultSource":
        result_object = self._declared_streams.get(tag, None)
        if result_object is None:
            result_object = declare_stream()
            self._declared_streams[tag] = result_object

            ra = _get_scope_as_result_analysis()
            ra.auto_save_all(tag, result_object)
            if add_legacy_timestamp:
                ra.auto_save_all(tag + _TIMESTAMPS_LEGACY_SUFFIX, result_object.timestamps())
        return result_object


class _ForScope(_BodyScope):
    def __init__(self, for_statement: _qua.QuaProgramForStatement):
        super().__init__(None)
        self._for_statement = for_statement

    def body(self):
        raise QmQuaException("for must be used with for_init, for_update, for_body and for_cond")

    def for_statement(self) -> _qua.QuaProgramForStatement:
        return self._for_statement


class _SwitchScope(_BaseScope):
    def __init__(self, expression: QuaExpression, container: _StatementsCollection, unsafe: bool):
        super().__init__()
        self.expression = expression
        self.if_statement: Optional[_qua.QuaProgramAnyStatement] = None
        self.container = container
        self.unsafe = unsafe


def strict_timing_() -> _BodyScope:
    """Any QUA command written within the strict timing block will be required to play without gaps.

    See [the documentation](../../../Guides/timing_in_qua/#strict-timing) for further information and examples.

    To be used with a context manager.

    -- Available from QOP 2.0 --
    """

    body = _get_scope_as_blocks_body()
    strict_timing_statement = body.strict_timing_block()
    return _BodyScope(_StatementsCollection(strict_timing_statement.body))


class _RAScope(_BaseScope):
    def __init__(self, ra: _ResultAnalysis):
        super().__init__()
        self._ra = ra

    def __enter__(self):
        super().__enter__()
        return self._ra

    def result_analysis(self) -> _ResultAnalysis:
        return self._ra


def _get_root_program_scope() -> _ProgramScope:
    global _block_stack
    first_block = _block_stack[0]
    if not isinstance(first_block, _ProgramScope):
        raise QmQuaException("Expecting program scope")
    return first_block


def _get_scope_as_program() -> "Program":
    global _block_stack
    last_block = _block_stack[-1]
    if not isinstance(last_block, _ProgramScope):
        raise QmQuaException("Expecting program scope")
    return last_block.program


def _get_scope_as_for() -> _qua.QuaProgramForStatement:
    global _block_stack
    last_block = _block_stack[-1]
    if not isinstance(last_block, _ForScope):
        raise QmQuaException("Expecting for scope")
    return last_block.for_statement()


def _get_scope_as_blocks_body() -> _StatementsCollection:
    global _block_stack
    last_block = _block_stack[-1]
    if not isinstance(last_block, _BodyScope):
        raise QmQuaException("Expecting scope with body.")
    return last_block.body()


def _get_scope_as_switch_scope() -> _SwitchScope:
    global _block_stack
    last_block = _block_stack[-1]
    if not isinstance(last_block, _SwitchScope):
        raise QmQuaException("Expecting switch scope")
    return last_block


def _get_scope_as_result_analysis() -> _ResultAnalysis:
    global _block_stack
    return _get_root_program_scope().program.result_analysis


def _unwrap_exp(expression: QuaExpression) -> MessageVariableOrExpression:
    if not isinstance(expression, QuaExpression):
        raise QmQuaException("invalid expression: " + str(expression))
    return expression.unwrap()


def _unwrap_var(expression: QuaExpression) -> MessageVarType:
    var = _unwrap_exp(expression)
    if type(var) is not _qua.QuaProgramAnyScalarExpression:
        raise QmQuaException("invalid expression: " + str(expression))
    return var.variable


def _unwrap_array_cell(
    expression: QuaExpression,
) -> _qua.QuaProgramArrayCellRefExpression:
    var = _unwrap_exp(expression)
    if type(var) is not _qua.QuaProgramAnyScalarExpression:
        raise QmQuaException("invalid expression: " + str(expression))
    return var.array_cell


def _unwrap_assign_target(
    expression: QuaExpression,
) -> _qua.QuaProgramAssignmentStatementTarget:
    result = _qua.QuaProgramAssignmentStatementTarget()

    target = _unwrap_exp(expression)
    if type(target) is _qua.QuaProgramAnyScalarExpression:
        one_of, found = betterproto.which_one_of(target, "expression_oneof")
        if one_of == "array_cell":
            result.array_cell = target.array_cell
        elif one_of == "variable":
            result.variable = target.variable
        else:
            raise QmQuaException("invalid target expression: " + str(expression))
    # We don't support whole array assignment for now
    # elif type(target) is _Q.ArrayVarRefExpression:
    #     result.arrayVar.CopyFrom(target.arrayVar)
    else:
        raise QmQuaException("invalid target expression: " + str(expression))

    return result


def _unwrap_save_source(expression: QuaExpression) -> _qua.QuaProgramSaveStatementSource:
    result = _qua.QuaProgramSaveStatementSource()

    source = _unwrap_exp(expression)
    _assert_scalar_expression(expression)
    _assert_not_lib_expression(expression)
    one_of, found = betterproto.which_one_of(source, "expression_oneof")
    if one_of == "array_cell":
        result.array_cell = source.array_cell
    elif one_of == "variable":
        result.variable = source.variable
    elif one_of == "literal":
        result.literal = source.literal
    else:
        raise QmQuaException("invalid source expression: " + str(expression))

    return result


def _unwrap_outer_target(analog_process_target: AnalogProcessTargetType) -> _qua.QuaProgramAnalogProcessTarget:
    outer_target = _qua.QuaProgramAnalogProcessTarget()
    if isinstance(analog_process_target, ScalarProcessTarget):
        target = _qua.QuaProgramAnalogProcessTargetScalarProcessTarget()
        target_exp = _unwrap_exp(analog_process_target.target)
        if not isinstance(target_exp, _qua.QuaProgramAnyScalarExpression):
            raise QmQuaException(f"Unknown type - {type(target_exp)}")

        target_type, found = betterproto.which_one_of(target_exp, "expression_oneof")
        if target_type == "variable":
            target.variable = target_exp.variable
        elif target_type == "array_cell":
            target.array_cell = target_exp.array_cell
        else:
            raise QmQuaException(f"Unknown target type - {target_type}")
        outer_target.scalar_process = target

    elif isinstance(analog_process_target, VectorProcessTarget):
        target = _qua.QuaProgramAnalogProcessTargetVectorProcessTarget(
            array=_unwrap_exp(analog_process_target.target),
            time_division=_qua.QuaProgramAnalogProcessTargetTimeDivision().from_dict(
                _unwrap_time_division(analog_process_target.time_division).to_dict()
            ),
        )
        outer_target.vector_process = target
    else:
        raise QmQuaException(f"Unknown type - {type(analog_process_target)}")
    return outer_target


def _unwrap_analog_process(
    analog_process: AnalogMeasureProcess,
) -> _qua.QuaProgramAnalogMeasureProcess:
    result = _qua.QuaProgramAnalogMeasureProcess(loc=analog_process.loc)

    if isinstance(analog_process, BareIntegration):
        result.bare_integration = _qua.QuaProgramAnalogMeasureProcessBareIntegration(
            integration=_qua.QuaProgramIntegrationWeightReference(name=analog_process.iw),
            element_output=analog_process.element_output,
            target=_unwrap_outer_target(analog_process.target),
        )
    elif isinstance(analog_process, DualBareIntegration):
        result.dual_bare_integration = _qua.QuaProgramAnalogMeasureProcessDualBareIntegration(
            integration1=_qua.QuaProgramIntegrationWeightReference(name=analog_process.iw1),
            integration2=_qua.QuaProgramIntegrationWeightReference(name=analog_process.iw2),
            element_output1=analog_process.element_output1,
            element_output2=analog_process.element_output2,
            target=_unwrap_outer_target(analog_process.target),
        )
    elif isinstance(analog_process, DemodIntegration):
        result.demod_integration = _qua.QuaProgramAnalogMeasureProcessDemodIntegration(
            integration=_qua.QuaProgramIntegrationWeightReference(name=analog_process.iw),
            element_output=analog_process.element_output,
            target=_unwrap_outer_target(analog_process.target),
        )
    elif isinstance(analog_process, DualDemodIntegration):
        result.dual_demod_integration = _qua.QuaProgramAnalogMeasureProcessDualDemodIntegration(
            integration1=_qua.QuaProgramIntegrationWeightReference(name=analog_process.iw1),
            integration2=_qua.QuaProgramIntegrationWeightReference(name=analog_process.iw2),
            element_output1=analog_process.element_output1,
            element_output2=analog_process.element_output2,
            target=_unwrap_outer_target(analog_process.target),
        )
    elif isinstance(analog_process, AnalogRawTimeTagging):
        result.raw_time_tagging = _qua.QuaProgramAnalogMeasureProcessRawTimeTagging(
            max_time=int(analog_process.max_time),
            element_output=analog_process.element_output,
            target=_unwrap_exp(analog_process.target),
        )
        if analog_process.targetLen is not None:
            result.raw_time_tagging.target_len = _unwrap_exp(analog_process.targetLen).variable

    elif isinstance(analog_process, HighResTimeTagging):
        result.high_res_time_tagging = _qua.QuaProgramAnalogMeasureProcessHighResTimeTagging(
            max_time=int(analog_process.max_time),
            element_output=analog_process.element_output,
            target=_unwrap_exp(analog_process.target),
        )
        if analog_process.targetLen is not None:
            result.high_res_time_tagging.target_len = _unwrap_exp(analog_process.targetLen).variable

    return result


def _unwrap_digital_process(
    digital_process: DigitalMeasureProcess,
) -> _qua.QuaProgramDigitalMeasureProcess:
    result = _qua.QuaProgramDigitalMeasureProcess(loc=digital_process.loc)

    if isinstance(digital_process, DigitalRawTimeTagging):
        result.raw_time_tagging = _qua.QuaProgramDigitalMeasureProcessRawTimeTagging(
            max_time=int(digital_process.max_time),
            element_output=digital_process.element_output,
            target=_unwrap_exp(digital_process.target),
        )
        if digital_process.targetLen is not None:
            result.raw_time_tagging.target_len = _unwrap_exp(digital_process.targetLen).variable

    elif isinstance(digital_process, DigitalMeasureProcessCounting):
        result.counting = _qua.QuaProgramDigitalMeasureProcessCounting(
            max_time=int(digital_process.max_time),
            target=_unwrap_exp(digital_process.target).variable,
        )
        if type(digital_process.element_outputs) == tuple:
            result.counting.element_outputs.extend(digital_process.element_outputs)
        elif type(digital_process.element_outputs) == str:
            result.counting.element_outputs.append(digital_process.element_outputs)

    return result


def _unwrap_measure_process(
    process: MeasureProcessType,
) -> _qua.QuaProgramMeasureProcess():
    result = _qua.QuaProgramMeasureProcess()

    if isinstance(process, AnalogMeasureProcess):
        result.analog = _unwrap_analog_process(process)
    elif isinstance(process, DigitalMeasureProcess):
        result.digital = _unwrap_digital_process(process)

    return result


def _unwrap_time_division(
    time_division: TimeDivisionType,
) -> _qua.QuaProgramAnalogProcessTargetTimeDivision:
    result = _qua.QuaProgramAnalogProcessTargetTimeDivision()

    if isinstance(time_division, SlicedAnalogTimeDivision):
        result.sliced = _qua.QuaProgramAnalogTimeDivisionSliced(samples_per_chunk=time_division.samples_per_chunk)
    elif isinstance(time_division, AccumulatedAnalogTimeDivision):
        result.accumulated = _qua.QuaProgramAnalogTimeDivisionAccumulated(
            samples_per_chunk=time_division.samples_per_chunk
        )
    elif isinstance(time_division, MovingWindowAnalogTimeDivision):
        result.moving_window = _qua.QuaProgramAnalogTimeDivisionMovingWindow(
            samples_per_chunk=time_division.samples_per_chunk,
            chunks_per_window=time_division.chunks_per_window,
        )
    return result


class AccumulationMethod:
    def __init__(self):
        self.loc = ""
        self.return_func: Type[AnalogMeasureProcess] = None

    def _full_target(self, target: QuaVariableType) -> ScalarProcessTarget:
        return ScalarProcessTarget(self.loc, target)

    def _sliced_target(self, target: QuaVariableType, samples_per_chunk: int) -> VectorProcessTarget:
        analog_time_division = SlicedAnalogTimeDivision(self.loc, samples_per_chunk)
        return VectorProcessTarget(self.loc, target, analog_time_division)

    def _accumulated_target(self, target: QuaVariableType, samples_per_chunk: int) -> VectorProcessTarget:
        analog_time_division = AccumulatedAnalogTimeDivision(self.loc, samples_per_chunk)
        return VectorProcessTarget(self.loc, target, analog_time_division)

    def _moving_window_target(
        self, target: QuaVariableType, samples_per_chunk: int, chunks_per_window: int
    ) -> VectorProcessTarget:
        analog_time_division = MovingWindowAnalogTimeDivision(self.loc, samples_per_chunk, chunks_per_window)
        return VectorProcessTarget(self.loc, target, analog_time_division)


class RealAccumulationMethod(AccumulationMethod):
    """A base class for specifying the integration and demodulation processes in the [measure][qm.qua._dsl.measure]
    statement.
    These are the options which can be used inside the measure command as part of the ``demod`` and ``integration``
    processes.
    """

    def __init__(self):
        super().__init__()

    def __new__(cls):
        if cls is AccumulationMethod:
            raise TypeError("base class may not be instantiated")
        return object.__new__(cls)

    def full(self, iw: str, target: QuaVariableType, element_output: str = ""):
        """Perform an ordinary demodulation/integration. See [Full demodulation](../../../Guides/features/#full-demodulation).

        Args:
            iw (str): integration weights
            target (QUA variable): variable to which demod result is
                saved
            element_output: (optional) the output of an element from
                which to get ADC results
        """
        return self.return_func(self.loc, element_output, iw, self._full_target(target))

    def sliced(
        self,
        iw: str,
        target: QuaVariableType,
        samples_per_chunk: int,
        element_output: str = "",
    ):
        """Perform a demodulation/integration in which the demodulation/integration process is split into chunks
        and the value of each chunk is saved in an array cell. See [Sliced demodulation](../../../Guides/features/#sliced-demodulation).

        Args:
            iw (str): integration weights
            target (QUA array): variable to which demod result is saved
            samples_per_chunk (int): The number of ADC samples to be
                used for each chunk is this number times 4.
            element_output: (optional) the output of an element from
                which to get ADC results
        """
        return self.return_func(self.loc, element_output, iw, self._sliced_target(target, samples_per_chunk))

    def accumulated(
        self,
        iw: str,
        target: QuaVariableType,
        samples_per_chunk: int,
        element_output: str = "",
    ):
        """Same as ``sliced()``, however the accumulated result of the demodulation/integration
        is saved in each array cell. See [Accumulated demodulation](../../../Guides/features/#accumulated-demodulation).

        Args:
            iw (str): integration weights
            target (QUA array): variable to which demod result is saved
            samples_per_chunk (int): The number of ADC samples to be
                used for each chunk is this number times 4.
            element_output: (optional) the output of an element from
                which to get ADC results
        """
        return self.return_func(
            self.loc,
            element_output,
            iw,
            self._accumulated_target(target, samples_per_chunk),
        )

    def moving_window(
        self,
        iw: str,
        target: QuaVariableType,
        samples_per_chunk: int,
        chunks_per_window: int,
        element_output: str = "",
    ):
        """Same as ``sliced()``, however the several chunks are accumulated and saved to each array cell.
        See [Moving window demodulation](../../../Guides/features/#moving-window-demodulation).

        Args:
            iw (str): integration weights
            target (QUA array): variable to which demod result is saved
            samples_per_chunk (int): The number of ADC samples to be
                used for each chunk is this number times 4.
            chunks_per_window (int): The number of chunks to use in the
                moving window
            element_output: (optional) the output of an element from
                which to get ADC results
        """
        return self.return_func(
            self.loc,
            element_output,
            iw,
            self._moving_window_target(target, samples_per_chunk, chunks_per_window),
        )


class DualAccumulationMethod(AccumulationMethod):
    """A base class for specifying the dual integration and demodulation processes in the :func:`measure`
    statement.
    These are the options which can be used inside the measure command as part of the ``dual_demod`` and
    ``dual_integration`` processes.
    """

    def __init__(self):
        super().__init__()

    def __new__(cls):
        if cls is AccumulationMethod:
            raise TypeError("base class may not be instantiated")
        return object.__new__(cls)

    @overload
    def full(
        self,
        iw1: str,
        iw2: str,
        target: QuaVariableType,
    ):
        pass

    @overload
    def full(
        self,
        iw1: str,
        element_output1: str,
        iw2: str,
        element_output2: str,
        target: QuaVariableType,
    ):
        pass

    def full(self, *args, **kwargs):
        """Perform an ordinary dual demodulation/integration. See [Dual demodulation](../../../Guides/demod/#dual-demodulation).

        Args:
            iw1 (str): integration weights to be applied to
                element_output1
            element_output1 (str): the output of an element from which
                to get ADC results
            iw2 (str): integration weights to be applied to
                element_output2
            element_output2 (str): the output of an element from which
                to get ADC results
            target (QUA variable): variable to which demod result is
                saved
        """
        if len(args) + len(kwargs) == 3:
            kwargs.update(_make_dict_from_args(args, ["iw1", "iw2", "target"]))
            kwargs["element_output1"] = DEFAULT_OUT1
            kwargs["element_output2"] = DEFAULT_OUT2
            return self.full(**kwargs)
        elif len(args) + len(kwargs) == 5:
            kwargs.update(_make_dict_from_args(args, ["iw1", "element_output1", "iw2", "element_output2", "target"]))
        else:
            raise QmQuaException("Invalid number of arguments")

        return self.return_func(
            self.loc,
            kwargs["element_output1"],
            kwargs["element_output2"],
            kwargs["iw1"],
            kwargs["iw2"],
            self._full_target(kwargs["target"]),
        )

    @overload
    def sliced(
        self,
        iw1: str,
        iw2: str,
        samples_per_chunk: int,
        target: QuaVariableType,
    ):
        pass

    @overload
    def sliced(
        self,
        iw1: str,
        element_output1: str,
        iw2: str,
        element_output2: str,
        samples_per_chunk: int,
        target: QuaVariableType,
    ):
        pass

    def sliced(self, *args, **kwargs):
        """This feature is currently not supported in QUA"""
        if len(args) + len(kwargs) == 4:
            kwargs.update(_make_dict_from_args(args, ["iw1", "iw2", "samples_per_chunk", "target"]))
            kwargs["element_output1"] = DEFAULT_OUT1
            kwargs["element_output2"] = DEFAULT_OUT2
            return self.sliced(**kwargs)
        elif len(args) + len(kwargs) == 6:
            kwargs.update(
                _make_dict_from_args(
                    args,
                    ["iw1", "element_output1", "iw2", "element_output2", "samples_per_chunk", "target"],
                )
            )
        else:
            raise QmQuaException("Invalid number of arguments")

        return self.return_func(
            self.loc,
            kwargs["element_output1"],
            kwargs["element_output2"],
            kwargs["iw1"],
            kwargs["iw2"],
            self._sliced_target(kwargs["target"], kwargs["samples_per_chunk"]),
        )

    @overload
    def accumulated(
        self,
        iw1: str,
        iw2: str,
        samples_per_chunk: int,
        target: QuaVariableType,
    ):
        pass

    @overload
    def accumulated(
        self,
        iw1: str,
        element_output1: str,
        iw2: str,
        element_output2: str,
        samples_per_chunk: int,
        target: QuaVariableType,
    ):
        pass

    def accumulated(self, *args, **kwargs):
        """This feature is currently not supported in QUA"""
        if len(args) + len(kwargs) == 4:
            kwargs.update(_make_dict_from_args(args, ["iw1", "iw2", "samples_per_chunk", "target"]))
            kwargs["element_output1"] = DEFAULT_OUT1
            kwargs["element_output2"] = DEFAULT_OUT2
            return self.accumulated(**kwargs)
        elif len(args) + len(kwargs) == 6:
            kwargs.update(
                _make_dict_from_args(
                    args,
                    ["iw1", "element_output1", "iw2", "element_output2", "samples_per_chunk", "target"],
                )
            )
        else:
            raise QmQuaException("Invalid number of arguments")

        return self.return_func(
            self.loc,
            kwargs["element_output1"],
            kwargs["element_output2"],
            kwargs["iw1"],
            kwargs["iw2"],
            self._accumulated_target(kwargs["target"], kwargs["samples_per_chunk"]),
        )

    @overload
    def moving_window(
        self,
        iw1: str,
        iw2: str,
        samples_per_chunk: int,
        chunks_per_window: int,
        target: QuaVariableType,
    ):
        pass

    @overload
    def moving_window(
        self,
        iw1: str,
        element_output1: str,
        iw2: str,
        element_output2: str,
        samples_per_chunk: int,
        chunks_per_window: int,
        target: QuaVariableType,
    ):
        pass

    def moving_window(self, *args, **kwargs):
        """This feature is currently not supported in QUA"""
        if len(args) + len(kwargs) == 5:
            kwargs.update(
                _make_dict_from_args(args, ["iw1", "iw2", "samples_per_chunk", "chunks_per_window", "target"])
            )
            kwargs["element_output1"] = DEFAULT_OUT1
            kwargs["element_output2"] = DEFAULT_OUT2
            return self.moving_window(**kwargs)
        elif len(args) + len(kwargs) == 7:
            kwargs.update(
                _make_dict_from_args(
                    args,
                    [
                        "iw1",
                        "element_output1",
                        "iw2",
                        "element_output2",
                        "samples_per_chunk",
                        "chunks_per_window",
                        "target",
                    ],
                )
            )
        else:
            raise QmQuaException("Invalid number of arguments")

        return self.return_func(
            self.loc,
            kwargs["element_output1"],
            kwargs["element_output2"],
            kwargs["iw1"],
            kwargs["iw2"],
            self._moving_window_target(kwargs["target"], kwargs["samples_per_chunk"], kwargs["chunks_per_window"]),
        )


class _Demod(RealAccumulationMethod):
    def __init__(self):
        super().__init__()
        self.loc = ""
        self.return_func = DemodIntegration


class _BareIntegration(RealAccumulationMethod):
    def __init__(self):
        super().__init__()
        self.loc = ""
        self.return_func = BareIntegration


class _DualDemod(DualAccumulationMethod):
    def __init__(self):
        super().__init__()
        self.loc = ""
        self.return_func = DualDemodIntegration


class _DualBareIntegration(DualAccumulationMethod):
    def __init__(self):
        super().__init__()
        self.loc = ""
        self.return_func = DualBareIntegration


class TimeTagging:
    """A base class for specifying the time tagging process in the [measure][qm.qua._dsl.measure] statement.
    These are the options which can be used inside the measure command as part of the ``time_tagging`` process.
    """

    def __init__(self):
        self.loc = ""

    def analog(
        self,
        target: QuaVariableType,
        max_time: int,
        targetLen: Optional[QuaNumberType] = None,
        element_output: str = "",
    ):
        """Performs time tagging. See [Time tagging](../../../Guides/features/#time-tagging).

        Args:
            target (QUA array of type int): The QUA array into which the
                times of the detected pulses are saved (in ns)
            max_time (int): The time in which pulses are detected
                (Must be larger than the pulse duration)
            targetLen (QUA int): A QUA int which will get the number of
                pulses detected
            element_output (str): the output of an element from which to
                get the pulses
        """
        return AnalogRawTimeTagging(self.loc, element_output, target, targetLen, max_time)

    def digital(
        self,
        target: QuaVariableType,
        max_time: int,
        targetLen: Optional[QuaNumberType] = None,
        element_output: str = "",
    ):
        """Performs time tagging from the attached OPD.
         See [Time tagging](../../../Guides/features/#time-tagging).

        -- Available with the OPD addon --

        Args:
            target (QUA array of type int): The QUA array into which the
                times of the detected pulses are saved (in ns)
            max_time (int): The time in which pulses are detected
                (Must be larger than the pulse duration)
            targetLen (QUA int): A QUA int which will get the number of
                pulses detected
            element_output (str): the output of an element from which to
                get the pulses
        """
        return DigitalRawTimeTagging(self.loc, element_output, target, targetLen, max_time)

    def high_res(
        self,
        target: QuaVariableType,
        max_time: int,
        targetLen: Optional[QuaNumberType] = None,
        element_output: str = "",
    ):
        """Performs high resolution time tagging. See [Time tagging](../../../Guides/features/#time-tagging).

        -- Available from QOP 2.0 --

        Args:
            target (QUA array of type int): The QUA array into which the
                times of the detected pulses are saved (in ps)
            max_time (int): The time in which pulses are detected
                (Must be larger than the pulse duration)
            targetLen (QUA int): A QUA int which will get the number of
                pulses detected
            element_output (str): the output of an element from which to
                get the pulses
        """
        return HighResTimeTagging(self.loc, element_output, target, targetLen, max_time)


class Counting:
    """A base class for specifying the counting process in the [measure][qm.qua._dsl.measure] statement.
    These are the options which can be used inside the measure command as part of the ``counting`` process.

    -- Available with the OPD addon --
    """

    def __init__(self):
        self.loc = ""

    def digital(
        self,
        target: QuaVariableType,
        max_time: int,
        element_outputs: str = "",
    ):
        """Performs counting from the attached OPD. See [Time tagging](../../../Guides/features/#time-tagging).

        -- Available with the OPD addon --

        Args:
            target (QUA int): A QUA int which will get the number of
                pulses detected
            max_time (int): The time in which pulses are detected
                (Must be larger than the pulse duration)
            element_outputs (str): the outputs of an element from which
                to get ADC results
        """
        return DigitalMeasureProcessCounting(self.loc, element_outputs, target, max_time)


demod = _Demod()
dual_demod = _DualDemod()
integration = _BareIntegration()
dual_integration = _DualBareIntegration()
time_tagging = TimeTagging()
counting = Counting()


def stream_processing() -> _RAScope:
    """A context manager for the creation of [Stream processing pipelines](../../../Guides/stream_proc/#overview)

    Each pipeline defines an analysis process that is applied to every stream item.
    A pipeline must be terminated with a save/save_all terminal, and then can be retrieved with
    [QmJob.result_handles][qm.jobs.running_qm_job.RunningQmJob.result_handles].

    There are two save options: ``save_all`` will save every stream item, ``save`` will save only last item.

    A pipeline can be assigned to python variable, and then reused on other pipelines. It is ensured that the
    common part of the pipeline is processed only once.

    ??? example "Creating a result analysis object"
        ```python
        with stream_processing():
            a.save("tag")
            a.save_all("another tag")
        ```

    ??? example "Retrieving saved result"
        ```python
        QmJob.result_handles.get("tag")
        ```

    """
    prog = _get_scope_as_program()
    return _RAScope(prog.result_analysis)


CommandsType = List[str]


class _Functions:
    @staticmethod
    def average(axis: OneOrMore[PyNumberType] = None) -> CommandsType:
        """Perform a running average on a stream item. The Output of this operation is the
        running average of the values in the stream starting from the beginning of the
        QUA program.

        Args:
            axis: optional Axis or axes along which to average.

        Returns:
            stream object
        """
        if axis is None:
            return ["average"]
        else:
            if hasattr(axis, "__len__"):
                # vector
                return [
                    "average",
                    ["@array"] + [str(item) for item in list(axis)],
                ]
            else:
                # scalar
                return ["average", str(axis)]

    @staticmethod
    def dot_product(vector: PyNumberArrayType) -> CommandsType:
        """Computes dot product of the given vector and an item of the input stream

        Args:
            vector: constant vector of numbers

        Returns:
            stream object
        """
        return ["dot", ["@array"] + [str(item) for item in list(vector)]]

    @staticmethod
    def tuple_dot_product() -> CommandsType:
        """Computes dot product between the two vectors of the input stream

        Returns:
            stream object
        """
        return ["dot"]

    @staticmethod
    def multiply_by(scalar_or_vector: OneOrMore[PyNumberType]) -> CommandsType:
        """Multiply the input stream item by a constant scalar or vector.
        the input item can be either scalar or vector.

        Args:
            scalar_or_vector: either a scalar number, or a vector of
                scalars.

        Returns:
            stream object
        """
        if hasattr(scalar_or_vector, "__len__"):
            # vector
            return [
                "vmult",
                ["@array"] + [str(item) for item in list(scalar_or_vector)],
            ]
        else:
            # scalar
            return ["smult", str(scalar_or_vector)]

    @staticmethod
    def tuple_multiply() -> CommandsType:
        """Computes multiplication between the two elements of the input stream.
        Can be any combination of scalar and vectors.

        Returns:
            stream object
        """
        return ["tmult"]

    @staticmethod
    def convolution(constant_vector: PyNumberArrayType, mode: Optional[str] = None) -> CommandsType:
        """Computes discrete, linear convolution of one-dimensional constant vector and
        one-dimensional vector item of the input stream.

        Args:
            constant_vector: vector of numbers
            mode: "full", "same" or "valid"

        Returns:
            stream object
        """
        if mode is None:
            mode = ""
        return [
            "conv",
            str(mode),
            ["@array"] + [str(item) for item in list(constant_vector)],
        ]

    @staticmethod
    def tuple_convolution(mode: Optional[str] = None) -> CommandsType:
        """Computes discrete, linear convolution of two one-dimensional vectors of the
        input stream

        Args:
            mode: "full", "same" or "valid"

        Returns:
            stream object
        """
        if mode is None:
            mode = ""
        return ["conv", str(mode)]

    @staticmethod
    def fft(output: Optional[str] = None) -> CommandsType:
        """Computes one-dimensional discrete fourier transform for every item in the
        stream.
        Item can be a vector of numbers, in this case fft will assume all imaginary
        numbers are 0.
        Item can also be a vector of number pairs - in this case for each pair - the
        first will be real and second imaginary.

        Args:
            output: supported from QOP 1.30 and QOP 2.0, options are
                "normal", "abs" and "angle":

                *   "normal" - Same as default (none), returns a 2d array of
                    size Nx2, where N is the length of the original vector.
                    The first item in each pair is the real part, and the 2nd
                    is the imaginary part.
                *   "abs" - Returns a 1d array of size N with the abs of the fft.
                *   "angle" - Returns the angle between the imaginary and real
                    parts in radians.

        Returns:
            stream object
        """
        if output is None:
            return ["fft"]
        else:
            return ["fft", str(output)]

    @staticmethod
    def boolean_to_int() -> CommandsType:
        """
        Converts boolean to integer number - 1 for true and 0 for false

        :return: stream object
        """
        return ["booleancast"]

    @staticmethod
    def demod(
        frequency: PyNumberType,
        iw_cos: PyNumberType,
        iw_sin: PyNumberType,
        *,
        integrate: Optional[bool] = None,
    ):
        """Demodulates the acquired data from the indicated stream at the given frequency
        and integration weights.
        If operating on a stream of tuples, assumes that the 2nd item is the timestamps
        and uses them for the demodulation, reproducing the demodulation performed
        in real time.
        If operated on a single stream, assumes that the first item is at time zero and
        that the elements are separated by 1ns.

        Args:
            frequency: frequency for demodulation calculation
            iw_cos: cosine integration weight. Integration weight can be
                either a scalar for constant integration weight, or a
                python iterable for arbitrary integration weights.
            iw_sin: sine integration weight. Integration weight can be
                either a scalar for constant integration weight, or a
                python iterable for arbitrary integration weights.
            integrate: sum the demodulation result and returns a scalar
                if True (default), else the demodulated stream without
                summation is returned

        Returns:
            stream object

        Example:
            ```python
            with stream_processing():
                adc_stream.input1().with_timestamps().map(FUNCTIONS.demod(freq, 1.0, 0.0, integrate=False)).average().save('cos_env')
                adc_stream.input1().with_timestamps().map(FUNCTIONS.demod(freq, 1.0, 0.0)).average().save('cos_result')  # Default is integrate=True
            ```

        Note:
            The demodulation in the stream processing **does not** take in consideration
            any real-time modifications to the frame, phase or frequency of the element.
            If the program has any QUA command that changes them, the result of the
            stream processing demodulation will be invalid.

        """
        if hasattr(iw_cos, "__len__"):
            iw_cos = ["@array"] + [str(item) for item in list(iw_cos)]
        else:
            iw_cos = str(iw_cos)
        if hasattr(iw_sin, "__len__"):
            iw_sin = ["@array"] + [str(item) for item in list(iw_sin)]
        else:
            iw_sin = str(iw_sin)
        out = ["demod", str(frequency), iw_cos, iw_sin]
        if type(integrate) is bool:
            out.append("1" if integrate else "0")
        return out


FUNCTIONS = _Functions()


class _ResultStream:
    def __init__(
        self,
        input_stream: Optional[Union[CommandsType, "_ResultStream"]],
        operator_array: Optional[CommandsType],
    ):
        if operator_array is not None:
            self._operator_array = [*operator_array]
            self._operator_array.append(input_stream)
        else:
            self._operator_array = input_stream

    def average(self) -> "_ResultStream":
        """
        Perform a running average on a stream item. The Output of this operation is the running average
        of the values in the stream starting from the beginning of the QUA program.
        """
        return _ResultStream(self, ["average"])

    def real(self) -> "_ResultStream":
        return _ResultStream(self, ["real"])

    def image(self) -> "_ResultStream":
        return _ResultStream(self, ["image"])

    def buffer(self, *args) -> "_ResultStream":
        """Gather items into vectors - creates an array of input stream items and outputs the array as one item.
        only outputs full buffers.

        Note:
            The order of resulting dimensions is different when using a buffer with multiple inputs compared to using
            multiple buffers. The following two lines are equivalent:
            ```python
            stream.buffer(n, l, k)
            stream.buffer(k).buffer(l).buffer(n)
            ```

        Args:
            *args: number of items to gather, can either be a single
                number, which gives the results as a 1d array or
                multiple numbers for a multidimensional array.
        """
        int_args = [str(int(arg)) for arg in args]
        return _ResultStream(self, ["buffer"] + int_args)

    def buffer_and_skip(self, length: PyNumberType, skip: PyNumberType) -> "_ResultStream":
        """Gather items into vectors - creates an array of input stream items and outputs
        the array as one item.
        Skips the number of given elements. Note that length and skip start from the
        same index, so the `buffer(n)` command is equivalent to `buffer_and_skip(n, n)`.

        Only outputs full buffers.

        Example:
            ```python
            # The stream input is [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
            with stream_processing():
                stream.buffer(3).save_all("example1")
                stream.buffer_and_skip(3, 3).save_all("example2")
                stream.buffer_and_skip(3, 2).save_all("example3")
                stream.buffer_and_skip(3, 5).save_all("example4")
            # example1 -> [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
            # example2 -> [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
            # example3 -> [[1, 2, 3], [3, 4, 5], [5, 6, 7], [7, 8, 9]]
            # example4 -> [[1, 2, 3], [6, 7, 8]]
            ```
        Args:
            length: number of items to gather
            skip: number of items to skip for each buffer, starting from
                the same index as length
        """
        return _ResultStream(self, ["bufferAndSkip", str(int(length)), str(int(skip))])

    def map(self, function: CommandsType) -> "_ResultStream":
        """Transform the item by applying a
        [function][qm.qua._dsl._Functions] to it

        Args:
            function: a function to transform each item to a different
                item. For example, to compute an average between
                elements in a buffer you should write
                ".buffer(len).map(FUNCTIONS.average())"
        """
        return _ResultStream(self, ["map", function])

    def flatten(self) -> "_ResultStream":
        """
        Deconstruct an array item - and send its elements one by one as items
        """
        return _ResultStream(self, ["flatten"])

    def skip(self, length: PyNumberType) -> "_ResultStream":
        """Suppress the first n items of the stream

        Args:
            length: number of items to skip
        """
        return _ResultStream(self, ["skip", str(int(length))])

    def skip_last(self, length: PyNumberType) -> "_ResultStream":
        """Suppress the last n items of the stream

        Args:
            length: number of items to skip
        """
        return _ResultStream(self, ["skipLast", str(int(length))])

    def take(self, length: PyNumberType) -> "_ResultStream":
        """Outputs only the first n items of the stream

        Args:
            length: number of items to take
        """
        return _ResultStream(self, ["take", str(int(length))])

    def histogram(self, bins: List[List[PyNumberType]]) -> "_ResultStream":
        """Compute the histogram of all items in stream

        Args:
            bins: vector or pairs. each pair indicates the edge of each
                bin. example: [[1,10],[11,20]] - two bins, one between 1
                and 10, second between 11 and 20
        """
        converted_bins = []
        for sub_list in list(bins):
            converted_bins = converted_bins + [["@array"] + [str(item) for item in list(sub_list)]]
        return _ResultStream(self, ["histogram", ["@array"] + converted_bins])

    def zip(self, other: "_ResultStream") -> "_ResultStream":
        """Combine the emissions of two streams to one item that is a tuple of items of input streams

        Args:
            other: second stream to combine with self
        """
        return _ResultStream(self, ["zip", other._to_proto()])

    def save_all(self, tag: str):
        """Save all items received in stream.
        This will add to [qm._results.JobResults][] a [qm._results.SingleNamedJobResult][] object.

        Args:
            tag: result name
        """
        ra = _get_scope_as_result_analysis()
        ra.save_all(tag, self)

    def save(self, tag: str):
        """Save only the last item received in stream
        This will add to [qm._results.JobResults][] a [qm._results.MultipleNamedJobResult][] object.

        Args:
            tag: result name
        """
        ra = _get_scope_as_result_analysis()
        ra.save(tag, self)

    def dot_product(self, vector: PyNumberArrayType) -> "_ResultStream":
        """Computes dot product of the given vector and each item of the input stream

        Args:
            vector: constant vector of numbers
        """
        return self.map(FUNCTIONS.dot_product(vector))

    def tuple_dot_product(self) -> "_ResultStream":
        """
        Computes dot product of the given item of the input stream - that should include two vectors
        """
        return self.map(FUNCTIONS.tuple_dot_product())

    def multiply_by(self, scalar_or_vector: OneOrMore[PyNumberType]) -> "_ResultStream":
        """Multiply the input stream item by a constant scalar or vector.
        The input item can be either scalar or vector.

        Args:
            scalar_or_vector: either a scalar number, or a vector of
                scalars.
        """
        return self.map(FUNCTIONS.multiply_by(scalar_or_vector))

    def tuple_multiply(self) -> "_ResultStream":
        """
        Computes multiplication of the given item of the input stream - that can be any
        combination of scalar and vectors.
        """
        return self.map(FUNCTIONS.tuple_multiply())

    def convolution(self, constant_vector: PyNumberArrayType, mode: Optional[str] = None) -> "_ResultStream":
        """Computes discrete, linear convolution of one-dimensional constant vector and one-dimensional vector
        item of the input stream.

        Args:
            constant_vector: vector of numbers
            mode: "full", "same" or "valid"
        """
        return self.map(FUNCTIONS.convolution(constant_vector, mode))

    def tuple_convolution(self, mode: Optional[str] = None) -> "_ResultStream":
        """Computes discrete, linear convolution of two one-dimensional vectors that received as the one item from the input stream

        Args:
            mode: "full", "same" or "valid"
        """
        return self.map(FUNCTIONS.tuple_convolution(mode))

    def fft(self, output: Optional[str] = None) -> "_ResultStream":
        """Computes one-dimensional discrete fourier transform for every item in the
        stream.
        Item can be a vector of numbers, in this case fft will assume all imaginary
        numbers are 0.
        Item can also be a vector of number pairs - in this case for each pair - the
        first will be real and second imaginary.

        Args:
            output: supported from QOP 1.30 and QOP 2.0, options are
                "normal", "abs" and "angle":

                *   "normal" - Same as default (none), returns a 2d array of
                    size Nx2, where N is the length of the original vector.
                    The first item in each pair is the real part, and the 2nd
                    is the imaginary part.
                *   "abs" - Returns a 1d array of size N with the abs of the fft.
                *   "angle" - Returns the angle between the imaginary and real
                    parts in radians.

        Returns:
            stream object
        """
        return self.map(FUNCTIONS.fft(output))

    def boolean_to_int(self) -> "_ResultStream":
        """
        converts boolean to an integer number - 1 for true and 0 for false
        """
        return self.map(FUNCTIONS.boolean_to_int())

    def _array_to_proto(self, array: List[Union[str, CommandsType, "_ResultStream", "_ResultSource"]]) -> CommandsType:
        res = []
        for x in array:
            if isinstance(x, str):
                res.append(x)
            elif isinstance(x, list):
                res.append(self._array_to_proto(x))
            elif isinstance(x, _ResultSource):
                res.append(x._to_proto())
            elif isinstance(x, _ResultStream):
                res.append(x._to_proto())
        return res

    def _to_proto(self) -> CommandsType:
        res = self._array_to_proto(self._operator_array)
        return res

    def add(self, other: Union["_ResultStream", OneOrMore[PyNumberType]]) -> "_ResultStream":
        """Allows addition between streams. The addition is done element-wise.
        Can also be performed on buffers and other operators, but they must have the
        same dimensions.

        Example:
            ```python
            i = declare(int)
            j = declare(int)
            k = declare(int, value=5)
            stream = declare_stream()
            stream2 = declare_stream()
            stream3 = declare_stream()
            with for_(j, 0, j < 30, j + 1):
                with for_(i, 0, i < 10, i + 1):
                    save(i, stream)
                    save(j, stream2)
                    save(k, stream3)

            with stream_processing():
                (stream1 + stream2 + stream3).save_all("example1")
                (stream1.buffer(10) + stream2.buffer(10) + stream3.buffer(10)).save_all("example2")
                (stream1 + stream2 + stream3).buffer(10).average().save("example3")
            ```
        """
        return self.__add__(other)

    def subtract(self, other: Union["_ResultStream", OneOrMore[PyNumberType]]) -> "_ResultStream":
        """Allows subtraction between streams. The subtraction is done element-wise.
        Can also be performed on buffers and other operators, but they must have the
        same dimensions.

        Example:
            ```python
            i = declare(int)
            j = declare(int)
            k = declare(int, value=5)
            stream = declare_stream()
            stream2 = declare_stream()
            stream3 = declare_stream()
            with for_(j, 0, j < 30, j + 1):
                with for_(i, 0, i < 10, i + 1):
                    save(i, stream)
                    save(j, stream2)
                    save(k, stream3)

            with stream_processing():
                (stream1 - stream2 - stream3).save_all("example1")
                (stream1.buffer(10) - stream2.buffer(10) - stream3.buffer(10)).save_all("example2")
                (stream1 - stream2 - stream3).buffer(10).average().save("example3")
            ```
        """
        return self.__sub__(other)

    def multiply(self, other: Union["_ResultStream", OneOrMore[PyNumberType]]) -> "_ResultStream":
        """Allows multiplication between streams. The multiplication is done element-wise.
        Can also be performed on buffers and other operators, but they must have the
        same dimensions.

        Example:
            ```python
            i = declare(int)
            j = declare(int)
            k = declare(int, value=5)
            stream = declare_stream()
            stream2 = declare_stream()
            stream3 = declare_stream()
            with for_(j, 0, j < 30, j + 1):
                with for_(i, 0, i < 10, i + 1):
                    save(i, stream)
                    save(j, stream2)
                    save(k, stream3)

            with stream_processing():
                (stream1 * stream2 * stream3).save_all("example1")
                (stream1.buffer(10) * stream2.buffer(10) * stream3.buffer(10)).save_all("example2")
                (stream1 * stream2 * stream3).buffer(10).average().save("example3")
            ```
        """
        return self.__mul__(other)

    def divide(self, other: Union["_ResultStream", OneOrMore[PyNumberType]]) -> "_ResultStream":
        """Allows division between streams. The division is done element-wise.
        Can also be performed on buffers and other operators, but they must have the
        same dimensions.

        Example:
            ```python
            i = declare(int)
            j = declare(int)
            k = declare(int, value=5)
            stream = declare_stream()
            stream2 = declare_stream()
            stream3 = declare_stream()
            with for_(j, 0, j < 30, j + 1):
                with for_(i, 0, i < 10, i + 1):
                    save(i, stream)
                    save(j, stream2)
                    save(k, stream3)

            with stream_processing():
                (stream1 / stream2 / stream3).save_all("example1")
                (stream1.buffer(10) / stream2.buffer(10) / stream3.buffer(10)).save_all("example2")
                (stream1 / stream2 / stream3).buffer(10).average().save("example3")
            ```
        """
        return self.__truediv__(other)

    def __add__(self, other: Union["_ResultStream", OneOrMore[PyNumberType]]) -> "_ResultStream":
        if isinstance(other, _ResultStream):
            return _ResultStream(["+", self, other], None)
        elif isinstance(other, (int, float, np.integer, np.floating)) and not isinstance(other, (bool, np.bool_)):
            return _ResultStream(["+", self, str(other)], None)
        elif hasattr(other, "__len__"):
            return _ResultStream(["+", self, ["@array"] + [str(item) for item in list(other)]], None)

    def __radd__(self, other: OneOrMore[PyNumberType]) -> "_ResultStream":
        if isinstance(other, (int, float, np.integer, np.floating)) and not isinstance(other, (bool, np.bool_)):
            return _ResultStream(["+", str(other), self], None)
        elif hasattr(other, "__len__"):
            return _ResultStream(["+", ["@array"] + [str(item) for item in list(other)], self], None)

    def __sub__(self, other: Union["_ResultStream", OneOrMore[PyNumberType]]) -> "_ResultStream":
        if isinstance(other, _ResultStream):
            return _ResultStream(["-", self, other], None)
        elif isinstance(other, (int, float, np.integer, np.floating)) and not isinstance(other, (bool, np.bool_)):
            return _ResultStream(["-", self, str(other)], None)
        elif hasattr(other, "__len__"):
            return _ResultStream(["-", self, ["@array"] + [str(item) for item in list(other)]], None)

    def __rsub__(self, other: Union["_ResultStream", OneOrMore[PyNumberType]]) -> "_ResultStream":
        if isinstance(other, (int, float, np.integer, np.floating)) and not isinstance(other, (bool, np.bool_)):
            return _ResultStream(["-", str(other), self], None)
        elif hasattr(other, "__len__"):
            return _ResultStream(["-", ["@array"] + [str(item) for item in list(other)], self], None)

    def __gt__(self, _):
        raise QmQuaException("Can't use > operator on results")

    def __ge__(self, _):
        raise QmQuaException("Can't use >= operator on results")

    def __lt__(self, _):
        raise QmQuaException("Can't use < operator on results")

    def __le__(self, _):
        raise QmQuaException("Can't use <= operator on results")

    def __eq__(self, _):
        raise QmQuaException("Can't use == operator on results")

    def __mul__(self, other: Union["_ResultStream", OneOrMore[PyNumberType]]) -> "_ResultStream":
        if isinstance(other, _ResultStream):
            return _ResultStream(["*", self, other], None)
        elif isinstance(other, (int, float, np.integer, np.floating)) and not isinstance(other, (bool, np.bool_)):
            return _ResultStream(["*", self, str(other)], None)
        elif hasattr(other, "__len__"):
            return _ResultStream(["*", self, ["@array"] + [str(item) for item in list(other)]], None)

    def __rmul__(self, other: Union["_ResultStream", OneOrMore[PyNumberType]]) -> "_ResultStream":
        if isinstance(other, (int, float, np.integer, np.floating)) and not isinstance(other, (bool, np.bool_)):
            return _ResultStream(["*", str(other), self], None)
        elif hasattr(other, "__len__"):
            return _ResultStream(["*", ["@array"] + [str(item) for item in list(other)], self], None)

    def __div__(self, _):
        raise QmQuaException("Can't use / operator on results")

    def __truediv__(self, other: Union["_ResultStream", OneOrMore[PyNumberType]]) -> "_ResultStream":
        if isinstance(other, _ResultStream):
            return _ResultStream(["/", self, other], None)
        elif isinstance(other, (int, float, np.integer, np.floating)) and not isinstance(other, (bool, np.bool_)):
            return _ResultStream(["/", self, str(other)], None)
        elif hasattr(other, "__len__"):
            return _ResultStream(["/", self, ["@array"] + [str(item) for item in list(other)]], None)

    def __rtruediv__(self, other: Union["_ResultStream", OneOrMore[PyNumberType]]) -> "_ResultStream":
        if isinstance(other, (int, float, np.integer, np.floating)) and not isinstance(other, (bool, np.bool_)):
            return _ResultStream(["/", str(other), self], None)
        elif hasattr(other, "__len__"):
            return _ResultStream(["/", ["@array"] + [str(item) for item in list(other)], self], None)

    def __lshift__(self, other: Union["_ResultStream", OneOrMore[PyNumberType]]):
        save(other, self)

    def __rshift__(self, _):
        raise QmQuaException("Can't use >> operator on results")

    def __and__(self, _):
        raise QmQuaException("Can't use & operator on results")

    def __or__(self, _):
        raise QmQuaException("Can't use | operator on results")

    def __xor__(self, _):
        raise QmQuaException("Can't use ^ operator on results")


class _ResultSourceTimestampMode(Enum):
    Values = 0
    Timestamps = 1
    ValuesAndTimestamps = 2


@dataclass
class _ResultSourceConfiguration:
    var_name: str
    timestamp_mode: _ResultSourceTimestampMode
    is_adc_trace: bool
    input: int
    auto_reshape: bool


class _ResultSource(_ResultStream):
    """A python object representing a source of values that can be processed in a [`stream_processing()`][qm.qua._dsl.stream_processing] pipeline

    This interface is chainable, which means that calling most methods on this object will create a new streaming source

    See the base class [_ResultStream][qm.qua._dsl._ResultStream] for operations
    """

    def __init__(self, configuration: _ResultSourceConfiguration):
        super().__init__(None, None)
        self._configuration = configuration

    def _to_proto(self) -> List[str]:
        result = [
            _RESULT_SYMBOL,
            str(self._configuration.timestamp_mode.value),
            self._configuration.var_name,
        ]
        inputs = ["@macro_input", str(self._configuration.input), result] if self._configuration.input != -1 else result
        auto_reshape = ["@macro_auto_reshape", inputs] if self._configuration.auto_reshape else inputs
        return ["@macro_adc_trace", auto_reshape] if self._configuration.is_adc_trace else auto_reshape

    def get_var_name(self) -> str:
        return self._configuration.var_name

    def with_timestamps(self) -> _ResultStream:
        """Get a stream with the relevant timestamp for each stream-item"""
        return _ResultSource(
            dataclasses.replace(
                self._configuration,
                timestamp_mode=_ResultSourceTimestampMode.ValuesAndTimestamps,
            )
        )

    def timestamps(self) -> _ResultStream:
        """Get a stream with only the timestamps of the stream-items"""
        return _ResultSource(
            dataclasses.replace(
                self._configuration,
                timestamp_mode=_ResultSourceTimestampMode.Timestamps,
            )
        )

    def input1(self) -> "_ResultSource":
        """A stream of raw ADC data from input 1. Only relevant when saving data from measure statement."""
        return _ResultSource(dataclasses.replace(self._configuration, input=1))

    def input2(self) -> "_ResultSource":
        """A stream of raw ADC data from input 2. Only relevant when saving data from measure statement."""
        return _ResultSource(dataclasses.replace(self._configuration, input=2))

    def auto_reshape(self) -> "_ResultSource":
        """Creates a buffer with dimensions according to the program structure in QUA.

        For example, when running the following program the result "reshaped" will have
        shape of (30,10):

        Example:
            ```python
            i = declare(int)
            j = declare(int)
            stream = declare_stream()
            with for_(i, 0, i < 30, i + 1):
                with for_(j, 0, j < 10, j + 1):
                    save(i, stream)

            with stream_processing():
                stream.auto_reshape().save_all("reshaped")
            ```
        """
        return _ResultSource(dataclasses.replace(self._configuration, auto_reshape=True))


def bins(start: PyNumberType, end: PyNumberType, number_of_bins: PyFloatType):
    bin_size = _math.ceil((end - start + 1) / float(number_of_bins))
    bins_list = []
    while start < end:
        step_end = start + bin_size - 1
        if step_end >= end:
            step_end = end
        bins_list = bins_list + [[start, step_end]]
        start += bin_size
    return bins_list


def _make_dict_from_args(args: Sequence[object], names: Sequence[str]) -> Dict[str, object]:
    return {name: arg for name, arg in zip(names, args)}
