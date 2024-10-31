import numpy as np
from scipy.signal.windows import gaussian
from qm.qua import *


def gauss(amplitude, mu, sigma, length):
    t = np.linspace(-length / 2, length / 2, length)
    gauss_wave = amplitude * np.exp(-((t - mu) ** 2) / (2 * sigma**2))
    return [float(x) for x in gauss_wave]


def IQ_imbalance(g, phi):
    c = np.cos(phi)
    s = np.sin(phi)
    N = 1 / ((1 - g**2) * (2 * c**2 - 1))
    return [float(N * x) for x in [(1 - g) * c, (1 + g) * s, (1 - g) * s, (1 + g) * c]]


################
# CONFIGURATION:
################
opx_ip = "192.168.1.3"
opx_port = 10254
octave_ip = "192.168.1.3"
octave_port = 11050
con = "con1"
octave = "octave1"
cluster_name = "Cluster_1"

####### Lock-in readout ################################################################
lockin_freq = 0
lockin_amp = 0.01
readout_pulse_length = 300 * 1000  # ns  1800
readout_pulse_length22 = 300 * 1000  # ns
readout_pulse_length_calibration = 10 * 1000  # 10us
readout_pulse_length2 = 10 * 1000  # readout duration for initialization check
slice_size = 1250  # 3500 #1250 #50 # 4ns (max readout array length ~ 100)
slice_size2 = 1250  # 1250 #50 # 4ns (max readout array length ~ 100)

####### faster scan ###################################################################
step_num = 200  # number of dc values per gate
scan_vpp = 0.5

###### MIXER PARAMETER ####################
octave_gain = -5  # can set the gain from -10dB to 20dB
octave_gain2 = -4
IF = 100e6  # The IF frequency
LO = 15.60e9  # The LO frequency data set {13.0e9 ~ 17.9e9, step : 0.1e9}
IF2 = 100e6
LO2 = 13.000e9

if_freq = IF
lo_freq = LO

if_freq2 = IF2
lo_freq2 = LO2

calibration_amp = 0.125  # for best performance the IF amplitude should be set to 0.125V
calibration_pulse_length = 16
##############################################
"""
60ns
c1 : 0.484V, 152ns
c2 : 0.335V, 212ns
c3 : 0.245V, 272ns
c4 : 0.200V, 332ns

80ns
c1 : 0.499V, 168ns
c2 : 0.326V, 248ns
c3 : 0.241V, 328ns
c4 : 0.189V, 408ns

c1 : 0.499V, 176ns
c2 : 0.312V, 256ns0
c3 : 0.237V, 336ns
c4 : 0.187V, 416ns

c1 : 0.498V, 184ns
c2 : 0.31V, 264ns
c3 : 0.223V, 344ns
c4 : 0.182V, 424ns

"""
###### Pulse shape parameter #####################################
const_amp = 0.1
# const_amp2 = 0.498

## qubit 1 ##
pi_len1 = round(900 / 4) * 4  # Q1=550, Q2=340, Q4Q5=490
pi_len_cycle1 = pi_len1 // 4
half_pi_len1 = round(pi_len1 / 2 / 4) * 4  # Pulse length must be a multiple of 4
# half_pi_len1 = round(128/4)*4 # Pulse length must be a multiple of 4 #128
half_pi_len_cycle1 = half_pi_len1 // 4
pi_amp = 0.1
pi_half_amp = pi_amp

## qubit 2 ##
pi_len2 = round(1000 / 4) * 4
pi_len_cycle2 = pi_len2 // 4
half_pi_len2 = round(pi_len2 / 2 / 4) * 4  # Pulse length must be a multiple of 4
q2_pi_amp = 0.40


gauss_len = 20
gauss_amp = 0.3


intWarray_size = int(readout_pulse_length / 4)
intWarray_size22 = int(readout_pulse_length22 / 4)
intWarray_size_calibration = int(readout_pulse_length_calibration / 4)
amp_rs = 0.2
amp_rs2 = -0.2


################# rise/fall pulse parameter##################
rise_time = 20  # ns
fall_time = rise_time
rise_amp = 0.4
fall_amp = -rise_amp

