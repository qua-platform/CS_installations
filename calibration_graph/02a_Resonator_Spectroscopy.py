# %%
"""
        RESONATOR SPECTROSCOPY MULTIPLEXED
This sequence involves measuring the resonator by sending a readout pulse and demodulating the signals to extract the
'I' and 'Q' quadratures across varying readout intermediate frequencies for all resonators simultaneously.
The data is then post-processed to determine the resonator resonance frequency.
This frequency can be used to update the readout frequency in the state.

Prerequisites:
    - Ensure calibration of the time of flight, offsets, and gains (referenced as "time_of_flight").
    - Calibrate the IQ mixer connected to the readout line (whether it's an external mixer or an Octave port).
    - Define the readout pulse amplitude and duration in the state.
    - Specify the expected resonator depletion time in the state.

Before proceeding to the next node:
    - Update the readout frequency, in the state for all resonators.
    - Save the current state
"""

# %% {Imports}
from qualibrate import QualibrationNode, NodeParameters
from quam_libs.components import QuAM
from quam_libs.macros import qua_declaration
from quam_libs.lib.fit_utils import fit_resonator
from quam_libs.lib.qua_datasets import apply_angle, subtract_slope
from quam_libs.lib.plot_utils import QubitGrid, grid_iter, grid_names
from quam_libs.lib.save_utils import fetch_results_as_xarray, load_dataset
from qualang_tools.results import progress_counter, fetching_tool
from qualang_tools.plot import interrupt_on_close
from qualang_tools.loops import from_array
from qualang_tools.multi_user import qm_session
from qualang_tools.units import unit
from qm import SimulationConfig
from qm.qua import *
from typing import Optional, List
import matplotlib.pyplot as plt
from scipy import signal
import numpy as np


# %% {Node_parameters}
class Parameters(NodeParameters):

    qubits: Optional[List[str]] = None
    num_averages: int = 100
    frequency_span_in_mhz: float = 30.0
    frequency_step_in_mhz: float = 0.1
    simulate: bool = False
    timeout: int = 100
    load_data_id: Optional[int] = None # 1688
    multiplexed: bool = False

node = QualibrationNode(name="02a_Resonator_Spectroscopy", parameters=Parameters())
assert not (node.parameters.simulate and node.parameters.load_data_id is not None), "If simulate is True, load_data_id must be None, and vice versa."

# %% {Initialize_QuAM_and_QOP}
# Class containing tools to help handling units and conversions.
u = unit(coerce_to_integer=True)
# Instantiate the QuAM class from the state file
# path = r"C:\\Users\\tomdv\\Documents\\QCC_QUAM\\qw_statestore_QCC\\quam_state"
machine = QuAM.load()
# Generate the OPX and Octave configurations
config = machine.generate_config()
octave_config = machine.get_octave_config()
# Open Communication with the QOP
if node.parameters.load_data_id is None:
    qmm = machine.connect()

# Get the relevant QuAM components
if node.parameters.qubits is None or node.parameters.qubits == "":
    qubits = machine.active_qubits
else:
    qubits = [machine.qubits[q] for q in node.parameters.qubits]
resonators = [qubit.resonator for qubit in qubits]
num_qubits = len(qubits)
num_resonators = len(resonators)


# %% {QUA_program}
n_avg = node.parameters.num_averages
# The frequency sweep around the resonator resonance frequency
span = node.parameters.frequency_span_in_mhz * u.MHz
step = node.parameters.frequency_step_in_mhz * u.MHz
dfs = np.arange(-span / 2, +span / 2, step)

