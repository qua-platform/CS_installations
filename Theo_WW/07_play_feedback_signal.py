from qm.qua import *
from qm.QuantumMachinesManager import QuantumMachinesManager
from qm import SimulationConfig
from configuration import *


###################
# The QUA program #
###################

with program() as drive_flux:
    # with infinite_loop_():
    update_frequency("flux_line_sticky", 1e6)
    play("const", "flux_line_sticky", duration=4)
    play("const"*amp(0), "flux_line_sticky", duration=1000)
    # wait(1000, "flux_line_sticky")
    frame_rotation_2pi(0.1, "flux_line_sticky")
    wait(1000, "flux_line_sticky")
    ramp_to_zero("flux_line_sticky", 1)


#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(host=qop_ip, port=qop_port, cluster_name=cluster_name, octave=octave_config)

#######################
# Simulate or execute #
#######################
simulate = True

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=10_000)  # In clock cycles = 4ns
    job = qmm.simulate(config, drive_flux, simulation_config)
    job.get_simulated_samples().con1.plot()
else:
    # Open the quantum machine
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(drive_flux)
