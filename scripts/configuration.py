"""
QUA-Config supporting OPX1000 LF-FEM
"""

from pathlib import Path
from qualang_tools.units import unit
import plotly.io as pio
import numpy as np

pio.renderers.default = "browser"
#######################
# AUXILIARY FUNCTIONS #
#######################
u = unit(coerce_to_integer=True)


######################
# Network parameters #
######################
qop_ip = "172.16.33.115"  # Write the OPX IP address
cluster_name = "CS_3"  # Write your cluster_name if version >= QOP220
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
con = "con1"
fem = 5  # This should be the index of the LF-FEM module, e.g., 1
# Set octave_config to None if no octave are present
octave_config = None

# Frequencies
sampling_rate = int(1e9)  # or, int(2e9)

# AOM trapping parameters
AOM_trapping_frequency = 100 * u.MHz
AOM_trapping_amp = 0.1
rf_length = 1 * u.us

# AOM repump parameters
AOM_repump_frequency = 100 * u.MHz
AOM_repump_amp = 0.1

# AOM probe parameters
AOM_probe_frequency = 100 * u.MHz
AOM_probe_amp = 0.1

# B field parameters
b_amp = 0.1


# TTL parameters lengths
TTL_len_1 = 1 * u.us
TTL_len_2 = 1 * u.us
# measurement pulses
meas_len_1 = 1 * u.us
long_meas_len_1 = 5 * u.us

meas_len_2 = 1 * u.us
long_meas_len_2 = 5 * u.us

# Relaxation time from the metastable state to the ground state after during initialization
relaxation_time = 10 * u.us
wait_for_initialization = 5 * relaxation_time

# Photon source for time tagging simulation
gauss_len = 80
def gauss(amplitude, mu, sigma, length):
    t = np.linspace(-length / 2, length / 2 - 1, length)
    gauss_wave = amplitude * np.exp(-((t - mu) ** 2) / (2 * sigma ** 2))
    return [float(x) for x in gauss_wave]
gauss_pulse = gauss(0.2, 0, 10, gauss_len)

# Delays
detection_delay_1 = 80 * u.ns
detection_delay_2 = 80 * u.ns
laser_delay_1 = 0 * u.ns
laser_delay_2 = 0 * u.ns
mw_delay = 0 * u.ns

wait_between_runs = 100

