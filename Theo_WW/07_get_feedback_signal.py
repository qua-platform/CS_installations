from qm.qua import *
from qm.QuantumMachinesManager import QuantumMachinesManager
from qm import SimulationConfig
from configuration import *
from qualang_tools.results import progress_counter, fetching_tool
from qualang_tools.plot import interrupt_on_close
from qualang_tools.loops import from_array
import matplotlib.pyplot as plt
from scipy import signal
from scipy.optimize import curve_fit


##############################
# Program-specific variables #
##############################
n_avg = 100  # Number of averaging loops

total_readout_length = 1 * u.s
N_meas = int(total_readout_length / long_readout_len)
time = np.arange(0, total_readout_length, long_readout_len)
###################
# The QUA program #
###################

with program() as resonator_spec:
    n = declare(int)  # QUA variable for the averaging loop
    k = declare(int)  # QUA variable for the readout frequency
    dc = declare(fixed)  # QUA variable for the flux bias
    I = declare(fixed)  # QUA variable for the measured 'I' quadrature
    Q = declare(fixed)  # QUA variable for the measured 'Q' quadrature
    I_st = declare_stream()  # Stream for the 'I' quadrature
    Q_st = declare_stream()  # Stream for the 'Q' quadrature
    n_st = declare_stream()  # Stream for the averaging iteration 'n'


    with for_(n, 0, n < n_avg, n + 1):
        reset_phase("flux_line_sticky")
        play("const", "flux_line_sticky")

        with for_(k, 0, k < N_meas, k + 1):
            # Measure the FTR and demodulate the signals to get the 'I' & 'Q' quadratures
            measure(
                "long_readout",
                "FTR",
                None,
                dual_demod.full("cos", "out1", "sin", "out2", I),
                dual_demod.full("minus_sin", "out1", "cos", "out2", Q),
            )
            # Save the 'I' & 'Q' quadratures to their respective streams
            save(I, I_st)
            save(Q, Q_st)
        wait(10000)
        # Save the averaging iteration to get the progress bar
        save(n, n_st)

    with stream_processing():
        # Cast the data into a 2D matrix, average the 2D matrices together and store the results on the OPX processor
        I_st.buffer(N_meas).average().save("I")
        Q_st.buffer(N_meas).average().save("Q")
        n_st.save("iteration")


#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(host=qop_ip, port=qop_port, cluster_name=cluster_name, octave=octave_config)

#######################
# Simulate or execute #
#######################
simulate = False

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=100_000)  # In clock cycles = 4ns
    job = qmm.simulate(config, resonator_spec, simulation_config)
    job.get_simulated_samples().con1.plot()
else:
    # Open the quantum machine
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(resonator_spec)
    # Get results from QUA program
    results = fetching_tool(job, data_list=["I", "Q", "iteration"], mode="live")
    # Live plotting
    fig = plt.figure()
    interrupt_on_close(fig, job)  #  Interrupts the job when closing the figure
    while results.is_processing():
        # Fetch results
        I, Q, iteration = results.fetch_all()
        # Progress bar
        progress_counter(iteration, n_avg, start_time=results.get_start_time())
        # Convert results into Volts and normalize
        S = u.demod2volts(I + 1j * Q, readout_len)
        R = np.abs(S)  # Amplitude
        phase = np.angle(S)  # Phase
        # 2D spectroscopy plot
        plt.subplot(211)
        plt.cla()
        plt.suptitle(f"Resonator spectroscopy - LO = {resonator_LO / u.GHz} GHz")
        plt.title(r"$R=\sqrt{I^2 + Q^2}$")
        plt.plot(time, R)
        plt.ylabel("Readout IF [MHz]")
        plt.subplot(212)
        plt.cla()
        plt.title("Phase")
        plt.plot(time, signal.detrend(np.unwrap(phase)))
        plt.xlabel("Flux bias [V]")
        plt.ylabel("Readout IF [MHz]")
        plt.pause(0.1)
        plt.tight_layout()

    # Close the quantum machines at the end in order to put all flux biases to 0 so that the fridge doesn't heat-up
    qm.close()
