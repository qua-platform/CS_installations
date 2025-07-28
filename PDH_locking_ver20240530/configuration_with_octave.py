import numpy as np
from pathlib import Path
from qualang_tools.units import unit
from qualang_tools.config.waveform_tools import drag_gaussian_pulse_waveforms
from set_octave import OctaveUnit, octave_declaration


#############
# VARIABLES #
#############

qop_ip = "127.0.0.1"  # Write the QM router IP address
cluster_name = None  # Write your cluster_name if version >= QOP220
qop_port = None  # Write the QOP port if version < QOP220


############################
# Set octave configuration #
############################
# The Octave port is 11xxx, where xxx are the last three digits of the Octave internal IP that can be accessed from
# the OPX admin panel if you QOP version is >= QOP220. Otherwise, it is 50 for Octave1, then 51, 52 and so on.
octave_1 = OctaveUnit("octave1", qop_ip, port=11050, con="con1")
# Add the octaves
octaves = [octave_1]
# Configure the Octaves
octave_config = octave_declaration(octaves)


#############
# Save Path #
#############

# Path to base directories for script and data
base_dir = Path(__file__).resolve().parent
save_dir = base_dir / "Data"
save_dir.mkdir(parents=True, exist_ok=True)


#########
# Units #
#########
u = unit(coerce_to_integer=True)


#############################################
#                  Qubits                   #
#############################################
qubit_LO = 5.25 * u.GHz  # Used only for mixer correction and frequency rescaling for plots or computation

# Qubits IF
qubit_IF = -50 * u.MHz
qubit_IF_ef = -150 * u.MHz

# Relaxation time
qubit_T1 = 3 * u.us
thermalization_time = 5 * qubit_T1

# CW pulse paramter
const_len = 1000
const_amp = 0.125 # V
# Saturation pulse
saturation_len = 10 * u.us 
saturation_amp = 0.125 # V
# Pi pulse
# pi_len = 40 # ns
pi_len = 260 # ns
assert pi_len % 5 == 0
pi_sigma = pi_len / 5
pi_amp = 0.0215*4

# DRAG coefficients
drag_coef = 0
anharmonicity = -320 * u.MHz
AC_stark_detuning = -200 * u.MHz
drag_params = pi_len, pi_sigma, drag_coef, anharmonicity, AC_stark_detuning

# DRAG waveforms

# DRAG waveforms
# x180. No DRAG when alpha=0, it's just a gaussian.
x180_wf, x180_der_wf = np.array(drag_gaussian_pulse_waveforms(pi_amp, *drag_params))
x180_I_wf = x180_wf
x180_Q_wf = x180_der_wf

# x90. No DRAG when alpha=0, it's just a gaussian.
x90_wf, x90_der_wf = np.array(drag_gaussian_pulse_waveforms(pi_amp / 2, *drag_params))
x90_I_wf = x90_wf
x90_Q_wf = x90_der_wf

# minus_x90. No DRAG when alpha=0, it's just a gaussian.
minus_x90_wf, minus_x90_der_wf = np.array(drag_gaussian_pulse_waveforms(-pi_amp / 2, *drag_params))
minus_x90_I_wf = minus_x90_wf
minus_x90_Q_wf = minus_x90_der_wf

# y180. No DRAG when alpha=0, it's just a gaussian.
y180_wf, y180_der_wf = np.array(drag_gaussian_pulse_waveforms(pi_amp, *drag_params))
y180_I_wf = (-1) * y180_der_wf
y180_Q_wf = y180_wf

# y90. No DRAG when alpha=0, it's just a gaussian.
y90_wf, y90_der_wf = np.array(drag_gaussian_pulse_waveforms(pi_amp / 2, *drag_params))
y90_I_wf = (-1) * y90_der_wf
y90_Q_wf = y90_wf

# minus_y90. No DRAG when alpha=0, it's just a gaussian.
minus_y90_wf, minus_y90_der_wf = np.array(drag_gaussian_pulse_waveforms(-pi_amp / 2, *drag_params))
minus_y90_I_wf = (-1) * minus_y90_der_wf
minus_y90_Q_wf = minus_y90_wf


#############################################
#                Resonators                 #
#############################################
resonator_LO = 7.25 * u.GHz # Used only for mixer correction and frequency rescaling for plots or computation
# Resonators IF
resonator_IF = 125 * u.MHz
# Resonantor phase shift 
resonator_phase = 0.3
# Readout pulse parameters
readout_len = 1000
readout_amp = 0.125

