# %%
from qm import QuantumMachinesManager
from qm.qua import *
from qm import SimulationConfig, LoopbackInterface
from configuration_intro import *
import matplotlib.pyplot as plt
from qm_saas import QOPVersion, QmSaas
import matplotlib

matplotlib.use("TkAgg")


# Initialize QOP simulator client
client = QmSaas(email=EMAIL, password=PWD, host=HOST)
client.close_all()

with client.simulator(QOPVersion(QOP_VER)) as instance:
    # Initialize QuantumMachinesManager with the simulation instance details
    qmm = QuantumMachinesManager(
        host=instance.host,
        port=instance.port,
        connection_headers=instance.default_connection_headers,
    )

    # intro to time alignment managment - run simulation
    # message: easy to align signals - perhaps example of CR gates?
    with program() as prog:
        # play("gauss", "qubit_1")
        # align("qubit_1", "qubit_2")
        # play("gauss", "qubit_2")

        update_frequency("qubit_1", 0)
        update_frequency("qubit_2", 0)

        play("x180", "qubit_1")
        align("qubit_1", "qubit_2")
        play("x180", "qubit_2")


    #####################################
    #  Open Communication with the QOP  #
    #####################################

    job = qmm.simulate(config, prog, SimulationConfig(300))
    samples = job.get_simulated_samples()
    samples.con1.plot()
    plt.show()


# %%

