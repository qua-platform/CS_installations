# %%
"""
A simple sandbox to showcase different QUA functionalities during the installation.
"""

from qm.qua import *
from qm.QuantumMachinesManager import QuantumMachinesManager
from qm import SimulationConfig

from configuration import *
# from configuration_with_octave import *


###################
# The QUA program #
###################
with program() as hello_qua:

    play("cw", "rr1")
    align()
    play("cw", "rr2")
    align()
    play("cw", "q1_xy")
    align()
    play("cw", "q2_xy")
    align()
    play("square_positive", "cr_c1t2")
    align()
    play("square_positive", "cr_c2t1")
    align()
    play("square_positive", "cr_cancel_c1t2")
    align()
    play("square_positive", "cr_cancel_c2t1")



#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(
    host=qop_ip,
    port=qop_port,
    cluster_name=cluster_name,
    octave=octave_config,
)

###########################
# Run or Simulate Program #
###########################

simulate = False

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=10_000)  # In clock cycles = 4ns
    # Simulate blocks python until the simulation is done
    job = qmm.simulate(config, hello_qua, simulation_config)
    # Plot the simulated samples
    job.get_simulated_samples().con1.plot()
else:
    # Open a quantum machine to execute the QUA program
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it - Execute does not block python!
    job = qm.execute(hello_qua)

# %%
