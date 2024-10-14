# %%
"""
        QUBIT SPECTROSCOPY VERSUS FLUX
This sequence involves doing a qubit spectroscopy for several flux biases in order to exhibit the qubit frequency
versus flux response.

Prerequisites:
    - Identification of the resonator's resonance frequency when coupled to the qubit in question (referred to as "resonator_spectroscopy").
    - Calibration of the IQ mixer connected to the qubit drive line (whether it's an external mixer or an Octave port).
    - Identification of the approximate qubit frequency ("qubit_spectroscopy").

Before proceeding to the next node:
    - Update the qubit frequency, labeled as "f_01", in the state.
    - Update the relevant flux points in the state.
    - Save the current state by calling machine.save("quam")
"""


# %% {Imports}
from qualibrate import QualibrationNode, NodeParameters
from quam_libs.components import QuAM
from quam_libs.macros import qua_declaration
from quam_libs.lib.plot_utils import QubitGrid, grid_iter
from quam_libs.lib.save_utils import fetch_results_as_xarray
from quam_libs.lib.fit import peaks_dips
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

    qubit_pairs: Optional[List[str]] = ["q0-q1","q1-q2"]
    num_averages: int = 200
    operation: str = "saturation"
    operation_amplitude_factor: Optional[float] = 0.1
    operation_len_in_ns: Optional[int] = None
    frequency_span_in_mhz: float = 20
    frequency_step_in_mhz: float = 0.25
    min_flux_offset_in_v: float = -0.01
    max_flux_offset_in_v: float = 0.01
    num_flux_points: int = 11
    flux_point_joint_or_independent_or_pairwise: Literal["joint", "independent", "pairwise"] = "pairwise"
    simulate: bool = False
    timeout: int = 100


node = QualibrationNode(
    name="61_pairwise_qubit_spectroscopy_vs_flux", parameters=Parameters()
)




# %% {Initialize_QuAM_and_QOP}
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
if node.parameters.qubit_pairs is None or node.parameters.qubit_pairs == "":
    qubit_pairs = machine.active_qubit_pairs
else:
    qubit_pairs = [machine.qubit_pairs[qp] for qp in node.parameters.qubit_pairs]

num_qubit_pairs = len(qubit_pairs)


# %% {QUA_program}
n_avg = node.parameters.num_averages  # The number of averages
operation = (
    node.parameters.operation
)  # The qubit operation to play, can be switched to "x180" when the qubits are found.
# Adjust the pulse duration and amplitude to drive the qubit into a mixed state
operation_len = (
    node.parameters.operation_len_in_ns
)  # can be None - will just be ignored
if node.parameters.operation_amplitude_factor:
    # pre-factor to the value defined in the config - restricted to [-2; 2)
    operation_amp = node.parameters.operation_amplitude_factor
else:
    operation_amp = 1.0
