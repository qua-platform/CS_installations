# %%
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
from qm import QuantumMachinesManager, SimulationConfig
from qm import SimulationConfig

from configuration import *
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter
from qualang_tools.results.data_handler import DataHandler
import matplotlib
import time

# matplotlib.use('TkAgg')


##################
#   Parameters   #
##################

n_avg = 5000  # The number of averages
elem = "detector"

save_data_dict = {
    "detector": elem,
    "n_avg": n_avg,
    "config": config,
}


###################
#   QUA Program   #
###################

with program() as PROGRAM:
    n = declare(int)  # QUA variable for the averaging loop
    adc_st = declare_stream(adc_trace=True)  # The stream to store the raw ADC trace

    with for_(n, 0, n < n_avg, n + 1):
        # Reset the phase of the digital oscillator associated to the resonator element. Needed to average the cosine signal.
        reset_if_phase(elem)
        # Sends the readout pulse and stores the raw ADC traces in the stream called "adc_st"
        play("on", "occupation_matrix_dummy")
        measure("short_readout", elem, adc_stream=adc_st)
        # Wait for saving
        wait(1 * u.us, elem)

    with stream_processing():
        if config["elements"]["detector"]["outputs"]["out1"][1] == 1:
            # Will save average:
            adc_st.input1().average().save(f"adc")
            # Will save only last run:
            adc_st.input1().save(f"adc_single_run")
        else:
            # Will save average:
            adc_st.input2().average().save(f"adc")
            # Will save only last run:
            adc_st.input2().save(f"adc_single_run")


if __name__ == "__main__":
    #####################################
    #  Open Communication with the QOP  #
    #####################################
    qmm = QuantumMachinesManager(host=qop_ip, cluster_name=cluster_name)

    ###########################
    # Run or Simulate Program #
    ###########################

    simulate = False

    if simulate:
        # Simulates the QUA program for the specified duration
        simulation_config = SimulationConfig(duration=1_000)  # In clock cycles = 4ns
        # Simulate blocks python until the simulation is done
        job = qmm.simulate(config, PROGRAM, simulation_config)
        # Plot the simulated samples
        job.get_simulated_samples().con1.plot()

    else:
        try:
            # Open a quantum machine to execute the QUA program
            qm = qmm.open_qm(config)
            # Send the QUA program to the OPX, which compiles and executes it
            job = qm.execute(PROGRAM)
            # Creates a result handle to fetch data from the OPX
            res_handles = job.result_handles
            # Waits (blocks the Python console) until all results have been acquired
            res_handles.wait_for_all_values()
            # Fetch the raw ADC traces and convert them into Volts
            adc0 = u.raw2volts(res_handles.get("adc").fetch_all())
            adc0_single_run = u.raw2volts(res_handles.get("adc_single_run").fetch_all())

            save_data_dict["adc"] = adc0
            save_data_dict["adc_single"] = adc0_single_run

            # Derive the average values
            adc0_mean = np.mean(adc0)
            # Remove the average values
            adc0_unbiased = adc0 - np.mean(adc0)
            # Filter the data to get the pulse arrival time
            signal = savgol_filter(np.abs(adc0_unbiased), 11, 3)
            # Detect the arrival of the readout signal
            th = (np.mean(signal[:100]) + np.mean(signal[:-100])) / 2
            delay = np.where(signal > th)[0][0]

            # Plot data for each rl
            fig = plt.figure(figsize=(12, 6))
            plt.suptitle(f"Readout for {elem}")

            # Plot for single run
            plt.subplot(121)
            plt.title("Single run")
            plt.plot(adc0_single_run, label="Input")
            plt.axhline(y=0)
            plt.xlabel("Time [ns]")
            plt.ylabel("Signal amplitude [V]")
            plt.legend()

            # Plot for averaged run
            plt.subplot(122)
            plt.title("Averaged run")
            plt.plot(adc0, label="Input")
            plt.axhline(y=0)
            plt.xlabel("Time [ns]")
            plt.legend()
            plt.tight_layout()

            # Save results
            script_name = Path(__file__).name
            data_handler = DataHandler(root_data_folder=save_dir)
            save_data_dict.update({"fig_live": fig})
            data_handler.additional_files = {script_name: script_name, **default_additional_files}
            data_handler.save_data(data=save_data_dict, name="time_of_flight")

        except Exception as e:
            print(f"An exception occurred: {e}")

        finally:
            qm.close()
            print("Experiment QM is now closed")
            plt.show()

# %%
