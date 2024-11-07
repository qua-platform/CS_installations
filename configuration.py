import numpy as np
from qualang_tools.units import unit
from qualang_tools.plot import interrupt_on_close
from qualang_tools.results import progress_counter, fetching_tool


#############
# VARIABLES #
#############
u = unit(coerce_to_integer=True)
qop_ip = "172.16.33.101"  # QOP IP address
qop_port = None  # Write the QOP port if version < QOP220
cluster_name = "Cluster_83"  # Name of the cluster

# Frequencies
cooling_fm_freq = 0 * u.MHz # in units of Hz

# Pulses lengths
cooling_fm_len = 1000  # in ns

# MW parameters
cooling_fm_amp = 0.2  # in units of volts


config = {
    "version": 1,
    "controllers": {
        "con1": {
            "analog_outputs": {
                1: {"offset": 0.0, "delay": 0.0},
                2: {"offset": 0.0, "delay": 0.0},
                3: {"offset": 0.0, "delay": 0.0}, 
                4: {"offset": 0.0, "delay": 0.0},
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
                10: {},
            },
            "analog_inputs": {},
        }
    },
    "elements": {
        "cooling_fm": {
            "singleInput": {
                "port": ("con1", 1)
            },
            "intermediate_frequency": cooling_fm_freq,
            "operations": {
                "const": "const_pulse",
                "const_1us": "const_pulse_1us",
                "const_1ms": "const_pulse_1ms",
                "const_1s": "const_pulse_1s",
            },
        },
    },
    "pulses": {
        "const_pulse": {
            "operation": "control",
            "length": cooling_fm_len,
            "waveforms": {"single": "const_wf"},
        },
        "const_pulse_1us": {
            "operation": "control",
            "length": 1 * u.us,
            "waveforms": {"single": "const_wf"},
        },
        "const_pulse_1ms": {
            "operation": "control",
            "length": 1 * u.ms,
            "waveforms": {"single": "const_wf"},
        },
        "const_pulse_1s": {
            "operation": "control",
            "length": 1 * u.s,
            "waveforms": {"single": "const_wf"},
        },
    },
    "waveforms": {
        "const_wf": {"type": "constant", "sample": cooling_fm_amp},
        "zero_wf": {"type": "constant", "sample": 0.0},
    },
    "digital_waveforms": {
        "ON": {"samples": [(1, 0)]},  # [(on/off, ns)]
    },
}
