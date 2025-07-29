from pathlib import Path
import numpy as np
from qualang_tools.config.waveform_tools import drag_gaussian_pulse_waveforms
from qualang_tools.units import unit

# These packages are imported here so that we don't have to import them in all the other files
from qualang_tools.plot import interrupt_on_close
from qualang_tools.results import progress_counter, fetching_tool
import plotly.io as pio

pio.renderers.default = "browser"

#######################
# AUXILIARY FUNCTIONS #
#######################
u = unit(coerce_to_integer=True)
# Used to correct for IQ mixer imbalances


######################
# Network parameters #
######################
# IP address of the Quantum Orchestration Platform
qop_ip = "172.16.33.101"
cluster_name = "CS_2"


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

# Frequencies
AOM_IF = 100 * u.MHz

# Gaussian pulse parameters
gauss_amp = 0.3  # The gaussian is used when calibrating pi and pi_half pulses
gauss_len = 20  # The gaussian is used when calibrating pi and pi_half pulses
gauss_wf, gauss_der_wf = drag_gaussian_pulse_waveforms(
    gauss_amp, gauss_len, gauss_len / 5, alpha=0, delta=1, anharmonicity=0, detuning=0, subtracted=True
)

# Square pulse parameters
square_len = 16 # in ns
square_amp = 0.1 # in Volts

# Trigger pulse parameters
trigger_len = 320  # in ns

config = {
    "version": 1,
    "controllers": {
        "con1": {
            "analog_outputs": {
                1: {"offset": +0.0},
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
        "AOM": {
            "singleInput": {"port": ("con1", 1)},
            "intermediate_frequency": AOM_IF,
            "operations": {
                "const": "square_pulse",
                "gauss": "gaussian_pulse",
            },
            "digitalInputs": {
                "laser": {
                    "port": ("con1", 1),
                    "delay": 0,
                    "buffer": 0,
                },
            },
        },
        "trigger": {
            "digitalInputs": {
                "activate": {
                    "port": ("con1", 1),
                    "delay": 0,
                    "buffer": 0,
                },
            },
            "operations": {
                "ON": "ON_pulse",
            },
        },
    },
    "pulses": {
        "ON_pulse": {
            "operation": "control",
            "length": trigger_len,
            "digital_marker": "ON",
        },
        "gaussian_pulse": {
            "operation": "control",
            "length": gauss_len,  # in ns
            "waveforms": {"single": "gaussian_wf"},
        },
        "square_pulse": {"operation": "control", "length": square_len, "waveforms": {"single": "square_wf"}},  # in ns
    },
    "waveforms": {
        "square_wf": {"type": "constant", "sample": square_amp},
        "gaussian_wf": {"type": "arbitrary", "samples": gauss_wf},
    },
    "digital_waveforms": {
        "ON": {"samples": [(1, 0)]},
    },
}
