#%%
from qm.qua import *
from qm import SimulationConfig
from qualang_tools.units import unit
from quam_libs.components import QuAM
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import savgol_filter
from qualang_tools.units import unit
from quam_libs.components import QuAM

###################################################
#  Load QuAM and open Communication with the QOP  #
###################################################
# Class containing tools to help handling units and conversions.
u = unit(coerce_to_integer=True)
# Instantiate the QuAM class from the state file
path = "/workspaces/CS_installations/configuration/quam_state"
machine = QuAM.load(path)
# Generate the OPX and Octave configurations
config = machine.generate_config()
octave_config = machine.get_octave_config()
# Open Communication with the QOP
qmm = machine.connect()

qubits = machine.active_qubits

with program() as prog:

    qubits[0].xy.update_frequency(-50e6)
    qubits[1].xy.update_frequency(-100e6)
    qubits[0].resonator.play('const')
    qubits[1].resonator.play('const')


# job = qmm.simulate(config, prog, SimulationConfig(duration=1000))
# job.get_simulated_samples().con1.plot()

qm = qmm.open_qm(config)
job = qm.execute(prog)
# plt.show()


# %%
