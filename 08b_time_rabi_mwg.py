"""
    TIME RABI
    
    Measure photon count while varying the pulse duration of the applied mwe MWe pulse
    
"""

from qm import QuantumMachinesManager
from qm.qua import *
from qm import SimulationConfig
import matplotlib.pyplot as plt
from configuration_princeton_groundwork_with_octave import *
from qualang_tools.loops import from_array

###################
# The QUA program #
###################

tau_min = 100
tau_max = 1000
dtau = 10
taus = np.arange(tau_min, tau_max, dtau)

n_avg = 100
init_rep = 50
readout_rep = 250

with program() as time_rabi:

    times = declare(int, size=100)
    counts = declare(int)  # variable for number of counts
    total_counts = declare(int)
    counts_st = declare_stream()  # stream for counts

    t = declare(int)
    n = declare(int)  # number of iterations
    i = declare(int)
    j = declare(int)
    n_st = declare_stream()  # stream for number of iterations

    with for_(n, 0, n < n_avg, n + 1):

        with for_(*from_array(t, taus)):

            # initialization loop
            with for_(i, 0, i < init_rep, i + 1):

                play("AOM_ON", "AOM")
                play("laser_ON", "OpticalTrigger")
                play("cw", "EOM_A")

                # Pulse for excited spin flip
                wait((RF_switch_len >> 2), "RF_switch")
                play("RF_ON", "RF_switch")
                wait((RF_switch_len >> 2), "mwe")
                play("pi", "mwe")  # play microwave pulse

            align()  # align all elements
            # Long_readout duration and time tagging meas_len needs to be longer than readout_rep loop duration

            # Play the ground state spin transistion pulse for duration t
            play("RF_ON", "RF_switch", duration = t)
            play("cw", "mwg", duration = t)

            align()

            # Readout flashing loop
            with for_(j, 0, j < readout_rep, j + 1):

                # Begin readout, readout len and meas_length must be longer than each iteration
                measure(
                    "readout",
                    "SNSPD",
                    None,
                    time_tagging.analog(times, meas_len, counts),
                )

                # Drive A and B Transistions repetitively during readout
                play("cw", "EOM_A")
                play("AOM_ON", "AOM")
                play("laser_ON", "OpticalTrigger")

                align("EOM_A", "EOM_B")

                play("cw", "EOM_B")
                play("AOM_ON", "AOM")
                play("laser_ON", "OpticalTrigger")

                assign(total_counts, total_counts + counts)

            save(total_counts, counts_st)  # save counts on stream
            assign(total_counts, 0)

        save(n, n_st)  # save number of iteration inside for_loop

    with stream_processing():
        counts_st.buffer(len(taus)).average().save("counts")
        n_st.save("iteration")

#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(host=qop_ip, port=qop_port, cluster_name=cluster_name)

simulate = False
if simulate:
    simulation_config = SimulationConfig(duration=40000)
    job = qmm.simulate(config, time_rabi, simulation_config)

    samples = job.get_simulated_samples()
    waveform_report = job.get_simulated_waveform_report()
    waveform_report.create_plot(samples, plot=True, save_path=None)

    job.get_simulated_samples().con1.plot()
    plt.show()
else:
    qm = qmm.open_qm(config)

    job = qm.execute(time_rabi)  # execute QUA program

    # Get results from QUA program
    results = fetching_tool(job, data_list=["counts", "iteration"], mode="live")

    # Live plotting
    fig = plt.figure()
    interrupt_on_close(fig, job)  # Interrupts the job when closing the figure

    while results.is_processing():

        # Fetch results
        counts, iteration = results.fetch_all()
        print(counts.shape)
        # Progress bar
        progress_counter(iteration, n_avg, start_time=results.get_start_time())
        # Plot data
        plt.cla()
        plt.plot((taus) / u.ns, counts / 1000 / (meas_len * 1e-9))
        plt.xlabel("MWg duration [ns]")
        plt.ylabel("Intensity [kcps]")
        plt.title("ODMR")

        plt.pause(0.1)
