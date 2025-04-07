# %% {Imports}
from dataclasses import asdict
from re import A

import matplotlib.pyplot as plt
import numpy as np
import xarray as xr
from qm.qua import *
from qualang_tools.loops import from_array
from qualang_tools.multi_user import qm_session
from qualang_tools.results import progress_counter
from qualang_tools.units import unit
from qualibrate import QualibrationNode
from qualibrate.utils.logger_m import logger
from qualibration_libs.xarray_data_fetcher import XarrayDataFetcher
from quam_config import QuAM
from quam_experiments.experiments.cz_calibration import (
    Parameters,
    fit_raw_data,
    log_fitted_results,
    process_raw_dataset,
)
from quam_experiments.parameters.qubits_experiment import get_qubits
from quam_experiments.workflow import simulate_and_plot

# %% {Description}
description = """
"""

# Be sure to include [Parameters, QuAM] so the node has proper type hinting
node = QualibrationNode[Parameters, QuAM](
    name="13_cz_calibration",  # Name should be unique
    description=description,  # Describe what the node is doing, which is also reflected in the Qualibrate GUI
    parameters=Parameters(),  # Node parameters defined under quam_experiment/experiments/node_name
)


# Any parameters that should change for debugging purposes only should go in here
# These parameters are ignored when run through the GUI or as part of a graph
@node.run_action(skip_if=node.modes.external)
def custom_param(node: QualibrationNode[Parameters, QuAM]):
    """
    Allow the user to locally set the node parameters for debugging purposes, or
    execution in the Python IDE.
    """
    node.parameters.control_qubit = "q1"
    node.parameters.target_qubit = "q2"
    node.parameters.simulate = True
    node.parameters.cz_min_amplitude_factor = 1.0
    node.parameters.cz_max_amplitude_factor = 2.0
    node.parameters.cz_num_amplitude_factor = 5
    node.parameters.operation = "flattop"
    # You can get type hinting in your IDE by typing node.parameters.
    pass


# Instantiate the QuAM class from the state file
node.machine = QuAM.load()


# %% {Create_QUA_program}
@node.run_action(skip_if=node.parameters.load_data_id is not None)
def create_qua_program(node: QualibrationNode[Parameters, QuAM]):
    """
    Create the sweep axes and generate the QUA program from the pulse sequence and the
    node parameters.
    """
    # Class containing tools to help handle units and conversions.
    u = unit(coerce_to_integer=True)
    # Get the active qubits from the node and organize them by batches
    control = node.machine.qubits[node.parameters.control_qubit]
    target = node.machine.qubits[node.parameters.target_qubit]
    cz_duration = node.parameters.cz_duration
    assert cz_duration >= 40, "cz_duration must be greater than 40ns"
    n_avg = node.parameters.num_averages

    a_min = node.parameters.cz_min_amplitude_factor
    a_max = node.parameters.cz_max_amplitude_factor
    a_num = node.parameters.cz_num_amplitude_factor
    amps = np.linspace(a_min, a_max, a_num)

    tomo_angles = np.linspace(0, 1, node.parameters.num_tomo_angles)

    operation = node.parameters.operation
    # Register the sweep axes to be added to the dataset when fetching data
    node.namespace["sweep_axes"] = {
        "conditional_pi": xr.DataArray([True, False], attrs={"long_name": "conditional pi pulse"}),
        "cz_amplitude": xr.DataArray(amps, attrs={"long_name": "cz amplitude"}),
        "tomo_angles": xr.DataArray(tomo_angles, attrs={"long_name": "tomography angles"}),
    }

    with program() as node.namespace["qua_program"]:
        state_c = declare(fixed)
        state_c_st = declare_stream()
        state_t = declare(fixed)
        state_t_st = declare_stream()
        n = declare(int)
        n_st = declare_stream()
        a = declare(fixed)
        phi = declare(fixed)
        cond_pi = declare(bool)

        for qubit in node.machine.active_qubits:
            node.machine.initialize_qpu(target=qubit)
        align()
        with for_(n, 0, n < n_avg, n + 1):
            save(n, n_st)
            with for_each_(cond_pi, [True, False]):
                with for_(*from_array(a, amps)):
                    with for_(*from_array(phi, tomo_angles)):
                        control.xy.play("x180", condition=cond_pi)
                        target.xy.play("x90")
                        align()
                        control.z.play(pulse_name=operation, amplitude_scale=a)
                        align()
                        control.xy.play("x180", condition=cond_pi)
                        target.xy.frame_rotation_2pi(phi)
                        target.xy.play("x90")
                        target.xy.frame_rotation_2pi(-phi)
                        align()
                        control.readout_state(state_c)
                        target.readout_state(state_t)
                        control.resonator.wait(control.resonator.depletion_time * u.ns)
                        target.resonator.wait(target.resonator.depletion_time * u.ns)
                        # save data
                        save(state_c, state_c_st)
                        save(state_t, state_t_st)

        with stream_processing():
            n_st.save("n")
            state_c_st.buffer(len(tomo_angles)).buffer(len(amps)).buffer(2).average().save("state_c")
            state_t_st.buffer(len(tomo_angles)).buffer(len(amps)).buffer(2).average().save("state_t")


