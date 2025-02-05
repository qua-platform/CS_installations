from pathlib import Path

import numpy as np
from qualang_tools.config.waveform_tools import drag_gaussian_pulse_waveforms
from qualang_tools.units import unit

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


######################
# Network parameters #
######################
qop_ip = "172.16.33.101"  # Write the QM router IP address
cluster_name = "Cluster_81"  # Write your cluster_name if version >= QOP220
qop_port = None  # Write the QOP port if version < QOP220

# Path to save data
save_dir = Path().absolute() / "QM" / "INSTALLATION" / "data"

#####################
# OPX configuration #
#####################
# Set octave_config to None if no octave are present
octave_config = None

#####################
# Mixer Corrections #
#####################

mixer_ATS1_g = 0.00
mixer_ATS1_p = 0.00

mixer_ATS2_g = 0.00
mixer_ATS2_p = 0.00

mixer_memory1_g = 0.00
mixer_memory1_p = 0.00

mixer_memory2_g = 0.00
mixer_memory2_p = 0.00

#########################
# Experiment Parameters #
#########################
ATS1_LO = 7.1 * u.GHz
ATS1_IF = 50 * u.MHz
two_P_pump1_IF = 100 * u.MHz
two_P_pump2_IF = 100 * u.MHz
memory1_IF = 100 * u.MHz
memory2_IF = 100 * u.MHz

twoP_pump1_LO = 7.1 * u.GHz
twoP_pump2_LO = 7.1 * u.GHz
memory1_LO = 7.1 * u.GHz
memory2_LO = 7.1 * u.GHz

ATS2_LO = 7.8 * u.GHz
ATS2_IF = 100 * u.MHz

readout_len = 5 * u.us  # Length of the readout pulse
const_len = 1 * u.us  # Length of the constant pulse
const_amp = 0.1  # Amplitude of the constant pulse
ATS1_drive_len = 1 * u.us  # Length of the drive pulse
ATS2_drive_len = 1 * u.us  # Length of the drive pulse

time_of_flight = 24

memory1_pi_len = 100 * u.ns  # Length of the pi pulse
memory2_pi_len = 100 * u.ns  # Length of the pi pulse
memory1_pi_amp = 0.1  # Amplitude of the pi pulse
memory2_pi_amp = 0.1  # Amplitude of the pi pulse

saturation_amp = 0.3
ATS1_readout_amp = 0.1
ATS2_readout_amp = 0.1


