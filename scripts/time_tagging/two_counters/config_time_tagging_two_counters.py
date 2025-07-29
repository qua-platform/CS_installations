import numpy as np
from qualang_tools.units import unit
from qualang_tools.plot import interrupt_on_close
from qualang_tools.results import progress_counter, fetching_tool


def gauss(amplitude, mu, sigma, length):
    t = np.linspace(-length / 2, length / 2 - 1, length)
    gauss_wave = amplitude * np.exp(-((t - mu) ** 2) / (2 * sigma ** 2))
    return [float(x) for x in gauss_wave]

u = unit()
# Readout parameters
signal_threshold_1 = -615
signal_threshold_2 = -350

# Delays
detection_delay = 80

pulse_len = 80
sigma = 10
gauss_pulse = gauss(0.2, 0, sigma, pulse_len)
gauss_pulse_half_amp = gauss(0.1, 0, sigma, pulse_len)
meas_len = 5_000
long_meas_len = 1000
gauss_len_nuclear = 80
nuclear_freq = 0
config = {
    "version": 1,
    "controllers": {
        "con1": {
            "type": "opx1",
            "analog_outputs": {
                1: {"offset": +0.0},
                2: {"offset": +0.0},
                3: {"offset": +0.0},
                4: {"offset": +0.0},
            },
            "digital_outputs": {
                1: {},
                2: {},
            },
            "analog_inputs": {
                1: {"offset": 0.0},
            },
        }
    },
    "elements": {
        'photon_source1': {
            "singleInput": {"port": ("con1", 1)},
            'intermediate_frequency': nuclear_freq,
            'operations': {
                'gauss': 'nuclear_gauss_pulse',
                'const': 'const_pulse',

            }
        },
        'photon_source2': {
            "singleInput": {"port": ("con1", 1)},
            'intermediate_frequency': nuclear_freq,
            'operations': {
                'gauss_half_amp': 'nuclear_gauss_pulse_half_amp',
                'const': 'const_pulse',

            }
        },
        "SNSPD1": {
            "singleInput": {"port": ("con1", 1)},  # not used
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
            'timeTaggingParameters': {  # Time tagging parameters
                'signalThreshold': signal_threshold_1,
                'signalPolarity': 'Below',
                'derivativeThreshold': -10000,
                'derivativePolarity': 'Above'
            },
            "time_of_flight": detection_delay,
            "smearing": 0,
        },
        "SNSPD2": {
            "singleInput": {"port": ("con1", 1)},  # not used
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
            'timeTaggingParameters': {  # Time tagging parameters
                'signalThreshold': signal_threshold_2,
                'signalPolarity': 'Below',
                'derivativeThreshold': -10000,
                'derivativePolarity': 'Above'
            },
            "time_of_flight": detection_delay,
            "smearing": 0,
        },
    },
    "pulses": {
        "const_pulse": {
            "operation": "control",
            "length": 80,  # in ns
            "waveforms": {"single": "const_wf"},
        },
        "constPulse_IQ": {
            "operation": "control",
            "length": 100,  # in ns
            "waveforms": {
                "I": "const_wf",
                "Q": "zero_wf",
            },
        },
        'nuclear_gauss_pulse': {
            'operation': "control",
            'length': gauss_len_nuclear,
            'waveforms': {'single': 'gauss_wf'},
        },
        'nuclear_gauss_pulse_half_amp': {
            'operation': "control",
            'length': gauss_len_nuclear,
            'waveforms': {'single': 'gauss_wf_half_amp'},
        },
        "gaussian_Pulse_IQ": {
            "operation": "control",
            "length": pulse_len,  # in ns
            "waveforms": {
                "I": "gauss_wf",
                "Q": "zero_wf",
            },
        },
        "gaussianPulse": {
            "operation": "control",
            "length": pulse_len,  # in ns
            "waveforms": {"single": "gauss_wf"},
        },
        "laser_on": {
            "digital_marker": "ON",
            "operation": "measurement",
            "length": 1000,  # in ns
            "waveforms": {"single": "zero_wf"},
        },
        "digital_ON": {
            "digital_marker": "ON",
            "length": 100,
            "operation": "control",
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
    "digital_waveforms": {
        "ON": {"samples": [(1, 0)]},
        "short": {"samples": [(1, 8),(0, 8)]},
    },
    "waveforms": {
        "const_wf": {"type": "constant", "sample": 0.2},
        "zero_wf": {"type": "constant", "sample": 0.0},
        "gauss_wf": {"type": "arbitrary", "samples": gauss_pulse},
        "gauss_wf_half_amp": {"type": "arbitrary", "samples": gauss_pulse_half_amp},
    },
}
