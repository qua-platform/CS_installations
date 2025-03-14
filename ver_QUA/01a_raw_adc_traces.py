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
from configuration_with_lffem_octave import *
import matplotlib.pyplot as plt
import matplotlib
import time

matplotlib.use('TkAgg')

###################
# The QUA program #
###################
n_avg = 1000  # The number of averages

with program() as raw_trace_prog:
    n = declare(int)  # QUA variable for the averaging loop
    adc_st = declare_stream(adc_trace=True)  # The stream to store the raw ADC trace

    with for_(n, 0, n < n_avg, n + 1):  # QUA for_ loop for averaging
        # Make sure that the readout pulse is sent with the same phase so that the acquired signal does not average out
        reset_phase("rr1")
        # Measure the resonator (send a readout pulse and record the raw ADC trace)
        measure("readout", "rr1", adc_st)
        # Wait for the resonator to deplete
        wait(depletion_time * u.ns, "rr1")

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

###########################
# Run or Simulate Program #
###########################
simulate = False
save_data = True

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=10_000)  # In clock cycles = 4ns
    # Simulate blocks python until the simulation is done
    job = qmm.simulate(config, raw_trace_prog, simulation_config)
    # Plot the simulated samples
    job.get_simulated_samples().con1.plot()
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
    adc1_single_run = u.raw2volts(res_handles.get("adc1_single_run").fetch_all())
    adc2_single_run = u.raw2volts(res_handles.get("adc2_single_run").fetch_all())
    
    import time
    time.sleep(10)

    # Plot data
    fig = plt.figure()
    plt.subplot(121)
    plt.title("Single run")
    plt.plot(adc1_single_run, label="Input 1")
    plt.plot(adc2_single_run, label="Input 2")
    plt.xlabel("Time [ns]")
    plt.ylabel("Signal amplitude [V]")
    plt.legend()

    plt.subplot(122)
    plt.title("Averaged run")
    plt.plot(adc1, label="Input 1")
    plt.plot(adc2, label="Input 2")
    plt.xlabel("Time [ns]")
    plt.legend()
    plt.tight_layout()

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
