# %%
"""
        CRYOSCOPE
"""

from qm import QuantumMachinesManager, SimulationConfig
from qm.qua import *
from configuration import *
from scipy import signal
import matplotlib.pyplot as plt
from qualang_tools.results import fetching_tool, progress_counter
from qualang_tools.plot import interrupt_on_close
import numpy as np
from qualang_tools.bakery import baking

####################
# Helper functions #
####################

def baked_waveform(waveform_amp, flux_el):
    pulse_segments = []  # Stores the baking objects
    # Create the different baked sequences, each one corresponding to a different truncated duration
    waveform = [waveform_amp] * 16

    for i in range(1, 17):  # from first item up to pulse_duration (16)
        with baking(config, padding_method="left") as b:
            wf = waveform[:i]
            b.add_op("flux_pulse", flux_el, wf)
            b.play("flux_pulse", flux_el)

        # Append the baking object in the list to call it from the QUA program
        pulse_segments.append(b)

    return pulse_segments

###################
# The QUA program #
###################
    
n_avg = 1_000  # Number of averages

cryoscope_len = 112

assert cryoscope_len % 16 == 0, 'cryoscope_len is not multiple of 16 nanoseconds'

baked_signals = {}
# Baked flux pulse segments with 1ns resolution
# the first 16 nanoseconds and the 0.0 before the step
flux_amp = const_flux_amp
baked_signals = baked_waveform(flux_amp, 'flux_line') 

cryoscope_time = np.arange(1, cryoscope_len + 1, 1)  # x-axis for plotting - must be in ns

window_len = 3
poly_or = 2

