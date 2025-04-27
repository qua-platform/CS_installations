# %%
"""
Octave configuration working for QOP222 and qm-qua==1.1.5 and newer.
"""

from pathlib import Path
import numpy as np
from qualang_tools.config.waveform_tools import drag_gaussian_pulse_waveforms
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
qop_ip = "127.0.0.1"  # Write the QM router IP address
cluster_name = None  # Write your cluster_name if version >= QOP220
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

#############################################
#                  Qubits                   #
#############################################
# Qubits full scale power
qubit_full_scale_power_dbm_q1 = -8
qubit_full_scale_power_dbm_q2 = -8
qubit_full_scale_power_dbm_q3 = -8
qubit_full_scale_power_dbm_q4 = -8
qubit_full_scale_power_dbm_q5 = -8
qubit_full_scale_power_dbm_q6 = -8
qubit_full_scale_power_dbm_q7 = -8
qubit_full_scale_power_dbm_q8 = -8
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
qubit_band_q7 = 1
qubit_band_q8 = 1
# Qubits LO
qubit_LO_q1 = 4.00 * u.GHz
qubit_LO_q2 = 4.00 * u.GHz
qubit_LO_q3 = 4.00 * u.GHz
qubit_LO_q4 = 4.00 * u.GHz
qubit_LO_q5 = 4.00 * u.GHz
qubit_LO_q6 = 4.00 * u.GHz
qubit_LO_q7 = 4.00 * u.GHz
qubit_LO_q8 = 4.00 * u.GHz
# Qubits IF
qubit_IF_q1 = 300 * u.MHz
qubit_IF_q2 = 200 * u.MHz
qubit_IF_q3 = 100 * u.MHz
qubit_IF_q4 = -100 * u.MHz
qubit_IF_q5 = -200 * u.MHz
qubit_IF_q6 = -300 * u.MHz
qubit_IF_q7 = -400 * u.MHz
qubit_IF_q8 = -400 * u.MHz
# Qubits_delay
qubit_delay_q1 = 0
qubit_delay_q2 = 0
qubit_delay_q3 = 0
qubit_delay_q4 = 0
qubit_delay_q5 = 0
qubit_delay_q6 = 0
qubit_delay_q7 = 0
qubit_delay_q8 = 0

# Relaxation time
qubit1_T1 = int(30 * u.us)
qubit2_T1 = int(30 * u.us)
qubit3_T1 = int(30 * u.us)
qubit4_T1 = int(30 * u.us)
qubit5_T1 = int(30 * u.us)
qubit6_T1 = int(30 * u.us)
qubit7_T1 = int(30 * u.us)
qubit8_T1 = int(30 * u.us)
thermalization_time = 5 * max(qubit1_T1, qubit2_T1, qubit3_T1, qubit4_T1, qubit5_T1, qubit6_T1, qubit7_T1, qubit8_T1)

# CW pulse parameter
const_len = 1000
const_amp = 0.25

# Pi pulse parameters
pi_len = 40
pi_sigma = pi_len / 5
pi_amp_q1 = 0.22
pi_amp_q2 = 0.22
pi_amp_q3 = 0.22
pi_amp_q4 = 0.22
pi_amp_q5 = 0.22
pi_amp_q6 = 0.22
pi_amp_q7 = 0.22
pi_amp_q8 = 0.22

# DRAG coefficients
drag_coef_q1 = 1.0
drag_coef_q2 = 1.0
drag_coef_q3 = 1.0
drag_coef_q4 = 1.0
drag_coef_q5 = 1.0
drag_coef_q6 = 1.0
drag_coef_q7 = 1.0
drag_coef_q8 = 1.0
anharmonicity_q1 = -200 * u.MHz
anharmonicity_q2 = -180 * u.MHz
anharmonicity_q3 = -200 * u.MHz
anharmonicity_q4 = -180 * u.MHz
anharmonicity_q5 = -200 * u.MHz
anharmonicity_q6 = -180 * u.MHz
anharmonicity_q7 = -200 * u.MHz
anharmonicity_q8 = -200 * u.MHz
AC_stark_detuning_q1 = 0 * u.MHz
AC_stark_detuning_q2 = 0 * u.MHz
AC_stark_detuning_q3 = 0 * u.MHz
AC_stark_detuning_q4 = 0 * u.MHz
AC_stark_detuning_q5 = 0 * u.MHz
AC_stark_detuning_q6 = 0 * u.MHz
AC_stark_detuning_q7 = 0 * u.MHz
AC_stark_detuning_q8 = 0 * u.MHz

# DRAG waveforms
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
x180_wf_q7, x180_der_wf_q7 = np.array(
    drag_gaussian_pulse_waveforms(pi_amp_q7, pi_len, pi_sigma, drag_coef_q7, anharmonicity_q7, AC_stark_detuning_q7)
)
x180_I_wf_q7 = x180_wf_q7
x180_Q_wf_q7 = x180_der_wf_q7
#----------------
x180_wf_q8, x180_der_wf_q8 = np.array(
    drag_gaussian_pulse_waveforms(pi_amp_q8, pi_len, pi_sigma, drag_coef_q8, anharmonicity_q8, AC_stark_detuning_q8)
)
x180_I_wf_q8 = x180_wf_q8
x180_Q_wf_q8 = x180_der_wf_q8
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
x90_wf_q7, x90_der_wf_q7 = np.array(
    drag_gaussian_pulse_waveforms(pi_amp_q7 / 2, pi_len, pi_sigma, drag_coef_q7, anharmonicity_q7, AC_stark_detuning_q7)
)
x90_I_wf_q7 = x90_wf_q7
x90_Q_wf_q7 = x90_der_wf_q7
#-----------------
x90_wf_q8, x90_der_wf_q8 = np.array(
    drag_gaussian_pulse_waveforms(pi_amp_q8 / 2, pi_len, pi_sigma, drag_coef_q8, anharmonicity_q8, AC_stark_detuning_q8)
)
x90_I_wf_q8 = x90_wf_q8
x90_Q_wf_q8 = x90_der_wf_q8
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
minus_x90_wf_q7, minus_x90_der_wf_q7 = np.array(
    drag_gaussian_pulse_waveforms(
        -pi_amp_q7 / 2, pi_len, pi_sigma, drag_coef_q7, anharmonicity_q7, AC_stark_detuning_q7
    )
)
minus_x90_I_wf_q7 = minus_x90_wf_q7
minus_x90_Q_wf_q7 = minus_x90_der_wf_q7
#-----------------
minus_x90_wf_q8, minus_x90_der_wf_q8 = np.array(
    drag_gaussian_pulse_waveforms(
        -pi_amp_q8 / 2, pi_len, pi_sigma, drag_coef_q8, anharmonicity_q8, AC_stark_detuning_q8
    )
)
minus_x90_I_wf_q8 = minus_x90_wf_q8
minus_x90_Q_wf_q8 = minus_x90_der_wf_q8
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
y180_wf_q7, y180_der_wf_q7 = np.array(
    drag_gaussian_pulse_waveforms(pi_amp_q7, pi_len, pi_sigma, drag_coef_q7, anharmonicity_q7, AC_stark_detuning_q7)
)
y180_I_wf_q7 = (-1) * y180_der_wf_q7
y180_Q_wf_q7 = y180_wf_q7
#-----------------
y180_wf_q8, y180_der_wf_q8 = np.array(
    drag_gaussian_pulse_waveforms(pi_amp_q8, pi_len, pi_sigma, drag_coef_q8, anharmonicity_q8, AC_stark_detuning_q8)
)
y180_I_wf_q8 = (-1) * y180_der_wf_q8
y180_Q_wf_q8 = y180_wf_q8
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
y90_wf_q7, y90_der_wf_q7 = np.array(
    drag_gaussian_pulse_waveforms(pi_amp_q7 / 2, pi_len, pi_sigma, drag_coef_q7, anharmonicity_q7, AC_stark_detuning_q7)
)
y90_I_wf_q7 = (-1) * y90_der_wf_q7
y90_Q_wf_q7 = y90_wf_q7
#-----------------
y90_wf_q8, y90_der_wf_q8 = np.array(
    drag_gaussian_pulse_waveforms(pi_amp_q8 / 2, pi_len, pi_sigma, drag_coef_q8, anharmonicity_q8, AC_stark_detuning_q8)
)
y90_I_wf_q8 = (-1) * y90_der_wf_q8
y90_Q_wf_q8 = y90_wf_q8
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
minus_y90_wf_q7, minus_y90_der_wf_q7 = np.array(
    drag_gaussian_pulse_waveforms(
        -pi_amp_q7 / 2, pi_len, pi_sigma, drag_coef_q7, anharmonicity_q7, AC_stark_detuning_q7
    )
)
minus_y90_I_wf_q7 = (-1) * minus_y90_der_wf_q7
minus_y90_Q_wf_q7 = minus_y90_wf_q7
#-----------------
minus_y90_wf_q8, minus_y90_der_wf_q8 = np.array(
    drag_gaussian_pulse_waveforms(
        -pi_amp_q8 / 2, pi_len, pi_sigma, drag_coef_q8, anharmonicity_q8, AC_stark_detuning_q8
    )
)
minus_y90_I_wf_q8 = (-1) * minus_y90_der_wf_q8
minus_y90_Q_wf_q8 = minus_y90_wf_q8

