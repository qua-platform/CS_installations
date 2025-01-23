# %%
"""
QUA-Config supporting OPX1000 w/ LF-FEM & External Mixers
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
qop_ip = "192.168.1.41"  # Write the QM router IP address
# cluster_name = "Cluster_1"  # Write your cluster_name if version >= QOP220
# qop_ip = "172.16.33.107"  # Write the QM router IP address
cluster_name = "Cluster_1"  # "Beta_8"  # Write your cluster_name if version >= QOP220
# qop_ip = "192.168.88.253"  # Write the QM router IP address
# cluster_name = "Cluster_1"  # Write your cluster_name if version >= QOP220
qop_port = 9510  # Write the QOP port if version < QOP220
octave_config = None


#############
# Save Path #
#############

# Path to save data
save_dir = Path().absolute() / "data"
save_dir.mkdir(exist_ok=True)
default_additional_files = {
    "configuration_with_lffem.py": "configuration_with_lffem.py",
}


#####################
# OPX configuration #
#####################
con1 = "con1"
lffem1 = 4  # Should be the LF-FEM index, e.g., 1
lffem2 = 2  # Should be the LF-FEM index, e.g., 1
lffem3 = 3  # Should be the LF-FEM index, e.g., 1


#############################################
#              OPX PARAMETERS               #
#############################################
sampling_rate = int(1e9)  # or, int(2e9)


############################################
#              VIRTUAL GATES               #
############################################

VIRTUALIZATION_MATRIX = np.array(
    [
        [1.0, -0.1],
        [-0.1, 1.0],
    ]
)
STEP_LEN = 1000
STEP_AMP = 0.25

amplitude_scaling = 4.7
LEVEL_INIT = [-0.094, +0.094] # [-0.02, 0.02] * amplitude_scaling
LEVEL_READOUT = [0.00161, -0.0018]


#########################
#    DIGITAL TRIGGER    #
#########################

RF_SWITCH_DELAY = 200
rf_switch_delay = 0
rf_switch_buffer = 0


#########################
#    1Q QUBIT PULSES    #
#########################

# CW pulse
CONST_AMP = 0.3  # in V
CONST_LEN = 320  # in ns

# Saturation pulse
SATURATION_AMP = 0.1
SATURATION_LEN = 10_000

SQUARE_X180_AMP = 0.40
SQUARE_X90_AMP = 0.20
SQUARE_MINUS_X90_AMP = -0.20
SQUARE_Y180_AMP = 0.3
SQUARE_Y90_AMP = 0.15
SQUARE_MINUS_Y90_AMP = -0.15
SQUARE_LEN = 1000 # 52

PI_AMP = 0.3
PI_LEN = 160 # 52
PI_HALF_AMP = PI_AMP / 2
PI_HALF_LEN = PI_LEN
# PI_SIGMA = PI_LEN / 5


#########################
#    @Q QUBIT PULSES    #
#########################

qubit_pairs = [
    ["3", "2"],
]

CROT_DC_AMP = 0.1
CROT_DC_LEN = 100
CROT_PI_AMP = 0.1
CROT_PI_LEN = CROT_DC_LEN
CROT_PI_HALF_AMP = CROT_PI_AMP / 2
CROT_PI_HALF_LEN = CROT_PI_LEN
# CROT_RF_SIGMA = CROT_RF_LEN / 5


########################
#    REFELECTOMETRY    #
########################

REFLECTOMETRY_READOUT_AMP = 0.15
REFLECTOMETRY_READOUT_LEN = 20_000

PARITY_THRESHOLD1 = -0.0335
PARITY_THRESHOLD2 = 0.0


######################
#      DC GATES      #
######################

# Time to ramp down to zero for sticky elements in ns
hold_offset_duration = 4  # in ns
bias_tee_cut_off_frequency = 10 * u.kHz


#################
#   CONSTANTS   #
#################

# MARK: ONE QUBIT

QUBIT_CONSTANTS = {
    "qubit1": {
        "con": con1,
        "fem": lffem1,
        "aout_I": 1,
        "aout_Q": 2,
        "LO": 16 * u.GHz,
        "IF": (167.432) * u.MHz,
        "mixer_g": 0,
        "mixer_phi": 0.201,
        "square_pi_amp": 0.30671,
        "square_pi_len": 248,
        "square_pi_half_amp": 0.30671,
        "square_pi_half_len": 248,
        "kaiser_pi_amp": 0.446,
        "kaiser_pi_len": 280,
        "kaiser_pi_half_amp": 0.446,
        "kaiser_pi_half_len": 280,
        "gauss_pi_amp": 0.446,
        "gauss_pi_len": 280,
        "gauss_pi_half_amp": 0.446,
        "gauss_pi_half_len": 280,
        "delay": 0,
    },
    "qubit2": {
        "con": con1,
        "fem": lffem1,
        "aout_I": 1,
        "aout_Q": 2,
        "LO": 16 * u.GHz,
        "IF": 31.5 * u.MHz,
        "mixer_g": 0,
        "mixer_phi": 1.365,
        "square_pi_amp": 0.1567 * 252 / 250,
        "square_pi_len": 248,
        "square_pi_half_amp": 0.1567 * 252 / 250,
        "square_pi_half_len": 248,
        "kaiser_pi_amp": PI_AMP,
        "kaiser_pi_len": PI_LEN,
        "kaiser_pi_half_amp": PI_HALF_AMP,
        "kaiser_pi_half_len": PI_HALF_LEN,
        "gauss_pi_amp": PI_AMP,
        "gauss_pi_len": PI_LEN,
        "gauss_pi_half_amp": PI_HALF_AMP,
        "gauss_pi_half_len": PI_HALF_LEN,
        "delay": 0,
    },
    "qubit3": {
        "con": con1,
        "fem": lffem1,
        "aout_I": 3,
        "aout_Q": 4,
        "LO": 16.3 * u.GHz,
        "IF": 0 * u.MHz,
        "mixer_g": 0,
        "mixer_phi": 0,
        "square_pi_amp": PI_AMP,
        "square_pi_len": PI_LEN,
        "square_pi_half_amp": PI_HALF_AMP,
        "square_pi_half_len": PI_HALF_LEN,
        "kaiser_pi_amp": PI_AMP,
        "kaiser_pi_len": PI_LEN,
        "kaiser_pi_half_amp": PI_HALF_AMP,
        "kaiser_pi_half_len": PI_HALF_LEN,
        "gauss_pi_amp": PI_AMP,
        "gauss_pi_len": PI_LEN,
        "gauss_pi_half_amp": PI_HALF_AMP,
        "gauss_pi_half_len": PI_HALF_LEN,
        "delay": 0,
    },
    "qubit4": {
        "con": con1,
        "fem": lffem1,
        "aout_I": 3,  # TODO: Fix
        "aout_Q": 4,  # TODO: Fix
        "LO": 16.3 * u.GHz,
        "IF": 50 * u.MHz,
        "mixer_g": 0,
        "mixer_phi": 0,
        "square_pi_amp": PI_AMP,
        "square_pi_len": PI_LEN,
        "square_pi_half_amp": PI_HALF_AMP,
        "square_pi_half_len": PI_HALF_LEN,
        "kaiser_pi_amp": PI_AMP,
        "kaiser_pi_len": PI_LEN,
        "kaiser_pi_half_amp": PI_HALF_AMP,
        "kaiser_pi_half_len": PI_HALF_LEN,
        "gauss_pi_amp": PI_AMP,
        "gauss_pi_len": PI_LEN,
        "gauss_pi_half_amp": PI_HALF_AMP,
        "gauss_pi_half_len": PI_HALF_LEN,
        "delay": 0,
    },
    "qubit5": {
        "con": con1,
        "fem": lffem1,
        "aout_I": 5,  # TODO: Fix
        "aout_Q": 6,  # TODO: Fix
        "LO": 16.3 * u.GHz,
        "IF": 0 * u.MHz,
        "mixer_g": 0,
        "mixer_phi": 0,
        "square_pi_amp": PI_AMP,
        "square_pi_len": PI_LEN,
        "square_pi_half_amp": PI_HALF_AMP,
        "square_pi_half_len": PI_HALF_LEN,
        "kaiser_pi_amp": PI_AMP,
        "kaiser_pi_len": PI_LEN,
        "kaiser_pi_half_amp": PI_HALF_AMP,
        "kaiser_pi_half_len": PI_HALF_LEN,
        "gauss_pi_amp": PI_AMP,
        "gauss_pi_len": PI_LEN,
        "gauss_pi_half_amp": PI_HALF_AMP,
        "gauss_pi_half_len": PI_HALF_LEN,
        "delay": 0,
    },
}

DO_CONSTANTS = {
    "rf_switch": {
        "con": con1,
        "fem": lffem1,
        "dout": 1,
        "aout": 1,
        "delay": rf_switch_delay,
        "buffer": rf_switch_buffer,
    },
}

PLUNGER_CONSTANTS = {
    "P0": {
        "con": con1,
        "fem": lffem2,
        "ao": 1,
        "step_amp": STEP_AMP,
        "step_len": STEP_LEN,
        "delay": 0,
    },
    "P1": {
        "con": con1,
        "fem": lffem2,
        "ao": 3,
        "step_amp": STEP_AMP,
        "step_len": STEP_LEN,
        "delay": 0,
    },
    "P2": {
        "con": con1,
        "fem": lffem2,
        "ao": 5,
        "step_amp": STEP_AMP,
        "step_len": STEP_LEN,
        "delay": 0,
    },
    "P3": {
        "con": con1,
        "fem": lffem2,  # TODO: Fix
        "ao": 7,  # TODO: Fix
        "step_amp": STEP_AMP,
        "step_len": STEP_LEN,
        "delay": 0,
    },
    "P4": {
        "con": con1,
        "fem": lffem3,  # TODO: Fix
        "ao": 1,  # TODO: Fix
        "step_amp": STEP_AMP,
        "step_len": STEP_LEN,
        "delay": 0,
    },
}

BARRIER_CONSTANTS = {
    "B1": {
        "con": con1,
        "fem": lffem2,
        "ao": 2,
        "step_amp": STEP_AMP,
        "step_len": STEP_LEN,
        "delay": 0,
    },
    "B2": {
        "con": con1,
        "fem": lffem2,
        "ao": 4,
        "step_amp": STEP_AMP,
        "step_len": STEP_LEN,
        "delay": 0,
    },
    "B3": {
        "con": con1,
        "fem": lffem2,
        "ao": 6,
        "step_amp": STEP_AMP,
        "step_len": STEP_LEN,
        "delay": 0,
    },
    "B4": {
        "con": con1,
        "fem": lffem2,  # TODO: Fix
        "ao": 8,  # TODO: Fix
        "step_amp": STEP_AMP,
        "step_len": STEP_LEN,
        "delay": 0,
    },
}

PLUNGER_SD_CONSTANTS = {
    "Psd1": {
        "con": con1,
        "fem": lffem3,
        "ao": 2,
        "step_amp": STEP_AMP,
        "step_len": STEP_LEN,
        "delay": 0,
    },
    "Psd2": {
        "con": con1,
        "fem": lffem3,
        "ao": 3,
        "step_amp": STEP_AMP,
        "step_len": STEP_LEN,
        "delay": 0,
    },
}

TANK_CIRCUIT_CONSTANTS = {
    "tank_circuit1": {
        "con": con1,
        "fem": lffem3,
        "ao": 8,
        "ai": 2,
        "IF": 181.02 * u.MHz,
        "readout_amp": REFLECTOMETRY_READOUT_AMP,
        "readout_len": REFLECTOMETRY_READOUT_LEN,
        "threshold": PARITY_THRESHOLD1,
        "time_of_flight": 24 + 180,
        "delay": 0,
    },
    "tank_circuit2": {
        "con": con1,
        "fem": lffem3,
        "ao": 8,
        "ai": 2,
        "IF": 139.534 * u.MHz,
        "readout_amp": REFLECTOMETRY_READOUT_AMP,
        "readout_len": REFLECTOMETRY_READOUT_LEN,
        "threshold": PARITY_THRESHOLD2,
        "time_of_flight": 24 + 180,
        "delay": 0,
    },
}

# MARK: TWO QUBIT


# Constants for each qubit for CR DRIVE
CROT_CONSTANTS = {
    **{
        f"qp_control_c{c}t{t}": {
            "con": QUBIT_CONSTANTS[f"qubit{c}"]["con"],
            "fem": QUBIT_CONSTANTS[f"qubit{c}"]["fem"],
            "aout_I": QUBIT_CONSTANTS[f"qubit{c}"]["aout_I"],
            "aout_Q": QUBIT_CONSTANTS[f"qubit{c}"]["aout_Q"],
            "LO": QUBIT_CONSTANTS[f"qubit{c}"]["LO"],
            "IF": QUBIT_CONSTANTS[f"qubit{c}"]["IF"],
            "mixer_g": QUBIT_CONSTANTS[f"qubit{c}"]["mixer_g"],
            "mixer_phi": QUBIT_CONSTANTS[f"qubit{c}"]["mixer_phi"],
            "square_pi_amp": CROT_PI_AMP,
            "square_pi_len": CROT_PI_LEN,
            "square_pi_half_amp": CROT_PI_HALF_AMP,
            "square_pi_half_len": CROT_PI_HALF_LEN,
            "kaiser_pi_amp": CROT_PI_AMP,
            "kaiser_pi_len": CROT_PI_LEN,
            "kaiser_pi_half_amp": CROT_PI_HALF_AMP,
            "kaiser_pi_half_len": CROT_PI_HALF_LEN,
            "gauss_pi_amp": CROT_PI_AMP,
            "gauss_pi_len": CROT_PI_LEN,
            "gauss_pi_half_amp": CROT_PI_HALF_AMP,
            "gauss_pi_half_len": CROT_PI_HALF_LEN,
        }
        for c, t in qubit_pairs
    }
}
# # update after findng the optimal parameters
# CROT_CONSTANTS["qp_control_c3t2"]["square_pi_amp"] = 0.1
# CROT_CONSTANTS["qp_control_c3t2"]["square_pi_len"] = 100
# CROT_CONSTANTS["qp_control_c3t2"]["square_pi_half_amp"] = 0.05
# CROT_CONSTANTS["qp_control_c3t2"]["square_pi_half_amp"] = 100


#########################
#  GATE VIRTUALIZATION  #
#########################

from collections import OrderedDict

MAP_GATE_TO_IDX = OrderedDict(
    [
        ("P0", 0),
        ("P1", 1),
        ("P2", 2),
        ("B1", 3),
        ("B2", 4),
        ("B3", 5),
        ("Psd1", 6),
        ("Psd2", 7),
    ]
)

NUM_VGs = len(MAP_GATE_TO_IDX)
A = np.random.rand(NUM_VGs, NUM_VGs)
CROSSTALK_MATRIX = 0.1 * (A + A.T) / 2
np.fill_diagonal(CROSSTALK_MATRIX, 1)
INV_CROSSTALK_MATARIX = np.linalg.inv(CROSSTALK_MATRIX)

INV_CROSSTALK_MATARIX = np.array(
    [
        [1.03, -0.03, -0.06, -0.06, -0.05, -0.07, -0.03, -0.02, -0.05, -0.07, -0.03],
        [-0.03, 1.03, -0.06, -0.05, 0.01, -0.05, -0.05, -0.03, -0.06, -0.01, -0.04],
        [-0.06, -0.06, 1.02, -0.03, -0.03, 0.01, -0.01, -0.05, -0.02, -0.06, 0.00],
        [-0.06, -0.05, -0.03, 1.03, -0.03, -0.07, -0.01, 0.00, -0.03, -0.05, -0.06],
        [-0.05, 0.01, -0.03, -0.03, 1.02, -0.04, -0.00, -0.05, -0.04, -0.02, -0.03],
        [-0.07, -0.05, 0.01, -0.07, -0.04, 1.03, 0.00, -0.02, -0.03, -0.06, -0.03],
        [-0.03, -0.05, -0.01, -0.01, -0.00, 0.00, 1.02, -0.05, -0.03, -0.05, -0.06],
        [-0.02, -0.03, -0.05, 0.00, -0.05, -0.02, -0.05, 1.03, -0.07, -0.06, -0.05],
        [-0.05, -0.06, -0.02, -0.03, -0.04, -0.03, -0.03, -0.07, 1.02, -0.02, -0.02],
        [-0.07, -0.01, -0.06, -0.05, -0.02, -0.06, -0.05, -0.06, -0.02, 1.03, -0.01],
        [-0.03, -0.04, 0.00, -0.06, -0.03, -0.03, -0.06, -0.05, -0.02, -0.01, 1.02],
    ]
)


import copy

from qm.qua import *
from qm.qua._expressions import QuaVariable


class GateVirtualizer:
    MAP_GATE_TO_IDX = MAP_GATE_TO_IDX
    INV_CROSSTALK_MATARIX = INV_CROSSTALK_MATARIX

    def __init__(self):
        # Initialize the mapping of gates to indices
        self.num_vgs = len(MAP_GATE_TO_IDX)
        self.g2i = copy.deepcopy(GateVirtualizer.MAP_GATE_TO_IDX)

    def generate_virtual_voltages(
        self,
        gates: list[str],
        Vs_real: list[QuaVariable],
        Vs_virtual: list[QuaVariable],
    ):
        assert len(gates) == len(Vs_real), "length of gates and Vs_real must be the same"

        for g1, idx1 in self.g2i.items():
            for g2, v2 in zip(gates, Vs_real):
                idx2 = self.g2i[g2]
                assign(Vs_virtual[idx1], GateVirtualizer.INV_CROSSTALK_MATARIX[idx2, idx1] * v2)

        return Vs_virtual


########################
#  Pi pulse waveforms  #
########################

# from scipy.special import i0  # Zeroth-order modified Bessel function of the first kind
from scipy.signal.windows import \
    kaiser  # Zeroth-order modified Bessel function of the first kind

# def kaiser_window(T: int, alpha: float) -> np.ndarray:
#     """
#     Generate a Kaiser window for digital signal processing.

