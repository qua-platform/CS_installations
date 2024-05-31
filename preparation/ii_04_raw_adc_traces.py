import numpy as np
from qm.qua import *
from qm import QuantumMachinesManager
from qm import SimulationConfig
from configuration_OPX1000 import *
from qualang_tools.results import fetching_tool
import matplotlib.pyplot as plt

# get the config
config = get_config(sampling_rate=1e9)

###################
# The QUA program #
###################
with program() as raw_adc:
    n = declare(int)
    adc1_st = declare_stream(adc_trace=True)
    adc2_st = declare_stream(adc_trace=True)

    with for_(n, 0, n < 1, n + 1):  # The averaging loop
        play("const", "lf_element_2")
        play("const", "lf_element_1")
        measure("readout", "lf_readout_element", adc1_st)
        measure("readout", "dc_readout_element", adc2_st)
        wait(1000)

    with stream_processing():
        adc1_st.input1().average().save("adc_1")
        adc2_st.input2().average().save("adc_2")

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
    job = qmm.simulate(config, raw_adc, simulation_config)
    # Plot the simulated samples
    job.get_simulated_samples().con1.plot()
    # Get the waveform report
    samples = job.get_simulated_samples()
    waveform_report = job.get_simulated_waveform_report()
    waveform_report.create_plot(samples, plot=True, save_path=None)
else:
    # Open a quantum machine to execute the QUA program
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it - Execute does not block python!
    job = qm.execute(raw_adc)
    # Get results from QUA program
    results = fetching_tool(job, data_list=["adc_1", "adc_2"])
    # Fetch results
    adc_1, adc_2 = results.fetch_all()
    adc_1, adc_2 = -u.raw2volts(adc_1), -u.raw2volts(adc_2)
    plt.figure()
    plt.subplot(211)
    plt.ylabel("ADC 1 [V]")
    plt.xlabel("time [ns]")
    plt.plot(adc_1)
    plt.subplot(212)
    plt.plot(adc_2)
    plt.ylabel("ADC 2 [V]")
    plt.xlabel("time [ns]")
    plt.tight_layout()
    print(max(adc_1) - min(adc_1))
