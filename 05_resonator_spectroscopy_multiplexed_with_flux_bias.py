# %%
"""
        RESONATOR SPECTROSCOPY MULTIPLEXED
This sequence involves measuring the resonator by sending a readout pulse and demodulating the signals to extract the
'I' and 'Q' quadratures across varying readout intermediate frequencies for the two resonators simultaneously.
The data is then post-processed to determine the resonators' resonance frequency.
This frequency can be used to update the readout intermediate frequency in the configuration.

Prerequisites:
    - Ensure calibration of the time of flight, offsets, and gains (referenced as "time_of_flight").
    - Calibrate the IQ mixer connected to the readout line (whether it's an external mixer or an Octave port).
    - Having found each resonator resonant frequency and updated the configuration (resonator_spectroscopy).
    - Specify the expected resonator depletion time in the configuration.

Before proceeding to the next node:
    - Update the readout frequency, labeled as "resonator_IF_q1" and "resonator_IF_q2", in the configuration.
"""

from qm.qua import *
from qm import QuantumMachinesManager
from qm import SimulationConfig
from configuration import *
from qualang_tools.results.data_handler import DataHandler
from qualang_tools.results import progress_counter, fetching_tool
from qualang_tools.plot import interrupt_on_close
from qualang_tools.loops import from_array
import matplotlib.pyplot as plt
from scipy import signal

# import warnings
# import matplotlib

# matplotlib.use("TKAgg")
# warnings.filterwarnings("ignore")


###################
# The QUA program #
###################
n_avg = 100  # The number of averages
# The frequency sweep parameters (for both resonators)
span = 10 * u.MHz  # the span around the resonant frequencies
step = 100 * u.kHz
dfs = np.arange(-span, span, step)

resonators = ["rr1", "rr2", "rr3", "rr4", "rr5"]
resonators_IF = [resonator_IF_q1, resonator_IF_q2, resonator_IF_q3, resonator_IF_q4, resonator_IF_q5]

# should be set in the config
max_frequency_point1 = -0.4 # q3
max_frequency_point2 = -0.3 # q4
max_frequency_point3 = +0.4 # q5

with program() as multi_res_spec:
    n = declare(int)  # QUA variable for the averaging loop
    df = declare(int)  # QUA variable for the readout frequency detuning around the resonance
    n_st = declare_stream()  # Stream for the averaging iteration 'n'
    # Here we define one 'I', 'Q', 'I_st' & 'Q_st' for each resonator via a python list
    I = [declare(fixed) for _ in range(len(resonators))]
    Q = [declare(fixed) for _ in range(len(resonators))]
    I_st = [declare_stream() for _ in range(len(resonators))]
    Q_st = [declare_stream() for _ in range(len(resonators))]

    set_dc_offset("q3_z_dc", "single", max_frequency_point1) 
    set_dc_offset("q4_z_dc", "single", max_frequency_point2) 
    set_dc_offset("q5_z_dc", "single", max_frequency_point3)
    with for_(n, 0, n < n_avg, n + 1):  # QUA for_ loop for averaging
        with for_(*from_array(df, dfs)):  # QUA for_ loop for sweeping the frequency
            # wait for the resonators to deplete
            wait(10 * depletion_time * u.ns, *resonators)

            for i, (rr, resonator_IF) in enumerate(zip(resonators, resonators_IF)):
                update_frequency(rr, df + resonator_IF)  # Update the frequency the rr element
                # Measure the resonator (send a readout pulse and demodulate the signals to get the 'I' & 'Q' quadratures)
                measure(
                    "readout",
                    rr,
                    None,
                    demod.full("cos", I[i], "out1"),
                    demod.full("sin", Q[i], "out1"),
                )
                # Save the 'I' & 'Q' quadratures for rr1 to their respective streams
                save(I[i], I_st[i])
                save(Q[i], Q_st[i])

        # Save the averaging iteration to get the progress bar
        save(n, n_st)

    with stream_processing():
        n_st.save("iteration")
        for i, rr in enumerate(resonators):
            I_st[i].buffer(len(dfs)).average().save(f"I{i+1}")
            Q_st[i].buffer(len(dfs)).average().save(f"Q{i+1}")


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
    job = qmm.simulate(config, multi_res_spec, simulation_config)
    job.get_simulated_samples().con1.plot()

