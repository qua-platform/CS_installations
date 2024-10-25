import numpy as np
from qualang_tools.plot import interrupt_on_close
from qualang_tools.results import fetching_tool, progress_counter
from qualang_tools.units import unit

from qm import QuantumMachine
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


u = unit(coerce_to_integer=True)

#############
# VARIABLES #
#############
qop_ip = "172.16.2.103"
cluster_name = None
qop_port = None
octave_config = None

# Frequencies
readout_AOM_IF = 100 * u.MHz
control_AOM_IF = 100 * u.MHz
control_EOM_IF = 100 * u.MHz
control_EOM_LO = 6 * u.GHz

# Pulses lengths
readout_aom_len = 100 * u.ns
control_aom_len = 100 * u.ns
control_eom_len = 100 * u.ns


config = {
    "version": 1,
    "controllers": {
        "con1": {
            "type": "opx1",
            "analog_outputs": {
                1: {"offset": 0.0},
                2: {"offset": 0.0},
                3: {"offset": 0.0},
                9: {"offset": 0.0},
            },
            "digital_outputs": {
                1: {},
                2: {},
                3: {},
                4: {},
                5: {},
                6: {},
                7: {},
                8: {},
                9: {},
            },
            "analog_inputs": {}
        }
    },
    "elements": {
        "readout_aom": {
            "SingleInput": {
                "port": ("con1", 1),
            },
            "intermediate_frequency": readout_AOM_IF,
            "operations": {
                "readout": "readout_pulse",
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
        "A_transition": {
            "singleInput": {"port": ("con1", 1)},
            "intermediate_frequency": optical_transition_IF,
            "digitalInputs": {
                "marker0": {
                    "port": ("con1", 1),
                    "delay": laser_delay,
                    "buffer": 0,
                },
                "marker1": {
                    "port": ("con1", 2),
                    "delay": laser_delay,
                    "buffer": 0,
                },
            },
            "operations": {
                "laser_ON": "laser_ON_A",
            },
        },
        "B_RF": {
            "singleInput": {"port": ("con1", 3)},
            "intermediate_frequency": optical_transition_IF,
            "operations": {
                "+cw": "+const_pulse",
                "-cw": "-const_pulse",
            },
        },
        "F_transition": {
            "digitalInputs": {
                "marker0": {
                    "port": ("con1", 3),
                    "delay": laser_delay,
                    "buffer": 0,
                },
                "marker1": {
                    "port": ("con1", 4),
                    "delay": laser_delay,
                    "buffer": 0,
                },
            },
            "operations": {
                "laser_ON": "laser_ON",
            },
        },
        "excited_state_mw": {
            "digitalInputs": {
                "switch0": {
                    "port": ("con1", 5),
                    "delay": laser_delay,
                    "buffer": 0,
                },
                "switch1": {
                    "port": ("con1", 6),
                    "delay": laser_delay,
                    "buffer": 0,
                },
            },
            "operations": {
                "switch_ON": "switch_ON",
            },
        },
        "SNSPD": {
            # "singleInput": {"port": ("con1", 1)},  # not used
            "intermediate_frequency": Yb_IF_freq,
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
                "signalThreshold": signal_threshold,
                "signalPolarity": "Ascending",
                "derivativeThreshold": 1023,
                "derivativePolarity": "Below",
            },
            "time_of_flight": detection_delay,
            "smearing": 0,
        },
    },
    "pulses": {
        "readout_pulse": {
            "operation": "control",
            "length": mw_len_NV,
            "waveforms": {"single": "cw_wf"},
        },
    },
    "waveforms": {
        "cw_wf": {"type": "constant", "sample": mw_amp_NV},
        "+cw_wf": {"type": "constant", "sample": B_RF_amp},
        "-cw_wf": {"type": "constant", "sample": -B_RF_amp},
        "pi_wf": {"type": "constant", "sample": pi_amp_NV},
        "minus_pi_wf": {"type": "constant", "sample": -pi_amp_NV},
        "pi_half_wf": {"type": "constant", "sample": pi_half_amp_NV},
        "minus_pi_half_wf": {"type": "constant", "sample": -pi_half_amp_NV},
        "zero_wf": {"type": "constant", "sample": 0.0},
    },
    "digital_waveforms": {
        "ON": {"samples": [(1, 0)]},  # [(on/off, ns)]
        "OFF": {"samples": [(0, 0)]},  # [(on/off, ns)]
    },
    "mixers": {
        "mixer_Yb": [
            {
                "intermediate_frequency": Yb_IF_freq,
                "lo_frequency": Yb_LO_freq,
                "correction": IQ_imbalance(0.0, 0.0),
            },
        ],
    },
}
