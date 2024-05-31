from qm.qua import *
from qm import QuantumMachinesManager
from qm import SimulationConfig
from configuration_OPX1000 import *
from qualang_tools.loops import from_array
import plotly.io as pio
pio.renderers.default='browser'

# get the config
config = get_config(sampling_rate=2e9)

###################
# The QUA program #
###################
time_to_play_in_seconds = 3
frequencies = np.arange(-500e6, 500e6, 50e6)
with program() as rf_sweep:
    f = declare(int)
    i = declare(int)
    with for_(*from_array(f, frequencies)):
        update_frequency("mw_element_1", f)
        with for_(i, 0, i<int(time_to_play_in_seconds / (const_len * 1e-9)), i+1):
            play("const", "mw_element_1")


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
    job = qmm.simulate(config, rf_sweep, simulation_config)
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
    job = qm.execute(rf_sweep)
