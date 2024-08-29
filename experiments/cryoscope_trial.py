# %%
"""
        CRYOSCOPE
"""

from qm import QuantumMachinesManager
from qm.qua import *
from qm import SimulationConfig
from scipy import signal
import matplotlib.pyplot as plt
from qualang_tools.results import fetching_tool, progress_counter
from qualang_tools.plot import interrupt_on_close
from quam_libs.macros import qua_declaration, multiplexed_readout, node_save
import numpy as np
from qualang_tools.units import unit
from quam_libs.components import QuAM
from qualang_tools.bakery import baking

import matplotlib

matplotlib.use("TKAgg")

from qualibrate import QualibrationNode, NodeParameters
from typing import Optional, Literal


class Parameters(NodeParameters):
    qubits: Optional[str] = None
    num_averages: int = 200
    flux_point_joint_or_independent: Literal['joint', 'independent'] = "joint"
    simulate: bool = False

node = QualibrationNode(
    name="Cryoscope_trial",
    parameters_class=Parameters
)

node.parameters = Parameters()

###################################################
#  Load QuAM and open Communication with the QOP  #
###################################################
# Class containing tools to help handling units and conversions.
u = unit(coerce_to_integer=True)
# Instantiate the QuAM class from the state file
machine = QuAM.load(r"C:\Users\KevinAVillegasRosale\OneDrive - QM Machines LTD\Documents\GitKraken\CS_installations\configuration\quam_state")
# machine = QuAM.load()
# Generate the OPX and Octave configurations
config = machine.generate_config()
octave_config = machine.get_octave_config()
# Open Communication with the QOP
qmm = machine.connect()

# Get the relevant QuAM components
if node.parameters.qubits is None:
    qubits = machine.active_qubits
else:
    qubits = [machine.qubits[q] for q in node.parameters.qubits.split(', ')]
num_qubits = len(qubits)

# %%

####################
# Helper functions #
####################

def baked_waveform(waveform_amp, qubit):
    pulse_segments = []  # Stores the baking objects
    # Create the different baked sequences, each one corresponding to a different truncated duration
    waveform = [waveform_amp] * 16

    for i in range(1, 17):  # from first item up to pulse_duration (16)
        with baking(config, padding_method="left") as b:
            wf = waveform[:i]
            b.add_op("flux_pulse", qubit.z.name, wf)
            b.play("flux_pulse", qubit.z.name)

        # Append the baking object in the list to call it from the QUA program
        pulse_segments.append(b)

    return pulse_segments

###################
# The QUA program #
###################
n_avg = node.parameters.num_averages  # The number of averages

cryoscope_len = 112

assert cryoscope_len % 16 == 0, 'cryoscope_len is not multiple of 16 nanoseconds'

baked_signals = {}
# Baked flux pulse segments with 1ns resolution
baked_signals = baked_waveform(qubits[0].z.operations['const'].amplitude, qubits[0]) 

cryoscope_time = np.arange(1, cryoscope_len + 1, 1)  # x-axis for plotting - must be in ns

window_len = 3
poly_or = 2

# %%

