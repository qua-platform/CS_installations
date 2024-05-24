from pathlib import Path
import numpy as np
from set_octave import OctaveUnit, octave_declaration
from qualang_tools.config.waveform_tools import drag_gaussian_pulse_waveforms, flattop_gaussian_waveform, gaussian
from qualang_tools.units import unit

import matplotlib
matplotlib.use('TkAgg')


#######################
# AUXILIARY FUNCTIONS #
#######################
u = unit(coerce_to_integer=True)

######################
# Network parameters #
######################
# Either using Cluster (local) or Port (public):
cluster_name = "QPX_1"  # Write your cluster_name if version >= QOP220
# local:
# qop_ip = "192.168.1.77"  # Write the QM router IP address
# qop_port = None  # Write the QOP port if version < QOP220
# public:
qop_ip = "qum.phys.sinica.edu.tw"  # Write the QM router IP address
qop_port = 9800  # Write the QOP port if version < QOP220

# Path to save data
# save_dir = Path().absolute() / "QM" / "INSTALLATION" / "data"
save_dir = (Path().absolute()/"TEST"/"BETAsite"/"QM"/"OPXPlus"/"data")
run_dir = (Path().absolute()/"TEST"/"BETAsite"/"QM"/"OPXPlus"/"run")


############################
# Set octave configuration #
############################
# Custom port mapping example
port_mapping = {
    ("con1", 1): ("octave1", "I1"),
    ("con1", 2): ("octave1", "Q1"),
    ("con1", 3): ("octave1", "I2"),
    ("con1", 4): ("octave1", "Q2"),
    ("con1", 5): ("octave1", "I3"),
    ("con1", 6): ("octave1", "Q3"),
    ("con1", 7): ("octave1", "I4"),
    ("con1", 8): ("octave1", "Q4"),
    ("con1", 9): ("octave1", "I5"),
    ("con1", 10): ("octave1", "Q5"),
    ("con2", 1): ("octave2", "I1"),
    ("con2", 2): ("octave2", "Q1"),
    # ("con2", 3): ("octave2", "I2"),
    # ("con2", 4): ("octave2", "Q2"),
}

# The Octave port is 11xxx, where xxx are the last three digits of the Octave internal IP that can be accessed from
# the OPX admin panel if you QOP version is >= QOP220. Otherwise, it is 50 for Octave1, then 51, 52 and so on.
octave_1 = OctaveUnit("octave1", qop_ip, port=11250, con="con1", clock="External_1000MHz", port_mapping=port_mapping)
octave_2 = OctaveUnit("octave2", qop_ip, port=11251, con="con2", clock="External_1000MHz", port_mapping=port_mapping)

# Add the octaves
octaves = [octave_1, octave_2]
# Configure the Octaves
octave_config = octave_declaration(octaves)

#####################
# OPX configuration #
#####################

#############################################
#                  Qubits                   #
#############################################
#             LO: 5=3, 2=4; 1               #
#############################################   
qubit_LO_q1 = (5.200) * u.GHz
qubit_LO_q2 = (4.600) * u.GHz
qubit_LO_q3 = (4.600) * u.GHz
qubit_LO_q4 = qubit_LO_q2
qubit_LO_q5 = qubit_LO_q3

# Qubits IF (Mixers love 100MHz < IF < 400MHz)
qubit_IF_q1 = (-118 ) * u.MHz 
qubit_IF_q2 = (-164 ) * u.MHz 
qubit_IF_q3 = (-137 ) * u.MHz
qubit_IF_q4 = (-180 ) * u.MHz
qubit_IF_q5 = (-237 ) * u.MHz
# For comparing 2q:
# qubit_IF_q2 = qubit_IF_q1

# Relaxation time
qubit1_T1 = int(25028 * u.ns)
qubit2_T1 = int(22208 * u.ns)
qubit3_T1 = int(15672 * u.ns)
qubit4_T1 = int(28568 * u.ns)
qubit5_T1 = int(21624 * u.ns)
thermalization_time = 9 * max(qubit1_T1, qubit2_T1, qubit3_T1, qubit4_T1, qubit5_T1)

# CW pulse parameter
const_len = 100
const_amp = 270 * u.mV
# Saturation_pulse
saturation_len = 1 * u.us
saturation_amp = 0.270
# Pi pulse parameters
pi_len = 24 # 32
pi_sigma = pi_len / 4
pi_amp_q1 = 0.099
pi_amp_q2 = 0.1318
pi_amp_q3 = 0.1948
pi_amp_q4 = 0.141
pi_amp_q5 = 0.256

r90_amp_q1 = pi_amp_q1 / 2 *1.
r90_amp_q2 = pi_amp_q2 / 2 *1.0267324510810187
r90_amp_q3 = pi_amp_q3 / 2 *1.
r90_amp_q4 = pi_amp_q4 / 2 *1.0108383/.999
r90_amp_q5 = pi_amp_q5 / 2 *1.0056421673959859*.999

