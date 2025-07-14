# %%

from pathlib import Path
import numpy as np
from qualang_tools.units import unit
from itertools import product
from qualang_tools.config.waveform_tools import drag_gaussian_pulse_waveforms


#######################
# AUXILIARY FUNCTIONS #
#######################
u = unit(coerce_to_integer=True)


######################
# Network parameters #
######################
host_ip = "172.16.33.107"  # "172.16.33.101"
cluster_name = "Cluster_1"  # "Cluster
qop_port = 9510
# host_ip = "192.168.116.106"  # "172.16.33.101"
# cluster_name = "Cluster_4"  # "Cluster
# qop_port = None # Write the QOP port if version < QOP220
octave_config = None


#############
# Save Path #
#############

# Path to save data
save_dir = Path(r"/workspaces/end-to-end-programs/transmon-qubits/triple-chassis-AIST/data")
save_dir.mkdir(exist_ok=True)
config_path = Path(__file__)
default_additional_files = {str(config_path): config_path.name}


##############
# Parameters #
##############

# MW_CON_FEMS = {
#     "con1": [1, 2, 3, 4, 5, 6, 7],
#     "con2": [1, 2, 3, 4, 5, 6, 7],
#     "con3": [1, 2, 3]
# }

MW_CON_FEMS = {
    "con1": [1, 2],
}
MW_OUTPUT_PORTS = [1, 2, 3, 4, 5, 6, 7, 8]
MW_INPUT_PORTS = [1, 2]
MW_CON_FEM_PORTS = [(k, v, port) for k, values in MW_CON_FEMS.items() for v, port in product(values, MW_OUTPUT_PORTS)]


# keep in mind that the scope's bandwidth is up to 4.2 GHz
IF = 50 * u.MHz
LO1 = 4.0 * u.GHz - IF
LO2 = 1.0 * u.GHz - IF
BAND = 1


FULL_SCALE_POWER_DBM = 1
CONST_AMP = 0.25
CONST_LEN = 40
READOUT_AMP = 0.5
READOUT_LEN = 200
TOF = 300

PI_AMP = 0.25
PI_LEN = 40

#####################
#       Utils       #
#####################

def generate_waveforms(rotation_keys):
    """ Generate all necessary waveforms for a set of rotation types across all qubits. """
    
    if not isinstance(rotation_keys, list):
        raise ValueError("rotation_keys must be a list")

    waveforms = {}

    for rotation_key in rotation_keys:
        if rotation_key in ["x180", "y180"]:
            wf_amp = PI_AMP
        elif rotation_key in ["x90", "y90"]:
            wf_amp = PI_AMP / 2
        elif rotation_key in ["minus_x90", "minus_y90"]:
            wf_amp = -PI_AMP / 2
        else:
            continue

        wf, der_wf = np.array(drag_gaussian_pulse_waveforms(wf_amp, PI_LEN, PI_LEN / 5, 0, -200 * u.MHz, 0))
        # wf, der_wf = np.array(drag_cosine_pulse_waveforms(wf_amp, pi_len, drag_coef, anharmonicity, ac_stark_shift))

        if rotation_key in ["x180", "x90", "minus_x90"]:
            I_wf = wf
            Q_wf = der_wf
        elif rotation_key in ["y180", "y90", "minus_y90"]:
            I_wf = (-1) * der_wf
            Q_wf = wf
        else:
            raise ValueError(f'{rotation_key} is passed. rotation_key must be one of ["x180", "x90", "minus_x90", "y180", "y90", "minus_y90"]')

        waveforms[f"gauss_{rotation_key}_I"] = I_wf
        waveforms[f"gauss_{rotation_key}_Q"] = Q_wf

    return waveforms

qubit_rotation_keys = ["x180", "x90", "minus_x90", "y180", "y90", "minus_y90"]
waveforms = generate_waveforms(qubit_rotation_keys)


def print_elements_ports(elements):
    
    if type(elements) == list and len(elements) >= 1:
        for i, elem in enumerate(elements):
            print(f"{i + 1}, {elem}")


def get_all_elements(element_kind, duc=1):

    if element_kind not in ["qubit", "resonator", "jpa"]:
        raise ValueError("element_kind must be one of 'qubit', 'resonator', 'jpa'")

    return [
        f"{element_kind}_{con}-fem{fem}-port{p}-duc{duc}"
        for con, fem, p in MW_CON_FEM_PORTS
    ]


