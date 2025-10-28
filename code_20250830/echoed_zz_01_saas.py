# %%
"""
     XYZ
"""

from copy import deepcopy
from qm.qua import *
from qm import QuantumMachinesManager, SimulationConfig
from configuration_mw_fem import *
from qualang_tools.results import fetching_tool
from qualang_tools.loops import from_array
import matplotlib.pyplot as plt
from qualang_tools.results.data_handler import DataHandler
from qm_saas import QOPVersion, QmSaas
import matplotlib

matplotlib.use('TkAgg')

##################
#   Parameters   #
##################

qb1 = "q1_xy"
qb2 = "q2_xy"
n_avg = 3  # The number of averages
durations = np.arange(25, 60, 5)

save_data_dict = {
    "qubit": qb1,
    "durations": durations,
    "n_avg": n_avg,
    "config": config,
}


###################
#   QUA Program   #
###################

# Initialize QOP simulator client
client = QmSaas(email=EMAIL, password=PWD, host=HOST)

with client.simulator(QOPVersion(QOP_VER)) as instance:

    # Initialize QuantumMachinesManager with the simulation instance details
    qmm = QuantumMachinesManager(
        host=instance.host,
        port=instance.port,
        connection_headers=instance.default_connection_headers,
    )

    with program() as PROGRAM:
        n = declare(int)  # QUA variable for the averaging loop
        t = declare(int)  # QUA variable for the readout frequency --> Hz int 32 up to 2^32

        # update_frequency(qb1, 0)
        # update_frequency(qb2, 0)
        with for_(n, 0, n < n_avg, n + 1):  # QUA for_ loop for averaging
            with for_(*from_array(t, durations)):  # QUA for_ loop for sweeping the frequency
                # 1st
                play("const", qb1)
                wait(t, qb1)
                play("const", qb1)
                wait(t, qb1)
                play("const", qb1)
                wait(50)

                # 2nd
                play("const", qb1)
                wait(t, qb1)
                align(qb1, qb2)
                play("const", qb1)
                play("const", qb2)
                wait(t, qb1)
                play("const", qb1)
                wait(50)

    simulate = True
    if simulate:
        simulation_config = SimulationConfig(duration=500)  # In clock cycles = 4ns
        job = qmm.simulate(config, PROGRAM, simulation_config)
        samples = job.get_simulated_samples()
        samples.con1.plot()
        plt.show()

# %%