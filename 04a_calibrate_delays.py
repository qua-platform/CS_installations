# %%
"""
        CALIBRATE DELAYS
The program consists in playing a mw pulse during a laser pulse and while performing time tagging throughout the sequence.
This allows measuring all the delays in the system, as well as the NV initialization duration.
If the counts are too high, the program might hang. In this case reduce the resolution or use
calibrate_delays_python_histogram.py if high resolution is needed.

Next steps before going to the next node:
    - Update the initial laser delay (laser_delay_1) and initialization length (initialization_len_1) in the configuration.
    - Update the delay between the laser and mw (mw_delay) and the mw length (mw_len) in the configuration.
    - Update the measurement length (meas_len_1) in the configuration.
"""
from qm import QuantumMachinesManager
from qm.qua import *
from qm import SimulationConfig
from qualang_tools.results import progress_counter, fetching_tool
from qualang_tools.plot import interrupt_on_close
from qualang_tools.loops import from_array
from qualang_tools.results.data_handler import DataHandler
from configuration_with_octave import *
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import time

matplotlib.use('TkAgg')


###################
# The QUA program #
###################
laser_delay = 16  # delay before laser [ns]
initialization_len = 2_000  # laser duration length [ns]
mw_len = 1_000  # MW duration length [ns]
wait_between_runs = 1_000  # [ns]
n_avg = 3

resolution = 20 # ns

# total measurement length (ns), add 2*laser_delay to ensure that the window is larger than the laser pulse
meas_len = int((initialization_len + 4 * laser_delay) * u.ns)
config["pulses"]["readout_pulse"]["length"] = meas_len
# Time vector for plotting
ts_ns = np.arange(0, meas_len, 1)

assert (initialization_len - mw_len) > 4, "The MW must be shorter than the laser pulse"


# Main sequence macro
def calibrate_delays(
    times, counts, mw_on: bool = True,
    laser_delay=laser_delay,
    initialization_len=initialization_len,
    mw_len=mw_len,
):
    # Delay for laser
    wait(laser_delay * u.ns, "AOM")
    # Play the laser pulse for a duration given here by "initialization_len"
    play("laser_ON", "AOM", duration=initialization_len * u.ns)

    # Delay the microwave pulse with respect to the laser pulse so that it arrive at the middle of the laser pulse
    if mw_on:
        wait((laser_delay + (initialization_len - mw_len) // 2) * u.ns, "NV")
        play("cw", "NV", duration=mw_len * u.ns)
        
    # Measure the signal by the SPCM
    measure("readout", "SPCM", None, time_tagging.analog(times, meas_len, counts))
    # measure("readout", "SPCM", None, time_tagging.analog(times, meas_len, counts, element_output="out1"), time_tagging.analog(times, meas_len, counts, element_output="out2"))
    
    return times, counts


with program() as calib_delays:
    i = declare(int)  # variable used to save data
    n = declare(int)  # variable used in for loop for averaging
    n_st = declare_stream()  # stream variable used in for loop for averaging

    times_on = declare(int, size=5000)  # QUA vector for storing the time-tags
    times_on_st = declare_stream()  # stream for 'times_on'
    counts_on = declare(int)  # variable for number of counts_on of a single chunk

    times_off = declare(int, size=5000)  # QUA vector for storing the time-tags
    times_off_st = declare_stream()  # stream for 'times_off'
    counts_off = declare(int)  # variable for number of counts_off of a single chunk

    with for_(n, 0, n < n_avg, n + 1):  # QUA for_ loop for averaging
        
        # MW ON
        times_on, counts_on = calibrate_delays(
            times=times_on, counts=counts_on,
            mw_on=True, laser_delay=laser_delay,
        )
        wait(wait_between_runs * u.ns)
        with for_(i, 0, i < counts_on, i + 1):
            save(times_on[i], times_on_st)

        align()
        
        # MW OFF
        times_off, counts_off = calibrate_delays(
            times=times_off, counts=counts_off,
            mw_on=False, laser_delay=laser_delay,
        )
        wait(wait_between_runs * u.ns)
        with for_(i, 0, i < counts_off, i + 1):
            save(times_off[i], times_off_st)

        save(n, n_st)

    with stream_processing():
        # Directly derive the histograms in the stream processing
        times_on_st.histogram([[i, i + (resolution - 1)] for i in range(0, meas_len, resolution)]).save("times_on_hist")
        times_off_st.histogram([[i, i + (resolution - 1)] for i in range(0, meas_len, resolution)]).save("times_off_hist")
        n_st.save("iterations")


#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(host=qop_ip, port=None, cluster_name=cluster_name, octave=octave_config)

#######################
# Simulate or execute #
#######################
simulate = False
save_data = True

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=3_000)  # In clock cycles = 4ns
    job = qmm.simulate(config, calib_delays, simulation_config)
    job.get_simulated_samples().con1.plot()

else:
    # Open the quantum machine
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(calib_delays)
    # Get results from QUA program
    results = fetching_tool(job, data_list=["times_on_hist", "times_off_hist", "iterations"], mode="live")
    # Live plotting
    fig = plt.figure()
    interrupt_on_close(fig, job)  # Interrupts the job when closing the figure
    while results.is_processing():
        # Fetch results
        times_on_hist, times_off_hist, iterations = results.fetch_all()
        plt.cla()
        plt.plot(ts_ns[::resolution] + resolution / 2, times_on_hist / 1000 / (resolution / u.s) / iterations)
        plt.plot(ts_ns[::resolution] + resolution / 2, times_off_hist / 1000 / (resolution / u.s) / iterations)
        plt.xlabel("t [ns]")
        plt.ylabel(f"counts_on [kcps / {resolution}ns]")
        plt.title("Delays")
        plt.pause(1)

    plt.show()

    if save_data:
        # Arrange data to save
        data = {
            "fig_live": fig,
            "ts_ns": ts_ns,
            "times_on_hist": times_on_hist,
            "times_off_hist": times_off_hist,
            "iterations": np.array(iterations),
            "resolution": resolution,
            # "elapsed_time": np.array([elapsed_time]),  # convert float to np.array of float
        }
        # Initialize the DataHandler
        data_handler = DataHandler(root_data_folder=save_dir)
        data_handler.create_data_folder(name=Path(__file__).stem)
        data_handler.additional_files = {
            Path(__file__).name: Path(__file__).name,
            "configuration_with_octave.py": "configuration_with_octave.py",
        }
        # Save results
        data_folder = data_handler.save_data(data=data)


# %%
