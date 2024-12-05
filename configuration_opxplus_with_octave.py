# %%

import os
from pathlib import Path
import numpy as np
from qualang_tools.config.waveform_tools import drag_gaussian_pulse_waveforms, flattop_gaussian_waveform
from qualang_tools.units import unit


#######################
# AUXILIARY FUNCTIONS #
#######################
u = unit(coerce_to_integer=True)

#####################
# OPX configuration #
#####################
con = "con1"

# MARK: QUBITS
#############################################
#                  Qubits                   #
#############################################
# CW pulse parameter
CONST_LEN = 1000
CONST_AMP = 0.125

# PORT DELAYS
delays = {
    "rl1": 0,
    "q1_xy": 0,
    "q2_xy": 0,
    "q3_xy": 0,
    "q4_xy": 0,
}

# Relaxation time
qb_reset_time = 50_000
depletion_time = 50_000

# Saturation_pulse
SATURATION_LEN = 30 * u.us
SATURATION_AMP = 0.45

PI_LEN = 48
PI_SIGMA = PI_LEN / 5

QUBIT_CONSTANTS = {
    "q1_xy": {
        "amp": 0.125,
        "pi_len": PI_LEN,
        "pi_sigma": PI_SIGMA,
        "anharmonicity": -200 * u.MHz,
        "drag_coefficient": 0.5,
        "ac_stark_shift": 0.0 * u.MHz,
        "LO": 3.100 * u.GHz,
        "IF": 0 * u.MHz,
        "con": "con1",
        "ao_I": 3,
        "ao_Q": 4,
        "rf_in": 2,
        "delay": delays["q1_xy"],
        "thread": "fem1-thread1",
    },
    "q2_xy": {
        "amp": 0.125,
        "pi_len": PI_LEN,
        "pi_sigma": PI_SIGMA, 
        "anharmonicity": -180 * u.MHz,
        "drag_coefficient": 0.5,
        "ac_stark_shift": 0.0 * u.MHz,
        "LO": 3.100 * u.GHz,  
        "IF": -50 * u.MHz,
        "con": "con1",
        "ao_I": 5,
        "ao_Q": 6,
        "rf_in": 3,
        "delay": delays["q2_xy"],
        "thread": "fem1-thread2",
    },
    "q3_xy": {
        "amp": 0.125,
        "pi_len": PI_LEN,
        "pi_sigma": PI_SIGMA, 
        "anharmonicity": -190 * u.MHz,
        "drag_coefficient": 0.5,
        "ac_stark_shift": 0.0 * u.MHz,
        "LO": 3.100 * u.GHz,  
        "IF": -100 * u.MHz,
        "con": "con1",
        "ao_I": 7,
        "ao_Q": 8,
        "rf_in": 4,
        "delay": delays["q3_xy"],
        "thread": "fem1-thread3",
    },
    "q4_xy": {
        "amp": 0.125,
        "pi_len": PI_LEN,
        "pi_sigma": PI_SIGMA, 
        "anharmonicity": -185 * u.MHz,
        "drag_coefficient": 0.5,
        "ac_stark_shift": 0.0 * u.MHz,
        "LO": 3.100 * u.GHz,  
        "IF": -150 * u.MHz,
        "con": "con1",
        "ao_I": 9,
        "ao_Q": 10,
        "rf_in": 5,
        "delay": delays["q4_xy"],
        "thread": "fem1-thread4",
    },
}

for qubit in QUBIT_CONSTANTS.keys():
    assert QUBIT_CONSTANTS[qubit]["amp"] <= 0.499, f"{qubit} amplitude needs to be less than 0.499"


def generate_waveforms(rotation_keys):
    """ Generate all necessary waveforms for a set of rotation types across all qubits. """
    
    if not isinstance(rotation_keys, list):
        raise ValueError("rotation_keys must be a list")

    waveforms = {}

    for qubit, constants in QUBIT_CONSTANTS.items():
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

            if rotation_key in ["x180", "x90", "minus_x90"]:
                I_wf = wf
                Q_wf = der_wf
            elif rotation_key in ["y180", "y90", "minus_y90"]:
                I_wf = (-1) * der_wf
                Q_wf = wf
            else:
                raise ValueError(
                    f'{rotation_key} is passed. rotation_key must be one of ["x180", "x90", "minus_x90", "y180", "y90", "minus_y90"]'
                )

            waveforms[f"{qubit}_{rotation_key}_I"] = I_wf
            waveforms[f"{qubit}_{rotation_key}_Q"] = Q_wf

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
]

CR_DRIVE_SQUARE_AMP = 0.2
CR_DRIVE_SQUARE_LEN = 120
CR_DRIVE_FLATTOP_AMP = 0.2
CR_DRIVE_FLATTOP_LEN = 100
CR_DRIVE_GAUSSIAN_RISE_AMP = CR_DRIVE_FLATTOP_AMP
CR_DRIVE_GAUSSIAN_RISE_LEN = 20
CR_DRIVE_GAUSSIAN_RISE_PAD_LEN = CR_DRIVE_GAUSSIAN_RISE_LEN % 4
CR_DRIVE_GAUSSIAN_FALL_AMP = CR_DRIVE_FLATTOP_AMP
CR_DRIVE_GAUSSIAN_FALL_LEN = CR_DRIVE_GAUSSIAN_RISE_LEN
CR_DRIVE_GAUSSIAN_FALL_PAD_LEN = CR_DRIVE_GAUSSIAN_FALL_LEN % 4

CR_CANCEL_SQUARE_AMP = CR_DRIVE_SQUARE_AMP
CR_CANCEL_SQUARE_LEN = CR_DRIVE_SQUARE_LEN
CR_CANCEL_FLATTOP_AMP = CR_DRIVE_FLATTOP_AMP
CR_CANCEL_FLATTOP_LEN = CR_DRIVE_FLATTOP_LEN
CR_CANCEL_GAUSSIAN_RISE_AMP = CR_DRIVE_FLATTOP_AMP
CR_CANCEL_GAUSSIAN_RISE_LEN = CR_DRIVE_GAUSSIAN_RISE_LEN
CR_CANCEL_GAUSSIAN_RISE_PAD_LEN = CR_DRIVE_GAUSSIAN_RISE_LEN % 4
CR_CANCEL_GAUSSIAN_FALL_AMP = CR_DRIVE_FLATTOP_AMP
CR_CANCEL_GAUSSIAN_FALL_LEN = CR_DRIVE_GAUSSIAN_RISE_LEN
CR_CANCEL_GAUSSIAN_FALL_PAD_LEN = CR_DRIVE_GAUSSIAN_FALL_LEN % 4

assert (CR_DRIVE_GAUSSIAN_RISE_LEN + CR_DRIVE_GAUSSIAN_RISE_PAD_LEN) % 4 == 0, "duration of padded gaussian rise / fall len must be integer multiple of 4 ns"
assert (CR_DRIVE_GAUSSIAN_FALL_LEN + CR_DRIVE_GAUSSIAN_FALL_PAD_LEN) % 4 == 0, "duration of padded gaussian rise / fall len must be integer multiple of 4 ns"
assert (CR_CANCEL_GAUSSIAN_RISE_LEN + CR_CANCEL_GAUSSIAN_RISE_PAD_LEN) % 4 == 0, "duration of padded gaussian rise / fall len must be integer multiple of 4 ns"
assert (CR_CANCEL_GAUSSIAN_FALL_LEN + CR_CANCEL_GAUSSIAN_FALL_PAD_LEN) % 4 == 0, "duration of padded gaussian rise / fall len must be integer multiple of 4 ns"


