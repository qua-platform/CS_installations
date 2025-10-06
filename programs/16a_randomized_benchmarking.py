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
from qualang_tools.bakery.randomized_benchmark_c1 import c1_table
from scipy.optimize import curve_fit

from macros import multiplexed_parser, simple_two_state_discriminator, readout_macro


if False:
    from configurations.OPX1000config_DA_5Q import *
else:
    from configurations.OPX1000config_DB_6Q import *

inv_gates = [int(np.where(c1_table[i, :] == 0)[0][0]) for i in range(24)]
seed = 42

def play_RB_sequence_V1(sequence_indices, sequence_length, qub_key, x180_len):
    with for_(m, 0, m < sequence_length, m + 1): # playing out the sequency of cliffords
        assign(i, sequence_indices[m])
        with if_(i == 0):
            wait(x180_len//4, qub_key)
        with elif_(i == 1):
            play("x180", qub_key)
        with elif_(i == 2):
            play("y180", qub_key)
        with elif_(i == 3):
            play("y180", qub_key)
            play("x180", qub_key)
        with elif_(i == 4):
            play("x90", qub_key)
            play("y90", qub_key)
        with elif_(i == 5):
            play("x90", qub_key)
            play("-y90", qub_key)
        with elif_(i == 6):
            play("-x90", qub_key)
            play("y90", qub_key)
        with elif_(i == 7):
            play("-x90", qub_key)
            play("-y90", qub_key)
        with elif_(i == 8):
            play("y90", qub_key)
            play("x90", qub_key)
        with elif_(i == 9):
            play("y90", qub_key)
            play("-x90", qub_key)
        with elif_(i == 10):
            play("-y90", qub_key)
            play("x90", qub_key)
        with elif_(i == 11):
            play("-y90", qub_key)
            play("-x90", qub_key)
        with elif_(i == 12):
            play("x90", qub_key)
        with elif_(i == 13):
            play("-x90", qub_key)
        with elif_(i == 14):
            play("y90", qub_key)
        with elif_(i == 15):
            play("-y90", qub_key)
        with elif_(i == 16):
            play("-x90", qub_key)
            play("y90", qub_key)
            play("x90", qub_key)
        with elif_(i == 17):
            play("-x90", qub_key)
            play("-y90", qub_key)
            play("x90", qub_key)
        with elif_(i == 18):
            play("x180", qub_key)
            play("y90", qub_key)
        with elif_(i == 19):
            play("x180", qub_key)
            play("-y90", qub_key)
        with elif_(i == 20):
            play("y180", qub_key)
            play("x90", qub_key)
        with elif_(i == 21):
            play("y180", qub_key)
            play("-x90", qub_key)
        with elif_(i == 22):
            play("x90", qub_key)
            play("y90", qub_key)
            play("x90", qub_key)
        with elif_(i == 23):
            play("-x90", qub_key)
            play("y90", qub_key)
            play("-x90", qub_key)

def play_RB_sequence(sequence_indices, sequence_length, qub_key, x180_len):
    with for_(i, 0, i < sequence_length, i + 1): # playing out the sequency of cliffords
        with switch_(sequence_indices[i], unsafe = True):
            with case_(0):
                wait(x180_len//4, qub_key)
            with case_(1):
                play("x180", qub_key)
            with case_(2):
                play("y180", qub_key)
            with case_(3):
                play("y180", qub_key)
                play("x180", qub_key)
            with case_(4):
                play("x90", qub_key)
                play("y90", qub_key)
            with case_(5):
                play("x90", qub_key)
                play("-y90", qub_key)
            with case_(6):
                play("-x90", qub_key)
                play("y90", qub_key)
            with case_(7):
                play("-x90", qub_key)
                play("-y90", qub_key)
            with case_(8):
                play("y90", qub_key)
                play("x90", qub_key)
            with case_(9):
                play("y90", qub_key)
                play("-x90", qub_key)
            with case_(10):
                play("-y90", qub_key)
                play("x90", qub_key)
            with case_(11):
                play("-y90", qub_key)
                play("-x90", qub_key)
            with case_(12):
                play("x90", qub_key)
            with case_(13):
                play("-x90", qub_key)
            with case_(14):
                play("y90", qub_key)
            with case_(15):
                play("-y90", qub_key)
            with case_(16):
                play("-x90", qub_key)
                play("y90", qub_key)
                play("x90", qub_key)
            with case_(17):
                play("-x90", qub_key)
                play("-y90", qub_key)
                play("x90", qub_key)
            with case_(18):
                play("x180", qub_key)
                play("y90", qub_key)
            with case_(19):
                play("x180", qub_key)
                play("-y90", qub_key)
            with case_(20):
                play("y180", qub_key)
                play("x90", qub_key)
            with case_(21):
                play("y180", qub_key)
                play("-x90", qub_key)
            with case_(22):
                play("x90", qub_key)
                play("y90", qub_key)
                play("x90", qub_key)
            with case_(23):
                play("-x90", qub_key)
                play("y90", qub_key)
                play("-x90", qub_key)

def power_law(power, a, b, p):
    return a * (p**power) + b

def generate_RB_sequence(max_depth):
    '''
    Lets do some thinking here huh.
    This version is pretty much ripped straight from qua-libs to ensure everything else is working (strict timing was a learning curve).
    '''
    cayley = declare(int, value=c1_table.flatten().tolist())
    inv_list = declare(int, value=inv_gates)
    current_state = declare(int)
    step = declare(int)
    sequence = declare(int, size=max_depth + 1)
    inv_gate = declare(int, size=max_depth + 1)
    i = declare(int)
    rand = Random(seed=seed)

    assign(current_state, 0)
    with for_(i, 0, i < max_depth, i + 1):
        assign(step, rand.rand_int(24))
        assign(current_state, cayley[current_state * 24 + step])
        assign(sequence[i], step)
        assign(inv_gate[i], inv_list[current_state])

    return sequence, inv_gate

# ---- Multiplexed program parameters ---- #
multiplexed = True
qubit_keys = ["q0", "q1", "q2", "q3"]
required_parameters = ["qubit_key", "qubit_frequency", "qubit_relaxation", "resonator_key", "readout_len", "resonator_relaxation", "ge_threshold", "x180_len"]
qub_key_subset, qub_frequency, qubit_relaxation, res_key_subset, readout_len, resonator_relaxation, ge_threshold, x180_len = multiplexed_parser(qubit_keys, multiplexed_parameters.copy(), required_parameters)


# ---- RB program parameters ---- #
qub_relaxation = qubit_relaxation//4 # From ns to clock cycles
res_relaxation = resonator_relaxation//4 # From ns to clock cycles
max_depth = 10
m_avg = 8 # number of sequences at each depth
n_avg = 100 # number of averages for each sequence

with program() as randomized_benchmarking:
    m = declare(int) # how many sequencies at a depth
    n = declare(int) # for averaging on a single set of cliffords
    i = declare(int) # operation index
    d = declare(int) # depth counter
    n_st = declare_stream()

    I = [declare(fixed) for _ in range(len(qub_key_subset))]
    Q = [declare(fixed) for _ in range(len(qub_key_subset))]
    #I_st = [declare_stream() for _ in range(len(qub_key_subset))]
    #Q_st = [declare_stream() for _ in range(len(qub_key_subset))]
    state = [declare(int) for _ in range(len(qub_key_subset))]
    state_st = [declare_stream() for _ in range(len(qub_key_subset))]

    with for_(n, 0, n < n_avg, n + 1): # looping over number of sequences at each depth
        with for_(d, 1, d <= max_depth, d + 1): # looping over the different sequence depths
                sequence_indices, invert_gate_index = generate_RB_sequence(max_depth)
                with for_(m, 0, m < m_avg, m + 1):
                    for j in range(len(qub_key_subset)): 
                        with strict_timing_():
                            play_RB_sequence(sequence_indices, d, qub_key_subset[j], x180_len[j])
                        align(res_key_subset[j], qub_key_subset[j])
                        measure(
                            "readout",
                            res_key_subset[j],
                            None, # Warning vs Error depending on version, I'm keeping it
                            dual_demod.full("opt_cos", "opt_sin", I[j]),
                            dual_demod.full("opt_minus_sin", "opt_cos", Q[j])
                        )
                        state[j], I[j], Q[j] = readout_macro(res_key_subset[j], I[j], Q[j], state[j], threshold=ge_threshold[j])
                        #save(I[j], I_st[j])
                        #save(Q[j], Q_st[j])
                        save(state[j], state_st[j])
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
            #I_st[j].buffer(n_avg).map(FUNCTIONS.average()).buffer(m_avg).map(FUNCTIONS.average()).buffer(max_depth).save("I_"+str(j))
            #Q_st[j].buffer(n_avg).map(FUNCTIONS.average()).buffer(m_avg).map(FUNCTIONS.average()).buffer(max_depth).save("Q_"+str(j))
            state_st[j].buffer(m_avg).map(FUNCTIONS.average()).buffer(max_depth).buffer(n_avg).save("state_"+str(j))
            state_st[j].buffer(m_avg).map(FUNCTIONS.average()).buffer(max_depth).average().save("state_avg_"+str(j))

prog = randomized_benchmarking
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
    result_names = ["iteration"] + [f"state_avg_{j}" for j in range(len(qub_key_subset))]
    res_handles = fetching_tool(job, data_list = result_names, mode = "live")
    # Waits (blocks the Python console) until all results have been acquired
    fig = plt.figure()
    interrupt_on_close(fig, job)  #  Interrupts the job when closing the figure
    xPlot = np.arange(1, max_depth+1)
    # Stolen from the library, I was getting stuck on strict timing stuff:
    while res_handles.is_processing():
        # Fetch results
        iteration, *data = res_handles.fetch_all()
        state_avg = np.array([data[j] for j in range(len(qub_key_subset))])
        # Progress bar
        progress_counter(iteration, n_avg, start_time=res_handles.get_start_time())
        # Plot results
        plt.cla()
        for i in range(len(qub_key_subset)):
            plt.plot(xPlot, state_avg[i], marker=".")
        plt.xlabel("Number of Clifford gates")
        plt.ylabel("Sequence Fidelity")
        plt.title("Single qubit RB")
        plt.pause(0.1)
    
    
    result_names = [f"state_{j}" for j in range(len(qub_key_subset))]
    res_handles = fetching_tool(job, data_list = result_names)
    state_data = res_handles.fetch_all()
    state_avg = np.mean(state_data, axis = 1)
    error_avg = np.std(state_data, axis = 1)/np.sqrt(n_avg)

    for j in range(len(qub_key_subset)):
        pars, cov = curve_fit(
            f=power_law,
            xdata=xPlot,
            ydata=state_avg[j],
            p0=[0.5, 0.5, 0.9],
            bounds=(-np.inf, np.inf),
            maxfev=2000,
        )
        stdevs = np.sqrt(np.diag(cov))

        print("#########################")
        print("### Fitted Parameters ###")
        print("#########################")
        print(f"A = {pars[0]:.3} ({stdevs[0]:.1}), B = {pars[1]:.3} ({stdevs[1]:.1}), p = {pars[2]:.3} ({stdevs[2]:.1})")
        print("Covariance Matrix")
        print(cov)

        one_minus_p = 1 - pars[2]
        r_c = one_minus_p * (1 - 1 / 2**1)
        r_g = r_c / 1.875  # 1.875 is the average number of gates in clifford operation
        r_c_std = stdevs[2] * (1 - 1 / 2**1)
        r_g_std = r_c_std / 1.875

        print("#########################")
        print("### Useful Parameters ###")
        print("#########################")
        print(
            f"Error rate: 1-p = {np.format_float_scientific(one_minus_p, precision=2)} ({stdevs[2]:.1})\n"
            f"Clifford set infidelity: r_c = {np.format_float_scientific(r_c, precision=2)} ({r_c_std:.1})\n"
            f"Gate infidelity: r_g = {np.format_float_scientific(r_g, precision=2)}  ({r_g_std:.1})"
        )

        # Plots
        plt.figure()
        plt.errorbar(xPlot, state_avg[j], yerr=error_avg[j], marker=".")
        plt.plot(xPlot, power_law(xPlot, *pars), linestyle="--", linewidth=2)
        plt.xlabel("Number of Clifford gates")
        plt.ylabel("Sequence Fidelity")
        plt.title(f"Qubit {qub_key_subset[j]}, Single qubit RB")

    qm.close()