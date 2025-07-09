#%%
from qm.qua import *
from qm import QuantumMachinesManager
from qm import SimulationConfig
from qualang_tools.plot import interrupt_on_close
from qualang_tools.results import wait_until_job_is_paused, fetching_tool, progress_counter, DataHandler
from scipy import signal

from configuration_oscilloscope import *
import matplotlib.pyplot as plt

from macros import measure_current, measure_lock_in, fetch_results_current, fetch_results_lock_in

###################
# The QUA program #
###################
# Parameters Definition
n_avg = 100  # The number of averages

# The readout amplitude sweep (as a pre-factor of the readout amplitude) - must be within [-0.5; 0.5)
a_min = 0.5
a_max = 1
amplitudes = np.geomspace(a_min, a_max, 20)

with program() as prog:
    n = declare(int)  # QUA variable for the averaging loop
    a = declare(fixed)  # QUA variable for the readout amplitude pre-factor
    I = declare(fixed)  # QUA variable for the measured 'I' quadrature
    Q = declare(fixed)  # QUA variable for the measured 'Q' quadrature
    I_st = declare_stream()  # Stream for the 'I' quadrature
    Q_st = declare_stream()  # Stream for the 'Q' quadrature
    n_st = declare_stream()  # Stream for the averaging iteration 'n'

    with for_(n, 0, n < n_avg, n + 1):  # QUA for_ loop for averaging
        with for_each_(a, amplitudes):
            # and demodulate the signals to get the 'I' & 'Q' quadratures)
            measure(
                "readout" * amp(a),
                "resistance_tia_lock_in",
                None,
                demod.full("cos", I, "out1"),
                demod.full("sin", Q, "out1")
            )
            wait(50)
            # Save the 'I' & 'Q' quadratures to their respective streams
            save(I, I_st)
            save(Q, Q_st)
        # Save the averaging iteration to get the progress bar
        save(n, n_st)

    with stream_processing():

        I_st.buffer(len(amplitudes)).average().save("I")
        Q_st.buffer(len(amplitudes)).average().save("Q")
        n_st.save("iteration")



#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(**qmm_settings)

#######################
# Simulate or execute #
#######################
simulate = False

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=5_000)  # In clock cycles = 4ns
    # Simulate blocks python until the simulation is done
    job = qmm.simulate(config, prog, simulation_config)
    # Get the simulated samples
    samples = job.get_simulated_samples()
    # Get the waveform report object
    waveform_report = job.get_simulated_waveform_report()
    # Cast the waveform report to a python dictionary
    waveform_dict = waveform_report.to_dict()
    # Visualize and save the waveform report
    waveform_report.create_plot(samples, plot=True, save_path=save_dir / "waveform_report.html")
else:
    # Open the quantum machine
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(prog)
    # Get results from QUA program
    results = fetching_tool(job, data_list=["I", "Q", "iteration"], mode="live")
    # Live plotting
    fig = plt.figure()
    interrupt_on_close(fig, job)  # Interrupts the job when closing the figure
    while results.is_processing():
        # Fetch results
        I, Q, iteration = results.fetch_all()
        # Convert results into Volts
        S = u.demod2volts(I + 1j * Q, lock_in_length)
        R = np.abs(S)  # Amplitude
        R_A = R * tia_iv_scale_factor
        phase = np.angle(S)  # Phase
        # Progress bar
        progress_counter(iteration, n_avg, start_time=results.get_start_time())
        # Plot results
        plt.suptitle(f"Resistance lock-in measurement")
        ax1 = plt.subplot(211)
        plt.cla()
        plt.plot(amplitudes, R, ".")
        plt.ylabel("TIA Receive Volatage [V]")
        plt.subplot(212, sharex=ax1)
        plt.cla()
        # plt.plot(amplitudes, signal.detrend(np.unwrap(phase)), ".")
        plt.plot(amplitudes, R_A, ".")
        plt.xlabel("Output Volatage")
        plt.ylabel("Current [A]")
        plt.pause(0.1)
        plt.tight_layout()

    data_handler = DataHandler(root_data_folder=save_dir)
    data = {
        "I_data": I,
        "Q_data": Q,
        "figure": fig
    }
    # Save results
    data_folder = data_handler.save_data(data=data, name=f"Resistance_measurements")

plt.show()
