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
from quam_libs.lib.save_utils import fetch_results_as_xarray, load_dataset, get_node_id
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
    reset_type: Literal["thermal", "heralding", "active"] = "heralding"
    state_discrimination: bool = True
    update_x90: bool = True
    simulate: bool = False
    simulation_duration_ns: int = 2500
    timeout: int = 100
    load_data_id: Optional[int] = None
    multiplexed: bool = True


node = QualibrationNode(name="11_CZ_Amplitude_Cal", parameters=Parameters())
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
reset_type = node.parameters.reset_type  # "thermal", "heralding" or "active"
state_discrimination = node.parameters.state_discrimination
operation = node.parameters.operation_x180_or_any_90  # The qubit operation to play
# Pulse amplitude sweep (as a pre-factor of the qubit pulse amplitude) - must be within [-2; 2)
amps = np.arange(
    node.parameters.min_amp_factor,
    node.parameters.max_amp_factor,
    node.parameters.amp_factor_step,
)
# make sure that if using heralded readout then also using state discrimination
if reset_type == "heralding" and not state_discrimination:
    raise AssertionError("Heralded readout is only supported with state discrimination.")

# Number of applied Rabi pulses sweep
if N_pi > 1:
    if operation == "x180_Cosine":
        N_pi_vec = np.arange(1, N_pi, 2).astype("int")
    elif operation in ["x90_Cosine", "-x90_Cosine", "y90_Cosine", "-y00_Cosine"]:
        N_pi_vec = np.arange(2, N_pi, 4).astype("int")
    else:
        raise ValueError(f"Unrecognized operation {operation}.")
else:
    N_pi_vec = np.linspace(1, N_pi, N_pi).astype("int")[::2]

q1 = machine.rf_qubits['q1']
q2 = machine.rf_qubits['q2']
c12 = machine.qubits['c12']
with program() as CZ_amp_cal:
    I, I_st, Q, Q_st, n, n_st = qua_declaration(num_qubits=num_qubits)
    if state_discrimination:
        state = [declare(int) for _ in range(num_qubits)]
        state_stream = [declare_stream() for _ in range(num_qubits)]
    if reset_type == "heralding":
        init_state = [declare(int) for _ in range(num_qubits)]
        final_state = [declare(int) for _ in range(num_qubits)]
        res_state = declare_stream()
    a = declare(fixed)  # QUA variable for the qubit drive amplitude pre-factor
    npi = declare(int)  # QUA variable for the number of qubit pulses
    count = declare(int)  # QUA variable for counting the qubit pulses

    for i, qubit in enumerate(qubits):
        # Bring the active qubits to the minimum frequency point
        machine.set_all_fluxes(flux_point=flux_point, target=qubit)

    with for_(n, 0, n < n_avg, n + 1):
        save(n, n_st)
        with for_(*from_array(a, amps)):
            # Initialize the qubits
            if reset_type == "active":
                active_reset(q1, "readout")
                active_reset(q2, "readout")
            elif reset_type == "heralding":
                wait(40 * u.us)
                q1.resonator.measure("readout", qua_vars=(I[0], Q[0]))
                q2.resonator.measure("readout", qua_vars=(I[1], Q[1]))
                assign(init_state[0], Cast.to_int(I[0] > q1.resonator.operations["readout"].threshold))
                assign(init_state[1], Cast.to_int(I[1] > q2.resonator.operations["readout"].threshold))
                wait(4 * u.us)
            else:
                wait(10000 * u.ns)

            align()
            # Loop for error amplification (perform many qubit pulses)
            play("x90_Cosine", q1.I.name)
            play("x90_Cosine", q1.I.name)
            play("x90_Cosine", q2.I.name)
            play("x90_Cosine", q2.I.name)

            align()

            play("x180"*amp(a), c12.xy.name)

            align()

            play("x90_Cosine", q1.I.name)
            play("x90_Cosine", q1.I.name)
            play("x90_Cosine", q2.I.name)
            play("x90_Cosine", q2.I.name)

            align()

            q1.resonator.measure("readout", qua_vars=(I[0], Q[0]))
            q2.resonator.measure("readout", qua_vars=(I[1], Q[1]))

            if reset_type == "heralding":
                assign(state[0], Cast.to_int(I[0] > q1.resonator.operations["readout"].threshold))
                assign(state[1], Cast.to_int(I[1] > q1.resonator.operations["readout"].threshold))
                assign(final_state[0], init_state[0] ^ state[0])
                assign(final_state[1], init_state[1] ^ state[1])
                with if_(final_state[0] + final_state[1] > 0):
                    save(1, res_state)
                with else_():
                    save(0, res_state)

            elif state_discrimination:
                assign(state[0], Cast.to_int(I[0] > q1.resonator.operations["readout"].threshold))
                assign(state[1], Cast.to_int(I[1] > q1.resonator.operations["readout"].threshold))
                save(state[0], state_stream[0])
                save(state[1], state_stream[1])
            else:
                save(I[0], I_st[0])
                save(Q[0], Q_st[0])
                save(I[1], I_st[1])
                save(Q[1], Q_st[1])

    with stream_processing():
        n_st.save("n")
        res_state.buffer(len(amps)).buffer(np.ceil(N_pi / 2)).average().save("state1")
        res_state.buffer(len(amps)).buffer(np.ceil(N_pi / 2)).average().save("state2")


