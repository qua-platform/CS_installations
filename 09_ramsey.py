"""
    TIME RABI_Optical
    
    Measure photon count while varying the pulse duration of the applied optical laser
    
"""

from qm import QuantumMachinesManager
from qm.qua import *
from qm import SimulationConfig
import matplotlib.pyplot as plt
from configuration_princeton_groundwork_with_octave import *
from qualang_tools.loops import from_array

from quam.components import *
from quam.components.channels import TimeTaggingAddon

qop_ip = "172.16.33.101"
cluster_name = "Cluster_81"
qop_port = None

quam = BasicQuAM()
machine = quam.load(r"C:\Users\BradCole\OneDrive - QM Machines LTD\Documents\Brewery\GitHubPull_testing_Dir\Princeton_QuAM\state.json")
config = machine.generate_config()
OpticalTrigger = machine.channels["OpticalTrigger"]
SNSPD = machine.channels["SNSPD"]
AOM1 = machine.channels["AOM1"]
AOM2 = machine.channels["AOM2"]
EOM_A = machine.channels["EOM_A"]
EOM_B = machine.channels["EOM_B"]
mwe = machine.channels["mwe"]
mwg = machine.channels["mwg"]
RF_switch = machine.channels["RF_switch"]

###################
# The QUA program #
###################

tau_min = 1000
tau_max = 10000
dtau = 100
taus = np.arange(tau_min, tau_max, dtau)


n_avg = 1
init_rep = 2 #50
readout_rep = 2 #250

with program() as ramsey:

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

                AOM1.play("AOM1_ON")
                AOM2.play("AOM2_ON")
                OpticalTrigger.play("Laser_ON")
                EOM_A.play("const_pulse")

                # Pulse for excited spin flip
                wait((RF_switch_len >> 2), "RF_switch")
                RF_switch.play("RF_ON",)
                wait((RF_switch_len >> 2), "mwe")
                mwe.play("pi")  # play microwave pulse

            align()  # align all elements

            # begin Ramsey sequence, play 1st pi_half pulse
            RF_switch.play("RF_ON", duration = mwg_pi_len)
            mwg.play("pi_half")
            # wait a varying idle
            wait(t >> 2, "mwg", "RF_switch") 
            # play 2ng pi_half pulse
            RF_switch.play("RF_ON", duration = mwg_pi_len)
            mwg.play("pi_half")

            align()

            with for_(j, 0, j < readout_rep, j + 1):

                # Begin readout, readout len and meas_length must be longer than each iteration
                times, counts = SNSPD.measure_time_tagging("readout", size = 1000, max_time = 3000)

                # Drive A and B Transistions repetitively during readout
                EOM_A.play("const_pulse")
                AOM1.play("AOM1_ON")
                AOM2.play("AOM2_ON")
                OpticalTrigger.play("Laser_ON")

                align("EOM_A", "EOM_B")

                EOM_B.play("const_pulse")
                AOM1.play("AOM1_ON")
                AOM2.play("AOM2_ON")
                OpticalTrigger.play("Laser_ON")

                assign(total_counts, total_counts + counts)

            save(total_counts, counts_st)  # save counts on stream
            assign(total_counts, 0)

        save(n, n_st)  # save number of iteration inside for_loop

    with stream_processing():
        counts_st.buffer(len(taus)).average().save(
            "counts"
        )
        n_st.save("iteration")

#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(host=qop_ip, port=qop_port, cluster_name=cluster_name)

simulate = True

if simulate:
    simulation_config = SimulationConfig(duration=40000)
    job = qmm.simulate(config, ramsey, simulation_config)

    samples = job.get_simulated_samples()
    waveform_report = job.get_simulated_waveform_report()
    waveform_report.create_plot(samples, plot=True, save_path=None)

    job.get_simulated_samples().con1.plot()
    plt.show()
else:
    qm = qmm.open_qm(config)

    job = qm.execute(ramsey)  # execute QUA program

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
        plt.plot((taus) * u.ns, counts / 1000 / (meas_len * 1e-9))
        plt.xlabel("Idle time [ns]")
        plt.ylabel("Counts [kcps]")
        plt.title("Ramsey")

        plt.pause(0.1)
