# %%
"""
A simple sandbox to showcase different QUA functionalities during the installation.
"""

from qm.qua import *
from qm import QuantumMachinesManager, SimulationConfig
from configuration_mw_fem import *
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use('TkAgg')

###################
# The QUA program #
###################
with program() as PROGRAM: # 'PROGRAM' is user defined name
    a = declare(fixed) #fixed is float, str is str, int is int
    # with infinite_loop_():
    with for_(a, 0, a < 2, a + 0.1): 
        #Actual amp is config.full_scale_power_dbm*config.pi_amp_q1*a(here)
        #'a' range in program is (2,-2) 
        #play("cw" * amp(a), "rr1")
        # play("cw" * amp(a), "rr2")
        play("cw"* amp(a), "q4_xy")
        # play("cw"* amp(1), "q2_xy")

#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(host=qop_ip, port=qop_port, cluster_name=cluster_name)

###########################
# Run or Simulate Program #
###########################

# simulate = False  
simulate = True

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=5000)  # In clock cycles = 4ns #5000 is 5000*4 ns = 20 us
    # Simulate blocks python until the simulation is done
    job = qmm.simulate(config, PROGRAM, simulation_config) #quipment start here
    # Get the simulated samples
    samples = job.get_simulated_samples()
    # Plot the simulated samples
    # samples.con1.plot()
    # plt.show()
    # Get the waveform report object
    waveform_report = job.get_simulated_waveform_report()
    # Cast the waveform report to a python dictionary
    waveform_dict = waveform_report.to_dict()
    # Visualize and save the waveform report
    waveform_report.create_plot(samples, plot=True, save_path=str(Path(__file__).resolve()))
else:
    # Open a quantum machine to execute the QUA program
    qm = qmm.open_qm(config)

    # Send the QUA program to the OPX, which compiles and executes it - Execute does not block python!
    job = qm.execute(PROGRAM) #quipment start here

# %%
