"""
        RESONATOR SPECTROSCOPY VERSUS READOUT AMPLITUDE
This sequence involves measuring the resonator by sending a readout pulse and demodulating the signals to
extract the 'I' and 'Q' quadratures.
This is done across various readout intermediate dfs and amplitudes.
Based on the results, one can determine if a qubit is coupled to the resonator by noting the resonator frequency
splitting. This information can then be used to adjust the readout amplitude, choosing a readout amplitude value
just before the observed frequency splitting.

Prerequisites:
    - Calibration of the time of flight, offsets, and gains (referenced as "time_of_flight").
    - Calibration of the IQ mixer connected to the readout line (be it an external mixer or an Octave port).
    - Identification of the resonator's resonance frequency (referred to as "resonator_spectroscopy").
    - Configuration of the readout pulse amplitude (the pulse processor will sweep up to twice this value) and duration.
    - Specification of the expected resonator depletion time in the configuration.

Before proceeding to the next node:
    - Update the readout frequency, labeled as "resonator_IF", in the configuration.
    - Adjust the readout amplitude, labeled as "readout_amp", in the configuration.
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
n_avg = 1000  # The number of averages
# The frequency sweep around the resonator frequency "resonator_IF"
span = 5 * u.MHz
df = 200 * u.kHz
dfs = np.arange(-span, +span + 0.1, df)
# The readout amplitude sweep (as a pre-factor of the readout amplitude) - must be within [-2; 2)
a_min = 0.001
a_max = 1
amplitudes = np.geomspace(a_min, a_max, 40)

# Data to save
save_data_dict = {
    "n_avg": n_avg,
    "dfs": dfs,
    "amplitudes": amplitudes,
    "config": config,
}

###################
# The QUA program #
###################
with program() as resonator_spec_2D:
    n = declare(int)  # QUA variable for the averaging loop
    df = declare(int)  # QUA variable for the readout frequency
    a = declare(fixed)  # QUA variable for the readout amplitude pre-factor
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
            with for_each_(a, amplitudes):  # QUA for_ loop for sweeping the readout amplitude
                # Measure the resonator (send a readout pulse whose amplitude is rescaled by the pre-factor 'a' [-2, 2)
                # and demodulate the signals to get the 'I' & 'Q' quadratures)
                measure(
                    "readout" * amp(a),
                    "resonator",
                    None,
                    dual_demod.full("cos", "sin", I1),
                    dual_demod.full("minus_sin", "cos", Q1),
                )

                measure(
                    "readout" * amp(a),
                    "resonator2",
                    None,
                    dual_demod.full("cos", "sin", I2),
                    dual_demod.full("minus_sin", "cos", Q2),
                )

                measure(
                    "readout" * amp(a),
                    "resonator3",
                    None,
                    dual_demod.full("cos", "sin", I3),
                    dual_demod.full("minus_sin", "cos", Q3),
                )

                # Wait for the resonator to deplete
                wait(depletion_time * u.ns)
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
        # Cast the data into a 2D matrix, average the 2D matrices together and store the results on the OPX processor
        # Note that the buffering goes from the most inner loop (left) to the most outer one (right)
        I1_st.buffer(len(amplitudes)).buffer(len(dfs)).average().save("I1")
        Q1_st.buffer(len(amplitudes)).buffer(len(dfs)).average().save("Q1")
        I2_st.buffer(len(amplitudes)).buffer(len(dfs)).average().save("I2")
        Q2_st.buffer(len(amplitudes)).buffer(len(dfs)).average().save("Q2")
        I3_st.buffer(len(amplitudes)).buffer(len(dfs)).average().save("I3")
        Q3_st.buffer(len(amplitudes)).buffer(len(dfs)).average().save("Q3")
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
    job = qmm.simulate(config, resonator_spec_2D, simulation_config)
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
    job = qm.execute(resonator_spec_2D)
    # Get results from QUA program
    results = fetching_tool(job, data_list=["I1", "Q1", "I2", "Q2","I3", "Q3","iteration"], mode="live")
    # Live plotting
    fig = plt.figure()
    interrupt_on_close(fig, job)  #  Interrupts the job when closing the figure
    while results.is_processing():
        # Fetch results
        I1, Q2, I2, Q2,I3, Q3,iteration = results.fetch_all()
        # Progress bar
        progress_counter(iteration, n_avg, start_time=results.get_start_time())
        # Convert results into Volts and normalize
        S1 = u.demod2volts(I1 + 1j * Q1, readout_len)
        R1 = np.abs(S1)  # Amplitude
        phase1 = np.angle(S1)  # Phase
        # Normalize data
        row_sums = R1.sum(axis=0)
        R1 /= row_sums[np.newaxis, :]

        S2 = u.demod2volts(I2 + 1j * Q2, readout_len)
        R2 = np.abs(S2)  # Amplitude
        phase2 = np.angle(S2)  # Phase
        # Normalize data
        row_sums = R2.sum(axis=0)
        R2 /= row_sums[np.newaxis, :]

        S3 = u.demod2volts(I3 + 1j * Q3, readout_len)
        R3 = np.abs(S3)  # Amplitude
        phase3 = np.angle(S3)  # Phase
        # Normalize data
        row_sums = R3.sum(axis=0)
        R3 /= row_sums[np.newaxis, :]

        side = 2.8  
        plt.gcf().set_size_inches(3*side, 2*side, forward=True)

        # 2D spectroscopy plot
        plt.subplot(2, 3, 1)
        plt.suptitle(f"Resonator spectroscopy - LO = {resonator_LO / u.GHz} GHz & IF = {resonator_IF / u.MHz} MHz")
        plt.cla()
        plt.title(r"$R=\sqrt{I^2 + Q^2}$ (normalized)")
        plt.pcolor(amplitudes * readout_amp, dfs / u.MHz, R1)
        plt.xscale("log")
        plt.xlim(amplitudes[0] * readout_amp, amplitudes[-1] * readout_amp)
        plt.ylabel("Readout detuning [MHz]")
        plt.subplot(2, 3, 4)
        plt.cla()
        plt.title("Phase")
        plt.pcolor(amplitudes * readout_amp, dfs / u.MHz, signal.detrend(np.unwrap(phase1)))
        plt.ylabel("Readout detuning [MHz]")
        plt.xlabel("Readout amplitude [V]")
        plt.xscale("log")
        plt.xlim(amplitudes[0] * readout_amp, amplitudes[-1] * readout_amp)
        plt.gca().set_box_aspect(1)

        plt.subplot(2, 3, 2)
        plt.suptitle(f"Resonator spectroscopy - LO = {resonator_LO / u.GHz} GHz & IF = {resonator_IF_2 / u.MHz} MHz")
        plt.cla()
        plt.title(r"$R=\sqrt{I^2 + Q^2}$ (normalized)")
        plt.pcolor(amplitudes * readout_amp_2, dfs / u.MHz, R2)
        plt.xscale("log")
        plt.xlim(amplitudes[0] * readout_amp_2, amplitudes[-1] * readout_amp_2)
        plt.ylabel("Readout detuning [MHz]")
        plt.subplot(2, 3, 5)
        plt.cla()
        plt.title("Phase")
        plt.pcolor(amplitudes * readout_amp_2, dfs / u.MHz, signal.detrend(np.unwrap(phase2)))
        plt.ylabel("Readout detuning [MHz]")
        plt.xlabel("Readout amplitude [V]")
        plt.xscale("log")
        plt.xlim(amplitudes[0] * readout_amp_2, amplitudes[-1] * readout_amp_2)
        plt.gca().set_box_aspect(1)

        plt.subplot(2, 3, 3)
        plt.suptitle(f"Resonator spectroscopy - LO = {resonator_LO / u.GHz} GHz & IF = {resonator_IF_3 / u.MHz} MHz")
        plt.cla()
        plt.title(r"$R=\sqrt{I^2 + Q^2}$ (normalized)")
        plt.pcolor(amplitudes * readout_amp_3, dfs / u.MHz, R3)
        plt.xscale("log")
        plt.xlim(amplitudes[0] * readout_amp_3, amplitudes[-1] * readout_amp_3)
        plt.ylabel("Readout detuning [MHz]")
        plt.subplot(2, 3, 6)
        plt.cla()
        plt.title("Phase")
        plt.pcolor(amplitudes * readout_amp_3, dfs / u.MHz, signal.detrend(np.unwrap(phase3)))
        plt.ylabel("Readout detuning [MHz]")
        plt.xlabel("Readout amplitude [V]")
        plt.xscale("log")
        plt.xlim(amplitudes[0] * readout_amp_3, amplitudes[-1] * readout_amp_3)
        plt.gca().set_box_aspect(1)

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

