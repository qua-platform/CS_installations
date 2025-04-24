"""
        POWER RABI WITH ERROR AMPLIFICATION
This sequence involves repeatedly executing the qubit pulse (such as x180) 'N' times and
measuring the state of the resonator across different qubit pulse amplitudes and number of pulses.
By doing so, the effect of amplitude inaccuracies is amplified, enabling a more precise measurement of the pi pulse
amplitude. The results are then analyzed to determine the qubit pulse amplitude suitable for the selected duration.

Prerequisites:
    - Having found the resonance frequency of the resonator coupled to the qubit under study (resonator_spectroscopy).
    - Having calibrated the IQ mixer connected to the qubit drive line (external mixer or Octave port)
    - Having found the rough qubit frequency and set the desired pi pulse duration (qubit spectroscopy).
    - Set the desired flux bias

Next steps before going to the next node:
    - Update the qubit pulse amplitude in the state.
    - Save the current state
"""

# %% {Imports}
from datetime import datetime
from qualibrate import QualibrationNode, NodeParameters
from quam_libs.components import QuAM
from quam_libs.macros import qua_declaration, active_reset
from quam_libs.lib.instrument_limits import instrument_limits
from quam_libs.lib.qua_datasets import convert_IQ_to_V
from quam_libs.lib.plot_utils import QubitGrid, grid_iter
from quam_libs.lib.save_utils import fetch_results_as_xarray, load_dataset, get_node_id, fetch_results_as_xarray_for_heralding
from quam_libs.lib.fit import fit_oscillation, oscillation
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
    qubits: Optional[List[str]] = None
    num_averages: int = 10
    operation_x180_or_any_90: Literal["x180_Cosine", "x90_Cosine"] = "x180_Cosine"
    min_amp_factor: float = 0.0
    max_amp_factor: float = 1.5
    amp_factor_step: float = 0.05
    max_number_rabi_pulses_per_sweep: int = 1
    flux_point_joint_or_independent: Literal["joint", "independent"] = "joint"
    reset_type_thermal_heralding_or_active: Literal["thermal", "active", "heralding"] = "heralding"
    state_discrimination: bool = True
    update_x90: bool = True
    simulate: bool = False
    simulation_duration_ns: int = 2500
    timeout: int = 100
    load_data_id: Optional[int] = None
    multiplexed: bool = True


node = QualibrationNode(name="04_Power_Rabi", parameters=Parameters())
node_id = get_node_id()

# %% {Initialize_QuAM_and_QOP}
# Class containing tools to help handling units and conversions.
u = unit(coerce_to_integer=True)
# Instantiate the QuAM class from the state file
path = r"C:\Git\CS_installations\qualibrate\configuration\quam_state"
machine = QuAM.load(path)
# Generate the OPX and Octave configurations
config = machine.generate_config()
# Open Communication with the QOP
if node.parameters.load_data_id is None:
    qmm = machine.connect()

# Get the relevant QuAM components
if node.parameters.qubits is None or node.parameters.qubits == "":
    qubits = machine.active_qubits
else:
    qubits = [machine.qubits[q] for q in node.parameters.qubits]
num_qubits = len(qubits)

# %% {QUA_program}
n_avg = node.parameters.num_averages  # The number of averages
N_pi = node.parameters.max_number_rabi_pulses_per_sweep  # Number of applied Rabi pulses sweep
flux_point = node.parameters.flux_point_joint_or_independent  # 'independent' or 'joint'
reset_type = node.parameters.reset_type_thermal_heralding_or_active  # "thermal", "heralding" or "active"
state_discrimination = node.parameters.state_discrimination
operation = node.parameters.operation_x180_or_any_90  # The qubit operation to play
# Pulse amplitude sweep (as a pre-factor of the qubit pulse amplitude) - must be within [-2; 2)
amps = np.arange(
    node.parameters.min_amp_factor,
    node.parameters.max_amp_factor,
    node.parameters.amp_factor_step,
)

# Number of applied Rabi pulses sweep
if N_pi > 1:
    if operation == "x180_Cosine":
        N_pi_vec = np.arange(1, N_pi, 2).astype("int")
    elif operation in ["x90_Cosine", "-x90_Cosine", "y90_Cosine", "-y90_Cosine"]:
        N_pi_vec = np.arange(2, N_pi, 4).astype("int")
    else:
        raise ValueError(f"Unrecognized operation {operation}.")
