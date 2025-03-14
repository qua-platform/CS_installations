
# Single QUA script generated at 2025-03-13 16:30:30.697816
# QUA library version: 1.2.2a3

from qm import CompilerOptionArguments
from qm.qua import *

with program() as prog:
    v1 = declare(int, )
    with for_(v1,0,(v1<10),(v1+1)):
        atr_r1 = declare_stream(adc_trace=True)
        measure("single", "rr_test6", adc_stream=atr_r1)
        measure("single", "rr_test7", adc_stream=atr_r1)
        measure("single", "rr_test8", adc_stream=atr_r1)
        wait(250, "rr_test6", "rr_test7", "rr_test8")
    with stream_processing():
        atr_r1.input1().average().save("adc1")
        atr_r1.input2().average().save("adc2")
        atr_r1.input1().save("adc1_single_run")
        atr_r1.input2().save("adc2_single_run")


config = {
    "version": 1,
    "controllers": {
        "con1": {
            "type": "opx1000",
            "fems": {
                "5": {
                    "type": "LF",
                    "analog_outputs": {
                        "1": {
                            "offset": 0.0,
                            "output_mode": "direct",
                            "sampling_rate": 2000000000.0,
                        },
                        "2": {
                            "offset": 0.0,
                            "output_mode": "direct",
                            "sampling_rate": 2000000000.0,
                        },
                        "3": {
                            "offset": 0.0,
                            "output_mode": "direct",
                            "sampling_rate": 2000000000.0,
                        },
                        "4": {
                            "offset": 0.0,
                            "output_mode": "direct",
                            "sampling_rate": 2000000000.0,
                        },
                        "5": {
                            "offset": 0.0,
                            "output_mode": "direct",
                            "sampling_rate": 2000000000.0,
                        },
                        "6": {
                            "offset": 0.0,
                            "output_mode": "direct",
                            "sampling_rate": 2000000000.0,
                        },
                        "7": {
                            "offset": 0.0,
                            "output_mode": "direct",
                            "sampling_rate": 2000000000.0,
                        },
                        "8": {
                            "offset": 0.0,
                            "output_mode": "direct",
                            "sampling_rate": 2000000000.0,
                        },
                    },
                    "digital_outputs": {},
                    "analog_inputs": {
                        "1": {
                            "offset": 0.0,
                            "gain_db": 0,
                            "sampling_rate": 2000000000.0,
                        },
                        "2": {
                            "offset": 0.0,
                            "gain_db": 0,
                            "sampling_rate": 2000000000.0,
                        },
                    },
                },
            },
        },
    },
    "elements": {
        "rr_test5": {
            "singleInput": {
                "port": ('con1', 5, 5),
            },
            "intermediate_frequency": 750000000,
            "operations": {
                "single": "single_pulse",
            },
            "outputs": {
                "out1": ('con1', 5, 1),
                "out2": ('con1', 5, 2),
            },
            "time_of_flight": 160,
            "smearing": 0,
        },
        "rr_test6": {
            "singleInput": {
                "port": ('con1', 5, 6),
            },
            "intermediate_frequency": 750000000,
            "operations": {
                "single": "single_pulse",
            },
            "outputs": {
                "out1": ('con1', 5, 1),
                "out2": ('con1', 5, 2),
            },
            "time_of_flight": 160,
            "smearing": 0,
        },
        "rr_test7": {
            "singleInput": {
                "port": ('con1', 5, 7),
            },
            "intermediate_frequency": 750000000,
            "operations": {
                "single": "single_pulse",
            },
            "outputs": {
                "out1": ('con1', 5, 1),
                "out2": ('con1', 5, 2),
            },
            "time_of_flight": 160,
            "smearing": 0,
        },
        "rr_test8": {
            "singleInput": {
                "port": ('con1', 5, 8),
            },
            "intermediate_frequency": 750000000,
            "operations": {
                "single": "single_pulse",
            },
            "outputs": {
                "out1": ('con1', 5, 1),
                "out2": ('con1', 5, 2),
            },
            "time_of_flight": 160,
            "smearing": 0,
        },
    },
    "pulses": {
        "single_pulse": {
            "operation": "measurement",
            "length": 100,
            "waveforms": {
                "single": "single_wf",
            },
            "integration_weights": {
                "cos": "cosine_weights",
                "sin": "sine_weights",
                "minus_sin": "minus_sine_weights",
            },
            "digital_marker": "ON",
        },
    },
    "waveforms": {
        "single_wf": {
            "type": "constant",
            "sample": 0.25,
        },
    },
    "digital_waveforms": {
        "ON": {
            "samples": [(1, 0)],
        },
    },
    "integration_weights": {
        "cosine_weights": {
            "cosine": [(1.0, 100)],
            "sine": [(0.0, 100)],
        },
        "sine_weights": {
            "cosine": [(0.0, 100)],
            "sine": [(1.0, 100)],
        },
        "minus_sine_weights": {
            "cosine": [(0.0, 100)],
            "sine": [(-1.0, 100)],
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
                    "analog_outputs": {
                        "1": {
                            "offset": 0.0,
                            "delay": 0,
                            "shareable": False,
                            "filter": {
                                "feedforward": [],
                            },
                            "crosstalk": {},
                            "output_mode": "direct",
                            "sampling_rate": 2000000000.0,
                        },
                        "2": {
                            "offset": 0.0,
                            "delay": 0,
                            "shareable": False,
                            "filter": {
                                "feedforward": [],
                            },
                            "crosstalk": {},
                            "output_mode": "direct",
                            "sampling_rate": 2000000000.0,
                        },
                        "3": {
                            "offset": 0.0,
                            "delay": 0,
                            "shareable": False,
                            "filter": {
                                "feedforward": [],
                            },
                            "crosstalk": {},
                            "output_mode": "direct",
                            "sampling_rate": 2000000000.0,
                        },
                        "4": {
                            "offset": 0.0,
                            "delay": 0,
                            "shareable": False,
                            "filter": {
                                "feedforward": [],
                            },
                            "crosstalk": {},
                            "output_mode": "direct",
                            "sampling_rate": 2000000000.0,
                        },
                        "5": {
                            "offset": 0.0,
                            "delay": 0,
                            "shareable": False,
                            "filter": {
                                "feedforward": [],
                            },
                            "crosstalk": {},
                            "output_mode": "direct",
                            "sampling_rate": 2000000000.0,
                        },
                        "6": {
                            "offset": 0.0,
                            "delay": 0,
                            "shareable": False,
                            "filter": {
                                "feedforward": [],
                            },
                            "crosstalk": {},
                            "output_mode": "direct",
                            "sampling_rate": 2000000000.0,
                        },
                        "7": {
                            "offset": 0.0,
                            "delay": 0,
                            "shareable": False,
                            "filter": {
                                "feedforward": [],
                            },
                            "crosstalk": {},
                            "output_mode": "direct",
                            "sampling_rate": 2000000000.0,
                        },
                        "8": {
                            "offset": 0.0,
                            "delay": 0,
                            "shareable": False,
                            "filter": {
                                "feedforward": [],
                            },
                            "crosstalk": {},
                            "output_mode": "direct",
                            "sampling_rate": 2000000000.0,
                        },
                    },
                    "analog_inputs": {
                        "1": {
                            "offset": 0.0,
                            "gain_db": 0,
                            "shareable": False,
                            "sampling_rate": 2000000000.0,
                        },
                        "2": {
                            "offset": 0.0,
                            "gain_db": 0,
                            "shareable": False,
                            "sampling_rate": 2000000000.0,
                        },
                    },
                },
            },
        },
    },
    "oscillators": {},
    "elements": {
        "rr_test5": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {
                "out1": ('con1', 5, 1),
                "out2": ('con1', 5, 2),
            },
            "operations": {
                "single": "single_pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "singleInput": {
                "port": ('con1', 5, 5),
            },
            "smearing": 0,
            "time_of_flight": 160,
            "intermediate_frequency": 750000000.0,
        },
        "rr_test6": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {
                "out1": ('con1', 5, 1),
                "out2": ('con1', 5, 2),
            },
            "operations": {
                "single": "single_pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "singleInput": {
                "port": ('con1', 5, 6),
            },
            "smearing": 0,
            "time_of_flight": 160,
            "intermediate_frequency": 750000000.0,
        },
        "rr_test7": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {
                "out1": ('con1', 5, 1),
                "out2": ('con1', 5, 2),
            },
            "operations": {
                "single": "single_pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "singleInput": {
                "port": ('con1', 5, 7),
            },
            "smearing": 0,
            "time_of_flight": 160,
            "intermediate_frequency": 750000000.0,
        },
        "rr_test8": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {
                "out1": ('con1', 5, 1),
                "out2": ('con1', 5, 2),
            },
            "operations": {
                "single": "single_pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "singleInput": {
                "port": ('con1', 5, 8),
            },
            "smearing": 0,
            "time_of_flight": 160,
            "intermediate_frequency": 750000000.0,
        },
    },
    "pulses": {
        "single_pulse": {
            "length": 100,
            "waveforms": {
                "single": "single_wf",
            },
            "integration_weights": {
                "cos": "cosine_weights",
                "sin": "sine_weights",
                "minus_sin": "minus_sine_weights",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
    },
    "waveforms": {
        "single_wf": {
            "type": "constant",
            "sample": 0.25,
        },
    },
    "digital_waveforms": {
        "ON": {
            "samples": [(1, 0)],
        },
    },
    "integration_weights": {
        "cosine_weights": {
            "cosine": [(1.0, 100)],
            "sine": [(0.0, 100)],
        },
        "sine_weights": {
            "cosine": [(0.0, 100)],
            "sine": [(1.0, 100)],
        },
        "minus_sine_weights": {
            "cosine": [(0.0, 100)],
            "sine": [(-1.0, 100)],
        },
    },
    "mixers": {},
}


