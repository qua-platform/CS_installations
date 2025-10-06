
from pathlib import Path
from qualang_tools.config.waveform_tools import drag_gaussian_pulse_waveforms
import numpy as np
from qualang_tools.units import unit
u = unit(coerce_to_integer=True)

con = "con1" # Controller name in OPX1000
mw_fem = 1 # Where is it in OPX1000
lf_fem = 5 # Where is it in OPX1000
sampling_rate = int(1e9)  # or, int(2e9)

# %% ---- Helper Functions ---- #
def mw_LO_band(frequency):
    if frequency < 4.5 * u.GHz:
        return 1
    elif frequency < 7.5 * u.GHz:
        return 2
    else:
        return 3
    
def amp_in_volt_to_dbm(volts, Z=50):
    """Convert voltage amplitude to power in dBm."""
    allowed_dBm = np.arange(-11, 17, 3)  # -11 to +16 dBm in 3 dBm steps
    watts = (volts ** 2) / 2 / Z
    dbm = 10 * np.log10(watts / 1e-3)
    dbm = allowed_dBm[allowed_dBm > dbm].min() if np.any(allowed_dBm > dbm) else allowed_dBm.max()
    return int(dbm)

output_power = amp_in_volt_to_dbm(0.45) # dBm
num_qubits = 5

#####################################
# %% ---- Resonator parameters ---- #
#####################################
_resonator_keys = [f"r{i}" for i in range(num_qubits)]
_resonator_absfreq = np.array([6.1, 6.2, 6.3, 6.4, 6.5]) * u.GHz
_resonator_relaxation_times = np.array([3_000, 3_000, 3_000, 3_000, 3_000], dtype = int)

# Readout optimization
_readout_lens = np.array([200, 200, 200, 200, 200]) # ns
_readout_amplitudes = np.array([0.3, 0.3, 0.3, 0.3, 0.3])
_rotation_angles = (np.array([0.0, 0.0, 0.0, 0.0, 0.0]) / 180) * np.pi
_ge_thresholds = np.array([0.0, 0.0, 0.0, 0.0, 0.0]) # Ge thresholds for each qubit

resonator_power = amp_in_volt_to_dbm(0.45) # dBm
resonator_LO = 6.35 * u.GHz
resonator_IFs = _resonator_absfreq - resonator_LO
resonator_LO_band = mw_LO_band(resonator_LO)
resonator_analogOutput = (con, mw_fem, 1) # Controller, FEM, channel
resonator_analogInput = (con, mw_fem, 1) # Controller, FEM, channel
time_of_flight = 308 # ns

# Settings for a default readout
readout_len_default = 5000 # ns
readout_amp_default = 1.0
rotation_angle_default = (0.0 / 180) * np.pi


default_additional_files = {
    Path(__file__).name: Path(__file__).name,
    "optimal_weights.npz": "optimal_weights.npz",
}
opt_weights = False
if opt_weights:
    weights = np.load("optimal_weights.npz")
    opt_weights_real = [(x, weights["division_length"] * 4) for x in weights["weights_real"]]
    opt_weights_minus_imag = [(x, weights["division_length"] * 4) for x in weights["weights_minus_imag"]]
    opt_weights_imag = [(x, weights["division_length"] * 4) for x in weights["weights_imag"]]
    opt_weights_minus_real = [(x, weights["division_length"] * 4) for x in weights["weights_minus_real"]]

