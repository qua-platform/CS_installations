import numpy as np
from qm import QuantumMachine
from qualang_tools.plot import interrupt_on_close
from qualang_tools.results import fetching_tool, progress_counter
from qualang_tools.units import unit

from quam.quam.utils import pulse

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
pulsed_laser_AOM_IF = 100 * u.MHz
readout_AOM_IF = 100 * u.MHz
control_AOM_IF = 100 * u.MHz
control_EOM_IF = 100 * u.MHz
control_EOM_LO = 6 * u.GHz

# Pulses lengths
readout_aom_len = 100 * u.ns
control_aom_len = 100 * u.ns
control_eom_len = 100 * u.ns
pulsed_laser_aom_len = 100 * u.ns

# Delays
readout_aom_delay = 0 * u.ns
control_aom_delay = 0 * u.ns
control_eom_delay = 0 * u.ns
pulsed_laser_aom_delay = 0 * u.ns

# Amplitudes
readout_amp = 0.1
control_aom_amp = 0.1
control_eom_amp = 0.1
pulsed_laser_amp = 0.1


#################
# CONFIGURATION #
#################

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
            "analog_inputs": {},
        }
    },
    "elements": {
        "readout_aom": {
            "SingleInput": {
                "port": ("con1", 1),  # TODO: assign the right port
                "delay": readout_aom_delay,
            },
            "intermediate_frequency": readout_AOM_IF,
            "operations": {
                "readout": "cw_readout_aom",
            },
            "digitalInputs": {
                "marker": {
                    "port": ("con1", 1),  # TODO: what is this?
                    "delay": readout_aom_delay,
                },
            },
        },
        "control_aom": {
            "SingleInput": {
                "port": ("con1", 1),  # TODO: assign the right port
                "delay": control_aom_delay,
            },
            "intermediate_frequency": control_AOM_IF,
            "operations": {
                "control": "cw_control_aom",
            },
            "digitalInputs": {
                "marker": {
                    "port": ("con1", 1),  # TODO: what is this?
                    "delay": control_aom_delay,
                },
            },
        },
        "control_eom": {
            "SingleInput": {
                "port": ("con1", 1),  # TODO: assign the right port
                "delay": control_eom_delay,
            },
            "intermediate_frequency": control_EOM_IF,
            "operations": {
                "control": "cw_control_eom",
            },
            "digitalInputs": {
                "marker": {
                    "port": ("con1", 1),  # TODO: what is this?
                    "delay": control_eom_delay,
                },
            },
        },
        "pulsed_laser_aom": {
            "SingleInput": {
                "port": ("con1", 1),  # TODO: assign the right port
                "delay": pulsed_laser_aom_delay,
            },
            "intermediate_frequency": pulsed_laser_AOM_IF,
            "operations": {
                "control": "cw_pulsed_laser_aom",
            },
            "digitalInputs": {
                "marker": {
                    "port": ("con1", 1),  # TODO: what is this?
                    "delay": pulsed_laser_aom_delay,
                },
            },
        },
    },
    "pulses": {
        "cw_readout_aom": {
            "operation": "readout",
            "length": readout_aom_len,
            "waveforms": {"single": "cw_r"},
        },
        "cw_control_aom": {
            "operation": "control",
            "length": control_aom_len,
            "waveforms": {"single": "cw_c_a"},
        },
        "cw_control_eom": {
            "operation": "control",
            "length": control_eom_len,
            "waveforms": {"single": "cw_c_e"},
        },
        "cw_pulsed_laser_aom": {
            "operation": "control",
            "length": pulsed_laser_aom_len,
            "waveforms": {"single": "cw_pl_a"},
        },
    },
    "waveforms": {
        "cw_r": {"type": "constant", "sample": readout_amp},
        "cw_c_a": {"type": "constant", "sample": control_aom_amp},
        "cw_c_e": {"type": "constant", "sample": control_eom_amp},
        "cw_pl_a": {"type": "constant", "sample": pulsed_laser_amp},
    },
    "digital_waveforms": {
        "ON": {"samples": [(1, 0)]},  # [(on/off, ns)]
        "OFF": {"samples": [(0, 0)]},  # [(on/off, ns)]
    },
}
