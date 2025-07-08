# %%
"""
A simple sandbox to showcase different QUA functionalities during the installation.
"""

from qm.qua import *
from qm import QuantumMachinesManager
from qm import SimulationConfig

from configuration_with_lf_fem import *
from qualang_tools.voltage_gates import VoltageGateSequence
import matplotlib.pyplot as plt
from qm import generate_qua_script
import matplotlib

matplotlib.use('TkAgg')


###################
# The QUA program #
###################
n_avg = 100


with program() as hello_qua:
    n = declare(int)

    with for_(n, 0, n < n_avg, n + 1):
        play("cw", "qubit")
        # wait(100, "P1")
        # wait(448//4, "P1")
        play("step", "P1")
        wait(250)


#####################################
#  Open Communication with the QOP  #
#####################################

# from qm import generate_qua_script
# sourceFile = open('debug.py', 'w')
# print(generate_qua_script(hello_qua, config), file=sourceFile)
# sourceFile.close()

qmm = QuantumMachinesManager(
    host=qop_ip, port=qop_port, cluster_name=cluster_name, octave=octave_config
)

###########################
# Run or Simulate Program #
###########################

simulate = True

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








0# %%

# %%