# ---- Populate the resonator elements ---- #
resonator_elements = {}
readout_pulses = {}
readout_waveforms = {}
readout_integration_weights = {}
for i, key in enumerate(_resonator_keys):
    resonator_elements[key] = {
        "MWInput":{
            "port":resonator_analogOutput,
            "upconverter": 1, # which upconverter to use (if shared)
        },
        "intermediate_frequency": resonator_IFs[i],
        "MWOutput":{
            "port":resonator_analogInput,
        },
        "operations":{
            "cw": "const_pulse",
            "readout": f"readout_pulse_{i}",
        },
        "time_of_flight":time_of_flight,
    }
    readout_pulses[f"readout_pulse_{i}"] = {
        "operation": "measurement",
        "length": _readout_lens[i],
        "waveforms": {
            "I": f"readout_wf_{i}",
            "Q": "zero_wf",
        },
        "integration_weights": {
            "cos": f"cosine_weights_{i}",
            "sin": f"sine_weights_{i}",
            "minus_sin": f"minus_sine_weights_{i}",
            "rotated_cos": f"rotated_cosine_weights_{i}",
            "rotated_sin": f"rotated_sine_weights_{i}",
            "rotated_minus_sin": f"rotated_minus_sine_weights_{i}",
            "opt_cos": f"opt_cosine_weights_{i}",
            "opt_sin": f"opt_sine_weights_{i}",
            "opt_minus_sin": f"opt_minus_sine_weights_{i}",
        },
        "digital_marker": "ON",
    }
    readout_waveforms[f"readout_wf_{i}"] = {"type": "constant", "sample": _readout_amplitudes[i]}
    readout_integration_weights_i = {
        f"cosine_weights_{i}": {
            "cosine": [(1.0, _readout_lens[i])],
            "sine": [(0.0, _readout_lens[i])],
        },
        f"sine_weights_{i}": {
            "cosine": [(0.0, _readout_lens[i])],
            "sine": [(1.0, _readout_lens[i])],
        },
        f"minus_sine_weights_{i}": {
            "cosine": [(0.0, _readout_lens[i])],
            "sine": [(-1.0, _readout_lens[i])],
        },
        f"rotated_cosine_weights_{i}": {
            "cosine": [(np.cos(_rotation_angles[i]), _readout_lens[i])],
            "sine": [(np.sin(_rotation_angles[i]), _readout_lens[i])],
        },
        f"rotated_sine_weights_{i}": {
            "cosine": [(-np.sin(_rotation_angles[i]), _readout_lens[i])],
            "sine": [(np.cos(_rotation_angles[i]), _readout_lens[i])],
        },
        f"rotated_minus_sine_weights_{i}": {
            "cosine": [(np.sin(_rotation_angles[i]), _readout_lens[i])],
            "sine": [(-np.cos(_rotation_angles[i]), _readout_lens[i])],
        },
    }
    if opt_weights:
        opt_readout_integration_weights_i = {
            f"opt_cosine_weights_{i}": {
                "cosine": opt_weights_real[i],
                "sine": opt_weights_minus_imag[i],
            },
            f"opt_sine_weights_{i}": {
                "cosine": opt_weights_imag[i],
                "sine": opt_weights_real[i],
            },
            f"opt_minus_sine_weights_{i}": {
                "cosine": opt_weights_minus_imag[i],
                "sine": opt_weights_minus_real[i],
            },
        }
    else:
        opt_readout_integration_weights_i = {
            f"opt_cosine_weights_{i}": {
                "cosine": [(np.cos(_rotation_angles[i]), _readout_lens[i])],
                "sine": [(np.sin(_rotation_angles[i]), _readout_lens[i])],
            },
            f"opt_sine_weights_{i}": {
                "cosine": [(-np.sin(_rotation_angles[i]), _readout_lens[i])],
                "sine": [(np.cos(_rotation_angles[i]), _readout_lens[i])],
            },
            f"opt_minus_sine_weights_{i}": {
                "cosine": [(np.sin(_rotation_angles[i]), _readout_lens[i])],
                "sine": [(-np.cos(_rotation_angles[i]), _readout_lens[i])],
            },
        }
    readout_integration_weights = {**readout_integration_weights, **readout_integration_weights_i, **opt_readout_integration_weights_i}

#################################
# %% ---- Qubit parameters ---- #
#################################
_qubit_keys = [f"q{i}" for i in range(num_qubits)]
_qubit_absfreq = np.array([4.2, 4.3, 4.4, 4.57, 4.6]) * u.GHz
_qubit_relaxation_times = np.array([30_000, 30_000, 30_000, 30_000, 30_000], dtype = int) # ns

