
# Single QUA script generated at 2025-05-13 07:04:17.191203
# QUA library version: 1.2.2

from qm import CompilerOptionArguments
from qm.qua import *

with program() as prog:
    v1 = declare(int, )
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
    with for_(v1,0,(v1<100),(v1+1)):
        r1 = declare_stream()
        save(v1, r1)
        reset_if_phase("q1.resonator")
        atr_r2 = declare_stream(adc_trace=True)
        measure("readout", "q1.resonator", dual_demod.full("iw1", "iw2", v2), dual_demod.full("iw3", "iw1", v3), adc_stream=atr_r2)
        wait(1000, "q1.resonator")
        reset_if_phase("q2.resonator")
        atr_r3 = declare_stream(adc_trace=True)
        measure("readout", "q2.resonator", dual_demod.full("iw1", "iw2", v4), dual_demod.full("iw3", "iw1", v5), adc_stream=atr_r3)
        wait(1000, "q2.resonator")
        reset_if_phase("q3.resonator")
        atr_r4 = declare_stream(adc_trace=True)
        measure("readout", "q3.resonator", dual_demod.full("iw1", "iw2", v6), dual_demod.full("iw3", "iw1", v7), adc_stream=atr_r4)
        wait(1000, "q3.resonator")
        reset_if_phase("q4.resonator")
        atr_r5 = declare_stream(adc_trace=True)
        measure("readout", "q4.resonator", dual_demod.full("iw1", "iw2", v8), dual_demod.full("iw3", "iw1", v9), adc_stream=atr_r5)
        wait(1000, "q4.resonator")
        reset_if_phase("q5.resonator")
        atr_r6 = declare_stream(adc_trace=True)
        measure("readout", "q5.resonator", dual_demod.full("iw1", "iw2", v10), dual_demod.full("iw3", "iw1", v11), adc_stream=atr_r6)
        wait(1000, "q5.resonator")
        reset_if_phase("q6.resonator")
        atr_r7 = declare_stream(adc_trace=True)
        measure("readout", "q6.resonator", dual_demod.full("iw1", "iw2", v12), dual_demod.full("iw3", "iw1", v13), adc_stream=atr_r7)
        wait(1000, "q6.resonator")
        reset_if_phase("q7.resonator")
        atr_r8 = declare_stream(adc_trace=True)
        measure("readout", "q7.resonator", dual_demod.full("iw1", "iw2", v14), dual_demod.full("iw3", "iw1", v15), adc_stream=atr_r8)
        wait(1000, "q7.resonator")
        reset_if_phase("q8.resonator")
        atr_r9 = declare_stream(adc_trace=True)
        measure("readout", "q8.resonator", dual_demod.full("iw1", "iw2", v16), dual_demod.full("iw3", "iw1", v17), adc_stream=atr_r9)
        wait(1000, "q8.resonator")
        align()
    with stream_processing():
        r1.save("n")
        atr_r2.input2().real().average().save("adcI1")
        atr_r2.input2().image().average().save("adcQ1")
        atr_r2.input2().real().save("adc_single_runI1")
        atr_r2.input2().image().save("adc_single_runQ1")
        atr_r3.input2().real().average().save("adcI2")
        atr_r3.input2().image().average().save("adcQ2")
        atr_r3.input2().real().save("adc_single_runI2")
        atr_r3.input2().image().save("adc_single_runQ2")
        atr_r4.input2().real().average().save("adcI3")
        atr_r4.input2().image().average().save("adcQ3")
        atr_r4.input2().real().save("adc_single_runI3")
        atr_r4.input2().image().save("adc_single_runQ3")
        atr_r5.input2().real().average().save("adcI4")
        atr_r5.input2().image().average().save("adcQ4")
        atr_r5.input2().real().save("adc_single_runI4")
        atr_r5.input2().image().save("adc_single_runQ4")
        atr_r6.input2().real().average().save("adcI5")
        atr_r6.input2().image().average().save("adcQ5")
        atr_r6.input2().real().save("adc_single_runI5")
        atr_r6.input2().image().save("adc_single_runQ5")
        atr_r7.input2().real().average().save("adcI6")
        atr_r7.input2().image().average().save("adcQ6")
        atr_r7.input2().real().save("adc_single_runI6")
        atr_r7.input2().image().save("adc_single_runQ6")
        atr_r8.input2().real().average().save("adcI7")
        atr_r8.input2().image().average().save("adcQ7")
        atr_r8.input2().real().save("adc_single_runI7")
        atr_r8.input2().image().save("adc_single_runQ7")
        atr_r9.input2().real().average().save("adcI8")
        atr_r9.input2().image().average().save("adcQ8")
        atr_r9.input2().real().save("adc_single_runI8")
        atr_r9.input2().image().save("adc_single_runQ8")


