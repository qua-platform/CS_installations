"""
Configuration file for DQD measurements with an LF-FEM and Octave

See the "README" file for the relevant python requirements.
"""
import os

import numpy as np
from qualang_tools.units import unit
from qualang_tools.voltage_gates import VoltageGateSequence
from pathlib import Path
from qdac import QDACWithChannelLookup as QDAC
import matplotlib.pyplot as plt
plt.rcParams['image.cmap'] = 'plasma'

u = unit(coerce_to_integer=True)

######################
# Network parameters #
######################
qop_ip = "ip_adress"  # Write the QM router IP address
cluster_name = "CS_3"  # Write your cluster_name if version >= QOP220
qop_port = 80  # Write the QOP port if version < QOP220
# In QOP versions > 2.2.2, the Octave is automatically deteced by the QOP.
# For QOP versions <= 2.2.2, see Tutorials/intro-to-octave/qop 222 and below.
# Below you can specify the path for the Octave mixer calibration's database file.
octave_calibration_db_path = os.getcwd()

# Combined settings for initializing the QuantumMachinesManager
qmm_settings = dict(
    host=qop_ip, port=qop_port, cluster_name=cluster_name, octave_calibration_db_path=octave_calibration_db_path
)

# Path to save data
save_dir = Path(__file__).parent.resolve() / "data"
save_dir.mkdir(exist_ok=True)


#####################
# OPX configuration #
#####################
con = "con1"  # name of the OPX1000
octave = "oct1"  # name of the connected Octave
fem = 3  # slot index of the lf-fem inside the chassis


######################
# QDAC-I parameters  #
######################
qdac_ip = "127.000.000.000"  # Write the QDAC instrument IP address here
qdac_channel_mapping = {
    "B20": 1, "P20": 2, "B21": 3, "B30": 4, "P30": 5, "B31": 6,
    "B1": 9, "P1": 10, "B2": 11, "P2": 12, "B3": 13,
    "AC1": 17, "AC0": 18, "AC3": 19, "P3": 21, "B4": 22, "P4": 23, "B5": 24
}

qdac_turn_on_voltages = {
    "B20": 0.0, "P20": 0.0, "B21": 0.0, "B30": 0.0, "P30": 0.0, "B31": 0.0,
    "B1": 0.0, "P1": 0.0, "B2": 0.0, "P2": 0.0, "B3": 0.0,
    "AC1": 0.0, "AC0": 0.0, "AC3": 0.0, "P3": 0.0, "B4": 0.0, "P4": 0.0, "B5": 0.0
}


settle_time = 1 * u.ms  # Assumes a voltage source bandwidth of 1 kHz


def get_qdac() -> QDAC:
    qdac = QDAC(name='qdac', address=f'TCPIP::{qdac_ip}::5025::SOCKET', update_currents=False,
                qdac_channel_mapping=qdac_channel_mapping, qdac_turn_on_voltages=qdac_turn_on_voltages)

    # set global channel settings
    for i in range(1,25):
        ch = qdac.get_channel_by_index(i)
        ch.slope(0.1)  # set to something "safe" in units of V/s
        # todo: do we need to set the output mode?

    return qdac
######################
#       READOUT      #
######################
# DC readout parameters
tia_iv_scale_factor = 1e-9  # from spec (Femto DDPCA-300 Transimpedance in A/V at V/A = 10^9)
tia_bandwidth = 150  # in Hz, from spec
readout_amp = 0.0  # should be 0 since the OPX doesn't ouptut voltage when measuring transport current
readout_len = 0.2 * u.ms  # should be greater than the time-constant, which is 1 / (2*pi*bandwidth)
# Note: if average source current exceeds 10mV, 4ms integration can lead to fixed-point overflow

lock_in_freq = 200 * u.Hz
lock_in_amp = 450 * u.mV
lock_in_length = 1 * u.ms

time_of_flight = 28

####################
#      QUBIT       #
####################
qubit_LO = 13 * u.GHz
qubit_1_IF = 50 * u.MHz
qubit_2_IF = 50 * u.MHz

photon_assisted_tunneling_LO = 10 * u.GHz
photon_assisted_tunneling_IF = 50 * u.MHz
photon_assisted_tunneling_length = 1 * u.ms
photon_assisted_tunneling_amp = 100 * u.mV

# Continuous wave
const_len = 100
const_amp = 0.1

saturation_len = 10 * u.us
saturation_amp = 0.1

square_pi_len = 100
square_pi_amp = 0.1

x180_len = 40
x180_amp = 0.35

