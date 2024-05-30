
# Single QUA script generated at 2024-05-30 11:35:53.292421
# QUA library version: 1.1.7.post15

from qm.qua import *

with program() as prog:
    v1 = declare(fixed, )
    v2 = declare(fixed, )
    v3 = declare(int, )
    v4 = declare(int, )
    with for_(v3,0,(v3<10),(v3+1)):
        play("const", "lf_element_2")
        with for_(v4,-900000000,(v4<=899900000),(v4+100000)):
            update_frequency("lf_readout_element", v4, "Hz", False)
            play("const"*amp(1), "lf_element_1")
            align()
            measure("readout"*amp(1), "lf_readout_element", None, demod.full("cos", v1, "out1"), demod.full("sin", v2, "out1"))
            r2 = declare_stream()
            save(v1, r2)
            r3 = declare_stream()
            save(v2, r3)
            wait(250, )
        r1 = declare_stream()
        save(v3, r1)
    with stream_processing():
        r2.buffer(18000).average().save("I")
        r3.buffer(18000).average().save("Q")
        r1.save("iteration")


config = {
    "version": 1,
    "controllers": {
        "con1": {
            "type": "opx1000",
            "fems": {
                "2": {
                    "type": "MW",
                    "analog_outputs": {
                        "1": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": -11,
                            "band": 2,
                            "delay": 0,
                        },
                    },
                },
                "3": {
                    "type": "LF",
                    "analog_outputs": {
                        "1": {
                            "offset": 0.0,
                            "sampling_rate": 1000000000.0,
                            "output_mode": "direct",
                            "upsampling_mode": "mw",
                            "delay": 0,
                        },
                        "2": {
                            "offset": 0.0,
                            "sampling_rate": 1000000000.0,
                            "output_mode": "amplified",
                            "upsampling_mode": "mw",
                            "delay": 0,
                        },
                        "3": {
                            "offset": 0.0,
                            "sampling_rate": 1000000000.0,
                            "output_mode": "direct",
                            "upsampling_mode": "mw",
                            "delay": 0,
                        },
                        "4": {
                            "offset": 0.0,
                            "sampling_rate": 1000000000.0,
                            "output_mode": "direct",
                            "upsampling_mode": "mw",
                            "delay": 0,
                        },
                    },
                    "analog_inputs": {
                        "1": {
                            "offset": 0.000358,
                            "sampling_rate": 1000000000,
                            "gain_db": 0,
                        },
                        "2": {
                            "offset": -0.00712,
                            "sampling_rate": 1000000000,
                            "gain_db": 0,
                        },
                    },
                },
            },
        },
    },
    "elements": {
        "mw_element_1": {
            "MWInput": {
                "port": ('con1', 2, 1),
                "oscillator_frequency": 5000000000.0,
            },
            "intermediate_frequency": 50000000.0,
            "operations": {
                "const": "const_pulse_mw",
            },
        },
        "lf_element_1": {
            "singleInput": {
                "port": ('con1', 3, 1),
            },
            "intermediate_frequency": 3000000,
            "operations": {
                "const": "const_single_pulse",
                "arbitrary": "arbitrary_pulse",
                "up": "up_pulse",
                "down": "down_pulse",
            },
        },
        "lf_element_2": {
            "singleInput": {
                "port": ('con1', 3, 2),
            },
            "intermediate_frequency": 0,
            "operations": {
                "const": "const_single_pulse",
                "arbitrary": "arbitrary_pulse",
                "up": "up_pulse",
                "down": "down_pulse",
            },
        },
        "lf_readout_element": {
            "singleInput": {
                "port": ('con1', 3, 3),
            },
            "intermediate_frequency": 3000000,
            "operations": {
                "readout": "readout_pulse",
            },
            "outputs": {
                "out1": ('con1', 3, 1),
            },
            "time_of_flight": 144,
            "smearing": 0,
        },
        "lf_readout_element_twin": {
            "singleInput": {
                "port": ('con1', 3, 3),
            },
            "intermediate_frequency": 3000000,
            "operations": {
                "readout": "readout_pulse",
            },
            "outputs": {
                "out1": ('con1', 3, 1),
            },
            "time_of_flight": 144,
            "smearing": 0,
        },
        "dc_readout_element": {
            "singleInput": {
                "port": ('con1', 3, 4),
            },
            "operations": {
                "readout": "dc_readout_pulse",
            },
            "outputs": {
                "out1": ('con1', 3, 1),
                "out2": ('con1', 3, 2),
            },
            "time_of_flight": 144,
            "smearing": 0,
        },
        "dc_readout_element_twin": {
            "singleInput": {
                "port": ('con1', 3, 4),
            },
            "operations": {
                "readout": "dc_readout_pulse",
            },
            "outputs": {
                "out1": ('con1', 3, 1),
                "out2": ('con1', 3, 2),
            },
            "time_of_flight": 144,
            "smearing": 0,
        },
    },
    "pulses": {
        "arbitrary_pulse": {
            "operation": "control",
            "length": 40,
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
            "length": 500,
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
                "rotated_cos": "rotated_cosine_weights",
                "rotated_sin": "rotated_sine_weights",
                "rotated_minus_sin": "rotated_minus_sine_weights",
            },
            "digital_marker": "ON",
        },
        "dc_readout_pulse": {
            "operation": "measurement",
            "length": 5000,
            "waveforms": {
                "single": "dc_readout_wf",
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
            "sample": 0.2,
        },
        "up_wf": {
            "type": "constant",
            "sample": 0.5,
        },
        "down_wf": {
            "type": "constant",
            "sample": -0.5,
        },
        "readout_wf": {
            "type": "constant",
            "sample": 0.2,
        },
        "dc_readout_wf": {
            "type": "constant",
            "sample": 0.2,
        },
        "arbitrary_wf": {
            "type": "arbitrary",
            "samples": [0.0, 0.00886018777329083, 0.020063252492694746, 0.03396633901599479, 0.05089424368285021, 0.0711066656181945, 0.09476161195079541, 0.12187770290189255, 0.15229900088574033, 0.1856665964262655, 0.22140136158049029, 0.25870190167400714, 0.2965607372272688, 0.333800159669259, 0.3691271596450651, 0.401204555487245, 0.4287332529952062, 0.45053877476225934, 0.46565410929362133] + [0.4733907653684089] * 2 + [0.46565410929362133, 0.45053877476225934, 0.4287332529952062, 0.401204555487245, 0.3691271596450651, 0.333800159669259, 0.2965607372272688, 0.25870190167400714, 0.22140136158049029, 0.1856665964262655, 0.15229900088574033, 0.12187770290189255, 0.09476161195079541, 0.0711066656181945, 0.05089424368285021, 0.03396633901599479, 0.020063252492694746, 0.00886018777329083, 0.0],
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
}

loaded_config = {
    "version": 1,
    "controllers": {
        "con1": {
            "type": "opx1000",
            "fems": {
                "2": {
                    "type": "MW",
                    "analog_outputs": {
                        "1": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": -11,
                            "band": 2,
                            "delay": 0,
                            "shareable": False,
                        },
                    },
                },
                "3": {
                    "type": "LF",
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
                            "output_mode": "direct",
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "mw",
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
                            "output_mode": "amplified",
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "mw",
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
                            "output_mode": "direct",
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "mw",
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
                            "output_mode": "direct",
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "mw",
                        },
                    },
                    "analog_inputs": {
                        "1": {
                            "offset": 0.000358,
                            "gain_db": 0,
                            "shareable": False,
                        },
                        "2": {
                            "offset": -0.00712,
                            "gain_db": 0,
                            "shareable": False,
                        },
                    },
                },
            },
        },
    },
    "oscillators": {},
    "elements": {
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
                "port": ('con1', 2, 1),
                "oscillator_frequency": 5000000000.0,
            },
            "MWOutput": {
                "port": ('', 0),
                "oscillator_frequency": 0.0,
            },
            "intermediate_frequency": 50000000.0,
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
                "port": ('con1', 3, 1),
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
            "intermediate_frequency": 3000000.0,
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
                "port": ('con1', 3, 2),
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
        "lf_readout_element": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {
                "out1": ('con1', 3, 1),
            },
            "operations": {
                "readout": "readout_pulse",
            },
            "singleInput": {
                "port": ('con1', 3, 3),
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
            "time_of_flight": 144,
            "intermediate_frequency": 3000000.0,
        },
        "lf_readout_element_twin": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {
                "out1": ('con1', 3, 1),
            },
            "operations": {
                "readout": "readout_pulse",
            },
            "singleInput": {
                "port": ('con1', 3, 3),
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
            "time_of_flight": 144,
            "intermediate_frequency": 3000000.0,
        },
        "dc_readout_element": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {
                "out1": ('con1', 3, 1),
                "out2": ('con1', 3, 2),
            },
            "operations": {
                "readout": "dc_readout_pulse",
            },
            "singleInput": {
                "port": ('con1', 3, 4),
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
            "time_of_flight": 144,
        },
        "dc_readout_element_twin": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {
                "out1": ('con1', 3, 1),
                "out2": ('con1', 3, 2),
            },
            "operations": {
                "readout": "dc_readout_pulse",
            },
            "singleInput": {
                "port": ('con1', 3, 4),
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
            "time_of_flight": 144,
        },
    },
    "pulses": {
        "arbitrary_pulse": {
            "length": 40,
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
            "length": 500,
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
                "rotated_cos": "rotated_cosine_weights",
                "rotated_sin": "rotated_sine_weights",
                "rotated_minus_sin": "rotated_minus_sine_weights",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "dc_readout_pulse": {
            "length": 5000,
            "waveforms": {
                "single": "dc_readout_wf",
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
            "sample": 0.2,
        },
        "up_wf": {
            "type": "constant",
            "sample": 0.5,
        },
        "down_wf": {
            "type": "constant",
            "sample": -0.5,
        },
        "readout_wf": {
            "type": "constant",
            "sample": 0.2,
        },
        "dc_readout_wf": {
            "type": "constant",
            "sample": 0.2,
        },
        "arbitrary_wf": {
            "type": "arbitrary",
            "samples": [0.0, 0.00886018777329083, 0.020063252492694746, 0.03396633901599479, 0.05089424368285021, 0.0711066656181945, 0.09476161195079541, 0.12187770290189255, 0.15229900088574033, 0.1856665964262655, 0.22140136158049029, 0.25870190167400714, 0.2965607372272688, 0.333800159669259, 0.3691271596450651, 0.401204555487245, 0.4287332529952062, 0.45053877476225934, 0.46565410929362133] + [0.4733907653684089] * 2 + [0.46565410929362133, 0.45053877476225934, 0.4287332529952062, 0.401204555487245, 0.3691271596450651, 0.333800159669259, 0.2965607372272688, 0.25870190167400714, 0.22140136158049029, 0.1856665964262655, 0.15229900088574033, 0.12187770290189255, 0.09476161195079541, 0.0711066656181945, 0.05089424368285021, 0.03396633901599479, 0.020063252492694746, 0.00886018777329083, 0.0],
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
    "mixers": {},
}


