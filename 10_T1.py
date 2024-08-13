# %%
"""
       T1 MEASUREMENT
The program consists in measuring signals (in |0> and |1> successively) received by the SPCM across 
varying wait times either after initialization (start from |0>), or after a pi pulse (start from |1>).
The sequence is repeated without playing the mw pulses to measure the dark counts on the SPCM.

The data is then post-processed to determine the thermal relaxation time T1.

Prerequisites:
    - Ensure calibration of the different delays in the system (calibrate_delays).
    - Having updated the different delays in the configuration.
    - Having updated the NV frequency, labeled as "NV_IF_freq", in the configuration.
    - Having set the pi pulse amplitude and duration in the configuration

Next steps before going to the next node:
    -
"""

from qm.QuantumMachinesManager import QuantumMachinesManager
from qm.qua import *
from qm import SimulationConfig
from qualang_tools.results import progress_counter, fetching_tool
from qualang_tools.plot import interrupt_on_close
from qualang_tools.loops import from_array
from qualang_tools.results.data_handler import DataHandler
import matplotlib.pyplot as plt
from configuration_with_octave import *
import matplotlib
import warnings
matplotlib.use("TKAgg")
warnings.filterwarnings("ignore")


###################
# The QUA program #
###################

# The wait time vector in clock cycles (4ns)
ts_cycle = np.arange(4, 250, 10)
ts_ns = 4 * ts_cycle # ns
n_avg = 1_000  # The number averaging iterations
start_from_e = True


# Main sequence macro
def play_T1(
    times, counts, counts_st,
    t: int, start_from_e: bool = True, pi_after_delay: bool = True, mw_amp_ratio: float = 1,
):
    play("x180" * amp(int(start_from_e) * mw_amp_ratio), "NV")
    wait(t, "NV")  # variable delay in spin Echo
    play("x180" * amp(int(pi_after_delay) * mw_amp_ratio), "NV")

    align()
    # Measure and detect the photons on SPCM
    play("laser_ON", "AOM1")
    measure("readout", "SPCM", None, time_tagging.analog(times, meas_len, counts))
    # save counts
    save(counts, counts_st)


with program() as T1:
    t = declare(int)  # variable to sweep over in time
    n = declare(int)  # number of iterations
    times_on_g = declare(int, size=100)  # QUA vector for storing the time-tags
    times_on_e = declare(int, size=100)  # QUA vector for storing the time-tags
    times_off = declare(int, size=100)  # QUA vector for storing the time-tags
    counts_on_g = declare(int)  # saves number of photon counts
    counts_on_e = declare(int)  # saves number of photon counts
    counts_off = declare(int)  # saves number of photon counts
    
    n_st = declare_stream()  # stream for number of iterations
    counts_on_g_st = declare_stream()  # stream for counts
    counts_on_e_st = declare_stream()  # stream for counts
    counts_off_st = declare_stream()  # stream for counts

    # Spin initialization
    play("laser_ON", "AOM1")
    wait(wait_for_initialization * u.ns, "AOM1")

    # T1 sequence
    with for_(n, 0, n < n_avg, n + 1):
        with for_(*from_array(t, ts_cycle)):
            # Measure in |0> for Start in |1>
            play_T1(
                times_on_g, counts_on_g, counts_on_g_st,
                t=t,
                start_from_e=start_from_e,
                pi_after_delay=False,
                mw_amp_ratio=1,
            )
            wait(wait_between_runs * u.ns, "AOM1")

            align()
            # Measure in |1> for Start in |0>
            play_T1(
                times_on_e, counts_on_e, counts_on_e_st,
                t=t,
                start_from_e=start_from_e,
                pi_after_delay=True,
                mw_amp_ratio=1,
            )
            wait(wait_between_runs * u.ns, "AOM1")

            align()
            # Measure dark counts
            play_T1(
                times_off, counts_off, counts_off_st,
                t=t,
                start_from_e=start_from_e,
                pi_after_delay=False,
                mw_amp_ratio=0,
            )
            wait(wait_between_runs * u.ns, "AOM1")

        save(n, n_st)  # save number of iterations inside for_loop

    with stream_processing():
        # Cast the data into a 1D vector, average the 1D vectors together and store the results on the OPX processor
        counts_on_g_st.buffer(len(ts_cycle)).average().save("counts_on_g")
        counts_on_e_st.buffer(len(ts_cycle)).average().save("counts_on_e")
        counts_off_st.buffer(len(ts_cycle)).average().save("counts_off")
        n_st.save("iterations")

