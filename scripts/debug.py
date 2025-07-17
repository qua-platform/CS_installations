
# Single QUA script generated at 2025-07-08 17:00:35.818678
# QUA library version: 1.2.2

from qm import CompilerOptionArguments
from qm.qua import *

with program() as prog:
    v1 = declare(int, )
    a1 = declare(fixed, value=[-10000000.0, 10000000.0])
    with for_each_((v1),(a1)):
        pass
    with while_():
        update_frequency("AOM_trapping", v1, "Hz", False)
        play("const", "AOM_trapping")



    ####     SERIALIZATION VALIDATION ERROR     ####
    #
    #  for must be used with for_init, for_update, for_body and for_cond
    #
    # Trace:
    #   ['Traceback (most recent call last):\n', '  File "C:\\Git\\QM-CS-Michal\\venv\\Lib\\site-packages\\qm\\serialization\\generate_qua_script.py", line 103, in _generate_qua_script_pb\n    extra_info = extra_info + _validate_program(proto_prog, serialized_program)\n                              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n', '  File "C:\\Git\\QM-CS-Michal\\venv\\Lib\\site-packages\\qm\\serialization\\generate_qua_script.py", line 123, in _validate_program\n    exec(serialized_program, generated_mod.__dict__)\n', '  File "<string>", line 10, in <module>\n', '  File "C:\\Git\\QM-CS-Michal\\venv\\Lib\\site-packages\\qm\\qua\\_dsl.py", line 355, in update_frequency\n    body = _get_scope_as_blocks_body()\n           ^^^^^^^^^^^^^^^^^^^^^^^^^^^\n', '  File "C:\\Git\\QM-CS-Michal\\venv\\Lib\\site-packages\\qm\\qua\\_dsl.py", line 1969, in _get_scope_as_blocks_body\n    return last_block.body()\n           ^^^^^^^^^^^^^^^^^\n', '  File "C:\\Git\\QM-CS-Michal\\venv\\Lib\\site-packages\\qm\\qua\\_dsl.py", line 1896, in body\n    raise QmQuaException("for must be used with for_init, for_update, for_body and for_cond")\n', 'qm.exceptions.QmQuaException: for must be used with for_init, for_update, for_body and for_cond\n']
    #
    ################################################

            
