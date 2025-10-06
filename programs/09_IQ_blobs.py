import numpy as np
from qm.qua import *
from qm import QuantumMachinesManager
from qualang_tools.loops import from_array
from qualang_tools.results import fetching_tool, progress_counter
from qualang_tools.plot import interrupt_on_close
from qualang_tools.analysis import two_state_discriminator
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

# ---- IQ blobs ---- #
qubit_keys = ["q0", "q1", "q2", "q3"]
qub_key_subset, qub_freq_subset, res_key_subset, res_freq_subset, readout_lens, ge_thresholds, drag_coef_subset,  = multiplexed_parser(qubit_keys, multiplexed_parameters)

with program() as IQ_blobs:
    pd = declare(int)
    n = declare(int)
    n_st = declare_stream()
    I_g = [declare(fixed) for _ in range(len(qub_key_subset))]
    Q_g = [declare(fixed) for _ in range(len(qub_key_subset))]
    I_g_st = [declare_stream() for _ in range(len(qub_key_subset))]
    Q_g_st = [declare_stream() for _ in range(len(qub_key_subset))]
    I_e = [declare(fixed) for _ in range(len(qub_key_subset))]
    Q_e = [declare(fixed) for _ in range(len(qub_key_subset))]
    I_e_st = [declare_stream() for _ in range(len(qub_key_subset))]
    Q_e_st = [declare_stream() for _ in range(len(qub_key_subset))]

    with for_(n, 0, n < n_avg, n + 1):
        for j in range(len(qub_key_subset)): # a real Python for loop so it unravels and executes in parallel, not sequentially
            measure(
                "readout",
                res_key_subset[j],
                None, # Warning vs Error depending on version, I'm keeping it
                dual_demod.full("cos", "sin", I_g[j]),
                dual_demod.full("minus_sin", "cos", Q_g[j])
            )
            save(I_g[j], I_g_st[j])
            save(Q_g[j], Q_g_st[j])
            align(res_key_subset[j], qub_key_subset[j]) 
            wait(qub_relaxation, qub_key_subset[j]) # ensure qubit is in ground state after readout, just in case
            wait(res_relaxation, res_key_subset[j])
            align(res_key_subset[j], qub_key_subset[j]) 
            play(
                "x180", 
                qub_key_subset[j],
            )
            align(qub_key_subset[j], res_key_subset[j]) # Make sure the readout occurs after the pulse to qubit
            measure(
                "readout",
                res_key_subset[j],
                None, # Warning vs Error depending on version, I'm keeping it
                dual_demod.full("cos", "sin", I_e[j]),
                dual_demod.full("minus_sin", "cos", Q_e[j])
            )
            save(I_e[j], I_e_st[j])
            save(Q_e[j], Q_e_st[j])
            if multiplexed:
                wait(res_relaxation, res_key_subset[j])
                wait(qub_relaxation, qub_key_subset[j]) 
            else:
                align() # When python unravels, this makes sure the readouts are sequential
                if j == len(res_key_subset)-1:
                    wait(res_relaxation, *res_key_subset) # after last resonator, we wait for relaxation
                    wait(qub_relaxation, *qub_key_subset)
        save(n, n_st)
    with stream_processing():
        n_st.save("iteration")
        for j in range(len(qub_key_subset)):
            I_g_st[j].save_all("I_g_"+str(j))
            Q_g_st[j].save_all("Q_g_"+str(j))
            I_e_st[j].save_all("I_e_"+str(j))
            Q_e_st[j].save_all("Q_e_"+str(j))

prog = IQ_blobs
# ---- Open communication with the OPX ---- #
from warsh_credentials import host_ip, cluster
qmm = QuantumMachinesManager(host = host_ip, cluster_name = cluster)

simulate = True
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
    result_names = ["iteration"] + [f"I_g_{j}" for j in range(len(qub_key_subset))] + [f"Q_g_{j}" for j in range(len(qub_key_subset))] + [f"I_e_{j}" for j in range(len(qub_key_subset))] + [f"Q_e_{j}" for j in range(len(qub_key_subset))]
    res_handles = fetching_tool(job, data_list = result_names, mode = "wait_for_all")

    iteration, *IQ_data = res_handles.fetch_all()
    I_g = np.array([IQ_data[j] for j in range(len(qub_key_subset))])
    Q_g = np.array([IQ_data[j + len(qub_key_subset)] for j in range(len(qub_key_subset))])
    I_e = np.array([IQ_data[j + 2*len(qub_key_subset)] for j in range(len(qub_key_subset))])
    Q_e = np.array([IQ_data[j + 3*len(qub_key_subset)] for j in range(len(qub_key_subset))])

    for j in range(len(qub_key_subset)):
        angle, threshold, fidelity, gg, ge, eg, ee = two_state_discriminator(I_g[j], Q_g[j], I_e[j], Q_e[j], b_print=True, b_plot=True)
        print(f"Qubit {qub_key_subset[j]}: angle = {angle}, threshold = {threshold}, fidelity = {fidelity}")

    if False:
        # Two-state discriminator using I/Q data
        discriminators = []
        thresholds = []
        for j in range(len(qub_key_subset)):
            # Stack I/Q data for ground and excited states
            ground = np.vstack([I_g[j], Q_g[j]]).T
            excited = np.vstack([I_e[j], Q_e[j]]).T

            # Compute mean of each state
            mean_g = np.mean(ground, axis=0)
            mean_e = np.mean(excited, axis=0)

            # Discrimination axis (unit vector from ground to excited)
            axis = mean_e - mean_g
            axis /= np.linalg.norm(axis)

            # Project all points onto discrimination axis
            proj_g = (ground - mean_g) @ axis
            proj_e = (excited - mean_g) @ axis

            # Threshold: midpoint between projected means
            th = 0.5 * (np.mean(proj_g) + np.mean(proj_e))
            thresholds.append(th)
            discriminators.append(axis)

            # Assign state labels for all points (example: excited=1, ground=0)
            all_proj = np.concatenate([proj_g, proj_e])
            labels = np.concatenate([np.zeros_like(proj_g), np.ones_like(proj_e)])
            pred = (all_proj > th).astype(int)

            # Plot IQ blobs and discrimination axis
            plt.figure()
            plt.scatter(I_g[j], Q_g[j], label="Ground", alpha=0.5)
            plt.scatter(I_e[j], Q_e[j], label="Excited", alpha=0.5)
            # Plot discrimination axis
            x0, y0 = mean_g
            dx, dy = axis * 2  # scale for visualization
            #plt.arrow(x0, y0, dx, dy, head_width=0.05, head_length=0.1, fc='k', ec='k')
            plt.xlabel("I")
            plt.ylabel("Q")
            plt.title(f"Qubit {qub_key_subset[j]} IQ Blobs and Discriminator")
            plt.legend()
            plt.grid(True)
            plt.show()

        