##############################################################

config = {
    "version": 1,
    "controllers": {
        con: {
            "analog_outputs": {
                1: {"offset": 0.0},  # I1
                2: {"offset": 0.0},  # Q1
                3: {"offset": 0.0},  # I2
                4: {"offset": 0.0},  # Q2
                5: {"offset": 0.0},  # trig5
                6: {"offset": 0.0},  # trig6
                7: {"offset": 0.0},
                8: {"offset": 0.0},
                9: {"offset": 0.0},
                10: {"offset": 0.0},
            },
            "digital_outputs": {
                1: {},
                2: {},
                3: {},
                4: {},
                5: {},
                6: {},
                7: {},
                8: {},
                9: {},
                10: {},
            },
            "analog_inputs": {
                1: {"offset": 0.0055},  # rf-demodulated signal
                2: {"offset": 0.0055},  # rf-demodulated signal 2
            },
        }
    },
    "elements": {
        ##########################################
        # qm-qua > 1.1.5 version
        ##############   #1 IQ mixed input element  ####################
        "qe1": {
            # "mixInputs": { # "mixers" key is not needed when using the octave at qm-qua > 1.1.5
            #     "I": (con, 9),
            #     "Q": (con, 10),
            #     "lo_frequency": LO,
            #     "mixer": f"octave_{octave}_1",  # a fixed name, do not change.
            # },
            "RF_inputs": {"port": (octave, 1)},  # octave RF output port1
            "intermediate_frequency": IF,
            "operations": {
                "CW": "CW_IQ",
                "pi": "pi_pulse1",
                "pi2": "pi_pulse2",
                "half_pi": "half_pi_pulse1",
                "pi_zero": "pi_zeropulse1",
                "edsr": "IQPulse",
                "open_the_door": "please_open",
                "X/2": "half_pi_pulse1",
                "-X/2": "-half_pi_pulse1",
                "X": "pi_pulse1",
                "-X": "pi_pulse1",
                "Y/2": "Y/2Pulse",
                "Y": "YPulse",
                "-Y/2": "-Y/2Pulse",
            },
            "digitalInputs": {
                "switch": {
                    "port": (con, 1),
                    "delay": 87,
                    "buffer": 87,
                },
            },
            "outputs": {
                "out1": (con, 1),
                "out2": (con, 2),
            },
            "time_of_flight": 24,
            "smearing": 0,
        },
        "qe2": {
            # "mixInputs": {
            #     "I": (con, 3),
            #     "Q": (con, 4),
            #     "lo_frequency": LO2,
            #     "mixer": f"octave_{octave}_2",  # a fixed name, do not change.
            # },
            "RF_inputs": {"port": (octave, 2)},  # octave RF output port2
            "intermediate_frequency": IF2,
            "operations": {
                "CW": "CW_IQ",
                "pi": "pi_pulse2",
                "half_pi": "half_pi_pulse2",
                "edsr": "IQPulse",
                "open_the_door": "please_open",
            },
            "digitalInputs": {
                "switch": {
                    "port": (con, 3),
                    "delay": 87,
                    "buffer": 87,
                },
            },
            "outputs": {
                "out1": (con, 1),
                "out2": (con, 2),
            },
            "time_of_flight": 24,
            "smearing": 0,
        },
        "clifford_gate": {
            "mixInputs": {
                "I": ("con1", 1),
                "Q": ("con1", 2),
                "lo_frequency": LO,
                "mixer": f"octave_{octave}_1",  # a fixed name, do not change.
            },
            "outputs": {"output1": (con, 1)},
            "intermediate_frequency": IF,
            "operations": {
                "X/2": "half_pi_pulse1",
                "X": "pi_pulse1",
                "-X/2": "-half_pi_pulse1",
                "Y/2": "Y/2Pulse",
                "Y": "YPulse",
                "-Y/2": "-Y/2Pulse",
            },
            "digitalInputs": {
                "switch": {
                    "port": (con, 1),
                    "delay": 87,
                    "buffer": 87,
                },
            },
            "outputs": {
                "out1": (con, 1),
                "out2": (con, 2),
            },
            "time_of_flight": 24,
            "smearing": 0,
        },
        ###############   #2 single input element   ########################
        "simple_element": {
            "singleInput": {
                "port": ("con1", 1),
            },
            "intermediate_frequency": 0e6,
            "hold_offset": {"duration": 100},
            "operations": {
                "CW": "CW",
                "step": "stepPulse",
                "bottom": "bottomPulse",
                "RS": "RS",
                "RS2": "RS2",
            },
        },
        "gateL": {
            "singleInput": {
                "port": ("con1", 1),
            },
            "hold_offset": {"duration": 100},
            "digitalInputs": {
                "input_switch": {
                    "port": ("con1", 1),
                    "delay": 120,
                    "buffer": 20,
                }
            },
            "operations": {
                "CW": "CW",
                "step": "stepPulse",
                "bottom": "bottomPulse",
                "RS": "RS",
                "RS2": "RS2",
                "rise": "risePulse",
                "fall": "fallPulse",
                "trigger": "triggerPulse",  # zero waveform with marker
                "trig_gated": "triggerPulse_gated",  # zero waveform with marker
            },
        },
        "gateR": {
            "singleInput": {
                "port": ("con1", 2),
            },
            "hold_offset": {"duration": 100},
            "digitalInputs": {
                "input_switch": {
                    "port": ("con1", 2),
                    "delay": 144,
                    "buffer": 20,
                }
            },
            "operations": {
                "CW": "CW",
                "step": "stepPulse",
                "bottom": "bottomPulse",
                "rise": "risePulse",
                "fall": "fallPulse",
                "trigger": "triggerPulse",
                "trig_gated": "triggerPulse_gated",
            },
        },
        "gateM": {
            "singleInput": {
                "port": ("con1", 10),
            },
            "hold_offset": {"duration": 100},
            "digitalInputs": {
                "input_switch": {
                    "port": ("con1", 10),
                    "delay": 144,
                    "buffer": 20,
                }
            },
            "operations": {
                "CW": "CW",
                "step": "stepPulse2",
                "bottom": "bottomPulse",
                "rise": "risePulse",
                "fall": "fallPulse",
            },
        },
        "Trigger5": {
            "singleInput": {
                "port": ("con1", 5),
            },
            "hold_offset": {"duration": 16},
            "digitalInputs": {
                "input_switch": {
                    "port": ("con1", 5),
                    "delay": 144,
                    "buffer": 20,
                }
            },
            "operations": {
                "CW": "CW",
                "step": "stepPulse",
                "bottom": "bottomPulse",
                "trigger": "triggerPulse",
            },
        },
        "Trigger6": {
            "singleInput": {
                "port": ("con1", 6),
            },
            "hold_offset": {"duration": 16},
            "digitalInputs": {
                "input_switch": {
                    "port": ("con1", 6),
                    "delay": 144,
                    "buffer": 20,
                }
            },
            "operations": {
                "CW": "CW",
                "step": "stepPulse",
                "bottom": "bottomPulse",
                "trigger": "triggerPulse",
            },
        },
        "lockin": {
            "singleInput": {
                "port": ("con1", 9),
            },
            # 'mixInputs': {
            #     'I': ('con1', 1),
            #     'Q': ('con1', 2),
            #     'lo_frequency': lo_freq,
            #     'mixer': 'octave_octave1_1'
            # },
            "intermediate_frequency": lockin_freq,
            "operations": {
                "CW": "CW_lockin",
                "readout": "readout_pulse",
                "readout2": "readout_pulse2",
                "readout_calibration": "readout_pulse_calibration",
                "zeropulse": "zeroPulse",
            },
            "hold_offset": {"duration": 1},
            "outputs": {"out1": ("con1", 1)},
            "time_of_flight": 200,
            "smearing": 0,
            "outputPulseParameters": {
                "signalThreshold": 300,
                "signalPolarity": "Descending",
                "derivativeThreshold": 200,
                "derivativePolarity": "Descending",
            },
        },
        "lockin2": {
            "singleInput": {
                "port": ("con1", 10),
            },
            "intermediate_frequency": lockin_freq,
            "operations": {
                "CW": "CW_lockin",
                "readout": "readout_pulse",
                "readout2": "readout_pulse2",
                "readout_calibration": "readout_pulse_calibration",
            },
            "hold_offset": {"duration": 1},
            "outputs": {"out1": ("con1", 2)},
            "time_of_flight": 200,
            "smearing": 0,
            "outputPulseParameters": {
                "signalThreshold": 300,
                "signalPolarity": "Descending",
                "derivativeThreshold": 200,
                "derivativePolarity": "Descending",
            },
        },
    },
    "octaves": {
        octave: {
            "RF_outputs": {  # octave's up converters
                1: {
                    "LO_frequency": LO,
                    "LO_source": "internal",  # can be external or internal. internal is the default
                    "output_mode": "triggered",  # can be: "always_on" / "always_off"/ "triggered" / "triggered_reversed". "always_off" is the default
                    "gain": octave_gain,  # can be in the range [-20 : 0.5 : 20]dB
                },
                2: {
                    "LO_frequency": LO2,
                    "LO_source": "internal",
                    "output_mode": "triggered",
                    "gain": octave_gain2,
                },
                3: {
                    "LO_frequency": LO,
                    "LO_source": "internal",  # can be external or internal. internal is the default
                    "output_mode": "triggered",  # can be: "always_on" / "always_off"/ "triggered" / "triggered_reversed". "always_off" is the default
                    "gain": octave_gain,  # can be in the range [-20 : 0.5 : 20]dB
                },
                4: {
                    "LO_frequency": LO2,
                    "LO_source": "internal",
                    "output_mode": "triggered",
                    "gain": octave_gain2,
                },
                5: {
                    "LO_frequency": LO,
                    "LO_source": "internal",
                    "output_mode": "triggered",
                    "gain": octave_gain,
                },
            },
            "RF_inputs": {  # octave's down converters
                1: {
                    "RF_source": "RF_in",
                    "LO_frequency": LO,
                    "LO_source": "internal",  # internal is the default
                    "IF_mode_I": "direct",  # can be: "direct" / "mixer" / "envelope" / "off". direct is default
                    "IF_mode_Q": "direct",
                },
                2: {
                    "RF_source": "RF_in",
                    "LO_frequency": LO2,
                    "LO_source": "internal",  # external is the default
                    "IF_mode_I": "direct",  # can be: "direct" / "mixer" / "envelope" / "off". direct is default
                    "IF_mode_Q": "direct",
                },
            },
            "connectivity": con,
        }
    },
    "pulses": {
        ############ For AC Control###############
        "constPulse": {
            "operation": "control",
            "length": 800,
            "waveforms": {"single": "one_wf"},
        },
        "zeroPulse": {
            "operation": "control",
            "length": readout_pulse_length,
            "waveforms": {"single": "zero_wf"},
        },
        "piPulse": {
            "operation": "control",
            "length": 800,
            "waveforms": {"single": "pi_wf"},
        },
        "pi_halfPulse": {
            "operation": "control",
            "length": 800,
            "waveforms": {"single": "pi_half_wf"},
        },
        ##########################################
        "CW": {
            "operation": "control",
            "length": 5000,
            "waveforms": {
                "single": "const_wf",
            },
        },
        "IQPulse": {
            "operation": "control",
            "length": 200,
            "waveforms": {"I": "I_const_wf", "Q": "Q_const_wf"},
        },
        "RS": {
            "operation": "control",
            "length": gauss_len,
            "waveforms": {
                "single": "square_ramp",
            },
            "digital_marker": "ON",
        },
        "RS2": {
            "operation": "control",
            "length": gauss_len,
            "waveforms": {
                "single": "square_ramp2",
            },
            # 'digital_marker' : 'ON',
        },
        "CW_lockin": {
            "operation": "control",
            "length": 16,
            "waveforms": {
                "single": "const_lockin_wf",
            },
        },
        "stepPulse": {
            "operation": "control",
            "length": 5000,  # in 1ns
            "waveforms": {"single": "step_wf"},
            "digital_marker": "ON",
        },
        "stepPulse2": {
            "operation": "control",
            "length": 5000,  # in 1ns
            "waveforms": {"single": "step_wf"},
            "digital_marker": "ON",
        },
        "triggerPulse": {
            "operation": "control",
            "length": 200,  # in 1ns
            "waveforms": {"single": "zero_wf"},
            "digital_marker": "ON",
        },
        "triggerPulse_gated": {
            "operation": "control",
            "length": 200,  # in 1ns
            "waveforms": {"single": "zero_wf"},
            "digital_marker": "MW_ON",
        },
        "risePulse": {
            "operation": "control",
            "length": rise_time,  # in 1ns
            "waveforms": {"single": "rise"},
            "digital_marker": "ON",
        },
        "fallPulse": {
            "operation": "control",
            "length": fall_time,  # in 1ns
            "waveforms": {"single": "fall"},
            # 'digital_marker': 'ON'
        },
        "readout_pulse": {
            "operation": "measurement",
            "length": readout_pulse_length,
            "waveforms": {
                "single": "zero_wf",
            },
            "integration_weights": {
                "integ_weights_cos": "integW_cosine",
                "integ_weights_sin": "integW_sine",
                "integ_weights_cos22": "integW_cosine22",
            },
            "digital_marker": "ON",  # ON
        },
        "readout_pulse2": {
            "operation": "measurement",
            "length": readout_pulse_length2,
            "waveforms": {
                "single": "zero_wf",
            },
            "integration_weights": {
                "integ_weights_cos2": "integW_cosine2",
                "integ_weights_sin2": "integW_sine2",
            },
            "digital_marker": "ON",
        },
        "readout_pulse_calibration": {
            "operation": "measurement",
            "length": readout_pulse_length_calibration,
            "waveforms": {
                "single": "zero_wf",
            },
            "integration_weights": {
                "integ_weights_cos": "integW_cosine",
                "integ_weights_sin": "integW_sine",
                "integ_weights_cos22": "integW_cosine22",
            },
            "digital_marker": "ON",  # ON
        },
        "bottomPulse": {
            "operation": "control",
            "length": 16,  # in ns
            "waveforms": {"single": "bottom_wf"},
        },
        "CW_IQ": {
            "operation": "control",
            "length": 16,
            "waveforms": {"I": "const_wf", "Q": "zero_wf"},
            "digital_marker": "MW_ON",
        },
        "please_open": {
            "operation": "control",
            "length": 16,
            "waveforms": {"I": "zero_wf", "Q": "zero_wf"},
            "digital_marker": "MW_ON",
        },
        "calibration_pulse": {
            "operation": "control",
            "length": calibration_pulse_length,
            "waveforms": {"I": "cal_wf", "Q": "zero_wf"},
            "digital_marker": "MW_ON",
        },
        "gaussian_pulse": {
            "operation": "control",
            "length": gauss_len,
            "waveforms": {"I": "gauss_wf", "Q": "zero_wf"},
        },
        "pi_pulse1": {
            "operation": "control",
            "length": pi_len1,
            "waveforms": {"I": "pi_wf", "Q": "zero_wf"},
            "digital_marker": "MW_ON",
        },
        "half_pi_pulse1": {
            "operation": "control",
            "length": half_pi_len1,
            "waveforms": {"I": "pi_half_wf", "Q": "zero_wf"},
            "digital_marker": "MW_ON",
        },
        "-half_pi_pulse1": {
            "operation": "control",
            "length": half_pi_len1,
            "waveforms": {"I": "-pi_half_wf", "Q": "zero_wf"},
            "digital_marker": "MW_ON",
        },
        "YPulse": {
            "operation": "control",
            "length": pi_len1,
            "waveforms": {"I": "zero_wf", "Q": "pi_wf"},
            "digital_marker": "MW_ON",
        },
        "Y/2Pulse": {
            "operation": "control",
            "length": half_pi_len1,
            "waveforms": {"I": "zero_wf", "Q": "pi_half_wf"},
            "digital_marker": "MW_ON",
        },
        "-Y/2Pulse": {
            "operation": "control",
            "length": half_pi_len1,
            "waveforms": {"I": "zero_wf", "Q": "-pi_half_wf"},
            "digital_marker": "MW_ON",
        },
        "pi_pulse2": {
            "operation": "control",
            "length": pi_len2,
            "waveforms": {"I": "pi_wf2", "Q": "zero_wf"},
            "digital_marker": "MW_ON",
        },
        "half_pi_pulse2": {
            "operation": "control",
            "length": half_pi_len2,
            "waveforms": {"I": "pi_half_wf2", "Q": "zero_wf"},
            "digital_marker": "MW_ON",
        },
        "pi_zeropulse1": {
            "operation": "control",
            "length": pi_len1,
            "waveforms": {"I": "zero_wf", "Q": "zero_wf"},
            "digital_marker": "MW_ON",
        },
    },
    "waveforms": {
        "I_const_wf": {"type": "constant", "sample": 0.5},
        "Q_const_wf": {"type": "constant", "sample": 0.5},
        "cal_wf": {"type": "constant", "sample": calibration_amp},
        "const_wf": {"type": "constant", "sample": const_amp},
        "const_lockin_wf": {"type": "constant", "sample": lockin_amp},
        "zero_wf": {"type": "constant", "sample": 0.0},
        "step_wf": {
            "type": "constant",
            "sample": 0.4,
        },  # with respect to 50 Ohm, x2 if input to HighL #set 0 when using HDAWG output to output only digital markers
        "bottom_wf": {"type": "constant", "sample": -scan_vpp / 2},
        "gauss_wf": {
            "type": "arbitrary",
            "samples": gauss_amp * gaussian(gauss_len, gauss_len / 6),
        },
        "pi_wf": {"type": "constant", "sample": pi_amp},
        "pi_wf2": {"type": "constant", "sample": q2_pi_amp},
        "pi_half_wf": {"type": "constant", "sample": pi_half_amp},
        "-pi_half_wf": {"type": "constant", "sample": (-1) * pi_half_amp},
        "pi_half_wf2": {"type": "constant", "sample": pi_half_amp},
        "one_wf": {"type": "constant", "sample": 0.05},
        "square_ramp": {
            "type": "arbitrary",
            "samples": np.linspace(0.9 * amp_rs, 1.1 * amp_rs, gauss_len),
        },
        "square_ramp2": {
            "type": "arbitrary",
            "samples": np.linspace(0, -1 * amp_rs, gauss_len),
        },
        "rise": {"type": "arbitrary", "samples": np.linspace(0, rise_amp, rise_time)},
        "fall": {"type": "arbitrary", "samples": np.linspace(0, fall_amp, fall_time)},
    },
    "digital_waveforms": {
        "ON": {"samples": [(1, 10)]},
        "OFF": {"samples": [(0, 0)]},
        "MW_ON": {"samples": [(1, 0)]},
        "TEST": {"samples": [(1, 1), (0, 999)] * 200},
    },
    "integration_weights": {
        "integW_cosine": {
            "cosine": [-1.0 for i in range(intWarray_size)],
            "sine": [0.0 for i in range(intWarray_size)],
        },
        "integW_cosine22": {
            "cosine": [-1.0 for i in range(intWarray_size22)],
            "sine": [0.0 for i in range(intWarray_size22)],
        },
        "integW_cosine2": {
            "cosine": [-1.0],
            "sine": [0.0],
        },
        "integW_sine": {
            "cosine": [0.0 for i in range(intWarray_size)],
            "sine": [-1.0 for i in range(intWarray_size)],
        },
        "integW_sine2": {
            "cosine": [0.0],
            "sine": [-1.0],
        },
        "cosine_weights": {
            "cosine": [(1.0, calibration_pulse_length)],
            "sine": [(0.0, calibration_pulse_length)],
        },
        "sine_weights": {
            "cosine": [(0.0, calibration_pulse_length)],
            "sine": [(1.0, calibration_pulse_length)],
        },
        "minus_sine_weights": {
            "cosine": [(0.0, calibration_pulse_length)],
            "sine": [(-1.0, calibration_pulse_length)],
        },
    },
    "mixers": {
        f"octave_{octave}_1": [
            {
                "intermediate_frequency": IF,
                "lo_frequency": LO,
                "correction": (1, 0, 0, 1),
            },
        ],
        f"octave_{octave}_2": [
            {
                "intermediate_frequency": IF2,
                "lo_frequency": LO2,
                "correction": (1, 0, 0, 1),
            },
        ],
        # f"octave_{octave}_3":
        # f"octave_{octave}_4":
        # f"octave_{octave}_5":
    },
}

