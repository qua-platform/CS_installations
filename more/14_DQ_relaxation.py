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
t_vec = np.arange(4, 500, 20)
n_avg = 1_000_000
readout_len = long_meas_len

with program() as DQ_relaxation:
    counts1 = declare(int)  # saves number of photon counts
    counts2 = declare(int)  # saves number of photon counts
    counts3 = declare(int)  # saves number of photon counts
    counts4 = declare(int)  # saves number of photon counts
    times1 = declare(int, size=100)  # QUA vector for storing the time-tags
    times2 = declare(int, size=100)  # QUA vector for storing the time-tags
    times3 = declare(int, size=100)  # QUA vector for storing the time-tags
    times4 = declare(int, size=100)  # QUA vector for storing the time-tags
    t = declare(int)  # variable to sweep over in time
    n = declare(int)  # variable to for_loop
    counts_1_st = declare_stream()  # stream for counts
    counts_2_st = declare_stream()  # stream for counts
    counts_3_st = declare_stream()  # stream for counts
    counts_4_st = declare_stream()  # stream for counts
    n_st = declare_stream()  # stream to save iterations

    play("trigger", "laser")  # 3us duration - Spin initialization for first iteration
    with for_(n, 0, n < n_avg, n + 1):
        with for_(*from_array(t, t_vec)):
            # prepare in state |0>
            wait(100)
            align()
            # wait variable idle time
            wait(t, "laser", "APD")  # Variable idle time
            # measure
            wait(100, "laser", "APD")
            play("trigger", "laser")  # 3us duration - for measurement and Spin initialization for the next measurement
            measure("readout", "APD", None, time_tagging.analog(times1, readout_len, counts1))
            save(counts1, counts_1_st)
            wait(wait_between_runs * u.ns)

            align()

            # prepare in state |0>
            wait(100)
            align()
            # wait variable idle time
            wait(t, "NV_minus")  # Variable idle time
            # play pi-pulse
            play("x180", "NV_minus")
            align()
            # measure
            wait(100, "laser", "APD")
            play("trigger", "laser")  # 3us duration - for measurement and Spin initialization for the next measurement
            measure("readout", "APD", None, time_tagging.analog(times2, readout_len, counts2))
            save(counts2, counts_2_st)
            wait(wait_between_runs * u.ns)

            align()

            # prepare in state |1>
            wait(100)
            align()
            # play pi-pulse
            play("x180", "NV_minus")
            # wait variable idle time
            wait(t, "NV_minus")  # Variable idle time
            # play pi-pulse
            play("x180", "NV_minus")
            align()
            # measure
            wait(100, "laser", "APD")
            play("trigger", "laser")  # 3us duration - for measurement and Spin initialization for the next measurement
            measure("readout", "APD", None, time_tagging.analog(times3, readout_len, counts3))
            save(counts3, counts_3_st)
            wait(wait_between_runs * u.ns)

            align()

            # prepare in state |1>
            wait(100, "laser")
            align()
            # play pi-pulse
            play("x180", "NV_minus")
            # wait variable idle time
            align()
            wait(t, "NV")  # Variable idle time
            # play pi-pulse
            play("x180", "NV")
            align()
            # measure
            wait(100, "laser", "APD")
            play("trigger", "laser")  # 3us duration - for measurement and Spin initialization for the next iteration
            measure("readout", "APD", None, time_tagging.analog(times4, readout_len, counts4))
            save(counts4, counts_4_st)
            wait(wait_between_runs * u.ns)

        save(n, n_st)  # save number of iteration inside for_loop

    with stream_processing():
        # Cast the data into a 1D vector, average the 1D vectors together and store the results on the OPX processor
        counts_1_st.buffer(len(t_vec)).average().save("counts1")
        counts_2_st.buffer(len(t_vec)).average().save("counts2")
        counts_3_st.buffer(len(t_vec)).average().save("counts3")
        counts_4_st.buffer(len(t_vec)).average().save("counts4")
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
    job = qmm.simulate(config, DQ_relaxation, simulation_config)
    job.get_simulated_samples().con1.plot()
else:
    # Open the quantum machine
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it
    # execute QUA program
    job = qm.execute(DQ_relaxation)
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
        # Plot data
        plt.cla()
        plt.plot(4 * t_vec, (counts1-counts2) / 1000 / (readout_len / u.s), label="S$0,0$-S$0,-1$")
        plt.plot(4 * t_vec, (counts3-counts4) / 1000 / (readout_len / u.s), label="S$-1,-1$-S$-1,+1$")
        plt.xlabel("idle time [ns]")
        plt.ylabel("Intensity [kcps]")
        plt.title("Double-quantum relaxation")
        plt.legend()
        plt.pause(0.1)