# Qubit detuning sweep with respect to their resonance frequencies
span = node.parameters.frequency_span_in_mhz * u.MHz
step = node.parameters.frequency_step_in_mhz * u.MHz
# dfs = np.arange(-span//2, +span//2, step, dtype=np.int32)
dfs = np.arange(-span // 2, 10e6, step, dtype=np.int32)
# Flux bias sweep
dcs = np.linspace(
    node.parameters.min_flux_offset_in_v,
    node.parameters.max_flux_offset_in_v,
    node.parameters.num_flux_points,
)
flux_point = node.parameters.flux_point_joint_or_independent_or_pairwise  # 'joint' or 'independent' or 'pairwise'

with program() as multi_qubit_spec_vs_flux:
    # Macro to declare I, Q, n and their respective streams for a given number of qubit (defined in macros.py)
    I1, I1_st, Q1, Q1_st, n, n_st = qua_declaration(num_qubits=num_qubit_pairs)
    I2, I2_st, Q2, Q2_st , _, _= qua_declaration(num_qubits=num_qubit_pairs)
    df = declare(int)  # QUA variable for the qubit frequency
    dc = declare(fixed)  # QUA variable for the flux dc level

    for i, qp in enumerate(qubit_pairs):

        qubit = qp.qubit_control
        mutual_flux_point = machine.set_all_fluxes(flux_point, qp)
        wait(1000)

        with for_(n, 0, n < n_avg, n + 1):
            save(n, n_st)

            with for_(*from_array(df, dfs)):
                # Update the qubit frequencies for all qubits
                qubit.xy.update_frequency(df + qubit.xy.intermediate_frequency)

                with for_(*from_array(dc, dcs)):
                    # Flux sweeping for a qubit
                    qubit.z.set_dc_offset(dc + mutual_flux_point[0])
                    wait(250, qubit.z.name)  # Wait for the flux to settle

                    align()

                    # Apply saturation pulse to all qubits
                    qubit.xy.play(
                        operation,
                        amplitude_scale=operation_amp,
                        duration=operation_len,
                    )

                    qubit.xy.wait(250)
                    qubit.align()

                    # Flux sweeping for a qubit
                    qubit.z.set_dc_offset(mutual_flux_point[0])
                    qubit.align()
                    # QUA macro to read the state of the active resonators
                    qubit.resonator.measure("readout", qua_vars=(I1[i], Q1[i]))
                    # save data
                    save(I1[i], I1_st[i])
                    save(Q1[i], Q1_st[i])
                    # Wait for the qubits to decay to the ground state
                    qubit.resonator.wait(machine.depletion_time * u.ns)

        align()

        qubit = qp.qubit_target
        mutual_flux_point = machine.set_all_fluxes(flux_point, qp)
        wait(1000)

        with for_(n, 0, n < n_avg, n + 1):
            save(n, n_st)

            with for_(*from_array(df, dfs)):
                # Update the qubit frequencies for all qubits
                qubit.xy.update_frequency(df + qubit.xy.intermediate_frequency)

                with for_(*from_array(dc, dcs)):
                    # Flux sweeping for a qubit
                    qubit.z.set_dc_offset(dc + mutual_flux_point[1])
                    wait(250, qubit.z.name)  # Wait for the flux to settle

                    align()

                    # Apply saturation pulse to all qubits
                    qubit.xy.play(
                        operation,
                        amplitude_scale=operation_amp,
                        duration=operation_len,
                    )

                    qubit.xy.wait(250)
                    qubit.align()

                    # Flux sweeping for a qubit
                    qubit.z.set_dc_offset(mutual_flux_point[1])
                    qubit.align()
                    # QUA macro to read the state of the active resonators
                    qubit.resonator.measure("readout", qua_vars=(I2[i], Q2[i]))
                    # save data
                    save(I2[i], I2_st[i])
                    save(Q2[i], Q2_st[i])
                    # Wait for the qubits to decay to the ground state
                    qubit.resonator.wait(machine.depletion_time * u.ns)

        align()

    with stream_processing():
        n_st.save("n")
        for i in range(num_qubit_pairs):
            I1_st[i].buffer(len(dcs)).buffer(len(dfs)).average().save(f"I_control{i + 1}")
            Q1_st[i].buffer(len(dcs)).buffer(len(dfs)).average().save(f"Q_control{i + 1}")
            I2_st[i].buffer(len(dcs)).buffer(len(dfs)).average().save(f"I_target{i + 1}")
            Q2_st[i].buffer(len(dcs)).buffer(len(dfs)).average().save(f"Q_target{i + 1}")


# %% {Simulate_or_execute}
if node.parameters.simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=10_000)  # In clock cycles = 4ns
    job = qmm.simulate(config, multi_qubit_spec_vs_flux, simulation_config)
    job.get_simulated_samples().con1.plot()
    node.results = {"figure": plt.gcf()}
    node.machine = machine
    node.save()

else:
    with qm_session(qmm, config, timeout=node.parameters.timeout) as qm:
        job = qm.execute(multi_qubit_spec_vs_flux)
        results = fetching_tool(job, ["n"], mode="live")
        while results.is_processing():
            # Fetch results
            n = results.fetch_all()[0]
            # Progress bar
            progress_counter(n, n_avg, start_time=results.start_time)

