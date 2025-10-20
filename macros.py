"""
This file contains useful QUA macros meant to simplify and ease QUA programs.
All the macros below have been written and tested with the basic configuration. If you modify this configuration
(elements, operations, integration weights...) these macros will need to be modified accordingly.
"""

from qm.qua import *

##############
# QUA macros #
##############

from qm.qua import *
import numpy as np

def multiplexed_parser(qubit_keys, multiplexed_parameters, call_list=None):
    '''
    Parse multiplexed parameters for the given qubit keys. Returns Tuple of arrays of the parameters in order of the qubit keys given.
    If call_list is given, returns only the parameters in the call_list in the order they are given.

    :param qubit_keys: List of qubit keys to parse the parameters for.
    :param multiplexed_parameters: Dictionary of the multiplexed parameters for all qubits (taken from configuration file).
    :param call_list: List of parameter names to return. If None, returns large subset of parameters (in order specified below). Keys available: ["qubit_key", "qubit_frequency", "qubit_LO", "qubit_IF","resonator_key", "resonator_frequency", "resonator_LO", "resonator_IF", "readout_len", "qubit_relaxation", "resonator_relaxation", "ge_threshold", "drag_coef", "anharmonicity", "x180_len", "x180_amp", "x90_len", "x90_amp"]
    :return: Tuple of lists/arrays of the parameters in order of the qubit keys given, or in the order specified in call_list. (default order is: "qubit_key", "qubit_frequency", "qubit_LO", "qubit_IF","resonator_key", "resonator_frequency", "resonator_LO", "resonator_IF", "readout_len", "qubit_relaxation", "resonator_relaxation", "ge_threshold", "drag_coef", "anharmonicity")
    '''
    if call_list is None:
        call_list = ["qubit_key", "qubit_frequency", "qubit_LO", "qubit_IF","resonator_key", "resonator_frequency", "resonator_LO", "resonator_IF", "readout_len", "qubit_relaxation", "resonator_relaxation", "ge_threshold", "drag_coef", "anharmonicity"]
    list_to_return = []
    for item in call_list:
        item_list = []
        for key in qubit_keys:
            if key in list(multiplexed_parameters.keys()):
                item_list.append(multiplexed_parameters[key][item])
        list_to_return.append(np.array(item_list))
    return tuple(list_to_return)

def mp_result_names(qub_key_subset, single_tags=[], mp_tags = []):
    result_names = single_tags.copy()
    for tag in mp_tags:
        for j in range(len(qub_key_subset)):
            result_names.append(f"{tag}_{j}")
    return result_names

def mp_fetch_all(res_handles, qub_key_subset, num_single_tags = 0):
    '''
    Sort out fetch_all() results when using multiplexing

    :param res_handles: result handles from fetching_tool
    :param qub_key_subset: list of qubit keys used in the multiplexed experiment (in order used in program)
    :param num_single_tags: number of unmultiplexed fetch results like "iteration" before the multiplexed results start
    :return: tuple of numpy arrays, for each streamed quantity.
    '''
    results = res_handles.fetch_all()
    num_qubits = len(qub_key_subset)
    try:
        assert (len(results) - num_single_tags) % num_qubits == 0
    except AssertionError:
        raise ValueError(f"Incompatible number of results and qubits, {len(results)} results for {num_qubits} qubits with {num_single_tags} single tags.")
    num_streams = (len(results) - num_single_tags) // num_qubits
    sorted_results = [results[k] for k in range(num_single_tags)] + [np.array([results[num_single_tags + (i * num_qubits) + j] for j in range(num_qubits)])
        for i in range(num_streams)]
    return tuple(sorted_results)

def simple_two_state_discriminator(I, threshold, state=None):
    '''
    Takes I, applies threshold, returns state (0 or 1), must be rotated.

    :param I: A QUA variable for the information in the `I` quadrature. Should be of type `Fixed`.
    :param threshold: A QUA variable for the threshold value. Should be of type `Fixed`.
    :param state: A QUA variable for the state information. Should be of type `bool`. If None, it will be declared inside the function.
    :return: QUA `state` variable as 0 or 1
    '''
    if state is None:
        state = declare(int)
    with if_(I > threshold):
        assign(state, 1)
    with else_():
        assign(state, 0)
    return state
    
def readout_macro(resonator, I, Q, state, threshold, state_boolean=False):
    '''
    Perform a readout on the given resonator, demodulate the signal, and apply a simple two-state discrimination based on the provided threshold.

    :param resonator: The resonator key to perform the readout on. Should be a string corresponding to a resonator defined in the configuration.
    :param I: A QUA variable for the information in the `I` quadrature. Should be of type `Fixed`.
    :param Q: A QUA variable for the information in the `Q` quadrature. Should be of type `Fixed`.
    :param state: A QUA variable for the state information. Should be of type `int`.
    :param threshold: A QUA variable for the threshold value. Should be of type `Fixed`.
    :return: QUA variables `I`, `Q`, and `state` (0 or 1)
    '''
    measure(
        "readout",
        resonator,
        dual_demod.full("opt_cos", "opt_sin", I),
        dual_demod.full("opt_minus_sin", "opt_cos", Q),
    )
    if state_boolean:
        assign(state, I > threshold)
    else:
        with if_(I > threshold):
            assign(state, 1)
        with else_():
            assign(state, 0)
    return I, Q, state