# DRAG coefficients (# No DRAG when drag_coef_qi=0, it's just a gaussian.)
drag_coef_q1 = 0.8999
drag_coef_q2 = 0.63
drag_coef_q3 = 0.8341
drag_coef_q4 = .983
drag_coef_q5 = 0.128
anharmonicity_q1 = - 204.46 *u.MHz      # checked
anharmonicity_q2 = - 214.24 *u.MHz      # checked
anharmonicity_q3 = + 216.32 *u.MHz      # checked
anharmonicity_q4 = + 221.52 *u.MHz      # checked
anharmonicity_q5 = - 216.84 *u.MHz      # checked
AC_stark_detuning_q1 = 0.0 * u.MHz
AC_stark_detuning_q2 = 0.0 * u.MHz
AC_stark_detuning_q3 = 0.0 * u.MHz
AC_stark_detuning_q4 = 0.0 * u.MHz
AC_stark_detuning_q5 = 0.0 * u.MHz

# DRAG waveforms (x180)
x180_wf_q1, x180_der_wf_q1 = np.array(drag_gaussian_pulse_waveforms(pi_amp_q1, pi_len, pi_sigma, drag_coef_q1, anharmonicity_q1, AC_stark_detuning_q1))
x180_I_wf_q1, x180_Q_wf_q1 = x180_wf_q1, x180_der_wf_q1
x180_wf_q2, x180_der_wf_q2 = np.array(drag_gaussian_pulse_waveforms(pi_amp_q2, pi_len, pi_sigma, drag_coef_q2, anharmonicity_q2, AC_stark_detuning_q2))
x180_I_wf_q2, x180_Q_wf_q2 = x180_wf_q2, x180_der_wf_q2
x180_wf_q3, x180_der_wf_q3 = np.array(drag_gaussian_pulse_waveforms(pi_amp_q3, pi_len, pi_sigma, drag_coef_q3, anharmonicity_q3, AC_stark_detuning_q3))
x180_I_wf_q3, x180_Q_wf_q3 = x180_wf_q3, x180_der_wf_q3
x180_wf_q4, x180_der_wf_q4 = np.array(drag_gaussian_pulse_waveforms(pi_amp_q4, pi_len, pi_sigma, drag_coef_q4, anharmonicity_q4, AC_stark_detuning_q4))
x180_I_wf_q4, x180_Q_wf_q4 = x180_wf_q4, x180_der_wf_q4
x180_wf_q5, x180_der_wf_q5 = np.array(drag_gaussian_pulse_waveforms(pi_amp_q5, pi_len, pi_sigma, drag_coef_q5, anharmonicity_q5, AC_stark_detuning_q5))
x180_I_wf_q5, x180_Q_wf_q5 = x180_wf_q5, x180_der_wf_q5
# DRAG waveforms (x90)
x90_wf_q1, x90_der_wf_q1 = np.array(drag_gaussian_pulse_waveforms(r90_amp_q1, pi_len, pi_sigma, drag_coef_q1, anharmonicity_q1, AC_stark_detuning_q1))
x90_I_wf_q1, x90_Q_wf_q1 = x90_wf_q1, x90_der_wf_q1
x90_wf_q2, x90_der_wf_q2 = np.array(drag_gaussian_pulse_waveforms(r90_amp_q2, pi_len, pi_sigma, drag_coef_q2, anharmonicity_q2, AC_stark_detuning_q2))
x90_I_wf_q2, x90_Q_wf_q2 = x90_wf_q2, x90_der_wf_q2
x90_wf_q3, x90_der_wf_q3 = np.array(drag_gaussian_pulse_waveforms(r90_amp_q3, pi_len, pi_sigma, drag_coef_q3, anharmonicity_q3, AC_stark_detuning_q3))
x90_I_wf_q3, x90_Q_wf_q3 = x90_wf_q3, x90_der_wf_q3
x90_wf_q4, x90_der_wf_q4 = np.array(drag_gaussian_pulse_waveforms(r90_amp_q4, pi_len, pi_sigma, drag_coef_q4, anharmonicity_q4, AC_stark_detuning_q4))
x90_I_wf_q4, x90_Q_wf_q4 = x90_wf_q4, x90_der_wf_q4
x90_wf_q5, x90_der_wf_q5 = np.array(drag_gaussian_pulse_waveforms(r90_amp_q5, pi_len, pi_sigma, drag_coef_q5, anharmonicity_q5, AC_stark_detuning_q5))
x90_I_wf_q5, x90_Q_wf_q5 = x90_wf_q5, x90_der_wf_q5
# DRAG waveforms (-x90)
minus_x90_wf_q1, minus_x90_der_wf_q1 = np.array(drag_gaussian_pulse_waveforms(-r90_amp_q1, pi_len, pi_sigma, drag_coef_q1, anharmonicity_q1, AC_stark_detuning_q1))
minus_x90_I_wf_q1, minus_x90_Q_wf_q1 = minus_x90_wf_q1, minus_x90_der_wf_q1
minus_x90_wf_q2, minus_x90_der_wf_q2 = np.array(drag_gaussian_pulse_waveforms(-r90_amp_q2, pi_len, pi_sigma, drag_coef_q2, anharmonicity_q2, AC_stark_detuning_q2))
minus_x90_I_wf_q2, minus_x90_Q_wf_q2 = minus_x90_wf_q2, minus_x90_der_wf_q2
minus_x90_wf_q3, minus_x90_der_wf_q3 = np.array(drag_gaussian_pulse_waveforms(-r90_amp_q3, pi_len, pi_sigma, drag_coef_q3, anharmonicity_q3, AC_stark_detuning_q3))
minus_x90_I_wf_q3, minus_x90_Q_wf_q3 = minus_x90_wf_q3, minus_x90_der_wf_q3
minus_x90_wf_q4, minus_x90_der_wf_q4 = np.array(drag_gaussian_pulse_waveforms(-r90_amp_q4, pi_len, pi_sigma, drag_coef_q4, anharmonicity_q4, AC_stark_detuning_q4))
minus_x90_I_wf_q4, minus_x90_Q_wf_q4 = minus_x90_wf_q4, minus_x90_der_wf_q4
minus_x90_wf_q5, minus_x90_der_wf_q5 = np.array(drag_gaussian_pulse_waveforms(-r90_amp_q5, pi_len, pi_sigma, drag_coef_q5, anharmonicity_q5, AC_stark_detuning_q5))
minus_x90_I_wf_q5, minus_x90_Q_wf_q5 = minus_x90_wf_q5, minus_x90_der_wf_q5
# DRAG waveforms (y180)
y180_wf_q1, y180_der_wf_q1 = np.array(drag_gaussian_pulse_waveforms(pi_amp_q1, pi_len, pi_sigma, drag_coef_q1, anharmonicity_q1, AC_stark_detuning_q1))
y180_I_wf_q1, y180_Q_wf_q1 = (-1) * y180_der_wf_q1, y180_wf_q1
y180_wf_q2, y180_der_wf_q2 = np.array(drag_gaussian_pulse_waveforms(pi_amp_q2, pi_len, pi_sigma, drag_coef_q2, anharmonicity_q2, AC_stark_detuning_q2))
y180_I_wf_q2, y180_Q_wf_q2 = (-1) * y180_der_wf_q2, y180_wf_q2
y180_wf_q3, y180_der_wf_q3 = np.array(drag_gaussian_pulse_waveforms(pi_amp_q3, pi_len, pi_sigma, drag_coef_q3, anharmonicity_q3, AC_stark_detuning_q3))
y180_I_wf_q3, y180_Q_wf_q3 = (-1) * y180_der_wf_q3, y180_wf_q3
y180_wf_q4, y180_der_wf_q4 = np.array(drag_gaussian_pulse_waveforms(pi_amp_q4, pi_len, pi_sigma, drag_coef_q4, anharmonicity_q4, AC_stark_detuning_q4))
y180_I_wf_q4, y180_Q_wf_q4 = (-1) * y180_der_wf_q4, y180_wf_q4
y180_wf_q5, y180_der_wf_q5 = np.array(drag_gaussian_pulse_waveforms(pi_amp_q5, pi_len, pi_sigma, drag_coef_q5, anharmonicity_q5, AC_stark_detuning_q5))
y180_I_wf_q5, y180_Q_wf_q5 = (-1) * y180_der_wf_q5, y180_wf_q5
# DRAG waveforms (y90)
y90_wf_q1, y90_der_wf_q1 = np.array(drag_gaussian_pulse_waveforms(pi_amp_q1 / 2, pi_len, pi_sigma, drag_coef_q1, anharmonicity_q1, AC_stark_detuning_q1))
y90_I_wf_q1, y90_Q_wf_q1 = (-1) * y90_der_wf_q1, y90_wf_q1
y90_wf_q2, y90_der_wf_q2 = np.array(drag_gaussian_pulse_waveforms(pi_amp_q2 / 2, pi_len, pi_sigma, drag_coef_q2, anharmonicity_q2, AC_stark_detuning_q2))
y90_I_wf_q2, y90_Q_wf_q2 = (-1) * y90_der_wf_q2, y90_wf_q2
y90_wf_q3, y90_der_wf_q3 = np.array(drag_gaussian_pulse_waveforms(pi_amp_q3 / 2, pi_len, pi_sigma, drag_coef_q3, anharmonicity_q3, AC_stark_detuning_q3))
y90_I_wf_q3, y90_Q_wf_q3 = (-1) * y90_der_wf_q3, y90_wf_q3
y90_wf_q4, y90_der_wf_q4 = np.array(drag_gaussian_pulse_waveforms(pi_amp_q4 / 2, pi_len, pi_sigma, drag_coef_q4, anharmonicity_q4, AC_stark_detuning_q4))
y90_I_wf_q4, y90_Q_wf_q4 = (-1) * y90_der_wf_q4, y90_wf_q4
y90_wf_q5, y90_der_wf_q5 = np.array(drag_gaussian_pulse_waveforms(pi_amp_q5 / 2, pi_len, pi_sigma, drag_coef_q5, anharmonicity_q5, AC_stark_detuning_q5))
y90_I_wf_q5, y90_Q_wf_q5 = (-1) * y90_der_wf_q5, y90_wf_q5
# DRAG waveforms (-y90)
minus_y90_wf_q1, minus_y90_der_wf_q1 = np.array(drag_gaussian_pulse_waveforms(-pi_amp_q1 / 2, pi_len, pi_sigma, drag_coef_q1, anharmonicity_q1, AC_stark_detuning_q1))
minus_y90_I_wf_q1, minus_y90_Q_wf_q1 = (-1) * minus_y90_der_wf_q1, minus_y90_wf_q1
minus_y90_wf_q2, minus_y90_der_wf_q2 = np.array(drag_gaussian_pulse_waveforms(-pi_amp_q2 / 2, pi_len, pi_sigma, drag_coef_q2, anharmonicity_q2, AC_stark_detuning_q2))
minus_y90_I_wf_q2, minus_y90_Q_wf_q2 = (-1) * minus_y90_der_wf_q2, minus_y90_wf_q2
minus_y90_wf_q3, minus_y90_der_wf_q3 = np.array(drag_gaussian_pulse_waveforms(-pi_amp_q3 / 2, pi_len, pi_sigma, drag_coef_q3, anharmonicity_q3, AC_stark_detuning_q3))
minus_y90_I_wf_q3, minus_y90_Q_wf_q3 = (-1) * minus_y90_der_wf_q3, minus_y90_wf_q3
minus_y90_wf_q4, minus_y90_der_wf_q4 = np.array(drag_gaussian_pulse_waveforms(-pi_amp_q4 / 2, pi_len, pi_sigma, drag_coef_q4, anharmonicity_q4, AC_stark_detuning_q4))
minus_y90_I_wf_q4, minus_y90_Q_wf_q4 = (-1) * minus_y90_der_wf_q4, minus_y90_wf_q4
minus_y90_wf_q5, minus_y90_der_wf_q5 = np.array(drag_gaussian_pulse_waveforms(-pi_amp_q5 / 2, pi_len, pi_sigma, drag_coef_q5, anharmonicity_q5, AC_stark_detuning_q5))
minus_y90_I_wf_q5, minus_y90_Q_wf_q5 = (-1) * minus_y90_der_wf_q5, minus_y90_wf_q5

