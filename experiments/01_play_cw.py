# %%
"""
Drives CW for aom1 to aom5.
"""

from qm.qua import *
from qm.QuantumMachinesManager import QuantumMachinesManager
from qm import SimulationConfig
from configuration import *

###################
# The QUA program #
###################
with program() as drive_cw:
    with infinite_loop_():
        play("cw" * amp(1), "aom1")
        play("cw" * amp(1), "aom2")

#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(host=qop_ip, port=qop_port, cluster_name=cluster_name, octave=octave_config)

###########################
# Run or Simulate Program #
###########################

simulate = False

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=200)  # In clock cycles = 4ns
    # Simulate blocks python until the simulation is done
    job = qmm.simulate(config, drive_cw, simulation_config)
    # Plot the simulated samples
    job.get_simulated_samples().con1.plot()
else:
    # Open a quantum machine to execute the QUA program
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it - Execute does not block python!
    job = qm.execute(drive_cw)

# %%
