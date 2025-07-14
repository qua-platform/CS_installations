import numpy as np
from scipy.signal.windows import gaussian


#######################
# AUXILIARY FUNCTIONS #
#######################


# IQ imbalance matrix
def IQ_imbalance(g, phi):
    c = np.cos(phi)
    s = np.sin(phi)
    N = 1 / ((1 - g**2) * (2 * c**2 - 1))
    return [float(N * x) for x in [(1 - g) * c, (1 + g) * s, (1 - g) * s, (1 + g) * c]]


######################
# Network parameters #
######################
qop_ip = "172.16.33.101"  # Write the QM router IP address
cluster_name = "CS_2"  # Write your cluster_name if version >= QOP220
qop_port = None  # Write the QOP port if version < QOP220
octave_config = None

# These should be changed to your credentials.
QOP_VER = "v2_4_4"
EMAIL = "fabio@quantum-machines.co"
PWD = "97kL6z3Yn6hq"
HOST = "qm-saas.dev.quantum-machines.co"


#############
# VARIABLES #
#############

# Readout Resonator
readout_LO = 7e9
readout_IF = 30e6
readout_len = 200
readout_amp = 0.2

# Qubits
qubit_LO = 5e9
qubit_1_IF = 30e6
qubit_2_IF = 15e6
mixer_qubit_1_g = 0.0
mixer_qubit_1_phi = 0.0
mixer_qubit_2_g = 0.0
mixer_qubit_2_phi = 0.0

# Qubit Pulses
const_len = 100
const_amp = 0.4
gauss_len = 200
sqrt_amp = 0.2
gauss_sigma = gauss_len / 5
gauss_amp = 0.45
gauss_wf = gauss_amp * gaussian(gauss_len, gauss_sigma)
sqrt_wf = np.sqrt(np.linspace(0, sqrt_amp, const_len))
pi_len = 40
pi_sigma = pi_len / 5
pi_amp = 0.35
pi_wf = pi_amp * gaussian(pi_len, pi_sigma)
pi_half_len = 40
pi_half_sigma = pi_half_len / 5
pi_half_amp = pi_amp / 2
pi_half_wf = pi_half_amp * gaussian(pi_half_len, pi_half_sigma)


# Sequence
phase_coherence_pulse = 250
phase_coherence_delay = 5e6


##########
# CONFIG #
##########
con = "con1"
config = {
    "version": 1,
    "controllers": {
        con: {
            "type": "opx1",
            "analog_outputs": {
                1: {"offset": 0.0},  # I qubit
                2: {"offset": 0.0},  # Q qubit
                3: {"offset": 0.0},  # qubit_1
                # 4: {'offset': 0.0},  # qubit_2
                # 9: {'offset': 0.0},  # qubit_2
                10: {"offset": 0.0},  # junk
            },
            "analog_inputs": {
                1: {"offset": 0.0, "gain_db": 0},
                # 2: {'offset': 0.0, 'gain_db': 0},
            },
            "digital_outputs": {
                1: {},
            },
        },
    },
    "elements": {
        "readout_resonator": {
            "singleInput": {
                "port": (con, 1),
            },
            "outputs": {
                "out1": (con, 1),
            },
            "time_of_flight": 24,
            "smearing": 0,
            "intermediate_frequency": readout_IF,
            "operations": {
                "readout": "readout_pulse_single",
            },
        },
        "qubit_1": {
            "singleInput": {
                "port": (con, 2),
            },
            "intermediate_frequency": qubit_1_IF,
            "operations": {
                "x180": "const_pulse_single",
                "sqrt": "sqrt_pulse",
                "gauss": "gaussian_single",
            },
        },
        "qubit_2": {
            "singleInput": {
                "port": (con, 3),
            },
            "intermediate_frequency": qubit_1_IF,
            "operations": {
                "x180": "const_pulse_single",
                "sqrt": "sqrt_pulse",
                "gauss": "gaussian_single",
            },
        },
        "digital_start": {
            "digitalInputs": {
                "digital": {"buffer": 0, "delay": 0, "port": (con, 1)},
            },
            "operations": {
                "start": "digital_ON",
            },
        },
    },
    "pulses": {
        "const_pulse": {
            "operation": "control",
            "length": const_len,
            "waveforms": {
                "I": "const_wf",
                "Q": "zero_wf",
            },
        },
        "const_pulse_single": {
            "operation": "control",
            "length": const_len,
            "waveforms": {
                "single": "const_wf",
            },
        },
        "sqrt_pulse": {
            "operation": "control",
            "length": const_len,
            "waveforms": {
                "single": "sqrt_wf",
            },
        },
        "gaussian_pulse": {
            "operation": "control",
            "length": gauss_len,
            "waveforms": {
                "I": "gauss_wf",
                "Q": "zero_wf",
            },
        },
        "gaussian_single": {
            "operation": "control",
            "length": gauss_len,
            "waveforms": {
                "single": "gauss_wf",
            },
        },
        "pi_pulse": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "pi_wf",
                "Q": "zero_wf",
            },
        },
        "pi_half_pulse": {
            "operation": "control",
            "length": pi_half_len,
            "waveforms": {
                "I": "pi_half_wf",
                "Q": "zero_wf",
            },
        },
        "digital_ON": {
            "digital_marker": "ON",
            "length": 100,
            "operation": "control",
        },
        "readout_pulse_single": {
            "operation": "measurement",
            "length": readout_len,
            "waveforms": {
                "single": "readout_wf",
            },
            "integration_weights": {
                "cos": "cosine_weights",
                "sin": "sine_weights",
            },
            "digital_marker": "ON",
        },
    },
    "waveforms": {
        "const_wf": {"type": "constant", "sample": const_amp},
        "sqrt_wf": {"type": "arbitrary", "samples": sqrt_wf.tolist()},
        "zero_wf": {"type": "constant", "sample": 0.0},
        "gauss_wf": {"type": "arbitrary", "samples": gauss_wf.tolist()},
        "pi_wf": {"type": "arbitrary", "samples": pi_wf.tolist()},
        "pi_half_wf": {"type": "arbitrary", "samples": pi_half_wf.tolist()},
        "readout_wf": {"type": "constant", "sample": readout_amp},
    },
    "digital_waveforms": {
        "ON": {"samples": [(1, 0)]},
    },
    "integration_weights": {
        "cosine_weights": {
            "cosine": [(1.0, readout_len)],
            "sine": [(0.0, readout_len)],
        },
        "sine_weights": {
            "cosine": [(0.0, readout_len)],
            "sine": [(1.0, readout_len)],
        },
    },
    # "mixers": {
    #     "mixer_qubit_1": [
    #         {
    #             "intermediate_frequency": qubit_1_IF,
    #             "lo_frequency": qubit_LO,
    #             "correction": IQ_imbalance(mixer_qubit_1_g, mixer_qubit_1_phi),
    #         },
    #     ],
    #     "mixer_qubit_2": [
    #         {
    #             "intermediate_frequency": qubit_2_IF,
    #             "lo_frequency": qubit_LO,
    #             "correction": IQ_imbalance(mixer_qubit_2_g, mixer_qubit_2_phi),
    #         }
    #     ],
    # },
}
