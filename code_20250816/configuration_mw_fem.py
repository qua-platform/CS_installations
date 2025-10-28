# %%

import os
from pathlib import Path
import numpy as np
from qualang_tools.config.waveform_tools import drag_gaussian_pulse_waveforms, flattop_gaussian_waveform, drag_cosine_pulse_waveforms
from qualang_tools.units import unit


#######################
# AUXILIARY FUNCTIONS #
#######################
u = unit(coerce_to_integer=True)


######################
# Network parameters #
######################
qop_ip = "172.16.33.114"  # Write the QM router IP address
cluster_name = 'CS_4'  # Write your cluster_name if version >= QOP220
qop_port = None  # Write the QOP port if version < QOP220
octave_config = None


######################
#       Utils        #
######################

def get_band(freq):
    """Determine the MW fem DAC band corresponding to a given frequency.

    Args:
        freq (float): The frequency in Hz.

    Returns:
        int: The Nyquist band number.
            - 1 if 50 MHz <= freq < 5.5 GHz
            - 2 if 4.5 GHz <= freq < 7.5 GHz
            - 3 if 6.5 GHz <= freq <= 10.5 GHz

    Raises:
        ValueError: If the frequency is outside the MW fem bandwidth [50 MHz, 10.5 GHz].
    """
    if 50e6 <= freq < 5.5e9:
        return 1
    elif 4.5e9 <= freq < 7.5e9:
        return 2
    elif 6.5e9 <= freq <= 10.5e9:
        return 3
    else:
        raise ValueError(f"The specified frequency {freq} Hz is outside of the MW fem bandwidth [50 MHz, 10.5 GHz]")



#############
# Save Path #
#############

# Path to save data
save_dir = Path(r"/workspaces/data")
save_dir.mkdir(exist_ok=True)

default_additional_files = {
    "configuration_mw_fem.py": "configuration_mw_fem.py",
    "optimal_weights.npz": "optimal_weights.npz",
}

# These should be changed to your credentials.
QOP_VER = "v3_3_0"
EMAIL = "fabio@quantum-machines.co"
PWD = "97kL6z3Yn6hq"
HOST = "qm-saas.dev.quantum-machines.co"

#####################
# OPX configuration #
#####################

mwfem_slot = 1

# MARK: QUBITS
#############################################
#                  Qubits                   #
#############################################
# CW pulse parameter
CONST_LEN = 100
CONST_AMP = 0.5 # 125 * u.mV

# Saturation_pulse
SATURATION_LEN = 100 * u.us
SATURATION_AMP = 0.4

# Constants for Pi Pulse
PI_LEN = 32 # less than 40 can cause issue with strict timing
PI_SIGMA = PI_LEN / 5

