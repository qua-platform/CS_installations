"""
A script used for playing with QUA
"""

from qm import SimulationConfig
from qm.qua import *
from qm import LoopbackInterface
from qm import QuantumMachinesManager
from configuration import *


###################
# The QUA program #
###################
with program() as hello_qua:
    a = declare(fixed)
    # update_frequency("AOM", 10e6)
    play("ON", "trigger")
    align()
    with infinite_loop_():
        with for_(a, 0, a < 1.1, a + 0.05):
            play("const" * amp(a), "AOM")
            # play("const" * amp(a), "AOM", duration = 100)
        wait(25, "AOM")

with program() as external_trigger:
    play("ON", "trigger")
    play("const", "AOM", duration=4)
    wait_for_trigger("AOM")
    play("const", "AOM")
################################
# Open quantum machine manager #
################################

qmm = QuantumMachinesManager(host=qop_ip, cluster_name=cluster_name)

#######################
# Simulate or execute #
#######################

simulate = False

if simulate:
    # Simulates the QUA program for the specified duration
    simulate_config = SimulationConfig(duration=1000) # duration is in clock cycles (1 clock cycles ia 4ns)
    # Simulate blocks python until the simulation is done
    job = qmm.simulate(config, external_trigger, simulate_config)
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
    qm = qmm.open_qm(config)
    job = qm.execute(external_trigger)  # execute QUA program