
# Single QUA script generated at 2024-11-14 18:29:33.057397
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
                "5": {
                    "offset": 0.0,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                    "crosstalk": {},
                },
                "6": {
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
            "digital_outputs": {
                "1": {
                    "shareable": False,
                    "inverted": False,
                },
            },
            "digital_inputs": {},
        },
    },
    "oscillators": {},
    "elements": {
        "__oct__oct1_3_I_offset": {
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
                "port": ('con1', 1, 5),
            },
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
        "__oct__oct1_3_IQmixer": {
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
                "I": ('con1', 1, 5),
                "Q": ('con1', 1, 6),
                "mixer": "__oct__dummy_mixer",
                "lo_frequency": 6000000000.0,
            },
            "intermediate_frequency": 50000000.0,
        },
        "__oct__oct1_3_signal_analyzer": {
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
                "I": ('con1', 1, 5),
                "Q": ('con1', 1, 6),
                "mixer": "__oct__dummy_mixer",
                "lo_frequency": 6000000000.0,
            },
            "smearing": 0,
            "time_of_flight": 1400,
            "intermediate_frequency": 43000000.0,
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
        "q2_xy": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "cw": "const_pulse",
                "x180": "x180_pulse_q2",
                "x90": "x90_pulse_q2",
                "-x90": "-x90_pulse_q2",
                "y90": "y90_pulse_q2",
                "y180": "y180_pulse_q2",
                "-y90": "-y90_pulse_q2",
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
                "I": ('con1', 1, 5),
                "Q": ('con1', 1, 6),
                "mixer": "q2_xy_mixer_ff0",
                "lo_frequency": 3950000000.0,
            },
            "intermediate_frequency": 75000000.0,
        },
        "rr1": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {
                "out2": ('con1', 1, 2),
                "out1": ('con1', 1, 1),
            },
            "operations": {
                "cw": "const_pulse",
                "readout": "readout_pulse_q1",
                "step": "step_pulse",
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
                "mixer": "rr1_mixer_d42",
                "lo_frequency": 5000000000.0,
            },
            "smearing": 0,
            "time_of_flight": 24,
            "intermediate_frequency": 75000000.0,
        },
        "q1_xy": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "cw": "const_pulse",
                "x180": "x180_pulse_q1",
                "x90": "x90_pulse_q1",
                "-x90": "-x90_pulse_q1",
                "y90": "y90_pulse_q1",
                "y180": "y180_pulse_q1",
                "-y90": "-y90_pulse_q1",
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
                "mixer": "q1_xy_mixer_26d",
                "lo_frequency": 3950000000.0,
            },
            "intermediate_frequency": 50000000.0,
        },
        "__oct__oct1_3_Q_offset": {
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
                "port": ('con1', 1, 6),
            },
        },
        "__oct__oct1_3_lo_analyzer": {
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
                "I": ('con1', 1, 5),
                "Q": ('con1', 1, 6),
                "mixer": "__oct__dummy_mixer",
                "lo_frequency": 6000000000.0,
            },
            "smearing": 0,
            "time_of_flight": 1400,
            "intermediate_frequency": -7000000.0,
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
        "rr2": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {
                "out2": ('con1', 1, 2),
                "out1": ('con1', 1, 1),
            },
            "operations": {
                "cw": "const_pulse",
                "readout": "readout_pulse_q2",
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
                "mixer": "rr2_mixer_7b5",
                "lo_frequency": 5000000000.0,
            },
            "smearing": 0,
            "time_of_flight": 24,
            "intermediate_frequency": 133000000.0,
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
        "__oct__oct1_3_image_analyzer": {
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
                "I": ('con1', 1, 5),
                "Q": ('con1', 1, 6),
                "mixer": "__oct__dummy_mixer",
                "lo_frequency": 6000000000.0,
            },
            "smearing": 0,
            "time_of_flight": 1400,
            "intermediate_frequency": -57000000.0,
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
        "-y90_pulse_q2": {
            "length": 40,
            "waveforms": {
                "I": "minus_y90_I_wf_q2",
                "Q": "minus_y90_Q_wf_q2",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "-y90_pulse_q1": {
            "length": 40,
            "waveforms": {
                "I": "minus_y90_I_wf_q1",
                "Q": "minus_y90_Q_wf_q1",
            },
            "integration_weights": {},
            "operation": "control",
        },
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
        "step_pulse": {
            "length": 16,
            "waveforms": {
                "I": "step_wf",
                "Q": "zero_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "-x90_pulse_q2": {
            "length": 40,
            "waveforms": {
                "I": "minus_x90_I_wf_q2",
                "Q": "minus_x90_Q_wf_q2",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "-x90_pulse_q1": {
            "length": 40,
            "waveforms": {
                "I": "minus_x90_I_wf_q1",
                "Q": "minus_x90_Q_wf_q1",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "y90_pulse_q1": {
            "length": 40,
            "waveforms": {
                "I": "y90_I_wf_q1",
                "Q": "y90_Q_wf_q1",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "readout_pulse_q2": {
            "length": 4000,
            "waveforms": {
                "I": "readout_wf_q2",
                "Q": "zero_wf",
            },
            "integration_weights": {
                "cos": "cosine_weights",
                "sin": "sine_weights",
                "minus_sin": "minus_sine_weights",
                "rotated_cos": "rotated_cosine_weights_q2",
                "rotated_sin": "rotated_sine_weights_q2",
                "rotated_minus_sin": "rotated_minus_sine_weights_q2",
                "opt_cos": "opt_cosine_weights_q2",
                "opt_sin": "opt_sine_weights_q2",
                "opt_minus_sin": "opt_minus_sine_weights_q2",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "readout_pulse_q1": {
            "length": 4000,
            "waveforms": {
                "I": "readout_wf_q1",
                "Q": "zero_wf",
            },
            "integration_weights": {
                "cos": "cosine_weights",
                "sin": "sine_weights",
                "minus_sin": "minus_sine_weights",
                "rotated_cos": "rotated_cosine_weights_q1",
                "rotated_sin": "rotated_sine_weights_q1",
                "rotated_minus_sin": "rotated_minus_sine_weights_q1",
                "opt_cos": "opt_cosine_weights_q1",
                "opt_sin": "opt_sine_weights_q1",
                "opt_minus_sin": "opt_minus_sine_weights_q1",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "y90_pulse_q2": {
            "length": 40,
            "waveforms": {
                "I": "y90_I_wf_q2",
                "Q": "y90_Q_wf_q2",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "x90_pulse_q2": {
            "length": 40,
            "waveforms": {
                "I": "x90_I_wf_q2",
                "Q": "x90_Q_wf_q2",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "x90_pulse_q1": {
            "length": 40,
            "waveforms": {
                "I": "x90_I_wf_q1",
                "Q": "x90_Q_wf_q1",
            },
            "integration_weights": {},
            "operation": "control",
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
        "y180_pulse_q1": {
            "length": 40,
            "waveforms": {
                "I": "y180_I_wf_q1",
                "Q": "y180_Q_wf_q1",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "y180_pulse_q2": {
            "length": 40,
            "waveforms": {
                "I": "y180_I_wf_q2",
                "Q": "y180_Q_wf_q2",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "x180_pulse_q2": {
            "length": 40,
            "waveforms": {
                "I": "x180_I_wf_q2",
                "Q": "x180_Q_wf_q2",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "x180_pulse_q1": {
            "length": 40,
            "waveforms": {
                "I": "x180_I_wf_q1",
                "Q": "x180_Q_wf_q1",
            },
            "integration_weights": {},
            "operation": "control",
        },
    },
    "waveforms": {
        "step_wf": {
            "type": "arbitrary",
            "samples": [0.0] * 6 + [0.4999847412109375] * 10,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "readout_wf_q1": {
            "type": "constant",
            "sample": 0.07,
        },
        "readout_wf_q2": {
            "type": "constant",
            "sample": 0.07,
        },
        "zero_wf": {
            "type": "constant",
            "sample": 0.0,
        },
        "__oct__zero_wf": {
            "type": "constant",
            "sample": 0.0,
        },
        "const_wf": {
            "type": "constant",
            "sample": 0.27,
        },
        "x180_I_wf_q1": {
            "type": "arbitrary",
            "samples": [0.0, 0.003898482620247966, 0.00882783109678569, 0.014945189167037706, 0.022393467220454093, 0.031286932872005575, 0.04169510925834998, 0.05362618927683272, 0.06701156038972575, 0.08169330242755682, 0.09741659909541572, 0.11382883673656312, 0.13048672437999825, 0.14687207025447396, 0.16241595024382866, 0.1765300044143878, 0.18864263131789072, 0.1982370608953941, 0.20488780808919338] + [0.20829193676209992] * 2 + [0.20488780808919338, 0.1982370608953941, 0.18864263131789072, 0.1765300044143878, 0.16241595024382866, 0.14687207025447396, 0.13048672437999825, 0.11382883673656312, 0.09741659909541572, 0.08169330242755682, 0.06701156038972575, 0.05362618927683272, 0.04169510925834998, 0.031286932872005575, 0.022393467220454093, 0.014945189167037706, 0.00882783109678569, 0.003898482620247966, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x180_I_wf_q2": {
            "type": "arbitrary",
            "samples": [0.0, 0.003898482620247966, 0.00882783109678569, 0.014945189167037706, 0.022393467220454093, 0.031286932872005575, 0.04169510925834998, 0.05362618927683272, 0.06701156038972575, 0.08169330242755682, 0.09741659909541572, 0.11382883673656312, 0.13048672437999825, 0.14687207025447396, 0.16241595024382866, 0.1765300044143878, 0.18864263131789072, 0.1982370608953941, 0.20488780808919338] + [0.20829193676209992] * 2 + [0.20488780808919338, 0.1982370608953941, 0.18864263131789072, 0.1765300044143878, 0.16241595024382866, 0.14687207025447396, 0.13048672437999825, 0.11382883673656312, 0.09741659909541572, 0.08169330242755682, 0.06701156038972575, 0.05362618927683272, 0.04169510925834998, 0.031286932872005575, 0.022393467220454093, 0.014945189167037706, 0.00882783109678569, 0.003898482620247966, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y180_Q_wf_q2": {
            "type": "arbitrary",
            "samples": [0.0, 0.003898482620247966, 0.00882783109678569, 0.014945189167037706, 0.022393467220454093, 0.031286932872005575, 0.04169510925834998, 0.05362618927683272, 0.06701156038972575, 0.08169330242755682, 0.09741659909541572, 0.11382883673656312, 0.13048672437999825, 0.14687207025447396, 0.16241595024382866, 0.1765300044143878, 0.18864263131789072, 0.1982370608953941, 0.20488780808919338] + [0.20829193676209992] * 2 + [0.20488780808919338, 0.1982370608953941, 0.18864263131789072, 0.1765300044143878, 0.16241595024382866, 0.14687207025447396, 0.13048672437999825, 0.11382883673656312, 0.09741659909541572, 0.08169330242755682, 0.06701156038972575, 0.05362618927683272, 0.04169510925834998, 0.031286932872005575, 0.022393467220454093, 0.014945189167037706, 0.00882783109678569, 0.003898482620247966, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "__oct__readout_wf": {
            "type": "constant",
            "sample": 0.125,
        },
        "x90_Q_wf_q1": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y180_Q_wf_q1": {
            "type": "arbitrary",
            "samples": [0.0, 0.003898482620247966, 0.00882783109678569, 0.014945189167037706, 0.022393467220454093, 0.031286932872005575, 0.04169510925834998, 0.05362618927683272, 0.06701156038972575, 0.08169330242755682, 0.09741659909541572, 0.11382883673656312, 0.13048672437999825, 0.14687207025447396, 0.16241595024382866, 0.1765300044143878, 0.18864263131789072, 0.1982370608953941, 0.20488780808919338] + [0.20829193676209992] * 2 + [0.20488780808919338, 0.1982370608953941, 0.18864263131789072, 0.1765300044143878, 0.16241595024382866, 0.14687207025447396, 0.13048672437999825, 0.11382883673656312, 0.09741659909541572, 0.08169330242755682, 0.06701156038972575, 0.05362618927683272, 0.04169510925834998, 0.031286932872005575, 0.022393467220454093, 0.014945189167037706, 0.00882783109678569, 0.003898482620247966, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x90_Q_wf_q2": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x90_I_wf_q1": {
            "type": "arbitrary",
            "samples": [0.0, 0.001949241310123983, 0.004413915548392845, 0.007472594583518853, 0.011196733610227046, 0.015643466436002788, 0.02084755462917499, 0.02681309463841636, 0.033505780194862875, 0.04084665121377841, 0.04870829954770786, 0.05691441836828156, 0.06524336218999913, 0.07343603512723698, 0.08120797512191433, 0.0882650022071939, 0.09432131565894536, 0.09911853044769706, 0.10244390404459669] + [0.10414596838104996] * 2 + [0.10244390404459669, 0.09911853044769706, 0.09432131565894536, 0.0882650022071939, 0.08120797512191433, 0.07343603512723698, 0.06524336218999913, 0.05691441836828156, 0.04870829954770786, 0.04084665121377841, 0.033505780194862875, 0.02681309463841636, 0.02084755462917499, 0.015643466436002788, 0.011196733610227046, 0.007472594583518853, 0.004413915548392845, 0.001949241310123983, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y180_I_wf_q1": {
            "type": "arbitrary",
            "samples": [-0.0] * 40,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x90_I_wf_q2": {
            "type": "arbitrary",
            "samples": [0.0, 0.001949241310123983, 0.004413915548392845, 0.007472594583518853, 0.011196733610227046, 0.015643466436002788, 0.02084755462917499, 0.02681309463841636, 0.033505780194862875, 0.04084665121377841, 0.04870829954770786, 0.05691441836828156, 0.06524336218999913, 0.07343603512723698, 0.08120797512191433, 0.0882650022071939, 0.09432131565894536, 0.09911853044769706, 0.10244390404459669] + [0.10414596838104996] * 2 + [0.10244390404459669, 0.09911853044769706, 0.09432131565894536, 0.0882650022071939, 0.08120797512191433, 0.07343603512723698, 0.06524336218999913, 0.05691441836828156, 0.04870829954770786, 0.04084665121377841, 0.033505780194862875, 0.02681309463841636, 0.02084755462917499, 0.015643466436002788, 0.011196733610227046, 0.007472594583518853, 0.004413915548392845, 0.001949241310123983, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_x90_Q_wf_q1": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_x90_I_wf_q2": {
            "type": "arbitrary",
            "samples": [0.0, -0.001949241310123983, -0.004413915548392845, -0.007472594583518853, -0.011196733610227046, -0.015643466436002788, -0.02084755462917499, -0.02681309463841636, -0.033505780194862875, -0.04084665121377841, -0.04870829954770786, -0.05691441836828156, -0.06524336218999913, -0.07343603512723698, -0.08120797512191433, -0.0882650022071939, -0.09432131565894536, -0.09911853044769706, -0.10244390404459669] + [-0.10414596838104996] * 2 + [-0.10244390404459669, -0.09911853044769706, -0.09432131565894536, -0.0882650022071939, -0.08120797512191433, -0.07343603512723698, -0.06524336218999913, -0.05691441836828156, -0.04870829954770786, -0.04084665121377841, -0.033505780194862875, -0.02681309463841636, -0.02084755462917499, -0.015643466436002788, -0.011196733610227046, -0.007472594583518853, -0.004413915548392845, -0.001949241310123983, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_x90_I_wf_q1": {
            "type": "arbitrary",
            "samples": [0.0, -0.001949241310123983, -0.004413915548392845, -0.007472594583518853, -0.011196733610227046, -0.015643466436002788, -0.02084755462917499, -0.02681309463841636, -0.033505780194862875, -0.04084665121377841, -0.04870829954770786, -0.05691441836828156, -0.06524336218999913, -0.07343603512723698, -0.08120797512191433, -0.0882650022071939, -0.09432131565894536, -0.09911853044769706, -0.10244390404459669] + [-0.10414596838104996] * 2 + [-0.10244390404459669, -0.09911853044769706, -0.09432131565894536, -0.0882650022071939, -0.08120797512191433, -0.07343603512723698, -0.06524336218999913, -0.05691441836828156, -0.04870829954770786, -0.04084665121377841, -0.033505780194862875, -0.02681309463841636, -0.02084755462917499, -0.015643466436002788, -0.011196733610227046, -0.007472594583518853, -0.004413915548392845, -0.001949241310123983, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_x90_Q_wf_q2": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y180_I_wf_q2": {
            "type": "arbitrary",
            "samples": [-0.0] * 40,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x180_Q_wf_q1": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x180_Q_wf_q2": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "__oct__DC_offset_wf": {
            "type": "constant",
            "sample": 0.25,
        },
        "minus_y90_I_wf_q2": {
            "type": "arbitrary",
            "samples": [-0.0] * 40,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_y90_I_wf_q1": {
            "type": "arbitrary",
            "samples": [-0.0] * 40,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_y90_Q_wf_q2": {
            "type": "arbitrary",
            "samples": [0.0, -0.001949241310123983, -0.004413915548392845, -0.007472594583518853, -0.011196733610227046, -0.015643466436002788, -0.02084755462917499, -0.02681309463841636, -0.033505780194862875, -0.04084665121377841, -0.04870829954770786, -0.05691441836828156, -0.06524336218999913, -0.07343603512723698, -0.08120797512191433, -0.0882650022071939, -0.09432131565894536, -0.09911853044769706, -0.10244390404459669] + [-0.10414596838104996] * 2 + [-0.10244390404459669, -0.09911853044769706, -0.09432131565894536, -0.0882650022071939, -0.08120797512191433, -0.07343603512723698, -0.06524336218999913, -0.05691441836828156, -0.04870829954770786, -0.04084665121377841, -0.033505780194862875, -0.02681309463841636, -0.02084755462917499, -0.015643466436002788, -0.011196733610227046, -0.007472594583518853, -0.004413915548392845, -0.001949241310123983, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_y90_Q_wf_q1": {
            "type": "arbitrary",
            "samples": [0.0, -0.001949241310123983, -0.004413915548392845, -0.007472594583518853, -0.011196733610227046, -0.015643466436002788, -0.02084755462917499, -0.02681309463841636, -0.033505780194862875, -0.04084665121377841, -0.04870829954770786, -0.05691441836828156, -0.06524336218999913, -0.07343603512723698, -0.08120797512191433, -0.0882650022071939, -0.09432131565894536, -0.09911853044769706, -0.10244390404459669] + [-0.10414596838104996] * 2 + [-0.10244390404459669, -0.09911853044769706, -0.09432131565894536, -0.0882650022071939, -0.08120797512191433, -0.07343603512723698, -0.06524336218999913, -0.05691441836828156, -0.04870829954770786, -0.04084665121377841, -0.033505780194862875, -0.02681309463841636, -0.02084755462917499, -0.015643466436002788, -0.011196733610227046, -0.007472594583518853, -0.004413915548392845, -0.001949241310123983, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y90_Q_wf_q1": {
            "type": "arbitrary",
            "samples": [0.0, 0.001949241310123983, 0.004413915548392845, 0.007472594583518853, 0.011196733610227046, 0.015643466436002788, 0.02084755462917499, 0.02681309463841636, 0.033505780194862875, 0.04084665121377841, 0.04870829954770786, 0.05691441836828156, 0.06524336218999913, 0.07343603512723698, 0.08120797512191433, 0.0882650022071939, 0.09432131565894536, 0.09911853044769706, 0.10244390404459669] + [0.10414596838104996] * 2 + [0.10244390404459669, 0.09911853044769706, 0.09432131565894536, 0.0882650022071939, 0.08120797512191433, 0.07343603512723698, 0.06524336218999913, 0.05691441836828156, 0.04870829954770786, 0.04084665121377841, 0.033505780194862875, 0.02681309463841636, 0.02084755462917499, 0.015643466436002788, 0.011196733610227046, 0.007472594583518853, 0.004413915548392845, 0.001949241310123983, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y90_I_wf_q2": {
            "type": "arbitrary",
            "samples": [-0.0] * 40,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y90_I_wf_q1": {
            "type": "arbitrary",
            "samples": [-0.0] * 40,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y90_Q_wf_q2": {
            "type": "arbitrary",
            "samples": [0.0, 0.001949241310123983, 0.004413915548392845, 0.007472594583518853, 0.011196733610227046, 0.015643466436002788, 0.02084755462917499, 0.02681309463841636, 0.033505780194862875, 0.04084665121377841, 0.04870829954770786, 0.05691441836828156, 0.06524336218999913, 0.07343603512723698, 0.08120797512191433, 0.0882650022071939, 0.09432131565894536, 0.09911853044769706, 0.10244390404459669] + [0.10414596838104996] * 2 + [0.10244390404459669, 0.09911853044769706, 0.09432131565894536, 0.0882650022071939, 0.08120797512191433, 0.07343603512723698, 0.06524336218999913, 0.05691441836828156, 0.04870829954770786, 0.04084665121377841, 0.033505780194862875, 0.02681309463841636, 0.02084755462917499, 0.015643466436002788, 0.011196733610227046, 0.007472594583518853, 0.004413915548392845, 0.001949241310123983, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
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
        "opt_sine_weights_q1": {
            "cosine": [(0.0, 4000)],
            "sine": [(1.0, 4000)],
        },
        "opt_sine_weights_q2": {
            "cosine": [(0.0, 4000)],
            "sine": [(1.0, 4000)],
        },
        "sine_weights": {
            "cosine": [(0.0, 4000)],
            "sine": [(1.0, 4000)],
        },
        "rotated_minus_sine_weights_q1": {
            "cosine": [(0.0, 4000)],
            "sine": [(-1.0, 4000)],
        },
        "__oct__integW_cosine": {
            "cosine": [(1.0, 10000)],
            "sine": [(0.0, 10000)],
        },
        "rotated_minus_sine_weights_q2": {
            "cosine": [(0.0, 4000)],
            "sine": [(-1.0, 4000)],
        },
        "__oct__integW_sine": {
            "cosine": [(0.0, 10000)],
            "sine": [(1.0, 10000)],
        },
        "rotated_sine_weights_q1": {
            "cosine": [(0.0, 4000)],
            "sine": [(1.0, 4000)],
        },
        "rotated_cosine_weights_q2": {
            "cosine": [(1.0, 4000)],
            "sine": [(0.0, 4000)],
        },
        "rotated_cosine_weights_q1": {
            "cosine": [(1.0, 4000)],
            "sine": [(0.0, 4000)],
        },
        "rotated_sine_weights_q2": {
            "cosine": [(0.0, 4000)],
            "sine": [(1.0, 4000)],
        },
        "cosine_weights": {
            "cosine": [(1.0, 4000)],
            "sine": [(0.0, 4000)],
        },
        "__oct__integW_zero": {
            "cosine": [(0.0, 10000)],
            "sine": [(0.0, 10000)],
        },
        "opt_minus_sine_weights_q1": {
            "cosine": [(0.0, 4000)],
            "sine": [(-1.0, 4000)],
        },
        "opt_minus_sine_weights_q2": {
            "cosine": [(0.0, 4000)],
            "sine": [(-1.0, 4000)],
        },
        "minus_sine_weights": {
            "cosine": [(0.0, 4000)],
            "sine": [(-1.0, 4000)],
        },
        "opt_cosine_weights_q1": {
            "cosine": [(1.0, 4000)],
            "sine": [(0.0, 4000)],
        },
        "opt_cosine_weights_q2": {
            "cosine": [(1.0, 4000)],
            "sine": [(0.0, 4000)],
        },
        "__oct__integW_minus_sine": {
            "cosine": [(0.0, 10000)],
            "sine": [(-1.0, 10000)],
        },
    },
    "mixers": {
        "rr2_mixer_7b5": [{'intermediate_frequency': 133000000.0, 'lo_frequency': 5000000000.0, 'correction': (1.0, 0.0, 0.0, 1.0)}],
        "__oct__dummy_mixer": [
            {'intermediate_frequency': 50000000.0, 'lo_frequency': 6000000000.0, 'correction': (1.0, 0.0, 0.0, 1.0)},
            {'intermediate_frequency': 43000000.0, 'lo_frequency': 6000000000.0, 'correction': (1.0, 0.0, 0.0, 1.0)},
            {'intermediate_frequency': -7000000.0, 'lo_frequency': 6000000000.0, 'correction': (1.0, 0.0, 0.0, 1.0)},
            {'intermediate_frequency': -57000000.0, 'lo_frequency': 6000000000.0, 'correction': (1.0, 0.0, 0.0, 1.0)},
        ],
        "q1_xy_mixer_26d": [{'intermediate_frequency': 50000000.0, 'lo_frequency': 3950000000.0, 'correction': (1.0, 0.0, 0.0, 1.0)}],
        "q2_xy_mixer_ff0": [{'intermediate_frequency': 75000000.0, 'lo_frequency': 3950000000.0, 'correction': (1.0, 0.0, 0.0, 1.0)}],
        "rr1_mixer_d42": [{'intermediate_frequency': 75000000.0, 'lo_frequency': 5000000000.0, 'correction': (1.0, 0.0, 0.0, 1.0)}],
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
                "5": {
                    "offset": 0.0,
                    "delay": 0,
                    "shareable": False,
                    "filter": {
                        "feedforward": [],
                        "feedback": [],
                    },
                    "crosstalk": {},
                },
                "6": {
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
            "digital_outputs": {
                "1": {
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
        "__oct__oct1_3_I_offset": {
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
                "port": ('con1', 1, 5),
            },
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
        "__oct__oct1_3_IQmixer": {
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
                "I": ('con1', 1, 5),
                "Q": ('con1', 1, 6),
                "mixer": "__oct__dummy_mixer",
                "lo_frequency": 6000000000.0,
            },
            "intermediate_frequency": 50000000.0,
        },
        "__oct__oct1_3_signal_analyzer": {
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
                "I": ('con1', 1, 5),
                "Q": ('con1', 1, 6),
                "mixer": "__oct__dummy_mixer",
                "lo_frequency": 6000000000.0,
            },
            "smearing": 0,
            "time_of_flight": 1400,
            "intermediate_frequency": 43000000.0,
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
        "q2_xy": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "cw": "const_pulse",
                "x180": "x180_pulse_q2",
                "x90": "x90_pulse_q2",
                "-x90": "-x90_pulse_q2",
                "y90": "y90_pulse_q2",
                "y180": "y180_pulse_q2",
                "-y90": "-y90_pulse_q2",
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
                "I": ('con1', 1, 5),
                "Q": ('con1', 1, 6),
                "mixer": "q2_xy_mixer_ff0",
                "lo_frequency": 3950000000.0,
            },
            "intermediate_frequency": 75000000.0,
        },
        "rr1": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {
                "out2": ('con1', 1, 2),
                "out1": ('con1', 1, 1),
            },
            "operations": {
                "cw": "const_pulse",
                "readout": "readout_pulse_q1",
                "step": "step_pulse",
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
                "mixer": "rr1_mixer_d42",
                "lo_frequency": 5000000000.0,
            },
            "smearing": 0,
            "time_of_flight": 24,
            "intermediate_frequency": 75000000.0,
        },
        "q1_xy": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "cw": "const_pulse",
                "x180": "x180_pulse_q1",
                "x90": "x90_pulse_q1",
                "-x90": "-x90_pulse_q1",
                "y90": "y90_pulse_q1",
                "y180": "y180_pulse_q1",
                "-y90": "-y90_pulse_q1",
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
                "mixer": "q1_xy_mixer_26d",
                "lo_frequency": 3950000000.0,
            },
            "intermediate_frequency": 50000000.0,
        },
        "__oct__oct1_3_Q_offset": {
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
                "port": ('con1', 1, 6),
            },
        },
        "__oct__oct1_3_lo_analyzer": {
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
                "I": ('con1', 1, 5),
                "Q": ('con1', 1, 6),
                "mixer": "__oct__dummy_mixer",
                "lo_frequency": 6000000000.0,
            },
            "smearing": 0,
            "time_of_flight": 1400,
            "intermediate_frequency": -7000000.0,
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
        "rr2": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {
                "out2": ('con1', 1, 2),
                "out1": ('con1', 1, 1),
            },
            "operations": {
                "cw": "const_pulse",
                "readout": "readout_pulse_q2",
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
                "mixer": "rr2_mixer_7b5",
                "lo_frequency": 5000000000.0,
            },
            "smearing": 0,
            "time_of_flight": 24,
            "intermediate_frequency": 133000000.0,
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
        "__oct__oct1_3_image_analyzer": {
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
                "I": ('con1', 1, 5),
                "Q": ('con1', 1, 6),
                "mixer": "__oct__dummy_mixer",
                "lo_frequency": 6000000000.0,
            },
            "smearing": 0,
            "time_of_flight": 1400,
            "intermediate_frequency": -57000000.0,
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
        "-y90_pulse_q2": {
            "length": 40,
            "waveforms": {
                "I": "minus_y90_I_wf_q2",
                "Q": "minus_y90_Q_wf_q2",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "-y90_pulse_q1": {
            "length": 40,
            "waveforms": {
                "I": "minus_y90_I_wf_q1",
                "Q": "minus_y90_Q_wf_q1",
            },
            "integration_weights": {},
            "operation": "control",
        },
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
        "step_pulse": {
            "length": 16,
            "waveforms": {
                "I": "step_wf",
                "Q": "zero_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "-x90_pulse_q2": {
            "length": 40,
            "waveforms": {
                "I": "minus_x90_I_wf_q2",
                "Q": "minus_x90_Q_wf_q2",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "-x90_pulse_q1": {
            "length": 40,
            "waveforms": {
                "I": "minus_x90_I_wf_q1",
                "Q": "minus_x90_Q_wf_q1",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "y90_pulse_q1": {
            "length": 40,
            "waveforms": {
                "I": "y90_I_wf_q1",
                "Q": "y90_Q_wf_q1",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "readout_pulse_q2": {
            "length": 4000,
            "waveforms": {
                "I": "readout_wf_q2",
                "Q": "zero_wf",
            },
            "integration_weights": {
                "cos": "cosine_weights",
                "sin": "sine_weights",
                "minus_sin": "minus_sine_weights",
                "rotated_cos": "rotated_cosine_weights_q2",
                "rotated_sin": "rotated_sine_weights_q2",
                "rotated_minus_sin": "rotated_minus_sine_weights_q2",
                "opt_cos": "opt_cosine_weights_q2",
                "opt_sin": "opt_sine_weights_q2",
                "opt_minus_sin": "opt_minus_sine_weights_q2",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "readout_pulse_q1": {
            "length": 4000,
            "waveforms": {
                "I": "readout_wf_q1",
                "Q": "zero_wf",
            },
            "integration_weights": {
                "cos": "cosine_weights",
                "sin": "sine_weights",
                "minus_sin": "minus_sine_weights",
                "rotated_cos": "rotated_cosine_weights_q1",
                "rotated_sin": "rotated_sine_weights_q1",
                "rotated_minus_sin": "rotated_minus_sine_weights_q1",
                "opt_cos": "opt_cosine_weights_q1",
                "opt_sin": "opt_sine_weights_q1",
                "opt_minus_sin": "opt_minus_sine_weights_q1",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "y90_pulse_q2": {
            "length": 40,
            "waveforms": {
                "I": "y90_I_wf_q2",
                "Q": "y90_Q_wf_q2",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "x90_pulse_q2": {
            "length": 40,
            "waveforms": {
                "I": "x90_I_wf_q2",
                "Q": "x90_Q_wf_q2",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "x90_pulse_q1": {
            "length": 40,
            "waveforms": {
                "I": "x90_I_wf_q1",
                "Q": "x90_Q_wf_q1",
            },
            "integration_weights": {},
            "operation": "control",
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
        "y180_pulse_q1": {
            "length": 40,
            "waveforms": {
                "I": "y180_I_wf_q1",
                "Q": "y180_Q_wf_q1",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "y180_pulse_q2": {
            "length": 40,
            "waveforms": {
                "I": "y180_I_wf_q2",
                "Q": "y180_Q_wf_q2",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "x180_pulse_q2": {
            "length": 40,
            "waveforms": {
                "I": "x180_I_wf_q2",
                "Q": "x180_Q_wf_q2",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "x180_pulse_q1": {
            "length": 40,
            "waveforms": {
                "I": "x180_I_wf_q1",
                "Q": "x180_Q_wf_q1",
            },
            "integration_weights": {},
            "operation": "control",
        },
    },
    "waveforms": {
        "step_wf": {
            "type": "arbitrary",
            "samples": [0.0] * 6 + [0.4999847412109375] * 10,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "readout_wf_q1": {
            "type": "constant",
            "sample": 0.07,
        },
        "readout_wf_q2": {
            "type": "constant",
            "sample": 0.07,
        },
        "zero_wf": {
            "type": "constant",
            "sample": 0.0,
        },
        "__oct__zero_wf": {
            "type": "constant",
            "sample": 0.0,
        },
        "const_wf": {
            "type": "constant",
            "sample": 0.27,
        },
        "x180_I_wf_q1": {
            "type": "arbitrary",
            "samples": [0.0, 0.003898482620247966, 0.00882783109678569, 0.014945189167037706, 0.022393467220454093, 0.031286932872005575, 0.04169510925834998, 0.05362618927683272, 0.06701156038972575, 0.08169330242755682, 0.09741659909541572, 0.11382883673656312, 0.13048672437999825, 0.14687207025447396, 0.16241595024382866, 0.1765300044143878, 0.18864263131789072, 0.1982370608953941, 0.20488780808919338] + [0.20829193676209992] * 2 + [0.20488780808919338, 0.1982370608953941, 0.18864263131789072, 0.1765300044143878, 0.16241595024382866, 0.14687207025447396, 0.13048672437999825, 0.11382883673656312, 0.09741659909541572, 0.08169330242755682, 0.06701156038972575, 0.05362618927683272, 0.04169510925834998, 0.031286932872005575, 0.022393467220454093, 0.014945189167037706, 0.00882783109678569, 0.003898482620247966, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x180_I_wf_q2": {
            "type": "arbitrary",
            "samples": [0.0, 0.003898482620247966, 0.00882783109678569, 0.014945189167037706, 0.022393467220454093, 0.031286932872005575, 0.04169510925834998, 0.05362618927683272, 0.06701156038972575, 0.08169330242755682, 0.09741659909541572, 0.11382883673656312, 0.13048672437999825, 0.14687207025447396, 0.16241595024382866, 0.1765300044143878, 0.18864263131789072, 0.1982370608953941, 0.20488780808919338] + [0.20829193676209992] * 2 + [0.20488780808919338, 0.1982370608953941, 0.18864263131789072, 0.1765300044143878, 0.16241595024382866, 0.14687207025447396, 0.13048672437999825, 0.11382883673656312, 0.09741659909541572, 0.08169330242755682, 0.06701156038972575, 0.05362618927683272, 0.04169510925834998, 0.031286932872005575, 0.022393467220454093, 0.014945189167037706, 0.00882783109678569, 0.003898482620247966, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y180_Q_wf_q2": {
            "type": "arbitrary",
            "samples": [0.0, 0.003898482620247966, 0.00882783109678569, 0.014945189167037706, 0.022393467220454093, 0.031286932872005575, 0.04169510925834998, 0.05362618927683272, 0.06701156038972575, 0.08169330242755682, 0.09741659909541572, 0.11382883673656312, 0.13048672437999825, 0.14687207025447396, 0.16241595024382866, 0.1765300044143878, 0.18864263131789072, 0.1982370608953941, 0.20488780808919338] + [0.20829193676209992] * 2 + [0.20488780808919338, 0.1982370608953941, 0.18864263131789072, 0.1765300044143878, 0.16241595024382866, 0.14687207025447396, 0.13048672437999825, 0.11382883673656312, 0.09741659909541572, 0.08169330242755682, 0.06701156038972575, 0.05362618927683272, 0.04169510925834998, 0.031286932872005575, 0.022393467220454093, 0.014945189167037706, 0.00882783109678569, 0.003898482620247966, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "__oct__readout_wf": {
            "type": "constant",
            "sample": 0.125,
        },
        "x90_Q_wf_q1": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y180_Q_wf_q1": {
            "type": "arbitrary",
            "samples": [0.0, 0.003898482620247966, 0.00882783109678569, 0.014945189167037706, 0.022393467220454093, 0.031286932872005575, 0.04169510925834998, 0.05362618927683272, 0.06701156038972575, 0.08169330242755682, 0.09741659909541572, 0.11382883673656312, 0.13048672437999825, 0.14687207025447396, 0.16241595024382866, 0.1765300044143878, 0.18864263131789072, 0.1982370608953941, 0.20488780808919338] + [0.20829193676209992] * 2 + [0.20488780808919338, 0.1982370608953941, 0.18864263131789072, 0.1765300044143878, 0.16241595024382866, 0.14687207025447396, 0.13048672437999825, 0.11382883673656312, 0.09741659909541572, 0.08169330242755682, 0.06701156038972575, 0.05362618927683272, 0.04169510925834998, 0.031286932872005575, 0.022393467220454093, 0.014945189167037706, 0.00882783109678569, 0.003898482620247966, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x90_Q_wf_q2": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x90_I_wf_q1": {
            "type": "arbitrary",
            "samples": [0.0, 0.001949241310123983, 0.004413915548392845, 0.007472594583518853, 0.011196733610227046, 0.015643466436002788, 0.02084755462917499, 0.02681309463841636, 0.033505780194862875, 0.04084665121377841, 0.04870829954770786, 0.05691441836828156, 0.06524336218999913, 0.07343603512723698, 0.08120797512191433, 0.0882650022071939, 0.09432131565894536, 0.09911853044769706, 0.10244390404459669] + [0.10414596838104996] * 2 + [0.10244390404459669, 0.09911853044769706, 0.09432131565894536, 0.0882650022071939, 0.08120797512191433, 0.07343603512723698, 0.06524336218999913, 0.05691441836828156, 0.04870829954770786, 0.04084665121377841, 0.033505780194862875, 0.02681309463841636, 0.02084755462917499, 0.015643466436002788, 0.011196733610227046, 0.007472594583518853, 0.004413915548392845, 0.001949241310123983, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y180_I_wf_q1": {
            "type": "arbitrary",
            "samples": [-0.0] * 40,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x90_I_wf_q2": {
            "type": "arbitrary",
            "samples": [0.0, 0.001949241310123983, 0.004413915548392845, 0.007472594583518853, 0.011196733610227046, 0.015643466436002788, 0.02084755462917499, 0.02681309463841636, 0.033505780194862875, 0.04084665121377841, 0.04870829954770786, 0.05691441836828156, 0.06524336218999913, 0.07343603512723698, 0.08120797512191433, 0.0882650022071939, 0.09432131565894536, 0.09911853044769706, 0.10244390404459669] + [0.10414596838104996] * 2 + [0.10244390404459669, 0.09911853044769706, 0.09432131565894536, 0.0882650022071939, 0.08120797512191433, 0.07343603512723698, 0.06524336218999913, 0.05691441836828156, 0.04870829954770786, 0.04084665121377841, 0.033505780194862875, 0.02681309463841636, 0.02084755462917499, 0.015643466436002788, 0.011196733610227046, 0.007472594583518853, 0.004413915548392845, 0.001949241310123983, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_x90_Q_wf_q1": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_x90_I_wf_q2": {
            "type": "arbitrary",
            "samples": [0.0, -0.001949241310123983, -0.004413915548392845, -0.007472594583518853, -0.011196733610227046, -0.015643466436002788, -0.02084755462917499, -0.02681309463841636, -0.033505780194862875, -0.04084665121377841, -0.04870829954770786, -0.05691441836828156, -0.06524336218999913, -0.07343603512723698, -0.08120797512191433, -0.0882650022071939, -0.09432131565894536, -0.09911853044769706, -0.10244390404459669] + [-0.10414596838104996] * 2 + [-0.10244390404459669, -0.09911853044769706, -0.09432131565894536, -0.0882650022071939, -0.08120797512191433, -0.07343603512723698, -0.06524336218999913, -0.05691441836828156, -0.04870829954770786, -0.04084665121377841, -0.033505780194862875, -0.02681309463841636, -0.02084755462917499, -0.015643466436002788, -0.011196733610227046, -0.007472594583518853, -0.004413915548392845, -0.001949241310123983, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_x90_I_wf_q1": {
            "type": "arbitrary",
            "samples": [0.0, -0.001949241310123983, -0.004413915548392845, -0.007472594583518853, -0.011196733610227046, -0.015643466436002788, -0.02084755462917499, -0.02681309463841636, -0.033505780194862875, -0.04084665121377841, -0.04870829954770786, -0.05691441836828156, -0.06524336218999913, -0.07343603512723698, -0.08120797512191433, -0.0882650022071939, -0.09432131565894536, -0.09911853044769706, -0.10244390404459669] + [-0.10414596838104996] * 2 + [-0.10244390404459669, -0.09911853044769706, -0.09432131565894536, -0.0882650022071939, -0.08120797512191433, -0.07343603512723698, -0.06524336218999913, -0.05691441836828156, -0.04870829954770786, -0.04084665121377841, -0.033505780194862875, -0.02681309463841636, -0.02084755462917499, -0.015643466436002788, -0.011196733610227046, -0.007472594583518853, -0.004413915548392845, -0.001949241310123983, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_x90_Q_wf_q2": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y180_I_wf_q2": {
            "type": "arbitrary",
            "samples": [-0.0] * 40,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x180_Q_wf_q1": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x180_Q_wf_q2": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "__oct__DC_offset_wf": {
            "type": "constant",
            "sample": 0.25,
        },
        "minus_y90_I_wf_q2": {
            "type": "arbitrary",
            "samples": [-0.0] * 40,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_y90_I_wf_q1": {
            "type": "arbitrary",
            "samples": [-0.0] * 40,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_y90_Q_wf_q2": {
            "type": "arbitrary",
            "samples": [0.0, -0.001949241310123983, -0.004413915548392845, -0.007472594583518853, -0.011196733610227046, -0.015643466436002788, -0.02084755462917499, -0.02681309463841636, -0.033505780194862875, -0.04084665121377841, -0.04870829954770786, -0.05691441836828156, -0.06524336218999913, -0.07343603512723698, -0.08120797512191433, -0.0882650022071939, -0.09432131565894536, -0.09911853044769706, -0.10244390404459669] + [-0.10414596838104996] * 2 + [-0.10244390404459669, -0.09911853044769706, -0.09432131565894536, -0.0882650022071939, -0.08120797512191433, -0.07343603512723698, -0.06524336218999913, -0.05691441836828156, -0.04870829954770786, -0.04084665121377841, -0.033505780194862875, -0.02681309463841636, -0.02084755462917499, -0.015643466436002788, -0.011196733610227046, -0.007472594583518853, -0.004413915548392845, -0.001949241310123983, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_y90_Q_wf_q1": {
            "type": "arbitrary",
            "samples": [0.0, -0.001949241310123983, -0.004413915548392845, -0.007472594583518853, -0.011196733610227046, -0.015643466436002788, -0.02084755462917499, -0.02681309463841636, -0.033505780194862875, -0.04084665121377841, -0.04870829954770786, -0.05691441836828156, -0.06524336218999913, -0.07343603512723698, -0.08120797512191433, -0.0882650022071939, -0.09432131565894536, -0.09911853044769706, -0.10244390404459669] + [-0.10414596838104996] * 2 + [-0.10244390404459669, -0.09911853044769706, -0.09432131565894536, -0.0882650022071939, -0.08120797512191433, -0.07343603512723698, -0.06524336218999913, -0.05691441836828156, -0.04870829954770786, -0.04084665121377841, -0.033505780194862875, -0.02681309463841636, -0.02084755462917499, -0.015643466436002788, -0.011196733610227046, -0.007472594583518853, -0.004413915548392845, -0.001949241310123983, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y90_Q_wf_q1": {
            "type": "arbitrary",
            "samples": [0.0, 0.001949241310123983, 0.004413915548392845, 0.007472594583518853, 0.011196733610227046, 0.015643466436002788, 0.02084755462917499, 0.02681309463841636, 0.033505780194862875, 0.04084665121377841, 0.04870829954770786, 0.05691441836828156, 0.06524336218999913, 0.07343603512723698, 0.08120797512191433, 0.0882650022071939, 0.09432131565894536, 0.09911853044769706, 0.10244390404459669] + [0.10414596838104996] * 2 + [0.10244390404459669, 0.09911853044769706, 0.09432131565894536, 0.0882650022071939, 0.08120797512191433, 0.07343603512723698, 0.06524336218999913, 0.05691441836828156, 0.04870829954770786, 0.04084665121377841, 0.033505780194862875, 0.02681309463841636, 0.02084755462917499, 0.015643466436002788, 0.011196733610227046, 0.007472594583518853, 0.004413915548392845, 0.001949241310123983, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y90_I_wf_q2": {
            "type": "arbitrary",
            "samples": [-0.0] * 40,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y90_I_wf_q1": {
            "type": "arbitrary",
            "samples": [-0.0] * 40,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y90_Q_wf_q2": {
            "type": "arbitrary",
            "samples": [0.0, 0.001949241310123983, 0.004413915548392845, 0.007472594583518853, 0.011196733610227046, 0.015643466436002788, 0.02084755462917499, 0.02681309463841636, 0.033505780194862875, 0.04084665121377841, 0.04870829954770786, 0.05691441836828156, 0.06524336218999913, 0.07343603512723698, 0.08120797512191433, 0.0882650022071939, 0.09432131565894536, 0.09911853044769706, 0.10244390404459669] + [0.10414596838104996] * 2 + [0.10244390404459669, 0.09911853044769706, 0.09432131565894536, 0.0882650022071939, 0.08120797512191433, 0.07343603512723698, 0.06524336218999913, 0.05691441836828156, 0.04870829954770786, 0.04084665121377841, 0.033505780194862875, 0.02681309463841636, 0.02084755462917499, 0.015643466436002788, 0.011196733610227046, 0.007472594583518853, 0.004413915548392845, 0.001949241310123983, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
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
        "opt_sine_weights_q1": {
            "cosine": [(0.0, 4000)],
            "sine": [(1.0, 4000)],
        },
        "opt_sine_weights_q2": {
            "cosine": [(0.0, 4000)],
            "sine": [(1.0, 4000)],
        },
        "sine_weights": {
            "cosine": [(0.0, 4000)],
            "sine": [(1.0, 4000)],
        },
        "rotated_minus_sine_weights_q1": {
            "cosine": [(0.0, 4000)],
            "sine": [(-1.0, 4000)],
        },
        "__oct__integW_cosine": {
            "cosine": [(1.0, 10000)],
            "sine": [(0.0, 10000)],
        },
        "rotated_minus_sine_weights_q2": {
            "cosine": [(0.0, 4000)],
            "sine": [(-1.0, 4000)],
        },
        "__oct__integW_sine": {
            "cosine": [(0.0, 10000)],
            "sine": [(1.0, 10000)],
        },
        "rotated_sine_weights_q1": {
            "cosine": [(0.0, 4000)],
            "sine": [(1.0, 4000)],
        },
        "rotated_cosine_weights_q2": {
            "cosine": [(1.0, 4000)],
            "sine": [(0.0, 4000)],
        },
        "rotated_cosine_weights_q1": {
            "cosine": [(1.0, 4000)],
            "sine": [(0.0, 4000)],
        },
        "rotated_sine_weights_q2": {
            "cosine": [(0.0, 4000)],
            "sine": [(1.0, 4000)],
        },
        "cosine_weights": {
            "cosine": [(1.0, 4000)],
            "sine": [(0.0, 4000)],
        },
        "__oct__integW_zero": {
            "cosine": [(0.0, 10000)],
            "sine": [(0.0, 10000)],
        },
        "opt_minus_sine_weights_q1": {
            "cosine": [(0.0, 4000)],
            "sine": [(-1.0, 4000)],
        },
        "opt_minus_sine_weights_q2": {
            "cosine": [(0.0, 4000)],
            "sine": [(-1.0, 4000)],
        },
        "minus_sine_weights": {
            "cosine": [(0.0, 4000)],
            "sine": [(-1.0, 4000)],
        },
        "opt_cosine_weights_q1": {
            "cosine": [(1.0, 4000)],
            "sine": [(0.0, 4000)],
        },
        "opt_cosine_weights_q2": {
            "cosine": [(1.0, 4000)],
            "sine": [(0.0, 4000)],
        },
        "__oct__integW_minus_sine": {
            "cosine": [(0.0, 10000)],
            "sine": [(-1.0, 10000)],
        },
    },
    "mixers": {
        "rr2_mixer_7b5": [{'intermediate_frequency': 133000000.0, 'lo_frequency': 5000000000.0, 'correction': (1.0, 0.0, 0.0, 1.0)}],
        "__oct__dummy_mixer": [
            {'intermediate_frequency': 50000000.0, 'lo_frequency': 6000000000.0, 'correction': (1.0, 0.0, 0.0, 1.0)},
            {'intermediate_frequency': 43000000.0, 'lo_frequency': 6000000000.0, 'correction': (1.0, 0.0, 0.0, 1.0)},
            {'intermediate_frequency': -7000000.0, 'lo_frequency': 6000000000.0, 'correction': (1.0, 0.0, 0.0, 1.0)},
            {'intermediate_frequency': -57000000.0, 'lo_frequency': 6000000000.0, 'correction': (1.0, 0.0, 0.0, 1.0)},
        ],
        "q1_xy_mixer_26d": [{'intermediate_frequency': 50000000.0, 'lo_frequency': 3950000000.0, 'correction': (1.0, 0.0, 0.0, 1.0)}],
        "q2_xy_mixer_ff0": [{'intermediate_frequency': 75000000.0, 'lo_frequency': 3950000000.0, 'correction': (1.0, 0.0, 0.0, 1.0)}],
        "rr1_mixer_d42": [{'intermediate_frequency': 75000000.0, 'lo_frequency': 5000000000.0, 'correction': (1.0, 0.0, 0.0, 1.0)}],
    },
}


