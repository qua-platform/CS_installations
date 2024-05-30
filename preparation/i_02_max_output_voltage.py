from qm.qua import *
from qm import QuantumMachinesManager
from qm import SimulationConfig
from configuration_OPX1000 import *


###################
# The QUA program #
###################
a_min = -1
a_max = 1
da = 0.1
with program() as scan_amp:
    a = declare(fixed)
    play("const", "lf_element_2")
    with for_(a, a_min, a < a_max + da/2, a + da):
        play("const" * amp(a), "lf_element_1")  # 1Vpp
    with for_(a, a_max, a > a_min - da/2, a - da):
        play("const" * amp(a), "lf_element_1")  # 1Vpp

with program() as max_amp:
    with infinite_loop_():
        play("const", "lf_element_2")
        play("up" , "lf_element_1")
        play("down", "lf_element_1")

#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(host=qop_ip, port=qop_port, cluster_name=cluster_name)

###########################
# Run or Simulate Program #
###########################

simulate = False

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=10_000)  # In clock cycles = 4ns
    # Simulate blocks python until the simulation is done
    job = qmm.simulate(config, scan_amp, simulation_config)
    # Plot the simulated samples
    job.get_simulated_samples().con1.plot()
else:
    # Open a quantum machine to execute the QUA program
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it - Execute does not block python!
    job = qm.execute(max_amp)
