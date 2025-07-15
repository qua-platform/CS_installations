# %%
from qm import QuantumMachinesManager
from qm.qua import *
from qm.octave import *
from configuration import *
from qm import SimulationConfig
import time
import numpy as np

amp_list = np.linspace(0, 1, 10)

###################################
# Open Communication with the QOP #
###################################
qmm = QuantumMachinesManager(host=qop_ip, port=qop_port, octave=octave_config)

###################
# The QUA program #
###################
with program() as prog:
    a = declare(fixed)  # QUA variable
    with for_each_((a,), (amp_list,)):
        play("pi" * amp(a), "qubit1")
        align("qubit1", "qubit2")
        play("pi" * amp(a), "qubit2")

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