##########################################
#               Flux line                #
##########################################
flux_settle_time = 28 * u.ns

max_frequency_point1 = 0
max_frequency_point2 = 0
max_frequency_point3 = 0
max_frequency_point4 = 0
max_frequency_point5 = 0

idle_q1 = max_frequency_point1 +0.
idle_q2 = max_frequency_point2 +0.
idle_q3 = max_frequency_point3 +0.
idle_q4 = max_frequency_point4 +0.
idle_q5 = max_frequency_point5 +0.

idle_c1 = 0
idle_c2 = 0
idle_c3 = 0
idle_c4 = 0

q5_phi0 = 0.359-(-0.396)

# Resonator frequency versus flux fit parameters according to resonator_spec_vs_flux
# amplitude * np.cos(2 * np.pi * frequency * x + phase) + offset
amplitude_fit1, frequency_fit1, phase_fit1, offset_fit1 = [0, 0, 0, 0]
amplitude_fit2, frequency_fit2, phase_fit2, offset_fit2 = [0, 0, 0, 0]
amplitude_fit3, frequency_fit3, phase_fit3, offset_fit3 = [0, 0, 0, 0]
amplitude_fit4, frequency_fit4, phase_fit4, offset_fit4 = [0, 0, 0, 0]
amplitude_fit5, frequency_fit5, phase_fit5, offset_fit5 = [0, 0, 0, 0]