config = {
    "version": 1,
    "controllers": {
        "con1": {
            "type": "opx1000",
            "fems": {
                "3": {
                    "type": "LF",
                    "analog_outputs": {
                        "1": {
                            "offset": 0.0,
                            "delay": 0,
                            "output_mode": "direct",
                            "sampling_rate": 1000000000,
                            "upsampling_mode": "mw",
                        },
                        "2": {
                            "offset": 0.0,
                            "delay": 0,
                            "output_mode": "direct",
                            "sampling_rate": 1000000000,
                            "upsampling_mode": "mw",
                        },
                        "3": {
                            "offset": 0.0,
                            "delay": 0,
                            "output_mode": "direct",
                            "sampling_rate": 1000000000,
                            "upsampling_mode": "mw",
                        },
                        "4": {
                            "offset": 0.0,
                            "delay": 0,
                            "output_mode": "direct",
                            "sampling_rate": 1000000000,
                            "upsampling_mode": "mw",
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
                    },
                    "analog_inputs": {
                        "1": {
                            "offset": 0,
                            "sampling_rate": 1000000000,
                        },
                        "2": {
                            "offset": 0,
                            "sampling_rate": 1000000000,
                        },
                    },
                },
            },
        },
    },
    "elements": {
        "AOM_trapping": {
            "singleInput": {
                "port": ('con1', 3, 1),
            },
            "intermediate_frequency": 10000000,
            "operations": {
                "const": "trapping_pulse",
            },
            "digitalInputs": {
                "marker": {
                    "port": ('con1', 3, 1),
                    "delay": 0,
                    "buffer": 0,
                },
            },
        },
        "AOM_repump": {
            "singleInput": {
                "port": ('con1', 3, 2),
            },
            "intermediate_frequency": 10000000,
            "operations": {
                "const": "repump_pulse",
            },
            "digitalInputs": {
                "marker": {
                    "port": ('con1', 3, 2),
                    "delay": 0,
                    "buffer": 0,
                },
            },
        },
        "AOM_probe": {
            "singleInput": {
                "port": ('con1', 3, 3),
            },
            "intermediate_frequency": 10000000,
            "operations": {
                "const": "probe_pulse",
            },
            "digitalInputs": {
                "marker": {
                    "port": ('con1', 3, 3),
                    "delay": 0,
                    "buffer": 0,
                },
            },
        },
        "B_field": {
            "singleInput": {
                "port": ('con1', 3, 4),
            },
            "operations": {
                "const": "b_pulse",
            },
            "sticky": {
                "analog": True,
                "digital": True,
                "duration": 4,
            },
            "digitalInputs": {
                "marker": {
                    "port": ('con1', 3, 1),
                    "delay": 0,
                    "buffer": 0,
                },
            },
        },
        "PMT": {
            "singleInput": {
                "port": ('con1', 3, 1),
            },
            "digitalInputs": {
                "marker": {
                    "port": ('con1', 3, 3),
                    "delay": 80,
                    "buffer": 0,
                },
            },
            "operations": {
                "readout": "readout_pulse_1",
                "long_readout": "long_readout_pulse_1",
            },
            "outputs": {
                "out1": ('con1', 3, 1),
            },
            "outputPulseParameters": {
                "signalThreshold": -2000,
                "signalPolarity": "Below",
                "derivativeThreshold": -2000,
                "derivativePolarity": "Above",
            },
            "time_of_flight": 80,
            "smearing": 0,
        },
        "SPCM1": {
            "singleInput": {
                "port": ('con1', 3, 1),
            },
            "digitalInputs": {
                "marker": {
                    "port": ('con1', 3, 3),
                    "delay": 80,
                    "buffer": 0,
                },
            },
            "operations": {
                "readout": "readout_pulse_1",
                "long_readout": "long_readout_pulse_1",
            },
            "outputs": {
                "out1": ('con1', 3, 1),
            },
            "timeTaggingParameters": {
                "signalThreshold": -500,
                "signalPolarity": "Below",
                "derivativeThreshold": -10000,
                "derivativePolarity": "Above",
            },
            "time_of_flight": 80,
            "smearing": 0,
        },
        "SPCM2": {
            "singleInput": {
                "port": ('con1', 3, 1),
            },
            "digitalInputs": {
                "marker": {
                    "port": ('con1', 3, 4),
                    "delay": 80,
                    "buffer": 0,
                },
            },
            "operations": {
                "readout": "readout_pulse_2",
                "long_readout": "long_readout_pulse_2",
            },
            "outputs": {
                "out1": ('con1', 3, 2),
            },
            "timeTaggingParameters": {
                "signalThreshold": -500,
                "signalPolarity": "Below",
                "derivativeThreshold": -10000,
                "derivativePolarity": "Above",
            },
            "time_of_flight": 80,
            "smearing": 0,
        },
        "TTL1": {
            "digitalInputs": {
                "marker": {
                    "port": ('con1', 3, 6),
                    "delay": 0,
                    "buffer": 0,
                },
            },
            "operations": {
                "ON": "TTL_1",
            },
        },
        "TTL2": {
            "digitalInputs": {
                "marker": {
                    "port": ('con1', 3, 7),
                    "delay": 0,
                    "buffer": 0,
                },
            },
            "operations": {
                "ON": "TTL_2",
            },
        },
    },
    "pulses": {
        "trapping_pulse": {
            "operation": "control",
            "length": 1000,
            "waveforms": {
                "single": "trapping_const_wf",
            },
            "digital_marker": "ON",
        },
        "repump_pulse": {
            "operation": "control",
            "length": 1000,
            "waveforms": {
                "single": "repump_const_wf",
            },
            "digital_marker": "ON",
        },
        "probe_pulse": {
            "operation": "control",
            "length": 1000,
            "waveforms": {
                "single": "probe_const_wf",
            },
            "digital_marker": "ON",
        },
        "b_pulse": {
            "operation": "control",
            "length": 1000,
            "waveforms": {
                "single": "b_const_wf",
            },
            "digital_marker": "ON",
        },
        "TTL_1": {
            "operation": "control",
            "length": 3000,
            "digital_marker": "ON",
        },
        "TTL_2": {
            "operation": "control",
            "length": 3000,
            "digital_marker": "ON",
        },
        "readout_pulse_1": {
            "operation": "measurement",
            "length": 500,
            "digital_marker": "ON",
            "waveforms": {
                "single": "zero_wf",
            },
        },
        "long_readout_pulse_1": {
            "operation": "measurement",
            "length": 5000,
            "digital_marker": "ON",
            "waveforms": {
                "single": "zero_wf",
            },
        },
        "readout_pulse_2": {
            "operation": "measurement",
            "length": 500,
            "digital_marker": "ON",
            "waveforms": {
                "single": "zero_wf",
            },
        },
        "long_readout_pulse_2": {
            "operation": "measurement",
            "length": 5000,
            "digital_marker": "ON",
            "waveforms": {
                "single": "zero_wf",
            },
        },
    },
    "waveforms": {
        "trapping_const_wf": {
            "type": "constant",
            "sample": 0.1,
        },
        "repump_const_wf": {
            "type": "constant",
            "sample": 0.1,
        },
        "probe_const_wf": {
            "type": "constant",
            "sample": 0.1,
        },
        "b_const_wf": {
            "type": "constant",
            "sample": 0.1,
        },
        "zero_wf": {
            "type": "constant",
            "sample": 0.0,
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
}

loaded_config = {
    "version": 1,
    "controllers": {
        "con1": {
            "type": "opx1000",
            "fems": {
                "3": {
                    "type": "LF",
                    "analog_outputs": {
                        "1": {
                            "offset": 0.0,
                            "delay": 0,
                            "shareable": False,
                            "filter": {
                                "feedforward": [],
                                "exponential": [],
                                "high_pass": None,
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
                                "exponential": [],
                                "high_pass": None,
                            },
                            "crosstalk": {},
                            "output_mode": "direct",
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "mw",
                        },
                        "3": {
                            "offset": 0.0,
                            "delay": 0,
                            "shareable": False,
                            "filter": {
                                "feedforward": [],
                                "exponential": [],
                                "high_pass": None,
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
                                "exponential": [],
                                "high_pass": None,
                            },
                            "crosstalk": {},
                            "output_mode": "direct",
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "mw",
                        },
                    },
                    "analog_inputs": {
                        "1": {
                            "offset": 0.0,
                            "gain_db": 0,
                            "shareable": False,
                            "sampling_rate": 1000000000.0,
                        },
                        "2": {
                            "offset": 0.0,
                            "gain_db": 0,
                            "shareable": False,
                            "sampling_rate": 1000000000.0,
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
                    },
                },
            },
        },
    },
    "oscillators": {},
    "elements": {
        "AOM_trapping": {
            "digitalInputs": {
                "marker": {
                    "delay": 0,
                    "buffer": 0,
                    "port": ('con1', 3, 1),
                },
            },
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "trapping_pulse",
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
                "port": ('con1', 3, 1),
            },
            "intermediate_frequency": 10000000.0,
        },
        "AOM_repump": {
            "digitalInputs": {
                "marker": {
                    "delay": 0,
                    "buffer": 0,
                    "port": ('con1', 3, 2),
                },
            },
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "repump_pulse",
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
                "port": ('con1', 3, 2),
            },
            "intermediate_frequency": 10000000.0,
        },
        "AOM_probe": {
            "digitalInputs": {
                "marker": {
                    "delay": 0,
                    "buffer": 0,
                    "port": ('con1', 3, 3),
                },
            },
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "probe_pulse",
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
                "port": ('con1', 3, 3),
            },
            "intermediate_frequency": 10000000.0,
        },
        "B_field": {
            "digitalInputs": {
                "marker": {
                    "delay": 0,
                    "buffer": 0,
                    "port": ('con1', 3, 1),
                },
            },
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "b_pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": True,
                "digital": True,
                "duration": 4,
            },
            "singleInput": {
                "port": ('con1', 3, 4),
            },
        },
        "PMT": {
            "digitalInputs": {
                "marker": {
                    "delay": 80,
                    "buffer": 0,
                    "port": ('con1', 3, 3),
                },
            },
            "digitalOutputs": {},
            "outputs": {
                "out1": ('con1', 3, 1),
            },
            "operations": {
                "readout": "readout_pulse_1",
                "long_readout": "long_readout_pulse_1",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "timeTaggingParameters": {
                "signalThreshold": -2000,
                "signalPolarity": "BELOW",
                "derivativeThreshold": -2000,
                "derivativePolarity": "ABOVE",
            },
            "singleInput": {
                "port": ('con1', 3, 1),
            },
            "smearing": 0,
            "time_of_flight": 80,
        },
        "SPCM1": {
            "digitalInputs": {
                "marker": {
                    "delay": 80,
                    "buffer": 0,
                    "port": ('con1', 3, 3),
                },
            },
            "digitalOutputs": {},
            "outputs": {
                "out1": ('con1', 3, 1),
            },
            "operations": {
                "readout": "readout_pulse_1",
                "long_readout": "long_readout_pulse_1",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "timeTaggingParameters": {
                "signalThreshold": -500,
                "signalPolarity": "BELOW",
                "derivativeThreshold": -10000,
                "derivativePolarity": "ABOVE",
            },
            "singleInput": {
                "port": ('con1', 3, 1),
            },
            "smearing": 0,
            "time_of_flight": 80,
        },
        "SPCM2": {
            "digitalInputs": {
                "marker": {
                    "delay": 80,
                    "buffer": 0,
                    "port": ('con1', 3, 4),
                },
            },
            "digitalOutputs": {},
            "outputs": {
                "out1": ('con1', 3, 2),
            },
            "operations": {
                "readout": "readout_pulse_2",
                "long_readout": "long_readout_pulse_2",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "timeTaggingParameters": {
                "signalThreshold": -500,
                "signalPolarity": "BELOW",
                "derivativeThreshold": -10000,
                "derivativePolarity": "ABOVE",
            },
            "singleInput": {
                "port": ('con1', 3, 1),
            },
            "smearing": 0,
            "time_of_flight": 80,
        },
        "TTL1": {
            "digitalInputs": {
                "marker": {
                    "delay": 0,
                    "buffer": 0,
                    "port": ('con1', 3, 6),
                },
            },
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "ON": "TTL_1",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
        },
        "TTL2": {
            "digitalInputs": {
                "marker": {
                    "delay": 0,
                    "buffer": 0,
                    "port": ('con1', 3, 7),
                },
            },
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "ON": "TTL_2",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
        },
    },
    "pulses": {
        "trapping_pulse": {
            "length": 1000,
            "waveforms": {
                "single": "trapping_const_wf",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "repump_pulse": {
            "length": 1000,
            "waveforms": {
                "single": "repump_const_wf",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "probe_pulse": {
            "length": 1000,
            "waveforms": {
                "single": "probe_const_wf",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "b_pulse": {
            "length": 1000,
            "waveforms": {
                "single": "b_const_wf",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "TTL_1": {
            "length": 3000,
            "waveforms": {},
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "TTL_2": {
            "length": 3000,
            "waveforms": {},
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "readout_pulse_1": {
            "length": 500,
            "waveforms": {
                "single": "zero_wf",
            },
            "integration_weights": {},
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "long_readout_pulse_1": {
            "length": 5000,
            "waveforms": {
                "single": "zero_wf",
            },
            "integration_weights": {},
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "readout_pulse_2": {
            "length": 500,
            "waveforms": {
                "single": "zero_wf",
            },
            "integration_weights": {},
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "long_readout_pulse_2": {
            "length": 5000,
            "waveforms": {
                "single": "zero_wf",
            },
            "integration_weights": {},
            "operation": "measurement",
            "digital_marker": "ON",
        },
    },
    "waveforms": {
        "trapping_const_wf": {
            "type": "constant",
            "sample": 0.1,
        },
        "repump_const_wf": {
            "type": "constant",
            "sample": 0.1,
        },
        "probe_const_wf": {
            "type": "constant",
            "sample": 0.1,
        },
        "b_const_wf": {
            "type": "constant",
            "sample": 0.1,
        },
        "zero_wf": {
            "type": "constant",
            "sample": 0.0,
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
    "integration_weights": {},
    "mixers": {},
}


