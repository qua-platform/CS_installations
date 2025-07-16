# %%
"""
QUA-Config supporting OPX1000 w/ LF-FEM & MW-FEM
"""

from pathlib import Path
import numpy as np
from qualang_tools.config.waveform_tools import drag_gaussian_pulse_waveforms, flattop_gaussian_waveform, drag_cosine_pulse_waveforms
from qualang_tools.units import unit
from typing import Union


######################
# Network parameters #
######################
qop_ip = "172.16.33.115"  # Write the QM router IP address
cluster_name = "CS_3"  # Write your cluster_name if version >= QOP220


#####################
# OPX configuration #
#####################
con = "con1"
mw_fem = 1
lf_fem = 5


#############
# Data Save #
#############

# Path to save data
save_dir = Path().absolute() / "data"
save_dir.mkdir(exist_ok=True)
default_additional_files = {
    "configuration_with_mwfem_lffem.py": "configuration_with_mwfem_lffem.py",
    "optimal_weights.npz": "optimal_weights.npz",
    "00_QDAC_initial.py": "00_QDAC_initial.py",
}


#############################################
#              OPX PARAMETERS               #
#############################################
sampling_rate = int(1e9)  # or, int(2e9)


#############################################
#                   Util                    #
#############################################


def generate_waveforms(qubit, rotation_keys, amp, pi_len, pi_sigma):
    """ Generate all necessary waveforms for a set of rotation types across all qubits. """
    
    if not isinstance(rotation_keys, list):
        raise ValueError("rotation_keys must be a list")

    waveforms = {}

    for rotation_key in rotation_keys:
        if rotation_key in ["x180", "y180"]:
            wf_amp = amp
        elif rotation_key in ["x90", "y90"]:
            wf_amp = amp / 2
        elif rotation_key in ["minus_x90", "minus_y90"]:
            wf_amp = -amp / 2
        else:
            continue

        wf, der_wf = np.array(drag_gaussian_pulse_waveforms(wf_amp, pi_len, pi_sigma, 0, 0, 0))
        # wf, der_wf = np.array(drag_cosine_pulse_waveforms(wf_amp, pi_len, 0, 0))

        if rotation_key in ["x180", "x90", "minus_x90"]:
            I_wf = wf
            Q_wf = der_wf
        elif rotation_key in ["y180", "y90", "minus_y90"]:
            I_wf = (-1) * der_wf
            Q_wf = wf
        else:
            raise ValueError(f'{rotation_key} is passed. rotation_key must be one of ["x180", "x90", "minus_x90", "y180", "y90", "minus_y90"]')

        waveforms[f"{qubit}_{rotation_key}_I"] = I_wf
        waveforms[f"{qubit}_{rotation_key}_Q"] = Q_wf

    return waveforms


######################
#       READOUT      #
######################
u = unit(coerce_to_integer=True)

# Reflectometry
resonator_IF = 186 * u.MHz  # L

reflectometry_readout_length = 1 * u.us
readout_len = reflectometry_readout_length
measurement_delay = 300 * u.ns
reflectometry_readout_long_length = 200 * u.us
reflectometry_readout_amp = 0.0316  # V -20dB

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
duration_readout = reflectometry_readout_length + 100
duration_compensation_pulse = 4 * u.us

# Step parameters
step_length = 1000  # in ns
P1_step_amp = 0.5  # in V
P2_step_amp = 0.5  # in V
charge_sensor_amp = 0.5  # in V

# Time to ramp down to zero for sticky elements in ns
hold_offset_duration = 1000  # in ns
bias_tee_cut_off_frequency = 10 * u.kHz

######################
#    QUBIT PULSES    #
######################
qubit = "qubit"
qubit_LO = 8 * u.GHz
qubit_IF = 100 * u.MHz
qubit_full_scale_power_dbm = 1  # power in dBm at waveform amp = 1 (steps of 3 dB)

# Note: amplitudes can be -1..1 and are scaled up to `qubit_power` at amp=1
# Pi pulse
pi_amp = 0.7  # in arb.
pi_length = 32  # in ns
# Pi half
pi_half_amp = 0.7  # in arb.
pi_half_length = 16  # in ns
# CW pulse
const_amp = 0.85  # in arb.
const_length = 100  # in ns

qubit_rotation_keys = ["x180", "x90", "minus_x90", "y180", "y90", "minus_y90"]
waveforms = generate_waveforms(qubit, qubit_rotation_keys, pi_amp, pi_length, pi_length / 5)



