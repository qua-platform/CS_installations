# %%
"""
A simple sandbox to showcase different QUA functionalities during the installation.
"""

import matplotlib.pyplot as plt
from qm import QuantumMachinesManager, SimulationConfig
from qm.qua import *

# from configuration_with_lffem import *
from qualang_tools.voltage_gates import VoltageGateSequence

from configuration_with_lffem import *

# from qm import generate_qua_script
# import matplotlib

# # matplotlib.use('TkAgg')


###################
# The QUA program #
###################
n_avg = 10


with program() as hello_qua:
    n = declare(int)

    with for_(n, 0, n < n_avg, n + 1):
        play("x180_square", "qubit1")
        play("x180_square", "qubit2")
        play("x180_square", "qubit3")
        play("x180_square", "qubit4")
        play("x180_square", "qubit5")
        # align()
        # play("step", "P1", duration=100*u.ns)
        # play("step", "P2", duration=100*u.ns)
        # play("step", "P3", duration=100*u.ns)
        # play("step", "P4", duration=100*u.ns)
        # play("step", "P5", duration=100*u.ns)
        # align()
        # play("step", "B1", duration=100*u.ns)
        # play("step", "B2", duration=100*u.ns)
        # play("step", "B3", duration=100*u.ns)
        # play("step", "B4", duration=100*u.ns)
        # align()
        # play("step", "Psd1", duration=100*u.ns)
        # play("step", "Psd2", duration=100*u.ns)
        # align()
        # play("readout", "tank_circuit1", duration=200*u.ns)
        # play("readout", "tank_circuit2", duration=200*u.ns)
        wait(250)


#####################################
#  Open Communication with the QOP  #
#####################################

# from qm import generate_qua_script
# sourceFile = open('debug.py', 'w')
# print(generate_qua_script(hello_qua, config), file=sourceFile)
# sourceFile.close()

qmm = QuantumMachinesManager(host=qop_ip, port=qop_port, cluster_name=cluster_name, octave=octave_config)

###########################
# Run or Simulate Program #
###########################

simulate = False

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=1_000)  # In clock cycles = 4ns
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


# %%
