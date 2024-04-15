import os
import numpy as np
from pathlib import Path
from qualang_tools.config.waveform_tools import drag_gaussian_pulse_waveforms
from qualang_tools.units import unit
from qualang_tools.config.waveform_tools import flattop_gaussian_waveform
from set_octave import OctaveUnit, octave_declaration


#############
# VARIABLES #
#############

qop_ip = "127.0.0.1"  # Write the QM router IP address
cluster_name = None  # Write your cluster_name if version >= QOP220
qop_port = None  # Write the QOP port if version < QOP220

qop_ip = "172.16.33.101"
cluster_name = "Cluster_83"
qop_port = None  # Write the QOP port if version < QOP220


############################
# Set octave configuration #
############################

# The Octave port is 11xxx, where xxx are the last three digits of the Octave internal IP that can be accessed from
# the OPX admin panel if you QOP version is >= QOP220. Otherwise, it is 50 for Octave1, then 51, 52 and so on.
# However, when you are accessing to Octave internally, provide the Octave's IP and the port is 80.s
octave_ip = "192.168.88.246"
octave_port = 80  # Must be 11xxx, where xxx are the last three digits of the Octave IP address
con = "con1"
octave = "octave1"
# octave1 = OctaveUnit("octave1", octave_ip, port=octave_ip, con="con1")
# Create the octave config object
octave_config = QmOctaveConfig()
# Specify where to store the outcome of the calibration (correction matrix, offsets...)
octave_config.set_calibration_db(os.getcwd())
# Add an Octave called 'octave1' with the specified IP and port
octave_config.add_device_info(octave, octave_ip, octave_port)
# # Add the octaves
# octaves = [octave1]
# # Configure the Octaves
# octave_config = octave_declaration(octaves)


#############
# Save Path #
#############

# Path to base directories for script and data
base_dir = Path(__file__).resolve().parent
save_dir = base_dir / "Data"


#########
# Units #
#########
u = unit(coerce_to_integer=True)


#############################################
#                  Qubits                   #
#############################################
qubit_LO_q1 = 5.25 * u.GHz  # Used only for mixer correction and frequency rescaling for plots or computation
qubit_LO_q2 = 5.25 * u.GHz  # Used only for mixer correction and frequency rescaling for plots or computation

# Qubits IF
qubit_IF_q1 = -50 * u.MHz
qubit_IF_q1_ef = -150 * u.MHz
qubit_IF_q2 = -75 * u.MHz
qubit_IF_q2_ef = -250 * u.MHz

# Relaxation time
qubit_T1_q1 = 3 * u.us
qubit_T1_q2 = 3 * u.us
thermalization_time = 5 * max(qubit_T1_q1, qubit_T1_q2)

# CW pulse paramter
const_len = 1000
const_amp = 0.125 # V
# Saturation pulse
saturation_len = 10 * u.us 
saturation_amp = 0.125 # V
# Pi pulse
pi_len = 40 # ns
assert pi_len % 5 == 0
pi_sigma = pi_len / 5
pi_amp_q1 = 0.125
pi_amp_q2 = 0.125

# DRAG coefficients
drag_coef_q1 = 0
drag_coef_q2 = 0
anharmonicity_q1 = -200 * u.MHz
anharmonicity_q2 = -180 * u.MHz
AC_stark_detuning_q1 = -200 * u.MHz
AC_stark_detuning_q2 = -180 * u.MHz
drag_params_q1 = pi_len, pi_sigma, drag_coef_q1, anharmonicity_q1, AC_stark_detuning_q1
drag_params_q2 = pi_len, pi_sigma, drag_coef_q2, anharmonicity_q2, AC_stark_detuning_q2

# DRAG waveforms
# x180. No DRAG when alpha=0, it's just a gaussian.
# q1
x180_wf_q1, x180_der_wf_q1 = np.array(drag_gaussian_pulse_waveforms(pi_amp_q1, *drag_params_q1))
x180_I_wf_q1 = x180_wf_q1
x180_Q_wf_q1 = x180_der_wf_q1
# q2
x180_wf_q2, x180_der_wf_q2 = np.array(drag_gaussian_pulse_waveforms(pi_amp_q2, *drag_params_q2))
x180_I_wf_q2 = x180_wf_q2
x180_Q_wf_q2 = x180_der_wf_q2

