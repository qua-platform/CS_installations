# %%

import os
from pathlib import Path
import numpy as np
from qualang_tools.config.waveform_tools import (
    drag_gaussian_pulse_waveforms,
    flattop_gaussian_waveform,
    drag_cosine_pulse_waveforms,
)
from qualang_tools.units import unit


#######################
# AUXILIARY FUNCTIONS #
#######################
u = unit(coerce_to_integer=True)


######################
# Network parameters #
######################
# qop_ip = "192.168.88.252"  # Write the QM router IP address
# cluster_name = "Cluster_1"  # Write your cluster_name if version >= QOP220
qop_ip = "172.16.33.101"  # Write the QM router IP address
cluster_name = "CS_2"  # Write your cluster_name if version >= QOP220
qop_port = None  # Write the QOP port if version < QOP220
octave_config = None


#############
# Save Path #
#############

# Path to save data
# save_dir = Path(r"C:\Users\OhmoriG-X1\Desktop\CS_installations-HI_10Jun2025/data")
save_dir = Path("/workspaces/data")

save_dir.mkdir(exist_ok=True)

default_additional_files = {
    "configuration.py": "configuration.py",
}


##################
# Util Functions #
##################

# Path to save data


def blackman(t, v_start, v_end):
    """
    Amplitude waveform that minimizes the amount of side lobes in the Fourier domain.
    :param t: pulse duration [ns] (int)
    :param v_start: start amplitude [V] (float)
    :param v_end: end amplitude [V] (float)
    :return:
    """
    time_vector = np.asarray([x * 1.0 for x in range(int(t))])
    black = v_start + (
        time_vector / t
        - (25 / (42 * np.pi)) * np.sin(2 * np.pi * time_vector / t)
        + (1 / (21 * np.pi)) * np.sin(4 * np.pi * time_vector / t)
    ) * (v_end - v_start)
    return black


def print_2d(matrix):
    """
    Nicely prints a 2D array
    :param matrix: 2D python array
    """
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(f"{matrix[i][j]}\t", end="")
        print("")


#############
# VARIABLES #
#############

# --> Array geometry
# Number of cols
num_cols = 8
# Number of rows
num_rows = 8
# Maximum number of tweezers available
max_num_tweezers = 8
# Number of configured tweezers, if it increases don't forget to update the "align" in the QUA program
n_tweezers = 8
n_segment_py = 50

# --> Chirp pulse
# Amplitude of each individual tweezer
# WARNING: total output cannot exceed 0.5V
const_pulse_amp = 0.5 / max_num_tweezers  # Must be < 0.49/max_num_tweezers
# Duration of tweezer frequency chirp
const_pulse_len = 100 * u.us
# Analog readout threshold discriminating between atom and no-atom [V]
threshold = 0.0000

# --> Blackman pulses
# Amplitude of the Blackman pulse which should match the amplitude of the tweezers during frequency chirps
blackman_amp = const_pulse_amp
# Duration of the Blackman pulse for ramping up and down the tweezers power
blackman_pulse_len = 0.3 * u.ms
# Reduced sampling rate for generating long pulses without memory issues
sampling_rate = 100 * u.MHz  # Used for Blackman_long_pulse_len

# Tweezer col phases
phases_list = [0.1, 0.4, 0.9, 0.3, 0.7, 0.2, 0.5, 0.8, 0.0, 0.6]
# --> Col frequencies
col_spacing = -10 * u.MHz  # in Hz
col_IF_01 = 200 * u.MHz  # in Hz
col_IFs = [int(col_IF_01 + col_spacing * i) for i in range(num_cols)]
# --> Row frequencies
row_spacing = -10 * u.MHz  # in Hz
row_IF_01 = 200 * u.MHz  # in Hz
row_IFs = [row_IF_01 + row_spacing * x for x in range(num_rows)]

# Readout time of the occupation matrix sent by fpga
readout_fpga_len = 60
# Readout duration for acquiring the spectrographs
readout_pulse_len = blackman_pulse_len * 2 + const_pulse_len  # 2 * u.us
short_readout_pulse_len = 0.4 * u.us

occupation_matrix_pulse_len = 3 * readout_fpga_len + 200
occupation_matrix_pulse_amp = 0.5

artiq_trigger_len = 20_000

# # Qubit Drive RF
# qubit_LO = 9.4e9  # Hz
# qubit_IF = 100 * u.MHz  # Hz
# const_mw_pulse_len = 100e3  # ns
# const_mw_pulse_amp = 0.3  # V

