# %%
"""
Octave configuration working for QOP222 and qm-qua==1.1.5 and newer.
"""

from pathlib import Path
import numpy as np
from qualang_tools.config.waveform_tools import drag_gaussian_pulse_waveforms, drag_cosine_pulse_waveforms
from qualang_tools.units import unit
import plotly.io as pio

pio.renderers.default = "browser"

#######################
# AUXILIARY FUNCTIONS #
#######################
u = unit(coerce_to_integer=True)

######################
# Network parameters #
######################
qop_ip = "172.16.33.116"  # Write the QM router IP address
cluster_name = "CS_DGX"  # Write your cluster_name if version >= QOP220
qop_port = None  # Write the QOP port if version < QOP220
octave_config = None


#############
# Save Path #
#############
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
MW_FEM = 1
#############################################
#                  Qubits                   #
#############################################
# Qubits full scale power #set between -11 and 16 dBm with a 3 dB granularity
qubit_full_scale_power_dbm_q1 = -11 #Lo
qubit_full_scale_power_dbm_q2 = -11 #Lo
qubit_full_scale_power_dbm_q3 = -11 #Lo
qubit_full_scale_power_dbm_q4 = -11 #Lo
qubit_full_scale_power_dbm_q5 = -11 #Lo
qubit_full_scale_power_dbm_q6 = -11 #Lo
# Qubits bands
# The keyword "band" refers to the following frequency bands:
#   1: (50 MHz - 5.5 GHz)
#   2: (4.5 GHz - 7.5 GHz)
#   3: (6.5 GHz - 10.5 GHz)
qubit_band_q1 = 1
qubit_band_q2 = 1
qubit_band_q3 = 1
qubit_band_q4 = 1
qubit_band_q5 = 1
qubit_band_q6 = 1
# Qubits LO
qubit_LO_q1 = 5.10 * u.GHz # = 5.1e9
qubit_LO_q2 = 5.00 * u.GHz
qubit_LO_q3 = 4.50 * u.GHz
qubit_LO_q4 = 4.90 * u.GHz
qubit_LO_q5 = 4.90 * u.GHz
qubit_LO_q6 = 5.05 * u.GHz
# Qubits IF 
qubit_IF_q1 = 100* u.MHz
qubit_IF_q2 = 100 * u.MHz
qubit_IF_q3 = 100 * u.MHz
qubit_IF_q4 = 100 * u.MHz
qubit_IF_q5 = 200 * u.MHz
qubit_IF_q6 = 150 * u.MHz
# Qubits_delay
qubit_delay_q1 = 0
qubit_delay_q2 = 0
qubit_delay_q3 = 0
qubit_delay_q4 = 0
qubit_delay_q5 = 0
qubit_delay_q6 = 0

# Relaxation time
qubit1_T1 = int(30 * u.us)
qubit2_T1 = int(30 * u.us)
qubit3_T1 = int(30 * u.us)
qubit4_T1 = int(30 * u.us)
qubit5_T1 = int(30 * u.us)
qubit6_T1 = int(30 * u.us)
thermalization_time = 5 * max(qubit1_T1, qubit2_T1, qubit3_T1, qubit4_T1, qubit5_T1, qubit6_T1)

# CW pulse parameter
const_len = 1000 #ns
const_amp = 0.5

# Pi pulse parameters
pi_len = 40
pi_sigma = pi_len / 5

pi_amp_q1 = 0.1183 #max = 0.5 V_pk, V_pp = 1
pi_amp_q2 = 0.04953
pi_amp_q3 = 0.02313
pi_amp_q4 = 0.22
pi_amp_q5 = 0.22
pi_amp_q6 = 0.22

# DRAG coefficients
drag_coef_q1 = 0
drag_coef_q2 = 0
drag_coef_q3 = 0
drag_coef_q4 = 0
drag_coef_q5 = 0
drag_coef_q6 = 0

anharmonicity_q1 = -258 * u.MHz
anharmonicity_q2 = -268 * u.MHz
anharmonicity_q3 = -268 * u.MHz
anharmonicity_q4 = -200 * u.MHz
anharmonicity_q5 = -200 * u.MHz
anharmonicity_q6 = -200 * u.MHz

AC_stark_detuning_q1 = 20 * u.kHz
AC_stark_detuning_q2 = 2 * u.kHz
AC_stark_detuning_q3 = -1.49 * u.MHz
AC_stark_detuning_q4 = 0 * u.MHz
AC_stark_detuning_q5 = 0 * u.MHz
AC_stark_detuning_q6 = 0 * u.MHz


#############################################
#                Resonators                 #
#############################################
# Qubits full scale power,set between -11 and 16 dBm with a 3 dB granularity
resonator_full_scale_power_dbm = -11
# Qubits bands
# The keyword "band" refers to the following frequency bands:
#   1: (50 MHz - 5.5 GHz)
#   2: (4.5 GHz - 7.5 GHz)
#   3: (6.5 GHz - 10.5 GHz)
resonator_band = 2
# Resonators LO
resonator_LO = 5.6 * u.GHz
# Resonators IF
resonator_IF_q1 = int(-250 * u.MHz)
resonator_IF_q2 = int(-100 * u.MHz)
resonator_IF_q3 = int(70 * u.MHz)
resonator_IF_q4 = int(195.0 * u.MHz)
resonator_IF_q5 = int(320 * u.MHz)
resonator_IF_q6 = int(450* u.MHz)
# resontor_delay
resonator_delay = 0

# Readout pulse parameters
readout_len = 1000
readout_amp_q1 = 0.3 # our q1 as their q3
readout_amp_q2 = 0.03
readout_amp_q3 = 0.03
readout_amp_q4 = 0.03
readout_amp_q5 = 0.03# 0.05
readout_amp_q6 = 0.03

# TOF and depletion time
time_of_flight = 32 + 332  # must be a multiple of 4
depletion_time = 2 * u.us

# state discrimination
rotation_angle_q1 = (0.0 / 180) * np.pi
rotation_angle_q2 = (0.0 / 180) * np.pi
rotation_angle_q3 = (0.0 / 180) * np.pi
rotation_angle_q4 = (0.0 / 180) * np.pi
rotation_angle_q5 = (0.0 / 180) * np.pi
rotation_angle_q6 = (0.0 / 180) * np.pi
rotation_angle_q7 = (0.0 / 180) * np.pi

