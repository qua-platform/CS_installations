"""
QUA-Config supporting OPX1000 w/ LF-FEM & MW-FEM
"""

from pathlib import Path
import numpy as np
from scipy.signal.windows import gaussian
from qualang_tools.units import unit
from set_octave import OctaveUnit, octave_declaration
from qm.qua import declare, assign, play, fixed, Cast, amp, wait, ramp, ramp_to_zero
from typing import Union


######################
# Network parameters #
######################
qop_ip = "172.16.33.107"  # Write the QM router IP address
cluster_name = "Beta_8"  # Write your cluster_name if version >= QOP220
# qop_ip = "192.168.88.253"  # Write the QM router IP address
# cluster_name = "Cluster_1"  # Write your cluster_name if version >= QOP220
qop_port = 9510  # Write the QOP port if version < QOP220
octave_config = None


#####################
# OPX configuration #
#####################
con = "con1"
lf_fem = 5  # Should be the LF-FEM index, e.g., 1


# ############################
# # Set octave configuration #
# ############################
# # The Octave port is 11xxx, where xxx are the last three digits of the Octave internal IP that can be accessed from
# # the OPX admin panel if you QOP version is >= QOP220. Otherwise, it is 50 for Octave1, then 51, 52 and so on.
# octave_1 = OctaveUnit("octave1", qop_ip, port=11109, con=con)
# # octave_2 = OctaveUnit("octave2", qop_ip, port=11051, con=con)

# # If the control PC or local network is connected to the internal network of the QM router (port 2 onwards)
# # or directly to the Octave (without QM the router), use the local octave IP and port 80.
# # octave_ip = "192.168.88.X"
# # octave_1 = OctaveUnit("octave1", octave_ip, port=80, con=con)

# # Add the octaves
# octaves = [octave_1]
# # Configure the Octaves
# octave_config = octave_declaration(octaves)


#############
# Data Save #
#############