x90_len = x180_len
x90_amp = x180_amp / 2

minus_x90_len = x180_len
minus_x90_amp = -x90_amp

y180_len = x180_len
y180_amp = x180_amp

y90_len = x180_len
y90_amp = y180_amp / 2

minus_y90_len = y180_len
minus_y90_amp = -y90_amp


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
                    "type": "LF",
                    "analog_outputs": {
                        1: {"offset": 0.0, "upsampling_mode": "mw"},  # Qubit RF I-Quadrature
                        2: {"offset": 0.0, "upsampling_mode": "mw"},  # Qubit RF Q-Quadrature
                        3: {"offset": 0.0, "upsampling_mode": "mw"},  # P2 RF I-Quadrature
                        4: {"offset": 0.0, "upsampling_mode": "mw"},  # P2 RF Q-Quadrature
                        5: {"offset": 0.0, "upsampling_mode": "pulse"},  # Plunger Gate Qubit 1 (P1)
                        6: {"offset": 0.0, "upsampling_mode": "pulse"},  # Plunger Gate Qubit 2 (P2)
                        7: {"offset": 0.0, "upsampling_mode": "pulse"},  # SET Plunger Gate (P20)
                        8: {"offset": 0.0, "upsampling_mode": "mw"},  # Drain Gate (AC0)
                    },
                    "digital_outputs": {
                        1: {},  # Octave Trigger
                    },
                    "analog_inputs": {
                        1: {"offset": 0.0, "gain_db": 0},  # Source Gate TIA
                        2: {"offset": 0.0, "gain_db": 0},  # (Must be defined for Octave mixer calibration)
                    },
                }
            }
        },
    },
    "elements": {
        "qubit_1": {
            "RF_inputs": {"port": (octave, 1)},
            # 'mixInputs': {
            #     'I': (con, fem, 1),
            #     'Q': (con, fem, 2),
            #     'lo_frequency': qubit_LO,
            #     'mixer': 'mixer_qubit'
            # },
            "intermediate_frequency": qubit_1_IF,
            "operations": {
                "cw": "const_pulse_q1",
                "saturation": "saturation_pulse_q1",
                "x90": "x90_pulse_q1",
                "x180": "x180_pulse_q1",
                "-x90": "-x90_pulse_q1",
                "y90": "y90_pulse_q1",
                "y180": "y180_pulse_q1",
                "-y90": "-y90_pulse_q1",
            },
        },
        "qubit_2": {
            "RF_inputs": {"port": (octave, 1)},
            # 'mixInputs': {
            #     'I': (con, fem, 1),
            #     'Q': (con, fem, 2),
            #     'lo_frequency': qubit_LO,
            #     'mixer': 'mixer_qubit'
            # },
            "intermediate_frequency": qubit_2_IF,
            "operations": {
                "cw": "const_pulse_q2",
                "saturation": "saturation_pulse_q2",
                "x90": "x90_pulse_q2",
                "x180": "x180_pulse_q2",
                "-x90": "-x90_pulse_q2",
                "y90": "y90_pulse_q2",
                "y180": "y180_pulse_q2",
                "-y90": "-y90_pulse_q2",
            },
        },
        "P2_RF": {
            "RF_inputs": {"port": (octave, 2)},
            # 'mixInputs': {
            #     'I': (con, fem, 3),
            #     'Q': (con, fem, 4),
            #     'lo_frequency': photon_assisted_tunneling_LO,
            #     'mixer': 'mixer_pat'
            # },
            "intermediate_frequency": photon_assisted_tunneling_IF,
            "operations": {
                "photon_assisted_tunneling": "const_pulse_pat",
            },
        },
        "P1": {
            "singleInput": {
                "port": (con, fem, 5),
            },
            "operations": {
                "step": "P1_step_pulse",
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
        "P2": {
            "singleInput": {
                "port": (con, fem, 6),
            },
            "operations": {
                "step": "P2_step_pulse",
            },
        },
        "P2_sticky": {
            "singleInput": {
                "port": (con, fem, 6),
            },
            "sticky": {"analog": True, "duration": hold_offset_duration},
            "operations": {
                "step": "P1_step_pulse",
            },
        },
        "SET": {
            "singleInput": {
                "port": (con, fem, 7),
            },
            "operations": {
                "step": "SET_step_pulse",
            },
        },
        "SET_sticky": {
            "singleInput": {
                "port": (con, fem, 7),
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
                "port": (con, fem, 8),
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
                },
                2: {
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
        "const_pulse_q1": {
            "operation": "control",
            "length": const_len,
            "waveforms": {
                "I": "const_wf",
                "Q": "zero_wf",
            },
        },
        "saturation_pulse_q1": {
            "operation": "control",
            "length": saturation_len,
            "waveforms": {"I": "saturation_drive_wf", "Q": "zero_wf"},
        },
        "x90_pulse_q1": {
            "operation": "control",
            "length": x90_len,
            "waveforms": {
                "I": "x90_I_wf",
                "Q": "zero_wf",
            },
        },
        "x180_pulse_q1": {
            "operation": "control",
            "length": x180_len,
            "waveforms": {
                "I": "x180_I_wf",
                "Q": "zero_wf",
            },
        },
        "-x90_pulse_q1": {
            "operation": "control",
            "length": minus_x90_len,
            "waveforms": {
                "I": "minus_x90_I_wf",
                "Q": "zero_wf",
            },
        },
        "y90_pulse_q1": {
            "operation": "control",
            "length": y90_len,
            "waveforms": {
                "I": "zero_wf",
                "Q": "y90_Q_wf",
            },
        },
        "y180_pulse_q1": {
            "operation": "control",
            "length": y180_len,
            "waveforms": {
                "I": "zero_wf",
                "Q": "y180_Q_wf",
            },
        },
        "-y90_pulse_q1": {
            "operation": "control",
            "length": minus_y90_len,
            "waveforms": {
                "I": "zero_wf",
                "Q": "minus_y90_Q_wf",
            },
        },
        "const_pulse_q2": {
            "operation": "control",
            "length": const_len,
            "waveforms": {
                "I": "const_wf",
                "Q": "zero_wf",
            },
        },
        "saturation_pulse_q2": {
            "operation": "control",
            "length": saturation_len,
            "waveforms": {"I": "saturation_drive_wf", "Q": "zero_wf"},
        },
        "x90_pulse_q2": {
            "operation": "control",
            "length": x90_len,
            "waveforms": {
                "I": "x90_I_wf",
                "Q": "zero_wf",
            },
        },
        "x180_pulse_q2": {
            "operation": "control",
            "length": x180_len,
            "waveforms": {
                "I": "x180_I_wf",
                "Q": "zero_wf",
            },
        },
        "-x90_pulse_q2": {
            "operation": "control",
            "length": minus_x90_len,
            "waveforms": {
                "I": "minus_x90_I_wf",
                "Q": "zero_wf",
            },
        },
        "y90_pulse_q2": {
            "operation": "control",
            "length": y90_len,
            "waveforms": {
                "I": "zero_wf",
                "Q": "y90_Q_wf",
            },
        },
        "y180_pulse_q2": {
            "operation": "control",
            "length": y180_len,
            "waveforms": {
                "I": "zero_wf",
                "Q": "y180_Q_wf",
            },
        },
        "-y90_pulse_q2": {
            "operation": "control",
            "length": minus_y90_len,
            "waveforms": {
                "I": "zero_wf",
                "Q": "minus_y90_Q_wf",
            },
        },
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
        "const_pulse_pat": {
            "operation": "control",
            "length": photon_assisted_tunneling_length,
            "waveforms": {
                "I": "const_pat_wf",
                "Q": "zero_wf",
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
        "const_wf": {"type": "constant", "sample": const_amp},
        "const_pat_wf": {"type": "constant", "sample": photon_assisted_tunneling_amp},
        "saturation_drive_wf": {"type": "constant", "sample": saturation_amp},
        "zero_wf": {"type": "constant", "sample": 0.0},
        "x90_I_wf": {"type": "constant", "sample": x90_amp},
        "x180_I_wf": {"type": "constant", "sample": x180_amp},
        "minus_x90_I_wf": {"type": "constant", "sample": minus_x90_amp},
        "y90_Q_wf": {"type": "constant", "sample": y90_amp},
        "y180_Q_wf": {"type": "constant", "sample": y180_amp},
        "minus_y90_Q_wf": {"type": "constant", "sample": minus_y90_amp},
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
    "mixers": {
        'mixer_pat': [
            {'intermediate_frequency': photon_assisted_tunneling_IF, 'lo_frequency': photon_assisted_tunneling_LO, 'correction': [1.0, 0.0, 0.0, 1.0]},
        ],
        'mixer_qubit': [
            {'intermediate_frequency': qubit_1_IF, 'lo_frequency': qubit_LO, 'correction': [1.0, 0.0, 0.0, 1.0]},
        ],
    }
}
