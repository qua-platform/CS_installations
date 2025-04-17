
# Single QUA script generated at 2025-04-16 22:12:06.453904
# QUA library version: 1.2.2

from qm import CompilerOptionArguments
from qm.qua import *

from qm import QuantumMachinesManager
from qm.qua import *
import matplotlib.pyplot as plt
from configuration import *
from qm import SimulationConfig
from qm import generate_qua_script

with program() as prog:
    v1 = declare(int, )
    with for_(v1,0,(v1<4),(v1+1)):
        play("cw", "JPA")
        atr_r1 = declare_stream(adc_trace=True)
        measure("readout", "readout_element", adc_stream=atr_r1)
        wait(1000, )
    with stream_processing():
        atr_r1.input1().average().save("adc1")
        atr_r1.input1().save("adc1_single_run")
        atr_r1.input2().average().save("adc2")
        atr_r1.input2().save("adc2_single_run")


config = {
    "version": 1,
    "controllers": {
        "con1": {
            "analog_outputs": {
                "1": {
                    "offset": 0.0,
                },
                "2": {
                    "offset": 0.0,
                },
                "3": {
                    "offset": 0.0,
                },
                "4": {
                    "offset": 0.0,
                },
                "9": {
                    "offset": 0.0,
                },
            },
            "digital_outputs": {
                "1": {},
                "2": {},
                "3": {},
            },
            "analog_inputs": {
                "1": {
                    "offset": 0.0,
                    "gain_db": 0,
                },
                "2": {
                    "offset": 0.0,
                    "gain_db": 0,
                },
            },
        },
    },
    "elements": {
        "qubit": {
            "mixInputs": {
                "I": ('con1', 1),
                "Q": ('con1', 2),
                "lo_frequency": 6000000000,
                "mixer": "mixer_qubit",
            },
            "intermediate_frequency": 50000000,
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
        "readout_element": {
            "singleInput": {
                "port": ('con1', 1),
            },
            "digitalInputs": {
                "marker": {
                    "port": ('con1', 3),
                    "delay": 50,
                    "buffer": 0,
                },
            },
            "intermediate_frequency": 50000000,
            "operations": {
                "cw": "const_readout_pulse",
                "readout": "readout_pulse",
            },
            "outputs": {
                "out1": ('con1', 1),
                "out2": ('con1', 2),
            },
            "time_of_flight": 28,
            "smearing": 0,
        },
        "readout_counter": {
            "singleInput": {
                "port": ('con1', 1),
            },
            "digitalInputs": {
                "marker": {
                    "port": ('con1', 3),
                    "delay": 50,
                    "buffer": 0,
                },
            },
            "operations": {
                "readout": "counter_pulse",
            },
            "outputs": {
                "out1": ('con1', 1),
            },
            "outputPulseParameters": {
                "signalThreshold": 500,
                "signalPolarity": "Below",
                "derivativeThreshold": -2000,
                "derivativePolarity": "Above",
            },
            "time_of_flight": 28,
            "smearing": 0,
        },
        "JPA": {
            "singleInput": {
                "port": ('con1', 9),
            },
            "intermediate_frequency": 1000000,
            "operations": {
                "cw": "const_pulse_JPA",
            },
        },
        "AMP": {
            "singleInput": {
                "port": ('con1', 4),
            },
            "intermediate_frequency": 50000000,
            "operations": {
                "cw": "const_pulse_AMP",
            },
        },
        "TTL1": {
            "digitalInputs": {
                "marker": {
                    "port": ('con1', 1),
                    "delay": 100,
                    "buffer": 0,
                },
            },
            "operations": {
                "signal_1": "signal_ON_1",
            },
        },
        "TTL2": {
            "digitalInputs": {
                "marker": {
                    "port": ('con1', 2),
                    "delay": 100,
                    "buffer": 0,
                },
            },
            "operations": {
                "signal_2": "signal_ON_2",
            },
        },
    },
    "pulses": {
        "const_pulse": {
            "operation": "control",
            "length": 100,
            "waveforms": {
                "I": "const_wf",
                "Q": "zero_wf",
            },
        },
        "const_readout_pulse": {
            "operation": "control",
            "length": 100,
            "waveforms": {
                "single": "const_wf_readout",
            },
        },
        "const_pulse_JPA": {
            "operation": "control",
            "length": 3000,
            "waveforms": {
                "single": "const_wf_JPA",
            },
        },
        "const_pulse_AMP": {
            "operation": "control",
            "length": 5000000,
            "waveforms": {
                "single": "const_wf_AMP",
            },
        },
        "square_pi_pulse": {
            "operation": "control",
            "length": 100,
            "waveforms": {
                "I": "square_pi_wf",
                "Q": "zero_wf",
            },
        },
        "square_pi_half_pulse": {
            "operation": "control",
            "length": 100,
            "waveforms": {
                "I": "square_pi_half_wf",
                "Q": "zero_wf",
            },
        },
        "saturation_pulse": {
            "operation": "control",
            "length": 10000,
            "waveforms": {
                "I": "saturation_drive_wf",
                "Q": "zero_wf",
            },
        },
        "x90_pulse": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "x90_I_wf",
                "Q": "x90_Q_wf",
            },
        },
        "x180_pulse": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "x180_I_wf",
                "Q": "x180_Q_wf",
            },
        },
        "-x90_pulse": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "minus_x90_I_wf",
                "Q": "minus_x90_Q_wf",
            },
        },
        "y90_pulse": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "y90_I_wf",
                "Q": "y90_Q_wf",
            },
        },
        "y180_pulse": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "y180_I_wf",
                "Q": "y180_Q_wf",
            },
        },
        "-y90_pulse": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "minus_y90_I_wf",
                "Q": "minus_y90_Q_wf",
            },
        },
        "readout_pulse": {
            "operation": "measurement",
            "length": 4000,
            "waveforms": {
                "single": "readout_wf",
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
        "counter_pulse": {
            "operation": "measurement",
            "length": 1000,
            "digital_marker": "ON",
            "waveforms": {
                "single": "zero_wf",
            },
        },
        "signal_ON_1": {
            "operation": "control",
            "length": 5000,
            "digital_marker": "ON",
        },
        "signal_ON_2": {
            "operation": "control",
            "length": 5000,
            "digital_marker": "ON",
        },
    },
    "waveforms": {
        "const_wf": {
            "type": "constant",
            "sample": 0.1,
        },
        "const_wf_JPA": {
            "type": "constant",
            "sample": 0.1,
        },
        "const_wf_AMP": {
            "type": "constant",
            "sample": 0.01,
        },
        "saturation_drive_wf": {
            "type": "constant",
            "sample": 0.1,
        },
        "square_pi_wf": {
            "type": "constant",
            "sample": 0.1,
        },
        "square_pi_half_wf": {
            "type": "constant",
            "sample": 0.05,
        },
        "zero_wf": {
            "type": "constant",
            "sample": 0.0,
        },
        "x90_I_wf": {
            "type": "arbitrary",
            "samples": [0.0, 0.00310106572065179, 0.007022138372443162, 0.011888218655598174, 0.017812985288997572, 0.024887332966368074, 0.03316656418277839, 0.04265719601566239, 0.05330465031000912, 0.06498330874919292, 0.0774904765531716, 0.09054566558590248, 0.10379625802954405, 0.11683005588424064, 0.12919450587577277, 0.14042159442053573, 0.15005663854832216, 0.15768857116679075, 0.16297893825276744] + [0.1656867678789431] * 2 + [0.16297893825276744, 0.15768857116679075, 0.15005663854832216, 0.14042159442053573, 0.12919450587577277, 0.11683005588424064, 0.10379625802954405, 0.09054566558590248, 0.0774904765531716, 0.06498330874919292, 0.05330465031000912, 0.04265719601566239, 0.03316656418277839, 0.024887332966368074, 0.017812985288997572, 0.011888218655598174, 0.007022138372443162, 0.00310106572065179, 0.0],
        },
        "x90_Q_wf": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
        },
        "x180_I_wf": {
            "type": "arbitrary",
            "samples": [0.0, 0.00620213144130358, 0.014044276744886324, 0.023776437311196347, 0.035625970577995145, 0.04977466593273615, 0.06633312836555678, 0.08531439203132478, 0.10660930062001824, 0.12996661749838584, 0.1549809531063432, 0.18109133117180495, 0.2075925160590881, 0.23366011176848128, 0.25838901175154555, 0.28084318884107146, 0.3001132770966443, 0.3153771423335815, 0.32595787650553487] + [0.3313735357578862] * 2 + [0.32595787650553487, 0.3153771423335815, 0.3001132770966443, 0.28084318884107146, 0.25838901175154555, 0.23366011176848128, 0.2075925160590881, 0.18109133117180495, 0.1549809531063432, 0.12996661749838584, 0.10660930062001824, 0.08531439203132478, 0.06633312836555678, 0.04977466593273615, 0.035625970577995145, 0.023776437311196347, 0.014044276744886324, 0.00620213144130358, 0.0],
        },
        "x180_Q_wf": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
        },
        "minus_x90_I_wf": {
            "type": "arbitrary",
            "samples": [0.0, -0.00310106572065179, -0.007022138372443162, -0.011888218655598174, -0.017812985288997572, -0.024887332966368074, -0.03316656418277839, -0.04265719601566239, -0.05330465031000912, -0.06498330874919292, -0.0774904765531716, -0.09054566558590248, -0.10379625802954405, -0.11683005588424064, -0.12919450587577277, -0.14042159442053573, -0.15005663854832216, -0.15768857116679075, -0.16297893825276744] + [-0.1656867678789431] * 2 + [-0.16297893825276744, -0.15768857116679075, -0.15005663854832216, -0.14042159442053573, -0.12919450587577277, -0.11683005588424064, -0.10379625802954405, -0.09054566558590248, -0.0774904765531716, -0.06498330874919292, -0.05330465031000912, -0.04265719601566239, -0.03316656418277839, -0.024887332966368074, -0.017812985288997572, -0.011888218655598174, -0.007022138372443162, -0.00310106572065179, 0.0],
        },
        "minus_x90_Q_wf": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
        },
        "y90_Q_wf": {
            "type": "arbitrary",
            "samples": [0.0, 0.00310106572065179, 0.007022138372443162, 0.011888218655598174, 0.017812985288997572, 0.024887332966368074, 0.03316656418277839, 0.04265719601566239, 0.05330465031000912, 0.06498330874919292, 0.0774904765531716, 0.09054566558590248, 0.10379625802954405, 0.11683005588424064, 0.12919450587577277, 0.14042159442053573, 0.15005663854832216, 0.15768857116679075, 0.16297893825276744] + [0.1656867678789431] * 2 + [0.16297893825276744, 0.15768857116679075, 0.15005663854832216, 0.14042159442053573, 0.12919450587577277, 0.11683005588424064, 0.10379625802954405, 0.09054566558590248, 0.0774904765531716, 0.06498330874919292, 0.05330465031000912, 0.04265719601566239, 0.03316656418277839, 0.024887332966368074, 0.017812985288997572, 0.011888218655598174, 0.007022138372443162, 0.00310106572065179, 0.0],
        },
        "y90_I_wf": {
            "type": "arbitrary",
            "samples": [-0.0] * 40,
        },
        "y180_Q_wf": {
            "type": "arbitrary",
            "samples": [0.0, 0.00620213144130358, 0.014044276744886324, 0.023776437311196347, 0.035625970577995145, 0.04977466593273615, 0.06633312836555678, 0.08531439203132478, 0.10660930062001824, 0.12996661749838584, 0.1549809531063432, 0.18109133117180495, 0.2075925160590881, 0.23366011176848128, 0.25838901175154555, 0.28084318884107146, 0.3001132770966443, 0.3153771423335815, 0.32595787650553487] + [0.3313735357578862] * 2 + [0.32595787650553487, 0.3153771423335815, 0.3001132770966443, 0.28084318884107146, 0.25838901175154555, 0.23366011176848128, 0.2075925160590881, 0.18109133117180495, 0.1549809531063432, 0.12996661749838584, 0.10660930062001824, 0.08531439203132478, 0.06633312836555678, 0.04977466593273615, 0.035625970577995145, 0.023776437311196347, 0.014044276744886324, 0.00620213144130358, 0.0],
        },
        "y180_I_wf": {
            "type": "arbitrary",
            "samples": [-0.0] * 40,
        },
        "minus_y90_Q_wf": {
            "type": "arbitrary",
            "samples": [0.0, -0.00310106572065179, -0.007022138372443162, -0.011888218655598174, -0.017812985288997572, -0.024887332966368074, -0.03316656418277839, -0.04265719601566239, -0.05330465031000912, -0.06498330874919292, -0.0774904765531716, -0.09054566558590248, -0.10379625802954405, -0.11683005588424064, -0.12919450587577277, -0.14042159442053573, -0.15005663854832216, -0.15768857116679075, -0.16297893825276744] + [-0.1656867678789431] * 2 + [-0.16297893825276744, -0.15768857116679075, -0.15005663854832216, -0.14042159442053573, -0.12919450587577277, -0.11683005588424064, -0.10379625802954405, -0.09054566558590248, -0.0774904765531716, -0.06498330874919292, -0.05330465031000912, -0.04265719601566239, -0.03316656418277839, -0.024887332966368074, -0.017812985288997572, -0.011888218655598174, -0.007022138372443162, -0.00310106572065179, 0.0],
        },
        "minus_y90_I_wf": {
            "type": "arbitrary",
            "samples": [-0.0] * 40,
        },
        "readout_wf": {
            "type": "constant",
            "sample": 0,
        },
        "const_wf_readout": {
            "type": "constant",
            "sample": 0,
        },
    },
    "digital_waveforms": {
        "ON": {
            "samples": [(1, 0)],
        },
    },
    "integration_weights": {
        "cosine_weights": {
            "cosine": [(1.0, 4000)],
            "sine": [(0.0, 4000)],
        },
        "sine_weights": {
            "cosine": [(0.0, 4000)],
            "sine": [(1.0, 4000)],
        },
        "minus_sine_weights": {
            "cosine": [(0.0, 4000)],
            "sine": [(-1.0, 4000)],
        },
        "opt_cosine_weights": {
            "cosine": [(1.0, 4000)],
            "sine": [(0.0, 4000)],
        },
        "opt_sine_weights": {
            "cosine": [(0.0, 4000)],
            "sine": [(1.0, 4000)],
        },
        "opt_minus_sine_weights": {
            "cosine": [(0.0, 4000)],
            "sine": [(-1.0, 4000)],
        },
        "rotated_cosine_weights": {
            "cosine": [(1.0, 4000)],
            "sine": [(0.0, 4000)],
        },
        "rotated_sine_weights": {
            "cosine": [(-0.0, 4000)],
            "sine": [(1.0, 4000)],
        },
        "rotated_minus_sine_weights": {
            "cosine": [(0.0, 4000)],
            "sine": [(-1.0, 4000)],
        },
    },
    "mixers": {
        "mixer_qubit": [{'intermediate_frequency': 50000000, 'lo_frequency': 6000000000, 'correction': [1.0, 0.0, 0.0, 1.0]}],
        "mixer_JPA": [{'intermediate_frequency': 1000000, 'lo_frequency': 6950000000, 'correction': [1.0, 0.0, 0.0, 1.0]}],
        "mixer_AMP": [{'intermediate_frequency': 50000000, 'lo_frequency': 7950000000, 'correction': [1.0, 0.0, 0.0, 1.0]}],
    },
}

