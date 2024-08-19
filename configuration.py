"""
Configuration file for DC/Lock-in/Reflectometry measurements.
See the "README" file for the relevant python requirements.
"""
import numpy as np
from qualang_tools.units import unit


######################
# Network parameters #
######################
qop_ip = "127.0.0.1"  # Write the QM router IP address
cluster_name = "Cluster_1"  # Write your cluster_name if version >= QOP220
qop_port = None  # Write the QOP port if version < QOP220

######################
# QDAC-II parameters #
######################
qdac_ip = "127.0.0.2"  # Write the QDAC instrument IP address here
qdac_source_gate_ch = 9
qdac_left_plunger_ch = 10
qdac_right_plunger_ch = 11  # if only one plunger, use CH11!

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

lock_in_freq = 100 * u.kHz
lock_in_amp = 100 * u.mV
lock_in_length = 1 * u.ms

# RF-Reflectometry readout parameters
rf_readout_length = 1 * u.us

source_resonator_IF = 300 * u.MHz
source_rf_readout_amp = 30 * u.mV

plunger_resonator_IF = 300 * u.MHz
plunger_rf_readout_amp = 30 * u.mV

# Time of flight
time_of_flight = 24

######################
#      DC GATES      #
######################
## Section defining the points from the charge stability map - can be done in the config
# Relevant points in the charge stability map as ["P1", "P2"] in V
level_init = [0.1, -0.1]
level_manip = [0.2, -0.2]
level_readout = [0.12, -0.12]

# Duration of each step in ns
duration_init = 2500
duration_manip = 1000
duration_readout = readout_len + 100
duration_compensation_pulse = 4 * u.us

# Step parameters
step_length = 16  # in ns
P1_step_amp = 0.25  # in V
P2_step_amp = 0.25  # in V
charge_sensor_amp = 0.25  # in V

# Time to ramp down to zero for sticky elements in ns
hold_offset_duration = 4  # in ns
bias_tee_cut_off_frequency = 10 * u.kHz

######################
#    QUBIT PULSES    #
######################
qubit_LO = 4 * u.GHz
qubit_IF = 100 * u.MHz
qubit_g = 0.0
qubit_phi = 0.0

# Pi pulse
pi_amp = 0.25  # in V
pi_length = 32  # in ns
# Pi half
pi_half_amp = 0.25  # in V
pi_half_length = 16  # in ns
# CW pulse
cw_amp = 0.3  # in V
cw_len = 100  # in ns

#############################################
#                  Config                   #
#############################################
config = {
    "version": 1,
    "controllers": {
        "con1": {
            "analog_outputs": {
                1: {"offset": 0.0},  # Source gate RF-reflectometry
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
        "source_tank_circuit": {
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
        "plunger_tank_circuit": {
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
        "TIA": {
            "singleInput": {
                "port": ("con1", 1),
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
        "TIA_lock_in": {
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
        "P1_step_pulse": {
            "operation": "control",
            "length": step_length,
            "waveforms": {
                "single": "P1_step_wf",
            },
        },
        "P2_step_pulse": {
            "operation": "control",
            "length": step_length,
            "waveforms": {
                "single": "P2_step_wf",
            },
        },
        "bias_charge_pulse": {
            "operation": "control",
            "length": step_length,
            "waveforms": {
                "single": "charge_sensor_step_wf",
            },
        },
        "trigger_pulse": {
            "operation": "control",
            "length": 1000,
            "digital_marker": "ON",
        },
        "cw_pulse": {
            "operation": "control",
            "length": cw_len,
            "waveforms": {
                "I": "const_wf",
                "Q": "zero_wf",
            },
        },
        "pi_pulse": {
            "operation": "control",
            "length": pi_length,
            "waveforms": {
                "I": "pi_wf",
                "Q": "zero_wf",
            },
        },
        "pi_half_pulse": {
            "operation": "control",
            "length": pi_half_length,
            "waveforms": {
                "I": "pi_half_wf",
                "Q": "zero_wf",
            },
        },
        "source_rf_readout_pulse": {
            "operation": "measurement",
            "length": source_rf_readout_length,
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
        "P1_step_wf": {"type": "constant", "sample": P1_step_amp},
        "P2_step_wf": {"type": "constant", "sample": P2_step_amp},
        "charge_sensor_step_wf": {"type": "constant", "sample": charge_sensor_amp},
        "pi_wf": {"type": "constant", "sample": pi_amp},
        "pi_half_wf": {"type": "constant", "sample": pi_half_amp},
        "readout_pulse_wf": {"type": "constant", "sample": readout_amp},
        "source_reflect_wf": {"type": "constant", "sample": source_rf_readout_amp},
        "plunger_reflect_wf": {"type": "constant", "sample": plunger_rf_readout_amp},
        "const_wf": {"type": "constant", "sample": cw_amp},
        "zero_wf": {"type": "constant", "sample": 0.0},
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
