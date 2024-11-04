"""
A simple sandbox to showcase different QUA functionalities during the installation.
"""

from re import T
from configuration import *
from qm import QuantumMachinesManager, SimulationConfig
from qm.qua import *
from qualang_tools.loops import from_array

# Variables

n_rabi = 5

ti = 200 * u.ns
tf = 4 * u.us
t_rabi = np.arange(ti, tf, 200 * u.ns)

omega_rabi = 90 * u.MHz

###################
# The QUA program #
###################
with program() as hello_qua:
    n = declare(fixed)
    t = declare(int)
    play("readout", "readout_aom", duration=100 * u.ns)
    update_frequency("control_aom", omega_rabi)
    with for_(n, 0, n < n_rabi, n + 1):
        with for_(*from_array(t, t_rabi)):
            play("control", "control_aom", duration=t/4)
            align()
            play("readout", "readout_aom", duration=100 * u.ns)




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
    job = qmm.simulate(config, hello_qua, simulation_config)
    # Plot the simulated samples
    job.get_simulated_samples().con1.plot()
    plt.show()
else:
    # Open a quantum machine to execute the QUA program
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it - Execute does not block python!
    job = qm.execute(hello_qua)
