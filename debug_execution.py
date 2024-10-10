# %%
# Single QUA script generated at 2024-10-08 16:14:46.514267
# QUA library version: 1.2.1a1

from qm import QuantumMachinesManager
from qm.qua import *

with program() as prog:
    play("const", "Vg1")


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
            },
        },
    },
    "elements": {
        "Vg1": {
            "singleInput": {
                "port": ('con1', 1),
            },
            "intermediate_frequency": 5000000.0,
            "operations": {
                "const": "const_pulse",
            },
        },
        "Vg2": {
            "singleInput": {
                "port": ('con1', 2),
            },
            "intermediate_frequency": 10000000.0,
            "operations": {
                "const": "const_pulse",
            },
        },
    },
    "pulses": {
        "const_pulse": {
            "operation": "control",
            "length": 1000,
            "waveforms": {
                "single": "const_wf",
            },
        },
    },
    "waveforms": {
        "const_wf": {
            "type": "constant",
            "sample": 0.2,
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
            },
            "analog_inputs": {},
            "digital_outputs": {},
            "digital_inputs": {},
        },
    },
    "oscillators": {},
    "elements": {
        "Vg1": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
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
                "port": ('con1', 1, 1),
            },
            "intermediate_frequency": 5000000.0,
        },
        "Vg2": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
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
                "port": ('con1', 1, 2),
            },
            "intermediate_frequency": 10000000.0,
        },
    },
    "pulses": {
        "const_pulse": {
            "length": 1000,
            "waveforms": {
                "single": "const_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
    },
    "waveforms": {
        "const_wf": {
            "type": "constant",
            "sample": 0.2,
        },
    },
    "digital_waveforms": {},
    "integration_weights": {},
    "mixers": {},
}


from set_octave import OctaveUnit, octave_declaration

qop_ip = "172.16.33.101" # Write the QM router IP address
cluster_name = "Cluster_81" # Write the QM router IP address
qop_port = None  # Write the QOP port if version < QOP220
# octave_1 = OctaveUnit("octave1", qop_ip, port=11232, con="con1")
# octaves = [octave_1]
# octave_config = octave_declaration(octaves)
octave_config = None 

qmm = QuantumMachinesManager(host=qop_ip, port=qop_port, cluster_name=cluster_name, octave=octave_config, log_level="DEBUG")
# Open the quantum machine
qm = qmm.open_qm(config)
# Send the QUA program to the OPX, which compiles and executes it
job = qm.execute(prog)


# %%
