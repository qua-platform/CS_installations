"""
A simple sandbox to showcase different QUA functionalities during the installation.
"""

from configuration_with_octave import *
from qm import QuantumMachinesManager, SimulationConfig
from qm.qua import *

###################
# The QUA program #
###################
with program() as hello_qua:
    a = declare(fixed)
    I = declare(fixed)
    Q = declare(fixed)
    # update_frequency("rr1", 0.0)
    with for_(a, 0, a < 1.1, a + 0.05):
        play("cw" * amp(a), "q1_xy")
        wait(100, "q1_xy")
        align()
        play("step", "rr1")
        measure("readout", "rr1", None, dual_demod.full("cos", "sin", I), dual_demod.full("minus_sin", "cos", Q))


#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(
    host=qop_ip, port=qop_port, cluster_name=cluster_name, octave=octave_config
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
    waveform_report.create_plot(samples, "con1")
    # plt.show()
else:
    # Open a quantum machine to execute the QUA program
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it - Execute does not block python!
    job = qm.execute(hello_qua)
