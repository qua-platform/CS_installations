"""
        READOUT OPTIMISATION: FREQUENCY
This sequence involves measuring the state of the resonator in two scenarios: first, after thermalization
(with the qubit in the |g> state) and then after applying a pi pulse to the qubit (transitioning the qubit to the
|e> state). This is done while varying the readout frequency.
The average I & Q quadratures for the qubit states |g> and |e>, along with their variances, are extracted to
determine the Signal-to-Noise Ratio (SNR). The readout frequency that yields the highest SNR is selected as the
optimal choice.

Prerequisites:
    - Having found the resonance frequency of the resonator coupled to the qubit under study (resonator_spectroscopy).
    - Having calibrated qubit pi pulse (x180) by running qubit, spectroscopy, rabi_chevron, power_rabi and updated the config.

Next steps before going to the next node:
    - Update the readout frequency (resonator_IF) in the configuration.
"""

import numpy as np
from qm.qua import *
from qm import QuantumMachinesManager
from qualang_tools.loops import from_array
from qualang_tools.results import fetching_tool, progress_counter
from qualang_tools.analysis import two_state_discriminator
from qualang_tools.plot import interrupt_on_close
from qm_saas import QmSaas, QOPVersion
from qm import SimulationConfig
import matplotlib.pyplot as plt
from pathlib import Path
from scipy.signal import savgol_filter
from qualang_tools.units import unit
u = unit(coerce_to_integer=True)
from scipy import signal
from macros import multiplexed_parser, mp_result_names, mp_fetch_all

if False:
    from configurations.OPX1000config_DA_5Q import *
else:
    from configurations.OPX1000config_DB_6Q import *

##################
#   Parameters   #
##################
# Parameters Definition
# ---- Multiplexed program parameters ---- #
n_avg = 100
multiplexed = True
qubit_keys = ["q0", "q1", "q2", "q3"]
required_parameters = ["qubit_key", "qubit_relaxation", "resonator_key", "readout_len", "resonator_relaxation", "resonator_IF", "readout_amp"]
qub_key_subset, qubit_relaxation, res_key_subset, readout_len, resonator_relaxation, resonator_IF, readout_amp = multiplexed_parser(qubit_keys, multiplexed_parameters.copy(), required_parameters)

thermalization_time = qubit_relaxation//4  # ns to clock cycles
res_relaxation = resonator_relaxation//4  # ns to clock cycles

# The readout amplitude sweep (as a pre-factor of the readout amplitude) - must be within [-2; 2)
a_min = 0.5
a_max = 1.5
da = 0.01
amplitudes = np.arange(a_min, a_max + da / 2, da)  # The amplitude vector +da/2 to add a_max to the scan

###################
# The QUA program #
###################
with program() as ro_amp_opt:
    n = declare(int)
    n_st = declare_stream()
    a = declare(fixed)
    I_g = [declare(fixed) for _ in range(len(qub_key_subset))]
    Q_g = [declare(fixed) for _ in range(len(qub_key_subset))]
    I_g_st = [declare_stream() for _ in range(len(res_key_subset))]
    Q_g_st = [declare_stream() for _ in range(len(res_key_subset))]
    I_e = [declare(fixed) for _ in range(len(qub_key_subset))]
    Q_e = [declare(fixed) for _ in range(len(qub_key_subset))]
    I_e_st = [declare_stream() for _ in range(len(res_key_subset))]
    Q_e_st = [declare_stream() for _ in range(len(res_key_subset))]
    n_st = declare_stream()

    with for_(n, 0, n < n_avg, n + 1):
        with for_(*from_array(a, amplitudes)):
            for j in range(len(qub_key_subset)):  # A Python for loop so it unravels and executes in parallel, not sequentially
                # Measure the state of the resonator
                measure(
                    "readout" * amp(a),
                    res_key_subset[j],
                    dual_demod.full("rotated_cos", "rotated_sin", I_g[j]),
                    dual_demod.full("rotated_minus_sin", "rotated_cos", Q_g[j]),
                )
                # Wait for the qubit to decay to the ground state
                wait(thermalization_time[j], qub_key_subset[j])
                wait(res_relaxation[j], res_key_subset[j])
                # Save the 'I_g' & 'Q_g' quadratures to their respective streams
                save(I_g[j], I_g_st[j])
                save(Q_g[j], Q_g_st[j])

                align()  # global align
                # Play the x180 gate to put the qubit in the excited state
                play("x180", qub_key_subset[j])
                # Align the two elements to measure after playing the qubit pulse.
                align(qub_key_subset[j], res_key_subset[j])
                # Measure the state of the resonator
                measure(
                    "readout" * amp(a),
                    res_key_subset[j],
                    None,
                    dual_demod.full("rotated_cos", "rotated_sin", I_e[j]),
                    dual_demod.full("rotated_minus_sin", "rotated_cos", Q_e[j]),
                )
                # Save the 'I_e' & 'Q_e' quadratures to their respective streams
                save(I_e[j], I_e_st[j])
                save(Q_e[j], Q_e_st[j])
                if multiplexed:
                    wait(res_relaxation[j], res_key_subset[j])
                    wait(thermalization_time[j], qub_key_subset[j]) 
                else:
                    align() # When python unravels, this makes sure the readouts are sequential
                    if j == len(res_key_subset)-1:
                        wait(np.max(res_relaxation), *res_key_subset) 
                        wait(np.max(thermalization_time), *qub_key_subset)
        # Save the averaging iteration to get the progress bar
        save(n, n_st)

    with stream_processing():
        n_st.save("iteration")
        for j in range(len(qub_key_subset)):
            # Save all streamed points for plotting the IQ blobs
            I_g_st[j].buffer(len(amplitudes)).buffer(n_avg).save("I_g_"+str(j))
            Q_g_st[j].buffer(len(amplitudes)).buffer(n_avg).save("Q_g_"+str(j))
            I_e_st[j].buffer(len(amplitudes)).buffer(n_avg).save("I_e_"+str(j))
            Q_e_st[j].buffer(len(amplitudes)).buffer(n_avg).save("Q_e_"+str(j))