qubit_power = amp_in_volt_to_dbm(0.45) # dBm
qubit_LO = 4.5 * u.GHz
qubit_IFs = _qubit_absfreq - qubit_LO
qubit_LO_band = mw_LO_band(qubit_LO)
qubit_analogOutput = (con, mw_fem, 2) # Controller, FEM, channel

# ---- Qubit operation parameters ---- #
# Drag pulse parameters
_x180_lens = np.array([40, 40, 40, 40, 40]) # ns
_x180_amplitudes = np.array([0.3, 0.3, 0.3, 0.3, 0.3]) # Amplitude for 180 pulse
_x90_lens = _x180_lens # ns
_x90_amplitudes = _x180_amplitudes / 2 # Amplitude for 90 pulse
_drag_coefficients = np.array([1.0, 1.0, 1.0, 1.0, 1.0]) # DRAG coefficients
_anharmonicities = np.ones(_x180_lens.shape) * -150 * u.MHz
_AC_stark_detunings = np.ones(_x180_lens.shape) * 0.0 * u.MHz

# Saturation_pulse
saturation_len = 10 * u.us
saturation_amp = 0.03
# Square pi pulse
square_pi_len = 100
square_pi_amp = 0.03
# Constant pulse parameters 
const_len = 100
const_amp = 0.03

# ---- Drag pulse parameters & generation ---- #
def generate_drag_x180(drag_coef, anharmonicity, AC_stark_detuning, x180_len, x180_amp):
    x180_sigma = x180_len / 5
    x180_wf, x180_der_wf = np.array(
        drag_gaussian_pulse_waveforms(x180_amp, x180_len, x180_sigma, drag_coef, anharmonicity, AC_stark_detuning)
    )
    x180_I_wf = x180_wf
    x180_Q_wf = x180_der_wf
    # No DRAG when alpha=0, it's just a gaussian.
    return x180_I_wf, x180_Q_wf, x180_len, x180_amp

def generate_drag_x90(drag_coef, anharmonicity, AC_stark_detuning, x90_len, x90_amp):
    x90_sigma = x90_len / 5
    x90_wf, x90_der_wf = np.array(
        drag_gaussian_pulse_waveforms(x90_amp, x90_len, x90_sigma, drag_coef, anharmonicity, AC_stark_detuning)
    )
    x90_I_wf = x90_wf
    x90_Q_wf = x90_der_wf
    # No DRAG when alpha=0, it's just a gaussian.
    return x90_I_wf, x90_Q_wf, x90_len, x90_amp

def generate_drag_minus_x90(drag_coef, anharmonicity, AC_stark_detuning, minus_x90_len, minus_x90_amp):
    minus_x90_sigma = minus_x90_len / 5
    minus_x90_wf, minus_x90_der_wf = np.array(
        drag_gaussian_pulse_waveforms(
            minus_x90_amp,
            minus_x90_len,
            minus_x90_sigma,
            drag_coef,
            anharmonicity,
            AC_stark_detuning,
        )
    )
    minus_x90_I_wf = minus_x90_wf
    minus_x90_Q_wf = minus_x90_der_wf
    # No DRAG when alpha=0, it's just a gaussian.
    return minus_x90_I_wf, minus_x90_Q_wf, minus_x90_len, minus_x90_amp

def generate_drag_y180(drag_coef, anharmonicity, AC_stark_detuning, y180_len, y180_amp):
    y180_sigma = y180_len / 5
    y180_wf, y180_der_wf = np.array(
        drag_gaussian_pulse_waveforms(y180_amp, y180_len, y180_sigma, drag_coef, anharmonicity, AC_stark_detuning)
    )
    y180_I_wf = (-1) * y180_der_wf
    y180_Q_wf = y180_wf
    # No DRAG when alpha=0, it's just a gaussian.
    return y180_I_wf, y180_Q_wf, y180_len, y180_amp

