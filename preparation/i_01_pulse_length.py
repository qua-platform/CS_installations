from qm.qua import *
from qm import QuantumMachinesManager
from qm import SimulationConfig
from configuration_OPX1000 import *
import plotly.io as pio
pio.renderers.default='browser'

###################
# The QUA program #
###################
t_min = 16//4  # In clock cycles (4ns) - Must be larger than 4 clock cycles = 16ns
t_max = 120//4  # In clock cycles (4ns) - Must be lower than 2**24 clock cycles = 67ms
step = 4//4  # In clock cycles (4ns)
with program() as scan_length:
    t = declare(int)
    with infinite_loop_():
        play("const", "lf_element_2")
        with for_(t, t_min, t <= t_max, t + step):
            play("const", "lf_element_1", duration=t)
            wait(250)
        wait(1000)

with program() as scan_length_arbitrary:
    t = declare(int)
    with infinite_loop_():
        play("const", "lf_element_2", duration=step)
        with for_each_(t, [400000, 40000, 4000, 400, 40, 4, 40, 400, 4000, 40000, 400000]):
            play("const", "lf_element_1", duration=t)
            wait(200 * u.ns)
        wait(1 * u.us)

with program() as cw:
    update_frequency("lf_element_1", 0)
    play("const", "lf_element_2")
    with infinite_loop_():
        play("arbitrary", "lf_element_1")

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
    job = qm.execute(cw)
