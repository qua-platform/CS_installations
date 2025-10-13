"""
        IQ BLOBS
This sequence involves measuring the state of the resonator 'N' times, first after thermalization (with the qubit
in the |g> state) and then after applying a pi pulse to the qubit (bringing the qubit to the |e> state) successively.
The resulting IQ blobs are displayed, and the data is processed to determine:
    - The rotation angle required for the integration weights, ensuring that the separation between |g> and |e> states
      aligns with the 'I' quadrature.
    - The threshold along the 'I' quadrature for effective qubit state discrimination.
    - The readout fidelity matrix, which is also influenced by the pi pulse fidelity.

Prerequisites:
    - Having found the resonance frequency of the resonator coupled to the qubit under study (resonator_spectroscopy).
    - Having calibrated qubit pi pulse (x180) by running qubit, spectroscopy, rabi_chevron, power_rabi and updated the config.

Next steps before going to the next node:
    - Update the rotation angle (rotation_angle) in the configuration.
    - Update the g -> e threshold (ge_threshold) in the configuration.
"""
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
from qualang_tools.results.data_handler import DataHandler
from macros import multiplexed_parser, mp_result_names, mp_fetch_all

# ---- Choose which device configuration ---- #
if False:
    from configurations.DA_5Q.OPX1000config import *
else:
    from configurations.DB_6Q.OPX1000config import *

# ---- Multiplexed program parameters ----
n_avg = 1000
multiplexed = True
qubit_keys = ["q0", "q1", "q2", "q3"]
required_parameters = ["qubit_key", "qubit_frequency", "qubit_relaxation", "resonator_key", "readout_len", "resonator_relaxation"]
qub_key_subset, qub_frequency, qubit_relaxation, res_key_subset, readout_len, resonator_relaxation = multiplexed_parser(qubit_keys, multiplexed_parameters.copy(), required_parameters)

# ---- IQ blobs ---- #
qub_relaxation = qubit_relaxation//4 # From ns to clock cycles
res_relaxation = resonator_relaxation//4 # From ns to clock cycles

# ---- Data to save ---- #
save_data_dict = {
    "qubit_keys": qub_key_subset,
    "n_avg": n_avg,
    "config": config,
}
save_dir = Path(__file__).resolve().parent / "data"

# ---- IQ blobs QUA program ---- #
with program() as IQ_blobs:
    pd = declare(int) # QUA variable for the pulse duration
    n = declare(int) # QUA variable for the averaging loop
    n_st = declare_stream() # Stream for the averaging iteration 'n'
    # Ground state measurements
    I_g = [declare(fixed) for _ in range(len(qub_key_subset))] # I_g QUA variable for each qubit
    Q_g = [declare(fixed) for _ in range(len(qub_key_subset))] # Q_g QUA variable for each qubit
    I_g_st = [declare_stream() for _ in range(len(qub_key_subset))]
    Q_g_st = [declare_stream() for _ in range(len(qub_key_subset))]
    # Excited state measurements
    I_e = [declare(fixed) for _ in range(len(qub_key_subset))] # I_e QUA variable for each qubit
    Q_e = [declare(fixed) for _ in range(len(qub_key_subset))] # Q_e QUA variable for each qubit
    I_e_st = [declare_stream() for _ in range(len(qub_key_subset))]
    Q_e_st = [declare_stream() for _ in range(len(qub_key_subset))]

    with for_(n, 0, n < n_avg, n + 1):
        for j in range(len(qub_key_subset)): # a real Python for loop so it unravels and executes in parallel, not sequentially
            measure(
                "readout",
                res_key_subset[j],
                dual_demod.full("cos", "sin", I_g[j]),
                dual_demod.full("minus_sin", "cos", Q_g[j])
            ) # Measure the resonator with the qubit in ground state
            save(I_g[j], I_g_st[j])
            save(Q_g[j], Q_g_st[j])
            align(res_key_subset[j], qub_key_subset[j]) 
            wait(qub_relaxation[j], qub_key_subset[j]) # Ensure qubit is in ground state after readout pulse
            wait(res_relaxation[j], res_key_subset[j])
            align(res_key_subset[j], qub_key_subset[j]) 
            play(
                "x180", 
                qub_key_subset[j],
            ) # Bring the qubit to the excited state
            align(qub_key_subset[j], res_key_subset[j]) # Make sure the readout occurs after the pulse to qubit
            measure(
                "readout",
                res_key_subset[j],
                dual_demod.full("cos", "sin", I_e[j]),
                dual_demod.full("minus_sin", "cos", Q_e[j])
            ) # Measure the resonator with the qubit in excited state
            save(I_e[j], I_e_st[j])
            save(Q_e[j], Q_e_st[j])
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
            I_g_st[j].save_all("I_g_"+str(j))
            Q_g_st[j].save_all("Q_g_"+str(j))
            I_e_st[j].save_all("I_e_"+str(j))
            Q_e_st[j].save_all("Q_e_"+str(j))

prog = IQ_blobs
# ---- Open communication with the OPX ---- #
from opx_credentials import qop_ip, cluster
qmm = QuantumMachinesManager(host=qop_ip, cluster_name=cluster)

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
    result_names = mp_result_names(qub_key_subset, single_tags = ["iteration"], mp_tags = ["I_g", "Q_g", "I_e", "Q_e"])
    res_handles = fetching_tool(job, data_list = result_names, mode = "wait_for_all")

    iteration, I_g, Q_g, I_e, Q_e = mp_fetch_all(res_handles, qub_key_subset, num_single_tags=1)

    
    for j in range(len(qub_key_subset)):
        angle, threshold, fidelity, gg, ge, eg, ee = two_state_discriminator(I_g[j], Q_g[j], I_e[j], Q_e[j], b_print=True, b_plot=True)
        print(f"Qubit {qub_key_subset[j]}: angle = {angle}, threshold = {threshold}, fidelity = {fidelity}")

    qubit_results = {}
    for j in range(len(qub_key_subset)):
        angle, threshold, fidelity, gg, ge, eg, ee = two_state_discriminator(I_g[j], Q_g[j], I_e[j], Q_e[j], b_print=True, b_plot=True)
        print(f"Qubit {qub_key_subset[j]}: angle = {angle}, threshold = {threshold}, fidelity = {fidelity}")
        qubit_results[qub_key_subset[j]] = {
            "angle": angle,
            "threshold": threshold,
            "fidelity": fidelity,
            "matrix": np.array([[gg, ge], [eg, ee]])
        }

    # Save results
    script_name = Path(__file__).name
    data_handler = DataHandler(root_data_folder=save_dir)
    save_data_dict.update({"I_e_data": I_e})
    save_data_dict.update({"Q_e_data": Q_e})
    save_data_dict.update({"I_g_data": I_g})
    save_data_dict.update({"Q_g_data": Q_g})
    save_data_dict.update({"discriminator_results": qubit_results})
    data_handler.additional_files = {script_name: script_name, **default_additional_files}
    data_handler.save_data(data=save_data_dict, name="_".join(script_name.split("_")[1:]).split(".")[0])
    
    qm.close()
        