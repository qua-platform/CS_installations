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

from qm.qua import *
from qm import QuantumMachinesManager
from qm import SimulationConfig
from configuration import *
from qualang_tools.results import progress_counter, fetching_tool
from qualang_tools.plot import interrupt_on_close
from qualang_tools.loops import from_array
import matplotlib.pyplot as plt
from scipy import signal
from qualang_tools.results.data_handler import DataHandler

##################
#   Parameters   #
##################
# Parameters Definition
n_avg = 100  # The number of averages
# The frequency sweep parameters
span = 30* u.MHz
df = 100 * u.kHz
dfs = np.arange(-span, +span + 0.1, df) # The frequency vector (+ 0.1 to add f_max to frequencies)

# Data to save
save_data_dict = {
    "n_avg": n_avg,
    "dfs": dfs,
    "config": config,
}

###################
# The QUA program #
###################
with program() as resonator_spec:
    n = declare(int)  # QUA variable for the averaging loop
    df = declare(int)  # QUA variable for the readout frequency
    I1 = declare(fixed)  # QUA variable for the measured 'I' quadrature
    Q1 = declare(fixed)  # QUA variable for the measured 'Q' quadrature
    I2 = declare(fixed)  # QUA variable for the measured 'I' quadrature
    Q2 = declare(fixed)  # QUA variable for the measured 'Q' quadrature
    I3 = declare(fixed)  # QUA variable for the measured 'I' quadrature
    Q3 = declare(fixed)  # QUA variable for the measured 'Q' quadrature
    I1_st = declare_stream()  # Stream for the 'I' quadrature
    Q1_st = declare_stream()  # Stream for the 'Q' quadrature
    I2_st = declare_stream()  # Stream for the 'I' quadrature
    Q2_st = declare_stream()  # Stream for the 'Q' quadrature
    I3_st = declare_stream()  # Stream for the 'I' quadrature
    Q3_st = declare_stream()  # Stream for the 'Q' quadrature
    n_st = declare_stream()  # Stream for the averaging iteration 'n'
    reset_global_phase()

    with for_(n, 0, n < n_avg, n + 1):  # QUA for_ loop for averaging
        with for_(*from_array(df, dfs)):  # QUA for_ loop for sweeping the frequency
            # Update the frequency of the digital oscillator linked to the resonator element
            update_frequency("resonator", df + resonator_IF)
            update_frequency("resonator2", df + resonator_IF_2)
            update_frequency("resonator3", df + resonator_IF_3)
            # Measure the resonator (send a readout pulse and demodulate the signals to get the 'I' & 'Q' quadratures)
            measure(
                "readout",
                "resonator",
                None,
                dual_demod.full("cos", "sin", I1),
                dual_demod.full("minus_sin", "cos", Q1),
            )

            measure(
                "readout",
                "resonator2",
                None,
                dual_demod.full("cos", "sin", I2),
                dual_demod.full("minus_sin", "cos", Q2),
            )

            measure(
                "readout",
                "resonator3",
                None,
                dual_demod.full("cos", "sin", I3),
                dual_demod.full("minus_sin", "cos", Q3),
            )
            # Save the 'I' & 'Q' quadratures to their respective streams
            save(I1, I1_st)
            save(Q1, Q1_st)
            save(I2, I2_st)
            save(Q2, Q2_st)
            save(I3, I3_st)
            save(Q3, Q3_st)
        # Save the averaging iteration to get the progress bar
        save(n, n_st)

    with stream_processing():
        # Cast the data into a 1D vector, average the 1D vectors together and store the results on the OPX processor
        I1_st.buffer(len(dfs)).average().save("I1")
        Q1_st.buffer(len(dfs)).average().save("Q1")
        I2_st.buffer(len(dfs)).average().save("I2")
        Q2_st.buffer(len(dfs)).average().save("Q2")
        I3_st.buffer(len(dfs)).average().save("I3")
        Q3_st.buffer(len(dfs)).average().save("Q3")
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
    simulation_config = SimulationConfig(duration=10_000)  # In clock cycles = 4ns
    # Simulate blocks python until the simulation is done
    job = qmm.simulate(config, resonator_spec, simulation_config)
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
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(resonator_spec)
    # Get results from QUA program
    results = fetching_tool(job, data_list=["I1", "Q1", "I2", "Q2","I3", "Q3","iteration"], mode="live")
    fig = plt.figure()
    interrupt_on_close(fig, job)  # Interrupts the job when closing the figure
    while results.is_processing():
        # Fetch results
        I1, Q1, I2, Q2, I3, Q3,iteration = results.fetch_all()
        # Convert results into Volts
        S1 = u.demod2volts(I1 + 1j * Q1, readout_len)
        R1 = np.abs(S1)  # Amplitude
        phase1 = np.angle(S1)  # Phase

        S2 = u.demod2volts(I2 + 1j * Q2, readout_len)
        R2 = np.abs(S2)  # Amplitude
        phase2 = np.angle(S2)  # Phase

        S3 = u.demod2volts(I3 + 1j * Q3, readout_len)
        R3 = np.abs(S3)  # Amplitude
        phase3 = np.angle(S3)  # Phase
        # Progress bar
        progress_counter(iteration, n_avg, start_time=results.get_start_time())
        # Plot results
        side = 2.8  
        plt.gcf().set_size_inches(3*side, 2*side, forward=True)
        
        plt.suptitle(f"Resonator spectroscopy - LO = {resonator_LO / u.GHz} GHz")
        plt.subplot(2, 3, 1)
        plt.suptitle("Q3")
        plt.cla()
        plt.plot((dfs + resonator_IF) / u.MHz, R1, ".")
        plt.ylabel(r"$R=\sqrt{I^2 + Q^2}$ [V]")
        plt.subplot(2, 3, 4)
        plt.cla()
        plt.plot((dfs + resonator_IF) / u.MHz, signal.detrend(np.unwrap(phase1)), ".")
        plt.xlabel("Readout IF [MHz]")
        plt.ylabel("Phase [rad]")
        plt.gca().set_box_aspect(1)
        plt.tight_layout()


        plt.subplot(2, 3, 2)
        plt.suptitle("Q1")
        plt.cla()
        plt.plot((dfs + resonator_IF_2) / u.MHz, R2, ".")
        plt.ylabel(r"$R=\sqrt{I^2 + Q^2}$ [V]")
        plt.subplot(2, 3, 5)
        plt.cla()
        plt.plot((dfs + resonator_IF_2) / u.MHz, signal.detrend(np.unwrap(phase2)), ".")
        plt.xlabel("Readout IF [MHz]")
        plt.ylabel("Phase [rad]")
        plt.gca().set_box_aspect(1)
        plt.tight_layout()


        plt.subplot(2, 3, 3)
        plt.suptitle("Q2")
        plt.cla()
        plt.plot((dfs + resonator_IF_3) / u.MHz, R3, ".")
        plt.ylabel(r"$R=\sqrt{I^2 + Q^2}$ [V]")
        plt.subplot(2, 3, 6)
        plt.cla()
        plt.plot((dfs + resonator_IF_3) / u.MHz, signal.detrend(np.unwrap(phase3)), ".")
        plt.xlabel("Readout IF [MHz]")
        plt.ylabel("Phase [rad]")
        plt.gca().set_box_aspect(1)
        plt.pause(0.1)
        plt.tight_layout()




    # Close the quantum machines at the end in order to put all flux biases to 0 so that the fridge doesn't heat-up
    qm.close()
    # Save results
    script_name = Path(__file__).name
    data_handler = DataHandler(root_data_folder=save_dir)
    save_data_dict.update({"I1_data": I1})
    save_data_dict.update({"Q1_data": Q1})
    save_data_dict.update({"I1_data": I2})
    save_data_dict.update({"Q1_data": Q2})
    save_data_dict.update({"I1_data": I3})
    save_data_dict.update({"Q1_data": Q3})
    save_data_dict.update({"fig_live": fig})
    data_handler.additional_files = {script_name: script_name, **default_additional_files}
    data_handler.save_data(data=save_data_dict, name="_".join(script_name.split("_")[1:]).split(".")[0])

    plt.show(block=True)
