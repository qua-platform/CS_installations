"""
        RESONATOR SPECTROSCOPY
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
from configuration import config, qop_ip, cluster_name, u, thermalization_time, readout_len, resonator_LO
from qualang_tools.results import progress_counter, fetching_tool
from qualang_tools.plot import interrupt_on_close
from qualang_tools.loops import from_array
import matplotlib.pyplot as plt
from scipy import signal
from qualang_tools.results.data_handler import DataHandler

data_handler = DataHandler(root_data_folder="./")

###################
# The QUA program #
###################
n_avg = 1000  # The number of averages
# The frequency sweep parameters
f_min = 30 * u.MHz
f_max = 70 * u.MHz
df = 100 * u.kHz
frequencies = np.arange(f_min, f_max + 0.1, df)  # The frequency vector (+ 0.1 to add f_max to frequencies)

qubit_resonator_2chi_data = {
    "n_avg": n_avg,
    "frequencies": frequencies,
    "config": config
}

with qua.program() as qubit_resonator_2chi:
    n = qua.declare(int)  # QUA variable for the averaging loop
    f = qua.declare(int)  # QUA variable for the readout frequency
    I = qua.declare(qua.fixed)  # QUA variable for the measured 'I' quadrature
    Q = qua.declare(qua.fixed)  # QUA variable for the measured 'Q' quadrature
    I_st = qua.declare_stream()  # Stream for the 'I' quadrature
    Q_st = qua.declare_stream()  # Stream for the 'Q' quadrature
    n_st = qua.declare_stream()  # Stream for the averaging iteration 'n'

    with qua.for_(n, 0, n < n_avg, n + 1):  # QUA for_ loop for averaging
        # Save the averaging iteration to get the progress bar
        qua.save(n, n_st)
        with qua.for_(*from_array(f, frequencies)):  # QUA for_ loop for sweeping the frequency
            # Wait for the qubit to decay
            qua.wait(thermalization_time * u.ns, "resonator")
            # Update the frequency of the digital oscillator linked to the resonator element
            qua.update_frequency("resonator", f)
            # Measure the resonator (send a readout pulse and demodulate the signals to get the 'I' & 'Q' quadratures)
            qua.measure(
                "readout",
                "resonator",
                None,
                qua.dual_demod.full("cos", "out1", "sin", "out2", I),
                qua.dual_demod.full("minus_sin", "out1", "cos", "out2", Q),
            )
            # Save the 'I' & 'Q' quadratures to their respective streams
            qua.save(I, I_st)
            qua.save(Q, Q_st)

            qua.align()

            # Wait for the qubit to decay
            qua.wait(thermalization_time * u.ns, "resonator")
            qua.play("x180", "qubit")
            qua.align("qubit", "resonator")
            # Update the frequency of the digital oscillator linked to the resonator element
            qua.update_frequency("resonator", f)
            # Measure the resonator (send a readout pulse and demodulate the signals to get the 'I' & 'Q' quadratures)
            qua.measure(
                "readout",
                "resonator",
                None,
                qua.dual_demod.full("cos", "out1", "sin", "out2", I),
                qua.dual_demod.full("minus_sin", "out1", "cos", "out2", Q),
            )
            # Save the 'I' & 'Q' quadratures to their respective streams
            qua.save(I, I_st)
            qua.save(Q, Q_st)

    with qua.stream_processing():
        # Cast the data into a 1D vector, average the 1D vectors together and store the results on the OPX processor
        I_st.bufer(2).buffer(len(frequencies)).average().save("I")
        Q_st.bufer(2).buffer(len(frequencies)).average().save("Q")
        n_st.save("iteration")

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
    job = qmm.simulate(config, qubit_resonator_2chi, simulation_config)
    # Plot the simulated samples
    job.get_simulated_samples().con1.plot()

else:
    # Open the quantum machine
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(qubit_resonator_2chi)
    # Get results from QUA program
    results = fetching_tool(job, data_list=["I", "Q", "iteration"], mode="live")
    # Live plotting
    fig = plt.figure()
    interrupt_on_close(fig, job)  # Interrupts the job when closing the figure
    while results.is_processing():
        # Fetch results
        I, Q, iteration = results.fetch_all()
        # Convert results into Volts
        S = u.demod2volts(I + 1j * Q, readout_len)
        R = np.abs(S)  # Amplitude
        phase = np.angle(S)  # Phase
        # Progress bar
        progress_counter(iteration, n_avg, start_time=results.get_start_time())
        # Plot results
        plt.suptitle(f"Resonator spectroscopy - LO = {resonator_LO / u.GHz} GHz")
        ax1 = plt.subplot(211)
        plt.cla()
        plt.plot(frequencies / u.MHz, R[:, 0], ".")
        plt.plot(frequencies / u.MHz, R[:, 1], ".")
        plt.ylabel(r"$R=\sqrt{I^2 + Q^2}$ [V]")
        plt.subplot(212, sharex=ax1)
        plt.cla()
        plt.plot(frequencies / u.MHz, signal.detrend(np.unwrap(phase[:, 0])), ".")
        plt.plot(frequencies / u.MHz, signal.detrend(np.unwrap(phase[:, 1])), ".")
        plt.xlabel("Intermediate frequency [MHz]")
        plt.ylabel("Phase [rad]")
        plt.tight_layout()
        plt.pause(1)

    qubit_resonator_2chi_data['I'] = I
    qubit_resonator_2chi_data['Q'] = Q
    qubit_resonator_2chi_data['R'] = R
    qubit_resonator_2chi_data['phase'] = phase

    data_handler.save_data(data=qubit_resonator_2chi_data, name="qubit_resonator_2chi")
    
    # Fit the results to extract the resonance frequency
    try:
        from qualang_tools.plot.fitting import Fit

        fit = Fit()
        plt.figure()
        res_spec_fit = fit.transmission_qubit_resonator_2chitroscopy(frequencies / u.MHz, R[:, 0], plot=True)
        plt.title(f"Resonator spectroscopy - LO = {resonator_LO / u.GHz} GHz")
        plt.xlabel("Intermediate frequency [MHz]")
        plt.ylabel(r"R=$\sqrt{I^2 + Q^2}$ [V]")
        print(f"Resonator resonance frequency to update in the config: resonator_IF = {res_spec_fit['f'][0]:.6f} MHz")
    except (Exception,):
        pass

    # Fit the results to extract the resonance frequency
    try:
        from qualang_tools.plot.fitting import Fit

        fit = Fit()
        plt.figure()
        res_spec_fit = fit.transmission_qubit_resonator_2chitroscopy(frequencies / u.MHz, R[:, 1], plot=True)
        plt.title(f"Resonator spectroscopy - LO = {resonator_LO / u.GHz} GHz")
        plt.xlabel("Intermediate frequency [MHz]")
        plt.ylabel(r"R=$\sqrt{I^2 + Q^2}$ [V]")
        print(f"Resonator resonance frequency to update in the config: resonator_IF = {res_spec_fit['f'][0]:.6f} MHz")
    except (Exception,):
        pass