# %% {Simulate_or_execute}
if node.parameters.simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=node.parameters.simulation_duration_ns * 4)  # In clock cycles = 4ns
    job = qmm.simulate(config, CZ_amp_cal, simulation_config)
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
    job = qm.execute(CZ_amp_cal)
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
        ds = fetch_results_as_xarray(job.result_handles, qubits, {"amp": amps, "N": N_pi_vec})
        if not state_discrimination:
            ds = convert_IQ_to_V(ds, qubits)
        # Add the qubit pulse absolute amplitude to the dataset
        ds = ds.assign_coords(
            {
                "abs_amp": (
                    ["qubit", "amp"],
                    np.array([c12.xy.operations["x180"].amplitude * amps for q in qubits]),
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
    if N_pi == 1:
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
            new_pi_amp = c12.xy.operations["x180"].amplitude * factor
            fit_results[q.name]["CZ_amplitude"] = new_pi_amp
            # limits = instrument_limits(q.I)
            # if new_pi_amp < limits.max_x180_wf_amplitude:
            #     print(f"amplitude for Pi pulse is modified by a factor of {factor:.2f}")
            #     print(f"new amplitude is {1e3 * new_pi_amp:.2f} {limits.units} \n")
            #     fit_results[q.name]["Pi_amplitude"] = new_pi_amp
            # else:
            #     print(f"Fitted amplitude too high, new amplitude is {limits.max_x180_wf_amplitude} \n")
            #     fit_results[q.name]["Pi_amplitude"] = limits.max_x180_wf_amplitude
        node.results["fit_results"] = fit_results

    elif N_pi > 1:
        # Get the average along the number of pulses axis to identify the best pulse amplitude
        if state_discrimination:
            I_n = ds.state.mean(dim="N")
        else:
            I_n = ds.I.mean(dim="N")
        if (N_pi_vec[0] % 2 == 0 and operation == "x180") or (N_pi_vec[0] % 2 != 0 and operation != "x180"):
            data_max_idx = I_n.argmin(dim="amp")
        else:
            data_max_idx = I_n.argmax(dim="amp")

        # Save fitting results
        for q in qubits:
            new_pi_amp = float(ds.abs_amp.sel(qubit=q.name)[data_max_idx.sel(qubit=q.name)].data)
            fit_results[q.name] = {}
            fit_results[q.name]["CZ_amplitude"] = new_pi_amp


    # %% {Plotting}
    grid = QubitGrid(ds, [q.grid_location for q in qubits])
    for ax, qubit in grid_iter(grid):
        if N_pi == 1:
            if state_discrimination:
                ds.assign_coords(amp_mV=ds.abs_amp * 1e3).loc[qubit].state.plot(ax=ax, x="amp_mV")
                ax.plot(ds.abs_amp.loc[qubit] * 1e3, fit_evals.loc[qubit][0])
                ax.set_ylabel("Qubit state")
            else:
                (ds.assign_coords(amp_mV=ds.abs_amp * 1e3).loc[qubit].I * 1e3).plot(ax=ax, x="amp_mV")
                ax.plot(ds.abs_amp.loc[qubit] * 1e3, 1e3 * fit_evals.loc[qubit][0])
                ax.set_ylabel("Trans. amp. I [mV]")

        elif N_pi > 1:
            if state_discrimination:
                ds.assign_coords(amp_mV=ds.abs_amp * 1e3).loc[qubit].state.plot(ax=ax, x="amp_mV", y="N")
            else:
                (ds.assign_coords(amp_mV=ds.abs_amp * 1e3).loc[qubit].I * 1e3).plot(ax=ax, x="amp_mV", y="N")
            ax.set_ylabel("num. of pulses")
            ax.axvline(1e3 * ds.abs_amp.loc[qubit][data_max_idx.loc[qubit]], color="r")
        ax.set_xlabel("Amplitude [mV]")
        ax.set_title(qubit["qubit"])
    grid.fig.suptitle(
        f"Rabi : I vs. amplitude \n {date_time} #{node_id} \n multiplexed = {node.parameters.multiplexed} reset Type = {node.parameters.reset_type}")
    plt.tight_layout()
    plt.show()
    node.results["figure"] = grid.fig

    # %% {Update_state}
    if node.parameters.load_data_id is None:
        with node.record_state_updates():
            for q in qubits:
                c12.xy.operations['x180'].amplitude = fit_results[q.name]["CZ_amplitude"]
            # for q in qubits:
            #     q.I.operations[operation].amplitude = fit_results[q.name]["Pi_amplitude"]
            #     if operation == "x180_Cosine" and node.parameters.update_x90:
            #         q.I.operations["x90_Cosine"].amplitude = fit_results[q.name]["Pi_amplitude"] / 2
            #         q.Q.operations["x90_Cosine"].amplitude = fit_results[q.name]["Pi_amplitude"] / 2

        # %% {Save_results}
        node.outcomes = {q.name: "successful" for q in qubits}
        node.results["initial_parameters"] = node.parameters.model_dump()
        node.machine = machine
        node.save()
    #
