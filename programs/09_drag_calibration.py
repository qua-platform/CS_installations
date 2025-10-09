"""
        DRAG PULSE CALIBRATION (GOOGLE METHOD)
The sequence consists in applying an increasing number of x180 and -x180 pulses successively while varying the DRAG
coefficient alpha. After such a sequence, the qubit is expected to always be in the ground state if the DRAG
coefficient has the correct value. Note that the idea is very similar to what is done in power_rabi_error_amplification.

This protocol is described in more details in https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.117.190503

Prerequisites:
    - Having found the resonance frequency of the resonator coupled to the qubit under study (resonator_spectroscopy).
    - Having calibrated qubit pi pulse (x180) by running qubit, spectroscopy, rabi_chevron, power_rabi and updated the config.
    - (optional) Having calibrated the readout (readout_frequency, amplitude, duration_optimization IQ_blobs) for better SNR.
    - Set the DRAG coefficient to a non-zero value in the config: such as drag_coef = 1

Next steps before going to the next node:
    - Update the DRAG coefficient (drag_coef) in the configuration.
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

if False:
    from configurations.DA_5Q.OPX1000config import *
else:
    from configurations.DB_6Q.OPX1000config import *

##################
#   Parameters   #
##################
# ---- Multiplexed program parameters ---- #
n_avg = 100 # number of averages for each sequence
multiplexed = True
qubit_keys = ["q0", "q1", "q2", "q3"]
required_parameters = ["qubit_key", "qubit_frequency", "qubit_relaxation", "resonator_key", "readout_len", "resonator_relaxation", "ge_threshold", "drag_coef"]
qub_key_subset, qub_frequency, qubit_relaxation, res_key_subset, readout_len, resonator_relaxation, ge_threshold, drag_coef_subset = multiplexed_parser(qubit_keys, multiplexed_parameters.copy(), required_parameters)


# ---- RB program parameters ---- #
qub_relaxation = qubit_relaxation//4 # From ns to clock cycles
res_relaxation = resonator_relaxation//4 # From ns to clock cycles

# Scan the DRAG coefficient pre-factor
a_min = 0.0
a_max = 1.0
da = 0.1
amps = np.arange(a_min, a_max + da / 2, da)  # + da/2 to add a_max to amplitudes

# Scan the number of pulses
iter_min = 0
iter_max = 25
d = 1
iters = np.arange(iter_min, iter_max + 0.1, d)

# ---- Data to save ---- #
save_data_dict = {
    "qubit_keys": qub_key_subset,
    "n_avg": n_avg,
    "amplitudes": amps,
    "iters": iters,
    "config": config,
}
save_dir = Path(__file__).resolve().parent / "data"

###################
# The QUA program #
###################
with program() as drag_calibration:
    n = declare(int)  # QUA variable for the averaging loop
    a = declare(fixed)  # QUA variable for the DRAG coefficient pre-factor
    it = declare(int)  # QUA variable for the number of qubit pulses
    pulses = declare(int)  # QUA variable for counting the qubit pulses
    I = [declare(fixed) for _ in range(len(qub_key_subset))]  # QUA variable for the measured 'I' quadrature
    Q = [declare(fixed) for _ in range(len(qub_key_subset))]  # QUA variable for the measured 'Q' quadrature
    state = [declare(int) for _ in range(len(qub_key_subset))]  # QUA variable for the qubit state
    I_st = [declare_stream() for _ in range(len(qub_key_subset))]  # Stream for the 'I' quadrature
    Q_st = [declare_stream() for _ in range(len(qub_key_subset))]  # Stream for the 'Q' quadrature
    state_st = [declare_stream() for _ in range(len(qub_key_subset))]  # Stream for the qubit state
    n_st = declare_stream()  # Stream for the averaging iteration 'n'

    with for_(n, 0, n < n_avg, n + 1):  # QUA for_ loop for averaging
        with for_(*from_array(a, amps)):  # QUA for_ loop for sweeping the pulse amplitude
            with for_(*from_array(it, iters)):  # QUA for_ loop for sweeping the number of pulses
                for j in range(len(qub_key_subset)): # a real Python for loop so it unravels and executes in parallel, not sequentially
                    with for_(pulses, iter_min, pulses <= it, pulses + d):
                        play("x180" * amp(1, 0, 0, a), qub_key_subset[j])
                        play("x180" * amp(-1, 0, 0, -a), qub_key_subset[j])
                    # Align the two elements to measure after playing the qubit pulses.
                    align(res_key_subset[j], qub_key_subset[j])
                    # Measure the resonator and extract the qubit state
                    state[j], I[j], Q[j] = readout_macro(res_key_subset[j], I[j], Q[j], state[j], threshold=ge_threshold[j])
                    # Save the 'I' & 'Q' quadratures to their respective streams
                    save(I[j], I_st[j])
                    save(Q[j], Q_st[j])
                    save(state[j], state_st[j])
                    if multiplexed:
                        wait(res_relaxation[j], res_key_subset[j])
                        wait(qub_relaxation[j], qub_key_subset[j]) 
                    else:
                        align() # When python unravels, this makes sure the readouts are sequential
                        if j == len(res_key_subset)-1:
                            wait(np.max(res_relaxation), *res_key_subset) 
                            wait(np.max(qub_relaxation), *qub_key_subset)
        # Save the averaging iteration to get the progress bar
        save(n, n_st)

    with stream_processing():
        n_st.save("iteration")
        # Cast the data into a 2D matrix, average the 2D matrices together and store the results on the OPX processor
        for j in range(len(qub_key_subset)):
            I_st[j].buffer(len(iters)).buffer(len(amps)).average().save("I_"+str(j))
            Q_st[j].buffer(len(iters)).buffer(len(amps)).average().save("Q_"+str(j))
            state_st[j].buffer(len(iters)).buffer(len(amps)).average().save("state_"+str(j))


prog = drag_calibration
# ---- Open communication with the OPX ---- #
from warsh_credentials import host_ip, cluster
qmm = QuantumMachinesManager(host = host_ip, cluster_name = cluster)

simulate = False
if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=20_000)  # In clock cycles = 4ns
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
    qm = qmm.open_qm(config, close_other_machines=True)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(prog)
    # Creates a result handle to fetch data from the OPX
    result_names = mp_result_names(qub_key_subset, single_tags = ["iteration"], mp_tags = ["I", "Q", "state"])
    res_handles = fetching_tool(job, data_list = result_names, mode = "live")
    # Waits (blocks the Python console) until all results have been acquired
    fig = plt.figure()
    interrupt_on_close(fig, job)  #  Interrupts the job when closing the figure
    while res_handles.is_processing():
        # Fetch results
        iteration, I, Q, state = mp_fetch_all(res_handles, qub_key_subset, num_single_tags=1)
        # Convert the results into Volts
        for j in range(len(qub_key_subset)):
            I[j] = u.demod2volts(I[j], readout_len[j])
            Q[j] = u.demod2volts(Q[j], readout_len[j])
        # Progress bar
        progress_counter(iteration, n_avg, start_time=res_handles.get_start_time())
        # Plot results
        plt.suptitle("DRAG calibration (Google)")
        plt.subplot(231)
        plt.cla()
        for j in range(len(qub_key_subset)):
            plt.pcolor(iters, amps * drag_coef_subset[j], I[j], cmap="magma")
        plt.xlabel("Number of iterations")
        plt.ylabel(r"Drag coefficient $\alpha$")
        plt.title("I [V]")
        plt.subplot(232)
        plt.cla()
        for j in range(len(qub_key_subset)):
            plt.pcolor(iters, amps * drag_coef_subset[j], Q[j], cmap="magma")
        plt.xlabel("Number of iterations")
        plt.title("Q [V]")
        plt.subplot(233)
        plt.cla()
        for j in range(len(qub_key_subset)):
            plt.pcolor(iters, amps * drag_coef_subset[j], state[j], cmap="magma")
        plt.xlabel("Number of iterations")
        plt.title("State")
        plt.subplot(212)
        plt.cla()
        for j in range(len(qub_key_subset)):
            plt.plot(amps * drag_coef_subset[j], np.sum(I[j], axis=1))
        plt.xlabel(r"Drag coefficient $\alpha$")
        plt.ylabel("Sum along the iterations")
        plt.tight_layout()
        plt.pause(0.1)
    for j in range(len(qub_key_subset)):
        print(f"Qubit {qub_key_subset[j]}, Optimal drag_coef = {drag_coef_subset[j] * amps[np.argmin(np.sum(I[j], axis=1))]:.3f}")

    # Save results
    script_name = Path(__file__).name
    data_handler = DataHandler(root_data_folder=save_dir)
    save_data_dict.update({"I_data": I})
    save_data_dict.update({"Q_data": Q})
    save_data_dict.update({"fig_live": fig})
    data_handler.additional_files = {script_name: script_name, **default_additional_files}
    data_handler.save_data(data=save_data_dict, name="_".join(script_name.split("_")[1:]).split(".")[0])
    
    qm.close()