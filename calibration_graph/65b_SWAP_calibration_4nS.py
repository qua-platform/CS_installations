# %%
"""
Two-Qubit Readout Confusion Matrix Measurement

This sequence measures the readout error when simultaneously measuring the state of two qubits. The process involves:

1. Preparing the two qubits in all possible combinations of computational basis states (|00⟩, |01⟩, |10⟩, |11⟩)
2. Performing simultaneous readout on both qubits
3. Calculating the confusion matrix based on the measurement results

For each prepared state, we measure:
1. The readout result of the first qubit
2. The readout result of the second qubit

The measurement process involves:
1. Initializing both qubits to the ground state
2. Applying single-qubit gates to prepare the desired input state
3. Performing simultaneous readout on both qubits
4. Repeating the process multiple times to gather statistics

The outcome of this measurement will be used to:
1. Quantify the readout fidelity for two-qubit states
2. Identify and characterize crosstalk effects in the readout process
3. Provide data for readout error mitigation in two-qubit experiments

Prerequisites:
- Calibrated single-qubit gates for both qubits in the pair
- Calibrated readout for both qubits

Outcomes:
- 4x4 confusion matrix representing the probabilities of measuring each two-qubit state given a prepared input state
- Readout fidelity metrics for simultaneous two-qubit measurement
"""

# %% {Imports}
from qualibrate import QualibrationNode, NodeParameters
from quam_libs.components import QuAM
from quam_libs.macros import active_reset, readout_state, readout_state_gef, active_reset_gef
from quam_libs.lib.plot_utils import QubitPairGrid, grid_iter, grid_pair_names
from quam_libs.lib.save_utils import fetch_results_as_xarray, load_dataset
from qualang_tools.results import progress_counter, fetching_tool
from qualang_tools.loops import from_array
from qualang_tools.multi_user import qm_session
from qualang_tools.units import unit
from qm import SimulationConfig
from qm.qua import *
from typing import Literal, Optional, List
import matplotlib.pyplot as plt
import numpy as np
import warnings
from qualang_tools.bakery import baking
from quam_libs.lib.fit import extract_dominant_frequencies
from quam_libs.lib.plot_utils import QubitPairGrid, grid_iter, grid_pair_names
from scipy.optimize import curve_fit
from quam_libs.components.gates.two_qubit_gates import CZGate
from quam_libs.lib.pulses import FluxPulse
from scipy.fft import fft
import xarray as xr
from quam_libs.components.gates.two_qubit_gates import SWAP_Coupler_Gate

# %% {Node_parameters}
class Parameters(NodeParameters):

    qubit_pairs: Optional[List[str]] = ["q1-q2"]
    num_averages: int = 100
    flux_point_joint_or_independent_or_pairwise: Literal["joint", "independent", "pairwise"] = "pairwise"
    reset_type: Literal['active', 'thermal'] = "thermal"
    simulate: bool = False
    timeout: int = 100
    load_data_id: Optional[int] = None
    control_amp_range : float = 0.3
    control_amp_step : float = 0.02
    idle_time_min : int = 16
    idle_time_max : int = 200
    idle_time_step : int = 4
    use_state_discrimination: bool = True
    

node = QualibrationNode(
    name="64_coupler_interaction_strength_calibration", parameters=Parameters()
)
assert not (node.parameters.simulate and node.parameters.load_data_id is not None), "If simulate is True, load_data_id must be None, and vice versa."

# %% {Initialize_QuAM_and_QOP}
# Class containing tools to help handling units and conversions.
u = unit(coerce_to_integer=True)
# Instantiate the QuAM class from the state file
machine = QuAM.load()

# Get the relevant QuAM components
if node.parameters.qubit_pairs is None or node.parameters.qubit_pairs == "":
    qubit_pairs = machine.active_qubit_pairs
else:
    qubit_pairs = [machine.qubit_pairs[qp] for qp in node.parameters.qubit_pairs]
