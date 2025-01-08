# do it with scope
# %%
"""
A simple protocol to calibrate delay and buffer for digital output for RF switch

intrinsic delay between AO and DO: 136 ns (DO is played faster)

    - params:
        - delay = 116 ns
        - buffer = 20 ns
        - pulse_len = 60 ns
    - want
        - DO is on 40 ns before AO
        - DO ends at the same time as AO
    - equation
        - start: -136 + a - b = A  --> A = -40
        - end: -136 + a + P + b = P
        - -> b = -A/2, a = 136 + A/2
    - result
        - AO is on [0 ns, 60 ns]
        - DO is on [-40 ns, 60 ns]
    - details:
        - t_AO_start = 0 ns
        - t_AO_end = 60ns
        - t_DO_start = -136 ns
        - t_DO_end = -136 ns + 60 ns = -76 ns
        - t_DO_start + delay = -136 ns + 116 ns = -20 ns
        - t_DO_start + delay - buffer = -136 ns + 116 ns - 20 ns = -40 ns
        - t_DO_end + delay = -76 ns + 116 ns = 40 ns
        - t_DO_end + delay - buffer = -76 ns + 100 ns + 20 ns= 60 ns

"""

import matplotlib.pyplot as plt
from qm import QuantumMachinesManager, SimulationConfig
from qm.qua import *

from qualang_tools.voltage_gates import VoltageGateSequence

from configuration_with_lffem import *


###################
# The QUA program #
###################

qubit = "qubit1"
switch_delay = 116
switch_buffer = 20

config["elements"][qubit]["digitalInputs"]["output_switch"]["delay"] = switch_delay
config["elements"][qubit]["digitalInputs"]["output_switch"]["buffer"] = switch_buffer


with program() as rf_swtich_calib:

    play("x180_square", qubit)


#####################################
#  Open Communication with the QOP  #
#####################################

qmm = QuantumMachinesManager(host=qop_ip, port=qop_port, cluster_name=cluster_name, octave=octave_config)

###########################
# Run or Simulate Program #
###########################

simulate = False

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=1_000)  # In clock cycles = 4ns
    # Simulate blocks python until the simulation is done
    job = qmm.simulate(config, rf_swtich_calib, simulation_config)
    # Plot the simulated samples
    job.get_simulated_samples().con1.plot()
    plt.show()
else:
    # Open a quantum machine to execute the QUA program
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it - Execute does not block python!
    job = qm.execute(rf_swtich_calib)


# %%
