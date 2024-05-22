# %%
"""
       T1 MEASUREMENT
The program consists in measuring signals (in |0> and |1> successively) received by the PD across 
varying wait times either after initialization (start from |0>), or after a pi pulse (start from |1>).
The sequence is repeated without playing the mw pulses to measure the dark counts on the PD.

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
from configuration import *


###################
# The QUA program #
###################

# The wait time vector in clock cycles (4ns)
t_vec = np.arange(4, 250, 10)
n_avg = 1_000  # The number averaging iterations
start_from_one = False


# Main sequence macro
def play_T1(I, I_st, t: int, start_from_one: bool = True, measure_in_one: bool = True, mw_amp_ratio: float = 1):
    # TODO: change to use MW_SWitch if IQ mixer is not available yet
    play("x180" * amp(int(start_from_one) * mw_amp_ratio), "NV")
    wait(t, "NV")  # variable delay in spin Echo
    play("x180" * amp(int(measure_in_one) * mw_amp_ratio), "NV")  # Pi pulse to qubit to measure second state
    align()  # Play the laser pulse after the mw sequence
    # Measure and detect the dark counts on PD
    play("laser_ON", "AOM")
    # TODO: change from integration to time tagging
    measure("readout", "PD", None, integration.full("const", I, "out1"))
    save(I, I_st)  # save counts


with program() as T1:
    t = declare(int)  # variable to sweep over in time
    n = declare(int)  # number of iterations
    I_mw_on0 = declare(fixed)  # variable for PD reading
    I_mw_on1 = declare(fixed)  # variable for PD reading
    I_mw_off = declare(fixed)  # variable for PD reading
    
    n_st = declare_stream()  # stream for number of iterations
    I_mw_on0_st = declare_stream()  # stream for PD reading
    I_mw_on1_st = declare_stream()  # stream for PD reading
    I_mw_off_st = declare_stream()  # stream for PD reading


    # Spin initialization
    play("laser_ON", "AOM")
    wait(wait_for_initialization * u.ns, "AOM")

    # T1 sequence
    with for_(n, 0, n < n_avg, n + 1):
        with for_(*from_array(t, t_vec)):
            # Measure in |0>
            play_T1(
                I_mw_on0, I_mw_on0_st, t=t,
                start_from_one=start_from_one,
                measure_in_one=False,
                mw_amp_ratio=1,
            )
            wait(wait_between_runs * u.ns, "AOM")

            align()
            # Measure in |1>
            play_T1(
                I_mw_on1, I_mw_on1_st, t=t,
                start_from_one=start_from_one,
                measure_in_one=True,
                mw_amp_ratio=1,
            )
            wait(wait_between_runs * u.ns, "AOM")

            align()
            # Measure dark counts
            play_T1(
                I_mw_off, I_mw_off_st, t=t,
                start_from_one=start_from_one,
                measure_in_one=False,
                mw_amp_ratio=0,
            )
            wait(wait_between_runs * u.ns, "AOM")

        save(n, n_st)  # save number of iterations inside for_loop

    with stream_processing():
        # Cast the data into a 1D vector, average the 1D vectors together and store the results on the OPX processor
        I_mw_on0_st.buffer(len(t_vec)).average().save("I_mw_on0")
        I_mw_on1_st.buffer(len(t_vec)).average().save("I_mw_on1")
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
    simulation_config = SimulationConfig(duration=4_000)  # In clock cycles = 4ns
    job = qmm.simulate(config, T1, simulation_config)
    job.get_simulated_samples().con1.plot()
else:
    # Open the quantum machine
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(T1)
    # Get results from QUA program
    results = fetching_tool(job, data_list=["I_mw_on0", "I_mw_on1", "I_mw_off", "iterations"], mode="live")
    # Live plotting
    fig = plt.figure()
    interrupt_on_close(fig, job)  # Interrupts the job when closing the figure

    while results.is_processing():
        # Fetch results
        I_mw_on0, I_mw_on1, I_mw_off, iterations = results.fetch_all()
        I_mw_on0 = u.demod2volts(I_mw_on0, meas_len)
        I_mw_on1 = u.demod2volts(I_mw_on1, meas_len)
        I_mw_off = u.demod2volts(I_mw_off, meas_len)
        # Progress bar
        progress_counter(iterations, n_avg, start_time=results.get_start_time())
        # Plot data
        plt.cla()
        plt.plot(t_vec * 4, I_mw_on0, label="x90_idle_x180_idle_x90")
        plt.plot(t_vec * 4, I_mw_on1, label="x90_idle_x180_idle_-x90")
        plt.plot(t_vec * 4, I_mw_off, label="mw off")
        plt.xlabel("Wait time [ns]")
        plt.ylabel("PD Voltage [V]")
        plt.title(f"T1 - starting from  {'|1>' if start_from_one else '|0>'}")
        plt.legend()
        plt.pause(0.1)


    if save_data:
        # Arrange data to save
        data = {
            "fig_live": fig,
            "t_vec": t_vec,
            "I_mw_on0": I_mw_on0,
            "I_mw_on1": I_mw_on1,
            "I_mw_off": I_mw_off,
            "iterations": iterations,
            # "elapsed_time": np.array([elapsed_time]),  # convert float to np.array of float
        }
        # Initialize the DataHandler
        data_handler = DataHandler(root_data_folder=save_dir)
        data_handler.create_data_folder(name=Path(__file__).stem)
        data_handler.additional_files = {
            Path(__file__).name: Path(__file__).name,
            "configuration.py": "configuration.py",
        }
        # Save results
        data_folder = data_handler.save_data(data=data)

# %%
