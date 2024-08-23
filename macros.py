"""
This file contains useful QUA macros meant to simplify and ease QUA programs.
All the macros below have been written and tested with the basic configuration. If you modify this configuration
(elements, operations, integration weights...) these macros will need to be modified accordingly.
"""

from qm.qua import *
from typing import Literal
from qualang_tools.addons.variables import assign_variables_to_element
import matplotlib.pyplot as plt
from configuration_with_octave import u, pi_len
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix


##############
# QUA macros #
##############

def prepare_control_state(st: Literal["0", "1"], elem="q1_xy", pi_len: int = pi_len):
    """
    QUA macro to prepare control qubit's state either |0> or |1>
    
    :param st: control state.
    :param elem: element for pi pulse
    :param pi_len: duration of pi pulse (ns)
    """
    # Prepare control state in 1
    if st == "1":
        play("x180", elem)
    # Prepare control state in 0
    else:
        wait(pi_len >> 2, elem)


def play_cr_pulse(
    kind: Literal["direct", "direct+echo", "direct+cancel", "direct+cancel+echo"],
    t, t_half, a=1,
    pi_len: int = pi_len,
    qc="1", qt="2",
):
    """
    QUA macro to form CR sequences
    :param kind: 
        kind = "direct": direct only
        kind = "direct+echo": direct and echo
        kind = "direct+cancel": direct and cancel
        kind = "direct+cancel+echo": full (direct + cancel + echo for each)
    :param t: total duration of cr pulse (cycle)
    :param t_half: half of total duration of cr pulse (cycle)
    :param a: scaling ratio for the amplitude of cr pulse
    :param pi_len: duration of pi pulse (ns)
    :param qc: the control qubit.
    :param qt: the target qubit.
    """

    if qc == "1" and qt == "2":
        qc_xy = "q1_xy"
        qt_xy = "q2_xy"
        cr = "cr_c1t2"
        cr_cancel = "cr_cancel_c1t2"
        rrc = "rr1"
        rrt = "rr2"

    elif qc == "2" and qt == "1":
        qc_xy = "q2_xy"
        qt_xy = "q1_xy"
        cr = "cr_c2t1"
        cr_cancel = "cr_cancel_c2t1"
        rrc = "rr2"
        rrt = "rr1"
    
    else:
        raise ValueError("The assignement of the control and target qubits is invalid")

    align()

    if kind == "direct":
        play("square_positive" * amp(a), cr, duration=t)
        wait(t, qt_xy, "rr1", "rr2")
    
    elif kind == "direct+cancel":
        play("square_positive" * amp(a), cr, duration=t)
        play("square_positive" * amp(a), cr_cancel, duration=t)
        wait(t, qt_xy, rrc, rrt)

    elif kind == "direct+echo":
        play("square_positive" * amp(a), cr, duration=t_half)
        wait(t_half, qc_xy)
        play("x180", qc_xy)
        wait(pi_len >> 2, cr)
        play("square_negative" * amp(a), cr, duration=t_half)
        wait(t_half, qc_xy)
        play("x180", qc_xy)
        wait(t + (pi_len >> 1), qt_xy, rrc, rrt)

    elif kind == "direct+cancel+echo":
        play("square_positive" * amp(a), cr, duration=t_half)
        play("square_positive" * amp(a), cr_cancel, duration=t_half)
        wait(t_half, qc_xy)
        play("x180", qc_xy)
        wait(pi_len >> 2, cr, cr_cancel)
        play("square_negative" * amp(a), cr, duration=t_half)
        play("square_negative" * amp(a), cr_cancel, duration=t_half)
        wait(t_half, qc_xy)
        play("x180", qc_xy)
        wait(t + (pi_len >> 1), qt_xy, rrc, rrt)


def perform_QST_target(bss: Literal["x", "y", "z"], elem="q2_xy", pi_len: int = pi_len):
    """
    QUA macro to perfom QST on the target qubit
    
    :param bss: projection basis and is among "x", "y" and "z".
    :param elem: element for pi pulse
    :param pi_len: duration of pi pulse (ns)
    """
    if bss == "x":
        play("-y90", elem)
    elif bss == "y":
        play("x90", elem)
    else:
        wait(pi_len >> 2, elem)

    wait(pi_len >> 2, "rr1", "rr2")


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


def freq_from_qua_config(element: str, config: dict) -> int:
    element_config = config['elements'][element]
    IF = element_config['intermediate_frequency']
    channel_port = element_config['RF_inputs']['port']
    LO = config['octaves'][channel_port[0]]['RF_outputs'][channel_port[1]]['LO_frequency']

    return LO + IF


