# %%
"""
RAMSEY WITH VIRTUAL Z ROTATIONS
The program consists in playing a Ramsey sequence (x90 - idle_time - x90 - measurement) for different idle times.
Instead of detuning the qubit gates, the frame of the second x90 pulse is rotated (de-phased) to mimic an accumulated
phase acquired for a given detuning after the idle time.
This method has the advantage of playing resonant gates.

From the results, one can fit the Ramsey oscillations and precisely measure the qubit resonance frequency and T2*.

Prerequisites:
    - Having found the resonance frequency of the resonator coupled to the qubit under study (resonator_spectroscopy).
    - Having calibrated qubit pi pulse (x180) by running qubit, spectroscopy, rabi_chevron, power_rabi and updated the state.
    - (optional) Having calibrated the readout (readout_frequency, amplitude, duration_optimization IQ_blobs) for better SNR.

Next steps before going to the next node:
    - Update the qubits frequency (f_01) in the state.
    - Save the current state by calling machine.save("quam")
"""
from qualibrate import QualibrationNode, NodeParameters
from typing import Optional, Literal, List

# %% {Node_parameters}
class Parameters(NodeParameters):
    qubit_pairs: Optional[List[str]] = ["q1-q2"]
    num_averages: int = 100
    frequency_detuning_in_mhz: float = 4.0
    min_wait_time_in_ns: int = 16
    max_wait_time_in_ns: int = 2000
    wait_time_step_in_ns: int = 4
    flux_span : float = 0.24
    flux_step : float = 0.002
    flux_point_joint_or_independent_or_pairwise: Literal['joint', 'independent', 'pairwise'] = "pairwise"
    simulate: bool = False
    timeout: int = 100
    flux_mode_dc_or_pulsed: Literal['dc', 'pulsed'] = 'pulsed'

node = QualibrationNode(
    name="62b_Ramsey_flux_pair_large_range",
    parameters=Parameters()
)

from qm.qua import *
from qm import SimulationConfig
from qualang_tools.results import progress_counter, fetching_tool
from qualang_tools.plot import interrupt_on_close
from qualang_tools.loops import from_array, get_equivalent_log_array
from qualang_tools.multi_user import qm_session
from qualang_tools.units import unit
from quam_libs.components import QuAM
from quam_libs.macros import qua_declaration, multiplexed_readout, node_save, active_reset, readout_state

import matplotlib.pyplot as plt
import numpy as np

import matplotlib
from quam_libs.lib.plot_utils import QubitGrid, grid_iter
from quam_libs.lib.save_utils import fetch_results_as_xarray
from quam_libs.lib.fit import fit_oscillation_decay_exp, oscillation_decay_exp
from quam_libs.lib.plot_utils import QubitPairGrid, grid_iter, grid_pair_names
from scipy.signal import find_peaks
from quam_libs.lib.fit import fit_oscillation, oscillation

# %% Helper functions