#####################################
#  Open Communication with the QOP  #
#####################################
#qmm = QuantumMachinesManager(host=qop_ip, port=qop_port, cluster_name=cluster_name, octave=octave_config)
prog = ro_amp_opt
# ---- Open communication with the OPX ---- #
from warsh_credentials import host_ip, cluster
qmm = QuantumMachinesManager(host = host_ip, cluster_name = cluster)


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
    job = qm.execute(prog)  # execute QUA program
    # Get results from QUA program
    result_names = mp_result_names(qub_key_subset, single_tags = ["iteration"],mp_tags=["I_g", "Q_g", "I_e", "Q_e"])
    res_handles = fetching_tool(job, data_list=result_names, mode="live")
    # Waits (blocks the Python console) until all results have been acquired
    # Create subplots for all qubits
    fig, axs = plt.subplots(len(qub_key_subset), 1, figsize=(8, 4 * len(qub_key_subset)), sharex=True)
    interrupt_on_close(fig, job)  # Interrupts the job when closing the figure
    while res_handles.is_processing():
        # Fetch results
        iteration, I_g, Q_g, I_e, Q_e = mp_fetch_all(res_handles, qub_key_subset, num_single_tags=1)
        # Progress bar
        progress_counter(iteration, n_avg, start_time=res_handles.get_start_time())
        expected_shape = (n_avg, len(amplitudes))
        # Check that I_g has the expected shape
        if I_g[-1].shape != expected_shape:
            pass 
        else:
            for j in range(len(qub_key_subset)):
                # Process the data
                fidelity_vec = []
                ground_fidelity_vec = []
                Ig, Qg = I_g[j].T, Q_g[j].T
                Ie, Qe = I_e[j].T, Q_e[j].T
                for i in range(len(amplitudes)):
                    angle, threshold, fidelity, gg, ge, eg, ee = two_state_discriminator(
                        Ig, Qg, Ie, Qe, b_print=False, b_plot=False
                    )
                    fidelity_vec.append(fidelity)
                    ground_fidelity_vec.append(gg)

                # Plot the data for each qubit in its own subplot
                ax = axs[j]
                ax.clear()
                ax.plot(amplitudes * readout_amp[j], fidelity_vec, "b.-", label="averaged fidelity")
                ax.plot(amplitudes * readout_amp[j], ground_fidelity_vec, "r.-", label="ground fidelity")
                ax.set_title(f"Readout amplitude optimization: {qub_key_subset[j]}")
                ax.set_xlabel("Readout amplitude [V]")
                ax.set_ylabel("Readout fidelity [%]")
                ax.legend(
                    (
                        f"readout_amp = {readout_amp[j] * amplitudes[np.argmax(fidelity_vec)] / u.mV:.3f} mV, for {max(fidelity_vec):.1f}% averaged fidelity",
                        f"readout_amp = {readout_amp[j] * amplitudes[np.argmax(ground_fidelity_vec)] / u.mV:.3f} mV, for {max(ground_fidelity_vec):.1f}% ground fidelity",
                    )
                )
                print(
                    f"Resonator {res_key_subset[j]}: The optimal readout amplitude is {readout_amp[j] * amplitudes[np.argmax(fidelity_vec)] / u.mV:.3f} mV (Averaged fidelity={max(fidelity_vec):.1f}%)"
                )
                print(
                    f"Resonator {res_key_subset[j]}: The optimal readout amplitude is {readout_amp[j] * amplitudes[np.argmax(ground_fidelity_vec)] / u.mV:.3f} mV (Ground fidelity={max(ground_fidelity_vec):.1f}%)"
                )
            plt.tight_layout()
            plt.pause(0.1)
        
    qm.close()