else:
    N_pi_vec = np.linspace(1, N_pi, N_pi).astype("int")[::2]

with program() as power_rabi:
    I, I_st, Q, Q_st, n, n_st = qua_declaration(num_qubits=num_qubits)
    if state_discrimination:
        state = [declare(bool) for _ in range(num_qubits)]
        state_stream = [declare_stream() for _ in range(num_qubits)]
    a = declare(fixed)  # QUA variable for the qubit drive amplitude pre-factor
    npi = declare(int)  # QUA variable for the number of qubit pulses
    count = declare(int)  # QUA variable for counting the qubit pulses
    state_integer = [declare(int) for _ in range(len(qubits))]
    init_state = [declare(int) for _ in range(len(qubits))]

    for i, qubit in enumerate(qubits):
        # Bring the active qubits to the minimum frequency point
        machine.set_all_fluxes(flux_point=flux_point, target=qubit)

        with for_(n, 0, n < n_avg, n + 1):
            save(n, n_st)
            # Initialize the qubits
            qubit.wait(qubit.resonator_depopulation_time * u.ns)

            qubit.xy_play(operation, amplitude_scale=amps[0])

            qubit.align()
            qubit.resonator.measure("readout", qua_vars=(I[i], Q[i]))
            assign(state[i], I[i] > qubit.resonator.operations["readout"].threshold)
            assign(init_state[i], Cast.to_int(state[i]))
            # save(init_state[i], "start")


            with for_(*from_array(a, amps[1:])):
                # Initialize the qubits
                qubit.wait(qubit.resonator_depopulation_time * u.ns)

                # Loop for error amplification (perform many qubit pulses)

                qubit.xy_play(operation, amplitude_scale=a)
                qubit.align()
                qubit.resonator.measure("readout", qua_vars=(I[i], Q[i]))

                assign(state[i], I[i] > qubit.resonator.operations["readout"].threshold)
                assign(state_integer[i], Cast.to_int(state[i]))
                # save(state_integer[i], "data")
                # save(init_state[i], "data_init")
                with if_(init_state[i] < 0.5):
                    assign(init_state[i], state_integer[i])
                    save(state_integer[i], state_stream[i])
                with else_():
                    assign(init_state[i], state_integer[i])
                    assign(state_integer[i], -1)
                    save(state_integer[i], state_stream[i])



        if not node.parameters.multiplexed:
            align()

    with stream_processing():
        n_st.save("n")
        for i, qubit in enumerate(qubits):
            if operation == "x180_Cosine":
                    state_stream[i].buffer(len(amps)).average().save(
                        f"state{i + 1}"
                    )

            elif operation in ["x90_Cosine", "-x90_Cosine"]:
                state_stream[i].boolean_to_int().buffer(len(amps)).average().save(
                    f"state{i + 1}"
                )
            else:
                raise ValueError(f"Unrecognized operation {operation}.")

# %% {Simulate_or_execute}
if node.parameters.simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=node.parameters.simulation_duration_ns * 4)  # In clock cycles = 4ns
    job = qmm.simulate(config, power_rabi, simulation_config)
    # Get the simulated samples and plot them for all controllers
    samples = job.get_simulated_samples()
    fig, ax = plt.subplots(nrows=len(samples.keys()), sharex=True)
    for i, con in enumerate(samples.keys()):
        plt.subplot(len(samples.keys()), 1, i + 1)
        samples[con].plot()
        plt.title(con)
    plt.tight_layout()
    # Save the figure
    node.results = {"figure": plt.gcf()}
    node.machine = machine
    node.save()