def filter_frequency_data(frequency, min_brill_size = 0.02):
    flux_data = frequency.flux.values
    freq_data = frequency.values    
    
    # find center of the first brillouin zone by fitting the data around zero to a prabola
    fitvals = frequency.sel(flux = slice(-min_brill_size,min_brill_size)).polyfit(dim = 'flux', deg = 2)
    center_flux = float((-0.5*fitvals.sel(degree = 1).polyfit_coefficients/fitvals.sel(degree = 2).polyfit_coefficients).values)

    # find the brillouin zones
    max_peaks, _ = find_peaks(freq_data)
    min_peaks, _ = find_peaks(-freq_data)
    all_peaks = np.sort(np.concatenate([max_peaks, min_peaks]))

    # Convert peak indices to flux values
    zone_boundaries = flux_data[all_peaks] 
    # Remove zone boundaries that are within min_brill_size of the center
    zone_boundaries = zone_boundaries[np.abs(zone_boundaries - center_flux) >= min_brill_size]
    # Index every point in zone_boundaries to indicate which zone begins there
    zone_indices = np.arange(-len(zone_boundaries[zone_boundaries < center_flux]),
                             len(zone_boundaries[zone_boundaries >= center_flux]) + 1)

    # Add 1 to all values which are zero or greater
    zone_indices[zone_indices >= 0] += 1
    
    # Create an array to store the zone for each flux point
    zones = np.zeros_like(frequency.flux.values, dtype=int)
    
    # Ensure zone_indices and zone_boundaries have the same length
    zone_indices = zone_indices[:len(zone_boundaries)]
    
    # Separate positive and negative flux boundaries
    neg_boundaries = zone_boundaries[zone_boundaries < 0]
    pos_boundaries = zone_boundaries[zone_boundaries >= 0]
    neg_indices = zone_indices[zone_boundaries < 0]
    pos_indices = zone_indices[zone_boundaries >= 0]
    
    # Iterate through the flux values and assign zones
    for i, flux_value in enumerate(frequency.flux.values):
        if flux_value < 0:
            # For negative flux
            if flux_value < neg_boundaries[0]:
                zones[i] = neg_indices[0] 
            else:
                for j in range(len(neg_boundaries)):
                    if j == len(neg_boundaries) - 1 or neg_boundaries[j] <= flux_value < neg_boundaries[j + 1]:
                        zones[i] = neg_indices[j] + 1
                        break
        else:
            # For positive flux
            if flux_value < pos_boundaries[0]:
                zones[i] = pos_indices[0] - 1
            else:
                for j in range(len(pos_boundaries)):
                    if j == len(pos_boundaries) - 1 or pos_boundaries[j] <= flux_value < pos_boundaries[j + 1]:
                        zones[i] = pos_indices[j]
                        break
    
    # Add the zone information to the frequency DataArray
    frequency = frequency.assign_coords(zone=("flux", np.abs(zones)))
    frequency_mod = frequency * (frequency.zone == 0) + (2*125 - frequency) * (frequency.zone == 1) + (2*125 + frequency) * (frequency.zone > 1)
    return frequency_mod

def fit_frequency_data(frequency):
    fitvals = fit_oscillation(frequency, dim = 'flux')
    fitted_freq = oscillation(frequency.flux, fitvals.sel(fit_vals = 'a'), fitvals.sel(fit_vals = 'f'), fitvals.sel(fit_vals = 'phi'), fitvals.sel(fit_vals = 'offset'))
    # Calculate the difference between fitted_freq and frequency_mod
    diff = np.abs(fitted_freq - frequency)
    # Calculate the standard deviation of the difference
    std_diff = np.std(diff)
    # Define a threshold for significant deviation (e.g., 2 standard deviations)
    threshold = 2 * std_diff
    # Find points that deviate significantly
    significant_deviations = diff > threshold
    
    # Create a new frequency data that excludes significant deviations
    frequency_filtered = frequency.where(~significant_deviations, drop=True)
    
    # Fit the filtered data
    fitvals_filtered = fit_oscillation(frequency_filtered, dim='flux')
    return fitvals_filtered


# %%



# Class containing tools to help handle units and conversions.
u = unit(coerce_to_integer=True)
# Instantiate the QuAM class from the state file
machine = QuAM.load()
# Generate the OPX and Octave configurations
config = machine.generate_config()
octave_config = machine.get_octave_config()
# Open Communication with the QOP
qmm = machine.connect()

# Get the relevant QuAM components
if node.parameters.qubit_pairs is None or node.parameters.qubit_pairs == '':
    qubit_pairs = machine.active_qubit_pairs
else:
    qubit_pairs = [machine.qubit_pairs[qp] for qp in node.parameters.qubit_pairs]
num_qubits = len(qubit_pairs)

# %%

# %% {QUA_program}
n_avg = node.parameters.num_averages  # The number of averages