# Constants for each qubit for CR DRIVE
CR_DRIVE_CONSTANTS = {
    **{f"cr_drive_c{c}t{t}": {
        # main
        "square_positive_amp": CR_DRIVE_SQUARE_AMP,
        "square_positive_len": CR_DRIVE_SQUARE_LEN,
        "flattop_positive_amp": CR_DRIVE_FLATTOP_AMP,
        "flattop_positive_len": CR_DRIVE_FLATTOP_LEN,
        "square_negative_amp": -CR_DRIVE_SQUARE_AMP,
        "square_negative_len": CR_DRIVE_SQUARE_LEN,
        "flattop_negative_amp": -CR_DRIVE_FLATTOP_AMP,
        "flattop_negative_len": CR_DRIVE_FLATTOP_LEN,
        # twin
        "gaussian_rise_positive_amp": CR_DRIVE_GAUSSIAN_RISE_AMP,
        "gaussian_rise_positive_len": CR_DRIVE_GAUSSIAN_RISE_LEN,
        "gaussian_rise_positive_pad_len": CR_DRIVE_GAUSSIAN_RISE_PAD_LEN,
        "gaussian_fall_positive_amp": CR_DRIVE_GAUSSIAN_FALL_AMP,
        "gaussian_fall_positive_len": CR_DRIVE_GAUSSIAN_FALL_LEN,
        "gaussian_fall_positive_pad_len": CR_DRIVE_GAUSSIAN_FALL_PAD_LEN,
        "gaussian_rise_negative_amp": -CR_DRIVE_GAUSSIAN_RISE_AMP,
        "gaussian_rise_negative_len": CR_DRIVE_GAUSSIAN_RISE_LEN,
        "gaussian_rise_negative_pad_len": CR_DRIVE_GAUSSIAN_RISE_PAD_LEN,
        "gaussian_fall_negative_amp": -CR_DRIVE_GAUSSIAN_FALL_AMP,
        "gaussian_fall_negative_len": CR_DRIVE_GAUSSIAN_FALL_LEN,
        "gaussian_fall_negative_pad_len": CR_DRIVE_GAUSSIAN_FALL_PAD_LEN,
        # common
        "LO": QUBIT_CONSTANTS[f"q{t}_xy"]["LO"],
        "IF": QUBIT_CONSTANTS[f"q{t}_xy"]["IF"],
        "con": QUBIT_CONSTANTS[f"q{c}_xy"]["con"],
        "ao_I": QUBIT_CONSTANTS[f"q{c}_xy"]["ao_I"],
        "ao_Q": QUBIT_CONSTANTS[f"q{c}_xy"]["ao_Q"],
        "rf_in": QUBIT_CONSTANTS[f"q{c}_xy"]["rf_in"],
        "delay": QUBIT_CONSTANTS[f"q{c}_xy"]["delay"],
        "thread_main": None,
        "thread_twin": None,
    } for c, t in qubit_pairs}
}
# update after finidng the optimal parameters for amplitude and cr_square_len for each pair
# CR_DRIVE_CONSTANTS["cr_drive_c1t2"].update({"square_positive_amp": CR_DRIVE_SQUARE_AMP, "square_positive_len": CR_DRIVE_SQUARE_LEN, "flattop_amp": CR_DRIVE_FLATTOP_AMP, "flattop_len": CR_DRIVE_FLATTOP_LEN})
# CR_DRIVE_CONSTANTS["cr_drive_c2t1"].update({"square_positive_amp": CR_DRIVE_SQUARE_AMP, "square_positive_len": CR_DRIVE_SQUARE_LEN, "flattop_amp": CR_DRIVE_FLATTOP_AMP, "flattop_len": CR_DRIVE_FLATTOP_LEN})
# CR_DRIVE_CONSTANTS["cr_drive_c2t3"].update({"square_positive_amp": CR_DRIVE_SQUARE_AMP, "square_positive_len": CR_DRIVE_SQUARE_LEN, "flattop_amp": CR_DRIVE_FLATTOP_AMP, "flattop_len": CR_DRIVE_FLATTOP_LEN})
# CR_DRIVE_CONSTANTS["cr_drive_c3t2"].update({"square_positive_amp": CR_DRIVE_SQUARE_AMP, "square_positive_len": CR_DRIVE_SQUARE_LEN, "flattop_amp": CR_DRIVE_FLATTOP_AMP, "flattop_len": CR_DRIVE_FLATTOP_LEN})
# CR_DRIVE_CONSTANTS["cr_drive_c3t4"].update({"square_positive_amp": CR_DRIVE_SQUARE_AMP, "square_positive_len": CR_DRIVE_SQUARE_LEN, "flattop_amp": CR_DRIVE_FLATTOP_AMP, "flattop_len": CR_DRIVE_FLATTOP_LEN})
# CR_DRIVE_CONSTANTS["cr_drive_c4t3"].update({"square_positive_amp": CR_DRIVE_SQUARE_AMP, "square_positive_len": CR_DRIVE_SQUARE_LEN, "flattop_amp": CR_DRIVE_FLATTOP_AMP, "flattop_len": CR_DRIVE_FLATTOP_LEN})
# for k, v in CR_DRIVE_CONSTANTS.items():
#     k.update({
#         "square_negative_amp": -v["square_positive_amp"],
#         "flattop_negative_amp": -v["flattop_positive_amp"],
#         "gaussian_rise_positive_amp": v["flattop_positive_amp"],
#         "gaussian_rise_negative_amp": -v["flattop_positive_amp"],
#         "gaussian_fall_positive_amp": v["flattop_positive_amp"],
#         "gaussian_fall_negative_amp": -v["flattop_positive_amp"],
# })


# Constants for each qubit for CR CANCEL DRIVE
CR_CANCEL_CONSTANTS = {
    **{f"cr_cancel_c{c}t{t}": {
        # main
        "square_positive_amp": CR_CANCEL_SQUARE_AMP,
        "square_positive_len": CR_CANCEL_SQUARE_LEN,
        "flattop_positive_amp": CR_CANCEL_FLATTOP_AMP,
        "flattop_positive_len": CR_CANCEL_FLATTOP_LEN,
        "square_negative_amp": -CR_CANCEL_SQUARE_AMP,
        "square_negative_len": CR_CANCEL_SQUARE_LEN,
        "flattop_negative_amp": -CR_CANCEL_FLATTOP_AMP,
        "flattop_negative_len": CR_CANCEL_FLATTOP_LEN,
        # twin
        "gaussian_rise_positive_amp": CR_CANCEL_GAUSSIAN_RISE_AMP,
        "gaussian_rise_positive_len": CR_CANCEL_GAUSSIAN_RISE_LEN,
        "gaussian_rise_positive_pad_len": CR_DRIVE_GAUSSIAN_RISE_PAD_LEN,
        "gaussian_fall_positive_amp": CR_CANCEL_GAUSSIAN_FALL_AMP,
        "gaussian_fall_positive_len": CR_CANCEL_GAUSSIAN_FALL_LEN,
        "gaussian_fall_positive_pad_len": CR_DRIVE_GAUSSIAN_FALL_PAD_LEN,
        "gaussian_rise_negative_amp": -CR_CANCEL_GAUSSIAN_RISE_AMP,
        "gaussian_rise_negative_len": CR_CANCEL_GAUSSIAN_RISE_LEN,
        "gaussian_rise_negative_pad_len": CR_DRIVE_GAUSSIAN_RISE_PAD_LEN,
        "gaussian_fall_negative_amp": -CR_CANCEL_GAUSSIAN_FALL_AMP,
        "gaussian_fall_negative_len": CR_CANCEL_GAUSSIAN_FALL_LEN,
        "gaussian_fall_negative_pad_len": CR_DRIVE_GAUSSIAN_FALL_PAD_LEN,
        # common
        "LO": QUBIT_CONSTANTS[f"q{t}_xy"]["LO"],
        "IF": QUBIT_CONSTANTS[f"q{t}_xy"]["IF"],
        "con": QUBIT_CONSTANTS[f"q{t}_xy"]["con"],
        "ao_I": QUBIT_CONSTANTS[f"q{t}_xy"]["ao_I"],
        "ao_Q": QUBIT_CONSTANTS[f"q{t}_xy"]["ao_Q"],
        "rf_in": QUBIT_CONSTANTS[f"q{t}_xy"]["rf_in"],
        "delay": QUBIT_CONSTANTS[f"q{t}_xy"]["delay"],
        "thread_main": None,
        "thread_twin": None,
    } for c, t in qubit_pairs}
}
# update after finidng the optimal parameters for amplitude and cr_square_len for each pair
# CR_CANCEL_CONSTANTS["cr_cancel_c1t2"].update({"square_positive_amp": CR_CANCEL_SQUARE_AMP, "square_positive_len": CR_CANCEL_SQUARE_LEN, "flattop_amp": CR_CANCEL_FLATTOP_AMP, "flattop_len": CR_CANCEL_FLATTOP_LEN})
# CR_CANCEL_CONSTANTS["cr_cancel_c2t1"].update({"square_positive_amp": CR_CANCEL_SQUARE_AMP, "square_positive_len": CR_CANCEL_SQUARE_LEN, "flattop_amp": CR_CANCEL_FLATTOP_AMP, "flattop_len": CR_CANCEL_FLATTOP_LEN})
# CR_CANCEL_CONSTANTS["cr_cancel_c2t3"].update({"square_positive_amp": CR_CANCEL_SQUARE_AMP, "square_positive_len": CR_CANCEL_SQUARE_LEN, "flattop_amp": CR_CANCEL_FLATTOP_AMP, "flattop_len": CR_CANCEL_FLATTOP_LEN})
# CR_CANCEL_CONSTANTS["cr_cancel_c3t2"].update({"square_positive_amp": CR_CANCEL_SQUARE_AMP, "square_positive_len": CR_CANCEL_SQUARE_LEN, "flattop_amp": CR_CANCEL_FLATTOP_AMP, "flattop_len": CR_CANCEL_FLATTOP_LEN})
# CR_CANCEL_CONSTANTS["cr_cancel_c3t4"].update({"square_positive_amp": CR_CANCEL_SQUARE_AMP, "square_positive_len": CR_CANCEL_SQUARE_LEN, "flattop_amp": CR_CANCEL_FLATTOP_AMP, "flattop_len": CR_CANCEL_FLATTOP_LEN})
# CR_CANCEL_CONSTANTS["cr_cancel_c4t3"].update({"square_positive_amp": CR_CANCEL_SQUARE_AMP, "square_positive_len": CR_CANCEL_SQUARE_LEN, "flattop_amp": CR_DRIVE_FLATTOP_AMP, "flattop_len": CR_DRIVE_FLATTOP_LEN})
# for k, v in CR_DRIVE_CONSTANTS.items():
#     k.update({
#         "square_negative_amp": -v["square_positive_amp"],
#         "flattop_negative_amp": -v["flattop_positive_amp"],
#         "gaussian_rise_positive_amp": v["flattop_positive_amp"],
#         "gaussian_rise_negative_amp": -v["flattop_positive_amp"],
#         "gaussian_fall_positive_amp": v["flattop_positive_amp"],
#         "gaussian_fall_negative_amp": -v["flattop_positive_amp"],
# })


# MARK: STARK-INDUCED ZZ INTERACTION
#############################################
#      STARK-INDUCED ZZ INTERACTION         #
#############################################

