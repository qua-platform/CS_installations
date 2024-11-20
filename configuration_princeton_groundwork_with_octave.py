# Imports
import numpy as np
from qualang_tools.units import unit
from set_octave import OctaveUnit, octave_declaration

# Import the following in configuration so there is no need to import in every script
from qualang_tools.plot import interrupt_on_close
from qualang_tools.results import progress_counter, fetching_tool

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


#############
# VARIABLES #
#############
u = unit()
qop_ip = "172.16.33.101"
cluster_name = "Cluster_81"
qop_port = None

############################
# Set octave configuration #
############################
con = "con1"
# The Octave port is 11xxx, where xxx are the last three digits of the Octave internal IP that can be accessed from
# the OPX admin panel if you QOP version is >= QOP220. Otherwise, it is 50 for Octave1, then 51, 52 and so on.
octave_1 = OctaveUnit("oct1", qop_ip, port=11050, con=con)
# octave_2 = OctaveUnit("octave2", qop_ip, port=11051, con=con)

# If the control PC or local network is connected to the internal network of the QM router (port 2 onwards)
# or directly to the Octave (without QM the router), use the local octave IP and port 80.
# octave_ip = "192.168.88.X"
# octave_1 = OctaveUnit("octave1", octave_ip, port=80, con=con)

# Add the octaves
octaves = [octave_1]
# Configure the Octaves
octave_config = octave_declaration(octaves)


############################
# Set octave configuration #
############################

# AOM frequncies
AOM1_freq = 80e6
AOM1_len = 500  # in ns
AOM1_delay = 0  # in ns

AOM2_freq = 120e6
AOM2_len = 500  # in ns
AOM2_delay = 0  # in ns


AOM_freq = 80e6
AOM_len = 500  # in ns
AOM_delay = 0
AOM_amp = 0.004  # in volts

# Pulse lengths
initialization_len = 500  # in ns
excited_state_init = 500  # in ns

# SNSPD
signal_threshold = 500
meas_len = 5000  # in ns
long_meas_len = 10000  # in ns
SNSPD_delay = 0  # in ns
time_of_flight = 136  # in ns

# RF_switch
RF_switch_len = 500  # in ns

# RF_switch
RF_switch_delay = 0  # in ns

# Laser OpticalTrigger
laser_delay = 0  # in ns

# EOM parameters
EOM_LO_freq = 6e9  # 6-10GHz range, Spin preserving transition
EOM_IF_freq = 40e6
EOM_A_IF_freq = 10e6
EOM_B_IF_freq = 300e6
EOM_optical_transition_IF = 300e6

EOM_len = 500  # in ns
EOM_amp = 0.04  # in volts

EOM_pi_len = 512  # in ns
EOM_pi_amp = 0.004  # in volts
EOM_pi_half_len = 256  # in ns
EOM_pi_half_amp = 0.004  # in volts

EOM_delay = 0  # in ns

# MWe parameters
mwe_LO_freq = 2.5e9  # Spin flip transition
mwe_IF_freq = 10e6
mwe_optical_transition_IF = 300e6

mwe_len = 500  # in units of ns
mwe_amp = 0.004  # in units of volts

mwe_pi_len = 512
mwe_pi_amp = 0.004
mwe_pi_half_len = 256
mwe_pi_half_amp = 0.004

mwe_delay = 0  # in ns

# mwg parameters
mwg_LO_freq = 2.5e9  # Spin flip transition
mwg_IF_freq = 10e6
mwg_optical_transition_IF = 300e6

mwg_len = 512  # in ns
mwg_amp = 0.004  # in volts

mwg_pi_len = 512  # in ns
mwg_pi_amp = 0.004  # in volts
mwg_pi_half_len = 256  # in ns
mwg_pi_half_amp = 0.004  # in volts

mwg_delay = 0  # in ns


