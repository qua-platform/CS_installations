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
import numpy as np
from qm import QuantumMachinesManager
from qm.qua import *
from qm import SimulationConfig
import matplotlib.pyplot as plt
from qualang_tools.loops import from_array
from qualang_tools.plot import interrupt_on_close
from qualang_tools.results import fetching_tool, progress_counter

from configuration import *
from qualang_tools.results.data_handler import DataHandler

##################
#   Parameters   #
##################
# Parameters Definition
f_trapping_vec = [-10 * u.MHz, -20 * u.MHz, -15 * u.MHz, -175 * u.MHz]  # Frequency vector
f_repump_vec = [-20 * u.MHz, -9 * u.MHz, -5 * u.MHz, -7 * u.MHz]  # Frequency vector
f_prove_vec = np.arange(-30 * u.MHz, 70 * u.MHz, 10 * u.MHz)  # Frequency vector
n_avg = 1_000_000  # number of averages
readout_len = long_meas_len_1  # Readout duration for this experiment

if len(f_trapping_vec) !=len(f_repump_vec) <= 0: raise ValueError("Invalid value: len(f_trapping_vec) should be equal to len(f_repump_vec).")


# Data to save
save_data_dict = {
    "n_avg": n_avg,
    "trap_frequencies": f_trapping_vec,
    "repump_frequencies": f_repump_vec,
    "probe_frequencies": f_prove_vec,
    "config": config,
}

###################
# The QUA program #
###################
with program() as pg_cooling:
    f_trap = declare(int)
    with for_(for_each_(f_trap, [-10e6, 10e6])):
            update_frequency("AOM_trapping",  f_trap)
            play("const", "AOM_trapping")


#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(host=qop_ip, cluster_name=cluster_name, octave=octave_config)

#######################
# Simulate or execute #
#######################
simulate = True

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=10_000)  # In clock cycles = 4ns
    # Simulate blocks python until the simulation is done
    job = qmm.simulate(config, pg_cooling, simulation_config)
    job.wait_until("Done", timeout=120)
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
    job = qm.execute(pg_cooling)
