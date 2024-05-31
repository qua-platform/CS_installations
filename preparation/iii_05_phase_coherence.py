from qm.qua import *
from qm import QuantumMachinesManager
from qm import SimulationConfig
from configuration_OPX1000 import *
import matplotlib.pyplot as plt
import numpy as np
import plotly.io as pio
pio.renderers.default='browser'


# get the config
config = get_config(sampling_rate=1e9)

config["elements"]["lf_element_1_bis"] = {
                "singleInput": {
                    "port": ("con1", 2, 1),
                },
                "intermediate_frequency": intermediate_frequency,
                "operations": {
                    "const": "const_single_pulse",
                    "arbitrary": "arbitrary_pulse",
                    "up": "up_pulse",
                    "down": "down_pulse",
                },
            }
###################
# The QUA program #
###################
with program() as phase_coherence_1:
    update_frequency("lf_element_1", 100e6)
    update_frequency("lf_element_2", 100e6)
    play("const", "scope_trigger")
    play("const", "lf_element_1")
    play("const", "lf_element_2")
    frame_rotation_2pi(0.5, "lf_element_1")
    play("const", "lf_element_1")
    play("const", "lf_element_2")
    frame_rotation_2pi(-0.5, "lf_element_1")
    play("const", "lf_element_1")
    play("const", "lf_element_2")

with program() as phase_coherence_2:
    update_frequency("lf_element_1", 100e6)
    update_frequency("lf_element_1_bis", 100e6)
    play("const", "scope_trigger")
    play("const", "lf_element_1")
    play("const", "lf_element_1_bis")
    frame_rotation_2pi(0.5, "lf_element_1")
    play("const", "lf_element_1")
    play("const", "lf_element_1_bis")
    frame_rotation_2pi(-0.5, "lf_element_1")
    play("const", "lf_element_1")
    play("const", "lf_element_1_bis")

with program() as keep_phase:
    update_frequency("lf_element_1", 100e6)
    update_frequency("lf_element_2", 100e6)
    play("const", "scope_trigger")
    play("const", "lf_element_1")
    play("const", "lf_element_2")
    update_frequency("lf_element_1", 50e6, keep_phase=True)
    play("const", "lf_element_1")
    play("const", "lf_element_2")
    update_frequency("lf_element_1", 100e6, keep_phase=True)
    play("const", "lf_element_1")
    play("const", "lf_element_2")


#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(host=qop_ip, port=qop_port, cluster_name=cluster_name)

###########################
# Run or Simulate Program #
###########################

simulate = True

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=1_000)  # In clock cycles = 4ns
    job = qmm.simulate(config, phase_coherence, simulation_config)
    job.get_simulated_samples().con1.plot()
    # Get the waveform report
    samples = job.get_simulated_samples()
    waveform_report = job.get_simulated_waveform_report()
    waveform_report.create_plot(samples, plot=True, save_path=None)
else:
    # Open the quantum machine
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(phase_coherence)
