# %%

import copy
import os
from pathlib import Path
import black
import numpy as np
from qualang_tools.units import unit
from qualang_tools.config.waveform_tools import drag_gaussian_pulse_waveforms


#######################
# AUXILIARY FUNCTIONS #
#######################
u = unit(coerce_to_integer=True)


######################
# Network parameters #
######################
host_ip = "172.16.33.107"  # "172.16.33.101"
cluster_name = "Beta_8"  # "Cluster
qop_port = 9510  # Write the QOP port if version < QOP220
octave_config = None


#############
# Save Path #
#############

# Path to save data
save_dir = Path(r"/workspaces/end-to-end-programs/transmon-qubits/triple-chassis-AIST/data")
save_dir.mkdir(exist_ok=True)
config_path = Path(__file__)
default_additional_files = {str(config_path): config_path.name}


#####################
# OPX configuration #
#####################


# MARK: QUBITS
#############################################
#                  Qubits                   #
#############################################

QUBIT_PORT_MAP = {
    1:  {"con": "con1", "fem": 1, "ao": 2, "thread": "q1"},
    2:  {"con": "con1", "fem": 1, "ao": 3, "thread": "q2"},
    3:  {"con": "con1", "fem": 1, "ao": 4, "thread": "q3"},
    4:  {"con": "con1", "fem": 1, "ao": 5, "thread": "q4"},
    5:  {"con": "con1", "fem": 1, "ao": 6, "thread": "q5"},
    6:  {"con": "con1", "fem": 1, "ao": 7, "thread": "q6"},

    7:  {"con": "con1", "fem": 2, "ao": 2, "thread": "q7"},
    8:  {"con": "con1", "fem": 2, "ao": 3, "thread": "q8"},
    9:  {"con": "con1", "fem": 2, "ao": 4, "thread": "q9"},
    10:  {"con": "con1", "fem": 2, "ao": 5, "thread": "q10"},
}

qubits_idx = [i + 1 for i in range(len(QUBIT_PORT_MAP))]

# CW pulse parameter
CONST_LEN = 1000
CONST_AMP = 0.25 # 125 * u.mV

# Saturation_pulse
SATURATION_LEN = 100 * u.us
SATURATION_AMP = 0.4

# Constants for Pi Pulse
PI_AMP = 0.25
PI_LEN = 40 # less than 40 can cause issue with strict timing
PI_SIGMA = PI_LEN / 5

# Constants for each qubit
QUBIT_CONSTANTS_COMMON = {
    "amp": PI_AMP,
    "pi_len": PI_LEN,
    "pi_sigma": PI_SIGMA, 
    "anharmonicity": -200 * u.MHz,
    "drag_coefficient": 0.0, #0.9405, # 0.5394,
    "ac_stark_shift": 0.0 * u.MHz, # 5.0 * u.MHz
    "LO": 1.95* u.GHz,
    "IF": 50 * u.MHz,
    "con": "con""con1",
    "fem": 1,
    "ao": 1,
    "band": 3,
    "full_scale_power_dbm": +1,
    "delay": 0,
    "thread": "",
}

QUBIT_CONSTANTS = {
    f"q{qb}_xy": copy.deepcopy(QUBIT_CONSTANTS_COMMON)
    for qb in qubits_idx
}

for qb in qubits_idx:
    QUBIT_CONSTANTS[f"q{qb}_xy"].update(**QUBIT_PORT_MAP[qb])


# for qb in QUBIT_CONSTANTS.keys():
#     assert QUBIT_CONSTANTS[qb]["amp"] <= 0.499, f"{qb} amplitude needs to be less than 0.499"


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

            wf, der_wf = np.array(drag_gaussian_pulse_waveforms(wf_amp, pi_len, pi_sigma, drag_coef, anharmonicity, ac_stark_shift))
            # wf, der_wf = np.array(drag_cosine_pulse_waveforms(wf_amp, pi_len, drag_coef, anharmonicity, ac_stark_shift))

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



# MARK: CROSS RESONANCE
#############################################
#              CROSS RESONANCE              #
#############################################

qubit_pairs = [
    (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10),
]
qubit_pairs = qubit_pairs + [(qp[1], qp[0]) for qp in qubit_pairs]

# Constants for Pi Pulse
CR_SQUARE_AMP = 0.9
CR_SQUARE_LEN = 120
CR_SQUARE_PHASE = 0.0


