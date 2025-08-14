"""
This file is used to configure the Octave's clock and do the automatic calibration.
"""

from qm import QuantumMachinesManager
from qm.octave import ClockMode
from configuration import *
import time
import traceback

def main():
    # Configure the Octave according to the elements settings and calibrate
    qmm = QuantumMachinesManager(host=qop_ip, port=qop_port, octave=octave_config, log_level="ERROR")
    qm = qmm.open_qm(config)

    ##################
    # Clock settings #
    ##################
    qm.octave.set_clock("octave1", clock_mode=ClockMode.Internal)
    # If using external LO change this line to one of the following:
    #     qm.octave.set_clock("octave1", clock_mode=ClockMode.External_10MHz)
    #     qm.octave.set_clock("octave1", clock_mode=ClockMode.External_100MHz)
    #     qm.octave.set_clock("octave1", clock_mode=ClockMode.External_1000MHz)
    time.sleep(1.0)  # allow ref/PLL to lock before calibration

    ##################
    # Calibration #
    ##################
    calibration = True

    if calibration:
        elements = ["tls1", "tls2", "tls3", "rr1", "rr2", "rr3"]
        for element in elements:
            try:
                qm.calibrate_element(element)  # uses LO/IF from your config
                qm.octave.set_element_parameters_from_calibration_db(element)
                print(f" {element} calibrated and parameters applied from DB")
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