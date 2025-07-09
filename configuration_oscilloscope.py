"""
Configuration file for DQD measurements with an LF-FEM and Octave

See the "README" file for the relevant python requirements.
"""
import os

import numpy as np
from qualang_tools.units import unit
from pathlib import Path
import matplotlib.pyplot as plt
from qualang_tools.voltage_gates import VoltageGateSequence

u = unit(coerce_to_integer=True)

######################
# Network parameters #
######################
qop_ip = "ip_adress"  # Write the QM router IP address
cluster_name = "CS_3"  # Write your cluster_name if version >= QOP220
qop_port = None # Write the QOP port if version < QOP220
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
#       READOUT      #
######################
time_of_flight = 28
pulse_length = 1000 *u.ns
pulse_amp = 0.5

# DC readout parameters
tia_iv_scale_factor = 1e-9  # from spec (Femto DDPCA-300 Transimpedance in A/V at V/A = 10^9)
tia_bandwidth = 150  # in Hz, from spec

lock_in_freq = 200 * u.Hz
lock_in_amp = 450 * u.mV
lock_in_length = 10 * u.ms

time_of_flight = 28
####################
#      QUBIT       #
####################


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

#######################
# ARBITRARY PULSE WAVEFORM #
#######################
# Ω_X(t) = Σ_{k=1..k_max} a_k * sin(m_k * π * f_0)
# where:
#   Ω_X(t) : envelope of the X-control pulse
#   k_max  : number of harmonics included
#   a_k    : amplitude coefficients (list or ndarray)
#   m_k    : integer multipliers of the base frequency π/t_f
#   f_0    : Base frequency
# Ref: https://doi.org/10.1103/PhysRevA.95.062325

f_0       = 10 *u.MHz      # base frequency
k_max     = 3           
a_k       = [0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05]   # total_range:= -0.5 ~ 0.5 
m_k       = [1, 2, 3, 4, 5, 6, 7, 8] 
dt       = 1       # each waveform sample length, Note: need to check the port sampling rate

assert sum(a_k) < 0.5 and sum(a_k) > -0.5, "out of voltage range"
t_ns = np.arange(0, pulse_length, dt) 
t_s = t_ns * 1e-9 # Convert time from ns to seconds for unit consistency in sin(2πft)
omega = sum(a_k[k-1] * np.sin(2 * np.pi * m_k[k-1] * f_0 * t_s) for k in range(1, k_max+1))

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
                        1: {
                            "offset": 0.0, 
                            "upsampling_mode": "mw"
                        },  # IF I-Quadrature
                        2: {
                            "offset": 0.0, 
                            "upsampling_mode": "mw"
                        },  # IF Q-Quadrature
                        5: {
                            "offset": 0.0, 
                            "sampling_rate": 1e9, # default is 1 GSa/s
                        }, #low freq single input
                        6: {
                            "offset": 0.0, 
                            "upsampling_mode": "pulse"
                        },  # P1 Sticky
                        7: {
                            "offset": 0.0, 
                            "upsampling_mode": "pulse"
                        },  # P2 Sticky
                        8: {
                            "offset": 0.0, 
                            "upsampling_mode": "mw"
                        },  # lock-in measurement
                        
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
        "high_freq": {
            "RF_inputs": {"port": (octave, 1)},
            "intermediate_frequency": 300 *u.MHz,
            "operations": {
                "arb": "arb_pulse_high_freq",
                "cw": "const",
            },
        },
        "low_freq": {
            "singleInput": {
                "port": (con, fem, 5),
            },
            "intermediate_frequency": 300 *u.MHz,
            "operations": {
                "arb": "arb_pulse_low_freq",
                "const": "const_pulse"
            },
        },
        "resistance_tia_lock_in": {
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
        "P1_sticky": {
            "singleInput": {
                "port": (con, fem, 6),
            },
            "sticky": {"analog": True, "duration": hold_offset_duration},
            "operations": {
                "step": "P1_step_pulse",
            },
        },
        "P2_sticky": {
            "singleInput": {
                "port": (con, fem, 7),
            },
            "sticky": {"analog": True, "duration": hold_offset_duration},
            "operations": {
                "step": "P2_step_pulse",
            },
        },
    },
    "octaves": {
        "oct1": {
            "RF_outputs": {
                1: {
                    "LO_frequency": 3 *u.GHz,
                    "LO_source": "internal",
                    "output_mode": "always_on",
                    "gain": 0,
                },
            },
            "connectivity": (con, fem),
        }
    },
    "pulses": {
        "const": {
            "operation": "control",
            "length": pulse_length,
            "waveforms": {
                "I": "const_wf",
                "Q": "zero_wf",
            },
            "digital_marker": "ON",
        },
        "arb_pulse_high_freq": {
            "operation": "control",
            "length": pulse_length,
            "waveforms": {
                "I": "arb_wf",
                "Q": "zero_wf",
            },
        },
        "arb_pulse_low_freq": {
            "operation": "control",
            "length": pulse_length,
            "waveforms": {
                "single": "arb_wf",
            },
        },
        "const_pulse": {
            "operation": "control",
            "length": pulse_length,
            "waveforms": {
                "single": "const_wf",
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
    },
    "waveforms": {
        "const_wf": {"type": "constant", "sample": pulse_amp},
        "zero_wf": {"type": "constant", "sample": 0.0},
        "lock_in_wf": {"type": "constant", "sample": lock_in_amp},
        "P1_step_wf": {"type": "constant", "sample": P1_step_amp},
        "P2_step_wf": {"type": "constant", "sample": P2_step_amp},
        "arb_wf": {"type": "arbitrary", "samples": omega.tolist(), "max_allowed_error": 1e-3}, # default max_allowed_error is 1e-4  
    },

    "digital_waveforms": {
        "ON": {"samples": [(1, 0)]},
    },

    "integration_weights": {
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