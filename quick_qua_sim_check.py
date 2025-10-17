
import json

from qm.qua import *
from qm import QuantumMachinesManager, SimulationConfig
from qm import SimulationConfig
from qm_saas import QmSaas, QOPVersion, ClusterConfig        
from pathlib import Path


# --- Choose the qubit pairs and its coupler element ---
qA, qB = "q15", "q16"
coupler = "c7_Q1516"
coupler_alt = "c10_Q1516"

# small sanity-check program
with program() as two_qubit_sanity:
    # Declare result variables
    IA = declare(fixed)
    QA = declare(fixed)
    IB = declare(fixed)
    QB = declare(fixed)

    # Local single-qubit pre-rotations
    play("x90", f"{qA}.xy")
    play("x90", f"{qB}.xy")
    play("x90", "q14.xy")
    #align(f"{qA}.xy", f"{qB}.xy", coupler)
    wait(40, coupler, coupler_alt) 

    # One 2-qubit gate on the coupler 
    play("const_1102", coupler)
    play("const_1102", coupler_alt)

client = QmSaas(
    host="qm-saas.dev.quantum-machines.co",
    email="benjamin.safvati@quantum-machines.co",
    password="ubq@yvm3RXP1bwb5abv"
)

cluster_config = ClusterConfig()
controller = cluster_config.controller()
controller.lf_fems(1, 2)
controller.mw_fems(3, 4, 5)

with client.simulator(QOPVersion("v3_5_0"), cluster_config) as inst: 
    inst.spawn()                                                  # boot the virtual QOP

    qmm = QuantumMachinesManager(
        host=inst.host,
        port=inst.port,
        connection_headers=inst.default_connection_headers, log_level="DEBUG"
    )

    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=1_000)  # In clock cycles = 4ns
    # Simulate blocks python until the simulation is done
    config = json.loads(Path("qua_config.json").read_text())
    job = qmm.simulate(config, two_qubit_sanity, simulation_config)
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
  

