# %%
from qm import QuantumMachinesManager
from qm.qua import *
from qm.octave import *
from configuration import *
from qm import SimulationConfig
import time


###################################
# Open Communication with the QOP #
###################################
qmm = QuantumMachinesManager(host=qop_ip, port=qop_port, octave=octave_config)

###################
# The QUA program #
###################
with program() as prog:
    # qua variable
    # int, fixed, bool
    a = declare(fixed)
    # qua loop
    # for_, while_, infinite_loop_, for_each_
    with for_(a, 0, a < 2, a + 0.1):
        play("pi" * amp(a), "qubit1")
        wait(25)

#######################################
# Execute or Simulate the QUA program #
#######################################
simulate = True
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
