"""
A simple sandbox to showcase different QUA functionalities during the installation.
https://docs.quantum-machines.co/latest/docs/API_references/qua/dsl_main/
"""

from configuration import *
from qm import QuantumMachinesManager, SimulationConfig
from qm.qua import *

###################
# The QUA program #
###################
with program() as hello_qua:
    a = declare(fixed)
    with infinite_loop_():
        with for_(a, 0, a < 1.1, a + 0.05):
            # play("control", "control_aom")
            # update_frequency("readout_aom", 10e6)
            # frame_rotation(180,"readout_aom")
            play("control" * amp(a), "control_eom")
            reset_phase("readout_aom")
            frame_rotation(180, "readout_aom")
            play("readout" * amp(a), "readout_aom")
            play("gaussian" * amp(a), "control_aom")


#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(
    host=opx_ip, port=qop_port, cluster_name=cluster_name, octave=octave_config
)

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
    samples = job.get_simulated_samples()
    waveform_report = job.get_simulated_waveform_report()
    waveform_report.create_plot(samples, plot=True, save_path="./")
    plt.show()
else:
    # Open a quantum machine to execute the QUA program
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it - Execute does not block python!
    job = qm.execute(hello_qua)