# Constants for each qubit for CR DRIVE
CR_CONSTANTS = {
    **{f"cr_c{c}t{t}": {
        # main element
        "square_amp": CR_SQUARE_AMP,
        "square_len": CR_SQUARE_LEN,
        "square_phase": CR_SQUARE_PHASE, # in units of 2pi
        # common
        "LO": QUBIT_CONSTANTS[f"q{t}_xy"]["LO"],
        "IF": QUBIT_CONSTANTS[f"q{t}_xy"]["IF"],
        "con": QUBIT_CONSTANTS[f"q{c}_xy"]["con"],
        "fem": QUBIT_CONSTANTS[f"q{c}_xy"]["fem"],
        "ao": QUBIT_CONSTANTS[f"q{c}_xy"]["ao"],
        "band": QUBIT_CONSTANTS[f"q{t}_xy"]["band"],
        "full_scale_power_dbm": QUBIT_CONSTANTS[f"q{c}_xy"]["full_scale_power_dbm"],
        "delay": QUBIT_CONSTANTS[f"q{c}_xy"]["delay"],
        "thread": QUBIT_CONSTANTS[f"q{c}_xy"]["thread"],
    } for c, t in qubit_pairs}
}
# # update after findng the optimal parameters
# CR_CONSTANTS["cr_c1t2"].update({"square_amp": CR_SQUARE_AMP, "square_len": CR_SQUARE_LEN})
# CR_CONSTANTS["cr_c2t1"].update({"square_amp": CR_SQUARE_AMP, "square_len": CR_SQUARE_LEN})
# CR_CONSTANTS["cr_c2t3"].update({"square_amp": CR_SQUARE_AMP, "square_len": CR_SQUARE_LEN})
# CR_CONSTANTS["cr_c3t2"].update({"square_amp": CR_SQUARE_AMP, "square_len": CR_SQUARE_LEN})
# CR_CONSTANTS["cr_c3t4"].update({"square_amp": CR_SQUARE_AMP, "square_len": CR_SQUARE_LEN})
# CR_CONSTANTS["cr_c4t3"].update({"square_amp": 0.9, "square_len": 420})



# MARK: RESONATORS
#############################################
#                Resonators                 #
#############################################

RL_PORT_MAP = {
    1:  {"con": "con1", "fem": 1, "ao": 1, "ai": 1},
    2:  {"con": "con1", "fem": 1, "ao": 8, "ai": 2},
    3:  {"con": "con1", "fem": 2, "ao": 1, "ai": 1},
    4:  {"con": "con1", "fem": 2, "ao": 8, "ai": 2}, 
}

RR_RL_MAP = {
    1:  {"rl":  1, "thread": "q1"},
    2:  {"rl":  1, "thread": "q2"},
    3:  {"rl":  1, "thread": "q3"},
    4:  {"rl":  2, "thread": "q4"},
    5:  {"rl":  2, "thread": "q5"},
    6:  {"rl":  2, "thread": "q6"},

    7:  {"rl":  3, "thread": "q7"},
    8:  {"rl":  3, "thread": "q8"},
    9:  {"rl":  4, "thread": "q9"},
    10: {"rl":  4, "thread": "q10"},
}

RL_CONSTANTS_COMMON = {
    "LO": 1.95* u.GHz,
    "RESONATORS": [],
    "con": "con1",
    "fem": 1,
    "ao": 1,
    "ai": 1,
    "band": 3,
    "full_scale_power_dbm": +1,
    "delay": 0,
}

RL_CONSTANTS = {}
for rl, val in RL_PORT_MAP.items():
    rl_key = f"rl{rl}"
    RL_CONSTANTS[rl_key] = copy.deepcopy(RL_CONSTANTS_COMMON)
    RL_CONSTANTS[rl_key].update(**RL_PORT_MAP[rl])

for rr, val in RR_RL_MAP.items():
    rl = val["rl"]
    rl_key = f"rl{rl}"
    # RL_CONSTANTS.setdefault(rl_key, []).append(f"q{rr}_rr")
    RL_CONSTANTS[rl_key]["RESONATORS"].append(f"q{rr}_rr")


READOUT_LEN = 1000
READOUT_AMP = 0.25

# Constants for each qubit
RR_CONSTANTS_COMMON = {
    "amp": READOUT_AMP,
    "len": READOUT_LEN,
    "LO": 1.95* u.GHz,
    "IF": +50 * u.MHz,
    "TOF": 300,
    "rotation_angle": (0.0 / 180) * np.pi,
    "ge_threshold": 0.0,
    "thread": "",
}

RR_CONSTANTS = {}
for rr, val in RR_RL_MAP.items():
    rr_key = f"q{rr}_rr"
    # RR_CONSTANTS.setdefault(rl_key, []).append(f"q{rr}_rr")
    RR_CONSTANTS[rr_key] = copy.deepcopy(RR_CONSTANTS_COMMON)
    RR_CONSTANTS[rr_key].update(**RR_RL_MAP[rr])
    RR_CONSTANTS[rr_key].update(**RL_PORT_MAP[val["rl"]])


