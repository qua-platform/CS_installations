"""
        ECHO MEASUREMENT
The program consists in playing a Ramsey sequence with an echo pulse in the middle to compensate for dephasing and
enhance the coherence time (x90 - idle_time - x180 - idle_time - x90 - measurement) for different idle times.
Here the gates are on resonance so no oscillation is expected.

From the results, one can fit the exponential decay and extract T2.

Prerequisites:
    - Having found the resonance frequency of the resonator coupled to the qubit under study (resonator_spectroscopy).
    - Having calibrated qubit pi pulse (x180) by running qubit, spectroscopy, rabi_chevron, power_rabi and updated the config.
    - Having the qubit frequency perfectly calibrated (ramsey).
    - (optional) Having calibrated the readout (readout_frequency, amplitude, duration_optimization IQ_blobs) for better SNR.
"""

import numpy as np
from qm.qua import *
from qm import QuantumMachinesManager
from qualang_tools.loops import from_array
from qualang_tools.results import fetching_tool, progress_counter
from qualang_tools.plot import interrupt_on_close
from qualang_tools.loops import from_array, get_equivalent_log_array
from qm_saas import QmSaas, QOPVersion
from qm import SimulationConfig
import matplotlib.pyplot as plt
from pathlib import Path
from scipy.signal import savgol_filter
from qualang_tools.units import unit
u = unit(coerce_to_integer=True)
from scipy import signal
from qualang_tools.bakery.randomized_benchmark_c1 import c1_table
from scipy.optimize import curve_fit
from qualang_tools.results.data_handler import DataHandler
from macros import multiplexed_parser, mp_result_names, mp_fetch_all, readout_macro

# ---- Choose which device configuration ---- #
if False:
    from configurations.DA_5Q.OPX1000config import *
else:
    from configurations.DB_6Q.OPX1000config import *

##################
#   Parameters   #
##################
# ---- Multiplexed program parameters ---- #
multiplexed = True
qubit_keys = ["q0", "q1", "q2", "q3"]
required_parameters = ["qubit_key", "qubit_frequency", "qubit_relaxation", "resonator_key", "readout_len", "resonator_relaxation"]
qub_key_subset, qub_frequency, qubit_relaxation, res_key_subset, readout_len, resonator_relaxation= multiplexed_parser(qubit_keys, multiplexed_parameters.copy(), required_parameters)


# ---- RB program parameters ---- #
n_avg = 1000  # Number of averaging loops
qub_relaxation = qubit_relaxation//4 # From ns to clock cycles
res_relaxation = resonator_relaxation//4 # From ns to clock cycles

# Dephasing time sweep (in clock cycles = 4ns) - minimum is 4 clock cycles
tau_min = 4
tau_max = 20_000 // 4
d_tau = 40 // 4
taus = np.arange(tau_min, tau_max + 0.1, d_tau)  # Linear sweep
# taus = np.logspace(np.log10(tau_min), np.log10(tau_max), 21)  # Log sweep

# Data to save
save_data_dict = {
    "qubit_keys": qub_key_subset,
    "n_avg": n_avg,
    "taus": taus,
    "config": config,
}
save_dir = Path(__file__).resolve().parent / "data"

###################
# The QUA program #
###################
with program() as echo:
    n = declare(int)
    n_st = declare_stream()
    I = [declare(fixed) for _ in qub_key_subset]
    I_st = [declare_stream() for _ in qub_key_subset]
    Q = [declare(fixed) for _ in qub_key_subset]
    Q_st = [declare_stream() for _ in qub_key_subset]
    tau = declare(int)

    with for_(n, 0, n < n_avg, n + 1):
        with for_(*from_array(tau, taus)):
            for j in range(len(qub_key_subset)):
                # 1st x90 pulse
                play("x90", qub_key_subset[j])
                # Wait the varying idle time
                wait(tau, qub_key_subset[j])
                # Echo pulse
                play("x180", qub_key_subset[j])
                # Wait the varying idle time
                wait(tau, qub_key_subset[j])
                # 2nd x90 pulse
                play("x90", qub_key_subset[j])
                # Align the two elements to measure after playing the qubit pulse.
                align(qub_key_subset[j], res_key_subset[j])
                # Measure the state of the resonator
                measure(
                    "readout",
                    res_key_subset[j],
                    dual_demod.full("opt_cos", "opt_sin", I[j]),
                    dual_demod.full("opt_minus_sin", "opt_cos", Q[j]),
                )
                # Save the 'I' & 'Q' quadratures to their respective streams
                save(I[j], I_st[j])
                save(Q[j], Q_st[j])
                # Wait for the resonator and qubit to decay
                if multiplexed:
                    wait(qub_relaxation[j], qub_key_subset[j])
                    wait(res_relaxation[j], res_key_subset[j])
                else:
                    align() # When python unravels, this makes sure the readouts are sequential
                    if j == len(res_key_subset)-1:
                        wait(np.max(res_relaxation), *res_key_subset)
                        wait(np.max(qub_relaxation), *qub_key_subset)
        # Save the averaging iteration to get the progress bar
        save(n, n_st)

    with stream_processing():
        n_st.save("iteration")
        # Cast the data into a 1D vector, average the 1D vectors together and store the results on the OPX processor
        # If log sweep, then the swept values will be slightly different from np.logspace because of integer rounding in QUA.
        # get_equivalent_log_array() is used to get the exact values used in the QUA program.
        if np.isclose(np.std(taus[1:] / taus[:-1]), 0, atol=1e-3):
            taus = get_equivalent_log_array(taus)
            for j in range(len(qub_key_subset)):
                I_st[j].buffer(len(taus)).average().save("I_" + str(j))
                Q_st[j].buffer(len(taus)).average().save("Q_" + str(j))
        else:
            for j in range(len(qub_key_subset)):
                I_st[j].buffer(len(taus)).average().save("I_" + str(j))
                Q_st[j].buffer(len(taus)).average().save("Q_" + str(j))


