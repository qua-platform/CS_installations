# %%
"""
A simple sandbox to showcase different QUA functionalities during the installation.
"""

import matplotlib.pyplot as plt
from qm import QuantumMachinesManager, SimulationConfig
from qm.qua import *

from configuration_with_lffem_csrack import *
# from configuration_with_lffem import *

###################
# The QUA program #
###################
n_avg = 10


with program() as hello_qua:
    # with infinite_loop_():
    #     play("const", "qubit1")
    for pls in [
        "const",
        "saturation",
        "x180_kaiser",
        "x90_kaiser",
        "minus_x90_kaiser",
        "y180_kaiser",
        "y90_kaiser",
        "minus_y90_kaiser",
        "x180_gauss",
        "x90_gauss",
        "minus_x90_gauss",
        "y180_gauss",
        "y90_gauss",
        "minus_y90_gauss",
        "x180_square",
        "x90_square",
        "minus_x90_square",
        "y180_square",
        "y90_square",
        "minus_y90_square",
    ]:
        play(pls, "qubit1")
        play(pls, "qubit2")
        play(pls, "qubit3")
        # play(pls, "qubit4")
        # play(pls, "qubit5")
        wait(50)
        align()

        play(pls, "qp_control_c3t2")
        wait(50)
        align()

    # play("step", "P0", duration=100 * u.ns)
    play("step", "P1", duration=100 * u.ns)
    play("step", "P2", duration=100 * u.ns)
    play("step", "P3", duration=100 * u.ns)
    # play("step", "P4", duration=100 * u.ns)
    wait(50)
    align()

    play("step", "B1", duration=100 * u.ns)
    play("step", "B2", duration=100 * u.ns)
    play("step", "B3", duration=100 * u.ns)
    # play("step", "B4", duration=100 * u.ns)
    wait(50)
    align()

    play("step", "Psd1", duration=100 * u.ns)
    play("step", "Psd2", duration=100 * u.ns)
    wait(50)
    align()

    play("readout", "tank_circuit1", duration=200 * u.ns)
    play("readout", "tank_circuit2", duration=200 * u.ns)
    wait(50)


#####################################
#  Open Communication with the QOP  #
#####################################

qmm = QuantumMachinesManager(host=qop_ip, cluster_name=cluster_name)

###########################
# Run or Simulate Program #
###########################

simulate = False

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=1_000)  # In clock cycles = 4ns
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


# %%