# Constants for each qubit
QUBIT_CONSTANTS = {
    "q1_xy": {
        "amp": 0.5,
        "pi_len": PI_LEN,
        "pi_sigma": PI_SIGMA,
        "anharmonicity": -200 * u.MHz,
        "drag_coefficient": 0.0,
        "ac_stark_shift": 0 * u.MHz, # 3.8 * u.MHz
        "LO": 5.0 * u.GHz,
        "IF": 100 * u.MHz,
        "con": "con1",
        "fem": mwfem_slot,
        "ao": 1,
        "band": 2,
        "full_scale_power_dbm": -11,
        "delay": 0,
        "core": "fem1-thread1",
    },
    "q2_xy": {
        "amp": 0.5,
        "pi_len": PI_LEN,
        "pi_sigma": PI_SIGMA, 
        "anharmonicity": -200 * u.MHz,
        "drag_coefficient": 0.0,
        "ac_stark_shift": 0.0 * u.MHz, # 3.8 * u.MHz
        "LO": 5.0 * u.GHz,
        "IF": 100 * u.MHz,
        "con": "con1",
        "fem": mwfem_slot,
        "ao": 2,
        "band": 2,
        "full_scale_power_dbm": -11,
        "delay": 0,
        "core": "fem1-thread2",
    },
    "q3_xy": {
        "amp": 0.5,
        "pi_len": PI_LEN,
        "pi_sigma": PI_SIGMA, 
        "anharmonicity": -200 * u.MHz,
        "drag_coefficient": 0.0,
        "ac_stark_shift": 0.0 * u.MHz, # 4.4 * u.MHz
        "LO": 5.0 * u.GHz,
        "IF": 100 * u.MHz,
        "con": "con1",
        "fem": mwfem_slot,
        "ao": 3,
        "band": 2,
        "full_scale_power_dbm": -11,
        "delay": 0,
        "core": "fem1-thread3",
    },
    "q4_xy": {
        "amp": 0.5,
        "pi_len": PI_LEN,
        "pi_sigma": PI_SIGMA, 
        "anharmonicity": -200 * u.MHz,
        "drag_coefficient": 0.0,
        "ac_stark_shift": 0.0 * u.MHz, # 5.0 * u.MHz
        "LO": 5.0 * u.GHz,
        "IF": 100 * u.MHz,
        "con": "con1",
        "fem": mwfem_slot,
        "ao": 4,
        "band": 2,
        "full_scale_power_dbm": -11,
        "delay": 0,
        "core": "fem1-thread4",
    },
    "q5_xy": {
        "amp": 0.5,
        "pi_len": PI_LEN,
        "pi_sigma": PI_SIGMA, 
        "anharmonicity": -200 * u.MHz,
        "drag_coefficient": 0.0,
        "ac_stark_shift": 0.0 * u.MHz, # 5.0 * u.MHz
        "LO": 5.0 * u.GHz,
        "IF": 100 * u.MHz,
        "con": "con1",
        "fem": mwfem_slot,
        "ao": 5,
        "band": 2,
        "full_scale_power_dbm": -11,
        "delay": 0,
        "core": "fem1-thread5",
    },
    "q6_xy": {
        "amp": 0.5,
        "pi_len": PI_LEN,
        "pi_sigma": PI_SIGMA, 
        "anharmonicity": -200 * u.MHz,
        "drag_coefficient": 0.0,
        "ac_stark_shift": 0.0 * u.MHz, # 5.0 * u.MHz
        "LO": 5.0 * u.GHz,
        "IF": 100 * u.MHz,
        "con": "con1",
        "fem": mwfem_slot,
        "ao": 6,
        "band": 2,
        "full_scale_power_dbm": -11,
        "delay": 0,
        "core": "fem1-thread6",
    },
    "q7_xy": {
        "amp": 0.5,
        "pi_len": PI_LEN,
        "pi_sigma": PI_SIGMA, 
        "anharmonicity": -200 * u.MHz,
        "drag_coefficient": 0.0,
        "ac_stark_shift": 0.0 * u.MHz, # 5.0 * u.MHz
        "LO": 5.0 * u.GHz,
        "IF": 100 * u.MHz,
        "con": "con1",
        "fem": mwfem_slot,
        "ao": 7,
        "band": 2,
        "full_scale_power_dbm": -11,
        "delay": 0,
        "core": "fem1-thread7",
    },
}


def generate_waveforms(rotation_keys):
    """ Generate all necessary waveforms for a set of rotation types across all qubits. """
    
    if not isinstance(rotation_keys, list):
        raise ValueError("rotation_keys must be a list")

    waveforms = {}

    for qb, constants in QUBIT_CONSTANTS.items():
        amp = constants["amp"]
        pi_len = constants["pi_len"]
        pi_sigma = constants["pi_sigma"]
        drag_coef = constants["drag_coefficient"]
        ac_stark_shift = constants["ac_stark_shift"]
        anharmonicity = constants["anharmonicity"]

        for rotation_key in rotation_keys:
            if rotation_key in ["x180", "y180"]:
                wf_amp = amp
            elif rotation_key in ["x90", "y90"]:
                wf_amp = amp / 2
            elif rotation_key in ["minus_x90", "minus_y90"]:
                wf_amp = -amp / 2
            else:
                continue

            # wf, der_wf = np.array(drag_gaussian_pulse_waveforms(wf_amp, pi_len, pi_sigma, drag_coef, anharmonicity, ac_stark_shift))
            wf, der_wf = np.array(drag_cosine_pulse_waveforms(wf_amp, pi_len, drag_coef, anharmonicity, ac_stark_shift))

            if rotation_key in ["x180", "x90", "minus_x90"]:
                I_wf = wf
                Q_wf = der_wf
            elif rotation_key in ["y180", "y90", "minus_y90"]:
                I_wf = (-1) * der_wf
                Q_wf = wf
            else:
                raise ValueError(f'{rotation_key} is passed. rotation_key must be one of ["x180", "x90", "minus_x90", "y180", "y90", "minus_y90"]')

            waveforms[f"{qb}_{rotation_key}_I"] = I_wf
            waveforms[f"{qb}_{rotation_key}_Q"] = Q_wf

    return waveforms

