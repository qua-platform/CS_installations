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

# ---- Determine which device to run from ---- #
if False: 
    from configurations.DA_5Q.OPX1000config import *
else:
    from configurations.DB_6Q.OPX1000config import *

# ---- Multiplex parameters ---- #
qubit_keys = ["q0", "q1", "q2"] # Which qubits to run the program over.
required_parameters = ["qubit_key", "qubit_relaxation", "resonator_key", "resonator_relaxation"] # Parameters needed for the program.
qub_key_subset, qubit_relaxation, res_key_subset, resonator_relaxation = multiplexed_parser(qubit_keys, multiplexed_parameters.copy(), required_parameters) # Parse the parameters for the selected qubits.
# ---- Program parameters ---- #
n_avg = 200
qub_relaxation = qubit_relaxation//4 # From ns to clock cycles
res_relaxation = resonator_relaxation//4 # From ns to clock cycles

with program() as hello_qua:
    n = declare(int)
    a = declare(fixed)
    with for_(n, 0, n < n_avg, n + 1): 
        with for_(a, 0.1, a < 1.1, a + 0.1):
            for j in range(len(qub_key_subset)):
                play("cw" * amp(a), qub_key_subset[j])
                wait(200, qub_key_subset[j])

prog = hello_qua
# ---- Open communication with the OPX ---- #
from opx_credentials import qop_ip, cluster
qmm = QuantumMachinesManager(host=qop_ip, cluster_name=cluster)

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