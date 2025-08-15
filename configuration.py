"""
QUA-Config supporting OPX+ & Octave
"""

from pathlib import Path

import numpy as np
import plotly.io as pio
from qualang_tools.config.waveform_tools import drag_gaussian_pulse_waveforms
from qualang_tools.units import unit

pio.renderers.default = "browser"
#######################
# AUXILIARY FUNCTIONS #
#######################
u = unit(coerce_to_integer=True)

######################
# Network parameters #
######################
qop_ip = "172.16.33.101"  # Write the QM router IP address
cluster_name = "CS_2"  # Write your cluster_name if version >= QOP220
qop_port = None  # Write the QOP port if version < QOP220

#############
# Save Path #
#############
# Path to save data
save_dir = Path(__file__).parent.resolve() / "Data"
save_dir.mkdir(exist_ok=True)

default_additional_files = {
    Path(__file__).name: Path(__file__).name,
    "optimal_weights.npz": "optimal_weights.npz",
}

############################
# Set octave configuration #
############################
con = "con1"

#####################
# OPX configuration #
#####################
readout_length = 1*u.ms
readout_freq = 10 *u.MHz
readout_amp = 0.3
depletion_time = 100
#############################################
#                  Config                   #
#############################################
config = {
    "version": 1,
    "controllers": {
        con: {
            "analog_outputs": {
                9: {"offset": 0.0},  
            },
            "digital_outputs": {},
            "analog_inputs": {
                1: {"offset": 0.0, "gain_db": 0},  
            },
        }
    },
    "elements": {
            "test": {
                "singleInput": {
                    "port": (con, 9),
                },
                "intermediate_frequency": readout_freq,
                "operations": {
                    "readout": "readout_pulse",
                },
                "outputs": {
                    "out1": (con, 1),
                },
                "time_of_flight": 28,
                "smearing": 0,
            },
        },
    "pulses": {
         "readout_pulse": {
            "operation": "measurement",
            "length": readout_length,
            "waveforms": {
                "single": "readout_wf",
            },
            "integration_weights": {
                "cos": "cosine_weights",
                "sin": "sine_weights",
            },
            "digital_marker": "ON",
        },
    },
    "waveforms": {
        "readout_wf": {"type": "constant", "sample": readout_amp},
    },

    "digital_waveforms": {
        "ON": {"samples": [(1, 0)]},
    },

    "integration_weights": {
        "cosine_weights": {
            "cosine": [(0.1, readout_length)], #Reduce it when using long readout lengths to avoid overflow. 
            "sine": [(0.0, readout_length)],
        },
        "sine_weights": {
            "cosine": [(0.0, readout_length)],
            "sine": [(0.1, readout_length)],  #Reduce it when using long readout lengths to avoid overflow.
        },
    },
}