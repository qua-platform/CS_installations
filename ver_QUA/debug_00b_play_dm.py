# %%
# Single QUA script generated at 2025-03-06 02:48:33.056702
# QUA library version: 1.2.1a2

from qm.qua import *

with program() as prog:
    with infinite_loop_():
        play("trigger", "dm")
        wait(250, )


config = {
    "version": 1,
    "controllers": {
        "con1": {
            "type": "opx1000",
            "fems": {
                "5": {
                    "type": "LF",
                    "analog_outputs": {},
                    "digital_outputs": {
                        "1": {
                            "level": "LVTTL",
                        },
                    },
                    "analog_inputs": {},
                },
            },
        },
    },
    "elements": {
        "dm": {
            "digitalInputs": {
                "trigger": {
                    "port": ('con1', 5, 1),
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
            "type": "opx1000",
            "fems": {
                "5": {
                    "type": "LF",
                    "digital_outputs": {
                        "1": {
                            "shareable": False,
                            "inverted": False,
                            "level": "LVTTL",
                        },
                    },
                },
            },
        },
    },
    "oscillators": {},
    "elements": {
        "dm": {
            "digitalInputs": {
                "trigger": {
                    "delay": 0,
                    "buffer": 0,
                    "port": ('con1', 5, 1),
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



from qm import QuantumMachinesManager
qop_ip = "172.16.33.107"
cluster_name = "Cluster_1" 
qop_port = 9510
qmm = QuantumMachinesManager(host=qop_ip, port=qop_port, cluster_name=cluster_name)

# Open a quantum machine to execute the QUA program
qm = qmm.open_qm(config)
# Send the QUA program to the OPX, which compiles and executes it - Execute does not block python!
job = qm.execute(prog)


# %%
