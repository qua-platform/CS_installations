# %% {Imports}
import warnings
from dataclasses import asdict
import time
import matplotlib.pyplot as plt
import numpy as np
import xarray as xr
from qm.qua import *
from qualang_tools.loops import from_array
from qualang_tools.multi_user import qm_session
from qualang_tools.results import progress_counter, wait_until_job_is_paused
from qualang_tools.units import unit
from qualibrate import QualibrationNode
from quam_config import Quam
from calibration_utils.qubit_spectroscopy_vs_flux import (
    Parameters,
    fit_raw_data,
    log_fitted_results,
    plot_raw_data_with_fit,
    process_raw_dataset,
)
from qualibration_libs.parameters import get_qubits
from qualibration_libs.runtime import simulate_and_plot
from qualibration_libs.data import XarrayDataFetcher

# %% {Description}
description = """
        QUBIT SPECTROSCOPY VERSUS FLUX
This sequence involves doing a qubit spectroscopy for several flux biases in order to exhibit the qubit frequency
versus flux response.

Prerequisites:
    - Having calibrated the mixer or the Octave (nodes 01a or 01b).
    - Having calibrated the readout parameters (nodes 02a, 02b and/or 02c).
    - Having calibrated the qubit frequency (node 03a_qubit_spectroscopy.py).

State update:
    - The qubit 0->1 frequency at the set flux point: qubit.f_01 & qubit.xy.RF_frequency
"""


node = QualibrationNode[Parameters, Quam](
    name="03b_qubit_spectroscopy_vs_flux",
    description=description,
    parameters=Parameters(),
)


# Any parameters that should change for debugging purposes only should go in here
# These parameters are ignored when run through the GUI or as part of a graph
@node.run_action(skip_if=node.modes.external)
def custom_param(node: QualibrationNode[Parameters, Quam]):
    # You can get type hinting in your IDE by typing node.parameters.
    # node.parameters.qubits = ["q1", "q3"]

    pass


# Instantiate the QUAM class from the state file
node.machine = Quam.load()


