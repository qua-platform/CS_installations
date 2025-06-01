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
qop_ip = "172.16.33.115"  # Write the QM router IP address
cluster_name = 'CS_3'  # Write your cluster_name if version >= QOP220
qop_port = None  # Write the QOP port if version < QOP220
octave_config = None


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


#####################
# OPX configuration #
#####################


# MARK: QUBITS
#############################################
#                  Qubits                   #
#############################################
# CW pulse parameter
CONST_LEN = 1000
CONST_AMP = 0.25 # 125 * u.mV

# Relaxation time
qb_reset_time = 200_000
depletion_time = 10_000

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
        "IF": -300 * u.MHz,
        "con": "con1",
        "fem": 1,
        "ao": 2,
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
        "IF": -300 * u.MHz,
        "con": "con1",
        "fem": 1,
        "ao": 3,
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
        "IF": -300 * u.MHz,
        "con": "con1",
        "fem": 1,
        "ao": 4,
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
        "IF": -300 * u.MHz,
        "con": "con1",
        "fem": 1,
        "ao": 5,
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
        "IF": -300 * u.MHz,
        "con": "con1",
        "fem": 1,
        "ao": 6,
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
        "IF": -300 * u.MHz,
        "con": "con1",
        "fem": 1,
        "ao": 7,
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
        "IF": -300 * u.MHz,
        "con": "con1",
        "fem": 1,
        "ao": 8,
        "band": 2,
        "full_scale_power_dbm": -11,
        "delay": 0,
        "core": "fem1-thread7",
    },
    # "q8_xy": {
    #     "amp": 0.5,
    #     "pi_len": PI_LEN,
    #     "pi_sigma": PI_SIGMA, 
    #     "anharmonicity": -200 * u.MHz,
    #     "drag_coefficient": 0.0,
    #     "ac_stark_shift": 0.0 * u.MHz, # 5.0 * u.MHz
    #     "LO": 5.0 * u.GHz,
    #     "IF": -300 * u.MHz,
    #     "con": "con1",
    #     "fem": 1,
    #     "ao": 8,
    #     "band": 2,
    #     "full_scale_power_dbm": -11,
    #     "delay": 0,
    #     "core": "fem1-thread8",
    # },
}

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


# MARK: CROSS RESONANCE
#############################################
#              CROSS RESONANCE              #
#############################################

qubit_pairs = [
    ["1", "2"], ["2", "1"],
    ["2", "3"], ["3", "2"],
    ["3", "4"], ["4", "3"],
    ["4", "5"], ["5", "4"],
    ["5", "6"], ["6", "5"],
    ["6", "7"], ["7", "6"],
    # ["7", "8"], ["8", "7"],
    # ["8", "1"], ["1", "8"],
]

keys_common = [
    "LO",
    "IF",
    "con",
    "fem",
    "ao",
    "band",
    "full_scale_power_dbm",
    "delay",
    "core",
]

# Constants for Pi Pulse
CR_SQUARE_AMP = 0.9
CR_SQUARE_LEN = 120
CR_FLATTOP_AMP = 0.2
CR_FLATTOP_LEN = 100
CR_GAUSSIAN_RISE_FALL_AMP = CR_FLATTOP_AMP
CR_GAUSSIAN_RISE_FALL_LEN = 18
CR_GAUSSIAN_RISE_FALL_PAD_LEN = 0 if CR_GAUSSIAN_RISE_FALL_LEN % 4 == 0 else (4 - CR_GAUSSIAN_RISE_FALL_LEN % 4)

CR_SQUARE_PHASE = 0.0
CR_FLATTOP_PHASE = 0.0
CR_GAUSSIAN_FLATTOP_PHASE = 0.0

# READOUT_GAUSSIAN_FLATTOP_TOTAL_LEN
CR_GAUSSIAN_FLATTOP_TOTAL_AMP = CR_FLATTOP_AMP
CR_GAUSSIAN_FLATTOP_TOTAL_LEN = 2 * CR_GAUSSIAN_RISE_FALL_LEN + CR_FLATTOP_LEN

assert (CR_GAUSSIAN_RISE_FALL_LEN + CR_GAUSSIAN_RISE_FALL_PAD_LEN) % 4 == 0, "duration of padded gaussian rise / fall len must be integer multiple of 4 ns"

# Constants for each qubit for CR DRIVE
CR_DRIVE_CONSTANTS = {
    **{f"cr_drive_c{c}t{t}": {
        # main element
        "square_amp": CR_SQUARE_AMP,
        "square_len": CR_SQUARE_LEN,
        "flattop_amp": CR_FLATTOP_AMP,
        "flattop_len": CR_FLATTOP_LEN,
        "gaussian_rise_flattop_fall_amp": CR_GAUSSIAN_FLATTOP_TOTAL_AMP,
        "gaussian_rise_flattop_fall_len": CR_GAUSSIAN_FLATTOP_TOTAL_LEN, 
        "square_phase": CR_SQUARE_PHASE, # in units of 2pi
        "flattop_phase": CR_FLATTOP_PHASE, # in units of 2pi
        "gaussian_rise_flattop_fall_phase": CR_FLATTOP_PHASE, # in units of 2pi
        # twin element
        "gaussian_rise_fall_amp": CR_GAUSSIAN_RISE_FALL_AMP,
        "gaussian_rise_fall_len": CR_GAUSSIAN_RISE_FALL_LEN,
        "gaussian_rise_fall_pad_len": CR_GAUSSIAN_RISE_FALL_PAD_LEN,
        # common
        "LO": QUBIT_CONSTANTS[f"q{t}_xy"]["LO"],
        "IF": QUBIT_CONSTANTS[f"q{t}_xy"]["IF"],
        "con": QUBIT_CONSTANTS[f"q{c}_xy"]["con"],
        "fem": QUBIT_CONSTANTS[f"q{c}_xy"]["fem"],
        "ao": QUBIT_CONSTANTS[f"q{c}_xy"]["ao"],
        "band": QUBIT_CONSTANTS[f"q{t}_xy"]["band"],
        "full_scale_power_dbm": -11,
        "delay": QUBIT_CONSTANTS[f"q{c}_xy"]["delay"],
        "core": QUBIT_CONSTANTS[f"q{c}_xy"]["core"],
    } for c, t in qubit_pairs}
}
# # update after findng the optimal parameters
# CR_DRIVE_CONSTANTS["cr_drive_c1t2"].update({"square_amp": CR_SQUARE_AMP, "square_len": CR_SQUARE_LEN})
# CR_DRIVE_CONSTANTS["cr_drive_c2t1"].update({"square_amp": CR_SQUARE_AMP, "square_len": CR_SQUARE_LEN})
# CR_DRIVE_CONSTANTS["cr_drive_c2t3"].update({"square_amp": CR_SQUARE_AMP, "square_len": CR_SQUARE_LEN})
# CR_DRIVE_CONSTANTS["cr_drive_c3t2"].update({"square_amp": CR_SQUARE_AMP, "square_len": CR_SQUARE_LEN})
# CR_DRIVE_CONSTANTS["cr_drive_c3t4"].update({"square_amp": CR_SQUARE_AMP, "square_len": CR_SQUARE_LEN})
# CR_DRIVE_CONSTANTS["cr_drive_c4t3"].update({"square_amp": CR_SQUARE_AMP, "square_len": CR_SQUARE_LEN})
# CR_DRIVE_CONSTANTS["cr_drive_c4t5"].update({"square_amp": CR_SQUARE_AMP, "square_len": CR_SQUARE_LEN})
# CR_DRIVE_CONSTANTS["cr_drive_c5t4"].update({"square_amp": CR_SQUARE_AMP, "square_len": CR_SQUARE_LEN})
# CR_DRIVE_CONSTANTS["cr_drive_c5t6"].update({"square_amp": CR_SQUARE_AMP, "square_len": CR_SQUARE_LEN})
# CR_DRIVE_CONSTANTS["cr_drive_c6t5"].update({"square_amp": CR_SQUARE_AMP, "square_len": CR_SQUARE_LEN})
# CR_DRIVE_CONSTANTS["cr_drive_c6t7"].update({"square_amp": CR_SQUARE_AMP, "square_len": CR_SQUARE_LEN})
# CR_DRIVE_CONSTANTS["cr_drive_c7t6"].update({"square_amp": CR_SQUARE_AMP, "square_len": CR_SQUARE_LEN})
# CR_DRIVE_CONSTANTS["cr_drive_c7t8"].update({"square_amp": CR_SQUARE_AMP, "square_len": CR_SQUARE_LEN})
# CR_DRIVE_CONSTANTS["cr_drive_c8t7"].update({"square_amp": CR_SQUARE_AMP, "square_len": CR_SQUARE_LEN})
# CR_DRIVE_CONSTANTS["cr_drive_c8t1"].update({"square_amp": CR_SQUARE_AMP, "square_len": CR_SQUARE_LEN})
# CR_DRIVE_CONSTANTS["cr_drive_c1t8"].update({"square_amp": CR_SQUARE_AMP, "square_len": CR_SQUARE_LEN})

