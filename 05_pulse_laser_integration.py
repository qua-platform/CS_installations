"""
Pulse sequences can be synchronized to the arrival of an external trigger input from the Ti:sapph laser using the wait_for_trigger() API. The external trigger input is sampled at 250 MHz. 
"""

from configuration import *
from qm import QuantumMachinesManager, SimulationConfig
from qm.qua import *

###################
# The QUA program #
###################
with program() as pulse_laser_triggering:
    with infinite_loop_():
        wait_for_trigger("control_aom")
        play("control", "control_aom")

#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(
    host=opx_ip, port=qop_port, cluster_name=cluster_name, octave=octave_config
)

###########################
# Run or Simulate Program #
###########################

simulate = True

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=10_000)  # In clock cycles = 4ns
    # Simulate blocks python until the simulation is done
    job = qmm.simulate(config, pulse_laser_triggering, simulation_config)
    # Plot the simulated samples
    job.get_simulated_samples().con1.plot()
    plt.show()
else:
    # Open a quantum machine to execute the QUA program
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it - Execute does not block python!
    job = qm.execute(pulse_laser_triggering)
