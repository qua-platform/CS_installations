"""
A simple sandbox to showcase different QUA functionalities during the installation.
"""
#%%
from matplotlib import pyplot as plt
from qm.qua import *
from qm import SimulationConfig
from quam_components import QuAM
from qualang_tools.loops import from_array
import numpy as np
from macros import qua_declaration, multiplexed_readout, node_save

###################################################
#  Load QuAM and open Communication with the QOP  #
###################################################
# Instantiate the QuAM class from the state file
machine = QuAM.load("state.json")
# Generate the OPX and Octave configurations
config = machine.generate_config()
octave_config = machine.octave.get_octave_config()
# Open Communication with the QOP
qmm = machine.connect()
#%%

amplitude = np.arange(0.05,0.5,0.2)
frequency = np.arange(-20e6,20e6,10e6)
###################
# The QUA program #
###################
with program() as saturation:
    I, I_st, Q, Q_st, n, n_st = qua_declaration(nb_of_qubits=2)
    n = declare(int)
    a = declare(fixed)
    df = declare(int)
    a = declare(fixed)
    with for_(n, 0, n < 10, n + 1):
        with for_(*from_array(df,frequency)):
            update_frequency(machine.qubits["q0"].z_sb.name,df+machine.qubits["q0"].z_sb.intermediate_frequency)
            with for_(*from_array(a,amplitude)):
                machine.qubits["q0"].z.play("const",duration=500)
                machine.qubits["q0"].z_sb.play("const",amplitude_scale=a,duration=500)
                machine.qubits["q0"].xy.play("saturation",duration=500)
                align()
                multiplexed_readout(machine, I, I_st, Q, Q_st, sequential=False)


with program() as sideband_driving:
    I, I_st, Q, Q_st, n, n_st = qua_declaration(nb_of_qubits=2)
    n = declare(int)
    a = declare(fixed)
    df = declare(int)
    a = declare(fixed)
    with for_(n, 0, n < 10, n + 1):
        with for_(*from_array(df,frequency)):
            update_frequency(machine.qubits["q0"].z_sb.name,df+machine.qubits["q0"].z_sb.intermediate_frequency)
            with for_(*from_array(a,amplitude)):
                machine.qubits["q0"].xy.play("x180")
                align()
                machine.qubits["q0"].z.play("const",duration=500)
                machine.qubits["q0"].z_sb.play("const",amplitude_scale=a,duration=500)
                align()
                multiplexed_readout(machine, I, I_st, Q, Q_st, sequential=False)


# Simulates the QUA program for the specified duration
simulation_config = SimulationConfig(duration=10000)  # In clock cycles = 4ns
# Simulate blocks python until the simulation is done
job = qmm.simulate(config, sideband_driving, simulation_config)
# Plot the simulated samples
samples = job.get_simulated_samples()
# get the waveform report object
waveform_report = job.get_simulated_waveform_report()
waveform_report.create_plot(samples, plot=True, save_path="./")
