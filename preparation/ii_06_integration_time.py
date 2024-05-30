import numpy as np
from qm.qua import *
from qm import QuantumMachinesManager
from qm import SimulationConfig
from configuration_OPX1000 import *
from qualang_tools.loops import from_array


###################
# The QUA program #
###################
slice_length = 10  # Size of each demodulation slice in clock cycles
number_of_slices = int(readout_len / (4 * slice_length))

with program() as sliced_demodulation:
    n = declare(int)
    I = declare(fixed, size=number_of_slices)
    Q = declare(fixed, size=number_of_slices)
    dc_signal = declare(fixed, size=number_of_slices)
    I_st = declare_stream()
    Q_st = declare_stream()
    dc_signal_st = declare_stream()

    with for_(n, 0, n < 100, n + 1):  # The averaging loop
        measure(
            "readout", "lf_readout_element", None,
            demod.accumulated("cos", I, slice_length),
            demod.accumulated("sin", Q, slice_length)
        )
        # measure(
        #     "readout", "dc_readout_element", None,
        #     integration.accumulated("const", dc_signal, slice_length),
        # )
        save(I, I_st)
        save(Q, Q_st)
        save(dc_signal, dc_signal_st)
        # wait(250)

    with stream_processing():
        I_st.average().save("I")
        Q_st.average().save("Q")
        dc_signal_st.average().save("dc_signal")

#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(host=qop_ip, port=qop_port, cluster_name=cluster_name)

###########################
# Run or Simulate Program #
###########################

simulate = True

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=10_000)  # In clock cycles = 4ns
    # Simulate blocks python until the simulation is done
    job = qmm.simulate(config, sliced_demodulation, simulation_config)
    # Plot the simulated samples
    job.get_simulated_samples().con1.plot()
else:
    # Open a quantum machine to execute the QUA program
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it - Execute does not block python!
    job = qm.execute(sliced_demodulation)