# if any([qp.q1.z is None or qp.q2.z is None for qp in qubit_pairs]):
#     warnings.warn("Found qubit pairs without a flux line. Skipping")

num_qubit_pairs = len(qubit_pairs)

# Generate the OPX and Octave configurations
config = machine.generate_config()
octave_config = machine.get_octave_config()
# Open Communication with the QOP
if node.parameters.load_data_id is None:
    qmm = machine.connect()
# %%

####################
# Helper functions #
####################


# %% {QUA_program}
n_avg = node.parameters.num_averages  # The number of averages

flux_point = node.parameters.flux_point_joint_or_independent_or_pairwise  # 'independent' or 'joint' or 'pairwise'
# Loop parameters
control_amps = np.arange(1 - node.parameters.control_amp_range, 1 + node.parameters.control_amp_range, node.parameters.control_amp_step)
idle_times = np.arange(node.parameters.idle_time_min, node.parameters.idle_time_max, node.parameters.idle_time_step) // 4

with program() as CPhase_Oscillations:
    n = declare(int)
    
    amp = declare(float)
    idle_time = declare(int)
    n_st = declare_stream()
    if node.parameters.use_state_discrimination:
        state_control = [declare(int) for _ in range(num_qubit_pairs)]
        state_target = [declare(int) for _ in range(num_qubit_pairs)]
        state = [declare(int) for _ in range(num_qubit_pairs)]
        state_st_control = [declare_stream() for _ in range(num_qubit_pairs)]
        state_st_target = [declare_stream() for _ in range(num_qubit_pairs)]
        state_st = [declare_stream() for _ in range(num_qubit_pairs)]
    else:
        I_control = [declare(float) for _ in range(num_qubit_pairs)]
        Q_control = [declare(float) for _ in range(num_qubit_pairs)]
        I_target = [declare(float) for _ in range(num_qubit_pairs)]
        Q_target = [declare(float) for _ in range(num_qubit_pairs)]
        I_st_control = [declare_stream() for _ in range(num_qubit_pairs)]
        Q_st_control = [declare_stream() for _ in range(num_qubit_pairs)]
        I_st_target = [declare_stream() for _ in range(num_qubit_pairs)]
        Q_st_target = [declare_stream() for _ in range(num_qubit_pairs)]
    
    
    for i, qp in enumerate(qubit_pairs):
        # Bring the active qubits to the minimum frequency point
        machine.set_all_fluxes(flux_point, qp)
        wait(1000)

        with for_(n, 0, n < n_avg, n + 1):
            save(n, n_st)         
            with for_(*from_array(amp, control_amps)):
                with for_(*from_array(idle_time, idle_times)):
                    # reset
                    if node.parameters.reset_type == "active":
                            active_reset(qp.qubit_control)
                            active_reset(qp.qubit_target)
                            qp.align()
                    else:
                        wait(qp.qubit_control.thermalization_time * u.ns)
                        wait(qp.qubit_target.thermalization_time * u.ns)
                    align()
                    
                    # setting both qubits ot the initial state
                    qp.qubit_control.xy.play("x180")
                    
                                    
                    align()
                    qp.qubit_control.z.play("const", amplitude_scale = amp * qp.gates["SWAP_Coupler"].flux_pulse_control.amplitude  / 0.1, duration = idle_time)
                    qp.coupler.play("const", amplitude_scale = qp.gates["SWAP_Coupler"].coupler_pulse_control.amplitude / 0.1, duration = idle_time)
                    align()
                    # readout
                    if node.parameters.use_state_discrimination:
                        readout_state(qp.qubit_control, state_control[i])
                        readout_state(qp.qubit_target, state_target[i])
                        assign(state[i], state_control[i]*2 + state_target[i])
                        save(state_control[i], state_st_control[i])
                        save(state_target[i], state_st_target[i])
                        save(state[i], state_st[i])
                    else:
                        qp.qubit_control.resonator.measure("readout", qua_vars=(I_control[i], Q_control[i]))
                        qp.qubit_target.resonator.measure("readout", qua_vars=(I_target[i], Q_target[i]))
                        save(I_control[i], I_st_control[i])
                        save(Q_control[i], Q_st_control[i])
                        save(I_target[i], I_st_target[i])
                        save(Q_target[i], Q_st_target[i])
        align()
        
    with stream_processing():
        n_st.save("n")
        for i in range(num_qubit_pairs):
            if node.parameters.use_state_discrimination:
                state_st_control[i].buffer(len(idle_times)).buffer(len(control_amps)).average().save(f"state_control{i + 1}")
                state_st_target[i].buffer(len(idle_times)).buffer(len(control_amps)).average().save(f"state_target{i + 1}")
                state_st[i].buffer(len(idle_times)).buffer(len(control_amps)).average().save(f"state{i + 1}")
            else:
                I_st_control[i].buffer(len(idle_times)).buffer(len(control_amps)).average().save(f"I_control{i + 1}")
                Q_st_control[i].buffer(len(idle_times)).buffer(len(control_amps)).average().save(f"Q_control{i + 1}")
                I_st_target[i].buffer(len(idle_times)).buffer(len(control_amps)).average().save(f"I_target{i + 1}")
                Q_st_target[i].buffer(len(idle_times)).buffer(len(control_amps)).average().save(f"Q_target{i + 1}")

