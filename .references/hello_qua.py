from qm.qua import *
from qm import QuantumMachinesManager
from qm import SimulationConfig
from configuration import *
import matplotlib.pyplot as plt

with program() as hello_qua:

    # a = declare(fixed)
    # t = declare(int)

    # with for_(t, 32, t < 100, t + 16):
    #     with for_(a, 0, a < 1.0, a + 0.1):
    #         play('step' * amp(a), 'left_plunger', duration = t)
    #         wait(16)

    play('step', 'left_plunger')

    wait(4, 'left_plunger', 'right_plunger')

    play('step', 'right_plunger')


    # play('step'*amp(1.5), 'left_plunger', duration = 200 //4 )

qmm = QuantumMachinesManager(host=qop_ip, port=qop_port, cluster_name=cluster_name, octave=None)

#######################
# Simulate or execute #
#######################
simulate = True

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=10_000)  # In clock cycles = 4ns
    # Simulate blocks python until the simulation is done
    job = qmm.simulate(config, hello_qua, simulation_config)
    # Plot the simulated samples
    job.get_simulated_samples().con1.plot()
    plt.show()

