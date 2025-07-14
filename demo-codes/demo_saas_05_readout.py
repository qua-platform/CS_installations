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

    # intro to readout
    # message: easy readout line, demod with weights, but also more type: full, window, sliced etc
    with program() as prog:
        I = declare(fixed)
        Q = declare(fixed)
        a = declare(fixed)
        
        with for_(a, 0, a < 1, a + 0.2):
            play("gauss" * amp(a), "qubit_1")
            align("qubit_1", "qubit_2")
            play("gauss" * amp(a), "qubit_2")

        align()

        measure(
            "readout",
            "readout_resonator",
            demod.full("cos", I),
            demod.full("sin", Q),
        )


    #####################################
    #  Open Communication with the QOP  #
    #####################################

    job = qmm.simulate(config, prog, SimulationConfig(800))
    samples = job.get_simulated_samples()
    samples.con1.plot()
    plt.show()

# %%

