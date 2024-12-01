"""
cw_odmr.py: Counts photons while sweeping the frequency of the applied MW.
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
RF_switch = machine.channels["RF_switch"]

###################
# The QUA program #
###################

f_min = 100 * u.MHz  # start of freq sweep
f_max = 300 * u.MHz  # end of freq sweep
df = 5 * u.MHz  # freq step
mwe_frequencies = np.arange(
    f_min, f_max, df
)  # Array to call when updating frequencies in QUA loop
n_avg = 10000  # number of averages

init_rep = 50
readout_rep = 250

with program() as cw_odmr:
    counts_st = declare_stream()  # stream for counts
    total_counts = declare(int)
    f = declare(int)  # frequencies
    n = declare(int)  # number of iterations
    i = declare(int)
    j = declare(int)
    n_st = declare_stream()  # stream for number of iterations

    with for_(n, 0, n < n_avg, n + 1):

        with for_(*from_array(f, mwe_frequencies)):

            update_frequency("mwe", f + mwe.intermediate_frequency)  # update frequency of MWe, drive 1

            with for_(i, 0, i < init_rep, i + 1):

                # initialization Optical pulse
                # duration of these pulses should be set to the same value in config for Optical pi pulse
                AOM1.play("AOM1_ON")
                AOM2.play("AOM2_ON")  
                OpticalTrigger.play("Laser_ON")
                EOM_A.play("const_pulse")

                # Pulse for excited spin flip
                wait((RF_switch_len >> 2), "RF_switch")
                RF_switch.play("RF_ON")
                wait((RF_switch_len >> 2), "mwe")
                mwe.play("const_pulse")  # play microwave pulse

            align()  # align all elements

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
        counts_st.buffer(len(mwe_frequencies)).average().save("counts")
        n_st.save("iteration")

#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(host=qop_ip, port=qop_port, cluster_name=cluster_name)

simulate = True
if simulate:
    simulation_config = SimulationConfig(duration=10000)
    job = qmm.simulate(config, cw_odmr, simulation_config)

    samples = job.get_simulated_samples()
    waveform_report = job.get_simulated_waveform_report()
    waveform_report.create_plot(samples, plot=True, save_path=None)

    job.get_simulated_samples().con1.plot()
    plt.show()
else:
    qm = qmm.open_qm(config)

    job = qm.execute(cw_odmr)  # execute QUA program

    # Get results from QUA program
    results = fetching_tool(job, data_list=["counts", "iteration"], mode="live")
    # Live plotting
    fig = plt.figure()
    interrupt_on_close(fig, job)  # Interrupts the job when closing the figure

    while results.is_processing():
        # counts = counts_handle.fetch_all()
        # iteration = iteration_handle.fetch_all()

        # Fetch results
        counts, iteration = results.fetch_all()
        # Progress bar
        progress_counter(iteration, n_avg, start_time=results.get_start_time())
        # Plot data
        plt.cla()
        plt.plot(
            (mwe_LO_freq * 0 + mwe_frequencies) / u.MHz,
            counts / 1000 / (meas_len * 1e-9),
        )
        plt.xlabel("Frequency [MHz]")
        plt.ylabel("Intensity [kcps]")
        plt.title("ODMR")
        plt.pause(0.1)
