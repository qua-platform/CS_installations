import numpy as np
from qm.qua import *
from qm import QuantumMachinesManager
from qualang_tools.loops import from_array
from qm_saas import QmSaas, QOPVersion
from qm import SimulationConfig
import matplotlib.pyplot as plt
from pathlib import Path
from scipy.signal import savgol_filter
from qualang_tools.units import unit
u = unit(coerce_to_integer=True)
from macros import multiplexed_parser

if False:
    from configurations.DA_5Q.OPX1000config import *
else:
    from configurations.DB_6Q.OPX1000config import *

# ---- Multiplex parameters ---- #

qubit_keys = ["q0", "q1", "q2"]
required_parameters = ["qubit_key", "qubit_relaxation", "resonator_key", "resonator_relaxation"]
qub_key_subset, qubit_relaxation, res_key_subset, resonator_relaxation = multiplexed_parser(qubit_keys, multiplexed_parameters.copy(), required_parameters)
funnyWaits = [20, 40, 80]
# ---- Program parameters ---- #
n_avg = 200
qub_relaxation = qubit_relaxation//4 # From ns to clock cycles
res_relaxation = resonator_relaxation//4 # From ns to clock cycles

with program() as hello_qua:
    n = declare(int)
    chirp_rate = declare(int, value = [1_000_000, -1_000_000, 500_000, 500_000])
    #ind = [declare(int) for _ in range(len(qub_key_subset))]
    ind=declare(int)

    with for_(n, 0, n < n_avg, n + 1): 
        for j in range(len(qub_key_subset)):
            with for_(ind, 16, ind < 1024, ind + 32):
                wait(ind, qub_key_subset[j])
                play("x180", qub_key_subset[j])

prog = hello_qua
# ---- Open communication with the OPX ---- #
from warsh_credentials import host_ip, cluster
qmm = QuantumMachinesManager(host = host_ip, cluster_name = cluster)

simulate = True
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
    res_handles = job.result_handles
    # Waits (blocks the Python console) until all results have been acquired
    res_handles.wait_for_all_values()
    qm.close()

    # ---- Analysis ---- #
    adc = u.raw2volts(res_handles.get("adc").fetch_all())
    # Filter the data to get the pulse arrival time
    signal = savgol_filter(np.abs(adc), 11, 3)
    thresh = (np.mean(signal[:100]) + np.mean(signal[:-100])) / 2
    delay = np.where(signal > thresh)[0][0]
    delay = np.round(delay / 4) * 4  # Find the closest multiple integer of 4ns

    fig = plt.figure()
    plt.title("Averaged run")
    plt.plot(adc.real, "b", label="I")
    plt.plot(adc.imag, "r", label="Q")
    plt.axvline(delay, color="k", linestyle="--", label="ToF")
    plt.xlabel("Time (ns)")
    plt.legend()
    plt.tight_layout()
    plt.show()

    # Update the config
    print(f"Set time of flight to {time_of_flight + delay} ns")
