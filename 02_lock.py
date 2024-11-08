"""
Demo Script for Playing a Lock Pulse Sequence
"""

from configuration import *
from qm import QuantumMachinesManager, SimulationConfig
from qm.qua import *
from qualang_tools.loops import from_array

# Variables

n_locks = 100

ti = 20
tf = 200
t_wait = np.arange(ti, tf, 16)

###################
# The QUA program #
###################
with program() as hello_qua:
    n = declare(fixed)
    t = declare(int)
    with for_(n, 0, n < n_locks, n + 1):
        with for_(*from_array(t, t_wait)):
            play("control", "control_aom", duration=30 * u.ns)
            wait(16 * u.ns, "control_aom")
            play("control", "control_aom", duration=60 * u.ns)
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
    samples = job.get_simulated_samples()
    waveform_report = job.get_simulated_waveform_report()
    waveform_report.create_plot(samples, plot=True, save_path="./")
    plt.show()
else:
    # Open a quantum machine to execute the QUA program
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it - Execute does not block python!
    job = qm.execute(hello_qua)
