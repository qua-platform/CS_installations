"""
        TIME OF FLIGHT
This sequence involves sending a readout pulse and capturing the raw ADC traces.
The data undergoes post-processing to calibrate three distinct parameters:
    - Time of Flight: This represents the internal processing time and the propagation delay of the readout pulse.
    Its value can be adjusted in the configuration under "time_of_flight".
    This value is utilized to offset the acquisition window relative to when the readout pulse is dispatched.

    - Analog Inputs Offset: Due to minor impedance mismatches, the signals captured by the OPX might exhibit slight offsets.
    These can be rectified in the configuration at: config/controllers/"con1"/analog_inputs, enhancing the demodulation process.

    - Analog Inputs Gain: If a signal is constrained by digitization or if it saturates the ADC,
    the variable gain of the OPX analog input can be modified to fit the signal within the ADC range of +/-0.5V.
    This gain, ranging from -12 dB to 20 dB, can also be adjusted in the configuration at: config/controllers/"con1"/analog_inputs.
"""

from qm.qua import *
from qm import QuantumMachinesManager
from qm import SimulationConfig
from configuration import *
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter


###################
# The QUA program #
###################
n_avg = 100  # Number of averaging loops

element1 = "ATS1"  # The element to measure
element2 = "ATS2"  # The element to measure

with program() as raw_trace_prog:
    n = declare(int)  # QUA variable for the averaging loop
    adc_st1 = declare_stream(adc_trace=True)  # The stream to store the raw ADC trace
    adc_st2 = declare_stream(adc_trace=True)  # The stream to store the raw ADC trace

    with for_(n, 0, n < n_avg, n + 1):
        # Reset the phase of the digital oscillator associated to the resonator element. Needed to average the cosine signal.
        reset_if_phase(element1)
        reset_if_phase(element2)
        # Sends the readout pulse and stores the raw ADC traces in the stream called "adc_st"
        measure("readout", element1, adc_st1)
        measure("readout", element2, adc_st2)
        # Wait for the resonator to deplete
        wait(1000 * u.ns)

    with stream_processing():
        # Will save average:
        adc_st1.input1().average().save("adc1")
        adc_st2.input1().average().save("adc2")
        # Will save only last run:
        adc_st1.input1().save("adc1_single_run")
        adc_st2.input1().save("adc2_single_run")


#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(host=qop_ip, port=qop_port, cluster_name=cluster_name)

#######################
# Simulate or execute #
#######################
simulate = False
if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=10_000)  # In clock cycles = 4ns
    # Simulate blocks python until the simulation is done
    job = qmm.simulate(config, raw_trace_prog, simulation_config)
    # Plot the simulated samples
    job.get_simulated_samples().con1.plot()

else:
    # Open the quantum machine
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(raw_trace_prog)
    # Creates a result handle to fetch data from the OPX
    res_handles = job.result_handles
    # Waits (blocks the Python console) until all results have been acquired
    res_handles.wait_for_all_values()
    # Fetch the raw ADC traces and convert them into Volts
    adc1 = u.raw2volts(res_handles.get("adc1").fetch_all())
    adc2 = u.raw2volts(res_handles.get("adc2").fetch_all())
    adc1_single_run = u.raw2volts(res_handles.get("adc1_single_run").fetch_all())
    adc2_single_run = u.raw2volts(res_handles.get("adc2_single_run").fetch_all())
    # Derive the average values
    adc1_mean = np.mean(adc1)
    adc2_mean = np.mean(adc2)
    # Remove the average values
    adc1_unbiased = adc1 - np.mean(adc1)
    adc2_unbiased = adc2 - np.mean(adc2)
    # Filter the data to get the pulse arrival time
    signal1 = savgol_filter(np.abs(adc1_unbiased), 11, 3)
    signal2 = savgol_filter(np.abs(adc2_unbiased), 11, 3)
    # Detect the arrival of the readout signal
    th = (np.mean(signal1[:100]) + np.mean(signal1[:-100])) / 2
    delay1 = np.where(signal1 > th)[0][0]
    delay1 = np.round(delay1 / 4) * 4  # Find the closest multiple integer of 4ns
    th = (np.mean(signal2[:100]) + np.mean(signal2[:-100])) / 2
    delay2 = np.where(signal2 > th)[0][0]
    delay2 = np.round(delay2 / 4) * 4  # Find the closest multiple integer of 4ns

    # Plot data
    fig = plt.figure()
    plt.subplot(121)
    plt.title("Single run")
    plt.plot(adc1_single_run, "b", label="Input 1")
    plt.plot(adc2_single_run, "r", label="Input 2")
    xl = plt.xlim()
    yl = plt.ylim()
    plt.axhline(y=0.5)
    plt.axhline(y=-0.5)
    plt.plot(xl, adc1_mean * np.ones(2), "k--")
    plt.plot(xl, adc2_mean * np.ones(2), "k--")
    plt.plot(delay1 * np.ones(2), yl, "k--")
    plt.plot(delay2 * np.ones(2), yl, "g--")
    plt.xlabel("Time [ns]")
    plt.ylabel("Signal amplitude [V]")
    plt.legend()
    plt.subplot(122)
    plt.title("Averaged run")
    plt.plot(adc1, "b", label="Input 1")
    plt.plot(adc2, "r", label="Input 2")
    xl = plt.xlim()
    yl = plt.ylim()
    plt.plot(xl, adc1_mean * np.ones(2), "k--")
    plt.plot(xl, adc2_mean * np.ones(2), "k--")
    plt.plot(delay1 * np.ones(2), yl, "k--")
    plt.plot(delay2 * np.ones(2), yl, "g--")
    plt.xlabel("Time [ns]")
    plt.legend()
    plt.grid("all")
    plt.tight_layout()
    plt.show()

    # Update the config
    print(f"DC offset to add to I in the config: {-adc1_mean:.6f} V")
    print(f"DC offset to add to Q in the config: {-adc2_mean:.6f} V")
    print(f"Time Of Flight to add in the config for ATS1: {delay1} ns")
    print(f"Time Of Flight to add in the config for ATS2: {delay2} ns")
