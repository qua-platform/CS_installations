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
from quam_libs.macros import qua_declaration
from quam_libs.lib.plot_utils import QubitGrid, grid_iter
from quam_libs.lib.save_utils import fetch_results_as_xarray
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
from quam_libs.lib.plot_utils import QubitPairGrid, grid_iter, grid_pair_names


# %% {Node_parameters}
class Parameters(NodeParameters):

    qubit_pairs: Optional[List[str]] = None
    num_averages: int = 20
    min_flux_offset_in_v: float = -0.15
    max_flux_offset_in_v: float = 0.15
    num_flux_points: int = 81
    frequency_span_in_mhz: float = 10
    frequency_step_in_mhz: float = 0.05
    flux_point_joint_or_independent_or_pairwise: Literal["joint", "independent", "pairwise"] = "pairwise"
    simulate: bool = False
    timeout: int = 100
    input_line_impedance_in_ohm: float = 50
    line_attenuation_in_db: float = 0
    plot_current_mA: bool = True


node = QualibrationNode(
    name="60_pairwise_resonator_spectroscopy_vs_flux", parameters=Parameters()
)

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


# %% {QUA_program}
n_avg = node.parameters.num_averages  # The number of averages
# Flux bias sweep in V
dcs = np.linspace(
    node.parameters.min_flux_offset_in_v,
    node.parameters.max_flux_offset_in_v,
    node.parameters.num_flux_points,
)
# The frequency sweep around the resonator resonance frequency 
span = node.parameters.frequency_span_in_mhz * u.MHz
step = node.parameters.frequency_step_in_mhz * u.MHz
dfs = np.arange(-span / 2, +span / 2, step)

flux_point = node.parameters.flux_point_joint_or_independent_or_pairwise  # 'independent' or 'joint' or 'pairwise'

with program() as multi_res_spec_vs_flux:
    # Declare 'I' and 'Q' and the corresponding streams for the two resonators.
    # For instance, here 'I' is a python list containing two QUA fixed variables.
    I1, I1_st, Q1, Q1_st, n, n_st = qua_declaration(num_qubits=num_qubit_pairs)
    I2, I2_st, Q2, Q2_st, _, _ = qua_declaration(num_qubits=num_qubit_pairs)
    dc = declare(fixed)  # QUA variable for the flux bias
    df = declare(int)  # QUA variable for the readout frequency

    for i, qp in enumerate(qubit_pairs):

        qubit = qp.qubit_control
        machine.set_all_fluxes(flux_point, qp)
        wait(1000)

        with for_(n, 0, n < n_avg, n + 1):
            save(n, n_st)
            with for_(*from_array(dc, dcs)):
                # Flux sweeping by tuning the OPX dc offset associated with the flux_line element
                qubit.z.set_dc_offset(dc)
                wait(100)  # Wait for the flux to settle
                with for_(*from_array(df, dfs)):
                    # Update the resonator frequencies for resonator
                    update_frequency(qubit.resonator.name, df + qubit.resonator.intermediate_frequency)
                    # readout the resonator
                    qubit.resonator.measure("readout", qua_vars=(I1[i], Q1[i]))
                    # wait for the resonator to relax
                    qubit.resonator.wait(machine.depletion_time * u.ns)
                    # save data
                    save(I1[i], I1_st[i])
                    save(Q1[i], Q1_st[i])
        # Measure sequentially
        align()
        
        qubit = qp.qubit_target
        machine.set_all_fluxes(flux_point, qp)
        wait(1000)

        with for_(n, 0, n < n_avg, n + 1):
            save(n, n_st)
            with for_(*from_array(dc, dcs)):
                # Flux sweeping by tuning the OPX dc offset associated with the flux_line element
                qubit.z.set_dc_offset(dc)
                wait(100)  # Wait for the flux to settle
                with for_(*from_array(df, dfs)):
                    # Update the resonator frequencies for resonator
                    update_frequency(qubit.resonator.name, df + qubit.resonator.intermediate_frequency)
                    # readout the resonator
                    qubit.resonator.measure("readout", qua_vars=(I2[i], Q2[i]))
                    # wait for the resonator to relax
                    qubit.resonator.wait(machine.depletion_time * u.ns)
                    # save data
                    save(I2[i], I2_st[i])
                    save(Q2[i], Q2_st[i])
        # Measure sequentially
        align()


    with stream_processing():
        n_st.save("n")
        for i in range(num_qubit_pairs):
            I1_st[i].buffer(len(dfs)).buffer(len(dcs)).average().save(f"Icontrol{i + 1}")
            Q1_st[i].buffer(len(dfs)).buffer(len(dcs)).average().save(f"Qcontrol{i + 1}")
            I2_st[i].buffer(len(dfs)).buffer(len(dcs)).average().save(f"Itarget{i + 1}")
            Q2_st[i].buffer(len(dfs)).buffer(len(dcs)).average().save(f"Qtarget{i + 1}")


