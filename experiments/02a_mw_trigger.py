# %%
"""
        RAW ADC TRACES
The goal of this script is to measure the raw ADC traces without demodulation or integration.
It can be used to make sure that the ADCs are not saturated/offsetted and estimate the SNR.
It also allows to calibrate several parameters:
    - The time of flight: it corresponds to some internal processing time and propagation delay of the readout pulse.
      Its value can be updated in the configuration (time_of_flight) and is used to delay the acquisition window with
      respect to the time at which the readout pulse is sent.
    - The analog inputs offset: due to some small impedance mismatch, the signals acquired by the OPX can have small
      offsets that can be removed in the configuration (config/controllers/"con1"/analog_inputs) to improve demodulation.
    - The analog inputs gain: if the signal is limited by digitization or saturates the ADC, the variable gain of the
      OPX analog input can be set to adjust the signal within the ADC range +/-0.5V.
      The gain (-12 dB to 20 dB) can also be set in the configuration (config/controllers/"con1"/analog_inputs). 
"""

from qm.QuantumMachinesManager import QuantumMachinesManager
from qm.qua import *
import matplotlib.pyplot as plt
from configuration import *
from qm import SimulationConfig


###################
# The QUA program #
###################

with program() as pulse_on:

    with infinite_loop_():
        # Drive the AOM to play the readout laser pulse
        play("mw_ON", "MW_Switch")
        # Waits for the
        wait(1 * u.us, "MW_Switch")


#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(qop_ip, cluster_name=cluster_name)

simulate = False

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=10_000)  # In clock cycles = 4ns
    job = qmm.simulate(config, pulse_on, simulation_config)
    plt.figure()
    job.get_simulated_samples().con1.plot()
else:
    # Open Quantum Machine
    qm = qmm.open_qm(config)
    # Execute program
    job = qm.execute(pulse_on)

# %%