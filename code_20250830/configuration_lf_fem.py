# %%

import os
from pathlib import Path
import numpy as np
from qualang_tools.config.waveform_tools import drag_gaussian_pulse_waveforms, flattop_gaussian_waveform, drag_cosine_pulse_waveforms
from qualang_tools.units import unit


#######################
# AUXILIARY FUNCTIONS #
#######################
u = unit(coerce_to_integer=True)


######################
# Network parameters #
######################
qop_ip = "172.16.33.115"  # Write the QM router IP address
cluster_name = 'CS_4'  # Write your cluster_name if version >= QOP220
qop_port = None  # Write the QOP port if version < QOP220
octave_config = None


######################
#       Utils        #
######################

#############
# Save Path #
#############

# Path to save data
save_dir = Path(r"/workspaces/data")
save_dir.mkdir(exist_ok=True)

default_additional_files = {
    "configuration_lf_fem.py": "configuration_lf_fem.py",
}

#####################
# OPX configuration #
#####################

lffem_slot = 5

# MARK: QUBITS
#############################################
#                  Qubits                   #
#############################################
# CW pulse parameter
CONST_LEN = 100
CONST_AMP = 0.5 # 125 * u.mV
READOUT_AMP = 0.02
READOUT_LEN = 2000
TOF = 200

RL_CONSTANTS = {
    "rl1": {
        "RESONATORS": [f"q{i:02d}_rr" for i in range(1, 17, 1)],
        "TOF": TOF,
        "con": "con1",
        "fem": lffem_slot,
        "ao": 1,
        "ai": 2,
    },
    "rl2": {
        "RESONATORS": [f"q{i:02d}_rr" for i in range(17, 33, 1)],
        "TOF": TOF,
        "con": "con1",
        "fem": lffem_slot,
        "ao": 2,
        "ai": 2,
    },
}