qubit_pairs = [
    ["1", "2"], ["2", "1"],
    ["2", "3"], ["3", "2"],
    ["3", "4"], ["4", "3"],
]

ZZ_CONTROL_DETUNING = 0 * u.MHz
ZZ_CONTROL_SQUARE_AMP = 0.2
ZZ_CONTROL_SQUARE_LEN = 120
ZZ_CONTROL_FLATTOP_AMP = 0.2
ZZ_CONTROL_FLATTOP_LEN = 100
ZZ_CONTROL_GAUSSIAN_RISE_AMP = ZZ_CONTROL_FLATTOP_AMP
ZZ_CONTROL_GAUSSIAN_RISE_LEN = 20
ZZ_CONTROL_GAUSSIAN_RISE_PAD_LEN = ZZ_CONTROL_GAUSSIAN_RISE_LEN % 4
ZZ_CONTROL_GAUSSIAN_FALL_AMP = ZZ_CONTROL_FLATTOP_AMP
ZZ_CONTROL_GAUSSIAN_FALL_LEN = ZZ_CONTROL_GAUSSIAN_RISE_LEN
ZZ_CONTROL_GAUSSIAN_FALL_PAD_LEN = ZZ_CONTROL_GAUSSIAN_FALL_LEN % 4

ZZ_TARGET_DETUNING = ZZ_CONTROL_DETUNING
ZZ_TARGET_SQUARE_AMP = ZZ_CONTROL_SQUARE_AMP
ZZ_TARGET_SQUARE_LEN = ZZ_CONTROL_SQUARE_LEN
ZZ_TARGET_FLATTOP_AMP = ZZ_CONTROL_FLATTOP_AMP
ZZ_TARGET_FLATTOP_LEN = ZZ_CONTROL_FLATTOP_LEN
ZZ_TARGET_GAUSSIAN_RISE_AMP = ZZ_CONTROL_FLATTOP_AMP
ZZ_TARGET_GAUSSIAN_RISE_LEN = ZZ_CONTROL_GAUSSIAN_RISE_LEN
ZZ_TARGET_GAUSSIAN_RISE_PAD_LEN = ZZ_CONTROL_GAUSSIAN_RISE_LEN % 4
ZZ_TARGET_GAUSSIAN_FALL_AMP = ZZ_CONTROL_FLATTOP_AMP
ZZ_TARGET_GAUSSIAN_FALL_LEN = ZZ_CONTROL_GAUSSIAN_RISE_LEN
ZZ_TARGET_GAUSSIAN_FALL_PAD_LEN = ZZ_CONTROL_GAUSSIAN_FALL_LEN % 4

assert (ZZ_CONTROL_GAUSSIAN_RISE_LEN + ZZ_CONTROL_GAUSSIAN_RISE_PAD_LEN) % 4 == 0, "duration of padded gaussian rise / fall len must be integer multiple of 4 ns"
assert (ZZ_CONTROL_GAUSSIAN_FALL_LEN + ZZ_CONTROL_GAUSSIAN_FALL_PAD_LEN) % 4 == 0, "duration of padded gaussian rise / fall len must be integer multiple of 4 ns"
assert (ZZ_TARGET_GAUSSIAN_RISE_LEN + ZZ_TARGET_GAUSSIAN_RISE_PAD_LEN) % 4 == 0, "duration of padded gaussian rise / fall len must be integer multiple of 4 ns"
assert (ZZ_TARGET_GAUSSIAN_FALL_LEN + ZZ_TARGET_GAUSSIAN_FALL_PAD_LEN) % 4 == 0, "duration of padded gaussian rise / fall len must be integer multiple of 4 ns"


ZZ_CONTROL_CONSTANTS = {
    **{f"zz_control_c{c}t{t}": {
        "control_index": int(c),
        "target_index": int(t),
        # main
        "square_amp": ZZ_CONTROL_SQUARE_AMP,
        "square_len": ZZ_CONTROL_SQUARE_LEN,
        "flattop_amp": ZZ_CONTROL_FLATTOP_AMP,
        "flattop_len": ZZ_CONTROL_FLATTOP_LEN,
        # twin
        "gaussian_rise_amp": ZZ_CONTROL_GAUSSIAN_RISE_AMP,
        "gaussian_rise_len": ZZ_CONTROL_GAUSSIAN_RISE_LEN,
        "gaussian_rise_pad_len": ZZ_CONTROL_GAUSSIAN_RISE_PAD_LEN,
        "gaussian_fall_amp": ZZ_CONTROL_GAUSSIAN_FALL_AMP,
        "gaussian_fall_len": ZZ_CONTROL_GAUSSIAN_FALL_LEN,
        "gaussian_fall_pad_len": ZZ_CONTROL_GAUSSIAN_FALL_PAD_LEN,
        # common
        "detuning": ZZ_CONTROL_DETUNING,
        "LO": QUBIT_CONSTANTS[f"q{t}_xy"]["LO"],
        "IF": QUBIT_CONSTANTS[f"q{t}_xy"]["IF"],
        "con": QUBIT_CONSTANTS[f"q{c}_xy"]["con"],
        "ao_I": QUBIT_CONSTANTS[f"q{c}_xy"]["ao_I"],
        "ao_Q": QUBIT_CONSTANTS[f"q{c}_xy"]["ao_Q"],
        "rf_in": QUBIT_CONSTANTS[f"q{c}_xy"]["rf_in"],
        "delay": QUBIT_CONSTANTS[f"q{c}_xy"]["delay"],
        "thread_main": None,
        "thread_twin": None,
    } for c, t in qubit_pairs}
}
# # main
# ZZ_CONTROL_CONSTANTS["zz_control_c1t2"].update({"detuning: ZZ_CONTROL_DETUNING, "square_amp": ZZ_CONTROL_SQUARE_AMP, "square_len": ZZ_CONTROL_SQUARE_LEN, "flattop_amp": ZZ_CONTROL_FLATTOP_AMP, "flattop_len": ZZ_CONTROL_FLATTOP_LEN})
# ZZ_CONTROL_CONSTANTS["zz_control_c2t1"].update({"detuning: ZZ_CONTROL_DETUNING, "square_amp": ZZ_CONTROL_SQUARE_AMP, "square_len": ZZ_CONTROL_SQUARE_LEN, "flattop_amp": ZZ_CONTROL_FLATTOP_AMP, "flattop_len": ZZ_CONTROL_FLATTOP_LEN})
# ZZ_CONTROL_CONSTANTS["zz_control_c2t3"].update({"detuning: ZZ_CONTROL_DETUNING, "square_amp": ZZ_CONTROL_SQUARE_AMP, "square_len": ZZ_CONTROL_SQUARE_LEN, "flattop_amp": ZZ_CONTROL_FLATTOP_AMP, "flattop_len": ZZ_CONTROL_FLATTOP_LEN})
# ZZ_CONTROL_CONSTANTS["zz_control_c3t2"].update({"detuning: ZZ_CONTROL_DETUNING, "square_amp": ZZ_CONTROL_SQUARE_AMP, "square_len": ZZ_CONTROL_SQUARE_LEN, "flattop_amp": ZZ_CONTROL_FLATTOP_AMP, "flattop_len": ZZ_CONTROL_FLATTOP_LEN})
# ZZ_CONTROL_CONSTANTS["zz_control_c3t4"].update({"detuning: ZZ_CONTROL_DETUNING, "square_amp": ZZ_CONTROL_SQUARE_AMP, "square_len": ZZ_CONTROL_SQUARE_LEN, "flattop_amp": ZZ_CONTROL_FLATTOP_AMP, "flattop_len": ZZ_CONTROL_FLATTOP_LEN})
# ZZ_CONTROL_CONSTANTS["zz_control_c4t3"].update({"detuning: ZZ_CONTROL_DETUNING, "square_amp": ZZ_CONTROL_SQUARE_AMP, "square_len": ZZ_CONTROL_SQUARE_LEN, "flattop_amp": ZZ_CONTROL_FLATTOP_AMP, "flattop_len": ZZ_CONTROL_FLATTOP_LEN})
# # twin
# ZZ_CONTROL_CONSTANTS["zz_control_c1t2"].update({"detuning: ZZ_CONTROL_DETUNING, "gaussian_rise_amp": ZZ_CONTROL_GAUSSIAN_RISE_AMP, "gaussian_rise_len": ZZ_CONTROL_GAUSSIAN_RISE_LEN, "gaussian_fall_amp": ZZ_CONTROL_GAUSSIAN_FALL_AMP, "gaussian_fall_len": ZZ_CONTROL_GAUSSIAN_FALL_LEN})
# ZZ_CONTROL_CONSTANTS["zz_control_c2t1"].update({"detuning: ZZ_CONTROL_DETUNING, "gaussian_rise_amp": ZZ_CONTROL_GAUSSIAN_RISE_AMP, "gaussian_rise_len": ZZ_CONTROL_GAUSSIAN_RISE_LEN, "gaussian_fall_amp": ZZ_CONTROL_GAUSSIAN_FALL_AMP, "gaussian_fall_len": ZZ_CONTROL_GAUSSIAN_FALL_LEN})
# ZZ_CONTROL_CONSTANTS["zz_control_c2t3"].update({"detuning: ZZ_CONTROL_DETUNING, "gaussian_rise_amp": ZZ_CONTROL_GAUSSIAN_RISE_AMP, "gaussian_rise_len": ZZ_CONTROL_GAUSSIAN_RISE_LEN, "gaussian_fall_amp": ZZ_CONTROL_GAUSSIAN_FALL_AMP, "gaussian_fall_len": ZZ_CONTROL_GAUSSIAN_FALL_LEN})
# ZZ_CONTROL_CONSTANTS["zz_control_c3t2"].update({"detuning: ZZ_CONTROL_DETUNING, "gaussian_rise_amp": ZZ_CONTROL_GAUSSIAN_RISE_AMP, "gaussian_rise_len": ZZ_CONTROL_GAUSSIAN_RISE_LEN, "gaussian_fall_amp": ZZ_CONTROL_GAUSSIAN_FALL_AMP, "gaussian_fall_len": ZZ_CONTROL_GAUSSIAN_FALL_LEN})
# ZZ_CONTROL_CONSTANTS["zz_control_c3t4"].update({"detuning: ZZ_CONTROL_DETUNING, "gaussian_rise_amp": ZZ_CONTROL_GAUSSIAN_RISE_AMP, "gaussian_rise_len": ZZ_CONTROL_GAUSSIAN_RISE_LEN, "gaussian_fall_amp": ZZ_CONTROL_GAUSSIAN_FALL_AMP, "gaussian_fall_len": ZZ_CONTROL_GAUSSIAN_FALL_LEN})
# ZZ_CONTROL_CONSTANTS["zz_control_c4t3"].update({"detuning: ZZ_CONTROL_DETUNING, "gaussian_rise_amp": ZZ_CONTROL_GAUSSIAN_RISE_AMP, "gaussian_rise_len": ZZ_CONTROL_GAUSSIAN_RISE_LEN, "gaussian_fall_amp": ZZ_CONTROL_GAUSSIAN_FALL_AMP, "gaussian_fall_len": ZZ_CONTROL_GAUSSIAN_FALL_LEN})
for zz, val in ZZ_CONTROL_CONSTANTS.items():
    val["IF"] += val["detuning"]

