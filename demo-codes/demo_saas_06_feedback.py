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

    # intro to feedback and comprehensive flow
    # message: easy to do feedabck and we can do a lot of math on the FPGA
    with program() as prog:
        a = declare(fixed)
        b = declare(fixed)
        I = declare(fixed)
        Q = declare(fixed)
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
        align()

        with if_(I < 0):
            play("gauss", "qubit_2")
        assign(b, 0.5 + 3 * Math.cos2pi(I * 0.3 + 0.1))

        align()
        play("gauss", "qubit_1", condition=I > b)


    #####################################
    #  Open Communication with the QOP  #
    #####################################

    job = qmm.simulate(config, prog, SimulationConfig(800))
    samples = job.get_simulated_samples()
    samples.con1.plot()
    plt.show()


# %%