# Dephasing time sweep (in clock cycles = 4ns) - minimum is 4 clock cycles
idle_times = np.arange(
    node.parameters.min_wait_time_in_ns // 4,
    node.parameters.max_wait_time_in_ns // 4,
    node.parameters.wait_time_step_in_ns // 4,
)

# Detuning converted into virtual Z-rotations to observe Ramsey oscillation and get the qubit frequency
detuning = int(1e6 * node.parameters.frequency_detuning_in_mhz)
flux_point = node.parameters.flux_point_joint_or_independent_or_pairwise  # 'independent' or 'joint' or 'pairwise'
fluxes = np.arange(-node.parameters.flux_span / 2, node.parameters.flux_span / 2+0.001, step = node.parameters.flux_step)

# %%
with program() as ramsey:
    I, I_st, Q, Q_st, n, n_st = qua_declaration(num_qubits=num_qubits)
    init_state = declare(int)
    state_control = [declare(int) for _ in range(num_qubits)]
    state_target = [declare(int) for _ in range(num_qubits)]
    state_control_st = [declare_stream() for _ in range(num_qubits)]
    state_target_st = [declare_stream() for _ in range(num_qubits)]
    t = declare(int)  # QUA variable for the idle time
    phi = declare(fixed)  # QUA variable for dephasing the second pi/2 pulse (virtual Z-rotation)
    flux = declare(fixed)  # QUA variable for the flux dc level

    for i, qp in enumerate(qubit_pairs):
        qubit = qp.qubit_control
        state = state_control
        state_st = state_control_st
        mutual_flux_point = machine.set_all_fluxes(flux_point, qp)
        wait(1000)        
        align()

        with for_(n, 0, n < n_avg, n + 1):
            save(n, n_st)
            with for_(*from_array(flux, fluxes)):
                with for_(*from_array(t, idle_times)):
                    readout_state(qubit, init_state, pulse_name = "readout_QND")
                    # Rotate the frame of the second x90 gate to implement a virtual Z-rotation
                    # 4*tau because tau was in clock cycles and 1e-9 because tau is ns
                    assign(phi, Cast.mul_fixed_by_int(detuning * 1e-9, 4 * t ))
                    qubit.align()
                    # Strict_timing ensures that the sequence will be played without gaps
                    # with strict_timing_():
                    qubit.xy.play("x180", amplitude_scale = 0.5)
                    qubit.align()
                    wait(20, qubit.z.name)
                    qubit.z.play("const", amplitude_scale = flux / qubit.z.operations["const"].amplitude, duration=t)
                    wait(20, qubit.z.name)
                    qubit.xy.frame_rotation_2pi(phi)
                    qubit.align()
                    qubit.xy.play("x180", amplitude_scale = 0.5)

                    # Align the elements to measure after playing the qubit pulse.
                    align()
                    # Measure the state of the resonators
                    readout_state(qubit, state[i])
                    assign(state[i], init_state ^ state[i])
                    save(state[i], state_st[i])
                    
                    # Reset the frame of the qubits in order not to accumulate rotations
                    reset_frame(qubit.xy.name)
                    qubit.align()
        qp.align()

        qubit = qp.qubit_target
        state = state_target
        state_st = state_target_st
        mutual_flux_point = machine.set_all_fluxes(flux_point, qp)
        wait(1000)        
        align()

        with for_(n, 0, n < n_avg, n + 1):
            save(n, n_st)
            with for_(*from_array(flux, fluxes)):
                with for_(*from_array(t, idle_times)):
                    readout_state(qubit, init_state)
                    # Rotate the frame of the second x90 gate to implement a virtual Z-rotation
                    # 4*tau because tau was in clock cycles and 1e-9 because tau is ns
                    assign(phi, Cast.mul_fixed_by_int(detuning * 1e-9, 4 * t ))
                    qubit.align()
                    # Strict_timing ensures that the sequence will be played without gaps
                    # with strict_timing_():
                    qubit.xy.play("x180", amplitude_scale = 0.5)
                    qubit.align()
                    wait(20, qubit.z.name)
                    qubit.z.play("const", amplitude_scale = flux / qubit.z.operations["const"].amplitude, duration=t)
                    wait(20, qubit.z.name)
                    qubit.xy.frame_rotation_2pi(phi)
                    qubit.align()
                    qubit.xy.play("x180", amplitude_scale = 0.5)

                    # Align the elements to measure after playing the qubit pulse.
                    align()
                    # Measure the state of the resonators
                    readout_state(qubit, state[i])
                    assign(state[i], init_state ^ state[i])
                    save(state[i], state_st[i])
                    
                    # Reset the frame of the qubits in order not to accumulate rotations
                    reset_frame(qubit.xy.name)
                    qubit.align()
        
        align()

    with stream_processing():
        n_st.save("n")
        for i in range(num_qubits):
            state_control_st[i].buffer(len(idle_times)).buffer(len(fluxes)).average().save(f"state_control{i + 1}")
            state_target_st[i].buffer(len(idle_times)).buffer(len(fluxes)).average().save(f"state_target{i + 1}")



