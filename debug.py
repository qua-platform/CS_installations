# Single QUA script generated at 2024-10-31 11:47:37.938695
# QUA library version: 1.2.1a1

from qm.qua import *

with program() as prog:
    v1 = declare(
        fixed,
    )
    v2 = declare(
        fixed,
    )
    v3 = declare(fixed, value=0.0)
    v4 = declare(fixed, value=0.0)
    v5 = declare(
        int,
    )
    pause()
    with infinite_loop_():
        assign(v5, IO1)
        with if_((v5 == 0)):
            assign(v3, IO2)
        with elif_((v5 == 1)):
            assign(v4, IO2)
        play("readout" * amp(v3), "readout_aom")
        play("control" * amp(v4), "control_aom")
        wait(100, "readout_aom")
        align()
        measure("readout", "SNSPD", None, integration.full("constant", v1, "out1"))
        measure("readout", "APD", None, integration.full("constant", v2, "out2"))
        r1 = declare_stream()
        save(v1, r1)
        r2 = declare_stream()
        save(v2, r2)
    with stream_processing():
        r1.buffer(1000).save("signal1")
        r2.buffer(1000).save("signal2")


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
                "6": {
                    "offset": 0.0,
                },
                "7": {
                    "offset": 0.0,
                },
                "8": {
                    "offset": 0.0,
                },
                "9": {
                    "offset": 0.0,
                },
                "10": {
                    "offset": 0.0,
                },
            },
            "digital_outputs": {
                "1": {},
                "2": {},
                "3": {},
                "4": {},
                "5": {},
                "6": {},
                "7": {},
                "8": {},
                "9": {},
            },
            "analog_inputs": {
                "1": {
                    "offset": 0.0,
                },
                "2": {
                    "offset": 0.0,
                },
            },
        },
    },
    "elements": {
        "readout_aom": {
            "singleInput": {
                "port": ("con1", 1),
            },
            "intermediate_frequency": 0,
            "operations": {
                "readout": "cw_readout_aom",
            },
            "digitalInputs": {
                "marker": {
                    "port": ("con1", 1),
                    "delay": 0,
                    "buffer": 0,
                },
            },
        },
        "control_aom": {
            "singleInput": {
                "port": ("con1", 2),
            },
            "intermediate_frequency": 0,
            "operations": {
                "control": "cw_control_aom",
            },
            "digitalInputs": {
                "marker": {
                    "port": ("con1", 2),
                    "delay": 0,
                    "buffer": 0,
                },
            },
        },
        "SNSPD": {
            "singleInput": {
                "port": ("con1", 1),
            },
            "operations": {
                "readout": "readout_pulse_snspd",
            },
            "outputs": {
                "out1": ("con1", 1),
            },
            "time_of_flight": 24,
            "smearing": 0,
        },
        "APD": {
            "singleInput": {
                "port": ("con1", 1),
            },
            "operations": {
                "readout": "readout_pulse_apd",
            },
            "outputs": {
                "out2": ("con1", 2),
            },
            "time_of_flight": 24,
            "smearing": 0,
        },
    },
    "pulses": {
        "cw_readout_aom": {
            "operation": "control",
            "length": 100,
            "waveforms": {
                "single": "cw_r",
            },
            "digital_marker": "ON",
        },
        "cw_control_aom": {
            "operation": "control",
            "length": 100,
            "waveforms": {
                "single": "cw_c_a",
            },
            "digital_marker": "ON",
        },
        "cw_control_eom": {
            "operation": "control",
            "length": 100,
            "waveforms": {
                "I": "cw_c_e",
                "Q": "zero_wf",
            },
            "digital_marker": "ON",
        },
        "cw_pulsed_laser_aom": {
            "operation": "control",
            "length": 100,
            "waveforms": {
                "single": "cw_pl_a",
            },
            "digital_marker": "ON",
        },
        "readout_pulse_snspd": {
            "operation": "measurement",
            "length": 1000,
            "waveforms": {
                "single": "zero_wf",
            },
            "integration_weights": {
                "constant": "constant_weights_snspd",
            },
            "digital_marker": "ON",
        },
        "readout_pulse_apd": {
            "operation": "measurement",
            "length": 1000,
            "waveforms": {
                "single": "zero_wf",
            },
            "integration_weights": {
                "constant": "constant_weights_apd",
            },
            "digital_marker": "ON",
        },
    },
    "waveforms": {
        "cw_r": {
            "type": "constant",
            "sample": 0.1,
        },
        "cw_c_a": {
            "type": "constant",
            "sample": 0.1,
        },
        "cw_c_e": {
            "type": "constant",
            "sample": 0.1,
        },
        "zero_wf": {
            "type": "constant",
            "sample": 0.0,
        },
        "cw_pl_a": {
            "type": "constant",
            "sample": 0.1,
        },
    },
    "digital_waveforms": {
        "ON": {
            "samples": [(1, 0)],
        },
        "OFF": {
            "samples": [(0, 0)],
        },
    },
    "integration_weights": {
        "constant_weights_snspd": {
            "cosine": [(1, 1000)],
            "sine": [(0.0, 1000)],
        },
        "constant_weights_apd": {
            "cosine": [(1, 1000)],
            "sine": [(0.0, 1000)],
        },
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
                "6": {
                    "offset": 0.0,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                    "crosstalk": {},
                },
                "7": {
                    "offset": 0.0,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                    "crosstalk": {},
                },
                "8": {
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
                "10": {
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
                "3": {
                    "shareable": False,
                    "inverted": False,
                    "level": "LVTTL",
                },
                "4": {
                    "shareable": False,
                    "inverted": False,
                    "level": "LVTTL",
                },
                "5": {
                    "shareable": False,
                    "inverted": False,
                    "level": "LVTTL",
                },
                "6": {
                    "shareable": False,
                    "inverted": False,
                    "level": "LVTTL",
                },
                "7": {
                    "shareable": False,
                    "inverted": False,
                    "level": "LVTTL",
                },
                "8": {
                    "shareable": False,
                    "inverted": False,
                    "level": "LVTTL",
                },
                "9": {
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
        "readout_aom": {
            "digitalInputs": {
                "marker": {
                    "delay": 0,
                    "buffer": 0,
                    "port": ("con1", 1, 1),
                },
            },
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "readout": "cw_readout_aom",
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
            "singleInput": {
                "port": ("con1", 1, 1),
            },
            "intermediate_frequency": 0.0,
        },
        "control_aom": {
            "digitalInputs": {
                "marker": {
                    "delay": 0,
                    "buffer": 0,
                    "port": ("con1", 1, 2),
                },
            },
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "control": "cw_control_aom",
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
            "singleInput": {
                "port": ("con1", 1, 2),
            },
            "intermediate_frequency": 0.0,
        },
        "SNSPD": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {
                "out1": ("con1", 1, 1),
            },
            "operations": {
                "readout": "readout_pulse_snspd",
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
            "singleInput": {
                "port": ("con1", 1, 1),
            },
            "smearing": 0,
            "time_of_flight": 24,
        },
        "APD": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {
                "out2": ("con1", 1, 2),
            },
            "operations": {
                "readout": "readout_pulse_apd",
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
            "singleInput": {
                "port": ("con1", 1, 1),
            },
            "smearing": 0,
            "time_of_flight": 24,
        },
    },
    "pulses": {
        "cw_readout_aom": {
            "length": 100,
            "waveforms": {
                "single": "cw_r",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "cw_control_aom": {
            "length": 100,
            "waveforms": {
                "single": "cw_c_a",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "cw_control_eom": {
            "length": 100,
            "waveforms": {
                "I": "cw_c_e",
                "Q": "zero_wf",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "cw_pulsed_laser_aom": {
            "length": 100,
            "waveforms": {
                "single": "cw_pl_a",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "readout_pulse_snspd": {
            "length": 1000,
            "waveforms": {
                "single": "zero_wf",
            },
            "integration_weights": {
                "constant": "constant_weights_snspd",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "readout_pulse_apd": {
            "length": 1000,
            "waveforms": {
                "single": "zero_wf",
            },
            "integration_weights": {
                "constant": "constant_weights_apd",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
    },
    "waveforms": {
        "cw_r": {
            "type": "constant",
            "sample": 0.1,
        },
        "cw_c_a": {
            "type": "constant",
            "sample": 0.1,
        },
        "cw_c_e": {
            "type": "constant",
            "sample": 0.1,
        },
        "zero_wf": {
            "type": "constant",
            "sample": 0.0,
        },
        "cw_pl_a": {
            "type": "constant",
            "sample": 0.1,
        },
    },
    "digital_waveforms": {
        "ON": {
            "samples": [(1, 0)],
        },
        "OFF": {
            "samples": [(0, 0)],
        },
    },
    "integration_weights": {
        "constant_weights_snspd": {
            "cosine": [(1.0, 1000)],
            "sine": [(0.0, 1000)],
        },
        "constant_weights_apd": {
            "cosine": [(1.0, 1000)],
            "sine": [(0.0, 1000)],
        },
    },
    "mixers": {},
}
