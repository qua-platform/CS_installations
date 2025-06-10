# %%
"""
hello_qua.py: template for basic qua program demonstration
"""
from qm.qua import *
from qm import QuantumMachinesManager
from qm import SimulationConfig, LoopbackInterface
from configuration import *
import matplotlib.pyplot as plt
import time


###################
# The QUA program #
###################

with program() as hello_QUA:
    with infinite_loop_():
        play("const", "col_selector_01")
        # for i in range(n_tweezers):
        #     play("const" * amp((i + 1) / n_tweezers), f"col_selector_{i + 1:02d}")
        #     play("const" * amp((i + 1) / n_tweezers), f"row_selector_{i + 1:02d}")
        #     wait(250_000)


#####################################
#  Open Communication with the QOP  #
#####################################

qmm = QuantumMachinesManager(host=qop_ip, cluster_name=cluster_name)

# sim_config = SimulationConfig(duration=1000)
# job_sim = qmm.simulate(config, hello_QUA, sim_config)
# job_sim.get_simulated_samples().con2.plot()
# plt.show()

qm = qmm.open_qm(config)  # , close_other_machines=False)
job = qm.execute(hello_QUA)
time.sleep(5)
job.halt()
qm.close()


# %%
