"""
QUA-Config supporting OPX1000 w/ LF-FEM and Octave
"""

from pathlib import Path

import numpy as np
from qm.octave import QmOctaveConfig
from qualang_tools.units import unit
from qualang_tools.voltage_gates import VoltageGateSequence

######################
# Network parameters #
######################
qop_ip = "172.16.33.107"  # Write the QM router IP address
cluster_name = "Cluster_1"  # Write your cluster_name if version >= QOP220
qop_port = None  # Write the QOP port if version < QOP220

#####################
# OPX configuration #
#####################
con = "con1"
fem = 3  # Should be the LF-FEM index, e.g., 1

# Set octave_config to None if no octave are present
octave_config = None

########################
# Octave configuration #
########################

octave_config = QmOctaveConfig()
octave_config.set_calibration_db(Path().absolute())

#############################################
#              OPX PARAMETERS               #
#############################################
sampling_rate = int(1e9)  # or, int(2e9)

######################
#       READOUT      #
######################
u = unit(coerce_to_integer=True)

# Reflectometry
resonator_IF = 151 * u.MHz
readout_len = 1 * u.us
readout_amp = 0.125
resonator_LO = 5.5 * u.GHz

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
hold_offset_duration = 4

bias_tee_cut_off_frequency = 10 * u.kHz

#########################
#    QUBIT MW PULSES    #
#########################

qubit_LO = 5.5 * u.GHz

drive_amp = 0.125
drive_len = 1 * u.us

# Durations in ns
pi_length = 32
pi_half_length = 16
# Amplitudes in V
pi_amps = [0.27, -0.27]
pi_half_amps = [0.27, -0.27]


#############################################
#                  Config                   #
#############################################
config = {
    "version": 1,
    "controllers": {
        con: {
            "type": "opx1000",
            "fems": {
                fem: {
                    "type": "LF",
                    "analog_outputs": {
                        # I readout
                        1: {
                            "offset": 0.0,
                            "output_mode": "direct",
                            "sampling_rate": sampling_rate,
                            "upsampling_mode": "mw",
                        },
                        # Q readout
                        2: {
                            "offset": 0.0,
                            "output_mode": "direct",
                            "sampling_rate": sampling_rate,
                            "upsampling_mode": "mw",
                        },
                        # I drive
                        3: {
                            "offset": 0.0,
                            "output_mode": "direct",
                            "sampling_rate": sampling_rate,
                            "upsampling_mode": "mw",
                        },
                        # Q drive
                        4: {
                            "offset": 0.0,
                            "output_mode": "direct",
                            "sampling_rate": sampling_rate,
                            "upsampling_mode": "mw",
                        },
                        # Plunger gate
                        5: {
                            "offset": 0.0,
                            "output_mode": "amplified",
                            "sampling_rate": sampling_rate,
                            "upsampling_mode": "pulse",
                        },
                    },
                    "digital_outputs": {
                        1: {},  # TTL for QDAC
                        2: {},  # TTL for QDAC
                    },
                    "analog_inputs": {
                        1: {"offset": 0.0, "gain_db": 0, "sampling_rate": sampling_rate},  # I readout input
                        2: {"offset": 0.0, "gain_db": 0, "sampling_rate": sampling_rate},  # Q readout input
                    },
                },
            },
        },
    },
    "elements": {
        "P1": {
            "singleInput": {
                "port": (con, fem, 5),
            },
            "operations": {
                "step": "P1_step_pulse",
                "pi": "P1_pi_pulse",
                "pi_half": "P1_pi_half_pulse",
            },
        },
        "P1_sticky": {
            "singleInput": {
                "port": (con, fem, 5),
            },
            "sticky": {"analog": True, "duration": hold_offset_duration},
            "operations": {
                "step": "P1_step_pulse",
            },
        },
        "resonator": {
            "RF_inputs": {"port": ("oct1", 1)},
            "RF_outputs": {"port": ("oct1", 1)},
            "intermediate_frequency": resonator_IF,
            "operations": {
                "readout": "readout_pulse",
            },
            "time_of_flight": time_of_flight,
            "smearing": 0,
        },
        "drive": {
            "RF_inputs": {"port": ("oct1", 2)},
            "intermediate_frequency": resonator_IF,
            "operations": {
                "saturation": "saturation_pulse",
            },
        },
        "qdac_trigger1": {
            "digitalInputs": {
                "trigger": {
                    "port": (con, fem, 1),
                    "delay": 0,
                    "buffer": 0,
                }
            },
            "operations": {
                "trigger": "trigger_pulse",
            },
        },
        "qdac_trigger2": {
            "digitalInputs": {
                "trigger": {
                    "port": (con, fem, 2),
                    "delay": 0,
                    "buffer": 0,
                }
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
                2: {
                    "LO_frequency": qubit_LO,
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
            "connectivity": (con, fem),
        }
    },
    "pulses": {
        "P1_pi_pulse": {
            "operation": "control",
            "length": pi_length,
            "waveforms": {
                "single": "P1_pi_wf",
            },
        },
        "P1_pi_half_pulse": {
            "operation": "control",
            "length": pi_half_length,
            "waveforms": {
                "single": "P1_pi_half_wf",
            },
        },
        "P1_step_pulse": {
            "operation": "control",
            "length": step_length,
            "waveforms": {
                "single": "P1_step_wf",
            },
        },
        "trigger_pulse": {
            "operation": "control",
            "length": 1000,
            "digital_marker": "ON",
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
        "saturation_pulse": {
            "operation": "control",
            "length": 1000,
            "waveforms": {
                "I": "saturation_wf",
                "Q": "zero_wf",
            },
        },
    },
    "waveforms": {
        "P1_pi_wf": {"type": "constant", "sample": pi_amps[0] - level_manip[0]},
        "P1_pi_half_wf": {"type": "constant", "sample": pi_half_amps[0] - level_manip[0]},
        "P1_step_wf": {"type": "constant", "sample": P1_step_amp},
        "readout_wf": {"type": "constant", "sample": readout_amp},
        "saturation_wf": {"type": "constant", "sample": drive_amp},
        "zero_wf": {"type": "constant", "sample": 0.0},
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