with program() as cryoscope:

    I, I_st, Q, Q_st, n, n_st = qua_declaration(num_qubits=num_qubits)
    t = declare(int)  # QUA variable for the flux pulse segment index
    state = [declare(bool) for _ in range(num_qubits)]
    state_st = [declare_stream() for _ in range(num_qubits)]
    global_state = declare(int)
    idx = declare(int)
    idx2 = declare(int)
    flag = declare(bool)

    # Bring the active qubits to the minimum frequency point
    machine.apply_all_flux_to_min()

    # Outer loop for averaging
    with for_(n, 0, n < n_avg, n + 1):
        save(n, n_st)

        # The first 16 nanoseconds
        with for_(idx, 0, idx<16, idx+1):
            # Alternate between X/2 and Y/2 pulses
            # for tomo in ['x90', 'y90']:
            with for_each_(flag, [True, False]):
                # Play first X/2
                for qubit in qubits:
                    qubit.xy.play("x90")

                align()

                # Delay between x90 and the flux pulse
                # NOTE: it can be made larger than 16 nanoseconds it could be benefitial
                wait(16 // 4)

                align()

                with switch_(idx):
                    for i in range(16):
                        with case_(i):
                            baked_signals[i].run()

                # Wait for the idle time set slightly above the maximum flux pulse duration to ensure that the 2nd x90
                # pulse arrives after the longest flux pulse
                for qubit in qubits:
                    qubit.xy.wait((cryoscope_len + 16) // 4)
                    # Play second X/2 or Y/2
                    # if tomo == 'x90':
                    with if_(flag):
                        qubit.xy.play("x90")
                    # elif tomo == 'y90':
                    with else_():
                        qubit.xy.play("y90")

                # Measure resonator state after the sequence
                align()

                multiplexed_readout(qubits, I, I_st, Q, Q_st)

                for i in range(num_qubits):
                    assign(state[i], Cast.to_int(I[i] > qubit.resonator.operations["readout"].threshold))
                    save(state[i], state_st[i])

                wait(5*machine.thermalization_time * u.ns)

        with for_(t, 4, t < cryoscope_len // 4, t + 4):

            with for_(idx2, 0, idx2<16, idx2+1):

                # Alternate between X/2 and Y/2 pulses
                # for tomo in ['x90', 'y90']:
                with for_each_(flag, [True, False]):

                    # Play first X/2
                    for qubit in qubits:
                        qubit.xy.play("x90")

                    align()

                    # Delay between x90 and the flux pulse
                    wait(16 // 4)

                    align()
                    with switch_(idx2):
                        for j in range(16):
                            with case_(j):
                                baked_signals[j].run() 
                                qubits[0].z.play('const', duration=t)

                    # Wait for the idle time set slightly above the maximum flux pulse duration to ensure that the 2nd x90
                    # pulse arrives after the longest flux pulse
                    for qubit in qubits:
                        qubit.xy.wait((cryoscope_len + 16) // 4)
                        # Play second X/2 or Y/2
                        with if_(flag):
                            qubit.xy.play("x90")
                        # elif tomo == 'y90':
                        with else_():
                            qubit.xy.play("y90")

                    # Measure resonator state after the sequence
                    align()
                    multiplexed_readout(qubits, I, I_st, Q, Q_st)

                    for i in range(num_qubits):
                        assign(state[i], Cast.to_int(I[i] > qubit.resonator.operations["readout"].threshold))
                        save(state[i], state_st[i])

                    wait(5*machine.thermalization_time * u.ns)

    with stream_processing():
        # for the progress counter
        n_st.save("iteration")
        for i, qubit in enumerate(qubits):
            I_st[i].buffer(2).buffer(cryoscope_len).average().save(f"I_{i + 1}")
            Q_st[i].buffer(2).buffer(cryoscope_len).average().save(f"Q_{i + 1}")
            state_st[i].boolean_to_int().buffer(2).buffer(cryoscope_len).average().save(f"state_{i + 1}")


# %%
###########################
# Run or Simulate Program #
###########################
simulate = True

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=1000)  # In clock cycles = 4ns
    job = qmm.simulate(config, cryoscope, simulation_config)
    job.get_simulated_samples().con1.plot()
    plt.show()
    # analog5 = job.get_simulated_samples().con1.analog['5']
    # threshold = 0.01
    # indices = np.where(np.diff(np.sign(analog5 - threshold)) != 0)[0] + 1
    # # Plot the signal
    # plt.figure(figsize=(10, 6))
    # plt.plot(analog5)
    # plt.axhline(threshold, color='r', linestyle='--', label='Threshold')
    # for idx in indices:
    #     plt.axvline(idx, color='g', linestyle='--')

    # subtracted_values = []

    # for i in range(0, len(indices), 2):
    #     if i + 1 < len(indices):
    #         subtracted_value = indices[i + 1] - indices[i]
    #         subtracted_values.append(subtracted_value)

    # # Print the subtracted values
    # for i, value in enumerate(subtracted_values):
    #     print(f"Subtracted value {i + 1}: {value}")
    # plt.show(block=False)
else:
    try:
        # Open the quantum machine
        qm = qmm.open_qm(config, close_other_machines=False)
        print("Open QMs: ", qmm.list_open_quantum_machines())
        # Send the QUA program to the OPX, which compiles and executes it
        job = qm.execute(cryoscope)
        fetch_names = ["iteration"]
        
        for i in range(num_qubits):
            fetch_names.append(f"I_{i + 1}")
            fetch_names.append(f"Q_{i + 1}")
            fetch_names.append(f"state_{i + 1}")

        # Tool to easily fetch results from the OPX (results_handle used in it)
        results = fetching_tool(job, fetch_names, mode="live")
        # Prepare the figure for live plotting
        fig = plt.figure()
        interrupt_on_close(fig, job)
        # Live plotting
        while results.is_processing():
            # Fetch results
            res = results.fetch_all()
            # Progress bar
            progress_counter(res[0], n_avg, start_time=results.start_time)

            plt.suptitle("Cryoscope")

            # state_data = (-2*res[3*ind+3]+1) - np.mean((-2*res[3*ind+3]+1)[-len(res[3*ind+3]):])
            # state_S = state_data[:,0] + 1j*state_data[:,1]
            # state_phase = np.unwrap(np.angle(state_S)) - np.unwrap(np.angle(state_S))[-1]
            # state_signal_freq = -signal.savgol_filter(state_phase / 2 / np.pi, window_len, poly_or, deriv=1)
            # state_signal_freq = state_signal_freq / np.mean(state_signal_freq)
            # state_signal_volt = np.sqrt(state_signal_freq)

            # I_data = (res[3*ind+1]) - np.mean((res[3*ind+1])[-len(res[3*ind+1]):])
            # I_S = I_data[:,0] + 1j*I_data[:,1]
            # I_phase = np.unwrap(np.angle(I_S)) - np.unwrap(np.angle(I_S))[-1]
            # I_signal_freq = -signal.savgol_filter(I_phase / 2 / np.pi, window_len, poly_or, deriv=1)
            # I_signal_freq = I_signal_freq / np.mean(I_signal_freq)
            # I_signal_volt = np.sqrt(I_signal_freq)

            # # Plot state
            # plt.subplot(num_rows, num_cols * 2, (ind * 2) + 1)
            # plt.cla()
            # plt.plot(cryoscope_time, res[3*ind + 3])
            # plt.ylabel("State")

            # # Plot state_signal_volt and I_signal_volt
            # plt.subplot(num_rows, num_cols * 2, (ind * 2) + 2)
            # plt.cla()
            # plt.plot(cryoscope_time, state_signal_volt, label='State Signal Volt')
            # plt.plot(cryoscope_time, I_signal_volt, label='I Signal Volt')
            # plt.ylabel("Signal Volt")
            # plt.legend()

            # plt.tight_layout()
            # plt.pause(1.0)

    finally:
        qm.close()
        print("Experiment QM is now closed")
        plt.show(block=True)

# %%