import sys

import flax
import flax.linen as nn
import jax
import jax.numpy as jnp
import numpy as np
from flax.training import train_state

from quam.quam.components.ports import analog_outputs

sys.path.append(r"D:\NNcat\NNcat1e\artemix")
import h5py
import matplotlib.pyplot as plt
import scipy
import scipy.optimize as opt
from bspln import *
from neurax import *
from scipy.constants import *


def padded_time(t):
    return max(t + (4 - t % 4) % 4, 16)


def pad_time(L, before=True):
    return (padded_time(len(L)) - len(L)) * [0] + list(L)


def IQ_imbalance(g, phi):
    c = np.cos(phi)
    s = np.sin(phi)
    N = 1 / ((1 - g**2) * (2 * c**2 - 1))
    return [float(N * x) for x in [(1 - g) * c, (1 + g) * s, (1 - g) * s, (1 + g) * c]]


def gaussian_shape(amp, total_time, width, padding=True):
    pad_time = 0
    if padding:
        if total_time < 16:
            pad_time = 16 - total_time
        else:
            pad_time = (4 - total_time % 4) % 4
    time = np.array(range(total_time))
    gaussian = np.exp(-np.square(time - total_time / 2) / (2 * width**2))

    return list(amp * gaussian) + [0.0] * pad_time


def double_pulse(amp, t_pulse, width, t_wait, reverse=False, padding=True):
    pad_time = 0
    total_time = t_pulse * 2 + t_wait
    reverser = -2 * reverse + 1  # tells to play the second pulse with opposite phase or not
    if padding:
        if total_time < 16:
            pad_time = 16 - total_time
        else:
            pad_time = (4 - total_time % 4) % 4
    time = np.array(range(t_pulse))
    gaussian = np.exp(-np.square(time - t_pulse / 2) / (2 * width**2))

    return list(amp * gaussian) + [0.0] * t_wait + list(reverser * amp * gaussian) + [0.0] * pad_time


calib = [round(float(c), 5) for c in np.load(r"D:\automatic_psa_calibration\calib.npy")]

# Coefficients in Hamiltonian
chi = 0.246 * (2 * np.pi)
A_nonlin = 0  # 0.01 * (2 * np.pi)

# Driving fields scales
mu_qub = 4.0
mu_cav = 8.0

# Alphas
alpha_min = 0.0
alpha_max = 2.0

# Relaxation times
t1_qub = 28
t2_qub = 20
t1_cav = 270

# Time grid
time_start = 0.0
time_end = 2.0
time_intervals_num = 2000

# B-splines
k = 3
n = 11
skip_left = 1
skip_right = 1

time_edges = np.linspace(time_start, time_end, time_intervals_num + 1)
bspline_builder = setup_bspline_builder(time_start, time_end, n, k, skip_left, skip_right)
bsplns_edges = bspline_builder(time_edges)

bspln_set_size = n - skip_left - skip_right


def nn_call(x):
    x = nn.Dense(features=30)(x)
    x = nn.relu(x)
    x = nn.Dense(features=60)(x)
    x = nn.relu(x)
    x = nn.Dense(features=30)(x)
    x = nn.relu(x)
    x = nn.Dense(features=4 * bspln_set_size)(x)
    x = x.reshape((4, bspln_set_size))
    return x


seed = 1234
key = jax.random.PRNGKey(seed)

key, subkey = jax.random.split(key)
state = create_flax_state(subkey, nn_call, jnp.ones([1]), optax.adam(learning_rate=0.001), print_summary=True)
state = restore_flax_state(r"D:\NNcat\NNcat1e\artemix1\artemix\nn_2us_cat4.0", state)


def get_coeffs(state, alpha):
    return state.apply_fn({"params": state.params}, np.array([alpha]))


def ctrl_from_coeffs(ctrl_coeffs, bsplns):
    ctrls_real = ctrl_coeffs @ bsplns
    e_qub = ctrls_real[0, ...] + 1j * ctrls_real[1, ...]
    e_cav = ctrls_real[2, ...] + 1j * ctrls_real[3, ...]
    return e_qub, e_cav


