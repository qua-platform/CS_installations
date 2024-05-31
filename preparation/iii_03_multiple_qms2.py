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
config = get_config(sampling_rate=1e9)
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
                    "const": "const_single_pulse",
                    "arbitrary": "arbitrary_pulse",
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
                    "arbitrary": "arbitrary_pulse",
                    "up": "up_pulse",
                    "down": "down_pulse",
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
        },
    }
###################
# The QUA program #
###################

with program() as rb_prog:
    n = declare(int)

#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(host=qop_ip, port=qop_port, cluster_name=cluster_name)

###########################
# Run or Simulate Program #
###########################

simulate = True

if simulate:
    # Simulates the QUA program for the specified duration
    simulation_config = SimulationConfig(duration=100_000)  # In clock cycles = 4ns
    # Simulate blocks python until the simulation is done
    job = qmm.simulate(config, rb_prog, simulation_config)
    # Plot the simulated samples
    job.get_simulated_samples().con1.plot()
    # Get the waveform report
    samples = job.get_simulated_samples()
    waveform_report = job.get_simulated_waveform_report()
    waveform_report.create_plot(samples, plot=True, save_path=None)
else:
    # Open a quantum machine to execute the QUA program
    qm = qmm.open_qm(config)
    # Send the QUA program to the OPX, which compiles and executes it - Execute does not block python!
    job = qm.execute(rb_prog)
    # Get results from QUA program


