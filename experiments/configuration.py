from pathlib import Path
import numpy as np
from qualang_tools.units import unit


#######################
# AUXILIARY FUNCTIONS #
#######################

# IQ imbalance matrix
def IQ_imbalance(g, phi):
    """
    Creates the correction matrix for the mixer imbalance caused by the gain and phase imbalances, more information can
    be seen here:
    https://docs.qualang.io/libs/examples/mixer-calibration/#non-ideal-mixer

    :param g: relative gain imbalance between the I & Q ports (unit-less). Set to 0 for no gain imbalance.
    :param phi: relative phase imbalance between the I & Q ports (radians). Set to 0 for no phase imbalance.
    """
    c = np.cos(phi)
    s = np.sin(phi)
    N = 1 / ((1 - g**2) * (2 * c**2 - 1))
    return [float(N * x) for x in [(1 - g) * c, (1 + g) * s, (1 - g) * s, (1 + g) * c]]


######################
# Network parameters #
######################

u = unit(coerce_to_integer=True)
qop_ip = "127.0.0.0"
cluster_name = "Cluster_1"


##################
# Data save path #
##################

base_dir = Path().absolute()
save_dir = base_dir / 'QM' / 'Data'


#############
# VARIABLES #
#############
# mw pulses
NV_IF_freq = 40 * u.MHz
NV_LO_freq = 2.83 * u.GHz

mw_amp_NV = 0.025
mw_len_NV = 40 * u.ns

pi_amp_NV = 0.125  # in units of volts
pi_len_NV = 40 * u.ns

pi_half_amp_NV = pi_amp_NV / 2
pi_half_len_NV = pi_len_NV

minus_pi_half_amp_NV = -1 * pi_half_amp_NV
minus_pi_half_len_NV = pi_len_NV

# trigger lengths
initialization_len = 3_000 * u.ns
mw_switch_len = 40 * u.ns
meas_len = 500 * u.ns
long_meas_len = 5_000 * u.ns

# delays
detection_delay = 24 * u.ns
mw_delay = 40 * u.ns
laser_delay = 40 * u.ns
mw_switch_delay = 40 * u.ns

# integration weights
const_weight = 1.0
long_const_weight = 0.1 # should be about const_weight * meas_len / long_meas_len

# for time taggling
signal_threshold = 0

# relaxation time from the metastable state to the ground state after during initialization
relaxation_time = 300 * u.ns
wait_between_runs = 5 * relaxation_time
wait_for_initialization = 5 * relaxation_time


config = {
    "version": 1,
    "controllers": {
        "con1": {
            "analog_outputs": {
                1: {"offset": 0.0, "delay": mw_delay},
                2: {"offset": 0.0, "delay": mw_delay},
            },
            "digital_outputs": {
                1: {},  # AOM/Laser
                2: {},  # MW Switch
                3: {},  # SCPM
            },
            "analog_inputs": {
                1: {"offset": 0.0},  # PD
            },
        }
    },
    "elements": {
        "NVs": {
            "mixInputs": {"I": ("con1", 1), "Q": ("con1", 2)},
            "intermediate_frequency": NV_IF_freq,
            "operations": {
                "cw": "const_pulse",
                "x180": "x180_pulse",
                "x90": "x90_pulse",
                "-x90": "-x90_pulse",
                "y180": "y180_pulse",
                "y90": "y90_pulse",
                "-y90": "-y90_pulse",
            },
        },
        "AOM": {
            "digitalInputs": {
                "marker": {
                    "port": ("con1", 1),
                    "delay": laser_delay,
                    "buffer": 0,
                },
            },
            "operations": {
                "laser_ON": "laser_ON",
            },
        },
        "PD": {
            "singleInput": {"port": ("con1", 1)},  # not used
            "digitalInputs": {
                "marker": {
                    "port": ("con1", 2),
                    "delay": detection_delay,
                    "buffer": 0,
                },
            },
            "operations": {
                "readout": "readout_pulse",
                "long_readout": "long_readout_pulse",
            },
            "outputs": {"out1": ("con1", 1)},
            "outputPulseParameters": {
                "signalThreshold": signal_threshold,  # ADC units
                "signalPolarity": "Below",
                "derivativeThreshold": -10_000,
                "derivativePolarity": "Above",
            },
            "time_of_flight": detection_delay,
            "smearing": 0,
        },
        "MW_Switch": {
            "digitalInputs": {
                "marker": {
                    "port": ("con1", 3),
                    "delay": mw_switch_delay,
                    "buffer": 0,
                },
            },
            "operations": {
                "mw_ON": "mw_ON",
            },
        },
    },
    "pulses": {
        "const_pulse": {
            "operation": "control",
            "length": mw_len_NV,
            "waveforms": {"I": "const_wf", "Q": "zero_wf"},
        },
        "x180_pulse": {
            "operation": "control",
            "length": pi_len_NV,
            "waveforms": {"I": "pi_wf", "Q": "zero_wf"},
        },
        "x90_pulse": {
            "operation": "control",
            "length": pi_half_len_NV,
            "waveforms": {"I": "pi_half_wf", "Q": "zero_wf"},
        },
        "-x90_pulse": {
            "operation": "control",
            "length": minus_pi_half_len_NV,
            "waveforms": {"I": "minus_pi_half_wf", "Q": "zero_wf"},
        },
        "y180_pulse": {
            "operation": "control",
            "length": pi_len_NV,
            "waveforms": {"I": "zero_wf", "Q": "pi_wf"},
        },
        "y90_pulse": {
            "operation": "control",
            "length": pi_half_len_NV,
            "waveforms": {"I": "zero_wf", "Q": "pi_half_wf"},
        },
        "-y90_pulse": {
            "operation": "control",
            "length": minus_pi_half_len_NV,
            "waveforms": {"I": "zero_wf", "Q": "minus_pi_half_wf"},
        },
        "laser_ON": {
            "operation": "control",
            "length": initialization_len,
            "digital_marker": "ON",
        },
        "mw_ON": {
            "operation": "control",
            "length": mw_switch_len,
            "digital_marker": "ON",
        },
        "readout_pulse": {
            "operation": "measurement",
            "length": meas_len,
            "digital_marker": "ON",
            "waveforms": {"single": "zero_wf"},
            "integration_weights": {
                "const": "constant_weights",
            },
        },
        "long_readout_pulse": {
            "operation": "measurement",
            "length": long_meas_len,
            "digital_marker": "ON",
            "waveforms": {"single": "zero_wf"},
            "integration_weights": {
                "const": "long_constant_weights",
            },
        },
    },
    "waveforms": {
        "const_wf": {"type": "constant", "sample": mw_amp_NV},
        "zero_wf": {"type": "constant", "sample": 0.0},
        "pi_wf": {"type": "constant", "sample": pi_amp_NV},
        "pi_half_wf": {"type": "constant", "sample": pi_half_amp_NV},
        "minus_pi_half_wf": {"type": "constant", "sample": minus_pi_half_amp_NV},
    },
    "digital_waveforms": {
        "ON": {"samples": [(1, 0)]},
    },
    "integration_weights": {
        "constant_weights": {
            "cosine": [(const_weight, meas_len)],
            "sine": [(0.0, meas_len)],
        },
        "long_constant_weights": {
            "cosine": [(long_const_weight, long_meas_len)],
            "sine": [(0.0, long_meas_len)],
        },
    },
    "mixers": {
        "mixer_NV": [
            {
                "intermediate_frequency": NV_IF_freq,
                "lo_frequency": NV_LO_freq,
                "correction": IQ_imbalance(0.0, 0.0),
            },
        ],
    },
}
