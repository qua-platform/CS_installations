# %% {Imports}
import matplotlib.pyplot as plt
import numpy as np
import xarray as xr
from dataclasses import asdict

from qm.qua import *

from qualang_tools.loops import from_array
from qualang_tools.multi_user import qm_session
from qualang_tools.results import progress_counter
from qualang_tools.units import unit

from qualibrate import QualibrationNode
from quam_config import Quam
from calibration_utils.rabi_chevron import (
    Parameters,
    process_raw_dataset,
    fit_raw_data,
    log_fitted_results,
    plot_raw_data_with_fit,
)
from qualibration_libs.parameters import get_qubits
from qualibration_libs.runtime import simulate_and_plot
from qualibration_libs.data import XarrayDataFetcher
from qualibration_libs.core import tracked_updates


# %% {Description}
description =  """
        Cross-Resonance Time Rabi
The sequence consists two consecutive pulse sequences with the qubit's thermal decay in between.
In the first sequence, we set the control qubit in |g> and play a rectangular cross-resonance pulse to
the target qubit; the cross-resonance pulse has a variable duration. In the second sequence, we initialize the control
qubit in |e> and play the variable duration cross-resonance pulse to the target qubit. Note that in
the second sequence after the cross-resonance pulse we send a x180_c pulse. With it, the target qubit starts
in |g> in both sequences when CR lenght -> zero.

Prerequisites:
    - Having found the resonance frequency of the resonator coupled to the qubit under study (resonator_spectroscopy).
    - Having calibrated qubit pi pulse (x180) by running qubit, spectroscopy, rabi_chevron, power_rabi and updated the config.
    - (optional) Having calibrated the readout (readout_frequency, amplitude, duration_optimization IQ_blobs) for better SNR.

Reference: A. D. Corcoles et al., Phys. Rev. A 87, 030301 (2013)

"""


# Be sure to include [Parameters, Quam] so the node has proper type hinting
node = QualibrationNode[Parameters, Quam](
    name="30a_CR_time_rabi_1q_QST",  # Name should be unique
    description=description,  # Describe what the node is doing, which is also reflected in the QUAlibrate GUI
    parameters=Parameters(),  # Node parameters defined under quam_experiment/experiments/node_name
)


