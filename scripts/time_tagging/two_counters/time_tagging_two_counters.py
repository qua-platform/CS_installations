from matplotlib import gridspec
from qm import QuantumMachinesManager
from qm.qua import *
from qm import SimulationConfig
from config_time_tagging_two_counters import *
import matplotlib.pyplot as plt
from qm import LoopbackInterface
import matplotlib
matplotlib.use("TkAgg")

qop_ip = "172.16.33.101"  # Write the QM router IP address
cluster_name = "CS_2"  # Write your cluster_name if version >= QOP220
qop_port = None  # Write the QOP port if version < QOP220

qmm = QuantumMachinesManager(host=qop_ip, cluster_name=cluster_name, port=qop_port)
resolution = 100
with program() as prog:
    n = declare(int)  # for_loop variable
    i = declare(int)  # for_loop variable
    j = declare(int)  # for_loop variable
    k = declare(int)  # for_loop variable
    times1 = declare(int, size=30)  # QUA-array
    times2 = declare(int, size=30)  # QUA-array
    times1_st = declare_stream()  # stream for arrival times
    times2_st = declare_stream()  # stream for arrival times
    counts1 = declare(int)  # variable to store counted single-photon events
    counts2 = declare(int)  # variable to store counted single-photon events
    counts1_st = declare_stream()  # stream for counts
    counts2_st = declare_stream()  # stream for counts
    adc_st = declare_stream(adc_trace=True)  # stream to save raw ADC of type 'adc_trace'

    # simulating photons
    with for_(i, 0, i < 50, i + 1):
        wait(4, "photon_source1")  # wait 4 clock cycles (16 ns)
        play("gauss", "photon_source1", condition=Random().rand_fixed() > 0.7)  # simulates single photon coming from SPCM1
        wait(10, "photon_source2")
        play("gauss_half_amp", "photon_source2", condition=Random().rand_fixed() > 0.7)  # simulates single photon coming from SPCM2

    # measuring from 2 SNSPDs
    measure(
        "readout", "SNSPD1", adc_st, time_tagging.analog(times1, meas_len, counts1)
    )  # measures on SNSPD1
    measure(
        "readout", "SNSPD2", None, time_tagging.analog(times2, meas_len, counts2)
    )  # measures on SNSPD2

    with for_(j, 0, j < counts1, j+1):
        save(times1[j], times1_st)

    with for_(j, 0, j < counts2, j+1):
        save(times2[j], times2_st)

    save(counts1, counts1_st)  # save counts1 to a stream
    save(counts2, counts2_st)  # save counts2 to a stream

    with stream_processing():
        adc_st.input1().save("AI1_adc")  # saves stream data that arrives to analog input 1
        counts1_st.save_all("counts1")  # saves stream of single-photon counts in SNSPD1
        counts2_st.save_all("counts2")  # saves stream of single-photon counts in SNSPD2
        times1_st.save_all('times1_stamps')
        times2_st.save_all('times2_stamps')



