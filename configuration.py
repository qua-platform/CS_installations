from pathlib import Path
import plotly.io as pio
import numpy as np
from qualang_tools.units import unit
from set_octave import OctaveUnit, octave_declaration
from qualang_tools.config.waveform_tools import drag_gaussian_pulse_waveforms

pio.renderers.default = "browser"

#######################
# AUXILIARY FUNCTIONS #
#######################
u = unit(coerce_to_integer=True)

######################
# Network parameters #
######################
qop_ip = "172.16.33.101"  # QM router IP address
cluster_name = "CS_2"  # Write cluster_name if version >= QOP220
qop_port = None  # Write the QOP port if version < QOP220

# Path to save data
save_dir = Path(__file__).parent.resolve() / "Data"
save_dir.mkdir(exist_ok=True)

default_additional_files = {
    Path(__file__).name: Path(__file__).name,
    "optimal_weights.npz": "optimal_weights.npz",
}

############################
# Set octave configuration #
############################

# The Octave port is 11xxx, where xxx are the last three digits of the Octave internal IP that can be accessed from
# the OPX admin panel if your QOP version is >= QOP220. Otherwise, it is 50 for Octave1, then 51, 52 and so on.
octave_1 = OctaveUnit("oct1", qop_ip, port=11232, con="con1")

# If the control PC or local network is connected to the internal network of the QM router (port 2 onwards)
# or directly to the Octave (without the QM router), use the local octave IP and port 80.
#octave_ip = "192.168.88.X"
#octave_1 = OctaveUnit("octave1", octave_ip, port=80, con=con)

# Add the octave
octaves = [octave_1]
# Configure the octave config
octave_config = octave_declaration(octaves)

### TLS parameters ###

# TLS drives: 1 LO+IF pair for each TLS.
LO_TLS1 = 3.5 * u.GHz    
IF_TLS1 = 2.0 * u.MHz    
LO_TLS2 = 4.5 * u.GHz         
IF_TLS2 = 4.0 * u.MHz     
LO_TLS3 = 5.5 * u.GHz            
IF_TLS3 = 6.0 * u.MHz            
# Initial guess on TLS relaxation/thermalization values.
# More precise value will be calculated in TLS_T1.py.
T1_TLS = int(1 * u.us)
thermalization_time = 5 * T1_TLS

### Resonator Parameters ###

# Readout drives: shared LO + 3 IFs for multiplexing.
LO_RR   = 4e9            
IF_RR1  = 3e6            
IF_RR2  = 4e6            
IF_RR3  = 5e6            
# Readout pulse parameters.
READOUT_LEN = 1000      
READOUT_AMP = 0.2     
# Pulse delay to account for signal propagation time. 
# Must be multiple of 4 and >=24.
# Calculated in time_of_flight.py.
TIME_OF_FLIGHT = 24   
# Resonator relaxation time and broadening.
DEPLETION_TIME = 1 * u.us
SMEARING_LEN = 0

# Time trace integration weights for digital demodulator.
# Calculated in readout_weights_opt.py
opt_weights = False
if opt_weights:
    weights = np.load("optimal_weights.npz")
    opt_weights_real = [(x, weights["division_length"] * 4) for x in weights["weights_real"]]
    opt_weights_minus_imag = [(x, weights["division_length"] * 4) for x in weights["weights_minus_imag"]]
    opt_weights_imag = [(x, weights["division_length"] * 4) for x in weights["weights_imag"]]
    opt_weights_minus_real = [(x, weights["division_length"] * 4) for x in weights["weights_minus_real"]]
else:
    opt_weights_real = [(1.0, READOUT_LEN)]
    opt_weights_minus_imag = [(0.0, READOUT_LEN)]
    opt_weights_imag = [(0.0, READOUT_LEN)]
    opt_weights_minus_real = [(-1.0, READOUT_LEN)]

### Flux Line Parameters ###

