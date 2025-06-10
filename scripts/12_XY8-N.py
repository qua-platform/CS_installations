from qm import QuantumMachinesManager
from qm.qua import *
from qm import SimulationConfig
import matplotlib.pyplot as plt
from configuration import *
from qualang_tools.loops import from_array

###################
# The QUA program #
###################

# The time vector for varying the idle time in clock cycles (4ns)
t_vec = np.arange(x180_len_NV//4 + 4, 500, 20)
n_avg = 1_000_000
N = 2
readout_len = long_meas_len

def xy8(t):
    play("x180", "NV")
    wait(2 * t - x180_len_NV//4, "NV")
    play("y180", "NV")
    wait(2 * t - x180_len_NV//4, "NV")
    play("x180", "NV")
    wait(2 * t - x180_len_NV//4, "NV")
    play("y180", "NV")
    wait(2 * t - x180_len_NV//4, "NV")
    play("y180", "NV")
    wait(2 * t - x180_len_NV//4, "NV")
    play("x180", "NV")
    wait(2 * t - x180_len_NV//4, "NV")
    play("y180", "NV")
    wait(2 * t - x180_len_NV//4, "NV")
    play("x180", "NV")

with program() as correlation_meas:
    counts = [declare(int) for i in range(4)]  # variable for number of counts
    counts_st = [declare_stream() for i in range(4)]  # stream for counts
    times = [declare(int, size=100) for i in range(4)]  # QUA vector for storing the time-tags
    times_st = [declare_stream() for i in range(4)]  # stream for counts
    t = declare(int)  # variable to sweep over in time
    n = declare(int)  # variable to for_loop
    i = declare(int)  # variable to for_loop
    n_st = declare_stream()  # stream to save iterations


    # XY8-N sequence
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

            play("x90", "NV")  # Pi/2 pulse to qubit
            wait(t - x180_len_NV//8, "NV")

            align()
            with for_(i, 0, i<N, i+1):
                xy8(t)
                wait(2 * t - x180_len_NV//4)
            wait(t - x180_len_NV//8, "NV")
            play("x90", "NV")  # Pi/2 pulse to qubit

            align()  # Play the laser pulse after the XY8-N sequence

            # second two measurements
            play("laser_ON", "AOM",
                 duration=initialization_len * u.ns + 100 * u.ns)  # adding 100ns for some extra buffer time
            measure("readout", "APD", time_tagging.analog(times[2], meas_len, counts[2]))
            save(counts[2], counts_st[2])  # save counts
            wait((initialization_len - 2 * meas_len) * u.ns, "APD")
            measure("readout", "APD", time_tagging.analog(times[3], meas_len, counts[3]))
            save(counts[3], counts_st[3])  # save counts

            wait(wait_between_runs * u.ns)

        save(n, n_st)  # save number of iteration inside for_loop

    with stream_processing():
        # Cast the data into a 1D vector, average the 1D vectors together and store the results on the OPX processor
        for i in range(4):
            counts_st[i].buffer(len(t_vec)).average().save(f"counts{i + 1}")
        n_st.save("iteration")

#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(host=qop_ip, cluster_name=cluster_name, octave=octave_config)

#######################
# Simulate or execute #
#######################
simulate = False

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
    results = fetching_tool(job, data_list=["counts1", "counts2", "counts3", "counts4", "iteration"], mode="live")
    # Live plotting
    fig = plt.figure()
    interrupt_on_close(fig, job)  # Interrupts the job when closing the figure

    while results.is_processing():
        # Fetch results
        counts1, counts2, counts3, counts4, iteration = results.fetch_all()
        # Progress bar
        progress_counter(iteration, n_avg, start_time=results.get_start_time())
        counts = (counts3 - counts4) / (counts1 - counts2)
        # Plot data
        plt.cla()
        plt.plot(4 * t_vec, counts / 1000 / (meas_len / u.s))
        plt.xlabel("idle time [ns]")
        plt.ylabel("Intensity [kcps]")
        plt.title("Correlation measurement")
        plt.legend()
        plt.pause(0.1)
