#%%
from qm.qua import *
from qm import QuantumMachinesManager
from qm import SimulationConfig
from configuration_oscilloscope import *
import matplotlib.pyplot as plt

##################
#   Parameters   #
##################
# Parameters Definition
n_avg = 10  # Number of averaging loops

###################
# The QUA program #
###################
with program() as prog:
    n = declare(int)  # QUA variable for the averaging loop

    with for_(n, 0, n < n_avg, n + 1):  # QUA for_ loop for averaging
        play('arb', 'low_freq')
        wait(50)

#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(**qmm_settings)

###########################
# Run or Simulate Program #
###########################
simulate = False

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=10000)  # In clock cycles = 4ns
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
    waveform_report.create_plot(samples, plot=True, save_path=save_dir / "waveform_report.html")

else:
    # Open a quantum machine to execute the QUA program
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it
    job = qm.execute(prog)