qubit_rotation_keys = ["x180", "x90", "minus_x90", "y180", "y90", "minus_y90"]
waveforms = generate_waveforms(qubit_rotation_keys)



# MARK: RESONATORS
#############################################
#                Resonators                 #
#############################################

READOUT_LEN = 1000
READOUT_AMP = 1.0
TOF = 300

RL_CONSTANTS = {
    "rl1": {
        "LO": 7.0 * u.GHz,
        "RESONATORS": [
            "q1_rr",
            "q2_rr",
            "q3_rr",
            "q4_rr",
            "q5_rr",
            "q6_rr",
            "q7_rr",
        ],
        "TOF": TOF,
        "con": "con1",
        "fem": mwfem_slot,
        "ao": 8,
        "ai": 2,
        "band": 2,
        "full_scale_power_dbm": -11,
        "delay": 0,
    },
}

RR_QUBIT_MAP = {
    "q1_rr": "q1_xy",
    "q2_rr": "q2_xy",
    "q3_rr": "q3_xy",
    "q4_rr": "q4_xy",
    "q5_rr": "q5_xy",
    "q6_rr": "q6_xy",
    "q7_rr": "q7_xy",
}
QUBIT_RR_MAP = {
    "q1_xy": "q1_rr",
    "q2_xy": "q2_rr",
    "q3_xy": "q3_rr",
    "q4_xy": "q4_rr",
    "q5_xy": "q5_rr",
    "q6_xy": "q6_rr",
    "q7_xy": "q7_rr",
}

