"""
This script is designed to continuously read out the number of TTL
counts received in a given detection window. It will stream counts
into the plotting window until the program ends.
"""

from qm.qua import *
from qm import QuantumMachinesManager
from configuration import *
from qualang_tools.macros import long_wait

import matplotlib.pyplot as plt

from qualang_tools.results import fetching_tool
from qualang_tools.plot import interrupt_on_close

###################
# The QUA program #
###################

detection_window = 1_000  # ns
wait_time_between_measurements = 1 * u.s

with program() as raw_trace_prog:
    counts = declare(int, value=0)
    counts_st = declare_stream()

    with infinite_loop_():
        measure('read_count', 'alice_h', None, counting.digital(counts, detection_window))

        save(counts, counts_st)

        # wait before time-tagging again to reduce data rate to PC.
        long_wait(wait_time_between_measurements)

    with stream_processing():
        # this is CPU-based processing for streamed data
        counts_st.save_all("counts")

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

results = fetching_tool(job, data_list=["counts", "loop_count"], mode="live")
# Live plotting
fig = plt.figure()
interrupt_on_close(fig, job)  # Interrupts the job when closing the figure
while results.is_processing():
    # Fetch results
    counts = results.fetch_all()
    plt.plot(counts, 'k.-')
    plt.xlabel("Iteration")
    plt.ylabel("Counts (#)")
    plt.tight_layout()
    plt.pause(0.1)