"""
This file is used to run the automatic mixer calibration.
"""

import os

from configuration import *
from qm import QuantumMachinesManager

# from qualang_tools.octave_tools import calibration_result_plotter as plotter

# Configure the Octave according to the elements settings and calibrate
qmm = QuantumMachinesManager(
    host=opx_ip, port=qop_port, octave=octave_config, log_level="ERROR"
)
qm = qmm.open_qm(config)

##################
# Calibration #
##################

save = True

cal_res = []

elements = ["control_eom"]
for element in elements:
    print("-" * 37 + f" Calibrates {element}")
    res = qm.calibrate_element(element)
    cal_res.append(res)

# if save:
#     for result in cal_res:
#         plotter.show_lo_result(result)
#         plt.savefig(f"{os.getcwd()}/calibration_plots/{element}_lo_calibration.png")
#         plotter.show_if_result(result)
#         plt.savefig(f"{os.getcwd()}/calibration_plots/{element}_if_calibration.png")
