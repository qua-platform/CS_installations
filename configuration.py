"""
QUA-Config supporting OPX+ & Octave
"""

from pathlib import Path

import numpy as np
import plotly.io as pio
from qm.octave import QmOctaveConfig
from qualang_tools.units import unit
from scipy.signal.windows import gaussian

pio.renderers.default = "browser"
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

#############
# Save Path #
#############
# Path to save data
save_dir = Path(__file__).parent.resolve() / "Data"
save_dir.mkdir(exist_ok=True)

#####################
# OPX configuration #
#####################

octave_config = QmOctaveConfig()
octave_config.set_calibration_db(str(Path(__file__).parent.resolve()))


#############################################
#                Resonators                 #
#############################################
resonator_LO = 5.5 * u.GHz
resonator_IF = 60 * u.MHz

readout_len = 1000
readout_amp = 0.125

const_amp = 0.2

time_of_flight = 24
depletion_time = 2 * u.us

#############################################
#                Fast DC gate               #
#############################################
gaussian_len = 60

gaussian_waveform = (0.4 * gaussian(gaussian_len, gaussian_len / 8)).tolist()

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
                3: {"offset": 0.0},  # Fast DC gate
            },
            "digital_outputs": {
                1: {},
                2: {},
                3: {},
            },
            "analog_inputs": {
                1: {"offset": 0.0, "gain_db": 0},  # I from down-conversion
                2: {"offset": 0.0, "gain_db": 0},  # Q from down-conversion
            },
        }
    },
    "elements": {
        "resonator": {
            "RF_inputs": {"port": ("oct1", 1)},
            "RF_outputs": {"port": ("oct1", 1)},
            "intermediate_frequency": resonator_IF,
            "operations": {
                "cw": "const_pulse",
                "readout": "readout_pulse",
            },
            "time_of_flight": time_of_flight,
            "smearing": 0,
        },
        "fast_dc_gate": {
            "singleInput": {"port": ("con1", 3)},
            "operations": {
                "square": "square_pulse",
                "gaussian": "gaussian_pulse",
            },
        },
        "qdac_trigger_1": {
            "digitalInputs": {
                "trig": {
                    "port": ("con1", 1),
                    "delay": 0,
                    "buffer": 0,
                },
            },
            "operations": {
                "trigger": "trigger_pulse",
            },
        },
        "qdac_trigger_2": {
            "digitalInputs": {
                "trig": {
                    "port": ("con1", 2),
                    "delay": 0,
                    "buffer": 0,
                },
            },
            "operations": {
                "trigger": "trigger_pulse",
            },
        },
        "qdac_trigger_3": {
            "digitalInputs": {
                "trig": {
                    "port": ("con1", 3),
                    "buffer": 0,
                    "delay": 0,
                },
            },
            "operations": {
                "trigger": "trigger_pulse",
            },
        },
    },
    "octaves": {
        "oct1": {
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
                    "IF_mode_I": "direct",
                    "IF_mode_Q": "off",
                },
            },
            "connectivity": "con1",
        }
    },
    "pulses": {
        "const_pulse": {
            "operation": "control",
            "length": readout_len,
            "waveforms": {
                "I": "const_wf",
                "Q": "zero_wf",
            },
        },
        "square_pulse": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "single": "square_wf",
            },
        },
        "gaussian_pulse": {
            "operation": "control",
            "length": gaussian_len,
            "waveforms": {
                "single": "gaussian_wf",
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
            },
            "digital_marker": "ON",
        },
        "trigger_pulse": {
            "operation": "control",
            "length": 100,
            "digital_marker": "ON",
        },
    },
    "waveforms": {
        "const_wf": {"type": "constant", "sample": const_amp},
        "square_wf": {"type": "constant", "sample": 0.3},
        "gaussian_wf": {"type": "arbitrary", "samples": gaussian_waveform},
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
    },
}
