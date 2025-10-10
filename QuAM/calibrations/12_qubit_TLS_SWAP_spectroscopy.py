# %% {Imports}
from dataclasses import asdict

import matplotlib.pyplot as plt
import numpy as np
import xarray as xr
from qm.qua import *
from qualang_tools.loops import from_array
from qualang_tools.multi_user import qm_session
from qualang_tools.results import progress_counter
from qualang_tools.units import unit
from iqcc_calibration_tools.qualibrate_config.qualibrate.node import QualibrationNode
from qualibration_libs.data import XarrayDataFetcher
from iqcc_calibration_tools.quam_config.components.quam_root import Quam
from calibration_utils.qubit_TLS_SWAP_spectroscopy import (
    Parameters,
    fit_raw_data,
    log_fitted_results,
    process_raw_dataset,
    plot_tls_decay_envelopes
)
from calibration_utils.qubit_TLS_SWAP_spectroscopy.plotting import (
    plot_raw_data_with_fit
)
from qualibration_libs.parameters import get_qubits
from qualibration_libs.runtime import simulate_and_plot

# %% {Node initialisation}
description = """
        QUBIT-TLS SWAP SPECTROSCOPY
This program consists of exciting the qubit with an xy pi pulse and then tuning the resonant frequency
with a Z pulse of varying amplitude and duration. Lastly, the qubit population is read out upon the Z
pulse ending. The resulting chevron patterns correspond to vacuum Rabi oscilations between the qubit and
strongly coupled TLSs in its vicinity.

Prerequisites:
    - Having found the resonance frequency of the resonator coupled to the qubit under
      study (resonator_spectroscopy).
    - Having calibrated qubit pi pulse (x180) by running qubit, spectroscopy,
      rabi_chevron, power_rabi and updated the state.
    - (optional) Having calibrated the readout (readout_frequency, amplitude,
      duration_optimization IQ_blobs) for better SNR.
"""


node = QualibrationNode[Parameters, Quam](
    name="12_qubit_TLS_swap_spectroscopy",
    description=description,
    parameters=Parameters(),
)


# Any parameters that should change for debugging purposes only should go in here
# These parameters are ignored when run through the GUI or as part of a graph
@node.run_action(skip_if=node.modes.external)
def custom_param(node: QualibrationNode[Parameters, Quam]):
    # You can get type hinting in your IDE by typing node.parameters.
    node.parameters.qubits = ["qD4"]
    node.parameters.simulate = True
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

    n_avg = node.parameters.num_shots  # The number of averages
    # If True, uses state discrimination rather than demodulated readout signals.
    state_discrimination = node.parameters.use_state_discrimination

    # Z SWAP pulse length sweep (in ns)
    z_duration = np.arange(node.parameters.min_z_duration_in_ns // 4,
                           node.parameters.max_z_duration_in_ns // 4,
                           node.parameters.z_duration_step_in_ns // 4
                        )

    # Z SWAP flux amplitude sweep (in volts)
    fluxes = np.linspace(
        -node.parameters.flux_span / 2 + node.parameters.flux_center,
        node.parameters.flux_span / 2 + node.parameters.flux_center,
        node.parameters.flux_num,
    )
    # Register the sweep axes to be added to the dataset when fetching data
    node.namespace["sweep_axes"] = {
        "qubit": xr.DataArray(qubits.get_names()),
        "flux_bias": xr.DataArray(fluxes, attrs={"long_name": "flux bias", "units": "V"}),
        "z_duration": xr.DataArray(4*z_duration, attrs={"long_name": "flux duration", "units": "ns"}),
    }
    with program() as node.namespace["qua_program"]:
        I, I_st, Q, Q_st, n, n_st = node.machine.declare_qua_variables()
        state = [declare(int) for _ in range(num_qubits)]
        state_st = [declare_stream() for _ in range(num_qubits)]
        t = declare(int)  # QUA variable for the flux pulse duration
        flux = declare(fixed)  # QUA variable for the flux dc level

        for multiplexed_qubits in qubits.batch():
            # Initialize the QPU in terms of flux points (flux tunable transmons and/or tunable couplers)
            for qubit in multiplexed_qubits.values():
                node.machine.initialize_qpu(target=qubit)
            align()

            with for_(n, 0, n < n_avg, n + 1):
                save(n, n_st)
                with for_(*from_array(flux, fluxes)):
                    with for_(*from_array(t, z_duration)):
                        # Qubit manipulation
                        for i, qubit in multiplexed_qubits.items():
                            qubit.reset_qubit_thermal()
                            qubit.xy.play("x180")
                            #qubit.z.wait(duration=qubit.xy.operations["x180"].length) 
                            qubit.align()
                            qubit.z.play("const", amplitude_scale=flux/qubit.z.operations["const"].amplitude, duration=t)
                        align()
                        # Qubit readout
                        for i, qubit in multiplexed_qubits.items():
                            if state_discrimination:
                                qubit.readout_state(state[i])
                                save(state[i], state_st[i])
                                reset_frame(qubit.xy.name)

                            else:
                                qubit.resonator.measure("readout", qua_vars=(I[i], Q[i]))
                                save(I[i], I_st[i])
                                save(Q[i], Q_st[i])
                                reset_frame(qubit.xy.name)


        with stream_processing():
            n_st.save("n")
            for i in range(num_qubits):
                if node.parameters.use_state_discrimination:
                    state_st[i].buffer(len(z_duration)).buffer(len(fluxes)).average().save(f"state{i + 1}")
                else:
                    I_st[i].buffer(len(z_duration)).buffer(len(fluxes)).average().save(f"I{i + 1}")
                    Q_st[i].buffer(len(z_duration)).buffer(len(fluxes)).average().save(f"Q{i + 1}")



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
        for dataset in data_fetcher:
            progress_counter(
                data_fetcher["n"],
                node.parameters.num_shots,
                start_time=data_fetcher.t_start,
            )
        # Display the execution report to expose possible runtime errors
        node.log(job.execution_report())
    # Register the raw dataset
    node.results["ds_raw"] = data_fetcher.dataset


# %% {Load_historical_data}
@node.run_action(skip_if=node.parameters.load_data_id is None)
def load_data(node: QualibrationNode[Parameters, Quam]):
    """Load a previously acquired dataset."""
    load_data_id = node.parameters.load_data_id
    # Load the specified dataset
    node.load_from_id(node.parameters.load_data_id)
    node.parameters.load_data_id = load_data_id
    # Get the active qubits from the loaded node parameters
    node.namespace["qubits"] = get_qubits(node)


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
    fig1 = plot_raw_data_with_fit(node.results["ds_raw"], node.namespace["qubits"], node.results["ds_fit"])
    fig2 = plot_tls_decay_envelopes(node.results["ds_raw"],
                                    node.namespace["qubits"],
                                    node.results["ds_fit"])
    plt.show()
    node.results["figures"] = {"raw_data": fig1, "tls_envelopes": fig2}


# %% {Update_state}
@node.run_action(skip_if=node.parameters.simulate)
def update_state(node: QualibrationNode[Parameters, Quam]):
    """Update the relevant parameters if the qubit data analysis was successful."""
    with node.record_state_updates():
        for q in node.namespace["qubits"]:
            if node.outcomes[q.name] == "failed":
                continue



# %% {Save_results}
@node.run_action()
def save_results(node: QualibrationNode[Parameters, Quam]):
    node.save()
