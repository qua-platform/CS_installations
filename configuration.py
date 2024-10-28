import matplotlib.pyplot as plt
import numpy as np
from octave_sdk import Octave
from qm import QuantumMachine
from qualang_tools.plot import interrupt_on_close
from qualang_tools.results import fetching_tool, progress_counter
from qualang_tools.units import unit
from set_octave import OctaveUnit, octave_declaration

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
qop_ip = "172.16.33.101"
cluster_name = "Cluster_81"
qop_port = None

octave_1 = OctaveUnit("oct1", qop_ip, port=11232, con="con1")
# Add the octaves
octaves = [octave_1]
# Configure the Octaves
octave_config = octave_declaration(octaves)

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
snspd_readout_len = 1 * u.us
apd_readout_len = 1 * u.us

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

# Time of flight
time_of_flight = 24 * u.ns

#################
# CONFIGURATION #
#################

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
                6: {"offset": 0.0},
                7: {"offset": 0.0},
                8: {"offset": 0.0},
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
            "analog_inputs": {
                1: {"offset": 0.0},
                2: {"offset": 0.0},
            },
        },
    },
    "elements": {
        "readout_aom": {
            "singleInput": {
                "port": ("con1", 1),  # TODO: assign the right port
            },
            "intermediate_frequency": readout_AOM_IF,
            "operations": {
                "readout": "cw_readout_aom",
            },
            "digitalInputs": {
                "marker": {
                    "port": ("con1", 1),  # TODO: what is this?
                    "delay": readout_aom_delay,
                    "buffer": 0,
                },
            },
        },
        "control_aom": {
            "singleInput": {
                "port": ("con1", 2),  # TODO: assign the right port
            },
            "intermediate_frequency": control_AOM_IF,
            "operations": {
                "control": "cw_control_aom",
            },
            "digitalInputs": {
                "marker": {
                    "port": ("con1", 2),  # TODO: what is this?
                    "delay": control_aom_delay,
                    "buffer": 0,
                },
            },
        },
        "control_eom": {
            "RF_inputs": {"port": ("oct1", 2)},
            "intermediate_frequency": control_EOM_IF,
            "operations": {
                "control": "cw_control_eom",
            },
            "digitalInputs": {
                "marker": {
                    "port": ("con1", 3),  # TODO: what is this?
                    "delay": control_eom_delay,
                    "buffer": 0,
                },
            },
        },
        "pulsed_laser_aom": {
            "singleInput": {
                "port": ("con1", 5),  # TODO: assign the right port
            },
            "intermediate_frequency": pulsed_laser_AOM_IF,
            "operations": {
                "control": "cw_pulsed_laser_aom",
            },
            "digitalInputs": {
                "marker": {
                    "port": ("con1", 5),  # TODO: what is this?
                    "delay": pulsed_laser_aom_delay,
                    "buffer": 0,
                },
            },
        },
        "SNSPD": {
            "singleInput": {
                "port": ("con1", 1),  # TODO: assign the right port
            },
            "operations": {"readout": "readout_pulse_snspd"},
            "outputs": {
                "out1": ("con1", 1),
            },
            "time_of_flight": time_of_flight,
            "smearing": 0,
        },
        "APD": {
            "singleInput": {
                "port": ("con1", 1),  # TODO: assign the right port
            },
            "operations": {"readout": "readout_pulse_apd"},
            "outputs": {
                "out1": ("con1", 2),
            },
            "time_of_flight": time_of_flight,
            "smearing": 0,
        },
    },
    "octaves": {
        "oct1": {
            "RF_outputs": {
                2: {
                    "LO_frequency": control_EOM_LO,
                    "LO_source": "internal",  # can be external or internal. internal is the default
                    "output_mode": "triggered",  # can be: "always_on" / "always_off"/ "triggered" / "triggered_reversed". "always_off" is the default
                    "gain": 0,  # can be in the range [-20 : 0.5 : 20]dB
                },
            },
            "connectivity": "con1",
        },
    },
    "pulses": {
        "cw_readout_aom": {
            "operation": "control",
            "length": readout_aom_len,
            "waveforms": {"single": "cw_r"},
            "digital_marker": "ON",
        },
        "cw_control_aom": {
            "operation": "control",
            "length": control_aom_len,
            "waveforms": {"single": "cw_c_a"},
            "digital_marker": "ON",
        },
        "cw_control_eom": {
            "operation": "control",
            "length": control_eom_len,
            "waveforms": {
                "I": "cw_c_e",
                "Q": "zero_wf",
            },
            "digital_marker": "ON",
        },
        "cw_pulsed_laser_aom": {
            "operation": "control",
            "length": pulsed_laser_aom_len,
            "waveforms": {"single": "cw_pl_a"},
            "digital_marker": "ON",
        },
        "readout_pulse_snspd": {
            "operation": "measurement",
            "length": snspd_readout_len,
            "waveforms": {"single": "zero_wf"},
            "digital_marker": "ON",
        },
        "readout_pulse_apd": {
            "operation": "measurement",
            "length": apd_readout_len,
            "waveforms": {"single": "zero_wf"},
            "digital_marker": "ON",
        },
    },
    "waveforms": {
        "cw_r": {"type": "constant", "sample": readout_amp},
        "cw_c_a": {"type": "constant", "sample": control_aom_amp},
        "cw_c_e": {"type": "constant", "sample": control_eom_amp},
        "zero_wf": {"type": "constant", "sample": 0.0},
        "cw_pl_a": {"type": "constant", "sample": pulsed_laser_amp},
    },
    "digital_waveforms": {
        "ON": {"samples": [(1, 0)]},  # [(on/off, ns)]
        "OFF": {"samples": [(0, 0)]},  # [(on/off, ns)]
    },
}
