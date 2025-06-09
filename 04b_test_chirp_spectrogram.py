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
        for i in range(n_tweezers):
            # col
            play("const", f"col_selector_{i + 1:02d}", chirp=(+25, "Hz/nsec"))
            play("const", f"col_selector_{i + 1:02d}", chirp=(-25, "Hz/nsec"))
            # row
            play("const", f"row_selector_{i + 1:02d}", chirp=(+25, "Hz/nsec"))
            play("const", f"row_selector_{i + 1:02d}", chirp=(-25, "Hz/nsec"))
            # done
            wait(250_000)


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
# time.sleep(5)
job.halt()
qm.close()


# %%
