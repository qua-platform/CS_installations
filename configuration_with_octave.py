import os
import numpy as np
from qm.octave import QmOctaveConfig
from qualang_tools.units import unit
from qualang_tools.plot import interrupt_on_close
from qualang_tools.results import progress_counter, fetching_tool
from qualang_tools.loops import from_array

#######################
# AUXILIARY FUNCTIONS #
#######################
u = unit(coerce_to_integer=True)


#############
# VARIABLES #
#############
qop_ip = "127.0.0.1"  # Write the OPX IP address
cluster_name = "Cluster_1"  # Write your cluster_name if version >= QOP220
qop_port = None  # Write the QOP port if version < QOP220
octave_ip = qop_ip  # Write the Octave IP address
octave_port = 11050  # 11xxx, where xxx are the last three digits of the Octave IP address


############################
# Set octave configuration #
############################
octave_config = QmOctaveConfig()
octave_config.set_calibration_db(os.getcwd())
octave_config.add_device_info("octave1", octave_ip, octave_port)


#############
# VARIABLES #
#############
# Frequencies
NV_IF_freq = 40 * u.MHz
NV_LO_freq = 2.83 * u.GHz

# Pulses lengths
initialization_len = 3000 * u.ns
meas_len = 500 * u.ns
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

# Readout parameters
signal_threshold = -2_000  # ADC untis, to convert to volts divide by 4096 (12 bit ADC)

# Delays
detection_delay = 80 * u.ns
laser_delay = 0 * u.ns
mw_delay = 0 * u.ns
rf_delay = 0 * u.ns

trigger_delay = 87  # 57ns with QOP222 and above otherwise 87ns
trigger_buffer = 15  # 18ns with QOP222 and above otherwise 15ns

wait_after_measure = 1 * u.us  # Wait time after each measurement

#############################################
#                  Config                   #
#############################################
wait_between_runs = 100

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
                1: {},  # Octave switch
                2: {},  # AOM/Laser 1
                3: {},  # SPCM1 - indicator
            },
            "analog_inputs": {
                1: {"offset": 0},  # SPCM1
                2: {"offset": 0},  # SPCM2
            },
        }
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
        "AOM1": {
            "digitalInputs": {
                "marker": {
                    "port": ("con1", 2),
                    "delay": laser_delay,
                    "buffer": 0,
                },
            },
            "operations": {
                "laser_ON": "laser_ON",
            },
        },
        "SPCM1": {
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
                    "LO_frequency": NV_LO_freq,
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
        "cw_wf": {"type": "constant", "sample": mw_amp_NV},
        "x180_wf": {"type": "constant", "sample": x180_amp_NV},
        "x90_wf": {"type": "constant", "sample": x90_amp_NV},
        "minus_x90_wf": {"type": "constant", "sample": -x90_amp_NV},
        "zero_wf": {"type": "constant", "sample": 0.0},
    },
    "digital_waveforms": {
        "ON": {"samples": [(1, 0)]},  # [(on/off, ns)]
        "OFF": {"samples": [(0, 0)]},  # [(on/off, ns)]
    },
}
