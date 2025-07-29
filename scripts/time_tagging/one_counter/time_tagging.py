from qm import QuantumMachinesManager
from qm.qua import *
from qm import SimulationConfig
from configuration import *
import matplotlib.pyplot as plt
from qm import LoopbackInterface


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
    times = declare(int, size=30)  # QUA-array
    times_st = declare_stream()  # stream for arrival times
    counts = declare(int)  # variable to store counted single-photon events
    counts_st = declare_stream()  # stream for counts
    adc_st = declare_stream(adc_trace=True)  # stream to save raw ADC of type 'adc_trace'

    with for_(i, 0, i < 5, i + 1):
        with for_(n, 0, n < 10, n + 1):
            play("gauss", "photon_source", condition= Random().rand_fixed() > 0.8)  # plays single_photon operation on qubit
            wait(4, "photon_source")  # wait 4 clock cycles (16 ns)

    measure(
        "readout", "SPCM", adc_st, time_tagging.analog(times, meas_len, counts)
    )  # measures on SPCM

    with for_(j, 0, j < counts, j+1):
        save(times[j], times_st)
    save(counts, counts_st)  # save counts to a stream

    with stream_processing():
        adc_st.input1().save("AI1_adc")  # saves stream data that arrives to analog input 1
        counts_st.save_all("counts")  # saves stream of single-photon counts
        times_st.save_all('times_stamps')



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



    AI1_adc = res_handle.get(
        "AI1_adc"
    ).fetch_all()  # fetches rawADC data in bit units -- inverted polarity due to historical reasons
    counts = res_handle.get(
        "counts"
    ).fetch_all()  # fetches number of single-photon events
    print(f"The numbr of counts is {counts[0][0]}")  # print number of photons counted
    times = res_handle.times_stamps.fetch_all()
    print(f"The time stamps of the counts are {times}")
    plt.figure()
    plt.plot(
        AI1_adc
        # AI1_adc * 2 ** -12
    )  # result is in bit units so it is divided by the 12-bit ADC
    plt.xlabel("time [ns]")  # time since the measure on SPCM1 started
    plt.ylabel("ADC trace [bit units]")  # analog input 1 trace
    plt.title("ADC trace at analog input 1")

else:
    qm = qmm.open_qm(config)  # calling the configuration file
    job = qm.execute(prog)
    res_handle = job.result_handles  # creates handles to access results
    res_handle.wait_for_all_values()  # wait for all values to arrive before granting access to results

    AI1_adc = res_handle.get(
        "AI1_adc"
    ).fetch_all()  # fetches rawADC data in bit units -- inverted polarity due to historical reasons
    counts = res_handle.get(
        "counts"
    ).fetch_all()  # fetches number of single-photon events
    print(f"The numbr of counts is {counts[0][0]}")  # print number of photons counted
    plt.figure()
    plt.plot(
        AI1_adc
        # AI1_adc * 2 ** -12
    )  # result is in bit units so it is divided by the 12-bit ADC