#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(host=qop_ip, port=None, cluster_name=cluster_name, octave=octave_config)

#######################
# Simulate or execute #
#######################
simulate = False
save_data = True

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=4_000)  # In clock cycles = 4ns
    job = qmm.simulate(config, T1, simulation_config)
    job.get_simulated_samples().con_e.plot()
else:
    # Open the quantum machine
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(T1)
    # Get results from QUA program
    results = fetching_tool(job, data_list=["counts_on_g", "counts_on_e", "counts_off", "iterations"], mode="live")
    # Live plotting
    fig = plt.figure()
    interrupt_on_close(fig, job)  # Interrupts the job when closing the figure

    while results.is_processing():
        # Fetch results
        counts_on_g, counts_on_e, counts_off, iterations = results.fetch_all()
        # Progress bar
        progress_counter(iterations, n_avg, start_time=results.get_start_time())
        # Plot data
        plt.cla()
        plt.plot(ts_ns, counts_on_g, label="mw off (pi_after_delay=False)")
        plt.plot(ts_ns, counts_on_e, label="mw off (pi_after_delay=True)")
        plt.plot(ts_ns, counts_off, label="mw off")
        plt.xlabel("Wait time [ns]")
        plt.ylabel("SPCM Voltage [V]")
        plt.title(f"T1 - starting from  {'|1>' if start_from_e else '|0>'}")
        plt.legend()
        plt.pause(0.1)

    # Fit the results to extract the qubit decay time T1
    try:
        from qualang_tools.plot.fitting import Fit

        fit = Fit()
        plt.figure()
        plt.suptitle("T1 measurement")

        plt.subplot(121)
        decay_fit = fit.T1(4 * ts_ns, counts_on_g, plot=True)
        qubit_T1 = np.round(np.abs(decay_fit["T1"][0]) / 4) * 4
        plt.xlabel("Delay [ns]")
        plt.ylabel("I quadrature [V]")
        print(f"qubit_T1 = {qubit_T1:.0f} ns")
        plt.legend((f"depletion time = {qubit_T1:.0f} ns",))
        plt.title("Qubit 1")

        plt.subplot(122)
        decay_fit = fit.T1(4 * ts_ns, counts_on_e, plot=True)
        qubit_T1 = np.round(np.abs(decay_fit["T1"][0]) / 4) * 4
        plt.xlabel("Delay [ns]")
        plt.ylabel("I quadrature [V]")
        print(f"qubit_T1 = {qubit_T1:.0f} ns")
        plt.legend((f"depletion time = {qubit_T1:.0f} ns",))
        plt.title("Qubit 2")

        plt.tight_layout()

    except (Exception,):
        pass

    if save_data:
        # Arrange data to save
        data = {
            "fig_live": fig,
            "ts_cycle": ts_cycle,
            "ts_ns": ts_ns,
            "counts_on_g": counts_on_g,
            "counts_on_e": counts_on_e,
            "counts_off": counts_off,
            "iterations": np.array(iterations),
            # "elapsed_time": np.array([elapsed_time]),  # convert float to np.array of float
        }
        # Initialize the DataHandler
        data_handler = DataHandler(root_data_folder=save_dir)
        data_handler.create_data_folder(name=Path(__file__).stem)
        data_handler.additional_files = {
            Path(__file__).name: Path(__file__).name,
            "configuration_with_octave.py": "configuration_with_octave.py",
        }
        # Save results
        data_folder = data_handler.save_data(data=data)

# %%
