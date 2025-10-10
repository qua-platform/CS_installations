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