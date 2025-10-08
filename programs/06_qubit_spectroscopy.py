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

if True:
    from configurations.OPX1000config_DA_5Q import *
else:
    from configurations.OPX1000config_DB_6Q import *

# ---- Multiplexed program parameters ---- #
n_avg = 1000
multiplexed = True
qubit_keys = ["q0", "q1", "q2", "q3"]
required_parameters = ["qubit_key", "qubit_frequency", "qubit_relaxation", "qubit_LO", "resonator_key", "readout_len", "resonator_relaxation"]
qub_key_subset, qub_frequency, qubit_relaxation, qubit_LO, res_key_subset, readout_len, resonator_relaxation = multiplexed_parser(qubit_keys, multiplexed_parameters.copy(), required_parameters)

# ---- Qubit Spectroscopy ---- #
res_relaxation = resonator_relaxation//4 # From ns to clock cycles
qub_relaxation = qubit_relaxation//4 # From ns to clock cycles

qub_IF_guesses = qub_frequency - qubit_LO
qub_spec_span = 80 * u.MHz
qub_spec_df = 5 * u.MHz
qub_spec_sweep_dfs = np.arange(-qub_spec_span, qub_spec_span + qub_spec_df, qub_spec_df)
qub_spec_frequencies = np.array([qub_spec_sweep_dfs + guess for guess in qub_frequency])


with program() as qubit_spec_multiplexed:
    n = declare(int)
    n_st = declare_stream()
    df = declare(int)
    I = [declare(fixed) for _ in range(len(qub_key_subset))]
    Q = [declare(fixed) for _ in range(len(qub_key_subset))]
    I_st = [declare_stream() for _ in range(len(qub_key_subset))]
    Q_st = [declare_stream() for _ in range(len(qub_key_subset))]

    with for_(n, 0, n < n_avg, n + 1):
        with for_(*from_array(df, qub_spec_sweep_dfs)):
            for j in range(len(qub_key_subset)): # A Python for loop so it unravels and executes in parallel, not sequentially
                update_frequency(qub_key_subset[j], df + qub_IF_guesses[j])
                play("saturation", qub_key_subset[j])
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
            I_st[j].buffer(len(qub_spec_sweep_dfs)).average().save("I_"+str(j))
            Q_st[j].buffer(len(qub_spec_sweep_dfs)).average().save("Q_"+str(j))

prog = qubit_spec_multiplexed
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
        # Convert results into Volts
        for j in range(len(qub_key_subset)):
            I[j] = u.demod2volts(I[j], readout_len[j])
            Q[j] = u.demod2volts(Q[j], readout_len[j])
        S = I + 1j * Q
        R = np.abs(S)  # Amplitude
        phase = np.angle(S)  # Phase
        # Progress bar
        progress_counter(iteration, n_avg, start_time=res_handles.get_start_time())
        # Plot results
        plt.suptitle(f"Qubit spectroscopy - LO = {qubit_LO / u.GHz} GHz")
        ax1 = plt.subplot(211)
        plt.cla()
        for j in range(len(qub_key_subset)):
            plt.plot((qub_spec_frequencies[j] - qubit_LO) / u.MHz, R[j], label=f"Qubit {qub_key_subset[j]} at {qub_frequency[j]/u.GHz:.3f} GHz")
        plt.ylabel(r"$R=\sqrt{I^2 + Q^2}$ (V)")
        plt.subplot(212, sharex=ax1)
        plt.cla()
        for j in range(len(qub_key_subset)):
            plt.plot((qub_spec_frequencies[j] - qubit_LO) / u.MHz, signal.detrend(np.unwrap(phase[j])), label=f"Qubit {qub_key_subset[j]} at {qub_frequency[j]/u.GHz:.3f} GHz")
        plt.xlabel("Intermediate frequency (MHz)")
        plt.ylabel("Phase (rad)")
        plt.pause(0.1)
        plt.tight_layout()
    
    from qualang_tools.plot.fitting import Fit

    for j in range(len(qub_key_subset)):
        try:
            # Fit the data
            fit = Fit()
            plt.figure()
            spec_fit = fit.reflection_resonator_spectroscopy( (qub_spec_frequencies[j] - qubit_LO) / u.MHz, R[j], plot=True) # I am using the opposite of what I used for resonator fit as a rough estimate for the qubit spectroscopy
            plt.title(f"Qubit {qub_key_subset[j]}, Qubit spectroscopy - LO = {qubit_LO / u.GHz} GHz")
            plt.xlabel("Intermediate frequency (MHz)")
            plt.ylabel(r"R=$\sqrt{I^2 + Q^2}$ (V)")
            print(f"Update qubit {qub_key_subset[j]} IF to {spec_fit['f'][0]:.6f} MHz")
        except (Exception,):
            print("Unable to fit qubit " + str(qub_key_subset[j]))
            plt.figure()
            plt.plot((qub_spec_frequencies[j] - qubit_LO) / u.MHz, R[j])
            plt.title(f"Qubit {qub_key_subset[j]}, Qubit spectroscopy - LO = {qubit_LO / u.GHz} GHz")
            plt.xlabel("Intermediate frequency (MHz)")
            plt.ylabel(r"R=$\sqrt{I^2 + Q^2}$ (V)")

    qm.close()