# %%
"""
QUA-Config supporting OPX1000 w/ MW-FEM
"""

from pathlib import Path
import numpy as np
from qualang_tools.config.waveform_tools import drag_gaussian_pulse_waveforms
from qualang_tools.units import unit
from set_octave import OctaveUnit, octave_declaration


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
qop_ip = "172.16.33.107"
cluster_name = "Cluster_1" 
qop_port = None  # Write the QOP port if version < QOP220

con = "con1"
lffem1 = 3
lffem2 = 5

# The Octave port is 11xxx, where xxx are the last three digits of the Octave internal IP that can be accessed from
# the OPX admin panel if you QOP version is >= QOP220. Otherwise, it is 50 for Octave1, then 51, 52 and so on.
# octave_1 = OctaveUnit("octave1", qop_ip, port=11109, con=con)
# octave_2 = OctaveUnit("octave2", qop_ip, port=11051, con=con)

# If the control PC or local network is connected to the internal network of the QM router (port 2 onwards)
# or directly to the Octave (without QM the router), use the local octave IP and port 80.
octave_ip = "172.16.33.109"
octave_1 = OctaveUnit("octave1", octave_ip, port=80, con=con)

# Add the octaves
octaves = [octave_1]
# Configure the Octaves
octave_config = octave_declaration(octaves)


# Path to save data
save_dir = Path().absolute() / "data"
save_dir.mkdir(exist_ok=True)
default_additional_files = {
    "configuration_with_lffem_octave.py": "configuration_with_lffem_octave.py",
    "optimal_weights.npz": "optimal_weights.npz",
}


#############################################
#                  Qubits                   #
#############################################
# Qubits LO
qubit_LO_q1 = 8.00 * u.GHz
qubit_LO_q2 = 7.50 * u.GHz
# Qubits IF
qubit_IF_q1 = -100 * u.MHz
qubit_IF_q2 = -200 * u.MHz
# Qubits_delay
qubit_delay_q1 = 0
qubit_delay_q2 = 0

# Mixer parameters
mixer_qubit_g_q1 = 0.00
mixer_qubit_g_q2 = 0.00
mixer_qubit_phi_q1 = 0.0
mixer_qubit_phi_q2 = 0.0

# Relaxation time
qubit1_T1 = int(30 * u.us)
qubit2_T1 = int(30 * u.us)
thermalization_time = 5 * max(qubit1_T1, qubit2_T1)

# CW pulse parameter
const_len = 1000
const_amp = 0.25

# Pi pulse parameters
pi_len = 40
pi_sigma = pi_len / 5
pi_amp_q1 = 0.22
pi_amp_q2 = 0.22

# DRAG coefficients
drag_coef_q1 = 1.0
drag_coef_q2 = 1.0
anharmonicity_q1 = -200 * u.MHz
anharmonicity_q2 = -180 * u.MHz
AC_stark_detuning_q1 = 0 * u.MHz
AC_stark_detuning_q2 = 0 * u.MHz

# DRAG waveforms
x180_wf_q1, x180_der_wf_q1 = np.array(
    drag_gaussian_pulse_waveforms(pi_amp_q1, pi_len, pi_sigma, drag_coef_q1, anharmonicity_q1, AC_stark_detuning_q1)
)
x180_I_wf_q1 = x180_wf_q1
x180_Q_wf_q1 = x180_der_wf_q1
x180_wf_q2, x180_der_wf_q2 = np.array(
    drag_gaussian_pulse_waveforms(pi_amp_q2, pi_len, pi_sigma, drag_coef_q2, anharmonicity_q2, AC_stark_detuning_q2)
)
x180_I_wf_q2 = x180_wf_q2
x180_Q_wf_q2 = x180_der_wf_q2
# No DRAG when alpha=0, it's just a gaussian.

x90_wf_q1, x90_der_wf_q1 = np.array(
    drag_gaussian_pulse_waveforms(pi_amp_q1 / 2, pi_len, pi_sigma, drag_coef_q1, anharmonicity_q1, AC_stark_detuning_q1)
)
x90_I_wf_q1 = x90_wf_q1
x90_Q_wf_q1 = x90_der_wf_q1
x90_wf_q2, x90_der_wf_q2 = np.array(
    drag_gaussian_pulse_waveforms(pi_amp_q2 / 2, pi_len, pi_sigma, drag_coef_q2, anharmonicity_q2, AC_stark_detuning_q2)
)
x90_I_wf_q2 = x90_wf_q2
x90_Q_wf_q2 = x90_der_wf_q2
# No DRAG when alpha=0, it's just a gaussian.

minus_x90_wf_q1, minus_x90_der_wf_q1 = np.array(
    drag_gaussian_pulse_waveforms(
        -pi_amp_q1 / 2, pi_len, pi_sigma, drag_coef_q1, anharmonicity_q1, AC_stark_detuning_q1
    )
)
minus_x90_I_wf_q1 = minus_x90_wf_q1
minus_x90_Q_wf_q1 = minus_x90_der_wf_q1
minus_x90_wf_q2, minus_x90_der_wf_q2 = np.array(
    drag_gaussian_pulse_waveforms(
        -pi_amp_q2 / 2, pi_len, pi_sigma, drag_coef_q2, anharmonicity_q2, AC_stark_detuning_q2
    )
)
minus_x90_I_wf_q2 = minus_x90_wf_q2
minus_x90_Q_wf_q2 = minus_x90_der_wf_q2
# No DRAG when alpha=0, it's just a gaussian.

