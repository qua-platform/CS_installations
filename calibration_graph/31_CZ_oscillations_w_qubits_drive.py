

# %% {Imports}
from qualibrate import QualibrationNode, NodeParameters
from quam_libs.components import QuAM
from quam_libs.macros import active_reset, readout_state, readout_state_gef, active_reset_gef, multiplexed_readout
from quam_libs.lib.plot_utils import QubitPairGrid, grid_iter, grid_pair_names
from quam_libs.lib.save_utils import fetch_results_as_xarray, load_dataset
from quam_libs.lib.fit import fit_oscillation
from qualang_tools.results import progress_counter, fetching_tool
from qualang_tools.loops import from_array
from qualang_tools.multi_user import qm_session
from qualang_tools.units import unit
from qm import SimulationConfig
from qm.qua import *
from typing import Literal, Optional, List
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

# %% {Node_parameters}
class Parameters(NodeParameters):
    num_averages: int = 100
    max_time_in_ns: int = 160
    flux_point_joint_or_independent: Literal["joint", "independent"] = "joint"
    reset_type: Literal['active', 'thermal'] = "thermal"
    simulate: bool = False
    timeout: int = 100
    amp_range: float = 0.2
    amp_step: float = 0.01
    frequency_span_in_mhz: float = 100.0
    frequency_step_in_mhz: float = 0.1
    load_data_id: Optional[int] = None

node = QualibrationNode(
    name="31_CZ_oscillations_w_qubits_drive", parameters=Parameters()
)
assert not (node.parameters.simulate and node.parameters.load_data_id is not None), "If simulate is True, load_data_id must be None, and vice versa."

# %% {Initialize_QuAM_and_QOP}
# Class containing tools to help handling units and conversions.
u = unit(coerce_to_integer=True)
# Instantiate the QuAM class from the state file
machine = QuAM.load()

# Generate the OPX and Octave configurations
config = machine.generate_config()
octave_config = machine.get_octave_config()
# Open Communication with the QOP
if node.parameters.load_data_id is None:
    qmm = machine.connect()

n_avg = node.parameters.num_averages  # The number of averages

flux_point = node.parameters.flux_point_joint_or_independent  # 'independent' or 'joint'

# Loop parameters
span = node.parameters.frequency_span_in_mhz * u.MHz
step = node.parameters.frequency_step_in_mhz * u.MHz
dfs = np.arange(-span // 2, +span // 2, step, dtype=np.int32)

amplitudes = np.arange(1-node.parameters.amp_range, 1+node.parameters.amp_range, node.parameters.amp_step)

qubits = machine.active_qubits
qc = qubits[1]
qt = qubits[0]

with program() as CPhase_Oscillations:
    f = declare(int) # QUA variable for the frequency sweep
    idx = declare(int)
    amp = declare(fixed) # QUA variable for the amplitude sweep
    s = declare(int) # QUA variables for the control state preparation
    c = declare(int) # QUA variables for tomography measurement
    n = declare(int)
    n_st = declare_stream()
    I = [declare(fixed) for _ in range(2)]
    Q = [declare(fixed) for _ in range(2)]
    I_st = [declare_stream() for _ in range(2)]
    Q_st = [declare_stream() for _ in range(2)]

    with for_(n, 0, n < n_avg, n + 1):
        save(n, n_st)

        with for_(*from_array(f, dfs)):
            update_frequency(qc.xy.name, f + qc.xy.intermediate_frequency)
            update_frequency(qt.xy.name, f + qt.xy.intermediate_frequency)
            # rest of the pulse
            with for_(*from_array(amp, amplitudes)):
                wait(qc.thermalization_time * u.ns) # thermalization
                with for_(c, 0, c < 3, c + 1):  # bases
                    with for_(s, 0, s < 2, s + 1):  # states
                        with if_(s == 1):
                            qc.xy.play("x180")
                            align(qc.xy.name, qt.xy.name)

                        qt.xy.play("x90") # prepare target qubit in (|0>+|1>)/2

                        qc.xy.play("saturation", amplitude_scale=amp) # play CZ on control qubit
                        qt.xy.play("saturation", amplitude_scale=amp) # play CZ on target qubit

                        # QST on Target
                        with switch_(c):
                            with case_(0):  # projection along X
                                qt.xy.play("-y90")
                            with case_(1):  # projection along Y
                                qt.xy.play("x90")
                            with case_(2):  # projection along Z
                                wait(qt.xy.operations['x180'].length * u.ns, qt.xy.name) # wait x180_len

                        # measure both qubits
                        multiplexed_readout([qc, qt], I, I_st, Q, Q_st)


    with stream_processing():
        n_st.save("iteration")
        I_st[0].buffer(len(amplitudes)).buffer(len(dfs)).average().save('I1')
        Q_st[0].buffer(len(amplitudes)).buffer(len(dfs)).average().save('Q1')
        I_st[1].buffer(len(amplitudes)).buffer(len(dfs)).average().save('I2')
        Q_st[1].buffer(len(amplitudes)).buffer(len(dfs)).average().save('Q2')

# %% {Simulate_or_execute}
if node.parameters.simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=10_000)  # In clock cycles = 4ns
    job = qmm.simulate(config, CPhase_Oscillations, simulation_config)
    job.get_simulated_samples().con1.plot()
    node.results = {"figure": plt.gcf()}
    node.machine = machine
    node.save()
elif node.parameters.load_data_id is None:
    qm = qmm.open_qm(config)
    job = qm.execute(CPhase_Oscillations)
    #
    fetch_names = ["iteration", "I1", "Q1", "I2", "Q2"]
    results = fetching_tool(job, fetch_names, mode="live")
    # Live plotting
    while results.is_processing():
        # Fetch results
        iterations, I1, Q1, I2, Q2 = results.fetch_all()
        # Progress bar
        progress_counter(iterations, n_avg, start_time=results.start_time)
        # Convert the results into Volts
        I1, Q1 = u.demod2volts(I1, qc.resonator.operations['readout'].length), u.demod2volts(Q1, qc.resonator.operations['readout'].length)
        I2, Q2 = u.demod2volts(I2, qt.resonator.operations['readout'].length), u.demod2volts(Q2, qt.resonator.operations['readout'].length)

        S = u.demod2volts(I2 + 1j * Q2, qt.resonator.operations['readout'].length)
        R = np.abs(S)  # Amplitude
        phase = np.angle(S)  # Phase
        # Normalize data
        row_sums = R.sum(axis=0)
        R /= row_sums[np.newaxis, :]
        # 2D spectroscopy plot
        plt.subplot(211)
        plt.suptitle("target qubit state")
        plt.cla()
        plt.title(r"$R=\sqrt{I^2 + Q^2}$ (normalized)")
        plt.pcolor(amplitudes * qt.resonator.operations['readout'].amplitude, dfs / u.MHz, R)
        plt.xscale("log")
        plt.xlim(amplitudes[0] * qt.resonator.operations['readout'].amplitude, amplitudes[-1] * qt.resonator.operations['readout'].amplitude)
        plt.ylabel("detuning [MHz]")
        plt.subplot(212)
        plt.cla()
        plt.title("Phase")
        plt.pcolor(amplitudes * qt.resonator.operations['readout'].amplitude, dfs / u.MHz, signal.detrend(np.unwrap(phase)))
        plt.ylabel("detuning [MHz]")
        plt.xlabel("Drive amplitude [V]")
        plt.xscale("log")
        plt.xlim(amplitudes[0] * qt.resonator.operations['readout'].amplitude, amplitudes[-1] * qt.resonator.operations['readout'].amplitude)
        plt.pause(5)
        plt.tight_layout()