RR_CONSTANTS = {
    "q01_rr": {
        "IF": 10 * u.MHz, 
        "amp": READOUT_AMP,
        "ao": 1,
        "core": "core_01",
    },
    "q02_rr": {
        "IF": 20 * u.MHz, 
        "amp": READOUT_AMP,
        "ao": 1,
        "core": "core_02",
    },
    "q03_rr": {
        "IF": 30 * u.MHz, 
        "amp": READOUT_AMP,
        "ao": 1,
        "core": "core_03",
    },
    "q04_rr": {
        "IF": 40 * u.MHz, 
        "amp": READOUT_AMP,
        "ao": 1,
        "core": "core_04",
    },
    "q05_rr": {
        "IF": 50 * u.MHz, 
        "amp": READOUT_AMP,
        "ao": 1,
        "core": "core_05",
    },
    "q06_rr": {
        "IF": 60 * u.MHz, 
        "amp": READOUT_AMP,
        "ao": 1,
        "core": "core_06",
    },
    "q07_rr": {
        "IF": 70 * u.MHz, 
        "amp": READOUT_AMP,
        "ao": 1,
        "core": "core_07",
    },
    "q08_rr": {
        "IF": 80 * u.MHz, 
        "amp": READOUT_AMP,
        "ao": 1,
        "core": "core_08",
    },
    "q09_rr": {
        "IF": 90 * u.MHz, 
        "amp": READOUT_AMP,
        "ao": 1,
        "core": "core_09",
    },
    "q10_rr": {
        "IF": 100 * u.MHz, 
        "amp": READOUT_AMP,
        "ao": 1,
        "core": "core_10",
    },
    "q11_rr": {
        "IF": 110 * u.MHz, 
        "amp": READOUT_AMP,
        "ao": 1,
        "core": "core_11",
    },
    "q12_rr": {
        "IF": 120 * u.MHz, 
        "amp": READOUT_AMP,
        "ao": 1,
        "core": "core_12",
    },
    "q13_rr": {
        "IF": 130 * u.MHz, 
        "amp": READOUT_AMP,
        "ao": 1,
        "core": "core_13",
    },
    "q14_rr": {
        "IF": 140 * u.MHz, 
        "amp": READOUT_AMP,
        "ao": 1,
        "core": "core_14",
    },
    "q15_rr": {
        "IF": 150 * u.MHz, 
        "amp": READOUT_AMP,
        "ao": 1,
        "core": "core_15",
    },
    "q16_rr": {
        "IF": 160 * u.MHz, 
        "amp": READOUT_AMP,
        "ao": 1,
        "core": "core_16",
    },
    "q17_rr": {
        "IF": 170 * u.MHz, 
        "amp": READOUT_AMP,
        "ao": 2,
        "core": "core_01",
    },
    "q18_rr": {
        "IF": 180 * u.MHz, 
        "amp": READOUT_AMP,
        "ao": 2,
        "core": "core_02",
    },
    "q19_rr": {
        "IF": 190 * u.MHz, 
        "amp": READOUT_AMP,
        "ao": 2,
        "core": "core_03",
    },
    "q20_rr": {
        "IF": 200 * u.MHz, 
        "amp": READOUT_AMP,
        "ao": 2,
        "core": "core_04",
    },
    "q21_rr": {
        "IF": 210 * u.MHz, 
        "amp": READOUT_AMP,
        "ao": 2,
        "core": "core_05",
    },
    "q22_rr": {
        "IF": 220 * u.MHz, 
        "amp": READOUT_AMP,
        "ao": 2,
        "core": "core_06",
    },
    "q23_rr": {
        "IF": 230 * u.MHz, 
        "amp": READOUT_AMP,
        "ao": 2,
        "core": "core_07",
    },
    "q24_rr": {
        "IF": 240 * u.MHz, 
        "amp": READOUT_AMP,
        "ao": 2,
        "core": "core_08",
    },
    "q25_rr": {
        "IF": 250 * u.MHz, 
        "amp": READOUT_AMP,
        "ao": 2,
        "core": "core_09",
    },
    "q26_rr": {
        "IF": 260 * u.MHz, 
        "amp": READOUT_AMP,
        "ao": 2,
        "core": "core_10",
    },
    "q27_rr": {
        "IF": 270 * u.MHz, 
        "amp": READOUT_AMP,
        "ao": 2,
        "core": "core_11",
    },
    "q28_rr": {
        "IF": 280 * u.MHz, 
        "amp": READOUT_AMP,
        "ao": 2,
        "core": "core_12",
    },
    "q29_rr": {
        "IF": 290 * u.MHz, 
        "amp": READOUT_AMP,
        "ao": 2,
        "core": "core_13",
    },
    "q30_rr": {
        "IF": 300 * u.MHz, 
        "amp": READOUT_AMP,
        "ao": 2,
        "core": "core_14",
    },
    "q31_rr": {
        "IF": 310 * u.MHz, 
        "amp": READOUT_AMP,
        "ao": 2,
        "core": "core_15",
    },
    "q32_rr": {
        "IF": 320 * u.MHz, 
        "amp": READOUT_AMP,
        "ao": 2,
        "core": "core_16",
    },
}

for k, v in RR_CONSTANTS.items():
    v.update({
        "TOF": RL_CONSTANTS["rl1"]["TOF"],
        "con": RL_CONSTANTS["rl1"]["con"],
        "fem": RL_CONSTANTS["rl1"]["fem"],
        "ai": RL_CONSTANTS["rl1"]["ai"],
    }) 

for rl in RL_CONSTANTS.keys():
    total_amp = 0
    for rr in RL_CONSTANTS[rl]["RESONATORS"]:
        total_amp += RR_CONSTANTS[rr]["amp"]
    assert total_amp < 0.5



# MARK: CONFIGURATION
#############################################
#                  Config                   #
#############################################

