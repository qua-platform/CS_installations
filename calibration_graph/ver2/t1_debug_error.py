
# Single QUA script generated at 2024-12-04 18:52:18.784335
# QUA library version: 1.2.1

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
    v18 = declare(int, )
    with for_(v1,0,(v1<100),(v1+1)):
        r1 = declare_stream()
        save(v1, r1)
        with for_(v18,4,(v18<=24904),(v18+150)):
            wait(28750, "q1.xy", "q1.resonator")
            play("x180", "q1.xy")
            wait(v18, "q1.xy", "q1.resonator")
            align("q1.xy", "q1.resonator")
            measure("readout", "q1.resonator", None, dual_demod.full("iw1", "iw2", v2), dual_demod.full("iw3", "iw1", v10))
            r2 = declare_stream()
            save(v2, r2)
            r10 = declare_stream()
            save(v10, r10)
            align()
    align()
    with for_(v1,0,(v1<100),(v1+1)):
        save(v1, r1)
        with for_(v18,4,(v18<=24904),(v18+150)):
            wait(51250, "q2.xy", "q2.resonator")
            play("x180", "q2.xy")
            wait(v18, "q2.xy", "q2.resonator")
            align("q2.xy", "q2.resonator")
            measure("readout", "q2.resonator", None, dual_demod.full("iw1", "iw2", v3), dual_demod.full("iw3", "iw1", v11))
            r3 = declare_stream()
            save(v3, r3)
            r11 = declare_stream()
            save(v11, r11)
            align()
    align()
    with for_(v1,0,(v1<100),(v1+1)):
        save(v1, r1)
        with for_(v18,4,(v18<=24904),(v18+150)):
            wait(61250, "q3.xy", "q3.resonator")
            play("x180", "q3.xy")
            wait(v18, "q3.xy", "q3.resonator")
            align("q3.xy", "q3.resonator")
            measure("readout", "q3.resonator", None, dual_demod.full("iw1", "iw2", v4), dual_demod.full("iw3", "iw1", v12))
            r4 = declare_stream()
            save(v4, r4)
            r12 = declare_stream()
            save(v12, r12)
            align()
    align()
    with for_(v1,0,(v1<100),(v1+1)):
        save(v1, r1)
        with for_(v18,4,(v18<=24904),(v18+150)):
            wait(41249, "q4.xy", "q4.resonator")
            play("x180", "q4.xy")
            wait(v18, "q4.xy", "q4.resonator")
            align("q4.xy", "q4.resonator")
            measure("readout", "q4.resonator", None, dual_demod.full("iw1", "iw2", v5), dual_demod.full("iw3", "iw1", v13))
            r5 = declare_stream()
            save(v5, r5)
            r13 = declare_stream()
            save(v13, r13)
            align()
    align()
    with for_(v1,0,(v1<100),(v1+1)):
        save(v1, r1)
        with for_(v18,4,(v18<=24904),(v18+150)):
            wait(61250, "q5.xy", "q5.resonator")
            play("x180", "q5.xy")
            wait(v18, "q5.xy", "q5.resonator")
            align("q5.xy", "q5.resonator")
            measure("readout", "q5.resonator", None, dual_demod.full("iw1", "iw2", v6), dual_demod.full("iw3", "iw1", v14))
            r6 = declare_stream()
            save(v6, r6)
            r14 = declare_stream()
            save(v14, r14)
            align()
    align()
    with for_(v1,0,(v1<100),(v1+1)):
        save(v1, r1)
        with for_(v18,4,(v18<=24904),(v18+150)):
            wait(17500, "q6.xy", "q6.resonator")
            play("x180", "q6.xy")
            wait(v18, "q6.xy", "q6.resonator")
            align("q6.xy", "q6.resonator")
            measure("readout", "q6.resonator", None, dual_demod.full("iw1", "iw2", v7), dual_demod.full("iw3", "iw1", v15))
            r7 = declare_stream()
            save(v7, r7)
            r15 = declare_stream()
            save(v15, r15)
            align()
    align()
    with for_(v1,0,(v1<100),(v1+1)):
        save(v1, r1)
        with for_(v18,4,(v18<=24904),(v18+150)):
            wait(23749, "q7.xy", "q7.resonator")
            play("x180", "q7.xy")
            wait(v18, "q7.xy", "q7.resonator")
            align("q7.xy", "q7.resonator")
            measure("readout", "q7.resonator", None, dual_demod.full("iw1", "iw2", v8), dual_demod.full("iw3", "iw1", v16))
            r8 = declare_stream()
            save(v8, r8)
            r16 = declare_stream()
            save(v16, r16)
            align()
    align()
    with for_(v1,0,(v1<100),(v1+1)):
        save(v1, r1)
        with for_(v18,4,(v18<=24904),(v18+150)):
            wait(42500, "q8.xy", "q8.resonator")
            play("x180", "q8.xy")
            wait(v18, "q8.xy", "q8.resonator")
            align("q8.xy", "q8.resonator")
            measure("readout", "q8.resonator", None, dual_demod.full("iw1", "iw2", v9), dual_demod.full("iw3", "iw1", v17))
            r9 = declare_stream()
            save(v9, r9)
            r17 = declare_stream()
            save(v17, r17)
            align()
    align()
    with stream_processing():
        r1.save("n")
        r2.buffer(167).average().save("I1")
        r10.buffer(167).average().save("Q1")
        r3.buffer(167).average().save("I2")
        r11.buffer(167).average().save("Q2")
        r4.buffer(167).average().save("I3")
        r12.buffer(167).average().save("Q3")
        r5.buffer(167).average().save("I4")
        r13.buffer(167).average().save("Q4")
        r6.buffer(167).average().save("I5")
        r14.buffer(167).average().save("Q5")
        r7.buffer(167).average().save("I6")
        r15.buffer(167).average().save("Q6")
        r8.buffer(167).average().save("I7")
        r16.buffer(167).average().save("Q7")
        r9.buffer(167).average().save("I8")
        r17.buffer(167).average().save("Q8")


