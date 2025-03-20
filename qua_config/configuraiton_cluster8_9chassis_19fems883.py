# %%

from pathlib import Path
import numpy as np
from qualang_tools.units import unit
from itertools import product
from qualang_tools.config.waveform_tools import drag_gaussian_pulse_waveforms
import matplotlib.pyplot as plt



#######################
# AUXILIARY FUNCTIONS #
#######################
u = unit(coerce_to_integer=True)


######################
# Network parameters #
######################
host_ip = "172.16.33.115"  # "172.16.33.101"
cluster_name = "CS_3"  # "Cluster
qop_port = 80 #9510  # Write the QOP port if version < QOP220


#############
# Save Path #
#############

# Path to save data
save_dir = Path(r"/workspaces/data")
save_dir.mkdir(exist_ok=True)
config_path = Path(__file__)
default_additional_files = {str(config_path): config_path.name}


##############
# Parameters #
##############

MW_CON_FEMS = {
    "con1": [1, 2, 3, 4, 5, 6, 7, 8],
    "con2": [1, 2, 3, 4, 5, 6, 7, 8],
    "con3": [1, 2, 3],
}
MW_OUTPUT_PORTS = [1, 2, 3, 4, 5, 6, 7, 8]
MW_INPUT_PORTS = [1, 2]
MW_CON_FEM_PORTS = [(k, v, port) for k, values in MW_CON_FEMS.items() for v, port in product(values, MW_OUTPUT_PORTS)]


# keep in mind that the scope's bandwidth is up to 4.2 GHz
IF = 50 * u.MHz
LO1 = 1.0 * u.GHz - IF
LO2 = 2.0 * u.GHz - IF
BAND = 1


FULL_SCALE_POWER_DBM = 1
CONST_AMP = 0.5
CONST_LEN = 40
READOUT_AMP = 0.5
READOUT_LEN = 200
TOF = 300

PI_AMP = 0.25
PI_LEN = 40
GAUSS_AMP = 0.5
GAUSS_RISE_FALL_LEN = 8 # ensure it's multiple of 4ns 
ARB_AMP = 0.5
ARB_LEN = 100

#####################
#       Utils       #
#####################

def generate_waveforms(rotation_keys, sampling_rate=1e9):
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

        K = int(sampling_rate) / 1e9 if sampling_rate != 1e9 else 1

        wf, der_wf = np.array(drag_gaussian_pulse_waveforms(wf_amp, K * PI_LEN, K * PI_LEN / 5, 0, -200 * u.MHz, 0))

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
waveforms = generate_waveforms(qubit_rotation_keys, sampling_rate=SAMPLING_RATE)



def generate_gaussian_waveform(
    amplitude: float,
    length: int,
    sigma_ratio: float = 0.2,
    rise_fall: str = "rise",
    subtracted: bool = True,
    sampling_rate: float = 1e9,
) -> np.ndarray:
    """
    Creates Gaussian-based DRAG waveforms that compensate for leakage and AC Stark shift.

    :param amplitude: The amplitude in volts.
    :param length: The pulse length in ns.
    :param sigma: The Gaussian standard deviation in ns.
    :param subtracted: Whether to subtract the final value of the waveform.
    :param sampling_rate: The sampling rate in samples/s. Default is 1G samples/s.
    :param rise_fall_full: Specifies the portion of the Gaussian ('rise', 'fall', or 'full').
    :return: A 1D numpy array representing the Gaussian waveform.
    """
    t = np.arange(length, step=1e9 / sampling_rate)  # Full waveform
    if rise_fall == "rise":
        center = (length - 1e9 / sampling_rate)
    elif rise_fall == "fall":
        center = 0
    else:
        raise ValueError("Invalid value for rise_fall_full. Choose from 'rise', 'fall', or 'full'.")

    gauss_wave = amplitude * np.exp(-((t - center) ** 2) / (2 * (2 * sigma_ratio * length) ** 2))
    if subtracted:
        gauss_wave -= gauss_wave.min()  # Subtract the final value
    gauss_wave /= gauss_wave.max()  # Normalize to the peak value
    gauss_wave *= amplitude

    return gauss_wave


# gauss rise
gauss_rise_wf = generate_gaussian_waveform(
    amplitude=GAUSS_AMP,
    length=GAUSS_RISE_FALL_LEN,
    sigma_ratio=0.2,
    rise_fall="rise", # rise or fall
)
# gauss fall
gauss_fall_wf = generate_gaussian_waveform(
    amplitude=GAUSS_AMP,
    length=GAUSS_RISE_FALL_LEN,
    sigma_ratio=0.2,
    rise_fall="fall", # rise or fall
)



