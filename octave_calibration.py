"""
This file is used to configure the Octave's clock and do the automatic calibration.
"""

from qm import QuantumMachinesManager
from configuration import *


# Configure the Octave according to the elements settings and calibrate
qmm = QuantumMachinesManager(**qmm_settings)
qm = qmm.open_qm(config)

calibration = True

if calibration:
    elements = ["qubit", "resonator"]
    for element in elements:
        print("-" * 37 + f" Calibrates {element}")
        qm.calibrate_element(element)
