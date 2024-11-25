# %%
from pathlib import Path
from set_octave import OctaveUnit, octave_declaration
from qualang_tools.units import unit


#######################
# AUXILIARY FUNCTIONS #
#######################
u = unit(coerce_to_integer=True)


#############
# VARIABLES #
#############
qop_ip = "172.16.33.101"  # Write the OPX IP address
cluster_name = "Cluster_81"  # Write your cluster_name if version >= QOP220
qop_port = None  # Write the QOP port if version < QOP220
con = "con1"

# The Octave port is 11xxx, where xxx are the last three digits of the Octave internal IP that can be accessed from
# the OPX admin panel if you QOP version is >= QOP220. Otherwise, it is 50 for Octave1, then 51, 52 and so on.
octave_1 = OctaveUnit("octave1", qop_ip, port=11232, con=con)
# octave_2 = OctaveUnit("octave2", qop_ip, port=11051, con=con)

# Add the octaves
octaves = [octave_1]
# Configure the Octaves
octave_config = octave_declaration(octaves)


# Path to save data
save_dir = Path().absolute() / "data"
save_dir.mkdir(exist_ok=True)
default_additional_files = {
    "configuration_mw_fem.py": "configuration_mw_fem.py",
    "optimal_weights.npz": "optimal_weights.npz",
}


#############
# VARIABLES #
#############
# Frequencies
mw_IF_freq = 40 * u.MHz
mw_LO_freq = 2.83 * u.GHz

# Pulses lengths
initialization_len = 3000 * u.ns
meas_len = 500 * u.ns
long_meas_len = 5_000 * u.ns
wait_between_runs = 1000 * u.ns

# MW parameters
mw_amp = 0.2  # in units of volts
mw_len = 200 * u.ns

pi_amp = 0.1  # in units of volts
pi_len = 32  # in units of ns
pi_half_amp = pi_amp / 2  # in units of volts
pi_half_len = pi_len  # in units of ns

# Readout parameters
signal_threshold = -2_000  # ADC untis, to convert to volts divide by 4096 (12 bit ADC)

# Delays
time_of_flight = 28 * u.ns
detection_delay = 80 * u.ns
laser_delay = 0 * u.ns
mw_delay = 0 * u.ns

trigger_delay = 87  # 57ns with QOP222 and above otherwise 87ns
trigger_buffer = 15  # 18ns with QOP222 and above otherwise 15ns

#############################################
#                  Config                   #
#############################################

config = {
    "version": 1,
    "controllers": {
        "con1": {
            "analog_outputs": {
                1: {"offset": 0.0, "delay": mw_delay},  # NV I
                2: {"offset": 0.0, "delay": mw_delay},  # NV Q
            },
            "digital_outputs": {
                1: {},  # AOM/Laser
                2: {},  # SPCM - indicator
            },
            "analog_inputs": {
                1: {"offset": 0},  # SPCM
            },
        }
    },
    "elements": {
        "NV": {
            "RF_inputs": {"port": ("octave1", 1)},
            "intermediate_frequency": mw_IF_freq,
            "operations": {
                "cw": "const_pulse",
                "x180": "x180_pulse",
                "x90": "x90_pulse",
                "-x90": "-x90_pulse",
                "-y90": "-y90_pulse",
                "y90": "y90_pulse",
                "y180": "y180_pulse",
            },
            "digitalInputs": {
                "marker": {
                    "port": ("con1", 1),
                    "delay": trigger_delay,
                    "buffer": trigger_buffer,
                },
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
        "SPCM": {
            "singleInput": {"port": ("con1", 1)},  # not used
            "digitalInputs": {  # for visualization in simulation
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
                "derivativeThreshold": -2_000,
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
                    "LO_frequency": mw_LO_freq,
                    "LO_source": "internal",  # can be external or internal. internal is the default
                    "output_mode": "always_on",  # can be: "always_on" / "always_off"/ "triggered" / "triggered_reversed". "always_off" is the default
                    "gain": 0,  # can be in the range [-20 : 0.5 : 20]dB
                },
            },
            "connectivity": "con1",
        }
    },
    "pulses": {
        "const_pulse": {
            "operation": "control",
            "length": mw_len,
            "waveforms": {"I": "const_wf", "Q": "zero_wf"},
        },
        "x180_pulse": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {"I": "x180_wf", "Q": "zero_wf"},
        },
        "x90_pulse": {
            "operation": "control",
            "length": pi_half_len,
            "waveforms": {"I": "x90_wf", "Q": "zero_wf"},
        },
        "-x90_pulse": {
            "operation": "control",
            "length": pi_half_len,
            "waveforms": {"I": "minus_x90_wf", "Q": "zero_wf"},
        },
        "y180_pulse": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {"I": "zero_wf", "Q": "x180_wf"},
        },
        "y90_pulse": {
            "operation": "control",
            "length": pi_half_len,
            "waveforms": {"I": "zero_wf", "Q": "x90_wf"},
        },
        "-y90_pulse": {
            "operation": "control",
            "length": pi_half_len,
            "waveforms": {"I": "zero_wf", "Q": "minus_x90_wf"},
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
            "waveforms": {"single": "zero_wf"},
        },
        "long_readout_pulse": {
            "operation": "measurement",
            "length": long_meas_len,
            "digital_marker": "ON",
            "waveforms": {"single": "zero_wf"},
        },
    },
    "waveforms": {
        "zero_wf": {"type": "constant", "sample": 0.0},
        "const_wf": {"type": "constant", "sample": mw_amp},
        "x180_wf": {"type": "constant", "sample": pi_amp},
        "x90_wf": {"type": "constant", "sample": pi_half_amp},
        "minus_x90_wf": {"type": "constant", "sample": -pi_half_amp},
    },
    "digital_waveforms": {
        "ON": {"samples": [(1, 0)]},  # [(on/off, ns)]
        "OFF": {"samples": [(0, 0)]},  # [(on/off, ns)]
    },
}
