"""
        EOM Time rabi
Once the magnetic field value is found and an EOM frequency is found for either the A or B transistion, this
script plays a laser tone with varied duration to determine when photon begin being emitted to determine appropriate pulse
timings

Next steps before going to the next node:
    - Replace the relevant determined pulse durations for for EOM_A, EOM_B pi and pi_half pulses
"""

from qm import QuantumMachinesManager
from qm.qua import *
from qm import SimulationConfig
import matplotlib.pyplot as plt
from configuration_princeton_groundwork_with_octave import *
from qualang_tools.loops import from_array
from qualang_tools.results import wait_until_job_is_paused

tau_min = 40 // 4 #in ns
tau_max = 2000 // 4 # in ns
dtau = 16 // 4 # in ns
taus = np.arange(tau_min, tau_max, dtau)

n_avg = 1

integration_len = (tau_max * 4 + 200)  # in ns, time_tagging must always be longer than pulse duration

# Time vector for plotting
t_vec = np.arange(0, meas_len, 1)

# Run the QUA program for each externally set magnetic field value

with program() as EOM_sweep:

    t = declare(int)
    times = declare(int, size=100)  # 'size' defines the max number of photons to be counted
    # times_st = declare_stream()  # stream for 'times'
    counts = declare(int)  # variable for number of counts
    counts_st = declare_stream()  # stream for counts
    total_counts = declare(int)
    n = declare(int)  # number of iterations
    #i = declare(int)
    n_st = declare_stream()  # stream for number of iterations

    with for_(*from_array(t, taus)):

        with for_(n, 0, n < n_avg, n + 1):

            play("AOM_ON", "AOM", duration=t)
            play("laser_ON", "OpticalTrigger", duration=t)
            play("cw", "EOM", duration=t)

            # Make sure readout len is the same as tau max
            measure("readout","SNSPD",None,time_tagging.analog(times, integration_len, counts))

            # Save to counts stream and reset for next iteration of the infinite loop
            save(counts, counts_st)

            save(n, n_st)  # save number of iteration inside for_loop


    with stream_processing():
        counts_st.buffer(n_avg).map(FUNCTIONS.average()).buffer(len(taus)).save("counts")
        n_st.save("iteration")

#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(host=qop_ip, port=qop_port, cluster_name=cluster_name)

simulate = True

if simulate:

    simulation_config = SimulationConfig(duration=28000)
    job = qmm.simulate(config, EOM_sweep, simulation_config)

    # Get the waveform report
    samples = job.get_simulated_samples()
    waveform_report = job.get_simulated_waveform_report()
    waveform_report.create_plot(samples, plot=True, save_path=None)

    # Plot simulated waveforms
    job.get_simulated_samples().con1.plot()
    plt.show()

else:
    qm = qmm.open_qm(config)

    job = qm.execute(EOM_sweep)

    # Live plotting
    fig = plt.figure()
    interrupt_on_close(fig, job)  # Interrupts the job when closing the figure


    results = fetching_tool(job, data_list=["counts", "iteration"], mode="live")

    while results.is_processing():
        # Fetch results
        counts, iteration = results.fetch_all()
        # Progress bar
        progress_counter(iteration, n_avg, start_time=results.get_start_time())
        # Plot data
        plt.cla()
        plt.plot(taus / u.ns, counts / integration_len / 1000)
        plt.xlabel("Pulse length [ns]")
        plt.ylabel("Counts")
        plt.title("Counts vs time")
        plt.pause(0.1)
        print(counts.shape, iteration.shape)