# x90. No DRAG when alpha=0, it's just a gaussian.
# q1
x90_wf_q1, x90_der_wf_q1 = np.array(drag_gaussian_pulse_waveforms(pi_amp_q1 / 2, *drag_params_q1))
x90_I_wf_q1 = x90_wf_q1
x90_Q_wf_q1 = x90_der_wf_q1
# q2
x90_wf_q2, x90_der_wf_q2 = np.array(drag_gaussian_pulse_waveforms(pi_amp_q2 / 2, *drag_params_q2))
x90_I_wf_q2 = x90_wf_q2
x90_Q_wf_q2 = x90_der_wf_q2

# minus_x90. No DRAG when alpha=0, it's just a gaussian.
# q1
minus_x90_wf_q1, minus_x90_der_wf_q1 = np.array(drag_gaussian_pulse_waveforms(-pi_amp_q1 / 2, *drag_params_q1))
minus_x90_I_wf_q1 = minus_x90_wf_q1
minus_x90_Q_wf_q1 = minus_x90_der_wf_q1
# q2
minus_x90_wf_q2, minus_x90_der_wf_q2 = np.array(drag_gaussian_pulse_waveforms(-pi_amp_q2 / 2, *drag_params_q2))
minus_x90_I_wf_q2 = minus_x90_wf_q2
minus_x90_Q_wf_q2 = minus_x90_der_wf_q2

# y180. No DRAG when alpha=0, it's just a gaussian.
# q1
y180_wf_q1, y180_der_wf_q1 = np.array(drag_gaussian_pulse_waveforms(pi_amp_q1, *drag_params_q1))
y180_I_wf_q1 = (-1) * y180_der_wf_q1
y180_Q_wf_q1 = y180_wf_q1
# q2
y180_wf_q2, y180_der_wf_q2 = np.array(drag_gaussian_pulse_waveforms(pi_amp_q2, *drag_params_q2))
y180_I_wf_q2 = (-1) * y180_der_wf_q2
y180_Q_wf_q2 = y180_wf_q2

# y90. No DRAG when alpha=0, it's just a gaussian.
# q1
y90_wf_q1, y90_der_wf_q1 = np.array(drag_gaussian_pulse_waveforms(pi_amp_q1 / 2, *drag_params_q1))
y90_I_wf_q1 = (-1) * y90_der_wf_q1
y90_Q_wf_q1 = y90_wf_q1
# q2
y90_wf_q2, y90_der_wf_q2 = np.array(drag_gaussian_pulse_waveforms(pi_amp_q2 / 2, *drag_params_q2))
y90_I_wf_q2 = (-1) * y90_der_wf_q2
y90_Q_wf_q2 = y90_wf_q2

# minus_y90. No DRAG when alpha=0, it's just a gaussian.
# q1
minus_y90_wf_q1, minus_y90_der_wf_q1 = np.array(drag_gaussian_pulse_waveforms(-pi_amp_q1 / 2, *drag_params_q1))
minus_y90_I_wf_q1 = (-1) * minus_y90_der_wf_q1
minus_y90_Q_wf_q1 = minus_y90_wf_q1
# q2
minus_y90_wf_q2, minus_y90_der_wf_q2 = np.array(drag_gaussian_pulse_waveforms(-pi_amp_q2 / 2, *drag_params_q2))
minus_y90_I_wf_q2 = (-1) * minus_y90_der_wf_q2
minus_y90_Q_wf_q2 = minus_y90_wf_q2


#############################################
#                Resonators                 #
#############################################
resonator_LO = 7.25 * u.GHz # Used only for mixer correction and frequency rescaling for plots or computation
# Resonators IF
resonator_IF_q1 = int(75 * u.MHz)
resonator_IF_q2 = int(133 * u.MHz)
# Mixer parameters
mixer_resonator_g_q1 = 0.0
mixer_resonator_g_q2 = 0.0
mixer_resonator_phi_q1 = -0.00
mixer_resonator_phi_q2 = -0.00

# Readout pulse parameters
readout_len = 1000
readout_amp_q1 = 0.01
readout_amp_q2 = 0.01

# TOF and depletion time
time_of_flight = 24  # must be a multiple of 4
depletion_time = 2 * u.us