def get_elements(element_kind, cons=None, fems=None, ports=None, duc=1):

    if element_kind not in ["qubit", "resonator", "jpa"]:
        raise ValueError("element_kind must be one of 'qubit', 'resonator', 'jpa'")

    if type(cons) != list:
        cons = [cons]

    if type(fems) != list:
        fems = [fems]

    if type(ports) != list:
        ports = [ports]

    cons = set(cons) if cons else None
    fems = set(fems) if fems else None
    ports = set(ports) if ports else None

    elems = [
        f"{element_kind}_{con}-fem{fem}-port{port}-duc{duc}" for con, fem, port in MW_CON_FEM_PORTS
        if (cons is None or con in cons) and
           (fems is None or fem in fems) and
           (ports is None or port in ports)
    ]
    
    if len(elems) == 0:
        return []
    elif len(elems) == 1:
        return elems[0]
    else:
        return elems


def update_readout_length(new_readout_length, resonators):
    for rr in resonators:
        config["pulses"]["readout_pulse"]["length"] = new_readout_length
        config["integration_weights"]["cosine_weights"] = {
            "cosine": [(1.0, new_readout_length)],
            "sine": [(0.0, new_readout_length)],
        }
        config["integration_weights"]["sine_weights"] = {
            "cosine": [(0.0, new_readout_length)],
            "sine": [(1.0, new_readout_length)],
        }
        config["integration_weights"]["minus_sine_weights"] = {
            "cosine": [(0.0, new_readout_length)],
            "sine": [(-1.0, new_readout_length)],
        }


######################
#       Config       #
######################

