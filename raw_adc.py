"""
A simple sandbox to showcase different QUA functionalities during the installation.
"""

import time

from configuration import *
from qm import QuantumMachinesManager, SimulationConfig
from qm.qua import *

meas_len = 1000
resolution = 1000  # ps
t_vec = np.arange(0, meas_len * 1e3, 1)
###################
# The QUA program #
###################
with program() as hello_qua:
    i = declare(int)
    times = declare(
        int, size=100
    )  # 'size' defines the max number of photons to be counted
    times_st = declare_stream()  # stream for 'times'
    counts = declare(int)  # variable to save the total number of photons
    adc_st = declare_stream(adc_trace=True)
    update_frequency("readout_aom", 0)
    for _ in range(4):
        play("readout" * amp(0.3), "readout_aom", duration=16 * u.ns)
        wait(100 * u.ns, "readout_aom")
    for _ in range(2):
        play("readout" * amp(0.1), "readout_aom", duration=16 * u.ns)
        wait(100 * u.ns, "readout_aom")
    align("SNSPD", "time_tagger")
    measure("readout", "SNSPD", adc_st)
    measure(
        "readout", "time_tagger", None, time_tagging.high_res(times, meas_len, counts)
    )

    with for_(i, 0, i < counts, i + 1):
        save(times[i], times_st)  # save time tags to stream

    with stream_processing():
        adc_st.input1().save_all("adc_trace")
        times_st.histogram(
            [
                [i, i + (resolution - 1)]
                for i in range(0, meas_len * int(1e3), resolution)
            ]
        ).save("times_hist")

with program() as time_tagger:
    i = declare(int)
    n = declare(int)
    times = declare(
        int, size=2000
    )  # 'size' defines the max number of photons to be counted
    times_st = declare_stream()  # stream for 'times'
    counts = declare(int)  # variable to save the total number of photons
    adc_st = declare_stream(adc_trace=True)
    # play("control", "control_eom")
    with for_(n, 0, n < 1000000, n + 1):
        # with infinite_loop_():
        align("control_aom", "time_tagger")
        # measure("readout", "SNSPD", adc_st)
        play("control", "control_eom", duration=48 * u.ns)
        play("control", "control_aom", duration=100 * u.ns)
        measure(
            "readout",
            "time_tagger",
            None,
            time_tagging.high_res(times, meas_len, counts),
        )
        wait(100 * u.ns, "control_aom")
        play("control", "control_aom", duration=100 * u.ns)

        with for_(i, 0, i < counts, i + 1):
            save(times[i], times_st)  # save time tags to stream

    with stream_processing():
        # adc_st.input1().save_all("adc_trace")
        times_st.histogram(
            [
                [i, i + (resolution - 1)]
                for i in range(0, meas_len * int(1e3), resolution)
            ]
        ).save("times_hist")


#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(
    host=opx_ip, port=None, cluster_name=cluster_name, octave=octave_config
)

###########################
# Run or Simulate Program #
###########################

simulate = False

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=1_000)  # In clock cycles = 4ns
    # Simulate blocks python until the simulation is done
    job = qmm.simulate(config, time_tagger, simulation_config)
    # Plot the simulated samples
    samples = job.get_simulated_samples()
    waveform_report = job.get_simulated_waveform_report()
    waveform_report.create_plot(samples, plot=True, save_path=None)
    plt.show()
else:
    # Open a quantum machine to execute the QUA program
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it - Execute does not block python!
    job = qm.execute(time_tagger)

    res = job.result_handles
    job.result_handles.wait_for_all_values()
    # adc_res = res.get("adc_trace").fetch_all()["value"]

    try:
        fig, ax = plt.subplots(1, 2, figsize=(10, 5))
        print(type(res.get("times_hist").fetch_all()))
        # ax[0].plot(adc_res[0, :], ".--")
        ax[1].plot(
            (t_vec[::resolution] + resolution / 2) / 1000 * u.ns,
            res.get("times_hist").fetch_all(),
            label=f"Total counts: {res.get('times_hist').fetch_all().sum()}",
        )

        ax[0].set_xlabel("t [ns]")
        ax[0].set_ylabel("ADC units [a.u.]")
        ax[0].set_title("ADC trace")
        ax[1].set_xlabel("t [ns]")
        ax[1].set_ylabel("counts")
        ax[1].set_title("TimeTag Histogram")
        plt.legend()

        fig.tight_layout()
        plt.show()
    except Exception as e:
        print(e)
        plt.close()
        plt.figure()
        plt.plot(adc_res[0, :])
        plt.title("Time tagging failed. ADC trace only")
        plt.xlabel("t [ns]")
        plt.ylabel("ADC units [a.u.]")
        plt.show()
