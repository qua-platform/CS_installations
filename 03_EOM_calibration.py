"""
        CALIBRATE EOM RF
This program consists of playing the laser and varying the magnetic field to calibrate the desired frequency difference 
between the A and B optical transistions. This also determines MWe used for cw_odmr. This script assumes the magnetic 
field has some software controller which will be iterated in outside of the QUA loop. Ideally, the duration of the optical 
pulse and the EOM pulse are long to account for any delays that are not yet calibrated

Next steps before going to the next node:
    - Replace the relevant determined frequences for EOM_A, EOM_B, and mwe/mwg
    - Set Magnetic field value
"""

from qm import QuantumMachinesManager
from qm.qua import *
from qm import SimulationConfig
import matplotlib.pyplot as plt
from configuration_princeton_groundwork_with_octave import *
from qualang_tools.loops import from_array
from qualang_tools.results import wait_until_job_is_paused

EOM_min_freq = 10 * u.MHz
EOM_max_freq = 350 * u.MHz
dfs = 10 * u.MHz
frequencies = np.arange(EOM_min_freq, EOM_max_freq, dfs)

n_avg = 1

resolution = 20  # Number of histogram bins

B_min = 0  # In Gauss
B_max = 50  # In Gauss
B_step = 5  # In Gauss
B_fields = np.arange(B_min, B_max, B_step)
b_count = len(B_fields)

integration_len = (meas_len + 200)  # in ns, time_tagging must always be longer than pulse duration
pulse_len = meas_len // 4

# Time vector for plotting
t_vec = np.arange(0, meas_len, 1)

# Run the QUA program for each externally set magnetic field value

with program() as EOM_sweep:

    f = declare(int)
    times = declare(int, size=100)  # 'size' defines the max number of photons to be counted
    # times_st = declare_stream()  # stream for 'times'
    counts = declare(int)  # variable for number of counts
    counts_st = declare_stream()  # stream for counts
    total_counts = declare(int)
    n = declare(int)  # number of iterations
    i = declare(int)
    n_st = declare_stream()  # stream for number of iterations
    b = declare(int)
    b_st = declare_stream()

    with for_(b, 0, b <= b_count, b + 1):

        pause()
        wait(100)  # Wait for B field to settle

        with for_(*from_array(f, frequencies)):
            # Update the frequency of the EOM
            update_frequency("EOM", f + EOM_IF_freq)

            with for_(n, 0, n < n_avg, n + 1):

                play("AOM_ON", "AOM", duration=pulse_len)
                play("laser_ON", "OpticalTrigger", duration=pulse_len)
                play("cw", "EOM", duration=pulse_len)

                measure("readout","SNSPD",None,time_tagging.analog(times, integration_len, counts))

                # Save to counts stream and reset for next iteration of the infinite loop
                save(counts, counts_st)

                save(n, n_st)  # save number of iteration inside for_loop

        save(b, b_st)

    with stream_processing():
        counts_st.buffer(n_avg).map(FUNCTIONS.average()).buffer(len(frequencies)).save_all("counts")
        b_st.save("b_iteration")
        n_st.save("iteration")

#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(host=qop_ip, port=qop_port, cluster_name=cluster_name)

simulate = False

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

    for i in range(len(B_fields)):
        # set magnetic field to next value in array
        # set(B_field[i])
        # add delay?
        job.resume()
        # Wait until program reaches the 'pause' statement again, indicating the qua program is done for this magnetic field value
        wait_until_job_is_paused(job)
        if i == 0:
            # Get results from QUA program and initialize live plotting
            results = fetching_tool(job, data_list=["counts", "iteration", "b_iteration"], mode="live")

        # while results.is_processing():
        # Fetch results
        counts, iteration, b_iteration = results.fetch_all()
        # Progress bar
        progress_counter(b_iteration, b_count, start_time=results.get_start_time())
        # Plot data
        plt.cla()
        plt.pcolor(
            (EOM_IF_freq * 0 + frequencies) / u.MHz,
            B_fields[: i + 1] / 1000 / (integration_len * 1e-9),
            counts[: i + 1],
        )
        plt.xlabel("Frequencies [ns]")
        plt.ylabel("B_field")
        plt.title("Counts for Frequency vs B_field")
        plt.pause(0.1)
        print(counts.shape, iteration.shape, b_iteration.shape)
