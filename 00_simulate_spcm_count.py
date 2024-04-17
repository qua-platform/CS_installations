"""
"""

from qm.qua import *
from qm import QuantumMachinesManager
from configuration import *
import matplotlib.pyplot as plt


###################
# The QUA program #
###################

with program() as raw_trace_prog:
    n = declare(int)
    counts_st = declare_stream()

    times = declare(int, size=10)
    counts = declare(int, value=0)

    # wait(100 * u.ns, 'spcm_alice_h')
    play('fake_count', 'spcm_alice_h')

    measure('read_count', 'alice_h', None, counting.digital(counts, 1_000))

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
print(counts)