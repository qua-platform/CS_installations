from qm.qua import *
from qm import QuantumMachinesManager
from qm import SimulationConfig
from configuration_OPX1000 import *
from qualang_tools.bakery import baking

###################
# The QUA program #
###################
def baked_waveform(baked_durations, pulse_amplitude, element):
    pulse_segments = []  # Stores the baking objects
    # Create the different baked sequences, each one corresponding to a different truncated duration
    for t in baked_durations:
        with baking(config, padding_method="right") as b:
            if t == 0:  # Otherwise, the baking will be empty and will not be created
                wf = [0.0] * 16
            else:
                wf = [pulse_amplitude] * t
            b.add_op("baled_pulse", element, wf)
            b.play("baled_pulse", element)
        # Append the baking object in the list to call it from the QUA program
        pulse_segments.append(b)
    return pulse_segments

baked_wf = baked_waveform(np.arange(0, 20, 1), 0.5, "lf_element_1")

with program() as scan_length_baking:
    i = declare(int)
    with infinite_loop_():
        play("const", "lf_element_2", duration=100)
        with for_(i, 0, i <= len(baked_wf), i + 1):
            with switch_(i):
                for j in range(len(baked_wf)):
                    with case_(j):
                        baked_wf[j].run()
                        wait(100 * u.ns)
        wait(1000 * u.ns)

#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(host=qop_ip, port=qop_port, cluster_name=cluster_name)
qmm.close_all_qms()
###########################
# Run or Simulate Program #
###########################

simulate = False

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=1_000)  # In clock cycles = 4ns
    # Simulate blocks python until the simulation is done
    job = qmm.simulate(config, scan_length_baking, simulation_config)
    # Plot the simulated samples
    job.get_simulated_samples().con1.plot()
else:
    # Open a quantum machine to execute the QUA program
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it - Execute does not block python!
    job = qm.execute(scan_length_baking)
