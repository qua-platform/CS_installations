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
from qualang_tools.loops import from_array

###################
# The QUA program #
###################
    
n_avg = 1_000  # Number of averages

window_len = 3
poly_or = 2

cryoscope_amps = np.arange(0, 1, 0.1)

# %%
with program() as cryoscope:

    n = declare(int)
    n_st = declare_stream()
    I = declare(fixed)
    Q = declare(fixed)
    I_st = declare_stream()
    Q_st = declare_stream()
    a = declare(fixed) 
    state = declare(bool)
    state_st = declare_stream()
    idx = declare(int)
    idx2 = declare(int)
    flag = declare(bool)

    # Outer loop for averaging
    with for_(n, 0, n < n_avg, n + 1):
        save(n, n_st)

        with for_(*from_array(a, cryoscope_amps)):

            # Alternate between X/2 and Y/2 pulses
            # for tomo in ['x90', 'y90']:
            with for_each_(flag, [True, False]):
                align()
                # Play first X/2
                play("x90", 'qubit')
                align()

                # Delay between x90 and the flux pulse
                wait(32 // 4)
                align()

                play('const'*amp(a), 'flux_line')

                # Wait for the idle time set slightly above the maximum flux pulse duration to ensure that the 2nd x90
                # pulse arrives after the longest flux pulse
                wait((const_flux_len + 32) // 4, 'qubit')
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
        I_st.buffer(2).buffer(len(cryoscope_amps)).average().save("I")
        Q_st.buffer(2).buffer(len(cryoscope_amps)).average().save("Q")
        state_st.boolean_to_int().buffer(2).buffer(len(cryoscope_amps)).average().save("state")


# %%
#####################################
#  Open Communication with the QOP  #
#####################################

qmm = QuantumMachinesManager(host=qop_ip, port=qop_port, cluster_name=cluster_name)
qmm.close_all_qms()

###########################
# Run or Simulate Program #
###########################
simulate = False

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=10_000)  # In clock cycles = 4ns
    job = qmm.simulate(config, cryoscope, simulation_config)
    job.get_simulated_samples().con1.plot()
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
            state_phase = np.unwrap(np.angle(state_S))
            state_signal_freq = state_phase / (2 * np.pi * const_flux_len)

            I_data = (res[1]) - np.mean((res[1])[-len(res[1]):])
            I_S = I_data[:,0] + 1j*I_data[:,1]
            I_phase = np.unwrap(np.angle(I_S))
            I_signal_freq = I_phase / (2 * np.pi * const_flux_len)

            # Inside the while loop, after calculating state_signal_volt and I_signal_volt

            # Plot state
            plt.subplot(1, 2, 1)
            plt.cla()
            plt.plot(cryoscope_amps, res[3])
            plt.ylabel("State")
            plt.xlabel("Pulse length [ns]")

            # Plot state_signal_volt and I_signal_volt
            plt.subplot(1, 2, 2)
            plt.cla()
            plt.plot(cryoscope_amps, state_signal_freq, label='State Signal Freq')
            plt.plot(cryoscope_amps, I_signal_freq, label='I Signal Freq')
            plt.ylabel("Signal Volt")
            plt.xlabel('Pulse length [ns]')
            plt.legend()

            plt.tight_layout()
            plt.pause(1.0)

        pol_state = np.polyfit(cryoscope_amps, state_signal_freq, deg=2)
        pol_I = np.polyfit(cryoscope_amps, I_signal_freq, deg=2)

    finally:
        qm.close()
        print("Experiment QM is now closed")
        plt.show(block=True)

# %%