for rl in RL_CONSTANTS.keys():
    total_amp = 0
    for rr in RL_CONSTANTS[rl]["RESONATORS"]:
        total_amp += RR_CONSTANTS[rr]["amp"]
    assert total_amp <= 0.999, f"the sum of {rl} resonators is larger than 0.499"
    print(f'Total power on {rl}', total_amp)


opt_weights = False
if opt_weights:
    current_file_path = os.path.dirname(os.path.abspath(__file__))
    OPT_WEIGHTS = {}
    for rr in RR_CONSTANTS.keys():
        weights = np.load(os.path.join(current_file_path, f"optimal_weights_{rr}.npz"))
        OPT_WEIGHTS[rr] = {
            "real": [(x, weights["division_length"] * 4) for x in weights["weights_real"]],
            "minus_imag": [(x, weights["division_length"] * 4) for x in weights["weights_minus_imag"]],
            "imag": [(x, weights["division_length"] * 4) for x in weights["weights_imag"]] ,
            "minus_real": [(x, weights["division_length"] * 4) for x in weights["weights_minus_real"]] 
        }

else:
    OPT_WEIGHTS = {}
    for rr in RR_CONSTANTS.keys():
        OPT_WEIGHTS[rr] = {
            "real": [(1.0, READOUT_LEN)],
            "minus_imag": [(0.0, READOUT_LEN)],
            "imag": [(0.0, READOUT_LEN)],
            "minus_real": [(1.0, READOUT_LEN)]
        }


# MARK: JPA PUMP
#########################################
#                JPA PUMP               #
#########################################

JPA_PORT_MAP = {
    1:  {"con": "con1", "fem": 2, "ao": 6, "thread": "j1"},
    2:  {"con": "con1", "fem": 2, "ao": 7, "thread": "j2"},
}

JPA_RL_MAP = {
    1:  {"rl": 1},
    2:  {"rl": 2},
}

jpas_idx = [i + 1 for i in range(len(JPA_PORT_MAP))]

# CW pulse parameter
JPA_LEN = 1000
JPA_POWER = 1
JPA_AMP = 1.0

# Constants for each qubit
JPA_CONSTANTS_COMMON = {
    "LO": 1.95* u.GHz,
    "IF": 50 * u.MHz,
    "con": "con1",
    "fem": 1,
    "ao": 1,
    "band": 3,
    "full_scale_power_dbm": JPA_POWER,
    "delay": 0,
    "thread": "",
    "pump_amp": JPA_AMP,
    "pump_len": JPA_LEN,
}

JPA_CONSTANTS = {
    f"jpa{j}": copy.deepcopy(JPA_CONSTANTS_COMMON)
    for j in jpas_idx
}

for j in jpas_idx:
    JPA_CONSTANTS[f"jpa{j}"].update(**JPA_PORT_MAP[j])


# MARK: CONFIGURATION
#############################################
#                  Config                   #
#############################################

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

config_controllers = dict()

con_fems = {(v["con"], v["fem"]) for v in QUBIT_PORT_MAP.values()}
for con, fem in con_fems:
    if con not in config_controllers:
        config_controllers[con] = {
            "type": "opx1000",
            "fems": {}
        }
    config_controllers[con]["fems"][fem] = {
        "type": "MW",
        "analog_outputs": {},
        "digital_outputs": {},
        "analog_inputs": {},
    }  # Initialize fems as an empty dict

for q, val in QUBIT_CONSTANTS.items():
    con, fem, ao = val["con"], val["fem"], val["ao"]
    config_controllers[con]["fems"][fem]["analog_outputs"][ao] = {
        "sampling_rate": 1e9,
        "full_scale_power_dbm": val["full_scale_power_dbm"],
        "band": val["band"],
        "delay": val["delay"],
        "upconverters": {
            "1": {"frequency": val["LO"]},
            "2": {"frequency": val["LO"] - 500 * u.MHz},
        },
    }

for rl, val in RL_CONSTANTS.items():
    con, fem, ao, ai = val["con"], val["fem"], val["ao"], val["ai"]
    config_controllers[con]["fems"][fem]["analog_outputs"][ao] = {
        "sampling_rate": 1e9,
        "full_scale_power_dbm": val["full_scale_power_dbm"],
        "band": val["band"],
        "delay": val["delay"],
        "upconverters": {
            "1": {"frequency": val["LO"]},
        },
    }
    config_controllers[con]["fems"][fem]["analog_inputs"][ai] = {
        "sampling_rate": 1e9,
        "band": val["band"],
        "gain_db": 1,
        "downconverter_frequency": val["LO"],
    }