################# Randomized Benchmarking library #######################
# The list of 1 Qubit cliffords, X are pi rotations, X/2 are pi/2 rotations around the X axis (Y accordingly)
cliffords = [
    ["I"],
    ["X"],
    ["Y"],
    ["Y", "X"],
    ["X/2", "Y/2"],
    ["X/2", "-Y/2"],
    ["-X/2", "Y/2"],
    ["-X/2", "-Y/2"],
    ["Y/2", "X/2"],
    ["Y/2", "-X/2"],
    ["-Y/2", "X/2"],
    ["-Y/2", "-X/2"],
    ["X/2"],
    ["-X/2"],
    ["Y/2"],
    ["-Y/2"],
    ["-X/2", "Y/2", "X/2"],
    ["-X/2", "-Y/2", "X/2"],
    ["X", "Y/2"],
    ["X", "-Y/2"],
    ["Y", "X/2"],
    ["Y", "-X/2"],
    ["X/2", "Y/2", "X/2"],
    ["-X/2", "Y/2", "-X/2"],
]


def recovery_clifford(state: str):
    """
    Returns the required clifford to return to the ground state based on the position on the bloch sphere
    :param state: The current position on the Bloch sphere
    :return: A string representing the recovery clifford
    """
    # operations = {'x': ['I'], '-x': ['Y'], 'y': ['X/2', '-Y/2'], '-y': ['-X/2', '-Y/2'], 'z': ['-Y/2'], '-z': ['Y/2']}
    operations = {
        "z": ["I"],
        "-x": ["-Y/2"],
        "y": ["X/2"],
        "-y": ["-X/2"],
        "x": ["Y/2"],
        "-z": ["X"],
    }
    return operations[state]


