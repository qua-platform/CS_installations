# %%
"""
        CALIBRATE DELAYS
The program consists in playing a mw pulse during a laser pulse and while measuring throughout the sequence.
This allows measuring all the delays in the system, as well as the NV initialization duration.

Next steps before going to the next node:
    - Update the initial laser delay (laser_delay_1) and initialization length (initialization_len_1) in the configuration.
    - Update the delay between the laser and mw (mw_delay) and the mw length (mw_len) in the configuration.
    - Update the measurement length (meas_len_1) in the configuration.
"""
from qm.QuantumMachinesManager import QuantumMachinesManager
from qm.qua import *
from qm import SimulationConfig
import matplotlib.pyplot as plt
from qualang_tools.results import progress_counter, fetching_tool
from qualang_tools.plot import interrupt_on_close
from utils import save_files_and_get_dir_data
from configuration import *


###################
# The QUA program #
###################
laser_delay = 500  # delay before laser [ns]
initialization_len = 2_000  # laser duration length [ns]
mw_len = 1_000  # MW duration length [ns]
wait_between_runs = 1_000  # [ns]
n_avg = 100

# total measurement length (ns), add 2*laser_delay to ensure that the window is larger than the laser pulse
meas_len = int(initialization_len + 2 * laser_delay)
config["pulses"]["readout_pulse"]["length"] = meas_len
# Time vector for plotting
t_vec = np.arange(0, meas_len, 1)

assert (initialization_len - mw_len) > 4, "The MW must be shorter than the laser pulse"


def play_laser_mw_and_measure_pd(I_st, mw_amp_ratio: float = 1):
    # Wait before starting the play the laser pulse
    wait(laser_delay * u.ns, "AOM")
    # Play the laser pulse for a duration given here by "initialization_len"
    play("laser_ON", "AOM", duration=initialization_len * u.ns)

    # Delay the microwave pulse with respect to the laser pulse so that it arrive at the middle of the laser pulse
    wait((laser_delay + (initialization_len - mw_len) // 2) * u.ns, "NVs")
    # Play microwave pulse
    play("cw" * amp(mw_amp_ratio), "NVs", duration=mw_len * u.ns)

    # Measure the signal by the PD
    measure("readout", "PD", I_st)
    # Adjust the wait time between each averaging iterations
    wait(wait_between_runs * u.ns, "PD")


with program() as calib_delays:
    n = declare(int)  # variable used in for loop for averaging
    n_st = declare_stream()  # stream variable used in for loop for averaging
    I_mw_on_st = declare_stream(adc_trace=True)  # stream for PD reading
    I_mw_off_st = declare_stream(adc_trace=True)  # stream for PD reading

    with for_(n, 0, n < n_avg, n + 1):  # QUA for_ loop for averaging
        play_laser_mw_and_measure_pd(I_mw_on_st, mw_amp_ratio=1)

        align()  # global align before measuring the dark counts

        play_laser_mw_and_measure_pd(I_mw_off_st, mw_amp_ratio=0)

        save(n, n_st)

    with stream_processing():
        # Directly derive the histograms in the stream processing
        I_mw_on_st.input1().average().save("I_mw_on")
        I_mw_off_st.input1().average().save("I_mw_off")
        n_st.save("iterations")


#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(host=qop_ip, port=None, cluster_name=cluster_name, octave=None)

#######################
# Simulate or execute #
#######################
simulate = False
save_data = True

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=2_000)  # In clock cycles = 4ns
    job = qmm.simulate(config, calib_delays, simulation_config)
    job.get_simulated_samples().con1.plot()

else:
    # Open the quantum machine
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(calib_delays)
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
        plt.plot(t_vec, I_mw_on)
        plt.plot(t_vec, I_mw_off)
        plt.xlabel("t [ns]")
        plt.ylabel("PD Voltage [V]")
        plt.title("Delays")
        plt.legend(["mw_on", "mw_off"])
        plt.pause(0.1)

    if save_data:
        dir_data = save_files_and_get_dir_data(
            base_dir=base_dir,
            save_dir=save_dir,
            script_path=__file__,
        )
        np.savez(
            file=dir_data / "data.npz",
            I_mw_on=I_mw_on,
            I_mw_off=I_mw_off,
            iterations=iterations,
        )
        # If a matplotlib figure object is available.
        fig.savefig(dir_data / "data_live.png")

# %%
