# %%
"""
       RAMSEY MEASUREMENT (T2*)
The program consists in playing two Ramsey sequence successively (first ending with x90 and then with -x90)
and measure the photon counts received by the PD across varying idle times.
The sequence is repeated without playing the mw pulses to measure the dark counts on the PD.

The data is then post-processed to determine the dephasing time T2*.

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
from utils import save_files_and_get_dir_data
import matplotlib.pyplot as plt
from configuration import *


###################
# The QUA program #
###################

def play_ramsey(I, I_st, t: int, p1: str = "x90", p2: str = "x90", mw_amp_ratio: float = 1):
    play(p1 * amp(mw_amp_ratio), "NVs")  # Pi/2 pulse to qubit
    wait(t, "NVs")  # Variable idle time
    play(p2 * amp(mw_amp_ratio), "NVs")  # Pi/2 pulse to qubit
    align()  # Play the laser pulse after the Ramsey sequence
    # Measure and detect the photons on PD
    play("laser_ON", "AOM")
    measure("readout", "PD", None, integration.full("const", I, "out1"))
    save(I, I_st)  # save counts


# The time vector for varying the idle time in clock cycles (4ns)
t_vec = np.arange(4, 250, 10)
n_avg = 1_000  # The number of averaging iterations

with program() as ramsey:
    t = declare(int)  # variable to sweep over in time
    n = declare(int)  # number of iterations
    I_mw_on_p = declare(fixed)  # variable for PD reading
    I_mw_on_n = declare(fixed)  # variable for PD reading
    I_mw_off = declare(fixed)  # variable for PD reading
    
    n_st = declare_stream()  # stream for number of iterations
    I_mw_on_p_st = declare_stream()  # stream for PD reading
    I_mw_on_n_st = declare_stream()  # stream for PD reading
    I_mw_off_st = declare_stream()  # stream for PD reading

    # Spin initialization
    play("laser_ON", "AOM")
    wait(wait_for_initialization * u.ns, "AOM")

    # Ramsey sequence
    with for_(n, 0, n < n_avg, n + 1):
        with for_(*from_array(t, t_vec)):
            # First Ramsey sequence with x90 - idle time - x90
            play_ramsey(I_mw_on_p, I_mw_on_p_st, t=t, p1="x90", p2="x90", mw_amp_ratio=1)
            wait(wait_between_runs * u.ns, "AOM")

            align()
            # Second Ramsey sequence with x90 - idle time - -x90
            play_ramsey(I_mw_on_n, I_mw_on_n_st, t=t, p1="x90", p2="-x90", mw_amp_ratio=1)
            wait(wait_between_runs * u.ns, "AOM")

            align()
            # Third Ramsey sequence for measuring the dark counts
            play_ramsey(I_mw_off, I_mw_off_st, t=t, p1="x90", p2="x90", mw_amp_ratio=0)
            wait(wait_between_runs * u.ns, "AOM")

        save(n, n_st)  # save number of iterations inside for_loop

    with stream_processing():
        # Cast the data into a 1D vector, average the 1D vectors together and store the results on the OPX processor
        I_mw_on_p_st.buffer(len(t_vec)).average().save("I_mw_on_p")
        I_mw_on_n_st.buffer(len(t_vec)).average().save("I_mw_on_n")
        I_mw_off_st.buffer(len(t_vec)).average().save("I_mw_off")
        n_st.save("iterations")

#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(host=qop_ip, cluster_name=cluster_name)

#######################
# Simulate or execute #
#######################
simulate = False
save_data = True

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=10_000)  # In clock cycles = 4ns
    job = qmm.simulate(config, ramsey, simulation_config)
    job.get_simulated_samples().con1.plot()
else:
    # Open the quantum machine
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(ramsey)
    # Get results from QUA program
    results = fetching_tool(job, data_list=["I_mw_on_p", "I_mw_on_n", "I_mw_off", "iterations"], mode="live")
    # Live plotting
    fig = plt.figure()
    interrupt_on_close(fig, job)  # Interrupts the job when closing the figure

    while results.is_processing():
        # Fetch results
        I_mw_on_p, I_mw_on_n, I_mw_off, iterations = results.fetch_all()
        I_mw_on_p = u.demod2volts(I_mw_on_p, meas_len)
        I_mw_on_n = u.demod2volts(I_mw_on_n, meas_len)
        I_mw_off = u.demod2volts(I_mw_off, meas_len)
        # Progress bar
        progress_counter(iterations, n_avg, start_time=results.get_start_time())
        # Plot data
        plt.cla()
        plt.plot(t_vec * 4, I_mw_on_p, label="x90_idle_x90")
        plt.plot(t_vec * 4, I_mw_on_n, label="x90_idle_-x90")
        plt.plot(t_vec * 4, I_mw_off, label="mw off")
        plt.xlabel("Ramsey idle time [ns]")
        plt.ylabel("PD Voltage [V]")
        plt.title("Ramsey")
        plt.legend()
        plt.pause(0.1)

    if save_data:
        dir_data = save_files_and_get_dir_data(
            base_dir=base_dir,
            save_dir=save_dir,
            script_path=__file__,
        )
        np.savez(
            file=dir_data / "data.npz",
            t_vec=t_vec,
            I_mw_on_p=I_mw_on_p,
            I_mw_on_n=I_mw_on_n,
            I_mw_off=I_mw_off,
            iterations=iterations,
        )
        # If a matplotlib figure object is available.
        fig.savefig(dir_data / "data_live.png")

# %%
