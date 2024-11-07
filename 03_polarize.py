"""
Demo Script for Playing a Polarize Pulse Sequence
"""

from configuration import *
from qm import QuantumMachinesManager, SimulationConfig
from qm.qua import *
from qualang_tools.loops import from_array

# Variables

n_polarize = 5

ti = 16 * u.ns
tf = 200 * u.ns
t_wait = np.arange(ti, tf, 4 * u.ns)

omega_1 = 60 * u.MHz
omega_2 = 80 * u.MHz

###################
# The QUA program #
###################
with program() as polarize:
    n = declare(fixed)
    with for_(n, 0, n < n_polarize, n + 1):
        play("control", "control_aom", duration=30 * u.ns)
        update_frequency("control_aom", omega_1)
        play("control", "control_aom", duration=30 * u.ns)
        align()
        play("readout", "readout_aom", duration=100 * u.ns)
        align()
        play("control", "control_aom", duration=30 * u.ns)
        update_frequency("control_aom", omega_2)
        play("control", "control_aom", duration=30 * u.ns)
        align()
        play("readout", "readout_aom", duration=100 * u.ns)

#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(host=opx_ip, port=qop_port, cluster_name=cluster_name, octave=octave_config)

###########################
# Run or Simulate Program #
###########################

simulate = True

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=10_000)  # In clock cycles = 4ns
    # Simulate blocks python until the simulation is done
    job = qmm.simulate(config, polarize, simulation_config)
    # Plot the simulated samples
    job.get_simulated_samples().con1.plot()
    plt.show()
else:
    # Open a quantum machine to execute the QUA program
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it - Execute does not block python!
    job = qm.execute(polarize)