def generate_drag_minus_y90(drag_coef, anharmonicity, AC_stark_detuning, y90_len, y90_amp):
    y90_sigma = y90_len / 5
    y90_wf, y90_der_wf = np.array(
        drag_gaussian_pulse_waveforms(y90_amp, y90_len, y90_sigma, drag_coef, anharmonicity, AC_stark_detuning)
    )
    y90_I_wf = (-1) * y90_der_wf
    y90_Q_wf = y90_wf
    # No DRAG when alpha=0, it's just a gaussian.
    return y90_I_wf, y90_Q_wf, y90_len, y90_amp

def generate_drag_minus_y90(drag_coef, anharmonicity, AC_stark_detuning, minus_y90_len, minus_y90_amp):
    minus_y90_sigma = minus_y90_len / 5
    minus_y90_wf, minus_y90_der_wf = np.array(
        drag_gaussian_pulse_waveforms(
            minus_y90_amp,
            minus_y90_len,
            minus_y90_sigma,
            drag_coef,
            anharmonicity,
            AC_stark_detuning,
        )
    )
    minus_y90_I_wf = (-1) * minus_y90_der_wf
    minus_y90_Q_wf = minus_y90_wf
    # No DRAG when alpha=0, it's just a gaussian.
    return minus_y90_I_wf, minus_y90_Q_wf, minus_y90_len, minus_y90_amp