ZZ_TARGET_CONSTANTS = {
    **{f"zz_target_c{c}t{t}": {
        "control_index": int(c),
        "target_index": int(t),
        # main
        "square_amp": ZZ_TARGET_SQUARE_AMP,
        "square_len": ZZ_TARGET_SQUARE_LEN,
        "flattop_amp": ZZ_TARGET_FLATTOP_AMP,
        "flattop_len": ZZ_TARGET_FLATTOP_LEN,
        # twin
        "gaussian_rise_amp": ZZ_TARGET_GAUSSIAN_RISE_AMP,
        "gaussian_rise_len": ZZ_TARGET_GAUSSIAN_RISE_LEN,
        "gaussian_rise_pad_len": ZZ_TARGET_GAUSSIAN_RISE_PAD_LEN,
        "gaussian_fall_amp": ZZ_TARGET_GAUSSIAN_FALL_AMP,
        "gaussian_fall_len": ZZ_TARGET_GAUSSIAN_FALL_LEN,
        "gaussian_fall_pad_len": ZZ_TARGET_GAUSSIAN_FALL_PAD_LEN,
        # common
        "detuning": ZZ_TARGET_DETUNING,
        "LO": QUBIT_CONSTANTS[f"q{t}_xy"]["LO"],
        "IF": QUBIT_CONSTANTS[f"q{t}_xy"]["IF"],
        "con": QUBIT_CONSTANTS[f"q{t}_xy"]["con"],
        "ao_I": QUBIT_CONSTANTS[f"q{t}_xy"]["ao_I"],
        "ao_Q": QUBIT_CONSTANTS[f"q{t}_xy"]["ao_Q"],
        "rf_in": QUBIT_CONSTANTS[f"q{t}_xy"]["rf_in"],
        "delay": QUBIT_CONSTANTS[f"q{t}_xy"]["delay"],
        "thread_main": None,
        "thread_twin": None,
    } for c, t in qubit_pairs}
}
# # main
# ZZ_TARGET_CONSTANTS["zz_target_c1t2"].update({"detuning: ZZ_TARGET_DETUNING, "square_amp": ZZ_TARGET_SQUARE_AMP, "square_len": ZZ_TARGET_SQUARE_LEN, "flattop_amp": ZZ_TARGET_FLATTOP_AMP, "flattop_len": ZZ_TARGET_FLATTOP_LEN})
# ZZ_TARGET_CONSTANTS["zz_target_c2t1"].update({"detuning: ZZ_TARGET_DETUNING, "square_amp": ZZ_TARGET_SQUARE_AMP, "square_len": ZZ_TARGET_SQUARE_LEN, "flattop_amp": ZZ_TARGET_FLATTOP_AMP, "flattop_len": ZZ_TARGET_FLATTOP_LEN})
# ZZ_TARGET_CONSTANTS["zz_target_c2t3"].update({"detuning: ZZ_TARGET_DETUNING, "square_amp": ZZ_TARGET_SQUARE_AMP, "square_len": ZZ_TARGET_SQUARE_LEN, "flattop_amp": ZZ_TARGET_FLATTOP_AMP, "flattop_len": ZZ_TARGET_FLATTOP_LEN})
# ZZ_TARGET_CONSTANTS["zz_target_c3t2"].update({"detuning: ZZ_TARGET_DETUNING, "square_amp": ZZ_TARGET_SQUARE_AMP, "square_len": ZZ_TARGET_SQUARE_LEN, "flattop_amp": ZZ_TARGET_FLATTOP_AMP, "flattop_len": ZZ_TARGET_FLATTOP_LEN})
# ZZ_TARGET_CONSTANTS["zz_target_c3t4"].update({"detuning: ZZ_TARGET_DETUNING, "square_amp": ZZ_TARGET_SQUARE_AMP, "square_len": ZZ_TARGET_SQUARE_LEN, "flattop_amp": ZZ_TARGET_FLATTOP_AMP, "flattop_len": ZZ_TARGET_FLATTOP_LEN})
# ZZ_TARGET_CONSTANTS["zz_target_c4t3"].update({"detuning: ZZ_TARGET_DETUNING, "square_amp": ZZ_TARGET_SQUARE_AMP, "square_len": ZZ_TARGET_SQUARE_LEN, "flattop_amp": ZZ_TARGET_FLATTOP_AMP, "flattop_len": ZZ_TARGET_FLATTOP_LEN})
# # twin
# ZZ_TARGET_CONSTANTS["zz_target_c1t2"].update({"detuning: ZZ_TARGET_DETUNING, "gaussian_rise_amp": ZZ_TARGET_GAUSSIAN_RISE_AMP, "gaussian_rise_len": ZZ_TARGET_GAUSSIAN_RISE_LEN, "gaussian_fall_amp": ZZ_TARGET_GAUSSIAN_FALL_AMP, "gaussian_fall_len": ZZ_TARGET_GAUSSIAN_FALL_LEN})
# ZZ_TARGET_CONSTANTS["zz_target_c2t1"].update({"detuning: ZZ_TARGET_DETUNING, "gaussian_rise_amp": ZZ_TARGET_GAUSSIAN_RISE_AMP, "gaussian_rise_len": ZZ_TARGET_GAUSSIAN_RISE_LEN, "gaussian_fall_amp": ZZ_TARGET_GAUSSIAN_FALL_AMP, "gaussian_fall_len": ZZ_TARGET_GAUSSIAN_FALL_LEN})
# ZZ_TARGET_CONSTANTS["zz_target_c2t3"].update({"detuning: ZZ_TARGET_DETUNING, "gaussian_rise_amp": ZZ_TARGET_GAUSSIAN_RISE_AMP, "gaussian_rise_len": ZZ_TARGET_GAUSSIAN_RISE_LEN, "gaussian_fall_amp": ZZ_TARGET_GAUSSIAN_FALL_AMP, "gaussian_fall_len": ZZ_TARGET_GAUSSIAN_FALL_LEN})
# ZZ_TARGET_CONSTANTS["zz_target_c3t2"].update({"detuning: ZZ_TARGET_DETUNING, "gaussian_rise_amp": ZZ_TARGET_GAUSSIAN_RISE_AMP, "gaussian_rise_len": ZZ_TARGET_GAUSSIAN_RISE_LEN, "gaussian_fall_amp": ZZ_TARGET_GAUSSIAN_FALL_AMP, "gaussian_fall_len": ZZ_TARGET_GAUSSIAN_FALL_LEN})
# ZZ_TARGET_CONSTANTS["zz_target_c3t4"].update({"detuning: ZZ_TARGET_DETUNING, "gaussian_rise_amp": ZZ_TARGET_GAUSSIAN_RISE_AMP, "gaussian_rise_len": ZZ_TARGET_GAUSSIAN_RISE_LEN, "gaussian_fall_amp": ZZ_TARGET_GAUSSIAN_FALL_AMP, "gaussian_fall_len": ZZ_TARGET_GAUSSIAN_FALL_LEN})
# ZZ_TARGET_CONSTANTS["zz_target_c4t3"].update({"detuning: ZZ_TARGET_DETUNING, "gaussian_rise_amp": ZZ_TARGET_GAUSSIAN_RISE_AMP, "gaussian_rise_len": ZZ_TARGET_GAUSSIAN_RISE_LEN, "gaussian_fall_amp": ZZ_TARGET_GAUSSIAN_FALL_AMP, "gaussian_fall_len": ZZ_TARGET_GAUSSIAN_FALL_LEN})
for zz, val in ZZ_TARGET_CONSTANTS.items():
    val["IF"] += val["detuning"]


# MARK: RESONATORS
#############################################
#                Resonators                 #
#############################################

