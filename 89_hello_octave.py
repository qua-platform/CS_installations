#%%
"""
hello_octave.py: template for basic usage of the Octave
"""

from qm import QuantumMachinesManager
from qm.qua import *
from qm.octave import *
from configuration_oscilloscope import *
from qm import SimulationConfig
import time


###################################
# Open Communication with the QOP #
###################################
qmm = QuantumMachinesManager(**qmm_settings)

###################
# The QUA program #
###################
with program() as hello_octave:
    with infinite_loop_():
        play("cw" * amp(0.5), "high_freq")

#######################################
# Execute or Simulate the QUA program #
#######################################
simulate = False
if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=1000)  # In clock cycles = 4ns
    # Simulate blocks python until the simulation is done
    job = qmm.simulate(config, hello_octave, simulation_config)
    # Get the simulated samples
    samples = job.get_simulated_samples()
    # Plot the simulated samples
    samples.con1.plot()
    # Get the waveform report object
    waveform_report = job.get_simulated_waveform_report()
    # Cast the waveform report to a python dictionary
    waveform_dict = waveform_report.to_dict()
    # Visualize and save the waveform report
    waveform_report.create_plot(samples, plot=True, save_path=save_dir / "waveform_report.html")
else:
    qm = qmm.open_qm(config)
    job = qm.execute(hello_octave)
    # Execute does not block python! As this is an infinite loop, the job would run forever.
    # In this case, we've put a 10 seconds sleep and then halted the job.
    time.sleep(10)
    job.halt()