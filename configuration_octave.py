"""
QUA-Config supporting OPX+ & External Mixers
"""

from pathlib import Path

import numpy as np
import plotly.io as pio
from qualang_tools.units import unit
from qualang_tools.voltage_gates import VoltageGateSequence
from scipy.signal.windows import gaussian
from set_octave import OctaveUnit, octave_declaration
from qdac2_driver import QDACII

pio.renderers.default = "browser"
#######################
# AUXILIARY FUNCTIONS #
#######################
u = unit(coerce_to_integer=True)


######################
# Network parameters #
######################
# qop_ip = "172.16.33.101"  # Write the QM router IP address
# octave_port = (
#     11232  # Must be 11xxx, where xxx are the last three digits of the Octave IP address
# )
# cluster_name = "CS_1"  # Write your cluster_name if version >= QOP220
qop_ip = "192.168.88.249"  # Write the QM router IP address
octave_port = (
    11251  # Must be 11xxx, where xxx are the last three digits of the Octave IP address
)
cluster_name = "Cluster_1"  # Write your cluster_name if version >= QOP220
qop_port = None  # Write the QOP port if version < QOP220
# Create the qdac instrument
# qdac = QDACII(
#     "Ethernet",
#     IP_address="224.0.0.251",
#     port=5025,
#     # "Ethernet", IP_address="172.16.33.101", port=5025
# )  # Using Ethernet protocol
qdac = QDACII("USB", USB_device=8)  # Using USB protocol


#############
# Save Path #
#############
# Path to save data
save_dir = Path(__file__).parent.resolve() / "Data"
save_dir.mkdir(exist_ok=True)

default_additional_files = {
    Path(__file__).name: Path(__file__).name,
    "optimal_weights.npz": "optimal_weights.npz",
}

############################
# OPX/octave configuration #
############################
con = "con1"
oct = "oct1"

# Add the octaves
octaves = [OctaveUnit(oct, qop_ip, port=octave_port, con=con)]
# Configure the Octaves
octave_config = octave_declaration(octaves)

######################
#       READOUT      #
######################
# DC readout parameters
readout_len = 1 * u.us
readout_amp = 0.0
IV_scale_factor = 0.5e-9  # in A/V

# Reflectometry
resonator_IF = 10 * u.MHz
# resonator_IF = 151 * u.MHz
reflectometry_readout_length = 1 * u.us
reflectometry_readout_amp = 30 * u.mV

# Time of flight
time_of_flight = 28

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
coulomb_step_length = 60  # in ns
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
# Octave gain in dB
octave_gain = 0
# x180 pulse
x180_amp = 0.25  # in V
x180_len = 32  # in ns
# y180 pulse
y180_amp = x180_amp  # in V
y180_len = x180_len  # in ns
# x90 pulse
x90_amp = x180_amp / 2  # in V
x90_len = x180_len  # in ns
# -x90 pulse
minus_x90_amp = -x90_amp  # in V
minus_x90_len = x180_len  # in ns
# y90 pulse
y90_amp = y180_amp / 2  # in V
y90_len = y180_len  # in ns
# -y90 pulse
minus_y90_amp = -y90_amp  # in V
minus_y90_len = y180_len  # in ns
# Gaussian pulse
gaussian_amp = 0.1  # in V
gaussian_length = 20  # in ns
# CW pulse
cw_amp = 0.3  # in V
cw_len = 100  # in ns

#############################################
#              Plunger Gates                #
#############################################

hold_offset_duration = 4
step_len = 1000
P1_step_amp = 0.25
P2_step_amp = 0.25


