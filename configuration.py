"""
Configuration file for DC/Lock-in/Reflectometry measurements.
See the "README" file for the relevant python requirements.
"""
import numpy as np
from qualang_tools.units import unit


######################
# Network parameters #
######################
qop_ip = "172.16.33.101"  # Write the QM router IP address
cluster_name = "Cluster_83"  # Write your cluster_name if version >= QOright_plunger20
qop_port = None  # Write the QOP port if version < QOright_plunger20

######################
# QDAC-II parameters #
######################
qdac_ip = "127.0.0.2"  # Write the QDAC instrument IP address here
qdac_source_gate_ch = 9
qdac_left_plunger_ch = 10
qdac_right_plunger_ch = 11  # if only one plunger, use this channel!

######################
#       READOUT      #
######################
u = unit(coerce_to_integer=True)

# DC readout parameters
tia_iv_scale_factor = 1e-10  # from spec (Femto LCA-200-10G Transimpedance in A/V)
tia_bandwidth = 200  # in Hz, from spec
readout_amp = 0.0  # should be 0 since the OPX doesn't ouptut voltage when measuring transport current
readout_len = 4 * u.ms  # should be greater than the time-constant, which is 1 / (2*pi*bandwidth)
# Note: if average drain current exceeds 10mV, 4ms integration can lead to fixed-point overflow

lock_in_freq = 1 * u.MHz
lock_in_amp = 10 * u.mV
lock_in_length = 10 * u.us

# RF-Reflectometry readout parameters
rf_readout_length = 1 * u.us

source_resonator_IF = 300 * u.MHz
source_rf_readout_amp = 30 * u.mV

plunger_resonator_IF = 300 * u.MHz
plunger_rf_readout_amp = 30 * u.mV

# Time of flight
time_of_flight = 24


#######################
# DC PULSE PARAMETERS #
#######################
step_length = 16 * u.ns  # Will be replaced with sub-ns
left_plunger_step_amp = 0.1  # in V
right_plunger_step_amp = 0.1  # in V

#############################################
#                  Config                   #
#############################################
config = {
    "version": 1,
    "controllers": {
        "con1": {
            "analog_outputs": {
                1: {"offset": 0.0},  # Source gate RF-reflectometry
                2: {"offset": 0.0},  # Plunger gate RF-reflectometry
            },
            "digital_outputs": {
                1: {},
                2: {},
            },
            "analog_inputs": {
                1: {"offset": 0.0, "gain_db": 0},  # Source gate RF-input/Drain DC-input
                2: {"offset": 0.0, "gain_db": 0},  # Plunger gate RF-input
            },
        },
    },
    "elements": {
        "left_plunger": {
            "singleInput": {
                "port": ("con1", 1),
            },
            "operations": {
                "step": "left_plunger_step_pulse",
            },
        },
        "right_plunger": {
            "singleInput": {
                "port": ("con1", 2),
            },
            "operations": {
                "step": "right_plunger_step_pulse",
            },
        },
        "source_resonator": {
            "singleInput": {
                "port": ("con1", 1),
            },
            "intermediate_frequency": source_resonator_IF,
            "operations": {
                "readout": "source_rf_readout_pulse",
            },
            "outputs": {
                "out1": ("con1", 1),
            },
            "time_of_flight": time_of_flight,
            "smearing": 0,
        },
        "plunger_resonator": {
            "singleInput": {
                "port": ("con1", 2),
            },
            "intermediate_frequency": plunger_resonator_IF,
            "operations": {
                "readout": "plunger_rf_readout_pulse",
            },
            "outputs": {
                "out1": ("con1", 2),
            },
            "time_of_flight": time_of_flight,
            "smearing": 0,
        },
        "drain_tia": {
            "singleInput": {
                "port": ("con1", 1),  # won't be used
            },
            "operations": {
                "readout": "readout_pulse",
            },
            "outputs": {
                "out1": ("con1", 1),
            },
            "time_of_flight": time_of_flight,
            "smearing": 0,
        },
        "drain_tia_lock_in": {
            "singleInput": {
                "port": ("con1", 1),
            },
            "intermediate_frequency": lock_in_freq,
            "operations": {
                "readout": "lock_in_pulse",
            },
            "outputs": {
                "out1": ("con1", 1),
            },
            "time_of_flight": time_of_flight,
            "smearing": 0,
        },
    },
    "pulses": {
        "left_plunger_step_pulse": {
            "operation": "control",
            "length": step_length,
            "waveforms": {
                "single": "left_plunger_step_wf",
            },
        },
        "right_plunger_step_pulse": {
            "operation": "control",
            "length": step_length,
            "waveforms": {
                "single": "right_plunger_step_wf",
            },
        },
        "lock_in_pulse": {
            "operation": "measurement",
            "length": lock_in_length,
            "waveforms": {
                "single": "lock_in_wf",
            },
            "integration_weights": {
                "cos": "cosine_weights",
                "sin": "sine_weights",
            },
            "digital_marker": "ON",
        },
        "source_rf_readout_pulse": {
            "operation": "measurement",
            "length": rf_readout_length,
            "waveforms": {
                "single": "source_rf_wf",
            },
            "integration_weights": {
                "cos": "cosine_weights",
                "sin": "sine_weights",
            },
            "digital_marker": "ON",
        },
        "plunger_rf_readout_pulse": {
            "operation": "measurement",
            "length": rf_readout_length,
            "waveforms": {
                "single": "plunger_rf_wf",
            },
            "integration_weights": {
                "cos": "cosine_weights",
                "sin": "sine_weights",
            },
            "digital_marker": "ON",
        },
        "readout_pulse": {
            "operation": "measurement",
            "length": readout_len,
            "waveforms": {
                "single": "readout_pulse_wf",
            },
            "integration_weights": {
                "constant": "constant_weights",
            },
            "digital_marker": "ON",
        },
    },
    "waveforms": {
        "left_plunger_step_wf": {"type": "constant", "sample": left_plunger_step_amp},
        "right_plunger_step_wf": {"type": "constant", "sample": right_plunger_step_amp},
        "lock_in_wf": {"type": "constant", "sample": lock_in_amp},
        "readout_pulse_wf": {"type": "constant", "sample": readout_amp},
        "source_rf_wf": {"type": "constant", "sample": source_rf_readout_amp},
        "plunger_rf_wf": {"type": "constant", "sample": plunger_rf_readout_amp},
    },
    "digital_waveforms": {
        "ON": {"samples": [(1, 0)]},
    },
    "integration_weights": {
        "constant_weights": {
            "cosine": [(1, readout_len)],
            "sine": [(0.0, readout_len)],
        },
        "cosine_weights": {
            "cosine": [(1.0, rf_readout_length)],
            "sine": [(0.0, rf_readout_length)],
        },
        "sine_weights": {
            "cosine": [(0.0, rf_readout_length)],
            "sine": [(1.0, rf_readout_length)],
        },
    },
}