def transform_state(input_state: str, transformation: str):
    """
    A function to track the next position on the Bloch sphere based on the current position and the applied clifford
    :param input_state: Position on the bloch sphere (one of the six poles)
    :param transformation: A clifford operation
    :return: The next state on the bloch sphere
    """
    transformations = {
        "x": {
            "I": "x",
            "X/2": "x",
            "X": "x",
            "-X/2": "x",
            "Y/2": "z",
            "Y": "-x",
            "-Y/2": "-z",
        },
        "-x": {
            "I": "-x",
            "X/2": "-x",
            "X": "-x",
            "-X/2": "-x",
            "Y/2": "-z",
            "Y": "x",
            "-Y/2": "z",
        },
        "y": {
            "I": "y",
            "X/2": "z",
            "X": "-y",
            "-X/2": "-z",
            "Y/2": "y",
            "Y": "y",
            "-Y/2": "y",
        },
        "-y": {
            "I": "-y",
            "X/2": "-z",
            "X": "y",
            "-X/2": "z",
            "Y/2": "-y",
            "Y": "-y",
            "-Y/2": "-y",
        },
        "z": {
            "I": "z",
            "X/2": "-y",
            "X": "-z",
            "-X/2": "y",
            "Y/2": "-x",
            "Y": "-z",
            "-Y/2": "x",
        },
        "-z": {
            "I": "-z",
            "X/2": "y",
            "X": "z",
            "-X/2": "-y",
            "Y/2": "x",
            "Y": "z",
            "-Y/2": "-x",
        },
    }

    return transformations[input_state][transformation]


