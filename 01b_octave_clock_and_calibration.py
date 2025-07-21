# %%
"""
This file is used to configure the Octave's clock and do the automatic calibration.
"""

import os

from qm import QuantumMachinesManager
from qm.octave import ClockMode
from configuration_octave import *


# Configure the Octave according to the elements settings and calibrate
qmm = QuantumMachinesManager(
    host=qop_ip,
    log_level="ERROR",
    cluster_name=cluster_name,
    octave_calibration_db_path=os.getcwd(),
)
qm = qmm.open_qm(config)

##################
# Clock settings #
##################
# qm.octave.set_clock(octave, clock_mode=ClockMode.Internal)
# If using external LO change this line to one of the following:
#     qm.octave.set_clock(octave clock_mode=ClockMode.External_10MHz)
#     qm.octave.set_clock(octave clock_mode=ClockMode.External_100MHz)
#     qm.octave.set_clock(octave clock_mode=ClockMode.External_1000MHz)

##################
# Calibration #
##################
calibration = True

if calibration:
    # convert the existing calibration_db.json to calibration_db.old.json
    # if os.path.exists("calibration_db.json"):
    #     os.rename("calibration_db.json", "calibration_db.old.json")
    # elements = config["elements"].keys()
    elements = ["qubit"]
    for element in elements:
        print("-" * 37 + f" Calibrates {element}")
        qm.calibrate_element(element)
