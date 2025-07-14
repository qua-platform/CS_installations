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

    # intro QUA var and for loops - run simulation
    # message: no points in memory, QUA variables, keep LO phase
    with program() as prog:
        a = declare(fixed)
        with for_(a, 0, a < 1, a + 0.1):
            play("gauss" * amp(a), "qubit_1")
            wait(25)


    #####################################
    #  Open Communication with the QOP  #
    #####################################

    job = qmm.simulate(config, prog, SimulationConfig(1000))
    samples = job.get_simulated_samples()
    samples.con1.plot()
    plt.show()


# %%