# No DRAG when alpha=0, it's just a gaussian.


#############################################
#              Cross Resonance              #
#############################################

# CR Drive full scale power
cr_drive_full_scale_power_dbm_c1t2 = -2
cr_drive_full_scale_power_dbm_c2t1 = -2
cr_drive_full_scale_power_dbm_c2t3 = -2
cr_drive_full_scale_power_dbm_c3t2 = -2
cr_drive_full_scale_power_dbm_c3t4 = -2
cr_drive_full_scale_power_dbm_c4t3 = -2
cr_drive_full_scale_power_dbm_c4t5 = -2
cr_drive_full_scale_power_dbm_c5t4 = -2
cr_drive_full_scale_power_dbm_c5t6 = -2
cr_drive_full_scale_power_dbm_c6t5 = -2
cr_drive_full_scale_power_dbm_c6t7 = -2
cr_drive_full_scale_power_dbm_c7t6 = -2
cr_drive_full_scale_power_dbm_c7t8 = -2
cr_drive_full_scale_power_dbm_c8t1 = -2
# CR Cancel full scale power
cr_cancel_full_scale_power_dbm_c1t2 = -8
cr_cancel_full_scale_power_dbm_c2t1 = -8
cr_cancel_full_scale_power_dbm_c2t3 = -8
cr_cancel_full_scale_power_dbm_c3t2 = -8
cr_cancel_full_scale_power_dbm_c3t4 = -8
cr_cancel_full_scale_power_dbm_c4t3 = -8
cr_cancel_full_scale_power_dbm_c4t5 = -8
cr_cancel_full_scale_power_dbm_c5t4 = -8
cr_cancel_full_scale_power_dbm_c5t6 = -8
cr_cancel_full_scale_power_dbm_c6t5 = -8
cr_cancel_full_scale_power_dbm_c6t7 = -8
cr_cancel_full_scale_power_dbm_c7t6 = -8
cr_cancel_full_scale_power_dbm_c7t8 = -8
cr_cancel_full_scale_power_dbm_c8t1 = -8

# CR Drive bands
cr_drive_band_c1t2 = qubit_band_q2
cr_drive_band_c2t1 = qubit_band_q1
cr_drive_band_c2t3 = qubit_band_q3
cr_drive_band_c3t2 = qubit_band_q2
cr_drive_band_c3t4 = qubit_band_q4
cr_drive_band_c4t3 = qubit_band_q3
cr_drive_band_c4t5 = qubit_band_q5
cr_drive_band_c5t4 = qubit_band_q4
cr_drive_band_c5t6 = qubit_band_q6
cr_drive_band_c6t5 = qubit_band_q5
cr_drive_band_c6t7 = qubit_band_q7
cr_drive_band_c7t6 = qubit_band_q6
cr_drive_band_c7t8 = qubit_band_q8
cr_drive_band_c8t1 = qubit_band_q1

# CR Cancel bands
cr_cancel_band_c1t2 = qubit_band_q2
cr_cancel_band_c2t1 = qubit_band_q1
cr_cancel_band_c2t3 = qubit_band_q3
cr_cancel_band_c3t2 = qubit_band_q2
cr_cancel_band_c3t4 = qubit_band_q4
cr_cancel_band_c4t3 = qubit_band_q3
cr_cancel_band_c4t5 = qubit_band_q5
cr_cancel_band_c5t4 = qubit_band_q4
cr_cancel_band_c5t6 = qubit_band_q6
cr_cancel_band_c6t5 = qubit_band_q5
cr_cancel_band_c6t7 = qubit_band_q7
cr_cancel_band_c7t6 = qubit_band_q6
cr_cancel_band_c7t8 = qubit_band_q8
cr_cancel_band_c8t1 = qubit_band_q1

# CR Drive LO
cr_drive_LO_c1t2 = qubit_LO_q2
cr_drive_LO_c2t1 = qubit_LO_q1
cr_drive_LO_c2t3 = qubit_LO_q3
cr_drive_LO_c3t2 = qubit_LO_q2
cr_drive_LO_c3t4 = qubit_LO_q4
cr_drive_LO_c4t3 = qubit_LO_q3
cr_drive_LO_c4t5 = qubit_LO_q5
cr_drive_LO_c5t4 = qubit_LO_q4
cr_drive_LO_c5t6 = qubit_LO_q6
cr_drive_LO_c6t5 = qubit_LO_q5
cr_drive_LO_c6t7 = qubit_LO_q7
cr_drive_LO_c7t6 = qubit_LO_q6
cr_drive_LO_c7t8 = qubit_LO_q8
cr_drive_LO_c8t1 = qubit_LO_q1

# CR Cancel LO
cr_cancel_LO_c1t2 = qubit_LO_q2
cr_cancel_LO_c2t1 = qubit_LO_q1
cr_cancel_LO_c2t3 = qubit_LO_q3
cr_cancel_LO_c3t2 = qubit_LO_q2
cr_cancel_LO_c3t4 = qubit_LO_q4
cr_cancel_LO_c4t3 = qubit_LO_q3
cr_cancel_LO_c4t5 = qubit_LO_q5
cr_cancel_LO_c5t4 = qubit_LO_q4
cr_cancel_LO_c5t6 = qubit_LO_q6
cr_cancel_LO_c6t5 = qubit_LO_q5
cr_cancel_LO_c6t7 = qubit_LO_q7
cr_cancel_LO_c7t6 = qubit_LO_q6
cr_cancel_LO_c7t8 = qubit_LO_q8
cr_cancel_LO_c8t1 = qubit_LO_q1

# CR Drive IF
cr_drive_IF_c1t2 = qubit_IF_q2
cr_drive_IF_c2t1 = qubit_IF_q1
cr_drive_IF_c2t3 = qubit_IF_q3
cr_drive_IF_c3t2 = qubit_IF_q2
cr_drive_IF_c3t4 = qubit_IF_q4
cr_drive_IF_c4t3 = qubit_IF_q3
cr_drive_IF_c4t5 = qubit_IF_q5
cr_drive_IF_c5t4 = qubit_IF_q4
cr_drive_IF_c5t6 = qubit_IF_q6
cr_drive_IF_c6t5 = qubit_IF_q5
cr_drive_IF_c6t7 = qubit_IF_q7
cr_drive_IF_c7t6 = qubit_IF_q6
cr_drive_IF_c7t8 = qubit_IF_q8
cr_drive_IF_c8t1 = qubit_IF_q1

# CR Cancel IF
cr_cancel_IF_c1t2 = qubit_IF_q2
cr_cancel_IF_c2t1 = qubit_IF_q1
cr_cancel_IF_c2t3 = qubit_IF_q3
cr_cancel_IF_c3t2 = qubit_IF_q2
cr_cancel_IF_c3t4 = qubit_IF_q4
cr_cancel_IF_c4t3 = qubit_IF_q3
cr_cancel_IF_c4t5 = qubit_IF_q5
cr_cancel_IF_c5t4 = qubit_IF_q4
cr_cancel_IF_c5t6 = qubit_IF_q6
cr_cancel_IF_c6t5 = qubit_IF_q5
cr_cancel_IF_c6t7 = qubit_IF_q7
cr_cancel_IF_c7t6 = qubit_IF_q6
cr_cancel_IF_c7t8 = qubit_IF_q8
cr_cancel_IF_c8t1 = qubit_IF_q1

# CR Drive pulse len
cr_drive_square_len_c1t2 = 120
cr_drive_square_len_c2t1 = 120
cr_drive_square_len_c2t3 = 120
cr_drive_square_len_c3t2 = 120
cr_drive_square_len_c3t4 = 120
cr_drive_square_len_c4t3 = 120
cr_drive_square_len_c4t5 = 120
cr_drive_square_len_c5t4 = 120
cr_drive_square_len_c5t6 = 120
cr_drive_square_len_c6t5 = 120
cr_drive_square_len_c6t7 = 120
cr_drive_square_len_c7t6 = 120
cr_drive_square_len_c7t8 = 120
cr_drive_square_len_c8t1 = 120

