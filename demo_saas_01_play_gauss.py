# %%
from qm import QuantumMachinesManager
from qm.qua import *
from qm import SimulationConfig, LoopbackInterface
from configuration import *
import matplotlib.pyplot as plt
from qm_saas import QOPVersion, QmSaas
# import matplotlib
# matplotlib.use("TkAgg")


# Initialize QOP simulator client
client = QmSaas(email=EMAIL, password=PWD, host=HOST)


with client.simulator(QOPVersion(QOP_VER)) as instance:
    # Initialize QuantumMachinesManager with the simulation instance details
    qmm = QuantumMachinesManager(
        host=instance.host,
        port=instance.port,
        connection_headers=instance.default_connection_headers,
    )

    # intro play - run simulation
    # message: no points in memory
    with program() as prog:
        play("gauss", "qubit_1")


    #####################################
    #  Open Communication with the QOP  #
    #####################################

    job = qmm.simulate(config, prog, SimulationConfig(150))
    samples = job.get_simulated_samples()
    samples.con1.plot()
    plt.show()


# %%

