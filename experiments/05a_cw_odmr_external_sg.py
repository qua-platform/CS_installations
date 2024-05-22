# %%
"""
        CW Optically Detected Magnetic Resonance (ODMR) With External SG
The program consists in playing a mw trigger and the readout laser pulse simultaneously to extract
the photon counts received by the PD across varying intermediate frequencies.
The sequence is repeated without playing the mw pulses to measure the dark counts on the PD.

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
from qualang_tools.results import progress_counter, fetching_tool, wait_until_job_is_paused
from qualang_tools.plot import interrupt_on_close
from qualang_tools.loops import from_array
from qualang_tools.results.data_handler import DataHandler
import matplotlib.pyplot as plt
from configuration import *

import pyvisa # ek

###################
# The QUA program #
###################

# MW Power
MWP = 0 # dBm

# SG setting
rm = pyvisa.ResourceManager()
visa_list = rm.list_resources()
sg = rm.open_resource(visa_list[0])
sg.write(":POWER {0:f}".format(MWP))
sg.write(":OUTP:STAT ON")

# Frequency vector
#f_vec = np.arange(-30e6, 70e6, 2e6)
f_vec = np.arange(2.74e9, 3.00e9, 2e6)
n_avg = 1_000  # number of averages
readout_len = long_meas_len  # Readout duration for this experiment
resolution = 12 # ns


# Main sequence macro
def play_laser_mw_and_measure_pd(times, counts, mw_amp_ratio: float = 1):
    # play laser and mw
    play("cw" * amp(mw_amp_ratio), "NV", duration=readout_len * u.ns)
    # ... and the laser pulse simultaneously (the laser pulse is delayed by 'laser_delay_1')
    play("laser_ON", "AOM", duration=readout_len * u.ns)
    # so readout don't catch the first part of spin reinitialization
    wait(1_000 * u.ns, "PD")
    # Measure and detect the photons on PD
    measure("readout", "PD", None, time_tagging.analog(times, meas_len, counts))
    # data to stream processor
    return counts


with program() as cw_odmr:
    f = declare(int)
    n = declare(int)  # variable used in for loop for averaging
    times_on = declare(int, size=5000)  # QUA vector for storing the time-tags
    times_off = declare(int, size=5000)  # QUA vector for storing the time-tags
    counts_on = declare(int)  # variable for number of counts of a single chunk
    counts_off = declare(int)  # variable for number of counts of a single chunk
    
    n_st = declare_stream()  # stream variable used in for loop for averaging
    counts_on_st = declare_stream()  # stream for 'times'
    counts_off_st = declare_stream()  # stream for 'times'

    with for_(n, 0, n < n_avg, n + 1):
        with for_(*from_array(f, f_vec)):
            pause()
            wait(1 * u.us)

            # align all elements 
            align()
            # play laser and mw
            counts_on = play_laser_mw_and_measure_pd(times_on, counts_on, mw_amp_ratio=1)
            # Wait and align all elements before measuring the dark events
            wait(wait_between_runs * u.ns)
            save(counts_on, counts_on_st)
            
            # align all elements 
            align()
            # play laser and mw
            counts_off = play_laser_mw_and_measure_pd(times_off, counts_off, mw_amp_ratio=0)
            # Wait and align all elements before measuring the next iterations
            wait(wait_between_runs * u.ns)
            save(counts_off, counts_off_st)

            # save data for iterations
            save(n, n_st)

    with stream_processing():
        # Directly derive the histograms in the stream processing
        counts_on_st.buffer(len(f_vec)).average().save("counts_on")
        counts_off_st.buffer(len(f_vec)).average().save("counts_off")
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
    job = qmm.simulate(config, cw_odmr, simulation_config)
    job.get_simulated_samples().con1.plot()
else:
    # Open the quantum machine
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(cw_odmr)
    # Live plotting
    fig = plt.figure()
    interrupt_on_close(fig, job)  # Interrupts the job when closing the figure  
    for i, f in enumerate(f_vec):
        # update frequency
        sg.write(":FREQ {0:e} Hz".format(f)) # Hz
        # Resume the QUA program (escape the 'pause' statement)
        job.resume()
        # Wait until the program reaches the 'pause' statement again, indicating that the QUA program is done
        wait_until_job_is_paused(job)
        # Fetch results from QUA program and initialize live plotting
        if i == 0:
            # Get results from QUA program
            results = fetching_tool(job, data_list=["counts_on", "counts_off", "iterations"], mode="live")
        counts_on, counts_off, iterations = results.fetch_all()
        # Progress bar
        progress_counter(iterations, n_avg, start_time=results.get_start_time())
        # Plot data
        plt.cla()
        plt.plot((NV_LO_freq * 0 + f_vec) / u.MHz, counts_on, label="mw on")
        plt.plot((NV_LO_freq * 0 + f_vec) / u.MHz, counts_off, label="mw off")
        plt.xlabel("MW frequency [MHz]")
        plt.ylabel("PD Voltage [V]")
        plt.title("ODMR")
        plt.legend()
        plt.pause(0.1)

    if save_data:
        # Arrange data to save
        data = {
            "fig_live": fig,
            "f_vec": f_vec,
            "counts_on": counts_on,
            "counts_off": counts_off,
            "iterations": iterations,
            "resolution": resolution,
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
