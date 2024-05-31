from qm.qua import *
from qm import QuantumMachinesManager
from qm import SimulationConfig
from configuration_OPX1000 import *
from time import sleep
import plotly.io as pio
pio.renderers.default='browser'

# get the config
config = get_config(sampling_rate=1e9)

###################
# The QUA program #
###################
voltage_values_slow = np.linspace(-1.5, 1.5, 51)
voltage_values_fast = np.linspace(-1.5, 1.5, 101)
# Set up the qdac and load the voltage list
# mdac = MDAC()

with program() as mdac_trig:
    n = declare(int)
    i = declare(int)
    j = declare(int)
    with for_(n, 0, n < 100, n + 1):  # The averaging loop
        with for_(i, 0, i < len(voltage_values_slow), i + 1):
            play("trigger", "mdac_trigger")
            wait(5 * u.us)


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
    simulation_config = SimulationConfig(duration=10_000)  # In clock cycles = 4ns
    # Simulate blocks python until the simulation is done
    job = qmm.simulate(config, mdac_trig, simulation_config)
    # Plot the simulated samples
    job.get_simulated_samples().con1.plot()
    # Get the waveform report
    samples = job.get_simulated_samples()
    waveform_report = job.get_simulated_waveform_report()
    waveform_report.create_plot(samples, plot=True, save_path=None)
else:
    # Open a quantum machine to execute the QUA program
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it - Execute does not block python!
    job = qm.execute(mdac_trig)