y180_wf_q1, y180_der_wf_q1 = np.array(
    drag_gaussian_pulse_waveforms(pi_amp_q1, pi_len, pi_sigma, drag_coef_q1, anharmonicity_q1, AC_stark_detuning_q1)
)
y180_I_wf_q1 = (-1) * y180_der_wf_q1
y180_Q_wf_q1 = y180_wf_q1
y180_wf_q2, y180_der_wf_q2 = np.array(
    drag_gaussian_pulse_waveforms(pi_amp_q2, pi_len, pi_sigma, drag_coef_q2, anharmonicity_q2, AC_stark_detuning_q2)
)
y180_I_wf_q2 = (-1) * y180_der_wf_q2
y180_Q_wf_q2 = y180_wf_q2
# No DRAG when alpha=0, it's just a gaussian.

y90_wf_q1, y90_der_wf_q1 = np.array(
    drag_gaussian_pulse_waveforms(pi_amp_q1 / 2, pi_len, pi_sigma, drag_coef_q1, anharmonicity_q1, AC_stark_detuning_q1)
)
y90_I_wf_q1 = (-1) * y90_der_wf_q1
y90_Q_wf_q1 = y90_wf_q1
y90_wf_q2, y90_der_wf_q2 = np.array(
    drag_gaussian_pulse_waveforms(pi_amp_q2 / 2, pi_len, pi_sigma, drag_coef_q2, anharmonicity_q2, AC_stark_detuning_q2)
)
y90_I_wf_q2 = (-1) * y90_der_wf_q2
y90_Q_wf_q2 = y90_wf_q2
# No DRAG when alpha=0, it's just a gaussian.

minus_y90_wf_q1, minus_y90_der_wf_q1 = np.array(
    drag_gaussian_pulse_waveforms(
        -pi_amp_q1 / 2, pi_len, pi_sigma, drag_coef_q1, anharmonicity_q1, AC_stark_detuning_q1
    )
)
minus_y90_I_wf_q1 = (-1) * minus_y90_der_wf_q1
minus_y90_Q_wf_q1 = minus_y90_wf_q1
minus_y90_wf_q2, minus_y90_der_wf_q2 = np.array(
    drag_gaussian_pulse_waveforms(
        -pi_amp_q2 / 2, pi_len, pi_sigma, drag_coef_q2, anharmonicity_q2, AC_stark_detuning_q2
    )
)
minus_y90_I_wf_q2 = (-1) * minus_y90_der_wf_q2
minus_y90_Q_wf_q2 = minus_y90_wf_q2
# No DRAG when alpha=0, it's just a gaussian.



#############################################
#                Resonators                 #
#############################################
# Qubits full scale power
resonator_full_scale_power_dbm = -20
# Qubits bands
# The keyword "band" refers to the following frequency bands:
#   1: (50 MHz - 5.5 GHz)
#   2: (4.5 GHz - 7.5 GHz)
#   3: (6.5 GHz - 10.5 GHz)
resonator_band = 3
# Resonators LO
resonator_LO = 10.0 * u.GHz
# Resonators IF
resonator_IF_q1 = int(100 * u.MHz)
resonator_IF_q2 = int(200 * u.MHz)
# resontor_delay
resonator_delay = 0

# Readout pulse parameters
readout_len = 1000
readout_amp_q1 = 0.1
readout_amp_q2 = 0.1

# TOF and depletion time
time_of_flight = 24  # must be a multiple of 4
depletion_time = 2 * u.us

# Mixer parameters
mixer_resonator_g_q1 = 0.0
mixer_resonator_g_q2 = 0.0
mixer_resonator_phi_q1 = -0.00
mixer_resonator_phi_q2 = -0.00

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
    opt_weights_minus_imag_q1 = [(0.0, readout_len)]
    opt_weights_imag_q1 = [(0.0, readout_len)]
    opt_weights_minus_real_q1 = [(-1.0, readout_len)]
    opt_weights_real_q2 = [(1.0, readout_len)]
    opt_weights_minus_imag_q2 = [(0.0, readout_len)]
    opt_weights_imag_q2 = [(0.0, readout_len)]
    opt_weights_minus_real_q2 = [(-1.0, readout_len)]

# state discrimination
rotation_angle_q1 = (0.0 / 180) * np.pi
rotation_angle_q2 = (0.0 / 180) * np.pi
ge_threshold_q1 = 0.0
ge_threshold_q2 = 0.0

#############################################
#                  Config                   #
#############################################
sampling_rate = 1e9
config = {
    "version": 1,
    "controllers": {
        con: {
            "type": "opx1000",
            "fems": {
                lffem2: {
                    "type": "LF",
                    "analog_outputs": {},
                    "digital_outputs": {
                        1: {
                            "level": "TTL",
                        },
                    },
                    "analog_inputs": {},
                },
            },
        }
    },
    "elements": {
        "dm": {
            "digitalInputs": {
                "trigger": {
                    "port": (con, lffem2, 1),
                    "delay": 0,
                    "buffer": 0,
                }
            },
            "operations": {
                "trigger": "trigger_pulse",
            },
        },
    },
    "pulses": {
        "trigger_pulse": {
            "operation": "control",
            "length": 1000,
            "digital_marker": "ON",
        },
    },
    "digital_waveforms": {
        "ON": {"samples": [(1, 0)]},
    },
}

# %%
