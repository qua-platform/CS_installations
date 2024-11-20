"""
    Hahn Echo
    
    Measure photon count while varying the pulse duration of the applied optical laser
    
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

tau_min = 4  # In clock cycle units
tau_max = 500
dtau = 20
taus = np.arange(tau_min, tau_max, dtau)

n_avg = 100
init_rep = 50
readout_rep = 250

with program() as hahn_echo:

    times = declare(int, size=100)
    counts_1 = declare(int)  # variable for number of counts
    counts_2 = declare(int)
    total_counts_1 = declare(int)
    total_counts_2 = declare(int)
    counts_1_st = declare_stream()  # stream for counts
    counts_2_st = declare_stream()
    t = declare(int)
    f = declare(int)
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
                play("RF_ON", "RF_switch")
                play("cw", "EOM_A")

                # Pulse for excited spin flip
                wait((RF_switch_len >> 2), "mwe")
                play("pi", "mwe")  # play microwave pulse

            align()  # align all elements

            # begin Ramsey sequence, play 1st pi_half pulse
            play("RF_ON", "RF_switch", duration = mwg_pi_half_len)
            play("pi_half", "mwg")
            # wait a varying idle 1
            wait(t, "mwg", "RF_switch")
            # play pi pulse
            play("RF_ON", "RF_switch", duration = mwg_pi_len)
            play("pi", "mwg")
            # wait a varying idle 2
            wait(t, "mwg", "RF_switch")
            # Play second pi_half pulse
            play("RF_ON", "RF_switch", duration = mwg_pi_half_len)
            play("pi_half", "mwg")

            align()

            with for_(j, 0, j < readout_rep, j + 1):

                # Begin readout, readout len and meas_length must be longer than each iteration
                measure(
                    "readout",
                    "SNSPD",
                    None,
                    time_tagging.analog(times, meas_len, counts_1),
                )

                # Drive A and B Transistions repetitively during readout
                play("cw", "EOM_A")
                play("AOM_ON", "AOM")
                play("laser_ON", "OpticalTrigger")

                align("EOM_A", "EOM_B")

                play("cw", "EOM_B")
                play("AOM_ON", "AOM")
                play("laser_ON", "OpticalTrigger")

                assign(total_counts_1, total_counts_1 + counts_1)

            #########################################################################################
            #########################################################################################

            # initialization loop
            with for_(i, 0, i < init_rep, i + 1):

                play("AOM_ON", "AOM")
                play("laser_ON", "OpticalTrigger")
                play("RF_ON", "RF_switch")
                play("cw", "EOM_A")

                # Pulse for excited spin flip
                wait((RF_switch_len >> 2), "mwe")
                play("pi", "mwe")  # play microwave pulse

            align()  # align all elements

            # begin second sequence, play 1st pi_half pulse
            play("RF_ON", "RF_switch", duration = mwg_pi_half_len)
            play("pi_half", "mwg")
            # wait a varying idle 1
            wait(t, "mwg", "RF_switch")
            # play pi pulse
            play("RF_ON", "RF_switch", duration = mwg_pi_len)
            play("pi", "mwg")
            # wait a varying idle 2
            wait(t, "mwg","RF_switch")
            frame_rotation_2pi(0.5, "mwg")  # Turns next pulse to -x
            # Play second pi_half pulse
            play("RF_ON", "RF_switch", duration = mwg_pi_half_len)
            play("pi_half", "mwg")
            reset_frame("mwg")

            align()

            with for_(j, 0, j < readout_rep, j + 1):

                # Begin readout, readout len and meas_length must be longer than each iteration
                measure(
                    "readout",
                    "SNSPD",
                    None,
                    time_tagging.analog(times, meas_len, counts_2),
                )

                # Drive A and B Transistions repetitively during readout
                play("cw", "EOM_A")
                play("AOM_ON", "AOM")
                play("laser_ON", "OpticalTrigger")

                align("EOM_A", "EOM_B")

                play("cw", "EOM_B")
                play("AOM_ON", "AOM")
                play("laser_ON", "OpticalTrigger")

                assign(total_counts_2, total_counts_2 + counts_2)

            save(total_counts_1, counts_1_st)  # save counts_1 on stream
            assign(total_counts_1, 0)
            save(total_counts_2, counts_2_st)  # save counts_2 on stream
            assign(total_counts_2, 0)

        save(n, n_st)  # save number of iteration inside for_loop

    with stream_processing():
        counts_1_st.buffer(len(taus)).average().save("counts_1")
        counts_2_st.buffer(len(taus)).average().save("counts_2")
        n_st.save("iteration")

#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(host=qop_ip, port=qop_port, cluster_name=cluster_name)

simulate = False

if simulate:
    simulation_config = SimulationConfig(duration=40000)
    job = qmm.simulate(config, hahn_echo, simulation_config)

    samples = job.get_simulated_samples()
    waveform_report = job.get_simulated_waveform_report()
    waveform_report.create_plot(samples, plot=True, save_path=None)

    job.get_simulated_samples().con1.plot()
    plt.show()
else:
    qm = qmm.open_qm(config)

    job = qm.execute(hahn_echo)  # execute QUA program

    # Get results from QUA program
    results = fetching_tool(
        job, data_list=["counts_1", "counts_2", "iteration"], mode="live"
    )

    # Live plotting
    fig = plt.figure()
    interrupt_on_close(fig, job)  # Interrupts the job when closing the figure

    while results.is_processing():

        # Fetch results
        counts_1, counts_2, iteration = results.fetch_all()

        print(counts_1.shape, counts_2.shape)
        # Progress bar
        progress_counter(iteration, n_avg, start_time=results.get_start_time())
        # Plot data
        plt.cla()
        plt.plot((taus) / u.ns, counts_1 / 1000 / (meas_len * 1e-9))
        plt.plot((taus) / u.ns, counts_2 / 1000 / (meas_len * 1e-9))
        plt.xlabel("Idle time (tau) [ns]")
        plt.ylabel("Counts [kcps]")
        plt.title("Hahn Echo")

        plt.pause(0.1)
