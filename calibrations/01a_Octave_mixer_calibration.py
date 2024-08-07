"""
A simple program to calibrate Octave mixers for all qubits and resonators
"""

from pathlib import Path
from quam_libs.components import QuAM

###################################################
#  Load QuAM and open Communication with the QOP  #
###################################################
# Instantiate the QuAM class from the state file

# Instantiate the QuAM class from the state file
machine = QuAM.load()


# # external_clock = False
# # if external_clock:
# #     # Change to the relevant external frequency
# #     qm.octave.set_clock(octave, clock_mode=ClockMode.External_10MHz)
# # else:
# #     qm.octave.set_clock(octave, clock_mode=ClockMode.Internal)
# # You can connect clock out from rear panel to a spectrum analyzer  to see the 1GHz signal


# Generate the OPX and Octave configurations
config = machine.generate_config()
octave_config = machine.get_octave_config()
# Open Communication with the QOP
qmm = machine.connect()
qm = qmm.open_qm(config)

resonators = [machine.qubits["q0"].resonator.name, machine.qubits["q6"].resonator.name]

for resonator in resonators:
    qm.calibrate_element(resonators)

