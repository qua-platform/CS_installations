from pathlib import Path

from qm.qua import *
from qm import SimulationConfig
from qualang_tools.units import unit
from quam_libs.components import QuAM
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import savgol_filter
from qualang_tools.units import unit
from quam_libs.components import QuAM
from qm import QuantumMachinesManager

###################################################
#  Load QuAM and open Communication with the QOP  #
###################################################
# Class containing tools to help handling units and conversions.
u = unit(coerce_to_integer=True)
# Instantiate the QuAM class from the state file
path = "C:\Git\CS_installations\qualibrate\configuration\quam_state"
machine = QuAM.load(path)
# Generate the OPX and Octave configurations
config = machine.generate_config()
# Open Communication with the QOP
qmm = machine.connect()

qubits = [machine.rf_qubits[q] for q in machine.active_qubit_names]
with program() as hello_qua:
    # check I and Q, put two I and Q elements on two different ports for debugging purposes
    # square pulse
    frame_rotation_2pi(0.25, "q1.Q")
    align()
    qubits[0].I.play("x180_Square")
    qubits[0].Q.play("x180_Square")

    align()
    reset_frame("q1.Q")
    wait(100)

    # cosine pulse
    frame_rotation_2pi(0.25, "q1.Q")
    align()
    qubits[0].I.play("x180_Cosine", duration=100)
    qubits[0].Q.play("x180_Cosine", duration=100)

    align()
    reset_frame("q1.Q")
    wait(100)

    # DRAG cosine pulse
    frame_rotation_2pi(0.25, "q1.Q")
    align()
    qubits[0].I.play("x180_DragCosine", duration=100)
    qubits[0].Q.play("x180_DragCosine", duration=100)


simulate = True

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=10_000)  # In clock cycles = 4ns
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
    waveform_report.create_plot(samples, plot=True, save_path=str(Path(__file__).resolve()))
else:
    # Open a quantum machine to execute the QUA program
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it - Execute does not block python!
    job = qm.execute(hello_qua)



debug = True
plot_wfs_from_config = True

if debug:
    from qm import generate_qua_script
    sourceFile = open('debug.py', 'w')
    print(generate_qua_script(hello_qua, config), file=sourceFile)
    sourceFile.close()

plot_wfs_from_config = False
if plot_wfs_from_config:
    import matplotlib.pyplot as plt

    fig, axes = plt.subplots(2, 3, figsize=(10, 8))
    axes = axes.flatten()
    axes[0].plot(config['waveforms']['q1.I.x90_DragCosine.wf']['samples'])
    axes[0].set_title("q1.I.x90_DragCosine")

    axes[3].plot(config['waveforms']['q1.Q.x90_DragCosine.wf']['samples'])
    axes[3].set_title("q1.Q.x90_DragCosine")

    axes[1].plot(config['waveforms']['q1.I.x90_Cosine.wf']['samples'])
    axes[1].set_title("q1.I.x90_Cosine")

    axes[4].plot(config['waveforms']['q1.Q.x90_Cosine.wf']['samples'])
    axes[4].set_title("q1.Q.x90_Cosine")

    axes[2].plot(config['waveforms']['q1.I.saturation.wf']['sample']*np.ones(config['pulses']['q1.I.saturation.pulse']['length']))
    axes[2].set_title("q1.I.saturation")


    plt.show()
