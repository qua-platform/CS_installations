# %%
"""
        RAW ADC TRACES
The goal of this script is to measure the raw ADC traces from SPCM(SPCM) without demodulation or integration.
It can be used to make sure that the ADCs are not saturated/offsetted and estimate the SNR.
It also allows to calibrate several parameters:
    - The time of flight: it corresponds to some internal processing time and propagation delay of the readout pulse.
      Its value can be updated in the configuration (time_of_flight) and is used to delay the acquisition window with
      respect to the time at which the readout pulse is sent. In the case of NV center experiments with time tagging, 
      it can be set to 36 ns (minimal) and adjust the delays accordingly.
    - The threshold for time-tagging: it corresponds to the ADC value above or below which the signal is considere
    - The analog inputs gain: if the signal is limited by digitization or saturates the ADC, the variable gain of the
      OPX analog input can be set to adjust the signal within the ADC range +/-0.5V.
      The gain (-12 dB to 20 dB) can also be set in the configuration (config/controllers/"con1"/analog_inputs). d to
      be an event that can be detected and time-tagged in the subsequent scripts.
    - The analog inputs offset: due to some small impedance mismatch, the signals acquired by the OPX can have small
      offsets that can be removed in the configuration (config/controllers/"con1"/analog_inputs) to improve demodulation.
"""

from qm.QuantumMachinesManager import QuantumMachinesManager
from qm.qua import *
import matplotlib.pyplot as plt
from configuration_with_octave import *
from qm import SimulationConfig


###################
# The QUA program #
###################
n_avg = 100

with program() as adc_trace:
    n = declare(int)  # QUA variable for the averaging loop
    adc_st = declare_stream(adc_trace=True)  # The stream to store the raw ADC trace

    with for_(n, 0, n < n_avg, n + 1):  # QUA for_ loop for averaging
        # Drive the AOM to play the readout laser pulse
        # Keep this commented out to measure dark counts from SPCM to calibrate the thresholds
        play("laser_ON", "AOM")
        # Record the raw ADC traces in the stream called "adc_st"
        measure("long_readout", "SPCM", adc_st)
        # Waits for the
        wait(2 * u.us)

    with stream_processing():
        # Will save average:
        adc_st.input1().average().save("adc1")
        # Will save only last run:
        adc_st.input1().save("adc1_single_run")

#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(host=qop_ip, port=None, cluster_name=cluster_name, octave=octave_config)

simulate = False
save_data = True

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=10_000)  # In clock cycles = 4ns
    job = qmm.simulate(config, adc_trace, simulation_config)
    plt.figure()
    job.get_simulated_samples().con1.plot()
else:
    # Open Quantum Machine
    qm = qmm.open_qm(config)
    # Execute program
    job = qm.execute(adc_trace)
    # create a handle to get results
    res_handles = job.result_handles
    # Wait until the program is done
    res_handles.wait_for_all_values()
    # Fetch results and convert traces to volts
    # adc1 = u.raw2volts(res_handles.get("adc1").fetch_all())
    # adc1_single_run = u.raw2volts(res_handles.get("adc1_single_run").fetch_all())
    adc1 = res_handles.get("adc1").fetch_all()
    adc1_single_run = res_handles.get("adc1_single_run").fetch_all()
    # Plot data
    plt.figure()
    plt.subplot(121)
    plt.title("Single run")
    plt.plot(adc1_single_run, label="Input 1")
    plt.xlabel("Time [ns]")
    plt.ylabel("Signal amplitude [V]")

    plt.subplot(122)
    plt.title("Averaged run")
    plt.plot(adc1, label="Input 1")
    plt.xlabel("Time [ns]")
    plt.tight_layout()

    print(f"\nInput1 mean: {np.mean(adc1)} V")

# %%
