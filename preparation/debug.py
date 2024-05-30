
# Single QUA script generated at 2024-05-29 08:33:20.389677
# QUA library version: 1.1.7.post15

from qm.qua import *

with program() as prog:
    v1 = declare(int, )
    with infinite_loop_():
        play("arbitrary", "lf_element_2")
        with for_(v1,4,(v1<=30),(v1+1)):
            play("arbitrary", "lf_element_1")


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
                "5": {
                    "offset": 0.0,
                },
            },
            "digital_outputs": {
                "1": {},
                "2": {},
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
        "lf_readout_element": {
            "singleInput": {
                "port": ('con1', 1),
            },
            "intermediate_frequency": 60000000,
            "operations": {
                "readout": "readout_pulse",
            },
            "outputs": {
                "out1": ('con1', 1),
                "out2": ('con1', 2),
            },
            "time_of_flight": 24,
            "smearing": 0,
        },
        "lf_readout_element_twin": {
            "singleInput": {
                "port": ('con1', 1),
            },
            "intermediate_frequency": 60000000,
            "operations": {
                "readout": "readout_pulse",
            },
            "outputs": {
                "out1": ('con1', 1),
                "out2": ('con1', 2),
            },
            "time_of_flight": 24,
            "smearing": 0,
        },
        "dc_readout_element": {
            "singleInput": {
                "port": ('con1', 1),
            },
            "operations": {
                "readout": "fake_readout_pulse",
            },
            "outputs": {
                "out1": ('con1', 1),
                "out2": ('con1', 2),
            },
            "time_of_flight": 24,
            "smearing": 0,
        },
        "dc_readout_element_twin": {
            "singleInput": {
                "port": ('con1', 1),
            },
            "operations": {
                "readout": "fake_readout_pulse",
            },
            "outputs": {
                "out1": ('con1', 1),
                "out2": ('con1', 2),
            },
            "time_of_flight": 24,
            "smearing": 0,
        },
        "lf_element_1": {
            "singleInput": {
                "port": ('con1', 1),
            },
            "intermediate_frequency": 0,
            "operations": {
                "const": "const_single_pulse",
                "arbitrary": "arbitrary_pulse",
                "up": "up_pulse",
                "down": "down_pulse",
            },
        },
        "lf_element_2": {
            "singleInput": {
                "port": ('con1', 2),
            },
            "intermediate_frequency": 0,
            "operations": {
                "const": "const_single_pulse",
                "arbitrary": "arbitrary_pulse",
                "up": "up_pulse",
                "down": "down_pulse",
            },
        },
        "mw_element_1": {
            "mixInputs": {
                "I": ('con1', 1),
                "Q": ('con1', 2),
                "lo_frequency": 7400000000,
                "mixer": "mixer_qubit",
            },
            "intermediate_frequency": 110000000,
            "operations": {
                "const": "const_pulse_mw",
            },
        },
        "qdac_trigger1": {
            "digitalInputs": {
                "trigger": {
                    "port": ('con1', 1),
                    "delay": 0,
                    "buffer": 0,
                },
            },
            "operations": {
                "trigger": "trigger_pulse",
            },
        },
        "qdac_trigger2": {
            "digitalInputs": {
                "trigger": {
                    "port": ('con1', 2),
                    "delay": 0,
                    "buffer": 0,
                },
            },
            "operations": {
                "trigger": "trigger_pulse",
            },
        },
    },
    "pulses": {
        "arbitrary_pulse": {
            "operation": "control",
            "length": 16,
            "waveforms": {
                "single": "arbitrary_wf",
            },
        },
        "up_pulse": {
            "operation": "control",
            "length": 500,
            "waveforms": {
                "single": "up_wf",
            },
        },
        "down_pulse": {
            "operation": "control",
            "length": 1000,
            "waveforms": {
                "single": "down_wf",
            },
        },
        "const_single_pulse": {
            "operation": "control",
            "length": 100,
            "waveforms": {
                "single": "const_wf",
            },
        },
        "trigger_pulse": {
            "operation": "control",
            "length": 1000,
            "digital_marker": "ON",
        },
        "const_pulse_mw": {
            "operation": "control",
            "length": 100,
            "waveforms": {
                "I": "const_wf",
                "Q": "zero_wf",
            },
        },
        "readout_pulse": {
            "operation": "measurement",
            "length": 5000,
            "waveforms": {
                "single": "readout_wf",
            },
            "integration_weights": {
                "cos": "cosine_weights",
                "sin": "sine_weights",
                "minus_sin": "minus_sine_weights",
            },
            "digital_marker": "ON",
        },
        "fake_readout_pulse": {
            "operation": "measurement",
            "length": 5000,
            "waveforms": {
                "single": "zero_wf",
            },
            "integration_weights": {
                "const": "const_weights",
            },
            "digital_marker": "ON",
        },
    },
    "waveforms": {
        "zero_wf": {
            "type": "constant",
            "sample": 0.0,
        },
        "const_wf": {
            "type": "constant",
            "sample": 0.25,
        },
        "up_wf": {
            "type": "constant",
            "sample": 0.25,
        },
        "down_wf": {
            "type": "constant",
            "sample": -0.25,
        },
        "readout_wf": {
            "type": "constant",
            "sample": 0.2,
        },
        "arbitrary_wf": {
            "type": "arbitrary",
            "samples": [0.0, 0.025848755604565593, 0.07116676503714674, 0.14035776686747115, 0.23119934151234656, 0.3313556721171544, 0.419279984480594] + [0.4711350915602544] * 2 + [0.419279984480594, 0.3313556721171544, 0.23119934151234656, 0.14035776686747115, 0.07116676503714674, 0.025848755604565593, 0.0],
        },
    },
    "digital_waveforms": {
        "ON": {
            "samples": [(1, 0)],
        },
    },
    "integration_weights": {
        "const_weights": {
            "cosine": [(1.0, 5000)],
            "sine": [(0.0, 5000)],
        },
        "cosine_weights": {
            "cosine": [(1.0, 5000)],
            "sine": [(0.0, 5000)],
        },
        "sine_weights": {
            "cosine": [(0.0, 5000)],
            "sine": [(1.0, 5000)],
        },
        "minus_sine_weights": {
            "cosine": [(0.0, 5000)],
            "sine": [(-1.0, 5000)],
        },
        "rotated_cosine_weights": {
            "cosine": [(1.0, 5000)],
            "sine": [(0.0, 5000)],
        },
        "rotated_sine_weights": {
            "cosine": [(-0.0, 5000)],
            "sine": [(1.0, 5000)],
        },
        "rotated_minus_sine_weights": {
            "cosine": [(0.0, 5000)],
            "sine": [(-1.0, 5000)],
        },
    },
    "mixers": {
        "mixer_qubit": [{'intermediate_frequency': 110000000, 'lo_frequency': 7400000000, 'correction': [1.0, 0.0, 0.0, 1.0]}],
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
                "5": {
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
                },
                "2": {
                    "offset": 0.0,
                    "gain_db": 0,
                    "shareable": False,
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
            },
            "digital_inputs": {},
        },
    },
    "oscillators": {},
    "elements": {
        "lf_readout_element": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {
                "out1": ('con1', 1, 1),
                "out2": ('con1', 1, 2),
            },
            "operations": {
                "readout": "readout_pulse",
            },
            "singleInput": {
                "port": ('con1', 1, 1),
            },
            "mixInputs": {
                "I": ('', 0),
                "Q": ('', 0),
                "mixer": "",
                "lo_frequency": 0.0,
            },
            "singleInputCollection": {
                "inputs": {},
            },
            "multipleInputs": {
                "inputs": {},
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "thread": "",
            "MWInput": {
                "port": ('', 0),
                "oscillator_frequency": 0.0,
            },
            "MWOutput": {
                "port": ('', 0),
                "oscillator_frequency": 0.0,
            },
            "smearing": 0,
            "time_of_flight": 24,
            "intermediate_frequency": 60000000.0,
        },
        "lf_readout_element_twin": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {
                "out1": ('con1', 1, 1),
                "out2": ('con1', 1, 2),
            },
            "operations": {
                "readout": "readout_pulse",
            },
            "singleInput": {
                "port": ('con1', 1, 1),
            },
            "mixInputs": {
                "I": ('', 0),
                "Q": ('', 0),
                "mixer": "",
                "lo_frequency": 0.0,
            },
            "singleInputCollection": {
                "inputs": {},
            },
            "multipleInputs": {
                "inputs": {},
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "thread": "",
            "MWInput": {
                "port": ('', 0),
                "oscillator_frequency": 0.0,
            },
            "MWOutput": {
                "port": ('', 0),
                "oscillator_frequency": 0.0,
            },
            "smearing": 0,
            "time_of_flight": 24,
            "intermediate_frequency": 60000000.0,
        },
        "dc_readout_element": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {
                "out1": ('con1', 1, 1),
                "out2": ('con1', 1, 2),
            },
            "operations": {
                "readout": "fake_readout_pulse",
            },
            "singleInput": {
                "port": ('con1', 1, 1),
            },
            "mixInputs": {
                "I": ('', 0),
                "Q": ('', 0),
                "mixer": "",
                "lo_frequency": 0.0,
            },
            "singleInputCollection": {
                "inputs": {},
            },
            "multipleInputs": {
                "inputs": {},
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "thread": "",
            "MWInput": {
                "port": ('', 0),
                "oscillator_frequency": 0.0,
            },
            "MWOutput": {
                "port": ('', 0),
                "oscillator_frequency": 0.0,
            },
            "smearing": 0,
            "time_of_flight": 24,
        },
        "dc_readout_element_twin": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {
                "out1": ('con1', 1, 1),
                "out2": ('con1', 1, 2),
            },
            "operations": {
                "readout": "fake_readout_pulse",
            },
            "singleInput": {
                "port": ('con1', 1, 1),
            },
            "mixInputs": {
                "I": ('', 0),
                "Q": ('', 0),
                "mixer": "",
                "lo_frequency": 0.0,
            },
            "singleInputCollection": {
                "inputs": {},
            },
            "multipleInputs": {
                "inputs": {},
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "thread": "",
            "MWInput": {
                "port": ('', 0),
                "oscillator_frequency": 0.0,
            },
            "MWOutput": {
                "port": ('', 0),
                "oscillator_frequency": 0.0,
            },
            "smearing": 0,
            "time_of_flight": 24,
        },
        "lf_element_1": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_single_pulse",
                "arbitrary": "arbitrary_pulse",
                "up": "up_pulse",
                "down": "down_pulse",
            },
            "singleInput": {
                "port": ('con1', 1, 1),
            },
            "mixInputs": {
                "I": ('', 0),
                "Q": ('', 0),
                "mixer": "",
                "lo_frequency": 0.0,
            },
            "singleInputCollection": {
                "inputs": {},
            },
            "multipleInputs": {
                "inputs": {},
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "thread": "",
            "MWInput": {
                "port": ('', 0),
                "oscillator_frequency": 0.0,
            },
            "MWOutput": {
                "port": ('', 0),
                "oscillator_frequency": 0.0,
            },
            "intermediate_frequency": 0,
        },
        "lf_element_2": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_single_pulse",
                "arbitrary": "arbitrary_pulse",
                "up": "up_pulse",
                "down": "down_pulse",
            },
            "singleInput": {
                "port": ('con1', 1, 2),
            },
            "mixInputs": {
                "I": ('', 0),
                "Q": ('', 0),
                "mixer": "",
                "lo_frequency": 0.0,
            },
            "singleInputCollection": {
                "inputs": {},
            },
            "multipleInputs": {
                "inputs": {},
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "thread": "",
            "MWInput": {
                "port": ('', 0),
                "oscillator_frequency": 0.0,
            },
            "MWOutput": {
                "port": ('', 0),
                "oscillator_frequency": 0.0,
            },
            "intermediate_frequency": 0,
        },
        "mw_element_1": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse_mw",
            },
            "singleInput": {
                "port": ('', 0),
            },
            "mixInputs": {
                "I": ('con1', 1, 1),
                "Q": ('con1', 1, 2),
                "mixer": "mixer_qubit",
                "lo_frequency": 7400000000.0,
            },
            "singleInputCollection": {
                "inputs": {},
            },
            "multipleInputs": {
                "inputs": {},
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "thread": "",
            "MWInput": {
                "port": ('', 0),
                "oscillator_frequency": 0.0,
            },
            "MWOutput": {
                "port": ('', 0),
                "oscillator_frequency": 0.0,
            },
            "intermediate_frequency": 110000000.0,
        },
        "qdac_trigger1": {
            "digitalInputs": {
                "trigger": {
                    "delay": 0,
                    "buffer": 0,
                    "port": ('con1', 1, 1),
                },
            },
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "trigger": "trigger_pulse",
            },
            "singleInput": {
                "port": ('', 0),
            },
            "mixInputs": {
                "I": ('', 0),
                "Q": ('', 0),
                "mixer": "",
                "lo_frequency": 0.0,
            },
            "singleInputCollection": {
                "inputs": {},
            },
            "multipleInputs": {
                "inputs": {},
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "thread": "",
            "MWInput": {
                "port": ('', 0),
                "oscillator_frequency": 0.0,
            },
            "MWOutput": {
                "port": ('', 0),
                "oscillator_frequency": 0.0,
            },
        },
        "qdac_trigger2": {
            "digitalInputs": {
                "trigger": {
                    "delay": 0,
                    "buffer": 0,
                    "port": ('con1', 1, 2),
                },
            },
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "trigger": "trigger_pulse",
            },
            "singleInput": {
                "port": ('', 0),
            },
            "mixInputs": {
                "I": ('', 0),
                "Q": ('', 0),
                "mixer": "",
                "lo_frequency": 0.0,
            },
            "singleInputCollection": {
                "inputs": {},
            },
            "multipleInputs": {
                "inputs": {},
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "thread": "",
            "MWInput": {
                "port": ('', 0),
                "oscillator_frequency": 0.0,
            },
            "MWOutput": {
                "port": ('', 0),
                "oscillator_frequency": 0.0,
            },
        },
    },
    "pulses": {
        "arbitrary_pulse": {
            "length": 16,
            "waveforms": {
                "single": "arbitrary_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "up_pulse": {
            "length": 500,
            "waveforms": {
                "single": "up_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "down_pulse": {
            "length": 1000,
            "waveforms": {
                "single": "down_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "const_single_pulse": {
            "length": 100,
            "waveforms": {
                "single": "const_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "trigger_pulse": {
            "length": 1000,
            "waveforms": {},
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "const_pulse_mw": {
            "length": 100,
            "waveforms": {
                "I": "const_wf",
                "Q": "zero_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "readout_pulse": {
            "length": 5000,
            "waveforms": {
                "single": "readout_wf",
            },
            "integration_weights": {
                "cos": "cosine_weights",
                "sin": "sine_weights",
                "minus_sin": "minus_sine_weights",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "fake_readout_pulse": {
            "length": 5000,
            "waveforms": {
                "single": "zero_wf",
            },
            "integration_weights": {
                "const": "const_weights",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
    },
    "waveforms": {
        "zero_wf": {
            "type": "constant",
            "sample": 0.0,
        },
        "const_wf": {
            "type": "constant",
            "sample": 0.25,
        },
        "up_wf": {
            "type": "constant",
            "sample": 0.25,
        },
        "down_wf": {
            "type": "constant",
            "sample": -0.25,
        },
        "readout_wf": {
            "type": "constant",
            "sample": 0.2,
        },
        "arbitrary_wf": {
            "type": "arbitrary",
            "samples": [0.0, 0.025848755604565593, 0.07116676503714674, 0.14035776686747115, 0.23119934151234656, 0.3313556721171544, 0.419279984480594] + [0.4711350915602544] * 2 + [0.419279984480594, 0.3313556721171544, 0.23119934151234656, 0.14035776686747115, 0.07116676503714674, 0.025848755604565593, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
    },
    "digital_waveforms": {
        "ON": {
            "samples": [(1, 0)],
        },
    },
    "integration_weights": {
        "const_weights": {
            "cosine": [(1.0, 5000)],
            "sine": [(0.0, 5000)],
        },
        "cosine_weights": {
            "cosine": [(1.0, 5000)],
            "sine": [(0.0, 5000)],
        },
        "sine_weights": {
            "cosine": [(0.0, 5000)],
            "sine": [(1.0, 5000)],
        },
        "minus_sine_weights": {
            "cosine": [(0.0, 5000)],
            "sine": [(-1.0, 5000)],
        },
        "rotated_cosine_weights": {
            "cosine": [(1.0, 5000)],
            "sine": [(0.0, 5000)],
        },
        "rotated_sine_weights": {
            "cosine": [(-0.0, 5000)],
            "sine": [(1.0, 5000)],
        },
        "rotated_minus_sine_weights": {
            "cosine": [(0.0, 5000)],
            "sine": [(-1.0, 5000)],
        },
    },
    "mixers": {
        "mixer_qubit": [{'intermediate_frequency': 110000000.0, 'lo_frequency': 7400000000.0, 'correction': (1.0, 0.0, 0.0, 1.0)}],
    },
}


