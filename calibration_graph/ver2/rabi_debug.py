
# Single QUA script generated at 2024-12-11 18:36:17.337815
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
        with for_(v19,1,(v19<=99),(v19+2)):
            with for_(v18,0.8,(v18<1.1975000000000002),(v18+0.0050000000000000044)):
                wait(23657, "q1.xy", "q1.resonator")
                with for_(v20,0,(v20<v19),(v20+1)):
                    play("x180"*amp(v18), "q1.xy")
                align("q1.xy", "q1.resonator")
                measure("readout", "q1.resonator", None, dual_demod.full("iw1", "iw2", v2), dual_demod.full("iw3", "iw1", v10))
                r2 = declare_stream()
                save(v2, r2)
                r10 = declare_stream()
                save(v10, r10)
    with for_(v1,0,(v1<50),(v1+1)):
        save(v1, r1)
        with for_(v19,1,(v19<=99),(v19+2)):
            with for_(v18,0.8,(v18<1.1975000000000002),(v18+0.0050000000000000044)):
                wait(33777, "q2.xy", "q2.resonator")
                with for_(v20,0,(v20<v19),(v20+1)):
                    play("x180"*amp(v18), "q2.xy")
                align("q2.xy", "q2.resonator")
                measure("readout", "q2.resonator", None, dual_demod.full("iw1", "iw2", v3), dual_demod.full("iw3", "iw1", v11))
                r3 = declare_stream()
                save(v3, r3)
                r11 = declare_stream()
                save(v11, r11)
    with for_(v1,0,(v1<50),(v1+1)):
        save(v1, r1)
        with for_(v19,1,(v19<=99),(v19+2)):
            with for_(v18,0.8,(v18<1.1975000000000002),(v18+0.0050000000000000044)):
                wait(49097, "q3.xy", "q3.resonator")
                with for_(v20,0,(v20<v19),(v20+1)):
                    play("x180"*amp(v18), "q3.xy")
                align("q3.xy", "q3.resonator")
                measure("readout", "q3.resonator", None, dual_demod.full("iw1", "iw2", v4), dual_demod.full("iw3", "iw1", v12))
                r4 = declare_stream()
                save(v4, r4)
                r12 = declare_stream()
                save(v12, r12)
    with for_(v1,0,(v1<50),(v1+1)):
        save(v1, r1)
        with for_(v19,1,(v19<=99),(v19+2)):
            with for_(v18,0.8,(v18<1.1975000000000002),(v18+0.0050000000000000044)):
                wait(44744, "q4.xy", "q4.resonator")
                with for_(v20,0,(v20<v19),(v20+1)):
                    play("x180"*amp(v18), "q4.xy")
                align("q4.xy", "q4.resonator")
                measure("readout", "q4.resonator", None, dual_demod.full("iw1", "iw2", v5), dual_demod.full("iw3", "iw1", v13))
                r5 = declare_stream()
                save(v5, r5)
                r13 = declare_stream()
                save(v13, r13)
    with for_(v1,0,(v1<50),(v1+1)):
        save(v1, r1)
        with for_(v19,1,(v19<=99),(v19+2)):
            with for_(v18,0.8,(v18<1.1975000000000002),(v18+0.0050000000000000044)):
                wait(35346, "q5.xy", "q5.resonator")
                with for_(v20,0,(v20<v19),(v20+1)):
                    play("x180"*amp(v18), "q5.xy")
                align("q5.xy", "q5.resonator")
                measure("readout", "q5.resonator", None, dual_demod.full("iw1", "iw2", v6), dual_demod.full("iw3", "iw1", v14))
                r6 = declare_stream()
                save(v6, r6)
                r14 = declare_stream()
                save(v14, r14)
    with for_(v1,0,(v1<50),(v1+1)):
        save(v1, r1)
        with for_(v19,1,(v19<=99),(v19+2)):
            with for_(v18,0.8,(v18<1.1975000000000002),(v18+0.0050000000000000044)):
                wait(28009, "q6.xy", "q6.resonator")
                with for_(v20,0,(v20<v19),(v20+1)):
                    play("x180"*amp(v18), "q6.xy")
                align("q6.xy", "q6.resonator")
                measure("readout", "q6.resonator", None, dual_demod.full("iw1", "iw2", v7), dual_demod.full("iw3", "iw1", v15))
                r7 = declare_stream()
                save(v7, r7)
                r15 = declare_stream()
                save(v15, r15)
    with for_(v1,0,(v1<50),(v1+1)):
        save(v1, r1)
        with for_(v19,1,(v19<=99),(v19+2)):
            with for_(v18,0.8,(v18<1.1975000000000002),(v18+0.0050000000000000044)):
                wait(17310, "q7.xy", "q7.resonator")
                with for_(v20,0,(v20<v19),(v20+1)):
                    play("x180"*amp(v18), "q7.xy")
                align("q7.xy", "q7.resonator")
                measure("readout", "q7.resonator", None, dual_demod.full("iw1", "iw2", v8), dual_demod.full("iw3", "iw1", v16))
                r8 = declare_stream()
                save(v8, r8)
                r16 = declare_stream()
                save(v16, r16)
    with for_(v1,0,(v1<50),(v1+1)):
        save(v1, r1)
        with for_(v19,1,(v19<=99),(v19+2)):
            with for_(v18,0.8,(v18<1.1975000000000002),(v18+0.0050000000000000044)):
                wait(37622, "q8.xy", "q8.resonator")
                with for_(v20,0,(v20<v19),(v20+1)):
                    play("x180"*amp(v18), "q8.xy")
                align("q8.xy", "q8.resonator")
                measure("readout", "q8.resonator", None, dual_demod.full("iw1", "iw2", v9), dual_demod.full("iw3", "iw1", v17))
                r9 = declare_stream()
                save(v9, r9)
                r17 = declare_stream()
                save(v17, r17)
    with stream_processing():
        r1.save("iteration")
        r2.buffer(80).buffer(50).average().save("I1")
        r10.buffer(80).buffer(50).average().save("Q1")
        r3.buffer(80).buffer(50).average().save("I2")
        r11.buffer(80).buffer(50).average().save("Q2")
        r4.buffer(80).buffer(50).average().save("I3")
        r12.buffer(80).buffer(50).average().save("Q3")
        r5.buffer(80).buffer(50).average().save("I4")
        r13.buffer(80).buffer(50).average().save("Q4")
        r6.buffer(80).buffer(50).average().save("I5")
        r14.buffer(80).buffer(50).average().save("Q5")
        r7.buffer(80).buffer(50).average().save("I6")
        r15.buffer(80).buffer(50).average().save("Q6")
        r8.buffer(80).buffer(50).average().save("I7")
        r16.buffer(80).buffer(50).average().save("Q7")
        r9.buffer(80).buffer(50).average().save("I8")
        r17.buffer(80).buffer(50).average().save("Q8")


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
                            "full_scale_power_dbm": -17,
                            "upconverter_frequency": 9983000000,
                        },
                        "2": {
                            "band": 1,
                            "delay": 0,
                            "shareable": False,
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": -5,
                            "upconverter_frequency": 4551000000,
                        },
                        "8": {
                            "band": 3,
                            "delay": 0,
                            "shareable": False,
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": -17,
                            "upconverter_frequency": 9572000000,
                        },
                        "3": {
                            "band": 1,
                            "delay": 0,
                            "shareable": False,
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": -5,
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
                            "full_scale_power_dbm": -17,
                            "upconverter_frequency": 9896000000,
                        },
                        "2": {
                            "band": 1,
                            "delay": 0,
                            "shareable": False,
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": -5,
                            "upconverter_frequency": 4303000000,
                        },
                        "8": {
                            "band": 3,
                            "delay": 0,
                            "shareable": False,
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": -17,
                            "upconverter_frequency": 9374000000,
                        },
                        "3": {
                            "band": 1,
                            "delay": 0,
                            "shareable": False,
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": -5,
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
                            "full_scale_power_dbm": -17,
                            "upconverter_frequency": 9697000000,
                        },
                        "2": {
                            "band": 1,
                            "delay": 0,
                            "shareable": False,
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": -5,
                            "upconverter_frequency": 4461000000,
                        },
                        "8": {
                            "band": 3,
                            "delay": 0,
                            "shareable": False,
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": -17,
                            "upconverter_frequency": 9275000000,
                        },
                        "3": {
                            "band": 1,
                            "delay": 0,
                            "shareable": False,
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": -5,
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
                            "full_scale_power_dbm": -17,
                            "upconverter_frequency": 9792000000,
                        },
                        "2": {
                            "band": 1,
                            "delay": 0,
                            "shareable": False,
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": -5,
                            "upconverter_frequency": 4464000000,
                        },
                        "8": {
                            "band": 3,
                            "delay": 0,
                            "shareable": False,
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": -17,
                            "upconverter_frequency": 9468000000,
                        },
                        "3": {
                            "band": 1,
                            "delay": 0,
                            "shareable": False,
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": -5,
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
                "cr_q2_q1_Square": "q1.xy.cr_q2_q1_Square.pulse",
            },
            "intermediate_frequency": 51429959.310891405,
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
            "intermediate_frequency": 50020905,
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
            "intermediate_frequency": 51021926.20792695,
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
            "intermediate_frequency": 49474765,
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
            "intermediate_frequency": 47978773.749092855,
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
            "intermediate_frequency": 50688915,
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
            "intermediate_frequency": 50838121.96023835,
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
            "intermediate_frequency": 49581765,
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
            "intermediate_frequency": 50158321.634366505,
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
            "intermediate_frequency": 50221316,
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
            "intermediate_frequency": 51211754.33278539,
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
            "intermediate_frequency": 49661041,
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
            "intermediate_frequency": 51286611.227740586,
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
            "intermediate_frequency": 49850000,
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
            "intermediate_frequency": 51093212.89560413,
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
            "intermediate_frequency": 49800000,
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
            "intermediate_frequency": -179978073.79207325,
            "MWInput": {
                "port": ('con1', 2, 2),
                "upconverter": 1,
            },
        },
        "zz_q1_q2": {
            "operations": {
                "square": "zz_q1_q2.square.pulse",
            },
            "MWInput": {
                "port": ('con1', 2, 2),
                "upconverter": 1,
            },
        },
        "cr_q2_q1": {
            "operations": {
                "square": "cr_q2_q1.square.pulse",
            },
            "intermediate_frequency": 282429959.31089115,
            "MWInput": {
                "port": ('con1', 2, 3),
                "upconverter": 1,
            },
        },
        "cr_q2_q3": {
            "operations": {
                "square": "cr_q2_q3.square.pulse",
            },
            "intermediate_frequency": 30978773.749093056,
            "MWInput": {
                "port": ('con1', 2, 3),
                "upconverter": 1,
            },
        },
        "zz_q2_q3": {
            "operations": {
                "square": "zz_q2_q3.square.pulse",
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
                "port": ('con1', 3, 2),
                "upconverter": 1,
            },
        },
        "zz_q3_q4": {
            "operations": {
                "square": "zz_q3_q4.square.pulse",
            },
            "MWInput": {
                "port": ('con1', 3, 2),
                "upconverter": 1,
            },
        },
        "cr_q4_q5": {
            "operations": {
                "square": "cr_q4_q5.square.pulse",
            },
            "MWInput": {
                "port": ('con1', 3, 3),
                "upconverter": 1,
            },
        },
        "zz_q4_q5": {
            "operations": {
                "square": "zz_q4_q5.square.pulse",
            },
            "MWInput": {
                "port": ('con1', 3, 3),
                "upconverter": 1,
            },
        },
        "cr_q5_q6": {
            "operations": {
                "square": "cr_q5_q6.square.pulse",
            },
            "MWInput": {
                "port": ('con1', 5, 2),
                "upconverter": 1,
            },
        },
        "zz_q5_q6": {
            "operations": {
                "square": "zz_q5_q6.square.pulse",
            },
            "MWInput": {
                "port": ('con1', 5, 2),
                "upconverter": 1,
            },
        },
        "cr_q6_q7": {
            "operations": {
                "square": "cr_q6_q7.square.pulse",
            },
            "MWInput": {
                "port": ('con1', 5, 3),
                "upconverter": 1,
            },
        },
        "zz_q6_q7": {
            "operations": {
                "square": "zz_q6_q7.square.pulse",
            },
            "MWInput": {
                "port": ('con1', 5, 3),
                "upconverter": 1,
            },
        },
        "cr_q7_q8": {
            "operations": {
                "square": "cr_q7_q8.square.pulse",
            },
            "MWInput": {
                "port": ('con1', 7, 2),
                "upconverter": 1,
            },
        },
        "zz_q7_q8": {
            "operations": {
                "square": "zz_q7_q8.square.pulse",
            },
            "MWInput": {
                "port": ('con1', 7, 2),
                "upconverter": 1,
            },
        },
        "cr_q8_q1": {
            "operations": {
                "square": "cr_q8_q1.square.pulse",
            },
            "MWInput": {
                "port": ('con1', 7, 3),
                "upconverter": 1,
            },
        },
        "zz_q8_q1": {
            "operations": {
                "square": "zz_q8_q1.square.pulse",
            },
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
            "length": 28,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q1.xy.x180_DragCosine.wf.I",
                "Q": "q1.xy.x180_DragCosine.wf.Q",
            },
        },
        "q1.xy.x90_DragCosine.pulse": {
            "operation": "control",
            "length": 28,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q1.xy.x90_DragCosine.wf.I",
                "Q": "q1.xy.x90_DragCosine.wf.Q",
            },
        },
        "q1.xy.-x90_DragCosine.pulse": {
            "operation": "control",
            "length": 28,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q1.xy.-x90_DragCosine.wf.I",
                "Q": "q1.xy.-x90_DragCosine.wf.Q",
            },
        },
        "q1.xy.y180_DragCosine.pulse": {
            "operation": "control",
            "length": 28,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q1.xy.y180_DragCosine.wf.I",
                "Q": "q1.xy.y180_DragCosine.wf.Q",
            },
        },
        "q1.xy.y90_DragCosine.pulse": {
            "operation": "control",
            "length": 28,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q1.xy.y90_DragCosine.wf.I",
                "Q": "q1.xy.y90_DragCosine.wf.Q",
            },
        },
        "q1.xy.-y90_DragCosine.pulse": {
            "operation": "control",
            "length": 28,
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
        "q1.xy.cr_q2_q1_Square.pulse": {
            "operation": "control",
            "length": 100,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q1.xy.cr_q2_q1_Square.wf.I",
                "Q": "q1.xy.cr_q2_q1_Square.wf.Q",
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
            "length": 28,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q2.xy.x180_DragCosine.wf.I",
                "Q": "q2.xy.x180_DragCosine.wf.Q",
            },
        },
        "q2.xy.x90_DragCosine.pulse": {
            "operation": "control",
            "length": 28,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q2.xy.x90_DragCosine.wf.I",
                "Q": "q2.xy.x90_DragCosine.wf.Q",
            },
        },
        "q2.xy.-x90_DragCosine.pulse": {
            "operation": "control",
            "length": 28,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q2.xy.-x90_DragCosine.wf.I",
                "Q": "q2.xy.-x90_DragCosine.wf.Q",
            },
        },
        "q2.xy.y180_DragCosine.pulse": {
            "operation": "control",
            "length": 28,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q2.xy.y180_DragCosine.wf.I",
                "Q": "q2.xy.y180_DragCosine.wf.Q",
            },
        },
        "q2.xy.y90_DragCosine.pulse": {
            "operation": "control",
            "length": 28,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q2.xy.y90_DragCosine.wf.I",
                "Q": "q2.xy.y90_DragCosine.wf.Q",
            },
        },
        "q2.xy.-y90_DragCosine.pulse": {
            "operation": "control",
            "length": 28,
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
            "length": 2500,
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
            "length": 28,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q3.xy.x180_DragCosine.wf.I",
                "Q": "q3.xy.x180_DragCosine.wf.Q",
            },
        },
        "q3.xy.x90_DragCosine.pulse": {
            "operation": "control",
            "length": 28,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q3.xy.x90_DragCosine.wf.I",
                "Q": "q3.xy.x90_DragCosine.wf.Q",
            },
        },
        "q3.xy.-x90_DragCosine.pulse": {
            "operation": "control",
            "length": 28,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q3.xy.-x90_DragCosine.wf.I",
                "Q": "q3.xy.-x90_DragCosine.wf.Q",
            },
        },
        "q3.xy.y180_DragCosine.pulse": {
            "operation": "control",
            "length": 28,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q3.xy.y180_DragCosine.wf.I",
                "Q": "q3.xy.y180_DragCosine.wf.Q",
            },
        },
        "q3.xy.y90_DragCosine.pulse": {
            "operation": "control",
            "length": 28,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q3.xy.y90_DragCosine.wf.I",
                "Q": "q3.xy.y90_DragCosine.wf.Q",
            },
        },
        "q3.xy.-y90_DragCosine.pulse": {
            "operation": "control",
            "length": 28,
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
            "length": 28,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q4.xy.x180_DragCosine.wf.I",
                "Q": "q4.xy.x180_DragCosine.wf.Q",
            },
        },
        "q4.xy.x90_DragCosine.pulse": {
            "operation": "control",
            "length": 28,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q4.xy.x90_DragCosine.wf.I",
                "Q": "q4.xy.x90_DragCosine.wf.Q",
            },
        },
        "q4.xy.-x90_DragCosine.pulse": {
            "operation": "control",
            "length": 28,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q4.xy.-x90_DragCosine.wf.I",
                "Q": "q4.xy.-x90_DragCosine.wf.Q",
            },
        },
        "q4.xy.y180_DragCosine.pulse": {
            "operation": "control",
            "length": 28,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q4.xy.y180_DragCosine.wf.I",
                "Q": "q4.xy.y180_DragCosine.wf.Q",
            },
        },
        "q4.xy.y90_DragCosine.pulse": {
            "operation": "control",
            "length": 28,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q4.xy.y90_DragCosine.wf.I",
                "Q": "q4.xy.y90_DragCosine.wf.Q",
            },
        },
        "q4.xy.-y90_DragCosine.pulse": {
            "operation": "control",
            "length": 28,
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
            "length": 28,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q5.xy.x180_DragCosine.wf.I",
                "Q": "q5.xy.x180_DragCosine.wf.Q",
            },
        },
        "q5.xy.x90_DragCosine.pulse": {
            "operation": "control",
            "length": 28,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q5.xy.x90_DragCosine.wf.I",
                "Q": "q5.xy.x90_DragCosine.wf.Q",
            },
        },
        "q5.xy.-x90_DragCosine.pulse": {
            "operation": "control",
            "length": 28,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q5.xy.-x90_DragCosine.wf.I",
                "Q": "q5.xy.-x90_DragCosine.wf.Q",
            },
        },
        "q5.xy.y180_DragCosine.pulse": {
            "operation": "control",
            "length": 28,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q5.xy.y180_DragCosine.wf.I",
                "Q": "q5.xy.y180_DragCosine.wf.Q",
            },
        },
        "q5.xy.y90_DragCosine.pulse": {
            "operation": "control",
            "length": 28,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q5.xy.y90_DragCosine.wf.I",
                "Q": "q5.xy.y90_DragCosine.wf.Q",
            },
        },
        "q5.xy.-y90_DragCosine.pulse": {
            "operation": "control",
            "length": 28,
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
            "length": 28,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q6.xy.x180_DragCosine.wf.I",
                "Q": "q6.xy.x180_DragCosine.wf.Q",
            },
        },
        "q6.xy.x90_DragCosine.pulse": {
            "operation": "control",
            "length": 28,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q6.xy.x90_DragCosine.wf.I",
                "Q": "q6.xy.x90_DragCosine.wf.Q",
            },
        },
        "q6.xy.-x90_DragCosine.pulse": {
            "operation": "control",
            "length": 28,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q6.xy.-x90_DragCosine.wf.I",
                "Q": "q6.xy.-x90_DragCosine.wf.Q",
            },
        },
        "q6.xy.y180_DragCosine.pulse": {
            "operation": "control",
            "length": 28,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q6.xy.y180_DragCosine.wf.I",
                "Q": "q6.xy.y180_DragCosine.wf.Q",
            },
        },
        "q6.xy.y90_DragCosine.pulse": {
            "operation": "control",
            "length": 28,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q6.xy.y90_DragCosine.wf.I",
                "Q": "q6.xy.y90_DragCosine.wf.Q",
            },
        },
        "q6.xy.-y90_DragCosine.pulse": {
            "operation": "control",
            "length": 28,
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
            "length": 28,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q7.xy.x180_DragCosine.wf.I",
                "Q": "q7.xy.x180_DragCosine.wf.Q",
            },
        },
        "q7.xy.x90_DragCosine.pulse": {
            "operation": "control",
            "length": 28,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q7.xy.x90_DragCosine.wf.I",
                "Q": "q7.xy.x90_DragCosine.wf.Q",
            },
        },
        "q7.xy.-x90_DragCosine.pulse": {
            "operation": "control",
            "length": 28,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q7.xy.-x90_DragCosine.wf.I",
                "Q": "q7.xy.-x90_DragCosine.wf.Q",
            },
        },
        "q7.xy.y180_DragCosine.pulse": {
            "operation": "control",
            "length": 28,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q7.xy.y180_DragCosine.wf.I",
                "Q": "q7.xy.y180_DragCosine.wf.Q",
            },
        },
        "q7.xy.y90_DragCosine.pulse": {
            "operation": "control",
            "length": 28,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q7.xy.y90_DragCosine.wf.I",
                "Q": "q7.xy.y90_DragCosine.wf.Q",
            },
        },
        "q7.xy.-y90_DragCosine.pulse": {
            "operation": "control",
            "length": 28,
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
            "length": 28,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q8.xy.x180_DragCosine.wf.I",
                "Q": "q8.xy.x180_DragCosine.wf.Q",
            },
        },
        "q8.xy.x90_DragCosine.pulse": {
            "operation": "control",
            "length": 28,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q8.xy.x90_DragCosine.wf.I",
                "Q": "q8.xy.x90_DragCosine.wf.Q",
            },
        },
        "q8.xy.-x90_DragCosine.pulse": {
            "operation": "control",
            "length": 28,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q8.xy.-x90_DragCosine.wf.I",
                "Q": "q8.xy.-x90_DragCosine.wf.Q",
            },
        },
        "q8.xy.y180_DragCosine.pulse": {
            "operation": "control",
            "length": 28,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q8.xy.y180_DragCosine.wf.I",
                "Q": "q8.xy.y180_DragCosine.wf.Q",
            },
        },
        "q8.xy.y90_DragCosine.pulse": {
            "operation": "control",
            "length": 28,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q8.xy.y90_DragCosine.wf.I",
                "Q": "q8.xy.y90_DragCosine.wf.Q",
            },
        },
        "q8.xy.-y90_DragCosine.pulse": {
            "operation": "control",
            "length": 28,
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
            "samples": [0.0, 0.005635945982423489, 0.02223994862297123, 0.04891688184150544, 0.08422858526314811, 0.12627139581634475, 0.17277877470179662, 0.22124349708580268, 0.2690528172400154, 0.31362932233993973, 0.35256988145744067, 0.38377519897110557, 0.4055629881365775] + [0.4167586636003867] * 2 + [0.4055629881365775, 0.3837751989711056, 0.3525698814574407, 0.31362932233993984, 0.26905281724001545, 0.2212434970858028, 0.17277877470179653, 0.1262713958163448, 0.08422858526314818, 0.048916881841505486, 0.022239948622971253, 0.005635945982423443, 0.0],
        },
        "q1.xy.x180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 28,
        },
        "q1.xy.x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0028179729912117444, 0.011119974311485615, 0.02445844092075272, 0.042114292631574055, 0.06313569790817238, 0.08638938735089831, 0.11062174854290134, 0.1345264086200077, 0.15681466116996987, 0.17628494072872034, 0.19188759948555278, 0.20278149406828874] + [0.20837933180019336] * 2 + [0.20278149406828874, 0.1918875994855528, 0.17628494072872036, 0.15681466116996992, 0.13452640862000773, 0.1106217485429014, 0.08638938735089827, 0.0631356979081724, 0.04211429263157409, 0.024458440920752743, 0.011119974311485627, 0.0028179729912117214, 0.0],
        },
        "q1.xy.x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 28,
        },
        "q1.xy.-x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -0.0028179729912117444, -0.011119974311485615, -0.02445844092075272, -0.042114292631574055, -0.06313569790817238, -0.08638938735089831, -0.11062174854290134, -0.1345264086200077, -0.15681466116996987, -0.17628494072872034, -0.19188759948555278, -0.20278149406828874] + [-0.20837933180019336] * 2 + [-0.20278149406828874, -0.1918875994855528, -0.17628494072872036, -0.15681466116996992, -0.13452640862000773, -0.1106217485429014, -0.08638938735089827, -0.0631356979081724, -0.04211429263157409, -0.024458440920752743, -0.011119974311485627, -0.0028179729912117214, 0.0],
        },
        "q1.xy.-x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 3.4510216037711553e-19, 1.3618040947161651e-18, 2.995295138573446e-18, 5.157513366961213e-18, 7.731893035517754e-18, 1.0579648669957845e-17, 1.354725702691475e-17, 1.6474733571728132e-17, 1.9204257286118032e-17, 2.1588678840130823e-17, 2.3499453450605152e-17, 2.483357076370478e-17] + [2.5519108169757105e-17] * 2 + [2.483357076370478e-17, 2.3499453450605155e-17, 2.1588678840130826e-17, 1.920425728611804e-17, 1.6474733571728138e-17, 1.3547257026914758e-17, 1.057964866995784e-17, 7.731893035517758e-18, 5.157513366961217e-18, 2.995295138573449e-18, 1.3618040947161665e-18, 3.451021603771127e-19, 0.0],
        },
        "q1.xy.y180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 3.4510216037711553e-19, 1.3618040947161651e-18, 2.995295138573446e-18, 5.157513366961213e-18, 7.731893035517754e-18, 1.0579648669957845e-17, 1.354725702691475e-17, 1.6474733571728132e-17, 1.9204257286118032e-17, 2.1588678840130823e-17, 2.3499453450605152e-17, 2.483357076370478e-17] + [2.5519108169757105e-17] * 2 + [2.483357076370478e-17, 2.3499453450605155e-17, 2.1588678840130826e-17, 1.920425728611804e-17, 1.6474733571728138e-17, 1.3547257026914758e-17, 1.057964866995784e-17, 7.731893035517758e-18, 5.157513366961217e-18, 2.995295138573449e-18, 1.3618040947161665e-18, 3.451021603771127e-19, 0.0],
        },
        "q1.xy.y180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.005635945982423489, 0.02223994862297123, 0.04891688184150544, 0.08422858526314811, 0.12627139581634475, 0.17277877470179662, 0.22124349708580268, 0.2690528172400154, 0.31362932233993973, 0.35256988145744067, 0.38377519897110557, 0.4055629881365775] + [0.4167586636003867] * 2 + [0.4055629881365775, 0.3837751989711056, 0.3525698814574407, 0.31362932233993984, 0.26905281724001545, 0.2212434970858028, 0.17277877470179653, 0.1262713958163448, 0.08422858526314818, 0.048916881841505486, 0.022239948622971253, 0.005635945982423443, 0.0],
        },
        "q1.xy.y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 1.7255108018855777e-19, 6.809020473580826e-19, 1.497647569286723e-18, 2.5787566834806065e-18, 3.865946517758877e-18, 5.289824334978923e-18, 6.773628513457375e-18, 8.237366785864066e-18, 9.602128643059016e-18, 1.0794339420065411e-17, 1.1749726725302576e-17, 1.241678538185239e-17] + [1.2759554084878553e-17] * 2 + [1.241678538185239e-17, 1.1749726725302577e-17, 1.0794339420065413e-17, 9.60212864305902e-18, 8.237366785864069e-18, 6.773628513457379e-18, 5.28982433497892e-18, 3.865946517758879e-18, 2.5787566834806084e-18, 1.4976475692867245e-18, 6.809020473580832e-19, 1.7255108018855635e-19, 0.0],
        },
        "q1.xy.y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0028179729912117444, 0.011119974311485615, 0.02445844092075272, 0.042114292631574055, 0.06313569790817238, 0.08638938735089831, 0.11062174854290134, 0.1345264086200077, 0.15681466116996987, 0.17628494072872034, 0.19188759948555278, 0.20278149406828874] + [0.20837933180019336] * 2 + [0.20278149406828874, 0.1918875994855528, 0.17628494072872036, 0.15681466116996992, 0.13452640862000773, 0.1106217485429014, 0.08638938735089827, 0.0631356979081724, 0.04211429263157409, 0.024458440920752743, 0.011119974311485627, 0.0028179729912117214, 0.0],
        },
        "q1.xy.-y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 1.7255108018855777e-19, 6.809020473580826e-19, 1.497647569286723e-18, 2.5787566834806065e-18, 3.865946517758877e-18, 5.289824334978923e-18, 6.773628513457375e-18, 8.237366785864066e-18, 9.602128643059016e-18, 1.0794339420065411e-17, 1.1749726725302576e-17, 1.241678538185239e-17] + [1.2759554084878553e-17] * 2 + [1.241678538185239e-17, 1.1749726725302577e-17, 1.0794339420065413e-17, 9.60212864305902e-18, 8.237366785864069e-18, 6.773628513457379e-18, 5.28982433497892e-18, 3.865946517758879e-18, 2.5787566834806084e-18, 1.4976475692867245e-18, 6.809020473580832e-19, 1.7255108018855635e-19, 0.0],
        },
        "q1.xy.-y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.0028179729912117444, -0.011119974311485615, -0.02445844092075272, -0.042114292631574055, -0.06313569790817238, -0.08638938735089831, -0.11062174854290134, -0.1345264086200077, -0.15681466116996987, -0.17628494072872034, -0.19188759948555278, -0.20278149406828874] + [-0.20837933180019336] * 2 + [-0.20278149406828874, -0.1918875994855528, -0.17628494072872036, -0.15681466116996992, -0.13452640862000773, -0.1106217485429014, -0.08638938735089827, -0.0631356979081724, -0.04211429263157409, -0.024458440920752743, -0.011119974311485627, -0.0028179729912117214, 0.0],
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
            "sample": 0.058118024879361775,
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
        "q1.xy.cr_q2_q1_Square.wf.I": {
            "type": "constant",
            "sample": -0.059846006905785815,
        },
        "q1.xy.cr_q2_q1_Square.wf.Q": {
            "type": "constant",
            "sample": -0.08011526357338306,
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
            "sample": 0.1096393611252029,
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
            "samples": [0.0, 0.004417441222850343, 0.01743161949166544, 0.03834093708737901, 0.06601816728623099, 0.09897122344421723, 0.13542359777428006, 0.17341013334094038, 0.21088296617935126, 0.24582192617171267, 0.2763434449412238, 0.3008020995108196, 0.31787931748176634] + [0.3266544616129772] * 2 + [0.31787931748176634, 0.3008020995108196, 0.27634344494122387, 0.24582192617171278, 0.21088296617935134, 0.17341013334094044, 0.13542359777427998, 0.09897122344421729, 0.06601816728623104, 0.03834093708737905, 0.017431619491665457, 0.004417441222850306, 0.0],
        },
        "q2.xy.x180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 28,
        },
        "q2.xy.x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0022087206114251713, 0.00871580974583272, 0.019170468543689506, 0.03300908364311549, 0.049485611722108615, 0.06771179888714003, 0.08670506667047019, 0.10544148308967563, 0.12291096308585633, 0.1381717224706119, 0.1504010497554098, 0.15893965874088317] + [0.1633272308064886] * 2 + [0.15893965874088317, 0.1504010497554098, 0.13817172247061194, 0.12291096308585639, 0.10544148308967567, 0.08670506667047022, 0.06771179888713999, 0.04948561172210864, 0.03300908364311552, 0.019170468543689523, 0.008715809745832729, 0.002208720611425153, 0.0],
        },
        "q2.xy.x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 28,
        },
        "q2.xy.-x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -0.0022087206114251713, -0.00871580974583272, -0.019170468543689506, -0.03300908364311549, -0.049485611722108615, -0.06771179888714003, -0.08670506667047019, -0.10544148308967563, -0.12291096308585633, -0.1381717224706119, -0.1504010497554098, -0.15893965874088317] + [-0.1633272308064886] * 2 + [-0.15893965874088317, -0.1504010497554098, -0.13817172247061194, -0.12291096308585639, -0.10544148308967567, -0.08670506667047022, -0.06771179888713999, -0.04948561172210864, -0.03300908364311552, -0.019170468543689523, -0.008715809745832729, -0.002208720611425153, 0.0],
        },
        "q2.xy.-x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 2.704902626992621e-19, 1.0673788507211346e-18, 2.3477052940184377e-18, 4.0424468626328645e-18, 6.060239599932906e-18, 8.292303777164536e-18, 1.0618308236784918e-17, 1.2912857476312103e-17, 1.5052251752321246e-17, 1.6921155765631128e-17, 1.8418816417136443e-17, 1.946449443345952e-17] + [2.0001817042076722e-17] * 2 + [1.946449443345952e-17, 1.8418816417136443e-17, 1.692115576563113e-17, 1.5052251752321252e-17, 1.2912857476312108e-17, 1.0618308236784921e-17, 8.29230377716453e-18, 6.060239599932909e-18, 4.0424468626328675e-18, 2.3477052940184396e-18, 1.0673788507211358e-18, 2.7049026269925986e-19, 0.0],
        },
        "q2.xy.y180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 2.704902626992621e-19, 1.0673788507211346e-18, 2.3477052940184377e-18, 4.0424468626328645e-18, 6.060239599932906e-18, 8.292303777164536e-18, 1.0618308236784918e-17, 1.2912857476312103e-17, 1.5052251752321246e-17, 1.6921155765631128e-17, 1.8418816417136443e-17, 1.946449443345952e-17] + [2.0001817042076722e-17] * 2 + [1.946449443345952e-17, 1.8418816417136443e-17, 1.692115576563113e-17, 1.5052251752321252e-17, 1.2912857476312108e-17, 1.0618308236784921e-17, 8.29230377716453e-18, 6.060239599932909e-18, 4.0424468626328675e-18, 2.3477052940184396e-18, 1.0673788507211358e-18, 2.7049026269925986e-19, 0.0],
        },
        "q2.xy.y180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.004417441222850343, 0.01743161949166544, 0.03834093708737901, 0.06601816728623099, 0.09897122344421723, 0.13542359777428006, 0.17341013334094038, 0.21088296617935126, 0.24582192617171267, 0.2763434449412238, 0.3008020995108196, 0.31787931748176634] + [0.3266544616129772] * 2 + [0.31787931748176634, 0.3008020995108196, 0.27634344494122387, 0.24582192617171278, 0.21088296617935134, 0.17341013334094044, 0.13542359777427998, 0.09897122344421729, 0.06601816728623104, 0.03834093708737905, 0.017431619491665457, 0.004417441222850306, 0.0],
        },
        "q2.xy.y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 1.3524513134963104e-19, 5.336894253605673e-19, 1.1738526470092189e-18, 2.0212234313164322e-18, 3.030119799966453e-18, 4.146151888582268e-18, 5.309154118392459e-18, 6.456428738156052e-18, 7.526125876160623e-18, 8.460577882815564e-18, 9.209408208568222e-18, 9.73224721672976e-18] + [1.0000908521038361e-17] * 2 + [9.73224721672976e-18, 9.209408208568222e-18, 8.460577882815566e-18, 7.526125876160626e-18, 6.456428738156054e-18, 5.309154118392461e-18, 4.146151888582265e-18, 3.0301197999664545e-18, 2.0212234313164338e-18, 1.1738526470092198e-18, 5.336894253605679e-19, 1.3524513134962993e-19, 0.0],
        },
        "q2.xy.y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0022087206114251713, 0.00871580974583272, 0.019170468543689506, 0.03300908364311549, 0.049485611722108615, 0.06771179888714003, 0.08670506667047019, 0.10544148308967563, 0.12291096308585633, 0.1381717224706119, 0.1504010497554098, 0.15893965874088317] + [0.1633272308064886] * 2 + [0.15893965874088317, 0.1504010497554098, 0.13817172247061194, 0.12291096308585639, 0.10544148308967567, 0.08670506667047022, 0.06771179888713999, 0.04948561172210864, 0.03300908364311552, 0.019170468543689523, 0.008715809745832729, 0.002208720611425153, 0.0],
        },
        "q2.xy.-y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 1.3524513134963104e-19, 5.336894253605673e-19, 1.1738526470092189e-18, 2.0212234313164322e-18, 3.030119799966453e-18, 4.146151888582268e-18, 5.309154118392459e-18, 6.456428738156052e-18, 7.526125876160623e-18, 8.460577882815564e-18, 9.209408208568222e-18, 9.73224721672976e-18] + [1.0000908521038361e-17] * 2 + [9.73224721672976e-18, 9.209408208568222e-18, 8.460577882815566e-18, 7.526125876160626e-18, 6.456428738156054e-18, 5.309154118392461e-18, 4.146151888582265e-18, 3.0301197999664545e-18, 2.0212234313164338e-18, 1.1738526470092198e-18, 5.336894253605679e-19, 1.3524513134962993e-19, 0.0],
        },
        "q2.xy.-y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.0022087206114251713, -0.00871580974583272, -0.019170468543689506, -0.03300908364311549, -0.049485611722108615, -0.06771179888714003, -0.08670506667047019, -0.10544148308967563, -0.12291096308585633, -0.1381717224706119, -0.1504010497554098, -0.15893965874088317] + [-0.1633272308064886] * 2 + [-0.15893965874088317, -0.1504010497554098, -0.13817172247061194, -0.12291096308585639, -0.10544148308967567, -0.08670506667047022, -0.06771179888713999, -0.04948561172210864, -0.03300908364311552, -0.019170468543689523, -0.008715809745832729, -0.002208720611425153, 0.0],
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
            "sample": 0.03753181236700035,
        },
        "q2.xy.saturation.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q2.xy.cr_q1_q2_Square.wf.I": {
            "type": "constant",
            "sample": -0.059846006905785815,
        },
        "q2.xy.cr_q1_q2_Square.wf.Q": {
            "type": "constant",
            "sample": -0.08011526357338306,
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
            "sample": 0.0411256207067346,
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
            "samples": [0.0, 0.006413580743147028, 0.02530856517463152, 0.05566631979296777, 0.09585025018886931, 0.14369403027347044, 0.19661838947850938, 0.25177016190028273, 0.3061761012120285, 0.3569031691429978, 0.4012166563308202, 0.43672761121108145, 0.4615216290145186] + [0.474262057823656] * 2 + [0.4615216290145186, 0.4367276112110815, 0.40121665633082026, 0.35690316914299797, 0.3061761012120286, 0.25177016190028284, 0.19661838947850926, 0.1436940302734705, 0.09585025018886939, 0.055666319792967815, 0.025308565174631547, 0.006413580743146975, 0.0],
        },
        "q3.xy.x180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 28,
        },
        "q3.xy.x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.003206790371573514, 0.01265428258731576, 0.027833159896483883, 0.047925125094434654, 0.07184701513673522, 0.09830919473925469, 0.12588508095014136, 0.15308805060601424, 0.1784515845714989, 0.2006083281654101, 0.21836380560554072, 0.2307608145072593] + [0.237131028911828] * 2 + [0.2307608145072593, 0.21836380560554075, 0.20060832816541013, 0.17845158457149898, 0.1530880506060143, 0.12588508095014142, 0.09830919473925463, 0.07184701513673525, 0.047925125094434695, 0.027833159896483908, 0.012654282587315773, 0.0032067903715734874, 0.0],
        },
        "q3.xy.x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 28,
        },
        "q3.xy.-x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -0.003206790371573514, -0.01265428258731576, -0.027833159896483883, -0.047925125094434654, -0.07184701513673522, -0.09830919473925469, -0.12588508095014136, -0.15308805060601424, -0.1784515845714989, -0.2006083281654101, -0.21836380560554072, -0.2307608145072593] + [-0.237131028911828] * 2 + [-0.2307608145072593, -0.21836380560554075, -0.20060832816541013, -0.17845158457149898, -0.1530880506060143, -0.12588508095014142, -0.09830919473925463, -0.07184701513673525, -0.047925125094434695, -0.027833159896483908, -0.012654282587315773, -0.0032067903715734874, 0.0],
        },
        "q3.xy.-x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 3.927185564084055e-19, 1.5497026666062332e-18, 3.4085790177385466e-18, 5.869135104563589e-18, 8.798721711549422e-18, 1.2039404066418207e-17, 1.5416476144599607e-17, 1.8747879116236335e-17, 2.1854016184825934e-17, 2.456743469700713e-17, 2.674185355844603e-17, 2.826004928549512e-17] + [2.9040175553538864e-17] * 2 + [2.826004928549512e-17, 2.6741853558446034e-17, 2.4567434697007133e-17, 2.1854016184825943e-17, 1.8747879116236344e-17, 1.5416476144599613e-17, 1.20394040664182e-17, 8.798721711549426e-18, 5.869135104563594e-18, 3.4085790177385493e-18, 1.549702666606235e-18, 3.927185564084023e-19, 0.0],
        },
        "q3.xy.y180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 3.927185564084055e-19, 1.5497026666062332e-18, 3.4085790177385466e-18, 5.869135104563589e-18, 8.798721711549422e-18, 1.2039404066418207e-17, 1.5416476144599607e-17, 1.8747879116236335e-17, 2.1854016184825934e-17, 2.456743469700713e-17, 2.674185355844603e-17, 2.826004928549512e-17] + [2.9040175553538864e-17] * 2 + [2.826004928549512e-17, 2.6741853558446034e-17, 2.4567434697007133e-17, 2.1854016184825943e-17, 1.8747879116236344e-17, 1.5416476144599613e-17, 1.20394040664182e-17, 8.798721711549426e-18, 5.869135104563594e-18, 3.4085790177385493e-18, 1.549702666606235e-18, 3.927185564084023e-19, 0.0],
        },
        "q3.xy.y180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.006413580743147028, 0.02530856517463152, 0.05566631979296777, 0.09585025018886931, 0.14369403027347044, 0.19661838947850938, 0.25177016190028273, 0.3061761012120285, 0.3569031691429978, 0.4012166563308202, 0.43672761121108145, 0.4615216290145186] + [0.474262057823656] * 2 + [0.4615216290145186, 0.4367276112110815, 0.40121665633082026, 0.35690316914299797, 0.3061761012120286, 0.25177016190028284, 0.19661838947850926, 0.1436940302734705, 0.09585025018886939, 0.055666319792967815, 0.025308565174631547, 0.006413580743146975, 0.0],
        },
        "q3.xy.y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 1.9635927820420276e-19, 7.748513333031166e-19, 1.7042895088692733e-18, 2.9345675522817945e-18, 4.399360855774711e-18, 6.019702033209104e-18, 7.708238072299803e-18, 9.373939558118168e-18, 1.0927008092412967e-17, 1.2283717348503565e-17, 1.3370926779223015e-17, 1.413002464274756e-17] + [1.4520087776769432e-17] * 2 + [1.413002464274756e-17, 1.3370926779223017e-17, 1.2283717348503567e-17, 1.0927008092412972e-17, 9.373939558118172e-18, 7.708238072299806e-18, 6.0197020332091e-18, 4.399360855774713e-18, 2.934567552281797e-18, 1.7042895088692746e-18, 7.748513333031175e-19, 1.9635927820420115e-19, 0.0],
        },
        "q3.xy.y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.003206790371573514, 0.01265428258731576, 0.027833159896483883, 0.047925125094434654, 0.07184701513673522, 0.09830919473925469, 0.12588508095014136, 0.15308805060601424, 0.1784515845714989, 0.2006083281654101, 0.21836380560554072, 0.2307608145072593] + [0.237131028911828] * 2 + [0.2307608145072593, 0.21836380560554075, 0.20060832816541013, 0.17845158457149898, 0.1530880506060143, 0.12588508095014142, 0.09830919473925463, 0.07184701513673525, 0.047925125094434695, 0.027833159896483908, 0.012654282587315773, 0.0032067903715734874, 0.0],
        },
        "q3.xy.-y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 1.9635927820420276e-19, 7.748513333031166e-19, 1.7042895088692733e-18, 2.9345675522817945e-18, 4.399360855774711e-18, 6.019702033209104e-18, 7.708238072299803e-18, 9.373939558118168e-18, 1.0927008092412967e-17, 1.2283717348503565e-17, 1.3370926779223015e-17, 1.413002464274756e-17] + [1.4520087776769432e-17] * 2 + [1.413002464274756e-17, 1.3370926779223017e-17, 1.2283717348503567e-17, 1.0927008092412972e-17, 9.373939558118172e-18, 7.708238072299806e-18, 6.0197020332091e-18, 4.399360855774713e-18, 2.934567552281797e-18, 1.7042895088692746e-18, 7.748513333031175e-19, 1.9635927820420115e-19, 0.0],
        },
        "q3.xy.-y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.003206790371573514, -0.01265428258731576, -0.027833159896483883, -0.047925125094434654, -0.07184701513673522, -0.09830919473925469, -0.12588508095014136, -0.15308805060601424, -0.1784515845714989, -0.2006083281654101, -0.21836380560554072, -0.2307608145072593] + [-0.237131028911828] * 2 + [-0.2307608145072593, -0.21836380560554075, -0.20060832816541013, -0.17845158457149898, -0.1530880506060143, -0.12588508095014142, -0.09830919473925463, -0.07184701513673525, -0.047925125094434695, -0.027833159896483908, -0.012654282587315773, -0.0032067903715734874, 0.0],
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
            "sample": 0.05274791552973862,
        },
        "q3.xy.saturation.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q3.xy.cr_q2_q3_Square.wf.I": {
            "type": "constant",
            "sample": 0.13899999999999998,
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
            "sample": 0.34565678375741143,
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
            "samples": [0.0, 0.006209627188159414, 0.024503746143621857, 0.0538961161782422, 0.09280218701552259, 0.1391245223061642, 0.19036587296455895, 0.2437638045133835, 0.29643962064130136, 0.3455535544662295, 0.38845786110299835, 0.4228395582754537, 0.44684511978965796] + [0.4591803996107723] * 2 + [0.44684511978965796, 0.4228395582754538, 0.3884578611029984, 0.34555355446622965, 0.2964396206413014, 0.24376380451338361, 0.19036587296455884, 0.1391245223061643, 0.09280218701552267, 0.05389611617824225, 0.02450374614362188, 0.006209627188159363, 0.0],
        },
        "q4.xy.x180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 28,
        },
        "q4.xy.x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.003104813594079707, 0.012251873071810929, 0.0269480580891211, 0.046401093507761296, 0.0695622611530821, 0.09518293648227948, 0.12188190225669175, 0.14821981032065068, 0.17277677723311474, 0.19422893055149917, 0.21141977913772686, 0.22342255989482898] + [0.22959019980538614] * 2 + [0.22342255989482898, 0.2114197791377269, 0.1942289305514992, 0.17277677723311483, 0.1482198103206507, 0.12188190225669181, 0.09518293648227942, 0.06956226115308214, 0.04640109350776134, 0.026948058089121124, 0.01225187307181094, 0.0031048135940796814, 0.0],
        },
        "q4.xy.x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 28,
        },
        "q4.xy.-x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -0.003104813594079707, -0.012251873071810929, -0.0269480580891211, -0.046401093507761296, -0.0695622611530821, -0.09518293648227948, -0.12188190225669175, -0.14821981032065068, -0.17277677723311474, -0.19422893055149917, -0.21141977913772686, -0.22342255989482898] + [-0.22959019980538614] * 2 + [-0.22342255989482898, -0.2114197791377269, -0.1942289305514992, -0.17277677723311483, -0.1482198103206507, -0.12188190225669181, -0.09518293648227942, -0.06956226115308214, -0.04640109350776134, -0.026948058089121124, -0.01225187307181094, -0.0031048135940796814, 0.0],
        },
        "q4.xy.-x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 3.8023000299389026e-19, 1.5004217140952903e-18, 3.3001853082079094e-18, 5.68249506412169e-18, 8.518920046257427e-18, 1.165654784964694e-17, 1.492622814726481e-17, 1.815169162794127e-17, 2.1159052720552927e-17, 2.3786183810170702e-17, 2.5891455579745755e-17, 2.736137228325101e-17] + [2.811669033072674e-17] * 2 + [2.736137228325101e-17, 2.589145557974576e-17, 2.3786183810170705e-17, 2.1159052720552936e-17, 1.8151691627941272e-17, 1.4926228147264817e-17, 1.1656547849646932e-17, 8.518920046257432e-18, 5.6824950641216956e-18, 3.3001853082079125e-18, 1.5004217140952918e-18, 3.8023000299388713e-19, 0.0],
        },
        "q4.xy.y180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 3.8023000299389026e-19, 1.5004217140952903e-18, 3.3001853082079094e-18, 5.68249506412169e-18, 8.518920046257427e-18, 1.165654784964694e-17, 1.492622814726481e-17, 1.815169162794127e-17, 2.1159052720552927e-17, 2.3786183810170702e-17, 2.5891455579745755e-17, 2.736137228325101e-17] + [2.811669033072674e-17] * 2 + [2.736137228325101e-17, 2.589145557974576e-17, 2.3786183810170705e-17, 2.1159052720552936e-17, 1.8151691627941272e-17, 1.4926228147264817e-17, 1.1656547849646932e-17, 8.518920046257432e-18, 5.6824950641216956e-18, 3.3001853082079125e-18, 1.5004217140952918e-18, 3.8023000299388713e-19, 0.0],
        },
        "q4.xy.y180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.006209627188159414, 0.024503746143621857, 0.0538961161782422, 0.09280218701552259, 0.1391245223061642, 0.19036587296455895, 0.2437638045133835, 0.29643962064130136, 0.3455535544662295, 0.38845786110299835, 0.4228395582754537, 0.44684511978965796] + [0.4591803996107723] * 2 + [0.44684511978965796, 0.4228395582754538, 0.3884578611029984, 0.34555355446622965, 0.2964396206413014, 0.24376380451338361, 0.19036587296455884, 0.1391245223061643, 0.09280218701552267, 0.05389611617824225, 0.02450374614362188, 0.006209627188159363, 0.0],
        },
        "q4.xy.y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 1.9011500149694513e-19, 7.502108570476451e-19, 1.6500926541039547e-18, 2.841247532060845e-18, 4.259460023128714e-18, 5.82827392482347e-18, 7.463114073632406e-18, 9.075845813970635e-18, 1.0579526360276463e-17, 1.1893091905085351e-17, 1.2945727789872878e-17, 1.3680686141625505e-17] + [1.405834516536337e-17] * 2 + [1.3680686141625505e-17, 1.294572778987288e-17, 1.1893091905085352e-17, 1.0579526360276468e-17, 9.075845813970636e-18, 7.463114073632409e-18, 5.828273924823466e-18, 4.259460023128716e-18, 2.8412475320608478e-18, 1.6500926541039563e-18, 7.502108570476459e-19, 1.9011500149694357e-19, 0.0],
        },
        "q4.xy.y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.003104813594079707, 0.012251873071810929, 0.0269480580891211, 0.046401093507761296, 0.0695622611530821, 0.09518293648227948, 0.12188190225669175, 0.14821981032065068, 0.17277677723311474, 0.19422893055149917, 0.21141977913772686, 0.22342255989482898] + [0.22959019980538614] * 2 + [0.22342255989482898, 0.2114197791377269, 0.1942289305514992, 0.17277677723311483, 0.1482198103206507, 0.12188190225669181, 0.09518293648227942, 0.06956226115308214, 0.04640109350776134, 0.026948058089121124, 0.01225187307181094, 0.0031048135940796814, 0.0],
        },
        "q4.xy.-y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 1.9011500149694513e-19, 7.502108570476451e-19, 1.6500926541039547e-18, 2.841247532060845e-18, 4.259460023128714e-18, 5.82827392482347e-18, 7.463114073632406e-18, 9.075845813970635e-18, 1.0579526360276463e-17, 1.1893091905085351e-17, 1.2945727789872878e-17, 1.3680686141625505e-17] + [1.405834516536337e-17] * 2 + [1.3680686141625505e-17, 1.294572778987288e-17, 1.1893091905085352e-17, 1.0579526360276468e-17, 9.075845813970636e-18, 7.463114073632409e-18, 5.828273924823466e-18, 4.259460023128716e-18, 2.8412475320608478e-18, 1.6500926541039563e-18, 7.502108570476459e-19, 1.9011500149694357e-19, 0.0],
        },
        "q4.xy.-y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.003104813594079707, -0.012251873071810929, -0.0269480580891211, -0.046401093507761296, -0.0695622611530821, -0.09518293648227948, -0.12188190225669175, -0.14821981032065068, -0.17277677723311474, -0.19422893055149917, -0.21141977913772686, -0.22342255989482898] + [-0.22959019980538614] * 2 + [-0.22342255989482898, -0.2114197791377269, -0.1942289305514992, -0.17277677723311483, -0.1482198103206507, -0.12188190225669181, -0.09518293648227942, -0.06956226115308214, -0.04640109350776134, -0.026948058089121124, -0.01225187307181094, -0.0031048135940796814, 0.0],
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
            "sample": 0.07562669833799542,
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
            "sample": 0.04727070176547587,
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
            "samples": [0.0, 0.004491496794801091, 0.017723849424415995, 0.03898369833351539, 0.06712491956450292, 0.10063041259673244, 0.13769388762826282, 0.17631724312662136, 0.21441828399960858, 0.24994297327167483, 0.2809761657489401, 0.30584485399231237, 0.32320836058157154] + [0.3321306143821144] * 2 + [0.32320836058157154, 0.3058448539923124, 0.28097616574894013, 0.24994297327167495, 0.21441828399960866, 0.17631724312662142, 0.13769388762826276, 0.1006304125967325, 0.06712491956450298, 0.03898369833351543, 0.017723849424416013, 0.004491496794801053, 0.0],
        },
        "q5.xy.x180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 28,
        },
        "q5.xy.x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0022457483974005453, 0.008861924712207998, 0.019491849166757697, 0.03356245978225146, 0.05031520629836622, 0.06884694381413141, 0.08815862156331068, 0.10720914199980429, 0.12497148663583742, 0.14048808287447004, 0.15292242699615619, 0.16160418029078577] + [0.1660653071910572] * 2 + [0.16160418029078577, 0.1529224269961562, 0.14048808287447007, 0.12497148663583747, 0.10720914199980433, 0.08815862156331071, 0.06884694381413138, 0.05031520629836625, 0.03356245978225149, 0.019491849166757714, 0.008861924712208006, 0.0022457483974005267, 0.0],
        },
        "q5.xy.x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 28,
        },
        "q5.xy.-x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -0.0022457483974005453, -0.008861924712207998, -0.019491849166757697, -0.03356245978225146, -0.05031520629836622, -0.06884694381413141, -0.08815862156331068, -0.10720914199980429, -0.12497148663583742, -0.14048808287447004, -0.15292242699615619, -0.16160418029078577] + [-0.1660653071910572] * 2 + [-0.16160418029078577, -0.1529224269961562, -0.14048808287447007, -0.12497148663583747, -0.10720914199980433, -0.08815862156331071, -0.06884694381413138, -0.05031520629836625, -0.03356245978225149, -0.019491849166757714, -0.008861924712208006, -0.0022457483974005267, 0.0],
        },
        "q5.xy.-x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 2.750248586566876e-19, 1.0852727733090353e-18, 2.3870630691532816e-18, 4.1102158943846024e-18, 6.161835634173294e-18, 8.43131893730537e-18, 1.0796317371475125e-17, 1.3129333258939439e-17, 1.530459310932645e-17, 1.720482810105678e-17, 1.8727596073868748e-17, 1.9790804212194258e-17] + [2.0337134690095013e-17] * 2 + [1.9790804212194258e-17, 1.872759607386875e-17, 1.7204828101056784e-17, 1.5304593109326458e-17, 1.3129333258939444e-17, 1.079631737147513e-17, 8.431318937305367e-18, 6.161835634173297e-18, 4.1102158943846055e-18, 2.387063069153284e-18, 1.0852727733090364e-18, 2.7502485865668533e-19, 0.0],
        },
        "q5.xy.y180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 2.750248586566876e-19, 1.0852727733090353e-18, 2.3870630691532816e-18, 4.1102158943846024e-18, 6.161835634173294e-18, 8.43131893730537e-18, 1.0796317371475125e-17, 1.3129333258939439e-17, 1.530459310932645e-17, 1.720482810105678e-17, 1.8727596073868748e-17, 1.9790804212194258e-17] + [2.0337134690095013e-17] * 2 + [1.9790804212194258e-17, 1.872759607386875e-17, 1.7204828101056784e-17, 1.5304593109326458e-17, 1.3129333258939444e-17, 1.079631737147513e-17, 8.431318937305367e-18, 6.161835634173297e-18, 4.1102158943846055e-18, 2.387063069153284e-18, 1.0852727733090364e-18, 2.7502485865668533e-19, 0.0],
        },
        "q5.xy.y180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.004491496794801091, 0.017723849424415995, 0.03898369833351539, 0.06712491956450292, 0.10063041259673244, 0.13769388762826282, 0.17631724312662136, 0.21441828399960858, 0.24994297327167483, 0.2809761657489401, 0.30584485399231237, 0.32320836058157154] + [0.3321306143821144] * 2 + [0.32320836058157154, 0.3058448539923124, 0.28097616574894013, 0.24994297327167495, 0.21441828399960866, 0.17631724312662142, 0.13769388762826276, 0.1006304125967325, 0.06712491956450298, 0.03898369833351543, 0.017723849424416013, 0.004491496794801053, 0.0],
        },
        "q5.xy.y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 1.375124293283438e-19, 5.426363866545176e-19, 1.1935315345766408e-18, 2.0551079471923012e-18, 3.080917817086647e-18, 4.215659468652685e-18, 5.3981586857375626e-18, 6.5646666294697195e-18, 7.652296554663226e-18, 8.60241405052839e-18, 9.363798036934374e-18, 9.895402106097129e-18] + [1.0168567345047506e-17] * 2 + [9.895402106097129e-18, 9.363798036934376e-18, 8.602414050528392e-18, 7.652296554663229e-18, 6.564666629469722e-18, 5.398158685737565e-18, 4.215659468652683e-18, 3.0809178170866486e-18, 2.0551079471923027e-18, 1.193531534576642e-18, 5.426363866545182e-19, 1.3751242932834267e-19, 0.0],
        },
        "q5.xy.y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0022457483974005453, 0.008861924712207998, 0.019491849166757697, 0.03356245978225146, 0.05031520629836622, 0.06884694381413141, 0.08815862156331068, 0.10720914199980429, 0.12497148663583742, 0.14048808287447004, 0.15292242699615619, 0.16160418029078577] + [0.1660653071910572] * 2 + [0.16160418029078577, 0.1529224269961562, 0.14048808287447007, 0.12497148663583747, 0.10720914199980433, 0.08815862156331071, 0.06884694381413138, 0.05031520629836625, 0.03356245978225149, 0.019491849166757714, 0.008861924712208006, 0.0022457483974005267, 0.0],
        },
        "q5.xy.-y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 1.375124293283438e-19, 5.426363866545176e-19, 1.1935315345766408e-18, 2.0551079471923012e-18, 3.080917817086647e-18, 4.215659468652685e-18, 5.3981586857375626e-18, 6.5646666294697195e-18, 7.652296554663226e-18, 8.60241405052839e-18, 9.363798036934374e-18, 9.895402106097129e-18] + [1.0168567345047506e-17] * 2 + [9.895402106097129e-18, 9.363798036934376e-18, 8.602414050528392e-18, 7.652296554663229e-18, 6.564666629469722e-18, 5.398158685737565e-18, 4.215659468652683e-18, 3.0809178170866486e-18, 2.0551079471923027e-18, 1.193531534576642e-18, 5.426363866545182e-19, 1.3751242932834267e-19, 0.0],
        },
        "q5.xy.-y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.0022457483974005453, -0.008861924712207998, -0.019491849166757697, -0.03356245978225146, -0.05031520629836622, -0.06884694381413141, -0.08815862156331068, -0.10720914199980429, -0.12497148663583742, -0.14048808287447004, -0.15292242699615619, -0.16160418029078577] + [-0.1660653071910572] * 2 + [-0.16160418029078577, -0.1529224269961562, -0.14048808287447007, -0.12497148663583747, -0.10720914199980433, -0.08815862156331071, -0.06884694381413138, -0.05031520629836625, -0.03356245978225149, -0.019491849166757714, -0.008861924712208006, -0.0022457483974005267, 0.0],
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
            "sample": 0.0465830919328653,
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
            "sample": 0.05116362917943104,
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
            "samples": [0.0, 0.005479424617822204, 0.02162230127184579, 0.04755836330322451, 0.08188939089454725, 0.12276458946211057, 0.1679803664709863, 0.21509912767895834, 0.26158068847306815, 0.3049192158796016, 0.34277831866831293, 0.3731170028083991, 0.3942997019849924] + [0.40518445140254544] * 2 + [0.3942997019849924, 0.3731170028083991, 0.34277831866831293, 0.3049192158796017, 0.2615806884730682, 0.21509912767895842, 0.16798036647098621, 0.12276458946211063, 0.08188939089454732, 0.04755836330322455, 0.021622301271845813, 0.005479424617822159, 0.0],
        },
        "q6.xy.x180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 28,
        },
        "q6.xy.x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.002739712308911102, 0.010811150635922894, 0.023779181651612254, 0.040944695447273624, 0.06138229473105528, 0.08399018323549315, 0.10754956383947917, 0.13079034423653407, 0.1524596079398008, 0.17138915933415647, 0.18655850140419955, 0.1971498509924962] + [0.20259222570127272] * 2 + [0.1971498509924962, 0.18655850140419955, 0.17138915933415647, 0.15245960793980085, 0.1307903442365341, 0.10754956383947921, 0.08399018323549311, 0.06138229473105532, 0.04094469544727366, 0.023779181651612274, 0.010811150635922907, 0.0027397123089110795, 0.0],
        },
        "q6.xy.x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 28,
        },
        "q6.xy.-x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -0.002739712308911102, -0.010811150635922894, -0.023779181651612254, -0.040944695447273624, -0.06138229473105528, -0.08399018323549315, -0.10754956383947917, -0.13079034423653407, -0.1524596079398008, -0.17138915933415647, -0.18655850140419955, -0.1971498509924962] + [-0.20259222570127272] * 2 + [-0.1971498509924962, -0.18655850140419955, -0.17138915933415647, -0.15245960793980085, -0.1307903442365341, -0.10754956383947921, -0.08399018323549311, -0.06138229473105532, -0.04094469544727366, -0.023779181651612274, -0.010811150635922907, -0.0027397123089110795, 0.0],
        },
        "q6.xy.-x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 3.355179909692586e-19, 1.3239841021382845e-18, 2.912109869599042e-18, 5.014279022156685e-18, 7.51716307667063e-18, 1.0285830905914637e-17, 1.3171022910571209e-17, 1.6017197642865192e-17, 1.8670917086273743e-17, 2.0989118538713044e-17, 2.2846827159837997e-17, 2.4143893397033812e-17] + [2.481039207372018e-17] * 2 + [2.4143893397033812e-17, 2.2846827159837997e-17, 2.0989118538713044e-17, 1.867091708627375e-17, 1.6017197642865195e-17, 1.3171022910571213e-17, 1.0285830905914632e-17, 7.517163076670633e-18, 5.014279022156689e-18, 2.9121098695990443e-18, 1.323984102138286e-18, 3.355179909692558e-19, 0.0],
        },
        "q6.xy.y180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 3.355179909692586e-19, 1.3239841021382845e-18, 2.912109869599042e-18, 5.014279022156685e-18, 7.51716307667063e-18, 1.0285830905914637e-17, 1.3171022910571209e-17, 1.6017197642865192e-17, 1.8670917086273743e-17, 2.0989118538713044e-17, 2.2846827159837997e-17, 2.4143893397033812e-17] + [2.481039207372018e-17] * 2 + [2.4143893397033812e-17, 2.2846827159837997e-17, 2.0989118538713044e-17, 1.867091708627375e-17, 1.6017197642865195e-17, 1.3171022910571213e-17, 1.0285830905914632e-17, 7.517163076670633e-18, 5.014279022156689e-18, 2.9121098695990443e-18, 1.323984102138286e-18, 3.355179909692558e-19, 0.0],
        },
        "q6.xy.y180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.005479424617822204, 0.02162230127184579, 0.04755836330322451, 0.08188939089454725, 0.12276458946211057, 0.1679803664709863, 0.21509912767895834, 0.26158068847306815, 0.3049192158796016, 0.34277831866831293, 0.3731170028083991, 0.3942997019849924] + [0.40518445140254544] * 2 + [0.3942997019849924, 0.3731170028083991, 0.34277831866831293, 0.3049192158796017, 0.2615806884730682, 0.21509912767895842, 0.16798036647098621, 0.12276458946211063, 0.08188939089454732, 0.04755836330322455, 0.021622301271845813, 0.005479424617822159, 0.0],
        },
        "q6.xy.y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 1.677589954846293e-19, 6.619920510691423e-19, 1.456054934799521e-18, 2.5071395110783426e-18, 3.758581538335315e-18, 5.142915452957318e-18, 6.585511455285604e-18, 8.008598821432596e-18, 9.335458543136871e-18, 1.0494559269356522e-17, 1.1423413579918998e-17, 1.2071946698516906e-17] + [1.240519603686009e-17] * 2 + [1.2071946698516906e-17, 1.1423413579918998e-17, 1.0494559269356522e-17, 9.335458543136874e-18, 8.008598821432598e-18, 6.5855114552856066e-18, 5.142915452957316e-18, 3.7585815383353166e-18, 2.5071395110783445e-18, 1.4560549347995221e-18, 6.61992051069143e-19, 1.677589954846279e-19, 0.0],
        },
        "q6.xy.y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.002739712308911102, 0.010811150635922894, 0.023779181651612254, 0.040944695447273624, 0.06138229473105528, 0.08399018323549315, 0.10754956383947917, 0.13079034423653407, 0.1524596079398008, 0.17138915933415647, 0.18655850140419955, 0.1971498509924962] + [0.20259222570127272] * 2 + [0.1971498509924962, 0.18655850140419955, 0.17138915933415647, 0.15245960793980085, 0.1307903442365341, 0.10754956383947921, 0.08399018323549311, 0.06138229473105532, 0.04094469544727366, 0.023779181651612274, 0.010811150635922907, 0.0027397123089110795, 0.0],
        },
        "q6.xy.-y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 1.677589954846293e-19, 6.619920510691423e-19, 1.456054934799521e-18, 2.5071395110783426e-18, 3.758581538335315e-18, 5.142915452957318e-18, 6.585511455285604e-18, 8.008598821432596e-18, 9.335458543136871e-18, 1.0494559269356522e-17, 1.1423413579918998e-17, 1.2071946698516906e-17] + [1.240519603686009e-17] * 2 + [1.2071946698516906e-17, 1.1423413579918998e-17, 1.0494559269356522e-17, 9.335458543136874e-18, 8.008598821432598e-18, 6.5855114552856066e-18, 5.142915452957316e-18, 3.7585815383353166e-18, 2.5071395110783445e-18, 1.4560549347995221e-18, 6.61992051069143e-19, 1.677589954846279e-19, 0.0],
        },
        "q6.xy.-y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.002739712308911102, -0.010811150635922894, -0.023779181651612254, -0.040944695447273624, -0.06138229473105528, -0.08399018323549315, -0.10754956383947917, -0.13079034423653407, -0.1524596079398008, -0.17138915933415647, -0.18655850140419955, -0.1971498509924962] + [-0.20259222570127272] * 2 + [-0.1971498509924962, -0.18655850140419955, -0.17138915933415647, -0.15245960793980085, -0.1307903442365341, -0.10754956383947921, -0.08399018323549311, -0.06138229473105532, -0.04094469544727366, -0.023779181651612274, -0.010811150635922907, -0.0027397123089110795, 0.0],
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
            "sample": 0.053813886347604395,
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
            "sample": 0.09594356747997401,
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
            "samples": [0.0, 0.0012146810013134736, 0.00479324023806462, 0.010542756655524661, 0.01815327233542146, 0.027214502407543226, 0.03723795361328989, 0.04768325910368601, 0.05798730975607778, 0.06759461153269064, 0.07598723230799004, 0.08271272372363064, 0.08740851279656674] + [0.0898214483224166] * 2 + [0.08740851279656674, 0.08271272372363066, 0.07598723230799005, 0.06759461153269067, 0.0579873097560778, 0.04768325910368603, 0.03723795361328987, 0.027214502407543244, 0.018153272335421473, 0.01054275665552467, 0.004793240238064625, 0.0012146810013134637, 0.0],
        },
        "q7.xy.x180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 28,
        },
        "q7.xy.x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0006073405006567368, 0.00239662011903231, 0.0052713783277623305, 0.00907663616771073, 0.013607251203771613, 0.018618976806644944, 0.023841629551843005, 0.02899365487803889, 0.03379730576634532, 0.03799361615399502, 0.04135636186181532, 0.04370425639828337] + [0.0449107241612083] * 2 + [0.04370425639828337, 0.04135636186181533, 0.037993616153995026, 0.033797305766345334, 0.0289936548780389, 0.023841629551843015, 0.018618976806644934, 0.013607251203771622, 0.009076636167710737, 0.005271378327762335, 0.0023966201190323126, 0.0006073405006567318, 0.0],
        },
        "q7.xy.x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 28,
        },
        "q7.xy.-x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -0.0006073405006567368, -0.00239662011903231, -0.0052713783277623305, -0.00907663616771073, -0.013607251203771613, -0.018618976806644944, -0.023841629551843005, -0.02899365487803889, -0.03379730576634532, -0.03799361615399502, -0.04135636186181532, -0.04370425639828337] + [-0.0449107241612083] * 2 + [-0.04370425639828337, -0.04135636186181533, -0.037993616153995026, -0.033797305766345334, -0.0289936548780389, -0.023841629551843015, -0.018618976806644934, -0.013607251203771622, -0.009076636167710737, -0.005271378327762335, -0.0023966201190323126, -0.0006073405006567318, 0.0],
        },
        "q7.xy.-x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 7.437776001218238e-20, 2.935013157545067e-19, 6.455576596188865e-19, 1.1115673429812044e-18, 1.6664076631892876e-18, 2.280167034965654e-18, 2.919757531712148e-18, 3.550698664197337e-18, 4.138976232655918e-18, 4.652876041102317e-18, 5.064693617845181e-18, 5.3522277707272955e-18] + [5.499977459141345e-18] * 2 + [5.3522277707272955e-18, 5.064693617845182e-18, 4.652876041102318e-18, 4.13897623265592e-18, 3.550698664197338e-18, 2.9197575317121495e-18, 2.2801670349656525e-18, 1.6664076631892885e-18, 1.1115673429812052e-18, 6.455576596188871e-19, 2.93501315754507e-19, 7.437776001218176e-20, 0.0],
        },
        "q7.xy.y180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 7.437776001218238e-20, 2.935013157545067e-19, 6.455576596188865e-19, 1.1115673429812044e-18, 1.6664076631892876e-18, 2.280167034965654e-18, 2.919757531712148e-18, 3.550698664197337e-18, 4.138976232655918e-18, 4.652876041102317e-18, 5.064693617845181e-18, 5.3522277707272955e-18] + [5.499977459141345e-18] * 2 + [5.3522277707272955e-18, 5.064693617845182e-18, 4.652876041102318e-18, 4.13897623265592e-18, 3.550698664197338e-18, 2.9197575317121495e-18, 2.2801670349656525e-18, 1.6664076631892885e-18, 1.1115673429812052e-18, 6.455576596188871e-19, 2.93501315754507e-19, 7.437776001218176e-20, 0.0],
        },
        "q7.xy.y180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0012146810013134736, 0.00479324023806462, 0.010542756655524661, 0.01815327233542146, 0.027214502407543226, 0.03723795361328989, 0.04768325910368601, 0.05798730975607778, 0.06759461153269064, 0.07598723230799004, 0.08271272372363064, 0.08740851279656674] + [0.0898214483224166] * 2 + [0.08740851279656674, 0.08271272372363066, 0.07598723230799005, 0.06759461153269067, 0.0579873097560778, 0.04768325910368603, 0.03723795361328987, 0.027214502407543244, 0.018153272335421473, 0.01054275665552467, 0.004793240238064625, 0.0012146810013134637, 0.0],
        },
        "q7.xy.y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 3.718888000609119e-20, 1.4675065787725336e-19, 3.2277882980944326e-19, 5.557836714906022e-19, 8.332038315946438e-19, 1.140083517482827e-18, 1.459878765856074e-18, 1.7753493320986683e-18, 2.069488116327959e-18, 2.3264380205511587e-18, 2.5323468089225905e-18, 2.6761138853636477e-18] + [2.7499887295706724e-18] * 2 + [2.6761138853636477e-18, 2.532346808922591e-18, 2.326438020551159e-18, 2.06948811632796e-18, 1.775349332098669e-18, 1.4598787658560747e-18, 1.1400835174828263e-18, 8.332038315946443e-19, 5.557836714906026e-19, 3.2277882980944355e-19, 1.467506578772535e-19, 3.718888000609088e-20, 0.0],
        },
        "q7.xy.y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0006073405006567368, 0.00239662011903231, 0.0052713783277623305, 0.00907663616771073, 0.013607251203771613, 0.018618976806644944, 0.023841629551843005, 0.02899365487803889, 0.03379730576634532, 0.03799361615399502, 0.04135636186181532, 0.04370425639828337] + [0.0449107241612083] * 2 + [0.04370425639828337, 0.04135636186181533, 0.037993616153995026, 0.033797305766345334, 0.0289936548780389, 0.023841629551843015, 0.018618976806644934, 0.013607251203771622, 0.009076636167710737, 0.005271378327762335, 0.0023966201190323126, 0.0006073405006567318, 0.0],
        },
        "q7.xy.-y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 3.718888000609119e-20, 1.4675065787725336e-19, 3.2277882980944326e-19, 5.557836714906022e-19, 8.332038315946438e-19, 1.140083517482827e-18, 1.459878765856074e-18, 1.7753493320986683e-18, 2.069488116327959e-18, 2.3264380205511587e-18, 2.5323468089225905e-18, 2.6761138853636477e-18] + [2.7499887295706724e-18] * 2 + [2.6761138853636477e-18, 2.532346808922591e-18, 2.326438020551159e-18, 2.06948811632796e-18, 1.775349332098669e-18, 1.4598787658560747e-18, 1.1400835174828263e-18, 8.332038315946443e-19, 5.557836714906026e-19, 3.2277882980944355e-19, 1.467506578772535e-19, 3.718888000609088e-20, 0.0],
        },
        "q7.xy.-y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.0006073405006567368, -0.00239662011903231, -0.0052713783277623305, -0.00907663616771073, -0.013607251203771613, -0.018618976806644944, -0.023841629551843005, -0.02899365487803889, -0.03379730576634532, -0.03799361615399502, -0.04135636186181532, -0.04370425639828337] + [-0.0449107241612083] * 2 + [-0.04370425639828337, -0.04135636186181533, -0.037993616153995026, -0.033797305766345334, -0.0289936548780389, -0.023841629551843015, -0.018618976806644934, -0.013607251203771622, -0.009076636167710737, -0.005271378327762335, -0.0023966201190323126, -0.0006073405006567318, 0.0],
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
            "sample": 0.014047598378514256,
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
            "sample": 0.03894542288996688,
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
            "samples": [0.0, 0.0050733579843309055, 0.020019925895198545, 0.04403393038775318, 0.07582077026400777, 0.11366680875851662, 0.1555317561399588, 0.19915866225866305, 0.2421955893133663, 0.282322405426856, 0.3173758635560149, 0.34546622269985044, 0.36507912432600015] + [0.3751572318311877] * 2 + [0.36507912432600015, 0.3454662226998505, 0.31737586355601494, 0.28232240542685616, 0.24219558931336638, 0.19915866225866313, 0.1555317561399587, 0.11366680875851667, 0.07582077026400783, 0.044033930387753224, 0.02001992589519857, 0.005073357984330864, 0.0],
        },
        "q8.xy.x180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 28,
        },
        "q8.xy.x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0025366789921654528, 0.010009962947599272, 0.02201696519387659, 0.037910385132003885, 0.05683340437925831, 0.0777658780699794, 0.09957933112933152, 0.12109779465668315, 0.141161202713428, 0.15868793177800744, 0.17273311134992522, 0.18253956216300007] + [0.18757861591559385] * 2 + [0.18253956216300007, 0.17273311134992525, 0.15868793177800747, 0.14116120271342808, 0.12109779465668319, 0.09957933112933157, 0.07776587806997935, 0.05683340437925834, 0.03791038513200391, 0.022016965193876612, 0.010009962947599284, 0.002536678992165432, 0.0],
        },
        "q8.xy.x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 28,
        },
        "q8.xy.-x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -0.0025366789921654528, -0.010009962947599272, -0.02201696519387659, -0.037910385132003885, -0.05683340437925831, -0.0777658780699794, -0.09957933112933152, -0.12109779465668315, -0.141161202713428, -0.15868793177800744, -0.17273311134992522, -0.18253956216300007] + [-0.18757861591559385] * 2 + [-0.18253956216300007, -0.17273311134992525, -0.15868793177800747, -0.14116120271342808, -0.12109779465668319, -0.09957933112933157, -0.07776587806997935, -0.05683340437925834, -0.03791038513200391, -0.022016965193876612, -0.010009962947599284, -0.002536678992165432, 0.0],
        },
        "q8.xy.-x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 3.1065358082197554e-19, 1.2258669083361053e-18, 2.6963005951619652e-18, 4.6426831806351964e-18, 6.960084675770586e-18, 9.523573366128362e-18, 1.2194950912877024e-17, 1.4830202661011046e-17, 1.7287261506679028e-17, 1.9433666771525036e-17, 2.1153705192144928e-17, 2.2354649052067734e-17] + [2.297175515695228e-17] * 2 + [2.2354649052067734e-17, 2.115370519214493e-17, 1.943366677152504e-17, 1.7287261506679037e-17, 1.4830202661011052e-17, 1.2194950912877029e-17, 9.523573366128356e-18, 6.960084675770589e-18, 4.6426831806352e-18, 2.696300595161968e-18, 1.2258669083361068e-18, 3.1065358082197303e-19, 0.0],
        },
        "q8.xy.y180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 3.1065358082197554e-19, 1.2258669083361053e-18, 2.6963005951619652e-18, 4.6426831806351964e-18, 6.960084675770586e-18, 9.523573366128362e-18, 1.2194950912877024e-17, 1.4830202661011046e-17, 1.7287261506679028e-17, 1.9433666771525036e-17, 2.1153705192144928e-17, 2.2354649052067734e-17] + [2.297175515695228e-17] * 2 + [2.2354649052067734e-17, 2.115370519214493e-17, 1.943366677152504e-17, 1.7287261506679037e-17, 1.4830202661011052e-17, 1.2194950912877029e-17, 9.523573366128356e-18, 6.960084675770589e-18, 4.6426831806352e-18, 2.696300595161968e-18, 1.2258669083361068e-18, 3.1065358082197303e-19, 0.0],
        },
        "q8.xy.y180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0050733579843309055, 0.020019925895198545, 0.04403393038775318, 0.07582077026400777, 0.11366680875851662, 0.1555317561399588, 0.19915866225866305, 0.2421955893133663, 0.282322405426856, 0.3173758635560149, 0.34546622269985044, 0.36507912432600015] + [0.3751572318311877] * 2 + [0.36507912432600015, 0.3454662226998505, 0.31737586355601494, 0.28232240542685616, 0.24219558931336638, 0.19915866225866313, 0.1555317561399587, 0.11366680875851667, 0.07582077026400783, 0.044033930387753224, 0.02001992589519857, 0.005073357984330864, 0.0],
        },
        "q8.xy.y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 1.5532679041098777e-19, 6.129334541680526e-19, 1.3481502975809826e-18, 2.3213415903175982e-18, 3.480042337885293e-18, 4.761786683064181e-18, 6.097475456438512e-18, 7.415101330505523e-18, 8.643630753339514e-18, 9.716833385762518e-18, 1.0576852596072464e-17, 1.1177324526033867e-17] + [1.148587757847614e-17] * 2 + [1.1177324526033867e-17, 1.0576852596072466e-17, 9.71683338576252e-18, 8.643630753339519e-18, 7.415101330505526e-18, 6.097475456438514e-18, 4.761786683064178e-18, 3.4800423378852945e-18, 2.3213415903176e-18, 1.348150297580984e-18, 6.129334541680534e-19, 1.5532679041098652e-19, 0.0],
        },
        "q8.xy.y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0025366789921654528, 0.010009962947599272, 0.02201696519387659, 0.037910385132003885, 0.05683340437925831, 0.0777658780699794, 0.09957933112933152, 0.12109779465668315, 0.141161202713428, 0.15868793177800744, 0.17273311134992522, 0.18253956216300007] + [0.18757861591559385] * 2 + [0.18253956216300007, 0.17273311134992525, 0.15868793177800747, 0.14116120271342808, 0.12109779465668319, 0.09957933112933157, 0.07776587806997935, 0.05683340437925834, 0.03791038513200391, 0.022016965193876612, 0.010009962947599284, 0.002536678992165432, 0.0],
        },
        "q8.xy.-y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 1.5532679041098777e-19, 6.129334541680526e-19, 1.3481502975809826e-18, 2.3213415903175982e-18, 3.480042337885293e-18, 4.761786683064181e-18, 6.097475456438512e-18, 7.415101330505523e-18, 8.643630753339514e-18, 9.716833385762518e-18, 1.0576852596072464e-17, 1.1177324526033867e-17] + [1.148587757847614e-17] * 2 + [1.1177324526033867e-17, 1.0576852596072466e-17, 9.71683338576252e-18, 8.643630753339519e-18, 7.415101330505526e-18, 6.097475456438514e-18, 4.761786683064178e-18, 3.4800423378852945e-18, 2.3213415903176e-18, 1.348150297580984e-18, 6.129334541680534e-19, 1.5532679041098652e-19, 0.0],
        },
        "q8.xy.-y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.0025366789921654528, -0.010009962947599272, -0.02201696519387659, -0.037910385132003885, -0.05683340437925831, -0.0777658780699794, -0.09957933112933152, -0.12109779465668315, -0.141161202713428, -0.15868793177800744, -0.17273311134992522, -0.18253956216300007] + [-0.18757861591559385] * 2 + [-0.18253956216300007, -0.17273311134992525, -0.15868793177800747, -0.14116120271342808, -0.12109779465668319, -0.09957933112933157, -0.07776587806997935, -0.05683340437925834, -0.03791038513200391, -0.022016965193876612, -0.010009962947599284, -0.002536678992165432, 0.0],
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
            "sample": 0.05886600096490788,
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
            "sample": 0.07311249761928179,
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
            "sample": -0.08976901035867871,
        },
        "cr_q1_q2.square.wf.Q": {
            "type": "constant",
            "sample": -0.12017289536007456,
        },
        "zz_q1_q2.square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "zz_q1_q2.square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "cr_q2_q1.square.wf.I": {
            "type": "constant",
            "sample": -0.22442252589669678,
        },
        "cr_q2_q1.square.wf.Q": {
            "type": "constant",
            "sample": -0.3004322384001864,
        },
        "cr_q2_q3.square.wf.I": {
            "type": "constant",
            "sample": -0.014961501726446454,
        },
        "cr_q2_q3.square.wf.Q": {
            "type": "constant",
            "sample": -0.020028815893345764,
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
            "cosine": [(-0.35085202724936854, 2000)],
            "sine": [(0.9364309130816904, 2000)],
        },
        "q1.resonator.readout.iw2": {
            "cosine": [(-0.9364309130816904, 2000)],
            "sine": [(-0.35085202724936854, 2000)],
        },
        "q1.resonator.readout.iw3": {
            "cosine": [(0.9364309130816904, 2000)],
            "sine": [(0.35085202724936854, 2000)],
        },
        "q2.resonator.readout.iw1": {
            "cosine": [(-0.1180848483063911, 2500)],
            "sine": [(-0.9930035088560647, 2500)],
        },
        "q2.resonator.readout.iw2": {
            "cosine": [(0.9930035088560647, 2500)],
            "sine": [(-0.1180848483063911, 2500)],
        },
        "q2.resonator.readout.iw3": {
            "cosine": [(-0.9930035088560647, 2500)],
            "sine": [(0.1180848483063911, 2500)],
        },
        "q3.resonator.readout.iw1": {
            "cosine": [(0.9468898519242067, 2000)],
            "sine": [(0.32155809478685793, 2000)],
        },
        "q3.resonator.readout.iw2": {
            "cosine": [(-0.32155809478685793, 2000)],
            "sine": [(0.9468898519242067, 2000)],
        },
        "q3.resonator.readout.iw3": {
            "cosine": [(0.32155809478685793, 2000)],
            "sine": [(-0.9468898519242067, 2000)],
        },
        "q4.resonator.readout.iw1": {
            "cosine": [(-0.3121146787814643, 2000)],
            "sine": [(-0.9500444343761735, 2000)],
        },
        "q4.resonator.readout.iw2": {
            "cosine": [(0.9500444343761735, 2000)],
            "sine": [(-0.3121146787814643, 2000)],
        },
        "q4.resonator.readout.iw3": {
            "cosine": [(-0.9500444343761735, 2000)],
            "sine": [(0.3121146787814643, 2000)],
        },
        "q5.resonator.readout.iw1": {
            "cosine": [(-0.9965476171382793, 2000)],
            "sine": [(0.08302317011544058, 2000)],
        },
        "q5.resonator.readout.iw2": {
            "cosine": [(-0.08302317011544058, 2000)],
            "sine": [(-0.9965476171382793, 2000)],
        },
        "q5.resonator.readout.iw3": {
            "cosine": [(0.08302317011544058, 2000)],
            "sine": [(0.9965476171382793, 2000)],
        },
        "q6.resonator.readout.iw1": {
            "cosine": [(-0.8114511176826852, 2000)],
            "sine": [(0.5844202970564258, 2000)],
        },
        "q6.resonator.readout.iw2": {
            "cosine": [(-0.5844202970564258, 2000)],
            "sine": [(-0.8114511176826852, 2000)],
        },
        "q6.resonator.readout.iw3": {
            "cosine": [(0.5844202970564258, 2000)],
            "sine": [(0.8114511176826852, 2000)],
        },
        "q7.resonator.readout.iw1": {
            "cosine": [(-0.9929690166473447, 2000)],
            "sine": [(-0.1183745410905795, 2000)],
        },
        "q7.resonator.readout.iw2": {
            "cosine": [(0.1183745410905795, 2000)],
            "sine": [(-0.9929690166473447, 2000)],
        },
        "q7.resonator.readout.iw3": {
            "cosine": [(-0.1183745410905795, 2000)],
            "sine": [(0.9929690166473447, 2000)],
        },
        "q8.resonator.readout.iw1": {
            "cosine": [(0.7452364606756877, 2000)],
            "sine": [(0.6668002832029799, 2000)],
        },
        "q8.resonator.readout.iw2": {
            "cosine": [(-0.6668002832029799, 2000)],
            "sine": [(0.7452364606756877, 2000)],
        },
        "q8.resonator.readout.iw3": {
            "cosine": [(0.6668002832029799, 2000)],
            "sine": [(-0.7452364606756877, 2000)],
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
                            "full_scale_power_dbm": -17,
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
                            "full_scale_power_dbm": -5,
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
                            "full_scale_power_dbm": -17,
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
                            "full_scale_power_dbm": -5,
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
                            "full_scale_power_dbm": -17,
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
                            "full_scale_power_dbm": -5,
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
                            "full_scale_power_dbm": -17,
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
                            "full_scale_power_dbm": -5,
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
                            "full_scale_power_dbm": -17,
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
                            "full_scale_power_dbm": -5,
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
                            "full_scale_power_dbm": -17,
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
                            "full_scale_power_dbm": -5,
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
                            "full_scale_power_dbm": -17,
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
                            "full_scale_power_dbm": -5,
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
                            "full_scale_power_dbm": -17,
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
                            "full_scale_power_dbm": -5,
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
                "cr_q2_q1_Square": "q1.xy.cr_q2_q1_Square.pulse",
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
            "intermediate_frequency": 51429959.310891405,
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
            "intermediate_frequency": 50020905.0,
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
            "intermediate_frequency": 51021926.20792695,
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
            "intermediate_frequency": 49474765.0,
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
            "intermediate_frequency": 47978773.749092855,
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
            "intermediate_frequency": 50688915.0,
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
            "intermediate_frequency": 50838121.96023835,
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
            "intermediate_frequency": 49581765.0,
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
            "intermediate_frequency": 50158321.634366505,
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
            "intermediate_frequency": 50221316.0,
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
            "intermediate_frequency": 51211754.33278539,
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
            "intermediate_frequency": 49661041.0,
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
            "intermediate_frequency": 51286611.227740586,
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
            "intermediate_frequency": 49850000.0,
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
            "intermediate_frequency": 51093212.89560413,
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
            "intermediate_frequency": 49800000.0,
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
            "thread": "",
            "MWInput": {
                "port": ('con1', 2, 2),
                "upconverter": 1,
            },
            "intermediate_frequency": -179978073.79207325,
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
            "thread": "",
            "MWInput": {
                "port": ('con1', 2, 2),
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
            "thread": "",
            "MWInput": {
                "port": ('con1', 2, 3),
                "upconverter": 1,
            },
            "intermediate_frequency": 282429959.31089115,
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
            "thread": "",
            "MWInput": {
                "port": ('con1', 2, 3),
                "upconverter": 1,
            },
            "intermediate_frequency": 30978773.749093056,
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
            "thread": "",
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
            "thread": "",
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
            "thread": "",
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
            "thread": "",
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
            "thread": "",
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
            "thread": "",
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
            "thread": "",
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
            "thread": "",
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
            "thread": "",
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
            "thread": "",
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
            "thread": "",
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
            "thread": "",
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
            "thread": "",
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
            "length": 28,
            "waveforms": {
                "I": "q1.xy.x180_DragCosine.wf.I",
                "Q": "q1.xy.x180_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q1.xy.x90_DragCosine.pulse": {
            "length": 28,
            "waveforms": {
                "I": "q1.xy.x90_DragCosine.wf.I",
                "Q": "q1.xy.x90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q1.xy.-x90_DragCosine.pulse": {
            "length": 28,
            "waveforms": {
                "I": "q1.xy.-x90_DragCosine.wf.I",
                "Q": "q1.xy.-x90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q1.xy.y180_DragCosine.pulse": {
            "length": 28,
            "waveforms": {
                "I": "q1.xy.y180_DragCosine.wf.I",
                "Q": "q1.xy.y180_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q1.xy.y90_DragCosine.pulse": {
            "length": 28,
            "waveforms": {
                "I": "q1.xy.y90_DragCosine.wf.I",
                "Q": "q1.xy.y90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q1.xy.-y90_DragCosine.pulse": {
            "length": 28,
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
        "q1.xy.cr_q2_q1_Square.pulse": {
            "length": 100,
            "waveforms": {
                "I": "q1.xy.cr_q2_q1_Square.wf.I",
                "Q": "q1.xy.cr_q2_q1_Square.wf.Q",
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
            "length": 28,
            "waveforms": {
                "I": "q2.xy.x180_DragCosine.wf.I",
                "Q": "q2.xy.x180_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q2.xy.x90_DragCosine.pulse": {
            "length": 28,
            "waveforms": {
                "I": "q2.xy.x90_DragCosine.wf.I",
                "Q": "q2.xy.x90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q2.xy.-x90_DragCosine.pulse": {
            "length": 28,
            "waveforms": {
                "I": "q2.xy.-x90_DragCosine.wf.I",
                "Q": "q2.xy.-x90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q2.xy.y180_DragCosine.pulse": {
            "length": 28,
            "waveforms": {
                "I": "q2.xy.y180_DragCosine.wf.I",
                "Q": "q2.xy.y180_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q2.xy.y90_DragCosine.pulse": {
            "length": 28,
            "waveforms": {
                "I": "q2.xy.y90_DragCosine.wf.I",
                "Q": "q2.xy.y90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q2.xy.-y90_DragCosine.pulse": {
            "length": 28,
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
            "length": 2500,
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
            "length": 28,
            "waveforms": {
                "I": "q3.xy.x180_DragCosine.wf.I",
                "Q": "q3.xy.x180_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q3.xy.x90_DragCosine.pulse": {
            "length": 28,
            "waveforms": {
                "I": "q3.xy.x90_DragCosine.wf.I",
                "Q": "q3.xy.x90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q3.xy.-x90_DragCosine.pulse": {
            "length": 28,
            "waveforms": {
                "I": "q3.xy.-x90_DragCosine.wf.I",
                "Q": "q3.xy.-x90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q3.xy.y180_DragCosine.pulse": {
            "length": 28,
            "waveforms": {
                "I": "q3.xy.y180_DragCosine.wf.I",
                "Q": "q3.xy.y180_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q3.xy.y90_DragCosine.pulse": {
            "length": 28,
            "waveforms": {
                "I": "q3.xy.y90_DragCosine.wf.I",
                "Q": "q3.xy.y90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q3.xy.-y90_DragCosine.pulse": {
            "length": 28,
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
            "length": 28,
            "waveforms": {
                "I": "q4.xy.x180_DragCosine.wf.I",
                "Q": "q4.xy.x180_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q4.xy.x90_DragCosine.pulse": {
            "length": 28,
            "waveforms": {
                "I": "q4.xy.x90_DragCosine.wf.I",
                "Q": "q4.xy.x90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q4.xy.-x90_DragCosine.pulse": {
            "length": 28,
            "waveforms": {
                "I": "q4.xy.-x90_DragCosine.wf.I",
                "Q": "q4.xy.-x90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q4.xy.y180_DragCosine.pulse": {
            "length": 28,
            "waveforms": {
                "I": "q4.xy.y180_DragCosine.wf.I",
                "Q": "q4.xy.y180_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q4.xy.y90_DragCosine.pulse": {
            "length": 28,
            "waveforms": {
                "I": "q4.xy.y90_DragCosine.wf.I",
                "Q": "q4.xy.y90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q4.xy.-y90_DragCosine.pulse": {
            "length": 28,
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
            "length": 28,
            "waveforms": {
                "I": "q5.xy.x180_DragCosine.wf.I",
                "Q": "q5.xy.x180_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q5.xy.x90_DragCosine.pulse": {
            "length": 28,
            "waveforms": {
                "I": "q5.xy.x90_DragCosine.wf.I",
                "Q": "q5.xy.x90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q5.xy.-x90_DragCosine.pulse": {
            "length": 28,
            "waveforms": {
                "I": "q5.xy.-x90_DragCosine.wf.I",
                "Q": "q5.xy.-x90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q5.xy.y180_DragCosine.pulse": {
            "length": 28,
            "waveforms": {
                "I": "q5.xy.y180_DragCosine.wf.I",
                "Q": "q5.xy.y180_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q5.xy.y90_DragCosine.pulse": {
            "length": 28,
            "waveforms": {
                "I": "q5.xy.y90_DragCosine.wf.I",
                "Q": "q5.xy.y90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q5.xy.-y90_DragCosine.pulse": {
            "length": 28,
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
            "length": 28,
            "waveforms": {
                "I": "q6.xy.x180_DragCosine.wf.I",
                "Q": "q6.xy.x180_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q6.xy.x90_DragCosine.pulse": {
            "length": 28,
            "waveforms": {
                "I": "q6.xy.x90_DragCosine.wf.I",
                "Q": "q6.xy.x90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q6.xy.-x90_DragCosine.pulse": {
            "length": 28,
            "waveforms": {
                "I": "q6.xy.-x90_DragCosine.wf.I",
                "Q": "q6.xy.-x90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q6.xy.y180_DragCosine.pulse": {
            "length": 28,
            "waveforms": {
                "I": "q6.xy.y180_DragCosine.wf.I",
                "Q": "q6.xy.y180_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q6.xy.y90_DragCosine.pulse": {
            "length": 28,
            "waveforms": {
                "I": "q6.xy.y90_DragCosine.wf.I",
                "Q": "q6.xy.y90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q6.xy.-y90_DragCosine.pulse": {
            "length": 28,
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
            "length": 28,
            "waveforms": {
                "I": "q7.xy.x180_DragCosine.wf.I",
                "Q": "q7.xy.x180_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q7.xy.x90_DragCosine.pulse": {
            "length": 28,
            "waveforms": {
                "I": "q7.xy.x90_DragCosine.wf.I",
                "Q": "q7.xy.x90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q7.xy.-x90_DragCosine.pulse": {
            "length": 28,
            "waveforms": {
                "I": "q7.xy.-x90_DragCosine.wf.I",
                "Q": "q7.xy.-x90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q7.xy.y180_DragCosine.pulse": {
            "length": 28,
            "waveforms": {
                "I": "q7.xy.y180_DragCosine.wf.I",
                "Q": "q7.xy.y180_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q7.xy.y90_DragCosine.pulse": {
            "length": 28,
            "waveforms": {
                "I": "q7.xy.y90_DragCosine.wf.I",
                "Q": "q7.xy.y90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q7.xy.-y90_DragCosine.pulse": {
            "length": 28,
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
            "length": 28,
            "waveforms": {
                "I": "q8.xy.x180_DragCosine.wf.I",
                "Q": "q8.xy.x180_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q8.xy.x90_DragCosine.pulse": {
            "length": 28,
            "waveforms": {
                "I": "q8.xy.x90_DragCosine.wf.I",
                "Q": "q8.xy.x90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q8.xy.-x90_DragCosine.pulse": {
            "length": 28,
            "waveforms": {
                "I": "q8.xy.-x90_DragCosine.wf.I",
                "Q": "q8.xy.-x90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q8.xy.y180_DragCosine.pulse": {
            "length": 28,
            "waveforms": {
                "I": "q8.xy.y180_DragCosine.wf.I",
                "Q": "q8.xy.y180_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q8.xy.y90_DragCosine.pulse": {
            "length": 28,
            "waveforms": {
                "I": "q8.xy.y90_DragCosine.wf.I",
                "Q": "q8.xy.y90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q8.xy.-y90_DragCosine.pulse": {
            "length": 28,
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
            "samples": [0.0, 0.005635945982423489, 0.02223994862297123, 0.04891688184150544, 0.08422858526314811, 0.12627139581634475, 0.17277877470179662, 0.22124349708580268, 0.2690528172400154, 0.31362932233993973, 0.35256988145744067, 0.38377519897110557, 0.4055629881365775] + [0.4167586636003867] * 2 + [0.4055629881365775, 0.3837751989711056, 0.3525698814574407, 0.31362932233993984, 0.26905281724001545, 0.2212434970858028, 0.17277877470179653, 0.1262713958163448, 0.08422858526314818, 0.048916881841505486, 0.022239948622971253, 0.005635945982423443, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.xy.x180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 28,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.xy.x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0028179729912117444, 0.011119974311485615, 0.02445844092075272, 0.042114292631574055, 0.06313569790817238, 0.08638938735089831, 0.11062174854290134, 0.1345264086200077, 0.15681466116996987, 0.17628494072872034, 0.19188759948555278, 0.20278149406828874] + [0.20837933180019336] * 2 + [0.20278149406828874, 0.1918875994855528, 0.17628494072872036, 0.15681466116996992, 0.13452640862000773, 0.1106217485429014, 0.08638938735089827, 0.0631356979081724, 0.04211429263157409, 0.024458440920752743, 0.011119974311485627, 0.0028179729912117214, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.xy.x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 28,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.xy.-x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -0.0028179729912117444, -0.011119974311485615, -0.02445844092075272, -0.042114292631574055, -0.06313569790817238, -0.08638938735089831, -0.11062174854290134, -0.1345264086200077, -0.15681466116996987, -0.17628494072872034, -0.19188759948555278, -0.20278149406828874] + [-0.20837933180019336] * 2 + [-0.20278149406828874, -0.1918875994855528, -0.17628494072872036, -0.15681466116996992, -0.13452640862000773, -0.1106217485429014, -0.08638938735089827, -0.0631356979081724, -0.04211429263157409, -0.024458440920752743, -0.011119974311485627, -0.0028179729912117214, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.xy.-x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 3.4510216037711553e-19, 1.3618040947161651e-18, 2.995295138573446e-18, 5.157513366961213e-18, 7.731893035517754e-18, 1.0579648669957845e-17, 1.354725702691475e-17, 1.6474733571728132e-17, 1.9204257286118032e-17, 2.1588678840130823e-17, 2.3499453450605152e-17, 2.483357076370478e-17] + [2.5519108169757105e-17] * 2 + [2.483357076370478e-17, 2.3499453450605155e-17, 2.1588678840130826e-17, 1.920425728611804e-17, 1.6474733571728138e-17, 1.3547257026914758e-17, 1.057964866995784e-17, 7.731893035517758e-18, 5.157513366961217e-18, 2.995295138573449e-18, 1.3618040947161665e-18, 3.451021603771127e-19, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.xy.y180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 3.4510216037711553e-19, 1.3618040947161651e-18, 2.995295138573446e-18, 5.157513366961213e-18, 7.731893035517754e-18, 1.0579648669957845e-17, 1.354725702691475e-17, 1.6474733571728132e-17, 1.9204257286118032e-17, 2.1588678840130823e-17, 2.3499453450605152e-17, 2.483357076370478e-17] + [2.5519108169757105e-17] * 2 + [2.483357076370478e-17, 2.3499453450605155e-17, 2.1588678840130826e-17, 1.920425728611804e-17, 1.6474733571728138e-17, 1.3547257026914758e-17, 1.057964866995784e-17, 7.731893035517758e-18, 5.157513366961217e-18, 2.995295138573449e-18, 1.3618040947161665e-18, 3.451021603771127e-19, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.xy.y180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.005635945982423489, 0.02223994862297123, 0.04891688184150544, 0.08422858526314811, 0.12627139581634475, 0.17277877470179662, 0.22124349708580268, 0.2690528172400154, 0.31362932233993973, 0.35256988145744067, 0.38377519897110557, 0.4055629881365775] + [0.4167586636003867] * 2 + [0.4055629881365775, 0.3837751989711056, 0.3525698814574407, 0.31362932233993984, 0.26905281724001545, 0.2212434970858028, 0.17277877470179653, 0.1262713958163448, 0.08422858526314818, 0.048916881841505486, 0.022239948622971253, 0.005635945982423443, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.xy.y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 1.7255108018855777e-19, 6.809020473580826e-19, 1.497647569286723e-18, 2.5787566834806065e-18, 3.865946517758877e-18, 5.289824334978923e-18, 6.773628513457375e-18, 8.237366785864066e-18, 9.602128643059016e-18, 1.0794339420065411e-17, 1.1749726725302576e-17, 1.241678538185239e-17] + [1.2759554084878553e-17] * 2 + [1.241678538185239e-17, 1.1749726725302577e-17, 1.0794339420065413e-17, 9.60212864305902e-18, 8.237366785864069e-18, 6.773628513457379e-18, 5.28982433497892e-18, 3.865946517758879e-18, 2.5787566834806084e-18, 1.4976475692867245e-18, 6.809020473580832e-19, 1.7255108018855635e-19, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.xy.y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0028179729912117444, 0.011119974311485615, 0.02445844092075272, 0.042114292631574055, 0.06313569790817238, 0.08638938735089831, 0.11062174854290134, 0.1345264086200077, 0.15681466116996987, 0.17628494072872034, 0.19188759948555278, 0.20278149406828874] + [0.20837933180019336] * 2 + [0.20278149406828874, 0.1918875994855528, 0.17628494072872036, 0.15681466116996992, 0.13452640862000773, 0.1106217485429014, 0.08638938735089827, 0.0631356979081724, 0.04211429263157409, 0.024458440920752743, 0.011119974311485627, 0.0028179729912117214, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.xy.-y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 1.7255108018855777e-19, 6.809020473580826e-19, 1.497647569286723e-18, 2.5787566834806065e-18, 3.865946517758877e-18, 5.289824334978923e-18, 6.773628513457375e-18, 8.237366785864066e-18, 9.602128643059016e-18, 1.0794339420065411e-17, 1.1749726725302576e-17, 1.241678538185239e-17] + [1.2759554084878553e-17] * 2 + [1.241678538185239e-17, 1.1749726725302577e-17, 1.0794339420065413e-17, 9.60212864305902e-18, 8.237366785864069e-18, 6.773628513457379e-18, 5.28982433497892e-18, 3.865946517758879e-18, 2.5787566834806084e-18, 1.4976475692867245e-18, 6.809020473580832e-19, 1.7255108018855635e-19, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.xy.-y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.0028179729912117444, -0.011119974311485615, -0.02445844092075272, -0.042114292631574055, -0.06313569790817238, -0.08638938735089831, -0.11062174854290134, -0.1345264086200077, -0.15681466116996987, -0.17628494072872034, -0.19188759948555278, -0.20278149406828874] + [-0.20837933180019336] * 2 + [-0.20278149406828874, -0.1918875994855528, -0.17628494072872036, -0.15681466116996992, -0.13452640862000773, -0.1106217485429014, -0.08638938735089827, -0.0631356979081724, -0.04211429263157409, -0.024458440920752743, -0.011119974311485627, -0.0028179729912117214, 0.0],
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
            "sample": 0.058118024879361775,
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
        "q1.xy.cr_q2_q1_Square.wf.I": {
            "type": "constant",
            "sample": -0.059846006905785815,
        },
        "q1.xy.cr_q2_q1_Square.wf.Q": {
            "type": "constant",
            "sample": -0.08011526357338306,
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
            "sample": 0.1096393611252029,
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
            "samples": [0.0, 0.004417441222850343, 0.01743161949166544, 0.03834093708737901, 0.06601816728623099, 0.09897122344421723, 0.13542359777428006, 0.17341013334094038, 0.21088296617935126, 0.24582192617171267, 0.2763434449412238, 0.3008020995108196, 0.31787931748176634] + [0.3266544616129772] * 2 + [0.31787931748176634, 0.3008020995108196, 0.27634344494122387, 0.24582192617171278, 0.21088296617935134, 0.17341013334094044, 0.13542359777427998, 0.09897122344421729, 0.06601816728623104, 0.03834093708737905, 0.017431619491665457, 0.004417441222850306, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.xy.x180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 28,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.xy.x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0022087206114251713, 0.00871580974583272, 0.019170468543689506, 0.03300908364311549, 0.049485611722108615, 0.06771179888714003, 0.08670506667047019, 0.10544148308967563, 0.12291096308585633, 0.1381717224706119, 0.1504010497554098, 0.15893965874088317] + [0.1633272308064886] * 2 + [0.15893965874088317, 0.1504010497554098, 0.13817172247061194, 0.12291096308585639, 0.10544148308967567, 0.08670506667047022, 0.06771179888713999, 0.04948561172210864, 0.03300908364311552, 0.019170468543689523, 0.008715809745832729, 0.002208720611425153, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.xy.x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 28,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.xy.-x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -0.0022087206114251713, -0.00871580974583272, -0.019170468543689506, -0.03300908364311549, -0.049485611722108615, -0.06771179888714003, -0.08670506667047019, -0.10544148308967563, -0.12291096308585633, -0.1381717224706119, -0.1504010497554098, -0.15893965874088317] + [-0.1633272308064886] * 2 + [-0.15893965874088317, -0.1504010497554098, -0.13817172247061194, -0.12291096308585639, -0.10544148308967567, -0.08670506667047022, -0.06771179888713999, -0.04948561172210864, -0.03300908364311552, -0.019170468543689523, -0.008715809745832729, -0.002208720611425153, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.xy.-x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 2.704902626992621e-19, 1.0673788507211346e-18, 2.3477052940184377e-18, 4.0424468626328645e-18, 6.060239599932906e-18, 8.292303777164536e-18, 1.0618308236784918e-17, 1.2912857476312103e-17, 1.5052251752321246e-17, 1.6921155765631128e-17, 1.8418816417136443e-17, 1.946449443345952e-17] + [2.0001817042076722e-17] * 2 + [1.946449443345952e-17, 1.8418816417136443e-17, 1.692115576563113e-17, 1.5052251752321252e-17, 1.2912857476312108e-17, 1.0618308236784921e-17, 8.29230377716453e-18, 6.060239599932909e-18, 4.0424468626328675e-18, 2.3477052940184396e-18, 1.0673788507211358e-18, 2.7049026269925986e-19, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.xy.y180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 2.704902626992621e-19, 1.0673788507211346e-18, 2.3477052940184377e-18, 4.0424468626328645e-18, 6.060239599932906e-18, 8.292303777164536e-18, 1.0618308236784918e-17, 1.2912857476312103e-17, 1.5052251752321246e-17, 1.6921155765631128e-17, 1.8418816417136443e-17, 1.946449443345952e-17] + [2.0001817042076722e-17] * 2 + [1.946449443345952e-17, 1.8418816417136443e-17, 1.692115576563113e-17, 1.5052251752321252e-17, 1.2912857476312108e-17, 1.0618308236784921e-17, 8.29230377716453e-18, 6.060239599932909e-18, 4.0424468626328675e-18, 2.3477052940184396e-18, 1.0673788507211358e-18, 2.7049026269925986e-19, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.xy.y180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.004417441222850343, 0.01743161949166544, 0.03834093708737901, 0.06601816728623099, 0.09897122344421723, 0.13542359777428006, 0.17341013334094038, 0.21088296617935126, 0.24582192617171267, 0.2763434449412238, 0.3008020995108196, 0.31787931748176634] + [0.3266544616129772] * 2 + [0.31787931748176634, 0.3008020995108196, 0.27634344494122387, 0.24582192617171278, 0.21088296617935134, 0.17341013334094044, 0.13542359777427998, 0.09897122344421729, 0.06601816728623104, 0.03834093708737905, 0.017431619491665457, 0.004417441222850306, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.xy.y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 1.3524513134963104e-19, 5.336894253605673e-19, 1.1738526470092189e-18, 2.0212234313164322e-18, 3.030119799966453e-18, 4.146151888582268e-18, 5.309154118392459e-18, 6.456428738156052e-18, 7.526125876160623e-18, 8.460577882815564e-18, 9.209408208568222e-18, 9.73224721672976e-18] + [1.0000908521038361e-17] * 2 + [9.73224721672976e-18, 9.209408208568222e-18, 8.460577882815566e-18, 7.526125876160626e-18, 6.456428738156054e-18, 5.309154118392461e-18, 4.146151888582265e-18, 3.0301197999664545e-18, 2.0212234313164338e-18, 1.1738526470092198e-18, 5.336894253605679e-19, 1.3524513134962993e-19, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.xy.y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0022087206114251713, 0.00871580974583272, 0.019170468543689506, 0.03300908364311549, 0.049485611722108615, 0.06771179888714003, 0.08670506667047019, 0.10544148308967563, 0.12291096308585633, 0.1381717224706119, 0.1504010497554098, 0.15893965874088317] + [0.1633272308064886] * 2 + [0.15893965874088317, 0.1504010497554098, 0.13817172247061194, 0.12291096308585639, 0.10544148308967567, 0.08670506667047022, 0.06771179888713999, 0.04948561172210864, 0.03300908364311552, 0.019170468543689523, 0.008715809745832729, 0.002208720611425153, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.xy.-y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 1.3524513134963104e-19, 5.336894253605673e-19, 1.1738526470092189e-18, 2.0212234313164322e-18, 3.030119799966453e-18, 4.146151888582268e-18, 5.309154118392459e-18, 6.456428738156052e-18, 7.526125876160623e-18, 8.460577882815564e-18, 9.209408208568222e-18, 9.73224721672976e-18] + [1.0000908521038361e-17] * 2 + [9.73224721672976e-18, 9.209408208568222e-18, 8.460577882815566e-18, 7.526125876160626e-18, 6.456428738156054e-18, 5.309154118392461e-18, 4.146151888582265e-18, 3.0301197999664545e-18, 2.0212234313164338e-18, 1.1738526470092198e-18, 5.336894253605679e-19, 1.3524513134962993e-19, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.xy.-y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.0022087206114251713, -0.00871580974583272, -0.019170468543689506, -0.03300908364311549, -0.049485611722108615, -0.06771179888714003, -0.08670506667047019, -0.10544148308967563, -0.12291096308585633, -0.1381717224706119, -0.1504010497554098, -0.15893965874088317] + [-0.1633272308064886] * 2 + [-0.15893965874088317, -0.1504010497554098, -0.13817172247061194, -0.12291096308585639, -0.10544148308967567, -0.08670506667047022, -0.06771179888713999, -0.04948561172210864, -0.03300908364311552, -0.019170468543689523, -0.008715809745832729, -0.002208720611425153, 0.0],
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
            "sample": 0.03753181236700035,
        },
        "q2.xy.saturation.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q2.xy.cr_q1_q2_Square.wf.I": {
            "type": "constant",
            "sample": -0.059846006905785815,
        },
        "q2.xy.cr_q1_q2_Square.wf.Q": {
            "type": "constant",
            "sample": -0.08011526357338306,
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
            "sample": 0.0411256207067346,
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
            "samples": [0.0, 0.006413580743147028, 0.02530856517463152, 0.05566631979296777, 0.09585025018886931, 0.14369403027347044, 0.19661838947850938, 0.25177016190028273, 0.3061761012120285, 0.3569031691429978, 0.4012166563308202, 0.43672761121108145, 0.4615216290145186] + [0.474262057823656] * 2 + [0.4615216290145186, 0.4367276112110815, 0.40121665633082026, 0.35690316914299797, 0.3061761012120286, 0.25177016190028284, 0.19661838947850926, 0.1436940302734705, 0.09585025018886939, 0.055666319792967815, 0.025308565174631547, 0.006413580743146975, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q3.xy.x180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 28,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q3.xy.x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.003206790371573514, 0.01265428258731576, 0.027833159896483883, 0.047925125094434654, 0.07184701513673522, 0.09830919473925469, 0.12588508095014136, 0.15308805060601424, 0.1784515845714989, 0.2006083281654101, 0.21836380560554072, 0.2307608145072593] + [0.237131028911828] * 2 + [0.2307608145072593, 0.21836380560554075, 0.20060832816541013, 0.17845158457149898, 0.1530880506060143, 0.12588508095014142, 0.09830919473925463, 0.07184701513673525, 0.047925125094434695, 0.027833159896483908, 0.012654282587315773, 0.0032067903715734874, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q3.xy.x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 28,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q3.xy.-x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -0.003206790371573514, -0.01265428258731576, -0.027833159896483883, -0.047925125094434654, -0.07184701513673522, -0.09830919473925469, -0.12588508095014136, -0.15308805060601424, -0.1784515845714989, -0.2006083281654101, -0.21836380560554072, -0.2307608145072593] + [-0.237131028911828] * 2 + [-0.2307608145072593, -0.21836380560554075, -0.20060832816541013, -0.17845158457149898, -0.1530880506060143, -0.12588508095014142, -0.09830919473925463, -0.07184701513673525, -0.047925125094434695, -0.027833159896483908, -0.012654282587315773, -0.0032067903715734874, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q3.xy.-x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 3.927185564084055e-19, 1.5497026666062332e-18, 3.4085790177385466e-18, 5.869135104563589e-18, 8.798721711549422e-18, 1.2039404066418207e-17, 1.5416476144599607e-17, 1.8747879116236335e-17, 2.1854016184825934e-17, 2.456743469700713e-17, 2.674185355844603e-17, 2.826004928549512e-17] + [2.9040175553538864e-17] * 2 + [2.826004928549512e-17, 2.6741853558446034e-17, 2.4567434697007133e-17, 2.1854016184825943e-17, 1.8747879116236344e-17, 1.5416476144599613e-17, 1.20394040664182e-17, 8.798721711549426e-18, 5.869135104563594e-18, 3.4085790177385493e-18, 1.549702666606235e-18, 3.927185564084023e-19, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q3.xy.y180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 3.927185564084055e-19, 1.5497026666062332e-18, 3.4085790177385466e-18, 5.869135104563589e-18, 8.798721711549422e-18, 1.2039404066418207e-17, 1.5416476144599607e-17, 1.8747879116236335e-17, 2.1854016184825934e-17, 2.456743469700713e-17, 2.674185355844603e-17, 2.826004928549512e-17] + [2.9040175553538864e-17] * 2 + [2.826004928549512e-17, 2.6741853558446034e-17, 2.4567434697007133e-17, 2.1854016184825943e-17, 1.8747879116236344e-17, 1.5416476144599613e-17, 1.20394040664182e-17, 8.798721711549426e-18, 5.869135104563594e-18, 3.4085790177385493e-18, 1.549702666606235e-18, 3.927185564084023e-19, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q3.xy.y180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.006413580743147028, 0.02530856517463152, 0.05566631979296777, 0.09585025018886931, 0.14369403027347044, 0.19661838947850938, 0.25177016190028273, 0.3061761012120285, 0.3569031691429978, 0.4012166563308202, 0.43672761121108145, 0.4615216290145186] + [0.474262057823656] * 2 + [0.4615216290145186, 0.4367276112110815, 0.40121665633082026, 0.35690316914299797, 0.3061761012120286, 0.25177016190028284, 0.19661838947850926, 0.1436940302734705, 0.09585025018886939, 0.055666319792967815, 0.025308565174631547, 0.006413580743146975, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q3.xy.y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 1.9635927820420276e-19, 7.748513333031166e-19, 1.7042895088692733e-18, 2.9345675522817945e-18, 4.399360855774711e-18, 6.019702033209104e-18, 7.708238072299803e-18, 9.373939558118168e-18, 1.0927008092412967e-17, 1.2283717348503565e-17, 1.3370926779223015e-17, 1.413002464274756e-17] + [1.4520087776769432e-17] * 2 + [1.413002464274756e-17, 1.3370926779223017e-17, 1.2283717348503567e-17, 1.0927008092412972e-17, 9.373939558118172e-18, 7.708238072299806e-18, 6.0197020332091e-18, 4.399360855774713e-18, 2.934567552281797e-18, 1.7042895088692746e-18, 7.748513333031175e-19, 1.9635927820420115e-19, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q3.xy.y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.003206790371573514, 0.01265428258731576, 0.027833159896483883, 0.047925125094434654, 0.07184701513673522, 0.09830919473925469, 0.12588508095014136, 0.15308805060601424, 0.1784515845714989, 0.2006083281654101, 0.21836380560554072, 0.2307608145072593] + [0.237131028911828] * 2 + [0.2307608145072593, 0.21836380560554075, 0.20060832816541013, 0.17845158457149898, 0.1530880506060143, 0.12588508095014142, 0.09830919473925463, 0.07184701513673525, 0.047925125094434695, 0.027833159896483908, 0.012654282587315773, 0.0032067903715734874, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q3.xy.-y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 1.9635927820420276e-19, 7.748513333031166e-19, 1.7042895088692733e-18, 2.9345675522817945e-18, 4.399360855774711e-18, 6.019702033209104e-18, 7.708238072299803e-18, 9.373939558118168e-18, 1.0927008092412967e-17, 1.2283717348503565e-17, 1.3370926779223015e-17, 1.413002464274756e-17] + [1.4520087776769432e-17] * 2 + [1.413002464274756e-17, 1.3370926779223017e-17, 1.2283717348503567e-17, 1.0927008092412972e-17, 9.373939558118172e-18, 7.708238072299806e-18, 6.0197020332091e-18, 4.399360855774713e-18, 2.934567552281797e-18, 1.7042895088692746e-18, 7.748513333031175e-19, 1.9635927820420115e-19, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q3.xy.-y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.003206790371573514, -0.01265428258731576, -0.027833159896483883, -0.047925125094434654, -0.07184701513673522, -0.09830919473925469, -0.12588508095014136, -0.15308805060601424, -0.1784515845714989, -0.2006083281654101, -0.21836380560554072, -0.2307608145072593] + [-0.237131028911828] * 2 + [-0.2307608145072593, -0.21836380560554075, -0.20060832816541013, -0.17845158457149898, -0.1530880506060143, -0.12588508095014142, -0.09830919473925463, -0.07184701513673525, -0.047925125094434695, -0.027833159896483908, -0.012654282587315773, -0.0032067903715734874, 0.0],
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
            "sample": 0.05274791552973862,
        },
        "q3.xy.saturation.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q3.xy.cr_q2_q3_Square.wf.I": {
            "type": "constant",
            "sample": 0.13899999999999998,
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
            "sample": 0.34565678375741143,
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
            "samples": [0.0, 0.006209627188159414, 0.024503746143621857, 0.0538961161782422, 0.09280218701552259, 0.1391245223061642, 0.19036587296455895, 0.2437638045133835, 0.29643962064130136, 0.3455535544662295, 0.38845786110299835, 0.4228395582754537, 0.44684511978965796] + [0.4591803996107723] * 2 + [0.44684511978965796, 0.4228395582754538, 0.3884578611029984, 0.34555355446622965, 0.2964396206413014, 0.24376380451338361, 0.19036587296455884, 0.1391245223061643, 0.09280218701552267, 0.05389611617824225, 0.02450374614362188, 0.006209627188159363, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q4.xy.x180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 28,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q4.xy.x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.003104813594079707, 0.012251873071810929, 0.0269480580891211, 0.046401093507761296, 0.0695622611530821, 0.09518293648227948, 0.12188190225669175, 0.14821981032065068, 0.17277677723311474, 0.19422893055149917, 0.21141977913772686, 0.22342255989482898] + [0.22959019980538614] * 2 + [0.22342255989482898, 0.2114197791377269, 0.1942289305514992, 0.17277677723311483, 0.1482198103206507, 0.12188190225669181, 0.09518293648227942, 0.06956226115308214, 0.04640109350776134, 0.026948058089121124, 0.01225187307181094, 0.0031048135940796814, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q4.xy.x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 28,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q4.xy.-x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -0.003104813594079707, -0.012251873071810929, -0.0269480580891211, -0.046401093507761296, -0.0695622611530821, -0.09518293648227948, -0.12188190225669175, -0.14821981032065068, -0.17277677723311474, -0.19422893055149917, -0.21141977913772686, -0.22342255989482898] + [-0.22959019980538614] * 2 + [-0.22342255989482898, -0.2114197791377269, -0.1942289305514992, -0.17277677723311483, -0.1482198103206507, -0.12188190225669181, -0.09518293648227942, -0.06956226115308214, -0.04640109350776134, -0.026948058089121124, -0.01225187307181094, -0.0031048135940796814, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q4.xy.-x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 3.8023000299389026e-19, 1.5004217140952903e-18, 3.3001853082079094e-18, 5.68249506412169e-18, 8.518920046257427e-18, 1.165654784964694e-17, 1.492622814726481e-17, 1.815169162794127e-17, 2.1159052720552927e-17, 2.3786183810170702e-17, 2.5891455579745755e-17, 2.736137228325101e-17] + [2.811669033072674e-17] * 2 + [2.736137228325101e-17, 2.589145557974576e-17, 2.3786183810170705e-17, 2.1159052720552936e-17, 1.8151691627941272e-17, 1.4926228147264817e-17, 1.1656547849646932e-17, 8.518920046257432e-18, 5.6824950641216956e-18, 3.3001853082079125e-18, 1.5004217140952918e-18, 3.8023000299388713e-19, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q4.xy.y180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 3.8023000299389026e-19, 1.5004217140952903e-18, 3.3001853082079094e-18, 5.68249506412169e-18, 8.518920046257427e-18, 1.165654784964694e-17, 1.492622814726481e-17, 1.815169162794127e-17, 2.1159052720552927e-17, 2.3786183810170702e-17, 2.5891455579745755e-17, 2.736137228325101e-17] + [2.811669033072674e-17] * 2 + [2.736137228325101e-17, 2.589145557974576e-17, 2.3786183810170705e-17, 2.1159052720552936e-17, 1.8151691627941272e-17, 1.4926228147264817e-17, 1.1656547849646932e-17, 8.518920046257432e-18, 5.6824950641216956e-18, 3.3001853082079125e-18, 1.5004217140952918e-18, 3.8023000299388713e-19, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q4.xy.y180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.006209627188159414, 0.024503746143621857, 0.0538961161782422, 0.09280218701552259, 0.1391245223061642, 0.19036587296455895, 0.2437638045133835, 0.29643962064130136, 0.3455535544662295, 0.38845786110299835, 0.4228395582754537, 0.44684511978965796] + [0.4591803996107723] * 2 + [0.44684511978965796, 0.4228395582754538, 0.3884578611029984, 0.34555355446622965, 0.2964396206413014, 0.24376380451338361, 0.19036587296455884, 0.1391245223061643, 0.09280218701552267, 0.05389611617824225, 0.02450374614362188, 0.006209627188159363, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q4.xy.y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 1.9011500149694513e-19, 7.502108570476451e-19, 1.6500926541039547e-18, 2.841247532060845e-18, 4.259460023128714e-18, 5.82827392482347e-18, 7.463114073632406e-18, 9.075845813970635e-18, 1.0579526360276463e-17, 1.1893091905085351e-17, 1.2945727789872878e-17, 1.3680686141625505e-17] + [1.405834516536337e-17] * 2 + [1.3680686141625505e-17, 1.294572778987288e-17, 1.1893091905085352e-17, 1.0579526360276468e-17, 9.075845813970636e-18, 7.463114073632409e-18, 5.828273924823466e-18, 4.259460023128716e-18, 2.8412475320608478e-18, 1.6500926541039563e-18, 7.502108570476459e-19, 1.9011500149694357e-19, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q4.xy.y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.003104813594079707, 0.012251873071810929, 0.0269480580891211, 0.046401093507761296, 0.0695622611530821, 0.09518293648227948, 0.12188190225669175, 0.14821981032065068, 0.17277677723311474, 0.19422893055149917, 0.21141977913772686, 0.22342255989482898] + [0.22959019980538614] * 2 + [0.22342255989482898, 0.2114197791377269, 0.1942289305514992, 0.17277677723311483, 0.1482198103206507, 0.12188190225669181, 0.09518293648227942, 0.06956226115308214, 0.04640109350776134, 0.026948058089121124, 0.01225187307181094, 0.0031048135940796814, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q4.xy.-y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 1.9011500149694513e-19, 7.502108570476451e-19, 1.6500926541039547e-18, 2.841247532060845e-18, 4.259460023128714e-18, 5.82827392482347e-18, 7.463114073632406e-18, 9.075845813970635e-18, 1.0579526360276463e-17, 1.1893091905085351e-17, 1.2945727789872878e-17, 1.3680686141625505e-17] + [1.405834516536337e-17] * 2 + [1.3680686141625505e-17, 1.294572778987288e-17, 1.1893091905085352e-17, 1.0579526360276468e-17, 9.075845813970636e-18, 7.463114073632409e-18, 5.828273924823466e-18, 4.259460023128716e-18, 2.8412475320608478e-18, 1.6500926541039563e-18, 7.502108570476459e-19, 1.9011500149694357e-19, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q4.xy.-y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.003104813594079707, -0.012251873071810929, -0.0269480580891211, -0.046401093507761296, -0.0695622611530821, -0.09518293648227948, -0.12188190225669175, -0.14821981032065068, -0.17277677723311474, -0.19422893055149917, -0.21141977913772686, -0.22342255989482898] + [-0.22959019980538614] * 2 + [-0.22342255989482898, -0.2114197791377269, -0.1942289305514992, -0.17277677723311483, -0.1482198103206507, -0.12188190225669181, -0.09518293648227942, -0.06956226115308214, -0.04640109350776134, -0.026948058089121124, -0.01225187307181094, -0.0031048135940796814, 0.0],
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
            "sample": 0.07562669833799542,
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
            "sample": 0.04727070176547587,
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
            "samples": [0.0, 0.004491496794801091, 0.017723849424415995, 0.03898369833351539, 0.06712491956450292, 0.10063041259673244, 0.13769388762826282, 0.17631724312662136, 0.21441828399960858, 0.24994297327167483, 0.2809761657489401, 0.30584485399231237, 0.32320836058157154] + [0.3321306143821144] * 2 + [0.32320836058157154, 0.3058448539923124, 0.28097616574894013, 0.24994297327167495, 0.21441828399960866, 0.17631724312662142, 0.13769388762826276, 0.1006304125967325, 0.06712491956450298, 0.03898369833351543, 0.017723849424416013, 0.004491496794801053, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q5.xy.x180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 28,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q5.xy.x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0022457483974005453, 0.008861924712207998, 0.019491849166757697, 0.03356245978225146, 0.05031520629836622, 0.06884694381413141, 0.08815862156331068, 0.10720914199980429, 0.12497148663583742, 0.14048808287447004, 0.15292242699615619, 0.16160418029078577] + [0.1660653071910572] * 2 + [0.16160418029078577, 0.1529224269961562, 0.14048808287447007, 0.12497148663583747, 0.10720914199980433, 0.08815862156331071, 0.06884694381413138, 0.05031520629836625, 0.03356245978225149, 0.019491849166757714, 0.008861924712208006, 0.0022457483974005267, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q5.xy.x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 28,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q5.xy.-x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -0.0022457483974005453, -0.008861924712207998, -0.019491849166757697, -0.03356245978225146, -0.05031520629836622, -0.06884694381413141, -0.08815862156331068, -0.10720914199980429, -0.12497148663583742, -0.14048808287447004, -0.15292242699615619, -0.16160418029078577] + [-0.1660653071910572] * 2 + [-0.16160418029078577, -0.1529224269961562, -0.14048808287447007, -0.12497148663583747, -0.10720914199980433, -0.08815862156331071, -0.06884694381413138, -0.05031520629836625, -0.03356245978225149, -0.019491849166757714, -0.008861924712208006, -0.0022457483974005267, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q5.xy.-x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 2.750248586566876e-19, 1.0852727733090353e-18, 2.3870630691532816e-18, 4.1102158943846024e-18, 6.161835634173294e-18, 8.43131893730537e-18, 1.0796317371475125e-17, 1.3129333258939439e-17, 1.530459310932645e-17, 1.720482810105678e-17, 1.8727596073868748e-17, 1.9790804212194258e-17] + [2.0337134690095013e-17] * 2 + [1.9790804212194258e-17, 1.872759607386875e-17, 1.7204828101056784e-17, 1.5304593109326458e-17, 1.3129333258939444e-17, 1.079631737147513e-17, 8.431318937305367e-18, 6.161835634173297e-18, 4.1102158943846055e-18, 2.387063069153284e-18, 1.0852727733090364e-18, 2.7502485865668533e-19, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q5.xy.y180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 2.750248586566876e-19, 1.0852727733090353e-18, 2.3870630691532816e-18, 4.1102158943846024e-18, 6.161835634173294e-18, 8.43131893730537e-18, 1.0796317371475125e-17, 1.3129333258939439e-17, 1.530459310932645e-17, 1.720482810105678e-17, 1.8727596073868748e-17, 1.9790804212194258e-17] + [2.0337134690095013e-17] * 2 + [1.9790804212194258e-17, 1.872759607386875e-17, 1.7204828101056784e-17, 1.5304593109326458e-17, 1.3129333258939444e-17, 1.079631737147513e-17, 8.431318937305367e-18, 6.161835634173297e-18, 4.1102158943846055e-18, 2.387063069153284e-18, 1.0852727733090364e-18, 2.7502485865668533e-19, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q5.xy.y180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.004491496794801091, 0.017723849424415995, 0.03898369833351539, 0.06712491956450292, 0.10063041259673244, 0.13769388762826282, 0.17631724312662136, 0.21441828399960858, 0.24994297327167483, 0.2809761657489401, 0.30584485399231237, 0.32320836058157154] + [0.3321306143821144] * 2 + [0.32320836058157154, 0.3058448539923124, 0.28097616574894013, 0.24994297327167495, 0.21441828399960866, 0.17631724312662142, 0.13769388762826276, 0.1006304125967325, 0.06712491956450298, 0.03898369833351543, 0.017723849424416013, 0.004491496794801053, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q5.xy.y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 1.375124293283438e-19, 5.426363866545176e-19, 1.1935315345766408e-18, 2.0551079471923012e-18, 3.080917817086647e-18, 4.215659468652685e-18, 5.3981586857375626e-18, 6.5646666294697195e-18, 7.652296554663226e-18, 8.60241405052839e-18, 9.363798036934374e-18, 9.895402106097129e-18] + [1.0168567345047506e-17] * 2 + [9.895402106097129e-18, 9.363798036934376e-18, 8.602414050528392e-18, 7.652296554663229e-18, 6.564666629469722e-18, 5.398158685737565e-18, 4.215659468652683e-18, 3.0809178170866486e-18, 2.0551079471923027e-18, 1.193531534576642e-18, 5.426363866545182e-19, 1.3751242932834267e-19, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q5.xy.y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0022457483974005453, 0.008861924712207998, 0.019491849166757697, 0.03356245978225146, 0.05031520629836622, 0.06884694381413141, 0.08815862156331068, 0.10720914199980429, 0.12497148663583742, 0.14048808287447004, 0.15292242699615619, 0.16160418029078577] + [0.1660653071910572] * 2 + [0.16160418029078577, 0.1529224269961562, 0.14048808287447007, 0.12497148663583747, 0.10720914199980433, 0.08815862156331071, 0.06884694381413138, 0.05031520629836625, 0.03356245978225149, 0.019491849166757714, 0.008861924712208006, 0.0022457483974005267, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q5.xy.-y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 1.375124293283438e-19, 5.426363866545176e-19, 1.1935315345766408e-18, 2.0551079471923012e-18, 3.080917817086647e-18, 4.215659468652685e-18, 5.3981586857375626e-18, 6.5646666294697195e-18, 7.652296554663226e-18, 8.60241405052839e-18, 9.363798036934374e-18, 9.895402106097129e-18] + [1.0168567345047506e-17] * 2 + [9.895402106097129e-18, 9.363798036934376e-18, 8.602414050528392e-18, 7.652296554663229e-18, 6.564666629469722e-18, 5.398158685737565e-18, 4.215659468652683e-18, 3.0809178170866486e-18, 2.0551079471923027e-18, 1.193531534576642e-18, 5.426363866545182e-19, 1.3751242932834267e-19, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q5.xy.-y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.0022457483974005453, -0.008861924712207998, -0.019491849166757697, -0.03356245978225146, -0.05031520629836622, -0.06884694381413141, -0.08815862156331068, -0.10720914199980429, -0.12497148663583742, -0.14048808287447004, -0.15292242699615619, -0.16160418029078577] + [-0.1660653071910572] * 2 + [-0.16160418029078577, -0.1529224269961562, -0.14048808287447007, -0.12497148663583747, -0.10720914199980433, -0.08815862156331071, -0.06884694381413138, -0.05031520629836625, -0.03356245978225149, -0.019491849166757714, -0.008861924712208006, -0.0022457483974005267, 0.0],
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
            "sample": 0.0465830919328653,
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
            "sample": 0.05116362917943104,
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
            "samples": [0.0, 0.005479424617822204, 0.02162230127184579, 0.04755836330322451, 0.08188939089454725, 0.12276458946211057, 0.1679803664709863, 0.21509912767895834, 0.26158068847306815, 0.3049192158796016, 0.34277831866831293, 0.3731170028083991, 0.3942997019849924] + [0.40518445140254544] * 2 + [0.3942997019849924, 0.3731170028083991, 0.34277831866831293, 0.3049192158796017, 0.2615806884730682, 0.21509912767895842, 0.16798036647098621, 0.12276458946211063, 0.08188939089454732, 0.04755836330322455, 0.021622301271845813, 0.005479424617822159, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q6.xy.x180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 28,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q6.xy.x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.002739712308911102, 0.010811150635922894, 0.023779181651612254, 0.040944695447273624, 0.06138229473105528, 0.08399018323549315, 0.10754956383947917, 0.13079034423653407, 0.1524596079398008, 0.17138915933415647, 0.18655850140419955, 0.1971498509924962] + [0.20259222570127272] * 2 + [0.1971498509924962, 0.18655850140419955, 0.17138915933415647, 0.15245960793980085, 0.1307903442365341, 0.10754956383947921, 0.08399018323549311, 0.06138229473105532, 0.04094469544727366, 0.023779181651612274, 0.010811150635922907, 0.0027397123089110795, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q6.xy.x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 28,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q6.xy.-x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -0.002739712308911102, -0.010811150635922894, -0.023779181651612254, -0.040944695447273624, -0.06138229473105528, -0.08399018323549315, -0.10754956383947917, -0.13079034423653407, -0.1524596079398008, -0.17138915933415647, -0.18655850140419955, -0.1971498509924962] + [-0.20259222570127272] * 2 + [-0.1971498509924962, -0.18655850140419955, -0.17138915933415647, -0.15245960793980085, -0.1307903442365341, -0.10754956383947921, -0.08399018323549311, -0.06138229473105532, -0.04094469544727366, -0.023779181651612274, -0.010811150635922907, -0.0027397123089110795, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q6.xy.-x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 3.355179909692586e-19, 1.3239841021382845e-18, 2.912109869599042e-18, 5.014279022156685e-18, 7.51716307667063e-18, 1.0285830905914637e-17, 1.3171022910571209e-17, 1.6017197642865192e-17, 1.8670917086273743e-17, 2.0989118538713044e-17, 2.2846827159837997e-17, 2.4143893397033812e-17] + [2.481039207372018e-17] * 2 + [2.4143893397033812e-17, 2.2846827159837997e-17, 2.0989118538713044e-17, 1.867091708627375e-17, 1.6017197642865195e-17, 1.3171022910571213e-17, 1.0285830905914632e-17, 7.517163076670633e-18, 5.014279022156689e-18, 2.9121098695990443e-18, 1.323984102138286e-18, 3.355179909692558e-19, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q6.xy.y180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 3.355179909692586e-19, 1.3239841021382845e-18, 2.912109869599042e-18, 5.014279022156685e-18, 7.51716307667063e-18, 1.0285830905914637e-17, 1.3171022910571209e-17, 1.6017197642865192e-17, 1.8670917086273743e-17, 2.0989118538713044e-17, 2.2846827159837997e-17, 2.4143893397033812e-17] + [2.481039207372018e-17] * 2 + [2.4143893397033812e-17, 2.2846827159837997e-17, 2.0989118538713044e-17, 1.867091708627375e-17, 1.6017197642865195e-17, 1.3171022910571213e-17, 1.0285830905914632e-17, 7.517163076670633e-18, 5.014279022156689e-18, 2.9121098695990443e-18, 1.323984102138286e-18, 3.355179909692558e-19, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q6.xy.y180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.005479424617822204, 0.02162230127184579, 0.04755836330322451, 0.08188939089454725, 0.12276458946211057, 0.1679803664709863, 0.21509912767895834, 0.26158068847306815, 0.3049192158796016, 0.34277831866831293, 0.3731170028083991, 0.3942997019849924] + [0.40518445140254544] * 2 + [0.3942997019849924, 0.3731170028083991, 0.34277831866831293, 0.3049192158796017, 0.2615806884730682, 0.21509912767895842, 0.16798036647098621, 0.12276458946211063, 0.08188939089454732, 0.04755836330322455, 0.021622301271845813, 0.005479424617822159, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q6.xy.y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 1.677589954846293e-19, 6.619920510691423e-19, 1.456054934799521e-18, 2.5071395110783426e-18, 3.758581538335315e-18, 5.142915452957318e-18, 6.585511455285604e-18, 8.008598821432596e-18, 9.335458543136871e-18, 1.0494559269356522e-17, 1.1423413579918998e-17, 1.2071946698516906e-17] + [1.240519603686009e-17] * 2 + [1.2071946698516906e-17, 1.1423413579918998e-17, 1.0494559269356522e-17, 9.335458543136874e-18, 8.008598821432598e-18, 6.5855114552856066e-18, 5.142915452957316e-18, 3.7585815383353166e-18, 2.5071395110783445e-18, 1.4560549347995221e-18, 6.61992051069143e-19, 1.677589954846279e-19, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q6.xy.y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.002739712308911102, 0.010811150635922894, 0.023779181651612254, 0.040944695447273624, 0.06138229473105528, 0.08399018323549315, 0.10754956383947917, 0.13079034423653407, 0.1524596079398008, 0.17138915933415647, 0.18655850140419955, 0.1971498509924962] + [0.20259222570127272] * 2 + [0.1971498509924962, 0.18655850140419955, 0.17138915933415647, 0.15245960793980085, 0.1307903442365341, 0.10754956383947921, 0.08399018323549311, 0.06138229473105532, 0.04094469544727366, 0.023779181651612274, 0.010811150635922907, 0.0027397123089110795, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q6.xy.-y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 1.677589954846293e-19, 6.619920510691423e-19, 1.456054934799521e-18, 2.5071395110783426e-18, 3.758581538335315e-18, 5.142915452957318e-18, 6.585511455285604e-18, 8.008598821432596e-18, 9.335458543136871e-18, 1.0494559269356522e-17, 1.1423413579918998e-17, 1.2071946698516906e-17] + [1.240519603686009e-17] * 2 + [1.2071946698516906e-17, 1.1423413579918998e-17, 1.0494559269356522e-17, 9.335458543136874e-18, 8.008598821432598e-18, 6.5855114552856066e-18, 5.142915452957316e-18, 3.7585815383353166e-18, 2.5071395110783445e-18, 1.4560549347995221e-18, 6.61992051069143e-19, 1.677589954846279e-19, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q6.xy.-y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.002739712308911102, -0.010811150635922894, -0.023779181651612254, -0.040944695447273624, -0.06138229473105528, -0.08399018323549315, -0.10754956383947917, -0.13079034423653407, -0.1524596079398008, -0.17138915933415647, -0.18655850140419955, -0.1971498509924962] + [-0.20259222570127272] * 2 + [-0.1971498509924962, -0.18655850140419955, -0.17138915933415647, -0.15245960793980085, -0.1307903442365341, -0.10754956383947921, -0.08399018323549311, -0.06138229473105532, -0.04094469544727366, -0.023779181651612274, -0.010811150635922907, -0.0027397123089110795, 0.0],
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
            "sample": 0.053813886347604395,
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
            "sample": 0.09594356747997401,
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
            "samples": [0.0, 0.0012146810013134736, 0.00479324023806462, 0.010542756655524661, 0.01815327233542146, 0.027214502407543226, 0.03723795361328989, 0.04768325910368601, 0.05798730975607778, 0.06759461153269064, 0.07598723230799004, 0.08271272372363064, 0.08740851279656674] + [0.0898214483224166] * 2 + [0.08740851279656674, 0.08271272372363066, 0.07598723230799005, 0.06759461153269067, 0.0579873097560778, 0.04768325910368603, 0.03723795361328987, 0.027214502407543244, 0.018153272335421473, 0.01054275665552467, 0.004793240238064625, 0.0012146810013134637, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q7.xy.x180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 28,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q7.xy.x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0006073405006567368, 0.00239662011903231, 0.0052713783277623305, 0.00907663616771073, 0.013607251203771613, 0.018618976806644944, 0.023841629551843005, 0.02899365487803889, 0.03379730576634532, 0.03799361615399502, 0.04135636186181532, 0.04370425639828337] + [0.0449107241612083] * 2 + [0.04370425639828337, 0.04135636186181533, 0.037993616153995026, 0.033797305766345334, 0.0289936548780389, 0.023841629551843015, 0.018618976806644934, 0.013607251203771622, 0.009076636167710737, 0.005271378327762335, 0.0023966201190323126, 0.0006073405006567318, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q7.xy.x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 28,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q7.xy.-x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -0.0006073405006567368, -0.00239662011903231, -0.0052713783277623305, -0.00907663616771073, -0.013607251203771613, -0.018618976806644944, -0.023841629551843005, -0.02899365487803889, -0.03379730576634532, -0.03799361615399502, -0.04135636186181532, -0.04370425639828337] + [-0.0449107241612083] * 2 + [-0.04370425639828337, -0.04135636186181533, -0.037993616153995026, -0.033797305766345334, -0.0289936548780389, -0.023841629551843015, -0.018618976806644934, -0.013607251203771622, -0.009076636167710737, -0.005271378327762335, -0.0023966201190323126, -0.0006073405006567318, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q7.xy.-x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 7.437776001218238e-20, 2.935013157545067e-19, 6.455576596188865e-19, 1.1115673429812044e-18, 1.6664076631892876e-18, 2.280167034965654e-18, 2.919757531712148e-18, 3.550698664197337e-18, 4.138976232655918e-18, 4.652876041102317e-18, 5.064693617845181e-18, 5.3522277707272955e-18] + [5.499977459141345e-18] * 2 + [5.3522277707272955e-18, 5.064693617845182e-18, 4.652876041102318e-18, 4.13897623265592e-18, 3.550698664197338e-18, 2.9197575317121495e-18, 2.2801670349656525e-18, 1.6664076631892885e-18, 1.1115673429812052e-18, 6.455576596188871e-19, 2.93501315754507e-19, 7.437776001218176e-20, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q7.xy.y180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 7.437776001218238e-20, 2.935013157545067e-19, 6.455576596188865e-19, 1.1115673429812044e-18, 1.6664076631892876e-18, 2.280167034965654e-18, 2.919757531712148e-18, 3.550698664197337e-18, 4.138976232655918e-18, 4.652876041102317e-18, 5.064693617845181e-18, 5.3522277707272955e-18] + [5.499977459141345e-18] * 2 + [5.3522277707272955e-18, 5.064693617845182e-18, 4.652876041102318e-18, 4.13897623265592e-18, 3.550698664197338e-18, 2.9197575317121495e-18, 2.2801670349656525e-18, 1.6664076631892885e-18, 1.1115673429812052e-18, 6.455576596188871e-19, 2.93501315754507e-19, 7.437776001218176e-20, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q7.xy.y180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0012146810013134736, 0.00479324023806462, 0.010542756655524661, 0.01815327233542146, 0.027214502407543226, 0.03723795361328989, 0.04768325910368601, 0.05798730975607778, 0.06759461153269064, 0.07598723230799004, 0.08271272372363064, 0.08740851279656674] + [0.0898214483224166] * 2 + [0.08740851279656674, 0.08271272372363066, 0.07598723230799005, 0.06759461153269067, 0.0579873097560778, 0.04768325910368603, 0.03723795361328987, 0.027214502407543244, 0.018153272335421473, 0.01054275665552467, 0.004793240238064625, 0.0012146810013134637, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q7.xy.y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 3.718888000609119e-20, 1.4675065787725336e-19, 3.2277882980944326e-19, 5.557836714906022e-19, 8.332038315946438e-19, 1.140083517482827e-18, 1.459878765856074e-18, 1.7753493320986683e-18, 2.069488116327959e-18, 2.3264380205511587e-18, 2.5323468089225905e-18, 2.6761138853636477e-18] + [2.7499887295706724e-18] * 2 + [2.6761138853636477e-18, 2.532346808922591e-18, 2.326438020551159e-18, 2.06948811632796e-18, 1.775349332098669e-18, 1.4598787658560747e-18, 1.1400835174828263e-18, 8.332038315946443e-19, 5.557836714906026e-19, 3.2277882980944355e-19, 1.467506578772535e-19, 3.718888000609088e-20, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q7.xy.y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0006073405006567368, 0.00239662011903231, 0.0052713783277623305, 0.00907663616771073, 0.013607251203771613, 0.018618976806644944, 0.023841629551843005, 0.02899365487803889, 0.03379730576634532, 0.03799361615399502, 0.04135636186181532, 0.04370425639828337] + [0.0449107241612083] * 2 + [0.04370425639828337, 0.04135636186181533, 0.037993616153995026, 0.033797305766345334, 0.0289936548780389, 0.023841629551843015, 0.018618976806644934, 0.013607251203771622, 0.009076636167710737, 0.005271378327762335, 0.0023966201190323126, 0.0006073405006567318, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q7.xy.-y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 3.718888000609119e-20, 1.4675065787725336e-19, 3.2277882980944326e-19, 5.557836714906022e-19, 8.332038315946438e-19, 1.140083517482827e-18, 1.459878765856074e-18, 1.7753493320986683e-18, 2.069488116327959e-18, 2.3264380205511587e-18, 2.5323468089225905e-18, 2.6761138853636477e-18] + [2.7499887295706724e-18] * 2 + [2.6761138853636477e-18, 2.532346808922591e-18, 2.326438020551159e-18, 2.06948811632796e-18, 1.775349332098669e-18, 1.4598787658560747e-18, 1.1400835174828263e-18, 8.332038315946443e-19, 5.557836714906026e-19, 3.2277882980944355e-19, 1.467506578772535e-19, 3.718888000609088e-20, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q7.xy.-y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.0006073405006567368, -0.00239662011903231, -0.0052713783277623305, -0.00907663616771073, -0.013607251203771613, -0.018618976806644944, -0.023841629551843005, -0.02899365487803889, -0.03379730576634532, -0.03799361615399502, -0.04135636186181532, -0.04370425639828337] + [-0.0449107241612083] * 2 + [-0.04370425639828337, -0.04135636186181533, -0.037993616153995026, -0.033797305766345334, -0.0289936548780389, -0.023841629551843015, -0.018618976806644934, -0.013607251203771622, -0.009076636167710737, -0.005271378327762335, -0.0023966201190323126, -0.0006073405006567318, 0.0],
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
            "sample": 0.014047598378514256,
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
            "sample": 0.03894542288996688,
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
            "samples": [0.0, 0.0050733579843309055, 0.020019925895198545, 0.04403393038775318, 0.07582077026400777, 0.11366680875851662, 0.1555317561399588, 0.19915866225866305, 0.2421955893133663, 0.282322405426856, 0.3173758635560149, 0.34546622269985044, 0.36507912432600015] + [0.3751572318311877] * 2 + [0.36507912432600015, 0.3454662226998505, 0.31737586355601494, 0.28232240542685616, 0.24219558931336638, 0.19915866225866313, 0.1555317561399587, 0.11366680875851667, 0.07582077026400783, 0.044033930387753224, 0.02001992589519857, 0.005073357984330864, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q8.xy.x180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 28,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q8.xy.x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0025366789921654528, 0.010009962947599272, 0.02201696519387659, 0.037910385132003885, 0.05683340437925831, 0.0777658780699794, 0.09957933112933152, 0.12109779465668315, 0.141161202713428, 0.15868793177800744, 0.17273311134992522, 0.18253956216300007] + [0.18757861591559385] * 2 + [0.18253956216300007, 0.17273311134992525, 0.15868793177800747, 0.14116120271342808, 0.12109779465668319, 0.09957933112933157, 0.07776587806997935, 0.05683340437925834, 0.03791038513200391, 0.022016965193876612, 0.010009962947599284, 0.002536678992165432, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q8.xy.x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 28,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q8.xy.-x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -0.0025366789921654528, -0.010009962947599272, -0.02201696519387659, -0.037910385132003885, -0.05683340437925831, -0.0777658780699794, -0.09957933112933152, -0.12109779465668315, -0.141161202713428, -0.15868793177800744, -0.17273311134992522, -0.18253956216300007] + [-0.18757861591559385] * 2 + [-0.18253956216300007, -0.17273311134992525, -0.15868793177800747, -0.14116120271342808, -0.12109779465668319, -0.09957933112933157, -0.07776587806997935, -0.05683340437925834, -0.03791038513200391, -0.022016965193876612, -0.010009962947599284, -0.002536678992165432, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q8.xy.-x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 3.1065358082197554e-19, 1.2258669083361053e-18, 2.6963005951619652e-18, 4.6426831806351964e-18, 6.960084675770586e-18, 9.523573366128362e-18, 1.2194950912877024e-17, 1.4830202661011046e-17, 1.7287261506679028e-17, 1.9433666771525036e-17, 2.1153705192144928e-17, 2.2354649052067734e-17] + [2.297175515695228e-17] * 2 + [2.2354649052067734e-17, 2.115370519214493e-17, 1.943366677152504e-17, 1.7287261506679037e-17, 1.4830202661011052e-17, 1.2194950912877029e-17, 9.523573366128356e-18, 6.960084675770589e-18, 4.6426831806352e-18, 2.696300595161968e-18, 1.2258669083361068e-18, 3.1065358082197303e-19, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q8.xy.y180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 3.1065358082197554e-19, 1.2258669083361053e-18, 2.6963005951619652e-18, 4.6426831806351964e-18, 6.960084675770586e-18, 9.523573366128362e-18, 1.2194950912877024e-17, 1.4830202661011046e-17, 1.7287261506679028e-17, 1.9433666771525036e-17, 2.1153705192144928e-17, 2.2354649052067734e-17] + [2.297175515695228e-17] * 2 + [2.2354649052067734e-17, 2.115370519214493e-17, 1.943366677152504e-17, 1.7287261506679037e-17, 1.4830202661011052e-17, 1.2194950912877029e-17, 9.523573366128356e-18, 6.960084675770589e-18, 4.6426831806352e-18, 2.696300595161968e-18, 1.2258669083361068e-18, 3.1065358082197303e-19, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q8.xy.y180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0050733579843309055, 0.020019925895198545, 0.04403393038775318, 0.07582077026400777, 0.11366680875851662, 0.1555317561399588, 0.19915866225866305, 0.2421955893133663, 0.282322405426856, 0.3173758635560149, 0.34546622269985044, 0.36507912432600015] + [0.3751572318311877] * 2 + [0.36507912432600015, 0.3454662226998505, 0.31737586355601494, 0.28232240542685616, 0.24219558931336638, 0.19915866225866313, 0.1555317561399587, 0.11366680875851667, 0.07582077026400783, 0.044033930387753224, 0.02001992589519857, 0.005073357984330864, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q8.xy.y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 1.5532679041098777e-19, 6.129334541680526e-19, 1.3481502975809826e-18, 2.3213415903175982e-18, 3.480042337885293e-18, 4.761786683064181e-18, 6.097475456438512e-18, 7.415101330505523e-18, 8.643630753339514e-18, 9.716833385762518e-18, 1.0576852596072464e-17, 1.1177324526033867e-17] + [1.148587757847614e-17] * 2 + [1.1177324526033867e-17, 1.0576852596072466e-17, 9.71683338576252e-18, 8.643630753339519e-18, 7.415101330505526e-18, 6.097475456438514e-18, 4.761786683064178e-18, 3.4800423378852945e-18, 2.3213415903176e-18, 1.348150297580984e-18, 6.129334541680534e-19, 1.5532679041098652e-19, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q8.xy.y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0025366789921654528, 0.010009962947599272, 0.02201696519387659, 0.037910385132003885, 0.05683340437925831, 0.0777658780699794, 0.09957933112933152, 0.12109779465668315, 0.141161202713428, 0.15868793177800744, 0.17273311134992522, 0.18253956216300007] + [0.18757861591559385] * 2 + [0.18253956216300007, 0.17273311134992525, 0.15868793177800747, 0.14116120271342808, 0.12109779465668319, 0.09957933112933157, 0.07776587806997935, 0.05683340437925834, 0.03791038513200391, 0.022016965193876612, 0.010009962947599284, 0.002536678992165432, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q8.xy.-y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 1.5532679041098777e-19, 6.129334541680526e-19, 1.3481502975809826e-18, 2.3213415903175982e-18, 3.480042337885293e-18, 4.761786683064181e-18, 6.097475456438512e-18, 7.415101330505523e-18, 8.643630753339514e-18, 9.716833385762518e-18, 1.0576852596072464e-17, 1.1177324526033867e-17] + [1.148587757847614e-17] * 2 + [1.1177324526033867e-17, 1.0576852596072466e-17, 9.71683338576252e-18, 8.643630753339519e-18, 7.415101330505526e-18, 6.097475456438514e-18, 4.761786683064178e-18, 3.4800423378852945e-18, 2.3213415903176e-18, 1.348150297580984e-18, 6.129334541680534e-19, 1.5532679041098652e-19, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q8.xy.-y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.0025366789921654528, -0.010009962947599272, -0.02201696519387659, -0.037910385132003885, -0.05683340437925831, -0.0777658780699794, -0.09957933112933152, -0.12109779465668315, -0.141161202713428, -0.15868793177800744, -0.17273311134992522, -0.18253956216300007] + [-0.18757861591559385] * 2 + [-0.18253956216300007, -0.17273311134992525, -0.15868793177800747, -0.14116120271342808, -0.12109779465668319, -0.09957933112933157, -0.07776587806997935, -0.05683340437925834, -0.03791038513200391, -0.022016965193876612, -0.010009962947599284, -0.002536678992165432, 0.0],
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
            "sample": 0.05886600096490788,
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
            "sample": 0.07311249761928179,
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
            "sample": -0.08976901035867871,
        },
        "cr_q1_q2.square.wf.Q": {
            "type": "constant",
            "sample": -0.12017289536007456,
        },
        "zz_q1_q2.square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "zz_q1_q2.square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "cr_q2_q1.square.wf.I": {
            "type": "constant",
            "sample": -0.22442252589669678,
        },
        "cr_q2_q1.square.wf.Q": {
            "type": "constant",
            "sample": -0.3004322384001864,
        },
        "cr_q2_q3.square.wf.I": {
            "type": "constant",
            "sample": -0.014961501726446454,
        },
        "cr_q2_q3.square.wf.Q": {
            "type": "constant",
            "sample": -0.020028815893345764,
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
            "cosine": [(-0.35085202724936854, 2000)],
            "sine": [(0.9364309130816904, 2000)],
        },
        "q1.resonator.readout.iw2": {
            "cosine": [(-0.9364309130816904, 2000)],
            "sine": [(-0.35085202724936854, 2000)],
        },
        "q1.resonator.readout.iw3": {
            "cosine": [(0.9364309130816904, 2000)],
            "sine": [(0.35085202724936854, 2000)],
        },
        "q2.resonator.readout.iw1": {
            "cosine": [(-0.1180848483063911, 2500)],
            "sine": [(-0.9930035088560647, 2500)],
        },
        "q2.resonator.readout.iw2": {
            "cosine": [(0.9930035088560647, 2500)],
            "sine": [(-0.1180848483063911, 2500)],
        },
        "q2.resonator.readout.iw3": {
            "cosine": [(-0.9930035088560647, 2500)],
            "sine": [(0.1180848483063911, 2500)],
        },
        "q3.resonator.readout.iw1": {
            "cosine": [(0.9468898519242067, 2000)],
            "sine": [(0.32155809478685793, 2000)],
        },
        "q3.resonator.readout.iw2": {
            "cosine": [(-0.32155809478685793, 2000)],
            "sine": [(0.9468898519242067, 2000)],
        },
        "q3.resonator.readout.iw3": {
            "cosine": [(0.32155809478685793, 2000)],
            "sine": [(-0.9468898519242067, 2000)],
        },
        "q4.resonator.readout.iw1": {
            "cosine": [(-0.3121146787814643, 2000)],
            "sine": [(-0.9500444343761735, 2000)],
        },
        "q4.resonator.readout.iw2": {
            "cosine": [(0.9500444343761735, 2000)],
            "sine": [(-0.3121146787814643, 2000)],
        },
        "q4.resonator.readout.iw3": {
            "cosine": [(-0.9500444343761735, 2000)],
            "sine": [(0.3121146787814643, 2000)],
        },
        "q5.resonator.readout.iw1": {
            "cosine": [(-0.9965476171382793, 2000)],
            "sine": [(0.08302317011544058, 2000)],
        },
        "q5.resonator.readout.iw2": {
            "cosine": [(-0.08302317011544058, 2000)],
            "sine": [(-0.9965476171382793, 2000)],
        },
        "q5.resonator.readout.iw3": {
            "cosine": [(0.08302317011544058, 2000)],
            "sine": [(0.9965476171382793, 2000)],
        },
        "q6.resonator.readout.iw1": {
            "cosine": [(-0.8114511176826852, 2000)],
            "sine": [(0.5844202970564258, 2000)],
        },
        "q6.resonator.readout.iw2": {
            "cosine": [(-0.5844202970564258, 2000)],
            "sine": [(-0.8114511176826852, 2000)],
        },
        "q6.resonator.readout.iw3": {
            "cosine": [(0.5844202970564258, 2000)],
            "sine": [(0.8114511176826852, 2000)],
        },
        "q7.resonator.readout.iw1": {
            "cosine": [(-0.9929690166473447, 2000)],
            "sine": [(-0.1183745410905795, 2000)],
        },
        "q7.resonator.readout.iw2": {
            "cosine": [(0.1183745410905795, 2000)],
            "sine": [(-0.9929690166473447, 2000)],
        },
        "q7.resonator.readout.iw3": {
            "cosine": [(-0.1183745410905795, 2000)],
            "sine": [(0.9929690166473447, 2000)],
        },
        "q8.resonator.readout.iw1": {
            "cosine": [(0.7452364606756877, 2000)],
            "sine": [(0.6668002832029799, 2000)],
        },
        "q8.resonator.readout.iw2": {
            "cosine": [(-0.6668002832029799, 2000)],
            "sine": [(0.7452364606756877, 2000)],
        },
        "q8.resonator.readout.iw3": {
            "cosine": [(0.6668002832029799, 2000)],
            "sine": [(-0.7452364606756877, 2000)],
        },
    },
    "mixers": {},
}


