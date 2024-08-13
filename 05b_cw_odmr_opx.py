# %%
"""
        CW Optically Detected Magnetic Resonance (ODMR)
The program consists in playing a mw pulse and the readout laser pulse simultaneously to extract
the photon counts received by the SPCM across varying intermediate frequencies.
The sequence is repeated without playing the mw pulses to measure the dark counts on the SPCM.

The data is then post-processed to determine the spin resonance frequency.
This frequency can be used to update the NV intermediate frequency in the configuration under "NV_IF_freq".

Prerequisites:
    - Ensure calibration of the different delays in the system (calibrate_delays).
    - Update the different delays in the configuration

Next steps before going to the next node:
    - Update the NV frequency, labeled as "NV_IF_freq", in the configuration.
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

# Frequency vector
f_vec = np.arange(-30 * u.MHz, 70 * u.MHz, 2 * u.MHz)
n_avg = 1_000  # number of averages
readout_len = long_meas_len  # Readout duration for this experiment


# Main sequence macro
def play_laser_mw_and_measure_pd(times, counts, mw_amp_ratio: float = 1):
    # play laser and mw
    play("cw" * amp(mw_amp_ratio), "NV", duration=readout_len * u.ns)
    # ... and the laser pulse simultaneously (the laser pulse is delayed by 'laser_delay_1')
    play("laser_ON", "AOM1", duration=readout_len * u.ns)
    # so readout don't catch the first part of spin reinitialization
    wait(1_000 * u.ns, "SPCM")
    # Measure and detect the photons on SPCM
    measure("readout", "SPCM", None, time_tagging.analog(times, meas_len, counts))
    # data to stream processor
    return counts


with program() as cw_odmr:
    f = declare(int)  # frequencies
    n = declare(int)  # number of iterations
    I_mw_on = declare(fixed)  # variable for SPCM reading
    I_mw_off = declare(fixed)  # variable for SPCM reading
    
    n_st = declare_stream()  # stream for number of iterations
    I_mw_on_st = declare_stream()  # stream for SPCM reading
    I_mw_off_st = declare_stream()  # stream for SPCM reading
    
    with for_(n, 0, n < n_avg, n + 1):
        with for_(*from_array(f, f_vec)):
            # Update the frequency of the digital oscillator linked to the element "NV"
            update_frequency("NV", f)

            # align all elements 
            align()
            # play laser and mw
            play_laser_mw_and_measure_pd(I_mw_on, I_mw_on_st, mw_amp_ratio=1)

            # Wait and align all elements before measuring the dark events
            wait(wait_between_runs * u.ns)
            
            # align all elements 
            align()
            # play laser an no mw
            play_laser_mw_and_measure_pd(I_mw_off, I_mw_off_st, mw_amp_ratio=0)
            
            # Wait and align all elements before measuring the next iterations
            wait(wait_between_runs * u.ns)

        # save number of iterations inside for_loop
        save(n, n_st)

    with stream_processing():
        # Cast the data into a 1D vector, average the 1D vectors together and store the results on the OPX processor
        I_mw_on_st.buffer(len(f_vec)).average().save("I_mw_on")
        I_mw_off_st.buffer(len(f_vec)).average().save("I_mw_off")
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
    simulation_config = SimulationConfig(duration=10_000)  # In clock cycles = 4ns
    job = qmm.simulate(config, cw_odmr, simulation_config)
    job.get_simulated_samples().con1.plot()
else:
    # Open the quantum machine
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(cw_odmr)
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
        plt.plot((NV_LO_freq * 0 + f_vec) / u.MHz, I_mw_on, label="mw on")
        plt.plot((NV_LO_freq * 0 + f_vec) / u.MHz, I_mw_off, label="mw off")
        plt.xlabel("MW frequency [MHz]")
        plt.ylabel("SPCM Voltage [V]")
        plt.title("ODMR")
        plt.legend()
        plt.pause(0.1)

    if save_data:
        # Arrange data to save
        data = {
            "fig_live": fig,
            "f_vec": f_vec,
            "I_mw_on": I_mw_on,
            "I_mw_off": I_mw_off,
            "iterations": np.array(iterations),
            "iteration": np.array([n]),  # convert int to np.array of int
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