# Integration weights
opt_weights = False
if opt_weights:
    from qualang_tools.config.integration_weights_tools import convert_integration_weights

    weights_q1 = np.load("optimal_weights_q1.npz")
    opt_weights_real_q1 = convert_integration_weights(weights_q1["weights_real"])
    opt_weights_minus_imag_q1 = convert_integration_weights(weights_q1["weights_minus_imag"])
    opt_weights_imag_q1 = convert_integration_weights(weights_q1["weights_imag"])
    opt_weights_minus_real_q1 = convert_integration_weights(weights_q1["weights_minus_real"])
    weights_q2 = np.load("optimal_weights_q2.npz")
    opt_weights_real_q2 = convert_integration_weights(weights_q2["weights_real"])
    opt_weights_minus_imag_q2 = convert_integration_weights(weights_q2["weights_minus_imag"])
    opt_weights_imag_q2 = convert_integration_weights(weights_q2["weights_imag"])
    opt_weights_minus_real_q2 = convert_integration_weights(weights_q2["weights_minus_real"])
else:
    opt_weights_real_q1 = [(1.0, readout_len)]
    opt_weights_minus_imag_q1 = [(1.0, readout_len)]
    opt_weights_imag_q1 = [(1.0, readout_len)]
    opt_weights_minus_real_q1 = [(1.0, readout_len)]
    opt_weights_real_q2 = [(1.0, readout_len)]
    opt_weights_minus_imag_q2 = [(1.0, readout_len)]
    opt_weights_imag_q2 = [(1.0, readout_len)]
    opt_weights_minus_real_q2 = [(1.0, readout_len)]

# state discrimination
rotation_angle_q1 = (0.0 / 180) * np.pi
rotation_angle_q2 = (0.0 / 180) * np.pi
ge_threshold_q1 = 0.0
ge_threshold_q2 = 0.0


#############################################
#                Cross-resonance            #
#############################################
cr_IF_c1t2 = (qubit_IF_q2 + qubit_LO_q2) - (qubit_IF_q1 + qubit_LO_q1)
cr_IF_c2t1 = (-1) * cr_IF_c1t2
# Pulse durations
c1t2_square_positive_len = 100
c1t2_square_negative_len = c1t2_square_positive_len
c2t1_square_positive_len = 100
c2t1_square_negative_len = c2t1_square_positive_len
# Pulse amplitudes
c1t2_square_positive_amp = 0.1
c1t2_square_negative_amp = (-1) * c1t2_square_positive_amp
c2t1_square_positive_amp = 0.1
c2t1_square_negative_amp = (-1) * c2t1_square_positive_amp


#############################################
#         Flat-top generation               #
#############################################
# flattop wf generation
rise_fall_len = 16
assert rise_fall_len == int(rise_fall_len)
flat_top_len = 200
assert flat_top_len == int(flat_top_len)
flat_top_amp = 0.1
zero_pad = []
if rise_fall_len < 16:
    zero_pad = [0] * (16 - rise_fall_len)
elif rise_fall_len % 4 != 0:
    zero_pad = [0] * (4 - rise_fall_len % 4)

