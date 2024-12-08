# %%
import numpy as np
from scipy.signal.windows import gaussian
from qualang_tools.units import unit
from qm.qua._dsl import QuaVariable, QuaExpression
from qm.qua import declare, assign, play, fixed, Cast, amp, wait, ramp, ramp_to_zero
from typing import Union

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
const_amp = 0.3  # in V
const_len = 100  # in ns

#############################################
#                  Config                   #
#############################################
config = {
    "version": 1,
    "controllers": {
        "con1": {
            "analog_outputs": {
                1: {"offset": 0.0},  # qubit
                2: {"offset": 0.0},  # RF reflectometry
            },
            "digital_outputs": {},
            "analog_inputs": {
                1: {"offset": 0.0, "gain_db": 0},  # RF reflectometry input
                2: {"offset": 0.0, "gain_db": 0},  # DC readout input
            },
        },
    },
    "elements": {
        "qubit": {
            "singleInput": {
                "port": ("con1", 1),
            },
            "intermediate_frequency": qubit_IF,
            "operations": {
                "const": "const_pulse",
                "x90": "const_pulse",
                "y90": "const_pulse",
            },
        },
        "tank_circuit": {
            "singleInput": {
                "port": ("con1", 2),
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
