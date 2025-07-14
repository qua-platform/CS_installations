# %%
from qm import QuantumMachinesManager
from qm.qua import *
from qm import SimulationConfig, LoopbackInterface
from configuration import *
import matplotlib.pyplot as plt
from qm_saas import QOPVersion, QmSaas


# Initialize QOP simulator client
client = QmSaas(email=EMAIL, password=PWD, host=HOST)


pulse_len = 250

def phase_coherence_demo():
    """
    Demonstrates ability to preserve phase coherence during frequency update
    and ability to restore to original phase after frequency update.
    """
    # reset_if_phase("qubit_1")
    # reset_if_phase("qubit_2")

    update_frequency("qubit_1", 2.5e6)
    update_frequency("qubit_2", 2.5e6)

    play("x180", "qubit_1", duration=1 * pulse_len)
    play("x180", "qubit_2", duration=4 * pulse_len)

    align()
    play("start", "digital_start", duration=4)

    # update qubit 1 frequency, preserve phase coherence
    update_frequency("qubit_1", 1.0e6)
    frame_rotation_2pi(0.345, "qubit_1")
    play("x180", "qubit_1", duration=2 * pulse_len)
    frame_rotation_2pi(-0.345, "qubit_1")

    align()
    play("start", "digital_start", duration=4)

    # update qubit 1 frequency, restores to original phase (same as qubit_2)
    update_frequency("qubit_1", 2.5e6)
    play("x180", "qubit_1", duration=1 * pulse_len)

    reset_frame("qubit_1")


with client.simulator(QOPVersion(QOP_VER)) as instance:
    # Initialize QuantumMachinesManager with the simulation instance details
    qmm = QuantumMachinesManager(
        host=instance.host,
        port=instance.port,
        connection_headers=instance.default_connection_headers,
    )

    # demo about phase stability and frame rotation
    num_reps = 1
    with program() as prog:
        N = declare(int)

        with for_(N, 0, N < num_reps, N + 1):
            phase_coherence_demo()


    #####################################
    #  Open Communication with the QOP  #
    #####################################

    job = qmm.simulate(config, prog, SimulationConfig(1200))
    samples = job.get_simulated_samples()
    samples.con1.plot()
    plt.show()

# %%

