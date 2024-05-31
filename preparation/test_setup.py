from qm.qua import *
from qm import QuantumMachinesManager
from qm import SimulationConfig
from configuration_OPX1000 import *
import N9010B_driver
import pyvisa
import matplotlib.pyplot as plt
from time import sleep


rm = pyvisa.ResourceManager()
inst = rm.open_resource("TCPIP0::192.168.116.141::inst0::INSTR")
spectrum = N9010B_driver.KeysightXSeries(inst)

#spectrum.set_video_bandwidth(10e3)
#spectrum.set_bandwidth(1e6)
spectrum.set_center_freq(int(7.45e9))
spectrum.set_span(int(1e9))
spectrum.set_sweep_points(1000)
spectrum.set_ref_value(10)
sleep(1)
plt.plot(spectrum.get_full_trace())
spectrum.set_center_freq(int(5.45e9))
sleep(2)
plt.plot(spectrum.get_full_trace())

###################
# The QUA program #
###################
with program() as hello_qua:
    set_dc_offset("element_1", "single", -0.3)
    wait(100)
    align()
    play("const", "element_1")
    play("const", "element_2")

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
    job = qmm.simulate(config, hello_qua, simulation_config)
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
    job = qm.execute(hello_qua)
