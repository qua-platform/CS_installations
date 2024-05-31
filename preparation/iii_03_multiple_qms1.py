from qm.qua import *
from qm import QuantumMachinesManager
from qm import SimulationConfig
from configuration_OPX1000 import *
from qualang_tools.results import fetching_tool
import matplotlib.pyplot as plt
import numpy as np
import plotly.io as pio
pio.renderers.default='browser'


# get the config
config1 = {
        "version": 1,
        "controllers": {
            "con1": {
                "type": "opx1000",
                "fems": {
                    2: {
                        "type": "LF",
                        "analog_outputs": {
                            1: {"offset": 0.0, "sampling_rate": 1e9, "output_mode": "direct", "delay": 0},
                        },
                    },
                },
            },
        },
        "elements": {
            "lf_element_1": {
                "singleInput": {
                    "port": ("con1", 2, 1),
                },
                "intermediate_frequency": intermediate_frequency,
                "operations": {
                    "up": "up_pulse",
                    "down": "down_pulse",
                },
            },
        },
        "pulses": {
            "up_pulse": {
                "operation": "control",
                "length": square_up_len,
                "waveforms": {
                    "single": "up_wf",
                },
            },
            "down_pulse": {
                "operation": "control",
                "length": square_down_len,
                "waveforms": {
                    "single": "down_wf",
                },
            },
            "const_single_pulse": {
                "operation": "control",
                "length": const_len,
                "waveforms": {
                    "single": "const_wf",
                },
            },
        },
        "waveforms": {
            "zero_wf": {"type": "constant", "sample": 0.0},
            "const_wf": {"type": "constant", "sample": const_amp},
            "up_wf": {"type": "constant", "sample": square_amp},
            "down_wf": {"type": "constant", "sample": -square_amp},
        },
    }
config2 = {
        "version": 1,
        "controllers": {
            "con1": {
                "type": "opx1000",
                "fems": {
                    2: {
                        "type": "LF",
                        "analog_outputs": {
                            2: {"offset": 0.0, "sampling_rate": 1e9, "output_mode": "amplified", "delay": 0},
                            3: {"offset": 0.0, "sampling_rate": 1e9, "output_mode": "direct", "delay": 0},
                        },
                    },
                },
            },
        },
        "elements": {
            "lf_element_2": {
                "singleInput": {
                    "port": ("con1", 2, 2),
                },
                "intermediate_frequency": 0,
                "operations": {
                    "const": "const_single_pulse",
                },
            },
            "scope_trigger": {
                "singleInput": {
                    "port": ("con1", 2, 3),
                },
                "operations": {
                    "const": "const_single_pulse",
                },
            },
        },
        "pulses": {
            "const_single_pulse": {
                "operation": "control",
                "length": const_len,
                "waveforms": {
                    "single": "const_wf",
                },
            },
        },
        "waveforms": {
            "zero_wf": {"type": "constant", "sample": 0.0},
            "const_wf": {"type": "constant", "sample": const_amp},
        },
    }

###################
# The QUA program #
###################

with program() as qm1_prog:
    with infinite_loop_():
        play("up", "lf_element_1")
        play("down", "lf_element_1")

with program() as qm2_prog:
    with infinite_loop_():
        play("const", "lf_element_2")

#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(host=qop_ip, port=qop_port, cluster_name=cluster_name)

###########################
# Run or Simulate Program #
###########################
# Open a quantum machine to execute the QUA program
qm1 = qmm.open_qm(config1)
qm2 = qmm.open_qm(config2, close_other_machines=False)
# Send the QUA program to the OPX, which compiles and executes it - Execute does not block python!
job1 = qm1.execute(qm1_prog)
job2 = qm2.execute(qm2_prog)
# Get results from QUA program


