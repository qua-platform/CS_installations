# %%
"""
hello_octave.py: template for basic usage of the Octave
"""

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
with program() as hello_octave:
    a = declare(int)  # QUA variable for the loop
    with infinite_loop_():
        with for_(a, 1, a < 10, a + 1):
            update_frequency(
                "qubit", a * 1e6
            )  # Update the IF frequency of the qubit element
            play("cw", "qubit", duration=50)  # Play a CW pulse on the qubit element
        wait(200)

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
    time.sleep(20)
    job.halt()
    qm.close()

# %%