sampling_rate = 1e9
config = {
    "version": 1,
    "controllers": {
        "con1": {
            "type": "opx1000",
            "fems": {
                lffem_slot: {
                    "type": "LF",
                    "analog_outputs": {
                        # "offset": 0.0,
                        # # The "output_mode" can be used to tailor the max voltage and frequency bandwidth, i.e.,
                        # #   "direct":    1Vpp (-0.5V to 0.5V), 750MHz bandwidth (default)
                        # #   "amplified": 5Vpp (-2.5V to 2.5V), 330MHz bandwidth
                        # # Note, 'offset' takes absolute values, e.g., if in amplified mode and want to output 2.0 V, then set "offset": 2.0
                        # "output_mode": "direct",
                        # # The "sampling_rate" can be adjusted by using more FEM cores, i.e.,
                        # #   1 GS/s: uses one core per output (default)
                        # #   2 GS/s: uses two cores per output
                        # # NOTE: duration parameterization of arb. waveforms, sticky elements and chirping
                        # #       aren't yet supported in 2 GS/s.
                        # "sampling_rate": sampling_rate,
                        # # At 1 GS/s, use the "upsampling_mode" to optimize output for
                        # #   modulated pulses (optimized for modulated pulses):      "mw"    (default)
                        # #   unmodulated pulses (optimized for clean step response): "pulse"
                        # "upsampling_mode": "mw",
                        **{
                            v["ao"]: {
                                "offset": 0.0,
                                "output_mode": "direct",
                                "sampling_rate": sampling_rate,
                                "upsampling_mode": "mw",
                            } for k, v in RL_CONSTANTS.items()
                        }
                    },
                    "analog_inputs": {
                        **{
                            v["ai"]: {
                                "offset": 0.0,
                                "gain_db": 0,
                                "sampling_rate": sampling_rate,
                            } for k, v in RL_CONSTANTS.items()
                        },
                    },
                },
            },
        },
    },
    "elements": {
        **{rr: {
            "singleInput": {
                "port": (val["con"], val["fem"], val["ao"]),
            },
            "intermediate_frequency": val["IF"],
            "outputs": {
                "out1": (val["con"], val["fem"], val["ai"]),
            },
			'time_of_flight': val["TOF"],
            "operations": {
                "const": "const_pulse",
                "readout": f"readout_pulse_{rr}",
            },
            "core": val["core"]
        } for rr, val in RR_CONSTANTS.items()},
    }, 
    "pulses": {
        "const_pulse": {
            "operation": "control",
            "length": CONST_LEN,
            "waveforms": {
                "single": "const_wf",
            },
        },
        "zero_pulse": {
            "operation": "control",
            "length": 16,
            "waveforms": {
                "single": "zero_wf",
            },
        },
        **{
            f"readout_pulse_{rr}": {
                "operation": "measurement",
                "length": READOUT_LEN,
                "waveforms": {
                    "single": f"readout_wf_{rr}",
                },
                "integration_weights": {
                    "cos": f"cosine_weights_{rr}",
                    "sin": f"sine_weights_{rr}",
                },
                "digital_marker": "ON",
            }
            for rr, val in RR_CONSTANTS.items()
        },
    },
    "waveforms": {
        "const_wf": {"type": "constant", "sample": CONST_AMP},
        "zero_wf": {"type": "constant", "sample": 0.0},
        **{f"readout_wf_{k}": {"type": "constant", "sample": READOUT_AMP} for k, val in RR_CONSTANTS.items()},
    },
    "digital_waveforms": {
        "ON": {"samples": [(1, 0)]},
    },
    "integration_weights": {
        "cosine_weights": {
            "cosine": [(1.0, READOUT_LEN)],
            "sine": [(0.0, READOUT_LEN)],
        },
        "sine_weights": {
            "cosine": [(0.0, READOUT_LEN)],
            "sine": [(1.0, READOUT_LEN)],
        },
        "minus_sine_weights": {
            "cosine": [(0.0, READOUT_LEN)],
            "sine": [(-1.0, READOUT_LEN)],
        },
    },
}

# %%