# CR Cancel pulse len
cr_cancel_square_len_c1t2 = cr_drive_square_len_c1t2
cr_cancel_square_len_c2t1 = cr_drive_square_len_c2t1
cr_cancel_square_len_c2t3 = cr_drive_square_len_c2t3
cr_cancel_square_len_c3t2 = cr_drive_square_len_c3t2
cr_cancel_square_len_c3t4 = cr_drive_square_len_c3t4
cr_cancel_square_len_c4t3 = cr_drive_square_len_c4t3
cr_cancel_square_len_c4t5 = cr_drive_square_len_c4t5
cr_cancel_square_len_c5t4 = cr_drive_square_len_c5t4
cr_cancel_square_len_c5t6 = cr_drive_square_len_c5t6
cr_cancel_square_len_c6t5 = cr_drive_square_len_c6t5
cr_cancel_square_len_c6t7 = cr_drive_square_len_c6t7
cr_cancel_square_len_c7t6 = cr_drive_square_len_c7t6
cr_cancel_square_len_c7t8 = cr_drive_square_len_c7t8
cr_cancel_square_len_c8t1 = cr_drive_square_len_c8t1

# CR Drive pulse amp
cr_drive_square_amp_c1t2 = 0.5
cr_drive_square_amp_c2t1 = 0.5
cr_drive_square_amp_c2t3 = 0.5
cr_drive_square_amp_c3t2 = 0.5
cr_drive_square_amp_c3t4 = 0.5
cr_drive_square_amp_c4t3 = 0.5
cr_drive_square_amp_c4t5 = 0.5
cr_drive_square_amp_c5t4 = 0.5
cr_drive_square_amp_c5t6 = 0.5
cr_drive_square_amp_c6t5 = 0.5
cr_drive_square_amp_c6t7 = 0.5
cr_drive_square_amp_c7t6 = 0.5
cr_drive_square_amp_c7t8 = 0.5
cr_drive_square_amp_c8t1 = 0.5

# CR Cancel pulse amp
cr_cancel_square_amp_c1t2 = 0.5
cr_cancel_square_amp_c2t1 = 0.5
cr_cancel_square_amp_c2t3 = 0.5
cr_cancel_square_amp_c3t2 = 0.5
cr_cancel_square_amp_c3t4 = 0.5
cr_cancel_square_amp_c4t3 = 0.5
cr_cancel_square_amp_c4t5 = 0.5
cr_cancel_square_amp_c5t4 = 0.5
cr_cancel_square_amp_c5t6 = 0.5
cr_cancel_square_amp_c6t5 = 0.5
cr_cancel_square_amp_c6t7 = 0.5
cr_cancel_square_amp_c7t6 = 0.5
cr_cancel_square_amp_c7t8 = 0.5
cr_cancel_square_amp_c8t1 = 0.5

# CR Drive pulse phase
cr_drive_square_phase_c1t2 = 0.0  # in units of 2pi
cr_drive_square_phase_c2t1 = 0.0  # in units of 2pi  
cr_drive_square_phase_c1t2 = 0.0  # in units of 2pi
cr_drive_square_phase_c2t1 = 0.0  # in units of 2pi
cr_drive_square_phase_c2t3 = 0.0  # in units of 2pi
cr_drive_square_phase_c3t2 = 0.0  # in units of 2pi
cr_drive_square_phase_c3t4 = 0.0  # in units of 2pi
cr_drive_square_phase_c4t3 = 0.0  # in units of 2pi
cr_drive_square_phase_c4t5 = 0.0  # in units of 2pi
cr_drive_square_phase_c5t4 = 0.0  # in units of 2pi
cr_drive_square_phase_c5t6 = 0.0  # in units of 2pi
cr_drive_square_phase_c6t5 = 0.0  # in units of 2pi
cr_drive_square_phase_c6t7 = 0.0  # in units of 2pi
cr_drive_square_phase_c7t6 = 0.0  # in units of 2pi
cr_drive_square_phase_c7t8 = 0.0  # in units of 2pi
cr_drive_square_phase_c8t1 = 0.0  # in units of 2pi

# CR Cancel pulse phase
cr_cancel_square_phase_c1t2 = 0.0  # in units of 2pi
cr_cancel_square_phase_c2t1 = 0.0  # in units of 2pi  
cr_cancel_square_phase_c1t2 = 0.0  # in units of 2pi
cr_cancel_square_phase_c2t1 = 0.0  # in units of 2pi
cr_cancel_square_phase_c2t3 = 0.0  # in units of 2pi
cr_cancel_square_phase_c3t2 = 0.0  # in units of 2pi
cr_cancel_square_phase_c3t4 = 0.0  # in units of 2pi
cr_cancel_square_phase_c4t3 = 0.0  # in units of 2pi
cr_cancel_square_phase_c4t5 = 0.0  # in units of 2pi
cr_cancel_square_phase_c5t4 = 0.0  # in units of 2pi
cr_cancel_square_phase_c5t6 = 0.0  # in units of 2pi
cr_cancel_square_phase_c6t5 = 0.0  # in units of 2pi
cr_cancel_square_phase_c6t7 = 0.0  # in units of 2pi
cr_cancel_square_phase_c7t6 = 0.0  # in units of 2pi
cr_cancel_square_phase_c7t8 = 0.0  # in units of 2pi
cr_cancel_square_phase_c8t1 = 0.0  # in units of 2pi

# CR Drive pulse phase
cr_drive_square_phase_ZI_correct_c1t2 = 0.0  # in units of 2pi
cr_drive_square_phase_ZI_correct_c2t1 = 0.0  # in units of 2pi  
cr_drive_square_phase_ZI_correct_c1t2 = 0.0  # in units of 2pi
cr_drive_square_phase_ZI_correct_c2t1 = 0.0  # in units of 2pi
cr_drive_square_phase_ZI_correct_c2t3 = 0.0  # in units of 2pi
cr_drive_square_phase_ZI_correct_c3t2 = 0.0  # in units of 2pi
cr_drive_square_phase_ZI_correct_c3t4 = 0.0  # in units of 2pi
cr_drive_square_phase_ZI_correct_c4t3 = 0.0  # in units of 2pi
cr_drive_square_phase_ZI_correct_c4t5 = 0.0  # in units of 2pi
cr_drive_square_phase_ZI_correct_c5t4 = 0.0  # in units of 2pi
cr_drive_square_phase_ZI_correct_c5t6 = 0.0  # in units of 2pi
cr_drive_square_phase_ZI_correct_c6t5 = 0.0  # in units of 2pi
cr_drive_square_phase_ZI_correct_c6t7 = 0.0  # in units of 2pi
cr_drive_square_phase_ZI_correct_c7t6 = 0.0  # in units of 2pi
cr_drive_square_phase_ZI_correct_c7t8 = 0.0  # in units of 2pi
cr_drive_square_phase_ZI_correct_c8t1 = 0.0  # in units of 2pi


#############################################
#                Resonators                 #
#############################################
# Qubits full scale power
resonator_full_scale_power_dbm = -11
# Qubits bands
# The keyword "band" refers to the following frequency bands:
#   1: (50 MHz - 5.5 GHz)
#   2: (4.5 GHz - 7.5 GHz)
#   3: (6.5 GHz - 10.5 GHz)
resonator_band = 2
# Resonators LO
resonator_LO1 = 6.3 * u.GHz
resonator_LO2 = 7.2 * u.GHz
# Resonators IF
resonator_IF_q1 = int(100 * u.MHz)
resonator_IF_q2 = int(200 * u.MHz)
resonator_IF_q3 = int(100 * u.MHz)
resonator_IF_q4 = int(200 * u.MHz)
resonator_IF_q5 = int(100 * u.MHz)
resonator_IF_q6 = int(200 * u.MHz)
resonator_IF_q7 = int(100 * u.MHz)
resonator_IF_q8 = int(100 * u.MHz)
# resontor_delay
resonator_delay = 0

# Readout pulse parameters
readout_len = 1000
readout_amp_q1 = 0.1 # our q1 as their q3
readout_amp_q2 = 0.1
readout_amp_q3 = 0.1
readout_amp_q4 = 0.1
readout_amp_q5 = 0.1
readout_amp_q6 = 0.1
readout_amp_q7 = 0.1
readout_amp_q8 = 0.1

