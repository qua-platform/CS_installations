"""
Octave configuration working for QOP222 and qm-qua==1.1.5 and newer.
"""

from pathlib import Path
import numpy as np
import os
from qm.octave import QmOctaveConfig, ClockType, ClockFrequency
from octave_sdk.octave import ClockInfo
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

# The Octave port is 11xxx, where xxx are the last three digits of the Octave internal IP that can be accessed from
# the OPX admin panel if you QOP version is >= QOP220. Otherwise, it is 50 for Octave1, then 51, 52 and so on.
octave_config = QmOctaveConfig()
octave_config.set_calibration_db(os.getcwd())
octave_config.add_device_info("octave1", qop_ip, 11050, ClockInfo(ClockType.Internal, ClockFrequency.MHZ_10))

#####################
# OPX configuration #
#####################

# Continuous wave
const_len = 100
const_amp = 0.1

#############################################
#                Resonators                 #
#############################################
resonator_LO = 4.8 * u.GHz
resonator_IF = 60 * u.MHz

readout_len = 5000
readout_amp = 0.2

time_of_flight = 24
depletion_time = 2 * u.us

opt_weights = False
if opt_weights:
    from qualang_tools.config.integration_weights_tools import convert_integration_weights

    weights = np.load("optimal_weights.npz")
    opt_weights_real = convert_integration_weights(weights["weights_real"])
    opt_weights_minus_imag = convert_integration_weights(weights["weights_minus_imag"])
    opt_weights_imag = convert_integration_weights(weights["weights_imag"])
    opt_weights_minus_real = convert_integration_weights(weights["weights_minus_real"])
else:
    opt_weights_real = [(1.0, readout_len)]
    opt_weights_minus_imag = [(1.0, readout_len)]
    opt_weights_imag = [(1.0, readout_len)]
    opt_weights_minus_real = [(1.0, readout_len)]

##########################################
#               Flux line                #
##########################################
flux_IF = 100

max_frequency_point = 0.0
flux_settle_time = 100 * u.ns

# Resonator frequency versus flux fit parameters according to resonator_spec_vs_flux
# amplitude * np.cos(2 * np.pi * frequency * x + phase) + offset
amplitude_fit, frequency_fit, phase_fit, offset_fit = [0, 0, 0, 0]

# FLux pulse parameters
const_flux_len = 200
const_flux_amp = 0.45

# IQ Plane Angle
rotation_angle = (0 / 180) * np.pi
# Threshold for single shot g-e discrimination
ge_threshold = 0.0

#############################################
#                  Config                   #
#############################################
config = {
    "version": 1,
    "controllers": {
        "con1": {
            "analog_outputs": {
                1: {"offset": 0.0},  # I resonator
                2: {"offset": 0.0},  # Q resonator
                3: {"offset": 0.0},  # I qubit
                4: {"offset": 0.0},  # Q qubit
                5: {"offset": max_frequency_point},  # flux line
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
        "FTR": {
            "RF_inputs": {"port": ("octave1", 1)},
            "RF_outputs": {"port": ("octave1", 1)},
            "intermediate_frequency": resonator_IF,
            "operations": {
                "cw": "const_pulse",
                "readout": "readout_pulse",
            },
            "time_of_flight": time_of_flight,
            "smearing": 0,
        },
        "flux_line": {
            "singleInput": {
                "port": ("con1", 5),
            },
            "intermediate_frequency": flux_IF,
            "operations": {
                "const": "const_flux_pulse",
            },
        },
        "flux_line_sticky": {
            "singleInput": {
                "port": ("con1", 5),
            },
            "intermediate_frequency": flux_IF,
            "sticky": {"analog": True, "duration": 20},
            "operations": {
                "const": "const_flux_pulse",
            },
        },
    },
    "octaves": {
        "octave1": {
            "RF_outputs": {
                1: {
                    "LO_frequency": resonator_LO,
                    "LO_source": "internal",
                    "output_mode": "always_on",
                    "gain": 0,
                },
            },
            "RF_inputs": {
                1: {
                    "LO_frequency": resonator_LO,
                    "LO_source": "internal",
                },
            },
            "connectivity": "con1",
        }
    },
    "pulses": {
        "const_single_pulse": {
            "operation": "control",
            "length": const_len,
            "waveforms": {
                "single": "const_wf",
            },
        },
        "const_flux_pulse": {
            "operation": "control",
            "length": const_flux_len,
            "waveforms": {
                "single": "const_flux_wf",
            },
        },
        "const_pulse": {
            "operation": "control",
            "length": const_len,
            "waveforms": {
                "I": "const_wf",
                "Q": "zero_wf",
            },
        },
        "readout_pulse": {
            "operation": "measurement",
            "length": readout_len,
            "waveforms": {
                "I": "readout_wf",
                "Q": "zero_wf",
            },
            "integration_weights": {
                "cos": "cosine_weights",
                "sin": "sine_weights",
                "minus_sin": "minus_sine_weights",
                "rotated_cos": "rotated_cosine_weights",
                "rotated_sin": "rotated_sine_weights",
                "rotated_minus_sin": "rotated_minus_sine_weights",
                "opt_cos": "opt_cosine_weights",
                "opt_sin": "opt_sine_weights",
                "opt_minus_sin": "opt_minus_sine_weights",
            },
            "digital_marker": "ON",
        },
    },
    "waveforms": {
        "const_wf": {"type": "constant", "sample": const_amp},
        "const_flux_wf": {"type": "constant", "sample": const_flux_amp},
        "zero_wf": {"type": "constant", "sample": 0.0},
        "readout_wf": {"type": "constant", "sample": readout_amp},
    },
    "digital_waveforms": {
        "ON": {"samples": [(1, 0)]},
    },
    "integration_weights": {
        "cosine_weights": {
            "cosine": [(1.0, readout_len)],
            "sine": [(0.0, readout_len)],
        },
        "sine_weights": {
            "cosine": [(0.0, readout_len)],
            "sine": [(1.0, readout_len)],
        },
        "minus_sine_weights": {
            "cosine": [(0.0, readout_len)],
            "sine": [(-1.0, readout_len)],
        },
        "opt_cosine_weights": {
            "cosine": opt_weights_real,
            "sine": opt_weights_minus_imag,
        },
        "opt_sine_weights": {
            "cosine": opt_weights_imag,
            "sine": opt_weights_real,
        },
        "opt_minus_sine_weights": {
            "cosine": opt_weights_minus_imag,
            "sine": opt_weights_minus_real,
        },
        "rotated_cosine_weights": {
            "cosine": [(np.cos(rotation_angle), readout_len)],
            "sine": [(np.sin(rotation_angle), readout_len)],
        },
        "rotated_sine_weights": {
            "cosine": [(-np.sin(rotation_angle), readout_len)],
            "sine": [(np.cos(rotation_angle), readout_len)],
        },
        "rotated_minus_sine_weights": {
            "cosine": [(np.sin(rotation_angle), readout_len)],
            "sine": [(-np.cos(rotation_angle), readout_len)],
        },
    },
}
