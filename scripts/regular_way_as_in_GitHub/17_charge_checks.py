
from qm import QuantumMachinesManager
from qm.qua import *
from qm import SimulationConfig
import matplotlib.pyplot as plt
from configuration import *
from qualang_tools.results.data_handler import DataHandler

##################
#   Parameters   #
##################
# Parameters Definition
n_avg = 1_000_000  # number of averages
readout_len = meas_len  # Readout duration for this experiment
a_vec = np.arange(0.1, 1, 0.02)  # The amplitude pre-factor vector
# Data to save
save_data_dict = {
    "n_avg": n_avg,
    "a_vec": a_vec,
    "config": config,
}
n_readouts = 10
charge_checks = True
###################
# The QUA program #
###################
with program() as power_rabi_with_charge_checks:
    a = declare(fixed)  # variable to sweep over the amplitude
    times = declare(int, size=100)  # QUA vector for storing the time-tags
    counts = declare(int)  # variable for number of counts
    counts_t = declare(int)  # variable for number of counts
    counts_st = declare_stream()  # stream for counts
    counts_dark_st = declare_stream()  # stream for counts
    i = declare(int)  # number of iterations
    n = declare(int)  # number of iterations
    counter = declare(int)  # number of iterations
    n_st = declare_stream()  # stream for number of iterations
    time_stamps = declare_stream()
    assign(counter, 0)
    with for_(n, 0, n < n_avg, n + 1):
        with for_(*from_array(a, a_vec)):
            if charge_checks:
                with while_((counts < charge_checks_threshold) & (counter < max_tries)):
                    play("laser_ON", "AOM", duration=(readout_len + 1_000) * u.ns)  # 1_000 for the wait time
                    play("laser_ON", "repump_AOM", duration=(readout_len + 1_000) * u.ns)  # 1_000 for the wait time
                    measure("readout", "APD", time_tagging.analog(times, readout_len, counts))
                    assign(counter, counter + 1)
                with if_(counts < charge_checks_threshold):
                    pause()
                align()
            # Play the Rabi pulse with varying amplitude
            play("x180" * amp(a), "NV")  # 'a' is a pre-factor to the amplitude defined in the config ("mw_amp_NV")
            align()  # Play the laser pulse after the mw pulse
            play("laser_ON", "AOM")
            # Measure and detect the photons on APD
            measure("readout", "APD", time_tagging.analog(times, meas_len, counts))
            save(counts, counts_st)  # save counts

            # Wait and align all elements before measuring the dark events
            wait(wait_between_runs * u.ns)
            align()

            # Play the Rabi pulse with zero amplitude
            play("x180" * amp(0), "NV")
            align()  # Play the laser pulse after the mw pulse
            play("laser_ON", "AOM")
            # Measure and detect the dark counts on APD
            measure("readout", "APD", time_tagging.analog(times, meas_len, counts))
            save(counts, counts_dark_st)  # save dark counts
            wait(wait_between_runs * u.ns)  # wait in between iterations
        save(n, n_st)  # save number of iteration inside for_loop

    with stream_processing():
        # Cast the data into a 1D vector, average the 1D vectors together and store the results on the OPX processor
        counts_st.buffer(len(a_vec)).average().save("counts")
        counts_dark_st.buffer(len(a_vec)).average().save("counts_dark")
        n_st.save("iteration")
#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(host=qop_ip, cluster_name=cluster_name)

#######################
# Simulate or execute #
#######################
simulate = False

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=10_000)  # In clock cycles = 4ns
    # Simulate blocks python until the simulation is done
    job = qmm.simulate(config, power_rabi_with_charge_checks, simulation_config)
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
    job = qm.execute(power_rabi_with_charge_checks)
    # Get results from QUA program
    if job.is_paused():
        job.cancel()
        print(f"the number of counts is lower than the threshold. Number of tries:{max_tries}")
        print("here")

    results = fetching_tool(job, data_list=["counts", "counts_dark", "iteration"], mode="live")
    # Live plotting
    fig = plt.figure()
    interrupt_on_close(fig, job)  # Interrupts the job when closing the figure

    while results.is_processing():
        if job.is_paused():
            job.cancel()
            print(f"the number of counts is lower than the threshold. Number of tries:{max_tries}")
        # Fetch results
        counts, counts_dark, iteration = results.fetch_all()
        # Progress bar
        progress_counter(iteration, n_avg, start_time=results.get_start_time())
        # Plot data
        plt.cla()
        plt.plot(a_vec * x180_amp_NV, counts / 1000 / (meas_len * 1e-9), label="photon counts")
        plt.plot(a_vec * x180_amp_NV, counts_dark / 1000 / (meas_len * 1e-9), label="dark_counts")
        plt.xlabel("Rabi pulse amplitude [V]")
        plt.ylabel("Intensity [kcps]")
        plt.title("Power Rabi")
        plt.legend()
        plt.pause(0.1)
    # Save results
    script_name = Path(__file__).name
    data_handler = DataHandler(root_data_folder=save_dir)
    save_data_dict.update({"counts_data": counts})
    save_data_dict.update({"counts_dark_data": counts_dark})
    save_data_dict.update({"fig_live": fig})
    data_handler.additional_files = {script_name: script_name, **default_additional_files}
    data_handler.save_data(data=save_data_dict, name="_".join(script_name.split("_")[1:]).split(".")[0])