#############################################
#                  Config                   #
#############################################
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
                3: {"offset": 0.0},  # EDSR I quadrature
                4: {"offset": 0.0},  # EDSR Q quadrature
                5: {"offset": 0.0},  # Sensor gate
                6: {"offset": 0.0},  # Dummy
            },
            "digital_outputs": {
                1: {},  # TTL for QDAC
                2: {},  # TTL for QDAC
                3: {},  # TTL for qubit
            },
            "analog_inputs": {
                1: {"offset": 0.0, "gain_db": 0},  # RF reflectometry input
                2: {"offset": 0.0, "gain_db": 0},  # DC readout input
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
                "coulomb_step": "P1_coulomb_step_pulse",
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
                "coulomb_step": "P2_coulomb_step_pulse",
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
        "sensor_gate": {
            "singleInput": {
                "port": (con, 5),
            },
            "operations": {
                "step": "bias_charge_pulse",
            },
        },
        "sensor_gate_sticky": {
            "singleInput": {
                "port": (con, 5),
            },
            "sticky": {"analog": True, "duration": hold_offset_duration},
            "operations": {
                "step": "bias_charge_pulse",
            },
        },
        "qdac_trigger1": {
            "digitalInputs": {
                "trigger": {
                    "port": (con, 1),
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
                    "port": (con, 2),
                    "delay": 0,
                    "buffer": 0,
                }
            },
            "operations": {
                "trigger": "trigger_pulse",
            },
        },
        "qubit": {
            "RF_inputs": {"port": (oct, 2)},
            "intermediate_frequency": qubit_IF,
            "operations": {
                "cw": "cw_pulse",
                "cw_w_trig": "cw_w_trig_pulse",
                "x180": "x180_pulse",
                "y180": "y180_pulse",
                "x90": "x90_pulse",
                "-x90": "-x90_pulse",
                "y90": "y90_pulse",
                "-y90": "-y90_pulse",
                "gauss": "gaussian_pulse",
            },
            "digitalInputs": {
                "switch": {
                    "port": (con, 3),
                    # "delay": 57,  # Suggested delay and buffer values
                    # "buffer": 18,  # https://docs.quantum-machines.co/latest/docs/Guides/octave/?h=octave#calibrating-the-digital-pulse
                    "delay": 0,  # Suggested delay and buffer values
                    "buffer": 0,  # https://docs.quantum-machines.co/latest/docs/Guides/octave/?h=octave#calibrating-the-digital-pulse
                },
            },
        },
        "tank_circuit": {
            "singleInput": {
                "port": (con, 5),
            },
            "intermediate_frequency": resonator_IF,
            "operations": {
                "readout": "reflectometry_readout_pulse",
            },
            "outputs": {
                "out1": (con, 1),
                "out2": (con, 2),
            },
            "time_of_flight": time_of_flight,
            "smearing": 0,
        },
        "tank_circuit_dummy": {
            "singleInput": {
                "port": (con, 6),
            },
            "intermediate_frequency": resonator_IF,
            "operations": {
                "readout": "reflectometry_readout_pulse",
            },
            "outputs": {
                "out1": (con, 1),
                "out2": (con, 2),
            },
            "time_of_flight": time_of_flight,
            "smearing": 0,
        },
        # "TIA": {
        #     "singleInput": {
        #         "port": (con, 6),
        #     },
        #     "operations": {
        #         "readout": "readout_pulse",
        #     },
        #     "outputs": {
        #         "out1": (con, 1),
        #         "out2": (con, 2),
        #     },
        #     "time_of_flight": time_of_flight,
        #     "smearing": 0,
        # },
    },
    "octaves": {
        oct: {
            "RF_outputs": {
                2: {
                    "LO_frequency": qubit_LO,
                    "LO_source": "internal",
                    "output_mode": "always_on",
                    "gain": octave_gain,
                },
            },
            "connectivity": con,
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
        "P1_coulomb_step_pulse": {
            "operation": "control",
            "length": coulomb_step_length,
            "waveforms": {
                "single": "P1_step_wf",
            },
        },
        "P2_coulomb_step_pulse": {
            "operation": "control",
            "length": coulomb_step_length,
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
        "cw_w_trig_pulse": {
            "operation": "control",
            "length": cw_len,
            "waveforms": {
                "I": "const_wf",
                "Q": "zero_wf",
            },
            "digital_marker": "ON",
        },
        "gaussian_pulse": {
            "operation": "control",
            "length": gaussian_length,
            "waveforms": {
                "I": "gaussian_wf",
                "Q": "zero_wf",
            },
        },
        "x180_pulse": {
            "operation": "control",
            "length": x180_len,
            "waveforms": {
                "I": "x180_wf",
                "Q": "zero_wf",
            },
        },
        "y180_pulse": {
            "operation": "control",
            "length": y180_len,
            "waveforms": {
                "I": "zero_wf",
                "Q": "y180_wf",
            },
        },
        "x90_pulse": {
            "operation": "control",
            "length": x90_len,
            "waveforms": {
                "I": "x90_wf",
                "Q": "zero_wf",
            },
        },
        "-x90_pulse": {
            "operation": "control",
            "length": minus_x90_len,
            "waveforms": {
                "I": "minus_x90_wf",
                "Q": "zero_wf",
            },
        },
        "y90_pulse": {
            "operation": "control",
            "length": y90_len,
            "waveforms": {
                "I": "zero_wf",
                "Q": "y90_wf",
            },
        },
        "-y90_pulse": {
            "operation": "control",
            "length": minus_y90_len,
            "waveforms": {
                "I": "zero_wf",
                "Q": "minus_y90_wf",
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
        "x180_wf": {"type": "constant", "sample": x180_amp},
        "y180_wf": {"type": "constant", "sample": y180_amp},
        "x90_wf": {"type": "constant", "sample": x90_amp},
        "minus_x90_wf": {"type": "constant", "sample": minus_x90_amp},
        "y90_wf": {"type": "constant", "sample": y90_amp},
        "minus_y90_wf": {"type": "constant", "sample": minus_y90_amp},
        "gaussian_wf": {
            "type": "arbitrary",
            "samples": list(
                gaussian_amp * gaussian(gaussian_length, gaussian_length / 5)
            ),
        },
        "readout_pulse_wf": {"type": "constant", "sample": readout_amp},
        "reflect_wf": {"type": "constant", "sample": reflectometry_readout_amp},
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
            "cosine": [(1.0, reflectometry_readout_length)],
            "sine": [(0.0, reflectometry_readout_length)],
        },
        "sine_weights": {
            "cosine": [(0.0, reflectometry_readout_length)],
            "sine": [(1.0, reflectometry_readout_length)],
        },
    },
}
