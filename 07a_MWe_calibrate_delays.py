"""
        CALIBRATE DELAYS
The program consists in playing a mw pulse during a laser pulse and while performing time tagging throughout the sequence.
This allows measuring all the delays in the system.
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
import matplotlib.pyplot as plt
from configuration_princeton_groundwork_with_octave import *

###################
# The QUA program #
###################

# Determine these values and enter into configuration to move on to next protocol

EOM_delay = 0  # in ns
mwe_delay = 0  # in ns
mwg_delay = 0  # in ns
SNSPD_delay = 0
RF_switch_delay = 0  # in ns
laser_delay = 100 // 4  # delay before laser [ns]
AOM1_delay = 0  # in ns
AOM2_delay = 0  # in ns

initial_delay_cycles = 500 // 4
laser_len_cycles = 2000 // 4
var_len_cycles = 1000 // 4
wait_between_runs = 3000 // 4

n_avg = 5000


resolution = 12  # ns

# total measurement length (ns), add 2*laser_delay to ensure that the window is larger than the laser pulse
meas_len = (
    laser_len_cycles * 4 + 1000
)  # need to change measure length of element in config, for current setup meas_len should = 3000 ns
# Time vector for plotting
t_vec = np.arange(0, meas_len, 1)

with program() as calib_mw_delays:
    times = declare(
        int, size=100
    )  # 'size' defines the max number of photons to be counted
    times_st = declare_stream()  # stream for 'times'
    counts = declare(int)  # variable to save the total number of photons
    i = declare(int)  # variable used to save data
    n = declare(int)  # variable used in for loop for averaging
    n_st = declare_stream()  # stream for 'iteration'

    with for_(n, 0, n < n_avg, n + 1):

        wait(initial_delay_cycles, "OpticalTrigger", "EOM", "AOM", "RF_switch")  # wait before starting PL, replace with elements not testing currently
        #After calibrating drive 1 (mwe), switch out "RF_switch" and mwe
        play("cw", "EOM", duration=laser_len_cycles)
        play("AOM_ON", "AOM", duration=laser_len_cycles)
        play("laser_ON", "OpticalTrigger", duration=laser_len_cycles)  # Cycle through each of these for various delays
        play("RF_ON", "RF_switch", duration=laser_len_cycles)

        wait(initial_delay_cycles + (laser_len_cycles - var_len_cycles) // 2, "mwe")  # delay the pulse until
        play("cw", "mwe", duration = var_len_cycles)  # play microwave pulse


        measure("readout", "SNSPD", None, time_tagging.analog(times, meas_len, counts))
        wait(wait_between_runs, "SNSPD")

        with for_(i, 0, i < counts, i + 1):
            save(times[i], times_st)  # save time tags to stream

        save(n, n_st)  # save number of iteration inside for_loop

    with stream_processing():
        times_st.histogram(
            [[i, i + (resolution - 1)] for i in range(0, meas_len, resolution)]
        ).save_all("times_hist")
        n_st.save("iteration")


#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(host=qop_ip, port=qop_port, cluster_name=cluster_name)

simulate = True
if simulate:
    simulation_config = SimulationConfig(duration=28000)
    job = qmm.simulate(config, calib_mw_delays, simulation_config)

    # Get the waveform report
    samples = job.get_simulated_samples()
    waveform_report = job.get_simulated_waveform_report()
    waveform_report.create_plot(samples, plot=True, save_path=None)

    # Plot simlation
    job.get_simulated_samples().con1.plot()
    plt.show()

else:
    qm = qmm.open_qm(config)

    job = qm.execute(calib_mw_delays)
    # Get results from QUA program
    results = fetching_tool(job, data_list=["times_hist", "iteration"], mode="live")
    # Live plotting
    fig = plt.figure()
    interrupt_on_close(fig, job)  # Interrupts the job when closing the figure

    while results.is_processing():
        # Fetch results
        times_hist, iteration = results.fetch_all()
        # Progress bar
        progress_counter(iteration, n_avg, start_time=results.get_start_time())
        # Plot data
        plt.cla()
        plt.plot(
            t_vec[::resolution] + resolution / 2,
            times_hist / 1000 / (resolution / u.s) / iteration,
        )
        plt.xlabel("t [ns]")
        plt.ylabel(f"counts [kcps / {resolution}ns]")
        plt.title("Delays")
        plt.pause(0.1)
