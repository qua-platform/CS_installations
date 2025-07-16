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
from qm import QuantumMachinesManager
from qm import SimulationConfig
from configuration_with_mwfem_lffem import *
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter
import matplotlib

matplotlib.use("TkAgg")

###################
# The QUA program #
###################
n_avg = 1000  # Number of averaging loops

with program() as tof_prog:
    n = declare(int)  # QUA variable for the averaging loop
    adc_st = declare_stream(adc_trace=True)  # The stream to store the raw ADC trace

    with for_(n, 0, n < n_avg, n + 1):
        # Reset the phase of the digital oscillator associated to the resonator element. Needed to average the cosine signal.
        reset_phase("tank_circuit")
        # Sends the readout pulse and stores the raw ADC traces in the stream called "adc_st"
        # measure("readout", "TIA", adc_st)
        measure("readout", "tank_circuit", adc_st)
        # Wait for the resonator to deplete
        wait(1_000 * u.ns, "tank_circuit")

    with stream_processing():
        # Please adjust the analog inputs according to the connectivity (input1/2 -> rf)
        # Will save average:
        adc_st.input1().average().save("adc1")
        # Will save only last run:
        adc_st.input1().save("adc1_single_run")


#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(host=qop_ip, cluster_name=cluster_name)

#######################
# Simulate or execute #
#######################
simulate = False
save_data = True

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=10_000)  # In clock cycles = 4ns
    # Simulate blocks python until the simulation is done
    job = qmm.simulate(config, tof_prog, simulation_config)
    # Plot the simulated samples
    job.get_simulated_samples().con1.plot()

else:
    # Open the quantum machine
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(tof_prog)
    # Creates a result handle to fetch data from the OPX
    res_handles = job.result_handles
    # Waits (blocks the Python console) until all results have been acquired
    res_handles.wait_for_all_values()
    # Fetch the raw ADC traces and convert them into Volts
    adc1_raw = res_handles.get("adc1").fetch_all()
    adc1 = u.raw2volts(adc1_raw)
    adc1_single_run = u.raw2volts(res_handles.get("adc1_single_run").fetch_all())
    # Derive the average values
    adc1_mean = np.mean(adc1)
    # Remove the average values
    adc1_unbiased = adc1 - np.mean(adc1)
    # Filter the data to get the pulse arrival time
    signal = savgol_filter(np.abs(1j * adc1_unbiased), 11, 3)
    # Detect the arrival of the readout signal
    th = (np.mean(signal[:100]) + np.mean(signal[:-100])) / 2
    delay = np.where(signal > th)[0][0]
    delay = np.round(delay / 4) * 4  # Find the closest multiple integer of 4ns

    # Plot data
    fig = plt.figure()
    plt.subplot(121)
    plt.title("Single run")
    plt.plot(adc1_single_run, "r", label="Input 2")
    xl = plt.xlim()
    yl = plt.ylim()
    plt.axhline(y=0.5)
    plt.axhline(y=-0.5)
    plt.plot(xl, adc1_mean * np.ones(2), "k--")
    plt.plot(delay * np.ones(2), yl, "k--")
    plt.xlabel("Time [ns]")
    plt.ylabel("Signal amplitude [V]")
    plt.legend()
    plt.subplot(122)
    plt.title("Averaged run")
    plt.plot(adc1, "r", label="Input 2")
    xl = plt.xlim()
    yl = plt.ylim()
    plt.plot(xl, adc1_mean * np.ones(2), "k--")
    plt.plot(delay * np.ones(2), yl, "k--")
    plt.xlabel("Time [ns]")
    plt.legend()
    plt.grid("all")
    plt.tight_layout()
    # plt.show()

    # Update the config
    print(f"DC offset to add to Q in the config: {-adc1_mean:.6f} V")
    print(f"Time Of Flight to add in the config: {delay} ns")

    if save_data:
        from qualang_tools.results.data_handler import DataHandler

        # Data to save
        save_data_dict = {}
        # save_data_dict["elapsed_time"] =  np.array([elapsed_time])
        save_data_dict["adc_rf"] = adc1_mean
        save_data_dict["adc_rf_single_run"] = adc1_single_run

        # Save results
        script_name = Path(__file__).name
        data_handler = DataHandler(root_data_folder=save_dir)
        save_data_dict.update({"fig_live": fig})
        data_handler.additional_files = {
            script_name: script_name,
            **default_additional_files,
        }
        data_handler.save_data(data=save_data_dict, name="time_of_flight_RF")

    # plt.show()
    qm.close()

# if save_data:
#         from qualang_tools.results.data_handler import DataHandler

#         # Data to save
#         save_data_dict = {}
#         # save_data_dict["elapsed_time"] =  np.array([elapsed_time])
#         save_data_dict["adc_rf"] = adc1_mean
#         save_data_dict["adc_rf_single_run"] = adc1_single_run

#         # Save results
#         script_name = Path(__file__).name
#         data_handler = DataHandler(root_data_folder=save_dir)
#         save_data_dict.update({"fig_live": fig})
#         data_handler.additional_files = {
#             script_name: script_name,
#             **default_additional_files,
#         }
#         data_handler.save_data(data=save_data_dict, name="time_of_flight_RF")


# %%
