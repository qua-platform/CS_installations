# %%
"""
       HAHN ECHO MEASUREMENT (T2)
The program consists in playing two Hahn echo sequences successively (first ending with x90 and then with -x90)
and measure the photon counts received by the SPCM across varying idle times.
The sequence is repeated without playing the mw pulses to measure the dark counts on the SPCM.

The data is then post-processed to determine the coherence time T2.

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
#matplotlib.use("TKAgg")
warnings.filterwarnings("ignore")


###################
# The QUA program #
###################

# The time vector for varying the idle time in clock cycles (4ns)
ts_cycle = np.arange(4, 500, 20)
ts_ns = 4 * ts_cycle # ns
n_pi_pulses = 100
n_avg = 1_000

# Main sequence macro
def play_cpmg(
    times, counts, counts_st,
    t: int, i, n_pi: int, p1: str = "x90", p2: str = "x90", mw_amp_ratio: float = 1
):
    play(p1 * amp(mw_amp_ratio), "NV")  # Pi/2 pulse to qubit
    
    with for_(i, 0, i < n_pi, i + 1):
        wait(t, "NV")  # Variable idle time
        play("y180" * amp(mw_amp_ratio), "NV")  # Pi pulse to qubit
    
    wait(t, "NV")  # variable delay in spin Echo
    play(p2 * amp(mw_amp_ratio), "NV")  # Pi/2 pulse to qubit
    
    align()  # Play the laser pulse after the Ramsey sequence
    # Measure and detect the photons on SPCM
    play("laser_ON", "AOM")
    measure("readout", "SPCM", None, time_tagging.analog(times, meas_len, counts))
    # save counts
    save(counts, counts_st)


with program() as hahn_echo:
    t = declare(int)  # variable to sweep over in time
    n = declare(int)  # number of iterations
    i = declare(int)  # number of  t-pi
    n_pi = declare(int) # number of pi pulses

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
    play("laser_ON", "AOM")
    wait(wait_for_initialization * u.ns, "AOM")

    # Hahn echo sequence
    with for_(n, 0, n < n_avg, n + 1):
        with for_(n_pi, 0, n_pi < n_pi_pulses, n_pi + 1):
            with for_each_(t, ts_cycle):
                # First Hahn echo sequence with x90 - idle time - x90
                play_cpmg(
                    times_on_g, counts_on_g, counts_on_g_st,
                    t=t, i=i, n_pi=n_pi,
                    p1="x90", p2="x90", mw_amp_ratio=1,
                )
                wait(wait_between_runs * u.ns, "AOM")

                align()
                # Second Hahn echo sequence with x90 - idle time - -x90
                play_cpmg(
                    times_on_e, counts_on_e, counts_on_e_st,
                    t=t, i=i, n_pi=n_pi,
                    p1="x90", p2="-x90", mw_amp_ratio=1,
                )
                wait(wait_between_runs * u.ns, "AOM")

                align()
                # Third Hahn echo sequence for measuring the dark counts
                play_cpmg(
                    times_off, counts_off, counts_off_st,
                    t=t, i=i, n_pi=n_pi,
                    p1="x90", p2="x90", mw_amp_ratio=0,
                )
                wait(wait_between_runs * u.ns, "AOM")

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
    job = qmm.simulate(config, hahn_echo, simulation_config)
    job.get_simulated_samples().con1.plot()
else:
    # Open the quantum machine
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it
    # execute QUA program
    job = qm.execute(hahn_echo)
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
        plt.plot(ts_ns, counts_on_g, label="x90_idle_x180_idle_x90")
        plt.plot(ts_ns, counts_on_e, label="x90_idle_x180_idle_-x90")
        plt.plot(ts_ns, counts_off, label="mw off")
        plt.xlabel("2 * idle time [ns]")
        plt.ylabel("SPCM Voltage [V]")
        plt.title("Hahn Echo")
        plt.legend()
        plt.pause(0.1)

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
