# %%
"""

"""
from qualibrate import QualibrationNode, NodeParameters
from typing import Optional, Literal, List


class Parameters(NodeParameters):
    qubits: Optional[List[str]] = 'q2, q3'
    num_averages: int = 2000
    operation: str = "x180_Square"
    min_amp_factor: float = 0.
    max_amp_factor: float = 1.0
    amp_factor_step: float = 0.005
    flux_point_joint_or_independent: Literal['joint', 'independent'] = "joint"
    simulate: bool = False

node = QualibrationNode(
    name="MW_crosstalk",
    parameters_class=Parameters
)

node.parameters = Parameters()


from qm.qua import *
from qm import SimulationConfig
from qualang_tools.results import progress_counter, fetching_tool
from qualang_tools.plot import interrupt_on_close
from qualang_tools.loops import from_array
from qualang_tools.units import unit
from quam_libs.components import QuAM
from quam_libs.macros import qua_declaration, multiplexed_readout, node_save, readout_state
from quam.components import pulses
import copy
import matplotlib.pyplot as plt
import numpy as np

import matplotlib
from quam_libs.lib.plot_utils import QubitGrid, grid_iter
from quam_libs.lib.save_utils import fetch_results_as_xarray
from quam_libs.lib.fit import fit_oscillation, oscillation
from quam_libs.trackable_object import tracked_updates
from quam_libs.lib.fit import fit_oscillation_decay_exp, oscillation_decay_exp

# matplotlib.use("TKAgg")


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
if node.parameters.qubits is None or node.parameters.qubits == '':
    qubits = machine.active_qubits
else:
    qubits = [machine.qubits[q] for q in node.parameters.qubits.replace(' ', '').split(',')]
num_qubits = len(qubits)


        
###################
# The QUA program #
###################

operation = node.parameters.operation  # The qubit operation to play, can be switched to "x180" when the qubits are found.
n_avg = node.parameters.num_averages  # The number of averages
flux_point = node.parameters.flux_point_joint_or_independent  # 'independent' or 'joint'

tracked_qubits = []
max_amp = 0.25
for i, qubit in enumerate(qubits):
    with tracked_updates(qubit, auto_revert=False, dont_assign_to_none=True) as qubit:
        qubit.xy.operations[operation].amplitude = max_amp
        qubit.xy.operations[operation].length = 220
        tracked_qubits.append(qubit)
config = machine.generate_config()
for tracked_qubit in tracked_qubits:
    tracked_qubit.revert_changes()


# Pulse amplitude sweep (as a pre-factor of the qubit pulse amplitude) - must be within [-2; 2)
amps = np.arange(node.parameters.min_amp_factor,
                 node.parameters.max_amp_factor,
                 node.parameters.amp_factor_step)

with program() as power_rabi:
    n = declare(int)
    n_st = declare_stream()
    state = [declare(int) for _ in range(num_qubits * (num_qubits ))]
    state_stream = [declare_stream() for _ in range(num_qubits * (num_qubits ))]

    
    a = declare(fixed)  # QUA variable for the qubit drive amplitude pre-factor

    qubit_control = qubits[0]
    qubit_target = qubits[1]
    machine.apply_all_flux_to_joint_idle()
    
    with for_(n, 0, n < n_avg, n + 1):
        save(n, n_st)  
        qubit_control.xy.play('x90') 
        align()
        qubit_control.xy.update_frequency(qubit_target.xy.intermediate_frequency)
        qubit_control.xy.play(operation, amplitude_scale=1.0)
        qubit_control.xy.update_frequency(qubit_control.xy.intermediate_frequency)
        align()
        # qubit_control.xy.play('x90') 
        # align()
        readout_state(qubit_target, state[0])
        readout_state(qubit_control, state[1])
        save(state[0], state_stream[0])
        save(state[1], state_stream[1])
        qubit_control.resonator.wait(machine.thermalization_time * u.ns)
        align()

    with stream_processing():
        n_st.save("n")
        state_stream[0].buffer(n_avg).save(f"state1")
        state_stream[1].buffer(n_avg).save(f"state2")



###########################
# Run or Simulate Program #
###########################
simulate = node.parameters.simulate

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=10_000)  # In clock cycles = 4ns
    job = qmm.simulate(config, power_rabi, simulation_config)
    job.get_simulated_samples().con1.plot()
    node.results = {"figure": plt.gcf()}
    node.machine = machine
    node.save()
    quit()
else:
    # Open the quantum machine
    qm = qmm.open_qm(config)
    # Calibrate the active qubits
    # machine.calibrate_octave_ports(qm)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(power_rabi, flags=['auto-element-thread'])
    # Get results from QUA program
    data_list = ["n"] 
    results = fetching_tool(job, data_list, mode="live")
    # Live plotting
    # fig = plt.figure()
    # interrupt_on_close(fig, job)  # Interrupts the job when closing the figure
    while results.is_processing():
        fetched_data = results.fetch_all()
        n = fetched_data[0]
        progress_counter(n, n_avg, start_time=results.start_time)

    # Close the quantum machines at the end in order to put all flux biases to 0 so that the fridge doesn't heat-up
    qm.close()

    plt.show()


# %%
handles = job.result_handles 
ds = fetch_results_as_xarray(handles, qubits, {"n": np.arange(0,n_avg,1)})

# %%

full_state =ds.state.sel(qubit=qubits[0].name) * 2 + ds.state.sel(qubit=qubits[1].name)
hist = np.histogram(full_state, bins=np.arange(0,2*num_qubits+1))
# Plot the histogram
plt.figure(figsize=(10, 6))
plt.bar(hist[1][:-1], hist[0], width=np.diff(hist[1]), align='edge', edgecolor='black')
plt.xlabel('State')
plt.ylabel('Count')
plt.title('Histogram of Qubit States')
plt.xticks(np.arange(0, 2*num_qubits+1))
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Add labels for each state
state_labels = ['|00>', '|01>', '|10>', '|11>']
for i, label in enumerate(state_labels):
    plt.text(i, hist[0][i], label, ha='center', va='bottom')

plt.tight_layout()
plt.show()

# Save the figure to node.results
node.results['histogram'] = plt.gcf()

# %%
# for q in qubits:
#     with node.record_state_updates():
#         pass
# # %%
# node.results['initial_parameters'] = node.parameters.model_dump()
# node.machine = machine
# node.save()
# # %%