#############################################
#                  Config                   #
#############################################
config = {
    "version": 1,
    "controllers": {
        "con1": {
            "analog_outputs": {
                1: {"offset": 0.0},  # ATS1 drive I
                2: {"offset": 0.0},  # ATS1 drive Q
                3: {"offset": 0.0},  # Memory1 drive I
                4: {"offset": 0.0},  # Memory1 drive Q
            },
            "digital_outputs": {
                1: {},  # ATS1 flux switch
                2: {},  # QDAC ATS1 switch1
                3: {},  # QDAC ATS1 switch2
            },
            "analog_inputs": {
                1: {"offset": 0.0, "gain_db": 0},  # ATS1 readout
            },
        },
        "con2": {
            "analog_outputs": {
                1: {"offset": 0.0},  # ATS2 drive I
                2: {"offset": 0.0},  # ATS2 drive Q
                3: {"offset": 0.0},  # Memory2 drive I
                4: {"offset": 0.0},  # Memory2 drive Q
            },
            "digital_outputs": {
                1: {},  # ATS2 flux switch
                2: {},  # QDAC ATS2 switch1
                3: {},  # QDAC ATS2 switch2
            },
            "analog_inputs": {
                1: {"offset": 0.0, "gain_db": 0},  # ATS2 readout
            },
        },
    },
    "elements": {
        "ATS1": {
            "mixInputs": {
                "I": ("con1", 1),
                "Q": ("con1", 2),
                "lo_frequency": ATS1_LO,
                "mixer": "mixer_ATS1",
            },
            "intermediate_frequency": ATS1_IF,
            "operations": {
                "cw": "const_pulse",
                "drive": "drive_pulse_ATS1",
                "readout": "readout_pulse_ATS1",
            },
            "outputs": {
                "out1": ("con1", 1),
            },
            "time_of_flight": time_of_flight,
            "smearing": 0,
        },
        "ATS2": {
            "mixInputs": {
                "I": ("con2", 1),
                "Q": ("con2", 2),
                "lo_frequency": ATS2_LO,
                "mixer": "mixer_ATS2",
            },
            "intermediate_frequency": ATS2_IF,
            "operations": {
                "cw": "const_pulse",
                "drive": "drive_pulse_ATS1",
                "readout": "readout_pulse_ATS2",
            },
            "outputs": {
                "out1": ("con2", 1),
            },
            "time_of_flight": time_of_flight,
            "smearing": 0,
        },
        "pump_trigger1": {
            "digitalInputs": {
                "trigger": {
                    "port": ("con1", 1),
                    "delay": 0,
                    "buffer": 0,
                }
            },
            "operations": {
                "pump_trigger": "long_trigger_pulse",
            },
        },
        "pump_trigger2": {
            "digitalInputs": {
                "trigger": {
                    "port": ("con2", 1),
                    "delay": 0,
                    "buffer": 0,
                }
            },
            "operations": {
                "pump_trigger": "long_trigger_pulse",
            },
        },
        "memory1": {
            "mixInputs": {
                "I": ("con1", 3),
                "Q": ("con2", 4),
                "lo_frequency": memory1_LO,
                "mixer": "mixer_twoP_pump2",
            },
            "intermediate_frequency": memory1_IF,
            "operations": {
                "cw": "const_pulse",
                "pi": "memory1_pi_pulse",
            },
        },
        "memory2": {
            "mixInputs": {
                "I": ("con2", 3),
                "Q": ("con2", 4),
                "lo_frequency": memory2_LO,
                "mixer": "mixer_twoP_pump2",
            },
            "intermediate_frequency": memory2_IF,
            "operations": {
                "cw": "const_pulse",
                "pi": "memory2_pi_pulse",
            },
        },
        "QDAC_trigger1": {
            "digitalInputs": {
                "trigger": {
                    "port": ("con1", 2),
                    "delay": 0,
                    "buffer": 0,
                }
            },
            "operations": {
                "qdac_trigger": "short_trigger_pulse",
            },
        },
        "QDAC_trigger2": {
            "digitalInputs": {
                "trigger": {
                    "port": ("con1", 3),
                    "delay": 0,
                    "buffer": 0,
                }
            },
            "operations": {
                "qdac_trigger": "short_trigger_pulse",
            },
        },
        "QDAC_trigger3": {
            "digitalInputs": {
                "trigger": {
                    "port": ("con2", 2),
                    "delay": 0,
                    "buffer": 0,
                }
            },
            "operations": {
                "qdac_trigger": "short_trigger_pulse",
            },
        },
        "QDAC_trigger4": {
            "digitalInputs": {
                "trigger": {
                    "port": ("con2", 3),
                    "delay": 0,
                    "buffer": 0,
                }
            },
            "operations": {
                "qdac_trigger": "short_trigger_pulse",
            },
        },
    },
    "pulses": {
        "const_pulse": {
            "operation": "control",
            "length": const_len,
            "waveforms": {
                "I": "const_wf",
                "Q": "zero_wf",
            },
        },
        "memory1_pi_pulse": {
            "operation": "control",
            "length": memory1_pi_len,
            "waveforms": {
                "I": "memory1_pi_wf_I",
                "Q": "memory1_pi_wf_Q",
            },
        },
        "memory2_pi_pulse": {
            "operation": "control",
            "length": memory2_pi_len,
            "waveforms": {
                "I": "memory2_pi_wf_I",
                "Q": "memory2_pi_wf_Q",
            },
        },
        "drive_pulse_ATS1": {
            "operation": "control",
            "length": ATS1_drive_len,
            "waveforms": {"I": "saturation_drive_wf", "Q": "zero_wf"},
        },
        "readout_pulse_ATS1": {
            "operation": "measurement",
            "length": readout_len,
            "waveforms": {
                "I": "ATS1_readout_wf",
                "Q": "zero_wf",
            },
            "integration_weights": {
                "cos": "cosine_weights",
                "sin": "sine_weights",
                "minus_sin": "minus_sine_weights",
            },
            "digital_marker": "ON",
        },
        "drive_pulse_ATS2": {
            "operation": "control",
            "length": ATS2_drive_len,
            "waveforms": {"I": "saturation_drive_wf", "Q": "zero_wf"},
        },
        "readout_pulse_ATS2": {
            "operation": "measurement",
            "length": readout_len,
            "waveforms": {
                "I": "ATS2_readout_wf",
                "Q": "zero_wf",
            },
            "integration_weights": {
                "cos": "cosine_weights",
                "sin": "sine_weights",
                "minus_sin": "minus_sine_weights",
            },
            "digital_marker": "ON",
        },
        "long_trigger_pulse": {
            "operation": "control",
            "length": 1000,
            "digital_marker": "ON",
        },
        "short_trigger_pulse": {
            "operation": "control",
            "length": 100,
            "digital_marker": "ON",
        },
    },
    "waveforms": {
        "const_wf": {"type": "constant", "sample": const_amp},
        "ATS1_readout_wf": {"type": "constant", "sample": ATS1_readout_amp},
        "ATS2_readout_wf": {"type": "constant", "sample": ATS2_readout_amp},
        "zero_wf": {"type": "constant", "sample": 0.0},
        "memory1_pi_wf_I": {
            "type": "arbitrary",
            "samples": drag_gaussian_pulse_waveforms(
                amplitude=memory1_pi_amp,
                length=memory1_pi_len,
                sigma=memory1_pi_len / 4,
                alpha=0.0,
                anharmonicity=200 * u.MHz,
            )[0],
        },
        "memory1_pi_wf_Q": {
            "type": "arbitrary",
            "samples": drag_gaussian_pulse_waveforms(
                amplitude=memory1_pi_amp,
                length=memory1_pi_len,
                sigma=memory1_pi_len / 4,
                alpha=0.0,
                anharmonicity=200 * u.MHz,
            )[1],
        },
        "memory2_pi_wf_I": {
            "type": "arbitrary",
            "samples": drag_gaussian_pulse_waveforms(
                amplitude=memory2_pi_amp,
                length=memory2_pi_len,
                sigma=memory2_pi_len / 4,
                alpha=0.0,
                anharmonicity=200 * u.MHz,
            )[0],
        },
        "memory2_pi_wf_Q": {
            "type": "arbitrary",
            "samples": drag_gaussian_pulse_waveforms(
                amplitude=memory2_pi_amp,
                length=memory2_pi_len,
                sigma=memory2_pi_len / 4,
                alpha=0.0,
                anharmonicity=200 * u.MHz,
            )[1],
        },
        "saturation_drive_wf": {"type": "constant", "sample": saturation_amp},
    },
    "digital_waveforms": {
        "ON": {"samples": [(1, 0)]},
    },
    "integration_weights": {
        "cosine_weights": {
            "cosine": [(1.0, readout_len)],
            "sine": [(0.0, readout_len)],
        },
        "sine_weights": {
            "cosine": [(0.0, readout_len)],
            "sine": [(1.0, readout_len)],
        },
        "minus_sine_weights": {
            "cosine": [(0.0, readout_len)],
            "sine": [(-1.0, readout_len)],
        },
    },
    "mixers": {
        "mixer_ATS1": [
            {
                "intermediate_frequency": ATS1_IF,
                "lo_frequency": ATS1_LO,
                "correction": IQ_imbalance(mixer_ATS1_g, mixer_ATS1_p),
            }
        ],
        "mixer_ATS2": [
            {
                "intermediate_frequency": ATS2_IF,
                "lo_frequency": ATS2_LO,
                "correction": IQ_imbalance(mixer_ATS2_g, mixer_ATS2_p),
            }
        ],
        "mixer_memory1": [
            {
                "intermediate_frequency": memory1_IF,
                "lo_frequency": memory1_LO,
                "correction": IQ_imbalance(mixer_memory1_g, mixer_memory1_p),
            }
        ],
        "mixer_memory2": [
            {
                "intermediate_frequency": memory2_IF,
                "lo_frequency": memory2_LO,
                "correction": IQ_imbalance(mixer_memory2_g, mixer_memory2_p),
            }
        ],
    },
}