def IQ_rot(data):
    dataf = data.flatten()
    I = np.real(dataf)
    Q = np.imag(dataf)
    Cov = np.cov(I, Q)
    A = scipy.linalg.eig(Cov)
    eigvecs = A[1]
    if A[0][1] > A[0][0]:
        eigvec1 = eigvecs[:, 0]
    else:
        eigvec1 = eigvecs[:, 1]
    theta = np.arctan(eigvec1[0] / eigvec1[1])
    #     theta = theta%np.pi # added 19/07/2019
    data_c = data * np.exp(1j * theta)

    return data_c


parameters = {  # These values are overwritten by Exopy (section "OPX_config/parameters")
    "RO2_if": 66e6,
    "RO2_pulse_length": 1000,
    "RO2_pulse_amp": 0.2,
    "YN_pulse_length": 1000,
    "YN_pulse_amp": 0.2,
    "YN2_pulse_length": 1000,
    "YN2_pulse_amp": 0.2,
    "Storage_pulse_length": 1000,
    "Storage_pulse_amp": 0.2,
    "Wigner_pulse_length": 500,
    "Wigner_pulse_amp": 0.2,
    "Storage_ref_pulse_length": 1000,
    "Storage_ref_pulse_amp": 0.2,
    "YN2_if": 110e6,
    "alpha": 1.57,
    "reset_length": 700000,
}

optimized_parameters = {  # These values are hardcoded: Exopy does not change them
    "delay_RO": 340,
    "RO_pulse_amp": 0.023,
    "RO_pulse_length": 2200,
    "RO_phase": 0.6649041609080298 + np.pi + 0.234,
    "thresholdpi": 0,
    "threshold": 0,
    #### IF ####
    "RO_if": 66e6,
    "Storage_if": 70e6,
    "YN_if": 110e6,
    "short_pi_length": 64,
    "short_pi_amp": 0.38465,
    "short_hpi_length": 32,
    "short_hpi_amp": 0.38465,
    "long_pi_length": 20000,
    "long_pi_amp": 0.00127,
    "time_mod2": 2096 - 32,
    "ksi_qub": 39.3,
    "ksi_cav": 33.4,
}


def get_parameters():
    return parameters


