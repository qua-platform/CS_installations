# %%
"""
        RAW ADC TRACES
This script aims to measure data captured within a specific window defined by the measure() function.
We term the digitized, unprocessed data as "raw ADC traces" because they represent the acquired waveforms without any
real-time processing by the pulse processor, such as demodulation, integration, or time-tagging.

The script is useful for inspecting signals prior to demodulation, ensuring the ADCs are not saturated,
correcting any non-zero DC offsets, and estimating the SNR.
"""

from qm.qua import *
from qm import QuantumMachinesManager
from qm import SimulationConfig
from configuration_with_lffem_octave_2GSPS import *
import matplotlib.pyplot as plt
import matplotlib
import time

# matplotlib.use('TkAgg')

###################
# The QUA program #
###################
n_avg = 10  # The number of averages
rr_if = 750 * u.MHz
resonators = [f"rr_test{p}" for p in range(6, 9, 1)]

for rr, rr_val in config["elements"].items():
    rr_val["intermediate_frequency"] = rr_if


with program() as raw_trace_prog:
    n = declare(int)  # QUA variable for the averaging loop
    adc_st = declare_stream(adc_trace=True)  # The stream to store the raw ADC trace

    with for_(n, 0, n < n_avg, n + 1):  # QUA for_ loop for averaging
        # Make sure that the readout pulse is sent with the same phase so that the acquired signal does not average out
        # for rr in resonators:
        #     reset_phase(rr)
        # Measure the resonator (send a readout pulse and record the raw ADC trace)
        for rr in resonators:
            measure("single", rr, adc_stream=adc_st)
        # Wait for the resonator to deplete
        wait(1000 * u.ns, *resonators)

    with stream_processing():
        # Will save average:
        adc_st.input1().average().save("adc1")
        adc_st.input2().average().save("adc2")
        # Will save only last run:
        adc_st.input1().save("adc1_single_run")
        adc_st.input2().save("adc2_single_run")


#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(host=qop_ip, port=qop_port, cluster_name=cluster_name)

from pathlib import Path
from qm import generate_qua_script
debug_filepath = sourceFile = f"debug_{Path(__file__).stem}.py"
sourceFile = open(debug_filepath, "w")
print(generate_qua_script(raw_trace_prog, config), file=sourceFile)
sourceFile.close()

###########################
# Run or Simulate Program #
###########################
simulate = False
save_data = True

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=400)  # In clock cycles = 4ns
    # Simulate blocks python until the simulation is done
    job = qmm.simulate(config, raw_trace_prog, simulation_config)
    # Plot the simulated samples
    res = job.get_simulated_samples().con1.analog
    ys = res["5-7"]
    ts1 = np.arange(len(ys)) * (1e9 / sampling_rate)
    fft_adc1 = np.fft.fft(ys)
    freqs = np.fft.fftfreq(len(ys), d=1 / sampling_rate) / 1e6

    # Plot data
    fig, axs = plt.subplots(2, 1, figsize=(7, 5))
    
    ax = axs[0]
    ax.set_title(f"IF at {rr_if / u.MHz} MHz")
    ax.plot(ts1, ys, label="Input 1")
    # ax.plot(ts2, adc2_single_run, label="Input 2")
    ax.set_xlabel("Time [ns]")
    ax.set_ylabel("Signal amplitude [V]")
    ax.legend()

    ax = axs[1]
    ax.set_title("FFT")
    ax.plot(freqs[:len(freqs) // 2], np.abs(fft_adc1)[:len(freqs) // 2], label="Input 1")
    # ax.plot(freqs[:len(freqs) // 2], np.abs(fft_adc2)[:len(freqs) // 2], label="Input 2")
    ax.set_xlabel("Frequency [MHz]")
    ax.set_ylabel("Magnitude")
    ylim = ax.get_ylim()
    for f in [250, 500, 750]:
        ax.vlines(x=f, ymin=ylim[0], ymax=ylim[1], color='m', alpha=0.2)
        ax.annotate(f"f = {f} MHz", xy=(f, ylim[1] * 0.9), xytext=(f + 10, ylim[1] * 0.9), color='m')
    ax.set_ylim(ylim)
    ax.legend()
    plt.tight_layout()
    plt.show()

    
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
    adc1 = u.raw2volts(res_handles.get("adc1").fetch_all())
    adc2 = u.raw2volts(res_handles.get("adc2").fetch_all())
    # adc2 = adc1 # u.raw2volts(res_handles.get("adc2").fetch_all())
    adc1_single_run = u.raw2volts(res_handles.get("adc1_single_run").fetch_all())
    adc2_single_run = u.raw2volts(res_handles.get("adc2_single_run").fetch_all())
    # adc2_single_run = adc1_single_run # u.raw2volts(res_handles.get("adc2_single_run").fetch_all())
    ts1 = np.arange(len(adc1_single_run)) * (1e9 / sampling_rate)
    ts2 = np.arange(len(adc2_single_run)) * (1e9 / sampling_rate) 

    # Compute FFT
    fft_adc1 = np.fft.fft(adc1_single_run)
    fft_adc2 = np.fft.fft(adc2_single_run)

    # Frequency axis (in MHz)
    freqs = np.fft.fftfreq(len(adc1_single_run), d=1 / sampling_rate) / 1e6

    # Plot data
    fig, axs = plt.subplots(2, 1, figsize=(7, 5))
    
    ax = axs[0]
    ax.set_title(f"IF at {rr_if / u.MHz} MHz")
    ax.plot(ts1, adc1_single_run, label="Input 1")
    # ax.plot(ts2, adc2_single_run, label="Input 2")
    ax.set_xlabel("Time [ns]")
    ax.set_ylabel("Signal amplitude [V]")
    ax.legend()

    ax = axs[1]
    ax.set_title("FFT")
    ax.plot(freqs[:len(freqs) // 2], np.abs(fft_adc1)[:len(freqs) // 2], label="Input 1")
    # ax.plot(freqs[:len(freqs) // 2], np.abs(fft_adc2)[:len(freqs) // 2], label="Input 2")
    ax.set_xlabel("Frequency [MHz]")
    ax.set_ylabel("Magnitude")
    ylim = ax.get_ylim()
    for f in [250, 500, 750]:
        ax.vlines(x=f, ymin=ylim[0], ymax=ylim[1], color='m', alpha=0.2)
        ax.annotate(f"f = {f} MHz", xy=(f, ylim[1] * 0.9), xytext=(f + 10, ylim[1] * 0.9), color='m')
    ax.set_ylim(ylim)
    ax.legend()
    plt.tight_layout()
    plt.show()

    print(f"\nInput1 mean: {np.mean(adc1)} V\n" f"Input2 mean: {np.mean(adc2)} V")

    if save_data:
        from qualang_tools.results.data_handler import DataHandler

        # Data to save
        save_data_dict = {}
        save_data_dict["adc1"] = adc1
        save_data_dict["adc2"] = adc2
        save_data_dict["adc1_single_run"] = adc1_single_run
        save_data_dict["adc2_single_run"] = adc2_single_run

        # Save results
        script_name = Path(__file__).name
        data_handler = DataHandler(root_data_folder=save_dir)
        save_data_dict.update({"fig_live": fig})
        data_handler.additional_files = {script_name: script_name, **default_additional_files}
        data_handler.save_data(data=save_data_dict, name=script_name.replace(".py", ""))
    
    plt.show()
    qm.close()


# %%
