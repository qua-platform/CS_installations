# %%
"""
        RESONATOR SPECTROSCOPY VERSUS READOUT AMPLITUDE
This sequence involves measuring the resonator by sending a readout pulse and demodulating the signals to
extract the 'I' and 'Q' quadratures.
This is done across various readout intermediate frequencies and amplitudes.
Based on the results, one can determine if a qubit is coupled to the resonator by noting the resonator frequency
splitting. This information can then be used to adjust the readout amplitude, choosing a readout amplitude value
just before the observed frequency splitting.

Prerequisites:
    - Calibration of the time of flight, offsets, and gains (referenced as "time_of_flight").
    - Calibration of the IQ mixer connected to the readout line (be it an external mixer or an Octave port).
    - Identification of the resonator's resonance frequency (referred to as "resonator_spectroscopy_multiplexed").
    - Configuration of the readout pulse amplitude (the pulse processor will sweep up to twice this value) and duration.
    - Specification of the expected resonator depletion time in the configuration.

Before proceeding to the next node:
    - Update the readout frequency, labeled as "resonator_IF_q", in the configuration.
    - Adjust the readout amplitude, labeled as "readout_amp_q", in the configuration.
"""

from qm.qua import *
from qm import QuantumMachinesManager, SimulationConfig
from configuration_mw_fem import *
from qualang_tools.results import progress_counter, fetching_tool
from qualang_tools.plot import interrupt_on_close
from qualang_tools.loops import from_array
from macros import qua_declaration, multiplexed_readout
import matplotlib.pyplot as plt
import math
from qualang_tools.results.data_handler import DataHandler
from scipy import signal
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use('TkAgg')

##################
#   Parameters   #
##################
# Choose parameters of target rr/qb

# Parameters Definition
n_avg = 100  # The number of averages
# The frequency sweep around the resonators' frequency
span = 600 * u.MHz  # the span around the resonant frequencies
step = 2 * u.MHz
dfs = np.arange(-span, span, step)
# The readout amplitude sweep (as a pre-factor of the readout amplitude) - must be within [-2; 2)
a_min = 0.01
a_max = 1.00
# da = 0.003
amplitudes = np.geomspace(a_min, a_max, 20)  # The amplitude vector +da/2 to add a_max to the scan

# Data to save
save_data_dict = {
    "n_avg": n_avg,
    "dfs": dfs,
    "amplitudes": amplitudes,
    "config": config,
    resonator: ["rr1","rr2","rr3","rr4","rr5","rr6"],
}

###################
# The QUA program #
###################
with program() as PROGRAM:
    # QUA macro to declare the measurement variables and their corresponding streams for a given number of resonators
    I, I_st, Q, Q_st, n, n_st = qua_declaration(nb_of_qubits=6)
    df = declare(int)  # QUA variable for sweeping the readout frequency detuning around the resonance
    a = declare(fixed)  # QUA variable for sweeping the readout amplitude pre-factor

    with for_(n, 0, n < n_avg, n + 1):  # QUA for_ loop for averaging
        with for_(*from_array(df, dfs)):  # QUA for_ loop for sweeping the frequency
            # Update the frequency of the two resonator elements
            update_frequency("rr1", df + resonator_IF_q1)
            update_frequency("rr2", df + resonator_IF_q2)
            update_frequency("rr3", df + resonator_IF_q3)
            update_frequency("rr4", df + resonator_IF_q4)
            update_frequency("rr5", df + resonator_IF_q5)
            update_frequency("rr6", df + resonator_IF_q6)

            with for_each_(a, amplitudes):  # QUA for_ loop for sweeping the readout amplitude
                multiplexed_readout(I, I_st, Q, Q_st, resonators=[1,2,3,4,5,6], amplitude=a, weights="rotated_")
        # Save the averaging iteration to get the progress bar
        save(n, n_st)

    with stream_processing():
        n_st.save("n")
        # Cast the data into a 2D matrix, average the 2D matrices together and store the results on the OPX processor
        # Note that the buffering goes from the most inner loop (left) to the most outer one (right)
        # resonator 1
        for ind in range(6):
            I_st[ind].buffer(len(amplitudes)).buffer(len(dfs)).average().save(f"I{ind+1}")
            Q_st[ind].buffer(len(amplitudes)).buffer(len(dfs)).average().save(f"Q{ind+1}")


#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(host=qop_ip, port=qop_port, cluster_name=cluster_name, octave=octave_config)

