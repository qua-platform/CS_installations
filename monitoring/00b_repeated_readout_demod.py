"""
    Repeated Readout

"""
from qm.qua import *
from qm import QuantumMachinesManager
from configuration import *
from qualang_tools.results import fetching_tool
import matplotlib.pyplot as plt
from scipy import signal
from qualang_tools.addons.variables import assign_variables_to_element
import numpy as np
import time

shots = 1_000_000

with program() as repeated_readout:

    n = declare(int)  # QUA variable for the averaging loop
    n_st = declare_stream()
    n1 = declare(int)  # QUA variable for the averaging loop
    # Here we define one 'I', 'Q', 'I_st' & 'Q_st' for each resonator via a python list
    I = [declare(fixed) for _ in range(2)]
    Q = [declare(fixed) for _ in range(2)]
    I_st = [declare_stream() for _ in range(2)]
    Q_st = [declare_stream() for _ in range(2)]
    clock = declare(int)
    
    assign_variables_to_element('rr1', n, I[0], Q[0])
    assign_variables_to_element('rr1_twin', n1, I[1], Q[1])

    align()

    with infinite_loop_():

        with for_(clock, 0, clock < 10_000_000, clock + 1):

            wait(250)

        align()

        wait((readout_len + 16) // 4, 'rr1_twin')  # needed to delay second for_loop

        with for_(n, 0, n < shots, n + 1):  # QUA for_ loop for averaging
            measure('readout', 'rr1', None, demod.full("cos", I[0], 'out1'), demod.full("sin", Q[0], 'out1'))
            save(I[0], I_st[0])
            save(Q[0], Q_st[0])
            wait(readout_len // 4, 'rr1')

        with for_(n1, 0, n1 < shots, n1 + 1):  # QUA for_ loop for averaging
            measure('readout', 'rr1_twin', None, demod.full("cos", I[1], 'out1'), demod.full("sin", Q[1], 'out1'))
            save(I[1], I_st[1])
            save(Q[1], Q_st[1])
            wait(readout_len // 4, 'rr1_twin')

    with stream_processing():
        for ind in range(2):
            I_st[ind].buffer(shots).save(f"I_{ind}")
            Q_st[ind].buffer(shots).save(f"Q_{ind}")


qmm = QuantumMachinesManager(host=qop_ip, cluster_name=cluster_name)

qm = qmm.open_qm(config)

if readout_len >= 1_000 and shots <= 10_000_000:

    try:

        job = qm.execute(repeated_readout)

        fetch_names = []

        for ind in range(2):
            fetch_names.append(f"I_{ind}")
            fetch_names.append(f"Q_{ind}")

        results = fetching_tool(job, fetch_names, mode="live")

        plt.figure()

        counter = 0

        while results.is_processing():

            start_time = time.time()

            res = results.fetch_all()

            complete_I = np.empty((res[0].size + res[2].size))
            complete_Q = np.empty((res[1].size + res[3].size))

            complete_I[0::2] = res[0]
            complete_I[1::2] = res[2]

            complete_Q[0::2] = res[1]
            complete_Q[1::2] = res[3]

            complete_Z = complete_I + 1j*complete_Q

            phase = np.unwrap(np.angle(complete_Z))
            phase -= np.mean(phase)
            f, pxx = signal.welch(phase, nperseg=int(len(phase)/32), fs= 1e9 / readout_len)

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

        plt.show()

        res = results.fetch_all()

        complete_I = np.empty((res[0].size + res[2].size))
        complete_Q = np.empty((res[1].size + res[3].size))

        complete_I[0::2] = res[0]
        complete_I[1::2] = res[2]

        complete_Q[0::2] = res[1]
        complete_Q[1::2] = res[3]

        complete_Z = complete_I + 1j*complete_Q

        phase = np.unwrap(np.angle(complete_Z))
        phase -= np.mean(phase)
        f, pxx = signal.welch(phase, nperseg=int(len(phase)/32), fs= 1e9 / readout_len)

        plt.plot(f, pxx)
        plt.yscale('log')
        plt.xscale('log')
        plt.xlabel('Frequency [Hz]')
        plt.ylabel('PSD [a.u.]')
        plt.show()

    except Exception as e:
        print(e)

    finally:
        job.cancel()
        qm.close()
else:
    print("Lock in readout length is less than 1 microsecond or shots > 10 million")


# %%