# %% {Simulate_or_execute}
if node.parameters.simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=10_000)  # In clock cycles = 4ns
    job = qmm.simulate(config, ramsey, simulation_config)
    job.get_simulated_samples().con1.plot()
    node.results = {"figure": plt.gcf()}
    node.machine = machine
    node.save()

else:
    with qm_session(qmm, config, timeout=node.parameters.timeout) as qm:
        job = qm.execute(ramsey)
        # Get results from QUA program
        for i in range(num_qubits):
            print(f"Fetching results for qubit {qubit_pairs[i].name}")
            data_list = ["n"] + sum([[f"state_control{i + 1}"] for i in range(num_qubits)], []) + sum([[f"state_target{i + 1}"] for i in range(num_qubits)], [])
            results = fetching_tool(job, data_list, mode="live")
        # Live plotting
        # fig, axes = plt.subplots(2, num_qubits, figsize=(4 * num_qubits, 8))
        # interrupt_on_close(fig, job)  # Interrupts the job when closing the figure
            while results.is_processing():
            # Fetch results
                fetched_data = results.fetch_all()
                n = fetched_data[0]

                progress_counter(n, n_avg, start_time=results.start_time)

# %%
if not node.parameters.simulate:
    ds = fetch_results_as_xarray(job.result_handles, qubit_pairs, {"idle_time": idle_times, "flux": fluxes})

    node.results = {"ds": ds}
    
    ds_control = ds
    ds_control = ds_control.assign({"state" : ds_control.state_control})
    ds_target = ds
    ds_target = ds_target.assign({"state" : ds_target.state_target})
        
    
