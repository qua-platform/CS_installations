import numpy as np
from qm.qua import *
from qm import QuantumMachinesManager
from qm import SimulationConfig
from configuration_OPX1000 import *
from qualang_tools.loops import from_array
from qualang_tools.results import fetching_tool, progress_counter
from macros import interrupt_on_close
from scipy import signal
import matplotlib.pyplot as plt
import plotly.io as pio
pio.renderers.default='browser'

# get the config
config = get_config(sampling_rate=2e9)

###################
# The QUA program #
###################
n_avg = 100
frequencies = np.arange(-900e6, 900e6, 0.1e6)
amplitudes = np.logspace(-4, 0, 51)
with program() as rf_reflectometry:
    I = declare(fixed)
    Q = declare(fixed)
    n = declare(int)
    f = declare(int)
    a = declare(fixed)
    n_st = declare_stream()
    I_st = declare_stream()
    Q_st = declare_stream()

    with for_(n, 0, n < n_avg, n + 1):  # The averaging loop
        play("const", "scope_trigger")
        with for_(*from_array(f, frequencies)):
            update_frequency("lf_readout_element", f)
            with for_(*from_array(a, amplitudes)):
                measure("readout" * amp(a), "lf_readout_element", None,
                        demod.full("cos", I, "out1"),
                        demod.full("sin", Q, "out1"))
                save(I, I_st)
                save(Q, Q_st)
                wait(200 * u.ns)
        save(n, n_st)

    with stream_processing():
        I_st.buffer(len(amplitudes)).buffer(len(frequencies)).average().save("I")
        Q_st.buffer(len(amplitudes)).buffer(len(frequencies)).average().save("Q")
        n_st.save("iteration")

#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(host=qop_ip, port=qop_port, cluster_name=cluster_name)

###########################
# Run or Simulate Program #
###########################

simulate = True

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=10_000)  # In clock cycles = 4ns
    # Simulate blocks python until the simulation is done
    job = qmm.simulate(config, rf_reflectometry, simulation_config)
    # Plot the simulated samples
    job.get_simulated_samples().con1.plot()
    # Get the waveform report
    samples = job.get_simulated_samples()
    waveform_report = job.get_simulated_waveform_report()
    waveform_report.create_plot(samples, plot=True, save_path=None)
    samples = job.get_simulated_samples()
    waveform_report = job.get_simulated_waveform_report()
else:
    # Open a quantum machine to execute the QUA program
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it - Execute does not block python!
    job = qm.execute(rf_reflectometry)
    # Get results from QUA program
    results = fetching_tool(job, data_list=["I", "Q", "iteration"], mode="live")
    # Live plotting
    fig = plt.figure()
    interrupt_on_close(fig, job)  # Interrupts the job when closing the figure
    while results.is_processing():
        # Fetch results
        I, Q, iteration = results.fetch_all()
        # Progress bar
        progress_counter(iteration, n_avg, start_time=results.get_start_time())
        # Convert results into Volts and normalize
        S = u.demod2volts(I + 1j * Q, readout_len)
        R = np.abs(S)  # Amplitude
        phase = np.angle(S)  # Phase
        # Normalize data
        row_sums = R.sum(axis=0)
        R /= row_sums[np.newaxis, :]
        # 2D spectroscopy plot
        plt.subplot(211)
        plt.cla()
        plt.title(r"$R=\sqrt{I^2 + Q^2}$ (normalized)")
        plt.pcolor(amplitudes * readout_amp, f / u.MHz, R)
        plt.ylabel("Readout frequency [MHz]")
        plt.subplot(212)
        plt.cla()
        plt.title("Phase")
        plt.pcolor(amplitudes * readout_amp, f / u.MHz, signal.detrend(np.unwrap(phase)))
        plt.ylabel("Readout frequency [MHz]")
        plt.xlabel("Readout amplitude [V]")
        plt.pause(0.1)
        plt.tight_layout()
