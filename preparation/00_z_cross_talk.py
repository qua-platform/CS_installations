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

q0 = machine.active_qubits[0]
q1 = machine.active_qubits[1]

# Frequency detuning sweep in Hz
dfs = np.arange(-10e6, 10e6, 0.1e6)
amps = np.arange(0.05, 1.99, 0.5)
# Idle time sweep (Must be a list of integers) - in clock cycles (4ns)
t_delay = np.arange(4, 300, 4)
xy90_len = machine.qubits['q0'].xy.operations['x90'].length
###################
# The QUA program #
###################
with program() as crosstalk:
    I, I_st, Q, Q_st, n, n_st = qua_declaration(nb_of_qubits=2)
    t = declare(int)
    a = declare(fixed)
    df = declare(int)
    with for_(n, 0, n < 10, n + 1):
        with for_(*from_array(df,dfs)):
            update_frequency(q0.xy.name,df+q0.xy.intermediate_frequency)
            with for_(*from_array(t,t_delay)):
                with for_(*from_array(a, amps)):
                    q0.xy.play('x90')
                    q1.z.play('const',amplitude_scale = a,duration=t+xy90_len*2//4)
                    wait(t)
                    q0.xy.play('x90')
                    align(q0.xy.name,q1.xy.name,q1.resonator.name,q0.resonator.name)
                    wait(4)
                    multiplexed_readout(machine, I, I_st, Q, Q_st, sequential=False)
                    
# Simulates the QUA program for the specified duration
simulation_config = SimulationConfig(duration=10000)  # In clock cycles = 4ns
# Simulate blocks python until the simulation is done
job = qmm.simulate(config, crosstalk, simulation_config)
# Plot the simulated samples
samples = job.get_simulated_samples()
# get the waveform report object
waveform_report = job.get_simulated_waveform_report()
waveform_report.create_plot(samples, plot=True, save_path="./")
#%%