# ---- Populate the qubit elements ---- #
qubit_elements = {}
qubit_pulses = {}
qubit_waveforms = {}
for i, key in enumerate(_qubit_keys):
    qubit_elements[key] = {
        "MWInput":{
            "port":qubit_analogOutput,
            "upconverter": 1, # which upconverter to use (if shared)
        },
        "intermediate_frequency": qubit_IFs[i],
        "operations":{
            "cw": "const_pulse",
            "saturation": "saturation_pulse",
            "pi": "pi_pulse",
            "pi_half": "pi_half_pulse",
            "x180": f"x180_pulse_{i}",
            "x90": f"x90_pulse_{i}",
            "-x90": f"-x90_pulse_{i}",
            "y90": f"y90_pulse_{i}",
            "y180": f"y180_pulse_{i}",
            "-y90": f"-y90_pulse_{i}",
        },
    }
    x90_I_wf, x90_Q_wf, _x90_len, _x90_amp = generate_drag_x90(_drag_coefficients[i], _anharmonicities[i], _AC_stark_detunings[i], _x90_lens[i], _x90_amplitudes[i])
    x180_I_wf, x180_Q_wf, _x180_len, _x180_amp = generate_drag_x180(_drag_coefficients[i], _anharmonicities[i], _AC_stark_detunings[i], _x180_lens[i], _x180_amplitudes[i])
    minus_x90_I_wf, minus_x90_Q_wf, _minus_x90_len, _minus_x90_amp = generate_drag_minus_x90(_drag_coefficients[i], _anharmonicities[i], _AC_stark_detunings[i], _x90_lens[i], -_x90_amplitudes[i])
    y90_I_wf, y90_Q_wf, _y90_len, _y90_amp = generate_drag_y180(_drag_coefficients[i], _anharmonicities[i], _AC_stark_detunings[i], _x90_lens[i], _x90_amplitudes[i])
    y180_I_wf, y180_Q_wf, _y180_len, _y180_amp = generate_drag_y180(_drag_coefficients[i], _anharmonicities[i], _AC_stark_detunings[i], _x180_lens[i], _x180_amplitudes[i])
    minus_y90_I_wf, minus_y90_Q_wf, _minus_y90_len, _minus_y90_amp = generate_drag_minus_y90(_drag_coefficients[i], _anharmonicities[i], _AC_stark_detunings[i], _x90_lens[i], -_x90_amplitudes[i])
    qubit_i_pulses = {
        f"x90_pulse_{i}": {
            "operation": "control",
            "length": _x90_len,
            "waveforms": {
                "I": f"x90_I_wf_{i}",
                "Q": f"x90_Q_wf_{i}",
            },
        },
        f"x180_pulse_{i}": {
            "operation": "control",
            "length": _x180_len,
            "waveforms": {
                "I": f"x180_I_wf_{i}",
                "Q": f"x180_Q_wf_{i}",
            },
        },
        f"-x90_pulse_{i}": {
            "operation": "control",
            "length": _minus_x90_len,
            "waveforms": {
                "I": f"-x90_I_wf_{i}",
                "Q": f"-x90_Q_wf_{i}",
            },
        },
        f"y90_pulse_{i}": {
            "operation": "control",
            "length": _y90_len,
            "waveforms": {
                "I": f"y90_I_wf_{i}",
                "Q": f"y90_Q_wf_{i}",
            },
        },
        f"y180_pulse_{i}": {
            "operation": "control",
            "length": _y180_len,
            "waveforms": {
                "I": f"y180_I_wf_{i}",
                "Q": f"y180_Q_wf_{i}",
            },
        },
        f"-y90_pulse_{i}": {
            "operation": "control",
            "length": _minus_y90_len,
            "waveforms": {
                "I": f"-y90_I_wf_{i}",
                "Q": f"-y90_Q_wf_{i}",
            },
        },
    }
    qubit_pulses = {**qubit_pulses, **qubit_i_pulses}
    qubit_i_waveforms = {
        f"x90_I_wf_{i}": {"type": "arbitrary", "samples": x90_I_wf.tolist()},
        f"x90_Q_wf_{i}": {"type": "arbitrary", "samples": x90_Q_wf.tolist()},
        f"x180_I_wf_{i}": {"type": "arbitrary", "samples": x180_I_wf.tolist()},
        f"x180_Q_wf_{i}": {"type": "arbitrary", "samples": x180_Q_wf.tolist()},
        f"-x90_I_wf_{i}": {"type": "arbitrary", "samples": minus_x90_I_wf.tolist()},
        f"-x90_Q_wf_{i}": {"type": "arbitrary", "samples": minus_x90_Q_wf.tolist()},
        f"y90_I_wf_{i}": {"type": "arbitrary", "samples": y90_I_wf.tolist()},
        f"y90_Q_wf_{i}": {"type": "arbitrary", "samples": y90_Q_wf.tolist()},
        f"y180_I_wf_{i}": {"type": "arbitrary", "samples": y180_I_wf.tolist()},
        f"y180_Q_wf_{i}": {"type": "arbitrary", "samples": y180_Q_wf.tolist()},
        f"-y90_I_wf_{i}": {"type": "arbitrary", "samples": minus_y90_I_wf.tolist()},
        f"-y90_Q_wf_{i}": {"type": "arbitrary", "samples": minus_y90_Q_wf.tolist()},
    }
    qubit_waveforms  = {**qubit_waveforms, **qubit_i_waveforms}

#%% ---- Create dictionary to parse parameters for multiplexed readout ---- #
multiplexed_parameters = {}
for i, key in enumerate(_qubit_keys):
    multiplexed_parameters[key] = {
        "qubit_key": _qubit_keys[i],
        "resonator_key": _resonator_keys[i],
        "readout_len": _readout_lens[i],
        "readout_amp": _readout_amplitudes[i],
        "rotation_angle": _rotation_angles[i],
        "ge_threshold": _ge_thresholds[i],
        "resonator_frequency": _resonator_absfreq[i],
        "qubit_frequency": _qubit_absfreq[i],
        "qubit_relaxation": _qubit_relaxation_times[i],
        "drag_coef": _drag_coefficients[i],
        "anharmonicity": _anharmonicities[i],
        "resonator_relaxation": _resonator_relaxation_times[i],
        "x180_len": _x180_lens[i],
        "x180_amp": _x180_amplitudes[i],
        "x90_len": _x90_lens[i],
        "x90_amp": _x90_amplitudes[i],
    }

