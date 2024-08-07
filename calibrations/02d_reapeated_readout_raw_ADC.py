from pathlib import Path
from qm.qua import *
from qm import SimulationConfig
from qualang_tools.units import unit
from quam_libs.components import QuAM
from quam_libs.macros import node_save
import matplotlib.pyplot as plt
import numpy as np
from qualang_tools.results import fetching_tool, progress_counter
from scipy import signal
import matplotlib
from quam_libs.macros import qua_declaration, multiplexed_readout, node_save

matplotlib.use("TKAgg")


###################################################
#  Load QuAM and open Communication with the QOP  #
###################################################
# Class containing tools to help handling units and conversions.
u = unit(coerce_to_integer=True)
# Instantiate the QuAM class from the state file
machine = QuAM.load()
# Generate the OPX and Octave configurations
config = machine.generate_config()
octave_config = machine.get_octave_config()
# Open Communication with the QOP
qmm = machine.connect()

# Get the relevant QuAM components

resonator1 = machine.qubits["q0"].resonator
resonator2 = machine.qubits["q1"].resonator

###################
# The QUA program #
###################
n_avg = 2  # The number of averages
readout_len = resonator2.operations.readout.length #readout length
if resonator2.operations.readout.length != resonator1.operations.readout.length:
    ValueError(f"Make sure that the readout_len of {resonator1.name} is equal to readout_len of {resonator2.name}")
with program() as repeated_readout:
    n = declare(int)  # QUA variable for the averaging loop
    n_st = declare_stream()
    n1 = declare(int)  # QUA variable for the averaging loop
    # Here we define one 'I', 'Q', 'I_st' & 'Q_st' for each resonator via a python list
    I, I_st, Q, Q_st, n, n_st = qua_declaration(num_qubits=2)
    adc_st = [declare_stream(adc_trace=True) for _ in range(2)]
    align()

    resonator2.wait((readout_len + 16) * u.ns) # needed to delay second for_loop
    resonator2.operations.
    with for_(n, 0, n < n_avg, n + 1):  # QUA for_ loop for averaging
        resonator1.measure('readout', stream=adc_st[0])
        save(I[0], I_st[0])
        save(Q[0], Q_st[0])
        save(n, n_st)
        resonator1.wait(readout_len * u.ns)

    with for_(n1, 0, n1 < n_avg, n1 + 1):  # QUA for_ loop for averaging
        resonator2.measure('readout', stream=adc_st[1])
        save(I[1], I_st[1])
        save(Q[1], Q_st[1])
        wait(readout_len * u.ns, 'QDS_twin')

    with stream_processing():
        n_st.save('iteration')
        for ind in range(2):
            adc_st[ind].input2().buffer(n_avg).save(f"adc_{ind}")


###########################
# Run or Simulate Program #
###########################

simulate = False

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=10_000)  # In clock cycles = 4ns
    # Simulate blocks python until the simulation is done
    job = qmm.simulate(config, repeated_readout, simulation_config)
    # Plot the simulated samples
    job.get_simulated_samples().con1.plot()

else:
    # Open a quantum machine to execute the QUA program
    qm = qmm.open_qm(config)

    job = qm.execute(repeated_readout)

    fetch_names = ['iteration']

    results = fetching_tool(job, fetch_names, mode="live")

    while results.is_processing():
        res = results.fetch_all()

        progress_counter(res[0], shots, start_time=results.start_time)

    for ind in range(2):
        fetch_names.append(f"adc_{ind}")

    results = fetching_tool(job, fetch_names)
    res = results.fetch_all()

    complete_adc = np.empty(((len(res[1]) + len(res[2])), lock_in_readout_length), dtype=res[1][0][0])

    complete_adc[0::2] = res[1]
    complete_adc[1::2] = res[2]

    f, pxx = signal.periodogram(complete_adc.flatten(), fs=1e9)

    plt.plot(f, pxx)
    plt.yscale('log')
    plt.xscale('log')
    plt.xlabel('Frequency [Hz]')
    plt.ylabel('PSD [a.u.]')


    qm.close()
    print("Experiment QM is now closed")
    # Close the quantum machines at the end in order to put all flux biases to 0 so that the fridge doesn't heat-up

