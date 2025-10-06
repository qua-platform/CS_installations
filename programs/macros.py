from qm.qua import *
import numpy as np

def multiplexed_parser(qubit_keys, multiplexed_parameters, call_list=None):
    '''
    Parse multiplexed parameters for the given qubit keys. Returns Tuple of arrays of the parameters in order of the qubit keys given.
    If call_list is given, returns only the parameters in the call_list in the order they are given.
    :param qubit_keys: List of qubit keys to parse the parameters for.
    :param multiplexed_parameters: Dictionary of the multiplexed parameters for all qubits (taken from configuration file).
    :param call_list: List of parameter names to return. If None, returns large subset of parameters (in order specified below). Keys available: ["qubit_key", "qubit_frequency", "resonator_key", "resonator_frequency", "readout_len", "readout_amp", "qubit_relaxation", "resonator_relaxation", "ge_threshold", "drag_coef", "anharmonicity", "x180_len", "x180_amp", "x90_len", "x90_amp"]
    :return: Tuple of lists/arrays of the parameters in order of the qubit keys given, or in the order specified in call_list. (default order is: "qubit_key", "qubit_frequency", "resonator_key", "resonator_frequency", "readout_len", "qubit_relaxation", "resonator_relaxation", "ge_threshold", "drag_coef", "anharmonicity")
    '''
    if call_list is None:
        call_list = ["qubit_key", "qubit_frequency", "resonator_key", "resonator_frequency", "readout_len", "qubit_relaxation", "resonator_relaxation", "ge_threshold", "drag_coef", "anharmonicity"]
    list_to_return = []
    for item in call_list:
        item_list = []
        for key in qubit_keys:
            if key in list(multiplexed_parameters.keys()):
                item_list.append(multiplexed_parameters[key][item])
        list_to_return.append(np.array(item_list))
    return tuple(list_to_return)


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
    
def readout_macro(resonator, I, Q, state, threshold):
    measure(
        "readout",
        resonator,
        None,
        dual_demod.full("opt_cos", "opt_sin", I),
        dual_demod.full("opt_minus_sin", "opt_cos", Q),
    )
    
    with if_(I > threshold):
        assign(state, 1)
    with else_():
        assign(state, 0)
    return I, Q, state