def play_clifford(clifford: list, state: str, qubit):
    """

    :param clifford: a list of cliffords
    :param state: a string representing the current state on the bloch sphere
    :return: the final state on the bloch sphere
    """

    for op in clifford:
        state = transform_state(state, op)
        if op != "I":
            play(op, qubit)
    return state


def randomize_and_play_circuit(qubit, n_gates: int, init_state: str = "z"):
    """

    :param n_gates: the depth of the circuit
    :param init_state: starting position on the bloch sphere
    :return:
    """
    state = init_state
    for ind in range(n_gates):
        state = play_clifford(
            cliffords[np.random.randint(0, len(cliffords))], state, qubit
        )
    return state


def randomize_and_play_circuit_modified(qubit, clifford_vec, init_state: str = "z"):
    """

    :param n_gates: the depth of the circuit
    :param init_state: starting position on the bloch sphere
    :return:
    """
    state = init_state
    for ind in clifford_vec:
        state = play_clifford(cliffords[ind], state, qubit)
    return state


seed = 0


def randomize_and_play_circuit_modified2(qubit, n_gates: int, init_state: str = "z"):
    """

    :param n_gates: the depth of the circuit
    :param init_state: starting position on the bloch sphere
    :return:
    """
    state = init_state

    sequence_list = play_sequence(depth)
    return state


