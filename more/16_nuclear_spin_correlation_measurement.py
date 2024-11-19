from qm import QuantumMachinesManager
from qm.qua import *
from qm import SimulationConfig
import matplotlib.pyplot as plt
from configuration import *
from qualang_tools.loops import from_array

###################
# The QUA program #
###################

# The time vector for varying the idle time in XY8 in clock cycles (4ns)
t_vec = np.arange(4, 500, 200)
# The time vector for varying the idle time between two XY8 sequences in clock cycles (4ns)
tau_vec = np.arange(4, 500, 20)
n_avg = 1_000_000
readout_len = long_meas_len
N = 2
t_larmor = 40
def xy8(t_larmor):
    play("x180", "NV")
    wait(2 * t_larmor, "NV")
    play("y180", "NV")
    wait(2 * t_larmor, "NV")
    play("x180", "NV")
    wait(2 * t_larmor, "NV")
    play("y180", "NV")
    wait(2 * t_larmor, "NV")
    play("y180", "NV")
    wait(2 * t_larmor, "NV")
    play("x180", "NV")
    wait(2 * t_larmor, "NV")
    play("y180", "NV")
    wait(2 * t_larmor, "NV")
    play("x180", "NV")
with program() as correlation_meas:
    counts = declare(int)  # saves number of photon counts
    counts_dark = declare(int)  # saves number of photon counts
    times = declare(int, size=100)  # QUA vector for storing the time-tags
    t = declare(int)  # variable to sweep over in time
    tau = declare(int)  # variable to sweep over in time
    n = declare(int)  # variable to for_loop
    i = declare(int)  # variable to for_loop
    counts_st = declare_stream()  # stream for counts
    n_st = declare_stream()  # stream to save iterations


    # Nuclear Spin Correlation sequence
    play("trigger", "laser")  # 3us duration - Spin initialization for first iteration
    with for_(n, 0, n < n_avg, n + 1):
        with for_(*from_array(tau, tau_vec)):
            wait(100, "NV")
            align()

            play("y90", "NV")  # Pi/2 pulse to qubit
            wait(t_larmor, "NV")
            with for_(i, 0, i < N, i + 1):
                xy8(t_larmor)
                wait(2 * t_larmor)
            wait(tau, "NV")
            with for_(i, 0, i < N, i + 1):
                xy8(t_larmor)
                wait(2 * t_larmor)
            wait(t_larmor, "NV")
            play("y90", "NV")  # Pi/2 pulse to qubit

            align()  # Play the laser pulse after the Echo sequence
            wait(100, "laser", "APD")

            # Measure and detect the photons on APD
            play("trigger", "laser")  # 3us duration - for measurement and Spin initialization for the next iteration
            measure("readout", "APD", None, time_tagging.analog(times, readout_len, counts))
            save(counts, counts_st)  # save counts
            wait(wait_between_runs * u.ns)

        save(n, n_st)  # save number of iteration inside for_loop

    with stream_processing():
        # Cast the data into a 1D vector, average the 1D vectors together and store the results on the OPX processor
        counts_st.buffer(len(tau_vec)).average().save("counts")
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