# Flux bias that maximizes TLS resonant frequency.
# Calculated in resonator_spec_vs_flux.py
MAX_FREQ_POINT_TLS1 = 0.0
MAX_FREQ_POINT_TLS2 = 0.0
MAX_FREQ_POINT_TLS3 = 0.0
# Flux line settle time.
FLUX_SETTLE_TIME = 100 * u.ns
# Resonator frequency versus flux fit parameters according to resonator_spec_vs_flux.py.
# amplitude * np.cos(2 * np.pi * frequency * x + phase) + offset
amplitude_fit, frequency_fit, phase_fit, offset_fit = [0, 0, 0, 0]
# Flux Pulse Parameters
CONST_FLUX_LEN = 200
CONST_FLUX_AMP = 0.45
# IQ plane angle and single-shot g-e discrimination threshold.
# Calculated in IQ_blobs.py.
rotation_angle = (0 / 180) * np.pi
ge_threshold = 0.0

### Pulse Waveform Parameters ###

# Continuous wave
CONST_LEN = 1000
CONST_AMP   = 0.4
# Saturation pulse
SAT_LEN = 10 *u.us
SAT_AMP = 0.5
# Square pi pulse
SQUARE_PI_LEN = 1000
SQUARE_PI_AMP = 0.4
# Gaussian pulse parameters
GAUSS_LEN   = 1000  
GAUSS_SIGMA = 400   
_t = np.arange(GAUSS_LEN)  
_c = (GAUSS_LEN - 1) / 2.0  
_gauss_samples = (CONST_AMP * np.exp(-0.5 * ((_t - _c) / GAUSS_SIGMA) ** 2)).tolist() 
# Drag pulse parameters
drag_coef = 0
anharmonicity = -200 * u.MHz
AC_stark_detuning = 0 * u.MHz
# pi pulse, x axis
x180_len = 600
x180_sigma = x180_len / 5
x180_amp = 0.35
x180_wf, x180_der_wf = np.array(
    drag_gaussian_pulse_waveforms(x180_amp, x180_len, x180_sigma, drag_coef, anharmonicity, AC_stark_detuning)
)
x180_I_wf = x180_wf
x180_Q_wf = x180_der_wf
# pi/2 pulse, x axis
x90_len = x180_len
x90_sigma = x90_len / 5
x90_amp = x180_amp / 2
x90_wf, x90_der_wf = np.array(
    drag_gaussian_pulse_waveforms(x90_amp, x90_len, x90_sigma, drag_coef, anharmonicity, AC_stark_detuning)
)
x90_I_wf = x90_wf
x90_Q_wf = x90_der_wf
# minus pi/2 pulse, x axis
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
# pi pulse, y axis.
y180_len = x180_len
y180_sigma = y180_len / 5
y180_amp = x180_amp
y180_wf, y180_der_wf = np.array(
    drag_gaussian_pulse_waveforms(y180_amp, y180_len, y180_sigma, drag_coef, anharmonicity, AC_stark_detuning)
)
y180_I_wf = (-1) * y180_der_wf
y180_Q_wf = y180_wf
# pi/2 pulse, y axis
y90_len = x180_len
y90_sigma = y90_len / 5
y90_amp = y180_amp / 2
y90_wf, y90_der_wf = np.array(
    drag_gaussian_pulse_waveforms(y90_amp, y90_len, y90_sigma, drag_coef, anharmonicity, AC_stark_detuning)
)
y90_I_wf = (-1) * y90_der_wf
y90_Q_wf = y90_wf
# minus pi/2 pulse, y axis
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

### Octave parameters ###

# Octave LO source (likely internal)
LO_SOURCE_TLS = "internal" 
LO_SOURCE_RR  = "internal" 
# Per-port Octave digital gain/attenuation (dB). Tune later.
OCT_TLS1_GAIN_DB = -12      
OCT_TLS2_GAIN_DB = -12      
OCT_TLS3_GAIN_DB = -12     
OCT_RO_GAIN_DB   = -12    

### CONFIG ###

