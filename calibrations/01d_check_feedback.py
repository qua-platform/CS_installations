from pathlib import Path
from qm.qua import *
from qm import SimulationConfig
from qualang_tools.units import unit
from quam_libs.components import QuAM
from quam_libs.macros import node_save
import matplotlib.pyplot as plt
import numpy as np
from qualang_tools.results import fetching_tool, progress_counter
from scipy import signal
import matplotlib
from quam_libs.macros import qua_declaration, multiplexed_readout, node_save

matplotlib.use("TKAgg")


###################################################
#  Load QuAM and open Communication with the QOP  #
###################################################
# Class containing tools to help handling units and conversions.
u = unit(coerce_to_integer=True)
# Instantiate the QuAM class from the state file
machine = QuAM.load()
# Generate the OPX and Octave configurations
config = machine.generate_config()
octave_config = machine.get_octave_config()
# Open Communication with the QOP
qmm = machine.connect()

# Get the relevant QuAM components

qubit = machine.qubits["q0"]
qubit_fem2 = machine.qubits["q1"]
###################
# The QUA program #
###################
n_avg = 2  # The number of averages


with program() as repeated_readout:
    n = declare(int)  # QUA variable for the averaging loop
    n_st = declare_stream()
    n1 = declare(int)  # QUA variable for the averaging loop
    # Here we define one 'I', 'Q', 'I_st' & 'Q_st' for each resonator via a python list
    I = declare(fixed)
    Q = declare(fixed)
    I_st = declare_stream()
    Q_st = declare_stream()

    qubit.resonator.measure('readout', qua_vars=(I, Q))
    qubit.xy.play("x180", condition=I>-1)


###########################
# Run or Simulate Program #
###########################

simulate = True

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=10_000)  # In clock cycles = 4ns
    # Simulate blocks python until the simulation is done
    job = qmm.simulate(config, repeated_readout, simulation_config)
    # Plot the simulated samples
    job.get_simulated_samples().con1.plot()

else:
    # Open a quantum machine to execute the QUA program
    qm = qmm.open_qm(config)

    job = qm.execute(repeated_readout)

