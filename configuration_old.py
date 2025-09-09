"""
QUA-Config supporting OPX1000 w/ MW-FEM
"""

from pathlib import Path

import numpy as np
import plotly.io as pio
from qualang_tools.config.waveform_tools import drag_gaussian_pulse_waveforms
from qualang_tools.units import unit

pio.renderers.default = "browser"

#######################
# AUXILIARY FUNCTIONS #
#######################
u = unit(coerce_to_integer=True)


def choose_band(LO_frequency):
    # 1 : 50 MHz - 5.5 GHz, 2 : 4.5 GHz - 7.5 GHz, 3 : 6.5 GHz - 10.5 GHz
    if 50 * u.MHz <= LO_frequency < 5 * u.GHz:
        return 1
    elif LO_frequency < 7 * u.GHz:
        return 2
    elif LO_frequency < 11.5 * u.GHz:
        return 3
    else:
        raise ValueError("LO frequency out of range for band selection.")


######################
# Network parameters #
######################
qop_ip = "192.168.88.254"  # Write the QM router IP address
cluster_name = "Cluster_nakamura"  # Write your cluster_name if version >= QOP220
qop_port = None  # Write the QOP port if version < QOP220

#############
# Save Path #
############
# Path to save data
save_dir = Path(__file__).parent.resolve() / "Data"
save_dir.mkdir(exist_ok=True)

default_additional_files = {
    Path(__file__).name: Path(__file__).name,
    "optimal_weights.npz": "optimal_weights.npz",
}

#####################
# OPX configuration #
#####################

con = "con1"
fem = 2
qubit_port = 7
resonator_port = 1
# Set octave_config to None if no octave are present
octave_config = None

#############################################
#                  Qubits                   #
#############################################

qubit_LO = 4.9 * u.GHz
qubit_IF = 45 * u.MHz + 86 * u.kHz
qubit_power = 10  # power in dBm at waveform amp = 1 (steps of 3 dB)

qubit_T1 = int(36 * u.us)
thermalization_time = 5 * qubit_T1

# Note: amplitudes can be -1..1 and are scaled up to `qubit_power` at amp=1
# Continuous wave
const_len = 100
const_amp = 0.03
# Saturation_pulse
saturation_len = 10 * u.us
saturation_amp = 0.1
# Square pi pulse
square_pi_len = 100
square_pi_amp = 0.1
# Drag pulses
drag_coef = 0.96
anharmonicity = -200 * u.MHz
AC_stark_detuning = -0.517 * u.MHz

x180_len = 52
x180_sigma = x180_len / 5
x180_amp = 0.0935
x180_wf, x180_der_wf = np.array(
    drag_gaussian_pulse_waveforms(
        x180_amp, x180_len, x180_sigma, drag_coef, anharmonicity, AC_stark_detuning
    )
)
x180_I_wf = x180_wf
x180_Q_wf = x180_der_wf
# No DRAG when alpha=0, it's just a gaussian.

x90_len = x180_len
x90_sigma = x90_len / 5
x90_amp = x180_amp / 2
x90_wf, x90_der_wf = np.array(
    drag_gaussian_pulse_waveforms(
        x90_amp, x90_len, x90_sigma, drag_coef, anharmonicity, AC_stark_detuning
    )
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
    drag_gaussian_pulse_waveforms(
        y180_amp, y180_len, y180_sigma, drag_coef, anharmonicity, AC_stark_detuning
    )
)
y180_I_wf = (-1) * y180_der_wf
y180_Q_wf = y180_wf
# No DRAG when alpha=0, it's just a gaussian.

