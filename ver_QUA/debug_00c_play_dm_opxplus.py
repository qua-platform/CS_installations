
# Single QUA script generated at 2025-03-06 16:31:10.470185
# QUA library version: 1.2.1a2

from qm.qua import *

with program() as prog:
    with infinite_loop_():
        play("trigger", "dm1")
        play("trigger", "dm2")
        play("trigger", "dm3")
        play("trigger", "dm4")
        play("trigger", "dm5")
        play("trigger", "dm6")
        play("trigger", "dm7")
        play("trigger", "dm8")
        wait(250, )


config = {
    "version": 1,
    "controllers": {
        "con1": {
            "analog_outputs": {},
            "digital_outputs": {
                "1": {},
                "2": {},
                "3": {},
                "4": {},
                "5": {},
                "6": {},
                "7": {},
                "8": {},
            },
            "analog_inputs": {},
        },
    },
    "elements": {
        "dm1": {
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
        "dm2": {
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
        "dm3": {
            "digitalInputs": {
                "trigger": {
                    "port": ('con1', 3),
                    "delay": 0,
                    "buffer": 0,
                },
            },
            "operations": {
                "trigger": "trigger_pulse",
            },
        },
        "dm4": {
            "digitalInputs": {
                "trigger": {
                    "port": ('con1', 4),
                    "delay": 0,
                    "buffer": 0,
                },
            },
            "operations": {
                "trigger": "trigger_pulse",
            },
        },
        "dm5": {
            "digitalInputs": {
                "trigger": {
                    "port": ('con1', 5),
                    "delay": 0,
                    "buffer": 0,
                },
            },
            "operations": {
                "trigger": "trigger_pulse",
            },
        },
        "dm6": {
            "digitalInputs": {
                "trigger": {
                    "port": ('con1', 6),
                    "delay": 0,
                    "buffer": 0,
                },
            },
            "operations": {
                "trigger": "trigger_pulse",
            },
        },
        "dm7": {
            "digitalInputs": {
                "trigger": {
                    "port": ('con1', 7),
                    "delay": 0,
                    "buffer": 0,
                },
            },
            "operations": {
                "trigger": "trigger_pulse",
            },
        },
        "dm8": {
            "digitalInputs": {
                "trigger": {
                    "port": ('con1', 8),
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
        "trigger_pulse": {
            "operation": "control",
            "length": 1000,
            "digital_marker": "ON",
        },
    },
    "digital_waveforms": {
        "ON": {
            "samples": [(1, 0)],
        },
    },
}

loaded_config = {
    "version": 1,
    "controllers": {
        "con1": {
            "type": "opx1",
            "analog_outputs": {},
            "analog_inputs": {},
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
            },
            "digital_inputs": {},
        },
    },
    "oscillators": {},
    "elements": {
        "dm1": {
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
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "thread": "",
        },
        "dm2": {
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
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "thread": "",
        },
        "dm3": {
            "digitalInputs": {
                "trigger": {
                    "delay": 0,
                    "buffer": 0,
                    "port": ('con1', 1, 3),
                },
            },
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "trigger": "trigger_pulse",
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
        },
        "dm4": {
            "digitalInputs": {
                "trigger": {
                    "delay": 0,
                    "buffer": 0,
                    "port": ('con1', 1, 4),
                },
            },
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "trigger": "trigger_pulse",
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
        },
        "dm5": {
            "digitalInputs": {
                "trigger": {
                    "delay": 0,
                    "buffer": 0,
                    "port": ('con1', 1, 5),
                },
            },
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "trigger": "trigger_pulse",
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
        },
        "dm6": {
            "digitalInputs": {
                "trigger": {
                    "delay": 0,
                    "buffer": 0,
                    "port": ('con1', 1, 6),
                },
            },
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "trigger": "trigger_pulse",
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
        },
        "dm7": {
            "digitalInputs": {
                "trigger": {
                    "delay": 0,
                    "buffer": 0,
                    "port": ('con1', 1, 7),
                },
            },
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "trigger": "trigger_pulse",
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
        },
        "dm8": {
            "digitalInputs": {
                "trigger": {
                    "delay": 0,
                    "buffer": 0,
                    "port": ('con1', 1, 8),
                },
            },
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "trigger": "trigger_pulse",
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
        },
    },
    "pulses": {
        "trigger_pulse": {
            "length": 1000,
            "waveforms": {},
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
    },
    "waveforms": {},
    "digital_waveforms": {
        "ON": {
            "samples": [(1, 0)],
        },
    },
    "integration_weights": {},
    "mixers": {},
}