# %% {Simulate_or_execute}
if node.parameters.simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=10_000)  # In clock cycles = 4ns
    job = qmm.simulate(config, multi_res_spec_vs_flux, simulation_config)
    job.get_simulated_samples().con1.plot()
    node.results = {"figure": plt.gcf()}
    node.machine = machine
    node.save()
else:
    with qm_session(qmm, config, timeout=node.parameters.timeout) as qm:
        job = qm.execute(multi_res_spec_vs_flux)
        results = fetching_tool(job, ["n"], mode="live")
        while results.is_processing():
            # Fetch results
            n = results.fetch_all()[0]
            # Progress bar
            progress_counter(n, n_avg, start_time=results.start_time)

# %% {Data_fetching_and_dataset_creation}
if not node.parameters.simulate:
    # Fetch the data from the OPX and convert it into a xarray with corresponding axes (from most inner to outer loop)
    ds = fetch_results_as_xarray(job.result_handles, qubit_pairs, {"freq": dfs, "flux": dcs})
    # Derive the amplitude IQ_abs = sqrt(I**2 + Q**2)
    ds_control = ds[["Icontrol", "Qcontrol"]]
    ds_target = ds[["Itarget", "Qtarget"]]

    ds_control = ds_control.assign({"IQ_abs": np.sqrt(ds_control["Icontrol"] ** 2 + ds_control["Qcontrol"] ** 2)})
    ds_target = ds_target.assign({"IQ_abs": np.sqrt(ds_target["Itarget"] ** 2 + ds_target["Qtarget"] ** 2)})

 
 # %%
if not node.parameters.simulate:   
    # Add the resonator RF frequency axis of each qubit to the dataset coordinates for plotting
    RF_freq_control = np.array([dfs + qp.qubit_control.resonator.RF_frequency for qp in qubit_pairs])
    RF_freq_target = np.array([dfs + qp.qubit_target.resonator.RF_frequency for qp in qubit_pairs])
    
    ds_control = ds_control.assign_coords({"freq_full": (["qubit", "freq"], RF_freq_control)})
    ds_control.freq_full.attrs["long_name"] = "Frequency"
    ds_control.freq_full.attrs["units"] = "GHz"
    
    ds_target = ds_target.assign_coords({"freq_full": (["qubit", "freq"], RF_freq_target)})
    ds_target.freq_full.attrs["long_name"] = "Frequency"
    ds_target.freq_full.attrs["units"] = "GHz"
    
    
    # Add the current axis of each qubit to the dataset coordinates for plotting
    # current = np.array(
    #     [ds.flux.values / node.parameters.input_line_impedance_in_ohm for q in qubits]
    # )
    # ds = ds.assign_coords({"current": (["qubit", "flux"], current)})
    # ds.current.attrs["long_name"] = "Current"
    # ds.current.attrs["units"] = "A"
    # # Add attenuated current to dataset
    # attenuation_factor = 10 ** (-node.parameters.line_attenuation_in_db / 20)
    # attenuated_current = ds.current * attenuation_factor
    # ds = ds.assign_coords(
    #     {"attenuated_current": (["qubit", "flux"], attenuated_current.values)}
    # )
    # ds.attenuated_current.attrs["long_name"] = "Attenuated Current"
    # ds.attenuated_current.attrs["units"] = "A"
    # Add the dataset to the node
    node.results = {"ds": ds}

