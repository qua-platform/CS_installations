# %%
"""
       PAIRWISE RESONATOR SPECTROSCOPY VERSUS FLUX 
This sequence involves measuring the resonator by sending a readout pulse and demodulating the signals to
extract the 'I' and 'Q' quadratures. This is done across various readout intermediate dfs and flux biases.
The resonator frequency as a function of flux bias is then extracted and fitted so that the parameters can be stored in the configuration.

This information can then be used to adjust the readout frequency for the maximum and minimum frequency points.

Prerequisites:
    - Calibration of the time of flight, offsets, and gains (referenced as "time_of_flight").
    - Calibration of the IQ mixer connected to the readout line (be it an external mixer or an Octave port).
    - Identification of the resonator's resonance frequency (referred to as "resonator_spectroscopy").
    - Configuration of the readout pulse amplitude and duration.
    - Specification of the expected resonator depletion time in the state.

Before proceeding to the next node:
    - Adjust the flux bias to the minimum frequency point, labeled as "max_frequency_point", in the state.
    - Adjust the flux bias to the minimum frequency point, labeled as "min_frequency_point", in the state.
    - Save the current state by calling machine.save("quam")
"""

# %% {Imports}
from qualibrate import QualibrationNode, NodeParameters
from quam_libs.components import QuAM
from quam_libs.macros import active_reset, readout_state
from quam_libs.lib.plot_utils import QubitPairGrid, grid_iter, grid_pair_names
from quam_libs.lib.save_utils import fetch_results_as_xarray, load_dataset
from quam_libs.lib.fit import fit_oscillation
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


# %% {Node_parameters}
class Parameters(NodeParameters):

    qubit_pairs: Optional[List[str]] = None
    num_averages: int = 10
    max_time_in_ns: int = 160
    flux_point_joint_or_independent: Literal["joint", "independent"] = "joint"
    reset_type: Literal['active', 'thermal'] = "thermal"
    simulate: bool = False
    timeout: int = 100
    method: Literal['coarse', 'fine'] = "coarse"
    amp_range_coarse : float = 0.3
    amp_step_coarse : float = 0.1
    amp_range_fine : float = 0.04
    amp_step_fine : float = 0.002
    load_data_id: Optional[int] = None  

