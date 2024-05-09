"""
This file contains useful QUA macros meant to simplify and ease QUA programs.
All the macros below have been written and tested with the basic configuration. If you modify this configuration
(elements, operations, integration weights...) these macros will need to be modified accordingly.
"""

from qm.qua import *
from qualang_tools.addons.variables import assign_variables_to_element
import matplotlib.pyplot as plt
from configuration_with_octave import u
from datetime import datetime
import os
import time

##############
# QUA macros #
##############


def one_qb_QST(qb: str, len: float, projection_index):
    """
    QUA macro to do single qubit quantum state tomography
    """
    with switch_(projection_index):
        with case_(0):  # projection along X
            play("-y90", qb)
        with case_(1):  # projection along Y
            play("x90", qb)
        with case_(2):  # projection along Z
            wait(len * u.ns, qb)


def plot_1qb_tomography_results(array, xaxis, fig=None, axs=None):
    """
    Helper function to display quantum state tomography data
    """
    if fig is None and axs is None:
        fig, axs = plt.subplots(3, 1, figsize=(12, 8))
    axs = axs.ravel()
    for i in range(3):
        axs[i].cla()
        axs[i].plot(xaxis, array[:, i, 0], label="control |0>")
        axs[i].plot(xaxis, array[:, i, 1], label="control |0>")
        axs[i].set_title(f"<{chr(88 + i)}>")
        axs[i].set_xlabel("CR length [ns]")
        axs[i].set_ylabel("State probability")
    # axs[3].cla()
    # axs[3].plot(xaxis, get_r_vector(array), label='Data dimension 0')
    # axs[3].set_xlabel("CR length [ns]")
    # axs[3].set_ylabel("R-vector")
    plt.tight_layout()
    plt.pause(0.1)
    plt.show()


