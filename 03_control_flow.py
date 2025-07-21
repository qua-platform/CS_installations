# %%
from qm import QuantumMachinesManager
from qm.qua import *
from qm.octave import *
from configuration_octave import *
from qm import SimulationConfig
import time
import numpy as np


cond_list = np.random.choice([True, False], size=10)
t_list = np.linspace(10, 100, len(cond_list)).astype(int)
print("Condition list:", cond_list)
print("Time list:", t_list)

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
    t = declare(int)  # QUA variable for the time sweep
    cond = declare(bool)  # QUA variable for the condition
    with for_each_((t, cond), (t_list, cond_list)):
        # Play a pulse if the condition is True
        with if_(cond):
            play("cw", "qubit", duration=t)
        with else_():
            wait(t)

#######################################
# Execute or Simulate the QUA program #
#######################################
simulate = False
if simulate:
    simulation_config = SimulationConfig(duration=400)  # in clock cycles
    job_sim = qmm.simulate(config, prog, simulation_config)
    job_sim.get_simulated_samples().con1.plot()
else:
    qm = qmm.open_qm(config)
    job = qm.execute(prog)
    # Execute does not block python! As this is an infinite loop, the job would run forever.
    # In this case, we've put a 10 seconds sleep and then halted the job.
    time.sleep(10)
    job.halt()

# %%
