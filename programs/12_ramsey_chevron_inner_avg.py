import numpy as np
from qm.qua import *
from qm import QuantumMachinesManager
from qualang_tools.loops import from_array
from qualang_tools.results import fetching_tool, progress_counter
from qualang_tools.plot import interrupt_on_close
from qm_saas import QmSaas, QOPVersion
from qm import SimulationConfig
import matplotlib.pyplot as plt
from pathlib import Path
from scipy.signal import savgol_filter
from qualang_tools.units import unit
u = unit(coerce_to_integer=True)
from scipy import signal
from macros import multiplexed_parser

if False:
    from configurations.OPX1000config_DA_5Q import *
else:
    from configurations.OPX1000config_DB_6Q import *

# ---- Multiplexed program parameters ----
n_avg = 1000
multiplexed = True
qub_relaxation = qubit_relaxation//4 # From ns to clock cycles
res_relaxation = resonator_relaxation//4 # From ns to clock cycles

# ---- Time Rabi Chevron Multiplexed ---- #
qubit_keys = ["q0", "q1", "q2", "q3"]
qub_key_subset, qub_freq_subset, res_key_subset, res_freq_subset, readout_lens, ge_thresholds, drag_coef_subset,  = multiplexed_parser(qubit_keys, multiplexed_parameters)

qub_IFs = qub_freq_subset - qubit_LO
qub_detune_span = 20 * u.MHz
qub_detune_df = 2 * u.MHz
qub_detune_sweep_dfs = np.arange(-qub_detune_span, qub_detune_span + qub_detune_df, qub_detune_df)
qub_detune_frequencies = np.array([qub_detune_sweep_dfs + guess for guess in qub_freq_subset])

tau_min = 0 # ns
tau_max = 16000 # ns
dtau = 64 # ns
taus_ns = np.arange(tau_min, tau_max + dtau, dtau)
taus_cycles = taus_ns // 4 # Converted to clock cycles
taus_effective_ns = taus_ns + 16 # accounting for the 4 cycles of align (there is probably more, but I'll test later)

def ramsey_sequence(tau, qub_key):
    with if_(tau >= 4):
        play("x90", qub_key)
        wait(tau, qub_key)
        play("x90", qub_key)
    with else_():
        play("x90", qub_key)
        play("x90", qub_key)

with program() as ramsey_chevron_inner_avg:
    n = declare(int)
    i = declare(int)
    n_st = declare_stream()
    tau = declare(int)
    df = declare(int)
    I = [declare(fixed) for _ in range(len(qub_key_subset))]
    Q = [declare(fixed) for _ in range(len(qub_key_subset))]
    I_st = [declare_stream() for _ in range(len(qub_key_subset))]
    Q_st = [declare_stream() for _ in range(len(qub_key_subset))]

    with for_(*from_array(tau, taus_cycles)):
        with for_(*from_array(df, qub_detune_sweep_dfs)):
            with for_(n, 0, n < n_avg, n + 1):
                for j in range(len(qub_key_subset)): # a real Python for loop so it unravels and executes in parallel, not sequentially
                    update_frequency(qub_key_subset[j], df + qub_IFs[j])
                    ramsey_sequence(tau, qub_key_subset[j])
                    align(qub_key_subset[j], res_key_subset[j]) # Make sure the readout occurs after the pulse to qubit
                    measure(
                        "readout",
                        res_key_subset[j],
                        None, # Warning vs Error depending on version, I'm keeping it
                        dual_demod.full("rotated_cos", "rotated_sin", I[j]),
                        dual_demod.full("rotated_minus_sin", "rotated_cos", Q[j])
                    )
                    save(I[j], I_st[j])
                    save(Q[j], Q_st[j])
                    if multiplexed:
                        wait(res_relaxation, res_key_subset[j])
                        wait(qub_relaxation, qub_key_subset[j]) 
                    else:
                        align() # When python unravels, this makes sure the readouts are sequential
                        if j == len(res_key_subset)-1:
                            wait(res_relaxation, *res_key_subset) # after last resonator, we wait for relaxation
                            wait(qub_relaxation, *qub_key_subset)
        assign(i, i+1)
        save(i, n_st)
    with stream_processing():
        n_st.save("iteration")
        for j in range(len(qub_key_subset)):
            I_st[j].buffer(n_avg).map(FUNCTIONS.average()).buffer(len(qub_detune_sweep_dfs)).buffer(len(taus_cycles)).save("I_"+str(j))
            Q_st[j].buffer(n_avg).map(FUNCTIONS.average()).buffer(len(qub_detune_sweep_dfs)).buffer(len(taus_cycles)).save("Q_"+str(j))