# Any parameters that should change for debugging purposes only should go in here
# These parameters are ignored when run through the GUI or as part of a graph
@node.run_action(skip_if=node.modes.external)
def custom_param(node: QualibrationNode[Parameters, Quam]):
    """Allow the user to locally set the node parameters for debugging purposes, or execution in the Python IDE."""
    # You can get type hinting in your IDE by typing node.parameters.
    # node.parameters.qubits = ["q1", "q2"]
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
    node.namespace["qubit_pairs"] = qubit_pairs = get_qubits(node)
    num_qubit_pairs = len(qubit_pairs)

    # Update the readout power to match the desired range, this change will be reverted at the end of the node.
    node.namespace["tracked_qubits"] = []
    for q in qubits:
        with tracked_updates(q, auto_revert=False) as q:
            q.xy.operations["x180"].length = 16
        node.namespace["tracked_qubits"].append(q)

    n_avg = node.parameters.num_shots  # The number of averages
    state_discrimination = node.parameters.use_state_discrimination
    # Pulse amplitude sweep (as a pre-factor of the qubit pulse amplitude) - must be within [-2; 2)
    pulse_durations = np.arange(
        node.parameters.min_wait_time_in_ns,
        node.parameters.max_wait_time_in_ns,
        node.parameters.time_step_in_ns,
    )
    qst_basis = np.array([0, 1, 2])
    control_state = np.array([0, 1])

    # Register the sweep axes to be added to the dataset when fetching data
    node.namespace["sweep_axes"] = {
        "qubit": xr.DataArray(qubits.get_names()),
        "qst_basis": xr.DataArray(qst_basis, attrs={"long_name": "qst basis"}),
        "control_state": xr.DataArray(control_state, attrs={"long_name": "control state"}),
        "pulse_duration": xr.DataArray(pulse_durations, attrs={"long_name": "qubit pulse duration", "units": "ns"}),
    }

    with program() as node.namespace["qua_program"]:
        n = declare(int)
        n_st = declare_stream()
        I, I_st, Q, Q_st, n, n_st = node.machine.declare_qua_variables()
        if state_discrimination:
            state_control = [declare(int) for _ in range(num_qubit_pairs)]
            state_target = [declare(int) for _ in range(num_qubit_pairs)]
            state_st_control = [declare_stream() for _ in range(num_qubit_pairs)]
            state_st_target = [declare_stream() for _ in range(num_qubit_pairs)]
        t = declare(int)
        s = declare(int)  # QUA variable for the control state
        c = declare(int)  # QUA variable for the projection index in QST

        for multiplexed_qubits in qubits.batch():
            # Initialize the QPU in terms of flux points (flux tunable transmons and/or tunable couplers)
            for qubit in multiplexed_qubits.values():
                node.machine.initialize_qpu(target=qubit)
            align()

            qc = qp.qubit_control
            qt = qp.qubit_target
            cr = qp.cross_resonance

            with for_(n, 0, n < n_avg, n + 1):
                save(n, n_st)

                with for_(*from_array(t, pulse_durations)):
                    with for_(c, 0, c < 3, c + 1):  # bases
                        with for_(s, 0, s < 2, s + 1):  # states
                            with if_(s == 1):
                                qc.xy.play("x180")
                                align(qc.xy.name, qt.xy.name, cr.name)

                            if node.parameters.cr_type == "direct":
                                # phase shift for cr drive
                                cr.frame_rotation_2pi(node.parameters.cr_drive_phase[i])
                                align(qc.xy.name, cr.name)
                                cr.play("square", amplitude_scale=node.parameters.cr_drive_amp_scaling[i])
                                align(qc.xy.name, cr.name)
                                reset_frame(cr.name)

                            elif node.parameters.cr_type == "direct+echo":
                                # phase shift for cr drive
                                cr.frame_rotation_2pi(node.parameters.cr_drive_phase[i])
                                qt.xy.frame_rotation_2pi(node.parameters.cr_cancel_phase[i])
                                # direct + cancel
                                align(qc.xy.name, cr.name)
                                cr.play("square", amplitude_scale=node.parameters.cr_drive_amp_scaling[i])
                                # pi pulse on control
                                align(qc.xy.name, cr.name)
                                qc.xy.play("x180")
                                # echoed direct + cancel
                                align(qc.xy.name, cr.name)
                                cr.play("square", amplitude_scale=-node.parameters.cr_drive_amp_scaling[i])
                                # pi pulse on control
                                align(qc.xy.name, cr.name)
                                qc.xy.play("x180")
                                # align for the next step and clear the phase shift
                                align(qc.xy.name, qt.xy.name)
                                reset_frame(cr.name)
                                reset_frame(qt.xy.name)

                            elif node.parameters.cr_type == "direct+cancel":
                                # phase shift for cr drive
                                cr.frame_rotation_2pi(node.parameters.cr_drive_phase[i])
                                qt.xy.frame_rotation_2pi(node.parameters.cr_cancel_phase[i])
                                # direct + cancel
                                align(qc.xy.name, qt.xy.name, cr.name)
                                cr.play("square", amplitude_scale=node.parameters.cr_drive_amp_scaling[i])
                                qt.xy.play(f"{cr.name}_Square", amplitude_scale=node.parameters.cr_cancel_amp_scaling[i])
                                # align for the next step and clear the phase shift
                                align(qt.xy.name, cr.name)
                                reset_frame(cr.name)
                                reset_frame(qt.xy.name)

                            elif node.parameters.cr_type == "direct+cancel+echo":
                                # phase shift for cr drive
                                cr.frame_rotation_2pi(node.parameters.cr_drive_phase[i])
                                qt.xy.frame_rotation_2pi(node.parameters.cr_cancel_phase[i])
                                # direct + cancel
                                align(qc.xy.name, qt.xy.name, cr.name)
                                cr.play("square", amplitude_scale=node.parameters.cr_drive_amp_scaling[i])
                                qt.xy.play(f"{cr.name}_Square", amplitude_scale=node.parameters.cr_cancel_amp_scaling[i])
                                # pi pulse on control
                                align(qc.xy.name, qt.xy.name, cr.name)
                                qc.xy.play("x180")
                                # echoed direct + cancel
                                align(qc.xy.name, qt.xy.name, cr.name)
                                cr.play("square", amplitude_scale=-node.parameters.cr_drive_amp_scaling[i])
                                qt.xy.play(f"{cr.name}_Square", amplitude_scale=-node.parameters.cr_cancel_amp_scaling[i])
                                # pi pulse on control
                                align(qc.xy.name, qt.xy.name, cr.name)
                                qc.xy.play("x180")
                                # align for the next step and clear the phase shift
                                align(qc.xy.name, qt.xy.name)
                                reset_frame(cr.name)
                                reset_frame(qt.xy.name)

                            align()

                            # QST on Target
                            align(qt.xy.name, cr.name)
                            with switch_(c):
                                with case_(0):  # projection along X
                                    qt.xy.play("-y90")
                                with case_(1):  # projection along Y
                                    qt.xy.play("x90")
                                with case_(2):  # projection along Z
                                    qt.xy.wait(qt.xy.operations["x180"].length * u.ns)

                            align(qt.xy.name, qc.resonator.name, qt.resonator.name)
                            reset_frame(qt.xy.name)

                            # Measure the state of the resonators
                            for i, qubit in multiplexed_qubits.items():
                                if node.parameters.use_state_discrimination:
                                    qubit.readout_state(state[i])
                                    save(state[i], state_st[i])
                                else:
                                    qubit.resonator.measure("readout", qua_vars=(I[i], Q[i]))
                                    # save data
                                    save(I[i], I_st[i])
                                    save(Q[i], Q_st[i])

                            # # Measure the state of the resonators
                            # readout_state(qc, state_control[i])
                            # readout_state(qt, state_target[i])
                            # save(state_control[i], state_st_control[i])
                            # save(state_target[i], state_st_target[i])

                            # Wait for the qubit to decay to the ground state - Can be replaced by active reset
                            wait(machine.thermalization_time * u.ns)

        with stream_processing():
            n_st.save("n")
            for i in range(num_qubits):
                if node.parameters.use_state_discrimination:
                    state_st[i].buffer(len(pulse_durations)).buffer(len(dfs)).average().save(f"state{i + 1}")
                else:
                    I_st[i].buffer(len(pulse_durations)).buffer(len(dfs)).average().save(f"I{i + 1}")
                    Q_st[i].buffer(len(pulse_durations)).buffer(len(dfs)).average().save(f"Q{i + 1}")


        with stream_processing():
            n_st.save("n")
            for i in range(num_qubit_pairs):
                state_st_control[i].buffer(2).buffer(3).buffer(len(idle_time_cycles)).average().save(f"state_control{i + 1}")
                state_st_target[i].buffer(2).buffer(3).buffer(len(idle_time_cycles)).average().save(f"state_target{i + 1}")



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
    node.results["ds_raw"] = dataset


# %% {Load_data}
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

    # Revert the change done at the beginning of the node
    for tracked_qubit in node.namespace.get("tracked_qubits", []):
        tracked_qubit.revert_changes()

    with node.record_state_updates():
        for q in node.namespace["qubits"]:
            if node.outcomes[q.name] == "failed":
                continue


# %% {Save_results}
@node.run_action()
def save_results(node: QualibrationNode[Parameters, Quam]):
    node.save()