config = {
    "version": 1,
    "controllers": {
        con: {
            "type": "opx1000",
            "fems": {
                mw_fem: {
                    "type": "MW",
                    "analog_inputs": {
                        p: {
                            "sampling_rate": 1e9,
                            "band": BAND,
                            "gain_db": 1,
                            "downconverter_frequency": LO1,
                        }
                        for p in MW_INPUT_PORTS
                    },
                    "analog_outputs": {
                        p: {
                            "sampling_rate": 1e9,
                            "band": BAND,
                            "full_scale_power_dbm": FULL_SCALE_POWER_DBM,
                            "upconverters": {
                                1: {"frequency": LO1},
                                2: {"frequency": LO2},
                            }
                        }
                        for p in MW_OUTPUT_PORTS
                    },
                } for mw_fem in MW_CON_FEMS[con]
            },
        } for con in MW_CON_FEMS.keys()
    },
    # 260, 315, 370, 425, 480, 535, 590, 645
    "elements": {
        **{
            f"qubit_{con}-fem{fem}-port{p}-duc1": {
                "MWInput": {
                    "port": (con, fem, p),
                    "upconverter": 1,
                },
                "intermediate_frequency": 50 * u.MHz,
                "operations": {
                    "const": "const_pulse",
                    "x180": "gauss_x180_pulse",
                    "x90": "gauss_x90_pulse",
                    "-x90": "gauss_minus_x90_pulse",
                    "y90": "gauss_y90_pulse",
                    "y180": "gauss_y180_pulse",
                    "-y90": "gauss_minus_y90_pulse",
                },
                "thread": f"{con}-fem{fem}-port{p}-duc1",
            }
            for p in MW_OUTPUT_PORTS for con in MW_CON_FEMS.keys() for fem in MW_CON_FEMS[con]
        },
        **{
            f"qubit_{con}-fem{fem}-port{p}-duc2": {
                "MWInput": {
                    "port": (con, fem, p),
                    "upconverter": 2,
                },
                "intermediate_frequency": 50 * u.MHz,
                "operations": {
                    "const": "const_pulse",
                    "x180": "gauss_x180_pulse",
                    "x90": "gauss_x90_pulse",
                    "-x90": "gauss_minus_x90_pulse",
                    "y90": "gauss_y90_pulse",
                    "y180": "gauss_y180_pulse",
                    "-y90": "gauss_minus_y90_pulse",
                },
                "thread": f"{con}-fem{fem}-port{p}-duc2",
            }
            for p in MW_OUTPUT_PORTS for con in MW_CON_FEMS.keys() for fem in MW_CON_FEMS[con]
        },
        **{
            f"resonator_{con}-fem{fem}-port{p}-duc1": {
                "MWInput": {
                    "port": (con, fem, p),
                    "upconverter": 1,
                },
                "intermediate_frequency": 50 * u.MHz,
                "MWOutput": {
                    "port": (con, fem, (p - 1) // 4 + 1),
                },
                'time_of_flight': TOF,
                'smearing': 0,
                "operations": {
                    "const": "const_pulse",
                    "readout": "readout_pulse",
                },
                "thread": f"{con}-fem{fem}-port{p}-duc1",
            }
            for p in MW_OUTPUT_PORTS for con in MW_CON_FEMS.keys() for fem in MW_CON_FEMS[con]
        },
        **{
            f"jpa_{con}-fem{fem}-port{p}": {
                "MWInput": {
                    "port": (con, fem, p),
                    "upconverter": 1,
                },
                "intermediate_frequency": 50 * u.MHz,
                "operations": {
                    "const": "const_pulse",
                },
            }
            for p in MW_OUTPUT_PORTS for con in MW_CON_FEMS.keys() for fem in MW_CON_FEMS[con]
        }
    },
    "pulses": {
        "const_pulse": {
            "length": CONST_LEN,
            "operation": "control",
            "waveforms": {
                "I": "const_wf",
                "Q": "zero_wf",
            },
        },
        **{
            f"gauss_{rk}_pulse": {
                "operation": "control",
                "length": PI_LEN,
                "waveforms": {
                    "I": f"gauss_{rk}_I_wf",
                    "Q": f"gauss_{rk}_Q_wf",
                },
            }
            for rk in ["x180", "y180"]
        },
        **{
            f"gauss_{rk}_pulse": {
                "operation": "control",
                "length": PI_LEN,
                "waveforms": {
                    "I": f"gauss_{rk}_I_wf",
                    "Q": f"gauss_{rk}_Q_wf",
                },
            }
            for rk in ["x90", "minus_x90", "y90", "minus_y90"]  # Loop over
        },
        "readout_pulse": {
            "operation": "measurement",
            "length": READOUT_LEN,
            "waveforms": {
                "I": "readout_wf",
                "Q": "zero_wf"
            },
            "integration_weights": {
                "cos": "cosine_weights",
                "sin": "sine_weights",
                "minus_sin": "minus_sine_weights",
                "rotated_cos": f"rotated_cosine_weights",
                "rotated_sin": f"rotated_sine_weights",
                "rotated_minus_sin": f"rotated_minus_sine_weights",
            },
            "digital_marker": "ON",
        },
    },
    "waveforms": {
        "const_wf": {"type": "constant", "sample": CONST_AMP},
        "zero_wf": {"type": "constant", "sample": 0.0},
        "readout_wf": {"type": "constant", "sample": READOUT_AMP},
        "gauss_x90_I_wf": {"type": "arbitrary", "samples": waveforms["gauss_x90_I"].tolist()},
        "gauss_x90_Q_wf": {"type": "arbitrary", "samples": waveforms["gauss_x90_Q"].tolist()},
        "gauss_x180_I_wf": {"type": "arbitrary", "samples": waveforms["gauss_x180_I"].tolist()},
        "gauss_x180_Q_wf": {"type": "arbitrary", "samples": waveforms["gauss_x180_Q"].tolist()},
        "gauss_minus_x90_I_wf": {"type": "arbitrary", "samples": waveforms["gauss_minus_x90_I"].tolist()},
        "gauss_minus_x90_Q_wf": {"type": "arbitrary", "samples": waveforms["gauss_minus_x90_Q"].tolist()},
        "gauss_y90_I_wf": {"type": "arbitrary", "samples": waveforms["gauss_y90_I"].tolist()},
        "gauss_y90_Q_wf": {"type": "arbitrary", "samples": waveforms["gauss_y90_Q"].tolist()},
        "gauss_y180_I_wf": {"type": "arbitrary", "samples": waveforms["gauss_y180_I"].tolist()},
        "gauss_y180_Q_wf": {"type": "arbitrary", "samples": waveforms["gauss_y180_Q"].tolist()},
        "gauss_minus_y90_I_wf": {"type": "arbitrary", "samples": waveforms["gauss_minus_y90_I"].tolist()},
        "gauss_minus_y90_Q_wf": {"type": "arbitrary", "samples": waveforms["gauss_minus_y90_Q"].tolist()},
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
        "rotated_cosine_weights": {
            "cosine": [(np.cos(0.25)), READOUT_LEN],
            "sine": [(np.sin(0.25)), READOUT_LEN],
        },
        "rotated_sine_weights": {
            "cosine": [(-np.sin(0.25)), READOUT_LEN],
            "sine": [(np.cos(0.25)), READOUT_LEN],
        },
        "rotated_minus_sine_weights": {
            "cosine": [(np.sin(0.25)), READOUT_LEN],
            "sine": [(-np.cos(0.25)), READOUT_LEN],
        }
    },
}


# %%