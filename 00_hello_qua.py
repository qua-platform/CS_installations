"""
A simple sandbox to showcase different QUA functionalities during the installation.
"""

from qm.qua import *
from qm import QuantumMachinesManager
from qm import SimulationConfig
from configuration import *
import matplotlib.pyplot as plt

u = unit(coerce_to_integer=True)
dur=16*u.ns

###################
# The QUA program #
###################
with program() as hello_qua:
    a = declare(fixed)
    with infinite_loop_():
        # play("const","dc_flux_line")
        # wait(1000)
        with for_(a, 0, a < 1.1, a + 0.05):
            # reset_global_phase()
            # align()
            # play("const"*amp(0.5),"dc_flux_line", duration=4)
            play("cw" * amp(1), "qubit", duration=dur * u.ns)
            wait(dur * u.ns)
            # ramp_to_zero('dc_flux_line')
        # wait(4, "qubit")

#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(host='172.16.33.107')

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
    # qm.close()
    # Send the QUA program to the OPX, which compiles and executes it - Execute does not block python!
    job = qm.execute(hello_qua)
    qm.close()
