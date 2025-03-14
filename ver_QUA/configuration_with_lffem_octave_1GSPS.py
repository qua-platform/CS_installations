# %%
"""
QUA-Config supporting OPX1000 w/ MW-FEM
"""

from pathlib import Path
import numpy as np
from qualang_tools.config.waveform_tools import drag_gaussian_pulse_waveforms
from qualang_tools.units import unit


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
qop_ip = "172.16.33.115"
cluster_name = "Cluster_1" 
qop_port = 80  # Write the QOP port if version < QOP220

con = "con1"
lffem1 = 3
lffem2 = 5

# Path to save data
save_dir = Path().absolute() / "data"
save_dir.mkdir(exist_ok=True)
default_additional_files = {
    "configuration_with_lffem_octave.py": "configuration_with_lffem_octave.py",
    "optimal_weights.npz": "optimal_weights.npz",
}


#############################################
#                  Qubits                   #
#############################################
single_len = 100
single_amp = 0.25
single_IF = 250 * u.MHz

# TOF and depletion time
time_of_flight = 28  # must be a multiple of 4
depletion_time = 2 * u.us


#############################################
#                  Config                   #
#############################################
sampling_rate = 1e9
config = {
    "version": 1,
    "controllers": {
        con: {
            "type": "opx1000",
            "fems": {
                lffem2: {
                    "type": "LF",
                    "analog_outputs": {
                        **{
                            p: {
                                "offset": 0.0,
                                "output_mode": "direct",
                                "sampling_rate": sampling_rate,
                                # "upsampling_mode": "mw",
                            }
                            for p in range(1, 9, 1)
                        }
                    },
                    "digital_outputs": {
                    },
                    "analog_inputs": {
                        # I from down-conversion
                        1: {"offset": 0.0, "gain_db": 0, "sampling_rate": sampling_rate},
                        # Q from down-conversion
                        2: {"offset": 0.0, "gain_db": 0, "sampling_rate": sampling_rate},
                    },
                },
            },
        }
    },
    "elements": {
        **{
            f"rr_test{p}": {
                "singleInput": {
                    "port": (con, lffem2, p),
                },
                "intermediate_frequency": single_IF,  # in Hz
                "operations": {
                    "single": "single_pulse",
                },
                "outputs": {
                    "out1": (con, lffem2, 1),
                    "out2": (con, lffem2, 2),
                },
                "time_of_flight": 28,
                "smearing": 0,
            }
            for p in range(1, 9, 1)
        },
    },
    "pulses": {
        "single_pulse": {
            "operation": "measurement",
            "length": single_len,
            "waveforms": {
                "single": "single_wf",
            },
            "integration_weights": {
                "cos": "cosine_weights",
                "sin": "sine_weights",
                "minus_sin": "minus_sine_weights",
            },
            "digital_marker": "ON",
        },
    },
    "waveforms": {
        "single_wf": {"type": "constant", "sample": single_amp},
    },
    "digital_waveforms": {
        "ON": {"samples": [(1, 0)]},
    },
    "integration_weights": {
        "cosine_weights": {
            "cosine": [(1.0, single_len)],
            "sine": [(0.0, single_len)],
        },
        "sine_weights": {
            "cosine": [(0.0, single_len)],
            "sine": [(1.0, single_len)],
        },
        "minus_sine_weights": {
            "cosine": [(0.0, single_len)],
            "sine": [(-1.0, single_len)],
        },
    },
}

# %%
