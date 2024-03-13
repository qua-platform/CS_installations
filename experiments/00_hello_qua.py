# %%
"""
A simple sandbox to showcase different QUA functionalities during the installation.
"""
from qm.qua import *
from qm.QuantumMachinesManager import QuantumMachinesManager
from qm import SimulationConfig
from configuration import *
import matplotlib.pyplot as plt
from qm import generate_qua_script


###################
# The QUA program #
###################
level_init = [0.1, -0.1]
level_manip = [0.2, -0.2]
level_readout = [0.05, -0.15]
duration_init = 200
duration_manip = 800
duration_readout = 500

seq = OPX_virtual_gate_sequence(config, ["P1_sticky", "P2_sticky"])
seq.add_points("initialization", level_init, duration_init)
seq.add_points("idle", level_manip, duration_manip)
seq.add_points("readout", level_readout, duration_readout)


with program() as hello_qua:
    t = declare(int, value=240)
    a = declare(fixed, value=0.2)
    i = declare(int)
    with strict_timing_():
        seq.add_step(voltage_point_name="initialization")
        seq.add_step(voltage_point_name="idle", duration=t)
        seq.add_step(voltage_point_name="readout")
        seq.add_compensation_pulse(duration=2_000)
    seq.ramp_to_zero()
#

####################################
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
