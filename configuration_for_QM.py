"""
QUA-Config supporting OPX1000 w/ LF-FEM + MW-FEM
"""



from pathlib import Path
import numpy as np
from qualang_tools.config.waveform_tools import drag_gaussian_pulse_waveforms
from qualang_tools.units import unit

from scipy.signal.windows import gaussian, blackman


drag_coef_q1_setting = 0.5

drag_coef_q2_setting = -0.1 

const_flux_len_setting = 100 
const_flux_amp_setting = 1.5 

readout_amp_q1_setting = 0.4

readout_amp_q2_setting = 0.4

rotation_angle_q1_setting = ((300) / 180) * np.pi 

rotation_angle_q2_setting = ((200) / 180) * np.pi 

ge_threshold_q1_setting = 8e-04 
ge_threshold_q2_setting = 4e-04 

######################
# Network parameters #
######################
qop_ip = "192.168.88.250"  # Write the QM router IP address
cluster_name = "Cluster_1"  # Write your cluster_name if version >= QOP220
qop_port = None  # Write the QOP port if version < QOP220

# Path to save data
save_dir = Path().absolute() / "QM" / "INSTALLATION" / "data"

#####################
# OPX configuration #
#####################
con = "con1"

lf_fem1 = 1
lf_fem2 = 2

mw_fem1 = 3
mw_fem2 = 4
mw_fem3 = 5

# Set octave_config to None if no octave are present
octave_config = None

#############################################
#                  Qubits                   #
#############################################
u = unit(coerce_to_integer=True)

sampling_rate = int(1e9)  

qubit_LO_q1 = 5.5 * u.GHz
qubit_LO_q2 = 5.0 * u.GHz
qubit_LO_q3 = 5.5 * u.GHz

qubit_LO_q4 = 5.0 * u.GHz
qubit_LO_q5 = 5.5 * u.GHz
qubit_LO_q6 = 5.0 * u.GHz 

qubit_LO_q7 = 5.0 * u.GHz 
qubit_LO_q8 = 5.0 * u.GHz
qubit_LO_q9 = 5.5 * u.GHz
qubit_LO_q10 = 5.0 * u.GHz
qubit_LO_q11 = 5.5 * u.GHz
qubit_LO_q12 = 5.5 * u.GHz
qubit_LO_q13 = 5.0 * u.GHz
qubit_LO_q14 = 5.5 * u.GHz
qubit_LO_q15 = 5.0 * u.GHz
qubit_LO_q16 = 5.5 * u.GHz
qubit_LO_q17 = 5.0 * u.GHz
qubit_LO_q18 = 5.5 * u.GHz
qubit_LO_q19 = 5.0 * u.GHz
qubit_LO_q20 = 5.5 * u.GHz

qubit_LO_q_C6 = (5.0) * u.GHz

qubit_IF_q1 = (110) * u.MHz 
qubit_IF_q2 = (120) * u.MHz 
qubit_IF_q3 = (130) * u.MHz 
qubit_IF_q4 = (140) * u.MHz 
qubit_IF_q5 = (150) * u.MHz
qubit_IF_q6 = (160) * u.MHz 
qubit_IF_q7 = (170) * u.MHz 
qubit_IF_q8 = (180) * u.MHz
qubit_IF_q9 = (190) * u.MHz
qubit_IF_q10 = (200) * u.MHz
qubit_IF_q11 = (210) * u.MHz
qubit_IF_q12 = (220) * u.MHz
qubit_IF_q13 = (230) * u.MHz
qubit_IF_q14 = (240) * u.MHz
qubit_IF_q15 = (250) * u.MHz
qubit_IF_q16 = (260) * u.MHz
qubit_IF_q17 = (270) * u.MHz
qubit_IF_q18 =  (280) * u.MHz 
qubit_IF_q19 = (290) * u.MHz
qubit_IF_q20 = (300) * u.MHz

qubit_IF_q_C6 = (0) * u.MHz


qubit_power = -5 


#osc
osc_power = -5
osc_LO = 100 * u.MHz

# Relaxation time
qubit1_T1 = 50 * u.us
qubit2_T1 = 50 * u.us
thermalization_time = 5 * max(qubit1_T1, qubit2_T1)

# Note: amplitudes can be -1..1 and are scaled up to `qubit_power` at amp=1
# CW pulse parameter
const_len = 1000
const_amp = 0.35 
const_amp_dc = 1.0 

frequency_sine_Hz=10e6
# Saturation_pulse
saturation_len = 10 * u.us
saturation_amp = 0.35
# Pi pulse parameters
pi_len = 20
pi_sigma = pi_len / 5

pi_amp_q1 = 0.1
pi_amp_q2 = 0.15
pi_amp_q3 = 0.2
pi_amp_q4 = 0.25
pi_amp_q5 = 0.3
pi_amp_q6 = 0.35
pi_amp_q7 = 0.4
pi_amp_q8 = 0.45
pi_amp_q9 = 0.5
pi_amp_q10 = 0.55
pi_amp_q11 = 0.6
pi_amp_q12 = 0.65
pi_amp_q13 = 0.7
pi_amp_q14 = 0.75
pi_amp_q15 = 0.8
pi_amp_q16 = 0.85
pi_amp_q17 = 0.9
pi_amp_q18 = 0.95
pi_amp_q19 = 1.0
pi_amp_q20 = 0.05

pi_amp_q_C6 = 0.2

# DRAG coefficients
drag_coef_q1 = 0.05
drag_coef_q2 = 0.1
drag_coef_q3 = 0.15
drag_coef_q4 = 0.2
drag_coef_q5 = 0.25
drag_coef_q6 = 0.3
drag_coef_q7 = 0.35
drag_coef_q8 = 0.4
drag_coef_q9 = 0.45
drag_coef_q10 = 0.5
drag_coef_q11 = 0.55 
drag_coef_q12 = 0.6
drag_coef_q13 = 0.65
drag_coef_q14 = 0.7
drag_coef_q15 = 0.75
drag_coef_q16 = 0.8
drag_coef_q17 = 0.85
drag_coef_q18 = 0.9
drag_coef_q19 = 0.95
drag_coef_q20 = 1.0

drag_coef_q_C6 = 0.500

anharmonicity_q1 = -250 * u.MHz
anharmonicity_q2 = -250 * u.MHz
anharmonicity_q3 = -250 * u.MHz
anharmonicity_q4 = -250 * u.MHz
anharmonicity_q5 = -250 * u.MHz
anharmonicity_q6 = -250 * u.MHz
anharmonicity_q7 = -250 * u.MHz
anharmonicity_q8 = -250 * u.MHz
anharmonicity_q9 = -250 * u.MHz
anharmonicity_q10 = -250 * u.MHz
anharmonicity_q11 = -250 * u.MHz
anharmonicity_q12 = -250 * u.MHz
anharmonicity_q13 = -250 * u.MHz
anharmonicity_q14 = -250 * u.MHz
anharmonicity_q15 = -250 * u.MHz
anharmonicity_q16 = -250 * u.MHz
anharmonicity_q17 = -250 * u.MHz
anharmonicity_q18 = -250 * u.MHz
anharmonicity_q19 = -250 * u.MHz
anharmonicity_q20 = -250 * u.MHz

anharmonicity_q_C6 = -250 * u.MHz


AC_stark_detuning_q1 = 0 * u.MHz
AC_stark_detuning_q2 = 0 * u.MHz
AC_stark_detuning_q3 = 0 * u.MHz
AC_stark_detuning_q4 = 0 * u.MHz
AC_stark_detuning_q5 = 0 * u.MHz
AC_stark_detuning_q6 = 0 * u.MHz
AC_stark_detuning_q7 = 0 * u.MHz
AC_stark_detuning_q8 = 0 * u.MHz
AC_stark_detuning_q9 = 0 * u.MHz
AC_stark_detuning_q10 = 0 * u.MHz
AC_stark_detuning_q11 = 0 * u.MHz
AC_stark_detuning_q12 = 0 * u.MHz
AC_stark_detuning_q13 = 0 * u.MHz
AC_stark_detuning_q14 = 0 * u.MHz
AC_stark_detuning_q15 = 0 * u.MHz
AC_stark_detuning_q16 = 0 * u.MHz
AC_stark_detuning_q17 = 0 * u.MHz
AC_stark_detuning_q18 = 0 * u.MHz
AC_stark_detuning_q19 = 0 * u.MHz
AC_stark_detuning_q20 = 0 * u.MHz
AC_stark_detuning_q_C6 = 0 * u.MHz


# DRAG waveforms
x180_wf_q1, x180_der_wf_q1 = np.array(
    drag_gaussian_pulse_waveforms(
        amplitude=pi_amp_q1,
        length=pi_len,
        sigma=pi_sigma,
        alpha=drag_coef_q1,
        anharmonicity=anharmonicity_q1,
        detuning=AC_stark_detuning_q1,
        sampling_rate=sampling_rate,
    )
)
x180_I_wf_q1 = x180_wf_q1
x180_Q_wf_q1 = x180_der_wf_q1

x180_wf_q2, x180_der_wf_q2 = np.array(
    drag_gaussian_pulse_waveforms(
        pi_amp_q2, pi_len, pi_sigma, drag_coef_q2, anharmonicity_q2, AC_stark_detuning_q2, sampling_rate=sampling_rate
    )
)
x180_I_wf_q2 = x180_wf_q2
x180_Q_wf_q2 = x180_der_wf_q2

x180_wf_q3, x180_der_wf_q3 = np.array(
    drag_gaussian_pulse_waveforms(
        pi_amp_q3, pi_len, pi_sigma, drag_coef_q3, anharmonicity_q3, AC_stark_detuning_q3, sampling_rate=sampling_rate
    )
)
x180_I_wf_q3 = x180_wf_q3
x180_Q_wf_q3 = x180_der_wf_q3

x180_wf_q4, x180_der_wf_q4 = np.array(
    drag_gaussian_pulse_waveforms(
        pi_amp_q4, pi_len, pi_sigma, drag_coef_q4, anharmonicity_q4, AC_stark_detuning_q4, sampling_rate=sampling_rate
    )
)
x180_I_wf_q4 = x180_wf_q4
x180_Q_wf_q4 = x180_der_wf_q4

x180_wf_q5, x180_der_wf_q5 = np.array(
    drag_gaussian_pulse_waveforms(
        amplitude=pi_amp_q5,
        length=pi_len,
        sigma=pi_sigma,
        alpha=drag_coef_q5,
        anharmonicity=anharmonicity_q5,
        detuning=AC_stark_detuning_q5,
        sampling_rate=sampling_rate,
    )
)
x180_I_wf_q5 = x180_wf_q5
x180_Q_wf_q5 = x180_der_wf_q5

x180_wf_q6, x180_der_wf_q6 = np.array(
    drag_gaussian_pulse_waveforms(
        amplitude=pi_amp_q6,
        length=pi_len,
        sigma=pi_sigma,
        alpha=drag_coef_q6,
        anharmonicity=anharmonicity_q6,
        detuning=AC_stark_detuning_q6,
        sampling_rate=sampling_rate,
    )
)
x180_I_wf_q6 = x180_wf_q6
x180_Q_wf_q6 = x180_der_wf_q6

x180_wf_q7, x180_der_wf_q7 = np.array(
    drag_gaussian_pulse_waveforms(
        amplitude=pi_amp_q7,
        length=pi_len,
        sigma=pi_sigma,
        alpha=drag_coef_q7,
        anharmonicity=anharmonicity_q7,
        detuning=AC_stark_detuning_q7,
        sampling_rate=sampling_rate,
    )
)
x180_I_wf_q7 = x180_wf_q7
x180_Q_wf_q7 = x180_der_wf_q7

x180_wf_q8, x180_der_wf_q8 = np.array(
    drag_gaussian_pulse_waveforms(
        amplitude=pi_amp_q8,
        length=pi_len,
        sigma=pi_sigma,
        alpha=drag_coef_q8,
        anharmonicity=anharmonicity_q8,
        detuning=AC_stark_detuning_q8,
        sampling_rate=sampling_rate,
    )
)
x180_I_wf_q8 = x180_wf_q8
x180_Q_wf_q8 = x180_der_wf_q8

x180_wf_q9, x180_der_wf_q9 = np.array(
    drag_gaussian_pulse_waveforms(
        amplitude=pi_amp_q9,
        length=pi_len,
        sigma=pi_sigma,
        alpha=drag_coef_q9,
        anharmonicity=anharmonicity_q9,
        detuning=AC_stark_detuning_q9,
        sampling_rate=sampling_rate,
    )
)
x180_I_wf_q9 = x180_wf_q9
x180_Q_wf_q9 = x180_der_wf_q9

x180_wf_q10, x180_der_wf_q10 = np.array(
    drag_gaussian_pulse_waveforms(
        amplitude=pi_amp_q10,
        length=pi_len,
        sigma=pi_sigma,
        alpha=drag_coef_q10,
        anharmonicity=anharmonicity_q10,
        detuning=AC_stark_detuning_q10,
        sampling_rate=sampling_rate,
    )
)
x180_I_wf_q10 = x180_wf_q10
x180_Q_wf_q10 = x180_der_wf_q10

x180_wf_q11, x180_der_wf_q11 = np.array(
    drag_gaussian_pulse_waveforms(
        amplitude=pi_amp_q11,
        length=pi_len,
        sigma=pi_sigma,
        alpha=drag_coef_q11,
        anharmonicity=anharmonicity_q11,
        detuning=AC_stark_detuning_q11,
        sampling_rate=sampling_rate,
    )
)
x180_I_wf_q11 = x180_wf_q11
x180_Q_wf_q11 = x180_der_wf_q11

x180_wf_q12, x180_der_wf_q12 = np.array(
    drag_gaussian_pulse_waveforms(
        amplitude=pi_amp_q12,
        length=pi_len,
        sigma=pi_sigma,
        alpha=drag_coef_q12,
        anharmonicity=anharmonicity_q12,
        detuning=AC_stark_detuning_q12,
        sampling_rate=sampling_rate,
    )
)
x180_I_wf_q12 = x180_wf_q12
x180_Q_wf_q12 = x180_der_wf_q12

x180_wf_q13, x180_der_wf_q13 = np.array(
    drag_gaussian_pulse_waveforms(
        amplitude=pi_amp_q13,
        length=pi_len,
        sigma=pi_sigma,
        alpha=drag_coef_q13,
        anharmonicity=anharmonicity_q13,
        detuning=AC_stark_detuning_q13,
        sampling_rate=sampling_rate,
    )
)
x180_I_wf_q13 = x180_wf_q13
x180_Q_wf_q13 = x180_der_wf_q13

x180_wf_q14, x180_der_wf_q14 = np.array(
    drag_gaussian_pulse_waveforms(
        amplitude=pi_amp_q14,
        length=pi_len,
        sigma=pi_sigma,
        alpha=drag_coef_q14,
        anharmonicity=anharmonicity_q14,
        detuning=AC_stark_detuning_q14,
        sampling_rate=sampling_rate,
    )
)
x180_I_wf_q14 = x180_wf_q14
x180_Q_wf_q14 = x180_der_wf_q14

x180_wf_q15, x180_der_wf_q15 = np.array(
    drag_gaussian_pulse_waveforms(
        amplitude=pi_amp_q15,
        length=pi_len,
        sigma=pi_sigma,
        alpha=drag_coef_q15,
        anharmonicity=anharmonicity_q15,
        detuning=AC_stark_detuning_q15,
        sampling_rate=sampling_rate,
    )
)
x180_I_wf_q15 = x180_wf_q15
x180_Q_wf_q15 = x180_der_wf_q15

x180_wf_q16, x180_der_wf_q16 = np.array(
    drag_gaussian_pulse_waveforms(
        amplitude=pi_amp_q16,
        length=pi_len,
        sigma=pi_sigma,
        alpha=drag_coef_q16,
        anharmonicity=anharmonicity_q16,
        detuning=AC_stark_detuning_q16,
        sampling_rate=sampling_rate,
    )
)
x180_I_wf_q16 = x180_wf_q16
x180_Q_wf_q16 = x180_der_wf_q16

x180_wf_q17, x180_der_wf_q17 = np.array(
    drag_gaussian_pulse_waveforms(
        amplitude=pi_amp_q17,
        length=pi_len,
        sigma=pi_sigma,
        alpha=drag_coef_q17,
        anharmonicity=anharmonicity_q17,
        detuning=AC_stark_detuning_q17,
        sampling_rate=sampling_rate,
    )
)
x180_I_wf_q17 = x180_wf_q17
x180_Q_wf_q17 = x180_der_wf_q17

x180_wf_q18, x180_der_wf_q18 = np.array(
    drag_gaussian_pulse_waveforms(
        amplitude=pi_amp_q18,
        length=pi_len,
        sigma=pi_sigma,
        alpha=drag_coef_q18,
        anharmonicity=anharmonicity_q18,
        detuning=AC_stark_detuning_q18,
        sampling_rate=sampling_rate,
    )
)
x180_I_wf_q18 = x180_wf_q18
x180_Q_wf_q18 = x180_der_wf_q18

x180_wf_q19, x180_der_wf_q19 = np.array(
    drag_gaussian_pulse_waveforms(
        amplitude=pi_amp_q19,
        length=pi_len,
        sigma=pi_sigma,
        alpha=drag_coef_q19,
        anharmonicity=anharmonicity_q19,
        detuning=AC_stark_detuning_q19,
        sampling_rate=sampling_rate,
    )
)
x180_I_wf_q19 = x180_wf_q19
x180_Q_wf_q19 = x180_der_wf_q19

x180_wf_q20, x180_der_wf_q20 = np.array(
    drag_gaussian_pulse_waveforms(
        amplitude=pi_amp_q20,
        length=pi_len,
        sigma=pi_sigma,
        alpha=drag_coef_q20,
        anharmonicity=anharmonicity_q20,
        detuning=AC_stark_detuning_q20,
        sampling_rate=sampling_rate,
    )
)
x180_I_wf_q20 = x180_wf_q20
x180_Q_wf_q20 = x180_der_wf_q20

x180_wf_q_C6, x180_der_wf_q_C6 = np.array(
    drag_gaussian_pulse_waveforms(
        amplitude=pi_amp_q_C6,
        length=pi_len,
        sigma=pi_sigma,
        alpha=drag_coef_q_C6,
        anharmonicity=anharmonicity_q_C6,
        detuning=AC_stark_detuning_q_C6,
        sampling_rate=sampling_rate,
    )
)
x180_I_wf_q_C6 = x180_wf_q_C6
x180_Q_wf_q_C6 = x180_der_wf_q_C6


# No DRAG when alpha=0, it's just a gaussian.

x90_wf_q1, x90_der_wf_q1 = np.array(
    drag_gaussian_pulse_waveforms(
        pi_amp_q1 / 2,
        pi_len,
        pi_sigma,
        drag_coef_q1,
        anharmonicity_q1,
        AC_stark_detuning_q1,
        sampling_rate=sampling_rate,
    )
)
x90_I_wf_q1 = x90_wf_q1
x90_Q_wf_q1 = x90_der_wf_q1
x90_wf_q2, x90_der_wf_q2 = np.array(
    drag_gaussian_pulse_waveforms(
        pi_amp_q2 / 2,
        pi_len,
        pi_sigma,
        drag_coef_q2,
        anharmonicity_q2,
        AC_stark_detuning_q2,
        sampling_rate=sampling_rate,
    )
)
x90_I_wf_q2 = x90_wf_q2
x90_Q_wf_q2 = x90_der_wf_q2
x90_wf_q3, x90_der_wf_q3 = np.array(
    drag_gaussian_pulse_waveforms(
        pi_amp_q3 / 2,
        pi_len,
        pi_sigma,
        drag_coef_q3,
        anharmonicity_q3,
        AC_stark_detuning_q3,
        sampling_rate=sampling_rate,
    )
)
x90_I_wf_q3 = x90_wf_q3
x90_Q_wf_q3 = x90_der_wf_q3
x90_wf_q4, x90_der_wf_q4 = np.array(
    drag_gaussian_pulse_waveforms(
        pi_amp_q4 / 2,
        pi_len,
        pi_sigma,
        drag_coef_q4,
        anharmonicity_q4,
        AC_stark_detuning_q4,
        sampling_rate=sampling_rate,
    )
)
x90_I_wf_q4 = x90_wf_q4
x90_Q_wf_q4 = x90_der_wf_q4

x90_wf_q5, x90_der_wf_q5 = np.array(
    drag_gaussian_pulse_waveforms(
        pi_amp_q5 / 2,
        pi_len,
        pi_sigma,
        drag_coef_q5,
        anharmonicity_q5,
        AC_stark_detuning_q5,
        sampling_rate=sampling_rate,
    )
)
x90_I_wf_q5 = x90_wf_q5
x90_Q_wf_q5 = x90_der_wf_q5

x90_wf_q6, x90_der_wf_q6 = np.array(
    drag_gaussian_pulse_waveforms(
        pi_amp_q6 / 2,
        pi_len,
        pi_sigma,
        drag_coef_q6,
        anharmonicity_q6,
        AC_stark_detuning_q6,
        sampling_rate=sampling_rate,
    )
)
x90_I_wf_q6 = x90_wf_q6
x90_Q_wf_q6 = x90_der_wf_q6

x90_wf_q7, x90_der_wf_q7 = np.array(
    drag_gaussian_pulse_waveforms(
        pi_amp_q7 / 2,
        pi_len,
        pi_sigma,
        drag_coef_q7,
        anharmonicity_q7,
        AC_stark_detuning_q7,
        sampling_rate=sampling_rate,
    )
)
x90_I_wf_q7 = x90_wf_q7
x90_Q_wf_q7 = x90_der_wf_q7

x90_wf_q8, x90_der_wf_q8 = np.array(
    drag_gaussian_pulse_waveforms(
        pi_amp_q8 / 2,
        pi_len,
        pi_sigma,
        drag_coef_q8,
        anharmonicity_q8,
        AC_stark_detuning_q8,
        sampling_rate=sampling_rate,
    )
)
x90_I_wf_q8 = x90_wf_q8
x90_Q_wf_q8 = x90_der_wf_q8

x90_wf_q9, x90_der_wf_q9 = np.array(
    drag_gaussian_pulse_waveforms(
        pi_amp_q9 / 2,
        pi_len,
        pi_sigma,
        drag_coef_q9,
        anharmonicity_q9,
        AC_stark_detuning_q9,
        sampling_rate=sampling_rate,
    )
)
x90_I_wf_q9 = x90_wf_q9
x90_Q_wf_q9 = x90_der_wf_q9

x90_wf_q10, x90_der_wf_q10 = np.array(
    drag_gaussian_pulse_waveforms(
        pi_amp_q10 / 2,
        pi_len,
        pi_sigma,
        drag_coef_q10,
        anharmonicity_q10,
        AC_stark_detuning_q10,
        sampling_rate=sampling_rate,
    )
)
x90_I_wf_q10 = x90_wf_q10
x90_Q_wf_q10 = x90_der_wf_q10

x90_wf_q11, x90_der_wf_q11 = np.array(
    drag_gaussian_pulse_waveforms(
        pi_amp_q11 / 2,
        pi_len,
        pi_sigma,
        drag_coef_q11,
        anharmonicity_q11,
        AC_stark_detuning_q11,
        sampling_rate=sampling_rate,
    )
)
x90_I_wf_q11 = x90_wf_q11
x90_Q_wf_q11 = x90_der_wf_q11

x90_wf_q12, x90_der_wf_q12 = np.array(
    drag_gaussian_pulse_waveforms(
        pi_amp_q12 / 2,
        pi_len,
        pi_sigma,
        drag_coef_q12,
        anharmonicity_q12,
        AC_stark_detuning_q12,
        sampling_rate=sampling_rate,
    )
)
x90_I_wf_q12 = x90_wf_q12
x90_Q_wf_q12 = x90_der_wf_q12

x90_wf_q13, x90_der_wf_q13 = np.array(
    drag_gaussian_pulse_waveforms(
        pi_amp_q13 / 2,
        pi_len,
        pi_sigma,
        drag_coef_q13,
        anharmonicity_q13,
        AC_stark_detuning_q13,
        sampling_rate=sampling_rate,
    )
)
x90_I_wf_q13 = x90_wf_q13
x90_Q_wf_q13 = x90_der_wf_q13

x90_wf_q14, x90_der_wf_q14 = np.array(
    drag_gaussian_pulse_waveforms(
        pi_amp_q14 / 2,
        pi_len,
        pi_sigma,
        drag_coef_q14,
        anharmonicity_q14,
        AC_stark_detuning_q14,
        sampling_rate=sampling_rate,
    )
)
x90_I_wf_q14 = x90_wf_q14
x90_Q_wf_q14 = x90_der_wf_q14

x90_wf_q15, x90_der_wf_q15 = np.array(
    drag_gaussian_pulse_waveforms(
        pi_amp_q15 / 2,
        pi_len,
        pi_sigma,
        drag_coef_q15,
        anharmonicity_q15,
        AC_stark_detuning_q15,
        sampling_rate=sampling_rate,
    )
)
x90_I_wf_q15 = x90_wf_q15
x90_Q_wf_q15 = x90_der_wf_q15

x90_wf_q16, x90_der_wf_q16 = np.array(
    drag_gaussian_pulse_waveforms(
        pi_amp_q16 / 2,
        pi_len,
        pi_sigma,
        drag_coef_q16,
        anharmonicity_q16,
        AC_stark_detuning_q16,
        sampling_rate=sampling_rate,
    )
)
x90_I_wf_q16 = x90_wf_q16
x90_Q_wf_q16 = x90_der_wf_q16

x90_wf_q17, x90_der_wf_q17 = np.array(
    drag_gaussian_pulse_waveforms(
        pi_amp_q17 / 2,
        pi_len,
        pi_sigma,
        drag_coef_q17,
        anharmonicity_q17,
        AC_stark_detuning_q17,
        sampling_rate=sampling_rate,
    )
)
x90_I_wf_q17 = x90_wf_q17
x90_Q_wf_q17 = x90_der_wf_q17

x90_wf_q18, x90_der_wf_q18 = np.array(
    drag_gaussian_pulse_waveforms(
        pi_amp_q18 / 2,
        pi_len,
        pi_sigma,
        drag_coef_q18,
        anharmonicity_q18,
        AC_stark_detuning_q18,
        sampling_rate=sampling_rate,
    )
)
x90_I_wf_q18 = x90_wf_q18
x90_Q_wf_q18 = x90_der_wf_q18

x90_wf_q19, x90_der_wf_q19 = np.array(
    drag_gaussian_pulse_waveforms(
        pi_amp_q19 / 2,
        pi_len,
        pi_sigma,
        drag_coef_q19,
        anharmonicity_q19,
        AC_stark_detuning_q19,
        sampling_rate=sampling_rate,
    )
)
x90_I_wf_q19 = x90_wf_q19
x90_Q_wf_q19 = x90_der_wf_q19

x90_wf_q20, x90_der_wf_q20 = np.array(
    drag_gaussian_pulse_waveforms(
        pi_amp_q20 / 2,
        pi_len,
        pi_sigma,
        drag_coef_q20,
        anharmonicity_q20,
        AC_stark_detuning_q20,
        sampling_rate=sampling_rate,
    )
)
x90_I_wf_q20 = x90_wf_q20
x90_Q_wf_q20 = x90_der_wf_q20

x90_wf_q_C6, x90_der_wf_q_C6 = np.array(
    drag_gaussian_pulse_waveforms(
        pi_amp_q_C6 / 2,
        pi_len,
        pi_sigma,
        drag_coef_q_C6,
        anharmonicity_q_C6,
        AC_stark_detuning_q_C6,
        sampling_rate=sampling_rate,
    )
)
x90_I_wf_q_C6 = x90_wf_q_C6
x90_Q_wf_q_C6 = x90_der_wf_q_C6





# No DRAG when alpha=0, it's just a gaussian.

minus_x90_wf_q1, minus_x90_der_wf_q1 = np.array(
    drag_gaussian_pulse_waveforms(
        -pi_amp_q1 / 2,
        pi_len,
        pi_sigma,
        drag_coef_q1,
        anharmonicity_q1,
        AC_stark_detuning_q1,
        sampling_rate=sampling_rate,
    )
)
minus_x90_I_wf_q1 = minus_x90_wf_q1
minus_x90_Q_wf_q1 = minus_x90_der_wf_q1
minus_x90_wf_q2, minus_x90_der_wf_q2 = np.array(
    drag_gaussian_pulse_waveforms(
        -pi_amp_q2 / 2,
        pi_len,
        pi_sigma,
        drag_coef_q2,
        anharmonicity_q2,
        AC_stark_detuning_q2,
        sampling_rate=sampling_rate,
    )
)
minus_x90_I_wf_q2 = minus_x90_wf_q2
minus_x90_Q_wf_q2 = minus_x90_der_wf_q2
minus_x90_wf_q3, minus_x90_der_wf_q3 = np.array(
    drag_gaussian_pulse_waveforms(
        -pi_amp_q3 / 2,
        pi_len,
        pi_sigma,
        drag_coef_q3,
        anharmonicity_q3,
        AC_stark_detuning_q3,
        sampling_rate=sampling_rate,
    )
)
minus_x90_I_wf_q3 = minus_x90_wf_q3
minus_x90_Q_wf_q3 = minus_x90_der_wf_q3
minus_x90_wf_q4, minus_x90_der_wf_q4 = np.array(
    drag_gaussian_pulse_waveforms(
        -pi_amp_q4 / 2,
        pi_len,
        pi_sigma,
        drag_coef_q4,
        anharmonicity_q4,
        AC_stark_detuning_q4,
        sampling_rate=sampling_rate,
    )
)
minus_x90_I_wf_q4 = minus_x90_wf_q4
minus_x90_Q_wf_q4 = minus_x90_der_wf_q4

minus_x90_wf_q5, minus_x90_der_wf_q5 = np.array(
    drag_gaussian_pulse_waveforms(
        -pi_amp_q5 / 2,
        pi_len,
        pi_sigma,
        drag_coef_q5,
        anharmonicity_q5,
        AC_stark_detuning_q5,
        sampling_rate=sampling_rate,
    )
)
minus_x90_I_wf_q5 = minus_x90_wf_q5
minus_x90_Q_wf_q5 = minus_x90_der_wf_q5

minus_x90_wf_q6, minus_x90_der_wf_q6 = np.array(
    drag_gaussian_pulse_waveforms(
        -pi_amp_q6 / 2,
        pi_len,
        pi_sigma,
        drag_coef_q6,
        anharmonicity_q6,
        AC_stark_detuning_q6,
        sampling_rate=sampling_rate,
    )
)
minus_x90_I_wf_q6 = minus_x90_wf_q6
minus_x90_Q_wf_q6 = minus_x90_der_wf_q6

minus_x90_wf_q7, minus_x90_der_wf_q7 = np.array(
    drag_gaussian_pulse_waveforms(
        -pi_amp_q7 / 2,
        pi_len,
        pi_sigma,
        drag_coef_q7,
        anharmonicity_q7,
        AC_stark_detuning_q7,
        sampling_rate=sampling_rate,
    )
)
minus_x90_I_wf_q7 = minus_x90_wf_q7
minus_x90_Q_wf_q7 = minus_x90_der_wf_q7

minus_x90_wf_q8, minus_x90_der_wf_q8 = np.array(
    drag_gaussian_pulse_waveforms(
        -pi_amp_q8 / 2,
        pi_len,
        pi_sigma,
        drag_coef_q8,
        anharmonicity_q8,
        AC_stark_detuning_q8,
        sampling_rate=sampling_rate,
    )
)
minus_x90_I_wf_q8 = minus_x90_wf_q8
minus_x90_Q_wf_q8 = minus_x90_der_wf_q8

minus_x90_wf_q9, minus_x90_der_wf_q9 = np.array(
    drag_gaussian_pulse_waveforms(
        -pi_amp_q9 / 2,
        pi_len,
        pi_sigma,
        drag_coef_q9,
        anharmonicity_q9,
        AC_stark_detuning_q9,
        sampling_rate=sampling_rate,
    )
)
minus_x90_I_wf_q9 = minus_x90_wf_q9
minus_x90_Q_wf_q9 = minus_x90_der_wf_q9

minus_x90_wf_q10, minus_x90_der_wf_q10 = np.array(
    drag_gaussian_pulse_waveforms(
        -pi_amp_q10 / 2,
        pi_len,
        pi_sigma,
        drag_coef_q10,
        anharmonicity_q10,
        AC_stark_detuning_q10,
        sampling_rate=sampling_rate,
    )
)
minus_x90_I_wf_q10 = minus_x90_wf_q10
minus_x90_Q_wf_q10 = minus_x90_der_wf_q10

minus_x90_wf_q11, minus_x90_der_wf_q11 = np.array(
    drag_gaussian_pulse_waveforms(
        -pi_amp_q11 / 2,
        pi_len,
        pi_sigma,
        drag_coef_q11,
        anharmonicity_q11,
        AC_stark_detuning_q11,
        sampling_rate=sampling_rate,
    )
)
minus_x90_I_wf_q11 = minus_x90_wf_q11
minus_x90_Q_wf_q11 = minus_x90_der_wf_q11

minus_x90_wf_q12, minus_x90_der_wf_q12 = np.array(
    drag_gaussian_pulse_waveforms(
        -pi_amp_q12 / 2,
        pi_len,
        pi_sigma,
        drag_coef_q12,
        anharmonicity_q12,
        AC_stark_detuning_q12,
        sampling_rate=sampling_rate,
    )
)
minus_x90_I_wf_q12 = minus_x90_wf_q12
minus_x90_Q_wf_q12 = minus_x90_der_wf_q12

minus_x90_wf_q13, minus_x90_der_wf_q13 = np.array(
    drag_gaussian_pulse_waveforms(
        -pi_amp_q13 / 2,
        pi_len,
        pi_sigma,
        drag_coef_q13,
        anharmonicity_q13,
        AC_stark_detuning_q13,
        sampling_rate=sampling_rate,
    )
)
minus_x90_I_wf_q13 = minus_x90_wf_q13
minus_x90_Q_wf_q13 = minus_x90_der_wf_q13

minus_x90_wf_q14, minus_x90_der_wf_q14 = np.array(
    drag_gaussian_pulse_waveforms(
        -pi_amp_q14 / 2,
        pi_len,
        pi_sigma,
        drag_coef_q14,
        anharmonicity_q14,
        AC_stark_detuning_q14,
        sampling_rate=sampling_rate,
    )
)
minus_x90_I_wf_q14 = minus_x90_wf_q14
minus_x90_Q_wf_q14 = minus_x90_der_wf_q14

minus_x90_wf_q15, minus_x90_der_wf_q15 = np.array(
    drag_gaussian_pulse_waveforms(
        -pi_amp_q15 / 2,
        pi_len,
        pi_sigma,
        drag_coef_q15,
        anharmonicity_q15,
        AC_stark_detuning_q15,
        sampling_rate=sampling_rate,
    )
)
minus_x90_I_wf_q15 = minus_x90_wf_q15
minus_x90_Q_wf_q15 = minus_x90_der_wf_q15

minus_x90_wf_q16, minus_x90_der_wf_q16 = np.array(
    drag_gaussian_pulse_waveforms(
        -pi_amp_q16 / 2,
        pi_len,
        pi_sigma,
        drag_coef_q16,
        anharmonicity_q16,
        AC_stark_detuning_q16,
        sampling_rate=sampling_rate,
    )
)
minus_x90_I_wf_q16 = minus_x90_wf_q16
minus_x90_Q_wf_q16 = minus_x90_der_wf_q16

minus_x90_wf_q17, minus_x90_der_wf_q17 = np.array(
    drag_gaussian_pulse_waveforms(
        -pi_amp_q17 / 2,
        pi_len,
        pi_sigma,
        drag_coef_q17,
        anharmonicity_q17,
        AC_stark_detuning_q17,
        sampling_rate=sampling_rate,
    )
)
minus_x90_I_wf_q17 = minus_x90_wf_q17
minus_x90_Q_wf_q17 = minus_x90_der_wf_q17

minus_x90_wf_q18, minus_x90_der_wf_q18 = np.array(
    drag_gaussian_pulse_waveforms(
        -pi_amp_q18 / 2,
        pi_len,
        pi_sigma,
        drag_coef_q18,
        anharmonicity_q18,
        AC_stark_detuning_q18,
        sampling_rate=sampling_rate,
    )
)
minus_x90_I_wf_q18 = minus_x90_wf_q18
minus_x90_Q_wf_q18 = minus_x90_der_wf_q18

minus_x90_wf_q19, minus_x90_der_wf_q19 = np.array(
    drag_gaussian_pulse_waveforms(
        -pi_amp_q19 / 2,
        pi_len,
        pi_sigma,
        drag_coef_q19,
        anharmonicity_q19,
        AC_stark_detuning_q19,
        sampling_rate=sampling_rate,
    )
)
minus_x90_I_wf_q19 = minus_x90_wf_q19
minus_x90_Q_wf_q19 = minus_x90_der_wf_q19

minus_x90_wf_q20, minus_x90_der_wf_q20 = np.array(
    drag_gaussian_pulse_waveforms(
        -pi_amp_q20 / 2,
        pi_len,
        pi_sigma,
        drag_coef_q20,
        anharmonicity_q20,
        AC_stark_detuning_q20,
        sampling_rate=sampling_rate,
    )
)
minus_x90_I_wf_q20 = minus_x90_wf_q20
minus_x90_Q_wf_q20 = minus_x90_der_wf_q20

minus_x90_wf_q_C6, minus_x90_der_wf_q_C6 = np.array(
    drag_gaussian_pulse_waveforms(
        -pi_amp_q_C6 / 2,
        pi_len,
        pi_sigma,
        drag_coef_q_C6,
        anharmonicity_q_C6,
        AC_stark_detuning_q_C6,
        sampling_rate=sampling_rate,
    )
)
minus_x90_I_wf_q_C6 = minus_x90_wf_q_C6
minus_x90_Q_wf_q_C6 = minus_x90_der_wf_q_C6






# No DRAG when alpha=0, it's just a gaussian.

y180_wf_q1, y180_der_wf_q1 = np.array(
    drag_gaussian_pulse_waveforms(
        pi_amp_q1, pi_len, pi_sigma, drag_coef_q1, anharmonicity_q1, AC_stark_detuning_q1, sampling_rate=sampling_rate
    )
)
y180_I_wf_q1 = (-1) * y180_der_wf_q1
y180_Q_wf_q1 = y180_wf_q1
y180_wf_q2, y180_der_wf_q2 = np.array(
    drag_gaussian_pulse_waveforms(
        pi_amp_q2, pi_len, pi_sigma, drag_coef_q2, anharmonicity_q2, AC_stark_detuning_q2, sampling_rate=sampling_rate
    )
)
y180_I_wf_q2 = (-1) * y180_der_wf_q2
y180_Q_wf_q2 = y180_wf_q2
y180_wf_q3, y180_der_wf_q3 = np.array(
    drag_gaussian_pulse_waveforms(
        pi_amp_q3, pi_len, pi_sigma, drag_coef_q3, anharmonicity_q3, AC_stark_detuning_q3, sampling_rate=sampling_rate
    )
)
y180_I_wf_q3 = (-1) * y180_der_wf_q3
y180_Q_wf_q3 = y180_wf_q3
y180_wf_q4, y180_der_wf_q4 = np.array(
    drag_gaussian_pulse_waveforms(
        pi_amp_q4, pi_len, pi_sigma, drag_coef_q4, anharmonicity_q4, AC_stark_detuning_q4, sampling_rate=sampling_rate
    )
)
y180_I_wf_q4 = (-1) * y180_der_wf_q4
y180_Q_wf_q4 = y180_wf_q4

y180_wf_q5, y180_der_wf_q5 = np.array(
    drag_gaussian_pulse_waveforms(
        pi_amp_q5, pi_len, pi_sigma, drag_coef_q5, anharmonicity_q5, AC_stark_detuning_q5, sampling_rate=sampling_rate
    )
)
y180_I_wf_q5 = (-1) * y180_der_wf_q5
y180_Q_wf_q5 = y180_wf_q5

y180_wf_q6, y180_der_wf_q6 = np.array(
    drag_gaussian_pulse_waveforms(
        pi_amp_q6, pi_len, pi_sigma, drag_coef_q6, anharmonicity_q6, AC_stark_detuning_q6, sampling_rate=sampling_rate
    )
)
y180_I_wf_q6 = (-1) * y180_der_wf_q6
y180_Q_wf_q6 = y180_wf_q6

y180_wf_q7, y180_der_wf_q7 = np.array(
    drag_gaussian_pulse_waveforms(
        pi_amp_q7, pi_len, pi_sigma, drag_coef_q7, anharmonicity_q7, AC_stark_detuning_q7, sampling_rate=sampling_rate
    )
)
y180_I_wf_q7 = (-1) * y180_der_wf_q7
y180_Q_wf_q7 = y180_wf_q7

y180_wf_q8, y180_der_wf_q8 = np.array(
    drag_gaussian_pulse_waveforms(
        pi_amp_q8, pi_len, pi_sigma, drag_coef_q8, anharmonicity_q8, AC_stark_detuning_q8, sampling_rate=sampling_rate
    )
)
y180_I_wf_q8 = (-1) * y180_der_wf_q8
y180_Q_wf_q8 = y180_wf_q8

y180_wf_q9, y180_der_wf_q9 = np.array(
    drag_gaussian_pulse_waveforms(
        pi_amp_q9, pi_len, pi_sigma, drag_coef_q9, anharmonicity_q9, AC_stark_detuning_q9, sampling_rate=sampling_rate
    )
)
y180_I_wf_q9 = (-1) * y180_der_wf_q9
y180_Q_wf_q9 = y180_wf_q9

y180_wf_q10, y180_der_wf_q10 = np.array(
    drag_gaussian_pulse_waveforms(
        pi_amp_q10, pi_len, pi_sigma, drag_coef_q10, anharmonicity_q10, AC_stark_detuning_q10, sampling_rate=sampling_rate
    )
)
y180_I_wf_q10 = (-1) * y180_der_wf_q10
y180_Q_wf_q10 = y180_wf_q10

y180_wf_q11, y180_der_wf_q11 = np.array(
    drag_gaussian_pulse_waveforms(
        pi_amp_q11, pi_len, pi_sigma, drag_coef_q11, anharmonicity_q11, AC_stark_detuning_q11, sampling_rate=sampling_rate
    )
)
y180_I_wf_q11 = (-1) * y180_der_wf_q11
y180_Q_wf_q11 = y180_wf_q11

y180_wf_q12, y180_der_wf_q12 = np.array(
    drag_gaussian_pulse_waveforms(
        pi_amp_q12, pi_len, pi_sigma, drag_coef_q12, anharmonicity_q12, AC_stark_detuning_q12, sampling_rate=sampling_rate
    )
)
y180_I_wf_q12 = (-1) * y180_der_wf_q12
y180_Q_wf_q12 = y180_wf_q12

y180_wf_q13, y180_der_wf_q13 = np.array(
    drag_gaussian_pulse_waveforms(
        pi_amp_q13, pi_len, pi_sigma, drag_coef_q13, anharmonicity_q13, AC_stark_detuning_q13, sampling_rate=sampling_rate
    )
)
y180_I_wf_q13 = (-1) * y180_der_wf_q13
y180_Q_wf_q13 = y180_wf_q13

y180_wf_q14, y180_der_wf_q14 = np.array(
    drag_gaussian_pulse_waveforms(
        pi_amp_q14, pi_len, pi_sigma, drag_coef_q14, anharmonicity_q14, AC_stark_detuning_q14, sampling_rate=sampling_rate
    )
)
y180_I_wf_q14 = (-1) * y180_der_wf_q14
y180_Q_wf_q14 = y180_wf_q14

y180_wf_q15, y180_der_wf_q15 = np.array(
    drag_gaussian_pulse_waveforms(
        pi_amp_q15, pi_len, pi_sigma, drag_coef_q15, anharmonicity_q15, AC_stark_detuning_q15, sampling_rate=sampling_rate
    )
)
y180_I_wf_q15 = (-1) * y180_der_wf_q15
y180_Q_wf_q15 = y180_wf_q15

y180_wf_q16, y180_der_wf_q16 = np.array(
    drag_gaussian_pulse_waveforms(
        pi_amp_q16, pi_len, pi_sigma, drag_coef_q16, anharmonicity_q16, AC_stark_detuning_q16, sampling_rate=sampling_rate
    )
)
y180_I_wf_q16 = (-1) * y180_der_wf_q16
y180_Q_wf_q16 = y180_wf_q16

y180_wf_q17, y180_der_wf_q17 = np.array(
    drag_gaussian_pulse_waveforms(
        pi_amp_q17, pi_len, pi_sigma, drag_coef_q17, anharmonicity_q17, AC_stark_detuning_q17, sampling_rate=sampling_rate
    )
)
y180_I_wf_q17 = (-1) * y180_der_wf_q17
y180_Q_wf_q17 = y180_wf_q17

y180_wf_q18, y180_der_wf_q18 = np.array(
    drag_gaussian_pulse_waveforms(
        pi_amp_q18, pi_len, pi_sigma, drag_coef_q18, anharmonicity_q18, AC_stark_detuning_q18, sampling_rate=sampling_rate
    )
)
y180_I_wf_q18 = (-1) * y180_der_wf_q18
y180_Q_wf_q18 = y180_wf_q18

y180_wf_q19, y180_der_wf_q19 = np.array(
    drag_gaussian_pulse_waveforms(
        pi_amp_q19, pi_len, pi_sigma, drag_coef_q19, anharmonicity_q19, AC_stark_detuning_q19, sampling_rate=sampling_rate
    )
)
y180_I_wf_q19 = (-1) * y180_der_wf_q19
y180_Q_wf_q19 = y180_wf_q19

y180_wf_q20, y180_der_wf_q20 = np.array(
    drag_gaussian_pulse_waveforms(
        pi_amp_q20, pi_len, pi_sigma, drag_coef_q20, anharmonicity_q20, AC_stark_detuning_q20, sampling_rate=sampling_rate
    )
)
y180_I_wf_q20 = (-1) * y180_der_wf_q20
y180_Q_wf_q20 = y180_wf_q20

y180_wf_q_C6, y180_der_wf_q_C6 = np.array(
    drag_gaussian_pulse_waveforms(
        pi_amp_q_C6, pi_len, pi_sigma, drag_coef_q_C6, anharmonicity_q_C6, AC_stark_detuning_q_C6, sampling_rate=sampling_rate
    )
)
y180_I_wf_q_C6 = (-1) * y180_der_wf_q_C6
y180_Q_wf_q_C6 = y180_wf_q_C6




# No DRAG when alpha=0, it's just a gaussian.

y90_wf_q1, y90_der_wf_q1 = np.array(
    drag_gaussian_pulse_waveforms(
        pi_amp_q1 / 2,
        pi_len,
        pi_sigma,
        drag_coef_q1,
        anharmonicity_q1,
        AC_stark_detuning_q1,
        sampling_rate=sampling_rate,
    )
)
y90_I_wf_q1 = (-1) * y90_der_wf_q1
y90_Q_wf_q1 = y90_wf_q1
y90_wf_q2, y90_der_wf_q2 = np.array(
    drag_gaussian_pulse_waveforms(
        pi_amp_q2 / 2,
        pi_len,
        pi_sigma,
        drag_coef_q2,
        anharmonicity_q2,
        AC_stark_detuning_q2,
        sampling_rate=sampling_rate,
    )
)
y90_I_wf_q2 = (-1) * y90_der_wf_q2
y90_Q_wf_q2 = y90_wf_q2

y90_wf_q3, y90_der_wf_q3 = np.array(
    drag_gaussian_pulse_waveforms(
        pi_amp_q3 / 2,
        pi_len,
        pi_sigma,
        drag_coef_q3,
        anharmonicity_q3,
        AC_stark_detuning_q3,
        sampling_rate=sampling_rate,
    )
)
y90_I_wf_q3 = (-1) * y90_der_wf_q3
y90_Q_wf_q3 = y90_wf_q3

y90_wf_q4, y90_der_wf_q4 = np.array(
    drag_gaussian_pulse_waveforms(
        pi_amp_q4 / 2,
        pi_len,
        pi_sigma,
        drag_coef_q4,
        anharmonicity_q4,
        AC_stark_detuning_q4,
        sampling_rate=sampling_rate,
    )
)
y90_I_wf_q4 = (-1) * y90_der_wf_q4
y90_Q_wf_q4 = y90_wf_q4

y90_wf_q5, y90_der_wf_q5 = np.array(
    drag_gaussian_pulse_waveforms(
        pi_amp_q5 / 2,
        pi_len,
        pi_sigma,
        drag_coef_q5,
        anharmonicity_q5,
        AC_stark_detuning_q5,
        sampling_rate=sampling_rate,
    )
)
y90_I_wf_q5 = (-1) * y90_der_wf_q5
y90_Q_wf_q5 = y90_wf_q5

y90_wf_q6, y90_der_wf_q6 = np.array(
    drag_gaussian_pulse_waveforms(
        pi_amp_q6 / 2,
        pi_len,
        pi_sigma,
        drag_coef_q6,
        anharmonicity_q6,
        AC_stark_detuning_q6,
        sampling_rate=sampling_rate,
    )
)
y90_I_wf_q6 = (-1) * y90_der_wf_q6
y90_Q_wf_q6 = y90_wf_q6

y90_wf_q7, y90_der_wf_q7 = np.array(
    drag_gaussian_pulse_waveforms(
        pi_amp_q7 / 2,
        pi_len,
        pi_sigma,
        drag_coef_q7,
        anharmonicity_q7,
        AC_stark_detuning_q7,
        sampling_rate=sampling_rate,
    )
)
y90_I_wf_q7 = (-1) * y90_der_wf_q7
y90_Q_wf_q7 = y90_wf_q7

y90_wf_q8, y90_der_wf_q8 = np.array(
    drag_gaussian_pulse_waveforms(
        pi_amp_q8 / 2,
        pi_len,
        pi_sigma,
        drag_coef_q8,
        anharmonicity_q8,
        AC_stark_detuning_q8,
        sampling_rate=sampling_rate,
    )
)
y90_I_wf_q8 = (-1) * y90_der_wf_q8
y90_Q_wf_q8 = y90_wf_q8

y90_wf_q9, y90_der_wf_q9 = np.array(
    drag_gaussian_pulse_waveforms(
        pi_amp_q9 / 2,
        pi_len,
        pi_sigma,
        drag_coef_q9,
        anharmonicity_q9,
        AC_stark_detuning_q9,
        sampling_rate=sampling_rate,
    )
)
y90_I_wf_q9 = (-1) * y90_der_wf_q9
y90_Q_wf_q9 = y90_wf_q9

y90_wf_q10, y90_der_wf_q10 = np.array(
    drag_gaussian_pulse_waveforms(
        pi_amp_q10 / 2,
        pi_len,
        pi_sigma,
        drag_coef_q10,
        anharmonicity_q10,
        AC_stark_detuning_q10,
        sampling_rate=sampling_rate,
    )
)
y90_I_wf_q10 = (-1) * y90_der_wf_q10
y90_Q_wf_q10 = y90_wf_q10

y90_wf_q11, y90_der_wf_q11 = np.array(
    drag_gaussian_pulse_waveforms(
        pi_amp_q11 / 2,
        pi_len,
        pi_sigma,
        drag_coef_q11,
        anharmonicity_q11,
        AC_stark_detuning_q11,
        sampling_rate=sampling_rate,
    )
)
y90_I_wf_q11 = (-1) * y90_der_wf_q11
y90_Q_wf_q11 = y90_wf_q11

y90_wf_q12, y90_der_wf_q12 = np.array(
    drag_gaussian_pulse_waveforms(
        pi_amp_q12 / 2,
        pi_len,
        pi_sigma,
        drag_coef_q12,
        anharmonicity_q12,
        AC_stark_detuning_q12,
        sampling_rate=sampling_rate,
    )
)
y90_I_wf_q12 = (-1) * y90_der_wf_q12
y90_Q_wf_q12 = y90_wf_q12

y90_wf_q13, y90_der_wf_q13 = np.array(
    drag_gaussian_pulse_waveforms(
        pi_amp_q13 / 2,
        pi_len,
        pi_sigma,
        drag_coef_q13,
        anharmonicity_q13,
        AC_stark_detuning_q13,
        sampling_rate=sampling_rate,
    )
)
y90_I_wf_q13 = (-1) * y90_der_wf_q13
y90_Q_wf_q13 = y90_wf_q13

y90_wf_q14, y90_der_wf_q14 = np.array(
    drag_gaussian_pulse_waveforms(
        pi_amp_q14 / 2,
        pi_len,
        pi_sigma,
        drag_coef_q14,
        anharmonicity_q14,
        AC_stark_detuning_q14,
        sampling_rate=sampling_rate,
    )
)
y90_I_wf_q14 = (-1) * y90_der_wf_q14
y90_Q_wf_q14 = y90_wf_q14

y90_wf_q15, y90_der_wf_q15 = np.array(
    drag_gaussian_pulse_waveforms(
        pi_amp_q15 / 2,
        pi_len,
        pi_sigma,
        drag_coef_q15,
        anharmonicity_q15,
        AC_stark_detuning_q15,
        sampling_rate=sampling_rate,
    )
)
y90_I_wf_q15 = (-1) * y90_der_wf_q15
y90_Q_wf_q15 = y90_wf_q15

y90_wf_q16, y90_der_wf_q16 = np.array(
    drag_gaussian_pulse_waveforms(
        pi_amp_q16 / 2,
        pi_len,
        pi_sigma,
        drag_coef_q16,
        anharmonicity_q16,
        AC_stark_detuning_q16,
        sampling_rate=sampling_rate,
    )
)
y90_I_wf_q16 = (-1) * y90_der_wf_q16
y90_Q_wf_q16 = y90_wf_q16

y90_wf_q17, y90_der_wf_q17 = np.array(
    drag_gaussian_pulse_waveforms(
        pi_amp_q17 / 2,
        pi_len,
        pi_sigma,
        drag_coef_q17,
        anharmonicity_q17,
        AC_stark_detuning_q17,
        sampling_rate=sampling_rate,
    )
)
y90_I_wf_q17 = (-1) * y90_der_wf_q17
y90_Q_wf_q17 = y90_wf_q17

y90_wf_q18, y90_der_wf_q18 = np.array(
    drag_gaussian_pulse_waveforms(
        pi_amp_q18 / 2,
        pi_len,
        pi_sigma,
        drag_coef_q18,
        anharmonicity_q18,
        AC_stark_detuning_q18,
        sampling_rate=sampling_rate,
    )
)
y90_I_wf_q18 = (-1) * y90_der_wf_q18
y90_Q_wf_q18 = y90_wf_q18

y90_wf_q19, y90_der_wf_q19 = np.array(
    drag_gaussian_pulse_waveforms(
        pi_amp_q19 / 2,
        pi_len,
        pi_sigma,
        drag_coef_q19,
        anharmonicity_q19,
        AC_stark_detuning_q19,
        sampling_rate=sampling_rate,
    )
)
y90_I_wf_q19 = (-1) * y90_der_wf_q19
y90_Q_wf_q19 = y90_wf_q19

y90_wf_q20, y90_der_wf_q20 = np.array(
    drag_gaussian_pulse_waveforms(
        pi_amp_q20 / 2,
        pi_len,
        pi_sigma,
        drag_coef_q20,
        anharmonicity_q20,
        AC_stark_detuning_q20,
        sampling_rate=sampling_rate,
    )
)
y90_I_wf_q20 = (-1) * y90_der_wf_q20
y90_Q_wf_q20 = y90_wf_q20

y90_wf_q_C6, y90_der_wf_q_C6 = np.array(
    drag_gaussian_pulse_waveforms(
        pi_amp_q_C6 / 2,
        pi_len,
        pi_sigma,
        drag_coef_q_C6,
        anharmonicity_q_C6,
        AC_stark_detuning_q_C6,
        sampling_rate=sampling_rate,
    )
)
y90_I_wf_q_C6 = -y90_der_wf_q_C6
y90_Q_wf_q_C6 = y90_wf_q_C6



# No DRAG when alpha=0, it's just a gaussian.

minus_y90_wf_q1, minus_y90_der_wf_q1 = np.array(
    drag_gaussian_pulse_waveforms(
        -pi_amp_q1 / 2,
        pi_len,
        pi_sigma,
        drag_coef_q1,
        anharmonicity_q1,
        AC_stark_detuning_q1,
        sampling_rate=sampling_rate,
    )
)
minus_y90_I_wf_q1 = (-1) * minus_y90_der_wf_q1
minus_y90_Q_wf_q1 = minus_y90_wf_q1
minus_y90_wf_q2, minus_y90_der_wf_q2 = np.array(
    drag_gaussian_pulse_waveforms(
        -pi_amp_q2 / 2,
        pi_len,
        pi_sigma,
        drag_coef_q2,
        anharmonicity_q2,
        AC_stark_detuning_q2,
        sampling_rate=sampling_rate,
    )
)
minus_y90_I_wf_q2 = (-1) * minus_y90_der_wf_q2
minus_y90_Q_wf_q2 = minus_y90_wf_q2
minus_y90_wf_q3, minus_y90_der_wf_q3 = np.array(
    drag_gaussian_pulse_waveforms(
        -pi_amp_q3 / 2,
        pi_len,
        pi_sigma,
        drag_coef_q3,
        anharmonicity_q3,
        AC_stark_detuning_q3,
        sampling_rate=sampling_rate,
    )
)
minus_y90_I_wf_q3 = (-1) * minus_y90_der_wf_q3
minus_y90_Q_wf_q3 = minus_y90_wf_q3

minus_y90_wf_q4, minus_y90_der_wf_q4 = np.array(
    drag_gaussian_pulse_waveforms(
        -pi_amp_q4 / 2,
        pi_len,
        pi_sigma,
        drag_coef_q4,
        anharmonicity_q4,
        AC_stark_detuning_q4,
        sampling_rate=sampling_rate,
    )
)
minus_y90_I_wf_q4 = (-1) * minus_y90_der_wf_q4
minus_y90_Q_wf_q4 = minus_y90_wf_q4

minus_y90_wf_q5, minus_y90_der_wf_q5 = np.array(
    drag_gaussian_pulse_waveforms(
        -pi_amp_q5 / 2,
        pi_len,
        pi_sigma,
        drag_coef_q5,
        anharmonicity_q5,
        AC_stark_detuning_q5,
        sampling_rate=sampling_rate,
    )
)
minus_y90_I_wf_q5 = (-1) * minus_y90_der_wf_q5
minus_y90_Q_wf_q5 = minus_y90_wf_q5

minus_y90_wf_q6, minus_y90_der_wf_q6 = np.array(
    drag_gaussian_pulse_waveforms(
        -pi_amp_q6 / 2,
        pi_len,
        pi_sigma,
        drag_coef_q6,
        anharmonicity_q6,
        AC_stark_detuning_q6,
        sampling_rate=sampling_rate,
    )
)
minus_y90_I_wf_q6 = (-1) * minus_y90_der_wf_q6
minus_y90_Q_wf_q6 = minus_y90_wf_q6

minus_y90_wf_q7, minus_y90_der_wf_q7 = np.array(
    drag_gaussian_pulse_waveforms(
        -pi_amp_q7 / 2,
        pi_len,
        pi_sigma,
        drag_coef_q7,
        anharmonicity_q7,
        AC_stark_detuning_q7,
        sampling_rate=sampling_rate,
    )
)
minus_y90_I_wf_q7 = (-1) * minus_y90_der_wf_q7
minus_y90_Q_wf_q7 = minus_y90_wf_q7

minus_y90_wf_q8, minus_y90_der_wf_q8 = np.array(
    drag_gaussian_pulse_waveforms(
        -pi_amp_q8 / 2,
        pi_len,
        pi_sigma,
        drag_coef_q8,
        anharmonicity_q8,
        AC_stark_detuning_q8,
        sampling_rate=sampling_rate,
    )
)
minus_y90_I_wf_q8 = (-1) * minus_y90_der_wf_q8
minus_y90_Q_wf_q8 = minus_y90_wf_q8

minus_y90_wf_q9, minus_y90_der_wf_q9 = np.array(
    drag_gaussian_pulse_waveforms(
        -pi_amp_q9 / 2,
        pi_len,
        pi_sigma,
        drag_coef_q9,
        anharmonicity_q9,
        AC_stark_detuning_q9,
        sampling_rate=sampling_rate,
    )
)
minus_y90_I_wf_q9 = (-1) * minus_y90_der_wf_q9
minus_y90_Q_wf_q9 = minus_y90_wf_q9

minus_y90_wf_q10, minus_y90_der_wf_q10 = np.array(
    drag_gaussian_pulse_waveforms(
        -pi_amp_q10 / 2,
        pi_len,
        pi_sigma,
        drag_coef_q10,
        anharmonicity_q10,
        AC_stark_detuning_q10,
        sampling_rate=sampling_rate,
    )
)
minus_y90_I_wf_q10 = (-1) * minus_y90_der_wf_q10
minus_y90_Q_wf_q10 = minus_y90_wf_q10

minus_y90_wf_q11, minus_y90_der_wf_q11 = np.array(
    drag_gaussian_pulse_waveforms(
        -pi_amp_q11 / 2,
        pi_len,
        pi_sigma,
        drag_coef_q11,
        anharmonicity_q11,
        AC_stark_detuning_q11,
        sampling_rate=sampling_rate,
    )
)
minus_y90_I_wf_q11 = (-1) * minus_y90_der_wf_q11
minus_y90_Q_wf_q11 = minus_y90_wf_q11

minus_y90_wf_q12, minus_y90_der_wf_q12 = np.array(
    drag_gaussian_pulse_waveforms(
        -pi_amp_q12 / 2,
        pi_len,
        pi_sigma,
        drag_coef_q12,
        anharmonicity_q12,
        AC_stark_detuning_q12,
        sampling_rate=sampling_rate,
    )
)
minus_y90_I_wf_q12 = (-1) * minus_y90_der_wf_q12
minus_y90_Q_wf_q12 = minus_y90_wf_q12

minus_y90_wf_q13, minus_y90_der_wf_q13 = np.array(
    drag_gaussian_pulse_waveforms(
        -pi_amp_q13 / 2,
        pi_len,
        pi_sigma,
        drag_coef_q13,
        anharmonicity_q13,
        AC_stark_detuning_q13,
        sampling_rate=sampling_rate,
    )
)
minus_y90_I_wf_q13 = (-1) * minus_y90_der_wf_q13
minus_y90_Q_wf_q13 = minus_y90_wf_q13

minus_y90_wf_q14, minus_y90_der_wf_q14 = np.array(
    drag_gaussian_pulse_waveforms(
        -pi_amp_q14 / 2,
        pi_len,
        pi_sigma,
        drag_coef_q14,
        anharmonicity_q14,
        AC_stark_detuning_q14,
        sampling_rate=sampling_rate,
    )
)
minus_y90_I_wf_q14 = (-1) * minus_y90_der_wf_q14
minus_y90_Q_wf_q14 = minus_y90_wf_q14

minus_y90_wf_q15, minus_y90_der_wf_q15 = np.array(
    drag_gaussian_pulse_waveforms(
        -pi_amp_q15 / 2,
        pi_len,
        pi_sigma,
        drag_coef_q15,
        anharmonicity_q15,
        AC_stark_detuning_q15,
        sampling_rate=sampling_rate,
    )
)
minus_y90_I_wf_q15 = (-1) * minus_y90_der_wf_q15
minus_y90_Q_wf_q15 = minus_y90_wf_q15

minus_y90_wf_q16, minus_y90_der_wf_q16 = np.array(
    drag_gaussian_pulse_waveforms(
        -pi_amp_q16 / 2,
        pi_len,
        pi_sigma,
        drag_coef_q16,
        anharmonicity_q16,
        AC_stark_detuning_q16,
        sampling_rate=sampling_rate,
    )
)
minus_y90_I_wf_q16 = (-1) * minus_y90_der_wf_q16
minus_y90_Q_wf_q16 = minus_y90_wf_q16

minus_y90_wf_q17, minus_y90_der_wf_q17 = np.array(
    drag_gaussian_pulse_waveforms(
        -pi_amp_q17 / 2,
        pi_len,
        pi_sigma,
        drag_coef_q17,
        anharmonicity_q17,
        AC_stark_detuning_q17,
        sampling_rate=sampling_rate,
    )
)
minus_y90_I_wf_q17 = (-1) * minus_y90_der_wf_q17
minus_y90_Q_wf_q17 = minus_y90_wf_q17

minus_y90_wf_q18, minus_y90_der_wf_q18 = np.array(
    drag_gaussian_pulse_waveforms(
        -pi_amp_q18 / 2,
        pi_len,
        pi_sigma,
        drag_coef_q18,
        anharmonicity_q18,
        AC_stark_detuning_q18,
        sampling_rate=sampling_rate,
    )
)
minus_y90_I_wf_q18 = (-1) * minus_y90_der_wf_q18
minus_y90_Q_wf_q18 = minus_y90_wf_q18

minus_y90_wf_q19, minus_y90_der_wf_q19 = np.array(
    drag_gaussian_pulse_waveforms(
        -pi_amp_q19 / 2,
        pi_len,
        pi_sigma,
        drag_coef_q19,
        anharmonicity_q19,
        AC_stark_detuning_q19,
        sampling_rate=sampling_rate,
    )
)
minus_y90_I_wf_q19 = (-1) * minus_y90_der_wf_q19
minus_y90_Q_wf_q19 = minus_y90_wf_q19

minus_y90_wf_q20, minus_y90_der_wf_q20 = np.array(
    drag_gaussian_pulse_waveforms(
        -pi_amp_q20 / 2,
        pi_len,
        pi_sigma,
        drag_coef_q20,
        anharmonicity_q20,
        AC_stark_detuning_q20,
        sampling_rate=sampling_rate,
    )
)
minus_y90_I_wf_q20 = (-1) * minus_y90_der_wf_q20
minus_y90_Q_wf_q20 = minus_y90_wf_q20

minus_y90_wf_q_C6, minus_y90_der_wf_q_C6 = np.array(
    drag_gaussian_pulse_waveforms(
        -pi_amp_q_C6 / 2,
        pi_len,
        pi_sigma,
        drag_coef_q_C6,
        anharmonicity_q_C6,
        AC_stark_detuning_q_C6,
        sampling_rate=sampling_rate,
    )
)
minus_y90_I_wf_q_C6 = -minus_y90_der_wf_q_C6
minus_y90_Q_wf_q_C6 = minus_y90_wf_q_C6



# No DRAG when alpha=0, it's just a gaussian.

y45_wf_q1, y45_der_wf_q1 = np.array(
    drag_gaussian_pulse_waveforms(
        pi_amp_q1 / 4,
        pi_len,
        pi_sigma,
        drag_coef_q1,
        anharmonicity_q1,
        AC_stark_detuning_q1,
        sampling_rate=sampling_rate,
    )
)
y45_I_wf_q1 = (-1) * y45_der_wf_q1
y45_Q_wf_q1 = y45_wf_q1

minus_y45_wf_q1, minus_y45_der_wf_q1 = np.array(
    drag_gaussian_pulse_waveforms(
        -pi_amp_q1 / 4,
        pi_len,
        pi_sigma,
        drag_coef_q1,
        anharmonicity_q1,
        AC_stark_detuning_q1,
        sampling_rate=sampling_rate,
    )
)
minus_y45_I_wf_q1 = (-1) * minus_y45_der_wf_q1
minus_y45_Q_wf_q1 = minus_y45_wf_q1

y45_wf_q2, y45_der_wf_q2 = np.array(
    drag_gaussian_pulse_waveforms(
        pi_amp_q2 / 4,
        pi_len,
        pi_sigma,
        drag_coef_q2,
        anharmonicity_q2,
        AC_stark_detuning_q2,
        sampling_rate=sampling_rate,
    )
)
y45_I_wf_q2 = (-1) * y45_der_wf_q2
y45_Q_wf_q2 = y45_wf_q2

minus_y45_wf_q2, minus_y45_der_wf_q2 = np.array(
    drag_gaussian_pulse_waveforms(
        -pi_amp_q2 / 4,
        pi_len,
        pi_sigma,
        drag_coef_q2,
        anharmonicity_q2,
        AC_stark_detuning_q2,
        sampling_rate=sampling_rate,
    )
)
minus_y45_I_wf_q2 = (-1) * minus_y45_der_wf_q2
minus_y45_Q_wf_q2 = minus_y45_wf_q2

y45_wf_q3, y45_der_wf_q3 = np.array(
    drag_gaussian_pulse_waveforms(
        pi_amp_q3 / 4,
        pi_len,
        pi_sigma,
        drag_coef_q3,
        anharmonicity_q3,
        AC_stark_detuning_q3,
        sampling_rate=sampling_rate,
    )
)
y45_I_wf_q3 = (-1) * y45_der_wf_q3
y45_Q_wf_q3 = y45_wf_q3

minus_y45_wf_q3, minus_y45_der_wf_q3 = np.array(
    drag_gaussian_pulse_waveforms(
        -pi_amp_q3 / 4,
        pi_len,
        pi_sigma,
        drag_coef_q3,
        anharmonicity_q3,
        AC_stark_detuning_q3,
        sampling_rate=sampling_rate,
    )
)
minus_y45_I_wf_q3 = (-1) * minus_y45_der_wf_q3
minus_y45_Q_wf_q3 = minus_y45_wf_q3

y45_wf_q4, y45_der_wf_q4 = np.array(
    drag_gaussian_pulse_waveforms(
        pi_amp_q4 / 4,
        pi_len,
        pi_sigma,
        drag_coef_q4,
        anharmonicity_q4,
        AC_stark_detuning_q4,
        sampling_rate=sampling_rate,
    )
)
y45_I_wf_q4 = (-1) * y45_der_wf_q4
y45_Q_wf_q4 = y45_wf_q4

minus_y45_wf_q4, minus_y45_der_wf_q4 = np.array(
    drag_gaussian_pulse_waveforms(
        -pi_amp_q4 / 4,
        pi_len,
        pi_sigma,
        drag_coef_q4,
        anharmonicity_q4,
        AC_stark_detuning_q4,
        sampling_rate=sampling_rate,
    )
)
minus_y45_I_wf_q4 = (-1) * minus_y45_der_wf_q4
minus_y45_Q_wf_q4 = minus_y45_wf_q4

y45_wf_q5, y45_der_wf_q5 = np.array(
    drag_gaussian_pulse_waveforms(
        pi_amp_q5 / 4,
        pi_len,
        pi_sigma,
        drag_coef_q5,
        anharmonicity_q5,
        AC_stark_detuning_q5,
        sampling_rate=sampling_rate,
    )
)
y45_I_wf_q5 = (-1) * y45_der_wf_q5
y45_Q_wf_q5 = y45_wf_q5

minus_y45_wf_q5, minus_y45_der_wf_q5 = np.array(
    drag_gaussian_pulse_waveforms(
        -pi_amp_q5 / 4,
        pi_len,
        pi_sigma,
        drag_coef_q5,
        anharmonicity_q5,
        AC_stark_detuning_q5,
        sampling_rate=sampling_rate,
    )
)
minus_y45_I_wf_q5 = (-1) * minus_y45_der_wf_q5
minus_y45_Q_wf_q5 = minus_y45_wf_q5

y45_wf_q6, y45_der_wf_q6 = np.array(
    drag_gaussian_pulse_waveforms(
        pi_amp_q6 / 4,
        pi_len,
        pi_sigma,
        drag_coef_q6,
        anharmonicity_q6,
        AC_stark_detuning_q6,
        sampling_rate=sampling_rate,
    )
)
y45_I_wf_q6 = (-1) * y45_der_wf_q6
y45_Q_wf_q6 = y45_wf_q6

minus_y45_wf_q6, minus_y45_der_wf_q6 = np.array(
    drag_gaussian_pulse_waveforms(
        -pi_amp_q6 / 4,
        pi_len,
        pi_sigma,
        drag_coef_q6,
        anharmonicity_q6,
        AC_stark_detuning_q6,
        sampling_rate=sampling_rate,
    )
)
minus_y45_I_wf_q6 = (-1) * minus_y45_der_wf_q6
minus_y45_Q_wf_q6 = minus_y45_wf_q6

y45_wf_q7, y45_der_wf_q7 = np.array(
    drag_gaussian_pulse_waveforms(
        pi_amp_q7 / 4,
        pi_len,
        pi_sigma,
        drag_coef_q7,
        anharmonicity_q7,
        AC_stark_detuning_q7,
        sampling_rate=sampling_rate,
    )
)
y45_I_wf_q7 = (-1) * y45_der_wf_q7
y45_Q_wf_q7 = y45_wf_q7

minus_y45_wf_q7, minus_y45_der_wf_q7 = np.array(
    drag_gaussian_pulse_waveforms(
        -pi_amp_q7 / 4,
        pi_len,
        pi_sigma,
        drag_coef_q7,
        anharmonicity_q7,
        AC_stark_detuning_q7,
        sampling_rate=sampling_rate,
    )
)
minus_y45_I_wf_q7 = (-1) * minus_y45_der_wf_q7
minus_y45_Q_wf_q7 = minus_y45_wf_q7

y45_wf_q8, y45_der_wf_q8 = np.array(
    drag_gaussian_pulse_waveforms(
        pi_amp_q8 / 4,
        pi_len,
        pi_sigma,
        drag_coef_q8,
        anharmonicity_q8,
        AC_stark_detuning_q8,
        sampling_rate=sampling_rate,
    )
)
y45_I_wf_q8 = (-1) * y45_der_wf_q8
y45_Q_wf_q8 = y45_wf_q8

minus_y45_wf_q8, minus_y45_der_wf_q8 = np.array(
    drag_gaussian_pulse_waveforms(
        -pi_amp_q8 / 4,
        pi_len,
        pi_sigma,
        drag_coef_q8,
        anharmonicity_q8,
        AC_stark_detuning_q8,
        sampling_rate=sampling_rate,
    )
)
minus_y45_I_wf_q8 = (-1) * minus_y45_der_wf_q8
minus_y45_Q_wf_q8 = minus_y45_wf_q8

y45_wf_q9, y45_der_wf_q9 = np.array(
    drag_gaussian_pulse_waveforms(
        pi_amp_q9 / 4,
        pi_len,
        pi_sigma,
        drag_coef_q9,
        anharmonicity_q9,
        AC_stark_detuning_q9,
        sampling_rate=sampling_rate,
    )
)
y45_I_wf_q9 = (-1) * y45_der_wf_q9
y45_Q_wf_q9 = y45_wf_q9

minus_y45_wf_q9, minus_y45_der_wf_q9 = np.array(
    drag_gaussian_pulse_waveforms(
        -pi_amp_q9 / 4,
        pi_len,
        pi_sigma,
        drag_coef_q9,
        anharmonicity_q9,
        AC_stark_detuning_q9,
        sampling_rate=sampling_rate,
    )
)
minus_y45_I_wf_q9 = (-1) * minus_y45_der_wf_q9
minus_y45_Q_wf_q9 = minus_y45_wf_q9

y45_wf_q10, y45_der_wf_q10 = np.array(
    drag_gaussian_pulse_waveforms(
        pi_amp_q10 / 4,
        pi_len,
        pi_sigma,
        drag_coef_q10,
        anharmonicity_q10,
        AC_stark_detuning_q10,
        sampling_rate=sampling_rate,
    )
)
y45_I_wf_q10 = (-1) * y45_der_wf_q10
y45_Q_wf_q10 = y45_wf_q10

minus_y45_wf_q10, minus_y45_der_wf_q10 = np.array(
    drag_gaussian_pulse_waveforms(
        -pi_amp_q10 / 4,
        pi_len,
        pi_sigma,
        drag_coef_q10,
        anharmonicity_q10,
        AC_stark_detuning_q10,
        sampling_rate=sampling_rate,
    )
)
minus_y45_I_wf_q10 = (-1) * minus_y45_der_wf_q10
minus_y45_Q_wf_q10 = minus_y45_wf_q10

y45_wf_q11, y45_der_wf_q11 = np.array(
    drag_gaussian_pulse_waveforms(
        pi_amp_q11 / 4,
        pi_len,
        pi_sigma,
        drag_coef_q11,
        anharmonicity_q11,
        AC_stark_detuning_q11,
        sampling_rate=sampling_rate,
    )
)
y45_I_wf_q11 = (-1) * y45_der_wf_q11
y45_Q_wf_q11 = y45_wf_q11

minus_y45_wf_q11, minus_y45_der_wf_q11 = np.array(
    drag_gaussian_pulse_waveforms(
        -pi_amp_q11 / 4,
        pi_len,
        pi_sigma,
        drag_coef_q11,
        anharmonicity_q11,
        AC_stark_detuning_q11,
        sampling_rate=sampling_rate,
    )
)
minus_y45_I_wf_q11 = (-1) * minus_y45_der_wf_q11
minus_y45_Q_wf_q11 = minus_y45_wf_q11

y45_wf_q12, y45_der_wf_q12 = np.array(
    drag_gaussian_pulse_waveforms(
        pi_amp_q12 / 4,
        pi_len,
        pi_sigma,
        drag_coef_q12,
        anharmonicity_q12,
        AC_stark_detuning_q12,
        sampling_rate=sampling_rate,
    )
)
y45_I_wf_q12 = (-1) * y45_der_wf_q12
y45_Q_wf_q12 = y45_wf_q12

minus_y45_wf_q12, minus_y45_der_wf_q12 = np.array(
    drag_gaussian_pulse_waveforms(
        -pi_amp_q12 / 4,
        pi_len,
        pi_sigma,
        drag_coef_q12,
        anharmonicity_q12,
        AC_stark_detuning_q12,
        sampling_rate=sampling_rate,
    )
)
minus_y45_I_wf_q12 = (-1) * minus_y45_der_wf_q12
minus_y45_Q_wf_q12 = minus_y45_wf_q12

y45_wf_q13, y45_der_wf_q13 = np.array(
    drag_gaussian_pulse_waveforms(
        pi_amp_q13 / 4,
        pi_len,
        pi_sigma,
        drag_coef_q13,
        anharmonicity_q13,
        AC_stark_detuning_q13,
        sampling_rate=sampling_rate,
    )
)
y45_I_wf_q13 = (-1) * y45_der_wf_q13
y45_Q_wf_q13 = y45_wf_q13

minus_y45_wf_q13, minus_y45_der_wf_q13 = np.array(
    drag_gaussian_pulse_waveforms(
        -pi_amp_q13 / 4,
        pi_len,
        pi_sigma,
        drag_coef_q13,
        anharmonicity_q13,
        AC_stark_detuning_q13,
        sampling_rate=sampling_rate,
    )
)
minus_y45_I_wf_q13 = (-1) * minus_y45_der_wf_q13
minus_y45_Q_wf_q13 = minus_y45_wf_q13

y45_wf_q14, y45_der_wf_q14 = np.array(
    drag_gaussian_pulse_waveforms(
        pi_amp_q14 / 4,
        pi_len,
        pi_sigma,
        drag_coef_q14,
        anharmonicity_q14,
        AC_stark_detuning_q14,
        sampling_rate=sampling_rate,
    )
)
y45_I_wf_q14 = (-1) * y45_der_wf_q14
y45_Q_wf_q14 = y45_wf_q14

minus_y45_wf_q14, minus_y45_der_wf_q14 = np.array(
    drag_gaussian_pulse_waveforms(
        -pi_amp_q14 / 4,
        pi_len,
        pi_sigma,
        drag_coef_q14,
        anharmonicity_q14,
        AC_stark_detuning_q14,
        sampling_rate=sampling_rate,
    )
)
minus_y45_I_wf_q14 = (-1) * minus_y45_der_wf_q14
minus_y45_Q_wf_q14 = minus_y45_wf_q14

y45_wf_q15, y45_der_wf_q15 = np.array(
    drag_gaussian_pulse_waveforms(
        pi_amp_q15 / 4,
        pi_len,
        pi_sigma,
        drag_coef_q15,
        anharmonicity_q15,
        AC_stark_detuning_q15,
        sampling_rate=sampling_rate,
    )
)
y45_I_wf_q15 = (-1) * y45_der_wf_q15
y45_Q_wf_q15 = y45_wf_q15

minus_y45_wf_q15, minus_y45_der_wf_q15 = np.array(
    drag_gaussian_pulse_waveforms(
        -pi_amp_q15 / 4,
        pi_len,
        pi_sigma,
        drag_coef_q15,
        anharmonicity_q15,
        AC_stark_detuning_q15,
        sampling_rate=sampling_rate,
    )
)
minus_y45_I_wf_q15 = (-1) * minus_y45_der_wf_q15
minus_y45_Q_wf_q15 = minus_y45_wf_q15

y45_wf_q16, y45_der_wf_q16 = np.array(
    drag_gaussian_pulse_waveforms(
        pi_amp_q16 / 4,
        pi_len,
        pi_sigma,
        drag_coef_q16,
        anharmonicity_q16,
        AC_stark_detuning_q16,
        sampling_rate=sampling_rate,
    )
)
y45_I_wf_q16 = (-1) * y45_der_wf_q16
y45_Q_wf_q16 = y45_wf_q16

minus_y45_wf_q16, minus_y45_der_wf_q16 = np.array(
    drag_gaussian_pulse_waveforms(
        -pi_amp_q16 / 4,
        pi_len,
        pi_sigma,
        drag_coef_q16,
        anharmonicity_q16,
        AC_stark_detuning_q16,
        sampling_rate=sampling_rate,
    )
)
minus_y45_I_wf_q16 = (-1) * minus_y45_der_wf_q16
minus_y45_Q_wf_q16 = minus_y45_wf_q16

y45_wf_q17, y45_der_wf_q17 = np.array(
    drag_gaussian_pulse_waveforms(
        pi_amp_q17 / 4,
        pi_len,
        pi_sigma,
        drag_coef_q17,
        anharmonicity_q17,
        AC_stark_detuning_q17,
        sampling_rate=sampling_rate,
    )
)
y45_I_wf_q17 = (-1) * y45_der_wf_q17
y45_Q_wf_q17 = y45_wf_q17

minus_y45_wf_q17, minus_y45_der_wf_q17 = np.array(
    drag_gaussian_pulse_waveforms(
        -pi_amp_q17 / 4,
        pi_len,
        pi_sigma,
        drag_coef_q17,
        anharmonicity_q17,
        AC_stark_detuning_q17,
        sampling_rate=sampling_rate,
    )
)
minus_y45_I_wf_q17 = (-1) * minus_y45_der_wf_q17
minus_y45_Q_wf_q17 = minus_y45_wf_q17

y45_wf_q18, y45_der_wf_q18 = np.array(
    drag_gaussian_pulse_waveforms(
        pi_amp_q18 / 4,
        pi_len,
        pi_sigma,
        drag_coef_q18,
        anharmonicity_q18,
        AC_stark_detuning_q18,
        sampling_rate=sampling_rate,
    )
)
y45_I_wf_q18 = (-1) * y45_der_wf_q18
y45_Q_wf_q18 = y45_wf_q18

minus_y45_wf_q18, minus_y45_der_wf_q18 = np.array(
    drag_gaussian_pulse_waveforms(
        -pi_amp_q18 / 4,
        pi_len,
        pi_sigma,
        drag_coef_q18,
        anharmonicity_q18,
        AC_stark_detuning_q18,
        sampling_rate=sampling_rate,
    )
)
minus_y45_I_wf_q18 = (-1) * minus_y45_der_wf_q18
minus_y45_Q_wf_q18 = minus_y45_wf_q18

y45_wf_q19, y45_der_wf_q19 = np.array(
    drag_gaussian_pulse_waveforms(
        pi_amp_q19 / 4,
        pi_len,
        pi_sigma,
        drag_coef_q19,
        anharmonicity_q19,
        AC_stark_detuning_q19,
        sampling_rate=sampling_rate,
    )
)
y45_I_wf_q19 = (-1) * y45_der_wf_q19
y45_Q_wf_q19 = y45_wf_q19

minus_y45_wf_q19, minus_y45_der_wf_q19 = np.array(
    drag_gaussian_pulse_waveforms(
        -pi_amp_q19 / 4,
        pi_len,
        pi_sigma,
        drag_coef_q19,
        anharmonicity_q19,
        AC_stark_detuning_q19,
        sampling_rate=sampling_rate,
    )
)
minus_y45_I_wf_q19 = (-1) * minus_y45_der_wf_q19
minus_y45_Q_wf_q19 = minus_y45_wf_q19

y45_wf_q20, y45_der_wf_q20 = np.array(
    drag_gaussian_pulse_waveforms(
        pi_amp_q20 / 4,
        pi_len,
        pi_sigma,
        drag_coef_q20,
        anharmonicity_q20,
        AC_stark_detuning_q20,
        sampling_rate=sampling_rate,
    )
)
y45_I_wf_q20 = (-1) * y45_der_wf_q20
y45_Q_wf_q20 = y45_wf_q20

minus_y45_wf_q20, minus_y45_der_wf_q20 = np.array(
    drag_gaussian_pulse_waveforms(
        -pi_amp_q20 / 4,
        pi_len,
        pi_sigma,
        drag_coef_q20,
        anharmonicity_q20,
        AC_stark_detuning_q20,
        sampling_rate=sampling_rate,
    )
)
minus_y45_I_wf_q20 = (-1) * minus_y45_der_wf_q20
minus_y45_Q_wf_q20 = minus_y45_wf_q20

y45_wf_q_C6, y45_der_wf_q_C6 = np.array(
    drag_gaussian_pulse_waveforms(
        pi_amp_q_C6 / 4,
        pi_len,
        pi_sigma,
        drag_coef_q_C6,
        anharmonicity_q_C6,
        AC_stark_detuning_q_C6,
        sampling_rate=sampling_rate,
    )
)
y45_I_wf_q_C6 = (-1)*y45_der_wf_q_C6
y45_Q_wf_q_C6 = y45_wf_q_C6


minus_y45_wf_q_C6, minus_y45_der_wf_q_C6 = np.array(
    drag_gaussian_pulse_waveforms(
        -pi_amp_q_C6 / 4,
        pi_len,
        pi_sigma,
        drag_coef_q_C6,
        anharmonicity_q_C6,
        AC_stark_detuning_q_C6,
        sampling_rate=sampling_rate,
    )
)
minus_y45_I_wf_q_C6 = (-1)* minus_y45_der_wf_q_C6
minus_y45_Q_wf_q_C6 = minus_y45_wf_q_C6




##########################################
#               Flux line                #
##########################################
flux_settle_time = 100 * u.ns

max_frequency_point1 = 0 
max_frequency_point2 = 0 

# Resonator frequency versus flux fit parameters according to resonator_spec_vs_flux
# amplitude * np.cos(2 * np.pi * frequency * x + phase) + offset
amplitude_fit1, frequency_fit1, phase_fit1, offset_fit1 = [0, 0, 0, 0]
amplitude_fit2, frequency_fit2, phase_fit2, offset_fit2 = [0, 0, 0, 0]





#############################################
#                Parametric                 #
#############################################
#no longer used, changed to parametric_IF_C12_0110 # parametric_IF1 = int(72.5e6) # parametric_IF2 = int(155.8e6) # parametric_IF1 = int(73.2e6)

# C12_1001 in q1q2 format
parametric_IF_C12_1001 = int(50e6) 
parametric_IF_C12_1102 = int(60e6) 
parametric_IF_C12_1120 = int(70e6) 


const_flux_len_C12_1001 = const_flux_len_setting 
const_flux_len_C12_1102 = 100
const_flux_len_C12_1120 = 160

gauss_flux_len = 160


const_flux_amp_C12_1001 = const_flux_amp_setting 
const_flux_amp_C12_1102 = 1.0 
const_flux_amp_C12_1120 = 1.5

gauss_flux_amp = 1.8

######################### new below

parametric_const_len = 500 

#C1
parametric_const_len_C1_Q12_1001 = parametric_const_len
parametric_const_len_C1_Q12_1102 = parametric_const_len
parametric_const_len_C1_Q12_1120 = parametric_const_len

parametric_const_len_C1_Q15_1001 = parametric_const_len
parametric_const_len_C1_Q15_1102 = parametric_const_len
parametric_const_len_C1_Q15_1120 = parametric_const_len

parametric_const_len_C1_Q16_1001 = parametric_const_len
parametric_const_len_C1_Q16_1102 = parametric_const_len
parametric_const_len_C1_Q16_1120 = parametric_const_len

parametric_const_len_C1_Q25_1001 = parametric_const_len
parametric_const_len_C1_Q25_1102 = parametric_const_len
parametric_const_len_C1_Q25_1120 = parametric_const_len

parametric_const_len_C1_Q26_1001 = parametric_const_len
parametric_const_len_C1_Q26_1102 = parametric_const_len
parametric_const_len_C1_Q26_1120 = parametric_const_len

parametric_const_len_C1_Q56_1001 = parametric_const_len
parametric_const_len_C1_Q56_1102 = parametric_const_len
parametric_const_len_C1_Q56_1120 = parametric_const_len

#C4
parametric_const_len_C4_Q56_1001 = parametric_const_len
parametric_const_len_C4_Q56_1102 = parametric_const_len
parametric_const_len_C4_Q56_1120 = parametric_const_len

parametric_const_len_C4_Q59_1001 = parametric_const_len
parametric_const_len_C4_Q59_1102 = parametric_const_len
parametric_const_len_C4_Q59_1120 = parametric_const_len

parametric_const_len_C4_Q510_1001 = parametric_const_len
parametric_const_len_C4_Q510_1102 = parametric_const_len
parametric_const_len_C4_Q510_1120 = parametric_const_len

parametric_const_len_C4_Q69_1001 = parametric_const_len
parametric_const_len_C4_Q69_1102 = parametric_const_len
parametric_const_len_C4_Q69_1120 = parametric_const_len

parametric_const_len_C4_Q610_1001 = parametric_const_len
parametric_const_len_C4_Q610_1102 = parametric_const_len
parametric_const_len_C4_Q610_1120 = parametric_const_len

parametric_const_len_C4_Q910_1001 = parametric_const_len
parametric_const_len_C4_Q910_1102 = parametric_const_len
parametric_const_len_C4_Q910_1120 = parametric_const_len

#C6
parametric_const_len_C6_Q910_1001 = parametric_const_len
parametric_const_len_C6_Q910_1102 = parametric_const_len
parametric_const_len_C6_Q910_1120 = parametric_const_len

parametric_const_len_C6_Q913_1001 = parametric_const_len
parametric_const_len_C6_Q913_1102 = parametric_const_len
parametric_const_len_C6_Q913_1120 = parametric_const_len

parametric_const_len_C6_Q914_1001 = parametric_const_len
parametric_const_len_C6_Q914_1102 = parametric_const_len
parametric_const_len_C6_Q914_1120 = parametric_const_len

parametric_const_len_C6_Q1013_1001 = parametric_const_len
parametric_const_len_C6_Q1013_1102 = parametric_const_len
parametric_const_len_C6_Q1013_1120 = parametric_const_len

parametric_const_len_C6_Q1014_1001 = parametric_const_len
parametric_const_len_C6_Q1014_1102 = parametric_const_len
parametric_const_len_C6_Q1014_1120 = parametric_const_len

parametric_const_len_C6_Q1314_1001 = parametric_const_len
parametric_const_len_C6_Q1314_1102 = parametric_const_len
parametric_const_len_C6_Q1314_1120 = parametric_const_len

#C8
parametric_const_len_C8_Q1314_1001 = parametric_const_len
parametric_const_len_C8_Q1314_1102 = parametric_const_len
parametric_const_len_C8_Q1314_1120 = parametric_const_len

parametric_const_len_C8_Q1317_1001 = parametric_const_len
parametric_const_len_C8_Q1317_1102 = parametric_const_len
parametric_const_len_C8_Q1317_1120 = parametric_const_len

parametric_const_len_C8_Q1318_1001 = parametric_const_len
parametric_const_len_C8_Q1318_1102 = parametric_const_len
parametric_const_len_C8_Q1318_1120 = parametric_const_len

parametric_const_len_C8_Q1417_1001 = parametric_const_len
parametric_const_len_C8_Q1417_1102 = parametric_const_len
parametric_const_len_C8_Q1417_1120 = parametric_const_len

parametric_const_len_C8_Q1418_1001 = parametric_const_len
parametric_const_len_C8_Q1418_1102 = parametric_const_len
parametric_const_len_C8_Q1418_1120 = parametric_const_len

parametric_const_len_C8_Q1718_1001 = parametric_const_len
parametric_const_len_C8_Q1718_1102 = parametric_const_len
parametric_const_len_C8_Q1718_1120 = parametric_const_len

# ---- C3 lengths ----
parametric_const_len_C3_Q34_1001 = parametric_const_len
parametric_const_len_C3_Q34_1102 = parametric_const_len
parametric_const_len_C3_Q34_1120 = parametric_const_len

parametric_const_len_C3_Q38_1001 = parametric_const_len
parametric_const_len_C3_Q38_1102 = parametric_const_len
parametric_const_len_C3_Q38_1120 = parametric_const_len

parametric_const_len_C3_Q37_1001 = parametric_const_len
parametric_const_len_C3_Q37_1102 = parametric_const_len
parametric_const_len_C3_Q37_1120 = parametric_const_len

parametric_const_len_C3_Q48_1001 = parametric_const_len
parametric_const_len_C3_Q48_1102 = parametric_const_len
parametric_const_len_C3_Q48_1120 = parametric_const_len

parametric_const_len_C3_Q47_1001 = parametric_const_len
parametric_const_len_C3_Q47_1102 = parametric_const_len
parametric_const_len_C3_Q47_1120 = parametric_const_len

parametric_const_len_C3_Q78_1001 = parametric_const_len
parametric_const_len_C3_Q78_1102 = parametric_const_len
parametric_const_len_C3_Q78_1120 = parametric_const_len

# ---- C5 lengths ----
parametric_const_len_C5_Q78_1001 = parametric_const_len
parametric_const_len_C5_Q78_1102 = parametric_const_len
parametric_const_len_C5_Q78_1120 = parametric_const_len

parametric_const_len_C5_Q712_1001 = parametric_const_len
parametric_const_len_C5_Q712_1102 = parametric_const_len
parametric_const_len_C5_Q712_1120 = parametric_const_len

parametric_const_len_C5_Q711_1001 = parametric_const_len
parametric_const_len_C5_Q711_1102 = parametric_const_len
parametric_const_len_C5_Q711_1120 = parametric_const_len

parametric_const_len_C5_Q812_1001 = parametric_const_len
parametric_const_len_C5_Q812_1102 = parametric_const_len
parametric_const_len_C5_Q812_1120 = parametric_const_len

parametric_const_len_C5_Q811_1001 = parametric_const_len
parametric_const_len_C5_Q811_1102 = parametric_const_len
parametric_const_len_C5_Q811_1120 = parametric_const_len

parametric_const_len_C5_Q1112_1001 = parametric_const_len
parametric_const_len_C5_Q1112_1102 = parametric_const_len
parametric_const_len_C5_Q1112_1120 = parametric_const_len

# ---- C7 lengths ----
parametric_const_len_C7_Q1112_1001 = parametric_const_len
parametric_const_len_C7_Q1112_1102 = parametric_const_len
parametric_const_len_C7_Q1112_1120 = parametric_const_len

parametric_const_len_C7_Q1116_1001 = parametric_const_len
parametric_const_len_C7_Q1116_1102 = parametric_const_len
parametric_const_len_C7_Q1116_1120 = parametric_const_len

parametric_const_len_C7_Q1115_1001 = parametric_const_len
parametric_const_len_C7_Q1115_1102 = parametric_const_len
parametric_const_len_C7_Q1115_1120 = parametric_const_len

parametric_const_len_C7_Q1216_1001 = parametric_const_len
parametric_const_len_C7_Q1216_1102 = parametric_const_len
parametric_const_len_C7_Q1216_1120 = parametric_const_len

parametric_const_len_C7_Q1215_1001 = parametric_const_len
parametric_const_len_C7_Q1215_1102 = parametric_const_len
parametric_const_len_C7_Q1215_1120 = parametric_const_len

parametric_const_len_C7_Q1516_1001 = parametric_const_len
parametric_const_len_C7_Q1516_1102 = parametric_const_len
parametric_const_len_C7_Q1516_1120 = parametric_const_len

# ---- C10 lengths ----
parametric_const_len_C10_Q1516_1001 = parametric_const_len
parametric_const_len_C10_Q1516_1102 = parametric_const_len
parametric_const_len_C10_Q1516_1120 = parametric_const_len

parametric_const_len_C10_Q1520_1001 = parametric_const_len
parametric_const_len_C10_Q1520_1102 = parametric_const_len
parametric_const_len_C10_Q1520_1120 = parametric_const_len

parametric_const_len_C10_Q1519_1001 = parametric_const_len
parametric_const_len_C10_Q1519_1102 = parametric_const_len
parametric_const_len_C10_Q1519_1120 = parametric_const_len

parametric_const_len_C10_Q1620_1001 = parametric_const_len
parametric_const_len_C10_Q1620_1102 = parametric_const_len
parametric_const_len_C10_Q1620_1120 = parametric_const_len

parametric_const_len_C10_Q1619_1001 = parametric_const_len
parametric_const_len_C10_Q1619_1102 = parametric_const_len
parametric_const_len_C10_Q1619_1120 = parametric_const_len

parametric_const_len_C10_Q1920_1001 = parametric_const_len
parametric_const_len_C10_Q1920_1102 = parametric_const_len
parametric_const_len_C10_Q1920_1120 = parametric_const_len

parametric_const_len_C2_Q37_1001 = parametric_const_len
parametric_const_len_C2_Q37_1102 = parametric_const_len
parametric_const_len_C2_Q37_1120 = parametric_const_len

parametric_const_len_C2_Q36_1001 = parametric_const_len
parametric_const_len_C2_Q36_1102 = parametric_const_len
parametric_const_len_C2_Q36_1120 = parametric_const_len

parametric_const_len_C2_Q67_1001 = parametric_const_len
parametric_const_len_C2_Q67_1102 = parametric_const_len
parametric_const_len_C2_Q67_1120 = parametric_const_len

parametric_const_len_C9_Q1519_1001 = parametric_const_len
parametric_const_len_C9_Q1519_1102 = parametric_const_len
parametric_const_len_C9_Q1519_1120 = parametric_const_len

parametric_const_len_C9_Q1415_1001 = parametric_const_len
parametric_const_len_C9_Q1415_1102 = parametric_const_len
parametric_const_len_C9_Q1415_1120 = parametric_const_len

parametric_const_len_C9_Q1419_1001 = parametric_const_len
parametric_const_len_C9_Q1419_1102 = parametric_const_len
parametric_const_len_C9_Q1419_1120 = parametric_const_len





#C1
parametric_IF_C1_Q12_1001 = (50) * u.MHz
parametric_IF_C1_Q12_1102 = (100) * u.MHz
parametric_IF_C1_Q12_1120 = (150) * u.MHz

parametric_IF_C1_Q15_1001 = (200) * u.MHz
parametric_IF_C1_Q15_1102 = (250) * u.MHz
parametric_IF_C1_Q15_1120 = (300) * u.MHz

parametric_IF_C1_Q16_1001 = (350) * u.MHz
parametric_IF_C1_Q16_1102 = (400) * u.MHz
parametric_IF_C1_Q16_1120 = (450) * u.MHz

parametric_IF_C1_Q25_1001 = (50) * u.MHz
parametric_IF_C1_Q25_1102 = (100) * u.MHz
parametric_IF_C1_Q25_1120 = (150) * u.MHz

parametric_IF_C1_Q26_1001 = (200) * u.MHz
parametric_IF_C1_Q26_1102 = (250) * u.MHz
parametric_IF_C1_Q26_1120 = (300) * u.MHz

parametric_IF_C1_Q56_1001 = (350) * u.MHz
parametric_IF_C1_Q56_1102 = (400) * u.MHz
parametric_IF_C1_Q56_1120 = (450) * u.MHz



#C4
parametric_IF_C4_Q56_1001 = (50) * u.MHz
parametric_IF_C4_Q56_1102 = (100) * u.MHz
parametric_IF_C4_Q56_1120 = (150) * u.MHz

parametric_IF_C4_Q59_1001 = (200) * u.MHz
parametric_IF_C4_Q59_1102 = (250) * u.MHz
parametric_IF_C4_Q59_1120 = (300) * u.MHz

parametric_IF_C4_Q510_1001 = (350) * u.MHz
parametric_IF_C4_Q510_1102 = (400) * u.MHz
parametric_IF_C4_Q510_1120 = (450) * u.MHz

parametric_IF_C4_Q69_1001 = (50) * u.MHz
parametric_IF_C4_Q69_1102 = (100) * u.MHz
parametric_IF_C4_Q69_1120 = (150) * u.MHz

parametric_IF_C4_Q610_1001 = (200) * u.MHz
parametric_IF_C4_Q610_1102 = (250) * u.MHz
parametric_IF_C4_Q610_1120 = (300) * u.MHz

parametric_IF_C4_Q910_1001 = (350) * u.MHz
parametric_IF_C4_Q910_1102 = (400) * u.MHz
parametric_IF_C4_Q910_1120 = (450) * u.MHz




#C6
parametric_IF_C6_Q910_1001 = (50) * u.MHz
parametric_IF_C6_Q910_1102 = (100) * u.MHz
parametric_IF_C6_Q910_1120 = (150) * u.MHz

parametric_IF_C6_Q913_1001 = (200) * u.MHz
parametric_IF_C6_Q913_1102 = (250) * u.MHz
parametric_IF_C6_Q913_1120 = (300) * u.MHz

parametric_IF_C6_Q914_1001 = (350) * u.MHz
parametric_IF_C6_Q914_1102 = (400) * u.MHz
parametric_IF_C6_Q914_1120 = (450) * u.MHz

parametric_IF_C6_Q1013_1001 = (50) * u.MHz
parametric_IF_C6_Q1013_1102 = (100) * u.MHz
parametric_IF_C6_Q1013_1120 = (150) * u.MHz

parametric_IF_C6_Q1014_1001 = (200) * u.MHz
parametric_IF_C6_Q1014_1102 = (250) * u.MHz 
parametric_IF_C6_Q1014_1120 = (300) * u.MHz

parametric_IF_C6_Q1314_1001 = (350) * u.MHz
parametric_IF_C6_Q1314_1102 = (400) * u.MHz
parametric_IF_C6_Q1314_1120 = (450) * u.MHz




#C8

parametric_IF_C8_Q1314_1001 = (50) * u.MHz
parametric_IF_C8_Q1314_1102 = (100) * u.MHz
parametric_IF_C8_Q1314_1120 = (150) * u.MHz

parametric_IF_C8_Q1317_1001 = (200) * u.MHz
parametric_IF_C8_Q1317_1102 = (250) * u.MHz
parametric_IF_C8_Q1317_1120 = (300) * u.MHz


parametric_IF_C8_Q1318_1001 = (350) * u.MHz
parametric_IF_C8_Q1318_1102 = (400) * u.MHz
parametric_IF_C8_Q1318_1120 = (450) * u.MHz

parametric_IF_C8_Q1417_1001 = (50) * u.MHz
parametric_IF_C8_Q1417_1102 = (100) * u.MHz
parametric_IF_C8_Q1417_1120 = (150) * u.MHz

parametric_IF_C8_Q1418_1001 = (200) * u.MHz
parametric_IF_C8_Q1418_1102 = (250) * u.MHz
parametric_IF_C8_Q1418_1120 = (300) * u.MHz

parametric_IF_C8_Q1718_1001 = (350) * u.MHz
parametric_IF_C8_Q1718_1102 = (400) * u.MHz
parametric_IF_C8_Q1718_1120 = (450) * u.MHz

# ---- C3 coupling frequencies (Δ/2) ----

# Q3–Q4
parametric_IF_C3_Q34_1001 = (50) * u.MHz   
parametric_IF_C3_Q34_1102 = (100) * u.MHz  
parametric_IF_C3_Q34_1120 = (150) * u.MHz   

# Q3–Q8
parametric_IF_C3_Q38_1001 = (200) * u.MHz   
parametric_IF_C3_Q38_1102 = (250) * u.MHz  
parametric_IF_C3_Q38_1120 = (300) * u.MHz 

# Q3–Q7 (provided)
parametric_IF_C3_Q37_1001 = (350) * u.MHz 
parametric_IF_C3_Q37_1102 = (400) * u.MHz  
parametric_IF_C3_Q37_1120 = (450) * u.MHz  

# Q4–Q8
parametric_IF_C3_Q48_1001 = (50) * u.MHz 
parametric_IF_C3_Q48_1102 = (100) * u.MHz  
parametric_IF_C3_Q48_1120 = (150) * u.MHz  

# Q4–Q7
parametric_IF_C3_Q47_1001 = (200) * u.MHz  
parametric_IF_C3_Q47_1102 = (250) * u.MHz  
parametric_IF_C3_Q47_1120 = (300) * u.MHz  

# Q7–Q8
parametric_IF_C3_Q78_1001 = (350) * u.MHz 
parametric_IF_C3_Q78_1102 = (400) * u.MHz  
parametric_IF_C3_Q78_1120 = (450) * u.MHz 

# ---- Corrected C5 coupling frequencies (Δ/2) ----

# C5_Q78 (Q7–Q8)
parametric_IF_C5_Q78_1001 = (50) * u.MHz 
parametric_IF_C5_Q78_1102 = (100) * u.MHz   
parametric_IF_C5_Q78_1120 = (150) * u.MHz  

# C5_Q712 (Q7–Q12)
parametric_IF_C5_Q712_1001 = (200) * u.MHz  
parametric_IF_C5_Q712_1102 = (250) * u.MHz  
parametric_IF_C5_Q712_1120 = (300) * u.MHz  

# C5_Q711 (Q7–Q11)
parametric_IF_C5_Q711_1001 = (350) * u.MHz 
parametric_IF_C5_Q711_1102 = (400) * u.MHz 
parametric_IF_C5_Q711_1120 = (450) * u.MHz  

# C5_Q812 (Q8–Q12)
parametric_IF_C5_Q812_1001 = (50) * u.MHz  
parametric_IF_C5_Q812_1102 = (100) * u.MHz  
parametric_IF_C5_Q812_1120 = (150) * u.MHz  

# C5_Q811 (Q8–Q11)
parametric_IF_C5_Q811_1001 = (200) * u.MHz  
parametric_IF_C5_Q811_1102 = (250) * u.MHz  
parametric_IF_C5_Q811_1120 = (300) * u.MHz  

# C5_Q1112 (Q11–Q12)
parametric_IF_C5_Q1112_1001 = (350) * u.MHz  
parametric_IF_C5_Q1112_1102 = (400) * u.MHz  
parametric_IF_C5_Q1112_1120 = (450) * u.MHz  

# ---- C7 coupling frequencies (Δ/2) ----

# Q11–Q12
parametric_IF_C7_Q1112_1001 = (50) * u.MHz 
parametric_IF_C7_Q1112_1102 = (100) * u.MHz 
parametric_IF_C7_Q1112_1120 = (150) * u.MHz 

# Q11–Q16
parametric_IF_C7_Q1116_1001 = (200) * u.MHz  
parametric_IF_C7_Q1116_1102 = (250) * u.MHz   
parametric_IF_C7_Q1116_1120 = (300) * u.MHz   

# Q11–Q15
parametric_IF_C7_Q1115_1001 = (350) * u.MHz 
parametric_IF_C7_Q1115_1102 = (400) * u.MHz   
parametric_IF_C7_Q1115_1120 = (450) * u.MHz  

# Q12–Q16
parametric_IF_C7_Q1216_1001 = (50) * u.MHz   
parametric_IF_C7_Q1216_1102 = (100) * u.MHz   
parametric_IF_C7_Q1216_1120 = (150) * u.MHz   

# Q12–Q15
parametric_IF_C7_Q1215_1001 = (200) * u.MHz   
parametric_IF_C7_Q1215_1102 = (250) * u.MHz   
parametric_IF_C7_Q1215_1120 = (300) * u.MHz    

# Q15–Q16
parametric_IF_C7_Q1516_1001 = (350) * u.MHz   
parametric_IF_C7_Q1516_1102 = (400) * u.MHz   
parametric_IF_C7_Q1516_1120 = (450) * u.MHz  

# ---- C10 coupling frequencies (Δ/2) ----

# C10_Q1516 (Q15–Q16)
parametric_IF_C10_Q1516_1001 = (50) * u.MHz 
parametric_IF_C10_Q1516_1102 = (100) * u.MHz 
parametric_IF_C10_Q1516_1120 = (150) * u.MHz   

# C10_Q1520 (Q15–Q20)
parametric_IF_C10_Q1520_1001 = (200) * u.MHz 
parametric_IF_C10_Q1520_1102 = (250) * u.MHz 
parametric_IF_C10_Q1520_1120 = (300) * u.MHz   

# C10_Q1519 (Q15–Q19)
parametric_IF_C10_Q1519_1001 = (350) * u.MHz 
parametric_IF_C10_Q1519_1102 = (400) * u.MHz 
parametric_IF_C10_Q1519_1120 = (450) * u.MHz   

# C10_Q1620 (Q16–Q20)
parametric_IF_C10_Q1620_1001 = (50) * u.MHz 
parametric_IF_C10_Q1620_1102 = (100) * u.MHz 
parametric_IF_C10_Q1620_1120 = (150) * u.MHz 

# C10_Q1619 (Q16–Q19)
parametric_IF_C10_Q1619_1001 = (200) * u.MHz   
parametric_IF_C10_Q1619_1102 = (250) * u.MHz
parametric_IF_C10_Q1619_1120 = (300) * u.MHz 

# C10_Q1920 (Q19–Q20)
parametric_IF_C10_Q1920_1001 = (350) * u.MHz 
parametric_IF_C10_Q1920_1102 = (400) * u.MHz   
parametric_IF_C10_Q1920_1120 = (450) * u.MHz   

# C2_Q37 (Q3–Q7)
parametric_IF_C2_Q37_1001 = (50) * u.MHz 
parametric_IF_C2_Q37_1102 = (100) * u.MHz   
parametric_IF_C2_Q37_1120 = (150) * u.MHz  

# C2_Q36 (Q3–Q6)
parametric_IF_C2_Q36_1001 = (200) * u.MHz  
parametric_IF_C2_Q36_1102 = (250) * u.MHz   
parametric_IF_C2_Q36_1120 = (300) * u.MHz   

# C2_Q67 (Q6–Q7)
parametric_IF_C2_Q67_1001 = (350) * u.MHz 
parametric_IF_C2_Q67_1102 = (400) * u.MHz   
parametric_IF_C2_Q67_1120 = (450) * u.MHz   

# C9_Q1519 (Q15–Q19)
parametric_IF_C9_Q1519_1001 = (50) * u.MHz 
parametric_IF_C9_Q1519_1102 = (100) * u.MHz 
parametric_IF_C9_Q1519_1120 = (150) * u.MHz 

# C9_Q1415 (Q14–Q15)
parametric_IF_C9_Q1415_1001 = (200) * u.MHz 
parametric_IF_C9_Q1415_1102 = (250) * u.MHz 
parametric_IF_C9_Q1415_1120 = (300) * u.MHz 

# C9_Q1419 (Q14–Q19)
parametric_IF_C9_Q1419_1001 = (350) * u.MHz 
parametric_IF_C9_Q1419_1102 = (400) * u.MHz 
parametric_IF_C9_Q1419_1120 = (450) * u.MHz 


#C1
parametric_const_amp_C1_Q12_1001 = 2.5
parametric_const_amp_C1_Q12_1102 = 2.5
parametric_const_amp_C1_Q12_1120 = 2.5

parametric_const_amp_C1_Q15_1001 = 2.5
parametric_const_amp_C1_Q15_1102 = 2.5
parametric_const_amp_C1_Q15_1120 = 2.5

parametric_const_amp_C1_Q16_1001 = 2.5
parametric_const_amp_C1_Q16_1102 = 2.5
parametric_const_amp_C1_Q16_1120 = 2.5

parametric_const_amp_C1_Q25_1001 = 2.5
parametric_const_amp_C1_Q25_1102 = 2.5
parametric_const_amp_C1_Q25_1120 = 2.5

parametric_const_amp_C1_Q26_1001 = 2.5
parametric_const_amp_C1_Q26_1102 = 2.5
parametric_const_amp_C1_Q26_1120 = 2.5

parametric_const_amp_C1_Q56_1001 = 2.5
parametric_const_amp_C1_Q56_1102 = 2.5
parametric_const_amp_C1_Q56_1120 = 2.5

#C4
parametric_const_amp_C4_Q56_1001 = 2.5
parametric_const_amp_C4_Q56_1102 = 2.5
parametric_const_amp_C4_Q56_1120 = 2.5

parametric_const_amp_C4_Q59_1001 = 2.5
parametric_const_amp_C4_Q59_1102 = 2.5
parametric_const_amp_C4_Q59_1120 = 2.5

parametric_const_amp_C4_Q510_1001 = 2.5
parametric_const_amp_C4_Q510_1102 = 2.5
parametric_const_amp_C4_Q510_1120 = 2.5

parametric_const_amp_C4_Q69_1001 = 2.5
parametric_const_amp_C4_Q69_1102 = 2.5
parametric_const_amp_C4_Q69_1120 = 2.5

parametric_const_amp_C4_Q610_1001 = 2.5
parametric_const_amp_C4_Q610_1102 = 2.5
parametric_const_amp_C4_Q610_1120 = 2.5

parametric_const_amp_C4_Q910_1001 = 2.5
parametric_const_amp_C4_Q910_1102 = 2.5
parametric_const_amp_C4_Q910_1120 = 2.5

#C6
parametric_const_amp_C6_Q910_1001 = 2.5
parametric_const_amp_C6_Q910_1102 = 2.5
parametric_const_amp_C6_Q910_1120 = 2.5

parametric_const_amp_C6_Q913_1001 = 2.5
parametric_const_amp_C6_Q913_1102 = 2.5
parametric_const_amp_C6_Q913_1120 = 2.5

parametric_const_amp_C6_Q914_1001 = 2.5
parametric_const_amp_C6_Q914_1102 = 1.8
parametric_const_amp_C6_Q914_1120 = 2.5

parametric_const_amp_C6_Q1013_1001 = 2.5
parametric_const_amp_C6_Q1013_1102 = 2.5
parametric_const_amp_C6_Q1013_1120 = 2.5

parametric_const_amp_C6_Q1014_1001 = 2.5
parametric_const_amp_C6_Q1014_1102 = 2.5
parametric_const_amp_C6_Q1014_1120 = 2.5

parametric_const_amp_C6_Q1314_1001 = 2.5
parametric_const_amp_C6_Q1314_1102 = 2.5
parametric_const_amp_C6_Q1314_1120 = 2.5

#C8
parametric_const_amp_C8_Q1314_1001 = 2.5
parametric_const_amp_C8_Q1314_1102 = 2.5
parametric_const_amp_C8_Q1314_1120 = 2.5

parametric_const_amp_C8_Q1317_1001 = 2.5
parametric_const_amp_C8_Q1317_1102 = 2.5
parametric_const_amp_C8_Q1317_1120 = 2.5

parametric_const_amp_C8_Q1318_1001 = 2.5
parametric_const_amp_C8_Q1318_1102 = 2.5
parametric_const_amp_C8_Q1318_1120 = 2.5

parametric_const_amp_C8_Q1417_1001 = 2.5
parametric_const_amp_C8_Q1417_1102 = 2.5
parametric_const_amp_C8_Q1417_1120 = 2.5

parametric_const_amp_C8_Q1418_1001 = 2.5
parametric_const_amp_C8_Q1418_1102 = 2.5
parametric_const_amp_C8_Q1418_1120 = 2.5

parametric_const_amp_C8_Q1718_1001 = 2.5
parametric_const_amp_C8_Q1718_1102 = 2.5
parametric_const_amp_C8_Q1718_1120 = 2.5

# ---- C3 amplitudes ----
parametric_const_amp_C3_Q34_1001 = 2.5
parametric_const_amp_C3_Q34_1102 = 2.5
parametric_const_amp_C3_Q34_1120 = 2.5

parametric_const_amp_C3_Q38_1001 = 2.5
parametric_const_amp_C3_Q38_1102 = 2.5
parametric_const_amp_C3_Q38_1120 = 2.5

parametric_const_amp_C3_Q37_1001 = 2.5
parametric_const_amp_C3_Q37_1102 = 2.5
parametric_const_amp_C3_Q37_1120 = 2.5

parametric_const_amp_C3_Q48_1001 = 2.5
parametric_const_amp_C3_Q48_1102 = 2.5
parametric_const_amp_C3_Q48_1120 = 2.5

parametric_const_amp_C3_Q47_1001 = 2.5
parametric_const_amp_C3_Q47_1102 = 2.5
parametric_const_amp_C3_Q47_1120 = 2.5

parametric_const_amp_C3_Q78_1001 = 2.5
parametric_const_amp_C3_Q78_1102 = 2.5
parametric_const_amp_C3_Q78_1120 = 2.5

# ---- C5 amplitudes ----
parametric_const_amp_C5_Q78_1001 = 2.5
parametric_const_amp_C5_Q78_1102 = 2.5
parametric_const_amp_C5_Q78_1120 = 2.5

parametric_const_amp_C5_Q712_1001 = 2.5
parametric_const_amp_C5_Q712_1102 = 2.5
parametric_const_amp_C5_Q712_1120 = 2.5

parametric_const_amp_C5_Q711_1001 = 2.5
parametric_const_amp_C5_Q711_1102 = 2.5
parametric_const_amp_C5_Q711_1120 = 2.5

parametric_const_amp_C5_Q812_1001 = 2.5
parametric_const_amp_C5_Q812_1102 = 2.5
parametric_const_amp_C5_Q812_1120 = 2.5

parametric_const_amp_C5_Q811_1001 = 2.5
parametric_const_amp_C5_Q811_1102 = 2.5
parametric_const_amp_C5_Q811_1120 = 2.5

parametric_const_amp_C5_Q1112_1001 = 2.5
parametric_const_amp_C5_Q1112_1102 = 2.5
parametric_const_amp_C5_Q1112_1120 = 2.5

# ---- C7 amplitudes ----
parametric_const_amp_C7_Q1112_1001 = 2.5
parametric_const_amp_C7_Q1112_1102 = 2.5
parametric_const_amp_C7_Q1112_1120 = 2.5

parametric_const_amp_C7_Q1116_1001 = 2.5
parametric_const_amp_C7_Q1116_1102 = 2.5
parametric_const_amp_C7_Q1116_1120 = 2.5

parametric_const_amp_C7_Q1115_1001 = 2.5
parametric_const_amp_C7_Q1115_1102 = 2.5
parametric_const_amp_C7_Q1115_1120 = 2.5

parametric_const_amp_C7_Q1216_1001 = 2.5
parametric_const_amp_C7_Q1216_1102 = 2.5
parametric_const_amp_C7_Q1216_1120 = 2.5

parametric_const_amp_C7_Q1215_1001 = 2.5
parametric_const_amp_C7_Q1215_1102 = 2.5
parametric_const_amp_C7_Q1215_1120 = 2.5

parametric_const_amp_C7_Q1516_1001 = 2.5
parametric_const_amp_C7_Q1516_1102 = 2.5
parametric_const_amp_C7_Q1516_1120 = 2.5

# ---- C10 amplitudes ----
parametric_const_amp_C10_Q1516_1001 = 2.5 
parametric_const_amp_C10_Q1516_1102 = 2.5
parametric_const_amp_C10_Q1516_1120 = 2.5

parametric_const_amp_C10_Q1520_1001 = 2.5
parametric_const_amp_C10_Q1520_1102 = 2.5
parametric_const_amp_C10_Q1520_1120 = 2.5

parametric_const_amp_C10_Q1519_1001 = 2.5
parametric_const_amp_C10_Q1519_1102 = 2.5
parametric_const_amp_C10_Q1519_1120 = 2.5

parametric_const_amp_C10_Q1620_1001 = 2.5
parametric_const_amp_C10_Q1620_1102 = 2.5
parametric_const_amp_C10_Q1620_1120 = 2.5

parametric_const_amp_C10_Q1619_1001 = 2.5
parametric_const_amp_C10_Q1619_1102 = 2.5
parametric_const_amp_C10_Q1619_1120 = 2.5

parametric_const_amp_C10_Q1920_1001 = 2.5
parametric_const_amp_C10_Q1920_1102 = 2.5
parametric_const_amp_C10_Q1920_1120 = 2.5

parametric_const_amp_C2_Q37_1001 = 2.5
parametric_const_amp_C2_Q37_1102 = 2.5
parametric_const_amp_C2_Q37_1120 = 2.5

parametric_const_amp_C2_Q36_1001 = 2.5
parametric_const_amp_C2_Q36_1102 = 2.5 
parametric_const_amp_C2_Q36_1120 = 2.5 

parametric_const_amp_C2_Q67_1001 = 2.5
parametric_const_amp_C2_Q67_1102 = 2.5 
parametric_const_amp_C2_Q67_1120 = 2.5 

parametric_const_amp_C9_Q1519_1001 = 2.5
parametric_const_amp_C9_Q1519_1102 = 2.5
parametric_const_amp_C9_Q1519_1120 = 2.5

parametric_const_amp_C9_Q1415_1001 = 2.5
parametric_const_amp_C9_Q1415_1102 = 2.5
parametric_const_amp_C9_Q1415_1120 = 2.5

parametric_const_amp_C9_Q1419_1001 = 2.5
parametric_const_amp_C9_Q1419_1102 = 2.5
parametric_const_amp_C9_Q1419_1120 = 2.5


#############################################
#            Ringup Coupler Pulse           #
#############################################



rise_len_C12_1102 = 12            
mid_len_C12_1102  = 88       
fall_len_C12_1102 = 12         
amp_flux_C12_1102 = 1.6           
total_len_C12_1102 = rise_len_C12_1102 + mid_len_C12_1102 + fall_len_C12_1102

rise_wf = amp_flux_C12_1102 * (np.sin(np.linspace(-np.pi/2, np.pi/2, rise_len_C12_1102))/2) + amp_flux_C12_1102/2   # 0→amp 
mid_wf  = amp_flux_C12_1102 * np.ones(mid_len_C12_1102)                                  # const amp
fall_wf = amp_flux_C12_1102 * (np.sin(np.linspace(np.pi/2, 3*np.pi/2, fall_len_C12_1102))/2) + amp_flux_C12_1102/2  # amp→0 

rise_up_flux_samples = np.concatenate([rise_wf, mid_wf, fall_wf])



parametric_ringup_amp_C8_Q1317_1102 = 1.6

parametric_ringup_rise_len = 12 
parametric_ringup_mid_len = 88 
parametric_ringup_fall_len = 12  
parametric_ringup_total_len = parametric_ringup_rise_len + parametric_ringup_mid_len + parametric_ringup_fall_len

parametric_ringup_rise_len_1102 = parametric_ringup_rise_len
parametric_ringup_mid_len_1102 =parametric_ringup_mid_len
parametric_ringup_fall_len_1102 = parametric_ringup_fall_len
parametric_ringup_total_len_1102 = parametric_ringup_total_len
parametric_ringup_rise_len_1120 = parametric_ringup_rise_len
parametric_ringup_mid_len_1120 =parametric_ringup_mid_len
parametric_ringup_fall_len_1120 = parametric_ringup_fall_len
parametric_ringup_total_len_1120 = parametric_ringup_total_len
parametric_ringup_rise_len_1001 = parametric_ringup_rise_len
parametric_ringup_mid_len_1001 =parametric_ringup_mid_len
parametric_ringup_fall_len_1001 = parametric_ringup_fall_len
parametric_ringup_total_len_1001 = parametric_ringup_total_len



parametric_ringup_rise_len_C8_Q1317_1102 = parametric_ringup_rise_len_1102
parametric_ringup_mid_len_C8_Q1317_1102 = parametric_ringup_mid_len_1102
parametric_ringup_fall_len_C8_Q1317_1102 = parametric_ringup_fall_len_1102
parametric_ringup_total_len_C8_Q1317_1102 = parametric_ringup_total_len_1102

rise_wf_C8_Q1317_1102 = parametric_ringup_amp_C8_Q1317_1102 * (np.sin(np.linspace(-np.pi/2, np.pi/2, rise_len_C12_1102))/2) + amp_flux_C12_1102/2   
mid_wf_C8_Q1317_1102  = parametric_ringup_amp_C8_Q1317_1102 * np.ones(mid_len_C12_1102)                                  
fall_wf_C8_Q1317_1102 = parametric_ringup_amp_C8_Q1317_1102 * (np.sin(np.linspace(np.pi/2, 3*np.pi/2, fall_len_C12_1102))/2) + amp_flux_C12_1102/2  
ringup_wf_C8_Q1317_1102 = np.concatenate([rise_wf_C8_Q1317_1102, mid_wf_C8_Q1317_1102, fall_wf_C8_Q1317_1102])

#############################################
#                Test Sine Pulse            #
#############################################
pulse_time=np.arange(const_len)
sine_samples = np.cos(2 * np.pi * frequency_sine_Hz * pulse_time * 1e-9).tolist()


#############################################
#                Resonators                 #
#############################################
resonator_LO_1 = 7.0 * u.GHz 
resonator_LO_2 = 7.0 * u.GHz 
resonator_LO_3 = 7.0 * u.GHz 
# Resonators IF



resonator_IF_q1 = (50) * u.MHz 
resonator_IF_q2 = (60) * u.MHz 
resonator_IF_q3 = (70) * u.MHz
resonator_IF_q4 = (80) * u.MHz 
resonator_IF_q5 = (90) * u.MHz 
resonator_IF_q6 = (100) * u.MHz 
resonator_IF_q7 = (110) * u.MHz 
resonator_IF_q8 = (120) * u.MHz 
resonator_IF_q9 = (130) * u.MHz 
resonator_IF_q10 = (140) * u.MHz 
resonator_IF_q11 = (150) * u.MHz 
resonator_IF_q12 = (160) * u.MHz 
resonator_IF_q13 = (170) * u.MHz 
resonator_IF_q14 = (180) * u.MHz 
resonator_IF_q15 = (190) * u.MHz
resonator_IF_q16 = (200) * u.MHz
resonator_IF_q17 = (210) * u.MHz 

resonator_IF_q18 = (220) * u.MHz 
resonator_IF_q19 = (230) * u.MHz
resonator_IF_q20 = (240) * u.MHz
resonator_IF_q_C6 = (250) * u.MHz 

resonator_power = -8 


# Note: amplitudes can be -1..1 and are scaled up to `qubit_power` at amp=1
# Readout pulse parameters
readout_len = 2000 

readout_amp_q1 = 0.2
readout_amp_q2 = 0.3
readout_amp_q3 = 0.4
readout_amp_q4 = 0.5
readout_amp_q5 = 0.6
readout_amp_q6 = 0.7 
readout_amp_q7 = 0.8 
readout_amp_q8 = 0.9 
readout_amp_q9 = 0.1
readout_amp_q10 = 0.2
readout_amp_q11 = 0.3 
readout_amp_q12 = 0.4 
readout_amp_q13 = 0.5
readout_amp_q14 = 0.6 
readout_amp_q15 = 0.7 
readout_amp_q16 = 0.8 
readout_amp_q17 = 0.9
readout_amp_q18 = 1.0
readout_amp_q19 = 0.1 
readout_amp_q20 = 0.2
readout_amp_q_C6 = 0.3



# TOF and depletion time

time_of_flight = 28 + 348 
time_of_flight = 28 + 348 -12 
depletion_time = 3 * u.us

opt_weights = False

if opt_weights:
    weights_q1 = np.load("optimal_weights_q1.npz")
    opt_weights_real_q1 = [(x, weights_q1["division_length"] * 4) for x in weights_q1["weights_real"]]
    opt_weights_minus_imag_q1 = [(x, weights_q1["division_length"] * 4) for x in weights_q1["weights_minus_imag"]]
    opt_weights_imag_q1 = [(x, weights_q1["division_length"] * 4) for x in weights_q1["weights_imag"]]
    opt_weights_minus_real_q1 = [(x, weights_q1["division_length"] * 4) for x in weights_q1["weights_minus_real"]]

    weights_q2 = np.load("optimal_weights_q2.npz")
    opt_weights_real_q2 = [(x, weights_q2["division_length"] * 4) for x in weights_q2["weights_real"]]
    opt_weights_minus_imag_q2 = [(x, weights_q2["division_length"] * 4) for x in weights_q2["weights_minus_imag"]]
    opt_weights_imag_q2 = [(x, weights_q2["division_length"] * 4) for x in weights_q2["weights_imag"]]
    opt_weights_minus_real_q2 = [(x, weights_q2["division_length"] * 4) for x in weights_q2["weights_minus_real"]]

    weights_q3 = np.load("optimal_weights_q3.npz")
    opt_weights_real_q3 = [(x, weights_q3["division_length"] * 4) for x in weights_q3["weights_real"]]
    opt_weights_minus_imag_q3 = [(x, weights_q3["division_length"] * 4) for x in weights_q3["weights_minus_imag"]]
    opt_weights_imag_q3 = [(x, weights_q3["division_length"] * 4) for x in weights_q3["weights_imag"]]
    opt_weights_minus_real_q3 = [(x, weights_q3["division_length"] * 4) for x in weights_q3["weights_minus_real"]]

    weights_q4 = np.load("optimal_weights_q4.npz")
    opt_weights_real_q4 = [(x, weights_q4["division_length"] * 4) for x in weights_q4["weights_real"]]
    opt_weights_minus_imag_q4 = [(x, weights_q4["division_length"] * 4) for x in weights_q4["weights_minus_imag"]]
    opt_weights_imag_q4 = [(x, weights_q4["division_length"] * 4) for x in weights_q4["weights_imag"]]
    opt_weights_minus_real_q4 = [(x, weights_q4["division_length"] * 4) for x in weights_q4["weights_minus_real"]]

    weights_q5 = np.load("optimal_weights_q5.npz")
    opt_weights_real_q5 = [(x, weights_q5["division_length"] * 4) for x in weights_q5["weights_real"]]
    opt_weights_minus_imag_q5 = [(x, weights_q5["division_length"] * 4) for x in weights_q5["weights_minus_imag"]]
    opt_weights_imag_q5 = [(x, weights_q5["division_length"] * 4) for x in weights_q5["weights_imag"]]
    opt_weights_minus_real_q5 = [(x, weights_q5["division_length"] * 4) for x in weights_q5["weights_minus_real"]]

    weights_q6 = np.load("optimal_weights_q6.npz")
    opt_weights_real_q6 = [(x, weights_q6["division_length"] * 4) for x in weights_q6["weights_real"]]
    opt_weights_minus_imag_q6 = [(x, weights_q6["division_length"] * 4) for x in weights_q6["weights_minus_imag"]]
    opt_weights_imag_q6 = [(x, weights_q6["division_length"] * 4) for x in weights_q6["weights_imag"]]
    opt_weights_minus_real_q6 = [(x, weights_q6["division_length"] * 4) for x in weights_q6["weights_minus_real"]]

    weights_q7 = np.load("optimal_weights_q7.npz")
    opt_weights_real_q7 = [(x, weights_q7["division_length"] * 4) for x in weights_q7["weights_real"]]
    opt_weights_minus_imag_q7 = [(x, weights_q7["division_length"] * 4) for x in weights_q7["weights_minus_imag"]]
    opt_weights_imag_q7 = [(x, weights_q7["division_length"] * 4) for x in weights_q7["weights_imag"]]
    opt_weights_minus_real_q7 = [(x, weights_q7["division_length"] * 4) for x in weights_q7["weights_minus_real"]]

    weights_q8 = np.load("optimal_weights_q8.npz")
    opt_weights_real_q8 = [(x, weights_q8["division_length"] * 4) for x in weights_q8["weights_real"]]
    opt_weights_minus_imag_q8 = [(x, weights_q8["division_length"] * 4) for x in weights_q8["weights_minus_imag"]]
    opt_weights_imag_q8 = [(x, weights_q8["division_length"] * 4) for x in weights_q8["weights_imag"]]
    opt_weights_minus_real_q8 = [(x, weights_q8["division_length"] * 4) for x in weights_q8["weights_minus_real"]]

    weights_q9 = np.load("optimal_weights_q9.npz")
    opt_weights_real_q9 = [(x, weights_q9["division_length"] * 4) for x in weights_q9["weights_real"]]
    opt_weights_minus_imag_q9 = [(x, weights_q9["division_length"] * 4) for x in weights_q9["weights_minus_imag"]]
    opt_weights_imag_q9 = [(x, weights_q9["division_length"] * 4) for x in weights_q9["weights_imag"]]
    opt_weights_minus_real_q9 = [(x, weights_q9["division_length"] * 4) for x in weights_q9["weights_minus_real"]]

    weights_q10 = np.load("optimal_weights_q10.npz")
    opt_weights_real_q10 = [(x, weights_q10["division_length"] * 4) for x in weights_q10["weights_real"]]
    opt_weights_minus_imag_q10 = [(x, weights_q10["division_length"] * 4) for x in weights_q10["weights_minus_imag"]]
    opt_weights_imag_q10 = [(x, weights_q10["division_length"] * 4) for x in weights_q10["weights_imag"]]
    opt_weights_minus_real_q10 = [(x, weights_q10["division_length"] * 4) for x in weights_q10["weights_minus_real"]]

    weights_q11 = np.load("optimal_weights_q11.npz")
    opt_weights_real_q11 = [(x, weights_q11["division_length"] * 4) for x in weights_q11["weights_real"]]
    opt_weights_minus_imag_q11 = [(x, weights_q11["division_length"] * 4) for x in weights_q11["weights_minus_imag"]]
    opt_weights_imag_q11 = [(x, weights_q11["division_length"] * 4) for x in weights_q11["weights_imag"]]
    opt_weights_minus_real_q11 = [(x, weights_q11["division_length"] * 4) for x in weights_q11["weights_minus_real"]]

    weights_q12 = np.load("optimal_weights_q12.npz")
    opt_weights_real_q12 = [(x, weights_q12["division_length"] * 4) for x in weights_q12["weights_real"]]
    opt_weights_minus_imag_q12 = [(x, weights_q12["division_length"] * 4) for x in weights_q12["weights_minus_imag"]]
    opt_weights_imag_q12 = [(x, weights_q12["division_length"] * 4) for x in weights_q12["weights_imag"]]
    opt_weights_minus_real_q12 = [(x, weights_q12["division_length"] * 4) for x in weights_q12["weights_minus_real"]]

    weights_q13 = np.load("optimal_weights_q13.npz")
    opt_weights_real_q13 = [(x, weights_q13["division_length"] * 4) for x in weights_q13["weights_real"]]
    opt_weights_minus_imag_q13 = [(x, weights_q13["division_length"] * 4) for x in weights_q13["weights_minus_imag"]]
    opt_weights_imag_q13 = [(x, weights_q13["division_length"] * 4) for x in weights_q13["weights_imag"]]
    opt_weights_minus_real_q13 = [(x, weights_q13["division_length"] * 4) for x in weights_q13["weights_minus_real"]]

    weights_q14 = np.load("optimal_weights_q14.npz")
    opt_weights_real_q14 = [(x, weights_q14["division_length"] * 4) for x in weights_q14["weights_real"]]
    opt_weights_minus_imag_q14 = [(x, weights_q14["division_length"] * 4) for x in weights_q14["weights_minus_imag"]]
    opt_weights_imag_q14 = [(x, weights_q14["division_length"] * 4) for x in weights_q14["weights_imag"]]
    opt_weights_minus_real_q14 = [(x, weights_q14["division_length"] * 4) for x in weights_q14["weights_minus_real"]]

    weights_q15 = np.load("optimal_weights_q15.npz")
    opt_weights_real_q15 = [(x, weights_q15["division_length"] * 4) for x in weights_q15["weights_real"]]
    opt_weights_minus_imag_q15 = [(x, weights_q15["division_length"] * 4) for x in weights_q15["weights_minus_imag"]]
    opt_weights_imag_q15 = [(x, weights_q15["division_length"] * 4) for x in weights_q15["weights_imag"]]
    opt_weights_minus_real_q15 = [(x, weights_q15["division_length"] * 4) for x in weights_q15["weights_minus_real"]]

    weights_q16 = np.load("optimal_weights_q16.npz")
    opt_weights_real_q16 = [(x, weights_q16["division_length"] * 4) for x in weights_q16["weights_real"]]
    opt_weights_minus_imag_q16 = [(x, weights_q16["division_length"] * 4) for x in weights_q16["weights_minus_imag"]]
    opt_weights_imag_q16 = [(x, weights_q16["division_length"] * 4) for x in weights_q16["weights_imag"]]
    opt_weights_minus_real_q16 = [(x, weights_q16["division_length"] * 4) for x in weights_q16["weights_minus_real"]]

    weights_q17 = np.load("optimal_weights_q17.npz")
    opt_weights_real_q17 = [(x, weights_q17["division_length"] * 4) for x in weights_q17["weights_real"]]
    opt_weights_minus_imag_q17 = [(x, weights_q17["division_length"] * 4) for x in weights_q17["weights_minus_imag"]]
    opt_weights_imag_q17 = [(x, weights_q17["division_length"] * 4) for x in weights_q17["weights_imag"]]
    opt_weights_minus_real_q17 = [(x, weights_q17["division_length"] * 4) for x in weights_q17["weights_minus_real"]]

    weights_q18 = np.load("optimal_weights_q18.npz")
    opt_weights_real_q18 = [(x, weights_q18["division_length"] * 4) for x in weights_q18["weights_real"]]
    opt_weights_minus_imag_q18 = [(x, weights_q18["division_length"] * 4) for x in weights_q18["weights_minus_imag"]]
    opt_weights_imag_q18 = [(x, weights_q18["division_length"] * 4) for x in weights_q18["weights_imag"]]
    opt_weights_minus_real_q18 = [(x, weights_q18["division_length"] * 4) for x in weights_q18["weights_minus_real"]]

    weights_q19 = np.load("optimal_weights_q19.npz")
    opt_weights_real_q19 = [(x, weights_q19["division_length"] * 4) for x in weights_q19["weights_real"]]
    opt_weights_minus_imag_q19 = [(x, weights_q19["division_length"] * 4) for x in weights_q19["weights_minus_imag"]]
    opt_weights_imag_q19 = [(x, weights_q19["division_length"] * 4) for x in weights_q19["weights_imag"]]
    opt_weights_minus_real_q19 = [(x, weights_q19["division_length"] * 4) for x in weights_q19["weights_minus_real"]]

    weights_q20 = np.load("optimal_weights_q20.npz")
    opt_weights_real_q20 = [(x, weights_q20["division_length"] * 4) for x in weights_q20["weights_real"]]
    opt_weights_minus_imag_q20 = [(x, weights_q20["division_length"] * 4) for x in weights_q20["weights_minus_imag"]]
    opt_weights_imag_q20 = [(x, weights_q20["division_length"] * 4) for x in weights_q20["weights_imag"]]
    opt_weights_minus_real_q20 = [(x, weights_q20["division_length"] * 4) for x in weights_q20["weights_minus_real"]]

    weights_q_C6 = np.load("optimal_weights_q_C6.npz")
    opt_weights_real_q_C6 = [(x, weights_q_C6["division_length"] * 4) for x in weights_q_C6["weights_real"]]
    opt_weights_minus_imag_q_C6 = [(x, weights_q_C6["division_length"] * 4) for x in weights_q_C6["weights_minus_imag"]]
    opt_weights_imag_q_C6 = [(x, weights_q_C6["division_length"] * 4) for x in weights_q_C6["weights_imag"]]
    opt_weights_minus_real_q_C6 = [(x, weights_q_C6["division_length"] * 4) for x in weights_q_C6["weights_minus_real"]]



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

    opt_weights_real_q9 = [(1.0, readout_len)]
    opt_weights_minus_imag_q9 = [(0.0, readout_len)]
    opt_weights_imag_q9 = [(0.0, readout_len)]
    opt_weights_minus_real_q9 = [(-1.0, readout_len)]

    opt_weights_real_q10 = [(1.0, readout_len)]
    opt_weights_minus_imag_q10 = [(0.0, readout_len)]
    opt_weights_imag_q10 = [(0.0, readout_len)]
    opt_weights_minus_real_q10 = [(-1.0, readout_len)]

    opt_weights_real_q11 = [(1.0, readout_len)]
    opt_weights_minus_imag_q11 = [(0.0, readout_len)]
    opt_weights_imag_q11 = [(0.0, readout_len)]
    opt_weights_minus_real_q11 = [(-1.0, readout_len)]

    opt_weights_real_q12 = [(1.0, readout_len)]
    opt_weights_minus_imag_q12 = [(0.0, readout_len)]
    opt_weights_imag_q12 = [(0.0, readout_len)]
    opt_weights_minus_real_q12 = [(-1.0, readout_len)]

    opt_weights_real_q13 = [(1.0, readout_len)]
    opt_weights_minus_imag_q13 = [(0.0, readout_len)]
    opt_weights_imag_q13 = [(0.0, readout_len)]
    opt_weights_minus_real_q13 = [(-1.0, readout_len)]

    opt_weights_real_q14 = [(1.0, readout_len)]
    opt_weights_minus_imag_q14 = [(0.0, readout_len)]
    opt_weights_imag_q14 = [(0.0, readout_len)]
    opt_weights_minus_real_q14 = [(-1.0, readout_len)]

    opt_weights_real_q15 = [(1.0, readout_len)]
    opt_weights_minus_imag_q15 = [(0.0, readout_len)]
    opt_weights_imag_q15 = [(0.0, readout_len)]
    opt_weights_minus_real_q15 = [(-1.0, readout_len)]

    opt_weights_real_q16 = [(1.0, readout_len)]
    opt_weights_minus_imag_q16 = [(0.0, readout_len)]
    opt_weights_imag_q16 = [(0.0, readout_len)]
    opt_weights_minus_real_q16 = [(-1.0, readout_len)]

    opt_weights_real_q17 = [(1.0, readout_len)]
    opt_weights_minus_imag_q17 = [(0.0, readout_len)]
    opt_weights_imag_q17 = [(0.0, readout_len)]
    opt_weights_minus_real_q17 = [(-1.0, readout_len)]

    opt_weights_real_q18 = [(1.0, readout_len)]
    opt_weights_minus_imag_q18 = [(0.0, readout_len)]
    opt_weights_imag_q18 = [(0.0, readout_len)]
    opt_weights_minus_real_q18 = [(-1.0, readout_len)]

    opt_weights_real_q19 = [(1.0, readout_len)]
    opt_weights_minus_imag_q19 = [(0.0, readout_len)]
    opt_weights_imag_q19 = [(0.0, readout_len)]
    opt_weights_minus_real_q19 = [(-1.0, readout_len)]

    opt_weights_real_q20 = [(1.0, readout_len)]
    opt_weights_minus_imag_q20 = [(0.0, readout_len)]
    opt_weights_imag_q20 = [(0.0, readout_len)]
    opt_weights_minus_real_q20 = [(-1.0, readout_len)]

    opt_weights_real_q_C6 = [(1.0, readout_len)]
    opt_weights_minus_imag_q_C6 = [(0.0, readout_len)]
    opt_weights_imag_q_C6 = [(0.0, readout_len)]
    opt_weights_minus_real_q_C6 = [(-1.0, readout_len)]


# state discrimination
rotation_angle_q1 = ((10)/ 180) * np.pi
rotation_angle_q2 = ((20)/ 180) * np.pi
rotation_angle_q3 = ((30) / 180) * np.pi
rotation_angle_q4 = ((40) / 180) * np.pi
rotation_angle_q5 = ((50) / 180) * np.pi
rotation_angle_q6 = ((60) / 180) * np.pi
rotation_angle_q7 = ((70) / 180) * np.pi
rotation_angle_q8 = ((80) / 180) * np.pi
rotation_angle_q9 = (90 / 180) * np.pi
rotation_angle_q10 = (100 / 180) * np.pi
rotation_angle_q11 = ((110) / 180) * np.pi
rotation_angle_q12 = ((120) / 180) * np.pi
rotation_angle_q13 = ((130) / 180) * np.pi
rotation_angle_q14 = ((140) / 180) * np.pi
rotation_angle_q15 = ((150) / 180) * np.pi
rotation_angle_q16 = ((160) / 180) * np.pi
rotation_angle_q17 = (170 / 180) * np.pi
rotation_angle_q18 = ((180) / 180) * np.pi
rotation_angle_q19 = ((190) / 180) * np.pi
rotation_angle_q20 = ((200) / 180) * np.pi
rotation_angle_q_C6 = ((210) / 180) * np.pi

ge_threshold_q1 = 1e-04
ge_threshold_q2 = 2e-04
ge_threshold_q3 = 3e-04
ge_threshold_q4 = 4e-04
ge_threshold_q5 = 5e-04
ge_threshold_q6 = 6e-04
ge_threshold_q7 = 7e-04
ge_threshold_q8 = 8e-04
ge_threshold_q9 = 9e-04
ge_threshold_q10 = 1e-03
ge_threshold_q11 = 1.1e-03
ge_threshold_q12 = 1.2e-03
ge_threshold_q13 = 1.3e-03
ge_threshold_q14 = 1.4e-03
ge_threshold_q15 =  1.5e-03
ge_threshold_q16 = 1.6e-03
ge_threshold_q17 = 1.7e-03
ge_threshold_q18 = 1.8e-03
ge_threshold_q19 = 1.9e-03
ge_threshold_q20 = 2.0e-03
ge_threshold_q_C6 = 2.1e-03



#############################################
#                  Config                   #
#############################################
config = {
    "version": 1,
    "controllers": {
        con: {
            "type": "opx1000",
            "fems": {
                mw_fem1: {
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
                        # Resonator 2
                        1: {
                            "band": 3, #2
                            "full_scale_power_dbm": resonator_power,
                            "upconverters": {1: {"frequency": resonator_LO_2}},
                            # "upconverters": {1: {"frequency": resonator_LO_1_1}},
                            # "upconverters": {2: {"frequency": resonator_LO_1_2}},
                        },
                        # Qubit XY1
                        # 2: {
                        #     "band": 2,
                        #     "full_scale_power_dbm": qubit_power,
                        #     "upconverters": {1: {"frequency": qubit_LO_q1}},
                        # },
                        
                        2: {
                            "band": 2,
                            "full_scale_power_dbm": qubit_power,
                            "upconverters": {1: {"frequency": qubit_LO_q3}},
                        },
                        # XY8 
                        # 3: {
                        #     "band": 2,
                        #     "full_scale_power_dbm": qubit_power,
                        #     "upconverters": {1: {"frequency": qubit_LO_q7}},
                        # },

                        3: {
                            "band": 2,
                            "full_scale_power_dbm": qubit_power,
                            "upconverters": {1: {"frequency": qubit_LO_q16}},
                        },


                        # Qubit  XY4
                        # 4: {
                        #     "band": 2,
                        #     "full_scale_power_dbm": qubit_power,
                        #     "upconverters": {1: {"frequency": qubit_LO_q13}},
                        # },
                        4: {
                            "band": 2,
                            "full_scale_power_dbm": qubit_power,
                            "upconverters": {1: {"frequency": qubit_LO_q8}},
                        },

                        # Qubit  XY5
                        # 5: {
                        #     "band": 2,
                        #     "full_scale_power_dbm": qubit_power,
                        #     "upconverters": {1: {"frequency": qubit_LO_q17}},
                        # },
                        5: {
                            "band": 2,
                            "full_scale_power_dbm": qubit_power,
                            "upconverters": {1: {"frequency": qubit_LO_q11}},
                        },

                        # Qubit  XY6
                        # 6: {
                        #     "band": 2,
                        #     "full_scale_power_dbm": qubit_power,
                        #     "upconverters": {1: {"frequency": qubit_LO_q18}},
                        # },
                        6: {
                            "band": 2,
                            "full_scale_power_dbm": qubit_power,
                            "upconverters": {1: {"frequency": qubit_LO_q12}},
                        },



                        # Qubit  XY7
                        # 7: {
                        #     "band": 2,
                        #     "full_scale_power_dbm": qubit_power,
                        #     "upconverters": {1: {"frequency": qubit_LO_q6}},
                        # },

                        7: {
                            "band": 2,
                            "full_scale_power_dbm": qubit_power,
                            "upconverters": {1: {"frequency": qubit_LO_q15}},
                        },
                        # resonator 3
                        8: {
                            "band": 3,
                            "full_scale_power_dbm": resonator_power,
                            "upconverters": {1: {"frequency": resonator_LO_3}},
                        },
                    },
                    "digital_outputs": {},
                    "analog_inputs": {
                        1: {"band": 3, "downconverter_frequency": resonator_LO_2, "gain_db": 20},  # for down-conversion in1 for resonator 2
                        # 2: {"band": 2, "downconverter_frequency": resonator_LO, "gain_db": 20}, #Harry change the "gain_db" to 10, the origin number is 20
                        2: {"band": 3, "downconverter_frequency": resonator_LO_3, "gain_db": 20},  # for down-conversion in2 for resonator 3
                    },
                },
                mw_fem2: {
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
                        # Qubit  XY2
                        # 1: {
                        #     "band": 2,
                        #     "full_scale_power_dbm": qubit_power,
                        #     "upconverters": {1: {"frequency": qubit_LO_q5}},
                        # },

                        1: {
                            "band": 2,
                            "full_scale_power_dbm": qubit_power,
                            "upconverters": {1: {"frequency": qubit_LO_q4}},
                        },
                        
                        # Qubit XY9
                        # 2: {
                        #     "band": 2,
                        #     "full_scale_power_dbm": qubit_power,
                        #     "upconverters": {1: {"frequency": qubit_LO_q10}},
                        # },
                        2: {
                            "band": 2,
                            "full_scale_power_dbm": qubit_power,
                            "upconverters": {1: {"frequency": qubit_LO_q19}},
                        },

                        # Qubit XY10
                        # 3: {
                        #     "band": 2,
                        #     "full_scale_power_dbm": qubit_power,
                        #     "upconverters": {1: {"frequency": qubit_LO_q14}},
                        # },
                        3: {
                            "band": 2,
                            "full_scale_power_dbm": qubit_power,
                            "upconverters": {1: {"frequency": qubit_LO_q20}},
                        },

                    },
                    "digital_outputs": {},
                    "analog_inputs": {
                        1: {"band": 2, "downconverter_frequency": resonator_LO_1},  # for down-conversion
                    },
                },
                mw_fem3: {
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
                        # Qubit  XY3
                        # 1: {
                        #     "band": 2,
                        #     "full_scale_power_dbm": qubit_power,
                        #     "upconverters": {1: {"frequency": qubit_LO_q9}},
                        # },
                        1: {
                            "band": 2,
                            "full_scale_power_dbm": qubit_power,
                            "upconverters": {1: {"frequency": qubit_LO_q7}},
                        },

                        # # Qubit 0 XY
                        # 2: {
                        #     "band": 2,
                        #     "full_scale_power_dbm": qubit_power,
                        #     "upconverters": {1: {"frequency": qubit_LO_q3}},
                        # },
                        # # Qubit 0 XY
                        # 3: {
                        #     "band": 2,
                        #     "full_scale_power_dbm": qubit_power,
                        #     "upconverters": {1: {"frequency": qubit_LO_q3}},
                        # },
                        # # osc
                        # 8: {
                        #     "band": 1,
                        #     "full_scale_power_dbm": osc_power,
                        #     "upconverters": {1: {"frequency": osc_LO}},
                        # },
                    },
                    "digital_outputs": {},
                    "analog_inputs": {
                        1: {"band": 2, "downconverter_frequency": resonator_LO_1},  # for down-conversion
                    },
                },
                lf_fem1: {
                    "type": "LF",
                    "analog_outputs": {
                        # C1 flux line
                        1: {
                            "offset": max_frequency_point1,
                            # The "output_mode" can be used to tailor the max voltage and frequency bandwidth, i.e.,
                            #   "direct":    1Vpp (-0.5V to 0.5V), 750MHz bandwidth (default)
                            #   "amplified": 5Vpp (-2.5V to 2.5V), 330MHz bandwidth
                            # Note, 'offset' takes absolute values, e.g., if in amplified mode and want to output 2.0 V, then set "offset": 2.0
                            "output_mode": "amplified",
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
                            "delay": 161,
                        },
                        # C5 flux line
                        2: {
                            "offset": 0, 
                            # "offset": max_frequency_point2,
                            "output_mode": "amplified",
                            "sampling_rate": sampling_rate,
                            "upsampling_mode": "mw",
                            "delay": 161, #173, changed 05262025
                        },
                        
                        # mix DC and IF pulse test
                        3: {
                            "offset": max_frequency_point2,
                            "output_mode": "amplified",
                            "sampling_rate": sampling_rate,
                            "upsampling_mode": "pulse",
                            "delay": 161,
                        },

                        # C3 flux line
                        4: {
                            "offset": 0, 
                            "output_mode": "amplified",
                            "sampling_rate": sampling_rate,
                            "upsampling_mode": "mw",
                            "delay": 161,
                        }
                    },
                    "digital_outputs": {
                        1: {},
                    },
                },
                lf_fem2: {
                    "type": "LF",
                    "analog_outputs": {
                        # C7 flux line
                        1: {
                            "offset": 0, 
                            # "offset": max_frequency_point1,
                            # The "output_mode" can be used to tailor the max voltage and frequency bandwidth, i.e.,
                            #   "direct":    1Vpp (-0.5V to 0.5V), 750MHz bandwidth (default)
                            #   "amplified": 5Vpp (-2.5V to 2.5V), 330MHz bandwidth
                            # Note, 'offset' takes absolute values, e.g., if in amplified mode and want to output 2.0 V, then set "offset": 2.0
                            "output_mode": "amplified",
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
                            "delay": 161,
                        },
                        # C10 flux line
                        2: {
                            "offset": 0, 
                            "output_mode": "amplified",
                            "sampling_rate": sampling_rate,
                            "upsampling_mode": "mw",
                            "delay": 161,
                        },
                    },
                    "digital_outputs": {
                        1: {},
                    },
                },
            },
        }
    },
    "elements": {
        "rr1": {
            "MWInput": {
                "port": (con, mw_fem1, 1),
                "upconverter": 1,
            },
            "intermediate_frequency": resonator_IF_q1,  
            "operations": {
                "cw": "const_pulse",
                "readout": "readout_pulse_q1",
            },
            "MWOutput": {
                "port": (con, mw_fem1, 1),
            },
            "time_of_flight": time_of_flight,
            "smearing": 0,
        },
        "rr2": {
            "MWInput": {
                "port": (con, mw_fem1, 1),
                "upconverter": 1,
            },
            "intermediate_frequency": resonator_IF_q2,  
            "operations": {
                "cw": "const_pulse",
                "readout": "readout_pulse_q2",
            },
            "MWOutput": {
                "port": (con, mw_fem1, 1),
            },
            "time_of_flight": time_of_flight,
            "smearing": 0,
        },
        "rr3": {
            "MWInput": {
                "port": (con, mw_fem1, 8),
                "upconverter": 1,
            },
            "intermediate_frequency": resonator_IF_q3,  
            "operations": {
                "cw": "const_pulse",
                "readout": "readout_pulse_q3",
            },
            "MWOutput": {
                "port": (con, mw_fem1, 2),
            },
            "time_of_flight": time_of_flight,
            "smearing": 0,
        },
        "rr4": {
            "MWInput": {
                "port": (con, mw_fem1, 8),
                "upconverter": 1,
            },
            "intermediate_frequency": resonator_IF_q4,  
            "operations": {
                "cw": "const_pulse",
                "readout": "readout_pulse_q4",
            },
            "MWOutput": {
                "port": (con, mw_fem1, 2),
            },
            "time_of_flight": time_of_flight,
            "smearing": 0,
        },
        "rr5": {
            "MWInput": {
                "port": (con, mw_fem1, 1),
                "upconverter": 1,
            },
            "intermediate_frequency": resonator_IF_q5,  # 
            "operations": {
                "cw": "const_pulse",
                "readout": "readout_pulse_q5",
            },
            "MWOutput": {
                "port": (con, mw_fem1, 1),
            },
            "time_of_flight": time_of_flight,
            "smearing": 0,
        },
        "rr6": {
            "MWInput": {
                "port": (con, mw_fem1, 1),
                "upconverter": 1,
            },
            "intermediate_frequency": resonator_IF_q6,  # 
            "operations": {
                "cw": "const_pulse",
                "readout": "readout_pulse_q6",
            },
            "MWOutput": {
                "port": (con, mw_fem1, 1),
            },
            "time_of_flight": time_of_flight,
            "smearing": 0,
        },
        "rr7": {
            "MWInput": {
                "port": (con, mw_fem1, 1),
                "upconverter": 1,
            },
            "intermediate_frequency": resonator_IF_q7,  #
            "operations": {
                "cw": "const_pulse",
                "readout": "readout_pulse_q7",
            },
            "MWOutput": {
                "port": (con, mw_fem1, 1),
            },
            "time_of_flight": time_of_flight,
            "smearing": 0,
        },
        "rr8": {
            "MWInput": {
                "port": (con, mw_fem1, 8),
                "upconverter": 1,
            },
            "intermediate_frequency": resonator_IF_q8,  
            "operations": {
                "cw": "const_pulse",
                "readout": "readout_pulse_q8",
            },
            "MWOutput": {
                "port": (con, mw_fem1, 2),
            },
            "time_of_flight": time_of_flight,
            "smearing": 0,
        },
        "rr9": {
            "MWInput": {
                "port": (con, mw_fem1, 1),
                "upconverter": 1,
            },
            "intermediate_frequency": resonator_IF_q9,  # 
            "operations": {
                "cw": "const_pulse",
                "readout": "readout_pulse_q9",
            },
            "MWOutput": {
                "port": (con, mw_fem1, 1),
            },
            "time_of_flight": time_of_flight,
            "smearing": 0,
        },
        "rr10": {
            "MWInput": {
                "port": (con, mw_fem1, 1),
                "upconverter": 1,
            },
            "intermediate_frequency": resonator_IF_q10,  # 
            "operations": {
                "cw": "const_pulse",
                "readout": "readout_pulse_q10",
            },
            "MWOutput": {
                "port": (con, mw_fem1, 1),
            },
            "time_of_flight": time_of_flight,
            "smearing": 0,
        },
        "rr11": {
            "MWInput": {
                "port": (con, mw_fem1, 1),
                "upconverter": 1,
            },
            "intermediate_frequency": resonator_IF_q11,
            "operations": {
                "cw": "const_pulse",
                "readout": "readout_pulse_q11",
            },
            "MWOutput": {
                "port": (con, mw_fem1, 1),
            },
            "time_of_flight": time_of_flight,
            "smearing": 0,
        },

        "rr12": {
            "MWInput": {
                "port": (con, mw_fem1, 8),
                "upconverter": 1,
            },
            "intermediate_frequency": resonator_IF_q12,
            "operations": {
                "cw": "const_pulse",
                "readout": "readout_pulse_q12",
            },
            "MWOutput": {
                "port": (con, mw_fem1, 2),
            },
            "time_of_flight": time_of_flight,
            "smearing": 0,
        },

        "rr13": {
            "MWInput": {
                "port": (con, mw_fem1, 1),
                "upconverter": 1,
            },
            "intermediate_frequency": resonator_IF_q13,  # 
            "operations": {
                "cw": "const_pulse",
                "readout": "readout_pulse_q13",
            },
            "MWOutput": {
                "port": (con, mw_fem1, 1),
            },
            "time_of_flight": time_of_flight,
            "smearing": 0,
        },

        "rr14": {
            "MWInput": {
                "port": (con, mw_fem1, 1),
                "upconverter": 1,
            },
            "intermediate_frequency": resonator_IF_q14,
            "operations": {
                "cw": "const_pulse",
                "readout": "readout_pulse_q14",
            },
            "MWOutput": {
                "port": (con, mw_fem1, 1),
            },
            "time_of_flight": time_of_flight,
            "smearing": 0,
        },

        "rr15": {
            "MWInput": {
                "port": (con, mw_fem1, 1),
                "upconverter": 1,
            },
            "intermediate_frequency": resonator_IF_q15,
            "operations": {
                "cw": "const_pulse",
                "readout": "readout_pulse_q15",
            },
            "MWOutput": {
                "port": (con, mw_fem1, 1),
            },
            "time_of_flight": time_of_flight,
            "smearing": 0,
        },

        "rr16": {
            "MWInput": {
                "port": (con, mw_fem1, 8),
                "upconverter": 1,
            },
            "intermediate_frequency": resonator_IF_q16,
            "operations": {
                "cw": "const_pulse",
                "readout": "readout_pulse_q16",
            },
            "MWOutput": {
                "port": (con, mw_fem1, 2),
            },
            "time_of_flight": time_of_flight,
            "smearing": 0,
        },

        "rr17": {
            "MWInput": {
                "port": (con, mw_fem1, 1),
                "upconverter": 1,
            },
            "intermediate_frequency": resonator_IF_q17,  # 
            "operations": {
                "cw": "const_pulse",
                "readout": "readout_pulse_q17",
            },
            "MWOutput": {
                "port": (con, mw_fem1, 1),
            },
            "time_of_flight": time_of_flight,
            "smearing": 0,
        },

        "rr18": {
            "MWInput": {
                "port": (con, mw_fem1, 1),
                "upconverter": 1,
            },
            "intermediate_frequency": resonator_IF_q18,
            "operations": {
                "cw": "const_pulse",
                "readout": "readout_pulse_q18",
            },
            "MWOutput": {
                "port": (con, mw_fem1, 1),
            },
            "time_of_flight": time_of_flight,
            "smearing": 0,
        },

        "rr19": {
            "MWInput": {
                "port": (con, mw_fem1, 1),
                "upconverter": 1,
            },
            "intermediate_frequency": resonator_IF_q19,
            "operations": {
                "cw": "const_pulse",
                "readout": "readout_pulse_q19",
            },
            "MWOutput": {
                "port": (con, mw_fem1, 1),
            },
            "time_of_flight": time_of_flight,
            "smearing": 0,
        },

        "rr20": {
            "MWInput": {
                "port": (con, mw_fem1, 8),
                "upconverter": 1,
            },
            "intermediate_frequency": resonator_IF_q20,
            "operations": {
                "cw": "const_pulse",
                "readout": "readout_pulse_q20",
            },
            "MWOutput": {
                "port": (con, mw_fem1, 2),
            },
            "time_of_flight": time_of_flight,
            "smearing": 0,
        },

        
        "rr_C6": {
            "MWInput": {
                "port": (con, mw_fem1, 8),
                "upconverter": 1,
            },
            "intermediate_frequency": resonator_IF_q_C6,
            "operations": {
                "cw": "const_pulse",
                "readout": "readout_pulse_q_C6",
            },
            "MWOutput": {
                "port": (con, mw_fem1, 2),
            },
            "time_of_flight": time_of_flight,
            "smearing": 0,
        },




        "q1_xy": {
            "MWInput": {
                "port": (con, mw_fem1, 2),
                "upconverter": 1,
            },
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
        "q2_xy": {
            "MWInput": {
                "port": (con, mw_fem1, 2), 
                "upconverter": 1,
            },
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
                "-y45": "-y45_pulse_q2",
                "y45": "y45_pulse_q2",
            },
        },
        "q3_xy": {
            "MWInput": {
                "port": (con, mw_fem1, 2),
                "upconverter": 1,
            },
            "intermediate_frequency": qubit_IF_q3,  
            "operations": {
                "cw": "const_pulse",
                "saturation": "saturation_pulse",
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
                "port": (con, mw_fem2, 1),
                "upconverter": 1,
            },
            "intermediate_frequency": qubit_IF_q4,  
            "operations": {
                "cw": "const_pulse",
                "saturation": "saturation_pulse",
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
                "port": (con, mw_fem2, 1),
                "upconverter": 1,
            },
            "intermediate_frequency": qubit_IF_q5,
            "operations": {
                "cw": "const_pulse",
                "saturation": "saturation_pulse",
                "x180": "x180_pulse_q5",
                "x90": "x90_pulse_q5",
                "-x90": "-x90_pulse_q5",
                "y90": "y90_pulse_q5",
                "y180": "y180_pulse_q5",
                "-y90": "-y90_pulse_q5",
            },
        },
        # "q6_xy": {
        #     "MWInput": {
        #         "port": (con, mw_fem1, 7),
        #         "upconverter": 1,
        #     },
        #     "intermediate_frequency": qubit_IF_q6,
        #     "operations": {
        #         "cw": "const_pulse",
        #         "saturation": "saturation_pulse",
        #         "x180": "x180_pulse_q6",
        #         "x90": "x90_pulse_q6",
        #         "-x90": "-x90_pulse_q6",
        #         "y90": "y90_pulse_q6",
        #         "y180": "y180_pulse_q6",
        #         "-y90": "-y90_pulse_q6",
        #     },
        # },
        #####Cooldown_5, q6_xy######
        "q6_xy": {
            "MWInput": {
                "port": (con, mw_fem2, 1),
                "upconverter": 1,
            },
            "intermediate_frequency": qubit_IF_q6,
            "operations": {
                "cw": "const_pulse",
                "saturation": "saturation_pulse",
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
                "port": (con, mw_fem3, 1),
                "upconverter": 1,
            },
            "intermediate_frequency": qubit_IF_q7,
            "operations": {
                "cw": "const_pulse",
                "saturation": "saturation_pulse",
                "x180": "x180_pulse_q7",
                "x90": "x90_pulse_q7",
                "-x90": "-x90_pulse_q7",
                "y90": "y90_pulse_q7",
                "y180": "y180_pulse_q7",
                "-y90": "-y90_pulse_q7",
            },
        },
        "q8_xy": {
            "MWInput": {
                "port": (con, mw_fem1, 4),
                "upconverter": 1,
            },
            "intermediate_frequency": qubit_IF_q8,
            "operations": {
                "cw": "const_pulse",
                "saturation": "saturation_pulse",
                "x180": "x180_pulse_q8",
                "x90": "x90_pulse_q8",
                "-x90": "-x90_pulse_q8",
                "y90": "y90_pulse_q8",
                "y180": "y180_pulse_q8",
                "-y90": "-y90_pulse_q8",
            },
        },
        "q9_xy": {
            "MWInput": {
                "port": (con, mw_fem3, 1),
                "upconverter": 1,
            },
            "intermediate_frequency": qubit_IF_q9,
            "operations": {
                "cw": "const_pulse",
                "saturation": "saturation_pulse",
                "x180": "x180_pulse_q9",
                "x90": "x90_pulse_q9",
                "-x90": "-x90_pulse_q9",
                "y90": "y90_pulse_q9",
                "y180": "y180_pulse_q9",
                "-y90": "-y90_pulse_q9",
            },
        },
        "q10_xy": {
            "MWInput": {
                "port": (con, mw_fem2, 2),
                "upconverter": 1,
            },
            "intermediate_frequency": qubit_IF_q10,
            "operations": {
                "cw": "const_pulse",
                "saturation": "saturation_pulse",
                "x180": "x180_pulse_q10",
                "x90": "x90_pulse_q10",
                "-x90": "-x90_pulse_q10",
                "y90": "y90_pulse_q10",
                "y180": "y180_pulse_q10",
                "-y90": "-y90_pulse_q10",
            },
        },
        "q11_xy": {
            "MWInput": {
                "port": (con, mw_fem1, 5),
                "upconverter": 1,
            },
            "intermediate_frequency": qubit_IF_q11,
            "operations": {
                "cw": "const_pulse",
                "saturation": "saturation_pulse",
                "x180": "x180_pulse_q11",
                "x90": "x90_pulse_q11",
                "-x90": "-x90_pulse_q11",
                "y90": "y90_pulse_q11",
                "y180": "y180_pulse_q11",
                "-y90": "-y90_pulse_q11",
            },
        },
        "q12_xy": {
            "MWInput": {
                "port": (con, mw_fem1, 6),
                "upconverter": 1,
            },
            "intermediate_frequency": qubit_IF_q12,
            "operations": {
                "cw": "const_pulse",
                "saturation": "saturation_pulse",
                "x180": "x180_pulse_q12",
                "x90": "x90_pulse_q12",
                "-x90": "-x90_pulse_q12",
                "y90": "y90_pulse_q12",
                "y180": "y180_pulse_q12",
                "-y90": "-y90_pulse_q12",
            },
        },
        "q13_xy": {
            "MWInput": {
                "port": (con, mw_fem1, 4),
                "upconverter": 1,
            },
            "intermediate_frequency": qubit_IF_q13,
            "operations": {
                "cw": "const_pulse",
                "saturation": "saturation_pulse",
                "x180": "x180_pulse_q13",
                "x90": "x90_pulse_q13",
                "-x90": "-x90_pulse_q13",
                "y90": "y90_pulse_q13",
                "y180": "y180_pulse_q13",
                "-y90": "-y90_pulse_q13",
            },
        },
        "q14_xy": {
            "MWInput": {
                "port": (con, mw_fem2, 3),
                "upconverter": 1,
            },
            "intermediate_frequency": qubit_IF_q14,
            "operations": {
                "cw": "const_pulse",
                "saturation": "saturation_pulse",
                "x180": "x180_pulse_q14",
                "x90": "x90_pulse_q14",
                "-x90": "-x90_pulse_q14",
                "y90": "y90_pulse_q14",
                "y180": "y180_pulse_q14",
                "-y90": "-y90_pulse_q14",
            },
        },
        "q15_xy": {
            "MWInput": {
                "port": (con, mw_fem1, 7),
                "upconverter": 1,
            },
            "intermediate_frequency": qubit_IF_q15,
            "operations": {
                "cw": "const_pulse",
                "saturation": "saturation_pulse",
                "x180": "x180_pulse_q15",
                "x90": "x90_pulse_q15",
                "-x90": "-x90_pulse_q15",
                "y90": "y90_pulse_q15",
                "y180": "y180_pulse_q15",
                "-y90": "-y90_pulse_q15",
            },
        },
        "q16_xy": {
            "MWInput": {
                "port": (con, mw_fem1, 3),
                "upconverter": 1,
            },
            "intermediate_frequency": qubit_IF_q16,
            "operations": {
                "cw": "const_pulse",
                "saturation": "saturation_pulse",
                "x180": "x180_pulse_q16",
                "x90": "x90_pulse_q16",
                "-x90": "-x90_pulse_q16",
                "y90": "y90_pulse_q16",
                "y180": "y180_pulse_q16",
                "-y90": "-y90_pulse_q16",
            },
        },
        "q17_xy": {
            "MWInput": {
                "port": (con, mw_fem1, 5),
                "upconverter": 1,
            },
            "intermediate_frequency": qubit_IF_q17,
            "operations": {
                "cw": "const_pulse",
                "saturation": "saturation_pulse",
                "x180": "x180_pulse_q17",
                "x90": "x90_pulse_q17",
                "-x90": "-x90_pulse_q17",
                "y90": "y90_pulse_q17",
                "y180": "y180_pulse_q17",
                "-y90": "-y90_pulse_q17",
            },
        },
        "q18_xy": {
            "MWInput": {
                "port": (con, mw_fem1, 6),
                "upconverter": 1,
            },
            "intermediate_frequency": qubit_IF_q18,
            "operations": {
                "cw": "const_pulse",
                "saturation": "saturation_pulse",
                "x180": "x180_pulse_q18",
                "x90": "x90_pulse_q18",
                "-x90": "-x90_pulse_q18",
                "y90": "y90_pulse_q18",
                "y180": "y180_pulse_q18",
                "-y90": "-y90_pulse_q18",
            },
        },
        "q19_xy": {
            "MWInput": {
                "port": (con, mw_fem2, 2),
                "upconverter": 1,
            },
            "intermediate_frequency": qubit_IF_q19,
            "operations": {
                "cw": "const_pulse",
                "saturation": "saturation_pulse",
                "x180": "x180_pulse_q19",
                "x90": "x90_pulse_q19",
                "-x90": "-x90_pulse_q19",
                "y90": "y90_pulse_q19",
                "y180": "y180_pulse_q19",
                "-y90": "-y90_pulse_q19",
            },
        },
        "q20_xy": {
            "MWInput": {
                "port": (con, mw_fem2, 3),
                "upconverter": 1,
            },
            "intermediate_frequency": qubit_IF_q20,
            "operations": {
                "cw": "const_pulse",
                "saturation": "saturation_pulse",
                "x180": "x180_pulse_q20",
                "x90": "x90_pulse_q20",
                "-x90": "-x90_pulse_q20",
                "y90": "y90_pulse_q20",
                "y180": "y180_pulse_q20",
                "-y90": "-y90_pulse_q20",
            },
        },

        
        
        "q_C6_xy": { 
            "MWInput": {
                "port": (con, mw_fem2, 2),
                "upconverter": 1,
            },
            "intermediate_frequency": qubit_IF_q_C6,
            "operations": {
                "cw": "const_pulse",
                "saturation": "saturation_pulse",
                "x180": "x180_pulse_q_C6",
                "x90": "x90_pulse_q_C6",
                "-x90": "-x90_pulse_q_C6",
                "y90": "y90_pulse_q_C6",
                "y180": "y180_pulse_q_C6",
                "-y90": "-y90_pulse_q_C6",
            },
        },
            
        # "q1_z": {
        #     "singleInput": {
        #         "port": (con, lf_fem1, 1),
        #     },
        #     "intermediate_frequency": parametric_IF1,
        #     "operations": {
        #         "const": "const_flux_pulse",
        #         "gauss": "gauss_flux_pulse",
        #     },
        # },
        "c12_z_1001": {
            "singleInput": {
                "port": (con, lf_fem1, 1),
            },
            "intermediate_frequency": parametric_IF_C12_1001,
            "operations": {
                "const": "const_flux_pulse_C12_1001",
                #"gauss": "gauss_flux_pulse",
            },
        },
        "c12_z_1120": {
            "singleInput": {
                "port": (con, lf_fem1, 1),
            },
            "intermediate_frequency": parametric_IF_C12_1120,
            "operations": {
                "const": "const_flux_pulse_C12_1120",
                #"gauss": "gauss_flux_pulse",
            },
        },
        "c12_z_1102": {
            "singleInput": {
                "port": (con, lf_fem1, 1),
            },
            "intermediate_frequency": parametric_IF_C12_1102,
            "operations": {
                "const": "const_flux_pulse_C12_1102",
                "riseup": "riseup_flux_pulse_C12_1102",
            },
        },

#marktemp

        #C1
        "c1_Q12_1001": {
            "singleInput": {
                "port": (con, lf_fem1, 1),
            },
            "intermediate_frequency": parametric_IF_C1_Q12_1001,
            "operations": {
                "const": "parametric_const_pulse_C1_Q12_1001",
                # "ringup": "ringup_flux_pulse_C1_Q12_1001",
            },
        },

        "c1_Q12_1102": {
            "singleInput": {
                "port": (con, lf_fem1, 1),
            },
            "intermediate_frequency": parametric_IF_C1_Q12_1102,
            "operations": {
                "const": "parametric_const_pulse_C1_Q12_1102",
                # "ringup": "ringup_flux_pulse_C1_Q12_1102",
            },
        },

        "c1_Q12_1120": {
            "singleInput": {
                "port": (con, lf_fem1, 1),
            },
            "intermediate_frequency": parametric_IF_C1_Q12_1120,
            "operations": {
                "const": "parametric_const_pulse_C1_Q12_1120",
                # "ringup": "ringup_flux_pulse_C1_Q12_1120",
            },
        },

        "c1_Q15_1001": {
            "singleInput": {
                "port": (con, lf_fem1, 1),
            },
            "intermediate_frequency": parametric_IF_C1_Q15_1001,
            "operations": {
                "const": "parametric_const_pulse_C1_Q15_1001",
                # "ringup": "ringup_flux_pulse_C1_Q15_1001",
            },
        },

        "c1_Q15_1102": {
            "singleInput": {
                "port": (con, lf_fem1, 1),
            },
            "intermediate_frequency": parametric_IF_C1_Q15_1102,
            "operations": {
                "const": "parametric_const_pulse_C1_Q15_1102",
                # "ringup": "ringup_flux_pulse_C1_Q15_1102",
            },
        },

        "c1_Q15_1120": {
            "singleInput": {
                "port": (con, lf_fem1, 1),
            },
            "intermediate_frequency": parametric_IF_C1_Q15_1120,
            "operations": {
                "const": "parametric_const_pulse_C1_Q15_1120",
                # "ringup": "ringup_flux_pulse_C1_Q15_1120",
            },
        },

        "c1_Q16_1001": {
            "singleInput": {
                "port": (con, lf_fem1, 1),
            },
            "intermediate_frequency": parametric_IF_C1_Q16_1001,
            "operations": {
                "const": "parametric_const_pulse_C1_Q16_1001",
                # "ringup": "ringup_flux_pulse_C1_Q16_1001",
            },
        },

        "c1_Q16_1102": {
            "singleInput": {
                "port": (con, lf_fem1, 1),
            },
            "intermediate_frequency": parametric_IF_C1_Q16_1102,
            "operations": {
                "const": "parametric_const_pulse_C1_Q16_1102",
                # "ringup": "ringup_flux_pulse_C1_Q16_1102",
            },
        },

        "c1_Q16_1120": {
            "singleInput": {
                "port": (con, lf_fem1, 1),
            },
            "intermediate_frequency": parametric_IF_C1_Q16_1120,
            "operations": {
                "const": "parametric_const_pulse_C1_Q16_1120",
                # "ringup": "ringup_flux_pulse_C1_Q16_1120",
            },
        },

        "c1_Q25_1001": {
            "singleInput": {
                "port": (con, lf_fem1, 1),
            },
            "intermediate_frequency": parametric_IF_C1_Q25_1001,
            "operations": {
                "const": "parametric_const_pulse_C1_Q25_1001",
                # "ringup": "ringup_flux_pulse_C1_Q25_1001",
            },
        },

        "c1_Q25_1102": {
            "singleInput": {
                "port": (con, lf_fem1, 1),
            },
            "intermediate_frequency": parametric_IF_C1_Q25_1102,
            "operations": {
                "const": "parametric_const_pulse_C1_Q25_1102",
                # "ringup": "ringup_flux_pulse_C1_Q25_1102",
            },
        },

        "c1_Q25_1120": {
            "singleInput": {
                "port": (con, lf_fem1, 1),
            },
            "intermediate_frequency": parametric_IF_C1_Q25_1120,
            "operations": {
                "const": "parametric_const_pulse_C1_Q25_1120",
                # "ringup": "ringup_flux_pulse_C1_Q25_1120",
            },
        },

        "c1_Q26_1001": {
            "singleInput": {
                "port": (con, lf_fem1, 1),
            },
            "intermediate_frequency": parametric_IF_C1_Q26_1001,
            "operations": {
                "const": "parametric_const_pulse_C1_Q26_1001",
                # "ringup": "ringup_flux_pulse_C1_Q26_1001",
            },
        },

        "c1_Q26_1102": {
            "singleInput": {
                "port": (con, lf_fem1, 1),
            },
            "intermediate_frequency": parametric_IF_C1_Q26_1102,
            "operations": {
                "const": "parametric_const_pulse_C1_Q26_1102",
                # "ringup": "ringup_flux_pulse_C1_Q26_1102",
            },
        },

        "c1_Q26_1120": {
            "singleInput": {
                "port": (con, lf_fem1, 1),
            },
            "intermediate_frequency": parametric_IF_C1_Q26_1120,
            "operations": {
                "const": "parametric_const_pulse_C1_Q26_1120",
                # "ringup": "ringup_flux_pulse_C1_Q26_1120",
            },
        },

        "c1_Q56_1001": {
            "singleInput": {
                "port": (con, lf_fem1, 1),
            },
            "intermediate_frequency": parametric_IF_C1_Q56_1001,
            "operations": {
                "const": "parametric_const_pulse_C1_Q56_1001",
                # "ringup": "ringup_flux_pulse_C1_Q56_1001",
            },
        },

        "c1_Q56_1102": {
            "singleInput": {
                "port": (con, lf_fem1, 1),
            },
            "intermediate_frequency": parametric_IF_C1_Q56_1102,
            "operations": {
                "const": "parametric_const_pulse_C1_Q56_1102",
                # "ringup": "ringup_flux_pulse_C1_Q56_1102",
            },
        },

        "c1_Q56_1120": {
            "singleInput": {
                "port": (con, lf_fem1, 1),
            },
            "intermediate_frequency": parametric_IF_C1_Q56_1120,
            "operations": {
                "const": "parametric_const_pulse_C1_Q56_1120",
                # "ringup": "ringup_flux_pulse_C1_Q56_1120",
            },
        },
        #C4
        "c4_Q56_1001": {
            "singleInput": {
                "port": (con, lf_fem1, 2),
            },
            "intermediate_frequency": parametric_IF_C4_Q56_1001,
            "operations": {
                "const": "parametric_const_pulse_C4_Q56_1001",
                # "ringup": "ringup_flux_pulse_C4_Q56_1001",
            },
        },

        "c4_Q56_1102": {
            "singleInput": {
                "port": (con, lf_fem1, 2),
            },
            "intermediate_frequency": parametric_IF_C4_Q56_1102,
            "operations": {
                "const": "parametric_const_pulse_C4_Q56_1102",
                # "ringup": "ringup_flux_pulse_C4_Q56_1102",
            },
        },

        "c4_Q56_1120": {
            "singleInput": {
                "port": (con, lf_fem1, 2),
            },
            "intermediate_frequency": parametric_IF_C4_Q56_1120,
            "operations": {
                "const": "parametric_const_pulse_C4_Q56_1120",
                # "ringup": "ringup_flux_pulse_C4_Q56_1120",
            },
        },

        "c4_Q59_1001": {
            "singleInput": {
                "port": (con, lf_fem1, 2),
            },
            "intermediate_frequency": parametric_IF_C4_Q59_1001,
            "operations": {
                "const": "parametric_const_pulse_C4_Q59_1001",
                # "ringup": "ringup_flux_pulse_C4_Q59_1001",
            },
        },

        "c4_Q59_1102": {
            "singleInput": {
                "port": (con, lf_fem1, 2),
            },
            "intermediate_frequency": parametric_IF_C4_Q59_1102,
            "operations": {
                "const": "parametric_const_pulse_C4_Q59_1102",
                # "ringup": "ringup_flux_pulse_C4_Q59_1102",
            },
        },

        "c4_Q59_1120": {
            "singleInput": {
                "port": (con, lf_fem1, 2),
            },
            "intermediate_frequency": parametric_IF_C4_Q59_1120,
            "operations": {
                "const": "parametric_const_pulse_C4_Q59_1120",
                # "ringup": "ringup_flux_pulse_C4_Q59_1120",
            },
        },

        "c4_Q510_1001": {
            "singleInput": {
                "port": (con, lf_fem1, 2),
            },
            "intermediate_frequency": parametric_IF_C4_Q510_1001,
            "operations": {
                "const": "parametric_const_pulse_C4_Q510_1001",
                # "ringup": "ringup_flux_pulse_C4_Q510_1001",
            },
        },

        "c4_Q510_1102": {
            "singleInput": {
                "port": (con, lf_fem1, 2),
            },
            "intermediate_frequency": parametric_IF_C4_Q510_1102,
            "operations": {
                "const": "parametric_const_pulse_C4_Q510_1102",
                # "ringup": "ringup_flux_pulse_C4_Q510_1102",
            },
        },

        "c4_Q510_1120": {
            "singleInput": {
                "port": (con, lf_fem1, 2),
            },
            "intermediate_frequency": parametric_IF_C4_Q510_1120,
            "operations": {
                "const": "parametric_const_pulse_C4_Q510_1120",
                # "ringup": "ringup_flux_pulse_C4_Q510_1120",
            },
        },

        "c4_Q69_1001": {
            "singleInput": {
                "port": (con, lf_fem1, 2),
            },
            "intermediate_frequency": parametric_IF_C4_Q69_1001,
            "operations": {
                "const": "parametric_const_pulse_C4_Q69_1001",
                # "ringup": "ringup_flux_pulse_C4_Q69_1001",
            },
        },

        "c4_Q69_1102": {
            "singleInput": {
                "port": (con, lf_fem1, 2),
            },
            "intermediate_frequency": parametric_IF_C4_Q69_1102,
            "operations": {
                "const": "parametric_const_pulse_C4_Q69_1102",
                # "ringup": "ringup_flux_pulse_C4_Q69_1102",
            },
        },

        "c4_Q69_1120": {
            "singleInput": {
                "port": (con, lf_fem1, 2),
            },
            "intermediate_frequency": parametric_IF_C4_Q69_1120,
            "operations": {
                "const": "parametric_const_pulse_C4_Q69_1120",
                # "ringup": "ringup_flux_pulse_C4_Q69_1120",
            },
        },

        "c4_Q610_1001": {
            "singleInput": {
                "port": (con, lf_fem1, 2),
            },
            "intermediate_frequency": parametric_IF_C4_Q610_1001,
            "operations": {
                "const": "parametric_const_pulse_C4_Q610_1001",
                # "ringup": "ringup_flux_pulse_C4_Q610_1001",
            },
        },

        "c4_Q610_1102": {
            "singleInput": {
                "port": (con, lf_fem1, 2),
            },
            "intermediate_frequency": parametric_IF_C4_Q610_1102,
            "operations": {
                "const": "parametric_const_pulse_C4_Q610_1102",
                # "ringup": "ringup_flux_pulse_C4_Q610_1102",
            },
        },

        "c4_Q610_1120": {
            "singleInput": {
                "port": (con, lf_fem1, 2),
            },
            "intermediate_frequency": parametric_IF_C4_Q610_1120,
            "operations": {
                "const": "parametric_const_pulse_C4_Q610_1120",
                # "ringup": "ringup_flux_pulse_C4_Q610_1120",
            },
        },

        "c4_Q910_1001": {
            "singleInput": {
                "port": (con, lf_fem1, 2),
            },
            "intermediate_frequency": parametric_IF_C4_Q910_1001,
            "operations": {
                "const": "parametric_const_pulse_C4_Q910_1001",
                # "ringup": "ringup_flux_pulse_C4_Q910_1001",
            },
        },

        "c4_Q910_1102": {
            "singleInput": {
                "port": (con, lf_fem1, 2),
            },
            "intermediate_frequency": parametric_IF_C4_Q910_1102,
            "operations": {
                "const": "parametric_const_pulse_C4_Q910_1102",
                # "ringup": "ringup_flux_pulse_C4_Q910_1102",
            },
        },

        "c4_Q910_1120": {
            "singleInput": {
                "port": (con, lf_fem1, 2),
            },
            "intermediate_frequency": parametric_IF_C4_Q910_1120,
            "operations": {
                "const": "parametric_const_pulse_C4_Q910_1120",
                # "ringup": "ringup_flux_pulse_C4_Q910_1120",
            },
        },
        #C6
        "c6_Q910_1001": {
            "singleInput": {
                "port": (con, lf_fem2, 1),
            },
            "intermediate_frequency": parametric_IF_C6_Q910_1001,
            "operations": {
                "const": "parametric_const_pulse_C6_Q910_1001",
                # "ringup": "ringup_flux_pulse_C6_Q910_1001",
            },
        },

        "c6_Q910_1102": {
            "singleInput": {
                "port": (con, lf_fem2, 1),
            },
            "intermediate_frequency": parametric_IF_C6_Q910_1102,
            "operations": {
                "const": "parametric_const_pulse_C6_Q910_1102",
                # "ringup": "ringup_flux_pulse_C6_Q910_1102",
            },
        },

        "c6_Q910_1120": {
            "singleInput": {
                "port": (con, lf_fem2, 1),
            },
            "intermediate_frequency": parametric_IF_C6_Q910_1120,
            "operations": {
                "const": "parametric_const_pulse_C6_Q910_1120",
                # "ringup": "ringup_flux_pulse_C6_Q910_1120",
            },
        },

        "c6_Q913_1001": {
            "singleInput": {
                "port": (con, lf_fem2, 1),
            },
            "intermediate_frequency": parametric_IF_C6_Q913_1001,
            "operations": {
                "const": "parametric_const_pulse_C6_Q913_1001",
                # "ringup": "ringup_flux_pulse_C6_Q913_1001",
            },
        },

        "c6_Q913_1102": {
            "singleInput": {
                "port": (con, lf_fem2, 1),
            },
            "intermediate_frequency": parametric_IF_C6_Q913_1102,
            "operations": {
                "const": "parametric_const_pulse_C6_Q913_1102",
                # "ringup": "ringup_flux_pulse_C6_Q913_1102",
            },
        },

        "c6_Q913_1120": {
            "singleInput": {
                "port": (con, lf_fem2, 1),
            },
            "intermediate_frequency": parametric_IF_C6_Q913_1120,
            "operations": {
                "const": "parametric_const_pulse_C6_Q913_1120",
                # "ringup": "ringup_flux_pulse_C6_Q913_1120",
            },
        },

        "c6_Q914_1001": {
            "singleInput": {
                "port": (con, lf_fem2, 1),
            },
            "intermediate_frequency": parametric_IF_C6_Q914_1001,
            "operations": {
                "const": "parametric_const_pulse_C6_Q914_1001",
                # "ringup": "ringup_flux_pulse_C6_Q914_1001",
            },
        },

        "c6_Q914_1102": {
            "singleInput": {
                "port": (con, lf_fem2, 1),
            },
            "intermediate_frequency": parametric_IF_C6_Q914_1102,
            "operations": {
                "const": "parametric_const_pulse_C6_Q914_1102",
                # "ringup": "ringup_flux_pulse_C6_Q914_1102",
            },
        },

        "c6_Q914_1120": {
            "singleInput": {
                "port": (con, lf_fem2, 1),
            },
            "intermediate_frequency": parametric_IF_C6_Q914_1120,
            "operations": {
                "const": "parametric_const_pulse_C6_Q914_1120",
                # "ringup": "ringup_flux_pulse_C6_Q914_1120",
            },
        },

        "c6_Q1013_1001": {
            "singleInput": {
                "port": (con, lf_fem2, 1),
            },
            "intermediate_frequency": parametric_IF_C6_Q1013_1001,
            "operations": {
                "const": "parametric_const_pulse_C6_Q1013_1001",
                # "ringup": "ringup_flux_pulse_C6_Q1013_1001",
            },
        },

        "c6_Q1013_1102": {
            "singleInput": {
                "port": (con, lf_fem2, 1),
            },
            "intermediate_frequency": parametric_IF_C6_Q1013_1102,
            "operations": {
                "const": "parametric_const_pulse_C6_Q1013_1102",
                # "ringup": "ringup_flux_pulse_C6_Q1013_1102",
            },
        },

        "c6_Q1013_1120": {
            "singleInput": {
                "port": (con, lf_fem2, 1),
            },
            "intermediate_frequency": parametric_IF_C6_Q1013_1120,
            "operations": {
                "const": "parametric_const_pulse_C6_Q1013_1120",
                # "ringup": "ringup_flux_pulse_C6_Q1013_1120",
            },
        },

        "c6_Q1014_1001": {
            "singleInput": {
                "port": (con, lf_fem2, 1),
            },
            "intermediate_frequency": parametric_IF_C6_Q1014_1001,
            "operations": {
                "const": "parametric_const_pulse_C6_Q1014_1001",
                # "ringup": "ringup_flux_pulse_C6_Q1014_1001",
            },
        },

        "c6_Q1014_1102": {
            "singleInput": {
                "port": (con, lf_fem2, 1),
            },
            "intermediate_frequency": parametric_IF_C6_Q1014_1102,
            "operations": {
                "const": "parametric_const_pulse_C6_Q1014_1102",
                # "ringup": "ringup_flux_pulse_C6_Q1014_1102",
            },
        },

        "c6_Q1014_1120": {
            "singleInput": {
                "port": (con, lf_fem2, 1),
            },
            "intermediate_frequency": parametric_IF_C6_Q1014_1120,
            "operations": {
                "const": "parametric_const_pulse_C6_Q1014_1120",
                # "ringup": "ringup_flux_pulse_C6_Q1014_1120",
            },
        },

        "c6_Q1314_1001": {
            "singleInput": {
                "port": (con, lf_fem2, 1),
            },
            "intermediate_frequency": parametric_IF_C6_Q1314_1001,
            "operations": {
                "const": "parametric_const_pulse_C6_Q1314_1001",
                # "ringup": "ringup_flux_pulse_C6_Q1314_1001",
            },
        },

        "c6_Q1314_1102": {
            "singleInput": {
                "port": (con, lf_fem2, 1),
            },
            "intermediate_frequency": parametric_IF_C6_Q1314_1102,
            "operations": {
                "const": "parametric_const_pulse_C6_Q1314_1102",
                # "ringup": "ringup_flux_pulse_C6_Q1314_1102",
            },
        },

        "c6_Q1314_1120": {
            "singleInput": {
                "port": (con, lf_fem2, 1),
            },
            "intermediate_frequency": parametric_IF_C6_Q1314_1120,
            "operations": {
                "const": "parametric_const_pulse_C6_Q1314_1120",
                # "ringup": "ringup_flux_pulse_C6_Q1314_1120",
            },
        },
        #C8
        "c8_Q1317_1001": {
            "singleInput": {
                "port": (con, lf_fem2, 2),
            },
            "intermediate_frequency": parametric_IF_C8_Q1317_1001,
            "operations": {
                "const": "parametric_const_pulse_C8_Q1317_1001",
                # "ringup": "ringup_flux_pulse_C8_Q1317_1001",
                
            },
        },

        "c8_Q1317_1102": {
            "singleInput": {
                "port": (con, lf_fem2, 2),
            },
            "intermediate_frequency": parametric_IF_C8_Q1317_1102,
            "operations": {
                "const": "parametric_const_pulse_C8_Q1317_1102",
                "ringup": "ringup_flux_pulse_C8_Q1317_1102",
                
            },

        },
        
        "c8_Q1317_1120": {
            "singleInput": {
                "port": (con, lf_fem2, 2),
            },
            "intermediate_frequency": parametric_IF_C8_Q1317_1120,
            "operations": {
                "const": "parametric_const_pulse_C8_Q1317_1120",
                # "ringup": "ringup_flux_pulse_C8_Q1317_1120",
                
            },
        },

        "c8_Q1314_1001": {
            "singleInput": {
                "port": (con, lf_fem2, 2),
            },
            "intermediate_frequency": parametric_IF_C8_Q1314_1001,
            "operations": {
                "const": "parametric_const_pulse_C8_Q1314_1001",
                # "ringup": "ringup_flux_pulse_C8_Q1314_1001",
            },
        },

        "c8_Q1314_1102": {
            "singleInput": {
                "port": (con, lf_fem2, 2),
            },
            "intermediate_frequency": parametric_IF_C8_Q1314_1102,
            "operations": {
                "const": "parametric_const_pulse_C8_Q1314_1102",
                # "ringup": "ringup_flux_pulse_C8_Q1314_1102",
            },
        },

        "c8_Q1314_1120": {
            "singleInput": {
                "port": (con, lf_fem2, 2),
            },
            "intermediate_frequency": parametric_IF_C8_Q1314_1120,
            "operations": {
                "const": "parametric_const_pulse_C8_Q1314_1120",
                # "ringup": "ringup_flux_pulse_C8_Q1314_1120",
            },
        },

        "c8_Q1318_1001": {
            "singleInput": {
                "port": (con, lf_fem2, 2),
            },
            "intermediate_frequency": parametric_IF_C8_Q1318_1001,
            "operations": {
                "const": "parametric_const_pulse_C8_Q1318_1001",
                # "ringup": "ringup_flux_pulse_C8_Q1318_1001",
            },
        },

        "c8_Q1318_1102": {
            "singleInput": {
                "port": (con, lf_fem2, 2),
            },
            "intermediate_frequency": parametric_IF_C8_Q1318_1102,
            "operations": {
                "const": "parametric_const_pulse_C8_Q1318_1102",
                # "ringup": "ringup_flux_pulse_C8_Q1318_1102",
            },
        },

        "c8_Q1318_1120": {
            "singleInput": {
                "port": (con, lf_fem2, 2),
            },
            "intermediate_frequency": parametric_IF_C8_Q1318_1120,
            "operations": {
                "const": "parametric_const_pulse_C8_Q1318_1120",
                # "ringup": "ringup_flux_pulse_C8_Q1318_1120",
            },
        },

        "c8_Q1417_1001": {
            "singleInput": {
                "port": (con, lf_fem2, 2),
            },
            "intermediate_frequency": parametric_IF_C8_Q1417_1001,
            "operations": {
                "const": "parametric_const_pulse_C8_Q1417_1001",
                # "ringup": "ringup_flux_pulse_C8_Q1417_1001",
            },
        },

        "c8_Q1417_1102": {
            "singleInput": {
                "port": (con, lf_fem2, 2),
            },
            "intermediate_frequency": parametric_IF_C8_Q1417_1102,
            "operations": {
                "const": "parametric_const_pulse_C8_Q1417_1102",
                # "ringup": "ringup_flux_pulse_C8_Q1417_1102",
            },
        },

        "c8_Q1417_1120": {
            "singleInput": {
                "port": (con, lf_fem2, 2),
            },
            "intermediate_frequency": parametric_IF_C8_Q1417_1120,
            "operations": {
                "const": "parametric_const_pulse_C8_Q1417_1120",
                # "ringup": "ringup_flux_pulse_C8_Q1417_1120",
            },
        },

        "c8_Q1418_1001": {
            "singleInput": {
                "port": (con, lf_fem2, 2),
            },
            "intermediate_frequency": parametric_IF_C8_Q1418_1001,
            "operations": {
                "const": "parametric_const_pulse_C8_Q1418_1001",
                # "ringup": "ringup_flux_pulse_C8_Q1418_1001",
            },
        },

        "c8_Q1418_1102": {
            "singleInput": {
                "port": (con, lf_fem2, 2),
            },
            "intermediate_frequency": parametric_IF_C8_Q1418_1102,
            "operations": {
                "const": "parametric_const_pulse_C8_Q1418_1102",
                # "ringup": "ringup_flux_pulse_C8_Q1418_1102",
            },
        },

        "c8_Q1418_1120": {
            "singleInput": {
                "port": (con, lf_fem2, 2),
            },
            "intermediate_frequency": parametric_IF_C8_Q1418_1120,
            "operations": {
                "const": "parametric_const_pulse_C8_Q1418_1120",
                # "ringup": "ringup_flux_pulse_C8_Q1418_1120",
            },
        },

        "c8_Q1718_1001": {
            "singleInput": {
                "port": (con, lf_fem2, 2),
            },
            "intermediate_frequency": parametric_IF_C8_Q1718_1001,
            "operations": {
                "const": "parametric_const_pulse_C8_Q1718_1001",
                # "ringup": "ringup_flux_pulse_C8_Q1718_1001",
            },
        },

        "c8_Q1718_1102": {
            "singleInput": {
                "port": (con, lf_fem2, 2),
            },
            "intermediate_frequency": parametric_IF_C8_Q1718_1102,
            "operations": {
                "const": "parametric_const_pulse_C8_Q1718_1102",
                # "ringup": "ringup_flux_pulse_C8_Q1718_1102",
            },
        },

        "c8_Q1718_1120": {
            "singleInput": {
                "port": (con, lf_fem2, 2),
            },
            "intermediate_frequency": parametric_IF_C8_Q1718_1120,
            "operations": {
                "const": "parametric_const_pulse_C8_Q1718_1120",
                # "ringup": "ringup_flux_pulse_C8_Q1718_1120",
            },
        },
#COOLDOWN2

        "c3_Q34_1001": {
            "singleInput": {
                "port": (con, lf_fem1, 4),
            },
            "intermediate_frequency": parametric_IF_C3_Q34_1001,
            "operations": {
                "const": "parametric_const_pulse_C3_Q34_1001",
                # "ringup": "ringup_flux_pulse_C3_Q34_1001",
            },
        },

        "c3_Q34_1102": {
            "singleInput": {
                "port": (con, lf_fem1, 4),
            },
            "intermediate_frequency": parametric_IF_C3_Q34_1102,
            "operations": {
                "const": "parametric_const_pulse_C3_Q34_1102",
                # "ringup": "ringup_flux_pulse_C3_Q34_1102",
            },
        },

        "c3_Q34_1120": {
            "singleInput": {
                "port": (con, lf_fem1, 4),
            },
            "intermediate_frequency": parametric_IF_C3_Q34_1120,
            "operations": {
                "const": "parametric_const_pulse_C3_Q34_1120",
                # "ringup": "ringup_flux_pulse_C3_Q34_1120",
            },
        },

        # C3_Q38
        "c3_Q38_1001": {
            "singleInput": {
                "port": (con, lf_fem1, 4),
            },
            "intermediate_frequency": parametric_IF_C3_Q38_1001,
            "operations": {
                "const": "parametric_const_pulse_C3_Q38_1001",
                # "ringup": "ringup_flux_pulse_C3_Q38_1001",
            },
        },
        "c3_Q38_1102": {
            "singleInput": {
                "port": (con, lf_fem1, 4),
            },
            "intermediate_frequency": parametric_IF_C3_Q38_1102,
            "operations": {
                "const": "parametric_const_pulse_C3_Q38_1102",
                # "ringup": "ringup_flux_pulse_C3_Q38_1102",
            },
        },
        "c3_Q38_1120": {
            "singleInput": {
                "port": (con, lf_fem1, 4),
            },
            "intermediate_frequency": parametric_IF_C3_Q38_1120,
            "operations": {
                "const": "parametric_const_pulse_C3_Q38_1120",
                # "ringup": "ringup_flux_pulse_C3_Q38_1120",
            },
        },

        # C3_Q37
        "c3_Q37_1001": {
            "singleInput": {
                "port": (con, lf_fem1, 4), #1
            },
            "intermediate_frequency": parametric_IF_C3_Q37_1001,
            "operations": {
                "const": "parametric_const_pulse_C3_Q37_1001",
                # "ringup": "ringup_flux_pulse_C3_Q37_1001",
            },
        },
        "c3_Q37_1102": {
            "singleInput": {
                "port": (con, lf_fem1, 4),
            },
            "intermediate_frequency": parametric_IF_C3_Q37_1102,
            "operations": {
                "const": "parametric_const_pulse_C3_Q37_1102",
                # "ringup": "ringup_flux_pulse_C3_Q37_1102",
            },
        },
        "c3_Q37_1120": {
            "singleInput": {
                "port": (con, lf_fem1, 4),
            },
            "intermediate_frequency": parametric_IF_C3_Q37_1120,
            "operations": {
                "const": "parametric_const_pulse_C3_Q37_1120",
                # "ringup": "ringup_flux_pulse_C3_Q37_1120",
            },
        },

        # C3_Q48
        "c3_Q48_1001": {
            "singleInput": {
                "port": (con, lf_fem1, 4),
            },
            "intermediate_frequency": parametric_IF_C3_Q48_1001,
            "operations": {
                "const": "parametric_const_pulse_C3_Q48_1001",
                # "ringup": "ringup_flux_pulse_C3_Q48_1001",
            },
        },
        "c3_Q48_1102": {
            "singleInput": {
                "port": (con, lf_fem1, 4),
            },
            "intermediate_frequency": parametric_IF_C3_Q48_1102,
            "operations": {
                "const": "parametric_const_pulse_C3_Q48_1102",
                # "ringup": "ringup_flux_pulse_C3_Q48_1102",
            },
        },
        "c3_Q48_1120": {
            "singleInput": {
                "port": (con, lf_fem1, 4),
            },
            "intermediate_frequency": parametric_IF_C3_Q48_1120,
            "operations": {
                "const": "parametric_const_pulse_C3_Q48_1120",
                # "ringup": "ringup_flux_pulse_C3_Q48_1120",
            },
        },

        # C3_Q47
        "c3_Q47_1001": {
            "singleInput": {
                "port": (con, lf_fem1, 4),
            },
            "intermediate_frequency": parametric_IF_C3_Q47_1001,
            "operations": {
                "const": "parametric_const_pulse_C3_Q47_1001",
                # "ringup": "ringup_flux_pulse_C3_Q47_1001",
            },
        },
        "c3_Q47_1102": {
            "singleInput": {
                "port": (con, lf_fem1, 4),
            },
            "intermediate_frequency": parametric_IF_C3_Q47_1102,
            "operations": {
                "const": "parametric_const_pulse_C3_Q47_1102",
                # "ringup": "ringup_flux_pulse_C3_Q47_1102",
            },
        },
        "c3_Q47_1120": {
            "singleInput": {
                "port": (con, lf_fem1, 4),
            },
            "intermediate_frequency": parametric_IF_C3_Q47_1120,
            "operations": {
                "const": "parametric_const_pulse_C3_Q47_1120",
                # "ringup": "ringup_flux_pulse_C3_Q47_1120",
            },
        },

        # C3_Q78
        "c3_Q78_1001": {
            "singleInput": {
                "port": (con, lf_fem1, 4),
            },
            "intermediate_frequency": parametric_IF_C3_Q78_1001,
            "operations": {
                "const": "parametric_const_pulse_C3_Q78_1001",
                # "ringup": "ringup_flux_pulse_C3_Q78_1001",
            },
        },
        "c3_Q78_1102": {
            "singleInput": {
                "port": (con, lf_fem1,4),
            },
            "intermediate_frequency": parametric_IF_C3_Q78_1102,
            "operations": {
                "const": "parametric_const_pulse_C3_Q78_1102",
                # "ringup": "ringup_flux_pulse_C3_Q78_1102",
            },
        },
        "c3_Q78_1120": {
            "singleInput": {
                "port": (con, lf_fem1, 4),
            },
            "intermediate_frequency": parametric_IF_C3_Q78_1120,
            "operations": {
                "const": "parametric_const_pulse_C3_Q78_1120",
                # "ringup": "ringup_flux_pulse_C3_Q78_1120",
            },
        },

        # ---- Updated C5 blocks with port index changed to 2 ----

        # C5_Q78
        "c5_Q78_1001": {
            "singleInput": {
                "port": (con, lf_fem1, 2),
            },
            "intermediate_frequency": parametric_IF_C5_Q78_1001,
            "operations": {
                "const": "parametric_const_pulse_C5_Q78_1001",
                # "ringup": "ringup_flux_pulse_C5_Q78_1001",
            },
        },
        "c5_Q78_1102": {
            "singleInput": {
                "port": (con, lf_fem1, 2),
            },
            "intermediate_frequency": parametric_IF_C5_Q78_1102,
            "operations": {
                "const": "parametric_const_pulse_C5_Q78_1102",
                # "ringup": "ringup_flux_pulse_C5_Q78_1102",
            },
        },
        "c5_Q78_1120": {
            "singleInput": {
                "port": (con, lf_fem1, 2),
            },
            "intermediate_frequency": parametric_IF_C5_Q78_1120,
            "operations": {
                "const": "parametric_const_pulse_C5_Q78_1120",
                # "ringup": "ringup_flux_pulse_C5_Q78_1120",
            },
        },

        # C5_Q712
        "c5_Q712_1001": {
            "singleInput": {
                "port": (con, lf_fem1, 2),
            },
            "intermediate_frequency": parametric_IF_C5_Q712_1001,
            "operations": {
                "const": "parametric_const_pulse_C5_Q712_1001",
                # "ringup": "ringup_flux_pulse_C5_Q712_1001",
            },
        },
        "c5_Q712_1102": {
            "singleInput": {
                "port": (con, lf_fem1, 2),
            },
            "intermediate_frequency": parametric_IF_C5_Q712_1102,
            "operations": {
                "const": "parametric_const_pulse_C5_Q712_1102",
                # "ringup": "ringup_flux_pulse_C5_Q712_1102",
            },
        },
        "c5_Q712_1120": {
            "singleInput": {
                "port": (con, lf_fem1, 2),
            },
            "intermediate_frequency": parametric_IF_C5_Q712_1120,
            "operations": {
                "const": "parametric_const_pulse_C5_Q712_1120",
                # "ringup": "ringup_flux_pulse_C5_Q712_1120",
            },
        },

        # C5_Q711
        "c5_Q711_1001": {
            "singleInput": {
                "port": (con, lf_fem1, 2),
            },
            "intermediate_frequency": parametric_IF_C5_Q711_1001,
            "operations": {
                "const": "parametric_const_pulse_C5_Q711_1001",
                # "ringup": "ringup_flux_pulse_C5_Q711_1001",
            },
        },
        "c5_Q711_1102": {
            "singleInput": {
                "port": (con, lf_fem1, 2),
            },
            "intermediate_frequency": parametric_IF_C5_Q711_1102,
            "operations": {
                "const": "parametric_const_pulse_C5_Q711_1102",
                # "ringup": "ringup_flux_pulse_C5_Q711_1102",
            },
        },
        "c5_Q711_1120": {
            "singleInput": {
                "port": (con, lf_fem1, 2),
            },
            "intermediate_frequency": parametric_IF_C5_Q711_1120,
            "operations": {
                "const": "parametric_const_pulse_C5_Q711_1120",
                # "ringup": "ringup_flux_pulse_C5_Q711_1120",
            },
        },

        # C5_Q812
        "c5_Q812_1001": {
            "singleInput": {
                "port": (con, lf_fem1, 2),
            },
            "intermediate_frequency": parametric_IF_C5_Q812_1001,
            "operations": {
                "const": "parametric_const_pulse_C5_Q812_1001",
                # "ringup": "ringup_flux_pulse_C5_Q812_1001",
            },
        },
        "c5_Q812_1102": {
            "singleInput": {
                "port": (con, lf_fem1, 2),
            },
            "intermediate_frequency": parametric_IF_C5_Q812_1102,
            "operations": {
                "const": "parametric_const_pulse_C5_Q812_1102",
                # "ringup": "ringup_flux_pulse_C5_Q812_1102",
            },
        },
        "c5_Q812_1120": {
            "singleInput": {
                "port": (con, lf_fem1, 2),
            },
            "intermediate_frequency": parametric_IF_C5_Q812_1120,
            "operations": {
                "const": "parametric_const_pulse_C5_Q812_1120",
                # "ringup": "ringup_flux_pulse_C5_Q812_1120",
            },
        },

        # C5_Q811
        "c5_Q811_1001": {
            "singleInput": {
                "port": (con, lf_fem1, 2),
            },
            "intermediate_frequency": parametric_IF_C5_Q811_1001,
            "operations": {
                "const": "parametric_const_pulse_C5_Q811_1001",
                # "ringup": "ringup_flux_pulse_C5_Q811_1001",
            },
        },
        "c5_Q811_1102": {
            "singleInput": {
                "port": (con, lf_fem1, 2),
            },
            "intermediate_frequency": parametric_IF_C5_Q811_1102,
            "operations": {
                "const": "parametric_const_pulse_C5_Q811_1102",
                # "ringup": "ringup_flux_pulse_C5_Q811_1102",
            },
        },
        "c5_Q811_1120": {
            "singleInput": {
                "port": (con, lf_fem1, 2),
            },
            "intermediate_frequency": parametric_IF_C5_Q811_1120,
            "operations": {
                "const": "parametric_const_pulse_C5_Q811_1120",
                # "ringup": "ringup_flux_pulse_C5_Q811_1120",
            },
        },

        # C5_Q1112
        "c5_Q1112_1001": {
            "singleInput": {
                "port": (con, lf_fem1, 2),
            },
            "intermediate_frequency": parametric_IF_C5_Q1112_1001,
            "operations": {
                "const": "parametric_const_pulse_C5_Q1112_1001",
                # "ringup": "ringup_flux_pulse_C5_Q1112_1001",
            },
        },
        "c5_Q1112_1102": {
            "singleInput": {
                "port": (con, lf_fem1, 2),
            },
            "intermediate_frequency": parametric_IF_C5_Q1112_1102,
            "operations": {
                "const": "parametric_const_pulse_C5_Q1112_1102",
                # "ringup": "ringup_flux_pulse_C5_Q1112_1102",
            },
        },
        "c5_Q1112_1120": {
            "singleInput": {
                "port": (con, lf_fem1, 2),
            },
            "intermediate_frequency": parametric_IF_C5_Q1112_1120,
            "operations": {
                "const": "parametric_const_pulse_C5_Q1112_1120",
                # "ringup": "ringup_flux_pulse_C5_Q1112_1120",
            },
        },

        # ---- Updated C7 blocks with port using lf_fem2 ----

        # C7_Q1112
        "c7_Q1112_1001": {
            "singleInput": {
                "port": (con, lf_fem2, 1),
            },
            "intermediate_frequency": parametric_IF_C7_Q1112_1001,
            "operations": {
                "const": "parametric_const_pulse_C7_Q1112_1001",
                # "ringup": "ringup_flux_pulse_C7_Q1112_1001",
            },
        },
        "c7_Q1112_1102": {
            "singleInput": {
                "port": (con, lf_fem2, 1),
            },
            "intermediate_frequency": parametric_IF_C7_Q1112_1102,
            "operations": {
                "const": "parametric_const_pulse_C7_Q1112_1102",
                # "ringup": "ringup_flux_pulse_C7_Q1112_1102",
            },
        },
        "c7_Q1112_1120": {
            "singleInput": {
                "port": (con, lf_fem2, 1),
            },
            "intermediate_frequency": parametric_IF_C7_Q1112_1120,
            "operations": {
                "const": "parametric_const_pulse_C7_Q1112_1120",
                # "ringup": "ringup_flux_pulse_C7_Q1112_1120",
            },
        },

        # C7_Q1116
        "c7_Q1116_1001": {
            "singleInput": {
                "port": (con, lf_fem2, 1),
            },
            "intermediate_frequency": parametric_IF_C7_Q1116_1001,
            "operations": {
                "const": "parametric_const_pulse_C7_Q1116_1001",
                # "ringup": "ringup_flux_pulse_C7_Q1116_1001",
            },
        },
        "c7_Q1116_1102": {
            "singleInput": {
                "port": (con, lf_fem2, 1),
            },
            "intermediate_frequency": parametric_IF_C7_Q1116_1102,
            "operations": {
                "const": "parametric_const_pulse_C7_Q1116_1102",
                # "ringup": "ringup_flux_pulse_C7_Q1116_1102",
            },
        },
        "c7_Q1116_1120": {
            "singleInput": {
                "port": (con, lf_fem2, 1),
            },
            "intermediate_frequency": parametric_IF_C7_Q1116_1120,
            "operations": {
                "const": "parametric_const_pulse_C7_Q1116_1120",
                # "ringup": "ringup_flux_pulse_C7_Q1116_1120",
            },
        },

        # C7_Q1115
        "c7_Q1115_1001": {
            "singleInput": {
                "port": (con, lf_fem2, 1),
            },
            "intermediate_frequency": parametric_IF_C7_Q1115_1001,
            "operations": {
                "const": "parametric_const_pulse_C7_Q1115_1001",
                # "ringup": "ringup_flux_pulse_C7_Q1115_1001",
            },
        },
        "c7_Q1115_1102": {
            "singleInput": {
                "port": (con, lf_fem2, 1),
            },
            "intermediate_frequency": parametric_IF_C7_Q1115_1102,
            "operations": {
                "const": "parametric_const_pulse_C7_Q1115_1102",
                # "ringup": "ringup_flux_pulse_C7_Q1115_1102",
            },
        },
        "c7_Q1115_1120": {
            "singleInput": {
                "port": (con, lf_fem2, 1),
            },
            "intermediate_frequency": parametric_IF_C7_Q1115_1120,
            "operations": {
                "const": "parametric_const_pulse_C7_Q1115_1120",
                # "ringup": "ringup_flux_pulse_C7_Q1115_1120",
            },
        },

        # C7_Q1216
        "c7_Q1216_1001": {
            "singleInput": {
                "port": (con, lf_fem2, 1),
            },
            "intermediate_frequency": parametric_IF_C7_Q1216_1001,
            "operations": {
                "const": "parametric_const_pulse_C7_Q1216_1001",
                # "ringup": "ringup_flux_pulse_C7_Q1216_1001",
            },
        },
        "c7_Q1216_1102": {
            "singleInput": {
                "port": (con, lf_fem2, 1),
            },
            "intermediate_frequency": parametric_IF_C7_Q1216_1102,
            "operations": {
                "const": "parametric_const_pulse_C7_Q1216_1102",
                # "ringup": "ringup_flux_pulse_C7_Q1216_1102",
            },
        },
        "c7_Q1216_1120": {
            "singleInput": {
                "port": (con, lf_fem2, 1),
            },
            "intermediate_frequency": parametric_IF_C7_Q1216_1120,
            "operations": {
                "const": "parametric_const_pulse_C7_Q1216_1120",
                # "ringup": "ringup_flux_pulse_C7_Q1216_1120",
            },
        },

        # C7_Q1215
        "c7_Q1215_1001": {
            "singleInput": {
                "port": (con, lf_fem2, 1),
            },
            "intermediate_frequency": parametric_IF_C7_Q1215_1001,
            "operations": {
                "const": "parametric_const_pulse_C7_Q1215_1001",
                # "ringup": "ringup_flux_pulse_C7_Q1215_1001",
            },
        },
        "c7_Q1215_1102": {
            "singleInput": {
                "port": (con, lf_fem2, 1),
            },
            "intermediate_frequency": parametric_IF_C7_Q1215_1102,
            "operations": {
                "const": "parametric_const_pulse_C7_Q1215_1102",
                # "ringup": "ringup_flux_pulse_C7_Q1215_1102",
            },
        },
        "c7_Q1215_1120": {
            "singleInput": {
                "port": (con, lf_fem2, 1),
            },
            "intermediate_frequency": parametric_IF_C7_Q1215_1120,
            "operations": {
                "const": "parametric_const_pulse_C7_Q1215_1120",
                # "ringup": "ringup_flux_pulse_C7_Q1215_1120",
            },
        },

        # C7_Q1516
        "c7_Q1516_1001": {
            "singleInput": {
                "port": (con, lf_fem2, 1),
            },
            "intermediate_frequency": parametric_IF_C7_Q1516_1001,
            "operations": {
                "const": "parametric_const_pulse_C7_Q1516_1001",
                # "ringup": "ringup_flux_pulse_C7_Q1516_1001",
            },
        },
        "c7_Q1516_1102": {
            "singleInput": {
                "port": (con, lf_fem2, 1),
            },
            "intermediate_frequency": parametric_IF_C7_Q1516_1102,
            "operations": {
                "const": "parametric_const_pulse_C7_Q1516_1102",
                # "ringup": "ringup_flux_pulse_C7_Q1516_1102",
            },
        },
        "c7_Q1516_1120": {
            "singleInput": {
                "port": (con, lf_fem2, 1),
            },
            "intermediate_frequency": parametric_IF_C7_Q1516_1120,
            "operations": {
                "const": "parametric_const_pulse_C7_Q1516_1120",
                # "ringup": "ringup_flux_pulse_C7_Q1516_1120",
            },
        },

        # ---- C10 blocks with port using lf_fem2 index 2 ----

        # C10_Q1516
        "c10_Q1516_1001": {
            "singleInput": {
                "port": (con, lf_fem2, 2),
            },
            "intermediate_frequency": parametric_IF_C10_Q1516_1001,
            "operations": {
                "const": "parametric_const_pulse_C10_Q1516_1001",
                # "ringup": "ringup_flux_pulse_C10_Q1516_1001",
            },
        },
        "c10_Q1516_1102": {
            "singleInput": {
                "port": (con, lf_fem2, 2),
            },
            "intermediate_frequency": parametric_IF_C10_Q1516_1102,
            "operations": {
                "const": "parametric_const_pulse_C10_Q1516_1102",
                # "ringup": "ringup_flux_pulse_C10_Q1516_1102",
            },
        },
        "c10_Q1516_1120": {
            "singleInput": {
                "port": (con, lf_fem2, 2),
            },
            "intermediate_frequency": parametric_IF_C10_Q1516_1120,
            "operations": {
                "const": "parametric_const_pulse_C10_Q1516_1120",
                # "ringup": "ringup_flux_pulse_C10_Q1516_1120",
            },
        },

        # C10_Q1520
        "c10_Q1520_1001": {
            "singleInput": {
                "port": (con, lf_fem2, 2),
            },
            "intermediate_frequency": parametric_IF_C10_Q1520_1001,
            "operations": {
                "const": "parametric_const_pulse_C10_Q1520_1001",
                # "ringup": "ringup_flux_pulse_C10_Q1520_1001",
            },
        },
        "c10_Q1520_1102": {
            "singleInput": {
                "port": (con, lf_fem2, 2),
            },
            "intermediate_frequency": parametric_IF_C10_Q1520_1102,
            "operations": {
                "const": "parametric_const_pulse_C10_Q1520_1102",
                # "ringup": "ringup_flux_pulse_C10_Q1520_1102",
            },
        },
        "c10_Q1520_1120": {
            "singleInput": {
                "port": (con, lf_fem2, 2),
            },
            "intermediate_frequency": parametric_IF_C10_Q1520_1120,
            "operations": {
                "const": "parametric_const_pulse_C10_Q1520_1120",
                # "ringup": "ringup_flux_pulse_C10_Q1520_1120",
            },
        },

        # C10_Q1519
        "c10_Q1519_1001": {
            "singleInput": {
                "port": (con, lf_fem2, 2),
            },
            "intermediate_frequency": parametric_IF_C10_Q1519_1001,
            "operations": {
                "const": "parametric_const_pulse_C10_Q1519_1001",
                # "ringup": "ringup_flux_pulse_C10_Q1519_1001",
            },
        },
        "c10_Q1519_1102": {
            "singleInput": {
                "port": (con, lf_fem2, 2),
            },
            "intermediate_frequency": parametric_IF_C10_Q1519_1102,
            "operations": {
                "const": "parametric_const_pulse_C10_Q1519_1102",
                # "ringup": "ringup_flux_pulse_C10_Q1519_1102",
            },
        },
        "c10_Q1519_1120": {
            "singleInput": {
                "port": (con, lf_fem2, 2),
            },
            "intermediate_frequency": parametric_IF_C10_Q1519_1120,
            "operations": {
                "const": "parametric_const_pulse_C10_Q1519_1120",
                # "ringup": "ringup_flux_pulse_C10_Q1519_1120",
            },
        },

        # C10_Q1620
        "c10_Q1620_1001": {
            "singleInput": {
                "port": (con, lf_fem2, 2),
            },
            "intermediate_frequency": parametric_IF_C10_Q1620_1001,
            "operations": {
                "const": "parametric_const_pulse_C10_Q1620_1001",
                # "ringup": "ringup_flux_pulse_C10_Q1620_1001",
            },
        },
        "c10_Q1620_1102": {
            "singleInput": {
                "port": (con, lf_fem2, 2),
            },
            "intermediate_frequency": parametric_IF_C10_Q1620_1102,
            "operations": {
                "const": "parametric_const_pulse_C10_Q1620_1102",
                # "ringup": "ringup_flux_pulse_C10_Q1620_1102",
            },
        },
        "c10_Q1620_1120": {
            "singleInput": {
                "port": (con, lf_fem2, 2),
            },
            "intermediate_frequency": parametric_IF_C10_Q1620_1120,
            "operations": {
                "const": "parametric_const_pulse_C10_Q1620_1120",
                # "ringup": "ringup_flux_pulse_C10_Q1620_1120",
            },
        },

        # C10_Q1619
        "c10_Q1619_1001": {
            "singleInput": {
                "port": (con, lf_fem2, 2),
            },
            "intermediate_frequency": parametric_IF_C10_Q1619_1001,
            "operations": {
                "const": "parametric_const_pulse_C10_Q1619_1001",
                # "ringup": "ringup_flux_pulse_C10_Q1619_1001",
            },
        },
        "c10_Q1619_1102": {
            "singleInput": {
                "port": (con, lf_fem2, 2),
            },
            "intermediate_frequency": parametric_IF_C10_Q1619_1102,
            "operations": {
                "const": "parametric_const_pulse_C10_Q1619_1102",
                # "ringup": "ringup_flux_pulse_C10_Q1619_1102",
            },
        },
        "c10_Q1619_1120": {
            "singleInput": {
                "port": (con, lf_fem2, 2),
            },
            "intermediate_frequency": parametric_IF_C10_Q1619_1120,
            "operations": {
                "const": "parametric_const_pulse_C10_Q1619_1120",
                # "ringup": "ringup_flux_pulse_C10_Q1619_1120",
            },
        },

        # C10_Q1920
        "c10_Q1920_1001": {
            "singleInput": {
                "port": (con, lf_fem2, 2),
            },
            "intermediate_frequency": parametric_IF_C10_Q1920_1001,
            "operations": {
                "const": "parametric_const_pulse_C10_Q1920_1001",
                # "ringup": "ringup_flux_pulse_C10_Q1920_1001",
            },
        },
        "c10_Q1920_1102": {
            "singleInput": {
                "port": (con, lf_fem2, 2),
            },
            "intermediate_frequency": parametric_IF_C10_Q1920_1102,
            "operations": {
                "const": "parametric_const_pulse_C10_Q1920_1102",
                # "ringup": "ringup_flux_pulse_C10_Q1920_1102",
            },
        },
        "c10_Q1920_1120": {
            "singleInput": {
                "port": (con, lf_fem2, 2),
            },
            "intermediate_frequency": parametric_IF_C10_Q1920_1120,
            "operations": {
                "const": "parametric_const_pulse_C10_Q1920_1120",
                # "ringup": "ringup_flux_pulse_C10_Q1920_1120",
            },
        },

        # C2_Q37
        "c2_Q37_1001": {
            "singleInput": {
                "port": (con, lf_fem1, 3),
            },
            "intermediate_frequency": parametric_IF_C2_Q37_1001,
            "operations": {
                "const": "parametric_const_pulse_C2_Q37_1001",
                # "ringup": "ringup_flux_pulse_C2_Q37_1001",
            },
        },
        "c2_Q37_1102": {
            "singleInput": {
                "port": (con, lf_fem1, 3),
            },
            "intermediate_frequency": parametric_IF_C2_Q37_1102,
            "operations": {
                "const": "parametric_const_pulse_C2_Q37_1102",
                # "ringup": "ringup_flux_pulse_C2_Q37_1102",
            },
        },
        "c2_Q37_1120": {
            "singleInput": {
                "port": (con, lf_fem1, 3),
            },
            "intermediate_frequency": parametric_IF_C2_Q37_1120,
            "operations": {
                "const": "parametric_const_pulse_C2_Q37_1120",
                # "ringup": "ringup_flux_pulse_C2_Q37_1120",
            },
        },

        # C2_Q36
        "c2_Q36_1001": {
            "singleInput": {
                "port": (con, lf_fem1, 3),
            },
            "intermediate_frequency": parametric_IF_C2_Q36_1001,
            "operations": {
                "const": "parametric_const_pulse_C2_Q36_1001",
                # "ringup": "ringup_flux_pulse_C2_Q36_1001",
            },
        },
        "c2_Q36_1102": {
            "singleInput": {
                "port": (con, lf_fem1, 3),
            },
            "intermediate_frequency": parametric_IF_C2_Q36_1102,
            "operations": {
                "const": "parametric_const_pulse_C2_Q36_1102",
                # "ringup": "ringup_flux_pulse_C2_Q36_1102",
            },
        },
        "c2_Q36_1120": {
            "singleInput": {
                "port": (con, lf_fem1, 3),
            },
            "intermediate_frequency": parametric_IF_C2_Q36_1120,
            "operations": {
                "const": "parametric_const_pulse_C2_Q36_1120",
                # "ringup": "ringup_flux_pulse_C2_Q36_1120",
            },
        },

        # C2_Q67
        "c2_Q67_1001": {
            "singleInput": {
                "port": (con, lf_fem1, 3),
            },
            "intermediate_frequency": parametric_IF_C2_Q67_1001,
            "operations": {
                "const": "parametric_const_pulse_C2_Q67_1001",
                # "ringup": "ringup_flux_pulse_C2_Q67_1001",
            },
        },
        "c2_Q67_1102": {
            "singleInput": {
                "port": (con, lf_fem1, 3),
            },
            "intermediate_frequency": parametric_IF_C2_Q67_1102,
            "operations": {
                "const": "parametric_const_pulse_C2_Q67_1102",
                # "ringup": "ringup_flux_pulse_C2_Q67_1102",
            },
        },
        "c2_Q67_1120": {
            "singleInput": {
                "port": (con, lf_fem1, 3),
            },
            "intermediate_frequency": parametric_IF_C2_Q67_1120,
            "operations": {
                "const": "parametric_const_pulse_C2_Q67_1120",
                # "ringup": "ringup_flux_pulse_C2_Q67_1120",
            },
        },

        # C9_Q1519
        "c9_Q1519_1001": {
            "singleInput": {
                "port": (con, lf_fem1, 1),
            },
            "intermediate_frequency": parametric_IF_C9_Q1519_1001,
            "operations": {
                "const": "parametric_const_pulse_C9_Q1519_1001",
                # "ringup": "ringup_flux_pulse_C9_Q1519_1001",
            },
        },
        "c9_Q1519_1102": {
            "singleInput": {
                "port": (con, lf_fem1, 1),
            },
            "intermediate_frequency": parametric_IF_C9_Q1519_1102,
            "operations": {
                "const": "parametric_const_pulse_C9_Q1519_1102",
                # "ringup": "ringup_flux_pulse_C9_Q1519_1102",
            },
        },
        "c9_Q1519_1120": {
            "singleInput": {
                "port": (con, lf_fem1, 1),
            },
            "intermediate_frequency": parametric_IF_C9_Q1519_1120,
            "operations": {
                "const": "parametric_const_pulse_C9_Q1519_1120",
                # "ringup": "ringup_flux_pulse_C9_Q1519_1120",
            },
        },

        # C9_Q1415
        "c9_Q1415_1001": {
            "singleInput": {
                "port": (con, lf_fem1, 1),
            },
            "intermediate_frequency": parametric_IF_C9_Q1415_1001,
            "operations": {
                "const": "parametric_const_pulse_C9_Q1415_1001",
                # "ringup": "ringup_flux_pulse_C9_Q1415_1001",
            },
        },
        "c9_Q1415_1102": {
            "singleInput": {
                "port": (con, lf_fem1, 1),
            },
            "intermediate_frequency": parametric_IF_C9_Q1415_1102,
            "operations": {
                "const": "parametric_const_pulse_C9_Q1415_1102",
                # "ringup": "ringup_flux_pulse_C9_Q1415_1102",
            },
        },
        "c9_Q1415_1120": {
            "singleInput": {
                "port": (con, lf_fem1, 1),
            },
            "intermediate_frequency": parametric_IF_C9_Q1415_1120,
            "operations": {
                "const": "parametric_const_pulse_C9_Q1415_1120",
                # "ringup": "ringup_flux_pulse_C9_Q1415_1120",
            },
        },

        # C9_Q1419
        "c9_Q1419_1001": {
            "singleInput": {
                "port": (con, lf_fem1, 1),
            },
            "intermediate_frequency": parametric_IF_C9_Q1419_1001,
            "operations": {
                "const": "parametric_const_pulse_C9_Q1419_1001",
                # "ringup": "ringup_flux_pulse_C9_Q1419_1001",
            },
        },
        "c9_Q1419_1102": {
            "singleInput": {
                "port": (con, lf_fem1, 1),
            },
            "intermediate_frequency": parametric_IF_C9_Q1419_1102,
            "operations": {
                "const": "parametric_const_pulse_C9_Q1419_1102",
                # "ringup": "ringup_flux_pulse_C9_Q1419_1102",
            },
        },
        "c9_Q1419_1120": {
            "singleInput": {
                "port": (con, lf_fem1, 1),
            },
            "intermediate_frequency": parametric_IF_C9_Q1419_1120,
            "operations": {
                "const": "parametric_const_pulse_C9_Q1419_1120",
                # "ringup": "ringup_flux_pulse_C9_Q1419_1120",
            },
        },



        "c7_dc": { 
        "singleInput": {
            "port": (con, lf_fem2, 1),
            
        },
    
        "intermediate_frequency": 0,
        
        "operations": {}
        },

        "c5_dc": { 
        "singleInput": {
            "port": (con, lf_fem1, 2),
            
        },
        
        "intermediate_frequency": 0,
        
        "operations": {}
        },

        "c10_dc": { 
        "singleInput": {
            "port": (con, lf_fem2, 2),
            
        },
        
        "intermediate_frequency": 0,
        
        "operations": {}
        },

        "c3_dc": { 
        "singleInput": {
            "port": (con, lf_fem1, 4),
            
        },
        
        "intermediate_frequency": 0,
        
        "operations": {}
        },

        

        "dc_pulse_element": {
            "singleInput": {"port": (con, lf_fem2, 2)},
            "operations": {
                "const_dc": "const_pulse_op",
            },
        },
        # "sine_wave_element": {
        #     "singleInput": {"port": (con, lf_fem1, 4)},
        #     "operations": {
        #         "sine_10MHz": "sine_pulse_op",
        #     },
        #     # "mixInputs": {  # Required for generating sine waves with NCO
        #     #     "I": (con, lf_fem1, 4),
        #     #     "Q": (con, lf_fem1, 4), # Q is not strictly needed for single sideband, but good practice
        #     #                        # for I/Q mixers if you use them. For LF-FEM, it's a single analog out.
        #     #     "lo_frequency": 0, # NCO is used for direct digital synthesis
        #     #     "mixer": "mixer_LF_FEM_port3"
        #     # }
        # },



        
        # "c8_Q1718_1001": {
        #     "singleInput": {
        #         "port": (con, lf_fem2, 2),
        #     },
        #     "intermediate_frequency": parametric_IF_C8_Q1718_1001,
        #     "operations": {
        #         "const": "parametric_const_pulse_C8_Q1718_1001",
        #         # "ringup": "ringup_flux_pulse_C8_Q1718_1001",
                
        #     },
        # },


        # C1_Q0102_1001

        # parametric_IF_C1_Q0102_1001 = 
        # C1_Q0102_1102
        # C1_Q0102_1120

        # C1_Q0104_1001
        
        
        # "q2_z": {
        #     "singleInput": {
        #         "port": (con, lf_fem2, 1),
        #     },
        #     "intermediate_frequency": parametric_IF2,
        #     "operations": {
        #         "const": "const_flux_pulse",
        #     },
        # },
        # "q3_z": {
        #     "singleInput": {
        #         "port": (con, lf_fem2, 2),
        #     },
        #     "operations": {
        #         "const": "const_flux_pulse",
        #     },
        # },

    },
    "pulses": {
        # "const_flux_pulse": {
        #     "operation": "control",
        #     "length": const_flux_len,
        #     "waveforms": {
        #         "single": "const_flux_wf",
        #     },
        # },
        "gauss_flux_pulse": {
            "operation": "control",
            "length": gauss_flux_len,
            "waveforms": {
                "single": "gauss_flux_wf",
            },
        },
        "const_flux_pulse_C12_1001": {
            "operation": "control",
            "length": const_flux_len_C12_1001,
            "waveforms": {
                "single": "const_flux_wf_C12_1001",
            },
        },
        "const_flux_pulse_C12_1120": {
            "operation": "control",
            "length": const_flux_len_C12_1120,
            "waveforms": {
                "single": "const_flux_wf_C12_1120",
            },
        },
        "const_flux_pulse_C12_1102": {
            "operation": "control",
            "length": const_flux_len_C12_1102,
            "waveforms": {
                "single": "const_flux_wf_C12_1102",
            },
        },
        

        #C1
        "parametric_const_pulse_C1_Q12_1001": {
            "operation": "control",
            "length": parametric_const_len_C1_Q12_1001,
            "waveforms": {
                "single": "parametric_const_wf_C1_Q12_1001"
            }
        },
        "parametric_const_pulse_C1_Q12_1102": {
            "operation": "control",
            "length": parametric_const_len_C1_Q12_1102,
            "waveforms": {
                "single": "parametric_const_wf_C1_Q12_1102"
            }
        },
        "parametric_const_pulse_C1_Q12_1120": {
            "operation": "control",
            "length": parametric_const_len_C1_Q12_1120,
            "waveforms": {
                "single": "parametric_const_wf_C1_Q12_1120"
            }
        },

        "parametric_const_pulse_C1_Q15_1001": {
            "operation": "control",
            "length": parametric_const_len_C1_Q15_1001,
            "waveforms": {
                "single": "parametric_const_wf_C1_Q15_1001"
            }
        },
        "parametric_const_pulse_C1_Q15_1102": {
            "operation": "control",
            "length": parametric_const_len_C1_Q15_1102,
            "waveforms": {
                "single": "parametric_const_wf_C1_Q15_1102"
            }
        },
        "parametric_const_pulse_C1_Q15_1120": {
            "operation": "control",
            "length": parametric_const_len_C1_Q15_1120,
            "waveforms": {
                "single": "parametric_const_wf_C1_Q15_1120"
            }
        },

        "parametric_const_pulse_C1_Q16_1001": {
            "operation": "control",
            "length": parametric_const_len_C1_Q16_1001,
            "waveforms": {
                "single": "parametric_const_wf_C1_Q16_1001"
            }
        },
        "parametric_const_pulse_C1_Q16_1102": {
            "operation": "control",
            "length": parametric_const_len_C1_Q16_1102,
            "waveforms": {
                "single": "parametric_const_wf_C1_Q16_1102"
            }
        },
        "parametric_const_pulse_C1_Q16_1120": {
            "operation": "control",
            "length": parametric_const_len_C1_Q16_1120,
            "waveforms": {
                "single": "parametric_const_wf_C1_Q16_1120"
            }
        },

        "parametric_const_pulse_C1_Q25_1001": {
            "operation": "control",
            "length": parametric_const_len_C1_Q25_1001,
            "waveforms": {
                "single": "parametric_const_wf_C1_Q25_1001"
            }
        },
        "parametric_const_pulse_C1_Q25_1102": {
            "operation": "control",
            "length": parametric_const_len_C1_Q25_1102,
            "waveforms": {
                "single": "parametric_const_wf_C1_Q25_1102"
            }
        },
        "parametric_const_pulse_C1_Q25_1120": {
            "operation": "control",
            "length": parametric_const_len_C1_Q25_1120,
            "waveforms": {
                "single": "parametric_const_wf_C1_Q25_1120"
            }
        },

        "parametric_const_pulse_C1_Q26_1001": {
            "operation": "control",
            "length": parametric_const_len_C1_Q26_1001,
            "waveforms": {
                "single": "parametric_const_wf_C1_Q26_1001"
            }
        },
        "parametric_const_pulse_C1_Q26_1102": {
            "operation": "control",
            "length": parametric_const_len_C1_Q26_1102,
            "waveforms": {
                "single": "parametric_const_wf_C1_Q26_1102"
            }
        },
        "parametric_const_pulse_C1_Q26_1120": {
            "operation": "control",
            "length": parametric_const_len_C1_Q26_1120,
            "waveforms": {
                "single": "parametric_const_wf_C1_Q26_1120"
            }
        },

        "parametric_const_pulse_C1_Q56_1001": {
            "operation": "control",
            "length": parametric_const_len_C1_Q56_1001,
            "waveforms": {
                "single": "parametric_const_wf_C1_Q56_1001"
            }
        },
        "parametric_const_pulse_C1_Q56_1102": {
            "operation": "control",
            "length": parametric_const_len_C1_Q56_1102,
            "waveforms": {
                "single": "parametric_const_wf_C1_Q56_1102"
            }
        },
        "parametric_const_pulse_C1_Q56_1120": {
            "operation": "control",
            "length": parametric_const_len_C1_Q56_1120,
            "waveforms": {
                "single": "parametric_const_wf_C1_Q56_1120"
            }
        },

        #C4
        "parametric_const_pulse_C4_Q56_1001": {
            "operation": "control",
            "length": parametric_const_len_C4_Q56_1001,
            "waveforms": {
                "single": "parametric_const_wf_C4_Q56_1001"
            }
        },
        "parametric_const_pulse_C4_Q56_1102": {
            "operation": "control",
            "length": parametric_const_len_C4_Q56_1102,
            "waveforms": {
                "single": "parametric_const_wf_C4_Q56_1102"
            }
        },
        "parametric_const_pulse_C4_Q56_1120": {
            "operation": "control",
            "length": parametric_const_len_C4_Q56_1120,
            "waveforms": {
                "single": "parametric_const_wf_C4_Q56_1120"
            }
        },

        "parametric_const_pulse_C4_Q59_1001": {
            "operation": "control",
            "length": parametric_const_len_C4_Q59_1001,
            "waveforms": {
                "single": "parametric_const_wf_C4_Q59_1001"
            }
        },
        "parametric_const_pulse_C4_Q59_1102": {
            "operation": "control",
            "length": parametric_const_len_C4_Q59_1102,
            "waveforms": {
                "single": "parametric_const_wf_C4_Q59_1102"
            }
        },
        "parametric_const_pulse_C4_Q59_1120": {
            "operation": "control",
            "length": parametric_const_len_C4_Q59_1120,
            "waveforms": {
                "single": "parametric_const_wf_C4_Q59_1120"
            }
        },

        "parametric_const_pulse_C4_Q510_1001": {
            "operation": "control",
            "length": parametric_const_len_C4_Q510_1001,
            "waveforms": {
                "single": "parametric_const_wf_C4_Q510_1001"
            }
        },
        "parametric_const_pulse_C4_Q510_1102": {
            "operation": "control",
            "length": parametric_const_len_C4_Q510_1102,
            "waveforms": {
                "single": "parametric_const_wf_C4_Q510_1102"
            }
        },
        "parametric_const_pulse_C4_Q510_1120": {
            "operation": "control",
            "length": parametric_const_len_C4_Q510_1120,
            "waveforms": {
                "single": "parametric_const_wf_C4_Q510_1120"
            }
        },

        "parametric_const_pulse_C4_Q69_1001": {
            "operation": "control",
            "length": parametric_const_len_C4_Q69_1001,
            "waveforms": {
                "single": "parametric_const_wf_C4_Q69_1001"
            }
        },
        "parametric_const_pulse_C4_Q69_1102": {
            "operation": "control",
            "length": parametric_const_len_C4_Q69_1102,
            "waveforms": {
                "single": "parametric_const_wf_C4_Q69_1102"
            }
        },
        "parametric_const_pulse_C4_Q69_1120": {
            "operation": "control",
            "length": parametric_const_len_C4_Q69_1120,
            "waveforms": {
                "single": "parametric_const_wf_C4_Q69_1120"
            }
        },

        "parametric_const_pulse_C4_Q610_1001": {
            "operation": "control",
            "length": parametric_const_len_C4_Q610_1001,
            "waveforms": {
                "single": "parametric_const_wf_C4_Q610_1001"
            }
        },
        "parametric_const_pulse_C4_Q610_1102": {
            "operation": "control",
            "length": parametric_const_len_C4_Q610_1102,
            "waveforms": {
                "single": "parametric_const_wf_C4_Q610_1102"
            }
        },
        "parametric_const_pulse_C4_Q610_1120": {
            "operation": "control",
            "length": parametric_const_len_C4_Q610_1120,
            "waveforms": {
                "single": "parametric_const_wf_C4_Q610_1120"
            }
        },

        "parametric_const_pulse_C4_Q910_1001": {
            "operation": "control",
            "length": parametric_const_len_C4_Q910_1001,
            "waveforms": {
                "single": "parametric_const_wf_C4_Q910_1001"
            }
        },
        "parametric_const_pulse_C4_Q910_1102": {
            "operation": "control",
            "length": parametric_const_len_C4_Q910_1102,
            "waveforms": {
                "single": "parametric_const_wf_C4_Q910_1102"
            }
        },
        "parametric_const_pulse_C4_Q910_1120": {
            "operation": "control",
            "length": parametric_const_len_C4_Q910_1120,
            "waveforms": {
                "single": "parametric_const_wf_C4_Q910_1120"
            }
        },

        #C6

        "parametric_const_pulse_C6_Q910_1001": {
            "operation": "control",
            "length": parametric_const_len_C6_Q910_1001,
            "waveforms": {
                "single": "parametric_const_wf_C6_Q910_1001"
            }
        },
        "parametric_const_pulse_C6_Q910_1102": {
            "operation": "control",
            "length": parametric_const_len_C6_Q910_1102,
            "waveforms": {
                "single": "parametric_const_wf_C6_Q910_1102"
            }
        },
        "parametric_const_pulse_C6_Q910_1120": {
            "operation": "control",
            "length": parametric_const_len_C6_Q910_1120,
            "waveforms": {
                "single": "parametric_const_wf_C6_Q910_1120"
            }
        },

        "parametric_const_pulse_C6_Q913_1001": {
            "operation": "control",
            "length": parametric_const_len_C6_Q913_1001,
            "waveforms": {
                "single": "parametric_const_wf_C6_Q913_1001"
            }
        },
        "parametric_const_pulse_C6_Q913_1102": {
            "operation": "control",
            "length": parametric_const_len_C6_Q913_1102,
            "waveforms": {
                "single": "parametric_const_wf_C6_Q913_1102"
            }
        },
        "parametric_const_pulse_C6_Q913_1120": {
            "operation": "control",
            "length": parametric_const_len_C6_Q913_1120,
            "waveforms": {
                "single": "parametric_const_wf_C6_Q913_1120"
            }
        },

        "parametric_const_pulse_C6_Q914_1001": {
            "operation": "control",
            "length": parametric_const_len_C6_Q914_1001,
            "waveforms": {
                "single": "parametric_const_wf_C6_Q914_1001"
            }
        },
        "parametric_const_pulse_C6_Q914_1102": {
            "operation": "control",
            "length": parametric_const_len_C6_Q914_1102,
            "waveforms": {
                "single": "parametric_const_wf_C6_Q914_1102"
            }
        },
        "parametric_const_pulse_C6_Q914_1120": {
            "operation": "control",
            "length": parametric_const_len_C6_Q914_1120,
            "waveforms": {
                "single": "parametric_const_wf_C6_Q914_1120"
            }
        },

        "parametric_const_pulse_C6_Q1013_1001": {
            "operation": "control",
            "length": parametric_const_len_C6_Q1013_1001,
            "waveforms": {
                "single": "parametric_const_wf_C6_Q1013_1001"
            }
        },
        "parametric_const_pulse_C6_Q1013_1102": {
            "operation": "control",
            "length": parametric_const_len_C6_Q1013_1102,
            "waveforms": {
                "single": "parametric_const_wf_C6_Q1013_1102"
            }
        },
        "parametric_const_pulse_C6_Q1013_1120": {
            "operation": "control",
            "length": parametric_const_len_C6_Q1013_1120,
            "waveforms": {
                "single": "parametric_const_wf_C6_Q1013_1120"
            }
        },

        "parametric_const_pulse_C6_Q1014_1001": {
            "operation": "control",
            "length": parametric_const_len_C6_Q1014_1001,
            "waveforms": {
                "single": "parametric_const_wf_C6_Q1014_1001"
            }
        },
        "parametric_const_pulse_C6_Q1014_1102": {
            "operation": "control",
            "length": parametric_const_len_C6_Q1014_1102,
            "waveforms": {
                "single": "parametric_const_wf_C6_Q1014_1102"
            }
        },
        "parametric_const_pulse_C6_Q1014_1120": {
            "operation": "control",
            "length": parametric_const_len_C6_Q1014_1120,
            "waveforms": {
                "single": "parametric_const_wf_C6_Q1014_1120"
            }
        },

        "parametric_const_pulse_C6_Q1314_1001": {
            "operation": "control",
            "length": parametric_const_len_C6_Q1314_1001,
            "waveforms": {
                "single": "parametric_const_wf_C6_Q1314_1001"
            }
        },
        "parametric_const_pulse_C6_Q1314_1102": {
            "operation": "control",
            "length": parametric_const_len_C6_Q1314_1102,
            "waveforms": {
                "single": "parametric_const_wf_C6_Q1314_1102"
            }
        },
        "parametric_const_pulse_C6_Q1314_1120": {
            "operation": "control",
            "length": parametric_const_len_C6_Q1314_1120,
            "waveforms": {
                "single": "parametric_const_wf_C6_Q1314_1120"
            }
        },

        #C8
        "parametric_const_pulse_C8_Q1314_1001": {
            "operation": "control",
            "length": parametric_const_len_C8_Q1314_1001,
            "waveforms": {
                "single": "parametric_const_wf_C8_Q1314_1001",
            },
        },

        "parametric_const_pulse_C8_Q1314_1102": {
            "operation": "control",
            "length": parametric_const_len_C8_Q1314_1102,
            "waveforms": {
                "single": "parametric_const_wf_C8_Q1314_1102",
            },
        },

        "parametric_const_pulse_C8_Q1314_1120": {
            "operation": "control",
            "length": parametric_const_len_C8_Q1314_1120,
            "waveforms": {
                "single": "parametric_const_wf_C8_Q1314_1120",
            },
        },

        "parametric_const_pulse_C8_Q1317_1001": {
            "operation": "control",
            "length": parametric_const_len_C8_Q1317_1001,
            "waveforms": {
                "single": "parametric_const_wf_C8_Q1317_1001",
            },
        },

        "parametric_const_pulse_C8_Q1317_1102": {
            "operation": "control",
            "length": parametric_const_len_C8_Q1317_1102,
            "waveforms": {
                "single": "parametric_const_wf_C8_Q1317_1102",
            },
        },

        "parametric_const_pulse_C8_Q1317_1120": {
            "operation": "control",
            "length": parametric_const_len_C8_Q1317_1120,
            "waveforms": {
                "single": "parametric_const_wf_C8_Q1317_1120",
            },
        },

        "parametric_const_pulse_C8_Q1318_1001": {
            "operation": "control",
            "length": parametric_const_len_C8_Q1318_1001,
            "waveforms": {
                "single": "parametric_const_wf_C8_Q1318_1001",
            },
        },

        "parametric_const_pulse_C8_Q1318_1102": {
            "operation": "control",
            "length": parametric_const_len_C8_Q1318_1102,
            "waveforms": {
                "single": "parametric_const_wf_C8_Q1318_1102",
            },
        },

        "parametric_const_pulse_C8_Q1318_1120": {
            "operation": "control",
            "length": parametric_const_len_C8_Q1318_1120,
            "waveforms": {
                "single": "parametric_const_wf_C8_Q1318_1120",
            },
        },

        "parametric_const_pulse_C8_Q1417_1001": {
            "operation": "control",
            "length": parametric_const_len_C8_Q1417_1001,
            "waveforms": {
                "single": "parametric_const_wf_C8_Q1417_1001",
            },
        },

        "parametric_const_pulse_C8_Q1417_1102": {
            "operation": "control",
            "length": parametric_const_len_C8_Q1417_1102,
            "waveforms": {
                "single": "parametric_const_wf_C8_Q1417_1102",
            },
        },

        "parametric_const_pulse_C8_Q1417_1120": {
            "operation": "control",
            "length": parametric_const_len_C8_Q1417_1120,
            "waveforms": {
                "single": "parametric_const_wf_C8_Q1417_1120",
            },
        },

        "parametric_const_pulse_C8_Q1418_1001": {
            "operation": "control",
            "length": parametric_const_len_C8_Q1418_1001,
            "waveforms": {
                "single": "parametric_const_wf_C8_Q1418_1001",
            },
        },

        "parametric_const_pulse_C8_Q1418_1102": {
            "operation": "control",
            "length": parametric_const_len_C8_Q1418_1102,
            "waveforms": {
                "single": "parametric_const_wf_C8_Q1418_1102",
            },
        },

        "parametric_const_pulse_C8_Q1418_1120": {
            "operation": "control",
            "length": parametric_const_len_C8_Q1418_1120,
            "waveforms": {
                "single": "parametric_const_wf_C8_Q1418_1120",
            },
        },

        "parametric_const_pulse_C8_Q1718_1001": {
            "operation": "control",
            "length": parametric_const_len_C8_Q1718_1001,
            "waveforms": {
                "single": "parametric_const_wf_C8_Q1718_1001",
            },
        },

        "parametric_const_pulse_C8_Q1718_1102": {
            "operation": "control",
            "length": parametric_const_len_C8_Q1718_1102,
            "waveforms": {
                "single": "parametric_const_wf_C8_Q1718_1102",
            },
        },

        "parametric_const_pulse_C8_Q1718_1120": {
            "operation": "control",
            "length": parametric_const_len_C8_Q1718_1120,
            "waveforms": {
                "single": "parametric_const_wf_C8_Q1718_1120",
            },
        },

#COOLDOWN2
        # ---- C3 pulses ----

        # C3_Q34
        "parametric_const_pulse_C3_Q34_1001": {
            "operation": "control",
            "length": parametric_const_len_C3_Q34_1001,
            "waveforms": {
                "single": "parametric_const_wf_C3_Q34_1001",
            },
        },
        "parametric_const_pulse_C3_Q34_1102": {
            "operation": "control",
            "length": parametric_const_len_C3_Q34_1102,
            "waveforms": {
                "single": "parametric_const_wf_C3_Q34_1102",
            },
        },
        "parametric_const_pulse_C3_Q34_1120": {
            "operation": "control",
            "length": parametric_const_len_C3_Q34_1120,
            "waveforms": {
                "single": "parametric_const_wf_C3_Q34_1120",
            },
        },

        # C3_Q38
        "parametric_const_pulse_C3_Q38_1001": {
            "operation": "control",
            "length": parametric_const_len_C3_Q38_1001,
            "waveforms": {
                "single": "parametric_const_wf_C3_Q38_1001",
            },
        },
        "parametric_const_pulse_C3_Q38_1102": {
            "operation": "control",
            "length": parametric_const_len_C3_Q38_1102,
            "waveforms": {
                "single": "parametric_const_wf_C3_Q38_1102",
            },
        },
        "parametric_const_pulse_C3_Q38_1120": {
            "operation": "control",
            "length": parametric_const_len_C3_Q38_1120,
            "waveforms": {
                "single": "parametric_const_wf_C3_Q38_1120",
            },
        },

        # C3_Q37
        "parametric_const_pulse_C3_Q37_1001": {
            "operation": "control",
            "length": parametric_const_len_C3_Q37_1001,
            "waveforms": {
                "single": "parametric_const_wf_C3_Q37_1001",
            },
        },
        "parametric_const_pulse_C3_Q37_1102": {
            "operation": "control",
            "length": parametric_const_len_C3_Q37_1102,
            "waveforms": {
                "single": "parametric_const_wf_C3_Q37_1102",
            },
        },
        "parametric_const_pulse_C3_Q37_1120": {
            "operation": "control",
            "length": parametric_const_len_C3_Q37_1120,
            "waveforms": {
                "single": "parametric_const_wf_C3_Q37_1120",
            },
        },

        # C3_Q48
        "parametric_const_pulse_C3_Q48_1001": {
            "operation": "control",
            "length": parametric_const_len_C3_Q48_1001,
            "waveforms": {
                "single": "parametric_const_wf_C3_Q48_1001",
            },
        },
        "parametric_const_pulse_C3_Q48_1102": {
            "operation": "control",
            "length": parametric_const_len_C3_Q48_1102,
            "waveforms": {
                "single": "parametric_const_wf_C3_Q48_1102",
            },
        },
        "parametric_const_pulse_C3_Q48_1120": {
            "operation": "control",
            "length": parametric_const_len_C3_Q48_1120,
            "waveforms": {
                "single": "parametric_const_wf_C3_Q48_1120",
            },
        },

        # C3_Q47
        "parametric_const_pulse_C3_Q47_1001": {
            "operation": "control",
            "length": parametric_const_len_C3_Q47_1001,
            "waveforms": {
                "single": "parametric_const_wf_C3_Q47_1001",
            },
        },
        "parametric_const_pulse_C3_Q47_1102": {
            "operation": "control",
            "length": parametric_const_len_C3_Q47_1102,
            "waveforms": {
                "single": "parametric_const_wf_C3_Q47_1102",
            },
        },
        "parametric_const_pulse_C3_Q47_1120": {
            "operation": "control",
            "length": parametric_const_len_C3_Q47_1120,
            "waveforms": {
                "single": "parametric_const_wf_C3_Q47_1120",
            },
        },

        # C3_Q78
        "parametric_const_pulse_C3_Q78_1001": {
            "operation": "control",
            "length": parametric_const_len_C3_Q78_1001,
            "waveforms": {
                "single": "parametric_const_wf_C3_Q78_1001",
            },
        },
        "parametric_const_pulse_C3_Q78_1102": {
            "operation": "control",
            "length": parametric_const_len_C3_Q78_1102,
            "waveforms": {
                "single": "parametric_const_wf_C3_Q78_1102",
            },
        },
        "parametric_const_pulse_C3_Q78_1120": {
            "operation": "control",
            "length": parametric_const_len_C3_Q78_1120,
            "waveforms": {
                "single": "parametric_const_wf_C3_Q78_1120",
            },
        },

        # ---- C5 pulses ----

        # C5_Q78
        "parametric_const_pulse_C5_Q78_1001": {
            "operation": "control",
            "length": parametric_const_len_C5_Q78_1001,
            "waveforms": {
                "single": "parametric_const_wf_C5_Q78_1001",
            },
        },
        "parametric_const_pulse_C5_Q78_1102": {
            "operation": "control",
            "length": parametric_const_len_C5_Q78_1102,
            "waveforms": {
                "single": "parametric_const_wf_C5_Q78_1102",
            },
        },
        "parametric_const_pulse_C5_Q78_1120": {
            "operation": "control",
            "length": parametric_const_len_C5_Q78_1120,
            "waveforms": {
                "single": "parametric_const_wf_C5_Q78_1120",
            },
        },

        # C5_Q712
        "parametric_const_pulse_C5_Q712_1001": {
            "operation": "control",
            "length": parametric_const_len_C5_Q712_1001,
            "waveforms": {
                "single": "parametric_const_wf_C5_Q712_1001",
            },
        },
        "parametric_const_pulse_C5_Q712_1102": {
            "operation": "control",
            "length": parametric_const_len_C5_Q712_1102,
            "waveforms": {
                "single": "parametric_const_wf_C5_Q712_1102",
            },
        },
        "parametric_const_pulse_C5_Q712_1120": {
            "operation": "control",
            "length": parametric_const_len_C5_Q712_1120,
            "waveforms": {
                "single": "parametric_const_wf_C5_Q712_1120",
            },
        },

        # C5_Q711
        "parametric_const_pulse_C5_Q711_1001": {
            "operation": "control",
            "length": parametric_const_len_C5_Q711_1001,
            "waveforms": {
                "single": "parametric_const_wf_C5_Q711_1001",
            },
        },
        "parametric_const_pulse_C5_Q711_1102": {
            "operation": "control",
            "length": parametric_const_len_C5_Q711_1102,
            "waveforms": {
                "single": "parametric_const_wf_C5_Q711_1102",
            },
        },
        "parametric_const_pulse_C5_Q711_1120": {
            "operation": "control",
            "length": parametric_const_len_C5_Q711_1120,
            "waveforms": {
                "single": "parametric_const_wf_C5_Q711_1120",
            },
        },

        # C5_Q812
        "parametric_const_pulse_C5_Q812_1001": {
            "operation": "control",
            "length": parametric_const_len_C5_Q812_1001,
            "waveforms": {
                "single": "parametric_const_wf_C5_Q812_1001",
            },
        },
        "parametric_const_pulse_C5_Q812_1102": {
            "operation": "control",
            "length": parametric_const_len_C5_Q812_1102,
            "waveforms": {
                "single": "parametric_const_wf_C5_Q812_1102",
            },
        },
        "parametric_const_pulse_C5_Q812_1120": {
            "operation": "control",
            "length": parametric_const_len_C5_Q812_1120,
            "waveforms": {
                "single": "parametric_const_wf_C5_Q812_1120",
            },
        },

        # C5_Q811
        "parametric_const_pulse_C5_Q811_1001": {
            "operation": "control",
            "length": parametric_const_len_C5_Q811_1001,
            "waveforms": {
                "single": "parametric_const_wf_C5_Q811_1001",
            },
        },
        "parametric_const_pulse_C5_Q811_1102": {
            "operation": "control",
            "length": parametric_const_len_C5_Q811_1102,
            "waveforms": {
                "single": "parametric_const_wf_C5_Q811_1102",
            },
        },
        "parametric_const_pulse_C5_Q811_1120": {
            "operation": "control",
            "length": parametric_const_len_C5_Q811_1120,
            "waveforms": {
                "single": "parametric_const_wf_C5_Q811_1120",
            },
        },

        # C5_Q1112
        "parametric_const_pulse_C5_Q1112_1001": {
            "operation": "control",
            "length": parametric_const_len_C5_Q1112_1001,
            "waveforms": {
                "single": "parametric_const_wf_C5_Q1112_1001",
            },
        },
        "parametric_const_pulse_C5_Q1112_1102": {
            "operation": "control",
            "length": parametric_const_len_C5_Q1112_1102,
            "waveforms": {
                "single": "parametric_const_wf_C5_Q1112_1102",
            },
        },
        "parametric_const_pulse_C5_Q1112_1120": {
            "operation": "control",
            "length": parametric_const_len_C5_Q1112_1120,
            "waveforms": {
                "single": "parametric_const_wf_C5_Q1112_1120",
            },
        },

        # ---- C7 pulses ----

        # C7_Q1112
        "parametric_const_pulse_C7_Q1112_1001": {
            "operation": "control",
            "length": parametric_const_len_C7_Q1112_1001,
            "waveforms": {
                "single": "parametric_const_wf_C7_Q1112_1001",
            },
        },
        "parametric_const_pulse_C7_Q1112_1102": {
            "operation": "control",
            "length": parametric_const_len_C7_Q1112_1102,
            "waveforms": {
                "single": "parametric_const_wf_C7_Q1112_1102",
            },
        },
        "parametric_const_pulse_C7_Q1112_1120": {
            "operation": "control",
            "length": parametric_const_len_C7_Q1112_1120,
            "waveforms": {
                "single": "parametric_const_wf_C7_Q1112_1120",
            },
        },

        # C7_Q1116
        "parametric_const_pulse_C7_Q1116_1001": {
            "operation": "control",
            "length": parametric_const_len_C7_Q1116_1001,
            "waveforms": {
                "single": "parametric_const_wf_C7_Q1116_1001",
            },
        },
        "parametric_const_pulse_C7_Q1116_1102": {
            "operation": "control",
            "length": parametric_const_len_C7_Q1116_1102,
            "waveforms": {
                "single": "parametric_const_wf_C7_Q1116_1102",
            },
        },
        "parametric_const_pulse_C7_Q1116_1120": {
            "operation": "control",
            "length": parametric_const_len_C7_Q1116_1120,
            "waveforms": {
                "single": "parametric_const_wf_C7_Q1116_1120",
            },
        },

        # C7_Q1115
        "parametric_const_pulse_C7_Q1115_1001": {
            "operation": "control",
            "length": parametric_const_len_C7_Q1115_1001,
            "waveforms": {
                "single": "parametric_const_wf_C7_Q1115_1001",
            },
        },
        "parametric_const_pulse_C7_Q1115_1102": {
            "operation": "control",
            "length": parametric_const_len_C7_Q1115_1102,
            "waveforms": { 
                "single": "parametric_const_wf_C7_Q1115_1102",
            },
        },
        "parametric_const_pulse_C7_Q1115_1120": {
            "operation": "control",
            "length": parametric_const_len_C7_Q1115_1120,
            "waveforms": {
                "single": "parametric_const_wf_C7_Q1115_1120",
            },
        },

        # C7_Q1216
        "parametric_const_pulse_C7_Q1216_1001": {
            "operation": "control",
            "length": parametric_const_len_C7_Q1216_1001,
            "waveforms": {
                "single": "parametric_const_wf_C7_Q1216_1001",
            },
        },
        "parametric_const_pulse_C7_Q1216_1102": {
            "operation": "control",
            "length": parametric_const_len_C7_Q1216_1102,
            "waveforms": {
                "single": "parametric_const_wf_C7_Q1216_1102",
            },
        },
        "parametric_const_pulse_C7_Q1216_1120": {
            "operation": "control",
            "length": parametric_const_len_C7_Q1216_1120,
            "waveforms": {
                "single": "parametric_const_wf_C7_Q1216_1120",
            },
        },

        # C7_Q1215
        "parametric_const_pulse_C7_Q1215_1001": {
            "operation": "control",
            "length": parametric_const_len_C7_Q1215_1001,
            "waveforms": {
                "single": "parametric_const_wf_C7_Q1215_1001",
            },
        },
        "parametric_const_pulse_C7_Q1215_1102": {
            "operation": "control",
            "length": parametric_const_len_C7_Q1215_1102,
            "waveforms": {
                "single": "parametric_const_wf_C7_Q1215_1102",
            },
        },
        "parametric_const_pulse_C7_Q1215_1120": {
            "operation": "control",
            "length": parametric_const_len_C7_Q1215_1120,
            "waveforms": {
                "single": "parametric_const_wf_C7_Q1215_1120",
            },
        },

        # C7_Q1516
        "parametric_const_pulse_C7_Q1516_1001": {
            "operation": "control",
            "length": parametric_const_len_C7_Q1516_1001,
            "waveforms": {
                "single": "parametric_const_wf_C7_Q1516_1001",
            },
        },
        "parametric_const_pulse_C7_Q1516_1102": {
            "operation": "control",
            "length": parametric_const_len_C7_Q1516_1102,
            "waveforms": {
                "single": "parametric_const_wf_C7_Q1516_1102",
            },
        },
        "parametric_const_pulse_C7_Q1516_1120": {
            "operation": "control",
            "length": parametric_const_len_C7_Q1516_1120,
            "waveforms": {
                "single": "parametric_const_wf_C7_Q1516_1120",
            },
        },

        # ---- C10 pulses ----

        # C10_Q1516
        "parametric_const_pulse_C10_Q1516_1001": {
            "operation": "control",
            "length": parametric_const_len_C10_Q1516_1001,
            "waveforms": {
                "single": "parametric_const_wf_C10_Q1516_1001",
            },
        },
        "parametric_const_pulse_C10_Q1516_1102": {
            "operation": "control",
            "length": parametric_const_len_C10_Q1516_1102,
            "waveforms": {
                "single": "parametric_const_wf_C10_Q1516_1102",
            },
        },
        "parametric_const_pulse_C10_Q1516_1120": {
            "operation": "control",
            "length": parametric_const_len_C10_Q1516_1120,
            "waveforms": {
                "single": "parametric_const_wf_C10_Q1516_1120",
            },
        },

        # C10_Q1520
        "parametric_const_pulse_C10_Q1520_1001": {
            "operation": "control",
            "length": parametric_const_len_C10_Q1520_1001,
            "waveforms": {
                "single": "parametric_const_wf_C10_Q1520_1001",
            },
        },
        "parametric_const_pulse_C10_Q1520_1102": {
            "operation": "control",
            "length": parametric_const_len_C10_Q1520_1102,
            "waveforms": {
                "single": "parametric_const_wf_C10_Q1520_1102",
            },
        },
        "parametric_const_pulse_C10_Q1520_1120": {
            "operation": "control",
            "length": parametric_const_len_C10_Q1520_1120,
            "waveforms": {
                "single": "parametric_const_wf_C10_Q1520_1120",
            },
        },

        # C10_Q1519
        "parametric_const_pulse_C10_Q1519_1001": {
            "operation": "control",
            "length": parametric_const_len_C10_Q1519_1001,
            "waveforms": {
                "single": "parametric_const_wf_C10_Q1519_1001",
            },
        },
        "parametric_const_pulse_C10_Q1519_1102": {
            "operation": "control",
            "length": parametric_const_len_C10_Q1519_1102,
            "waveforms": {
                "single": "parametric_const_wf_C10_Q1519_1102",
            },
        },
        "parametric_const_pulse_C10_Q1519_1120": {
            "operation": "control",
            "length": parametric_const_len_C10_Q1519_1120,
            "waveforms": {
                "single": "parametric_const_wf_C10_Q1519_1120",
            },
        },

        # C10_Q1620
        "parametric_const_pulse_C10_Q1620_1001": {
            "operation": "control",
            "length": parametric_const_len_C10_Q1620_1001,
            "waveforms": {
                "single": "parametric_const_wf_C10_Q1620_1001",
            },
        },
        "parametric_const_pulse_C10_Q1620_1102": {
            "operation": "control",
            "length": parametric_const_len_C10_Q1620_1102,
            "waveforms": {
                "single": "parametric_const_wf_C10_Q1620_1102",
            },
        },
        "parametric_const_pulse_C10_Q1620_1120": {
            "operation": "control",
            "length": parametric_const_len_C10_Q1620_1120,
            "waveforms": {
                "single": "parametric_const_wf_C10_Q1620_1120",
            },
        },

        # C10_Q1619
        "parametric_const_pulse_C10_Q1619_1001": {
            "operation": "control",
            "length": parametric_const_len_C10_Q1619_1001,
            "waveforms": {
                "single": "parametric_const_wf_C10_Q1619_1001",
            },
        },
        "parametric_const_pulse_C10_Q1619_1102": {
            "operation": "control",
            "length": parametric_const_len_C10_Q1619_1102,
            "waveforms": {
                "single": "parametric_const_wf_C10_Q1619_1102",
            },
        },
        "parametric_const_pulse_C10_Q1619_1120": {
            "operation": "control",
            "length": parametric_const_len_C10_Q1619_1120,
            "waveforms": {
                "single": "parametric_const_wf_C10_Q1619_1120",
            },
        },

        # C10_Q1920
        "parametric_const_pulse_C10_Q1920_1001": {
            "operation": "control",
            "length": parametric_const_len_C10_Q1920_1001,
            "waveforms": {
                "single": "parametric_const_wf_C10_Q1920_1001",
            },
        },
        "parametric_const_pulse_C10_Q1920_1102": {
            "operation": "control",
            "length": parametric_const_len_C10_Q1920_1102,
            "waveforms": {
                "single": "parametric_const_wf_C10_Q1920_1102",
            },
        },
        "parametric_const_pulse_C10_Q1920_1120": {
            "operation": "control",
            "length": parametric_const_len_C10_Q1920_1120,
            "waveforms": {
                "single": "parametric_const_wf_C10_Q1920_1120",
            },
        },

        # C2_Q37
        "parametric_const_pulse_C2_Q37_1001": {
            "operation": "control",
            "length": parametric_const_len_C2_Q37_1001,
            "waveforms": {
                "single": "parametric_const_wf_C2_Q37_1001",
            },
        },
        "parametric_const_pulse_C2_Q37_1102": {
            "operation": "control",
            "length": parametric_const_len_C2_Q37_1102,
            "waveforms": {
                "single": "parametric_const_wf_C2_Q37_1102",
            },
        },
        "parametric_const_pulse_C2_Q37_1120": {
            "operation": "control",
            "length": parametric_const_len_C2_Q37_1120,
            "waveforms": {
                "single": "parametric_const_wf_C2_Q37_1120",
            },
        },

        # C2_Q36
        "parametric_const_pulse_C2_Q36_1001": {
            "operation": "control",
            "length": parametric_const_len_C2_Q36_1001,
            "waveforms": {
                "single": "parametric_const_wf_C2_Q36_1001",
            },
        },
        "parametric_const_pulse_C2_Q36_1102": {
            "operation": "control",
            "length": parametric_const_len_C2_Q36_1102,
            "waveforms": {
                "single": "parametric_const_wf_C2_Q36_1102",
            },
        },
        "parametric_const_pulse_C2_Q36_1120": {
            "operation": "control",
            "length": parametric_const_len_C2_Q36_1120,
            "waveforms": {
                "single": "parametric_const_wf_C2_Q36_1120",
            },
        },

        # C2_Q67
        "parametric_const_pulse_C2_Q67_1001": {
            "operation": "control",
            "length": parametric_const_len_C2_Q67_1001,
            "waveforms": {
                "single": "parametric_const_wf_C2_Q67_1001",
            },
        },
        "parametric_const_pulse_C2_Q67_1102": {
            "operation": "control",
            "length": parametric_const_len_C2_Q67_1102,
            "waveforms": {
                "single": "parametric_const_wf_C2_Q67_1102",
            },
        },
        "parametric_const_pulse_C2_Q67_1120": {
            "operation": "control",
            "length": parametric_const_len_C2_Q67_1120,
            "waveforms": {
                "single": "parametric_const_wf_C2_Q67_1120",
            },
        },

        # C9_Q1519
        "parametric_const_pulse_C9_Q1519_1001": {
            "operation": "control",
            "length": parametric_const_len_C9_Q1519_1001,
            "waveforms": {
                "single": "parametric_const_wf_C9_Q1519_1001",
            },
        },
        "parametric_const_pulse_C9_Q1519_1102": {
            "operation": "control",
            "length": parametric_const_len_C9_Q1519_1102,
            "waveforms": {
                "single": "parametric_const_wf_C9_Q1519_1102",
            },
        },
        "parametric_const_pulse_C9_Q1519_1120": {
            "operation": "control",
            "length": parametric_const_len_C9_Q1519_1120,
            "waveforms": {
                "single": "parametric_const_wf_C9_Q1519_1120",
            },
        },

        # C9_Q1415
        "parametric_const_pulse_C9_Q1415_1001": {
            "operation": "control",
            "length": parametric_const_len_C9_Q1415_1001,
            "waveforms": {
                "single": "parametric_const_wf_C9_Q1415_1001",
            },
        },
        "parametric_const_pulse_C9_Q1415_1102": {
            "operation": "control",
            "length": parametric_const_len_C9_Q1415_1102,
            "waveforms": {
                "single": "parametric_const_wf_C9_Q1415_1102",
            },
        },
        "parametric_const_pulse_C9_Q1415_1120": {
            "operation": "control",
            "length": parametric_const_len_C9_Q1415_1120,
            "waveforms": {
                "single": "parametric_const_wf_C9_Q1415_1120",
            },
        },

        # C9_Q1419
        "parametric_const_pulse_C9_Q1419_1001": {
            "operation": "control",
            "length": parametric_const_len_C9_Q1419_1001,
            "waveforms": {
                "single": "parametric_const_wf_C9_Q1419_1001",
            },
        },
        "parametric_const_pulse_C9_Q1419_1102": {
            "operation": "control",
            "length": parametric_const_len_C9_Q1419_1102,
            "waveforms": {
                "single": "parametric_const_wf_C9_Q1419_1102",
            },
        },
        "parametric_const_pulse_C9_Q1419_1120": {
            "operation": "control",
            "length": parametric_const_len_C9_Q1419_1120,
            "waveforms": {
                "single": "parametric_const_wf_C9_Q1419_1120",
            },
        },








        # "parametric_const_pulse_C8_Q1718_1001": {
        #     "operation": "control",
        #     "length": parametric_const_len_C8_Q1718_1001,
        #     "waveforms": {
        #         "single": "parametric_const_wf_C8_Q1718_1001",
        #     },
        # },

        "riseup_flux_pulse_C12_1102": {
            "operation": "control",
            "length": total_len_C12_1102,
            "waveforms": {
                "single": "riseup_wf_C12_1102",
            }
        },

        "ringup_flux_pulse_C8_Q1317_1102": {
            "operation": "control",
            "length": parametric_ringup_total_len_1102,
            "waveforms": {
                "single": "ringup_wf_C8_Q1317_1102",
            }
        },


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
        # dc pulse plus a LF pulse, Harry added 
        "const_pulse_op": {
            "operation": "control",
            "length": parametric_const_len,  # in ns
            #"amplitude": 0.2, # Adjust amplitude as needed (e.g., 0.2 for 200mV)
            #"digital_marker": "ON", # Optional, for trigger/marker if needed
            "waveforms": {
                "single": "const_wf",
            },
        },
        "sine_pulse_op": {
            "operation": "control",
            "length": const_len,  # in ns
            #"amplitude": 0.5, # Adjust amplitude as needed
            #"digital_marker": "ON", # Optional
            "waveforms": {
                "single": "sine_wf",
                #"Q": "sine_Q_wf", # Q waveform for NCO based sine wave
            },
        },

        # "x90_pulse_q1": {
        #     "operation": "control",
        #     "length": pi_len,
        #     "waveforms": {
        #         "I": "x90_I_wf_q1",
        #         "Q": "x90_Q_wf_q1",
        #     },
        # },
        # "x180_pulse_q1": {
        #     "operation": "control",
        #     "length": pi_len,
        #     "waveforms": {
        #         "I": "x180_I_wf_q1",
        #         "Q": "x180_Q_wf_q1",
        #     },
        # },
        # "-x90_pulse_q1": {
        #     "operation": "control",
        #     "length": pi_len,
        #     "waveforms": {
        #         "I": "minus_x90_I_wf_q1",
        #         "Q": "minus_x90_Q_wf_q1",
        #     },
        # },
        # "y90_pulse_q1": {
        #     "operation": "control",
        #     "length": pi_len,
        #     "waveforms": {
        #         "I": "y90_I_wf_q1",
        #         "Q": "y90_Q_wf_q1",
        #     },
        # },
        # "y180_pulse_q1": {
        #     "operation": "control",
        #     "length": pi_len,
        #     "waveforms": {
        #         "I": "y180_I_wf_q1",
        #         "Q": "y180_Q_wf_q1",
        #     },
        # },
        # "-y90_pulse_q1": {
        #     "operation": "control",
        #     "length": pi_len,
        #     "waveforms": {
        #         "I": "minus_y90_I_wf_q1",
        #         "Q": "minus_y90_Q_wf_q1",
        #     },
        # },
        # "readout_pulse_q1": {
        #     "operation": "measurement",
        #     "length": readout_len,
        #     "waveforms": {
        #         "I": "readout_wf_q1",
        #         "Q": "zero_wf",
        #     },
        #     "integration_weights": {
        #         "cos": "cosine_weights",
        #         "sin": "sine_weights",
        #         "minus_sin": "minus_sine_weights",
        #         "rotated_cos": "rotated_cosine_weights_q1",
        #         "rotated_sin": "rotated_sine_weights_q1",
        #         "rotated_minus_sin": "rotated_minus_sine_weights_q1",
        #         "opt_cos": "opt_cosine_weights_q1",
        #         "opt_sin": "opt_sine_weights_q1",
        #         "opt_minus_sin": "opt_minus_sine_weights_q1",
        #     },
        #     "digital_marker": "ON",
        # },

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
        "y45_pulse_q1": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "y45_I_wf_q1",
                "Q": "y45_Q_wf_q1",
            },
        },
        "-y45_pulse_q1": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "minus_y45_I_wf_q1",
                "Q": "minus_y45_Q_wf_q1",
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
        "y45_pulse_q2": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "y45_I_wf_q2",
                "Q": "y45_Q_wf_q2",
            },
        },
        "-y45_pulse_q2": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "minus_y45_I_wf_q2",
                "Q": "minus_y45_Q_wf_q2",
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
        "y45_pulse_q3": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "y45_I_wf_q3",
                "Q": "y45_Q_wf_q3",
            },
        },
        "-y45_pulse_q3": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "minus_y45_I_wf_q3",
                "Q": "minus_y45_Q_wf_q3",
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
        "y45_pulse_q6": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "y45_I_wf_q6",
                "Q": "y45_Q_wf_q6",
            },
        },
        "-y45_pulse_q6": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "minus_y45_I_wf_q6",
                "Q": "minus_y45_Q_wf_q6",
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
        "y45_pulse_q7": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "y45_I_wf_q7",
                "Q": "y45_Q_wf_q7",
            },
        },
        "-y45_pulse_q7": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "minus_y45_I_wf_q7",
                "Q": "minus_y45_Q_wf_q7",
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

        "x90_pulse_q8": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "x90_I_wf_q8",
                "Q": "x90_Q_wf_q8",
            },
        },
        "x180_pulse_q8": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "x180_I_wf_q8",
                "Q": "x180_Q_wf_q8",
            },
        },
        "-x90_pulse_q8": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "minus_x90_I_wf_q8",
                "Q": "minus_x90_Q_wf_q8",
            },
        },
        "y90_pulse_q8": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "y90_I_wf_q8",
                "Q": "y90_Q_wf_q8",
            },
        },
        "y180_pulse_q8": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "y180_I_wf_q8",
                "Q": "y180_Q_wf_q8",
            },
        },
        "-y90_pulse_q8": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "minus_y90_I_wf_q8",
                "Q": "minus_y90_Q_wf_q8",
            },
        },
        "y45_pulse_q8": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "y45_I_wf_q8",
                "Q": "y45_Q_wf_q8",
            },
        },
        "-y45_pulse_q8": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "minus_y45_I_wf_q8",
                "Q": "minus_y45_Q_wf_q8",
            },
        },
        "readout_pulse_q8": {
            "operation": "measurement",
            "length": readout_len,
            "waveforms": {
                "I": "readout_wf_q8",
                "Q": "zero_wf",
            },
            "integration_weights": {
                "cos": "cosine_weights",
                "sin": "sine_weights",
                "minus_sin": "minus_sine_weights",
                "rotated_cos": "rotated_cosine_weights_q8",
                "rotated_sin": "rotated_sine_weights_q8",
                "rotated_minus_sin": "rotated_minus_sine_weights_q8",
                "opt_cos": "opt_cosine_weights_q8",
                "opt_sin": "opt_sine_weights_q8",
                "opt_minus_sin": "opt_minus_sine_weights_q8",
            },
            "digital_marker": "ON",
        },
                "x90_pulse_q9": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "x90_I_wf_q9",
                "Q": "x90_Q_wf_q9",
            },
        },
        "x180_pulse_q9": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "x180_I_wf_q9",
                "Q": "x180_Q_wf_q9",
            },
        },
        "-x90_pulse_q9": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "minus_x90_I_wf_q9",
                "Q": "minus_x90_Q_wf_q9",
            },
        },
        "y90_pulse_q9": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "y90_I_wf_q9",
                "Q": "y90_Q_wf_q9",
            },
        },
        "y180_pulse_q9": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "y180_I_wf_q9",
                "Q": "y180_Q_wf_q9",
            },
        },
        "-y90_pulse_q9": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "minus_y90_I_wf_q9",
                "Q": "minus_y90_Q_wf_q9",
            },
        },
        "y45_pulse_q9": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "y45_I_wf_q9",
                "Q": "y45_Q_wf_q9",
            },
        },
        "-y45_pulse_q9": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "minus_y45_I_wf_q9",
                "Q": "minus_y45_Q_wf_q9",
            },
        },
        "readout_pulse_q9": {
            "operation": "measurement",
            "length": readout_len,
            "waveforms": {
                "I": "readout_wf_q9",
                "Q": "zero_wf",
            },
            "integration_weights": {
                "cos": "cosine_weights",
                "sin": "sine_weights",
                "minus_sin": "minus_sine_weights",
                "rotated_cos": "rotated_cosine_weights_q9",
                "rotated_sin": "rotated_sine_weights_q9",
                "rotated_minus_sin": "rotated_minus_sine_weights_q9",
                "opt_cos": "opt_cosine_weights_q9",
                "opt_sin": "opt_sine_weights_q9",
                "opt_minus_sin": "opt_minus_sine_weights_q9",
            },
            "digital_marker": "ON",
        },

        "x90_pulse_q10": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "x90_I_wf_q10",
                "Q": "x90_Q_wf_q10",
            },
        },
        "x180_pulse_q10": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "x180_I_wf_q10",
                "Q": "x180_Q_wf_q10",
            },
        },
        "-x90_pulse_q10": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "minus_x90_I_wf_q10",
                "Q": "minus_x90_Q_wf_q10",
            },
        },
        "y90_pulse_q10": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "y90_I_wf_q10",
                "Q": "y90_Q_wf_q10",
            },
        },
        "y180_pulse_q10": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "y180_I_wf_q10",
                "Q": "y180_Q_wf_q10",
            },
        },
        "-y90_pulse_q10": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "minus_y90_I_wf_q10",
                "Q": "minus_y90_Q_wf_q10",
            },
        },
        "y45_pulse_q10": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "y45_I_wf_q10",
                "Q": "y45_Q_wf_q10",
            },
        },
        "-y45_pulse_q10": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "minus_y45_I_wf_q10",
                "Q": "minus_y45_Q_wf_q10",
            },
        },
        "readout_pulse_q10": {
            "operation": "measurement",
            "length": readout_len,
            "waveforms": {
                "I": "readout_wf_q10",
                "Q": "zero_wf",
            },
            "integration_weights": {
                "cos": "cosine_weights",
                "sin": "sine_weights",
                "minus_sin": "minus_sine_weights",
                "rotated_cos": "rotated_cosine_weights_q10",
                "rotated_sin": "rotated_sine_weights_q10",
                "rotated_minus_sin": "rotated_minus_sine_weights_q10",
                "opt_cos": "opt_cosine_weights_q10",
                "opt_sin": "opt_sine_weights_q10",
                "opt_minus_sin": "opt_minus_sine_weights_q10",
            },
            "digital_marker": "ON",
        },

        "x90_pulse_q11": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "x90_I_wf_q11",
                "Q": "x90_Q_wf_q11",
            },
        },
        "x180_pulse_q11": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "x180_I_wf_q11",
                "Q": "x180_Q_wf_q11",
            },
        },
        "-x90_pulse_q11": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "minus_x90_I_wf_q11",
                "Q": "minus_x90_Q_wf_q11",
            },
        },
        "y90_pulse_q11": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "y90_I_wf_q11",
                "Q": "y90_Q_wf_q11",
            },
        },
        "y180_pulse_q11": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "y180_I_wf_q11",
                "Q": "y180_Q_wf_q11",
            },
        },
        "-y90_pulse_q11": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "minus_y90_I_wf_q11",
                "Q": "minus_y90_Q_wf_q11",
            },
        },
        "y45_pulse_q11": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "y45_I_wf_q11",
                "Q": "y45_Q_wf_q11",
            },
        },
        "-y45_pulse_q11": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "minus_y45_I_wf_q11",
                "Q": "minus_y45_Q_wf_q11",
            },
        },
        "readout_pulse_q11": {
            "operation": "measurement",
            "length": readout_len,
            "waveforms": {
                "I": "readout_wf_q11",
                "Q": "zero_wf",
            },
            "integration_weights": {
                "cos": "cosine_weights",
                "sin": "sine_weights",
                "minus_sin": "minus_sine_weights",
                "rotated_cos": "rotated_cosine_weights_q11",
                "rotated_sin": "rotated_sine_weights_q11",
                "rotated_minus_sin": "rotated_minus_sine_weights_q11",
                "opt_cos": "opt_cosine_weights_q11",
                "opt_sin": "opt_sine_weights_q11",
                "opt_minus_sin": "opt_minus_sine_weights_q11",
            },
            "digital_marker": "ON",
        },

        "x90_pulse_q12": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "x90_I_wf_q12",
                "Q": "x90_Q_wf_q12",
            },
        },
        "x180_pulse_q12": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "x180_I_wf_q12",
                "Q": "x180_Q_wf_q12",
            },
        },
        "-x90_pulse_q12": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "minus_x90_I_wf_q12",
                "Q": "minus_x90_Q_wf_q12",
            },
        },
        "y90_pulse_q12": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "y90_I_wf_q12",
                "Q": "y90_Q_wf_q12",
            },
        },
        "y180_pulse_q12": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "y180_I_wf_q12",
                "Q": "y180_Q_wf_q12",
            },
        },
        "-y90_pulse_q12": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "minus_y90_I_wf_q12",
                "Q": "minus_y90_Q_wf_q12",
            },
        },
        "y45_pulse_q12": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "y45_I_wf_q12",
                "Q": "y45_Q_wf_q12",
            },
        },
        "-y45_pulse_q12": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "minus_y45_I_wf_q12",
                "Q": "minus_y45_Q_wf_q12",
            },
        },
        "readout_pulse_q12": {
            "operation": "measurement",
            "length": readout_len,
            "waveforms": {
                "I": "readout_wf_q12",
                "Q": "zero_wf",
            },
            "integration_weights": {
                "cos": "cosine_weights",
                "sin": "sine_weights",
                "minus_sin": "minus_sine_weights",
                "rotated_cos": "rotated_cosine_weights_q12",
                "rotated_sin": "rotated_sine_weights_q12",
                "rotated_minus_sin": "rotated_minus_sine_weights_q12",
                "opt_cos": "opt_cosine_weights_q12",
                "opt_sin": "opt_sine_weights_q12",
                "opt_minus_sin": "opt_minus_sine_weights_q12",
            },
            "digital_marker": "ON",
        },

                "x90_pulse_q13": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "x90_I_wf_q13",
                "Q": "x90_Q_wf_q13",
            },
        },
        "x180_pulse_q13": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "x180_I_wf_q13",
                "Q": "x180_Q_wf_q13",
            },
        },
        "-x90_pulse_q13": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "minus_x90_I_wf_q13",
                "Q": "minus_x90_Q_wf_q13",
            },
        },
        "y90_pulse_q13": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "y90_I_wf_q13",
                "Q": "y90_Q_wf_q13",
            },
        },
        "y180_pulse_q13": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "y180_I_wf_q13",
                "Q": "y180_Q_wf_q13",
            },
        },
        "-y90_pulse_q13": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "minus_y90_I_wf_q13",
                "Q": "minus_y90_Q_wf_q13",
            },
        },
        "y45_pulse_q13": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "y45_I_wf_q13",
                "Q": "y45_Q_wf_q13",
            },
        },
        "-y45_pulse_q13": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "minus_y45_I_wf_q13",
                "Q": "minus_y45_Q_wf_q13",
            },
        },
        "readout_pulse_q13": {
            "operation": "measurement",
            "length": readout_len,
            "waveforms": {
                "I": "readout_wf_q13",
                "Q": "zero_wf",
            },
            "integration_weights": {
                "cos": "cosine_weights",
                "sin": "sine_weights",
                "minus_sin": "minus_sine_weights",
                "rotated_cos": "rotated_cosine_weights_q13",
                "rotated_sin": "rotated_sine_weights_q13",
                "rotated_minus_sin": "rotated_minus_sine_weights_q13",
                "opt_cos": "opt_cosine_weights_q13",
                "opt_sin": "opt_sine_weights_q13",
                "opt_minus_sin": "opt_minus_sine_weights_q13",
            },
            "digital_marker": "ON",
        },

        "x90_pulse_q14": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "x90_I_wf_q14",
                "Q": "x90_Q_wf_q14",
            },
        },
        "x180_pulse_q14": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "x180_I_wf_q14",
                "Q": "x180_Q_wf_q14",
            },
        },
        "-x90_pulse_q14": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "minus_x90_I_wf_q14",
                "Q": "minus_x90_Q_wf_q14",
            },
        },
        "y90_pulse_q14": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "y90_I_wf_q14",
                "Q": "y90_Q_wf_q14",
            },
        },
        "y180_pulse_q14": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "y180_I_wf_q14",
                "Q": "y180_Q_wf_q14",
            },
        },
        "-y90_pulse_q14": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "minus_y90_I_wf_q14",
                "Q": "minus_y90_Q_wf_q14",
            },
        },
        "y45_pulse_q14": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "y45_I_wf_q14",
                "Q": "y45_Q_wf_q14",
            },
        },
        "-y45_pulse_q14": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "minus_y45_I_wf_q14",
                "Q": "minus_y45_Q_wf_q14",
            },
        },
        "readout_pulse_q14": {
            "operation": "measurement",
            "length": readout_len,
            "waveforms": {
                "I": "readout_wf_q14",
                "Q": "zero_wf",
            },
            "integration_weights": {
                "cos": "cosine_weights",
                "sin": "sine_weights",
                "minus_sin": "minus_sine_weights",
                "rotated_cos": "rotated_cosine_weights_q14",
                "rotated_sin": "rotated_sine_weights_q14",
                "rotated_minus_sin": "rotated_minus_sine_weights_q14",
                "opt_cos": "opt_cosine_weights_q14",
                "opt_sin": "opt_sine_weights_q14",
                "opt_minus_sin": "opt_minus_sine_weights_q14",
            },
            "digital_marker": "ON",
        },

        "x90_pulse_q15": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "x90_I_wf_q15",
                "Q": "x90_Q_wf_q15",
            },
        },
        "x180_pulse_q15": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "x180_I_wf_q15",
                "Q": "x180_Q_wf_q15",
            },
        },
        "-x90_pulse_q15": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "minus_x90_I_wf_q15",
                "Q": "minus_x90_Q_wf_q15",
            },
        },
        "y90_pulse_q15": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "y90_I_wf_q15",
                "Q": "y90_Q_wf_q15",
            },
        },
        "y180_pulse_q15": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "y180_I_wf_q15",
                "Q": "y180_Q_wf_q15",
            },
        },
        "-y90_pulse_q15": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "minus_y90_I_wf_q15",
                "Q": "minus_y90_Q_wf_q15",
            },
        },
        "y45_pulse_q15": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "y45_I_wf_q15",
                "Q": "y45_Q_wf_q15",
            },
        },
        "-y45_pulse_q15": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "minus_y45_I_wf_q15",
                "Q": "minus_y45_Q_wf_q15",
            },
        },
        "readout_pulse_q15": {
            "operation": "measurement",
            "length": readout_len,
            "waveforms": {
                "I": "readout_wf_q15",
                "Q": "zero_wf",
            },
            "integration_weights": {
                "cos": "cosine_weights",
                "sin": "sine_weights",
                "minus_sin": "minus_sine_weights",
                "rotated_cos": "rotated_cosine_weights_q15",
                "rotated_sin": "rotated_sine_weights_q15",
                "rotated_minus_sin": "rotated_minus_sine_weights_q15",
                "opt_cos": "opt_cosine_weights_q15",
                "opt_sin": "opt_sine_weights_q15",
                "opt_minus_sin": "opt_minus_sine_weights_q15",
            },
            "digital_marker": "ON",
        },

        "x90_pulse_q16": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "x90_I_wf_q16",
                "Q": "x90_Q_wf_q16",
            },
        },
        "x180_pulse_q16": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "x180_I_wf_q16",
                "Q": "x180_Q_wf_q16",
            },
        },
        "-x90_pulse_q16": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "minus_x90_I_wf_q16",
                "Q": "minus_x90_Q_wf_q16",
            },
        },
        "y90_pulse_q16": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "y90_I_wf_q16",
                "Q": "y90_Q_wf_q16",
            },
        },
        "y180_pulse_q16": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "y180_I_wf_q16",
                "Q": "y180_Q_wf_q16",
            },
        },
        "-y90_pulse_q16": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "minus_y90_I_wf_q16",
                "Q": "minus_y90_Q_wf_q16",
            },
        },
        "y45_pulse_q16": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "y45_I_wf_q16",
                "Q": "y45_Q_wf_q16",
            },
        },
        "-y45_pulse_q16": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "minus_y45_I_wf_q16",
                "Q": "minus_y45_Q_wf_q16",
            },
        },
        "readout_pulse_q16": {
            "operation": "measurement",
            "length": readout_len,
            "waveforms": {
                "I": "readout_wf_q16",
                "Q": "zero_wf",
            },
            "integration_weights": {
                "cos": "cosine_weights",
                "sin": "sine_weights",
                "minus_sin": "minus_sine_weights",
                "rotated_cos": "rotated_cosine_weights_q16",
                "rotated_sin": "rotated_sine_weights_q16",
                "rotated_minus_sin": "rotated_minus_sine_weights_q16",
                "opt_cos": "opt_cosine_weights_q16",
                "opt_sin": "opt_sine_weights_q16",
                "opt_minus_sin": "opt_minus_sine_weights_q16",
            },
            "digital_marker": "ON",
        },
                "x90_pulse_q17": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "x90_I_wf_q17",
                "Q": "x90_Q_wf_q17",
            },
        },
        "x180_pulse_q17": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "x180_I_wf_q17",
                "Q": "x180_Q_wf_q17",
            },
        },
        "-x90_pulse_q17": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "minus_x90_I_wf_q17",
                "Q": "minus_x90_Q_wf_q17",
            },
        },
        "y90_pulse_q17": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "y90_I_wf_q17",
                "Q": "y90_Q_wf_q17",
            },
        },
        "y180_pulse_q17": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "y180_I_wf_q17",
                "Q": "y180_Q_wf_q17",
            },
        },
        "-y90_pulse_q17": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "minus_y90_I_wf_q17",
                "Q": "minus_y90_Q_wf_q17",
            },
        },
        "y45_pulse_q17": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "y45_I_wf_q17",
                "Q": "y45_Q_wf_q17",
            },
        },
        "-y45_pulse_q17": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "minus_y45_I_wf_q17",
                "Q": "minus_y45_Q_wf_q17",
            },
        },
        "readout_pulse_q17": {
            "operation": "measurement",
            "length": readout_len,
            "waveforms": {
                "I": "readout_wf_q17",
                "Q": "zero_wf",
            },
            "integration_weights": {
                "cos": "cosine_weights",
                "sin": "sine_weights",
                "minus_sin": "minus_sine_weights",
                "rotated_cos": "rotated_cosine_weights_q17",
                "rotated_sin": "rotated_sine_weights_q17",
                "rotated_minus_sin": "rotated_minus_sine_weights_q17",
                "opt_cos": "opt_cosine_weights_q17",
                "opt_sin": "opt_sine_weights_q17",
                "opt_minus_sin": "opt_minus_sine_weights_q17",
            },
            "digital_marker": "ON",
        },

        "x90_pulse_q18": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "x90_I_wf_q18",
                "Q": "x90_Q_wf_q18",
            },
        },
        "x180_pulse_q18": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "x180_I_wf_q18",
                "Q": "x180_Q_wf_q18",
            },
        },
        "-x90_pulse_q18": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "minus_x90_I_wf_q18",
                "Q": "minus_x90_Q_wf_q18",
            },
        },
        "y90_pulse_q18": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "y90_I_wf_q18",
                "Q": "y90_Q_wf_q18",
            },
        },
        "y180_pulse_q18": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "y180_I_wf_q18",
                "Q": "y180_Q_wf_q18",
            },
        },
        "-y90_pulse_q18": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "minus_y90_I_wf_q18",
                "Q": "minus_y90_Q_wf_q18",
            },
        },
        "y45_pulse_q18": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "y45_I_wf_q18",
                "Q": "y45_Q_wf_q18",
            },
        },
        "-y45_pulse_q18": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "minus_y45_I_wf_q18",
                "Q": "minus_y45_Q_wf_q18",
            },
        },
        "readout_pulse_q18": {
            "operation": "measurement",
            "length": readout_len,
            "waveforms": {
                "I": "readout_wf_q18",
                "Q": "zero_wf",
            },
            "integration_weights": {
                "cos": "cosine_weights",
                "sin": "sine_weights",
                "minus_sin": "minus_sine_weights",
                "rotated_cos": "rotated_cosine_weights_q18",
                "rotated_sin": "rotated_sine_weights_q18",
                "rotated_minus_sin": "rotated_minus_sine_weights_q18",
                "opt_cos": "opt_cosine_weights_q18",
                "opt_sin": "opt_sine_weights_q18",
                "opt_minus_sin": "opt_minus_sine_weights_q18",
            },
            "digital_marker": "ON",
        },

                "x90_pulse_q19": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "x90_I_wf_q19",
                "Q": "x90_Q_wf_q19",
            },
        },
        "x180_pulse_q19": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "x180_I_wf_q19",
                "Q": "x180_Q_wf_q19",
            },
        },
        "-x90_pulse_q19": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "minus_x90_I_wf_q19",
                "Q": "minus_x90_Q_wf_q19",
            },
        },
        "y90_pulse_q19": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "y90_I_wf_q19",
                "Q": "y90_Q_wf_q19",
            },
        },
        "y180_pulse_q19": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "y180_I_wf_q19",
                "Q": "y180_Q_wf_q19",
            },
        },
        "-y90_pulse_q19": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "minus_y90_I_wf_q19",
                "Q": "minus_y90_Q_wf_q19",
            },
        },
        "y45_pulse_q19": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "y45_I_wf_q19",
                "Q": "y45_Q_wf_q19",
            },
        },
        "-y45_pulse_q19": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "minus_y45_I_wf_q19",
                "Q": "minus_y45_Q_wf_q19",
            },
        },
        "readout_pulse_q19": {
            "operation": "measurement",
            "length": readout_len,
            "waveforms": {
                "I": "readout_wf_q19",
                "Q": "zero_wf",
            },
            "integration_weights": {
                "cos": "cosine_weights",
                "sin": "sine_weights",
                "minus_sin": "minus_sine_weights",
                "rotated_cos": "rotated_cosine_weights_q19",
                "rotated_sin": "rotated_sine_weights_q19",
                "rotated_minus_sin": "rotated_minus_sine_weights_q19",
                "opt_cos": "opt_cosine_weights_q19",
                "opt_sin": "opt_sine_weights_q19",
                "opt_minus_sin": "opt_minus_sine_weights_q19",
            },
            "digital_marker": "ON",
        },

        "x90_pulse_q20": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "x90_I_wf_q20",
                "Q": "x90_Q_wf_q20",
            },
        },
        "x180_pulse_q20": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "x180_I_wf_q20",
                "Q": "x180_Q_wf_q20",
            },
        },
        "-x90_pulse_q20": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "minus_x90_I_wf_q20",
                "Q": "minus_x90_Q_wf_q20",
            },
        },
        "y90_pulse_q20": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "y90_I_wf_q20",
                "Q": "y90_Q_wf_q20",
            },
        },
        "y180_pulse_q20": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "y180_I_wf_q20",
                "Q": "y180_Q_wf_q20",
            },
        },
        "-y90_pulse_q20": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "minus_y90_I_wf_q20",
                "Q": "minus_y90_Q_wf_q20",
            },
        },
        "y45_pulse_q20": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "y45_I_wf_q20",
                "Q": "y45_Q_wf_q20",
            },
        },
        "-y45_pulse_q20": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "minus_y45_I_wf_q20",
                "Q": "minus_y45_Q_wf_q20",
            },
        },
        "readout_pulse_q20": {
            "operation": "measurement",
            "length": readout_len,
            "waveforms": {
                "I": "readout_wf_q20",
                "Q": "zero_wf",
            },
            "integration_weights": {
                "cos": "cosine_weights",
                "sin": "sine_weights",
                "minus_sin": "minus_sine_weights",
                "rotated_cos": "rotated_cosine_weights_q20",
                "rotated_sin": "rotated_sine_weights_q20",
                "rotated_minus_sin": "rotated_minus_sine_weights_q20",
                "opt_cos": "opt_cosine_weights_q20",
                "opt_sin": "opt_sine_weights_q20",
                "opt_minus_sin": "opt_minus_sine_weights_q20",
            },
            "digital_marker": "ON",
        },

        "x90_pulse_q_C6": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "x90_I_wf_q_C6",
                "Q": "x90_Q_wf_q_C6",
            },
        },
        "x180_pulse_q_C6": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "x180_I_wf_q_C6",
                "Q": "x180_Q_wf_q_C6",
            },
        },
        "-x90_pulse_q_C6": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "minus_x90_I_wf_q_C6",
                "Q": "minus_x90_Q_wf_q_C6",
            },
        },
        "y90_pulse_q_C6": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "y90_I_wf_q_C6",
                "Q": "y90_Q_wf_q_C6",
            },
        },
        "y180_pulse_q_C6": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "y180_I_wf_q_C6",
                "Q": "y180_Q_wf_q_C6",
            },
        },
        "-y90_pulse_q_C6": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "minus_y90_I_wf_q_C6",
                "Q": "minus_y90_Q_wf_q_C6",
            },
        },
        "y45_pulse_q_C6": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "y45_I_wf_q_C6",
                "Q": "y45_Q_wf_q_C6",
            },
        },
        "-y45_pulse_q_C6": {
            "operation": "control",
            "length": pi_len,
            "waveforms": {
                "I": "minus_y45_I_wf_q_C6",
                "Q": "minus_y45_Q_wf_q_C6",
            },
        },
        "readout_pulse_q_C6": {
            "operation": "measurement",
            "length": readout_len,
            "waveforms": {
                "I": "readout_wf_q_C6",
                "Q": "zero_wf",
            },
            "integration_weights": {
                "cos": "cosine_weights",
                "sin": "sine_weights",
                "minus_sin": "minus_sine_weights",
                "rotated_cos": "rotated_cosine_weights_q_C6",
                "rotated_sin": "rotated_sine_weights_q_C6",
                "rotated_minus_sin": "rotated_minus_sine_weights_q_C6",
                "opt_cos": "opt_cosine_weights_q_C6",
                "opt_sin": "opt_sine_weights_q_C6",
                "opt_minus_sin": "opt_minus_sine_weights_q_C6",
            },
            "digital_marker": "ON",
        },



        # "x90_pulse_q3": {
        #     "operation": "control",
        #     "length": pi_len,
        #     "waveforms": {
        #         "I": "x90_I_wf_q3",
        #         "Q": "x90_Q_wf_q3",
        #     },
        # },
        # "x180_pulse_q3": {
        #     "operation": "control",
        #     "length": pi_len,
        #     "waveforms": {
        #         "I": "x180_I_wf_q3",
        #         "Q": "x180_Q_wf_q3",
        #     },
        # },
        # "-x90_pulse_q3": {
        #     "operation": "control",
        #     "length": pi_len,
        #     "waveforms": {
        #         "I": "minus_x90_I_wf_q3",
        #         "Q": "minus_x90_Q_wf_q3",
        #     },
        # },
        # "y90_pulse_q3": {
        #     "operation": "control",
        #     "length": pi_len,
        #     "waveforms": {
        #         "I": "y90_I_wf_q3",
        #         "Q": "y90_Q_wf_q3",
        #     },
        # },
        # "y180_pulse_q3": {
        #     "operation": "control",
        #     "length": pi_len,
        #     "waveforms": {
        #         "I": "y180_I_wf_q3",
        #         "Q": "y180_Q_wf_q3",
        #     },
        # },
        # "-y90_pulse_q3": {
        #     "operation": "control",
        #     "length": pi_len,
        #     "waveforms": {
        #         "I": "minus_y90_I_wf_q3",
        #         "Q": "minus_y90_Q_wf_q3",
        #     },
        # },
        # "readout_pulse_q3": {
        #     "operation": "measurement",
        #     "length": readout_len,
        #     "waveforms": {
        #         "I": "readout_wf_q3",
        #         "Q": "zero_wf",
        #     },
        #     "integration_weights": {
        #         "cos": "cosine_weights",
        #         "sin": "sine_weights",
        #         "minus_sin": "minus_sine_weights",
        #         "rotated_cos": "rotated_cosine_weights_q3",
        #         "rotated_sin": "rotated_sine_weights_q3",
        #         "rotated_minus_sin": "rotated_minus_sine_weights_q3",
        #         "opt_cos": "opt_cosine_weights_q3",
        #         "opt_sin": "opt_sine_weights_q3",
        #         "opt_minus_sin": "opt_minus_sine_weights_q3",
        #     },
        #     "digital_marker": "ON",
        # },
        # "x90_pulse_q4": {
        #     "operation": "control",
        #     "length": pi_len,
        #     "waveforms": {
        #         "I": "x90_I_wf_q4",
        #         "Q": "x90_Q_wf_q4",
        #     },
        # },
        # "x180_pulse_q4": {
        #     "operation": "control",
        #     "length": pi_len,
        #     "waveforms": {
        #         "I": "x180_I_wf_q4",
        #         "Q": "x180_Q_wf_q4",
        #     },
        # },
        # "-x90_pulse_q4": {
        #     "operation": "control",
        #     "length": pi_len,
        #     "waveforms": {
        #         "I": "minus_x90_I_wf_q4",
        #         "Q": "minus_x90_Q_wf_q4",
        #     },
        # },
        # "y90_pulse_q4": {
        #     "operation": "control",
        #     "length": pi_len,
        #     "waveforms": {
        #         "I": "y90_I_wf_q4",
        #         "Q": "y90_Q_wf_q4",
        #     },
        # },
        # "y180_pulse_q4": {
        #     "operation": "control",
        #     "length": pi_len,
        #     "waveforms": {
        #         "I": "y180_I_wf_q4",
        #         "Q": "y180_Q_wf_q4",
        #     },
        # },
        # "-y90_pulse_q4": {
        #     "operation": "control",
        #     "length": pi_len,
        #     "waveforms": {
        #         "I": "minus_y90_I_wf_q4",
        #         "Q": "minus_y90_Q_wf_q4",
        #     },
        # },
        # "readout_pulse_q4": {
        #     "operation": "measurement",
        #     "length": readout_len,
        #     "waveforms": {
        #         "I": "readout_wf_q4",
        #         "Q": "zero_wf",
        #     },
        #     "integration_weights": {
        #         "cos": "cosine_weights",
        #         "sin": "sine_weights",
        #         "minus_sin": "minus_sine_weights",
        #         "rotated_cos": "rotated_cosine_weights_q4",
        #         "rotated_sin": "rotated_sine_weights_q4",
        #         "rotated_minus_sin": "rotated_minus_sine_weights_q4",
        #         "opt_cos": "opt_cosine_weights_q4",
        #         "opt_sin": "opt_sine_weights_q4",
        #         "opt_minus_sin": "opt_minus_sine_weights_q4",
        #     },
        #     "digital_marker": "ON",
        # },
        # "readout_pulse_q5": {
        #     "operation": "measurement",
        #     "length": readout_len,
        #     "waveforms": {
        #         "I": "readout_wf_q5",
        #         "Q": "zero_wf",
        #     },
        #     "integration_weights": {
        #         "cos": "cosine_weights",
        #         "sin": "sine_weights",
        #         "minus_sin": "minus_sine_weights",
        #         "rotated_cos": "rotated_cosine_weights_q5",
        #         "rotated_sin": "rotated_sine_weights_q5",
        #         "rotated_minus_sin": "rotated_minus_sine_weights_q5",
        #         "opt_cos": "opt_cosine_weights_q5",
        #         "opt_sin": "opt_sine_weights_q5",
        #         "opt_minus_sin": "opt_minus_sine_weights_q5",
        #     },
        #     "digital_marker": "ON",
        # },
        # "readout_pulse_q9": {
        #     "operation": "measurement",
        #     "length": readout_len,
        #     "waveforms": {
        #         "I": "readout_wf_q9",
        #         "Q": "zero_wf",
        #     },
        #     "integration_weights": {
        #         "cos": "cosine_weights",
        #         "sin": "sine_weights",
        #         "minus_sin": "minus_sine_weights",
        #         "rotated_cos": "rotated_cosine_weights_q9",
        #         "rotated_sin": "rotated_sine_weights_q9",
        #         "rotated_minus_sin": "rotated_minus_sine_weights_q9",
        #         "opt_cos": "opt_cosine_weights_q9",
        #         "opt_sin": "opt_sine_weights_q9",
        #         "opt_minus_sin": "opt_minus_sine_weights_q9",
        #     },
        #     "digital_marker": "ON",
        # },
        #  "readout_pulse_q13": {
        #     "operation": "measurement",
        #     "length": readout_len,
        #     "waveforms": {
        #         "I": "readout_wf_q13",
        #         "Q": "zero_wf",
        #     },
        #     "integration_weights": {
        #         "cos": "cosine_weights",
        #         "sin": "sine_weights",
        #         "minus_sin": "minus_sine_weights",
        #         "rotated_cos": "rotated_cosine_weights_q13",
        #         "rotated_sin": "rotated_sine_weights_q13",
        #         "rotated_minus_sin": "rotated_minus_sine_weights_q13",
        #         "opt_cos": "opt_cosine_weights_q13",
        #         "opt_sin": "opt_sine_weights_q13",
        #         "opt_minus_sin": "opt_minus_sine_weights_q13",
        #     },
        #     "digital_marker": "ON",
        # },
        
    },
    "waveforms": {
        "const_wf": {"type": "constant", "sample": const_amp_dc},
        "saturation_wf": {"type": "constant", "sample": saturation_amp},
        # "const_flux_wf": {"type": "constant", "sample": const_flux_amp},
        "const_flux_wf_C12_1001": {"type": "constant", "sample": const_flux_amp_C12_1001},
        "const_flux_wf_C12_1120": {"type": "constant", "sample": const_flux_amp_C12_1120},
        "const_flux_wf_C12_1102": {"type": "constant", "sample": const_flux_amp_C12_1102},

        #C1
        "parametric_const_wf_C1_Q12_1001": {"type": "constant", "sample": parametric_const_amp_C1_Q12_1001},
        "parametric_const_wf_C1_Q12_1102": {"type": "constant", "sample": parametric_const_amp_C1_Q12_1102},
        "parametric_const_wf_C1_Q12_1120": {"type": "constant", "sample": parametric_const_amp_C1_Q12_1120},

        "parametric_const_wf_C1_Q15_1001": {"type": "constant", "sample": parametric_const_amp_C1_Q15_1001},
        "parametric_const_wf_C1_Q15_1102": {"type": "constant", "sample": parametric_const_amp_C1_Q15_1102},
        "parametric_const_wf_C1_Q15_1120": {"type": "constant", "sample": parametric_const_amp_C1_Q15_1120},

        "parametric_const_wf_C1_Q16_1001": {"type": "constant", "sample": parametric_const_amp_C1_Q16_1001},
        "parametric_const_wf_C1_Q16_1102": {"type": "constant", "sample": parametric_const_amp_C1_Q16_1102},
        "parametric_const_wf_C1_Q16_1120": {"type": "constant", "sample": parametric_const_amp_C1_Q16_1120},

        "parametric_const_wf_C1_Q25_1001": {"type": "constant", "sample": parametric_const_amp_C1_Q25_1001},
        "parametric_const_wf_C1_Q25_1102": {"type": "constant", "sample": parametric_const_amp_C1_Q25_1102},
        "parametric_const_wf_C1_Q25_1120": {"type": "constant", "sample": parametric_const_amp_C1_Q25_1120},

        "parametric_const_wf_C1_Q26_1001": {"type": "constant", "sample": parametric_const_amp_C1_Q26_1001},
        "parametric_const_wf_C1_Q26_1102": {"type": "constant", "sample": parametric_const_amp_C1_Q26_1102},
        "parametric_const_wf_C1_Q26_1120": {"type": "constant", "sample": parametric_const_amp_C1_Q26_1120},

        "parametric_const_wf_C1_Q56_1001": {"type": "constant", "sample": parametric_const_amp_C1_Q56_1001},
        "parametric_const_wf_C1_Q56_1102": {"type": "constant", "sample": parametric_const_amp_C1_Q56_1102},
        "parametric_const_wf_C1_Q56_1120": {"type": "constant", "sample": parametric_const_amp_C1_Q56_1120},


        #C4
        "parametric_const_wf_C4_Q56_1001": {"type": "constant", "sample": parametric_const_amp_C4_Q56_1001},
        "parametric_const_wf_C4_Q56_1102": {"type": "constant", "sample": parametric_const_amp_C4_Q56_1102},
        "parametric_const_wf_C4_Q56_1120": {"type": "constant", "sample": parametric_const_amp_C4_Q56_1120},

        "parametric_const_wf_C4_Q59_1001": {"type": "constant", "sample": parametric_const_amp_C4_Q59_1001},
        "parametric_const_wf_C4_Q59_1102": {"type": "constant", "sample": parametric_const_amp_C4_Q59_1102},
        "parametric_const_wf_C4_Q59_1120": {"type": "constant", "sample": parametric_const_amp_C4_Q59_1120},

        "parametric_const_wf_C4_Q510_1001": {"type": "constant", "sample": parametric_const_amp_C4_Q510_1001},
        "parametric_const_wf_C4_Q510_1102": {"type": "constant", "sample": parametric_const_amp_C4_Q510_1102},
        "parametric_const_wf_C4_Q510_1120": {"type": "constant", "sample": parametric_const_amp_C4_Q510_1120},

        "parametric_const_wf_C4_Q69_1001": {"type": "constant", "sample": parametric_const_amp_C4_Q69_1001},
        "parametric_const_wf_C4_Q69_1102": {"type": "constant", "sample": parametric_const_amp_C4_Q69_1102},
        "parametric_const_wf_C4_Q69_1120": {"type": "constant", "sample": parametric_const_amp_C4_Q69_1120},

        "parametric_const_wf_C4_Q610_1001": {"type": "constant", "sample": parametric_const_amp_C4_Q610_1001},
        "parametric_const_wf_C4_Q610_1102": {"type": "constant", "sample": parametric_const_amp_C4_Q610_1102},
        "parametric_const_wf_C4_Q610_1120": {"type": "constant", "sample": parametric_const_amp_C4_Q610_1120},

        "parametric_const_wf_C4_Q910_1001": {"type": "constant", "sample": parametric_const_amp_C4_Q910_1001},
        "parametric_const_wf_C4_Q910_1102": {"type": "constant", "sample": parametric_const_amp_C4_Q910_1102},
        "parametric_const_wf_C4_Q910_1120": {"type": "constant", "sample": parametric_const_amp_C4_Q910_1120},


        #C6
        "parametric_const_wf_C6_Q910_1001": {"type": "constant", "sample": parametric_const_amp_C6_Q910_1001},
        "parametric_const_wf_C6_Q910_1102": {"type": "constant", "sample": parametric_const_amp_C6_Q910_1102},
        "parametric_const_wf_C6_Q910_1120": {"type": "constant", "sample": parametric_const_amp_C6_Q910_1120},

        "parametric_const_wf_C6_Q913_1001": {"type": "constant", "sample": parametric_const_amp_C6_Q913_1001},
        "parametric_const_wf_C6_Q913_1102": {"type": "constant", "sample": parametric_const_amp_C6_Q913_1102},
        "parametric_const_wf_C6_Q913_1120": {"type": "constant", "sample": parametric_const_amp_C6_Q913_1120},

        "parametric_const_wf_C6_Q914_1001": {"type": "constant", "sample": parametric_const_amp_C6_Q914_1001},
        "parametric_const_wf_C6_Q914_1102": {"type": "constant", "sample": parametric_const_amp_C6_Q914_1102},
        "parametric_const_wf_C6_Q914_1120": {"type": "constant", "sample": parametric_const_amp_C6_Q914_1120},

        "parametric_const_wf_C6_Q1013_1001": {"type": "constant", "sample": parametric_const_amp_C6_Q1013_1001},
        "parametric_const_wf_C6_Q1013_1102": {"type": "constant", "sample": parametric_const_amp_C6_Q1013_1102},
        "parametric_const_wf_C6_Q1013_1120": {"type": "constant", "sample": parametric_const_amp_C6_Q1013_1120},

        "parametric_const_wf_C6_Q1014_1001": {"type": "constant", "sample": parametric_const_amp_C6_Q1014_1001},
        "parametric_const_wf_C6_Q1014_1102": {"type": "constant", "sample": parametric_const_amp_C6_Q1014_1102},
        "parametric_const_wf_C6_Q1014_1120": {"type": "constant", "sample": parametric_const_amp_C6_Q1014_1120},

        "parametric_const_wf_C6_Q1314_1001": {"type": "constant", "sample": parametric_const_amp_C6_Q1314_1001},
        "parametric_const_wf_C6_Q1314_1102": {"type": "constant", "sample": parametric_const_amp_C6_Q1314_1102},
        "parametric_const_wf_C6_Q1314_1120": {"type": "constant", "sample": parametric_const_amp_C6_Q1314_1120},

        
        #C8
        "parametric_const_wf_C8_Q1317_1001": {"type": "constant", "sample": parametric_const_amp_C8_Q1317_1001},
        "parametric_const_wf_C8_Q1317_1102": {"type": "constant", "sample": parametric_const_amp_C8_Q1317_1102},
        "parametric_const_wf_C8_Q1317_1120": {"type": "constant", "sample": parametric_const_amp_C8_Q1317_1120},

        "parametric_const_wf_C8_Q1314_1001": {"type": "constant", "sample": parametric_const_amp_C8_Q1314_1001},
        "parametric_const_wf_C8_Q1314_1102": {"type": "constant", "sample": parametric_const_amp_C8_Q1314_1102},
        "parametric_const_wf_C8_Q1314_1120": {"type": "constant", "sample": parametric_const_amp_C8_Q1314_1120},

        "parametric_const_wf_C8_Q1318_1001": {"type": "constant", "sample": parametric_const_amp_C8_Q1318_1001},
        "parametric_const_wf_C8_Q1318_1102": {"type": "constant", "sample": parametric_const_amp_C8_Q1318_1102},
        "parametric_const_wf_C8_Q1318_1120": {"type": "constant", "sample": parametric_const_amp_C8_Q1318_1120},

        "parametric_const_wf_C8_Q1417_1001": {"type": "constant", "sample": parametric_const_amp_C8_Q1417_1001},
        "parametric_const_wf_C8_Q1417_1102": {"type": "constant", "sample": parametric_const_amp_C8_Q1417_1102},
        "parametric_const_wf_C8_Q1417_1120": {"type": "constant", "sample": parametric_const_amp_C8_Q1417_1120},

        "parametric_const_wf_C8_Q1418_1001": {"type": "constant", "sample": parametric_const_amp_C8_Q1418_1001},
        "parametric_const_wf_C8_Q1418_1102": {"type": "constant", "sample": parametric_const_amp_C8_Q1418_1102},
        "parametric_const_wf_C8_Q1418_1120": {"type": "constant", "sample": parametric_const_amp_C8_Q1418_1120},

        "parametric_const_wf_C8_Q1718_1001": {"type": "constant", "sample": parametric_const_amp_C8_Q1718_1001},
        "parametric_const_wf_C8_Q1718_1102": {"type": "constant", "sample": parametric_const_amp_C8_Q1718_1102},
        "parametric_const_wf_C8_Q1718_1120": {"type": "constant", "sample": parametric_const_amp_C8_Q1718_1120},

        # ---- C3 waveforms ----
        "parametric_const_wf_C3_Q34_1001": {"type": "constant", "sample": parametric_const_amp_C3_Q34_1001},
        "parametric_const_wf_C3_Q34_1102": {"type": "constant", "sample": parametric_const_amp_C3_Q34_1102},
        "parametric_const_wf_C3_Q34_1120": {"type": "constant", "sample": parametric_const_amp_C3_Q34_1120},

        "parametric_const_wf_C3_Q38_1001": {"type": "constant", "sample": parametric_const_amp_C3_Q38_1001},
        "parametric_const_wf_C3_Q38_1102": {"type": "constant", "sample": parametric_const_amp_C3_Q38_1102},
        "parametric_const_wf_C3_Q38_1120": {"type": "constant", "sample": parametric_const_amp_C3_Q38_1120},

        "parametric_const_wf_C3_Q37_1001": {"type": "constant", "sample": parametric_const_amp_C3_Q37_1001},
        "parametric_const_wf_C3_Q37_1102": {"type": "constant", "sample": parametric_const_amp_C3_Q37_1102},
        "parametric_const_wf_C3_Q37_1120": {"type": "constant", "sample": parametric_const_amp_C3_Q37_1120},

        "parametric_const_wf_C3_Q48_1001": {"type": "constant", "sample": parametric_const_amp_C3_Q48_1001},
        "parametric_const_wf_C3_Q48_1102": {"type": "constant", "sample": parametric_const_amp_C3_Q48_1102},
        "parametric_const_wf_C3_Q48_1120": {"type": "constant", "sample": parametric_const_amp_C3_Q48_1120},

        "parametric_const_wf_C3_Q47_1001": {"type": "constant", "sample": parametric_const_amp_C3_Q47_1001},
        "parametric_const_wf_C3_Q47_1102": {"type": "constant", "sample": parametric_const_amp_C3_Q47_1102},
        "parametric_const_wf_C3_Q47_1120": {"type": "constant", "sample": parametric_const_amp_C3_Q47_1120},

        "parametric_const_wf_C3_Q78_1001": {"type": "constant", "sample": parametric_const_amp_C3_Q78_1001},
        "parametric_const_wf_C3_Q78_1102": {"type": "constant", "sample": parametric_const_amp_C3_Q78_1102},
        "parametric_const_wf_C3_Q78_1120": {"type": "constant", "sample": parametric_const_amp_C3_Q78_1120},

        # ---- C5 waveforms ----
        "parametric_const_wf_C5_Q78_1001": {"type": "constant", "sample": parametric_const_amp_C5_Q78_1001},
        "parametric_const_wf_C5_Q78_1102": {"type": "constant", "sample": parametric_const_amp_C5_Q78_1102},
        "parametric_const_wf_C5_Q78_1120": {"type": "constant", "sample": parametric_const_amp_C5_Q78_1120},

        "parametric_const_wf_C5_Q712_1001": {"type": "constant", "sample": parametric_const_amp_C5_Q712_1001},
        "parametric_const_wf_C5_Q712_1102": {"type": "constant", "sample": parametric_const_amp_C5_Q712_1102},
        "parametric_const_wf_C5_Q712_1120": {"type": "constant", "sample": parametric_const_amp_C5_Q712_1120},

        "parametric_const_wf_C5_Q711_1001": {"type": "constant", "sample": parametric_const_amp_C5_Q711_1001},
        "parametric_const_wf_C5_Q711_1102": {"type": "constant", "sample": parametric_const_amp_C5_Q711_1102},
        "parametric_const_wf_C5_Q711_1120": {"type": "constant", "sample": parametric_const_amp_C5_Q711_1120},

        "parametric_const_wf_C5_Q812_1001": {"type": "constant", "sample": parametric_const_amp_C5_Q812_1001},
        "parametric_const_wf_C5_Q812_1102": {"type": "constant", "sample": parametric_const_amp_C5_Q812_1102},
        "parametric_const_wf_C5_Q812_1120": {"type": "constant", "sample": parametric_const_amp_C5_Q812_1120},

        "parametric_const_wf_C5_Q811_1001": {"type": "constant", "sample": parametric_const_amp_C5_Q811_1001},
        "parametric_const_wf_C5_Q811_1102": {"type": "constant", "sample": parametric_const_amp_C5_Q811_1102},
        "parametric_const_wf_C5_Q811_1120": {"type": "constant", "sample": parametric_const_amp_C5_Q811_1120},

        "parametric_const_wf_C5_Q1112_1001": {"type": "constant", "sample": parametric_const_amp_C5_Q1112_1001},
        "parametric_const_wf_C5_Q1112_1102": {"type": "constant", "sample": parametric_const_amp_C5_Q1112_1102},
        "parametric_const_wf_C5_Q1112_1120": {"type": "constant", "sample": parametric_const_amp_C5_Q1112_1120},

        # ---- C7 waveforms ----
        "parametric_const_wf_C7_Q1112_1001": {"type": "constant", "sample": parametric_const_amp_C7_Q1112_1001},
        "parametric_const_wf_C7_Q1112_1102": {"type": "constant", "sample": parametric_const_amp_C7_Q1112_1102},
        "parametric_const_wf_C7_Q1112_1120": {"type": "constant", "sample": parametric_const_amp_C7_Q1112_1120},

        "parametric_const_wf_C7_Q1116_1001": {"type": "constant", "sample": parametric_const_amp_C7_Q1116_1001},
        "parametric_const_wf_C7_Q1116_1102": {"type": "constant", "sample": parametric_const_amp_C7_Q1116_1102},
        "parametric_const_wf_C7_Q1116_1120": {"type": "constant", "sample": parametric_const_amp_C7_Q1116_1120},

        "parametric_const_wf_C7_Q1115_1001": {"type": "constant", "sample": parametric_const_amp_C7_Q1115_1001},
        "parametric_const_wf_C7_Q1115_1102": {"type": "constant", "sample": parametric_const_amp_C7_Q1115_1102},
        "parametric_const_wf_C7_Q1115_1120": {"type": "constant", "sample": parametric_const_amp_C7_Q1115_1120},

        "parametric_const_wf_C7_Q1216_1001": {"type": "constant", "sample": parametric_const_amp_C7_Q1216_1001},
        "parametric_const_wf_C7_Q1216_1102": {"type": "constant", "sample": parametric_const_amp_C7_Q1216_1102},
        "parametric_const_wf_C7_Q1216_1120": {"type": "constant", "sample": parametric_const_amp_C7_Q1216_1120},

        "parametric_const_wf_C7_Q1215_1001": {"type": "constant", "sample": parametric_const_amp_C7_Q1215_1001},
        "parametric_const_wf_C7_Q1215_1102": {"type": "constant", "sample": parametric_const_amp_C7_Q1215_1102},
        "parametric_const_wf_C7_Q1215_1120": {"type": "constant", "sample": parametric_const_amp_C7_Q1215_1120},

        "parametric_const_wf_C7_Q1516_1001": {"type": "constant", "sample": parametric_const_amp_C7_Q1516_1001},
        "parametric_const_wf_C7_Q1516_1102": {"type": "constant", "sample": parametric_const_amp_C7_Q1516_1102},
        "parametric_const_wf_C7_Q1516_1120": {"type": "constant", "sample": parametric_const_amp_C7_Q1516_1120},

        # ---- C10 waveforms ----
        "parametric_const_wf_C10_Q1516_1001": {"type": "constant", "sample": parametric_const_amp_C10_Q1516_1001},
        "parametric_const_wf_C10_Q1516_1102": {"type": "constant", "sample": parametric_const_amp_C10_Q1516_1102},
        "parametric_const_wf_C10_Q1516_1120": {"type": "constant", "sample": parametric_const_amp_C10_Q1516_1120},

        "parametric_const_wf_C10_Q1520_1001": {"type": "constant", "sample": parametric_const_amp_C10_Q1520_1001},
        "parametric_const_wf_C10_Q1520_1102": {"type": "constant", "sample": parametric_const_amp_C10_Q1520_1102},
        "parametric_const_wf_C10_Q1520_1120": {"type": "constant", "sample": parametric_const_amp_C10_Q1520_1120},

        "parametric_const_wf_C10_Q1519_1001": {"type": "constant", "sample": parametric_const_amp_C10_Q1519_1001},
        "parametric_const_wf_C10_Q1519_1102": {"type": "constant", "sample": parametric_const_amp_C10_Q1519_1102},
        "parametric_const_wf_C10_Q1519_1120": {"type": "constant", "sample": parametric_const_amp_C10_Q1519_1120},

        "parametric_const_wf_C10_Q1620_1001": {"type": "constant", "sample": parametric_const_amp_C10_Q1620_1001},
        "parametric_const_wf_C10_Q1620_1102": {"type": "constant", "sample": parametric_const_amp_C10_Q1620_1102},
        "parametric_const_wf_C10_Q1620_1120": {"type": "constant", "sample": parametric_const_amp_C10_Q1620_1120},

        "parametric_const_wf_C10_Q1619_1001": {"type": "constant", "sample": parametric_const_amp_C10_Q1619_1001},
        "parametric_const_wf_C10_Q1619_1102": {"type": "constant", "sample": parametric_const_amp_C10_Q1619_1102},
        "parametric_const_wf_C10_Q1619_1120": {"type": "constant", "sample": parametric_const_amp_C10_Q1619_1120},

        "parametric_const_wf_C10_Q1920_1001": {"type": "constant", "sample": parametric_const_amp_C10_Q1920_1001},
        "parametric_const_wf_C10_Q1920_1102": {"type": "constant", "sample": parametric_const_amp_C10_Q1920_1102},
        "parametric_const_wf_C10_Q1920_1120": {"type": "constant", "sample": parametric_const_amp_C10_Q1920_1120},

        # Waveforms for C2_Q37
        "parametric_const_wf_C2_Q37_1001": {"type": "constant", "sample": parametric_const_amp_C2_Q37_1001},
        "parametric_const_wf_C2_Q37_1102": {"type": "constant", "sample": parametric_const_amp_C2_Q37_1102},
        "parametric_const_wf_C2_Q37_1120": {"type": "constant", "sample": parametric_const_amp_C2_Q37_1120},

        # Waveforms for C2_Q36
        "parametric_const_wf_C2_Q36_1001": {"type": "constant", "sample": parametric_const_amp_C2_Q36_1001},
        "parametric_const_wf_C2_Q36_1102": {"type": "constant", "sample": parametric_const_amp_C2_Q36_1102},
        "parametric_const_wf_C2_Q36_1120": {"type": "constant", "sample": parametric_const_amp_C2_Q36_1120},

        # Waveforms for C2_Q67
        "parametric_const_wf_C2_Q67_1001": {"type": "constant", "sample": parametric_const_amp_C2_Q67_1001},
        "parametric_const_wf_C2_Q67_1102": {"type": "constant", "sample": parametric_const_amp_C2_Q67_1102},
        "parametric_const_wf_C2_Q67_1120": {"type": "constant", "sample": parametric_const_amp_C2_Q67_1120},

        # Waveforms for C9_Q1519
        "parametric_const_wf_C9_Q1519_1001": {"type": "constant", "sample": parametric_const_amp_C9_Q1519_1001},
        "parametric_const_wf_C9_Q1519_1102": {"type": "constant", "sample": parametric_const_amp_C9_Q1519_1102},
        "parametric_const_wf_C9_Q1519_1120": {"type": "constant", "sample": parametric_const_amp_C9_Q1519_1120},

        # Waveforms for C9_Q1415
        "parametric_const_wf_C9_Q1415_1001": {"type": "constant", "sample": parametric_const_amp_C9_Q1415_1001},
        "parametric_const_wf_C9_Q1415_1102": {"type": "constant", "sample": parametric_const_amp_C9_Q1415_1102},
        "parametric_const_wf_C9_Q1415_1120": {"type": "constant", "sample": parametric_const_amp_C9_Q1415_1120},

        # Waveforms for C9_Q1419
        "parametric_const_wf_C9_Q1419_1001": {"type": "constant", "sample": parametric_const_amp_C9_Q1419_1001},
        "parametric_const_wf_C9_Q1419_1102": {"type": "constant", "sample": parametric_const_amp_C9_Q1419_1102},
        "parametric_const_wf_C9_Q1419_1120": {"type": "constant", "sample": parametric_const_amp_C9_Q1419_1120},


        
        # "parametric_const_wf_C8_Q1718_1001": {"type": "constant", "sample": parametric_const_amp_C8_Q1718_1001},

        "riseup_wf_C12_1102": { "type": "arbitrary","samples": rise_up_flux_samples.tolist()},
        
        "ringup_wf_C8_Q1317_1102": { "type": "arbitrary","samples": ringup_wf_C8_Q1317_1102.tolist()},
        
        "gauss_flux_wf": {"type": "arbitrary", "samples": gauss_flux_amp*gaussian(gauss_flux_len, std=gauss_flux_len/5)},
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
        "y45_I_wf_q2": {"type": "arbitrary", "samples": y45_I_wf_q2.tolist()},
        "y45_Q_wf_q2": {"type": "arbitrary", "samples": y45_Q_wf_q2.tolist()},
        "minus_y45_I_wf_q2": {"type": "arbitrary", "samples": minus_y45_I_wf_q2.tolist()},
        "minus_y45_Q_wf_q2": {"type": "arbitrary", "samples": minus_y45_Q_wf_q2.tolist()},
        "readout_wf_q2": {"type": "constant", "sample": readout_amp_q2},
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


        "x90_I_wf_q8": {"type": "arbitrary", "samples": x90_I_wf_q8.tolist()},
        "x90_Q_wf_q8": {"type": "arbitrary", "samples": x90_Q_wf_q8.tolist()},
        "x180_I_wf_q8": {"type": "arbitrary", "samples": x180_I_wf_q8.tolist()},
        "x180_Q_wf_q8": {"type": "arbitrary", "samples": x180_Q_wf_q8.tolist()},
        "minus_x90_I_wf_q8": {"type": "arbitrary", "samples": minus_x90_I_wf_q8.tolist()},
        "minus_x90_Q_wf_q8": {"type": "arbitrary", "samples": minus_x90_Q_wf_q8.tolist()},
        "y90_I_wf_q8": {"type": "arbitrary", "samples": y90_I_wf_q8.tolist()},
        "y90_Q_wf_q8": {"type": "arbitrary", "samples": y90_Q_wf_q8.tolist()},
        "y180_I_wf_q8": {"type": "arbitrary", "samples": y180_I_wf_q8.tolist()},
        "y180_Q_wf_q8": {"type": "arbitrary", "samples": y180_Q_wf_q8.tolist()},
        "minus_y90_I_wf_q8": {"type": "arbitrary", "samples": minus_y90_I_wf_q8.tolist()},
        "minus_y90_Q_wf_q8": {"type": "arbitrary", "samples": minus_y90_Q_wf_q8.tolist()},
        "readout_wf_q8": {"type": "constant", "sample": readout_amp_q8},


        "x90_I_wf_q9": {"type": "arbitrary", "samples": x90_I_wf_q9.tolist()},
        "x90_Q_wf_q9": {"type": "arbitrary", "samples": x90_Q_wf_q9.tolist()},
        "x180_I_wf_q9": {"type": "arbitrary", "samples": x180_I_wf_q9.tolist()},
        "x180_Q_wf_q9": {"type": "arbitrary", "samples": x180_Q_wf_q9.tolist()},
        "minus_x90_I_wf_q9": {"type": "arbitrary", "samples": minus_x90_I_wf_q9.tolist()},
        "minus_x90_Q_wf_q9": {"type": "arbitrary", "samples": minus_x90_Q_wf_q9.tolist()},
        "y90_I_wf_q9": {"type": "arbitrary", "samples": y90_I_wf_q9.tolist()},
        "y90_Q_wf_q9": {"type": "arbitrary", "samples": y90_Q_wf_q9.tolist()},
        "y180_I_wf_q9": {"type": "arbitrary", "samples": y180_I_wf_q9.tolist()},
        "y180_Q_wf_q9": {"type": "arbitrary", "samples": y180_Q_wf_q9.tolist()},
        "minus_y90_I_wf_q9": {"type": "arbitrary", "samples": minus_y90_I_wf_q9.tolist()},
        "minus_y90_Q_wf_q9": {"type": "arbitrary", "samples": minus_y90_Q_wf_q9.tolist()},
        "readout_wf_q9": {"type": "constant", "sample": readout_amp_q9},


        "x90_I_wf_q10": {"type": "arbitrary", "samples": x90_I_wf_q10.tolist()},
        "x90_Q_wf_q10": {"type": "arbitrary", "samples": x90_Q_wf_q10.tolist()},
        "x180_I_wf_q10": {"type": "arbitrary", "samples": x180_I_wf_q10.tolist()},
        "x180_Q_wf_q10": {"type": "arbitrary", "samples": x180_Q_wf_q10.tolist()},
        "minus_x90_I_wf_q10": {"type": "arbitrary", "samples": minus_x90_I_wf_q10.tolist()},
        "minus_x90_Q_wf_q10": {"type": "arbitrary", "samples": minus_x90_Q_wf_q10.tolist()},
        "y90_I_wf_q10": {"type": "arbitrary", "samples": y90_I_wf_q10.tolist()},
        "y90_Q_wf_q10": {"type": "arbitrary", "samples": y90_Q_wf_q10.tolist()},
        "y180_I_wf_q10": {"type": "arbitrary", "samples": y180_I_wf_q10.tolist()},
        "y180_Q_wf_q10": {"type": "arbitrary", "samples": y180_Q_wf_q10.tolist()},
        "minus_y90_I_wf_q10": {"type": "arbitrary", "samples": minus_y90_I_wf_q10.tolist()},
        "minus_y90_Q_wf_q10": {"type": "arbitrary", "samples": minus_y90_Q_wf_q10.tolist()},
        "readout_wf_q10": {"type": "constant", "sample": readout_amp_q10},


        "x90_I_wf_q11": {"type": "arbitrary", "samples": x90_I_wf_q11.tolist()},
        "x90_Q_wf_q11": {"type": "arbitrary", "samples": x90_Q_wf_q11.tolist()},
        "x180_I_wf_q11": {"type": "arbitrary", "samples": x180_I_wf_q11.tolist()},
        "x180_Q_wf_q11": {"type": "arbitrary", "samples": x180_Q_wf_q11.tolist()},
        "minus_x90_I_wf_q11": {"type": "arbitrary", "samples": minus_x90_I_wf_q11.tolist()},
        "minus_x90_Q_wf_q11": {"type": "arbitrary", "samples": minus_x90_Q_wf_q11.tolist()},
        "y90_I_wf_q11": {"type": "arbitrary", "samples": y90_I_wf_q11.tolist()},
        "y90_Q_wf_q11": {"type": "arbitrary", "samples": y90_Q_wf_q11.tolist()},
        "y180_I_wf_q11": {"type": "arbitrary", "samples": y180_I_wf_q11.tolist()},
        "y180_Q_wf_q11": {"type": "arbitrary", "samples": y180_Q_wf_q11.tolist()},
        "minus_y90_I_wf_q11": {"type": "arbitrary", "samples": minus_y90_I_wf_q11.tolist()},
        "minus_y90_Q_wf_q11": {"type": "arbitrary", "samples": minus_y90_Q_wf_q11.tolist()},
        "readout_wf_q11": {"type": "constant", "sample": readout_amp_q11},


        "x90_I_wf_q12": {"type": "arbitrary", "samples": x90_I_wf_q12.tolist()},
        "x90_Q_wf_q12": {"type": "arbitrary", "samples": x90_Q_wf_q12.tolist()},
        "x180_I_wf_q12": {"type": "arbitrary", "samples": x180_I_wf_q12.tolist()},
        "x180_Q_wf_q12": {"type": "arbitrary", "samples": x180_Q_wf_q12.tolist()},
        "minus_x90_I_wf_q12": {"type": "arbitrary", "samples": minus_x90_I_wf_q12.tolist()},
        "minus_x90_Q_wf_q12": {"type": "arbitrary", "samples": minus_x90_Q_wf_q12.tolist()},
        "y90_I_wf_q12": {"type": "arbitrary", "samples": y90_I_wf_q12.tolist()},
        "y90_Q_wf_q12": {"type": "arbitrary", "samples": y90_Q_wf_q12.tolist()},
        "y180_I_wf_q12": {"type": "arbitrary", "samples": y180_I_wf_q12.tolist()},
        "y180_Q_wf_q12": {"type": "arbitrary", "samples": y180_Q_wf_q12.tolist()},
        "minus_y90_I_wf_q12": {"type": "arbitrary", "samples": minus_y90_I_wf_q12.tolist()},
        "minus_y90_Q_wf_q12": {"type": "arbitrary", "samples": minus_y90_Q_wf_q12.tolist()},
        "readout_wf_q12": {"type": "constant", "sample": readout_amp_q12},


        "x90_I_wf_q13": {"type": "arbitrary", "samples": x90_I_wf_q13.tolist()},
        "x90_Q_wf_q13": {"type": "arbitrary", "samples": x90_Q_wf_q13.tolist()},
        "x180_I_wf_q13": {"type": "arbitrary", "samples": x180_I_wf_q13.tolist()},
        "x180_Q_wf_q13": {"type": "arbitrary", "samples": x180_Q_wf_q13.tolist()},
        "minus_x90_I_wf_q13": {"type": "arbitrary", "samples": minus_x90_I_wf_q13.tolist()},
        "minus_x90_Q_wf_q13": {"type": "arbitrary", "samples": minus_x90_Q_wf_q13.tolist()},
        "y90_I_wf_q13": {"type": "arbitrary", "samples": y90_I_wf_q13.tolist()},
        "y90_Q_wf_q13": {"type": "arbitrary", "samples": y90_Q_wf_q13.tolist()},
        "y180_I_wf_q13": {"type": "arbitrary", "samples": y180_I_wf_q13.tolist()},
        "y180_Q_wf_q13": {"type": "arbitrary", "samples": y180_Q_wf_q13.tolist()},
        "minus_y90_I_wf_q13": {"type": "arbitrary", "samples": minus_y90_I_wf_q13.tolist()},
        "minus_y90_Q_wf_q13": {"type": "arbitrary", "samples": minus_y90_Q_wf_q13.tolist()},
        "readout_wf_q13": {"type": "constant", "sample": readout_amp_q13},


        "x90_I_wf_q14": {"type": "arbitrary", "samples": x90_I_wf_q14.tolist()},
        "x90_Q_wf_q14": {"type": "arbitrary", "samples": x90_Q_wf_q14.tolist()},
        "x180_I_wf_q14": {"type": "arbitrary", "samples": x180_I_wf_q14.tolist()},
        "x180_Q_wf_q14": {"type": "arbitrary", "samples": x180_Q_wf_q14.tolist()},
        "minus_x90_I_wf_q14": {"type": "arbitrary", "samples": minus_x90_I_wf_q14.tolist()},
        "minus_x90_Q_wf_q14": {"type": "arbitrary", "samples": minus_x90_Q_wf_q14.tolist()},
        "y90_I_wf_q14": {"type": "arbitrary", "samples": y90_I_wf_q14.tolist()},
        "y90_Q_wf_q14": {"type": "arbitrary", "samples": y90_Q_wf_q14.tolist()},
        "y180_I_wf_q14": {"type": "arbitrary", "samples": y180_I_wf_q14.tolist()},
        "y180_Q_wf_q14": {"type": "arbitrary", "samples": y180_Q_wf_q14.tolist()},
        "minus_y90_I_wf_q14": {"type": "arbitrary", "samples": minus_y90_I_wf_q14.tolist()},
        "minus_y90_Q_wf_q14": {"type": "arbitrary", "samples": minus_y90_Q_wf_q14.tolist()},
        "readout_wf_q14": {"type": "constant", "sample": readout_amp_q14},


        "x90_I_wf_q15": {"type": "arbitrary", "samples": x90_I_wf_q15.tolist()},
        "x90_Q_wf_q15": {"type": "arbitrary", "samples": x90_Q_wf_q15.tolist()},
        "x180_I_wf_q15": {"type": "arbitrary", "samples": x180_I_wf_q15.tolist()},
        "x180_Q_wf_q15": {"type": "arbitrary", "samples": x180_Q_wf_q15.tolist()},
        "minus_x90_I_wf_q15": {"type": "arbitrary", "samples": minus_x90_I_wf_q15.tolist()},
        "minus_x90_Q_wf_q15": {"type": "arbitrary", "samples": minus_x90_Q_wf_q15.tolist()},
        "y90_I_wf_q15": {"type": "arbitrary", "samples": y90_I_wf_q15.tolist()},
        "y90_Q_wf_q15": {"type": "arbitrary", "samples": y90_Q_wf_q15.tolist()},
        "y180_I_wf_q15": {"type": "arbitrary", "samples": y180_I_wf_q15.tolist()},
        "y180_Q_wf_q15": {"type": "arbitrary", "samples": y180_Q_wf_q15.tolist()},
        "minus_y90_I_wf_q15": {"type": "arbitrary", "samples": minus_y90_I_wf_q15.tolist()},
        "minus_y90_Q_wf_q15": {"type": "arbitrary", "samples": minus_y90_Q_wf_q15.tolist()},
        "readout_wf_q15": {"type": "constant", "sample": readout_amp_q15},


        "x90_I_wf_q16": {"type": "arbitrary", "samples": x90_I_wf_q16.tolist()},
        "x90_Q_wf_q16": {"type": "arbitrary", "samples": x90_Q_wf_q16.tolist()},
        "x180_I_wf_q16": {"type": "arbitrary", "samples": x180_I_wf_q16.tolist()},
        "x180_Q_wf_q16": {"type": "arbitrary", "samples": x180_Q_wf_q16.tolist()},
        "minus_x90_I_wf_q16": {"type": "arbitrary", "samples": minus_x90_I_wf_q16.tolist()},
        "minus_x90_Q_wf_q16": {"type": "arbitrary", "samples": minus_x90_Q_wf_q16.tolist()},
        "y90_I_wf_q16": {"type": "arbitrary", "samples": y90_I_wf_q16.tolist()},
        "y90_Q_wf_q16": {"type": "arbitrary", "samples": y90_Q_wf_q16.tolist()},
        "y180_I_wf_q16": {"type": "arbitrary", "samples": y180_I_wf_q16.tolist()},
        "y180_Q_wf_q16": {"type": "arbitrary", "samples": y180_Q_wf_q16.tolist()},
        "minus_y90_I_wf_q16": {"type": "arbitrary", "samples": minus_y90_I_wf_q16.tolist()},
        "minus_y90_Q_wf_q16": {"type": "arbitrary", "samples": minus_y90_Q_wf_q16.tolist()},
        "readout_wf_q16": {"type": "constant", "sample": readout_amp_q16},


        "x90_I_wf_q17": {"type": "arbitrary", "samples": x90_I_wf_q17.tolist()},
        "x90_Q_wf_q17": {"type": "arbitrary", "samples": x90_Q_wf_q17.tolist()},
        "x180_I_wf_q17": {"type": "arbitrary", "samples": x180_I_wf_q17.tolist()},
        "x180_Q_wf_q17": {"type": "arbitrary", "samples": x180_Q_wf_q17.tolist()},
        "minus_x90_I_wf_q17": {"type": "arbitrary", "samples": minus_x90_I_wf_q17.tolist()},
        "minus_x90_Q_wf_q17": {"type": "arbitrary", "samples": minus_x90_Q_wf_q17.tolist()},
        "y90_I_wf_q17": {"type": "arbitrary", "samples": y90_I_wf_q17.tolist()},
        "y90_Q_wf_q17": {"type": "arbitrary", "samples": y90_Q_wf_q17.tolist()},
        "y180_I_wf_q17": {"type": "arbitrary", "samples": y180_I_wf_q17.tolist()},
        "y180_Q_wf_q17": {"type": "arbitrary", "samples": y180_Q_wf_q17.tolist()},
        "minus_y90_I_wf_q17": {"type": "arbitrary", "samples": minus_y90_I_wf_q17.tolist()},
        "minus_y90_Q_wf_q17": {"type": "arbitrary", "samples": minus_y90_Q_wf_q17.tolist()},
        "readout_wf_q17": {"type": "constant", "sample": readout_amp_q17},


        "x90_I_wf_q18": {"type": "arbitrary", "samples": x90_I_wf_q18.tolist()},
        "x90_Q_wf_q18": {"type": "arbitrary", "samples": x90_Q_wf_q18.tolist()},
        "x180_I_wf_q18": {"type": "arbitrary", "samples": x180_I_wf_q18.tolist()},
        "x180_Q_wf_q18": {"type": "arbitrary", "samples": x180_Q_wf_q18.tolist()},
        "minus_x90_I_wf_q18": {"type": "arbitrary", "samples": minus_x90_I_wf_q18.tolist()},
        "minus_x90_Q_wf_q18": {"type": "arbitrary", "samples": minus_x90_Q_wf_q18.tolist()},
        "y90_I_wf_q18": {"type": "arbitrary", "samples": y90_I_wf_q18.tolist()},
        "y90_Q_wf_q18": {"type": "arbitrary", "samples": y90_Q_wf_q18.tolist()},
        "y180_I_wf_q18": {"type": "arbitrary", "samples": y180_I_wf_q18.tolist()},
        "y180_Q_wf_q18": {"type": "arbitrary", "samples": y180_Q_wf_q18.tolist()},
        "minus_y90_I_wf_q18": {"type": "arbitrary", "samples": minus_y90_I_wf_q18.tolist()},
        "minus_y90_Q_wf_q18": {"type": "arbitrary", "samples": minus_y90_Q_wf_q18.tolist()},
        "readout_wf_q18": {"type": "constant", "sample": readout_amp_q18},


        "x90_I_wf_q19": {"type": "arbitrary", "samples": x90_I_wf_q19.tolist()},
        "x90_Q_wf_q19": {"type": "arbitrary", "samples": x90_Q_wf_q19.tolist()},
        "x180_I_wf_q19": {"type": "arbitrary", "samples": x180_I_wf_q19.tolist()},
        "x180_Q_wf_q19": {"type": "arbitrary", "samples": x180_Q_wf_q19.tolist()},
        "minus_x90_I_wf_q19": {"type": "arbitrary", "samples": minus_x90_I_wf_q19.tolist()},
        "minus_x90_Q_wf_q19": {"type": "arbitrary", "samples": minus_x90_Q_wf_q19.tolist()},
        "y90_I_wf_q19": {"type": "arbitrary", "samples": y90_I_wf_q19.tolist()},
        "y90_Q_wf_q19": {"type": "arbitrary", "samples": y90_Q_wf_q19.tolist()},
        "y180_I_wf_q19": {"type": "arbitrary", "samples": y180_I_wf_q19.tolist()},
        "y180_Q_wf_q19": {"type": "arbitrary", "samples": y180_Q_wf_q19.tolist()},
        "minus_y90_I_wf_q19": {"type": "arbitrary", "samples": minus_y90_I_wf_q19.tolist()},
        "minus_y90_Q_wf_q19": {"type": "arbitrary", "samples": minus_y90_Q_wf_q19.tolist()},
        "readout_wf_q19": {"type": "constant", "sample": readout_amp_q19},


        "x90_I_wf_q20": {"type": "arbitrary", "samples": x90_I_wf_q20.tolist()},
        "x90_Q_wf_q20": {"type": "arbitrary", "samples": x90_Q_wf_q20.tolist()},
        "x180_I_wf_q20": {"type": "arbitrary", "samples": x180_I_wf_q20.tolist()},
        "x180_Q_wf_q20": {"type": "arbitrary", "samples": x180_Q_wf_q20.tolist()},
        "minus_x90_I_wf_q20": {"type": "arbitrary", "samples": minus_x90_I_wf_q20.tolist()},
        "minus_x90_Q_wf_q20": {"type": "arbitrary", "samples": minus_x90_Q_wf_q20.tolist()},
        "y90_I_wf_q20": {"type": "arbitrary", "samples": y90_I_wf_q20.tolist()},
        "y90_Q_wf_q20": {"type": "arbitrary", "samples": y90_Q_wf_q20.tolist()},
        "y180_I_wf_q20": {"type": "arbitrary", "samples": y180_I_wf_q20.tolist()},
        "y180_Q_wf_q20": {"type": "arbitrary", "samples": y180_Q_wf_q20.tolist()},
        "minus_y90_I_wf_q20": {"type": "arbitrary", "samples": minus_y90_I_wf_q20.tolist()},
        "minus_y90_Q_wf_q20": {"type": "arbitrary", "samples": minus_y90_Q_wf_q20.tolist()},
        "readout_wf_q20": {"type": "constant", "sample": readout_amp_q20},


        "x90_I_wf_q_C6": {"type": "arbitrary", "samples": x90_I_wf_q_C6.tolist()},
        "x90_Q_wf_q_C6": {"type": "arbitrary", "samples": x90_Q_wf_q_C6.tolist()},
        "x180_I_wf_q_C6": {"type": "arbitrary", "samples": x180_I_wf_q_C6.tolist()},
        "x180_Q_wf_q_C6": {"type": "arbitrary", "samples": x180_Q_wf_q_C6.tolist()},
        "minus_x90_I_wf_q_C6": {"type": "arbitrary", "samples": minus_x90_I_wf_q_C6.tolist()},
        "minus_x90_Q_wf_q_C6": {"type": "arbitrary", "samples": minus_x90_Q_wf_q_C6.tolist()},
        "y90_I_wf_q_C6": {"type": "arbitrary", "samples": y90_I_wf_q_C6.tolist()},
        "y90_Q_wf_q_C6": {"type": "arbitrary", "samples": y90_Q_wf_q_C6.tolist()},
        "y180_I_wf_q_C6": {"type": "arbitrary", "samples": y180_I_wf_q_C6.tolist()},
        "y180_Q_wf_q_C6": {"type": "arbitrary", "samples": y180_Q_wf_q_C6.tolist()},
        "minus_y90_I_wf_q_C6": {"type": "arbitrary", "samples": minus_y90_I_wf_q_C6.tolist()},
        "minus_y90_Q_wf_q_C6": {"type": "arbitrary", "samples": minus_y90_Q_wf_q_C6.tolist()},
        "readout_wf_q_C6": {"type": "constant", "sample": readout_amp_q_C6},


        # add all 45
        "y45_I_wf_q1": {"type": "arbitrary", "samples": y45_I_wf_q1.tolist()},
        "y45_Q_wf_q1": {"type": "arbitrary", "samples": y45_Q_wf_q1.tolist()},
        "minus_y45_I_wf_q1": {"type": "arbitrary", "samples": minus_y45_I_wf_q1.tolist()},
        "minus_y45_Q_wf_q1": {"type": "arbitrary", "samples": minus_y45_Q_wf_q1.tolist()},
        "y45_I_wf_q2": {"type": "arbitrary", "samples": y45_I_wf_q2.tolist()},
        "y45_Q_wf_q2": {"type": "arbitrary", "samples": y45_Q_wf_q2.tolist()},
        "minus_y45_I_wf_q2": {"type": "arbitrary", "samples": minus_y45_I_wf_q2.tolist()},
        "minus_y45_Q_wf_q2": {"type": "arbitrary", "samples": minus_y45_Q_wf_q2.tolist()},
        "y45_I_wf_q3": {"type": "arbitrary", "samples": y45_I_wf_q3.tolist()},
        "y45_Q_wf_q3": {"type": "arbitrary", "samples": y45_Q_wf_q3.tolist()},
        "minus_y45_I_wf_q3": {"type": "arbitrary", "samples": minus_y45_I_wf_q3.tolist()},
        "minus_y45_Q_wf_q3": {"type": "arbitrary", "samples": minus_y45_Q_wf_q3.tolist()},
        "y45_I_wf_q4": {"type": "arbitrary", "samples": y45_I_wf_q4.tolist()},
        "y45_Q_wf_q4": {"type": "arbitrary", "samples": y45_Q_wf_q4.tolist()},
        "minus_y45_I_wf_q4": {"type": "arbitrary", "samples": minus_y45_I_wf_q4.tolist()},
        "minus_y45_Q_wf_q4": {"type": "arbitrary", "samples": minus_y45_Q_wf_q4.tolist()},
        "y45_I_wf_q5": {"type": "arbitrary", "samples": y45_I_wf_q5.tolist()},
        "y45_Q_wf_q5": {"type": "arbitrary", "samples": y45_Q_wf_q5.tolist()},
        "minus_y45_I_wf_q5": {"type": "arbitrary", "samples": minus_y45_I_wf_q5.tolist()},
        "minus_y45_Q_wf_q5": {"type": "arbitrary", "samples": minus_y45_Q_wf_q5.tolist()},
        "y45_I_wf_q6": {"type": "arbitrary", "samples": y45_I_wf_q6.tolist()},
        "y45_Q_wf_q6": {"type": "arbitrary", "samples": y45_Q_wf_q6.tolist()},
        "minus_y45_I_wf_q6": {"type": "arbitrary", "samples": minus_y45_I_wf_q6.tolist()},
        "minus_y45_Q_wf_q6": {"type": "arbitrary", "samples": minus_y45_Q_wf_q6.tolist()},
        "y45_I_wf_q7": {"type": "arbitrary", "samples": y45_I_wf_q7.tolist()},
        "y45_Q_wf_q7": {"type": "arbitrary", "samples": y45_Q_wf_q7.tolist()},
        "minus_y45_I_wf_q7": {"type": "arbitrary", "samples": minus_y45_I_wf_q7.tolist()},
        "minus_y45_Q_wf_q7": {"type": "arbitrary", "samples": minus_y45_Q_wf_q7.tolist()},
        "y45_I_wf_q8": {"type": "arbitrary", "samples": y45_I_wf_q8.tolist()},
        "y45_Q_wf_q8": {"type": "arbitrary", "samples": y45_Q_wf_q8.tolist()},
        "minus_y45_I_wf_q8": {"type": "arbitrary", "samples": minus_y45_I_wf_q8.tolist()},
        "minus_y45_Q_wf_q8": {"type": "arbitrary", "samples": minus_y45_Q_wf_q8.tolist()},
        "y45_I_wf_q9": {"type": "arbitrary", "samples": y45_I_wf_q9.tolist()},
        "y45_Q_wf_q9": {"type": "arbitrary", "samples": y45_Q_wf_q9.tolist()},
        "minus_y45_I_wf_q9": {"type": "arbitrary", "samples": minus_y45_I_wf_q9.tolist()},
        "minus_y45_Q_wf_q9": {"type": "arbitrary", "samples": minus_y45_Q_wf_q9.tolist()},
        "y45_I_wf_q10": {"type": "arbitrary", "samples": y45_I_wf_q10.tolist()},
        "y45_Q_wf_q10": {"type": "arbitrary", "samples": y45_Q_wf_q10.tolist()},
        "minus_y45_I_wf_q10": {"type": "arbitrary", "samples": minus_y45_I_wf_q10.tolist()},
        "minus_y45_Q_wf_q10": {"type": "arbitrary", "samples": minus_y45_Q_wf_q10.tolist()},
        "y45_I_wf_q11": {"type": "arbitrary", "samples": y45_I_wf_q11.tolist()},
        "y45_Q_wf_q11": {"type": "arbitrary", "samples": y45_Q_wf_q11.tolist()},
        "minus_y45_I_wf_q11": {"type": "arbitrary", "samples": minus_y45_I_wf_q11.tolist()},
        "minus_y45_Q_wf_q11": {"type": "arbitrary", "samples": minus_y45_Q_wf_q11.tolist()},
        "y45_I_wf_q12": {"type": "arbitrary", "samples": y45_I_wf_q12.tolist()},
        "y45_Q_wf_q12": {"type": "arbitrary", "samples": y45_Q_wf_q12.tolist()},
        "minus_y45_I_wf_q12": {"type": "arbitrary", "samples": minus_y45_I_wf_q12.tolist()},
        "minus_y45_Q_wf_q12": {"type": "arbitrary", "samples": minus_y45_Q_wf_q12.tolist()},
        "y45_I_wf_q13": {"type": "arbitrary", "samples": y45_I_wf_q13.tolist()},
        "y45_Q_wf_q13": {"type": "arbitrary", "samples": y45_Q_wf_q13.tolist()},
        "minus_y45_I_wf_q13": {"type": "arbitrary", "samples": minus_y45_I_wf_q13.tolist()},
        "minus_y45_Q_wf_q13": {"type": "arbitrary", "samples": minus_y45_Q_wf_q13.tolist()},
        "y45_I_wf_q14": {"type": "arbitrary", "samples": y45_I_wf_q14.tolist()},
        "y45_Q_wf_q14": {"type": "arbitrary", "samples": y45_Q_wf_q14.tolist()},
        "minus_y45_I_wf_q14": {"type": "arbitrary", "samples": minus_y45_I_wf_q14.tolist()},
        "minus_y45_Q_wf_q14": {"type": "arbitrary", "samples": minus_y45_Q_wf_q14.tolist()},
        "y45_I_wf_q15": {"type": "arbitrary", "samples": y45_I_wf_q15.tolist()},
        "y45_Q_wf_q15": {"type": "arbitrary", "samples": y45_Q_wf_q15.tolist()},
        "minus_y45_I_wf_q15": {"type": "arbitrary", "samples": minus_y45_I_wf_q15.tolist()},
        "minus_y45_Q_wf_q15": {"type": "arbitrary", "samples": minus_y45_Q_wf_q15.tolist()},
        "y45_I_wf_q16": {"type": "arbitrary", "samples": y45_I_wf_q16.tolist()},
        "y45_Q_wf_q16": {"type": "arbitrary", "samples": y45_Q_wf_q16.tolist()},
        "minus_y45_I_wf_q16": {"type": "arbitrary", "samples": minus_y45_I_wf_q16.tolist()},
        "minus_y45_Q_wf_q16": {"type": "arbitrary", "samples": minus_y45_Q_wf_q16.tolist()},
        "y45_I_wf_q17": {"type": "arbitrary", "samples": y45_I_wf_q17.tolist()},
        "y45_Q_wf_q17": {"type": "arbitrary", "samples": y45_Q_wf_q17.tolist()},
        "minus_y45_I_wf_q17": {"type": "arbitrary", "samples": minus_y45_I_wf_q17.tolist()},
        "minus_y45_Q_wf_q17": {"type": "arbitrary", "samples": minus_y45_Q_wf_q17.tolist()},
        "y45_I_wf_q18": {"type": "arbitrary", "samples": y45_I_wf_q18.tolist()},
        "y45_Q_wf_q18": {"type": "arbitrary", "samples": y45_Q_wf_q18.tolist()},
        "minus_y45_I_wf_q18": {"type": "arbitrary", "samples": minus_y45_I_wf_q18.tolist()},
        "minus_y45_Q_wf_q18": {"type": "arbitrary", "samples": minus_y45_Q_wf_q18.tolist()},
        "y45_I_wf_q19": {"type": "arbitrary", "samples": y45_I_wf_q19.tolist()},
        "y45_Q_wf_q19": {"type": "arbitrary", "samples": y45_Q_wf_q19.tolist()},
        "minus_y45_I_wf_q19": {"type": "arbitrary", "samples": minus_y45_I_wf_q19.tolist()},
        "minus_y45_Q_wf_q19": {"type": "arbitrary", "samples": minus_y45_Q_wf_q19.tolist()},
        "y45_I_wf_q20": {"type": "arbitrary", "samples": y45_I_wf_q20.tolist()},
        "y45_Q_wf_q20": {"type": "arbitrary", "samples": y45_Q_wf_q20.tolist()},
        "minus_y45_I_wf_q20": {"type": "arbitrary", "samples": minus_y45_I_wf_q20.tolist()},
        "minus_y45_Q_wf_q20": {"type": "arbitrary", "samples": minus_y45_Q_wf_q20.tolist()},

        "y45_I_wf_q_C6": {"type": "arbitrary", "samples": y45_I_wf_q_C6.tolist()},
        "y45_Q_wf_q_C6": {"type": "arbitrary", "samples": y45_Q_wf_q_C6.tolist()},
        "minus_y45_I_wf_q_C6": {"type": "arbitrary", "samples": minus_y45_I_wf_q_C6.tolist()},
        "minus_y45_Q_wf_q_C6": {"type": "arbitrary", "samples": minus_y45_Q_wf_q_C6.tolist()},
        ### Test waveform for DC plus sine wave pulse

        #"const_wf": {"type": "constant", "sample": 0.1}, # A DC value of 0.1V 
        # Generating sine wave samples for 10MHz, 1000ns duration Harry Added
        "sine_wf": {"type": "arbitrary", "samples": sine_samples},
        #"sine_Q_wf": {"type": "arbitrary", "samples": [np.sin(2 * np.pi * 10e6 * t / 1e9) for t in range(1000)]},




        # "readout_wf_q5": {"type": "constant", "sample": readout_amp_q5},
        # "readout_wf_q9": {"type": "constant", "sample": readout_amp_q9},
        # "readout_wf_q13": {"type": "constant", "sample": readout_amp_q13},
    },
    "digital_waveforms": {
        "ON": {"samples": [(1, 0)]},
    },
     
    #Test DC cosnt plus IF pulses
    "mixers": {
        "mixer_LF_FEM_port3": [
            {
                "intermediate_frequency": 10e6, 
                "lo_frequency": 0,             # No external LO for LF-FEM, NCO is used
                "correction": [1.0, 0.0, 0.0, 1.0], #
            }
        ],
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
        "rotated_cosine_weights_q8": {
            "cosine": [(np.cos(rotation_angle_q8), readout_len)],
            "sine": [(np.sin(rotation_angle_q8), readout_len)],
        },
        "rotated_sine_weights_q8": {
            "cosine": [(-np.sin(rotation_angle_q8), readout_len)],
            "sine": [(np.cos(rotation_angle_q8), readout_len)],
        },
        "rotated_minus_sine_weights_q8": {
            "cosine": [(np.sin(rotation_angle_q8), readout_len)],
            "sine": [(-np.cos(rotation_angle_q8), readout_len)],
        },
        "rotated_cosine_weights_q9": {
            "cosine": [(np.cos(rotation_angle_q9), readout_len)],
            "sine": [(np.sin(rotation_angle_q9), readout_len)],
        },
        "rotated_sine_weights_q9": {
            "cosine": [(-np.sin(rotation_angle_q9), readout_len)],
            "sine": [(np.cos(rotation_angle_q9), readout_len)],
        },
        "rotated_minus_sine_weights_q9": {
            "cosine": [(np.sin(rotation_angle_q9), readout_len)],
            "sine": [(-np.cos(rotation_angle_q9), readout_len)],
        },
        "rotated_cosine_weights_q10": {
            "cosine": [(np.cos(rotation_angle_q10), readout_len)],
            "sine": [(np.sin(rotation_angle_q10), readout_len)],
        },
        "rotated_sine_weights_q10": {
            "cosine": [(-np.sin(rotation_angle_q10), readout_len)],
            "sine": [(np.cos(rotation_angle_q10), readout_len)],
        },
        "rotated_minus_sine_weights_q10": {
            "cosine": [(np.sin(rotation_angle_q10), readout_len)],
            "sine": [(-np.cos(rotation_angle_q10), readout_len)],
        },
        "rotated_cosine_weights_q11": {
            "cosine": [(np.cos(rotation_angle_q11), readout_len)],
            "sine": [(np.sin(rotation_angle_q11), readout_len)],
        },
        "rotated_sine_weights_q11": {
            "cosine": [(-np.sin(rotation_angle_q11), readout_len)],
            "sine": [(np.cos(rotation_angle_q11), readout_len)],
        },
        "rotated_minus_sine_weights_q11": {
            "cosine": [(np.sin(rotation_angle_q11), readout_len)],
            "sine": [(-np.cos(rotation_angle_q11), readout_len)],
        },
        "rotated_cosine_weights_q12": {
            "cosine": [(np.cos(rotation_angle_q12), readout_len)],
            "sine": [(np.sin(rotation_angle_q12), readout_len)],
        },
        "rotated_sine_weights_q12": {
            "cosine": [(-np.sin(rotation_angle_q12), readout_len)],
            "sine": [(np.cos(rotation_angle_q12), readout_len)],
        },
        "rotated_minus_sine_weights_q12": {
            "cosine": [(np.sin(rotation_angle_q12), readout_len)],
            "sine": [(-np.cos(rotation_angle_q12), readout_len)],
        },
        "rotated_cosine_weights_q13": {
            "cosine": [(np.cos(rotation_angle_q13), readout_len)],
            "sine": [(np.sin(rotation_angle_q13), readout_len)],
        },
        "rotated_sine_weights_q13": {
            "cosine": [(-np.sin(rotation_angle_q13), readout_len)],
            "sine": [(np.cos(rotation_angle_q13), readout_len)],
        },
        "rotated_minus_sine_weights_q13": {
            "cosine": [(np.sin(rotation_angle_q13), readout_len)],
            "sine": [(-np.cos(rotation_angle_q13), readout_len)],
        },
        "rotated_cosine_weights_q14": {
            "cosine": [(np.cos(rotation_angle_q14), readout_len)],
            "sine": [(np.sin(rotation_angle_q14), readout_len)],
        },
        "rotated_sine_weights_q14": {
            "cosine": [(-np.sin(rotation_angle_q14), readout_len)],
            "sine": [(np.cos(rotation_angle_q14), readout_len)],
        },
        "rotated_minus_sine_weights_q14": {
            "cosine": [(np.sin(rotation_angle_q14), readout_len)],
            "sine": [(-np.cos(rotation_angle_q14), readout_len)],
        },
        "rotated_cosine_weights_q15": {
            "cosine": [(np.cos(rotation_angle_q15), readout_len)],
            "sine": [(np.sin(rotation_angle_q15), readout_len)],
        },
        "rotated_sine_weights_q15": {
            "cosine": [(-np.sin(rotation_angle_q15), readout_len)],
            "sine": [(np.cos(rotation_angle_q15), readout_len)],
        },
        "rotated_minus_sine_weights_q15": {
            "cosine": [(np.sin(rotation_angle_q15), readout_len)],
            "sine": [(-np.cos(rotation_angle_q15), readout_len)],
        },
        "rotated_cosine_weights_q16": {
            "cosine": [(np.cos(rotation_angle_q16), readout_len)],
            "sine": [(np.sin(rotation_angle_q16), readout_len)],
        },
        "rotated_sine_weights_q16": {
            "cosine": [(-np.sin(rotation_angle_q16), readout_len)],
            "sine": [(np.cos(rotation_angle_q16), readout_len)],
        },
        "rotated_minus_sine_weights_q16": {
            "cosine": [(np.sin(rotation_angle_q16), readout_len)],
            "sine": [(-np.cos(rotation_angle_q16), readout_len)],
        },
        "rotated_cosine_weights_q17": {
            "cosine": [(np.cos(rotation_angle_q17), readout_len)],
            "sine": [(np.sin(rotation_angle_q17), readout_len)],
        },
        "rotated_sine_weights_q17": {
            "cosine": [(-np.sin(rotation_angle_q17), readout_len)],
            "sine": [(np.cos(rotation_angle_q17), readout_len)],
        },
        "rotated_minus_sine_weights_q17": {
            "cosine": [(np.sin(rotation_angle_q17), readout_len)],
            "sine": [(-np.cos(rotation_angle_q17), readout_len)],
        },
        "rotated_cosine_weights_q18": {
            "cosine": [(np.cos(rotation_angle_q18), readout_len)],
            "sine": [(np.sin(rotation_angle_q18), readout_len)],
        },
        "rotated_sine_weights_q18": {
            "cosine": [(-np.sin(rotation_angle_q18), readout_len)],
            "sine": [(np.cos(rotation_angle_q18), readout_len)],
        },
        "rotated_minus_sine_weights_q18": {
            "cosine": [(np.sin(rotation_angle_q18), readout_len)],
            "sine": [(-np.cos(rotation_angle_q18), readout_len)],
        },
        "rotated_cosine_weights_q19": {
            "cosine": [(np.cos(rotation_angle_q19), readout_len)],
            "sine": [(np.sin(rotation_angle_q19), readout_len)],
        },
        "rotated_sine_weights_q19": {
            "cosine": [(-np.sin(rotation_angle_q19), readout_len)],
            "sine": [(np.cos(rotation_angle_q19), readout_len)],
        },
        "rotated_minus_sine_weights_q19": {
            "cosine": [(np.sin(rotation_angle_q19), readout_len)],
            "sine": [(-np.cos(rotation_angle_q19), readout_len)],
        },
        "rotated_cosine_weights_q20": {
            "cosine": [(np.cos(rotation_angle_q20), readout_len)],
            "sine": [(np.sin(rotation_angle_q20), readout_len)],
        },
        "rotated_sine_weights_q20": {
            "cosine": [(-np.sin(rotation_angle_q20), readout_len)],
            "sine": [(np.cos(rotation_angle_q20), readout_len)],
        },
        "rotated_minus_sine_weights_q20": {
            "cosine": [(np.sin(rotation_angle_q20), readout_len)],
            "sine": [(-np.cos(rotation_angle_q20), readout_len)],
        },
        "rotated_cosine_weights_q_C6": {
            "cosine": [(np.cos(rotation_angle_q_C6), readout_len)],
            "sine": [(np.sin(rotation_angle_q_C6), readout_len)],
        },
        "rotated_sine_weights_q_C6": {
            "cosine": [(-np.sin(rotation_angle_q_C6), readout_len)],
            "sine": [(np.cos(rotation_angle_q_C6), readout_len)],
        },
        "rotated_minus_sine_weights_q_C6": {
            "cosine": [(np.sin(rotation_angle_q_C6), readout_len)],
            "sine": [(-np.cos(rotation_angle_q_C6), readout_len)],
        },







        # "rotated_cosine_weights_q9": {
        #     "cosine": [(np.cos(rotation_angle_q9), readout_len)],
        #     "sine": [(np.sin(rotation_angle_q9), readout_len)],
        # },
        # "rotated_sine_weights_q9": {
        #     "cosine": [(-np.sin(rotation_angle_q9), readout_len)],
        #     "sine": [(np.cos(rotation_angle_q9), readout_len)],
        # },
        # "rotated_minus_sine_weights_q9": {
        #     "cosine": [(np.sin(rotation_angle_q9), readout_len)],
        #     "sine": [(-np.cos(rotation_angle_q9), readout_len)],
        # },
        # "rotated_cosine_weights_q13": {
        #     "cosine": [(np.cos(rotation_angle_q13), readout_len)],
        #     "sine": [(np.sin(rotation_angle_q13), readout_len)],
        # },
        # "rotated_sine_weights_q13": {
        #     "cosine": [(-np.sin(rotation_angle_q13), readout_len)],
        #     "sine": [(np.cos(rotation_angle_q13), readout_len)],
        # },
        # "rotated_minus_sine_weights_q13": {
        #     "cosine": [(np.sin(rotation_angle_q13), readout_len)],
        #     "sine": [(-np.cos(rotation_angle_q13), readout_len)],
        # },

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

        "opt_cosine_weights_q8": {
            "cosine": opt_weights_real_q8,
            "sine": opt_weights_minus_imag_q8,
        },
        "opt_sine_weights_q8": {
            "cosine": opt_weights_imag_q8,
            "sine": opt_weights_real_q8,
        },
        "opt_minus_sine_weights_q8": {
            "cosine": opt_weights_minus_imag_q8,
            "sine": opt_weights_minus_real_q8,
        },

        "opt_cosine_weights_q9": {
            "cosine": opt_weights_real_q9,
            "sine": opt_weights_minus_imag_q9,
        },
        "opt_sine_weights_q9": {
            "cosine": opt_weights_imag_q9,
            "sine": opt_weights_real_q9,
        },
        "opt_minus_sine_weights_q9": {
            "cosine": opt_weights_minus_imag_q9,
            "sine": opt_weights_minus_real_q9,
        },

        "opt_cosine_weights_q10": {
            "cosine": opt_weights_real_q10,
            "sine": opt_weights_minus_imag_q10,
        },
        "opt_sine_weights_q10": {
            "cosine": opt_weights_imag_q10,
            "sine": opt_weights_real_q10,
        },
        "opt_minus_sine_weights_q10": {
            "cosine": opt_weights_minus_imag_q10,
            "sine": opt_weights_minus_real_q10,
        },

        "opt_cosine_weights_q11": {
            "cosine": opt_weights_real_q11,
            "sine": opt_weights_minus_imag_q11,
        },
        "opt_sine_weights_q11": {
            "cosine": opt_weights_imag_q11,
            "sine": opt_weights_real_q11,
        },
        "opt_minus_sine_weights_q11": {
            "cosine": opt_weights_minus_imag_q11,
            "sine": opt_weights_minus_real_q11,
        },

        "opt_cosine_weights_q12": {
            "cosine": opt_weights_real_q12,
            "sine": opt_weights_minus_imag_q12,
        },
        "opt_sine_weights_q12": {
            "cosine": opt_weights_imag_q12,
            "sine": opt_weights_real_q12,
        },
        "opt_minus_sine_weights_q12": {
            "cosine": opt_weights_minus_imag_q12,
            "sine": opt_weights_minus_real_q12,
        },

        "opt_cosine_weights_q13": {
            "cosine": opt_weights_real_q13,
            "sine": opt_weights_minus_imag_q13,
        },
        "opt_sine_weights_q13": {
            "cosine": opt_weights_imag_q13,
            "sine": opt_weights_real_q13,
        },
        "opt_minus_sine_weights_q13": {
            "cosine": opt_weights_minus_imag_q13,
            "sine": opt_weights_minus_real_q13,
        },

        "opt_cosine_weights_q14": {
            "cosine": opt_weights_real_q14,
            "sine": opt_weights_minus_imag_q14,
        },
        "opt_sine_weights_q14": {
            "cosine": opt_weights_imag_q14,
            "sine": opt_weights_real_q14,
        },
        "opt_minus_sine_weights_q14": {
            "cosine": opt_weights_minus_imag_q14,
            "sine": opt_weights_minus_real_q14,
        },

        "opt_cosine_weights_q15": {
            "cosine": opt_weights_real_q15,
            "sine": opt_weights_minus_imag_q15,
        },
        "opt_sine_weights_q15": {
            "cosine": opt_weights_imag_q15,
            "sine": opt_weights_real_q15,
        },
        "opt_minus_sine_weights_q15": {
            "cosine": opt_weights_minus_imag_q15,
            "sine": opt_weights_minus_real_q15,
        },

        "opt_cosine_weights_q16": {
            "cosine": opt_weights_real_q16,
            "sine": opt_weights_minus_imag_q16,
        },
        "opt_sine_weights_q16": {
            "cosine": opt_weights_imag_q16,
            "sine": opt_weights_real_q16,
        },
        "opt_minus_sine_weights_q16": {
            "cosine": opt_weights_minus_imag_q16,
            "sine": opt_weights_minus_real_q16,
        },

        "opt_cosine_weights_q17": {
            "cosine": opt_weights_real_q17,
            "sine": opt_weights_minus_imag_q17,
        },
        "opt_sine_weights_q17": {
            "cosine": opt_weights_imag_q17,
            "sine": opt_weights_real_q17,
        },
        "opt_minus_sine_weights_q17": {
            "cosine": opt_weights_minus_imag_q17,
            "sine": opt_weights_minus_real_q17,
        },

        "opt_cosine_weights_q18": {
            "cosine": opt_weights_real_q18,
            "sine": opt_weights_minus_imag_q18,
        },
        "opt_sine_weights_q18": {
            "cosine": opt_weights_imag_q18,
            "sine": opt_weights_real_q18,
        },
        "opt_minus_sine_weights_q18": {
            "cosine": opt_weights_minus_imag_q18,
            "sine": opt_weights_minus_real_q18,
        },

        "opt_cosine_weights_q19": {
            "cosine": opt_weights_real_q19,
            "sine": opt_weights_minus_imag_q19,
        },
        "opt_sine_weights_q19": {
            "cosine": opt_weights_imag_q19,
            "sine": opt_weights_real_q19,
        },
        "opt_minus_sine_weights_q19": {
            "cosine": opt_weights_minus_imag_q19,
            "sine": opt_weights_minus_real_q19,
        },

        "opt_cosine_weights_q20": {
            "cosine": opt_weights_real_q20,
            "sine": opt_weights_minus_imag_q20,
        },
        "opt_sine_weights_q20": {
            "cosine": opt_weights_imag_q20,
            "sine": opt_weights_real_q20,
        },
        "opt_minus_sine_weights_q20": {
            "cosine": opt_weights_minus_imag_q20,
            "sine": opt_weights_minus_real_q20,
        },

        "opt_cosine_weights_q_C6": {
            "cosine": opt_weights_real_q_C6,
            "sine": opt_weights_minus_imag_q_C6,
        },
        "opt_sine_weights_q_C6": {
            "cosine": opt_weights_imag_q_C6,
            "sine": opt_weights_real_q_C6,
        },
        "opt_minus_sine_weights_q_C6": {
            "cosine": opt_weights_minus_imag_q_C6,
            "sine": opt_weights_minus_real_q_C6,
        },


        


        #   "opt_cosine_weights_q9": {
        #     "cosine": opt_weights_real_q9,
        #     "sine": opt_weights_minus_imag_q9,
        # },
        # "opt_sine_weights_q9": {
        #     "cosine": opt_weights_imag_q9,
        #     "sine": opt_weights_real_q9,
        # },
        # "opt_minus_sine_weights_q9": {
        #     "cosine": opt_weights_minus_imag_q9,
        #     "sine": opt_weights_minus_real_q9,
        # },
        # "opt_cosine_weights_q13": {
        #     "cosine": opt_weights_real_q13,
        #     "sine": opt_weights_minus_imag_q13,
        # },
        # "opt_sine_weights_q13": {
        #     "cosine": opt_weights_imag_q13,
        #     "sine": opt_weights_real_q13,
        # },
        # "opt_minus_sine_weights_q13": {
        #     "cosine": opt_weights_minus_imag_q13,
        #     "sine": opt_weights_minus_real_q13,
        # },

    },
}