def perform_gef_discrimination_blob_mean(Ig, Qg, Ie, Qe, If, Qf, suptitle="qubit 1"):
    """
    Given three blobs in the IQ plane representing g, e, f states,
    finds the averange (mean) point of each blob, classify the label of each data point,
    and computes the confusion matrix of the resulting classification and overall fidelity.
    Plots the raw data of IQ blobs, resulting classification and confusion matrix.

    .. note::
        This function assumes that there are only three blobs in the IQ plane representing gef states (ground, excited, further)

    :param float Ig: A vector containing the `I` quadrature of data points in the ground state
    :param float Qg: A vector containing the `Q` quadrature of data points in the ground state
    :param float Ie: A vector containing the `I` quadrature of data points in the excited state
    :param float Qe: A vector containing the `Q` quadrature of data points in the excited state
    :param float If: A vector containing the `I` quadrature of data points in the further excited state
    :param float Qf: A vector containing the `Q` quadrature of data points in the further excited  state
    :param string suptitle: suptitle for the figure
    :returns: A tuple of (fig, Xg_mean, Xe_mean, Xf_mean, fidelity, y_true, y_pred).
        fig - figure handler.
        Xg_mean - average of g state data.
        Xe_mean - average of e state data.
        Xf_mean - average of f state data.
        fidelity - The fidelity for discriminating the states.
        y_true - ground truth of each data point (0: g, 1: e, 2: f).
        y_pred - predicted labels of each data point (0: g, 1: e, 2: f).
    """
    import numpy as np
    import matplotlib.pyplot as plt
    from sklearn.metrics import confusion_matrix

    Xg = np.column_stack((Ig, Qg))
    Xe = np.column_stack((Ie, Qe))
    Xf = np.column_stack((If, Qf))
    X = np.concatenate([Xg, Xe, Xf], axis=0)

    # Condition to have the Q equal for both states:
    Xg_mean = Xg.mean(axis=0)
    Xe_mean = Xe.mean(axis=0)
    Xf_mean = Xf.mean(axis=0)
    X_mean = np.column_stack((Xg_mean, Xe_mean, Xf_mean))

    Xg_diff = np.mean((Xg[..., None] - X_mean[None, ...]) ** 2, axis=1)
    Xe_diff = np.mean((Xe[..., None] - X_mean[None, ...]) ** 2, axis=1)
    Xf_diff = np.mean((Xf[..., None] - X_mean[None, ...]) ** 2, axis=1)

    yg_pred = Xg_diff.argmin(axis=1)
    ye_pred = Xe_diff.argmin(axis=1)
    yf_pred = Xf_diff.argmin(axis=1)
    y_pred = np.hstack([yg_pred, ye_pred, yf_pred])
    y_true = np.hstack([np.zeros(Xg.shape[0]), np.ones(Xe.shape[0]), 2 * np.ones(Xf.shape[0])])

    fidelity = (y_true == y_pred).mean() # accuracy of classifier

    def plot_IQ(ax, Xg, Xe, Xf, alpha=1.0, no_legend=False):
        if no_legend:
            ax.scatter(Xg[:, 0], Xg[:, 1], color='r', s=10, alpha=alpha, label="_nolegend_")
            ax.scatter(Xe[:, 0], Xe[:, 1], color='g', s=10, alpha=alpha, label="_nolegend_")
            ax.scatter(Xf[:, 0], Xf[:, 1], color='b', s=10, alpha=alpha, label="_nolegend_")
        else:
            ax.scatter(Xg[:, 0], Xg[:, 1], color='r', s=10, alpha=alpha)
            ax.scatter(Xe[:, 0], Xe[:, 1], color='g', s=10, alpha=alpha)
            ax.scatter(Xf[:, 0], Xf[:, 1], color='b', s=10, alpha=alpha)
        ax.set_xlabel("I")
        ax.set_ylabel("Q")
        # ax.set_aspect('eq|ual')

    def plot_confusion_matrix(ax, y_true, y_pred, normalize=True):
        # Generate confusion matrix
        cm = confusion_matrix(y_true, y_pred)

        # Plotting
        cax = ax.matshow(cm, cmap='Blues')
        if normalize:
            # Normalize the confusion matrix by row (by the sum of true instances)
            cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]

        # Annotate the confusion matrix with text
        for (i, j), val in np.ndenumerate(cm):
            if normalize:
                ax.text(j, i, f'{val:3.2f}', ha='center', va='center', color='black')
            else:
                ax.text(j, i, f'{val}', ha='center', va='center', color='black')

        # Set axis labels and title
        ax.set_xlabel('Predicted Labels')
        ax.set_ylabel('True Labels')
        ax.set_xticks(np.arange(len(np.unique(y_true))))
        ax.set_yticks(np.arange(len(np.unique(y_true))))
        ax.set_xticklabels(np.unique(y_true))
        ax.set_yticklabels(np.unique(y_true))
        plt.title('Confusion Matrix')


    fig, axss = plt.subplots(2, 3, figsize=(11, 7))
    plt.suptitle(suptitle, fontsize=16)

    # plot all
    ax = axss[0, 0]
    plot_IQ(axss[0, 0], Xg, Xe, Xf, alpha=1.0)
    ax.set_title("g, e, f states")
    ax.legend(["g", "e", "f"])

    # plot
    ax = axss[0, 1]
    plot_IQ(ax, Xg, Xe, Xf, alpha=0.1, no_legend=True)
    ax.scatter(Xg[yg_pred == 0, 0], Xg[yg_pred == 0, 1], color='r', s=12)
    ax.scatter(Xg[yg_pred != 0, 0], Xg[yg_pred != 0, 1], color='k', s=12)
    ax.set_title("g state classification")
    ax.legend(["g", "not g"])

    # plot
    ax = axss[1, 0]
    plot_IQ(ax, Xg, Xe, Xf, alpha=0.1, no_legend=True)
    ax.scatter(Xe[ye_pred == 1, 0], Xe[ye_pred == 1, 1], color='g', s=12)
    ax.scatter(Xe[ye_pred != 1, 0], Xe[ye_pred != 1, 1], color='k', s=12)
    ax.set_title("e state classification")
    ax.legend(["e", "not e"])

    # plot
    ax = axss[1, 1]
    plot_IQ(ax, Xg, Xe, Xf, alpha=0.1, no_legend=True)
    ax.scatter(Xf[yf_pred == 2, 0], Xf[yf_pred == 2, 1], color='b', s=12)
    ax.scatter(Xf[yf_pred != 2, 0], Xf[yf_pred != 2, 1], color='k', s=12)
    ax.set_title("f state classification")
    ax.legend(["f", "not f"])

    ax = axss[0, 2]
    plot_confusion_matrix(ax, y_true, y_pred, normalize=False)
    ax.set_title("confusion matrix [count]")

    ax = axss[1, 2]
    plot_confusion_matrix(ax, y_true, y_pred, normalize=True)
    ax.set_title("confusion matrix [probability]")

    plt.tight_layout()
    return fig, Xg_mean, Xe_mean, Xf_mean, fidelity, y_true, y_pred