const_flux_len = 200 # 360, 600, 260 max-bake: 260ns (200ns to be safe?)
const_flux_amp = 0.48 # for cz-chevron 
cryo_flux_amp = 0.142 # for cryoscope: make sure detuning < 400 MHz

# filter taps:
fir4 = []
iir4 = []

# fir5 = []
# iir5 = []
fir5 = [1.06569937, -0.98851684]
iir5 = [0.92281746]


# readout correction with filter on:
ro_corr = [0, 0, 0, 0, 0]
if len(fir5): 
    ro_corr = [60.2, 20.2, 211.6, 160.7, 123.6]

##########################################
#               two-qubit                #
##########################################
cz_point_1_2_q2 = 0.14519591 # q1 - q2 = Ec
gft_cz_1_2_q2 = flattop_gaussian_waveform(cz_point_1_2_q2-idle_q2, 8 * u.ns, 8 * u.ns)
g_cz_1_2_q2 = 0.5 * abs(0.5-idle_q2) * gaussian(16, 16/4)

# q5 -> q4:
cz5_4_len = 28#28 # ns
cz5_4_amp = (0.19449 - idle_q5) *1.0008333
cz5_4_2pi_dev = -0.188
cz4_5_2pi_dev = -0.028

# q4 -> q3:
cz4_3_len = 48 # ns
cz4_3_amp = (0.16668 - idle_q4) *0.9546288003055827
cz4_3_2pi_dev = -0.153
cz3_4_2pi_dev = -0.008