ge_threshold_q1 = 0.0
ge_threshold_q2 = 0.0
ge_threshold_q3 = 0.0
ge_threshold_q4 = 0.0
ge_threshold_q5 = 0.0
ge_threshold_q6 = 0.0
ge_threshold_q7 = 0.0
#############################################
#              Drag waveform                #
#############################################
x180_wf_q1, x180_der_wf_q1 = np.array(
    drag_gaussian_pulse_waveforms(pi_amp_q1, pi_len, pi_sigma, drag_coef_q1, anharmonicity_q1, AC_stark_detuning_q1)
)
x180_I_wf_q1 = x180_wf_q1
x180_Q_wf_q1 = x180_der_wf_q1
#----------------
x180_wf_q2, x180_der_wf_q2 = np.array(
    drag_gaussian_pulse_waveforms(pi_amp_q2, pi_len, pi_sigma, drag_coef_q2, anharmonicity_q2, AC_stark_detuning_q2)
)
x180_I_wf_q2 = x180_wf_q2
x180_Q_wf_q2 = x180_der_wf_q2
#----------------
x180_wf_q3, x180_der_wf_q3 = np.array(
    drag_gaussian_pulse_waveforms(pi_amp_q3, pi_len, pi_sigma, drag_coef_q3, anharmonicity_q3, AC_stark_detuning_q3)
)
x180_I_wf_q3 = x180_wf_q3
x180_Q_wf_q3 = x180_der_wf_q3
#----------------
x180_wf_q4, x180_der_wf_q4 = np.array(
    drag_gaussian_pulse_waveforms(pi_amp_q4, pi_len, pi_sigma, drag_coef_q4, anharmonicity_q4, AC_stark_detuning_q4)
)
x180_I_wf_q4 = x180_wf_q4
x180_Q_wf_q4 = x180_der_wf_q4
#----------------
x180_wf_q5, x180_der_wf_q5 = np.array(
    drag_gaussian_pulse_waveforms(pi_amp_q5, pi_len, pi_sigma, drag_coef_q5, anharmonicity_q5, AC_stark_detuning_q5)
)
x180_I_wf_q5 = x180_wf_q5
x180_Q_wf_q5 = x180_der_wf_q5
#----------------
x180_wf_q6, x180_der_wf_q6 = np.array(
    drag_gaussian_pulse_waveforms(pi_amp_q6, pi_len, pi_sigma, drag_coef_q6, anharmonicity_q6, AC_stark_detuning_q6)
)
x180_I_wf_q6 = x180_wf_q6
x180_Q_wf_q6 = x180_der_wf_q6
#----------------
# No DRAG when alpha=0, it's just a gaussian.

#--------------------------------------------------------------------------------------------------------
x90_wf_q1, x90_der_wf_q1 = np.array(
    drag_gaussian_pulse_waveforms(pi_amp_q1 / 2, pi_len, pi_sigma, drag_coef_q1, anharmonicity_q1, AC_stark_detuning_q1)
)
x90_I_wf_q1 = x90_wf_q1
x90_Q_wf_q1 = x90_der_wf_q1
#-----------------
x90_wf_q2, x90_der_wf_q2 = np.array(
    drag_gaussian_pulse_waveforms(pi_amp_q2 / 2, pi_len, pi_sigma, drag_coef_q2, anharmonicity_q2, AC_stark_detuning_q2)
)
x90_I_wf_q2 = x90_wf_q2
x90_Q_wf_q2 = x90_der_wf_q2
#-----------------
x90_wf_q3, x90_der_wf_q3 = np.array(
    drag_gaussian_pulse_waveforms(pi_amp_q3 / 2, pi_len, pi_sigma, drag_coef_q3, anharmonicity_q3, AC_stark_detuning_q3)
)
x90_I_wf_q3 = x90_wf_q3
x90_Q_wf_q3 = x90_der_wf_q3
#-----------------
x90_wf_q4, x90_der_wf_q4 = np.array(
    drag_gaussian_pulse_waveforms(pi_amp_q4 / 2, pi_len, pi_sigma, drag_coef_q4, anharmonicity_q4, AC_stark_detuning_q4)
)
x90_I_wf_q4 = x90_wf_q4
x90_Q_wf_q4 = x90_der_wf_q4
#-----------------
x90_wf_q5, x90_der_wf_q5 = np.array(
    drag_gaussian_pulse_waveforms(pi_amp_q5 / 2, pi_len, pi_sigma, drag_coef_q5, anharmonicity_q5, AC_stark_detuning_q5)
)
x90_I_wf_q5 = x90_wf_q5
x90_Q_wf_q5 = x90_der_wf_q5
#-----------------
x90_wf_q6, x90_der_wf_q6 = np.array(
    drag_gaussian_pulse_waveforms(pi_amp_q6 / 2, pi_len, pi_sigma, drag_coef_q6, anharmonicity_q6, AC_stark_detuning_q6)
)
x90_I_wf_q6 = x90_wf_q6
x90_Q_wf_q6 = x90_der_wf_q6
#-----------------
# No DRAG when alpha=0, it's just a gaussian.

#--------------------------------------------------------------------------------------------------------
minus_x90_wf_q1, minus_x90_der_wf_q1 = np.array(
    drag_gaussian_pulse_waveforms(
        -pi_amp_q1 / 2, pi_len, pi_sigma, drag_coef_q1, anharmonicity_q1, AC_stark_detuning_q1
    )
)
minus_x90_I_wf_q1 = minus_x90_wf_q1
minus_x90_Q_wf_q1 = minus_x90_der_wf_q1
#-----------------
minus_x90_wf_q2, minus_x90_der_wf_q2 = np.array(
    drag_gaussian_pulse_waveforms(
        -pi_amp_q2 / 2, pi_len, pi_sigma, drag_coef_q2, anharmonicity_q2, AC_stark_detuning_q2
    )
)
minus_x90_I_wf_q2 = minus_x90_wf_q2
minus_x90_Q_wf_q2 = minus_x90_der_wf_q2
#-----------------
minus_x90_wf_q3, minus_x90_der_wf_q3 = np.array(
    drag_gaussian_pulse_waveforms(
        -pi_amp_q3 / 2, pi_len, pi_sigma, drag_coef_q3, anharmonicity_q3, AC_stark_detuning_q3
    )
)
minus_x90_I_wf_q3 = minus_x90_wf_q3
minus_x90_Q_wf_q3 = minus_x90_der_wf_q3
#-----------------
minus_x90_wf_q4, minus_x90_der_wf_q4 = np.array(
    drag_gaussian_pulse_waveforms(
        -pi_amp_q4 / 2, pi_len, pi_sigma, drag_coef_q4, anharmonicity_q4, AC_stark_detuning_q4
    )
)
minus_x90_I_wf_q4 = minus_x90_wf_q4
minus_x90_Q_wf_q4 = minus_x90_der_wf_q4
#-----------------
minus_x90_wf_q5, minus_x90_der_wf_q5 = np.array(
    drag_gaussian_pulse_waveforms(
        -pi_amp_q5 / 2, pi_len, pi_sigma, drag_coef_q5, anharmonicity_q5, AC_stark_detuning_q5
    )
)
minus_x90_I_wf_q5 = minus_x90_wf_q5
minus_x90_Q_wf_q5 = minus_x90_der_wf_q5
#-----------------
minus_x90_wf_q6, minus_x90_der_wf_q6 = np.array(
    drag_gaussian_pulse_waveforms(
        -pi_amp_q6 / 2, pi_len, pi_sigma, drag_coef_q6, anharmonicity_q6, AC_stark_detuning_q6
    )
)
minus_x90_I_wf_q6 = minus_x90_wf_q6
minus_x90_Q_wf_q6 = minus_x90_der_wf_q6
#-----------------
# No DRAG when alpha=0, it's just a gaussian.

