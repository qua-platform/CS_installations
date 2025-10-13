"""
        RAMSEY WITH DETUNED GATES
The program consists in playing a Ramsey sequence (x90 - idle_time - x90 - measurement) for different idle times.
A detuning is set in order to measure Ramsey oscillations and extract the qubit frequency and T2*.

From the results, one can fit the Ramsey oscillations and precisely measure the qubit resonance frequency and T2*.

Prerequisites:
    - Having found the resonance frequency of the resonator coupled to the qubit under study (resonator_spectroscopy).
    - Having calibrated qubit pi pulse (x180) by running qubit, spectroscopy, rabi_chevron, power_rabi and updated the config.
    - (optional) Having calibrated the readout (readout_frequency, amplitude, duration_optimization IQ_blobs) for better SNR.

Next steps before going to the next node:
    - Update the qubit frequency (qubit_IF) in the configuration.
"""
from qm.qua import *
from qm import QuantumMachinesManager
from qm import SimulationConfig
from qualang_tools.results import progress_counter, fetching_tool
from qualang_tools.plot import interrupt_on_close
from qualang_tools.loops import from_array
import matplotlib.pyplot as plt
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
n_avg = 1000
multiplexed = True
qubit_keys = ["q0", "q1", "q2", "q3"]
required_parameters = ["qubit_key", "qubit_IF", "qubit_relaxation", "qubit_LO", "resonator_key", "readout_len", "resonator_relaxation"]
qub_key_subset, qubit_IF, qubit_relaxation, qubit_LO, res_key_subset, readout_len, resonator_relaxation = multiplexed_parser(qubit_keys, multiplexed_parameters.copy(), required_parameters)

qub_relaxation = qubit_relaxation//4 # From ns to clock cycles
res_relaxation = resonator_relaxation//4 # From ns to clock cycles
# Dephasing time sweep (in clock cycles = 4ns) - minimum is 4 clock cycles
tau_min = 4
tau_max = 2000 // 4
d_tau = 40 // 4
taus = np.arange(tau_min, tau_max + 0.1, d_tau)  # + 0.1 to add tau_max to taus
# Detuning converted into virtual Z-rotations to observe Ramsey oscillation and get the qubit frequency
detuning = 1 * u.MHz  # in Hz

# Data to save
save_data_dict = {
    "n_avg": n_avg,
    "taus": taus,
    "detuning": detuning,
    "config": config,
}
save_dir = Path(__file__).resolve().parent / "data"

###################
# The QUA program #
###################
with program() as ramsey:
    n = declare(int)  # QUA variable for the averaging loop
    tau = declare(int)  # QUA variable for the idle time
    I = [declare(fixed) for _ in range(len(qub_key_subset))]
    Q = [declare(fixed) for _ in range(len(qub_key_subset))]
    I_st = [declare_stream() for _ in range(len(qub_key_subset))]
    Q_st = [declare_stream() for _ in range(len(qub_key_subset))]
    n_st = declare_stream()  # Stream for the averaging iteration 'n'

    # Shift the qubit drive frequency to observe Ramsey oscillations
    for j in range(len(qub_key_subset)):
        update_frequency(qub_key_subset[j], qubit_IF[j] + detuning)

    with for_(*from_array(tau, taus)):
        with for_(n, 0, n < n_avg, n + 1):
            for j in range(len(qub_key_subset)):
                # 1st x90 gate
                play("x90", qub_key_subset[j])
                # Wait a varying idle time
                wait(tau, qub_key_subset[j])
                # 2nd x90 gate
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
        for j in range(len(qub_key_subset)):
            # Cast the data into a 1D vector, average the 1D vectors together and store the results on the OPX processor
            I_st[j].buffer(len(taus)).average().save("I_" + str(j))
            Q_st[j].buffer(len(taus)).average().save("Q_" + str(j))
        

#####################################
#  Open Communication with the QOP  #
#####################################
prog = ramsey
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
    result_names = mp_result_names(qub_key_subset, single_tags = ["iteration"], mp_tags = ["I", "Q"])
    res_handles = fetching_tool(job, data_list = result_names, mode = "live")
    # Live plotting
    fig = plt.figure()
    interrupt_on_close(fig, job)  # Interrupts the job when closing the figure
    while res_handles.is_processing():
        # Fetch results
        iteration, I, Q = mp_fetch_all(res_handles, qub_key_subset, num_single_tags=1)
        # Progress bar
        progress_counter(iteration, len(taus), start_time=res_handles.get_start_time())
    
    for j in range(len(qub_key_subset)):
        I[j] = u.demod2volts(I[j], readout_len[j])
        Q[j] = u.demod2volts(Q[j], readout_len[j])
    # Plot results
    plt.suptitle(f"Ramsey with detuned gates: {detuning / u.MHz} MHz")
    plt.subplot(211)
    plt.cla()
    for j in range(len(qub_key_subset)):
        plt.plot(4 * taus, I[j], ".", label=f"{qub_key_subset[j]}")
    plt.ylabel("I quadrature [V]")
    plt.subplot(212)
    plt.cla()
    for j in range(len(qub_key_subset)):
        plt.plot(4 * taus, Q[j], ".", label=f"{qub_key_subset[j]}")
    plt.xlabel("Idle time [ns]")
    plt.ylabel("Q quadrature [V]")
    plt.pause(0.1)
    plt.tight_layout()

    # Fit the results to extract the qubit frequency and T2*
    from qualang_tools.plot.fitting import Fit
    for j in range(len(qub_key_subset)):
        try:
            fit = Fit()
            plt.figure()
            ramsey_fit = fit.ramsey(4 * taus, I[j], plot=True)
            qubit_T2 = np.abs(ramsey_fit["T2"][0])
            qubit_detuning = ramsey_fit["f"][0] * u.GHz - detuning
            plt.xlabel("Idle time [ns]")
            plt.ylabel("I quadrature [V]")
            print(f"Qubit detuning to update in the config: qubit_IF += {-qubit_detuning:.0f} Hz")
            print(f"T2* = {qubit_T2:.0f} ns")
            plt.legend((f"detuning = {-qubit_detuning / u.kHz:.3f} kHz", f"T2* = {qubit_T2:.0f} ns"))
            plt.title(f"Qubit {qub_key_subset[j]}: Ramsey measurement with detuned gates")
            print(f"Qubit {qub_key_subset[j]}, Detuning to add: {-qubit_detuning / u.kHz:.3f} kHz")
        except (Exception,):
            plt.figure()
            plt.plot(4 * taus, I[j], ".")
            plt.title(f"Qubit {qub_key_subset[j]}: Ramsey measurement with detuned gates")
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