# %% {Create_QUA_program}
@node.run_action(skip_if=node.parameters.load_data_id is not None)
def create_qua_program(node: QualibrationNode[Parameters, Quam]):
    """Create the sweep axes and generate the QUA program from the pulse sequence and the node parameters."""
    # Class containing tools to help handle units and conversions.
    u = unit(coerce_to_integer=True)
    # Get the active qubits from the node and organize them by batches
    node.namespace["qubits"] = qubits = get_qubits(node)
    num_qubits = len(qubits)
    # Check if the qubits have a z-line attached
    if any([q.z is None for q in qubits]):
        warnings.warn("Found qubits without a flux line. Skipping")

    operation = node.parameters.operation  # The qubit operation to play
    n_avg = node.parameters.num_shots
    # Adjust the pulse duration and amplitude to drive the qubit into a mixed state - can be None
    operation_len = node.parameters.operation_len_in_ns
    # pre-factor to the value defined in the config - restricted to [-2; 2)
    operation_amp = node.parameters.operation_amplitude_factor
    # Qubit detuning sweep with respect to their resonance frequencies
    span = node.parameters.frequency_span_in_mhz * u.MHz
    step = node.parameters.frequency_step_in_mhz * u.MHz
    dfs = np.arange(-span / 2, +span / 2, step)
    # Flux bias sweep in V
    span = node.parameters.flux_offset_span_in_v * u.V
    num = node.parameters.num_flux_points
    dcs = np.linspace(-span / 2, +span / 2, num)

    # Register the sweep axes to be added to the dataset when fetching data
    node.namespace["sweep_axes"] = {
        "qubit": xr.DataArray(qubits.get_names()),
        "detuning": xr.DataArray(dfs, attrs={"long_name": "qubit frequency", "units": "Hz"}),
        "flux_bias": xr.DataArray(dcs, attrs={"long_name": "flux bias", "units": "V"}),
    }

    ###################################
    # Helper functions and QUA macros #
    ###################################
    # Get the resonator frequency vs flux trend from the node 05_resonator_spec_vs_flux.py in order to always measure on
    # resonance while sweeping the flux
    def cosine_func(x, amplitude, frequency, phase, offset):
        return amplitude * np.cos(2 * np.pi * frequency * x + phase) + offset

    # The fit parameters are take from the config
    fitted_curve = cosine_func(dcs, amplitude_fit, frequency_fit, phase_fit, offset_fit) #TODO: ADD FUNCTION TO CREATE THE FITTER CURVE BASED ON RES SPEC VS FLUX PARAMETERS
    fitted_curve = fitted_curve.astype(int)

    with program() as node.namespace["qua_program"]:
        # Macro to declare I, Q, n and their respective streams for a given number of qubit
        I, I_st, Q, Q_st, n, n_st = node.machine.declare_qua_variables()
        df = declare(int)  # QUA variable for the qubit frequency
        dc = declare(fixed)  # QUA variable for the flux dc level
        resonator_freq = declare(int, value=fitted_curve.tolist())
        index = declare(int, value=0)  # index to get the right resonator freq for a given flux
        for multiplexed_qubits in qubits.batch():
            with for_(*from_array(dc, dcs)):
                # Wait until it is resumed from python
                pause()
                with for_(n, 0, n < n_avg, n + 1):
                    with for_(*from_array(df, dfs)):
                        # Qubit initialization
                        for i, qubit in multiplexed_qubits.items():
                            # Update the qubit frequency
                            qubit.xy.update_frequency(df + qubit.xy.intermediate_frequency)
                            # Update the resonator frequency
                            qubit.rr.update_frequency(resonator_freq[index] + qubit.rr.intermediate_frequency)
                            # Wait for the qubits to decay to the ground state
                            qubit.reset_qubit_thermal()
                            # Flux sweeping for a qubit
                            duration = (
                                operation_len * u.ns
                                if operation_len is not None
                                else qubit.xy.operations[operation].length * u.ns
                            )
                        align()

                        # Qubit manipulation
                        for i, qubit in multiplexed_qubits.items():
                            # Bring the qubit to the desired point during the saturation pulse
                            qubit.z.play(
                                "const", amplitude_scale=dc / qubit.z.operations["const"].amplitude, duration=duration
                            )
                            # Apply saturation pulse to all qubits
                            qubit.xy.play(
                                operation,
                                amplitude_scale=operation_amp,
                                duration=duration,
                            )
                        align()

                        # Qubit readout
                        for i, qubit in multiplexed_qubits.items():
                            qubit.resonator.measure("readout", qua_vars=(I[i], Q[i]))
                            # save data
                            save(I[i], I_st[i])
                            save(Q[i], Q_st[i])
                # Update the resonator frequency vs flux index
                assign(index, index + 1)
            # Measure sequentially
            if not node.parameters.multiplexed:
                align()

        with stream_processing():
            n_st.save("n")
            for i, qubit in enumerate(qubits):
                I_st[i].buffer(len(dcs)).buffer(len(dfs)).average().save(f"I{i + 1}")
                Q_st[i].buffer(len(dcs)).buffer(len(dfs)).average().save(f"Q{i + 1}")


# %% {Simulate}
@node.run_action(skip_if=node.parameters.load_data_id is not None or not node.parameters.simulate)
def simulate_qua_program(node: QualibrationNode[Parameters, Quam]):
    """Connect to the QOP and simulate the QUA program"""
    # Connect to the QOP
    qmm = node.machine.connect()
    # Get the config from the machine
    config = node.machine.generate_config()
    # Simulate the QUA program, generate the waveform report and plot the simulated samples
    samples, fig, wf_report = simulate_and_plot(qmm, config, node.namespace["qua_program"], node.parameters)
    # Store the figure, waveform report and simulated samples
    node.results["simulation"] = {"figure": fig, "wf_report": wf_report, "samples": samples}