#############################################
#                  Config                   #
#############################################
config = {
    "version": 1,
    "controllers": {
        con: {
            "type": "opx1000",
            "fems": {
                mw_fem: {
                    # The keyword "band" refers to the following frequency bands:
                    #   1: (50 MHz - 5.5 GHz)
                    #   2: (4.5 GHz - 7.5 GHz)
                    #   3: (6.5 GHz - 10.5 GHz)
                    # Note that the "coupled" ports O1 & I1, O2 & O3, O4 & O5, O6 & O7, O8 & O1
                    # must be in the same band, or in bands 1 & 3.
                    # The keyword "full_scale_power_dbm" is the maximum power of
                    # normalized pulse waveforms in [-1,1]. To convert to voltage,
                    #   power_mw = 10**(full_scale_power_dbm / 10)
                    #   max_voltage_amp = np.sqrt(2 * power_mw * 50 / 1000)
                    #   amp_in_volts = waveform * max_voltage_amp
                    #   ^ equivalent to OPX+ amp
                    # Its range is -41dBm to +10dBm with 3dBm steps.
                    "type": "MW",
                    "analog_outputs": {
                        1: {
                            "sampling_rate": 1e9,
                            "full_scale_power_dbm": qubit_full_scale_power_dbm,
                            "band": 3,
                            "delay": 0,
                            "upconverters": {
                                1: {"frequency": qubit_LO},
                                # 2: {"frequency": QUBIT_CONSTANTS["q8_xy"]["LO"]},
                            },
                        }
                    },
                    "digital_outputs": {},
                    "analog_inputs": {}
                },
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
                        4: {
                            "offset": 0.0,
                            "output_mode": "direct",
                            "sampling_rate": sampling_rate,
                            "upsampling_mode": "pulse",
                        },
                        # BC
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
                        1: {},  # TTL for QDACa3
                        2: {},  # TTL for QDACa4
                        3: {},  # TTL for QDACb3
                        4: {},  # TTL for QDACb4
                        5: {},  # TTL for QDACa1
                        6: {},  # TTL for QDACb1
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
        "BC": {
            "singleInput": {
                "port": (con, lf_fem, 3),
            },
            "operations": {
                "step": "P2_step_pulse",
            },
        },
        "BC_sticky": {
            "singleInput": {
                "port": (con, lf_fem, 3),
            },
            "sticky": {"analog": True, "duration": hold_offset_duration},
            "operations": {
                "step": "P2_step_pulse",
            },
        },
        "sensor_gate": {
            "singleInput": {
                "port": (con, lf_fem, 4),
            },
            "operations": {
                "step": "bias_charge_pulse",
            },
        },
        "sensor_gate_sticky": {
            "singleInput": {
                "port": (con, lf_fem, 4),
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
        "qdac_trigger2": {
            "digitalInputs": {
                "trigger": {
                    "port": (con, lf_fem, 3),
                    "delay": 0,
                    "buffer": 0,
                }
            },
            "operations": {
                "trigger": "trigger_pulse",
            },
        },
        "qubit": {
            "MWInput": {
                "port": (con, mw_fem, 1),
                "upconverter": 1,
            },
            "intermediate_frequency": qubit_IF,
            "operations": {
                "cw": "cw_pulse",
                "x180": f"x180_pulse",
                "x90": f"x90_pulse",
                "-x90": f"-x90_pulse",
                "y90": f"y90_pulse",
                "y180": f"y180_pulse",
                "-y90": f"-y90_pulse",
            },
        },
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
            "length": const_length,
            "waveforms": {
                "I": "const_wf",
                "Q": "zero_wf",
            },
        },
        "x90_pulse": {
            "operation": "control",
            "length": pi_length,
            "waveforms": {
                "I": f"x90_I_wf",
                "Q": f"x90_Q_wf"
            }
        },
        "x180_pulse": {
            "operation": "control",
            "length": pi_length,
            "waveforms": {
                "I": f"x180_I_wf",
                "Q": f"x180_Q_wf"
            }
        },
        "-x90_pulse": {
            "operation": "control",
            "length": pi_length,
            "waveforms": {
                "I": f"minus_x90_I_wf",
                "Q": f"minus_x90_Q_wf"
            }
        },
        "y90_pulse": {
            "operation": "control",
            "length": pi_length,
            "waveforms": {
                "I": f"y90_I_wf",
                "Q": f"y90_Q_wf"
            }
        },
        "y180_pulse": {
            "operation": "control",
            "length": pi_length,
            "waveforms": {
                "I": f"y180_I_wf",
                "Q": f"y180_Q_wf"
            }
        },
        "-y90_pulse": {
            "operation": "control",
            "length": pi_length,
            "waveforms": {
                "I": f"minus_y90_I_wf",
                "Q": f"minus_y90_Q_wf"
            }
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
    },
    "waveforms": {
        "P1_step_wf": {"type": "constant", "sample": P1_step_amp},
        "P2_step_wf": {"type": "constant", "sample": P2_step_amp},
        "charge_sensor_step_wf": {"type": "constant", "sample": charge_sensor_amp},
        "reflect_wf": {"type": "constant", "sample": reflectometry_readout_amp},
        "const_wf": {"type": "constant", "sample": const_amp},
        "zero_wf": {"type": "constant", "sample": 0.0},
        "x90_I_wf": {"type": "arbitrary", "samples": waveforms["qubit_x90_I"].tolist()},
        "x90_Q_wf": {"type": "arbitrary", "samples": waveforms["qubit_x90_Q"].tolist()},
        "x180_I_wf": {"type": "arbitrary", "samples": waveforms["qubit_x180_I"].tolist()},
        "x180_Q_wf": {"type": "arbitrary", "samples": waveforms["qubit_x180_Q"].tolist()},
        "minus_x90_I_wf": {"type": "arbitrary", "samples": waveforms["qubit_minus_x90_I"].tolist()},
        "minus_x90_Q_wf": {"type": "arbitrary", "samples": waveforms["qubit_minus_x90_Q"].tolist()},
        "y90_I_wf": {"type": "arbitrary", "samples": waveforms["qubit_y90_I"].tolist()},
        "y90_Q_wf": {"type": "arbitrary", "samples": waveforms["qubit_y90_Q"].tolist()},
        "y180_I_wf": {"type": "arbitrary", "samples": waveforms["qubit_y180_I"].tolist()},
        "y180_Q_wf": {"type": "arbitrary", "samples": waveforms["qubit_y180_Q"].tolist()},
        "minus_y90_I_wf": {"type": "arbitrary", "samples": waveforms["qubit_minus_y90_I"].tolist()},
        "minus_y90_Q_wf": {"type": "arbitrary", "samples": waveforms["qubit_minus_y90_Q"].tolist()},
    },
    "digital_waveforms": {
        "ON": {"samples": [(1, 0)]},
    },
    "integration_weights": {
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
