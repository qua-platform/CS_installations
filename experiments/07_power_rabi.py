# %%
"""
        POWER RABI
The program consists in playing a mw pulse and measure the photon counts received by the PD
across varying mw pulse amplitudes.
The sequence is repeated without playing the mw pulses to measure the dark counts on the PD.

The data is then post-processed to determine the pi pulse amplitude for the specified duration.

Prerequisites:
    - Ensure calibration of the different delays in the system (calibrate_delays).
    - Having updated the different delays in the configuration.
    - Having updated the NV frequency, labeled as "NV_IF_freq", in the configuration.
    - Set the desired pi pulse duration, labeled as "mw_len_NV", in the configuration

Next steps before going to the next node:
    - Update the pi pulse amplitude, labeled as "mw_amp_NV", in the configuration.
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

a_vec = np.arange(0.1, 1, 0.02)  # The amplitude pre-factor vector
n_avg = 1_000  # number of iterations


# Main sequence macro
def play_power_rabi(I, I_st, mw_amp_ratio: float = 1):
    # Play the Rabi pulse with varying durations
    play("x180" * amp(mw_amp_ratio), "NV")
    align()  # Play the laser pulse after the mw pulse
    play("laser_ON", "AOM")
    # Measure and detect the photons on PD
    # TODO: change from integration to time tagging
    measure("readout", "PD", None, integration.full("const", I, "out1"))
    save(I, I_st)  # save counts


with program() as power_rabi:
    a = declare(fixed)  # variable to sweep over the amplitude
    n = declare(int)  # number of iterations
    I_mw_on = declare(fixed)  # variable for PD reading
    I_mw_off = declare(fixed)  # variable for PD reading
    
    n_st = declare_stream()  # stream for number of iterations
    I_mw_on_st = declare_stream()  # stream for PD reading
    I_mw_off_st = declare_stream()  # stream for PD reading

    # Spin initialization
    play("laser_ON", "AOM")
    wait(wait_for_initialization * u.ns, "AOM")

    # Power Rabi sweep
    with for_(n, 0, n < n_avg, n + 1):
        with for_(*from_array(a, a_vec)):
            # Play the Rabi pulse with varying amplitude
            play_power_rabi(I_mw_on, I_mw_on_st, mw_amp_ratio=a)

            # Wait and align all elements before measuring the dark events
            wait(wait_between_runs * u.ns)

            align()
            # Play the Rabi pulse with zero amplitude
            play_power_rabi(I_mw_off, I_mw_off_st, mw_amp_ratio=0)

            # Wait and align all elements before measuring the next iterations 
            wait(wait_between_runs * u.ns)  # wait in between iterations

        save(n, n_st)  # save number of iterations inside for_loop

    with stream_processing():
        # Cast the data into a 1D vector, average the 1D vectors together and store the results on the OPX processor
        I_mw_on_st.buffer(len(a_vec)).average().save("I_mw_on")
        I_mw_off_st.buffer(len(a_vec)).average().save("I_mw_off")
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
    job = qmm.simulate(config, power_rabi, simulation_config)
    job.get_simulated_samples().con1.plot()
else:
    # Open the quantum machine
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(power_rabi)
    # Get results from QUA program
    results = fetching_tool(job, data_list=["I_mw_on", "I_mw_off", "iterations"], mode="live")
    # Live plotting
    fig = plt.figure()
    interrupt_on_close(fig, job)  # Interrupts the job when closing the figure

    while results.is_processing():
        # Fetch results
        I_mw_on, I_mw_off, iterations = results.fetch_all()
        I_mw_on, I_mw_off = u.demod2volts(I_mw_on, meas_len), u.demod2volts(I_mw_off, meas_len)
        # Progress bar
        progress_counter(iterations, n_avg, start_time=results.get_start_time())
        # Plot data
        plt.cla()
        plt.plot(a_vec * pi_amp_NV, I_mw_on, label="mw on")
        plt.plot(a_vec * pi_amp_NV, I_mw_off, label="mw off")
        plt.xlabel("Rabi pulse amplitude [V]")
        plt.ylabel("PD Voltage [V]")
        plt.title("Power Rabi")
        plt.legend()
        plt.pause(0.1)

    if save_data:
        # Arrange data to save
        data = {
            "fig_live": fig,
            "a_vec": a_vec,
            "I_mw_on": I_mw_on,
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
