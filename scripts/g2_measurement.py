from qm import QuantumMachinesManager
from qm.simulate.credentials import create_credentials
from qm.qua import *
from qm import SimulationConfig, LoopbackInterface
from configuration import *

# Scan Parameters
n_avg = 1e4
expected_counts = 1000
meas_len = meas_len_1
with program() as g2_two_channel:
    counts_1 = declare(int)  # variable for the number of counts on SPCM1
    counts_2 = declare(int)  # variable for the number of counts on SPCM2
    times_1 = declare(int, size=expected_counts)  # array of count clicks on SPCM1
    times_2 = declare(int, size=expected_counts)  # array of count clicks on SPCM2
    n = declare(int)
    t1 = declare(int)
    t2 = declare(int)
    times_1_st = declare_stream()
    times_2_st = declare_stream()
    n_st = declare_stream()

    with for_(n, 0, n < n_avg, n+1):
        play('ON', 'TTL1')
        play('ON', 'TTL2')

        measure("readout", "SPCM1", time_tagging.analog(times_1, meas_len, counts_1))
        measure("readout", "SPCM2", time_tagging.analog(times_2, meas_len, counts_2))

        with for_(t1, 0, t1 < counts_1, t1 + 1):
            save(times_1[t1], times_1_st)
        with for_(t2, 0, t2 < counts_2, t2 + 1):
            save(times_2[t2], times_2_st)
        save(n, n_st)


    with stream_processing():
        times_1_st.save_all("times1")
        times_2_st.save_all("times2")
        n_st.save("iteration")


qmm = QuantumMachinesManager(qop_ip, cluster_name=cluster_name)

simulate = True
if simulate:
    simulation_config = SimulationConfig(duration=10_000)
    job = qmm.simulate(config, g2_two_channel, simulation_config)
    job.wait_until("Done", timeout=120)
    # Get the simulated samples
    samples = job.get_simulated_samples()
    # Plot the simulated samples
    samples.con1.plot()
    # Get the waveform report object
    waveform_report = job.get_simulated_waveform_report()
    # Cast the waveform report to a python dictionary
    waveform_dict = waveform_report.to_dict()
    # Visualize and save the waveform report
    waveform_report.create_plot(samples, plot=True, save_path=str(Path(__file__).resolve()))
else:
    qm = qmm.open_qm(config, close_other_machines=True)
    job = qm.execute(g2_two_channel)
    res = job.result_handles
    res.wait_for_all_values()
    times_1 = res.times1.fetch_all()
    times_2 = res.times2.fetch_all()
