from pathlib import Path
import numpy as np
from qualang_tools.units import unit
from set_octave import OctaveUnit, octave_declaration

######################
# Network parameters #
######################

u = unit(coerce_to_integer=True)
qop_ip = "127.0.0.1"
cluster_name = "Cluster_1"


############################
# Set octave configuration #
############################
# The Octave port is 11xxx, where xxx are the last three digits of the Octave internal IP that can be accessed from
# the OPX admin panel if you QOP version is >= QOP220. Otherwise, it is 50 for Octave1, then 51, 52 and so on.
octave_1 = OctaveUnit("octave1", qop_ip, port=11050, con="con1")
# Add the octaves
octaves = [octave_1]
# Configure the Octaves
octave_config = octave_declaration(octaves)


#############
# Save Path #
#############

# Path to base directories for script and data
base_dir = Path(__file__).resolve().parent
save_dir = base_dir / "Data"
save_dir.mkdir(parents=True, exist_ok=True)


#########
# Units #
#########
u = unit(coerce_to_integer=True)


#############
# VARIABLES #
#############
# mw pulses
NV_IF_freq = 40 * u.MHz
NV_LO_freq = 2.83 * u.GHz

mw_amp_NV = 0.025
mw_len_NV = 40 * u.ns

pi_amp_NV = 0.125  # in units of volts
pi_len_NV = 80 * u.ns 

pi_half_amp_NV = pi_amp_NV / 2
pi_half_len_NV = pi_len_NV

minus_pi_half_amp_NV = -1 * pi_half_amp_NV
minus_pi_half_len_NV = pi_len_NV

# trigger lengths
initialization_len = 2 * u.us # aom
meas_len = 300 * u.ns # for SPCM
long_meas_len = 5 * u.us # for SPCM

# delays
time_of_flight = 36 * u.ns
detection_delay = time_of_flight + 0 * u.ns # delay for SPCM
laser_delay1 = time_of_flight + 0 * u.ns # delay for AOM/Laser1
laser_delay2 = time_of_flight + 0 * u.ns # delay for AOM/Laser2
laser_delay3 = time_of_flight + 0 * u.ns # delay for AOM/Laser3
mw_delay = time_of_flight + 0 * u.ns # delay for MW

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

# counts at |0> and |1> measured with Rabi
count_on_rabi_g = 1000
count_on_rabi_e = 900


config = {
    "version": 1,
    "controllers": {
        "con1": {
            "analog_outputs": {
                1: {"offset": 0.0},  # NV MW I
                2: {"offset": 0.0},  # NV MW Q
            },
            "digital_outputs": {
                1: {},  # AOM/Laser1
                2: {},  # AOM/Laser2
                3: {},  # AOM/Laser3
                4: {},  # SPCM/SPCM
            },
            "analog_inputs": {
                1: {"offset": 0.0, "gain_db": 0},  # SPCM/SPCM
                2: {"offset": 0.0, "gain_db": 0},  # not used
            },
        },
    },
    "elements": {
        "NV": {
            "RF_inputs": {"port": ("octave1", 1)},
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
        "AOM1": {
            "digitalInputs": {
                "marker": {
                    "port": ("con1", 1), # digital output
                    "delay": laser_delay1,
                    "buffer": 0,
                },
            },
            "operations": {
                "laser_ON": "laser_ON",
            },
        },
        "AOM2": {
            "digitalInputs": {
                "marker": {
                    "port": ("con1", 2), # digital output
                    "delay": laser_delay1,
                    "buffer": 0,
                },
            },
            "operations": {
                "laser_ON": "laser_ON",
            },
        },
        "AOM3": {
            "digitalInputs": {
                "marker": {
                    "port": ("con1", 3), # digital output
                    "delay": laser_delay1,
                    "buffer": 0,
                },
            },
            "operations": {
                "laser_ON": "laser_ON",
            },
        },
        "SPCM": {
            "singleInput": {"port": ("con1", 4)},  # not used
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
    "octaves": {
        "octave1": {
            "RF_outputs": {
                1: {
                    "LO_frequency": NV_LO_freq,
                    "LO_source": "internal",
                    "output_mode": "always_on",
                    "gain": 0,
                },
            },
            "connectivity": "con1",
        }
    },
    "pulses": {
        "const_pulse": {
            "operation": "control",
            "length": mw_len_NV,
            "waveforms": {
                "I": "const_wf",
                "Q": "zero_wf",
            },
        },
        "x180_pulse": {
            "operation": "control",
            "length": pi_len_NV,
            "waveforms": {
                "I": "pi_wf",
                "Q": "zero_wf",
            },
        },
        "x90_pulse": {
            "operation": "control",
            "length": pi_half_len_NV,
            "waveforms": {
                "I": "pi_half_wf",
                "Q": "zero_wf",
            },
        },
        "-x90_pulse": {
            "operation": "control",
            "length": minus_pi_half_len_NV,
            "waveforms": {
                "I": "minus_pi_half_wf",
                "Q": "zero_wf",
            },
        },
        "y180_pulse": {
            "operation": "control",
            "length": pi_len_NV,
            "waveforms": {
                "I": "zero_wf",
                "Q": "pi_wf",
            },
        },
        "y90_pulse": {
            "operation": "control",
            "length": pi_half_len_NV,
            "waveforms": {
                "I": "zero_wf",
                "Q": "pi_half_wf",
            },
        },
        "-y90_pulse": {
            "operation": "control",
            "length": minus_pi_half_len_NV,
            "waveforms": {
                "I": "zero_wf",
                "Q": "minus_pi_half_wf",
            },
        },
        "laser_ON": {
            "operation": "control",
            "length": initialization_len,
            "digital_marker": "ON",
        },
        "readout_pulse": {
            "operation": "measurement",
            "length": meas_len,
            "waveforms": {"single": "zero_wf"},
            "integration_weights": {
                "const": "constant_weights",
            },
            "digital_marker": "ON",
        },
        "long_readout_pulse": {
            "operation": "measurement",
            "length": long_meas_len,
            "waveforms": {"single": "zero_wf"},
            "integration_weights": {
                "const": "long_constant_weights",
            },
            "digital_marker": "ON",
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
}