with program() as multi_res_spec:
    # Declare 'I' and 'Q' and the corresponding streams for the two resonators.
    # For instance, here 'I' is a python list containing two QUA fixed variables.
    I, I_st, Q, Q_st, n, n_st = qua_declaration(num_qubits=num_qubits)
    df = declare(int)  # QUA variable for the readout frequency

    # Bring the active qubits to the minimum frequency point
    machine.apply_all_flux_to_min()

    with for_(n, 0, n < n_avg, n + 1):
        for i, rr in enumerate(resonators):
            with for_(*from_array(df, dfs)):
                # Update the resonator frequencies for all resonators
                update_frequency(rr.name, df + rr.intermediate_frequency)
                # Measure the resonator
                rr.measure("readout", qua_vars=(I[i], Q[i]))
                # wait for the resonator to relax
                rr.wait(machine.depletion_time * u.ns)
                # save data
                save(I[i], I_st[i])
                save(Q[i], Q_st[i])
            if not node.parameters.multiplexed:
                align()

    with stream_processing():
        for i in range(num_qubits):
            I_st[i].buffer(len(dfs)).average().save(f"I{i + 1}")
            Q_st[i].buffer(len(dfs)).average().save(f"Q{i + 1}")


# %% {Simulate_or_execute}
if node.parameters.simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=10_000)  # In clock cycles = 4ns
    # Simulate blocks python until the simulation is done
    job = qmm.simulate(config, multi_res_spec, simulation_config)
    # Plot the simulated samples
    job.get_simulated_samples().con1.plot()
    # Update the node & save
    node.results = {"figure": plt.gcf()}
    node.machine = machine
    node.save()
    
elif node.parameters.load_data_id is None:
    # Open a quantum machine to execute the QUA program
    with qm_session(qmm, config, timeout=node.parameters.timeout) as qm:
        job = qm.execute(multi_res_spec)
        
        # {Live_plot}
        # Tool to easily fetch results from the OPX (results_handle used in it)
        data_list = sum([[f"I{i + 1}", f"Q{i + 1}"] for i in range(num_qubits)], [])
        results = fetching_tool(job, data_list, mode="live")
        # Prepare the figures for live plotting
        fig, axss = plt.subplots(2, num_qubits, figsize=(4 * num_qubits, 5))
        if len(axss.shape) == 1:
            axss = np.expand_dims(axss, -1)
        interrupt_on_close(fig, job)
        s_data = []
        while results.is_processing():
            # Fetch results
            data = results.fetch_all()
            for i in range(num_qubits):
                I, Q = data[2 * i : 2 * i + 2]
                rr = resonators[i]
                # Data analysis
                s_data.append(
                    u.demod2volts(I + 1j * Q, rr.operations["readout"].length)
                )
                # Plot
                plt.sca(axss[0, i])
                plt.suptitle("Multiplexed resonator spectroscopy")
                plt.cla()
                plt.plot(rr.RF_frequency / u.MHz + dfs / u.MHz, np.abs(s_data[-1]), ".")
                plt.title(f"{rr.name}")
                plt.ylabel(r"R=$\sqrt{I^2 + Q^2}$ [V]")
                plt.sca(axss[1, i])
                plt.cla()
                plt.plot(
                    rr.RF_frequency / u.MHz + dfs / u.MHz,
                    signal.detrend(np.unwrap(np.angle(s_data[-1]))),
                    ".",
                )
                plt.ylabel("Phase [rad]")
                plt.xlabel("Readout frequency [MHz]")
                plt.tight_layout()
                plt.pause(0.1)
                
# %% {Data_fetching_and_dataset_creation}
if not node.parameters.simulate:
    # Fetch the data from the OPX and convert it into a xarray with corresponding axes (from most inner to outer loop)
    if node.parameters.load_data_id is not None:
        ds = load_dataset(node.parameters.load_data_id)
    else:
        ds = fetch_results_as_xarray(job.result_handles, qubits, {"freq": dfs})

    ds = ds.assign({"IQ_abs": np.sqrt(ds["I"] ** 2 + ds["Q"] ** 2)})
    ds = ds.assign(
        {"phase": subtract_slope(apply_angle(ds.I + 1j * ds.Q, dim="freq"), dim="freq")}
    )

    def abs_freq(q, freq):
        return freq + q.resonator.RF_frequency

    ds = ds.assign_coords(
        {"freq_full": (["qubit", "freq"], np.array([abs_freq(q, dfs) for q in qubits]))}
    )
    node.results = {"ds": ds}

