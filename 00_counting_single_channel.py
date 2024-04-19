"""
This script is designed to demonstrate the capabilities of the OPX+ and OPD,
bypassing the use of SPCMs for testing purposes.

The program is designed deterministically generate counts from the digital
output of the OPX+ (mimicking the SPCM TTL signal), and detect them at the
input of the OPD.

The line to play `fake_count` can be removed if the element is connected to
an external source of TTL signals.
"""

from qm.qua import *
from qm import QuantumMachinesManager
from configuration import *


###################
# The QUA program #
###################

# duration over which we will count TTL events
detection_window = 1_000  # ns

with program() as raw_trace_prog:
    counts_st = declare_stream()

    counts = declare(int, value=0)

    # wait(100 * u.ns, 'alice_h')
    # play('fake_count', 'alice_h')

    # Note that there is a dead-time between counts, potentially reducing the
    #  counts/time rate.
    measure('read_count', 'alice_h', None, counting.digital(counts, detection_window))

    save(counts, counts_st)

    with stream_processing():
        counts_st.save("counts")

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
# Creates a result handle to fetch data from the OPX
res_handles = job.result_handles
# Waits (blocks the Python console) until all results have been acquired
res_handles.wait_for_all_values()
# Fetch the raw ADC traces and convert them into Volts
counts = res_handles.get("counts").fetch_all()
# Output the number of detected counts
print(f"Received {counts} counts in {detection_window} ns!")