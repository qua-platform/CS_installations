"""
Configuration file for DQD measurements with an LF-FEM and Octave

See the "README" file for the relevant python requirements.
"""
import os

import numpy as np
from qualang_tools.units import unit
from pathlib import Path
import matplotlib.pyplot as plt


u = unit(coerce_to_integer=True)

######################
# Network parameters #
######################
qop_ip = "172.16.33.115"  # Write the QM router IP address
cluster_name = "CS_3"  # Write your cluster_name if version >= QOP220
qop_port = 9510  # Write the QOP port if version < QOP220
# In QOP versions > 2.2.2, the Octave is automatically deteced by the QOP.
# For QOP versions <= 2.2.2, see Tutorials/intro-to-octave/qop 222 and below.
# Below you can specify the path for the Octave mixer calibration's database file.
# octave_calibration_db_path = os.getcwd()

# Combined settings for initializing the QuantumMachinesManager
# qmm_settings = dict(
#     host=qop_ip, port=qop_port, cluster_name=cluster_name, octave_calibration_db_path=octave_calibration_db_path
# )

# Path to save data
save_dir = Path(__file__).parent.resolve() / "data"
save_dir.mkdir(exist_ok=True)


#####################
# OPX configuration #
#####################
con = "con1"  # name of the OPX1000
# octave = "oct1"  # name of the connected Octave
fem = 3  # slot index of the lf-fem inside the chassis


######################
# QDAC-I parameters  #
######################


######################
#       READOUT      #
######################
time_of_flight = 28
pulse_length = 800 *u.ns
pulse_amp = 0.5
####################
#      QUBIT       #
####################


#######################
# DC PULSE PARAMETERS #
#######################

#############################################
#                  Config                   #
#############################################
config = {
    "version": 1,
    "controllers": {
        con: {
            "type": "opx1000",
            "fems":{
                fem: {
                    "type": "LF",
                    "analog_outputs": {
                        7: {"offset": 0.0, "upsampling_mode": "mw"} #Demo
                    },
                    "digital_outputs": {
                        1: {},  # Octave Trigger
                    },
                    "analog_inputs": {
                        1: {"offset": 0.0, "gain_db": 0},  # Source Gate TIA
                        2: {"offset": 0.0, "gain_db": 0},  # (Must be defined for Octave mixer calibration)
                    },
                }
            }
        },
    },
    "elements": {
        "oscilloscope_test1": {
            "singleInput": {
                "port": (con, fem, 7),
            },
            "intermediate_frequency": 50 *u.MHz,
            "operations": {
                "strange": "strange_pulse",
                "normal": "normal_pulse"
            },
        },
        "oscilloscope_test2": {
            "singleInput": {
                "port": (con, fem, 7),
            },
            "intermediate_frequency": 80 *u.MHz,
            "operations": {
                "strange": "strange_pulse",
                "normal": "normal_pulse"
            },
        },
        "oscilloscope_sin3": {
            "singleInput": {
                "port": (con, fem, 7),
            },
            "intermediate_frequency": 150 *u.MHz,
            "operations": {
                "strange": "strange_pulse",
                "normal": "normal_pulse"
            },
        },
    },

    "pulses": {
        "strange_pulse": {
            "operation": "control",
            "length": pulse_length,
            "waveforms": {
                "single": "strange_wf",
            },
        },
        "normal_pulse": {
            "operation": "control",
            "length": pulse_length,
            "waveforms": {
                "single": "normal_wf",
            },
        },
    },
    "waveforms": {
        "normal_wf": {"type": "constant", "sample": pulse_amp},
        "strange_wf": {"type": "arbitrary", "samples": [0.5] * 100 + [0.1] * 300 + [0.3] * (pulse_length - 400)}, #range:= -0.5~0.5
    },
    "digital_waveforms": {
        "ON": {"samples": [(1, 0)]},
    },
}