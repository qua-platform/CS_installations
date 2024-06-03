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
qop_ip = "192.168.88.253"
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

# aom
aom_amp = 0.3
initialization_len = 2 * u.us # * u.us # 3_000 * u.ns

# trigger lengths
mw_switch_len = 1000 * u.ns
meas_len = 300 * u.ns
long_meas_len = 5 * u.us

# delays
time_of_flight = 36 * u.ns
detection_delay = time_of_flight + 500 * u.ns
mw_delay = time_of_flight + 100 * u.ns
laser_delay = time_of_flight # 40 * u.ns
mw_switch_delay = time_of_flight + 0 * u.ns # 40 * u.ns

# integration weights
const_weight = 1.0
long_const_weight = 1e-4 # should be about const_weight * meas_len / long_meas_len

# for time taggling
signal_threshold = -1000
deriv_threshold = -10000

# relaxation time from the metastable state to the ground state after during initialization
relaxation_time = 1000 * u.ns
wait_between_runs = 5 * relaxation_time
wait_for_initialization = 5 * relaxation_time


config = {
    "version": 1,
    "controllers": {
        "con1": {
            "analog_outputs": {
                1: {"offset": 0.0, "delay": laser_delay}, # AOM/Laser
                2: {"offset": 0.0, "delay": detection_delay}, # SPCM
            },
            "digital_outputs": {
                1: {},  # AOM/Laser
                2: {},  # MW Switch
            },
            "analog_inputs": {
                1: {"offset": 0.0, "gain_db": 0},  # SPCM/SPCM
            },
        },
    },
    "elements": {
        # Require IQ Mixer
        # "NV": {
        #     "mixInputs": {"I": ("con1", 1), "Q": ("con1", 2)},
        #     "intermediate_frequency": NV_IF_freq,
        #     "operations": {
        #         "cw": "const_pulse",
        #         "x180": "x180_pulse",
        #         "x90": "x90_pulse",
        #         "-x90": "-x90_pulse",
        #         "y180": "y180_pulse",
        #         "y90": "y90_pulse",
        #         "-y90": "-y90_pulse",
        #     },
        # },
        "AOM": {
            "singleInput": {"port": ("con1", 1)},  # not used
            "intermediate_frequency": 0,
            "operations": {
                "laser_ON": "laser_ON",
            },
        },
        "MW_Switch": {
            "digitalInputs": {
                "marker": {
                    "port": ("con1", 1),
                    "delay": mw_switch_delay,
                    "buffer": 0,
                },
            },
            "operations": {
                "mw_ON": "mw_ON",
            },
        },
        "SPCM": {
            "singleInput": {"port": ("con1", 2)},  # not used
            "operations": {
                "readout": "readout_pulse",
                "long_readout": "long_readout_pulse",
            },
            "outputs": {"out1": ("con1", 1)},
            "outputPulseParameters": {
                "signalThreshold": signal_threshold,  # ADC units
                "signalPolarity": "Below",
                "derivativeThreshold": deriv_threshold,
                "derivativePolarity": "Above",
            },
            "time_of_flight": detection_delay,
            "smearing": 0,
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
            "waveforms": {"single": "aom_wf"},
            # "digital_marker": "ON",
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
        "aom_wf": {"type": "constant", "sample": aom_amp},
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