# %% {Execute}
@node.run_action(skip_if=node.parameters.load_data_id is not None or node.parameters.simulate)
def execute_qua_program(node: QualibrationNode[Parameters, Quam]):
    """Connect to the QOP, execute the QUA program and fetch the raw data and store it in a xarray dataset called "ds_raw"."""
    # Connect to the QOP
    qmm = node.machine.connect()
    # Get the config from the machine
    config = node.machine.generate_config()
    # Execute the QUA program only if the quantum machine is available (this is to avoid interrupting running jobs).
    with qm_session(qmm, config, timeout=node.parameters.timeout) as qm:
        # The job is stored in the node namespace to be reused in the fetching_data run_action
        node.namespace["job"] = job = qm.execute(node.namespace["qua_program"])
        # Display the progress bar
        data_fetcher = XarrayDataFetcher(job, node.namespace["sweep_axes"])

        for i, voltage_gate in enumerate(node.namespace["sweep_axes"]["flux_bias"].values):
            # Wait until the program reaches the 'pause' statement
            wait_until_job_is_paused(job)
            # IVCC.volt = voltage_gate # update the voltage gate of the external device
            time.sleep(0.1)
            # Resume the program
            job.resume()
            # # Wait until the program reaches the 'pause' statement again, indicating that the QUA program is done
            # wait_until_job_is_paused(job)

            progress_counter(
                i + 1,
                node.parameters.num_flux_points,
                start_time=data_fetcher.t_start,
            )
        # Display the execution report to expose possible runtime errors
        node.log(job.execution_report())
        for ds in data_fetcher:
            last_ds = ds
            print(ds)
        if last_ds is not None:
            node.results["ds_raw"] = last_ds


# %% {Load_historical_data}
@node.run_action(skip_if=node.parameters.load_data_id is None)
def load_data(node: QualibrationNode[Parameters, Quam]):
    """Load a previously acquired dataset."""
    load_data_id = node.parameters.load_data_id
    # Load the specified dataset
    node.load_from_id(node.parameters.load_data_id)
    node.parameters.load_data_id = load_data_id
    # Get the active qubits from the loaded node parameters
    # node.namespace["qubits"] = get_qubits(node)
    # ds_processed = process_raw_dataset(node.results["ds_raw"], node)
    # ds_processed.IQ_abs.plot()


# %% {Analyse_data}
@node.run_action(skip_if=node.parameters.simulate)
def analyse_data(node: QualibrationNode[Parameters, Quam]):
    """Analyse the raw data and store the fitted data in another xarray dataset "ds_fit" and the fitted results in the "fit_results" dictionary."""
    node.results["ds_raw"] = process_raw_dataset(node.results["ds_raw"], node)
    node.results["ds_fit"], fit_results = fit_raw_data(node.results["ds_raw"], node)
    node.results["fit_results"] = {k: asdict(v) for k, v in fit_results.items()}

    # Log the relevant information extracted from the data analysis
    log_fitted_results(node.results["fit_results"], log_callable=node.log)
    node.outcomes = {
        qubit_name: ("successful" if fit_result["success"] else "failed")
        for qubit_name, fit_result in node.results["fit_results"].items()
    }


# %% {Plot_data}
@node.run_action(skip_if=node.parameters.simulate)
def plot_data(node: QualibrationNode[Parameters, Quam]):
    """Plot the raw and fitted data in specific figures whose shape is given by qubit.grid_location."""
    fig_raw_fit = plot_raw_data_with_fit(node.results["ds_raw"], node.namespace["qubits"], node.results["ds_fit"])
    plt.show()
    # Store the generated figures
    node.results["figures"] = {
        "amplitude": fig_raw_fit,
    }


# %% {Update_state}
@node.run_action(skip_if=node.parameters.simulate)
def update_state(node: QualibrationNode[Parameters, Quam]):
    """Update the relevant parameters if the qubit data analysis was successful."""
    with node.record_state_updates():
        for q in node.namespace["qubits"]:
            if node.outcomes[q.name] == "failed":
                continue
            else:
                fit_results = node.results["fit_results"][q.name]
                q.xy.RF_frequency = fit_results["qubit_frequency"]
                q.f_01 = fit_results["qubit_frequency"]
                # q.freq_vs_flux_01_quad_term = fit_results["quad_term"]


# %% {Save_results}
@node.run_action()
def save_results(node: QualibrationNode[Parameters, Quam]):
    node.save()