RR_CONSTANTS = {
    "q1_rr": {
        # main
        "IF": 100 * u.MHz, 
        "amp": READOUT_AMP,
        "rotation_angle": 0.0,
        "ge_threshold": 0.0,
        # common
        "TOF": RL_CONSTANTS["rl1"]["TOF"],
        "LO": RL_CONSTANTS["rl1"]["LO"],
        "con": RL_CONSTANTS["rl1"]["con"],
        "fem": RL_CONSTANTS["rl1"]["fem"],
        "ao": RL_CONSTANTS["rl1"]["ao"],
        "ai": RL_CONSTANTS["rl1"]["ai"],
        "delay": RL_CONSTANTS["rl1"]["delay"],
        "core": QUBIT_CONSTANTS[f"q1_xy"]["core"],
    },
    "q2_rr": {
        # main
        "IF": 100 * u.MHz, 
        "amp": READOUT_AMP,
        "rotation_angle": 0.0,
        "ge_threshold": 0.0,
        # common
        "TOF": RL_CONSTANTS["rl1"]["TOF"],
        "LO": RL_CONSTANTS["rl1"]["LO"],
        "con": RL_CONSTANTS["rl1"]["con"],
        "fem": RL_CONSTANTS["rl1"]["fem"],
        "ao": RL_CONSTANTS["rl1"]["ao"],
        "ai": RL_CONSTANTS["rl1"]["ai"],
        "delay": RL_CONSTANTS["rl1"]["delay"],
        "core": QUBIT_CONSTANTS[f"q2_xy"]["core"],
    },
    "q3_rr": {
        # main
        "IF": 100 * u.MHz, 
        "amp": READOUT_AMP,
        "rotation_angle": 0.0,
        "ge_threshold": 0.0,
        # common
        "TOF": RL_CONSTANTS["rl1"]["TOF"],
        "LO": RL_CONSTANTS["rl1"]["LO"],
        "con": RL_CONSTANTS["rl1"]["con"],
        "fem": RL_CONSTANTS["rl1"]["fem"],
        "ao": RL_CONSTANTS["rl1"]["ao"],
        "ai": RL_CONSTANTS["rl1"]["ai"],
        "delay": RL_CONSTANTS["rl1"]["delay"],
        "core": QUBIT_CONSTANTS[f"q3_xy"]["core"],
    },
    "q4_rr": {
        # main
        "IF": 100 * u.MHz, 
        "amp": READOUT_AMP,
        "rotation_angle": 0.0,
        "ge_threshold": 0.0,
        # common
        "TOF": RL_CONSTANTS["rl1"]["TOF"],
        "LO": RL_CONSTANTS["rl1"]["LO"],
        "con": RL_CONSTANTS["rl1"]["con"],
        "fem": RL_CONSTANTS["rl1"]["fem"],
        "ao": RL_CONSTANTS["rl1"]["ao"],
        "ai": RL_CONSTANTS["rl1"]["ai"],
        "delay": RL_CONSTANTS["rl1"]["delay"],
        "core": QUBIT_CONSTANTS[f"q4_xy"]["core"],
    },
    "q5_rr": {
        # main
        "IF": 100 * u.MHz, 
        "amp": READOUT_AMP,
        "rotation_angle": 0.0,
        "ge_threshold": 0.0,
        # common
        "TOF": RL_CONSTANTS["rl1"]["TOF"],
        "LO": RL_CONSTANTS["rl1"]["LO"],
        "con": RL_CONSTANTS["rl1"]["con"],
        "fem": RL_CONSTANTS["rl1"]["fem"],
        "ao": RL_CONSTANTS["rl1"]["ao"],
        "ai": RL_CONSTANTS["rl1"]["ai"],
        "delay": RL_CONSTANTS["rl1"]["delay"],
        "core": QUBIT_CONSTANTS[f"q5_xy"]["core"],
    },
    "q6_rr": {
        # main
        "IF": 100 * u.MHz, 
        "amp": READOUT_AMP,
        "rotation_angle": 0.0,
        "ge_threshold": 0.0,
        # common
        "TOF": RL_CONSTANTS["rl1"]["TOF"],
        "LO": RL_CONSTANTS["rl1"]["LO"],
        "con": RL_CONSTANTS["rl1"]["con"],
        "fem": RL_CONSTANTS["rl1"]["fem"],
        "ao": RL_CONSTANTS["rl1"]["ao"],
        "ai": RL_CONSTANTS["rl1"]["ai"],
        "delay": RL_CONSTANTS["rl1"]["delay"],
        "core": QUBIT_CONSTANTS[f"q6_xy"]["core"],
    },
    "q7_rr": {
        # main
        "IF": 100 * u.MHz, 
        "amp": READOUT_AMP,
        "rotation_angle": 0.0,
        "ge_threshold": 0.0,
        # common
        "TOF": RL_CONSTANTS["rl1"]["TOF"],
        "LO": RL_CONSTANTS["rl1"]["LO"],
        "con": RL_CONSTANTS["rl1"]["con"],
        "fem": RL_CONSTANTS["rl1"]["fem"],
        "ao": RL_CONSTANTS["rl1"]["ao"],
        "ai": RL_CONSTANTS["rl1"]["ai"],
        "delay": RL_CONSTANTS["rl1"]["delay"],
        "core": QUBIT_CONSTANTS[f"q7_xy"]["core"],
    },
}

assert set(RR_CONSTANTS.keys()) == set([rr for rl, val in RL_CONSTANTS.items() for rr in val["RESONATORS"]]), "resonators in RL_CONSTANTS and RR_CONTANTS do not match!"


for rl in RL_CONSTANTS.keys():
    total_amp = 0
    for rr in RL_CONSTANTS[rl]["RESONATORS"]:
        total_amp += RR_CONSTANTS[rr]["amp"]
    print(f'Total power on {rl}', RL_CONSTANTS[rl]["full_scale_power_dbm"])


