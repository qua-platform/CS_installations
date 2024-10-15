# %%
"""
        IQ BLOBS
This sequence involves measuring the state of the resonator 'N' times, first after thermalization (with the qubit
in the |g> state) and then after applying a pi pulse to the qubit (bringing the qubit to the |e> state) successively.
The resulting IQ blobs are displayed, and the data is processed to determine:
    - The rotation angle required for the integration weights, ensuring that the separation between |g> and |e> states
      aligns with the 'I' quadrature.
    - The threshold along the 'I' quadrature for effective qubit state discrimination.
    - The readout fidelity matrix, which is also influenced by the pi pulse fidelity.

Prerequisites:
    - Having found the resonance frequency of the resonator coupled to the qubit under study (resonator_spectroscopy).
    - Having calibrated qubit pi pulse (x180) by running qubit, spectroscopy, rabi_chevron, power_rabi and updated the state.
    - Set the desired flux bias

Next steps before going to the next node:
    - Update the rotation angle (rotation_angle) in the state.
    - Update the g -> e threshold (ge_threshold) in the state.
    - Save the current state by calling machine.save("quam")
"""
# TODO: this script isn't working great, the readout amp found at the end isn't always correct maybe because of SNR...

# %% {Imports}
from qualibrate import QualibrationNode, NodeParameters
from quam_libs.components import QuAM
from quam_libs.macros import qua_declaration, active_reset
from quam_libs.lib.plot_utils import QubitGrid, grid_iter
from quam_libs.lib.save_utils import fetch_results_as_xarray
from qualang_tools.analysis import two_state_discriminator
from qualang_tools.results import progress_counter, fetching_tool
from qualang_tools.loops import from_array
from qualang_tools.multi_user import qm_session
from qualang_tools.units import unit
from qm import SimulationConfig
from qm.qua import *
from typing import Literal, Optional, List
import matplotlib.pyplot as plt
import numpy as np
import xarray as xr
from quam.components.pulses import SquareReadoutPulse

# %% {Node_parameters}
class Parameters(NodeParameters):

    qubits: Optional[List[str]] = None
    num_runs: int = 2000
    reset_type_thermal_or_active: Literal['thermal', 'active'] = "thermal"
    flux_point_joint_or_independent: Literal['joint', 'independent'] = "joint"
    simulate: bool = False
    timeout: int = 100
    start_amp: float = 0.5
    end_amp: float = 1.99
    num_amps: int = 5
    outliers_threshold: float = 0.98

node = QualibrationNode(
    name="07b_Readout_Power_Optimization",
    parameters=Parameters()
)

from sklearn.mixture import GaussianMixture


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
if node.parameters.qubits is None or node.parameters.qubits == '':
    qubits = machine.active_qubits
else:
    qubits = [machine.qubits[q] for q in node.parameters.qubits]
num_qubits = len(qubits)
# %%

n_runs = node.parameters.num_runs  # Number of runs
flux_point = node.parameters.flux_point_joint_or_independent  # 'independent' or 'joint'
reset_type = node.parameters.reset_type_thermal_or_active  # "active" or "thermal"
amps = np.linspace(node.parameters.start_amp, node.parameters.end_amp, node.parameters.num_amps)

