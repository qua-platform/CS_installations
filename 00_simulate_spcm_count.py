"""
"""

from qm.qua import *
from qm import QuantumMachinesManager, LoopbackInterface
from qm import SimulationConfig
from configuration import *
import matplotlib.pyplot as plt

from qualang_tools.results import fetching_tool

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

###########################
# Run or Simulate Program #
###########################
simulate = True

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(
        duration=1_000,
        simulation_interface=LoopbackInterface([
            ("con1", 1, "con1", 1),
            ("spcm_alice_h", "alice_h", 0),
            ("spcm_alice_h", "alice_h", 1),
        ], latency=36)
    )
    # Simulate blocks python until the simulation is done
    job = qmm.simulate(config, raw_trace_prog, simulation_config)
    results = fetching_tool(job, data_list=["counts"])
    counts, = results.fetch_all()
    print(counts)
    ## Plot the simulated samples
    samples = job.get_simulated_samples(include_digital=True)
    plt.plot(samples.con1.digital['1-1'])
    plt.show()
    pass
else:
    # Open a quantum machine to execute the QUA program
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(raw_trace_prog)
    # Creates a result handle to fetch data from the OPX
    res_handles = job.result_handles
    # Waits (blocks the Python console) until all results have been acquired
    res_handles.wait_for_all_values()
    # Fetch the raw ADC traces and convert them into Volts
    adc1_single_run = u.raw2volts(res_handles.get("adc1_single_run").fetch_all())
    # Plot data
    plt.figure()
    plt.title("Single run")
    plt.plot(adc1_single_run, label="Input 1")
    plt.xlabel("Time [ns]")
    plt.ylabel("Signal amplitude [V]")
    plt.legend()