config = {
    "version": 1,
    "controllers": {
        "con1": {
            "type": "opx1",
            "analog_outputs": {
                1: {"offset": 0.0, "delay": EOM_delay},  # EOM I
                2: {"offset": 0.0, "delay": EOM_delay},  # EOM Q
                3: {"offset": 0.0, "delay": mwe_delay},  # mwe I
                4: {"offset": 0.0, "delay": mwe_delay},  # mwe Q
                5: {"offset": 0.0, "delay": mwg_delay},  # mwg I
                6: {"offset": 0.0, "delay": mwg_delay},  # mwg Q
                7: {"offset": 0.0, "delay": AOM1_delay},  # AOM 1
                8: {"offset": 0.0, "delay": AOM2_delay},  # AOM 2
            },
            "digital_outputs": {
                1: {},  # Optical Switch trigger
                2: {},  # SNSPD trigger
                3: {},  # RF SWITCH trigger
                4: {},  # EOM trigger if necessary
            },
            "analog_inputs": {
                1: {"offset": 0, "gain_db": 0},  # SNSPD
                2: {"offset": 0, "gain_db": 0},
            },
        }
    },
    "elements": {
        "EOM": {
            "RF_inputs": {"port": ("oct1", 1)},
            "intermediate_frequency": EOM_IF_freq,
            "operations": {
                "cw": "EOM_const_pulse",
                "pi": "EOM_pi_pulse",
                "pi_half": "EOM_pi_half_pulse",
            },
            "digitalInputs": {
                "marker": {
                    "port": ("con1", 4),
                    "delay": 57,
                    "buffer": 18,
                },
            },
        },
        "EOM_A": {
            "RF_inputs": {"port": ("oct1", 1)},
            "intermediate_frequency": EOM_A_IF_freq,
            "operations": {
                "cw": "EOM_const_pulse",
                "pi": "EOM_pi_pulse",
                "pi_half": "EOM_pi_half_pulse",
            },
            "digitalInputs": {
                "marker": {
                    "port": ("con1", 4),
                    "delay": 57,
                    "buffer": 18,
                },
            },
        },
        "EOM_B": {
            "RF_inputs": {"port": ("oct1", 1)},
            "intermediate_frequency": EOM_B_IF_freq,
            "operations": {
                "cw": "EOM_const_pulse",
                "pi": "EOM_pi_pulse",
                "pi_half": "EOM_pi_half_pulse",
            },
            "digitalInputs": {
                "marker": {
                    "port": ("con1", 4),
                    "delay": 57,
                    "buffer": 18,
                },
            },
        },
        "mwe": {
            "RF_inputs": {"port": ("oct1", 2)},
            "intermediate_frequency": mwe_IF_freq,
            "operations": {
                "cw": "mwe_const_pulse",
                "pi": "mwe_pi_pulse",
                "pi_half": "mwe_pi_half_pulse",
            },
        },
        "mwg": {
            "RF_inputs": {"port": ("oct1", 3)},
            "intermediate_frequency": mwg_IF_freq,
            "operations": {
                "cw": "mwg_const_pulse",
                "pi": "mwg_pi_pulse",
                "pi_half": "mwg_pi_half_pulse",
            },
        },
        "AOM1": {
            "singleInput": {"port": ("con1", 7)},
            "intermediate_frequency": AOM1_freq,
            "operations": {
                "AOM1_ON": "AOM1_ON",
            },
        },
        "AOM2": {
            "singleInput": {"port": ("con1", 8)},
            "intermediate_frequency": AOM2_freq,
            "operations": {
                "AOM2_ON": "AOM2_ON",
            },
        },
        "AOM": {
            "multipleInputs": {
                "inputs": {
                    "input1": ("con1", 7),
                    "input2": ("con1", 8),
                },
            },
            "intermediate_frequency": AOM_freq,
            "operations": {
                "AOM_ON": "AOM_ON",
            },
        },
        "OpticalTrigger": {  # Laser switch
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
        "SNSPD": {  # SNSPD
            "digitalInputs": {
                "marker": {
                    "port": ("con1", 2),
                    "delay": SNSPD_delay,
                    "buffer": 0,
                },
            },
            "operations": {
                "readout": "readout_pulse",
                "long_readout": "long_readout_pulse",
            },
            "outputs": {"out1": ("con1", 1)},
            "outputPulseParameters": {
                "signalThreshold": -500,
                "signalPolarity": "Above",
                "derivativeThreshold": -10000,
                "derivativePolarity": "Above",
            },
            "time_of_flight": time_of_flight,
            "smearing": 0,
        },
        "RF_switch": {  # RF switch trigger
            "digitalInputs": {
                "marker": {
                    "port": ("con1", 3),
                    "delay": RF_switch_delay,
                    "buffer": 0,
                },
            },
            "operations": {
                "RF_ON": "RF_switch_ON",
            },
        },
    },
    "octaves": {
        "oct1": {
            "RF_outputs": {
                1: {
                    "LO_frequency": EOM_LO_freq,
                    "LO_source": "internal",
                    "output_mode": "triggered",
                    "gain": 0,
                },
                2: {
                    "LO_frequency": mwe_LO_freq,
                    "LO_source": "internal",
                    "output_mode": "always_on",
                    "gain": 0,
                },
                3: {
                    "LO_frequency": mwe_LO_freq,
                    "LO_source": "internal",
                    "output_mode": "always_on",
                    "gain": 0,
                },
            },
            "connectivity": "con1",
        },
    },
    "pulses": {
        "EOM_const_pulse": {
            "operation": "control",
            "length": EOM_len,
            "waveforms": {"I": "EOM_cw_wf", "Q": "zero_wf"},
            "digital_marker": "OFF",
        },
        "EOM_pi_pulse": {
            "operation": "control",
            "length": EOM_pi_len,
            "waveforms": {"I": "EOM_pi_wf", "Q": "zero_wf"},
        },
        "EOM_pi_half_pulse": {
            "operation": "control",
            "length": EOM_pi_half_len,
            "waveforms": {"I": "EOM_pi_half_wf", "Q": "zero_wf"},
        },
        "mwe_const_pulse": {
            "operation": "control",
            "length": mwe_len,
            "waveforms": {"I": "mwe_cw_wf", "Q": "zero_wf"},
        },
        "mwe_pi_pulse": {
            "operation": "control",
            "length": mwe_pi_len,
            "waveforms": {"I": "mwe_pi_wf", "Q": "zero_wf"},
        },
        "mwe_pi_half_pulse": {
            "operation": "control",
            "length": mwe_pi_half_len,
            "waveforms": {"I": "mwe_pi_half_wf", "Q": "zero_wf"},
        },
        "mwg_const_pulse": {
            "operation": "control",
            "length": mwg_len,
            "waveforms": {"I": "mwg_cw_wf", "Q": "zero_wf"},
        },
        "mwg_pi_pulse": {
            "operation": "control",
            "length": mwg_pi_len,
            "waveforms": {"I": "mwg_pi_wf", "Q": "zero_wf"},
        },
        "mwg_pi_half_pulse": {
            "operation": "control",
            "length": mwg_pi_half_len,
            "waveforms": {"I": "mwg_pi_half_wf", "Q": "zero_wf"},
        },
        "AOM1_ON": {
            "operation": "control",
            "length": AOM1_len,
            "waveforms": {"single": "AOM_wf"},
        },
        "AOM2_ON": {
            "operation": "control",
            "length": AOM2_len,
            "waveforms": {"single": "AOM_wf"},
        },
        "AOM_ON": {
            "operation": "control",
            "length": AOM_len,
            "waveforms": {"single": "AOM_wf"},
        },
        "laser_ON": {
            "operation": "control",
            "length": initialization_len,
            "digital_marker": "ON",
        },
        "readout_pulse": {
            "operation": "measurement",
            "length": meas_len,
            "digital_marker": "ON",
        },
        "long_readout_pulse": {
            "operation": "measurement",
            "length": long_meas_len,
            "digital_marker": "ON",
        },
        "RF_switch_ON": {
            "operation": "control",
            "length": RF_switch_len,
            "digital_marker": "ON",
        },
    },
    "waveforms": {
        "EOM_cw_wf": {"type": "constant", "sample": EOM_amp},
        "EOM_pi_wf": {"type": "constant", "sample": EOM_pi_amp},
        "EOM_pi_half_wf": {"type": "constant", "sample": EOM_pi_half_amp},
        "mwe_cw_wf": {"type": "constant", "sample": mwe_amp},
        "mwe_pi_wf": {"type": "constant", "sample": mwe_pi_amp},
        "mwe_pi_half_wf": {"type": "constant", "sample": mwe_pi_half_amp},
        "mwg_cw_wf": {"type": "constant", "sample": mwg_amp},
        "mwg_pi_wf": {"type": "constant", "sample": mwg_pi_amp},
        "mwg_pi_half_wf": {"type": "constant", "sample": mwg_pi_half_amp},
        "zero_wf": {"type": "constant", "sample": 0.0},
        "AOM_wf": {"type": "constant", "sample": AOM_amp},  #
    },
    "digital_waveforms": {
        "ON": {"samples": [(1, 0)]},  # [(on/off, ns)]
        "OFF": {"samples": [(0, 0)]},  # [(on/off, ns)]
    },
}
