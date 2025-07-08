# %%
from qm import QuantumMachinesManager
from qm.qua import *
from qm import SimulationConfig, LoopbackInterface
from configuration import *
import matplotlib.pyplot as plt
from qm_saas import QOPVersion, QmSaas


# Initialize QOP simulator client
client = QmSaas(email=EMAIL, password=PWD, host=HOST)


with client.simulator(QOPVersion(QOP_VER)) as instance:
    # Initialize QuantumMachinesManager with the simulation instance details
    qmm = QuantumMachinesManager(
        host=instance.host,
        port=instance.port,
        connection_headers=instance.default_connection_headers,
    )

    # intro varying paramters - run simulation
    # message: no points in memory (envelope, ), QUA variables, keep LO phase
    with program() as prog:
        n = declare(int)

        with for_(n, 0, n < 6, n + 1):
            update_frequency("qubit_1", 10e6)
            update_frequency("qubit_2", 10e6)

            play("gauss", "qubit_1", duration=400 // 4)
            play("gauss", "qubit_2", duration=400 // 4)

            frame_rotation_2pi(0.25, "qubit_1")
            wait(25)


    #####################################
    #  Open Communication with the QOP  #
    #####################################

    job = qmm.simulate(config, prog, SimulationConfig(1300))
    samples = job.get_simulated_samples()
    samples.con1.plot()
    plt.show()

# %%