else:
    # Open a quantum machine to execute the QUA program
    qm = qmm.open_qm(config)
    # Execute the QUA program
    job = qm.execute(multi_res_spec)
    # Tool to easily fetch results from the OPX (results_handle used in it)
    results = fetching_tool(job, ["I1", "Q1", "I2", "Q2", "I3", "Q3", "I4", "Q4", "I5", "Q5", "iteration"], mode="live")
    # Live plotting
    fig, axss = plt.subplots(2, 5, figsize=(20, 7))
    interrupt_on_close(fig, job)  # Interrupts the job when closing the figure
    while results.is_processing():
        # Fetch results
        I1, Q1, I2, Q2, I3, Q3, I4, Q4, I5, Q5, iteration = results.fetch_all()
        # Progress bar
        progress_counter(iteration, n_avg, start_time=results.get_start_time())
        # Data analysis
        S1 = u.demod2volts(I1 + 1j * Q1, readout_len)
        S2 = u.demod2volts(I2 + 1j * Q2, readout_len)
        S3 = u.demod2volts(I3 + 1j * Q3, readout_len)
        S4 = u.demod2volts(I4 + 1j * Q4, readout_len)
        S5 = u.demod2volts(I5 + 1j * Q5, readout_len)
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
        # Plot
        plt.suptitle("Multiplexed resonator spectroscopy")
        axss[0, 0].plot((resonator_IF_q1 + dfs) / u.MHz, R1)
        plt.title(f"Resonator 1 - LO: {resonator_LO / u.GHz} GHz")
        plt.ylabel(r"R=$\sqrt{I^2 + Q^2}$ [V]")
        axss[0, 1].plot((resonator_IF_q2 + dfs) / u.MHz, R2)
        plt.title(f"Resonator 2 - LO: {resonator_LO / u.GHz} GHz")
        axss[0, 2].plot((resonator_IF_q3 + dfs) / u.MHz, R3)
        plt.title(f"Resonator 3 - LO: {resonator_LO / u.GHz} GHz")
        axss[0, 3].plot((resonator_IF_q4 + dfs) / u.MHz, R4)
        plt.title(f"Resonator 4 - LO: {resonator_LO / u.GHz} GHz")
        axss[0, 4].plot((resonator_IF_q5 + dfs) / u.MHz, R5)
        plt.title(f"Resonator 5 - LO: {resonator_LO / u.GHz} GHz")
        axss[1, 0].plot((resonator_IF_q1 + dfs) / u.MHz, signal.detrend(np.unwrap(phase1)))
        plt.xlabel("Readout IF [MHz]")
        plt.ylabel("Phase [rad]")
        axss[1, 1].plot((resonator_IF_q2 + dfs) / u.MHz, signal.detrend(np.unwrap(phase2)))
        plt.xlabel("Readout IF [MHz]")
        axss[1, 2].plot((resonator_IF_q3 + dfs) / u.MHz, signal.detrend(np.unwrap(phase3)))
        plt.xlabel("Readout IF [MHz]")
        plt.ylabel("Phase [rad]")
        axss[1, 3].plot((resonator_IF_q4 + dfs) / u.MHz, signal.detrend(np.unwrap(phase4)))
        plt.xlabel("Readout IF [MHz]")
        axss[1, 4].plot((resonator_IF_q5 + dfs) / u.MHz, signal.detrend(np.unwrap(phase5)))
        plt.xlabel("Readout IF [MHz]")
        plt.tight_layout()
        plt.pause(0.1)

    try:
        from qualang_tools.plot.fitting import Fit

        fit = Fit()
        plt.figure(figsize=(20, 6))
        plt.subplot(151)
        fit.reflection_resonator_spectroscopy((resonator_IF_q1 + dfs) / u.MHz, R1, plot=True)
        plt.xlabel("rr1 IF [MHz]")
        plt.ylabel("Amplitude [V]")
        plt.subplot(152)
        fit.reflection_resonator_spectroscopy((resonator_IF_q2 + dfs) / u.MHz, R2, plot=True)
        plt.xlabel("rr2 IF [MHz]")
        plt.title(f"Multiplexed resonator spectroscopy")
        plt.subplot(153)
        fit.reflection_resonator_spectroscopy((resonator_IF_q3 + dfs) / u.MHz, R3, plot=True)
        plt.xlabel("rr3 IF [MHz]")
        plt.title(f"Multiplexed resonator spectroscopy")
        plt.subplot(154)
        fit.reflection_resonator_spectroscopy((resonator_IF_q4 + dfs) / u.MHz, R4, plot=True)
        plt.xlabel("rr4 IF [MHz]")
        plt.title(f"Multiplexed resonator spectroscopy")
        plt.subplot(155)
        fit.reflection_resonator_spectroscopy((resonator_IF_q5 + dfs) / u.MHz, R5, plot=True)
        plt.xlabel("rr5 IF [MHz]")
        plt.title(f"Multiplexed resonator spectroscopy")
        plt.tight_layout()
    except (Exception,):
        pass
    # Close the quantum machines at the end in order to put all flux biases to 0 so that the fridge doesn't heat-up
    qm.close()

    # Save results
    save_data_dict = {"fig_live": fig, "frequencies": dfs,
        "I1": I1, "Q1": Q1, "I2": I2, "Q2": Q2,
        "I3": I3, "Q3": Q3, "I4": I4, "Q4": Q4, "I5": I5, "Q5": Q5,
    }
    script_name = Path(__file__).name
    data_handler = DataHandler(root_data_folder=save_dir)
    data_handler.additional_files = {script_name: script_name, **default_additional_files}
    data_handler.save_data(data=save_data_dict, name=Path(__file__).stem)

# %%