prog = ramsey_chevron_inner_avg
# ---- Open communication with the OPX ---- #
from warsh_credentials import host_ip, cluster
qmm = QuantumMachinesManager(host = host_ip, cluster_name = cluster)

simulate = False
if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=2_000)  # In clock cycles = 4ns
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
    result_names = ["iteration"] + [f"I_{j}" for j in range(len(qub_key_subset))] + [f"Q_{j}" for j in range(len(qub_key_subset))]
    res_handles = fetching_tool(job, data_list = result_names, mode = "live")
    # Plot results
    # Waits (blocks the Python console) until all results have been acquired
    fig = plt.figure()
    interrupt_on_close(fig, job)  #  Interrupts the job when closing the figure
    while res_handles.is_processing():
        iteration, *IQ_data= res_handles.fetch_all()
        # Progress bar
        progress_counter(iteration, len(taus_cycles), start_time=res_handles.get_start_time())
        plt.pause(0.1)
    # Fetch results
    iteration, *IQ_data = res_handles.fetch_all()
    I = np.array([IQ_data[j] for j in range(len(qub_key_subset))])
    Q = np.array([IQ_data[j + len(qub_key_subset)] for j in range(len(qub_key_subset))])
    for j in range(len(qub_key_subset)):
        I[j] = u.demod2volts(I[j], readout_lens[j])
        Q[j] = u.demod2volts(Q[j], readout_lens[j])
    plt.clf()
    n_qubits = len(qub_key_subset)
    fig, axs = plt.subplots(2, n_qubits, figsize=(5 * n_qubits, 8), sharex=False)
    if n_qubits == 1:
        axs = np.array([[axs[0]], [axs[1]]])  # 2D array for single qubit

    for j in range(n_qubits):
        # I
        im0 = axs[0, j].imshow(
        I[j],
        aspect='auto',
        origin='lower',
        extent=[
            qub_detune_sweep_dfs[0] / u.MHz,
            qub_detune_sweep_dfs[-1] / u.MHz,
            taus_effective_ns[0],
            taus_effective_ns[-1]
        ],
        cmap='bwr'
        )
        axs[0, j].set_title(f"I, Qubit {qub_key_subset[j]}")
        axs[0, j].set_ylabel("Wait time (ns)")
        axs[0, j].set_xlabel("Frequency detuning (MHz)")
        plt.colorbar(im0, ax=axs[0, j], label="I")

        # Q
        im1 = axs[1, j].imshow(
        Q[j],
        aspect='auto',
        origin='lower',
        extent=[
            qub_detune_sweep_dfs[0] / u.MHz,
            qub_detune_sweep_dfs[-1] / u.MHz,
            taus_effective_ns[0],
            taus_effective_ns[-1]
        ],
        cmap='bwr'
        )
        axs[1, j].set_title(f"Q, Qubit {qub_key_subset[j]}")
        axs[1, j].set_ylabel("Wait time (ns)")
        axs[1, j].set_xlabel("Frequency detuning (MHz)")
        plt.colorbar(im1, ax=axs[1, j], label="Q")

    plt.tight_layout()
    plt.show(block=False)
    plt.tight_layout()


    qm.close()