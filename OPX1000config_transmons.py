
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

# %% ---- Resonator parameters ---- #
resonator_absfreq = np.linspace(5.9, 6.8, num_qubits) * u.GHz
resonator_LO = 6.35 * u.GHz
resonator_IFs = resonator_absfreq - resonator_LO
resonator_LO_band = mw_LO_band(resonator_LO)
resonator_analogOutput = (con, mw_fem, 1) # Controller, FEM, channel
resonator_analogInput = (con, mw_fem, 1) # Controller, FEM, channel
time_of_flight = 32 # ns
resonator_keys = [f"r{i}" for i in range(len(resonator_absfreq))]
# ---- Populate the resonator elements ----
resonator_elements = {}
for i, key in enumerate(resonator_keys):
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
            "readout": "readout_pulse",
        },
        "time_of_flight":time_of_flight,
    }
# ---- Readout parameters ---- #
readout_len = 4000 # ns
readout_amp = 0.3
# ---- Integration weights ---- #
w_plus = [(1.0, readout_len)]
w_zero = [(0.0, readout_len)]
w_minus = [(-1.0, readout_len)]

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
else:
    opt_weights_real = [(1.0, readout_len)]
    opt_weights_minus_imag = [(0.0, readout_len)]
    opt_weights_imag = [(0.0, readout_len)]
    opt_weights_minus_real = [(-1.0, readout_len)]

# IQ Plane Angle
rotation_angle = (0 / 180) * np.pi
# Threshold for single shot g-e discrimination
ge_threshold = 0.0


# %% ---- Qubit parameters ---- #
qubit_absfreq = np.linspace(4.3, 5.2, num_qubits) * u.GHz
qubit_LO = 4.75 * u.GHz
qubit_IFs = qubit_absfreq - qubit_LO
qubit_LO_band = mw_LO_band(qubit_LO)
qubit_analogOutput = (con, mw_fem, 1) # Controller, FEM, channel
qubit_analogInput = (con, mw_fem, 1) # Controller, FEM, channel
time_of_flight = 32 # ns
qubit_keys = [f"q{i}" for i in range(len(qubit_absfreq))]
# ---- Populate the qubit elements ----
qubit_elements = {}
for i, key in enumerate(qubit_keys):
    qubit_elements[key] = {
        "MWInput":{
            "port":qubit_analogOutput,
            "upconverter": 2, # which upconverter to use (if shared)
        },
        "intermediate_frequency": qubit_IFs[i],
        "operations":{
            "cw": "const_pulse",
            "saturation": "saturation_pulse",
            "pi": "pi_pulse",
            "pi_half": "pi_half_pulse",
            "x180": "x180_pulse",
            "x90": "x90_pulse",
            "-x90": "-x90_pulse",
            "y90": "y90_pulse",
            "y180": "y180_pulse",
            "-y90": "-y90_pulse",
        },
    }
# ---- Qubit operation parameters ---- #
# Saturation_pulse
saturation_len = 10 * u.us
saturation_amp = 0.03
# Square pi pulse
square_pi_len = 100
square_pi_amp = 0.03
# Constant pulse parameters 
const_len = 100
const_amp = 0.03




# %% ---- Drag pulse parameters ---- #
drag_coef = 0
anharmonicity = -150 * u.MHz
AC_stark_detuning = 0 * u.MHz

x180_len = 40
x180_sigma = x180_len / 5
x180_amp = 1
x180_wf, x180_der_wf = np.array(
    drag_gaussian_pulse_waveforms(x180_amp, x180_len, x180_sigma, drag_coef, anharmonicity, AC_stark_detuning)
)
x180_I_wf = x180_wf
x180_Q_wf = x180_der_wf
# No DRAG when alpha=0, it's just a gaussian.

x90_len = x180_len
x90_sigma = x90_len / 5
x90_amp = x180_amp / 2
x90_wf, x90_der_wf = np.array(
    drag_gaussian_pulse_waveforms(x90_amp, x90_len, x90_sigma, drag_coef, anharmonicity, AC_stark_detuning)
)
x90_I_wf = x90_wf
x90_Q_wf = x90_der_wf
# No DRAG when alpha=0, it's just a gaussian.

minus_x90_len = x180_len
minus_x90_sigma = minus_x90_len / 5
minus_x90_amp = -x90_amp
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

y180_len = x180_len
y180_sigma = y180_len / 5
y180_amp = x180_amp
y180_wf, y180_der_wf = np.array(
    drag_gaussian_pulse_waveforms(y180_amp, y180_len, y180_sigma, drag_coef, anharmonicity, AC_stark_detuning)
)
y180_I_wf = (-1) * y180_der_wf
y180_Q_wf = y180_wf
# No DRAG when alpha=0, it's just a gaussian.

y90_len = x180_len
y90_sigma = y90_len / 5
y90_amp = y180_amp / 2
y90_wf, y90_der_wf = np.array(
    drag_gaussian_pulse_waveforms(y90_amp, y90_len, y90_sigma, drag_coef, anharmonicity, AC_stark_detuning)
)
y90_I_wf = (-1) * y90_der_wf
y90_Q_wf = y90_wf
# No DRAG when alpha=0, it's just a gaussian.