#     :param T: Length of the window (number of points - 1).
#     :param alpha: Shape parameter that determines the trade-off between main lobe width and side lobe level.
#     :return: A numpy array of the Kaiser window values.
#     """
#     # Compute the normalized indices
#     t = np.arange(T)
#     x = (2 * t / (T - 1)) - 1

#     # Calculate the Kaiser window using the zeroth-order modified Bessel function
#     window = 1.6 * kaiser(np.pi * alpha * np.sqrt(1 - x**2)) / (np.pi * alpha)

#     return window


def generate_waveforms(rotation_keys):
    """Generate all necessary waveforms for a set of rotation types across all qubits."""

    def compute_and_update_waveform(waveforms, rotation_key, qubit, wf_name, wf_amp, wf_len):
        zero_len = 2

        if wf_name == "gauss":
            wf_sigma = (wf_len - zero_len) / 5
            wf, der_wf = np.array(drag_gaussian_pulse_waveforms(wf_amp, wf_len - zero_len, wf_sigma, alpha=0, anharmonicity=0))
        elif wf_name == "kaiser":
            wf = wf_amp * kaiser(wf_len - zero_len, beta=8.0)
            # wf = wf_amp * kaiser_window(wf_len - zero_len, alpha=4.0)
            der_wf = np.array([0] * (wf_len - zero_len))
        elif wf_name == "square":
            wf = np.array([wf_amp] * (wf_len - zero_len))
            der_wf = np.array([0] * (wf_len - zero_len))
        else:
            raise ValueError(f'{wf_name} is passed. wf_name must be one of ["gauss", "kaiser", "square]')


        if rotation_key in ["x180", "x90", "minus_x90"]:
            I_wf = wf
            Q_wf = der_wf
        elif rotation_key in ["y180", "y90", "minus_y90"]:
            I_wf = (-1) * der_wf
            Q_wf = wf
        else:
            raise ValueError(f'{rotation_key} is passed. rotation_key must be one of ["x180", "x90", "minus_x90", "y180", "y90", "minus_y90"]')

        waveforms[f"{qubit}_{wf_name}_{rotation_key}_I"] = I_wf.tolist() + [0] * zero_len
        waveforms[f"{qubit}_{wf_name}_{rotation_key}_Q"] = Q_wf.tolist() + [0] * zero_len

        return waveforms

    if not isinstance(rotation_keys, list):
        raise ValueError("rotation_keys must be a list")

    waveforms = {}
    for rk in rotation_keys:
        if rk in ["x180", "y180"]:
            for qubit, constants in {**QUBIT_CONSTANTS, **CROT_CONSTANTS}.items():
                waveforms = compute_and_update_waveform(waveforms, rk, qubit, "gauss", constants["gauss_pi_amp"], constants["gauss_pi_len"])
                waveforms = compute_and_update_waveform(waveforms, rk, qubit, "kaiser", constants["kaiser_pi_amp"], constants["kaiser_pi_len"])
                waveforms = compute_and_update_waveform(waveforms, rk, qubit, "square", constants["square_pi_amp"], constants["square_pi_len"])

        if rk in ["x90", "minus_x90", "y90", "minus_y90"]:
            for qubit, constants in {**QUBIT_CONSTANTS, **CROT_CONSTANTS}.items():
                waveforms = compute_and_update_waveform(waveforms, rk, qubit, "gauss", constants["gauss_pi_half_amp"], constants["gauss_pi_half_len"])
                waveforms = compute_and_update_waveform(waveforms, rk, qubit, "kaiser", constants["kaiser_pi_half_amp"], constants["kaiser_pi_half_len"])
                waveforms = compute_and_update_waveform(waveforms, rk, qubit, "square", constants["square_pi_half_amp"], constants["square_pi_half_len"])

    return waveforms