config = {
    "version": 1,
    "controllers": {
        "con1": {
            "fems": {
                "2": {
                    "type": "MW",
                    "analog_outputs": {
                        "1": {
                            "band": 3,
                            "delay": 0,
                            "shareable": False,
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": -14,
                            "upconverter_frequency": 9983000000,
                        },
                        "2": {
                            "band": 1,
                            "delay": 0,
                            "shareable": False,
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": 1,
                            "upconverter_frequency": 4551000000,
                        },
                        "8": {
                            "band": 3,
                            "delay": 0,
                            "shareable": False,
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": -14,
                            "upconverter_frequency": 9572000000,
                        },
                        "3": {
                            "band": 1,
                            "delay": 0,
                            "shareable": False,
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": 1,
                            "upconverter_frequency": 4320000000,
                        },
                    },
                    "analog_inputs": {
                        "1": {
                            "band": 3,
                            "downconverter_frequency": 9983000000,
                            "sampling_rate": 1000000000.0,
                            "shareable": False,
                        },
                        "2": {
                            "band": 3,
                            "downconverter_frequency": 9572000000,
                            "sampling_rate": 1000000000.0,
                            "shareable": False,
                        },
                    },
                },
                "3": {
                    "type": "MW",
                    "analog_outputs": {
                        "1": {
                            "band": 3,
                            "delay": 0,
                            "shareable": False,
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": -14,
                            "upconverter_frequency": 9896000000,
                        },
                        "2": {
                            "band": 1,
                            "delay": 0,
                            "shareable": False,
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": 1,
                            "upconverter_frequency": 4303000000,
                        },
                        "8": {
                            "band": 3,
                            "delay": 0,
                            "shareable": False,
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": -14,
                            "upconverter_frequency": 9374000000,
                        },
                        "3": {
                            "band": 1,
                            "delay": 0,
                            "shareable": False,
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": 1,
                            "upconverter_frequency": 4053000000,
                        },
                    },
                    "analog_inputs": {
                        "1": {
                            "band": 3,
                            "downconverter_frequency": 9896000000,
                            "sampling_rate": 1000000000.0,
                            "shareable": False,
                        },
                        "2": {
                            "band": 3,
                            "downconverter_frequency": 9374000000,
                            "sampling_rate": 1000000000.0,
                            "shareable": False,
                        },
                    },
                },
                "5": {
                    "type": "MW",
                    "analog_outputs": {
                        "1": {
                            "band": 3,
                            "delay": 0,
                            "shareable": False,
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": -14,
                            "upconverter_frequency": 9697000000,
                        },
                        "2": {
                            "band": 1,
                            "delay": 0,
                            "shareable": False,
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": 1,
                            "upconverter_frequency": 4461000000,
                        },
                        "8": {
                            "band": 3,
                            "delay": 0,
                            "shareable": False,
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": -14,
                            "upconverter_frequency": 9275000000,
                        },
                        "3": {
                            "band": 1,
                            "delay": 0,
                            "shareable": False,
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": 1,
                            "upconverter_frequency": 4406000000,
                        },
                    },
                    "analog_inputs": {
                        "1": {
                            "band": 3,
                            "downconverter_frequency": 9697000000,
                            "sampling_rate": 1000000000.0,
                            "shareable": False,
                        },
                        "2": {
                            "band": 3,
                            "downconverter_frequency": 9275000000,
                            "sampling_rate": 1000000000.0,
                            "shareable": False,
                        },
                    },
                },
                "7": {
                    "type": "MW",
                    "analog_outputs": {
                        "1": {
                            "band": 3,
                            "delay": 0,
                            "shareable": False,
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": -14,
                            "upconverter_frequency": 9792000000,
                        },
                        "2": {
                            "band": 1,
                            "delay": 0,
                            "shareable": False,
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": 1,
                            "upconverter_frequency": 4464000000,
                        },
                        "8": {
                            "band": 3,
                            "delay": 0,
                            "shareable": False,
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": -14,
                            "upconverter_frequency": 9468000000,
                        },
                        "3": {
                            "band": 1,
                            "delay": 0,
                            "shareable": False,
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": 1,
                            "upconverter_frequency": 4268000000,
                        },
                    },
                    "analog_inputs": {
                        "1": {
                            "band": 3,
                            "downconverter_frequency": 9792000000,
                            "sampling_rate": 1000000000.0,
                            "shareable": False,
                        },
                        "2": {
                            "band": 3,
                            "downconverter_frequency": 9468000000,
                            "sampling_rate": 1000000000.0,
                            "shareable": False,
                        },
                    },
                },
            },
        },
    },
    "elements": {
        "q1.xy": {
            "operations": {
                "x180_DragCosine": "q1.xy.x180_DragCosine.pulse",
                "x90_DragCosine": "q1.xy.x90_DragCosine.pulse",
                "-x90_DragCosine": "q1.xy.-x90_DragCosine.pulse",
                "y180_DragCosine": "q1.xy.y180_DragCosine.pulse",
                "y90_DragCosine": "q1.xy.y90_DragCosine.pulse",
                "-y90_DragCosine": "q1.xy.-y90_DragCosine.pulse",
                "x180_Square": "q1.xy.x180_Square.pulse",
                "x90_Square": "q1.xy.x90_Square.pulse",
                "-x90_Square": "q1.xy.-x90_Square.pulse",
                "y180_Square": "q1.xy.y180_Square.pulse",
                "y90_Square": "q1.xy.y90_Square.pulse",
                "-y90_Square": "q1.xy.-y90_Square.pulse",
                "x180": "q1.xy.x180_DragCosine.pulse",
                "x90": "q1.xy.x90_DragCosine.pulse",
                "-x90": "q1.xy.-x90_DragCosine.pulse",
                "y180": "q1.xy.y180_DragCosine.pulse",
                "y90": "q1.xy.y90_DragCosine.pulse",
                "-y90": "q1.xy.-y90_DragCosine.pulse",
                "saturation": "q1.xy.saturation.pulse",
                "cr_q8_q1_Square": "q1.xy.cr_q8_q1_Square.pulse",
            },
            "intermediate_frequency": 51500000.0,
            "MWInput": {
                "port": ('con1', 2, 2),
                "upconverter": 1,
            },
        },
        "q1.xy_detuned": {
            "operations": {
                "zz_q8_q1_Square": "q1.xy_detuned.zz_q8_q1_Square.pulse",
            },
            "intermediate_frequency": -210000000,
            "MWInput": {
                "port": ('con1', 2, 2),
                "upconverter": 1,
            },
        },
        "q1.resonator": {
            "operations": {
                "readout": "q1.resonator.readout.pulse",
                "const": "q1.resonator.const.pulse",
            },
            "intermediate_frequency": 50113489,
            "MWOutput": {
                "port": ('con1', 2, 1),
            },
            "smearing": 0,
            "time_of_flight": 304,
            "MWInput": {
                "port": ('con1', 2, 1),
                "upconverter": 1,
            },
        },
        "q2.xy": {
            "operations": {
                "x180_DragCosine": "q2.xy.x180_DragCosine.pulse",
                "x90_DragCosine": "q2.xy.x90_DragCosine.pulse",
                "-x90_DragCosine": "q2.xy.-x90_DragCosine.pulse",
                "y180_DragCosine": "q2.xy.y180_DragCosine.pulse",
                "y90_DragCosine": "q2.xy.y90_DragCosine.pulse",
                "-y90_DragCosine": "q2.xy.-y90_DragCosine.pulse",
                "x180_Square": "q2.xy.x180_Square.pulse",
                "x90_Square": "q2.xy.x90_Square.pulse",
                "-x90_Square": "q2.xy.-x90_Square.pulse",
                "y180_Square": "q2.xy.y180_Square.pulse",
                "y90_Square": "q2.xy.y90_Square.pulse",
                "-y90_Square": "q2.xy.-y90_Square.pulse",
                "x180": "q2.xy.x180_DragCosine.pulse",
                "x90": "q2.xy.x90_DragCosine.pulse",
                "-x90": "q2.xy.-x90_DragCosine.pulse",
                "y180": "q2.xy.y180_DragCosine.pulse",
                "y90": "q2.xy.y90_DragCosine.pulse",
                "-y90": "q2.xy.-y90_DragCosine.pulse",
                "saturation": "q2.xy.saturation.pulse",
                "cr_q1_q2_Square": "q2.xy.cr_q1_q2_Square.pulse",
            },
            "intermediate_frequency": 51000000.0,
            "MWInput": {
                "port": ('con1', 2, 3),
                "upconverter": 1,
            },
        },
        "q2.xy_detuned": {
            "operations": {
                "zz_q1_q2_Square": "q2.xy_detuned.zz_q1_q2_Square.pulse",
            },
            "intermediate_frequency": -210000000,
            "MWInput": {
                "port": ('con1', 2, 3),
                "upconverter": 1,
            },
        },
        "q2.resonator": {
            "operations": {
                "readout": "q2.resonator.readout.pulse",
                "const": "q2.resonator.const.pulse",
            },
            "intermediate_frequency": 49013812,
            "MWOutput": {
                "port": ('con1', 2, 2),
            },
            "smearing": 0,
            "time_of_flight": 304,
            "MWInput": {
                "port": ('con1', 2, 8),
                "upconverter": 1,
            },
        },
        "q3.xy": {
            "operations": {
                "x180_DragCosine": "q3.xy.x180_DragCosine.pulse",
                "x90_DragCosine": "q3.xy.x90_DragCosine.pulse",
                "-x90_DragCosine": "q3.xy.-x90_DragCosine.pulse",
                "y180_DragCosine": "q3.xy.y180_DragCosine.pulse",
                "y90_DragCosine": "q3.xy.y90_DragCosine.pulse",
                "-y90_DragCosine": "q3.xy.-y90_DragCosine.pulse",
                "x180_Square": "q3.xy.x180_Square.pulse",
                "x90_Square": "q3.xy.x90_Square.pulse",
                "-x90_Square": "q3.xy.-x90_Square.pulse",
                "y180_Square": "q3.xy.y180_Square.pulse",
                "y90_Square": "q3.xy.y90_Square.pulse",
                "-y90_Square": "q3.xy.-y90_Square.pulse",
                "x180": "q3.xy.x180_DragCosine.pulse",
                "x90": "q3.xy.x90_DragCosine.pulse",
                "-x90": "q3.xy.-x90_DragCosine.pulse",
                "y180": "q3.xy.y180_DragCosine.pulse",
                "y90": "q3.xy.y90_DragCosine.pulse",
                "-y90": "q3.xy.-y90_DragCosine.pulse",
                "saturation": "q3.xy.saturation.pulse",
                "cr_q2_q3_Square": "q3.xy.cr_q2_q3_Square.pulse",
            },
            "intermediate_frequency": 48000000.0,
            "MWInput": {
                "port": ('con1', 3, 2),
                "upconverter": 1,
            },
        },
        "q3.xy_detuned": {
            "operations": {
                "zz_q2_q3_Square": "q3.xy_detuned.zz_q2_q3_Square.pulse",
            },
            "intermediate_frequency": -210000000,
            "MWInput": {
                "port": ('con1', 3, 2),
                "upconverter": 1,
            },
        },
        "q3.resonator": {
            "operations": {
                "readout": "q3.resonator.readout.pulse",
                "const": "q3.resonator.const.pulse",
            },
            "intermediate_frequency": 50146943,
            "MWOutput": {
                "port": ('con1', 3, 1),
            },
            "smearing": 0,
            "time_of_flight": 304,
            "MWInput": {
                "port": ('con1', 3, 1),
                "upconverter": 1,
            },
        },
        "q4.xy": {
            "operations": {
                "x180_DragCosine": "q4.xy.x180_DragCosine.pulse",
                "x90_DragCosine": "q4.xy.x90_DragCosine.pulse",
                "-x90_DragCosine": "q4.xy.-x90_DragCosine.pulse",
                "y180_DragCosine": "q4.xy.y180_DragCosine.pulse",
                "y90_DragCosine": "q4.xy.y90_DragCosine.pulse",
                "-y90_DragCosine": "q4.xy.-y90_DragCosine.pulse",
                "x180_Square": "q4.xy.x180_Square.pulse",
                "x90_Square": "q4.xy.x90_Square.pulse",
                "-x90_Square": "q4.xy.-x90_Square.pulse",
                "y180_Square": "q4.xy.y180_Square.pulse",
                "y90_Square": "q4.xy.y90_Square.pulse",
                "-y90_Square": "q4.xy.-y90_Square.pulse",
                "x180": "q4.xy.x180_DragCosine.pulse",
                "x90": "q4.xy.x90_DragCosine.pulse",
                "-x90": "q4.xy.-x90_DragCosine.pulse",
                "y180": "q4.xy.y180_DragCosine.pulse",
                "y90": "q4.xy.y90_DragCosine.pulse",
                "-y90": "q4.xy.-y90_DragCosine.pulse",
                "saturation": "q4.xy.saturation.pulse",
                "cr_q3_q4_Square": "q4.xy.cr_q3_q4_Square.pulse",
            },
            "intermediate_frequency": 50750000.0,
            "MWInput": {
                "port": ('con1', 3, 3),
                "upconverter": 1,
            },
        },
        "q4.xy_detuned": {
            "operations": {
                "zz_q3_q4_Square": "q4.xy_detuned.zz_q3_q4_Square.pulse",
            },
            "intermediate_frequency": -210000000,
            "MWInput": {
                "port": ('con1', 3, 3),
                "upconverter": 1,
            },
        },
        "q4.resonator": {
            "operations": {
                "readout": "q4.resonator.readout.pulse",
                "const": "q4.resonator.const.pulse",
            },
            "intermediate_frequency": 48881765,
            "MWOutput": {
                "port": ('con1', 3, 2),
            },
            "smearing": 0,
            "time_of_flight": 24,
            "MWInput": {
                "port": ('con1', 3, 8),
                "upconverter": 1,
            },
        },
        "q5.xy": {
            "operations": {
                "x180_DragCosine": "q5.xy.x180_DragCosine.pulse",
                "x90_DragCosine": "q5.xy.x90_DragCosine.pulse",
                "-x90_DragCosine": "q5.xy.-x90_DragCosine.pulse",
                "y180_DragCosine": "q5.xy.y180_DragCosine.pulse",
                "y90_DragCosine": "q5.xy.y90_DragCosine.pulse",
                "-y90_DragCosine": "q5.xy.-y90_DragCosine.pulse",
                "x180_Square": "q5.xy.x180_Square.pulse",
                "x90_Square": "q5.xy.x90_Square.pulse",
                "-x90_Square": "q5.xy.-x90_Square.pulse",
                "y180_Square": "q5.xy.y180_Square.pulse",
                "y90_Square": "q5.xy.y90_Square.pulse",
                "-y90_Square": "q5.xy.-y90_Square.pulse",
                "x180": "q5.xy.x180_DragCosine.pulse",
                "x90": "q5.xy.x90_DragCosine.pulse",
                "-x90": "q5.xy.-x90_DragCosine.pulse",
                "y180": "q5.xy.y180_DragCosine.pulse",
                "y90": "q5.xy.y90_DragCosine.pulse",
                "-y90": "q5.xy.-y90_DragCosine.pulse",
                "saturation": "q5.xy.saturation.pulse",
                "cr_q4_q5_Square": "q5.xy.cr_q4_q5_Square.pulse",
            },
            "intermediate_frequency": 50250000.0,
            "MWInput": {
                "port": ('con1', 5, 2),
                "upconverter": 1,
            },
        },
        "q5.xy_detuned": {
            "operations": {
                "zz_q4_q5_Square": "q5.xy_detuned.zz_q4_q5_Square.pulse",
            },
            "intermediate_frequency": -210000000,
            "MWInput": {
                "port": ('con1', 5, 2),
                "upconverter": 1,
            },
        },
        "q5.resonator": {
            "operations": {
                "readout": "q5.resonator.readout.pulse",
                "const": "q5.resonator.const.pulse",
            },
            "intermediate_frequency": 50216992,
            "MWOutput": {
                "port": ('con1', 5, 1),
            },
            "smearing": 0,
            "time_of_flight": 304,
            "MWInput": {
                "port": ('con1', 5, 1),
                "upconverter": 1,
            },
        },
        "q6.xy": {
            "operations": {
                "x180_DragCosine": "q6.xy.x180_DragCosine.pulse",
                "x90_DragCosine": "q6.xy.x90_DragCosine.pulse",
                "-x90_DragCosine": "q6.xy.-x90_DragCosine.pulse",
                "y180_DragCosine": "q6.xy.y180_DragCosine.pulse",
                "y90_DragCosine": "q6.xy.y90_DragCosine.pulse",
                "-y90_DragCosine": "q6.xy.-y90_DragCosine.pulse",
                "x180_Square": "q6.xy.x180_Square.pulse",
                "x90_Square": "q6.xy.x90_Square.pulse",
                "-x90_Square": "q6.xy.-x90_Square.pulse",
                "y180_Square": "q6.xy.y180_Square.pulse",
                "y90_Square": "q6.xy.y90_Square.pulse",
                "-y90_Square": "q6.xy.-y90_Square.pulse",
                "x180": "q6.xy.x180_DragCosine.pulse",
                "x90": "q6.xy.x90_DragCosine.pulse",
                "-x90": "q6.xy.-x90_DragCosine.pulse",
                "y180": "q6.xy.y180_DragCosine.pulse",
                "y90": "q6.xy.y90_DragCosine.pulse",
                "-y90": "q6.xy.-y90_DragCosine.pulse",
                "saturation": "q6.xy.saturation.pulse",
                "cr_q5_q6_Square": "q6.xy.cr_q5_q6_Square.pulse",
            },
            "intermediate_frequency": 51250000.0,
            "MWInput": {
                "port": ('con1', 5, 3),
                "upconverter": 1,
            },
        },
        "q6.xy_detuned": {
            "operations": {
                "zz_q5_q6_Square": "q6.xy_detuned.zz_q5_q6_Square.pulse",
            },
            "intermediate_frequency": -210000000,
            "MWInput": {
                "port": ('con1', 5, 3),
                "upconverter": 1,
            },
        },
        "q6.resonator": {
            "operations": {
                "readout": "q6.resonator.readout.pulse",
                "const": "q6.resonator.const.pulse",
            },
            "intermediate_frequency": 49625230,
            "MWOutput": {
                "port": ('con1', 5, 2),
            },
            "smearing": 0,
            "time_of_flight": 24,
            "MWInput": {
                "port": ('con1', 5, 8),
                "upconverter": 1,
            },
        },
        "q7.xy": {
            "operations": {
                "x180_DragCosine": "q7.xy.x180_DragCosine.pulse",
                "x90_DragCosine": "q7.xy.x90_DragCosine.pulse",
                "-x90_DragCosine": "q7.xy.-x90_DragCosine.pulse",
                "y180_DragCosine": "q7.xy.y180_DragCosine.pulse",
                "y90_DragCosine": "q7.xy.y90_DragCosine.pulse",
                "-y90_DragCosine": "q7.xy.-y90_DragCosine.pulse",
                "x180_Square": "q7.xy.x180_Square.pulse",
                "x90_Square": "q7.xy.x90_Square.pulse",
                "-x90_Square": "q7.xy.-x90_Square.pulse",
                "y180_Square": "q7.xy.y180_Square.pulse",
                "y90_Square": "q7.xy.y90_Square.pulse",
                "-y90_Square": "q7.xy.-y90_Square.pulse",
                "x180": "q7.xy.x180_DragCosine.pulse",
                "x90": "q7.xy.x90_DragCosine.pulse",
                "-x90": "q7.xy.-x90_DragCosine.pulse",
                "y180": "q7.xy.y180_DragCosine.pulse",
                "y90": "q7.xy.y90_DragCosine.pulse",
                "-y90": "q7.xy.-y90_DragCosine.pulse",
                "saturation": "q7.xy.saturation.pulse",
                "cr_q6_q7_Square": "q7.xy.cr_q6_q7_Square.pulse",
            },
            "intermediate_frequency": 51250000.0,
            "MWInput": {
                "port": ('con1', 7, 2),
                "upconverter": 1,
            },
        },
        "q7.xy_detuned": {
            "operations": {
                "zz_q6_q7_Square": "q7.xy_detuned.zz_q6_q7_Square.pulse",
            },
            "intermediate_frequency": -210000000,
            "MWInput": {
                "port": ('con1', 7, 2),
                "upconverter": 1,
            },
        },
        "q7.resonator": {
            "operations": {
                "readout": "q7.resonator.readout.pulse",
                "const": "q7.resonator.const.pulse",
            },
            "intermediate_frequency": 49550000,
            "MWOutput": {
                "port": ('con1', 7, 1),
            },
            "smearing": 0,
            "time_of_flight": 304,
            "MWInput": {
                "port": ('con1', 7, 1),
                "upconverter": 1,
            },
        },
        "q8.xy": {
            "operations": {
                "x180_DragCosine": "q8.xy.x180_DragCosine.pulse",
                "x90_DragCosine": "q8.xy.x90_DragCosine.pulse",
                "-x90_DragCosine": "q8.xy.-x90_DragCosine.pulse",
                "y180_DragCosine": "q8.xy.y180_DragCosine.pulse",
                "y90_DragCosine": "q8.xy.y90_DragCosine.pulse",
                "-y90_DragCosine": "q8.xy.-y90_DragCosine.pulse",
                "x180_Square": "q8.xy.x180_Square.pulse",
                "x90_Square": "q8.xy.x90_Square.pulse",
                "-x90_Square": "q8.xy.-x90_Square.pulse",
                "y180_Square": "q8.xy.y180_Square.pulse",
                "y90_Square": "q8.xy.y90_Square.pulse",
                "-y90_Square": "q8.xy.-y90_Square.pulse",
                "x180": "q8.xy.x180_DragCosine.pulse",
                "x90": "q8.xy.x90_DragCosine.pulse",
                "-x90": "q8.xy.-x90_DragCosine.pulse",
                "y180": "q8.xy.y180_DragCosine.pulse",
                "y90": "q8.xy.y90_DragCosine.pulse",
                "-y90": "q8.xy.-y90_DragCosine.pulse",
                "saturation": "q8.xy.saturation.pulse",
                "cr_q7_q8_Square": "q8.xy.cr_q7_q8_Square.pulse",
            },
            "intermediate_frequency": 51000000.0,
            "MWInput": {
                "port": ('con1', 7, 3),
                "upconverter": 1,
            },
        },
        "q8.xy_detuned": {
            "operations": {
                "zz_q7_q8_Square": "q8.xy_detuned.zz_q7_q8_Square.pulse",
            },
            "intermediate_frequency": -210000000,
            "MWInput": {
                "port": ('con1', 7, 3),
                "upconverter": 1,
            },
        },
        "q8.resonator": {
            "operations": {
                "readout": "q8.resonator.readout.pulse",
                "const": "q8.resonator.const.pulse",
            },
            "intermediate_frequency": 49700000,
            "MWOutput": {
                "port": ('con1', 7, 2),
            },
            "smearing": 0,
            "time_of_flight": 24,
            "MWInput": {
                "port": ('con1', 7, 8),
                "upconverter": 1,
            },
        },
        "cr_q1_q2": {
            "operations": {
                "square": "cr_q1_q2.square.pulse",
            },
            "thread": "q1",
            "MWInput": {
                "port": ('con1', 2, 2),
                "upconverter": 1,
            },
        },
        "zz_q1_q2": {
            "operations": {
                "square": "zz_q1_q2.square.pulse",
            },
            "thread": "q1",
            "MWInput": {
                "port": ('con1', 2, 2),
                "upconverter": 1,
            },
        },
        "cr_q2_q3": {
            "operations": {
                "square": "cr_q2_q3.square.pulse",
            },
            "thread": "q2",
            "MWInput": {
                "port": ('con1', 2, 3),
                "upconverter": 1,
            },
        },
        "zz_q2_q3": {
            "operations": {
                "square": "zz_q2_q3.square.pulse",
            },
            "thread": "q2",
            "MWInput": {
                "port": ('con1', 2, 3),
                "upconverter": 1,
            },
        },
        "cr_q3_q4": {
            "operations": {
                "square": "cr_q3_q4.square.pulse",
            },
            "thread": "q3",
            "MWInput": {
                "port": ('con1', 3, 2),
                "upconverter": 1,
            },
        },
        "zz_q3_q4": {
            "operations": {
                "square": "zz_q3_q4.square.pulse",
            },
            "thread": "q3",
            "MWInput": {
                "port": ('con1', 3, 2),
                "upconverter": 1,
            },
        },
        "cr_q4_q5": {
            "operations": {
                "square": "cr_q4_q5.square.pulse",
            },
            "thread": "q4",
            "MWInput": {
                "port": ('con1', 3, 3),
                "upconverter": 1,
            },
        },
        "zz_q4_q5": {
            "operations": {
                "square": "zz_q4_q5.square.pulse",
            },
            "thread": "q4",
            "MWInput": {
                "port": ('con1', 3, 3),
                "upconverter": 1,
            },
        },
        "cr_q5_q6": {
            "operations": {
                "square": "cr_q5_q6.square.pulse",
            },
            "thread": "q5",
            "MWInput": {
                "port": ('con1', 5, 2),
                "upconverter": 1,
            },
        },
        "zz_q5_q6": {
            "operations": {
                "square": "zz_q5_q6.square.pulse",
            },
            "thread": "q5",
            "MWInput": {
                "port": ('con1', 5, 2),
                "upconverter": 1,
            },
        },
        "cr_q6_q7": {
            "operations": {
                "square": "cr_q6_q7.square.pulse",
            },
            "thread": "q6",
            "MWInput": {
                "port": ('con1', 5, 3),
                "upconverter": 1,
            },
        },
        "zz_q6_q7": {
            "operations": {
                "square": "zz_q6_q7.square.pulse",
            },
            "thread": "q6",
            "MWInput": {
                "port": ('con1', 5, 3),
                "upconverter": 1,
            },
        },
        "cr_q7_q8": {
            "operations": {
                "square": "cr_q7_q8.square.pulse",
            },
            "thread": "q7",
            "MWInput": {
                "port": ('con1', 7, 2),
                "upconverter": 1,
            },
        },
        "zz_q7_q8": {
            "operations": {
                "square": "zz_q7_q8.square.pulse",
            },
            "thread": "q7",
            "MWInput": {
                "port": ('con1', 7, 2),
                "upconverter": 1,
            },
        },
        "cr_q8_q1": {
            "operations": {
                "square": "cr_q8_q1.square.pulse",
            },
            "thread": "q8",
            "MWInput": {
                "port": ('con1', 7, 3),
                "upconverter": 1,
            },
        },
        "zz_q8_q1": {
            "operations": {
                "square": "zz_q8_q1.square.pulse",
            },
            "thread": "q8",
            "MWInput": {
                "port": ('con1', 7, 3),
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
        "q1.xy.x180_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q1.xy.x180_DragCosine.wf.I",
                "Q": "q1.xy.x180_DragCosine.wf.Q",
            },
        },
        "q1.xy.x90_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q1.xy.x90_DragCosine.wf.I",
                "Q": "q1.xy.x90_DragCosine.wf.Q",
            },
        },
        "q1.xy.-x90_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q1.xy.-x90_DragCosine.wf.I",
                "Q": "q1.xy.-x90_DragCosine.wf.Q",
            },
        },
        "q1.xy.y180_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q1.xy.y180_DragCosine.wf.I",
                "Q": "q1.xy.y180_DragCosine.wf.Q",
            },
        },
        "q1.xy.y90_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q1.xy.y90_DragCosine.wf.I",
                "Q": "q1.xy.y90_DragCosine.wf.Q",
            },
        },
        "q1.xy.-y90_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q1.xy.-y90_DragCosine.wf.I",
                "Q": "q1.xy.-y90_DragCosine.wf.Q",
            },
        },
        "q1.xy.x180_Square.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q1.xy.x180_Square.wf.I",
                "Q": "q1.xy.x180_Square.wf.Q",
            },
        },
        "q1.xy.x90_Square.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q1.xy.x90_Square.wf.I",
                "Q": "q1.xy.x90_Square.wf.Q",
            },
        },
        "q1.xy.-x90_Square.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q1.xy.-x90_Square.wf.I",
                "Q": "q1.xy.-x90_Square.wf.Q",
            },
        },
        "q1.xy.y180_Square.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q1.xy.y180_Square.wf.I",
                "Q": "q1.xy.y180_Square.wf.Q",
            },
        },
        "q1.xy.y90_Square.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q1.xy.y90_Square.wf.I",
                "Q": "q1.xy.y90_Square.wf.Q",
            },
        },
        "q1.xy.-y90_Square.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q1.xy.-y90_Square.wf.I",
                "Q": "q1.xy.-y90_Square.wf.Q",
            },
        },
        "q1.xy.saturation.pulse": {
            "operation": "control",
            "length": 40000,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q1.xy.saturation.wf.I",
                "Q": "q1.xy.saturation.wf.Q",
            },
        },
        "q1.xy.cr_q8_q1_Square.pulse": {
            "operation": "control",
            "length": 100,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q1.xy.cr_q8_q1_Square.wf.I",
                "Q": "q1.xy.cr_q8_q1_Square.wf.Q",
            },
        },
        "q1.xy_detuned.zz_q8_q1_Square.pulse": {
            "operation": "control",
            "length": 100,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q1.xy_detuned.zz_q8_q1_Square.wf.I",
                "Q": "q1.xy_detuned.zz_q8_q1_Square.wf.Q",
            },
        },
        "q1.resonator.readout.pulse": {
            "operation": "measurement",
            "length": 2000,
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
            "length": 100,
            "waveforms": {
                "I": "q1.resonator.const.wf.I",
                "Q": "q1.resonator.const.wf.Q",
            },
        },
        "q2.xy.x180_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q2.xy.x180_DragCosine.wf.I",
                "Q": "q2.xy.x180_DragCosine.wf.Q",
            },
        },
        "q2.xy.x90_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q2.xy.x90_DragCosine.wf.I",
                "Q": "q2.xy.x90_DragCosine.wf.Q",
            },
        },
        "q2.xy.-x90_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q2.xy.-x90_DragCosine.wf.I",
                "Q": "q2.xy.-x90_DragCosine.wf.Q",
            },
        },
        "q2.xy.y180_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q2.xy.y180_DragCosine.wf.I",
                "Q": "q2.xy.y180_DragCosine.wf.Q",
            },
        },
        "q2.xy.y90_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q2.xy.y90_DragCosine.wf.I",
                "Q": "q2.xy.y90_DragCosine.wf.Q",
            },
        },
        "q2.xy.-y90_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q2.xy.-y90_DragCosine.wf.I",
                "Q": "q2.xy.-y90_DragCosine.wf.Q",
            },
        },
        "q2.xy.x180_Square.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q2.xy.x180_Square.wf.I",
                "Q": "q2.xy.x180_Square.wf.Q",
            },
        },
        "q2.xy.x90_Square.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q2.xy.x90_Square.wf.I",
                "Q": "q2.xy.x90_Square.wf.Q",
            },
        },
        "q2.xy.-x90_Square.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q2.xy.-x90_Square.wf.I",
                "Q": "q2.xy.-x90_Square.wf.Q",
            },
        },
        "q2.xy.y180_Square.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q2.xy.y180_Square.wf.I",
                "Q": "q2.xy.y180_Square.wf.Q",
            },
        },
        "q2.xy.y90_Square.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q2.xy.y90_Square.wf.I",
                "Q": "q2.xy.y90_Square.wf.Q",
            },
        },
        "q2.xy.-y90_Square.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q2.xy.-y90_Square.wf.I",
                "Q": "q2.xy.-y90_Square.wf.Q",
            },
        },
        "q2.xy.saturation.pulse": {
            "operation": "control",
            "length": 40000,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q2.xy.saturation.wf.I",
                "Q": "q2.xy.saturation.wf.Q",
            },
        },
        "q2.xy.cr_q1_q2_Square.pulse": {
            "operation": "control",
            "length": 100,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q2.xy.cr_q1_q2_Square.wf.I",
                "Q": "q2.xy.cr_q1_q2_Square.wf.Q",
            },
        },
        "q2.xy_detuned.zz_q1_q2_Square.pulse": {
            "operation": "control",
            "length": 100,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q2.xy_detuned.zz_q1_q2_Square.wf.I",
                "Q": "q2.xy_detuned.zz_q1_q2_Square.wf.Q",
            },
        },
        "q2.resonator.readout.pulse": {
            "operation": "measurement",
            "length": 2000,
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
            "length": 100,
            "waveforms": {
                "I": "q2.resonator.const.wf.I",
                "Q": "q2.resonator.const.wf.Q",
            },
        },
        "q3.xy.x180_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q3.xy.x180_DragCosine.wf.I",
                "Q": "q3.xy.x180_DragCosine.wf.Q",
            },
        },
        "q3.xy.x90_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q3.xy.x90_DragCosine.wf.I",
                "Q": "q3.xy.x90_DragCosine.wf.Q",
            },
        },
        "q3.xy.-x90_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q3.xy.-x90_DragCosine.wf.I",
                "Q": "q3.xy.-x90_DragCosine.wf.Q",
            },
        },
        "q3.xy.y180_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q3.xy.y180_DragCosine.wf.I",
                "Q": "q3.xy.y180_DragCosine.wf.Q",
            },
        },
        "q3.xy.y90_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q3.xy.y90_DragCosine.wf.I",
                "Q": "q3.xy.y90_DragCosine.wf.Q",
            },
        },
        "q3.xy.-y90_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q3.xy.-y90_DragCosine.wf.I",
                "Q": "q3.xy.-y90_DragCosine.wf.Q",
            },
        },
        "q3.xy.x180_Square.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q3.xy.x180_Square.wf.I",
                "Q": "q3.xy.x180_Square.wf.Q",
            },
        },
        "q3.xy.x90_Square.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q3.xy.x90_Square.wf.I",
                "Q": "q3.xy.x90_Square.wf.Q",
            },
        },
        "q3.xy.-x90_Square.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q3.xy.-x90_Square.wf.I",
                "Q": "q3.xy.-x90_Square.wf.Q",
            },
        },
        "q3.xy.y180_Square.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q3.xy.y180_Square.wf.I",
                "Q": "q3.xy.y180_Square.wf.Q",
            },
        },
        "q3.xy.y90_Square.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q3.xy.y90_Square.wf.I",
                "Q": "q3.xy.y90_Square.wf.Q",
            },
        },
        "q3.xy.-y90_Square.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q3.xy.-y90_Square.wf.I",
                "Q": "q3.xy.-y90_Square.wf.Q",
            },
        },
        "q3.xy.saturation.pulse": {
            "operation": "control",
            "length": 40000,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q3.xy.saturation.wf.I",
                "Q": "q3.xy.saturation.wf.Q",
            },
        },
        "q3.xy.cr_q2_q3_Square.pulse": {
            "operation": "control",
            "length": 100,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q3.xy.cr_q2_q3_Square.wf.I",
                "Q": "q3.xy.cr_q2_q3_Square.wf.Q",
            },
        },
        "q3.xy_detuned.zz_q2_q3_Square.pulse": {
            "operation": "control",
            "length": 100,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q3.xy_detuned.zz_q2_q3_Square.wf.I",
                "Q": "q3.xy_detuned.zz_q2_q3_Square.wf.Q",
            },
        },
        "q3.resonator.readout.pulse": {
            "operation": "measurement",
            "length": 2000,
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
            "length": 100,
            "waveforms": {
                "I": "q3.resonator.const.wf.I",
                "Q": "q3.resonator.const.wf.Q",
            },
        },
        "q4.xy.x180_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q4.xy.x180_DragCosine.wf.I",
                "Q": "q4.xy.x180_DragCosine.wf.Q",
            },
        },
        "q4.xy.x90_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q4.xy.x90_DragCosine.wf.I",
                "Q": "q4.xy.x90_DragCosine.wf.Q",
            },
        },
        "q4.xy.-x90_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q4.xy.-x90_DragCosine.wf.I",
                "Q": "q4.xy.-x90_DragCosine.wf.Q",
            },
        },
        "q4.xy.y180_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q4.xy.y180_DragCosine.wf.I",
                "Q": "q4.xy.y180_DragCosine.wf.Q",
            },
        },
        "q4.xy.y90_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q4.xy.y90_DragCosine.wf.I",
                "Q": "q4.xy.y90_DragCosine.wf.Q",
            },
        },
        "q4.xy.-y90_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q4.xy.-y90_DragCosine.wf.I",
                "Q": "q4.xy.-y90_DragCosine.wf.Q",
            },
        },
        "q4.xy.x180_Square.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q4.xy.x180_Square.wf.I",
                "Q": "q4.xy.x180_Square.wf.Q",
            },
        },
        "q4.xy.x90_Square.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q4.xy.x90_Square.wf.I",
                "Q": "q4.xy.x90_Square.wf.Q",
            },
        },
        "q4.xy.-x90_Square.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q4.xy.-x90_Square.wf.I",
                "Q": "q4.xy.-x90_Square.wf.Q",
            },
        },
        "q4.xy.y180_Square.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q4.xy.y180_Square.wf.I",
                "Q": "q4.xy.y180_Square.wf.Q",
            },
        },
        "q4.xy.y90_Square.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q4.xy.y90_Square.wf.I",
                "Q": "q4.xy.y90_Square.wf.Q",
            },
        },
        "q4.xy.-y90_Square.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q4.xy.-y90_Square.wf.I",
                "Q": "q4.xy.-y90_Square.wf.Q",
            },
        },
        "q4.xy.saturation.pulse": {
            "operation": "control",
            "length": 40000,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q4.xy.saturation.wf.I",
                "Q": "q4.xy.saturation.wf.Q",
            },
        },
        "q4.xy.cr_q3_q4_Square.pulse": {
            "operation": "control",
            "length": 100,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q4.xy.cr_q3_q4_Square.wf.I",
                "Q": "q4.xy.cr_q3_q4_Square.wf.Q",
            },
        },
        "q4.xy_detuned.zz_q3_q4_Square.pulse": {
            "operation": "control",
            "length": 100,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q4.xy_detuned.zz_q3_q4_Square.wf.I",
                "Q": "q4.xy_detuned.zz_q3_q4_Square.wf.Q",
            },
        },
        "q4.resonator.readout.pulse": {
            "operation": "measurement",
            "length": 2000,
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
            "length": 100,
            "waveforms": {
                "I": "q4.resonator.const.wf.I",
                "Q": "q4.resonator.const.wf.Q",
            },
        },
        "q5.xy.x180_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q5.xy.x180_DragCosine.wf.I",
                "Q": "q5.xy.x180_DragCosine.wf.Q",
            },
        },
        "q5.xy.x90_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q5.xy.x90_DragCosine.wf.I",
                "Q": "q5.xy.x90_DragCosine.wf.Q",
            },
        },
        "q5.xy.-x90_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q5.xy.-x90_DragCosine.wf.I",
                "Q": "q5.xy.-x90_DragCosine.wf.Q",
            },
        },
        "q5.xy.y180_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q5.xy.y180_DragCosine.wf.I",
                "Q": "q5.xy.y180_DragCosine.wf.Q",
            },
        },
        "q5.xy.y90_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q5.xy.y90_DragCosine.wf.I",
                "Q": "q5.xy.y90_DragCosine.wf.Q",
            },
        },
        "q5.xy.-y90_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q5.xy.-y90_DragCosine.wf.I",
                "Q": "q5.xy.-y90_DragCosine.wf.Q",
            },
        },
        "q5.xy.x180_Square.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q5.xy.x180_Square.wf.I",
                "Q": "q5.xy.x180_Square.wf.Q",
            },
        },
        "q5.xy.x90_Square.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q5.xy.x90_Square.wf.I",
                "Q": "q5.xy.x90_Square.wf.Q",
            },
        },
        "q5.xy.-x90_Square.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q5.xy.-x90_Square.wf.I",
                "Q": "q5.xy.-x90_Square.wf.Q",
            },
        },
        "q5.xy.y180_Square.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q5.xy.y180_Square.wf.I",
                "Q": "q5.xy.y180_Square.wf.Q",
            },
        },
        "q5.xy.y90_Square.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q5.xy.y90_Square.wf.I",
                "Q": "q5.xy.y90_Square.wf.Q",
            },
        },
        "q5.xy.-y90_Square.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q5.xy.-y90_Square.wf.I",
                "Q": "q5.xy.-y90_Square.wf.Q",
            },
        },
        "q5.xy.saturation.pulse": {
            "operation": "control",
            "length": 40000,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q5.xy.saturation.wf.I",
                "Q": "q5.xy.saturation.wf.Q",
            },
        },
        "q5.xy.cr_q4_q5_Square.pulse": {
            "operation": "control",
            "length": 100,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q5.xy.cr_q4_q5_Square.wf.I",
                "Q": "q5.xy.cr_q4_q5_Square.wf.Q",
            },
        },
        "q5.xy_detuned.zz_q4_q5_Square.pulse": {
            "operation": "control",
            "length": 100,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q5.xy_detuned.zz_q4_q5_Square.wf.I",
                "Q": "q5.xy_detuned.zz_q4_q5_Square.wf.Q",
            },
        },
        "q5.resonator.readout.pulse": {
            "operation": "measurement",
            "length": 2000,
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
            "length": 100,
            "waveforms": {
                "I": "q5.resonator.const.wf.I",
                "Q": "q5.resonator.const.wf.Q",
            },
        },
        "q6.xy.x180_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q6.xy.x180_DragCosine.wf.I",
                "Q": "q6.xy.x180_DragCosine.wf.Q",
            },
        },
        "q6.xy.x90_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q6.xy.x90_DragCosine.wf.I",
                "Q": "q6.xy.x90_DragCosine.wf.Q",
            },
        },
        "q6.xy.-x90_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q6.xy.-x90_DragCosine.wf.I",
                "Q": "q6.xy.-x90_DragCosine.wf.Q",
            },
        },
        "q6.xy.y180_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q6.xy.y180_DragCosine.wf.I",
                "Q": "q6.xy.y180_DragCosine.wf.Q",
            },
        },
        "q6.xy.y90_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q6.xy.y90_DragCosine.wf.I",
                "Q": "q6.xy.y90_DragCosine.wf.Q",
            },
        },
        "q6.xy.-y90_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q6.xy.-y90_DragCosine.wf.I",
                "Q": "q6.xy.-y90_DragCosine.wf.Q",
            },
        },
        "q6.xy.x180_Square.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q6.xy.x180_Square.wf.I",
                "Q": "q6.xy.x180_Square.wf.Q",
            },
        },
        "q6.xy.x90_Square.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q6.xy.x90_Square.wf.I",
                "Q": "q6.xy.x90_Square.wf.Q",
            },
        },
        "q6.xy.-x90_Square.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q6.xy.-x90_Square.wf.I",
                "Q": "q6.xy.-x90_Square.wf.Q",
            },
        },
        "q6.xy.y180_Square.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q6.xy.y180_Square.wf.I",
                "Q": "q6.xy.y180_Square.wf.Q",
            },
        },
        "q6.xy.y90_Square.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q6.xy.y90_Square.wf.I",
                "Q": "q6.xy.y90_Square.wf.Q",
            },
        },
        "q6.xy.-y90_Square.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q6.xy.-y90_Square.wf.I",
                "Q": "q6.xy.-y90_Square.wf.Q",
            },
        },
        "q6.xy.saturation.pulse": {
            "operation": "control",
            "length": 40000,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q6.xy.saturation.wf.I",
                "Q": "q6.xy.saturation.wf.Q",
            },
        },
        "q6.xy.cr_q5_q6_Square.pulse": {
            "operation": "control",
            "length": 100,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q6.xy.cr_q5_q6_Square.wf.I",
                "Q": "q6.xy.cr_q5_q6_Square.wf.Q",
            },
        },
        "q6.xy_detuned.zz_q5_q6_Square.pulse": {
            "operation": "control",
            "length": 100,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q6.xy_detuned.zz_q5_q6_Square.wf.I",
                "Q": "q6.xy_detuned.zz_q5_q6_Square.wf.Q",
            },
        },
        "q6.resonator.readout.pulse": {
            "operation": "measurement",
            "length": 2000,
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
            "length": 100,
            "waveforms": {
                "I": "q6.resonator.const.wf.I",
                "Q": "q6.resonator.const.wf.Q",
            },
        },
        "q7.xy.x180_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q7.xy.x180_DragCosine.wf.I",
                "Q": "q7.xy.x180_DragCosine.wf.Q",
            },
        },
        "q7.xy.x90_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q7.xy.x90_DragCosine.wf.I",
                "Q": "q7.xy.x90_DragCosine.wf.Q",
            },
        },
        "q7.xy.-x90_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q7.xy.-x90_DragCosine.wf.I",
                "Q": "q7.xy.-x90_DragCosine.wf.Q",
            },
        },
        "q7.xy.y180_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q7.xy.y180_DragCosine.wf.I",
                "Q": "q7.xy.y180_DragCosine.wf.Q",
            },
        },
        "q7.xy.y90_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q7.xy.y90_DragCosine.wf.I",
                "Q": "q7.xy.y90_DragCosine.wf.Q",
            },
        },
        "q7.xy.-y90_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q7.xy.-y90_DragCosine.wf.I",
                "Q": "q7.xy.-y90_DragCosine.wf.Q",
            },
        },
        "q7.xy.x180_Square.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q7.xy.x180_Square.wf.I",
                "Q": "q7.xy.x180_Square.wf.Q",
            },
        },
        "q7.xy.x90_Square.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q7.xy.x90_Square.wf.I",
                "Q": "q7.xy.x90_Square.wf.Q",
            },
        },
        "q7.xy.-x90_Square.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q7.xy.-x90_Square.wf.I",
                "Q": "q7.xy.-x90_Square.wf.Q",
            },
        },
        "q7.xy.y180_Square.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q7.xy.y180_Square.wf.I",
                "Q": "q7.xy.y180_Square.wf.Q",
            },
        },
        "q7.xy.y90_Square.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q7.xy.y90_Square.wf.I",
                "Q": "q7.xy.y90_Square.wf.Q",
            },
        },
        "q7.xy.-y90_Square.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q7.xy.-y90_Square.wf.I",
                "Q": "q7.xy.-y90_Square.wf.Q",
            },
        },
        "q7.xy.saturation.pulse": {
            "operation": "control",
            "length": 40000,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q7.xy.saturation.wf.I",
                "Q": "q7.xy.saturation.wf.Q",
            },
        },
        "q7.xy.cr_q6_q7_Square.pulse": {
            "operation": "control",
            "length": 100,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q7.xy.cr_q6_q7_Square.wf.I",
                "Q": "q7.xy.cr_q6_q7_Square.wf.Q",
            },
        },
        "q7.xy_detuned.zz_q6_q7_Square.pulse": {
            "operation": "control",
            "length": 100,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q7.xy_detuned.zz_q6_q7_Square.wf.I",
                "Q": "q7.xy_detuned.zz_q6_q7_Square.wf.Q",
            },
        },
        "q7.resonator.readout.pulse": {
            "operation": "measurement",
            "length": 2000,
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
            "length": 100,
            "waveforms": {
                "I": "q7.resonator.const.wf.I",
                "Q": "q7.resonator.const.wf.Q",
            },
        },
        "q8.xy.x180_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q8.xy.x180_DragCosine.wf.I",
                "Q": "q8.xy.x180_DragCosine.wf.Q",
            },
        },
        "q8.xy.x90_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q8.xy.x90_DragCosine.wf.I",
                "Q": "q8.xy.x90_DragCosine.wf.Q",
            },
        },
        "q8.xy.-x90_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q8.xy.-x90_DragCosine.wf.I",
                "Q": "q8.xy.-x90_DragCosine.wf.Q",
            },
        },
        "q8.xy.y180_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q8.xy.y180_DragCosine.wf.I",
                "Q": "q8.xy.y180_DragCosine.wf.Q",
            },
        },
        "q8.xy.y90_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q8.xy.y90_DragCosine.wf.I",
                "Q": "q8.xy.y90_DragCosine.wf.Q",
            },
        },
        "q8.xy.-y90_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q8.xy.-y90_DragCosine.wf.I",
                "Q": "q8.xy.-y90_DragCosine.wf.Q",
            },
        },
        "q8.xy.x180_Square.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q8.xy.x180_Square.wf.I",
                "Q": "q8.xy.x180_Square.wf.Q",
            },
        },
        "q8.xy.x90_Square.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q8.xy.x90_Square.wf.I",
                "Q": "q8.xy.x90_Square.wf.Q",
            },
        },
        "q8.xy.-x90_Square.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q8.xy.-x90_Square.wf.I",
                "Q": "q8.xy.-x90_Square.wf.Q",
            },
        },
        "q8.xy.y180_Square.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q8.xy.y180_Square.wf.I",
                "Q": "q8.xy.y180_Square.wf.Q",
            },
        },
        "q8.xy.y90_Square.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q8.xy.y90_Square.wf.I",
                "Q": "q8.xy.y90_Square.wf.Q",
            },
        },
        "q8.xy.-y90_Square.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q8.xy.-y90_Square.wf.I",
                "Q": "q8.xy.-y90_Square.wf.Q",
            },
        },
        "q8.xy.saturation.pulse": {
            "operation": "control",
            "length": 40000,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q8.xy.saturation.wf.I",
                "Q": "q8.xy.saturation.wf.Q",
            },
        },
        "q8.xy.cr_q7_q8_Square.pulse": {
            "operation": "control",
            "length": 100,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q8.xy.cr_q7_q8_Square.wf.I",
                "Q": "q8.xy.cr_q7_q8_Square.wf.Q",
            },
        },
        "q8.xy_detuned.zz_q7_q8_Square.pulse": {
            "operation": "control",
            "length": 100,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q8.xy_detuned.zz_q7_q8_Square.wf.I",
                "Q": "q8.xy_detuned.zz_q7_q8_Square.wf.Q",
            },
        },
        "q8.resonator.readout.pulse": {
            "operation": "measurement",
            "length": 2000,
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
            "length": 100,
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
        "zz_q1_q2.square.pulse": {
            "operation": "control",
            "length": 100,
            "waveforms": {
                "I": "zz_q1_q2.square.wf.I",
                "Q": "zz_q1_q2.square.wf.Q",
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
        "zz_q2_q3.square.pulse": {
            "operation": "control",
            "length": 100,
            "waveforms": {
                "I": "zz_q2_q3.square.wf.I",
                "Q": "zz_q2_q3.square.wf.Q",
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
        "zz_q3_q4.square.pulse": {
            "operation": "control",
            "length": 100,
            "waveforms": {
                "I": "zz_q3_q4.square.wf.I",
                "Q": "zz_q3_q4.square.wf.Q",
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
        "zz_q4_q5.square.pulse": {
            "operation": "control",
            "length": 100,
            "waveforms": {
                "I": "zz_q4_q5.square.wf.I",
                "Q": "zz_q4_q5.square.wf.Q",
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
        "zz_q5_q6.square.pulse": {
            "operation": "control",
            "length": 100,
            "waveforms": {
                "I": "zz_q5_q6.square.wf.I",
                "Q": "zz_q5_q6.square.wf.Q",
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
        "zz_q6_q7.square.pulse": {
            "operation": "control",
            "length": 100,
            "waveforms": {
                "I": "zz_q6_q7.square.wf.I",
                "Q": "zz_q6_q7.square.wf.Q",
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
        "zz_q7_q8.square.pulse": {
            "operation": "control",
            "length": 100,
            "waveforms": {
                "I": "zz_q7_q8.square.wf.I",
                "Q": "zz_q7_q8.square.wf.Q",
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
        "zz_q8_q1.square.pulse": {
            "operation": "control",
            "length": 100,
            "waveforms": {
                "I": "zz_q8_q1.square.wf.I",
                "Q": "zz_q8_q1.square.wf.Q",
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
        "q1.xy.x180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0009587121065884679, 0.0038100182863815214, 0.008480071207044722, 0.014847918950998806, 0.022748637606551846, 0.03197760271058151, 0.04229578891464574, 0.05343596061595301, 0.06510959321910238, 0.07701434577154927, 0.08884189143546399, 0.10028590299087507, 0.11104998654975992, 0.12085535800205625, 0.12944806337767426, 0.13660555612092581, 0.14214246092941862, 0.14591537487701495] + [0.14782658147429253] * 2 + [0.14591537487701495, 0.14214246092941862, 0.13660555612092584, 0.12944806337767428, 0.12085535800205625, 0.11104998654975987, 0.1002859029908751, 0.08884189143546402, 0.07701434577154927, 0.06510959321910244, 0.05343596061595306, 0.04229578891464577, 0.03197760271058154, 0.022748637606551853, 0.014847918950998806, 0.008480071207044713, 0.003810018286381513, 0.0009587121065884679, 0.0],
        },
        "q1.xy.x180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
        },
        "q1.xy.x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.00047935605329423394, 0.0019050091431907607, 0.004240035603522361, 0.007423959475499403, 0.011374318803275923, 0.015988801355290756, 0.02114789445732287, 0.026717980307976504, 0.03255479660955119, 0.03850717288577463, 0.044420945717731995, 0.050142951495437536, 0.05552499327487996, 0.06042767900102813, 0.06472403168883713, 0.06830277806046291, 0.07107123046470931, 0.07295768743850747] + [0.07391329073714627] * 2 + [0.07295768743850747, 0.07107123046470931, 0.06830277806046292, 0.06472403168883714, 0.06042767900102813, 0.05552499327487993, 0.05014295149543755, 0.04442094571773201, 0.03850717288577463, 0.03255479660955122, 0.02671798030797653, 0.021147894457322885, 0.01598880135529077, 0.011374318803275926, 0.007423959475499403, 0.004240035603522357, 0.0019050091431907566, 0.00047935605329423394, 0.0],
        },
        "q1.xy.x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
        },
        "q1.xy.-x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -0.00047935605329423394, -0.0019050091431907607, -0.004240035603522361, -0.007423959475499403, -0.011374318803275923, -0.015988801355290756, -0.02114789445732287, -0.026717980307976504, -0.03255479660955119, -0.03850717288577463, -0.044420945717731995, -0.050142951495437536, -0.05552499327487996, -0.06042767900102813, -0.06472403168883713, -0.06830277806046291, -0.07107123046470931, -0.07295768743850747] + [-0.07391329073714627] * 2 + [-0.07295768743850747, -0.07107123046470931, -0.06830277806046292, -0.06472403168883714, -0.06042767900102813, -0.05552499327487993, -0.05014295149543755, -0.04442094571773201, -0.03850717288577463, -0.03255479660955122, -0.02671798030797653, -0.021147894457322885, -0.01598880135529077, -0.011374318803275926, -0.007423959475499403, -0.004240035603522357, -0.0019050091431907566, -0.00047935605329423394, 0.0],
        },
        "q1.xy.-x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 5.870418563186916e-20, 2.332963349555007e-19, 5.192546030124476e-19, 9.091728208670006e-19, 1.3929523114913413e-18, 1.9580634401959688e-18, 2.5898701255866507e-18, 3.272008906384544e-18, 3.986812746477997e-18, 4.715768601877765e-18, 5.439996898831882e-18, 6.140740504868857e-18, 6.799850528676006e-18, 7.400256366851283e-18, 7.926407823564624e-18, 8.364677852461796e-18, 8.703715490007011e-18, 8.934739839476124e-18] + [9.051767491569389e-18] * 2 + [8.934739839476124e-18, 8.703715490007011e-18, 8.364677852461798e-18, 7.926407823564626e-18, 7.400256366851283e-18, 6.799850528676002e-18, 6.140740504868858e-18, 5.439996898831883e-18, 4.715768601877765e-18, 3.986812746478001e-18, 3.272008906384547e-18, 2.5898701255866523e-18, 1.9580634401959703e-18, 1.3929523114913417e-18, 9.091728208670006e-19, 5.19254603012447e-19, 2.332963349555002e-19, 5.870418563186916e-20, 0.0],
        },
        "q1.xy.y180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 5.870418563186916e-20, 2.332963349555007e-19, 5.192546030124476e-19, 9.091728208670006e-19, 1.3929523114913413e-18, 1.9580634401959688e-18, 2.5898701255866507e-18, 3.272008906384544e-18, 3.986812746477997e-18, 4.715768601877765e-18, 5.439996898831882e-18, 6.140740504868857e-18, 6.799850528676006e-18, 7.400256366851283e-18, 7.926407823564624e-18, 8.364677852461796e-18, 8.703715490007011e-18, 8.934739839476124e-18] + [9.051767491569389e-18] * 2 + [8.934739839476124e-18, 8.703715490007011e-18, 8.364677852461798e-18, 7.926407823564626e-18, 7.400256366851283e-18, 6.799850528676002e-18, 6.140740504868858e-18, 5.439996898831883e-18, 4.715768601877765e-18, 3.986812746478001e-18, 3.272008906384547e-18, 2.5898701255866523e-18, 1.9580634401959703e-18, 1.3929523114913417e-18, 9.091728208670006e-19, 5.19254603012447e-19, 2.332963349555002e-19, 5.870418563186916e-20, 0.0],
        },
        "q1.xy.y180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0009587121065884679, 0.0038100182863815214, 0.008480071207044722, 0.014847918950998806, 0.022748637606551846, 0.03197760271058151, 0.04229578891464574, 0.05343596061595301, 0.06510959321910238, 0.07701434577154927, 0.08884189143546399, 0.10028590299087507, 0.11104998654975992, 0.12085535800205625, 0.12944806337767426, 0.13660555612092581, 0.14214246092941862, 0.14591537487701495] + [0.14782658147429253] * 2 + [0.14591537487701495, 0.14214246092941862, 0.13660555612092584, 0.12944806337767428, 0.12085535800205625, 0.11104998654975987, 0.1002859029908751, 0.08884189143546402, 0.07701434577154927, 0.06510959321910244, 0.05343596061595306, 0.04229578891464577, 0.03197760271058154, 0.022748637606551853, 0.014847918950998806, 0.008480071207044713, 0.003810018286381513, 0.0009587121065884679, 0.0],
        },
        "q1.xy.y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 2.935209281593458e-20, 1.1664816747775036e-19, 2.596273015062238e-19, 4.545864104335003e-19, 6.964761557456706e-19, 9.790317200979844e-19, 1.2949350627933254e-18, 1.636004453192272e-18, 1.9934063732389985e-18, 2.3578843009388826e-18, 2.719998449415941e-18, 3.0703702524344283e-18, 3.399925264338003e-18, 3.700128183425641e-18, 3.963203911782312e-18, 4.182338926230898e-18, 4.3518577450035054e-18, 4.467369919738062e-18] + [4.5258837457846946e-18] * 2 + [4.467369919738062e-18, 4.3518577450035054e-18, 4.182338926230899e-18, 3.963203911782313e-18, 3.700128183425641e-18, 3.399925264338001e-18, 3.070370252434429e-18, 2.7199984494159416e-18, 2.3578843009388826e-18, 1.9934063732390004e-18, 1.6360044531922735e-18, 1.2949350627933261e-18, 9.790317200979852e-19, 6.964761557456708e-19, 4.545864104335003e-19, 2.596273015062235e-19, 1.166481674777501e-19, 2.935209281593458e-20, 0.0],
        },
        "q1.xy.y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.00047935605329423394, 0.0019050091431907607, 0.004240035603522361, 0.007423959475499403, 0.011374318803275923, 0.015988801355290756, 0.02114789445732287, 0.026717980307976504, 0.03255479660955119, 0.03850717288577463, 0.044420945717731995, 0.050142951495437536, 0.05552499327487996, 0.06042767900102813, 0.06472403168883713, 0.06830277806046291, 0.07107123046470931, 0.07295768743850747] + [0.07391329073714627] * 2 + [0.07295768743850747, 0.07107123046470931, 0.06830277806046292, 0.06472403168883714, 0.06042767900102813, 0.05552499327487993, 0.05014295149543755, 0.04442094571773201, 0.03850717288577463, 0.03255479660955122, 0.02671798030797653, 0.021147894457322885, 0.01598880135529077, 0.011374318803275926, 0.007423959475499403, 0.004240035603522357, 0.0019050091431907566, 0.00047935605329423394, 0.0],
        },
        "q1.xy.-y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 2.935209281593458e-20, 1.1664816747775036e-19, 2.596273015062238e-19, 4.545864104335003e-19, 6.964761557456706e-19, 9.790317200979844e-19, 1.2949350627933254e-18, 1.636004453192272e-18, 1.9934063732389985e-18, 2.3578843009388826e-18, 2.719998449415941e-18, 3.0703702524344283e-18, 3.399925264338003e-18, 3.700128183425641e-18, 3.963203911782312e-18, 4.182338926230898e-18, 4.3518577450035054e-18, 4.467369919738062e-18] + [4.5258837457846946e-18] * 2 + [4.467369919738062e-18, 4.3518577450035054e-18, 4.182338926230899e-18, 3.963203911782313e-18, 3.700128183425641e-18, 3.399925264338001e-18, 3.070370252434429e-18, 2.7199984494159416e-18, 2.3578843009388826e-18, 1.9934063732390004e-18, 1.6360044531922735e-18, 1.2949350627933261e-18, 9.790317200979852e-19, 6.964761557456708e-19, 4.545864104335003e-19, 2.596273015062235e-19, 1.166481674777501e-19, 2.935209281593458e-20, 0.0],
        },
        "q1.xy.-y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.00047935605329423394, -0.0019050091431907607, -0.004240035603522361, -0.007423959475499403, -0.011374318803275923, -0.015988801355290756, -0.02114789445732287, -0.026717980307976504, -0.03255479660955119, -0.03850717288577463, -0.044420945717731995, -0.050142951495437536, -0.05552499327487996, -0.06042767900102813, -0.06472403168883713, -0.06830277806046291, -0.07107123046470931, -0.07295768743850747] + [-0.07391329073714627] * 2 + [-0.07295768743850747, -0.07107123046470931, -0.06830277806046292, -0.06472403168883714, -0.06042767900102813, -0.05552499327487993, -0.05014295149543755, -0.04442094571773201, -0.03850717288577463, -0.03255479660955122, -0.02671798030797653, -0.021147894457322885, -0.01598880135529077, -0.011374318803275926, -0.007423959475499403, -0.004240035603522357, -0.0019050091431907566, -0.00047935605329423394, 0.0],
        },
        "q1.xy.x180_Square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "q1.xy.x180_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q1.xy.x90_Square.wf.I": {
            "type": "constant",
            "sample": 0.05,
        },
        "q1.xy.x90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q1.xy.-x90_Square.wf.I": {
            "type": "constant",
            "sample": -0.125,
        },
        "q1.xy.-x90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q1.xy.y180_Square.wf.I": {
            "type": "constant",
            "sample": -0.11201840403229253,
        },
        "q1.xy.y180_Square.wf.Q": {
            "type": "constant",
            "sample": 0.22349916590013946,
        },
        "q1.xy.y90_Square.wf.I": {
            "type": "constant",
            "sample": -0.056009202016146266,
        },
        "q1.xy.y90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.11174958295006973,
        },
        "q1.xy.-y90_Square.wf.I": {
            "type": "constant",
            "sample": 0.056009202016146266,
        },
        "q1.xy.-y90_Square.wf.Q": {
            "type": "constant",
            "sample": -0.11174958295006973,
        },
        "q1.xy.saturation.wf.I": {
            "type": "constant",
            "sample": 0.06342390975458759,
        },
        "q1.xy.saturation.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q1.xy.cr_q8_q1_Square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "q1.xy.cr_q8_q1_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q1.xy_detuned.zz_q8_q1_Square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "q1.xy_detuned.zz_q8_q1_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q1.resonator.readout.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "q1.resonator.readout.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q1.resonator.const.wf.I": {
            "type": "constant",
            "sample": 0.125,
        },
        "q1.resonator.const.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q2.xy.x180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0007510084282569763, 0.00298458298922262, 0.006642875275010638, 0.011631137437031628, 0.017820176105502773, 0.025049698429863057, 0.03313246357940488, 0.04185913218243622, 0.05100368810604664, 0.06032929215522879, 0.06959441608362318, 0.07855909804823011, 0.08699115749509692, 0.09467220851370672, 0.10140331591734797, 0.10701014755995437, 0.11134748944711555, 0.11430300670225482, 0.11580015298092586, 0.11580015298092587, 0.11430300670225482, 0.11134748944711556, 0.1070101475599544, 0.101403315917348, 0.09467220851370672, 0.08699115749509688, 0.07855909804823014, 0.06959441608362321, 0.06032929215522879, 0.051003688106046684, 0.041859132182436254, 0.0331324635794049, 0.025049698429863078, 0.01782017610550278, 0.011631137437031628, 0.006642875275010631, 0.0029845829892226135, 0.0007510084282569763, 0.0],
        },
        "q2.xy.x180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
        },
        "q2.xy.x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.00037550421412848814, 0.00149229149461131, 0.003321437637505319, 0.005815568718515814, 0.008910088052751387, 0.012524849214931529, 0.01656623178970244, 0.02092956609121811, 0.02550184405302332, 0.030164646077614394, 0.03479720804181159, 0.039279549024115054, 0.04349557874754846, 0.04733610425685336, 0.050701657958673985, 0.05350507377997719, 0.05567374472355777, 0.05715150335112741, 0.05790007649046293, 0.057900076490462936, 0.05715150335112741, 0.05567374472355778, 0.0535050737799772, 0.050701657958674, 0.04733610425685336, 0.04349557874754844, 0.03927954902411507, 0.034797208041811606, 0.030164646077614394, 0.025501844053023342, 0.020929566091218127, 0.01656623178970245, 0.012524849214931539, 0.00891008805275139, 0.005815568718515814, 0.0033214376375053155, 0.0014922914946113067, 0.00037550421412848814, 0.0],
        },
        "q2.xy.x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
        },
        "q2.xy.-x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -0.00037550421412848814, -0.00149229149461131, -0.003321437637505319, -0.005815568718515814, -0.008910088052751387, -0.012524849214931529, -0.01656623178970244, -0.02092956609121811, -0.02550184405302332, -0.030164646077614394, -0.03479720804181159, -0.039279549024115054, -0.04349557874754846, -0.04733610425685336, -0.050701657958673985, -0.05350507377997719, -0.05567374472355777, -0.05715150335112741, -0.05790007649046293, -0.057900076490462936, -0.05715150335112741, -0.05567374472355778, -0.0535050737799772, -0.050701657958674, -0.04733610425685336, -0.04349557874754844, -0.03927954902411507, -0.034797208041811606, -0.030164646077614394, -0.025501844053023342, -0.020929566091218127, -0.01656623178970245, -0.012524849214931539, -0.00891008805275139, -0.005815568718515814, -0.0033214376375053155, -0.0014922914946113067, -0.00037550421412848814, 0.0],
        },
        "q2.xy.-x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 4.5986003389879534e-20, 1.8275300022705605e-19, 4.067587971338436e-19, 7.122017616351866e-19, 1.091171081392306e-18, 1.5338516500869136e-18, 2.028778273519222e-18, 2.5631326121153237e-18, 3.1230751691889973e-18, 3.694103726636323e-18, 4.261428944766911e-18, 4.8103573984334044e-18, 5.326672129024686e-18, 5.797000856226087e-18, 6.209162313055402e-18, 6.5524817342792036e-18, 6.818067327225187e-18, 6.999040564541742e-18, 7.090714334443233e-18, 7.090714334443235e-18, 6.999040564541742e-18, 6.818067327225188e-18, 6.552481734279205e-18, 6.2091623130554036e-18, 5.797000856226087e-18, 5.326672129024684e-18, 4.810357398433406e-18, 4.261428944766912e-18, 3.694103726636323e-18, 3.123075169189e-18, 2.563132612115326e-18, 2.0287782735192232e-18, 1.533851650086915e-18, 1.0911710813923064e-18, 7.122017616351866e-19, 4.0675879713384314e-19, 1.8275300022705566e-19, 4.5986003389879534e-20, 0.0],
        },
        "q2.xy.y180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 4.5986003389879534e-20, 1.8275300022705605e-19, 4.067587971338436e-19, 7.122017616351866e-19, 1.091171081392306e-18, 1.5338516500869136e-18, 2.028778273519222e-18, 2.5631326121153237e-18, 3.1230751691889973e-18, 3.694103726636323e-18, 4.261428944766911e-18, 4.8103573984334044e-18, 5.326672129024686e-18, 5.797000856226087e-18, 6.209162313055402e-18, 6.5524817342792036e-18, 6.818067327225187e-18, 6.999040564541742e-18, 7.090714334443233e-18, 7.090714334443235e-18, 6.999040564541742e-18, 6.818067327225188e-18, 6.552481734279205e-18, 6.2091623130554036e-18, 5.797000856226087e-18, 5.326672129024684e-18, 4.810357398433406e-18, 4.261428944766912e-18, 3.694103726636323e-18, 3.123075169189e-18, 2.563132612115326e-18, 2.0287782735192232e-18, 1.533851650086915e-18, 1.0911710813923064e-18, 7.122017616351866e-19, 4.0675879713384314e-19, 1.8275300022705566e-19, 4.5986003389879534e-20, 0.0],
        },
        "q2.xy.y180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0007510084282569763, 0.00298458298922262, 0.006642875275010638, 0.011631137437031628, 0.017820176105502773, 0.025049698429863057, 0.03313246357940488, 0.04185913218243622, 0.05100368810604664, 0.06032929215522879, 0.06959441608362318, 0.07855909804823011, 0.08699115749509692, 0.09467220851370672, 0.10140331591734797, 0.10701014755995437, 0.11134748944711555, 0.11430300670225482, 0.11580015298092586, 0.11580015298092587, 0.11430300670225482, 0.11134748944711556, 0.1070101475599544, 0.101403315917348, 0.09467220851370672, 0.08699115749509688, 0.07855909804823014, 0.06959441608362321, 0.06032929215522879, 0.051003688106046684, 0.041859132182436254, 0.0331324635794049, 0.025049698429863078, 0.01782017610550278, 0.011631137437031628, 0.006642875275010631, 0.0029845829892226135, 0.0007510084282569763, 0.0],
        },
        "q2.xy.y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 2.2993001694939767e-20, 9.137650011352802e-20, 2.033793985669218e-19, 3.561008808175933e-19, 5.45585540696153e-19, 7.669258250434568e-19, 1.014389136759611e-18, 1.2815663060576618e-18, 1.5615375845944987e-18, 1.8470518633181615e-18, 2.1307144723834554e-18, 2.4051786992167022e-18, 2.663336064512343e-18, 2.8985004281130434e-18, 3.104581156527701e-18, 3.2762408671396018e-18, 3.4090336636125936e-18, 3.499520282270871e-18, 3.545357167221617e-18, 3.5453571672216175e-18, 3.499520282270871e-18, 3.409033663612594e-18, 3.2762408671396026e-18, 3.1045811565277018e-18, 2.8985004281130434e-18, 2.663336064512342e-18, 2.405178699216703e-18, 2.130714472383456e-18, 1.8470518633181615e-18, 1.5615375845945e-18, 1.281566306057663e-18, 1.0143891367596116e-18, 7.669258250434575e-19, 5.455855406961532e-19, 3.561008808175933e-19, 2.0337939856692157e-19, 9.137650011352783e-20, 2.2993001694939767e-20, 0.0],
        },
        "q2.xy.y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.00037550421412848814, 0.00149229149461131, 0.003321437637505319, 0.005815568718515814, 0.008910088052751387, 0.012524849214931529, 0.01656623178970244, 0.02092956609121811, 0.02550184405302332, 0.030164646077614394, 0.03479720804181159, 0.039279549024115054, 0.04349557874754846, 0.04733610425685336, 0.050701657958673985, 0.05350507377997719, 0.05567374472355777, 0.05715150335112741, 0.05790007649046293, 0.057900076490462936, 0.05715150335112741, 0.05567374472355778, 0.0535050737799772, 0.050701657958674, 0.04733610425685336, 0.04349557874754844, 0.03927954902411507, 0.034797208041811606, 0.030164646077614394, 0.025501844053023342, 0.020929566091218127, 0.01656623178970245, 0.012524849214931539, 0.00891008805275139, 0.005815568718515814, 0.0033214376375053155, 0.0014922914946113067, 0.00037550421412848814, 0.0],
        },
        "q2.xy.-y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 2.2993001694939767e-20, 9.137650011352802e-20, 2.033793985669218e-19, 3.561008808175933e-19, 5.45585540696153e-19, 7.669258250434568e-19, 1.014389136759611e-18, 1.2815663060576618e-18, 1.5615375845944987e-18, 1.8470518633181615e-18, 2.1307144723834554e-18, 2.4051786992167022e-18, 2.663336064512343e-18, 2.8985004281130434e-18, 3.104581156527701e-18, 3.2762408671396018e-18, 3.4090336636125936e-18, 3.499520282270871e-18, 3.545357167221617e-18, 3.5453571672216175e-18, 3.499520282270871e-18, 3.409033663612594e-18, 3.2762408671396026e-18, 3.1045811565277018e-18, 2.8985004281130434e-18, 2.663336064512342e-18, 2.405178699216703e-18, 2.130714472383456e-18, 1.8470518633181615e-18, 1.5615375845945e-18, 1.281566306057663e-18, 1.0143891367596116e-18, 7.669258250434575e-19, 5.455855406961532e-19, 3.561008808175933e-19, 2.0337939856692157e-19, 9.137650011352783e-20, 2.2993001694939767e-20, 0.0],
        },
        "q2.xy.-y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.00037550421412848814, -0.00149229149461131, -0.003321437637505319, -0.005815568718515814, -0.008910088052751387, -0.012524849214931529, -0.01656623178970244, -0.02092956609121811, -0.02550184405302332, -0.030164646077614394, -0.03479720804181159, -0.039279549024115054, -0.04349557874754846, -0.04733610425685336, -0.050701657958673985, -0.05350507377997719, -0.05567374472355777, -0.05715150335112741, -0.05790007649046293, -0.057900076490462936, -0.05715150335112741, -0.05567374472355778, -0.0535050737799772, -0.050701657958674, -0.04733610425685336, -0.04349557874754844, -0.03927954902411507, -0.034797208041811606, -0.030164646077614394, -0.025501844053023342, -0.020929566091218127, -0.01656623178970245, -0.012524849214931539, -0.00891008805275139, -0.005815568718515814, -0.0033214376375053155, -0.0014922914946113067, -0.00037550421412848814, 0.0],
        },
        "q2.xy.x180_Square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "q2.xy.x180_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q2.xy.x90_Square.wf.I": {
            "type": "constant",
            "sample": 0.05,
        },
        "q2.xy.x90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q2.xy.-x90_Square.wf.I": {
            "type": "constant",
            "sample": -0.125,
        },
        "q2.xy.-x90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q2.xy.y180_Square.wf.I": {
            "type": "constant",
            "sample": -0.11201840403229253,
        },
        "q2.xy.y180_Square.wf.Q": {
            "type": "constant",
            "sample": 0.22349916590013946,
        },
        "q2.xy.y90_Square.wf.I": {
            "type": "constant",
            "sample": -0.056009202016146266,
        },
        "q2.xy.y90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.11174958295006973,
        },
        "q2.xy.-y90_Square.wf.I": {
            "type": "constant",
            "sample": 0.056009202016146266,
        },
        "q2.xy.-y90_Square.wf.Q": {
            "type": "constant",
            "sample": -0.11174958295006973,
        },
        "q2.xy.saturation.wf.I": {
            "type": "constant",
            "sample": 0.038831084391286984,
        },
        "q2.xy.saturation.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q2.xy.cr_q1_q2_Square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "q2.xy.cr_q1_q2_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q2.xy_detuned.zz_q1_q2_Square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "q2.xy_detuned.zz_q1_q2_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q2.resonator.readout.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "q2.resonator.readout.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q2.resonator.const.wf.I": {
            "type": "constant",
            "sample": 0.125,
        },
        "q2.resonator.const.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q3.xy.x180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0010815323883923203, 0.004298118432812735, 0.00956645024430564, 0.016750080796280722, 0.025662957830829294, 0.03607424251447538, 0.047714288042708726, 0.0602816233505826, 0.07345076105494051, 0.08688062740666926, 0.10022339592164317, 0.11313349590395828, 0.12527656254543598, 0.13633809679852132, 0.14603161073641596, 0.154106047439897, 0.1603522832396507, 0.16460854390946003, 0.16676459453368778, 0.1667645945336878, 0.16460854390946003, 0.1603522832396507, 0.15410604743989706, 0.146031610736416, 0.13633809679852132, 0.12527656254543593, 0.11313349590395833, 0.10022339592164321, 0.08688062740666926, 0.07345076105494058, 0.06028162335058265, 0.04771428804270877, 0.036074242514475406, 0.025662957830829305, 0.016750080796280722, 0.009566450244305632, 0.004298118432812727, 0.0010815323883923203, 0.0],
        },
        "q3.xy.x180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
        },
        "q3.xy.x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0005407661941961602, 0.0021490592164063677, 0.00478322512215282, 0.008375040398140361, 0.012831478915414647, 0.01803712125723769, 0.023857144021354363, 0.0301408116752913, 0.03672538052747026, 0.04344031370333463, 0.050111697960821586, 0.05656674795197914, 0.06263828127271799, 0.06816904839926066, 0.07301580536820798, 0.0770530237199485, 0.08017614161982535, 0.08230427195473002, 0.08338229726684389, 0.0833822972668439, 0.08230427195473002, 0.08017614161982535, 0.07705302371994853, 0.073015805368208, 0.06816904839926066, 0.06263828127271796, 0.05656674795197916, 0.050111697960821606, 0.04344031370333463, 0.03672538052747029, 0.030140811675291326, 0.023857144021354384, 0.018037121257237703, 0.012831478915414652, 0.008375040398140361, 0.004783225122152816, 0.0021490592164063634, 0.0005407661941961602, 0.0],
        },
        "q3.xy.x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
        },
        "q3.xy.-x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -0.0005407661941961602, -0.0021490592164063677, -0.00478322512215282, -0.008375040398140361, -0.012831478915414647, -0.01803712125723769, -0.023857144021354363, -0.0301408116752913, -0.03672538052747026, -0.04344031370333463, -0.050111697960821586, -0.05656674795197914, -0.06263828127271799, -0.06816904839926066, -0.07301580536820798, -0.0770530237199485, -0.08017614161982535, -0.08230427195473002, -0.08338229726684389, -0.0833822972668439, -0.08230427195473002, -0.08017614161982535, -0.07705302371994853, -0.073015805368208, -0.06816904839926066, -0.06263828127271796, -0.05656674795197916, -0.050111697960821606, -0.04344031370333463, -0.03672538052747029, -0.030140811675291326, -0.023857144021354384, -0.018037121257237703, -0.012831478915414652, -0.008375040398140361, -0.004783225122152816, -0.0021490592164063634, -0.0005407661941961602, 0.0],
        },
        "q3.xy.-x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 6.622475888094236e-20, 2.631838490550177e-19, 5.857761335445659e-19, 1.0256466416312368e-18, 1.57140295820893e-18, 2.208910281350882e-18, 2.9216575062549035e-18, 3.691184854184866e-18, 4.497561971043498e-18, 5.319904113074566e-18, 6.13691305075591e-18, 6.927428681756635e-18, 7.670977066472568e-18, 8.348300692307557e-18, 8.941857233134203e-18, 9.436273886326002e-18, 9.8187455202704e-18, 1.0079366320551338e-17, 1.0211386345339346e-17, 1.0211386345339349e-17, 1.0079366320551338e-17, 9.8187455202704e-18, 9.436273886326005e-18, 8.941857233134205e-18, 8.348300692307557e-18, 7.670977066472565e-18, 6.927428681756638e-18, 6.136913050755913e-18, 5.319904113074566e-18, 4.497561971043503e-18, 3.691184854184869e-18, 2.9216575062549062e-18, 2.2089102813508838e-18, 1.5714029582089305e-18, 1.0256466416312368e-18, 5.857761335445654e-19, 2.631838490550172e-19, 6.622475888094236e-20, 0.0],
        },
        "q3.xy.y180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 6.622475888094236e-20, 2.631838490550177e-19, 5.857761335445659e-19, 1.0256466416312368e-18, 1.57140295820893e-18, 2.208910281350882e-18, 2.9216575062549035e-18, 3.691184854184866e-18, 4.497561971043498e-18, 5.319904113074566e-18, 6.13691305075591e-18, 6.927428681756635e-18, 7.670977066472568e-18, 8.348300692307557e-18, 8.941857233134203e-18, 9.436273886326002e-18, 9.8187455202704e-18, 1.0079366320551338e-17, 1.0211386345339346e-17, 1.0211386345339349e-17, 1.0079366320551338e-17, 9.8187455202704e-18, 9.436273886326005e-18, 8.941857233134205e-18, 8.348300692307557e-18, 7.670977066472565e-18, 6.927428681756638e-18, 6.136913050755913e-18, 5.319904113074566e-18, 4.497561971043503e-18, 3.691184854184869e-18, 2.9216575062549062e-18, 2.2089102813508838e-18, 1.5714029582089305e-18, 1.0256466416312368e-18, 5.857761335445654e-19, 2.631838490550172e-19, 6.622475888094236e-20, 0.0],
        },
        "q3.xy.y180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0010815323883923203, 0.004298118432812735, 0.00956645024430564, 0.016750080796280722, 0.025662957830829294, 0.03607424251447538, 0.047714288042708726, 0.0602816233505826, 0.07345076105494051, 0.08688062740666926, 0.10022339592164317, 0.11313349590395828, 0.12527656254543598, 0.13633809679852132, 0.14603161073641596, 0.154106047439897, 0.1603522832396507, 0.16460854390946003, 0.16676459453368778, 0.1667645945336878, 0.16460854390946003, 0.1603522832396507, 0.15410604743989706, 0.146031610736416, 0.13633809679852132, 0.12527656254543593, 0.11313349590395833, 0.10022339592164321, 0.08688062740666926, 0.07345076105494058, 0.06028162335058265, 0.04771428804270877, 0.036074242514475406, 0.025662957830829305, 0.016750080796280722, 0.009566450244305632, 0.004298118432812727, 0.0010815323883923203, 0.0],
        },
        "q3.xy.y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 3.311237944047118e-20, 1.3159192452750886e-19, 2.9288806677228293e-19, 5.128233208156184e-19, 7.85701479104465e-19, 1.104455140675441e-18, 1.4608287531274518e-18, 1.845592427092433e-18, 2.248780985521749e-18, 2.659952056537283e-18, 3.068456525377955e-18, 3.4637143408783177e-18, 3.835488533236284e-18, 4.1741503461537786e-18, 4.4709286165671015e-18, 4.718136943163001e-18, 4.9093727601352e-18, 5.039683160275669e-18, 5.105693172669673e-18, 5.1056931726696745e-18, 5.039683160275669e-18, 4.9093727601352e-18, 4.7181369431630024e-18, 4.470928616567102e-18, 4.1741503461537786e-18, 3.8354885332362826e-18, 3.463714340878319e-18, 3.0684565253779565e-18, 2.659952056537283e-18, 2.2487809855217515e-18, 1.8455924270924346e-18, 1.4608287531274531e-18, 1.1044551406754419e-18, 7.857014791044653e-19, 5.128233208156184e-19, 2.928880667722827e-19, 1.315919245275086e-19, 3.311237944047118e-20, 0.0],
        },
        "q3.xy.y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0005407661941961602, 0.0021490592164063677, 0.00478322512215282, 0.008375040398140361, 0.012831478915414647, 0.01803712125723769, 0.023857144021354363, 0.0301408116752913, 0.03672538052747026, 0.04344031370333463, 0.050111697960821586, 0.05656674795197914, 0.06263828127271799, 0.06816904839926066, 0.07301580536820798, 0.0770530237199485, 0.08017614161982535, 0.08230427195473002, 0.08338229726684389, 0.0833822972668439, 0.08230427195473002, 0.08017614161982535, 0.07705302371994853, 0.073015805368208, 0.06816904839926066, 0.06263828127271796, 0.05656674795197916, 0.050111697960821606, 0.04344031370333463, 0.03672538052747029, 0.030140811675291326, 0.023857144021354384, 0.018037121257237703, 0.012831478915414652, 0.008375040398140361, 0.004783225122152816, 0.0021490592164063634, 0.0005407661941961602, 0.0],
        },
        "q3.xy.-y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 3.311237944047118e-20, 1.3159192452750886e-19, 2.9288806677228293e-19, 5.128233208156184e-19, 7.85701479104465e-19, 1.104455140675441e-18, 1.4608287531274518e-18, 1.845592427092433e-18, 2.248780985521749e-18, 2.659952056537283e-18, 3.068456525377955e-18, 3.4637143408783177e-18, 3.835488533236284e-18, 4.1741503461537786e-18, 4.4709286165671015e-18, 4.718136943163001e-18, 4.9093727601352e-18, 5.039683160275669e-18, 5.105693172669673e-18, 5.1056931726696745e-18, 5.039683160275669e-18, 4.9093727601352e-18, 4.7181369431630024e-18, 4.470928616567102e-18, 4.1741503461537786e-18, 3.8354885332362826e-18, 3.463714340878319e-18, 3.0684565253779565e-18, 2.659952056537283e-18, 2.2487809855217515e-18, 1.8455924270924346e-18, 1.4608287531274531e-18, 1.1044551406754419e-18, 7.857014791044653e-19, 5.128233208156184e-19, 2.928880667722827e-19, 1.315919245275086e-19, 3.311237944047118e-20, 0.0],
        },
        "q3.xy.-y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.0005407661941961602, -0.0021490592164063677, -0.00478322512215282, -0.008375040398140361, -0.012831478915414647, -0.01803712125723769, -0.023857144021354363, -0.0301408116752913, -0.03672538052747026, -0.04344031370333463, -0.050111697960821586, -0.05656674795197914, -0.06263828127271799, -0.06816904839926066, -0.07301580536820798, -0.0770530237199485, -0.08017614161982535, -0.08230427195473002, -0.08338229726684389, -0.0833822972668439, -0.08230427195473002, -0.08017614161982535, -0.07705302371994853, -0.073015805368208, -0.06816904839926066, -0.06263828127271796, -0.05656674795197916, -0.050111697960821606, -0.04344031370333463, -0.03672538052747029, -0.030140811675291326, -0.023857144021354384, -0.018037121257237703, -0.012831478915414652, -0.008375040398140361, -0.004783225122152816, -0.0021490592164063634, -0.0005407661941961602, 0.0],
        },
        "q3.xy.x180_Square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "q3.xy.x180_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q3.xy.x90_Square.wf.I": {
            "type": "constant",
            "sample": 0.05,
        },
        "q3.xy.x90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q3.xy.-x90_Square.wf.I": {
            "type": "constant",
            "sample": -0.125,
        },
        "q3.xy.-x90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q3.xy.y180_Square.wf.I": {
            "type": "constant",
            "sample": -0.11201840403229253,
        },
        "q3.xy.y180_Square.wf.Q": {
            "type": "constant",
            "sample": 0.22349916590013946,
        },
        "q3.xy.y90_Square.wf.I": {
            "type": "constant",
            "sample": -0.056009202016146266,
        },
        "q3.xy.y90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.11174958295006973,
        },
        "q3.xy.-y90_Square.wf.I": {
            "type": "constant",
            "sample": 0.056009202016146266,
        },
        "q3.xy.-y90_Square.wf.Q": {
            "type": "constant",
            "sample": -0.11174958295006973,
        },
        "q3.xy.saturation.wf.I": {
            "type": "constant",
            "sample": 0.053266113103201604,
        },
        "q3.xy.saturation.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q3.xy.cr_q2_q3_Square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "q3.xy.cr_q2_q3_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q3.xy_detuned.zz_q2_q3_Square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "q3.xy_detuned.zz_q2_q3_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q3.resonator.readout.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "q3.resonator.readout.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q3.resonator.const.wf.I": {
            "type": "constant",
            "sample": 0.125,
        },
        "q3.resonator.const.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q4.xy.x180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0010454824370173307, 0.004154852302117222, 0.009247578549070403, 0.01619176224316678, 0.024807552674341083, 0.03487180539609231, 0.0461238615494358, 0.05827229879043301, 0.07100247897582254, 0.08398469712565869, 0.09688272060910604, 0.10936249739296332, 0.12110080781385363, 0.13179363579772657, 0.14116404271648392, 0.14896933995297812, 0.1550073744087179, 0.1591217641629331] + [0.16120594868217908] * 2 + [0.1591217641629331, 0.15500737440871792, 0.14896933995297815, 0.14116404271648395, 0.13179363579772657, 0.12110080781385357, 0.10936249739296335, 0.09688272060910608, 0.08398469712565869, 0.0710024789758226, 0.05827229879043306, 0.04612386154943584, 0.03487180539609234, 0.024807552674341093, 0.01619176224316678, 0.009247578549070394, 0.004154852302117213, 0.0010454824370173307, 0.0],
        },
        "q4.xy.x180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
        },
        "q4.xy.x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0005227412185086653, 0.002077426151058611, 0.0046237892745352015, 0.00809588112158339, 0.012403776337170542, 0.017435902698046155, 0.0230619307747179, 0.029136149395216505, 0.03550123948791127, 0.041992348562829344, 0.04844136030455302, 0.05468124869648166, 0.060550403906926814, 0.06589681789886329, 0.07058202135824196, 0.07448466997648906, 0.07750368720435895, 0.07956088208146656] + [0.08060297434108954] * 2 + [0.07956088208146656, 0.07750368720435896, 0.07448466997648907, 0.07058202135824197, 0.06589681789886329, 0.060550403906926786, 0.05468124869648167, 0.04844136030455304, 0.041992348562829344, 0.0355012394879113, 0.02913614939521653, 0.02306193077471792, 0.01743590269804617, 0.012403776337170547, 0.00809588112158339, 0.004623789274535197, 0.0020774261510586064, 0.0005227412185086653, 0.0],
        },
        "q4.xy.x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
        },
        "q4.xy.-x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -0.0005227412185086653, -0.002077426151058611, -0.0046237892745352015, -0.00809588112158339, -0.012403776337170542, -0.017435902698046155, -0.0230619307747179, -0.029136149395216505, -0.03550123948791127, -0.041992348562829344, -0.04844136030455302, -0.05468124869648166, -0.060550403906926814, -0.06589681789886329, -0.07058202135824196, -0.07448466997648906, -0.07750368720435895, -0.07956088208146656] + [-0.08060297434108954] * 2 + [-0.07956088208146656, -0.07750368720435896, -0.07448466997648907, -0.07058202135824197, -0.06589681789886329, -0.060550403906926786, -0.05468124869648167, -0.04844136030455304, -0.041992348562829344, -0.0355012394879113, -0.02913614939521653, -0.02306193077471792, -0.01743590269804617, -0.012403776337170547, -0.00809588112158339, -0.004623789274535197, -0.0020774261510586064, -0.0005227412185086653, 0.0],
        },
        "q4.xy.-x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 6.401733600290242e-20, 2.544113286358934e-19, 5.662508734991397e-19, 9.914594901824583e-19, 1.5190244988655585e-18, 2.1352822429406924e-18, 2.8242719705416114e-18, 3.568149209633098e-18, 4.347647930463416e-18, 5.142579525614891e-18, 5.932355684331451e-18, 6.696521618952664e-18, 7.415285833169731e-18, 8.070032711383894e-18, 8.643804653372114e-18, 9.121741267225428e-18, 9.491464245693587e-18, 9.743397957840803e-18] + [9.871017452857154e-18] * 2 + [9.743397957840803e-18, 9.491464245693588e-18, 9.12174126722543e-18, 8.643804653372116e-18, 8.070032711383894e-18, 7.415285833169728e-18, 6.696521618952666e-18, 5.932355684331453e-18, 5.142579525614891e-18, 4.347647930463419e-18, 3.568149209633101e-18, 2.824271970541614e-18, 2.135282242940694e-18, 1.519024498865559e-18, 9.914594901824583e-19, 5.662508734991392e-19, 2.5441132863589283e-19, 6.401733600290242e-20, 0.0],
        },
        "q4.xy.y180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 6.401733600290242e-20, 2.544113286358934e-19, 5.662508734991397e-19, 9.914594901824583e-19, 1.5190244988655585e-18, 2.1352822429406924e-18, 2.8242719705416114e-18, 3.568149209633098e-18, 4.347647930463416e-18, 5.142579525614891e-18, 5.932355684331451e-18, 6.696521618952664e-18, 7.415285833169731e-18, 8.070032711383894e-18, 8.643804653372114e-18, 9.121741267225428e-18, 9.491464245693587e-18, 9.743397957840803e-18] + [9.871017452857154e-18] * 2 + [9.743397957840803e-18, 9.491464245693588e-18, 9.12174126722543e-18, 8.643804653372116e-18, 8.070032711383894e-18, 7.415285833169728e-18, 6.696521618952666e-18, 5.932355684331453e-18, 5.142579525614891e-18, 4.347647930463419e-18, 3.568149209633101e-18, 2.824271970541614e-18, 2.135282242940694e-18, 1.519024498865559e-18, 9.914594901824583e-19, 5.662508734991392e-19, 2.5441132863589283e-19, 6.401733600290242e-20, 0.0],
        },
        "q4.xy.y180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0010454824370173307, 0.004154852302117222, 0.009247578549070403, 0.01619176224316678, 0.024807552674341083, 0.03487180539609231, 0.0461238615494358, 0.05827229879043301, 0.07100247897582254, 0.08398469712565869, 0.09688272060910604, 0.10936249739296332, 0.12110080781385363, 0.13179363579772657, 0.14116404271648392, 0.14896933995297812, 0.1550073744087179, 0.1591217641629331] + [0.16120594868217908] * 2 + [0.1591217641629331, 0.15500737440871792, 0.14896933995297815, 0.14116404271648395, 0.13179363579772657, 0.12110080781385357, 0.10936249739296335, 0.09688272060910608, 0.08398469712565869, 0.0710024789758226, 0.05827229879043306, 0.04612386154943584, 0.03487180539609234, 0.024807552674341093, 0.01619176224316678, 0.009247578549070394, 0.004154852302117213, 0.0010454824370173307, 0.0],
        },
        "q4.xy.y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 3.200866800145121e-20, 1.272056643179467e-19, 2.8312543674956984e-19, 4.9572974509122915e-19, 7.595122494327792e-19, 1.0676411214703462e-18, 1.4121359852708057e-18, 1.784074604816549e-18, 2.173823965231708e-18, 2.5712897628074456e-18, 2.9661778421657254e-18, 3.348260809476332e-18, 3.707642916584866e-18, 4.035016355691947e-18, 4.321902326686057e-18, 4.560870633612714e-18, 4.7457321228467934e-18, 4.8716989789204015e-18] + [4.935508726428577e-18] * 2 + [4.8716989789204015e-18, 4.745732122846794e-18, 4.560870633612715e-18, 4.321902326686058e-18, 4.035016355691947e-18, 3.707642916584864e-18, 3.348260809476333e-18, 2.9661778421657266e-18, 2.5712897628074456e-18, 2.1738239652317096e-18, 1.7840746048165507e-18, 1.412135985270807e-18, 1.067641121470347e-18, 7.595122494327795e-19, 4.9572974509122915e-19, 2.831254367495696e-19, 1.2720566431794642e-19, 3.200866800145121e-20, 0.0],
        },
        "q4.xy.y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0005227412185086653, 0.002077426151058611, 0.0046237892745352015, 0.00809588112158339, 0.012403776337170542, 0.017435902698046155, 0.0230619307747179, 0.029136149395216505, 0.03550123948791127, 0.041992348562829344, 0.04844136030455302, 0.05468124869648166, 0.060550403906926814, 0.06589681789886329, 0.07058202135824196, 0.07448466997648906, 0.07750368720435895, 0.07956088208146656] + [0.08060297434108954] * 2 + [0.07956088208146656, 0.07750368720435896, 0.07448466997648907, 0.07058202135824197, 0.06589681789886329, 0.060550403906926786, 0.05468124869648167, 0.04844136030455304, 0.041992348562829344, 0.0355012394879113, 0.02913614939521653, 0.02306193077471792, 0.01743590269804617, 0.012403776337170547, 0.00809588112158339, 0.004623789274535197, 0.0020774261510586064, 0.0005227412185086653, 0.0],
        },
        "q4.xy.-y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 3.200866800145121e-20, 1.272056643179467e-19, 2.8312543674956984e-19, 4.9572974509122915e-19, 7.595122494327792e-19, 1.0676411214703462e-18, 1.4121359852708057e-18, 1.784074604816549e-18, 2.173823965231708e-18, 2.5712897628074456e-18, 2.9661778421657254e-18, 3.348260809476332e-18, 3.707642916584866e-18, 4.035016355691947e-18, 4.321902326686057e-18, 4.560870633612714e-18, 4.7457321228467934e-18, 4.8716989789204015e-18] + [4.935508726428577e-18] * 2 + [4.8716989789204015e-18, 4.745732122846794e-18, 4.560870633612715e-18, 4.321902326686058e-18, 4.035016355691947e-18, 3.707642916584864e-18, 3.348260809476333e-18, 2.9661778421657266e-18, 2.5712897628074456e-18, 2.1738239652317096e-18, 1.7840746048165507e-18, 1.412135985270807e-18, 1.067641121470347e-18, 7.595122494327795e-19, 4.9572974509122915e-19, 2.831254367495696e-19, 1.2720566431794642e-19, 3.200866800145121e-20, 0.0],
        },
        "q4.xy.-y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.0005227412185086653, -0.002077426151058611, -0.0046237892745352015, -0.00809588112158339, -0.012403776337170542, -0.017435902698046155, -0.0230619307747179, -0.029136149395216505, -0.03550123948791127, -0.041992348562829344, -0.04844136030455302, -0.05468124869648166, -0.060550403906926814, -0.06589681789886329, -0.07058202135824196, -0.07448466997648906, -0.07750368720435895, -0.07956088208146656] + [-0.08060297434108954] * 2 + [-0.07956088208146656, -0.07750368720435896, -0.07448466997648907, -0.07058202135824197, -0.06589681789886329, -0.060550403906926786, -0.05468124869648167, -0.04844136030455304, -0.041992348562829344, -0.0355012394879113, -0.02913614939521653, -0.02306193077471792, -0.01743590269804617, -0.012403776337170547, -0.00809588112158339, -0.004623789274535197, -0.0020774261510586064, -0.0005227412185086653, 0.0],
        },
        "q4.xy.x180_Square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "q4.xy.x180_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q4.xy.x90_Square.wf.I": {
            "type": "constant",
            "sample": 0.05,
        },
        "q4.xy.x90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q4.xy.-x90_Square.wf.I": {
            "type": "constant",
            "sample": -0.125,
        },
        "q4.xy.-x90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q4.xy.y180_Square.wf.I": {
            "type": "constant",
            "sample": -0.11201840403229253,
        },
        "q4.xy.y180_Square.wf.Q": {
            "type": "constant",
            "sample": 0.22349916590013946,
        },
        "q4.xy.y90_Square.wf.I": {
            "type": "constant",
            "sample": -0.056009202016146266,
        },
        "q4.xy.y90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.11174958295006973,
        },
        "q4.xy.-y90_Square.wf.I": {
            "type": "constant",
            "sample": 0.056009202016146266,
        },
        "q4.xy.-y90_Square.wf.Q": {
            "type": "constant",
            "sample": -0.11174958295006973,
        },
        "q4.xy.saturation.wf.I": {
            "type": "constant",
            "sample": 0.050494213379647726,
        },
        "q4.xy.saturation.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q4.xy.cr_q3_q4_Square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "q4.xy.cr_q3_q4_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q4.xy_detuned.zz_q3_q4_Square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "q4.xy_detuned.zz_q3_q4_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q4.resonator.readout.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "q4.resonator.readout.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q4.resonator.const.wf.I": {
            "type": "constant",
            "sample": 0.125,
        },
        "q4.resonator.const.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q5.xy.x180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0007476787839983893, 0.002971350648225588, 0.0066134236594391806, 0.011579570039741652, 0.017741169206479807, 0.024938638977774204, 0.03298556866720522, 0.041673547022674215, 0.05077755996835955, 0.060061818351085886, 0.06928586475553708, 0.0782108012250065, 0.08660547659298821, 0.09425247317697152, 0.10095373778221371, 0.10653571117545134, 0.11085382317787522, 0.1137962369568224, 0.11528674554099697, 0.11528674554099698, 0.1137962369568224, 0.11085382317787523, 0.10653571117545137, 0.10095373778221374, 0.09425247317697152, 0.08660547659298819, 0.07821080122500652, 0.06928586475553711, 0.060061818351085886, 0.050777559968359594, 0.04167354702267425, 0.03298556866720525, 0.024938638977774225, 0.017741169206479813, 0.011579570039741652, 0.0066134236594391745, 0.0029713506482255815, 0.0007476787839983893, 0.0],
        },
        "q5.xy.x180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
        },
        "q5.xy.x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.00037383939199919466, 0.001485675324112794, 0.0033067118297195903, 0.005789785019870826, 0.008870584603239903, 0.012469319488887102, 0.01649278433360261, 0.020836773511337107, 0.025388779984179776, 0.030030909175542943, 0.03464293237776854, 0.03910540061250325, 0.04330273829649411, 0.04712623658848576, 0.050476868891106856, 0.05326785558772567, 0.05542691158893761, 0.0568981184784112, 0.05764337277049848, 0.05764337277049849, 0.0568981184784112, 0.055426911588937616, 0.05326785558772568, 0.05047686889110687, 0.04712623658848576, 0.043302738296494094, 0.03910540061250326, 0.034642932377768554, 0.030030909175542943, 0.025388779984179797, 0.020836773511337125, 0.016492784333602625, 0.012469319488887113, 0.008870584603239907, 0.005789785019870826, 0.0033067118297195872, 0.0014856753241127907, 0.00037383939199919466, 0.0],
        },
        "q5.xy.x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
        },
        "q5.xy.-x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -0.00037383939199919466, -0.001485675324112794, -0.0033067118297195903, -0.005789785019870826, -0.008870584603239903, -0.012469319488887102, -0.01649278433360261, -0.020836773511337107, -0.025388779984179776, -0.030030909175542943, -0.03464293237776854, -0.03910540061250325, -0.04330273829649411, -0.04712623658848576, -0.050476868891106856, -0.05326785558772567, -0.05542691158893761, -0.0568981184784112, -0.05764337277049848, -0.05764337277049849, -0.0568981184784112, -0.055426911588937616, -0.05326785558772568, -0.05047686889110687, -0.04712623658848576, -0.043302738296494094, -0.03910540061250326, -0.034642932377768554, -0.030030909175542943, -0.025388779984179797, -0.020836773511337125, -0.016492784333602625, -0.012469319488887113, -0.008870584603239907, -0.005789785019870826, -0.0033067118297195872, -0.0014856753241127907, -0.00037383939199919466, 0.0],
        },
        "q5.xy.-x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 4.578212148070064e-20, 1.8194275302469397e-19, 4.049554057968784e-19, 7.090441692336102e-19, 1.0863333040923541e-18, 1.52705121996113e-18, 2.019783554317405e-18, 2.5517687985217346e-18, 3.109228814188215e-18, 3.6777256797313546e-18, 4.242535624951245e-18, 4.789030368947705e-18, 5.3030559849117015e-18, 5.771299479394997e-18, 6.181633591847462e-18, 6.523430884295169e-18, 6.787838986401578e-18, 6.968009867209315e-18] + [7.059277195544867e-18] * 2 + [6.968009867209315e-18, 6.787838986401579e-18, 6.523430884295171e-18, 6.1816335918474636e-18, 5.771299479394997e-18, 5.3030559849117e-18, 4.789030368947707e-18, 4.242535624951246e-18, 3.6777256797313546e-18, 3.1092288141882177e-18, 2.5517687985217365e-18, 2.019783554317407e-18, 1.5270512199611313e-18, 1.0863333040923545e-18, 7.090441692336102e-19, 4.04955405796878e-19, 1.8194275302469358e-19, 4.578212148070064e-20, 0.0],
        },
        "q5.xy.y180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 4.578212148070064e-20, 1.8194275302469397e-19, 4.049554057968784e-19, 7.090441692336102e-19, 1.0863333040923541e-18, 1.52705121996113e-18, 2.019783554317405e-18, 2.5517687985217346e-18, 3.109228814188215e-18, 3.6777256797313546e-18, 4.242535624951245e-18, 4.789030368947705e-18, 5.3030559849117015e-18, 5.771299479394997e-18, 6.181633591847462e-18, 6.523430884295169e-18, 6.787838986401578e-18, 6.968009867209315e-18] + [7.059277195544867e-18] * 2 + [6.968009867209315e-18, 6.787838986401579e-18, 6.523430884295171e-18, 6.1816335918474636e-18, 5.771299479394997e-18, 5.3030559849117e-18, 4.789030368947707e-18, 4.242535624951246e-18, 3.6777256797313546e-18, 3.1092288141882177e-18, 2.5517687985217365e-18, 2.019783554317407e-18, 1.5270512199611313e-18, 1.0863333040923545e-18, 7.090441692336102e-19, 4.04955405796878e-19, 1.8194275302469358e-19, 4.578212148070064e-20, 0.0],
        },
        "q5.xy.y180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0007476787839983893, 0.002971350648225588, 0.0066134236594391806, 0.011579570039741652, 0.017741169206479807, 0.024938638977774204, 0.03298556866720522, 0.041673547022674215, 0.05077755996835955, 0.060061818351085886, 0.06928586475553708, 0.0782108012250065, 0.08660547659298821, 0.09425247317697152, 0.10095373778221371, 0.10653571117545134, 0.11085382317787522, 0.1137962369568224, 0.11528674554099697, 0.11528674554099698, 0.1137962369568224, 0.11085382317787523, 0.10653571117545137, 0.10095373778221374, 0.09425247317697152, 0.08660547659298819, 0.07821080122500652, 0.06928586475553711, 0.060061818351085886, 0.050777559968359594, 0.04167354702267425, 0.03298556866720525, 0.024938638977774225, 0.017741169206479813, 0.011579570039741652, 0.0066134236594391745, 0.0029713506482255815, 0.0007476787839983893, 0.0],
        },
        "q5.xy.y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 2.289106074035032e-20, 9.097137651234698e-20, 2.024777028984392e-19, 3.545220846168051e-19, 5.431666520461771e-19, 7.63525609980565e-19, 1.0098917771587025e-18, 1.2758843992608673e-18, 1.5546144070941075e-18, 1.8388628398656773e-18, 2.1212678124756224e-18, 2.3945151844738526e-18, 2.6515279924558508e-18, 2.8856497396974984e-18, 3.090816795923731e-18, 3.2617154421475846e-18, 3.393919493200789e-18, 3.4840049336046575e-18] + [3.5296385977724334e-18] * 2 + [3.4840049336046575e-18, 3.3939194932007896e-18, 3.2617154421475854e-18, 3.0908167959237318e-18, 2.8856497396974984e-18, 2.65152799245585e-18, 2.3945151844738533e-18, 2.121267812475623e-18, 1.8388628398656773e-18, 1.5546144070941088e-18, 1.2758843992608683e-18, 1.0098917771587034e-18, 7.635256099805656e-19, 5.431666520461773e-19, 3.545220846168051e-19, 2.02477702898439e-19, 9.097137651234679e-20, 2.289106074035032e-20, 0.0],
        },
        "q5.xy.y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.00037383939199919466, 0.001485675324112794, 0.0033067118297195903, 0.005789785019870826, 0.008870584603239903, 0.012469319488887102, 0.01649278433360261, 0.020836773511337107, 0.025388779984179776, 0.030030909175542943, 0.03464293237776854, 0.03910540061250325, 0.04330273829649411, 0.04712623658848576, 0.050476868891106856, 0.05326785558772567, 0.05542691158893761, 0.0568981184784112, 0.05764337277049848, 0.05764337277049849, 0.0568981184784112, 0.055426911588937616, 0.05326785558772568, 0.05047686889110687, 0.04712623658848576, 0.043302738296494094, 0.03910540061250326, 0.034642932377768554, 0.030030909175542943, 0.025388779984179797, 0.020836773511337125, 0.016492784333602625, 0.012469319488887113, 0.008870584603239907, 0.005789785019870826, 0.0033067118297195872, 0.0014856753241127907, 0.00037383939199919466, 0.0],
        },
        "q5.xy.-y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 2.289106074035032e-20, 9.097137651234698e-20, 2.024777028984392e-19, 3.545220846168051e-19, 5.431666520461771e-19, 7.63525609980565e-19, 1.0098917771587025e-18, 1.2758843992608673e-18, 1.5546144070941075e-18, 1.8388628398656773e-18, 2.1212678124756224e-18, 2.3945151844738526e-18, 2.6515279924558508e-18, 2.8856497396974984e-18, 3.090816795923731e-18, 3.2617154421475846e-18, 3.393919493200789e-18, 3.4840049336046575e-18] + [3.5296385977724334e-18] * 2 + [3.4840049336046575e-18, 3.3939194932007896e-18, 3.2617154421475854e-18, 3.0908167959237318e-18, 2.8856497396974984e-18, 2.65152799245585e-18, 2.3945151844738533e-18, 2.121267812475623e-18, 1.8388628398656773e-18, 1.5546144070941088e-18, 1.2758843992608683e-18, 1.0098917771587034e-18, 7.635256099805656e-19, 5.431666520461773e-19, 3.545220846168051e-19, 2.02477702898439e-19, 9.097137651234679e-20, 2.289106074035032e-20, 0.0],
        },
        "q5.xy.-y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.00037383939199919466, -0.001485675324112794, -0.0033067118297195903, -0.005789785019870826, -0.008870584603239903, -0.012469319488887102, -0.01649278433360261, -0.020836773511337107, -0.025388779984179776, -0.030030909175542943, -0.03464293237776854, -0.03910540061250325, -0.04330273829649411, -0.04712623658848576, -0.050476868891106856, -0.05326785558772567, -0.05542691158893761, -0.0568981184784112, -0.05764337277049848, -0.05764337277049849, -0.0568981184784112, -0.055426911588937616, -0.05326785558772568, -0.05047686889110687, -0.04712623658848576, -0.043302738296494094, -0.03910540061250326, -0.034642932377768554, -0.030030909175542943, -0.025388779984179797, -0.020836773511337125, -0.016492784333602625, -0.012469319488887113, -0.008870584603239907, -0.005789785019870826, -0.0033067118297195872, -0.0014856753241127907, -0.00037383939199919466, 0.0],
        },
        "q5.xy.x180_Square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "q5.xy.x180_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q5.xy.x90_Square.wf.I": {
            "type": "constant",
            "sample": 0.05,
        },
        "q5.xy.x90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q5.xy.-x90_Square.wf.I": {
            "type": "constant",
            "sample": -0.125,
        },
        "q5.xy.-x90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q5.xy.y180_Square.wf.I": {
            "type": "constant",
            "sample": -0.11201840403229253,
        },
        "q5.xy.y180_Square.wf.Q": {
            "type": "constant",
            "sample": 0.22349916590013946,
        },
        "q5.xy.y90_Square.wf.I": {
            "type": "constant",
            "sample": -0.056009202016146266,
        },
        "q5.xy.y90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.11174958295006973,
        },
        "q5.xy.-y90_Square.wf.I": {
            "type": "constant",
            "sample": 0.056009202016146266,
        },
        "q5.xy.-y90_Square.wf.Q": {
            "type": "constant",
            "sample": -0.11174958295006973,
        },
        "q5.xy.saturation.wf.I": {
            "type": "constant",
            "sample": 0.05521676406770869,
        },
        "q5.xy.saturation.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q5.xy.cr_q4_q5_Square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "q5.xy.cr_q4_q5_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q5.xy_detuned.zz_q4_q5_Square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "q5.xy_detuned.zz_q4_q5_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q5.resonator.readout.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "q5.resonator.readout.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q5.resonator.const.wf.I": {
            "type": "constant",
            "sample": 0.125,
        },
        "q5.resonator.const.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q6.xy.x180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0009296953956100164, 0.003694702960040281, 0.008223410449763675, 0.014398526719616937, 0.022060119501850165, 0.031009757567852982, 0.041015649992744464, 0.051818649418573295, 0.06313896383476499, 0.07468340304422766, 0.08615297213545103, 0.09725061529365987, 0.10768890939038021, 0.1171975080914905, 0.12553014368526905, 0.13247100528676906, 0.13784032822637848, 0.14149904986033693, 0.14335241122016293, 0.14335241122016296, 0.14149904986033693, 0.13784032822637848, 0.13247100528676908, 0.12553014368526907, 0.1171975080914905, 0.10768890939038017, 0.09725061529365991, 0.08615297213545106, 0.07468340304422766, 0.06313896383476504, 0.051818649418573344, 0.04101564999274449, 0.031009757567853007, 0.022060119501850176, 0.014398526719616937, 0.008223410449763666, 0.003694702960040273, 0.0009296953956100164, 0.0],
        },
        "q6.xy.x180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
        },
        "q6.xy.x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0004648476978050082, 0.0018473514800201405, 0.004111705224881837, 0.007199263359808469, 0.011030059750925083, 0.015504878783926491, 0.020507824996372232, 0.025909324709286648, 0.03156948191738249, 0.03734170152211383, 0.04307648606772552, 0.048625307646829936, 0.05384445469519011, 0.05859875404574525, 0.06276507184263452, 0.06623550264338453, 0.06892016411318924, 0.07074952493016846, 0.07167620561008146, 0.07167620561008148, 0.07074952493016846, 0.06892016411318924, 0.06623550264338454, 0.06276507184263454, 0.05859875404574525, 0.053844454695190086, 0.04862530764682996, 0.04307648606772553, 0.03734170152211383, 0.03156948191738252, 0.025909324709286672, 0.020507824996372246, 0.015504878783926503, 0.011030059750925088, 0.007199263359808469, 0.004111705224881833, 0.0018473514800201366, 0.0004648476978050082, 0.0],
        },
        "q6.xy.x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
        },
        "q6.xy.-x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -0.0004648476978050082, -0.0018473514800201405, -0.004111705224881837, -0.007199263359808469, -0.011030059750925083, -0.015504878783926491, -0.020507824996372232, -0.025909324709286648, -0.03156948191738249, -0.03734170152211383, -0.04307648606772552, -0.048625307646829936, -0.05384445469519011, -0.05859875404574525, -0.06276507184263452, -0.06623550264338453, -0.06892016411318924, -0.07074952493016846, -0.07167620561008146, -0.07167620561008148, -0.07074952493016846, -0.06892016411318924, -0.06623550264338454, -0.06276507184263454, -0.05859875404574525, -0.053844454695190086, -0.04862530764682996, -0.04307648606772553, -0.03734170152211383, -0.03156948191738252, -0.025909324709286672, -0.020507824996372246, -0.015504878783926503, -0.011030059750925088, -0.007199263359808469, -0.004111705224881833, -0.0018473514800201366, -0.0004648476978050082, 0.0],
        },
        "q6.xy.-x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 5.692742452079194e-20, 2.2623530769067906e-19, 5.03538664268899e-19, 8.81655482980826e-19, 1.3507927368374454e-18, 1.8988000173903284e-18, 2.5114842239281333e-18, 3.1729771573297322e-18, 3.8661464980862714e-18, 4.573039524377255e-18, 5.275348078135561e-18, 5.95488273672456e-18, 6.594043909429924e-18, 7.176277657614494e-18, 7.686504433033604e-18, 8.111509630213692e-18, 8.44028583779275e-18, 8.664317924692668e-18, 8.777803577541383e-18, 8.777803577541385e-18, 8.664317924692668e-18, 8.44028583779275e-18, 8.111509630213693e-18, 7.686504433033605e-18, 7.176277657614494e-18, 6.594043909429921e-18, 5.954882736724563e-18, 5.275348078135563e-18, 4.573039524377255e-18, 3.866146498086275e-18, 3.172977157329735e-18, 2.5114842239281352e-18, 1.89880001739033e-18, 1.350792736837446e-18, 8.81655482980826e-19, 5.035386642688985e-19, 2.262353076906786e-19, 5.692742452079194e-20, 0.0],
        },
        "q6.xy.y180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 5.692742452079194e-20, 2.2623530769067906e-19, 5.03538664268899e-19, 8.81655482980826e-19, 1.3507927368374454e-18, 1.8988000173903284e-18, 2.5114842239281333e-18, 3.1729771573297322e-18, 3.8661464980862714e-18, 4.573039524377255e-18, 5.275348078135561e-18, 5.95488273672456e-18, 6.594043909429924e-18, 7.176277657614494e-18, 7.686504433033604e-18, 8.111509630213692e-18, 8.44028583779275e-18, 8.664317924692668e-18, 8.777803577541383e-18, 8.777803577541385e-18, 8.664317924692668e-18, 8.44028583779275e-18, 8.111509630213693e-18, 7.686504433033605e-18, 7.176277657614494e-18, 6.594043909429921e-18, 5.954882736724563e-18, 5.275348078135563e-18, 4.573039524377255e-18, 3.866146498086275e-18, 3.172977157329735e-18, 2.5114842239281352e-18, 1.89880001739033e-18, 1.350792736837446e-18, 8.81655482980826e-19, 5.035386642688985e-19, 2.262353076906786e-19, 5.692742452079194e-20, 0.0],
        },
        "q6.xy.y180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0009296953956100164, 0.003694702960040281, 0.008223410449763675, 0.014398526719616937, 0.022060119501850165, 0.031009757567852982, 0.041015649992744464, 0.051818649418573295, 0.06313896383476499, 0.07468340304422766, 0.08615297213545103, 0.09725061529365987, 0.10768890939038021, 0.1171975080914905, 0.12553014368526905, 0.13247100528676906, 0.13784032822637848, 0.14149904986033693, 0.14335241122016293, 0.14335241122016296, 0.14149904986033693, 0.13784032822637848, 0.13247100528676908, 0.12553014368526907, 0.1171975080914905, 0.10768890939038017, 0.09725061529365991, 0.08615297213545106, 0.07468340304422766, 0.06313896383476504, 0.051818649418573344, 0.04101564999274449, 0.031009757567853007, 0.022060119501850176, 0.014398526719616937, 0.008223410449763666, 0.003694702960040273, 0.0009296953956100164, 0.0],
        },
        "q6.xy.y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 2.846371226039597e-20, 1.1311765384533953e-19, 2.517693321344495e-19, 4.40827741490413e-19, 6.753963684187227e-19, 9.494000086951642e-19, 1.2557421119640666e-18, 1.5864885786648661e-18, 1.9330732490431357e-18, 2.2865197621886276e-18, 2.6376740390677803e-18, 2.97744136836228e-18, 3.297021954714962e-18, 3.588138828807247e-18, 3.843252216516802e-18, 4.055754815106846e-18, 4.220142918896375e-18, 4.332158962346334e-18, 4.388901788770692e-18, 4.3889017887706924e-18, 4.332158962346334e-18, 4.220142918896375e-18, 4.0557548151068465e-18, 3.843252216516803e-18, 3.588138828807247e-18, 3.2970219547149605e-18, 2.9774413683622814e-18, 2.6376740390677815e-18, 2.2865197621886276e-18, 1.9330732490431376e-18, 1.5864885786648674e-18, 1.2557421119640676e-18, 9.49400008695165e-19, 6.75396368418723e-19, 4.40827741490413e-19, 2.5176933213444926e-19, 1.131176538453393e-19, 2.846371226039597e-20, 0.0],
        },
        "q6.xy.y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0004648476978050082, 0.0018473514800201405, 0.004111705224881837, 0.007199263359808469, 0.011030059750925083, 0.015504878783926491, 0.020507824996372232, 0.025909324709286648, 0.03156948191738249, 0.03734170152211383, 0.04307648606772552, 0.048625307646829936, 0.05384445469519011, 0.05859875404574525, 0.06276507184263452, 0.06623550264338453, 0.06892016411318924, 0.07074952493016846, 0.07167620561008146, 0.07167620561008148, 0.07074952493016846, 0.06892016411318924, 0.06623550264338454, 0.06276507184263454, 0.05859875404574525, 0.053844454695190086, 0.04862530764682996, 0.04307648606772553, 0.03734170152211383, 0.03156948191738252, 0.025909324709286672, 0.020507824996372246, 0.015504878783926503, 0.011030059750925088, 0.007199263359808469, 0.004111705224881833, 0.0018473514800201366, 0.0004648476978050082, 0.0],
        },
        "q6.xy.-y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 2.846371226039597e-20, 1.1311765384533953e-19, 2.517693321344495e-19, 4.40827741490413e-19, 6.753963684187227e-19, 9.494000086951642e-19, 1.2557421119640666e-18, 1.5864885786648661e-18, 1.9330732490431357e-18, 2.2865197621886276e-18, 2.6376740390677803e-18, 2.97744136836228e-18, 3.297021954714962e-18, 3.588138828807247e-18, 3.843252216516802e-18, 4.055754815106846e-18, 4.220142918896375e-18, 4.332158962346334e-18, 4.388901788770692e-18, 4.3889017887706924e-18, 4.332158962346334e-18, 4.220142918896375e-18, 4.0557548151068465e-18, 3.843252216516803e-18, 3.588138828807247e-18, 3.2970219547149605e-18, 2.9774413683622814e-18, 2.6376740390677815e-18, 2.2865197621886276e-18, 1.9330732490431376e-18, 1.5864885786648674e-18, 1.2557421119640676e-18, 9.49400008695165e-19, 6.75396368418723e-19, 4.40827741490413e-19, 2.5176933213444926e-19, 1.131176538453393e-19, 2.846371226039597e-20, 0.0],
        },
        "q6.xy.-y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.0004648476978050082, -0.0018473514800201405, -0.004111705224881837, -0.007199263359808469, -0.011030059750925083, -0.015504878783926491, -0.020507824996372232, -0.025909324709286648, -0.03156948191738249, -0.03734170152211383, -0.04307648606772552, -0.048625307646829936, -0.05384445469519011, -0.05859875404574525, -0.06276507184263452, -0.06623550264338453, -0.06892016411318924, -0.07074952493016846, -0.07167620561008146, -0.07167620561008148, -0.07074952493016846, -0.06892016411318924, -0.06623550264338454, -0.06276507184263454, -0.05859875404574525, -0.053844454695190086, -0.04862530764682996, -0.04307648606772553, -0.03734170152211383, -0.03156948191738252, -0.025909324709286672, -0.020507824996372246, -0.015504878783926503, -0.011030059750925088, -0.007199263359808469, -0.004111705224881833, -0.0018473514800201366, -0.0004648476978050082, 0.0],
        },
        "q6.xy.x180_Square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "q6.xy.x180_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q6.xy.x90_Square.wf.I": {
            "type": "constant",
            "sample": 0.05,
        },
        "q6.xy.x90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q6.xy.-x90_Square.wf.I": {
            "type": "constant",
            "sample": -0.125,
        },
        "q6.xy.-x90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q6.xy.y180_Square.wf.I": {
            "type": "constant",
            "sample": -0.11201840403229253,
        },
        "q6.xy.y180_Square.wf.Q": {
            "type": "constant",
            "sample": 0.22349916590013946,
        },
        "q6.xy.y90_Square.wf.I": {
            "type": "constant",
            "sample": -0.056009202016146266,
        },
        "q6.xy.y90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.11174958295006973,
        },
        "q6.xy.-y90_Square.wf.I": {
            "type": "constant",
            "sample": 0.056009202016146266,
        },
        "q6.xy.-y90_Square.wf.Q": {
            "type": "constant",
            "sample": -0.11174958295006973,
        },
        "q6.xy.saturation.wf.I": {
            "type": "constant",
            "sample": 0.06342628178578913,
        },
        "q6.xy.saturation.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q6.xy.cr_q5_q6_Square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "q6.xy.cr_q5_q6_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q6.xy_detuned.zz_q5_q6_Square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "q6.xy_detuned.zz_q5_q6_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q6.resonator.readout.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "q6.resonator.readout.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q6.resonator.const.wf.I": {
            "type": "constant",
            "sample": 0.125,
        },
        "q6.resonator.const.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q7.xy.x180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.00020538635070153783, 0.000816226004207466, 0.001816698534351283, 0.0031808922281263, 0.004873475185441714, 0.006850610396775961, 0.009061091098696824, 0.011447667002136619, 0.01394852704480689, 0.0164989002652438, 0.01903273333668742, 0.021484401313548646, 0.023790407283028676, 0.025891026901807158, 0.027731855225162447, 0.02926521576646226, 0.030451395293124153, 0.03125967237847901, 0.03166911307058455, 0.03166911307058456, 0.03125967237847901, 0.030451395293124156, 0.029265215766462266, 0.027731855225162454, 0.025891026901807158, 0.023790407283028663, 0.021484401313548653, 0.019032733336687428, 0.0164989002652438, 0.013948527044806903, 0.01144766700213663, 0.00906109109869683, 0.006850610396775966, 0.004873475185441715, 0.0031808922281263, 0.0018166985343512812, 0.0008162260042074642, 0.00020538635070153783, 0.0],
        },
        "q7.xy.x180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
        },
        "q7.xy.x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.00010269317535076891, 0.000408113002103733, 0.0009083492671756414, 0.00159044611406315, 0.002436737592720857, 0.0034253051983879805, 0.004530545549348412, 0.0057238335010683095, 0.006974263522403445, 0.0082494501326219, 0.00951636666834371, 0.010742200656774323, 0.011895203641514338, 0.012945513450903579, 0.013865927612581224, 0.01463260788323113, 0.015225697646562076, 0.015629836189239504, 0.015834556535292275, 0.01583455653529228, 0.015629836189239504, 0.015225697646562078, 0.014632607883231133, 0.013865927612581227, 0.012945513450903579, 0.011895203641514331, 0.010742200656774326, 0.009516366668343714, 0.0082494501326219, 0.006974263522403452, 0.005723833501068315, 0.004530545549348415, 0.003425305198387983, 0.0024367375927208577, 0.00159044611406315, 0.0009083492671756406, 0.0004081130021037321, 0.00010269317535076891, 0.0],
        },
        "q7.xy.x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
        },
        "q7.xy.-x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -0.00010269317535076891, -0.000408113002103733, -0.0009083492671756414, -0.00159044611406315, -0.002436737592720857, -0.0034253051983879805, -0.004530545549348412, -0.0057238335010683095, -0.006974263522403445, -0.0082494501326219, -0.00951636666834371, -0.010742200656774323, -0.011895203641514338, -0.012945513450903579, -0.013865927612581224, -0.01463260788323113, -0.015225697646562076, -0.015629836189239504, -0.015834556535292275, -0.01583455653529228, -0.015629836189239504, -0.015225697646562078, -0.014632607883231133, -0.013865927612581227, -0.012945513450903579, -0.011895203641514331, -0.010742200656774326, -0.009516366668343714, -0.0082494501326219, -0.006974263522403452, -0.005723833501068315, -0.004530545549348415, -0.003425305198387983, -0.0024367375927208577, -0.00159044611406315, -0.0009083492671756406, -0.0004081130021037321, -0.00010269317535076891, 0.0],
        },
        "q7.xy.-x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 1.2576286848759702e-20, 4.997942817167536e-20, 1.1124070225544932e-19, 1.9477347428037827e-19, 2.984142893287624e-19, 4.19478904730863e-19, 5.548318105400819e-19, 7.009674375935694e-19, 8.541009499121524e-19, 1.0102662699641118e-18, 1.1654187979899686e-18, 1.315540165011727e-18, 1.4567423064786474e-18, 1.5853681610968075e-18, 1.6980863867956497e-18, 1.791977640737733e-18, 1.8646101887647636e-18, 1.9141028860349623e-18, 1.9391738976863488e-18, 1.939173897686349e-18, 1.9141028860349623e-18, 1.8646101887647636e-18, 1.7919776407377336e-18, 1.69808638679565e-18, 1.5853681610968075e-18, 1.4567423064786466e-18, 1.3155401650117274e-18, 1.165418797989969e-18, 1.0102662699641118e-18, 8.541009499121533e-19, 7.0096743759357e-19, 5.548318105400824e-19, 4.194789047308633e-19, 2.984142893287625e-19, 1.9477347428037827e-19, 1.1124070225544922e-19, 4.9979428171675257e-20, 1.2576286848759702e-20, 0.0],
        },
        "q7.xy.y180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 1.2576286848759702e-20, 4.997942817167536e-20, 1.1124070225544932e-19, 1.9477347428037827e-19, 2.984142893287624e-19, 4.19478904730863e-19, 5.548318105400819e-19, 7.009674375935694e-19, 8.541009499121524e-19, 1.0102662699641118e-18, 1.1654187979899686e-18, 1.315540165011727e-18, 1.4567423064786474e-18, 1.5853681610968075e-18, 1.6980863867956497e-18, 1.791977640737733e-18, 1.8646101887647636e-18, 1.9141028860349623e-18, 1.9391738976863488e-18, 1.939173897686349e-18, 1.9141028860349623e-18, 1.8646101887647636e-18, 1.7919776407377336e-18, 1.69808638679565e-18, 1.5853681610968075e-18, 1.4567423064786466e-18, 1.3155401650117274e-18, 1.165418797989969e-18, 1.0102662699641118e-18, 8.541009499121533e-19, 7.0096743759357e-19, 5.548318105400824e-19, 4.194789047308633e-19, 2.984142893287625e-19, 1.9477347428037827e-19, 1.1124070225544922e-19, 4.9979428171675257e-20, 1.2576286848759702e-20, 0.0],
        },
        "q7.xy.y180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.00020538635070153783, 0.000816226004207466, 0.001816698534351283, 0.0031808922281263, 0.004873475185441714, 0.006850610396775961, 0.009061091098696824, 0.011447667002136619, 0.01394852704480689, 0.0164989002652438, 0.01903273333668742, 0.021484401313548646, 0.023790407283028676, 0.025891026901807158, 0.027731855225162447, 0.02926521576646226, 0.030451395293124153, 0.03125967237847901, 0.03166911307058455, 0.03166911307058456, 0.03125967237847901, 0.030451395293124156, 0.029265215766462266, 0.027731855225162454, 0.025891026901807158, 0.023790407283028663, 0.021484401313548653, 0.019032733336687428, 0.0164989002652438, 0.013948527044806903, 0.01144766700213663, 0.00906109109869683, 0.006850610396775966, 0.004873475185441715, 0.0031808922281263, 0.0018166985343512812, 0.0008162260042074642, 0.00020538635070153783, 0.0],
        },
        "q7.xy.y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 6.288143424379851e-21, 2.498971408583768e-20, 5.562035112772466e-20, 9.738673714018913e-20, 1.492071446643812e-19, 2.097394523654315e-19, 2.7741590527004096e-19, 3.504837187967847e-19, 4.270504749560762e-19, 5.051331349820559e-19, 5.827093989949843e-19, 6.577700825058635e-19, 7.283711532393237e-19, 7.926840805484037e-19, 8.490431933978248e-19, 8.959888203688666e-19, 9.323050943823818e-19, 9.570514430174812e-19, 9.695869488431744e-19, 9.695869488431746e-19, 9.570514430174812e-19, 9.323050943823818e-19, 8.959888203688668e-19, 8.49043193397825e-19, 7.926840805484037e-19, 7.283711532393233e-19, 6.577700825058637e-19, 5.827093989949845e-19, 5.051331349820559e-19, 4.2705047495607663e-19, 3.50483718796785e-19, 2.774159052700412e-19, 2.0973945236543165e-19, 1.4920714466438126e-19, 9.738673714018913e-20, 5.562035112772461e-20, 2.4989714085837628e-20, 6.288143424379851e-21, 0.0],
        },
        "q7.xy.y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.00010269317535076891, 0.000408113002103733, 0.0009083492671756414, 0.00159044611406315, 0.002436737592720857, 0.0034253051983879805, 0.004530545549348412, 0.0057238335010683095, 0.006974263522403445, 0.0082494501326219, 0.00951636666834371, 0.010742200656774323, 0.011895203641514338, 0.012945513450903579, 0.013865927612581224, 0.01463260788323113, 0.015225697646562076, 0.015629836189239504, 0.015834556535292275, 0.01583455653529228, 0.015629836189239504, 0.015225697646562078, 0.014632607883231133, 0.013865927612581227, 0.012945513450903579, 0.011895203641514331, 0.010742200656774326, 0.009516366668343714, 0.0082494501326219, 0.006974263522403452, 0.005723833501068315, 0.004530545549348415, 0.003425305198387983, 0.0024367375927208577, 0.00159044611406315, 0.0009083492671756406, 0.0004081130021037321, 0.00010269317535076891, 0.0],
        },
        "q7.xy.-y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 6.288143424379851e-21, 2.498971408583768e-20, 5.562035112772466e-20, 9.738673714018913e-20, 1.492071446643812e-19, 2.097394523654315e-19, 2.7741590527004096e-19, 3.504837187967847e-19, 4.270504749560762e-19, 5.051331349820559e-19, 5.827093989949843e-19, 6.577700825058635e-19, 7.283711532393237e-19, 7.926840805484037e-19, 8.490431933978248e-19, 8.959888203688666e-19, 9.323050943823818e-19, 9.570514430174812e-19, 9.695869488431744e-19, 9.695869488431746e-19, 9.570514430174812e-19, 9.323050943823818e-19, 8.959888203688668e-19, 8.49043193397825e-19, 7.926840805484037e-19, 7.283711532393233e-19, 6.577700825058637e-19, 5.827093989949845e-19, 5.051331349820559e-19, 4.2705047495607663e-19, 3.50483718796785e-19, 2.774159052700412e-19, 2.0973945236543165e-19, 1.4920714466438126e-19, 9.738673714018913e-20, 5.562035112772461e-20, 2.4989714085837628e-20, 6.288143424379851e-21, 0.0],
        },
        "q7.xy.-y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.00010269317535076891, -0.000408113002103733, -0.0009083492671756414, -0.00159044611406315, -0.002436737592720857, -0.0034253051983879805, -0.004530545549348412, -0.0057238335010683095, -0.006974263522403445, -0.0082494501326219, -0.00951636666834371, -0.010742200656774323, -0.011895203641514338, -0.012945513450903579, -0.013865927612581224, -0.01463260788323113, -0.015225697646562076, -0.015629836189239504, -0.015834556535292275, -0.01583455653529228, -0.015629836189239504, -0.015225697646562078, -0.014632607883231133, -0.013865927612581227, -0.012945513450903579, -0.011895203641514331, -0.010742200656774326, -0.009516366668343714, -0.0082494501326219, -0.006974263522403452, -0.005723833501068315, -0.004530545549348415, -0.003425305198387983, -0.0024367375927208577, -0.00159044611406315, -0.0009083492671756406, -0.0004081130021037321, -0.00010269317535076891, 0.0],
        },
        "q7.xy.x180_Square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "q7.xy.x180_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q7.xy.x90_Square.wf.I": {
            "type": "constant",
            "sample": 0.05,
        },
        "q7.xy.x90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q7.xy.-x90_Square.wf.I": {
            "type": "constant",
            "sample": -0.125,
        },
        "q7.xy.-x90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q7.xy.y180_Square.wf.I": {
            "type": "constant",
            "sample": -0.11201840403229253,
        },
        "q7.xy.y180_Square.wf.Q": {
            "type": "constant",
            "sample": 0.22349916590013946,
        },
        "q7.xy.y90_Square.wf.I": {
            "type": "constant",
            "sample": -0.056009202016146266,
        },
        "q7.xy.y90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.11174958295006973,
        },
        "q7.xy.-y90_Square.wf.I": {
            "type": "constant",
            "sample": 0.056009202016146266,
        },
        "q7.xy.-y90_Square.wf.Q": {
            "type": "constant",
            "sample": -0.11174958295006973,
        },
        "q7.xy.saturation.wf.I": {
            "type": "constant",
            "sample": 0.007784263341854068,
        },
        "q7.xy.saturation.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q7.xy.cr_q6_q7_Square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "q7.xy.cr_q6_q7_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q7.xy_detuned.zz_q6_q7_Square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "q7.xy_detuned.zz_q6_q7_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q7.resonator.readout.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "q7.resonator.readout.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q7.resonator.const.wf.I": {
            "type": "constant",
            "sample": 0.125,
        },
        "q7.resonator.const.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q8.xy.x180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0008713351703200674, 0.0034627735580602787, 0.007707198270198096, 0.013494680936182852, 0.02067532879499028, 0.029063166838897987, 0.03844095446849734, 0.04856581191010684, 0.05917551067433166, 0.06999526513619665, 0.08074484933849495, 0.09114585469688381, 0.1009289006359776, 0.10984061140475129, 0.11765017837539991, 0.12415533786556042, 0.12918760966144066, 0.13261666056685806, 0.13435367996455982, 0.13435367996455985, 0.13261666056685806, 0.1291876096614407, 0.12415533786556046, 0.11765017837539994, 0.10984061140475129, 0.10092890063597756, 0.09114585469688384, 0.08074484933849498, 0.06999526513619665, 0.05917551067433171, 0.04856581191010688, 0.03844095446849737, 0.029063166838898008, 0.02067532879499029, 0.013494680936182852, 0.007707198270198088, 0.0034627735580602713, 0.0008713351703200674, 0.0],
        },
        "q8.xy.x180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
        },
        "q8.xy.x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0004356675851600337, 0.0017313867790301393, 0.003853599135099048, 0.006747340468091426, 0.01033766439749514, 0.014531583419448994, 0.01922047723424867, 0.02428290595505342, 0.02958775533716583, 0.034997632568098326, 0.040372424669247474, 0.045572927348441906, 0.0504644503179888, 0.054920305702375646, 0.05882508918769996, 0.06207766893278021, 0.06459380483072033, 0.06630833028342903, 0.06717683998227991, 0.06717683998227993, 0.06630833028342903, 0.06459380483072034, 0.06207766893278023, 0.05882508918769997, 0.054920305702375646, 0.05046445031798878, 0.04557292734844192, 0.04037242466924749, 0.034997632568098326, 0.029587755337165855, 0.02428290595505344, 0.019220477234248686, 0.014531583419449004, 0.010337664397495144, 0.006747340468091426, 0.003853599135099044, 0.0017313867790301357, 0.0004356675851600337, 0.0],
        },
        "q8.xy.x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
        },
        "q8.xy.-x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -0.0004356675851600337, -0.0017313867790301393, -0.003853599135099048, -0.006747340468091426, -0.01033766439749514, -0.014531583419448994, -0.01922047723424867, -0.02428290595505342, -0.02958775533716583, -0.034997632568098326, -0.040372424669247474, -0.045572927348441906, -0.0504644503179888, -0.054920305702375646, -0.05882508918769996, -0.06207766893278021, -0.06459380483072033, -0.06630833028342903, -0.06717683998227991, -0.06717683998227993, -0.06630833028342903, -0.06459380483072034, -0.06207766893278023, -0.05882508918769997, -0.054920305702375646, -0.05046445031798878, -0.04557292734844192, -0.04037242466924749, -0.034997632568098326, -0.029587755337165855, -0.02428290595505344, -0.019220477234248686, -0.014531583419449004, -0.010337664397495144, -0.006747340468091426, -0.003853599135099044, -0.0017313867790301357, -0.0004356675851600337, 0.0],
        },
        "q8.xy.-x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 5.335389136584922e-20, 2.1203372770253059e-19, 4.719297845996058e-19, 8.263108907005569e-19, 1.2659987615051976e-18, 1.779605712117096e-18, 2.3538295923007203e-18, 2.9737983051852373e-18, 3.623454986761515e-18, 4.285973870225678e-18, 4.9441960645011556e-18, 5.581073960504425e-18, 6.180112755265562e-18, 6.7257976586608465e-18, 7.203995718327433e-18, 7.602321855705837e-18, 7.91045963306905e-18, 8.120428443840687e-18, 8.226790206113303e-18, 8.226790206113305e-18, 8.120428443840687e-18, 7.910459633069051e-18, 7.60232185570584e-18, 7.203995718327435e-18, 6.7257976586608465e-18, 6.180112755265559e-18, 5.5810739605044276e-18, 4.944196064501158e-18, 4.285973870225678e-18, 3.623454986761518e-18, 2.9737983051852396e-18, 2.3538295923007226e-18, 1.779605712117097e-18, 1.265998761505198e-18, 8.263108907005569e-19, 4.719297845996053e-19, 2.1203372770253013e-19, 5.335389136584922e-20, 0.0],
        },
        "q8.xy.y180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 5.335389136584922e-20, 2.1203372770253059e-19, 4.719297845996058e-19, 8.263108907005569e-19, 1.2659987615051976e-18, 1.779605712117096e-18, 2.3538295923007203e-18, 2.9737983051852373e-18, 3.623454986761515e-18, 4.285973870225678e-18, 4.9441960645011556e-18, 5.581073960504425e-18, 6.180112755265562e-18, 6.7257976586608465e-18, 7.203995718327433e-18, 7.602321855705837e-18, 7.91045963306905e-18, 8.120428443840687e-18, 8.226790206113303e-18, 8.226790206113305e-18, 8.120428443840687e-18, 7.910459633069051e-18, 7.60232185570584e-18, 7.203995718327435e-18, 6.7257976586608465e-18, 6.180112755265559e-18, 5.5810739605044276e-18, 4.944196064501158e-18, 4.285973870225678e-18, 3.623454986761518e-18, 2.9737983051852396e-18, 2.3538295923007226e-18, 1.779605712117097e-18, 1.265998761505198e-18, 8.263108907005569e-19, 4.719297845996053e-19, 2.1203372770253013e-19, 5.335389136584922e-20, 0.0],
        },
        "q8.xy.y180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0008713351703200674, 0.0034627735580602787, 0.007707198270198096, 0.013494680936182852, 0.02067532879499028, 0.029063166838897987, 0.03844095446849734, 0.04856581191010684, 0.05917551067433166, 0.06999526513619665, 0.08074484933849495, 0.09114585469688381, 0.1009289006359776, 0.10984061140475129, 0.11765017837539991, 0.12415533786556042, 0.12918760966144066, 0.13261666056685806, 0.13435367996455982, 0.13435367996455985, 0.13261666056685806, 0.1291876096614407, 0.12415533786556046, 0.11765017837539994, 0.10984061140475129, 0.10092890063597756, 0.09114585469688384, 0.08074484933849498, 0.06999526513619665, 0.05917551067433171, 0.04856581191010688, 0.03844095446849737, 0.029063166838898008, 0.02067532879499029, 0.013494680936182852, 0.007707198270198088, 0.0034627735580602713, 0.0008713351703200674, 0.0],
        },
        "q8.xy.y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 2.667694568292461e-20, 1.0601686385126529e-19, 2.359648922998029e-19, 4.1315544535027846e-19, 6.329993807525988e-19, 8.89802856058548e-19, 1.1769147961503601e-18, 1.4868991525926186e-18, 1.8117274933807573e-18, 2.142986935112839e-18, 2.4720980322505778e-18, 2.7905369802522126e-18, 3.090056377632781e-18, 3.3628988293304232e-18, 3.6019978591637166e-18, 3.801160927852919e-18, 3.955229816534525e-18, 4.060214221920343e-18, 4.113395103056652e-18, 4.1133951030566524e-18, 4.060214221920343e-18, 3.955229816534526e-18, 3.80116092785292e-18, 3.601997859163717e-18, 3.3628988293304232e-18, 3.0900563776327795e-18, 2.7905369802522138e-18, 2.472098032250579e-18, 2.142986935112839e-18, 1.811727493380759e-18, 1.4868991525926198e-18, 1.1769147961503613e-18, 8.898028560585485e-19, 6.32999380752599e-19, 4.1315544535027846e-19, 2.3596489229980265e-19, 1.0601686385126507e-19, 2.667694568292461e-20, 0.0],
        },
        "q8.xy.y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0004356675851600337, 0.0017313867790301393, 0.003853599135099048, 0.006747340468091426, 0.01033766439749514, 0.014531583419448994, 0.01922047723424867, 0.02428290595505342, 0.02958775533716583, 0.034997632568098326, 0.040372424669247474, 0.045572927348441906, 0.0504644503179888, 0.054920305702375646, 0.05882508918769996, 0.06207766893278021, 0.06459380483072033, 0.06630833028342903, 0.06717683998227991, 0.06717683998227993, 0.06630833028342903, 0.06459380483072034, 0.06207766893278023, 0.05882508918769997, 0.054920305702375646, 0.05046445031798878, 0.04557292734844192, 0.04037242466924749, 0.034997632568098326, 0.029587755337165855, 0.02428290595505344, 0.019220477234248686, 0.014531583419449004, 0.010337664397495144, 0.006747340468091426, 0.003853599135099044, 0.0017313867790301357, 0.0004356675851600337, 0.0],
        },
        "q8.xy.-y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 2.667694568292461e-20, 1.0601686385126529e-19, 2.359648922998029e-19, 4.1315544535027846e-19, 6.329993807525988e-19, 8.89802856058548e-19, 1.1769147961503601e-18, 1.4868991525926186e-18, 1.8117274933807573e-18, 2.142986935112839e-18, 2.4720980322505778e-18, 2.7905369802522126e-18, 3.090056377632781e-18, 3.3628988293304232e-18, 3.6019978591637166e-18, 3.801160927852919e-18, 3.955229816534525e-18, 4.060214221920343e-18, 4.113395103056652e-18, 4.1133951030566524e-18, 4.060214221920343e-18, 3.955229816534526e-18, 3.80116092785292e-18, 3.601997859163717e-18, 3.3628988293304232e-18, 3.0900563776327795e-18, 2.7905369802522138e-18, 2.472098032250579e-18, 2.142986935112839e-18, 1.811727493380759e-18, 1.4868991525926198e-18, 1.1769147961503613e-18, 8.898028560585485e-19, 6.32999380752599e-19, 4.1315544535027846e-19, 2.3596489229980265e-19, 1.0601686385126507e-19, 2.667694568292461e-20, 0.0],
        },
        "q8.xy.-y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.0004356675851600337, -0.0017313867790301393, -0.003853599135099048, -0.006747340468091426, -0.01033766439749514, -0.014531583419448994, -0.01922047723424867, -0.02428290595505342, -0.02958775533716583, -0.034997632568098326, -0.040372424669247474, -0.045572927348441906, -0.0504644503179888, -0.054920305702375646, -0.05882508918769996, -0.06207766893278021, -0.06459380483072033, -0.06630833028342903, -0.06717683998227991, -0.06717683998227993, -0.06630833028342903, -0.06459380483072034, -0.06207766893278023, -0.05882508918769997, -0.054920305702375646, -0.05046445031798878, -0.04557292734844192, -0.04037242466924749, -0.034997632568098326, -0.029587755337165855, -0.02428290595505344, -0.019220477234248686, -0.014531583419449004, -0.010337664397495144, -0.006747340468091426, -0.003853599135099044, -0.0017313867790301357, -0.0004356675851600337, 0.0],
        },
        "q8.xy.x180_Square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "q8.xy.x180_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q8.xy.x90_Square.wf.I": {
            "type": "constant",
            "sample": 0.05,
        },
        "q8.xy.x90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q8.xy.-x90_Square.wf.I": {
            "type": "constant",
            "sample": -0.125,
        },
        "q8.xy.-x90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q8.xy.y180_Square.wf.I": {
            "type": "constant",
            "sample": -0.11201840403229253,
        },
        "q8.xy.y180_Square.wf.Q": {
            "type": "constant",
            "sample": 0.22349916590013946,
        },
        "q8.xy.y90_Square.wf.I": {
            "type": "constant",
            "sample": -0.056009202016146266,
        },
        "q8.xy.y90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.11174958295006973,
        },
        "q8.xy.-y90_Square.wf.I": {
            "type": "constant",
            "sample": 0.056009202016146266,
        },
        "q8.xy.-y90_Square.wf.Q": {
            "type": "constant",
            "sample": -0.11174958295006973,
        },
        "q8.xy.saturation.wf.I": {
            "type": "constant",
            "sample": 0.043017810278935274,
        },
        "q8.xy.saturation.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q8.xy.cr_q7_q8_Square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "q8.xy.cr_q7_q8_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q8.xy_detuned.zz_q7_q8_Square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "q8.xy_detuned.zz_q7_q8_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q8.resonator.readout.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "q8.resonator.readout.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q8.resonator.const.wf.I": {
            "type": "constant",
            "sample": 0.125,
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
        "zz_q1_q2.square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "zz_q1_q2.square.wf.Q": {
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
        "zz_q2_q3.square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "zz_q2_q3.square.wf.Q": {
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
        "zz_q3_q4.square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "zz_q3_q4.square.wf.Q": {
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
        "zz_q4_q5.square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "zz_q4_q5.square.wf.Q": {
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
        "zz_q5_q6.square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "zz_q5_q6.square.wf.Q": {
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
        "zz_q6_q7.square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "zz_q6_q7.square.wf.Q": {
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
        "zz_q7_q8.square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "zz_q7_q8.square.wf.Q": {
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
        "zz_q8_q1.square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "zz_q8_q1.square.wf.Q": {
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
            "cosine": [(-0.9425588238789202, 2000)],
            "sine": [(0.33404021244153614, 2000)],
        },
        "q1.resonator.readout.iw2": {
            "cosine": [(-0.33404021244153614, 2000)],
            "sine": [(-0.9425588238789202, 2000)],
        },
        "q1.resonator.readout.iw3": {
            "cosine": [(0.33404021244153614, 2000)],
            "sine": [(0.9425588238789202, 2000)],
        },
        "q2.resonator.readout.iw1": {
            "cosine": [(-0.9572310893844667, 2000)],
            "sine": [(0.2893244571684653, 2000)],
        },
        "q2.resonator.readout.iw2": {
            "cosine": [(-0.2893244571684653, 2000)],
            "sine": [(-0.9572310893844667, 2000)],
        },
        "q2.resonator.readout.iw3": {
            "cosine": [(0.2893244571684653, 2000)],
            "sine": [(0.9572310893844667, 2000)],
        },
        "q3.resonator.readout.iw1": {
            "cosine": [(0.1345356924135238, 2000)],
            "sine": [(-0.9909087483047133, 2000)],
        },
        "q3.resonator.readout.iw2": {
            "cosine": [(0.9909087483047133, 2000)],
            "sine": [(0.1345356924135238, 2000)],
        },
        "q3.resonator.readout.iw3": {
            "cosine": [(-0.9909087483047133, 2000)],
            "sine": [(-0.1345356924135238, 2000)],
        },
        "q4.resonator.readout.iw1": {
            "cosine": [(-0.8679447933694215, 2000)],
            "sine": [(0.49666068463581065, 2000)],
        },
        "q4.resonator.readout.iw2": {
            "cosine": [(-0.49666068463581065, 2000)],
            "sine": [(-0.8679447933694215, 2000)],
        },
        "q4.resonator.readout.iw3": {
            "cosine": [(0.49666068463581065, 2000)],
            "sine": [(0.8679447933694215, 2000)],
        },
        "q5.resonator.readout.iw1": {
            "cosine": [(-0.7898172096237304, 2000)],
            "sine": [(-0.6133422987061827, 2000)],
        },
        "q5.resonator.readout.iw2": {
            "cosine": [(0.6133422987061827, 2000)],
            "sine": [(-0.7898172096237304, 2000)],
        },
        "q5.resonator.readout.iw3": {
            "cosine": [(-0.6133422987061827, 2000)],
            "sine": [(0.7898172096237304, 2000)],
        },
        "q6.resonator.readout.iw1": {
            "cosine": [(-0.9042233768894555, 2000)],
            "sine": [(0.4270598139448731, 2000)],
        },
        "q6.resonator.readout.iw2": {
            "cosine": [(-0.4270598139448731, 2000)],
            "sine": [(-0.9042233768894555, 2000)],
        },
        "q6.resonator.readout.iw3": {
            "cosine": [(0.4270598139448731, 2000)],
            "sine": [(0.9042233768894555, 2000)],
        },
        "q7.resonator.readout.iw1": {
            "cosine": [(-0.8759906098241979, 2000)],
            "sine": [(0.4823281574818433, 2000)],
        },
        "q7.resonator.readout.iw2": {
            "cosine": [(-0.4823281574818433, 2000)],
            "sine": [(-0.8759906098241979, 2000)],
        },
        "q7.resonator.readout.iw3": {
            "cosine": [(0.4823281574818433, 2000)],
            "sine": [(0.8759906098241979, 2000)],
        },
        "q8.resonator.readout.iw1": {
            "cosine": [(0.7989098841294603, 2000)],
            "sine": [(0.601450743652589, 2000)],
        },
        "q8.resonator.readout.iw2": {
            "cosine": [(-0.601450743652589, 2000)],
            "sine": [(0.7989098841294603, 2000)],
        },
        "q8.resonator.readout.iw3": {
            "cosine": [(0.601450743652589, 2000)],
            "sine": [(-0.7989098841294603, 2000)],
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
                "2": {
                    "type": "MW",
                    "analog_outputs": {
                        "1": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": -14,
                            "band": 3,
                            "delay": 0,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 9983000000.0,
                                },
                            },
                        },
                        "2": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": 1,
                            "band": 1,
                            "delay": 0,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 4551000000.0,
                                },
                            },
                        },
                        "8": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": -14,
                            "band": 3,
                            "delay": 0,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 9572000000.0,
                                },
                            },
                        },
                        "3": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": 1,
                            "band": 1,
                            "delay": 0,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 4320000000.0,
                                },
                            },
                        },
                    },
                    "analog_inputs": {
                        "1": {
                            "band": 3,
                            "shareable": False,
                            "gain_db": 0,
                            "sampling_rate": 1000000000.0,
                            "downconverter_frequency": 9983000000.0,
                        },
                        "2": {
                            "band": 3,
                            "shareable": False,
                            "gain_db": 0,
                            "sampling_rate": 1000000000.0,
                            "downconverter_frequency": 9572000000.0,
                        },
                    },
                },
                "3": {
                    "type": "MW",
                    "analog_outputs": {
                        "1": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": -14,
                            "band": 3,
                            "delay": 0,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 9896000000.0,
                                },
                            },
                        },
                        "2": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": 1,
                            "band": 1,
                            "delay": 0,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 4303000000.0,
                                },
                            },
                        },
                        "8": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": -14,
                            "band": 3,
                            "delay": 0,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 9374000000.0,
                                },
                            },
                        },
                        "3": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": 1,
                            "band": 1,
                            "delay": 0,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 4053000000.0,
                                },
                            },
                        },
                    },
                    "analog_inputs": {
                        "1": {
                            "band": 3,
                            "shareable": False,
                            "gain_db": 0,
                            "sampling_rate": 1000000000.0,
                            "downconverter_frequency": 9896000000.0,
                        },
                        "2": {
                            "band": 3,
                            "shareable": False,
                            "gain_db": 0,
                            "sampling_rate": 1000000000.0,
                            "downconverter_frequency": 9374000000.0,
                        },
                    },
                },
                "5": {
                    "type": "MW",
                    "analog_outputs": {
                        "1": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": -14,
                            "band": 3,
                            "delay": 0,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 9697000000.0,
                                },
                            },
                        },
                        "2": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": 1,
                            "band": 1,
                            "delay": 0,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 4461000000.0,
                                },
                            },
                        },
                        "8": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": -14,
                            "band": 3,
                            "delay": 0,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 9275000000.0,
                                },
                            },
                        },
                        "3": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": 1,
                            "band": 1,
                            "delay": 0,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 4406000000.0,
                                },
                            },
                        },
                    },
                    "analog_inputs": {
                        "1": {
                            "band": 3,
                            "shareable": False,
                            "gain_db": 0,
                            "sampling_rate": 1000000000.0,
                            "downconverter_frequency": 9697000000.0,
                        },
                        "2": {
                            "band": 3,
                            "shareable": False,
                            "gain_db": 0,
                            "sampling_rate": 1000000000.0,
                            "downconverter_frequency": 9275000000.0,
                        },
                    },
                },
                "7": {
                    "type": "MW",
                    "analog_outputs": {
                        "1": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": -14,
                            "band": 3,
                            "delay": 0,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 9792000000.0,
                                },
                            },
                        },
                        "2": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": 1,
                            "band": 1,
                            "delay": 0,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 4464000000.0,
                                },
                            },
                        },
                        "8": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": -14,
                            "band": 3,
                            "delay": 0,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 9468000000.0,
                                },
                            },
                        },
                        "3": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": 1,
                            "band": 1,
                            "delay": 0,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 4268000000.0,
                                },
                            },
                        },
                    },
                    "analog_inputs": {
                        "1": {
                            "band": 3,
                            "shareable": False,
                            "gain_db": 0,
                            "sampling_rate": 1000000000.0,
                            "downconverter_frequency": 9792000000.0,
                        },
                        "2": {
                            "band": 3,
                            "shareable": False,
                            "gain_db": 0,
                            "sampling_rate": 1000000000.0,
                            "downconverter_frequency": 9468000000.0,
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
                "x180_DragCosine": "q1.xy.x180_DragCosine.pulse",
                "x90_DragCosine": "q1.xy.x90_DragCosine.pulse",
                "-x90_DragCosine": "q1.xy.-x90_DragCosine.pulse",
                "y180_DragCosine": "q1.xy.y180_DragCosine.pulse",
                "y90_DragCosine": "q1.xy.y90_DragCosine.pulse",
                "-y90_DragCosine": "q1.xy.-y90_DragCosine.pulse",
                "x180_Square": "q1.xy.x180_Square.pulse",
                "x90_Square": "q1.xy.x90_Square.pulse",
                "-x90_Square": "q1.xy.-x90_Square.pulse",
                "y180_Square": "q1.xy.y180_Square.pulse",
                "y90_Square": "q1.xy.y90_Square.pulse",
                "-y90_Square": "q1.xy.-y90_Square.pulse",
                "x180": "q1.xy.x180_DragCosine.pulse",
                "x90": "q1.xy.x90_DragCosine.pulse",
                "-x90": "q1.xy.-x90_DragCosine.pulse",
                "y180": "q1.xy.y180_DragCosine.pulse",
                "y90": "q1.xy.y90_DragCosine.pulse",
                "-y90": "q1.xy.-y90_DragCosine.pulse",
                "saturation": "q1.xy.saturation.pulse",
                "cr_q8_q1_Square": "q1.xy.cr_q8_q1_Square.pulse",
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
            "MWInput": {
                "port": ('con1', 2, 2),
                "upconverter": 1,
            },
            "intermediate_frequency": 51500000.0,
        },
        "q1.xy_detuned": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "zz_q8_q1_Square": "q1.xy_detuned.zz_q8_q1_Square.pulse",
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
            "MWInput": {
                "port": ('con1', 2, 2),
                "upconverter": 1,
            },
            "intermediate_frequency": -210000000.0,
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
            "thread": "",
            "MWInput": {
                "port": ('con1', 2, 1),
                "upconverter": 1,
            },
            "MWOutput": {
                "port": ('con1', 2, 1),
            },
            "smearing": 0,
            "time_of_flight": 304,
            "intermediate_frequency": 50113489.0,
        },
        "q2.xy": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "x180_DragCosine": "q2.xy.x180_DragCosine.pulse",
                "x90_DragCosine": "q2.xy.x90_DragCosine.pulse",
                "-x90_DragCosine": "q2.xy.-x90_DragCosine.pulse",
                "y180_DragCosine": "q2.xy.y180_DragCosine.pulse",
                "y90_DragCosine": "q2.xy.y90_DragCosine.pulse",
                "-y90_DragCosine": "q2.xy.-y90_DragCosine.pulse",
                "x180_Square": "q2.xy.x180_Square.pulse",
                "x90_Square": "q2.xy.x90_Square.pulse",
                "-x90_Square": "q2.xy.-x90_Square.pulse",
                "y180_Square": "q2.xy.y180_Square.pulse",
                "y90_Square": "q2.xy.y90_Square.pulse",
                "-y90_Square": "q2.xy.-y90_Square.pulse",
                "x180": "q2.xy.x180_DragCosine.pulse",
                "x90": "q2.xy.x90_DragCosine.pulse",
                "-x90": "q2.xy.-x90_DragCosine.pulse",
                "y180": "q2.xy.y180_DragCosine.pulse",
                "y90": "q2.xy.y90_DragCosine.pulse",
                "-y90": "q2.xy.-y90_DragCosine.pulse",
                "saturation": "q2.xy.saturation.pulse",
                "cr_q1_q2_Square": "q2.xy.cr_q1_q2_Square.pulse",
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
            "MWInput": {
                "port": ('con1', 2, 3),
                "upconverter": 1,
            },
            "intermediate_frequency": 51000000.0,
        },
        "q2.xy_detuned": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "zz_q1_q2_Square": "q2.xy_detuned.zz_q1_q2_Square.pulse",
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
            "MWInput": {
                "port": ('con1', 2, 3),
                "upconverter": 1,
            },
            "intermediate_frequency": -210000000.0,
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
            "thread": "",
            "MWInput": {
                "port": ('con1', 2, 8),
                "upconverter": 1,
            },
            "MWOutput": {
                "port": ('con1', 2, 2),
            },
            "smearing": 0,
            "time_of_flight": 304,
            "intermediate_frequency": 49013812.0,
        },
        "q3.xy": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "x180_DragCosine": "q3.xy.x180_DragCosine.pulse",
                "x90_DragCosine": "q3.xy.x90_DragCosine.pulse",
                "-x90_DragCosine": "q3.xy.-x90_DragCosine.pulse",
                "y180_DragCosine": "q3.xy.y180_DragCosine.pulse",
                "y90_DragCosine": "q3.xy.y90_DragCosine.pulse",
                "-y90_DragCosine": "q3.xy.-y90_DragCosine.pulse",
                "x180_Square": "q3.xy.x180_Square.pulse",
                "x90_Square": "q3.xy.x90_Square.pulse",
                "-x90_Square": "q3.xy.-x90_Square.pulse",
                "y180_Square": "q3.xy.y180_Square.pulse",
                "y90_Square": "q3.xy.y90_Square.pulse",
                "-y90_Square": "q3.xy.-y90_Square.pulse",
                "x180": "q3.xy.x180_DragCosine.pulse",
                "x90": "q3.xy.x90_DragCosine.pulse",
                "-x90": "q3.xy.-x90_DragCosine.pulse",
                "y180": "q3.xy.y180_DragCosine.pulse",
                "y90": "q3.xy.y90_DragCosine.pulse",
                "-y90": "q3.xy.-y90_DragCosine.pulse",
                "saturation": "q3.xy.saturation.pulse",
                "cr_q2_q3_Square": "q3.xy.cr_q2_q3_Square.pulse",
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
            "MWInput": {
                "port": ('con1', 3, 2),
                "upconverter": 1,
            },
            "intermediate_frequency": 48000000.0,
        },
        "q3.xy_detuned": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "zz_q2_q3_Square": "q3.xy_detuned.zz_q2_q3_Square.pulse",
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
            "MWInput": {
                "port": ('con1', 3, 2),
                "upconverter": 1,
            },
            "intermediate_frequency": -210000000.0,
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
            "thread": "",
            "MWInput": {
                "port": ('con1', 3, 1),
                "upconverter": 1,
            },
            "MWOutput": {
                "port": ('con1', 3, 1),
            },
            "smearing": 0,
            "time_of_flight": 304,
            "intermediate_frequency": 50146943.0,
        },
        "q4.xy": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "x180_DragCosine": "q4.xy.x180_DragCosine.pulse",
                "x90_DragCosine": "q4.xy.x90_DragCosine.pulse",
                "-x90_DragCosine": "q4.xy.-x90_DragCosine.pulse",
                "y180_DragCosine": "q4.xy.y180_DragCosine.pulse",
                "y90_DragCosine": "q4.xy.y90_DragCosine.pulse",
                "-y90_DragCosine": "q4.xy.-y90_DragCosine.pulse",
                "x180_Square": "q4.xy.x180_Square.pulse",
                "x90_Square": "q4.xy.x90_Square.pulse",
                "-x90_Square": "q4.xy.-x90_Square.pulse",
                "y180_Square": "q4.xy.y180_Square.pulse",
                "y90_Square": "q4.xy.y90_Square.pulse",
                "-y90_Square": "q4.xy.-y90_Square.pulse",
                "x180": "q4.xy.x180_DragCosine.pulse",
                "x90": "q4.xy.x90_DragCosine.pulse",
                "-x90": "q4.xy.-x90_DragCosine.pulse",
                "y180": "q4.xy.y180_DragCosine.pulse",
                "y90": "q4.xy.y90_DragCosine.pulse",
                "-y90": "q4.xy.-y90_DragCosine.pulse",
                "saturation": "q4.xy.saturation.pulse",
                "cr_q3_q4_Square": "q4.xy.cr_q3_q4_Square.pulse",
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
            "MWInput": {
                "port": ('con1', 3, 3),
                "upconverter": 1,
            },
            "intermediate_frequency": 50750000.0,
        },
        "q4.xy_detuned": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "zz_q3_q4_Square": "q4.xy_detuned.zz_q3_q4_Square.pulse",
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
            "MWInput": {
                "port": ('con1', 3, 3),
                "upconverter": 1,
            },
            "intermediate_frequency": -210000000.0,
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
            "thread": "",
            "MWInput": {
                "port": ('con1', 3, 8),
                "upconverter": 1,
            },
            "MWOutput": {
                "port": ('con1', 3, 2),
            },
            "smearing": 0,
            "time_of_flight": 24,
            "intermediate_frequency": 48881765.0,
        },
        "q5.xy": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "x180_DragCosine": "q5.xy.x180_DragCosine.pulse",
                "x90_DragCosine": "q5.xy.x90_DragCosine.pulse",
                "-x90_DragCosine": "q5.xy.-x90_DragCosine.pulse",
                "y180_DragCosine": "q5.xy.y180_DragCosine.pulse",
                "y90_DragCosine": "q5.xy.y90_DragCosine.pulse",
                "-y90_DragCosine": "q5.xy.-y90_DragCosine.pulse",
                "x180_Square": "q5.xy.x180_Square.pulse",
                "x90_Square": "q5.xy.x90_Square.pulse",
                "-x90_Square": "q5.xy.-x90_Square.pulse",
                "y180_Square": "q5.xy.y180_Square.pulse",
                "y90_Square": "q5.xy.y90_Square.pulse",
                "-y90_Square": "q5.xy.-y90_Square.pulse",
                "x180": "q5.xy.x180_DragCosine.pulse",
                "x90": "q5.xy.x90_DragCosine.pulse",
                "-x90": "q5.xy.-x90_DragCosine.pulse",
                "y180": "q5.xy.y180_DragCosine.pulse",
                "y90": "q5.xy.y90_DragCosine.pulse",
                "-y90": "q5.xy.-y90_DragCosine.pulse",
                "saturation": "q5.xy.saturation.pulse",
                "cr_q4_q5_Square": "q5.xy.cr_q4_q5_Square.pulse",
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
            "MWInput": {
                "port": ('con1', 5, 2),
                "upconverter": 1,
            },
            "intermediate_frequency": 50250000.0,
        },
        "q5.xy_detuned": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "zz_q4_q5_Square": "q5.xy_detuned.zz_q4_q5_Square.pulse",
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
            "MWInput": {
                "port": ('con1', 5, 2),
                "upconverter": 1,
            },
            "intermediate_frequency": -210000000.0,
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
            "thread": "",
            "MWInput": {
                "port": ('con1', 5, 1),
                "upconverter": 1,
            },
            "MWOutput": {
                "port": ('con1', 5, 1),
            },
            "smearing": 0,
            "time_of_flight": 304,
            "intermediate_frequency": 50216992.0,
        },
        "q6.xy": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "x180_DragCosine": "q6.xy.x180_DragCosine.pulse",
                "x90_DragCosine": "q6.xy.x90_DragCosine.pulse",
                "-x90_DragCosine": "q6.xy.-x90_DragCosine.pulse",
                "y180_DragCosine": "q6.xy.y180_DragCosine.pulse",
                "y90_DragCosine": "q6.xy.y90_DragCosine.pulse",
                "-y90_DragCosine": "q6.xy.-y90_DragCosine.pulse",
                "x180_Square": "q6.xy.x180_Square.pulse",
                "x90_Square": "q6.xy.x90_Square.pulse",
                "-x90_Square": "q6.xy.-x90_Square.pulse",
                "y180_Square": "q6.xy.y180_Square.pulse",
                "y90_Square": "q6.xy.y90_Square.pulse",
                "-y90_Square": "q6.xy.-y90_Square.pulse",
                "x180": "q6.xy.x180_DragCosine.pulse",
                "x90": "q6.xy.x90_DragCosine.pulse",
                "-x90": "q6.xy.-x90_DragCosine.pulse",
                "y180": "q6.xy.y180_DragCosine.pulse",
                "y90": "q6.xy.y90_DragCosine.pulse",
                "-y90": "q6.xy.-y90_DragCosine.pulse",
                "saturation": "q6.xy.saturation.pulse",
                "cr_q5_q6_Square": "q6.xy.cr_q5_q6_Square.pulse",
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
            "MWInput": {
                "port": ('con1', 5, 3),
                "upconverter": 1,
            },
            "intermediate_frequency": 51250000.0,
        },
        "q6.xy_detuned": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "zz_q5_q6_Square": "q6.xy_detuned.zz_q5_q6_Square.pulse",
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
            "MWInput": {
                "port": ('con1', 5, 3),
                "upconverter": 1,
            },
            "intermediate_frequency": -210000000.0,
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
            "thread": "",
            "MWInput": {
                "port": ('con1', 5, 8),
                "upconverter": 1,
            },
            "MWOutput": {
                "port": ('con1', 5, 2),
            },
            "smearing": 0,
            "time_of_flight": 24,
            "intermediate_frequency": 49625230.0,
        },
        "q7.xy": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "x180_DragCosine": "q7.xy.x180_DragCosine.pulse",
                "x90_DragCosine": "q7.xy.x90_DragCosine.pulse",
                "-x90_DragCosine": "q7.xy.-x90_DragCosine.pulse",
                "y180_DragCosine": "q7.xy.y180_DragCosine.pulse",
                "y90_DragCosine": "q7.xy.y90_DragCosine.pulse",
                "-y90_DragCosine": "q7.xy.-y90_DragCosine.pulse",
                "x180_Square": "q7.xy.x180_Square.pulse",
                "x90_Square": "q7.xy.x90_Square.pulse",
                "-x90_Square": "q7.xy.-x90_Square.pulse",
                "y180_Square": "q7.xy.y180_Square.pulse",
                "y90_Square": "q7.xy.y90_Square.pulse",
                "-y90_Square": "q7.xy.-y90_Square.pulse",
                "x180": "q7.xy.x180_DragCosine.pulse",
                "x90": "q7.xy.x90_DragCosine.pulse",
                "-x90": "q7.xy.-x90_DragCosine.pulse",
                "y180": "q7.xy.y180_DragCosine.pulse",
                "y90": "q7.xy.y90_DragCosine.pulse",
                "-y90": "q7.xy.-y90_DragCosine.pulse",
                "saturation": "q7.xy.saturation.pulse",
                "cr_q6_q7_Square": "q7.xy.cr_q6_q7_Square.pulse",
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
            "MWInput": {
                "port": ('con1', 7, 2),
                "upconverter": 1,
            },
            "intermediate_frequency": 51250000.0,
        },
        "q7.xy_detuned": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "zz_q6_q7_Square": "q7.xy_detuned.zz_q6_q7_Square.pulse",
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
            "MWInput": {
                "port": ('con1', 7, 2),
                "upconverter": 1,
            },
            "intermediate_frequency": -210000000.0,
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
            "thread": "",
            "MWInput": {
                "port": ('con1', 7, 1),
                "upconverter": 1,
            },
            "MWOutput": {
                "port": ('con1', 7, 1),
            },
            "smearing": 0,
            "time_of_flight": 304,
            "intermediate_frequency": 49550000.0,
        },
        "q8.xy": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "x180_DragCosine": "q8.xy.x180_DragCosine.pulse",
                "x90_DragCosine": "q8.xy.x90_DragCosine.pulse",
                "-x90_DragCosine": "q8.xy.-x90_DragCosine.pulse",
                "y180_DragCosine": "q8.xy.y180_DragCosine.pulse",
                "y90_DragCosine": "q8.xy.y90_DragCosine.pulse",
                "-y90_DragCosine": "q8.xy.-y90_DragCosine.pulse",
                "x180_Square": "q8.xy.x180_Square.pulse",
                "x90_Square": "q8.xy.x90_Square.pulse",
                "-x90_Square": "q8.xy.-x90_Square.pulse",
                "y180_Square": "q8.xy.y180_Square.pulse",
                "y90_Square": "q8.xy.y90_Square.pulse",
                "-y90_Square": "q8.xy.-y90_Square.pulse",
                "x180": "q8.xy.x180_DragCosine.pulse",
                "x90": "q8.xy.x90_DragCosine.pulse",
                "-x90": "q8.xy.-x90_DragCosine.pulse",
                "y180": "q8.xy.y180_DragCosine.pulse",
                "y90": "q8.xy.y90_DragCosine.pulse",
                "-y90": "q8.xy.-y90_DragCosine.pulse",
                "saturation": "q8.xy.saturation.pulse",
                "cr_q7_q8_Square": "q8.xy.cr_q7_q8_Square.pulse",
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
            "MWInput": {
                "port": ('con1', 7, 3),
                "upconverter": 1,
            },
            "intermediate_frequency": 51000000.0,
        },
        "q8.xy_detuned": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "zz_q7_q8_Square": "q8.xy_detuned.zz_q7_q8_Square.pulse",
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
            "MWInput": {
                "port": ('con1', 7, 3),
                "upconverter": 1,
            },
            "intermediate_frequency": -210000000.0,
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
            "thread": "",
            "MWInput": {
                "port": ('con1', 7, 8),
                "upconverter": 1,
            },
            "MWOutput": {
                "port": ('con1', 7, 2),
            },
            "smearing": 0,
            "time_of_flight": 24,
            "intermediate_frequency": 49700000.0,
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
            "thread": "q1",
            "MWInput": {
                "port": ('con1', 2, 2),
                "upconverter": 1,
            },
        },
        "zz_q1_q2": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "square": "zz_q1_q2.square.pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "thread": "q1",
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
            "thread": "q2",
            "MWInput": {
                "port": ('con1', 2, 3),
                "upconverter": 1,
            },
        },
        "zz_q2_q3": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "square": "zz_q2_q3.square.pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "thread": "q2",
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
            "thread": "q3",
            "MWInput": {
                "port": ('con1', 3, 2),
                "upconverter": 1,
            },
        },
        "zz_q3_q4": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "square": "zz_q3_q4.square.pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "thread": "q3",
            "MWInput": {
                "port": ('con1', 3, 2),
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
            "thread": "q4",
            "MWInput": {
                "port": ('con1', 3, 3),
                "upconverter": 1,
            },
        },
        "zz_q4_q5": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "square": "zz_q4_q5.square.pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "thread": "q4",
            "MWInput": {
                "port": ('con1', 3, 3),
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
            "thread": "q5",
            "MWInput": {
                "port": ('con1', 5, 2),
                "upconverter": 1,
            },
        },
        "zz_q5_q6": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "square": "zz_q5_q6.square.pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "thread": "q5",
            "MWInput": {
                "port": ('con1', 5, 2),
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
            "thread": "q6",
            "MWInput": {
                "port": ('con1', 5, 3),
                "upconverter": 1,
            },
        },
        "zz_q6_q7": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "square": "zz_q6_q7.square.pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "thread": "q6",
            "MWInput": {
                "port": ('con1', 5, 3),
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
            "thread": "q7",
            "MWInput": {
                "port": ('con1', 7, 2),
                "upconverter": 1,
            },
        },
        "zz_q7_q8": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "square": "zz_q7_q8.square.pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "thread": "q7",
            "MWInput": {
                "port": ('con1', 7, 2),
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
            "thread": "q8",
            "MWInput": {
                "port": ('con1', 7, 3),
                "upconverter": 1,
            },
        },
        "zz_q8_q1": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "square": "zz_q8_q1.square.pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "thread": "q8",
            "MWInput": {
                "port": ('con1', 7, 3),
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
        "q1.xy.x180_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q1.xy.x180_DragCosine.wf.I",
                "Q": "q1.xy.x180_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q1.xy.x90_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q1.xy.x90_DragCosine.wf.I",
                "Q": "q1.xy.x90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q1.xy.-x90_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q1.xy.-x90_DragCosine.wf.I",
                "Q": "q1.xy.-x90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q1.xy.y180_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q1.xy.y180_DragCosine.wf.I",
                "Q": "q1.xy.y180_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q1.xy.y90_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q1.xy.y90_DragCosine.wf.I",
                "Q": "q1.xy.y90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q1.xy.-y90_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q1.xy.-y90_DragCosine.wf.I",
                "Q": "q1.xy.-y90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q1.xy.x180_Square.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q1.xy.x180_Square.wf.I",
                "Q": "q1.xy.x180_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q1.xy.x90_Square.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q1.xy.x90_Square.wf.I",
                "Q": "q1.xy.x90_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q1.xy.-x90_Square.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q1.xy.-x90_Square.wf.I",
                "Q": "q1.xy.-x90_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q1.xy.y180_Square.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q1.xy.y180_Square.wf.I",
                "Q": "q1.xy.y180_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q1.xy.y90_Square.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q1.xy.y90_Square.wf.I",
                "Q": "q1.xy.y90_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q1.xy.-y90_Square.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q1.xy.-y90_Square.wf.I",
                "Q": "q1.xy.-y90_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q1.xy.saturation.pulse": {
            "length": 40000,
            "waveforms": {
                "I": "q1.xy.saturation.wf.I",
                "Q": "q1.xy.saturation.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q1.xy.cr_q8_q1_Square.pulse": {
            "length": 100,
            "waveforms": {
                "I": "q1.xy.cr_q8_q1_Square.wf.I",
                "Q": "q1.xy.cr_q8_q1_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q1.xy_detuned.zz_q8_q1_Square.pulse": {
            "length": 100,
            "waveforms": {
                "I": "q1.xy_detuned.zz_q8_q1_Square.wf.I",
                "Q": "q1.xy_detuned.zz_q8_q1_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q1.resonator.readout.pulse": {
            "length": 2000,
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
            "length": 100,
            "waveforms": {
                "I": "q1.resonator.const.wf.I",
                "Q": "q1.resonator.const.wf.Q",
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
            "digital_marker": "ON",
        },
        "q2.xy.x90_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q2.xy.x90_DragCosine.wf.I",
                "Q": "q2.xy.x90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q2.xy.-x90_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q2.xy.-x90_DragCosine.wf.I",
                "Q": "q2.xy.-x90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q2.xy.y180_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q2.xy.y180_DragCosine.wf.I",
                "Q": "q2.xy.y180_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q2.xy.y90_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q2.xy.y90_DragCosine.wf.I",
                "Q": "q2.xy.y90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q2.xy.-y90_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q2.xy.-y90_DragCosine.wf.I",
                "Q": "q2.xy.-y90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q2.xy.x180_Square.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q2.xy.x180_Square.wf.I",
                "Q": "q2.xy.x180_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q2.xy.x90_Square.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q2.xy.x90_Square.wf.I",
                "Q": "q2.xy.x90_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q2.xy.-x90_Square.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q2.xy.-x90_Square.wf.I",
                "Q": "q2.xy.-x90_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q2.xy.y180_Square.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q2.xy.y180_Square.wf.I",
                "Q": "q2.xy.y180_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q2.xy.y90_Square.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q2.xy.y90_Square.wf.I",
                "Q": "q2.xy.y90_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q2.xy.-y90_Square.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q2.xy.-y90_Square.wf.I",
                "Q": "q2.xy.-y90_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q2.xy.saturation.pulse": {
            "length": 40000,
            "waveforms": {
                "I": "q2.xy.saturation.wf.I",
                "Q": "q2.xy.saturation.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q2.xy.cr_q1_q2_Square.pulse": {
            "length": 100,
            "waveforms": {
                "I": "q2.xy.cr_q1_q2_Square.wf.I",
                "Q": "q2.xy.cr_q1_q2_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q2.xy_detuned.zz_q1_q2_Square.pulse": {
            "length": 100,
            "waveforms": {
                "I": "q2.xy_detuned.zz_q1_q2_Square.wf.I",
                "Q": "q2.xy_detuned.zz_q1_q2_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q2.resonator.readout.pulse": {
            "length": 2000,
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
            "length": 100,
            "waveforms": {
                "I": "q2.resonator.const.wf.I",
                "Q": "q2.resonator.const.wf.Q",
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
            "digital_marker": "ON",
        },
        "q3.xy.x90_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q3.xy.x90_DragCosine.wf.I",
                "Q": "q3.xy.x90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q3.xy.-x90_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q3.xy.-x90_DragCosine.wf.I",
                "Q": "q3.xy.-x90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q3.xy.y180_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q3.xy.y180_DragCosine.wf.I",
                "Q": "q3.xy.y180_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q3.xy.y90_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q3.xy.y90_DragCosine.wf.I",
                "Q": "q3.xy.y90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q3.xy.-y90_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q3.xy.-y90_DragCosine.wf.I",
                "Q": "q3.xy.-y90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q3.xy.x180_Square.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q3.xy.x180_Square.wf.I",
                "Q": "q3.xy.x180_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q3.xy.x90_Square.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q3.xy.x90_Square.wf.I",
                "Q": "q3.xy.x90_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q3.xy.-x90_Square.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q3.xy.-x90_Square.wf.I",
                "Q": "q3.xy.-x90_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q3.xy.y180_Square.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q3.xy.y180_Square.wf.I",
                "Q": "q3.xy.y180_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q3.xy.y90_Square.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q3.xy.y90_Square.wf.I",
                "Q": "q3.xy.y90_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q3.xy.-y90_Square.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q3.xy.-y90_Square.wf.I",
                "Q": "q3.xy.-y90_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q3.xy.saturation.pulse": {
            "length": 40000,
            "waveforms": {
                "I": "q3.xy.saturation.wf.I",
                "Q": "q3.xy.saturation.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q3.xy.cr_q2_q3_Square.pulse": {
            "length": 100,
            "waveforms": {
                "I": "q3.xy.cr_q2_q3_Square.wf.I",
                "Q": "q3.xy.cr_q2_q3_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q3.xy_detuned.zz_q2_q3_Square.pulse": {
            "length": 100,
            "waveforms": {
                "I": "q3.xy_detuned.zz_q2_q3_Square.wf.I",
                "Q": "q3.xy_detuned.zz_q2_q3_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q3.resonator.readout.pulse": {
            "length": 2000,
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
            "length": 100,
            "waveforms": {
                "I": "q3.resonator.const.wf.I",
                "Q": "q3.resonator.const.wf.Q",
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
            "digital_marker": "ON",
        },
        "q4.xy.x90_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q4.xy.x90_DragCosine.wf.I",
                "Q": "q4.xy.x90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q4.xy.-x90_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q4.xy.-x90_DragCosine.wf.I",
                "Q": "q4.xy.-x90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q4.xy.y180_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q4.xy.y180_DragCosine.wf.I",
                "Q": "q4.xy.y180_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q4.xy.y90_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q4.xy.y90_DragCosine.wf.I",
                "Q": "q4.xy.y90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q4.xy.-y90_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q4.xy.-y90_DragCosine.wf.I",
                "Q": "q4.xy.-y90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q4.xy.x180_Square.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q4.xy.x180_Square.wf.I",
                "Q": "q4.xy.x180_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q4.xy.x90_Square.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q4.xy.x90_Square.wf.I",
                "Q": "q4.xy.x90_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q4.xy.-x90_Square.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q4.xy.-x90_Square.wf.I",
                "Q": "q4.xy.-x90_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q4.xy.y180_Square.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q4.xy.y180_Square.wf.I",
                "Q": "q4.xy.y180_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q4.xy.y90_Square.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q4.xy.y90_Square.wf.I",
                "Q": "q4.xy.y90_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q4.xy.-y90_Square.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q4.xy.-y90_Square.wf.I",
                "Q": "q4.xy.-y90_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q4.xy.saturation.pulse": {
            "length": 40000,
            "waveforms": {
                "I": "q4.xy.saturation.wf.I",
                "Q": "q4.xy.saturation.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q4.xy.cr_q3_q4_Square.pulse": {
            "length": 100,
            "waveforms": {
                "I": "q4.xy.cr_q3_q4_Square.wf.I",
                "Q": "q4.xy.cr_q3_q4_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q4.xy_detuned.zz_q3_q4_Square.pulse": {
            "length": 100,
            "waveforms": {
                "I": "q4.xy_detuned.zz_q3_q4_Square.wf.I",
                "Q": "q4.xy_detuned.zz_q3_q4_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q4.resonator.readout.pulse": {
            "length": 2000,
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
            "length": 100,
            "waveforms": {
                "I": "q4.resonator.const.wf.I",
                "Q": "q4.resonator.const.wf.Q",
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
            "digital_marker": "ON",
        },
        "q5.xy.x90_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q5.xy.x90_DragCosine.wf.I",
                "Q": "q5.xy.x90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q5.xy.-x90_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q5.xy.-x90_DragCosine.wf.I",
                "Q": "q5.xy.-x90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q5.xy.y180_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q5.xy.y180_DragCosine.wf.I",
                "Q": "q5.xy.y180_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q5.xy.y90_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q5.xy.y90_DragCosine.wf.I",
                "Q": "q5.xy.y90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q5.xy.-y90_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q5.xy.-y90_DragCosine.wf.I",
                "Q": "q5.xy.-y90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q5.xy.x180_Square.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q5.xy.x180_Square.wf.I",
                "Q": "q5.xy.x180_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q5.xy.x90_Square.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q5.xy.x90_Square.wf.I",
                "Q": "q5.xy.x90_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q5.xy.-x90_Square.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q5.xy.-x90_Square.wf.I",
                "Q": "q5.xy.-x90_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q5.xy.y180_Square.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q5.xy.y180_Square.wf.I",
                "Q": "q5.xy.y180_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q5.xy.y90_Square.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q5.xy.y90_Square.wf.I",
                "Q": "q5.xy.y90_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q5.xy.-y90_Square.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q5.xy.-y90_Square.wf.I",
                "Q": "q5.xy.-y90_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q5.xy.saturation.pulse": {
            "length": 40000,
            "waveforms": {
                "I": "q5.xy.saturation.wf.I",
                "Q": "q5.xy.saturation.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q5.xy.cr_q4_q5_Square.pulse": {
            "length": 100,
            "waveforms": {
                "I": "q5.xy.cr_q4_q5_Square.wf.I",
                "Q": "q5.xy.cr_q4_q5_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q5.xy_detuned.zz_q4_q5_Square.pulse": {
            "length": 100,
            "waveforms": {
                "I": "q5.xy_detuned.zz_q4_q5_Square.wf.I",
                "Q": "q5.xy_detuned.zz_q4_q5_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q5.resonator.readout.pulse": {
            "length": 2000,
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
            "length": 100,
            "waveforms": {
                "I": "q5.resonator.const.wf.I",
                "Q": "q5.resonator.const.wf.Q",
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
            "digital_marker": "ON",
        },
        "q6.xy.x90_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q6.xy.x90_DragCosine.wf.I",
                "Q": "q6.xy.x90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q6.xy.-x90_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q6.xy.-x90_DragCosine.wf.I",
                "Q": "q6.xy.-x90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q6.xy.y180_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q6.xy.y180_DragCosine.wf.I",
                "Q": "q6.xy.y180_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q6.xy.y90_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q6.xy.y90_DragCosine.wf.I",
                "Q": "q6.xy.y90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q6.xy.-y90_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q6.xy.-y90_DragCosine.wf.I",
                "Q": "q6.xy.-y90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q6.xy.x180_Square.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q6.xy.x180_Square.wf.I",
                "Q": "q6.xy.x180_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q6.xy.x90_Square.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q6.xy.x90_Square.wf.I",
                "Q": "q6.xy.x90_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q6.xy.-x90_Square.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q6.xy.-x90_Square.wf.I",
                "Q": "q6.xy.-x90_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q6.xy.y180_Square.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q6.xy.y180_Square.wf.I",
                "Q": "q6.xy.y180_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q6.xy.y90_Square.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q6.xy.y90_Square.wf.I",
                "Q": "q6.xy.y90_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q6.xy.-y90_Square.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q6.xy.-y90_Square.wf.I",
                "Q": "q6.xy.-y90_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q6.xy.saturation.pulse": {
            "length": 40000,
            "waveforms": {
                "I": "q6.xy.saturation.wf.I",
                "Q": "q6.xy.saturation.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q6.xy.cr_q5_q6_Square.pulse": {
            "length": 100,
            "waveforms": {
                "I": "q6.xy.cr_q5_q6_Square.wf.I",
                "Q": "q6.xy.cr_q5_q6_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q6.xy_detuned.zz_q5_q6_Square.pulse": {
            "length": 100,
            "waveforms": {
                "I": "q6.xy_detuned.zz_q5_q6_Square.wf.I",
                "Q": "q6.xy_detuned.zz_q5_q6_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q6.resonator.readout.pulse": {
            "length": 2000,
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
            "length": 100,
            "waveforms": {
                "I": "q6.resonator.const.wf.I",
                "Q": "q6.resonator.const.wf.Q",
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
            "digital_marker": "ON",
        },
        "q7.xy.x90_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q7.xy.x90_DragCosine.wf.I",
                "Q": "q7.xy.x90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q7.xy.-x90_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q7.xy.-x90_DragCosine.wf.I",
                "Q": "q7.xy.-x90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q7.xy.y180_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q7.xy.y180_DragCosine.wf.I",
                "Q": "q7.xy.y180_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q7.xy.y90_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q7.xy.y90_DragCosine.wf.I",
                "Q": "q7.xy.y90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q7.xy.-y90_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q7.xy.-y90_DragCosine.wf.I",
                "Q": "q7.xy.-y90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q7.xy.x180_Square.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q7.xy.x180_Square.wf.I",
                "Q": "q7.xy.x180_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q7.xy.x90_Square.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q7.xy.x90_Square.wf.I",
                "Q": "q7.xy.x90_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q7.xy.-x90_Square.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q7.xy.-x90_Square.wf.I",
                "Q": "q7.xy.-x90_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q7.xy.y180_Square.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q7.xy.y180_Square.wf.I",
                "Q": "q7.xy.y180_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q7.xy.y90_Square.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q7.xy.y90_Square.wf.I",
                "Q": "q7.xy.y90_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q7.xy.-y90_Square.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q7.xy.-y90_Square.wf.I",
                "Q": "q7.xy.-y90_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q7.xy.saturation.pulse": {
            "length": 40000,
            "waveforms": {
                "I": "q7.xy.saturation.wf.I",
                "Q": "q7.xy.saturation.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q7.xy.cr_q6_q7_Square.pulse": {
            "length": 100,
            "waveforms": {
                "I": "q7.xy.cr_q6_q7_Square.wf.I",
                "Q": "q7.xy.cr_q6_q7_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q7.xy_detuned.zz_q6_q7_Square.pulse": {
            "length": 100,
            "waveforms": {
                "I": "q7.xy_detuned.zz_q6_q7_Square.wf.I",
                "Q": "q7.xy_detuned.zz_q6_q7_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q7.resonator.readout.pulse": {
            "length": 2000,
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
            "length": 100,
            "waveforms": {
                "I": "q7.resonator.const.wf.I",
                "Q": "q7.resonator.const.wf.Q",
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
            "digital_marker": "ON",
        },
        "q8.xy.x90_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q8.xy.x90_DragCosine.wf.I",
                "Q": "q8.xy.x90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q8.xy.-x90_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q8.xy.-x90_DragCosine.wf.I",
                "Q": "q8.xy.-x90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q8.xy.y180_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q8.xy.y180_DragCosine.wf.I",
                "Q": "q8.xy.y180_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q8.xy.y90_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q8.xy.y90_DragCosine.wf.I",
                "Q": "q8.xy.y90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q8.xy.-y90_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q8.xy.-y90_DragCosine.wf.I",
                "Q": "q8.xy.-y90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q8.xy.x180_Square.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q8.xy.x180_Square.wf.I",
                "Q": "q8.xy.x180_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q8.xy.x90_Square.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q8.xy.x90_Square.wf.I",
                "Q": "q8.xy.x90_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q8.xy.-x90_Square.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q8.xy.-x90_Square.wf.I",
                "Q": "q8.xy.-x90_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q8.xy.y180_Square.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q8.xy.y180_Square.wf.I",
                "Q": "q8.xy.y180_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q8.xy.y90_Square.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q8.xy.y90_Square.wf.I",
                "Q": "q8.xy.y90_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q8.xy.-y90_Square.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q8.xy.-y90_Square.wf.I",
                "Q": "q8.xy.-y90_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q8.xy.saturation.pulse": {
            "length": 40000,
            "waveforms": {
                "I": "q8.xy.saturation.wf.I",
                "Q": "q8.xy.saturation.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q8.xy.cr_q7_q8_Square.pulse": {
            "length": 100,
            "waveforms": {
                "I": "q8.xy.cr_q7_q8_Square.wf.I",
                "Q": "q8.xy.cr_q7_q8_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q8.xy_detuned.zz_q7_q8_Square.pulse": {
            "length": 100,
            "waveforms": {
                "I": "q8.xy_detuned.zz_q7_q8_Square.wf.I",
                "Q": "q8.xy_detuned.zz_q7_q8_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q8.resonator.readout.pulse": {
            "length": 2000,
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
            "length": 100,
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
        "zz_q1_q2.square.pulse": {
            "length": 100,
            "waveforms": {
                "I": "zz_q1_q2.square.wf.I",
                "Q": "zz_q1_q2.square.wf.Q",
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
        "zz_q2_q3.square.pulse": {
            "length": 100,
            "waveforms": {
                "I": "zz_q2_q3.square.wf.I",
                "Q": "zz_q2_q3.square.wf.Q",
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
        "zz_q3_q4.square.pulse": {
            "length": 100,
            "waveforms": {
                "I": "zz_q3_q4.square.wf.I",
                "Q": "zz_q3_q4.square.wf.Q",
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
        "zz_q4_q5.square.pulse": {
            "length": 100,
            "waveforms": {
                "I": "zz_q4_q5.square.wf.I",
                "Q": "zz_q4_q5.square.wf.Q",
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
        "zz_q5_q6.square.pulse": {
            "length": 100,
            "waveforms": {
                "I": "zz_q5_q6.square.wf.I",
                "Q": "zz_q5_q6.square.wf.Q",
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
        "zz_q6_q7.square.pulse": {
            "length": 100,
            "waveforms": {
                "I": "zz_q6_q7.square.wf.I",
                "Q": "zz_q6_q7.square.wf.Q",
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
        "zz_q7_q8.square.pulse": {
            "length": 100,
            "waveforms": {
                "I": "zz_q7_q8.square.wf.I",
                "Q": "zz_q7_q8.square.wf.Q",
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
        "zz_q8_q1.square.pulse": {
            "length": 100,
            "waveforms": {
                "I": "zz_q8_q1.square.wf.I",
                "Q": "zz_q8_q1.square.wf.Q",
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
        "q1.xy.x180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0009587121065884679, 0.0038100182863815214, 0.008480071207044722, 0.014847918950998806, 0.022748637606551846, 0.03197760271058151, 0.04229578891464574, 0.05343596061595301, 0.06510959321910238, 0.07701434577154927, 0.08884189143546399, 0.10028590299087507, 0.11104998654975992, 0.12085535800205625, 0.12944806337767426, 0.13660555612092581, 0.14214246092941862, 0.14591537487701495] + [0.14782658147429253] * 2 + [0.14591537487701495, 0.14214246092941862, 0.13660555612092584, 0.12944806337767428, 0.12085535800205625, 0.11104998654975987, 0.1002859029908751, 0.08884189143546402, 0.07701434577154927, 0.06510959321910244, 0.05343596061595306, 0.04229578891464577, 0.03197760271058154, 0.022748637606551853, 0.014847918950998806, 0.008480071207044713, 0.003810018286381513, 0.0009587121065884679, 0.0],
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
            "samples": [0.0, 0.00047935605329423394, 0.0019050091431907607, 0.004240035603522361, 0.007423959475499403, 0.011374318803275923, 0.015988801355290756, 0.02114789445732287, 0.026717980307976504, 0.03255479660955119, 0.03850717288577463, 0.044420945717731995, 0.050142951495437536, 0.05552499327487996, 0.06042767900102813, 0.06472403168883713, 0.06830277806046291, 0.07107123046470931, 0.07295768743850747] + [0.07391329073714627] * 2 + [0.07295768743850747, 0.07107123046470931, 0.06830277806046292, 0.06472403168883714, 0.06042767900102813, 0.05552499327487993, 0.05014295149543755, 0.04442094571773201, 0.03850717288577463, 0.03255479660955122, 0.02671798030797653, 0.021147894457322885, 0.01598880135529077, 0.011374318803275926, 0.007423959475499403, 0.004240035603522357, 0.0019050091431907566, 0.00047935605329423394, 0.0],
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
            "samples": [0.0, -0.00047935605329423394, -0.0019050091431907607, -0.004240035603522361, -0.007423959475499403, -0.011374318803275923, -0.015988801355290756, -0.02114789445732287, -0.026717980307976504, -0.03255479660955119, -0.03850717288577463, -0.044420945717731995, -0.050142951495437536, -0.05552499327487996, -0.06042767900102813, -0.06472403168883713, -0.06830277806046291, -0.07107123046470931, -0.07295768743850747] + [-0.07391329073714627] * 2 + [-0.07295768743850747, -0.07107123046470931, -0.06830277806046292, -0.06472403168883714, -0.06042767900102813, -0.05552499327487993, -0.05014295149543755, -0.04442094571773201, -0.03850717288577463, -0.03255479660955122, -0.02671798030797653, -0.021147894457322885, -0.01598880135529077, -0.011374318803275926, -0.007423959475499403, -0.004240035603522357, -0.0019050091431907566, -0.00047935605329423394, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.xy.-x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 5.870418563186916e-20, 2.332963349555007e-19, 5.192546030124476e-19, 9.091728208670006e-19, 1.3929523114913413e-18, 1.9580634401959688e-18, 2.5898701255866507e-18, 3.272008906384544e-18, 3.986812746477997e-18, 4.715768601877765e-18, 5.439996898831882e-18, 6.140740504868857e-18, 6.799850528676006e-18, 7.400256366851283e-18, 7.926407823564624e-18, 8.364677852461796e-18, 8.703715490007011e-18, 8.934739839476124e-18] + [9.051767491569389e-18] * 2 + [8.934739839476124e-18, 8.703715490007011e-18, 8.364677852461798e-18, 7.926407823564626e-18, 7.400256366851283e-18, 6.799850528676002e-18, 6.140740504868858e-18, 5.439996898831883e-18, 4.715768601877765e-18, 3.986812746478001e-18, 3.272008906384547e-18, 2.5898701255866523e-18, 1.9580634401959703e-18, 1.3929523114913417e-18, 9.091728208670006e-19, 5.19254603012447e-19, 2.332963349555002e-19, 5.870418563186916e-20, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.xy.y180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 5.870418563186916e-20, 2.332963349555007e-19, 5.192546030124476e-19, 9.091728208670006e-19, 1.3929523114913413e-18, 1.9580634401959688e-18, 2.5898701255866507e-18, 3.272008906384544e-18, 3.986812746477997e-18, 4.715768601877765e-18, 5.439996898831882e-18, 6.140740504868857e-18, 6.799850528676006e-18, 7.400256366851283e-18, 7.926407823564624e-18, 8.364677852461796e-18, 8.703715490007011e-18, 8.934739839476124e-18] + [9.051767491569389e-18] * 2 + [8.934739839476124e-18, 8.703715490007011e-18, 8.364677852461798e-18, 7.926407823564626e-18, 7.400256366851283e-18, 6.799850528676002e-18, 6.140740504868858e-18, 5.439996898831883e-18, 4.715768601877765e-18, 3.986812746478001e-18, 3.272008906384547e-18, 2.5898701255866523e-18, 1.9580634401959703e-18, 1.3929523114913417e-18, 9.091728208670006e-19, 5.19254603012447e-19, 2.332963349555002e-19, 5.870418563186916e-20, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.xy.y180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0009587121065884679, 0.0038100182863815214, 0.008480071207044722, 0.014847918950998806, 0.022748637606551846, 0.03197760271058151, 0.04229578891464574, 0.05343596061595301, 0.06510959321910238, 0.07701434577154927, 0.08884189143546399, 0.10028590299087507, 0.11104998654975992, 0.12085535800205625, 0.12944806337767426, 0.13660555612092581, 0.14214246092941862, 0.14591537487701495] + [0.14782658147429253] * 2 + [0.14591537487701495, 0.14214246092941862, 0.13660555612092584, 0.12944806337767428, 0.12085535800205625, 0.11104998654975987, 0.1002859029908751, 0.08884189143546402, 0.07701434577154927, 0.06510959321910244, 0.05343596061595306, 0.04229578891464577, 0.03197760271058154, 0.022748637606551853, 0.014847918950998806, 0.008480071207044713, 0.003810018286381513, 0.0009587121065884679, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.xy.y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 2.935209281593458e-20, 1.1664816747775036e-19, 2.596273015062238e-19, 4.545864104335003e-19, 6.964761557456706e-19, 9.790317200979844e-19, 1.2949350627933254e-18, 1.636004453192272e-18, 1.9934063732389985e-18, 2.3578843009388826e-18, 2.719998449415941e-18, 3.0703702524344283e-18, 3.399925264338003e-18, 3.700128183425641e-18, 3.963203911782312e-18, 4.182338926230898e-18, 4.3518577450035054e-18, 4.467369919738062e-18] + [4.5258837457846946e-18] * 2 + [4.467369919738062e-18, 4.3518577450035054e-18, 4.182338926230899e-18, 3.963203911782313e-18, 3.700128183425641e-18, 3.399925264338001e-18, 3.070370252434429e-18, 2.7199984494159416e-18, 2.3578843009388826e-18, 1.9934063732390004e-18, 1.6360044531922735e-18, 1.2949350627933261e-18, 9.790317200979852e-19, 6.964761557456708e-19, 4.545864104335003e-19, 2.596273015062235e-19, 1.166481674777501e-19, 2.935209281593458e-20, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.xy.y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.00047935605329423394, 0.0019050091431907607, 0.004240035603522361, 0.007423959475499403, 0.011374318803275923, 0.015988801355290756, 0.02114789445732287, 0.026717980307976504, 0.03255479660955119, 0.03850717288577463, 0.044420945717731995, 0.050142951495437536, 0.05552499327487996, 0.06042767900102813, 0.06472403168883713, 0.06830277806046291, 0.07107123046470931, 0.07295768743850747] + [0.07391329073714627] * 2 + [0.07295768743850747, 0.07107123046470931, 0.06830277806046292, 0.06472403168883714, 0.06042767900102813, 0.05552499327487993, 0.05014295149543755, 0.04442094571773201, 0.03850717288577463, 0.03255479660955122, 0.02671798030797653, 0.021147894457322885, 0.01598880135529077, 0.011374318803275926, 0.007423959475499403, 0.004240035603522357, 0.0019050091431907566, 0.00047935605329423394, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.xy.-y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 2.935209281593458e-20, 1.1664816747775036e-19, 2.596273015062238e-19, 4.545864104335003e-19, 6.964761557456706e-19, 9.790317200979844e-19, 1.2949350627933254e-18, 1.636004453192272e-18, 1.9934063732389985e-18, 2.3578843009388826e-18, 2.719998449415941e-18, 3.0703702524344283e-18, 3.399925264338003e-18, 3.700128183425641e-18, 3.963203911782312e-18, 4.182338926230898e-18, 4.3518577450035054e-18, 4.467369919738062e-18] + [4.5258837457846946e-18] * 2 + [4.467369919738062e-18, 4.3518577450035054e-18, 4.182338926230899e-18, 3.963203911782313e-18, 3.700128183425641e-18, 3.399925264338001e-18, 3.070370252434429e-18, 2.7199984494159416e-18, 2.3578843009388826e-18, 1.9934063732390004e-18, 1.6360044531922735e-18, 1.2949350627933261e-18, 9.790317200979852e-19, 6.964761557456708e-19, 4.545864104335003e-19, 2.596273015062235e-19, 1.166481674777501e-19, 2.935209281593458e-20, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.xy.-y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.00047935605329423394, -0.0019050091431907607, -0.004240035603522361, -0.007423959475499403, -0.011374318803275923, -0.015988801355290756, -0.02114789445732287, -0.026717980307976504, -0.03255479660955119, -0.03850717288577463, -0.044420945717731995, -0.050142951495437536, -0.05552499327487996, -0.06042767900102813, -0.06472403168883713, -0.06830277806046291, -0.07107123046470931, -0.07295768743850747] + [-0.07391329073714627] * 2 + [-0.07295768743850747, -0.07107123046470931, -0.06830277806046292, -0.06472403168883714, -0.06042767900102813, -0.05552499327487993, -0.05014295149543755, -0.04442094571773201, -0.03850717288577463, -0.03255479660955122, -0.02671798030797653, -0.021147894457322885, -0.01598880135529077, -0.011374318803275926, -0.007423959475499403, -0.004240035603522357, -0.0019050091431907566, -0.00047935605329423394, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.xy.x180_Square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "q1.xy.x180_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q1.xy.x90_Square.wf.I": {
            "type": "constant",
            "sample": 0.05,
        },
        "q1.xy.x90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q1.xy.-x90_Square.wf.I": {
            "type": "constant",
            "sample": -0.125,
        },
        "q1.xy.-x90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q1.xy.y180_Square.wf.I": {
            "type": "constant",
            "sample": -0.11201840403229253,
        },
        "q1.xy.y180_Square.wf.Q": {
            "type": "constant",
            "sample": 0.22349916590013946,
        },
        "q1.xy.y90_Square.wf.I": {
            "type": "constant",
            "sample": -0.056009202016146266,
        },
        "q1.xy.y90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.11174958295006973,
        },
        "q1.xy.-y90_Square.wf.I": {
            "type": "constant",
            "sample": 0.056009202016146266,
        },
        "q1.xy.-y90_Square.wf.Q": {
            "type": "constant",
            "sample": -0.11174958295006973,
        },
        "q1.xy.saturation.wf.I": {
            "type": "constant",
            "sample": 0.06342390975458759,
        },
        "q1.xy.saturation.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q1.xy.cr_q8_q1_Square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "q1.xy.cr_q8_q1_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q1.xy_detuned.zz_q8_q1_Square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "q1.xy_detuned.zz_q8_q1_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q1.resonator.readout.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "q1.resonator.readout.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q1.resonator.const.wf.I": {
            "type": "constant",
            "sample": 0.125,
        },
        "q1.resonator.const.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q2.xy.x180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0007510084282569763, 0.00298458298922262, 0.006642875275010638, 0.011631137437031628, 0.017820176105502773, 0.025049698429863057, 0.03313246357940488, 0.04185913218243622, 0.05100368810604664, 0.06032929215522879, 0.06959441608362318, 0.07855909804823011, 0.08699115749509692, 0.09467220851370672, 0.10140331591734797, 0.10701014755995437, 0.11134748944711555, 0.11430300670225482, 0.11580015298092586, 0.11580015298092587, 0.11430300670225482, 0.11134748944711556, 0.1070101475599544, 0.101403315917348, 0.09467220851370672, 0.08699115749509688, 0.07855909804823014, 0.06959441608362321, 0.06032929215522879, 0.051003688106046684, 0.041859132182436254, 0.0331324635794049, 0.025049698429863078, 0.01782017610550278, 0.011631137437031628, 0.006642875275010631, 0.0029845829892226135, 0.0007510084282569763, 0.0],
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
            "samples": [0.0, 0.00037550421412848814, 0.00149229149461131, 0.003321437637505319, 0.005815568718515814, 0.008910088052751387, 0.012524849214931529, 0.01656623178970244, 0.02092956609121811, 0.02550184405302332, 0.030164646077614394, 0.03479720804181159, 0.039279549024115054, 0.04349557874754846, 0.04733610425685336, 0.050701657958673985, 0.05350507377997719, 0.05567374472355777, 0.05715150335112741, 0.05790007649046293, 0.057900076490462936, 0.05715150335112741, 0.05567374472355778, 0.0535050737799772, 0.050701657958674, 0.04733610425685336, 0.04349557874754844, 0.03927954902411507, 0.034797208041811606, 0.030164646077614394, 0.025501844053023342, 0.020929566091218127, 0.01656623178970245, 0.012524849214931539, 0.00891008805275139, 0.005815568718515814, 0.0033214376375053155, 0.0014922914946113067, 0.00037550421412848814, 0.0],
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
            "samples": [0.0, -0.00037550421412848814, -0.00149229149461131, -0.003321437637505319, -0.005815568718515814, -0.008910088052751387, -0.012524849214931529, -0.01656623178970244, -0.02092956609121811, -0.02550184405302332, -0.030164646077614394, -0.03479720804181159, -0.039279549024115054, -0.04349557874754846, -0.04733610425685336, -0.050701657958673985, -0.05350507377997719, -0.05567374472355777, -0.05715150335112741, -0.05790007649046293, -0.057900076490462936, -0.05715150335112741, -0.05567374472355778, -0.0535050737799772, -0.050701657958674, -0.04733610425685336, -0.04349557874754844, -0.03927954902411507, -0.034797208041811606, -0.030164646077614394, -0.025501844053023342, -0.020929566091218127, -0.01656623178970245, -0.012524849214931539, -0.00891008805275139, -0.005815568718515814, -0.0033214376375053155, -0.0014922914946113067, -0.00037550421412848814, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.xy.-x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 4.5986003389879534e-20, 1.8275300022705605e-19, 4.067587971338436e-19, 7.122017616351866e-19, 1.091171081392306e-18, 1.5338516500869136e-18, 2.028778273519222e-18, 2.5631326121153237e-18, 3.1230751691889973e-18, 3.694103726636323e-18, 4.261428944766911e-18, 4.8103573984334044e-18, 5.326672129024686e-18, 5.797000856226087e-18, 6.209162313055402e-18, 6.5524817342792036e-18, 6.818067327225187e-18, 6.999040564541742e-18, 7.090714334443233e-18, 7.090714334443235e-18, 6.999040564541742e-18, 6.818067327225188e-18, 6.552481734279205e-18, 6.2091623130554036e-18, 5.797000856226087e-18, 5.326672129024684e-18, 4.810357398433406e-18, 4.261428944766912e-18, 3.694103726636323e-18, 3.123075169189e-18, 2.563132612115326e-18, 2.0287782735192232e-18, 1.533851650086915e-18, 1.0911710813923064e-18, 7.122017616351866e-19, 4.0675879713384314e-19, 1.8275300022705566e-19, 4.5986003389879534e-20, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.xy.y180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 4.5986003389879534e-20, 1.8275300022705605e-19, 4.067587971338436e-19, 7.122017616351866e-19, 1.091171081392306e-18, 1.5338516500869136e-18, 2.028778273519222e-18, 2.5631326121153237e-18, 3.1230751691889973e-18, 3.694103726636323e-18, 4.261428944766911e-18, 4.8103573984334044e-18, 5.326672129024686e-18, 5.797000856226087e-18, 6.209162313055402e-18, 6.5524817342792036e-18, 6.818067327225187e-18, 6.999040564541742e-18, 7.090714334443233e-18, 7.090714334443235e-18, 6.999040564541742e-18, 6.818067327225188e-18, 6.552481734279205e-18, 6.2091623130554036e-18, 5.797000856226087e-18, 5.326672129024684e-18, 4.810357398433406e-18, 4.261428944766912e-18, 3.694103726636323e-18, 3.123075169189e-18, 2.563132612115326e-18, 2.0287782735192232e-18, 1.533851650086915e-18, 1.0911710813923064e-18, 7.122017616351866e-19, 4.0675879713384314e-19, 1.8275300022705566e-19, 4.5986003389879534e-20, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.xy.y180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0007510084282569763, 0.00298458298922262, 0.006642875275010638, 0.011631137437031628, 0.017820176105502773, 0.025049698429863057, 0.03313246357940488, 0.04185913218243622, 0.05100368810604664, 0.06032929215522879, 0.06959441608362318, 0.07855909804823011, 0.08699115749509692, 0.09467220851370672, 0.10140331591734797, 0.10701014755995437, 0.11134748944711555, 0.11430300670225482, 0.11580015298092586, 0.11580015298092587, 0.11430300670225482, 0.11134748944711556, 0.1070101475599544, 0.101403315917348, 0.09467220851370672, 0.08699115749509688, 0.07855909804823014, 0.06959441608362321, 0.06032929215522879, 0.051003688106046684, 0.041859132182436254, 0.0331324635794049, 0.025049698429863078, 0.01782017610550278, 0.011631137437031628, 0.006642875275010631, 0.0029845829892226135, 0.0007510084282569763, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.xy.y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 2.2993001694939767e-20, 9.137650011352802e-20, 2.033793985669218e-19, 3.561008808175933e-19, 5.45585540696153e-19, 7.669258250434568e-19, 1.014389136759611e-18, 1.2815663060576618e-18, 1.5615375845944987e-18, 1.8470518633181615e-18, 2.1307144723834554e-18, 2.4051786992167022e-18, 2.663336064512343e-18, 2.8985004281130434e-18, 3.104581156527701e-18, 3.2762408671396018e-18, 3.4090336636125936e-18, 3.499520282270871e-18, 3.545357167221617e-18, 3.5453571672216175e-18, 3.499520282270871e-18, 3.409033663612594e-18, 3.2762408671396026e-18, 3.1045811565277018e-18, 2.8985004281130434e-18, 2.663336064512342e-18, 2.405178699216703e-18, 2.130714472383456e-18, 1.8470518633181615e-18, 1.5615375845945e-18, 1.281566306057663e-18, 1.0143891367596116e-18, 7.669258250434575e-19, 5.455855406961532e-19, 3.561008808175933e-19, 2.0337939856692157e-19, 9.137650011352783e-20, 2.2993001694939767e-20, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.xy.y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.00037550421412848814, 0.00149229149461131, 0.003321437637505319, 0.005815568718515814, 0.008910088052751387, 0.012524849214931529, 0.01656623178970244, 0.02092956609121811, 0.02550184405302332, 0.030164646077614394, 0.03479720804181159, 0.039279549024115054, 0.04349557874754846, 0.04733610425685336, 0.050701657958673985, 0.05350507377997719, 0.05567374472355777, 0.05715150335112741, 0.05790007649046293, 0.057900076490462936, 0.05715150335112741, 0.05567374472355778, 0.0535050737799772, 0.050701657958674, 0.04733610425685336, 0.04349557874754844, 0.03927954902411507, 0.034797208041811606, 0.030164646077614394, 0.025501844053023342, 0.020929566091218127, 0.01656623178970245, 0.012524849214931539, 0.00891008805275139, 0.005815568718515814, 0.0033214376375053155, 0.0014922914946113067, 0.00037550421412848814, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.xy.-y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 2.2993001694939767e-20, 9.137650011352802e-20, 2.033793985669218e-19, 3.561008808175933e-19, 5.45585540696153e-19, 7.669258250434568e-19, 1.014389136759611e-18, 1.2815663060576618e-18, 1.5615375845944987e-18, 1.8470518633181615e-18, 2.1307144723834554e-18, 2.4051786992167022e-18, 2.663336064512343e-18, 2.8985004281130434e-18, 3.104581156527701e-18, 3.2762408671396018e-18, 3.4090336636125936e-18, 3.499520282270871e-18, 3.545357167221617e-18, 3.5453571672216175e-18, 3.499520282270871e-18, 3.409033663612594e-18, 3.2762408671396026e-18, 3.1045811565277018e-18, 2.8985004281130434e-18, 2.663336064512342e-18, 2.405178699216703e-18, 2.130714472383456e-18, 1.8470518633181615e-18, 1.5615375845945e-18, 1.281566306057663e-18, 1.0143891367596116e-18, 7.669258250434575e-19, 5.455855406961532e-19, 3.561008808175933e-19, 2.0337939856692157e-19, 9.137650011352783e-20, 2.2993001694939767e-20, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.xy.-y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.00037550421412848814, -0.00149229149461131, -0.003321437637505319, -0.005815568718515814, -0.008910088052751387, -0.012524849214931529, -0.01656623178970244, -0.02092956609121811, -0.02550184405302332, -0.030164646077614394, -0.03479720804181159, -0.039279549024115054, -0.04349557874754846, -0.04733610425685336, -0.050701657958673985, -0.05350507377997719, -0.05567374472355777, -0.05715150335112741, -0.05790007649046293, -0.057900076490462936, -0.05715150335112741, -0.05567374472355778, -0.0535050737799772, -0.050701657958674, -0.04733610425685336, -0.04349557874754844, -0.03927954902411507, -0.034797208041811606, -0.030164646077614394, -0.025501844053023342, -0.020929566091218127, -0.01656623178970245, -0.012524849214931539, -0.00891008805275139, -0.005815568718515814, -0.0033214376375053155, -0.0014922914946113067, -0.00037550421412848814, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.xy.x180_Square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "q2.xy.x180_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q2.xy.x90_Square.wf.I": {
            "type": "constant",
            "sample": 0.05,
        },
        "q2.xy.x90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q2.xy.-x90_Square.wf.I": {
            "type": "constant",
            "sample": -0.125,
        },
        "q2.xy.-x90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q2.xy.y180_Square.wf.I": {
            "type": "constant",
            "sample": -0.11201840403229253,
        },
        "q2.xy.y180_Square.wf.Q": {
            "type": "constant",
            "sample": 0.22349916590013946,
        },
        "q2.xy.y90_Square.wf.I": {
            "type": "constant",
            "sample": -0.056009202016146266,
        },
        "q2.xy.y90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.11174958295006973,
        },
        "q2.xy.-y90_Square.wf.I": {
            "type": "constant",
            "sample": 0.056009202016146266,
        },
        "q2.xy.-y90_Square.wf.Q": {
            "type": "constant",
            "sample": -0.11174958295006973,
        },
        "q2.xy.saturation.wf.I": {
            "type": "constant",
            "sample": 0.038831084391286984,
        },
        "q2.xy.saturation.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q2.xy.cr_q1_q2_Square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "q2.xy.cr_q1_q2_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q2.xy_detuned.zz_q1_q2_Square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "q2.xy_detuned.zz_q1_q2_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q2.resonator.readout.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "q2.resonator.readout.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q2.resonator.const.wf.I": {
            "type": "constant",
            "sample": 0.125,
        },
        "q2.resonator.const.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q3.xy.x180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0010815323883923203, 0.004298118432812735, 0.00956645024430564, 0.016750080796280722, 0.025662957830829294, 0.03607424251447538, 0.047714288042708726, 0.0602816233505826, 0.07345076105494051, 0.08688062740666926, 0.10022339592164317, 0.11313349590395828, 0.12527656254543598, 0.13633809679852132, 0.14603161073641596, 0.154106047439897, 0.1603522832396507, 0.16460854390946003, 0.16676459453368778, 0.1667645945336878, 0.16460854390946003, 0.1603522832396507, 0.15410604743989706, 0.146031610736416, 0.13633809679852132, 0.12527656254543593, 0.11313349590395833, 0.10022339592164321, 0.08688062740666926, 0.07345076105494058, 0.06028162335058265, 0.04771428804270877, 0.036074242514475406, 0.025662957830829305, 0.016750080796280722, 0.009566450244305632, 0.004298118432812727, 0.0010815323883923203, 0.0],
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
            "samples": [0.0, 0.0005407661941961602, 0.0021490592164063677, 0.00478322512215282, 0.008375040398140361, 0.012831478915414647, 0.01803712125723769, 0.023857144021354363, 0.0301408116752913, 0.03672538052747026, 0.04344031370333463, 0.050111697960821586, 0.05656674795197914, 0.06263828127271799, 0.06816904839926066, 0.07301580536820798, 0.0770530237199485, 0.08017614161982535, 0.08230427195473002, 0.08338229726684389, 0.0833822972668439, 0.08230427195473002, 0.08017614161982535, 0.07705302371994853, 0.073015805368208, 0.06816904839926066, 0.06263828127271796, 0.05656674795197916, 0.050111697960821606, 0.04344031370333463, 0.03672538052747029, 0.030140811675291326, 0.023857144021354384, 0.018037121257237703, 0.012831478915414652, 0.008375040398140361, 0.004783225122152816, 0.0021490592164063634, 0.0005407661941961602, 0.0],
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
            "samples": [0.0, -0.0005407661941961602, -0.0021490592164063677, -0.00478322512215282, -0.008375040398140361, -0.012831478915414647, -0.01803712125723769, -0.023857144021354363, -0.0301408116752913, -0.03672538052747026, -0.04344031370333463, -0.050111697960821586, -0.05656674795197914, -0.06263828127271799, -0.06816904839926066, -0.07301580536820798, -0.0770530237199485, -0.08017614161982535, -0.08230427195473002, -0.08338229726684389, -0.0833822972668439, -0.08230427195473002, -0.08017614161982535, -0.07705302371994853, -0.073015805368208, -0.06816904839926066, -0.06263828127271796, -0.05656674795197916, -0.050111697960821606, -0.04344031370333463, -0.03672538052747029, -0.030140811675291326, -0.023857144021354384, -0.018037121257237703, -0.012831478915414652, -0.008375040398140361, -0.004783225122152816, -0.0021490592164063634, -0.0005407661941961602, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q3.xy.-x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 6.622475888094236e-20, 2.631838490550177e-19, 5.857761335445659e-19, 1.0256466416312368e-18, 1.57140295820893e-18, 2.208910281350882e-18, 2.9216575062549035e-18, 3.691184854184866e-18, 4.497561971043498e-18, 5.319904113074566e-18, 6.13691305075591e-18, 6.927428681756635e-18, 7.670977066472568e-18, 8.348300692307557e-18, 8.941857233134203e-18, 9.436273886326002e-18, 9.8187455202704e-18, 1.0079366320551338e-17, 1.0211386345339346e-17, 1.0211386345339349e-17, 1.0079366320551338e-17, 9.8187455202704e-18, 9.436273886326005e-18, 8.941857233134205e-18, 8.348300692307557e-18, 7.670977066472565e-18, 6.927428681756638e-18, 6.136913050755913e-18, 5.319904113074566e-18, 4.497561971043503e-18, 3.691184854184869e-18, 2.9216575062549062e-18, 2.2089102813508838e-18, 1.5714029582089305e-18, 1.0256466416312368e-18, 5.857761335445654e-19, 2.631838490550172e-19, 6.622475888094236e-20, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q3.xy.y180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 6.622475888094236e-20, 2.631838490550177e-19, 5.857761335445659e-19, 1.0256466416312368e-18, 1.57140295820893e-18, 2.208910281350882e-18, 2.9216575062549035e-18, 3.691184854184866e-18, 4.497561971043498e-18, 5.319904113074566e-18, 6.13691305075591e-18, 6.927428681756635e-18, 7.670977066472568e-18, 8.348300692307557e-18, 8.941857233134203e-18, 9.436273886326002e-18, 9.8187455202704e-18, 1.0079366320551338e-17, 1.0211386345339346e-17, 1.0211386345339349e-17, 1.0079366320551338e-17, 9.8187455202704e-18, 9.436273886326005e-18, 8.941857233134205e-18, 8.348300692307557e-18, 7.670977066472565e-18, 6.927428681756638e-18, 6.136913050755913e-18, 5.319904113074566e-18, 4.497561971043503e-18, 3.691184854184869e-18, 2.9216575062549062e-18, 2.2089102813508838e-18, 1.5714029582089305e-18, 1.0256466416312368e-18, 5.857761335445654e-19, 2.631838490550172e-19, 6.622475888094236e-20, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q3.xy.y180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0010815323883923203, 0.004298118432812735, 0.00956645024430564, 0.016750080796280722, 0.025662957830829294, 0.03607424251447538, 0.047714288042708726, 0.0602816233505826, 0.07345076105494051, 0.08688062740666926, 0.10022339592164317, 0.11313349590395828, 0.12527656254543598, 0.13633809679852132, 0.14603161073641596, 0.154106047439897, 0.1603522832396507, 0.16460854390946003, 0.16676459453368778, 0.1667645945336878, 0.16460854390946003, 0.1603522832396507, 0.15410604743989706, 0.146031610736416, 0.13633809679852132, 0.12527656254543593, 0.11313349590395833, 0.10022339592164321, 0.08688062740666926, 0.07345076105494058, 0.06028162335058265, 0.04771428804270877, 0.036074242514475406, 0.025662957830829305, 0.016750080796280722, 0.009566450244305632, 0.004298118432812727, 0.0010815323883923203, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q3.xy.y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 3.311237944047118e-20, 1.3159192452750886e-19, 2.9288806677228293e-19, 5.128233208156184e-19, 7.85701479104465e-19, 1.104455140675441e-18, 1.4608287531274518e-18, 1.845592427092433e-18, 2.248780985521749e-18, 2.659952056537283e-18, 3.068456525377955e-18, 3.4637143408783177e-18, 3.835488533236284e-18, 4.1741503461537786e-18, 4.4709286165671015e-18, 4.718136943163001e-18, 4.9093727601352e-18, 5.039683160275669e-18, 5.105693172669673e-18, 5.1056931726696745e-18, 5.039683160275669e-18, 4.9093727601352e-18, 4.7181369431630024e-18, 4.470928616567102e-18, 4.1741503461537786e-18, 3.8354885332362826e-18, 3.463714340878319e-18, 3.0684565253779565e-18, 2.659952056537283e-18, 2.2487809855217515e-18, 1.8455924270924346e-18, 1.4608287531274531e-18, 1.1044551406754419e-18, 7.857014791044653e-19, 5.128233208156184e-19, 2.928880667722827e-19, 1.315919245275086e-19, 3.311237944047118e-20, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q3.xy.y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0005407661941961602, 0.0021490592164063677, 0.00478322512215282, 0.008375040398140361, 0.012831478915414647, 0.01803712125723769, 0.023857144021354363, 0.0301408116752913, 0.03672538052747026, 0.04344031370333463, 0.050111697960821586, 0.05656674795197914, 0.06263828127271799, 0.06816904839926066, 0.07301580536820798, 0.0770530237199485, 0.08017614161982535, 0.08230427195473002, 0.08338229726684389, 0.0833822972668439, 0.08230427195473002, 0.08017614161982535, 0.07705302371994853, 0.073015805368208, 0.06816904839926066, 0.06263828127271796, 0.05656674795197916, 0.050111697960821606, 0.04344031370333463, 0.03672538052747029, 0.030140811675291326, 0.023857144021354384, 0.018037121257237703, 0.012831478915414652, 0.008375040398140361, 0.004783225122152816, 0.0021490592164063634, 0.0005407661941961602, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q3.xy.-y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 3.311237944047118e-20, 1.3159192452750886e-19, 2.9288806677228293e-19, 5.128233208156184e-19, 7.85701479104465e-19, 1.104455140675441e-18, 1.4608287531274518e-18, 1.845592427092433e-18, 2.248780985521749e-18, 2.659952056537283e-18, 3.068456525377955e-18, 3.4637143408783177e-18, 3.835488533236284e-18, 4.1741503461537786e-18, 4.4709286165671015e-18, 4.718136943163001e-18, 4.9093727601352e-18, 5.039683160275669e-18, 5.105693172669673e-18, 5.1056931726696745e-18, 5.039683160275669e-18, 4.9093727601352e-18, 4.7181369431630024e-18, 4.470928616567102e-18, 4.1741503461537786e-18, 3.8354885332362826e-18, 3.463714340878319e-18, 3.0684565253779565e-18, 2.659952056537283e-18, 2.2487809855217515e-18, 1.8455924270924346e-18, 1.4608287531274531e-18, 1.1044551406754419e-18, 7.857014791044653e-19, 5.128233208156184e-19, 2.928880667722827e-19, 1.315919245275086e-19, 3.311237944047118e-20, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q3.xy.-y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.0005407661941961602, -0.0021490592164063677, -0.00478322512215282, -0.008375040398140361, -0.012831478915414647, -0.01803712125723769, -0.023857144021354363, -0.0301408116752913, -0.03672538052747026, -0.04344031370333463, -0.050111697960821586, -0.05656674795197914, -0.06263828127271799, -0.06816904839926066, -0.07301580536820798, -0.0770530237199485, -0.08017614161982535, -0.08230427195473002, -0.08338229726684389, -0.0833822972668439, -0.08230427195473002, -0.08017614161982535, -0.07705302371994853, -0.073015805368208, -0.06816904839926066, -0.06263828127271796, -0.05656674795197916, -0.050111697960821606, -0.04344031370333463, -0.03672538052747029, -0.030140811675291326, -0.023857144021354384, -0.018037121257237703, -0.012831478915414652, -0.008375040398140361, -0.004783225122152816, -0.0021490592164063634, -0.0005407661941961602, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q3.xy.x180_Square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "q3.xy.x180_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q3.xy.x90_Square.wf.I": {
            "type": "constant",
            "sample": 0.05,
        },
        "q3.xy.x90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q3.xy.-x90_Square.wf.I": {
            "type": "constant",
            "sample": -0.125,
        },
        "q3.xy.-x90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q3.xy.y180_Square.wf.I": {
            "type": "constant",
            "sample": -0.11201840403229253,
        },
        "q3.xy.y180_Square.wf.Q": {
            "type": "constant",
            "sample": 0.22349916590013946,
        },
        "q3.xy.y90_Square.wf.I": {
            "type": "constant",
            "sample": -0.056009202016146266,
        },
        "q3.xy.y90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.11174958295006973,
        },
        "q3.xy.-y90_Square.wf.I": {
            "type": "constant",
            "sample": 0.056009202016146266,
        },
        "q3.xy.-y90_Square.wf.Q": {
            "type": "constant",
            "sample": -0.11174958295006973,
        },
        "q3.xy.saturation.wf.I": {
            "type": "constant",
            "sample": 0.053266113103201604,
        },
        "q3.xy.saturation.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q3.xy.cr_q2_q3_Square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "q3.xy.cr_q2_q3_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q3.xy_detuned.zz_q2_q3_Square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "q3.xy_detuned.zz_q2_q3_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q3.resonator.readout.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "q3.resonator.readout.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q3.resonator.const.wf.I": {
            "type": "constant",
            "sample": 0.125,
        },
        "q3.resonator.const.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q4.xy.x180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0010454824370173307, 0.004154852302117222, 0.009247578549070403, 0.01619176224316678, 0.024807552674341083, 0.03487180539609231, 0.0461238615494358, 0.05827229879043301, 0.07100247897582254, 0.08398469712565869, 0.09688272060910604, 0.10936249739296332, 0.12110080781385363, 0.13179363579772657, 0.14116404271648392, 0.14896933995297812, 0.1550073744087179, 0.1591217641629331] + [0.16120594868217908] * 2 + [0.1591217641629331, 0.15500737440871792, 0.14896933995297815, 0.14116404271648395, 0.13179363579772657, 0.12110080781385357, 0.10936249739296335, 0.09688272060910608, 0.08398469712565869, 0.0710024789758226, 0.05827229879043306, 0.04612386154943584, 0.03487180539609234, 0.024807552674341093, 0.01619176224316678, 0.009247578549070394, 0.004154852302117213, 0.0010454824370173307, 0.0],
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
            "samples": [0.0, 0.0005227412185086653, 0.002077426151058611, 0.0046237892745352015, 0.00809588112158339, 0.012403776337170542, 0.017435902698046155, 0.0230619307747179, 0.029136149395216505, 0.03550123948791127, 0.041992348562829344, 0.04844136030455302, 0.05468124869648166, 0.060550403906926814, 0.06589681789886329, 0.07058202135824196, 0.07448466997648906, 0.07750368720435895, 0.07956088208146656] + [0.08060297434108954] * 2 + [0.07956088208146656, 0.07750368720435896, 0.07448466997648907, 0.07058202135824197, 0.06589681789886329, 0.060550403906926786, 0.05468124869648167, 0.04844136030455304, 0.041992348562829344, 0.0355012394879113, 0.02913614939521653, 0.02306193077471792, 0.01743590269804617, 0.012403776337170547, 0.00809588112158339, 0.004623789274535197, 0.0020774261510586064, 0.0005227412185086653, 0.0],
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
            "samples": [0.0, -0.0005227412185086653, -0.002077426151058611, -0.0046237892745352015, -0.00809588112158339, -0.012403776337170542, -0.017435902698046155, -0.0230619307747179, -0.029136149395216505, -0.03550123948791127, -0.041992348562829344, -0.04844136030455302, -0.05468124869648166, -0.060550403906926814, -0.06589681789886329, -0.07058202135824196, -0.07448466997648906, -0.07750368720435895, -0.07956088208146656] + [-0.08060297434108954] * 2 + [-0.07956088208146656, -0.07750368720435896, -0.07448466997648907, -0.07058202135824197, -0.06589681789886329, -0.060550403906926786, -0.05468124869648167, -0.04844136030455304, -0.041992348562829344, -0.0355012394879113, -0.02913614939521653, -0.02306193077471792, -0.01743590269804617, -0.012403776337170547, -0.00809588112158339, -0.004623789274535197, -0.0020774261510586064, -0.0005227412185086653, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q4.xy.-x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 6.401733600290242e-20, 2.544113286358934e-19, 5.662508734991397e-19, 9.914594901824583e-19, 1.5190244988655585e-18, 2.1352822429406924e-18, 2.8242719705416114e-18, 3.568149209633098e-18, 4.347647930463416e-18, 5.142579525614891e-18, 5.932355684331451e-18, 6.696521618952664e-18, 7.415285833169731e-18, 8.070032711383894e-18, 8.643804653372114e-18, 9.121741267225428e-18, 9.491464245693587e-18, 9.743397957840803e-18] + [9.871017452857154e-18] * 2 + [9.743397957840803e-18, 9.491464245693588e-18, 9.12174126722543e-18, 8.643804653372116e-18, 8.070032711383894e-18, 7.415285833169728e-18, 6.696521618952666e-18, 5.932355684331453e-18, 5.142579525614891e-18, 4.347647930463419e-18, 3.568149209633101e-18, 2.824271970541614e-18, 2.135282242940694e-18, 1.519024498865559e-18, 9.914594901824583e-19, 5.662508734991392e-19, 2.5441132863589283e-19, 6.401733600290242e-20, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q4.xy.y180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 6.401733600290242e-20, 2.544113286358934e-19, 5.662508734991397e-19, 9.914594901824583e-19, 1.5190244988655585e-18, 2.1352822429406924e-18, 2.8242719705416114e-18, 3.568149209633098e-18, 4.347647930463416e-18, 5.142579525614891e-18, 5.932355684331451e-18, 6.696521618952664e-18, 7.415285833169731e-18, 8.070032711383894e-18, 8.643804653372114e-18, 9.121741267225428e-18, 9.491464245693587e-18, 9.743397957840803e-18] + [9.871017452857154e-18] * 2 + [9.743397957840803e-18, 9.491464245693588e-18, 9.12174126722543e-18, 8.643804653372116e-18, 8.070032711383894e-18, 7.415285833169728e-18, 6.696521618952666e-18, 5.932355684331453e-18, 5.142579525614891e-18, 4.347647930463419e-18, 3.568149209633101e-18, 2.824271970541614e-18, 2.135282242940694e-18, 1.519024498865559e-18, 9.914594901824583e-19, 5.662508734991392e-19, 2.5441132863589283e-19, 6.401733600290242e-20, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q4.xy.y180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0010454824370173307, 0.004154852302117222, 0.009247578549070403, 0.01619176224316678, 0.024807552674341083, 0.03487180539609231, 0.0461238615494358, 0.05827229879043301, 0.07100247897582254, 0.08398469712565869, 0.09688272060910604, 0.10936249739296332, 0.12110080781385363, 0.13179363579772657, 0.14116404271648392, 0.14896933995297812, 0.1550073744087179, 0.1591217641629331] + [0.16120594868217908] * 2 + [0.1591217641629331, 0.15500737440871792, 0.14896933995297815, 0.14116404271648395, 0.13179363579772657, 0.12110080781385357, 0.10936249739296335, 0.09688272060910608, 0.08398469712565869, 0.0710024789758226, 0.05827229879043306, 0.04612386154943584, 0.03487180539609234, 0.024807552674341093, 0.01619176224316678, 0.009247578549070394, 0.004154852302117213, 0.0010454824370173307, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q4.xy.y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 3.200866800145121e-20, 1.272056643179467e-19, 2.8312543674956984e-19, 4.9572974509122915e-19, 7.595122494327792e-19, 1.0676411214703462e-18, 1.4121359852708057e-18, 1.784074604816549e-18, 2.173823965231708e-18, 2.5712897628074456e-18, 2.9661778421657254e-18, 3.348260809476332e-18, 3.707642916584866e-18, 4.035016355691947e-18, 4.321902326686057e-18, 4.560870633612714e-18, 4.7457321228467934e-18, 4.8716989789204015e-18] + [4.935508726428577e-18] * 2 + [4.8716989789204015e-18, 4.745732122846794e-18, 4.560870633612715e-18, 4.321902326686058e-18, 4.035016355691947e-18, 3.707642916584864e-18, 3.348260809476333e-18, 2.9661778421657266e-18, 2.5712897628074456e-18, 2.1738239652317096e-18, 1.7840746048165507e-18, 1.412135985270807e-18, 1.067641121470347e-18, 7.595122494327795e-19, 4.9572974509122915e-19, 2.831254367495696e-19, 1.2720566431794642e-19, 3.200866800145121e-20, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q4.xy.y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0005227412185086653, 0.002077426151058611, 0.0046237892745352015, 0.00809588112158339, 0.012403776337170542, 0.017435902698046155, 0.0230619307747179, 0.029136149395216505, 0.03550123948791127, 0.041992348562829344, 0.04844136030455302, 0.05468124869648166, 0.060550403906926814, 0.06589681789886329, 0.07058202135824196, 0.07448466997648906, 0.07750368720435895, 0.07956088208146656] + [0.08060297434108954] * 2 + [0.07956088208146656, 0.07750368720435896, 0.07448466997648907, 0.07058202135824197, 0.06589681789886329, 0.060550403906926786, 0.05468124869648167, 0.04844136030455304, 0.041992348562829344, 0.0355012394879113, 0.02913614939521653, 0.02306193077471792, 0.01743590269804617, 0.012403776337170547, 0.00809588112158339, 0.004623789274535197, 0.0020774261510586064, 0.0005227412185086653, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q4.xy.-y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 3.200866800145121e-20, 1.272056643179467e-19, 2.8312543674956984e-19, 4.9572974509122915e-19, 7.595122494327792e-19, 1.0676411214703462e-18, 1.4121359852708057e-18, 1.784074604816549e-18, 2.173823965231708e-18, 2.5712897628074456e-18, 2.9661778421657254e-18, 3.348260809476332e-18, 3.707642916584866e-18, 4.035016355691947e-18, 4.321902326686057e-18, 4.560870633612714e-18, 4.7457321228467934e-18, 4.8716989789204015e-18] + [4.935508726428577e-18] * 2 + [4.8716989789204015e-18, 4.745732122846794e-18, 4.560870633612715e-18, 4.321902326686058e-18, 4.035016355691947e-18, 3.707642916584864e-18, 3.348260809476333e-18, 2.9661778421657266e-18, 2.5712897628074456e-18, 2.1738239652317096e-18, 1.7840746048165507e-18, 1.412135985270807e-18, 1.067641121470347e-18, 7.595122494327795e-19, 4.9572974509122915e-19, 2.831254367495696e-19, 1.2720566431794642e-19, 3.200866800145121e-20, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q4.xy.-y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.0005227412185086653, -0.002077426151058611, -0.0046237892745352015, -0.00809588112158339, -0.012403776337170542, -0.017435902698046155, -0.0230619307747179, -0.029136149395216505, -0.03550123948791127, -0.041992348562829344, -0.04844136030455302, -0.05468124869648166, -0.060550403906926814, -0.06589681789886329, -0.07058202135824196, -0.07448466997648906, -0.07750368720435895, -0.07956088208146656] + [-0.08060297434108954] * 2 + [-0.07956088208146656, -0.07750368720435896, -0.07448466997648907, -0.07058202135824197, -0.06589681789886329, -0.060550403906926786, -0.05468124869648167, -0.04844136030455304, -0.041992348562829344, -0.0355012394879113, -0.02913614939521653, -0.02306193077471792, -0.01743590269804617, -0.012403776337170547, -0.00809588112158339, -0.004623789274535197, -0.0020774261510586064, -0.0005227412185086653, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q4.xy.x180_Square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "q4.xy.x180_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q4.xy.x90_Square.wf.I": {
            "type": "constant",
            "sample": 0.05,
        },
        "q4.xy.x90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q4.xy.-x90_Square.wf.I": {
            "type": "constant",
            "sample": -0.125,
        },
        "q4.xy.-x90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q4.xy.y180_Square.wf.I": {
            "type": "constant",
            "sample": -0.11201840403229253,
        },
        "q4.xy.y180_Square.wf.Q": {
            "type": "constant",
            "sample": 0.22349916590013946,
        },
        "q4.xy.y90_Square.wf.I": {
            "type": "constant",
            "sample": -0.056009202016146266,
        },
        "q4.xy.y90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.11174958295006973,
        },
        "q4.xy.-y90_Square.wf.I": {
            "type": "constant",
            "sample": 0.056009202016146266,
        },
        "q4.xy.-y90_Square.wf.Q": {
            "type": "constant",
            "sample": -0.11174958295006973,
        },
        "q4.xy.saturation.wf.I": {
            "type": "constant",
            "sample": 0.050494213379647726,
        },
        "q4.xy.saturation.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q4.xy.cr_q3_q4_Square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "q4.xy.cr_q3_q4_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q4.xy_detuned.zz_q3_q4_Square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "q4.xy_detuned.zz_q3_q4_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q4.resonator.readout.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "q4.resonator.readout.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q4.resonator.const.wf.I": {
            "type": "constant",
            "sample": 0.125,
        },
        "q4.resonator.const.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q5.xy.x180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0007476787839983893, 0.002971350648225588, 0.0066134236594391806, 0.011579570039741652, 0.017741169206479807, 0.024938638977774204, 0.03298556866720522, 0.041673547022674215, 0.05077755996835955, 0.060061818351085886, 0.06928586475553708, 0.0782108012250065, 0.08660547659298821, 0.09425247317697152, 0.10095373778221371, 0.10653571117545134, 0.11085382317787522, 0.1137962369568224, 0.11528674554099697, 0.11528674554099698, 0.1137962369568224, 0.11085382317787523, 0.10653571117545137, 0.10095373778221374, 0.09425247317697152, 0.08660547659298819, 0.07821080122500652, 0.06928586475553711, 0.060061818351085886, 0.050777559968359594, 0.04167354702267425, 0.03298556866720525, 0.024938638977774225, 0.017741169206479813, 0.011579570039741652, 0.0066134236594391745, 0.0029713506482255815, 0.0007476787839983893, 0.0],
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
            "samples": [0.0, 0.00037383939199919466, 0.001485675324112794, 0.0033067118297195903, 0.005789785019870826, 0.008870584603239903, 0.012469319488887102, 0.01649278433360261, 0.020836773511337107, 0.025388779984179776, 0.030030909175542943, 0.03464293237776854, 0.03910540061250325, 0.04330273829649411, 0.04712623658848576, 0.050476868891106856, 0.05326785558772567, 0.05542691158893761, 0.0568981184784112, 0.05764337277049848, 0.05764337277049849, 0.0568981184784112, 0.055426911588937616, 0.05326785558772568, 0.05047686889110687, 0.04712623658848576, 0.043302738296494094, 0.03910540061250326, 0.034642932377768554, 0.030030909175542943, 0.025388779984179797, 0.020836773511337125, 0.016492784333602625, 0.012469319488887113, 0.008870584603239907, 0.005789785019870826, 0.0033067118297195872, 0.0014856753241127907, 0.00037383939199919466, 0.0],
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
            "samples": [0.0, -0.00037383939199919466, -0.001485675324112794, -0.0033067118297195903, -0.005789785019870826, -0.008870584603239903, -0.012469319488887102, -0.01649278433360261, -0.020836773511337107, -0.025388779984179776, -0.030030909175542943, -0.03464293237776854, -0.03910540061250325, -0.04330273829649411, -0.04712623658848576, -0.050476868891106856, -0.05326785558772567, -0.05542691158893761, -0.0568981184784112, -0.05764337277049848, -0.05764337277049849, -0.0568981184784112, -0.055426911588937616, -0.05326785558772568, -0.05047686889110687, -0.04712623658848576, -0.043302738296494094, -0.03910540061250326, -0.034642932377768554, -0.030030909175542943, -0.025388779984179797, -0.020836773511337125, -0.016492784333602625, -0.012469319488887113, -0.008870584603239907, -0.005789785019870826, -0.0033067118297195872, -0.0014856753241127907, -0.00037383939199919466, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q5.xy.-x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 4.578212148070064e-20, 1.8194275302469397e-19, 4.049554057968784e-19, 7.090441692336102e-19, 1.0863333040923541e-18, 1.52705121996113e-18, 2.019783554317405e-18, 2.5517687985217346e-18, 3.109228814188215e-18, 3.6777256797313546e-18, 4.242535624951245e-18, 4.789030368947705e-18, 5.3030559849117015e-18, 5.771299479394997e-18, 6.181633591847462e-18, 6.523430884295169e-18, 6.787838986401578e-18, 6.968009867209315e-18] + [7.059277195544867e-18] * 2 + [6.968009867209315e-18, 6.787838986401579e-18, 6.523430884295171e-18, 6.1816335918474636e-18, 5.771299479394997e-18, 5.3030559849117e-18, 4.789030368947707e-18, 4.242535624951246e-18, 3.6777256797313546e-18, 3.1092288141882177e-18, 2.5517687985217365e-18, 2.019783554317407e-18, 1.5270512199611313e-18, 1.0863333040923545e-18, 7.090441692336102e-19, 4.04955405796878e-19, 1.8194275302469358e-19, 4.578212148070064e-20, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q5.xy.y180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 4.578212148070064e-20, 1.8194275302469397e-19, 4.049554057968784e-19, 7.090441692336102e-19, 1.0863333040923541e-18, 1.52705121996113e-18, 2.019783554317405e-18, 2.5517687985217346e-18, 3.109228814188215e-18, 3.6777256797313546e-18, 4.242535624951245e-18, 4.789030368947705e-18, 5.3030559849117015e-18, 5.771299479394997e-18, 6.181633591847462e-18, 6.523430884295169e-18, 6.787838986401578e-18, 6.968009867209315e-18] + [7.059277195544867e-18] * 2 + [6.968009867209315e-18, 6.787838986401579e-18, 6.523430884295171e-18, 6.1816335918474636e-18, 5.771299479394997e-18, 5.3030559849117e-18, 4.789030368947707e-18, 4.242535624951246e-18, 3.6777256797313546e-18, 3.1092288141882177e-18, 2.5517687985217365e-18, 2.019783554317407e-18, 1.5270512199611313e-18, 1.0863333040923545e-18, 7.090441692336102e-19, 4.04955405796878e-19, 1.8194275302469358e-19, 4.578212148070064e-20, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q5.xy.y180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0007476787839983893, 0.002971350648225588, 0.0066134236594391806, 0.011579570039741652, 0.017741169206479807, 0.024938638977774204, 0.03298556866720522, 0.041673547022674215, 0.05077755996835955, 0.060061818351085886, 0.06928586475553708, 0.0782108012250065, 0.08660547659298821, 0.09425247317697152, 0.10095373778221371, 0.10653571117545134, 0.11085382317787522, 0.1137962369568224, 0.11528674554099697, 0.11528674554099698, 0.1137962369568224, 0.11085382317787523, 0.10653571117545137, 0.10095373778221374, 0.09425247317697152, 0.08660547659298819, 0.07821080122500652, 0.06928586475553711, 0.060061818351085886, 0.050777559968359594, 0.04167354702267425, 0.03298556866720525, 0.024938638977774225, 0.017741169206479813, 0.011579570039741652, 0.0066134236594391745, 0.0029713506482255815, 0.0007476787839983893, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q5.xy.y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 2.289106074035032e-20, 9.097137651234698e-20, 2.024777028984392e-19, 3.545220846168051e-19, 5.431666520461771e-19, 7.63525609980565e-19, 1.0098917771587025e-18, 1.2758843992608673e-18, 1.5546144070941075e-18, 1.8388628398656773e-18, 2.1212678124756224e-18, 2.3945151844738526e-18, 2.6515279924558508e-18, 2.8856497396974984e-18, 3.090816795923731e-18, 3.2617154421475846e-18, 3.393919493200789e-18, 3.4840049336046575e-18] + [3.5296385977724334e-18] * 2 + [3.4840049336046575e-18, 3.3939194932007896e-18, 3.2617154421475854e-18, 3.0908167959237318e-18, 2.8856497396974984e-18, 2.65152799245585e-18, 2.3945151844738533e-18, 2.121267812475623e-18, 1.8388628398656773e-18, 1.5546144070941088e-18, 1.2758843992608683e-18, 1.0098917771587034e-18, 7.635256099805656e-19, 5.431666520461773e-19, 3.545220846168051e-19, 2.02477702898439e-19, 9.097137651234679e-20, 2.289106074035032e-20, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q5.xy.y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.00037383939199919466, 0.001485675324112794, 0.0033067118297195903, 0.005789785019870826, 0.008870584603239903, 0.012469319488887102, 0.01649278433360261, 0.020836773511337107, 0.025388779984179776, 0.030030909175542943, 0.03464293237776854, 0.03910540061250325, 0.04330273829649411, 0.04712623658848576, 0.050476868891106856, 0.05326785558772567, 0.05542691158893761, 0.0568981184784112, 0.05764337277049848, 0.05764337277049849, 0.0568981184784112, 0.055426911588937616, 0.05326785558772568, 0.05047686889110687, 0.04712623658848576, 0.043302738296494094, 0.03910540061250326, 0.034642932377768554, 0.030030909175542943, 0.025388779984179797, 0.020836773511337125, 0.016492784333602625, 0.012469319488887113, 0.008870584603239907, 0.005789785019870826, 0.0033067118297195872, 0.0014856753241127907, 0.00037383939199919466, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q5.xy.-y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 2.289106074035032e-20, 9.097137651234698e-20, 2.024777028984392e-19, 3.545220846168051e-19, 5.431666520461771e-19, 7.63525609980565e-19, 1.0098917771587025e-18, 1.2758843992608673e-18, 1.5546144070941075e-18, 1.8388628398656773e-18, 2.1212678124756224e-18, 2.3945151844738526e-18, 2.6515279924558508e-18, 2.8856497396974984e-18, 3.090816795923731e-18, 3.2617154421475846e-18, 3.393919493200789e-18, 3.4840049336046575e-18] + [3.5296385977724334e-18] * 2 + [3.4840049336046575e-18, 3.3939194932007896e-18, 3.2617154421475854e-18, 3.0908167959237318e-18, 2.8856497396974984e-18, 2.65152799245585e-18, 2.3945151844738533e-18, 2.121267812475623e-18, 1.8388628398656773e-18, 1.5546144070941088e-18, 1.2758843992608683e-18, 1.0098917771587034e-18, 7.635256099805656e-19, 5.431666520461773e-19, 3.545220846168051e-19, 2.02477702898439e-19, 9.097137651234679e-20, 2.289106074035032e-20, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q5.xy.-y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.00037383939199919466, -0.001485675324112794, -0.0033067118297195903, -0.005789785019870826, -0.008870584603239903, -0.012469319488887102, -0.01649278433360261, -0.020836773511337107, -0.025388779984179776, -0.030030909175542943, -0.03464293237776854, -0.03910540061250325, -0.04330273829649411, -0.04712623658848576, -0.050476868891106856, -0.05326785558772567, -0.05542691158893761, -0.0568981184784112, -0.05764337277049848, -0.05764337277049849, -0.0568981184784112, -0.055426911588937616, -0.05326785558772568, -0.05047686889110687, -0.04712623658848576, -0.043302738296494094, -0.03910540061250326, -0.034642932377768554, -0.030030909175542943, -0.025388779984179797, -0.020836773511337125, -0.016492784333602625, -0.012469319488887113, -0.008870584603239907, -0.005789785019870826, -0.0033067118297195872, -0.0014856753241127907, -0.00037383939199919466, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q5.xy.x180_Square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "q5.xy.x180_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q5.xy.x90_Square.wf.I": {
            "type": "constant",
            "sample": 0.05,
        },
        "q5.xy.x90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q5.xy.-x90_Square.wf.I": {
            "type": "constant",
            "sample": -0.125,
        },
        "q5.xy.-x90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q5.xy.y180_Square.wf.I": {
            "type": "constant",
            "sample": -0.11201840403229253,
        },
        "q5.xy.y180_Square.wf.Q": {
            "type": "constant",
            "sample": 0.22349916590013946,
        },
        "q5.xy.y90_Square.wf.I": {
            "type": "constant",
            "sample": -0.056009202016146266,
        },
        "q5.xy.y90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.11174958295006973,
        },
        "q5.xy.-y90_Square.wf.I": {
            "type": "constant",
            "sample": 0.056009202016146266,
        },
        "q5.xy.-y90_Square.wf.Q": {
            "type": "constant",
            "sample": -0.11174958295006973,
        },
        "q5.xy.saturation.wf.I": {
            "type": "constant",
            "sample": 0.05521676406770869,
        },
        "q5.xy.saturation.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q5.xy.cr_q4_q5_Square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "q5.xy.cr_q4_q5_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q5.xy_detuned.zz_q4_q5_Square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "q5.xy_detuned.zz_q4_q5_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q5.resonator.readout.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "q5.resonator.readout.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q5.resonator.const.wf.I": {
            "type": "constant",
            "sample": 0.125,
        },
        "q5.resonator.const.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q6.xy.x180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0009296953956100164, 0.003694702960040281, 0.008223410449763675, 0.014398526719616937, 0.022060119501850165, 0.031009757567852982, 0.041015649992744464, 0.051818649418573295, 0.06313896383476499, 0.07468340304422766, 0.08615297213545103, 0.09725061529365987, 0.10768890939038021, 0.1171975080914905, 0.12553014368526905, 0.13247100528676906, 0.13784032822637848, 0.14149904986033693, 0.14335241122016293, 0.14335241122016296, 0.14149904986033693, 0.13784032822637848, 0.13247100528676908, 0.12553014368526907, 0.1171975080914905, 0.10768890939038017, 0.09725061529365991, 0.08615297213545106, 0.07468340304422766, 0.06313896383476504, 0.051818649418573344, 0.04101564999274449, 0.031009757567853007, 0.022060119501850176, 0.014398526719616937, 0.008223410449763666, 0.003694702960040273, 0.0009296953956100164, 0.0],
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
            "samples": [0.0, 0.0004648476978050082, 0.0018473514800201405, 0.004111705224881837, 0.007199263359808469, 0.011030059750925083, 0.015504878783926491, 0.020507824996372232, 0.025909324709286648, 0.03156948191738249, 0.03734170152211383, 0.04307648606772552, 0.048625307646829936, 0.05384445469519011, 0.05859875404574525, 0.06276507184263452, 0.06623550264338453, 0.06892016411318924, 0.07074952493016846, 0.07167620561008146, 0.07167620561008148, 0.07074952493016846, 0.06892016411318924, 0.06623550264338454, 0.06276507184263454, 0.05859875404574525, 0.053844454695190086, 0.04862530764682996, 0.04307648606772553, 0.03734170152211383, 0.03156948191738252, 0.025909324709286672, 0.020507824996372246, 0.015504878783926503, 0.011030059750925088, 0.007199263359808469, 0.004111705224881833, 0.0018473514800201366, 0.0004648476978050082, 0.0],
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
            "samples": [0.0, -0.0004648476978050082, -0.0018473514800201405, -0.004111705224881837, -0.007199263359808469, -0.011030059750925083, -0.015504878783926491, -0.020507824996372232, -0.025909324709286648, -0.03156948191738249, -0.03734170152211383, -0.04307648606772552, -0.048625307646829936, -0.05384445469519011, -0.05859875404574525, -0.06276507184263452, -0.06623550264338453, -0.06892016411318924, -0.07074952493016846, -0.07167620561008146, -0.07167620561008148, -0.07074952493016846, -0.06892016411318924, -0.06623550264338454, -0.06276507184263454, -0.05859875404574525, -0.053844454695190086, -0.04862530764682996, -0.04307648606772553, -0.03734170152211383, -0.03156948191738252, -0.025909324709286672, -0.020507824996372246, -0.015504878783926503, -0.011030059750925088, -0.007199263359808469, -0.004111705224881833, -0.0018473514800201366, -0.0004648476978050082, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q6.xy.-x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 5.692742452079194e-20, 2.2623530769067906e-19, 5.03538664268899e-19, 8.81655482980826e-19, 1.3507927368374454e-18, 1.8988000173903284e-18, 2.5114842239281333e-18, 3.1729771573297322e-18, 3.8661464980862714e-18, 4.573039524377255e-18, 5.275348078135561e-18, 5.95488273672456e-18, 6.594043909429924e-18, 7.176277657614494e-18, 7.686504433033604e-18, 8.111509630213692e-18, 8.44028583779275e-18, 8.664317924692668e-18, 8.777803577541383e-18, 8.777803577541385e-18, 8.664317924692668e-18, 8.44028583779275e-18, 8.111509630213693e-18, 7.686504433033605e-18, 7.176277657614494e-18, 6.594043909429921e-18, 5.954882736724563e-18, 5.275348078135563e-18, 4.573039524377255e-18, 3.866146498086275e-18, 3.172977157329735e-18, 2.5114842239281352e-18, 1.89880001739033e-18, 1.350792736837446e-18, 8.81655482980826e-19, 5.035386642688985e-19, 2.262353076906786e-19, 5.692742452079194e-20, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q6.xy.y180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 5.692742452079194e-20, 2.2623530769067906e-19, 5.03538664268899e-19, 8.81655482980826e-19, 1.3507927368374454e-18, 1.8988000173903284e-18, 2.5114842239281333e-18, 3.1729771573297322e-18, 3.8661464980862714e-18, 4.573039524377255e-18, 5.275348078135561e-18, 5.95488273672456e-18, 6.594043909429924e-18, 7.176277657614494e-18, 7.686504433033604e-18, 8.111509630213692e-18, 8.44028583779275e-18, 8.664317924692668e-18, 8.777803577541383e-18, 8.777803577541385e-18, 8.664317924692668e-18, 8.44028583779275e-18, 8.111509630213693e-18, 7.686504433033605e-18, 7.176277657614494e-18, 6.594043909429921e-18, 5.954882736724563e-18, 5.275348078135563e-18, 4.573039524377255e-18, 3.866146498086275e-18, 3.172977157329735e-18, 2.5114842239281352e-18, 1.89880001739033e-18, 1.350792736837446e-18, 8.81655482980826e-19, 5.035386642688985e-19, 2.262353076906786e-19, 5.692742452079194e-20, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q6.xy.y180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0009296953956100164, 0.003694702960040281, 0.008223410449763675, 0.014398526719616937, 0.022060119501850165, 0.031009757567852982, 0.041015649992744464, 0.051818649418573295, 0.06313896383476499, 0.07468340304422766, 0.08615297213545103, 0.09725061529365987, 0.10768890939038021, 0.1171975080914905, 0.12553014368526905, 0.13247100528676906, 0.13784032822637848, 0.14149904986033693, 0.14335241122016293, 0.14335241122016296, 0.14149904986033693, 0.13784032822637848, 0.13247100528676908, 0.12553014368526907, 0.1171975080914905, 0.10768890939038017, 0.09725061529365991, 0.08615297213545106, 0.07468340304422766, 0.06313896383476504, 0.051818649418573344, 0.04101564999274449, 0.031009757567853007, 0.022060119501850176, 0.014398526719616937, 0.008223410449763666, 0.003694702960040273, 0.0009296953956100164, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q6.xy.y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 2.846371226039597e-20, 1.1311765384533953e-19, 2.517693321344495e-19, 4.40827741490413e-19, 6.753963684187227e-19, 9.494000086951642e-19, 1.2557421119640666e-18, 1.5864885786648661e-18, 1.9330732490431357e-18, 2.2865197621886276e-18, 2.6376740390677803e-18, 2.97744136836228e-18, 3.297021954714962e-18, 3.588138828807247e-18, 3.843252216516802e-18, 4.055754815106846e-18, 4.220142918896375e-18, 4.332158962346334e-18, 4.388901788770692e-18, 4.3889017887706924e-18, 4.332158962346334e-18, 4.220142918896375e-18, 4.0557548151068465e-18, 3.843252216516803e-18, 3.588138828807247e-18, 3.2970219547149605e-18, 2.9774413683622814e-18, 2.6376740390677815e-18, 2.2865197621886276e-18, 1.9330732490431376e-18, 1.5864885786648674e-18, 1.2557421119640676e-18, 9.49400008695165e-19, 6.75396368418723e-19, 4.40827741490413e-19, 2.5176933213444926e-19, 1.131176538453393e-19, 2.846371226039597e-20, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q6.xy.y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0004648476978050082, 0.0018473514800201405, 0.004111705224881837, 0.007199263359808469, 0.011030059750925083, 0.015504878783926491, 0.020507824996372232, 0.025909324709286648, 0.03156948191738249, 0.03734170152211383, 0.04307648606772552, 0.048625307646829936, 0.05384445469519011, 0.05859875404574525, 0.06276507184263452, 0.06623550264338453, 0.06892016411318924, 0.07074952493016846, 0.07167620561008146, 0.07167620561008148, 0.07074952493016846, 0.06892016411318924, 0.06623550264338454, 0.06276507184263454, 0.05859875404574525, 0.053844454695190086, 0.04862530764682996, 0.04307648606772553, 0.03734170152211383, 0.03156948191738252, 0.025909324709286672, 0.020507824996372246, 0.015504878783926503, 0.011030059750925088, 0.007199263359808469, 0.004111705224881833, 0.0018473514800201366, 0.0004648476978050082, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q6.xy.-y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 2.846371226039597e-20, 1.1311765384533953e-19, 2.517693321344495e-19, 4.40827741490413e-19, 6.753963684187227e-19, 9.494000086951642e-19, 1.2557421119640666e-18, 1.5864885786648661e-18, 1.9330732490431357e-18, 2.2865197621886276e-18, 2.6376740390677803e-18, 2.97744136836228e-18, 3.297021954714962e-18, 3.588138828807247e-18, 3.843252216516802e-18, 4.055754815106846e-18, 4.220142918896375e-18, 4.332158962346334e-18, 4.388901788770692e-18, 4.3889017887706924e-18, 4.332158962346334e-18, 4.220142918896375e-18, 4.0557548151068465e-18, 3.843252216516803e-18, 3.588138828807247e-18, 3.2970219547149605e-18, 2.9774413683622814e-18, 2.6376740390677815e-18, 2.2865197621886276e-18, 1.9330732490431376e-18, 1.5864885786648674e-18, 1.2557421119640676e-18, 9.49400008695165e-19, 6.75396368418723e-19, 4.40827741490413e-19, 2.5176933213444926e-19, 1.131176538453393e-19, 2.846371226039597e-20, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q6.xy.-y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.0004648476978050082, -0.0018473514800201405, -0.004111705224881837, -0.007199263359808469, -0.011030059750925083, -0.015504878783926491, -0.020507824996372232, -0.025909324709286648, -0.03156948191738249, -0.03734170152211383, -0.04307648606772552, -0.048625307646829936, -0.05384445469519011, -0.05859875404574525, -0.06276507184263452, -0.06623550264338453, -0.06892016411318924, -0.07074952493016846, -0.07167620561008146, -0.07167620561008148, -0.07074952493016846, -0.06892016411318924, -0.06623550264338454, -0.06276507184263454, -0.05859875404574525, -0.053844454695190086, -0.04862530764682996, -0.04307648606772553, -0.03734170152211383, -0.03156948191738252, -0.025909324709286672, -0.020507824996372246, -0.015504878783926503, -0.011030059750925088, -0.007199263359808469, -0.004111705224881833, -0.0018473514800201366, -0.0004648476978050082, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q6.xy.x180_Square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "q6.xy.x180_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q6.xy.x90_Square.wf.I": {
            "type": "constant",
            "sample": 0.05,
        },
        "q6.xy.x90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q6.xy.-x90_Square.wf.I": {
            "type": "constant",
            "sample": -0.125,
        },
        "q6.xy.-x90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q6.xy.y180_Square.wf.I": {
            "type": "constant",
            "sample": -0.11201840403229253,
        },
        "q6.xy.y180_Square.wf.Q": {
            "type": "constant",
            "sample": 0.22349916590013946,
        },
        "q6.xy.y90_Square.wf.I": {
            "type": "constant",
            "sample": -0.056009202016146266,
        },
        "q6.xy.y90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.11174958295006973,
        },
        "q6.xy.-y90_Square.wf.I": {
            "type": "constant",
            "sample": 0.056009202016146266,
        },
        "q6.xy.-y90_Square.wf.Q": {
            "type": "constant",
            "sample": -0.11174958295006973,
        },
        "q6.xy.saturation.wf.I": {
            "type": "constant",
            "sample": 0.06342628178578913,
        },
        "q6.xy.saturation.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q6.xy.cr_q5_q6_Square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "q6.xy.cr_q5_q6_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q6.xy_detuned.zz_q5_q6_Square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "q6.xy_detuned.zz_q5_q6_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q6.resonator.readout.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "q6.resonator.readout.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q6.resonator.const.wf.I": {
            "type": "constant",
            "sample": 0.125,
        },
        "q6.resonator.const.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q7.xy.x180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.00020538635070153783, 0.000816226004207466, 0.001816698534351283, 0.0031808922281263, 0.004873475185441714, 0.006850610396775961, 0.009061091098696824, 0.011447667002136619, 0.01394852704480689, 0.0164989002652438, 0.01903273333668742, 0.021484401313548646, 0.023790407283028676, 0.025891026901807158, 0.027731855225162447, 0.02926521576646226, 0.030451395293124153, 0.03125967237847901, 0.03166911307058455, 0.03166911307058456, 0.03125967237847901, 0.030451395293124156, 0.029265215766462266, 0.027731855225162454, 0.025891026901807158, 0.023790407283028663, 0.021484401313548653, 0.019032733336687428, 0.0164989002652438, 0.013948527044806903, 0.01144766700213663, 0.00906109109869683, 0.006850610396775966, 0.004873475185441715, 0.0031808922281263, 0.0018166985343512812, 0.0008162260042074642, 0.00020538635070153783, 0.0],
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
            "samples": [0.0, 0.00010269317535076891, 0.000408113002103733, 0.0009083492671756414, 0.00159044611406315, 0.002436737592720857, 0.0034253051983879805, 0.004530545549348412, 0.0057238335010683095, 0.006974263522403445, 0.0082494501326219, 0.00951636666834371, 0.010742200656774323, 0.011895203641514338, 0.012945513450903579, 0.013865927612581224, 0.01463260788323113, 0.015225697646562076, 0.015629836189239504, 0.015834556535292275, 0.01583455653529228, 0.015629836189239504, 0.015225697646562078, 0.014632607883231133, 0.013865927612581227, 0.012945513450903579, 0.011895203641514331, 0.010742200656774326, 0.009516366668343714, 0.0082494501326219, 0.006974263522403452, 0.005723833501068315, 0.004530545549348415, 0.003425305198387983, 0.0024367375927208577, 0.00159044611406315, 0.0009083492671756406, 0.0004081130021037321, 0.00010269317535076891, 0.0],
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
            "samples": [0.0, -0.00010269317535076891, -0.000408113002103733, -0.0009083492671756414, -0.00159044611406315, -0.002436737592720857, -0.0034253051983879805, -0.004530545549348412, -0.0057238335010683095, -0.006974263522403445, -0.0082494501326219, -0.00951636666834371, -0.010742200656774323, -0.011895203641514338, -0.012945513450903579, -0.013865927612581224, -0.01463260788323113, -0.015225697646562076, -0.015629836189239504, -0.015834556535292275, -0.01583455653529228, -0.015629836189239504, -0.015225697646562078, -0.014632607883231133, -0.013865927612581227, -0.012945513450903579, -0.011895203641514331, -0.010742200656774326, -0.009516366668343714, -0.0082494501326219, -0.006974263522403452, -0.005723833501068315, -0.004530545549348415, -0.003425305198387983, -0.0024367375927208577, -0.00159044611406315, -0.0009083492671756406, -0.0004081130021037321, -0.00010269317535076891, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q7.xy.-x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 1.2576286848759702e-20, 4.997942817167536e-20, 1.1124070225544932e-19, 1.9477347428037827e-19, 2.984142893287624e-19, 4.19478904730863e-19, 5.548318105400819e-19, 7.009674375935694e-19, 8.541009499121524e-19, 1.0102662699641118e-18, 1.1654187979899686e-18, 1.315540165011727e-18, 1.4567423064786474e-18, 1.5853681610968075e-18, 1.6980863867956497e-18, 1.791977640737733e-18, 1.8646101887647636e-18, 1.9141028860349623e-18, 1.9391738976863488e-18, 1.939173897686349e-18, 1.9141028860349623e-18, 1.8646101887647636e-18, 1.7919776407377336e-18, 1.69808638679565e-18, 1.5853681610968075e-18, 1.4567423064786466e-18, 1.3155401650117274e-18, 1.165418797989969e-18, 1.0102662699641118e-18, 8.541009499121533e-19, 7.0096743759357e-19, 5.548318105400824e-19, 4.194789047308633e-19, 2.984142893287625e-19, 1.9477347428037827e-19, 1.1124070225544922e-19, 4.9979428171675257e-20, 1.2576286848759702e-20, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q7.xy.y180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 1.2576286848759702e-20, 4.997942817167536e-20, 1.1124070225544932e-19, 1.9477347428037827e-19, 2.984142893287624e-19, 4.19478904730863e-19, 5.548318105400819e-19, 7.009674375935694e-19, 8.541009499121524e-19, 1.0102662699641118e-18, 1.1654187979899686e-18, 1.315540165011727e-18, 1.4567423064786474e-18, 1.5853681610968075e-18, 1.6980863867956497e-18, 1.791977640737733e-18, 1.8646101887647636e-18, 1.9141028860349623e-18, 1.9391738976863488e-18, 1.939173897686349e-18, 1.9141028860349623e-18, 1.8646101887647636e-18, 1.7919776407377336e-18, 1.69808638679565e-18, 1.5853681610968075e-18, 1.4567423064786466e-18, 1.3155401650117274e-18, 1.165418797989969e-18, 1.0102662699641118e-18, 8.541009499121533e-19, 7.0096743759357e-19, 5.548318105400824e-19, 4.194789047308633e-19, 2.984142893287625e-19, 1.9477347428037827e-19, 1.1124070225544922e-19, 4.9979428171675257e-20, 1.2576286848759702e-20, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q7.xy.y180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.00020538635070153783, 0.000816226004207466, 0.001816698534351283, 0.0031808922281263, 0.004873475185441714, 0.006850610396775961, 0.009061091098696824, 0.011447667002136619, 0.01394852704480689, 0.0164989002652438, 0.01903273333668742, 0.021484401313548646, 0.023790407283028676, 0.025891026901807158, 0.027731855225162447, 0.02926521576646226, 0.030451395293124153, 0.03125967237847901, 0.03166911307058455, 0.03166911307058456, 0.03125967237847901, 0.030451395293124156, 0.029265215766462266, 0.027731855225162454, 0.025891026901807158, 0.023790407283028663, 0.021484401313548653, 0.019032733336687428, 0.0164989002652438, 0.013948527044806903, 0.01144766700213663, 0.00906109109869683, 0.006850610396775966, 0.004873475185441715, 0.0031808922281263, 0.0018166985343512812, 0.0008162260042074642, 0.00020538635070153783, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q7.xy.y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 6.288143424379851e-21, 2.498971408583768e-20, 5.562035112772466e-20, 9.738673714018913e-20, 1.492071446643812e-19, 2.097394523654315e-19, 2.7741590527004096e-19, 3.504837187967847e-19, 4.270504749560762e-19, 5.051331349820559e-19, 5.827093989949843e-19, 6.577700825058635e-19, 7.283711532393237e-19, 7.926840805484037e-19, 8.490431933978248e-19, 8.959888203688666e-19, 9.323050943823818e-19, 9.570514430174812e-19, 9.695869488431744e-19, 9.695869488431746e-19, 9.570514430174812e-19, 9.323050943823818e-19, 8.959888203688668e-19, 8.49043193397825e-19, 7.926840805484037e-19, 7.283711532393233e-19, 6.577700825058637e-19, 5.827093989949845e-19, 5.051331349820559e-19, 4.2705047495607663e-19, 3.50483718796785e-19, 2.774159052700412e-19, 2.0973945236543165e-19, 1.4920714466438126e-19, 9.738673714018913e-20, 5.562035112772461e-20, 2.4989714085837628e-20, 6.288143424379851e-21, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q7.xy.y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.00010269317535076891, 0.000408113002103733, 0.0009083492671756414, 0.00159044611406315, 0.002436737592720857, 0.0034253051983879805, 0.004530545549348412, 0.0057238335010683095, 0.006974263522403445, 0.0082494501326219, 0.00951636666834371, 0.010742200656774323, 0.011895203641514338, 0.012945513450903579, 0.013865927612581224, 0.01463260788323113, 0.015225697646562076, 0.015629836189239504, 0.015834556535292275, 0.01583455653529228, 0.015629836189239504, 0.015225697646562078, 0.014632607883231133, 0.013865927612581227, 0.012945513450903579, 0.011895203641514331, 0.010742200656774326, 0.009516366668343714, 0.0082494501326219, 0.006974263522403452, 0.005723833501068315, 0.004530545549348415, 0.003425305198387983, 0.0024367375927208577, 0.00159044611406315, 0.0009083492671756406, 0.0004081130021037321, 0.00010269317535076891, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q7.xy.-y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 6.288143424379851e-21, 2.498971408583768e-20, 5.562035112772466e-20, 9.738673714018913e-20, 1.492071446643812e-19, 2.097394523654315e-19, 2.7741590527004096e-19, 3.504837187967847e-19, 4.270504749560762e-19, 5.051331349820559e-19, 5.827093989949843e-19, 6.577700825058635e-19, 7.283711532393237e-19, 7.926840805484037e-19, 8.490431933978248e-19, 8.959888203688666e-19, 9.323050943823818e-19, 9.570514430174812e-19, 9.695869488431744e-19, 9.695869488431746e-19, 9.570514430174812e-19, 9.323050943823818e-19, 8.959888203688668e-19, 8.49043193397825e-19, 7.926840805484037e-19, 7.283711532393233e-19, 6.577700825058637e-19, 5.827093989949845e-19, 5.051331349820559e-19, 4.2705047495607663e-19, 3.50483718796785e-19, 2.774159052700412e-19, 2.0973945236543165e-19, 1.4920714466438126e-19, 9.738673714018913e-20, 5.562035112772461e-20, 2.4989714085837628e-20, 6.288143424379851e-21, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q7.xy.-y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.00010269317535076891, -0.000408113002103733, -0.0009083492671756414, -0.00159044611406315, -0.002436737592720857, -0.0034253051983879805, -0.004530545549348412, -0.0057238335010683095, -0.006974263522403445, -0.0082494501326219, -0.00951636666834371, -0.010742200656774323, -0.011895203641514338, -0.012945513450903579, -0.013865927612581224, -0.01463260788323113, -0.015225697646562076, -0.015629836189239504, -0.015834556535292275, -0.01583455653529228, -0.015629836189239504, -0.015225697646562078, -0.014632607883231133, -0.013865927612581227, -0.012945513450903579, -0.011895203641514331, -0.010742200656774326, -0.009516366668343714, -0.0082494501326219, -0.006974263522403452, -0.005723833501068315, -0.004530545549348415, -0.003425305198387983, -0.0024367375927208577, -0.00159044611406315, -0.0009083492671756406, -0.0004081130021037321, -0.00010269317535076891, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q7.xy.x180_Square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "q7.xy.x180_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q7.xy.x90_Square.wf.I": {
            "type": "constant",
            "sample": 0.05,
        },
        "q7.xy.x90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q7.xy.-x90_Square.wf.I": {
            "type": "constant",
            "sample": -0.125,
        },
        "q7.xy.-x90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q7.xy.y180_Square.wf.I": {
            "type": "constant",
            "sample": -0.11201840403229253,
        },
        "q7.xy.y180_Square.wf.Q": {
            "type": "constant",
            "sample": 0.22349916590013946,
        },
        "q7.xy.y90_Square.wf.I": {
            "type": "constant",
            "sample": -0.056009202016146266,
        },
        "q7.xy.y90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.11174958295006973,
        },
        "q7.xy.-y90_Square.wf.I": {
            "type": "constant",
            "sample": 0.056009202016146266,
        },
        "q7.xy.-y90_Square.wf.Q": {
            "type": "constant",
            "sample": -0.11174958295006973,
        },
        "q7.xy.saturation.wf.I": {
            "type": "constant",
            "sample": 0.007784263341854068,
        },
        "q7.xy.saturation.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q7.xy.cr_q6_q7_Square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "q7.xy.cr_q6_q7_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q7.xy_detuned.zz_q6_q7_Square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "q7.xy_detuned.zz_q6_q7_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q7.resonator.readout.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "q7.resonator.readout.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q7.resonator.const.wf.I": {
            "type": "constant",
            "sample": 0.125,
        },
        "q7.resonator.const.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q8.xy.x180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0008713351703200674, 0.0034627735580602787, 0.007707198270198096, 0.013494680936182852, 0.02067532879499028, 0.029063166838897987, 0.03844095446849734, 0.04856581191010684, 0.05917551067433166, 0.06999526513619665, 0.08074484933849495, 0.09114585469688381, 0.1009289006359776, 0.10984061140475129, 0.11765017837539991, 0.12415533786556042, 0.12918760966144066, 0.13261666056685806, 0.13435367996455982, 0.13435367996455985, 0.13261666056685806, 0.1291876096614407, 0.12415533786556046, 0.11765017837539994, 0.10984061140475129, 0.10092890063597756, 0.09114585469688384, 0.08074484933849498, 0.06999526513619665, 0.05917551067433171, 0.04856581191010688, 0.03844095446849737, 0.029063166838898008, 0.02067532879499029, 0.013494680936182852, 0.007707198270198088, 0.0034627735580602713, 0.0008713351703200674, 0.0],
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
            "samples": [0.0, 0.0004356675851600337, 0.0017313867790301393, 0.003853599135099048, 0.006747340468091426, 0.01033766439749514, 0.014531583419448994, 0.01922047723424867, 0.02428290595505342, 0.02958775533716583, 0.034997632568098326, 0.040372424669247474, 0.045572927348441906, 0.0504644503179888, 0.054920305702375646, 0.05882508918769996, 0.06207766893278021, 0.06459380483072033, 0.06630833028342903, 0.06717683998227991, 0.06717683998227993, 0.06630833028342903, 0.06459380483072034, 0.06207766893278023, 0.05882508918769997, 0.054920305702375646, 0.05046445031798878, 0.04557292734844192, 0.04037242466924749, 0.034997632568098326, 0.029587755337165855, 0.02428290595505344, 0.019220477234248686, 0.014531583419449004, 0.010337664397495144, 0.006747340468091426, 0.003853599135099044, 0.0017313867790301357, 0.0004356675851600337, 0.0],
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
            "samples": [0.0, -0.0004356675851600337, -0.0017313867790301393, -0.003853599135099048, -0.006747340468091426, -0.01033766439749514, -0.014531583419448994, -0.01922047723424867, -0.02428290595505342, -0.02958775533716583, -0.034997632568098326, -0.040372424669247474, -0.045572927348441906, -0.0504644503179888, -0.054920305702375646, -0.05882508918769996, -0.06207766893278021, -0.06459380483072033, -0.06630833028342903, -0.06717683998227991, -0.06717683998227993, -0.06630833028342903, -0.06459380483072034, -0.06207766893278023, -0.05882508918769997, -0.054920305702375646, -0.05046445031798878, -0.04557292734844192, -0.04037242466924749, -0.034997632568098326, -0.029587755337165855, -0.02428290595505344, -0.019220477234248686, -0.014531583419449004, -0.010337664397495144, -0.006747340468091426, -0.003853599135099044, -0.0017313867790301357, -0.0004356675851600337, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q8.xy.-x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 5.335389136584922e-20, 2.1203372770253059e-19, 4.719297845996058e-19, 8.263108907005569e-19, 1.2659987615051976e-18, 1.779605712117096e-18, 2.3538295923007203e-18, 2.9737983051852373e-18, 3.623454986761515e-18, 4.285973870225678e-18, 4.9441960645011556e-18, 5.581073960504425e-18, 6.180112755265562e-18, 6.7257976586608465e-18, 7.203995718327433e-18, 7.602321855705837e-18, 7.91045963306905e-18, 8.120428443840687e-18, 8.226790206113303e-18, 8.226790206113305e-18, 8.120428443840687e-18, 7.910459633069051e-18, 7.60232185570584e-18, 7.203995718327435e-18, 6.7257976586608465e-18, 6.180112755265559e-18, 5.5810739605044276e-18, 4.944196064501158e-18, 4.285973870225678e-18, 3.623454986761518e-18, 2.9737983051852396e-18, 2.3538295923007226e-18, 1.779605712117097e-18, 1.265998761505198e-18, 8.263108907005569e-19, 4.719297845996053e-19, 2.1203372770253013e-19, 5.335389136584922e-20, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q8.xy.y180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 5.335389136584922e-20, 2.1203372770253059e-19, 4.719297845996058e-19, 8.263108907005569e-19, 1.2659987615051976e-18, 1.779605712117096e-18, 2.3538295923007203e-18, 2.9737983051852373e-18, 3.623454986761515e-18, 4.285973870225678e-18, 4.9441960645011556e-18, 5.581073960504425e-18, 6.180112755265562e-18, 6.7257976586608465e-18, 7.203995718327433e-18, 7.602321855705837e-18, 7.91045963306905e-18, 8.120428443840687e-18, 8.226790206113303e-18, 8.226790206113305e-18, 8.120428443840687e-18, 7.910459633069051e-18, 7.60232185570584e-18, 7.203995718327435e-18, 6.7257976586608465e-18, 6.180112755265559e-18, 5.5810739605044276e-18, 4.944196064501158e-18, 4.285973870225678e-18, 3.623454986761518e-18, 2.9737983051852396e-18, 2.3538295923007226e-18, 1.779605712117097e-18, 1.265998761505198e-18, 8.263108907005569e-19, 4.719297845996053e-19, 2.1203372770253013e-19, 5.335389136584922e-20, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q8.xy.y180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0008713351703200674, 0.0034627735580602787, 0.007707198270198096, 0.013494680936182852, 0.02067532879499028, 0.029063166838897987, 0.03844095446849734, 0.04856581191010684, 0.05917551067433166, 0.06999526513619665, 0.08074484933849495, 0.09114585469688381, 0.1009289006359776, 0.10984061140475129, 0.11765017837539991, 0.12415533786556042, 0.12918760966144066, 0.13261666056685806, 0.13435367996455982, 0.13435367996455985, 0.13261666056685806, 0.1291876096614407, 0.12415533786556046, 0.11765017837539994, 0.10984061140475129, 0.10092890063597756, 0.09114585469688384, 0.08074484933849498, 0.06999526513619665, 0.05917551067433171, 0.04856581191010688, 0.03844095446849737, 0.029063166838898008, 0.02067532879499029, 0.013494680936182852, 0.007707198270198088, 0.0034627735580602713, 0.0008713351703200674, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q8.xy.y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 2.667694568292461e-20, 1.0601686385126529e-19, 2.359648922998029e-19, 4.1315544535027846e-19, 6.329993807525988e-19, 8.89802856058548e-19, 1.1769147961503601e-18, 1.4868991525926186e-18, 1.8117274933807573e-18, 2.142986935112839e-18, 2.4720980322505778e-18, 2.7905369802522126e-18, 3.090056377632781e-18, 3.3628988293304232e-18, 3.6019978591637166e-18, 3.801160927852919e-18, 3.955229816534525e-18, 4.060214221920343e-18, 4.113395103056652e-18, 4.1133951030566524e-18, 4.060214221920343e-18, 3.955229816534526e-18, 3.80116092785292e-18, 3.601997859163717e-18, 3.3628988293304232e-18, 3.0900563776327795e-18, 2.7905369802522138e-18, 2.472098032250579e-18, 2.142986935112839e-18, 1.811727493380759e-18, 1.4868991525926198e-18, 1.1769147961503613e-18, 8.898028560585485e-19, 6.32999380752599e-19, 4.1315544535027846e-19, 2.3596489229980265e-19, 1.0601686385126507e-19, 2.667694568292461e-20, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q8.xy.y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0004356675851600337, 0.0017313867790301393, 0.003853599135099048, 0.006747340468091426, 0.01033766439749514, 0.014531583419448994, 0.01922047723424867, 0.02428290595505342, 0.02958775533716583, 0.034997632568098326, 0.040372424669247474, 0.045572927348441906, 0.0504644503179888, 0.054920305702375646, 0.05882508918769996, 0.06207766893278021, 0.06459380483072033, 0.06630833028342903, 0.06717683998227991, 0.06717683998227993, 0.06630833028342903, 0.06459380483072034, 0.06207766893278023, 0.05882508918769997, 0.054920305702375646, 0.05046445031798878, 0.04557292734844192, 0.04037242466924749, 0.034997632568098326, 0.029587755337165855, 0.02428290595505344, 0.019220477234248686, 0.014531583419449004, 0.010337664397495144, 0.006747340468091426, 0.003853599135099044, 0.0017313867790301357, 0.0004356675851600337, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q8.xy.-y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 2.667694568292461e-20, 1.0601686385126529e-19, 2.359648922998029e-19, 4.1315544535027846e-19, 6.329993807525988e-19, 8.89802856058548e-19, 1.1769147961503601e-18, 1.4868991525926186e-18, 1.8117274933807573e-18, 2.142986935112839e-18, 2.4720980322505778e-18, 2.7905369802522126e-18, 3.090056377632781e-18, 3.3628988293304232e-18, 3.6019978591637166e-18, 3.801160927852919e-18, 3.955229816534525e-18, 4.060214221920343e-18, 4.113395103056652e-18, 4.1133951030566524e-18, 4.060214221920343e-18, 3.955229816534526e-18, 3.80116092785292e-18, 3.601997859163717e-18, 3.3628988293304232e-18, 3.0900563776327795e-18, 2.7905369802522138e-18, 2.472098032250579e-18, 2.142986935112839e-18, 1.811727493380759e-18, 1.4868991525926198e-18, 1.1769147961503613e-18, 8.898028560585485e-19, 6.32999380752599e-19, 4.1315544535027846e-19, 2.3596489229980265e-19, 1.0601686385126507e-19, 2.667694568292461e-20, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q8.xy.-y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.0004356675851600337, -0.0017313867790301393, -0.003853599135099048, -0.006747340468091426, -0.01033766439749514, -0.014531583419448994, -0.01922047723424867, -0.02428290595505342, -0.02958775533716583, -0.034997632568098326, -0.040372424669247474, -0.045572927348441906, -0.0504644503179888, -0.054920305702375646, -0.05882508918769996, -0.06207766893278021, -0.06459380483072033, -0.06630833028342903, -0.06717683998227991, -0.06717683998227993, -0.06630833028342903, -0.06459380483072034, -0.06207766893278023, -0.05882508918769997, -0.054920305702375646, -0.05046445031798878, -0.04557292734844192, -0.04037242466924749, -0.034997632568098326, -0.029587755337165855, -0.02428290595505344, -0.019220477234248686, -0.014531583419449004, -0.010337664397495144, -0.006747340468091426, -0.003853599135099044, -0.0017313867790301357, -0.0004356675851600337, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q8.xy.x180_Square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "q8.xy.x180_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q8.xy.x90_Square.wf.I": {
            "type": "constant",
            "sample": 0.05,
        },
        "q8.xy.x90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q8.xy.-x90_Square.wf.I": {
            "type": "constant",
            "sample": -0.125,
        },
        "q8.xy.-x90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q8.xy.y180_Square.wf.I": {
            "type": "constant",
            "sample": -0.11201840403229253,
        },
        "q8.xy.y180_Square.wf.Q": {
            "type": "constant",
            "sample": 0.22349916590013946,
        },
        "q8.xy.y90_Square.wf.I": {
            "type": "constant",
            "sample": -0.056009202016146266,
        },
        "q8.xy.y90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.11174958295006973,
        },
        "q8.xy.-y90_Square.wf.I": {
            "type": "constant",
            "sample": 0.056009202016146266,
        },
        "q8.xy.-y90_Square.wf.Q": {
            "type": "constant",
            "sample": -0.11174958295006973,
        },
        "q8.xy.saturation.wf.I": {
            "type": "constant",
            "sample": 0.043017810278935274,
        },
        "q8.xy.saturation.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q8.xy.cr_q7_q8_Square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "q8.xy.cr_q7_q8_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q8.xy_detuned.zz_q7_q8_Square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "q8.xy_detuned.zz_q7_q8_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q8.resonator.readout.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "q8.resonator.readout.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q8.resonator.const.wf.I": {
            "type": "constant",
            "sample": 0.125,
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
        "zz_q1_q2.square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "zz_q1_q2.square.wf.Q": {
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
        "zz_q2_q3.square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "zz_q2_q3.square.wf.Q": {
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
        "zz_q3_q4.square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "zz_q3_q4.square.wf.Q": {
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
        "zz_q4_q5.square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "zz_q4_q5.square.wf.Q": {
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
        "zz_q5_q6.square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "zz_q5_q6.square.wf.Q": {
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
        "zz_q6_q7.square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "zz_q6_q7.square.wf.Q": {
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
        "zz_q7_q8.square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "zz_q7_q8.square.wf.Q": {
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
        "zz_q8_q1.square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "zz_q8_q1.square.wf.Q": {
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
            "cosine": [(-0.9425588238789202, 2000)],
            "sine": [(0.33404021244153614, 2000)],
        },
        "q1.resonator.readout.iw2": {
            "cosine": [(-0.33404021244153614, 2000)],
            "sine": [(-0.9425588238789202, 2000)],
        },
        "q1.resonator.readout.iw3": {
            "cosine": [(0.33404021244153614, 2000)],
            "sine": [(0.9425588238789202, 2000)],
        },
        "q2.resonator.readout.iw1": {
            "cosine": [(-0.9572310893844667, 2000)],
            "sine": [(0.2893244571684653, 2000)],
        },
        "q2.resonator.readout.iw2": {
            "cosine": [(-0.2893244571684653, 2000)],
            "sine": [(-0.9572310893844667, 2000)],
        },
        "q2.resonator.readout.iw3": {
            "cosine": [(0.2893244571684653, 2000)],
            "sine": [(0.9572310893844667, 2000)],
        },
        "q3.resonator.readout.iw1": {
            "cosine": [(0.1345356924135238, 2000)],
            "sine": [(-0.9909087483047133, 2000)],
        },
        "q3.resonator.readout.iw2": {
            "cosine": [(0.9909087483047133, 2000)],
            "sine": [(0.1345356924135238, 2000)],
        },
        "q3.resonator.readout.iw3": {
            "cosine": [(-0.9909087483047133, 2000)],
            "sine": [(-0.1345356924135238, 2000)],
        },
        "q4.resonator.readout.iw1": {
            "cosine": [(-0.8679447933694215, 2000)],
            "sine": [(0.49666068463581065, 2000)],
        },
        "q4.resonator.readout.iw2": {
            "cosine": [(-0.49666068463581065, 2000)],
            "sine": [(-0.8679447933694215, 2000)],
        },
        "q4.resonator.readout.iw3": {
            "cosine": [(0.49666068463581065, 2000)],
            "sine": [(0.8679447933694215, 2000)],
        },
        "q5.resonator.readout.iw1": {
            "cosine": [(-0.7898172096237304, 2000)],
            "sine": [(-0.6133422987061827, 2000)],
        },
        "q5.resonator.readout.iw2": {
            "cosine": [(0.6133422987061827, 2000)],
            "sine": [(-0.7898172096237304, 2000)],
        },
        "q5.resonator.readout.iw3": {
            "cosine": [(-0.6133422987061827, 2000)],
            "sine": [(0.7898172096237304, 2000)],
        },
        "q6.resonator.readout.iw1": {
            "cosine": [(-0.9042233768894555, 2000)],
            "sine": [(0.4270598139448731, 2000)],
        },
        "q6.resonator.readout.iw2": {
            "cosine": [(-0.4270598139448731, 2000)],
            "sine": [(-0.9042233768894555, 2000)],
        },
        "q6.resonator.readout.iw3": {
            "cosine": [(0.4270598139448731, 2000)],
            "sine": [(0.9042233768894555, 2000)],
        },
        "q7.resonator.readout.iw1": {
            "cosine": [(-0.8759906098241979, 2000)],
            "sine": [(0.4823281574818433, 2000)],
        },
        "q7.resonator.readout.iw2": {
            "cosine": [(-0.4823281574818433, 2000)],
            "sine": [(-0.8759906098241979, 2000)],
        },
        "q7.resonator.readout.iw3": {
            "cosine": [(0.4823281574818433, 2000)],
            "sine": [(0.8759906098241979, 2000)],
        },
        "q8.resonator.readout.iw1": {
            "cosine": [(0.7989098841294603, 2000)],
            "sine": [(0.601450743652589, 2000)],
        },
        "q8.resonator.readout.iw2": {
            "cosine": [(-0.601450743652589, 2000)],
            "sine": [(0.7989098841294603, 2000)],
        },
        "q8.resonator.readout.iw3": {
            "cosine": [(0.601450743652589, 2000)],
            "sine": [(-0.7989098841294603, 2000)],
        },
    },
    "mixers": {},
}