READOUT_AMP = 0.1
READOUT_LEN = 900
rr_reset_time = 4_000
# midcircuit
READOUT_MIDCIRCUIT_AMP = 0.1
READOUT_MIDCIRCUIT_LEN = READOUT_LEN

RL_CONSTANTS = {
    "rl1": {
        "LO": 3.2 * u.GHz,
        "RESONATORS": [
            "q1_rr",
            "q2_rr",
            "q3_rr",
            "q4_rr",
        ],
        "TOF": 28,
        "con": "con1",
        "ao_I": 1,
        "ao_Q": 2,
        "ai_I": 1,
        "ai_Q": 2,
        "rf_in": 1,
        "rf_out": 1,
        "delay": delays["rl1"],
    },
}

RR_CONSTANTS = {
    "q1_rr": {
        "IF": 0 * u.MHz,
        "readout_amp": READOUT_AMP,
        "readout_len": READOUT_LEN,
        "rotation_angle": (0.0 / 180) * np.pi,
        "ge_threshold": 0.0,
        "midcircuit_readout_amp": READOUT_MIDCIRCUIT_AMP,
        "midcircuit_readout_len": READOUT_MIDCIRCUIT_LEN,
        "midcircuit_readout_rotation_angle": (0.0 / 180) * np.pi,
        "midcircuit_readout_ge_threshold": 0.0,
        "TOF": RL_CONSTANTS["rl1"]["TOF"],
        "LO": RL_CONSTANTS["rl1"]["LO"],
        "con": RL_CONSTANTS["rl1"]["con"],
        "ao_I": RL_CONSTANTS["rl1"]["ao_I"],
        "ao_Q": RL_CONSTANTS["rl1"]["ao_Q"],
        "rf_in": RL_CONSTANTS["rl1"]["rf_in"],
        "rf_out": RL_CONSTANTS["rl1"]["rf_out"],
        "delay": RL_CONSTANTS["rl1"]["delay"],
        "thread": QUBIT_CONSTANTS[f"q1_xy"]["thread"],
    },
    "q2_rr": {
        "IF": -50 * u.MHz,
        "readout_amp": READOUT_AMP,
        "readout_len": READOUT_LEN,
        "rotation_angle": (0.0 / 180) * np.pi,
        "ge_threshold": 0.0,
        "midcircuit_readout_amp": READOUT_MIDCIRCUIT_AMP, 
        "midcircuit_readout_len": READOUT_MIDCIRCUIT_LEN, 
        "midcircuit_readout_rotation_angle": (0.0 / 180) * np.pi,
        "midcircuit_readout_ge_threshold": 0.0,
        "TOF": RL_CONSTANTS["rl1"]["TOF"],
        "LO": RL_CONSTANTS["rl1"]["LO"],
        "con": RL_CONSTANTS["rl1"]["con"],
        "ao_I": RL_CONSTANTS["rl1"]["ao_I"],
        "ao_Q": RL_CONSTANTS["rl1"]["ao_Q"],
        "rf_in": RL_CONSTANTS["rl1"]["rf_in"],
        "rf_out": RL_CONSTANTS["rl1"]["rf_out"],
        "delay": RL_CONSTANTS["rl1"]["delay"],
        "thread": QUBIT_CONSTANTS[f"q2_xy"]["thread"],
    },
    "q3_rr": {
        "IF": -100 * u.MHz,
        "readout_amp": READOUT_AMP,
        "readout_len": READOUT_LEN,
        "rotation_angle": (0.0 / 180) * np.pi,
        "ge_threshold": 0.0,
        "midcircuit_readout_amp": READOUT_MIDCIRCUIT_AMP,
        "midcircuit_readout_len": READOUT_MIDCIRCUIT_LEN,
        "midcircuit_readout_rotation_angle": (0.0 / 180) * np.pi,
        "midcircuit_readout_ge_threshold": 0.0,
        "TOF": RL_CONSTANTS["rl1"]["TOF"],
        "LO": RL_CONSTANTS["rl1"]["LO"],
        "con": RL_CONSTANTS["rl1"]["con"],
        "ao_I": RL_CONSTANTS["rl1"]["ao_I"],
        "ao_Q": RL_CONSTANTS["rl1"]["ao_Q"],
        "rf_in": RL_CONSTANTS["rl1"]["rf_in"],
        "rf_out": RL_CONSTANTS["rl1"]["rf_out"],
        "delay": RL_CONSTANTS["rl1"]["delay"],
        "thread": QUBIT_CONSTANTS[f"q3_xy"]["thread"],
    },
    "q4_rr": {
        "IF": -150 * u.MHz,
        "readout_amp": READOUT_AMP,
        "readout_len": READOUT_LEN,
        "rotation_angle": (0.0 / 180) * np.pi,
        "ge_threshold": 0.0,
        "midcircuit_readout_amp": READOUT_MIDCIRCUIT_AMP, 
        "midcircuit_readout_len": READOUT_MIDCIRCUIT_LEN, 
        "midcircuit_readout_rotation_angle": (0.0 / 180) * np.pi,
        "midcircuit_readout_ge_threshold": 0.0,
        "TOF": RL_CONSTANTS["rl1"]["TOF"],
        "LO": RL_CONSTANTS["rl1"]["LO"],
        "con": RL_CONSTANTS["rl1"]["con"],
        "ao_I": RL_CONSTANTS["rl1"]["ao_I"],
        "ao_Q": RL_CONSTANTS["rl1"]["ao_Q"],
        "rf_in": RL_CONSTANTS["rl1"]["rf_in"],
        "rf_out": RL_CONSTANTS["rl1"]["rf_out"],
        "delay": RL_CONSTANTS["rl1"]["delay"],
        "thread": QUBIT_CONSTANTS[f"q4_xy"]["thread"],
    },
}

assert set(RR_CONSTANTS.keys()) == set([rr for rl, val in RL_CONSTANTS.items() for rr in val["RESONATORS"]]), "resonators in RL_CONSTANTS and RR_CONTANTS do not match!"

for rr, val in RR_CONSTANTS.items():
    assert val["readout_amp"] <= 0.499, f"{rr} amplitude needs to be less than 0.499"

for rl_key in RL_CONSTANTS.keys():
    total_amp = 0
    for rr in RL_CONSTANTS[rl_key]["RESONATORS"]:
        total_amp += RR_CONSTANTS[rr]["readout_amp"]
    assert total_amp <= 0.499, f"the sum of resonators on the readoutline {rl_key} is larger than 0.499"

opt_weights = False
if opt_weights:

    current_file_path = os.path.dirname(os.path.abspath(__file__))
    weights_q1_rr = np.load(os.path.join(current_file_path, "optimal_weights_q1_rr.npz"))
    weights_q2_rr = np.load(os.path.join(current_file_path, "optimal_weights_q2_rr.npz"))
    weights_q3_rr = np.load(os.path.join(current_file_path, "optimal_weights_q3_rr.npz"))
    weights_q4_rr = np.load(os.path.join(current_file_path, "optimal_weights_q4_rr.npz"))

    OPT_WEIGHTS = {
        "q1_rr": {
            "real": [(x, weights_q1_rr["division_length"] * 4) for x in weights_q1_rr["weights_real"]],
            "minus_imag": [(x, weights_q1_rr["division_length"] * 4) for x in weights_q1_rr["weights_minus_imag"]],
            "imag": [(x, weights_q1_rr["division_length"] * 4) for x in weights_q1_rr["weights_imag"]] ,
            "minus_real": [(x, weights_q1_rr["division_length"] * 4) for x in weights_q1_rr["weights_minus_real"]] 
        },
        "q2_rr": {
            "real": [(x, weights_q2_rr["division_length"] * 4) for x in weights_q2_rr["weights_real"]],
            "minus_imag": [(x, weights_q2_rr["division_length"] * 4) for x in weights_q2_rr["weights_minus_imag"]],
            "imag": [(x, weights_q2_rr["division_length"] * 4) for x in weights_q2_rr["weights_imag"]] ,
            "minus_real": [(x, weights_q2_rr["division_length"] * 4) for x in weights_q2_rr["weights_minus_real"]] 
        },
        "q3_rr": {
            "real": [(x, weights_q3_rr["division_length"] * 4) for x in weights_q3_rr["weights_real"]],
            "minus_imag": [(x, weights_q3_rr["division_length"] * 4) for x in weights_q3_rr["weights_minus_imag"]],
            "imag": [(x, weights_q3_rr["division_length"] * 4) for x in weights_q3_rr["weights_imag"]] ,
            "minus_real": [(x, weights_q3_rr["division_length"] * 4) for x in weights_q3_rr["weights_minus_real"]] 
        },
        "q4_rr": {
            "real": [(x, weights_q4_rr["division_length"] * 4) for x in weights_q4_rr["weights_real"]],
            "minus_imag": [(x, weights_q4_rr["division_length"] * 4) for x in weights_q4_rr["weights_minus_imag"]],
            "imag": [(x, weights_q4_rr["division_length"] * 4) for x in weights_q4_rr["weights_imag"]] ,
            "minus_real": [(x, weights_q4_rr["division_length"] * 4) for x in weights_q4_rr["weights_minus_real"]] 
        },
    }

