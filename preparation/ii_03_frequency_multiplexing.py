import numpy as np
from qm.qua import *
from qm import QuantumMachinesManager
from qm import SimulationConfig
from configuration_OPX1000 import *
import plotly.io as pio
pio.renderers.default='browser'

# get the config
config = get_config(sampling_rate=1e9)

###################
# The QUA program #
###################
freq_list = (np.random.random(16) * 500e6).astype("int")
for i in range(len(freq_list)):
    config["elements"][f"lf_element_{i}"] = {
            "singleInput": {
                "port": ("con1", 3, 1),
            },
            "intermediate_frequency": int(freq_list[i]),
            "operations": {
                "const": "const_single_pulse",
                "arbitrary": "arbitrary_pulse",
                "up": "up_pulse",
                "down": "down_pulse",
            },
        }

with program() as LF_multiplexing:
    with infinite_loop_():
        for i in range(16):
            play("const"*amp(1/16), f"lf_element_{i}")

freq_list = (np.random.random(8) * 350e6).astype("int")
freq_list_if = [-300e6, -200e6, -100e6, 0, 100e6, 200e6, 300e6, 400e6]
for i in range(len(freq_list)):
    config["elements"][f"mw_element_{i}"] = {
        "MWInput": {
                "port": ("con1", 2, 1),
                "oscillator_frequency": 6e9,
            },
            "intermediate_frequency": freq_list_if[i],
            "operations": {
                "const": "const_pulse_mw",
            },
    }


with program() as MW_multiplexing:
    with infinite_loop_():
        for i in range(8):
            play("const"*amp(1/8), f"mw_element_{i}")

#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(host=qop_ip, port=qop_port, cluster_name=cluster_name)
qmm.close_all_quantum_machines()
###########################
# Run or Simulate Program #
###########################

simulate = True

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=10_000)  # In clock cycles = 4ns
    # Simulate blocks python until the simulation is done
    job = qmm.simulate(config, LF_multiplexing, simulation_config)
    # Plot the simulated samples
    job.get_simulated_samples().con1.plot()
    # Get the waveform report
    # samples = job.get_simulated_samples()
    # waveform_report = job.get_simulated_waveform_report()
    # waveform_report.create_plot(samples, plot=True, save_path=None)
else:
    # Open a quantum machine to execute the QUA program
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it - Execute does not block python!
    job = qm.execute(MW_multiplexing)