node = QualibrationNode(
    name="30_02_11_oscillations", parameters=Parameters()
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
qmm = machine.connect()
# %%

####################
# Helper functions #
####################

def baked_waveform(waveform_amp, qubit):
    pulse_segments = []  # Stores the baking objects
    # Create the different baked sequences, each one corresponding to a different truncated duration
    waveform = [waveform_amp] * 16

    for i in range(1, 17):  # from first item up to pulse_duration (16)
        with baking(config, padding_method="left") as b:
            wf = waveform[:i]
            b.add_op("flux_pulse", qubit.z.name, wf)
            b.play("flux_pulse", qubit.z.name)
        # Append the baking object in the list to call it from the QUA program
        pulse_segments.append(b)
        
    return pulse_segments

# %% {QUA_program}
n_avg = node.parameters.num_averages  # The number of averages

flux_point = node.parameters.flux_point_joint_or_independent  # 'independent' or 'joint'

# define the amplitudes for the flux pulses
pulse_amplitudes = {}
if node.parameters.method == "coarse":
    for qp in qubit_pairs:
        detuning = qp.qubit_control.xy.RF_frequency - qp.qubit_target.xy.RF_frequency - qp.qubit_target.anharmonicity
        pulse_amplitudes[qp.name] = float(np.sqrt(-detuning/qp.qubit_control.freq_vs_flux_01_quad_term))
else:
    for qp in qubit_pairs:
        pulse_amplitudes[qp.name] = qp.gates["Cz"].amp

baked_signals = {qp.name : baked_waveform(pulse_amplitudes[qp.name], qp.qubit_control) for qp in qubit_pairs}

# Loop parameters
if node.parameters.method == "coarse":
    amplitudes = np.arange(1-node.parameters.amp_range_coarse, 1+node.parameters.amp_range_coarse, node.parameters.amp_step_coarse)
else:
    amplitudes = np.arange(1-node.parameters.amp_range_fine, node.parameters.amp_range_fine, node.parameters.amp_step_fine)
times_ns = np.arange(1, node.parameters.max_time_in_ns)

with program() as CPhase_Oscillations:
    t = declare(int)  # QUA variable for the flux pulse segment index
    idx = declare(int)
    amp = declare(fixed)    
    n = declare(int)
    n_st = declare_stream()
    state_control = [declare(int) for _ in range(num_qubit_pairs)]
    state_target = [declare(int) for _ in range(num_qubit_pairs)]
    state_st_control = [declare_stream() for _ in range(num_qubit_pairs)]
    state_st_target = [declare_stream() for _ in range(num_qubit_pairs)]
    
    for i, qp in enumerate(qubit_pairs):
        # Bring the active qubits to the minimum frequency point
        if flux_point == "independent":
            machine.apply_all_flux_to_min()
            # qp.apply_mutual_flux_point()
        elif flux_point == "joint":
            machine.apply_all_flux_to_joint_idle()
        else:
            machine.apply_all_flux_to_zero()
        wait(1000)

        with for_(n, 0, n < n_avg, n + 1):
            save(n, n_st)
            
            with for_(*from_array(amp, amplitudes)):
                # first 16 nS                
                with for_(idx, 0, idx<16, idx+1):
                    # reset                    
                    if node.parameters.reset_type == "active":
                        for qubit in [qp.qubit_control, qp.qubit_target]:
                            # TODO: use GEF reset
                            active_reset(machine, qubit.name)
                            qubit.align()
                    else:
                        wait(qubit.thermalization_time * u.ns)
                    # set both qubits to the excited state
                    for state,qubit in zip([state_control, state_target], [qp.qubit_control, qp.qubit_target]):
                        qubit.xy.play("x180")
                        qubit.xy.wait(5)
                        qubit.align()

                    # play the flux pulse
                    with switch_(idx):
                        for j in range(16):
                            with case_(j):
                                baked_signals[qp.name][j].run(amp_array = [(qp.qubit_control.z, amp)]) 
                                                                               
                    # wait for the flux pulse to end and some extra time
                    for qubit in [qp.qubit_control, qp.qubit_target]:
                        qubit.xy.wait(node.parameters.max_time_in_ns // 4 + 10)
                        qubit.align()
                    
                    # measure both qubits
                    for qubit, state, state_st in zip([qp.qubit_control, qp.qubit_target], [state_control, state_target], [state_st_control, state_st_target]):
                        readout_state(qubit, state[i]) # TODO: readout gef
                        # save data
                        save(state[i], state_st[i])   
                                                                                              
                # rest of the pulse
                with for_(t, 4, t < node.parameters.max_time_in_ns // 4, t + 4):
                    with for_(idx, 0, idx<16, idx+1):
                        # reset                    
                        if node.parameters.reset_type == "active":
                            for qubit in [qp.qubit_control, qp.qubit_target]:
                                # TODO: use GEF reset
                                active_reset(machine, qubit.name)
                                qubit.align()
                        else:
                            wait(qubit.thermalization_time * u.ns)
                        # set both qubits to the excited state
                        for state,qubit in zip([state_control, state_target], [qp.qubit_control, qp.qubit_target]):
                            qubit.xy.play("x180")
                            qubit.xy.wait(5)
                            qubit.align()

                        # play the flux pulse
                        with switch_(idx):
                            for j in range(16):
                                with case_(j):
                                    baked_signals[qp.name][j].run(amp_array = [(qp.qubit_control.z, amp)]) 
                        qp.qubit_control.z.play('const', duration=t, amplitude_scale = pulse_amplitudes[qp.name] / qp.qubit_control.z.operations['const'].amplitude * amp)
                        
                        # wait for the flux pulse to end and some extra time
                        for qubit in [qp.qubit_control, qp.qubit_target]:
                            qubit.xy.wait(node.parameters.max_time_in_ns // 4 + 10)
                            qubit.align()          
                                   
                        # measure both qubits
                        for qubit, state, state_st in zip([qp.qubit_control, qp.qubit_target], [state_control, state_target], [state_st_control, state_st_target]):
                            readout_state(qubit, state[i]) # TODO: readout gef
                            # save data
                            save(state[i], state_st[i])   
        align()
        
    with stream_processing():
        n_st.save("n")
        for i in range(num_qubit_pairs):
            state_st_control[i].buffer(len(amplitudes)).buffer(len(times_ns)).average().save(f"state_control{i + 1}")
            state_st_target[i].buffer(len(amplitudes)).buffer(len(times_ns)).average().save(f"state_target{i + 1}")

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
        ds = fetch_results_as_xarray(job.result_handles, qubit_pairs, {"amp": amplitudes, "time": times_ns})
    else:
        ds = load_dataset(node.parameters.load_data_id)
    node.results = {"ds": ds}

# %% {Data_analysis}
if not node.parameters.simulate:
    # Find the minimum of each frequency line to follow the resonance vs flux
    peak_freq1  = ds.IQ_abs1.idxmin(dim="freq")
    peak_freq2  = ds.IQ_abs2.idxmin(dim="freq")
    # Fit to a cosine using the qiskit function: a * np.cos(2 * np.pi * f * t + phi) + offset
    fit_osc1 = fit_oscillation(peak_freq1.dropna(dim="flux"), "flux")
    fit_osc2 = fit_oscillation(peak_freq2.dropna(dim="flux"), "flux")
    # Ensure that the phase is between -pi and pi
    idle_offset1 = -fit_osc1.sel(fit_vals="phi")
    idle_offset1 = np.mod(idle_offset1 + np.pi, 2 * np.pi) - np.pi
    idle_offset2 = -fit_osc2.sel(fit_vals="phi")
    idle_offset2 = np.mod(idle_offset2 + np.pi, 2 * np.pi) - np.pi
    # converting the phase phi from radians to voltage
    idle_offset1 = idle_offset1 / fit_osc1.sel(fit_vals="f") / 2 / np.pi
    idle_offset2 = idle_offset2 / fit_osc2.sel(fit_vals="f") / 2 / np.pi

    
    
    # Save fitting results
    fit_results = {}
    for qp in qubit_pairs:
        fit_results[qp.name] = {}
        fit_results[qp.name]["mutual_flux_point"] = [
            float(idle_offset1.sel(qubit=qp.id).values),
            float(idle_offset2.sel(qubit=qp.id).values),
        ]
        

    node.results["fit_results"] = fit_results

    # %% {Plotting}
    # Reload the plot_utils module to ensure we have the latest version
    import importlib
    import quam_libs.lib.plot_utils
    importlib.reload(quam_libs.lib.plot_utils)
    from quam_libs.lib.plot_utils import QubitPairGrid, grid_iter, grid_pair_names
    
    grid_names, qubit_pair_names = grid_pair_names(qubit_pairs)
    grid = QubitPairGrid(grid_names, qubit_pair_names)
    for ax, qubit in grid_iter(grid):
        ds.assign_coords(freq_MHz=ds.freq / 1e6).loc[qubit].IQ_abs1.plot(
            ax=ax, add_colorbar=False, x="flux", y="freq_MHz", robust=True
        )
        ax.axvline(idle_offset1.loc[qubit], linestyle="dashed", linewidth=2, color="r")
        # Location of the current resonator frequency
        ax.set_title(qubit["qubit"])
        ax.set_xlabel("Flux (V)")

    grid.fig.suptitle("Resonator spectroscopy vs flux for control")
    plt.tight_layout()
    plt.show()
    node.results["figure_control"] = grid.fig

    grid_names, qubit_pair_names = grid_pair_names(qubit_pairs)
    grid = QubitPairGrid(grid_names, qubit_pair_names)
    for ax, qubit in grid_iter(grid):
        ds.assign_coords(freq_MHz=ds.freq / 1e6).loc[qubit].IQ_abs2.plot(
            ax=ax, add_colorbar=False, x="flux", y="freq_MHz", robust=True
        )        
        ax.axvline(idle_offset2.loc[qubit], linestyle="dashed", linewidth=2, color="r")
        # Location of the current resonator frequency
        ax.set_title(qubit["qubit"])
        ax.set_xlabel("Flux (V)")

    grid.fig.suptitle("Resonator spectroscopy vs flux for target")
    plt.tight_layout()
    plt.show()
    node.results["figure_target"] = grid.fig
    # %% {Update_state}
    with node.record_state_updates():
        for qp in qubit_pairs:
            qp.mutual_flux_point = fit_results[qp.name]["mutual_flux_point"]

    # %% {Save_results}
    # node.outcomes = {q.name: "successful" for q in qubits}
    node.results["initial_parameters"] = node.parameters.model_dump()
    node.machine = machine
    node.save()

# %%