#######################
# Simulate or execute #
#######################
simulate = True

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=1_000)  # In clock cycles = 4ns
    # Simulate blocks python until the simulation is done
    job = qmm.simulate(config, PROGRAM, simulation_config)
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
    try:
        # Open a quantum machine to execute the QUA program
        qm = qmm.open_qm(config)
        # Send the QUA program to the OPX, which compiles and executes it
        job = qm.execute(PROGRAM)
        # Prepare the figure for live plotting
        fig = plt.figure()
        interrupt_on_close(fig, job)
        # Tool to easily fetch results from the OPX (results_handle used in it)
        results = fetching_tool(job, ["n", "I1", "Q1", "I2", "Q2", "I3", "Q3","I4", "Q4", "I5", "Q5","I6", "Q6"], mode="live")
        # Live plotting
        while results.is_processing():
            # Fetch results
            n, I1, Q1, I2, Q2, I3, Q3, I4, Q4, I5, Q5, I6, Q6, = results.fetch_all()
            # Progress bar
            progress_counter(n, n_avg, start_time=results.start_time)
            # Data analysis
            S1 = u.demod2volts(I1 + 1j * Q1, readout_len)
            S2 = u.demod2volts(I2 + 1j * Q2, readout_len)
            S3 = u.demod2volts(I1 + 1j * Q1, readout_len)
            S4 = u.demod2volts(I2 + 1j * Q2, readout_len)
            S5 = u.demod2volts(I1 + 1j * Q1, readout_len)
            S6 = u.demod2volts(I2 + 1j * Q2, readout_len)

            R1 = np.abs(S1)
            phase1 = np.angle(S1)
            R2 = np.abs(S2)
            phase2 = np.angle(S2)
            R3 = np.abs(S3)
            phase3 = np.angle(S3)
            R4 = np.abs(S4)
            phase4 = np.angle(S4)
            R5 = np.abs(S5)
            phase5 = np.angle(S5)
            R6 = np.abs(S6)
            phase6 = np.angle(S6)
            
            # Normalize data
            row_sums = R1.sum(axis=0)
            R1 /= row_sums[np.newaxis, :]
            row_sums = R2.sum(axis=0)
            R2 /= row_sums[np.newaxis, :]
            row_sums = R3.sum(axis=0)
            R3 /= row_sums[np.newaxis, :]
            row_sums = R4.sum(axis=0)
            R4 /= row_sums[np.newaxis, :]
            row_sums = R5.sum(axis=0)
            R5 /= row_sums[np.newaxis, :]
            row_sums = R6.sum(axis=0)
            R6 /= row_sums[np.newaxis, :]

        plt.suptitle("Resonator spectroscopy")

        side = 2.8  
        plt.gcf().set_size_inches(6*side, 2*side, forward=True)

        # --- Row 1 ---
        plt.subplot(2, 6, 1)  # R1 (magnitude)
        plt.cla()
        plt.title(f"Resonator 1 - LO: {resonator_LO/u.GHz} GHz")
        plt.ylabel("Readout IF [MHz]")
        plt.pcolor(amplitudes*readout_amp_q1, (dfs+resonator_IF_q1)/u.MHz, R1)
        plt.xscale("log")
        plt.xlim(amplitudes[0]*readout_amp_q1, amplitudes[-1]*readout_amp_q1)
        plt.gca().set_box_aspect(1) 

        plt.subplot(2, 6, 7)  # phase1
        plt.cla()
        plt.title("Phase 1")
        plt.pcolor(amplitudes*readout_amp_q1, (dfs+resonator_IF_q1)/u.MHz, signal.detrend(np.unwrap(phase1)))
        plt.xscale("log")
        plt.xlim(amplitudes[0]*readout_amp_q1, amplitudes[-1]*readout_amp_q1)
        plt.gca().set_box_aspect(1)

        # --- Row 2 ---
        plt.subplot(2, 6, 2)  # R2
        plt.cla()
        plt.title(f"Resonator 2 - LO: {resonator_LO/u.GHz} GHz")
        plt.ylabel("Readout IF [MHz]")
        plt.pcolor(amplitudes*readout_amp_q2, (dfs+resonator_IF_q2)/u.MHz, R2)
        plt.xscale("log")
        plt.xlim(amplitudes[0]*readout_amp_q2, amplitudes[-1]*readout_amp_q2)
        plt.gca().set_box_aspect(1)

        plt.subplot(2, 6, 8)  # phase2
        plt.cla()
        plt.title("Phase 2")
        plt.pcolor(amplitudes*readout_amp_q2, (dfs+resonator_IF_q2)/u.MHz, signal.detrend(np.unwrap(phase2)))
        plt.xscale("log")
        plt.xlim(amplitudes[0]*readout_amp_q2, amplitudes[-1]*readout_amp_q2)
        plt.gca().set_box_aspect(1)

        # --- Row 3 ---
        plt.subplot(2, 6, 3)  # R3
        plt.cla()
        plt.title(f"Resonator 3 - LO: {resonator_LO/u.GHz} GHz")
        plt.ylabel("Readout IF [MHz]")
        plt.pcolor(amplitudes*readout_amp_q3, (dfs+resonator_IF_q3)/u.MHz, R3)
        plt.xscale("log")
        plt.xlim(amplitudes[0]*readout_amp_q3, amplitudes[-1]*readout_amp_q3)
        plt.gca().set_box_aspect(1)

        plt.subplot(2, 6, 9)  # phase3
        plt.cla()
        plt.title("Phase 3")
        plt.pcolor(amplitudes*readout_amp_q3, (dfs+resonator_IF_q3)/u.MHz, signal.detrend(np.unwrap(phase3)))
        plt.xscale("log")
        plt.xlim(amplitudes[0]*readout_amp_q3, amplitudes[-1]*readout_amp_q3)
        plt.gca().set_box_aspect(1)

        # --- Row 4 ---
        plt.subplot(2, 6, 4)  # R4
        plt.cla()
        plt.title(f"Resonator 4 - LO: {resonator_LO/u.GHz} GHz")
        plt.ylabel("Readout IF [MHz]")
        plt.pcolor(amplitudes*readout_amp_q4, (dfs+resonator_IF_q4)/u.MHz, R4)
        plt.xscale("log")
        plt.xlim(amplitudes[0]*readout_amp_q4, amplitudes[-1]*readout_amp_q4)
        plt.gca().set_box_aspect(1)

        plt.subplot(2, 6, 10)  # phase4
        plt.cla()
        plt.title("Phase 4")
        plt.pcolor(amplitudes*readout_amp_q4, (dfs+resonator_IF_q4)/u.MHz, signal.detrend(np.unwrap(phase4)))
        plt.xscale("log")
        plt.xlim(amplitudes[0]*readout_amp_q4, amplitudes[-1]*readout_amp_q4)
        plt.gca().set_box_aspect(1)

        # --- Row 5 ---
        plt.subplot(2, 6, 5)  # R5
        plt.cla()
        plt.title(f"Resonator 5 - LO: {resonator_LO/u.GHz} GHz")
        plt.ylabel("Readout IF [MHz]")
        plt.pcolor(amplitudes*readout_amp_q5, (dfs+resonator_IF_q5)/u.MHz, R5)
        plt.xscale("log")
        plt.xlim(amplitudes[0]*readout_amp_q5, amplitudes[-1]*readout_amp_q5)
        plt.gca().set_box_aspect(1)

        plt.subplot(2, 6, 11)  # phase5
        plt.cla()
        plt.title("Phase 5")
        plt.pcolor(amplitudes*readout_amp_q5, (dfs+resonator_IF_q5)/u.MHz, signal.detrend(np.unwrap(phase5)))
        plt.xscale("log")
        plt.xlim(amplitudes[0]*readout_amp_q5, amplitudes[-1]*readout_amp_q5)
        plt.gca().set_box_aspect(1)

        # --- Row 6 ---
        plt.subplot(2, 6, 6)  # R6
        plt.cla()
        plt.title(f"Resonator 6 - LO: {resonator_LO/u.GHz} GHz")
        plt.ylabel("Readout IF [MHz]")
        plt.pcolor(amplitudes*readout_amp_q6, (dfs+resonator_IF_q6)/u.MHz, R6)
        plt.xscale("log")
        plt.xlim(amplitudes[0]*readout_amp_q6, amplitudes[-1]*readout_amp_q6)
        plt.gca().set_box_aspect(1)

        plt.subplot(2, 6, 12)  # phase6
        plt.cla()
        plt.title("Phase 6")
        plt.xlabel("Readout amplitude [V]")
        plt.pcolor(amplitudes*readout_amp_q6, (dfs+resonator_IF_q6)/u.MHz, signal.detrend(np.unwrap(phase6)))
        plt.xscale("log")
        plt.xlim(amplitudes[0]*readout_amp_q6, amplitudes[-1]*readout_amp_q6)
        plt.gca().set_box_aspect(1)

        plt.tight_layout(rect=[0, 0, 1, 0.96])  # 預留上邊給 suptitle
        plt.pause(0.1)

        # Save results
        script_name = Path(__file__).name
        data_handler = DataHandler(root_data_folder=save_dir)
        save_data_dict.update({"I1_data": I1})
        save_data_dict.update({"Q1_data": Q1})
        save_data_dict.update({"I2_data": I2})
        save_data_dict.update({"Q2_data": Q2})
        save_data_dict.update({"fig_live": fig})
        data_handler.additional_files = {script_name: script_name, **default_additional_files}
        data_handler.save_data(data=save_data_dict, name="_".join(script_name.split("_")[1:]).split(".")[0])

    except Exception as e:
        print(f"An exception occurred: {e}")

    finally:
        qm.close()
        print("Experiment QM is now closed")
        plt.show(block=True)

# %%