def get_config(params):
    params.update(optimized_parameters)

    RO_if = float(params["RO_if"])
    YN_if = float(params["YN_if"])
    YN2_if = float(params["YN2_if"])
    RO2_if = float(params["RO2_if"])

    Storage_if = float(params["Storage_if"])

    RO_pulse_length = int(params["RO_pulse_length"])
    RO_pulse_amp = float(params["RO_pulse_amp"])

    delay_RO = int(params["delay_RO"])
    RO_phase = float(params["RO_phase"])
    threshold = float(params["threshold"])
    thresholdpi = float(params["thresholdpi"])

    RO2_pulse_length = int(params["RO2_pulse_length"])
    RO2_pulse_amp = float(params["RO2_pulse_amp"])

    YN_pulse_length = int(params["YN_pulse_length"])
    YN_pulse_amp = float(params["YN_pulse_amp"])

    YN2_pulse_length = int(params["YN2_pulse_length"])
    YN2_pulse_amp = float(params["YN2_pulse_amp"])

    short_pi_length = int(params["short_pi_length"])
    short_pi_amp = float(params["short_pi_amp"])

    Storage_pulse_length = int(params["Storage_pulse_length"])
    Storage_pulse_amp = float(params["Storage_pulse_amp"])
    Wigner_pulse_length = int(params["Wigner_pulse_length"])
    Wigner_pulse_amp = float(params["Wigner_pulse_amp"])

    Storage_ref_pulse_length = int(params["Storage_ref_pulse_length"])
    Storage_ref_pulse_amp = float(params["Storage_ref_pulse_amp"])

    reset_length = int(params["reset_length"])

    short_pi_length = int(params["short_pi_length"])
    short_pi_amp = float(params["short_pi_amp"])
    short_hpi_length = int(params["short_hpi_length"])
    short_hpi_amp = float(params["short_hpi_amp"])
    time_mod2 = int(params["time_mod2"])
    controls = np.load(r"D:\NNcat\NNcat1c\ctrl.npy")
    alpha = float(params["alpha"])
    ksi_qub = float(params["ksi_qub"])
    ksi_cav = float(params["ksi_cav"])
    translation_qub = mu_qub / 2 / np.pi / ksi_qub * 2
    translation_cav = mu_cav / 2 / np.pi / ksi_cav

    coeffs = np.array(get_coeffs(state, alpha))
    ctrl = np.array(ctrl_from_coeffs(coeffs, bsplns_edges))

    ctrl[0] = ctrl[0].conj() * translation_qub
    ctrl[1] = ctrl[1].conj() * translation_cav
    controls_YN_I = pad_time(ctrl[0].real)
    controls_YN_Q = pad_time(ctrl[0].imag)
    controls_Storage_I = pad_time(ctrl[1].real)
    controls_Storage_Q = pad_time(ctrl[1].imag)

    mw_slot = 1
    lf_slot = 2
    resonator_power = -11  # dBm, power on the resonator [-11, 16] in steps of 3dbm
    YN_power = 1
    YN2_power = 1
    storage_power = 1

    config = {
        "version": 1,
        "controllers": {
            "con1": {
                "type": "opx1000",
                "fems": {
                    mw_slot: {
                        "type": "MW",
                        "analog_outputs": {
                            1: {
                                "band": 3,
                                "full_scale_power_dbm": resonator_power,
                                "upconverters": {1: {"frequency": 7.8e9}},
                            },  # RO and RO2
                            2: {
                                "band": 1,
                                "full_scale_power_dbm": YN_power,
                                "upconverters": {1: {"frequency": 3.41209420450e9}},
                            },  # YN
                            3: {
                                "band": 1,
                                "full_scale_power_dbm": YN2_power,
                                "upconverters": {1: {"frequency": 3.41209420450e9}},
                            },  # YN2
                            4: {
                                "band": 1,
                                "full_scale_power_dbm": storage_power,
                                "upconverters": {1: {"frequency": 4.6397e9}},
                            },  # Storage
                        },
                        "analog_inputs": {
                            1: {
                                "band": 3,
                                "downconverter_frequency": 7.8e9,
                            },  # RO and RO2 input
                        },
                        "digital_outputs": {1: {}, 2: {}},
                    },
                    lf_slot: {
                        "type": "LF",
                        "analog_outputs": {
                            1: {
                                "offset": 0.0,
                                "output_mode": "direct",
                                "sampling_rate": int(1e9),
                                "upsampling_mode": "pulse",
                                "delay": 141,
                            },
                        },
                        "digital_outputs": {1: {}},
                        "analog_inputs": {},
                    },
                },
            },
        },
        "elements": {
            "RO": {
                "MWInput": {"port": ("con1", mw_slot, 1), "upconverter": 1},
                "intermediate_frequency": RO_if,
                "operations": {"RO_ro": "RO_ro", "RO_pulse": "RO_pulse"},
                # MWOutput corresponds to an OPX physical input port
                "MWOutput": {"port": ("con1", mw_slot, 1)},
                "digitalInputs": {"port": {"port": ("con1", mw_slot, 2), "buffer": 0, "delay": 0}},
                "time_of_flight": delay_RO,
                "smearing": 0,
            },
            "RO2": {
                "MWInput": {"port": ("con1", mw_slot, 1), "upconverter": 1},
                "intermediate_frequency": RO2_if,
                "operations": {
                    "RO2_pulse": "RO2_pulse",
                },
            },
            "YN": {
                "MWInput": {"port": ("con1", mw_slot, 2), "upconverter": 1},
                "intermediate_frequency": YN_if,
                "operations": {
                    "YN_pulse": "YN_pulse",
                    "short_pi": "YN_short_pi_pulse",
                    "short_hpi": "YN_short_hpi_pulse",
                    "mod2": "mod2_pulse",
                    "mod2_minus": "mod2_minus_pulse",
                    "GRAPE": "YN_GRAPE_pulse",
                },
            },
            "YN2": {
                "MWInput": {"port": ("con1", mw_slot, 3), "upconverter": 1},
                "intermediate_frequency": YN2_if,
                "operations": {
                    "YN2_pulse": "YN2_pulse",
                },
            },
            "reset_storage": {
                "singleInput": {"port": ("con1", lf_slot, 9)},
                "intermediate_frequency": 0,
                "operations": {
                    "reset_pulse": "reset_pulse",
                },
                "digitalInputs": {"port": {"port": ("con1", lf_slot, 1), "buffer": 0, "delay": 0}},
            },
            "Storage": {
                "MWInput": {"port": ("con1", mw_slot, 4), "upconverter": 1},
                "intermediate_frequency": Storage_if,
                "operations": {
                    "Storage_pulse": "Storage_pulse",
                    "Storage_ref_pulse": "Storage_ref_pulse",
                    "Wigner_pulse": "Wigner_pulse",
                    "GRAPE": "Storage_GRAPE_pulse",
                },
            },
        },
        "pulses": {
            "RO_ro": {
                "operation": "measurement",
                "length": padded_time(RO_pulse_length),
                "waveforms": {"I": "RO_ro_wave", "Q": "zero"},
                "integration_weights": {
                    "RO_square_integW1": "RO_square_integW1",
                    "RO_square_integW2": "RO_square_integW2",
                },
                "digital_marker": "ON",
            },
            "RO_pulse": {
                "operation": "control",
                "length": padded_time(RO_pulse_length),
                "waveforms": {"I": "RO_ro_wave", "Q": "zero"},
            },
            "RO2_pulse": {
                "operation": "control",
                "length": padded_time(RO2_pulse_length),
                "waveforms": {"I": "RO2_pulse_wave", "Q": "zero"},
            },
            "YN_pulse": {
                "operation": "control",
                "length": padded_time(YN_pulse_length),
                "waveforms": {"I": "YN_pulse_wave", "Q": "zero"},
            },
            "YN_square_pulse": {
                "operation": "control",
                "length": padded_time(YN_pulse_length),
                "waveforms": {"I": "YN_square_pulse_wave", "Q": "zero"},
            },
            "mod2_pulse": {
                "operation": "control",
                "length": padded_time(short_hpi_length * 2 + time_mod2),
                "waveforms": {"I": "mod2_wave", "Q": "zero"},
            },
            "mod2_minus_pulse": {
                "operation": "control",
                "length": padded_time(short_hpi_length * 2 + time_mod2),
                "waveforms": {"I": "mod2_minus_wave", "Q": "zero"},
            },
            "YN2_pulse": {
                "operation": "control",
                "length": padded_time(YN2_pulse_length),
                "waveforms": {"I": "YN2_pulse_wave", "Q": "zero"},
            },
            "YN_short_pi_pulse": {
                "operation": "control",
                "length": padded_time(short_pi_length),
                "waveforms": {"I": "YN_short_pi_wave", "Q": "zero"},
            },
            "YN_short_hpi_pulse": {
                "operation": "control",
                "length": padded_time(short_hpi_length),
                "waveforms": {"I": "YN_short_hpi_wave", "Q": "zero"},
            },
            "YN_GRAPE_pulse": {
                "operation": "control",
                "length": padded_time(len(controls_YN_I)),
                "waveforms": {"I": "YN_GRAPE_pulse_wave_I", "Q": "YN_GRAPE_pulse_wave_Q"},
            },
            "Storage_pulse": {
                "operation": "control",
                "length": padded_time(Storage_pulse_length),
                "waveforms": {"I": "Storage_pulse_wave", "Q": "zero"},
            },
            "Wigner_pulse": {
                "operation": "control",
                "length": padded_time(Wigner_pulse_length),
                "waveforms": {"I": "Wigner_pulse_wave", "Q": "zero"},
            },
            "Storage_ref_pulse": {
                "operation": "control",
                "length": padded_time(Storage_ref_pulse_length),
                "waveforms": {"I": "Storage_ref_pulse_wave", "Q": "zero"},
            },
            "Storage_GRAPE_pulse": {
                "operation": "control",
                "length": padded_time(len(controls_Storage_I)),
                "waveforms": {"I": "Storage_GRAPE_pulse_wave_I", "Q": "Storage_GRAPE_pulse_wave_Q"},
            },
            "reset_pulse": {
                "operation": "control",
                "length": reset_length,
                "waveforms": {"single": "zero"},
                "digital_marker": "reset",
            },
        },
        "waveforms": {
            "RO_ro_wave": {"type": "constant", "sample": RO_pulse_amp},
            "RO2_pulse_wave": {"type": "constant", "sample": RO2_pulse_amp},
            "Storage_ref_pulse_wave": {"type": "constant", "sample": Storage_ref_pulse_amp},
            "Storage_pulse_wave": {"type": "constant", "sample": Storage_pulse_amp},
            "Wigner_pulse_wave": {"type": "constant", "sample": Wigner_pulse_amp},
            "Storage_GRAPE_pulse_wave_I": {"type": "arbitrary", "samples": controls_Storage_I},
            "Storage_GRAPE_pulse_wave_Q": {"type": "arbitrary", "samples": controls_Storage_Q},
            "YN_pulse_wave": {
                "type": "arbitrary",
                "samples": gaussian_shape(YN_pulse_amp, YN_pulse_length, YN_pulse_length / 6, padding=True),
            },
            "YN_square_pulse_wave": {"type": "constant", "sample": YN_pulse_amp},
            "mod2_wave": {
                "type": "arbitrary",
                "samples": double_pulse(
                    short_hpi_amp, short_hpi_length, short_hpi_length / 6, time_mod2, reverse=False, padding=True
                ),
            },
            "mod2_minus_wave": {
                "type": "arbitrary",
                "samples": double_pulse(
                    short_hpi_amp, short_hpi_length, short_hpi_length / 6, time_mod2, reverse=True, padding=True
                ),
            },
            "YN2_pulse_wave": {
                "type": "arbitrary",
                "samples": gaussian_shape(YN2_pulse_amp, YN2_pulse_length, YN2_pulse_length / 6, padding=True),
            },
            "YN_short_pi_wave": {
                "type": "arbitrary",
                "samples": gaussian_shape(short_pi_amp, short_pi_length, short_pi_length / 6, padding=True),
            },
            "YN_short_hpi_wave": {
                "type": "arbitrary",
                "samples": gaussian_shape(short_hpi_amp, short_hpi_length, short_hpi_length / 6, padding=True),
            },
            "YN_GRAPE_pulse_wave_I": {"type": "arbitrary", "samples": controls_YN_I},
            "YN_GRAPE_pulse_wave_Q": {"type": "arbitrary", "samples": controls_YN_Q},
            "zero": {"type": "constant", "sample": 0},
        },
        "digital_waveforms": {"ON": {"samples": [(1, 0)]}, "reset": {"samples": [(1, 0)]}},
        "integration_weights": {
            "RO_square_integW1": {
                "cosine": [np.cos(RO_phase)] * (padded_time(RO_pulse_length) // 4),
                "sine": [np.sin(RO_phase)] * (padded_time(RO_pulse_length) // 4),
            },
            "RO_square_integW2": {
                "cosine": [-np.sin(RO_phase)] * (padded_time(RO_pulse_length) // 4),
                "sine": [np.cos(RO_phase)] * (padded_time(RO_pulse_length) // 4),
            },
        },
    }

    return config