minus_y90_len = y180_len
minus_y90_sigma = minus_y90_len / 5
minus_y90_amp = -y90_amp
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

# %% Extra definitions
flux_analogOutput = (con, lf_fem, 1) # Controller, FEM, channel
const_flux_len = 100 # ns
const_flux_amp = 0.3

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
                            "full_scale_power_dbm":output_power,
                            "upconverters":{
                                1:{"frequency":resonator_LO},
                                2:{"frequency":qubit_LO}
                            },
                        },  # qubit, resonator shared analog output
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
        "x90_pulse": {
            "operation": "control",
            "length": x90_len,
            "waveforms": {
                "I": "x90_I_wf",
                "Q": "x90_Q_wf",
            },
        },
        "x180_pulse": {
            "operation": "control",
            "length": x180_len,
            "waveforms": {
                "I": "x180_I_wf",
                "Q": "x180_Q_wf",
            },
        },
        "-x90_pulse": {
            "operation": "control",
            "length": minus_x90_len,
            "waveforms": {
                "I": "minus_x90_I_wf",
                "Q": "minus_x90_Q_wf",
            },
        },
        "y90_pulse": {
            "operation": "control",
            "length": y90_len,
            "waveforms": {
                "I": "y90_I_wf",
                "Q": "y90_Q_wf",
            },
        },
        "y180_pulse": {
            "operation": "control",
            "length": y180_len,
            "waveforms": {
                "I": "y180_I_wf",
                "Q": "y180_Q_wf",
            },
        },
        "-y90_pulse": {
            "operation": "control",
            "length": minus_y90_len,
            "waveforms": {
                "I": "minus_y90_I_wf",
                "Q": "minus_y90_Q_wf",
            },
        },
        "readout_pulse": {
            "operation": "measurement",
            "length": readout_len,
            "waveforms": {
                "I": "readout_wf",
                "Q": "zero_wf",
            },
            "integration_weights": {
                "cos": "cosine_weights",
                "sin": "sine_weights",
                "minus_sin": "minus_sine_weights",
                "rotated_cos": "rotated_cosine_weights",
                "rotated_sin": "rotated_sine_weights",
                "rotated_minus_sin": "rotated_minus_sine_weights",
                "opt_cos": "opt_cosine_weights",
                "opt_sin": "opt_sine_weights",
                "opt_minus_sin": "opt_minus_sine_weights",
            },
            "digital_marker": "ON",
        },
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
        "x90_I_wf": {"type": "arbitrary", "samples": x90_I_wf.tolist()},
        "x90_Q_wf": {"type": "arbitrary", "samples": x90_Q_wf.tolist()},
        "x180_I_wf": {"type": "arbitrary", "samples": x180_I_wf.tolist()},
        "x180_Q_wf": {"type": "arbitrary", "samples": x180_Q_wf.tolist()},
        "minus_x90_I_wf": {"type": "arbitrary", "samples": minus_x90_I_wf.tolist()},
        "minus_x90_Q_wf": {"type": "arbitrary", "samples": minus_x90_Q_wf.tolist()},
        "y90_Q_wf": {"type": "arbitrary", "samples": y90_Q_wf.tolist()},
        "y90_I_wf": {"type": "arbitrary", "samples": y90_I_wf.tolist()},
        "y180_Q_wf": {"type": "arbitrary", "samples": y180_Q_wf.tolist()},
        "y180_I_wf": {"type": "arbitrary", "samples": y180_I_wf.tolist()},
        "minus_y90_Q_wf": {"type": "arbitrary", "samples": minus_y90_Q_wf.tolist()},
        "minus_y90_I_wf": {"type": "arbitrary", "samples": minus_y90_I_wf.tolist()},
        "readout_wf": {"type": "constant", "sample": readout_amp},
    },
    "digital_waveforms": {
        "ON": {"samples": [(1, 0)]},
    },
    "integration_weights":{
        "integW_cos":{
            "cosine":w_plus,
            "sine":w_zero,
        },
        "cosine_weights": {
            "cosine": w_plus,
            "sine": w_zero,
        },
        "sine_weights": {
            "cosine": w_zero,
            "sine": w_plus,
        },
        "minus_sine_weights": {
            "cosine": w_zero,
            "sine": w_minus,
        },
        "opt_cosine_weights": {
            "cosine": opt_weights_real,
            "sine": opt_weights_minus_imag,
        },
        "opt_sine_weights": {
            "cosine": opt_weights_imag,
            "sine": opt_weights_real,
        },
        "opt_minus_sine_weights": {
            "cosine": opt_weights_minus_imag,
            "sine": opt_weights_minus_real,
        },
        "rotated_cosine_weights": {
            "cosine": [(np.cos(rotation_angle), readout_len)],
            "sine": [(np.sin(rotation_angle), readout_len)],
        },
        "rotated_sine_weights": {
            "cosine": [(-np.sin(rotation_angle), readout_len)],
            "sine": [(np.cos(rotation_angle), readout_len)],
        },
        "rotated_minus_sine_weights": {
            "cosine": [(np.sin(rotation_angle), readout_len)],
            "sine": [(-np.cos(rotation_angle), readout_len)],
        },
    },
}