with program() as iq_blobs:
    I_g_a, I_g_a_st, Q_g_a, Q_g_a_st, n, n_st = qua_declaration(num_qubits=num_qubits)
    I_g_b, I_g_b_st, Q_g_b, Q_g_b_st, _, _ = qua_declaration(num_qubits=num_qubits)
    I_e_a, I_e_a_st, Q_e_a, Q_e_a_st, _, _ = qua_declaration(num_qubits=num_qubits)
    I_e_b, I_e_b_st, Q_e_b, Q_e_b_st, _, _ = qua_declaration(num_qubits=num_qubits)
    a = declare(fixed)
    
    for i, qubit in enumerate(qubits):

        machine.set_all_fluxes(flux_point, qubit)
        wait(1000)
        
        with for_(n, 0, n < n_runs, n + 1):
            # ground iq blobs for all qubits
            save(n, n_st)
            with for_(*from_array(a, amps)):
                if reset_type == "active":
                    active_reset(qubit)
                elif reset_type == "thermal":
                    wait(5*qubit.thermalization_time * u.ns)
                else:
                    raise ValueError(f"Unrecognized reset type {reset_type}.")

                qubit.align()
                qubit.resonator.measure("readout", qua_vars=(I_g_a[i], Q_g_a[i]), amplitude_scale=a)
                qubit.resonator.wait(qubit.resonator.depletion_time // 4)
                qubit.align()
                # save data
                save(I_g_a[i], I_g_a_st[i])
                save(Q_g_a[i], Q_g_a_st[i])
                qubit.resonator.measure("readout", qua_vars=(I_g_b[i], Q_g_b[i]), amplitude_scale=a)
                qubit.resonator.wait(qubit.resonator.depletion_time // 4)
                qubit.align()
                # save data
                save(I_g_b[i], I_g_b_st[i])
                save(Q_g_b[i], Q_g_b_st[i])
                                             
                if reset_type == "active":
                    active_reset(qubit)
                elif reset_type == "thermal":
                    wait(5*qubit.thermalization_time * u.ns)
                else:
                    raise ValueError(f"Unrecognized reset type {reset_type}.")
                align()
                qubit.xy.play('x180')
                align()
                qubit.resonator.measure("readout", qua_vars=(I_e_a[i], Q_e_a[i]), amplitude_scale=a)
                qubit.resonator.wait(qubit.resonator.depletion_time // 4)
                qubit.align()
                save(I_e_a[i], I_e_a_st[i])
                save(Q_e_a[i], Q_e_a_st[i])
                qubit.resonator.measure("readout", qua_vars=(I_e_b[i], Q_e_b[i]), amplitude_scale=a)
                qubit.resonator.wait(qubit.resonator.depletion_time // 4)
                qubit.align()
                save(I_e_b[i], I_e_b_st[i])
                save(Q_e_b[i], Q_e_b_st[i])

        align()
            

    with stream_processing():
        n_st.save("n")
        for i in range(num_qubits):
            I_g_a_st[i].buffer(len(amps)).buffer(n_runs).save(f"I_g_a{i + 1}")
            Q_g_a_st[i].buffer(len(amps)).buffer(n_runs).save(f"Q_g_a{i + 1}")
            I_g_b_st[i].buffer(len(amps)).buffer(n_runs).save(f"I_g_b{i + 1}")
            Q_g_b_st[i].buffer(len(amps)).buffer(n_runs).save(f"Q_g_b{i + 1}")
            I_e_a_st[i].buffer(len(amps)).buffer(n_runs).save(f"I_e_a{i + 1}")
            Q_e_a_st[i].buffer(len(amps)).buffer(n_runs).save(f"Q_e_a{i + 1}")
            I_e_b_st[i].buffer(len(amps)).buffer(n_runs).save(f"I_e_b{i + 1}")
            Q_e_b_st[i].buffer(len(amps)).buffer(n_runs).save(f"Q_e_b{i + 1}")


if node.parameters.simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=10_000)  # In clock cycles = 4ns
    job = qmm.simulate(config, iq_blobs, simulation_config)
    job.get_simulated_samples().con1.plot()
    node.results = {"figure": plt.gcf()}
    node.machine = machine
    node.save()

else:
    with qm_session(qmm, config, timeout=node.parameters.timeout) as qm:
        job = qm.execute(iq_blobs)

        for i in range(num_qubits):
            print(f"Fetching results for qubit {qubits[i].name}")
            data_list =  ["n"]
            results = fetching_tool(job, data_list, mode="live")
            while results.is_processing():
                fetched_data = results.fetch_all()
                n = fetched_data[0]
                progress_counter(n, n_runs, start_time=results.start_time)

# %% {Data_fetching_and_dataset_creation}
    
if not node.parameters.simulate:
    
    # Fetch the data from the OPX and convert it into a xarray with corresponding axes (from most inner to outer loop)
    ds = fetch_results_as_xarray(job.result_handles, qubits, {"amplitude": amps, "N": np.linspace(1, n_runs, n_runs)})

    def abs_amp(q):
        def foo(amp):
            return amp * q.resonator.operations["readout"].amplitude
        return foo

    ds = ds.assign_coords({'readout_amp' : (['qubit','amplitude'],np.array([abs_amp(q)(amps) for q in qubits]))})

    # Rearrange the data to combine I_g and I_e into I, and Q_g and Q_e into Q
    ds_rearranged = xr.Dataset()

    # Combine I_g and I_e into I
    ds_rearranged['I_a'] = xr.concat([ds.I_g_a, ds.I_e_a], dim='state')
    ds_rearranged['I_a'] = ds_rearranged['I_a'].assign_coords(state=[0, 1])
    ds_rearranged['I_b'] = xr.concat([ds.I_g_b, ds.I_e_b], dim='state')
    ds_rearranged['I_b'] = ds_rearranged['I_b'].assign_coords(state=[0, 1])

    # Combine Q_g and Q_e into Q
    ds_rearranged['Q_a'] = xr.concat([ds.Q_g_a, ds.Q_e_a], dim='state')
    ds_rearranged['Q_a'] = ds_rearranged['Q_a'].assign_coords(state=[0, 1])
    ds_rearranged['Q_b'] = xr.concat([ds.Q_g_b, ds.Q_e_b], dim='state')
    ds_rearranged['Q_b'] = ds_rearranged['Q_b'].assign_coords(state=[0, 1])

    # Copy other coordinates and data variables
    for var in ds.coords:
        if var not in ds_rearranged.coords:
            ds_rearranged[var] = ds[var]

    for var in ds.data_vars:
        if var not in ['I_g_a', 'I_e_a', 'Q_g_a', 'Q_e_a', 'I_g_b', 'I_e_b', 'Q_g_b', 'Q_e_b']:
            ds_rearranged[var] = ds[var]

    # Replace the original dataset with the rearranged one
    ds = ds_rearranged


    node.results = {"ds": ds}

    node.results["results"] = {}
    node.results["figs"] = {}
# %%
if not node.parameters.simulate:
    plot_raw = False

    if plot_raw:
        fig, axes = plt.subplots(ncols=num_qubits, nrows=len(ds.amplitude), sharex=False, sharey=False,
                                squeeze=False, figsize=(5*num_qubits, 5*len(ds.amplitude)))
        for amplitude, ax1 in zip(ds.amplitude, axes):
            for q, ax2 in zip(list(qubits), ax1):
                ds_q = ds.sel(qubit=q.name, amplitude=amplitude)
                ax2.plot(ds_q.I_a.sel(state=0), ds_q.Q_a.sel(state=0), ".", alpha=0.2, label="Ground", markersize=2)
                ax2.plot(ds_q.I_a.sel(state=1), ds_q.Q_a.sel(state=1), ".", alpha=0.2, label="Excited", markersize=2)
                ax2.plot(ds_q.I_b.sel(state=0), 2e-3+ds_q.Q_b.sel(state=0), ".", alpha=0.2, label="Ground", markersize=2)
                ax2.plot(ds_q.I_b.sel(state=1), 2e-3+ds_q.Q_b.sel(state=1), ".", alpha=0.2, label="Excited", markersize=2)
                ax2.set_xlabel('I')
                ax2.set_ylabel('Q')
                ax2.set_title(f'{q.name}, {float(amplitude)}')
                ax2.axis('equal')
        plt.show()
        node.results['figure_raw_data_a'] = fig
        
# %%
if not node.parameters.simulate:

    def apply_fit_gmm(I, Q):
        I_mean = np.mean(I, axis=1)
        Q_mean = np.mean(Q, axis=1)
        means_init = [[I_mean[0], Q_mean[0]], [I_mean[1], Q_mean[1]]]
        precisions_init = [
            1 / ((np.mean(np.var(I, axis=1)) + np.mean(np.var(Q, axis=1)))/2)] * 2
        clf = GaussianMixture(n_components=2, covariance_type='spherical', means_init=means_init,
                              precisions_init=precisions_init, tol=1e-5, reg_covar=1e-12)
        X = np.array([np.array(I).flatten(), np.array(Q).flatten()]).T
        clf.fit(X)
        meas_fidelity = (np.sum(clf.predict(np.array([I[0], Q[0]]).T) == 0)/len(
            I[0]) + np.sum(clf.predict(np.array([I[1], Q[1]]).T) == 1)/len(I[1]))/2
        loglikelihood = clf.score_samples(X)
        max_ll = np.max(loglikelihood)
        outliers = np.sum(loglikelihood > np.log(0.01) + max_ll) / len(X)
        return np.array([meas_fidelity, outliers])


    fit_res_a = xr.apply_ufunc(apply_fit_gmm, ds.I_a, ds.Q_a,
                             input_core_dims=[['state', 'N'], ['state', 'N']],
                             output_core_dims=[['result']],
                             vectorize=True)
    fit_res_b = xr.apply_ufunc(apply_fit_gmm, ds.I_b, ds.Q_b,
                             input_core_dims=[['state', 'N'], ['state', 'N']],
                             output_core_dims=[['result']],
                             vectorize=True)

    fit_res_a = fit_res_a.assign_coords(result=['meas_fidelity', 'outliers'])
    fit_res_b = fit_res_b.assign_coords(result=['meas_fidelity', 'outliers'])

    fit_res = xr.concat([fit_res_a, fit_res_b], dim='order')
    fit_res = fit_res.assign_coords(order=['a', 'b'])

    def apply_discriminator(I_g,Q_g,I_e,Q_e):
        angle, threshold, fidelity, gg, ge, eg, ee = two_state_discriminator(I_g, Q_g, I_e, Q_e, False, b_plot=False)
        I_rot = I_g * np.cos(angle) - Q_g * np.sin(angle)
        hist = np.histogram(I_rot, bins=100)
        RUS_threshold = hist[1][1:][np.argmax(hist[0])]
        return np.array([angle, threshold, fidelity, gg, ge, eg, ee, RUS_threshold])

    discriminator_res_a = xr.apply_ufunc(apply_discriminator, ds.I_a.sel(state=0), ds.Q_a.sel(state=0),ds.I_a.sel(state=1), ds.Q_a.sel(state=1),
                                input_core_dims=[['N'], ['N'], ['N'], ['N']],
                                output_core_dims=[['result']],
                                vectorize=True)
    discriminator_res_b = xr.apply_ufunc(apply_discriminator, ds.I_b.sel(state=0), ds.Q_b.sel(state=0),ds.I_b.sel(state=1), ds.Q_b.sel(state=1),
                                input_core_dims=[['N'], ['N'], ['N'], ['N']],
                                output_core_dims=[['result']],
                                vectorize=True)

    discriminator_res_a = discriminator_res_a.assign_coords(result=['angle', 'threshold', 'fidelity', 'gg', 'ge', 'eg', 'ee', 'rus_threshold'])
    discriminator_res_b = discriminator_res_b.assign_coords(result=['angle', 'threshold', 'fidelity', 'gg', 'ge', 'eg', 'ee', 'rus_threshold'])

    discriminator_res = xr.concat([discriminator_res_a, discriminator_res_b], dim='order')
    discriminator_res = discriminator_res.assign_coords(order=['a', 'b'])


    state = (ds.I_a * np.cos(discriminator_res.sel(result = "angle")) - ds.Q_a * np.sin(discriminator_res.sel(result = "angle"))) > discriminator_res.sel(result = "threshold")
    state_a = state.sel(order = "a")
    state_b = state.sel(order = "b")
    state00 = ((state_a == 0) & (state_b == 0)).sum(dim = ["N", "state"])   
    state01 = ((state_a == 0) & (state_b == 1)).sum(dim = ["N", "state"])
    state10 = ((state_a == 1) & (state_b == 0)).sum(dim = ["N", "state"])
    state11 = ((state_a == 1) & (state_b == 1)).sum(dim = ["N", "state"])

    Outliers = fit_res.sel(result = "outliers").mean(dim = "order")
    QND_fidelity = (state00 + state11) / (state00 + state01 + state10 + state11)
    Fidelity = (discriminator_res.sel(result = "gg", order = "a") + discriminator_res.sel(result = "ee", order = "a"))/2
    Valid_Fidelity = Fidelity * ((Outliers > 0.98) & (QND_fidelity > 0.98))
    best_amp = ds.amplitude[Valid_Fidelity.argmax(dim = 'amplitude')]
    
    best_readout_amp = {qubit.name : float(best_amp.sel(qubit = qubit.name).values * qubit.resonator.operations["readout"].amplitude) for qubit in qubits}
    best_data = {}
    node.results["results"] = {}
    for q in qubits:
        discriminator_res_q = discriminator_res.sel(amplitude = best_amp.sel(qubit = q.name).values,  order = 'a', qubit = q.name)
        best_data[q.name] = ds.sel(qubit = q.name, amplitude = best_amp.sel(qubit = q.name).values)
        node.results["results"][q.name] = {}
        node.results["results"][q.name]["best_amp"] = best_readout_amp[q.name]
        node.results["results"][q.name]["angle"] = float(discriminator_res_q.sel(result = "angle"))
        node.results["results"][q.name]["threshold"] = float(discriminator_res_q.sel(result = "threshold"))
        node.results["results"][q.name]["fidelity"] = float(discriminator_res_q.sel(result = "fidelity"))
        node.results["results"][q.name]["confusion_matrix"] = np.array([[discriminator_res_q.sel(result = "gg"), discriminator_res_q.sel(result = "ge")], [discriminator_res_q.sel(result = "eg"), discriminator_res_q.sel(result = "ee")]])
        node.results["results"][q.name]["rus_threshold"] = float(discriminator_res_q.sel(result = "rus_threshold"))

# %%
if not node.parameters.simulate:

    
    grid = QubitGrid(ds, [q.grid_location for q in qubits])
    for ax, qubit in grid_iter(grid):
        # fit_res.loc[qubit].plot(ax = ax,x = 'readout_amp', hue='result', add_legend=False)
        Fidelity.sel(qubit = qubit['qubit']).plot(ax = ax, marker = '.', x = "readout_amp", label = "Fidelity")
        Outliers.sel(qubit = qubit['qubit']).plot(ax = ax, marker = '.', x = "readout_amp", label = "Outliers")
        QND_fidelity.sel(qubit = qubit['qubit']).plot(ax = ax, marker = '.', x = "readout_amp", label = "QND Fidelity")
        ax.axvline(best_readout_amp[qubit['qubit']], color = 'k', linestyle = 'dashed')
        ax.set_xlabel('Relative power')
        ax.set_ylabel('Fidelity / outliers')
        ax.set_title(qubit['qubit'])
        ax.legend()
    grid.fig.suptitle('Assignment fidelity and non-outlier probability')

    plt.tight_layout()
    plt.show()
    node.results['figure_assignment_fid'] = grid.fig


# %%
if not node.parameters.simulate:
   
    grid = QubitGrid(ds, [q.grid_location for q in qubits])
    for ax, qubit in grid_iter(grid):
        ds_q = best_data[qubit['qubit']]
        qn = qubit['qubit']
        ax.plot(1e3*(ds_q.I_a.sel(state=0) * np.cos(node.results["results"][qn]["angle"]) - ds_q.Q_a.sel(state=0) * np.sin(node.results["results"][qn]["angle"])), 1e3*(ds_q.I_a.sel(state=0) * np.sin(node.results["results"][qn]["angle"]) + ds_q.Q_a.sel(state=0) * np.cos(node.results["results"][qn]["angle"])), ".", alpha=0.1, label="Ground", markersize=1)
        ax.plot(1e3 * (ds_q.I_a.sel(state=1) * np.cos(node.results["results"][qn]["angle"]) - ds_q.Q_a.sel(state=1) * np.sin(node.results["results"][qn]["angle"])), 1e3 * (ds_q.I_a.sel(state=1) * np.sin(node.results["results"][qn]["angle"]) + ds_q.Q_a.sel(state=1) * np.cos(node.results["results"][qn]["angle"])), ".", alpha=0.1, label="Excited", markersize=1)
        ax.axvline(1e3 * node.results["results"][qn]["rus_threshold"], color="k", linestyle="--", lw = 0.5, label="RUS Threshold")
        ax.axvline(1e3 * node.results["results"][qn]["threshold"], color="r", linestyle="--", lw = 0.5, label="Threshold")
        ax.axis("equal")
        ax.set_xlabel("I [mV]")
        ax.set_ylabel("Q [mV]")
        ax.set_title(qubit['qubit'])
        

    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    grid.fig.suptitle('g.s. and e.s. discriminators (rotated)')
    plt.tight_layout()
    node.results['figure_IQ_blobs'] = grid.fig


    grid = QubitGrid(ds, [q.grid_location for q in qubits])
    for ax, qubit in grid_iter(grid):
        confusion = node.results["results"][qubit['qubit']]["confusion_matrix"]
        ax.imshow(confusion)
        ax.set_xticks([0, 1])
        ax.set_yticks([0, 1])
        ax.set_xticklabels(labels=["|g>", "|e>"])
        ax.set_yticklabels(labels=["|g>", "|e>"])
        ax.set_ylabel("Prepared")
        ax.set_xlabel("Measured")
        ax.text(0, 0, f"{100 * confusion[0][0]:.1f}%", ha="center", va="center", color="k")
        ax.text(1, 0, f"{100 * confusion[0][1]:.1f}%", ha="center", va="center", color="w")
        ax.text(0, 1, f"{100 * confusion[1][0]:.1f}%", ha="center", va="center", color="w")
        ax.text(1, 1, f"{100 * confusion[1][1]:.1f}%", ha="center", va="center", color="k")
        ax.set_title(qubit['qubit'])

    grid.fig.suptitle('g.s. and e.s. fidelity')
    plt.tight_layout()
    plt.show()
    node.results['figure_fidelities'] = grid.fig

# %%
if not node.parameters.simulate:
    with node.record_state_updates():
        for qubit in qubits:
            qubit.resonator.operations["readout_QND"] = SquareReadoutPulse(length = q.resonator.operations["readout"].length, amplitude = 0.1, digital_marker = "ON")
            qubit.resonator.operations["readout_QND"].integration_weights_angle -= float(node.results["results"][qubit.name]["angle"])
            qubit.resonator.operations["readout_QND"].threshold = float(node.results["results"][qubit.name]["threshold"])
            qubit.resonator.operations["readout_QND"].rus_exit_threshold = float(node.results["results"][qubit.name]["rus_threshold"])
            qubit.resonator.operations["readout_QND"].amplitude = float(node.results["results"][qubit.name]["best_amp"])

# %% {Save_results}
node.outcomes = {q.name: "successful" for q in qubits}
node.results['initial_parameters'] = node.parameters.model_dump()
node.machine = machine
node.save()
# %%