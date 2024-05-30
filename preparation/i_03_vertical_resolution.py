from qm.qua import *
from qm import QuantumMachinesManager
from qm import SimulationConfig
from configuration_OPX1000 import *


###################
# The QUA program #
###################
with program() as scan_amp:
    a = declare(fixed)
    with infinite_loop_():
        with for_(a, 0, a < 100*2**-16, a + 2**-16):
            play("const" * amp(a), "lf_element_1")  # 1Vpp
            play("const", "lf_element_2")


with program() as ramp_prog:
    a = declare(fixed)
    with infinite_loop_():
        play("const", "lf_element_2")
        with for_(a, 1e-5, a < 5e-4, a + 6e-5):
            play(ramp(a), "lf_element_1", duration=1*u.us)

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
    job = qm.execute(scan_amp)
