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

    # demo about repeat until success
    num_reps = 5
    th0 = 0.2
    with program() as prog:
        n = declare(int)
        I = declare(fixed)
        rus_flag = declare(bool)
        theta = declare(fixed)
        rand = Random(seed=0)

        with for_(n, 0, n < num_reps, n + 1):
            assign(rus_flag, False)
            assign(theta, th0)

            play("start", "digital_start", duration=4)
            align()
            with while_(~rus_flag):
                frame_rotation_2pi(theta, "qubit_1") # wrapping around [-8, 8) in units of 2pi should be fine
                play("gauss", "qubit_1")
                play("gauss", "qubit_2")
                align()
                measure(
                    "readout",
                    "readout_resonator",
                    demod.full("cos", I),
                )

                assign(theta, 2 * theta)
                assign(I, I + rand.rand_fixed() - 0.4) # adding random value to randomize the result
                assign(rus_flag, I < 0)
                wait(25)

            # repeat_until_success()
            reset_frame("qubit_1")
            reset_frame("qubit_2")

    #####################################
    #  Open Communication with the QOP  #
    #####################################

    job = qmm.simulate(
        config, prog,
        SimulationConfig(
            2400, simulation_interface=LoopbackInterface([("con1", 1, "con1", 1)])
        ),
    )
    samples = job.get_simulated_samples()
    samples.con1.plot()
    plt.show()

# %%