# Voltage offset the col and row analog outputs
row_selector_voltage_offset = 0.0
col_selector_voltage_offset = 0.0
# mw_I_voltage_offset = 0.0
# mw_Q_voltage_offset = 0.0

# Analog output connected to the col AOD
col_channel = 1
# Analog output connected to the row AOD
row_channel = 2
# # Analog output connected the the mw I port
# mw_I = 3
# # Analog output connected the the mw Q port
# mw_Q = 4


config = {
    "version": 1,
    "controllers": {
        "con1": {
            "type": "opx1",
            "analog_outputs": {
                col_channel: {"offset": col_selector_voltage_offset},  # Col AOD tone
                row_channel: {"offset": row_selector_voltage_offset},  # Row AOD tone
                # mw_I: {"offset": mw_I_voltage_offset},  # MW I port
                # mw_Q: {"offset": mw_Q_voltage_offset},  # MW Q port
                9: {"offset": 0.0},  # Fake port for measurement
                10: {"offset": 0.008},  # Fake port for measurement
            },
            "digital_outputs": {
                1: {},
            },  # Not used yet
            "analog_inputs": {
                1: {"offset": 0.0},  # Analog input 1 used for fpga readout
                # 2: {"offset": 0.0},  # Not used yet
            },
        },
    },
    "elements": {
        # fpga is used to read the occupation matrix sent by fpga
        "occupation_matrix_dummy": {
            "singleInput": {
                "port": ("con1", 9),
            },  # Fake output port for measurement
            "intermediate_frequency": 0,
            "operations": {
                "const": "const_pulse",
                "on": "unit_pulse",
                "off": "zero_pulse",
            },
        },
        # fpga is used to read the occupation matrix sent by fpga
        "fpga": {
            "singleInput": {
                "port": ("con1", 10),
            },  # Fake output port for measurement
            "intermediate_frequency": 0,
            "operations": {
                "const": "const_pulse",
                "readout_fpga": "readout_fpga_pulse",
            },
            "outputs": {
                "out1": ("con1", 1),
            },
            "time_of_flight": 24 + 176,
            "smearing": 0,
        },
        # detector is used to acquire the spectrographs for debuging
        "detector": {
            "singleInput": {
                "port": ("con1", 10),
            },
            "intermediate_frequency": 0,
            "operations": {
                "const": "const_pulse",
                "readout": "readout_pulse",
                "short_readout": "short_readout_pulse",
            },
            "outputs": {
                "out1": ("con1", 1),
            },
            "time_of_flight": 24 + 176,  # with ext. trigger: 24 + 176 ns
            "smearing": 0,
        },
        # row_selector is used to control the row AOD
        **{
            f"row_selector_{i + 1:02d}": {
                "singleInput": {
                    "port": ("con1", row_channel),
                },
                "intermediate_frequency": row_IFs[i],
                "operations": {
                    "blackman_up": "blackman_up_pulse",
                    "blackman_down": "blackman_down_pulse",
                    "const": "const_pulse",
                },
            }
            for i in range(n_tweezers)
        },
        # col_selector is used to control the column AOD
        **{
            f"col_selector_{i + 1:02d}": {
                "singleInput": {
                    "port": ("con1", col_channel),
                },
                "intermediate_frequency": col_IFs[i],
                "operations": {
                    "blackman_up": "blackman_up_pulse",
                    "blackman_down": "blackman_down_pulse",
                    "const": "const_pulse",
                },
            }
            for i in range(n_tweezers)
        },
        "trigger_artiq": {
            "digitalInputs": {
                "marker": {
                    "port": ("con1", 1),
                    "delay": 0,
                    "buffer": 0,
                },
            },
            "operations": {
                "on": "artiq_trigger_ON",
            },
        },
        # "qubit": {
        #     "mixInputs": {
        #         # Connect the I qubit mixer component to output "mw_I" of the OPX
        #         "I": ("con1", mw_I),
        #         # Connect the Q qubit mixer component to output "mw_Q" of the OPX
        #         "Q": ("con1", mw_Q),
        #         # Qubit local oscillator frequency in Hz (int)
        #         "lo_frequency": qubit_LO,
        #         # Associate a mixer entity to control the IQ mixing process
        #         "mixer": "mixer_qubit",
        #     },
        #     # Resonant frequency of the qubit
        #     "intermediate_frequency": qubit_IF,
        #     # Define the set of operations doable on the qubit, each operation is related to a pulse
        #     "operations": {
        #         "const": "const_pulse",
        #         "const_mw": "const_mw_pulse",
        #     },
        # },
    },
    "pulses": {
        "readout_fpga_pulse": {
            "operation": "measurement",
            "length": readout_fpga_len,
            "waveforms": {
                "single": "zero_wf",
            },
            "digital_marker": "ON",
            "integration_weights": {
                "const_fpga": "const_fpga_weights",
            },
        },
        "readout_pulse": {
            "operation": "measurement",
            "length": readout_pulse_len,
            "waveforms": {
                "single": "zero_wf",
            },
            "integration_weights": {
                "cos": "cosine_weights",
                "sin": "sine_weights",
                "const": "const_weights",
            },
            "digital_marker": "ON",
        },
        "short_readout_pulse": {
            "operation": "measurement",
            "length": short_readout_pulse_len,
            "waveforms": {
                "single": "zero_wf",
            },
            "integration_weights": {
                "cos": "cosine_weights",
                "sin": "sine_weights",
            },
            "digital_marker": "ON",
        },
        "blackman_up_pulse": {
            "operation": "control",
            "length": blackman_pulse_len,
            "waveforms": {
                "single": "blackman_up_wf",
            },
            "digital_marker": "ON",
        },
        "blackman_down_pulse": {
            "operation": "control",
            "length": blackman_pulse_len,
            "waveforms": {
                "single": "blackman_down_wf",
            },
            "digital_marker": "ON",
        },
        "const_pulse": {
            "operation": "control",
            "length": const_pulse_len,
            "waveforms": {
                "single": "const_wf",
            },
            "digital_marker": "ON",
        },
        "unit_pulse": {
            "operation": "control",
            "length": occupation_matrix_pulse_len,
            "waveforms": {
                "single": "unit_wf",
            },
            "digital_marker": "ON",
        },
        "zero_pulse": {
            "operation": "control",
            "length": occupation_matrix_pulse_len,
            "waveforms": {
                "single": "zero_wf",
            },
            "digital_marker": "ON",
        },
        "artiq_trigger_ON": {
            "operation": "control",
            "length": artiq_trigger_len,
            "digital_marker": "ON",
        },
        # "const_mw_pulse": {
        #     "operation": "control",
        #     "length": const_mw_pulse_len,
        #     "waveforms": {"I": "const_mw_wf", "Q": "zero_wf"},
        #     "digital_marker": "ON",
        # },
    },
    "waveforms": {
        "blackman_up_wf": {
            "type": "arbitrary",
            "samples": blackman(
                blackman_pulse_len / (1e9 / sampling_rate), 0, blackman_amp
            ),
            "sampling_rate": sampling_rate,
        },
        "blackman_down_wf": {
            "type": "arbitrary",
            "samples": blackman(
                blackman_pulse_len / (1e9 / sampling_rate), blackman_amp, 0
            ),
            "sampling_rate": sampling_rate,
        },
        "const_wf": {
            "type": "constant",
            "sample": const_pulse_amp,
        },
        "unit_wf": {
            "type": "constant",
            "sample": occupation_matrix_pulse_amp,
        },
        "zero_wf": {
            "type": "constant",
            "sample": 0.0,
        },
        # "const_mw_wf": {
        #     "type": "constant",
        #     "sample": const_mw_pulse_amp,
        # },
    },
    "digital_waveforms": {
        "ON": {"samples": [(1, 0)]},
    },
    "integration_weights": {
        "const_fpga_weights": {
            "cosine": [(1.0, readout_fpga_len)],
            "sine": [(0.0, readout_fpga_len)],
        },
        "const_weights": {
            "cosine": [(1.0, readout_pulse_len)],
            "sine": [(0.0, readout_pulse_len)],
        },
        "cosine_weights": {
            "cosine": [(1.0, readout_pulse_len)],
            "sine": [(0.0, readout_pulse_len)],
        },
        "sine_weights": {
            "cosine": [(0.0, readout_pulse_len)],
            "sine": [(1.0, readout_pulse_len)],
        },
    },
    # "mixers": {
    #     "mixer_qubit": [
    #         {
    #             "intermediate_frequency": qubit_IF,
    #             "lo_frequency": qubit_LO,
    #             "correction": [1.0, 0.0, 0.0, 1.0],
    #         }
    #     ],
    # },
}


# %%