# %% {Data_analysis}
if not node.parameters.simulate:
    # Find the minimum of each frequency line to follow the resonance vs flux
    peak_freq_control  = ds_control.IQ_abs.idxmin(dim="freq")
    peak_freq_target  = ds_target.IQ_abs.idxmin(dim="freq")
    # Fit to a cosine using the qiskit function: a * np.cos(2 * np.pi * f * t + phi) + offset
    fit_osc_control = fit_oscillation(peak_freq_control.dropna(dim="flux"), "flux")
    fit_osc_target = fit_oscillation(peak_freq_target.dropna(dim="flux"), "flux")
    # Ensure that the phase is between -pi and pi
    idle_offset_control = -fit_osc_control.sel(fit_vals="phi")
    idle_offset_control = np.mod(idle_offset_control + np.pi, 2 * np.pi) - np.pi
    idle_offset_target = -fit_osc_target.sel(fit_vals="phi")
    idle_offset_target = np.mod(idle_offset_target + np.pi, 2 * np.pi) - np.pi
    # converting the phase phi from radians to voltage
    idle_offset_control = idle_offset_control / fit_osc_control.sel(fit_vals="f") / 2 / np.pi
    idle_offset_target = idle_offset_target / fit_osc_target.sel(fit_vals="f") / 2 / np.pi
    
    # Save fitting results
    fit_results = {}
    for qp in qubit_pairs:
        fit_results[qp.name] = {}
        fit_results[qp.name]["mutual_flux_point"] = [
            float(idle_offset_control.sel(qubit=qp.id).values),
            float(idle_offset_target.sel(qubit=qp.id).values),
        ]
        

    node.results["fit_results"] = fit_results

# %% {Plotting}
if not node.parameters.simulate:
    # Reload the plot_utils module to ensure we have the latest version

    
    grid_names, qubit_pair_names = grid_pair_names(qubit_pairs)
    grid = QubitPairGrid(grid_names, qubit_pair_names)
    for ax, qubit in grid_iter(grid):
        ds_control.assign_coords(freq_GHz=ds_control.freq_full / 1e9).loc[qubit].IQ_abs.plot(
            ax=ax, add_colorbar=False, x="flux", y="freq_GHz", robust=True
        )
        ax.axvline(idle_offset_control.loc[qubit], linestyle="dashed", linewidth=2, color="r")
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
        ds_target.assign_coords(freq_GHz=ds_target.freq_full / 1e9).loc[qubit].IQ_abs.plot(
            ax=ax, add_colorbar=False, x="flux", y="freq_GHz", robust=True
        )        
        ax.axvline(idle_offset_target.loc[qubit], linestyle="dashed", linewidth=2, color="r")
        # Location of the current resonator frequency
        ax.set_title(qubit["qubit"])
        ax.set_xlabel("Flux (V)")

    grid.fig.suptitle("Resonator spectroscopy vs flux for target")
    plt.tight_layout()
    plt.show()
    node.results["figure_target"] = grid.fig
# %% {Update_state}
if not node.parameters.simulate:
    with node.record_state_updates():
        for qp in qubit_pairs:
            qp.mutual_flux_bias = fit_results[qp.name]["mutual_flux_point"]

# %% {Save_results}
if not node.parameters.simulate:
    node.outcomes = {qp.name: "successful" for qp in qubit_pairs}
    node.results["initial_parameters"] = node.parameters.model_dump()
    node.machine = machine
    node.save()

# %%
