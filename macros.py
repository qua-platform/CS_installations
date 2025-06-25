from qm.qua import *

from configuration import *


def measure_current():
    """
    Integrate the current measurement through the source-gate and
    transimpedance amplifier, and save it to a stream for data processing.
    """
    i_source = declare(fixed)
    i_source_st = declare_stream()  # The stream to store the raw ADC trace for the DC line
    measure("readout", "source_tia", None, integration.full("constant", i_source, "out1"))
    save(i_source, i_source_st)

    return i_source_st


def measure_lock_in():
    """
    Perform modulated measurement of the source gate and save the
    demodulated I/Q-quadrature values to a stream for data processing.
    """
    I = declare(fixed)
    Q = declare(fixed)

    I_st = declare_stream()
    Q_st = declare_stream()

    reset_phase("source_tia_lock_in")

    measure(
        "readout",
        "source_tia_lock_in",
        None,
        demod.full("cos", I, "out1"),
        demod.full("sin", Q, "out1")
    )
    save(I, I_st)
    save(Q, Q_st)

    return I_st, Q_st


def fetch_results_current(results) -> dict:
    # Fetch the data from the last OPX run corresponding to the current slow axis iteration
    i_source, _ = results.fetch_all()
    i_source = u.demod2volts(i_source, readout_len)
    i_source_A = i_source * tia_iv_scale_factor

    return {
        "readout_source_current_pA": i_source_A
    }


def fetch_results_lock_in(results) -> dict:
    I, Q, _ = results.fetch_all()
    # Convert results into Volts
    S = u.demod2volts(I + 1j * Q, lock_in_length)
    R = np.abs(S)  # Amplitude
    phase = np.angle(S)  # Phase

    return {
        "measured_amplitude_V": R,
        "measured_phase_rad": phase,
    }