# %% {Simulate_or_execute}
if node.parameters.simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=10_000)  # In clock cycles = 4ns
    job = qmm.simulate(config, CPhase_Oscillations, simulation_config)
    job.get_simulated_samples().con1.plot()
    node.results = {"figure": plt.gcf()}
    node.machine = machine
    node.save()
elif node.parameters.load_data_id is None:
    with qm_session(qmm, config, timeout=node.parameters.timeout) as qm:
        job = qm.execute(CPhase_Oscillations)

        results = fetching_tool(job, ["n"], mode="live")
        while results.is_processing():
            # Fetch results
            n = results.fetch_all()[0]
            # Progress bar
            progress_counter(n, n_avg, start_time=results.start_time)

# %% {Data_fetching_and_dataset_creation}
if not node.parameters.simulate:
    if node.parameters.load_data_id is None:
        # Fetch the data from the OPX and convert it into a xarray with corresponding axes (from most inner to outer loop)
        ds = fetch_results_as_xarray(job.result_handles, qubit_pairs, {  "idle_time": idle_times, "amp": control_amps})
    else:
        ds, machine = load_dataset(node.parameters.load_data_id)
        
    node.results = {"ds": ds}

# %%
if not node.parameters.simulate:
    ds = ds.assign_coords(idle_time = ds.idle_time * 4)
    ds = ds.assign({"res_sum" : ds.state_control - ds.state_target})
    # flux_coupler_full = np.array([fluxes_coupler + qp.coupler.decouple_offset for qp in qubit_pairs])
    # ds = ds.assign_coords({"flux_coupler_full": (["qubit", "flux_coupler"], flux_coupler_full)})    
    
    ds.state_control.plot()
    plt.show()
    ds.state_target.plot()
    plt.show()
# %%
if not node.parameters.simulate:
    # Add the dominant frequencies to the dataset
    ds['dominant_frequency'] = extract_dominant_frequencies(ds.res_sum)
    ds.dominant_frequency.attrs['units'] = 'GHz'


# %%
# Plot the dominant frequencies
# Find the values of flux_coupler_full for which the dominant frequencies are max and min
interaction_max = ds.dominant_frequency.max(dim='flux_coupler')
coupler_flux_pulse = ds.flux_coupler.isel(flux_coupler=ds.dominant_frequency.argmax(dim='flux_coupler'))
coupler_flux_min = ds.flux_coupler_full.isel(flux_coupler=ds.dominant_frequency.argmin(dim='flux_coupler'))