config = {
    "version": 1,
    "controllers": {
        con: {
            "type": "opx1000",
            "fems": {
                fem: {
                    "type": "LF",
                    "analog_outputs": {
                        # AOM trapping
                        1: {
                            "offset": 0.0,
                            "delay": mw_delay,
                            # The "output_mode" can be used to tailor the max voltage and frequency bandwidth, i.e.,
                            #   "direct":    1Vpp (-0.5V to 0.5V), 750MHz bandwidth (default)
                            #   "amplified": 5Vpp (-2.5V to 2.5V), 330MHz bandwidth
                            # Note, 'offset' takes absolute values, e.g., if in amplified mode and want to output 2.0 V, then set "offset": 2.0
                            "output_mode": "direct",
                            # The "sampling_rate" can be adjusted by using more FEM cores, i.e.,
                            #   1 GS/s: uses one core per output (default)
                            #   2 GS/s: uses two cores per output
                            # NOTE: duration parameterization of arb. waveforms, sticky elements and chirping
                            #       aren't yet supported in 2 GS/s.
                            "sampling_rate": sampling_rate,
                            # At 1 GS/s, use the "upsampling_mode" to optimize output for
                            #   modulated pulses (optimized for modulated pulses):      "mw"    (default)
                            #   unmodulated pulses (optimized for clean step response): "pulse"
                            "upsampling_mode": "mw",
                        },
                        # AOM repump
                        2: {
                            "offset": 0.0,
                            "delay": mw_delay,
                            "output_mode": "direct",
                            "sampling_rate": sampling_rate,
                            "upsampling_mode": "mw",
                        },
                        # AOM probe
                        3: {
                            "offset": 0.0,
                            "delay": mw_delay,
                            "output_mode": "direct",
                            "sampling_rate": sampling_rate,
                            "upsampling_mode": "mw",
                        },
                        # B field
                        4: {
                            "offset": 0.0,
                            "delay": mw_delay,
                            "output_mode": "direct",
                            "sampling_rate": sampling_rate,
                            "upsampling_mode": "mw",
                        },
                        # photon source for time tagging simulation
                        5: {
                            "offset": 0.0,
                            "delay": 0,
                            "output_mode": "direct",
                            "sampling_rate": sampling_rate,
                            "upsampling_mode": "mw",
                        },
                    },
                    "digital_outputs": {
                        1: {},  # AOM trapping
                        2: {},  # AOM repump
                        3: {},  # AOM probe
                        4: {},  # SPCM1 - indicator
                        5: {},  # SPCM2 - indicator
                        6: {},  # TTL1
                        7: {},  # TTL2
                    },
                    "analog_inputs": {
                        1: {"offset": 0, "sampling_rate": sampling_rate},  # SPCM1/PMT
                        2: {"offset": 0, "sampling_rate": sampling_rate},  # SPCM2
                    },
                }
            },
        }
    },
    "elements": {
        "AOM_trapping": {
            "singleInput": {"port": (con, fem, 1)},
            "intermediate_frequency": AOM_trapping_frequency,
            "operations": {
                "const": "trapping_pulse",
            },
            "digitalInputs": {
                "marker": {
                    "port": (con, fem, 1),
                    "delay": laser_delay_1,
                    "buffer": 0,
                },
            },
        },
        "AOM_repump": {
            "singleInput": {"port": (con, fem, 2)},
            "intermediate_frequency": AOM_repump_frequency,
            "operations": {
                "const": "repump_pulse",
            },
            "digitalInputs": {
                "marker": {
                    "port": (con, fem, 2),
                    "delay": laser_delay_1,
                    "buffer": 0,
                },
            },
        },
        "AOM_probe": {
            "singleInput": {"port": (con, fem, 3)},
            "intermediate_frequency": AOM_probe_frequency,
            "operations": {
                "const": "probe_pulse",
            },
            "digitalInputs": {
                "marker": {
                    "port": (con, fem, 3),
                    "delay": laser_delay_1,
                    "buffer": 0,
                },
            },
        },
        "B_field": {
            "singleInput": {"port": (con, fem, 4)},
            "operations": {
                "const": "b_pulse",
            },
            'sticky': {
                'analog': True,
                'digital': True,
                'duration': 4,
            },
            "digitalInputs": {
                "marker": {
                    "port": (con, fem, 1),
                    "delay": laser_delay_1,
                    "buffer": 0,
                },
            },
        },
        "PMT": {
            "singleInput": {"port": (con, fem, 1)},  # not used
            "digitalInputs": {  # for visualization in simulation
                "marker": {
                    "port": (con, fem, 3),
                    "delay": detection_delay_1,
                    "buffer": 0,
                },
            },
            "operations": {
                "readout": "readout_pulse_1",
                "long_readout": "long_readout_pulse_1",
            },
            "outputs": {"out1": (con, fem, 1)},
            'timeTaggingParameters': {  # Time tagging parameters
                'signalThreshold': -500,
                'signalPolarity': 'Below',
                'derivativeThreshold': -10000,
                'derivativePolarity': 'Above'
            },
            "time_of_flight": detection_delay_1,
            "smearing": 0,
        },
        "SPCM1": {
            "singleInput": {"port": (con, fem, 1)},  # not used
            "digitalInputs": {  # for visualization in simulation
                "marker": {
                    "port": (con, fem, 3),
                    "delay": detection_delay_1,
                    "buffer": 0,
                },
            },
            "operations": {
                "readout": "readout_pulse_1",
                "long_readout": "long_readout_pulse_1",
            },
            "outputs": {"out1": (con, fem, 1)},
            'timeTaggingParameters': {   # Time tagging parameters
                    'signalThreshold': -500,
                    'signalPolarity': 'Below',
                    'derivativeThreshold': -10000,
                    'derivativePolarity': 'Above'
                },
            "time_of_flight": detection_delay_1,
            "smearing": 0,
        },
        "SPCM2": {
            "singleInput": {"port": (con, fem, 1)},  # not used
            "digitalInputs": {  # for visualization in simulation
                "marker": {
                    "port": (con, fem, 4),
                    "delay": detection_delay_2,
                    "buffer": 0,
                },
            },
            "operations": {
                "readout": "readout_pulse_2",
                "long_readout": "long_readout_pulse_2",
            },
            "outputs": {"out1": (con, fem, 2)},
            'timeTaggingParameters': {   # Time tagging parameters
                    'signalThreshold': -500,
                    'signalPolarity': 'Below',
                    'derivativeThreshold': -10000,
                    'derivativePolarity': 'Above'
                },
            "time_of_flight": detection_delay_2,
            "smearing": 0,
        },
        "TTL1": {
            "digitalInputs": {
                "marker": {
                    "port": (con, fem, 6),
                    "delay": laser_delay_2,
                    "buffer": 0,
                },
            },
            "operations": {
                "ON": "TTL_1",
            },
        },
        "TTL2": {
            "digitalInputs": {
                "marker": {
                    "port": (con, fem, 7),
                    "delay": laser_delay_2,
                    "buffer": 0,
                },
            },
            "operations": {
                "ON": "TTL_2",
            },
        },
        'photon_source': {
            "singleInput": {"port": (con, fem, 5)},
            'operations': {
                'gauss': 'gauss_pulse',

            }
        },
    },
    "pulses": {
        "trapping_pulse": {
            "operation": "control",
            "length": rf_length,  # in ns
            "waveforms": {"single": "trapping_const_wf"},
            "digital_marker": "ON",
        },
        "repump_pulse": {
            "operation": "control",
            "length": rf_length,  # in ns
            "waveforms": {"single": "repump_const_wf"},
            "digital_marker": "ON",
        },
        "probe_pulse": {
            "operation": "control",
            "length": rf_length,  # in ns
            "waveforms": {"single": "probe_const_wf"},
            "digital_marker": "ON",
        },
        "b_pulse": {
            "operation": "control",
            "length": rf_length,  # in ns
            "waveforms": {"single": "b_const_wf"},
            "digital_marker": "ON",
        },
        "TTL_1": {
            "operation": "control",
            "length": TTL_len_1,
            "digital_marker": "ON",
        },
        "TTL_2": {
            "operation": "control",
            "length": TTL_len_2,
            "digital_marker": "ON",
        },
        "readout_pulse_1": {
            "operation": "measurement",
            "length": meas_len_1,
            "digital_marker": "ON",
            "waveforms": {"single": "zero_wf"},
        },
        "long_readout_pulse_1": {
            "operation": "measurement",
            "length": long_meas_len_1,
            "digital_marker": "ON",
            "waveforms": {"single": "zero_wf"},
        },
        "readout_pulse_2": {
            "operation": "measurement",
            "length": meas_len_2,
            "digital_marker": "ON",
            "waveforms": {"single": "zero_wf"},
        },
        "long_readout_pulse_2": {
            "operation": "measurement",
            "length": long_meas_len_2,
            "digital_marker": "ON",
            "waveforms": {"single": "zero_wf"},
        },
        'gauss_pulse': {
            'operation': "control",
            'length': gauss_len,
            'waveforms': {'single': 'gauss_wf'},
        },
    },
    "waveforms": {
        "trapping_const_wf": {"type": "constant", "sample": AOM_trapping_amp},
        "repump_const_wf": {"type": "constant", "sample": AOM_trapping_amp},
        "probe_const_wf": {"type": "constant", "sample": AOM_trapping_amp},
        "b_const_wf": {"type": "constant", "sample": b_amp},
        "zero_wf": {"type": "constant", "sample": 0.0},
        "gauss_wf": {"type": "arbitrary", "samples": gauss_pulse},
    },
    "digital_waveforms": {
        "ON": {"samples": [(1, 0)]},  # [(on/off, ns)]
        "OFF": {"samples": [(0, 0)]},  # [(on/off, ns)]
    },
}