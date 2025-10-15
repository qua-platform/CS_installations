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
import numpy as np
from qm.qua import *
from qm import QuantumMachinesManager
from qm import SimulationConfig
from configuration_with_mw_fem_SAIT_multi import *
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter
from test import visualize_opx1000_config
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
    adc_st_1 = declare_stream(adc_trace=True)  # The stream to store the raw ADC trace
    adc_st_2 = declare_stream(adc_trace=True)  # The stream to store the raw ADC trace

    with for_(n, 0, n < n_avg, n + 1):
        # Reset the phase of the digital oscillator associated to the resonator element. Needed to average the cosine signal.
        reset_phase("resonator_1")
        # reset_phase("resonator_2")
        # Sends the readout pulse and stores the raw ADC traces in the stream called "adc_st"
        measure("readout", "resonator_1", adc_st_1)
        wait(depletion_time * u.ns, "resonator_1")
        
        measure("readout", "resonator_2", adc_st_2)
        wait(depletion_time * u.ns, "resonator_2")

    with stream_processing():
        (adc_st_1.input1() if res1_in_port==1 else adc_st_1.input2()).average().save("adc1")
        (adc_st_1.input1() if res1_in_port==1 else adc_st_1.input2()).save("adc1_single_run")
        (adc_st_2.input1() if res2_in_port==1 else adc_st_2.input2()).average().save("adc2")
        (adc_st_2.input1() if res2_in_port==1 else adc_st_2.input2()).save("adc2_single_run")

#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(host=qop_ip, 
                             port=qop_port, 
                             cluster_name=cluster_name)

SAMPLE_DT_NS = 1  
def estimate_tof_ns(adc_trace, dt_ns=SAMPLE_DT_NS, sg_window=11, sg_poly=3,
                    edge_pre=100, edge_post=100):
    mag = np.abs(adc_trace).astype(float)

    max_allowed = len(mag) - (1 if len(mag) % 2 == 0 else 0)
    win = min(sg_window if sg_window % 2 == 1 else sg_window + 1, max_allowed)
    if win >= 5 and win < len(mag):
        sm = savgol_filter(mag, win, min(sg_poly, win - 1))
    else:
        sm = mag  

    pre = max(10, min(edge_pre, max(10, len(sm)//10)))
    post = pre
    base = np.mean(sm[:pre])
    tail = np.mean(sm[-post:]) 

    th = 0.5 * (base + tail) 

    idxs = np.flatnonzero(sm > th)
    if idxs.size == 0:
        return None, sm, th  

    idx_first = int(idxs[0])
    tof_ns = int(np.round((idx_first * dt_ns) / 4.0) * 4.0)  
    return tof_ns, sm, th

simulate = False
if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=2_000)  # In clock cycles = 4ns
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
    job = qm.execute(raw_trace_prog)
    res_handles = job.result_handles
    res_handles.wait_for_all_values()

    adc1 = u.raw2volts(res_handles.get("adc1").fetch_all())
    adc1_single_run = u.raw2volts(res_handles.get("adc1_single_run").fetch_all())
    adc2 = u.raw2volts(res_handles.get("adc2").fetch_all())
    adc2_single_run = u.raw2volts(res_handles.get("adc2_single_run").fetch_all())

    delay1_ns, sm1, th1 = estimate_tof_ns(adc1)
    delay2_ns, sm2, th2 = estimate_tof_ns(adc2)

    if delay1_ns is None:
        print("[WARN] Resonator 1: TOF 검출 실패 (문턱 초과 샘플 없음)")
        delay1_ns = 0
    if delay2_ns is None:
        print("[WARN] Resonator 2: TOF 검출 실패 (문턱 초과 샘플 없음)")
        delay2_ns = 0

    t1 = np.arange(len(adc1)) * SAMPLE_DT_NS
    t1s = np.arange(len(adc1_single_run)) * SAMPLE_DT_NS
    t2 = np.arange(len(adc2)) * SAMPLE_DT_NS
    t2s = np.arange(len(adc2_single_run)) * SAMPLE_DT_NS

    fig = plt.figure(figsize=(14, 8))

    ax11 = plt.subplot(221)
    ax11.set_title("Resonator 1 — Single run")
    ax11.plot(t1s, adc1_single_run.real, label="I")
    ax11.plot(t1s, adc1_single_run.imag, label="Q")
    ax11.axvline(delay1_ns, linestyle="--", label=f"TOF ≈ {delay1_ns} ns")
    ax11.set_xlabel("Time [ns]")
    ax11.set_ylabel("Amplitude [V]")
    ax11.legend()
    ax11.grid(True)
    ax11.tick_params(axis="both", which="both", labelsize=12, width=1.5, length=6)
    for s in ax11.spines.values():
        s.set_linewidth(1.5)

    ax21 = plt.subplot(223)
    ax21.set_title("Resonator 1 — Averaged")
    ax21.plot(t1, adc1.real, label="I")
    ax21.plot(t1, adc1.imag, label="Q")
    ax21.axvline(delay1_ns, linestyle="--", label=f"TOF ≈ {delay1_ns} ns")
    ax21.set_xlabel("Time [ns]")
    ax21.legend()
    ax21.grid(True)
    ax21.tick_params(axis="both", which="both", labelsize=12, width=1.5, length=6)
    for s in ax21.spines.values():
        s.set_linewidth(1.5)

    ax12 = plt.subplot(222)
    ax12.set_title("Resonator 2 — Single run")
    ax12.plot(t2s, adc2_single_run.real, label="I")
    ax12.plot(t2s, adc2_single_run.imag, label="Q")
    ax12.axvline(delay2_ns, linestyle="--", label=f"TOF ≈ {delay2_ns} ns")
    ax12.set_xlabel("Time [ns]")
    ax12.legend()
    ax12.grid(True)
    ax12.tick_params(axis="both", which="both", labelsize=12, width=1.5, length=6)
    for s in ax12.spines.values():
        s.set_linewidth(1.5)

    ax22 = plt.subplot(224)
    ax22.set_title("Resonator 2 — Averaged")
    ax22.plot(t2, adc2.real, label="I")
    ax22.plot(t2, adc2.imag, label="Q")
    ax22.axvline(delay2_ns, linestyle="--", label=f"TOF ≈ {delay2_ns} ns")
    ax22.set_xlabel("Time [ns]")
    ax22.legend()
    ax22.grid(True)
    ax22.tick_params(axis="both", which="both", labelsize=12, width=1.5, length=6)
    for s in ax22.spines.values():
        s.set_linewidth(1.5)

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

    print(f"Time Of Flight to add in the config — resonator_1: {delay1_ns} ns")
    print(f"Time Of Flight to add in the config — resonator_2: {delay2_ns} ns")