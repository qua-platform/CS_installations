"""
        POWER RABI WITH ERROR AMPLIFICATION
This sequence involves repeatedly executing the qubit pulse (such as x180) 'N' times and
measuring the state of the resonator across different qubit pulse amplitudes and number of pulses.
By doing so, the effect of amplitude inaccuracies is amplified, enabling a more precise measurement of the pi pulse
amplitude. The results are then analyzed to determine the qubit pulse amplitude suitable for the selected duration.

Prerequisites:
    - Having found the resonance frequency of the resonator coupled to the qubit under study (resonator_spectroscopy).
    - Having calibrated the IQ mixer connected to the qubit drive line (external mixer or Octave port)
    - Having found the rough qubit frequency and set the desired pi pulse duration (qubit spectroscopy).
    - Set the desired flux bias

Next steps before going to the next node:
    - Update the qubit pulse amplitude in the state.
    - Save the current state
"""

# %% {Imports}
from datetime import datetime
from qualibrate import QualibrationNode, NodeParameters
from quam_libs.components import QuAM
from quam_libs.macros import qua_declaration, active_reset
from quam_libs.lib.instrument_limits import instrument_limits
from quam_libs.lib.qua_datasets import convert_IQ_to_V
from quam_libs.lib.plot_utils import QubitGrid, grid_iter
from quam_libs.lib.save_utils import fetch_results_as_xarray, load_dataset, get_node_id
from quam_libs.lib.fit import fit_oscillation, oscillation
from qualang_tools.results import progress_counter, fetching_tool
from qualang_tools.loops import from_array
from qualang_tools.multi_user import qm_session
from qualang_tools.units import unit
from qm import SimulationConfig
from qm.qua import *
from typing import Literal, Optional, List
import matplotlib.pyplot as plt
import numpy as np


# %% {Node_parameters}
class Parameters(NodeParameters):
    qubits: Optional[List[str]] = None
    num_averages: int = 10
    operation_x180_or_any_90: Literal["x180_Cosine", "x90_Cosine"] = "x180_Cosine"
    min_amp_factor: float = 0.0
    max_amp_factor: float = 1.5
    amp_factor_step: float = 0.05
    max_number_rabi_pulses_per_sweep: int = 1
    flux_point_joint_or_independent: Literal["joint", "independent"] = "joint"
    reset_type_thermal_heralding_or_active: Literal["thermal", "active", "heralding"] = "heralding"
    state_discrimination: bool = True
    update_x90: bool = True
    simulate: bool = False
    simulation_duration_ns: int = 2500
    timeout: int = 100
    load_data_id: Optional[int] = None
    multiplexed: bool = True


node = QualibrationNode(name="04_Power_Rabi", parameters=Parameters())
node_id = get_node_id()

# %% {Initialize_QuAM_and_QOP}
# Class containing tools to help handling units and conversions.
u = unit(coerce_to_integer=True)
# Instantiate the QuAM class from the state file
path = r"C:\Git\CS_installations\qualibrate\configuration\quam_state"
machine = QuAM.load(path)
# Generate the OPX and Octave configurations
config = machine.generate_config()
# Open Communication with the QOP
if node.parameters.load_data_id is None:
    qmm = machine.connect()

# Get the relevant QuAM components
if node.parameters.qubits is None or node.parameters.qubits == "":
    qubits = machine.active_qubits
else:
    qubits = [machine.qubits[q] for q in node.parameters.qubits]
num_qubits = len(qubits)

# %% {QUA_program}
n_avg = node.parameters.num_averages  # The number of averages
N_pi = node.parameters.max_number_rabi_pulses_per_sweep  # Number of applied Rabi pulses sweep
flux_point = node.parameters.flux_point_joint_or_independent  # 'independent' or 'joint'
reset_type = node.parameters.reset_type_thermal_heralding_or_active  # "thermal", "heralding" or "active"
state_discrimination = node.parameters.state_discrimination
operation = node.parameters.operation_x180_or_any_90  # The qubit operation to play
# Pulse amplitude sweep (as a pre-factor of the qubit pulse amplitude) - must be within [-2; 2)
amps = np.arange(
    node.parameters.min_amp_factor,
    node.parameters.max_amp_factor,
    node.parameters.amp_factor_step,
)

# Number of applied Rabi pulses sweep
if N_pi > 1:
    if operation == "x180_Cosine":
        N_pi_vec = np.arange(1, N_pi, 2).astype("int")
    elif operation in ["x90_Cosine", "-x90_Cosine", "y90_Cosine", "-y90_Cosine"]:
        N_pi_vec = np.arange(2, N_pi, 4).astype("int")
    else:
        raise ValueError(f"Unrecognized operation {operation}.")
else:
    N_pi_vec = np.linspace(1, N_pi, N_pi).astype("int")[::2]

with program() as power_rabi:
    a = declare(int)
    b = declare(int)
    c = declare(int)
    c_st = declare_stream()
    assign(a, 0)
    assign(b, 1)
    assign(c, a ^ b)
    save(c, c_st)
    with stream_processing():
        c_st.save_all("test")


#

date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# with qm_session(qmm, config, timeout=node.parameters.timeout) as qm:
qm = qmm.open_qm(config)
job = qm.execute(power_rabi)
res = job.result_handles
res.wait_for_all_values()
t = res.test.fetch_all()
