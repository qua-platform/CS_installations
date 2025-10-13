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
from qualang_tools.loops import from_array
from qm_saas import QmSaas, QOPVersion
from qm import SimulationConfig
import matplotlib.pyplot as plt
from pathlib import Path
from scipy.signal import savgol_filter
from qualang_tools.units import unit
u = unit(coerce_to_integer=True)
from macros import multiplexed_parser

# ---- Determine which device to run from ---- #
if False:
    from configurations.DA_5Q.OPX1000config import *
else:
    from configurations.DB_6Q.OPX1000config import *

# ---- Program parameters ---- #
n_avg = 200
resonator_qubit_keys = ["q0"] # Which qubit's resonator to use for the program, for this, best to run over just one.
required_parameters = ["resonator_key", "resonator_relaxation"]
res_key_subset, resonator_relaxation = multiplexed_parser(resonator_qubit_keys, multiplexed_parameters.copy(), required_parameters)

# ---- Time of Flight ---- #
reskey = res_key_subset[0] # Use the first resonator key in the subset
res_relaxation = resonator_relaxation[0]//4 # From ns to clock cycles

with program() as time_of_flight_prog:
    n = declare(int) # QUA variable for the averaging loop
    adc_st = declare_stream(adc_trace=True) # The stream to store the raw ADC trace

    with for_(n, 0, n < n_avg, n + 1): 
        reset_phase(reskey) # Reset the phase of the digital oscillator associated to the resonator element. Needed to average the cosine signal.
        measure("readout", reskey, adc_st) # Sends the readout pulse and stores the raw ADC traces in the stream called "adc_st"
        wait(res_relaxation, reskey) # Wait for the resonator to deplete
    with stream_processing():
        # Will save average:
        adc_st.input1().average().save("adc")

prog = time_of_flight_prog
# ---- Open communication with the OPX ---- #
from opx_credentials import qop_ip, cluster
qmm = QuantumMachinesManager(host=qop_ip, cluster_name=cluster)

simulate = True
if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=2_000)  # In clock cycles = 4ns
    # Simulate blocks python until the simulation is done
    job = qmm.simulate(config, prog, simulation_config)
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
    qm = qmm.open_qm(config, close_other_machines=True)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(prog)
    # Creates a result handle to fetch data from the OPX
    res_handles = job.result_handles
    # Waits (blocks the Python console) until all results have been acquired
    res_handles.wait_for_all_values()
    qm.close()

    # ---- Analysis ---- #
    adc = u.raw2volts(res_handles.get("adc").fetch_all())
    # Filter the data to get the pulse arrival time
    signal = savgol_filter(np.abs(adc), 11, 3)
    thresh = (np.mean(signal[:100]) + np.mean(signal[:-100])) / 2
    delay = np.where(signal > thresh)[0][0]
    delay = np.round(delay / 4) * 4  # Find the closest multiple integer of 4ns

    fig = plt.figure()
    plt.title("Averaged run")
    plt.plot(adc.real, "b", label="I")
    plt.plot(adc.imag, "r", label="Q")
    plt.axvline(delay, color="k", linestyle="--", label="ToF")
    plt.xlabel("Time (ns)")
    plt.legend()
    plt.tight_layout()
    plt.show()

    # Update the config
    print(f"Set time of flight to {time_of_flight + delay} ns")