rotation_keys = ["x180", "x90", "minus_x90", "y180", "y90", "minus_y90"]
waveforms = generate_waveforms(rotation_keys)


# MARK: CONFIG
#############################################
#                  Config                   #
#############################################
config = {
    "version": 1,
    "controllers": {
        con1: {
            "type": "opx1000",
            "fems": {
                lffem1: {
                    "type": "LF",
                    "analog_outputs": {
                        # EDSR I1 (q1)
                        1: {
                            # DC Offset applied to the analog output at the beginning of a program.
                            "offset": 0.0,
                            # The "output_mode" can be used to tailor the max voltage and frequency bandwidth, i.e.,
                            #   "direct":    1Vpp (-0.5V to 0.5V), 750MHz bandwidth (default)
                            #   "direct": 5Vpp (-2.5V to 2.5V), 330MHz bandwidth
                            "output_mode": "direct",
                            # The "sampling_rate" can be adjusted by using more FEM cores, i.e.,
                            #   1 GS/s: uses one core per output (default)
                            #   2 GS/s: uses two cores per output
                            # NOTE: duration parameterization of arb. waveforms, sticky elements and chirping
                            #       aren't yet supported in 2 GS/s.
                            "sampling_rate": sampling_rate,
                            # At 1 GS/s, use the "upsampling_mode" to optimize output for
                            #   modulated pulses (optimized for modulated pulses):      "mw"    (default)
                            #   unmodulated pulses (optimized for clean step response): "pulse"
                            "upsampling_mode": "mw",
                        },
                        # EDSR Q1 (q1)
                        2: {
                            "offset": 0.0,
                            "output_mode": "direct",
                            "sampling_rate": sampling_rate,
                            "upsampling_mode": "mw",
                        },
                        # EDSR I2 (q2)
                        3: {
                            "offset": 0.0,
                            "output_mode": "direct",
                            "sampling_rate": sampling_rate,
                            "upsampling_mode": "mw",
                        },
                        # EDSR Q2 (q2)
                        4: {
                            "offset": 0.0,
                            "output_mode": "direct",
                            "sampling_rate": sampling_rate,
                            "upsampling_mode": "mw",
                        },
                        # EDSR I3 (q3)
                        5: {
                            "offset": 0.0,
                            "output_mode": "direct",
                            "sampling_rate": sampling_rate,
                            "upsampling_mode": "mw",
                        },
                        # EDSR Q3 (q3)
                        6: {
                            "offset": 0.0,
                            "output_mode": "direct",
                            "sampling_rate": sampling_rate,
                            "upsampling_mode": "mw",
                        },
                        # Psd2
                        7: {
                            "offset": 0.0,
                            "output_mode": "direct",
                            "sampling_rate": sampling_rate,
                            "upsampling_mode": "pulse",
                        },
                    },
                    "digital_outputs": {
                        1: {},  # TTL for RF
                    },
                    "analog_inputs": {
                    },
                },
                lffem2: {
                    "type": "LF",
                    "analog_outputs": {
                        # P0
                        1: {
                            "offset": 0.0,
                            "output_mode": "direct",
                            "sampling_rate": sampling_rate,
                            "upsampling_mode": "pulse",
                        },
                        # B1
                        2: {
                            "offset": 0.0,
                            "output_mode": "direct",
                            "sampling_rate": sampling_rate,
                            "upsampling_mode": "pulse",
                        },
                        # P1
                        3: {
                            "offset": 0.0,
                            "output_mode": "direct",
                            "sampling_rate": sampling_rate,
                            "upsampling_mode": "pulse",
                        },
                        # B2
                        4: {
                            "offset": 0.0,
                            "output_mode": "direct",
                            "sampling_rate": sampling_rate,
                            "upsampling_mode": "pulse",
                        },
                        # P2
                        5: {
                            "offset": 0.0,
                            "output_mode": "direct",
                            "sampling_rate": sampling_rate,
                            "upsampling_mode": "pulse",
                        },
                        # B3
                        6: {
                            "offset": 0.0,
                            "output_mode": "direct",
                            "sampling_rate": sampling_rate,
                            "upsampling_mode": "pulse",
                        },
                        # P3
                        7: {
                            "offset": 0.0,
                            "output_mode": "direct",
                            "sampling_rate": sampling_rate,
                            "upsampling_mode": "pulse",
                        },
                        # B4
                        8: {
                            "offset": 0.0,
                            "output_mode": "direct",
                            "sampling_rate": sampling_rate,
                            "upsampling_mode": "pulse",
                        },
                    },
                    "digital_outputs": {},
                    "analog_inputs": {},
                },
                lffem3: {
                    "type": "LF",
                    "analog_outputs": {
                        # P4
                        1: {
                            "offset": 0.0,
                            "output_mode": "direct",
                            "sampling_rate": sampling_rate,
                            "upsampling_mode": "pulse",
                        },
                        # Psd1
                        2: {
                            "offset": 0.0,
                            "output_mode": "direct",
                            "sampling_rate": sampling_rate,
                            "upsampling_mode": "pulse",
                        },
                        # Psd2
                        3: {
                            "offset": 0.0,
                            "output_mode": "direct",
                            "sampling_rate": sampling_rate,
                            "upsampling_mode": "pulse",
                        },
                        # Reflectometry out
                        8: {
                            "offset": 0.0,
                            "output_mode": "direct",
                            "sampling_rate": sampling_rate,
                            "upsampling_mode": "pulse",
                        },
                    },
                    "digital_outputs": {},
                    "analog_inputs": {
                        # Reflectometry in
                        2: {
                            "offset": -0.007773877929687499,
                            "gain_db": 0,
                            "sampling_rate": sampling_rate,
                        },  # DC readout input
                    },
                },
            },
        }
    },
    "elements": {
        # pluger (P1, P2, ...)
        **{
            pg: {
                "singleInput": {
                    "port": (val["con"], val["fem"], val["ao"]),
                },
                "operations": {
                    "step": f"{pg}_step_pulse",
                },
            }
            for pg, val in PLUNGER_CONSTANTS.items()
        },
        # pluger sticky (P1_sticky, P2_sticky, ...)
        **{
            f"{pg}_sticky": {
                "singleInput": {
                    "port": (val["con"], val["fem"], val["ao"]),
                },
                "sticky": {"analog": True, "duration": hold_offset_duration},
                "operations": {
                    "step": f"{pg}_step_pulse",
                },
            }
            for pg, val in PLUNGER_CONSTANTS.items()
        },
        # barrier (B1, B2, ...)
        **{
            br: {
                "singleInput": {
                    "port": (val["con"], val["fem"], val["ao"]),
                },
                "operations": {
                    "step": f"{br}_step_pulse",
                },
            }
            for br, val in BARRIER_CONSTANTS.items()
        },
        # barrier sticky (B1_sticky, B2_sticky, ...)
        **{
            f"{br}_sticky": {
                "singleInput": {
                    "port": (val["con"], val["fem"], val["ao"]),
                },
                "sticky": {"analog": True, "duration": hold_offset_duration},
                "operations": {
                    "step": f"{br}_step_pulse",
                },
            }
            for br, val in BARRIER_CONSTANTS.items()
        },
        # barrier (B1, B2, ...)
        **{
            psdg: {
                "singleInput": {
                    "port": (val["con"], val["fem"], val["ao"]),
                },
                "operations": {
                    "step": f"{psdg}_step_pulse",
                },
            }
            for psdg, val in PLUNGER_SD_CONSTANTS.items()
        },
        # barrier sticky (B1_sticky, B2_sticky, ...)
        **{
            f"{psdg}_sticky": {
                "singleInput": {
                    "port": (val["con"], val["fem"], val["ao"]),
                },
                "sticky": {"analog": True, "duration": hold_offset_duration},
                "operations": {
                    "step": f"{psdg}_step_pulse",
                },
            }
            for psdg, val in PLUNGER_SD_CONSTANTS.items()
        },
        # qubits & crot (qubit1, ...)
        **{
            qb: {
                "mixInputs": {
                    "I": (val["con"], val["fem"], val["aout_I"]),
                    "Q": (val["con"], val["fem"], val["aout_Q"]),
                    "lo_frequency": val["LO"],
                    "mixer": f"mixer_{qb}",
                },
                "intermediate_frequency": val["IF"],
                "operations": {
                    "const": "const_pulse",
                    "saturation": "saturation_pulse",
                    "x180_kaiser": f"x180_kaiser_pulse_{qb}",
                    "x90_kaiser": f"x90_kaiser_pulse_{qb}",
                    "-x90_kaiser": f"minus_x90_kaiser_pulse_{qb}",
                    "y180_kaiser": f"y180_kaiser_pulse_{qb}",
                    "y90_kaiser": f"y90_kaiser_pulse_{qb}",
                    "-y90_kaiser": f"minus_y90_kaiser_pulse_{qb}",
                    "x180_gauss": f"x180_gauss_pulse_{qb}",
                    "x90_gauss": f"x90_gauss_pulse_{qb}",
                    "-x90_gauss": f"minus_x90_gauss_pulse_{qb}",
                    "y180_gauss": f"y180_gauss_pulse_{qb}",
                    "y90_gauss": f"y90_gauss_pulse_{qb}",
                    "-y90_gauss": f"minus_y90_gauss_pulse_{qb}",
                    "x180_square": f"x180_square_pulse_{qb}",
                    "x90_square": f"x90_square_pulse_{qb}",
                    "-x90_square": f"minus_x90_square_pulse_{qb}",
                    "y180_square": f"y180_square_pulse_{qb}",
                    "y90_square": f"y90_square_pulse_{qb}",
                    "-y90_square": f"minus_y90_square_pulse_{qb}",
                },
                # "thread": qb,
            }
            for qb, val in {**QUBIT_CONSTANTS, **CROT_CONSTANTS}.items()
        },
        # qubits & crot (qubit1, ...)
        **{
            f"{qb}_dup": {
                "mixInputs": {
                    "I": (val["con"], val["fem"], val["aout_I"]),
                    "Q": (val["con"], val["fem"], val["aout_Q"]),
                    "lo_frequency": val["LO"],
                    "mixer": f"mixer_{qb}",
                },
                "intermediate_frequency": val["IF"],
                "operations": {
                    "const": "const_pulse",
                    "saturation": "saturation_pulse",
                    "x180_kaiser": f"x180_kaiser_pulse_{qb}",
                    "x90_kaiser": f"x90_kaiser_pulse_{qb}",
                    "-x90_kaiser": f"minus_x90_kaiser_pulse_{qb}",
                    "y180_kaiser": f"y180_kaiser_pulse_{qb}",
                    "y90_kaiser": f"y90_kaiser_pulse_{qb}",
                    "-y90_kaiser": f"minus_y90_kaiser_pulse_{qb}",
                    "x180_gauss": f"x180_gauss_pulse_{qb}",
                    "x90_gauss": f"x90_gauss_pulse_{qb}",
                    "-x90_gauss": f"minus_x90_gauss_pulse_{qb}",
                    "y180_gauss": f"y180_gauss_pulse_{qb}",
                    "y90_gauss": f"y90_gauss_pulse_{qb}",
                    "-y90_gauss": f"minus_y90_gauss_pulse_{qb}",
                    "x180_square": f"x180_square_pulse_{qb}",
                    "x90_square": f"x90_square_pulse_{qb}",
                    "-x90_square": f"minus_x90_square_pulse_{qb}",
                    "y180_square": f"y180_square_pulse_{qb}",
                    "y90_square": f"y90_square_pulse_{qb}",
                    "-y90_square": f"minus_y90_square_pulse_{qb}",
                },
                # "thread": qb,
            }
            for qb, val in {**QUBIT_CONSTANTS, **CROT_CONSTANTS}.items()
        },
        # RF switch
        **{
            dm: {
                "singleInput": {
                    "port": (val["con"], val["fem"], val["aout"]),
                },
                "digitalInputs": {
                    "trigger": {
                        "port": (val["con"], val["fem"], val["dout"]),
                        "delay": val["delay"],
                        "buffer": val["buffer"],
                    }
                },
                "operations": {
                    "trigger": "trigger_pulse",
                    
                },
            }
            for dm, val in DO_CONSTANTS.items()
        },
        # reflectometry (qubit1, ...)
        **{
            tc: {
                "singleInput": {
                    "port": (val["con"], val["fem"], val["ao"]),
                },
                "intermediate_frequency": val["IF"],
                "operations": {
                    "readout": f"reflectometry_readout_pulse_{tc}",
                },
                "outputs": {
                    "out1": (val["con"], val["fem"], val["ai"]),
                },
                "time_of_flight": val["time_of_flight"],
                "smearing": 0,
            }
            for tc, val in TANK_CIRCUIT_CONSTANTS.items()
        },
    },
    "pulses": {
        # pluger (P1, P2, ...)
        **{
            f"{pg}_step_pulse": {
                "operation": "control",
                "length": val["step_len"],
                "waveforms": {
                    "single": f"{pg}_step_wf",
                },
            }
            for pg, val in PLUNGER_CONSTANTS.items()
        },
        **{
            f"{br}_step_pulse": {
                "operation": "control",
                "length": val["step_len"],
                "waveforms": {
                    "single": f"{br}_step_wf",
                },
            }
            for br, val in BARRIER_CONSTANTS.items()
        },
        **{
            f"{pg}_step_pulse": {
                "operation": "control",
                "length": val["step_len"],
                "waveforms": {
                    "single": f"{pg}_step_wf",
                },
            }
            for pg, val in PLUNGER_SD_CONSTANTS.items()
        },
        **{
            f"{rk}_{wf}_pulse_{qb}": {
                "operation": "control",
                "length": val[f"{wf}_pi_len"],
                "waveforms": {
                    "I": f"{rk}_{wf}_I_wf_{qb}",
                    "Q": f"{rk}_{wf}_Q_wf_{qb}",
                },
            }
            for rk in ["x180", "y180"]  # Loop over 
            for wf in ["gauss", "kaiser", "square"]  # Loop over waveforms
            for qb, val in {**QUBIT_CONSTANTS, **CROT_CONSTANTS}.items()
        },
        **{
            f"{rk}_{wf}_pulse_{qb}": {
                "operation": "control",
                "length": val[f"{wf}_pi_half_len"],
                "waveforms": {
                    "I": f"{rk}_{wf}_I_wf_{qb}",
                    "Q": f"{rk}_{wf}_Q_wf_{qb}",
                },
            }
            for rk in ["x90", "minus_x90", "y90", "minus_y90"]  # Loop over 
            for wf in ["gauss", "kaiser", "square"]  # Loop over waveforms
            for qb, val in {**QUBIT_CONSTANTS, **CROT_CONSTANTS}.items()
        },
        **{
            f"reflectometry_readout_pulse_{tc}": {
                "operation": "measurement",
                "length": val["readout_len"],
                "waveforms": {
                    "single": f"reflectometry_readout_wf_{tc}",
                },
                "integration_weights": {
                    "cos": f"cosine_weights_{tc}",
                    "sin": f"sine_weights_{tc}",
                },
                "digital_marker": "ON",
            }
            for tc, val in TANK_CIRCUIT_CONSTANTS.items()
        },
        "const_pulse": {
            "operation": "control",
            "length": CONST_LEN,
            "waveforms": {
                "I": "const_wf",
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
        "trigger_pulse": {
            "operation": "control",
            "length": 1000,
            "digital_marker": "ON",
            "waveforms": {
                "single": "zero_wf",
            },
        },
    },
    "waveforms": {
        "zero_wf": {"type": "constant", "sample": 0.0},
        "const_wf": {"type": "constant", "sample": CONST_AMP},
        "saturation_wf": {"type": "constant", "sample": SATURATION_AMP},
        **{f"reflectometry_readout_wf_{key}": {"type": "constant", "sample": val["readout_amp"]} for key, val in TANK_CIRCUIT_CONSTANTS.items()},
        **{f"{key}_step_wf": {"type": "constant", "sample": val["step_amp"]} for key, val in PLUNGER_CONSTANTS.items()},
        **{f"{key}_step_wf": {"type": "constant", "sample": val["step_amp"]} for key, val in BARRIER_CONSTANTS.items()},
        **{f"{key}_step_wf": {"type": "constant", "sample": val["step_amp"]} for key, val in PLUNGER_SD_CONSTANTS.items()},

        **{f"x180_square_I_wf_{key}": {"type": "arbitrary", "samples": waveforms[key + "_square_x180_I"]} for key in {**QUBIT_CONSTANTS, **CROT_CONSTANTS}.keys()},
        **{f"x180_square_Q_wf_{key}": {"type": "arbitrary", "samples": waveforms[key + "_square_x180_Q"]} for key in {**QUBIT_CONSTANTS, **CROT_CONSTANTS}.keys()},
        **{f"x90_square_I_wf_{key}": {"type": "arbitrary", "samples": waveforms[key + "_square_x90_I"]} for key in {**QUBIT_CONSTANTS, **CROT_CONSTANTS}.keys()},
        **{f"x90_square_Q_wf_{key}": {"type": "arbitrary", "samples": waveforms[key + "_square_x90_Q"]} for key in {**QUBIT_CONSTANTS, **CROT_CONSTANTS}.keys()},
        **{f"minus_x90_square_I_wf_{key}": {"type": "arbitrary", "samples": waveforms[key + "_square_minus_x90_I"]} for key in {**QUBIT_CONSTANTS, **CROT_CONSTANTS}.keys()},
        **{f"minus_x90_square_Q_wf_{key}": {"type": "arbitrary", "samples": waveforms[key + "_square_minus_x90_Q"]} for key in {**QUBIT_CONSTANTS, **CROT_CONSTANTS}.keys()},
        **{f"y180_square_I_wf_{key}": {"type": "arbitrary", "samples": waveforms[key + "_square_y180_I"]} for key in {**QUBIT_CONSTANTS, **CROT_CONSTANTS}.keys()},
        **{f"y180_square_Q_wf_{key}": {"type": "arbitrary", "samples": waveforms[key + "_square_y180_Q"]} for key in {**QUBIT_CONSTANTS, **CROT_CONSTANTS}.keys()},
        **{f"y90_square_I_wf_{key}": {"type": "arbitrary", "samples": waveforms[key + "_square_y90_I"]} for key in {**QUBIT_CONSTANTS, **CROT_CONSTANTS}.keys()},
        **{f"y90_square_Q_wf_{key}": {"type": "arbitrary", "samples": waveforms[key + "_square_y90_Q"]} for key in {**QUBIT_CONSTANTS, **CROT_CONSTANTS}.keys()},
        **{f"minus_y90_square_I_wf_{key}": {"type": "arbitrary", "samples": waveforms[key + "_square_minus_y90_I"]} for key in {**QUBIT_CONSTANTS, **CROT_CONSTANTS}.keys()},
        **{f"minus_y90_square_Q_wf_{key}": {"type": "arbitrary", "samples": waveforms[key + "_square_minus_y90_Q"]} for key in {**QUBIT_CONSTANTS, **CROT_CONSTANTS}.keys()},
        
        **{f"x180_gauss_I_wf_{key}": {"type": "arbitrary", "samples": waveforms[key + "_gauss_x180_I"]} for key in {**QUBIT_CONSTANTS, **CROT_CONSTANTS}.keys()},
        **{f"x180_gauss_Q_wf_{key}": {"type": "arbitrary", "samples": waveforms[key + "_gauss_x180_Q"]} for key in {**QUBIT_CONSTANTS, **CROT_CONSTANTS}.keys()},
        **{f"x90_gauss_I_wf_{key}": {"type": "arbitrary", "samples": waveforms[key + "_gauss_x90_I"]} for key in {**QUBIT_CONSTANTS, **CROT_CONSTANTS}.keys()},
        **{f"x90_gauss_Q_wf_{key}": {"type": "arbitrary", "samples": waveforms[key + "_gauss_x90_Q"]} for key in {**QUBIT_CONSTANTS, **CROT_CONSTANTS}.keys()},
        **{f"minus_x90_gauss_I_wf_{key}": {"type": "arbitrary", "samples": waveforms[key + "_gauss_minus_x90_I"]} for key in {**QUBIT_CONSTANTS, **CROT_CONSTANTS}.keys()},
        **{f"minus_x90_gauss_Q_wf_{key}": {"type": "arbitrary", "samples": waveforms[key + "_gauss_minus_x90_Q"]} for key in {**QUBIT_CONSTANTS, **CROT_CONSTANTS}.keys()},
        **{f"y180_gauss_I_wf_{key}": {"type": "arbitrary", "samples": waveforms[key + "_gauss_y180_I"]} for key in {**QUBIT_CONSTANTS, **CROT_CONSTANTS}.keys()},
        **{f"y180_gauss_Q_wf_{key}": {"type": "arbitrary", "samples": waveforms[key + "_gauss_y180_Q"]} for key in {**QUBIT_CONSTANTS, **CROT_CONSTANTS}.keys()},
        **{f"y90_gauss_I_wf_{key}": {"type": "arbitrary", "samples": waveforms[key + "_gauss_y90_I"]} for key in {**QUBIT_CONSTANTS, **CROT_CONSTANTS}.keys()},
        **{f"y90_gauss_Q_wf_{key}": {"type": "arbitrary", "samples": waveforms[key + "_gauss_y90_Q"]} for key in {**QUBIT_CONSTANTS, **CROT_CONSTANTS}.keys()},
        **{f"minus_y90_gauss_I_wf_{key}": {"type": "arbitrary", "samples": waveforms[key + "_gauss_minus_y90_I"]} for key in {**QUBIT_CONSTANTS, **CROT_CONSTANTS}.keys()},
        **{f"minus_y90_gauss_Q_wf_{key}": {"type": "arbitrary", "samples": waveforms[key + "_gauss_minus_y90_Q"]} for key in {**QUBIT_CONSTANTS, **CROT_CONSTANTS}.keys()},
        
        **{f"x180_kaiser_I_wf_{key}": {"type": "arbitrary", "samples": waveforms[key + "_kaiser_x180_I"]} for key in {**QUBIT_CONSTANTS, **CROT_CONSTANTS}.keys()},
        **{f"x180_kaiser_Q_wf_{key}": {"type": "arbitrary", "samples": waveforms[key + "_kaiser_x180_Q"]} for key in {**QUBIT_CONSTANTS, **CROT_CONSTANTS}.keys()},
        **{f"x90_kaiser_I_wf_{key}": {"type": "arbitrary", "samples": waveforms[key + "_kaiser_x90_I"]} for key in {**QUBIT_CONSTANTS, **CROT_CONSTANTS}.keys()},
        **{f"x90_kaiser_Q_wf_{key}": {"type": "arbitrary", "samples": waveforms[key + "_kaiser_x90_Q"]} for key in {**QUBIT_CONSTANTS, **CROT_CONSTANTS}.keys()},
        **{f"minus_x90_kaiser_I_wf_{key}": {"type": "arbitrary", "samples": waveforms[key + "_kaiser_minus_x90_I"]} for key in {**QUBIT_CONSTANTS, **CROT_CONSTANTS}.keys()},
        **{f"minus_x90_kaiser_Q_wf_{key}": {"type": "arbitrary", "samples": waveforms[key + "_kaiser_minus_x90_Q"]} for key in {**QUBIT_CONSTANTS, **CROT_CONSTANTS}.keys()},
        **{f"y180_kaiser_I_wf_{key}": {"type": "arbitrary", "samples": waveforms[key + "_kaiser_y180_I"]} for key in {**QUBIT_CONSTANTS, **CROT_CONSTANTS}.keys()},
        **{f"y180_kaiser_Q_wf_{key}": {"type": "arbitrary", "samples": waveforms[key + "_kaiser_y180_Q"]} for key in {**QUBIT_CONSTANTS, **CROT_CONSTANTS}.keys()},
        **{f"y90_kaiser_I_wf_{key}": {"type": "arbitrary", "samples": waveforms[key + "_kaiser_y90_I"]} for key in {**QUBIT_CONSTANTS, **CROT_CONSTANTS}.keys()},
        **{f"y90_kaiser_Q_wf_{key}": {"type": "arbitrary", "samples": waveforms[key + "_kaiser_y90_Q"]} for key in {**QUBIT_CONSTANTS, **CROT_CONSTANTS}.keys()},
        **{f"minus_y90_kaiser_I_wf_{key}": {"type": "arbitrary", "samples": waveforms[key + "_kaiser_minus_y90_I"]} for key in {**QUBIT_CONSTANTS, **CROT_CONSTANTS}.keys()},
        **{f"minus_y90_kaiser_Q_wf_{key}": {"type": "arbitrary", "samples": waveforms[key + "_kaiser_minus_y90_Q"]} for key in {**QUBIT_CONSTANTS, **CROT_CONSTANTS}.keys()},
    },
    "digital_waveforms": {
        "ON": {"samples": [(1, 0)]},
    },
    "integration_weights": {
        **{
            f"cosine_weights_{tc}": {
                "cosine": [(1.0, val["readout_len"])],
                "sine": [(0.0, val["readout_len"])],
            }
            for tc, val in TANK_CIRCUIT_CONSTANTS.items()
        },
        **{
            f"sine_weights_{tc}": {
                "cosine": [(0.0, val["readout_len"])],
                "sine": [(1.0, val["readout_len"])],
            }
            for tc, val in TANK_CIRCUIT_CONSTANTS.items()
        },
    },
    "mixers": {
        **{
            f"mixer_{qb}": [
                {
                    "intermediate_frequency": val["IF"],
                    "lo_frequency": val["LO"],
                    "correction": IQ_imbalance(val["mixer_g"], val["mixer_phi"]),
                },
            ]
            for qb, val in {**QUBIT_CONSTANTS, **CROT_CONSTANTS}.items()
        },
    },
}

# %%
