
# Single QUA script generated at 2024-10-31 17:41:13.512168
# QUA library version: 1.2.1a1

from qm.qua import *

with program() as prog:
    v1 = declare(fixed, )
    v2 = declare(fixed, )
    v3 = declare(fixed, )
    v4 = declare(fixed, )
    v5 = declare(fixed, )
    v6 = declare(fixed, )
    v7 = declare(fixed, )
    v8 = declare(fixed, )
    v9 = declare(fixed, )
    v10 = declare(fixed, )
    v11 = declare(fixed, )
    v12 = declare(fixed, )
    v13 = declare(fixed, )
    v14 = declare(fixed, )
    v15 = declare(fixed, )
    v16 = declare(fixed, )
    v17 = declare(fixed, )
    v18 = declare(fixed, )
    v19 = declare(fixed, )
    v20 = declare(fixed, )
    v21 = declare(fixed, )
    v22 = declare(fixed, )
    v23 = declare(fixed, )
    v24 = declare(fixed, )
    v25 = declare(fixed, )
    v26 = declare(fixed, )
    v27 = declare(fixed, )
    v28 = declare(fixed, )
    v29 = declare(fixed, )
    v30 = declare(fixed, )
    v31 = declare(fixed, )
    v32 = declare(fixed, )
    v33 = declare(fixed, )
    v34 = declare(int, )
    v35 = declare(bool, value=True)
    with while_(v35):
        pause()
        assign(v34, IO1)
        with if_((v34<2)):
            assign(v17, 1.0)
            assign(v15, Util.cond((v34==0),1.0,0.125))
            assign(v7, Util.cond((v34==0),0.0,v7))
            assign(v8, Util.cond((v34==0),0.0,v8))
            assign(v33, 7.96875)
            with for_(v9,-1.0,(v9<=1.0),(v9+0.125)):
                with for_(v10,-1.0,(v10<=1.0),(v10+0.125)):
                    assign(v11, ((v9*v15)+v7))
                    assign(v12, ((v10*v15)+v8))
                    align()
                    reset_phase("__oct__oct1_1_IQmixer")
                    reset_phase("__oct__oct1_1_lo_analyzer")
                    reset_phase("__oct__oct1_1_image_analyzer")
                    play("DC_offset"*amp(v11), "__oct__oct1_1_I_offset")
                    play("DC_offset"*amp(v12), "__oct__oct1_1_Q_offset")
                    play("calibration"*amp(v17), "__oct__oct1_1_IQmixer")
                    measure("Analyze", "__oct__oct1_1_lo_analyzer", None, dual_demod.full("integW_cos", "integW_sin", v3), dual_demod.full("integW_minus_sin", "integW_cos", v1))
                    measure("Analyze", "__oct__oct1_1_image_analyzer", None, dual_demod.full("integW_cos", "integW_sin", v4), dual_demod.full("integW_minus_sin", "integW_cos", v2))
                    assign(v5, ((v3*v3)+(v1*v1)))
                    assign(v6, ((v4*v4)+(v2*v2)))
                    with if_((v5<v33)):
                        assign(v13, v11)
                        assign(v14, v12)
                        assign(v33, v5)
                    save(v11, "i_scan")
                    save(v12, "q_scan")
                    save(v5, "lo")
            assign(v7, Util.cond((v34==1),v13,0.0))
            assign(v8, Util.cond((v34==1),v14,0.0))
            with if_((v34==0)):
                measure("Analyze", "__oct__oct1_1_lo_analyzer", "lo_adc_data")
        with else_():
            with if_((v34<4)):
                assign(v17, 1.0)
                assign(v16, Util.cond((v34==2),1.0,0.125))
                assign(v11, 0.0)
                assign(v12, 0.0)
                pause()
                assign(v18, IO1)
                assign(v19, IO2)
                with for_(v20,-0.25,(v20<=0.25),(v20+0.015625)):
                    with for_(v21,-0.25,(v21<=0.25),(v21+0.015625)):
                        assign(v22, ((v20*v16)+v18))
                        assign(v23, ((v21*v16)+v19))
                        assign(v28, v23)
                        assign(v26, (v28*v28))
                        assign(v27, ((1+(1.5*v26))-(3.125*(v26*v26))))
                        assign(v24, ((1+v22)+((0.5*v22)*v22)))
                        assign(v25, ((1-v22)+((0.5*v22)*v22)))
                        assign(v29, (v24*v27))
                        assign(v30, (v24*v28))
                        assign(v31, (v25*v28))
                        assign(v32, (v25*v27))
                        update_correction("__oct__oct1_1_IQmixer",v29,v30,v31,v32)
                        align()
                        reset_phase("__oct__oct1_1_IQmixer")
                        reset_phase("__oct__oct1_1_lo_analyzer")
                        reset_phase("__oct__oct1_1_image_analyzer")
                        play("DC_offset"*amp(v11), "__oct__oct1_1_I_offset")
                        play("DC_offset"*amp(v12), "__oct__oct1_1_Q_offset")
                        play("calibration"*amp(v17), "__oct__oct1_1_IQmixer")
                        measure("Analyze", "__oct__oct1_1_lo_analyzer", None, dual_demod.full("integW_cos", "integW_sin", v3), dual_demod.full("integW_minus_sin", "integW_cos", v1))
                        measure("Analyze", "__oct__oct1_1_image_analyzer", None, dual_demod.full("integW_cos", "integW_sin", v4), dual_demod.full("integW_minus_sin", "integW_cos", v2))
                        assign(v5, ((v3*v3)+(v1*v1)))
                        assign(v6, ((v4*v4)+(v2*v2)))
                        save(v22, "g_scan")
                        save(v23, "p_scan")
                        save(v6, "image")
            with else_():
                assign(v35, False)


