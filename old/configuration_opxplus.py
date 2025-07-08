"""
QUA-Config supporting OPX plus
"""

from pathlib import Path
import numpy as np
from scipy.signal.windows import gaussian
from qualang_tools.units import unit
from qm.qua import declare, assign, play, fixed, Cast, amp, wait, ramp, ramp_to_zero
from typing import Union


######################
# Network parameters #
######################
qop_ip = "172.16.33.101"  # Write the QM router IP address
# qop_ip = "fe80::d263:b4ff:fe04:beed"  # Write the QM router IP address
cluster_name = "CS_2"  # Write your cluster_name if version >= QOP220
qop_port = None # 9510  # Write the QOP port if version < QOP220
octave_config = None


#####################
# OPX configuration #
#####################
con = "con1"


#############
# Data Save #
#############

# Path to save data
save_dir = Path().absolute() / "data"
save_dir.mkdir(exist_ok=True)
default_additional_files = {
    "configuration_with_opxplus.py": "configuration_with_opxplus.py",
    "optimal_weights.npz": "optimal_weights.npz",
    "00_QDAC_initial.py": "00_QDAC_initial.py",
}


#############################################
#              OPX PARAMETERS               #
#############################################
sampling_rate = int(1e9)  # or, int(2e9)


######################
#       READOUT      #
######################
u = unit(coerce_to_integer=True)

# Reflectometry
# resonator_IF = 178 * u.MHz
# resonator_IF = 148 * u.MHz #R
resonator_IF = 186 * u.MHz #L

reflectometry_readout_length = 1 * u.us
readout_len = reflectometry_readout_length
measurement_delay = 300 * u.ns
reflectometry_readout_long_length = 200 * u.us
# reflectometry_readout_long_length = 0.5 * u.ms 
reflectometry_readout_long_length_trimmed = 0.5 * u.ms - measurement_delay

# reflectometry_readout_amp = 0.2 # V
# reflectometry_readout_amp = 0.4 # V
reflectometry_readout_amp = 0.0316 # V -20dB
# reflectometry_readout_amp = 0.316 # V

# Time of flight
time_of_flight = 240 # ns
# time_of_flight = 4 # ns

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
duration_readout = reflectometry_readout_length + 100
duration_compensation_pulse = 4 * u.us

# Step parameters
step_length = 1000  # in ns
P1_step_amp = 0.25  # in V
P2_step_amp = 0.25  # in V
charge_sensor_amp = 0.25  # in V

# Time to ramp down to zero for sticky elements in ns
hold_offset_duration = 1000  # in ns
bias_tee_cut_off_frequency = 10 * u.kHz

######################
#    QUBIT PULSES    #
######################
qubit_LO = 3 * u.GHz
qubit_IF = 100 * u.MHz
qubit_power = 1  # power in dBm at waveform amp = 1 (steps of 3 dB)

