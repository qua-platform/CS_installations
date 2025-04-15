"""
A simple sandbox to showcase different QUA functionalities during the installation.
"""

from qm.qua import *
from qm import SimulationConfig
from quam_builder import Quam
import matplotlib.pyplot as plt
from qualang_tools.units import unit
from pathlib import Path
import numpy as np
from qualang_tools.voltage_gates import VoltageGateSequence
from qualang_tools.loops import from_array

machine = Quam.load("state.json")
u = unit(coerce_to_integer=True)
config = machine.generate_config()

##################
#   Parameters   #
##################
# Parameters Definition

###################
# The QUA program #
###################
qubit = machine.qubits["q1"]

level_init = [qubit.p1.level_init, qubit.p2.level_init]
level_manip = [qubit.p1.level_idle, qubit.p2.level_idle]
level_readout = [qubit.p1.level_readout, qubit.p2.level_readout]
duration_init = 200
duration_manip = 800
duration_readout = 500
# Add the relevant voltage points describing the "slow" sequence (no qubit pulse)
seq = VoltageGateSequence(config, [qubit.p1.name, qubit.p2.name])
seq.add_points("initialization", level_init, duration_init)
seq.add_points("idle", level_manip, duration_manip)
seq.add_points("readout", level_readout, qubit.resonator.operations["readout"].length)

durations = np.arange(16, 1000, 40)
with program() as hello_qua:
    t = declare(int, value=16)
    a = declare(fixed, value=0.2)
    i = declare(int)
    qubit.qdac_trigger.play("trigger")
    align()
    with for_(*from_array(t, durations)):
        align()
        seq.add_step(voltage_point_name="initialization")
        seq.add_step(voltage_point_name="idle", duration=t)
        seq.add_step(voltage_point_name="readout")
        seq.add_compensation_pulse()
        seq.ramp_to_zero()
        qubit.resonator.wait((duration_init) // 4 + (t >> 2))
        qubit.resonator.measure("readout")


#####################################
#  Open Communication with the QOP  #
#####################################
qmm = machine.connect()

###########################
# Run or Simulate Program #
###########################

simulate = True

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=10_000)  # In clock cycles = 4ns
    # Simulate blocks python until the simulation is done
    job = qmm.simulate(config, hello_qua, simulation_config)
    # Get the simulated samples
    samples = job.get_simulated_samples()
    # Plot the simulated samples
    samples.con1.plot()
    # Get the waveform report object
    waveform_report = job.get_simulated_waveform_report()
    # Cast the waveform report to a python dictionary
    waveform_dict = waveform_report.to_dict()
    # Visualize and save the waveform report
    waveform_report.create_plot(
        samples, plot=True, save_path=str(Path(__file__).resolve())
    )
else:
    # Open a quantum machine to execute the QUA program
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it - Execute does not block python!
    job = qm.execute(hello_qua)