#--------------------------------------------------------------------------------------------------------
y180_wf_q1, y180_der_wf_q1 = np.array(
    drag_gaussian_pulse_waveforms(pi_amp_q1, pi_len, pi_sigma, drag_coef_q1, anharmonicity_q1, AC_stark_detuning_q1)
)
y180_I_wf_q1 = (-1) * y180_der_wf_q1
y180_Q_wf_q1 = y180_wf_q1
#-----------------
y180_wf_q2, y180_der_wf_q2 = np.array(
    drag_gaussian_pulse_waveforms(pi_amp_q2, pi_len, pi_sigma, drag_coef_q2, anharmonicity_q2, AC_stark_detuning_q2)
)
y180_I_wf_q2 = (-1) * y180_der_wf_q2
y180_Q_wf_q2 = y180_wf_q2
#-----------------
y180_wf_q3, y180_der_wf_q3 = np.array(
    drag_gaussian_pulse_waveforms(pi_amp_q3, pi_len, pi_sigma, drag_coef_q3, anharmonicity_q3, AC_stark_detuning_q3)
)
y180_I_wf_q3 = (-1) * y180_der_wf_q3
y180_Q_wf_q3 = y180_wf_q3
#-----------------
y180_wf_q4, y180_der_wf_q4 = np.array(
    drag_gaussian_pulse_waveforms(pi_amp_q4, pi_len, pi_sigma, drag_coef_q4, anharmonicity_q4, AC_stark_detuning_q4)
)
y180_I_wf_q4 = (-1) * y180_der_wf_q4
y180_Q_wf_q4 = y180_wf_q4
#-----------------
y180_wf_q5, y180_der_wf_q5 = np.array(
    drag_gaussian_pulse_waveforms(pi_amp_q5, pi_len, pi_sigma, drag_coef_q5, anharmonicity_q5, AC_stark_detuning_q5)
)
y180_I_wf_q5 = (-1) * y180_der_wf_q5
y180_Q_wf_q5 = y180_wf_q5
#-----------------
y180_wf_q6, y180_der_wf_q6 = np.array(
    drag_gaussian_pulse_waveforms(pi_amp_q6, pi_len, pi_sigma, drag_coef_q6, anharmonicity_q6, AC_stark_detuning_q6)
)
y180_I_wf_q6 = (-1) * y180_der_wf_q6
y180_Q_wf_q6 = y180_wf_q6
#-----------------
# No DRAG when alpha=0, it's just a gaussian.

#--------------------------------------------------------------------------------------------------------
y90_wf_q1, y90_der_wf_q1 = np.array(
    drag_gaussian_pulse_waveforms(pi_amp_q1 / 2, pi_len, pi_sigma, drag_coef_q1, anharmonicity_q1, AC_stark_detuning_q1)
)
y90_I_wf_q1 = (-1) * y90_der_wf_q1
y90_Q_wf_q1 = y90_wf_q1
#-----------------
y90_wf_q2, y90_der_wf_q2 = np.array(
    drag_gaussian_pulse_waveforms(pi_amp_q2 / 2, pi_len, pi_sigma, drag_coef_q2, anharmonicity_q2, AC_stark_detuning_q2)
)
y90_I_wf_q2 = (-1) * y90_der_wf_q2
y90_Q_wf_q2 = y90_wf_q2
#-----------------
y90_wf_q3, y90_der_wf_q3 = np.array(
    drag_gaussian_pulse_waveforms(pi_amp_q3 / 2, pi_len, pi_sigma, drag_coef_q3, anharmonicity_q3, AC_stark_detuning_q3)
)
y90_I_wf_q3 = (-1) * y90_der_wf_q3
y90_Q_wf_q3 = y90_wf_q3
#-----------------
y90_wf_q4, y90_der_wf_q4 = np.array(
    drag_gaussian_pulse_waveforms(pi_amp_q4 / 2, pi_len, pi_sigma, drag_coef_q4, anharmonicity_q4, AC_stark_detuning_q4)
)
y90_I_wf_q4 = (-1) * y90_der_wf_q4
y90_Q_wf_q4 = y90_wf_q4
#-----------------
y90_wf_q5, y90_der_wf_q5 = np.array(
    drag_gaussian_pulse_waveforms(pi_amp_q5 / 2, pi_len, pi_sigma, drag_coef_q5, anharmonicity_q5, AC_stark_detuning_q5)
)
y90_I_wf_q5 = (-1) * y90_der_wf_q5
y90_Q_wf_q5 = y90_wf_q5
#-----------------
y90_wf_q6, y90_der_wf_q6 = np.array(
    drag_gaussian_pulse_waveforms(pi_amp_q6 / 2, pi_len, pi_sigma, drag_coef_q6, anharmonicity_q6, AC_stark_detuning_q6)
)
y90_I_wf_q6 = (-1) * y90_der_wf_q6
y90_Q_wf_q6 = y90_wf_q6
#-----------------
# No DRAG when alpha=0, it's just a gaussian.

#--------------------------------------------------------------------------------------------------------
minus_y90_wf_q1, minus_y90_der_wf_q1 = np.array(
    drag_gaussian_pulse_waveforms(
        -pi_amp_q1 / 2, pi_len, pi_sigma, drag_coef_q1, anharmonicity_q1, AC_stark_detuning_q1
    )
)
minus_y90_I_wf_q1 = (-1) * minus_y90_der_wf_q1
minus_y90_Q_wf_q1 = minus_y90_wf_q1
#-----------------
minus_y90_wf_q2, minus_y90_der_wf_q2 = np.array(
    drag_gaussian_pulse_waveforms(
        -pi_amp_q2 / 2, pi_len, pi_sigma, drag_coef_q2, anharmonicity_q2, AC_stark_detuning_q2
    )
)
minus_y90_I_wf_q2 = (-1) * minus_y90_der_wf_q2
minus_y90_Q_wf_q2 = minus_y90_wf_q2
#-----------------
minus_y90_wf_q3, minus_y90_der_wf_q3 = np.array(
    drag_gaussian_pulse_waveforms(
        -pi_amp_q3 / 2, pi_len, pi_sigma, drag_coef_q3, anharmonicity_q3, AC_stark_detuning_q3
    )
)
minus_y90_I_wf_q3 = (-1) * minus_y90_der_wf_q3
minus_y90_Q_wf_q3 = minus_y90_wf_q3
#-----------------
minus_y90_wf_q4, minus_y90_der_wf_q4 = np.array(
    drag_gaussian_pulse_waveforms(
        -pi_amp_q4 / 2, pi_len, pi_sigma, drag_coef_q4, anharmonicity_q4, AC_stark_detuning_q4
    )
)
minus_y90_I_wf_q4 = (-1) * minus_y90_der_wf_q4
minus_y90_Q_wf_q4 = minus_y90_wf_q4
#-----------------
minus_y90_wf_q5, minus_y90_der_wf_q5 = np.array(
    drag_gaussian_pulse_waveforms(
        -pi_amp_q5 / 2, pi_len, pi_sigma, drag_coef_q5, anharmonicity_q5, AC_stark_detuning_q5
    )
)
minus_y90_I_wf_q5 = (-1) * minus_y90_der_wf_q5
minus_y90_Q_wf_q5 = minus_y90_wf_q5
#-----------------
minus_y90_wf_q6, minus_y90_der_wf_q6 = np.array(
    drag_gaussian_pulse_waveforms(
        -pi_amp_q6 / 2, pi_len, pi_sigma, drag_coef_q6, anharmonicity_q6, AC_stark_detuning_q6
    )
)
minus_y90_I_wf_q6 = (-1) * minus_y90_der_wf_q6
minus_y90_Q_wf_q6 = minus_y90_wf_q6
#-----------------