# TOF and depletion time
time_of_flight = 32  # must be a multiple of 4
depletion_time = 2 * u.us

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

    weights_q8 = np.load("optimal_weights_q8.npz")
    opt_weights_real_q8 = convert_integration_weights(weights_q8["weights_real"])
    opt_weights_minus_imag_q8 = convert_integration_weights(weights_q8["weights_minus_imag"])
    opt_weights_imag_q8 = convert_integration_weights(weights_q8["weights_imag"])
    opt_weights_minus_real_q8 = convert_integration_weights(weights_q8["weights_minus_real"])


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

    opt_weights_real_q8 = [(1.0, readout_len)]
    opt_weights_minus_imag_q8 = [(0.0, readout_len)]
    opt_weights_imag_q8 = [(0.0, readout_len)]
    opt_weights_minus_real_q8 = [(-1.0, readout_len)]

# state discrimination
rotation_angle_q1 = (0.0 / 180) * np.pi
rotation_angle_q2 = (0.0 / 180) * np.pi
rotation_angle_q3 = (0.0 / 180) * np.pi
rotation_angle_q4 = (0.0 / 180) * np.pi
rotation_angle_q5 = (0.0 / 180) * np.pi
rotation_angle_q6 = (0.0 / 180) * np.pi
rotation_angle_q7 = (0.0 / 180) * np.pi
rotation_angle_q8 = (0.0 / 180) * np.pi

ge_threshold_q1 = 0.0
ge_threshold_q2 = 0.0
ge_threshold_q3 = 0.0
ge_threshold_q4 = 0.0
ge_threshold_q5 = 0.0
ge_threshold_q6 = 0.0
ge_threshold_q7 = 0.0
ge_threshold_q8 = 0.0