# # update after findng the optimal parameters
# CR_DRIVE_CONSTANTS["cr_drive_c1t2"].update({"flattop_amp": CR_FLATTOP_AMP, "flattop_len": CR_FLATTOP_LEN, "gaussian_rise_fall_len": CR_GAUSSIAN_RISE_FALL_LEN, "gaussian_rise_fall_pad_len": CR_GAUSSIAN_RISE_FALL_PAD_LEN})
# CR_DRIVE_CONSTANTS["cr_drive_c2t1"].update({"flattop_amp": CR_FLATTOP_AMP, "flattop_len": CR_FLATTOP_LEN, "gaussian_rise_fall_len": CR_GAUSSIAN_RISE_FALL_LEN, "gaussian_rise_fall_pad_len": CR_GAUSSIAN_RISE_FALL_PAD_LEN})
# CR_DRIVE_CONSTANTS["cr_drive_c2t3"].update({"flattop_amp": CR_FLATTOP_AMP, "flattop_len": CR_FLATTOP_LEN, "gaussian_rise_fall_len": CR_GAUSSIAN_RISE_FALL_LEN, "gaussian_rise_fall_pad_len": CR_GAUSSIAN_RISE_FALL_PAD_LEN})
# CR_DRIVE_CONSTANTS["cr_drive_c3t2"].update({"flattop_amp": CR_FLATTOP_AMP, "flattop_len": CR_FLATTOP_LEN, "gaussian_rise_fall_len": CR_GAUSSIAN_RISE_FALL_LEN, "gaussian_rise_fall_pad_len": CR_GAUSSIAN_RISE_FALL_PAD_LEN})
# CR_DRIVE_CONSTANTS["cr_drive_c3t4"].update({"flattop_amp": CR_FLATTOP_AMP, "flattop_len": CR_FLATTOP_LEN, "gaussian_rise_fall_len": CR_GAUSSIAN_RISE_FALL_LEN, "gaussian_rise_fall_pad_len": CR_GAUSSIAN_RISE_FALL_PAD_LEN})
# CR_DRIVE_CONSTANTS["cr_drive_c4t3"].update({"flattop_amp": CR_FLATTOP_AMP, "flattop_len": CR_FLATTOP_LEN, "gaussian_rise_fall_len": CR_GAUSSIAN_RISE_FALL_LEN, "gaussian_rise_fall_pad_len": CR_GAUSSIAN_RISE_FALL_PAD_LEN})
# CR_DRIVE_CONSTANTS["cr_drive_c4t5"].update({"flattop_amp": CR_FLATTOP_AMP, "flattop_len": CR_FLATTOP_LEN, "gaussian_rise_fall_len": CR_GAUSSIAN_RISE_FALL_LEN, "gaussian_rise_fall_pad_len": CR_GAUSSIAN_RISE_FALL_PAD_LEN})
# CR_DRIVE_CONSTANTS["cr_drive_c5t4"].update({"flattop_amp": CR_FLATTOP_AMP, "flattop_len": CR_FLATTOP_LEN, "gaussian_rise_fall_len": CR_GAUSSIAN_RISE_FALL_LEN, "gaussian_rise_fall_pad_len": CR_GAUSSIAN_RISE_FALL_PAD_LEN})
# CR_DRIVE_CONSTANTS["cr_drive_c5t6"].update({"flattop_amp": CR_FLATTOP_AMP, "flattop_len": CR_FLATTOP_LEN, "gaussian_rise_fall_len": CR_GAUSSIAN_RISE_FALL_LEN, "gaussian_rise_fall_pad_len": CR_GAUSSIAN_RISE_FALL_PAD_LEN})
# CR_DRIVE_CONSTANTS["cr_drive_c6t5"].update({"flattop_amp": CR_FLATTOP_AMP, "flattop_len": CR_FLATTOP_LEN, "gaussian_rise_fall_len": CR_GAUSSIAN_RISE_FALL_LEN, "gaussian_rise_fall_pad_len": CR_GAUSSIAN_RISE_FALL_PAD_LEN})
# CR_DRIVE_CONSTANTS["cr_drive_c6t7"].update({"flattop_amp": CR_FLATTOP_AMP, "flattop_len": CR_FLATTOP_LEN, "gaussian_rise_fall_len": CR_GAUSSIAN_RISE_FALL_LEN, "gaussian_rise_fall_pad_len": CR_GAUSSIAN_RISE_FALL_PAD_LEN})
# CR_DRIVE_CONSTANTS["cr_drive_c7t6"].update({"flattop_amp": CR_FLATTOP_AMP, "flattop_len": CR_FLATTOP_LEN, "gaussian_rise_fall_len": CR_GAUSSIAN_RISE_FALL_LEN, "gaussian_rise_fall_pad_len": CR_GAUSSIAN_RISE_FALL_PAD_LEN})
# CR_DRIVE_CONSTANTS["cr_drive_c7t8"].update({"flattop_amp": CR_FLATTOP_AMP, "flattop_len": CR_FLATTOP_LEN, "gaussian_rise_fall_len": CR_GAUSSIAN_RISE_FALL_LEN, "gaussian_rise_fall_pad_len": CR_GAUSSIAN_RISE_FALL_PAD_LEN})
# CR_DRIVE_CONSTANTS["cr_drive_c8t7"].update({"flattop_amp": CR_FLATTOP_AMP, "flattop_len": CR_FLATTOP_LEN, "gaussian_rise_fall_len": CR_GAUSSIAN_RISE_FALL_LEN, "gaussian_rise_fall_pad_len": CR_GAUSSIAN_RISE_FALL_PAD_LEN})
# CR_DRIVE_CONSTANTS["cr_drive_c8t1"].update({"flattop_amp": CR_FLATTOP_AMP, "flattop_len": CR_FLATTOP_LEN, "gaussian_rise_fall_len": CR_GAUSSIAN_RISE_FALL_LEN, "gaussian_rise_fall_pad_len": CR_GAUSSIAN_RISE_FALL_PAD_LEN})
# CR_DRIVE_CONSTANTS["cr_drive_c1t8"].update({"flattop_amp": CR_FLATTOP_AMP, "flattop_len": CR_FLATTOP_LEN, "gaussian_rise_fall_len": CR_GAUSSIAN_RISE_FALL_LEN, "gaussian_rise_fall_pad_len": CR_GAUSSIAN_RISE_FALL_PAD_LEN})

# # update after findng the optimal parameters
# CR_DRIVE_CONSTANTS["cr_drive_c1t2"].update({"square_phase": CR_SQUARE_PHASE, "flattop_phase": CR_FLATTOP_PHASE, "gaussian_rise_flattop_fall_phase": CR_FLATTOP_PHASE})
# CR_DRIVE_CONSTANTS["cr_drive_c2t1"].update({"square_phase": CR_SQUARE_PHASE, "flattop_phase": CR_FLATTOP_PHASE, "gaussian_rise_flattop_fall_phase": CR_FLATTOP_PHASE})
# CR_DRIVE_CONSTANTS["cr_drive_c2t3"].update({"square_phase": CR_SQUARE_PHASE, "flattop_phase": CR_FLATTOP_PHASE, "gaussian_rise_flattop_fall_phase": CR_FLATTOP_PHASE})
# CR_DRIVE_CONSTANTS["cr_drive_c3t2"].update({"square_phase": CR_SQUARE_PHASE, "flattop_phase": CR_FLATTOP_PHASE, "gaussian_rise_flattop_fall_phase": CR_FLATTOP_PHASE})
# CR_DRIVE_CONSTANTS["cr_drive_c3t4"].update({"square_phase": CR_SQUARE_PHASE, "flattop_phase": CR_FLATTOP_PHASE, "gaussian_rise_flattop_fall_phase": CR_FLATTOP_PHASE})
# CR_DRIVE_CONSTANTS["cr_drive_c4t3"].update({"square_phase": CR_SQUARE_PHASE, "flattop_phase": CR_FLATTOP_PHASE, "gaussian_rise_flattop_fall_phase": CR_FLATTOP_PHASE})
# CR_DRIVE_CONSTANTS["cr_drive_c4t5"].update({"square_phase": CR_SQUARE_PHASE, "flattop_phase": CR_FLATTOP_PHASE, "gaussian_rise_flattop_fall_phase": CR_FLATTOP_PHASE})
# CR_DRIVE_CONSTANTS["cr_drive_c5t4"].update({"square_phase": CR_SQUARE_PHASE, "flattop_phase": CR_FLATTOP_PHASE, "gaussian_rise_flattop_fall_phase": CR_FLATTOP_PHASE})
# CR_DRIVE_CONSTANTS["cr_drive_c5t6"].update({"square_phase": CR_SQUARE_PHASE, "flattop_phase": CR_FLATTOP_PHASE, "gaussian_rise_flattop_fall_phase": CR_FLATTOP_PHASE})
# CR_DRIVE_CONSTANTS["cr_drive_c6t5"].update({"square_phase": CR_SQUARE_PHASE, "flattop_phase": CR_FLATTOP_PHASE, "gaussian_rise_flattop_fall_phase": CR_FLATTOP_PHASE})
# CR_DRIVE_CONSTANTS["cr_drive_c6t7"].update({"square_phase": CR_SQUARE_PHASE, "flattop_phase": CR_FLATTOP_PHASE, "gaussian_rise_flattop_fall_phase": CR_FLATTOP_PHASE})
# CR_DRIVE_CONSTANTS["cr_drive_c7t6"].update({"square_phase": CR_SQUARE_PHASE, "flattop_phase": CR_FLATTOP_PHASE, "gaussian_rise_flattop_fall_phase": CR_FLATTOP_PHASE})
# CR_DRIVE_CONSTANTS["cr_drive_c7t8"].update({"square_phase": CR_SQUARE_PHASE, "flattop_phase": CR_FLATTOP_PHASE, "gaussian_rise_flattop_fall_phase": CR_FLATTOP_PHASE})
# CR_DRIVE_CONSTANTS["cr_drive_c8t7"].update({"square_phase": CR_SQUARE_PHASE, "flattop_phase": CR_FLATTOP_PHASE, "gaussian_rise_flattop_fall_phase": CR_FLATTOP_PHASE})
# CR_DRIVE_CONSTANTS["cr_drive_c8t1"].update({"square_phase": CR_SQUARE_PHASE, "flattop_phase": CR_FLATTOP_PHASE, "gaussian_rise_flattop_fall_phase": CR_FLATTOP_PHASE})
# CR_DRIVE_CONSTANTS["cr_drive_c1t8"].update({"square_phase": CR_SQUARE_PHASE, "flattop_phase": CR_FLATTOP_PHASE, "gaussian_rise_flattop_fall_phase": CR_FLATTOP_PHASE})


