import numpy as np
from qm.qua import *
from qm import QuantumMachinesManager
from qm import SimulationConfig
from configuration_OPX1000 import *
from qualang_tools.results import fetching_tool
import matplotlib.pyplot as plt

###################
# The QUA program #
###################
with program() as readout_modes:
    n = declare(int)
    I = declare(fixed)
    Q = declare(fixed)
    dc_signal = declare(fixed)
    I_st = declare_stream()
    Q_st = declare_stream()
    dc_signal_st = declare_stream()
    adc_st = declare_stream(adc_trace=True)

    with for_(n, 0, n < 1, n + 1):  # The averaging loop
        measure("readout", "lf_readout_element", adc_st, demod.full("cos", I, "out1"), demod.full("sin", Q, "out1"))
        measure("readout", "dc_readout_element", None, integration.full("const", dc_signal, "out1"))
        save(I, I_st)
        save(Q, Q_st)
        save(dc_signal, dc_signal_st)
        wait(1000)

    with stream_processing():
        I_st.average().save("I")
        Q_st.average().save("Q")
        dc_signal_st.average().save("dc_signal")
        adc_st.input1().average().save("adc_1")
        adc_st.input2().average().save("adc_2")

#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(host=qop_ip, port=qop_port, cluster_name=cluster_name)

###########################
# Run or Simulate Program #
###########################

simulate = False

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=10_000)  # In clock cycles = 4ns
    # Simulate blocks python until the simulation is done
    job = qmm.simulate(config, readout_modes, simulation_config)
    # Plot the simulated samples
    job.get_simulated_samples().con1.plot()
else:
    # Open a quantum machine to execute the QUA program
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it - Execute does not block python!
    job = qm.execute(readout_modes)
    # Get results from QUA program
    results = fetching_tool(job, data_list=["I", "Q", "dc_signal", "adc_1", "adc_2"])
    # Fetch results
    I, Q, dc_signal, adc_1, adc_2 = results.fetch_all()
    S = u.demod2volts(I + 1j * Q, readout_len, single_demod=True)
    dc_signal = u.demod2volts(dc_signal, readout_len)
    adc_1, adc_2 = u.raw2volts(adc_1), u.raw2volts(adc_2)
    plt.figure()
    plt.subplot(411)
    plt.plot(adc_1)
    plt.subplot(412)
    plt.plot(adc_2)
    plt.subplot(413)
    plt.plot(np.abs(S))
    plt.subplot(414)
    plt.plot(dc_signal)