#############################################
#                  Config                   #
#############################################
config = {
    "version": 1,
    "controllers": {
        "con1": {
            "type": "opx1000",
            "fems": {
                1: {
                    # The keyword "band" refers to the following frequency bands:
                    #   1: (50 MHz - 5.5 GHz)
                    #   2: (4.5 GHz - 7.5 GHz)
                    #   3: (6.5 GHz - 10.5 GHz)
                    # The keyword "full_scale_power_dbm" is the maximum power of
                    # normalized pulse waveforms in [-1,1]. To convert to voltage,
                    #   power_mw = 10**(full_scale_power_dbm / 10)
                    #   max_voltage_amp = np.sqrt(2 * power_mw * 50 / 1000)
                    #   amp_in_volts = waveform * max_voltage_amp
                    #   ^ equivalent to OPX+ amp
                    # Its range is -41dBm to +10dBm with 3dBm steps.
                    "type": "MW",
                    "analog_outputs": {
                        1: {
                            "sampling_rate": 1e9,
                            "full_scale_power_dbm": resonator_full_scale_power_dbm,
                            "band": resonator_band,
                            "delay": resonator_delay,
                            "upconverters": {
                                1: {"frequency": resonator_LO1},
                                2: {"frequency": resonator_LO2},
                            },
                        },  # RL1  0.5V => 4dbm +[+6, -45] 3db spacing

                        2: {
                            "sampling_rate": 1e9,
                            "full_scale_power_dbm": qubit_full_scale_power_dbm_q1,
                            "band": qubit_band_q1,
                            "delay": qubit_delay_q1,
                            "upconverters": {
                                1: {"frequency": qubit_LO_q1},  # cr_cancel_LO_c2t1 = qubit_LO_q1
                                2: {"frequency": cr_drive_LO_c1t2},
                            },
                        },  # q1 XY

                        3: {
                            "sampling_rate": 1e9,
                            "full_scale_power_dbm": qubit_full_scale_power_dbm_q2,
                            "band": qubit_band_q2,
                            "delay": qubit_delay_q2,
                            "upconverters": {
                                1: {"frequency": qubit_LO_q2},  # cr_cancel_LO_c1t2 = qubit_LO_q2
                                2: {"frequency": cr_drive_LO_c2t3},
                                # 3: {"frequency": cr_drive_LO_c2t1},
                            },
                        },  # q2 XY

                        4: {
                            "sampling_rate": 1e9,
                            "full_scale_power_dbm": qubit_full_scale_power_dbm_q3,
                            "band": qubit_band_q3,
                            "delay": qubit_delay_q3,
                            "upconverters": {
                                1: {"frequency": qubit_LO_q3}, 
                                2: {"frequency": cr_drive_LO_c3t4},
                                # 3: {"frequency": cr_drive_LO_c3t2},
                            },
                        },  # q3 XY

                        5: {
                            "sampling_rate": 1e9,
                            "full_scale_power_dbm": qubit_full_scale_power_dbm_q4,
                            "band": qubit_band_q4,
                            "delay": qubit_delay_q4,
                            "upconverters": {
                                1: {"frequency": qubit_LO_q4}, 
                                2: {"frequency": cr_drive_LO_c4t5},
                                # 3: {"frequency": cr_drive_LO_c4t3},
                            },
                        },  # q4 XY

                        6: {
                            "sampling_rate": 1e9,
                            "full_scale_power_dbm": qubit_full_scale_power_dbm_q5,
                            "band": qubit_band_q5,
                            "delay": qubit_delay_q5,
                            "upconverters": {
                                1: {"frequency": qubit_LO_q5}, 
                                2: {"frequency": cr_drive_LO_c5t6},
                                # 3: {"frequency": cr_drive_LO_c5t4},
                            },
                        },  # q5 XY

                        7: {
                            "sampling_rate": 1e9,
                            "full_scale_power_dbm": qubit_full_scale_power_dbm_q6,
                            "band": qubit_band_q6,
                            "delay": qubit_delay_q6,
                            "upconverters": {
                                1: {"frequency": qubit_LO_q6}, 
                                2: {"frequency": cr_drive_LO_c6t7},
                                # 3: {"frequency": cr_drive_LO_c6t5},
                            },
                        },  # q6 XY

                        8: {
                            "sampling_rate": 1e9,
                            "full_scale_power_dbm": qubit_full_scale_power_dbm_q7,
                            "band": qubit_band_q7,
                            "delay": qubit_delay_q7,
                            "upconverters": {
                                1: {"frequency": qubit_LO_q7}, 
                                2: {"frequency": cr_drive_LO_c7t6},
                            },
                        },  # q7 XY
                    },
                    "analog_inputs": {
                        1: {
                            "sampling_rate": 1e9,
                            "band": resonator_band,
                            "gain_db": 0,
                            "downconverter_frequency": resonator_LO,
                        },  # RL1, gain_db resolution is 1
                    },
                },
            },
        },
    },
    "elements": {
        "rr1": {
            "MWInput": {
                "port": ("con1", 1, 1),
                "upconverter": 1,
            },
            "intermediate_frequency": resonator_IF_q1,  # in Hz [-350e6, +350e6]
            "MWOutput": {
                "port": ("con1", 1, 1),
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
                "port": ("con1", 1, 1),
                "upconverter": 1,
            },
            "intermediate_frequency": resonator_IF_q2,  # in Hz [-350e6, +350e6]
            "MWOutput": {
                "port": ("con1", 1, 1),
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
                "port": ("con1", 1, 1),
                "upconverter": 1,
            },
            "intermediate_frequency": resonator_IF_q3,  # in Hz [-350e6, +350e6]
            "MWOutput": {
                "port": ("con1", 1, 1),
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
                "port": ("con1", 1, 1),
                "upconverter": 1,
            },
            "intermediate_frequency": resonator_IF_q4,  # in Hz [-350e6, +350e6]
            "MWOutput": {
                "port": ("con1", 1, 1),
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
                "port": ("con1", 1, 1),
                "upconverter": 1,
            },
            "intermediate_frequency": resonator_IF_q5,  # in Hz [-350e6, +350e6]
            "MWOutput": {
                "port": ("con1", 1, 1),
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
                "port": ("con1", 1, 1),
                "upconverter": 1,
            },
            "intermediate_frequency": resonator_IF_q6,  # in Hz [-350e6, +350e6]
            "MWOutput": {
                "port": ("con1", 1, 1),
            },
            "time_of_flight": time_of_flight,
            "smearing": 0,
            "operations": {
                "cw": "const_pulse",
                "readout": "readout_pulse_q6",
            },
        },
         "rr7": {
            "MWInput": {
                "port": ("con1", 1, 1),
                "upconverter": 1,
            },
            "intermediate_frequency": resonator_IF_q7,  # in Hz [-350e6, +350e6]
            "MWOutput": {
                "port": ("con1", 1, 1),
            },
            "time_of_flight": time_of_flight,
            "smearing": 0,
            "operations": {
                "cw": "const_pulse",
                "readout": "readout_pulse_q7",
            },
        },
        #----------------------
        "q1_xy": {
            "MWInput": {
                "port": ("con1", 1, 2),
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
                "port": ("con1", 1, 3),
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
                "port": ("con1", 1, 4),
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
                "port": ("con1", 1, 5),
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
                "port": ("con1", 1, 5),
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
                "port": ("con1", 1, 7),
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
        "q7_xy": {
            "MWInput": {
                "port": ("con1", 1, 8),
                "upconverter": 1,
            },
            "intermediate_frequency": qubit_IF_q7,  # in Hz
            "operations": {
                "cw": "const_pulse",
                "x180": "x180_pulse_q7",
                "x90": "x90_pulse_q7",
                "-x90": "-x90_pulse_q7",
                "y90": "y90_pulse_q7",
                "y180": "y180_pulse_q7",
                "-y90": "-y90_pulse_q7",
            },
        },
        #----------------------
        "cr_drive_c1t2": {
            "MWInput": {
                "port": ("con1", 1, 2),
                "upconverter": 2,
            },
            "intermediate_frequency": cr_drive_IF_c1t2,  # in Hz
            "operations": {
                "cw": "const_pulse",
                "square_positive": "square_positive_pulse_cr_drive_c1t2",
                "square_negative": "square_negative_pulse_cr_drive_c1t2",
            },
        },
        "cr_drive_c2t3": {
            "MWInput": {
                "port": ("con1", 1, 3),
                "upconverter": 2,
            },
            "intermediate_frequency": cr_drive_IF_c2t3,  # in Hz
            "operations": {
                "cw": "const_pulse",
                "square_positive": "square_positive_pulse_cr_drive_c2t3",
                "square_negative": "square_negative_pulse_cr_drive_c2t3",
            },
        },
        "cr_drive_c2t1": {
            "MWInput": {
                "port": ("con1", 1, 3),
                "upconverter": 2, #3
            },
            "intermediate_frequency": cr_drive_IF_c2t1,  # in Hz
            "operations": {
                "cw": "const_pulse",
                "square_positive": "square_positive_pulse_cr_drive_c2t1",
                "square_negative": "square_negative_pulse_cr_drive_c2t1",
            },
        },
        "cr_drive_c3t4": {
            "MWInput": {
                "port": ("con1", 1, 4),
                "upconverter": 2,
            },
            "intermediate_frequency": cr_drive_IF_c3t4,  # in Hz
            "operations": {
                "cw": "const_pulse",
                "square_positive": "square_positive_pulse_cr_drive_c3t4",
                "square_negative": "square_negative_pulse_cr_drive_c3t4",
            },
        },
        "cr_drive_c3t2": {
            "MWInput": {
                "port": ("con1", 1, 4),
                "upconverter": 2, #3
            },
            "intermediate_frequency": cr_drive_IF_c3t2,  # in Hz
            "operations": {
                "cw": "const_pulse",
                "square_positive": "square_positive_pulse_cr_drive_c3t2",
                "square_negative": "square_negative_pulse_cr_drive_c3t2",
            },
        },
        "cr_drive_c4t5": {
            "MWInput": {
                "port": ("con1", 1, 5),
                "upconverter": 2,
            },
            "intermediate_frequency": cr_drive_IF_c4t5,  # in Hz
            "operations": {
                "cw": "const_pulse",
                "square_positive": "square_positive_pulse_cr_drive_c4t5",
                "square_negative": "square_negative_pulse_cr_drive_c4t5",
            },
        },
        "cr_drive_c4t3": {
            "MWInput": {
                "port": ("con1", 1, 5),
                "upconverter": 2, #3
            },
            "intermediate_frequency": cr_drive_IF_c4t3,  # in Hz
            "operations": {
                "cw": "const_pulse",
                "square_positive": "square_positive_pulse_cr_drive_c4t3",
                "square_negative": "square_negative_pulse_cr_drive_c4t3",
            },
        },
        "cr_drive_c5t6": {
            "MWInput": {
                "port": ("con1", 1, 6),
                "upconverter": 2,
            },
            "intermediate_frequency": cr_drive_IF_c5t6,  # in Hz
            "operations": {
                "cw": "const_pulse",
                "square_positive": "square_positive_pulse_cr_drive_c5t6",
                "square_negative": "square_negative_pulse_cr_drive_c5t6",
            },
        },
        "cr_drive_c5t4": {
            "MWInput": {
                "port": ("con1", 1, 6),
                "upconverter": 2, #3
            },
            "intermediate_frequency": cr_drive_IF_c5t4,  # in Hz
            "operations": {
                "cw": "const_pulse",
                "square_positive": "square_positive_pulse_cr_drive_c5t4",
                "square_negative": "square_negative_pulse_cr_drive_c5t4",
            },
        },
        "cr_drive_c6t7": {
            "MWInput": {
                "port": ("con1", 1, 7),
                "upconverter": 2,
            },
            "intermediate_frequency": cr_drive_IF_c6t7,  # in Hz
            "operations": {
                "cw": "const_pulse",
                "square_positive": "square_positive_pulse_cr_drive_c6t7",
                "square_negative": "square_negative_pulse_cr_drive_c6t7",
            },
        },
        "cr_drive_c6t5": {
            "MWInput": {
                "port": ("con1", 1, 7),
                "upconverter": 2, #3
            },
            "intermediate_frequency": cr_drive_IF_c6t5,  # in Hz
            "operations": {
                "cw": "const_pulse",
                "square_positive": "square_positive_pulse_cr_drive_c6t5",
                "square_negative": "square_negative_pulse_cr_drive_c6t5",
            },
        },
        "cr_drive_c7t6": {
            "MWInput": {
                "port": ("con1", 1, 8),
                "upconverter": 2,
            },
            "intermediate_frequency": cr_drive_IF_c7t6,  # in Hz
            "operations": {
                "cw": "const_pulse",
                "square_positive": "square_positive_pulse_cr_drive_c7t6",
                "square_negative": "square_negative_pulse_cr_drive_c7t6",
            },
        },
        #----------------------
        "cr_cancel_c1t2": {
            "MWInput": {
                "port": ("con1", 1, 2),
                "upconverter": 2,
            },
            "intermediate_frequency": cr_cancel_IF_c1t2,  # in Hz
            "operations": {
                "cw": "const_pulse",
                "square_positive": "square_positive_pulse_cr_cancel_c1t2",
                "square_negative": "square_negative_pulse_cr_cancel_c1t2",
            },
        },
        "cr_cancel_c2t3": {
            "MWInput": {
                "port": ("con1", 1, 3),
                "upconverter": 2,
            },
            "intermediate_frequency": cr_cancel_IF_c2t3,  # in Hz
            "operations": {
                "cw": "const_pulse",
                "square_positive": "square_positive_pulse_cr_cancel_c2t3",
                "square_negative": "square_negative_pulse_cr_cancel_c2t3",
            },
        },
        "cr_cancel_c2t1": {
            "MWInput": {
                "port": ("con1", 1, 3),
                "upconverter": 2, #3
            },
            "intermediate_frequency": cr_cancel_IF_c2t1,  # in Hz
            "operations": {
                "cw": "const_pulse",
                "square_positive": "square_positive_pulse_cr_cancel_c2t1",
                "square_negative": "square_negative_pulse_cr_cancel_c2t1",
            },
        },
        "cr_cancel_c3t4": {
            "MWInput": {
                "port": ("con1", 1, 4),
                "upconverter": 2,
            },
            "intermediate_frequency": cr_cancel_IF_c3t4,  # in Hz
            "operations": {
                "cw": "const_pulse",
                "square_positive": "square_positive_pulse_cr_cancel_c3t4",
                "square_negative": "square_negative_pulse_cr_cancel_c3t4",
            },
        },
        "cr_cancel_c3t2": {
            "MWInput": {
                "port": ("con1", 1, 4),
                "upconverter": 2, #3
            },
            "intermediate_frequency": cr_cancel_IF_c3t2,  # in Hz
            "operations": {
                "cw": "const_pulse",
                "square_positive": "square_positive_pulse_cr_cancel_c3t2",
                "square_negative": "square_negative_pulse_cr_cancel_c3t2",
            },
        },
        "cr_cancel_c4t5": {
            "MWInput": {
                "port": ("con1", 1, 5),
                "upconverter": 2,
            },
            "intermediate_frequency": cr_cancel_IF_c4t5,  # in Hz
            "operations": {
                "cw": "const_pulse",
                "square_positive": "square_positive_pulse_cr_cancel_c4t5",
                "square_negative": "square_negative_pulse_cr_cancel_c4t5",
            },
        },
        "cr_cancel_c4t3": {
            "MWInput": {
                "port": ("con1", 1, 5),
                "upconverter": 2, #3,
            },
            "intermediate_frequency": cr_cancel_IF_c4t3,  # in Hz
            "operations": {
                "cw": "const_pulse",
                "square_positive": "square_positive_pulse_cr_cancel_c4t3",
                "square_negative": "square_negative_pulse_cr_cancel_c4t3",
            },
        },
        "cr_cancel_c5t6": {
            "MWInput": {
                "port": ("con1", 1, 6),
                "upconverter": 2,
            },
            "intermediate_frequency": cr_cancel_IF_c5t6,  # in Hz
            "operations": {
                "cw": "const_pulse",
                "square_positive": "square_positive_pulse_cr_cancel_c5t6",
                "square_negative": "square_negative_pulse_cr_cancel_c5t6",
            },
        },
        "cr_cancel_c5t4": {
            "MWInput": {
                "port": ("con1", 1, 6),
                "upconverter": 2, #3
            },
            "intermediate_frequency": cr_cancel_IF_c5t4,  # in Hz
            "operations": {
                "cw": "const_pulse",
                "square_positive": "square_positive_pulse_cr_cancel_c5t4",
                "square_negative": "square_negative_pulse_cr_cancel_c5t4",
            },
        },
        "cr_cancel_c6t7": {
            "MWInput": {
                "port": ("con1", 1, 7),
                "upconverter": 2,
            },
            "intermediate_frequency": cr_cancel_IF_c6t7,  # in Hz
            "operations": {
                "cw": "const_pulse",
                "square_positive": "square_positive_pulse_cr_cancel_c6t7",
                "square_negative": "square_negative_pulse_cr_cancel_c6t7",
            },
        },
        "cr_cancel_c6t5": {
            "MWInput": {
                "port": ("con1", 1, 7),
                "upconverter": 2, #3
            },
            "intermediate_frequency": cr_cancel_IF_c6t5,  # in Hz
            "operations": {
                "cw": "const_pulse",
                "square_positive": "square_positive_pulse_cr_cancel_c6t5",
                "square_negative": "square_negative_pulse_cr_cancel_c6t5",
            },
        },
        "cr_cancel_c7t6": {
            "MWInput": {
                "port": ("con1", 1, 8),
                "upconverter": 2,
            },
            "intermediate_frequency": cr_cancel_IF_c7t6,  # in Hz
            "operations": {
                "cw": "const_pulse",
                "square_positive": "square_positive_pulse_cr_cancel_c7t6",
                "square_negative": "square_negative_pulse_cr_cancel_c7t6",
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
        #------------------
        "x90_pulse_q7": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "x90_I_wf_q7",
                "Q": "x90_Q_wf_q7",
            },
        },
        "x180_pulse_q7": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "x180_I_wf_q7",
                "Q": "x180_Q_wf_q7",
            },
        },
        "-x90_pulse_q7": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "minus_x90_I_wf_q7",
                "Q": "minus_x90_Q_wf_q7",
            },
        },
        "y90_pulse_q7": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "y90_I_wf_q7",
                "Q": "y90_Q_wf_q7",
            },
        },
        "y180_pulse_q7": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "y180_I_wf_q7",
                "Q": "y180_Q_wf_q7",
            },
        },
        "-y90_pulse_q7": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "minus_y90_I_wf_q7",
                "Q": "minus_y90_Q_wf_q7",
            },
        },
        "readout_pulse_q7": {
            "operation": "measurement",
            "length": readout_len,
            "waveforms": {
                "I": "readout_wf_q7",
                "Q": "zero_wf",
            },
            "integration_weights": {
                "cos": "cosine_weights",
                "sin": "sine_weights",
                "minus_sin": "minus_sine_weights",
                "rotated_cos": "rotated_cosine_weights_q7",
                "rotated_sin": "rotated_sine_weights_q7",
                "rotated_minus_sin": "rotated_minus_sine_weights_q7",
                "opt_cos": "opt_cosine_weights_q7",
                "opt_sin": "opt_sine_weights_q7",
                "opt_minus_sin": "opt_minus_sine_weights_q7",
            },
            "digital_marker": "ON",
        },
        #------------------
        "square_positive_pulse_cr_drive_c1t2": {
            "operation": "control",
            "length": cr_drive_square_len_c1t2,
            "waveforms": {"I": "square_positive_wf_cr_drive_c1t2", "Q": "zero_wf"},
        },
        "square_positive_pulse_cr_drive_c2t3": {
            "operation": "control",
            "length": cr_drive_square_len_c2t3,
            "waveforms": {"I": "square_positive_wf_cr_drive_c2t3", "Q": "zero_wf"},
        },
        "square_positive_pulse_cr_drive_c2t1": {
            "operation": "control",
            "length": cr_drive_square_len_c2t1,
            "waveforms": {"I": "square_positive_wf_cr_drive_c2t1", "Q": "zero_wf"},
        },
        "square_positive_pulse_cr_drive_c3t4": {
            "operation": "control",
            "length": cr_drive_square_len_c3t4,
            "waveforms": {"I": "square_positive_wf_cr_drive_c3t4", "Q": "zero_wf"},
        },
        "square_positive_pulse_cr_drive_c3t2": {
            "operation": "control",
            "length": cr_drive_square_len_c3t2,
            "waveforms": {"I": "square_positive_wf_cr_drive_c3t2", "Q": "zero_wf"},
        },
        "square_positive_pulse_cr_drive_c4t5": {
            "operation": "control",
            "length": cr_drive_square_len_c4t5,
            "waveforms": {"I": "square_positive_wf_cr_drive_c4t5", "Q": "zero_wf"},
        },
        "square_positive_pulse_cr_drive_c4t3": {
            "operation": "control",
            "length": cr_drive_square_len_c4t3,
            "waveforms": {"I": "square_positive_wf_cr_drive_c4t3", "Q": "zero_wf"},
        },
        "square_positive_pulse_cr_drive_c5t6": {
            "operation": "control",
            "length": cr_drive_square_len_c5t6,
            "waveforms": {"I": "square_positive_wf_cr_drive_c5t6", "Q": "zero_wf"},
        },
        "square_positive_pulse_cr_drive_c5t4": {
            "operation": "control",
            "length": cr_drive_square_len_c5t4,
            "waveforms": {"I": "square_positive_wf_cr_drive_c5t4", "Q": "zero_wf"},
        },
        "square_positive_pulse_cr_drive_c6t7": {
            "operation": "control",
            "length": cr_drive_square_len_c6t7,
            "waveforms": {"I": "square_positive_wf_cr_drive_c6t7", "Q": "zero_wf"},
        },
        "square_positive_pulse_cr_drive_c6t5": {
            "operation": "control",
            "length": cr_drive_square_len_c6t5,
            "waveforms": {"I": "square_positive_wf_cr_drive_c6t5", "Q": "zero_wf"},
        },
        "square_positive_pulse_cr_drive_c7t6": {
            "operation": "control",
            "length": cr_drive_square_len_c7t6,
            "waveforms": {"I": "square_positive_wf_cr_drive_c7t6", "Q": "zero_wf"},
        },
        #------------------
        "square_negative_pulse_cr_drive_c1t2": {
            "operation": "control",
            "length": cr_drive_square_len_c1t2,
            "waveforms": {"I": "square_negative_wf_cr_drive_c1t2", "Q": "zero_wf"},
        },
        "square_negative_pulse_cr_drive_c2t3": {
            "operation": "control",
            "length": cr_drive_square_len_c2t3,
            "waveforms": {"I": "square_negative_wf_cr_drive_c2t3", "Q": "zero_wf"},
        },
        "square_negative_pulse_cr_drive_c2t1": {
            "operation": "control",
            "length": cr_drive_square_len_c2t1,
            "waveforms": {"I": "square_negative_wf_cr_drive_c2t1", "Q": "zero_wf"},
        },
        "square_negative_pulse_cr_drive_c3t4": {
            "operation": "control",
            "length": cr_drive_square_len_c3t4,
            "waveforms": {"I": "square_negative_wf_cr_drive_c3t4", "Q": "zero_wf"},
        },
        "square_negative_pulse_cr_drive_c3t2": {
            "operation": "control",
            "length": cr_drive_square_len_c3t2,
            "waveforms": {"I": "square_negative_wf_cr_drive_c3t2", "Q": "zero_wf"},
        },
        "square_negative_pulse_cr_drive_c4t5": {
            "operation": "control",
            "length": cr_drive_square_len_c4t5,
            "waveforms": {"I": "square_negative_wf_cr_drive_c4t5", "Q": "zero_wf"},
        },
        "square_negative_pulse_cr_drive_c4t3": {
            "operation": "control",
            "length": cr_drive_square_len_c4t3,
            "waveforms": {"I": "square_negative_wf_cr_drive_c4t3", "Q": "zero_wf"},
        },
        "square_negative_pulse_cr_drive_c5t6": {
            "operation": "control",
            "length": cr_drive_square_len_c5t6,
            "waveforms": {"I": "square_negative_wf_cr_drive_c5t6", "Q": "zero_wf"},
        },
        "square_negative_pulse_cr_drive_c5t4": {
            "operation": "control",
            "length": cr_drive_square_len_c5t4,
            "waveforms": {"I": "square_negative_wf_cr_drive_c5t4", "Q": "zero_wf"},
        },
        "square_negative_pulse_cr_drive_c6t7": {
            "operation": "control",
            "length": cr_drive_square_len_c6t7,
            "waveforms": {"I": "square_negative_wf_cr_drive_c6t7", "Q": "zero_wf"},
        },
        "square_negative_pulse_cr_drive_c6t5": {
            "operation": "control",
            "length": cr_drive_square_len_c6t5,
            "waveforms": {"I": "square_negative_wf_cr_drive_c6t5", "Q": "zero_wf"},
        },
        "square_negative_pulse_cr_drive_c7t6": {
            "operation": "control",
            "length": cr_drive_square_len_c7t6,
            "waveforms": {"I": "square_negative_wf_cr_drive_c7t6", "Q": "zero_wf"},
        },
        #------------------
        "square_positive_pulse_cr_cancel_c1t2": {
            "operation": "control",
            "length": cr_cancel_square_len_c1t2,
            "waveforms": {"I": "square_positive_wf_cr_cancel_c1t2", "Q": "zero_wf"},
        },
        "square_positive_pulse_cr_cancel_c2t3": {
            "operation": "control",
            "length": cr_cancel_square_len_c2t3,
            "waveforms": {"I": "square_positive_wf_cr_cancel_c2t3", "Q": "zero_wf"},
        },
        "square_positive_pulse_cr_cancel_c2t1": {
            "operation": "control",
            "length": cr_cancel_square_len_c2t1,
            "waveforms": {"I": "square_positive_wf_cr_cancel_c2t1", "Q": "zero_wf"},
        },
        "square_positive_pulse_cr_cancel_c3t4": {
            "operation": "control",
            "length": cr_cancel_square_len_c3t4,
            "waveforms": {"I": "square_positive_wf_cr_cancel_c3t4", "Q": "zero_wf"},
        },
        "square_positive_pulse_cr_cancel_c3t2": {
            "operation": "control",
            "length": cr_cancel_square_len_c3t2,
            "waveforms": {"I": "square_positive_wf_cr_cancel_c3t2", "Q": "zero_wf"},
        },
        "square_positive_pulse_cr_cancel_c4t5": {
            "operation": "control",
            "length": cr_cancel_square_len_c4t5,
            "waveforms": {"I": "square_positive_wf_cr_cancel_c4t5", "Q": "zero_wf"},
        },
        "square_positive_pulse_cr_cancel_c4t3": {
            "operation": "control",
            "length": cr_cancel_square_len_c4t3,
            "waveforms": {"I": "square_positive_wf_cr_cancel_c4t3", "Q": "zero_wf"},
        },
        "square_positive_pulse_cr_cancel_c5t6": {
            "operation": "control",
            "length": cr_cancel_square_len_c5t6,
            "waveforms": {"I": "square_positive_wf_cr_cancel_c5t6", "Q": "zero_wf"},
        },
        "square_positive_pulse_cr_cancel_c5t4": {
            "operation": "control",
            "length": cr_cancel_square_len_c5t4,
            "waveforms": {"I": "square_positive_wf_cr_cancel_c5t4", "Q": "zero_wf"},
        },
        "square_positive_pulse_cr_cancel_c6t7": {
            "operation": "control",
            "length": cr_cancel_square_len_c6t7,
            "waveforms": {"I": "square_positive_wf_cr_cancel_c6t7", "Q": "zero_wf"},
        },
        "square_positive_pulse_cr_cancel_c6t5": {
            "operation": "control",
            "length": cr_cancel_square_len_c6t5,
            "waveforms": {"I": "square_positive_wf_cr_cancel_c6t5", "Q": "zero_wf"},
        },
        "square_positive_pulse_cr_cancel_c7t6": {
            "operation": "control",
            "length": cr_cancel_square_len_c7t6,
            "waveforms": {"I": "square_positive_wf_cr_cancel_c7t6", "Q": "zero_wf"},
        },
        #------------------
        "square_negative_pulse_cr_cancel_c1t2": {
            "operation": "control",
            "length": cr_cancel_square_len_c1t2,
            "waveforms": {"I": "square_negative_wf_cr_cancel_c1t2", "Q": "zero_wf"},
        },
        "square_negative_pulse_cr_cancel_c2t3": {
            "operation": "control",
            "length": cr_cancel_square_len_c2t3,
            "waveforms": {"I": "square_negative_wf_cr_cancel_c2t3", "Q": "zero_wf"},
        },
        "square_negative_pulse_cr_cancel_c2t1": {
            "operation": "control",
            "length": cr_cancel_square_len_c2t1,
            "waveforms": {"I": "square_negative_wf_cr_cancel_c2t1", "Q": "zero_wf"},
        },
        "square_negative_pulse_cr_cancel_c3t4": {
            "operation": "control",
            "length": cr_cancel_square_len_c3t4,
            "waveforms": {"I": "square_negative_wf_cr_cancel_c3t4", "Q": "zero_wf"},
        },
        "square_negative_pulse_cr_cancel_c3t2": {
            "operation": "control",
            "length": cr_cancel_square_len_c3t2,
            "waveforms": {"I": "square_negative_wf_cr_cancel_c3t2", "Q": "zero_wf"},
        },
        "square_negative_pulse_cr_cancel_c4t5": {
            "operation": "control",
            "length": cr_cancel_square_len_c4t5,
            "waveforms": {"I": "square_negative_wf_cr_cancel_c4t5", "Q": "zero_wf"},
        },
        "square_negative_pulse_cr_cancel_c4t3": {
            "operation": "control",
            "length": cr_cancel_square_len_c4t3,
            "waveforms": {"I": "square_negative_wf_cr_cancel_c4t3", "Q": "zero_wf"},
        },
        "square_negative_pulse_cr_cancel_c5t6": {
            "operation": "control",
            "length": cr_cancel_square_len_c5t6,
            "waveforms": {"I": "square_negative_wf_cr_cancel_c5t6", "Q": "zero_wf"},
        },
        "square_negative_pulse_cr_cancel_c5t4": {
            "operation": "control",
            "length": cr_cancel_square_len_c5t4,
            "waveforms": {"I": "square_negative_wf_cr_cancel_c5t4", "Q": "zero_wf"},
        },
        "square_negative_pulse_cr_cancel_c6t7": {
            "operation": "control",
            "length": cr_cancel_square_len_c6t7,
            "waveforms": {"I": "square_negative_wf_cr_cancel_c6t7", "Q": "zero_wf"},
        },
        "square_negative_pulse_cr_cancel_c6t5": {
            "operation": "control",
            "length": cr_cancel_square_len_c6t5,
            "waveforms": {"I": "square_negative_wf_cr_cancel_c6t5", "Q": "zero_wf"},
        },
        "square_negative_pulse_cr_cancel_c7t6": {
            "operation": "control",
            "length": cr_cancel_square_len_c7t6,
            "waveforms": {"I": "square_negative_wf_cr_cancel_c7t6", "Q": "zero_wf"},
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
        #------------------
        "x90_I_wf_q7": {"type": "arbitrary", "samples": x90_I_wf_q7.tolist()},
        "x90_Q_wf_q7": {"type": "arbitrary", "samples": x90_Q_wf_q7.tolist()},
        "x180_I_wf_q7": {"type": "arbitrary", "samples": x180_I_wf_q7.tolist()},
        "x180_Q_wf_q7": {"type": "arbitrary", "samples": x180_Q_wf_q7.tolist()},
        "minus_x90_I_wf_q7": {"type": "arbitrary", "samples": minus_x90_I_wf_q7.tolist()},
        "minus_x90_Q_wf_q7": {"type": "arbitrary", "samples": minus_x90_Q_wf_q7.tolist()},
        "y90_I_wf_q7": {"type": "arbitrary", "samples": y90_I_wf_q7.tolist()},
        "y90_Q_wf_q7": {"type": "arbitrary", "samples": y90_Q_wf_q7.tolist()},
        "y180_I_wf_q7": {"type": "arbitrary", "samples": y180_I_wf_q7.tolist()},
        "y180_Q_wf_q7": {"type": "arbitrary", "samples": y180_Q_wf_q7.tolist()},
        "minus_y90_I_wf_q7": {"type": "arbitrary", "samples": minus_y90_I_wf_q7.tolist()},
        "minus_y90_Q_wf_q7": {"type": "arbitrary", "samples": minus_y90_Q_wf_q7.tolist()},
        "readout_wf_q7": {"type": "constant", "sample": readout_amp_q7},
        #------------------
        "square_positive_wf_cr_drive_c1t2": {"type": "constant", "sample": cr_drive_square_amp_c1t2},
        "square_negative_wf_cr_drive_c1t2": {"type": "constant", "sample": -cr_drive_square_amp_c1t2},
        "square_positive_wf_cr_cancel_c1t2": {"type": "constant", "sample": cr_cancel_square_amp_c1t2},
        "square_negative_wf_cr_cancel_c1t2": {"type": "constant", "sample": -cr_cancel_square_amp_c1t2},
        #------------------
        "square_positive_wf_cr_drive_c2t3": {"type": "constant", "sample": cr_drive_square_amp_c2t3},
        "square_negative_wf_cr_drive_c2t3": {"type": "constant", "sample": -cr_drive_square_amp_c2t3},
        "square_positive_wf_cr_cancel_c2t3": {"type": "constant", "sample": cr_cancel_square_amp_c2t3},
        "square_negative_wf_cr_cancel_c2t3": {"type": "constant", "sample": -cr_cancel_square_amp_c2t3},
        #------------------
        "square_positive_wf_cr_drive_c2t1": {"type": "constant", "sample": cr_drive_square_amp_c2t1},
        "square_negative_wf_cr_drive_c2t1": {"type": "constant", "sample": -cr_drive_square_amp_c2t1},
        "square_positive_wf_cr_cancel_c2t1": {"type": "constant", "sample": cr_cancel_square_amp_c2t1},
        "square_negative_wf_cr_cancel_c2t1": {"type": "constant", "sample": -cr_cancel_square_amp_c2t1},
        #------------------
        "square_positive_wf_cr_drive_c3t4": {"type": "constant", "sample": cr_drive_square_amp_c3t4},
        "square_negative_wf_cr_drive_c3t4": {"type": "constant", "sample": -cr_drive_square_amp_c3t4},
        "square_positive_wf_cr_cancel_c3t4": {"type": "constant", "sample": cr_cancel_square_amp_c3t4},
        "square_negative_wf_cr_cancel_c3t4": {"type": "constant", "sample": -cr_cancel_square_amp_c3t4},
        #------------------
        "square_positive_wf_cr_drive_c3t2": {"type": "constant", "sample": cr_drive_square_amp_c3t2},
        "square_negative_wf_cr_drive_c3t2": {"type": "constant", "sample": -cr_drive_square_amp_c3t2},
        "square_positive_wf_cr_cancel_c3t2": {"type": "constant", "sample": cr_cancel_square_amp_c3t2},
        "square_negative_wf_cr_cancel_c3t2": {"type": "constant", "sample": -cr_cancel_square_amp_c3t2},
        #------------------
        "square_positive_wf_cr_drive_c4t5": {"type": "constant", "sample": cr_drive_square_amp_c4t5},
        "square_negative_wf_cr_drive_c4t5": {"type": "constant", "sample": -cr_drive_square_amp_c4t5},
        "square_positive_wf_cr_cancel_c4t5": {"type": "constant", "sample": cr_cancel_square_amp_c4t5},
        "square_negative_wf_cr_cancel_c4t5": {"type": "constant", "sample": -cr_cancel_square_amp_c4t5},
        #------------------
        "square_positive_wf_cr_drive_c4t3": {"type": "constant", "sample": cr_drive_square_amp_c4t3},
        "square_negative_wf_cr_drive_c4t3": {"type": "constant", "sample": -cr_drive_square_amp_c4t3},
        "square_positive_wf_cr_cancel_c4t3": {"type": "constant", "sample": cr_cancel_square_amp_c4t3},
        "square_negative_wf_cr_cancel_c4t3": {"type": "constant", "sample": -cr_cancel_square_amp_c4t3},
        #------------------
        "square_positive_wf_cr_drive_c5t6": {"type": "constant", "sample": cr_drive_square_amp_c5t6},
        "square_negative_wf_cr_drive_c5t6": {"type": "constant", "sample": -cr_drive_square_amp_c5t6},
        "square_positive_wf_cr_cancel_c5t6": {"type": "constant", "sample": cr_cancel_square_amp_c5t6},
        "square_negative_wf_cr_cancel_c5t6": {"type": "constant", "sample": -cr_cancel_square_amp_c5t6},
        #------------------
        "square_positive_wf_cr_drive_c5t4": {"type": "constant", "sample": cr_drive_square_amp_c5t4},
        "square_negative_wf_cr_drive_c5t4": {"type": "constant", "sample": -cr_drive_square_amp_c5t4},
        "square_positive_wf_cr_cancel_c5t4": {"type": "constant", "sample": cr_cancel_square_amp_c5t4},
        "square_negative_wf_cr_cancel_c5t4": {"type": "constant", "sample": -cr_cancel_square_amp_c5t4},
        #------------------
        "square_positive_wf_cr_drive_c6t7": {"type": "constant", "sample": cr_drive_square_amp_c6t7},
        "square_negative_wf_cr_drive_c6t7": {"type": "constant", "sample": -cr_drive_square_amp_c6t7},
        "square_positive_wf_cr_cancel_c6t7": {"type": "constant", "sample": cr_cancel_square_amp_c6t7},
        "square_negative_wf_cr_cancel_c6t7": {"type": "constant", "sample": -cr_cancel_square_amp_c6t7},
        #------------------
        "square_positive_wf_cr_drive_c6t5": {"type": "constant", "sample": cr_drive_square_amp_c6t5},
        "square_negative_wf_cr_drive_c6t5": {"type": "constant", "sample": -cr_drive_square_amp_c6t5},
        "square_positive_wf_cr_cancel_c6t5": {"type": "constant", "sample": cr_cancel_square_amp_c6t5},
        "square_negative_wf_cr_cancel_c6t5": {"type": "constant", "sample": -cr_cancel_square_amp_c6t5},
        #------------------
        "square_positive_wf_cr_drive_c7t6": {"type": "constant", "sample": cr_drive_square_amp_c7t6},
        "square_negative_wf_cr_drive_c7t6": {"type": "constant", "sample": -cr_drive_square_amp_c7t6},
        "square_positive_wf_cr_cancel_c7t6": {"type": "constant", "sample": cr_cancel_square_amp_c7t6},
        "square_negative_wf_cr_cancel_c7t6": {"type": "constant", "sample": -cr_cancel_square_amp_c7t6},
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
        "rotated_cosine_weights_q7": {
            "cosine": [(np.cos(rotation_angle_q7), readout_len)],
            "sine": [(np.sin(rotation_angle_q7), readout_len)],
        },
        "rotated_sine_weights_q7": {
            "cosine": [(-np.sin(rotation_angle_q7), readout_len)],
            "sine": [(np.cos(rotation_angle_q7), readout_len)],
        },
        "rotated_minus_sine_weights_q7": {
            "cosine": [(np.sin(rotation_angle_q7), readout_len)],
            "sine": [(-np.cos(rotation_angle_q7), readout_len)],
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
        #------------------
        "opt_cosine_weights_q7": {
            "cosine": opt_weights_real_q7,
            "sine": opt_weights_minus_imag_q7,
        },
        "opt_sine_weights_q7": {
            "cosine": opt_weights_imag_q7,
            "sine": opt_weights_real_q7,
        },
        "opt_minus_sine_weights_q7": {
            "cosine": opt_weights_minus_imag_q7,
            "sine": opt_weights_minus_real_q7,
        },
    },
}

# %%