config = {
    "version": 1,

    "controllers": {
        "con1": {
            "analog_outputs": {
                # Readout I/Q IF to Octave OUT1
                1: {"offset": 0.0}, 2: {"offset": 0.0},
                # TLS I/Q IF to Octave RF OUTs
                3: {"offset": 0.0}, 4: {"offset": 0.0},   # TLS1 IF to Octave OUT2
                5: {"offset": 0.0}, 6: {"offset": 0.0},   # TLS2 IF to Octave OUT3
                7: {"offset": 0.0}, 8: {"offset": 0.0},   # TLS3 IF to Octave OUT4
                # Flux line (baseband, not through Octave)
                9: {"offset": 0.0},                       # Flux to shared TLS2 and TLS3
                10: {"offset": 0.0},                      # Flux to TLS1
            },
            "analog_inputs": {
                1: {"offset": 0.0},   # Octave IN1 to Readout return I
                2: {"offset": 0.0},   # Octave IN1 to Readout return Q
            },
            # digital triggers for octave
            "digital_outputs": { 
                1: {},           # trigger for octave input 1
                3: {},           # trigger for octave input 2
                5: {},           # trigger for octave input 3
                7: {},           # trigger for octave input 4
            }
        }
    },

    "octaves": {
        "oct1": {
            # RF Outputs 1,2,3,4 = RR, TLS1, TLS2, TLS3
            "RF_outputs": {
                1: {"LO_frequency": LO_RR,   "LO_source": LO_SOURCE_RR,  "gain": OCT_RO_GAIN_DB, "output_mode": "always_on"},
                2: {"LO_frequency": LO_TLS1, "LO_source": LO_SOURCE_TLS, "gain": OCT_TLS1_GAIN_DB},
                3: {"LO_frequency": LO_TLS2, "LO_source": LO_SOURCE_TLS, "gain": OCT_TLS2_GAIN_DB},
                4: {"LO_frequency": LO_TLS3, "LO_source": LO_SOURCE_TLS, "gain": OCT_TLS3_GAIN_DB},
            },
            # RF Input 1 = Readout downconversion
            "RF_inputs": {
                1: {"LO_frequency": LO_RR, "LO_source": LO_SOURCE_RR}
            },
            "connectivity": "con1",
        }
    },

    "elements": {
        # TLS drives
        "tls1": {
            "RF_inputs": {
                "port": ("oct1", 2)},
            "intermediate_frequency": IF_TLS1,
            "operations": {"const": "const_pulse",
                            "gauss": "gauss_IQ",
                            "saturation": "saturation_pulse",
                            "const_trig": "const_pulse_trig", 
                            "square_pi": "square_pi_pulse",
                            "square_pi_half": "square_pi_half_pulse",
                            "x90": "x90_pulse",
                            "x180": "x180_pulse",
                            "-x90": "-x90_pulse",
                            "y90": "y90_pulse",
                            "y180": "y180_pulse",
                            "-y90": "-y90_pulse",},
            "digitalInputs": {
                "switch": {
                    "port": ("con1", 3),
                    "delay": 87, # should be calibrated with scope
                    "buffer": 15,
                },
            },
        },
        "tls2": {
            "RF_inputs": {
                "port": ("oct1", 3)},
            "intermediate_frequency": IF_TLS2,
            "operations": {"const": "const_pulse",
                            "gauss": "gauss_IQ",
                            "saturation": "saturation_pulse",
                            "const_trig": "const_pulse_trig", 
                            "square_pi": "square_pi_pulse",
                            "square_pi_half": "square_pi_half_pulse",
                            "x90": "x90_pulse",
                            "x180": "x180_pulse",
                            "-x90": "-x90_pulse",
                            "y90": "y90_pulse",
                            "y180": "y180_pulse",
                            "-y90": "-y90_pulse",},
            "digitalInputs": {
                "switch": {
                    "port": ("con1", 5),
                    "delay": 87,
                    "buffer": 15,
                },
            },
        },
        "tls3": {
            "RF_inputs": {
                "port": ("oct1", 4)},
            "intermediate_frequency": IF_TLS3,
            "operations": {"const": "const_pulse",
                            "gauss": "gauss_IQ",
                            "saturation": "saturation_pulse",
                            "const_trig": "const_pulse_trig", 
                            "square_pi": "square_pi_pulse",
                            "square_pi_half": "square_pi_half_pulse",
                            "x90": "x90_pulse",
                            "x180": "x180_pulse",
                            "-x90": "-x90_pulse",
                            "y90": "y90_pulse",
                            "y180": "y180_pulse",
                            "-y90": "-y90_pulse",},           
            "digitalInputs": {
                "switch": {
                    "port": ("con1", 7),
                    "delay": 87,
                    "buffer": 15,
                },
            },
        },

        # Flux lines (baseband)
        "flux_tls1": {
            "singleInput": {"port": ("con1", 10)},
            "operations": {"const": "const_flux"},
        },
        "flux_tls23": {
            "singleInput": {"port": ("con1", 9)},
            "operations": {"const": "const_flux"},
        },

        # Multiplexed readout (shared output on OUT1, received on IN1)
        "rr1": { # signal path: OPX AO 1/2 -> Octave OUT1 -> Fridge
            "RF_inputs": {"port": ("oct1", 1)},
            "RF_outputs": {"port": ("oct1", 1)},  # Readout from IN1 to OPX AI 1/2
            "intermediate_frequency": IF_RR1,
            "time_of_flight": TIME_OF_FLIGHT,
            "smearing": SMEARING_LEN,
            "operations": {"readout": "readout_pulse"},
            "digitalInputs": {
                "switch": {
                    "port": ("con1", 1),
                    "delay": 87,
                    "buffer": 15,
                },
            },
        },
        "rr2": { # same as rr1 at different IF.
            "RF_inputs": {"port": ("oct1", 1)},
            "RF_outputs": {"port": ("oct1", 1)}, 
            "intermediate_frequency": IF_RR2,
            "time_of_flight": TIME_OF_FLIGHT,
            "smearing": SMEARING_LEN,
            "operations": {"readout": "readout_pulse"},
            "digitalInputs": {
                "switch": {
                    "port": ("con1", 1),
                    "delay": 87,
                    "buffer": 15,
                },
            },
        },
        "rr3": { # same as rr1 at different IF.
            "RF_inputs": {"port": ("oct1", 1)},
            "RF_outputs": {"port": ("oct1", 1)}, 
            "intermediate_frequency": IF_RR3,
            "time_of_flight": TIME_OF_FLIGHT,
            "smearing": SMEARING_LEN,
            "operations": {"readout": "readout_pulse"},
            "digitalInputs": {
                "switch": {
                    "port": ("con1", 1),
                    "delay": 87,
                    "buffer": 15,
                },
            },
        },
    },

    "pulses": {
        "const_pulse": {
            "operation": "control",
            "length": CONST_LEN,  
            "waveforms": {
                "I": "const_wf",
                "Q": "zero_wf"},
            "digital_marker": "ON",

        },
        "const_pulse_trig": {
            "operation": "control",
            "length": CONST_LEN,
            "waveforms": {
                "I": "const_wf",
                "Q": "zero_wf"},
            "digital_marker": "ON",
        },
        "saturation_pulse": {
            "operation": "control",
            "length": SAT_LEN,
            "waveforms": {
                "I": "saturation_drive_wf",
                "Q": "zero_wf"},
            "digital_marker": "ON",

        },
        "square_pi_pulse": {
            "operation": "control",
            "length": SQUARE_PI_LEN,
            "waveforms": {
                "I": "square_pi_wf",
                "Q": "zero_wf"},
            "digital_marker": "ON",
        },
        "square_pi_half_pulse": {
            "operation": "control",
            "length": SQUARE_PI_LEN,
            "waveforms": {
                "I": "square_pi_half_wf",
                "Q": "zero_wf",
            },
            "digital_marker": "ON",
        },
        "gauss_IQ": {
            "operation": "control",
            "length": GAUSS_LEN,  
            "waveforms": {"I": "gauss_drive", "Q": "zero_wf"},
            "digital_marker": "ON",
        },
        "x90_pulse": {
            "operation": "control",
            "length": x90_len,
            "waveforms": {
                "I": "x90_I_wf",
                "Q": "x90_Q_wf",
            },
            "digital_marker": "ON",
        },
        "x180_pulse": {
            "operation": "control",
            "length": x180_len,
            "waveforms": {
                "I": "x180_I_wf",
                "Q": "x180_Q_wf",
            },
            "digital_marker": "ON",
        },
        "-x90_pulse": {
            "operation": "control",
            "length": minus_x90_len,
            "waveforms": {
                "I": "minus_x90_I_wf",
                "Q": "minus_x90_Q_wf",
            },
            "digital_marker": "ON",
        },
        "y90_pulse": {
            "operation": "control",
            "length": y90_len,
            "waveforms": {
                "I": "y90_I_wf",
                "Q": "y90_Q_wf",
            },
            "digital_marker": "ON",
        },
        "y180_pulse": {
            "operation": "control",
            "length": y180_len,
            "waveforms": {
                "I": "y180_I_wf",
                "Q": "y180_Q_wf",
            },
            "digital_marker": "ON",
        },
        "-y90_pulse": {
            "operation": "control",
            "length": minus_y90_len,
            "waveforms": {
                "I": "minus_y90_I_wf",
                "Q": "minus_y90_Q_wf",
            },
            "digital_marker": "ON",

        },
        "const_flux": {
            "operation": "control",
            "length": CONST_FLUX_LEN,
            "waveforms": {"single": "const_flux_wf"},
        },
        "readout_pulse": {
            "operation": "measurement",
            "length": READOUT_LEN,
            "waveforms": {"I": "readout_I", "Q": "readout_Q"},
            "integration_weights": {"cos": "cosine_weights",
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
        }
    },

    "waveforms": {
        "const_wf": {"type": "constant", "sample": CONST_AMP},
        "saturation_drive_wf": {"type": "constant", "sample": SAT_AMP},
        "gauss_drive":  {"type": "arbitrary", "samples": _gauss_samples},  
        "square_pi_wf": {"type": "constant", "sample": SQUARE_PI_AMP},
        "square_pi_half_wf": {"type": "constant", "sample": SQUARE_PI_AMP / 2},
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

        "const_flux_wf":  {"type": "constant", "sample": CONST_FLUX_AMP},
        "readout_I": {"type": "constant", "sample": READOUT_AMP},
        "readout_Q": {"type": "constant", "sample": 0.0},
    },

    "integration_weights": {
        "cosine_weights": {
            "cosine": [(1.0, READOUT_LEN)],
            "sine": [(0.0, READOUT_LEN)],
        },
        "sine_weights": {
            "cosine": [(0.0, READOUT_LEN)],
            "sine": [(1.0, READOUT_LEN)],
        },
        "minus_sine_weights": {
            "cosine": [(0.0, READOUT_LEN)],
            "sine": [(-1.0, READOUT_LEN)],
        },
        "rotated_cosine_weights": {
            "cosine": [(np.cos(rotation_angle), READOUT_LEN)],
            "sine": [(np.sin(rotation_angle), READOUT_LEN)],
        },
        "rotated_sine_weights": {
            "cosine": [(-np.sin(rotation_angle), READOUT_LEN)],
            "sine": [(np.cos(rotation_angle), READOUT_LEN)],
        },
        "rotated_minus_sine_weights": {
            "cosine": [(np.sin(rotation_angle), READOUT_LEN)],
            "sine": [(-np.cos(rotation_angle), READOUT_LEN)],
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
    },

    "digital_waveforms": {
        "ON": {"samples": [(1, 0)]}
    },
}