# Constants for each qubit for CR CANCEL DRIVE
CR_CANCEL_CONSTANTS = {
    **{f"cr_cancel_c{c}t{t}": {
        # main element
        "square_amp": CR_SQUARE_AMP,
        "square_len": CR_SQUARE_LEN,
        "flattop_amp": CR_FLATTOP_AMP,
        "flattop_len": CR_FLATTOP_LEN,
        "gaussian_rise_flattop_fall_amp": CR_GAUSSIAN_FLATTOP_TOTAL_AMP,
        "gaussian_rise_flattop_fall_len": CR_GAUSSIAN_FLATTOP_TOTAL_LEN, 
        "square_phase": CR_SQUARE_PHASE, # in units of 2pi
        "flattop_phase": CR_FLATTOP_PHASE, # in units of 2pi
        "gaussian_rise_flattop_fall_phase": CR_FLATTOP_PHASE, # in units of 2pi
        # twin element
        "gaussian_rise_fall_amp": CR_GAUSSIAN_RISE_FALL_AMP,
        "gaussian_rise_fall_len": CR_GAUSSIAN_RISE_FALL_LEN,
        "gaussian_rise_fall_pad_len": CR_GAUSSIAN_RISE_FALL_PAD_LEN,
        # common
        "LO": QUBIT_CONSTANTS[f"q{t}_xy"]["LO"],
        "IF": QUBIT_CONSTANTS[f"q{t}_xy"]["IF"],
        "con": QUBIT_CONSTANTS[f"q{t}_xy"]["con"],
        "fem": QUBIT_CONSTANTS[f"q{t}_xy"]["fem"],
        "ao": QUBIT_CONSTANTS[f"q{t}_xy"]["ao"],
        "band": QUBIT_CONSTANTS[f"q{t}_xy"]["band"],
        "full_scale_power_dbm": -11,
        "delay": QUBIT_CONSTANTS[f"q{t}_xy"]["delay"],
        "core": QUBIT_CONSTANTS[f"q{t}_xy"]["core"],
    } for c, t in qubit_pairs}
}
# # update after findng the optimal parameters
# CR_CANCEL_CONSTANTS["cr_cancel_c1t2"].update({"square_amp": CR_SQUARE_AMP, "square_len": CR_SQUARE_LEN})
# CR_CANCEL_CONSTANTS["cr_cancel_c2t1"].update({"square_amp": CR_SQUARE_AMP, "square_len": CR_SQUARE_LEN})
# CR_CANCEL_CONSTANTS["cr_cancel_c2t3"].update({"square_amp": CR_SQUARE_AMP, "square_len": CR_SQUARE_LEN})
# CR_CANCEL_CONSTANTS["cr_cancel_c3t2"].update({"square_amp": CR_SQUARE_AMP, "square_len": CR_SQUARE_LEN})
# CR_CANCEL_CONSTANTS["cr_cancel_c3t4"].update({"square_amp": CR_SQUARE_AMP, "square_len": CR_SQUARE_LEN})
# CR_CANCEL_CONSTANTS["cr_cancel_c4t3"].update({"square_amp": CR_SQUARE_AMP, "square_len": CR_SQUARE_LEN})
# CR_CANCEL_CONSTANTS["cr_cancel_c4t5"].update({"square_amp": CR_SQUARE_AMP, "square_len": CR_SQUARE_LEN})
# CR_CANCEL_CONSTANTS["cr_cancel_c5t4"].update({"square_amp": CR_SQUARE_AMP, "square_len": CR_SQUARE_LEN})
# CR_CANCEL_CONSTANTS["cr_cancel_c5t6"].update({"square_amp": CR_SQUARE_AMP, "square_len": CR_SQUARE_LEN})
# CR_CANCEL_CONSTANTS["cr_cancel_c6t5"].update({"square_amp": CR_SQUARE_AMP, "square_len": CR_SQUARE_LEN})
# CR_CANCEL_CONSTANTS["cr_cancel_c6t7"].update({"square_amp": CR_SQUARE_AMP, "square_len": CR_SQUARE_LEN})
# CR_CANCEL_CONSTANTS["cr_cancel_c7t6"].update({"square_amp": CR_SQUARE_AMP, "square_len": CR_SQUARE_LEN})
# CR_CANCEL_CONSTANTS["cr_cancel_c7t8"].update({"square_amp": CR_SQUARE_AMP, "square_len": CR_SQUARE_LEN})
# CR_CANCEL_CONSTANTS["cr_cancel_c8t7"].update({"square_amp": CR_SQUARE_AMP, "square_len": CR_SQUARE_LEN})
# CR_CANCEL_CONSTANTS["cr_cancel_c8t1"].update({"square_amp": CR_SQUARE_AMP, "square_len": CR_SQUARE_LEN})
# CR_CANCEL_CONSTANTS["cr_cancel_c1t8"].update({"square_amp": CR_SQUARE_AMP, "square_len": CR_SQUARE_LEN})

# # update after findng the optimal parameters
# CR_CANCEL_CONSTANTS["cr_cancel_c1t2"].update({"flattop_amp": CR_FLATTOP_AMP, "flattop_len": CR_FLATTOP_LEN, "gaussian_rise_fall_len": CR_GAUSSIAN_RISE_FALL_LEN, "gaussian_rise_fall_pad_len": CR_GAUSSIAN_RISE_FALL_PAD_LEN})
# CR_CANCEL_CONSTANTS["cr_cancel_c2t1"].update({"flattop_amp": CR_FLATTOP_AMP, "flattop_len": CR_FLATTOP_LEN, "gaussian_rise_fall_len": CR_GAUSSIAN_RISE_FALL_LEN, "gaussian_rise_fall_pad_len": CR_GAUSSIAN_RISE_FALL_PAD_LEN})
# CR_CANCEL_CONSTANTS["cr_cancel_c2t3"].update({"flattop_amp": CR_FLATTOP_AMP, "flattop_len": CR_FLATTOP_LEN, "gaussian_rise_fall_len": CR_GAUSSIAN_RISE_FALL_LEN, "gaussian_rise_fall_pad_len": CR_GAUSSIAN_RISE_FALL_PAD_LEN})
# CR_CANCEL_CONSTANTS["cr_cancel_c3t2"].update({"flattop_amp": CR_FLATTOP_AMP, "flattop_len": CR_FLATTOP_LEN, "gaussian_rise_fall_len": CR_GAUSSIAN_RISE_FALL_LEN, "gaussian_rise_fall_pad_len": CR_GAUSSIAN_RISE_FALL_PAD_LEN})
# CR_CANCEL_CONSTANTS["cr_cancel_c3t4"].update({"flattop_amp": CR_FLATTOP_AMP, "flattop_len": CR_FLATTOP_LEN, "gaussian_rise_fall_len": CR_GAUSSIAN_RISE_FALL_LEN, "gaussian_rise_fall_pad_len": CR_GAUSSIAN_RISE_FALL_PAD_LEN})
# CR_CANCEL_CONSTANTS["cr_cancel_c4t3"].update({"flattop_amp": CR_FLATTOP_AMP, "flattop_len": CR_FLATTOP_LEN, "gaussian_rise_fall_len": CR_GAUSSIAN_RISE_FALL_LEN, "gaussian_rise_fall_pad_len": CR_GAUSSIAN_RISE_FALL_PAD_LEN})
# CR_CANCEL_CONSTANTS["cr_cancel_c4t5"].update({"flattop_amp": CR_FLATTOP_AMP, "flattop_len": CR_FLATTOP_LEN, "gaussian_rise_fall_len": CR_GAUSSIAN_RISE_FALL_LEN, "gaussian_rise_fall_pad_len": CR_GAUSSIAN_RISE_FALL_PAD_LEN})
# CR_CANCEL_CONSTANTS["cr_cancel_c5t4"].update({"flattop_amp": CR_FLATTOP_AMP, "flattop_len": CR_FLATTOP_LEN, "gaussian_rise_fall_len": CR_GAUSSIAN_RISE_FALL_LEN, "gaussian_rise_fall_pad_len": CR_GAUSSIAN_RISE_FALL_PAD_LEN})
# CR_CANCEL_CONSTANTS["cr_cancel_c5t6"].update({"flattop_amp": CR_FLATTOP_AMP, "flattop_len": CR_FLATTOP_LEN, "gaussian_rise_fall_len": CR_GAUSSIAN_RISE_FALL_LEN, "gaussian_rise_fall_pad_len": CR_GAUSSIAN_RISE_FALL_PAD_LEN})
# CR_CANCEL_CONSTANTS["cr_cancel_c6t5"].update({"flattop_amp": CR_FLATTOP_AMP, "flattop_len": CR_FLATTOP_LEN, "gaussian_rise_fall_len": CR_GAUSSIAN_RISE_FALL_LEN, "gaussian_rise_fall_pad_len": CR_GAUSSIAN_RISE_FALL_PAD_LEN})
# CR_CANCEL_CONSTANTS["cr_cancel_c6t7"].update({"flattop_amp": CR_FLATTOP_AMP, "flattop_len": CR_FLATTOP_LEN, "gaussian_rise_fall_len": CR_GAUSSIAN_RISE_FALL_LEN, "gaussian_rise_fall_pad_len": CR_GAUSSIAN_RISE_FALL_PAD_LEN})
# CR_CANCEL_CONSTANTS["cr_cancel_c7t6"].update({"flattop_amp": CR_FLATTOP_AMP, "flattop_len": CR_FLATTOP_LEN, "gaussian_rise_fall_len": CR_GAUSSIAN_RISE_FALL_LEN, "gaussian_rise_fall_pad_len": CR_GAUSSIAN_RISE_FALL_PAD_LEN})
# CR_CANCEL_CONSTANTS["cr_cancel_c7t8"].update({"flattop_amp": CR_FLATTOP_AMP, "flattop_len": CR_FLATTOP_LEN, "gaussian_rise_fall_len": CR_GAUSSIAN_RISE_FALL_LEN, "gaussian_rise_fall_pad_len": CR_GAUSSIAN_RISE_FALL_PAD_LEN})
# CR_CANCEL_CONSTANTS["cr_cancel_c8t7"].update({"flattop_amp": CR_FLATTOP_AMP, "flattop_len": CR_FLATTOP_LEN, "gaussian_rise_fall_len": CR_GAUSSIAN_RISE_FALL_LEN, "gaussian_rise_fall_pad_len": CR_GAUSSIAN_RISE_FALL_PAD_LEN})
# CR_CANCEL_CONSTANTS["cr_cancel_c8t1"].update({"flattop_amp": CR_FLATTOP_AMP, "flattop_len": CR_FLATTOP_LEN, "gaussian_rise_fall_len": CR_GAUSSIAN_RISE_FALL_LEN, "gaussian_rise_fall_pad_len": CR_GAUSSIAN_RISE_FALL_PAD_LEN})
# CR_CANCEL_CONSTANTS["cr_cancel_c1t8"].update({"flattop_amp": CR_FLATTOP_AMP, "flattop_len": CR_FLATTOP_LEN, "gaussian_rise_fall_len": CR_GAUSSIAN_RISE_FALL_LEN, "gaussian_rise_fall_pad_len": CR_GAUSSIAN_RISE_FALL_PAD_LEN})