config = {
    "version": 1,
    "controllers": {
        "con1": {
            "fems": {
                "1": {
                    "type": "MW",
                    "analog_outputs": {
                        "1": {
                            "band": 1,
                            "delay": 0,
                            "shareable": False,
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": -2,
                            "upconverter_frequency": 4750000000,
                        },
                    },
                    "analog_inputs": {
                        "2": {
                            "band": 1,
                            "downconverter_frequency": 4750000000,
                            "sampling_rate": 1000000000.0,
                            "shareable": False,
                        },
                    },
                },
                "2": {
                    "type": "MW",
                    "analog_outputs": {
                        "1": {
                            "band": 2,
                            "delay": 0,
                            "shareable": False,
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": -2,
                            "upconverter_frequency": 6000000000.0,
                        },
                        "2": {
                            "band": 2,
                            "delay": 0,
                            "shareable": False,
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": -2,
                            "upconverter_frequency": 6100000000.0,
                        },
                        "3": {
                            "band": 2,
                            "delay": 0,
                            "shareable": False,
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": -2,
                            "upconverter_frequency": 6500000000.0,
                        },
                        "4": {
                            "band": 2,
                            "delay": 0,
                            "shareable": False,
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": -2,
                            "upconverter_frequency": 6800000000.0,
                        },
                        "5": {
                            "band": 2,
                            "delay": 0,
                            "shareable": False,
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": -2,
                            "upconverter_frequency": 7100000000.0,
                        },
                        "6": {
                            "band": 2,
                            "delay": 0,
                            "shareable": False,
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": -2,
                            "upconverter_frequency": 7100000000.0,
                        },
                        "7": {
                            "band": 2,
                            "delay": 0,
                            "shareable": False,
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": -2,
                            "upconverter_frequency": 7100000000.0,
                        },
                        "8": {
                            "band": 2,
                            "delay": 0,
                            "shareable": False,
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": -2,
                            "upconverter_frequency": 7100000000.0,
                        },
                    },
                },
            },
        },
    },
    "elements": {
        "q1.xy": {
            "operations": {
                "saturation": "q1.xy.saturation.pulse",
                "x180_DragCosine": "q1.xy.x180_DragCosine.pulse",
                "x90_DragCosine": "q1.xy.x90_DragCosine.pulse",
                "-x90_DragCosine": "q1.xy.-x90_DragCosine.pulse",
                "y180_DragCosine": "q1.xy.y180_DragCosine.pulse",
                "y90_DragCosine": "q1.xy.y90_DragCosine.pulse",
                "-y90_DragCosine": "q1.xy.-y90_DragCosine.pulse",
                "x180": "q1.xy.x180_DragCosine.pulse",
                "x90": "q1.xy.x90_DragCosine.pulse",
                "-x90": "q1.xy.-x90_DragCosine.pulse",
                "y180": "q1.xy.y180_DragCosine.pulse",
                "y90": "q1.xy.y90_DragCosine.pulse",
                "-y90": "q1.xy.-y90_DragCosine.pulse",
                "const": "q1.xy.const.pulse",
            },
            "intermediate_frequency": 12000000.0,
            "MWInput": {
                "port": ('con1', 2, 1),
                "upconverter": 1,
            },
        },
        "q1.resonator": {
            "operations": {
                "readout": "q1.resonator.readout.pulse",
                "const": "q1.resonator.const.pulse",
            },
            "intermediate_frequency": -355000000.0,
            "MWOutput": {
                "port": ('con1', 1, 2),
            },
            "smearing": 0,
            "time_of_flight": 28,
            "MWInput": {
                "port": ('con1', 1, 1),
                "upconverter": 1,
            },
        },
        "q2.xy": {
            "operations": {
                "saturation": "q2.xy.saturation.pulse",
                "x180_DragCosine": "q2.xy.x180_DragCosine.pulse",
                "x90_DragCosine": "q2.xy.x90_DragCosine.pulse",
                "-x90_DragCosine": "q2.xy.-x90_DragCosine.pulse",
                "y180_DragCosine": "q2.xy.y180_DragCosine.pulse",
                "y90_DragCosine": "q2.xy.y90_DragCosine.pulse",
                "-y90_DragCosine": "q2.xy.-y90_DragCosine.pulse",
                "x180": "q2.xy.x180_DragCosine.pulse",
                "x90": "q2.xy.x90_DragCosine.pulse",
                "-x90": "q2.xy.-x90_DragCosine.pulse",
                "y180": "q2.xy.y180_DragCosine.pulse",
                "y90": "q2.xy.y90_DragCosine.pulse",
                "-y90": "q2.xy.-y90_DragCosine.pulse",
                "const": "q2.xy.const.pulse",
            },
            "intermediate_frequency": 321000000.0,
            "MWInput": {
                "port": ('con1', 2, 2),
                "upconverter": 1,
            },
        },
        "q2.resonator": {
            "operations": {
                "readout": "q2.resonator.readout.pulse",
                "const": "q2.resonator.const.pulse",
            },
            "intermediate_frequency": -338000000.0,
            "MWOutput": {
                "port": ('con1', 1, 2),
            },
            "smearing": 0,
            "time_of_flight": 28,
            "MWInput": {
                "port": ('con1', 1, 1),
                "upconverter": 1,
            },
        },
        "q3.xy": {
            "operations": {
                "saturation": "q3.xy.saturation.pulse",
                "x180_DragCosine": "q3.xy.x180_DragCosine.pulse",
                "x90_DragCosine": "q3.xy.x90_DragCosine.pulse",
                "-x90_DragCosine": "q3.xy.-x90_DragCosine.pulse",
                "y180_DragCosine": "q3.xy.y180_DragCosine.pulse",
                "y90_DragCosine": "q3.xy.y90_DragCosine.pulse",
                "-y90_DragCosine": "q3.xy.-y90_DragCosine.pulse",
                "x180": "q3.xy.x180_DragCosine.pulse",
                "x90": "q3.xy.x90_DragCosine.pulse",
                "-x90": "q3.xy.-x90_DragCosine.pulse",
                "y180": "q3.xy.y180_DragCosine.pulse",
                "y90": "q3.xy.y90_DragCosine.pulse",
                "-y90": "q3.xy.-y90_DragCosine.pulse",
                "const": "q3.xy.const.pulse",
            },
            "intermediate_frequency": 285000000.0,
            "MWInput": {
                "port": ('con1', 2, 3),
                "upconverter": 1,
            },
        },
        "q3.resonator": {
            "operations": {
                "readout": "q3.resonator.readout.pulse",
                "const": "q3.resonator.const.pulse",
            },
            "intermediate_frequency": -229000000.0,
            "MWOutput": {
                "port": ('con1', 1, 2),
            },
            "smearing": 0,
            "time_of_flight": 28,
            "MWInput": {
                "port": ('con1', 1, 1),
                "upconverter": 1,
            },
        },
        "q4.xy": {
            "operations": {
                "saturation": "q4.xy.saturation.pulse",
                "x180_DragCosine": "q4.xy.x180_DragCosine.pulse",
                "x90_DragCosine": "q4.xy.x90_DragCosine.pulse",
                "-x90_DragCosine": "q4.xy.-x90_DragCosine.pulse",
                "y180_DragCosine": "q4.xy.y180_DragCosine.pulse",
                "y90_DragCosine": "q4.xy.y90_DragCosine.pulse",
                "-y90_DragCosine": "q4.xy.-y90_DragCosine.pulse",
                "x180": "q4.xy.x180_DragCosine.pulse",
                "x90": "q4.xy.x90_DragCosine.pulse",
                "-x90": "q4.xy.-x90_DragCosine.pulse",
                "y180": "q4.xy.y180_DragCosine.pulse",
                "y90": "q4.xy.y90_DragCosine.pulse",
                "-y90": "q4.xy.-y90_DragCosine.pulse",
                "const": "q4.xy.const.pulse",
            },
            "intermediate_frequency": 201000000.0,
            "MWInput": {
                "port": ('con1', 2, 4),
                "upconverter": 1,
            },
        },
        "q4.resonator": {
            "operations": {
                "readout": "q4.resonator.readout.pulse",
                "const": "q4.resonator.const.pulse",
            },
            "intermediate_frequency": -22000000.0,
            "MWOutput": {
                "port": ('con1', 1, 2),
            },
            "smearing": 0,
            "time_of_flight": 28,
            "MWInput": {
                "port": ('con1', 1, 1),
                "upconverter": 1,
            },
        },
        "q5.xy": {
            "operations": {
                "saturation": "q5.xy.saturation.pulse",
                "x180_DragCosine": "q5.xy.x180_DragCosine.pulse",
                "x90_DragCosine": "q5.xy.x90_DragCosine.pulse",
                "-x90_DragCosine": "q5.xy.-x90_DragCosine.pulse",
                "y180_DragCosine": "q5.xy.y180_DragCosine.pulse",
                "y90_DragCosine": "q5.xy.y90_DragCosine.pulse",
                "-y90_DragCosine": "q5.xy.-y90_DragCosine.pulse",
                "x180": "q5.xy.x180_DragCosine.pulse",
                "x90": "q5.xy.x90_DragCosine.pulse",
                "-x90": "q5.xy.-x90_DragCosine.pulse",
                "y180": "q5.xy.y180_DragCosine.pulse",
                "y90": "q5.xy.y90_DragCosine.pulse",
                "-y90": "q5.xy.-y90_DragCosine.pulse",
                "const": "q5.xy.const.pulse",
            },
            "intermediate_frequency": -17000000.0,
            "MWInput": {
                "port": ('con1', 2, 5),
                "upconverter": 1,
            },
        },
        "q5.resonator": {
            "operations": {
                "readout": "q5.resonator.readout.pulse",
                "const": "q5.resonator.const.pulse",
            },
            "intermediate_frequency": 165000000.0,
            "MWOutput": {
                "port": ('con1', 1, 2),
            },
            "smearing": 0,
            "time_of_flight": 28,
            "MWInput": {
                "port": ('con1', 1, 1),
                "upconverter": 1,
            },
        },
        "q6.xy": {
            "operations": {
                "saturation": "q6.xy.saturation.pulse",
                "x180_DragCosine": "q6.xy.x180_DragCosine.pulse",
                "x90_DragCosine": "q6.xy.x90_DragCosine.pulse",
                "-x90_DragCosine": "q6.xy.-x90_DragCosine.pulse",
                "y180_DragCosine": "q6.xy.y180_DragCosine.pulse",
                "y90_DragCosine": "q6.xy.y90_DragCosine.pulse",
                "-y90_DragCosine": "q6.xy.-y90_DragCosine.pulse",
                "x180": "q6.xy.x180_DragCosine.pulse",
                "x90": "q6.xy.x90_DragCosine.pulse",
                "-x90": "q6.xy.-x90_DragCosine.pulse",
                "y180": "q6.xy.y180_DragCosine.pulse",
                "y90": "q6.xy.y90_DragCosine.pulse",
                "-y90": "q6.xy.-y90_DragCosine.pulse",
                "const": "q6.xy.const.pulse",
            },
            "intermediate_frequency": 21000000.0,
            "MWInput": {
                "port": ('con1', 2, 6),
                "upconverter": 1,
            },
        },
        "q6.resonator": {
            "operations": {
                "readout": "q6.resonator.readout.pulse",
                "const": "q6.resonator.const.pulse",
            },
            "intermediate_frequency": 250000000.0,
            "MWOutput": {
                "port": ('con1', 1, 2),
            },
            "smearing": 0,
            "time_of_flight": 28,
            "MWInput": {
                "port": ('con1', 1, 1),
                "upconverter": 1,
            },
        },
        "q7.xy": {
            "operations": {
                "saturation": "q7.xy.saturation.pulse",
                "x180_DragCosine": "q7.xy.x180_DragCosine.pulse",
                "x90_DragCosine": "q7.xy.x90_DragCosine.pulse",
                "-x90_DragCosine": "q7.xy.-x90_DragCosine.pulse",
                "y180_DragCosine": "q7.xy.y180_DragCosine.pulse",
                "y90_DragCosine": "q7.xy.y90_DragCosine.pulse",
                "-y90_DragCosine": "q7.xy.-y90_DragCosine.pulse",
                "x180": "q7.xy.x180_DragCosine.pulse",
                "x90": "q7.xy.x90_DragCosine.pulse",
                "-x90": "q7.xy.-x90_DragCosine.pulse",
                "y180": "q7.xy.y180_DragCosine.pulse",
                "y90": "q7.xy.y90_DragCosine.pulse",
                "-y90": "q7.xy.-y90_DragCosine.pulse",
                "const": "q7.xy.const.pulse",
            },
            "intermediate_frequency": 84000000.0,
            "MWInput": {
                "port": ('con1', 2, 7),
                "upconverter": 1,
            },
        },
        "q7.resonator": {
            "operations": {
                "readout": "q7.resonator.readout.pulse",
                "const": "q7.resonator.const.pulse",
            },
            "intermediate_frequency": 312500000.0,
            "MWOutput": {
                "port": ('con1', 1, 2),
            },
            "smearing": 0,
            "time_of_flight": 28,
            "MWInput": {
                "port": ('con1', 1, 1),
                "upconverter": 1,
            },
        },
        "q8.xy": {
            "operations": {
                "saturation": "q8.xy.saturation.pulse",
                "x180_DragCosine": "q8.xy.x180_DragCosine.pulse",
                "x90_DragCosine": "q8.xy.x90_DragCosine.pulse",
                "-x90_DragCosine": "q8.xy.-x90_DragCosine.pulse",
                "y180_DragCosine": "q8.xy.y180_DragCosine.pulse",
                "y90_DragCosine": "q8.xy.y90_DragCosine.pulse",
                "-y90_DragCosine": "q8.xy.-y90_DragCosine.pulse",
                "x180": "q8.xy.x180_DragCosine.pulse",
                "x90": "q8.xy.x90_DragCosine.pulse",
                "-x90": "q8.xy.-x90_DragCosine.pulse",
                "y180": "q8.xy.y180_DragCosine.pulse",
                "y90": "q8.xy.y90_DragCosine.pulse",
                "-y90": "q8.xy.-y90_DragCosine.pulse",
                "const": "q8.xy.const.pulse",
            },
            "intermediate_frequency": 154000000.0,
            "MWInput": {
                "port": ('con1', 2, 8),
                "upconverter": 1,
            },
        },
        "q8.resonator": {
            "operations": {
                "readout": "q8.resonator.readout.pulse",
                "const": "q8.resonator.const.pulse",
            },
            "intermediate_frequency": 350000000.0,
            "MWOutput": {
                "port": ('con1', 1, 2),
            },
            "smearing": 0,
            "time_of_flight": 28,
            "MWInput": {
                "port": ('con1', 1, 1),
                "upconverter": 1,
            },
        },
        "cr_q1_q2": {
            "operations": {
                "square": "cr_q1_q2.square.pulse",
            },
            "MWInput": {
                "port": ('con1', 2, 1),
                "upconverter": 1,
            },
        },
        "cr_q5_q4": {
            "operations": {
                "square": "cr_q5_q4.square.pulse",
            },
            "MWInput": {
                "port": ('con1', 2, 5),
                "upconverter": 1,
            },
        },
        "zz_q5_q4": {
            "operations": {
                "square": "zz_q5_q4.square.pulse",
            },
            "MWInput": {
                "port": ('con1', 2, 1),
                "upconverter": 1,
            },
        },
        "cr_q2_q1": {
            "operations": {
                "square": "cr_q2_q1.square.pulse",
            },
            "MWInput": {
                "port": ('con1', 2, 2),
                "upconverter": 1,
            },
        },
        "cr_q2_q3": {
            "operations": {
                "square": "cr_q2_q3.square.pulse",
            },
            "MWInput": {
                "port": ('con1', 2, 2),
                "upconverter": 1,
            },
        },
        "cr_q3_q2": {
            "operations": {
                "square": "cr_q3_q2.square.pulse",
            },
            "MWInput": {
                "port": ('con1', 2, 3),
                "upconverter": 1,
            },
        },
        "cr_q3_q4": {
            "operations": {
                "square": "cr_q3_q4.square.pulse",
            },
            "MWInput": {
                "port": ('con1', 2, 3),
                "upconverter": 1,
            },
        },
        "cr_q4_q3": {
            "operations": {
                "square": "cr_q4_q3.square.pulse",
            },
            "MWInput": {
                "port": ('con1', 2, 4),
                "upconverter": 1,
            },
        },
        "cr_q4_q5": {
            "operations": {
                "square": "cr_q4_q5.square.pulse",
            },
            "MWInput": {
                "port": ('con1', 2, 4),
                "upconverter": 1,
            },
        },
        "cr_q5_q6": {
            "operations": {
                "square": "cr_q5_q6.square.pulse",
            },
            "MWInput": {
                "port": ('con1', 2, 5),
                "upconverter": 1,
            },
        },
        "cr_q6_q5": {
            "operations": {
                "square": "cr_q6_q5.square.pulse",
            },
            "MWInput": {
                "port": ('con1', 2, 6),
                "upconverter": 1,
            },
        },
        "cr_q6_q7": {
            "operations": {
                "square": "cr_q6_q7.square.pulse",
            },
            "MWInput": {
                "port": ('con1', 2, 6),
                "upconverter": 1,
            },
        },
        "cr_q7_q6": {
            "operations": {
                "square": "cr_q7_q6.square.pulse",
            },
            "MWInput": {
                "port": ('con1', 2, 7),
                "upconverter": 1,
            },
        },
        "cr_q7_q8": {
            "operations": {
                "square": "cr_q7_q8.square.pulse",
            },
            "MWInput": {
                "port": ('con1', 2, 7),
                "upconverter": 1,
            },
        },
        "cr_q8_q7": {
            "operations": {
                "square": "cr_q8_q7.square.pulse",
            },
            "MWInput": {
                "port": ('con1', 2, 8),
                "upconverter": 1,
            },
        },
        "cr_q8_q1": {
            "operations": {
                "square": "cr_q8_q1.square.pulse",
            },
            "MWInput": {
                "port": ('con1', 2, 8),
                "upconverter": 1,
            },
        },
        "cr_q1_q8": {
            "operations": {
                "square": "cr_q1_q8.square.pulse",
            },
            "MWInput": {
                "port": ('con1', 2, 1),
                "upconverter": 1,
            },
        },
    },
    "pulses": {
        "const_pulse": {
            "operation": "control",
            "length": 1000,
            "waveforms": {
                "I": "const_wf",
                "Q": "zero_wf",
            },
        },
        "q1.xy.saturation.pulse": {
            "operation": "control",
            "length": 20000,
            "waveforms": {
                "I": "q1.xy.saturation.wf.I",
                "Q": "q1.xy.saturation.wf.Q",
            },
        },
        "q1.xy.x180_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "q1.xy.x180_DragCosine.wf.I",
                "Q": "q1.xy.x180_DragCosine.wf.Q",
            },
        },
        "q1.xy.x90_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "q1.xy.x90_DragCosine.wf.I",
                "Q": "q1.xy.x90_DragCosine.wf.Q",
            },
        },
        "q1.xy.-x90_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "q1.xy.-x90_DragCosine.wf.I",
                "Q": "q1.xy.-x90_DragCosine.wf.Q",
            },
        },
        "q1.xy.y180_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "q1.xy.y180_DragCosine.wf.I",
                "Q": "q1.xy.y180_DragCosine.wf.Q",
            },
        },
        "q1.xy.y90_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "q1.xy.y90_DragCosine.wf.I",
                "Q": "q1.xy.y90_DragCosine.wf.Q",
            },
        },
        "q1.xy.-y90_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "q1.xy.-y90_DragCosine.wf.I",
                "Q": "q1.xy.-y90_DragCosine.wf.Q",
            },
        },
        "q1.xy.const.pulse": {
            "operation": "control",
            "length": 1000,
            "waveforms": {
                "I": "q1.xy.const.wf.I",
                "Q": "q1.xy.const.wf.Q",
            },
        },
        "q1.resonator.readout.pulse": {
            "operation": "measurement",
            "length": 1000,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q1.resonator.readout.wf.I",
                "Q": "q1.resonator.readout.wf.Q",
            },
            "integration_weights": {
                "iw1": "q1.resonator.readout.iw1",
                "iw2": "q1.resonator.readout.iw2",
                "iw3": "q1.resonator.readout.iw3",
            },
        },
        "q1.resonator.const.pulse": {
            "operation": "control",
            "length": 1000,
            "waveforms": {
                "I": "q1.resonator.const.wf.I",
                "Q": "q1.resonator.const.wf.Q",
            },
        },
        "q2.xy.saturation.pulse": {
            "operation": "control",
            "length": 20000,
            "waveforms": {
                "I": "q2.xy.saturation.wf.I",
                "Q": "q2.xy.saturation.wf.Q",
            },
        },
        "q2.xy.x180_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "q2.xy.x180_DragCosine.wf.I",
                "Q": "q2.xy.x180_DragCosine.wf.Q",
            },
        },
        "q2.xy.x90_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "q2.xy.x90_DragCosine.wf.I",
                "Q": "q2.xy.x90_DragCosine.wf.Q",
            },
        },
        "q2.xy.-x90_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "q2.xy.-x90_DragCosine.wf.I",
                "Q": "q2.xy.-x90_DragCosine.wf.Q",
            },
        },
        "q2.xy.y180_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "q2.xy.y180_DragCosine.wf.I",
                "Q": "q2.xy.y180_DragCosine.wf.Q",
            },
        },
        "q2.xy.y90_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "q2.xy.y90_DragCosine.wf.I",
                "Q": "q2.xy.y90_DragCosine.wf.Q",
            },
        },
        "q2.xy.-y90_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "q2.xy.-y90_DragCosine.wf.I",
                "Q": "q2.xy.-y90_DragCosine.wf.Q",
            },
        },
        "q2.xy.const.pulse": {
            "operation": "control",
            "length": 1000,
            "waveforms": {
                "I": "q2.xy.const.wf.I",
                "Q": "q2.xy.const.wf.Q",
            },
        },
        "q2.resonator.readout.pulse": {
            "operation": "measurement",
            "length": 1000,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q2.resonator.readout.wf.I",
                "Q": "q2.resonator.readout.wf.Q",
            },
            "integration_weights": {
                "iw1": "q2.resonator.readout.iw1",
                "iw2": "q2.resonator.readout.iw2",
                "iw3": "q2.resonator.readout.iw3",
            },
        },
        "q2.resonator.const.pulse": {
            "operation": "control",
            "length": 1000,
            "waveforms": {
                "I": "q2.resonator.const.wf.I",
                "Q": "q2.resonator.const.wf.Q",
            },
        },
        "q3.xy.saturation.pulse": {
            "operation": "control",
            "length": 20000,
            "waveforms": {
                "I": "q3.xy.saturation.wf.I",
                "Q": "q3.xy.saturation.wf.Q",
            },
        },
        "q3.xy.x180_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "q3.xy.x180_DragCosine.wf.I",
                "Q": "q3.xy.x180_DragCosine.wf.Q",
            },
        },
        "q3.xy.x90_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "q3.xy.x90_DragCosine.wf.I",
                "Q": "q3.xy.x90_DragCosine.wf.Q",
            },
        },
        "q3.xy.-x90_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "q3.xy.-x90_DragCosine.wf.I",
                "Q": "q3.xy.-x90_DragCosine.wf.Q",
            },
        },
        "q3.xy.y180_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "q3.xy.y180_DragCosine.wf.I",
                "Q": "q3.xy.y180_DragCosine.wf.Q",
            },
        },
        "q3.xy.y90_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "q3.xy.y90_DragCosine.wf.I",
                "Q": "q3.xy.y90_DragCosine.wf.Q",
            },
        },
        "q3.xy.-y90_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "q3.xy.-y90_DragCosine.wf.I",
                "Q": "q3.xy.-y90_DragCosine.wf.Q",
            },
        },
        "q3.xy.const.pulse": {
            "operation": "control",
            "length": 1000,
            "waveforms": {
                "I": "q3.xy.const.wf.I",
                "Q": "q3.xy.const.wf.Q",
            },
        },
        "q3.resonator.readout.pulse": {
            "operation": "measurement",
            "length": 1000,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q3.resonator.readout.wf.I",
                "Q": "q3.resonator.readout.wf.Q",
            },
            "integration_weights": {
                "iw1": "q3.resonator.readout.iw1",
                "iw2": "q3.resonator.readout.iw2",
                "iw3": "q3.resonator.readout.iw3",
            },
        },
        "q3.resonator.const.pulse": {
            "operation": "control",
            "length": 1000,
            "waveforms": {
                "I": "q3.resonator.const.wf.I",
                "Q": "q3.resonator.const.wf.Q",
            },
        },
        "q4.xy.saturation.pulse": {
            "operation": "control",
            "length": 20000,
            "waveforms": {
                "I": "q4.xy.saturation.wf.I",
                "Q": "q4.xy.saturation.wf.Q",
            },
        },
        "q4.xy.x180_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "q4.xy.x180_DragCosine.wf.I",
                "Q": "q4.xy.x180_DragCosine.wf.Q",
            },
        },
        "q4.xy.x90_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "q4.xy.x90_DragCosine.wf.I",
                "Q": "q4.xy.x90_DragCosine.wf.Q",
            },
        },
        "q4.xy.-x90_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "q4.xy.-x90_DragCosine.wf.I",
                "Q": "q4.xy.-x90_DragCosine.wf.Q",
            },
        },
        "q4.xy.y180_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "q4.xy.y180_DragCosine.wf.I",
                "Q": "q4.xy.y180_DragCosine.wf.Q",
            },
        },
        "q4.xy.y90_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "q4.xy.y90_DragCosine.wf.I",
                "Q": "q4.xy.y90_DragCosine.wf.Q",
            },
        },
        "q4.xy.-y90_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "q4.xy.-y90_DragCosine.wf.I",
                "Q": "q4.xy.-y90_DragCosine.wf.Q",
            },
        },
        "q4.xy.const.pulse": {
            "operation": "control",
            "length": 1000,
            "waveforms": {
                "I": "q4.xy.const.wf.I",
                "Q": "q4.xy.const.wf.Q",
            },
        },
        "q4.resonator.readout.pulse": {
            "operation": "measurement",
            "length": 1000,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q4.resonator.readout.wf.I",
                "Q": "q4.resonator.readout.wf.Q",
            },
            "integration_weights": {
                "iw1": "q4.resonator.readout.iw1",
                "iw2": "q4.resonator.readout.iw2",
                "iw3": "q4.resonator.readout.iw3",
            },
        },
        "q4.resonator.const.pulse": {
            "operation": "control",
            "length": 1000,
            "waveforms": {
                "I": "q4.resonator.const.wf.I",
                "Q": "q4.resonator.const.wf.Q",
            },
        },
        "q5.xy.saturation.pulse": {
            "operation": "control",
            "length": 20000,
            "waveforms": {
                "I": "q5.xy.saturation.wf.I",
                "Q": "q5.xy.saturation.wf.Q",
            },
        },
        "q5.xy.x180_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "q5.xy.x180_DragCosine.wf.I",
                "Q": "q5.xy.x180_DragCosine.wf.Q",
            },
        },
        "q5.xy.x90_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "q5.xy.x90_DragCosine.wf.I",
                "Q": "q5.xy.x90_DragCosine.wf.Q",
            },
        },
        "q5.xy.-x90_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "q5.xy.-x90_DragCosine.wf.I",
                "Q": "q5.xy.-x90_DragCosine.wf.Q",
            },
        },
        "q5.xy.y180_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "q5.xy.y180_DragCosine.wf.I",
                "Q": "q5.xy.y180_DragCosine.wf.Q",
            },
        },
        "q5.xy.y90_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "q5.xy.y90_DragCosine.wf.I",
                "Q": "q5.xy.y90_DragCosine.wf.Q",
            },
        },
        "q5.xy.-y90_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "q5.xy.-y90_DragCosine.wf.I",
                "Q": "q5.xy.-y90_DragCosine.wf.Q",
            },
        },
        "q5.xy.const.pulse": {
            "operation": "control",
            "length": 1000,
            "waveforms": {
                "I": "q5.xy.const.wf.I",
                "Q": "q5.xy.const.wf.Q",
            },
        },
        "q5.resonator.readout.pulse": {
            "operation": "measurement",
            "length": 1000,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q5.resonator.readout.wf.I",
                "Q": "q5.resonator.readout.wf.Q",
            },
            "integration_weights": {
                "iw1": "q5.resonator.readout.iw1",
                "iw2": "q5.resonator.readout.iw2",
                "iw3": "q5.resonator.readout.iw3",
            },
        },
        "q5.resonator.const.pulse": {
            "operation": "control",
            "length": 1000,
            "waveforms": {
                "I": "q5.resonator.const.wf.I",
                "Q": "q5.resonator.const.wf.Q",
            },
        },
        "q6.xy.saturation.pulse": {
            "operation": "control",
            "length": 20000,
            "waveforms": {
                "I": "q6.xy.saturation.wf.I",
                "Q": "q6.xy.saturation.wf.Q",
            },
        },
        "q6.xy.x180_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "q6.xy.x180_DragCosine.wf.I",
                "Q": "q6.xy.x180_DragCosine.wf.Q",
            },
        },
        "q6.xy.x90_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "q6.xy.x90_DragCosine.wf.I",
                "Q": "q6.xy.x90_DragCosine.wf.Q",
            },
        },
        "q6.xy.-x90_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "q6.xy.-x90_DragCosine.wf.I",
                "Q": "q6.xy.-x90_DragCosine.wf.Q",
            },
        },
        "q6.xy.y180_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "q6.xy.y180_DragCosine.wf.I",
                "Q": "q6.xy.y180_DragCosine.wf.Q",
            },
        },
        "q6.xy.y90_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "q6.xy.y90_DragCosine.wf.I",
                "Q": "q6.xy.y90_DragCosine.wf.Q",
            },
        },
        "q6.xy.-y90_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "q6.xy.-y90_DragCosine.wf.I",
                "Q": "q6.xy.-y90_DragCosine.wf.Q",
            },
        },
        "q6.xy.const.pulse": {
            "operation": "control",
            "length": 1000,
            "waveforms": {
                "I": "q6.xy.const.wf.I",
                "Q": "q6.xy.const.wf.Q",
            },
        },
        "q6.resonator.readout.pulse": {
            "operation": "measurement",
            "length": 1000,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q6.resonator.readout.wf.I",
                "Q": "q6.resonator.readout.wf.Q",
            },
            "integration_weights": {
                "iw1": "q6.resonator.readout.iw1",
                "iw2": "q6.resonator.readout.iw2",
                "iw3": "q6.resonator.readout.iw3",
            },
        },
        "q6.resonator.const.pulse": {
            "operation": "control",
            "length": 1000,
            "waveforms": {
                "I": "q6.resonator.const.wf.I",
                "Q": "q6.resonator.const.wf.Q",
            },
        },
        "q7.xy.saturation.pulse": {
            "operation": "control",
            "length": 20000,
            "waveforms": {
                "I": "q7.xy.saturation.wf.I",
                "Q": "q7.xy.saturation.wf.Q",
            },
        },
        "q7.xy.x180_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "q7.xy.x180_DragCosine.wf.I",
                "Q": "q7.xy.x180_DragCosine.wf.Q",
            },
        },
        "q7.xy.x90_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "q7.xy.x90_DragCosine.wf.I",
                "Q": "q7.xy.x90_DragCosine.wf.Q",
            },
        },
        "q7.xy.-x90_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "q7.xy.-x90_DragCosine.wf.I",
                "Q": "q7.xy.-x90_DragCosine.wf.Q",
            },
        },
        "q7.xy.y180_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "q7.xy.y180_DragCosine.wf.I",
                "Q": "q7.xy.y180_DragCosine.wf.Q",
            },
        },
        "q7.xy.y90_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "q7.xy.y90_DragCosine.wf.I",
                "Q": "q7.xy.y90_DragCosine.wf.Q",
            },
        },
        "q7.xy.-y90_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "q7.xy.-y90_DragCosine.wf.I",
                "Q": "q7.xy.-y90_DragCosine.wf.Q",
            },
        },
        "q7.xy.const.pulse": {
            "operation": "control",
            "length": 1000,
            "waveforms": {
                "I": "q7.xy.const.wf.I",
                "Q": "q7.xy.const.wf.Q",
            },
        },
        "q7.resonator.readout.pulse": {
            "operation": "measurement",
            "length": 1000,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q7.resonator.readout.wf.I",
                "Q": "q7.resonator.readout.wf.Q",
            },
            "integration_weights": {
                "iw1": "q7.resonator.readout.iw1",
                "iw2": "q7.resonator.readout.iw2",
                "iw3": "q7.resonator.readout.iw3",
            },
        },
        "q7.resonator.const.pulse": {
            "operation": "control",
            "length": 1000,
            "waveforms": {
                "I": "q7.resonator.const.wf.I",
                "Q": "q7.resonator.const.wf.Q",
            },
        },
        "q8.xy.saturation.pulse": {
            "operation": "control",
            "length": 20000,
            "waveforms": {
                "I": "q8.xy.saturation.wf.I",
                "Q": "q8.xy.saturation.wf.Q",
            },
        },
        "q8.xy.x180_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "q8.xy.x180_DragCosine.wf.I",
                "Q": "q8.xy.x180_DragCosine.wf.Q",
            },
        },
        "q8.xy.x90_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "q8.xy.x90_DragCosine.wf.I",
                "Q": "q8.xy.x90_DragCosine.wf.Q",
            },
        },
        "q8.xy.-x90_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "q8.xy.-x90_DragCosine.wf.I",
                "Q": "q8.xy.-x90_DragCosine.wf.Q",
            },
        },
        "q8.xy.y180_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "q8.xy.y180_DragCosine.wf.I",
                "Q": "q8.xy.y180_DragCosine.wf.Q",
            },
        },
        "q8.xy.y90_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "q8.xy.y90_DragCosine.wf.I",
                "Q": "q8.xy.y90_DragCosine.wf.Q",
            },
        },
        "q8.xy.-y90_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "q8.xy.-y90_DragCosine.wf.I",
                "Q": "q8.xy.-y90_DragCosine.wf.Q",
            },
        },
        "q8.xy.const.pulse": {
            "operation": "control",
            "length": 1000,
            "waveforms": {
                "I": "q8.xy.const.wf.I",
                "Q": "q8.xy.const.wf.Q",
            },
        },
        "q8.resonator.readout.pulse": {
            "operation": "measurement",
            "length": 1000,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q8.resonator.readout.wf.I",
                "Q": "q8.resonator.readout.wf.Q",
            },
            "integration_weights": {
                "iw1": "q8.resonator.readout.iw1",
                "iw2": "q8.resonator.readout.iw2",
                "iw3": "q8.resonator.readout.iw3",
            },
        },
        "q8.resonator.const.pulse": {
            "operation": "control",
            "length": 1000,
            "waveforms": {
                "I": "q8.resonator.const.wf.I",
                "Q": "q8.resonator.const.wf.Q",
            },
        },
        "cr_q1_q2.square.pulse": {
            "operation": "control",
            "length": 100,
            "waveforms": {
                "I": "cr_q1_q2.square.wf.I",
                "Q": "cr_q1_q2.square.wf.Q",
            },
        },
        "cr_q5_q4.square.pulse": {
            "operation": "control",
            "length": 100,
            "waveforms": {
                "I": "cr_q5_q4.square.wf.I",
                "Q": "cr_q5_q4.square.wf.Q",
            },
        },
        "zz_q5_q4.square.pulse": {
            "operation": "control",
            "length": 100,
            "waveforms": {
                "I": "zz_q5_q4.square.wf.I",
                "Q": "zz_q5_q4.square.wf.Q",
            },
        },
        "cr_q2_q1.square.pulse": {
            "operation": "control",
            "length": 100,
            "waveforms": {
                "I": "cr_q2_q1.square.wf.I",
                "Q": "cr_q2_q1.square.wf.Q",
            },
        },
        "cr_q2_q3.square.pulse": {
            "operation": "control",
            "length": 100,
            "waveforms": {
                "I": "cr_q2_q3.square.wf.I",
                "Q": "cr_q2_q3.square.wf.Q",
            },
        },
        "cr_q3_q2.square.pulse": {
            "operation": "control",
            "length": 100,
            "waveforms": {
                "I": "cr_q3_q2.square.wf.I",
                "Q": "cr_q3_q2.square.wf.Q",
            },
        },
        "cr_q3_q4.square.pulse": {
            "operation": "control",
            "length": 100,
            "waveforms": {
                "I": "cr_q3_q4.square.wf.I",
                "Q": "cr_q3_q4.square.wf.Q",
            },
        },
        "cr_q4_q3.square.pulse": {
            "operation": "control",
            "length": 100,
            "waveforms": {
                "I": "cr_q4_q3.square.wf.I",
                "Q": "cr_q4_q3.square.wf.Q",
            },
        },
        "cr_q4_q5.square.pulse": {
            "operation": "control",
            "length": 100,
            "waveforms": {
                "I": "cr_q4_q5.square.wf.I",
                "Q": "cr_q4_q5.square.wf.Q",
            },
        },
        "cr_q5_q6.square.pulse": {
            "operation": "control",
            "length": 100,
            "waveforms": {
                "I": "cr_q5_q6.square.wf.I",
                "Q": "cr_q5_q6.square.wf.Q",
            },
        },
        "cr_q6_q5.square.pulse": {
            "operation": "control",
            "length": 100,
            "waveforms": {
                "I": "cr_q6_q5.square.wf.I",
                "Q": "cr_q6_q5.square.wf.Q",
            },
        },
        "cr_q6_q7.square.pulse": {
            "operation": "control",
            "length": 100,
            "waveforms": {
                "I": "cr_q6_q7.square.wf.I",
                "Q": "cr_q6_q7.square.wf.Q",
            },
        },
        "cr_q7_q6.square.pulse": {
            "operation": "control",
            "length": 100,
            "waveforms": {
                "I": "cr_q7_q6.square.wf.I",
                "Q": "cr_q7_q6.square.wf.Q",
            },
        },
        "cr_q7_q8.square.pulse": {
            "operation": "control",
            "length": 100,
            "waveforms": {
                "I": "cr_q7_q8.square.wf.I",
                "Q": "cr_q7_q8.square.wf.Q",
            },
        },
        "cr_q8_q7.square.pulse": {
            "operation": "control",
            "length": 100,
            "waveforms": {
                "I": "cr_q8_q7.square.wf.I",
                "Q": "cr_q8_q7.square.wf.Q",
            },
        },
        "cr_q8_q1.square.pulse": {
            "operation": "control",
            "length": 100,
            "waveforms": {
                "I": "cr_q8_q1.square.wf.I",
                "Q": "cr_q8_q1.square.wf.Q",
            },
        },
        "cr_q1_q8.square.pulse": {
            "operation": "control",
            "length": 100,
            "waveforms": {
                "I": "cr_q1_q8.square.wf.I",
                "Q": "cr_q1_q8.square.wf.Q",
            },
        },
    },
    "waveforms": {
        "zero_wf": {
            "type": "constant",
            "sample": 0.0,
        },
        "const_wf": {
            "type": "constant",
            "sample": 0.1,
        },
        "q1.xy.saturation.wf.I": {
            "type": "constant",
            "sample": 0.03981071705534972,
        },
        "q1.xy.saturation.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q1.xy.x180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0025776916503157127, 0.01024400574151878, 0.022800388765576485, 0.03992163699773022, 0.061164319102145016, 0.08597826077058386, 0.11372079394799796, 0.14367340159757425, 0.17506032691456946, 0.20706866502006654, 0.23886941677033918, 0.2696389593992218, 0.29858037791512293, 0.3249441047807083, 0.3480473333183877, 0.36729170204460276, 0.3821787919179461, 0.3923230351305265, 0.3974617011116639, 0.39746170111166396, 0.3923230351305265, 0.3821787919179461, 0.3672917020446029, 0.34804733331838783, 0.3249441047807083, 0.2985803779151228, 0.26963895939922183, 0.23886941677033927, 0.20706866502006654, 0.17506032691456963, 0.14367340159757439, 0.11372079394799806, 0.08597826077058393, 0.06116431910214504, 0.03992163699773022, 0.022800388765576465, 0.010244005741518757, 0.0025776916503157127, 0.0],
        },
        "q1.xy.x180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
        },
        "q1.xy.x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0012888458251578564, 0.00512200287075939, 0.011400194382788243, 0.01996081849886511, 0.030582159551072508, 0.04298913038529193, 0.05686039697399898, 0.07183670079878712, 0.08753016345728473, 0.10353433251003327, 0.11943470838516959, 0.1348194796996109, 0.14929018895756146, 0.16247205239035414, 0.17402366665919386, 0.18364585102230138, 0.19108939595897306, 0.19616151756526326, 0.19873085055583195, 0.19873085055583198, 0.19616151756526326, 0.19108939595897306, 0.18364585102230144, 0.17402366665919392, 0.16247205239035414, 0.1492901889575614, 0.13481947969961092, 0.11943470838516963, 0.10353433251003327, 0.08753016345728482, 0.07183670079878719, 0.05686039697399903, 0.042989130385291965, 0.03058215955107252, 0.01996081849886511, 0.011400194382788232, 0.005122002870759378, 0.0012888458251578564, 0.0],
        },
        "q1.xy.x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
        },
        "q1.xy.-x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -0.0012888458251578564, -0.00512200287075939, -0.011400194382788243, -0.01996081849886511, -0.030582159551072508, -0.04298913038529193, -0.05686039697399898, -0.07183670079878712, -0.08753016345728473, -0.10353433251003327, -0.11943470838516959, -0.1348194796996109, -0.14929018895756146, -0.16247205239035414, -0.17402366665919386, -0.18364585102230138, -0.19108939595897306, -0.19616151756526326, -0.19873085055583195, -0.19873085055583198, -0.19616151756526326, -0.19108939595897306, -0.18364585102230144, -0.17402366665919392, -0.16247205239035414, -0.1492901889575614, -0.13481947969961092, -0.11943470838516963, -0.10353433251003327, -0.08753016345728482, -0.07183670079878719, -0.05686039697399903, -0.042989130385291965, -0.03058215955107252, -0.01996081849886511, -0.011400194382788232, -0.005122002870759378, -0.0012888458251578564, 0.0],
        },
        "q1.xy.-x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 1.578380914373998e-19, 6.27264442089904e-19, 1.3961211560539257e-18, 2.4444952482996434e-18, 3.745234380523461e-18, 5.2646500924475986e-18, 6.96339031524557e-18, 8.797458569454076e-18, 1.0719353450680837e-17, 1.2679298891027e-17, 1.462653333309955e-17, 1.6510624427684005e-17, 1.8282775205098117e-17, 1.9897087891074827e-17, 2.1311752635006774e-17, 2.2490130363115307e-17, 2.3401701711215753e-17, 2.4022857460218697e-17, 2.433751000250306e-17, 2.4337510002503062e-17, 2.4022857460218697e-17, 2.3401701711215753e-17, 2.2490130363115313e-17, 2.131175263500678e-17, 1.9897087891074827e-17, 1.828277520509811e-17, 1.651062442768401e-17, 1.4626533333099555e-17, 1.2679298891027e-17, 1.0719353450680847e-17, 8.797458569454085e-18, 6.963390315245576e-18, 5.264650092447603e-18, 3.7452343805234614e-18, 2.4444952482996434e-18, 1.3961211560539245e-18, 6.272644420899027e-19, 1.578380914373998e-19, 0.0],
        },
        "q1.xy.y180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 1.578380914373998e-19, 6.27264442089904e-19, 1.3961211560539257e-18, 2.4444952482996434e-18, 3.745234380523461e-18, 5.2646500924475986e-18, 6.96339031524557e-18, 8.797458569454076e-18, 1.0719353450680837e-17, 1.2679298891027e-17, 1.462653333309955e-17, 1.6510624427684005e-17, 1.8282775205098117e-17, 1.9897087891074827e-17, 2.1311752635006774e-17, 2.2490130363115307e-17, 2.3401701711215753e-17, 2.4022857460218697e-17, 2.433751000250306e-17, 2.4337510002503062e-17, 2.4022857460218697e-17, 2.3401701711215753e-17, 2.2490130363115313e-17, 2.131175263500678e-17, 1.9897087891074827e-17, 1.828277520509811e-17, 1.651062442768401e-17, 1.4626533333099555e-17, 1.2679298891027e-17, 1.0719353450680847e-17, 8.797458569454085e-18, 6.963390315245576e-18, 5.264650092447603e-18, 3.7452343805234614e-18, 2.4444952482996434e-18, 1.3961211560539245e-18, 6.272644420899027e-19, 1.578380914373998e-19, 0.0],
        },
        "q1.xy.y180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0025776916503157127, 0.01024400574151878, 0.022800388765576485, 0.03992163699773022, 0.061164319102145016, 0.08597826077058386, 0.11372079394799796, 0.14367340159757425, 0.17506032691456946, 0.20706866502006654, 0.23886941677033918, 0.2696389593992218, 0.29858037791512293, 0.3249441047807083, 0.3480473333183877, 0.36729170204460276, 0.3821787919179461, 0.3923230351305265, 0.3974617011116639, 0.39746170111166396, 0.3923230351305265, 0.3821787919179461, 0.3672917020446029, 0.34804733331838783, 0.3249441047807083, 0.2985803779151228, 0.26963895939922183, 0.23886941677033927, 0.20706866502006654, 0.17506032691456963, 0.14367340159757439, 0.11372079394799806, 0.08597826077058393, 0.06116431910214504, 0.03992163699773022, 0.022800388765576465, 0.010244005741518757, 0.0025776916503157127, 0.0],
        },
        "q1.xy.y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 7.89190457186999e-20, 3.13632221044952e-19, 6.980605780269628e-19, 1.2222476241498217e-18, 1.8726171902617303e-18, 2.6323250462237993e-18, 3.481695157622785e-18, 4.398729284727038e-18, 5.359676725340419e-18, 6.3396494455135e-18, 7.313266666549774e-18, 8.255312213842003e-18, 9.141387602549059e-18, 9.948543945537414e-18, 1.0655876317503387e-17, 1.1245065181557654e-17, 1.1700850855607877e-17, 1.2011428730109348e-17, 1.216875500125153e-17, 1.2168755001251531e-17, 1.2011428730109348e-17, 1.1700850855607877e-17, 1.1245065181557657e-17, 1.065587631750339e-17, 9.948543945537414e-18, 9.141387602549055e-18, 8.255312213842004e-18, 7.313266666549777e-18, 6.3396494455135e-18, 5.359676725340423e-18, 4.3987292847270425e-18, 3.481695157622788e-18, 2.6323250462238016e-18, 1.8726171902617307e-18, 1.2222476241498217e-18, 6.980605780269622e-19, 3.1363222104495134e-19, 7.89190457186999e-20, 0.0],
        },
        "q1.xy.y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0012888458251578564, 0.00512200287075939, 0.011400194382788243, 0.01996081849886511, 0.030582159551072508, 0.04298913038529193, 0.05686039697399898, 0.07183670079878712, 0.08753016345728473, 0.10353433251003327, 0.11943470838516959, 0.1348194796996109, 0.14929018895756146, 0.16247205239035414, 0.17402366665919386, 0.18364585102230138, 0.19108939595897306, 0.19616151756526326, 0.19873085055583195, 0.19873085055583198, 0.19616151756526326, 0.19108939595897306, 0.18364585102230144, 0.17402366665919392, 0.16247205239035414, 0.1492901889575614, 0.13481947969961092, 0.11943470838516963, 0.10353433251003327, 0.08753016345728482, 0.07183670079878719, 0.05686039697399903, 0.042989130385291965, 0.03058215955107252, 0.01996081849886511, 0.011400194382788232, 0.005122002870759378, 0.0012888458251578564, 0.0],
        },
        "q1.xy.-y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 7.89190457186999e-20, 3.13632221044952e-19, 6.980605780269628e-19, 1.2222476241498217e-18, 1.8726171902617303e-18, 2.6323250462237993e-18, 3.481695157622785e-18, 4.398729284727038e-18, 5.359676725340419e-18, 6.3396494455135e-18, 7.313266666549774e-18, 8.255312213842003e-18, 9.141387602549059e-18, 9.948543945537414e-18, 1.0655876317503387e-17, 1.1245065181557654e-17, 1.1700850855607877e-17, 1.2011428730109348e-17, 1.216875500125153e-17, 1.2168755001251531e-17, 1.2011428730109348e-17, 1.1700850855607877e-17, 1.1245065181557657e-17, 1.065587631750339e-17, 9.948543945537414e-18, 9.141387602549055e-18, 8.255312213842004e-18, 7.313266666549777e-18, 6.3396494455135e-18, 5.359676725340423e-18, 4.3987292847270425e-18, 3.481695157622788e-18, 2.6323250462238016e-18, 1.8726171902617307e-18, 1.2222476241498217e-18, 6.980605780269622e-19, 3.1363222104495134e-19, 7.89190457186999e-20, 0.0],
        },
        "q1.xy.-y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.0012888458251578564, -0.00512200287075939, -0.011400194382788243, -0.01996081849886511, -0.030582159551072508, -0.04298913038529193, -0.05686039697399898, -0.07183670079878712, -0.08753016345728473, -0.10353433251003327, -0.11943470838516959, -0.1348194796996109, -0.14929018895756146, -0.16247205239035414, -0.17402366665919386, -0.18364585102230138, -0.19108939595897306, -0.19616151756526326, -0.19873085055583195, -0.19873085055583198, -0.19616151756526326, -0.19108939595897306, -0.18364585102230144, -0.17402366665919392, -0.16247205239035414, -0.1492901889575614, -0.13481947969961092, -0.11943470838516963, -0.10353433251003327, -0.08753016345728482, -0.07183670079878719, -0.05686039697399903, -0.042989130385291965, -0.03058215955107252, -0.01996081849886511, -0.011400194382788232, -0.005122002870759378, -0.0012888458251578564, 0.0],
        },
        "q1.xy.const.wf.I": {
            "type": "constant",
            "sample": 0.5,
        },
        "q1.xy.const.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q1.resonator.readout.wf.I": {
            "type": "constant",
            "sample": 0.31622776601683794,
        },
        "q1.resonator.readout.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q1.resonator.const.wf.I": {
            "type": "constant",
            "sample": 0.5,
        },
        "q1.resonator.const.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q2.xy.saturation.wf.I": {
            "type": "constant",
            "sample": 0.03981071705534972,
        },
        "q2.xy.saturation.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q2.xy.x180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0025776916503157127, 0.01024400574151878, 0.022800388765576485, 0.03992163699773022, 0.061164319102145016, 0.08597826077058386, 0.11372079394799796, 0.14367340159757425, 0.17506032691456946, 0.20706866502006654, 0.23886941677033918, 0.2696389593992218, 0.29858037791512293, 0.3249441047807083, 0.3480473333183877, 0.36729170204460276, 0.3821787919179461, 0.3923230351305265, 0.3974617011116639, 0.39746170111166396, 0.3923230351305265, 0.3821787919179461, 0.3672917020446029, 0.34804733331838783, 0.3249441047807083, 0.2985803779151228, 0.26963895939922183, 0.23886941677033927, 0.20706866502006654, 0.17506032691456963, 0.14367340159757439, 0.11372079394799806, 0.08597826077058393, 0.06116431910214504, 0.03992163699773022, 0.022800388765576465, 0.010244005741518757, 0.0025776916503157127, 0.0],
        },
        "q2.xy.x180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
        },
        "q2.xy.x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0012888458251578564, 0.00512200287075939, 0.011400194382788243, 0.01996081849886511, 0.030582159551072508, 0.04298913038529193, 0.05686039697399898, 0.07183670079878712, 0.08753016345728473, 0.10353433251003327, 0.11943470838516959, 0.1348194796996109, 0.14929018895756146, 0.16247205239035414, 0.17402366665919386, 0.18364585102230138, 0.19108939595897306, 0.19616151756526326, 0.19873085055583195, 0.19873085055583198, 0.19616151756526326, 0.19108939595897306, 0.18364585102230144, 0.17402366665919392, 0.16247205239035414, 0.1492901889575614, 0.13481947969961092, 0.11943470838516963, 0.10353433251003327, 0.08753016345728482, 0.07183670079878719, 0.05686039697399903, 0.042989130385291965, 0.03058215955107252, 0.01996081849886511, 0.011400194382788232, 0.005122002870759378, 0.0012888458251578564, 0.0],
        },
        "q2.xy.x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
        },
        "q2.xy.-x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -0.0012888458251578564, -0.00512200287075939, -0.011400194382788243, -0.01996081849886511, -0.030582159551072508, -0.04298913038529193, -0.05686039697399898, -0.07183670079878712, -0.08753016345728473, -0.10353433251003327, -0.11943470838516959, -0.1348194796996109, -0.14929018895756146, -0.16247205239035414, -0.17402366665919386, -0.18364585102230138, -0.19108939595897306, -0.19616151756526326, -0.19873085055583195, -0.19873085055583198, -0.19616151756526326, -0.19108939595897306, -0.18364585102230144, -0.17402366665919392, -0.16247205239035414, -0.1492901889575614, -0.13481947969961092, -0.11943470838516963, -0.10353433251003327, -0.08753016345728482, -0.07183670079878719, -0.05686039697399903, -0.042989130385291965, -0.03058215955107252, -0.01996081849886511, -0.011400194382788232, -0.005122002870759378, -0.0012888458251578564, 0.0],
        },
        "q2.xy.-x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 1.578380914373998e-19, 6.27264442089904e-19, 1.3961211560539257e-18, 2.4444952482996434e-18, 3.745234380523461e-18, 5.2646500924475986e-18, 6.96339031524557e-18, 8.797458569454076e-18, 1.0719353450680837e-17, 1.2679298891027e-17, 1.462653333309955e-17, 1.6510624427684005e-17, 1.8282775205098117e-17, 1.9897087891074827e-17, 2.1311752635006774e-17, 2.2490130363115307e-17, 2.3401701711215753e-17, 2.4022857460218697e-17, 2.433751000250306e-17, 2.4337510002503062e-17, 2.4022857460218697e-17, 2.3401701711215753e-17, 2.2490130363115313e-17, 2.131175263500678e-17, 1.9897087891074827e-17, 1.828277520509811e-17, 1.651062442768401e-17, 1.4626533333099555e-17, 1.2679298891027e-17, 1.0719353450680847e-17, 8.797458569454085e-18, 6.963390315245576e-18, 5.264650092447603e-18, 3.7452343805234614e-18, 2.4444952482996434e-18, 1.3961211560539245e-18, 6.272644420899027e-19, 1.578380914373998e-19, 0.0],
        },
        "q2.xy.y180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 1.578380914373998e-19, 6.27264442089904e-19, 1.3961211560539257e-18, 2.4444952482996434e-18, 3.745234380523461e-18, 5.2646500924475986e-18, 6.96339031524557e-18, 8.797458569454076e-18, 1.0719353450680837e-17, 1.2679298891027e-17, 1.462653333309955e-17, 1.6510624427684005e-17, 1.8282775205098117e-17, 1.9897087891074827e-17, 2.1311752635006774e-17, 2.2490130363115307e-17, 2.3401701711215753e-17, 2.4022857460218697e-17, 2.433751000250306e-17, 2.4337510002503062e-17, 2.4022857460218697e-17, 2.3401701711215753e-17, 2.2490130363115313e-17, 2.131175263500678e-17, 1.9897087891074827e-17, 1.828277520509811e-17, 1.651062442768401e-17, 1.4626533333099555e-17, 1.2679298891027e-17, 1.0719353450680847e-17, 8.797458569454085e-18, 6.963390315245576e-18, 5.264650092447603e-18, 3.7452343805234614e-18, 2.4444952482996434e-18, 1.3961211560539245e-18, 6.272644420899027e-19, 1.578380914373998e-19, 0.0],
        },
        "q2.xy.y180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0025776916503157127, 0.01024400574151878, 0.022800388765576485, 0.03992163699773022, 0.061164319102145016, 0.08597826077058386, 0.11372079394799796, 0.14367340159757425, 0.17506032691456946, 0.20706866502006654, 0.23886941677033918, 0.2696389593992218, 0.29858037791512293, 0.3249441047807083, 0.3480473333183877, 0.36729170204460276, 0.3821787919179461, 0.3923230351305265, 0.3974617011116639, 0.39746170111166396, 0.3923230351305265, 0.3821787919179461, 0.3672917020446029, 0.34804733331838783, 0.3249441047807083, 0.2985803779151228, 0.26963895939922183, 0.23886941677033927, 0.20706866502006654, 0.17506032691456963, 0.14367340159757439, 0.11372079394799806, 0.08597826077058393, 0.06116431910214504, 0.03992163699773022, 0.022800388765576465, 0.010244005741518757, 0.0025776916503157127, 0.0],
        },
        "q2.xy.y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 7.89190457186999e-20, 3.13632221044952e-19, 6.980605780269628e-19, 1.2222476241498217e-18, 1.8726171902617303e-18, 2.6323250462237993e-18, 3.481695157622785e-18, 4.398729284727038e-18, 5.359676725340419e-18, 6.3396494455135e-18, 7.313266666549774e-18, 8.255312213842003e-18, 9.141387602549059e-18, 9.948543945537414e-18, 1.0655876317503387e-17, 1.1245065181557654e-17, 1.1700850855607877e-17, 1.2011428730109348e-17, 1.216875500125153e-17, 1.2168755001251531e-17, 1.2011428730109348e-17, 1.1700850855607877e-17, 1.1245065181557657e-17, 1.065587631750339e-17, 9.948543945537414e-18, 9.141387602549055e-18, 8.255312213842004e-18, 7.313266666549777e-18, 6.3396494455135e-18, 5.359676725340423e-18, 4.3987292847270425e-18, 3.481695157622788e-18, 2.6323250462238016e-18, 1.8726171902617307e-18, 1.2222476241498217e-18, 6.980605780269622e-19, 3.1363222104495134e-19, 7.89190457186999e-20, 0.0],
        },
        "q2.xy.y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0012888458251578564, 0.00512200287075939, 0.011400194382788243, 0.01996081849886511, 0.030582159551072508, 0.04298913038529193, 0.05686039697399898, 0.07183670079878712, 0.08753016345728473, 0.10353433251003327, 0.11943470838516959, 0.1348194796996109, 0.14929018895756146, 0.16247205239035414, 0.17402366665919386, 0.18364585102230138, 0.19108939595897306, 0.19616151756526326, 0.19873085055583195, 0.19873085055583198, 0.19616151756526326, 0.19108939595897306, 0.18364585102230144, 0.17402366665919392, 0.16247205239035414, 0.1492901889575614, 0.13481947969961092, 0.11943470838516963, 0.10353433251003327, 0.08753016345728482, 0.07183670079878719, 0.05686039697399903, 0.042989130385291965, 0.03058215955107252, 0.01996081849886511, 0.011400194382788232, 0.005122002870759378, 0.0012888458251578564, 0.0],
        },
        "q2.xy.-y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 7.89190457186999e-20, 3.13632221044952e-19, 6.980605780269628e-19, 1.2222476241498217e-18, 1.8726171902617303e-18, 2.6323250462237993e-18, 3.481695157622785e-18, 4.398729284727038e-18, 5.359676725340419e-18, 6.3396494455135e-18, 7.313266666549774e-18, 8.255312213842003e-18, 9.141387602549059e-18, 9.948543945537414e-18, 1.0655876317503387e-17, 1.1245065181557654e-17, 1.1700850855607877e-17, 1.2011428730109348e-17, 1.216875500125153e-17, 1.2168755001251531e-17, 1.2011428730109348e-17, 1.1700850855607877e-17, 1.1245065181557657e-17, 1.065587631750339e-17, 9.948543945537414e-18, 9.141387602549055e-18, 8.255312213842004e-18, 7.313266666549777e-18, 6.3396494455135e-18, 5.359676725340423e-18, 4.3987292847270425e-18, 3.481695157622788e-18, 2.6323250462238016e-18, 1.8726171902617307e-18, 1.2222476241498217e-18, 6.980605780269622e-19, 3.1363222104495134e-19, 7.89190457186999e-20, 0.0],
        },
        "q2.xy.-y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.0012888458251578564, -0.00512200287075939, -0.011400194382788243, -0.01996081849886511, -0.030582159551072508, -0.04298913038529193, -0.05686039697399898, -0.07183670079878712, -0.08753016345728473, -0.10353433251003327, -0.11943470838516959, -0.1348194796996109, -0.14929018895756146, -0.16247205239035414, -0.17402366665919386, -0.18364585102230138, -0.19108939595897306, -0.19616151756526326, -0.19873085055583195, -0.19873085055583198, -0.19616151756526326, -0.19108939595897306, -0.18364585102230144, -0.17402366665919392, -0.16247205239035414, -0.1492901889575614, -0.13481947969961092, -0.11943470838516963, -0.10353433251003327, -0.08753016345728482, -0.07183670079878719, -0.05686039697399903, -0.042989130385291965, -0.03058215955107252, -0.01996081849886511, -0.011400194382788232, -0.005122002870759378, -0.0012888458251578564, 0.0],
        },
        "q2.xy.const.wf.I": {
            "type": "constant",
            "sample": 0.5,
        },
        "q2.xy.const.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q2.resonator.readout.wf.I": {
            "type": "constant",
            "sample": 0.31622776601683794,
        },
        "q2.resonator.readout.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q2.resonator.const.wf.I": {
            "type": "constant",
            "sample": 0.5,
        },
        "q2.resonator.const.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q3.xy.saturation.wf.I": {
            "type": "constant",
            "sample": 0.03981071705534972,
        },
        "q3.xy.saturation.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q3.xy.x180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0025776916503157127, 0.01024400574151878, 0.022800388765576485, 0.03992163699773022, 0.061164319102145016, 0.08597826077058386, 0.11372079394799796, 0.14367340159757425, 0.17506032691456946, 0.20706866502006654, 0.23886941677033918, 0.2696389593992218, 0.29858037791512293, 0.3249441047807083, 0.3480473333183877, 0.36729170204460276, 0.3821787919179461, 0.3923230351305265, 0.3974617011116639, 0.39746170111166396, 0.3923230351305265, 0.3821787919179461, 0.3672917020446029, 0.34804733331838783, 0.3249441047807083, 0.2985803779151228, 0.26963895939922183, 0.23886941677033927, 0.20706866502006654, 0.17506032691456963, 0.14367340159757439, 0.11372079394799806, 0.08597826077058393, 0.06116431910214504, 0.03992163699773022, 0.022800388765576465, 0.010244005741518757, 0.0025776916503157127, 0.0],
        },
        "q3.xy.x180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
        },
        "q3.xy.x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0012888458251578564, 0.00512200287075939, 0.011400194382788243, 0.01996081849886511, 0.030582159551072508, 0.04298913038529193, 0.05686039697399898, 0.07183670079878712, 0.08753016345728473, 0.10353433251003327, 0.11943470838516959, 0.1348194796996109, 0.14929018895756146, 0.16247205239035414, 0.17402366665919386, 0.18364585102230138, 0.19108939595897306, 0.19616151756526326, 0.19873085055583195, 0.19873085055583198, 0.19616151756526326, 0.19108939595897306, 0.18364585102230144, 0.17402366665919392, 0.16247205239035414, 0.1492901889575614, 0.13481947969961092, 0.11943470838516963, 0.10353433251003327, 0.08753016345728482, 0.07183670079878719, 0.05686039697399903, 0.042989130385291965, 0.03058215955107252, 0.01996081849886511, 0.011400194382788232, 0.005122002870759378, 0.0012888458251578564, 0.0],
        },
        "q3.xy.x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
        },
        "q3.xy.-x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -0.0012888458251578564, -0.00512200287075939, -0.011400194382788243, -0.01996081849886511, -0.030582159551072508, -0.04298913038529193, -0.05686039697399898, -0.07183670079878712, -0.08753016345728473, -0.10353433251003327, -0.11943470838516959, -0.1348194796996109, -0.14929018895756146, -0.16247205239035414, -0.17402366665919386, -0.18364585102230138, -0.19108939595897306, -0.19616151756526326, -0.19873085055583195, -0.19873085055583198, -0.19616151756526326, -0.19108939595897306, -0.18364585102230144, -0.17402366665919392, -0.16247205239035414, -0.1492901889575614, -0.13481947969961092, -0.11943470838516963, -0.10353433251003327, -0.08753016345728482, -0.07183670079878719, -0.05686039697399903, -0.042989130385291965, -0.03058215955107252, -0.01996081849886511, -0.011400194382788232, -0.005122002870759378, -0.0012888458251578564, 0.0],
        },
        "q3.xy.-x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 1.578380914373998e-19, 6.27264442089904e-19, 1.3961211560539257e-18, 2.4444952482996434e-18, 3.745234380523461e-18, 5.2646500924475986e-18, 6.96339031524557e-18, 8.797458569454076e-18, 1.0719353450680837e-17, 1.2679298891027e-17, 1.462653333309955e-17, 1.6510624427684005e-17, 1.8282775205098117e-17, 1.9897087891074827e-17, 2.1311752635006774e-17, 2.2490130363115307e-17, 2.3401701711215753e-17, 2.4022857460218697e-17, 2.433751000250306e-17, 2.4337510002503062e-17, 2.4022857460218697e-17, 2.3401701711215753e-17, 2.2490130363115313e-17, 2.131175263500678e-17, 1.9897087891074827e-17, 1.828277520509811e-17, 1.651062442768401e-17, 1.4626533333099555e-17, 1.2679298891027e-17, 1.0719353450680847e-17, 8.797458569454085e-18, 6.963390315245576e-18, 5.264650092447603e-18, 3.7452343805234614e-18, 2.4444952482996434e-18, 1.3961211560539245e-18, 6.272644420899027e-19, 1.578380914373998e-19, 0.0],
        },
        "q3.xy.y180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 1.578380914373998e-19, 6.27264442089904e-19, 1.3961211560539257e-18, 2.4444952482996434e-18, 3.745234380523461e-18, 5.2646500924475986e-18, 6.96339031524557e-18, 8.797458569454076e-18, 1.0719353450680837e-17, 1.2679298891027e-17, 1.462653333309955e-17, 1.6510624427684005e-17, 1.8282775205098117e-17, 1.9897087891074827e-17, 2.1311752635006774e-17, 2.2490130363115307e-17, 2.3401701711215753e-17, 2.4022857460218697e-17, 2.433751000250306e-17, 2.4337510002503062e-17, 2.4022857460218697e-17, 2.3401701711215753e-17, 2.2490130363115313e-17, 2.131175263500678e-17, 1.9897087891074827e-17, 1.828277520509811e-17, 1.651062442768401e-17, 1.4626533333099555e-17, 1.2679298891027e-17, 1.0719353450680847e-17, 8.797458569454085e-18, 6.963390315245576e-18, 5.264650092447603e-18, 3.7452343805234614e-18, 2.4444952482996434e-18, 1.3961211560539245e-18, 6.272644420899027e-19, 1.578380914373998e-19, 0.0],
        },
        "q3.xy.y180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0025776916503157127, 0.01024400574151878, 0.022800388765576485, 0.03992163699773022, 0.061164319102145016, 0.08597826077058386, 0.11372079394799796, 0.14367340159757425, 0.17506032691456946, 0.20706866502006654, 0.23886941677033918, 0.2696389593992218, 0.29858037791512293, 0.3249441047807083, 0.3480473333183877, 0.36729170204460276, 0.3821787919179461, 0.3923230351305265, 0.3974617011116639, 0.39746170111166396, 0.3923230351305265, 0.3821787919179461, 0.3672917020446029, 0.34804733331838783, 0.3249441047807083, 0.2985803779151228, 0.26963895939922183, 0.23886941677033927, 0.20706866502006654, 0.17506032691456963, 0.14367340159757439, 0.11372079394799806, 0.08597826077058393, 0.06116431910214504, 0.03992163699773022, 0.022800388765576465, 0.010244005741518757, 0.0025776916503157127, 0.0],
        },
        "q3.xy.y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 7.89190457186999e-20, 3.13632221044952e-19, 6.980605780269628e-19, 1.2222476241498217e-18, 1.8726171902617303e-18, 2.6323250462237993e-18, 3.481695157622785e-18, 4.398729284727038e-18, 5.359676725340419e-18, 6.3396494455135e-18, 7.313266666549774e-18, 8.255312213842003e-18, 9.141387602549059e-18, 9.948543945537414e-18, 1.0655876317503387e-17, 1.1245065181557654e-17, 1.1700850855607877e-17, 1.2011428730109348e-17, 1.216875500125153e-17, 1.2168755001251531e-17, 1.2011428730109348e-17, 1.1700850855607877e-17, 1.1245065181557657e-17, 1.065587631750339e-17, 9.948543945537414e-18, 9.141387602549055e-18, 8.255312213842004e-18, 7.313266666549777e-18, 6.3396494455135e-18, 5.359676725340423e-18, 4.3987292847270425e-18, 3.481695157622788e-18, 2.6323250462238016e-18, 1.8726171902617307e-18, 1.2222476241498217e-18, 6.980605780269622e-19, 3.1363222104495134e-19, 7.89190457186999e-20, 0.0],
        },
        "q3.xy.y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0012888458251578564, 0.00512200287075939, 0.011400194382788243, 0.01996081849886511, 0.030582159551072508, 0.04298913038529193, 0.05686039697399898, 0.07183670079878712, 0.08753016345728473, 0.10353433251003327, 0.11943470838516959, 0.1348194796996109, 0.14929018895756146, 0.16247205239035414, 0.17402366665919386, 0.18364585102230138, 0.19108939595897306, 0.19616151756526326, 0.19873085055583195, 0.19873085055583198, 0.19616151756526326, 0.19108939595897306, 0.18364585102230144, 0.17402366665919392, 0.16247205239035414, 0.1492901889575614, 0.13481947969961092, 0.11943470838516963, 0.10353433251003327, 0.08753016345728482, 0.07183670079878719, 0.05686039697399903, 0.042989130385291965, 0.03058215955107252, 0.01996081849886511, 0.011400194382788232, 0.005122002870759378, 0.0012888458251578564, 0.0],
        },
        "q3.xy.-y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 7.89190457186999e-20, 3.13632221044952e-19, 6.980605780269628e-19, 1.2222476241498217e-18, 1.8726171902617303e-18, 2.6323250462237993e-18, 3.481695157622785e-18, 4.398729284727038e-18, 5.359676725340419e-18, 6.3396494455135e-18, 7.313266666549774e-18, 8.255312213842003e-18, 9.141387602549059e-18, 9.948543945537414e-18, 1.0655876317503387e-17, 1.1245065181557654e-17, 1.1700850855607877e-17, 1.2011428730109348e-17, 1.216875500125153e-17, 1.2168755001251531e-17, 1.2011428730109348e-17, 1.1700850855607877e-17, 1.1245065181557657e-17, 1.065587631750339e-17, 9.948543945537414e-18, 9.141387602549055e-18, 8.255312213842004e-18, 7.313266666549777e-18, 6.3396494455135e-18, 5.359676725340423e-18, 4.3987292847270425e-18, 3.481695157622788e-18, 2.6323250462238016e-18, 1.8726171902617307e-18, 1.2222476241498217e-18, 6.980605780269622e-19, 3.1363222104495134e-19, 7.89190457186999e-20, 0.0],
        },
        "q3.xy.-y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.0012888458251578564, -0.00512200287075939, -0.011400194382788243, -0.01996081849886511, -0.030582159551072508, -0.04298913038529193, -0.05686039697399898, -0.07183670079878712, -0.08753016345728473, -0.10353433251003327, -0.11943470838516959, -0.1348194796996109, -0.14929018895756146, -0.16247205239035414, -0.17402366665919386, -0.18364585102230138, -0.19108939595897306, -0.19616151756526326, -0.19873085055583195, -0.19873085055583198, -0.19616151756526326, -0.19108939595897306, -0.18364585102230144, -0.17402366665919392, -0.16247205239035414, -0.1492901889575614, -0.13481947969961092, -0.11943470838516963, -0.10353433251003327, -0.08753016345728482, -0.07183670079878719, -0.05686039697399903, -0.042989130385291965, -0.03058215955107252, -0.01996081849886511, -0.011400194382788232, -0.005122002870759378, -0.0012888458251578564, 0.0],
        },
        "q3.xy.const.wf.I": {
            "type": "constant",
            "sample": 0.5,
        },
        "q3.xy.const.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q3.resonator.readout.wf.I": {
            "type": "constant",
            "sample": 0.31622776601683794,
        },
        "q3.resonator.readout.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q3.resonator.const.wf.I": {
            "type": "constant",
            "sample": 0.5,
        },
        "q3.resonator.const.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q4.xy.saturation.wf.I": {
            "type": "constant",
            "sample": 0.03981071705534972,
        },
        "q4.xy.saturation.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q4.xy.x180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0025776916503157127, 0.01024400574151878, 0.022800388765576485, 0.03992163699773022, 0.061164319102145016, 0.08597826077058386, 0.11372079394799796, 0.14367340159757425, 0.17506032691456946, 0.20706866502006654, 0.23886941677033918, 0.2696389593992218, 0.29858037791512293, 0.3249441047807083, 0.3480473333183877, 0.36729170204460276, 0.3821787919179461, 0.3923230351305265, 0.3974617011116639, 0.39746170111166396, 0.3923230351305265, 0.3821787919179461, 0.3672917020446029, 0.34804733331838783, 0.3249441047807083, 0.2985803779151228, 0.26963895939922183, 0.23886941677033927, 0.20706866502006654, 0.17506032691456963, 0.14367340159757439, 0.11372079394799806, 0.08597826077058393, 0.06116431910214504, 0.03992163699773022, 0.022800388765576465, 0.010244005741518757, 0.0025776916503157127, 0.0],
        },
        "q4.xy.x180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
        },
        "q4.xy.x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0012888458251578564, 0.00512200287075939, 0.011400194382788243, 0.01996081849886511, 0.030582159551072508, 0.04298913038529193, 0.05686039697399898, 0.07183670079878712, 0.08753016345728473, 0.10353433251003327, 0.11943470838516959, 0.1348194796996109, 0.14929018895756146, 0.16247205239035414, 0.17402366665919386, 0.18364585102230138, 0.19108939595897306, 0.19616151756526326, 0.19873085055583195, 0.19873085055583198, 0.19616151756526326, 0.19108939595897306, 0.18364585102230144, 0.17402366665919392, 0.16247205239035414, 0.1492901889575614, 0.13481947969961092, 0.11943470838516963, 0.10353433251003327, 0.08753016345728482, 0.07183670079878719, 0.05686039697399903, 0.042989130385291965, 0.03058215955107252, 0.01996081849886511, 0.011400194382788232, 0.005122002870759378, 0.0012888458251578564, 0.0],
        },
        "q4.xy.x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
        },
        "q4.xy.-x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -0.0012888458251578564, -0.00512200287075939, -0.011400194382788243, -0.01996081849886511, -0.030582159551072508, -0.04298913038529193, -0.05686039697399898, -0.07183670079878712, -0.08753016345728473, -0.10353433251003327, -0.11943470838516959, -0.1348194796996109, -0.14929018895756146, -0.16247205239035414, -0.17402366665919386, -0.18364585102230138, -0.19108939595897306, -0.19616151756526326, -0.19873085055583195, -0.19873085055583198, -0.19616151756526326, -0.19108939595897306, -0.18364585102230144, -0.17402366665919392, -0.16247205239035414, -0.1492901889575614, -0.13481947969961092, -0.11943470838516963, -0.10353433251003327, -0.08753016345728482, -0.07183670079878719, -0.05686039697399903, -0.042989130385291965, -0.03058215955107252, -0.01996081849886511, -0.011400194382788232, -0.005122002870759378, -0.0012888458251578564, 0.0],
        },
        "q4.xy.-x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 1.578380914373998e-19, 6.27264442089904e-19, 1.3961211560539257e-18, 2.4444952482996434e-18, 3.745234380523461e-18, 5.2646500924475986e-18, 6.96339031524557e-18, 8.797458569454076e-18, 1.0719353450680837e-17, 1.2679298891027e-17, 1.462653333309955e-17, 1.6510624427684005e-17, 1.8282775205098117e-17, 1.9897087891074827e-17, 2.1311752635006774e-17, 2.2490130363115307e-17, 2.3401701711215753e-17, 2.4022857460218697e-17, 2.433751000250306e-17, 2.4337510002503062e-17, 2.4022857460218697e-17, 2.3401701711215753e-17, 2.2490130363115313e-17, 2.131175263500678e-17, 1.9897087891074827e-17, 1.828277520509811e-17, 1.651062442768401e-17, 1.4626533333099555e-17, 1.2679298891027e-17, 1.0719353450680847e-17, 8.797458569454085e-18, 6.963390315245576e-18, 5.264650092447603e-18, 3.7452343805234614e-18, 2.4444952482996434e-18, 1.3961211560539245e-18, 6.272644420899027e-19, 1.578380914373998e-19, 0.0],
        },
        "q4.xy.y180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 1.578380914373998e-19, 6.27264442089904e-19, 1.3961211560539257e-18, 2.4444952482996434e-18, 3.745234380523461e-18, 5.2646500924475986e-18, 6.96339031524557e-18, 8.797458569454076e-18, 1.0719353450680837e-17, 1.2679298891027e-17, 1.462653333309955e-17, 1.6510624427684005e-17, 1.8282775205098117e-17, 1.9897087891074827e-17, 2.1311752635006774e-17, 2.2490130363115307e-17, 2.3401701711215753e-17, 2.4022857460218697e-17, 2.433751000250306e-17, 2.4337510002503062e-17, 2.4022857460218697e-17, 2.3401701711215753e-17, 2.2490130363115313e-17, 2.131175263500678e-17, 1.9897087891074827e-17, 1.828277520509811e-17, 1.651062442768401e-17, 1.4626533333099555e-17, 1.2679298891027e-17, 1.0719353450680847e-17, 8.797458569454085e-18, 6.963390315245576e-18, 5.264650092447603e-18, 3.7452343805234614e-18, 2.4444952482996434e-18, 1.3961211560539245e-18, 6.272644420899027e-19, 1.578380914373998e-19, 0.0],
        },
        "q4.xy.y180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0025776916503157127, 0.01024400574151878, 0.022800388765576485, 0.03992163699773022, 0.061164319102145016, 0.08597826077058386, 0.11372079394799796, 0.14367340159757425, 0.17506032691456946, 0.20706866502006654, 0.23886941677033918, 0.2696389593992218, 0.29858037791512293, 0.3249441047807083, 0.3480473333183877, 0.36729170204460276, 0.3821787919179461, 0.3923230351305265, 0.3974617011116639, 0.39746170111166396, 0.3923230351305265, 0.3821787919179461, 0.3672917020446029, 0.34804733331838783, 0.3249441047807083, 0.2985803779151228, 0.26963895939922183, 0.23886941677033927, 0.20706866502006654, 0.17506032691456963, 0.14367340159757439, 0.11372079394799806, 0.08597826077058393, 0.06116431910214504, 0.03992163699773022, 0.022800388765576465, 0.010244005741518757, 0.0025776916503157127, 0.0],
        },
        "q4.xy.y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 7.89190457186999e-20, 3.13632221044952e-19, 6.980605780269628e-19, 1.2222476241498217e-18, 1.8726171902617303e-18, 2.6323250462237993e-18, 3.481695157622785e-18, 4.398729284727038e-18, 5.359676725340419e-18, 6.3396494455135e-18, 7.313266666549774e-18, 8.255312213842003e-18, 9.141387602549059e-18, 9.948543945537414e-18, 1.0655876317503387e-17, 1.1245065181557654e-17, 1.1700850855607877e-17, 1.2011428730109348e-17, 1.216875500125153e-17, 1.2168755001251531e-17, 1.2011428730109348e-17, 1.1700850855607877e-17, 1.1245065181557657e-17, 1.065587631750339e-17, 9.948543945537414e-18, 9.141387602549055e-18, 8.255312213842004e-18, 7.313266666549777e-18, 6.3396494455135e-18, 5.359676725340423e-18, 4.3987292847270425e-18, 3.481695157622788e-18, 2.6323250462238016e-18, 1.8726171902617307e-18, 1.2222476241498217e-18, 6.980605780269622e-19, 3.1363222104495134e-19, 7.89190457186999e-20, 0.0],
        },
        "q4.xy.y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0012888458251578564, 0.00512200287075939, 0.011400194382788243, 0.01996081849886511, 0.030582159551072508, 0.04298913038529193, 0.05686039697399898, 0.07183670079878712, 0.08753016345728473, 0.10353433251003327, 0.11943470838516959, 0.1348194796996109, 0.14929018895756146, 0.16247205239035414, 0.17402366665919386, 0.18364585102230138, 0.19108939595897306, 0.19616151756526326, 0.19873085055583195, 0.19873085055583198, 0.19616151756526326, 0.19108939595897306, 0.18364585102230144, 0.17402366665919392, 0.16247205239035414, 0.1492901889575614, 0.13481947969961092, 0.11943470838516963, 0.10353433251003327, 0.08753016345728482, 0.07183670079878719, 0.05686039697399903, 0.042989130385291965, 0.03058215955107252, 0.01996081849886511, 0.011400194382788232, 0.005122002870759378, 0.0012888458251578564, 0.0],
        },
        "q4.xy.-y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 7.89190457186999e-20, 3.13632221044952e-19, 6.980605780269628e-19, 1.2222476241498217e-18, 1.8726171902617303e-18, 2.6323250462237993e-18, 3.481695157622785e-18, 4.398729284727038e-18, 5.359676725340419e-18, 6.3396494455135e-18, 7.313266666549774e-18, 8.255312213842003e-18, 9.141387602549059e-18, 9.948543945537414e-18, 1.0655876317503387e-17, 1.1245065181557654e-17, 1.1700850855607877e-17, 1.2011428730109348e-17, 1.216875500125153e-17, 1.2168755001251531e-17, 1.2011428730109348e-17, 1.1700850855607877e-17, 1.1245065181557657e-17, 1.065587631750339e-17, 9.948543945537414e-18, 9.141387602549055e-18, 8.255312213842004e-18, 7.313266666549777e-18, 6.3396494455135e-18, 5.359676725340423e-18, 4.3987292847270425e-18, 3.481695157622788e-18, 2.6323250462238016e-18, 1.8726171902617307e-18, 1.2222476241498217e-18, 6.980605780269622e-19, 3.1363222104495134e-19, 7.89190457186999e-20, 0.0],
        },
        "q4.xy.-y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.0012888458251578564, -0.00512200287075939, -0.011400194382788243, -0.01996081849886511, -0.030582159551072508, -0.04298913038529193, -0.05686039697399898, -0.07183670079878712, -0.08753016345728473, -0.10353433251003327, -0.11943470838516959, -0.1348194796996109, -0.14929018895756146, -0.16247205239035414, -0.17402366665919386, -0.18364585102230138, -0.19108939595897306, -0.19616151756526326, -0.19873085055583195, -0.19873085055583198, -0.19616151756526326, -0.19108939595897306, -0.18364585102230144, -0.17402366665919392, -0.16247205239035414, -0.1492901889575614, -0.13481947969961092, -0.11943470838516963, -0.10353433251003327, -0.08753016345728482, -0.07183670079878719, -0.05686039697399903, -0.042989130385291965, -0.03058215955107252, -0.01996081849886511, -0.011400194382788232, -0.005122002870759378, -0.0012888458251578564, 0.0],
        },
        "q4.xy.const.wf.I": {
            "type": "constant",
            "sample": 0.5,
        },
        "q4.xy.const.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q4.resonator.readout.wf.I": {
            "type": "constant",
            "sample": 0.31622776601683794,
        },
        "q4.resonator.readout.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q4.resonator.const.wf.I": {
            "type": "constant",
            "sample": 0.5,
        },
        "q4.resonator.const.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q5.xy.saturation.wf.I": {
            "type": "constant",
            "sample": 0.03981071705534972,
        },
        "q5.xy.saturation.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q5.xy.x180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0025776916503157127, 0.01024400574151878, 0.022800388765576485, 0.03992163699773022, 0.061164319102145016, 0.08597826077058386, 0.11372079394799796, 0.14367340159757425, 0.17506032691456946, 0.20706866502006654, 0.23886941677033918, 0.2696389593992218, 0.29858037791512293, 0.3249441047807083, 0.3480473333183877, 0.36729170204460276, 0.3821787919179461, 0.3923230351305265, 0.3974617011116639, 0.39746170111166396, 0.3923230351305265, 0.3821787919179461, 0.3672917020446029, 0.34804733331838783, 0.3249441047807083, 0.2985803779151228, 0.26963895939922183, 0.23886941677033927, 0.20706866502006654, 0.17506032691456963, 0.14367340159757439, 0.11372079394799806, 0.08597826077058393, 0.06116431910214504, 0.03992163699773022, 0.022800388765576465, 0.010244005741518757, 0.0025776916503157127, 0.0],
        },
        "q5.xy.x180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
        },
        "q5.xy.x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0012888458251578564, 0.00512200287075939, 0.011400194382788243, 0.01996081849886511, 0.030582159551072508, 0.04298913038529193, 0.05686039697399898, 0.07183670079878712, 0.08753016345728473, 0.10353433251003327, 0.11943470838516959, 0.1348194796996109, 0.14929018895756146, 0.16247205239035414, 0.17402366665919386, 0.18364585102230138, 0.19108939595897306, 0.19616151756526326, 0.19873085055583195, 0.19873085055583198, 0.19616151756526326, 0.19108939595897306, 0.18364585102230144, 0.17402366665919392, 0.16247205239035414, 0.1492901889575614, 0.13481947969961092, 0.11943470838516963, 0.10353433251003327, 0.08753016345728482, 0.07183670079878719, 0.05686039697399903, 0.042989130385291965, 0.03058215955107252, 0.01996081849886511, 0.011400194382788232, 0.005122002870759378, 0.0012888458251578564, 0.0],
        },
        "q5.xy.x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
        },
        "q5.xy.-x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -0.0012888458251578564, -0.00512200287075939, -0.011400194382788243, -0.01996081849886511, -0.030582159551072508, -0.04298913038529193, -0.05686039697399898, -0.07183670079878712, -0.08753016345728473, -0.10353433251003327, -0.11943470838516959, -0.1348194796996109, -0.14929018895756146, -0.16247205239035414, -0.17402366665919386, -0.18364585102230138, -0.19108939595897306, -0.19616151756526326, -0.19873085055583195, -0.19873085055583198, -0.19616151756526326, -0.19108939595897306, -0.18364585102230144, -0.17402366665919392, -0.16247205239035414, -0.1492901889575614, -0.13481947969961092, -0.11943470838516963, -0.10353433251003327, -0.08753016345728482, -0.07183670079878719, -0.05686039697399903, -0.042989130385291965, -0.03058215955107252, -0.01996081849886511, -0.011400194382788232, -0.005122002870759378, -0.0012888458251578564, 0.0],
        },
        "q5.xy.-x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 1.578380914373998e-19, 6.27264442089904e-19, 1.3961211560539257e-18, 2.4444952482996434e-18, 3.745234380523461e-18, 5.2646500924475986e-18, 6.96339031524557e-18, 8.797458569454076e-18, 1.0719353450680837e-17, 1.2679298891027e-17, 1.462653333309955e-17, 1.6510624427684005e-17, 1.8282775205098117e-17, 1.9897087891074827e-17, 2.1311752635006774e-17, 2.2490130363115307e-17, 2.3401701711215753e-17, 2.4022857460218697e-17, 2.433751000250306e-17, 2.4337510002503062e-17, 2.4022857460218697e-17, 2.3401701711215753e-17, 2.2490130363115313e-17, 2.131175263500678e-17, 1.9897087891074827e-17, 1.828277520509811e-17, 1.651062442768401e-17, 1.4626533333099555e-17, 1.2679298891027e-17, 1.0719353450680847e-17, 8.797458569454085e-18, 6.963390315245576e-18, 5.264650092447603e-18, 3.7452343805234614e-18, 2.4444952482996434e-18, 1.3961211560539245e-18, 6.272644420899027e-19, 1.578380914373998e-19, 0.0],
        },
        "q5.xy.y180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 1.578380914373998e-19, 6.27264442089904e-19, 1.3961211560539257e-18, 2.4444952482996434e-18, 3.745234380523461e-18, 5.2646500924475986e-18, 6.96339031524557e-18, 8.797458569454076e-18, 1.0719353450680837e-17, 1.2679298891027e-17, 1.462653333309955e-17, 1.6510624427684005e-17, 1.8282775205098117e-17, 1.9897087891074827e-17, 2.1311752635006774e-17, 2.2490130363115307e-17, 2.3401701711215753e-17, 2.4022857460218697e-17, 2.433751000250306e-17, 2.4337510002503062e-17, 2.4022857460218697e-17, 2.3401701711215753e-17, 2.2490130363115313e-17, 2.131175263500678e-17, 1.9897087891074827e-17, 1.828277520509811e-17, 1.651062442768401e-17, 1.4626533333099555e-17, 1.2679298891027e-17, 1.0719353450680847e-17, 8.797458569454085e-18, 6.963390315245576e-18, 5.264650092447603e-18, 3.7452343805234614e-18, 2.4444952482996434e-18, 1.3961211560539245e-18, 6.272644420899027e-19, 1.578380914373998e-19, 0.0],
        },
        "q5.xy.y180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0025776916503157127, 0.01024400574151878, 0.022800388765576485, 0.03992163699773022, 0.061164319102145016, 0.08597826077058386, 0.11372079394799796, 0.14367340159757425, 0.17506032691456946, 0.20706866502006654, 0.23886941677033918, 0.2696389593992218, 0.29858037791512293, 0.3249441047807083, 0.3480473333183877, 0.36729170204460276, 0.3821787919179461, 0.3923230351305265, 0.3974617011116639, 0.39746170111166396, 0.3923230351305265, 0.3821787919179461, 0.3672917020446029, 0.34804733331838783, 0.3249441047807083, 0.2985803779151228, 0.26963895939922183, 0.23886941677033927, 0.20706866502006654, 0.17506032691456963, 0.14367340159757439, 0.11372079394799806, 0.08597826077058393, 0.06116431910214504, 0.03992163699773022, 0.022800388765576465, 0.010244005741518757, 0.0025776916503157127, 0.0],
        },
        "q5.xy.y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 7.89190457186999e-20, 3.13632221044952e-19, 6.980605780269628e-19, 1.2222476241498217e-18, 1.8726171902617303e-18, 2.6323250462237993e-18, 3.481695157622785e-18, 4.398729284727038e-18, 5.359676725340419e-18, 6.3396494455135e-18, 7.313266666549774e-18, 8.255312213842003e-18, 9.141387602549059e-18, 9.948543945537414e-18, 1.0655876317503387e-17, 1.1245065181557654e-17, 1.1700850855607877e-17, 1.2011428730109348e-17, 1.216875500125153e-17, 1.2168755001251531e-17, 1.2011428730109348e-17, 1.1700850855607877e-17, 1.1245065181557657e-17, 1.065587631750339e-17, 9.948543945537414e-18, 9.141387602549055e-18, 8.255312213842004e-18, 7.313266666549777e-18, 6.3396494455135e-18, 5.359676725340423e-18, 4.3987292847270425e-18, 3.481695157622788e-18, 2.6323250462238016e-18, 1.8726171902617307e-18, 1.2222476241498217e-18, 6.980605780269622e-19, 3.1363222104495134e-19, 7.89190457186999e-20, 0.0],
        },
        "q5.xy.y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0012888458251578564, 0.00512200287075939, 0.011400194382788243, 0.01996081849886511, 0.030582159551072508, 0.04298913038529193, 0.05686039697399898, 0.07183670079878712, 0.08753016345728473, 0.10353433251003327, 0.11943470838516959, 0.1348194796996109, 0.14929018895756146, 0.16247205239035414, 0.17402366665919386, 0.18364585102230138, 0.19108939595897306, 0.19616151756526326, 0.19873085055583195, 0.19873085055583198, 0.19616151756526326, 0.19108939595897306, 0.18364585102230144, 0.17402366665919392, 0.16247205239035414, 0.1492901889575614, 0.13481947969961092, 0.11943470838516963, 0.10353433251003327, 0.08753016345728482, 0.07183670079878719, 0.05686039697399903, 0.042989130385291965, 0.03058215955107252, 0.01996081849886511, 0.011400194382788232, 0.005122002870759378, 0.0012888458251578564, 0.0],
        },
        "q5.xy.-y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 7.89190457186999e-20, 3.13632221044952e-19, 6.980605780269628e-19, 1.2222476241498217e-18, 1.8726171902617303e-18, 2.6323250462237993e-18, 3.481695157622785e-18, 4.398729284727038e-18, 5.359676725340419e-18, 6.3396494455135e-18, 7.313266666549774e-18, 8.255312213842003e-18, 9.141387602549059e-18, 9.948543945537414e-18, 1.0655876317503387e-17, 1.1245065181557654e-17, 1.1700850855607877e-17, 1.2011428730109348e-17, 1.216875500125153e-17, 1.2168755001251531e-17, 1.2011428730109348e-17, 1.1700850855607877e-17, 1.1245065181557657e-17, 1.065587631750339e-17, 9.948543945537414e-18, 9.141387602549055e-18, 8.255312213842004e-18, 7.313266666549777e-18, 6.3396494455135e-18, 5.359676725340423e-18, 4.3987292847270425e-18, 3.481695157622788e-18, 2.6323250462238016e-18, 1.8726171902617307e-18, 1.2222476241498217e-18, 6.980605780269622e-19, 3.1363222104495134e-19, 7.89190457186999e-20, 0.0],
        },
        "q5.xy.-y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.0012888458251578564, -0.00512200287075939, -0.011400194382788243, -0.01996081849886511, -0.030582159551072508, -0.04298913038529193, -0.05686039697399898, -0.07183670079878712, -0.08753016345728473, -0.10353433251003327, -0.11943470838516959, -0.1348194796996109, -0.14929018895756146, -0.16247205239035414, -0.17402366665919386, -0.18364585102230138, -0.19108939595897306, -0.19616151756526326, -0.19873085055583195, -0.19873085055583198, -0.19616151756526326, -0.19108939595897306, -0.18364585102230144, -0.17402366665919392, -0.16247205239035414, -0.1492901889575614, -0.13481947969961092, -0.11943470838516963, -0.10353433251003327, -0.08753016345728482, -0.07183670079878719, -0.05686039697399903, -0.042989130385291965, -0.03058215955107252, -0.01996081849886511, -0.011400194382788232, -0.005122002870759378, -0.0012888458251578564, 0.0],
        },
        "q5.xy.const.wf.I": {
            "type": "constant",
            "sample": 0.5,
        },
        "q5.xy.const.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q5.resonator.readout.wf.I": {
            "type": "constant",
            "sample": 0.31622776601683794,
        },
        "q5.resonator.readout.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q5.resonator.const.wf.I": {
            "type": "constant",
            "sample": 0.5,
        },
        "q5.resonator.const.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q6.xy.saturation.wf.I": {
            "type": "constant",
            "sample": 0.03981071705534972,
        },
        "q6.xy.saturation.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q6.xy.x180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0025776916503157127, 0.01024400574151878, 0.022800388765576485, 0.03992163699773022, 0.061164319102145016, 0.08597826077058386, 0.11372079394799796, 0.14367340159757425, 0.17506032691456946, 0.20706866502006654, 0.23886941677033918, 0.2696389593992218, 0.29858037791512293, 0.3249441047807083, 0.3480473333183877, 0.36729170204460276, 0.3821787919179461, 0.3923230351305265, 0.3974617011116639, 0.39746170111166396, 0.3923230351305265, 0.3821787919179461, 0.3672917020446029, 0.34804733331838783, 0.3249441047807083, 0.2985803779151228, 0.26963895939922183, 0.23886941677033927, 0.20706866502006654, 0.17506032691456963, 0.14367340159757439, 0.11372079394799806, 0.08597826077058393, 0.06116431910214504, 0.03992163699773022, 0.022800388765576465, 0.010244005741518757, 0.0025776916503157127, 0.0],
        },
        "q6.xy.x180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
        },
        "q6.xy.x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0012888458251578564, 0.00512200287075939, 0.011400194382788243, 0.01996081849886511, 0.030582159551072508, 0.04298913038529193, 0.05686039697399898, 0.07183670079878712, 0.08753016345728473, 0.10353433251003327, 0.11943470838516959, 0.1348194796996109, 0.14929018895756146, 0.16247205239035414, 0.17402366665919386, 0.18364585102230138, 0.19108939595897306, 0.19616151756526326, 0.19873085055583195, 0.19873085055583198, 0.19616151756526326, 0.19108939595897306, 0.18364585102230144, 0.17402366665919392, 0.16247205239035414, 0.1492901889575614, 0.13481947969961092, 0.11943470838516963, 0.10353433251003327, 0.08753016345728482, 0.07183670079878719, 0.05686039697399903, 0.042989130385291965, 0.03058215955107252, 0.01996081849886511, 0.011400194382788232, 0.005122002870759378, 0.0012888458251578564, 0.0],
        },
        "q6.xy.x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
        },
        "q6.xy.-x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -0.0012888458251578564, -0.00512200287075939, -0.011400194382788243, -0.01996081849886511, -0.030582159551072508, -0.04298913038529193, -0.05686039697399898, -0.07183670079878712, -0.08753016345728473, -0.10353433251003327, -0.11943470838516959, -0.1348194796996109, -0.14929018895756146, -0.16247205239035414, -0.17402366665919386, -0.18364585102230138, -0.19108939595897306, -0.19616151756526326, -0.19873085055583195, -0.19873085055583198, -0.19616151756526326, -0.19108939595897306, -0.18364585102230144, -0.17402366665919392, -0.16247205239035414, -0.1492901889575614, -0.13481947969961092, -0.11943470838516963, -0.10353433251003327, -0.08753016345728482, -0.07183670079878719, -0.05686039697399903, -0.042989130385291965, -0.03058215955107252, -0.01996081849886511, -0.011400194382788232, -0.005122002870759378, -0.0012888458251578564, 0.0],
        },
        "q6.xy.-x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 1.578380914373998e-19, 6.27264442089904e-19, 1.3961211560539257e-18, 2.4444952482996434e-18, 3.745234380523461e-18, 5.2646500924475986e-18, 6.96339031524557e-18, 8.797458569454076e-18, 1.0719353450680837e-17, 1.2679298891027e-17, 1.462653333309955e-17, 1.6510624427684005e-17, 1.8282775205098117e-17, 1.9897087891074827e-17, 2.1311752635006774e-17, 2.2490130363115307e-17, 2.3401701711215753e-17, 2.4022857460218697e-17, 2.433751000250306e-17, 2.4337510002503062e-17, 2.4022857460218697e-17, 2.3401701711215753e-17, 2.2490130363115313e-17, 2.131175263500678e-17, 1.9897087891074827e-17, 1.828277520509811e-17, 1.651062442768401e-17, 1.4626533333099555e-17, 1.2679298891027e-17, 1.0719353450680847e-17, 8.797458569454085e-18, 6.963390315245576e-18, 5.264650092447603e-18, 3.7452343805234614e-18, 2.4444952482996434e-18, 1.3961211560539245e-18, 6.272644420899027e-19, 1.578380914373998e-19, 0.0],
        },
        "q6.xy.y180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 1.578380914373998e-19, 6.27264442089904e-19, 1.3961211560539257e-18, 2.4444952482996434e-18, 3.745234380523461e-18, 5.2646500924475986e-18, 6.96339031524557e-18, 8.797458569454076e-18, 1.0719353450680837e-17, 1.2679298891027e-17, 1.462653333309955e-17, 1.6510624427684005e-17, 1.8282775205098117e-17, 1.9897087891074827e-17, 2.1311752635006774e-17, 2.2490130363115307e-17, 2.3401701711215753e-17, 2.4022857460218697e-17, 2.433751000250306e-17, 2.4337510002503062e-17, 2.4022857460218697e-17, 2.3401701711215753e-17, 2.2490130363115313e-17, 2.131175263500678e-17, 1.9897087891074827e-17, 1.828277520509811e-17, 1.651062442768401e-17, 1.4626533333099555e-17, 1.2679298891027e-17, 1.0719353450680847e-17, 8.797458569454085e-18, 6.963390315245576e-18, 5.264650092447603e-18, 3.7452343805234614e-18, 2.4444952482996434e-18, 1.3961211560539245e-18, 6.272644420899027e-19, 1.578380914373998e-19, 0.0],
        },
        "q6.xy.y180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0025776916503157127, 0.01024400574151878, 0.022800388765576485, 0.03992163699773022, 0.061164319102145016, 0.08597826077058386, 0.11372079394799796, 0.14367340159757425, 0.17506032691456946, 0.20706866502006654, 0.23886941677033918, 0.2696389593992218, 0.29858037791512293, 0.3249441047807083, 0.3480473333183877, 0.36729170204460276, 0.3821787919179461, 0.3923230351305265, 0.3974617011116639, 0.39746170111166396, 0.3923230351305265, 0.3821787919179461, 0.3672917020446029, 0.34804733331838783, 0.3249441047807083, 0.2985803779151228, 0.26963895939922183, 0.23886941677033927, 0.20706866502006654, 0.17506032691456963, 0.14367340159757439, 0.11372079394799806, 0.08597826077058393, 0.06116431910214504, 0.03992163699773022, 0.022800388765576465, 0.010244005741518757, 0.0025776916503157127, 0.0],
        },
        "q6.xy.y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 7.89190457186999e-20, 3.13632221044952e-19, 6.980605780269628e-19, 1.2222476241498217e-18, 1.8726171902617303e-18, 2.6323250462237993e-18, 3.481695157622785e-18, 4.398729284727038e-18, 5.359676725340419e-18, 6.3396494455135e-18, 7.313266666549774e-18, 8.255312213842003e-18, 9.141387602549059e-18, 9.948543945537414e-18, 1.0655876317503387e-17, 1.1245065181557654e-17, 1.1700850855607877e-17, 1.2011428730109348e-17, 1.216875500125153e-17, 1.2168755001251531e-17, 1.2011428730109348e-17, 1.1700850855607877e-17, 1.1245065181557657e-17, 1.065587631750339e-17, 9.948543945537414e-18, 9.141387602549055e-18, 8.255312213842004e-18, 7.313266666549777e-18, 6.3396494455135e-18, 5.359676725340423e-18, 4.3987292847270425e-18, 3.481695157622788e-18, 2.6323250462238016e-18, 1.8726171902617307e-18, 1.2222476241498217e-18, 6.980605780269622e-19, 3.1363222104495134e-19, 7.89190457186999e-20, 0.0],
        },
        "q6.xy.y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0012888458251578564, 0.00512200287075939, 0.011400194382788243, 0.01996081849886511, 0.030582159551072508, 0.04298913038529193, 0.05686039697399898, 0.07183670079878712, 0.08753016345728473, 0.10353433251003327, 0.11943470838516959, 0.1348194796996109, 0.14929018895756146, 0.16247205239035414, 0.17402366665919386, 0.18364585102230138, 0.19108939595897306, 0.19616151756526326, 0.19873085055583195, 0.19873085055583198, 0.19616151756526326, 0.19108939595897306, 0.18364585102230144, 0.17402366665919392, 0.16247205239035414, 0.1492901889575614, 0.13481947969961092, 0.11943470838516963, 0.10353433251003327, 0.08753016345728482, 0.07183670079878719, 0.05686039697399903, 0.042989130385291965, 0.03058215955107252, 0.01996081849886511, 0.011400194382788232, 0.005122002870759378, 0.0012888458251578564, 0.0],
        },
        "q6.xy.-y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 7.89190457186999e-20, 3.13632221044952e-19, 6.980605780269628e-19, 1.2222476241498217e-18, 1.8726171902617303e-18, 2.6323250462237993e-18, 3.481695157622785e-18, 4.398729284727038e-18, 5.359676725340419e-18, 6.3396494455135e-18, 7.313266666549774e-18, 8.255312213842003e-18, 9.141387602549059e-18, 9.948543945537414e-18, 1.0655876317503387e-17, 1.1245065181557654e-17, 1.1700850855607877e-17, 1.2011428730109348e-17, 1.216875500125153e-17, 1.2168755001251531e-17, 1.2011428730109348e-17, 1.1700850855607877e-17, 1.1245065181557657e-17, 1.065587631750339e-17, 9.948543945537414e-18, 9.141387602549055e-18, 8.255312213842004e-18, 7.313266666549777e-18, 6.3396494455135e-18, 5.359676725340423e-18, 4.3987292847270425e-18, 3.481695157622788e-18, 2.6323250462238016e-18, 1.8726171902617307e-18, 1.2222476241498217e-18, 6.980605780269622e-19, 3.1363222104495134e-19, 7.89190457186999e-20, 0.0],
        },
        "q6.xy.-y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.0012888458251578564, -0.00512200287075939, -0.011400194382788243, -0.01996081849886511, -0.030582159551072508, -0.04298913038529193, -0.05686039697399898, -0.07183670079878712, -0.08753016345728473, -0.10353433251003327, -0.11943470838516959, -0.1348194796996109, -0.14929018895756146, -0.16247205239035414, -0.17402366665919386, -0.18364585102230138, -0.19108939595897306, -0.19616151756526326, -0.19873085055583195, -0.19873085055583198, -0.19616151756526326, -0.19108939595897306, -0.18364585102230144, -0.17402366665919392, -0.16247205239035414, -0.1492901889575614, -0.13481947969961092, -0.11943470838516963, -0.10353433251003327, -0.08753016345728482, -0.07183670079878719, -0.05686039697399903, -0.042989130385291965, -0.03058215955107252, -0.01996081849886511, -0.011400194382788232, -0.005122002870759378, -0.0012888458251578564, 0.0],
        },
        "q6.xy.const.wf.I": {
            "type": "constant",
            "sample": 0.5,
        },
        "q6.xy.const.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q6.resonator.readout.wf.I": {
            "type": "constant",
            "sample": 0.31622776601683794,
        },
        "q6.resonator.readout.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q6.resonator.const.wf.I": {
            "type": "constant",
            "sample": 0.5,
        },
        "q6.resonator.const.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q7.xy.saturation.wf.I": {
            "type": "constant",
            "sample": 0.03981071705534972,
        },
        "q7.xy.saturation.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q7.xy.x180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0025776916503157127, 0.01024400574151878, 0.022800388765576485, 0.03992163699773022, 0.061164319102145016, 0.08597826077058386, 0.11372079394799796, 0.14367340159757425, 0.17506032691456946, 0.20706866502006654, 0.23886941677033918, 0.2696389593992218, 0.29858037791512293, 0.3249441047807083, 0.3480473333183877, 0.36729170204460276, 0.3821787919179461, 0.3923230351305265, 0.3974617011116639, 0.39746170111166396, 0.3923230351305265, 0.3821787919179461, 0.3672917020446029, 0.34804733331838783, 0.3249441047807083, 0.2985803779151228, 0.26963895939922183, 0.23886941677033927, 0.20706866502006654, 0.17506032691456963, 0.14367340159757439, 0.11372079394799806, 0.08597826077058393, 0.06116431910214504, 0.03992163699773022, 0.022800388765576465, 0.010244005741518757, 0.0025776916503157127, 0.0],
        },
        "q7.xy.x180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
        },
        "q7.xy.x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0012888458251578564, 0.00512200287075939, 0.011400194382788243, 0.01996081849886511, 0.030582159551072508, 0.04298913038529193, 0.05686039697399898, 0.07183670079878712, 0.08753016345728473, 0.10353433251003327, 0.11943470838516959, 0.1348194796996109, 0.14929018895756146, 0.16247205239035414, 0.17402366665919386, 0.18364585102230138, 0.19108939595897306, 0.19616151756526326, 0.19873085055583195, 0.19873085055583198, 0.19616151756526326, 0.19108939595897306, 0.18364585102230144, 0.17402366665919392, 0.16247205239035414, 0.1492901889575614, 0.13481947969961092, 0.11943470838516963, 0.10353433251003327, 0.08753016345728482, 0.07183670079878719, 0.05686039697399903, 0.042989130385291965, 0.03058215955107252, 0.01996081849886511, 0.011400194382788232, 0.005122002870759378, 0.0012888458251578564, 0.0],
        },
        "q7.xy.x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
        },
        "q7.xy.-x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -0.0012888458251578564, -0.00512200287075939, -0.011400194382788243, -0.01996081849886511, -0.030582159551072508, -0.04298913038529193, -0.05686039697399898, -0.07183670079878712, -0.08753016345728473, -0.10353433251003327, -0.11943470838516959, -0.1348194796996109, -0.14929018895756146, -0.16247205239035414, -0.17402366665919386, -0.18364585102230138, -0.19108939595897306, -0.19616151756526326, -0.19873085055583195, -0.19873085055583198, -0.19616151756526326, -0.19108939595897306, -0.18364585102230144, -0.17402366665919392, -0.16247205239035414, -0.1492901889575614, -0.13481947969961092, -0.11943470838516963, -0.10353433251003327, -0.08753016345728482, -0.07183670079878719, -0.05686039697399903, -0.042989130385291965, -0.03058215955107252, -0.01996081849886511, -0.011400194382788232, -0.005122002870759378, -0.0012888458251578564, 0.0],
        },
        "q7.xy.-x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 1.578380914373998e-19, 6.27264442089904e-19, 1.3961211560539257e-18, 2.4444952482996434e-18, 3.745234380523461e-18, 5.2646500924475986e-18, 6.96339031524557e-18, 8.797458569454076e-18, 1.0719353450680837e-17, 1.2679298891027e-17, 1.462653333309955e-17, 1.6510624427684005e-17, 1.8282775205098117e-17, 1.9897087891074827e-17, 2.1311752635006774e-17, 2.2490130363115307e-17, 2.3401701711215753e-17, 2.4022857460218697e-17, 2.433751000250306e-17, 2.4337510002503062e-17, 2.4022857460218697e-17, 2.3401701711215753e-17, 2.2490130363115313e-17, 2.131175263500678e-17, 1.9897087891074827e-17, 1.828277520509811e-17, 1.651062442768401e-17, 1.4626533333099555e-17, 1.2679298891027e-17, 1.0719353450680847e-17, 8.797458569454085e-18, 6.963390315245576e-18, 5.264650092447603e-18, 3.7452343805234614e-18, 2.4444952482996434e-18, 1.3961211560539245e-18, 6.272644420899027e-19, 1.578380914373998e-19, 0.0],
        },
        "q7.xy.y180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 1.578380914373998e-19, 6.27264442089904e-19, 1.3961211560539257e-18, 2.4444952482996434e-18, 3.745234380523461e-18, 5.2646500924475986e-18, 6.96339031524557e-18, 8.797458569454076e-18, 1.0719353450680837e-17, 1.2679298891027e-17, 1.462653333309955e-17, 1.6510624427684005e-17, 1.8282775205098117e-17, 1.9897087891074827e-17, 2.1311752635006774e-17, 2.2490130363115307e-17, 2.3401701711215753e-17, 2.4022857460218697e-17, 2.433751000250306e-17, 2.4337510002503062e-17, 2.4022857460218697e-17, 2.3401701711215753e-17, 2.2490130363115313e-17, 2.131175263500678e-17, 1.9897087891074827e-17, 1.828277520509811e-17, 1.651062442768401e-17, 1.4626533333099555e-17, 1.2679298891027e-17, 1.0719353450680847e-17, 8.797458569454085e-18, 6.963390315245576e-18, 5.264650092447603e-18, 3.7452343805234614e-18, 2.4444952482996434e-18, 1.3961211560539245e-18, 6.272644420899027e-19, 1.578380914373998e-19, 0.0],
        },
        "q7.xy.y180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0025776916503157127, 0.01024400574151878, 0.022800388765576485, 0.03992163699773022, 0.061164319102145016, 0.08597826077058386, 0.11372079394799796, 0.14367340159757425, 0.17506032691456946, 0.20706866502006654, 0.23886941677033918, 0.2696389593992218, 0.29858037791512293, 0.3249441047807083, 0.3480473333183877, 0.36729170204460276, 0.3821787919179461, 0.3923230351305265, 0.3974617011116639, 0.39746170111166396, 0.3923230351305265, 0.3821787919179461, 0.3672917020446029, 0.34804733331838783, 0.3249441047807083, 0.2985803779151228, 0.26963895939922183, 0.23886941677033927, 0.20706866502006654, 0.17506032691456963, 0.14367340159757439, 0.11372079394799806, 0.08597826077058393, 0.06116431910214504, 0.03992163699773022, 0.022800388765576465, 0.010244005741518757, 0.0025776916503157127, 0.0],
        },
        "q7.xy.y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 7.89190457186999e-20, 3.13632221044952e-19, 6.980605780269628e-19, 1.2222476241498217e-18, 1.8726171902617303e-18, 2.6323250462237993e-18, 3.481695157622785e-18, 4.398729284727038e-18, 5.359676725340419e-18, 6.3396494455135e-18, 7.313266666549774e-18, 8.255312213842003e-18, 9.141387602549059e-18, 9.948543945537414e-18, 1.0655876317503387e-17, 1.1245065181557654e-17, 1.1700850855607877e-17, 1.2011428730109348e-17, 1.216875500125153e-17, 1.2168755001251531e-17, 1.2011428730109348e-17, 1.1700850855607877e-17, 1.1245065181557657e-17, 1.065587631750339e-17, 9.948543945537414e-18, 9.141387602549055e-18, 8.255312213842004e-18, 7.313266666549777e-18, 6.3396494455135e-18, 5.359676725340423e-18, 4.3987292847270425e-18, 3.481695157622788e-18, 2.6323250462238016e-18, 1.8726171902617307e-18, 1.2222476241498217e-18, 6.980605780269622e-19, 3.1363222104495134e-19, 7.89190457186999e-20, 0.0],
        },
        "q7.xy.y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0012888458251578564, 0.00512200287075939, 0.011400194382788243, 0.01996081849886511, 0.030582159551072508, 0.04298913038529193, 0.05686039697399898, 0.07183670079878712, 0.08753016345728473, 0.10353433251003327, 0.11943470838516959, 0.1348194796996109, 0.14929018895756146, 0.16247205239035414, 0.17402366665919386, 0.18364585102230138, 0.19108939595897306, 0.19616151756526326, 0.19873085055583195, 0.19873085055583198, 0.19616151756526326, 0.19108939595897306, 0.18364585102230144, 0.17402366665919392, 0.16247205239035414, 0.1492901889575614, 0.13481947969961092, 0.11943470838516963, 0.10353433251003327, 0.08753016345728482, 0.07183670079878719, 0.05686039697399903, 0.042989130385291965, 0.03058215955107252, 0.01996081849886511, 0.011400194382788232, 0.005122002870759378, 0.0012888458251578564, 0.0],
        },
        "q7.xy.-y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 7.89190457186999e-20, 3.13632221044952e-19, 6.980605780269628e-19, 1.2222476241498217e-18, 1.8726171902617303e-18, 2.6323250462237993e-18, 3.481695157622785e-18, 4.398729284727038e-18, 5.359676725340419e-18, 6.3396494455135e-18, 7.313266666549774e-18, 8.255312213842003e-18, 9.141387602549059e-18, 9.948543945537414e-18, 1.0655876317503387e-17, 1.1245065181557654e-17, 1.1700850855607877e-17, 1.2011428730109348e-17, 1.216875500125153e-17, 1.2168755001251531e-17, 1.2011428730109348e-17, 1.1700850855607877e-17, 1.1245065181557657e-17, 1.065587631750339e-17, 9.948543945537414e-18, 9.141387602549055e-18, 8.255312213842004e-18, 7.313266666549777e-18, 6.3396494455135e-18, 5.359676725340423e-18, 4.3987292847270425e-18, 3.481695157622788e-18, 2.6323250462238016e-18, 1.8726171902617307e-18, 1.2222476241498217e-18, 6.980605780269622e-19, 3.1363222104495134e-19, 7.89190457186999e-20, 0.0],
        },
        "q7.xy.-y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.0012888458251578564, -0.00512200287075939, -0.011400194382788243, -0.01996081849886511, -0.030582159551072508, -0.04298913038529193, -0.05686039697399898, -0.07183670079878712, -0.08753016345728473, -0.10353433251003327, -0.11943470838516959, -0.1348194796996109, -0.14929018895756146, -0.16247205239035414, -0.17402366665919386, -0.18364585102230138, -0.19108939595897306, -0.19616151756526326, -0.19873085055583195, -0.19873085055583198, -0.19616151756526326, -0.19108939595897306, -0.18364585102230144, -0.17402366665919392, -0.16247205239035414, -0.1492901889575614, -0.13481947969961092, -0.11943470838516963, -0.10353433251003327, -0.08753016345728482, -0.07183670079878719, -0.05686039697399903, -0.042989130385291965, -0.03058215955107252, -0.01996081849886511, -0.011400194382788232, -0.005122002870759378, -0.0012888458251578564, 0.0],
        },
        "q7.xy.const.wf.I": {
            "type": "constant",
            "sample": 0.5,
        },
        "q7.xy.const.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q7.resonator.readout.wf.I": {
            "type": "constant",
            "sample": 0.31622776601683794,
        },
        "q7.resonator.readout.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q7.resonator.const.wf.I": {
            "type": "constant",
            "sample": 0.5,
        },
        "q7.resonator.const.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q8.xy.saturation.wf.I": {
            "type": "constant",
            "sample": 0.03981071705534972,
        },
        "q8.xy.saturation.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q8.xy.x180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0025776916503157127, 0.01024400574151878, 0.022800388765576485, 0.03992163699773022, 0.061164319102145016, 0.08597826077058386, 0.11372079394799796, 0.14367340159757425, 0.17506032691456946, 0.20706866502006654, 0.23886941677033918, 0.2696389593992218, 0.29858037791512293, 0.3249441047807083, 0.3480473333183877, 0.36729170204460276, 0.3821787919179461, 0.3923230351305265, 0.3974617011116639, 0.39746170111166396, 0.3923230351305265, 0.3821787919179461, 0.3672917020446029, 0.34804733331838783, 0.3249441047807083, 0.2985803779151228, 0.26963895939922183, 0.23886941677033927, 0.20706866502006654, 0.17506032691456963, 0.14367340159757439, 0.11372079394799806, 0.08597826077058393, 0.06116431910214504, 0.03992163699773022, 0.022800388765576465, 0.010244005741518757, 0.0025776916503157127, 0.0],
        },
        "q8.xy.x180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
        },
        "q8.xy.x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0012888458251578564, 0.00512200287075939, 0.011400194382788243, 0.01996081849886511, 0.030582159551072508, 0.04298913038529193, 0.05686039697399898, 0.07183670079878712, 0.08753016345728473, 0.10353433251003327, 0.11943470838516959, 0.1348194796996109, 0.14929018895756146, 0.16247205239035414, 0.17402366665919386, 0.18364585102230138, 0.19108939595897306, 0.19616151756526326, 0.19873085055583195, 0.19873085055583198, 0.19616151756526326, 0.19108939595897306, 0.18364585102230144, 0.17402366665919392, 0.16247205239035414, 0.1492901889575614, 0.13481947969961092, 0.11943470838516963, 0.10353433251003327, 0.08753016345728482, 0.07183670079878719, 0.05686039697399903, 0.042989130385291965, 0.03058215955107252, 0.01996081849886511, 0.011400194382788232, 0.005122002870759378, 0.0012888458251578564, 0.0],
        },
        "q8.xy.x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
        },
        "q8.xy.-x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -0.0012888458251578564, -0.00512200287075939, -0.011400194382788243, -0.01996081849886511, -0.030582159551072508, -0.04298913038529193, -0.05686039697399898, -0.07183670079878712, -0.08753016345728473, -0.10353433251003327, -0.11943470838516959, -0.1348194796996109, -0.14929018895756146, -0.16247205239035414, -0.17402366665919386, -0.18364585102230138, -0.19108939595897306, -0.19616151756526326, -0.19873085055583195, -0.19873085055583198, -0.19616151756526326, -0.19108939595897306, -0.18364585102230144, -0.17402366665919392, -0.16247205239035414, -0.1492901889575614, -0.13481947969961092, -0.11943470838516963, -0.10353433251003327, -0.08753016345728482, -0.07183670079878719, -0.05686039697399903, -0.042989130385291965, -0.03058215955107252, -0.01996081849886511, -0.011400194382788232, -0.005122002870759378, -0.0012888458251578564, 0.0],
        },
        "q8.xy.-x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 1.578380914373998e-19, 6.27264442089904e-19, 1.3961211560539257e-18, 2.4444952482996434e-18, 3.745234380523461e-18, 5.2646500924475986e-18, 6.96339031524557e-18, 8.797458569454076e-18, 1.0719353450680837e-17, 1.2679298891027e-17, 1.462653333309955e-17, 1.6510624427684005e-17, 1.8282775205098117e-17, 1.9897087891074827e-17, 2.1311752635006774e-17, 2.2490130363115307e-17, 2.3401701711215753e-17, 2.4022857460218697e-17, 2.433751000250306e-17, 2.4337510002503062e-17, 2.4022857460218697e-17, 2.3401701711215753e-17, 2.2490130363115313e-17, 2.131175263500678e-17, 1.9897087891074827e-17, 1.828277520509811e-17, 1.651062442768401e-17, 1.4626533333099555e-17, 1.2679298891027e-17, 1.0719353450680847e-17, 8.797458569454085e-18, 6.963390315245576e-18, 5.264650092447603e-18, 3.7452343805234614e-18, 2.4444952482996434e-18, 1.3961211560539245e-18, 6.272644420899027e-19, 1.578380914373998e-19, 0.0],
        },
        "q8.xy.y180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 1.578380914373998e-19, 6.27264442089904e-19, 1.3961211560539257e-18, 2.4444952482996434e-18, 3.745234380523461e-18, 5.2646500924475986e-18, 6.96339031524557e-18, 8.797458569454076e-18, 1.0719353450680837e-17, 1.2679298891027e-17, 1.462653333309955e-17, 1.6510624427684005e-17, 1.8282775205098117e-17, 1.9897087891074827e-17, 2.1311752635006774e-17, 2.2490130363115307e-17, 2.3401701711215753e-17, 2.4022857460218697e-17, 2.433751000250306e-17, 2.4337510002503062e-17, 2.4022857460218697e-17, 2.3401701711215753e-17, 2.2490130363115313e-17, 2.131175263500678e-17, 1.9897087891074827e-17, 1.828277520509811e-17, 1.651062442768401e-17, 1.4626533333099555e-17, 1.2679298891027e-17, 1.0719353450680847e-17, 8.797458569454085e-18, 6.963390315245576e-18, 5.264650092447603e-18, 3.7452343805234614e-18, 2.4444952482996434e-18, 1.3961211560539245e-18, 6.272644420899027e-19, 1.578380914373998e-19, 0.0],
        },
        "q8.xy.y180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0025776916503157127, 0.01024400574151878, 0.022800388765576485, 0.03992163699773022, 0.061164319102145016, 0.08597826077058386, 0.11372079394799796, 0.14367340159757425, 0.17506032691456946, 0.20706866502006654, 0.23886941677033918, 0.2696389593992218, 0.29858037791512293, 0.3249441047807083, 0.3480473333183877, 0.36729170204460276, 0.3821787919179461, 0.3923230351305265, 0.3974617011116639, 0.39746170111166396, 0.3923230351305265, 0.3821787919179461, 0.3672917020446029, 0.34804733331838783, 0.3249441047807083, 0.2985803779151228, 0.26963895939922183, 0.23886941677033927, 0.20706866502006654, 0.17506032691456963, 0.14367340159757439, 0.11372079394799806, 0.08597826077058393, 0.06116431910214504, 0.03992163699773022, 0.022800388765576465, 0.010244005741518757, 0.0025776916503157127, 0.0],
        },
        "q8.xy.y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 7.89190457186999e-20, 3.13632221044952e-19, 6.980605780269628e-19, 1.2222476241498217e-18, 1.8726171902617303e-18, 2.6323250462237993e-18, 3.481695157622785e-18, 4.398729284727038e-18, 5.359676725340419e-18, 6.3396494455135e-18, 7.313266666549774e-18, 8.255312213842003e-18, 9.141387602549059e-18, 9.948543945537414e-18, 1.0655876317503387e-17, 1.1245065181557654e-17, 1.1700850855607877e-17, 1.2011428730109348e-17, 1.216875500125153e-17, 1.2168755001251531e-17, 1.2011428730109348e-17, 1.1700850855607877e-17, 1.1245065181557657e-17, 1.065587631750339e-17, 9.948543945537414e-18, 9.141387602549055e-18, 8.255312213842004e-18, 7.313266666549777e-18, 6.3396494455135e-18, 5.359676725340423e-18, 4.3987292847270425e-18, 3.481695157622788e-18, 2.6323250462238016e-18, 1.8726171902617307e-18, 1.2222476241498217e-18, 6.980605780269622e-19, 3.1363222104495134e-19, 7.89190457186999e-20, 0.0],
        },
        "q8.xy.y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0012888458251578564, 0.00512200287075939, 0.011400194382788243, 0.01996081849886511, 0.030582159551072508, 0.04298913038529193, 0.05686039697399898, 0.07183670079878712, 0.08753016345728473, 0.10353433251003327, 0.11943470838516959, 0.1348194796996109, 0.14929018895756146, 0.16247205239035414, 0.17402366665919386, 0.18364585102230138, 0.19108939595897306, 0.19616151756526326, 0.19873085055583195, 0.19873085055583198, 0.19616151756526326, 0.19108939595897306, 0.18364585102230144, 0.17402366665919392, 0.16247205239035414, 0.1492901889575614, 0.13481947969961092, 0.11943470838516963, 0.10353433251003327, 0.08753016345728482, 0.07183670079878719, 0.05686039697399903, 0.042989130385291965, 0.03058215955107252, 0.01996081849886511, 0.011400194382788232, 0.005122002870759378, 0.0012888458251578564, 0.0],
        },
        "q8.xy.-y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 7.89190457186999e-20, 3.13632221044952e-19, 6.980605780269628e-19, 1.2222476241498217e-18, 1.8726171902617303e-18, 2.6323250462237993e-18, 3.481695157622785e-18, 4.398729284727038e-18, 5.359676725340419e-18, 6.3396494455135e-18, 7.313266666549774e-18, 8.255312213842003e-18, 9.141387602549059e-18, 9.948543945537414e-18, 1.0655876317503387e-17, 1.1245065181557654e-17, 1.1700850855607877e-17, 1.2011428730109348e-17, 1.216875500125153e-17, 1.2168755001251531e-17, 1.2011428730109348e-17, 1.1700850855607877e-17, 1.1245065181557657e-17, 1.065587631750339e-17, 9.948543945537414e-18, 9.141387602549055e-18, 8.255312213842004e-18, 7.313266666549777e-18, 6.3396494455135e-18, 5.359676725340423e-18, 4.3987292847270425e-18, 3.481695157622788e-18, 2.6323250462238016e-18, 1.8726171902617307e-18, 1.2222476241498217e-18, 6.980605780269622e-19, 3.1363222104495134e-19, 7.89190457186999e-20, 0.0],
        },
        "q8.xy.-y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.0012888458251578564, -0.00512200287075939, -0.011400194382788243, -0.01996081849886511, -0.030582159551072508, -0.04298913038529193, -0.05686039697399898, -0.07183670079878712, -0.08753016345728473, -0.10353433251003327, -0.11943470838516959, -0.1348194796996109, -0.14929018895756146, -0.16247205239035414, -0.17402366665919386, -0.18364585102230138, -0.19108939595897306, -0.19616151756526326, -0.19873085055583195, -0.19873085055583198, -0.19616151756526326, -0.19108939595897306, -0.18364585102230144, -0.17402366665919392, -0.16247205239035414, -0.1492901889575614, -0.13481947969961092, -0.11943470838516963, -0.10353433251003327, -0.08753016345728482, -0.07183670079878719, -0.05686039697399903, -0.042989130385291965, -0.03058215955107252, -0.01996081849886511, -0.011400194382788232, -0.005122002870759378, -0.0012888458251578564, 0.0],
        },
        "q8.xy.const.wf.I": {
            "type": "constant",
            "sample": 0.5,
        },
        "q8.xy.const.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q8.resonator.readout.wf.I": {
            "type": "constant",
            "sample": 0.31622776601683794,
        },
        "q8.resonator.readout.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q8.resonator.const.wf.I": {
            "type": "constant",
            "sample": 0.5,
        },
        "q8.resonator.const.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "cr_q1_q2.square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "cr_q1_q2.square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "cr_q5_q4.square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "cr_q5_q4.square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "zz_q5_q4.square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "zz_q5_q4.square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "cr_q2_q1.square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "cr_q2_q1.square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "cr_q2_q3.square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "cr_q2_q3.square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "cr_q3_q2.square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "cr_q3_q2.square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "cr_q3_q4.square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "cr_q3_q4.square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "cr_q4_q3.square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "cr_q4_q3.square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "cr_q4_q5.square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "cr_q4_q5.square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "cr_q5_q6.square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "cr_q5_q6.square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "cr_q6_q5.square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "cr_q6_q5.square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "cr_q6_q7.square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "cr_q6_q7.square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "cr_q7_q6.square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "cr_q7_q6.square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "cr_q7_q8.square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "cr_q7_q8.square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "cr_q8_q7.square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "cr_q8_q7.square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "cr_q8_q1.square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "cr_q8_q1.square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "cr_q1_q8.square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "cr_q1_q8.square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
    },
    "digital_waveforms": {
        "ON": {
            "samples": [[1, 0]],
        },
    },
    "integration_weights": {
        "q1.resonator.readout.iw1": {
            "cosine": [(1.0, 1000)],
            "sine": [(-0.0, 1000)],
        },
        "q1.resonator.readout.iw2": {
            "cosine": [(0.0, 1000)],
            "sine": [(1.0, 1000)],
        },
        "q1.resonator.readout.iw3": {
            "cosine": [(-0.0, 1000)],
            "sine": [(-1.0, 1000)],
        },
        "q2.resonator.readout.iw1": {
            "cosine": [(1.0, 1000)],
            "sine": [(-0.0, 1000)],
        },
        "q2.resonator.readout.iw2": {
            "cosine": [(0.0, 1000)],
            "sine": [(1.0, 1000)],
        },
        "q2.resonator.readout.iw3": {
            "cosine": [(-0.0, 1000)],
            "sine": [(-1.0, 1000)],
        },
        "q3.resonator.readout.iw1": {
            "cosine": [(1.0, 1000)],
            "sine": [(-0.0, 1000)],
        },
        "q3.resonator.readout.iw2": {
            "cosine": [(0.0, 1000)],
            "sine": [(1.0, 1000)],
        },
        "q3.resonator.readout.iw3": {
            "cosine": [(-0.0, 1000)],
            "sine": [(-1.0, 1000)],
        },
        "q4.resonator.readout.iw1": {
            "cosine": [(1.0, 1000)],
            "sine": [(-0.0, 1000)],
        },
        "q4.resonator.readout.iw2": {
            "cosine": [(0.0, 1000)],
            "sine": [(1.0, 1000)],
        },
        "q4.resonator.readout.iw3": {
            "cosine": [(-0.0, 1000)],
            "sine": [(-1.0, 1000)],
        },
        "q5.resonator.readout.iw1": {
            "cosine": [(1.0, 1000)],
            "sine": [(-0.0, 1000)],
        },
        "q5.resonator.readout.iw2": {
            "cosine": [(0.0, 1000)],
            "sine": [(1.0, 1000)],
        },
        "q5.resonator.readout.iw3": {
            "cosine": [(-0.0, 1000)],
            "sine": [(-1.0, 1000)],
        },
        "q6.resonator.readout.iw1": {
            "cosine": [(1.0, 1000)],
            "sine": [(-0.0, 1000)],
        },
        "q6.resonator.readout.iw2": {
            "cosine": [(0.0, 1000)],
            "sine": [(1.0, 1000)],
        },
        "q6.resonator.readout.iw3": {
            "cosine": [(-0.0, 1000)],
            "sine": [(-1.0, 1000)],
        },
        "q7.resonator.readout.iw1": {
            "cosine": [(1.0, 1000)],
            "sine": [(-0.0, 1000)],
        },
        "q7.resonator.readout.iw2": {
            "cosine": [(0.0, 1000)],
            "sine": [(1.0, 1000)],
        },
        "q7.resonator.readout.iw3": {
            "cosine": [(-0.0, 1000)],
            "sine": [(-1.0, 1000)],
        },
        "q8.resonator.readout.iw1": {
            "cosine": [(1.0, 1000)],
            "sine": [(-0.0, 1000)],
        },
        "q8.resonator.readout.iw2": {
            "cosine": [(0.0, 1000)],
            "sine": [(1.0, 1000)],
        },
        "q8.resonator.readout.iw3": {
            "cosine": [(-0.0, 1000)],
            "sine": [(-1.0, 1000)],
        },
    },
    "mixers": {},
    "oscillators": {},
}

