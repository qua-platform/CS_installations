#%%
from qualibrate import QualibrationNode, NodeParameters
from typing import Optional, Literal

class Parameters(NodeParameters):
    qubits: Optional[str] = None
    num_averages: int = 200
    operation: str = "x180"
    min_amp_factor: float = 0.00001
    max_amp_factor: float = 2.0
    amp_factor_step: float = 0.005
    max_number_rabi_pulses_per_sweep: int = 1
    flux_point_joint_or_independent: Literal['joint', 'independent'] = "joint"
    simulate: bool = False

node = QualibrationNode(
    name="fooo",
    parameters_class=Parameters
)

node.parameters = Parameters()

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
path = r"C:\Users\KevinAVillegasRosale\OneDrive - QM Machines LTD\Documents\GitKraken\CS_installations\configuration\quam_state"
machine = QuAM.load()
# Generate the OPX and Octave configurations
config = machine.generate_config()
octave_config = machine.get_octave_config()
# Open Communication with the QOP
qmm = machine.connect()

# Get the relevant QuAM components
if node.parameters.qubits is None or node.parameters.qubits == '':
    qubits = machine.active_qubits
else:
    qubits = [machine.qubits[q] for q in node.parameters.qubits.replace(' ', '').split(',')]
num_qubits = len(qubits)

print('-'*50)
print(qubits[0].xy.name)
print('-'*50)

with program() as prog:

    qubits[0].xy.update_frequency(0)
    qubits[1].xy.update_frequency(0)
    
    qubits[0].xy.play('x180')
    align()
    qubits[1].xy.play('x180')
    # qubits[0].xy.play('x90')
    # qubits[0].xy.play('-x90')
    # qubits[0].xy.play('y180')
    # qubits[0].xy.play('y90')
    # qubits[0].xy.play('-y90')

job = qmm.simulate(config, prog, SimulationConfig(duration=1000))
job.get_simulated_samples().con1.plot()

qm = qmm.open_qm(config)

plt.show()


# %%
