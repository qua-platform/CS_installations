import os
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from qualang_tools.units import unit

#######################
# AUXILIARY FUNCTIONS #
#######################
u = unit(coerce_to_integer=True)

######################
# Network parameters #
######################
qop_ip = "172.16.33.101"  # Write the QM router IP address
cluster_name = "Cluster_81"  # Write your cluster_name if version >= QOP220
qop_port = None  # Write the QOP port if version < QOP220

# Path to save data
save_dir = Path().absolute() / "QM" / "INSTALLATION" / "data"

############################
# Set octave configuration #
############################

from qm.octave import QmOctaveConfig

octave_config = QmOctaveConfig()
octave_config.set_calibration_db(os.getcwd())

#####################
# OPX configuration #
#####################

# LO frequencies:
pump_LO = 14 * u.GHz
pump_IF = 150 * u.MHz
mode_LO_1 = 6 * u.GHz
mode_LO_2 = 8 * u.GHz

# Intermediary frequencies:
IF_analyser_1 = 100 * u.MHz
IF_analyser_2 = 200 * u.MHz
time_of_flight = 24 * u.ns

# Pump parameters
pump_len = 1.0 * u.us
pump_amp = 0.15

#############################################
#                  Config                   #
#############################################
config = {
    "version": 1,
    "controllers": {
        "con1": {
            "analog_outputs": {
                1: {"offset": 0.0},  # I squeeze
                2: {"offset": 0.0},  # Q squeeze
            },
            "digital_outputs": {
                1: {},
            },
            "analog_inputs": {
                1: {"offset": 0.0, "gain_db": 0},  # I from down-conversion
                2: {"offset": 0.0, "gain_db": 0},  # Q from down-conversion
            },
        },
    },
    "elements": {
        "pump": {
            "RF_inputs": {"port": ("oct1", 1)},
            "intermediate_frequency": pump_IF,
            "operations": {
                "drive": "pump",
            },
            "time_of_flight": time_of_flight,
            "smearing": 0,
        },
        "analyser_1": {
            "RF_inputs": {"port": ("oct1", 1)},
            "RF_outputs": {"port": ("oct1", 1)},
            "intermediate_frequency": IF_analyser_1,
            "operations": {
                "read": "readout_1",
            },
            "time_of_flight": time_of_flight,
            "smearing": 0,
        },
        "analyser_2": {
            "RF_inputs": {"port": ("oct1", 1)},
            "RF_outputs": {"port": ("oct1", 2)},
            "intermediate_frequency": IF_analyser_2,
            "operations": {
                "read": "readout_2",
            },
            "time_of_flight": time_of_flight,
            "smearing": 0,
        },
    },
    "octaves": {
        "oct1": {
            "RF_outputs": {
                1: {
                    "LO_frequency": pump_LO,
                    "LO_source": "internal",
                    "output_mode": "always_on",
                    "gain": 0,
                },
            },
            "RF_inputs": {
                1: {
                    "LO_frequency": mode_LO_1,
                    "LO_source": "internal",
                    "IF_mode_I": "direct",
                    "IF_mode_Q": "off",
                },
                2: {
                    "LO_frequency": mode_LO_1,
                    "LO_source": "external",
                    "IF_mode_I": "off",
                    "IF_mode_Q": "direct",
                },
            },
            "connectivity": "con1",
        }
    },
    "pulses": {
        "pump": {
            "operation": "control",
            "length": pump_len,
            "waveforms": {
                "I": "pump_wf",
                "Q": "zero_wf",
            },
            "digital_marker": "ON",
        },
        "readout_1": {
            "operation": "measurement",
            "length": pump_len,
            "waveforms": {
                "I": "zero_wf",
                "Q": "zero_wf",
            },
            "integration_weights": {
                "cos": "cosine_weights",
                "sin": "sine_weights",
                "minus_sin": "minus_sine_weights"
            },
            "digital_marker": "ON",
        },
        "readout_2": {
            "operation": "measurement",
            "length": pump_len,
            "waveforms": {
                "I": "zero_wf",
                "Q": "zero_wf",
            },
            "integration_weights": {
                "cos": "cosine_weights",
                "sin": "sine_weights",
                "minus_sin": "minus_sine_weights"
            },
            "digital_marker": "ON",
        },
    },
    "waveforms": {
        "pump_wf": {"type": "constant", "sample": pump_amp},
    },
    "digital_waveforms": {
        "ON": {"samples": [(1, 0)]},
    },
    "integration_weights": {
        "cosine_weights": {
            "cosine": [(1.0, pump_len)],
            "sine": [(0.0, pump_len)],
        },
        "sine_weights": {
            "cosine": [(0.0, pump_len)],
            "sine": [(1.0, pump_len)],
        },
        "minus_sine_weights": {
            "cosine": [(0.0, pump_len)],
            "sine": [(-1.0, pump_len)],
        },
    },
}
