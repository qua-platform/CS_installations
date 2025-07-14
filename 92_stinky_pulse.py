#%%
"""
A simple sandbox to showcase different QUA functionalities during the installation.
"""
from qm.qua import *
from qm import QuantumMachinesManager
from qm import SimulationConfig
from configuration_oscilloscope import *

##################
#   Parameters   #
##################
n_avg = 1000000000  

# Parameters Definition
level_init = [0.3, -0.1]
level_manip = [0.4, -0.2]
level_readout = [0.3, -0.1]
duration_init = 2000
duration_manip = 5000
duration_readout = 1000

# Add the relevant voltage points describing the "slow" sequence (no qubit pulse)
seq = VoltageGateSequence(config, ["P1_sticky", "P2_sticky"])
seq.add_points("initialization", level_init, duration_init)
seq.add_points("idle", level_manip, duration_manip)
seq.add_points("readout", level_readout, duration_readout)
#Note : Can not set the step over than +-0.5
###################
# The QUA program #
###################
with program() as hello_qua:
    n = declare(int)  # QUA variable for the averaging loop
    t = declare(int, value=600)
    i = declare(int)
    with for_(n, 0, n < n_avg, n + 1):
        with strict_timing_():
            seq.add_step(voltage_point_name="initialization")
            seq.add_step(voltage_point_name="idle", duration=t)
            seq.add_step(voltage_point_name="readout")
            seq.add_compensation_pulse(duration=2_000)
        seq.ramp_to_zero()

#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(**qmm_settings)

###########################
# Run or Simulate Program #
###########################

simulate = True

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=1000)  # In clock cycles = 4ns
    # Simulate blocks python until the simulation is done
    job = qmm.simulate(config, hello_qua, simulation_config)
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
    # Send the QUA program to the OPX, which compiles and executes it - Execute does not block python!
    job = qm.execute(hello_qua)
