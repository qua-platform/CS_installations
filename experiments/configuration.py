"""
Configuration working for QOP222 and qm-qua==1.1.5 and newer.
"""

from pathlib import Path
import numpy as np
from qualang_tools.units import unit


#######################
# AUXILIARY FUNCTIONS #
#######################
u = unit(coerce_to_integer=True)


###########
# Network #
###########

qop_ip = "127.0.0.1"  # Write the QM router IP address
cluster_name = None  # Write your cluster_name if version >= QOP220
qop_port = None  # Write the QOP port if version < QOP220


# Set octave_config to None if no octave are present
octave_config = None


#############
# Save Path #
#############
# Path to base directories for script and data
base_dir = Path().absolute()
save_dir = base_dir / "QM" / "INSTALLATION" / "data"


#############
# VARIABLES #
#############

# frequencies
aom1_freq = 10 * u.MHz
aom2_freq = 20 * u.MHz

# amplitudes
const_aom1_amp = 0.01
const_aom2_amp = 0.02

# pulse length
const_len = 1 * u.ms

#############################################
#                  Config                   #
#############################################
config = {
    "version": 1,
    "controllers": {
        "con1": {
            "analog_outputs": {
                1: {"offset": 0.0},  # aom1
                2: {"offset": 0.0},  # aom2
            },
            "digital_outputs": {
                1: {},
            },  # Not used yet
            "analog_inputs": {
                1: {"offset": 0.0, "gain_db": 0},  # Not used yet
                2: {"offset": 0.0, "gain_db": 0},  # Not used yet
            },
        },
    },
    "elements": {
        "aom1": {
            "singleInput": {"port": ("con1", 1)},
            "intermediate_frequency": aom1_freq,
            "operations": {
                "cw": "const_pulse1",
            },
        },
        "aom2": {
            "singleInput": {"port": ("con1", 2)},
            "intermediate_frequency": aom2_freq,
            "operations": {
                "cw": "const_pulse2",
            },
        },
    },
    "pulses": {
        "const_pulse1": {
            "operation": "control",
            "length": const_len,
            "waveforms": {
                "single": "const_aom1_wf",
            },
        },
        "const_pulse2": {
            "operation": "control",
            "length": const_len,
            "waveforms": {
                "single": "const_aom2_wf",
            },
        },
    },
    "waveforms": {
        "zero_wf": {"type": "constant", "sample": 0.0},
        "const_aom1_wf": {"type": "constant", "sample": const_aom1_amp},
        "const_aom2_wf": {"type": "constant", "sample": const_aom2_amp},
    },
    "digital_waveforms": {
        "ON": {"samples": [(1, 0)]},
    },
    "integration_weights": {
        "cosine_weights": {
            "cosine": [(1.0, const_len)],
            "sine": [(0.0, const_len)],
        },
        "sine_weights": {
            "cosine": [(0.0, const_len)],
            "sine": [(1.0, const_len)],
        },
        "minus_sine_weights": {
            "cosine": [(0.0, const_len)],
            "sine": [(-1.0, const_len)],
        },
    },
}
