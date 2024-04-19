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

###################
# The QUA program #
###################
max_number_of_counts = 30  # size of array containing time_tags
detection_window = 1_000  # ns
wait_time_between_measurements = 1 * u.s

with program() as raw_trace_prog:
    n = declare(int, value=0)
    num_counts = declare(int, value=0)
    times = declare(int, size=max_number_of_counts)

    times_st = declare_stream()
    loop_count_st = declare_stream()
    with infinite_loop_():
        measure(
            'read_count', 'alice_h', None,
            time_tagging.digital(times, detection_window, num_counts)
        )

        with for_(n, 0, n < max_number_of_counts, n + 1):
            with if_(n < num_counts):
                # if there was a count detected, save it
                save(times[n], times_st)
            with else_():
                # otherwise, counts with index >= num_counts are invalid! Save as 0.
                save(INVALID, times_st)

        long_wait(wait_time_between_measurements)

    with stream_processing():
        # this is CPU-based processing for streamed data
        times_st.buffer(max_number_of_counts).save("times")

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

results = fetching_tool(job, data_list=["times"], mode="live")
# Live plotting
fig = plt.figure()
interrupt_on_close(fig, job)  # Interrupts the job when closing the figure
while results.is_processing():
    # Fetch results
    times = results.fetch_all()
    times = [t for t in times if t != INVALID]
    plt.cla()
    plt.hist(times)
    plt.xlabel("Time Bin")
    plt.ylabel("Counts (#)")
    plt.tight_layout()
    plt.pause(0.1)