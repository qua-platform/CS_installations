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
    num_averages: int = 10
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
initial_state = '00'
with program() as CZ_amp_cal:
    I, I_st, Q, Q_st, n, n_st = qua_declaration(num_qubits=num_qubits)
    if state_discrimination:
        state = [declare(int) for _ in range(num_qubits)]
        state_stream = [declare_stream() for _ in range(num_qubits)]
    if reset_type == "heralding":
        init_state = [declare(int) for _ in range(num_qubits)]
        final_state = [declare(int) for _ in range(num_qubits)]
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
            q1.resonator.measure("readout", qua_vars=(I[0], Q[0]))
            q2.resonator.measure("readout", qua_vars=(I[1], Q[1]))
            if initial_state == '00':
                play("x180_Cosine", q1.I.name, condition=I[0] > q1.resonator.operations["readout"].threshold)
                play("x180_Cosine", q2.I.name, condition=if_(I[1] > q2.resonator.operations["readout"].threshold))
            elif initial_state == '01':
                play("x180_Cosine", q1.I.name, condition=I[0] > q1.resonator.operations["readout"].threshold)
                play("x180_Cosine", q2.I.name, condition=I[1] < q2.resonator.operations["readout"].threshold)
            elif initial_state == '10':
                play("x180_Cosine", q1.I.name, condition=I[0] < q1.resonator.operations["readout"].threshold)
                play("x180_Cosine", q2.I.name, condition=I[1] > q2.resonator.operations["readout"].threshold)
            elif initial_state == '11':
                play("x180_Cosine", q1.I.name, condition=I[0] < q1.resonator.operations["readout"].threshold)
                play("x180_Cosine", q2.I.name, condition=I[1] < q2.resonator.operations["readout"].threshold)

            wait(1000)
            align()
            c12.xy.update_frequency(df + c12.xy.intermediate_frequency)

            align()

            play("x180", c12.xy.name)

            align()

            play("x90_Cosine", q1.I.name)
            play("x90_Cosine", q1.I.name)
            play("x90_Cosine", q2.I.name)
            play("x90_Cosine", q2.I.name)

            align()

            q1.resonator.measure("readout", qua_vars=(I[0], Q[0]))
            q2.resonator.measure("readout", qua_vars=(I[1], Q[1]))

            assign(state[0], Cast.to_int(I[0] > q1.resonator.operations["readout"].threshold))
            assign(state[1], Cast.to_int(I[1] > q2.resonator.operations["readout"].threshold))
            save(state[0], state_stream[0])
            save(state[1], state_stream[1])


    with stream_processing():
        n_st.save("n")
        state_stream[0].buffer(len(dfs)).average().save("state1")
        state_stream[1].buffer(len(dfs)).average().save("state2")


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
    state_q1 = res.state1.fetch_all()
    state_q2 = res.state2.fetch_all()


    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(16, 6))
    # Plots
    axes[0].plot((dfs + c12.xy.intermediate_frequency) / u.MHz, state_q1)
    axes[0].set_title("CZ MAP with initial state 00")
    axes[0].set_xlabel("Coupler frequency [MHz]")
    axes[0].set_ylabel("qubit1 state")
    axes[1].plot((dfs + c12.xy.intermediate_frequency) / u.MHz, state_q2)
    axes[1].set_title("CZ MAP with initial state 01")
    axes[1].set_xlabel("Coupler frequency [MHz]")
    axes[1].set_ylabel("qubit2 state")

    plt.show()

