# %%
from qm import QuantumMachinesManager
from qm.qua import *
from qm.octave import *
from configuration_octave import *
from qm import SimulationConfig
import time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import os

matplotlib.use("TkAgg")

amp_list = np.linspace(0.1, 1, 10)

###################################
# Open Communication with the QOP #
###################################
qmm = QuantumMachinesManager(
    host=qop_ip, cluster_name=cluster_name, octave_calibration_db_path=os.getcwd()
)

###################
# The QUA program #
###################
with program() as prog:
    a = declare(fixed)  # QUA variable
    # with for_each_(a, amp_list):
    with infinite_loop_():
        with for_(a, 0, a < 1, a + 0.1):
            play("pi", "qubit1")
            align()
            # # align("qubit1", "qubit2")
            # wait(20, "qubit2")
            play("pi", "qubit2")

            wait(25)
        wait(100)

#######################################
# Execute or Simulate the QUA program #
#######################################
simulate = False
if simulate:
    simulation_config = SimulationConfig(duration=400)  # in clock cycles
    job_sim = qmm.simulate(config, prog, simulation_config)
    job_sim.get_simulated_samples().con1.plot()
    plt.show()
else:
    qm = qmm.open_qm(config)
    job = qm.execute(prog)
    # Execute does not block python! As this is an infinite loop, the job would run forever.
    # In this case, we've put a 10 seconds sleep and then halted the job.
    # time.sleep(10)
    # job.halt()

# %%
