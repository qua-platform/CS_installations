# %%
import os
from pathlib import Path
import numpy as np
from qualang_tools.config.waveform_tools import drag_gaussian_pulse_waveforms
from qualang_tools.units import unit
import copy

#######################
# AUXILIARY FUNCTIONS #
#######################
u = unit(coerce_to_integer=True)

######################
# Network parameters #
######################
qop_ip = "172.16.33.100"  # Simulator
qop_port = 9515  # Write the QOP port if version < QOP220
cluster_name = None   # Write your cluster_name if version >= QOP220
#
qop_ip = "192.168.10.32"  # Akiva OPX1000
cluster_name = "Beta6"  # Write your cluster_name if version >= QOP220
qop_port = None  # Write the QOP port if version < QOP220

# Path to save data
save_dir = Path().absolute() / "data"

#####################
# OPX configuration #
#####################

digital_pulse_len = 100
# Continuous wave
const_len = 100
const_amp = 0.2
# Square wave
square_up_len = 500
square_down_len = 500
square_amp = 0.5
# Arbitrary pulse
arb_len = 40
arb_amp = 0.5
arb_wf = drag_gaussian_pulse_waveforms(arb_amp, arb_len, arb_len//5, 0.0, 50e6, 0)[0]

##########################################
#                Readout                 #
##########################################
intermediate_frequency = 1 * u.MHz

readout_len = 5000
readout_amp = 0.1

time_of_flight = 24 + 120
depletion_time = 2 * u.us

# IQ Plane Angle
rotation_angle = (0 / 180) * np.pi

# MARK: CONFIGURATION
#############################################
#                  Config                   #
#############################################
def get_config(sampling_rate = 1e9):
    config = {
        "version": 1,
        "controllers": {
            "con1": {
                "type": "opx1000",
                "fems": {
                    1: {
                        "type": "MW",
                        "analog_outputs": {
                            1: {"sampling_rate": sampling_rate, "full_scale_power_dbm": -11, "band": 2, "delay": 0}, # RL2  0.5V => 4dbm +[+6, -45] 3db spacing -11, -8, -5, -2, 1, 4, 7, 10
                        },
                    },
                    2: {
                        "type": "LF",
                        "analog_outputs": {
                            1: {"offset": 0.0, "sampling_rate": sampling_rate, "output_mode": "direct", "delay": 0},  # , "filter": {"feedforward": [], "feedback": []}
                            2: {"offset": 0.0, "sampling_rate": sampling_rate, "output_mode": "amplified", "delay": 0},
                            3: {"offset": 0.0, "sampling_rate": sampling_rate, "output_mode": "direct", "delay": 0},
                            4: {"offset": 0.0, "sampling_rate": sampling_rate, "output_mode": "direct", "delay": 0},
                            5: {"offset": 0.0, "sampling_rate": sampling_rate, "output_mode": "direct", "delay": 0},
                        },
                        "analog_inputs": {
                            1: {"offset": 0.0, "sampling_rate": int(sampling_rate), "gain_db": 0},
                            2: {"offset": 0.0, "sampling_rate": int(sampling_rate), "gain_db": 0},
                        },
                        "digital_outputs": {
                            1: {},
                        },
                    },
                },
            },
        },
        "elements": {
            "mw_element_1": {
                "MWInput": {
                    "port": ("con1", 1, 1),
                    "oscillator_frequency": 5e9,
                },
                "intermediate_frequency": 50e6,
                "operations": {
                    "const": "const_pulse_mw",
                },
            },
            "lf_element_1": {
                "singleInput": {
                    "port": ("con1", 2, 1),
                },
                "intermediate_frequency": intermediate_frequency,
                "operations": {
                    "const": "const_single_pulse",
                    "arbitrary": "arbitrary_pulse",
                    "up": "up_pulse",
                    "down": "down_pulse",
                },
            },
            "lf_element_2": {
                "singleInput": {
                    "port": ("con1", 2, 2),
                },
                "intermediate_frequency": 0,
                "operations": {
                    "const": "const_single_pulse",
                    "arbitrary": "arbitrary_pulse",
                    "up": "up_pulse",
                    "down": "down_pulse",
                },
            },
            "scope_trigger": {
                "singleInput": {
                    "port": ("con1", 2, 3),
                },
                "operations": {
                    "const": "const_single_pulse",
                },
            },
            "mdac_trigger": {
                "digitalInputs": {
                    'in0': {
                        'port': ("con1", 2, 1),
                        'delay': 0,
                        'buffer': 0,
                    },
                },
                "operations": {
                    "trigger": "switchON_pulse",
                },
            },
            "lf_readout_element": {
                "singleInput": {
                    "port": ("con1", 2, 4),
                },
                "intermediate_frequency": intermediate_frequency,
                "operations": {
                    "readout": "readout_pulse",
                },
                "outputs": {
                    "out1": ("con1", 2, 1),
                },
                "time_of_flight": time_of_flight,
                "smearing": 0,
            },
            "lf_readout_element_twin": {
                "singleInput": {
                    "port": ("con1", 2, 4),
                },
                "intermediate_frequency": intermediate_frequency,
                "operations": {
                    "readout": "readout_pulse",
                },
                "outputs": {
                    "out1": ("con1", 2, 1),
                },
                "time_of_flight": time_of_flight,
                "smearing": 0,
            },
            "dc_readout_element": {
                "singleInput": {
                    "port": ("con1", 2, 5),
                },
                "operations": {
                    "readout": "dc_readout_pulse",
                },
                "outputs": {
                    "out1": ("con1", 2, 1),
                    "out2": ("con1", 2, 2),
                },
                "time_of_flight": time_of_flight,
                "smearing": 0,
            },
            "dc_readout_element_twin": {
                "singleInput": {
                    "port": ("con1", 2, 5),
                },
                "operations": {
                    "readout": "dc_readout_pulse",
                },
                "outputs": {
                    "out1": ("con1", 2, 1),
                    "out2": ("con1", 2, 2),
                },
                "time_of_flight": time_of_flight,
                "smearing": 0,
            },

        },
        "pulses": {
            "arbitrary_pulse": {
                "operation": "control",
                "length": int(arb_len * 1e9 / sampling_rate),
                "waveforms": {
                    "single": "arbitrary_wf",
                },
            },
            "bias_pulse": {
                "operation": "control",
                "length": 16,
                "waveforms": {
                    "single": "bias_wf",
                },
            },
            "up_pulse": {
                "operation": "control",
                "length": square_up_len,
                "waveforms": {
                    "single": "up_wf",
                },
            },
            "down_pulse": {
                "operation": "control",
                "length": square_down_len,
                "waveforms": {
                    "single": "down_wf",
                },
            },
            "const_single_pulse": {
                "operation": "control",
                "length": const_len,
                "waveforms": {
                    "single": "const_wf",
                },
            },
            "trigger_pulse": {
                "operation": "control",
                "length": 1000,
                "digital_marker": "ON",
            },
            "const_pulse_mw": {
                "operation": "control",
                "length": const_len,
                "waveforms": {
                    "I": "const_wf",
                    "Q": "zero_wf",
                },
            },
            "switchON_pulse": {
                "operation": "control",
                "length": digital_pulse_len,
                "digital_marker": "ON",
            },
            "switchOFF_pulse": {
                "operation": "control",
                "length": digital_pulse_len,
                "digital_marker": "OFF",
            },
            "readout_pulse": {
                "operation": "measurement",
                "length": readout_len,
                "waveforms": {
                    "single": "readout_wf",
                },
                "integration_weights": {
                    "cos": "cosine_weights",
                    "sin": "sine_weights",
                    "minus_sin": "minus_sine_weights",
                    "rotated_cos": "rotated_cosine_weights",
                    "rotated_sin": "rotated_sine_weights",
                    "rotated_minus_sin": "rotated_minus_sine_weights",
                },
                "digital_marker": "ON",
            },
            "dc_readout_pulse": {
                "operation": "measurement",
                "length": readout_len,
                "waveforms": {
                    "single": "dc_readout_wf",
                },
                "integration_weights": {
                    "const": "const_weights",
                },
                "digital_marker": "ON",
            },
        },
        "waveforms": {
            "zero_wf": {"type": "constant", "sample": 0.0},
            "const_wf": {"type": "constant", "sample": const_amp},
            "bias_wf": {"type": "constant", "sample": 0.25},
            "up_wf": {"type": "constant", "sample": square_amp},
            "down_wf": {"type": "constant", "sample": -square_amp},
            "readout_wf": {"type": "constant", "sample": readout_amp},
            "dc_readout_wf": {"type": "constant", "sample": readout_amp},
            "arbitrary_wf": {"type": "arbitrary", "samples": arb_wf, "sampling_rate": sampling_rate},

        },
        "digital_waveforms": {
            "ON": {"samples": [(1, 0)]},
            "OFF": {"samples": [(0, 0)]},
        },
        "integration_weights": {
            "const_weights": {
                "cosine": [(1.0, readout_len)],
                "sine": [(0.0, readout_len)],
            },
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
    if sampling_rate == 1e9:
        config["elements"]["lf_element_1_sticky"] = {
            "singleInput": {
                "port": ("con1", 2, 1),
            },
            "intermediate_frequency": 0,
            "operations": {
                "const": "const_single_pulse",
                "bias": "bias_pulse",
                "arbitrary": "arbitrary_pulse",
                "up": "up_pulse",
                "down": "down_pulse",
            },
            'sticky': {
                'analog': True,
                'duration': 200
            },
        }
        config["elements"]["lf_element_2_sticky"] = {
            "singleInput": {
                "port": ("con1", 2, 2),
            },
            "intermediate_frequency": 0,
            "operations": {
                "const": "const_single_pulse",
                "bias": "bias_pulse",
                "arbitrary": "arbitrary_pulse",
                "up": "up_pulse",
                "down": "down_pulse",
            },
            'sticky': {
                'analog': True,
                'duration': 200
            },
        }
    return config

