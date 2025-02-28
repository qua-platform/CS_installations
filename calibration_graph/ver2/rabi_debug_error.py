
# Single QUA script generated at 2024-12-04 18:36:00.948971
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
    v18 = declare(fixed, )
    v19 = declare(int, )
    v20 = declare(int, )
    with for_(v1,0,(v1<50),(v1+1)):
        r1 = declare_stream()
        save(v1, r1)
        with for_(v19,1,(v19<=1),(v19+1)):
            with for_(v18,0.001,(v18<1.9885),(v18+0.005)):
                wait(28750, "q1.xy", "q1.resonator")
                align("q1.xy", "q1.resonator")
                with for_(v20,0,(v20<v19),(v20+1)):
                    play("x180"*amp(v18), "q1.xy")
                align("q1.xy", "q1.resonator")
                measure("readout", "q1.resonator", None, dual_demod.full("iw1", "iw2", v2), dual_demod.full("iw3", "iw1", v10))
                r2 = declare_stream()
                save(v2, r2)
                r10 = declare_stream()
                save(v10, r10)
                align()
    align()
    with for_(v1,0,(v1<50),(v1+1)):
        save(v1, r1)
        with for_(v19,1,(v19<=1),(v19+1)):
            with for_(v18,0.001,(v18<1.9885),(v18+0.005)):
                wait(51250, "q2.xy", "q2.resonator")
                align("q2.xy", "q2.resonator")
                with for_(v20,0,(v20<v19),(v20+1)):
                    play("x180"*amp(v18), "q2.xy")
                align("q2.xy", "q2.resonator")
                measure("readout", "q2.resonator", None, dual_demod.full("iw1", "iw2", v3), dual_demod.full("iw3", "iw1", v11))
                r3 = declare_stream()
                save(v3, r3)
                r11 = declare_stream()
                save(v11, r11)
                align()
    align()
    with for_(v1,0,(v1<50),(v1+1)):
        save(v1, r1)
        with for_(v19,1,(v19<=1),(v19+1)):
            with for_(v18,0.001,(v18<1.9885),(v18+0.005)):
                wait(61250, "q3.xy", "q3.resonator")
                align("q3.xy", "q3.resonator")
                with for_(v20,0,(v20<v19),(v20+1)):
                    play("x180"*amp(v18), "q3.xy")
                align("q3.xy", "q3.resonator")
                measure("readout", "q3.resonator", None, dual_demod.full("iw1", "iw2", v4), dual_demod.full("iw3", "iw1", v12))
                r4 = declare_stream()
                save(v4, r4)
                r12 = declare_stream()
                save(v12, r12)
                align()
    align()
    with for_(v1,0,(v1<50),(v1+1)):
        save(v1, r1)
        with for_(v19,1,(v19<=1),(v19+1)):
            with for_(v18,0.001,(v18<1.9885),(v18+0.005)):
                wait(41249, "q4.xy", "q4.resonator")
                align("q4.xy", "q4.resonator")
                with for_(v20,0,(v20<v19),(v20+1)):
                    play("x180"*amp(v18), "q4.xy")
                align("q4.xy", "q4.resonator")
                measure("readout", "q4.resonator", None, dual_demod.full("iw1", "iw2", v5), dual_demod.full("iw3", "iw1", v13))
                r5 = declare_stream()
                save(v5, r5)
                r13 = declare_stream()
                save(v13, r13)
                align()
    align()
    with for_(v1,0,(v1<50),(v1+1)):
        save(v1, r1)
        with for_(v19,1,(v19<=1),(v19+1)):
            with for_(v18,0.001,(v18<1.9885),(v18+0.005)):
                wait(61250, "q5.xy", "q5.resonator")
                align("q5.xy", "q5.resonator")
                with for_(v20,0,(v20<v19),(v20+1)):
                    play("x180"*amp(v18), "q5.xy")
                align("q5.xy", "q5.resonator")
                measure("readout", "q5.resonator", None, dual_demod.full("iw1", "iw2", v6), dual_demod.full("iw3", "iw1", v14))
                r6 = declare_stream()
                save(v6, r6)
                r14 = declare_stream()
                save(v14, r14)
                align()
    align()
    with for_(v1,0,(v1<50),(v1+1)):
        save(v1, r1)
        with for_(v19,1,(v19<=1),(v19+1)):
            with for_(v18,0.001,(v18<1.9885),(v18+0.005)):
                wait(17500, "q6.xy", "q6.resonator")
                align("q6.xy", "q6.resonator")
                with for_(v20,0,(v20<v19),(v20+1)):
                    play("x180"*amp(v18), "q6.xy")
                align("q6.xy", "q6.resonator")
                measure("readout", "q6.resonator", None, dual_demod.full("iw1", "iw2", v7), dual_demod.full("iw3", "iw1", v15))
                r7 = declare_stream()
                save(v7, r7)
                r15 = declare_stream()
                save(v15, r15)
                align()
    align()
    with for_(v1,0,(v1<50),(v1+1)):
        save(v1, r1)
        with for_(v19,1,(v19<=1),(v19+1)):
            with for_(v18,0.001,(v18<1.9885),(v18+0.005)):
                wait(23749, "q7.xy", "q7.resonator")
                align("q7.xy", "q7.resonator")
                with for_(v20,0,(v20<v19),(v20+1)):
                    play("x180"*amp(v18), "q7.xy")
                align("q7.xy", "q7.resonator")
                measure("readout", "q7.resonator", None, dual_demod.full("iw1", "iw2", v8), dual_demod.full("iw3", "iw1", v16))
                r8 = declare_stream()
                save(v8, r8)
                r16 = declare_stream()
                save(v16, r16)
                align()
    align()
    with for_(v1,0,(v1<50),(v1+1)):
        save(v1, r1)
        with for_(v19,1,(v19<=1),(v19+1)):
            with for_(v18,0.001,(v18<1.9885),(v18+0.005)):
                wait(42500, "q8.xy", "q8.resonator")
                align("q8.xy", "q8.resonator")
                with for_(v20,0,(v20<v19),(v20+1)):
                    play("x180"*amp(v18), "q8.xy")
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
        r2.buffer(398).buffer(1).average().save("I1")
        r10.buffer(398).buffer(1).average().save("Q1")
        r3.buffer(398).buffer(1).average().save("I2")
        r11.buffer(398).buffer(1).average().save("Q2")
        r4.buffer(398).buffer(1).average().save("I3")
        r12.buffer(398).buffer(1).average().save("Q3")
        r5.buffer(398).buffer(1).average().save("I4")
        r13.buffer(398).buffer(1).average().save("Q4")
        r6.buffer(398).buffer(1).average().save("I5")
        r14.buffer(398).buffer(1).average().save("Q5")
        r7.buffer(398).buffer(1).average().save("I6")
        r15.buffer(398).buffer(1).average().save("Q6")
        r8.buffer(398).buffer(1).average().save("I7")
        r16.buffer(398).buffer(1).average().save("Q7")
        r9.buffer(398).buffer(1).average().save("I8")
        r17.buffer(398).buffer(1).average().save("Q8")


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
            "samples": [0.0, 0.0009556910616820674, 0.0037980123502321136, 0.008453349237279348, 0.014801130942785182, 0.022676953254913295, 0.03187683651275862, 0.04216250857241926, 0.05326757593036487, 0.06490442317524811, 0.07677166207598103, 0.08856193737860832, 0.09996988714593863, 0.11070005147131827, 0.12047452473501581, 0.12904015321379603, 0.13617509162937613, 0.14169454882460322, 0.14545557375735835] + [0.1473607578574586] * 2 + [0.14545557375735835, 0.14169454882460325, 0.13617509162937616, 0.12904015321379608, 0.12047452473501581, 0.11070005147131823, 0.09996988714593866, 0.08856193737860835, 0.07677166207598103, 0.06490442317524817, 0.05326757593036492, 0.042162508572419294, 0.03187683651275864, 0.022676953254913302, 0.014801130942785182, 0.00845334923727934, 0.0037980123502321054, 0.0009556910616820674, 0.0],
        },
        "q1.xy.x180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
        },
        "q1.xy.x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0004778455308410337, 0.0018990061751160568, 0.004226674618639674, 0.007400565471392591, 0.011338476627456648, 0.01593841825637931, 0.02108125428620963, 0.026633787965182436, 0.032452211587624055, 0.038385831037990516, 0.04428096868930416, 0.049984943572969315, 0.055350025735659135, 0.060237262367507906, 0.06452007660689801, 0.06808754581468807, 0.07084727441230161, 0.07272778687867917] + [0.0736803789287293] * 2 + [0.07272778687867917, 0.07084727441230163, 0.06808754581468808, 0.06452007660689804, 0.060237262367507906, 0.055350025735659114, 0.04998494357296933, 0.04428096868930417, 0.038385831037990516, 0.03245221158762408, 0.02663378796518246, 0.021081254286209647, 0.01593841825637932, 0.011338476627456651, 0.007400565471392591, 0.00422667461863967, 0.0018990061751160527, 0.0004778455308410337, 0.0],
        },
        "q1.xy.x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
        },
        "q1.xy.-x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -0.0004778455308410337, -0.0018990061751160568, -0.004226674618639674, -0.007400565471392591, -0.011338476627456648, -0.01593841825637931, -0.02108125428620963, -0.026633787965182436, -0.032452211587624055, -0.038385831037990516, -0.04428096868930416, -0.049984943572969315, -0.055350025735659135, -0.060237262367507906, -0.06452007660689801, -0.06808754581468807, -0.07084727441230161, -0.07272778687867917] + [-0.0736803789287293] * 2 + [-0.07272778687867917, -0.07084727441230163, -0.06808754581468808, -0.06452007660689804, -0.060237262367507906, -0.055350025735659114, -0.04998494357296933, -0.04428096868930417, -0.038385831037990516, -0.03245221158762408, -0.02663378796518246, -0.021081254286209647, -0.01593841825637932, -0.011338476627456651, -0.007400565471392591, -0.00422667461863967, -0.0018990061751160527, -0.0004778455308410337, 0.0],
        },
        "q1.xy.-x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 5.851919998313397e-20, 2.325611833916937e-19, 5.176183542754436e-19, 9.06307881642136e-19, 1.388562910902186e-18, 1.951893290114666e-18, 2.5817090583618042e-18, 3.2616983180729967e-18, 3.974249704603644e-18, 4.700908511328621e-18, 5.422854656850051e-18, 6.1213901152197934e-18, 6.778423184989859e-18, 7.376937054776786e-18, 7.901430529737967e-18, 8.33831950437565e-18, 8.676288783733935e-18, 8.906585141004532e-18] + [9.023244021503244e-18] * 2 + [8.906585141004532e-18, 8.676288783733937e-18, 8.338319504375653e-18, 7.901430529737971e-18, 7.376937054776786e-18, 6.7784231849898556e-18, 6.121390115219795e-18, 5.4228546568500524e-18, 4.700908511328621e-18, 3.974249704603648e-18, 3.261698318073e-18, 2.5817090583618065e-18, 1.9518932901146673e-18, 1.3885629109021864e-18, 9.06307881642136e-19, 5.176183542754431e-19, 2.325611833916932e-19, 5.851919998313397e-20, 0.0],
        },
        "q1.xy.y180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 5.851919998313397e-20, 2.325611833916937e-19, 5.176183542754436e-19, 9.06307881642136e-19, 1.388562910902186e-18, 1.951893290114666e-18, 2.5817090583618042e-18, 3.2616983180729967e-18, 3.974249704603644e-18, 4.700908511328621e-18, 5.422854656850051e-18, 6.1213901152197934e-18, 6.778423184989859e-18, 7.376937054776786e-18, 7.901430529737967e-18, 8.33831950437565e-18, 8.676288783733935e-18, 8.906585141004532e-18] + [9.023244021503244e-18] * 2 + [8.906585141004532e-18, 8.676288783733937e-18, 8.338319504375653e-18, 7.901430529737971e-18, 7.376937054776786e-18, 6.7784231849898556e-18, 6.121390115219795e-18, 5.4228546568500524e-18, 4.700908511328621e-18, 3.974249704603648e-18, 3.261698318073e-18, 2.5817090583618065e-18, 1.9518932901146673e-18, 1.3885629109021864e-18, 9.06307881642136e-19, 5.176183542754431e-19, 2.325611833916932e-19, 5.851919998313397e-20, 0.0],
        },
        "q1.xy.y180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0009556910616820674, 0.0037980123502321136, 0.008453349237279348, 0.014801130942785182, 0.022676953254913295, 0.03187683651275862, 0.04216250857241926, 0.05326757593036487, 0.06490442317524811, 0.07677166207598103, 0.08856193737860832, 0.09996988714593863, 0.11070005147131827, 0.12047452473501581, 0.12904015321379603, 0.13617509162937613, 0.14169454882460322, 0.14545557375735835] + [0.1473607578574586] * 2 + [0.14545557375735835, 0.14169454882460325, 0.13617509162937616, 0.12904015321379608, 0.12047452473501581, 0.11070005147131823, 0.09996988714593866, 0.08856193737860835, 0.07677166207598103, 0.06490442317524817, 0.05326757593036492, 0.042162508572419294, 0.03187683651275864, 0.022676953254913302, 0.014801130942785182, 0.00845334923727934, 0.0037980123502321054, 0.0009556910616820674, 0.0],
        },
        "q1.xy.y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 2.925959999156699e-20, 1.1628059169584686e-19, 2.588091771377218e-19, 4.53153940821068e-19, 6.94281455451093e-19, 9.75946645057333e-19, 1.2908545291809021e-18, 1.6308491590364984e-18, 1.987124852301822e-18, 2.3504542556643105e-18, 2.7114273284250255e-18, 3.0606950576098967e-18, 3.3892115924949293e-18, 3.688468527388393e-18, 3.9507152648689834e-18, 4.169159752187825e-18, 4.3381443918669676e-18, 4.453292570502266e-18] + [4.511622010751622e-18] * 2 + [4.453292570502266e-18, 4.338144391866968e-18, 4.1691597521878265e-18, 3.950715264868986e-18, 3.688468527388393e-18, 3.3892115924949278e-18, 3.0606950576098975e-18, 2.7114273284250262e-18, 2.3504542556643105e-18, 1.987124852301824e-18, 1.6308491590365e-18, 1.2908545291809033e-18, 9.759466450573337e-19, 6.942814554510932e-19, 4.53153940821068e-19, 2.5880917713772153e-19, 1.162805916958466e-19, 2.925959999156699e-20, 0.0],
        },
        "q1.xy.y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0004778455308410337, 0.0018990061751160568, 0.004226674618639674, 0.007400565471392591, 0.011338476627456648, 0.01593841825637931, 0.02108125428620963, 0.026633787965182436, 0.032452211587624055, 0.038385831037990516, 0.04428096868930416, 0.049984943572969315, 0.055350025735659135, 0.060237262367507906, 0.06452007660689801, 0.06808754581468807, 0.07084727441230161, 0.07272778687867917] + [0.0736803789287293] * 2 + [0.07272778687867917, 0.07084727441230163, 0.06808754581468808, 0.06452007660689804, 0.060237262367507906, 0.055350025735659114, 0.04998494357296933, 0.04428096868930417, 0.038385831037990516, 0.03245221158762408, 0.02663378796518246, 0.021081254286209647, 0.01593841825637932, 0.011338476627456651, 0.007400565471392591, 0.00422667461863967, 0.0018990061751160527, 0.0004778455308410337, 0.0],
        },
        "q1.xy.-y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 2.925959999156699e-20, 1.1628059169584686e-19, 2.588091771377218e-19, 4.53153940821068e-19, 6.94281455451093e-19, 9.75946645057333e-19, 1.2908545291809021e-18, 1.6308491590364984e-18, 1.987124852301822e-18, 2.3504542556643105e-18, 2.7114273284250255e-18, 3.0606950576098967e-18, 3.3892115924949293e-18, 3.688468527388393e-18, 3.9507152648689834e-18, 4.169159752187825e-18, 4.3381443918669676e-18, 4.453292570502266e-18] + [4.511622010751622e-18] * 2 + [4.453292570502266e-18, 4.338144391866968e-18, 4.1691597521878265e-18, 3.950715264868986e-18, 3.688468527388393e-18, 3.3892115924949278e-18, 3.0606950576098975e-18, 2.7114273284250262e-18, 2.3504542556643105e-18, 1.987124852301824e-18, 1.6308491590365e-18, 1.2908545291809033e-18, 9.759466450573337e-19, 6.942814554510932e-19, 4.53153940821068e-19, 2.5880917713772153e-19, 1.162805916958466e-19, 2.925959999156699e-20, 0.0],
        },
        "q1.xy.-y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.0004778455308410337, -0.0018990061751160568, -0.004226674618639674, -0.007400565471392591, -0.011338476627456648, -0.01593841825637931, -0.02108125428620963, -0.026633787965182436, -0.032452211587624055, -0.038385831037990516, -0.04428096868930416, -0.049984943572969315, -0.055350025735659135, -0.060237262367507906, -0.06452007660689801, -0.06808754581468807, -0.07084727441230161, -0.07272778687867917] + [-0.0736803789287293] * 2 + [-0.07272778687867917, -0.07084727441230163, -0.06808754581468808, -0.06452007660689804, -0.060237262367507906, -0.055350025735659114, -0.04998494357296933, -0.04428096868930417, -0.038385831037990516, -0.03245221158762408, -0.02663378796518246, -0.021081254286209647, -0.01593841825637932, -0.011338476627456651, -0.007400565471392591, -0.00422667461863967, -0.0018990061751160527, -0.0004778455308410337, 0.0],
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
            "samples": [0.0, 0.0007493652082608129, 0.0029780526677727235, 0.006628340544010013, 0.011605688298386123, 0.017781185238543162, 0.024994889237570306, 0.0330599691510771, 0.0417675436456952, 0.050892091115892414, 0.06019729057509481, 0.06944214224510536, 0.07838720932376797, 0.0868008192723727, 0.09446506401271659, 0.10118144363186725, 0.10677600742564054, 0.11110385913046684, 0.114052909660507, 0.11554678015609796, 0.11554678015609797, 0.114052909660507, 0.11110385913046686, 0.10677600742564057, 0.10118144363186728, 0.09446506401271659, 0.08680081927237267, 0.078387209323768, 0.06944214224510539, 0.06019729057509481, 0.050892091115892456, 0.041767543645695245, 0.033059969151077125, 0.024994889237570324, 0.01778118523854317, 0.011605688298386123, 0.006628340544010007, 0.002978052667772717, 0.0007493652082608129, 0.0],
        },
        "q2.xy.x180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
        },
        "q2.xy.x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.00037468260413040644, 0.0014890263338863618, 0.0033141702720050066, 0.005802844149193061, 0.008890592619271581, 0.012497444618785153, 0.01652998457553855, 0.0208837718228476, 0.025446045557946207, 0.030098645287547406, 0.03472107112255268, 0.039193604661883985, 0.04340040963618635, 0.047232532006358297, 0.050590721815933624, 0.05338800371282027, 0.05555192956523342, 0.0570264548302535, 0.05777339007804898, 0.057773390078048985, 0.0570264548302535, 0.05555192956523343, 0.053388003712820285, 0.05059072181593364, 0.047232532006358297, 0.043400409636186334, 0.039193604661884, 0.034721071122552696, 0.030098645287547406, 0.025446045557946228, 0.020883771822847622, 0.016529984575538562, 0.012497444618785162, 0.008890592619271585, 0.005802844149193061, 0.0033141702720050036, 0.0014890263338863585, 0.00037468260413040644, 0.0],
        },
        "q2.xy.x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
        },
        "q2.xy.-x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -0.00037468260413040644, -0.0014890263338863618, -0.0033141702720050066, -0.005802844149193061, -0.008890592619271581, -0.012497444618785153, -0.01652998457553855, -0.0208837718228476, -0.025446045557946207, -0.030098645287547406, -0.03472107112255268, -0.039193604661883985, -0.04340040963618635, -0.047232532006358297, -0.050590721815933624, -0.05338800371282027, -0.05555192956523342, -0.0570264548302535, -0.05777339007804898, -0.057773390078048985, -0.0570264548302535, -0.05555192956523343, -0.053388003712820285, -0.05059072181593364, -0.047232532006358297, -0.043400409636186334, -0.039193604661884, -0.034721071122552696, -0.030098645287547406, -0.025446045557946228, -0.020883771822847622, -0.016529984575538562, -0.012497444618785162, -0.008890592619271585, -0.005802844149193061, -0.0033141702720050036, -0.0014890263338863585, -0.00037468260413040644, 0.0],
        },
        "q2.xy.-x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 4.588538518444971e-20, 1.823531333640051e-19, 4.0586880154402444e-19, 7.106434513260228e-19, 1.0887835793714024e-18, 1.5304955549916552e-18, 2.02433927003884e-18, 2.5575244316974e-18, 3.1162418243496547e-18, 3.6860209610066494e-18, 4.252104861320174e-18, 4.7998322496223e-18, 5.315017274263956e-18, 5.78431691372116e-18, 6.195576553843728e-18, 6.538144785977236e-18, 6.8031492728522326e-18, 6.983726537459107e-18] + [7.075199723497414e-18] * 2 + [6.983726537459107e-18, 6.803149272852233e-18, 6.538144785977237e-18, 6.19557655384373e-18, 5.78431691372116e-18, 5.3150172742639535e-18, 4.799832249622302e-18, 4.2521048613201755e-18, 3.6860209610066494e-18, 3.1162418243496574e-18, 2.5575244316974026e-18, 2.024339270038842e-18, 1.5304955549916562e-18, 1.088783579371403e-18, 7.106434513260228e-19, 4.0586880154402406e-19, 1.8235313336400469e-19, 4.588538518444971e-20, 0.0],
        },
        "q2.xy.y180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 4.588538518444971e-20, 1.823531333640051e-19, 4.0586880154402444e-19, 7.106434513260228e-19, 1.0887835793714024e-18, 1.5304955549916552e-18, 2.02433927003884e-18, 2.5575244316974e-18, 3.1162418243496547e-18, 3.6860209610066494e-18, 4.252104861320174e-18, 4.7998322496223e-18, 5.315017274263956e-18, 5.78431691372116e-18, 6.195576553843728e-18, 6.538144785977236e-18, 6.8031492728522326e-18, 6.983726537459107e-18] + [7.075199723497414e-18] * 2 + [6.983726537459107e-18, 6.803149272852233e-18, 6.538144785977237e-18, 6.19557655384373e-18, 5.78431691372116e-18, 5.3150172742639535e-18, 4.799832249622302e-18, 4.2521048613201755e-18, 3.6860209610066494e-18, 3.1162418243496574e-18, 2.5575244316974026e-18, 2.024339270038842e-18, 1.5304955549916562e-18, 1.088783579371403e-18, 7.106434513260228e-19, 4.0586880154402406e-19, 1.8235313336400469e-19, 4.588538518444971e-20, 0.0],
        },
        "q2.xy.y180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0007493652082608129, 0.0029780526677727235, 0.006628340544010013, 0.011605688298386123, 0.017781185238543162, 0.024994889237570306, 0.0330599691510771, 0.0417675436456952, 0.050892091115892414, 0.06019729057509481, 0.06944214224510536, 0.07838720932376797, 0.0868008192723727, 0.09446506401271659, 0.10118144363186725, 0.10677600742564054, 0.11110385913046684, 0.114052909660507, 0.11554678015609796, 0.11554678015609797, 0.114052909660507, 0.11110385913046686, 0.10677600742564057, 0.10118144363186728, 0.09446506401271659, 0.08680081927237267, 0.078387209323768, 0.06944214224510539, 0.06019729057509481, 0.050892091115892456, 0.041767543645695245, 0.033059969151077125, 0.024994889237570324, 0.01778118523854317, 0.011605688298386123, 0.006628340544010007, 0.002978052667772717, 0.0007493652082608129, 0.0],
        },
        "q2.xy.y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 2.2942692592224855e-20, 9.117656668200255e-20, 2.0293440077201222e-19, 3.553217256630114e-19, 5.443917896857012e-19, 7.652477774958276e-19, 1.01216963501942e-18, 1.2787622158487e-18, 1.5581209121748273e-18, 1.8430104805033247e-18, 2.126052430660087e-18, 2.39991612481115e-18, 2.657508637131978e-18, 2.89215845686058e-18, 3.097788276921864e-18, 3.269072392988618e-18, 3.4015746364261163e-18, 3.491863268729554e-18] + [3.537599861748707e-18] * 2 + [3.491863268729554e-18, 3.4015746364261167e-18, 3.2690723929886186e-18, 3.097788276921865e-18, 2.89215845686058e-18, 2.6575086371319767e-18, 2.399916124811151e-18, 2.1260524306600877e-18, 1.8430104805033247e-18, 1.5581209121748287e-18, 1.2787622158487013e-18, 1.012169635019421e-18, 7.652477774958281e-19, 5.443917896857015e-19, 3.553217256630114e-19, 2.0293440077201203e-19, 9.117656668200234e-20, 2.2942692592224855e-20, 0.0],
        },
        "q2.xy.y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.00037468260413040644, 0.0014890263338863618, 0.0033141702720050066, 0.005802844149193061, 0.008890592619271581, 0.012497444618785153, 0.01652998457553855, 0.0208837718228476, 0.025446045557946207, 0.030098645287547406, 0.03472107112255268, 0.039193604661883985, 0.04340040963618635, 0.047232532006358297, 0.050590721815933624, 0.05338800371282027, 0.05555192956523342, 0.0570264548302535, 0.05777339007804898, 0.057773390078048985, 0.0570264548302535, 0.05555192956523343, 0.053388003712820285, 0.05059072181593364, 0.047232532006358297, 0.043400409636186334, 0.039193604661884, 0.034721071122552696, 0.030098645287547406, 0.025446045557946228, 0.020883771822847622, 0.016529984575538562, 0.012497444618785162, 0.008890592619271585, 0.005802844149193061, 0.0033141702720050036, 0.0014890263338863585, 0.00037468260413040644, 0.0],
        },
        "q2.xy.-y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 2.2942692592224855e-20, 9.117656668200255e-20, 2.0293440077201222e-19, 3.553217256630114e-19, 5.443917896857012e-19, 7.652477774958276e-19, 1.01216963501942e-18, 1.2787622158487e-18, 1.5581209121748273e-18, 1.8430104805033247e-18, 2.126052430660087e-18, 2.39991612481115e-18, 2.657508637131978e-18, 2.89215845686058e-18, 3.097788276921864e-18, 3.269072392988618e-18, 3.4015746364261163e-18, 3.491863268729554e-18] + [3.537599861748707e-18] * 2 + [3.491863268729554e-18, 3.4015746364261167e-18, 3.2690723929886186e-18, 3.097788276921865e-18, 2.89215845686058e-18, 2.6575086371319767e-18, 2.399916124811151e-18, 2.1260524306600877e-18, 1.8430104805033247e-18, 1.5581209121748287e-18, 1.2787622158487013e-18, 1.012169635019421e-18, 7.652477774958281e-19, 5.443917896857015e-19, 3.553217256630114e-19, 2.0293440077201203e-19, 9.117656668200234e-20, 2.2942692592224855e-20, 0.0],
        },
        "q2.xy.-y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.00037468260413040644, -0.0014890263338863618, -0.0033141702720050066, -0.005802844149193061, -0.008890592619271581, -0.012497444618785153, -0.01652998457553855, -0.0208837718228476, -0.025446045557946207, -0.030098645287547406, -0.03472107112255268, -0.039193604661883985, -0.04340040963618635, -0.047232532006358297, -0.050590721815933624, -0.05338800371282027, -0.05555192956523342, -0.0570264548302535, -0.05777339007804898, -0.057773390078048985, -0.0570264548302535, -0.05555192956523343, -0.053388003712820285, -0.05059072181593364, -0.047232532006358297, -0.043400409636186334, -0.039193604661884, -0.034721071122552696, -0.030098645287547406, -0.025446045557946228, -0.020883771822847622, -0.016529984575538562, -0.012497444618785162, -0.008890592619271585, -0.005802844149193061, -0.0033141702720050036, -0.0014890263338863585, -0.00037468260413040644, 0.0],
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
            "samples": [0.0, 0.001080628881442259, 0.004294527805367907, 0.009558458477830673, 0.016736087859429313, 0.025641519119415625, 0.036044106265963695, 0.04767442775620553, 0.06023126437267054, 0.07338940064279505, 0.08680804774883369, 0.10013966977923097, 0.11303898472617849, 0.12517190710824852, 0.13622420060887627, 0.1459096166318981, 0.15397730798983267, 0.16021832571427266, 0.16447103072441085, 0.16662528019432776, 0.1666252801943278, 0.16447103072441085, 0.1602183257142727, 0.1539773079898327, 0.14590961663189814, 0.13622420060887627, 0.12517190710824846, 0.11303898472617853, 0.10013966977923101, 0.08680804774883369, 0.0733894006427951, 0.060231264372670595, 0.04767442775620556, 0.03604410626596372, 0.02564151911941563, 0.016736087859429313, 0.009558458477830665, 0.004294527805367898, 0.001080628881442259, 0.0],
        },
        "q3.xy.x180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
        },
        "q3.xy.x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0005403144407211295, 0.0021472639026839536, 0.004779229238915337, 0.008368043929714656, 0.012820759559707812, 0.018022053132981847, 0.023837213878102764, 0.03011563218633527, 0.03669470032139752, 0.043404023874416844, 0.050069834889615486, 0.056519492363089244, 0.06258595355412426, 0.06811210030443814, 0.07295480831594905, 0.07698865399491633, 0.08010916285713633, 0.08223551536220543, 0.08331264009716388, 0.0833126400971639, 0.08223551536220543, 0.08010916285713635, 0.07698865399491635, 0.07295480831594907, 0.06811210030443814, 0.06258595355412423, 0.056519492363089265, 0.05006983488961551, 0.043404023874416844, 0.03669470032139755, 0.030115632186335298, 0.02383721387810278, 0.01802205313298186, 0.012820759559707816, 0.008368043929714656, 0.004779229238915332, 0.002147263902683949, 0.0005403144407211295, 0.0],
        },
        "q3.xy.x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
        },
        "q3.xy.-x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -0.0005403144407211295, -0.0021472639026839536, -0.004779229238915337, -0.008368043929714656, -0.012820759559707812, -0.018022053132981847, -0.023837213878102764, -0.03011563218633527, -0.03669470032139752, -0.043404023874416844, -0.050069834889615486, -0.056519492363089244, -0.06258595355412426, -0.06811210030443814, -0.07295480831594905, -0.07698865399491633, -0.08010916285713633, -0.08223551536220543, -0.08331264009716388, -0.0833126400971639, -0.08223551536220543, -0.08010916285713635, -0.07698865399491635, -0.07295480831594907, -0.06811210030443814, -0.06258595355412423, -0.056519492363089265, -0.05006983488961551, -0.043404023874416844, -0.03669470032139755, -0.030115632186335298, -0.02383721387810278, -0.01802205313298186, -0.012820759559707816, -0.008368043929714656, -0.004779229238915332, -0.002147263902683949, -0.0005403144407211295, 0.0],
        },
        "q3.xy.-x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 6.616943503622235e-20, 2.6296398653465575e-19, 5.852867789829108e-19, 1.0247898213649492e-18, 1.5700902157434003e-18, 2.207064968336975e-18, 2.9192167676409414e-18, 3.6881012561294494e-18, 4.493804729427083e-18, 5.3154598907919885e-18, 6.131786303140407e-18, 6.921641541189052e-18, 7.664568769164318e-18, 8.341326562103362e-18, 8.934387248653571e-18, 9.428390868553737e-18, 9.810542987536604e-18, 1.0070946066455787e-17, 1.0202855802350718e-17, 1.020285580235072e-17, 1.0070946066455787e-17, 9.810542987536606e-18, 9.428390868553739e-18, 8.934387248653573e-18, 8.341326562103362e-18, 7.664568769164315e-18, 6.921641541189054e-18, 6.13178630314041e-18, 5.3154598907919885e-18, 4.4938047294270864e-18, 3.6881012561294525e-18, 2.9192167676409437e-18, 2.2070649683369765e-18, 1.5700902157434007e-18, 1.0247898213649492e-18, 5.852867789829103e-19, 2.6296398653465517e-19, 6.616943503622235e-20, 0.0],
        },
        "q3.xy.y180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 6.616943503622235e-20, 2.6296398653465575e-19, 5.852867789829108e-19, 1.0247898213649492e-18, 1.5700902157434003e-18, 2.207064968336975e-18, 2.9192167676409414e-18, 3.6881012561294494e-18, 4.493804729427083e-18, 5.3154598907919885e-18, 6.131786303140407e-18, 6.921641541189052e-18, 7.664568769164318e-18, 8.341326562103362e-18, 8.934387248653571e-18, 9.428390868553737e-18, 9.810542987536604e-18, 1.0070946066455787e-17, 1.0202855802350718e-17, 1.020285580235072e-17, 1.0070946066455787e-17, 9.810542987536606e-18, 9.428390868553739e-18, 8.934387248653573e-18, 8.341326562103362e-18, 7.664568769164315e-18, 6.921641541189054e-18, 6.13178630314041e-18, 5.3154598907919885e-18, 4.4938047294270864e-18, 3.6881012561294525e-18, 2.9192167676409437e-18, 2.2070649683369765e-18, 1.5700902157434007e-18, 1.0247898213649492e-18, 5.852867789829103e-19, 2.6296398653465517e-19, 6.616943503622235e-20, 0.0],
        },
        "q3.xy.y180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.001080628881442259, 0.004294527805367907, 0.009558458477830673, 0.016736087859429313, 0.025641519119415625, 0.036044106265963695, 0.04767442775620553, 0.06023126437267054, 0.07338940064279505, 0.08680804774883369, 0.10013966977923097, 0.11303898472617849, 0.12517190710824852, 0.13622420060887627, 0.1459096166318981, 0.15397730798983267, 0.16021832571427266, 0.16447103072441085, 0.16662528019432776, 0.1666252801943278, 0.16447103072441085, 0.1602183257142727, 0.1539773079898327, 0.14590961663189814, 0.13622420060887627, 0.12517190710824846, 0.11303898472617853, 0.10013966977923101, 0.08680804774883369, 0.0733894006427951, 0.060231264372670595, 0.04767442775620556, 0.03604410626596372, 0.02564151911941563, 0.016736087859429313, 0.009558458477830665, 0.004294527805367898, 0.001080628881442259, 0.0],
        },
        "q3.xy.y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 3.308471751811118e-20, 1.3148199326732787e-19, 2.926433894914554e-19, 5.123949106824746e-19, 7.850451078717001e-19, 1.1035324841684875e-18, 1.4596083838204707e-18, 1.8440506280647247e-18, 2.2469023647135417e-18, 2.6577299453959943e-18, 3.0658931515702035e-18, 3.460820770594526e-18, 3.832284384582159e-18, 4.170663281051681e-18, 4.467193624326786e-18, 4.7141954342768685e-18, 4.905271493768302e-18, 5.035473033227894e-18, 5.101427901175359e-18, 5.10142790117536e-18, 5.035473033227894e-18, 4.905271493768303e-18, 4.714195434276869e-18, 4.4671936243267864e-18, 4.170663281051681e-18, 3.8322843845821576e-18, 3.460820770594527e-18, 3.065893151570205e-18, 2.6577299453959943e-18, 2.2469023647135432e-18, 1.8440506280647263e-18, 1.4596083838204719e-18, 1.1035324841684883e-18, 7.850451078717003e-19, 5.123949106824746e-19, 2.9264338949145514e-19, 1.3148199326732758e-19, 3.308471751811118e-20, 0.0],
        },
        "q3.xy.y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0005403144407211295, 0.0021472639026839536, 0.004779229238915337, 0.008368043929714656, 0.012820759559707812, 0.018022053132981847, 0.023837213878102764, 0.03011563218633527, 0.03669470032139752, 0.043404023874416844, 0.050069834889615486, 0.056519492363089244, 0.06258595355412426, 0.06811210030443814, 0.07295480831594905, 0.07698865399491633, 0.08010916285713633, 0.08223551536220543, 0.08331264009716388, 0.0833126400971639, 0.08223551536220543, 0.08010916285713635, 0.07698865399491635, 0.07295480831594907, 0.06811210030443814, 0.06258595355412423, 0.056519492363089265, 0.05006983488961551, 0.043404023874416844, 0.03669470032139755, 0.030115632186335298, 0.02383721387810278, 0.01802205313298186, 0.012820759559707816, 0.008368043929714656, 0.004779229238915332, 0.002147263902683949, 0.0005403144407211295, 0.0],
        },
        "q3.xy.-y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 3.308471751811118e-20, 1.3148199326732787e-19, 2.926433894914554e-19, 5.123949106824746e-19, 7.850451078717001e-19, 1.1035324841684875e-18, 1.4596083838204707e-18, 1.8440506280647247e-18, 2.2469023647135417e-18, 2.6577299453959943e-18, 3.0658931515702035e-18, 3.460820770594526e-18, 3.832284384582159e-18, 4.170663281051681e-18, 4.467193624326786e-18, 4.7141954342768685e-18, 4.905271493768302e-18, 5.035473033227894e-18, 5.101427901175359e-18, 5.10142790117536e-18, 5.035473033227894e-18, 4.905271493768303e-18, 4.714195434276869e-18, 4.4671936243267864e-18, 4.170663281051681e-18, 3.8322843845821576e-18, 3.460820770594527e-18, 3.065893151570205e-18, 2.6577299453959943e-18, 2.2469023647135432e-18, 1.8440506280647263e-18, 1.4596083838204719e-18, 1.1035324841684883e-18, 7.850451078717003e-19, 5.123949106824746e-19, 2.9264338949145514e-19, 1.3148199326732758e-19, 3.308471751811118e-20, 0.0],
        },
        "q3.xy.-y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.0005403144407211295, -0.0021472639026839536, -0.004779229238915337, -0.008368043929714656, -0.012820759559707812, -0.018022053132981847, -0.023837213878102764, -0.03011563218633527, -0.03669470032139752, -0.043404023874416844, -0.050069834889615486, -0.056519492363089244, -0.06258595355412426, -0.06811210030443814, -0.07295480831594905, -0.07698865399491633, -0.08010916285713633, -0.08223551536220543, -0.08331264009716388, -0.0833126400971639, -0.08223551536220543, -0.08010916285713635, -0.07698865399491635, -0.07295480831594907, -0.06811210030443814, -0.06258595355412423, -0.056519492363089265, -0.05006983488961551, -0.043404023874416844, -0.03669470032139755, -0.030115632186335298, -0.02383721387810278, -0.01802205313298186, -0.012820759559707816, -0.008368043929714656, -0.004779229238915332, -0.002147263902683949, -0.0005403144407211295, 0.0],
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
            "samples": [0.0, 0.0010441878513468242, 0.0041497074885240475, 0.009236127584183164, 0.01617171252962013, 0.024776834317843235, 0.03482862481459994, 0.04606674792598683, 0.05820014216653334, 0.07091455899878804, 0.0838807017053713, 0.0967627540009839, 0.10922707749780024, 0.1209508527644605, 0.1316304401797739, 0.140989244039413, 0.1487848762393665, 0.1548154340005128, 0.15892472904454438, 0.16100633278833418, 0.1610063327883342, 0.15892472904454438, 0.1548154340005128, 0.14878487623936654, 0.14098924403941301, 0.1316304401797739, 0.12095085276446045, 0.10922707749780027, 0.09676275400098394, 0.0838807017053713, 0.0709145589987881, 0.058200142166533395, 0.04606674792598686, 0.034828624814599966, 0.024776834317843246, 0.01617171252962013, 0.009236127584183155, 0.004149707488524039, 0.0010441878513468242, 0.0],
        },
        "q4.xy.x180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
        },
        "q4.xy.x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0005220939256734121, 0.0020748537442620237, 0.004618063792091582, 0.008085856264810065, 0.012388417158921618, 0.01741431240729997, 0.023033373962993414, 0.02910007108326667, 0.03545727949939402, 0.04194035085268565, 0.04838137700049195, 0.05461353874890012, 0.06047542638223025, 0.06581522008988695, 0.0704946220197065, 0.07439243811968325, 0.0774077170002564, 0.07946236452227219, 0.08050316639416709, 0.0805031663941671, 0.07946236452227219, 0.0774077170002564, 0.07439243811968327, 0.07049462201970651, 0.06581522008988695, 0.060475426382230225, 0.05461353874890013, 0.04838137700049197, 0.04194035085268565, 0.03545727949939405, 0.029100071083266697, 0.02303337396299343, 0.017414312407299983, 0.012388417158921623, 0.008085856264810065, 0.004618063792091578, 0.0020748537442620194, 0.0005220939256734121, 0.0],
        },
        "q4.xy.x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
        },
        "q4.xy.-x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -0.0005220939256734121, -0.0020748537442620237, -0.004618063792091582, -0.008085856264810065, -0.012388417158921618, -0.01741431240729997, -0.023033373962993414, -0.02910007108326667, -0.03545727949939402, -0.04194035085268565, -0.04838137700049195, -0.05461353874890012, -0.06047542638223025, -0.06581522008988695, -0.0704946220197065, -0.07439243811968325, -0.0774077170002564, -0.07946236452227219, -0.08050316639416709, -0.0805031663941671, -0.07946236452227219, -0.0774077170002564, -0.07439243811968327, -0.07049462201970651, -0.06581522008988695, -0.060475426382230225, -0.05461353874890013, -0.04838137700049197, -0.04194035085268565, -0.03545727949939405, -0.029100071083266697, -0.02303337396299343, -0.017414312407299983, -0.012388417158921623, -0.008085856264810065, -0.004618063792091578, -0.0020748537442620194, -0.0005220939256734121, 0.0],
        },
        "q4.xy.-x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 6.393806549302202e-20, 2.5409629966093885e-19, 5.655497041243244e-19, 9.90231799306522e-19, 1.5171435420175506e-18, 2.1326381948951945e-18, 2.820774769734387e-18, 3.5637308907082975e-18, 4.342264384540595e-18, 5.136211642685845e-18, 5.925009848199384e-18, 6.6882295418950474e-18, 7.406103734606968e-18, 8.060039861825862e-18, 8.633101321353608e-18, 9.110446122403764e-18, 9.479711285366816e-18, 9.731333036488084e-18, 9.85879450458435e-18, 9.858794504584352e-18, 9.731333036488084e-18, 9.479711285366816e-18, 9.110446122403765e-18, 8.63310132135361e-18, 8.060039861825862e-18, 7.406103734606965e-18, 6.688229541895049e-18, 5.925009848199387e-18, 5.136211642685845e-18, 4.3422643845405984e-18, 3.563730890708301e-18, 2.820774769734389e-18, 2.1326381948951965e-18, 1.5171435420175513e-18, 9.90231799306522e-19, 5.655497041243239e-19, 2.5409629966093832e-19, 6.393806549302202e-20, 0.0],
        },
        "q4.xy.y180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 6.393806549302202e-20, 2.5409629966093885e-19, 5.655497041243244e-19, 9.90231799306522e-19, 1.5171435420175506e-18, 2.1326381948951945e-18, 2.820774769734387e-18, 3.5637308907082975e-18, 4.342264384540595e-18, 5.136211642685845e-18, 5.925009848199384e-18, 6.6882295418950474e-18, 7.406103734606968e-18, 8.060039861825862e-18, 8.633101321353608e-18, 9.110446122403764e-18, 9.479711285366816e-18, 9.731333036488084e-18, 9.85879450458435e-18, 9.858794504584352e-18, 9.731333036488084e-18, 9.479711285366816e-18, 9.110446122403765e-18, 8.63310132135361e-18, 8.060039861825862e-18, 7.406103734606965e-18, 6.688229541895049e-18, 5.925009848199387e-18, 5.136211642685845e-18, 4.3422643845405984e-18, 3.563730890708301e-18, 2.820774769734389e-18, 2.1326381948951965e-18, 1.5171435420175513e-18, 9.90231799306522e-19, 5.655497041243239e-19, 2.5409629966093832e-19, 6.393806549302202e-20, 0.0],
        },
        "q4.xy.y180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0010441878513468242, 0.0041497074885240475, 0.009236127584183164, 0.01617171252962013, 0.024776834317843235, 0.03482862481459994, 0.04606674792598683, 0.05820014216653334, 0.07091455899878804, 0.0838807017053713, 0.0967627540009839, 0.10922707749780024, 0.1209508527644605, 0.1316304401797739, 0.140989244039413, 0.1487848762393665, 0.1548154340005128, 0.15892472904454438, 0.16100633278833418, 0.1610063327883342, 0.15892472904454438, 0.1548154340005128, 0.14878487623936654, 0.14098924403941301, 0.1316304401797739, 0.12095085276446045, 0.10922707749780027, 0.09676275400098394, 0.0838807017053713, 0.0709145589987881, 0.058200142166533395, 0.04606674792598686, 0.034828624814599966, 0.024776834317843246, 0.01617171252962013, 0.009236127584183155, 0.004149707488524039, 0.0010441878513468242, 0.0],
        },
        "q4.xy.y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 3.196903274651101e-20, 1.2704814983046943e-19, 2.827748520621622e-19, 4.95115899653261e-19, 7.585717710087753e-19, 1.0663190974475973e-18, 1.4103873848671936e-18, 1.7818654453541487e-18, 2.1711321922702977e-18, 2.5681058213429225e-18, 2.962504924099692e-18, 3.3441147709475237e-18, 3.703051867303484e-18, 4.030019930912931e-18, 4.316550660676804e-18, 4.555223061201882e-18, 4.739855642683408e-18, 4.865666518244042e-18, 4.929397252292175e-18, 4.929397252292176e-18, 4.865666518244042e-18, 4.739855642683408e-18, 4.555223061201883e-18, 4.316550660676805e-18, 4.030019930912931e-18, 3.7030518673034826e-18, 3.3441147709475245e-18, 2.9625049240996934e-18, 2.5681058213429225e-18, 2.1711321922702992e-18, 1.7818654453541507e-18, 1.4103873848671945e-18, 1.0663190974475982e-18, 7.585717710087757e-19, 4.95115899653261e-19, 2.8277485206216193e-19, 1.2704814983046916e-19, 3.196903274651101e-20, 0.0],
        },
        "q4.xy.y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0005220939256734121, 0.0020748537442620237, 0.004618063792091582, 0.008085856264810065, 0.012388417158921618, 0.01741431240729997, 0.023033373962993414, 0.02910007108326667, 0.03545727949939402, 0.04194035085268565, 0.04838137700049195, 0.05461353874890012, 0.06047542638223025, 0.06581522008988695, 0.0704946220197065, 0.07439243811968325, 0.0774077170002564, 0.07946236452227219, 0.08050316639416709, 0.0805031663941671, 0.07946236452227219, 0.0774077170002564, 0.07439243811968327, 0.07049462201970651, 0.06581522008988695, 0.060475426382230225, 0.05461353874890013, 0.04838137700049197, 0.04194035085268565, 0.03545727949939405, 0.029100071083266697, 0.02303337396299343, 0.017414312407299983, 0.012388417158921623, 0.008085856264810065, 0.004618063792091578, 0.0020748537442620194, 0.0005220939256734121, 0.0],
        },
        "q4.xy.-y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 3.196903274651101e-20, 1.2704814983046943e-19, 2.827748520621622e-19, 4.95115899653261e-19, 7.585717710087753e-19, 1.0663190974475973e-18, 1.4103873848671936e-18, 1.7818654453541487e-18, 2.1711321922702977e-18, 2.5681058213429225e-18, 2.962504924099692e-18, 3.3441147709475237e-18, 3.703051867303484e-18, 4.030019930912931e-18, 4.316550660676804e-18, 4.555223061201882e-18, 4.739855642683408e-18, 4.865666518244042e-18, 4.929397252292175e-18, 4.929397252292176e-18, 4.865666518244042e-18, 4.739855642683408e-18, 4.555223061201883e-18, 4.316550660676805e-18, 4.030019930912931e-18, 3.7030518673034826e-18, 3.3441147709475245e-18, 2.9625049240996934e-18, 2.5681058213429225e-18, 2.1711321922702992e-18, 1.7818654453541507e-18, 1.4103873848671945e-18, 1.0663190974475982e-18, 7.585717710087757e-19, 4.95115899653261e-19, 2.8277485206216193e-19, 1.2704814983046916e-19, 3.196903274651101e-20, 0.0],
        },
        "q4.xy.-y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.0005220939256734121, -0.0020748537442620237, -0.004618063792091582, -0.008085856264810065, -0.012388417158921618, -0.01741431240729997, -0.023033373962993414, -0.02910007108326667, -0.03545727949939402, -0.04194035085268565, -0.04838137700049195, -0.05461353874890012, -0.06047542638223025, -0.06581522008988695, -0.0704946220197065, -0.07439243811968325, -0.0774077170002564, -0.07946236452227219, -0.08050316639416709, -0.0805031663941671, -0.07946236452227219, -0.0774077170002564, -0.07439243811968327, -0.07049462201970651, -0.06581522008988695, -0.060475426382230225, -0.05461353874890013, -0.04838137700049197, -0.04194035085268565, -0.03545727949939405, -0.029100071083266697, -0.02303337396299343, -0.017414312407299983, -0.012388417158921623, -0.008085856264810065, -0.004618063792091578, -0.0020748537442620194, -0.0005220939256734121, 0.0],
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
            "samples": [0.0, 0.000741300610345739, 0.00294600314496229, 0.006557006966280023, 0.01148078897209983, 0.017589825794814638, 0.024725896589645482, 0.03270418087141174, 0.041318045268015524, 0.050344395216239526, 0.05954945299374817, 0.06869481243929827, 0.0775436135470864, 0.0858666770164821, 0.09344843987553203, 0.10009253844870358, 0.10562689407293598, 0.10990816984462481, 0.112825482970134, 0.11430327657190693, 0.11430327657190695, 0.112825482970134, 0.10990816984462483, 0.105626894072936, 0.10009253844870361, 0.09344843987553203, 0.08586667701648207, 0.07754361354708643, 0.0686948124392983, 0.05954945299374817, 0.050344395216239575, 0.04131804526801556, 0.03270418087141177, 0.024725896589645503, 0.017589825794814645, 0.01148078897209983, 0.006557006966280017, 0.0029460031449622835, 0.000741300610345739, 0.0],
        },
        "q5.xy.x180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
        },
        "q5.xy.x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0003706503051728695, 0.001473001572481145, 0.0032785034831400114, 0.005740394486049915, 0.008794912897407319, 0.012362948294822741, 0.01635209043570587, 0.020659022634007762, 0.025172197608119763, 0.029774726496874085, 0.034347406219649136, 0.0387718067735432, 0.04293333850824105, 0.046724219937766015, 0.05004626922435179, 0.05281344703646799, 0.05495408492231241, 0.056412741485067, 0.05715163828595347, 0.057151638285953474, 0.056412741485067, 0.054954084922312414, 0.052813447036468, 0.050046269224351805, 0.046724219937766015, 0.042933338508241034, 0.038771806773543215, 0.03434740621964915, 0.029774726496874085, 0.025172197608119787, 0.02065902263400778, 0.016352090435705884, 0.012362948294822752, 0.008794912897407322, 0.005740394486049915, 0.0032785034831400084, 0.0014730015724811417, 0.0003706503051728695, 0.0],
        },
        "q5.xy.x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
        },
        "q5.xy.-x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -0.0003706503051728695, -0.001473001572481145, -0.0032785034831400114, -0.005740394486049915, -0.008794912897407319, -0.012362948294822741, -0.01635209043570587, -0.020659022634007762, -0.025172197608119763, -0.029774726496874085, -0.034347406219649136, -0.0387718067735432, -0.04293333850824105, -0.046724219937766015, -0.05004626922435179, -0.05281344703646799, -0.05495408492231241, -0.056412741485067, -0.05715163828595347, -0.057151638285953474, -0.056412741485067, -0.054954084922312414, -0.052813447036468, -0.050046269224351805, -0.046724219937766015, -0.042933338508241034, -0.038771806773543215, -0.03434740621964915, -0.029774726496874085, -0.025172197608119787, -0.02065902263400778, -0.016352090435705884, -0.012362948294822752, -0.008794912897407322, -0.005740394486049915, -0.0032785034831400084, -0.0014730015724811417, -0.0003706503051728695, 0.0],
        },
        "q5.xy.-x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 4.5391570983294425e-20, 1.8039066608780522e-19, 4.0150087966208634e-19, 7.029955733184144e-19, 1.0770661928589647e-18, 1.51402450572789e-18, 2.0025535211455244e-18, 2.5300005942250326e-18, 3.0827051228288527e-18, 3.646352349988473e-18, 4.206344108590721e-18, 4.7481769062379345e-18, 5.25781755808272e-18, 5.722066638944209e-18, 6.128900341486911e-18, 6.467781886514879e-18, 6.729934420018172e-18, 6.908568329081441e-18, 6.999057089292023e-18, 6.999057089292025e-18, 6.908568329081441e-18, 6.7299344200181725e-18, 6.467781886514881e-18, 6.128900341486913e-18, 5.722066638944209e-18, 5.257817558082718e-18, 4.748176906237937e-18, 4.2063441085907224e-18, 3.646352349988473e-18, 3.082705122828856e-18, 2.530000594225035e-18, 2.002553521145526e-18, 1.514024505727891e-18, 1.077066192858965e-18, 7.029955733184144e-19, 4.0150087966208595e-19, 1.8039066608780481e-19, 4.5391570983294425e-20, 0.0],
        },
        "q5.xy.y180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 4.5391570983294425e-20, 1.8039066608780522e-19, 4.0150087966208634e-19, 7.029955733184144e-19, 1.0770661928589647e-18, 1.51402450572789e-18, 2.0025535211455244e-18, 2.5300005942250326e-18, 3.0827051228288527e-18, 3.646352349988473e-18, 4.206344108590721e-18, 4.7481769062379345e-18, 5.25781755808272e-18, 5.722066638944209e-18, 6.128900341486911e-18, 6.467781886514879e-18, 6.729934420018172e-18, 6.908568329081441e-18, 6.999057089292023e-18, 6.999057089292025e-18, 6.908568329081441e-18, 6.7299344200181725e-18, 6.467781886514881e-18, 6.128900341486913e-18, 5.722066638944209e-18, 5.257817558082718e-18, 4.748176906237937e-18, 4.2063441085907224e-18, 3.646352349988473e-18, 3.082705122828856e-18, 2.530000594225035e-18, 2.002553521145526e-18, 1.514024505727891e-18, 1.077066192858965e-18, 7.029955733184144e-19, 4.0150087966208595e-19, 1.8039066608780481e-19, 4.5391570983294425e-20, 0.0],
        },
        "q5.xy.y180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.000741300610345739, 0.00294600314496229, 0.006557006966280023, 0.01148078897209983, 0.017589825794814638, 0.024725896589645482, 0.03270418087141174, 0.041318045268015524, 0.050344395216239526, 0.05954945299374817, 0.06869481243929827, 0.0775436135470864, 0.0858666770164821, 0.09344843987553203, 0.10009253844870358, 0.10562689407293598, 0.10990816984462481, 0.112825482970134, 0.11430327657190693, 0.11430327657190695, 0.112825482970134, 0.10990816984462483, 0.105626894072936, 0.10009253844870361, 0.09344843987553203, 0.08586667701648207, 0.07754361354708643, 0.0686948124392983, 0.05954945299374817, 0.050344395216239575, 0.04131804526801556, 0.03270418087141177, 0.024725896589645503, 0.017589825794814645, 0.01148078897209983, 0.006557006966280017, 0.0029460031449622835, 0.000741300610345739, 0.0],
        },
        "q5.xy.y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 2.2695785491647213e-20, 9.019533304390261e-20, 2.0075043983104317e-19, 3.514977866592072e-19, 5.385330964294823e-19, 7.57012252863945e-19, 1.0012767605727622e-18, 1.2650002971125163e-18, 1.5413525614144264e-18, 1.8231761749942366e-18, 2.1031720542953605e-18, 2.3740884531189672e-18, 2.62890877904136e-18, 2.8610333194721045e-18, 3.0644501707434555e-18, 3.2338909432574396e-18, 3.364967210009086e-18, 3.4542841645407204e-18, 3.499528544646012e-18, 3.4995285446460125e-18, 3.4542841645407204e-18, 3.3649672100090862e-18, 3.2338909432574403e-18, 3.0644501707434566e-18, 2.8610333194721045e-18, 2.628908779041359e-18, 2.3740884531189684e-18, 2.1031720542953612e-18, 1.8231761749942366e-18, 1.541352561414428e-18, 1.2650002971125175e-18, 1.001276760572763e-18, 7.570122528639455e-19, 5.385330964294825e-19, 3.514977866592072e-19, 2.0075043983104298e-19, 9.019533304390241e-20, 2.2695785491647213e-20, 0.0],
        },
        "q5.xy.y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0003706503051728695, 0.001473001572481145, 0.0032785034831400114, 0.005740394486049915, 0.008794912897407319, 0.012362948294822741, 0.01635209043570587, 0.020659022634007762, 0.025172197608119763, 0.029774726496874085, 0.034347406219649136, 0.0387718067735432, 0.04293333850824105, 0.046724219937766015, 0.05004626922435179, 0.05281344703646799, 0.05495408492231241, 0.056412741485067, 0.05715163828595347, 0.057151638285953474, 0.056412741485067, 0.054954084922312414, 0.052813447036468, 0.050046269224351805, 0.046724219937766015, 0.042933338508241034, 0.038771806773543215, 0.03434740621964915, 0.029774726496874085, 0.025172197608119787, 0.02065902263400778, 0.016352090435705884, 0.012362948294822752, 0.008794912897407322, 0.005740394486049915, 0.0032785034831400084, 0.0014730015724811417, 0.0003706503051728695, 0.0],
        },
        "q5.xy.-y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 2.2695785491647213e-20, 9.019533304390261e-20, 2.0075043983104317e-19, 3.514977866592072e-19, 5.385330964294823e-19, 7.57012252863945e-19, 1.0012767605727622e-18, 1.2650002971125163e-18, 1.5413525614144264e-18, 1.8231761749942366e-18, 2.1031720542953605e-18, 2.3740884531189672e-18, 2.62890877904136e-18, 2.8610333194721045e-18, 3.0644501707434555e-18, 3.2338909432574396e-18, 3.364967210009086e-18, 3.4542841645407204e-18, 3.499528544646012e-18, 3.4995285446460125e-18, 3.4542841645407204e-18, 3.3649672100090862e-18, 3.2338909432574403e-18, 3.0644501707434566e-18, 2.8610333194721045e-18, 2.628908779041359e-18, 2.3740884531189684e-18, 2.1031720542953612e-18, 1.8231761749942366e-18, 1.541352561414428e-18, 1.2650002971125175e-18, 1.001276760572763e-18, 7.570122528639455e-19, 5.385330964294825e-19, 3.514977866592072e-19, 2.0075043983104298e-19, 9.019533304390241e-20, 2.2695785491647213e-20, 0.0],
        },
        "q5.xy.-y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.0003706503051728695, -0.001473001572481145, -0.0032785034831400114, -0.005740394486049915, -0.008794912897407319, -0.012362948294822741, -0.01635209043570587, -0.020659022634007762, -0.025172197608119763, -0.029774726496874085, -0.034347406219649136, -0.0387718067735432, -0.04293333850824105, -0.046724219937766015, -0.05004626922435179, -0.05281344703646799, -0.05495408492231241, -0.056412741485067, -0.05715163828595347, -0.057151638285953474, -0.056412741485067, -0.054954084922312414, -0.052813447036468, -0.050046269224351805, -0.046724219937766015, -0.042933338508241034, -0.038771806773543215, -0.03434740621964915, -0.029774726496874085, -0.025172197608119787, -0.02065902263400778, -0.016352090435705884, -0.012362948294822752, -0.008794912897407322, -0.005740394486049915, -0.0032785034831400084, -0.0014730015724811417, -0.0003706503051728695, 0.0],
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
            "samples": [0.0, 0.000932688204479085, 0.0037065966833388963, 0.008249882664044025, 0.014444877426172512, 0.02213113385946622, 0.03110958195970752, 0.04114768463726193, 0.051985460305553434, 0.06334221626759488, 0.07492381850939873, 0.08643030961643793, 0.09756367751312184, 0.10803557381901534, 0.11757478192042971, 0.1259342413382538, 0.13289744646458787, 0.13828405394426324, 0.14195455347301097, 0.14381388104106116, 0.1438138810410612, 0.14195455347301097, 0.13828405394426327, 0.1328974464645879, 0.12593424133825382, 0.11757478192042971, 0.10803557381901528, 0.09756367751312187, 0.08643030961643795, 0.07492381850939873, 0.06334221626759494, 0.05198546030555348, 0.04114768463726196, 0.031109581959707543, 0.022131133859466228, 0.014444877426172512, 0.008249882664044018, 0.0037065966833388884, 0.000932688204479085, 0.0],
        },
        "q6.xy.x180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
        },
        "q6.xy.x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0004663441022395425, 0.0018532983416694481, 0.004124941332022012, 0.007222438713086256, 0.01106556692973311, 0.01555479097985376, 0.020573842318630964, 0.025992730152776717, 0.03167110813379744, 0.03746190925469937, 0.04321515480821896, 0.04878183875656092, 0.05401778690950767, 0.058787390960214854, 0.0629671206691269, 0.06644872323229394, 0.06914202697213162, 0.07097727673650549, 0.07190694052053058, 0.0719069405205306, 0.07097727673650549, 0.06914202697213163, 0.06644872323229395, 0.06296712066912691, 0.058787390960214854, 0.05401778690950764, 0.04878183875656093, 0.04321515480821898, 0.03746190925469937, 0.03167110813379747, 0.02599273015277674, 0.02057384231863098, 0.015554790979853772, 0.011065566929733114, 0.007222438713086256, 0.004124941332022009, 0.0018532983416694442, 0.0004663441022395425, 0.0],
        },
        "q6.xy.x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
        },
        "q6.xy.-x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -0.0004663441022395425, -0.0018532983416694481, -0.004124941332022012, -0.007222438713086256, -0.01106556692973311, -0.01555479097985376, -0.020573842318630964, -0.025992730152776717, -0.03167110813379744, -0.03746190925469937, -0.04321515480821896, -0.04878183875656092, -0.05401778690950767, -0.058787390960214854, -0.0629671206691269, -0.06644872323229394, -0.06914202697213162, -0.07097727673650549, -0.07190694052053058, -0.0719069405205306, -0.07097727673650549, -0.06914202697213163, -0.06644872323229395, -0.06296712066912691, -0.058787390960214854, -0.05401778690950764, -0.04878183875656093, -0.04321515480821898, -0.03746190925469937, -0.03167110813379747, -0.02599273015277674, -0.02057384231863098, -0.015554790979853772, -0.011065566929733114, -0.007222438713086256, -0.004124941332022009, -0.0018532983416694442, -0.0004663441022395425, 0.0],
        },
        "q6.xy.-x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 5.711068121089018e-20, 2.2696358819905875e-19, 5.051596198931377e-19, 8.844936452019012e-19, 1.355141112124846e-18, 1.904912498488403e-18, 2.519569014167377e-18, 3.18319137826989e-18, 3.878592120150474e-18, 4.587760725871619e-18, 5.2923301010542706e-18, 5.974052268974463e-18, 6.6152709835752365e-18, 7.199379016965116e-18, 7.71124827789714e-18, 8.137621621385713e-18, 8.467456201798096e-18, 8.692209476755734e-18, 8.80606045449469e-18, 8.806060454494691e-18, 8.692209476755734e-18, 8.467456201798097e-18, 8.137621621385715e-18, 7.711248277897141e-18, 7.199379016965116e-18, 6.615270983575233e-18, 5.974052268974465e-18, 5.292330101054272e-18, 4.587760725871619e-18, 3.878592120150477e-18, 3.183191378269893e-18, 2.519569014167379e-18, 1.9049124984884044e-18, 1.3551411121248463e-18, 8.844936452019012e-19, 5.051596198931373e-19, 2.2696358819905826e-19, 5.711068121089018e-20, 0.0],
        },
        "q6.xy.y180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 5.711068121089018e-20, 2.2696358819905875e-19, 5.051596198931377e-19, 8.844936452019012e-19, 1.355141112124846e-18, 1.904912498488403e-18, 2.519569014167377e-18, 3.18319137826989e-18, 3.878592120150474e-18, 4.587760725871619e-18, 5.2923301010542706e-18, 5.974052268974463e-18, 6.6152709835752365e-18, 7.199379016965116e-18, 7.71124827789714e-18, 8.137621621385713e-18, 8.467456201798096e-18, 8.692209476755734e-18, 8.80606045449469e-18, 8.806060454494691e-18, 8.692209476755734e-18, 8.467456201798097e-18, 8.137621621385715e-18, 7.711248277897141e-18, 7.199379016965116e-18, 6.615270983575233e-18, 5.974052268974465e-18, 5.292330101054272e-18, 4.587760725871619e-18, 3.878592120150477e-18, 3.183191378269893e-18, 2.519569014167379e-18, 1.9049124984884044e-18, 1.3551411121248463e-18, 8.844936452019012e-19, 5.051596198931373e-19, 2.2696358819905826e-19, 5.711068121089018e-20, 0.0],
        },
        "q6.xy.y180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.000932688204479085, 0.0037065966833388963, 0.008249882664044025, 0.014444877426172512, 0.02213113385946622, 0.03110958195970752, 0.04114768463726193, 0.051985460305553434, 0.06334221626759488, 0.07492381850939873, 0.08643030961643793, 0.09756367751312184, 0.10803557381901534, 0.11757478192042971, 0.1259342413382538, 0.13289744646458787, 0.13828405394426324, 0.14195455347301097, 0.14381388104106116, 0.1438138810410612, 0.14195455347301097, 0.13828405394426327, 0.1328974464645879, 0.12593424133825382, 0.11757478192042971, 0.10803557381901528, 0.09756367751312187, 0.08643030961643795, 0.07492381850939873, 0.06334221626759494, 0.05198546030555348, 0.04114768463726196, 0.031109581959707543, 0.022131133859466228, 0.014444877426172512, 0.008249882664044018, 0.0037065966833388884, 0.000932688204479085, 0.0],
        },
        "q6.xy.y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 2.855534060544509e-20, 1.1348179409952937e-19, 2.5257980994656885e-19, 4.422468226009506e-19, 6.77570556062423e-19, 9.524562492442015e-19, 1.2597845070836885e-18, 1.591595689134945e-18, 1.939296060075237e-18, 2.2938803629358095e-18, 2.6461650505271353e-18, 2.9870261344872316e-18, 3.3076354917876183e-18, 3.599689508482558e-18, 3.85562413894857e-18, 4.0688108106928565e-18, 4.233728100899048e-18, 4.346104738377867e-18, 4.403030227247345e-18, 4.4030302272473455e-18, 4.346104738377867e-18, 4.233728100899049e-18, 4.068810810692857e-18, 3.8556241389485704e-18, 3.599689508482558e-18, 3.3076354917876163e-18, 2.9870261344872323e-18, 2.646165050527136e-18, 2.2938803629358095e-18, 1.9392960600752387e-18, 1.5915956891349465e-18, 1.2597845070836894e-18, 9.524562492442022e-19, 6.775705560624231e-19, 4.422468226009506e-19, 2.5257980994656866e-19, 1.1348179409952913e-19, 2.855534060544509e-20, 0.0],
        },
        "q6.xy.y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0004663441022395425, 0.0018532983416694481, 0.004124941332022012, 0.007222438713086256, 0.01106556692973311, 0.01555479097985376, 0.020573842318630964, 0.025992730152776717, 0.03167110813379744, 0.03746190925469937, 0.04321515480821896, 0.04878183875656092, 0.05401778690950767, 0.058787390960214854, 0.0629671206691269, 0.06644872323229394, 0.06914202697213162, 0.07097727673650549, 0.07190694052053058, 0.0719069405205306, 0.07097727673650549, 0.06914202697213163, 0.06644872323229395, 0.06296712066912691, 0.058787390960214854, 0.05401778690950764, 0.04878183875656093, 0.04321515480821898, 0.03746190925469937, 0.03167110813379747, 0.02599273015277674, 0.02057384231863098, 0.015554790979853772, 0.011065566929733114, 0.007222438713086256, 0.004124941332022009, 0.0018532983416694442, 0.0004663441022395425, 0.0],
        },
        "q6.xy.-y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 2.855534060544509e-20, 1.1348179409952937e-19, 2.5257980994656885e-19, 4.422468226009506e-19, 6.77570556062423e-19, 9.524562492442015e-19, 1.2597845070836885e-18, 1.591595689134945e-18, 1.939296060075237e-18, 2.2938803629358095e-18, 2.6461650505271353e-18, 2.9870261344872316e-18, 3.3076354917876183e-18, 3.599689508482558e-18, 3.85562413894857e-18, 4.0688108106928565e-18, 4.233728100899048e-18, 4.346104738377867e-18, 4.403030227247345e-18, 4.4030302272473455e-18, 4.346104738377867e-18, 4.233728100899049e-18, 4.068810810692857e-18, 3.8556241389485704e-18, 3.599689508482558e-18, 3.3076354917876163e-18, 2.9870261344872323e-18, 2.646165050527136e-18, 2.2938803629358095e-18, 1.9392960600752387e-18, 1.5915956891349465e-18, 1.2597845070836894e-18, 9.524562492442022e-19, 6.775705560624231e-19, 4.422468226009506e-19, 2.5257980994656866e-19, 1.1348179409952913e-19, 2.855534060544509e-20, 0.0],
        },
        "q6.xy.-y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.0004663441022395425, -0.0018532983416694481, -0.004124941332022012, -0.007222438713086256, -0.01106556692973311, -0.01555479097985376, -0.020573842318630964, -0.025992730152776717, -0.03167110813379744, -0.03746190925469937, -0.04321515480821896, -0.04878183875656092, -0.05401778690950767, -0.058787390960214854, -0.0629671206691269, -0.06644872323229394, -0.06914202697213162, -0.07097727673650549, -0.07190694052053058, -0.0719069405205306, -0.07097727673650549, -0.06914202697213163, -0.06644872323229395, -0.06296712066912691, -0.058787390960214854, -0.05401778690950764, -0.04878183875656093, -0.04321515480821898, -0.03746190925469937, -0.03167110813379747, -0.02599273015277674, -0.02057384231863098, -0.015554790979853772, -0.011065566929733114, -0.007222438713086256, -0.004124941332022009, -0.0018532983416694442, -0.0004663441022395425, 0.0],
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
            "samples": [0.0, 0.0001984292420197456, 0.0007885777549407545, 0.0017551610022691186, 0.0030731449856218488, 0.004708394612135234, 0.006618557775439673, 0.008754162252968118, 0.011059897010533984, 0.013476044729063047, 0.015940028451789393, 0.018388032294565478, 0.02075665424374067, 0.022984548235011164, 0.025014012984261907, 0.02679248642051608, 0.028273907015963815, 0.029419906755337427, 0.030200804847353102, 0.030596376441614528, 0.03059637644161453, 0.030200804847353102, 0.02941990675533743, 0.028273907015963818, 0.026792486420516088, 0.025014012984261907, 0.022984548235011157, 0.020756654243740676, 0.018388032294565485, 0.015940028451789393, 0.01347604472906306, 0.011059897010533995, 0.008754162252968125, 0.006618557775439678, 0.004708394612135236, 0.0030731449856218488, 0.0017551610022691168, 0.0007885777549407529, 0.0001984292420197456, 0.0],
        },
        "q7.xy.x180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
        },
        "q7.xy.x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 9.92146210098728e-05, 0.00039428887747037725, 0.0008775805011345593, 0.0015365724928109244, 0.002354197306067617, 0.0033092788877198366, 0.004377081126484059, 0.005529948505266992, 0.006738022364531524, 0.007970014225894696, 0.009194016147282739, 0.010378327121870335, 0.011492274117505582, 0.012507006492130953, 0.01339624321025804, 0.014136953507981907, 0.014709953377668714, 0.015100402423676551, 0.015298188220807264, 0.015298188220807266, 0.015100402423676551, 0.014709953377668715, 0.014136953507981909, 0.013396243210258044, 0.012507006492130953, 0.011492274117505578, 0.010378327121870338, 0.009194016147282743, 0.007970014225894696, 0.00673802236453153, 0.005529948505266997, 0.0043770811264840625, 0.003309278887719839, 0.002354197306067618, 0.0015365724928109244, 0.0008775805011345584, 0.00039428887747037643, 9.92146210098728e-05, 0.0],
        },
        "q7.xy.x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
        },
        "q7.xy.-x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -9.92146210098728e-05, -0.00039428887747037725, -0.0008775805011345593, -0.0015365724928109244, -0.002354197306067617, -0.0033092788877198366, -0.004377081126484059, -0.005529948505266992, -0.006738022364531524, -0.007970014225894696, -0.009194016147282739, -0.010378327121870335, -0.011492274117505582, -0.012507006492130953, -0.01339624321025804, -0.014136953507981907, -0.014709953377668714, -0.015100402423676551, -0.015298188220807264, -0.015298188220807266, -0.015100402423676551, -0.014709953377668715, -0.014136953507981909, -0.013396243210258044, -0.012507006492130953, -0.011492274117505578, -0.010378327121870338, -0.009194016147282743, -0.007970014225894696, -0.00673802236453153, -0.005529948505266997, -0.0043770811264840625, -0.003309278887719839, -0.002354197306067618, -0.0015365724928109244, -0.0008775805011345584, -0.00039428887747037643, -9.92146210098728e-05, 0.0],
        },
        "q7.xy.-x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 1.2150286804835847e-20, 4.8286461173350047e-20, 1.0747261517085682e-19, 1.8817585849787678e-19, 2.883060195437029e-19, 4.052697797332011e-19, 5.360378391156994e-19, 6.772233736424912e-19, 8.25169752130681e-19, 9.76045241090081e-19, 1.1259422446078887e-18, 1.2709785090302667e-18, 1.4073976712927185e-18, 1.5316665467503338e-18, 1.6405666368041973e-18, 1.731277486324499e-18, 1.8014497319568786e-18, 1.8492659493992424e-18] + [1.873487723736536e-18] * 2 + [1.8492659493992424e-18, 1.801449731956879e-18, 1.7312774863244992e-18, 1.6405666368041977e-18, 1.5316665467503338e-18, 1.407397671292718e-18, 1.2709785090302673e-18, 1.125942244607889e-18, 9.76045241090081e-19, 8.251697521306818e-19, 6.772233736424918e-19, 5.360378391156998e-19, 4.052697797332014e-19, 2.88306019543703e-19, 1.8817585849787678e-19, 1.0747261517085671e-19, 4.8286461173349945e-20, 1.2150286804835847e-20, 0.0],
        },
        "q7.xy.y180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 1.2150286804835847e-20, 4.8286461173350047e-20, 1.0747261517085682e-19, 1.8817585849787678e-19, 2.883060195437029e-19, 4.052697797332011e-19, 5.360378391156994e-19, 6.772233736424912e-19, 8.25169752130681e-19, 9.76045241090081e-19, 1.1259422446078887e-18, 1.2709785090302667e-18, 1.4073976712927185e-18, 1.5316665467503338e-18, 1.6405666368041973e-18, 1.731277486324499e-18, 1.8014497319568786e-18, 1.8492659493992424e-18] + [1.873487723736536e-18] * 2 + [1.8492659493992424e-18, 1.801449731956879e-18, 1.7312774863244992e-18, 1.6405666368041977e-18, 1.5316665467503338e-18, 1.407397671292718e-18, 1.2709785090302673e-18, 1.125942244607889e-18, 9.76045241090081e-19, 8.251697521306818e-19, 6.772233736424918e-19, 5.360378391156998e-19, 4.052697797332014e-19, 2.88306019543703e-19, 1.8817585849787678e-19, 1.0747261517085671e-19, 4.8286461173349945e-20, 1.2150286804835847e-20, 0.0],
        },
        "q7.xy.y180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0001984292420197456, 0.0007885777549407545, 0.0017551610022691186, 0.0030731449856218488, 0.004708394612135234, 0.006618557775439673, 0.008754162252968118, 0.011059897010533984, 0.013476044729063047, 0.015940028451789393, 0.018388032294565478, 0.02075665424374067, 0.022984548235011164, 0.025014012984261907, 0.02679248642051608, 0.028273907015963815, 0.029419906755337427, 0.030200804847353102, 0.030596376441614528, 0.03059637644161453, 0.030200804847353102, 0.02941990675533743, 0.028273907015963818, 0.026792486420516088, 0.025014012984261907, 0.022984548235011157, 0.020756654243740676, 0.018388032294565485, 0.015940028451789393, 0.01347604472906306, 0.011059897010533995, 0.008754162252968125, 0.006618557775439678, 0.004708394612135236, 0.0030731449856218488, 0.0017551610022691168, 0.0007885777549407529, 0.0001984292420197456, 0.0],
        },
        "q7.xy.y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 6.0751434024179234e-21, 2.4143230586675023e-20, 5.373630758542841e-20, 9.408792924893839e-20, 1.4415300977185146e-19, 2.0263488986660056e-19, 2.680189195578497e-19, 3.386116868212456e-19, 4.125848760653405e-19, 4.880226205450405e-19, 5.629711223039444e-19, 6.354892545151334e-19, 7.036988356463592e-19, 7.658332733751669e-19, 8.202833184020986e-19, 8.656387431622495e-19, 9.007248659784393e-19, 9.246329746996212e-19] + [9.36743861868268e-19] * 2 + [9.246329746996212e-19, 9.007248659784395e-19, 8.656387431622496e-19, 8.202833184020988e-19, 7.658332733751669e-19, 7.03698835646359e-19, 6.354892545151337e-19, 5.629711223039445e-19, 4.880226205450405e-19, 4.125848760653409e-19, 3.386116868212459e-19, 2.680189195578499e-19, 2.026348898666007e-19, 1.441530097718515e-19, 9.408792924893839e-20, 5.3736307585428355e-20, 2.4143230586674972e-20, 6.0751434024179234e-21, 0.0],
        },
        "q7.xy.y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 9.92146210098728e-05, 0.00039428887747037725, 0.0008775805011345593, 0.0015365724928109244, 0.002354197306067617, 0.0033092788877198366, 0.004377081126484059, 0.005529948505266992, 0.006738022364531524, 0.007970014225894696, 0.009194016147282739, 0.010378327121870335, 0.011492274117505582, 0.012507006492130953, 0.01339624321025804, 0.014136953507981907, 0.014709953377668714, 0.015100402423676551, 0.015298188220807264, 0.015298188220807266, 0.015100402423676551, 0.014709953377668715, 0.014136953507981909, 0.013396243210258044, 0.012507006492130953, 0.011492274117505578, 0.010378327121870338, 0.009194016147282743, 0.007970014225894696, 0.00673802236453153, 0.005529948505266997, 0.0043770811264840625, 0.003309278887719839, 0.002354197306067618, 0.0015365724928109244, 0.0008775805011345584, 0.00039428887747037643, 9.92146210098728e-05, 0.0],
        },
        "q7.xy.-y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 6.0751434024179234e-21, 2.4143230586675023e-20, 5.373630758542841e-20, 9.408792924893839e-20, 1.4415300977185146e-19, 2.0263488986660056e-19, 2.680189195578497e-19, 3.386116868212456e-19, 4.125848760653405e-19, 4.880226205450405e-19, 5.629711223039444e-19, 6.354892545151334e-19, 7.036988356463592e-19, 7.658332733751669e-19, 8.202833184020986e-19, 8.656387431622495e-19, 9.007248659784393e-19, 9.246329746996212e-19] + [9.36743861868268e-19] * 2 + [9.246329746996212e-19, 9.007248659784395e-19, 8.656387431622496e-19, 8.202833184020988e-19, 7.658332733751669e-19, 7.03698835646359e-19, 6.354892545151337e-19, 5.629711223039445e-19, 4.880226205450405e-19, 4.125848760653409e-19, 3.386116868212459e-19, 2.680189195578499e-19, 2.026348898666007e-19, 1.441530097718515e-19, 9.408792924893839e-20, 5.3736307585428355e-20, 2.4143230586674972e-20, 6.0751434024179234e-21, 0.0],
        },
        "q7.xy.-y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -9.92146210098728e-05, -0.00039428887747037725, -0.0008775805011345593, -0.0015365724928109244, -0.002354197306067617, -0.0033092788877198366, -0.004377081126484059, -0.005529948505266992, -0.006738022364531524, -0.007970014225894696, -0.009194016147282739, -0.010378327121870335, -0.011492274117505582, -0.012507006492130953, -0.01339624321025804, -0.014136953507981907, -0.014709953377668714, -0.015100402423676551, -0.015298188220807264, -0.015298188220807266, -0.015100402423676551, -0.014709953377668715, -0.014136953507981909, -0.013396243210258044, -0.012507006492130953, -0.011492274117505578, -0.010378327121870338, -0.009194016147282743, -0.007970014225894696, -0.00673802236453153, -0.005529948505266997, -0.0043770811264840625, -0.003309278887719839, -0.002354197306067618, -0.0015365724928109244, -0.0008775805011345584, -0.00039428887747037643, -9.92146210098728e-05, 0.0],
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
            "samples": [0.0, 0.0008576065731987051, 0.003408214733028973, 0.007585765067924001, 0.013282061218576217, 0.020349572106810397, 0.02860525291301387, 0.03783528584081555, 0.047800617885698525, 0.058243152182248355, 0.0688924325773952, 0.0794726483027143, 0.08970977732845153, 0.09933868339015663, 0.10810998287866297, 0.11579650374456989, 0.122199169134994, 0.12715215337948865, 0.1305271767878043, 0.13223682802648376, 0.1322368280264838, 0.1305271767878043, 0.12715215337948865, 0.12219916913499403, 0.11579650374456991, 0.10810998287866297, 0.09933868339015657, 0.08970977732845156, 0.07947264830271435, 0.0688924325773952, 0.0582431521822484, 0.04780061788569857, 0.03783528584081559, 0.028605252913013895, 0.020349572106810404, 0.013282061218576217, 0.007585765067923993, 0.0034082147330289658, 0.0008576065731987051, 0.0],
        },
        "q8.xy.x180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
        },
        "q8.xy.x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.00042880328659935255, 0.0017041073665144866, 0.0037928825339620005, 0.006641030609288109, 0.010174786053405199, 0.014302626456506935, 0.018917642920407776, 0.023900308942849263, 0.029121576091124177, 0.0344462162886976, 0.03973632415135715, 0.04485488866422577, 0.04966934169507831, 0.054054991439331485, 0.05789825187228494, 0.061099584567497, 0.06357607668974433, 0.06526358839390214, 0.06611841401324188, 0.0661184140132419, 0.06526358839390214, 0.06357607668974433, 0.06109958456749701, 0.05789825187228496, 0.054054991439331485, 0.049669341695078285, 0.04485488866422578, 0.03973632415135717, 0.0344462162886976, 0.0291215760911242, 0.023900308942849283, 0.018917642920407794, 0.014302626456506947, 0.010174786053405202, 0.006641030609288109, 0.0037928825339619966, 0.0017041073665144829, 0.00042880328659935255, 0.0],
        },
        "q8.xy.x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
        },
        "q8.xy.-x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -0.00042880328659935255, -0.0017041073665144866, -0.0037928825339620005, -0.006641030609288109, -0.010174786053405199, -0.014302626456506935, -0.018917642920407776, -0.023900308942849263, -0.029121576091124177, -0.0344462162886976, -0.03973632415135715, -0.04485488866422577, -0.04966934169507831, -0.054054991439331485, -0.05789825187228494, -0.061099584567497, -0.06357607668974433, -0.06526358839390214, -0.06611841401324188, -0.0661184140132419, -0.06526358839390214, -0.06357607668974433, -0.06109958456749701, -0.05789825187228496, -0.054054991439331485, -0.049669341695078285, -0.04485488866422578, -0.03973632415135717, -0.0344462162886976, -0.0291215760911242, -0.023900308942849283, -0.018917642920407794, -0.014302626456506947, -0.010174786053405202, -0.006641030609288109, -0.0037928825339619966, -0.0017041073665144829, -0.00042880328659935255, 0.0],
        },
        "q8.xy.-x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 5.251325723977622e-20, 2.0869296318053915e-19, 4.644941454758466e-19, 8.132916878704279e-19, 1.2460519172311808e-18, 1.751566570936147e-18, 2.316743084988997e-18, 2.9269436845493212e-18, 3.566364494612131e-18, 4.218444852069094e-18, 4.86629621818412e-18, 5.4931395828754984e-18, 6.082740032263383e-18, 6.619827224411488e-18, 7.0904908831621e-18, 7.482541066981822e-18, 7.785823882044205e-18, 7.992484462746261e-18, 8.097170408601617e-18, 8.097170408601619e-18, 7.992484462746261e-18, 7.785823882044205e-18, 7.482541066981824e-18, 7.090490883162102e-18, 6.619827224411488e-18, 6.082740032263379e-18, 5.4931395828755e-18, 4.866296218184123e-18, 4.218444852069094e-18, 3.566364494612134e-18, 2.9269436845493235e-18, 2.3167430849889993e-18, 1.7515665709361485e-18, 1.2460519172311812e-18, 8.132916878704279e-19, 4.644941454758461e-19, 2.086929631805387e-19, 5.251325723977622e-20, 0.0],
        },
        "q8.xy.y180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 5.251325723977622e-20, 2.0869296318053915e-19, 4.644941454758466e-19, 8.132916878704279e-19, 1.2460519172311808e-18, 1.751566570936147e-18, 2.316743084988997e-18, 2.9269436845493212e-18, 3.566364494612131e-18, 4.218444852069094e-18, 4.86629621818412e-18, 5.4931395828754984e-18, 6.082740032263383e-18, 6.619827224411488e-18, 7.0904908831621e-18, 7.482541066981822e-18, 7.785823882044205e-18, 7.992484462746261e-18, 8.097170408601617e-18, 8.097170408601619e-18, 7.992484462746261e-18, 7.785823882044205e-18, 7.482541066981824e-18, 7.090490883162102e-18, 6.619827224411488e-18, 6.082740032263379e-18, 5.4931395828755e-18, 4.866296218184123e-18, 4.218444852069094e-18, 3.566364494612134e-18, 2.9269436845493235e-18, 2.3167430849889993e-18, 1.7515665709361485e-18, 1.2460519172311812e-18, 8.132916878704279e-19, 4.644941454758461e-19, 2.086929631805387e-19, 5.251325723977622e-20, 0.0],
        },
        "q8.xy.y180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0008576065731987051, 0.003408214733028973, 0.007585765067924001, 0.013282061218576217, 0.020349572106810397, 0.02860525291301387, 0.03783528584081555, 0.047800617885698525, 0.058243152182248355, 0.0688924325773952, 0.0794726483027143, 0.08970977732845153, 0.09933868339015663, 0.10810998287866297, 0.11579650374456989, 0.122199169134994, 0.12715215337948865, 0.1305271767878043, 0.13223682802648376, 0.1322368280264838, 0.1305271767878043, 0.12715215337948865, 0.12219916913499403, 0.11579650374456991, 0.10810998287866297, 0.09933868339015657, 0.08970977732845156, 0.07947264830271435, 0.0688924325773952, 0.0582431521822484, 0.04780061788569857, 0.03783528584081559, 0.028605252913013895, 0.020349572106810404, 0.013282061218576217, 0.007585765067923993, 0.0034082147330289658, 0.0008576065731987051, 0.0],
        },
        "q8.xy.y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 2.625662861988811e-20, 1.0434648159026957e-19, 2.322470727379233e-19, 4.0664584393521396e-19, 6.230259586155904e-19, 8.757832854680735e-19, 1.1583715424944985e-18, 1.4634718422746606e-18, 1.7831822473060655e-18, 2.109222426034547e-18, 2.43314810909206e-18, 2.7465697914377492e-18, 3.0413700161316915e-18, 3.309913612205744e-18, 3.54524544158105e-18, 3.741270533490911e-18, 3.892911941022102e-18, 3.996242231373131e-18, 4.048585204300809e-18, 4.0485852043008094e-18, 3.996242231373131e-18, 3.892911941022102e-18, 3.741270533490912e-18, 3.545245441581051e-18, 3.309913612205744e-18, 3.0413700161316896e-18, 2.74656979143775e-18, 2.4331481090920613e-18, 2.109222426034547e-18, 1.783182247306067e-18, 1.4634718422746618e-18, 1.1583715424944996e-18, 8.757832854680742e-19, 6.230259586155906e-19, 4.0664584393521396e-19, 2.3224707273792306e-19, 1.0434648159026935e-19, 2.625662861988811e-20, 0.0],
        },
        "q8.xy.y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.00042880328659935255, 0.0017041073665144866, 0.0037928825339620005, 0.006641030609288109, 0.010174786053405199, 0.014302626456506935, 0.018917642920407776, 0.023900308942849263, 0.029121576091124177, 0.0344462162886976, 0.03973632415135715, 0.04485488866422577, 0.04966934169507831, 0.054054991439331485, 0.05789825187228494, 0.061099584567497, 0.06357607668974433, 0.06526358839390214, 0.06611841401324188, 0.0661184140132419, 0.06526358839390214, 0.06357607668974433, 0.06109958456749701, 0.05789825187228496, 0.054054991439331485, 0.049669341695078285, 0.04485488866422578, 0.03973632415135717, 0.0344462162886976, 0.0291215760911242, 0.023900308942849283, 0.018917642920407794, 0.014302626456506947, 0.010174786053405202, 0.006641030609288109, 0.0037928825339619966, 0.0017041073665144829, 0.00042880328659935255, 0.0],
        },
        "q8.xy.-y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 2.625662861988811e-20, 1.0434648159026957e-19, 2.322470727379233e-19, 4.0664584393521396e-19, 6.230259586155904e-19, 8.757832854680735e-19, 1.1583715424944985e-18, 1.4634718422746606e-18, 1.7831822473060655e-18, 2.109222426034547e-18, 2.43314810909206e-18, 2.7465697914377492e-18, 3.0413700161316915e-18, 3.309913612205744e-18, 3.54524544158105e-18, 3.741270533490911e-18, 3.892911941022102e-18, 3.996242231373131e-18, 4.048585204300809e-18, 4.0485852043008094e-18, 3.996242231373131e-18, 3.892911941022102e-18, 3.741270533490912e-18, 3.545245441581051e-18, 3.309913612205744e-18, 3.0413700161316896e-18, 2.74656979143775e-18, 2.4331481090920613e-18, 2.109222426034547e-18, 1.783182247306067e-18, 1.4634718422746618e-18, 1.1583715424944996e-18, 8.757832854680742e-19, 6.230259586155906e-19, 4.0664584393521396e-19, 2.3224707273792306e-19, 1.0434648159026935e-19, 2.625662861988811e-20, 0.0],
        },
        "q8.xy.-y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.00042880328659935255, -0.0017041073665144866, -0.0037928825339620005, -0.006641030609288109, -0.010174786053405199, -0.014302626456506935, -0.018917642920407776, -0.023900308942849263, -0.029121576091124177, -0.0344462162886976, -0.03973632415135715, -0.04485488866422577, -0.04966934169507831, -0.054054991439331485, -0.05789825187228494, -0.061099584567497, -0.06357607668974433, -0.06526358839390214, -0.06611841401324188, -0.0661184140132419, -0.06526358839390214, -0.06357607668974433, -0.06109958456749701, -0.05789825187228496, -0.054054991439331485, -0.049669341695078285, -0.04485488866422578, -0.03973632415135717, -0.0344462162886976, -0.0291215760911242, -0.023900308942849283, -0.018917642920407794, -0.014302626456506947, -0.010174786053405202, -0.006641030609288109, -0.0037928825339619966, -0.0017041073665144829, -0.00042880328659935255, 0.0],
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
            "samples": [0.0, 0.0009556910616820674, 0.0037980123502321136, 0.008453349237279348, 0.014801130942785182, 0.022676953254913295, 0.03187683651275862, 0.04216250857241926, 0.05326757593036487, 0.06490442317524811, 0.07677166207598103, 0.08856193737860832, 0.09996988714593863, 0.11070005147131827, 0.12047452473501581, 0.12904015321379603, 0.13617509162937613, 0.14169454882460322, 0.14545557375735835] + [0.1473607578574586] * 2 + [0.14545557375735835, 0.14169454882460325, 0.13617509162937616, 0.12904015321379608, 0.12047452473501581, 0.11070005147131823, 0.09996988714593866, 0.08856193737860835, 0.07677166207598103, 0.06490442317524817, 0.05326757593036492, 0.042162508572419294, 0.03187683651275864, 0.022676953254913302, 0.014801130942785182, 0.00845334923727934, 0.0037980123502321054, 0.0009556910616820674, 0.0],
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
            "samples": [0.0, 0.0004778455308410337, 0.0018990061751160568, 0.004226674618639674, 0.007400565471392591, 0.011338476627456648, 0.01593841825637931, 0.02108125428620963, 0.026633787965182436, 0.032452211587624055, 0.038385831037990516, 0.04428096868930416, 0.049984943572969315, 0.055350025735659135, 0.060237262367507906, 0.06452007660689801, 0.06808754581468807, 0.07084727441230161, 0.07272778687867917] + [0.0736803789287293] * 2 + [0.07272778687867917, 0.07084727441230163, 0.06808754581468808, 0.06452007660689804, 0.060237262367507906, 0.055350025735659114, 0.04998494357296933, 0.04428096868930417, 0.038385831037990516, 0.03245221158762408, 0.02663378796518246, 0.021081254286209647, 0.01593841825637932, 0.011338476627456651, 0.007400565471392591, 0.00422667461863967, 0.0018990061751160527, 0.0004778455308410337, 0.0],
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
            "samples": [0.0, -0.0004778455308410337, -0.0018990061751160568, -0.004226674618639674, -0.007400565471392591, -0.011338476627456648, -0.01593841825637931, -0.02108125428620963, -0.026633787965182436, -0.032452211587624055, -0.038385831037990516, -0.04428096868930416, -0.049984943572969315, -0.055350025735659135, -0.060237262367507906, -0.06452007660689801, -0.06808754581468807, -0.07084727441230161, -0.07272778687867917] + [-0.0736803789287293] * 2 + [-0.07272778687867917, -0.07084727441230163, -0.06808754581468808, -0.06452007660689804, -0.060237262367507906, -0.055350025735659114, -0.04998494357296933, -0.04428096868930417, -0.038385831037990516, -0.03245221158762408, -0.02663378796518246, -0.021081254286209647, -0.01593841825637932, -0.011338476627456651, -0.007400565471392591, -0.00422667461863967, -0.0018990061751160527, -0.0004778455308410337, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.xy.-x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 5.851919998313397e-20, 2.325611833916937e-19, 5.176183542754436e-19, 9.06307881642136e-19, 1.388562910902186e-18, 1.951893290114666e-18, 2.5817090583618042e-18, 3.2616983180729967e-18, 3.974249704603644e-18, 4.700908511328621e-18, 5.422854656850051e-18, 6.1213901152197934e-18, 6.778423184989859e-18, 7.376937054776786e-18, 7.901430529737967e-18, 8.33831950437565e-18, 8.676288783733935e-18, 8.906585141004532e-18] + [9.023244021503244e-18] * 2 + [8.906585141004532e-18, 8.676288783733937e-18, 8.338319504375653e-18, 7.901430529737971e-18, 7.376937054776786e-18, 6.7784231849898556e-18, 6.121390115219795e-18, 5.4228546568500524e-18, 4.700908511328621e-18, 3.974249704603648e-18, 3.261698318073e-18, 2.5817090583618065e-18, 1.9518932901146673e-18, 1.3885629109021864e-18, 9.06307881642136e-19, 5.176183542754431e-19, 2.325611833916932e-19, 5.851919998313397e-20, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.xy.y180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 5.851919998313397e-20, 2.325611833916937e-19, 5.176183542754436e-19, 9.06307881642136e-19, 1.388562910902186e-18, 1.951893290114666e-18, 2.5817090583618042e-18, 3.2616983180729967e-18, 3.974249704603644e-18, 4.700908511328621e-18, 5.422854656850051e-18, 6.1213901152197934e-18, 6.778423184989859e-18, 7.376937054776786e-18, 7.901430529737967e-18, 8.33831950437565e-18, 8.676288783733935e-18, 8.906585141004532e-18] + [9.023244021503244e-18] * 2 + [8.906585141004532e-18, 8.676288783733937e-18, 8.338319504375653e-18, 7.901430529737971e-18, 7.376937054776786e-18, 6.7784231849898556e-18, 6.121390115219795e-18, 5.4228546568500524e-18, 4.700908511328621e-18, 3.974249704603648e-18, 3.261698318073e-18, 2.5817090583618065e-18, 1.9518932901146673e-18, 1.3885629109021864e-18, 9.06307881642136e-19, 5.176183542754431e-19, 2.325611833916932e-19, 5.851919998313397e-20, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.xy.y180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0009556910616820674, 0.0037980123502321136, 0.008453349237279348, 0.014801130942785182, 0.022676953254913295, 0.03187683651275862, 0.04216250857241926, 0.05326757593036487, 0.06490442317524811, 0.07677166207598103, 0.08856193737860832, 0.09996988714593863, 0.11070005147131827, 0.12047452473501581, 0.12904015321379603, 0.13617509162937613, 0.14169454882460322, 0.14545557375735835] + [0.1473607578574586] * 2 + [0.14545557375735835, 0.14169454882460325, 0.13617509162937616, 0.12904015321379608, 0.12047452473501581, 0.11070005147131823, 0.09996988714593866, 0.08856193737860835, 0.07677166207598103, 0.06490442317524817, 0.05326757593036492, 0.042162508572419294, 0.03187683651275864, 0.022676953254913302, 0.014801130942785182, 0.00845334923727934, 0.0037980123502321054, 0.0009556910616820674, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.xy.y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 2.925959999156699e-20, 1.1628059169584686e-19, 2.588091771377218e-19, 4.53153940821068e-19, 6.94281455451093e-19, 9.75946645057333e-19, 1.2908545291809021e-18, 1.6308491590364984e-18, 1.987124852301822e-18, 2.3504542556643105e-18, 2.7114273284250255e-18, 3.0606950576098967e-18, 3.3892115924949293e-18, 3.688468527388393e-18, 3.9507152648689834e-18, 4.169159752187825e-18, 4.3381443918669676e-18, 4.453292570502266e-18] + [4.511622010751622e-18] * 2 + [4.453292570502266e-18, 4.338144391866968e-18, 4.1691597521878265e-18, 3.950715264868986e-18, 3.688468527388393e-18, 3.3892115924949278e-18, 3.0606950576098975e-18, 2.7114273284250262e-18, 2.3504542556643105e-18, 1.987124852301824e-18, 1.6308491590365e-18, 1.2908545291809033e-18, 9.759466450573337e-19, 6.942814554510932e-19, 4.53153940821068e-19, 2.5880917713772153e-19, 1.162805916958466e-19, 2.925959999156699e-20, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.xy.y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0004778455308410337, 0.0018990061751160568, 0.004226674618639674, 0.007400565471392591, 0.011338476627456648, 0.01593841825637931, 0.02108125428620963, 0.026633787965182436, 0.032452211587624055, 0.038385831037990516, 0.04428096868930416, 0.049984943572969315, 0.055350025735659135, 0.060237262367507906, 0.06452007660689801, 0.06808754581468807, 0.07084727441230161, 0.07272778687867917] + [0.0736803789287293] * 2 + [0.07272778687867917, 0.07084727441230163, 0.06808754581468808, 0.06452007660689804, 0.060237262367507906, 0.055350025735659114, 0.04998494357296933, 0.04428096868930417, 0.038385831037990516, 0.03245221158762408, 0.02663378796518246, 0.021081254286209647, 0.01593841825637932, 0.011338476627456651, 0.007400565471392591, 0.00422667461863967, 0.0018990061751160527, 0.0004778455308410337, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.xy.-y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 2.925959999156699e-20, 1.1628059169584686e-19, 2.588091771377218e-19, 4.53153940821068e-19, 6.94281455451093e-19, 9.75946645057333e-19, 1.2908545291809021e-18, 1.6308491590364984e-18, 1.987124852301822e-18, 2.3504542556643105e-18, 2.7114273284250255e-18, 3.0606950576098967e-18, 3.3892115924949293e-18, 3.688468527388393e-18, 3.9507152648689834e-18, 4.169159752187825e-18, 4.3381443918669676e-18, 4.453292570502266e-18] + [4.511622010751622e-18] * 2 + [4.453292570502266e-18, 4.338144391866968e-18, 4.1691597521878265e-18, 3.950715264868986e-18, 3.688468527388393e-18, 3.3892115924949278e-18, 3.0606950576098975e-18, 2.7114273284250262e-18, 2.3504542556643105e-18, 1.987124852301824e-18, 1.6308491590365e-18, 1.2908545291809033e-18, 9.759466450573337e-19, 6.942814554510932e-19, 4.53153940821068e-19, 2.5880917713772153e-19, 1.162805916958466e-19, 2.925959999156699e-20, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.xy.-y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.0004778455308410337, -0.0018990061751160568, -0.004226674618639674, -0.007400565471392591, -0.011338476627456648, -0.01593841825637931, -0.02108125428620963, -0.026633787965182436, -0.032452211587624055, -0.038385831037990516, -0.04428096868930416, -0.049984943572969315, -0.055350025735659135, -0.060237262367507906, -0.06452007660689801, -0.06808754581468807, -0.07084727441230161, -0.07272778687867917] + [-0.0736803789287293] * 2 + [-0.07272778687867917, -0.07084727441230163, -0.06808754581468808, -0.06452007660689804, -0.060237262367507906, -0.055350025735659114, -0.04998494357296933, -0.04428096868930417, -0.038385831037990516, -0.03245221158762408, -0.02663378796518246, -0.021081254286209647, -0.01593841825637932, -0.011338476627456651, -0.007400565471392591, -0.00422667461863967, -0.0018990061751160527, -0.0004778455308410337, 0.0],
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
            "samples": [0.0, 0.0007493652082608129, 0.0029780526677727235, 0.006628340544010013, 0.011605688298386123, 0.017781185238543162, 0.024994889237570306, 0.0330599691510771, 0.0417675436456952, 0.050892091115892414, 0.06019729057509481, 0.06944214224510536, 0.07838720932376797, 0.0868008192723727, 0.09446506401271659, 0.10118144363186725, 0.10677600742564054, 0.11110385913046684, 0.114052909660507, 0.11554678015609796, 0.11554678015609797, 0.114052909660507, 0.11110385913046686, 0.10677600742564057, 0.10118144363186728, 0.09446506401271659, 0.08680081927237267, 0.078387209323768, 0.06944214224510539, 0.06019729057509481, 0.050892091115892456, 0.041767543645695245, 0.033059969151077125, 0.024994889237570324, 0.01778118523854317, 0.011605688298386123, 0.006628340544010007, 0.002978052667772717, 0.0007493652082608129, 0.0],
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
            "samples": [0.0, 0.00037468260413040644, 0.0014890263338863618, 0.0033141702720050066, 0.005802844149193061, 0.008890592619271581, 0.012497444618785153, 0.01652998457553855, 0.0208837718228476, 0.025446045557946207, 0.030098645287547406, 0.03472107112255268, 0.039193604661883985, 0.04340040963618635, 0.047232532006358297, 0.050590721815933624, 0.05338800371282027, 0.05555192956523342, 0.0570264548302535, 0.05777339007804898, 0.057773390078048985, 0.0570264548302535, 0.05555192956523343, 0.053388003712820285, 0.05059072181593364, 0.047232532006358297, 0.043400409636186334, 0.039193604661884, 0.034721071122552696, 0.030098645287547406, 0.025446045557946228, 0.020883771822847622, 0.016529984575538562, 0.012497444618785162, 0.008890592619271585, 0.005802844149193061, 0.0033141702720050036, 0.0014890263338863585, 0.00037468260413040644, 0.0],
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
            "samples": [0.0, -0.00037468260413040644, -0.0014890263338863618, -0.0033141702720050066, -0.005802844149193061, -0.008890592619271581, -0.012497444618785153, -0.01652998457553855, -0.0208837718228476, -0.025446045557946207, -0.030098645287547406, -0.03472107112255268, -0.039193604661883985, -0.04340040963618635, -0.047232532006358297, -0.050590721815933624, -0.05338800371282027, -0.05555192956523342, -0.0570264548302535, -0.05777339007804898, -0.057773390078048985, -0.0570264548302535, -0.05555192956523343, -0.053388003712820285, -0.05059072181593364, -0.047232532006358297, -0.043400409636186334, -0.039193604661884, -0.034721071122552696, -0.030098645287547406, -0.025446045557946228, -0.020883771822847622, -0.016529984575538562, -0.012497444618785162, -0.008890592619271585, -0.005802844149193061, -0.0033141702720050036, -0.0014890263338863585, -0.00037468260413040644, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.xy.-x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 4.588538518444971e-20, 1.823531333640051e-19, 4.0586880154402444e-19, 7.106434513260228e-19, 1.0887835793714024e-18, 1.5304955549916552e-18, 2.02433927003884e-18, 2.5575244316974e-18, 3.1162418243496547e-18, 3.6860209610066494e-18, 4.252104861320174e-18, 4.7998322496223e-18, 5.315017274263956e-18, 5.78431691372116e-18, 6.195576553843728e-18, 6.538144785977236e-18, 6.8031492728522326e-18, 6.983726537459107e-18] + [7.075199723497414e-18] * 2 + [6.983726537459107e-18, 6.803149272852233e-18, 6.538144785977237e-18, 6.19557655384373e-18, 5.78431691372116e-18, 5.3150172742639535e-18, 4.799832249622302e-18, 4.2521048613201755e-18, 3.6860209610066494e-18, 3.1162418243496574e-18, 2.5575244316974026e-18, 2.024339270038842e-18, 1.5304955549916562e-18, 1.088783579371403e-18, 7.106434513260228e-19, 4.0586880154402406e-19, 1.8235313336400469e-19, 4.588538518444971e-20, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.xy.y180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 4.588538518444971e-20, 1.823531333640051e-19, 4.0586880154402444e-19, 7.106434513260228e-19, 1.0887835793714024e-18, 1.5304955549916552e-18, 2.02433927003884e-18, 2.5575244316974e-18, 3.1162418243496547e-18, 3.6860209610066494e-18, 4.252104861320174e-18, 4.7998322496223e-18, 5.315017274263956e-18, 5.78431691372116e-18, 6.195576553843728e-18, 6.538144785977236e-18, 6.8031492728522326e-18, 6.983726537459107e-18] + [7.075199723497414e-18] * 2 + [6.983726537459107e-18, 6.803149272852233e-18, 6.538144785977237e-18, 6.19557655384373e-18, 5.78431691372116e-18, 5.3150172742639535e-18, 4.799832249622302e-18, 4.2521048613201755e-18, 3.6860209610066494e-18, 3.1162418243496574e-18, 2.5575244316974026e-18, 2.024339270038842e-18, 1.5304955549916562e-18, 1.088783579371403e-18, 7.106434513260228e-19, 4.0586880154402406e-19, 1.8235313336400469e-19, 4.588538518444971e-20, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.xy.y180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0007493652082608129, 0.0029780526677727235, 0.006628340544010013, 0.011605688298386123, 0.017781185238543162, 0.024994889237570306, 0.0330599691510771, 0.0417675436456952, 0.050892091115892414, 0.06019729057509481, 0.06944214224510536, 0.07838720932376797, 0.0868008192723727, 0.09446506401271659, 0.10118144363186725, 0.10677600742564054, 0.11110385913046684, 0.114052909660507, 0.11554678015609796, 0.11554678015609797, 0.114052909660507, 0.11110385913046686, 0.10677600742564057, 0.10118144363186728, 0.09446506401271659, 0.08680081927237267, 0.078387209323768, 0.06944214224510539, 0.06019729057509481, 0.050892091115892456, 0.041767543645695245, 0.033059969151077125, 0.024994889237570324, 0.01778118523854317, 0.011605688298386123, 0.006628340544010007, 0.002978052667772717, 0.0007493652082608129, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.xy.y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 2.2942692592224855e-20, 9.117656668200255e-20, 2.0293440077201222e-19, 3.553217256630114e-19, 5.443917896857012e-19, 7.652477774958276e-19, 1.01216963501942e-18, 1.2787622158487e-18, 1.5581209121748273e-18, 1.8430104805033247e-18, 2.126052430660087e-18, 2.39991612481115e-18, 2.657508637131978e-18, 2.89215845686058e-18, 3.097788276921864e-18, 3.269072392988618e-18, 3.4015746364261163e-18, 3.491863268729554e-18] + [3.537599861748707e-18] * 2 + [3.491863268729554e-18, 3.4015746364261167e-18, 3.2690723929886186e-18, 3.097788276921865e-18, 2.89215845686058e-18, 2.6575086371319767e-18, 2.399916124811151e-18, 2.1260524306600877e-18, 1.8430104805033247e-18, 1.5581209121748287e-18, 1.2787622158487013e-18, 1.012169635019421e-18, 7.652477774958281e-19, 5.443917896857015e-19, 3.553217256630114e-19, 2.0293440077201203e-19, 9.117656668200234e-20, 2.2942692592224855e-20, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.xy.y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.00037468260413040644, 0.0014890263338863618, 0.0033141702720050066, 0.005802844149193061, 0.008890592619271581, 0.012497444618785153, 0.01652998457553855, 0.0208837718228476, 0.025446045557946207, 0.030098645287547406, 0.03472107112255268, 0.039193604661883985, 0.04340040963618635, 0.047232532006358297, 0.050590721815933624, 0.05338800371282027, 0.05555192956523342, 0.0570264548302535, 0.05777339007804898, 0.057773390078048985, 0.0570264548302535, 0.05555192956523343, 0.053388003712820285, 0.05059072181593364, 0.047232532006358297, 0.043400409636186334, 0.039193604661884, 0.034721071122552696, 0.030098645287547406, 0.025446045557946228, 0.020883771822847622, 0.016529984575538562, 0.012497444618785162, 0.008890592619271585, 0.005802844149193061, 0.0033141702720050036, 0.0014890263338863585, 0.00037468260413040644, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.xy.-y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 2.2942692592224855e-20, 9.117656668200255e-20, 2.0293440077201222e-19, 3.553217256630114e-19, 5.443917896857012e-19, 7.652477774958276e-19, 1.01216963501942e-18, 1.2787622158487e-18, 1.5581209121748273e-18, 1.8430104805033247e-18, 2.126052430660087e-18, 2.39991612481115e-18, 2.657508637131978e-18, 2.89215845686058e-18, 3.097788276921864e-18, 3.269072392988618e-18, 3.4015746364261163e-18, 3.491863268729554e-18] + [3.537599861748707e-18] * 2 + [3.491863268729554e-18, 3.4015746364261167e-18, 3.2690723929886186e-18, 3.097788276921865e-18, 2.89215845686058e-18, 2.6575086371319767e-18, 2.399916124811151e-18, 2.1260524306600877e-18, 1.8430104805033247e-18, 1.5581209121748287e-18, 1.2787622158487013e-18, 1.012169635019421e-18, 7.652477774958281e-19, 5.443917896857015e-19, 3.553217256630114e-19, 2.0293440077201203e-19, 9.117656668200234e-20, 2.2942692592224855e-20, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.xy.-y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.00037468260413040644, -0.0014890263338863618, -0.0033141702720050066, -0.005802844149193061, -0.008890592619271581, -0.012497444618785153, -0.01652998457553855, -0.0208837718228476, -0.025446045557946207, -0.030098645287547406, -0.03472107112255268, -0.039193604661883985, -0.04340040963618635, -0.047232532006358297, -0.050590721815933624, -0.05338800371282027, -0.05555192956523342, -0.0570264548302535, -0.05777339007804898, -0.057773390078048985, -0.0570264548302535, -0.05555192956523343, -0.053388003712820285, -0.05059072181593364, -0.047232532006358297, -0.043400409636186334, -0.039193604661884, -0.034721071122552696, -0.030098645287547406, -0.025446045557946228, -0.020883771822847622, -0.016529984575538562, -0.012497444618785162, -0.008890592619271585, -0.005802844149193061, -0.0033141702720050036, -0.0014890263338863585, -0.00037468260413040644, 0.0],
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
            "samples": [0.0, 0.001080628881442259, 0.004294527805367907, 0.009558458477830673, 0.016736087859429313, 0.025641519119415625, 0.036044106265963695, 0.04767442775620553, 0.06023126437267054, 0.07338940064279505, 0.08680804774883369, 0.10013966977923097, 0.11303898472617849, 0.12517190710824852, 0.13622420060887627, 0.1459096166318981, 0.15397730798983267, 0.16021832571427266, 0.16447103072441085, 0.16662528019432776, 0.1666252801943278, 0.16447103072441085, 0.1602183257142727, 0.1539773079898327, 0.14590961663189814, 0.13622420060887627, 0.12517190710824846, 0.11303898472617853, 0.10013966977923101, 0.08680804774883369, 0.0733894006427951, 0.060231264372670595, 0.04767442775620556, 0.03604410626596372, 0.02564151911941563, 0.016736087859429313, 0.009558458477830665, 0.004294527805367898, 0.001080628881442259, 0.0],
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
            "samples": [0.0, 0.0005403144407211295, 0.0021472639026839536, 0.004779229238915337, 0.008368043929714656, 0.012820759559707812, 0.018022053132981847, 0.023837213878102764, 0.03011563218633527, 0.03669470032139752, 0.043404023874416844, 0.050069834889615486, 0.056519492363089244, 0.06258595355412426, 0.06811210030443814, 0.07295480831594905, 0.07698865399491633, 0.08010916285713633, 0.08223551536220543, 0.08331264009716388, 0.0833126400971639, 0.08223551536220543, 0.08010916285713635, 0.07698865399491635, 0.07295480831594907, 0.06811210030443814, 0.06258595355412423, 0.056519492363089265, 0.05006983488961551, 0.043404023874416844, 0.03669470032139755, 0.030115632186335298, 0.02383721387810278, 0.01802205313298186, 0.012820759559707816, 0.008368043929714656, 0.004779229238915332, 0.002147263902683949, 0.0005403144407211295, 0.0],
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
            "samples": [0.0, -0.0005403144407211295, -0.0021472639026839536, -0.004779229238915337, -0.008368043929714656, -0.012820759559707812, -0.018022053132981847, -0.023837213878102764, -0.03011563218633527, -0.03669470032139752, -0.043404023874416844, -0.050069834889615486, -0.056519492363089244, -0.06258595355412426, -0.06811210030443814, -0.07295480831594905, -0.07698865399491633, -0.08010916285713633, -0.08223551536220543, -0.08331264009716388, -0.0833126400971639, -0.08223551536220543, -0.08010916285713635, -0.07698865399491635, -0.07295480831594907, -0.06811210030443814, -0.06258595355412423, -0.056519492363089265, -0.05006983488961551, -0.043404023874416844, -0.03669470032139755, -0.030115632186335298, -0.02383721387810278, -0.01802205313298186, -0.012820759559707816, -0.008368043929714656, -0.004779229238915332, -0.002147263902683949, -0.0005403144407211295, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q3.xy.-x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 6.616943503622235e-20, 2.6296398653465575e-19, 5.852867789829108e-19, 1.0247898213649492e-18, 1.5700902157434003e-18, 2.207064968336975e-18, 2.9192167676409414e-18, 3.6881012561294494e-18, 4.493804729427083e-18, 5.3154598907919885e-18, 6.131786303140407e-18, 6.921641541189052e-18, 7.664568769164318e-18, 8.341326562103362e-18, 8.934387248653571e-18, 9.428390868553737e-18, 9.810542987536604e-18, 1.0070946066455787e-17, 1.0202855802350718e-17, 1.020285580235072e-17, 1.0070946066455787e-17, 9.810542987536606e-18, 9.428390868553739e-18, 8.934387248653573e-18, 8.341326562103362e-18, 7.664568769164315e-18, 6.921641541189054e-18, 6.13178630314041e-18, 5.3154598907919885e-18, 4.4938047294270864e-18, 3.6881012561294525e-18, 2.9192167676409437e-18, 2.2070649683369765e-18, 1.5700902157434007e-18, 1.0247898213649492e-18, 5.852867789829103e-19, 2.6296398653465517e-19, 6.616943503622235e-20, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q3.xy.y180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 6.616943503622235e-20, 2.6296398653465575e-19, 5.852867789829108e-19, 1.0247898213649492e-18, 1.5700902157434003e-18, 2.207064968336975e-18, 2.9192167676409414e-18, 3.6881012561294494e-18, 4.493804729427083e-18, 5.3154598907919885e-18, 6.131786303140407e-18, 6.921641541189052e-18, 7.664568769164318e-18, 8.341326562103362e-18, 8.934387248653571e-18, 9.428390868553737e-18, 9.810542987536604e-18, 1.0070946066455787e-17, 1.0202855802350718e-17, 1.020285580235072e-17, 1.0070946066455787e-17, 9.810542987536606e-18, 9.428390868553739e-18, 8.934387248653573e-18, 8.341326562103362e-18, 7.664568769164315e-18, 6.921641541189054e-18, 6.13178630314041e-18, 5.3154598907919885e-18, 4.4938047294270864e-18, 3.6881012561294525e-18, 2.9192167676409437e-18, 2.2070649683369765e-18, 1.5700902157434007e-18, 1.0247898213649492e-18, 5.852867789829103e-19, 2.6296398653465517e-19, 6.616943503622235e-20, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q3.xy.y180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.001080628881442259, 0.004294527805367907, 0.009558458477830673, 0.016736087859429313, 0.025641519119415625, 0.036044106265963695, 0.04767442775620553, 0.06023126437267054, 0.07338940064279505, 0.08680804774883369, 0.10013966977923097, 0.11303898472617849, 0.12517190710824852, 0.13622420060887627, 0.1459096166318981, 0.15397730798983267, 0.16021832571427266, 0.16447103072441085, 0.16662528019432776, 0.1666252801943278, 0.16447103072441085, 0.1602183257142727, 0.1539773079898327, 0.14590961663189814, 0.13622420060887627, 0.12517190710824846, 0.11303898472617853, 0.10013966977923101, 0.08680804774883369, 0.0733894006427951, 0.060231264372670595, 0.04767442775620556, 0.03604410626596372, 0.02564151911941563, 0.016736087859429313, 0.009558458477830665, 0.004294527805367898, 0.001080628881442259, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q3.xy.y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 3.308471751811118e-20, 1.3148199326732787e-19, 2.926433894914554e-19, 5.123949106824746e-19, 7.850451078717001e-19, 1.1035324841684875e-18, 1.4596083838204707e-18, 1.8440506280647247e-18, 2.2469023647135417e-18, 2.6577299453959943e-18, 3.0658931515702035e-18, 3.460820770594526e-18, 3.832284384582159e-18, 4.170663281051681e-18, 4.467193624326786e-18, 4.7141954342768685e-18, 4.905271493768302e-18, 5.035473033227894e-18, 5.101427901175359e-18, 5.10142790117536e-18, 5.035473033227894e-18, 4.905271493768303e-18, 4.714195434276869e-18, 4.4671936243267864e-18, 4.170663281051681e-18, 3.8322843845821576e-18, 3.460820770594527e-18, 3.065893151570205e-18, 2.6577299453959943e-18, 2.2469023647135432e-18, 1.8440506280647263e-18, 1.4596083838204719e-18, 1.1035324841684883e-18, 7.850451078717003e-19, 5.123949106824746e-19, 2.9264338949145514e-19, 1.3148199326732758e-19, 3.308471751811118e-20, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q3.xy.y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0005403144407211295, 0.0021472639026839536, 0.004779229238915337, 0.008368043929714656, 0.012820759559707812, 0.018022053132981847, 0.023837213878102764, 0.03011563218633527, 0.03669470032139752, 0.043404023874416844, 0.050069834889615486, 0.056519492363089244, 0.06258595355412426, 0.06811210030443814, 0.07295480831594905, 0.07698865399491633, 0.08010916285713633, 0.08223551536220543, 0.08331264009716388, 0.0833126400971639, 0.08223551536220543, 0.08010916285713635, 0.07698865399491635, 0.07295480831594907, 0.06811210030443814, 0.06258595355412423, 0.056519492363089265, 0.05006983488961551, 0.043404023874416844, 0.03669470032139755, 0.030115632186335298, 0.02383721387810278, 0.01802205313298186, 0.012820759559707816, 0.008368043929714656, 0.004779229238915332, 0.002147263902683949, 0.0005403144407211295, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q3.xy.-y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 3.308471751811118e-20, 1.3148199326732787e-19, 2.926433894914554e-19, 5.123949106824746e-19, 7.850451078717001e-19, 1.1035324841684875e-18, 1.4596083838204707e-18, 1.8440506280647247e-18, 2.2469023647135417e-18, 2.6577299453959943e-18, 3.0658931515702035e-18, 3.460820770594526e-18, 3.832284384582159e-18, 4.170663281051681e-18, 4.467193624326786e-18, 4.7141954342768685e-18, 4.905271493768302e-18, 5.035473033227894e-18, 5.101427901175359e-18, 5.10142790117536e-18, 5.035473033227894e-18, 4.905271493768303e-18, 4.714195434276869e-18, 4.4671936243267864e-18, 4.170663281051681e-18, 3.8322843845821576e-18, 3.460820770594527e-18, 3.065893151570205e-18, 2.6577299453959943e-18, 2.2469023647135432e-18, 1.8440506280647263e-18, 1.4596083838204719e-18, 1.1035324841684883e-18, 7.850451078717003e-19, 5.123949106824746e-19, 2.9264338949145514e-19, 1.3148199326732758e-19, 3.308471751811118e-20, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q3.xy.-y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.0005403144407211295, -0.0021472639026839536, -0.004779229238915337, -0.008368043929714656, -0.012820759559707812, -0.018022053132981847, -0.023837213878102764, -0.03011563218633527, -0.03669470032139752, -0.043404023874416844, -0.050069834889615486, -0.056519492363089244, -0.06258595355412426, -0.06811210030443814, -0.07295480831594905, -0.07698865399491633, -0.08010916285713633, -0.08223551536220543, -0.08331264009716388, -0.0833126400971639, -0.08223551536220543, -0.08010916285713635, -0.07698865399491635, -0.07295480831594907, -0.06811210030443814, -0.06258595355412423, -0.056519492363089265, -0.05006983488961551, -0.043404023874416844, -0.03669470032139755, -0.030115632186335298, -0.02383721387810278, -0.01802205313298186, -0.012820759559707816, -0.008368043929714656, -0.004779229238915332, -0.002147263902683949, -0.0005403144407211295, 0.0],
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
            "samples": [0.0, 0.0010441878513468242, 0.0041497074885240475, 0.009236127584183164, 0.01617171252962013, 0.024776834317843235, 0.03482862481459994, 0.04606674792598683, 0.05820014216653334, 0.07091455899878804, 0.0838807017053713, 0.0967627540009839, 0.10922707749780024, 0.1209508527644605, 0.1316304401797739, 0.140989244039413, 0.1487848762393665, 0.1548154340005128, 0.15892472904454438, 0.16100633278833418, 0.1610063327883342, 0.15892472904454438, 0.1548154340005128, 0.14878487623936654, 0.14098924403941301, 0.1316304401797739, 0.12095085276446045, 0.10922707749780027, 0.09676275400098394, 0.0838807017053713, 0.0709145589987881, 0.058200142166533395, 0.04606674792598686, 0.034828624814599966, 0.024776834317843246, 0.01617171252962013, 0.009236127584183155, 0.004149707488524039, 0.0010441878513468242, 0.0],
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
            "samples": [0.0, 0.0005220939256734121, 0.0020748537442620237, 0.004618063792091582, 0.008085856264810065, 0.012388417158921618, 0.01741431240729997, 0.023033373962993414, 0.02910007108326667, 0.03545727949939402, 0.04194035085268565, 0.04838137700049195, 0.05461353874890012, 0.06047542638223025, 0.06581522008988695, 0.0704946220197065, 0.07439243811968325, 0.0774077170002564, 0.07946236452227219, 0.08050316639416709, 0.0805031663941671, 0.07946236452227219, 0.0774077170002564, 0.07439243811968327, 0.07049462201970651, 0.06581522008988695, 0.060475426382230225, 0.05461353874890013, 0.04838137700049197, 0.04194035085268565, 0.03545727949939405, 0.029100071083266697, 0.02303337396299343, 0.017414312407299983, 0.012388417158921623, 0.008085856264810065, 0.004618063792091578, 0.0020748537442620194, 0.0005220939256734121, 0.0],
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
            "samples": [0.0, -0.0005220939256734121, -0.0020748537442620237, -0.004618063792091582, -0.008085856264810065, -0.012388417158921618, -0.01741431240729997, -0.023033373962993414, -0.02910007108326667, -0.03545727949939402, -0.04194035085268565, -0.04838137700049195, -0.05461353874890012, -0.06047542638223025, -0.06581522008988695, -0.0704946220197065, -0.07439243811968325, -0.0774077170002564, -0.07946236452227219, -0.08050316639416709, -0.0805031663941671, -0.07946236452227219, -0.0774077170002564, -0.07439243811968327, -0.07049462201970651, -0.06581522008988695, -0.060475426382230225, -0.05461353874890013, -0.04838137700049197, -0.04194035085268565, -0.03545727949939405, -0.029100071083266697, -0.02303337396299343, -0.017414312407299983, -0.012388417158921623, -0.008085856264810065, -0.004618063792091578, -0.0020748537442620194, -0.0005220939256734121, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q4.xy.-x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 6.393806549302202e-20, 2.5409629966093885e-19, 5.655497041243244e-19, 9.90231799306522e-19, 1.5171435420175506e-18, 2.1326381948951945e-18, 2.820774769734387e-18, 3.5637308907082975e-18, 4.342264384540595e-18, 5.136211642685845e-18, 5.925009848199384e-18, 6.6882295418950474e-18, 7.406103734606968e-18, 8.060039861825862e-18, 8.633101321353608e-18, 9.110446122403764e-18, 9.479711285366816e-18, 9.731333036488084e-18, 9.85879450458435e-18, 9.858794504584352e-18, 9.731333036488084e-18, 9.479711285366816e-18, 9.110446122403765e-18, 8.63310132135361e-18, 8.060039861825862e-18, 7.406103734606965e-18, 6.688229541895049e-18, 5.925009848199387e-18, 5.136211642685845e-18, 4.3422643845405984e-18, 3.563730890708301e-18, 2.820774769734389e-18, 2.1326381948951965e-18, 1.5171435420175513e-18, 9.90231799306522e-19, 5.655497041243239e-19, 2.5409629966093832e-19, 6.393806549302202e-20, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q4.xy.y180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 6.393806549302202e-20, 2.5409629966093885e-19, 5.655497041243244e-19, 9.90231799306522e-19, 1.5171435420175506e-18, 2.1326381948951945e-18, 2.820774769734387e-18, 3.5637308907082975e-18, 4.342264384540595e-18, 5.136211642685845e-18, 5.925009848199384e-18, 6.6882295418950474e-18, 7.406103734606968e-18, 8.060039861825862e-18, 8.633101321353608e-18, 9.110446122403764e-18, 9.479711285366816e-18, 9.731333036488084e-18, 9.85879450458435e-18, 9.858794504584352e-18, 9.731333036488084e-18, 9.479711285366816e-18, 9.110446122403765e-18, 8.63310132135361e-18, 8.060039861825862e-18, 7.406103734606965e-18, 6.688229541895049e-18, 5.925009848199387e-18, 5.136211642685845e-18, 4.3422643845405984e-18, 3.563730890708301e-18, 2.820774769734389e-18, 2.1326381948951965e-18, 1.5171435420175513e-18, 9.90231799306522e-19, 5.655497041243239e-19, 2.5409629966093832e-19, 6.393806549302202e-20, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q4.xy.y180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0010441878513468242, 0.0041497074885240475, 0.009236127584183164, 0.01617171252962013, 0.024776834317843235, 0.03482862481459994, 0.04606674792598683, 0.05820014216653334, 0.07091455899878804, 0.0838807017053713, 0.0967627540009839, 0.10922707749780024, 0.1209508527644605, 0.1316304401797739, 0.140989244039413, 0.1487848762393665, 0.1548154340005128, 0.15892472904454438, 0.16100633278833418, 0.1610063327883342, 0.15892472904454438, 0.1548154340005128, 0.14878487623936654, 0.14098924403941301, 0.1316304401797739, 0.12095085276446045, 0.10922707749780027, 0.09676275400098394, 0.0838807017053713, 0.0709145589987881, 0.058200142166533395, 0.04606674792598686, 0.034828624814599966, 0.024776834317843246, 0.01617171252962013, 0.009236127584183155, 0.004149707488524039, 0.0010441878513468242, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q4.xy.y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 3.196903274651101e-20, 1.2704814983046943e-19, 2.827748520621622e-19, 4.95115899653261e-19, 7.585717710087753e-19, 1.0663190974475973e-18, 1.4103873848671936e-18, 1.7818654453541487e-18, 2.1711321922702977e-18, 2.5681058213429225e-18, 2.962504924099692e-18, 3.3441147709475237e-18, 3.703051867303484e-18, 4.030019930912931e-18, 4.316550660676804e-18, 4.555223061201882e-18, 4.739855642683408e-18, 4.865666518244042e-18, 4.929397252292175e-18, 4.929397252292176e-18, 4.865666518244042e-18, 4.739855642683408e-18, 4.555223061201883e-18, 4.316550660676805e-18, 4.030019930912931e-18, 3.7030518673034826e-18, 3.3441147709475245e-18, 2.9625049240996934e-18, 2.5681058213429225e-18, 2.1711321922702992e-18, 1.7818654453541507e-18, 1.4103873848671945e-18, 1.0663190974475982e-18, 7.585717710087757e-19, 4.95115899653261e-19, 2.8277485206216193e-19, 1.2704814983046916e-19, 3.196903274651101e-20, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q4.xy.y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0005220939256734121, 0.0020748537442620237, 0.004618063792091582, 0.008085856264810065, 0.012388417158921618, 0.01741431240729997, 0.023033373962993414, 0.02910007108326667, 0.03545727949939402, 0.04194035085268565, 0.04838137700049195, 0.05461353874890012, 0.06047542638223025, 0.06581522008988695, 0.0704946220197065, 0.07439243811968325, 0.0774077170002564, 0.07946236452227219, 0.08050316639416709, 0.0805031663941671, 0.07946236452227219, 0.0774077170002564, 0.07439243811968327, 0.07049462201970651, 0.06581522008988695, 0.060475426382230225, 0.05461353874890013, 0.04838137700049197, 0.04194035085268565, 0.03545727949939405, 0.029100071083266697, 0.02303337396299343, 0.017414312407299983, 0.012388417158921623, 0.008085856264810065, 0.004618063792091578, 0.0020748537442620194, 0.0005220939256734121, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q4.xy.-y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 3.196903274651101e-20, 1.2704814983046943e-19, 2.827748520621622e-19, 4.95115899653261e-19, 7.585717710087753e-19, 1.0663190974475973e-18, 1.4103873848671936e-18, 1.7818654453541487e-18, 2.1711321922702977e-18, 2.5681058213429225e-18, 2.962504924099692e-18, 3.3441147709475237e-18, 3.703051867303484e-18, 4.030019930912931e-18, 4.316550660676804e-18, 4.555223061201882e-18, 4.739855642683408e-18, 4.865666518244042e-18, 4.929397252292175e-18, 4.929397252292176e-18, 4.865666518244042e-18, 4.739855642683408e-18, 4.555223061201883e-18, 4.316550660676805e-18, 4.030019930912931e-18, 3.7030518673034826e-18, 3.3441147709475245e-18, 2.9625049240996934e-18, 2.5681058213429225e-18, 2.1711321922702992e-18, 1.7818654453541507e-18, 1.4103873848671945e-18, 1.0663190974475982e-18, 7.585717710087757e-19, 4.95115899653261e-19, 2.8277485206216193e-19, 1.2704814983046916e-19, 3.196903274651101e-20, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q4.xy.-y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.0005220939256734121, -0.0020748537442620237, -0.004618063792091582, -0.008085856264810065, -0.012388417158921618, -0.01741431240729997, -0.023033373962993414, -0.02910007108326667, -0.03545727949939402, -0.04194035085268565, -0.04838137700049195, -0.05461353874890012, -0.06047542638223025, -0.06581522008988695, -0.0704946220197065, -0.07439243811968325, -0.0774077170002564, -0.07946236452227219, -0.08050316639416709, -0.0805031663941671, -0.07946236452227219, -0.0774077170002564, -0.07439243811968327, -0.07049462201970651, -0.06581522008988695, -0.060475426382230225, -0.05461353874890013, -0.04838137700049197, -0.04194035085268565, -0.03545727949939405, -0.029100071083266697, -0.02303337396299343, -0.017414312407299983, -0.012388417158921623, -0.008085856264810065, -0.004618063792091578, -0.0020748537442620194, -0.0005220939256734121, 0.0],
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
            "samples": [0.0, 0.000741300610345739, 0.00294600314496229, 0.006557006966280023, 0.01148078897209983, 0.017589825794814638, 0.024725896589645482, 0.03270418087141174, 0.041318045268015524, 0.050344395216239526, 0.05954945299374817, 0.06869481243929827, 0.0775436135470864, 0.0858666770164821, 0.09344843987553203, 0.10009253844870358, 0.10562689407293598, 0.10990816984462481, 0.112825482970134, 0.11430327657190693, 0.11430327657190695, 0.112825482970134, 0.10990816984462483, 0.105626894072936, 0.10009253844870361, 0.09344843987553203, 0.08586667701648207, 0.07754361354708643, 0.0686948124392983, 0.05954945299374817, 0.050344395216239575, 0.04131804526801556, 0.03270418087141177, 0.024725896589645503, 0.017589825794814645, 0.01148078897209983, 0.006557006966280017, 0.0029460031449622835, 0.000741300610345739, 0.0],
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
            "samples": [0.0, 0.0003706503051728695, 0.001473001572481145, 0.0032785034831400114, 0.005740394486049915, 0.008794912897407319, 0.012362948294822741, 0.01635209043570587, 0.020659022634007762, 0.025172197608119763, 0.029774726496874085, 0.034347406219649136, 0.0387718067735432, 0.04293333850824105, 0.046724219937766015, 0.05004626922435179, 0.05281344703646799, 0.05495408492231241, 0.056412741485067, 0.05715163828595347, 0.057151638285953474, 0.056412741485067, 0.054954084922312414, 0.052813447036468, 0.050046269224351805, 0.046724219937766015, 0.042933338508241034, 0.038771806773543215, 0.03434740621964915, 0.029774726496874085, 0.025172197608119787, 0.02065902263400778, 0.016352090435705884, 0.012362948294822752, 0.008794912897407322, 0.005740394486049915, 0.0032785034831400084, 0.0014730015724811417, 0.0003706503051728695, 0.0],
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
            "samples": [0.0, -0.0003706503051728695, -0.001473001572481145, -0.0032785034831400114, -0.005740394486049915, -0.008794912897407319, -0.012362948294822741, -0.01635209043570587, -0.020659022634007762, -0.025172197608119763, -0.029774726496874085, -0.034347406219649136, -0.0387718067735432, -0.04293333850824105, -0.046724219937766015, -0.05004626922435179, -0.05281344703646799, -0.05495408492231241, -0.056412741485067, -0.05715163828595347, -0.057151638285953474, -0.056412741485067, -0.054954084922312414, -0.052813447036468, -0.050046269224351805, -0.046724219937766015, -0.042933338508241034, -0.038771806773543215, -0.03434740621964915, -0.029774726496874085, -0.025172197608119787, -0.02065902263400778, -0.016352090435705884, -0.012362948294822752, -0.008794912897407322, -0.005740394486049915, -0.0032785034831400084, -0.0014730015724811417, -0.0003706503051728695, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q5.xy.-x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 4.5391570983294425e-20, 1.8039066608780522e-19, 4.0150087966208634e-19, 7.029955733184144e-19, 1.0770661928589647e-18, 1.51402450572789e-18, 2.0025535211455244e-18, 2.5300005942250326e-18, 3.0827051228288527e-18, 3.646352349988473e-18, 4.206344108590721e-18, 4.7481769062379345e-18, 5.25781755808272e-18, 5.722066638944209e-18, 6.128900341486911e-18, 6.467781886514879e-18, 6.729934420018172e-18, 6.908568329081441e-18, 6.999057089292023e-18, 6.999057089292025e-18, 6.908568329081441e-18, 6.7299344200181725e-18, 6.467781886514881e-18, 6.128900341486913e-18, 5.722066638944209e-18, 5.257817558082718e-18, 4.748176906237937e-18, 4.2063441085907224e-18, 3.646352349988473e-18, 3.082705122828856e-18, 2.530000594225035e-18, 2.002553521145526e-18, 1.514024505727891e-18, 1.077066192858965e-18, 7.029955733184144e-19, 4.0150087966208595e-19, 1.8039066608780481e-19, 4.5391570983294425e-20, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q5.xy.y180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 4.5391570983294425e-20, 1.8039066608780522e-19, 4.0150087966208634e-19, 7.029955733184144e-19, 1.0770661928589647e-18, 1.51402450572789e-18, 2.0025535211455244e-18, 2.5300005942250326e-18, 3.0827051228288527e-18, 3.646352349988473e-18, 4.206344108590721e-18, 4.7481769062379345e-18, 5.25781755808272e-18, 5.722066638944209e-18, 6.128900341486911e-18, 6.467781886514879e-18, 6.729934420018172e-18, 6.908568329081441e-18, 6.999057089292023e-18, 6.999057089292025e-18, 6.908568329081441e-18, 6.7299344200181725e-18, 6.467781886514881e-18, 6.128900341486913e-18, 5.722066638944209e-18, 5.257817558082718e-18, 4.748176906237937e-18, 4.2063441085907224e-18, 3.646352349988473e-18, 3.082705122828856e-18, 2.530000594225035e-18, 2.002553521145526e-18, 1.514024505727891e-18, 1.077066192858965e-18, 7.029955733184144e-19, 4.0150087966208595e-19, 1.8039066608780481e-19, 4.5391570983294425e-20, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q5.xy.y180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.000741300610345739, 0.00294600314496229, 0.006557006966280023, 0.01148078897209983, 0.017589825794814638, 0.024725896589645482, 0.03270418087141174, 0.041318045268015524, 0.050344395216239526, 0.05954945299374817, 0.06869481243929827, 0.0775436135470864, 0.0858666770164821, 0.09344843987553203, 0.10009253844870358, 0.10562689407293598, 0.10990816984462481, 0.112825482970134, 0.11430327657190693, 0.11430327657190695, 0.112825482970134, 0.10990816984462483, 0.105626894072936, 0.10009253844870361, 0.09344843987553203, 0.08586667701648207, 0.07754361354708643, 0.0686948124392983, 0.05954945299374817, 0.050344395216239575, 0.04131804526801556, 0.03270418087141177, 0.024725896589645503, 0.017589825794814645, 0.01148078897209983, 0.006557006966280017, 0.0029460031449622835, 0.000741300610345739, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q5.xy.y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 2.2695785491647213e-20, 9.019533304390261e-20, 2.0075043983104317e-19, 3.514977866592072e-19, 5.385330964294823e-19, 7.57012252863945e-19, 1.0012767605727622e-18, 1.2650002971125163e-18, 1.5413525614144264e-18, 1.8231761749942366e-18, 2.1031720542953605e-18, 2.3740884531189672e-18, 2.62890877904136e-18, 2.8610333194721045e-18, 3.0644501707434555e-18, 3.2338909432574396e-18, 3.364967210009086e-18, 3.4542841645407204e-18, 3.499528544646012e-18, 3.4995285446460125e-18, 3.4542841645407204e-18, 3.3649672100090862e-18, 3.2338909432574403e-18, 3.0644501707434566e-18, 2.8610333194721045e-18, 2.628908779041359e-18, 2.3740884531189684e-18, 2.1031720542953612e-18, 1.8231761749942366e-18, 1.541352561414428e-18, 1.2650002971125175e-18, 1.001276760572763e-18, 7.570122528639455e-19, 5.385330964294825e-19, 3.514977866592072e-19, 2.0075043983104298e-19, 9.019533304390241e-20, 2.2695785491647213e-20, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q5.xy.y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0003706503051728695, 0.001473001572481145, 0.0032785034831400114, 0.005740394486049915, 0.008794912897407319, 0.012362948294822741, 0.01635209043570587, 0.020659022634007762, 0.025172197608119763, 0.029774726496874085, 0.034347406219649136, 0.0387718067735432, 0.04293333850824105, 0.046724219937766015, 0.05004626922435179, 0.05281344703646799, 0.05495408492231241, 0.056412741485067, 0.05715163828595347, 0.057151638285953474, 0.056412741485067, 0.054954084922312414, 0.052813447036468, 0.050046269224351805, 0.046724219937766015, 0.042933338508241034, 0.038771806773543215, 0.03434740621964915, 0.029774726496874085, 0.025172197608119787, 0.02065902263400778, 0.016352090435705884, 0.012362948294822752, 0.008794912897407322, 0.005740394486049915, 0.0032785034831400084, 0.0014730015724811417, 0.0003706503051728695, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q5.xy.-y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 2.2695785491647213e-20, 9.019533304390261e-20, 2.0075043983104317e-19, 3.514977866592072e-19, 5.385330964294823e-19, 7.57012252863945e-19, 1.0012767605727622e-18, 1.2650002971125163e-18, 1.5413525614144264e-18, 1.8231761749942366e-18, 2.1031720542953605e-18, 2.3740884531189672e-18, 2.62890877904136e-18, 2.8610333194721045e-18, 3.0644501707434555e-18, 3.2338909432574396e-18, 3.364967210009086e-18, 3.4542841645407204e-18, 3.499528544646012e-18, 3.4995285446460125e-18, 3.4542841645407204e-18, 3.3649672100090862e-18, 3.2338909432574403e-18, 3.0644501707434566e-18, 2.8610333194721045e-18, 2.628908779041359e-18, 2.3740884531189684e-18, 2.1031720542953612e-18, 1.8231761749942366e-18, 1.541352561414428e-18, 1.2650002971125175e-18, 1.001276760572763e-18, 7.570122528639455e-19, 5.385330964294825e-19, 3.514977866592072e-19, 2.0075043983104298e-19, 9.019533304390241e-20, 2.2695785491647213e-20, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q5.xy.-y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.0003706503051728695, -0.001473001572481145, -0.0032785034831400114, -0.005740394486049915, -0.008794912897407319, -0.012362948294822741, -0.01635209043570587, -0.020659022634007762, -0.025172197608119763, -0.029774726496874085, -0.034347406219649136, -0.0387718067735432, -0.04293333850824105, -0.046724219937766015, -0.05004626922435179, -0.05281344703646799, -0.05495408492231241, -0.056412741485067, -0.05715163828595347, -0.057151638285953474, -0.056412741485067, -0.054954084922312414, -0.052813447036468, -0.050046269224351805, -0.046724219937766015, -0.042933338508241034, -0.038771806773543215, -0.03434740621964915, -0.029774726496874085, -0.025172197608119787, -0.02065902263400778, -0.016352090435705884, -0.012362948294822752, -0.008794912897407322, -0.005740394486049915, -0.0032785034831400084, -0.0014730015724811417, -0.0003706503051728695, 0.0],
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
            "samples": [0.0, 0.000932688204479085, 0.0037065966833388963, 0.008249882664044025, 0.014444877426172512, 0.02213113385946622, 0.03110958195970752, 0.04114768463726193, 0.051985460305553434, 0.06334221626759488, 0.07492381850939873, 0.08643030961643793, 0.09756367751312184, 0.10803557381901534, 0.11757478192042971, 0.1259342413382538, 0.13289744646458787, 0.13828405394426324, 0.14195455347301097, 0.14381388104106116, 0.1438138810410612, 0.14195455347301097, 0.13828405394426327, 0.1328974464645879, 0.12593424133825382, 0.11757478192042971, 0.10803557381901528, 0.09756367751312187, 0.08643030961643795, 0.07492381850939873, 0.06334221626759494, 0.05198546030555348, 0.04114768463726196, 0.031109581959707543, 0.022131133859466228, 0.014444877426172512, 0.008249882664044018, 0.0037065966833388884, 0.000932688204479085, 0.0],
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
            "samples": [0.0, 0.0004663441022395425, 0.0018532983416694481, 0.004124941332022012, 0.007222438713086256, 0.01106556692973311, 0.01555479097985376, 0.020573842318630964, 0.025992730152776717, 0.03167110813379744, 0.03746190925469937, 0.04321515480821896, 0.04878183875656092, 0.05401778690950767, 0.058787390960214854, 0.0629671206691269, 0.06644872323229394, 0.06914202697213162, 0.07097727673650549, 0.07190694052053058, 0.0719069405205306, 0.07097727673650549, 0.06914202697213163, 0.06644872323229395, 0.06296712066912691, 0.058787390960214854, 0.05401778690950764, 0.04878183875656093, 0.04321515480821898, 0.03746190925469937, 0.03167110813379747, 0.02599273015277674, 0.02057384231863098, 0.015554790979853772, 0.011065566929733114, 0.007222438713086256, 0.004124941332022009, 0.0018532983416694442, 0.0004663441022395425, 0.0],
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
            "samples": [0.0, -0.0004663441022395425, -0.0018532983416694481, -0.004124941332022012, -0.007222438713086256, -0.01106556692973311, -0.01555479097985376, -0.020573842318630964, -0.025992730152776717, -0.03167110813379744, -0.03746190925469937, -0.04321515480821896, -0.04878183875656092, -0.05401778690950767, -0.058787390960214854, -0.0629671206691269, -0.06644872323229394, -0.06914202697213162, -0.07097727673650549, -0.07190694052053058, -0.0719069405205306, -0.07097727673650549, -0.06914202697213163, -0.06644872323229395, -0.06296712066912691, -0.058787390960214854, -0.05401778690950764, -0.04878183875656093, -0.04321515480821898, -0.03746190925469937, -0.03167110813379747, -0.02599273015277674, -0.02057384231863098, -0.015554790979853772, -0.011065566929733114, -0.007222438713086256, -0.004124941332022009, -0.0018532983416694442, -0.0004663441022395425, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q6.xy.-x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 5.711068121089018e-20, 2.2696358819905875e-19, 5.051596198931377e-19, 8.844936452019012e-19, 1.355141112124846e-18, 1.904912498488403e-18, 2.519569014167377e-18, 3.18319137826989e-18, 3.878592120150474e-18, 4.587760725871619e-18, 5.2923301010542706e-18, 5.974052268974463e-18, 6.6152709835752365e-18, 7.199379016965116e-18, 7.71124827789714e-18, 8.137621621385713e-18, 8.467456201798096e-18, 8.692209476755734e-18, 8.80606045449469e-18, 8.806060454494691e-18, 8.692209476755734e-18, 8.467456201798097e-18, 8.137621621385715e-18, 7.711248277897141e-18, 7.199379016965116e-18, 6.615270983575233e-18, 5.974052268974465e-18, 5.292330101054272e-18, 4.587760725871619e-18, 3.878592120150477e-18, 3.183191378269893e-18, 2.519569014167379e-18, 1.9049124984884044e-18, 1.3551411121248463e-18, 8.844936452019012e-19, 5.051596198931373e-19, 2.2696358819905826e-19, 5.711068121089018e-20, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q6.xy.y180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 5.711068121089018e-20, 2.2696358819905875e-19, 5.051596198931377e-19, 8.844936452019012e-19, 1.355141112124846e-18, 1.904912498488403e-18, 2.519569014167377e-18, 3.18319137826989e-18, 3.878592120150474e-18, 4.587760725871619e-18, 5.2923301010542706e-18, 5.974052268974463e-18, 6.6152709835752365e-18, 7.199379016965116e-18, 7.71124827789714e-18, 8.137621621385713e-18, 8.467456201798096e-18, 8.692209476755734e-18, 8.80606045449469e-18, 8.806060454494691e-18, 8.692209476755734e-18, 8.467456201798097e-18, 8.137621621385715e-18, 7.711248277897141e-18, 7.199379016965116e-18, 6.615270983575233e-18, 5.974052268974465e-18, 5.292330101054272e-18, 4.587760725871619e-18, 3.878592120150477e-18, 3.183191378269893e-18, 2.519569014167379e-18, 1.9049124984884044e-18, 1.3551411121248463e-18, 8.844936452019012e-19, 5.051596198931373e-19, 2.2696358819905826e-19, 5.711068121089018e-20, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q6.xy.y180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.000932688204479085, 0.0037065966833388963, 0.008249882664044025, 0.014444877426172512, 0.02213113385946622, 0.03110958195970752, 0.04114768463726193, 0.051985460305553434, 0.06334221626759488, 0.07492381850939873, 0.08643030961643793, 0.09756367751312184, 0.10803557381901534, 0.11757478192042971, 0.1259342413382538, 0.13289744646458787, 0.13828405394426324, 0.14195455347301097, 0.14381388104106116, 0.1438138810410612, 0.14195455347301097, 0.13828405394426327, 0.1328974464645879, 0.12593424133825382, 0.11757478192042971, 0.10803557381901528, 0.09756367751312187, 0.08643030961643795, 0.07492381850939873, 0.06334221626759494, 0.05198546030555348, 0.04114768463726196, 0.031109581959707543, 0.022131133859466228, 0.014444877426172512, 0.008249882664044018, 0.0037065966833388884, 0.000932688204479085, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q6.xy.y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 2.855534060544509e-20, 1.1348179409952937e-19, 2.5257980994656885e-19, 4.422468226009506e-19, 6.77570556062423e-19, 9.524562492442015e-19, 1.2597845070836885e-18, 1.591595689134945e-18, 1.939296060075237e-18, 2.2938803629358095e-18, 2.6461650505271353e-18, 2.9870261344872316e-18, 3.3076354917876183e-18, 3.599689508482558e-18, 3.85562413894857e-18, 4.0688108106928565e-18, 4.233728100899048e-18, 4.346104738377867e-18, 4.403030227247345e-18, 4.4030302272473455e-18, 4.346104738377867e-18, 4.233728100899049e-18, 4.068810810692857e-18, 3.8556241389485704e-18, 3.599689508482558e-18, 3.3076354917876163e-18, 2.9870261344872323e-18, 2.646165050527136e-18, 2.2938803629358095e-18, 1.9392960600752387e-18, 1.5915956891349465e-18, 1.2597845070836894e-18, 9.524562492442022e-19, 6.775705560624231e-19, 4.422468226009506e-19, 2.5257980994656866e-19, 1.1348179409952913e-19, 2.855534060544509e-20, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q6.xy.y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0004663441022395425, 0.0018532983416694481, 0.004124941332022012, 0.007222438713086256, 0.01106556692973311, 0.01555479097985376, 0.020573842318630964, 0.025992730152776717, 0.03167110813379744, 0.03746190925469937, 0.04321515480821896, 0.04878183875656092, 0.05401778690950767, 0.058787390960214854, 0.0629671206691269, 0.06644872323229394, 0.06914202697213162, 0.07097727673650549, 0.07190694052053058, 0.0719069405205306, 0.07097727673650549, 0.06914202697213163, 0.06644872323229395, 0.06296712066912691, 0.058787390960214854, 0.05401778690950764, 0.04878183875656093, 0.04321515480821898, 0.03746190925469937, 0.03167110813379747, 0.02599273015277674, 0.02057384231863098, 0.015554790979853772, 0.011065566929733114, 0.007222438713086256, 0.004124941332022009, 0.0018532983416694442, 0.0004663441022395425, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q6.xy.-y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 2.855534060544509e-20, 1.1348179409952937e-19, 2.5257980994656885e-19, 4.422468226009506e-19, 6.77570556062423e-19, 9.524562492442015e-19, 1.2597845070836885e-18, 1.591595689134945e-18, 1.939296060075237e-18, 2.2938803629358095e-18, 2.6461650505271353e-18, 2.9870261344872316e-18, 3.3076354917876183e-18, 3.599689508482558e-18, 3.85562413894857e-18, 4.0688108106928565e-18, 4.233728100899048e-18, 4.346104738377867e-18, 4.403030227247345e-18, 4.4030302272473455e-18, 4.346104738377867e-18, 4.233728100899049e-18, 4.068810810692857e-18, 3.8556241389485704e-18, 3.599689508482558e-18, 3.3076354917876163e-18, 2.9870261344872323e-18, 2.646165050527136e-18, 2.2938803629358095e-18, 1.9392960600752387e-18, 1.5915956891349465e-18, 1.2597845070836894e-18, 9.524562492442022e-19, 6.775705560624231e-19, 4.422468226009506e-19, 2.5257980994656866e-19, 1.1348179409952913e-19, 2.855534060544509e-20, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q6.xy.-y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.0004663441022395425, -0.0018532983416694481, -0.004124941332022012, -0.007222438713086256, -0.01106556692973311, -0.01555479097985376, -0.020573842318630964, -0.025992730152776717, -0.03167110813379744, -0.03746190925469937, -0.04321515480821896, -0.04878183875656092, -0.05401778690950767, -0.058787390960214854, -0.0629671206691269, -0.06644872323229394, -0.06914202697213162, -0.07097727673650549, -0.07190694052053058, -0.0719069405205306, -0.07097727673650549, -0.06914202697213163, -0.06644872323229395, -0.06296712066912691, -0.058787390960214854, -0.05401778690950764, -0.04878183875656093, -0.04321515480821898, -0.03746190925469937, -0.03167110813379747, -0.02599273015277674, -0.02057384231863098, -0.015554790979853772, -0.011065566929733114, -0.007222438713086256, -0.004124941332022009, -0.0018532983416694442, -0.0004663441022395425, 0.0],
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
            "samples": [0.0, 0.0001984292420197456, 0.0007885777549407545, 0.0017551610022691186, 0.0030731449856218488, 0.004708394612135234, 0.006618557775439673, 0.008754162252968118, 0.011059897010533984, 0.013476044729063047, 0.015940028451789393, 0.018388032294565478, 0.02075665424374067, 0.022984548235011164, 0.025014012984261907, 0.02679248642051608, 0.028273907015963815, 0.029419906755337427, 0.030200804847353102, 0.030596376441614528, 0.03059637644161453, 0.030200804847353102, 0.02941990675533743, 0.028273907015963818, 0.026792486420516088, 0.025014012984261907, 0.022984548235011157, 0.020756654243740676, 0.018388032294565485, 0.015940028451789393, 0.01347604472906306, 0.011059897010533995, 0.008754162252968125, 0.006618557775439678, 0.004708394612135236, 0.0030731449856218488, 0.0017551610022691168, 0.0007885777549407529, 0.0001984292420197456, 0.0],
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
            "samples": [0.0, 9.92146210098728e-05, 0.00039428887747037725, 0.0008775805011345593, 0.0015365724928109244, 0.002354197306067617, 0.0033092788877198366, 0.004377081126484059, 0.005529948505266992, 0.006738022364531524, 0.007970014225894696, 0.009194016147282739, 0.010378327121870335, 0.011492274117505582, 0.012507006492130953, 0.01339624321025804, 0.014136953507981907, 0.014709953377668714, 0.015100402423676551, 0.015298188220807264, 0.015298188220807266, 0.015100402423676551, 0.014709953377668715, 0.014136953507981909, 0.013396243210258044, 0.012507006492130953, 0.011492274117505578, 0.010378327121870338, 0.009194016147282743, 0.007970014225894696, 0.00673802236453153, 0.005529948505266997, 0.0043770811264840625, 0.003309278887719839, 0.002354197306067618, 0.0015365724928109244, 0.0008775805011345584, 0.00039428887747037643, 9.92146210098728e-05, 0.0],
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
            "samples": [0.0, -9.92146210098728e-05, -0.00039428887747037725, -0.0008775805011345593, -0.0015365724928109244, -0.002354197306067617, -0.0033092788877198366, -0.004377081126484059, -0.005529948505266992, -0.006738022364531524, -0.007970014225894696, -0.009194016147282739, -0.010378327121870335, -0.011492274117505582, -0.012507006492130953, -0.01339624321025804, -0.014136953507981907, -0.014709953377668714, -0.015100402423676551, -0.015298188220807264, -0.015298188220807266, -0.015100402423676551, -0.014709953377668715, -0.014136953507981909, -0.013396243210258044, -0.012507006492130953, -0.011492274117505578, -0.010378327121870338, -0.009194016147282743, -0.007970014225894696, -0.00673802236453153, -0.005529948505266997, -0.0043770811264840625, -0.003309278887719839, -0.002354197306067618, -0.0015365724928109244, -0.0008775805011345584, -0.00039428887747037643, -9.92146210098728e-05, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q7.xy.-x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 1.2150286804835847e-20, 4.8286461173350047e-20, 1.0747261517085682e-19, 1.8817585849787678e-19, 2.883060195437029e-19, 4.052697797332011e-19, 5.360378391156994e-19, 6.772233736424912e-19, 8.25169752130681e-19, 9.76045241090081e-19, 1.1259422446078887e-18, 1.2709785090302667e-18, 1.4073976712927185e-18, 1.5316665467503338e-18, 1.6405666368041973e-18, 1.731277486324499e-18, 1.8014497319568786e-18, 1.8492659493992424e-18] + [1.873487723736536e-18] * 2 + [1.8492659493992424e-18, 1.801449731956879e-18, 1.7312774863244992e-18, 1.6405666368041977e-18, 1.5316665467503338e-18, 1.407397671292718e-18, 1.2709785090302673e-18, 1.125942244607889e-18, 9.76045241090081e-19, 8.251697521306818e-19, 6.772233736424918e-19, 5.360378391156998e-19, 4.052697797332014e-19, 2.88306019543703e-19, 1.8817585849787678e-19, 1.0747261517085671e-19, 4.8286461173349945e-20, 1.2150286804835847e-20, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q7.xy.y180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 1.2150286804835847e-20, 4.8286461173350047e-20, 1.0747261517085682e-19, 1.8817585849787678e-19, 2.883060195437029e-19, 4.052697797332011e-19, 5.360378391156994e-19, 6.772233736424912e-19, 8.25169752130681e-19, 9.76045241090081e-19, 1.1259422446078887e-18, 1.2709785090302667e-18, 1.4073976712927185e-18, 1.5316665467503338e-18, 1.6405666368041973e-18, 1.731277486324499e-18, 1.8014497319568786e-18, 1.8492659493992424e-18] + [1.873487723736536e-18] * 2 + [1.8492659493992424e-18, 1.801449731956879e-18, 1.7312774863244992e-18, 1.6405666368041977e-18, 1.5316665467503338e-18, 1.407397671292718e-18, 1.2709785090302673e-18, 1.125942244607889e-18, 9.76045241090081e-19, 8.251697521306818e-19, 6.772233736424918e-19, 5.360378391156998e-19, 4.052697797332014e-19, 2.88306019543703e-19, 1.8817585849787678e-19, 1.0747261517085671e-19, 4.8286461173349945e-20, 1.2150286804835847e-20, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q7.xy.y180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0001984292420197456, 0.0007885777549407545, 0.0017551610022691186, 0.0030731449856218488, 0.004708394612135234, 0.006618557775439673, 0.008754162252968118, 0.011059897010533984, 0.013476044729063047, 0.015940028451789393, 0.018388032294565478, 0.02075665424374067, 0.022984548235011164, 0.025014012984261907, 0.02679248642051608, 0.028273907015963815, 0.029419906755337427, 0.030200804847353102, 0.030596376441614528, 0.03059637644161453, 0.030200804847353102, 0.02941990675533743, 0.028273907015963818, 0.026792486420516088, 0.025014012984261907, 0.022984548235011157, 0.020756654243740676, 0.018388032294565485, 0.015940028451789393, 0.01347604472906306, 0.011059897010533995, 0.008754162252968125, 0.006618557775439678, 0.004708394612135236, 0.0030731449856218488, 0.0017551610022691168, 0.0007885777549407529, 0.0001984292420197456, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q7.xy.y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 6.0751434024179234e-21, 2.4143230586675023e-20, 5.373630758542841e-20, 9.408792924893839e-20, 1.4415300977185146e-19, 2.0263488986660056e-19, 2.680189195578497e-19, 3.386116868212456e-19, 4.125848760653405e-19, 4.880226205450405e-19, 5.629711223039444e-19, 6.354892545151334e-19, 7.036988356463592e-19, 7.658332733751669e-19, 8.202833184020986e-19, 8.656387431622495e-19, 9.007248659784393e-19, 9.246329746996212e-19] + [9.36743861868268e-19] * 2 + [9.246329746996212e-19, 9.007248659784395e-19, 8.656387431622496e-19, 8.202833184020988e-19, 7.658332733751669e-19, 7.03698835646359e-19, 6.354892545151337e-19, 5.629711223039445e-19, 4.880226205450405e-19, 4.125848760653409e-19, 3.386116868212459e-19, 2.680189195578499e-19, 2.026348898666007e-19, 1.441530097718515e-19, 9.408792924893839e-20, 5.3736307585428355e-20, 2.4143230586674972e-20, 6.0751434024179234e-21, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q7.xy.y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 9.92146210098728e-05, 0.00039428887747037725, 0.0008775805011345593, 0.0015365724928109244, 0.002354197306067617, 0.0033092788877198366, 0.004377081126484059, 0.005529948505266992, 0.006738022364531524, 0.007970014225894696, 0.009194016147282739, 0.010378327121870335, 0.011492274117505582, 0.012507006492130953, 0.01339624321025804, 0.014136953507981907, 0.014709953377668714, 0.015100402423676551, 0.015298188220807264, 0.015298188220807266, 0.015100402423676551, 0.014709953377668715, 0.014136953507981909, 0.013396243210258044, 0.012507006492130953, 0.011492274117505578, 0.010378327121870338, 0.009194016147282743, 0.007970014225894696, 0.00673802236453153, 0.005529948505266997, 0.0043770811264840625, 0.003309278887719839, 0.002354197306067618, 0.0015365724928109244, 0.0008775805011345584, 0.00039428887747037643, 9.92146210098728e-05, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q7.xy.-y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 6.0751434024179234e-21, 2.4143230586675023e-20, 5.373630758542841e-20, 9.408792924893839e-20, 1.4415300977185146e-19, 2.0263488986660056e-19, 2.680189195578497e-19, 3.386116868212456e-19, 4.125848760653405e-19, 4.880226205450405e-19, 5.629711223039444e-19, 6.354892545151334e-19, 7.036988356463592e-19, 7.658332733751669e-19, 8.202833184020986e-19, 8.656387431622495e-19, 9.007248659784393e-19, 9.246329746996212e-19] + [9.36743861868268e-19] * 2 + [9.246329746996212e-19, 9.007248659784395e-19, 8.656387431622496e-19, 8.202833184020988e-19, 7.658332733751669e-19, 7.03698835646359e-19, 6.354892545151337e-19, 5.629711223039445e-19, 4.880226205450405e-19, 4.125848760653409e-19, 3.386116868212459e-19, 2.680189195578499e-19, 2.026348898666007e-19, 1.441530097718515e-19, 9.408792924893839e-20, 5.3736307585428355e-20, 2.4143230586674972e-20, 6.0751434024179234e-21, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q7.xy.-y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -9.92146210098728e-05, -0.00039428887747037725, -0.0008775805011345593, -0.0015365724928109244, -0.002354197306067617, -0.0033092788877198366, -0.004377081126484059, -0.005529948505266992, -0.006738022364531524, -0.007970014225894696, -0.009194016147282739, -0.010378327121870335, -0.011492274117505582, -0.012507006492130953, -0.01339624321025804, -0.014136953507981907, -0.014709953377668714, -0.015100402423676551, -0.015298188220807264, -0.015298188220807266, -0.015100402423676551, -0.014709953377668715, -0.014136953507981909, -0.013396243210258044, -0.012507006492130953, -0.011492274117505578, -0.010378327121870338, -0.009194016147282743, -0.007970014225894696, -0.00673802236453153, -0.005529948505266997, -0.0043770811264840625, -0.003309278887719839, -0.002354197306067618, -0.0015365724928109244, -0.0008775805011345584, -0.00039428887747037643, -9.92146210098728e-05, 0.0],
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
            "samples": [0.0, 0.0008576065731987051, 0.003408214733028973, 0.007585765067924001, 0.013282061218576217, 0.020349572106810397, 0.02860525291301387, 0.03783528584081555, 0.047800617885698525, 0.058243152182248355, 0.0688924325773952, 0.0794726483027143, 0.08970977732845153, 0.09933868339015663, 0.10810998287866297, 0.11579650374456989, 0.122199169134994, 0.12715215337948865, 0.1305271767878043, 0.13223682802648376, 0.1322368280264838, 0.1305271767878043, 0.12715215337948865, 0.12219916913499403, 0.11579650374456991, 0.10810998287866297, 0.09933868339015657, 0.08970977732845156, 0.07947264830271435, 0.0688924325773952, 0.0582431521822484, 0.04780061788569857, 0.03783528584081559, 0.028605252913013895, 0.020349572106810404, 0.013282061218576217, 0.007585765067923993, 0.0034082147330289658, 0.0008576065731987051, 0.0],
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
            "samples": [0.0, 0.00042880328659935255, 0.0017041073665144866, 0.0037928825339620005, 0.006641030609288109, 0.010174786053405199, 0.014302626456506935, 0.018917642920407776, 0.023900308942849263, 0.029121576091124177, 0.0344462162886976, 0.03973632415135715, 0.04485488866422577, 0.04966934169507831, 0.054054991439331485, 0.05789825187228494, 0.061099584567497, 0.06357607668974433, 0.06526358839390214, 0.06611841401324188, 0.0661184140132419, 0.06526358839390214, 0.06357607668974433, 0.06109958456749701, 0.05789825187228496, 0.054054991439331485, 0.049669341695078285, 0.04485488866422578, 0.03973632415135717, 0.0344462162886976, 0.0291215760911242, 0.023900308942849283, 0.018917642920407794, 0.014302626456506947, 0.010174786053405202, 0.006641030609288109, 0.0037928825339619966, 0.0017041073665144829, 0.00042880328659935255, 0.0],
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
            "samples": [0.0, -0.00042880328659935255, -0.0017041073665144866, -0.0037928825339620005, -0.006641030609288109, -0.010174786053405199, -0.014302626456506935, -0.018917642920407776, -0.023900308942849263, -0.029121576091124177, -0.0344462162886976, -0.03973632415135715, -0.04485488866422577, -0.04966934169507831, -0.054054991439331485, -0.05789825187228494, -0.061099584567497, -0.06357607668974433, -0.06526358839390214, -0.06611841401324188, -0.0661184140132419, -0.06526358839390214, -0.06357607668974433, -0.06109958456749701, -0.05789825187228496, -0.054054991439331485, -0.049669341695078285, -0.04485488866422578, -0.03973632415135717, -0.0344462162886976, -0.0291215760911242, -0.023900308942849283, -0.018917642920407794, -0.014302626456506947, -0.010174786053405202, -0.006641030609288109, -0.0037928825339619966, -0.0017041073665144829, -0.00042880328659935255, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q8.xy.-x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 5.251325723977622e-20, 2.0869296318053915e-19, 4.644941454758466e-19, 8.132916878704279e-19, 1.2460519172311808e-18, 1.751566570936147e-18, 2.316743084988997e-18, 2.9269436845493212e-18, 3.566364494612131e-18, 4.218444852069094e-18, 4.86629621818412e-18, 5.4931395828754984e-18, 6.082740032263383e-18, 6.619827224411488e-18, 7.0904908831621e-18, 7.482541066981822e-18, 7.785823882044205e-18, 7.992484462746261e-18, 8.097170408601617e-18, 8.097170408601619e-18, 7.992484462746261e-18, 7.785823882044205e-18, 7.482541066981824e-18, 7.090490883162102e-18, 6.619827224411488e-18, 6.082740032263379e-18, 5.4931395828755e-18, 4.866296218184123e-18, 4.218444852069094e-18, 3.566364494612134e-18, 2.9269436845493235e-18, 2.3167430849889993e-18, 1.7515665709361485e-18, 1.2460519172311812e-18, 8.132916878704279e-19, 4.644941454758461e-19, 2.086929631805387e-19, 5.251325723977622e-20, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q8.xy.y180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 5.251325723977622e-20, 2.0869296318053915e-19, 4.644941454758466e-19, 8.132916878704279e-19, 1.2460519172311808e-18, 1.751566570936147e-18, 2.316743084988997e-18, 2.9269436845493212e-18, 3.566364494612131e-18, 4.218444852069094e-18, 4.86629621818412e-18, 5.4931395828754984e-18, 6.082740032263383e-18, 6.619827224411488e-18, 7.0904908831621e-18, 7.482541066981822e-18, 7.785823882044205e-18, 7.992484462746261e-18, 8.097170408601617e-18, 8.097170408601619e-18, 7.992484462746261e-18, 7.785823882044205e-18, 7.482541066981824e-18, 7.090490883162102e-18, 6.619827224411488e-18, 6.082740032263379e-18, 5.4931395828755e-18, 4.866296218184123e-18, 4.218444852069094e-18, 3.566364494612134e-18, 2.9269436845493235e-18, 2.3167430849889993e-18, 1.7515665709361485e-18, 1.2460519172311812e-18, 8.132916878704279e-19, 4.644941454758461e-19, 2.086929631805387e-19, 5.251325723977622e-20, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q8.xy.y180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0008576065731987051, 0.003408214733028973, 0.007585765067924001, 0.013282061218576217, 0.020349572106810397, 0.02860525291301387, 0.03783528584081555, 0.047800617885698525, 0.058243152182248355, 0.0688924325773952, 0.0794726483027143, 0.08970977732845153, 0.09933868339015663, 0.10810998287866297, 0.11579650374456989, 0.122199169134994, 0.12715215337948865, 0.1305271767878043, 0.13223682802648376, 0.1322368280264838, 0.1305271767878043, 0.12715215337948865, 0.12219916913499403, 0.11579650374456991, 0.10810998287866297, 0.09933868339015657, 0.08970977732845156, 0.07947264830271435, 0.0688924325773952, 0.0582431521822484, 0.04780061788569857, 0.03783528584081559, 0.028605252913013895, 0.020349572106810404, 0.013282061218576217, 0.007585765067923993, 0.0034082147330289658, 0.0008576065731987051, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q8.xy.y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 2.625662861988811e-20, 1.0434648159026957e-19, 2.322470727379233e-19, 4.0664584393521396e-19, 6.230259586155904e-19, 8.757832854680735e-19, 1.1583715424944985e-18, 1.4634718422746606e-18, 1.7831822473060655e-18, 2.109222426034547e-18, 2.43314810909206e-18, 2.7465697914377492e-18, 3.0413700161316915e-18, 3.309913612205744e-18, 3.54524544158105e-18, 3.741270533490911e-18, 3.892911941022102e-18, 3.996242231373131e-18, 4.048585204300809e-18, 4.0485852043008094e-18, 3.996242231373131e-18, 3.892911941022102e-18, 3.741270533490912e-18, 3.545245441581051e-18, 3.309913612205744e-18, 3.0413700161316896e-18, 2.74656979143775e-18, 2.4331481090920613e-18, 2.109222426034547e-18, 1.783182247306067e-18, 1.4634718422746618e-18, 1.1583715424944996e-18, 8.757832854680742e-19, 6.230259586155906e-19, 4.0664584393521396e-19, 2.3224707273792306e-19, 1.0434648159026935e-19, 2.625662861988811e-20, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q8.xy.y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.00042880328659935255, 0.0017041073665144866, 0.0037928825339620005, 0.006641030609288109, 0.010174786053405199, 0.014302626456506935, 0.018917642920407776, 0.023900308942849263, 0.029121576091124177, 0.0344462162886976, 0.03973632415135715, 0.04485488866422577, 0.04966934169507831, 0.054054991439331485, 0.05789825187228494, 0.061099584567497, 0.06357607668974433, 0.06526358839390214, 0.06611841401324188, 0.0661184140132419, 0.06526358839390214, 0.06357607668974433, 0.06109958456749701, 0.05789825187228496, 0.054054991439331485, 0.049669341695078285, 0.04485488866422578, 0.03973632415135717, 0.0344462162886976, 0.0291215760911242, 0.023900308942849283, 0.018917642920407794, 0.014302626456506947, 0.010174786053405202, 0.006641030609288109, 0.0037928825339619966, 0.0017041073665144829, 0.00042880328659935255, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q8.xy.-y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 2.625662861988811e-20, 1.0434648159026957e-19, 2.322470727379233e-19, 4.0664584393521396e-19, 6.230259586155904e-19, 8.757832854680735e-19, 1.1583715424944985e-18, 1.4634718422746606e-18, 1.7831822473060655e-18, 2.109222426034547e-18, 2.43314810909206e-18, 2.7465697914377492e-18, 3.0413700161316915e-18, 3.309913612205744e-18, 3.54524544158105e-18, 3.741270533490911e-18, 3.892911941022102e-18, 3.996242231373131e-18, 4.048585204300809e-18, 4.0485852043008094e-18, 3.996242231373131e-18, 3.892911941022102e-18, 3.741270533490912e-18, 3.545245441581051e-18, 3.309913612205744e-18, 3.0413700161316896e-18, 2.74656979143775e-18, 2.4331481090920613e-18, 2.109222426034547e-18, 1.783182247306067e-18, 1.4634718422746618e-18, 1.1583715424944996e-18, 8.757832854680742e-19, 6.230259586155906e-19, 4.0664584393521396e-19, 2.3224707273792306e-19, 1.0434648159026935e-19, 2.625662861988811e-20, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q8.xy.-y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.00042880328659935255, -0.0017041073665144866, -0.0037928825339620005, -0.006641030609288109, -0.010174786053405199, -0.014302626456506935, -0.018917642920407776, -0.023900308942849263, -0.029121576091124177, -0.0344462162886976, -0.03973632415135715, -0.04485488866422577, -0.04966934169507831, -0.054054991439331485, -0.05789825187228494, -0.061099584567497, -0.06357607668974433, -0.06526358839390214, -0.06611841401324188, -0.0661184140132419, -0.06526358839390214, -0.06357607668974433, -0.06109958456749701, -0.05789825187228496, -0.054054991439331485, -0.049669341695078285, -0.04485488866422578, -0.03973632415135717, -0.0344462162886976, -0.0291215760911242, -0.023900308942849283, -0.018917642920407794, -0.014302626456506947, -0.010174786053405202, -0.006641030609288109, -0.0037928825339619966, -0.0017041073665144829, -0.00042880328659935255, 0.0],
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


