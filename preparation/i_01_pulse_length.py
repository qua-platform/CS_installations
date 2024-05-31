"""
Change the pulse duration dynamically in QUA, by only preloading the shortest pulse shape.
Can do linear, logarithmic (for_()) and arbitrary (for_each_()) sweeps.
Can also play a continuous wave with constant or arbitrary amplitude modulation (infinite_loop_()).
Comments:
    - Dynamic duration isn't supported for 2Gs/s yet, but will be in the final version.
    - Currently the minimum step is 4ns, but it will be reduced down to 1ns in the future.
    - Currently the minimum pulse duration is 16ns, but it will be reduced down to 4ns in the future.
"""
from qm.qua import *
from qm import QuantumMachinesManager
from qm import SimulationConfig
from configuration_OPX1000 import *
from qualang_tools.loops import from_array, get_equivalent_log_array
import plotly.io as pio
pio.renderers.default='browser'

# get the config
config = get_config(sampling_rate=1e9)

###################
# The QUA program #
###################
# Linear or logarithmic scan
t_min = 16 // 4  # In clock cycles (4ns) - Must be larger than 4 clock cycles = 16ns
t_max = 10000 // 4  # In clock cycles (4ns) - Must be lower than 2**24 clock cycles = 67ms
step = 4 // 4  # In clock cycles (4ns)
with program() as scan_length:
    t = declare(int)
    with infinite_loop_():
        play("const", "scope_trigger")
        with for_(t, t_min, t <= t_max, t + step):
        # with for_(*from_array(t, np.arange(t_min, t_max + step/2, step))):
        # with for_(*from_array(t, np.logspace(np.log10(t_min), np.log10(t_max), 21))):
            play("const", "lf_element_1", duration=t)
            play("arbitrary", "lf_element_2", duration=t)
            wait(200 * u.ns)
        wait(1 * u.us)

# Arbitrary scan
with program() as scan_length_arbitrary:
    t = declare(int)
    with infinite_loop_():
        play("const", "scope_trigger", duration=step)
        with for_each_(t, [400000, 40000, 4000, 400, 40, 4, 40, 400, 4000, 40000, 400000]):
            play("const", "lf_element_1", duration=t)
            play("const", "lf_element_2", duration=t)
            wait(200 * u.ns)
        wait(1 * u.us)

# Play a continuous wave
with program() as cw:
    play("const", "scope_trigger")
    with infinite_loop_():
        play("arbitrary", "lf_element_1")
        play("arbitrary", "lf_element_2")

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
    job = qmm.simulate(config, scan_length, simulation_config)
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
    job = qm.execute(scan_length)