elif node.parameters.load_data_id is None:
    date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # with qm_session(qmm, config, timeout=node.parameters.timeout) as qm:
    qm = qmm.open_qm(config)
    job = qm.execute(power_rabi)
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
        if state_discrimination:
            ds = fetch_results_as_xarray(job.result_handles, qubits, {"amp": amps})
        else:
            ds = fetch_results_as_xarray(job.result_handles, qubits, {"amp": amps})
        if not state_discrimination:
            ds = convert_IQ_to_V(ds, qubits)

        # Add the qubit pulse absolute amplitude to the dataset
        ds = ds.assign_coords(
            {
                "abs_amp": (
                    ["qubit", "amp"],
                    np.array([q.I.operations[operation].amplitude * amps for q in qubits]),
                )
            }
        )
    else:
        node = node.load_from_id(node.parameters.load_data_id)
        ds = node.results["ds"]
    # Add the dataset to the node
    node.results = {"ds": ds}

    # %% {Data_analysis}
    fit_results = {}

    # Fit the power Rabi oscillations
    if state_discrimination:
        fit = fit_oscillation(ds.state, "amp")
    else:
        fit = fit_oscillation(ds.I, "amp")
    fit_evals = oscillation(
        ds.amp,
        fit.sel(fit_vals="a"),
        fit.sel(fit_vals="f"),
        fit.sel(fit_vals="phi"),
        fit.sel(fit_vals="offset"),
    )

    # Save fitting results
    for q in qubits:
        fit_results[q.name] = {}
        f_fit = fit.loc[q.name].sel(fit_vals="f")
        phi_fit = fit.loc[q.name].sel(fit_vals="phi")
        phi_fit = phi_fit - np.pi * (phi_fit > np.pi / 2)
        factor = float(1.0 * (np.pi - phi_fit) / (2 * np.pi * f_fit))
        new_pi_amp = q.I.operations[operation].amplitude * factor
        limits = instrument_limits(q.I)
        if new_pi_amp < limits.max_x180_wf_amplitude:
            print(f"amplitude for Pi pulse is modified by a factor of {factor:.2f}")
            print(f"new amplitude is {1e3 * new_pi_amp:.2f} {limits.units} \n")
            fit_results[q.name]["Pi_amplitude"] = new_pi_amp
        else:
            print(f"Fitted amplitude too high, new amplitude is {limits.max_x180_wf_amplitude} \n")
            fit_results[q.name]["Pi_amplitude"] = limits.max_x180_wf_amplitude
    node.results["fit_results"] = fit_results


    # %% {Plotting}
    grid = QubitGrid(ds, [q.grid_location for q in qubits])
    for ax, qubit in grid_iter(grid):
        if state_discrimination:
            ds.assign_coords(amp_mV=ds.abs_amp * 1e3).loc[qubit].state.plot(ax=ax, x="amp_mV")
            ax.plot(ds.abs_amp.loc[qubit] * 1e3, fit_evals.loc[qubit])
            ax.set_ylabel("Qubit state")
        else:
            (ds.assign_coords(amp_mV=ds.abs_amp * 1e3).loc[qubit].I * 1e3).plot(ax=ax, x="amp_mV")
            ax.plot(ds.abs_amp.loc[qubit] * 1e3, 1e3 * fit_evals.loc[qubit])
            ax.set_ylabel("Trans. amp. I [mV]")
        ax.set_xlabel("Amplitude [mV]")
        ax.set_title(qubit["qubit"])
    grid.fig.suptitle(
        f"Rabi : I vs. amplitude \n {date_time} #{node_id} \n multiplexed = {node.parameters.multiplexed} reset Type = {node.parameters.reset_type_thermal_heralding_or_active}")
    plt.tight_layout()
    plt.show()
    node.results["figure"] = grid.fig

    # %% {Update_state}
    if node.parameters.load_data_id is None:
        with node.record_state_updates():
            for q in qubits:
                q.I.operations[operation].amplitude = fit_results[q.name]["Pi_amplitude"]
                if operation == "x180_Cosine" and node.parameters.update_x90:
                    q.I.operations["x90_Cosine"].amplitude = fit_results[q.name]["Pi_amplitude"] / 2
                    q.Q.operations["x90_Cosine"].amplitude = fit_results[q.name]["Pi_amplitude"] / 2

        # %% {Save_results}
        node.outcomes = {q.name: "successful" for q in qubits}
        node.results["initial_parameters"] = node.parameters.model_dump()
        node.machine = machine
        node.save()

# %%
debug = True
if debug:
    from qm import generate_qua_script

    sourceFile = open('debug_power_rabi.py', 'w')
    print(generate_qua_script(power_rabi, config), file=sourceFile)
    sourceFile.close()