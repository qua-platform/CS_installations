from pathlib import Path
import numpy as np
from qualang_tools.units import unit
from qualang_tools.plot import interrupt_on_close
from qualang_tools.results import progress_counter, fetching_tool
from qualang_tools.loops import from_array
import plotly.io as pio

pio.renderers.default = "browser"

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
qop_ip = "172.16.33.101"  # Write the OPX IP address
cluster_name = "CS_2"  # Write your cluster_name if version >= QOP220
qop_port = None  # Write the QOP port if version < QOP220

#############
# Save Path #
#############
# Path to save data
save_dir = Path(__file__).parent.resolve() / "Data"
save_dir.mkdir(exist_ok=True)

default_additional_files = {
    Path(__file__).name: Path(__file__).name,
    "optimal_weights.npz": "optimal_weights.npz",
}

#####################
# OPX configuration #
#####################
# Set octave_config to None if no octave are present
octave_config = None

# Frequencies
NV_IF_freq = 40 * u.MHz
NV_LO_freq = 2.83 * u.GHz

# Pulses lengths
initialization_len = 1000 * u.ns
meas_len = 100 * u.ns
long_meas_len = 5_000 * u.ns

# Relaxation time from the metastable state to the ground state after during initialization
relaxation_time = 300 * u.ns
wait_for_initialization = 5 * relaxation_time

# MW parameters
mw_amp_NV = 0.2  # in units of volts
mw_len_NV = 100 * u.ns

x180_amp_NV = 0.1  # in units of volts
x180_len_NV = 32  # in units of ns

x90_amp_NV = x180_amp_NV / 2  # in units of volts
x90_len_NV = x180_len_NV  # in units of ns

# RF parameters
rf_frequency = 10 * u.MHz
rf_amp = 0.1
rf_length = 1000

# Readout parameters
signal_threshold = -2_000  # ADC untis, to convert to volts divide by 4096 (12 bit ADC)

# Delays
detection_delay = 36 * u.ns
laser_delay = 136 * u.ns
repump_laser_delay = 136 * u.ns
mw_delay = 0 * u.ns
rf_delay = 0 * u.ns

wait_pulse_time_for_background_measuremenets = True

wait_between_runs = 100
charge_checks_threshold = 100
max_tries = 3
config = {
    "version": 1,
    "controllers": {
        "con1": {
            "analog_outputs": {
                1: {"offset": 0.0, "delay": mw_delay},  # NV I
                2: {"offset": 0.0, "delay": mw_delay},  # NV Q
                3: {"offset": 0.0, "delay": rf_delay},  # RF
            },
            "digital_outputs": {
                1: {},  # AOM
                2: {},  # repump AOM
                3: {},  # APD
            },
            "analog_inputs": {
                1: {"offset": 0},  # SPCM1
                2: {"offset": 0},  # SPCM2
            },
        }
    },
    "elements": {
        "NV": {
            "mixInputs": {"I": ("con1", 1), "Q": ("con1", 2), "lo_frequency": NV_LO_freq, "mixer": "mixer_NV"},
            "intermediate_frequency": NV_IF_freq,
            "operations": {
                "cw": "const_pulse",
                "x180": "x180_pulse",
                "x90": "x90_pulse",
                "-x90": "-x90_pulse",
                "-y90": "-y90_pulse",
                "y90": "y90_pulse",
                "y180": "y180_pulse",
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
        "repump_AOM": {
            "digitalInputs": {
                "marker": {
                    "port": ("con1", 2),
                    "delay": repump_laser_delay,
                    "buffer": 0,
                },
            },
            "operations": {
                "laser_ON": "laser_ON",
            },
        },
        "APD": {
            "singleInput": {"port": ("con1", 1)},  # not used
            "digitalInputs": {  # for visualization in simulation
                "marker": {
                    "port": ("con1", 3),
                    "delay": detection_delay,
                    "buffer": 0,
                },
            },
            "operations": {
                "readout": "readout_pulse",
                "long_readout": "long_readout_pulse",
            },
            "outputs": {"out1": ("con1", 1)},
            "timeTaggingParameters": {
                "signalThreshold": signal_threshold,  # ADC units
                "signalPolarity": "Below",
                "derivativeThreshold": -2_000,
                "derivativePolarity": "Above",
            },
            "time_of_flight": detection_delay,
            "smearing": 0,
        },
        "RF": {
            "singleInput": {"port": ("con1", 3)},
            "intermediate_frequency": rf_frequency,
            "operations": {
                "const": "const_pulse_single",
                "x180": "x180_RF_pulse",
                "x90": "x90_RF_pulse",
            },
        },
    },
    "pulses": {
        "const_pulse": {
            "operation": "control",
            "length": mw_len_NV,
            "waveforms": {"I": "cw_wf", "Q": "zero_wf"},
        },
        "x180_pulse": {
            "operation": "control",
            "length": x180_len_NV,
            "waveforms": {"I": "x180_wf", "Q": "zero_wf"},
        },
        "x90_pulse": {
            "operation": "control",
            "length": x90_len_NV,
            "waveforms": {"I": "x90_wf", "Q": "zero_wf"},
        },
        "-x90_pulse": {
            "operation": "control",
            "length": x90_len_NV,
            "waveforms": {"I": "minus_x90_wf", "Q": "zero_wf"},
        },
        "-y90_pulse": {
            "operation": "control",
            "length": x90_len_NV,
            "waveforms": {"I": "zero_wf", "Q": "minus_x90_wf"},
        },
        "y90_pulse": {
            "operation": "control",
            "length": x90_len_NV,
            "waveforms": {"I": "zero_wf", "Q": "x90_wf"},
        },
        "y180_pulse": {
            "operation": "control",
            "length": x180_len_NV,
            "waveforms": {"I": "zero_wf", "Q": "x180_wf"},
        },
        "const_pulse_single": {
            "operation": "control",
            "length": rf_length,  # in ns
            "waveforms": {"single": "rf_const_wf"},
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
        "x180_RF_pulse": {
            "operation": "control",
            "length": x180_len_NV,
            "waveforms": {"single": "x180_wf"},
        },
        "x90_RF_pulse": {
            "operation": "control",
            "length": x90_len_NV,
            "waveforms": {"single": "x90_wf"},
        },
    },
    "waveforms": {
        "cw_wf": {"type": "constant", "sample": mw_amp_NV},
        "rf_const_wf": {"type": "constant", "sample": rf_amp},
        "x180_wf": {"type": "constant", "sample": x180_amp_NV},
        "x90_wf": {"type": "constant", "sample": x90_amp_NV},
        "minus_x90_wf": {"type": "constant", "sample": -x90_amp_NV},
        "zero_wf": {"type": "constant", "sample": 0.0},
    },
    "digital_waveforms": {
        "ON": {"samples": [(1, 0)]},  # [(on/off, ns)]
        "OFF": {"samples": [(0, 0)]},  # [(on/off, ns)]
    },
    "mixers": {
        "mixer_NV": [
            {"intermediate_frequency": NV_IF_freq, "lo_frequency": NV_LO_freq, "correction": IQ_imbalance(0.0, 0.0)},
        ],
    },
}
