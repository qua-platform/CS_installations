"""
This file is used to configure the Octave's clock and do the automatic calibration.
"""

from qm import QuantumMachinesManager
from qm.octave import ClockMode
from configuration import *
import time
import traceback
from qm.octave import QmOctaveConfig
import os

def main():
    # Configure the Octave according to the elements settings and calibrate
    qmm = QuantumMachinesManager(host=qop_ip, port=qop_port, octave_calibration_db_path=os.getcwd())
    qm = qmm.open_qm(config)

    ##################
    # Calibration #
    ##################
    calibration = True

    if calibration:
        elements = ["qubit1", "qubit2", "qubit3", "rr1", "rr2", "rr3"]
       # elements = ["qubit1", "qubit2", "qubit3"]
        for element in elements:
            try:
                qm.calibrate_element(element)  # uses LO/IF from your config
                #qm.octave.set_element_parameters_from_calibration_db(element)
                print(f" {element} calibrated and parameters applied to DB")
            except Exception:
                print(f" Calibration failed for {element}")
                traceback.print_exc()

    try:
        qm.close()
    except Exception:
        pass
    try:
        qmm.close()
    except Exception:
        pass

if __name__ == "__main__":
    main()