# Path to save data
save_dir = Path().absolute() / "data"
save_dir.mkdir(exist_ok=True)
default_additional_files = {
    "configuration_with_lf_fem.py": "configuration_with_lf_fem.py",
    "optimal_weights.npz": "optimal_weights.npz",
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
resonator_IF = 151 * u.MHz
reflectometry_readout_length = 1 * u.us
reflectometry_readout_long_length = 10 * u.us
reflectometry_readout_amp = 30 * u.mV

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
duration_readout = reflectometry_readout_length + 100
duration_compensation_pulse = 4 * u.us

# Step parameters
step_length = 16  # in ns
P1_step_amp = 0.25  # in V
P2_step_amp = 0.25  # in V
charge_sensor_amp = 0.25  # in V

# Time to ramp down to zero for sticky elements in ns
hold_offset_duration = 1000  # in ns
bias_tee_cut_off_frequency = 10 * u.kHz

######################
#    QUBIT PULSES    #
######################
qubit_LO = 4 * u.GHz
qubit_IF = 100 * u.MHz
qubit_power = 1  # power in dBm at waveform amp = 1 (steps of 3 dB)

# Note: amplitudes can be -1..1 and are scaled up to `qubit_power` at amp=1
# Pi pulse
pi_amp = 0.7  # in arb.
pi_length = 32  # in ns
# Pi half
pi_half_amp = 0.7  # in arb.
pi_half_length = 16  # in ns
# Gaussian pulse
gaussian_amp = 0.3  # in arb.
gaussian_length = 20 * int(sampling_rate // 1e9)  # in units of [1/sampling_rate]
# CW pulse
cw_amp = 0.85  # in arb.
cw_len = 100  # in ns

p1_port = 7

#############################################
#                  Config                   #
#############################################
config = {
    "version": 1,
    "controllers": {
        con: {
            "type": "opx1000",
            "fems": {
                # mw_fem: {
                #     # The keyword "band" refers to the following frequency bands:
                #     #   1: (50 MHz - 5.5 GHz)
                #     #   2: (4.5 GHz - 7.5 GHz)
                #     #   3: (6.5 GHz - 10.5 GHz)
                #     # Note that the "coupled" ports O1 & I1, O2 & O3, O4 & O5, O6 & O7, O8 & O1
                #     # must be in the same band, or in bands 1 & 3.
                #     # The keyword "full_scale_power_dbm" is the maximum power of
                #     # normalized pulse waveforms in [-1,1]. To convert to voltage,
                #     #   power_mw = 10**(full_scale_power_dbm / 10)
                #     #   max_voltage_amp = np.sqrt(2 * power_mw * 50 / 1000)
                #     #   amp_in_volts = waveform * max_voltage_amp
                #     #   ^ equivalent to OPX+ amp
                #     # Its range is -41dBm to +10dBm with 3dBm steps.
                #     "type": "MW",
                #     "analog_outputs": {
                #         1: {"band": 1, "full_scale_power_dbm": qubit_power},  # qubit
                #     },
                #     "digital_outputs": {},
                # },
                lf_fem: {
                    "type": "LF",
                    "analog_outputs": {
                        # P1
                        1: {
                            # DC Offset applied to the analog output at the beginning of a program.
                            "offset": 0.0,
                            # The "output_mode" can be used to tailor the max voltage and frequency bandwidth, i.e.,
                            #   "direct":    1Vpp (-0.5V to 0.5V), 750MHz bandwidth (default)
                            #   "amplified": 5Vpp (-2.5V to 2.5V), 330MHz bandwidth
                            # Note, 'offset' takes absolute values, e.g., if in amplified mode and want to output 2.0 V, then set "offset": 2.0
                            "output_mode": "direct",
                            # The "sampling_rate" can be adjusted by using more FEM cores, i.e.,
                            #   1 GS/s: uses one core per output (default)
                            #   2 GS/s: uses two cores per output
                            # NOTE: duration parameterization of arb. waveforms, sticky elements and chirping
                            #       aren't yet supported in 2 GS/s.
                            "sampling_rate": sampling_rate,
                            # At 1 GS/s, use the "upsampling_mode" to optimize output for
                            #   modulated pulses (optimized for modulated pulses):      "mw"    (default)
                            #   unmodulated pulses (optimized for clean step response): "pulse"
                            "upsampling_mode": "pulse",
                        },
                        # P2
                        2: {
                            "offset": 0.0,
                            "output_mode": "direct",
                            "sampling_rate": sampling_rate,
                            "upsampling_mode": "pulse",
                        },
                        # Sensor gate
                        3: {
                            "offset": 0.0,
                            "output_mode": "direct",
                            "sampling_rate": sampling_rate,
                            "upsampling_mode": "pulse",
                        },
                        # RF Reflectometry
                        8: {
                            "offset": 0.0,
                            "output_mode": "direct",
                            "sampling_rate": sampling_rate,
                            "upsampling_mode": "mw",
                        },
                    },
                    "digital_outputs": {
                        1: {},  # TTL for QDAC
                        2: {},  # TTL for QDAC
                    },
                    "analog_inputs": {
                        1: {
                            "offset": 0.0,
                            "gain_db": 0,
                            "sampling_rate": sampling_rate,
                        },  # RF reflectometry input
                        2: {
                            "offset": 0.0,
                            "gain_db": 0,
                            "sampling_rate": sampling_rate,
                        },  # RF reflectometry input
                    },
                },
            },
        }
    },
    "elements": {
        "P1": {
            "singleInput": {
                "port": (con, lf_fem, 1),
            },
            "operations": {
                "step": "P1_step_pulse",
            },
        },
        "P1_sticky": {
            "singleInput": {
                "port": (con, lf_fem, 1),
            },
            "sticky": {"analog": True, "duration": hold_offset_duration},
            "operations": {
                "step": "P1_step_pulse",
            },
        },
        "P2": {
            "singleInput": {
                "port": (con, lf_fem, 2),
            },
            "operations": {
                "step": "P2_step_pulse",
            },
        },
        "P2_sticky": {
            "singleInput": {
                "port": (con, lf_fem, 2),
            },
            "sticky": {"analog": True, "duration": hold_offset_duration},
            "operations": {
                "step": "P2_step_pulse",
            },
        },
        "sensor_gate": {
            "singleInput": {
                "port": (con, lf_fem, 3),
            },
            "operations": {
                "step": "bias_charge_pulse",
            },
        },
        "sensor_gate_sticky": {
            "singleInput": {
                "port": (con, lf_fem, 3),
            },
            "sticky": {"analog": True, "duration": hold_offset_duration},
            "operations": {
                "step": "bias_charge_pulse",
            },
        },
        "qdac_trigger1": {
            "digitalInputs": {
                "trigger": {
                    "port": (con, lf_fem, 1),
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
                    "port": (con, lf_fem, 2),
                    "delay": 0,
                    "buffer": 0,
                }
            },
            "operations": {
                "trigger": "trigger_pulse",
            },
        },
        # "qubit": {
        #     "RF_inputs": {"port": (con, mw_fem, 1)},
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
                "port": (con, lf_fem, 8),
            },
            "intermediate_frequency": resonator_IF,
            "operations": {
                "readout": "reflectometry_readout_pulse",
                "long_readout": "reflectometry_readout_long_pulse",
            },
            "outputs": {
                "out1": (con, lf_fem, 1),
            },
            "time_of_flight": time_of_flight,
            "smearing": 0,
        },
        # "TIA": {
        #     "singleInput": {
        #         "port": (con, lf_fem, 8),
        #     },
        #     "operations": {
        #         "readout": "readout_pulse",
        #     },
        #     "outputs": {
        #         "out1": (con, lf_fem, 1),
        #         "out2": (con, lf_fem, 2),
        #     },
        #     "time_of_flight": time_of_flight,
        #     "smearing": 0,
        # },
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
    },
}
