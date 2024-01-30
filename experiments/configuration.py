"""
Octave configuration working for QOP222 and qm-qua==1.1.5 and newer.
"""

import os
import numpy as np
from qualang_tools.config.waveform_tools import drag_gaussian_pulse_waveforms
from qualang_tools.units import unit
from qualang_tools.config.waveform_tools import flattop_gaussian_waveform
from set_octave import OctaveUnit, octave_declaration


#######################
# AUXILIARY FUNCTIONS #
#######################
u = unit(coerce_to_integer=True)


# IQ imbalance matrix
def IQ_imbalance(g, phi):
    """
    Creates the correction matrix for the mixer imbalance caused by the gain and phase imbalances, more information can
    be seen here:
    https://docs.qualang.io/libs/examples/mixer-calibration/#non-ideal-mixer
    :param g: relative gain imbalance between the 'I' & 'Q' ports. (unit-less), set to 0 for no gain imbalance.
    :param phi: relative phase imbalance between the 'I' & 'Q' ports (radians), set to 0 for no phase imbalance.
    """
    c = np.cos(phi)
    s = np.sin(phi)
    N = 1 / ((1 - g**2) * (2 * c**2 - 1))
    return [float(N * x) for x in [(1 - g) * c, (1 + g) * s, (1 - g) * s, (1 + g) * c]]


###########
# Network #
###########

qop_ip = "127.0.0.1"  # Write the QM router IP address
cluster_name = None  # Write your cluster_name if version >= QOP220
qop_port = None  # Write the QOP port if version < QOP220

# Set octave_config to None if no octave are present
octave_config = None


#############
# Save Path #
#############
from pathlib import Path

# Path to base directories for script and data
base_dir = Path(__file__).resolve().parent
save_dir = base_dir / "QM" / "INSTALLATION" / "data"


#############
# VARIABLES #
#############

# frequencies
bias_LO_freq = 2.05 * u.GHz # Used only for mixer correction and frequency rescaling for plots or computation
bias_IF_freq = 0.15 * u.GHz

pump_probe_LO_freq = 4.25 * u.GHz # Used only for mixer correction and frequency rescaling for plots or computation
pump_probe_IF_freq = 0.15 * u.GHz

pump_LO_freq = pump_probe_LO_freq
pump_IF_freq = pump_probe_IF_freq

probe_LO_freq = pump_probe_LO_freq
probe_IF_freq = pump_probe_IF_freq

assert 2 * (bias_LO_freq + bias_IF_freq) == (pump_probe_LO_freq + pump_probe_IF_freq)

# Mixer parameters
mixer_pump_probe_g = 0.00
mixer_bias_g = 0.00
mixer_pump_probe_phi = 0.0
mixer_bias_phi = 0.0

# amplitudes
const_bias_amp = 0.01
const_pump_amp = 0.1
const_probe_amp = 0.1

# pulse length
bias_len = 10 * u.us
pump_len = 10 * u.us
probe_len = 1_200 * u.us
probe_ringup_len = 100 * u.us
probe_ringdown_len = 100 * u.us
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
            "mixInputs": {
                "I": ("con1", 1),
                "Q": ("con1", 2),
                "lo_frequency": pump_probe_LO_freq,
                "mixer": "mixer_pump_probe",
            },
            "intermediate_frequency": pump_probe_IF_freq,
            "operations": {
                "cw": "const_pump_pulse",
                "readout": "const_probe_pulse",
            },
            "outputs": {
                "out1": ("con1", 1),
                "out2": ("con1", 2),
            },
            "time_of_flight": time_of_flight,
            "smearing": 0,
        },
        "bias": {
            "mixInputs": {
                "I": ("con1", 3),
                "Q": ("con1", 4),
                "lo_frequency": bias_LO_freq,
                "mixer": "mixer_bias"
            },
            "intermediate_frequency": bias_IF_freq,
            "operations": {
                "cw": "const_bias_pulse",
            },
        },
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
    "mixers": {
        "mixer_pump_probe": [
            {
                "intermediate_frequency": pump_probe_IF_freq,
                "lo_frequency": pump_probe_LO_freq,
                "correction": IQ_imbalance(mixer_pump_probe_g, mixer_pump_probe_phi),
            },
        ],
        "mixer_bias": [
            {
                "intermediate_frequency": bias_IF_freq,
                "lo_frequency": bias_LO_freq,
                "correction": IQ_imbalance(mixer_bias_g, mixer_bias_phi),
            },
        ],
    },
}

