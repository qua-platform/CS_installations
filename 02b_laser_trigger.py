# %%
"""
        Laser Trigger
The program triggers the laser to verify the trigger signal.
"""

from qm.QuantumMachinesManager import QuantumMachinesManager
from qm.qua import *
import matplotlib.pyplot as plt
from configuration_with_octave import *
from qm import SimulationConfig


###################
# The QUA program #
###################

with program() as pulse_on:

    with infinite_loop_():
        # Drive the AOM to play the readout laser pulse
        play("laser_ON", "AOM")
        # Waits for the
        wait(1 * u.us, "AOM")


#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(host=qop_ip, port=None, cluster_name=cluster_name, octave=octave_config)

simulate = False

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=10_000)  # In clock cycles = 4ns
    job = qmm.simulate(config, pulse_on, simulation_config)
    plt.figure()
    job.get_simulated_samples().con1.plot()
else:
    # Open Quantum Machine
    qm = qmm.open_qm(config)
    # Execute program
    job = qm.execute(pulse_on)

# %%
