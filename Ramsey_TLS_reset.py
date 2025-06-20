import numpy as np
from qm.qua import *

parameters = (
    {  # Additional parameters for the program. These values are overwritten by Exopy (section "OPX_config/parameters")
        "averaging": (10000, ""),
        "reset_time": (20000, ""),
        "time_wait": (40, ""),
        "delay": (40, ""),
        "time_min": (16, ""),
        "time_max": (1000, ""),
        "time_step": (16, ""),
    }
)


def get_parameters():
    return parameters


def get_prog(params):
    averaging = int(params["averaging"])
    reset_time = int(params["reset_time"]) // 4
    time_wait = int(params["time_wait"]) // 4
    YN_pulse_amp = float(params["YN_pulse_amp"])
    time_min = float(params["time_min"])
    time_max = float(params["time_max"])
    time_step = int(params["time_step"])

    times = [int(c) for c in np.arange(time_min, time_max + time_step, time_step, dtype=int) // 4]
    delay = int(params["delay"]) // 4
    threshold = float(params["threshold"])
    thresholdpi = float(params["thresholdpi"])

    def reset():
        align("YN", "RO", "Storage")

        assign(count, 1)
        measure("RO_ro", "RO", None, demod.full("RO_square_integW1", I), demod.full("RO_square_integW2", Q))
        wait(reset_time, "RO")

        with while_(I < threshold):
            align("YN", "RO")
            play("short_pi", "YN", condition=I < thresholdpi)
            wait(delay, "YN")
            align("YN", "RO")
            measure("RO_ro", "RO", None, demod.full("RO_square_integW1", I), demod.full("RO_square_integW2", Q))
            assign(count, count + 1)
            wait(reset_time, "RO")

        save(count, count_stream)
        align("YN", "RO", "Storage")

    def reset_cav():
        align("YN", "RO", "Storage")
        assign(count_cav, 1)

        reset()
        play("long_pi_pulse", "YN")
        align("YN", "RO", "Storage")
        wait(delay, "RO")
        measure("RO_ro", "RO", None, demod.full("RO_square_integW1", I), demod.full("RO_square_integW2", Q))

        wait(reset_time, "RO")

        with while_(I > threshold):
            align("YN", "RO", "Storage")

            wait(time_wait, "YN")
            reset()
            play("long_pi_pulse", "YN")
            align("YN", "RO", "Storage")
            wait(delay, "RO")
            measure("RO_ro", "RO", None, demod.full("RO_square_integW1", I), demod.full("RO_square_integW2", Q))
            assign(count_cav, count_cav + 1)

            wait(reset_time, "RO")

        align("YN", "RO", "Storage")

    def meas_TLS():
        reset()
        align("YN", "RO")
        wait(delay, "YN")
        reset_phase("YN")
        play("short_hpi", "YN")
        wait(15546 // 4, "YN")
        play("short_hpi", "YN")
        wait(delay, "YN")

        align("YN", "RO")
        measure("RO_ro", "RO", None, demod.full("RO_square_integW1", I), demod.full("RO_square_integW2", Q))
        wait(reset_time, "RO")

    def reset_TLS():
        assign(tls_count, 0)
        with for_(i, 0, i < 30, i + 1):
            meas_TLS()
            with if_(I < 0):
                assign(tls_count, tls_count + 1)
        reset()
        align("YN", "RO")
        play("long_pi", "YN")
        align("YN", "RO")
        wait(delay, "RO")
        measure("RO_ro", "RO", None, demod.full("RO_square_integW1", I), demod.full("RO_square_integW2", Q))

        wait(reset_time, "RO")
        with while_((tls_count < 20) | (I > (-threshold))):
            assign(tls_count, 0)
            with for_(i, 0, i < 30, i + 1):
                meas_TLS()
                with if_(I < 0):
                    assign(tls_count, tls_count + 1)
            reset()
            align("YN", "RO")
            play("long_pi", "YN")
            align("YN", "RO")
            wait(delay, "RO")
            measure("RO_ro", "RO", None, demod.full("RO_square_integW1", I), demod.full("RO_square_integW2", Q))

            wait(reset_time, "RO")
        save(tls_count, tls_count_stream)
        assign(tls_count, 0)
        align("YN", "RO")

    with program() as prg:
        tls_count = declare(int, value=0)
        tls_count_stream = declare_stream()
        N = declare(int)
        I = declare(fixed)
        Q = declare(fixed)
        t = declare(int)
        i = declare(int)
        count = declare(int)
        count_cav = declare(int)

        count_stream = declare_stream()
        count_cav_stream = declare_stream()

        I1_stream = declare_stream()
        Q1_stream = declare_stream()
        I2_stream = declare_stream()
        Q2_stream = declare_stream()
        time_stream = declare_stream()

        with for_(N, 0, N < averaging, N + 1):

            with for_each_(t, times):
                reset_TLS()

                reset()
                align("YN", "RO")
                wait(delay, "YN")
                reset_phase("YN")
                play("short_hpi", "YN")
                wait(t, "YN")
                play("short_hpi", "YN")
                wait(delay, "YN")

                align("YN", "RO")
                measure("RO_ro", "RO", None, demod.full("RO_square_integW1", I), demod.full("RO_square_integW2", Q))
                save(I, I1_stream)
                save(Q, Q1_stream)
                wait(reset_time, "RO")

                reset()
                align("YN", "RO")
                wait(delay, "YN")

                reset_phase("YN")

                play("short_hpi", "YN")
                wait(t, "YN")
                play("short_hpi" * amp(-1), "YN")
                wait(delay, "YN")

                align("YN", "RO")
                measure("RO_ro", "RO", None, demod.full("RO_square_integW1", I), demod.full("RO_square_integW2", Q))
                save(I, I2_stream)
                save(Q, Q2_stream)
                save(t, time_stream)
                wait(reset_time, "RO")

        with stream_processing():
            I1_stream.buffer(len(times)).average().save("I1")
            Q1_stream.buffer(len(times)).average().save("Q1")
            I2_stream.buffer(len(times)).average().save("I2")
            Q2_stream.buffer(len(times)).average().save("Q2")
            count_stream.buffer(len(times), 2).average().save("count")
            tls_count_stream.buffer(len(times), 2).average().save("tls_count")

            time_stream.buffer(len(times)).multiply_by(4).save("times")

    return prg
