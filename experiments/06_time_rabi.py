# %%
"""
        TIME RABI
The program consists in playing a mw pulse and measure the photon counts received by the PD
across varying mw pulse durations.
The sequence is repeated without playing the mw pulses to measure the dark counts on the PD.

The data is then post-processed to determine the pi pulse duration for the specified amplitude.

Prerequisites:
    - Ensure calibration of the different delays in the system (calibrate_delays).
    - Having updated the different delays in the configuration.
    - Having updated the NV frequency, labeled as "NV_IF_freq", in the configuration.
    - Set the desired pi pulse amplitude, labeled as "mw_amp_NV", in the configuration

Next steps before going to the next node:
    - Update the pi pulse duration, labeled as "mw_len_NV", in the configuration.
"""
from qm.QuantumMachinesManager import QuantumMachinesManager
from qm.qua import *
from qm import SimulationConfig
from qualang_tools.results import progress_counter, fetching_tool
from qualang_tools.plot import interrupt_on_close
from qualang_tools.loops import from_array
from utils import save_files_and_get_dir_data
import matplotlib.pyplot as plt
from configuration import *


###################
# The QUA program #
###################

def play_time_rabi(I, I_st, t: int, mw_amp_ratio: float = 1):
    # Play the Rabi pulse with varying durations
    play("x180" * amp(1), "NVs", duration=t)
    align()  # Play the laser pulse after the mw pulse
    play("laser_ON", "AOM")
    # Measure and detect the photons on PD
    measure("readout", "PD", None, integration.full("const", I, "out1"))
    save(I, I_st)  # save counts


t_vec = np.arange(4, 400, 1)  # Pulse durations in clock cycles (4ns)
n_avg = 1_000  # Number of averaging loops

with program() as time_rabi:
    t = declare(int)  # variable to sweep over in time
    n = declare(int)  # number of iterations
    I_mw_on = declare(fixed)  # variable for PD reading
    I_mw_off = declare(fixed)  # variable for PD reading
    
    n_st = declare_stream()  # stream for number of iterations
    I_mw_on_st = declare_stream()  # stream for PD reading
    I_mw_off_st = declare_stream()  # stream for PD reading

    # Spin initialization
    play("laser_ON", "AOM")
    wait(wait_for_initialization * u.ns, "AOM")

    # Time Rabi sweep
    with for_(n, 0, n < n_avg, n + 1):
        with for_(*from_array(t, t_vec)):
            # Play the Rabi pulse with varying durations
            play_time_rabi(I_mw_on, I_mw_on_st, t=t, mw_amp_ratio=1)

            # Wait and align all elements before measuring the dark events
            wait(wait_between_runs * u.ns)
            align()

            # Play the Rabi pulse with zero amplitude
            play_time_rabi(I_mw_off, I_mw_off_st, t=t, mw_amp_ratio=0)

            # Wait and align all elements before measuring the next iterations 
            wait(wait_between_runs * u.ns)

        save(n, n_st)  # save number of iterations inside for_loop

    with stream_processing():
        # Cast the data into a 1D vector, average the 1D vectors together and store the results on the OPX processor
        I_mw_on_st.buffer(len(t_vec)).average().save("I_mw_on")
        I_mw_off_st.buffer(len(t_vec)).average().save("I_mw_off")
        n_st.save("iterations")


#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(host=qop_ip, cluster_name=cluster_name)

#######################
# Simulate or execute #
#######################
simulate = False
save_data = True

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=10_000)  # In clock cycles = 4ns
    job = qmm.simulate(config, time_rabi, simulation_config)
    job.get_simulated_samples().con1.plot()
else:
    # Open the quantum machine
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(time_rabi)
    # Get results from QUA program
    results = fetching_tool(job, data_list=["I_mw_on", "I_mw_off", "iterations"], mode="live")
    # Live plotting
    fig = plt.figure()
    interrupt_on_close(fig, job)  # Interrupts the job when closing the figure

    while results.is_processing():
        # Fetch results
        I_mw_on, I_mw_off, iterations = results.fetch_all()
        I_mw_on, I_mw_off = u.demod2volts(I_mw_on, meas_len), u.demod2volts(I_mw_off, meas_len)
        # Progress bar
        progress_counter(iterations, n_avg, start_time=results.get_start_time())
        # Plot data
        plt.cla()
        plt.plot(t_vec * 4, I_mw_on, label="mw on")
        plt.plot(t_vec * 4, I_mw_off, label="mw off")
        plt.xlabel("Rabi pulse duration [ns]")
        plt.ylabel("PD Voltage [V]")
        plt.title("Time Rabi")
        plt.legend()
        plt.pause(0.1)

    if save_data:
        dir_data = save_files_and_get_dir_data(
            base_dir=base_dir,
            save_dir=save_dir,
            script_path=__file__,
        )
        # Suppose we want to save I, Q, iterations. 
        np.savez(
            file=dir_data / "data.npz",
            I_mw_on=I_mw_on,
            I_mw_off=I_mw_off,
            iterations=iterations,
        )
        # If a matplotlib figure object is available.
        fig.savefig(dir_data / "data_live.png")

# %%