# Note: amplitudes can be -1..1 and are scaled up to `qubit_power` at amp=1
# Pi pulse
pi_amp = 0.25  # in arb.
pi_length = 32  # in ns
# Pi half
pi_half_amp = 0.25  # in arb.
pi_half_length = 16  # in ns
# Gaussian pulse
gaussian_amp = 0.3  # in arb.
gaussian_length = 20 * int(sampling_rate // 1e9)  # in units of [1/sampling_rate]
# CW pulse
cw_amp = 0.25  # in arb.
cw_len = 800  # in ns

p1_port = 7

#############################################
#                  Config                   #
#############################################
config = {
    "version": 1,
    "controllers": {
        con: {
            "analog_outputs": {
                1: {"offset": 0.0},  # P1
                2: {"offset": 0.0},  # P2
                3: {"offset": 0.0},  # T12
                # 3: {"offset": 0.0},  # EDSR I quadrature (Octave I2)
                # 4: {"offset": 0.0},  # EDSR Q quadrature (Octave Q2)
                # 5: {"offset": 0.0},  # Sensor gate
                9: {"offset": 0.0},  # RF reflectometry
            },
            "digital_outputs": {
                1: {},  # TTL for QDACa3
                2: {},  # TTL for QDACa4
                3: {},  # TTL for QDACb3
                4: {},  # TTL for QDACb4
                9: {},  # TTL for QDACa1
                10: {},  # TTL for QDACb1
            },
            "analog_inputs": {
                1: {"offset": 0.0, "gain_db": 0},  # RF reflectometry input
                2: {"offset": 0.0, "gain_db": 0},  
            },
        },
    },
    "elements": {
        "P1": {
            "singleInput": {
                "port": (con, 1),
            },
            "operations": {
                "step": "P1_step_pulse",
            },
        },
        "P1_sticky": {
            "singleInput": {
                "port": (con, 1),
            },
            "sticky": {"analog": True, "duration": hold_offset_duration},
            "operations": {
                "step": "P1_step_pulse",
            },
        },
        "P2": {
            "singleInput": {
                "port": (con, 2),
            },
            "operations": {
                "step": "P2_step_pulse",
            },
        },
        "P2_sticky": {
            "singleInput": {
                "port": (con, 2),
            },
            "sticky": {"analog": True, "duration": hold_offset_duration},
            "operations": {
                "step": "P2_step_pulse",
            },
        },
        "BC": {
            "singleInput": {
                "port": (con, 3),
            },
            "operations": {
                "step": "P2_step_pulse",
            },
        },
        "BC_sticky": {
            "singleInput": {
                "port": (con, 3),
            },
            "sticky": {"analog": True, "duration": hold_offset_duration},
            "operations": {
                "step": "P2_step_pulse",
            },
        },
        # "sensor_gate": {
        #     "singleInput": {
        #         "port": (con, 3),
        #     },
        #     "operations": {
        #         "step": "bias_charge_pulse",
        #     },
        # },
        # "sensor_gate_sticky": {
        #     "singleInput": {
        #         "port": (con, 3),
        #     },
        #     "sticky": {"analog": True, "duration": hold_offset_duration},
        #     "operations": {
        #         "step": "bias_charge_pulse",
        #     },
        # },
        "qdac_trigger1": {
            "digitalInputs": {
                "trigger": {
                    "port": (con, 3),
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
                    "port": (con, 4),
                    "delay": 0,
                    "buffer": 0,
                }
            },
            "operations": {
                "trigger": "trigger_pulse",
            },
        },
        "qdac_trigger3": {
            "digitalInputs": {
                "trigger": {
                    "port": (con, 9),
                    "delay": 0,
                    "buffer": 0,
                }
            },
            "operations": {
                "trigger": "trigger_pulse",
            },
        },

        # "qubit": {
        #     "RF_inputs": {"port": ("octave1", 2)},
        #     "intermediate_frequency": qubit_IF,
        #     "operations": {
        #         "cw": "cw_pulse",
        #         "pi": "pi_pulse",
        #         "pi_half": "pi_half_pulse",
        #         "gauss": "gaussian_pulse",
        #     },
        # },
        "tank_circuit": {
            "singleInput": {
                "port": (con, 9),
            },
            "intermediate_frequency": resonator_IF,
            "operations": {
                "readout": "reflectometry_readout_pulse",
                "long_readout": "reflectometry_readout_long_pulse",
                "long_readout_trimmed": "reflectometry_readout_long_pulse_trimmed",
            },
            "outputs": {
                "out1": (con, 2),
            },
            "time_of_flight": time_of_flight,
            "smearing": 0,
        },
        "tank_circuit_twin": {
            "singleInput": {
                "port": (con, 9),
            },
            "intermediate_frequency": resonator_IF,
            "operations": {
                "readout": "reflectometry_readout_pulse",
                "long_readout": "reflectometry_readout_long_pulse",
            },
            "outputs": {
                "out1": (con, 2),
            },
            "time_of_flight": time_of_flight,
            "smearing": 0,
        },
    },
    # "octaves": {
    #     "octave1": {
    #         "RF_outputs": {
    #             2: {
    #                 "LO_frequency": qubit_LO,
    #                 "LO_source": "internal",
    #                 "output_mode": "always_on",
    #                 "gain": 0,
    #             },
    #         },
    #         "connectivity": "con1",
    #     }
    # },
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
        "gaussian_pulse": {
            "operation": "control",
            "length": gaussian_length,
            "waveforms": {
                "I": "gaussian_wf",
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
        "reflectometry_readout_pulse": {
            "operation": "measurement",
            "length": reflectometry_readout_length,
            "waveforms": {
                "single": "reflect_wf",
            },
            "integration_weights": {
                "cos": "cosine_weights",
                "sin": "sine_weights",
            },
            "digital_marker": "ON",
        },
        "reflectometry_readout_long_pulse": {
            "operation": "measurement",
            "length": reflectometry_readout_long_length,
            "waveforms": {
                "single": "reflect_wf",
            },
            "integration_weights": {
                "cos": "long_cosine_weights",
                "sin": "long_sine_weights",
            },
            "digital_marker": "ON",
        },
        "reflectometry_readout_long_pulse_trimmed": {
            "operation": "measurement",
            "length": reflectometry_readout_long_length_trimmed,
            "waveforms": {
                "single": "reflect_wf",
            },
            "integration_weights": {
                "cos": "long_cosine_weights_trimmed",
                "sin": "long_sine_weights_trimmed",
            },
            "digital_marker": "ON",
        },
        # "readout_pulse": {
        #     "operation": "measurement",
        #     "length": readout_len,
        #     "waveforms": {
        #         "single": "readout_pulse_wf",
        #     },
        #     "integration_weights": {
        #         "constant": "constant_weights",
        #     },
        #     "digital_marker": "ON",
        # },
    },
    "waveforms": {
        "P1_step_wf": {"type": "constant", "sample": P1_step_amp},
        "P2_step_wf": {"type": "constant", "sample": P2_step_amp},
        "charge_sensor_step_wf": {"type": "constant", "sample": charge_sensor_amp},
        "pi_wf": {"type": "constant", "sample": pi_amp},
        "pi_half_wf": {"type": "constant", "sample": pi_half_amp},
        "gaussian_wf": {
            "type": "arbitrary",
            "samples": list(
                gaussian_amp * gaussian(gaussian_length, gaussian_length / 5)
            ),
        },
        # "readout_pulse_wf": {"type": "constant", "sample": readout_amp},
        "reflect_wf": {"type": "constant", "sample": reflectometry_readout_amp},
        "const_wf": {"type": "constant", "sample": cw_amp},
        "zero_wf": {"type": "constant", "sample": 0.0},
    },
    "digital_waveforms": {
        "ON": {"samples": [(1, 0)]},
    },
    "integration_weights": {
        # "constant_weights": {
        #     "cosine": [(1, readout_len)],
        #     "sine": [(0.0, readout_len)],
        # },
        "cosine_weights": {
            "cosine": [(1.0, reflectometry_readout_length)],
            "sine": [(0.0, reflectometry_readout_length)],
        },
        "sine_weights": {
            "cosine": [(0.0, reflectometry_readout_length)],
            "sine": [(1.0, reflectometry_readout_length)],
        },
        "long_cosine_weights": {
            "cosine": [(1.0, reflectometry_readout_long_length)],
            "sine": [(0.0, reflectometry_readout_long_length)],
        },
        "long_sine_weights": {
            "cosine": [(0.0, reflectometry_readout_long_length)],
            "sine": [(1.0, reflectometry_readout_long_length)],
        },
        "long_cosine_weights_trimmed": {
            "cosine": [(1.0, reflectometry_readout_long_length_trimmed)],
            "sine": [(0.0, reflectometry_readout_long_length_trimmed)],
        },
        "long_sine_weights_trimmed": {
            "cosine": [(0.0, reflectometry_readout_long_length_trimmed)],
            "sine": [(1.0, reflectometry_readout_long_length_trimmed)],
        },
    },
}
