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
f_trapping_vec = [-10 * u.MHz, -20 * u.MHz, -15 * u.MHz, -175 * u.MHz]  # Trapping frequency vector
f_repump_vec = [-20 * u.MHz, -9 * u.MHz, -5 * u.MHz, -7 * u.MHz]  # Repump frequency vector
f_probe_vec = np.arange(-30 * u.MHz, 70 * u.MHz, 10 * u.MHz)  # Probe frequency vector
n_avg = 1_000_000  # number of averages
readout_len = meas_len_1  # Readout duration for this experiment

if len(f_trapping_vec) != len(f_repump_vec) <= 0: raise ValueError(
    "Invalid value: len(f_trapping_vec) should be equal to len(f_repump_vec).")

# Data to save
save_data_dict = {
    "n_avg": n_avg,
    "trap_frequencies": f_trapping_vec,
    "repump_frequencies": f_repump_vec,
    "probe_frequencies": f_probe_vec,
    "config": config,
}

###################
# The QUA program #
###################
with program() as pg_cooling:
    times = declare(int, size=1000)  # QUA vector for storing the time-tags
    counts = declare(int)  # variable for number of counts
    counts_st = declare_stream()  # stream for counts
    f_trap = declare(int)  # frequencies
    f_repump = declare(int)  # frequencies
    f_probe = declare(int)  # frequencies
    n = declare(int)  # number of iterations
    n_st = declare_stream()  # stream for number of iterations

    with for_(n, 0, n < n_avg, n + 1):
        with for_each_((f_trap, f_repump), (f_trapping_vec, f_repump_vec)):
            with for_(*from_array(f_probe, f_probe_vec)):
                ################
                #      MOT     #
                ################
                align()
                play("const", "AOM_trapping", duration=rf_length * u.ns)
                play("const", "AOM_repump", duration=rf_length * u.ns)
                play("const", "B_field", duration=rf_length * u.ns)

                align()

                ################
                #   CMOT PG    #
                ################
                update_frequency("AOM_trapping", AOM_trapping_frequency + f_trap, keep_phase=True)
                update_frequency("AOM_repump", AOM_repump_frequency + f_repump, keep_phase=True)
                align()
                play("const", "AOM_trapping", duration=rf_length * u.ns)
                play("const", "AOM_repump", duration=rf_length * u.ns)
                play(ramp(0.0001), "B_field", duration=rf_length * u.ns)  # the slope is in units of V/ns
                ramp_to_zero("B_field")
                # bring the AOM_trapping and AOM_repump frequency back to the one specified in the configuration
                update_frequency("AOM_trapping", AOM_trapping_frequency, keep_phase=True)
                update_frequency("AOM_repump", AOM_repump_frequency, keep_phase=True)
                align()
                ################
                #   measure    #
                ################
                # updated the AOM_probe frequency
                update_frequency("AOM_probe", f_probe)
                play("const", "AOM_probe", duration=readout_len * u.ns)

                # Measure and detect the photons on PMT
                measure("readout", "PMT", time_tagging.analog(times, readout_len, counts))

                save(counts, counts_st)  # save counts on stream

                # Wait and align all elements before measuring the dark events
                wait(wait_between_runs * u.ns)

                save(n, n_st)  # save number of iteration inside for_loop

    with stream_processing():
        # Cast the data into a 1D vector, average the 1D vectors together and store the results on the OPX processor
        counts_st.buffer(len(f_probe_vec)).buffer(len(f_trapping_vec)).average().save("counts")
        n_st.save("iteration")

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
    # Get results from QUA program
    results = fetching_tool(job, data_list=["counts", "iteration"], mode="live")
    # Live plotting
    fig = plt.figure()
    interrupt_on_close(fig, job)  # Interrupts the job when closing the figure

    while results.is_processing():
        # Fetch results
        counts, counts_dark, iteration = results.fetch_all()
        # Progress bar
        progress_counter(iteration, n_avg, start_time=results.get_start_time())
        # Plot data
        plt.cla()
        plt.plot(f_probe_vec / u.MHz, counts / 1000 / (readout_len * 1e-9), label="photon counts")
        plt.xlabel("Probe frequency [MHz]")
        plt.ylabel("Intensity [kcps]")
        plt.title("PG cooling")
        plt.legend()
        plt.pause(0.1)
    # Save results
    script_name = Path(__file__).name
    data_handler = DataHandler(root_data_folder=save_dir)
    save_data_dict.update({"counts_data": counts})
    save_data_dict.update({"fig_live": fig})
    data_handler.additional_files = {script_name: script_name, **default_additional_files}
    data_handler.save_data(data=save_data_dict, name="_".join(script_name.split("_")[1:]).split(".")[0])
