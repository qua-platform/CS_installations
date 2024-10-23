"""
A simple sandbox to showcase different QUA functionalities during the installation.
"""

import matplotlib.pyplot as plt
from configuration.make_quam import qpu
from qm import QuantumMachinesManager, SimulationConfig
from qm.qua import *

###################
# The QUA program #
###################

qubit = qpu.channels["qubit_xy"]

with program() as hello_qua:
    a = declare(fixed)
    with infinite_loop_():
        with for_(a, 0, a < 1.1, a + 0.05):
            qubit.play("square", amplitude_scale=a)
        qubit.wait(25)

#####################################
#  Open Communication with the QOP  #
#####################################

qmm = QuantumMachinesManager(
    host="172.16.33.101",  # TODO: could this not be hardcoded?
    cluster_name="Cluster_81",
    octave=qpu.octaves["octave1"].get_octave_config(),
)

###########################
# Run or Simulate Program #
###########################

simulate = True

config = qpu.generate_config()
if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=10_000)  # In clock cycles = 4ns
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
