"""
QUA-Config supporting OPX1000 w/ LF-FEM + MW-FEM
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
qop_ip = "172.16.33.115"  # Write the QM router IP address
cluster_name = "CS_3"  # Write your cluster_name if version >= QOP220
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

#####################
# OPX configuration #
#####################
con = "con1"
lf_fem = 5
mw_fem = 1
# Set octave_config to None if no octave are present
octave_config = None


#############################################
#                Resonators                 #
#############################################
resonator_LO = 6.35 * u.GHz
# Resonators IF
resonator_IF = 75 * u.MHz

resonator_power = 1  # power in dBm at waveform_amp = 1 (steps of 3 dB)

# Note: amplitudes can be -1..1 and are scaled up to `qubit_power` at amp=1
# Readout pulse parameters
readout_len = 4000
readout_amp = 0.35

time_of_flight = 28

#############################################
#                   Tests                   #
#############################################


test_full_scale_power = 1
test_LO = 2e9
test_IF = 133 * u.MHz


const_flux_len = 200
const_flux_amp = 0.45

const_len = 1000
const_amp = 0.1

saturation_len = 10 * u.us
saturation_amp = 0.35


rotation_angle = (0.0 / 180) * np.pi
rotation_angle_2 = (0.0 / 180) * np.pi
#############################################
#                  Config                   #
#############################################
config = {
    "version": 1,
    "controllers": {
        con: {
            "type": "opx1000",
            "fems": {
                mw_fem: {
                    "type": "MW",
                    "analog_outputs": {
                        # Resonator (If needed)
                        1: {
                            "band": 2,
                            "full_scale_power_dbm": resonator_power,
                            "upconverters": {1: {"frequency": resonator_LO}},
                        },
                        # Test Line
                        2: {
                            "band": 1,
                            "full_scale_power_dbm": test_full_scale_power,
                            "upconverters": {1: {"frequency": test_LO}},
                        },

                    },
                    "digital_outputs": {},
                    "analog_inputs": {
                        1: {"band": 2, "downconverter_frequency": resonator_LO},  # for down-conversion
                    },
                },
                lf_fem: {
                    "type": "LF",
                    "analog_outputs": {
                        # Test Line
                        1: {
                            "offset": 0,
                            "output_mode": "amplified",
                            "sampling_rate": 1e9,
                            "upsampling_mode": "pulse",
                            "delay": 141 * u.ns,
                        },

                    },
                    "digital_outputs": {
                        1: {},
                    },
                    "analog_inputs": {
                        1: {"offset": 0.0, "gain_db": 0, "sampling_rate": 1e9}
                    },
                },
            },
        }
    },
    "elements": {
        "MW_resonator": {
            "MWInput": {
                "port": (con, mw_fem, 1),
                "upconverter": 1,
            },
            "intermediate_frequency": resonator_IF,  # frequency at offset ch7
            "operations": {
                "cw": "const_pulse",
                "readout": "readout_pulse_1",
            },
            "MWOutput": {
                "port": (con, mw_fem, 1),
            },
            "time_of_flight": time_of_flight,
            "smearing": 0,
        },
        "MW_test": {
            "MWInput": {
                "port": (con, mw_fem, 8),
                "upconverter": 1,
            },
            "intermediate_frequency": test_IF,  # frequency at offset ch8
            "operations": {
                "cw": "const_pulse",
                "readout": "readout_pulse_2",
            },
            "MWOutput": {
                "port": (con, mw_fem, 2),
            },
            "time_of_flight": time_of_flight,
            "smearing": 0,
        },
        "LF_test_output": {
            "singleInput": {
                "port": (con, lf_fem, 1),
            },
            "operations": {
                "const": "const_pulse",
            },
        },
        "LF_resonator": {
            "singleInput": {
                "port": (con, lf_fem, 2),
            },
            "operations": {
                "const": "const_flux_pulse",
            },
            "outputs": {
                "port": (con, lf_fem, 1)
            } 
        },
    },
    "pulses": {
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
        "readout_pulse1": {
            "operation": "measurement",
            "length": readout_len,
            "waveforms": {
                "I": "readout_wf_1",
                "Q": "zero_wf",
            },
            "integration_weights": {
                "cos": "cosine_weights",
                "sin": "sine_weights",
                "minus_sin": "minus_sine_weights",
                "rotated_cos": "rotated_cosine_weights_q1",
                "rotated_sin": "rotated_sine_weights_q1",
                "rotated_minus_sin": "rotated_minus_sine_weights_q1"
            },
            "digital_marker": "ON",
        },
        "readout_pulse2": {
            "operation": "measurement",
            "length": readout_len,
            "waveforms": {
                "I": "readout_wf_2",
                "Q": "zero_wf",
            },
            "integration_weights": {
                "cos": "cosine_weights",
                "sin": "sine_weights",
                "minus_sin": "minus_sine_weights",
                "rotated_cos": "rotated_cosine_weights_q2",
                "rotated_sin": "rotated_sine_weights_q2",
                "rotated_minus_sin": "rotated_minus_sine_weights_q2",
            },
            "digital_marker": "ON",
        },
    },
    "waveforms": {
        "const_wf": {"type": "constant", "sample": const_amp},
        "saturation_wf": {"type": "constant", "sample": saturation_amp},
        "const_flux_wf": {"type": "constant", "sample": const_flux_amp},
        "zero_wf": {"type": "constant", "sample": 0.0},
        "readout_wf_2": {"type": "constant", "sample": readout_amp},
        "readout_wf_1": {"type": "constant", "sample": readout_amp},
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
        "rotated_cosine_weights_q1": {
            "cosine": [(np.cos(rotation_angle), readout_len)],
            "sine": [(np.sin(rotation_angle), readout_len)],
        },
        "rotated_sine_weights_q1": {
            "cosine": [(-np.sin(rotation_angle), readout_len)],
            "sine": [(np.cos(rotation_angle), readout_len)],
        },
        "rotated_minus_sine_weights_q1": {
            "cosine": [(np.sin(rotation_angle), readout_len)],
            "sine": [(-np.cos(rotation_angle), readout_len)],
        },
        "rotated_cosine_weights_q2": {
            "cosine": [(np.cos(rotation_angle_2), readout_len)],
            "sine": [(np.sin(rotation_angle_2), readout_len)],
        },
        "rotated_sine_weights_q2": {
            "cosine": [(-np.sin(rotation_angle_2), readout_len)],
            "sine": [(np.cos(rotation_angle_2), readout_len)],
        },
        "rotated_minus_sine_weights_q2": {
            "cosine": [(np.sin(rotation_angle_2), readout_len)],
            "sine": [(-np.cos(rotation_angle_2), readout_len)],
        },
    },
}
