# %%
"""
This file is used to configure the Octave's clock and do the automatic calibration.
"""

import os

from qm import QuantumMachinesManager
from qm.octave import ClockMode
from configuration import *


# Configure the Octave according to the elements settings and calibrate
qmm = QuantumMachinesManager(
    host=qop_ip,
    log_level="ERROR",
    cluster_name=cluster_name,
    octave_calibration_db_path=os.getcwd(),
)
qm = qmm.open_qm(config)

##################
# Calibration #
##################
calibration = True

if calibration:
    # convert the existing calibration_db.json to calibration_db.old.json
    # if os.path.exists("calibration_db.json"):
    #     os.rename("calibration_db.json", "calibration_db.old.json")
    # elements = config["elements"].keys()
    n_qubits = 4
    elements = ["resonator"] + ["qubit" + str(i) for i in range(1, n_qubits + 1)]
    for element in elements:
        print("-" * 37 + f" Calibrates {element}")
        qm.calibrate_element(element)