else:
    OPT_WEIGHTS = {
        "q1_rr": {
            "real": [(1.0, READOUT_LEN)],
            "minus_imag": [(0.0, READOUT_LEN)],
            "imag": [(0.0, READOUT_LEN)],
            "minus_real": [(1.0, READOUT_LEN)]
        },
        "q2_rr": {
            "real": [(1.0, READOUT_LEN)],
            "minus_imag": [(0.0, READOUT_LEN)],
            "imag": [(0.0, READOUT_LEN)],
            "minus_real": [(1.0, READOUT_LEN)]
        },
        "q3_rr": {
            "real": [(1.0, READOUT_LEN)],
            "minus_imag": [(0.0, READOUT_LEN)],
            "imag": [(0.0, READOUT_LEN)],
            "minus_real": [(1.0, READOUT_LEN)]
        },
        "q4_rr": {
            "real": [(1.0, READOUT_LEN)],
            "minus_imag": [(0.0, READOUT_LEN)],
            "imag": [(0.0, READOUT_LEN)],
            "minus_real": [(1.0, READOUT_LEN)]
        },
    }


##################
# DELAYS PER FEM #
##################

# MARK: CONFIGURATION
#############################################
#                  Config                   #
#############################################
config = {
    "version": 1,
    "controllers": {
        "con1": {
            "analog_outputs": {
                1: {"offset": 0.0},  # I readout line
                2: {"offset": 0.0},  # Q readout line
                3: {"offset": 0.0},  # I qubit1 XY
                4: {"offset": 0.0},  # Q qubit1 XY
                5: {"offset": 0.0},  # I qubit2 XY
                6: {"offset": 0.0},  # Q qubit2 XY
                7: {"offset": 0.0},  # I qubit3 XY
                8: {"offset": 0.0},  # Q qubit3 XY
                9: {"offset": 0.0},  # I qubit4 XY
                10: {"offset": 0.0},  # Q qubit4 XY
            },
            "digital_outputs": {
                1: {},
            },
            "analog_inputs": {
                1: {"offset": 0.0, "gain_db": 0},  # I from down-conversion
                2: {"offset": 0.0, "gain_db": 0},  # Q from down-conversion
            },
        },
    },
    "octaves": {
        "octave1": {
            "RF_outputs": {
                1: {
                    "LO_frequency": RL_CONSTANTS["rl1"]["LO"],
                    "LO_source": "internal",
                    "output_mode": "always_on",
                    "gain": 0,
                },
                2: {
                    "LO_frequency": QUBIT_CONSTANTS["q1_xy"]["LO"],
                    "LO_source": "internal",
                    "output_mode": "always_on",
                    "gain": 0,
                },
                3: {
                    "LO_frequency": QUBIT_CONSTANTS["q2_xy"]["LO"],
                    "LO_source": "internal",
                    "output_mode": "always_on",
                    "gain": 0,
                },
                4: {
                    "LO_frequency": QUBIT_CONSTANTS["q3_xy"]["LO"],
                    "LO_source": "internal",
                    "output_mode": "always_on",
                    "gain": 0,
                },
                5: {
                    "LO_frequency": QUBIT_CONSTANTS["q4_xy"]["LO"],
                    "LO_source": "internal",
                    "output_mode": "always_on",
                    "gain": 0,
                },
            },
            "RF_inputs": {
                1: {
                    "LO_frequency": RL_CONSTANTS["rl1"]["LO"],
                    "LO_source": "internal",
                },
            },
            "connectivity": "con1",
        }
    },
    "elements": {

        # readout line 1
        **{rr: {
            "RF_inputs": {"port": ("octave1", val["rf_in"])},
            "RF_outputs": {"port": ("octave1", val["rf_out"])},
            "intermediate_frequency": val["IF"],  # in Hz [-350e6, +350e6]
			'time_of_flight': val["TOF"],
            'smearing': 0,
            "operations": {
                "cw": "const_pulse",
                "readout": f"readout_pulse_{rr}",
                "midcircuit_readout": f"midcircuit_readout_pulse_{rr}",
            },
            # "thread": val["thread-main"],
        } for rr, val in RR_CONSTANTS.items()},

        # xy drives
        **{qb: {
            "RF_inputs": {"port": ("octave1", val["rf_in"])},
            "intermediate_frequency": val["IF"],  # in Hz
            "operations": {
                "zero": "zero_pulse",
                "cw": "const_pulse",
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
        **{cr_drive: {
            "RF_inputs": {"port": ("octave1", val["rf_in"])},
            "intermediate_frequency": val["IF"],  # in Hz
            "operations": {
                "cw": "const_pulse",
                "square_positive": f"square_positive_pulse_{cr_drive}",
                "square_negative": f"square_negative_pulse_{cr_drive}",
                "flattop_positive": f"flattop_positive_pulse_{cr_drive}",
                "flattop_negative": f"flattop_negative_pulse_{cr_drive}",
            },
            # "thread": val["thread_main"],
        } for cr_drive, val in CR_DRIVE_CONSTANTS.items()},

        # cr cancel
        **{cr_cancel: {
            "RF_inputs": {"port": ("octave1", val["rf_in"])},
            "intermediate_frequency": val["IF"],  # in Hz
            "operations": {
                "cw": "const_pulse",
                "square_positive": f"square_positive_pulse_{cr_cancel}",
                "square_negative": f"square_negative_pulse_{cr_cancel}",
                "flattop_positive": f"flattop_positive_pulse_{cr_cancel}",
                "flattop_negative": f"flattop_negative_pulse_{cr_cancel}",
            },
            # "thread": val["thread_main"],
        } for cr_cancel, val in CR_CANCEL_CONSTANTS.items()},

        # cr drive twin
        **{f"{cr_drive}_twin": {
            "RF_inputs": {"port": ("octave1", val["rf_in"])},
            "intermediate_frequency": val["IF"],  # in Hz
            "operations": {
                "cw": "const_pulse",
                "gaussian_rise_positive": f"gaussian_rise_positive_pulse_{cr_drive}_twin",
                "gaussian_fall_positive": f"gaussian_fall_positive_pulse_{cr_drive}_twin",
                "gaussian_rise_negative": f"gaussian_rise_negative_pulse_{cr_drive}_twin",
                "gaussian_fall_negative": f"gaussian_fall_negative_pulse_{cr_drive}_twin",
            },
            # "thread": val["thread_twin"],
        } for cr_drive, val in CR_DRIVE_CONSTANTS.items()},

        # cr cancel twin
        **{f"{cr_cancel}_twin": {
            "RF_inputs": {"port": ("octave1", val["rf_in"])},
            "intermediate_frequency": val["IF"],  # in Hz
            "operations": {
                "cw": "const_pulse",
                "gaussian_rise_positive": f"gaussian_rise_positive_pulse_{cr_cancel}_twin",
                "gaussian_fall_positive": f"gaussian_fall_positive_pulse_{cr_cancel}_twin",
                "gaussian_rise_negative": f"gaussian_rise_negative_pulse_{cr_cancel}_twin",
                "gaussian_fall_negative": f"gaussian_fall_negative_pulse_{cr_cancel}_twin",
            },
            # "thread": val["thread_twin"],
        } for cr_cancel, val in CR_CANCEL_CONSTANTS.items()},

        # zz control
        **{zz_control: {
            "RF_inputs": {"port": ("octave1", val["rf_in"])},
            "intermediate_frequency": val["IF"],  # in Hz
            "operations": {
                "cw": "const_pulse",
                "square": f"square_pulse_{zz_control}",
                "flattop": f"flattop_pulse_{zz_control}",
            },
            # "thread": val["thread_main"],
        } for zz_control, val in ZZ_CONTROL_CONSTANTS.items()},

        # zz_control cancel
        **{zz_target: {
            "RF_inputs": {"port": ("octave1", val["rf_in"])},
            "intermediate_frequency": val["IF"],  # in Hz
            "operations": {
                "cw": "const_pulse",
                "square": f"square_pulse_{zz_target}",
                "flattop": f"flattop_pulse_{zz_target}",
            },
            # "thread": val["thread_main"],
        } for zz_target, val in ZZ_TARGET_CONSTANTS.items()},

        # zz control twin
        **{f"{zz_control}_twin": {
            "RF_inputs": {"port": ("octave1", val["rf_in"])},
            "intermediate_frequency": val["IF"],  # in Hz
            "operations": {
                "cw": "const_pulse",
                "gaussian_rise": f"gaussian_rise_pulse_{zz_control}_twin",
                "gaussian_fall": f"gaussian_fall_pulse_{zz_control}_twin",
            },
            # "thread": val["thread_twin"],
        } for zz_control, val in ZZ_CONTROL_CONSTANTS.items()},

        # zz target twin
        **{f"{zz_target}_twin": {
            "RF_inputs": {"port": ("octave1", val["rf_in"])},
            "intermediate_frequency": val["IF"],  # in Hz
            "operations": {
                "cw": "const_pulse",
                "gaussian_rise": f"gaussian_rise_pulse_{zz_target}_twin",
                "gaussian_fall": f"gaussian_fall_pulse_{zz_target}_twin",
            },
            # "thread": val["thread_twin"],
        } for zz_target, val in ZZ_TARGET_CONSTANTS.items()},
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
        **{f"x90_pulse_{key}":
            {
                "operation": "control",
                "length": PI_LEN,
                "waveforms": {
                    "I": f"x90_I_wf_{key}",
                    "Q": f"x90_Q_wf_{key}"
                }
            }
            for key in QUBIT_CONSTANTS.keys()
        },
        **{f"x180_pulse_{key}":
            {
                "operation": "control",
                "length": PI_LEN,
                "waveforms": {
                    "I": f"x180_I_wf_{key}",
                    "Q": f"x180_Q_wf_{key}"
                }
            }
            for key in QUBIT_CONSTANTS.keys()
        },
        **{f"-x90_pulse_{key}":
            {
                "operation": "control",
                "length": PI_LEN,
                "waveforms": {
                    "I": f"minus_x90_I_wf_{key}",
                    "Q": f"minus_x90_Q_wf_{key}"
                }
            }
            for key in QUBIT_CONSTANTS.keys()
        },
        **{f"y90_pulse_{key}":
            {
                "operation": "control",
                "length": PI_LEN,
                "waveforms": {
                    "I": f"y90_I_wf_{key}",
                    "Q": f"y90_Q_wf_{key}"
                }
            }
            for key in QUBIT_CONSTANTS.keys()
        },
        **{f"y180_pulse_{key}":
            {
                "operation": "control",
                "length": PI_LEN,
                "waveforms": {
                    "I": f"y180_I_wf_{key}",
                    "Q": f"y180_Q_wf_{key}"
                }
            }
            for key in QUBIT_CONSTANTS.keys()
        },
        **{f"-y90_pulse_{key}":
            {
                "operation": "control",
                "length": PI_LEN,
                "waveforms": {
                    "I": f"minus_y90_I_wf_{key}",
                    "Q": f"minus_y90_Q_wf_{key}"
                }
            }
            for key in QUBIT_CONSTANTS.keys()
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
        **{f"gaussian_rise_positive_pulse_{cr_drive}_twin":
            {
                "operation": "control",
                "length": val["gaussian_rise_positive_len"],
                "waveforms": {
                    "I": f"gaussian_rise_positive_wf_{cr_drive}_twin",
                    "Q": f"zero_wf"
                }
            }
            for cr_drive, val in CR_DRIVE_CONSTANTS.items()
        },
        **{f"gaussian_rise_negative_pulse_{cr_drive}_twin":
            {
                "operation": "control",
                "length": val["gaussian_rise_negative_len"],
                "waveforms": {
                    "I": f"gaussian_rise_negative_wf_{cr_drive}_twin",
                    "Q": f"zero_wf"
                }
            }
            for cr_drive, val in CR_DRIVE_CONSTANTS.items()
        },
        **{f"gaussian_rise_positive_pulse_{cr_cancel}_twin":
            {
                "operation": "control",
                "length": val["gaussian_rise_positive_len"],
                "waveforms": {
                    "I": f"gaussian_rise_positive_wf_{cr_cancel}_twin",
                    "Q": f"zero_wf"
                }
            }
            for cr_cancel, val in CR_CANCEL_CONSTANTS.items()
        },
        **{f"gaussian_rise_negative_pulse_{cr_cancel}_twin":
            {
                "operation": "control",
                "length": val["gaussian_rise_negative_len"],
                "waveforms": {
                    "I": f"gaussian_rise_negative_wf_{cr_cancel}_twin",
                    "Q": f"zero_wf"
                }
            }
            for cr_cancel, val in CR_CANCEL_CONSTANTS.items()
        },
        **{f"gaussian_fall_positive_pulse_{cr_drive}_twin":
            {
                "operation": "control",
                "length": val["gaussian_fall_positive_len"],
                "waveforms": {
                    "I": f"gaussian_fall_positive_wf_{cr_drive}_twin",
                    "Q": f"zero_wf"
                }
            }
            for cr_drive, val in CR_DRIVE_CONSTANTS.items()
        },
        **{f"gaussian_fall_negative_pulse_{cr_drive}_twin":
            {
                "operation": "control",
                "length": val["gaussian_fall_negative_len"],
                "waveforms": {
                    "I": f"gaussian_fall_negative_wf_{cr_drive}_twin",
                    "Q": f"zero_wf"
                }
            }
            for cr_drive, val in CR_DRIVE_CONSTANTS.items()
        },
        **{f"gaussian_fall_positive_pulse_{cr_cancel}_twin":
            {
                "operation": "control",
                "length": val["gaussian_fall_positive_len"],
                "waveforms": {
                    "I": f"gaussian_fall_positive_wf_{cr_cancel}_twin",
                    "Q": f"zero_wf"
                }
            }
            for cr_cancel, val in CR_CANCEL_CONSTANTS.items()
        },
        **{f"gaussian_fall_negative_pulse_{cr_cancel}_twin":
            {
                "operation": "control",
                "length": val["gaussian_fall_negative_len"],
                "waveforms": {
                    "I": f"gaussian_fall_negative_wf_{cr_cancel}_twin",
                    "Q": f"zero_wf"
                }
            }
            for cr_cancel, val in CR_CANCEL_CONSTANTS.items()
        },**{f"square_pulse_{zz_control}":
            {
                "operation": "control",
                "length": val["square_len"],
                "waveforms": {
                    "I": f"square_wf_{zz_control}",
                    "Q": f"zero_wf"
                }
            }
            for zz_control, val in ZZ_CONTROL_CONSTANTS.items()
        },
        **{f"square_pulse_{zz_target}":
            {
                "operation": "control",
                "length": val["square_len"],
                "waveforms": {
                    "I": f"square_wf_{zz_target}",
                    "Q": f"zero_wf"
                }
            }
            for zz_target, val in ZZ_TARGET_CONSTANTS.items()
        },
        **{f"flattop_pulse_{zz_control}":
            {
                "operation": "control",
                "length": val["flattop_len"],
                "waveforms": {
                    "I": f"flattop_wf_{zz_control}",
                    "Q": f"zero_wf"
                }
            }
            for zz_control, val in ZZ_CONTROL_CONSTANTS.items()
        },
        **{f"flattop_pulse_{zz_target}":
            {
                "operation": "control",
                "length": val["flattop_len"],
                "waveforms": {
                    "I": f"flattop_wf_{zz_target}",
                    "Q": f"zero_wf"
                }
            }
            for zz_target, val in ZZ_TARGET_CONSTANTS.items()
        },
        **{f"gaussian_rise_pulse_{zz_control}_twin":
            {
                "operation": "control",
                "length": val["gaussian_rise_len"],
                "waveforms": {
                    "I": f"gaussian_rise_wf_{zz_control}_twin",
                    "Q": f"zero_wf"
                }
            }
            for zz_control, val in ZZ_CONTROL_CONSTANTS.items()
        },
        **{f"gaussian_rise_pulse_{zz_target}_twin":
            {
                "operation": "control",
                "length": val["gaussian_rise_len"],
                "waveforms": {
                    "I": f"gaussian_rise_wf_{zz_target}_twin",
                    "Q": f"zero_wf"
                }
            }
            for zz_target, val in ZZ_TARGET_CONSTANTS.items()
        },
        **{f"gaussian_fall_pulse_{zz_control}_twin":
            {
                "operation": "control",
                "length": val["gaussian_fall_len"],
                "waveforms": {
                    "I": f"gaussian_fall_wf_{zz_control}_twin",
                    "Q": f"zero_wf"
                }
            }
            for zz_control, val in ZZ_CONTROL_CONSTANTS.items()
        },
        **{f"gaussian_fall_pulse_{zz_target}_twin":
            {
                "operation": "control",
                "length": val["gaussian_fall_len"],
                "waveforms": {
                    "I": f"gaussian_fall_wf_{zz_target}_twin",
                    "Q": f"zero_wf"
                }
            }
            for zz_target, val in ZZ_TARGET_CONSTANTS.items()
        },
        **{
            f"readout_pulse_{rr}": {
                "operation": "measurement",
                "length": val["readout_len"],
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
            } for rr, val in RR_CONSTANTS.items()
        },
        **{
            f"midcircuit_readout_pulse_{rr}": {
                "operation": "measurement",
                "length": val["midcircuit_readout_len"],
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
            } for rr, val in RR_CONSTANTS.items()
        },
    },
    "waveforms": {
        "const_wf": {"type": "constant", "sample": CONST_AMP},
        "saturation_wf": {"type": "constant", "sample": SATURATION_AMP},
        "zero_wf": {"type": "constant", "sample": 0.0},
        **{f"readout_wf_{rr}": {"type": "constant", "sample": val["readout_amp"]} for rr, val in RR_CONSTANTS.items()},
        **{f"midcircuit_readout_wf_{rr}": {"type": "constant", "sample": val["midcircuit_readout_amp"]} for rr, val in RR_CONSTANTS.items()},
        **{f"x90_I_wf_{qb}": {"type": "arbitrary", "samples": waveforms[f"{qb}_x90_I"].tolist()} for qb in QUBIT_CONSTANTS.keys()},
        **{f"x90_Q_wf_{qb}": {"type": "arbitrary", "samples": waveforms[f"{qb}_x90_Q"].tolist()} for qb in QUBIT_CONSTANTS.keys()},
        **{f"x180_I_wf_{qb}": {"type": "arbitrary", "samples": waveforms[f"{qb}_x180_I"].tolist()} for qb in QUBIT_CONSTANTS.keys()},
        **{f"x180_Q_wf_{qb}": {"type": "arbitrary", "samples": waveforms[f"{qb}_x180_Q"].tolist()} for qb in QUBIT_CONSTANTS.keys()},
        **{f"minus_x90_I_wf_{qb}": {"type": "arbitrary", "samples": waveforms[f"{qb}_minus_x90_I"].tolist()} for qb in QUBIT_CONSTANTS.keys()},
        **{f"minus_x90_Q_wf_{qb}": {"type": "arbitrary", "samples": waveforms[f"{qb}_minus_x90_Q"].tolist()} for qb in QUBIT_CONSTANTS.keys()},
        **{f"y90_I_wf_{qb}": {"type": "arbitrary", "samples": waveforms[f"{qb}_y90_I"].tolist()} for qb in QUBIT_CONSTANTS.keys()},
        **{f"y90_Q_wf_{qb}": {"type": "arbitrary", "samples": waveforms[f"{qb}_y90_Q"].tolist()} for qb in QUBIT_CONSTANTS.keys()},
        **{f"y180_I_wf_{qb}": {"type": "arbitrary", "samples": waveforms[f"{qb}_y180_I"].tolist()} for qb in QUBIT_CONSTANTS.keys()},
        **{f"y180_Q_wf_{qb}": {"type": "arbitrary", "samples": waveforms[f"{qb}_y180_Q"].tolist()} for qb in QUBIT_CONSTANTS.keys()},
        **{f"minus_y90_I_wf_{qb}": {"type": "arbitrary", "samples": waveforms[f"{qb}_minus_y90_I"].tolist()} for qb in QUBIT_CONSTANTS.keys()},
        **{f"minus_y90_Q_wf_{qb}": {"type": "arbitrary", "samples": waveforms[f"{qb}_minus_y90_Q"].tolist()} for qb in QUBIT_CONSTANTS.keys()},
        **{f"square_positive_wf_{cr_drive}": {"type": "constant", "sample": val["square_positive_amp"]} for cr_drive, val in CR_DRIVE_CONSTANTS.items()},
        **{f"square_negative_wf_{cr_drive}": {"type": "constant", "sample": val["square_negative_amp"]} for cr_drive, val in CR_DRIVE_CONSTANTS.items()},
        **{f"square_positive_wf_{cr_cancel}": {"type": "constant", "sample": val["square_positive_amp"]} for cr_cancel, val in CR_CANCEL_CONSTANTS.items()},
        **{f"square_negative_wf_{cr_cancel}": {"type": "constant", "sample": val["square_negative_amp"]} for cr_cancel, val in CR_CANCEL_CONSTANTS.items()},
        **{f"flattop_positive_wf_{cr_drive}": {"type": "constant", "sample": val["flattop_positive_amp"]} for cr_drive, val in CR_DRIVE_CONSTANTS.items()},
        **{f"flattop_negative_wf_{cr_drive}": {"type": "constant", "sample": val["flattop_negative_amp"]} for cr_drive, val in CR_DRIVE_CONSTANTS.items()},
        **{f"flattop_positive_wf_{cr_cancel}": {"type": "constant", "sample": val["flattop_positive_amp"]} for cr_cancel, val in CR_CANCEL_CONSTANTS.items()},
        **{f"flattop_negative_wf_{cr_cancel}": {"type": "constant", "sample": val["flattop_negative_amp"]} for cr_cancel, val in CR_CANCEL_CONSTANTS.items()},
        **{f"gaussian_rise_positive_wf_{cr_drive}_twin": {"type": "arbitrary", "samples": [0] * val["gaussian_rise_positive_pad_len"] + flattop_gaussian_waveform(val["gaussian_rise_positive_amp"], CR_DRIVE_FLATTOP_LEN, val["gaussian_rise_positive_len"], return_part="rise")} for cr_drive, val in CR_DRIVE_CONSTANTS.items()},
        **{f"gaussian_rise_negative_wf_{cr_drive}_twin": {"type": "arbitrary", "samples": [0] * val["gaussian_rise_negative_pad_len"] + flattop_gaussian_waveform(val["gaussian_rise_negative_amp"], CR_DRIVE_FLATTOP_LEN, val["gaussian_rise_negative_len"], return_part="rise")} for cr_drive, val in CR_DRIVE_CONSTANTS.items()},
        **{f"gaussian_rise_positive_wf_{cr_cancel}_twin": {"type": "arbitrary", "samples": [0] * val["gaussian_rise_positive_pad_len"] + flattop_gaussian_waveform(val["gaussian_rise_positive_amp"], CR_CANCEL_FLATTOP_LEN, val["gaussian_rise_positive_len"], return_part="rise")} for cr_cancel, val in CR_CANCEL_CONSTANTS.items()},
        **{f"gaussian_rise_negative_wf_{cr_cancel}_twin": {"type": "arbitrary", "samples": [0] * val["gaussian_rise_negative_pad_len"] + flattop_gaussian_waveform(val["gaussian_rise_negative_amp"], CR_CANCEL_FLATTOP_LEN, val["gaussian_rise_negative_len"], return_part="rise")} for cr_cancel, val in CR_CANCEL_CONSTANTS.items()},
        **{f"gaussian_fall_positive_wf_{cr_drive}_twin": {"type": "arbitrary", "samples": flattop_gaussian_waveform(val["gaussian_fall_positive_amp"], CR_DRIVE_FLATTOP_LEN, val["gaussian_fall_positive_len"], return_part="fall") + [0] * val["gaussian_fall_positive_pad_len"]} for cr_drive, val in CR_DRIVE_CONSTANTS.items()},
        **{f"gaussian_fall_negative_wf_{cr_drive}_twin": {"type": "arbitrary", "samples": flattop_gaussian_waveform(val["gaussian_fall_negative_amp"], CR_DRIVE_FLATTOP_LEN, val["gaussian_fall_negative_len"], return_part="fall") + [0] * val["gaussian_fall_negative_pad_len"]} for cr_drive, val in CR_DRIVE_CONSTANTS.items()},
        **{f"gaussian_fall_positive_wf_{cr_cancel}_twin": {"type": "arbitrary", "samples": flattop_gaussian_waveform(val["gaussian_fall_positive_amp"], CR_CANCEL_FLATTOP_LEN, val["gaussian_fall_positive_len"], return_part="fall") + [0] * val["gaussian_fall_positive_pad_len"]} for cr_cancel, val in CR_CANCEL_CONSTANTS.items()},
        **{f"gaussian_fall_negative_wf_{cr_cancel}_twin": {"type": "arbitrary", "samples": flattop_gaussian_waveform(val["gaussian_fall_negative_amp"], CR_CANCEL_FLATTOP_LEN, val["gaussian_fall_negative_len"], return_part="fall") + [0] * val["gaussian_fall_negative_pad_len"]} for cr_cancel, val in CR_CANCEL_CONSTANTS.items()},
        **{f"square_wf_{zz_control}": {"type": "constant", "sample": val["square_amp"]} for zz_control, val in ZZ_CONTROL_CONSTANTS.items()},
        **{f"square_wf_{zz_target}": {"type": "constant", "sample": val["square_amp"]} for zz_target, val in ZZ_TARGET_CONSTANTS.items()},
        **{f"flattop_wf_{zz_control}": {"type": "constant", "sample": val["flattop_amp"]} for zz_control, val in ZZ_CONTROL_CONSTANTS.items()},
        **{f"flattop_wf_{zz_target}": {"type": "constant", "sample": val["flattop_amp"]} for zz_target, val in ZZ_TARGET_CONSTANTS.items()},
        **{f"gaussian_rise_wf_{zz_control}_twin": {"type": "arbitrary", "samples": [0] * val["gaussian_rise_pad_len"] + flattop_gaussian_waveform(val["gaussian_rise_amp"], CR_DRIVE_FLATTOP_LEN, val["gaussian_rise_len"], return_part="rise")} for zz_control, val in ZZ_CONTROL_CONSTANTS.items()},
        **{f"gaussian_rise_wf_{zz_target}_twin": {"type": "arbitrary", "samples": [0] * val["gaussian_rise_pad_len"] + flattop_gaussian_waveform(val["gaussian_rise_amp"], CR_CANCEL_FLATTOP_LEN, val["gaussian_rise_len"], return_part="rise")} for zz_target, val in ZZ_TARGET_CONSTANTS.items()},
        **{f"gaussian_fall_wf_{zz_control}_twin": {"type": "arbitrary", "samples": flattop_gaussian_waveform(val["gaussian_fall_amp"], CR_DRIVE_FLATTOP_LEN, val["gaussian_fall_len"], return_part="fall") + [0] * val["gaussian_fall_pad_len"]} for zz_control, val in ZZ_CONTROL_CONSTANTS.items()},
        **{f"gaussian_fall_wf_{zz_target}_twin": {"type": "arbitrary", "samples": flattop_gaussian_waveform(val["gaussian_fall_amp"], CR_CANCEL_FLATTOP_LEN, val["gaussian_fall_len"], return_part="fall") + [0] * val["gaussian_fall_pad_len"]} for zz_target, val in ZZ_TARGET_CONSTANTS.items()},
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
                "cosine": [(np.cos(val["midcircuit_readout_rotation_angle"])), READOUT_LEN],
                "sine": [(np.sin(val["midcircuit_readout_rotation_angle"])), READOUT_LEN]
            } for rr, val in RR_CONSTANTS.items()
        },
        **{
            f"midcircuit_rotated_sine_weights_{rr}": {
                "cosine": [(-np.sin(val["midcircuit_readout_rotation_angle"])), READOUT_LEN],
                "sine": [(np.cos(val["midcircuit_readout_rotation_angle"])), READOUT_LEN]
            } for rr, val in RR_CONSTANTS.items()
        },
        **{
            f"midcircuit_rotated_minus_sine_weights_{rr}": {
                "cosine": [(np.sin(val["midcircuit_readout_rotation_angle"])), READOUT_LEN],
                "sine": [(-np.cos(val["midcircuit_readout_rotation_angle"])), READOUT_LEN]
            } for rr, val in RR_CONSTANTS.items()
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
    },
}

# %%