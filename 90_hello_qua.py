# %%
"""
A simple sandbox to showcase different QUA functionalities during the installation.
"""

from qm.qua import *
from qm import QuantumMachinesManager
from qm import SimulationConfig
from configuration_MWFEM import *


###################
# The QUA program #
###################
amp_list = np.linspace(0, 1, 5)
dur_step = 4
dur_list = np.arange(dur_step, (len(amp_list) + 1) * dur_step, dur_step, dtype=int)
if_list = np.linspace(-300, 300, len(amp_list), dtype=int) * u.MHz
with program() as hello_qua:
    a = declare(fixed)
    b = declare(int)
    with infinite_loop_():
        with for_each_((a, b), (amp_list, if_list)):
            update_frequency("qubit", b)
            play("cw" * amp(a), "qubit")
        wait(30, "qubit")

#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(host=qop_ip, cluster_name=cluster_name)


###########################
# Run or Simulate Program #
###########################

simulate = True

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=1_000)  # In clock cycles = 4ns
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
    waveform_report.create_plot(
        samples, plot=True, save_path=str(Path(__file__).resolve())
    )
else:
    # Open a quantum machine to execute the QUA program
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it - Execute does not block python!
    job = qm.execute(hello_qua)
