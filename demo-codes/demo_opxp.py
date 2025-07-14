# %%
from qm import QuantumMachinesManager
from qm.qua import *
from qm import SimulationConfig, LoopbackInterface
from configuration import *
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
from qm import generate_qua_script

import matplotlib

matplotlib.use("TkAgg")


def phase_coherence_demo():
    """
    Demonstrates ability to preserve phase coherence during frequency update
    and ability to restore to original phase after frequency update.
    """
    update_frequency("qubit_1", 1e6)
    update_frequency("qubit_2", 2.5e6)

    reset_if_phase("qubit_1")
    reset_if_phase("qubit_2")

    play("x180", "qubit_1", duration=phase_coherence_pulse)
    play("x180", "qubit_2", duration=3 * phase_coherence_pulse)

    # update qubit 1 frequency, preserve phase coherence
    frame_rotation(15.708, "qubit_1")
    update_frequency("qubit_1", 2.5e6)
    frame_rotation_2pi(0.21 / (2 * np.pi), "qubit_1")
    play("x180", "qubit_1", duration=phase_coherence_pulse)

    # update qubit 1 frequency, restores to original phase (same as qubit_2)
    update_frequency("qubit_1", 1e6, keep_phase=False)
    play("x180", "qubit_1", duration=phase_coherence_pulse)

    reset_if_phase("qubit_1")
    reset_if_phase("qubit_2")

    update_frequency("qubit_1", 0)
    update_frequency("qubit_2", 0)


def repeat_until_success():
    """
    Demonstrates real-time demodulation of a signal and feedback
    based on the demodulated phase.
    """
    RUS_round = declare(fixed)
    theta = declare(fixed)
    RUS_flag = declare(bool)
    angle_res = declare(fixed)
    I = declare(fixed)

    assign(RUS_round, 0)
    assign(theta, Random().rand_fixed())
    assign(RUS_flag, False)
    assign(angle_res, 1)
    # repeat until the flag is zero
    reset_frame("qubit_1")
    reset_frame("qubit_2")
    play("gauss", "qubit_1")
    play("gauss", "qubit_2")

    with while_(RUS_flag == False):
        # repeat until success:
        # perform Q1
        # reset_if_phase("qubit_2")
        # frame_rotation_2pi(theta, "qubit_2")
        assign(theta, theta * angle_res)
        frame_rotation_2pi(theta, "qubit_1")
        play("gauss", "qubit_1")
        play("gauss", "qubit_2")
        measure("readout", "readout_resonator", demod.full("cos", I))
        assign(angle_res, angle_res * 2)
        assign(RUS_flag, I < 0)


# intro play - run simulation
# message: no points in memory
with program() as prog_play_gauss:
    play("gauss", "qubit_1")


# intro QUA var and for loops - run simulation
# message: no points in memory, QUA variables, keep LO phase
with program() as prog_amp:
    a = declare(fixed)
    with for_(a, 0, a < 1, a + 0.1):
        play("gauss" * amp(a), "qubit_1")
        wait(25)


# intro varying paramters - run simulation
# message: no points in memory (envelope, ), QUA variables, keep LO phase
with program() as prog_amp_freq_frame:
    a = declare(fixed)
    with for_(a, 0, a < 1, a + 0.25):
        
        update_frequency("qubit_1", 20e6)
        frame_rotation_2pi(0.5, "qubit_1")
        play("gauss" * amp(a), "qubit_1", duration=200 // 4)
        
        update_frequency("qubit_2", 20e6)
        play("gauss" * amp(a), "qubit_2", duration=200 // 4)
        
        wait(25)


# intro to time alignment managment - run simulation
# message: easy to align signals - perhaps example of CR gates?
with program() as prog_align_2Qs:
    a = declare(fixed)
    with for_(a, 0, a < 1, a + 0.25):
        play("gauss", "qubit_1")
        align()
        play("gauss", "qubit_2")
        wait(25)


# intro to readout
# message: easy readout line, demod with weights, but also more type: full, window, sliced etc
with program() as prog_readout:
    a = declare(fixed)
    I = declare(fixed)
    Q = declare(fixed)
    with for_(a, 0, a < 1, a + 0.25):
        play("gauss", "qubit_1")
        align()
        play("gauss", "qubit_2")
        wait(25)

    measure(
        "readout",
        "readout_resonator",
        integration.accumulated("cos", Q, samples_per_chunk=5),
        demod.full("sin", I),
    )


# intro to feedback and comprehensive flow
# message: easy to do feedabck and we can do a lot of math on the FPGA
with program() as prog_feedback:
    a = declare(fixed)
    b = declare(fixed)
    I = declare(fixed)
    Q = declare(fixed)
    with for_(a, 0, a < 1, a + 0.25):
        play("gauss", "qubit_1")
        align("qubit_1", "qubit_2")
        play("gauss", "qubit_2")
        wait(25)
    align()
    measure(
        "readout",
        "readout_resonator",
        integration.accumulated("cos", Q, samples_per_chunk=5),
        demod.full("sin", I),
    )
    align("readout_resonator", "qubit_2")

    with if_(I < 0):
        play("gauss", "qubit_2")
    assign(b, 0.5 + 3 * Math.cos2pi(I * 0.3 + 0.1))

    align("qubit_1", "qubit_2")
    play("gauss", "qubit_1", condition=I > b)


# demo about phase stability and frame rotation
num_reps = 1
with program() as prog_phase_coherence:
    N = declare(int)

    with for_(N, 0, N < num_reps, N + 1):
        play("start", "digital_start", duration=10)
        align("qubit_1", "qubit_2", "digital_start")

        wait(25, "qubit_1", "qubit_2")
        phase_coherence_demo()

        wait(25, "qubit_1", "qubit_2")


# demo about repeat until success
num_reps = 5
with program() as prog_rus:
    N = declare(int)

    with for_(N, 0, N < num_reps, N + 1):
        play("start", "digital_start", duration=10)
        align("qubit_1", "qubit_2", "digital_start")

        wait(25, "qubit_1", "qubit_2")
        repeat_until_success()

        wait(25, "qubit_1", "qubit_2")


#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(host=qop_ip, cluster_name=cluster_name)

simulate = True

prog, duration = prog_play_gauss, 150
# prog, duration = prog_amp, 1000
# prog, duration = prog_amp_freq_frame, 1000
# prog, duration = prog_align_2Qs, 500
# prog, duration = prog_readout, 500
# prog, duration = prog_feedback, 500
# prog, duration = prog_phase_coherence, 500
# prog, duration = prog_rus, 500


# if simulate:
#     # Simulates the QUA program for the specified duration
#     simulation_config = SimulationConfig(duration=10_000)  # In clock cycles = 4ns
#     job = qmm.simulate(config, PROGRAM, simulation_config)
#     job.get_simulated_samples().con1.plot()
#     plt.show(block=False)

job = qmm.simulate(
    config,
    prog,    
    SimulationConfig(duration),
    # SimulationConfig(
    #     duration, simulation_interface=LoopbackInterface([("con1", 1, "con1", 1)])
    # ),
)
samples = job.get_simulated_samples()
# waveform_report = job.get_simulated_waveform_report()
# waveform_report.create_plot(samples, plot=True, save_path="./")
samples.con1.plot()
plt.show()

qmm.close_all_qms()
qmm.clear_all_job_results()
qmm.close()



# sourceFile = open("debug.py", "w")
# print(generate_qua_script(prog, config), file=sourceFile)
# sourceFile.close()

# %%