# %% {Simulate}
@node.run_action(skip_if=node.parameters.load_data_id is not None or not node.parameters.simulate)
def simulate_qua_program(node: QualibrationNode[Parameters, QuAM]):
    """Connect to the QOP and simulate the QUA program"""
    # # Connect to the QOP
    # qmm = node.machine.connect()
    # # Get the config from the machine
    # config = node.machine.generate_config()
    # # Simulate the QUA program, generate the waveform report and plot the simulated samples
    # samples, fig, wf_report = simulate_and_plot(qmm, config, node.namespace["qua_program"], node.parameters)
    # # Store the figure, waveform report and simulated samples
    # node.results["simulation"] = {"figure": fig, "wf_report": wf_report.to_dict()}
    import os
    from qm_saas import QmSaas, QoPVersion
    from qm import QuantumMachinesManager, SimulationConfig
    password = os.environ["SAAS_PASSWORD"]
    email = os.environ["QM_EMAIL"]
    dev = os.environ["SAAS_DEV"]

    client = QmSaas(host=dev, email=email, password=password)

    with client.simulator(QoPVersion.v3_2_4) as instance:
        # Use the instance object to simulate QUA programs
        qmm = QuantumMachinesManager(
            host=instance.host, port=instance.port, connection_headers=instance.default_connection_headers
        )
        # Continue as usual with opening a quantum machine and simulation of a qua program
        # Simulates the QUA program for the specified duration
        simulation_config = SimulationConfig(duration=10_000 >> 2)
        # Simulate blocks python until the simulation is done
        job = qmm.simulate(node.machine.generate_config(), node.namespace["qua_program"], simulation_config)
        # Plot the simulated samples
        samples = job.get_simulated_samples()
        waveform_report = job.get_simulated_waveform_report()
        waveform_report.create_plot(samples, plot=True)
        # job.get_simulated_samples().con1.plot()
        # plt.show()


# %% {Execute}
@node.run_action(skip_if=node.parameters.load_data_id is not None or node.parameters.simulate)
def execute_qua_program(node: QualibrationNode[Parameters, QuAM]):
    """
    Connect to the QOP, execute the QUA program and fetch the raw data and store it in
    an xarray dataset called "ds_raw".
    """
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
            # print_progress_bar(job, iteration_variable="n", total_number_of_iterations=node.parameters.num_averages)
            progress_counter(
                data_fetcher["n"],
                node.parameters.num_runs,
                start_time=data_fetcher.t_start,
            )
        # Display the execution report to expose possible runtime errors
        print(job.execution_report())
    # Register the raw dataset
    node.results["ds_raw"] = dataset
    node.results["job_res"] = job.result_handles



# %% {Load_data}
@node.run_action(skip_if=node.parameters.load_data_id is None)
def load_data(node: QualibrationNode[Parameters, QuAM]):
    """Load a previously acquired dataset."""
    load_data_id = node.parameters.load_data_id
    # Load the specified dataset
    node = node.load_from_id(node.parameters.load_data_id)
    node.parameters.load_data_id = load_data_id
    # Get the active qubits from the loaded node parameters
    node.namespace["qubits"] = get_qubits(node)


# %% {Analyse_data}
@node.run_action(skip_if=node.parameters.simulate)
def analyse_data(node: QualibrationNode[Parameters, QuAM]):
    """
    Analyse the raw data and store the fitted data in another xarray dataset "ds_fit"
    and the fitted results in the "fit_results" dictionary.
    """
    node.results["ds_fit"], fit_results = fit_raw_data(node.results["ds_raw"], node)
    node.results["fit_results"] = {k: asdict(v) for k, v in fit_results.items()}

    # Log the relevant information extracted from the data analysis
    log_fitted_results(node.results["fit_results"], logger)
    node.outcomes = {
        qubit_name: ("successful" if fit_result["success"] else "failed")
        for qubit_name, fit_result in node.results["fit_results"].items()
    }


# %% {Plot_data}
@node.run_action(skip_if=node.parameters.simulate)
def plot_data(node: QualibrationNode[Parameters, QuAM]):
    """
    Plot the raw and fitted data in specific figures whose shape is given by
    qubit.grid_location.
    """

