from qm.qua import *
from qm import QuantumMachinesManager
from qm import SimulationConfig
from configuration_OPX1000 import *

from qdac2_driver import QDACII, load_voltage_list
from qualang_tools.callable_from_qua import patch_qua_program_addons, callable_from_qua
from time import sleep

# get the config
config = get_config(sampling_rate=1e9)

patch_qua_program_addons()
###################
# The QUA program #
###################
voltage_values_slow = np.linspace(-1.5, 1.5, 51)
voltage_values_fast = np.linspace(-1.5, 1.5, 101)
# Set up the qdac and load the voltage list
qdac = QDACII("Ethernet", IP_address="127.0.0.1", port=5025)
load_voltage_list(qdac, channel=1, trigger_port="ext1", voltage_list=voltage_values_fast)
load_voltage_list(qdac, channel=2, trigger_port="ext2", voltage_list=voltage_values_slow)

with program() as qdac_trig:
    n = declare(int)
    i = declare(int)
    j = declare(int)
    with for_(n, 0, n < 100, n + 1):  # The averaging loop
        with for_(i, 0, i < len(voltage_values_slow), i + 1):
            play("trigger", "qdac_trigger2")
            with for_(j, 0, j < len(voltage_values_fast), j + 1):
                play("trigger", "qdac_trigger1")
                wait(5000)


@callable_from_qua
def update_qdac(qdac, channel, voltage):
    print(f"setting the QDAC channel {channel} to {voltage} V")
    qdac.write(f'sour{channel}:volt:mode fix')
    qdac.write(f'sour{channel}:volt {voltage}')
    sleep(0.1)

with program() as qdac_integration:
    v = declare(fixed)
    with for_each_(v, voltage_values_slow):
        update_qdac(qdac, 1, v)

        # Whatever OPX sequence
        ...

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