# %% {Data_analysis}
if node.parameters.simulate is False:

    fits = {}
    fit_evals = {}
    fit_results = {}

    for index, q in enumerate(qubits):
        fit, fit_eval = fit_resonator(ds.sel(qubit=q.name), q.resonator.RF_frequency)
        fits[q.name] = fit
        fit_evals[q.name] = fit_eval
        Qe = np.abs(fit.params["Qe_real"].value + 1j * fit.params["Qe_imag"].value)
        Qi = 1 / (1 / fit.params["Q"].value - 1 / Qe)
        fit_results[q.name] = {}
        fit_results[q.name]["resonator_freq"] = (
            fit.params["omega_r"].value + q.resonator.RF_frequency
        )
        fit_results[q.name]["Quality_external"] = Qe
        fit_results[q.name]["Quality_internal"] = Qi
        print(
            f"Resonator frequency for {q.name} is {(fit.params['omega_r'].value + q.resonator.RF_frequency) / 1e9:.3f} GHz"
        )
        print(
            f"freq shift for {q.name} is {fit.params['omega_r'].value/1e6:.0f} MHz with respect to the IF"
        )
        print(f"Qe for {q.name} is {Qe:,.0f}")
        print(f"Qi for {q.name} is {Qi:,.0f} \n")

# %% {Plotting}
if node.parameters.simulate is False:
    grid = QubitGrid(ds, [q.grid_location for q in qubits])
    for ax, qubit in grid_iter(grid):
        (ds.assign_coords(freq_MHz=ds.freq / 1e6).loc[qubit].IQ_abs * 1e3).plot(
            ax=ax, x="freq_MHz"
        )
        ax.set_xlabel("Resonator detuning [MHz]")
        ax.set_ylabel("Trans. amp. [mV]")
        ax.set_title(qubit["qubit"])
    grid.fig.suptitle("Resonator spectroscopy (raw data)")
    plt.tight_layout()
    node.results["raw_amplitude"] = grid.fig

    grid = QubitGrid(ds, [q.grid_location for q in qubits])
    for ax, qubit in grid_iter(grid):
        (ds.assign_coords(freq_MHz=ds.freq / 1e6).loc[qubit].phase * 1e3).plot(
            ax=ax, x="freq_MHz"
        )
        ax.set_xlabel("Resonator detuning [MHz]")
        ax.set_ylabel("Trans. phase [rad]")
        ax.set_title(qubit["qubit"])
    grid.fig.suptitle("Resonator spectroscopy (raw data)")
    plt.tight_layout()
    node.results["raw_phase"] = grid.fig

    grid = QubitGrid(ds, [q.grid_location for q in qubits])
    for ax, qubit in grid_iter(grid):
        (ds.assign_coords(freq_GHz=ds.freq_full / 1e9).loc[qubit].IQ_abs * 1e3).plot(
            ax=ax, x="freq_GHz"
        )
        ax.plot(
            ds.assign_coords(freq_GHz=ds.freq_full / 1e9).loc[qubit].freq_GHz,
            1e3 * np.abs(fit_evals[qubit["qubit"]]),
        )
        ax.set_xlabel("Resonator freq [GHz]")
        ax.set_ylabel("Trans. amp. [mV]")
        ax.set_title(qubit["qubit"])
    grid.fig.suptitle("Resonator spectroscopy (fit)")
    node.results["fitted_amp"] = grid.fig

    plt.tight_layout()
    plt.show()

# %% {Update_state}
if node.parameters.load_data_id is None and node.parameters.simulate is False:
    with node.record_state_updates():
        for index, q in enumerate(qubits):
            q.resonator.intermediate_frequency += int(
                fits[q.name].params["omega_r"].value
            )

# %% {Save_results}
if node.parameters.simulate is False:
    node.outcomes = {q.name: "successful" for q in qubits}
    node.results["initial_parameters"] = node.parameters.model_dump()
    node.machine = machine
    node.save()
    print("Results saved")

# %%
