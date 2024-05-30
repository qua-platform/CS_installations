from qm.qua import *
from qm import QuantumMachinesManager
from qm import SimulationConfig
import matplotlib.pyplot as plt
import numpy as np

qop_ip = "172.16.32.102"  # Write the QM router IP address
cluster_name = "Cluster_2"  # Write your cluster_name if version >= QOP220
port = 9510

sinus_wave_duration = 100
readout_len = 500
sinus_wave = np.sin(2 * np.pi * readout_len)
ports = [1,2,3,4,5,6,7,8]
delays = [[7, 7, 7, 7, 7, 7, 7, 7], [4, 4, 4, 4, 4, 4, 4, 4]]

config = {
    "version": 1,
    "controllers": {
        "con1": {
            "type": "opx1000",
            "fems": {
                1: {
                    "type": "MW",
                    "analog_inputs": {},
                    "analog_outputs": {
                        i: {
                            "sampling_rate": 1e9,
                            "band": 1,
                            "full_scale_power_dbm": -6,
                            "delay": delays[0][i-1]
                        } 
                        for i in ports
                    },
                },
                2: {
                    "type": "MW",
                    "analog_inputs": {},
                    "analog_outputs": {
                        i: {
                            "sampling_rate": 1e9,
                            "band": 1,
                            "full_scale_power_dbm": -6,
                            "delay": delays[1][i-1]
                        } 
                        for i in ports
                    },
                },
                3: {
                    "type": "LF",
                    "analog_outputs": {
                        ** {i: {"offset": 0.0, "sampling_rate": 1e9, "output_mode": "amplified",
                                 "upsampling_mode": "pulse", "delay": 0} for i in ports},
                    },
                },
            },
        },
    },
    "elements": {
        **{f"flux_{i}": {
            "singleInput": {
                "port": ("con1", 3, i),
            },
            "intermediate_frequency": 100e6,
            "operations": {
                "cw": "cw_pulse",
            },
        } for i in ports},

        **{f"qubit_{i}": {
            "MWInput": {
                "port": ("con1", 1, i),
                "oscillator_frequency": 1000e6,  # + 50e6*i,  # in Hz LO
            },
            "intermediate_frequency": 50e6,  # 5e6+5e6*i,
            "operations": {
                "play_I": "pulse1",
                "play_Q": "pulse2",
            },
        }
        for i in ports},
        **{f"qubit_{i}_fem2": {
            "MWInput": {
                "port": ("con1", 2, i),
                "oscillator_frequency": 1000e6,
            },
            "intermediate_frequency": 50e6,
            "operations": {
                "play_I": "pulse1",
                "play_Q": "pulse2",
            },
        }
        for i in ports},
    },
    "pulses": {
        "pulse1": {
            "length": 5000,
            "operation": "control",
            "waveforms": {
                "I": "const_wf",
                "Q": "zero_wf",
            },
        },
        "pulse2": {
            "length": 5000,
            "operation": "control",
            "waveforms": {
                "I": "zero_wf",
                "Q": "const_wf",
            },
        },
        "cw_pulse": {
            "operation": "control",
            "length": 5000,
            "waveforms": {
                "single": "const_wf",
            },
        },
    },
    "waveforms": {
        "const_wf": {"sample": 0.499, "type": "constant"},
        "zero_wf": {"sample": 0.0, "type": "constant"},
    },
}

###################
# The QUA program #
###################
with program() as hello_QUA:
    with infinite_loop_():
      for i in ports:
          play("play_I", f"qubit_{i}")
          play("play_I", f"qubit_{i}_fem2")
          play("cw", f"flux_{i}")


#####################################
#  Open Communication with the QOP  #
#####################################
qmm = QuantumMachinesManager(host=qop_ip, port = port, cluster_name=cluster_name)

###########################
# Run or Simulate Program #
###########################

# run on real HW
qm = qmm.open_qm(config)
job = qm.execute(hello_QUA)