# # update after findng the optimal parameters
# CR_CANCEL_CONSTANTS["cr_cancel_c1t2"].update({"square_phase": CR_SQUARE_PHASE, "flattop_phase": CR_FLATTOP_PHASE, "gaussian_rise_flattop_fall_phase": CR_FLATTOP_PHASE})
# CR_CANCEL_CONSTANTS["cr_cancel_c2t1"].update({"square_phase": CR_SQUARE_PHASE, "flattop_phase": CR_FLATTOP_PHASE, "gaussian_rise_flattop_fall_phase": CR_FLATTOP_PHASE})
# CR_CANCEL_CONSTANTS["cr_cancel_c2t3"].update({"square_phase": CR_SQUARE_PHASE, "flattop_phase": CR_FLATTOP_PHASE, "gaussian_rise_flattop_fall_phase": CR_FLATTOP_PHASE})
# CR_CANCEL_CONSTANTS["cr_cancel_c3t2"].update({"square_phase": CR_SQUARE_PHASE, "flattop_phase": CR_FLATTOP_PHASE, "gaussian_rise_flattop_fall_phase": CR_FLATTOP_PHASE})
# CR_CANCEL_CONSTANTS["cr_cancel_c3t4"].update({"square_phase": CR_SQUARE_PHASE, "flattop_phase": CR_FLATTOP_PHASE, "gaussian_rise_flattop_fall_phase": CR_FLATTOP_PHASE})
# CR_CANCEL_CONSTANTS["cr_cancel_c4t3"].update({"square_phase": CR_SQUARE_PHASE, "flattop_phase": CR_FLATTOP_PHASE, "gaussian_rise_flattop_fall_phase": CR_FLATTOP_PHASE})
# CR_CANCEL_CONSTANTS["cr_cancel_c4t5"].update({"square_phase": CR_SQUARE_PHASE, "flattop_phase": CR_FLATTOP_PHASE, "gaussian_rise_flattop_fall_phase": CR_FLATTOP_PHASE})
# CR_CANCEL_CONSTANTS["cr_cancel_c5t4"].update({"square_phase": CR_SQUARE_PHASE, "flattop_phase": CR_FLATTOP_PHASE, "gaussian_rise_flattop_fall_phase": CR_FLATTOP_PHASE})
# CR_CANCEL_CONSTANTS["cr_cancel_c5t6"].update({"square_phase": CR_SQUARE_PHASE, "flattop_phase": CR_FLATTOP_PHASE, "gaussian_rise_flattop_fall_phase": CR_FLATTOP_PHASE})
# CR_CANCEL_CONSTANTS["cr_cancel_c6t5"].update({"square_phase": CR_SQUARE_PHASE, "flattop_phase": CR_FLATTOP_PHASE, "gaussian_rise_flattop_fall_phase": CR_FLATTOP_PHASE})
# CR_CANCEL_CONSTANTS["cr_cancel_c6t7"].update({"square_phase": CR_SQUARE_PHASE, "flattop_phase": CR_FLATTOP_PHASE, "gaussian_rise_flattop_fall_phase": CR_FLATTOP_PHASE})
# CR_CANCEL_CONSTANTS["cr_cancel_c7t6"].update({"square_phase": CR_SQUARE_PHASE, "flattop_phase": CR_FLATTOP_PHASE, "gaussian_rise_flattop_fall_phase": CR_FLATTOP_PHASE})
# CR_CANCEL_CONSTANTS["cr_cancel_c7t8"].update({"square_phase": CR_SQUARE_PHASE, "flattop_phase": CR_FLATTOP_PHASE, "gaussian_rise_flattop_fall_phase": CR_FLATTOP_PHASE})
# CR_CANCEL_CONSTANTS["cr_cancel_c8t7"].update({"square_phase": CR_SQUARE_PHASE, "flattop_phase": CR_FLATTOP_PHASE, "gaussian_rise_flattop_fall_phase": CR_FLATTOP_PHASE})
# CR_CANCEL_CONSTANTS["cr_cancel_c8t1"].update({"square_phase": CR_SQUARE_PHASE, "flattop_phase": CR_FLATTOP_PHASE, "gaussian_rise_flattop_fall_phase": CR_FLATTOP_PHASE})
# CR_CANCEL_CONSTANTS["cr_cancel_c1t8"].update({"square_phase": CR_SQUARE_PHASE, "flattop_phase": CR_FLATTOP_PHASE, "gaussian_rise_flattop_fall_phase": CR_FLATTOP_PHASE})

# Generate keys for positive/negative pulses for cr_drive/cr_cancel
for _constants in [CR_DRIVE_CONSTANTS, CR_CANCEL_CONSTANTS]:
    for cr, cr_dict in _constants.items():
        # Directly updating values
        cr_dict.update({
            "gaussian_rise_fall_amp": cr_dict["flattop_amp"],
            "gaussian_rise_flattop_fall_amp": cr_dict["flattop_amp"],
            "gaussian_rise_flattop_fall_len": cr_dict["flattop_len"] + 2 * cr_dict["gaussian_rise_fall_len"] + 2 * cr_dict["gaussian_rise_fall_pad_len"],
        })

        # Collect updates in a separate dict to avoid modifying while iterating
        updates = {}
        for sign, sign_name in zip([1, -1], ["positive", "negative"]):
            for k, v in cr_dict.items():
                if k in keys_common:
                    continue
                # Determine updates to be made based on the key type
                if k.endswith("amp"):
                    updates[k.replace("amp", f"{sign_name}_amp")] = sign * v
                    updates[k.replace("amp", f"{sign_name}_amp").replace("rise_fall", "rise")] = sign * v
                    updates[k.replace("amp", f"{sign_name}_amp").replace("rise_fall", "fall")] = sign * v
                elif k.endswith("pad_len"):
                    updates[k.replace("pad_len", f"{sign_name}_pad_len")] = v
                    updates[k.replace("pad_len", f"{sign_name}_pad_len").replace("rise_fall", "rise")] = v
                    updates[k.replace("pad_len", f"{sign_name}_pad_len").replace("rise_fall", "fall")] = v
                elif k.endswith("len"):
                    updates[k.replace("len", f"{sign_name}_len")] = v
                    updates[k.replace("len", f"{sign_name}_len").replace("rise_fall", "rise")] = v
                    updates[k.replace("len", f"{sign_name}_len").replace("rise_fall", "fall")] = v
                elif k.endswith("phase"):
                    updates[k.replace("phase", f"{sign_name}_phase")] = v
                    updates[k.replace("phase", f"{sign_name}_phase").replace("rise_fall", "rise")] = v
                    updates[k.replace("phase", f"{sign_name}_phase").replace("rise_fall", "fall")] = v
                else:
                    raise ValueError(f"unknown key '{k}' passed to CR_CONSTANTS")

        # Keep only the keys in 'keys_common'
        _constants[cr] = {k: v for k, v in cr_dict.items() if k in keys_common}

        # Apply all the updates at once (add all the k/v of positive/negative)
        _constants[cr].update(updates)


# MARK: RESONATORS
#############################################
#                Resonators                 #
#############################################

READOUT_LEN = 1000
READOUT_AMP = 0.5
rr_reset_time = 30_000

READOUT_FLATTOP_AMP = READOUT_AMP
READOUT_FLATTOP_LEN = int(0.6 * READOUT_LEN)
READOUT_GAUSSIAN_RISE_FALL_AMP = READOUT_AMP
READOUT_GAUSSIAN_RISE_FALL_MAIN_LEN = int(0.2 * READOUT_LEN)
READOUT_GAUSSIAN_RISE_FALL_PAD_LEN = READOUT_GAUSSIAN_RISE_FALL_MAIN_LEN % 4
READOUT_GAUSSIAN_RISE_FALL_LEN = READOUT_GAUSSIAN_RISE_FALL_MAIN_LEN + READOUT_GAUSSIAN_RISE_FALL_PAD_LEN
# READOUT_GAUSSIAN_FLATTOP_TOTAL_LEN
READOUT_GAUSSIAN_FLATTOP_TOTAL_AMP = READOUT_FLATTOP_AMP
READOUT_GAUSSIAN_FLATTOP_TOTAL_LEN = 2 * READOUT_GAUSSIAN_RISE_FALL_LEN + READOUT_FLATTOP_LEN

assert READOUT_LEN == READOUT_GAUSSIAN_FLATTOP_TOTAL_LEN, "flattop readout pulse len does not match the len of readout pulse!!"
assert READOUT_GAUSSIAN_FLATTOP_TOTAL_LEN % 4 == 0, "flattop readout pulse len must be multiple of 4 ns!!"

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
            # "q8_rr",
        ],
        "TOF": 32,
        "con": "con1",
        "fem": 1,
        "ao": 1,
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
    "q8_rr": "q8_xy",
}
QUBIT_RR_MAP = {
    "q1_xy": "q1_rr",
    "q2_xy": "q2_rr",
    "q3_xy": "q3_rr",
    "q4_xy": "q4_rr",
    "q5_xy": "q5_rr",
    "q6_xy": "q6_rr",
    "q7_xy": "q7_rr",
    "q8_xy": "q8_rr",
}

