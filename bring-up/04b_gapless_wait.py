# %%
from qm import QuantumMachinesManager
from qm.qua import *
from qm.octave import *
from configuration import *
from qm import SimulationConfig
import time
import numpy as np

amp_list = np.linspace(0, 1, 10)
duration_list = np.linspace(10, 100, len(amp_list)).astype(int)

###################################
# Open Communication with the QOP #
###################################
qmm = QuantumMachinesManager(host=qop_ip, port=qop_port, octave=octave_config)

###################
# The QUA program #
###################
with program() as prog:
    a = declare(fixed)  # QUA variable for the amplitude
    b = declare(int)  # QUA variable for the duration
    with for_each_((a, b), (amp_list, duration_list)):
        # Play a pulse with varying amplitude and duration
        play("pi" * amp(a), "qubit1", duration=b)
        # Align the qubits does not guarantee alignment due to synchronization between cores
        # align("qubit1", "qubit2")
        # Wait for the duration minus a small offset to ensure alignment
        wait(b - 4, "qubit2")
        # Play a pulse on the second qubit with the same amplitude
        play("pi" * amp(a), "qubit2", duration=b)

        wait(25)

#######################################
# Execute or Simulate the QUA program #
#######################################
simulate = True
if simulate:
    simulation_config = SimulationConfig(duration=400)  # in clock cycles
    job_sim = qmm.simulate(config, prog, simulation_config)
    samples = job_sim.get_simulated_samples()
    samples.con1.plot()
    waveform_report = job_sim.get_simulated_waveform_report()
    # Cast the waveform report to a python dictionary
    # waveform_dict = waveform_report.to_dict()
    # Visualize and save the waveform report
    waveform_report.create_plot(
        samples, plot=True, save_path=str(Path(__file__).resolve())
    )
else:
    qm = qmm.open_qm(config)
    job = qm.execute(prog)
    # Execute does not block python! As this is an infinite loop, the job would run forever.
    # In this case, we've put a 10 seconds sleep and then halted the job.
    time.sleep(10)
    job.halt()

# %%
