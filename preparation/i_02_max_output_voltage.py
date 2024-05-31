"""
We can scan the output voltage by rescaling the pulse amplitude by a factor lying within [-2, 2).
Can do linear, logarithmic (for_()) and arbitrary (for_each_()) sweeps.

Comments:
    - Dynamic rescaling isn't supported for 2Gs/s yet, but will be in the final version.
    - The waveform memory will be greatly increased in the future.
"""
from qm.qua import *
from qm import QuantumMachinesManager
from qm import SimulationConfig
from configuration_OPX1000 import *
from qualang_tools.loops import from_array
import plotly.io as pio
pio.renderers.default='browser'

# get the config
config = get_config(sampling_rate=1e9)

###################
# The QUA program #
###################
a_min = -1
a_max = 1
da = 0.1
with program() as scan_amp:
    a = declare(fixed)
    play("const", "scope_trigger")
    with for_(a, a_min, a < a_max + da/2, a + da):
        play("const" * amp(a), "lf_element_1")  # 1Vpp
        play("const" * amp(a), "lf_element_2")  # 5Vpp
    with for_(a, a_max, a > a_min - da/2, a - da):
        play("const" * amp(a), "lf_element_1")  # 1Vpp
        play("const" * amp(a), "lf_element_2")  # 5Vpp


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
    job = qmm.simulate(config, scan_amp, simulation_config)
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
    job = qm.execute(scan_amp)
