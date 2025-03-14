# %%
"""
QUA-Config supporting OPX1000 w/ MW-FEM
"""

from pathlib import Path
import numpy as np
from qualang_tools.config.waveform_tools import drag_gaussian_pulse_waveforms
from qualang_tools.units import unit


#######################
# AUXILIARY FUNCTIONS #
#######################
u = unit(coerce_to_integer=True)


######################
# Network parameters #
######################
qop_ip = "172.16.33.107"
cluster_name = "Cluster_1" 
qop_port = None  # Write the QOP port if version < QOP220

con = "con1"
lffem1 = 3
lffem2 = 5

# Path to save data
save_dir = Path().absolute() / "data"
save_dir.mkdir(exist_ok=True)
default_additional_files = {
    "configuration_with_lffem_octave.py": "configuration_with_lffem_octave.py",
    "optimal_weights.npz": "optimal_weights.npz",
}


#############################################
#                  Qubits                   #
#############################################

# CW pulse parameter
const_len = 1000
const_amp = 0.25


#############################################
#                Resonators                 #
#############################################
# Qubits full scale power
resonator_full_scale_power_dbm = -20
# Qubits bands
# The keyword "band" refers to the following frequency bands:
#   1: (50 MHz - 5.5 GHz)
#   2: (4.5 GHz - 7.5 GHz)
#   3: (6.5 GHz - 10.5 GHz)
resonator_band = 3
# Resonators LO
resonator_LO = 10.0 * u.GHz
# Resonators IF
resonator_IF_q1 = int(100 * u.MHz)
resonator_IF_q2 = int(200 * u.MHz)
# resontor_delay
resonator_delay = 0

# Readout pulse parameters
readout_len = 1000
readout_amp_q1 = 0.1
readout_amp_q2 = 0.1

# TOF and depletion time
time_of_flight = 24  # must be a multiple of 4
depletion_time = 2 * u.us

#############################################
#                  Config                   #
#############################################
sampling_rate = 1e9
config = {
    "version": 1,
    "controllers": {
        con: {
            "type": "opx1000",
            "fems": {
                lffem2: {
                    "type": "LF",
                    "analog_outputs": {},
                    "digital_outputs": {
                        1: {
                            "level": "TTL",
                        },
                    },
                    "analog_inputs": {},
                },
            },
        }
    },
    "elements": {
        "dm": {
            "digitalInputs": {
                "trigger": {
                    "port": (con, lffem2, 1),
                    "delay": 0,
                    "buffer": 0,
                }
            },
            "operations": {
                "trigger": "trigger_pulse",
            },
        },
    },
    "pulses": {
        "trigger_pulse": {
            "operation": "control",
            "length": 1000,
            "digital_marker": "ON",
        },
    },
    "digital_waveforms": {
        "ON": {"samples": [(1, 0)]},
    },
}

# %%