# %%
if not node.parameters.simulate:
    ds_control = ds_control.assign_coords(idle_time=4*ds.idle_time/1e3)  # convert to usec
    ds_control.flux.attrs = {'long_name': 'flux', 'units': 'V'}
    ds_control.idle_time.attrs = {'long_name': 'idle time', 'units': 'usec'}
    ds_target.flux.attrs = {'long_name': 'flux', 'units': 'V'}
    ds_target.idle_time.attrs = {'long_name': 'idle time', 'units': 'usec'}
    fit_data_control = fit_oscillation_decay_exp(ds_control.state, 'idle_time')
    fit_data_control.attrs = {'long_name' : 'time', 'units' : 'usec'}
    fitted_control =  oscillation_decay_exp(ds_control.state.idle_time,
                                                    fit_data_control.sel(
                                                        fit_vals="a"),
                                                    fit_data_control.sel(
                                                        fit_vals="f"),
                                                    fit_data_control.sel(
                                                        fit_vals="phi"),
                                                    fit_data_control.sel(
                                                        fit_vals="offset"),
                                                    fit_data_control.sel(fit_vals="decay"))
    frequency_control = fit_data_control.sel(fit_vals = 'f')
    frequency_control.attrs = {'long_name' : 'frequency', 'units' : 'MHz'}
    decay_control = fit_data_control.sel(fit_vals = 'decay')
    decay_control.attrs = {'long_name' : 'decay', 'units' : 'nSec'}
    tau_control = 1/fit_data_control.sel(fit_vals='decay')
    tau_control.attrs = {'long_name' : 'T2*', 'units' : 'uSec'}
    frequency_control = frequency_control.where(frequency_control>0,drop = True)
    


    ds_target = ds_target.assign_coords(idle_time=4*ds.idle_time/1e3)  # convert to usec
    ds_target.flux.attrs = {'long_name': 'flux', 'units': 'V'}
    ds_target.idle_time.attrs = {'long_name': 'idle time', 'units': 'usec'}

    fit_data_target = fit_oscillation_decay_exp(ds_target.state, 'idle_time')
    fit_data_target.attrs = {'long_name' : 'time', 'units' : 'usec'}
    fitted_target =  oscillation_decay_exp(ds_target.state.idle_time,
                                                    fit_data_target.sel(
                                                        fit_vals="a"),
                                                    fit_data_target.sel(
                                                        fit_vals="f"),
                                                    fit_data_target.sel(
                                                        fit_vals="phi"),
                                                    fit_data_target.sel(
                                                        fit_vals="offset"),
                                                    fit_data_target.sel(fit_vals="decay"))
    frequency_target = fit_data_target.sel(fit_vals = 'f')
    frequency_target.attrs = {'long_name' : 'frequency', 'units' : 'MHz'}
    decay_target = fit_data_target.sel(fit_vals = 'decay')
    decay_target.attrs = {'long_name' : 'decay', 'units' : 'nSec'}
    tau_target = 1/fit_data_target.sel(fit_vals='decay')
    tau_target.attrs = {'long_name' : 'T2*', 'units' : 'uSec'}
    frequency_target = frequency_target.where(frequency_target>0,drop = True)
# %%
if not node.parameters.simulate:
    a_control = {}
    f_control = {}
    phi_control = {}
    offset_control = {}
    a_target = {}
    f_target = {}
    phi_target = {}
    offset_target = {}
    frequency_control_mod_dict = {}
    frequency_target_mod_dict = {}
    fitted_freq_control = {}
    fitted_freq_target = {}
    
    for qp in qubit_pairs:
        
        frequency_control_mod = filter_frequency_data(frequency_control.sel(qubit =qp.name))
        fitvals_control = fit_frequency_data(frequency_control_mod)
        fitted_freq_control = oscillation(frequency_control_mod.flux, 
                                        fitvals_control.sel(fit_vals='a'), 
                                        fitvals_control.sel(fit_vals='f'), 
                                        fitvals_control.sel(fit_vals='phi'), 
                                        fitvals_control.sel(fit_vals='offset'))    
        frequency_control_mod_dict[qp.name] = frequency_control_mod
        fitted_freq_control[qp.name] = fitted_freq_control
        
        a_control[qp.name] = float(fitvals_control.sel(fit_vals='a').values)
        f_control[qp.name] = float(fitvals_control.sel(fit_vals='f').values)
        phi_control[qp.name] = float(fitvals_control.sel(fit_vals='phi').values)
        offset_control[qp.name] = float(fitvals_control.sel(fit_vals='offset').values)

        frequency_target_mod = filter_frequency_data(frequency_target.sel(qubit = qp.name))
        fitvals_target = fit_frequency_data(frequency_target_mod)
        fitted_freq_target = oscillation(frequency_target_mod.flux, 
                                        fitvals_target.sel(fit_vals='a'), 
                                        fitvals_target.sel(fit_vals='f'), 
                                        fitvals_target.sel(fit_vals='phi'), 
                                        fitvals_target.sel(fit_vals='offset'))    
        frequency_target_mod_dict[qp.name] = frequency_target_mod
        fitted_freq_target[qp.name] = fitted_freq_target

        a_target[qp.name] = float(fitvals_target.sel(fit_vals='a').values)
        f_target[qp.name] = float(fitvals_target.sel(fit_vals='f').values)
        phi_target[qp.name] = float(fitvals_target.sel(fit_vals='phi').values)
        offset_target[qp.name] = float(fitvals_target.sel(fit_vals='offset').values)