# TOF and depletion time
time_of_flight = 24  # must be a multiple of 4
depletion_time = 2 * u.us


#############################################
#                  POUND                    #
#############################################
pdh_mod_len = 2_000
pdh_mod_IF = 20 * u.MHz
pdh_mod_amp = 0.5

pdh_demod_len = pdh_mod_len
pdh_carrier_len = pdh_mod_len
pdh_mod_high_len  = pdh_mod_len
pdh_mod_low_len = pdh_mod_len

pdh_demod_IF = resonator_IF + pdh_mod_IF
pdh_carrier_IF = resonator_IF
pdh_mod_high_IF  = resonator_IF + pdh_mod_IF
pdh_mod_low_IF = resonator_IF - pdh_mod_IF

pdh_demod_amp = 0.0
pdh_carrier_amp = readout_amp
pdh_mod_high_amp  = + 0.5 * pdh_mod_amp * readout_amp
pdh_mod_low_amp = - 0.5 * pdh_mod_amp * readout_amp


#############################################
#                  Config                   #
#############################################
config = {
    "version": 1,
    "controllers": {
        "con1": {
            "analog_outputs": {
                1: {"offset": 0.0},  # I readout / PDH mod,demod line
                2: {"offset": 0.0},  # Q readout / PDH mod,demod line
                3: {"offset": 0.0},  # I qubit XY
                4: {"offset": 0.0},  # Q qubit XY
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
    "elements": {
        "rr": {
            "RF_inputs": {"port": ("octave1", 1)},
            "RF_outputs": {"port": ("octave1", 1)},
            "intermediate_frequency": resonator_IF,
            "operations": {
                "cw": "const_pulse",
                "readout": "readout_pulse",
                "pdh_carrier": "pdh_carrier_pulse",
            },
            "time_of_flight": time_of_flight,
            "smearing": 0,
        },
        "rr_sb_high": {
            "RF_inputs": {"port": ("octave1", 1)},
            "intermediate_frequency": pdh_mod_high_IF,
            "operations": {
                "pdh_modulation": "pdh_mod_high_pulse",
            },
        },
        "rr_sb_low": {
            "RF_inputs": {"port": ("octave1", 1)},
            "intermediate_frequency": pdh_mod_low_IF,
            "operations": {
                "pdh_modulation": "pdh_mod_low_pulse",
            },
        },
        "q_xy": {
            "RF_inputs": {"port": ("octave1", 2)},
            "intermediate_frequency": qubit_IF,
            "operations": {
                "cw": "const_pulse",
                "saturation": "saturation_pulse",
                "x180": "x180_pulse",
                "x90": "x90_pulse",
                "-x90": "-x90_pulse",
                "y90": "y90_pulse",
                "y180": "y180_pulse",
                "-y90": "-y90_pulse",
            },
        },
        "pdh_demod": {
            "RF_inputs": {"port": ("octave1", 1)},
            "RF_outputs": {"port": ("octave1", 1)},
            "intermediate_frequency": pdh_mod_IF,
            "operations": {
                "readout": "pdh_demod_pulse",
            },
            "time_of_flight": time_of_flight,
            "smearing": 0,
        },
    },
    "octaves": {
        "octave1": {
            "RF_outputs": {
                1: {
                    "LO_frequency": resonator_LO,
                    "LO_source": "internal",
                    "output_mode": "always_on",
                    "gain": -20,
                },
                2: {
                    "LO_frequency": qubit_LO,
                    "LO_source": "internal",
                    "output_mode": "always_on",
                    "gain": 0,
                },
            },
            "RF_inputs": {
                1: {
                    "LO_frequency": resonator_LO,
                    "LO_source": "internal",
                },
            },
            "connectivity": "con1",
        }
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
        "saturation_pulse": {
            "operation": "control",
            "length": saturation_len,
            "waveforms": {
                "I": "saturation_wf",
                "Q": "zero_wf",
            },
        },
        "x90_pulse": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "x90_I_wf",
                "Q": "x90_Q_wf",
            },
        },
        "x180_pulse": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "x180_I_wf",
                "Q": "x180_Q_wf",
            },
        },
        "-x90_pulse": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "minus_x90_I_wf",
                "Q": "minus_x90_Q_wf",
            },
        },
        "y90_pulse": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "y90_I_wf",
                "Q": "y90_Q_wf",
            },
        },
        "y180_pulse": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "y180_I_wf",
                "Q": "y180_Q_wf",
            },
        },
        "-y90_pulse": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "minus_y90_I_wf",
                "Q": "minus_y90_Q_wf",
            },
        },
        "pdh_carrier_pulse": {
            "operation": "control",
            "length": pdh_carrier_len,
            "waveforms": {
                "I": "pdh_carrier_wf",
                "Q": "zero_wf",
            },
        },
        "pdh_mod_high_pulse": {
            "operation": "control",
            "length": pdh_mod_high_len,
            "waveforms": {
                "I": "pdh_mod_high_wf",
                "Q": "zero_wf",
            },
        },
        "pdh_mod_low_pulse": {
            "operation": "control",
            "length": pdh_mod_low_len,
            "waveforms": {
                "I": "pdh_mod_low_wf",
                "Q": "zero_wf",
            },
        },
        "pdh_demod_pulse": {
            "operation": "measurement",
            "length": pdh_demod_len,
            "waveforms": {
                "I": "zero_wf",
                "Q": "zero_wf",
            },
            "integration_weights": {
                "cos": "pdh_cosine_weights",
                "sin": "pdh_sine_weights",
                "minus_sin": "pdh_minus_sine_weights",
            },
            "digital_marker": "ON",
        },
        "readout_pulse": {
            "operation": "measurement",
            "length": readout_len,
            "waveforms": {
                "I": "readout_wf",
                "Q": "zero_wf",
            },
            "integration_weights": {
                "cos": "rr_cosine_weights",
                "sin": "rr_sine_weights",
                "minus_sin": "rr_minus_sine_weights",
            },
            "digital_marker": "ON",
        },
    },
    "waveforms": {
        "const_wf": {"type": "constant", "sample": const_amp},
        "saturation_wf": {"type": "constant", "sample": saturation_amp},
        "zero_wf": {"type": "constant", "sample": 0.0},
        "readout_wf": {"type": "constant", "sample": readout_amp},
        "pdh_carrier_wf": {"type": "constant", "sample": pdh_carrier_amp},
        "pdh_mod_high_wf": {"type": "constant", "sample": pdh_mod_high_amp},
        "pdh_mod_low_wf": {"type": "constant", "sample": pdh_mod_low_amp},
        "x90_I_wf": {"type": "arbitrary", "samples": x90_I_wf.tolist()},
        "x90_Q_wf": {"type": "arbitrary", "samples": x90_Q_wf.tolist()},
        "x180_I_wf": {"type": "arbitrary", "samples": x180_I_wf.tolist()},
        "x180_Q_wf": {"type": "arbitrary", "samples": x180_Q_wf.tolist()},
        "minus_x90_I_wf": {"type": "arbitrary", "samples": minus_x90_I_wf.tolist()},
        "minus_x90_Q_wf": {"type": "arbitrary", "samples": minus_x90_Q_wf.tolist()},
        "y90_I_wf": {"type": "arbitrary", "samples": y90_I_wf.tolist()},
        "y90_Q_wf": {"type": "arbitrary", "samples": y90_Q_wf.tolist()},
        "y180_I_wf": {"type": "arbitrary", "samples": y180_I_wf.tolist()},
        "y180_Q_wf": {"type": "arbitrary", "samples": y180_Q_wf.tolist()},
        "minus_y90_I_wf": {"type": "arbitrary", "samples": minus_y90_I_wf.tolist()},
        "minus_y90_Q_wf": {"type": "arbitrary", "samples": minus_y90_Q_wf.tolist()},
    },
    "digital_waveforms": {
        "ON": {"samples": [(1, 0)]},
    },
    "integration_weights": {
        "rr_cosine_weights": {
            "cosine": [(1.0, readout_len)],
            "sine": [(0.0, readout_len)],
        },
        "rr_sine_weights": {
            "cosine": [(0.0, readout_len)],
            "sine": [(1.0, readout_len)],
        },
        "rr_minus_sine_weights": {
            "cosine": [(0.0, readout_len)],
            "sine": [(-1.0, readout_len)],
        },
        "pdh_cosine_weights": {
            "cosine": [(1.0, pdh_mod_len)],
            "sine": [(0.0, pdh_mod_len)],
        },
        "pdh_sine_weights": {
            "cosine": [(0.0, pdh_mod_len)],
            "sine": [(1.0, pdh_mod_len)],
        },
        "pdh_minus_sine_weights": {
            "cosine": [(0.0, pdh_mod_len)],
            "sine": [(-1.0, pdh_mod_len)],
        },
    },
}