# %% {Plotting}
if not node.parameters.simulate:
    grid_names, qubit_pair_names = grid_pair_names(qubit_pairs)
    grid = QubitPairGrid(grid_names, qubit_pair_names)    
    for ax, qp in grid_iter(grid):
        if node.parameters.use_state_discrimination:
            ds.state_control.sel(qubit=qp['qubit']).plot(ax = ax, cmap = 'viridis', x = 'idle_time', y = 'flux_coupler_full')
        else:
            ds.I_control.sel(qubit=qp['qubit']).plot(ax = ax, cmap = 'viridis', x = 'idle_time', y = 'flux_coupler_full')
        ax.set_title(qp['qubit'])
    grid.fig.suptitle('I Control')
    plt.tight_layout()
    plt.show()
    node.results['figure_I_control'] = grid.fig
    
    grid = QubitPairGrid(grid_names, qubit_pair_names)    
    for ax, qp in grid_iter(grid):
        if node.parameters.use_state_discrimination:
            ds.state_target.sel(qubit=qp['qubit']).plot(ax = ax, cmap = 'viridis', x = 'idle_time', y = 'flux_coupler_full')
        else:
            ds.I_target.sel(qubit=qp['qubit']).plot(ax = ax, cmap = 'viridis', x = 'idle_time', y = 'flux_coupler_full')
        ax.set_title(qp['qubit'])
    grid.fig.suptitle('I Target')
    plt.tight_layout()
    plt.show()
    node.results['figure_I_target'] = grid.fig
    
    grid = QubitPairGrid(grid_names, qubit_pair_names)    
    for ax, qp in grid_iter(grid):
        (1e3*ds.dominant_frequency.sel(qubit=qp['qubit'])).plot(ax = ax, marker = '.', ls = 'None')
        ax.axvline(x = coupler_flux_pulse.sel(qubit=qp['qubit']), color = 'red', lw = 0.5, ls = '--')
        ax.set_title(qp['qubit'])
        ax.set_xlabel('Flux Coupler')
        ax.set_ylabel('Frequency (MHz)')
    grid.fig.suptitle('Dominant Frequency')
    plt.tight_layout()
    plt.show()
    node.results['figure_dominant_frequency'] = grid.fig
# %%
from importlib import reload
import quam_libs.components.gates.two_qubit_gates as two_qubit_gates
reload(two_qubit_gates)
from quam_libs.components.gates.two_qubit_gates import SWAP_Coupler_Gate

# If you need to use the reloaded SWAP_Coupler_Gate specifically:
SWAP_Coupler_Gate = two_qubit_gates.SWAP_Coupler_Gate


# %% {Update_state}
if not node.parameters.simulate:
    with node.record_state_updates():
        for qp in qubit_pairs:
            gate_time_ns = int(1/ (2 * interaction_max.sel(qubit = qp.name).values)) 
            
            gate_time_including_zeros = gate_time_ns - gate_time_ns % 4 + 4
            zero_padding = gate_time_including_zeros - gate_time_ns
            coupler_flux_pulse_amp = float(coupler_flux_pulse.sel(qubit = qp.name).values)
            qubit_flux_pulse_amp = qp.detuning
            
            qp.coupler.decouple_offset = float(coupler_flux_min.sel(qubit = qp.name).values)
            qp.gates['SWAP_Coupler'] = SWAP_Coupler_Gate(flux_pulse_control = FluxPulse(length = gate_time_including_zeros, amplitude = qubit_flux_pulse_amp, zero_padding = zero_padding, id = 'flux_pulse_control_' + qp.qubit_target.name), 
                                                         coupler_pulse_control = FluxPulse(length = gate_time_including_zeros, amplitude = coupler_flux_pulse_amp, zero_padding = zero_padding, id = 'coupler_pulse_control_' + qp.qubit_target.name))
# %% {Save_results}
if not node.parameters.simulate:    
    node.outcomes = {q.name: "successful" for q in qubit_pairs}
    node.results['initial_parameters'] = node.parameters.model_dump()
    node.machine = machine
    node.save()
# %%
