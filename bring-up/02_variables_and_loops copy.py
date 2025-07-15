# %%
from qm import QuantumMachinesManager
from qm.qua import *
from qm.octave import *
from configuration_octave import *
from qm import SimulationConfig
import time
import os


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
    # qua variable
    # int, fixed, bool
    a = declare(fixed)
    b = declare(int)
    # qua loop
    # for_, while_, infinite_loop_, for_each_
    with infinite_loop_():
        with for_(a, 0, a < 2, a + 0.25):
            with for_(b, 0, b < 400, b + 100):
                play("x180" * amp(a), "qubit", duration=b)
                # play("x180" * amp(a), "qubit", duration=b, condition=b < 250)
                wait(25)

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
    # time.sleep(10)
    # job.halt()


# %%
