"""
TANK CIRCUIT SPECTROSCOPY (RF-REFLECTOMETRY)

The goal of this script is to perform the spectroscopy of the tank-circuit.

For this, the frequency of the element (pulser) used for reflectometry
readout is being swept and the signal reflected by the tank circuit is
being acquired, demodulated and integrated by the OPX.

A global averaging is performed (averaging on the most outer loop) and the
data is extracted while the program is running to display the frequency
response of the tank circuit with increasing SNR.

Prerequisites:
- Connect the tank circuit to the corresponding output and input channels.

Before proceeding to the next node:
- Update the config with the resonance frequency for reflectometry readout.

"""

from qm.qua import *
from qm import QuantumMachinesManager
from qm import SimulationConfig
from configuration import *
from qualang_tools.results import progress_counter, fetching_tool, DataHandler
from qualang_tools.plot import interrupt_on_close
from qualang_tools.loops import from_array
import matplotlib.pyplot as plt
from scipy import signal

###################
# The QUA program #
###################
n_avg = 2  # Number of averaging loops
# The frequency axis
frequencies = np.arange(200 * u.MHz, 400 * u.MHz, 0.1 * u.MHz)

with program() as reflectometry_spectroscopy:
    f = declare(int)  # QUA variable for the frequency sweep
    n = declare(int)  # QUA variable for the averaging loop
    I = declare(fixed)  # QUA variable for the measured 'I' quadrature
    Q = declare(fixed)  # QUA variable for the measured 'Q' quadrature
    I_st = declare_stream()  # Stream for the 'I' quadrature
    Q_st = declare_stream()  # Stream for the 'Q' quadrature
    n_st = declare_stream()  # Stream for the averaging iteration 'n'

    with for_(n, 0, n < n_avg, n + 1):
        with for_(*from_array(f, frequencies)):
            # Update the frequency of the tank_circuit element
            update_frequency("source_resonator", f)
            # RF reflectometry: the voltage measured by the analog input 2 is recorded, demodulated at the readout
            # frequency and the integrated quadratures are stored in "I" and "Q"
            measure(
                "readout",
                "source_resonator",
                None,
                demod.full("cos", I, "out1"),
                demod.full("sin", Q, "out1")
            )
            save(I, I_st)
            save(Q, Q_st)
            # Wait at each iteration in order to ensure that the data will not be transferred faster than 1 sample
            # per µs to the stream processing. Otherwise, the processor will receive the samples faster than it can
            # process them which can cause the OPX to crash.
            wait(1_000 * u.ns)  # in ns
        save(n, n_st)

    with stream_processing():
        I_st.buffer(len(frequencies)).average().save("I")
        Q_st.buffer(len(frequencies)).average().save("Q")
        n_st.save("iteration")

#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(host=qop_ip, port=qop_port, cluster_name=cluster_name, octave=None)

#######################
# Simulate or execute #
#######################
simulate = False

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=10_000)  # In clock cycles = 4ns
    # Simulate blocks python until the simulation is done
    job = qmm.simulate(config, reflectometry_spectroscopy, simulation_config)
    # Plot the simulated samples
    job.get_simulated_samples().con1.plot()

else:
    # Open the quantum machine
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(reflectometry_spectroscopy)
    # Get results from QUA program
    results = fetching_tool(job, data_list=["I", "Q", "iteration"], mode="live")
    # Live plotting
    fig = plt.figure()
    interrupt_on_close(fig, job)  # Interrupts the job when closing the figure
    while results.is_processing():
        # Fetch results
        I, Q, iteration = results.fetch_all()
        # Convert results into Volts
        S = u.demod2volts(I + 1j * Q, rf_readout_length)
        # S = 20*np.log10(S)
        R = np.abs(S)  # Amplitude
        R = 20*np.log10(R)
        phase = np.angle(S)  # Phase
        # Progress bar
        progress_counter(iteration, n_avg, start_time=results.get_start_time())
        # Plot results
        plt.suptitle("Tank-circuit Spectroscopy")
        plt.subplot(211)
        plt.cla()
        max_to_min = np.max(R) - np.min(R)
        plt.plot(frequencies / u.MHz, R, label=f"{max_to_min:3f} dB")
        plt.axhline(y=np.max(R), color='r', linestyle='--')
        plt.axhline(y=np.min(R), color='r', linestyle='--')
        plt.legend()
        plt.xlabel("Readout frequency [MHz]")
        plt.ylabel("Magnitude [dB]")
        plt.grid()
        plt.subplot(212)
        plt.cla()
        plt.plot(frequencies / u.MHz, signal.detrend(np.unwrap(phase)))
        plt.xlabel("Readout frequency [MHz]")
        plt.ylabel("Phase [rad]")
        plt.tight_layout()
        plt.pause(0.1)

    data_handler = DataHandler(root_data_folder=data_folder_path)
    data = {
        "frequency": frequencies,
        "measured_amplitude": S,
        "measured_phase": R,
        "figure": fig
    }
    # Save results
    data_folder = data_handler.save_data(data=data, name="tank_circuit_spectroscopy")

plt.show()