y90_len = x180_len
y90_sigma = y90_len / 5
y90_amp = y180_amp / 2
y90_wf, y90_der_wf = np.array(
    drag_gaussian_pulse_waveforms(
        y90_amp, y90_len, y90_sigma, drag_coef, anharmonicity, AC_stark_detuning
    )
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

#############################################
#                Resonators                 #
#############################################
resonator_LO = 7.4 * u.GHz
resonator_IF = -302 * u.MHz
resonator_power = -2  # power in dBm at waveform amp = 1 (steps of 3 dB)

# Note: amplitudes can be -1..1 and are scaled up to `resonator_power` at amp=1
readout_len = 2320
readout_amp = 0.07
# readout_amp = 1 # use 1 before amplitude scan

time_of_flight = 356  # min is 28
depletion_time = 180 * u.ns

opt_weights = False
if opt_weights:
    weights = np.load("optimal_weights.npz")
    opt_weights_real = [
        (x, weights["division_length"] * 4) for x in weights["weights_real"]
    ]
    opt_weights_minus_imag = [
        (x, weights["division_length"] * 4) for x in weights["weights_minus_imag"]
    ]
    opt_weights_imag = [
        (x, weights["division_length"] * 4) for x in weights["weights_imag"]
    ]
    opt_weights_minus_real = [
        (x, weights["division_length"] * 4) for x in weights["weights_minus_real"]
    ]
else:
    opt_weights_real = [(1.0, readout_len)]
    opt_weights_minus_imag = [(0.0, readout_len)]
    opt_weights_imag = [(0.0, readout_len)]
    opt_weights_minus_real = [(-1.0, readout_len)]

# IQ Plane
rotation_angle = (64.2 / 180) * np.pi
ge_threshold = -8.720e-05

#############################################
#                   Flux                    #
#############################################
qubit_flux_map = {
    "qB1": ("con1", 5, 1, -0.06600390269981624),
    "qB2": ("con1", 5, 2, 0.44634205079699796),
    "qB3": ("con1", 5, 3, 0.049262869748781746),
    "qB4": ("con1", 5, 4, -0.11500393560177126),
    "qB5": ("con1", 5, 5, -0.08819246314495716),
    "qC1": ("con1", 5, 6, 0.045121323857095955),
    "qC2": ("con1", 5, 7, 0.11902848429321082),
    "qC3": ("con1", 5, 8, -0.12075252364823641),
    "qC4": ("con1", 6, 1, 0.14215751519648723),
    "qC5": ("con1", 6, 2, 0.02241909812516478),
}

flux_fem = {
    fem: {
        "type": "LF",
        "analog_outputs": {
            port: {
                "delay": 0,
                "shareable": False,
                "sampling_rate": 1e9,
                "upsampling_mode": "pulse",
                "output_mode": "direct",
                "offset": offset,
            }
            for qb, (con, fem_id, port, offset) in qubit_flux_map.items()
            if fem_id == fem
        },
    }
    for fem in {fem_id for _, (con, fem_id, _, _) in qubit_flux_map.items()}
}

#############################################
#                  Config                   #
#############################################
config = {
    "version": 1,
    "controllers": {
        con: {
            "type": "opx1000",
            "fems": {
                fem: {
                    # The keyword "band" refers to the following frequency bands:
                    #   1: (50 MHz - 5.5 GHz)
                    #   2: (4.5 GHz - 7.5 GHz)
                    #   3: (6.5 GHz - 10.5 GHz)
                    # Note that the "coupled" ports O1 & I1, O2 & O3, O4 & O5, O6 & O7, and O8 & I2
                    # must be in the same band, or in bands 1 & 3 (that is, if you assign band 2 to one of the coupled ports, the other must use the same band).
                    # The keyword "full_scale_power_dbm" is the maximum power of
                    # normalized pulse waveforms in [-1,1]. To convert to voltage,
                    #   power_mw = 10**(full_scale_power_dbm / 10)
                    #   max_voltage_amp = np.sqrt(2 * power_mw * 50 / 1000)
                    #   amp_in_volts = waveform * max_voltage_amp
                    #   ^ equivalent to OPX+ amp
                    # Its range is -41dBm to +10dBm with 3dBm steps.
                    "type": "MW",
                    "analog_outputs": {
                        resonator_port: {
                            "band": choose_band(resonator_LO),
                            "full_scale_power_dbm": resonator_power,
                            "upconverters": {1: {"frequency": resonator_LO}},
                        },  # resonator
                        qubit_port: {
                            "band": choose_band(qubit_LO),
                            "full_scale_power_dbm": qubit_power,
                            "upconverters": {1: {"frequency": qubit_LO}},
                        },  # qubit
                    },
                    "digital_outputs": {},
                    "analog_inputs": {
                        resonator_port: {
                            "band": choose_band(resonator_LO),
                            "downconverter_frequency": resonator_LO,
                        },  # for down-conversion
                    },
                },
                **flux_fem,
            },
        },
    },
    "elements": {
        "resonator": {
            "MWInput": {
                "port": (con, fem, resonator_port),
                "upconverter": 1,
            },
            "intermediate_frequency": resonator_IF,
            "operations": {
                "cw": "const_pulse",
                "readout": "readout_pulse",
            },
            "MWOutput": {
                "port": (con, fem, resonator_port),
            },
            "time_of_flight": time_of_flight,
            "smearing": 0,
        },
        "qubit": {
            "MWInput": {
                "port": (con, fem, qubit_port),
                "upconverter": 1,
            },
            "intermediate_frequency": qubit_IF,
            "operations": {
                "cw": "const_pulse",
                "saturation": "saturation_pulse",
                "pi": "square_pi_pulse",
                "pi_half": "square_pi_half_pulse",
                "x90": "x90_pulse",
                "x180": "x180_pulse",
                "-x90": "-x90_pulse",
                "y90": "y90_pulse",
                "y180": "y180_pulse",
                "-y90": "-y90_pulse",
            },
        },
    },
    "pulses": {
        "const_pulse": {
            "operation": "control",
            "length": const_len,
            "waveforms": {
                "I": "const_wf",
                "Q": "zero_wf",
            },
        },
        "square_pi_pulse": {
            "operation": "control",
            "length": square_pi_len,
            "waveforms": {
                "I": "square_pi_wf",
                "Q": "zero_wf",
            },
        },
        "square_pi_half_pulse": {
            "operation": "control",
            "length": square_pi_len,
            "waveforms": {
                "I": "square_pi_half_wf",
                "Q": "zero_wf",
            },
        },
        "saturation_pulse": {
            "operation": "control",
            "length": saturation_len,
            "waveforms": {"I": "saturation_drive_wf", "Q": "zero_wf"},
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
    },
    "waveforms": {
        "const_wf": {"type": "constant", "sample": const_amp},
        "saturation_drive_wf": {"type": "constant", "sample": saturation_amp},
        "square_pi_wf": {"type": "constant", "sample": square_pi_amp},
        "square_pi_half_wf": {"type": "constant", "sample": square_pi_amp / 2},
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
    "integration_weights": {
        "cosine_weights": {
            "cosine": [(1.0, readout_len)],
            "sine": [(0.0, readout_len)],
        },
        "sine_weights": {
            "cosine": [(0.0, readout_len)],
            "sine": [(1.0, readout_len)],
        },
        "minus_sine_weights": {
            "cosine": [(0.0, readout_len)],
            "sine": [(-1.0, readout_len)],
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
