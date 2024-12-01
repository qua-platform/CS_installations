"""
        HELLO QUA
A simple sandbox to showcase different QUA functionalities during the installation.
"""

import time
import sys
from qm import SimulationConfig, LoopbackInterface
from qm.qua import *
from qm import QuantumMachinesManager
import matplotlib.pyplot as plt

from quam.components import *
from quam.components.channels import TimeTaggingAddon
from quam.utils import *

qop_ip = "172.16.33.101"
cluster_name = "Cluster_81"
qop_port = None

quam = BasicQuAM()

machine = quam.load(r"C:/Users/BradCole/OneDrive - QM Machines LTD/Documents/Brewery/GitHubPull_testing_Dir/Princeton_QuAM/state.json")
machine.print_summary()
EOM = machine.channels["EOM"]


###################
# The QUA program #
###################

with program() as hello_QUA:
    a = declare(fixed)
    with infinite_loop_():
        with for_(a, 0, a < 1.1, a + 0.05):
            EOM.play("const_pulse", amplitude_scale = a)
            wait(25, "EOM")

#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(host=qop_ip, cluster_name=cluster_name)

###########################
# Run or Simulate Program #
###########################

simulate = True

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=1_000)  # In clock cycles = 4ns
    job_sim = qmm.simulate(machine.generate_config(), hello_QUA, simulation_config) #May need to check machine input for previously generated config
    # Simulate blocks python until the simulation is done
    job_sim.get_simulated_samples().con1.plot()
    plt.show()
else:
    qm = qmm.open_qm(machine.generate_config())
    job = qm.execute(hello_QUA)
    # Execute does not block python! As this is an infinite loop, the job would run forever. In this case, we've put a 10
    # seconds sleep and then halted the job.
    time.sleep(10)
    job.halt()
