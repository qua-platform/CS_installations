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

shots = 5_000  # The number of averages

with program() as repeated_readout:

    n = declare(int)  # QUA variable for the averaging loop
    n_st = declare_stream()
    n1 = declare(int)  # QUA variable for the averaging loop
    adc_st = [declare_stream(adc_trace=True) for _ in range(2)]
    clock = declare(int)

    with infinite_loop_():

        with for_(clock, 0, clock < 10_000_000, clock + 1):

            wait(250)

        align()

        wait((readout_len) // 4, 'rr2_twin')

        with for_(n, 0, n < shots, n + 1):  # QUA for_ loop for averaging
            measure('zero', 'rr2', adc_st[0])
            save(n, n_st)
            wait(readout_len // 4, 'rr2')

        with for_(n1, 0, n1 < shots, n1 + 1):  # QUA for_ loop for averaging
            measure('zero', 'rr2_twin', adc_st[1])
            wait(readout_len // 4, 'rr2_twin')

    
    with stream_processing():
        n_st.save('iteration')
        for ind in range(2):
            adc_st[ind].input2().buffer(shots).save(f"adc_{ind}")

qmm = QuantumMachinesManager(host=qop_ip, cluster_name=cluster_name)
qmm.close_all_qms()
# Open a quantum machine to execute the QUA program
qm = qmm.open_qm(config, close_other_machines=False)

if readout_len >= 1_000 and shots <= 5_000:

    try:

        job = qm.execute(repeated_readout)

        fetch_names = []

        for ind in range(2):
            fetch_names.append(f"adc_{ind}")

        results = fetching_tool(job, fetch_names, mode="live")

        plt.figure()

        counter = 0

        while results.is_processing():

            start_time = time.time()

            res = results.fetch_all()

            complete_adc = np.empty(((len(res[0]) + len(res[1])), readout_len), dtype=res[1][0][0])

            complete_adc[0::2] = res[0]
            complete_adc[1::2] = res[1]

            f, pxx = signal.periodogram(complete_adc.flatten(), fs=1e9)

            end_time = time.time()

            plt.clf()
            plt.plot(f, pxx)
            plt.title(f'counter: {counter} and time taken: {end_time - start_time}')
            plt.yscale('log')
            plt.xscale('log')
            plt.xlabel('Frequency [Hz]')
            plt.ylabel('PSD [a.u.]')
            plt.pause(10)

            counter += 1

    except Exception as e:
        print(e)

    finally:
        job.cancel()
        qm.close()

else:
    print("Lock in readout length is less than 1 microsecond or shots > 10 million")

