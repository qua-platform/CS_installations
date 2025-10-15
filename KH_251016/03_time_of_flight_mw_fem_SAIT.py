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
from configuration_with_mw_fem_SAIT import *
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter
from vis_tool import visualize_opx1000_config
import os
from datetime import datetime

##################
#   Parameters   #
##################
# Parameters Definition
n_avg = 100  # Number of averaging loops

###################
# The QUA program #
###################
with program() as raw_trace_prog:
    n = declare(int)  # QUA variable for the averaging loop
    adc_st = declare_stream(adc_trace=True)  # The stream to store the raw ADC trace

    with for_(n, 0, n < n_avg, n + 1):
        # Reset the phase of the digital oscillator associated to the resonator element. Needed to average the cosine signal.
        reset_phase("resonator")
        # Sends the readout pulse and stores the raw ADC traces in the stream called "adc_st"
        measure("readout", "resonator", adc_st)
        # Wait for the resonator to deplete
        wait(depletion_time * u.ns, "resonator")

    with stream_processing():
        if res_in_port == 1:
            # Will save average: 
            adc_st.input1().average().save("adc")
            # Will save only last run:
            adc_st.input1().save("adc_single_run")
        else:
            # Will save average:
            adc_st.input2().average().save("adc")
            # Will save only last run:
            adc_st.input2().save("adc_single_run")

#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(host=qop_ip, 
                             port=qop_port, 
                             cluster_name=cluster_name)

#######################
# Simulate or execute #
#######################
simulate = False
if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=10_000)  # In clock cycles = 4ns
    # Simulate blocks python until the simulation is done
    job = qmm.simulate(config, raw_trace_prog, simulation_config)
    # Get the simulated samples
    samples = job.get_simulated_samples()
    # Plot the simulated samples
    samples.con1.plot()
    # Get the waveform report object
    waveform_report = job.get_simulated_waveform_report()
    # Cast the waveform report to a python dictionary
    waveform_dict = waveform_report.to_dict()
    # Visualize and save the waveform report
    waveform_report.create_plot(samples, plot=True, save_path=str(Path(__file__).resolve()))

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
    adc = u.raw2volts(res_handles.get("adc").fetch_all())
    adc_single_run = u.raw2volts(res_handles.get("adc_single_run").fetch_all())
    # Filter the data to get the pulse arrival time
    signal = savgol_filter(np.abs(adc), 11, 3)
    # Detect the arrival of the readout signal
    th = (np.mean(signal[:100]) + np.mean(signal[:-100])) / 2
    delay = np.where(signal > th)[0][0]
    delay = np.round(delay / 4) * 4  # Find the closest multiple integer of 4ns

    # Plot data
    fig = plt.figure(figsize=(12, 5))

    ax1 = plt.subplot(121)
    ax1.set_title("Single run")
    ax1.plot(adc_single_run.real, "b", label="I")
    ax1.plot(adc_single_run.imag, "r", label="Q")
    ax1.axvline(delay, color="k", linestyle="--", label="TOF")
    ax1.set_xlabel("Time [ns]")
    ax1.set_ylabel("Signal amplitude [V]")
    ax1.legend()
    ax1.tick_params(axis="both", which="both", labelsize=14, width=1.5, length=6)
    for spine in ax1.spines.values():
        spine.set_linewidth(1.5)

    ax2 = plt.subplot(122)
    ax2.set_title("Averaged run")
    ax2.plot(adc.real, "b", label="I")
    ax2.plot(adc.imag, "r", label="Q")
    ax2.axvline(delay, color="k", linestyle="--", label="TOF")
    ax2.set_xlabel("Time [ns]")
    ax2.legend()
    ax2.grid(True)
    ax2.tick_params(axis="both", which="both", labelsize=14, width=1.5, length=6)
    for spine in ax2.spines.values():
        spine.set_linewidth(1.5)

    plt.tight_layout()
    plt.show()

    timestamp = datetime.now().strftime('%y%m%d_%H%M')
    script_name = os.path.splitext(os.path.basename(__file__))[0]
    save_dir = os.path.join("./Data", script_name, timestamp)
    os.makedirs(save_dir, exist_ok=True)
    filename = f"{timestamp}_ToF.png"
    full_save_path = os.path.join(save_dir, filename)

    fig.savefig(full_save_path, dpi=300)
    print(f"Figure saved to: {full_save_path}") 

    visualize_opx1000_config(config, save_path=os.path.join(save_dir, f"{timestamp}_config.png"))

    # Update the config
    print(f"Time Of Flight to add in the config: {delay} ns")
