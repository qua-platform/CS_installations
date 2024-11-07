# %%

from qm.qua import *
from qm import QuantumMachinesManager
from qm import SimulationConfig
from configuration import *
import matplotlib.pyplot as plt


###################
# The QUA program #
###################

# ts = [10 * u.ms, 50 * u.ms, 100 * u.ms, 1 * u.s]
ts = [
    10 * u.ms // 4,
    50 * u.ms // 4,
    100 * u.ms // 4,
]

with program() as PROGRAM:
    t = declare(int)

    with for_each_(t, ts):
        play("const", "cooling_fm", duration=t) # works
        wait(10 * u.ms)


#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(host=qop_ip, port=qop_port, cluster_name=cluster_name)


###########################
# Run or Simulate Program #
###########################

simulate = False

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=10_000)  # In clock cycles = 4ns
    # Simulate blocks python until the simulation is done
    job = qmm.simulate(config, PROGRAM, simulation_config)
    # Plot the simulated samples
    job.get_simulated_samples().con1.plot()
else:
    # Open a quantum machine to execute the QUA program
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it - Execute does not block python!
    job = qm.execute(PROGRAM)

# %%
