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
    # play("const", "col_selector_01")
    with infinite_loop_():
        # # col
        # play("const", "col_selector_01")
        # play("const", "col_selector_02")
        # play("const", "col_selector_03")
        # play("const", "col_selector_04")
        # # # row
        # play("const", "row_selector_01")
        # play("const", "row_selector_02")
        # play("const", "row_selector_03")
        # play("const", "row_selector_04")
        for i in range(n_tweezers):
            r = (i + 1) / n_tweezers
            play("const" * amp(r), f"col_selector_{i + 1:02d}")
            play("const" * amp(r), f"row_selector_{i + 1:02d}")
        # for i in range(n_tweezers):
        #     play("const", f"col_selector_{i + 1:02d}")
        #     play("const", f"row_selector_{i + 1:02d}")

#####################################
#  Open Communication with the QOP  #
#####################################

qmm = QuantumMachinesManager(host=qop_ip, cluster_name=cluster_name)

from qm import generate_qua_script

sourceFile = open("debug.py", "w")
print(generate_qua_script(hello_QUA, config), file=sourceFile)
sourceFile.close()


# sim_config = SimulationConfig(duration=100)
# job_sim = qmm.simulate(config, hello_QUA, sim_config)
# job_sim.get_simulated_samples().con1.plot()
# plt.show()

qm = qmm.open_qm(config)  # , close_other_machines=False)
job = qm.execute(hello_QUA)
# time.sleep(100)
# job.halt()
# qm.close()


# %%
