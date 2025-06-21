"""
Configuration file for DQD measurements with an LF-FEM and Octave

See the "README" file for the relevant python requirements.
"""
import os

import numpy as np
from qualang_tools.units import unit
from qualang_tools.voltage_gates import VoltageGateSequence
from pathlib import Path

######################
# Network parameters #
######################
qop_ip = "127.0.0.1"  # Write the QM router IP address
cluster_name = None  # Write your cluster_name if version >= QOP220
qop_port = None  # Write the QOP port if version < QOP220
# In QOP versions > 2.2.2, the Octave is automatically deteced by the QOP.
# For QOP versions <= 2.2.2, see Tutorials/intro-to-octave/qop 222 and below.
# Below you can specify the path for the Octave mixer calibration's database file.
octave_calibration_db_path = os.getcwd()

# Combined settings for initializing the QuantumMachinesManager
qmm_settings = dict(
    host=qop_ip, port=qop_port, cluster_name=cluster_name, octave_calibration_db_path=octave_calibration_db_path
)

# Path to save data
save_dir = Path(__file__).parent.resolve() / "Data"
save_dir.mkdir(exist_ok=True)


#####################
# OPX configuration #
#####################
con = "con1"  # name of the OPX1000
octave = "oct1"  # name of the connected Octave
fem = 1  # slot index of the lf-fem inside the chassis


######################
# QDAC-I parameters  #
######################
qdac_ip = "127.0.0.2"  # Write the QDAC instrument IP address here
qdac_channel_mapping = {
    "B20": 1, "P20": 2, "B21": 3,
    "B1": 9, "P1": 10, "B2": 11, "P2": 12, "B3": 13,
    "S2": 17,
}

######################
#       READOUT      #
######################
u = unit(coerce_to_integer=True)

# DC readout parameters
tia_iv_scale_factor = 1e-9  # from spec (Femto LCA-200-10G Transimpedance in A/V)
tia_bandwidth = 200  # in Hz, from spec
readout_amp = 0.0  # should be 0 since the OPX doesn't ouptut voltage when measuring transport current
readout_len = 0.1 * u.ms  # should be greater than the time-constant, which is 1 / (2*pi*bandwidth)
# Note: if average drain current exceeds 10mV, 4ms integration can lead to fixed-point overflow

lock_in_freq = 200 * u.Hz
lock_in_amp = 450 * u.mV
lock_in_length = 1 * u.ms

time_of_flight = 24

# RF parameters
qubit_LO = 13 * u.GHz
qubit_1_IF = 50 * u.MHz
qubit_2_IF = 50 * u.MHz


#######################
# DC PULSE PARAMETERS #
#######################
step_length = 16 * u.ns  # Will be replaced with sub-ns
P1_step_amp = 0.1  # in V
P2_step_amp = 0.1  # in V
SET_step_amp = 0.1  # in V

# Time to ramp down to zero for sticky elements in ns
hold_offset_duration = 4
bias_tee_cut_off_frequency = 10 * u.kHz

#############################################
#                  Config                   #
#############################################
config = {
    "version": 1,
    "controllers": {
        con: {
            "type": "opx1000",
            "fems":{
                fem: {
                    "analog_outputs": {
                        1: {"offset": 0.0, "upsampling_mode": "mw"},  # Qubit RF I-Quadrature
                        2: {"offset": 0.0, "upsampling_mode": "mw"},  # Qubit RF Q-Quadrature
                        3: {"offset": 0.0, "upsampling_mode": "pulse"},  # Plunger Gate Qubit 1 (P1)
                        4: {"offset": 0.0, "upsampling_mode": "pulse"},  # Plunger Gate Qubit 2 (P2)
                        5: {"offset": 0.0, "upsampling_mode": "pulse"},  # SET Plunger Gate (P20)
                        6: {"offset": 0.0, "upsampling_mode": "pulse"},  # Source Gate (S2)
                    },
                    "digital_outputs": {
                        1: {},  # Octave Trigger
                    },
                    "analog_inputs": {
                        1: {"offset": 0.0, "gain_db": 0},  # Source Gate TIA
                    },
                }
            }
        },
    },
    "elements": {
        "qubit_1": {
            "RF_inputs": {"port": ("oct1", 1)},
            "intermediate_frequency": qubit_1_IF,
            "operations": {
            },
        },
        "qubit_2": {
            "RF_inputs": {"port": ("oct1", 1)},
            "intermediate_frequency": qubit_2_IF,
            "operations": {
            },
        },
        "P1": {
            "singleInput": {
                "port": (con, fem, 3),
            },
            "operations": {
                "step": "P1_step_pulse",
            },
        },
        "P1_sticky": {
            "singleInput": {
                "port": (con, fem, 3),
            },
            "sticky": {"analog": True, "duration": hold_offset_duration},
            "operations": {
                "step": "P1_step_pulse",
            },
        },
        "P2": {
            "singleInput": {
                "port": (con, fem, 4),
            },
            "operations": {
                "step": "P2_step_pulse",
            },
        },
        "P2_sticky": {
            "singleInput": {
                "port": (con, fem, 4),
            },
            "sticky": {"analog": True, "duration": hold_offset_duration},
            "operations": {
                "step": "P1_step_pulse",
            },
        },
        "SET": {
            "singleInput": {
                "port": (con, fem, 5),
            },
            "operations": {
                "step": "SET_step_pulse",
            },
        },
        "SET_sticky": {
            "singleInput": {
                "port": (con, fem, 5),
            },
            "sticky": {"analog": True, "duration": hold_offset_duration},
            "operations": {
                "step": "SET_step_pulse",
            },
        },
        "source_tia": {
            "singleInput": {
                "port": (con, fem, 1),  # won't be used
            },
            "operations": {
                "readout": "readout_pulse",
            },
            "outputs": {
                "out1": (con, fem, 1),
            },
            "time_of_flight": time_of_flight,
            "smearing": 0,
        },
        "source_tia_lock_in": {
            "singleInput": {
                "port": (con, fem, 1),
            },
            "intermediate_frequency": lock_in_freq,
            "operations": {
                "readout": "lock_in_pulse",
            },
            "outputs": {
                "out1": (con, fem, 1),
            },
            "time_of_flight": time_of_flight,
            "smearing": 0,
        },
    },
    "octaves": {
        "oct1": {
            "RF_outputs": {
                1: {
                    "LO_frequency": qubit_LO,
                    "LO_source": "internal",
                    "output_mode": "always_on",
                    "gain": 0,
                }
            },
            "connectivity": (con, fem),
        }
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
        "SET_step_pulse": {
            "operation": "control",
            "length": step_length,
            "waveforms": {
                "single": "SET_step_wf",
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
        "SET_step_wf": {"type": "constant", "sample": SET_step_amp},
        "lock_in_wf": {"type": "constant", "sample": lock_in_amp},
        "readout_pulse_wf": {"type": "constant", "sample": readout_amp},
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
            "cosine": [(1.0, lock_in_length)],
            "sine": [(0.0, lock_in_length)],
        },
        "sine_weights": {
            "cosine": [(0.0, lock_in_length)],
            "sine": [(1.0, lock_in_length)],
        },
    },
}