opt_weights = False
if opt_weights:

    current_file_path = os.path.dirname(os.path.abspath(__file__))
    integ_weights = {
        "q1_rr": np.load(os.path.join(current_file_path, "optimal_weights_q1_rr.npz")),
        "q2_rr": np.load(os.path.join(current_file_path, "optimal_weights_q2_rr.npz")),
        "q3_rr": np.load(os.path.join(current_file_path, "optimal_weights_q3_rr.npz")),
        "q4_rr": np.load(os.path.join(current_file_path, "optimal_weights_q4_rr.npz")),
        "q5_rr": np.load(os.path.join(current_file_path, "optimal_weights_q5_rr.npz")),
        "q6_rr": np.load(os.path.join(current_file_path, "optimal_weights_q6_rr.npz")),
        "q7_rr": np.load(os.path.join(current_file_path, "optimal_weights_q7_rr.npz")),
    }

    OPT_WEIGHTS = {
        **{rr: {
            "real": [(x, integ_weights[rr]["division_length"] * 4) for x in integ_weights[rr]["weights_real"]],
            "minus_imag": [(x, integ_weights[rr]["division_length"] * 4) for x in integ_weights[rr]["weights_minus_imag"]],
            "imag": [(x, integ_weights[rr]["division_length"] * 4) for x in integ_weights[rr]["weights_imag"]] ,
            "minus_real": [(x, integ_weights[rr]["division_length"] * 4) for x in integ_weights[rr]["weights_minus_real"]],
        } for rr in RR_CONSTANTS.keys()}
    }

else:
    OPT_WEIGHTS = {
        **{rr: {
            "real": [(1.0, READOUT_LEN)],
            "minus_imag": [(0.0, READOUT_LEN)],
            "imag": [(0.0, READOUT_LEN)],
            "minus_real": [(1.0, READOUT_LEN)],
        } for rr in RR_CONSTANTS.keys()}
    }


QUBITS_ALL = [qb for qb in QUBIT_CONSTANTS.keys()]
RESONATORS_ALL = [key for key in RR_CONSTANTS.keys()]