# q2 -> q3: hardest: might need to tune up q1 simultaneously
# zone-1:
# cz2_3_len = 60 #48,60 # ns
# cz2_3_amp = (0.164 - idle_q2) *1
# zone-2:
# cz2_3_len = 60 #48,60 # ns
# cz2_3_amp = (0.20040 - idle_q2) *0.9933368010473368
# zone-3:
cz2_3_len = 52 #64,52 # ns
cz2_3_amp = (0.2713 - idle_q2) *0.9903278753941791*1.0029167*.9975
cz2_3_2pi_dev = 0.048
cz3_2_2pi_dev = 0.153

# q3 -> q2: under consideration:
cz3_2_len = 32 # ns
cz3_2_amp = (0.015 - idle_q3) *1

# q1 -> q2:
cz1_2_len = 24 ## ns
cz1_2_amp = (-0.1398 - idle_q1) *0.9916667*0.9983333
cz1_2_2pi_dev = 0.053
cz2_1_2pi_dev = 0.078

#############################################
#                Resonators                 #
#############################################
resonator_LO = 5.88 * u.GHz
# Resonators IF
resonator_IF_q1 = int((34.3) * u.MHz) # 21.5
resonator_IF_q2 = int((134.4) * u.MHz)
resonator_IF_q3 = int((-22.2) * u.MHz)
resonator_IF_q4 = int((158) * u.MHz)
resonator_IF_q5 = int((63.3) * u.MHz)
# Above is for verifying wide-sweep results: -156, -38, 39, 138, 231

# Readout pulse parameters (optimal input for IQ-mixer: 125mV)
readout_len = 600 #1800
readout_amp_q1 = 0.0324
readout_amp_q2 = 0.144
readout_amp_q3 = 0.0891
readout_amp_q4 = 0.0691
readout_amp_q5 = 0.131

# TOF and depletion time
time_of_flight = 284  # must be a multiple of 4
# depletion_time = int(1000/560) * u.us
depletion_time = 37 * u.us # for resonator spectroscopy (average of 13700: >5us, 7us still safe, 8us faster)

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
else:
    opt_weights_real_q1 = [(1.0, readout_len)]
    opt_weights_minus_imag_q1 = [(1.0, readout_len)]
    opt_weights_imag_q1 = [(1.0, readout_len)]
    opt_weights_minus_real_q1 = [(1.0, readout_len)]
    opt_weights_real_q2 = [(1.0, readout_len)]
    opt_weights_minus_imag_q2 = [(1.0, readout_len)]
    opt_weights_imag_q2 = [(1.0, readout_len)]
    opt_weights_minus_real_q2 = [(1.0, readout_len)]
    opt_weights_real_q3 = [(1.0, readout_len)]
    opt_weights_minus_imag_q3 = [(1.0, readout_len)]
    opt_weights_imag_q3 = [(1.0, readout_len)]
    opt_weights_minus_real_q3 = [(1.0, readout_len)]
    opt_weights_real_q4 = [(1.0, readout_len)]
    opt_weights_minus_imag_q4 = [(1.0, readout_len)]
    opt_weights_imag_q4 = [(1.0, readout_len)]
    opt_weights_minus_real_q4 = [(1.0, readout_len)]
    opt_weights_real_q5 = [(1.0, readout_len)]
    opt_weights_minus_imag_q5 = [(1.0, readout_len)]
    opt_weights_imag_q5 = [(1.0, readout_len)]
    opt_weights_minus_real_q5 = [(1.0, readout_len)]