from pathlib import Path
from collections.abc import Mapping, Sequence
from typing import Iterable, Tuple, Any, Union
def numpyint32_finder(root: Any) -> Iterable[Path]:
    """
    paths_to_numpy_int32_including_arrays: Generator of paths to all np.int32 values in a nested structure.
    Like `paths_to_numpy_int32`, but also drills into numpy arrays.
    Array indices are appended to the path as integers.
    """
    def _walk(obj: Any, path: Path):
        if isinstance(obj, np.int32):
            yield path
            return

        if isinstance(obj, Mapping):
            for k, v in obj.items():
                yield from _walk(v, path + (k,))
            return

        if isinstance(obj, Sequence) and not isinstance(obj, (str, bytes, bytearray)):
            # Handle python lists/tuples
            for i, v in enumerate(obj):
                yield from _walk(v, path + (i,))
            return

        # Handle numpy arrays element-wise if dtype is int32
        if isinstance(obj, np.ndarray):
            if obj.dtype == np.int32:
                # iterate with ndenumerate to get multi-dimensional indices
                for idx, val in np.ndenumerate(obj):
                    # idx is a tuple of ints; append as a single step if you prefer
                    # but flattening them keeps path navigation straightforward:
                    yield path + idx
            else:
                # if not int32 dtype, still dive into object arrays cautiously
                if obj.dtype == object:
                    for idx, val in np.ndenumerate(obj):
                        yield from _walk(val, path + idx)

    return _walk(root, ())


# Macro for measuring the qubit state with single shot
def readout_macro(threshold=None, state=None, I=None, Q=None, res_key = "rr1"):
    """
    A macro for performing the single-shot readout, with the ability to perform state discrimination.
    If `threshold` is given, the information in the `I` quadrature will be compared against the threshold and `state`
    would be `True` if `I > threshold`.
    Note that it is assumed that the results are rotated such that all the information is in the `I` quadrature.

    :param threshold: Optional. The threshold to compare `I` against.
    :param state: A QUA variable for the state information, only used when a threshold is given.
        Should be of type `bool`. If not given, a new variable will be created
    :param I: A QUA variable for the information in the `I` quadrature. Should be of type `Fixed`. If not given, a new
        variable will be created
    :param Q: A QUA variable for the information in the `Q` quadrature. Should be of type `Fixed`. If not given, a new
        variable will be created
    :return: Three QUA variables populated with the results of the readout: (`state` (only if threshold is not None), `I`, `Q`)
    """
    if I is None:
        I = declare(fixed)
    if Q is None:
        Q = declare(fixed)
    if (threshold is not None) and (state is None):
        state = declare(bool)
    measure(
        "readout",
        res_key,
        None,
        dual_demod.full("rotated_cos", "rotated_sin", I),
        dual_demod.full("rotated_minus_sin", "rotated_cos", Q),
    )
    if threshold is not None:
        assign(state, I > threshold)
        return state, I, Q
    else:
        return I, Q


# Macro for measuring the averaged ground and excited states for calibration
def ge_averaged_measurement(cooldown_time, n_avg, res_key = "rr1", qubit_key = "q1"):
    """Macro measuring the qubit's ground and excited states n_avg times. The averaged values for the corresponding I
    and Q quadratures can be retrieved using the stream processing context manager `Ig_st.average().save("Ig")` for instance.

    :param cooldown_time: cooldown time between two successive qubit state measurements in clock cycle unit (4ns).
    :param n_avg: number of averaging iterations. Must be a python integer.
    :return: streams for the 'I' and 'Q' data for the ground and excited states respectively: [Ig_st, Qg_st, Ie_st, Qe_st].
    """
    n = declare(int)
    I = declare(fixed)
    Q = declare(fixed)
    Ig_st = declare_stream()
    Qg_st = declare_stream()
    Ie_st = declare_stream()
    Qe_st = declare_stream()
    with for_(n, 0, n < n_avg, n + 1):
        # Ground state calibration
        align(qubit_key, res_key)
        measure(
            "readout",
            res_key,
            None,
            dual_demod.full("cos", "sin", I),
            dual_demod.full("minus_sin", "cos", Q),
        )
        wait(cooldown_time, res_key, qubit_key)
        save(I, Ig_st)
        save(Q, Qg_st)

        # Excited state calibration
        align(qubit_key, res_key)
        play("x180", qubit_key)
        align(qubit_key, res_key)
        measure(
            "readout",
            res_key,
            None,
            dual_demod.full("cos", "sin", I),
            dual_demod.full("minus_sin", "cos", Q),
        )
        wait(cooldown_time, res_key, qubit_key)
        save(I, Ie_st)
        save(Q, Qe_st)

        return Ig_st, Qg_st, Ie_st, Qe_st