# %%
with program() as cryoscope:

    n = declare(int)
    n_st = declare_stream()
    I = declare(fixed)
    Q = declare(fixed)
    I_st = declare_stream()
    Q_st = declare_stream()
    t = declare(int)  # QUA variable for the flux pulse segment index
    state = declare(bool)
    state_st = declare_stream()
    idx = declare(int)
    idx2 = declare(int)
    flag = declare(bool)

    # Outer loop for averaging
    with for_(n, 0, n < n_avg, n + 1):
        save(n, n_st)

        # The first 16 nanoseconds
        # for time_segment in np.arange(0, 16):
        with for_(idx, 0, idx<16, idx+1):
            # Alternate between X/2 and Y/2 pulses
            # for tomo in ['x90', 'y90']:
            with for_each_(flag, [True, False]):
                # align()
                # Play first X/2
                play("x90", 'qubit')
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
                wait((cryoscope_len + 16) // 4, 'qubit')
                # Play second X/2 or Y/2
                # if tomo == 'x90':
                with if_(flag):
                    play("x90", 'qubit')
                # elif tomo == 'y90':
                with else_():
                    play("y90", 'qubit')

                # Measure resonator state after the sequence
                align()
                measure(
                    "readout",
                    "resonator",
                    None,
                    dual_demod.full("rotated_cos", "out1", "rotated_sin", "out2", I),
                    dual_demod.full("rotated_minus_sin", "out1", "rotated_cos", "out2", Q),
                )
                save(I, I_st)
                save(Q, Q_st)
                assign(state, I > ge_threshold)
                save(state, state_st)

                wait(thermalization_time // 4)

        with for_(t, 4, t < cryoscope_len // 4, t + 4):

            # for time_segment in np.arange(0, 16):
            with for_(idx2, 0, idx2<16, idx2+1):

                # Alternate between X/2 and Y/2 pulses
                # for tomo in ['x90', 'y90']:
                with for_each_(flag, [True, False]):
                    align()
                    # Play first X/2
                    play("x90", 'qubit')
                    align()

                    # Delay between x90 and the flux pulse
                    wait(16 // 4)
                    align()
                    with switch_(idx2):
                        for j in range(16):
                            with case_(j):
                                baked_signals[j].run() 
                                play('const', 'flux_line', duration=t)

                    # Wait for the idle time set slightly above the maximum flux pulse duration to ensure that the 2nd x90
                    # pulse arrives after the longest flux pulse
                    wait((cryoscope_len + 16) // 4, 'qubit')
                    # Play second X/2 or Y/2
                    with if_(flag):
                    # if tomo == 'x90':
                        play("x90", 'qubit')
                    # elif tomo == 'y90':
                    with else_():
                        play("y90", 'qubit')

                    # Measure resonator state after the sequence
                    align()

                    measure(
                        "readout",
                        "resonator",
                        None,
                        dual_demod.full("rotated_cos", "out1", "rotated_sin", "out2", I),
                        dual_demod.full("rotated_minus_sin", "out1", "rotated_cos", "out2", Q),
                    )
                    save(I, I_st)
                    save(Q, Q_st)
                    assign(state, I > ge_threshold)
                    save(state, state_st)

                    wait(thermalization_time // 4)

    with stream_processing():
        # for the progress counter
        n_st.save("iteration")
        I_st.buffer(2).buffer(cryoscope_len).average().save("I")
        Q_st.buffer(2).buffer(cryoscope_len).average().save("Q")
        state_st.boolean_to_int().buffer(2).buffer(cryoscope_len).average().save("state")


# %%
#####################################
#  Open Communication with the QOP  #
#####################################

qmm = QuantumMachinesManager(host=qop_ip, port=qop_port, cluster_name=cluster_name)
qmm.close_all_qms()

###########################
# Run or Simulate Program #
###########################
simulate = True

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=50_000)  # In clock cycles = 4ns
    job = qmm.simulate(config, cryoscope, simulation_config)
    job.get_simulated_samples().con1.plot()
    analog5 = job.get_simulated_samples().con1.analog['5']
    threshold = 0.01
    indices = np.where(np.diff(np.sign(analog5 - threshold)) != 0)[0] + 1
    # Plot the signal
    plt.figure(figsize=(10, 6))
    plt.plot(analog5)
    plt.axhline(threshold, color='r', linestyle='--', label='Threshold')
    for idx in indices:
        plt.axvline(idx, color='g', linestyle='--')

    subtracted_values = []

    for i in range(0, len(indices), 2):
        if i + 1 < len(indices):
            subtracted_value = indices[i + 1] - indices[i]
            subtracted_values.append(subtracted_value)

    # Print the subtracted values
    for i, value in enumerate(subtracted_values):
        print(f"Subtracted value {i + 1}: {value}")
    plt.show()
else:
    try:
        # Open the quantum machine
        qm = qmm.open_qm(config, close_other_machines=False)
        print("Open QMs: ", qmm.list_open_qms())
        # Send the QUA program to the OPX, which compiles and executes it
        job = qm.execute(cryoscope)
        fetch_names = ["iteration"]
        fetch_names.append("I")
        fetch_names.append("Q")
        fetch_names.append("state")
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

            state_data = (-2*res[3]+1) - np.mean((-2*res[3]+1)[-len(res[3]):])
            state_S = state_data[:,0] + 1j*state_data[:,1]
            state_phase = np.unwrap(np.angle(state_S)) - np.unwrap(np.angle(state_S))[-1]
            state_signal_freq = -signal.savgol_filter(state_phase / 2 / np.pi, window_len, poly_or, deriv=1)
            state_signal_freq = state_signal_freq / np.mean(state_signal_freq)
            state_signal_volt = np.sqrt(state_signal_freq)

            I_data = (res[1]) - np.mean((res[1])[-len(res[1]):])
            I_S = I_data[:,0] + 1j*I_data[:,1]
            I_phase = np.unwrap(np.angle(I_S)) - np.unwrap(np.angle(I_S))[-1]
            I_signal_freq = -signal.savgol_filter(I_phase / 2 / np.pi, window_len, poly_or, deriv=1)
            I_signal_freq = I_signal_freq / np.mean(I_signal_freq)
            I_signal_volt = np.sqrt(I_signal_freq)

            # Inside the while loop, after calculating state_signal_volt and I_signal_volt

            # Plot state
            plt.subplot(1, 2, 1)
            plt.cla()
            plt.plot(cryoscope_time, res[3])
            plt.ylabel("State")
            plt.xlabel("Pulse length [ns]")

            # Plot state_signal_volt and I_signal_volt
            plt.subplot(1, 2, 2)
            plt.cla()
            plt.plot(cryoscope_time, state_signal_volt, label='State Signal Volt')
            plt.plot(cryoscope_time, I_signal_volt, label='I Signal Volt')
            plt.ylabel("Signal Volt")
            plt.xlabel('Pulse length [ns]')
            plt.legend()

            plt.tight_layout()
            plt.pause(1.0)

    finally:
        qm.close()
        print("Experiment QM is now closed")
        plt.show(block=True)

# %%