for jpa, val in JPA_CONSTANTS.items():
    con, fem, ao = val["con"], val["fem"], val["ao"]
    config_controllers[con]["fems"][fem]["analog_outputs"][ao] = {
        "sampling_rate": 1e9,
        "full_scale_power_dbm": val["full_scale_power_dbm"],
        "band": val["band"],
        "delay": val["delay"],
        "upconverters": {
            "1": {"frequency": val["LO"]},
        },
    }

QUBIT_RR_MAP = {q: q.replace("xy", "rr") for q in QUBIT_CONSTANTS}
RR_QUBIT_MAP = {v: k for k, v in QUBIT_RR_MAP.items()}


# # Define file path
# file_path = f"{Path(__file__).stem}_controllers.py"

# # Write the OrderedDict to the file as a string
# with open(file_path, 'w') as file:
#     file.write(f"config_controller = {config_controllers}\n") 
# # Format the file using black
# black.format_file_in_place(Path(file_path), fast=False, mode=black.FileMode())


config = {
    "version": 1,
    "controllers": config_controllers,
    "elements": {
        # readout line
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
            'smearing': 0,
            "operations": {
                "const": "const_pulse",
                "readout": f"readout_pulse_{rr}",
            },
            "thread": val["thread"],
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
                "const_small": "const_small_pulse",
                "saturation": "saturation_pulse",
                "x180": f"x180_pulse_{qb}",
                "x90": f"x90_pulse_{qb}",
                "-x90": f"-x90_pulse_{qb}",
                "y90": f"y90_pulse_{qb}",
                "y180": f"y180_pulse_{qb}",
                "-y90": f"-y90_pulse_{qb}",
            },
            "thread": val["thread"],
        } for qb, val in QUBIT_CONSTANTS.items()},

        # cr drives
        **{cr: {
            "MWInput": {
                "port": (val["con"], val["fem"], val["ao"]),
                "upconverter": 2,
            },
            "intermediate_frequency": val["IF"],  # in Hz
            "operations": {
                "const": "const_pulse",
                "square_positive": f"square_positive_pulse_{cr}",
                "square_negative": f"square_negative_pulse_{cr}",
            },
            # "thread": val["thread_main"],
        } for cr, val in CR_CONSTANTS.items()},

        # jpa
        **{jpa: {
            "MWInput": {
                "port": (val["con"], val["fem"], val["ao"]),
                "upconverter": 1,
            },
            "intermediate_frequency": val["IF"],  # in Hz [-350e6, +350e6]
            "operations": {
                "const": "const_pulse",
                "pump": f"jpa_pump_pulse_{jpa}",
            },
            "thread": val["thread"],
        } for jpa, val in JPA_CONSTANTS.items()},

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
        "const_small_pulse": {
            "operation": "control",
            "length": CONST_LEN,
            "waveforms": {
                "I": "const_small_wf",
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
        **{f"square_positive_pulse_{cr}":
            {
                "operation": "control",
                "length": val["square_len"],
                "waveforms": {
                    "I": f"square_positive_wf_{cr}",
                    "Q": f"zero_wf"
                }
            }
            for cr, val in CR_CONSTANTS.items()
        },
        **{f"square_negative_pulse_{cr}":
            {
                "operation": "control",
                "length": val["square_len"],
                "waveforms": {
                    "I": f"square_negative_wf_{cr}",
                    "Q": f"zero_wf"
                }
            }
            for cr, val in CR_CONSTANTS.items()
        },
        **{f"jpa_pump_pulse_{jpa}":
            {
                "operation": "control",
                "length": val["pump_len"],
                "waveforms": {
                    "I": f"jpa_pump_wf_{jpa}",
                    "Q": f"zero_wf"
                }
            }
            for jpa, val in JPA_CONSTANTS.items()
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
    },
    "waveforms": {
        "const_wf": {"type": "constant", "sample": CONST_AMP},
        "const_small_wf": {"type": "constant", "sample": 0.5 * CONST_AMP},
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
        **{f"square_positive_wf_{key}": {"type": "constant", "sample": val["square_amp"]} for key, val in CR_CONSTANTS.items()},
        **{f"square_negative_wf_{key}": {"type": "constant", "sample": -val["square_amp"]} for key, val in CR_CONSTANTS.items()},
        **{f"readout_wf_{key}": {"type": "constant", "sample": val["amp"]} for key, val in RR_CONSTANTS.items()},
        **{f"jpa_pump_wf_{key}": {"type": "constant", "sample": val["pump_amp"]} for key, val in JPA_CONSTANTS.items()},
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