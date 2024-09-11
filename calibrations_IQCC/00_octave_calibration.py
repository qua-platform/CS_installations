# %%

"""
A simple program to calibrate Octave mixers for all qubits and resonators
"""

from typing import List, Optional
from qm import QuantumMachine
from qualibrate import QualibrationNode, NodeParameters

from quam_libs.components import QuAM


class Parameters(NodeParameters):
    qubits: Optional[List[str]] = None
    calibrate_resonator: bool = True
    calibrate_drive: bool = True


node = QualibrationNode(name="00_Mixer_Calibration", parameters_class=Parameters)

node.parameters = Parameters(qubits=["q0", "q1", "q2", "q3"])

# %% Load QuAM and open Communication with the QOP  #

# Instantiate the QuAM class from the state file
machine = QuAM.load()

# Generate the OPX and Octave configurations
config = machine.generate_config()
# Open Communication with the QOP
qmm = machine.connect()
qm = qmm.open_qm(config)

qubits = [machine.qubits[q] for q in node.parameters.qubits]


# %%
def calibrate_octave(
    qubit,
    qm: QuantumMachine,
    calibrate_resonator: bool = True,
    calibrate_drive: bool = True,
) -> dict:
    mixer_calibrations = {}

    channels = []
    if calibrate_resonator:
        channels.append(qubit.resonator)
    if calibrate_drive:
        channels.append(qubit.xy)

    for channel in channels:
        if channel is None:
            continue

        print(f"Calibrating {channel.name}")
        mixer_calibrations[channel.name] = qm.calibrate_element(
            qe=channel.name,
            lo_if_dict={channel.LO_frequency: [channel.intermediate_frequency]},
        )
    return mixer_calibrations


mixer_calibrations = []
for qubit in qubits:
    mixer_calibrations.append(
        calibrate_octave(
            qubit=qubit,
            qm=qm,
            calibrate_resonator=node.parameters.calibrate_resonator,
            calibrate_drive=node.parameters.calibrate_drive,
        )
    )

# %%
