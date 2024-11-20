"""
        COUNTER.py
This measurement seeks to verify that the threshold detection is correct once determined by the raw ADC traces. 
The optical laser with AOM1 & 2 will play during a time_tagging readout to determine photon counts within the measurement time-frame.
This plays for an infinite loop allowing for tuning of other parameters for experimental validation
        
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

total_integration_time = int(1 * u.ms)  # 100ms
single_integration_time_ns = int(5 * u.us)  # 500us
single_integration_time_cycles = single_integration_time_ns // 4
n_count = int(total_integration_time / single_integration_time_ns)
# Note, measure length for readout must be set to single_integration_time_ns in configuration

with program() as threshold_detection:
    times = declare(
        int, size=1000
    )  # array to store time tag for each count in ps for time_tagging.high_res()
    counts = declare(
        int
    )  # stores the total number of counts captured within duration of single_integration_time_ns,
    # note this time must be longer than pulse duration
    total_counts = declare(
        int
    )  # stores the total number of counts for each full n_count loop,
    # saves each iteration the experiment is run within the infinit loop
    n = declare(int)
    counts_st = declare_stream()

    with infinite_loop_():

        with for_(n, 0, n < n_count, n + 1):

            play(
                "laser_ON", "OpticalTrigger", duration=single_integration_time_cycles
            )  # Trigger laser
            play("AOM_ON", "AOM", duration=single_integration_time_cycles)  # Gain 1 & 2

            measure(
                "readout",
                "SNSPD",
                None,
                time_tagging.analog(times, single_integration_time_ns, counts),
            )  # ensure appropriate readout_len is set
            assign(total_counts, total_counts + counts)

        # Save to counts stream and reset for next iteration of the infinite loop
        save(total_counts, counts_st)
        assign(total_counts, 0)

    with stream_processing():
        counts_st.with_timestamps().save("counts")

#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(host=qop_ip, port=qop_port, cluster_name=cluster_name)

simulate = True

if simulate:
    simulation_config = SimulationConfig(duration=10000)  # in clock cycles
    job_sim = qmm.simulate(config, threshold_detection, simulation_config)

    # Get the waveform report
    samples = job_sim.get_simulated_samples()
    waveform_report = job_sim.get_simulated_waveform_report()
    waveform_report.create_plot(samples, plot=True, save_path=None)

    # Simulate blocks python until the simulation is done
    job_sim.get_simulated_samples().con1.plot()
    plt.legend("")
    plt.show()


else:

    qm = qmm.open_qm(config)
    # qm.close()
    job = qm.execute(threshold_detection)

    # Get results from QUA program
    res_handles = job.result_handles
    counts_handle = res_handles.get("counts")
    counts_handle.wait_for_values(1)
    time = []
    counts = []

    # Live plotting
    fig = plt.figure()
    interrupt_on_close(fig, job)  # Interrupts the job when closing the figure

    while res_handles.is_processing():
        new_counts = counts_handle.fetch_all()
        counts.append(new_counts["value"] / total_integration_time / 1000)
        time.append(new_counts["timestamp"] / u.s)  # Convert timestamps to seconds
        plt.cla()
        if len(time) > 50:
            plt.plot(time[-50:], counts[-50:])
        else:
            plt.plot(time, counts)

        plt.xlabel("time [s]")
        plt.ylabel("counts [kcps]")
        plt.title("Counter")
        plt.pause(0.1)