simulate = True
if simulate:
    simulate_config = SimulationConfig(
        duration=int(2000),
        simulation_interface=LoopbackInterface(
            ([("con1", 1, "con1", 1)])
        ),
    )  # simulation properties
    job = qmm.simulate(config, prog, simulate_config)  # do simulation
    # job.get_simulated_samples().con1.plot()  # visualize played pulses
    res_handle = job.result_handles  # creates handles to access results
    res_handle.wait_for_all_values()  # wait for all values to arrive before granting access to results


    AI1_adc = u.raw2volts(res_handle.AI1_adc.fetch_all())  # fetches rawADC data in bit units -- inverted polarity due to historical reasons
    counts_low = res_handle.counts1.fetch_all()["value"][0]  # fetches number of single-photon events in SNSPD1
    counts_high_and_low = res_handle.counts2.fetch_all()["value"][0]  # fetches number of single-photon events in SNSPD1 + SNSPD2
    counts_high = counts_high_and_low - counts_low  # fetches number of single-photon events in SNSPD2

    times_low = res_handle.times1_stamps.fetch_all()["value"]  # vector of the times on events in SNSPD1
    times_high_and_low = res_handle.times2_stamps.fetch_all()["value"]  # vector of the times on events in SNSPD1 + SNSPD2
    times_high = [num for num in times_high_and_low if all(abs(num - time) > sigma for time in times_low)]  # vector of the times on events in SNSPD2

    print(f"The number of events in SNSPD1 is {counts_low}")
    print(f"The number of events in SNSPD2 is {counts_high}")

    # plotting
    fig = plt.figure(figsize=(8, 8))
    gs = gridspec.GridSpec(2, 2, height_ratios=[1, 1], hspace=0.75)

    # Top subplot (spans both columns)
    ax1 = plt.subplot(gs[0, :])  # Row 0, span all columns
    # Bottom-left subplot
    ax2 = plt.subplot(gs[1, 0])  # Row 1, Column 0
    # Bottom-right subplot
    ax3 = plt.subplot(gs[1, 1])  # Row 1, Column 1

    ax1.set_title("raw ADC data measured on analog input 1")
    ax1.plot(AI1_adc)
    ax1.set_xlabel("time [ns]")
    ax1.set_ylabel("signal amplitude [V]")

    ax2.set_title(f"histogram of events in SNSPD1 \n counts = {counts_low}, signal threshold = {signal_threshold_1 / (4096):.2f}")
    ax2.hist(times_low, bins=100, edgecolor='black', alpha=0.75)
    ax2.set_xlabel("time [ns]")
    ax2.set_ylabel("# of counts")

    ax3.set_title(f"histogram of events in SNSPD2 \n counts = {counts_high}, signal threshold = {signal_threshold_2 / (4096):.2f}")
    ax3.hist(times_high, bins=100, edgecolor='black', alpha=0.75)
    ax3.set_xlabel("time [ns]")
    ax3.set_ylabel("# of counts")

    # Adjust layout for proper spacing
    plt.tight_layout()
    plt.show()
else:
    qm = qmm.open_qm(config)
    job = qm.execute(prog)
    res_handle = job.result_handles  # creates handles to access results
    res_handle.wait_for_all_values()  # wait for all values to arrive before granting access to results

    AI1_adc = u.raw2volts(res_handle.AI1_adc.fetch_all())  # fetches rawADC data in bit units -- inverted polarity due to historical reasons
    counts_low = res_handle.counts1.fetch_all()["value"][0]  # fetches number of single-photon events in SNSPD1
    counts_high_and_low = res_handle.counts2.fetch_all()["value"][
        0]  # fetches number of single-photon events in SNSPD1 + SNSPD2
    counts_high = counts_high_and_low - counts_low  # fetches number of single-photon events in SNSPD2

    times_low = res_handle.times1_stamps.fetch_all()["value"]  # vector of the times on events in SNSPD1
    times_high_and_low = res_handle.times2_stamps.fetch_all()["value"]  # vector of the times on events in SNSPD1 + SNSPD2
    times_high = [num for num in times_high_and_low if all(abs(num - time) > sigma for time in times_low)]  # vector of the times on events in SNSPD2

    print(f"The number of events in SNSPD1 is {counts_low}")
    print(f"The number of events in SNSPD2 is {counts_high}")

    # plotting
    fig = plt.figure(figsize=(8, 8))
    gs = gridspec.GridSpec(2, 2, height_ratios=[1, 1], hspace=0.75)

    # Top subplot (spans both columns)
    ax1 = plt.subplot(gs[0, :])  # Row 0, span all columns
    # Bottom-left subplot
    ax2 = plt.subplot(gs[1, 0])  # Row 1, Column 0
    # Bottom-right subplot
    ax3 = plt.subplot(gs[1, 1])  # Row 1, Column 1

    ax1.set_title("raw ADC data measured on analog input 1")
    ax1.plot(AI1_adc)
    ax1.set_xlabel("time [ns]")
    ax1.set_ylabel("signal amplitude [V]")

    ax2.set_title(f"histogram of events in SNSPD1 \n counts = {counts_low}, signal threshold = {signal_threshold_1 / (4096):.2f}")
    ax2.hist(times_low, bins=100, edgecolor='black', alpha=0.75)
    ax2.set_xlabel("time [ns]")
    ax2.set_ylabel("# of counts")

    ax3.set_title(f"histogram of events in SNSPD2 \n counts = {counts_high}, signal threshold = {signal_threshold_2 / (4096):.2f}")
    ax3.hist(times_high, bins=100, edgecolor='black', alpha=0.75)
    ax3.set_xlabel("time [ns]")
    ax3.set_ylabel("# of counts")

    # Adjust layout for proper spacing
    plt.tight_layout()
    plt.show()

