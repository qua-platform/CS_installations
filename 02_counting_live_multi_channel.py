"""
This script is designed to continuously read out the number of TTL
counts received in a given detection window simultaneously from multiple
channels. It will stream counts into the plotting window until the program ends.
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
    counts_alice_h = declare(int, value=0)
    counts_alice_v = declare(int, value=0)
    # counts_alice_d = declare(int, value=0)
    # counts_alice_a = declare(int, value=0)
    # counts_bob_h = declare(int, value=0)
    # counts_bob_v = declare(int, value=0)
    # counts_bob_d = declare(int, value=0)
    # counts_bob_a = declare(int, value=0)

    counts_alice_h_st = declare_stream()
    counts_alice_v_st = declare_stream()
    # counts_alice_d_st = declare_stream()
    # counts_alice_a_st = declare_stream()
    # counts_bob_h_st = declare_stream()
    # counts_bob_v_st = declare_stream()
    # counts_bob_d_st = declare_stream()
    # counts_bob_a_st = declare_stream()

    with infinite_loop_():
        measure('read_count', 'alice_h', None, counting.digital(counts_alice_h, detection_window))
        measure('read_count', 'alice_v', None, counting.digital(counts_alice_v, detection_window))
        # measure('read_count', 'alice_d', None, counting.digital(counts_alice_d, detection_window))
        # measure('read_count', 'alice_a', None, counting.digital(counts_alice_a, detection_window))
        # measure('read_count', 'bob_h', None, counting.digital(counts_bob_h, detection_window))
        # measure('read_count', 'bob_v', None, counting.digital(counts_bob_v, detection_window))
        # measure('read_count', 'bob_d', None, counting.digital(counts_bob_d, detection_window))
        # measure('read_count', 'bob_a', None, counting.digital(counts_bob_a, detection_window))

        save(counts_alice_h, counts_alice_h_st)
        save(counts_alice_v, counts_alice_v_st)
        # save(counts_alice_d, counts_alice_d_st)
        # save(counts_alice_a, counts_alice_a_st)
        # save(counts_bob_h, counts_bob_h_st)
        # save(counts_bob_v, counts_bob_v_st)
        # save(counts_bob_d, counts_bob_d_st)
        # save(counts_bob_a, counts_bob_a_st)

        # wait before time-tagging again to reduce data rate to PC.
        long_wait(wait_time_between_measurements)

    with stream_processing():
        # this is CPU-based processing for streamed data
        counts_alice_h_st.save_all("counts_alice_h")
        counts_alice_v_st.save_all("counts_alice_v")
        # counts_alice_d_st.save_all("counts_alice_d")
        # counts_alice_a_st.save_all("counts_alice_a")
        # counts_bob_h_st.save_all("counts_bob_h")
        # counts_bob_v_st.save_all("counts_bob_v")
        # counts_bob_d_st.save_all("counts_bob_d")
        # counts_bob_a_st.save_all("counts_bob_a")

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

data_list = [
    "counts_alice_h",
    "counts_alice_v",
    # "counts_alice_d",
    # "counts_alice_a",
    # "counts_bob_h",
    # "counts_bob_v",
    # "counts_bob_d",
    # "counts_bob_a"
]
results = fetching_tool(job, data_list=data_list, mode="live")
# Live plotting
fig = plt.figure()
interrupt_on_close(fig, job)  # Interrupts the job when closing the figure
added_legend = False
while results.is_processing():
    # Fetch results
    list_of_counts = results.fetch_all()
    for i, counts in enumerate(list_of_counts):
        plt.plot(counts, f'C{i}.-', label=data_list[i] if not added_legend else None)
    plt.xlabel("Iteration")
    plt.ylabel("Counts (#)")
    if not added_legend:
        plt.legend()
    plt.tight_layout()
    plt.pause(0.1)