def gef_state_discriminator_blob_mean(I, Q, state, state_st, blob_mean):
    """
    Given three blobs in the IQ plane representing g, e, f states,
    The discrimination is performed by identifying the closest blob mean for each IQ pair.

    .. note::
        This function assumes that there are only three blobs in the IQ plane representing gef states (ground, excited, further)
        Unexpected output will be returned in other cases.

    :param float I: A variable containing the `I` quadrature of data points
    :param float Q: A variable containing the `Q` quadrature of data points
    :param float state: A vector with length 3 (g,e,f) to contain the discriminated states 
    :param float state_st: A stream variable for state
    """
    
    s = declare(int)
    dist = declare(fixed, size=3)
    blob_closest = declare(int)
    xs = declare(fixed, size=3)
    ys = declare(fixed, size=3)
    xs2 = declare(fixed, size=3)
    ys2 = declare(fixed, size=3)

    assign(xs[0], I - blob_mean["g"][0])
    assign(xs[1], I - blob_mean["e"][0])
    assign(xs[2], I - blob_mean["f"][0])
    assign(ys[0], Q - blob_mean["g"][1])
    assign(ys[1], Q - blob_mean["e"][1])
    assign(ys[2], Q - blob_mean["f"][1])

    # (0: g, 1: e, 2: f)
    with for_(s, 0, s < 3, s + 1):
        assign(xs2[s], xs[s] * xs[s])
        assign(ys2[s], ys[s] * ys[s])
        assign(dist[s], xs2[s] + ys2[s])

    assign(blob_closest, Math.argmin(dist))
    
    # (0: g, 1: e, 2: f)
    with for_(s, 0, s < 3, s + 1):
        assign(state[s], blob_closest == s)
        save(state[s], state_st)
