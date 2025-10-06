from qm.qua import *
import numpy as np

def multiplexed_parser(qubit_keys, multiplexed_parameters):
    qubit_key_subset = []
    qubit_frequencies = []
    resonator_key_subset = []
    resonator_frequencies = []
    readout_lengths = []
    ge_thresholds = []
    drag_coef_subset = []
    for key in qubit_keys:
        if key in list(multiplexed_parameters.keys()):
            qubit_dict = multiplexed_parameters[key].copy()
            qubit_key_subset.append(key)
            qubit_frequencies.append(qubit_dict["qubit_freq"])
            resonator_key_subset.append(qubit_dict["res_key"])
            resonator_frequencies.append(qubit_dict["res_freq"])
            readout_lengths.append(qubit_dict["readout_len"])
            ge_thresholds.append(qubit_dict["ge_threshold"])
            drag_coef_subset.append(qubit_dict["drag_coef"])  # Default to 0.0 if not present
    return qubit_key_subset, np.array(qubit_frequencies), resonator_key_subset, np.array(resonator_frequencies), np.array(readout_lengths), np.array(ge_thresholds), np.array(drag_coef_subset)

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