# MARK: CONFIGURATION
#############################################
#                  Config                   #
#############################################
config = {
    "version": 1,
    "controllers": {
        "con1": {
            "type": "opx1000",
            "fems": {
                mwfem_slot: {
                    # The keyword "band" refers to the following frequency bands:
                    #   1: (50 MHz - 5.5 GHz)
                    #   2: (4.5 GHz - 7.5 GHz)
                    #   3: (6.5 GHz - 10.5 GHz)
                    # The keyword "full_scale_power_dbm" is the maximum power of
                    # normalized pulse waveforms in [-1,1]. To convert to voltage,
                    #   power_mw = 10**(full_scale_power_dbm / 10)
                    #   max_voltage_amp = np.sqrt(2 * power_mw * 50 / 1000)
                    #   amp_in_volts = waveform * max_voltage_amp
                    #   ^ equivalent to OPX+ amp
                    # Its range is -41dBm to +10dBm with 3dBm steps.
                    "type": "MW",
                    "analog_outputs": {
                        **{
                            v["ao"]: {
                                "sampling_rate": 1e9,
                                "full_scale_power_dbm": v["full_scale_power_dbm"],
                                "band": v["band"],
                                "delay": v["delay"],
                                "upconverters": {
                                    1: {"frequency": v["LO"]},
                                },
                            } for k, v in RL_CONSTANTS.items()
                        },
                        **{
                            v["ao"]: {
                                "sampling_rate": 1e9,
                                "full_scale_power_dbm": v["full_scale_power_dbm"],
                                "band": v["band"],
                                "delay": v["delay"],
                                "upconverters": {
                                    1: {"frequency": v["LO"]},
                                },
                            } for k, v in QUBIT_CONSTANTS.items()
                        }
                    },
                    "analog_inputs": {
                        **{
                            v["ai"]: {
                                "sampling_rate": 1e9,
                                "band": v["band"],
                            "gain_db": 0,
                            "downconverter_frequency": v["LO"],
                            } for k, v in RL_CONSTANTS.items()
                        },
                    },
                },
            },
        },
    },
    "elements": {

        # readout line 1
        **{rr: {
            "MWInput": {
                "port": (val["con"], val["fem"], val["ao"]),
                "upconverter": 1,
            },
            "intermediate_frequency": RR_CONSTANTS[rr]["IF"],  # in Hz [-350e6, +350e6]
            "MWOutput": {
                "port": (val["con"], val["fem"], val["ai"]),
            },
			'time_of_flight': val["TOF"],
            'smearing': 120,
            "operations": {
                "const": "const_pulse",
                "readout": f"readout_pulse_{rr}",
            },
            "core": val["core"],
        } for rr, val in RR_CONSTANTS.items()},

        # xy drives
        **{qb: {
            "MWInput": {
                "port": (val["con"], val["fem"], val["ao"]),
                "upconverter": 1,
            },
            "intermediate_frequency": val["IF"],  # in Hz
            "operations": {
                "zero": "zero_pulse",
                "const": "const_pulse",
                "saturation": "saturation_pulse",
                "x180": f"x180_pulse_{qb}",
                "x90": f"x90_pulse_{qb}",
                "-x90": f"-x90_pulse_{qb}",
                "y90": f"y90_pulse_{qb}",
                "y180": f"y180_pulse_{qb}",
                "-y90": f"-y90_pulse_{qb}",
                "rise": f"flattop_gaussian_rise_pulse_{qb}",
                "flattop": f"flattop_gaussian_flattop_pulse_{qb}",
                "fall": f"flattop_gaussian_fall_pulse_{qb}",
            },
            "core": val["core"],
        } for qb, val in QUBIT_CONSTANTS.items()},

        # xy drives
        **{f"{qb}_twin": {
            "MWInput": {
                "port": (val["con"], val["fem"], val["ao"]),
                "upconverter": 1,
            },
            "intermediate_frequency": val["IF"],  # in Hz
            "operations": {
                "zero": "zero_pulse",
                "const": "const_pulse",
                "saturation": "saturation_pulse",
                "x180": f"x180_pulse_{qb}",
                "x90": f"x90_pulse_{qb}",
                "-x90": f"-x90_pulse_{qb}",
                "y90": f"y90_pulse_{qb}",
                "y180": f"y180_pulse_{qb}",
                "-y90": f"-y90_pulse_{qb}",
                "rise": f"flattop_gaussian_rise_pulse_{qb}",
                "flattop": f"flattop_gaussian_flattop_pulse_{qb}",
                "fall": f"flattop_gaussian_fall_pulse_{qb}",
            },
            "core": val["core"] + "_twin",
        } for qb, val in QUBIT_CONSTANTS.items()},
    }, 
    "pulses": {
        "const_pulse": {
            "operation": "control",
            "length": CONST_LEN,
            "waveforms": {
                "I": "const_wf",
                "Q": "zero_wf",
            },
        },
        "zero_pulse": {
            "operation": "control",
            "length": 16,
            "waveforms": {
                "I": "zero_wf",
                "Q": "zero_wf",
            },
        },
        "saturation_pulse": {
            "operation": "control",
            "length": SATURATION_LEN,
            "waveforms": {
                "I": "saturation_wf",
                "Q": "zero_wf",
            },
        },
        **{f"x90_pulse_{qb}":
            {
                "operation": "control",
                "length": PI_LEN,
                "waveforms": {
                    "I": f"x90_I_wf_{qb}",
                    "Q": f"x90_Q_wf_{qb}"
                }
            }
            for qb in QUBIT_CONSTANTS.keys()
        },
        **{f"x180_pulse_{qb}":
            {
                "operation": "control",
                "length": PI_LEN,
                "waveforms": {
                    "I": f"x180_I_wf_{qb}",
                    "Q": f"x180_Q_wf_{qb}"
                }
            }
            for qb in QUBIT_CONSTANTS.keys()
        },
        **{f"-x90_pulse_{qb}":
            {
                "operation": "control",
                "length": PI_LEN,
                "waveforms": {
                    "I": f"minus_x90_I_wf_{qb}",
                    "Q": f"minus_x90_Q_wf_{qb}"
                }
            }
            for qb in QUBIT_CONSTANTS.keys()
        },
        **{f"y90_pulse_{qb}":
            {
                "operation": "control",
                "length": PI_LEN,
                "waveforms": {
                    "I": f"y90_I_wf_{qb}",
                    "Q": f"y90_Q_wf_{qb}"
                }
            }
            for qb in QUBIT_CONSTANTS.keys()
        },
        **{f"y180_pulse_{qb}":
            {
                "operation": "control",
                "length": PI_LEN,
                "waveforms": {
                    "I": f"y180_I_wf_{qb}",
                    "Q": f"y180_Q_wf_{qb}"
                }
            }
            for qb in QUBIT_CONSTANTS.keys()
        },
        **{f"-y90_pulse_{qb}":
            {
                "operation": "control",
                "length": PI_LEN,
                "waveforms": {
                    "I": f"minus_y90_I_wf_{qb}",
                    "Q": f"minus_y90_Q_wf_{qb}"
                }
            }
            for qb in QUBIT_CONSTANTS.keys()
        },
        **{
            f"readout_pulse_{rr}": {
                "operation": "measurement",
                "length": READOUT_LEN,
                "waveforms": {
                    "I": f"readout_wf_{rr}",
                    "Q": "zero_wf"
                },
                "integration_weights": {
                    "cos": "cosine_weights",
                    "sin": "sine_weights",
                    "minus_sin": "minus_sine_weights",
                    "rotated_cos": f"rotated_cosine_weights_{rr}",
                    "rotated_sin": f"rotated_sine_weights_{rr}",
                    "rotated_minus_sin": f"rotated_minus_sine_weights_{rr}",
                    "opt_cos": f"opt_cosine_weights_{rr}",
                    "opt_sin": f"opt_sine_weights_{rr}",
                    "opt_minus_sin": f"opt_minus_sine_weights_{rr}",
                },
                "digital_marker": "ON",
            } for rr in RR_CONSTANTS.keys()
        },
        **{f"flattop_gaussian_flattop_pulse_{qb}":
            {
                "operation": "control",
                "length": 100,
                "waveforms": {
                    "I": f"flattop_gaussian_flattop_wf_{qb}",
                    "Q": f"zero_wf"
                }
            }
             for qb in QUBIT_CONSTANTS.keys()
        },
        **{f"flattop_gaussian_rise_pulse_{qb}":
            {
                "operation": "control",
                "length": 16,
                "waveforms": {
                    "I": f"flattop_gaussian_rise_wf_{qb}",
                    "Q": f"zero_wf"
                }
            }
             for qb in QUBIT_CONSTANTS.keys()
        },
        **{f"flattop_gaussian_fall_pulse_{qb}":
            {
                "operation": "control",
                "length": 16,
                "waveforms": {
                    "I": f"flattop_gaussian_fall_wf_{qb}",
                    "Q": f"zero_wf"
                }
            }
             for qb in QUBIT_CONSTANTS.keys()
        },
    },
    "waveforms": {
        "const_wf": {"type": "constant", "sample": CONST_AMP},
        "saturation_wf": {"type": "constant", "sample": SATURATION_AMP},
        "zero_wf": {"type": "constant", "sample": 0.0},
        **{f"x90_I_wf_{key}": {"type": "arbitrary", "samples": waveforms[key+"_x90_I"].tolist()} for key in QUBIT_CONSTANTS.keys()},
        **{f"x90_Q_wf_{key}": {"type": "arbitrary", "samples": waveforms[key+"_x90_Q"].tolist()} for key in QUBIT_CONSTANTS.keys()},
        **{f"x180_I_wf_{key}": {"type": "arbitrary", "samples": waveforms[key+"_x180_I"].tolist()} for key in QUBIT_CONSTANTS.keys()},
        **{f"x180_Q_wf_{key}": {"type": "arbitrary", "samples": waveforms[key+"_x180_Q"].tolist()} for key in QUBIT_CONSTANTS.keys()},
        **{f"minus_x90_I_wf_{key}": {"type": "arbitrary", "samples": waveforms[key+"_minus_x90_I"].tolist()} for key in QUBIT_CONSTANTS.keys()},
        **{f"minus_x90_Q_wf_{key}": {"type": "arbitrary", "samples": waveforms[key+"_minus_x90_Q"].tolist()} for key in QUBIT_CONSTANTS.keys()},
        **{f"y90_I_wf_{key}": {"type": "arbitrary", "samples": waveforms[key+"_y90_I"].tolist()} for key in QUBIT_CONSTANTS.keys()},
        **{f"y90_Q_wf_{key}": {"type": "arbitrary", "samples": waveforms[key+"_y90_Q"].tolist()} for key in QUBIT_CONSTANTS.keys()},
        **{f"y180_I_wf_{key}": {"type": "arbitrary", "samples": waveforms[key+"_y180_I"].tolist()} for key in QUBIT_CONSTANTS.keys()},
        **{f"y180_Q_wf_{key}": {"type": "arbitrary", "samples": waveforms[key+"_y180_Q"].tolist()} for key in QUBIT_CONSTANTS.keys()},
        **{f"minus_y90_I_wf_{key}": {"type": "arbitrary", "samples": waveforms[key+"_minus_y90_I"].tolist()} for key in QUBIT_CONSTANTS.keys()},
        **{f"minus_y90_Q_wf_{key}": {"type": "arbitrary", "samples": waveforms[key+"_minus_y90_Q"].tolist()} for key in QUBIT_CONSTANTS.keys()},
        **{f"readout_wf_{key}": {"type": "constant", "sample": val["amp"]} for key, val in RR_CONSTANTS.items()},
        **{f"flattop_gaussian_rise_wf_{key}": {"type": "arbitrary", "samples": [0] * 4 + flattop_gaussian_waveform(0.1, 68, 12, return_part="rise")} for key, val in QUBIT_CONSTANTS.items()},
        **{f"flattop_gaussian_fall_wf_{key}": {"type": "arbitrary", "samples": flattop_gaussian_waveform(0.1, 68, 12, return_part="fall") + [0] * 4} for key, val in QUBIT_CONSTANTS.items()},
        **{f"flattop_gaussian_flattop_wf_{key}": {"type": "constant", "sample": 0.1} for key, val in QUBIT_CONSTANTS.items()},
    },
    "digital_waveforms": {
        "ON": {"samples": [(1, 0)]},
    },
    "integration_weights": {
        "cosine_weights": {
            "cosine": [(1.0, READOUT_LEN)],
            "sine": [(0.0, READOUT_LEN)],
        },
        "sine_weights": {
            "cosine": [(0.0, READOUT_LEN)],
            "sine": [(1.0, READOUT_LEN)],
        },
        "minus_sine_weights": {
            "cosine": [(0.0, READOUT_LEN)],
            "sine": [(-1.0, READOUT_LEN)],
        },
        **{
            f"rotated_cosine_weights_{rr}": {
                "cosine": [(np.cos(val["rotation_angle"])), READOUT_LEN],
                "sine": [(np.sin(val["rotation_angle"])), READOUT_LEN]
            } for rr, val in RR_CONSTANTS.items()
        },
        **{
            f"rotated_sine_weights_{rr}": {
                "cosine": [(-np.sin(val["rotation_angle"])), READOUT_LEN],
                "sine": [(np.cos(val["rotation_angle"])), READOUT_LEN]
            } for rr, val in RR_CONSTANTS.items()
        },
        **{
            f"rotated_minus_sine_weights_{rr}": {
                "cosine": [(np.sin(val["rotation_angle"])), READOUT_LEN],
                "sine": [(-np.cos(val["rotation_angle"])), READOUT_LEN]
            } for rr, val in RR_CONSTANTS.items()
        },
        **{
            f"opt_cosine_weights_{rr}": {
                "cosine": OPT_WEIGHTS[rr]["real"],
                "sine": OPT_WEIGHTS[rr]["minus_imag"]
            } for rr in RR_CONSTANTS.keys()
        },
        **{
            f"opt_sine_weights_{rr}": {
                "cosine": OPT_WEIGHTS[rr]["imag"],
                "sine": OPT_WEIGHTS[rr]["real"]
            } for rr in RR_CONSTANTS.keys()
        },
        **{
            f"opt_minus_sine_weights_{rr}": {
                "cosine": OPT_WEIGHTS[rr]["minus_imag"],
                "sine": OPT_WEIGHTS[rr]["minus_real"]
            } for rr in RR_CONSTANTS.keys()
        },
    },
}

# %%