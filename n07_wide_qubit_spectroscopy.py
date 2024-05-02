# %%
"""
        WIDE RESONATOR SPECTROSCOPY
This sequence involves measuring the resonator by sending a readout pulse and demodulating the signals to extract the
'I' and 'Q' quadratures across varying readout intermediate frequencies.
The data is then post-processed to determine the resonator resonance frequency.
This frequency can be used to update the readout intermediate frequency in the configuration under "resonator_IF".

Prerequisites:
    - Ensure calibration of the time of flight, offsets, and gains (referenced as "time_of_flight").
    - Calibrate the IQ mixer connected to the readout line (whether it's an external mixer or an Octave port).
    - Define the readout pulse amplitude and duration in the configuration.
    - Specify the expected resonator depletion time in the configuration.

Before proceeding to the next node:
    - Update the readout frequency, labeled as "resonator_IF", in the configuration.
"""

import qm.qua as qua
import qm as qm_api
import numpy as np
from configuration import config, qop_ip, cluster_name, u, depletion_time, readout_len, resonator_LO, mini_circuits_ip, qubit_LO
from qualang_tools.results import fetching_tool
from qualang_tools.loops import from_array
import matplotlib.pyplot as plt
from qualang_tools.results.data_handler import DataHandler
from qualang_tools.callable_from_qua import patch_qua_program_addons, callable_from_qua
from minicircuit_ssg_driver import MiniCircuitsSSG
import time

minisgs_module = MiniCircuitsSSG(host=mini_circuits_ip, port=80)

patch_qua_program_addons()

data_handler = DataHandler(root_data_folder="./")

@callable_from_qua
def set_lo_freq(element, frequency):
    # Here the LO frequency must be passed in kHz instead of Hz, 
    # because the QUA integer ranges in +/-2**31 ~ +/- 2.1e9
    print(f"setting the LO frequency of {element} to {frequency * 1e-6} GHz")
    minisgs_module.set_frequency(frequency * 1e3)
    time.sleep(1)

###################
# The QUA program #
###################
n_avg = 20  # The number of averages
# The frequency sweep parameters
f_min = 10 * u.MHz
f_max = 300 * u.MHz
df = 100 * u.kHz
frequencies = np.arange(f_min, f_max + 0.1, df)  # The frequency vector (+ 0.1 to add f_max to frequencies)

lo_min = 3.0 * u.GHz
lo_max = 7.0 * u.GHz
step_lo = f_max - f_min
lo_values = np.arange(lo_min, lo_max, step_lo)

wide_qubit_spectroscopy_data = {
    "n_avg": n_avg,
    "frequencies": frequencies,
    "lo_values": lo_values,
    "config": config
}

with qua.program() as qubit_spec:
    n = qua.declare(int)  # QUA variable for the averaging loop
    f_lo = qua.declare(int)
    f_if = qua.declare(int)  # QUA variable for the readout frequency
    I = qua.declare(qua.fixed)  # QUA variable for the measured 'I' quadrature
    Q = qua.declare(qua.fixed)  # QUA variable for the measured 'Q' quadrature
    I_st = qua.declare_stream()  # Stream for the 'I' quadrature
    Q_st = qua.declare_stream()  # Stream for the 'Q' quadrature

    with qua.for_(*from_array(f_lo, lo_values / 1e3)):
        
        set_lo_freq("qubit", f_lo)

        with qua.for_(n, 0, n < n_avg, n + 1):  # QUA for_ loop for averaging
            with qua.for_(*from_array(f_if, frequencies)):  # QUA for_ loop for sweeping the frequency
                # Update the frequency of the digital oscillator linked to the resonator element
                qua.update_frequency("qubit", f_if)
                qua.play("saturation", "qubit")
                qua.align("qubit", "resonator")
                # Measure the resonator (send a readout pulse and demodulate the signals to get the 'I' & 'Q' quadratures)
                qua.measure(
                    "readout",
                    "resonator",
                    None,
                    qua.dual_demod.full("cos", "out1", "sin", "out2", I),
                    qua.dual_demod.full("minus_sin", "out1", "cos", "out2", Q),
                )
                # Wait for the resonator to deplete
                qua.wait(depletion_time * u.ns, "resonator")
                # Save the 'I' & 'Q' quadratures to their respective streams
                qua.save(I, I_st)
                qua.save(Q, Q_st)

    with qua.stream_processing():
        # Cast the data into a 1D vector, average the 1D vectors together and store the results on the OPX processor
        I_st.buffer(len(frequencies)).buffer(n_avg).map(qua.FUNCTIONS.average()).buffer(len(lo_values)).save("I")
        Q_st.buffer(len(frequencies)).buffer(n_avg).map(qua.FUNCTIONS.average()).buffer(len(lo_values)).save("Q")

#####################################
#  Open Communication with the QOP  #
#####################################
qmm = qm_api.QuantumMachinesManager(host=qop_ip, cluster_name=cluster_name)

#######################
# Simulate or execute #
#######################
simulate = False

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = qm_api.SimulationConfig(duration=10_000)  # In clock cycles = 4ns
    # Simulate blocks python until the simulation is done
    job = qmm.simulate(config, qubit_spec, simulation_config)
    # Plot the simulated samples
    job.get_simulated_samples().con1.plot()

else:
    # Open the quantum machine
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(qubit_spec)
    # Get results from QUA program
    results = fetching_tool(job, data_list=["I", "Q"])
    I, Q = results.fetch_all()
    # Convert results into Volts
    S = u.demod2volts(I + 1j * Q, readout_len)
    R = np.abs(S)  # Amplitude
    phase = np.angle(S)  # Phase

    plt.figure()
    plt.title('Wide resonator spectroscopy')
    for i in range(len(lo_values)):
        plt.plot((frequencies + lo_values[i]) / u.GHz, R[i, :], color='b')
    plt.xlabel('Freq [GHz]')
    plt.ylabel('Magnitude')
    plt.tight_layout()

    wide_qubit_spectroscopy_data['I'] = I
    wide_qubit_spectroscopy_data['Q'] = Q
    wide_qubit_spectroscopy_data['R'] = R
    wide_qubit_spectroscopy_data['phase'] = phase

    data_handler.save_data(data=wide_qubit_spectroscopy_data, name="wide_qubit_spectroscopy")

    minisgs_module.set_frequency(qubit_LO)
    
    # Fit the results to extract the resonance frequency
    try:
        from qualang_tools.plot.fitting import Fit

        fit = Fit()
        plt.figure()
        res_spec_fit = fit.reflection_qubit_spectroscopy(frequencies / u.MHz, R, plot=True)
        plt.title(f"Resonator spectroscopy - LO = {resonator_LO / u.GHz} GHz")
        plt.xlabel("Intermediate frequency [MHz]")
        plt.ylabel(r"R=$\sqrt{I^2 + Q^2}$ [V]")
        print(f"Resonator resonance frequency to update in the config: resonator_IF = {res_spec_fit['f'][0]:.6f} MHz")

    except (Exception,):
        pass

# %%
