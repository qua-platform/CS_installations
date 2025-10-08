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

# ---- Multiplexed program parameters ---- #
n_avg = 1000
multiplexed = True
qubit_keys = ["q0", "q1", "q2", "q3"]
required_parameters = ["qubit_key", "qubit_frequency", "qubit_relaxation", "resonator_key", "readout_len", "resonator_relaxation"]
qub_key_subset, qub_frequency, qubit_relaxation, res_key_subset, readout_len, resonator_relaxation = multiplexed_parser(qubit_keys, multiplexed_parameters.copy(), required_parameters)
qub_relaxation = qubit_relaxation//4 # From ns to clock cycles
res_relaxation = resonator_relaxation//4 # From ns to clock cycles

# ---- T1 ---- #
tau_min = 0 # ns
tau_max = 16000 # ns
dtau = 64 # ns
taus_ns = np.arange(tau_min, tau_max + dtau, dtau)
taus_cycles = taus_ns // 4 # Converted to clock cycles
taus_effective_ns = taus_ns + 16 # accounting for the 4 cycles of align (there is probably more, but I'll test later)

with program() as measure_T1:
    n = declare(int)
    n_st = declare_stream()
    tau = declare(int)
    I = [declare(fixed) for _ in range(len(qub_key_subset))]
    Q = [declare(fixed) for _ in range(len(qub_key_subset))]
    I_st = [declare_stream() for _ in range(len(qub_key_subset))]
    Q_st = [declare_stream() for _ in range(len(qub_key_subset))]

    with for_(n, 0, n < n_avg, n + 1):
        with for_(*from_array(tau, taus_cycles)):
            for j in range(len(qub_key_subset)): # a real Python for loop so it unravels and executes in parallel, not sequentially
                with if_(tau >= 4):
                    play(
                        "x180", 
                        qub_key_subset[j], 
                    )
                    wait(tau, qub_key_subset[j])
                with else_():
                    play(
                        "x180", 
                        qub_key_subset[j], 
                    )
                align(qub_key_subset[j], res_key_subset[j]) 
                measure(
                    "readout",
                    res_key_subset[j],
                    dual_demod.full("rotated_cos", "rotated_sin", I[j]),
                    dual_demod.full("rotated_minus_sin", "rotated_cos", Q[j])
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
            I_st[j].buffer(len(taus_cycles)).average().save("I_"+str(j))
            Q_st[j].buffer(len(taus_cycles)).average().save("Q_"+str(j))

prog = measure_T1
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
        # Progress bar
        progress_counter(iteration, n_avg, start_time=res_handles.get_start_time())
        # Plot results
        plt.suptitle(f"Measure T1")
        ax1 = plt.subplot(211)
        plt.cla()
        for j in range(len(qub_key_subset)):
            plt.plot(taus_effective_ns, I[j], label=f"Qubit {qub_key_subset[j]}")
        plt.ylabel("I quadrature (V)")
        plt.subplot(212, sharex=ax1)
        plt.cla()
        for j in range(len(qub_key_subset)):
            plt.plot(taus_effective_ns, Q[j], label=f"Qubit {qub_key_subset[j]}")
        plt.xlabel("Measure delay (ns)")
        plt.ylabel("Q quadrature (V)")
        plt.pause(0.1)
        plt.tight_layout()
    
    from qualang_tools.plot.fitting import Fit

    for j in range(len(qub_key_subset)):
        try:
            # Fit the data
            fit = Fit()
            plt.figure()
            T1_fit = fit.T1(taus_effective_ns, I[j], plot=True)
            plt.title(f"Measure T1, Qubit {qub_key_subset[j]}")
            plt.xlabel("Measure delay (ns)")
            plt.ylabel("I quadrature (V)")
            print(f"Qubit {qub_key_subset[j]}, T1 = {1 / T1_fit['f'][0]:.1f} ns ")
        except (Exception,):
            plt.figure()
            plt.plot(taus_effective_ns, I[j])
            plt.title(f"Measure T1, Qubit {qub_key_subset[j]}")
            plt.xlabel("Measure delay (ns)")
            plt.ylabel("I quadrature (V)")
            print("Unable to fit qubit " + str(qub_key_subset[j]))

    qm.close()