"""
        RAW ADC TRACES
The goal of this script is to measure the raw ADC traces without demodulation or integration.
It can be used to check the signals before demodulation, make sure that the ADCs are not saturated and estimate the SNR.
It also allows to calibrate several parameters:

    - The analog inputs offset: due to some small impedance mismatch, the signals acquired by the OPX can have small
      offsets that can be removed in the configuration (config/controllers/"con1"/analog_inputs) to improve demodulation.
    - The analog inputs gain: if the signal is limited by digitization or saturates the ADC, the variable gain of the
      OPX analog input can be set to adjust the signal within the ADC range +/-0.5V.
      The gain (-12 dB to 20 dB) can also be set in the configuration (config/controllers/"con1"/analog_inputs).
    - The threshold for time-tagging: it corresponds to the ADC value above or below which the signal is considered to
      be an event that can be detected and time-tagged in the subsequent scripts.
"""

from qm import QuantumMachinesManager
from qm.qua import *
import matplotlib.pyplot as plt
from configuration_princeton_groundwork_with_octave import *
from qm import SimulationConfig

from quam.components import *
from quam.components.channels import TimeTaggingAddon

qop_ip = "172.16.33.101"
cluster_name = "Cluster_81"
qop_port = None


###################
# The QUA program #
###################
n_avg = 100
quam = BasicQuAM()

machine = quam.load(r"C:\Users\BradCole\OneDrive - QM Machines LTD\Documents\Brewery\GitHubPull_testing_Dir\Princeton_QuAM\state.json")

config = machine.generate_config()
OpticalTrigger = machine.channels["OpticalTrigger"]
SNSPD_RAW = machine.channels["SNSPD_RAW"]
AOM1 = machine.channels["AOM1"]
AOM2 = machine.channels["AOM1"]

with program() as raw_adc_traces:
    n = declare(int)  # QUA variable for the averaging loop
    adc_st = declare_stream(adc_trace=True)  # The stream to store the raw ADC trace
    with for_(n, 0, n < n_avg, n + 1):  # QUA for_ loop for averaging

        OpticalTrigger.play("Laser_ON")
        AOM1.play("AOM1_ON",)
        AOM2.play("AOM1_ON",)

        SNSPD_RAW.measure("readout", stream = adc_st)

        wait(1000)

    with stream_processing():
        # Will save average:
        adc_st.input1().average().save("adc1")
        # Will save only last run:
        adc_st.input1().save("adc1_single_run")

#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(host=qop_ip, cluster_name=cluster_name)

simulate = True

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=10_000)  # In clock cycles = 4ns
    job = qmm.simulate(config, raw_adc_traces, simulation_config)
    # Get the waveform report
    samples = job.get_simulated_samples()
    waveform_report = job.get_simulated_waveform_report()
    waveform_report.create_plot(samples, plot=True, save_path=None)

    plt.figure()
    job.get_simulated_samples().con1.plot()
    plt.show()

else:
    # Open Quantum Machine
    qm = qmm.open_qm(config)
    # Execute program
    job = qm.execute(raw_adc_traces)
    # create a handle to get results
    res_handles = job.result_handles
    # Wait until the program is done
    res_handles.wait_for_all_values()
    # Fetch results and convert traces to volts
    adc1 = u.raw2volts(res_handles.get("adc1").fetch_all())
    adc1_single_run = u.raw2volts(res_handles.get("adc1_single_run").fetch_all())
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
    plt.show()

    print(f"\nInput1 mean: {np.mean(adc1)} V")
    qm.close()
