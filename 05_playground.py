"""
A simple sandbox to showcase different QUA functionalities during the installation.
"""

import matplotlib.pyplot as plt
from configuration import *
from qm import QuantumMachinesManager, SimulationConfig
from qm.qua import *

###################
# The QUA program #
###################


with program() as hello_qua:

    a = declare(fixed)
    assign(a, 0.4)
    with infinite_loop_():

        play("cw" * amp(0.4), "resonator", duration=1000//4)
        wait(250, "resonator")

#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(host=qop_ip, port=qop_port, cluster_name=cluster_name, octave=octave_config)

###########################
# Run or Simulate Program #
###########################

simulate = True

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=10000 >> 2)  # In clock cycles = 4ns
    # Simulate blocks python until the simulation is done
    job = qmm.simulate(config, hello_qua, simulation_config)
    # Plot the simulated samples
    job.get_simulated_samples().con1.plot()
    plt.show()
else:
    # Open a quantum machine to execute the QUA program
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it - Execute does not block python!
    job = qm.execute(hello_qua)
