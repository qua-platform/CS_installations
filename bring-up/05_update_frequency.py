# %%
"""
hello_octave.py: template for basic usage of the Octave
"""

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
with program() as hello_octave:
    a = declare(int)  # QUA variable for the loop
    with for_(a, 10, a < 350, a + 10):
        update_frequency(
            "qubit1", a * 1e6
        )  # Update the IF frequency of the qubit element
        play("cw", "qubit1", duration=50)  # Play a CW pulse on the qubit element

#######################################
# Execute or Simulate the QUA program #
#######################################
simulate = False
if simulate:
    simulation_config = SimulationConfig(duration=400)  # in clock cycles
    job_sim = qmm.simulate(config, hello_octave, simulation_config)
    job_sim.get_simulated_samples().con1.plot()
else:
    qm = qmm.open_qm(config)
    job = qm.execute(hello_octave)
    # Execute does not block python! As this is an infinite loop, the job would run forever.
    # In this case, we've put a 10 seconds sleep and then halted the job.
    time.sleep(10)
    job.halt()

# %%
