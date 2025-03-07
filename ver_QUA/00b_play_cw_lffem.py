# %%
"""
A simple sandbox to showcase different QUA functionalities during the installation.
"""

from qm.qua import *
from qm import QuantumMachinesManager
from qm import SimulationConfig
# from configuration_with_lffem_octave import *
from configuration_with_lffem_octave import *
# from configuration_with_opxplus_octave import *
import matplotlib
import time

# matplotlib.use('TkAgg')

###################
# The QUA program #
###################
with program() as hello_qua:
    with infinite_loop_():
        play("readout", "rr1")
        # play("const", "rr2")
        # play("const", "q1_xy")
        # play("const", "q2_xy")


#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(host=qop_ip, port=qop_port, cluster_name=cluster_name)

from pathlib import Path
from qm import generate_qua_script
debug_filepath = sourceFile = f"debug_{Path(__file__).stem}.py"
sourceFile = open(debug_filepath, "w")
print(generate_qua_script(hello_qua, config), file=sourceFile)
sourceFile.close()

###########################
# Run or Simulate Program #
###########################

simulate = False
save_data = True

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
