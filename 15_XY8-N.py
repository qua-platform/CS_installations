from qm import QuantumMachinesManager
from qm.qua import *
from qm import SimulationConfig
import matplotlib.pyplot as plt
from configuration import *
from qualang_tools.loops import from_array
from qualang_tools.results.data_handler import DataHandler

###################
# The QUA program #
###################

# The time vector for varying the idle time in clock cycles (4ns)
t_vec = np.arange(4, 500, 20)
n_avg = 1_000_000
N = 2
readout_len = meas_len_1

##################
#  Date to save  #
##################
save_data_dict = {
    "n_avg": n_avg,
    "N": N,
    "t_vec": t_vec,
    "config": config,
}

def xy8(t):
    play("x180", "NV")
    wait(2 * t, "NV")
    play("y180", "NV")
    wait(2 * t, "NV")
    play("x180", "NV")
    wait(2 * t, "NV")
    play("y180", "NV")
    wait(2 * t, "NV")
    play("y180", "NV")
    wait(2 * t, "NV")
    play("x180", "NV")
    wait(2 * t, "NV")
    play("y180", "NV")
    wait(2 * t, "NV")
    play("x180", "NV")

with program() as correlation_meas:
    counts = declare(int)  # saves number of photon counts
    counts_dark = declare(int)  # saves number of photon counts
    times = declare(int, size=100)  # QUA vector for storing the time-tags
    t = declare(int)  # variable to sweep over in time
    n = declare(int)  # variable to for_loop
    i = declare(int)  # variable to for_loop
    counts_st = declare_stream()  # stream for counts
    n_st = declare_stream()  # stream to save iterations


    # XY8-N sequence
    play("trigger", "laser")  # 3us duration - Spin initialization for first iteration
    with for_(n, 0, n < n_avg, n + 1):
        with for_(*from_array(t, t_vec)):
            wait(100, "NV")

            play("x90", "NV")  # Pi/2 pulse to qubit
            wait(t, "NV")

            align()
            with for_(i, 0, i<N, i+1):
                xy8(t)
                wait(2*t)
            wait(t, "NV")
            play("x90", "NV")  # Pi/2 pulse to qubit

            align()  # Play the laser pulse after the XY8-N sequence
            wait(100, "laser", "APD")

            # Measure and detect the photons on APD
            play("trigger", "laser")  # 3us duration - for measurement and Spin initialization for the next iteration
            measure("readout", "APD", None, time_tagging.analog(times, readout_len, counts))
            save(counts, counts_st)  # save counts
            wait(wait_between_runs * u.ns)

        save(n, n_st)  # save number of iteration inside for_loop

    with stream_processing():
        # Cast the data into a 1D vector, average the 1D vectors together and store the results on the OPX processor
        counts_st.buffer(len(t_vec)).average().save("counts")
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
    job = qmm.simulate(config, correlation_meas, simulation_config)
    job.get_simulated_samples().con1.plot()
else:
    # Open the quantum machine
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it
    # execute QUA program
    job = qm.execute(correlation_meas)
    # Get results from QUA program
    results = fetching_tool(job, data_list=["counts", "iteration"], mode="live")
    # Live plotting
    fig = plt.figure()
    interrupt_on_close(fig, job)  # Interrupts the job when closing the figure

    while results.is_processing():
        # Fetch results
        counts, iteration = results.fetch_all()
        # Progress bar
        progress_counter(iteration, n_avg, start_time=results.get_start_time())
        # Plot data
        plt.cla()
        plt.plot(4 * t_vec, counts / 1000 / (readout_len / u.s))
        plt.xlabel("idle time [ns]")
        plt.ylabel("Intensity [kcps]")
        plt.title("Correlation measurement")
        plt.legend()
        plt.pause(0.1)

    # Save results
    script_name = Path(__file__).name
    data_handler = DataHandler(root_data_folder=save_dir)
    save_data_dict.update({"fig_live": fig})
    data_handler.additional_files = {script_name: script_name}
    data_handler.save_data(data=save_data_dict, name="XY8-N")
