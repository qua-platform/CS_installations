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
cluster_name = "Cluster_83"  # Write your cluster_name if version >= QOP220
qop_port = None  # Write the QOP port if version < QOP220

# Path to save data
save_dir = Path().absolute() / "QM" / "INSTALLATION" / "data"

#############################################
#                  Qubits                   #
#############################################
qubit_LO = 7.4 * u.GHz  # Used only for mixer correction and frequency rescaling for plots or computation
qubit_IF = 110 * u.MHz
mixer_qubit_g = 0.0
mixer_qubit_phi = 0.0

# Continuous wave
const_len = 100
const_amp = 0.25
# Square wave
square_up_len = 500
square_down_len = 1000
square_amp = 0.25
# Arbitrary pulse
arb_len = 16
arb_amp = 0.5
arb_wf = drag_gaussian_pulse_waveforms(arb_amp, arb_len, arb_len//5, 0.0, 50e6, 0)[0]

#############################################
#                Resonators                 #
#############################################
resonator_LO = 4.8 * u.GHz  # Used only for mixer correction and frequency rescaling for plots or computation
resonator_IF = 60 * u.MHz
mixer_resonator_g = 0.0
mixer_resonator_phi = 0.0

readout_len = 5000
readout_amp = 0.2

time_of_flight = 24
depletion_time = 2 * u.us

# IQ Plane Angle
rotation_angle = (0 / 180) * np.pi




#############################################
#                  Config                   #
#############################################
config = {
    "version": 1,
    "controllers": {
        "con1": {
            "analog_outputs": {
                1: {"offset": 0.0},
                2: {"offset": 0.0},
                3: {"offset": 0.0},
                4: {"offset": 0.0},
                5: {"offset": 0.0},
                9: {"offset": 0.0},
            },
            "digital_outputs": {
                1: {},
                2: {},
            },
            "analog_inputs": {
                1: {"offset": 0.0, "gain_db": 0},
                2: {"offset": 0.0, "gain_db": 0},
            },
        },
    },
    "elements": {
        "lf_readout_element": {
            "singleInput": {
                "port": ("con1", 9),
            },
            "intermediate_frequency": resonator_IF,
            "operations": {
                "readout": "readout_pulse",
            },
            "outputs": {
                "out1": ("con1", 1),
                "out2": ("con1", 2),
            },
            "time_of_flight": time_of_flight,
            "smearing": 0,
        },
        "lf_readout_element_twin": {
            "singleInput": {
                "port": ("con1", 1),
            },
            "intermediate_frequency": resonator_IF,
            "operations": {
                "readout": "readout_pulse",
            },
            "outputs": {
                "out1": ("con1", 1),
                "out2": ("con1", 2),
            },
            "time_of_flight": time_of_flight,
            "smearing": 0,
        },
        "dc_readout_element": {
            "singleInput": {
                "port": ("con1", 1),
            },
            "operations": {
                "readout": "fake_readout_pulse",
            },
            "outputs": {
                "out1": ("con1", 1),
                "out2": ("con1", 2),
            },
            "time_of_flight": time_of_flight,
            "smearing": 0,
        },
        "dc_readout_element_twin": {
            "singleInput": {
                "port": ("con1", 1),
            },
            "operations": {
                "readout": "fake_readout_pulse",
            },
            "outputs": {
                "out1": ("con1", 1),
                "out2": ("con1", 2),
            },
            "time_of_flight": time_of_flight,
            "smearing": 0,
        },
        "lf_element_1": {
            "singleInput": {
                "port": ("con1", 1),
            },
            "intermediate_frequency": 0,
            "operations": {
                "const": "const_single_pulse",
                "arbitrary": "arbitrary_pulse",
                "up": "up_pulse",
                "down": "down_pulse",
            },
        },
        "lf_element_2": {
            "singleInput": {
                "port": ("con1", 2),
            },
            "intermediate_frequency": 0,
            "operations": {
                "const": "const_single_pulse",
                "arbitrary": "arbitrary_pulse",
                "up": "up_pulse",
                "down": "down_pulse",
            },
        },
        "mw_element_1": {
            "mixInputs": {
                "I": ("con1", 1),
                "Q": ("con1", 2),
                "lo_frequency": qubit_LO,
                "mixer": "mixer_qubit",
            },
            "intermediate_frequency": qubit_IF,
            "operations": {
                "const": "const_pulse_mw",
            },
        },
        "qdac_trigger1": {
            "digitalInputs": {
                "trigger": {
                    "port": ("con1", 1),
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
                    "port": ("con1", 2),
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
        "arbitrary_pulse": {
            "operation": "control",
            "length": arb_len,
            "waveforms": {
                "single": "arbitrary_wf",
            },
        },
        "up_pulse": {
            "operation": "control",
            "length": square_up_len,
            "waveforms": {
                "single": "up_wf",
            },
        },
        "down_pulse": {
            "operation": "control",
            "length": square_down_len,
            "waveforms": {
                "single": "down_wf",
            },
        },
        "const_single_pulse": {
            "operation": "control",
            "length": const_len,
            "waveforms": {
                "single": "const_wf",
            },
        },
        "trigger_pulse": {
            "operation": "control",
            "length": 1000,
            "digital_marker": "ON",
        },
        "const_pulse_mw": {
            "operation": "control",
            "length": const_len,
            "waveforms": {
                "I": "const_wf",
                "Q": "zero_wf",
            },
        },
        "readout_pulse": {
            "operation": "measurement",
            "length": readout_len,
            "waveforms": {
                "single": "readout_wf",
            },
            "integration_weights": {
                "cos": "cosine_weights",
                "sin": "sine_weights",
                "minus_sin": "minus_sine_weights",
            },
            "digital_marker": "ON",
        },
        "fake_readout_pulse": {
            "operation": "measurement",
            "length": readout_len,
            "waveforms": {
                "single": "zero_wf",
            },
            "integration_weights": {
                "const": "const_weights",
            },
            "digital_marker": "ON",
        },
    },
    "waveforms": {
        "zero_wf": {"type": "constant", "sample": 0.0},
        "const_wf": {"type": "constant", "sample": const_amp},
        "up_wf": {"type": "constant", "sample": square_amp},
        "down_wf": {"type": "constant", "sample": -square_amp},
        "readout_wf": {"type": "constant", "sample": readout_amp},
        "arbitrary_wf": {"type": "arbitrary", "samples": arb_wf},

    },
    "digital_waveforms": {
        "ON": {"samples": [(1, 0)]},
    },
    "integration_weights": {
        "const_weights": {
            "cosine": [(1.0, readout_len)],
            "sine": [(0.0, readout_len)],
        },
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
        "rotated_cosine_weights": {
            "cosine": [(np.cos(rotation_angle), readout_len)],
            "sine": [(np.sin(rotation_angle), readout_len)],
        },
        "rotated_sine_weights": {
            "cosine": [(-np.sin(rotation_angle), readout_len)],
            "sine": [(np.cos(rotation_angle), readout_len)],
        },
        "rotated_minus_sine_weights": {
            "cosine": [(np.sin(rotation_angle), readout_len)],
            "sine": [(-np.cos(rotation_angle), readout_len)],
        },
    },
    "mixers": {
        "mixer_qubit": [
            {
                "intermediate_frequency": qubit_IF,
                "lo_frequency": qubit_LO,
                "correction": IQ_imbalance(mixer_qubit_g, mixer_qubit_phi),
            }
        ],
    },
}