# %% Extra definitions
# Not hooked up, but here if required.
flux_analogOutput = (con, lf_fem, 1) # Controller, FEM, channel
const_flux_len = 100 # ns
const_flux_amp = 0.3

# For detault control pulses
drag_coef_default = 0
anharmonicity_default = -150 * u.MHz
AC_stark_detuning_default = 0 * u.MHz
x180_len_default = 40
x180_amp_default = 1.0

# %% ---- Config ---- #
config = {
    "version": 1, 
    "controllers":{
        con:{
            "type":"opx1000",
            "fems":{
                # declaring MW-FEM for qubit control and resonator readout
                mw_fem: {
                    "type":"MW",
                    "analog_outputs":{ 
                        1:{
                            "band":resonator_LO_band,
                            "full_scale_power_dbm":resonator_power,
                            "upconverters":{
                                1:{"frequency":resonator_LO},
                            },
                        },  # Resonators
                        2:{
                            "band":qubit_LO_band,
                            "full_scale_power_dbm":qubit_power,
                            "upconverters":{
                                1:{"frequency":qubit_LO},
                            },
                        },  # Qubits
                    },
                    "analog_inputs":{
                        1:{
                            "band":resonator_LO_band, 
                            "downconverter_frequency":resonator_LO,
                        }, # resonator in
                    },
                    "digital_outputs":{ 
                        1: {}, # marker for readout pulse
                    },
                },
                # declaring LF-FEM for flux_line (unused for fixed transmons)
                lf_fem:{
                    "type":"LF",
                    "analog_outputs":{ 
                        1:{
                            "offset":0,
                            "delay":0,
                            "output_mode":"direct",
                        },  # unused for fixed transmons
                    },
                }
            }
        }
    },
    "elements":{
        **qubit_elements,
        **resonator_elements,
        "flux_line":{
            "singleInput":{
                "port":flux_analogOutput,
            }, 
            "sticky":{
                "analog":True,
            }, 
            "operations": {
                "const": "const_flux_pulse",
            }, 
        }, 
    }, 
    "pulses":{
        "const_pulse": {
            "operation": "control",
            "length": const_len,
            "waveforms": {
                "I": "const_wf",
                "Q": "zero_wf",
            },
        },
        "saturation_pulse":{
            "operation":"control",
            "length":saturation_len,
            "waveforms":{
                "I":"saturation_wf",
                "Q":"zero_wf",
            },
        },
        "pi_pulse": {
            "operation": "control",
            "length": square_pi_len,
            "waveforms": {
                "I": "pi_wf",
                "Q": "zero_wf",
            },
        },
        "pi_half_pulse": {
            "operation": "control",
            "length": square_pi_len,
            "waveforms": {
                "I": "pi_half_wf",
                "Q": "zero_wf",
            },
        },
        **readout_pulses,
        **qubit_pulses,
        "const_single_pulse": {
            "operation": "control",
            "length": const_len,
            "waveforms": {
                "single": "const_wf",
            },
        },
        "const_flux_pulse": {
            "operation": "control",
            "length": const_flux_len,
            "waveforms": {
                "single": "const_flux_wf",
            },
        },
    },
    "waveforms": {
        "const_wf": {"type": "constant", "sample": const_amp},
        "saturation_wf": {"type": "constant", "sample": saturation_amp},
        "pi_wf": {"type": "constant", "sample": square_pi_amp},
        "pi_half_wf": {"type": "constant", "sample": square_pi_amp / 2},
        "const_flux_wf": {"type": "constant", "sample": const_flux_amp},
        "zero_wf": {"type": "constant", "sample": 0.0},
        **readout_waveforms,
        **qubit_waveforms,
    },
    "digital_waveforms": {
        "ON": {"samples": [(1, 0)]},
    },
    "integration_weights":{
        **readout_integration_weights,
    },
}