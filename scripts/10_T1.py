"""
       T1 MEASUREMENT
The program consists in measuring the photon counts (in |0> and |1> successively) received by the APD across
varying wait times either after initialization (start from |0>), or after a pi pulse (start from |1>).
The sequence is repeated without playing the mw pulses to measure the dark counts on the APD.

The data is then post-processed to determine the thermal relaxation time T1.

Prerequisites:
    - Ensure calibration of the different delays in the system (calibrate_delays).
    - Having updated the different delays in the configuration.
    - Having updated the NV frequency, labeled as "NV_IF_freq", in the configuration.
    - Having set the pi pulse amplitude and duration in the configuration

Next steps before going to the next node:
    -
"""

from qm import QuantumMachinesManager
from qm.qua import *
from qm import SimulationConfig
import matplotlib.pyplot as plt
from configuration import *
from qualang_tools.loops import from_array
from qualang_tools.results.data_handler import DataHandler

##################
#   Parameters   #
##################
# Parameters Definition
t_vec = np.arange(4, 250, 10)  # The wait time vector in clock cycles (4ns)
n_avg = 1_000_000  # The number averaging iterations
start_from_one = False

# Data to save
save_data_dict = {
    "n_avg": n_avg,
    "t_vec": t_vec,
    "config": config,
}

###################
# The QUA program #
###################
with program() as T1:
    counts = [declare(int) for i in range(8)]  # variable for number of counts
    counts_st = [declare_stream() for i in range(8)]  # stream for counts
    times = [declare(int, size=100) for i in range(8)]  # QUA vector for storing the time-tags
    times_st = [declare_stream() for i in range(8)]  # stream for counts
    t = declare(int)  # variable to sweep over in time
    n = declare(int)  # variable to for_loop
    n_st = declare_stream()  # stream to save iterations

    # T1 sequence
    with for_(n, 0, n < n_avg, n + 1):
        with for_(*from_array(t, t_vec)):
            # first two measurements
            play("laser_ON", "AOM",
                 duration=initialization_len * u.ns + 100 * u.ns)  # adding 100ns for some extra buffer time
            measure("readout", "APD", time_tagging.analog(times[0], meas_len, counts[0]))
            save(counts[0], counts_st[0])  # save counts
            wait((initialization_len - 2 * meas_len) * u.ns, "APD")
            measure("readout", "APD", time_tagging.analog(times[1], meas_len, counts[1]))
            save(counts[1], counts_st[1])  # save counts

            align()

            # Measure in |0>
            if start_from_one:  # Choose to initialize either from |0> or |1>
                play("x180" * amp(1), "NV")
            wait(t, "NV")  # variable delay before measurement

            align()  # Play the laser pulse after the mw sequence

            # second two measurements
            play("laser_ON", "AOM",
                 duration=initialization_len * u.ns + 100 * u.ns)  # adding 100ns for some extra buffer time
            measure("readout", "APD", time_tagging.analog(times[2], meas_len, counts[2]))
            save(counts[2], counts_st[2])  # save counts
            wait((initialization_len - 2 * meas_len) * u.ns, "APD")
            measure("readout", "APD", time_tagging.analog(times[3], meas_len, counts[3]))
            save(counts[3], counts_st[3])  # save counts

            wait(wait_between_runs * u.ns, "AOM")
            align()
            # Measure dark counts
            # first two measurements
            play("laser_ON", "AOM",
                 duration=initialization_len * u.ns + 100 * u.ns)  # adding 100ns for some extra buffer time
            measure("readout", "APD", time_tagging.analog(times[4], meas_len, counts[4]))
            save(counts[4], counts_st[4])  # save counts
            wait((initialization_len - 2 * meas_len) * u.ns, "APD")
            measure("readout", "APD", time_tagging.analog(times[5], meas_len, counts[5]))
            save(counts[5], counts_st[5])  # save counts

            align()
            if wait_pulse_time_for_background_measuremenets:
                if start_from_one:  # Choose to start either from |0> or |1>
                    play("x180" * amp(0), "NV")
            wait(t, "NV")  # variable delay in spin Echo
            align()  # Play the laser pulse after the mw sequence

            # second two measurements
            play("laser_ON", "AOM",
                 duration=initialization_len * u.ns + 100 * u.ns)  # adding 100ns for some extra buffer time
            measure("readout", "APD", time_tagging.analog(times[6], meas_len, counts[6]))
            save(counts[6], counts_st[6])  # save counts
            wait((initialization_len - 2 * meas_len) * u.ns, "APD")
            measure("readout", "APD", time_tagging.analog(times[7], meas_len, counts[7]))
            save(counts[7], counts_st[7])  # save counts

            wait(wait_between_runs * u.ns, "AOM")

        save(n, n_st)  # save number of iteration inside for_loop

    with stream_processing():
        # Cast the data into a 1D vector, average the 1D vectors together and store the results on the OPX processor
        for i in range(8):
            counts_st[i].buffer(len(t_vec)).average().save(f"counts{i + 1}")
        n_st.save("iteration")

#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(host=qop_ip, cluster_name=cluster_name, octave=octave_config)

#######################
# Simulate or execute #
#######################
simulate = True

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=10_000)  # In clock cycles = 4ns
    # Simulate blocks python until the simulation is done
    job = qmm.simulate(config, T1, simulation_config)
    # Get the simulated samples
    samples = job.get_simulated_samples()
    # Plot the simulated samples
    samples.con1.plot()
    # Get the waveform report object
    waveform_report = job.get_simulated_waveform_report()
    # Cast the waveform report to a python dictionary
    waveform_dict = waveform_report.to_dict()
    # Visualize and save the waveform report
    waveform_report.create_plot(samples, plot=True, save_path=str(Path(__file__).resolve()))
else:
    # Open the quantum machine
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(T1)
    # Get results from QUA program
    results = fetching_tool(job, data_list=["counts1", "counts2", "counts3", "counts4", "counts5", "counts6", "counts7", "counts8", "iteration"], mode="live")
    # Live plotting
    fig = plt.figure()
    interrupt_on_close(fig, job)  # Interrupts the job when closing the figure

    while results.is_processing():
        # Fetch results
        counts1, counts2, counts3, counts4, counts5, counts6, counts7, counts8, iteration = results.fetch_all()
        # Progress bar
        progress_counter(iteration, n_avg, start_time=results.get_start_time())
        counts = (counts3 - counts4) / (counts1 - counts2)
        counts_dark = (counts7 - counts8) / (counts5 - counts6)
        # Plot data
        plt.cla()
        plt.plot(4 * t_vec, counts / 1000 / (meas_len / u.s), label=f"counts starting from  {'|1>' if start_from_one else '|0>'}")
        plt.plot(4 * t_vec, counts_dark / 1000 / (meas_len / u.s), label="dark counts")
        plt.xlabel("Wait time [ns]")
        plt.ylabel("Intensity [kcps]")
        plt.title(f"T1 - starting from  {'|1>' if start_from_one else '|0>'}")
        plt.legend()
        plt.pause(0.1)
    # Save results
    script_name = Path(__file__).name
    data_handler = DataHandler(root_data_folder=save_dir)
    save_data_dict.update({"counts1_data": counts})
    save_data_dict.update({"counts_dark_data": counts_dark})
    save_data_dict.update({"fig_live": fig})
    data_handler.additional_files = {script_name: script_name, **default_additional_files}
    data_handler.save_data(data=save_data_dict, name="_".join(script_name.split("_")[1:]).split(".")[0])