loaded_config = {
    "version": 1,
    "controllers": {
        "con1": {
            "type": "opx1000",
            "fems": {
                "1": {
                    "type": "MW",
                    "analog_outputs": {
                        "1": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": -2,
                            "band": 1,
                            "delay": 0,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 4750000000.0,
                                },
                            },
                        },
                    },
                    "analog_inputs": {
                        "2": {
                            "band": 1,
                            "shareable": False,
                            "gain_db": 0,
                            "sampling_rate": 1000000000.0,
                            "downconverter_frequency": 4750000000.0,
                        },
                    },
                },
                "2": {
                    "type": "MW",
                    "analog_outputs": {
                        "1": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": -2,
                            "band": 2,
                            "delay": 0,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 6000000000.0,
                                },
                            },
                        },
                        "2": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": -2,
                            "band": 2,
                            "delay": 0,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 6100000000.0,
                                },
                            },
                        },
                        "3": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": -2,
                            "band": 2,
                            "delay": 0,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 6500000000.0,
                                },
                            },
                        },
                        "4": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": -2,
                            "band": 2,
                            "delay": 0,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 6800000000.0,
                                },
                            },
                        },
                        "5": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": -2,
                            "band": 2,
                            "delay": 0,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 7100000000.0,
                                },
                            },
                        },
                        "6": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": -2,
                            "band": 2,
                            "delay": 0,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 7100000000.0,
                                },
                            },
                        },
                        "7": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": -2,
                            "band": 2,
                            "delay": 0,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 7100000000.0,
                                },
                            },
                        },
                        "8": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": -2,
                            "band": 2,
                            "delay": 0,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 7100000000.0,
                                },
                            },
                        },
                    },
                },
            },
        },
    },
    "oscillators": {},
    "elements": {
        "q1.xy": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "saturation": "q1.xy.saturation.pulse",
                "x180_DragCosine": "q1.xy.x180_DragCosine.pulse",
                "x90_DragCosine": "q1.xy.x90_DragCosine.pulse",
                "-x90_DragCosine": "q1.xy.-x90_DragCosine.pulse",
                "y180_DragCosine": "q1.xy.y180_DragCosine.pulse",
                "y90_DragCosine": "q1.xy.y90_DragCosine.pulse",
                "-y90_DragCosine": "q1.xy.-y90_DragCosine.pulse",
                "x180": "q1.xy.x180_DragCosine.pulse",
                "x90": "q1.xy.x90_DragCosine.pulse",
                "-x90": "q1.xy.-x90_DragCosine.pulse",
                "y180": "q1.xy.y180_DragCosine.pulse",
                "y90": "q1.xy.y90_DragCosine.pulse",
                "-y90": "q1.xy.-y90_DragCosine.pulse",
                "const": "q1.xy.const.pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "MWInput": {
                "port": ('con1', 2, 1),
                "upconverter": 1,
            },
            "intermediate_frequency": 12000000.0,
        },
        "q1.resonator": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "readout": "q1.resonator.readout.pulse",
                "const": "q1.resonator.const.pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "MWInput": {
                "port": ('con1', 1, 1),
                "upconverter": 1,
            },
            "MWOutput": {
                "port": ('con1', 1, 2),
            },
            "smearing": 0,
            "time_of_flight": 28,
            "intermediate_frequency": -355000000.0,
        },
        "q2.xy": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "saturation": "q2.xy.saturation.pulse",
                "x180_DragCosine": "q2.xy.x180_DragCosine.pulse",
                "x90_DragCosine": "q2.xy.x90_DragCosine.pulse",
                "-x90_DragCosine": "q2.xy.-x90_DragCosine.pulse",
                "y180_DragCosine": "q2.xy.y180_DragCosine.pulse",
                "y90_DragCosine": "q2.xy.y90_DragCosine.pulse",
                "-y90_DragCosine": "q2.xy.-y90_DragCosine.pulse",
                "x180": "q2.xy.x180_DragCosine.pulse",
                "x90": "q2.xy.x90_DragCosine.pulse",
                "-x90": "q2.xy.-x90_DragCosine.pulse",
                "y180": "q2.xy.y180_DragCosine.pulse",
                "y90": "q2.xy.y90_DragCosine.pulse",
                "-y90": "q2.xy.-y90_DragCosine.pulse",
                "const": "q2.xy.const.pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "MWInput": {
                "port": ('con1', 2, 2),
                "upconverter": 1,
            },
            "intermediate_frequency": 321000000.0,
        },
        "q2.resonator": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "readout": "q2.resonator.readout.pulse",
                "const": "q2.resonator.const.pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "MWInput": {
                "port": ('con1', 1, 1),
                "upconverter": 1,
            },
            "MWOutput": {
                "port": ('con1', 1, 2),
            },
            "smearing": 0,
            "time_of_flight": 28,
            "intermediate_frequency": -338000000.0,
        },
        "q3.xy": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "saturation": "q3.xy.saturation.pulse",
                "x180_DragCosine": "q3.xy.x180_DragCosine.pulse",
                "x90_DragCosine": "q3.xy.x90_DragCosine.pulse",
                "-x90_DragCosine": "q3.xy.-x90_DragCosine.pulse",
                "y180_DragCosine": "q3.xy.y180_DragCosine.pulse",
                "y90_DragCosine": "q3.xy.y90_DragCosine.pulse",
                "-y90_DragCosine": "q3.xy.-y90_DragCosine.pulse",
                "x180": "q3.xy.x180_DragCosine.pulse",
                "x90": "q3.xy.x90_DragCosine.pulse",
                "-x90": "q3.xy.-x90_DragCosine.pulse",
                "y180": "q3.xy.y180_DragCosine.pulse",
                "y90": "q3.xy.y90_DragCosine.pulse",
                "-y90": "q3.xy.-y90_DragCosine.pulse",
                "const": "q3.xy.const.pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "MWInput": {
                "port": ('con1', 2, 3),
                "upconverter": 1,
            },
            "intermediate_frequency": 285000000.0,
        },
        "q3.resonator": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "readout": "q3.resonator.readout.pulse",
                "const": "q3.resonator.const.pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "MWInput": {
                "port": ('con1', 1, 1),
                "upconverter": 1,
            },
            "MWOutput": {
                "port": ('con1', 1, 2),
            },
            "smearing": 0,
            "time_of_flight": 28,
            "intermediate_frequency": -229000000.0,
        },
        "q4.xy": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "saturation": "q4.xy.saturation.pulse",
                "x180_DragCosine": "q4.xy.x180_DragCosine.pulse",
                "x90_DragCosine": "q4.xy.x90_DragCosine.pulse",
                "-x90_DragCosine": "q4.xy.-x90_DragCosine.pulse",
                "y180_DragCosine": "q4.xy.y180_DragCosine.pulse",
                "y90_DragCosine": "q4.xy.y90_DragCosine.pulse",
                "-y90_DragCosine": "q4.xy.-y90_DragCosine.pulse",
                "x180": "q4.xy.x180_DragCosine.pulse",
                "x90": "q4.xy.x90_DragCosine.pulse",
                "-x90": "q4.xy.-x90_DragCosine.pulse",
                "y180": "q4.xy.y180_DragCosine.pulse",
                "y90": "q4.xy.y90_DragCosine.pulse",
                "-y90": "q4.xy.-y90_DragCosine.pulse",
                "const": "q4.xy.const.pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "MWInput": {
                "port": ('con1', 2, 4),
                "upconverter": 1,
            },
            "intermediate_frequency": 201000000.0,
        },
        "q4.resonator": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "readout": "q4.resonator.readout.pulse",
                "const": "q4.resonator.const.pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "MWInput": {
                "port": ('con1', 1, 1),
                "upconverter": 1,
            },
            "MWOutput": {
                "port": ('con1', 1, 2),
            },
            "smearing": 0,
            "time_of_flight": 28,
            "intermediate_frequency": -22000000.0,
        },
        "q5.xy": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "saturation": "q5.xy.saturation.pulse",
                "x180_DragCosine": "q5.xy.x180_DragCosine.pulse",
                "x90_DragCosine": "q5.xy.x90_DragCosine.pulse",
                "-x90_DragCosine": "q5.xy.-x90_DragCosine.pulse",
                "y180_DragCosine": "q5.xy.y180_DragCosine.pulse",
                "y90_DragCosine": "q5.xy.y90_DragCosine.pulse",
                "-y90_DragCosine": "q5.xy.-y90_DragCosine.pulse",
                "x180": "q5.xy.x180_DragCosine.pulse",
                "x90": "q5.xy.x90_DragCosine.pulse",
                "-x90": "q5.xy.-x90_DragCosine.pulse",
                "y180": "q5.xy.y180_DragCosine.pulse",
                "y90": "q5.xy.y90_DragCosine.pulse",
                "-y90": "q5.xy.-y90_DragCosine.pulse",
                "const": "q5.xy.const.pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "MWInput": {
                "port": ('con1', 2, 5),
                "upconverter": 1,
            },
            "intermediate_frequency": -17000000.0,
        },
        "q5.resonator": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "readout": "q5.resonator.readout.pulse",
                "const": "q5.resonator.const.pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "MWInput": {
                "port": ('con1', 1, 1),
                "upconverter": 1,
            },
            "MWOutput": {
                "port": ('con1', 1, 2),
            },
            "smearing": 0,
            "time_of_flight": 28,
            "intermediate_frequency": 165000000.0,
        },
        "q6.xy": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "saturation": "q6.xy.saturation.pulse",
                "x180_DragCosine": "q6.xy.x180_DragCosine.pulse",
                "x90_DragCosine": "q6.xy.x90_DragCosine.pulse",
                "-x90_DragCosine": "q6.xy.-x90_DragCosine.pulse",
                "y180_DragCosine": "q6.xy.y180_DragCosine.pulse",
                "y90_DragCosine": "q6.xy.y90_DragCosine.pulse",
                "-y90_DragCosine": "q6.xy.-y90_DragCosine.pulse",
                "x180": "q6.xy.x180_DragCosine.pulse",
                "x90": "q6.xy.x90_DragCosine.pulse",
                "-x90": "q6.xy.-x90_DragCosine.pulse",
                "y180": "q6.xy.y180_DragCosine.pulse",
                "y90": "q6.xy.y90_DragCosine.pulse",
                "-y90": "q6.xy.-y90_DragCosine.pulse",
                "const": "q6.xy.const.pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "MWInput": {
                "port": ('con1', 2, 6),
                "upconverter": 1,
            },
            "intermediate_frequency": 21000000.0,
        },
        "q6.resonator": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "readout": "q6.resonator.readout.pulse",
                "const": "q6.resonator.const.pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "MWInput": {
                "port": ('con1', 1, 1),
                "upconverter": 1,
            },
            "MWOutput": {
                "port": ('con1', 1, 2),
            },
            "smearing": 0,
            "time_of_flight": 28,
            "intermediate_frequency": 250000000.0,
        },
        "q7.xy": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "saturation": "q7.xy.saturation.pulse",
                "x180_DragCosine": "q7.xy.x180_DragCosine.pulse",
                "x90_DragCosine": "q7.xy.x90_DragCosine.pulse",
                "-x90_DragCosine": "q7.xy.-x90_DragCosine.pulse",
                "y180_DragCosine": "q7.xy.y180_DragCosine.pulse",
                "y90_DragCosine": "q7.xy.y90_DragCosine.pulse",
                "-y90_DragCosine": "q7.xy.-y90_DragCosine.pulse",
                "x180": "q7.xy.x180_DragCosine.pulse",
                "x90": "q7.xy.x90_DragCosine.pulse",
                "-x90": "q7.xy.-x90_DragCosine.pulse",
                "y180": "q7.xy.y180_DragCosine.pulse",
                "y90": "q7.xy.y90_DragCosine.pulse",
                "-y90": "q7.xy.-y90_DragCosine.pulse",
                "const": "q7.xy.const.pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "MWInput": {
                "port": ('con1', 2, 7),
                "upconverter": 1,
            },
            "intermediate_frequency": 84000000.0,
        },
        "q7.resonator": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "readout": "q7.resonator.readout.pulse",
                "const": "q7.resonator.const.pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "MWInput": {
                "port": ('con1', 1, 1),
                "upconverter": 1,
            },
            "MWOutput": {
                "port": ('con1', 1, 2),
            },
            "smearing": 0,
            "time_of_flight": 28,
            "intermediate_frequency": 312500000.0,
        },
        "q8.xy": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "saturation": "q8.xy.saturation.pulse",
                "x180_DragCosine": "q8.xy.x180_DragCosine.pulse",
                "x90_DragCosine": "q8.xy.x90_DragCosine.pulse",
                "-x90_DragCosine": "q8.xy.-x90_DragCosine.pulse",
                "y180_DragCosine": "q8.xy.y180_DragCosine.pulse",
                "y90_DragCosine": "q8.xy.y90_DragCosine.pulse",
                "-y90_DragCosine": "q8.xy.-y90_DragCosine.pulse",
                "x180": "q8.xy.x180_DragCosine.pulse",
                "x90": "q8.xy.x90_DragCosine.pulse",
                "-x90": "q8.xy.-x90_DragCosine.pulse",
                "y180": "q8.xy.y180_DragCosine.pulse",
                "y90": "q8.xy.y90_DragCosine.pulse",
                "-y90": "q8.xy.-y90_DragCosine.pulse",
                "const": "q8.xy.const.pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "MWInput": {
                "port": ('con1', 2, 8),
                "upconverter": 1,
            },
            "intermediate_frequency": 154000000.0,
        },
        "q8.resonator": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "readout": "q8.resonator.readout.pulse",
                "const": "q8.resonator.const.pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "MWInput": {
                "port": ('con1', 1, 1),
                "upconverter": 1,
            },
            "MWOutput": {
                "port": ('con1', 1, 2),
            },
            "smearing": 0,
            "time_of_flight": 28,
            "intermediate_frequency": 350000000.0,
        },
        "cr_q1_q2": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "square": "cr_q1_q2.square.pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "MWInput": {
                "port": ('con1', 2, 1),
                "upconverter": 1,
            },
        },
        "cr_q5_q4": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "square": "cr_q5_q4.square.pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "MWInput": {
                "port": ('con1', 2, 5),
                "upconverter": 1,
            },
        },
        "zz_q5_q4": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "square": "zz_q5_q4.square.pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "MWInput": {
                "port": ('con1', 2, 1),
                "upconverter": 1,
            },
        },
        "cr_q2_q1": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "square": "cr_q2_q1.square.pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "MWInput": {
                "port": ('con1', 2, 2),
                "upconverter": 1,
            },
        },
        "cr_q2_q3": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "square": "cr_q2_q3.square.pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "MWInput": {
                "port": ('con1', 2, 2),
                "upconverter": 1,
            },
        },
        "cr_q3_q2": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "square": "cr_q3_q2.square.pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "MWInput": {
                "port": ('con1', 2, 3),
                "upconverter": 1,
            },
        },
        "cr_q3_q4": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "square": "cr_q3_q4.square.pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "MWInput": {
                "port": ('con1', 2, 3),
                "upconverter": 1,
            },
        },
        "cr_q4_q3": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "square": "cr_q4_q3.square.pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "MWInput": {
                "port": ('con1', 2, 4),
                "upconverter": 1,
            },
        },
        "cr_q4_q5": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "square": "cr_q4_q5.square.pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "MWInput": {
                "port": ('con1', 2, 4),
                "upconverter": 1,
            },
        },
        "cr_q5_q6": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "square": "cr_q5_q6.square.pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "MWInput": {
                "port": ('con1', 2, 5),
                "upconverter": 1,
            },
        },
        "cr_q6_q5": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "square": "cr_q6_q5.square.pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "MWInput": {
                "port": ('con1', 2, 6),
                "upconverter": 1,
            },
        },
        "cr_q6_q7": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "square": "cr_q6_q7.square.pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "MWInput": {
                "port": ('con1', 2, 6),
                "upconverter": 1,
            },
        },
        "cr_q7_q6": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "square": "cr_q7_q6.square.pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "MWInput": {
                "port": ('con1', 2, 7),
                "upconverter": 1,
            },
        },
        "cr_q7_q8": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "square": "cr_q7_q8.square.pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "MWInput": {
                "port": ('con1', 2, 7),
                "upconverter": 1,
            },
        },
        "cr_q8_q7": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "square": "cr_q8_q7.square.pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "MWInput": {
                "port": ('con1', 2, 8),
                "upconverter": 1,
            },
        },
        "cr_q8_q1": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "square": "cr_q8_q1.square.pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "MWInput": {
                "port": ('con1', 2, 8),
                "upconverter": 1,
            },
        },
        "cr_q1_q8": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "square": "cr_q1_q8.square.pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "MWInput": {
                "port": ('con1', 2, 1),
                "upconverter": 1,
            },
        },
    },
    "pulses": {
        "const_pulse": {
            "length": 1000,
            "waveforms": {
                "I": "const_wf",
                "Q": "zero_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q1.xy.saturation.pulse": {
            "length": 20000,
            "waveforms": {
                "I": "q1.xy.saturation.wf.I",
                "Q": "q1.xy.saturation.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q1.xy.x180_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q1.xy.x180_DragCosine.wf.I",
                "Q": "q1.xy.x180_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q1.xy.x90_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q1.xy.x90_DragCosine.wf.I",
                "Q": "q1.xy.x90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q1.xy.-x90_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q1.xy.-x90_DragCosine.wf.I",
                "Q": "q1.xy.-x90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q1.xy.y180_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q1.xy.y180_DragCosine.wf.I",
                "Q": "q1.xy.y180_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q1.xy.y90_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q1.xy.y90_DragCosine.wf.I",
                "Q": "q1.xy.y90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q1.xy.-y90_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q1.xy.-y90_DragCosine.wf.I",
                "Q": "q1.xy.-y90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q1.xy.const.pulse": {
            "length": 1000,
            "waveforms": {
                "I": "q1.xy.const.wf.I",
                "Q": "q1.xy.const.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q1.resonator.readout.pulse": {
            "length": 1000,
            "waveforms": {
                "I": "q1.resonator.readout.wf.I",
                "Q": "q1.resonator.readout.wf.Q",
            },
            "integration_weights": {
                "iw1": "q1.resonator.readout.iw1",
                "iw2": "q1.resonator.readout.iw2",
                "iw3": "q1.resonator.readout.iw3",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "q1.resonator.const.pulse": {
            "length": 1000,
            "waveforms": {
                "I": "q1.resonator.const.wf.I",
                "Q": "q1.resonator.const.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q2.xy.saturation.pulse": {
            "length": 20000,
            "waveforms": {
                "I": "q2.xy.saturation.wf.I",
                "Q": "q2.xy.saturation.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q2.xy.x180_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q2.xy.x180_DragCosine.wf.I",
                "Q": "q2.xy.x180_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q2.xy.x90_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q2.xy.x90_DragCosine.wf.I",
                "Q": "q2.xy.x90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q2.xy.-x90_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q2.xy.-x90_DragCosine.wf.I",
                "Q": "q2.xy.-x90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q2.xy.y180_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q2.xy.y180_DragCosine.wf.I",
                "Q": "q2.xy.y180_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q2.xy.y90_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q2.xy.y90_DragCosine.wf.I",
                "Q": "q2.xy.y90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q2.xy.-y90_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q2.xy.-y90_DragCosine.wf.I",
                "Q": "q2.xy.-y90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q2.xy.const.pulse": {
            "length": 1000,
            "waveforms": {
                "I": "q2.xy.const.wf.I",
                "Q": "q2.xy.const.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q2.resonator.readout.pulse": {
            "length": 1000,
            "waveforms": {
                "I": "q2.resonator.readout.wf.I",
                "Q": "q2.resonator.readout.wf.Q",
            },
            "integration_weights": {
                "iw1": "q2.resonator.readout.iw1",
                "iw2": "q2.resonator.readout.iw2",
                "iw3": "q2.resonator.readout.iw3",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "q2.resonator.const.pulse": {
            "length": 1000,
            "waveforms": {
                "I": "q2.resonator.const.wf.I",
                "Q": "q2.resonator.const.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q3.xy.saturation.pulse": {
            "length": 20000,
            "waveforms": {
                "I": "q3.xy.saturation.wf.I",
                "Q": "q3.xy.saturation.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q3.xy.x180_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q3.xy.x180_DragCosine.wf.I",
                "Q": "q3.xy.x180_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q3.xy.x90_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q3.xy.x90_DragCosine.wf.I",
                "Q": "q3.xy.x90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q3.xy.-x90_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q3.xy.-x90_DragCosine.wf.I",
                "Q": "q3.xy.-x90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q3.xy.y180_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q3.xy.y180_DragCosine.wf.I",
                "Q": "q3.xy.y180_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q3.xy.y90_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q3.xy.y90_DragCosine.wf.I",
                "Q": "q3.xy.y90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q3.xy.-y90_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q3.xy.-y90_DragCosine.wf.I",
                "Q": "q3.xy.-y90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q3.xy.const.pulse": {
            "length": 1000,
            "waveforms": {
                "I": "q3.xy.const.wf.I",
                "Q": "q3.xy.const.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q3.resonator.readout.pulse": {
            "length": 1000,
            "waveforms": {
                "I": "q3.resonator.readout.wf.I",
                "Q": "q3.resonator.readout.wf.Q",
            },
            "integration_weights": {
                "iw1": "q3.resonator.readout.iw1",
                "iw2": "q3.resonator.readout.iw2",
                "iw3": "q3.resonator.readout.iw3",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "q3.resonator.const.pulse": {
            "length": 1000,
            "waveforms": {
                "I": "q3.resonator.const.wf.I",
                "Q": "q3.resonator.const.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q4.xy.saturation.pulse": {
            "length": 20000,
            "waveforms": {
                "I": "q4.xy.saturation.wf.I",
                "Q": "q4.xy.saturation.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q4.xy.x180_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q4.xy.x180_DragCosine.wf.I",
                "Q": "q4.xy.x180_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q4.xy.x90_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q4.xy.x90_DragCosine.wf.I",
                "Q": "q4.xy.x90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q4.xy.-x90_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q4.xy.-x90_DragCosine.wf.I",
                "Q": "q4.xy.-x90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q4.xy.y180_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q4.xy.y180_DragCosine.wf.I",
                "Q": "q4.xy.y180_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q4.xy.y90_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q4.xy.y90_DragCosine.wf.I",
                "Q": "q4.xy.y90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q4.xy.-y90_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q4.xy.-y90_DragCosine.wf.I",
                "Q": "q4.xy.-y90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q4.xy.const.pulse": {
            "length": 1000,
            "waveforms": {
                "I": "q4.xy.const.wf.I",
                "Q": "q4.xy.const.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q4.resonator.readout.pulse": {
            "length": 1000,
            "waveforms": {
                "I": "q4.resonator.readout.wf.I",
                "Q": "q4.resonator.readout.wf.Q",
            },
            "integration_weights": {
                "iw1": "q4.resonator.readout.iw1",
                "iw2": "q4.resonator.readout.iw2",
                "iw3": "q4.resonator.readout.iw3",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "q4.resonator.const.pulse": {
            "length": 1000,
            "waveforms": {
                "I": "q4.resonator.const.wf.I",
                "Q": "q4.resonator.const.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q5.xy.saturation.pulse": {
            "length": 20000,
            "waveforms": {
                "I": "q5.xy.saturation.wf.I",
                "Q": "q5.xy.saturation.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q5.xy.x180_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q5.xy.x180_DragCosine.wf.I",
                "Q": "q5.xy.x180_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q5.xy.x90_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q5.xy.x90_DragCosine.wf.I",
                "Q": "q5.xy.x90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q5.xy.-x90_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q5.xy.-x90_DragCosine.wf.I",
                "Q": "q5.xy.-x90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q5.xy.y180_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q5.xy.y180_DragCosine.wf.I",
                "Q": "q5.xy.y180_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q5.xy.y90_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q5.xy.y90_DragCosine.wf.I",
                "Q": "q5.xy.y90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q5.xy.-y90_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q5.xy.-y90_DragCosine.wf.I",
                "Q": "q5.xy.-y90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q5.xy.const.pulse": {
            "length": 1000,
            "waveforms": {
                "I": "q5.xy.const.wf.I",
                "Q": "q5.xy.const.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q5.resonator.readout.pulse": {
            "length": 1000,
            "waveforms": {
                "I": "q5.resonator.readout.wf.I",
                "Q": "q5.resonator.readout.wf.Q",
            },
            "integration_weights": {
                "iw1": "q5.resonator.readout.iw1",
                "iw2": "q5.resonator.readout.iw2",
                "iw3": "q5.resonator.readout.iw3",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "q5.resonator.const.pulse": {
            "length": 1000,
            "waveforms": {
                "I": "q5.resonator.const.wf.I",
                "Q": "q5.resonator.const.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q6.xy.saturation.pulse": {
            "length": 20000,
            "waveforms": {
                "I": "q6.xy.saturation.wf.I",
                "Q": "q6.xy.saturation.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q6.xy.x180_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q6.xy.x180_DragCosine.wf.I",
                "Q": "q6.xy.x180_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q6.xy.x90_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q6.xy.x90_DragCosine.wf.I",
                "Q": "q6.xy.x90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q6.xy.-x90_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q6.xy.-x90_DragCosine.wf.I",
                "Q": "q6.xy.-x90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q6.xy.y180_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q6.xy.y180_DragCosine.wf.I",
                "Q": "q6.xy.y180_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q6.xy.y90_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q6.xy.y90_DragCosine.wf.I",
                "Q": "q6.xy.y90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q6.xy.-y90_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q6.xy.-y90_DragCosine.wf.I",
                "Q": "q6.xy.-y90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q6.xy.const.pulse": {
            "length": 1000,
            "waveforms": {
                "I": "q6.xy.const.wf.I",
                "Q": "q6.xy.const.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q6.resonator.readout.pulse": {
            "length": 1000,
            "waveforms": {
                "I": "q6.resonator.readout.wf.I",
                "Q": "q6.resonator.readout.wf.Q",
            },
            "integration_weights": {
                "iw1": "q6.resonator.readout.iw1",
                "iw2": "q6.resonator.readout.iw2",
                "iw3": "q6.resonator.readout.iw3",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "q6.resonator.const.pulse": {
            "length": 1000,
            "waveforms": {
                "I": "q6.resonator.const.wf.I",
                "Q": "q6.resonator.const.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q7.xy.saturation.pulse": {
            "length": 20000,
            "waveforms": {
                "I": "q7.xy.saturation.wf.I",
                "Q": "q7.xy.saturation.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q7.xy.x180_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q7.xy.x180_DragCosine.wf.I",
                "Q": "q7.xy.x180_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q7.xy.x90_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q7.xy.x90_DragCosine.wf.I",
                "Q": "q7.xy.x90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q7.xy.-x90_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q7.xy.-x90_DragCosine.wf.I",
                "Q": "q7.xy.-x90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q7.xy.y180_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q7.xy.y180_DragCosine.wf.I",
                "Q": "q7.xy.y180_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q7.xy.y90_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q7.xy.y90_DragCosine.wf.I",
                "Q": "q7.xy.y90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q7.xy.-y90_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q7.xy.-y90_DragCosine.wf.I",
                "Q": "q7.xy.-y90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q7.xy.const.pulse": {
            "length": 1000,
            "waveforms": {
                "I": "q7.xy.const.wf.I",
                "Q": "q7.xy.const.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q7.resonator.readout.pulse": {
            "length": 1000,
            "waveforms": {
                "I": "q7.resonator.readout.wf.I",
                "Q": "q7.resonator.readout.wf.Q",
            },
            "integration_weights": {
                "iw1": "q7.resonator.readout.iw1",
                "iw2": "q7.resonator.readout.iw2",
                "iw3": "q7.resonator.readout.iw3",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "q7.resonator.const.pulse": {
            "length": 1000,
            "waveforms": {
                "I": "q7.resonator.const.wf.I",
                "Q": "q7.resonator.const.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q8.xy.saturation.pulse": {
            "length": 20000,
            "waveforms": {
                "I": "q8.xy.saturation.wf.I",
                "Q": "q8.xy.saturation.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q8.xy.x180_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q8.xy.x180_DragCosine.wf.I",
                "Q": "q8.xy.x180_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q8.xy.x90_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q8.xy.x90_DragCosine.wf.I",
                "Q": "q8.xy.x90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q8.xy.-x90_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q8.xy.-x90_DragCosine.wf.I",
                "Q": "q8.xy.-x90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q8.xy.y180_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q8.xy.y180_DragCosine.wf.I",
                "Q": "q8.xy.y180_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q8.xy.y90_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q8.xy.y90_DragCosine.wf.I",
                "Q": "q8.xy.y90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q8.xy.-y90_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q8.xy.-y90_DragCosine.wf.I",
                "Q": "q8.xy.-y90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q8.xy.const.pulse": {
            "length": 1000,
            "waveforms": {
                "I": "q8.xy.const.wf.I",
                "Q": "q8.xy.const.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q8.resonator.readout.pulse": {
            "length": 1000,
            "waveforms": {
                "I": "q8.resonator.readout.wf.I",
                "Q": "q8.resonator.readout.wf.Q",
            },
            "integration_weights": {
                "iw1": "q8.resonator.readout.iw1",
                "iw2": "q8.resonator.readout.iw2",
                "iw3": "q8.resonator.readout.iw3",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "q8.resonator.const.pulse": {
            "length": 1000,
            "waveforms": {
                "I": "q8.resonator.const.wf.I",
                "Q": "q8.resonator.const.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "cr_q1_q2.square.pulse": {
            "length": 100,
            "waveforms": {
                "I": "cr_q1_q2.square.wf.I",
                "Q": "cr_q1_q2.square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "cr_q5_q4.square.pulse": {
            "length": 100,
            "waveforms": {
                "I": "cr_q5_q4.square.wf.I",
                "Q": "cr_q5_q4.square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "zz_q5_q4.square.pulse": {
            "length": 100,
            "waveforms": {
                "I": "zz_q5_q4.square.wf.I",
                "Q": "zz_q5_q4.square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "cr_q2_q1.square.pulse": {
            "length": 100,
            "waveforms": {
                "I": "cr_q2_q1.square.wf.I",
                "Q": "cr_q2_q1.square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "cr_q2_q3.square.pulse": {
            "length": 100,
            "waveforms": {
                "I": "cr_q2_q3.square.wf.I",
                "Q": "cr_q2_q3.square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "cr_q3_q2.square.pulse": {
            "length": 100,
            "waveforms": {
                "I": "cr_q3_q2.square.wf.I",
                "Q": "cr_q3_q2.square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "cr_q3_q4.square.pulse": {
            "length": 100,
            "waveforms": {
                "I": "cr_q3_q4.square.wf.I",
                "Q": "cr_q3_q4.square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "cr_q4_q3.square.pulse": {
            "length": 100,
            "waveforms": {
                "I": "cr_q4_q3.square.wf.I",
                "Q": "cr_q4_q3.square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "cr_q4_q5.square.pulse": {
            "length": 100,
            "waveforms": {
                "I": "cr_q4_q5.square.wf.I",
                "Q": "cr_q4_q5.square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "cr_q5_q6.square.pulse": {
            "length": 100,
            "waveforms": {
                "I": "cr_q5_q6.square.wf.I",
                "Q": "cr_q5_q6.square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "cr_q6_q5.square.pulse": {
            "length": 100,
            "waveforms": {
                "I": "cr_q6_q5.square.wf.I",
                "Q": "cr_q6_q5.square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "cr_q6_q7.square.pulse": {
            "length": 100,
            "waveforms": {
                "I": "cr_q6_q7.square.wf.I",
                "Q": "cr_q6_q7.square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "cr_q7_q6.square.pulse": {
            "length": 100,
            "waveforms": {
                "I": "cr_q7_q6.square.wf.I",
                "Q": "cr_q7_q6.square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "cr_q7_q8.square.pulse": {
            "length": 100,
            "waveforms": {
                "I": "cr_q7_q8.square.wf.I",
                "Q": "cr_q7_q8.square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "cr_q8_q7.square.pulse": {
            "length": 100,
            "waveforms": {
                "I": "cr_q8_q7.square.wf.I",
                "Q": "cr_q8_q7.square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "cr_q8_q1.square.pulse": {
            "length": 100,
            "waveforms": {
                "I": "cr_q8_q1.square.wf.I",
                "Q": "cr_q8_q1.square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "cr_q1_q8.square.pulse": {
            "length": 100,
            "waveforms": {
                "I": "cr_q1_q8.square.wf.I",
                "Q": "cr_q1_q8.square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
    },
    "waveforms": {
        "zero_wf": {
            "type": "constant",
            "sample": 0.0,
        },
        "const_wf": {
            "type": "constant",
            "sample": 0.1,
        },
        "q1.xy.saturation.wf.I": {
            "type": "constant",
            "sample": 0.03981071705534972,
        },
        "q1.xy.saturation.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q1.xy.x180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0025776916503157127, 0.01024400574151878, 0.022800388765576485, 0.03992163699773022, 0.061164319102145016, 0.08597826077058386, 0.11372079394799796, 0.14367340159757425, 0.17506032691456946, 0.20706866502006654, 0.23886941677033918, 0.2696389593992218, 0.29858037791512293, 0.3249441047807083, 0.3480473333183877, 0.36729170204460276, 0.3821787919179461, 0.3923230351305265, 0.3974617011116639, 0.39746170111166396, 0.3923230351305265, 0.3821787919179461, 0.3672917020446029, 0.34804733331838783, 0.3249441047807083, 0.2985803779151228, 0.26963895939922183, 0.23886941677033927, 0.20706866502006654, 0.17506032691456963, 0.14367340159757439, 0.11372079394799806, 0.08597826077058393, 0.06116431910214504, 0.03992163699773022, 0.022800388765576465, 0.010244005741518757, 0.0025776916503157127, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.xy.x180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.xy.x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0012888458251578564, 0.00512200287075939, 0.011400194382788243, 0.01996081849886511, 0.030582159551072508, 0.04298913038529193, 0.05686039697399898, 0.07183670079878712, 0.08753016345728473, 0.10353433251003327, 0.11943470838516959, 0.1348194796996109, 0.14929018895756146, 0.16247205239035414, 0.17402366665919386, 0.18364585102230138, 0.19108939595897306, 0.19616151756526326, 0.19873085055583195, 0.19873085055583198, 0.19616151756526326, 0.19108939595897306, 0.18364585102230144, 0.17402366665919392, 0.16247205239035414, 0.1492901889575614, 0.13481947969961092, 0.11943470838516963, 0.10353433251003327, 0.08753016345728482, 0.07183670079878719, 0.05686039697399903, 0.042989130385291965, 0.03058215955107252, 0.01996081849886511, 0.011400194382788232, 0.005122002870759378, 0.0012888458251578564, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.xy.x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.xy.-x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -0.0012888458251578564, -0.00512200287075939, -0.011400194382788243, -0.01996081849886511, -0.030582159551072508, -0.04298913038529193, -0.05686039697399898, -0.07183670079878712, -0.08753016345728473, -0.10353433251003327, -0.11943470838516959, -0.1348194796996109, -0.14929018895756146, -0.16247205239035414, -0.17402366665919386, -0.18364585102230138, -0.19108939595897306, -0.19616151756526326, -0.19873085055583195, -0.19873085055583198, -0.19616151756526326, -0.19108939595897306, -0.18364585102230144, -0.17402366665919392, -0.16247205239035414, -0.1492901889575614, -0.13481947969961092, -0.11943470838516963, -0.10353433251003327, -0.08753016345728482, -0.07183670079878719, -0.05686039697399903, -0.042989130385291965, -0.03058215955107252, -0.01996081849886511, -0.011400194382788232, -0.005122002870759378, -0.0012888458251578564, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.xy.-x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 1.578380914373998e-19, 6.27264442089904e-19, 1.3961211560539257e-18, 2.4444952482996434e-18, 3.745234380523461e-18, 5.2646500924475986e-18, 6.96339031524557e-18, 8.797458569454076e-18, 1.0719353450680837e-17, 1.2679298891027e-17, 1.462653333309955e-17, 1.6510624427684005e-17, 1.8282775205098117e-17, 1.9897087891074827e-17, 2.1311752635006774e-17, 2.2490130363115307e-17, 2.3401701711215753e-17, 2.4022857460218697e-17, 2.433751000250306e-17, 2.4337510002503062e-17, 2.4022857460218697e-17, 2.3401701711215753e-17, 2.2490130363115313e-17, 2.131175263500678e-17, 1.9897087891074827e-17, 1.828277520509811e-17, 1.651062442768401e-17, 1.4626533333099555e-17, 1.2679298891027e-17, 1.0719353450680847e-17, 8.797458569454085e-18, 6.963390315245576e-18, 5.264650092447603e-18, 3.7452343805234614e-18, 2.4444952482996434e-18, 1.3961211560539245e-18, 6.272644420899027e-19, 1.578380914373998e-19, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.xy.y180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 1.578380914373998e-19, 6.27264442089904e-19, 1.3961211560539257e-18, 2.4444952482996434e-18, 3.745234380523461e-18, 5.2646500924475986e-18, 6.96339031524557e-18, 8.797458569454076e-18, 1.0719353450680837e-17, 1.2679298891027e-17, 1.462653333309955e-17, 1.6510624427684005e-17, 1.8282775205098117e-17, 1.9897087891074827e-17, 2.1311752635006774e-17, 2.2490130363115307e-17, 2.3401701711215753e-17, 2.4022857460218697e-17, 2.433751000250306e-17, 2.4337510002503062e-17, 2.4022857460218697e-17, 2.3401701711215753e-17, 2.2490130363115313e-17, 2.131175263500678e-17, 1.9897087891074827e-17, 1.828277520509811e-17, 1.651062442768401e-17, 1.4626533333099555e-17, 1.2679298891027e-17, 1.0719353450680847e-17, 8.797458569454085e-18, 6.963390315245576e-18, 5.264650092447603e-18, 3.7452343805234614e-18, 2.4444952482996434e-18, 1.3961211560539245e-18, 6.272644420899027e-19, 1.578380914373998e-19, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.xy.y180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0025776916503157127, 0.01024400574151878, 0.022800388765576485, 0.03992163699773022, 0.061164319102145016, 0.08597826077058386, 0.11372079394799796, 0.14367340159757425, 0.17506032691456946, 0.20706866502006654, 0.23886941677033918, 0.2696389593992218, 0.29858037791512293, 0.3249441047807083, 0.3480473333183877, 0.36729170204460276, 0.3821787919179461, 0.3923230351305265, 0.3974617011116639, 0.39746170111166396, 0.3923230351305265, 0.3821787919179461, 0.3672917020446029, 0.34804733331838783, 0.3249441047807083, 0.2985803779151228, 0.26963895939922183, 0.23886941677033927, 0.20706866502006654, 0.17506032691456963, 0.14367340159757439, 0.11372079394799806, 0.08597826077058393, 0.06116431910214504, 0.03992163699773022, 0.022800388765576465, 0.010244005741518757, 0.0025776916503157127, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.xy.y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 7.89190457186999e-20, 3.13632221044952e-19, 6.980605780269628e-19, 1.2222476241498217e-18, 1.8726171902617303e-18, 2.6323250462237993e-18, 3.481695157622785e-18, 4.398729284727038e-18, 5.359676725340419e-18, 6.3396494455135e-18, 7.313266666549774e-18, 8.255312213842003e-18, 9.141387602549059e-18, 9.948543945537414e-18, 1.0655876317503387e-17, 1.1245065181557654e-17, 1.1700850855607877e-17, 1.2011428730109348e-17, 1.216875500125153e-17, 1.2168755001251531e-17, 1.2011428730109348e-17, 1.1700850855607877e-17, 1.1245065181557657e-17, 1.065587631750339e-17, 9.948543945537414e-18, 9.141387602549055e-18, 8.255312213842004e-18, 7.313266666549777e-18, 6.3396494455135e-18, 5.359676725340423e-18, 4.3987292847270425e-18, 3.481695157622788e-18, 2.6323250462238016e-18, 1.8726171902617307e-18, 1.2222476241498217e-18, 6.980605780269622e-19, 3.1363222104495134e-19, 7.89190457186999e-20, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.xy.y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0012888458251578564, 0.00512200287075939, 0.011400194382788243, 0.01996081849886511, 0.030582159551072508, 0.04298913038529193, 0.05686039697399898, 0.07183670079878712, 0.08753016345728473, 0.10353433251003327, 0.11943470838516959, 0.1348194796996109, 0.14929018895756146, 0.16247205239035414, 0.17402366665919386, 0.18364585102230138, 0.19108939595897306, 0.19616151756526326, 0.19873085055583195, 0.19873085055583198, 0.19616151756526326, 0.19108939595897306, 0.18364585102230144, 0.17402366665919392, 0.16247205239035414, 0.1492901889575614, 0.13481947969961092, 0.11943470838516963, 0.10353433251003327, 0.08753016345728482, 0.07183670079878719, 0.05686039697399903, 0.042989130385291965, 0.03058215955107252, 0.01996081849886511, 0.011400194382788232, 0.005122002870759378, 0.0012888458251578564, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.xy.-y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 7.89190457186999e-20, 3.13632221044952e-19, 6.980605780269628e-19, 1.2222476241498217e-18, 1.8726171902617303e-18, 2.6323250462237993e-18, 3.481695157622785e-18, 4.398729284727038e-18, 5.359676725340419e-18, 6.3396494455135e-18, 7.313266666549774e-18, 8.255312213842003e-18, 9.141387602549059e-18, 9.948543945537414e-18, 1.0655876317503387e-17, 1.1245065181557654e-17, 1.1700850855607877e-17, 1.2011428730109348e-17, 1.216875500125153e-17, 1.2168755001251531e-17, 1.2011428730109348e-17, 1.1700850855607877e-17, 1.1245065181557657e-17, 1.065587631750339e-17, 9.948543945537414e-18, 9.141387602549055e-18, 8.255312213842004e-18, 7.313266666549777e-18, 6.3396494455135e-18, 5.359676725340423e-18, 4.3987292847270425e-18, 3.481695157622788e-18, 2.6323250462238016e-18, 1.8726171902617307e-18, 1.2222476241498217e-18, 6.980605780269622e-19, 3.1363222104495134e-19, 7.89190457186999e-20, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.xy.-y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.0012888458251578564, -0.00512200287075939, -0.011400194382788243, -0.01996081849886511, -0.030582159551072508, -0.04298913038529193, -0.05686039697399898, -0.07183670079878712, -0.08753016345728473, -0.10353433251003327, -0.11943470838516959, -0.1348194796996109, -0.14929018895756146, -0.16247205239035414, -0.17402366665919386, -0.18364585102230138, -0.19108939595897306, -0.19616151756526326, -0.19873085055583195, -0.19873085055583198, -0.19616151756526326, -0.19108939595897306, -0.18364585102230144, -0.17402366665919392, -0.16247205239035414, -0.1492901889575614, -0.13481947969961092, -0.11943470838516963, -0.10353433251003327, -0.08753016345728482, -0.07183670079878719, -0.05686039697399903, -0.042989130385291965, -0.03058215955107252, -0.01996081849886511, -0.011400194382788232, -0.005122002870759378, -0.0012888458251578564, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.xy.const.wf.I": {
            "type": "constant",
            "sample": 0.5,
        },
        "q1.xy.const.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q1.resonator.readout.wf.I": {
            "type": "constant",
            "sample": 0.31622776601683794,
        },
        "q1.resonator.readout.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q1.resonator.const.wf.I": {
            "type": "constant",
            "sample": 0.5,
        },
        "q1.resonator.const.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q2.xy.saturation.wf.I": {
            "type": "constant",
            "sample": 0.03981071705534972,
        },
        "q2.xy.saturation.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q2.xy.x180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0025776916503157127, 0.01024400574151878, 0.022800388765576485, 0.03992163699773022, 0.061164319102145016, 0.08597826077058386, 0.11372079394799796, 0.14367340159757425, 0.17506032691456946, 0.20706866502006654, 0.23886941677033918, 0.2696389593992218, 0.29858037791512293, 0.3249441047807083, 0.3480473333183877, 0.36729170204460276, 0.3821787919179461, 0.3923230351305265, 0.3974617011116639, 0.39746170111166396, 0.3923230351305265, 0.3821787919179461, 0.3672917020446029, 0.34804733331838783, 0.3249441047807083, 0.2985803779151228, 0.26963895939922183, 0.23886941677033927, 0.20706866502006654, 0.17506032691456963, 0.14367340159757439, 0.11372079394799806, 0.08597826077058393, 0.06116431910214504, 0.03992163699773022, 0.022800388765576465, 0.010244005741518757, 0.0025776916503157127, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.xy.x180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.xy.x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0012888458251578564, 0.00512200287075939, 0.011400194382788243, 0.01996081849886511, 0.030582159551072508, 0.04298913038529193, 0.05686039697399898, 0.07183670079878712, 0.08753016345728473, 0.10353433251003327, 0.11943470838516959, 0.1348194796996109, 0.14929018895756146, 0.16247205239035414, 0.17402366665919386, 0.18364585102230138, 0.19108939595897306, 0.19616151756526326, 0.19873085055583195, 0.19873085055583198, 0.19616151756526326, 0.19108939595897306, 0.18364585102230144, 0.17402366665919392, 0.16247205239035414, 0.1492901889575614, 0.13481947969961092, 0.11943470838516963, 0.10353433251003327, 0.08753016345728482, 0.07183670079878719, 0.05686039697399903, 0.042989130385291965, 0.03058215955107252, 0.01996081849886511, 0.011400194382788232, 0.005122002870759378, 0.0012888458251578564, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.xy.x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.xy.-x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -0.0012888458251578564, -0.00512200287075939, -0.011400194382788243, -0.01996081849886511, -0.030582159551072508, -0.04298913038529193, -0.05686039697399898, -0.07183670079878712, -0.08753016345728473, -0.10353433251003327, -0.11943470838516959, -0.1348194796996109, -0.14929018895756146, -0.16247205239035414, -0.17402366665919386, -0.18364585102230138, -0.19108939595897306, -0.19616151756526326, -0.19873085055583195, -0.19873085055583198, -0.19616151756526326, -0.19108939595897306, -0.18364585102230144, -0.17402366665919392, -0.16247205239035414, -0.1492901889575614, -0.13481947969961092, -0.11943470838516963, -0.10353433251003327, -0.08753016345728482, -0.07183670079878719, -0.05686039697399903, -0.042989130385291965, -0.03058215955107252, -0.01996081849886511, -0.011400194382788232, -0.005122002870759378, -0.0012888458251578564, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.xy.-x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 1.578380914373998e-19, 6.27264442089904e-19, 1.3961211560539257e-18, 2.4444952482996434e-18, 3.745234380523461e-18, 5.2646500924475986e-18, 6.96339031524557e-18, 8.797458569454076e-18, 1.0719353450680837e-17, 1.2679298891027e-17, 1.462653333309955e-17, 1.6510624427684005e-17, 1.8282775205098117e-17, 1.9897087891074827e-17, 2.1311752635006774e-17, 2.2490130363115307e-17, 2.3401701711215753e-17, 2.4022857460218697e-17, 2.433751000250306e-17, 2.4337510002503062e-17, 2.4022857460218697e-17, 2.3401701711215753e-17, 2.2490130363115313e-17, 2.131175263500678e-17, 1.9897087891074827e-17, 1.828277520509811e-17, 1.651062442768401e-17, 1.4626533333099555e-17, 1.2679298891027e-17, 1.0719353450680847e-17, 8.797458569454085e-18, 6.963390315245576e-18, 5.264650092447603e-18, 3.7452343805234614e-18, 2.4444952482996434e-18, 1.3961211560539245e-18, 6.272644420899027e-19, 1.578380914373998e-19, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.xy.y180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 1.578380914373998e-19, 6.27264442089904e-19, 1.3961211560539257e-18, 2.4444952482996434e-18, 3.745234380523461e-18, 5.2646500924475986e-18, 6.96339031524557e-18, 8.797458569454076e-18, 1.0719353450680837e-17, 1.2679298891027e-17, 1.462653333309955e-17, 1.6510624427684005e-17, 1.8282775205098117e-17, 1.9897087891074827e-17, 2.1311752635006774e-17, 2.2490130363115307e-17, 2.3401701711215753e-17, 2.4022857460218697e-17, 2.433751000250306e-17, 2.4337510002503062e-17, 2.4022857460218697e-17, 2.3401701711215753e-17, 2.2490130363115313e-17, 2.131175263500678e-17, 1.9897087891074827e-17, 1.828277520509811e-17, 1.651062442768401e-17, 1.4626533333099555e-17, 1.2679298891027e-17, 1.0719353450680847e-17, 8.797458569454085e-18, 6.963390315245576e-18, 5.264650092447603e-18, 3.7452343805234614e-18, 2.4444952482996434e-18, 1.3961211560539245e-18, 6.272644420899027e-19, 1.578380914373998e-19, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.xy.y180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0025776916503157127, 0.01024400574151878, 0.022800388765576485, 0.03992163699773022, 0.061164319102145016, 0.08597826077058386, 0.11372079394799796, 0.14367340159757425, 0.17506032691456946, 0.20706866502006654, 0.23886941677033918, 0.2696389593992218, 0.29858037791512293, 0.3249441047807083, 0.3480473333183877, 0.36729170204460276, 0.3821787919179461, 0.3923230351305265, 0.3974617011116639, 0.39746170111166396, 0.3923230351305265, 0.3821787919179461, 0.3672917020446029, 0.34804733331838783, 0.3249441047807083, 0.2985803779151228, 0.26963895939922183, 0.23886941677033927, 0.20706866502006654, 0.17506032691456963, 0.14367340159757439, 0.11372079394799806, 0.08597826077058393, 0.06116431910214504, 0.03992163699773022, 0.022800388765576465, 0.010244005741518757, 0.0025776916503157127, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.xy.y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 7.89190457186999e-20, 3.13632221044952e-19, 6.980605780269628e-19, 1.2222476241498217e-18, 1.8726171902617303e-18, 2.6323250462237993e-18, 3.481695157622785e-18, 4.398729284727038e-18, 5.359676725340419e-18, 6.3396494455135e-18, 7.313266666549774e-18, 8.255312213842003e-18, 9.141387602549059e-18, 9.948543945537414e-18, 1.0655876317503387e-17, 1.1245065181557654e-17, 1.1700850855607877e-17, 1.2011428730109348e-17, 1.216875500125153e-17, 1.2168755001251531e-17, 1.2011428730109348e-17, 1.1700850855607877e-17, 1.1245065181557657e-17, 1.065587631750339e-17, 9.948543945537414e-18, 9.141387602549055e-18, 8.255312213842004e-18, 7.313266666549777e-18, 6.3396494455135e-18, 5.359676725340423e-18, 4.3987292847270425e-18, 3.481695157622788e-18, 2.6323250462238016e-18, 1.8726171902617307e-18, 1.2222476241498217e-18, 6.980605780269622e-19, 3.1363222104495134e-19, 7.89190457186999e-20, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.xy.y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0012888458251578564, 0.00512200287075939, 0.011400194382788243, 0.01996081849886511, 0.030582159551072508, 0.04298913038529193, 0.05686039697399898, 0.07183670079878712, 0.08753016345728473, 0.10353433251003327, 0.11943470838516959, 0.1348194796996109, 0.14929018895756146, 0.16247205239035414, 0.17402366665919386, 0.18364585102230138, 0.19108939595897306, 0.19616151756526326, 0.19873085055583195, 0.19873085055583198, 0.19616151756526326, 0.19108939595897306, 0.18364585102230144, 0.17402366665919392, 0.16247205239035414, 0.1492901889575614, 0.13481947969961092, 0.11943470838516963, 0.10353433251003327, 0.08753016345728482, 0.07183670079878719, 0.05686039697399903, 0.042989130385291965, 0.03058215955107252, 0.01996081849886511, 0.011400194382788232, 0.005122002870759378, 0.0012888458251578564, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.xy.-y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 7.89190457186999e-20, 3.13632221044952e-19, 6.980605780269628e-19, 1.2222476241498217e-18, 1.8726171902617303e-18, 2.6323250462237993e-18, 3.481695157622785e-18, 4.398729284727038e-18, 5.359676725340419e-18, 6.3396494455135e-18, 7.313266666549774e-18, 8.255312213842003e-18, 9.141387602549059e-18, 9.948543945537414e-18, 1.0655876317503387e-17, 1.1245065181557654e-17, 1.1700850855607877e-17, 1.2011428730109348e-17, 1.216875500125153e-17, 1.2168755001251531e-17, 1.2011428730109348e-17, 1.1700850855607877e-17, 1.1245065181557657e-17, 1.065587631750339e-17, 9.948543945537414e-18, 9.141387602549055e-18, 8.255312213842004e-18, 7.313266666549777e-18, 6.3396494455135e-18, 5.359676725340423e-18, 4.3987292847270425e-18, 3.481695157622788e-18, 2.6323250462238016e-18, 1.8726171902617307e-18, 1.2222476241498217e-18, 6.980605780269622e-19, 3.1363222104495134e-19, 7.89190457186999e-20, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.xy.-y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.0012888458251578564, -0.00512200287075939, -0.011400194382788243, -0.01996081849886511, -0.030582159551072508, -0.04298913038529193, -0.05686039697399898, -0.07183670079878712, -0.08753016345728473, -0.10353433251003327, -0.11943470838516959, -0.1348194796996109, -0.14929018895756146, -0.16247205239035414, -0.17402366665919386, -0.18364585102230138, -0.19108939595897306, -0.19616151756526326, -0.19873085055583195, -0.19873085055583198, -0.19616151756526326, -0.19108939595897306, -0.18364585102230144, -0.17402366665919392, -0.16247205239035414, -0.1492901889575614, -0.13481947969961092, -0.11943470838516963, -0.10353433251003327, -0.08753016345728482, -0.07183670079878719, -0.05686039697399903, -0.042989130385291965, -0.03058215955107252, -0.01996081849886511, -0.011400194382788232, -0.005122002870759378, -0.0012888458251578564, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.xy.const.wf.I": {
            "type": "constant",
            "sample": 0.5,
        },
        "q2.xy.const.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q2.resonator.readout.wf.I": {
            "type": "constant",
            "sample": 0.31622776601683794,
        },
        "q2.resonator.readout.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q2.resonator.const.wf.I": {
            "type": "constant",
            "sample": 0.5,
        },
        "q2.resonator.const.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q3.xy.saturation.wf.I": {
            "type": "constant",
            "sample": 0.03981071705534972,
        },
        "q3.xy.saturation.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q3.xy.x180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0025776916503157127, 0.01024400574151878, 0.022800388765576485, 0.03992163699773022, 0.061164319102145016, 0.08597826077058386, 0.11372079394799796, 0.14367340159757425, 0.17506032691456946, 0.20706866502006654, 0.23886941677033918, 0.2696389593992218, 0.29858037791512293, 0.3249441047807083, 0.3480473333183877, 0.36729170204460276, 0.3821787919179461, 0.3923230351305265, 0.3974617011116639, 0.39746170111166396, 0.3923230351305265, 0.3821787919179461, 0.3672917020446029, 0.34804733331838783, 0.3249441047807083, 0.2985803779151228, 0.26963895939922183, 0.23886941677033927, 0.20706866502006654, 0.17506032691456963, 0.14367340159757439, 0.11372079394799806, 0.08597826077058393, 0.06116431910214504, 0.03992163699773022, 0.022800388765576465, 0.010244005741518757, 0.0025776916503157127, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q3.xy.x180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q3.xy.x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0012888458251578564, 0.00512200287075939, 0.011400194382788243, 0.01996081849886511, 0.030582159551072508, 0.04298913038529193, 0.05686039697399898, 0.07183670079878712, 0.08753016345728473, 0.10353433251003327, 0.11943470838516959, 0.1348194796996109, 0.14929018895756146, 0.16247205239035414, 0.17402366665919386, 0.18364585102230138, 0.19108939595897306, 0.19616151756526326, 0.19873085055583195, 0.19873085055583198, 0.19616151756526326, 0.19108939595897306, 0.18364585102230144, 0.17402366665919392, 0.16247205239035414, 0.1492901889575614, 0.13481947969961092, 0.11943470838516963, 0.10353433251003327, 0.08753016345728482, 0.07183670079878719, 0.05686039697399903, 0.042989130385291965, 0.03058215955107252, 0.01996081849886511, 0.011400194382788232, 0.005122002870759378, 0.0012888458251578564, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q3.xy.x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q3.xy.-x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -0.0012888458251578564, -0.00512200287075939, -0.011400194382788243, -0.01996081849886511, -0.030582159551072508, -0.04298913038529193, -0.05686039697399898, -0.07183670079878712, -0.08753016345728473, -0.10353433251003327, -0.11943470838516959, -0.1348194796996109, -0.14929018895756146, -0.16247205239035414, -0.17402366665919386, -0.18364585102230138, -0.19108939595897306, -0.19616151756526326, -0.19873085055583195, -0.19873085055583198, -0.19616151756526326, -0.19108939595897306, -0.18364585102230144, -0.17402366665919392, -0.16247205239035414, -0.1492901889575614, -0.13481947969961092, -0.11943470838516963, -0.10353433251003327, -0.08753016345728482, -0.07183670079878719, -0.05686039697399903, -0.042989130385291965, -0.03058215955107252, -0.01996081849886511, -0.011400194382788232, -0.005122002870759378, -0.0012888458251578564, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q3.xy.-x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 1.578380914373998e-19, 6.27264442089904e-19, 1.3961211560539257e-18, 2.4444952482996434e-18, 3.745234380523461e-18, 5.2646500924475986e-18, 6.96339031524557e-18, 8.797458569454076e-18, 1.0719353450680837e-17, 1.2679298891027e-17, 1.462653333309955e-17, 1.6510624427684005e-17, 1.8282775205098117e-17, 1.9897087891074827e-17, 2.1311752635006774e-17, 2.2490130363115307e-17, 2.3401701711215753e-17, 2.4022857460218697e-17, 2.433751000250306e-17, 2.4337510002503062e-17, 2.4022857460218697e-17, 2.3401701711215753e-17, 2.2490130363115313e-17, 2.131175263500678e-17, 1.9897087891074827e-17, 1.828277520509811e-17, 1.651062442768401e-17, 1.4626533333099555e-17, 1.2679298891027e-17, 1.0719353450680847e-17, 8.797458569454085e-18, 6.963390315245576e-18, 5.264650092447603e-18, 3.7452343805234614e-18, 2.4444952482996434e-18, 1.3961211560539245e-18, 6.272644420899027e-19, 1.578380914373998e-19, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q3.xy.y180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 1.578380914373998e-19, 6.27264442089904e-19, 1.3961211560539257e-18, 2.4444952482996434e-18, 3.745234380523461e-18, 5.2646500924475986e-18, 6.96339031524557e-18, 8.797458569454076e-18, 1.0719353450680837e-17, 1.2679298891027e-17, 1.462653333309955e-17, 1.6510624427684005e-17, 1.8282775205098117e-17, 1.9897087891074827e-17, 2.1311752635006774e-17, 2.2490130363115307e-17, 2.3401701711215753e-17, 2.4022857460218697e-17, 2.433751000250306e-17, 2.4337510002503062e-17, 2.4022857460218697e-17, 2.3401701711215753e-17, 2.2490130363115313e-17, 2.131175263500678e-17, 1.9897087891074827e-17, 1.828277520509811e-17, 1.651062442768401e-17, 1.4626533333099555e-17, 1.2679298891027e-17, 1.0719353450680847e-17, 8.797458569454085e-18, 6.963390315245576e-18, 5.264650092447603e-18, 3.7452343805234614e-18, 2.4444952482996434e-18, 1.3961211560539245e-18, 6.272644420899027e-19, 1.578380914373998e-19, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q3.xy.y180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0025776916503157127, 0.01024400574151878, 0.022800388765576485, 0.03992163699773022, 0.061164319102145016, 0.08597826077058386, 0.11372079394799796, 0.14367340159757425, 0.17506032691456946, 0.20706866502006654, 0.23886941677033918, 0.2696389593992218, 0.29858037791512293, 0.3249441047807083, 0.3480473333183877, 0.36729170204460276, 0.3821787919179461, 0.3923230351305265, 0.3974617011116639, 0.39746170111166396, 0.3923230351305265, 0.3821787919179461, 0.3672917020446029, 0.34804733331838783, 0.3249441047807083, 0.2985803779151228, 0.26963895939922183, 0.23886941677033927, 0.20706866502006654, 0.17506032691456963, 0.14367340159757439, 0.11372079394799806, 0.08597826077058393, 0.06116431910214504, 0.03992163699773022, 0.022800388765576465, 0.010244005741518757, 0.0025776916503157127, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q3.xy.y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 7.89190457186999e-20, 3.13632221044952e-19, 6.980605780269628e-19, 1.2222476241498217e-18, 1.8726171902617303e-18, 2.6323250462237993e-18, 3.481695157622785e-18, 4.398729284727038e-18, 5.359676725340419e-18, 6.3396494455135e-18, 7.313266666549774e-18, 8.255312213842003e-18, 9.141387602549059e-18, 9.948543945537414e-18, 1.0655876317503387e-17, 1.1245065181557654e-17, 1.1700850855607877e-17, 1.2011428730109348e-17, 1.216875500125153e-17, 1.2168755001251531e-17, 1.2011428730109348e-17, 1.1700850855607877e-17, 1.1245065181557657e-17, 1.065587631750339e-17, 9.948543945537414e-18, 9.141387602549055e-18, 8.255312213842004e-18, 7.313266666549777e-18, 6.3396494455135e-18, 5.359676725340423e-18, 4.3987292847270425e-18, 3.481695157622788e-18, 2.6323250462238016e-18, 1.8726171902617307e-18, 1.2222476241498217e-18, 6.980605780269622e-19, 3.1363222104495134e-19, 7.89190457186999e-20, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q3.xy.y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0012888458251578564, 0.00512200287075939, 0.011400194382788243, 0.01996081849886511, 0.030582159551072508, 0.04298913038529193, 0.05686039697399898, 0.07183670079878712, 0.08753016345728473, 0.10353433251003327, 0.11943470838516959, 0.1348194796996109, 0.14929018895756146, 0.16247205239035414, 0.17402366665919386, 0.18364585102230138, 0.19108939595897306, 0.19616151756526326, 0.19873085055583195, 0.19873085055583198, 0.19616151756526326, 0.19108939595897306, 0.18364585102230144, 0.17402366665919392, 0.16247205239035414, 0.1492901889575614, 0.13481947969961092, 0.11943470838516963, 0.10353433251003327, 0.08753016345728482, 0.07183670079878719, 0.05686039697399903, 0.042989130385291965, 0.03058215955107252, 0.01996081849886511, 0.011400194382788232, 0.005122002870759378, 0.0012888458251578564, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q3.xy.-y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 7.89190457186999e-20, 3.13632221044952e-19, 6.980605780269628e-19, 1.2222476241498217e-18, 1.8726171902617303e-18, 2.6323250462237993e-18, 3.481695157622785e-18, 4.398729284727038e-18, 5.359676725340419e-18, 6.3396494455135e-18, 7.313266666549774e-18, 8.255312213842003e-18, 9.141387602549059e-18, 9.948543945537414e-18, 1.0655876317503387e-17, 1.1245065181557654e-17, 1.1700850855607877e-17, 1.2011428730109348e-17, 1.216875500125153e-17, 1.2168755001251531e-17, 1.2011428730109348e-17, 1.1700850855607877e-17, 1.1245065181557657e-17, 1.065587631750339e-17, 9.948543945537414e-18, 9.141387602549055e-18, 8.255312213842004e-18, 7.313266666549777e-18, 6.3396494455135e-18, 5.359676725340423e-18, 4.3987292847270425e-18, 3.481695157622788e-18, 2.6323250462238016e-18, 1.8726171902617307e-18, 1.2222476241498217e-18, 6.980605780269622e-19, 3.1363222104495134e-19, 7.89190457186999e-20, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q3.xy.-y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.0012888458251578564, -0.00512200287075939, -0.011400194382788243, -0.01996081849886511, -0.030582159551072508, -0.04298913038529193, -0.05686039697399898, -0.07183670079878712, -0.08753016345728473, -0.10353433251003327, -0.11943470838516959, -0.1348194796996109, -0.14929018895756146, -0.16247205239035414, -0.17402366665919386, -0.18364585102230138, -0.19108939595897306, -0.19616151756526326, -0.19873085055583195, -0.19873085055583198, -0.19616151756526326, -0.19108939595897306, -0.18364585102230144, -0.17402366665919392, -0.16247205239035414, -0.1492901889575614, -0.13481947969961092, -0.11943470838516963, -0.10353433251003327, -0.08753016345728482, -0.07183670079878719, -0.05686039697399903, -0.042989130385291965, -0.03058215955107252, -0.01996081849886511, -0.011400194382788232, -0.005122002870759378, -0.0012888458251578564, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q3.xy.const.wf.I": {
            "type": "constant",
            "sample": 0.5,
        },
        "q3.xy.const.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q3.resonator.readout.wf.I": {
            "type": "constant",
            "sample": 0.31622776601683794,
        },
        "q3.resonator.readout.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q3.resonator.const.wf.I": {
            "type": "constant",
            "sample": 0.5,
        },
        "q3.resonator.const.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q4.xy.saturation.wf.I": {
            "type": "constant",
            "sample": 0.03981071705534972,
        },
        "q4.xy.saturation.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q4.xy.x180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0025776916503157127, 0.01024400574151878, 0.022800388765576485, 0.03992163699773022, 0.061164319102145016, 0.08597826077058386, 0.11372079394799796, 0.14367340159757425, 0.17506032691456946, 0.20706866502006654, 0.23886941677033918, 0.2696389593992218, 0.29858037791512293, 0.3249441047807083, 0.3480473333183877, 0.36729170204460276, 0.3821787919179461, 0.3923230351305265, 0.3974617011116639, 0.39746170111166396, 0.3923230351305265, 0.3821787919179461, 0.3672917020446029, 0.34804733331838783, 0.3249441047807083, 0.2985803779151228, 0.26963895939922183, 0.23886941677033927, 0.20706866502006654, 0.17506032691456963, 0.14367340159757439, 0.11372079394799806, 0.08597826077058393, 0.06116431910214504, 0.03992163699773022, 0.022800388765576465, 0.010244005741518757, 0.0025776916503157127, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q4.xy.x180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q4.xy.x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0012888458251578564, 0.00512200287075939, 0.011400194382788243, 0.01996081849886511, 0.030582159551072508, 0.04298913038529193, 0.05686039697399898, 0.07183670079878712, 0.08753016345728473, 0.10353433251003327, 0.11943470838516959, 0.1348194796996109, 0.14929018895756146, 0.16247205239035414, 0.17402366665919386, 0.18364585102230138, 0.19108939595897306, 0.19616151756526326, 0.19873085055583195, 0.19873085055583198, 0.19616151756526326, 0.19108939595897306, 0.18364585102230144, 0.17402366665919392, 0.16247205239035414, 0.1492901889575614, 0.13481947969961092, 0.11943470838516963, 0.10353433251003327, 0.08753016345728482, 0.07183670079878719, 0.05686039697399903, 0.042989130385291965, 0.03058215955107252, 0.01996081849886511, 0.011400194382788232, 0.005122002870759378, 0.0012888458251578564, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q4.xy.x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q4.xy.-x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -0.0012888458251578564, -0.00512200287075939, -0.011400194382788243, -0.01996081849886511, -0.030582159551072508, -0.04298913038529193, -0.05686039697399898, -0.07183670079878712, -0.08753016345728473, -0.10353433251003327, -0.11943470838516959, -0.1348194796996109, -0.14929018895756146, -0.16247205239035414, -0.17402366665919386, -0.18364585102230138, -0.19108939595897306, -0.19616151756526326, -0.19873085055583195, -0.19873085055583198, -0.19616151756526326, -0.19108939595897306, -0.18364585102230144, -0.17402366665919392, -0.16247205239035414, -0.1492901889575614, -0.13481947969961092, -0.11943470838516963, -0.10353433251003327, -0.08753016345728482, -0.07183670079878719, -0.05686039697399903, -0.042989130385291965, -0.03058215955107252, -0.01996081849886511, -0.011400194382788232, -0.005122002870759378, -0.0012888458251578564, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q4.xy.-x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 1.578380914373998e-19, 6.27264442089904e-19, 1.3961211560539257e-18, 2.4444952482996434e-18, 3.745234380523461e-18, 5.2646500924475986e-18, 6.96339031524557e-18, 8.797458569454076e-18, 1.0719353450680837e-17, 1.2679298891027e-17, 1.462653333309955e-17, 1.6510624427684005e-17, 1.8282775205098117e-17, 1.9897087891074827e-17, 2.1311752635006774e-17, 2.2490130363115307e-17, 2.3401701711215753e-17, 2.4022857460218697e-17, 2.433751000250306e-17, 2.4337510002503062e-17, 2.4022857460218697e-17, 2.3401701711215753e-17, 2.2490130363115313e-17, 2.131175263500678e-17, 1.9897087891074827e-17, 1.828277520509811e-17, 1.651062442768401e-17, 1.4626533333099555e-17, 1.2679298891027e-17, 1.0719353450680847e-17, 8.797458569454085e-18, 6.963390315245576e-18, 5.264650092447603e-18, 3.7452343805234614e-18, 2.4444952482996434e-18, 1.3961211560539245e-18, 6.272644420899027e-19, 1.578380914373998e-19, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q4.xy.y180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 1.578380914373998e-19, 6.27264442089904e-19, 1.3961211560539257e-18, 2.4444952482996434e-18, 3.745234380523461e-18, 5.2646500924475986e-18, 6.96339031524557e-18, 8.797458569454076e-18, 1.0719353450680837e-17, 1.2679298891027e-17, 1.462653333309955e-17, 1.6510624427684005e-17, 1.8282775205098117e-17, 1.9897087891074827e-17, 2.1311752635006774e-17, 2.2490130363115307e-17, 2.3401701711215753e-17, 2.4022857460218697e-17, 2.433751000250306e-17, 2.4337510002503062e-17, 2.4022857460218697e-17, 2.3401701711215753e-17, 2.2490130363115313e-17, 2.131175263500678e-17, 1.9897087891074827e-17, 1.828277520509811e-17, 1.651062442768401e-17, 1.4626533333099555e-17, 1.2679298891027e-17, 1.0719353450680847e-17, 8.797458569454085e-18, 6.963390315245576e-18, 5.264650092447603e-18, 3.7452343805234614e-18, 2.4444952482996434e-18, 1.3961211560539245e-18, 6.272644420899027e-19, 1.578380914373998e-19, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q4.xy.y180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0025776916503157127, 0.01024400574151878, 0.022800388765576485, 0.03992163699773022, 0.061164319102145016, 0.08597826077058386, 0.11372079394799796, 0.14367340159757425, 0.17506032691456946, 0.20706866502006654, 0.23886941677033918, 0.2696389593992218, 0.29858037791512293, 0.3249441047807083, 0.3480473333183877, 0.36729170204460276, 0.3821787919179461, 0.3923230351305265, 0.3974617011116639, 0.39746170111166396, 0.3923230351305265, 0.3821787919179461, 0.3672917020446029, 0.34804733331838783, 0.3249441047807083, 0.2985803779151228, 0.26963895939922183, 0.23886941677033927, 0.20706866502006654, 0.17506032691456963, 0.14367340159757439, 0.11372079394799806, 0.08597826077058393, 0.06116431910214504, 0.03992163699773022, 0.022800388765576465, 0.010244005741518757, 0.0025776916503157127, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q4.xy.y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 7.89190457186999e-20, 3.13632221044952e-19, 6.980605780269628e-19, 1.2222476241498217e-18, 1.8726171902617303e-18, 2.6323250462237993e-18, 3.481695157622785e-18, 4.398729284727038e-18, 5.359676725340419e-18, 6.3396494455135e-18, 7.313266666549774e-18, 8.255312213842003e-18, 9.141387602549059e-18, 9.948543945537414e-18, 1.0655876317503387e-17, 1.1245065181557654e-17, 1.1700850855607877e-17, 1.2011428730109348e-17, 1.216875500125153e-17, 1.2168755001251531e-17, 1.2011428730109348e-17, 1.1700850855607877e-17, 1.1245065181557657e-17, 1.065587631750339e-17, 9.948543945537414e-18, 9.141387602549055e-18, 8.255312213842004e-18, 7.313266666549777e-18, 6.3396494455135e-18, 5.359676725340423e-18, 4.3987292847270425e-18, 3.481695157622788e-18, 2.6323250462238016e-18, 1.8726171902617307e-18, 1.2222476241498217e-18, 6.980605780269622e-19, 3.1363222104495134e-19, 7.89190457186999e-20, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q4.xy.y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0012888458251578564, 0.00512200287075939, 0.011400194382788243, 0.01996081849886511, 0.030582159551072508, 0.04298913038529193, 0.05686039697399898, 0.07183670079878712, 0.08753016345728473, 0.10353433251003327, 0.11943470838516959, 0.1348194796996109, 0.14929018895756146, 0.16247205239035414, 0.17402366665919386, 0.18364585102230138, 0.19108939595897306, 0.19616151756526326, 0.19873085055583195, 0.19873085055583198, 0.19616151756526326, 0.19108939595897306, 0.18364585102230144, 0.17402366665919392, 0.16247205239035414, 0.1492901889575614, 0.13481947969961092, 0.11943470838516963, 0.10353433251003327, 0.08753016345728482, 0.07183670079878719, 0.05686039697399903, 0.042989130385291965, 0.03058215955107252, 0.01996081849886511, 0.011400194382788232, 0.005122002870759378, 0.0012888458251578564, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q4.xy.-y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 7.89190457186999e-20, 3.13632221044952e-19, 6.980605780269628e-19, 1.2222476241498217e-18, 1.8726171902617303e-18, 2.6323250462237993e-18, 3.481695157622785e-18, 4.398729284727038e-18, 5.359676725340419e-18, 6.3396494455135e-18, 7.313266666549774e-18, 8.255312213842003e-18, 9.141387602549059e-18, 9.948543945537414e-18, 1.0655876317503387e-17, 1.1245065181557654e-17, 1.1700850855607877e-17, 1.2011428730109348e-17, 1.216875500125153e-17, 1.2168755001251531e-17, 1.2011428730109348e-17, 1.1700850855607877e-17, 1.1245065181557657e-17, 1.065587631750339e-17, 9.948543945537414e-18, 9.141387602549055e-18, 8.255312213842004e-18, 7.313266666549777e-18, 6.3396494455135e-18, 5.359676725340423e-18, 4.3987292847270425e-18, 3.481695157622788e-18, 2.6323250462238016e-18, 1.8726171902617307e-18, 1.2222476241498217e-18, 6.980605780269622e-19, 3.1363222104495134e-19, 7.89190457186999e-20, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q4.xy.-y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.0012888458251578564, -0.00512200287075939, -0.011400194382788243, -0.01996081849886511, -0.030582159551072508, -0.04298913038529193, -0.05686039697399898, -0.07183670079878712, -0.08753016345728473, -0.10353433251003327, -0.11943470838516959, -0.1348194796996109, -0.14929018895756146, -0.16247205239035414, -0.17402366665919386, -0.18364585102230138, -0.19108939595897306, -0.19616151756526326, -0.19873085055583195, -0.19873085055583198, -0.19616151756526326, -0.19108939595897306, -0.18364585102230144, -0.17402366665919392, -0.16247205239035414, -0.1492901889575614, -0.13481947969961092, -0.11943470838516963, -0.10353433251003327, -0.08753016345728482, -0.07183670079878719, -0.05686039697399903, -0.042989130385291965, -0.03058215955107252, -0.01996081849886511, -0.011400194382788232, -0.005122002870759378, -0.0012888458251578564, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q4.xy.const.wf.I": {
            "type": "constant",
            "sample": 0.5,
        },
        "q4.xy.const.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q4.resonator.readout.wf.I": {
            "type": "constant",
            "sample": 0.31622776601683794,
        },
        "q4.resonator.readout.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q4.resonator.const.wf.I": {
            "type": "constant",
            "sample": 0.5,
        },
        "q4.resonator.const.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q5.xy.saturation.wf.I": {
            "type": "constant",
            "sample": 0.03981071705534972,
        },
        "q5.xy.saturation.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q5.xy.x180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0025776916503157127, 0.01024400574151878, 0.022800388765576485, 0.03992163699773022, 0.061164319102145016, 0.08597826077058386, 0.11372079394799796, 0.14367340159757425, 0.17506032691456946, 0.20706866502006654, 0.23886941677033918, 0.2696389593992218, 0.29858037791512293, 0.3249441047807083, 0.3480473333183877, 0.36729170204460276, 0.3821787919179461, 0.3923230351305265, 0.3974617011116639, 0.39746170111166396, 0.3923230351305265, 0.3821787919179461, 0.3672917020446029, 0.34804733331838783, 0.3249441047807083, 0.2985803779151228, 0.26963895939922183, 0.23886941677033927, 0.20706866502006654, 0.17506032691456963, 0.14367340159757439, 0.11372079394799806, 0.08597826077058393, 0.06116431910214504, 0.03992163699773022, 0.022800388765576465, 0.010244005741518757, 0.0025776916503157127, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q5.xy.x180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q5.xy.x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0012888458251578564, 0.00512200287075939, 0.011400194382788243, 0.01996081849886511, 0.030582159551072508, 0.04298913038529193, 0.05686039697399898, 0.07183670079878712, 0.08753016345728473, 0.10353433251003327, 0.11943470838516959, 0.1348194796996109, 0.14929018895756146, 0.16247205239035414, 0.17402366665919386, 0.18364585102230138, 0.19108939595897306, 0.19616151756526326, 0.19873085055583195, 0.19873085055583198, 0.19616151756526326, 0.19108939595897306, 0.18364585102230144, 0.17402366665919392, 0.16247205239035414, 0.1492901889575614, 0.13481947969961092, 0.11943470838516963, 0.10353433251003327, 0.08753016345728482, 0.07183670079878719, 0.05686039697399903, 0.042989130385291965, 0.03058215955107252, 0.01996081849886511, 0.011400194382788232, 0.005122002870759378, 0.0012888458251578564, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q5.xy.x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q5.xy.-x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -0.0012888458251578564, -0.00512200287075939, -0.011400194382788243, -0.01996081849886511, -0.030582159551072508, -0.04298913038529193, -0.05686039697399898, -0.07183670079878712, -0.08753016345728473, -0.10353433251003327, -0.11943470838516959, -0.1348194796996109, -0.14929018895756146, -0.16247205239035414, -0.17402366665919386, -0.18364585102230138, -0.19108939595897306, -0.19616151756526326, -0.19873085055583195, -0.19873085055583198, -0.19616151756526326, -0.19108939595897306, -0.18364585102230144, -0.17402366665919392, -0.16247205239035414, -0.1492901889575614, -0.13481947969961092, -0.11943470838516963, -0.10353433251003327, -0.08753016345728482, -0.07183670079878719, -0.05686039697399903, -0.042989130385291965, -0.03058215955107252, -0.01996081849886511, -0.011400194382788232, -0.005122002870759378, -0.0012888458251578564, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q5.xy.-x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 1.578380914373998e-19, 6.27264442089904e-19, 1.3961211560539257e-18, 2.4444952482996434e-18, 3.745234380523461e-18, 5.2646500924475986e-18, 6.96339031524557e-18, 8.797458569454076e-18, 1.0719353450680837e-17, 1.2679298891027e-17, 1.462653333309955e-17, 1.6510624427684005e-17, 1.8282775205098117e-17, 1.9897087891074827e-17, 2.1311752635006774e-17, 2.2490130363115307e-17, 2.3401701711215753e-17, 2.4022857460218697e-17, 2.433751000250306e-17, 2.4337510002503062e-17, 2.4022857460218697e-17, 2.3401701711215753e-17, 2.2490130363115313e-17, 2.131175263500678e-17, 1.9897087891074827e-17, 1.828277520509811e-17, 1.651062442768401e-17, 1.4626533333099555e-17, 1.2679298891027e-17, 1.0719353450680847e-17, 8.797458569454085e-18, 6.963390315245576e-18, 5.264650092447603e-18, 3.7452343805234614e-18, 2.4444952482996434e-18, 1.3961211560539245e-18, 6.272644420899027e-19, 1.578380914373998e-19, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q5.xy.y180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 1.578380914373998e-19, 6.27264442089904e-19, 1.3961211560539257e-18, 2.4444952482996434e-18, 3.745234380523461e-18, 5.2646500924475986e-18, 6.96339031524557e-18, 8.797458569454076e-18, 1.0719353450680837e-17, 1.2679298891027e-17, 1.462653333309955e-17, 1.6510624427684005e-17, 1.8282775205098117e-17, 1.9897087891074827e-17, 2.1311752635006774e-17, 2.2490130363115307e-17, 2.3401701711215753e-17, 2.4022857460218697e-17, 2.433751000250306e-17, 2.4337510002503062e-17, 2.4022857460218697e-17, 2.3401701711215753e-17, 2.2490130363115313e-17, 2.131175263500678e-17, 1.9897087891074827e-17, 1.828277520509811e-17, 1.651062442768401e-17, 1.4626533333099555e-17, 1.2679298891027e-17, 1.0719353450680847e-17, 8.797458569454085e-18, 6.963390315245576e-18, 5.264650092447603e-18, 3.7452343805234614e-18, 2.4444952482996434e-18, 1.3961211560539245e-18, 6.272644420899027e-19, 1.578380914373998e-19, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q5.xy.y180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0025776916503157127, 0.01024400574151878, 0.022800388765576485, 0.03992163699773022, 0.061164319102145016, 0.08597826077058386, 0.11372079394799796, 0.14367340159757425, 0.17506032691456946, 0.20706866502006654, 0.23886941677033918, 0.2696389593992218, 0.29858037791512293, 0.3249441047807083, 0.3480473333183877, 0.36729170204460276, 0.3821787919179461, 0.3923230351305265, 0.3974617011116639, 0.39746170111166396, 0.3923230351305265, 0.3821787919179461, 0.3672917020446029, 0.34804733331838783, 0.3249441047807083, 0.2985803779151228, 0.26963895939922183, 0.23886941677033927, 0.20706866502006654, 0.17506032691456963, 0.14367340159757439, 0.11372079394799806, 0.08597826077058393, 0.06116431910214504, 0.03992163699773022, 0.022800388765576465, 0.010244005741518757, 0.0025776916503157127, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q5.xy.y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 7.89190457186999e-20, 3.13632221044952e-19, 6.980605780269628e-19, 1.2222476241498217e-18, 1.8726171902617303e-18, 2.6323250462237993e-18, 3.481695157622785e-18, 4.398729284727038e-18, 5.359676725340419e-18, 6.3396494455135e-18, 7.313266666549774e-18, 8.255312213842003e-18, 9.141387602549059e-18, 9.948543945537414e-18, 1.0655876317503387e-17, 1.1245065181557654e-17, 1.1700850855607877e-17, 1.2011428730109348e-17, 1.216875500125153e-17, 1.2168755001251531e-17, 1.2011428730109348e-17, 1.1700850855607877e-17, 1.1245065181557657e-17, 1.065587631750339e-17, 9.948543945537414e-18, 9.141387602549055e-18, 8.255312213842004e-18, 7.313266666549777e-18, 6.3396494455135e-18, 5.359676725340423e-18, 4.3987292847270425e-18, 3.481695157622788e-18, 2.6323250462238016e-18, 1.8726171902617307e-18, 1.2222476241498217e-18, 6.980605780269622e-19, 3.1363222104495134e-19, 7.89190457186999e-20, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q5.xy.y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0012888458251578564, 0.00512200287075939, 0.011400194382788243, 0.01996081849886511, 0.030582159551072508, 0.04298913038529193, 0.05686039697399898, 0.07183670079878712, 0.08753016345728473, 0.10353433251003327, 0.11943470838516959, 0.1348194796996109, 0.14929018895756146, 0.16247205239035414, 0.17402366665919386, 0.18364585102230138, 0.19108939595897306, 0.19616151756526326, 0.19873085055583195, 0.19873085055583198, 0.19616151756526326, 0.19108939595897306, 0.18364585102230144, 0.17402366665919392, 0.16247205239035414, 0.1492901889575614, 0.13481947969961092, 0.11943470838516963, 0.10353433251003327, 0.08753016345728482, 0.07183670079878719, 0.05686039697399903, 0.042989130385291965, 0.03058215955107252, 0.01996081849886511, 0.011400194382788232, 0.005122002870759378, 0.0012888458251578564, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q5.xy.-y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 7.89190457186999e-20, 3.13632221044952e-19, 6.980605780269628e-19, 1.2222476241498217e-18, 1.8726171902617303e-18, 2.6323250462237993e-18, 3.481695157622785e-18, 4.398729284727038e-18, 5.359676725340419e-18, 6.3396494455135e-18, 7.313266666549774e-18, 8.255312213842003e-18, 9.141387602549059e-18, 9.948543945537414e-18, 1.0655876317503387e-17, 1.1245065181557654e-17, 1.1700850855607877e-17, 1.2011428730109348e-17, 1.216875500125153e-17, 1.2168755001251531e-17, 1.2011428730109348e-17, 1.1700850855607877e-17, 1.1245065181557657e-17, 1.065587631750339e-17, 9.948543945537414e-18, 9.141387602549055e-18, 8.255312213842004e-18, 7.313266666549777e-18, 6.3396494455135e-18, 5.359676725340423e-18, 4.3987292847270425e-18, 3.481695157622788e-18, 2.6323250462238016e-18, 1.8726171902617307e-18, 1.2222476241498217e-18, 6.980605780269622e-19, 3.1363222104495134e-19, 7.89190457186999e-20, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q5.xy.-y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.0012888458251578564, -0.00512200287075939, -0.011400194382788243, -0.01996081849886511, -0.030582159551072508, -0.04298913038529193, -0.05686039697399898, -0.07183670079878712, -0.08753016345728473, -0.10353433251003327, -0.11943470838516959, -0.1348194796996109, -0.14929018895756146, -0.16247205239035414, -0.17402366665919386, -0.18364585102230138, -0.19108939595897306, -0.19616151756526326, -0.19873085055583195, -0.19873085055583198, -0.19616151756526326, -0.19108939595897306, -0.18364585102230144, -0.17402366665919392, -0.16247205239035414, -0.1492901889575614, -0.13481947969961092, -0.11943470838516963, -0.10353433251003327, -0.08753016345728482, -0.07183670079878719, -0.05686039697399903, -0.042989130385291965, -0.03058215955107252, -0.01996081849886511, -0.011400194382788232, -0.005122002870759378, -0.0012888458251578564, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q5.xy.const.wf.I": {
            "type": "constant",
            "sample": 0.5,
        },
        "q5.xy.const.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q5.resonator.readout.wf.I": {
            "type": "constant",
            "sample": 0.31622776601683794,
        },
        "q5.resonator.readout.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q5.resonator.const.wf.I": {
            "type": "constant",
            "sample": 0.5,
        },
        "q5.resonator.const.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q6.xy.saturation.wf.I": {
            "type": "constant",
            "sample": 0.03981071705534972,
        },
        "q6.xy.saturation.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q6.xy.x180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0025776916503157127, 0.01024400574151878, 0.022800388765576485, 0.03992163699773022, 0.061164319102145016, 0.08597826077058386, 0.11372079394799796, 0.14367340159757425, 0.17506032691456946, 0.20706866502006654, 0.23886941677033918, 0.2696389593992218, 0.29858037791512293, 0.3249441047807083, 0.3480473333183877, 0.36729170204460276, 0.3821787919179461, 0.3923230351305265, 0.3974617011116639, 0.39746170111166396, 0.3923230351305265, 0.3821787919179461, 0.3672917020446029, 0.34804733331838783, 0.3249441047807083, 0.2985803779151228, 0.26963895939922183, 0.23886941677033927, 0.20706866502006654, 0.17506032691456963, 0.14367340159757439, 0.11372079394799806, 0.08597826077058393, 0.06116431910214504, 0.03992163699773022, 0.022800388765576465, 0.010244005741518757, 0.0025776916503157127, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q6.xy.x180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q6.xy.x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0012888458251578564, 0.00512200287075939, 0.011400194382788243, 0.01996081849886511, 0.030582159551072508, 0.04298913038529193, 0.05686039697399898, 0.07183670079878712, 0.08753016345728473, 0.10353433251003327, 0.11943470838516959, 0.1348194796996109, 0.14929018895756146, 0.16247205239035414, 0.17402366665919386, 0.18364585102230138, 0.19108939595897306, 0.19616151756526326, 0.19873085055583195, 0.19873085055583198, 0.19616151756526326, 0.19108939595897306, 0.18364585102230144, 0.17402366665919392, 0.16247205239035414, 0.1492901889575614, 0.13481947969961092, 0.11943470838516963, 0.10353433251003327, 0.08753016345728482, 0.07183670079878719, 0.05686039697399903, 0.042989130385291965, 0.03058215955107252, 0.01996081849886511, 0.011400194382788232, 0.005122002870759378, 0.0012888458251578564, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q6.xy.x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q6.xy.-x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -0.0012888458251578564, -0.00512200287075939, -0.011400194382788243, -0.01996081849886511, -0.030582159551072508, -0.04298913038529193, -0.05686039697399898, -0.07183670079878712, -0.08753016345728473, -0.10353433251003327, -0.11943470838516959, -0.1348194796996109, -0.14929018895756146, -0.16247205239035414, -0.17402366665919386, -0.18364585102230138, -0.19108939595897306, -0.19616151756526326, -0.19873085055583195, -0.19873085055583198, -0.19616151756526326, -0.19108939595897306, -0.18364585102230144, -0.17402366665919392, -0.16247205239035414, -0.1492901889575614, -0.13481947969961092, -0.11943470838516963, -0.10353433251003327, -0.08753016345728482, -0.07183670079878719, -0.05686039697399903, -0.042989130385291965, -0.03058215955107252, -0.01996081849886511, -0.011400194382788232, -0.005122002870759378, -0.0012888458251578564, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q6.xy.-x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 1.578380914373998e-19, 6.27264442089904e-19, 1.3961211560539257e-18, 2.4444952482996434e-18, 3.745234380523461e-18, 5.2646500924475986e-18, 6.96339031524557e-18, 8.797458569454076e-18, 1.0719353450680837e-17, 1.2679298891027e-17, 1.462653333309955e-17, 1.6510624427684005e-17, 1.8282775205098117e-17, 1.9897087891074827e-17, 2.1311752635006774e-17, 2.2490130363115307e-17, 2.3401701711215753e-17, 2.4022857460218697e-17, 2.433751000250306e-17, 2.4337510002503062e-17, 2.4022857460218697e-17, 2.3401701711215753e-17, 2.2490130363115313e-17, 2.131175263500678e-17, 1.9897087891074827e-17, 1.828277520509811e-17, 1.651062442768401e-17, 1.4626533333099555e-17, 1.2679298891027e-17, 1.0719353450680847e-17, 8.797458569454085e-18, 6.963390315245576e-18, 5.264650092447603e-18, 3.7452343805234614e-18, 2.4444952482996434e-18, 1.3961211560539245e-18, 6.272644420899027e-19, 1.578380914373998e-19, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q6.xy.y180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 1.578380914373998e-19, 6.27264442089904e-19, 1.3961211560539257e-18, 2.4444952482996434e-18, 3.745234380523461e-18, 5.2646500924475986e-18, 6.96339031524557e-18, 8.797458569454076e-18, 1.0719353450680837e-17, 1.2679298891027e-17, 1.462653333309955e-17, 1.6510624427684005e-17, 1.8282775205098117e-17, 1.9897087891074827e-17, 2.1311752635006774e-17, 2.2490130363115307e-17, 2.3401701711215753e-17, 2.4022857460218697e-17, 2.433751000250306e-17, 2.4337510002503062e-17, 2.4022857460218697e-17, 2.3401701711215753e-17, 2.2490130363115313e-17, 2.131175263500678e-17, 1.9897087891074827e-17, 1.828277520509811e-17, 1.651062442768401e-17, 1.4626533333099555e-17, 1.2679298891027e-17, 1.0719353450680847e-17, 8.797458569454085e-18, 6.963390315245576e-18, 5.264650092447603e-18, 3.7452343805234614e-18, 2.4444952482996434e-18, 1.3961211560539245e-18, 6.272644420899027e-19, 1.578380914373998e-19, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q6.xy.y180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0025776916503157127, 0.01024400574151878, 0.022800388765576485, 0.03992163699773022, 0.061164319102145016, 0.08597826077058386, 0.11372079394799796, 0.14367340159757425, 0.17506032691456946, 0.20706866502006654, 0.23886941677033918, 0.2696389593992218, 0.29858037791512293, 0.3249441047807083, 0.3480473333183877, 0.36729170204460276, 0.3821787919179461, 0.3923230351305265, 0.3974617011116639, 0.39746170111166396, 0.3923230351305265, 0.3821787919179461, 0.3672917020446029, 0.34804733331838783, 0.3249441047807083, 0.2985803779151228, 0.26963895939922183, 0.23886941677033927, 0.20706866502006654, 0.17506032691456963, 0.14367340159757439, 0.11372079394799806, 0.08597826077058393, 0.06116431910214504, 0.03992163699773022, 0.022800388765576465, 0.010244005741518757, 0.0025776916503157127, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q6.xy.y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 7.89190457186999e-20, 3.13632221044952e-19, 6.980605780269628e-19, 1.2222476241498217e-18, 1.8726171902617303e-18, 2.6323250462237993e-18, 3.481695157622785e-18, 4.398729284727038e-18, 5.359676725340419e-18, 6.3396494455135e-18, 7.313266666549774e-18, 8.255312213842003e-18, 9.141387602549059e-18, 9.948543945537414e-18, 1.0655876317503387e-17, 1.1245065181557654e-17, 1.1700850855607877e-17, 1.2011428730109348e-17, 1.216875500125153e-17, 1.2168755001251531e-17, 1.2011428730109348e-17, 1.1700850855607877e-17, 1.1245065181557657e-17, 1.065587631750339e-17, 9.948543945537414e-18, 9.141387602549055e-18, 8.255312213842004e-18, 7.313266666549777e-18, 6.3396494455135e-18, 5.359676725340423e-18, 4.3987292847270425e-18, 3.481695157622788e-18, 2.6323250462238016e-18, 1.8726171902617307e-18, 1.2222476241498217e-18, 6.980605780269622e-19, 3.1363222104495134e-19, 7.89190457186999e-20, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q6.xy.y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0012888458251578564, 0.00512200287075939, 0.011400194382788243, 0.01996081849886511, 0.030582159551072508, 0.04298913038529193, 0.05686039697399898, 0.07183670079878712, 0.08753016345728473, 0.10353433251003327, 0.11943470838516959, 0.1348194796996109, 0.14929018895756146, 0.16247205239035414, 0.17402366665919386, 0.18364585102230138, 0.19108939595897306, 0.19616151756526326, 0.19873085055583195, 0.19873085055583198, 0.19616151756526326, 0.19108939595897306, 0.18364585102230144, 0.17402366665919392, 0.16247205239035414, 0.1492901889575614, 0.13481947969961092, 0.11943470838516963, 0.10353433251003327, 0.08753016345728482, 0.07183670079878719, 0.05686039697399903, 0.042989130385291965, 0.03058215955107252, 0.01996081849886511, 0.011400194382788232, 0.005122002870759378, 0.0012888458251578564, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q6.xy.-y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 7.89190457186999e-20, 3.13632221044952e-19, 6.980605780269628e-19, 1.2222476241498217e-18, 1.8726171902617303e-18, 2.6323250462237993e-18, 3.481695157622785e-18, 4.398729284727038e-18, 5.359676725340419e-18, 6.3396494455135e-18, 7.313266666549774e-18, 8.255312213842003e-18, 9.141387602549059e-18, 9.948543945537414e-18, 1.0655876317503387e-17, 1.1245065181557654e-17, 1.1700850855607877e-17, 1.2011428730109348e-17, 1.216875500125153e-17, 1.2168755001251531e-17, 1.2011428730109348e-17, 1.1700850855607877e-17, 1.1245065181557657e-17, 1.065587631750339e-17, 9.948543945537414e-18, 9.141387602549055e-18, 8.255312213842004e-18, 7.313266666549777e-18, 6.3396494455135e-18, 5.359676725340423e-18, 4.3987292847270425e-18, 3.481695157622788e-18, 2.6323250462238016e-18, 1.8726171902617307e-18, 1.2222476241498217e-18, 6.980605780269622e-19, 3.1363222104495134e-19, 7.89190457186999e-20, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q6.xy.-y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.0012888458251578564, -0.00512200287075939, -0.011400194382788243, -0.01996081849886511, -0.030582159551072508, -0.04298913038529193, -0.05686039697399898, -0.07183670079878712, -0.08753016345728473, -0.10353433251003327, -0.11943470838516959, -0.1348194796996109, -0.14929018895756146, -0.16247205239035414, -0.17402366665919386, -0.18364585102230138, -0.19108939595897306, -0.19616151756526326, -0.19873085055583195, -0.19873085055583198, -0.19616151756526326, -0.19108939595897306, -0.18364585102230144, -0.17402366665919392, -0.16247205239035414, -0.1492901889575614, -0.13481947969961092, -0.11943470838516963, -0.10353433251003327, -0.08753016345728482, -0.07183670079878719, -0.05686039697399903, -0.042989130385291965, -0.03058215955107252, -0.01996081849886511, -0.011400194382788232, -0.005122002870759378, -0.0012888458251578564, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q6.xy.const.wf.I": {
            "type": "constant",
            "sample": 0.5,
        },
        "q6.xy.const.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q6.resonator.readout.wf.I": {
            "type": "constant",
            "sample": 0.31622776601683794,
        },
        "q6.resonator.readout.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q6.resonator.const.wf.I": {
            "type": "constant",
            "sample": 0.5,
        },
        "q6.resonator.const.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q7.xy.saturation.wf.I": {
            "type": "constant",
            "sample": 0.03981071705534972,
        },
        "q7.xy.saturation.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q7.xy.x180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0025776916503157127, 0.01024400574151878, 0.022800388765576485, 0.03992163699773022, 0.061164319102145016, 0.08597826077058386, 0.11372079394799796, 0.14367340159757425, 0.17506032691456946, 0.20706866502006654, 0.23886941677033918, 0.2696389593992218, 0.29858037791512293, 0.3249441047807083, 0.3480473333183877, 0.36729170204460276, 0.3821787919179461, 0.3923230351305265, 0.3974617011116639, 0.39746170111166396, 0.3923230351305265, 0.3821787919179461, 0.3672917020446029, 0.34804733331838783, 0.3249441047807083, 0.2985803779151228, 0.26963895939922183, 0.23886941677033927, 0.20706866502006654, 0.17506032691456963, 0.14367340159757439, 0.11372079394799806, 0.08597826077058393, 0.06116431910214504, 0.03992163699773022, 0.022800388765576465, 0.010244005741518757, 0.0025776916503157127, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q7.xy.x180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q7.xy.x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0012888458251578564, 0.00512200287075939, 0.011400194382788243, 0.01996081849886511, 0.030582159551072508, 0.04298913038529193, 0.05686039697399898, 0.07183670079878712, 0.08753016345728473, 0.10353433251003327, 0.11943470838516959, 0.1348194796996109, 0.14929018895756146, 0.16247205239035414, 0.17402366665919386, 0.18364585102230138, 0.19108939595897306, 0.19616151756526326, 0.19873085055583195, 0.19873085055583198, 0.19616151756526326, 0.19108939595897306, 0.18364585102230144, 0.17402366665919392, 0.16247205239035414, 0.1492901889575614, 0.13481947969961092, 0.11943470838516963, 0.10353433251003327, 0.08753016345728482, 0.07183670079878719, 0.05686039697399903, 0.042989130385291965, 0.03058215955107252, 0.01996081849886511, 0.011400194382788232, 0.005122002870759378, 0.0012888458251578564, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q7.xy.x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q7.xy.-x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -0.0012888458251578564, -0.00512200287075939, -0.011400194382788243, -0.01996081849886511, -0.030582159551072508, -0.04298913038529193, -0.05686039697399898, -0.07183670079878712, -0.08753016345728473, -0.10353433251003327, -0.11943470838516959, -0.1348194796996109, -0.14929018895756146, -0.16247205239035414, -0.17402366665919386, -0.18364585102230138, -0.19108939595897306, -0.19616151756526326, -0.19873085055583195, -0.19873085055583198, -0.19616151756526326, -0.19108939595897306, -0.18364585102230144, -0.17402366665919392, -0.16247205239035414, -0.1492901889575614, -0.13481947969961092, -0.11943470838516963, -0.10353433251003327, -0.08753016345728482, -0.07183670079878719, -0.05686039697399903, -0.042989130385291965, -0.03058215955107252, -0.01996081849886511, -0.011400194382788232, -0.005122002870759378, -0.0012888458251578564, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q7.xy.-x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 1.578380914373998e-19, 6.27264442089904e-19, 1.3961211560539257e-18, 2.4444952482996434e-18, 3.745234380523461e-18, 5.2646500924475986e-18, 6.96339031524557e-18, 8.797458569454076e-18, 1.0719353450680837e-17, 1.2679298891027e-17, 1.462653333309955e-17, 1.6510624427684005e-17, 1.8282775205098117e-17, 1.9897087891074827e-17, 2.1311752635006774e-17, 2.2490130363115307e-17, 2.3401701711215753e-17, 2.4022857460218697e-17, 2.433751000250306e-17, 2.4337510002503062e-17, 2.4022857460218697e-17, 2.3401701711215753e-17, 2.2490130363115313e-17, 2.131175263500678e-17, 1.9897087891074827e-17, 1.828277520509811e-17, 1.651062442768401e-17, 1.4626533333099555e-17, 1.2679298891027e-17, 1.0719353450680847e-17, 8.797458569454085e-18, 6.963390315245576e-18, 5.264650092447603e-18, 3.7452343805234614e-18, 2.4444952482996434e-18, 1.3961211560539245e-18, 6.272644420899027e-19, 1.578380914373998e-19, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q7.xy.y180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 1.578380914373998e-19, 6.27264442089904e-19, 1.3961211560539257e-18, 2.4444952482996434e-18, 3.745234380523461e-18, 5.2646500924475986e-18, 6.96339031524557e-18, 8.797458569454076e-18, 1.0719353450680837e-17, 1.2679298891027e-17, 1.462653333309955e-17, 1.6510624427684005e-17, 1.8282775205098117e-17, 1.9897087891074827e-17, 2.1311752635006774e-17, 2.2490130363115307e-17, 2.3401701711215753e-17, 2.4022857460218697e-17, 2.433751000250306e-17, 2.4337510002503062e-17, 2.4022857460218697e-17, 2.3401701711215753e-17, 2.2490130363115313e-17, 2.131175263500678e-17, 1.9897087891074827e-17, 1.828277520509811e-17, 1.651062442768401e-17, 1.4626533333099555e-17, 1.2679298891027e-17, 1.0719353450680847e-17, 8.797458569454085e-18, 6.963390315245576e-18, 5.264650092447603e-18, 3.7452343805234614e-18, 2.4444952482996434e-18, 1.3961211560539245e-18, 6.272644420899027e-19, 1.578380914373998e-19, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q7.xy.y180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0025776916503157127, 0.01024400574151878, 0.022800388765576485, 0.03992163699773022, 0.061164319102145016, 0.08597826077058386, 0.11372079394799796, 0.14367340159757425, 0.17506032691456946, 0.20706866502006654, 0.23886941677033918, 0.2696389593992218, 0.29858037791512293, 0.3249441047807083, 0.3480473333183877, 0.36729170204460276, 0.3821787919179461, 0.3923230351305265, 0.3974617011116639, 0.39746170111166396, 0.3923230351305265, 0.3821787919179461, 0.3672917020446029, 0.34804733331838783, 0.3249441047807083, 0.2985803779151228, 0.26963895939922183, 0.23886941677033927, 0.20706866502006654, 0.17506032691456963, 0.14367340159757439, 0.11372079394799806, 0.08597826077058393, 0.06116431910214504, 0.03992163699773022, 0.022800388765576465, 0.010244005741518757, 0.0025776916503157127, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q7.xy.y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 7.89190457186999e-20, 3.13632221044952e-19, 6.980605780269628e-19, 1.2222476241498217e-18, 1.8726171902617303e-18, 2.6323250462237993e-18, 3.481695157622785e-18, 4.398729284727038e-18, 5.359676725340419e-18, 6.3396494455135e-18, 7.313266666549774e-18, 8.255312213842003e-18, 9.141387602549059e-18, 9.948543945537414e-18, 1.0655876317503387e-17, 1.1245065181557654e-17, 1.1700850855607877e-17, 1.2011428730109348e-17, 1.216875500125153e-17, 1.2168755001251531e-17, 1.2011428730109348e-17, 1.1700850855607877e-17, 1.1245065181557657e-17, 1.065587631750339e-17, 9.948543945537414e-18, 9.141387602549055e-18, 8.255312213842004e-18, 7.313266666549777e-18, 6.3396494455135e-18, 5.359676725340423e-18, 4.3987292847270425e-18, 3.481695157622788e-18, 2.6323250462238016e-18, 1.8726171902617307e-18, 1.2222476241498217e-18, 6.980605780269622e-19, 3.1363222104495134e-19, 7.89190457186999e-20, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q7.xy.y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0012888458251578564, 0.00512200287075939, 0.011400194382788243, 0.01996081849886511, 0.030582159551072508, 0.04298913038529193, 0.05686039697399898, 0.07183670079878712, 0.08753016345728473, 0.10353433251003327, 0.11943470838516959, 0.1348194796996109, 0.14929018895756146, 0.16247205239035414, 0.17402366665919386, 0.18364585102230138, 0.19108939595897306, 0.19616151756526326, 0.19873085055583195, 0.19873085055583198, 0.19616151756526326, 0.19108939595897306, 0.18364585102230144, 0.17402366665919392, 0.16247205239035414, 0.1492901889575614, 0.13481947969961092, 0.11943470838516963, 0.10353433251003327, 0.08753016345728482, 0.07183670079878719, 0.05686039697399903, 0.042989130385291965, 0.03058215955107252, 0.01996081849886511, 0.011400194382788232, 0.005122002870759378, 0.0012888458251578564, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q7.xy.-y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 7.89190457186999e-20, 3.13632221044952e-19, 6.980605780269628e-19, 1.2222476241498217e-18, 1.8726171902617303e-18, 2.6323250462237993e-18, 3.481695157622785e-18, 4.398729284727038e-18, 5.359676725340419e-18, 6.3396494455135e-18, 7.313266666549774e-18, 8.255312213842003e-18, 9.141387602549059e-18, 9.948543945537414e-18, 1.0655876317503387e-17, 1.1245065181557654e-17, 1.1700850855607877e-17, 1.2011428730109348e-17, 1.216875500125153e-17, 1.2168755001251531e-17, 1.2011428730109348e-17, 1.1700850855607877e-17, 1.1245065181557657e-17, 1.065587631750339e-17, 9.948543945537414e-18, 9.141387602549055e-18, 8.255312213842004e-18, 7.313266666549777e-18, 6.3396494455135e-18, 5.359676725340423e-18, 4.3987292847270425e-18, 3.481695157622788e-18, 2.6323250462238016e-18, 1.8726171902617307e-18, 1.2222476241498217e-18, 6.980605780269622e-19, 3.1363222104495134e-19, 7.89190457186999e-20, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q7.xy.-y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.0012888458251578564, -0.00512200287075939, -0.011400194382788243, -0.01996081849886511, -0.030582159551072508, -0.04298913038529193, -0.05686039697399898, -0.07183670079878712, -0.08753016345728473, -0.10353433251003327, -0.11943470838516959, -0.1348194796996109, -0.14929018895756146, -0.16247205239035414, -0.17402366665919386, -0.18364585102230138, -0.19108939595897306, -0.19616151756526326, -0.19873085055583195, -0.19873085055583198, -0.19616151756526326, -0.19108939595897306, -0.18364585102230144, -0.17402366665919392, -0.16247205239035414, -0.1492901889575614, -0.13481947969961092, -0.11943470838516963, -0.10353433251003327, -0.08753016345728482, -0.07183670079878719, -0.05686039697399903, -0.042989130385291965, -0.03058215955107252, -0.01996081849886511, -0.011400194382788232, -0.005122002870759378, -0.0012888458251578564, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q7.xy.const.wf.I": {
            "type": "constant",
            "sample": 0.5,
        },
        "q7.xy.const.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q7.resonator.readout.wf.I": {
            "type": "constant",
            "sample": 0.31622776601683794,
        },
        "q7.resonator.readout.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q7.resonator.const.wf.I": {
            "type": "constant",
            "sample": 0.5,
        },
        "q7.resonator.const.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q8.xy.saturation.wf.I": {
            "type": "constant",
            "sample": 0.03981071705534972,
        },
        "q8.xy.saturation.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q8.xy.x180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0025776916503157127, 0.01024400574151878, 0.022800388765576485, 0.03992163699773022, 0.061164319102145016, 0.08597826077058386, 0.11372079394799796, 0.14367340159757425, 0.17506032691456946, 0.20706866502006654, 0.23886941677033918, 0.2696389593992218, 0.29858037791512293, 0.3249441047807083, 0.3480473333183877, 0.36729170204460276, 0.3821787919179461, 0.3923230351305265, 0.3974617011116639, 0.39746170111166396, 0.3923230351305265, 0.3821787919179461, 0.3672917020446029, 0.34804733331838783, 0.3249441047807083, 0.2985803779151228, 0.26963895939922183, 0.23886941677033927, 0.20706866502006654, 0.17506032691456963, 0.14367340159757439, 0.11372079394799806, 0.08597826077058393, 0.06116431910214504, 0.03992163699773022, 0.022800388765576465, 0.010244005741518757, 0.0025776916503157127, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q8.xy.x180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q8.xy.x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0012888458251578564, 0.00512200287075939, 0.011400194382788243, 0.01996081849886511, 0.030582159551072508, 0.04298913038529193, 0.05686039697399898, 0.07183670079878712, 0.08753016345728473, 0.10353433251003327, 0.11943470838516959, 0.1348194796996109, 0.14929018895756146, 0.16247205239035414, 0.17402366665919386, 0.18364585102230138, 0.19108939595897306, 0.19616151756526326, 0.19873085055583195, 0.19873085055583198, 0.19616151756526326, 0.19108939595897306, 0.18364585102230144, 0.17402366665919392, 0.16247205239035414, 0.1492901889575614, 0.13481947969961092, 0.11943470838516963, 0.10353433251003327, 0.08753016345728482, 0.07183670079878719, 0.05686039697399903, 0.042989130385291965, 0.03058215955107252, 0.01996081849886511, 0.011400194382788232, 0.005122002870759378, 0.0012888458251578564, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q8.xy.x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q8.xy.-x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -0.0012888458251578564, -0.00512200287075939, -0.011400194382788243, -0.01996081849886511, -0.030582159551072508, -0.04298913038529193, -0.05686039697399898, -0.07183670079878712, -0.08753016345728473, -0.10353433251003327, -0.11943470838516959, -0.1348194796996109, -0.14929018895756146, -0.16247205239035414, -0.17402366665919386, -0.18364585102230138, -0.19108939595897306, -0.19616151756526326, -0.19873085055583195, -0.19873085055583198, -0.19616151756526326, -0.19108939595897306, -0.18364585102230144, -0.17402366665919392, -0.16247205239035414, -0.1492901889575614, -0.13481947969961092, -0.11943470838516963, -0.10353433251003327, -0.08753016345728482, -0.07183670079878719, -0.05686039697399903, -0.042989130385291965, -0.03058215955107252, -0.01996081849886511, -0.011400194382788232, -0.005122002870759378, -0.0012888458251578564, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q8.xy.-x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 1.578380914373998e-19, 6.27264442089904e-19, 1.3961211560539257e-18, 2.4444952482996434e-18, 3.745234380523461e-18, 5.2646500924475986e-18, 6.96339031524557e-18, 8.797458569454076e-18, 1.0719353450680837e-17, 1.2679298891027e-17, 1.462653333309955e-17, 1.6510624427684005e-17, 1.8282775205098117e-17, 1.9897087891074827e-17, 2.1311752635006774e-17, 2.2490130363115307e-17, 2.3401701711215753e-17, 2.4022857460218697e-17, 2.433751000250306e-17, 2.4337510002503062e-17, 2.4022857460218697e-17, 2.3401701711215753e-17, 2.2490130363115313e-17, 2.131175263500678e-17, 1.9897087891074827e-17, 1.828277520509811e-17, 1.651062442768401e-17, 1.4626533333099555e-17, 1.2679298891027e-17, 1.0719353450680847e-17, 8.797458569454085e-18, 6.963390315245576e-18, 5.264650092447603e-18, 3.7452343805234614e-18, 2.4444952482996434e-18, 1.3961211560539245e-18, 6.272644420899027e-19, 1.578380914373998e-19, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q8.xy.y180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 1.578380914373998e-19, 6.27264442089904e-19, 1.3961211560539257e-18, 2.4444952482996434e-18, 3.745234380523461e-18, 5.2646500924475986e-18, 6.96339031524557e-18, 8.797458569454076e-18, 1.0719353450680837e-17, 1.2679298891027e-17, 1.462653333309955e-17, 1.6510624427684005e-17, 1.8282775205098117e-17, 1.9897087891074827e-17, 2.1311752635006774e-17, 2.2490130363115307e-17, 2.3401701711215753e-17, 2.4022857460218697e-17, 2.433751000250306e-17, 2.4337510002503062e-17, 2.4022857460218697e-17, 2.3401701711215753e-17, 2.2490130363115313e-17, 2.131175263500678e-17, 1.9897087891074827e-17, 1.828277520509811e-17, 1.651062442768401e-17, 1.4626533333099555e-17, 1.2679298891027e-17, 1.0719353450680847e-17, 8.797458569454085e-18, 6.963390315245576e-18, 5.264650092447603e-18, 3.7452343805234614e-18, 2.4444952482996434e-18, 1.3961211560539245e-18, 6.272644420899027e-19, 1.578380914373998e-19, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q8.xy.y180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0025776916503157127, 0.01024400574151878, 0.022800388765576485, 0.03992163699773022, 0.061164319102145016, 0.08597826077058386, 0.11372079394799796, 0.14367340159757425, 0.17506032691456946, 0.20706866502006654, 0.23886941677033918, 0.2696389593992218, 0.29858037791512293, 0.3249441047807083, 0.3480473333183877, 0.36729170204460276, 0.3821787919179461, 0.3923230351305265, 0.3974617011116639, 0.39746170111166396, 0.3923230351305265, 0.3821787919179461, 0.3672917020446029, 0.34804733331838783, 0.3249441047807083, 0.2985803779151228, 0.26963895939922183, 0.23886941677033927, 0.20706866502006654, 0.17506032691456963, 0.14367340159757439, 0.11372079394799806, 0.08597826077058393, 0.06116431910214504, 0.03992163699773022, 0.022800388765576465, 0.010244005741518757, 0.0025776916503157127, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q8.xy.y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 7.89190457186999e-20, 3.13632221044952e-19, 6.980605780269628e-19, 1.2222476241498217e-18, 1.8726171902617303e-18, 2.6323250462237993e-18, 3.481695157622785e-18, 4.398729284727038e-18, 5.359676725340419e-18, 6.3396494455135e-18, 7.313266666549774e-18, 8.255312213842003e-18, 9.141387602549059e-18, 9.948543945537414e-18, 1.0655876317503387e-17, 1.1245065181557654e-17, 1.1700850855607877e-17, 1.2011428730109348e-17, 1.216875500125153e-17, 1.2168755001251531e-17, 1.2011428730109348e-17, 1.1700850855607877e-17, 1.1245065181557657e-17, 1.065587631750339e-17, 9.948543945537414e-18, 9.141387602549055e-18, 8.255312213842004e-18, 7.313266666549777e-18, 6.3396494455135e-18, 5.359676725340423e-18, 4.3987292847270425e-18, 3.481695157622788e-18, 2.6323250462238016e-18, 1.8726171902617307e-18, 1.2222476241498217e-18, 6.980605780269622e-19, 3.1363222104495134e-19, 7.89190457186999e-20, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q8.xy.y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0012888458251578564, 0.00512200287075939, 0.011400194382788243, 0.01996081849886511, 0.030582159551072508, 0.04298913038529193, 0.05686039697399898, 0.07183670079878712, 0.08753016345728473, 0.10353433251003327, 0.11943470838516959, 0.1348194796996109, 0.14929018895756146, 0.16247205239035414, 0.17402366665919386, 0.18364585102230138, 0.19108939595897306, 0.19616151756526326, 0.19873085055583195, 0.19873085055583198, 0.19616151756526326, 0.19108939595897306, 0.18364585102230144, 0.17402366665919392, 0.16247205239035414, 0.1492901889575614, 0.13481947969961092, 0.11943470838516963, 0.10353433251003327, 0.08753016345728482, 0.07183670079878719, 0.05686039697399903, 0.042989130385291965, 0.03058215955107252, 0.01996081849886511, 0.011400194382788232, 0.005122002870759378, 0.0012888458251578564, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q8.xy.-y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 7.89190457186999e-20, 3.13632221044952e-19, 6.980605780269628e-19, 1.2222476241498217e-18, 1.8726171902617303e-18, 2.6323250462237993e-18, 3.481695157622785e-18, 4.398729284727038e-18, 5.359676725340419e-18, 6.3396494455135e-18, 7.313266666549774e-18, 8.255312213842003e-18, 9.141387602549059e-18, 9.948543945537414e-18, 1.0655876317503387e-17, 1.1245065181557654e-17, 1.1700850855607877e-17, 1.2011428730109348e-17, 1.216875500125153e-17, 1.2168755001251531e-17, 1.2011428730109348e-17, 1.1700850855607877e-17, 1.1245065181557657e-17, 1.065587631750339e-17, 9.948543945537414e-18, 9.141387602549055e-18, 8.255312213842004e-18, 7.313266666549777e-18, 6.3396494455135e-18, 5.359676725340423e-18, 4.3987292847270425e-18, 3.481695157622788e-18, 2.6323250462238016e-18, 1.8726171902617307e-18, 1.2222476241498217e-18, 6.980605780269622e-19, 3.1363222104495134e-19, 7.89190457186999e-20, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q8.xy.-y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.0012888458251578564, -0.00512200287075939, -0.011400194382788243, -0.01996081849886511, -0.030582159551072508, -0.04298913038529193, -0.05686039697399898, -0.07183670079878712, -0.08753016345728473, -0.10353433251003327, -0.11943470838516959, -0.1348194796996109, -0.14929018895756146, -0.16247205239035414, -0.17402366665919386, -0.18364585102230138, -0.19108939595897306, -0.19616151756526326, -0.19873085055583195, -0.19873085055583198, -0.19616151756526326, -0.19108939595897306, -0.18364585102230144, -0.17402366665919392, -0.16247205239035414, -0.1492901889575614, -0.13481947969961092, -0.11943470838516963, -0.10353433251003327, -0.08753016345728482, -0.07183670079878719, -0.05686039697399903, -0.042989130385291965, -0.03058215955107252, -0.01996081849886511, -0.011400194382788232, -0.005122002870759378, -0.0012888458251578564, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q8.xy.const.wf.I": {
            "type": "constant",
            "sample": 0.5,
        },
        "q8.xy.const.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q8.resonator.readout.wf.I": {
            "type": "constant",
            "sample": 0.31622776601683794,
        },
        "q8.resonator.readout.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q8.resonator.const.wf.I": {
            "type": "constant",
            "sample": 0.5,
        },
        "q8.resonator.const.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "cr_q1_q2.square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "cr_q1_q2.square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "cr_q5_q4.square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "cr_q5_q4.square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "zz_q5_q4.square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "zz_q5_q4.square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "cr_q2_q1.square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "cr_q2_q1.square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "cr_q2_q3.square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "cr_q2_q3.square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "cr_q3_q2.square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "cr_q3_q2.square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "cr_q3_q4.square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "cr_q3_q4.square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "cr_q4_q3.square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "cr_q4_q3.square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "cr_q4_q5.square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "cr_q4_q5.square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "cr_q5_q6.square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "cr_q5_q6.square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "cr_q6_q5.square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "cr_q6_q5.square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "cr_q6_q7.square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "cr_q6_q7.square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "cr_q7_q6.square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "cr_q7_q6.square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "cr_q7_q8.square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "cr_q7_q8.square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "cr_q8_q7.square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "cr_q8_q7.square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "cr_q8_q1.square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "cr_q8_q1.square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "cr_q1_q8.square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "cr_q1_q8.square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
    },
    "digital_waveforms": {
        "ON": {
            "samples": [(1, 0)],
        },
    },
    "integration_weights": {
        "q1.resonator.readout.iw1": {
            "cosine": [(1.0, 1000)],
            "sine": [(-0.0, 1000)],
        },
        "q1.resonator.readout.iw2": {
            "cosine": [(0.0, 1000)],
            "sine": [(1.0, 1000)],
        },
        "q1.resonator.readout.iw3": {
            "cosine": [(-0.0, 1000)],
            "sine": [(-1.0, 1000)],
        },
        "q2.resonator.readout.iw1": {
            "cosine": [(1.0, 1000)],
            "sine": [(-0.0, 1000)],
        },
        "q2.resonator.readout.iw2": {
            "cosine": [(0.0, 1000)],
            "sine": [(1.0, 1000)],
        },
        "q2.resonator.readout.iw3": {
            "cosine": [(-0.0, 1000)],
            "sine": [(-1.0, 1000)],
        },
        "q3.resonator.readout.iw1": {
            "cosine": [(1.0, 1000)],
            "sine": [(-0.0, 1000)],
        },
        "q3.resonator.readout.iw2": {
            "cosine": [(0.0, 1000)],
            "sine": [(1.0, 1000)],
        },
        "q3.resonator.readout.iw3": {
            "cosine": [(-0.0, 1000)],
            "sine": [(-1.0, 1000)],
        },
        "q4.resonator.readout.iw1": {
            "cosine": [(1.0, 1000)],
            "sine": [(-0.0, 1000)],
        },
        "q4.resonator.readout.iw2": {
            "cosine": [(0.0, 1000)],
            "sine": [(1.0, 1000)],
        },
        "q4.resonator.readout.iw3": {
            "cosine": [(-0.0, 1000)],
            "sine": [(-1.0, 1000)],
        },
        "q5.resonator.readout.iw1": {
            "cosine": [(1.0, 1000)],
            "sine": [(-0.0, 1000)],
        },
        "q5.resonator.readout.iw2": {
            "cosine": [(0.0, 1000)],
            "sine": [(1.0, 1000)],
        },
        "q5.resonator.readout.iw3": {
            "cosine": [(-0.0, 1000)],
            "sine": [(-1.0, 1000)],
        },
        "q6.resonator.readout.iw1": {
            "cosine": [(1.0, 1000)],
            "sine": [(-0.0, 1000)],
        },
        "q6.resonator.readout.iw2": {
            "cosine": [(0.0, 1000)],
            "sine": [(1.0, 1000)],
        },
        "q6.resonator.readout.iw3": {
            "cosine": [(-0.0, 1000)],
            "sine": [(-1.0, 1000)],
        },
        "q7.resonator.readout.iw1": {
            "cosine": [(1.0, 1000)],
            "sine": [(-0.0, 1000)],
        },
        "q7.resonator.readout.iw2": {
            "cosine": [(0.0, 1000)],
            "sine": [(1.0, 1000)],
        },
        "q7.resonator.readout.iw3": {
            "cosine": [(-0.0, 1000)],
            "sine": [(-1.0, 1000)],
        },
        "q8.resonator.readout.iw1": {
            "cosine": [(1.0, 1000)],
            "sine": [(-0.0, 1000)],
        },
        "q8.resonator.readout.iw2": {
            "cosine": [(0.0, 1000)],
            "sine": [(1.0, 1000)],
        },
        "q8.resonator.readout.iw3": {
            "cosine": [(-0.0, 1000)],
            "sine": [(-1.0, 1000)],
        },
    },
    "mixers": {},
}


