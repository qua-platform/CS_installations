"""
A simple sandbox to showcase different QUA functionalities during the installation.
"""

from pathlib import Path
from qm.qua import *
from qm import SimulationConfig
from quam_libs.components import QuAM
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')
###################################################
#  Load QuAM and open Communication with the QOP  #
###################################################
# Instantiate the QuAM class from the state file
machine = QuAM.load("C:\Git\QM-CS-Michal\Customers\Lincoln_Labs\configuration\quam_state")

# Generate the OPX and Octave configurations
config = machine.generate_config()
octave_config = machine.get_octave_config()
# Open Communication with the QOP
qmm = machine.connect()

qubit = machine.qubits["q0"]  # The element
###################
# The QUA program #
###################
with program() as hello_qua:
    a = declare(fixed)
    # with infinite_loop_():
    with for_(a, 0.1, a < 1.1, a + 0.05):
        qubit.xy.play("x180", amplitude_scale=a)
    qubit.xy.wait(25)
    align()

qubits = machine.qubits
with program() as test:
    with infinite_loop_():
        qubits["q0"].xy.play("const")
        qubits["q1"].xy.play("const")
        qubits["q2"].xy.play("const")
        qubits["q0"].resonator.play("const")

###########################
# Run or Simulate Program #
###########################

simulate = False

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=1000)  # In clock cycles = 4ns
    # Simulate blocks python until the simulation is done
    job = qmm.simulate(config, hello_qua, simulation_config)
    # Plot the simulated samples
    job.get_simulated_samples().con1.plot()
    plt.show()
else:
    # Open a quantum machine to execute the QUA program
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it - Execute does not block python!
    job = qm.execute(test)



from qm import generate_qua_script
sourceFile = open('plot_simulation_bug.py', 'w')
print(generate_qua_script(hello_qua, config), file=sourceFile)
sourceFile.close()