config = {
    "version": 1,
    "controllers": {
        "con1": {
            "type": "opx1",
            "analog_outputs": {
                "1": {
                    "offset": -0.01559603907814195,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                    "crosstalk": {},
                },
                "2": {
                    "offset": 0.006848445639807789,
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
            "digital_outputs": {},
            "digital_inputs": {},
        },
    },
    "oscillators": {},
    "elements": {
        "qubit_xy": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "x180": "qubit_xy.x180.pulse",
                "square": "qubit_xy.square.pulse",
                "saturation": "qubit_xy.saturation.pulse",
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
            "mixInputs": {
                "I": ('con1', 1, 3),
                "Q": ('con1', 1, 4),
                "mixer": "qubit_xy_mixer_8a4",
                "lo_frequency": 4000000000.0,
            },
            "intermediate_frequency": 50000000.0,
        },
        "__oct__oct1_1_Q_offset": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "DC_offset": "__oct__DC_offset_pulse",
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
        },
        "__oct__oct1_2_image_analyzer": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {
                "out2": ('con1', 1, 2),
                "out1": ('con1', 1, 1),
            },
            "operations": {
                "Analyze": "__oct__Analyze_pulse",
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
            "mixInputs": {
                "I": ('con1', 1, 3),
                "Q": ('con1', 1, 4),
                "mixer": "__oct__dummy_mixer",
                "lo_frequency": 6000000000.0,
            },
            "smearing": 0,
            "time_of_flight": 1400,
            "intermediate_frequency": -57000000.0,
        },
        "__oct__oct1_1_I_offset": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "DC_offset": "__oct__DC_offset_pulse",
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
        },
        "__oct__oct1_2_lo_analyzer": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {
                "out2": ('con1', 1, 2),
                "out1": ('con1', 1, 1),
            },
            "operations": {
                "Analyze": "__oct__Analyze_pulse",
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
            "mixInputs": {
                "I": ('con1', 1, 3),
                "Q": ('con1', 1, 4),
                "mixer": "__oct__dummy_mixer",
                "lo_frequency": 6000000000.0,
            },
            "smearing": 0,
            "time_of_flight": 1400,
            "intermediate_frequency": -7000000.0,
        },
        "__oct__oct1_1_signal_analyzer": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {
                "out2": ('con1', 1, 2),
                "out1": ('con1', 1, 1),
            },
            "operations": {
                "Analyze": "__oct__Analyze_pulse",
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
            "mixInputs": {
                "I": ('con1', 1, 1),
                "Q": ('con1', 1, 2),
                "mixer": "__oct__dummy_mixer",
                "lo_frequency": 6000000000.0,
            },
            "smearing": 0,
            "time_of_flight": 1400,
            "intermediate_frequency": 43000000.0,
        },
        "__oct__oct1_1_lo_analyzer": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {
                "out2": ('con1', 1, 2),
                "out1": ('con1', 1, 1),
            },
            "operations": {
                "Analyze": "__oct__Analyze_pulse",
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
            "mixInputs": {
                "I": ('con1', 1, 1),
                "Q": ('con1', 1, 2),
                "mixer": "__oct__dummy_mixer",
                "lo_frequency": 6000000000.0,
            },
            "smearing": 0,
            "time_of_flight": 1400,
            "intermediate_frequency": -7000000.0,
        },
        "resonator": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {
                "out2": ('con1', 1, 2),
                "out1": ('con1', 1, 1),
            },
            "operations": {
                "readout": "resonator.readout.pulse",
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
            "mixInputs": {
                "I": ('con1', 1, 1),
                "Q": ('con1', 1, 2),
                "mixer": "resonator_mixer_249",
                "lo_frequency": 6000000000.0,
            },
            "smearing": 0,
            "time_of_flight": 24,
            "intermediate_frequency": 50000000.0,
        },
        "__oct__oct1_2_IQmixer": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "calibration": "__oct__calibration_pulse",
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
            "mixInputs": {
                "I": ('con1', 1, 3),
                "Q": ('con1', 1, 4),
                "mixer": "__oct__dummy_mixer",
                "lo_frequency": 6000000000.0,
            },
            "intermediate_frequency": 50000000.0,
        },
        "__oct__oct1_2_I_offset": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "DC_offset": "__oct__DC_offset_pulse",
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
                "port": ('con1', 1, 3),
            },
        },
        "__oct__oct1_1_IQmixer": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "calibration": "__oct__calibration_pulse",
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
            "mixInputs": {
                "I": ('con1', 1, 1),
                "Q": ('con1', 1, 2),
                "mixer": "__oct__dummy_mixer",
                "lo_frequency": 6000000000.0,
            },
            "intermediate_frequency": 50000000.0,
        },
        "__oct__oct1_1_image_analyzer": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {
                "out2": ('con1', 1, 2),
                "out1": ('con1', 1, 1),
            },
            "operations": {
                "Analyze": "__oct__Analyze_pulse",
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
            "mixInputs": {
                "I": ('con1', 1, 1),
                "Q": ('con1', 1, 2),
                "mixer": "__oct__dummy_mixer",
                "lo_frequency": 6000000000.0,
            },
            "smearing": 0,
            "time_of_flight": 1400,
            "intermediate_frequency": -57000000.0,
        },
        "__oct__oct1_2_Q_offset": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "DC_offset": "__oct__DC_offset_pulse",
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
                "port": ('con1', 1, 4),
            },
        },
        "__oct__oct1_2_signal_analyzer": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {
                "out2": ('con1', 1, 2),
                "out1": ('con1', 1, 1),
            },
            "operations": {
                "Analyze": "__oct__Analyze_pulse",
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
            "mixInputs": {
                "I": ('con1', 1, 3),
                "Q": ('con1', 1, 4),
                "mixer": "__oct__dummy_mixer",
                "lo_frequency": 6000000000.0,
            },
            "smearing": 0,
            "time_of_flight": 1400,
            "intermediate_frequency": 43000000.0,
        },
    },
    "pulses": {
        "__oct__Analyze_pulse": {
            "length": 10000,
            "waveforms": {
                "I": "__oct__zero_wf",
                "Q": "__oct__zero_wf",
            },
            "integration_weights": {
                "integW_cos": "__oct__integW_cosine",
                "integW_sin": "__oct__integW_sine",
                "integW_minus_sin": "__oct__integW_minus_sine",
                "integW_zero": "__oct__integW_zero",
            },
            "operation": "measurement",
            "digital_marker": "__oct__ON",
        },
        "resonator.readout.pulse": {
            "length": 1000,
            "waveforms": {
                "I": "resonator.readout.wf.I",
                "Q": "resonator.readout.wf.Q",
            },
            "integration_weights": {
                "iw1": "resonator.readout.iw1",
                "iw2": "resonator.readout.iw2",
                "iw3": "resonator.readout.iw3",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "__oct__DC_offset_pulse": {
            "length": 12000,
            "waveforms": {
                "single": "__oct__DC_offset_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "const_pulse": {
            "length": 1000,
            "waveforms": {
                "I": "const_wf",
                "Q": "zero_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "__oct__calibration_pulse": {
            "length": 12000,
            "waveforms": {
                "I": "__oct__readout_wf",
                "Q": "__oct__zero_wf",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "__oct__ON",
        },
        "qubit_xy.x180.pulse": {
            "length": 20,
            "waveforms": {
                "I": "qubit_xy.x180.wf.I",
                "Q": "qubit_xy.x180.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "qubit_xy.square.pulse": {
            "length": 20,
            "waveforms": {
                "I": "qubit_xy.square.wf.I",
                "Q": "qubit_xy.square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "qubit_xy.saturation.pulse": {
            "length": 5000,
            "waveforms": {
                "I": "qubit_xy.saturation.wf.I",
                "Q": "qubit_xy.saturation.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
    },
    "waveforms": {
        "resonator.readout.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "qubit_xy.saturation.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "qubit_xy.square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "qubit_xy.x180.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 20,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "zero_wf": {
            "type": "constant",
            "sample": 0.0,
        },
        "qubit_xy.square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "__oct__zero_wf": {
            "type": "constant",
            "sample": 0.0,
        },
        "const_wf": {
            "type": "constant",
            "sample": 0.1,
        },
        "qubit_xy.x180.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.007460108018703365, 0.015031875129355693, 0.02247975961775374, 0.029545159612914956, 0.03596063878135093, 0.04146637828294318, 0.045827482636353806, 0.0488505495426262] + [0.050397880757583724] * 2 + [0.0488505495426262, 0.045827482636353806, 0.04146637828294318, 0.03596063878135093, 0.029545159612914956, 0.02247975961775374, 0.015031875129355693, 0.007460108018703365, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "__oct__DC_offset_wf": {
            "type": "constant",
            "sample": 0.25,
        },
        "__oct__readout_wf": {
            "type": "constant",
            "sample": 0.125,
        },
        "resonator.readout.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "qubit_xy.saturation.wf.I": {
            "type": "constant",
            "sample": 0.01,
        },
    },
    "digital_waveforms": {
        "__oct__OFF": {
            "samples": [(0, 0)],
        },
        "__oct__ON": {
            "samples": [(1, 0)],
        },
        "ON": {
            "samples": [(1, 0)],
        },
    },
    "integration_weights": {
        "__oct__integW_zero": {
            "cosine": [(0.0, 10000)],
            "sine": [(0.0, 10000)],
        },
        "__oct__integW_cosine": {
            "cosine": [(1.0, 10000)],
            "sine": [(0.0, 10000)],
        },
        "__oct__integW_sine": {
            "cosine": [(0.0, 10000)],
            "sine": [(1.0, 10000)],
        },
        "resonator.readout.iw1": {
            "cosine": [(1.0, 1000)],
            "sine": [(0.0, 1000)],
        },
        "resonator.readout.iw2": {
            "cosine": [(0.0, 1000)],
            "sine": [(1.0, 1000)],
        },
        "resonator.readout.iw3": {
            "cosine": [(0.0, 1000)],
            "sine": [(-1.0, 1000)],
        },
        "__oct__integW_minus_sine": {
            "cosine": [(0.0, 10000)],
            "sine": [(-1.0, 10000)],
        },
    },
    "mixers": {
        "resonator_mixer_249": [{'intermediate_frequency': 50000000.0, 'lo_frequency': 6000000000.0, 'correction': (1.0016890286012021, 0.011814927702862053, 0.011780032769537159, 0.9987305786856052)}],
        "__oct__dummy_mixer": [
            {'intermediate_frequency': 50000000.0, 'lo_frequency': 6000000000.0, 'correction': (1.0, 0.0, 0.0, 1.0)},
            {'intermediate_frequency': 43000000.0, 'lo_frequency': 6000000000.0, 'correction': (1.0, 0.0, 0.0, 1.0)},
            {'intermediate_frequency': -7000000.0, 'lo_frequency': 6000000000.0, 'correction': (1.0, 0.0, 0.0, 1.0)},
            {'intermediate_frequency': -57000000.0, 'lo_frequency': 6000000000.0, 'correction': (1.0, 0.0, 0.0, 1.0)},
        ],
        "qubit_xy_mixer_8a4": [{'intermediate_frequency': 50000000.0, 'lo_frequency': 4000000000.0, 'correction': (1.0, 0.0, 0.0, 1.0)}],
    },
}

loaded_config = {
    "version": 1,
    "controllers": {
        "con1": {
            "type": "opx1",
            "analog_outputs": {
                "1": {
                    "offset": -0.01559603907814195,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                    "crosstalk": {},
                },
                "2": {
                    "offset": 0.006848445639807789,
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
            "digital_outputs": {},
            "digital_inputs": {},
        },
    },
    "oscillators": {},
    "elements": {
        "qubit_xy": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "x180": "qubit_xy.x180.pulse",
                "square": "qubit_xy.square.pulse",
                "saturation": "qubit_xy.saturation.pulse",
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
            "mixInputs": {
                "I": ('con1', 1, 3),
                "Q": ('con1', 1, 4),
                "mixer": "qubit_xy_mixer_8a4",
                "lo_frequency": 4000000000.0,
            },
            "intermediate_frequency": 50000000.0,
        },
        "__oct__oct1_1_Q_offset": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "DC_offset": "__oct__DC_offset_pulse",
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
        },
        "__oct__oct1_2_image_analyzer": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {
                "out2": ('con1', 1, 2),
                "out1": ('con1', 1, 1),
            },
            "operations": {
                "Analyze": "__oct__Analyze_pulse",
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
            "mixInputs": {
                "I": ('con1', 1, 3),
                "Q": ('con1', 1, 4),
                "mixer": "__oct__dummy_mixer",
                "lo_frequency": 6000000000.0,
            },
            "smearing": 0,
            "time_of_flight": 1400,
            "intermediate_frequency": -57000000.0,
        },
        "__oct__oct1_1_I_offset": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "DC_offset": "__oct__DC_offset_pulse",
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
        },
        "__oct__oct1_2_lo_analyzer": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {
                "out2": ('con1', 1, 2),
                "out1": ('con1', 1, 1),
            },
            "operations": {
                "Analyze": "__oct__Analyze_pulse",
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
            "mixInputs": {
                "I": ('con1', 1, 3),
                "Q": ('con1', 1, 4),
                "mixer": "__oct__dummy_mixer",
                "lo_frequency": 6000000000.0,
            },
            "smearing": 0,
            "time_of_flight": 1400,
            "intermediate_frequency": -7000000.0,
        },
        "__oct__oct1_1_signal_analyzer": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {
                "out2": ('con1', 1, 2),
                "out1": ('con1', 1, 1),
            },
            "operations": {
                "Analyze": "__oct__Analyze_pulse",
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
            "mixInputs": {
                "I": ('con1', 1, 1),
                "Q": ('con1', 1, 2),
                "mixer": "__oct__dummy_mixer",
                "lo_frequency": 6000000000.0,
            },
            "smearing": 0,
            "time_of_flight": 1400,
            "intermediate_frequency": 43000000.0,
        },
        "__oct__oct1_1_lo_analyzer": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {
                "out2": ('con1', 1, 2),
                "out1": ('con1', 1, 1),
            },
            "operations": {
                "Analyze": "__oct__Analyze_pulse",
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
            "mixInputs": {
                "I": ('con1', 1, 1),
                "Q": ('con1', 1, 2),
                "mixer": "__oct__dummy_mixer",
                "lo_frequency": 6000000000.0,
            },
            "smearing": 0,
            "time_of_flight": 1400,
            "intermediate_frequency": -7000000.0,
        },
        "resonator": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {
                "out2": ('con1', 1, 2),
                "out1": ('con1', 1, 1),
            },
            "operations": {
                "readout": "resonator.readout.pulse",
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
            "mixInputs": {
                "I": ('con1', 1, 1),
                "Q": ('con1', 1, 2),
                "mixer": "resonator_mixer_249",
                "lo_frequency": 6000000000.0,
            },
            "smearing": 0,
            "time_of_flight": 24,
            "intermediate_frequency": 50000000.0,
        },
        "__oct__oct1_2_IQmixer": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "calibration": "__oct__calibration_pulse",
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
            "mixInputs": {
                "I": ('con1', 1, 3),
                "Q": ('con1', 1, 4),
                "mixer": "__oct__dummy_mixer",
                "lo_frequency": 6000000000.0,
            },
            "intermediate_frequency": 50000000.0,
        },
        "__oct__oct1_2_I_offset": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "DC_offset": "__oct__DC_offset_pulse",
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
                "port": ('con1', 1, 3),
            },
        },
        "__oct__oct1_1_IQmixer": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "calibration": "__oct__calibration_pulse",
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
            "mixInputs": {
                "I": ('con1', 1, 1),
                "Q": ('con1', 1, 2),
                "mixer": "__oct__dummy_mixer",
                "lo_frequency": 6000000000.0,
            },
            "intermediate_frequency": 50000000.0,
        },
        "__oct__oct1_1_image_analyzer": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {
                "out2": ('con1', 1, 2),
                "out1": ('con1', 1, 1),
            },
            "operations": {
                "Analyze": "__oct__Analyze_pulse",
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
            "mixInputs": {
                "I": ('con1', 1, 1),
                "Q": ('con1', 1, 2),
                "mixer": "__oct__dummy_mixer",
                "lo_frequency": 6000000000.0,
            },
            "smearing": 0,
            "time_of_flight": 1400,
            "intermediate_frequency": -57000000.0,
        },
        "__oct__oct1_2_Q_offset": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "DC_offset": "__oct__DC_offset_pulse",
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
                "port": ('con1', 1, 4),
            },
        },
        "__oct__oct1_2_signal_analyzer": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {
                "out2": ('con1', 1, 2),
                "out1": ('con1', 1, 1),
            },
            "operations": {
                "Analyze": "__oct__Analyze_pulse",
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
            "mixInputs": {
                "I": ('con1', 1, 3),
                "Q": ('con1', 1, 4),
                "mixer": "__oct__dummy_mixer",
                "lo_frequency": 6000000000.0,
            },
            "smearing": 0,
            "time_of_flight": 1400,
            "intermediate_frequency": 43000000.0,
        },
    },
    "pulses": {
        "__oct__Analyze_pulse": {
            "length": 10000,
            "waveforms": {
                "I": "__oct__zero_wf",
                "Q": "__oct__zero_wf",
            },
            "integration_weights": {
                "integW_cos": "__oct__integW_cosine",
                "integW_sin": "__oct__integW_sine",
                "integW_minus_sin": "__oct__integW_minus_sine",
                "integW_zero": "__oct__integW_zero",
            },
            "operation": "measurement",
            "digital_marker": "__oct__ON",
        },
        "resonator.readout.pulse": {
            "length": 1000,
            "waveforms": {
                "I": "resonator.readout.wf.I",
                "Q": "resonator.readout.wf.Q",
            },
            "integration_weights": {
                "iw1": "resonator.readout.iw1",
                "iw2": "resonator.readout.iw2",
                "iw3": "resonator.readout.iw3",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "__oct__DC_offset_pulse": {
            "length": 12000,
            "waveforms": {
                "single": "__oct__DC_offset_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "const_pulse": {
            "length": 1000,
            "waveforms": {
                "I": "const_wf",
                "Q": "zero_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "__oct__calibration_pulse": {
            "length": 12000,
            "waveforms": {
                "I": "__oct__readout_wf",
                "Q": "__oct__zero_wf",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "__oct__ON",
        },
        "qubit_xy.x180.pulse": {
            "length": 20,
            "waveforms": {
                "I": "qubit_xy.x180.wf.I",
                "Q": "qubit_xy.x180.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "qubit_xy.square.pulse": {
            "length": 20,
            "waveforms": {
                "I": "qubit_xy.square.wf.I",
                "Q": "qubit_xy.square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "qubit_xy.saturation.pulse": {
            "length": 5000,
            "waveforms": {
                "I": "qubit_xy.saturation.wf.I",
                "Q": "qubit_xy.saturation.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
    },
    "waveforms": {
        "resonator.readout.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "qubit_xy.saturation.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "qubit_xy.square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "qubit_xy.x180.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 20,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "zero_wf": {
            "type": "constant",
            "sample": 0.0,
        },
        "qubit_xy.square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "__oct__zero_wf": {
            "type": "constant",
            "sample": 0.0,
        },
        "const_wf": {
            "type": "constant",
            "sample": 0.1,
        },
        "qubit_xy.x180.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.007460108018703365, 0.015031875129355693, 0.02247975961775374, 0.029545159612914956, 0.03596063878135093, 0.04146637828294318, 0.045827482636353806, 0.0488505495426262] + [0.050397880757583724] * 2 + [0.0488505495426262, 0.045827482636353806, 0.04146637828294318, 0.03596063878135093, 0.029545159612914956, 0.02247975961775374, 0.015031875129355693, 0.007460108018703365, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "__oct__DC_offset_wf": {
            "type": "constant",
            "sample": 0.25,
        },
        "__oct__readout_wf": {
            "type": "constant",
            "sample": 0.125,
        },
        "resonator.readout.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "qubit_xy.saturation.wf.I": {
            "type": "constant",
            "sample": 0.01,
        },
    },
    "digital_waveforms": {
        "__oct__OFF": {
            "samples": [(0, 0)],
        },
        "__oct__ON": {
            "samples": [(1, 0)],
        },
        "ON": {
            "samples": [(1, 0)],
        },
    },
    "integration_weights": {
        "__oct__integW_zero": {
            "cosine": [(0.0, 10000)],
            "sine": [(0.0, 10000)],
        },
        "__oct__integW_cosine": {
            "cosine": [(1.0, 10000)],
            "sine": [(0.0, 10000)],
        },
        "__oct__integW_sine": {
            "cosine": [(0.0, 10000)],
            "sine": [(1.0, 10000)],
        },
        "resonator.readout.iw1": {
            "cosine": [(1.0, 1000)],
            "sine": [(0.0, 1000)],
        },
        "resonator.readout.iw2": {
            "cosine": [(0.0, 1000)],
            "sine": [(1.0, 1000)],
        },
        "resonator.readout.iw3": {
            "cosine": [(0.0, 1000)],
            "sine": [(-1.0, 1000)],
        },
        "__oct__integW_minus_sine": {
            "cosine": [(0.0, 10000)],
            "sine": [(-1.0, 10000)],
        },
    },
    "mixers": {
        "resonator_mixer_249": [{'intermediate_frequency': 50000000.0, 'lo_frequency': 6000000000.0, 'correction': (1.0016890286012021, 0.011814927702862053, 0.011780032769537159, 0.9987305786856052)}],
        "__oct__dummy_mixer": [
            {'intermediate_frequency': 50000000.0, 'lo_frequency': 6000000000.0, 'correction': (1.0, 0.0, 0.0, 1.0)},
            {'intermediate_frequency': 43000000.0, 'lo_frequency': 6000000000.0, 'correction': (1.0, 0.0, 0.0, 1.0)},
            {'intermediate_frequency': -7000000.0, 'lo_frequency': 6000000000.0, 'correction': (1.0, 0.0, 0.0, 1.0)},
            {'intermediate_frequency': -57000000.0, 'lo_frequency': 6000000000.0, 'correction': (1.0, 0.0, 0.0, 1.0)},
        ],
        "qubit_xy_mixer_8a4": [{'intermediate_frequency': 50000000.0, 'lo_frequency': 4000000000.0, 'correction': (1.0, 0.0, 0.0, 1.0)}],
    },
}


