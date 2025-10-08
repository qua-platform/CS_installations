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
qubit_keys = ["q0", "q1", "q2", "q3"]
required_parameters = ["qubit_key", "qubit_frequency", "qubit_relaxation", "qubit_LO", "resonator_key", "readout_len", "resonator_relaxation"]
qub_key_subset, qub_frequency, qubit_relaxation, qubit_LO, res_key_subset, readout_len, resonator_relaxation = multiplexed_parser(qubit_keys, multiplexed_parameters.copy(), required_parameters)


# ---- Amplitude Rabi Chevron Multiplexed ---- #
qub_relaxation = qubit_relaxation//4 # From ns to clock cycles
res_relaxation = resonator_relaxation//4 # From ns to clock cycles

qub_IFs = qub_frequency - qubit_LO
qub_spec_span = 20 * u.MHz
qub_spec_df = 2 * u.MHz
qub_spec_sweep_dfs = np.arange(-qub_spec_span, qub_spec_span + qub_spec_df, qub_spec_df)
qub_spec_frequencies = np.array([qub_spec_sweep_dfs + guess for guess in qub_frequency])

pulse_amp_min = 0.1 # ratio of max amplitude 
pulse_amp_max = 1.0 # ratio of max amplitude 
pulse_amp_damp = 0.1 # step in ratio of max amplitude 
pulse_amps = np.arange(pulse_amp_min, pulse_amp_max + pulse_amp_damp, pulse_amp_damp) 

with program() as amplitude_rabi_chevron_multiplexed:
    n = declare(int)
    n_st = declare_stream()
    a = declare(fixed)
    df = declare(int)
    I = [declare(fixed) for _ in range(len(qub_key_subset))]
    Q = [declare(fixed) for _ in range(len(qub_key_subset))]
    I_st = [declare_stream() for _ in range(len(qub_key_subset))]
    Q_st = [declare_stream() for _ in range(len(qub_key_subset))]

    with for_(n, 0, n < n_avg, n + 1):
        with for_(*from_array(a, pulse_amps)):
            with for_(*from_array(df, qub_spec_sweep_dfs)):
                for j in range(len(qub_key_subset)): # a real Python for loop so it unravels and executes in parallel, not sequentially
                    update_frequency(qub_key_subset[j], df + qub_IFs[j])
                    play(
                        "x180" * amp(a), 
                        qub_key_subset[j], 
                    )
                    align(qub_key_subset[j], res_key_subset[j]) # Make sure the readout occurs after the pulse to qubit
                    measure(
                        "readout",
                        res_key_subset[j],
                        dual_demod.full("cos", "sin", I[j]),
                        dual_demod.full("minus_sin", "cos", Q[j])
                    )
                    save(I[j], I_st[j])
                    save(Q[j], Q_st[j])
                    if multiplexed:
                        wait(res_relaxation[j], res_key_subset[j])
                        wait(qub_relaxation[j], qub_key_subset[j]) 
                    else:
                        align() # When python unravels, this makes sure the readouts are sequential
                        if j == len(res_key_subset)-1:
                            wait(np.max(res_relaxation), *res_key_subset) 
                            wait(np.max(qub_relaxation), *qub_key_subset)
        save(n, n_st)
    with stream_processing():
        n_st.save("iteration")
        for j in range(len(qub_key_subset)):
            I_st[j].buffer(len(qub_spec_sweep_dfs)).buffer(len(pulse_amps)).average().save("I_"+str(j))
            Q_st[j].buffer(len(qub_spec_sweep_dfs)).buffer(len(pulse_amps)).average().save("Q_"+str(j))

prog = amplitude_rabi_chevron_multiplexed
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
    # Waits (blocks the Python console) until all results have been acquired
    fig = plt.figure()
    interrupt_on_close(fig, job)  #  Interrupts the job when closing the figure
    while res_handles.is_processing():
        # Fetch results
        iteration, *IQ_data = res_handles.fetch_all()
        I = np.array([IQ_data[j] for j in range(len(qub_key_subset))])
        Q = np.array([IQ_data[j + len(qub_key_subset)] for j in range(len(qub_key_subset))])
        for j in range(len(qub_key_subset)):
            I[j] = u.demod2volts(I[j], readout_len[j])
            Q[j] = u.demod2volts(Q[j], readout_len[j])
        S = I + 1j * Q
        R = np.abs(S)  # Amplitude
        phase = np.angle(S)  # Phase
        # Progress bar
        progress_counter(iteration, n_avg, start_time=res_handles.get_start_time())
        # Plot results
        plt.clf()
        n_qubits = len(qub_key_subset)
        fig, axs = plt.subplots(2, n_qubits, figsize=(5 * n_qubits, 8), sharex=False)
        if n_qubits == 1:
            axs = np.array([[axs[0]], [axs[1]]])  # Ensure 2D array for single qubit

        for j in range(n_qubits):
            # R
            im0 = axs[0, j].imshow(
            R[j],
            aspect='auto',
            origin='lower',
            extent=[
                qub_spec_sweep_dfs[0] / u.MHz,
                qub_spec_sweep_dfs[-1] / u.MHz,
                pulse_amps[0] - pulse_amp_damp/2,
                pulse_amps[-1] + pulse_amp_damp/2
            ],
            cmap='bwr'
            )
            axs[0, j].set_title(f"Amplitude, Qubit {qub_key_subset[j]}")
            axs[0, j].set_ylabel("Pulse amplitude (ratio of x180_amp)")
            axs[0, j].set_xlabel("Frequency detuning (MHz)")
            plt.colorbar(im0, ax=axs[0, j], label="R (V)")

            # Phase
            im1 = axs[1, j].imshow(
            phase[j],
            aspect='auto',
            origin='lower',
            extent=[
                qub_spec_sweep_dfs[0] / u.MHz,
                qub_spec_sweep_dfs[-1] / u.MHz,
                pulse_amps[0] - pulse_amp_damp/2,
                pulse_amps[-1] + pulse_amp_damp/2
            ],
            cmap='bwr'
            )
            axs[1, j].set_title(f"Phase, Qubit {qub_key_subset[j]}")
            axs[1, j].set_ylabel("Pulse amplitude (ratio of x180_amp)")
            axs[1, j].set_xlabel("Frequency detuning (MHz)")
            plt.colorbar(im1, ax=axs[1, j], label="Phase (rad)")

        plt.tight_layout()
        plt.show(block=False)
        plt.pause(0.1)
        plt.tight_layout()

    qm.close()