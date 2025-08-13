import qm.qua as qua
import numpy as np

# amplitude stark shift echo
with qua.program() as prog:

    n = qua.declare(int)
    a = qua.declare(qua.fixed)
    idle = qua.declare(int)
    c = qua.declare(int)
    I = qua.declare(qua.fixed)
    state_st = qua.declare_stream()

    with qua.for_(n, 0, n < 10, n+1):

        with qua.for_(a, 0.0, a < 1.0, a + 0.1):

            with qua.for_(idle, 1_000, idle < 10_000, idle + 1_000):

                with qua.for_(c, 0, c < 2, c+1):

                    qua.play('x90', 'q_t')
                    qua.wait(idle, 'q_t')
                    qua.align()

                    with qua.switch_(c):

                        with qua.case_(0):

                            qua.play('x180', 'q_t')

                        with qua.case_(1):

                            qua.play('x180', 'q_t')
                            qua.play('x180', 'q_c')

                    qua.align()
                    qua.wait(idle, 'q_t')
                    qua.wait(25, 'stark_t', 'stark_c')
                    qua.play('stark' * qua.amp(a), 'stark_t')
                    qua.play('stark' * qua.amp(a), 'stark_c')
                    qua.align()

                    qua.play('x90', 'q_t')

                    qua.align()
                    qua.measure('readout', 'resonator', qua.dual_demod.full('cos', 'sin', I))

    with qua.stream_processing():
        state_st.buffer(2).buffer(len_idle).buffer(len_amps).average().save('state_st')

angle = np.arange(-2*np.pi, 2*np.pi, 0.1)

angle_cos = np.cos(angle).tolist()
angle_sin = np.sin(angle).tolist()

# rotation angle (amp matrix) stark shift echo
with qua.program() as prog1:

    n = qua.declare(int)
    a_counter = qua.declare(qua.fixed)
    idle = qua.declare(int)
    c = qua.declare(int)
    I = qua.declare(qua.fixed)
    state_st = qua.declare_stream()

    angle_cos_var = qua.declare(qua.fixed, value=angle_cos)
    angle_sin_var = qua.declare(qua.fixed, value=angle_sin)

    with qua.for_(n, 0, n < 10, n+1):

        with qua.for_(a_counter, 0, a_counter < len(angle), a_counter + 1):

            with qua.for_(idle, 1_000, idle < 10_000, idle + 1_000):

                with qua.for_(c, 0, c < 2, c+1):

                    qua.play('x90', 'q_t')
                    qua.wait(idle, 'q_t')
                    qua.align()

                    with qua.switch_(c):

                        with qua.case_(0):

                            qua.play('x180', 'q_t')

                        with qua.case_(1):

                            qua.play('x180', 'q_t')
                            qua.play('x180', 'q_c')

                    qua.align()
                    qua.wait(idle, 'q_t')
                    qua.wait(25, 'stark_t', 'stark_c')
                    qua.play('stark', 'stark_t')
                    qua.play('stark' * qua.amp(angle_cos_var[a_counter], -angle_sin_var[a_counter], angle_sin_var[a_counter], angle_cos_var[a_counter]), 'stark_c')
                    # this program will tell you the amplitude matrix needed, but then needs to be translated to I,Q waveform loading so we have a unique operation
                    qua.align()

                    qua.play('x90', 'q_t')

                    qua.align()
                    qua.measure('readout', 'resonator', qua.dual_demod.full('cos', 'sin', I))

    with qua.stream_processing():
        state_st.buffer(2).buffer(len_idle).buffer(len_angles).average().save('state_st')

# CNOT to find trivial phase updates (frame_rotation) for target qubit
with qua.program() as prog3:

    n = qua.declare(int)
    c = qua.declare(int)
    phase = qua.declare(qua.fixed)
    state_st = qua.declare_stream()

    with qua.for_(n, 0, n < 10, n+1):

        with qua.for_(phase, 0, phase < 2*np.pi, phase + 0.1):

            with qua.for_(c, 0, c < 4, c+1):

                with qua.switch_(c):

                    with qua.case_(0):

                        qua.wait(10, 'q_t')
                        qua.wait(10, 'q_c') # prepare 00

                    with qua.case_(1):

                        qua.wait(10, 'q_t')
                        qua.play('x180', 'q_c') # prepare 01

                    with qua.case_(2):

                        qua.play('x180', 'q_t')
                        qua.wait(10, 'q_c') # prepare 10

                    with qua.case_(3):

                        qua.play('x180', 'q_t')
                        qua.play('x180', 'q_c') # prepare 11

                qua.align()

                qua.play('y90', 'q_t') # hadamard
                qua.play('x180', 'q_t')

                qua.align()

                qua.play('cz', 'stark_c')
                qua.play('cz', 'stark_t')

                qua.align()

                qua.frame_rotation_2pi(phase, 'q_t')

                qua.align()

                qua.play('y90', 'q_t') # hadamard
                qua.play('x180', 'q_t')

    with qua.stream_processing():
        state_st.buffer(4).buffer(len_phase).average().save('state_st')

# CNOT to find trivial phase updates (frame_rotation) for control qubit
with qua.program() as prog4:

    n = qua.declare(int)
    c = qua.declare(int)
    phase = qua.declare(qua.fixed)
    state_st = qua.declare_stream()

    with qua.for_(n, 0, n < 10, n+1):

        with qua.for_(phase, 0, phase < 2*np.pi, phase + 0.1):

            with qua.for_(c, 0, c < 4, c+1):

                with qua.switch_(c):

                    with qua.case_(0):

                        qua.wait(10, 'q_t')
                        qua.wait(10, 'q_c') # prepare 00

                    with qua.case_(1):

                        qua.wait(10, 'q_t')
                        qua.play('x180', 'q_c') # prepare 01

                    with qua.case_(2):

                        qua.play('x180', 'q_t')
                        qua.wait(10, 'q_c') # prepare 10

                    with qua.case_(3):

                        qua.play('x180', 'q_t')
                        qua.play('x180', 'q_c') # prepare 11

                qua.align()

                qua.play('y90', 'q_c') # hadamard
                qua.play('x180', 'q_c')

                qua.align()

                qua.play('cz', 'stark_c')
                qua.play('cz', 'stark_t')

                qua.align()

                qua.frame_rotation_2pi(phase, 'q_c')

                qua.align()

                qua.play('y90', 'q_c') # hadamard
                qua.play('x180', 'q_c')

    with qua.stream_processing():
        state_st.buffer(4).buffer(len_phase).average().save('state_st')

# fine calibration of CZ gate
with qua.program() as prog5:

    n = qua.declare(int)
    err = qua.declare(int)

    with qua.for_(n, 0, n < 10, n+1):

        with qua.for_(c, 0, c<1, c+1):

            with qua.switch_(c):

                with qua.case_(0):
                    qua.play('y90', 'q_t')

                with qua.case_(1):
                    qua.play('y90', 'q_t')
                    qua.play('x180', 'q_c')

            qua.align()

            with qua.for_(err, 0, err < 10, err+1):

                qua.play('cz', 'stark_c') # choose parameter to tune
                qua.play('cz', 'stark_t')
                qua.frame_rotation_2pi(calibrated_phase_t, 'q_t')
                qua.frame_rotation_2pi(calibrated_phase_c, 'q_c')

                qua.align()

                with qua.switch_(c):

                    with qua.case_(0):
                        qua.frame_rotation_2pi(1, 'q_t')

                    with qua.case_(1):
                        qua.wait(10, 'q_t')

            qua.align()

            qua.play('x90', 'q_t')