RR_CONSTANTS = {
    "q1_rr": {
        # main
        "IF": -300 * u.MHz, 
        "amp": READOUT_AMP,
        "rotation_angle": 0.0,
        "ge_threshold": 0.0,
        "midcircuit_amplitude": 0.5,
        "midcircuit_rotation_angle": (0.0 / 180) * np.pi,
        "midcircuit_ge_threshold": 0.0,
        "gaussian_rise_flattop_fall_amp": READOUT_GAUSSIAN_FLATTOP_TOTAL_AMP,
        "gaussian_rise_flattop_fall_len": READOUT_GAUSSIAN_FLATTOP_TOTAL_LEN, 
        "flattop_amp": READOUT_FLATTOP_AMP,
        "flattop_len": READOUT_FLATTOP_LEN,
        # twin
        "gaussian_rise_fall_amp": READOUT_GAUSSIAN_RISE_FALL_AMP,
        "gaussian_rise_fall_len": READOUT_GAUSSIAN_RISE_FALL_LEN,
        "gaussian_rise_fall_pad_len": READOUT_GAUSSIAN_RISE_FALL_PAD_LEN,
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
        "IF": -300 * u.MHz, 
        "amp": READOUT_AMP,
        "rotation_angle": 0.0,
        "ge_threshold": 0.0,
        "midcircuit_amplitude": 0.5,
        "midcircuit_rotation_angle": (0.0 / 180) * np.pi,
        "midcircuit_ge_threshold": 0.0,
        "gaussian_rise_flattop_fall_amp": READOUT_GAUSSIAN_FLATTOP_TOTAL_AMP,
        "gaussian_rise_flattop_fall_len": READOUT_GAUSSIAN_FLATTOP_TOTAL_LEN, 
        "flattop_amp": READOUT_FLATTOP_AMP,
        "flattop_len": READOUT_FLATTOP_LEN,
        # twin
        "gaussian_rise_fall_amp": READOUT_GAUSSIAN_RISE_FALL_AMP,
        "gaussian_rise_fall_len": READOUT_GAUSSIAN_RISE_FALL_LEN,
        "gaussian_rise_fall_pad_len": READOUT_GAUSSIAN_RISE_FALL_PAD_LEN,
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
        "IF": -300 * u.MHz, 
        "amp": READOUT_AMP,
        "rotation_angle": 0.0,
        "ge_threshold": 0.0,
        "midcircuit_amplitude": 0.5,
        "midcircuit_rotation_angle": (0.0 / 180) * np.pi,
        "midcircuit_ge_threshold": 0.0,
        "gaussian_rise_flattop_fall_amp": READOUT_GAUSSIAN_FLATTOP_TOTAL_AMP,
        "gaussian_rise_flattop_fall_len": READOUT_GAUSSIAN_FLATTOP_TOTAL_LEN, 
        "flattop_amp": READOUT_FLATTOP_AMP,
        "flattop_len": READOUT_FLATTOP_LEN,
        # twin
        "gaussian_rise_fall_amp": READOUT_GAUSSIAN_RISE_FALL_AMP,
        "gaussian_rise_fall_len": READOUT_GAUSSIAN_RISE_FALL_LEN,
        "gaussian_rise_fall_pad_len": READOUT_GAUSSIAN_RISE_FALL_PAD_LEN,
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
        "IF": -300 * u.MHz, 
        "amp": READOUT_AMP,
        "rotation_angle": 0.0,
        "ge_threshold": 0.0,
        "midcircuit_amplitude": 0.5,
        "midcircuit_rotation_angle": (0.0 / 180) * np.pi,
        "midcircuit_ge_threshold": 0.0,
        "gaussian_rise_flattop_fall_amp": READOUT_GAUSSIAN_FLATTOP_TOTAL_AMP,
        "gaussian_rise_flattop_fall_len": READOUT_GAUSSIAN_FLATTOP_TOTAL_LEN, 
        "flattop_amp": READOUT_FLATTOP_AMP,
        "flattop_len": READOUT_FLATTOP_LEN,
        # twin
        "gaussian_rise_fall_amp": READOUT_GAUSSIAN_RISE_FALL_AMP,
        "gaussian_rise_fall_len": READOUT_GAUSSIAN_RISE_FALL_LEN,
        "gaussian_rise_fall_pad_len": READOUT_GAUSSIAN_RISE_FALL_PAD_LEN,
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
        "IF": -300 * u.MHz, 
        "amp": READOUT_AMP,
        "rotation_angle": 0.0,
        "ge_threshold": 0.0,
        "midcircuit_amplitude": 0.5,
        "midcircuit_rotation_angle": (0.0 / 180) * np.pi,
        "midcircuit_ge_threshold": 0.0,
        "gaussian_rise_flattop_fall_amp": READOUT_GAUSSIAN_FLATTOP_TOTAL_AMP,
        "gaussian_rise_flattop_fall_len": READOUT_GAUSSIAN_FLATTOP_TOTAL_LEN, 
        "flattop_amp": READOUT_FLATTOP_AMP,
        "flattop_len": READOUT_FLATTOP_LEN,
        # twin
        "gaussian_rise_fall_amp": READOUT_GAUSSIAN_RISE_FALL_AMP,
        "gaussian_rise_fall_len": READOUT_GAUSSIAN_RISE_FALL_LEN,
        "gaussian_rise_fall_pad_len": READOUT_GAUSSIAN_RISE_FALL_PAD_LEN,
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
        "IF": -300 * u.MHz, 
        "amp": READOUT_AMP,
        "rotation_angle": 0.0,
        "ge_threshold": 0.0,
        "midcircuit_amplitude": 0.5,
        "midcircuit_rotation_angle": (0.0 / 180) * np.pi,
        "midcircuit_ge_threshold": 0.0,
        "gaussian_rise_flattop_fall_amp": READOUT_GAUSSIAN_FLATTOP_TOTAL_AMP,
        "gaussian_rise_flattop_fall_len": READOUT_GAUSSIAN_FLATTOP_TOTAL_LEN, 
        "flattop_amp": READOUT_FLATTOP_AMP,
        "flattop_len": READOUT_FLATTOP_LEN,
        # twin
        "gaussian_rise_fall_amp": READOUT_GAUSSIAN_RISE_FALL_AMP,
        "gaussian_rise_fall_len": READOUT_GAUSSIAN_RISE_FALL_LEN,
        "gaussian_rise_fall_pad_len": READOUT_GAUSSIAN_RISE_FALL_PAD_LEN,
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
        "IF": -300 * u.MHz, 
        "amp": READOUT_AMP,
        "rotation_angle": 0.0,
        "ge_threshold": 0.0,
        "midcircuit_amplitude": 0.5,
        "midcircuit_rotation_angle": (0.0 / 180) * np.pi,
        "midcircuit_ge_threshold": 0.0,
        "gaussian_rise_flattop_fall_amp": READOUT_GAUSSIAN_FLATTOP_TOTAL_AMP,
        "gaussian_rise_flattop_fall_len": READOUT_GAUSSIAN_FLATTOP_TOTAL_LEN, 
        "flattop_amp": READOUT_FLATTOP_AMP,
        "flattop_len": READOUT_FLATTOP_LEN,
        # twin
        "gaussian_rise_fall_amp": READOUT_GAUSSIAN_RISE_FALL_AMP,
        "gaussian_rise_fall_len": READOUT_GAUSSIAN_RISE_FALL_LEN,
        "gaussian_rise_fall_pad_len": READOUT_GAUSSIAN_RISE_FALL_PAD_LEN,
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
    # "q8_rr": {
    #     # main
    #     "IF": -300 * u.MHz, 
    #     "amp": READOUT_AMP,
    #     "rotation_angle": 0.0,
    #     "ge_threshold": 0.0,
    #     "midcircuit_amplitude": 0.5,
    #     "midcircuit_rotation_angle": (0.0 / 180) * np.pi,
    #     "midcircuit_ge_threshold": 0.0,
    #     "gaussian_rise_flattop_fall_amp": READOUT_GAUSSIAN_FLATTOP_TOTAL_AMP,
    #     "gaussian_rise_flattop_fall_len": READOUT_GAUSSIAN_FLATTOP_TOTAL_LEN, 
    #     "flattop_amp": READOUT_FLATTOP_AMP,
    #     "flattop_len": READOUT_FLATTOP_LEN,
    #     # twin
    #     "gaussian_rise_fall_amp": READOUT_GAUSSIAN_RISE_FALL_AMP,
    #     "gaussian_rise_fall_len": READOUT_GAUSSIAN_RISE_FALL_LEN,
    #     "gaussian_rise_fall_pad_len": READOUT_GAUSSIAN_RISE_FALL_PAD_LEN,
    #     # common
    #     "TOF": RL_CONSTANTS["rl1"]["TOF"],
    #     "LO": RL_CONSTANTS["rl1"]["LO"],
    #     "con": RL_CONSTANTS["rl1"]["con"],
    #     "fem": RL_CONSTANTS["rl1"]["fem"],
    #     "ao": RL_CONSTANTS["rl1"]["ao"],
    #     "ai": RL_CONSTANTS["rl1"]["ai"],
    #     "delay": RL_CONSTANTS["rl1"]["delay"],
    #     "core": QUBIT_CONSTANTS[f"q4_xy"]["core"],
    # },
}

assert set(RR_CONSTANTS.keys()) == set([rr for rl, val in RL_CONSTANTS.items() for rr in val["RESONATORS"]]), "resonators in RL_CONSTANTS and RR_CONTANTS do not match!"

# for rr_key in RR_CONSTANTS.keys():
#     assert RR_CONSTANTS[rr_key]["amp"] <= 0.499, f"{rr_key} amplitude needs to be less than 0.499"

for rl in RL_CONSTANTS.keys():
    total_amp = 0
    for rr in RL_CONSTANTS[rl]["RESONATORS"]:
        total_amp += RR_CONSTANTS[rr]["amp"]
    # assert total_amp <= 0.499, f"the sum of {rl} resonators is larger than 0.499"
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
        "q8_rr": np.load(os.path.join(current_file_path, "optimal_weights_q8_rr.npz")),
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
                1: {
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
                                    # 2: {"frequency": QUBIT_CONSTANTS["q8_xy"]["LO"]},
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
                                    # 2: {"frequency": QUBIT_CONSTANTS["q8_xy"]["LO"]},
                                },
                            } for k, v in QUBIT_CONSTANTS.items()
                        }
                    },
                    "analog_inputs": {
                        **{
                            v["ai"]: {
                                "sampling_rate": 1e9,
                                "band": v["band"],
                            "gain_db": 10,
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
            'smearing': 0,
            "operations": {
                "const": "const_pulse",
                "readout": f"readout_pulse_{rr}",
                "flattop_readout": f"flattop_readout_pulse_{rr}",
                "midcircuit_readout": f"midcircuit_readout_pulse_{rr}",
                "gaussian_flattop_readout": f"gaussian_rise_flattop_fall_readout_pulse_{rr}"
            },
            "core": val["core"],
        } for rr, val in RR_CONSTANTS.items()},

        # readout line 1
        **{f"{rr}_twin": {
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
                "gaussian_rise_readout": f"gaussian_rise_readout_pulse_{rr}",
                "gaussian_fall_readout": f"gaussian_fall_readout_pulse_{rr}",
            },
            # "core": val["core-twin"],
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
            },
            "core": val["core"],
        } for qb, val in QUBIT_CONSTANTS.items()},

        # cr drives
        **{cr_drive: {
            "MWInput": {
                "port": (val["con"], val["fem"], val["ao"]),
                "upconverter": 1,
            },
            "intermediate_frequency": val["IF"],  # in Hz
            "operations": {
                "const": "const_pulse",
                "square_positive": f"square_positive_pulse_{cr_drive}",
                "square_negative": f"square_negative_pulse_{cr_drive}",
                "flattop_positive": f"flattop_positive_pulse_{cr_drive}",
                "flattop_negative": f"flattop_negative_pulse_{cr_drive}",
            },
            # "core": val["thread_main"],
        } for cr_drive, val in CR_DRIVE_CONSTANTS.items()},

        # cr cancel
        **{cr_cancel: {
            "MWInput": {
                "port": (val["con"], val["fem"], val["ao"]),
                "upconverter": 1,
            },
            "intermediate_frequency": val["IF"],  # in Hz
            "operations": {
                "const": "const_pulse",
                "square_positive": f"square_positive_pulse_{cr_cancel}",
                "square_negative": f"square_negative_pulse_{cr_cancel}",
                "flattop_positive": f"flattop_positive_pulse_{cr_cancel}",
                "flattop_negative": f"flattop_negative_pulse_{cr_cancel}",
            },
            # "core": val["thread_main"],
        } for cr_cancel, val in CR_CANCEL_CONSTANTS.items()},

        # cr drive twin
        **{f"{cr_drive}_twin": {
            "MWInput": {
                "port": (val["con"], val["fem"], val["ao"]),
                "upconverter": 1,
            },
            "intermediate_frequency": val["IF"],  # in Hz
            "operations": {
                "const": "const_pulse",
                "gaussian_rise_positive": f"gaussian_rise_positive_pulse_{cr_drive}",
                "gaussian_rise_negative": f"gaussian_rise_negative_pulse_{cr_drive}",
                "gaussian_rise_positive": f"gaussian_fall_positive_pulse_{cr_drive}",
                "gaussian_rise_negative": f"gaussian_fall_negative_pulse_{cr_drive}",
            },
            # "core": val["thread_twin"],
        } for cr_drive, val in CR_DRIVE_CONSTANTS.items()},

        # cr cancel twin
        **{f"{cr_cancel}_twin": {
            "MWInput": {
                "port": (val["con"], val["fem"], val["ao"]),
                "upconverter": 1,
            },
            "intermediate_frequency": val["IF"],  # in Hz
            "operations": {
                "const": "const_pulse",
                "gaussian_rise_positive": f"gaussian_rise_positive_pulse_{cr_cancel}",
                "gaussian_rise_negative": f"gaussian_rise_negative_pulse_{cr_cancel}",
                "gaussian_fall_positive": f"gaussian_fall_positive_pulse_{cr_cancel}",
                "gaussian_fall_negative": f"gaussian_fall_negative_pulse_{cr_cancel}",
            },
            # "core": val["thread_twin"],
        } for cr_cancel, val in CR_CANCEL_CONSTANTS.items()},
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
        **{f"square_positive_pulse_{cr_drive}":
            {
                "operation": "control",
                "length": val["square_positive_len"],
                "waveforms": {
                    "I": f"square_positive_wf_{cr_drive}",
                    "Q": f"zero_wf"
                }
            }
            for cr_drive, val in CR_DRIVE_CONSTANTS.items()
        },
        **{f"square_negative_pulse_{cr_drive}":
            {
                "operation": "control",
                "length": val["square_negative_len"],
                "waveforms": {
                    "I": f"square_negative_wf_{cr_drive}",
                    "Q": f"zero_wf"
                }
            }
            for cr_drive, val in CR_DRIVE_CONSTANTS.items()
        },
        **{f"square_positive_pulse_{cr_cancel}":
            {
                "operation": "control",
                "length": val["square_positive_len"],
                "waveforms": {
                    "I": f"square_positive_wf_{cr_cancel}",
                    "Q": f"zero_wf"
                }
            }
            for cr_cancel, val in CR_CANCEL_CONSTANTS.items()
        },
        **{f"square_negative_pulse_{cr_cancel}":
            {
                "operation": "control",
                "length": val["square_negative_len"],
                "waveforms": {
                    "I": f"square_negative_wf_{cr_cancel}",
                    "Q": f"zero_wf"
                }
            }
            for cr_cancel, val in CR_CANCEL_CONSTANTS.items()
        },
        **{f"flattop_positive_pulse_{cr_drive}":
            {
                "operation": "control",
                "length": val["flattop_positive_len"],
                "waveforms": {
                    "I": f"flattop_positive_wf_{cr_drive}",
                    "Q": f"zero_wf"
                }
            }
            for cr_drive, val in CR_DRIVE_CONSTANTS.items()
        },
        **{f"flattop_negative_pulse_{cr_drive}":
            {
                "operation": "control",
                "length": val["flattop_negative_len"],
                "waveforms": {
                    "I": f"flattop_negative_wf_{cr_drive}",
                    "Q": f"zero_wf"
                }
            }
            for cr_drive, val in CR_DRIVE_CONSTANTS.items()
        },
        **{f"flattop_positive_pulse_{cr_cancel}":
            {
                "operation": "control",
                "length": val["flattop_positive_len"],
                "waveforms": {
                    "I": f"flattop_positive_wf_{cr_cancel}",
                    "Q": f"zero_wf"
                }
            }
            for cr_cancel, val in CR_CANCEL_CONSTANTS.items()
        },
        **{f"flattop_negative_pulse_{cr_cancel}":
            {
                "operation": "control",
                "length": val["flattop_negative_len"],
                "waveforms": {
                    "I": f"flattop_negative_wf_{cr_cancel}",
                    "Q": f"zero_wf"
                }
            }
            for cr_cancel, val in CR_CANCEL_CONSTANTS.items()
        },
        **{f"gaussian_rise_positive_pulse_{cr_drive}":
            {
                "operation": "control",
                "length": val["gaussian_rise_positive_len"] + val["gaussian_rise_positive_pad_len"],
                "waveforms": {
                    "I": f"gaussian_rise_positive_wf_{cr_drive}",
                    "Q": f"zero_wf"
                }
            }
            for cr_drive, val in CR_DRIVE_CONSTANTS.items()
        },
        **{f"gaussian_rise_negative_pulse_{cr_drive}":
            {
                "operation": "control",
                "length": val["gaussian_rise_negative_len"] + val["gaussian_rise_negative_pad_len"],
                "waveforms": {
                    "I": f"gaussian_rise_negative_wf_{cr_drive}",
                    "Q": f"zero_wf"
                }
            }
            for cr_drive, val in CR_DRIVE_CONSTANTS.items()
        },
        **{f"gaussian_rise_positive_pulse_{cr_cancel}":
            {
                "operation": "control",
                "length": val["gaussian_rise_positive_len"] + val["gaussian_rise_negative_pad_len"],
                "waveforms": {
                    "I": f"gaussian_rise_positive_wf_{cr_cancel}",
                    "Q": f"zero_wf"
                }
            }
            for cr_cancel, val in CR_CANCEL_CONSTANTS.items()
        },
        **{f"gaussian_rise_negative_pulse_{cr_cancel}":
            {
                "operation": "control",
                "length": val["gaussian_rise_negative_len"] + val["gaussian_rise_negative_pad_len"],
                "waveforms": {
                    "I": f"gaussian_rise_negative_wf_{cr_cancel}",
                    "Q": f"zero_wf"
                }
            }
            for cr_cancel, val in CR_CANCEL_CONSTANTS.items()
        },
        **{f"gaussian_fall_positive_pulse_{cr_drive}":
            {
                "operation": "control",
                "length": val["gaussian_fall_positive_len"] + val["gaussian_rise_negative_pad_len"],
                "waveforms": {
                    "I": f"gaussian_fall_positive_wf_{cr_drive}",
                    "Q": f"zero_wf"
                }
            }
            for cr_drive, val in CR_DRIVE_CONSTANTS.items()
        },
        **{f"gaussian_fall_negative_pulse_{cr_drive}":
            {
                "operation": "control",
                "length": val["gaussian_fall_negative_len"] + val["gaussian_fall_negative_pad_len"],
                "waveforms": {
                    "I": f"gaussian_fall_negative_wf_{cr_drive}",
                    "Q": f"zero_wf"
                }
            }
            for cr_drive, val in CR_DRIVE_CONSTANTS.items()
        },
        **{f"gaussian_fall_positive_pulse_{cr_cancel}":
            {
                "operation": "control",
                "length": val["gaussian_fall_positive_len"] + val["gaussian_fall_positive_pad_len"],
                "waveforms": {
                    "I": f"gaussian_fall_positive_wf_{cr_cancel}",
                    "Q": f"zero_wf"
                }
            }
            for cr_cancel, val in CR_CANCEL_CONSTANTS.items()
        },
        **{f"gaussian_fall_negative_pulse_{cr_cancel}":
            {
                "operation": "control",
                "length": val["gaussian_fall_negative_len"] + val["gaussian_fall_negative_pad_len"],
                "waveforms": {
                    "I": f"gaussian_fall_negative_wf_{cr_cancel}",
                    "Q": f"zero_wf"
                }
            }
            for cr_cancel, val in CR_CANCEL_CONSTANTS.items()
        },
        **{f"gaussian_rise_flattop_fall_positive_pulse_{cr_drive}":
           {
                "operation": "control",
                "length": val["gaussian_rise_flattop_fall_positive_len"],
                "waveforms": {
                    "I": f"gaussian_rise_flattop_fall_positive_wf_{cr_drive}",
                    "Q": "zero_wf"
                },
            }
           \
            for cr_drive, val in CR_DRIVE_CONSTANTS.items()
        },
        **{f"gaussian_rise_flattop_fall_negative_pulse_{cr_drive}":
           {
                "operation": "control",
                "length": val["gaussian_rise_flattop_fall_negative_len"],
                "waveforms": {
                    "I": f"gaussian_rise_flattop_fall_negative_wf_{cr_drive}",
                    "Q": "zero_wf"
                },
            }
            for cr_drive, val in CR_DRIVE_CONSTANTS.items()
        },
        **{f"gaussian_rise_flattop_fall_positive_pulse_{cr_cancel}":
           {
                "operation": "control",
                "length": val["gaussian_rise_flattop_fall_positive_len"],
                "waveforms": {
                    "I": f"gaussian_rise_flattop_fall_positive_wf_{cr_cancel}",
                    "Q": "zero_wf"
                },
            }
            for cr_cancel, val in CR_CANCEL_CONSTANTS.items()
        },
        **{f"gaussian_rise_flattop_fall_negative_pulse_{cr_cancel}":
           {
                "operation": "control",
                "length": val["gaussian_rise_flattop_fall_negative_len"],
                "waveforms": {
                    "I": f"gaussian_rise_flattop_fall_negative_wf_{cr_cancel}",
                    "Q": "zero_wf"
                },
            }
            for cr_cancel, val in CR_CANCEL_CONSTANTS.items()
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
        **{
            f"midcircuit_readout_pulse_{rr}": {
                "operation": "measurement",
                "length": READOUT_LEN,
                "waveforms": {
                    "I": f"midcircuit_readout_wf_{rr}",
                    "Q": "zero_wf"
                },
                "integration_weights": {
                    "cos": "cosine_weights",
                    "sin": "sine_weights",
                    "minus_sin": "minus_sine_weights",
                    "rotated_cos": f"midcircuit_rotated_cosine_weights_{rr}",
                    "rotated_sin": f"midcircuit_rotated_sine_weights_{rr}",
                    "rotated_minus_sin": f"midcircuit_rotated_minus_sine_weights_{rr}",
                    "opt_cos": f"midcircuit_opt_cosine_weights_{rr}",
                    "opt_sin": f"midcircuit_opt_sine_weights_{rr}",
                    "opt_minus_sin": f"midcircuit_opt_minus_sine_weights_{rr}",
                },
                "digital_marker": "ON",
            } for rr in RR_CONSTANTS.keys()
        },
        **{
            f"gaussian_rise_flattop_fall_readout_pulse_{rr}": {
                "operation": "measurement",
                "length": READOUT_LEN,
                "waveforms": {
                    "I": f"gaussian_rise_flattop_fall_readout_wf_{rr}",
                    "Q": "zero_wf"
                },
                "integration_weights": {
                    "cos": f"gaussian_rise_flattop_fall_cosine_weights_{rr}",
                    "sin": f"gaussian_rise_flattop_fall_sine_weights_{rr}",
                    "minus_sin": f"gaussian_rise_flattop_fall_minus_sine_weights_{rr}",
                },
                "digital_marker": "ON",
            } for rr in RR_CONSTANTS.keys()
        },
        **{
            f"flattop_readout_pulse_{rr}": {
                "operation": "measurement",
                "length": READOUT_FLATTOP_LEN,
                "waveforms": {
                    "I": f"flattop_readout_wf_{rr}",
                    "Q": "zero_wf"
                },
                "integration_weights": {
                    "cos": f"flattop_cosine_weights_{rr}",
                    "sin": f"flattop_sine_weights_{rr}",
                    "minus_sin": f"flattop_minus_sine_weights_{rr}",
                },
                "digital_marker": "ON",
            } for rr in RR_CONSTANTS.keys()
        },
        **{
            f"gaussian_rise_readout_pulse_{rr}": {
                "operation": "measurement",
                "length": READOUT_GAUSSIAN_RISE_FALL_LEN,
                "waveforms": {
                    "I": f"gaussian_rise_readout_wf_{rr}",
                    "Q": "zero_wf"
                },
                "integration_weights": {
                    "cos": f"gaussian_rise_cosine_weights_{rr}",
                    "sin": f"gaussian_rise_sine_weights_{rr}",
                    "minus_sin": f"gaussian_rise_minus_sine_weights_{rr}",
                },
                "digital_marker": "ON",
            } for rr in RR_CONSTANTS.keys()
        },
        **{
            f"gaussian_fall_readout_pulse_{rr}": {
                "operation": "measurement",
                "length": READOUT_GAUSSIAN_RISE_FALL_LEN,
                "waveforms": {
                    "I": f"gaussian_fall_readout_wf_{rr}",
                    "Q": "zero_wf"
                },
                "integration_weights": {
                    "cos": f"gaussian_fall_cosine_weights_{rr}",
                    "sin": f"gaussian_fall_sine_weights_{rr}",
                    "minus_sin": f"gaussian_fall_minus_sine_weights_{rr}",
                },
                "digital_marker": "ON",
            } for rr in RR_CONSTANTS.keys()
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
        **{f"square_positive_wf_{key}": {"type": "constant", "sample": val["square_positive_amp"]} for key, val in CR_DRIVE_CONSTANTS.items()},
        **{f"square_negative_wf_{key}": {"type": "constant", "sample": val["square_negative_amp"]} for key, val in CR_DRIVE_CONSTANTS.items()},
        **{f"square_positive_wf_{key}": {"type": "constant", "sample": val["square_positive_amp"]} for key, val in CR_CANCEL_CONSTANTS.items()},
        **{f"square_negative_wf_{key}": {"type": "constant", "sample": val["square_negative_amp"]} for key, val in CR_CANCEL_CONSTANTS.items()},
        **{f"flattop_positive_wf_{key}": {"type": "constant", "sample": val["flattop_positive_amp"]} for key, val in CR_DRIVE_CONSTANTS.items()},
        **{f"flattop_negative_wf_{key}": {"type": "constant", "sample": val["flattop_negative_amp"]} for key, val in CR_DRIVE_CONSTANTS.items()},
        **{f"flattop_positive_wf_{key}": {"type": "constant", "sample": val["flattop_positive_amp"]} for key, val in CR_CANCEL_CONSTANTS.items()},
        **{f"flattop_negative_wf_{key}": {"type": "constant", "sample": val["flattop_negative_amp"]} for key, val in CR_CANCEL_CONSTANTS.items()},
        **{f"gaussian_rise_positive_wf_{key}": {"type": "arbitrary", "samples": [0] * val["gaussian_rise_positive_pad_len"] + flattop_gaussian_waveform(val["gaussian_rise_positive_amp"], val["flattop_positive_len"], val["gaussian_rise_positive_len"], return_part="rise")} for key, val in CR_DRIVE_CONSTANTS.items()},
        **{f"gaussian_rise_negative_wf_{key}": {"type": "arbitrary", "samples": [0] * val["gaussian_rise_negative_pad_len"] + flattop_gaussian_waveform(val["gaussian_rise_negative_amp"], val["flattop_positive_len"], val["gaussian_rise_negative_len"], return_part="rise")} for key, val in CR_DRIVE_CONSTANTS.items()},
        **{f"gaussian_rise_positive_wf_{key}": {"type": "arbitrary", "samples": [0] * val["gaussian_rise_positive_pad_len"] + flattop_gaussian_waveform(val["gaussian_rise_positive_amp"], val["flattop_positive_len"], val["gaussian_rise_positive_len"], return_part="rise")} for key, val in CR_CANCEL_CONSTANTS.items()},
        **{f"gaussian_rise_negative_wf_{key}": {"type": "arbitrary", "samples": [0] * val["gaussian_rise_negative_pad_len"] + flattop_gaussian_waveform(val["gaussian_rise_negative_amp"], val["flattop_positive_len"], val["gaussian_rise_negative_len"], return_part="rise")} for key, val in CR_CANCEL_CONSTANTS.items()},
        **{f"gaussian_fall_positive_wf_{key}": {"type": "arbitrary", "samples": flattop_gaussian_waveform(val["gaussian_fall_positive_amp"], val["flattop_positive_len"], val["gaussian_fall_positive_len"], return_part="fall") + [0] * val["gaussian_fall_positive_pad_len"]} for key, val in CR_DRIVE_CONSTANTS.items()},
        **{f"gaussian_fall_negative_wf_{key}": {"type": "arbitrary", "samples": flattop_gaussian_waveform(val["gaussian_fall_negative_amp"], val["flattop_positive_len"], val["gaussian_fall_negative_len"], return_part="fall") + [0] * val["gaussian_fall_negative_pad_len"]} for key, val in CR_DRIVE_CONSTANTS.items()},
        **{f"gaussian_fall_positive_wf_{key}": {"type": "arbitrary", "samples": flattop_gaussian_waveform(val["gaussian_fall_positive_amp"], val["flattop_positive_len"], val["gaussian_fall_positive_len"], return_part="fall") + [0] * val["gaussian_fall_positive_pad_len"]} for key, val in CR_CANCEL_CONSTANTS.items()},
        **{f"gaussian_fall_negative_wf_{key}": {"type": "arbitrary", "samples": flattop_gaussian_waveform(val["gaussian_fall_negative_amp"], val["flattop_positive_len"], val["gaussian_fall_negative_len"], return_part="fall") + [0] * val["gaussian_fall_negative_pad_len"]} for key, val in CR_CANCEL_CONSTANTS.items()},
        **{f"gaussian_rise_flattop_fall_positive_wf_{key}": {"type": "arbitrary", "samples": [0] * val["gaussian_rise_fall_positive_pad_len"] + flattop_gaussian_waveform(val["gaussian_rise_flattop_fall_positive_amp"], val["flattop_positive_len"], val["gaussian_rise_fall_positive_len"], return_part="all") + [0] * val["gaussian_rise_fall_positive_pad_len"]} for key, val in CR_DRIVE_CONSTANTS.items()},
        **{f"gaussian_rise_flattop_fall_negative_wf_{key}": {"type": "arbitrary", "samples": [0] * val["gaussian_rise_fall_negative_pad_len"] + flattop_gaussian_waveform(val["gaussian_rise_flattop_fall_negative_amp"], val["flattop_positive_len"], val["gaussian_rise_fall_negative_len"], return_part="all") + [0] * val["gaussian_rise_fall_negative_pad_len"]} for key, val in CR_DRIVE_CONSTANTS.items()},
        **{f"gaussian_rise_flattop_fall_positive_wf_{key}": {"type": "arbitrary", "samples": [0] * val["gaussian_rise_fall_positive_pad_len"] + flattop_gaussian_waveform(val["gaussian_rise_flattop_fall_positive_amp"], val["flattop_positive_len"], val["gaussian_rise_fall_positive_len"], return_part="all") + [0] * val["gaussian_rise_fall_positive_pad_len"]} for key, val in CR_CANCEL_CONSTANTS.items()},
        **{f"gaussian_rise_flattop_fall_negative_wf_{key}": {"type": "arbitrary", "samples": [0] * val["gaussian_rise_fall_negative_pad_len"] + flattop_gaussian_waveform(val["gaussian_rise_flattop_fall_negative_amp"], val["flattop_positive_len"], val["gaussian_rise_fall_negative_len"], return_part="all") + [0] * val["gaussian_rise_fall_negative_pad_len"]} for key, val in CR_CANCEL_CONSTANTS.items()},
        **{f"readout_wf_{key}": {"type": "constant", "sample": val["amp"]} for key, val in RR_CONSTANTS.items()},
        **{f"midcircuit_readout_wf_{key}": {"type": "constant", "sample": val["midcircuit_amplitude"]} for key, val in RR_CONSTANTS.items()},
        **{f"flattop_readout_wf_{key}": {"type": "constant", "sample": val["amp"]} for key, val in RR_CONSTANTS.items()},
        **{f"gaussian_rise_readout_wf_{key}": {"type": "arbitrary", "samples": [0] * val["gaussian_rise_fall_pad_len"] + flattop_gaussian_waveform(val["gaussian_rise_fall_amp"], val["flattop_len"], val["gaussian_rise_fall_len"], return_part="rise")} for key, val in RR_CONSTANTS.items()},
        **{f"gaussian_fall_readout_wf_{key}": {"type": "arbitrary", "samples": flattop_gaussian_waveform(val["gaussian_rise_fall_amp"], val["flattop_len"], val["gaussian_rise_fall_len"], return_part="fall") + [0] * val["gaussian_rise_fall_pad_len"]} for key, val in RR_CONSTANTS.items()},
        **{f"gaussian_rise_flattop_fall_readout_wf_{key}": {"type": "arbitrary", "samples": [0] * val["gaussian_rise_fall_pad_len"] + flattop_gaussian_waveform(val["gaussian_rise_flattop_fall_amp"], val["flattop_len"], val["gaussian_rise_fall_len"], return_part="all") + [0] * val["gaussian_rise_fall_pad_len"]} for key, val in RR_CONSTANTS.items()},
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
        **{
            f"midcircuit_rotated_cosine_weights_{rr}": {
                "cosine": [(np.cos(RR_CONSTANTS[rr]["midcircuit_rotation_angle"])), READOUT_LEN],
                "sine": [(np.sin(RR_CONSTANTS[rr]["midcircuit_rotation_angle"])), READOUT_LEN]
            } for rr in RR_CONSTANTS.keys()
        },
        **{
            f"midcircuit_rotated_sine_weights_{rr}": {
                "cosine": [(-np.sin(RR_CONSTANTS[rr]["midcircuit_rotation_angle"])), READOUT_LEN],
                "sine": [(np.cos(RR_CONSTANTS[rr]["midcircuit_rotation_angle"])), READOUT_LEN]
            } for rr in RR_CONSTANTS.keys()
        },
        **{
            f"midcircuit_rotated_minus_sine_weights_{rr}": {
                "cosine": [(np.sin(RR_CONSTANTS[rr]["midcircuit_rotation_angle"])), READOUT_LEN],
                "sine": [(-np.cos(RR_CONSTANTS[rr]["midcircuit_rotation_angle"])), READOUT_LEN]
            } for rr in RR_CONSTANTS.keys()
        },
        **{
            f"midcircuit_opt_cosine_weights_{rr}": {
                "cosine": OPT_WEIGHTS[rr]['real'],
                "sine": OPT_WEIGHTS[rr]['minus_imag']
            } for rr in RR_CONSTANTS.keys()
        },
        **{
            f"midcircuit_opt_sine_weights_{rr}": {
                "cosine": OPT_WEIGHTS[rr]['imag'],
                "sine": OPT_WEIGHTS[rr]['real']
            } for rr in RR_CONSTANTS.keys()
        },
        **{
            f"midcircuit_opt_minus_sine_weights_{rr}": {
                "cosine": OPT_WEIGHTS[rr]['minus_imag'],
                "sine": OPT_WEIGHTS[rr]['minus_real']
            } for rr in RR_CONSTANTS.keys()
        },
        **{
            f"gaussian_rise_cosine_weights_{rr}": {
                "cosine": [(1.0, READOUT_GAUSSIAN_RISE_FALL_LEN)],
                "sine": [(0.0, READOUT_GAUSSIAN_RISE_FALL_LEN)],
            } for rr in RR_CONSTANTS.keys()
        },
        **{
            f"gaussian_rise_sine_weights_{rr}": {
                "cosine": [(0.0, READOUT_GAUSSIAN_RISE_FALL_LEN)],
                "sine": [(1.0, READOUT_GAUSSIAN_RISE_FALL_LEN)],
            } for rr in RR_CONSTANTS.keys()
        },
        **{
            f"gaussian_rise_minus_sine_weights_{rr}": {
                "cosine": [(0.0, READOUT_GAUSSIAN_RISE_FALL_LEN)],
                "sine": [(-1.0, READOUT_GAUSSIAN_RISE_FALL_LEN)],
            } for rr in RR_CONSTANTS.keys()
        },
        **{
            f"gaussian_fall_cosine_weights_{rr}": {
                "cosine": [(1.0, READOUT_GAUSSIAN_RISE_FALL_LEN)],
                "sine": [(0.0, READOUT_GAUSSIAN_RISE_FALL_LEN)],
            } for rr in RR_CONSTANTS.keys()
        },
        **{
            f"gaussian_fall_sine_weights_{rr}": {
                "cosine": [(0.0, READOUT_GAUSSIAN_RISE_FALL_LEN)],
                "sine": [(1.0, READOUT_GAUSSIAN_RISE_FALL_LEN)],
            } for rr in RR_CONSTANTS.keys()
        },
        **{
            f"gaussian_fall_minus_sine_weights_{rr}": {
                "cosine": [(0.0, READOUT_GAUSSIAN_RISE_FALL_LEN)],
                "sine": [(-1.0, READOUT_GAUSSIAN_RISE_FALL_LEN)],
            } for rr in RR_CONSTANTS.keys()
        },
        **{
            f"flattop_cosine_weights_{rr}": {
                "cosine": [(1.0, READOUT_FLATTOP_LEN)],
                "sine": [(0.0, READOUT_FLATTOP_LEN)],
            } for rr in RR_CONSTANTS.keys()
        },
        **{
            f"flattop_sine_weights_{rr}": {
                "cosine": [(0.0, READOUT_FLATTOP_LEN)],
                "sine": [(1.0, READOUT_FLATTOP_LEN)],
            } for rr in RR_CONSTANTS.keys()
        },
        **{
            f"flattop_minus_sine_weights_{rr}": {
                "cosine": [(0.0, READOUT_FLATTOP_LEN)],
                "sine": [(-1.0, READOUT_FLATTOP_LEN)],
            } for rr in RR_CONSTANTS.keys()
        },
        **{
            f"gaussian_rise_flattop_fall_cosine_weights_{rr}": {
                "cosine": [(1.0, READOUT_LEN)],
                "sine": [(0.0, READOUT_LEN)],
            } for rr in RR_CONSTANTS.keys()
        },
        **{
            f"gaussian_rise_flattop_fall_sine_weights_{rr}": {
                "cosine": [(0.0, READOUT_LEN)],
                "sine": [(1.0, READOUT_LEN)],
            } for rr in RR_CONSTANTS.keys()
        },
        **{
            f"gaussian_rise_flattop_fall_minus_sine_weights_{rr}": {
                "cosine": [(0.0, READOUT_LEN)],
                "sine": [(-1.0, READOUT_LEN)],
            } for rr in RR_CONSTANTS.keys()
        },
    },
}

# %%