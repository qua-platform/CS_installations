"""
This file is used to perform automatic calibration of the Octave mixers given
the configuration of your qubit elements.
"""

from qm import QuantumMachinesManager
from configuration import *


# Configure the Octave according to the elements settings and calibrate
qmm = QuantumMachinesManager(**qmm_settings)
qm = qmm.open_qm(config)

calibration = True

if calibration:
    elements = ["qubit_1", "qubit_2"]
    for element in elements:
        print("-" * 37 + f" Calibrates {element}")
        qm.calibrate_element(element)
