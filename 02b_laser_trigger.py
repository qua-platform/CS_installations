# %%
"""
        Laser Trigger
The program triggers the laser to verify the trigger signal.
"""

from qm import QuantumMachinesManager
from qm.qua import *
from qm import SimulationConfig
from qualang_tools.results import progress_counter, fetching_tool
from qualang_tools.plot import interrupt_on_close
from qualang_tools.loops import from_array
from qualang_tools.results.data_handler import DataHandler
from configuration_with_octave import *
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import time

matplotlib.use('TkAgg')


###################
# The QUA program #
###################

with program() as pulse_on:

    with infinite_loop_():
        # Drive the AOM to play the readout laser pulse
        play("laser_ON", "AOM", duration=1 * u.ms)
        # Waits for the
        # wait(300 * u.ms, "AOM")


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
