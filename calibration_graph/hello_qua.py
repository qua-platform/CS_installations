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

with program() as prog:

    qubits[2].xy.update_frequency(-100e6)
    qubits[1].xy.update_frequency(-100e6)
    qubits[0].xy.update_frequency(-100e6)

    a = declare(fixed)

    with infinite_loop_():

        with for_(a, 0, a < 1.0, a +0.1):

            qubits[2].xy.play('x180', amplitude_scale=a)
            qubits[1].xy.play('x180', amplitude_scale=a)
            wait(4)
            align()
            qubits[0].resonator.play('const')
            align()
            wait(4)
        # for qubit in machine.active_qubits:
        #     qubit.z.play('const')
        #     qubit.z.wait(4)

        # with for_(a, 0, a < 2.0, a+0.2):
        # # for qubit in machine.active_qubits:
        #     qubits[2].xy.play('x180', amplitude_scale=a)
        #     qubits[2].xy.wait(4)


# job = qmm.simulate(config, prog, SimulationConfig(duration=1000))
# job.get_simulated_samples().con1.plot()

qm = qmm.open_qm(config)
job = qm.execute(prog)
plt.show()


# %%
