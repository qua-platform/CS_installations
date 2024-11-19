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

def sequence(tau):
    play("x180", "NV")
    play("RF", "Spin")
    wait(tau, "NV", "Spin")
    play("y180", "NV")
    play("RF", "Spin")
    wait(tau, "NV", "Spin")
    play("x180", "NV")
    play("RF", "Spin")
    wait(tau, "NV", "Spin")
    play("y180", "NV")
    play("RF", "Spin")
    wait(tau, "NV", "Spin")
    play("y180", "NV")
    play("RF", "Spin")
    wait(tau, "NV", "Spin")
    play("x180", "NV")
    play("RF", "Spin")
    wait(tau, "NV", "Spin")
    play("y180", "NV")
    play("RF", "Spin")
    wait(tau, "NV", "Spin")
    play("x180", "NV")
    play("RF", "Spin")

with program() as cpmg_deer:
    counts1 = declare(int)  # saves number of photon counts
    counts2 = declare(int)  # saves number of photon counts
    times = declare(int, size=100)  # QUA vector for storing the time-tags
    t = declare(int)  # variable to sweep over in time
    n = declare(int)  # variable to for_loop
    counts1_st = declare_stream()  # stream for counts
    counts2_st = declare_stream()  # stream for counts
    n_st = declare_stream()  # stream to save iterations


    # CPMG DEER sequence
    play("trigger", "laser")  # 3us duration - Spin initialization for first iteration
    with for_(n, 0, n < n_avg, n + 1):
        with for_(*from_array(t, t_vec)):
            wait(100, "NV")

            play("x90", "NV")  # Pi/2 pulse to qubit
            align()
            wait(t, "NV", "Spin")
            sequence(2*t) #number of times will tell us how much we are coupled to nuclear spins
            wait(2*t)
            sequence(2*t)
            wait(t, "NV")
            play("x90", "NV")  # Pi/2 pulse to qubit

            align()  # Play the laser pulse after the CPMG DEER sequence
            wait(100, "laser", "APD")

            # Measure and detect the photons on APD
            play("trigger", "laser")  # 3us duration - for measurement and Spin initialization for the next measurement
            measure("readout", "APD", None, time_tagging.analog(times, readout_len, counts1))
            save(counts1, counts1_st)  # save counts

            # Wait and align all elements
            wait(wait_between_runs * u.ns)
            align()  # align all elements

            wait(100, "NV")

            play("x90", "NV")  # Pi/2 pulse to qubit
            align()
            wait(t, "NV", "Spin")
            sequence(2 * t)  # number of times will tell us how much we are coupled to nuclear spins
            wait(2 * t)
            sequence(2 * t)
            wait(t)
            play("-x90", "NV")  # Pi/2 pulse to qubit

            align()  # Play the laser pulse after the sequence
            # Measure and detect the photons on APD
            wait(100, "laser", "APD")

            # Measure and detect the photons on APD
            play("trigger", "laser")  # 3us duration - for measurement and Spin initialization for the next iteration
            measure("readout", "APD", None, time_tagging.analog(times, readout_len, counts2))
            save(counts2, counts2_st)  # save counts
            wait(wait_between_runs * u.ns, "laser")


        save(n, n_st)  # save number of iteration inside for_loop

    with stream_processing():
        # Cast the data into a 1D vector, average the 1D vectors together and store the results on the OPX processor
        counts1_st.buffer(len(t_vec)).average().save("counts1")
        counts2_st.buffer(len(t_vec)).average().save("counts2")

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
    job = qmm.simulate(config, cpmg_deer, simulation_config)
    job.get_simulated_samples().con1.plot()
else:
    # Open the quantum machine
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it
    # execute QUA program
    job = qm.execute(cpmg_deer)
    # Get results from QUA program
    results = fetching_tool(job, data_list=["counts1", "counts2", "iteration"], mode="live")
    # Live plotting
    fig = plt.figure()
    interrupt_on_close(fig, job)  # Interrupts the job when closing the figure

    while results.is_processing():
        # Fetch results
        counts1, counts2, iteration = results.fetch_all()
        # Progress bar
        progress_counter(iteration, n_avg, start_time=results.get_start_time())
        # Plot data
        plt.cla()
        plt.plot(4 * 2 * 7 * t_vec, counts1 / 1000 / (readout_len / u.s), label="x90_XY8+RF_x90")
        plt.plot(4 * 2 * 7 * t_vec, counts2 / 1000 / (readout_len / u.s), label="x90_XY8+RF_-x90")
        plt.xlabel("14 * idle time [ns]")
        plt.ylabel("Intensity [kcps]")
        plt.title("CPMG DEER")
        plt.legend()
        plt.pause(0.1)