# No DRAG when alpha=0, it's just a gaussian.

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

    weights_q3 = np.load("optimal_weights_q3.npz")
    opt_weights_real_q3 = convert_integration_weights(weights_q3["weights_real"])
    opt_weights_minus_imag_q3 = convert_integration_weights(weights_q3["weights_minus_imag"])
    opt_weights_imag_q3 = convert_integration_weights(weights_q3["weights_imag"])
    opt_weights_minus_real_q3 = convert_integration_weights(weights_q3["weights_minus_real"])

    weights_q4 = np.load("optimal_weights_q4.npz")
    opt_weights_real_q4 = convert_integration_weights(weights_q4["weights_real"])
    opt_weights_minus_imag_q4 = convert_integration_weights(weights_q4["weights_minus_imag"])
    opt_weights_imag_q4 = convert_integration_weights(weights_q4["weights_imag"])
    opt_weights_minus_real_q4 = convert_integration_weights(weights_q4["weights_minus_real"])

    weights_q5 = np.load("optimal_weights_q5.npz")
    opt_weights_real_q5 = convert_integration_weights(weights_q5["weights_real"])
    opt_weights_minus_imag_q5 = convert_integration_weights(weights_q5["weights_minus_imag"])
    opt_weights_imag_q5 = convert_integration_weights(weights_q5["weights_imag"])
    opt_weights_minus_real_q5 = convert_integration_weights(weights_q5["weights_minus_real"])

    weights_q6 = np.load("optimal_weights_q6.npz")
    opt_weights_real_q6 = convert_integration_weights(weights_q6["weights_real"])
    opt_weights_minus_imag_q6 = convert_integration_weights(weights_q6["weights_minus_imag"])
    opt_weights_imag_q6 = convert_integration_weights(weights_q6["weights_imag"])
    opt_weights_minus_real_q6 = convert_integration_weights(weights_q6["weights_minus_real"])

    weights_q7 = np.load("optimal_weights_q7.npz")
    opt_weights_real_q7 = convert_integration_weights(weights_q7["weights_real"])
    opt_weights_minus_imag_q7 = convert_integration_weights(weights_q7["weights_minus_imag"])
    opt_weights_imag_q7 = convert_integration_weights(weights_q7["weights_imag"])
    opt_weights_minus_real_q7 = convert_integration_weights(weights_q7["weights_minus_real"])


else:
    opt_weights_real_q1 = [(1.0, readout_len)]
    opt_weights_minus_imag_q1 = [(0.0, readout_len)]
    opt_weights_imag_q1 = [(0.0, readout_len)]
    opt_weights_minus_real_q1 = [(-1.0, readout_len)]

    opt_weights_real_q2 = [(1.0, readout_len)]
    opt_weights_minus_imag_q2 = [(0.0, readout_len)]
    opt_weights_imag_q2 = [(0.0, readout_len)]
    opt_weights_minus_real_q2 = [(-1.0, readout_len)]

    opt_weights_real_q3 = [(1.0, readout_len)]
    opt_weights_minus_imag_q3 = [(0.0, readout_len)]
    opt_weights_imag_q3 = [(0.0, readout_len)]
    opt_weights_minus_real_q3 = [(-1.0, readout_len)]

    opt_weights_real_q4 = [(1.0, readout_len)]
    opt_weights_minus_imag_q4 = [(0.0, readout_len)]
    opt_weights_imag_q4 = [(0.0, readout_len)]
    opt_weights_minus_real_q4 = [(-1.0, readout_len)]

    opt_weights_real_q5 = [(1.0, readout_len)]
    opt_weights_minus_imag_q5 = [(0.0, readout_len)]
    opt_weights_imag_q5 = [(0.0, readout_len)]
    opt_weights_minus_real_q5 = [(-1.0, readout_len)]

    opt_weights_real_q6 = [(1.0, readout_len)]
    opt_weights_minus_imag_q6 = [(0.0, readout_len)]
    opt_weights_imag_q6 = [(0.0, readout_len)]
    opt_weights_minus_real_q6 = [(-1.0, readout_len)]

    opt_weights_real_q7 = [(1.0, readout_len)]
    opt_weights_minus_imag_q7 = [(0.0, readout_len)]
    opt_weights_imag_q7 = [(0.0, readout_len)]
    opt_weights_minus_real_q7 = [(-1.0, readout_len)]