######################################
#  Open Communication with the QOP  #
######################################
prog = echo
from opx_credentials import qop_ip, cluster
qmm = QuantumMachinesManager(host=qop_ip, cluster_name=cluster)

###########################
# Run or Simulate Program #
###########################
simulate = False
if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=10_000)  # In clock cycles = 4ns
    # Simulate blocks python until the simulation is done
    job = qmm.simulate(config, prog, simulation_config)
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
    job = qm.execute(prog)
    # Get results from QUA program
    result_names = mp_result_names( qub_key_subset, single_tags = ["iteration"], mp_tags = ["I", "Q"] )
    res_handles = fetching_tool(job, data_list = result_names, mode = "live")
    # Live plotting
    fig = plt.figure()
    interrupt_on_close(fig, job)  # Interrupts the job when closing the figure
    while res_handles.is_processing():
        # Fetch results
        iteration, I, Q = mp_fetch_all(res_handles, qub_key_subset, num_single_tags=1)
        # Convert the results into Volts
        for j in range(len(qub_key_subset)):
            I[j], Q[j] = u.demod2volts(I[j], readout_len[j]), u.demod2volts(Q[j], readout_len[j])
        # Progress bar
        progress_counter(iteration, n_avg, start_time=res_handles.get_start_time())
        # Plot results
        plt.suptitle(f"Echo measurement")
        plt.subplot(211)
        plt.cla()
        for j in range(len(qub_key_subset)):
            plt.plot(8 * taus, I[j], ".", label=f"{qub_key_subset[j]}")
        plt.ylabel("I quadrature [V]")
        plt.subplot(212)
        plt.cla()
        for j in range(len(qub_key_subset)):
            plt.plot(8 * taus, Q[j], ".", label=f"{qub_key_subset[j]}")
        plt.xlabel("Idle time [ns]")
        plt.ylabel("Q quadrature [V]")
        plt.pause(0.1)
        plt.tight_layout()

    # Fit the results to extract the qubit coherence time T2
    from qualang_tools.plot.fitting import Fit
    for j in range(len(qub_key_subset)):
        try:
            fit = Fit()
            plt.figure()
            T2_fit = fit.T1(8 * taus, I[j], plot=True)
            qubit_T2 = np.abs(T2_fit["T1"][0])
            plt.xlabel("Delay [ns]")
            plt.ylabel("I quadrature [V]")
            print(f"Qubit coherence time T2 = {qubit_T2:.0f} ns")
            plt.legend((f"Coherence time T2 = {qubit_T2:.0f} ns",))
            plt.title(f"Qubit, {qub_key_subset[j]}: Echo measurement")
        except (Exception,):
            plt.figure()
            plt.plot(8 * taus, I[j], ".")
            plt.title(f"Qubit, {qub_key_subset[j]}: Echo measurement")
            plt.xlabel("Delay [ns]")
            plt.ylabel("I quadrature [V]")
            print("Unable to fit qubit " + str(qub_key_subset[j]))
    # Save results
    script_name = Path(__file__).name
    data_handler = DataHandler(root_data_folder=save_dir)
    save_data_dict.update({"I_data": I})
    save_data_dict.update({"Q_data": Q})
    save_data_dict.update({"fig_live": fig})
    data_handler.additional_files = {script_name: script_name, **default_additional_files}
    data_handler.save_data(data=save_data_dict, name="_".join(script_name.split("_")[1:]).split(".")[0])