def print_elements_ports(elements):
    
    if type(elements) == list and len(elements) >= 1:
        for i, elem in enumerate(elements):
            print(f"{i + 1}, {elem}")


def get_all_elements(element_kind, duc=1):

    if element_kind not in ["qubit", "resonator", "jpa", "trigger"]:
        raise ValueError("element_kind must be one of 'qubit', 'resonator', 'jpa', 'trigger'")

    if element_kind == "trigger":
        return [
            f"{element_kind}_{con}-fem{fem}-port{p}"
            for con, fem, p in MW_CON_FEM_PORTS
        ]

    else:
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
                    "digital_outputs": {
                        p: {}
                        for p in MW_OUTPUT_PORTS
                    },
                } for mw_fem in MW_CON_FEMS[con]
            },
        } for con in MW_CON_FEMS.keys()
    },
    "elements": {
        **{
            f"qubit_{con}-fem{fem}-port{p}-duc{duc}{tw}": {
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
                    "gauss_rise": "gauss_rise_pulse",
                    "gauss_fall": "gauss_fall_pulse",
                    "arb": "arb_pulse",
                },
                "core": f"{con}-fem{fem}-port{p}-duc1",
            }
            for tw in ["", "-twin"]
            for duc in [1, 2]
            for p in MW_OUTPUT_PORTS
            for con in MW_CON_FEMS.keys()
            for fem in MW_CON_FEMS[con]
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
                    "arb": "arb_pulse",
                },
                "core": f"{con}-fem{fem}-port{p}-duc1",
            }
            for p in MW_OUTPUT_PORTS for con in MW_CON_FEMS.keys()
            for fem in MW_CON_FEMS[con]
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
            for p in MW_OUTPUT_PORTS
            for con in MW_CON_FEMS.keys()
            for fem in MW_CON_FEMS[con]
        },
        **{
            f"trigger_{con}-fem{fem}-port{p}": {
                "digitalInputs": {
                    "marker": {
                        "port": (con, fem, p),
                        "delay": 0,
                        "buffer": 0,
                    },
                },
                "operations": {
                    "on": "trigger_pulse",
                },
            }
            for p in MW_OUTPUT_PORTS
            for con in MW_CON_FEMS.keys()
            for fem in MW_CON_FEMS[con]
        },
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
        "gauss_rise_pulse": {
            "operation": "control",
            "length": GAUSS_RISE_FALL_LEN,
            "waveforms": {
                "I": "gauss_rise_wf",
                "Q": "zero_wf",
            },
        },
        "gauss_fall_pulse": {
            "operation": "control",
            "length": GAUSS_RISE_FALL_LEN,
            "waveforms": {
                "I": "gauss_fall_wf",
                "Q": "zero_wf",
            },
        },
        "arb_pulse": {
            "operation": "measurement",
            "length": ARB_LEN,
            "waveforms": {
                "I": "arb_I_wf",
                "Q": "arb_Q_wf",
            },
            "integration_weights": {
                "cos": "cosine_arb_weights",
                "sin": "sine_arb_weights",
                "minus_sin": "minus_sine_arb_weights",
            },
            "digital_marker": "ON",
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
        "trigger_pulse": {
            "operation": "control",
            "length": 1000,
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
        "gauss_rise_wf": {"type": "arbitrary", "samples": gauss_rise_wf.tolist()},
        "gauss_fall_wf": {"type": "arbitrary", "samples": gauss_fall_wf.tolist()},
        "arb_I_wf": {"type": "arbitrary", "samples": [ARB_AMP] * ARB_LEN},
        "arb_Q_wf": {"type": "arbitrary", "samples": [ARB_AMP] * ARB_LEN},
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
        },
        "cosine_arb_weights": {
            "cosine": [(1.0, ARB_LEN)],
            "sine": [(0.0, ARB_LEN)],
        },
        "sine_arb_weights": {
            "cosine": [(0.0, ARB_LEN)],
            "sine": [(1.0, ARB_LEN)],
        },
        "minus_sine_arb_weights": {
            "cosine": [(0.0, ARB_LEN)],
            "sine": [(-1.0, ARB_LEN)],
        },
    },
}


# %%