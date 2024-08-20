"""
TIME-RABI OSCILLATIONS

This program is designed to play a series of DC pulses with varying durations.
It mimics a Rabi oscillation measurement of a charge qubit.
"""

from qm import QuantumMachinesManager, SimulationConfig
from qm.qua import *
from configuration import *
import matplotlib.pyplot as plt
import numpy as np
from qualang_tools.bakery import baking


plunger_gate = "right"
max_length = 16  # in ns

####################
# Helper functions #
####################
def baked_waveform(waveform_amp, dc_el):
    pulse_segments = []  # Stores the baking objects
    # Create the different baked sequences, each one corresponding to a different truncated duration
    waveform = [waveform_amp] * max_length

    for i in range(1, max_length + 1):
        with baking(config, padding_method="left") as b:
            wf = waveform[:i]
            b.add_op(f"step", dc_el, wf)
            b.play("step", dc_el)

        # Append the baking object in the list to call it from the QUA program
        pulse_segments.append(b)

    return pulse_segments


###################
# The QUA program #
###################

baked_signals = {}
# Baked dc pulse segments with 1ns resolution
# the first 16 nanoseconds and the 0.0 before the step
dc_amp = left_plunger_step_amp
dc_el = f"{plunger_gate}_plunger"
baked_signals = baked_waveform(dc_amp, dc_el)

times = np.arange(1, max_length + 1, 1)  # x-axis for plotting - must be in ns

with program() as rabi:
    for i in range(max_length):
        baked_signals[i].run()
        wait(20 * u.ns)

qmm = QuantumMachinesManager(host=qop_ip, port=qop_port, cluster_name=cluster_name)

###########################
# Run or Simulate Program #
###########################
simulate = True

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=250)  # In clock cycles = 4ns
    job = qmm.simulate(config, rabi, simulation_config)
    waveform_on_ch2 = job.get_simulated_samples().con1.analog['1-2']
    plt.step(range(len(waveform_on_ch2)), waveform_on_ch2)
    plt.xlabel('Time [ns]')
    plt.ylabel('Output Voltage [V]')
    plt.title('Pulse Train for Rabi Oscillations')
    plt.show()
else:
    qm = qmm.open_qm(config)
    job = qm.execute(rabi)
