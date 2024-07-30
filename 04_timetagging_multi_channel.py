"""
This script is designed to extract the relative times at which a count was
detected, relative to the start of the window in ns.
"""

from qm.qua import *
from qm import QuantumMachinesManager
from qualang_tools.macros import long_wait

from configuration import *

import matplotlib.pyplot as plt

from qualang_tools.results import progress_counter, fetching_tool
from qualang_tools.plot import interrupt_on_close

# value to indicate saved time as invalid
INVALID = -1

elements = ['alice_h', 'alice_v']

###################
# The QUA program #
###################
max_number_of_counts = 15  # size of array containing time_tags
resolution_time = 1 * u.ms
# wait_time_between_measurements = 1 * u.s

num_counts = []
times = []
times_st = []

avg=1000

with program() as raw_trace_prog:
    i = declare(int)
    n = declare(int, value=0)
    for _ in elements:
        num_counts.append(declare(int, value=0))
        times.append(declare(int, size=max_number_of_counts))
        times_st.append(declare_stream())

    with for_(i, 0, i < avg, i+1):
        for k, element in enumerate(elements):
            measure(
               'read_count',
               element,
               None,
               time_tagging.digital(times[k], resolution_time, num_counts[k]),
               # counting.digital(times, detection_window, num_counts),
            )

        for k, element in enumerate(elements):
            with for_(n, 0, n < max_number_of_counts, n + 1):
                with if_(n < num_counts[k]):
                    # if there was a count detected, save it
                    save(times[k][n], times_st[k])
                with else_():
                    # otherwise, counts with index >= num_counts are invalid! Save as 0.
                    save(INVALID, times_st[k])

            wait(100 * u.us)

    with stream_processing():
        # this is CPU-based processing for streamed data
        for k, element in enumerate(elements):
            times_st[k].buffer(max_number_of_counts).save_all(f"times_{element}")

#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(qop_ip, cluster_name=cluster_name, octave=octave_config)

###############
# Run Program #
###############
# Open a quantum machine to execute the QUA program
qm = qmm.open_qm(config)
# Send the QUA program to the OPX, which compiles and executes it
job = qm.execute(raw_trace_prog)

results = fetching_tool(job, data_list=[f"times_{el}" for el in elements], mode="live")
# Live plotting
fig = plt.figure()
interrupt_on_close(fig, job)  # Interrupts the job when closing the figure
while results.is_processing():
    # Fetch results
    times = results.fetch_all()
    plt.cla()
    for k, element in enumerate(elements):
        print(f"Element: {element}, times: {times[k]}")
        times_k = []
        for j in range(len(times[k])):
            times_k_j = [t + j*1e6 for t in times[k][j] if t != INVALID]
            times_k.extend(times_k_j)
            plt.hist(times_k, color=f"C{j}", bins=500)
    plt.xlabel("Time Bin")
    plt.ylabel("Counts (#)")
    plt.tight_layout()
    plt.pause(0.1)