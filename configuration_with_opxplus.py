# %%
from typing import Union

import numpy as np
from qm.qua import Cast, amp, assign, declare, fixed, play, ramp, ramp_to_zero, wait
from qm.qua._dsl import QuaExpression, QuaVariable
from qualang_tools.units import unit
from scipy.signal.windows import gaussian

#######################
# AUXILIARY FUNCTIONS #
#######################
u = unit(coerce_to_integer=True)


######################
# Network parameters #
######################
qop_ip = "172.16.33.101"  # Write the QM router IP address
cluster_name = "Cluster_83"  # Write your cluster_name if version >= QOP220
qop_port = None  # Write the QOP port if version < QOP220
octave_config = None


######################
#       READOUT      #
######################
# Reflectometry
resonator_IF = 150 * u.MHz
reflectometry_readout_len = 1 * u.us
reflectometry_readout_amp = 30 * u.mV

# Time of flight
time_of_flight = 28


######################
#    QUBIT PULSES    #
######################
qubit_IF = 0 * u.MHz

# CW pulse
const_len = 60  # in ns
const_amp = 0.4  # in V
PI_AMP = 0.3
PI_LEN = 52

#############################################
#                  Config                   #
#############################################
config = {
    "version": 1,
    "controllers": {
        "con1": {
            "analog_outputs": {
                1: {"offset": 0.0},  # qubit
                2: {"offset": 0.0},  # qubit
                3: {"offset": 0.0},  # RF reflectometry
            },
            "digital_outputs": {},
            "analog_inputs": {
                1: {"offset": 0.0, "gain_db": 0},  # RF reflectometry input
                2: {"offset": 0.0, "gain_db": 0},  # DC readout input
            },
        },
    },
    "elements": {
        "qubit1": {
            "singleInput": {
                "port": ("con1", 1),
            },
            "intermediate_frequency": qubit_IF,
            "operations": {
                "const": "const_pulse",
                "x180_square": f"square_x180_pulse",
                "x90_square": f"square_x90_pulse",
                "-x90_square": f"square_minus_x90_pulse",
                "y180_square": f"square_y180_pulse",
                "y90_square": f"square_y90_pulse",
                "-y90_square": f"square_minus_y90_pulse",
            },
        },
        "qubit1_trio1": {
            "singleInput": {
                "port": ("con1", 1),
            },
            "intermediate_frequency": qubit_IF,
            "operations": {
                "const": "const_pulse",
                "x180_square": f"square_x180_pulse_trio1",
                "x90_square": f"square_x90_pulse_trio1",
                "-x90_square": f"square_minus_x90_pulse_trio1",
                "y180_square": f"square_y180_pulse_trio1",
                "y90_square": f"square_y90_pulse_trio1",
                "-y90_square": f"square_minus_y90_pulse_trio1",
            },
        },
        "qubit1_trio2": {
            "singleInput": {
                "port": ("con1", 1),
            },
            "intermediate_frequency": qubit_IF,
            "operations": {
                "const": "const_pulse",
                "x180_square": f"square_x180_pulse_trio2",
                "x90_square": f"square_x90_pulse_trio2",
                "-x90_square": f"square_minus_x90_pulse_trio2",
                "y180_square": f"square_y180_pulse_trio2",
                "y90_square": f"square_y90_pulse_trio2",
                "-y90_square": f"square_minus_y90_pulse_trio2",
            },
        },
        "tank_circuit1": {
            "singleInput": {
                "port": ("con1", 3),
            },
            "intermediate_frequency": resonator_IF,
            "operations": {
                "readout": "reflectometry_readout_pulse",
            },
            "outputs": {
                "out1": ("con1", 1),
                "out2": ("con1", 2),
            },
            "time_of_flight": time_of_flight,
            "smearing": 0,
        },
    },
    "pulses": {
        "const_pulse": {
            "operation": "control",
            "length": const_len,
            "waveforms": {
                "single": "const_wf",
            },
        },
        "square_x180_pulse": {
            "operation": "control",
            "length": const_len,
            "waveforms": {
                "single": "x180_wf",
            },
        },
        "square_y180_pulse": {
            "operation": "control",
            "length": const_len,
            "waveforms": {
                "single": "y180_wf",
            },
        },
        "square_x90_pulse": {
            "operation": "control",
            "length": const_len,
            "waveforms": {
                "single": "x90_wf",
            },
        },
        "square_y90_pulse": {
            "operation": "control",
            "length": const_len,
            "waveforms": {
                "single": "y90_wf",
            },
        },
        "square_minus_x90_pulse": {
            "operation": "control",
            "length": const_len,
            "waveforms": {
                "single": "minus_x90_wf",
            },
        },
        "square_minus_y90_pulse": {
            "operation": "control",
            "length": const_len,
            "waveforms": {
                "single": "minus_y90_wf",
            },
        },
        "square_x180_pulse_trio1": {
            "operation": "control",
            "length": const_len,
            "waveforms": {
                "single": "x180_wf_trio1",
            },
        },
        "square_y180_pulse_trio1": {
            "operation": "control",
            "length": const_len,
            "waveforms": {
                "single": "y180_wf_trio1",
            },
        },
        "square_x90_pulse_trio1": {
            "operation": "control",
            "length": const_len,
            "waveforms": {
                "single": "x90_wf_trio1",
            },
        },
        "square_y90_pulse_trio1": {
            "operation": "control",
            "length": const_len,
            "waveforms": {
                "single": "y90_wf_trio1",
            },
        },
        "square_minus_x90_pulse_trio1": {
            "operation": "control",
            "length": const_len,
            "waveforms": {
                "single": "minus_x90_wf_trio1",
            },
        },
        "square_minus_y90_pulse_trio1": {
            "operation": "control",
            "length": const_len,
            "waveforms": {
                "single": "minus_y90_wf_trio1",
            },
        },
        "square_x180_pulse_trio2": {
            "operation": "control",
            "length": const_len,
            "waveforms": {
                "single": "x180_wf_trio2",
            },
        },
        "square_y180_pulse_trio2": {
            "operation": "control",
            "length": const_len,
            "waveforms": {
                "single": "y180_wf_trio2",
            },
        },
        "square_x90_pulse_trio2": {
            "operation": "control",
            "length": const_len,
            "waveforms": {
                "single": "x90_wf_trio2",
            },
        },
        "square_y90_pulse_trio2": {
            "operation": "control",
            "length": const_len,
            "waveforms": {
                "single": "y90_wf_trio2",
            },
        },
        "square_minus_x90_pulse_trio2": {
            "operation": "control",
            "length": const_len,
            "waveforms": {
                "single": "minus_x90_wf_trio2",
            },
        },
        "square_minus_y90_pulse_trio2": {
            "operation": "control",
            "length": const_len,
            "waveforms": {
                "single": "minus_y90_wf_trio2",
            },
        },
        "reflectometry_readout_pulse": {
            "operation": "measurement",
            "length": reflectometry_readout_len,
            "waveforms": {
                "single": "readout_pulse_wf",
            },
            "integration_weights": {
                "cos": "cosine_weights",
                "sin": "sine_weights",
            },
            "digital_marker": "ON",
        },
    },
    "waveforms": {
        "zero_wf": {"type": "constant", "sample": 0.0},
        "const_wf": {"type": "constant", "sample": const_amp},
        "x180_wf": {"type": "constant", "sample": PI_AMP},
        "y180_wf": {"type": "constant", "sample": PI_AMP},
        "x90_wf": {"type": "constant", "sample": PI_AMP},
        "y90_wf": {"type": "constant", "sample": PI_AMP},
        "minus_x90_wf": {"type": "constant", "sample": PI_AMP},
        "minus_y90_wf": {"type": "constant", "sample": PI_AMP},
        "x180_wf_trio1": {"type": "constant", "sample": 0.6 * PI_AMP},
        "y180_wf_trio1": {"type": "constant", "sample": 0.6 * PI_AMP},
        "x90_wf_trio1": {"type": "constant", "sample": 0.6 * PI_AMP},
        "y90_wf_trio1": {"type": "constant", "sample": 0.6 * PI_AMP},
        "minus_x90_wf_trio1": {"type": "constant", "sample": 0.6 * PI_AMP},
        "minus_y90_wf_trio1": {"type": "constant", "sample": 0.6 * PI_AMP},
        "x180_wf_trio2": {"type": "constant", "sample": 0.3 * PI_AMP},
        "y180_wf_trio2": {"type": "constant", "sample": 0.3 * PI_AMP},
        "x90_wf_trio2": {"type": "constant", "sample": 0.3 * PI_AMP},
        "y90_wf_trio2": {"type": "constant", "sample": 0.3 * PI_AMP},
        "minus_x90_wf_trio2": {"type": "constant", "sample": 0.3 * PI_AMP},
        "minus_y90_wf_trio2": {"type": "constant", "sample": 0.3 * PI_AMP},
        "readout_pulse_wf": {"type": "constant", "sample": reflectometry_readout_amp},
    },
    "digital_waveforms": {
        "ON": {"samples": [(1, 0)]},
    },
    "integration_weights": {
        "constant_weights": {
            "cosine": [(1, reflectometry_readout_len)],
            "sine": [(0.0, reflectometry_readout_len)],
        },
        "cosine_weights": {
            "cosine": [(1.0, reflectometry_readout_len)],
            "sine": [(0.0, reflectometry_readout_len)],
        },
        "sine_weights": {
            "cosine": [(0.0, reflectometry_readout_len)],
            "sine": [(1.0, reflectometry_readout_len)],
        },
    },
}

# %%