def randomize_interleaved_circuit(
    qubit, interleave_op: list, d: int, init_state: str = "z"
):
    """
    :param interleave_op: The operation to interleave represented as a list of cliffords
    :param d: the depth of the circuit
    :param init_state: the initial state on the bloch sphere
    :return: the final state on the bloch spehre
    """
    state = init_state
    for ind in range(d):
        state = play_clifford(
            cliffords[np.random.randint(0, len(cliffords))], state, qubit
        )
        state = play_clifford(interleave_op, state, qubit)
    return state


# %%
# def play_sequence(depth):
#     i = declare(int)
#     clifford_indx = declare(int)
#     sequence_list = declare(int, size=depth+1)
#     rand = Random(seed=seed)

#     with for_(i, 0, i <= depth, i + 1):
#         assign(clifford_indx, rand.rand_int(24))
#         assgin(sequence_list[i], clifford_indx)
#         with switch_(clifford_indx, unsafe=True):
#             with case_(0):
#                 wait(pi_len_cycle1, qubit)
#             with case_(1):
#                 play("X", qubit)
#             with case_(2):
#                 play("Y", qubit)
#             with case_(3):
#                 play("Y", qubit)
#                 play("X", qubit)
#             with case_(4):
#                 play("X/2", qubit)
#                 play("Y/2", qubit)
#             with case_(5):
#                 play("X/2", qubit)
#                 play("-Y/2", qubit)
#             with case_(6):
#                 play("-X/2", qubit)
#                 play("Y/2", qubit)
#             with case_(7):
#                 play("-X/2", qubit)
#                 play("-Y/2", qubit)
#             with case_(8):
#                 play("Y/2", qubit)
#                 play("X/2", qubit)
#             with case_(9):
#                 play("Y/2", qubit)
#                 play("-X/2", qubit)
#             with case_(10):
#                 play("-Y/2", qubit)
#                 play("X/2", qubit)
#             with case_(11):
#                 play("-Y/2", qubit)
#                 play("-X/2", qubit)
#             with case_(12):
#                 play("X/2", qubit)
#             with case_(13):
#                 play("-X/2", qubit)
#             with case_(14):
#                 play("Y/2", qubit)
#             with case_(15):
#                 play("-Y/2", qubit)
#             with case_(16):
#                 play("-X/2", qubit)
#                 play("Y/2", qubit)
#                 play("X/2", qubit)
#             with case_(17):
#                 play("-X/2", qubit)
#                 play("-Y/2", qubit)
#                 play("X/2", qubit)
#             with case_(18):
#                 play("X", qubit)
#                 play("Y/2", qubit)
#             with case_(19):
#                 play("X", qubit)
#                 play("-Y/2", qubit)
#             with case_(20):
#                 play("Y", qubit)
#                 play("X/2", qubit)
#             with case_(21):
#                 play("Y", qubit)
#                 play("-X/2", qubit)
#             with case_(22):
#                 play("X/2", qubit)
#                 play("Y/2", qubit)
#                 play("X/2", qubit)
#             with case_(23):
#                 play("-X/2", qubit)
#                 play("Y/2", qubit)
#                 play("-X/2", qubit)
#     return sequence_list