def two_qb_QST(qb1: str, qb2: str, len1: float, len2: float, projection_index):
    """
    QUA macro to do two-qubit quantum state tomography
    """
    with switch_(projection_index):
        with case_(0):
            play("-y90", qb1)
            play("-y90", qb2)
        with case_(1):
            play("-y90", qb1)
            play("-x90", qb2)
        with case_(2):
            play("-x90", qb1)
            play("-y90", qb2)
        with case_(3):
            play("-x90", qb1)
            play("-x90", qb2)
        with case_(4):
            play("-y90", qb1)
            wait(int(len2 // 4), qb2)
        with case_(5):
            wait(int(len1 // 4), qb1)
            play("-y90", qb2)
        with case_(6):
            play("-x90", qb1)
            wait(int(len2 // 4), qb2)
        with case_(7):
            wait(int(len1 // 4), qb1)
            play("-x90", qb2)
        with case_(8):
            wait(int(len1 // 4), qb1)
            wait(int(len2 // 4), qb2)


def plot_2qb_tomography_results(data_q1, data_q2, xaxis, fig=None, axs=None):
    """
    Helper function to display quantum state tomography data
    """
    # Define the column titles
    col_titles = [
        "<-Y/2-Y/2>",
        "<-Y/2-X/2>",
        "<-X/2-Y/2>",
        "<-X/2-X/2>",
        "<-Y/2,I>",
        "<I,-Y/2>",
        "<-X/2,I>",
        "<I,-X/2>",
        "<I,I>",
    ]

    # Set up the figure and axes if not provided
    if fig is None and axs is None:
        fig, axs = plt.subplots(3, 3, figsize=(12, 12))

    # Loop through the columns in the data array
    for i in range(9):
        # Clear the current axis
        axs[i // 3, i % 3].cla()

        # Get the current column data
        col_data = data_q1[:, i]
        col_data1 = data_q2[:, i]

        # Plot the data on the current axis
        axs[i // 3, i % 3].plot(xaxis, col_data)
        axs[i // 3, i % 3].plot(xaxis, col_data1)

        # Set the x-axis label
        axs[i // 3, i % 3].set_xlabel("CR time [ns]")

        # Set the y-axis label
        axs[i // 3, i % 3].set_ylabel(col_titles[i])

    # Pause for 0.1 seconds
    fig.suptitle("CR power rabi two qubit QST")
    plt.tight_layout()
    plt.show()
    plt.pause(0.1)


def multiplexed_readout(I, I_st, Q, Q_st, resonators, sequential=False, amplitude=1.0, weights=""):
    """Perform multiplexed readout on two resonators"""
    if type(resonators) is not list:
        resonators = [resonators]

    for ind, res in enumerate(resonators):
        measure(
            "readout" * amp(amplitude),
            f"rr{res}",
            None,
            dual_demod.full(weights + "cos", "out1", weights + "sin", "out2", I[ind]),
            dual_demod.full(weights + "minus_sin", "out1", weights + "cos", "out2", Q[ind]),
        )

        if I_st is not None:
            save(I[ind], I_st[ind])
        if Q_st is not None:
            save(Q[ind], Q_st[ind])

        if sequential and ind < len(resonators) - 1:
            align(f"rr{res}", f"rr{res+1}")


def qua_declaration(nb_of_qubits):
    """
    Macro to declare the necessary QUA variables

    :param nb_of_qubits: Number of qubits used in this experiment
    :return:
    """
    n = declare(int)
    n_st = declare_stream()
    I = [declare(fixed) for _ in range(nb_of_qubits)]
    Q = [declare(fixed) for _ in range(nb_of_qubits)]
    I_st = [declare_stream() for _ in range(nb_of_qubits)]
    Q_st = [declare_stream() for _ in range(nb_of_qubits)]
    # Workaround to manually assign the results variables to the readout elements
    for i in range(nb_of_qubits):
        assign_variables_to_element(f"rr{i + 1}", I[i], Q[i])
    return I, I_st, Q, Q_st, n, n_st


def reset_qubit(method: str, qubit: str, resonator: str, **kwargs):
    """
    Macro to reset the qubit state.

    If method is 'cooldown', then the variable cooldown_time (in clock cycles) must be provided as a python integer > 4.

    **Example**: reset_qubit('cooldown', cooldown_times=500)

    If method is 'active', then 3 parameters are available as listed below.

    **Example**: reset_qubit('active', threshold=-0.003, max_tries=3)

    :param method: Method the reset the qubit state. Can be either 'cooldown' or 'active'.
    :param qubit: The qubit element. Must be defined in the config.
    :param resonator: The resonator element. Must be defined in the config.
    :key cooldown_time: qubit relaxation time in clock cycle, needed if method is 'cooldown'. Must be an integer > 4.
    :key threshold: threshold to discriminate between the ground and excited state, needed if method is 'active'.
    :key max_tries: python integer for the maximum number of tries used to perform active reset,
        needed if method is 'active'. Must be an integer > 0 and default value is 1.
    :key Ig: A QUA variable for the information in the `I` quadrature used for active reset. If not given, a new
        variable will be created. Must be of type `Fixed`.
    :return:
    """
    if method == "cooldown":
        # Check cooldown_time
        cooldown_time = kwargs.get("cooldown_time", None)
        if (cooldown_time is None) or (cooldown_time < 4):
            raise Exception("'cooldown_time' must be an integer > 4 clock cycles")
        # Reset qubit state
        wait(cooldown_time, qubit)
    elif method == "active":
        # Check threshold
        threshold = kwargs.get("threshold", None)
        if threshold is None:
            raise Exception("'threshold' must be specified for active reset.")
        # Check max_tries
        max_tries = kwargs.get("max_tries", 1)
        if (max_tries is None) or (not float(max_tries).is_integer()) or (max_tries < 1):
            raise Exception("'max_tries' must be an integer > 0.")
        # Check Ig
        Ig = kwargs.get("Ig", None)
        # Reset qubit state
        return active_reset(threshold, qubit, resonator, max_tries=max_tries, Ig=Ig)


# Macro for performing active reset until successful for a given number of tries.
def active_reset(threshold: float, qubit: str, resonator: str, max_tries=1, Ig=None):
    """Macro for performing active reset until successful for a given number of tries.

    :param threshold: threshold for the 'I' quadrature discriminating between ground and excited state.
    :param qubit: The qubit element. Must be defined in the config.
    :param resonator: The resonator element. Must be defined in the config.
    :param max_tries: python integer for the maximum number of tries used to perform active reset. Must >= 1.
    :param Ig: A QUA variable for the information in the `I` quadrature. Should be of type `Fixed`. If not given, a new
        variable will be created
    :return: A QUA variable for the information in the `I` quadrature and the number of tries after success.
    """
    if Ig is None:
        Ig = declare(fixed)
    if (max_tries < 1) or (not float(max_tries).is_integer()):
        raise Exception("max_count must be an integer >= 1.")
    # Initialize Ig to be > threshold
    assign(Ig, threshold + 2**-28)
    # Number of tries for active reset
    counter = declare(int)
    # Reset the number of tries
    assign(counter, 0)

    # Perform active feedback
    align(qubit, resonator)
    # Use a while loop and counter for other protocols and tests
    with while_((Ig > threshold) & (counter < max_tries)):
        # Measure the resonator
        measure(
            "readout",
            resonator,
            None,
            dual_demod.full("rotated_cos", "out1", "rotated_sin", "out2", Ig),
        )
        # Play a pi pulse to get back to the ground state
        play("x180", qubit, condition=(Ig > threshold))
        # Increment the number of tries
        assign(counter, counter + 1)
    return Ig, counter


# Exponential decay
def expdecay(x, a, t):
    """Exponential decay defined as 1 + a * np.exp(-x / t).

    :param x: numpy array for the time vector in ns
    :param a: float for the exponential amplitude
    :param t: float for the exponential decay time in ns
    :return: numpy array for the exponential decay
    """
    return 1 + a * np.exp(-x / t)


# Theoretical IIR and FIR taps based on exponential decay coefficients
def exponential_correction(A, tau, Ts=1e-9):
    """Derive FIR and IIR filter taps based on a the exponential coefficients A and tau from 1 + a * np.exp(-x / t).

    :param A: amplitude of the exponential decay
    :param tau: decay time of the exponential decay
    :param Ts: sampling period. Default is 1e-9
    :return: FIR and IIR taps
    """
    tau = tau * Ts
    k1 = Ts + 2 * tau * (A + 1)
    k2 = Ts - 2 * tau * (A + 1)
    c1 = Ts + 2 * tau
    c2 = Ts - 2 * tau
    feedback_tap = k2 / k1
    feedforward_taps = np.array([c1, c2]) / k1
    return feedforward_taps, feedback_tap


# FIR and IIR taps calculation
def filter_calc(exponential):
    """Derive FIR and IIR filter taps based on a list of exponential coefficients.

    :param exponential: exponential coefficients defined as [(A1, tau1), (A2, tau2)]
    :return: FIR and IIR taps as [fir], [iir]
    """
    # Initialization based on the number of exponential coefficients
    b = np.zeros((2, len(exponential)))
    feedback_taps = np.zeros(len(exponential))
    # Derive feedback tap for each set of exponential coefficients
    for i, (A, tau) in enumerate(exponential):
        b[:, i], feedback_taps[i] = exponential_correction(A, tau)
    # Derive feddback tap for each set of exponential coefficients
    feedforward_taps = b[:, 0]
    for i in range(len(exponential) - 1):
        feedforward_taps = np.convolve(feedforward_taps, b[:, i + 1])
    # feedforward taps are bounded to +/- 2
    if np.abs(max(feedforward_taps)) >= 2:
        feedforward_taps = 2 * feedforward_taps / max(feedforward_taps)

    return feedforward_taps, feedback_taps