#############################################
#                  Config                   #
#############################################
config = {
    "version": 1,
    "controllers": {
        "con1": {
            "type": "opx1000",
            "fems": {
                MW_FEM: { #FEM position
                    # The keyword "band" refers to the following frequency bands: (If+LO)
                    #   1: (50 MHz - 5.5 GHz)
                    #   2: (4.5 GHz - 7.5 GHz)
                    #   3: (6.5 GHz - 10.5 GHz)
                    # The keyword "full_scale_power_dbm" is the maximum power of
                    # normalized pulse waveforms in [-1,1]. To convert to voltage,
                    #   power_mw = 10**(full_scale_power_dbm / 10)
                    #   max_voltage_amp = np.sqrt(2 * power_mw * 50 / 1000)
                    #   amp_in_volts = waveform * max_voltage_amp
                    #   ^ equivalent to OPX+ amp
                    "type": "MW",
                    "analog_outputs": {
                        1: {
                            "sampling_rate": 1e9, #or 2e9
                            "full_scale_power_dbm": resonator_full_scale_power_dbm,
                            "band": resonator_band,
                            "delay": resonator_delay,
                            "upconverters": {
                                1: {"frequency": resonator_LO}, #can set 2 upconverters
                            },
                        },  # RL1  
                        2: {
                            "sampling_rate": 1e9,
                            "full_scale_power_dbm": qubit_full_scale_power_dbm_q1,
                            "band": qubit_band_q1,
                            "delay": qubit_delay_q1,
                            "upconverters": {
                                1: {"frequency": qubit_LO_q1},  
                            },
                        },  # q1 XY

                        3: {
                            "sampling_rate": 1e9,
                            "full_scale_power_dbm": qubit_full_scale_power_dbm_q2,
                            "band": qubit_band_q2,
                            "delay": qubit_delay_q2,
                            "upconverters": {
                                1: {"frequency": qubit_LO_q2},  
                            },
                        },  # q2 XY

                        4: {
                            "sampling_rate": 1e9,
                            "full_scale_power_dbm": qubit_full_scale_power_dbm_q3,
                            "band": qubit_band_q3,
                            "delay": qubit_delay_q3,
                            "upconverters": {
                                1: {"frequency": qubit_LO_q3}, 
                            },
                        },  # q3 XY

                        5: {
                            "sampling_rate": 1e9,
                            "full_scale_power_dbm": qubit_full_scale_power_dbm_q4,
                            "band": qubit_band_q4,
                            "delay": qubit_delay_q4,
                            "upconverters": {
                                1: {"frequency": qubit_LO_q4}, 
                            },
                        },  # q4 XY

                        6: {
                            "sampling_rate": 1e9,
                            "full_scale_power_dbm": qubit_full_scale_power_dbm_q5,
                            "band": qubit_band_q5,
                            "delay": qubit_delay_q5,
                            "upconverters": {
                                1: {"frequency": qubit_LO_q5}, 
                            },
                        },  # q5 XY

                        7: {
                            "sampling_rate": 1e9,
                            "full_scale_power_dbm": qubit_full_scale_power_dbm_q6,
                            "band": qubit_band_q6,
                            "delay": qubit_delay_q6,
                            "upconverters": {
                                1: {"frequency": qubit_LO_q6}, 
                            },
                        },  # q6 XY
                    },
                    "analog_inputs": {
                        1: {
                            "sampling_rate": 1e9,
                            "band": resonator_band,
                            "gain_db": 0, # 0 ~ 32
                            "downconverter_frequency": resonator_LO,
                        },  # RL1, gain_db resolution is 1
                        2: {
                            "sampling_rate": 1e9,
                            "band": resonator_band,
                            "gain_db": 0,
                            "downconverter_frequency": resonator_LO,
                        },  # RL1, gain_db resolution is 1, 
                    },
                },
            },
        },
    },
    "elements": {
        "rr1": {
            "MWInput": {
                "port": ("con1", MW_FEM, 1),
                "upconverter": 1,
            },
            "intermediate_frequency": resonator_IF_q1,  # in Hz [-350e6, +350e6] over, the power will decay
            "MWOutput": {
                "port": ("con1", MW_FEM, 2),
            },
            "time_of_flight": time_of_flight,
            "smearing": 0,
            "operations": {
                "cw": "const_pulse",
                "readout": "readout_pulse_q1",
            },
        },
        "rr2": {
            "MWInput": {
                "port": ("con1",MW_FEM, 1),
                "upconverter": 1,
            },
            "intermediate_frequency": resonator_IF_q2,  # in Hz [-350e6, +350e6]
            "MWOutput": {
                "port": ("con1", MW_FEM, 2),
            },
            "time_of_flight": time_of_flight,
            "smearing": 0,
            "operations": {
                "cw": "const_pulse",
                "readout": "readout_pulse_q2",
            },
        },
         "rr3": {
            "MWInput": {
                "port": ("con1",MW_FEM, 1),
                "upconverter": 1,
            },
            "intermediate_frequency": resonator_IF_q3,  # in Hz [-350e6, +350e6]
            "MWOutput": {
                "port": ("con1", MW_FEM, 2),
            },
            "time_of_flight": time_of_flight,
            "smearing": 0,
            "operations": {
                "cw": "const_pulse",
                "readout": "readout_pulse_q3",
            },
        },
         "rr4": {
            "MWInput": {
                "port": ("con1",MW_FEM, 1),
                "upconverter": 1,
            },
            "intermediate_frequency": resonator_IF_q4,  # in Hz [-350e6, +350e6]
            "MWOutput": {
                "port": ("con1", MW_FEM, 2
                ),
            },
            "time_of_flight": time_of_flight,
            "smearing": 0,
            "operations": {
                "cw": "const_pulse",
                "readout": "readout_pulse_q4",
            },
        },
         "rr5": {
            "MWInput": {
                "port": ("con1",MW_FEM, 1),
                "upconverter": 1,
            },
            "intermediate_frequency": resonator_IF_q5,  # in Hz [-350e6, +350e6]
            "MWOutput": {
                "port": ("con1", MW_FEM, 2
                ),
            },
            "time_of_flight": time_of_flight,
            "smearing": 0,
            "operations": {
                "cw": "const_pulse",
                "readout": "readout_pulse_q5",
            },
        },
         "rr6": {
            "MWInput": {
                "port": ("con1",MW_FEM, 1),
                "upconverter": 1,
            },
            "intermediate_frequency": resonator_IF_q6,  # in Hz [-350e6, +350e6]
            "MWOutput": {
                "port": ("con1", MW_FEM, 2
                ),
            },
            "time_of_flight": time_of_flight,
            "smearing": 0,
            "operations": {
                "cw": "const_pulse",
                "readout": "readout_pulse_q6",
            },
        },
        #----------------------
        "q1_xy": {
            "MWInput": {
                "port": ("con1", MW_FEM, 2),
                "upconverter": 1,
            },
            "intermediate_frequency": qubit_IF_q1,  # in Hz
            "operations": {
                "cw": "const_pulse",
                "x180": "x180_pulse_q1",
                "x90": "x90_pulse_q1",
                "-x90": "-x90_pulse_q1",
                "y90": "y90_pulse_q1",
                "y180": "y180_pulse_q1",
                "-y90": "-y90_pulse_q1",
            },
        },
        "q2_xy": {
            "MWInput": {
                "port": ("con1", MW_FEM, 3),
                "upconverter": 1,
            },
            "intermediate_frequency": qubit_IF_q2,  # in Hz
            "operations": {
                "cw": "const_pulse",
                "x180": "x180_pulse_q2",
                "x90": "x90_pulse_q2",
                "-x90": "-x90_pulse_q2",
                "y90": "y90_pulse_q2",
                "y180": "y180_pulse_q2",
                "-y90": "-y90_pulse_q2",
            },
        },
        "q3_xy": {
            "MWInput": {
                "port": ("con1", MW_FEM, 4),
                "upconverter": 1,
            },
            "intermediate_frequency": qubit_IF_q3,  # in Hz
            "operations": {
                "cw": "const_pulse",
                "x180": "x180_pulse_q3",
                "x90": "x90_pulse_q3",
                "-x90": "-x90_pulse_q3",
                "y90": "y90_pulse_q3",
                "y180": "y180_pulse_q3",
                "-y90": "-y90_pulse_q3",
            },
        },
        "q4_xy": {
            "MWInput": {
                "port": ("con1", MW_FEM, 5),
                "upconverter": 1,
            },
            "intermediate_frequency": qubit_IF_q4,  # in Hz
            "operations": {
                "cw": "const_pulse",
                "x180": "x180_pulse_q4",
                "x90": "x90_pulse_q4",
                "-x90": "-x90_pulse_q4",
                "y90": "y90_pulse_q4",
                "y180": "y180_pulse_q4",
                "-y90": "-y90_pulse_q4",
            },
        },
        "q5_xy": {
            "MWInput": {
                "port": ("con1", MW_FEM, 6),
                "upconverter": 1,
            },
            "intermediate_frequency": qubit_IF_q5,  # in Hz
            "operations": {
                "cw": "const_pulse",
                "x180": "x180_pulse_q5",
                "x90": "x90_pulse_q5",
                "-x90": "-x90_pulse_q5",
                "y90": "y90_pulse_q5",
                "y180": "y180_pulse_q5",
                "-y90": "-y90_pulse_q5",
            },
        },
        "q6_xy": {
            "MWInput": {
                "port": ("con1", MW_FEM, 7),
                "upconverter": 1,
            },
            "intermediate_frequency": qubit_IF_q6,  # in Hz
            "operations": {
                "cw": "const_pulse",
                "x180": "x180_pulse_q6",
                "x90": "x90_pulse_q6",
                "-x90": "-x90_pulse_q6",
                "y90": "y90_pulse_q6",
                "y180": "y180_pulse_q6",
                "-y90": "-y90_pulse_q6",
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
        #------------------
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
                "opt_cos": "opt_cosine_weights_q1",
                "opt_sin": "opt_sine_weights_q1",
                "opt_minus_sin": "opt_minus_sine_weights_q1",
            },
            "digital_marker": "ON",
        },
        #------------------
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
                "opt_cos": "opt_cosine_weights_q2",
                "opt_sin": "opt_sine_weights_q2",
                "opt_minus_sin": "opt_minus_sine_weights_q2",
            },
            "digital_marker": "ON",
        },
        #------------------
        "x90_pulse_q3": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "x90_I_wf_q3",
                "Q": "x90_Q_wf_q3",
            },
        },
        "x180_pulse_q3": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "x180_I_wf_q3",
                "Q": "x180_Q_wf_q3",
            },
        },
        "-x90_pulse_q3": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "minus_x90_I_wf_q3",
                "Q": "minus_x90_Q_wf_q3",
            },
        },
        "y90_pulse_q3": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "y90_I_wf_q3",
                "Q": "y90_Q_wf_q3",
            },
        },
        "y180_pulse_q3": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "y180_I_wf_q3",
                "Q": "y180_Q_wf_q3",
            },
        },
        "-y90_pulse_q3": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "minus_y90_I_wf_q3",
                "Q": "minus_y90_Q_wf_q3",
            },
        },
        "readout_pulse_q3": {
            "operation": "measurement",
            "length": readout_len,
            "waveforms": {
                "I": "readout_wf_q3",
                "Q": "zero_wf",
            },
            "integration_weights": {
                "cos": "cosine_weights",
                "sin": "sine_weights",
                "minus_sin": "minus_sine_weights",
                "rotated_cos": "rotated_cosine_weights_q3",
                "rotated_sin": "rotated_sine_weights_q3",
                "rotated_minus_sin": "rotated_minus_sine_weights_q3",
                "opt_cos": "opt_cosine_weights_q3",
                "opt_sin": "opt_sine_weights_q3",
                "opt_minus_sin": "opt_minus_sine_weights_q3",
            },
            "digital_marker": "ON",
        },
        #------------------
        "x90_pulse_q4": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "x90_I_wf_q4",
                "Q": "x90_Q_wf_q4",
            },
        },
        "x180_pulse_q4": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "x180_I_wf_q4",
                "Q": "x180_Q_wf_q4",
            },
        },
        "-x90_pulse_q4": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "minus_x90_I_wf_q4",
                "Q": "minus_x90_Q_wf_q4",
            },
        },
        "y90_pulse_q4": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "y90_I_wf_q4",
                "Q": "y90_Q_wf_q4",
            },
        },
        "y180_pulse_q4": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "y180_I_wf_q4",
                "Q": "y180_Q_wf_q4",
            },
        },
        "-y90_pulse_q4": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "minus_y90_I_wf_q4",
                "Q": "minus_y90_Q_wf_q4",
            },
        },
        "readout_pulse_q4": {
            "operation": "measurement",
            "length": readout_len,
            "waveforms": {
                "I": "readout_wf_q4",
                "Q": "zero_wf",
            },
            "integration_weights": {
                "cos": "cosine_weights",
                "sin": "sine_weights",
                "minus_sin": "minus_sine_weights",
                "rotated_cos": "rotated_cosine_weights_q4",
                "rotated_sin": "rotated_sine_weights_q4",
                "rotated_minus_sin": "rotated_minus_sine_weights_q4",
                "opt_cos": "opt_cosine_weights_q4",
                "opt_sin": "opt_sine_weights_q4",
                "opt_minus_sin": "opt_minus_sine_weights_q4",
            },
            "digital_marker": "ON",
        },
        #------------------
        "x90_pulse_q5": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "x90_I_wf_q5",
                "Q": "x90_Q_wf_q5",
            },
        },
        "x180_pulse_q5": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "x180_I_wf_q5",
                "Q": "x180_Q_wf_q5",
            },
        },
        "-x90_pulse_q5": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "minus_x90_I_wf_q5",
                "Q": "minus_x90_Q_wf_q5",
            },
        },
        "y90_pulse_q5": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "y90_I_wf_q5",
                "Q": "y90_Q_wf_q5",
            },
        },
        "y180_pulse_q5": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "y180_I_wf_q5",
                "Q": "y180_Q_wf_q5",
            },
        },
        "-y90_pulse_q5": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "minus_y90_I_wf_q5",
                "Q": "minus_y90_Q_wf_q5",
            },
        },
        "readout_pulse_q5": {
            "operation": "measurement",
            "length": readout_len,
            "waveforms": {
                "I": "readout_wf_q5",
                "Q": "zero_wf",
            },
            "integration_weights": {
                "cos": "cosine_weights",
                "sin": "sine_weights",
                "minus_sin": "minus_sine_weights",
                "rotated_cos": "rotated_cosine_weights_q5",
                "rotated_sin": "rotated_sine_weights_q5",
                "rotated_minus_sin": "rotated_minus_sine_weights_q5",
                "opt_cos": "opt_cosine_weights_q5",
                "opt_sin": "opt_sine_weights_q5",
                "opt_minus_sin": "opt_minus_sine_weights_q5",
            },
            "digital_marker": "ON",
        },
        #------------------
        "x90_pulse_q6": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "x90_I_wf_q6",
                "Q": "x90_Q_wf_q6",
            },
        },
        "x180_pulse_q6": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "x180_I_wf_q6",
                "Q": "x180_Q_wf_q6",
            },
        },
        "-x90_pulse_q6": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "minus_x90_I_wf_q6",
                "Q": "minus_x90_Q_wf_q6",
            },
        },
        "y90_pulse_q6": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "y90_I_wf_q6",
                "Q": "y90_Q_wf_q6",
            },
        },
        "y180_pulse_q6": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "y180_I_wf_q6",
                "Q": "y180_Q_wf_q6",
            },
        },
        "-y90_pulse_q6": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "minus_y90_I_wf_q6",
                "Q": "minus_y90_Q_wf_q6",
            },
        },
        "readout_pulse_q6": {
            "operation": "measurement",
            "length": readout_len,
            "waveforms": {
                "I": "readout_wf_q6",
                "Q": "zero_wf",
            },
            "integration_weights": {
                "cos": "cosine_weights",
                "sin": "sine_weights",
                "minus_sin": "minus_sine_weights",
                "rotated_cos": "rotated_cosine_weights_q6",
                "rotated_sin": "rotated_sine_weights_q6",
                "rotated_minus_sin": "rotated_minus_sine_weights_q6",
                "opt_cos": "opt_cosine_weights_q6",
                "opt_sin": "opt_sine_weights_q6",
                "opt_minus_sin": "opt_minus_sine_weights_q6",
            },
            "digital_marker": "ON",
        },
    },

    "waveforms": {
        "const_wf": {"type": "constant", "sample": const_amp},
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
        #------------------
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
        #------------------
        "x90_I_wf_q3": {"type": "arbitrary", "samples": x90_I_wf_q3.tolist()},
        "x90_Q_wf_q3": {"type": "arbitrary", "samples": x90_Q_wf_q3.tolist()},
        "x180_I_wf_q3": {"type": "arbitrary", "samples": x180_I_wf_q3.tolist()},
        "x180_Q_wf_q3": {"type": "arbitrary", "samples": x180_Q_wf_q3.tolist()},
        "minus_x90_I_wf_q3": {"type": "arbitrary", "samples": minus_x90_I_wf_q3.tolist()},
        "minus_x90_Q_wf_q3": {"type": "arbitrary", "samples": minus_x90_Q_wf_q3.tolist()},
        "y90_I_wf_q3": {"type": "arbitrary", "samples": y90_I_wf_q3.tolist()},
        "y90_Q_wf_q3": {"type": "arbitrary", "samples": y90_Q_wf_q3.tolist()},
        "y180_I_wf_q3": {"type": "arbitrary", "samples": y180_I_wf_q3.tolist()},
        "y180_Q_wf_q3": {"type": "arbitrary", "samples": y180_Q_wf_q3.tolist()},
        "minus_y90_I_wf_q3": {"type": "arbitrary", "samples": minus_y90_I_wf_q3.tolist()},
        "minus_y90_Q_wf_q3": {"type": "arbitrary", "samples": minus_y90_Q_wf_q3.tolist()},
        "readout_wf_q3": {"type": "constant", "sample": readout_amp_q3},
        #------------------
        "x90_I_wf_q4": {"type": "arbitrary", "samples": x90_I_wf_q4.tolist()},
        "x90_Q_wf_q4": {"type": "arbitrary", "samples": x90_Q_wf_q4.tolist()},
        "x180_I_wf_q4": {"type": "arbitrary", "samples": x180_I_wf_q4.tolist()},
        "x180_Q_wf_q4": {"type": "arbitrary", "samples": x180_Q_wf_q4.tolist()},
        "minus_x90_I_wf_q4": {"type": "arbitrary", "samples": minus_x90_I_wf_q4.tolist()},
        "minus_x90_Q_wf_q4": {"type": "arbitrary", "samples": minus_x90_Q_wf_q4.tolist()},
        "y90_I_wf_q4": {"type": "arbitrary", "samples": y90_I_wf_q4.tolist()},
        "y90_Q_wf_q4": {"type": "arbitrary", "samples": y90_Q_wf_q4.tolist()},
        "y180_I_wf_q4": {"type": "arbitrary", "samples": y180_I_wf_q4.tolist()},
        "y180_Q_wf_q4": {"type": "arbitrary", "samples": y180_Q_wf_q4.tolist()},
        "minus_y90_I_wf_q4": {"type": "arbitrary", "samples": minus_y90_I_wf_q4.tolist()},
        "minus_y90_Q_wf_q4": {"type": "arbitrary", "samples": minus_y90_Q_wf_q4.tolist()},
        "readout_wf_q4": {"type": "constant", "sample": readout_amp_q4},
        #------------------
        "x90_I_wf_q5": {"type": "arbitrary", "samples": x90_I_wf_q5.tolist()},
        "x90_Q_wf_q5": {"type": "arbitrary", "samples": x90_Q_wf_q5.tolist()},
        "x180_I_wf_q5": {"type": "arbitrary", "samples": x180_I_wf_q5.tolist()},
        "x180_Q_wf_q5": {"type": "arbitrary", "samples": x180_Q_wf_q5.tolist()},
        "minus_x90_I_wf_q5": {"type": "arbitrary", "samples": minus_x90_I_wf_q5.tolist()},
        "minus_x90_Q_wf_q5": {"type": "arbitrary", "samples": minus_x90_Q_wf_q5.tolist()},
        "y90_I_wf_q5": {"type": "arbitrary", "samples": y90_I_wf_q5.tolist()},
        "y90_Q_wf_q5": {"type": "arbitrary", "samples": y90_Q_wf_q5.tolist()},
        "y180_I_wf_q5": {"type": "arbitrary", "samples": y180_I_wf_q5.tolist()},
        "y180_Q_wf_q5": {"type": "arbitrary", "samples": y180_Q_wf_q5.tolist()},
        "minus_y90_I_wf_q5": {"type": "arbitrary", "samples": minus_y90_I_wf_q5.tolist()},
        "minus_y90_Q_wf_q5": {"type": "arbitrary", "samples": minus_y90_Q_wf_q5.tolist()},
        "readout_wf_q5": {"type": "constant", "sample": readout_amp_q5},
        #------------------
        "x90_I_wf_q6": {"type": "arbitrary", "samples": x90_I_wf_q6.tolist()},
        "x90_Q_wf_q6": {"type": "arbitrary", "samples": x90_Q_wf_q6.tolist()},
        "x180_I_wf_q6": {"type": "arbitrary", "samples": x180_I_wf_q6.tolist()},
        "x180_Q_wf_q6": {"type": "arbitrary", "samples": x180_Q_wf_q6.tolist()},
        "minus_x90_I_wf_q6": {"type": "arbitrary", "samples": minus_x90_I_wf_q6.tolist()},
        "minus_x90_Q_wf_q6": {"type": "arbitrary", "samples": minus_x90_Q_wf_q6.tolist()},
        "y90_I_wf_q6": {"type": "arbitrary", "samples": y90_I_wf_q6.tolist()},
        "y90_Q_wf_q6": {"type": "arbitrary", "samples": y90_Q_wf_q6.tolist()},
        "y180_I_wf_q6": {"type": "arbitrary", "samples": y180_I_wf_q6.tolist()},
        "y180_Q_wf_q6": {"type": "arbitrary", "samples": y180_Q_wf_q6.tolist()},
        "minus_y90_I_wf_q6": {"type": "arbitrary", "samples": minus_y90_I_wf_q6.tolist()},
        "minus_y90_Q_wf_q6": {"type": "arbitrary", "samples": minus_y90_Q_wf_q6.tolist()},
        "readout_wf_q6": {"type": "constant", "sample": readout_amp_q6},
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
        #------------------
        "rotated_cosine_weights_q1": {
            "cosine": [(np.cos(rotation_angle_q1), readout_len)],
            "sine": [(np.sin(rotation_angle_q1), readout_len)],
        },
        "rotated_sine_weights_q1": {
            "cosine": [(-np.sin(rotation_angle_q1), readout_len)],
            "sine": [(np.cos(rotation_angle_q1), readout_len)],
        },
        "rotated_minus_sine_weights_q1": {
            "cosine": [(np.sin(rotation_angle_q1), readout_len)],
            "sine": [(-np.cos(rotation_angle_q1), readout_len)],
        },
        #------------------
        "rotated_cosine_weights_q2": {
            "cosine": [(np.cos(rotation_angle_q2), readout_len)],
            "sine": [(np.sin(rotation_angle_q2), readout_len)],
        },
        "rotated_sine_weights_q2": {
            "cosine": [(-np.sin(rotation_angle_q2), readout_len)],
            "sine": [(np.cos(rotation_angle_q2), readout_len)],
        },
        "rotated_minus_sine_weights_q2": {
            "cosine": [(np.sin(rotation_angle_q2), readout_len)],
            "sine": [(-np.cos(rotation_angle_q2), readout_len)],
        },
        #------------------
        "rotated_cosine_weights_q3": {
            "cosine": [(np.cos(rotation_angle_q3), readout_len)],
            "sine": [(np.sin(rotation_angle_q3), readout_len)],
        },
        "rotated_sine_weights_q3": {
            "cosine": [(-np.sin(rotation_angle_q3), readout_len)],
            "sine": [(np.cos(rotation_angle_q3), readout_len)],
        },
        "rotated_minus_sine_weights_q3": {
            "cosine": [(np.sin(rotation_angle_q3), readout_len)],
            "sine": [(-np.cos(rotation_angle_q3), readout_len)],
        },
        #------------------
        "rotated_cosine_weights_q4": {
            "cosine": [(np.cos(rotation_angle_q4), readout_len)],
            "sine": [(np.sin(rotation_angle_q4), readout_len)],
        },
        "rotated_sine_weights_q4": {
            "cosine": [(-np.sin(rotation_angle_q4), readout_len)],
            "sine": [(np.cos(rotation_angle_q4), readout_len)],
        },
        "rotated_minus_sine_weights_q4": {
            "cosine": [(np.sin(rotation_angle_q4), readout_len)],
            "sine": [(-np.cos(rotation_angle_q4), readout_len)],
        },
        #------------------
        "rotated_cosine_weights_q5": {
            "cosine": [(np.cos(rotation_angle_q5), readout_len)],
            "sine": [(np.sin(rotation_angle_q5), readout_len)],
        },
        "rotated_sine_weights_q5": {
            "cosine": [(-np.sin(rotation_angle_q5), readout_len)],
            "sine": [(np.cos(rotation_angle_q5), readout_len)],
        },
        "rotated_minus_sine_weights_q5": {
            "cosine": [(np.sin(rotation_angle_q5), readout_len)],
            "sine": [(-np.cos(rotation_angle_q5), readout_len)],
        },
        #------------------
        "rotated_cosine_weights_q6": {
            "cosine": [(np.cos(rotation_angle_q6), readout_len)],
            "sine": [(np.sin(rotation_angle_q6), readout_len)],
        },
        "rotated_sine_weights_q6": {
            "cosine": [(-np.sin(rotation_angle_q6), readout_len)],
            "sine": [(np.cos(rotation_angle_q6), readout_len)],
        },
        "rotated_minus_sine_weights_q6": {
            "cosine": [(np.sin(rotation_angle_q6), readout_len)],
            "sine": [(-np.cos(rotation_angle_q6), readout_len)],
        },
        #------------------
        "opt_cosine_weights_q1": {
            "cosine": opt_weights_real_q1,
            "sine": opt_weights_minus_imag_q1,
        },
        "opt_sine_weights_q1": {
            "cosine": opt_weights_imag_q1,
            "sine": opt_weights_real_q1,
        },
        "opt_minus_sine_weights_q1": {
            "cosine": opt_weights_minus_imag_q1,
            "sine": opt_weights_minus_real_q1,
        },
        #------------------
        "opt_cosine_weights_q2": {
            "cosine": opt_weights_real_q2,
            "sine": opt_weights_minus_imag_q2,
        },
        "opt_sine_weights_q2": {
            "cosine": opt_weights_imag_q2,
            "sine": opt_weights_real_q2,
        },
        "opt_minus_sine_weights_q2": {
            "cosine": opt_weights_minus_imag_q2,
            "sine": opt_weights_minus_real_q2,
        },
        #------------------
        "opt_cosine_weights_q3": {
            "cosine": opt_weights_real_q3,
            "sine": opt_weights_minus_imag_q3,
        },
        "opt_sine_weights_q3": {
            "cosine": opt_weights_imag_q3,
            "sine": opt_weights_real_q3,
        },
        "opt_minus_sine_weights_q3": {
            "cosine": opt_weights_minus_imag_q3,
            "sine": opt_weights_minus_real_q3,
        },
        #------------------
        "opt_cosine_weights_q4": {
            "cosine": opt_weights_real_q4,
            "sine": opt_weights_minus_imag_q4,
        },
        "opt_sine_weights_q4": {
            "cosine": opt_weights_imag_q4,
            "sine": opt_weights_real_q4,
        },
        "opt_minus_sine_weights_q4": {
            "cosine": opt_weights_minus_imag_q4,
            "sine": opt_weights_minus_real_q4,
        },
        #------------------
        "opt_cosine_weights_q5": {
            "cosine": opt_weights_real_q5,
            "sine": opt_weights_minus_imag_q5,
        },
        "opt_sine_weights_q5": {
            "cosine": opt_weights_imag_q5,
            "sine": opt_weights_real_q5,
        },
        "opt_minus_sine_weights_q5": {
            "cosine": opt_weights_minus_imag_q5,
            "sine": opt_weights_minus_real_q5,
        },
        #------------------
        "opt_cosine_weights_q6": {
            "cosine": opt_weights_real_q6,
            "sine": opt_weights_minus_imag_q6,
        },
        "opt_sine_weights_q6": {
            "cosine": opt_weights_imag_q6,
            "sine": opt_weights_real_q6,
        },
        "opt_minus_sine_weights_q6": {
            "cosine": opt_weights_minus_imag_q6,
            "sine": opt_weights_minus_real_q6,
        },
    },
}

# %%