loaded_config = {
    "version": 1,
    "controllers": {
        "con1": {
            "type": "opx1",
            "analog_outputs": {
                "1": {
                    "offset": 0.0,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                    "crosstalk": {},
                },
                "2": {
                    "offset": 0.0,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                    "crosstalk": {},
                },
                "3": {
                    "offset": 0.0,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                    "crosstalk": {},
                },
                "4": {
                    "offset": 0.0,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                    "crosstalk": {},
                },
                "9": {
                    "offset": 0.0,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                    "crosstalk": {},
                },
            },
            "analog_inputs": {
                "1": {
                    "offset": 0.0,
                    "gain_db": 0,
                    "shareable": False,
                    "sampling_rate": 1000000000.0,
                },
                "2": {
                    "offset": 0.0,
                    "gain_db": 0,
                    "shareable": False,
                    "sampling_rate": 1000000000.0,
                },
            },
            "digital_outputs": {
                "1": {
                    "shareable": False,
                    "inverted": False,
                    "level": "LVTTL",
                },
                "2": {
                    "shareable": False,
                    "inverted": False,
                    "level": "LVTTL",
                },
                "3": {
                    "shareable": False,
                    "inverted": False,
                    "level": "LVTTL",
                },
            },
            "digital_inputs": {},
        },
    },
    "oscillators": {},
    "elements": {
        "qubit": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
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
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "mixInputs": {
                "I": ('con1', 1, 1),
                "Q": ('con1', 1, 2),
                "mixer": "mixer_qubit",
                "lo_frequency": 6000000000.0,
            },
            "intermediate_frequency": 50000000.0,
        },
        "readout_element": {
            "digitalInputs": {
                "marker": {
                    "delay": 50,
                    "buffer": 0,
                    "port": ('con1', 1, 3),
                },
            },
            "digitalOutputs": {},
            "outputs": {
                "out1": ('con1', 1, 1),
                "out2": ('con1', 1, 2),
            },
            "operations": {
                "cw": "const_readout_pulse",
                "readout": "readout_pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "singleInput": {
                "port": ('con1', 1, 1),
            },
            "smearing": 0,
            "time_of_flight": 28,
            "intermediate_frequency": 50000000.0,
        },
        "readout_counter": {
            "digitalInputs": {
                "marker": {
                    "delay": 50,
                    "buffer": 0,
                    "port": ('con1', 1, 3),
                },
            },
            "digitalOutputs": {},
            "outputs": {
                "out1": ('con1', 1, 1),
            },
            "operations": {
                "readout": "counter_pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "timeTaggingParameters": {
                "signalThreshold": 500,
                "signalPolarity": "BELOW",
                "derivativeThreshold": -2000,
                "derivativePolarity": "ABOVE",
            },
            "singleInput": {
                "port": ('con1', 1, 1),
            },
            "smearing": 0,
            "time_of_flight": 28,
        },
        "JPA": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "cw": "const_pulse_JPA",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "singleInput": {
                "port": ('con1', 1, 3),
            },
            "intermediate_frequency": 1000000.0,
        },
        "AMP": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "cw": "const_pulse_AMP",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "singleInput": {
                "port": ('con1', 1, 4),
            },
            "intermediate_frequency": 50000000.0,
        },
        "TTL1": {
            "digitalInputs": {
                "marker": {
                    "delay": 100,
                    "buffer": 0,
                    "port": ('con1', 1, 1),
                },
            },
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "signal_1": "signal_ON_1",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
        },
        "TTL2": {
            "digitalInputs": {
                "marker": {
                    "delay": 100,
                    "buffer": 0,
                    "port": ('con1', 1, 2),
                },
            },
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "signal_2": "signal_ON_2",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
        },
    },
    "pulses": {
        "const_pulse": {
            "length": 100,
            "waveforms": {
                "I": "const_wf",
                "Q": "zero_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "const_readout_pulse": {
            "length": 100,
            "waveforms": {
                "single": "const_wf_readout",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "const_pulse_JPA": {
            "length": 3000,
            "waveforms": {
                "single": "const_wf_JPA",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "const_pulse_AMP": {
            "length": 5000000,
            "waveforms": {
                "single": "const_wf_AMP",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "square_pi_pulse": {
            "length": 100,
            "waveforms": {
                "I": "square_pi_wf",
                "Q": "zero_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "square_pi_half_pulse": {
            "length": 100,
            "waveforms": {
                "I": "square_pi_half_wf",
                "Q": "zero_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "saturation_pulse": {
            "length": 10000,
            "waveforms": {
                "I": "saturation_drive_wf",
                "Q": "zero_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "x90_pulse": {
            "length": 40,
            "waveforms": {
                "I": "x90_I_wf",
                "Q": "x90_Q_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "x180_pulse": {
            "length": 40,
            "waveforms": {
                "I": "x180_I_wf",
                "Q": "x180_Q_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "-x90_pulse": {
            "length": 40,
            "waveforms": {
                "I": "minus_x90_I_wf",
                "Q": "minus_x90_Q_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "y90_pulse": {
            "length": 40,
            "waveforms": {
                "I": "y90_I_wf",
                "Q": "y90_Q_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "y180_pulse": {
            "length": 40,
            "waveforms": {
                "I": "y180_I_wf",
                "Q": "y180_Q_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "-y90_pulse": {
            "length": 40,
            "waveforms": {
                "I": "minus_y90_I_wf",
                "Q": "minus_y90_Q_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "readout_pulse": {
            "length": 4000,
            "waveforms": {
                "single": "readout_wf",
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
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "counter_pulse": {
            "length": 1000,
            "waveforms": {
                "single": "zero_wf",
            },
            "integration_weights": {},
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "signal_ON_1": {
            "length": 5000,
            "waveforms": {},
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "signal_ON_2": {
            "length": 5000,
            "waveforms": {},
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
    },
    "waveforms": {
        "const_wf": {
            "type": "constant",
            "sample": 0.1,
        },
        "const_wf_JPA": {
            "type": "constant",
            "sample": 0.1,
        },
        "const_wf_AMP": {
            "type": "constant",
            "sample": 0.01,
        },
        "saturation_drive_wf": {
            "type": "constant",
            "sample": 0.1,
        },
        "square_pi_wf": {
            "type": "constant",
            "sample": 0.1,
        },
        "square_pi_half_wf": {
            "type": "constant",
            "sample": 0.05,
        },
        "zero_wf": {
            "type": "constant",
            "sample": 0.0,
        },
        "x90_I_wf": {
            "type": "arbitrary",
            "samples": [0.0, 0.00310106572065179, 0.007022138372443162, 0.011888218655598174, 0.017812985288997572, 0.024887332966368074, 0.03316656418277839, 0.04265719601566239, 0.05330465031000912, 0.06498330874919292, 0.0774904765531716, 0.09054566558590248, 0.10379625802954405, 0.11683005588424064, 0.12919450587577277, 0.14042159442053573, 0.15005663854832216, 0.15768857116679075, 0.16297893825276744] + [0.1656867678789431] * 2 + [0.16297893825276744, 0.15768857116679075, 0.15005663854832216, 0.14042159442053573, 0.12919450587577277, 0.11683005588424064, 0.10379625802954405, 0.09054566558590248, 0.0774904765531716, 0.06498330874919292, 0.05330465031000912, 0.04265719601566239, 0.03316656418277839, 0.024887332966368074, 0.017812985288997572, 0.011888218655598174, 0.007022138372443162, 0.00310106572065179, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x90_Q_wf": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x180_I_wf": {
            "type": "arbitrary",
            "samples": [0.0, 0.00620213144130358, 0.014044276744886324, 0.023776437311196347, 0.035625970577995145, 0.04977466593273615, 0.06633312836555678, 0.08531439203132478, 0.10660930062001824, 0.12996661749838584, 0.1549809531063432, 0.18109133117180495, 0.2075925160590881, 0.23366011176848128, 0.25838901175154555, 0.28084318884107146, 0.3001132770966443, 0.3153771423335815, 0.32595787650553487] + [0.3313735357578862] * 2 + [0.32595787650553487, 0.3153771423335815, 0.3001132770966443, 0.28084318884107146, 0.25838901175154555, 0.23366011176848128, 0.2075925160590881, 0.18109133117180495, 0.1549809531063432, 0.12996661749838584, 0.10660930062001824, 0.08531439203132478, 0.06633312836555678, 0.04977466593273615, 0.035625970577995145, 0.023776437311196347, 0.014044276744886324, 0.00620213144130358, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x180_Q_wf": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_x90_I_wf": {
            "type": "arbitrary",
            "samples": [0.0, -0.00310106572065179, -0.007022138372443162, -0.011888218655598174, -0.017812985288997572, -0.024887332966368074, -0.03316656418277839, -0.04265719601566239, -0.05330465031000912, -0.06498330874919292, -0.0774904765531716, -0.09054566558590248, -0.10379625802954405, -0.11683005588424064, -0.12919450587577277, -0.14042159442053573, -0.15005663854832216, -0.15768857116679075, -0.16297893825276744] + [-0.1656867678789431] * 2 + [-0.16297893825276744, -0.15768857116679075, -0.15005663854832216, -0.14042159442053573, -0.12919450587577277, -0.11683005588424064, -0.10379625802954405, -0.09054566558590248, -0.0774904765531716, -0.06498330874919292, -0.05330465031000912, -0.04265719601566239, -0.03316656418277839, -0.024887332966368074, -0.017812985288997572, -0.011888218655598174, -0.007022138372443162, -0.00310106572065179, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_x90_Q_wf": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y90_Q_wf": {
            "type": "arbitrary",
            "samples": [0.0, 0.00310106572065179, 0.007022138372443162, 0.011888218655598174, 0.017812985288997572, 0.024887332966368074, 0.03316656418277839, 0.04265719601566239, 0.05330465031000912, 0.06498330874919292, 0.0774904765531716, 0.09054566558590248, 0.10379625802954405, 0.11683005588424064, 0.12919450587577277, 0.14042159442053573, 0.15005663854832216, 0.15768857116679075, 0.16297893825276744] + [0.1656867678789431] * 2 + [0.16297893825276744, 0.15768857116679075, 0.15005663854832216, 0.14042159442053573, 0.12919450587577277, 0.11683005588424064, 0.10379625802954405, 0.09054566558590248, 0.0774904765531716, 0.06498330874919292, 0.05330465031000912, 0.04265719601566239, 0.03316656418277839, 0.024887332966368074, 0.017812985288997572, 0.011888218655598174, 0.007022138372443162, 0.00310106572065179, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y90_I_wf": {
            "type": "arbitrary",
            "samples": [-0.0] * 40,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y180_Q_wf": {
            "type": "arbitrary",
            "samples": [0.0, 0.00620213144130358, 0.014044276744886324, 0.023776437311196347, 0.035625970577995145, 0.04977466593273615, 0.06633312836555678, 0.08531439203132478, 0.10660930062001824, 0.12996661749838584, 0.1549809531063432, 0.18109133117180495, 0.2075925160590881, 0.23366011176848128, 0.25838901175154555, 0.28084318884107146, 0.3001132770966443, 0.3153771423335815, 0.32595787650553487] + [0.3313735357578862] * 2 + [0.32595787650553487, 0.3153771423335815, 0.3001132770966443, 0.28084318884107146, 0.25838901175154555, 0.23366011176848128, 0.2075925160590881, 0.18109133117180495, 0.1549809531063432, 0.12996661749838584, 0.10660930062001824, 0.08531439203132478, 0.06633312836555678, 0.04977466593273615, 0.035625970577995145, 0.023776437311196347, 0.014044276744886324, 0.00620213144130358, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y180_I_wf": {
            "type": "arbitrary",
            "samples": [-0.0] * 40,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_y90_Q_wf": {
            "type": "arbitrary",
            "samples": [0.0, -0.00310106572065179, -0.007022138372443162, -0.011888218655598174, -0.017812985288997572, -0.024887332966368074, -0.03316656418277839, -0.04265719601566239, -0.05330465031000912, -0.06498330874919292, -0.0774904765531716, -0.09054566558590248, -0.10379625802954405, -0.11683005588424064, -0.12919450587577277, -0.14042159442053573, -0.15005663854832216, -0.15768857116679075, -0.16297893825276744] + [-0.1656867678789431] * 2 + [-0.16297893825276744, -0.15768857116679075, -0.15005663854832216, -0.14042159442053573, -0.12919450587577277, -0.11683005588424064, -0.10379625802954405, -0.09054566558590248, -0.0774904765531716, -0.06498330874919292, -0.05330465031000912, -0.04265719601566239, -0.03316656418277839, -0.024887332966368074, -0.017812985288997572, -0.011888218655598174, -0.007022138372443162, -0.00310106572065179, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_y90_I_wf": {
            "type": "arbitrary",
            "samples": [-0.0] * 40,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "readout_wf": {
            "type": "constant",
            "sample": 0.0,
        },
        "const_wf_readout": {
            "type": "constant",
            "sample": 0.0,
        },
    },
    "digital_waveforms": {
        "ON": {
            "samples": [(1, 0)],
        },
    },
    "integration_weights": {
        "cosine_weights": {
            "cosine": [(1.0, 4000)],
            "sine": [(0.0, 4000)],
        },
        "sine_weights": {
            "cosine": [(0.0, 4000)],
            "sine": [(1.0, 4000)],
        },
        "minus_sine_weights": {
            "cosine": [(0.0, 4000)],
            "sine": [(-1.0, 4000)],
        },
        "opt_cosine_weights": {
            "cosine": [(1.0, 4000)],
            "sine": [(0.0, 4000)],
        },
        "opt_sine_weights": {
            "cosine": [(0.0, 4000)],
            "sine": [(1.0, 4000)],
        },
        "opt_minus_sine_weights": {
            "cosine": [(0.0, 4000)],
            "sine": [(-1.0, 4000)],
        },
        "rotated_cosine_weights": {
            "cosine": [(1.0, 4000)],
            "sine": [(0.0, 4000)],
        },
        "rotated_sine_weights": {
            "cosine": [(-0.0, 4000)],
            "sine": [(1.0, 4000)],
        },
        "rotated_minus_sine_weights": {
            "cosine": [(0.0, 4000)],
            "sine": [(-1.0, 4000)],
        },
    },
    "mixers": {
        "mixer_qubit": [{'intermediate_frequency': 50000000.0, 'lo_frequency': 6000000000.0, 'correction': (1.0, 0.0, 0.0, 1.0)}],
        "mixer_JPA": [{'intermediate_frequency': 1000000.0, 'lo_frequency': 6950000000.0, 'correction': (1.0, 0.0, 0.0, 1.0)}],
        "mixer_AMP": [{'intermediate_frequency': 50000000.0, 'lo_frequency': 7950000000.0, 'correction': (1.0, 0.0, 0.0, 1.0)}],
    },
}


qop_ip = "172.16.33.101"  # Write the QM router IP address
cluster_name = "CS_2"  # Write your cluster_name if version >= QOP220
qmm = QuantumMachinesManager(host=qop_ip, cluster_name=cluster_name)

simulate = False

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=10_000)  # In clock cycles = 4ns
    # Simulate blocks python until the simulation is done
    job = qmm.simulate(config, prog, simulation_config)
    # Get the simulated samples
    samples = job.get_simulated_samples()
    # Plot the simulated samples
    samples.con1.plot()
    # Get the waveform report object
    waveform_report = job.get_simulated_waveform_report()
    # Cast the waveform report to a python dictionary
    waveform_dict = waveform_report.to_dict()
    # Visualize and save the waveform report
    waveform_report.create_plot(samples, plot=True, save_path=str(Path(__file__).resolve()))
else:
    # Open Quantum Machine
    qm = qmm.open_qm(config)
    # Execute program
    job = qm.execute(prog)
    # create a handle to get results
    res_handles = job.result_handles
    # Wait until the program is done
    res_handles.wait_for_all_values()
    # Fetch results and convert traces to volts
    adc1 = u.raw2volts(res_handles.get("adc1").fetch_all())
    adc1_single_run = u.raw2volts(res_handles.get("adc1_single_run").fetch_all())
    # Plot data
    plt.figure()
    plt.subplot(121)
    plt.title("Single run")
    plt.plot(adc1_single_run, label="Input 1")
    plt.xlabel("Time [ns]")
    plt.ylabel("Signal amplitude [V]")

    plt.subplot(122)
    plt.title("Averaged run")
    plt.plot(adc1, label="Input 1")
    plt.xlabel("Time [ns]")
    plt.tight_layout()

    print(f"\nInput1 mean: {np.mean(adc1)} V")
plt.show()