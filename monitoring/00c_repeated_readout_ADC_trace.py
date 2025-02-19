"""
    Repeated Readout

"""
from qm.qua import *
from qm import QuantumMachinesManager
from configuration import *
from qualang_tools.results import fetching_tool, progress_counter
import matplotlib.pyplot as plt
from scipy import signal
import time

###################
# The QUA program #
###################

shots = 10  # The number of averages

with program() as repeated_readout:

    n = declare(int)  # QUA variable for the averaging loop
    n_st = declare_stream()
    n1 = declare(int)  # QUA variable for the averaging loop
    adc_st = declare_stream(adc_trace=True)
    clock = declare(int)

    with infinite_loop_():

        with for_(clock, 0, clock < 10_000_000, clock + 1):

            wait(250)

        align()

        wait((readout_len) // 4, 'rr2_twin')

        with for_(n, 0, n < shots, n + 1):  # QUA for_ loop for averaging
            measure('readout', 'rr2', adc_st)
            # save(n, n_st)
            wait(readout_len // 4, 'rr2')

        with for_(n1, 0, n1 < shots, n1 + 1):  # QUA for_ loop for averaging
            measure('readout', 'rr2_twin', adc_st)
            wait(readout_len // 4, 'rr2_twin')

    with stream_processing():
        adc_st.input2().buffer(2*shots).save(f"adc_0")

qmm = QuantumMachinesManager(host=qop_ip, cluster_name=cluster_name)
qmm.close_all_qms()

# from qm import SimulationConfig

# job = qmm.simulate(config, repeated_readout, SimulationConfig(int(10000)))
# job.get_simulated_samples().con1.plot()
# plt.show()

# Open a quantum machine to execute the QUA program
qm = qmm.open_qm(config, close_other_machines=False)

if readout_len >= 1_000 and shots <= 5_000:

    try:

        job = qm.execute(repeated_readout)

        fetch_names = []

        # for ind in range(2):
        fetch_names.append("adc_0")

        results = fetching_tool(job, fetch_names, mode="live")

        plt.figure()

        counter = 0

        while results.is_processing():

            start_time = time.time()

            res = results.fetch_all()

            f, pxx = signal.periodogram(res[0].flatten(), fs=1e9)

            end_time = time.time()

            plt.clf()
            plt.plot(f, pxx)
            plt.title(f'counter: {counter} and time taken: {end_time - start_time}')
            plt.yscale('log')
            plt.axvline(x=250e6, color='r', linestyle='--')
            # plt.axvline(x=125e6, color='r', linestyle='--')
            # plt.axhline(y=10e-07, color='r', linestyle='--')
            # plt.ylim([1e-12, 1e-5])
            plt.xscale('log')
            plt.xlabel('Frequency [Hz]')
            plt.ylabel('PSD [a.u.]')
            plt.pause(4)

            counter += 1

    except Exception as e:
        print(e)

    finally:
        job.cancel()
        qm.close()

else:
    print("Lock in readout length is less than 1 microsecond or shots > 10 million")