# flat
flat = np.array([flat_top_amp] * round(flat_top_len)).tolist()
# rise
rise_flattop = flattop_gaussian_waveform(flat_top_amp, flat_top_len, rise_fall_len, return_part="rise")
rise = np.array(zero_pad + rise_flattop).tolist()
# fall
fall_flattop = flattop_gaussian_waveform(flat_top_amp, flat_top_len, rise_fall_len, return_part="fall")
fall = np.array(fall_flattop + zero_pad).tolist()


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
        "rr1": {
            "RF_inputs": {"port": ("octave1", 1)},
            "RF_outputs": {"port": ("octave1", 1)},
            "intermediate_frequency": resonator_IF_q1,
            "operations": {
                "cw": "const_pulse",
                "readout": "readout_pulse_q1",
            },
            "time_of_flight": time_of_flight,
            "smearing": 0,
        },
        "rr2": {
            "RF_inputs": {"port": ("octave1", 1)},
            "RF_outputs": {"port": ("octave1", 1)},
            "intermediate_frequency": resonator_IF_q2,
            "operations": {
                "cw": "const_pulse",
                "readout": "readout_pulse_q2",
            },
            "time_of_flight": time_of_flight,
            "smearing": 0,
        },
        "q1_xy": {
            "RF_inputs": {"port": ("octave1", 2)},
            "intermediate_frequency": qubit_IF_q1,
            "operations": {
                "cw": "const_pulse",
                "saturation": "saturation_pulse",
                "x180": "x180_pulse_q1",
                "x90": "x90_pulse_q1",
                "-x90": "-x90_pulse_q1",
                "y90": "y90_pulse_q1",
                "y180": "y180_pulse_q1",
                "-y90": "-y90_pulse_q1",
            },
        },
        "q1_xy_ef": {
            "RF_inputs": {"port": ("octave1", 2)},
            "intermediate_frequency": qubit_IF_q1_ef,
            "operations": {
                "cw": "const_pulse",
                "saturation": "saturation_pulse",
            },
        },
        "q2_xy": {
            "RF_inputs": {"port": ("octave1", 3)},
            "intermediate_frequency": qubit_IF_q2,
            "operations": {
                "cw": "const_pulse",
                "saturation": "saturation_pulse",
                "x180": "x180_pulse_q2",
                "x90": "x90_pulse_q2",
                "-x90": "-x90_pulse_q2",
                "y90": "y90_pulse_q2",
                "y180": "y180_pulse_q2",
                "-y90": "-y90_pulse_q2",
            },
        },
        "q2_xy_ef": {
            "RF_inputs": {"port": ("octave1", 3)},
            "intermediate_frequency": qubit_IF_q2_ef,
            "operations": {
                "cw": "const_pulse",
                "saturation": "saturation_pulse",
            },
        },
        "cr_c1t2": {
            "RF_inputs": {"port": ("octave1", 2)},
            "intermediate_frequency": qubit_IF_q2,
            "operations": {
                "square_positive": "cr_c1t2_square_positive_pulse",
                "square_negative": "cr_c1t2_square_negative_pulse",
                "flat_top": "cr_c1t2_flat_top_pulse",
            },
        },
        "cr_c1t2_twin": {
            "RF_inputs": {"port": ("octave1", 2)},
            "intermediate_frequency": qubit_IF_q2,
            "operations": {
                "gaussian_rise": "cr_c1t2_gaussian_rise_pulse",
                "gaussian_fall": "cr_c1t2_gaussian_fall_pulse",
            },
        },
        "cr_c2t1": {
            "RF_inputs": {"port": ("octave1", 3)},
            "intermediate_frequency": qubit_IF_q2,
            "operations": {
                "square_positive": "cr_c2t1_square_positive_pulse",
                "square_negative": "cr_c2t1_square_negative_pulse",
                "flat_top": "cr_c2t1_flat_top_pulse",
            },
        },
        "cr_c2t1_twin": {
            "RF_inputs": {"port": ("octave1", 3)},
            "intermediate_frequency": qubit_IF_q2,
            "operations": {
                "gaussian_rise": "cr_c2t1_gaussian_rise_pulse",
                "gaussian_fall": "cr_c2t1_gaussian_fall_pulse",
            },
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
                    "LO_frequency": qubit_LO_q1,
                    "LO_source": "internal",
                    "output_mode": "always_on",
                    "gain": 0,
                },
                3: {
                    "LO_frequency": qubit_LO_q2,
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
        "cr_c1t2_square_positive_pulse": {
            "operation": "control",
            "length": c1t2_square_positive_len,
            "waveforms": {
                "I": "c1t2_square_positive_wf",
                "Q": "zero_wf",
            },
        },
        "cr_c1t2_square_negative_pulse": {
            "operation": "control",
            "length": c1t2_square_positive_len,
            "waveforms": {
                "I": "c1t2_square_negative_wf",
                "Q": "zero_wf",
            },
        },
        "cr_c2t1_square_positive_pulse": {
            "operation": "control",
            "length": c2t1_square_positive_len,
            "waveforms": {
                "I": "c2t1_square_positive_wf",
                "Q": "zero_wf",
            },
        },
        "cr_c2t1_square_negative_pulse": {
            "operation": "control",
            "length": c2t1_square_positive_len,
            "waveforms": {
                "I": "c2t1_square_negative_wf",
                "Q": "zero_wf",
            },
        },
        "cr_c1t2_gaussian_rise_pulse": {
            "operation": "control",
            "length": rise_fall_len,
            "waveforms": {
                "I": "cr_c1t2_gaussian_rise_wf",
                "Q": "zero_wf",
            },
        },
        "cr_c1t2_gaussian_fall_pulse": {
            "operation": "control",
            "length": rise_fall_len,
            "waveforms": {
                "I": "cr_c1t2_gaussian_fall_wf",
                "Q": "zero_wf",
            },
        },
        "cr_c1t2_flat_top_pulse": {
            "operation": "control",
            "length": flat_top_length,
            "waveforms": {
                "I": "cr_c1t2_flat_top_wf",
                "Q": "zero_wf",
            },
        },
        "cr_c2t1_gaussian_rise_pulse": {
            "operation": "control",
            "length": rise_fall_len,
            "waveforms": {
                "I": "cr_c2t1_gaussian_rise_wf",
                "Q": "zero_wf",
            },
        },
        "cr_c2t1_gaussian_fall_pulse": {
            "operation": "control",
            "length": rise_fall_len,
            "waveforms": {
                "I": "cr_c2t1_gaussian_fall_wf",
                "Q": "zero_wf",
            },
        },
        "cr_c2t1_flat_top_pulse": {
            "operation": "control",
            "length": flat_top_length,
            "waveforms": {
                "I": "cr_c2t1_flat_top_wf",
                "Q": "zero_wf",
            },
        },
        "x90_pulse_q1": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "x90_I_wf_q1",
                "Q": "x90_Q_wf_q1",
            },
        },
        "x180_pulse_q1": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "x180_I_wf_q1",
                "Q": "x180_Q_wf_q1",
            },
        },
        "-x90_pulse_q1": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "minus_x90_I_wf_q1",
                "Q": "minus_x90_Q_wf_q1",
            },
        },
        "y90_pulse_q1": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "y90_I_wf_q1",
                "Q": "y90_Q_wf_q1",
            },
        },
        "y180_pulse_q1": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "y180_I_wf_q1",
                "Q": "y180_Q_wf_q1",
            },
        },
        "-y90_pulse_q1": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "minus_y90_I_wf_q1",
                "Q": "minus_y90_Q_wf_q1",
            },
        },
        "readout_pulse_q1": {
            "operation": "measurement",
            "length": readout_len,
            "waveforms": {
                "I": "readout_wf_q1",
                "Q": "zero_wf",
            },
            "integration_weights": {
                "cos": "cosine_weights",
                "sin": "sine_weights",
                "minus_sin": "minus_sine_weights",
                "rotated_cos": "rotated_cosine_weights_q1",
                "rotated_sin": "rotated_sine_weights_q1",
                "rotated_minus_sin": "rotated_minus_sine_weights_q1",
            },
            "digital_marker": "ON",
        },
        "x90_pulse_q2": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "x90_I_wf_q2",
                "Q": "x90_Q_wf_q2",
            },
        },
        "x180_pulse_q2": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "x180_I_wf_q2",
                "Q": "x180_Q_wf_q2",
            },
        },
        "-x90_pulse_q2": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "minus_x90_I_wf_q2",
                "Q": "minus_x90_Q_wf_q2",
            },
        },
        "y90_pulse_q2": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "y90_I_wf_q2",
                "Q": "y90_Q_wf_q2",
            },
        },
        "y180_pulse_q2": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "y180_I_wf_q2",
                "Q": "y180_Q_wf_q2",
            },
        },
        "-y90_pulse_q2": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "minus_y90_I_wf_q2",
                "Q": "minus_y90_Q_wf_q2",
            },
        },
        "readout_pulse_q2": {
            "operation": "measurement",
            "length": readout_len,
            "waveforms": {
                "I": "readout_wf_q2",
                "Q": "zero_wf",
            },
            "integration_weights": {
                "cos": "cosine_weights",
                "sin": "sine_weights",
                "minus_sin": "minus_sine_weights",
                "rotated_cos": "rotated_cosine_weights_q2",
                "rotated_sin": "rotated_sine_weights_q2",
                "rotated_minus_sin": "rotated_minus_sine_weights_q2",
            },
            "digital_marker": "ON",
        },
    },
    "waveforms": {
        "const_wf": {"type": "constant", "sample": const_amp},
        "saturation_wf": {"type": "constant", "sample": saturation_amp},
        "c1t2_square_positive_wf": {"type": "constant", "sample": c1t2_square_positive_amp},
        "c1t2_square_negative_wf": {"type": "constant", "sample": c1t2_square_negative_amp},
        "c2t1_square_positive_wf": {"type": "constant", "sample": c2t1_square_positive_amp},
        "c2t1_square_negative_wf": {"type": "constant", "sample": c2t1_square_negative_amp},
        "cr_c1t2_gaussian_rise_wf": {"type": "arbitrary", "samples": rise},
        "cr_c1t2_gaussian_fall_wf": {"type": "arbitrary", "samples": fall},
        "cr_c1t2_flat_top_wf": {"type": "arbitrary", "samples": flat},
        "cr_c2t1_gaussian_rise_wf": {"type": "arbitrary", "samples": rise},
        "cr_c2t1_gaussian_fall_wf": {"type": "arbitrary", "samples": fall},
        "cr_c2t1_flat_top_wf": {"type": "arbitrary", "samples": flat},
        "zero_wf": {"type": "constant", "sample": 0.0},
        "x90_I_wf_q1": {"type": "arbitrary", "samples": x90_I_wf_q1.tolist()},
        "x90_Q_wf_q1": {"type": "arbitrary", "samples": x90_Q_wf_q1.tolist()},
        "x180_I_wf_q1": {"type": "arbitrary", "samples": x180_I_wf_q1.tolist()},
        "x180_Q_wf_q1": {"type": "arbitrary", "samples": x180_Q_wf_q1.tolist()},
        "minus_x90_I_wf_q1": {"type": "arbitrary", "samples": minus_x90_I_wf_q1.tolist()},
        "minus_x90_Q_wf_q1": {"type": "arbitrary", "samples": minus_x90_Q_wf_q1.tolist()},
        "y90_I_wf_q1": {"type": "arbitrary", "samples": y90_I_wf_q1.tolist()},
        "y90_Q_wf_q1": {"type": "arbitrary", "samples": y90_Q_wf_q1.tolist()},
        "y180_I_wf_q1": {"type": "arbitrary", "samples": y180_I_wf_q1.tolist()},
        "y180_Q_wf_q1": {"type": "arbitrary", "samples": y180_Q_wf_q1.tolist()},
        "minus_y90_I_wf_q1": {"type": "arbitrary", "samples": minus_y90_I_wf_q1.tolist()},
        "minus_y90_Q_wf_q1": {"type": "arbitrary", "samples": minus_y90_Q_wf_q1.tolist()},
        "readout_wf_q1": {"type": "constant", "sample": readout_amp_q1},
        "x90_I_wf_q2": {"type": "arbitrary", "samples": x90_I_wf_q2.tolist()},
        "x90_Q_wf_q2": {"type": "arbitrary", "samples": x90_Q_wf_q2.tolist()},
        "x180_I_wf_q2": {"type": "arbitrary", "samples": x180_I_wf_q2.tolist()},
        "x180_Q_wf_q2": {"type": "arbitrary", "samples": x180_Q_wf_q2.tolist()},
        "minus_x90_I_wf_q2": {"type": "arbitrary", "samples": minus_x90_I_wf_q2.tolist()},
        "minus_x90_Q_wf_q2": {"type": "arbitrary", "samples": minus_x90_Q_wf_q2.tolist()},
        "y90_I_wf_q2": {"type": "arbitrary", "samples": y90_I_wf_q2.tolist()},
        "y90_Q_wf_q2": {"type": "arbitrary", "samples": y90_Q_wf_q2.tolist()},
        "y180_I_wf_q2": {"type": "arbitrary", "samples": y180_I_wf_q2.tolist()},
        "y180_Q_wf_q2": {"type": "arbitrary", "samples": y180_Q_wf_q2.tolist()},
        "minus_y90_I_wf_q2": {"type": "arbitrary", "samples": minus_y90_I_wf_q2.tolist()},
        "minus_y90_Q_wf_q2": {"type": "arbitrary", "samples": minus_y90_Q_wf_q2.tolist()},
        "readout_wf_q2": {"type": "constant", "sample": readout_amp_q2},
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
        "rotated_cosine_weights_q1": {
            "cosine": [(np.cos(rotation_angle_q1), readout_len)],
            "sine": [(-np.sin(rotation_angle_q1), readout_len)],
        },
        "rotated_sine_weights_q1": {
            "cosine": [(np.sin(rotation_angle_q1), readout_len)],
            "sine": [(np.cos(rotation_angle_q1), readout_len)],
        },
        "rotated_minus_sine_weights_q1": {
            "cosine": [(-np.sin(rotation_angle_q1), readout_len)],
            "sine": [(-np.cos(rotation_angle_q1), readout_len)],
        },
        "rotated_cosine_weights_q2": {
            "cosine": [(np.cos(rotation_angle_q2), readout_len)],
            "sine": [(-np.sin(rotation_angle_q2), readout_len)],
        },
        "rotated_sine_weights_q2": {
            "cosine": [(np.sin(rotation_angle_q2), readout_len)],
            "sine": [(np.cos(rotation_angle_q2), readout_len)],
        },
        "rotated_minus_sine_weights_q2": {
            "cosine": [(-np.sin(rotation_angle_q2), readout_len)],
            "sine": [(-np.cos(rotation_angle_q2), readout_len)],
        },
    },
}