# state discrimination
rotation_angle_q1 = ((109.8 +ro_corr[0]) / 180) * np.pi
rotation_angle_q2 = ((188.9  +ro_corr[1]) / 180) * np.pi
rotation_angle_q3 = ((197.1 +ro_corr[2]) / 180) * np.pi
rotation_angle_q4 = ((291.0 +ro_corr[3]) / 180) * np.pi
rotation_angle_q5 = ((140.3  +ro_corr[4]) / 180) * np.pi
ge_threshold_q1 = 1.988e-03
ge_threshold_q2 = 2.365e-03
ge_threshold_q3 = 2.471e-03
ge_threshold_q4 = 6.010e-04
ge_threshold_q5 = 1.304e-03

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
                5: {"offset": 0.0},  # I qubit3 XY
                6: {"offset": 0.0},  # Q qubit3 XY
                7: {"offset": 0.0},  # I qubit2 XY
                8: {"offset": 0.0},  # Q qubit2 XY
                9: {"offset": 0.0},  # I qubit4 XY
                10: {"offset": 0.0},  # Q qubit4 XY
            },
            "digital_outputs": {
                1: {},
                3: {},
                5: {},
                7: {},
                10: {},
            },
            "analog_inputs": {
                1: {"offset": 0.006487780227661133, "gain_db": 0},  # I from down-conversion
                2: {"offset": 0.004683707580566406, "gain_db": 0},  # Q from down-conversion
            },
        },
        "con2": {
            "analog_outputs": {
                1: {"offset": 0.0},  # I qubit5 XY
                2: {"offset": 0.0},  # Q qubit5 XY
                3: {"offset": idle_c1, "filter": {'feedforward': [], 'feedback':[]}},  # coupler-1 Z
                4: {"offset": idle_c2, "filter": {'feedforward': [], 'feedback':[]}},  # coupler-2 Z
                5: {"offset": idle_q1, "filter": {'feedforward': [], 'feedback':[]}},  # qubit-1 Z
                6: {"offset": idle_q2, "filter": {'feedforward': [], 'feedback':[]}},  # qubit-2 Z
                7: {"offset": idle_q3, "filter": {'feedforward': [], 'feedback':[]}},  # qubit-3 Z
                8: {"offset": idle_q4, "filter": {'feedforward': fir4, 'feedback':iir4}},  # qubit-4 Z
                9: {"offset": idle_q5, "filter": {'feedforward': fir5, 'feedback':iir5}},  # qubit-5 Z
                10: {"offset": idle_c4, "filter": {'feedforward': [], 'feedback':[]}},  # coupler-4 Z
            },
            "digital_outputs": {
                1: {},
                3: {},
            },
            "analog_inputs": {
                1: {"offset": 0.0, "gain_db": 0},  # I from down-conversion
                2: {"offset": 0.0, "gain_db": 0},  # Q from down-conversion
            },
        },
    },
    "elements": {
        "rr1": {
            "mixInputs": {
                "I": ("con1", 1),
                "Q": ("con1", 2),
                "lo_frequency": resonator_LO,
                "mixer": "octave_octave1_1",
            },
            "intermediate_frequency": resonator_IF_q1,
            "operations": {
                "cw": "const_pulse",
                "readout": "readout_pulse_q1",
            },
            "outputs": {
                "out1": ("con1", 1),
                "out2": ("con1", 2),
            },
            "time_of_flight": time_of_flight,
            "smearing": 0,
        },
        "rr2": {
            "mixInputs": {
                "I": ("con1", 1),
                "Q": ("con1", 2),
                "lo_frequency": resonator_LO,
                "mixer": "octave_octave1_1",
            },
            "intermediate_frequency": resonator_IF_q2,
            "operations": {
                "cw": "const_pulse",
                "readout": "readout_pulse_q2",
            },
            "outputs": {
                "out1": ("con1", 1),
                "out2": ("con1", 2),
            },
            "time_of_flight": time_of_flight,
            "smearing": 0,
        },
        "rr3": {
            "mixInputs": {
                "I": ("con1", 1),
                "Q": ("con1", 2),
                "lo_frequency": resonator_LO,
                "mixer": "octave_octave1_1",
            },
            "intermediate_frequency": resonator_IF_q3,
            "operations": {
                "cw": "const_pulse",
                "readout": "readout_pulse_q3",
            },
            "outputs": {
                "out1": ("con1", 1),
                "out2": ("con1", 2),
            },
            "time_of_flight": time_of_flight,
            "smearing": 0,
        },
        "rr4": {
            "mixInputs": {
                "I": ("con1", 1),
                "Q": ("con1", 2),
                "lo_frequency": resonator_LO,
                "mixer": "octave_octave1_1",
            },
            "intermediate_frequency": resonator_IF_q4,
            "operations": {
                "cw": "const_pulse",
                "readout": "readout_pulse_q4",
            },
            "outputs": {
                "out1": ("con1", 1),
                "out2": ("con1", 2),
            },
            "time_of_flight": time_of_flight,
            "smearing": 0,
        },
        "rr5": {
            "mixInputs": {
                "I": ("con1", 1),
                "Q": ("con1", 2),
                "lo_frequency": resonator_LO,
                "mixer": "octave_octave1_1",
            },
            "intermediate_frequency": resonator_IF_q5,
            "operations": {
                "cw": "const_pulse",
                "readout": "readout_pulse_q5",
            },
            "outputs": {
                "out1": ("con1", 1),
                "out2": ("con1", 2),
            },
            "time_of_flight": time_of_flight,
            "smearing": 0,
        },
        "q1_xy": {
            "mixInputs": {
                # "I": ("con1", 3),
                # "Q": ("con1", 4),
                "I": ("con2", 1),
                "Q": ("con2", 2),
                "lo_frequency": qubit_LO_q1,
                "mixer": "octave_octave2_1",
            },
            "intermediate_frequency": qubit_IF_q1,  # frequency at offset ch7 (max freq)
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
            "mixInputs": {
                "I": ("con1", 7),
                "Q": ("con1", 8),
                "lo_frequency": qubit_LO_q2,
                "mixer": "octave_octave1_4",
            },
            "intermediate_frequency": qubit_IF_q2,  # frequency at offset ch8 (max freq)
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
        "q3_xy": {
            "mixInputs": {
                "I": ("con1", 5),
                "Q": ("con1", 6),
                "lo_frequency": qubit_LO_q3,
                "mixer": "octave_octave1_3",
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
            "mixInputs": {
                "I": ("con1", 9),
                "Q": ("con1", 10),
                "lo_frequency": qubit_LO_q4,
                "mixer": "octave_octave1_5",
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
        "q00_xy": {
            "mixInputs": {
                "I": ("con1", 9),
                "Q": ("con1", 10),
                "lo_frequency": qubit_LO_q4,
                "mixer": "octave_octave1_5",
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
            "mixInputs": {
                # "I": ("con2", 1),
                # "Q": ("con2", 2),
                "I": ("con1", 3),
                "Q": ("con1", 4),
                "lo_frequency": qubit_LO_q5,
                "mixer": "octave_octave1_2",
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
        "q1_z": {
            "singleInput": {
                "port": ("con2", 5),
            },
            "operations": {
                "const": "const_flux_pulse",
                "cz_2c1t": "cz_2c1t_pulse",

            },
        },
        "q2_z": {
            "singleInput": {
                "port": ("con2", 6),
            },
            "operations": {
                "const": "const_flux_pulse",
                "cz_3c2t": "cz_3c2t_pulse",

                # options: gft_cz_pulse_1_2_q2, g_cz_pulse_1_2_q2
                "cz_1_2": "gft_cz_pulse_1_2_q2",
            },
        },
        "q3_z": {
            "singleInput": {
                "port": ("con2", 7),
            },
            "operations": {
                "const": "const_flux_pulse",
                "cz_2c3t": "cz_2c3t_pulse",
                
            },
        },
        "q4_z": {
            "singleInput": {
                "port": ("con2", 8),
            },
            "operations": {
                "const": "const_flux_pulse",
                "cz_3c4t": "cz_3c4t_pulse",

            },
        },
        "q5_z": {
            "singleInput": {
                "port": ("con2", 9),
            },
            "operations": {
                "const": "const_flux_pulse",
                "cz_4c5t": "cz_4c5t_pulse",

            },
        },

        # couplers:
        "c1_2": {
            "singleInput": {
                "port": ("con2", 3),
            },
            "operations": {
                "const": "const_flux_pulse",
                

            },
        },
        "c2_3": {
            "singleInput": {
                "port": ("con2", 4),
            },
            "operations": {
                "const": "const_flux_pulse",
                

            },
        },
        "c4_5": {
            "singleInput": {
                "port": ("con2", 10),
            },
            "operations": {
                "const": "const_flux_pulse",
                

            },
        },
        
    },
    "pulses": {
        # General:
        "const_flux_pulse": {
            "operation": "control",
            "length": const_flux_len,
            "waveforms": {
                "single": "const_flux_wf",
            },
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

        # Relationships:
        # q5 -> q4:
        "cz_4c5t_pulse": {
            "operation": "control",
            "length": cz5_4_len,
            "waveforms": {
                "single": "cz_4c5t_wf",
            },
        },
        # q4 -> q3:
        "cz_3c4t_pulse": {
            "operation": "control",
            "length": cz4_3_len,
            "waveforms": {
                "single": "cz_3c4t_wf",
            },
        },
        # q2 -> q3:
        "cz_3c2t_pulse": {
            "operation": "control",
            "length": cz2_3_len,
            "waveforms": {
                "single": "cz_3c2t_wf",
            },
        },
        # q3 -> q2:
        "cz_2c3t_pulse": {
            "operation": "control",
            "length": cz3_2_len,
            "waveforms": {
                "single": "cz_2c3t_wf",
            },
        },
        # q1 -> q2:
        "cz_2c1t_pulse": {
            "operation": "control",
            "length": cz1_2_len,
            "waveforms": {
                "single": "cz_2c1t_wf",
            },
        },
        
        # Qubit-1:
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
        # Qubit-2:
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
        # Qubit-3:
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
        # Qubit-4:
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
        # Qubit-5:
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

        # q1-q2:
        "gft_cz_pulse_1_2_q2": {
            "operation": "control",
            "length": len(gft_cz_1_2_q2),
            "waveforms": {
                "single": "gft_cz_wf_1_2_q2",
            },
        },
        "g_cz_pulse_1_2_q2": {
            "operation": "control",
            "length": len(g_cz_1_2_q2),
            "waveforms": {
                "single": "g_cz_wf_1_2_q2",
            },
        },

    },
    "waveforms": {
        # General:
        "const_wf": {"type": "constant", "sample": const_amp},
        "saturation_wf": {"type": "constant", "sample": saturation_amp},
        "const_flux_wf": {"type": "constant", "sample": const_flux_amp},
        "zero_wf": {"type": "constant", "sample": 0.0},

        # Qubit-1:
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
        # Qubit-2:
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
        # Qubit-3:
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
        # Qubit-4:
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
        # Qubit-5:
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

        # q1-q2:
        "gft_cz_wf_1_2_q2": {"type": "arbitrary", "samples": gft_cz_1_2_q2},
        "g_cz_wf_1_2_q2": {"type": "arbitrary", "samples": g_cz_1_2_q2},

        # q5->q4:
        "cz_4c5t_wf": {"type": "arbitrary", "samples": [0.0] + [cz5_4_amp]*(cz5_4_len-1) },
        # q4->q3:
        "cz_3c4t_wf": {"type": "arbitrary", "samples": [0.0] + [cz4_3_amp]*(cz4_3_len-1) },
        # q2->q3:
        "cz_3c2t_wf": {"type": "arbitrary", "samples": [0.0] + [cz2_3_amp]*(cz2_3_len-1) },
        # q3->q2:
        "cz_2c3t_wf": {"type": "arbitrary", "samples": [0.0] + [cz3_2_amp]*(cz3_2_len-1) },
        # q1->q2:
        "cz_2c1t_wf": {"type": "arbitrary", "samples": [0.0] + [cz1_2_amp]*(cz1_2_len-1) },
    },
    "digital_waveforms": {
        "ON": {"samples": [(1, 0)]},
    },
    "integration_weights": {
        # Default:
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

        # rotated q1:
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
        # rotated q2:
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
        # rotated q3:
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
        # rotated q4:
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
        # rotated q5:
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

        # optimal weight for readout on q1:
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
        # optimal weight for readout on q2:
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
        # optimal weight for readout on q3:
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
        # optimal weight for readout on q4:
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
        # optimal weight for readout on q5:
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

    },

    "mixers": {
        # Control:
        "octave_octave1_2": [
            {
                "intermediate_frequency": qubit_IF_q5,
                "lo_frequency": qubit_LO_q5,
                "correction": (1, 0, 0, 1),
            },
        ],
        "octave_octave1_3": [
            {
                "intermediate_frequency": qubit_IF_q3,
                "lo_frequency": qubit_LO_q3,
                "correction": (1, 0, 0, 1),
            }
        ],
        "octave_octave1_4": [
            {
                "intermediate_frequency": qubit_IF_q2,
                "lo_frequency": qubit_LO_q2,
                "correction": (1, 0, 0, 1),
            }
        ],
        "octave_octave1_5": [
            {
                "intermediate_frequency": qubit_IF_q4,
                "lo_frequency": qubit_LO_q4,
                "correction": (1, 0, 0, 1),
            }
        ],
        "octave_octave2_1": [
            {
                "intermediate_frequency": qubit_IF_q1,
                "lo_frequency": qubit_LO_q1,
                "correction": (1, 0, 0, 1),
            }
        ],

        # Readout:
        "octave_octave1_1": [
            {
                "intermediate_frequency": resonator_IF_q1,
                "lo_frequency": resonator_LO,
                "correction": (1, 0, 0, 1),
            },
            {
                "intermediate_frequency": resonator_IF_q2,
                "lo_frequency": resonator_LO,
                "correction": (1, 0, 0, 1),
            },
            {
                "intermediate_frequency": resonator_IF_q3,
                "lo_frequency": resonator_LO,
                "correction": (1, 0, 0, 1),
            },
            {
                "intermediate_frequency": resonator_IF_q4,
                "lo_frequency": resonator_LO,
                "correction": (1, 0, 0, 1),
            },
            {
                "intermediate_frequency": resonator_IF_q5,
                "lo_frequency": resonator_LO,
                "correction": (1, 0, 0, 1),
            },
        ],

    },
}
