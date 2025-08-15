#%%
from qm.qua import *
from qm import QuantumMachinesManager
from qm import SimulationConfig
from qualang_tools.plot import interrupt_on_close
from qualang_tools.results import wait_until_job_is_paused, fetching_tool, progress_counter, DataHandler
from scipy import signal
from configuration import *
import matplotlib.pyplot as plt
from qualang_tools.loops import from_array

###################
# The QUA program #
###################
# Parameters Definition
n_avg = 10  # The number of averages

# The readout amplitude sweep (as a pre-factor of the readout amplitude) - must be within [-0.5; 0.5)
f_min = 30 * u.MHz
f_max = 50 * u.MHz
df = 100 * u.kHz
frequencies = np.arange(f_min, f_max + 0.1, df)  # The frequency vector (+ 0.1 to add f_max to frequencies)

save_data_dict = {
    "n_avg": n_avg,
    "frequencies": frequencies,
    "config": config,
}

with program() as prog:
    n = declare(int)  # QUA variable for the averaging loop
    f = declare(int)  # QUA variable for the readout frequency
    I = declare(fixed)  # QUA variable for the measured 'I' quadrature
    Q = declare(fixed)  # QUA variable for the measured 'Q' quadrature
    I_st = declare_stream()  # Stream for the 'I' quadrature
    Q_st = declare_stream()  # Stream for the 'Q' quadrature
    n_st = declare_stream()  # Stream for the averaging iteration 'n'

    with for_(n, 0, n < n_avg, n + 1):  # QUA for_ loop for averaging
        with for_(*from_array(f, frequencies)):
            # and demodulate the signals to get the 'I' & 'Q' quadratures)
            reset_phase("test")
            update_frequency("test", f)
            measure(
                "readout",
                "test",
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

        I_st.buffer(len(frequencies)).average().save("I")
        Q_st.buffer(len(frequencies)).average().save("Q")
        n_st.save("iteration")



#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(host=qop_ip, port=qop_port, cluster_name=cluster_name)

#######################
# Simulate or execute #
#######################
simulate = False

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=2_000)  # In clock cycles = 4ns
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
        S = u.demod2volts(I + 1j * Q, readout_length)
        R = np.abs(S)*10*2/readout_amp
        # R = np.abs(S)
        phase = np.angle(S)  # Phase
        # Progress bar
        progress_counter(iteration, n_avg, start_time=results.get_start_time())

        plt.plot(frequencies, R, ".")
        plt.title("S21 measurement")
        plt.xlabel("Frequency (Hz)")
        plt.ylabel("S21")
        plt.ylim(0,1.1)
        plt.tight_layout()
        plt.show(block=True)

    script_name = Path(__file__).name
    data_handler = DataHandler(root_data_folder=save_dir)
    save_data_dict.update({"S21": R})
    save_data_dict.update({"fig_live": fig})
    data_handler.additional_files = {script_name: script_name, **default_additional_files}
    data_handler.save_data(data=save_data_dict, name="_".join(script_name.split("_")[1:]).split(".")[0])

plt.show()
