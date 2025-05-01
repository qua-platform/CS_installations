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
from datetime import datetime
from qualibrate import QualibrationNode, NodeParameters

from quam_libs.components import QuAM
from quam_libs.lib.instrument_limits import instrument_limits
from quam_libs.macros import qua_declaration, active_reset
from quam_libs.lib.qua_datasets import convert_IQ_to_V
from quam_libs.lib.plot_utils import QubitGrid, grid_iter
from quam_libs.lib.save_utils import fetch_results_as_xarray, load_dataset, get_node_id
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
    qubits: Optional[List[str]] = None
    num_averages: int = 1000
    operation_x180_or_any_90: Literal["x180_Cosine", "x90_Cosine"] = "x180_Cosine"
    frequency_span_in_mhz: float = 100
    frequency_step_in_mhz: float = 0.25
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
span = node.parameters.frequency_span_in_mhz * u.MHz
step = node.parameters.frequency_step_in_mhz * u.MHz
dfs = np.arange(-span // 2, +span // 2, step, dtype=np.int32)
qubit_freqs = {q.name: q.I.intermediate_frequency for q in qubits}

# make sure that if using heralded readout then also using state discrimination
if reset_type == "heralding" and not state_discrimination:
    raise AssertionError("Heralded readout is only supported with state discrimination.")

q1 = machine.rf_qubits['q1']
q2 = machine.rf_qubits['q2']
c12 = machine.qubits['c12']

with program() as CZ_amp_cal:
    I, I_st, Q, Q_st, n, n_st = qua_declaration(num_qubits=num_qubits)
    if state_discrimination:
        state = [declare(bool) for _ in range(num_qubits)]
        state_stream = [declare_stream() for _ in range(num_qubits)]
    if reset_type == "heralding":
        init_state = [declare(bool) for _ in range(num_qubits)]
        final_state = [declare(bool) for _ in range(num_qubits)]
        res_state_00 = declare_stream()
        res_state_01 = declare_stream()
        res_state_10 = declare_stream()
        res_state_11 = declare_stream()
    df = declare(int)  # QUA variable for the qubit drive amplitude pre-factor
    npi = declare(int)  # QUA variable for the number of qubit pulses
    count = declare(int)  # QUA variable for counting the qubit pulses

    for i, qubit in enumerate(qubits):
        # Bring the active qubits to the minimum frequency point
        machine.set_all_fluxes(flux_point=flux_point, target=qubit)

    with for_(n, 0, n < n_avg, n + 1):
        save(n, n_st)
        with for_(*from_array(df, dfs)):
            # Initialize the qubits

            wait(40 * u.us)
            q1.resonator.measure("readout", qua_vars=(I[0], Q[0]))
            q2.resonator.measure("readout", qua_vars=(I[1], Q[1]))
            assign(init_state[0], I[0] > q1.resonator.operations["readout"].threshold)
            assign(init_state[1], I[1] > q2.resonator.operations["readout"].threshold)
            wait(4 * u.us)

            c12.xy.update_frequency(df + c12.xy.intermediate_frequency)

            align()

            play("saturation", c12.xy.name)

            align()

            play("x90_Cosine", q1.I.name)
            play("x90_Cosine", q1.I.name)
            play("x90_Cosine", q2.I.name)
            play("x90_Cosine", q2.I.name)

            align()

            q1.resonator.measure("readout", qua_vars=(I[0], Q[0]))
            q2.resonator.measure("readout", qua_vars=(I[1], Q[1]))

            assign(state[0], I[0] > q1.resonator.operations["readout"].threshold)
            assign(state[1], I[1] > q2.resonator.operations["readout"].threshold)
            assign(final_state[0], init_state[0] ^ state[0])
            assign(final_state[1], init_state[1] ^ state[1])

            with if_(~init_state[0] & ~init_state[1]):
                with if_(final_state[0] | final_state[1]):
                    save(0, res_state_00)
                    save(-1, res_state_01)
                    save(-1, res_state_10)
                    save(-1, res_state_11)
                with else_():
                    save(1, res_state_00)
                    save(-1, res_state_01)
                    save(-1, res_state_10)
                    save(-1, res_state_11)
            with if_(~init_state[0] & init_state[1]):
                with if_(final_state[0] | final_state[1]):
                    save(0, res_state_01)
                    save(-1, res_state_00)
                    save(-1, res_state_10)
                    save(-1, res_state_11)
                with else_():
                    save(1, res_state_01)
                    save(-1, res_state_00)
                    save(-1, res_state_10)
                    save(-1, res_state_11)
            with if_(init_state[0] & ~init_state[1]):
                with if_(final_state[0] | final_state[1]):
                    save(0, res_state_10)
                    save(-1, res_state_01)
                    save(-1, res_state_00)
                    save(-1, res_state_11)
                with else_():
                    save(1, res_state_10)
                    save(-1, res_state_01)
                    save(-1, res_state_00)
                    save(-1, res_state_11)
            with if_(init_state[0] & init_state[1]):
                with if_(final_state[0] | final_state[1]):
                    save(0, res_state_11)
                    save(-1, res_state_01)
                    save(-1, res_state_10)
                    save(-1, res_state_00)
                with else_():
                    save(1, res_state_11)
                    save(-1, res_state_01)
                    save(-1, res_state_10)
                    save(-1, res_state_00)

    with stream_processing():
        n_st.save("n")
        res_state_00.buffer(len(dfs)).save_all("state1_00")
        res_state_01.buffer(len(dfs)).save_all("state1_01")
        res_state_10.buffer(len(dfs)).save_all("state1_10")
        res_state_11.buffer(len(dfs)).save_all("state1_11")


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
    res = job.result_handles
    state_00 = res.state1_00.fetch_all()['value']
    state_01 = res.state1_01.fetch_all()['value']
    state_10 = res.state1_10.fetch_all()['value']
    state_11 = res.state1_11.fetch_all()['value']

    # changing the -1 values to NaN and calculating the mean
    state_00 = state_00.astype(float)  # Ensure float for NaN support
    state_00[state_00 == -1] = np.nan
    averaged_state_00 = np.nanmean(state_00, axis=0)

    state_01 = state_01.astype(float)  # Ensure float for NaN support
    state_01[state_01 == -1] = np.nan
    averaged_state_01 = np.nanmean(state_01, axis=0)

    state_10 = state_10.astype(float)  # Ensure float for NaN support
    state_10[state_10 == -1] = np.nan
    averaged_state_10 = np.nanmean(state_10, axis=0)

    state_11 = state_11.astype(float)  # Ensure float for NaN support
    state_11[state_11 == -1] = np.nan
    averaged_state_11 = np.nanmean(state_11, axis=0)


    fig, axes = plt.subplots(nrows=1, ncols=4, figsize=(16, 6))
    # Plots
    axes[0].plot((dfs + c12.xy.intermediate_frequency) / u.MHz, averaged_state_00)
    axes[0].set_title("CZ MAP with initial state 00")
    axes[0].set_xlabel("Coupler frequency [MHz]")
    axes[0].set_ylabel("Coupler state")
    axes[1].plot((dfs + c12.xy.intermediate_frequency) / u.MHz, averaged_state_01)
    axes[1].set_title("CZ MAP with initial state 01")
    axes[1].set_xlabel("Coupler frequency [MHz]")
    axes[1].set_ylabel("Coupler state")
    axes[2].plot((dfs + c12.xy.intermediate_frequency) / u.MHz, averaged_state_10)
    axes[2].set_title("CZ MAP with initial state 10")
    axes[2].set_xlabel("Coupler frequency [MHz]")
    axes[2].set_ylabel("Coupler state")
    axes[3].plot((dfs + c12.xy.intermediate_frequency) / u.MHz, averaged_state_11)
    axes[3].set_title("CZ MAP with initial state 11")
    axes[3].set_xlabel("Coupler frequency [MHz]")
    axes[3].set_ylabel("Coupler state")

    plt.show()

