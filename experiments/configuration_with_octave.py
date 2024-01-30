"""
Octave configuration working for QOP222 and qm-qua==1.1.5 and newer.
"""

from pathlib import Path
import numpy as np
from qualang_tools.config.waveform_tools import drag_gaussian_pulse_waveforms
from qualang_tools.units import unit
from qualang_tools.config.waveform_tools import flattop_gaussian_waveform
from set_octave import OctaveUnit, octave_declaration


###########
# Network #
###########

qop_ip = "127.0.0.1"  # Write the QM router IP address
cluster_name = None  # Write your cluster_name if version >= QOP220
qop_port = None  # Write the QOP port if version < QOP220

# Set octave_config to None if no octave are present
# octave_config = None

############################
# Set octave configuration #
############################

# The Octave port is 11xxx, where xxx are the last three digits of the Octave internal IP that can be accessed from
# the OPX admin panel if you QOP version is >= QOP220. Otherwise, it is 50 for Octave1, then 51, 52 and so on.
octave_1 = OctaveUnit("octave1", qop_ip, port=11050, con="con1")
# octave_2 = OctaveUnit("octave2", qop_ip, port=11051, con="con1")

# Add the octaves
octaves = [octave_1]
# Configure the Octaves
octave_config = octave_declaration(octaves)

#############
# Save Path #
#############

# Path to base directories for script and data
base_dir = Path(__file__).resolve().parent
save_dir = base_dir / "QM" / "INSTALLATION" / "data"

#########
# Units #
#########
u = unit(coerce_to_integer=True)

#############
# VARIABLES #
#############
# frequencies
bias_LO_freq = 2.05 * u.GHz
bias_IF_freq = 0.15 * u.GHz

pump_probe_LO_freq = 4.25 * u.GHz
pump_probe_IF_freq = 0.15 * u.GHz

pump_LO_freq = pump_probe_LO_freq
pump_IF_freq = pump_probe_IF_freq

probe_LO_freq = pump_probe_LO_freq
probe_IF_freq = pump_probe_IF_freq

assert 2 * (bias_LO_freq + bias_IF_freq) == (pump_probe_LO_freq + pump_probe_IF_freq)

# amplitudes
const_bias_amp = 0.01
const_pump_amp = 0.1
const_probe_amp = 0.1

# pulse length
bias_len = 10 * u.us
pump_len = 10 * u.us
probe_len = 40 * u.us # 1_200 * u.us
probe_ringup_len = 10 * u.us # 100 * u.us
probe_ringdown_len = 10 * u.us # 100 * u.us
probe_trunc_len = probe_len - probe_ringup_len - probe_ringdown_len

assert probe_len % 4 == 0, 'must be integer multiple of 4'
assert probe_ringup_len % 4 == 0, 'must be integer multiple of 4'
assert probe_ringdown_len % 4 == 0, 'must be integer multiple of 4'

# ToF
time_of_flight = 24 * u.ns

# themalization time
thermalization_time = 1 * u.ms


#############################################
#                  Config                   #
#############################################
config = {
    "version": 1,
    "controllers": {
        "con1": {
            "analog_outputs": {
                1: {"offset": 0.0}, # I pump/probe
                2: {"offset": 0.0}, # Q pump/probe
                3: {"offset": 0.0}, # I bias
                4: {"offset": 0.0}, # Q bias
            },
            "digital_outputs": {
                1: {},
            },
            "analog_inputs": {
                1: {"offset": 0.0, "gain_db": 0}, # I from down-conversion
                2: {"offset": 0.0, "gain_db": 0}, # Q from down-conversion
            },
        },
    },
    "elements": {
        "pump_probe": {
            "RF_inputs": {"port": ("octave1", 1)},
            "RF_outputs": {"port": ("octave1", 1)},
            "intermediate_frequency": probe_IF_freq,
            "operations": {
                "cw": "const_pump_pulse",
                "readout": "const_probe_pulse",
            },
            "time_of_flight": time_of_flight,
            "smearing": 0,
        },
        "bias": {
            "RF_inputs": {"port": ("octave1", 2)},
            "intermediate_frequency": bias_IF_freq,
            "operations": {
                "cw": "const_bias_pulse",
            },
        },
    },
    "octaves": {
        "octave1": {
            "connectivity": "con1",
            "RF_outputs": {
                1: {
                    "LO_frequency": pump_probe_LO_freq,
                    "LO_source": "internal",
                    "output_mode": "always_on",
                    "gain": 0,
                },
                2: {
                    "LO_frequency": bias_LO_freq,
                    "LO_source": "internal",
                    "output_mode": "always_on",
                    "gain": 0,
                },
            },
            "RF_inputs": {
                1: {
                    "LO_frequency": probe_LO_freq,
                    "LO_source": "internal",
                },
            },
        }
    },
    "pulses": {
        "const_pump_pulse": {
            "operation": "constrol",
            "length": pump_len,
            "waveforms": {
                "I": "const_pump_wf",
                "Q": "zero_wf",
            },
            "digital_marker": "ON", 
        },
        "const_probe_pulse": {
            "operation": "constrol",
            "length": probe_len,
            "waveforms": {
                "I": "const_probe_wf",
                "Q": "zero_wf",
            },
            "integration_weights": {
                "cos": "cosine_weights",
                "sin": "sine_weights",
                "minus_sin": "minus_sine_weights",
                "truncated_cos": "truncated_cosine_weights", #TODO
                "truncated_sin": "truncated_sine_weights", # TODO
                "truncated_minus_sin": "truncated_minus_sine_weights", #TODO
            },
            "digital_marker": "ON", 
        },
        "const_bias_pulse": {
            "operation": "constrol",
            "length": bias_len,
            "waveforms": {
                "I": "const_bias_wf",
                "Q": "zero_wf",
            },
            "digital_marker": "ON", 
        },
    },
    "waveforms": {
        "zero_wf": {"type": "constant", "sample": 0.0},
        "const_pump_wf": {"type": "constant", "sample": const_pump_amp},
        "const_probe_wf": {"type": "constant", "sample": const_probe_amp},
        "const_bias_wf": {"type": "constant", "sample": const_bias_amp},
    },
    "digital_waveforms": {
        "ON": {"samples": [(1, 0)]},
    },
    "integration_weights": {
        "cosine_weights": {
            "cosine": [(1.0, probe_len)],
            "sine": [(0.0, probe_len)],
        },
        "sine_weights": {
            "cosine": [(0.0, probe_len)],
            "sine": [(1.0, probe_len)],
        },
        "minus_sine_weights": {
            "cosine": [(0.0, probe_len)],
            "sine": [(-1.0, probe_len)],
        },
        "truncated_cosine_weights": {
            "cosine": [(0.0, probe_ringup_len), (1.0, probe_trunc_len), (0.0, probe_ringdown_len)],
            "sine": [(0.0, probe_ringup_len), (0.0, probe_trunc_len), (0.0, probe_ringdown_len)],
        },
        "truncated_sine_weights": {
            "cosine": [(0.0, probe_ringup_len), (0.0, probe_trunc_len), (0.0, probe_ringdown_len)],
            "sine": [(0.0, probe_ringup_len), (1.0, probe_trunc_len), (0.0, probe_ringdown_len)],
        },
        "truncated_minus_sine_weights": {
            "cosine": [(0.0, probe_ringup_len), (0.0, probe_trunc_len), (0.0, probe_ringdown_len)],
            "sine": [(0.0, probe_ringup_len), (-1.0, probe_trunc_len), (0.0, probe_ringdown_len)],
        },
    },
}

