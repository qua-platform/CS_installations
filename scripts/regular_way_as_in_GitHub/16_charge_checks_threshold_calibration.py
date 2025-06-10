
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

# Data to save
save_data_dict = {
    "n_avg": n_avg,
    "config": config,
}
n_readouts = 10
###################
# The QUA program #
###################
with program() as optical_pumping:
    times = declare(int, size=100)  # QUA vector for storing the time-tags
    counts = declare(int)  # variable for number of counts
    counts_st = declare_stream()  # stream for counts
    i = declare(int)  # number of iterations
    n = declare(int)  # number of iterations
    n_st = declare_stream()  # stream for number of iterations
    time_stamps = declare_stream()
    with for_(n, 0, n < n_avg, n + 1):
        # Play the laser pulse...
        play("laser_ON", "AOM", duration=(readout_len * n_readouts + 1_000 + 10_000) * u.ns) # 1_000 for the wait time and 10_000 extra time due to analysis time
        play("laser_ON", "repump_AOM", duration=(readout_len * n_readouts + 1_000 + 10_000) * u.ns) # 1_000 for the wait time and 10_000 extra time due to analysis time
        # ... and the laser pulse simultaneously (the laser pulse is delayed by 'laser_delay_1')
        wait(1_000 * u.ns, "APD")  # so readout don't catch the first part of spin reinitialization
        with for_(i, 0, i < n_readouts, i+1):
            measure("readout", "APD", time_tagging.analog(times, readout_len, counts))

            save(counts, counts_st)  # save counts on stream


        save(n, n_st)  # save number of iteration inside for_loop

    with stream_processing():
        # Cast the data into a 1D vector, average the 1D vectors together and store the results on the OPX processor
        counts_st.buffer(n_readouts).average().save("counts")
        counts_st.timestamps().buffer(n_readouts).save("time_stamps")
        n_st.save("iteration")

#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(host=qop_ip, cluster_name=cluster_name)

#######################
# Simulate or execute #
#######################
simulate = True

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=10_000)  # In clock cycles = 4ns
    # Simulate blocks python until the simulation is done
    job = qmm.simulate(config, optical_pumping, simulation_config)
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
    job = qm.execute(optical_pumping)

    # Get results from QUA program
    results = fetching_tool(job, data_list=["counts", "time_stamps", "iteration"], mode="live")
    # Live plotting
    fig = plt.figure()
    interrupt_on_close(fig, job)  # Interrupts the job when closing the figure

    while results.is_processing():
        # Fetch results
        counts, times, iteration = results.fetch_all()
        # Progress bar
        progress_counter(iteration, n_avg, start_time=results.get_start_time())
        # Plot data
        plt.cla()
        plt.plot(times - times[0], counts / 1000 / (readout_len * 1e-9), label="photon counts")
        plt.xlabel("Duration [ns]")
        plt.ylabel("Intensity [kcps]")
        plt.title("Optical Pumping")
        plt.legend()
        plt.pause(0.1)
    # Save results
    script_name = Path(__file__).name
    data_handler = DataHandler(root_data_folder=save_dir)
    save_data_dict.update({"counts_data": counts})
    save_data_dict.update({"fig_live": fig})
    data_handler.additional_files = {script_name: script_name, **default_additional_files}
    data_handler.save_data(data=save_data_dict, name="_".join(script_name.split("_")[1:]).split(".")[0])
