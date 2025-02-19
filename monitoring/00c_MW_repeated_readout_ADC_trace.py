"""
    Repeated Readout

"""
from qm.qua import *
from qm import QuantumMachinesManager
from configuration import *
from qualang_tools.results import fetching_tool
import matplotlib.pyplot as plt
from scipy import signal
import time
import numpy as np

###################
# The QUA program #
###################

shots = 5_000  # The number of averages

duc_freqs = np.arange(4.5e9, 7.5e9, 0.5e9)

with program() as repeated_readout:

    n = declare(int)  # QUA variable for the averaging loop
    n_st = declare_stream()
    n1 = declare(int)  # QUA variable for the averaging loop
    adc_st = [declare_stream(adc_trace=True) for _ in range(2)]
    clock = declare(int)

    # with infinite_loop_():

        # with for_(clock, 0, clock < 10_000_000, clock + 1):

        #     wait(250)

        # align()

    wait((readout_len) // 4, 'mw_el_twin')

    with for_(n, 0, n < shots, n + 1):  # QUA for_ loop for averaging
        measure('zero', 'mw_el', adc_st[0])
        save(n, n_st)
        wait(readout_len // 4, 'mw_el')

    with for_(n1, 0, n1 < shots, n1 + 1):  # QUA for_ loop for averaging
        measure('zero', 'mw_el_twin', adc_st[1])
        wait(readout_len // 4, 'mw_el_twin')

    
    with stream_processing():
        n_st.save('iteration')
        for ind in range(2):
            adc_st[ind].input2().buffer(shots).save(f"adc_{ind}")

qmm = QuantumMachinesManager(host=qop_ip, cluster_name=cluster_name)
# qmm.close_all_qms()
# Open a quantum machine to execute the QUA program

for freq in duc_freqs:

    config['controllers']['con1']['fems'][mw_fem]['analog_outputs'][8]['upconverters'][1]["frequency"] = int(freq)
    config['controllers']['con1']['fems'][mw_fem]['analog_inputs'][2]['downconverter_frequency'] = int(freq)

    qm = qmm.open_qm(config, close_other_machines=True)

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

                complete_adc = np.empty(((len(res[0].real) + len(res[1].real)), readout_len), dtype=res[1][0][0])

                complete_adc[0::2] = res[0].real
                complete_adc[1::2] = res[1].real

                f, pxx = signal.periodogram(complete_adc.flatten(), fs=1e9)

                end_time = time.time()

                plt.clf()
                plt.plot(f, pxx)
                plt.title(f'counter: {counter} and time taken: {(end_time - start_time):.2f} and DUC freq {(freq/1e9):.2f} GHz')
                plt.yscale('log')
                plt.xscale('log')
                plt.ylim([1e-12, 1e-5])
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