# %% {Data_fetching_and_dataset_creation}
if not node.parameters.simulate:
    # Fetch the data from the OPX and convert it into a xarray with corresponding axes (from most inner to outer loop)
    ds = fetch_results_as_xarray(job.result_handles, qubit_pairs, {"flux": dcs, "freq": dfs})
    # Derive the amplitude IQ_abs = sqrt(I**2 + Q**2)
    ds_control = ds[["I_control", "Q_control"]]
    ds_target = ds[["I_target", "Q_target"]]    
    
    ds_control = ds_control.assign({"IQ_abs": np.sqrt(ds_control["I_control"] ** 2 + ds_control["Q_control"] ** 2)})
    ds_target = ds_target.assign({"IQ_abs": np.sqrt(ds_target["I_target"] ** 2 + ds_target["Q_target"] ** 2)})
    # Add the resonator RF frequency axis of each qubit to the dataset coordinates for plotting
    # ds = ds.assign_coords(
    #     {
    #         "freq_full": (
    #             ["qubit", "freq"],
    #             np.array([dfs + q.xy.RF_frequency for q in qubits]),
    #         )
    #     }
    # )
    # ds.freq_full.attrs["long_name"] = "Frequency"
    # ds.freq_full.attrs["units"] = "GHz"
    # Add the dataset to the node
    node.results = {"ds": ds}

    # %% {Data_analysis}
    # Find the resonance dips for each flux point
    peaks_control = peaks_dips(ds.IQ_abs_control, dim="freq", prominence_factor=7)
    peaks_target = peaks_dips(ds.IQ_abs_target, dim="freq", prominence_factor=7)
    # Fit the result with a parabola
    parabolic_fit_results_control = peaks_control.position.polyfit("flux", 2)
    parabolic_fit_results_target = peaks_target.position.polyfit("flux", 2)
    # Extract relevant fitted parameters
    coeff_control = parabolic_fit_results_control.polyfit_coefficients
    coeff_target = parabolic_fit_results_target.polyfit_coefficients
    fitted_control = (
        coeff_control.sel(degree=2) * ds.flux**2
        + coeff_control.sel(degree=1) * ds.flux
        + coeff_control.sel(degree=0)
    )
    fitted_target = (
        coeff_target.sel(degree=2) * ds.flux**2
        + coeff_target.sel(degree=1) * ds.flux
        + coeff_target.sel(degree=0)
    )
    flux_shift_control = -coeff_control.sel(degree=1) / (2 * coeff_control.sel(degree=0))
    flux_shift_target = -coeff_target.sel(degree=1) / (2 * coeff_target.sel(degree=0))
    freq_shift_control = (
        coeff_control.sel(degree=2) * flux_shift_control**2
        + coeff_control.sel(degree=1) * flux_shift_control
            + coeff_control.sel(degree=0)
    )
    freq_shift_target = (
        coeff_target.sel(degree=2) * flux_shift_target**2
        + coeff_target.sel(degree=1) * flux_shift_target
        + coeff_target.sel(degree=0)
    )
    
    # Save fitting results
    fit_results = {}
    for qp in qubit_pairs:
        fit_results[qp.name] = {}
        if not np.isnan(flux_shift_control.sel(qubit=qp.qubit_control.name).values):
            if flux_point == "independent":
                offset = qp.qubit_control.z.independent_offset
            elif flux_point == "joint":
                offset = qp.qubit_control.z.joint_offset
            print(
                f"flux offset for qubit {qp.name} is {offset*1e3 + flux_shift.sel(qubit = qp.name).values*1e3:.0f} mV"
            )
            print(f"(shift of  {flux_shift.sel(qubit = qp.name).values*1e3:.0f} mV)")
            print(
                f"Drive frequency for {qp.name} is {(freq_shift.sel(qubit = q.name).values + q.xy.RF_frequency)/1e9:.3f} GHz"
            )
            print(f"(shift of {freq_shift.sel(qubit = qp.name).values/1e6:.0f} MHz)")
            print(
                f"quad term for qubit {qp.name} is {float(coeff.sel(degree = 2, qubit = qp.name)/1e9):.3e} GHz/V^2 \n"
            )
            fit_results[qp.name]["flux_shift"] = float(
                flux_shift.sel(qubit=qp.name).values
            )
            fit_results[q.name]["drive_freq"] = float(
                freq_shift.sel(qubit=qp.name).values
            )
            fit_results[q.name]["quad_term"] = float(coeff.sel(degree=2, qubit=q.name))
        else:
            print(f"No fit for qubit {q.name}")
            fit_results[q.name]["flux_shift"] = np.nan
            fit_results[q.name]["drive_freq"] = np.nan
            fit_results[q.name]["quad_term"] = np.nan
    node.results["fit_results"] = fit_results


# %% {Plotting}
if not node.parameters.simulate:
        
    grid = QubitGrid(ds, [q.grid_location for q in qubits])

    for ax, qubit in grid_iter(grid):
        freq_ref = machine.qubits[qubit["qubit"]].xy.RF_frequency
        ds.assign_coords(freq_GHz=ds.freq_full / 1e9).loc[qubit].I.plot(
            ax=ax, add_colorbar=False, x="flux", y="freq_GHz", robust=True
        )
        ((fitted + freq_ref) / 1e9).loc[qubit].plot(
            ax=ax, linewidth=0.5, ls="--", color="r"
        )
        ax.plot(flux_shift.loc[qubit], ((freq_shift.loc[qubit] + freq_ref) / 1e9), "r*")
        ((peaks.position.loc[qubit] + freq_ref) / 1e9).plot(
            ax=ax, ls="", marker=".", color="g", ms=0.5
        )
        ax.set_ylabel("Freq (GHz)")
        ax.set_xlabel("Flux (V)")
        ax.set_title(qubit["qubit"])
    grid.fig.suptitle("Qubit spectroscopy vs flux ")

    plt.tight_layout()
    plt.show()
    node.results["figure"] = grid.fig

    # %% {Update_state}
    with node.record_state_updates():
        for q in qubits:
            if not np.isnan(flux_shift.sel(qubit=q.name).values):
                if flux_point == "independent":
                    q.z.independent_offset += fit_results[q.name]["flux_shift"]
                elif flux_point == "joint":
                    q.z.joint_offset += fit_results[q.name]["flux_shift"]
                q.xy.intermediate_frequency += fit_results[q.name]["drive_freq"]
                q.freq_vs_flux_01_quad_term = fit_results[q.name]["quad_term"]

    ds = ds.drop_vars("freq_full")
    node.results["ds"] = ds

    # %% {Save_results}
    node.outcomes = {q.name: "successful" for q in qubits}
    node.results["initial_parameters"] = node.parameters.model_dump()
    node.machine = machine
    node.save()