# %%
if not node.parameters.simulate:
    grid_names, qubit_pair_names = grid_pair_names(qubit_pairs)
    grid = QubitPairGrid(grid_names, qubit_pair_names)
    for ax, qubit in grid_iter(grid):
        ds_control.sel(qubit = qubit['qubit']).state.plot(ax = ax)
        ax.set_title(qubit['qubit'])
        ax.set_xlabel('Idle_time (uS)')
        ax.set_ylabel(' Flux (V)')
    grid.fig.suptitle('Ramsey freq. Vs. flux control')
    plt.tight_layout()
    plt.show()
    node.results['figure_raw_control'] = grid.fig
    
    grid = QubitPairGrid(grid_names, qubit_pair_names)
    for ax, qubit in grid_iter(grid):
        ds_target.sel(qubit = qubit['qubit']).state.plot(ax = ax)
        ax.set_title(qubit['qubit'])
        ax.set_xlabel('Idle_time (uS)')
        ax.set_ylabel(' Flux (V)')
    grid.fig.suptitle('Ramsey freq. Vs. flux target')
    plt.tight_layout()
    plt.show()
    node.results['figure_raw_target'] = grid.fig

    grid = QubitPairGrid(grid_names, qubit_pair_names)
    for ax, qubit in grid_iter(grid):
        frequency_control_mod_dict[qubit['qubit']].plot( marker = '.',linewidth = 0,ax=ax)
        fitted_freq_control[qubit['qubit']].plot(ax=ax)
        ax.set_title(qubit['qubit'])
        ax.set_xlabel(' Flux (V)')
    grid.fig.suptitle('Ramsey freq. Vs. flux control')
    plt.tight_layout()
    plt.show()
    node.results['figure_fitted_control'] = grid.fig
    
    grid = QubitPairGrid(grid_names, qubit_pair_names)
    for ax, qubit in grid_iter(grid):
        frequency_target_mod_dict[qubit['qubit']].plot( marker = '.',linewidth = 0,ax=ax)
        fitted_freq_target[qubit['qubit']].plot(ax=ax)
        ax.set_title(qubit['qubit'])
        ax.set_xlabel(' Flux (V)')
    grid.fig.suptitle('Ramsey freq. Vs. flux target')
    plt.tight_layout()
    plt.show()
    node.results['figure_fitted_target'] = grid.fig

# %%
    
# %% {Update_state}
if not node.parameters.simulate:
    with node.record_state_updates():
        for qp in qubit_pairs:
            qp.qubit_control.extras['a'] = a_control[qp.name]
            qp.qubit_control.extras['f'] = f_control[qp.name]
            qp.qubit_control.extras['phi'] = phi_control[qp.name]
            qp.qubit_control.extras['offset'] = offset_control[qp.name]
            qp.qubit_target.extras['a'] = a_target[qp.name]
            qp.qubit_target.extras['f'] = f_target[qp.name]
            qp.qubit_target.extras['phi'] = phi_target[qp.name]
            qp.qubit_target.extras['offset'] = offset_target[qp.name]
            
# %% {Save_results}
if not node.parameters.simulate:    
    node.outcomes = {q.name: "successful" for q in qubit_pairs}
    node.results['initial_parameters'] = node.parameters.model_dump()
    node.machine = machine
    node.save()
# %%


# %%
