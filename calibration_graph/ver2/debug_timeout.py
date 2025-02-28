
# Single QUA script generated at 2024-12-11 12:46:09.112973
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
            with for_(v18,0.0,(v18<1.9875),(v18+0.005)):
                wait(22274, "q1.xy", "q1.resonator")
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
        with for_(v19,1,(v19<=1),(v19+1)):
            with for_(v18,0.0,(v18<1.9875),(v18+0.005)):
                wait(35681, "q2.xy", "q2.resonator")
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
        with for_(v19,1,(v19<=1),(v19+1)):
            with for_(v18,0.0,(v18<1.9875),(v18+0.005)):
                wait(55088, "q3.xy", "q3.resonator")
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
        with for_(v19,1,(v19<=1),(v19+1)):
            with for_(v18,0.0,(v18<1.9875),(v18+0.005)):
                wait(45154, "q4.xy", "q4.resonator")
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
        with for_(v19,1,(v19<=1),(v19+1)):
            with for_(v18,0.0,(v18<1.9875),(v18+0.005)):
                wait(41144, "q5.xy", "q5.resonator")
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
        with for_(v19,1,(v19<=1),(v19+1)):
            with for_(v18,0.0,(v18<1.9875),(v18+0.005)):
                wait(35817, "q6.xy", "q6.resonator")
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
        with for_(v19,1,(v19<=1),(v19+1)):
            with for_(v18,0.0,(v18<1.9875),(v18+0.005)):
                wait(17381, "q7.xy", "q7.resonator")
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
        with for_(v19,1,(v19<=1),(v19+1)):
            with for_(v18,0.0,(v18<1.9875),(v18+0.005)):
                wait(35516, "q8.xy", "q8.resonator")
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
                            "full_scale_power_dbm": -17,
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
                            "full_scale_power_dbm": -17,
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
                            "full_scale_power_dbm": -17,
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
                            "full_scale_power_dbm": -17,
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
                            "full_scale_power_dbm": -17,
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
                            "full_scale_power_dbm": -17,
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
                            "full_scale_power_dbm": -17,
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
                            "full_scale_power_dbm": -17,
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
                "cr_q2_q1_Square": "q1.xy.cr_q2_q1_Square.pulse",
            },
            "intermediate_frequency": 51426404.60324453,
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
            "intermediate_frequency": 50120905,
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
            "intermediate_frequency": 50771317.958204485,
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
            "intermediate_frequency": 50674765,
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
            "intermediate_frequency": 47605795.797873005,
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
            "intermediate_frequency": 50288915,
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
            "intermediate_frequency": 50840259.77639715,
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
            "intermediate_frequency": 49481765,
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
            "intermediate_frequency": 49910259.46311582,
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
            "intermediate_frequency": 51021316,
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
            "intermediate_frequency": 51203539.02641499,
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
            "intermediate_frequency": 51257184.30678039,
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
            "intermediate_frequency": 50840298.0896424,
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
            "intermediate_frequency": -180228682.04179573,
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
            "intermediate_frequency": 282426404.6032448,
            "MWInput": {
                "port": ('con1', 2, 3),
                "upconverter": 1,
            },
        },
        "cr_q2_q3": {
            "operations": {
                "square": "cr_q2_q3.square.pulse",
            },
            "intermediate_frequency": 30605795.797872543,
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
            "samples": [0.0, 0.003138527302470915, 0.0123730182654633, 0.027170784793859648, 0.046678667260076516, 0.06977285303236916, 0.09512443172624098, 0.12127680051438272, 0.1467303358760095, 0.17002932633834628, 0.18984603897108973, 0.2050569773632444, 0.21480686869964116, 0.21855666270889954, 0.21611279005089107, 0.20763605336456972, 0.19362974236906597, 0.17490780139626133, 0.15254505895735265, 0.12781258350691474, 0.10210209453759578, 0.07684398236343083, 0.05342383711833801, 0.0331024382869832, 0.01694390926588425, 0.005756213868943394, 4.739714754167214e-05, -2.9058699871086474e-18],
        },
        "q1.xy.x180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.005662928898113587, -0.01068177932598392, -0.014460206436451276, -0.016494004550194924, -0.016409080609930897, -0.013990324906695654, -0.009199322567811228, -0.002179603673422463, 0.00675102531915266, 0.01712064680605409, 0.02833461630646744, 0.03971611331165615, 0.050553164009714824, 0.06014897490618011, 0.06787215806436933, 0.0732033968929995, 0.07577529987269063, 0.07540260702143868, 0.0721005245178405, 0.06608972817123616, 0.05778744739789006, 0.04778496180068675, 0.036812752447151556, 0.02569538976720347, 0.01529895396625175, 0.006474323968095041, 5.334881265600878e-18],
        },
        "q1.xy.x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0015692636512354575, 0.00618650913273165, 0.013585392396929824, 0.023339333630038258, 0.03488642651618458, 0.04756221586312049, 0.06063840025719136, 0.07336516793800475, 0.08501466316917314, 0.09492301948554487, 0.1025284886816222, 0.10740343434982058, 0.10927833135444977, 0.10805639502544553, 0.10381802668228486, 0.09681487118453298, 0.08745390069813067, 0.07627252947867633, 0.06390629175345737, 0.05105104726879789, 0.038421991181715416, 0.026711918559169004, 0.0165512191434916, 0.008471954632942124, 0.002878106934471697, 2.369857377083607e-05, -1.4529349935543237e-18],
        },
        "q1.xy.x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.0028314644490567936, -0.00534088966299196, -0.007230103218225638, -0.008247002275097462, -0.008204540304965448, -0.006995162453347827, -0.004599661283905614, -0.0010898018367112316, 0.00337551265957633, 0.008560323403027046, 0.01416730815323372, 0.019858056655828075, 0.025276582004857412, 0.030074487453090055, 0.033936079032184666, 0.03660169844649975, 0.037887649936345316, 0.03770130351071934, 0.03605026225892025, 0.03304486408561808, 0.02889372369894503, 0.023892480900343373, 0.018406376223575778, 0.012847694883601735, 0.007649476983125875, 0.0032371619840475207, 2.667440632800439e-18],
        },
        "q1.xy.-x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -0.001569263651235457, -0.006186509132731649, -0.013585392396929822, -0.023339333630038258, -0.03488642651618458, -0.04756221586312049, -0.06063840025719136, -0.07336516793800475, -0.08501466316917314, -0.09492301948554487, -0.1025284886816222, -0.10740343434982058, -0.10927833135444977, -0.10805639502544553, -0.10381802668228486, -0.09681487118453298, -0.08745390069813067, -0.07627252947867633, -0.06390629175345737, -0.051051047268797896, -0.03842199118171542, -0.026711918559169007, -0.016551219143491603, -0.008471954632942126, -0.002878106934471698, -2.3698573770836465e-05, 1.4529349935543233e-18],
        },
        "q1.xy.-x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0028314644490567936, 0.0053408896629919605, 0.00723010321822564, 0.008247002275097465, 0.008204540304965452, 0.006995162453347833, 0.004599661283905622, 0.0010898018367112405, -0.0033755126595763196, -0.008560323403027034, -0.014167308153233709, -0.01985805665582806, -0.025276582004857398, -0.03007448745309004, -0.03393607903218465, -0.036601698446499735, -0.0378876499363453, -0.03770130351071933, -0.036050262258920246, -0.033044864085618075, -0.028893723698945026, -0.02389248090034337, -0.018406376223575775, -0.012847694883601733, -0.007649476983125875, -0.0032371619840475207, -2.667440632800439e-18],
        },
        "q1.xy.y180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.005662928898113587, 0.01068177932598392, 0.014460206436451278, 0.016494004550194927, 0.0164090806099309, 0.01399032490669566, 0.009199322567811235, 0.0021796036734224723, -0.0067510253191526495, -0.01712064680605408, -0.028334616306467428, -0.039716113311656136, -0.05055316400971481, -0.0601489749061801, -0.06787215806436932, -0.07320339689299948, -0.07577529987269062, -0.07540260702143867, -0.07210052451784049, -0.06608972817123616, -0.05778744739789005, -0.04778496180068675, -0.036812752447151556, -0.02569538976720347, -0.01529895396625175, -0.006474323968095041, -5.334881265600878e-18],
        },
        "q1.xy.y180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0031385273024709145, 0.0123730182654633, 0.027170784793859648, 0.046678667260076516, 0.06977285303236916, 0.09512443172624098, 0.12127680051438272, 0.1467303358760095, 0.17002932633834628, 0.18984603897108973, 0.2050569773632444, 0.21480686869964116, 0.21855666270889954, 0.21611279005089107, 0.20763605336456972, 0.19362974236906597, 0.17490780139626133, 0.15254505895735265, 0.12781258350691474, 0.10210209453759578, 0.07684398236343083, 0.05342383711833801, 0.0331024382869832, 0.01694390926588425, 0.005756213868943395, 4.739714754167254e-05, -2.905869987108647e-18],
        },
        "q1.xy.y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0028314644490567936, 0.00534088966299196, 0.007230103218225639, 0.008247002275097464, 0.00820454030496545, 0.00699516245334783, 0.0045996612839056174, 0.0010898018367112362, -0.0033755126595763248, -0.00856032340302704, -0.014167308153233714, -0.019858056655828068, -0.025276582004857405, -0.03007448745309005, -0.03393607903218466, -0.03660169844649974, -0.03788764993634531, -0.03770130351071933, -0.036050262258920246, -0.03304486408561808, -0.028893723698945026, -0.023892480900343373, -0.018406376223575778, -0.012847694883601735, -0.007649476983125875, -0.0032371619840475207, -2.667440632800439e-18],
        },
        "q1.xy.y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0015692636512354573, 0.00618650913273165, 0.013585392396929824, 0.023339333630038258, 0.03488642651618458, 0.04756221586312049, 0.06063840025719136, 0.07336516793800475, 0.08501466316917314, 0.09492301948554487, 0.1025284886816222, 0.10740343434982058, 0.10927833135444977, 0.10805639502544553, 0.10381802668228486, 0.09681487118453298, 0.08745390069813067, 0.07627252947867633, 0.06390629175345737, 0.05105104726879789, 0.038421991181715416, 0.026711918559169004, 0.0165512191434916, 0.008471954632942124, 0.0028781069344716976, 2.369857377083627e-05, -1.4529349935543235e-18],
        },
        "q1.xy.-y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -0.0028314644490567936, -0.00534088966299196, -0.007230103218225637, -0.00824700227509746, -0.008204540304965447, -0.006995162453347825, -0.0045996612839056105, -0.001089801836711227, 0.003375512659576335, 0.00856032340302705, 0.014167308153233728, 0.019858056655828082, 0.02527658200485742, 0.030074487453090062, 0.03393607903218467, 0.036601698446499756, 0.03788764993634532, 0.03770130351071935, 0.03605026225892026, 0.03304486408561808, 0.028893723698945033, 0.023892480900343373, 0.018406376223575778, 0.012847694883601735, 0.007649476983125875, 0.0032371619840475207, 2.667440632800439e-18],
        },
        "q1.xy.-y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.0015692636512354577, -0.00618650913273165, -0.013585392396929824, -0.023339333630038258, -0.03488642651618458, -0.04756221586312049, -0.06063840025719136, -0.07336516793800475, -0.08501466316917314, -0.09492301948554487, -0.1025284886816222, -0.10740343434982058, -0.10927833135444977, -0.10805639502544553, -0.10381802668228486, -0.09681487118453298, -0.08745390069813067, -0.07627252947867633, -0.06390629175345737, -0.05105104726879789, -0.038421991181715416, -0.026711918559169004, -0.0165512191434916, -0.008471954632942124, -0.0028781069344716967, -2.369857377083587e-05, 1.4529349935543239e-18],
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
            "sample": 0.1133636504292105,
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
            "samples": [0.0, 0.0022178495452366597, 0.008704695351839492, 0.018973731613405254, 0.03225684454928212, 0.04756565546205715, 0.06376971277292262, 0.07968531343000894, 0.0941675684586457, 0.10619808974796346, 0.11496108467816765, 0.11990166568420395, 0.12076172482903294, 0.11759065577080342, 0.11073036081236472, 0.10077617380627042, 0.08851737239987781, 0.07486267052296171, 0.06075732748495396, 0.04709917774951648, 0.0346609194938273, 0.024025399220614644, 0.015539447488184513, 0.009290160848663447, 0.0051055320356405715, 0.0025791776187684074, 0.0011167866800144079, 1.2625662247269476e-18],
        },
        "q2.xy.x180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.0013334758574539845, -0.003421453651042604, -0.006939106422337691, -0.01241015440079845, -0.02014852014342328, -0.030219129626052423, -0.04242154721347455, -0.05629812708197781, -0.07116620567310163, -0.08617173622972105, -0.10035986173525957, -0.11275640228646477, -0.12245322973039365, -0.12869010447728946, -0.13092579284937908, -0.12889214896489387, -0.12262626014600597, -0.11247759889377427, -0.09908924017102819, -0.0833544090271549, -0.06635173136239397, -0.04926438891600118, -0.03328977116073602, -0.019547051744728938, -0.008990323079034097, -0.0023344810941751913, -1.2046827555042265e-19],
        },
        "q2.xy.x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0011089247726183298, 0.004352347675919746, 0.009486865806702627, 0.01612842227464106, 0.023782827731028574, 0.03188485638646131, 0.03984265671500447, 0.04708378422932285, 0.05309904487398173, 0.057480542339083826, 0.059950832842101974, 0.06038086241451647, 0.05879532788540171, 0.05536518040618236, 0.05038808690313521, 0.044258686199938904, 0.037431335261480854, 0.03037866374247698, 0.02354958887475824, 0.01733045974691365, 0.012012699610307322, 0.007769723744092257, 0.004645080424331724, 0.0025527660178202858, 0.0012895888093842037, 0.0005583933400072039, 6.312831123634738e-19],
        },
        "q2.xy.x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.0006667379287269923, -0.001710726825521302, -0.0034695532111688457, -0.006205077200399225, -0.01007426007171164, -0.015109564813026211, -0.021210773606737274, -0.028149063540988905, -0.03558310283655081, -0.04308586811486052, -0.050179930867629785, -0.05637820114323239, -0.06122661486519682, -0.06434505223864473, -0.06546289642468954, -0.06444607448244694, -0.061313130073002986, -0.05623879944688714, -0.04954462008551409, -0.04167720451357745, -0.03317586568119699, -0.02463219445800059, -0.01664488558036801, -0.009773525872364469, -0.004495161539517048, -0.0011672405470875957, -6.023413777521132e-20],
        },
        "q2.xy.-x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -0.0011089247726183298, -0.004352347675919746, -0.009486865806702627, -0.01612842227464106, -0.023782827731028574, -0.03188485638646131, -0.03984265671500447, -0.04708378422932285, -0.053099044873981725, -0.05748054233908382, -0.05995083284210197, -0.06038086241451646, -0.058795327885401705, -0.05536518040618235, -0.050388086903135204, -0.0442586861999389, -0.03743133526148085, -0.030378663742476972, -0.023549588874758234, -0.017330459746913645, -0.012012699610307319, -0.007769723744092254, -0.004645080424331722, -0.0025527660178202845, -0.001289588809384203, -0.0005583933400072038, -6.312831123634738e-19],
        },
        "q2.xy.-x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0006667379287269924, 0.0017107268255213024, 0.003469553211168847, 0.0062050772003992265, 0.010074260071711643, 0.015109564813026215, 0.021210773606737277, 0.028149063540988912, 0.03558310283655082, 0.04308586811486053, 0.05017993086762979, 0.056378201143232394, 0.06122661486519683, 0.06434505223864473, 0.06546289642468954, 0.06444607448244694, 0.06131313007300299, 0.056238799446887144, 0.04954462008551409, 0.04167720451357745, 0.03317586568119699, 0.02463219445800059, 0.01664488558036801, 0.009773525872364469, 0.004495161539517048, 0.0011672405470875957, 6.02341377752114e-20],
        },
        "q2.xy.y180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0013334758574539847, 0.0034214536510426045, 0.006939106422337692, 0.012410154400798451, 0.020148520143423283, 0.030219129626052426, 0.042421547213474554, 0.05629812708197782, 0.07116620567310163, 0.08617173622972106, 0.10035986173525958, 0.11275640228646479, 0.12245322973039366, 0.12869010447728946, 0.13092579284937908, 0.12889214896489387, 0.12262626014600597, 0.11247759889377427, 0.09908924017102819, 0.0833544090271549, 0.06635173136239397, 0.04926438891600118, 0.03328977116073602, 0.019547051744728938, 0.008990323079034097, 0.0023344810941751913, 1.2046827555042272e-19],
        },
        "q2.xy.y180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0022178495452366597, 0.008704695351839492, 0.018973731613405254, 0.03225684454928212, 0.04756565546205715, 0.06376971277292262, 0.07968531343000894, 0.0941675684586457, 0.10619808974796346, 0.11496108467816765, 0.11990166568420395, 0.12076172482903294, 0.11759065577080341, 0.1107303608123647, 0.10077617380627041, 0.0885173723998778, 0.0748626705229617, 0.06075732748495395, 0.047099177749516476, 0.03466091949382729, 0.02402539922061464, 0.01553944748818451, 0.009290160848663446, 0.005105532035640571, 0.002579177618768407, 0.0011167866800144077, 1.2625662247269476e-18],
        },
        "q2.xy.y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0006667379287269924, 0.0017107268255213022, 0.003469553211168846, 0.006205077200399226, 0.010074260071711642, 0.015109564813026213, 0.021210773606737277, 0.02814906354098891, 0.03558310283655081, 0.04308586811486053, 0.05017993086762979, 0.056378201143232394, 0.06122661486519683, 0.06434505223864473, 0.06546289642468954, 0.06444607448244694, 0.061313130073002986, 0.05623879944688714, 0.04954462008551409, 0.04167720451357745, 0.03317586568119699, 0.02463219445800059, 0.01664488558036801, 0.009773525872364469, 0.004495161539517048, 0.0011672405470875957, 6.023413777521136e-20],
        },
        "q2.xy.y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0011089247726183298, 0.004352347675919746, 0.009486865806702627, 0.01612842227464106, 0.023782827731028574, 0.03188485638646131, 0.03984265671500447, 0.04708378422932285, 0.05309904487398173, 0.057480542339083826, 0.059950832842101974, 0.06038086241451647, 0.058795327885401705, 0.05536518040618235, 0.050388086903135204, 0.0442586861999389, 0.03743133526148085, 0.030378663742476976, 0.023549588874758238, 0.017330459746913645, 0.01201269961030732, 0.007769723744092255, 0.004645080424331723, 0.0025527660178202853, 0.0012895888093842035, 0.0005583933400072038, 6.312831123634738e-19],
        },
        "q2.xy.-y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -0.0006667379287269922, -0.0017107268255213018, -0.0034695532111688452, -0.006205077200399224, -0.010074260071711638, -0.01510956481302621, -0.02121077360673727, -0.0281490635409889, -0.03558310283655081, -0.043085868114860516, -0.05017993086762978, -0.05637820114323238, -0.061226614865196816, -0.06434505223864473, -0.06546289642468954, -0.06444607448244694, -0.061313130073002986, -0.05623879944688714, -0.04954462008551409, -0.04167720451357745, -0.03317586568119699, -0.02463219445800059, -0.01664488558036801, -0.009773525872364469, -0.004495161539517048, -0.0011672405470875957, -6.023413777521129e-20],
        },
        "q2.xy.-y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.0011089247726183298, -0.004352347675919746, -0.009486865806702627, -0.01612842227464106, -0.023782827731028574, -0.03188485638646131, -0.03984265671500447, -0.04708378422932285, -0.05309904487398173, -0.057480542339083826, -0.059950832842101974, -0.06038086241451647, -0.05879532788540172, -0.055365180406182365, -0.05038808690313522, -0.04425868619993891, -0.03743133526148086, -0.030378663742476983, -0.023549588874758245, -0.017330459746913652, -0.012012699610307324, -0.007769723744092258, -0.0046450804243317245, -0.002552766017820286, -0.001289588809384204, -0.000558393340007204, -6.312831123634738e-19],
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
            "sample": 0.09345462248456422,
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
            "samples": [0.0, 0.003427538996024826, 0.013519611757053481, 0.029715229616201985, 0.051114293164133295, 0.07652785442388323, 0.10454448300561378, 0.13360900809989126, 0.16210921518023078, 0.1884656329957647, 0.21121937770688004, 0.22911313613344225, 0.24116076223425212, 0.24670160761244658, 0.24543657114292666, 0.23744388556103913, 0.22317380138291734, 0.20342251607027592, 0.17928686169696081, 0.1521023417031031, 0.12336803594552827, 0.09466262104664397, 0.06755623939422957, 0.04352316822751625, 0.023860178517195827, 0.009615136161162783, 0.001529805331169329, -1.882573198122245e-18],
        },
        "q3.xy.x180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.00634288334266427, -0.012133358106591843, -0.016856584190987407, -0.020070399253618823, -0.02143566652365199, -0.020739862895168333, -0.017912341099550703, -0.013030232726801596, -0.006314559281958048, 0.0018832514502115153, 0.011103626426996919, 0.020808497684380957, 0.030416468670258486, 0.039341254562322646, 0.04703092628220836, 0.05300541524249874, 0.05688982431458829, 0.0584413355620361, 0.05756789261122428, 0.054337341819841734, 0.04897631076756308, 0.04185874843979246, 0.0334847087385862, 0.024450586554498093, 0.015412574009767387, 0.007045558055728747, 6.507320532481616e-18],
        },
        "q3.xy.x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.001713769498012413, 0.006759805878526741, 0.014857614808100992, 0.025557146582066648, 0.03826392721194161, 0.05227224150280689, 0.06680450404994563, 0.08105460759011539, 0.09423281649788234, 0.10560968885344002, 0.11455656806672113, 0.12058038111712606, 0.12335080380622329, 0.12271828557146333, 0.11872194278051956, 0.11158690069145867, 0.10171125803513796, 0.08964343084848041, 0.07605117085155155, 0.061684017972764134, 0.047331310523321984, 0.033778119697114785, 0.021761584113758125, 0.011930089258597914, 0.004807568080581391, 0.0007649026655846645, -9.412865990611225e-19],
        },
        "q3.xy.x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.003171441671332135, -0.006066679053295922, -0.008428292095493704, -0.010035199626809412, -0.010717833261825994, -0.010369931447584167, -0.008956170549775351, -0.006515116363400798, -0.003157279640979024, 0.0009416257251057576, 0.005551813213498459, 0.010404248842190478, 0.015208234335129243, 0.019670627281161323, 0.02351546314110418, 0.02650270762124937, 0.028444912157294146, 0.02922066778101805, 0.02878394630561214, 0.027168670909920867, 0.02448815538378154, 0.02092937421989623, 0.0167423543692931, 0.012225293277249047, 0.007706287004883693, 0.0035227790278643733, 3.253660266240808e-18],
        },
        "q3.xy.-x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -0.0017137694980124125, -0.00675980587852674, -0.01485761480810099, -0.025557146582066648, -0.03826392721194161, -0.05227224150280689, -0.06680450404994563, -0.08105460759011539, -0.09423281649788234, -0.10560968885344002, -0.11455656806672113, -0.12058038111712606, -0.12335080380622329, -0.12271828557146333, -0.11872194278051956, -0.11158690069145867, -0.10171125803513796, -0.08964343084848041, -0.07605117085155155, -0.061684017972764134, -0.047331310523321984, -0.033778119697114785, -0.02176158411375813, -0.011930089258597915, -0.004807568080581392, -0.0007649026655846649, 9.41286599061122e-19],
        },
        "q3.xy.-x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.003171441671332135, 0.0060666790532959225, 0.008428292095493705, 0.010035199626809415, 0.010717833261826, 0.010369931447584173, 0.00895617054977536, 0.006515116363400807, 0.0031572796409790357, -0.0009416257251057447, -0.0055518132134984455, -0.010404248842190463, -0.015208234335129227, -0.01967062728116131, -0.023515463141104167, -0.026502707621249354, -0.028444912157294132, -0.02922066778101804, -0.02878394630561213, -0.02716867090992086, -0.024488155383781532, -0.020929374219896227, -0.016742354369293097, -0.012225293277249045, -0.0077062870048836924, -0.0035227790278643733, -3.253660266240808e-18],
        },
        "q3.xy.y180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.00634288334266427, 0.012133358106591843, 0.01685658419098741, 0.020070399253618827, 0.021435666523651992, 0.02073986289516834, 0.01791234109955071, 0.013030232726801606, 0.006314559281958059, -0.0018832514502115023, -0.011103626426996905, -0.020808497684380943, -0.030416468670258472, -0.03934125456232263, -0.04703092628220835, -0.05300541524249872, -0.05688982431458828, -0.05844133556203609, -0.057567892611224275, -0.05433734181984173, -0.04897631076756307, -0.041858748439792454, -0.0334847087385862, -0.024450586554498093, -0.015412574009767387, -0.007045558055728747, -6.507320532481616e-18],
        },
        "q3.xy.y180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0034275389960248255, 0.013519611757053481, 0.029715229616201985, 0.051114293164133295, 0.07652785442388323, 0.10454448300561378, 0.13360900809989126, 0.16210921518023078, 0.1884656329957647, 0.21121937770688004, 0.22911313613344225, 0.24116076223425212, 0.24670160761244658, 0.24543657114292666, 0.23744388556103913, 0.22317380138291734, 0.20342251607027592, 0.17928686169696081, 0.1521023417031031, 0.12336803594552827, 0.09466262104664397, 0.06755623939422957, 0.04352316822751625, 0.023860178517195827, 0.009615136161162784, 0.0015298053311693293, -1.8825731981222445e-18],
        },
        "q3.xy.y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.003171441671332135, 0.006066679053295922, 0.008428292095493705, 0.010035199626809413, 0.010717833261825996, 0.01036993144758417, 0.008956170549775355, 0.006515116363400803, 0.0031572796409790297, -0.0009416257251057511, -0.0055518132134984525, -0.010404248842190471, -0.015208234335129236, -0.019670627281161316, -0.023515463141104174, -0.02650270762124936, -0.02844491215729414, -0.029220667781018044, -0.028783946305612138, -0.027168670909920863, -0.024488155383781535, -0.020929374219896227, -0.0167423543692931, -0.012225293277249047, -0.007706287004883693, -0.0035227790278643733, -3.253660266240808e-18],
        },
        "q3.xy.y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0017137694980124127, 0.006759805878526741, 0.014857614808100992, 0.025557146582066648, 0.03826392721194161, 0.05227224150280689, 0.06680450404994563, 0.08105460759011539, 0.09423281649788234, 0.10560968885344002, 0.11455656806672113, 0.12058038111712606, 0.12335080380622329, 0.12271828557146333, 0.11872194278051956, 0.11158690069145867, 0.10171125803513796, 0.08964343084848041, 0.07605117085155155, 0.061684017972764134, 0.047331310523321984, 0.033778119697114785, 0.021761584113758125, 0.011930089258597914, 0.004807568080581392, 0.0007649026655846647, -9.412865990611223e-19],
        },
        "q3.xy.-y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -0.003171441671332135, -0.006066679053295922, -0.008428292095493702, -0.01003519962680941, -0.010717833261825993, -0.010369931447584163, -0.008956170549775348, -0.006515116363400793, -0.0031572796409790184, 0.0009416257251057641, 0.005551813213498466, 0.010404248842190485, 0.01520823433512925, 0.01967062728116133, 0.023515463141104188, 0.026502707621249375, 0.028444912157294153, 0.029220667781018058, 0.028783946305612144, 0.02716867090992087, 0.024488155383781542, 0.020929374219896234, 0.0167423543692931, 0.012225293277249047, 0.007706287004883693, 0.0035227790278643733, 3.253660266240808e-18],
        },
        "q3.xy.-y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.0017137694980124132, -0.006759805878526741, -0.014857614808100992, -0.025557146582066648, -0.03826392721194161, -0.05227224150280689, -0.06680450404994563, -0.08105460759011539, -0.09423281649788234, -0.10560968885344002, -0.11455656806672113, -0.12058038111712606, -0.12335080380622329, -0.12271828557146333, -0.11872194278051956, -0.11158690069145867, -0.10171125803513796, -0.08964343084848041, -0.07605117085155155, -0.061684017972764134, -0.047331310523321984, -0.033778119697114785, -0.021761584113758125, -0.011930089258597914, -0.00480756808058139, -0.0007649026655846642, 9.412865990611227e-19],
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
            "sample": 0.09301178911991174,
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
            "samples": [0.0, 0.0031418179039661917, 0.012398841698068305, 0.027274818735635063, 0.04697229950836004, 0.07043542202344713, 0.09640655656094506, 0.12349376838997234, 0.15024547533331314, 0.1752282911899412, 0.1971038756743615, 0.21470066582934424, 0.22707663984420196, 0.2335697469668364, 0.23383330071519923, 0.22785444113561082, 0.21595468189393305, 0.19877252054859923, 0.17722905366355216, 0.1524784506782249, 0.12584595263554185, 0.09875673036072367, 0.07265942562023679, 0.048948481988143416, 0.028889434506606495, 0.013551165538152526, 0.003748757313981707, 6.627987933035159e-19],
        },
        "q4.xy.x180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.005771852513742905, -0.011307947348866308, -0.016382559601478646, -0.020789632615630372, -0.024351632562333917, -0.026927265624842597, -0.028417741114190504, -0.028771315401553907, -0.027985913517889836, -0.026109695947102673, -0.023239515487715176, -0.019517290705797642, -0.015124405771312535, -0.01027432843170332, -0.005203715423279538, -0.00016234456470761506, 0.004597728032518575, 0.008833341740214096, 0.012321263199731243, 0.014868592618074349, 0.016322070653836635, 0.01657584244041028, 0.01557728655614855, 0.01333058776071953, 0.009897821035767302, 0.005397417881075277, 6.080606192049252e-18],
        },
        "q4.xy.x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0015709089519830959, 0.006199420849034153, 0.013637409367817531, 0.02348614975418002, 0.035217711011723565, 0.04820327828047253, 0.06174688419498617, 0.07512273766665657, 0.0876141455949706, 0.09855193783718075, 0.10735033291467212, 0.11353831992210098, 0.1167848734834182, 0.11691665035759961, 0.11392722056780541, 0.10797734094696652, 0.09938626027429961, 0.08861452683177608, 0.07623922533911245, 0.06292297631777093, 0.04937836518036184, 0.036329712810118396, 0.024474240994071708, 0.014444717253303247, 0.006775582769076263, 0.0018743786569908535, 3.3139939665175794e-19],
        },
        "q4.xy.x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.0028859262568714525, -0.005653973674433154, -0.008191279800739323, -0.010394816307815186, -0.012175816281166959, -0.013463632812421298, -0.014208870557095252, -0.014385657700776953, -0.013992956758944918, -0.013054847973551336, -0.011619757743857588, -0.009758645352898821, -0.007562202885656268, -0.00513716421585166, -0.002601857711639769, -8.117228235380753e-05, 0.0022988640162592876, 0.004416670870107048, 0.006160631599865621, 0.007434296309037174, 0.008161035326918318, 0.00828792122020514, 0.007788643278074275, 0.006665293880359765, 0.004948910517883651, 0.0026987089405376384, 3.040303096024626e-18],
        },
        "q4.xy.-x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -0.0015709089519830954, -0.006199420849034152, -0.01363740936781753, -0.02348614975418002, -0.035217711011723565, -0.04820327828047253, -0.06174688419498617, -0.07512273766665657, -0.0876141455949706, -0.09855193783718075, -0.10735033291467212, -0.11353831992210098, -0.1167848734834182, -0.11691665035759961, -0.11392722056780541, -0.10797734094696652, -0.09938626027429961, -0.08861452683177608, -0.07623922533911245, -0.06292297631777093, -0.04937836518036184, -0.036329712810118396, -0.024474240994071708, -0.014444717253303247, -0.006775582769076264, -0.001874378656990854, -3.313993966517583e-19],
        },
        "q4.xy.-x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0028859262568714525, 0.005653973674433155, 0.008191279800739325, 0.01039481630781519, 0.012175816281166962, 0.013463632812421304, 0.014208870557095259, 0.014385657700776962, 0.013992956758944929, 0.013054847973551349, 0.011619757743857602, 0.009758645352898835, 0.0075622028856562815, 0.005137164215851675, 0.002601857711639783, 8.117228235382076e-05, -0.0022988640162592755, -0.004416670870107037, -0.006160631599865612, -0.0074342963090371665, -0.008161035326918312, -0.008287921220205136, -0.007788643278074272, -0.0066652938803597635, -0.00494891051788365, -0.002698708940537638, -3.040303096024626e-18],
        },
        "q4.xy.y180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.005771852513742905, 0.011307947348866308, 0.016382559601478646, 0.020789632615630375, 0.02435163256233392, 0.026927265624842604, 0.02841774111419051, 0.028771315401553917, 0.027985913517889847, 0.026109695947102683, 0.02323951548771519, 0.019517290705797656, 0.015124405771312549, 0.010274328431703334, 0.005203715423279552, 0.0001623445647076283, -0.004597728032518563, -0.008833341740214086, -0.012321263199731234, -0.014868592618074342, -0.016322070653836628, -0.016575842440410278, -0.015577286556148547, -0.013330587760719529, -0.009897821035767302, -0.005397417881075277, -6.080606192049252e-18],
        },
        "q4.xy.y180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0031418179039661913, 0.012398841698068305, 0.027274818735635063, 0.04697229950836004, 0.07043542202344713, 0.09640655656094506, 0.12349376838997234, 0.15024547533331314, 0.1752282911899412, 0.1971038756743615, 0.21470066582934424, 0.22707663984420196, 0.2335697469668364, 0.23383330071519923, 0.22785444113561082, 0.21595468189393305, 0.19877252054859923, 0.17722905366355216, 0.1524784506782249, 0.12584595263554185, 0.09875673036072367, 0.07265942562023679, 0.048948481988143416, 0.028889434506606495, 0.013551165538152526, 0.0037487573139817075, 6.627987933035163e-19],
        },
        "q4.xy.y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0028859262568714525, 0.005653973674433154, 0.008191279800739323, 0.010394816307815188, 0.01217581628116696, 0.013463632812421302, 0.014208870557095256, 0.014385657700776959, 0.013992956758944923, 0.013054847973551342, 0.011619757743857595, 0.009758645352898828, 0.0075622028856562745, 0.005137164215851667, 0.002601857711639776, 8.117228235381415e-05, -0.0022988640162592815, -0.004416670870107043, -0.006160631599865617, -0.007434296309037171, -0.008161035326918314, -0.008287921220205139, -0.007788643278074273, -0.006665293880359764, -0.004948910517883651, -0.0026987089405376384, -3.040303096024626e-18],
        },
        "q4.xy.y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0015709089519830956, 0.006199420849034153, 0.013637409367817531, 0.02348614975418002, 0.035217711011723565, 0.04820327828047253, 0.06174688419498617, 0.07512273766665657, 0.0876141455949706, 0.09855193783718075, 0.10735033291467212, 0.11353831992210098, 0.1167848734834182, 0.11691665035759961, 0.11392722056780541, 0.10797734094696652, 0.09938626027429961, 0.08861452683177608, 0.07623922533911245, 0.06292297631777093, 0.04937836518036184, 0.036329712810118396, 0.024474240994071708, 0.014444717253303247, 0.006775582769076263, 0.0018743786569908538, 3.3139939665175813e-19],
        },
        "q4.xy.-y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -0.0028859262568714525, -0.005653973674433154, -0.008191279800739323, -0.010394816307815184, -0.012175816281166957, -0.013463632812421295, -0.014208870557095249, -0.014385657700776948, -0.013992956758944913, -0.013054847973551331, -0.011619757743857581, -0.009758645352898814, -0.007562202885656261, -0.005137164215851653, -0.0026018577116397623, -8.117228235380092e-05, 0.0022988640162592937, 0.004416670870107053, 0.006160631599865626, 0.007434296309037178, 0.008161035326918321, 0.008287921220205142, 0.007788643278074277, 0.006665293880359766, 0.004948910517883651, 0.0026987089405376384, 3.040303096024626e-18],
        },
        "q4.xy.-y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.001570908951983096, -0.006199420849034153, -0.013637409367817531, -0.02348614975418002, -0.035217711011723565, -0.04820327828047253, -0.06174688419498617, -0.07512273766665657, -0.0876141455949706, -0.09855193783718075, -0.10735033291467212, -0.11353831992210098, -0.1167848734834182, -0.11691665035759961, -0.11392722056780541, -0.10797734094696652, -0.09938626027429961, -0.08861452683177608, -0.07623922533911245, -0.06292297631777093, -0.04937836518036184, -0.036329712810118396, -0.024474240994071708, -0.014444717253303247, -0.006775582769076263, -0.0018743786569908533, -3.3139939665175774e-19],
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
            "sample": 0.0779312997256516,
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
            "samples": [0.0, 0.0022145819444009305, 0.00871154599615161, 0.019060869351641297, 0.03257949049214639, 0.048379153583885615, 0.06542835526433981, 0.0826238213232975, 0.09886625542811753, 0.1131348155293711, 0.12455490664067752, 0.13245441978657654, 0.13640445320989494, 0.1362417526248674, 0.13207150915916932, 0.12425064822826161, 0.1133532147435172, 0.10012079674740719, 0.08540202867759122, 0.07008599366129967, 0.055034743408211184, 0.04102014592360599, 0.028669858695089073, 0.01842644293161499, 0.010522546201643772, 0.004973773392648244, 0.0015894430293642884, 8.967218359287526e-19],
        },
        "q5.xy.x180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.0009881550572747077, -0.002550722228194775, -0.005204645039221282, -0.009356820302615613, -0.01526090589950815, -0.022987251147820784, -0.03240862393080892, -0.04320312666777444, -0.05487429313664531, -0.06678695124123799, -0.07821613497573703, -0.08840523598960594, -0.09662878902613306, -0.10225485071805616, -0.10480189416573123, -0.10398550763857162, -0.0997509282314294, -0.09228850432130324, -0.0820304828021743, -0.06962895786341451, -0.05591628578809323, -0.041850650565677744, -0.02845065004162883, -0.01672366861244572, -0.0075933389076911755, -0.0018315279037157404, 2.7254066193013106e-19],
        },
        "q5.xy.x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0011072909722004652, 0.004355772998075805, 0.009530434675820649, 0.016289745246073194, 0.024189576791942807, 0.032714177632169904, 0.04131191066164875, 0.049433127714058764, 0.05656740776468555, 0.06227745332033876, 0.06622720989328827, 0.06820222660494747, 0.0681208763124337, 0.06603575457958466, 0.062125324114130805, 0.0566766073717586, 0.050060398373703595, 0.04270101433879561, 0.035042996830649834, 0.027517371704105592, 0.020510072961802996, 0.014334929347544536, 0.009213221465807496, 0.005261273100821886, 0.002486886696324122, 0.0007947215146821442, 4.483609179643763e-19],
        },
        "q5.xy.x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.0004940775286373538, -0.0012753611140973876, -0.002602322519610641, -0.004678410151307807, -0.007630452949754075, -0.011493625573910392, -0.01620431196540446, -0.02160156333388722, -0.027437146568322655, -0.03339347562061899, -0.03910806748786851, -0.04420261799480297, -0.04831439451306653, -0.05112742535902808, -0.052400947082865613, -0.05199275381928581, -0.0498754641157147, -0.04614425216065162, -0.04101524140108715, -0.034814478931707256, -0.027958142894046616, -0.020925325282838872, -0.014225325020814415, -0.00836183430622286, -0.0037966694538455878, -0.0009157639518578702, 1.3627033096506553e-19],
        },
        "q5.xy.-x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -0.0011072909722004652, -0.004355772998075805, -0.009530434675820649, -0.016289745246073194, -0.024189576791942807, -0.032714177632169904, -0.04131191066164875, -0.049433127714058764, -0.05656740776468555, -0.06227745332033875, -0.06622720989328827, -0.06820222660494747, -0.0681208763124337, -0.06603575457958466, -0.0621253241141308, -0.05667660737175859, -0.05006039837370359, -0.042701014338795605, -0.03504299683064983, -0.02751737170410559, -0.020510072961802992, -0.014334929347544535, -0.009213221465807494, -0.005261273100821885, -0.0024868866963241214, -0.0007947215146821441, -4.483609179643763e-19],
        },
        "q5.xy.-x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0004940775286373539, 0.001275361114097388, 0.0026023225196106425, 0.004678410151307808, 0.007630452949754078, 0.011493625573910395, 0.016204311965404464, 0.021601563333887228, 0.027437146568322662, 0.033393475620619, 0.03910806748786852, 0.044202617994802976, 0.04831439451306654, 0.05112742535902809, 0.05240094708286562, 0.051992753819285815, 0.04987546411571471, 0.04614425216065163, 0.04101524140108716, 0.034814478931707256, 0.02795814289404662, 0.020925325282838875, 0.014225325020814417, 0.00836183430622286, 0.003796669453845588, 0.0009157639518578703, -1.3627033096506548e-19],
        },
        "q5.xy.y180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0009881550572747079, 0.0025507222281947756, 0.005204645039221283, 0.009356820302615615, 0.015260905899508154, 0.022987251147820787, 0.03240862393080893, 0.04320312666777445, 0.05487429313664532, 0.066786951241238, 0.07821613497573704, 0.08840523598960595, 0.09662878902613307, 0.10225485071805618, 0.10480189416573124, 0.10398550763857163, 0.0997509282314294, 0.09228850432130324, 0.0820304828021743, 0.06962895786341451, 0.05591628578809323, 0.041850650565677744, 0.02845065004162883, 0.01672366861244572, 0.0075933389076911755, 0.0018315279037157404, -2.72540661930131e-19],
        },
        "q5.xy.y180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0022145819444009305, 0.00871154599615161, 0.019060869351641297, 0.03257949049214639, 0.048379153583885615, 0.06542835526433981, 0.0826238213232975, 0.09886625542811753, 0.1131348155293711, 0.12455490664067752, 0.13245441978657654, 0.13640445320989494, 0.1362417526248674, 0.13207150915916932, 0.12425064822826161, 0.1133532147435172, 0.10012079674740719, 0.08540202867759122, 0.07008599366129967, 0.05503474340821118, 0.04102014592360599, 0.02866985869508907, 0.018426442931614988, 0.01052254620164377, 0.004973773392648243, 0.0015894430293642882, 8.967218359287526e-19],
        },
        "q5.xy.y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0004940775286373539, 0.0012753611140973878, 0.0026023225196106416, 0.0046784101513078075, 0.007630452949754077, 0.011493625573910394, 0.016204311965404464, 0.021601563333887224, 0.02743714656832266, 0.033393475620619, 0.03910806748786852, 0.044202617994802976, 0.04831439451306654, 0.05112742535902809, 0.05240094708286562, 0.051992753819285815, 0.0498754641157147, 0.04614425216065162, 0.04101524140108715, 0.034814478931707256, 0.027958142894046616, 0.020925325282838872, 0.014225325020814415, 0.00836183430622286, 0.0037966694538455878, 0.0009157639518578702, -1.362703309650655e-19],
        },
        "q5.xy.y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0011072909722004652, 0.004355772998075805, 0.009530434675820649, 0.016289745246073194, 0.024189576791942807, 0.032714177632169904, 0.04131191066164875, 0.049433127714058764, 0.05656740776468555, 0.06227745332033876, 0.06622720989328827, 0.06820222660494747, 0.0681208763124337, 0.06603575457958466, 0.062125324114130805, 0.0566766073717586, 0.050060398373703595, 0.04270101433879561, 0.035042996830649834, 0.02751737170410559, 0.020510072961802996, 0.014334929347544535, 0.009213221465807494, 0.005261273100821885, 0.0024868866963241214, 0.0007947215146821441, 4.483609179643763e-19],
        },
        "q5.xy.-y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -0.0004940775286373537, -0.0012753611140973874, -0.0026023225196106408, -0.004678410151307806, -0.007630452949754073, -0.01149362557391039, -0.016204311965404457, -0.021601563333887217, -0.027437146568322652, -0.033393475620618986, -0.039108067487868506, -0.04420261799480296, -0.04831439451306652, -0.051127425359028075, -0.05240094708286561, -0.0519927538192858, -0.0498754641157147, -0.04614425216065162, -0.04101524140108715, -0.034814478931707256, -0.027958142894046616, -0.020925325282838872, -0.014225325020814415, -0.00836183430622286, -0.0037966694538455878, -0.0009157639518578702, 1.3627033096506555e-19],
        },
        "q5.xy.-y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.0011072909722004652, -0.004355772998075805, -0.009530434675820649, -0.016289745246073194, -0.024189576791942807, -0.032714177632169904, -0.04131191066164875, -0.049433127714058764, -0.05656740776468555, -0.06227745332033876, -0.06622720989328827, -0.06820222660494747, -0.0681208763124337, -0.06603575457958466, -0.062125324114130805, -0.0566766073717586, -0.050060398373703595, -0.04270101433879561, -0.035042996830649834, -0.027517371704105596, -0.020510072961802996, -0.014334929347544538, -0.009213221465807497, -0.005261273100821887, -0.0024868866963241223, -0.0007947215146821443, -4.483609179643763e-19],
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
            "sample": 0.09322400929954788,
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
            "samples": [0.0, 0.0030965862409632902, 0.012202535134434653, 0.026777532241581314, 0.0459574166566813, 0.06860636439158399, 0.09338537505908844, 0.1188328381036055, 0.14345221797723479, 0.165801471615384, 0.18457872245410953, 0.19869896782326263, 0.2073571739971564, 0.21007397813527362, 0.20672131336604288, 0.1975265324163361, 0.183054946513302, 0.1641720349362164, 0.1419878322551346, 0.11778708654002776, 0.09294963511338278, 0.06886601234309053, 0.046853552538155784, 0.028078166724460594, 0.013486562710131763, 0.003752971824060207, -0.000756509823369142, -3.497042023007585e-18],
        },
        "q6.xy.x180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.0054836187524804755, -0.010248295898628797, -0.013630558187597046, -0.015073879714321583, -0.014172458676555621, -0.010704113273629533, -0.004649873863437861, 0.0038012255837528877, 0.014262620544909104, 0.02617534731349305, 0.038846192657757406, 0.0514962949718466, 0.0633168742463143, 0.07352823576097345, 0.08143792111475179, 0.08649389027582073, 0.08832891109186691, 0.08679289041230766, 0.08197066794249444, 0.07418375880873526, 0.06397560988269357, 0.05208105638832378, 0.03938175400856392, 0.026850344052173344, 0.015486918189903847, 0.006251928810969009, 4.751462397063911e-18],
        },
        "q6.xy.x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0015482931204816451, 0.0061012675672173266, 0.013388766120790657, 0.02297870832834065, 0.034303182195791995, 0.04669268752954422, 0.05941641905180275, 0.07172610898861739, 0.082900735807692, 0.09228936122705476, 0.09934948391163131, 0.1036785869985782, 0.10503698906763681, 0.10336065668302144, 0.09876326620816805, 0.091527473256651, 0.0820860174681082, 0.0709939161275673, 0.05889354327001388, 0.04647481755669139, 0.034433006171545266, 0.023426776269077892, 0.014039083362230297, 0.0067432813550658815, 0.0018764859120301036, -0.000378254911684571, -1.7485210115037923e-18],
        },
        "q6.xy.x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.0027418093762402377, -0.005124147949314399, -0.006815279093798523, -0.0075369398571607914, -0.007086229338277811, -0.005352056636814767, -0.0023249369317189304, 0.0019006127918764438, 0.007131310272454552, 0.013087673656746525, 0.019423096328878703, 0.0257481474859233, 0.03165843712315715, 0.036764117880486724, 0.040718960557375894, 0.043246945137910366, 0.044164455545933456, 0.04339644520615383, 0.04098533397124722, 0.03709187940436763, 0.03198780494134679, 0.02604052819416189, 0.01969087700428196, 0.013425172026086672, 0.007743459094951923, 0.0031259644054845047, 2.3757311985319556e-18],
        },
        "q6.xy.-x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -0.0015482931204816447, -0.006101267567217326, -0.013388766120790657, -0.02297870832834065, -0.034303182195791995, -0.04669268752954422, -0.05941641905180275, -0.07172610898861739, -0.082900735807692, -0.09228936122705476, -0.09934948391163131, -0.1036785869985782, -0.10503698906763681, -0.10336065668302144, -0.09876326620816805, -0.091527473256651, -0.0820860174681082, -0.0709939161275673, -0.058893543270013886, -0.046474817556691396, -0.03443300617154527, -0.023426776269077895, -0.014039083362230299, -0.006743281355065883, -0.0018764859120301044, 0.0003782549116845706, 1.748521011503792e-18],
        },
        "q6.xy.-x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0027418093762402377, 0.0051241479493143996, 0.006815279093798525, 0.007536939857160794, 0.007086229338277815, 0.005352056636814773, 0.0023249369317189378, -0.001900612791876435, -0.007131310272454542, -0.013087673656746512, -0.01942309632887869, -0.025748147485923287, -0.031658437123157135, -0.03676411788048671, -0.04071896055737588, -0.04324694513791035, -0.04416445554593345, -0.04339644520615382, -0.04098533397124721, -0.037091879404367624, -0.03198780494134678, -0.026040528194161888, -0.01969087700428196, -0.013425172026086672, -0.007743459094951923, -0.0031259644054845047, -2.375731198531956e-18],
        },
        "q6.xy.y180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0054836187524804755, 0.010248295898628797, 0.013630558187597048, 0.015073879714321586, 0.014172458676555625, 0.010704113273629539, 0.004649873863437868, -0.003801225583752879, -0.014262620544909094, -0.02617534731349304, -0.03884619265775739, -0.05149629497184659, -0.06331687424631428, -0.07352823576097343, -0.08143792111475177, -0.08649389027582072, -0.0883289110918669, -0.08679289041230764, -0.08197066794249443, -0.07418375880873526, -0.06397560988269357, -0.05208105638832378, -0.03938175400856392, -0.026850344052173344, -0.015486918189903847, -0.006251928810969009, -4.751462397063911e-18],
        },
        "q6.xy.y180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.00309658624096329, 0.012202535134434653, 0.026777532241581314, 0.0459574166566813, 0.06860636439158399, 0.09338537505908844, 0.1188328381036055, 0.14345221797723479, 0.165801471615384, 0.18457872245410953, 0.19869896782326263, 0.2073571739971564, 0.21007397813527362, 0.20672131336604288, 0.1975265324163361, 0.183054946513302, 0.1641720349362164, 0.1419878322551346, 0.11778708654002776, 0.09294963511338278, 0.06886601234309053, 0.046853552538155784, 0.028078166724460597, 0.013486562710131765, 0.003752971824060208, -0.0007565098233691416, -3.497042023007585e-18],
        },
        "q6.xy.y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0027418093762402377, 0.005124147949314399, 0.006815279093798524, 0.007536939857160793, 0.007086229338277812, 0.005352056636814769, 0.002324936931718934, -0.0019006127918764395, -0.007131310272454547, -0.01308767365674652, -0.019423096328878696, -0.025748147485923294, -0.03165843712315714, -0.03676411788048672, -0.04071896055737589, -0.04324694513791036, -0.04416445554593345, -0.04339644520615382, -0.04098533397124721, -0.03709187940436763, -0.03198780494134679, -0.02604052819416189, -0.01969087700428196, -0.013425172026086672, -0.007743459094951923, -0.0031259644054845047, -2.3757311985319556e-18],
        },
        "q6.xy.y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.001548293120481645, 0.0061012675672173266, 0.013388766120790657, 0.02297870832834065, 0.034303182195791995, 0.04669268752954422, 0.05941641905180275, 0.07172610898861739, 0.082900735807692, 0.09228936122705476, 0.09934948391163131, 0.1036785869985782, 0.10503698906763681, 0.10336065668302144, 0.09876326620816805, 0.091527473256651, 0.0820860174681082, 0.0709939161275673, 0.05889354327001388, 0.04647481755669139, 0.034433006171545266, 0.023426776269077892, 0.014039083362230299, 0.006743281355065882, 0.001876485912030104, -0.0003782549116845708, -1.7485210115037923e-18],
        },
        "q6.xy.-y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -0.0027418093762402377, -0.005124147949314399, -0.006815279093798522, -0.00753693985716079, -0.007086229338277809, -0.005352056636814764, -0.002324936931718927, 0.0019006127918764482, 0.007131310272454557, 0.01308767365674653, 0.01942309632887871, 0.025748147485923308, 0.031658437123157156, 0.03676411788048673, 0.0407189605573759, 0.04324694513791037, 0.04416445554593346, 0.043396445206153836, 0.04098533397124723, 0.03709187940436763, 0.03198780494134679, 0.02604052819416189, 0.01969087700428196, 0.013425172026086672, 0.007743459094951923, 0.0031259644054845047, 2.3757311985319556e-18],
        },
        "q6.xy.-y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.0015482931204816453, -0.0061012675672173266, -0.013388766120790657, -0.02297870832834065, -0.034303182195791995, -0.04669268752954422, -0.05941641905180275, -0.07172610898861739, -0.082900735807692, -0.09228936122705476, -0.09934948391163131, -0.1036785869985782, -0.10503698906763681, -0.10336065668302144, -0.09876326620816805, -0.091527473256651, -0.0820860174681082, -0.0709939161275673, -0.05889354327001388, -0.04647481755669139, -0.034433006171545266, -0.023426776269077892, -0.014039083362230295, -0.006743281355065881, -0.0018764859120301031, 0.0003782549116845712, 1.7485210115037923e-18],
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
            "sample": 0.09586708553446507,
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
            "samples": [0.0, 0.0006111507311347972, 0.0024043824972849346, 0.005261828068419316, 0.008996151598091794, 0.01336351431849177, 0.01808038314363127, 0.022842960300863947, 0.027347826179509697, 0.03131230673148022, 0.03449310675505968, 0.036701888627180844, 0.03781671173591753, 0.037788562877863946, 0.03664257815093054, 0.0344739542133999, 0.031438941065012604, 0.027741669952818546, 0.023617871446307143, 0.019316757675127402, 0.015082463072673417, 0.011136451207145381, 0.007662201116357545, 0.004793292919282823, 0.002605734867066953, 0.0011150343024962388, 0.00027813977658454076, 4.362284073217507e-20],
        },
        "q7.xy.x180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -7.140266213968797e-05, -0.00030305476564477835, -0.0008396348285968095, -0.0017959836520728878, -0.0032453419219738854, -0.005211092845650111, -0.0076627306475489975, -0.010516437590361182, -0.013640282115013775, -0.016863677669417907, -0.019990395083063817, -0.02281412823221524, -0.025135396429880257, -0.0267784447740055, -0.027606785658708086, -0.027536112817346484, -0.02654350742428085, -0.024672129972282023, -0.0220309311935979, -0.01878929439721397, -0.015166911280064943, -0.011419563616160871, -0.007821805663931819, -0.0046477916336201824, -0.002151649573812355, -0.0005488550090950498, 1.6059070921146568e-20],
        },
        "q7.xy.x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0003055753655673986, 0.0012021912486424673, 0.002630914034209658, 0.004498075799045897, 0.006681757159245885, 0.009040191571815634, 0.011421480150431974, 0.013673913089754849, 0.01565615336574011, 0.01724655337752984, 0.018350944313590422, 0.018908355867958766, 0.018894281438931973, 0.01832128907546527, 0.01723697710669995, 0.015719470532506302, 0.013870834976409273, 0.011808935723153571, 0.009658378837563701, 0.007541231536336708, 0.0055682256035726905, 0.0038311005581787723, 0.0023966464596414114, 0.0013028674335334766, 0.0005575171512481194, 0.00013906988829227038, 2.1811420366087536e-20],
        },
        "q7.xy.x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -3.570133106984399e-05, -0.00015152738282238917, -0.00041981741429840473, -0.0008979918260364439, -0.0016226709609869427, -0.0026055464228250556, -0.0038313653237744987, -0.005258218795180591, -0.006820141057506887, -0.008431838834708954, -0.009995197541531909, -0.01140706411610762, -0.012567698214940129, -0.01338922238700275, -0.013803392829354043, -0.013768056408673242, -0.013271753712140425, -0.012336064986141012, -0.01101546559679895, -0.009394647198606986, -0.007583455640032472, -0.005709781808080436, -0.003910902831965909, -0.0023238958168100912, -0.0010758247869061776, -0.0002744275045475249, 8.029535460573284e-21],
        },
        "q7.xy.-x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -0.0003055753655673986, -0.0012021912486424673, -0.002630914034209658, -0.004498075799045897, -0.006681757159245885, -0.009040191571815634, -0.011421480150431974, -0.013673913089754849, -0.01565615336574011, -0.01724655337752984, -0.018350944313590422, -0.018908355867958766, -0.018894281438931973, -0.01832128907546527, -0.01723697710669995, -0.015719470532506302, -0.013870834976409271, -0.01180893572315357, -0.0096583788375637, -0.0075412315363367075, -0.00556822560357269, -0.0038311005581787715, -0.002396646459641411, -0.0013028674335334764, -0.0005575171512481193, -0.00013906988829227035, -2.1811420366087536e-20],
        },
        "q7.xy.-x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 3.570133106984403e-05, 0.0001515273828223893, 0.00041981741429840505, 0.0008979918260364444, 0.0016226709609869436, 0.002605546422825057, 0.0038313653237745, 0.005258218795180593, 0.006820141057506889, 0.008431838834708955, 0.00999519754153191, 0.011407064116107622, 0.01256769821494013, 0.013389222387002752, 0.013803392829354045, 0.013768056408673244, 0.013271753712140427, 0.012336064986141013, 0.011015465596798953, 0.009394647198606988, 0.0075834556400324726, 0.0057097818080804365, 0.003910902831965909, 0.0023238958168100912, 0.0010758247869061776, 0.0002744275045475249, -8.029535460573281e-21],
        },
        "q7.xy.y180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 7.140266213968801e-05, 0.0003030547656447785, 0.0008396348285968098, 0.0017959836520728884, 0.0032453419219738862, 0.005211092845650112, 0.007662730647548999, 0.010516437590361184, 0.013640282115013776, 0.01686367766941791, 0.01999039508306382, 0.022814128232215243, 0.02513539642988026, 0.026778444774005504, 0.02760678565870809, 0.027536112817346487, 0.02654350742428085, 0.024672129972282023, 0.0220309311935979, 0.01878929439721397, 0.015166911280064943, 0.011419563616160871, 0.007821805663931819, 0.0046477916336201824, 0.002151649573812355, 0.0005488550090950498, -1.6059070921146565e-20],
        },
        "q7.xy.y180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0006111507311347972, 0.0024043824972849346, 0.005261828068419316, 0.008996151598091794, 0.01336351431849177, 0.01808038314363127, 0.022842960300863947, 0.027347826179509697, 0.03131230673148022, 0.03449310675505968, 0.036701888627180844, 0.03781671173591753, 0.037788562877863946, 0.03664257815093054, 0.0344739542133999, 0.031438941065012604, 0.027741669952818546, 0.023617871446307143, 0.019316757675127402, 0.015082463072673415, 0.01113645120714538, 0.007662201116357544, 0.004793292919282822, 0.0026057348670669527, 0.0011150343024962386, 0.0002781397765845407, 4.362284073217507e-20],
        },
        "q7.xy.y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 3.570133106984401e-05, 0.00015152738282238925, 0.0004198174142984049, 0.0008979918260364442, 0.0016226709609869431, 0.002605546422825056, 0.0038313653237744996, 0.005258218795180592, 0.006820141057506888, 0.008431838834708955, 0.00999519754153191, 0.011407064116107622, 0.01256769821494013, 0.013389222387002752, 0.013803392829354045, 0.013768056408673244, 0.013271753712140425, 0.012336064986141012, 0.01101546559679895, 0.009394647198606986, 0.007583455640032472, 0.005709781808080436, 0.003910902831965909, 0.0023238958168100912, 0.0010758247869061776, 0.0002744275045475249, -8.029535460573283e-21],
        },
        "q7.xy.y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0003055753655673986, 0.0012021912486424673, 0.002630914034209658, 0.004498075799045897, 0.006681757159245885, 0.009040191571815634, 0.011421480150431974, 0.013673913089754849, 0.01565615336574011, 0.01724655337752984, 0.018350944313590422, 0.018908355867958766, 0.018894281438931973, 0.01832128907546527, 0.01723697710669995, 0.015719470532506302, 0.013870834976409273, 0.011808935723153571, 0.009658378837563701, 0.0075412315363367075, 0.00556822560357269, 0.003831100558178772, 0.002396646459641411, 0.0013028674335334764, 0.0005575171512481193, 0.00013906988829227035, 2.1811420366087536e-20],
        },
        "q7.xy.-y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -3.5701331069843966e-05, -0.0001515273828223891, -0.00041981741429840457, -0.0008979918260364436, -0.0016226709609869423, -0.002605546422825055, -0.003831365323774498, -0.00525821879518059, -0.0068201410575068865, -0.008431838834708952, -0.009995197541531907, -0.011407064116107618, -0.012567698214940127, -0.013389222387002749, -0.013803392829354041, -0.01376805640867324, -0.013271753712140425, -0.012336064986141012, -0.01101546559679895, -0.009394647198606986, -0.007583455640032472, -0.005709781808080436, -0.003910902831965909, -0.0023238958168100912, -0.0010758247869061776, -0.0002744275045475249, 8.029535460573286e-21],
        },
        "q7.xy.-y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.0003055753655673986, -0.0012021912486424673, -0.002630914034209658, -0.004498075799045897, -0.006681757159245885, -0.009040191571815634, -0.011421480150431974, -0.013673913089754849, -0.01565615336574011, -0.01724655337752984, -0.018350944313590422, -0.018908355867958766, -0.018894281438931973, -0.01832128907546527, -0.01723697710669995, -0.015719470532506302, -0.013870834976409273, -0.011808935723153571, -0.009658378837563701, -0.007541231536336709, -0.005568225603572691, -0.0038311005581787728, -0.002396646459641412, -0.0013028674335334768, -0.0005575171512481195, -0.0001390698882922704, -2.1811420366087536e-20],
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
            "sample": 0.053928929583904925,
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
            "samples": [0.0, 0.00463001615930933, 0.018247383444917428, 0.04005040112564875, 0.06875637737675126, 0.1026784052326451, 0.13982619259534596, 0.1780247890942569, 0.2150439710783139, 0.24873041335404655, 0.27713463088982093, 0.2986250234557166, 0.3119821779287401, 0.3164678241520553, 0.3118644220811366, 0.29848318068755786, 0.2771402581970707, 0.24910284671355223, 0.216008680364199, 0.17976411094722797, 0.14242716988603296, 0.1060829025387238, 0.07271866905639778, 0.044107032667613864, 0.021703309562083502, 0.006563872287682304, -0.0007100541984628345, -4.8629040688787815e-18],
        },
        "q8.xy.x180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.00796112679719496, -0.01488957041978051, -0.019831952615434606, -0.021987828088880015, -0.020772350144276842, -0.015863444809666536, -0.007230034675605405, 0.0048608342409090935, 0.01985864418443848, 0.03696499854776062, 0.055187848979409655, 0.0734107295650413, 0.09047229069182314, 0.10525065960154636, 0.1167467575869685, 0.12416070471514916, 0.12695584474642252, 0.12490570156496603, 0.11812028454927229, 0.10704952223957019, 0.0924631321441131, 0.0754078285213268, 0.05714432328148112, 0.03906798342528813, 0.022618176108219833, 0.009182179074257148, 7.048338519495266e-18],
        },
        "q8.xy.x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0014200227136768107, 0.005596459723980372, 0.012283429978087231, 0.021087532791610325, 0.03149139497954109, 0.04288459534922199, 0.05460007814510073, 0.06595383533521346, 0.07628544359068848, 0.08499699721754096, 0.09158808556785797, 0.0956847154907679, 0.09706046004617704, 0.0956485998547719, 0.09154458249019563, 0.08499872310873369, 0.07639966864123517, 0.06624971099761201, 0.055133526939366226, 0.04368231326282082, 0.03253555191915843, 0.02230276487497956, 0.013527596031163719, 0.006656389843942803, 0.002013135033976438, -0.00021777312542019644, -1.4914492724512114e-18],
        },
        "q8.xy.x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.0024416720135517524, -0.0045666208206350456, -0.006082445978910004, -0.006743651476864012, -0.006370865242448973, -0.00486530741401242, -0.0022174465718413712, 0.0014908144576624004, 0.006090632264431482, 0.01133713916814507, 0.016926074634136406, 0.02251501934833309, 0.0277477881977683, 0.03228030359314279, 0.03580614879459643, 0.03808000118684943, 0.03893726867701464, 0.03830849119896969, 0.03622740855205911, 0.03283201350448778, 0.02835837787700666, 0.02312752819966477, 0.017526123932469936, 0.011982123157370149, 0.006936978772965125, 0.0028161678918282875, 2.1617204880035448e-18],
        },
        "q8.xy.-x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -0.0014200227136768105, -0.005596459723980371, -0.012283429978087231, -0.021087532791610325, -0.03149139497954109, -0.04288459534922199, -0.05460007814510073, -0.06595383533521346, -0.07628544359068848, -0.08499699721754096, -0.09158808556785797, -0.0956847154907679, -0.09706046004617704, -0.0956485998547719, -0.09154458249019563, -0.08499872310873369, -0.07639966864123517, -0.06624971099761201, -0.05513352693936623, -0.04368231326282083, -0.03253555191915844, -0.022302764874979564, -0.01352759603116372, -0.006656389843942805, -0.002013135033976439, 0.00021777312542019608, 1.4914492724512112e-18],
        },
        "q8.xy.-x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0024416720135517524, 0.004566620820635046, 0.006082445978910006, 0.006743651476864014, 0.0063708652424489766, 0.004865307414012425, 0.0022174465718413777, -0.0014908144576623924, -0.006090632264431473, -0.01133713916814506, -0.016926074634136395, -0.02251501934833308, -0.02774778819776829, -0.032280303593142774, -0.03580614879459642, -0.03808000118684941, -0.038937268677014636, -0.03830849119896968, -0.0362274085520591, -0.03283201350448777, -0.028358377877006655, -0.023127528199664765, -0.017526123932469936, -0.011982123157370149, -0.006936978772965125, -0.0028161678918282875, -2.1617204880035448e-18],
        },
        "q8.xy.y180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.00796112679719496, 0.014889570419780512, 0.01983195261543461, 0.02198782808888002, 0.02077235014427685, 0.015863444809666543, 0.007230034675605416, -0.0048608342409090805, -0.019858644184438466, -0.03696499854776061, -0.055187848979409634, -0.07341072956504129, -0.09047229069182312, -0.10525065960154635, -0.11674675758696848, -0.12416070471514914, -0.1269558447464225, -0.12490570156496601, -0.11812028454927227, -0.10704952223957018, -0.0924631321441131, -0.0754078285213268, -0.05714432328148112, -0.03906798342528813, -0.022618176108219833, -0.009182179074257148, -7.048338519495266e-18],
        },
        "q8.xy.y180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0046300161593093294, 0.018247383444917428, 0.04005040112564875, 0.06875637737675126, 0.1026784052326451, 0.13982619259534596, 0.1780247890942569, 0.2150439710783139, 0.24873041335404655, 0.27713463088982093, 0.2986250234557166, 0.3119821779287401, 0.3164678241520553, 0.3118644220811366, 0.29848318068755786, 0.2771402581970707, 0.24910284671355223, 0.216008680364199, 0.17976411094722797, 0.14242716988603296, 0.1060829025387238, 0.07271866905639778, 0.04410703266761387, 0.021703309562083505, 0.006563872287682306, -0.000710054198462834, -4.862904068878781e-18],
        },
        "q8.xy.y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0024416720135517524, 0.0045666208206350456, 0.006082445978910005, 0.0067436514768640125, 0.006370865242448975, 0.004865307414012423, 0.0022174465718413747, -0.0014908144576623963, -0.006090632264431478, -0.011337139168145065, -0.0169260746341364, -0.022515019348333082, -0.027747788197768294, -0.03228030359314278, -0.035806148794596426, -0.03808000118684942, -0.038937268677014636, -0.03830849119896968, -0.03622740855205911, -0.03283201350448778, -0.028358377877006655, -0.02312752819966477, -0.017526123932469936, -0.011982123157370149, -0.006936978772965125, -0.0028161678918282875, -2.1617204880035448e-18],
        },
        "q8.xy.y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0014200227136768105, 0.005596459723980372, 0.012283429978087231, 0.021087532791610325, 0.03149139497954109, 0.04288459534922199, 0.05460007814510073, 0.06595383533521346, 0.07628544359068848, 0.08499699721754096, 0.09158808556785797, 0.0956847154907679, 0.09706046004617704, 0.0956485998547719, 0.09154458249019563, 0.08499872310873369, 0.07639966864123517, 0.06624971099761201, 0.055133526939366226, 0.04368231326282082, 0.03253555191915843, 0.02230276487497956, 0.01352759603116372, 0.006656389843942804, 0.0020131350339764385, -0.00021777312542019627, -1.4914492724512112e-18],
        },
        "q8.xy.-y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -0.0024416720135517524, -0.0045666208206350456, -0.006082445978910003, -0.006743651476864011, -0.006370865242448971, -0.004865307414012417, -0.0022174465718413677, 0.0014908144576624045, 0.006090632264431487, 0.011337139168145076, 0.016926074634136413, 0.022515019348333096, 0.027747788197768308, 0.032280303593142795, 0.03580614879459644, 0.038080001186849434, 0.03893726867701465, 0.038308491198969695, 0.03622740855205911, 0.03283201350448778, 0.028358377877006662, 0.02312752819966477, 0.017526123932469936, 0.011982123157370149, 0.006936978772965125, 0.0028161678918282875, 2.1617204880035448e-18],
        },
        "q8.xy.-y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.001420022713676811, -0.005596459723980372, -0.012283429978087231, -0.021087532791610325, -0.03149139497954109, -0.04288459534922199, -0.05460007814510073, -0.06595383533521346, -0.07628544359068848, -0.08499699721754096, -0.09158808556785797, -0.0956847154907679, -0.09706046004617704, -0.0956485998547719, -0.09154458249019563, -0.08499872310873369, -0.07639966864123517, -0.06624971099761201, -0.055133526939366226, -0.04368231326282082, -0.03253555191915843, -0.02230276487497956, -0.013527596031163717, -0.006656389843942802, -0.0020131350339764376, 0.0002177731254201966, 1.4914492724512116e-18],
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
            "sample": 0.06763223593964335,
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
            "cosine": [(-0.3708905196588253, 2000)],
            "sine": [(0.9286765973293429, 2000)],
        },
        "q1.resonator.readout.iw2": {
            "cosine": [(-0.9286765973293429, 2000)],
            "sine": [(-0.3708905196588253, 2000)],
        },
        "q1.resonator.readout.iw3": {
            "cosine": [(0.9286765973293429, 2000)],
            "sine": [(0.3708905196588253, 2000)],
        },
        "q2.resonator.readout.iw1": {
            "cosine": [(-0.9925240821469165, 2000)],
            "sine": [(0.12204895066497343, 2000)],
        },
        "q2.resonator.readout.iw2": {
            "cosine": [(-0.12204895066497343, 2000)],
            "sine": [(-0.9925240821469165, 2000)],
        },
        "q2.resonator.readout.iw3": {
            "cosine": [(0.12204895066497343, 2000)],
            "sine": [(0.9925240821469165, 2000)],
        },
        "q3.resonator.readout.iw1": {
            "cosine": [(-0.670151037903351, 2000)],
            "sine": [(-0.7422247546377455, 2000)],
        },
        "q3.resonator.readout.iw2": {
            "cosine": [(0.7422247546377455, 2000)],
            "sine": [(-0.670151037903351, 2000)],
        },
        "q3.resonator.readout.iw3": {
            "cosine": [(-0.7422247546377455, 2000)],
            "sine": [(0.670151037903351, 2000)],
        },
        "q4.resonator.readout.iw1": {
            "cosine": [(-0.4484474924845168, 2000)],
            "sine": [(-0.8938091778922105, 2000)],
        },
        "q4.resonator.readout.iw2": {
            "cosine": [(0.8938091778922105, 2000)],
            "sine": [(-0.4484474924845168, 2000)],
        },
        "q4.resonator.readout.iw3": {
            "cosine": [(-0.8938091778922105, 2000)],
            "sine": [(0.4484474924845168, 2000)],
        },
        "q5.resonator.readout.iw1": {
            "cosine": [(0.9597091748147896, 2000)],
            "sine": [(0.28099519529044564, 2000)],
        },
        "q5.resonator.readout.iw2": {
            "cosine": [(-0.28099519529044564, 2000)],
            "sine": [(0.9597091748147896, 2000)],
        },
        "q5.resonator.readout.iw3": {
            "cosine": [(0.28099519529044564, 2000)],
            "sine": [(-0.9597091748147896, 2000)],
        },
        "q6.resonator.readout.iw1": {
            "cosine": [(-0.8182412482737133, 2000)],
            "sine": [(0.5748749947801484, 2000)],
        },
        "q6.resonator.readout.iw2": {
            "cosine": [(-0.5748749947801484, 2000)],
            "sine": [(-0.8182412482737133, 2000)],
        },
        "q6.resonator.readout.iw3": {
            "cosine": [(0.5748749947801484, 2000)],
            "sine": [(0.8182412482737133, 2000)],
        },
        "q7.resonator.readout.iw1": {
            "cosine": [(-0.9999526806088935, 2000)],
            "sine": [(-0.00972813153119021, 2000)],
        },
        "q7.resonator.readout.iw2": {
            "cosine": [(0.00972813153119021, 2000)],
            "sine": [(-0.9999526806088935, 2000)],
        },
        "q7.resonator.readout.iw3": {
            "cosine": [(-0.00972813153119021, 2000)],
            "sine": [(0.9999526806088935, 2000)],
        },
        "q8.resonator.readout.iw1": {
            "cosine": [(0.567637767708887, 2000)],
            "sine": [(0.8232784247570634, 2000)],
        },
        "q8.resonator.readout.iw2": {
            "cosine": [(-0.8232784247570634, 2000)],
            "sine": [(0.567637767708887, 2000)],
        },
        "q8.resonator.readout.iw3": {
            "cosine": [(0.8232784247570634, 2000)],
            "sine": [(-0.567637767708887, 2000)],
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
            "intermediate_frequency": 51426404.60324453,
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
            "intermediate_frequency": 50120905.0,
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
            "intermediate_frequency": 50771317.958204485,
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
            "intermediate_frequency": 50674765.0,
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
            "intermediate_frequency": 47605795.797873005,
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
            "intermediate_frequency": 50288915.0,
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
            "intermediate_frequency": 50840259.77639715,
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
            "intermediate_frequency": 49481765.0,
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
            "intermediate_frequency": 49910259.46311582,
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
            "intermediate_frequency": 51021316.0,
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
            "intermediate_frequency": 51203539.02641499,
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
            "intermediate_frequency": 51257184.30678039,
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
            "intermediate_frequency": 50840298.0896424,
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
            "intermediate_frequency": -180228682.04179573,
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
            "intermediate_frequency": 282426404.6032448,
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
            "intermediate_frequency": 30605795.797872543,
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
            "samples": [0.0, 0.003138527302470915, 0.0123730182654633, 0.027170784793859648, 0.046678667260076516, 0.06977285303236916, 0.09512443172624098, 0.12127680051438272, 0.1467303358760095, 0.17002932633834628, 0.18984603897108973, 0.2050569773632444, 0.21480686869964116, 0.21855666270889954, 0.21611279005089107, 0.20763605336456972, 0.19362974236906597, 0.17490780139626133, 0.15254505895735265, 0.12781258350691474, 0.10210209453759578, 0.07684398236343083, 0.05342383711833801, 0.0331024382869832, 0.01694390926588425, 0.005756213868943394, 4.739714754167214e-05, -2.9058699871086474e-18],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.xy.x180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.005662928898113587, -0.01068177932598392, -0.014460206436451276, -0.016494004550194924, -0.016409080609930897, -0.013990324906695654, -0.009199322567811228, -0.002179603673422463, 0.00675102531915266, 0.01712064680605409, 0.02833461630646744, 0.03971611331165615, 0.050553164009714824, 0.06014897490618011, 0.06787215806436933, 0.0732033968929995, 0.07577529987269063, 0.07540260702143868, 0.0721005245178405, 0.06608972817123616, 0.05778744739789006, 0.04778496180068675, 0.036812752447151556, 0.02569538976720347, 0.01529895396625175, 0.006474323968095041, 5.334881265600878e-18],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.xy.x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0015692636512354575, 0.00618650913273165, 0.013585392396929824, 0.023339333630038258, 0.03488642651618458, 0.04756221586312049, 0.06063840025719136, 0.07336516793800475, 0.08501466316917314, 0.09492301948554487, 0.1025284886816222, 0.10740343434982058, 0.10927833135444977, 0.10805639502544553, 0.10381802668228486, 0.09681487118453298, 0.08745390069813067, 0.07627252947867633, 0.06390629175345737, 0.05105104726879789, 0.038421991181715416, 0.026711918559169004, 0.0165512191434916, 0.008471954632942124, 0.002878106934471697, 2.369857377083607e-05, -1.4529349935543237e-18],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.xy.x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.0028314644490567936, -0.00534088966299196, -0.007230103218225638, -0.008247002275097462, -0.008204540304965448, -0.006995162453347827, -0.004599661283905614, -0.0010898018367112316, 0.00337551265957633, 0.008560323403027046, 0.01416730815323372, 0.019858056655828075, 0.025276582004857412, 0.030074487453090055, 0.033936079032184666, 0.03660169844649975, 0.037887649936345316, 0.03770130351071934, 0.03605026225892025, 0.03304486408561808, 0.02889372369894503, 0.023892480900343373, 0.018406376223575778, 0.012847694883601735, 0.007649476983125875, 0.0032371619840475207, 2.667440632800439e-18],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.xy.-x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -0.001569263651235457, -0.006186509132731649, -0.013585392396929822, -0.023339333630038258, -0.03488642651618458, -0.04756221586312049, -0.06063840025719136, -0.07336516793800475, -0.08501466316917314, -0.09492301948554487, -0.1025284886816222, -0.10740343434982058, -0.10927833135444977, -0.10805639502544553, -0.10381802668228486, -0.09681487118453298, -0.08745390069813067, -0.07627252947867633, -0.06390629175345737, -0.051051047268797896, -0.03842199118171542, -0.026711918559169007, -0.016551219143491603, -0.008471954632942126, -0.002878106934471698, -2.3698573770836465e-05, 1.4529349935543233e-18],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.xy.-x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0028314644490567936, 0.0053408896629919605, 0.00723010321822564, 0.008247002275097465, 0.008204540304965452, 0.006995162453347833, 0.004599661283905622, 0.0010898018367112405, -0.0033755126595763196, -0.008560323403027034, -0.014167308153233709, -0.01985805665582806, -0.025276582004857398, -0.03007448745309004, -0.03393607903218465, -0.036601698446499735, -0.0378876499363453, -0.03770130351071933, -0.036050262258920246, -0.033044864085618075, -0.028893723698945026, -0.02389248090034337, -0.018406376223575775, -0.012847694883601733, -0.007649476983125875, -0.0032371619840475207, -2.667440632800439e-18],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.xy.y180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.005662928898113587, 0.01068177932598392, 0.014460206436451278, 0.016494004550194927, 0.0164090806099309, 0.01399032490669566, 0.009199322567811235, 0.0021796036734224723, -0.0067510253191526495, -0.01712064680605408, -0.028334616306467428, -0.039716113311656136, -0.05055316400971481, -0.0601489749061801, -0.06787215806436932, -0.07320339689299948, -0.07577529987269062, -0.07540260702143867, -0.07210052451784049, -0.06608972817123616, -0.05778744739789005, -0.04778496180068675, -0.036812752447151556, -0.02569538976720347, -0.01529895396625175, -0.006474323968095041, -5.334881265600878e-18],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.xy.y180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0031385273024709145, 0.0123730182654633, 0.027170784793859648, 0.046678667260076516, 0.06977285303236916, 0.09512443172624098, 0.12127680051438272, 0.1467303358760095, 0.17002932633834628, 0.18984603897108973, 0.2050569773632444, 0.21480686869964116, 0.21855666270889954, 0.21611279005089107, 0.20763605336456972, 0.19362974236906597, 0.17490780139626133, 0.15254505895735265, 0.12781258350691474, 0.10210209453759578, 0.07684398236343083, 0.05342383711833801, 0.0331024382869832, 0.01694390926588425, 0.005756213868943395, 4.739714754167254e-05, -2.905869987108647e-18],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.xy.y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0028314644490567936, 0.00534088966299196, 0.007230103218225639, 0.008247002275097464, 0.00820454030496545, 0.00699516245334783, 0.0045996612839056174, 0.0010898018367112362, -0.0033755126595763248, -0.00856032340302704, -0.014167308153233714, -0.019858056655828068, -0.025276582004857405, -0.03007448745309005, -0.03393607903218466, -0.03660169844649974, -0.03788764993634531, -0.03770130351071933, -0.036050262258920246, -0.03304486408561808, -0.028893723698945026, -0.023892480900343373, -0.018406376223575778, -0.012847694883601735, -0.007649476983125875, -0.0032371619840475207, -2.667440632800439e-18],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.xy.y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0015692636512354573, 0.00618650913273165, 0.013585392396929824, 0.023339333630038258, 0.03488642651618458, 0.04756221586312049, 0.06063840025719136, 0.07336516793800475, 0.08501466316917314, 0.09492301948554487, 0.1025284886816222, 0.10740343434982058, 0.10927833135444977, 0.10805639502544553, 0.10381802668228486, 0.09681487118453298, 0.08745390069813067, 0.07627252947867633, 0.06390629175345737, 0.05105104726879789, 0.038421991181715416, 0.026711918559169004, 0.0165512191434916, 0.008471954632942124, 0.0028781069344716976, 2.369857377083627e-05, -1.4529349935543235e-18],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.xy.-y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -0.0028314644490567936, -0.00534088966299196, -0.007230103218225637, -0.00824700227509746, -0.008204540304965447, -0.006995162453347825, -0.0045996612839056105, -0.001089801836711227, 0.003375512659576335, 0.00856032340302705, 0.014167308153233728, 0.019858056655828082, 0.02527658200485742, 0.030074487453090062, 0.03393607903218467, 0.036601698446499756, 0.03788764993634532, 0.03770130351071935, 0.03605026225892026, 0.03304486408561808, 0.028893723698945033, 0.023892480900343373, 0.018406376223575778, 0.012847694883601735, 0.007649476983125875, 0.0032371619840475207, 2.667440632800439e-18],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.xy.-y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.0015692636512354577, -0.00618650913273165, -0.013585392396929824, -0.023339333630038258, -0.03488642651618458, -0.04756221586312049, -0.06063840025719136, -0.07336516793800475, -0.08501466316917314, -0.09492301948554487, -0.1025284886816222, -0.10740343434982058, -0.10927833135444977, -0.10805639502544553, -0.10381802668228486, -0.09681487118453298, -0.08745390069813067, -0.07627252947867633, -0.06390629175345737, -0.05105104726879789, -0.038421991181715416, -0.026711918559169004, -0.0165512191434916, -0.008471954632942124, -0.0028781069344716967, -2.369857377083587e-05, 1.4529349935543239e-18],
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
            "sample": 0.1133636504292105,
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
            "samples": [0.0, 0.0022178495452366597, 0.008704695351839492, 0.018973731613405254, 0.03225684454928212, 0.04756565546205715, 0.06376971277292262, 0.07968531343000894, 0.0941675684586457, 0.10619808974796346, 0.11496108467816765, 0.11990166568420395, 0.12076172482903294, 0.11759065577080342, 0.11073036081236472, 0.10077617380627042, 0.08851737239987781, 0.07486267052296171, 0.06075732748495396, 0.04709917774951648, 0.0346609194938273, 0.024025399220614644, 0.015539447488184513, 0.009290160848663447, 0.0051055320356405715, 0.0025791776187684074, 0.0011167866800144079, 1.2625662247269476e-18],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.xy.x180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.0013334758574539845, -0.003421453651042604, -0.006939106422337691, -0.01241015440079845, -0.02014852014342328, -0.030219129626052423, -0.04242154721347455, -0.05629812708197781, -0.07116620567310163, -0.08617173622972105, -0.10035986173525957, -0.11275640228646477, -0.12245322973039365, -0.12869010447728946, -0.13092579284937908, -0.12889214896489387, -0.12262626014600597, -0.11247759889377427, -0.09908924017102819, -0.0833544090271549, -0.06635173136239397, -0.04926438891600118, -0.03328977116073602, -0.019547051744728938, -0.008990323079034097, -0.0023344810941751913, -1.2046827555042265e-19],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.xy.x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0011089247726183298, 0.004352347675919746, 0.009486865806702627, 0.01612842227464106, 0.023782827731028574, 0.03188485638646131, 0.03984265671500447, 0.04708378422932285, 0.05309904487398173, 0.057480542339083826, 0.059950832842101974, 0.06038086241451647, 0.05879532788540171, 0.05536518040618236, 0.05038808690313521, 0.044258686199938904, 0.037431335261480854, 0.03037866374247698, 0.02354958887475824, 0.01733045974691365, 0.012012699610307322, 0.007769723744092257, 0.004645080424331724, 0.0025527660178202858, 0.0012895888093842037, 0.0005583933400072039, 6.312831123634738e-19],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.xy.x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.0006667379287269923, -0.001710726825521302, -0.0034695532111688457, -0.006205077200399225, -0.01007426007171164, -0.015109564813026211, -0.021210773606737274, -0.028149063540988905, -0.03558310283655081, -0.04308586811486052, -0.050179930867629785, -0.05637820114323239, -0.06122661486519682, -0.06434505223864473, -0.06546289642468954, -0.06444607448244694, -0.061313130073002986, -0.05623879944688714, -0.04954462008551409, -0.04167720451357745, -0.03317586568119699, -0.02463219445800059, -0.01664488558036801, -0.009773525872364469, -0.004495161539517048, -0.0011672405470875957, -6.023413777521132e-20],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.xy.-x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -0.0011089247726183298, -0.004352347675919746, -0.009486865806702627, -0.01612842227464106, -0.023782827731028574, -0.03188485638646131, -0.03984265671500447, -0.04708378422932285, -0.053099044873981725, -0.05748054233908382, -0.05995083284210197, -0.06038086241451646, -0.058795327885401705, -0.05536518040618235, -0.050388086903135204, -0.0442586861999389, -0.03743133526148085, -0.030378663742476972, -0.023549588874758234, -0.017330459746913645, -0.012012699610307319, -0.007769723744092254, -0.004645080424331722, -0.0025527660178202845, -0.001289588809384203, -0.0005583933400072038, -6.312831123634738e-19],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.xy.-x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0006667379287269924, 0.0017107268255213024, 0.003469553211168847, 0.0062050772003992265, 0.010074260071711643, 0.015109564813026215, 0.021210773606737277, 0.028149063540988912, 0.03558310283655082, 0.04308586811486053, 0.05017993086762979, 0.056378201143232394, 0.06122661486519683, 0.06434505223864473, 0.06546289642468954, 0.06444607448244694, 0.06131313007300299, 0.056238799446887144, 0.04954462008551409, 0.04167720451357745, 0.03317586568119699, 0.02463219445800059, 0.01664488558036801, 0.009773525872364469, 0.004495161539517048, 0.0011672405470875957, 6.02341377752114e-20],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.xy.y180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0013334758574539847, 0.0034214536510426045, 0.006939106422337692, 0.012410154400798451, 0.020148520143423283, 0.030219129626052426, 0.042421547213474554, 0.05629812708197782, 0.07116620567310163, 0.08617173622972106, 0.10035986173525958, 0.11275640228646479, 0.12245322973039366, 0.12869010447728946, 0.13092579284937908, 0.12889214896489387, 0.12262626014600597, 0.11247759889377427, 0.09908924017102819, 0.0833544090271549, 0.06635173136239397, 0.04926438891600118, 0.03328977116073602, 0.019547051744728938, 0.008990323079034097, 0.0023344810941751913, 1.2046827555042272e-19],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.xy.y180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0022178495452366597, 0.008704695351839492, 0.018973731613405254, 0.03225684454928212, 0.04756565546205715, 0.06376971277292262, 0.07968531343000894, 0.0941675684586457, 0.10619808974796346, 0.11496108467816765, 0.11990166568420395, 0.12076172482903294, 0.11759065577080341, 0.1107303608123647, 0.10077617380627041, 0.0885173723998778, 0.0748626705229617, 0.06075732748495395, 0.047099177749516476, 0.03466091949382729, 0.02402539922061464, 0.01553944748818451, 0.009290160848663446, 0.005105532035640571, 0.002579177618768407, 0.0011167866800144077, 1.2625662247269476e-18],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.xy.y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0006667379287269924, 0.0017107268255213022, 0.003469553211168846, 0.006205077200399226, 0.010074260071711642, 0.015109564813026213, 0.021210773606737277, 0.02814906354098891, 0.03558310283655081, 0.04308586811486053, 0.05017993086762979, 0.056378201143232394, 0.06122661486519683, 0.06434505223864473, 0.06546289642468954, 0.06444607448244694, 0.061313130073002986, 0.05623879944688714, 0.04954462008551409, 0.04167720451357745, 0.03317586568119699, 0.02463219445800059, 0.01664488558036801, 0.009773525872364469, 0.004495161539517048, 0.0011672405470875957, 6.023413777521136e-20],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.xy.y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0011089247726183298, 0.004352347675919746, 0.009486865806702627, 0.01612842227464106, 0.023782827731028574, 0.03188485638646131, 0.03984265671500447, 0.04708378422932285, 0.05309904487398173, 0.057480542339083826, 0.059950832842101974, 0.06038086241451647, 0.058795327885401705, 0.05536518040618235, 0.050388086903135204, 0.0442586861999389, 0.03743133526148085, 0.030378663742476976, 0.023549588874758238, 0.017330459746913645, 0.01201269961030732, 0.007769723744092255, 0.004645080424331723, 0.0025527660178202853, 0.0012895888093842035, 0.0005583933400072038, 6.312831123634738e-19],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.xy.-y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -0.0006667379287269922, -0.0017107268255213018, -0.0034695532111688452, -0.006205077200399224, -0.010074260071711638, -0.01510956481302621, -0.02121077360673727, -0.0281490635409889, -0.03558310283655081, -0.043085868114860516, -0.05017993086762978, -0.05637820114323238, -0.061226614865196816, -0.06434505223864473, -0.06546289642468954, -0.06444607448244694, -0.061313130073002986, -0.05623879944688714, -0.04954462008551409, -0.04167720451357745, -0.03317586568119699, -0.02463219445800059, -0.01664488558036801, -0.009773525872364469, -0.004495161539517048, -0.0011672405470875957, -6.023413777521129e-20],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.xy.-y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.0011089247726183298, -0.004352347675919746, -0.009486865806702627, -0.01612842227464106, -0.023782827731028574, -0.03188485638646131, -0.03984265671500447, -0.04708378422932285, -0.05309904487398173, -0.057480542339083826, -0.059950832842101974, -0.06038086241451647, -0.05879532788540172, -0.055365180406182365, -0.05038808690313522, -0.04425868619993891, -0.03743133526148086, -0.030378663742476983, -0.023549588874758245, -0.017330459746913652, -0.012012699610307324, -0.007769723744092258, -0.0046450804243317245, -0.002552766017820286, -0.001289588809384204, -0.000558393340007204, -6.312831123634738e-19],
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
            "sample": 0.09345462248456422,
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
            "samples": [0.0, 0.003427538996024826, 0.013519611757053481, 0.029715229616201985, 0.051114293164133295, 0.07652785442388323, 0.10454448300561378, 0.13360900809989126, 0.16210921518023078, 0.1884656329957647, 0.21121937770688004, 0.22911313613344225, 0.24116076223425212, 0.24670160761244658, 0.24543657114292666, 0.23744388556103913, 0.22317380138291734, 0.20342251607027592, 0.17928686169696081, 0.1521023417031031, 0.12336803594552827, 0.09466262104664397, 0.06755623939422957, 0.04352316822751625, 0.023860178517195827, 0.009615136161162783, 0.001529805331169329, -1.882573198122245e-18],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q3.xy.x180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.00634288334266427, -0.012133358106591843, -0.016856584190987407, -0.020070399253618823, -0.02143566652365199, -0.020739862895168333, -0.017912341099550703, -0.013030232726801596, -0.006314559281958048, 0.0018832514502115153, 0.011103626426996919, 0.020808497684380957, 0.030416468670258486, 0.039341254562322646, 0.04703092628220836, 0.05300541524249874, 0.05688982431458829, 0.0584413355620361, 0.05756789261122428, 0.054337341819841734, 0.04897631076756308, 0.04185874843979246, 0.0334847087385862, 0.024450586554498093, 0.015412574009767387, 0.007045558055728747, 6.507320532481616e-18],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q3.xy.x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.001713769498012413, 0.006759805878526741, 0.014857614808100992, 0.025557146582066648, 0.03826392721194161, 0.05227224150280689, 0.06680450404994563, 0.08105460759011539, 0.09423281649788234, 0.10560968885344002, 0.11455656806672113, 0.12058038111712606, 0.12335080380622329, 0.12271828557146333, 0.11872194278051956, 0.11158690069145867, 0.10171125803513796, 0.08964343084848041, 0.07605117085155155, 0.061684017972764134, 0.047331310523321984, 0.033778119697114785, 0.021761584113758125, 0.011930089258597914, 0.004807568080581391, 0.0007649026655846645, -9.412865990611225e-19],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q3.xy.x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.003171441671332135, -0.006066679053295922, -0.008428292095493704, -0.010035199626809412, -0.010717833261825994, -0.010369931447584167, -0.008956170549775351, -0.006515116363400798, -0.003157279640979024, 0.0009416257251057576, 0.005551813213498459, 0.010404248842190478, 0.015208234335129243, 0.019670627281161323, 0.02351546314110418, 0.02650270762124937, 0.028444912157294146, 0.02922066778101805, 0.02878394630561214, 0.027168670909920867, 0.02448815538378154, 0.02092937421989623, 0.0167423543692931, 0.012225293277249047, 0.007706287004883693, 0.0035227790278643733, 3.253660266240808e-18],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q3.xy.-x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -0.0017137694980124125, -0.00675980587852674, -0.01485761480810099, -0.025557146582066648, -0.03826392721194161, -0.05227224150280689, -0.06680450404994563, -0.08105460759011539, -0.09423281649788234, -0.10560968885344002, -0.11455656806672113, -0.12058038111712606, -0.12335080380622329, -0.12271828557146333, -0.11872194278051956, -0.11158690069145867, -0.10171125803513796, -0.08964343084848041, -0.07605117085155155, -0.061684017972764134, -0.047331310523321984, -0.033778119697114785, -0.02176158411375813, -0.011930089258597915, -0.004807568080581392, -0.0007649026655846649, 9.41286599061122e-19],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q3.xy.-x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.003171441671332135, 0.0060666790532959225, 0.008428292095493705, 0.010035199626809415, 0.010717833261826, 0.010369931447584173, 0.00895617054977536, 0.006515116363400807, 0.0031572796409790357, -0.0009416257251057447, -0.0055518132134984455, -0.010404248842190463, -0.015208234335129227, -0.01967062728116131, -0.023515463141104167, -0.026502707621249354, -0.028444912157294132, -0.02922066778101804, -0.02878394630561213, -0.02716867090992086, -0.024488155383781532, -0.020929374219896227, -0.016742354369293097, -0.012225293277249045, -0.0077062870048836924, -0.0035227790278643733, -3.253660266240808e-18],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q3.xy.y180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.00634288334266427, 0.012133358106591843, 0.01685658419098741, 0.020070399253618827, 0.021435666523651992, 0.02073986289516834, 0.01791234109955071, 0.013030232726801606, 0.006314559281958059, -0.0018832514502115023, -0.011103626426996905, -0.020808497684380943, -0.030416468670258472, -0.03934125456232263, -0.04703092628220835, -0.05300541524249872, -0.05688982431458828, -0.05844133556203609, -0.057567892611224275, -0.05433734181984173, -0.04897631076756307, -0.041858748439792454, -0.0334847087385862, -0.024450586554498093, -0.015412574009767387, -0.007045558055728747, -6.507320532481616e-18],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q3.xy.y180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0034275389960248255, 0.013519611757053481, 0.029715229616201985, 0.051114293164133295, 0.07652785442388323, 0.10454448300561378, 0.13360900809989126, 0.16210921518023078, 0.1884656329957647, 0.21121937770688004, 0.22911313613344225, 0.24116076223425212, 0.24670160761244658, 0.24543657114292666, 0.23744388556103913, 0.22317380138291734, 0.20342251607027592, 0.17928686169696081, 0.1521023417031031, 0.12336803594552827, 0.09466262104664397, 0.06755623939422957, 0.04352316822751625, 0.023860178517195827, 0.009615136161162784, 0.0015298053311693293, -1.8825731981222445e-18],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q3.xy.y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.003171441671332135, 0.006066679053295922, 0.008428292095493705, 0.010035199626809413, 0.010717833261825996, 0.01036993144758417, 0.008956170549775355, 0.006515116363400803, 0.0031572796409790297, -0.0009416257251057511, -0.0055518132134984525, -0.010404248842190471, -0.015208234335129236, -0.019670627281161316, -0.023515463141104174, -0.02650270762124936, -0.02844491215729414, -0.029220667781018044, -0.028783946305612138, -0.027168670909920863, -0.024488155383781535, -0.020929374219896227, -0.0167423543692931, -0.012225293277249047, -0.007706287004883693, -0.0035227790278643733, -3.253660266240808e-18],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q3.xy.y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0017137694980124127, 0.006759805878526741, 0.014857614808100992, 0.025557146582066648, 0.03826392721194161, 0.05227224150280689, 0.06680450404994563, 0.08105460759011539, 0.09423281649788234, 0.10560968885344002, 0.11455656806672113, 0.12058038111712606, 0.12335080380622329, 0.12271828557146333, 0.11872194278051956, 0.11158690069145867, 0.10171125803513796, 0.08964343084848041, 0.07605117085155155, 0.061684017972764134, 0.047331310523321984, 0.033778119697114785, 0.021761584113758125, 0.011930089258597914, 0.004807568080581392, 0.0007649026655846647, -9.412865990611223e-19],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q3.xy.-y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -0.003171441671332135, -0.006066679053295922, -0.008428292095493702, -0.01003519962680941, -0.010717833261825993, -0.010369931447584163, -0.008956170549775348, -0.006515116363400793, -0.0031572796409790184, 0.0009416257251057641, 0.005551813213498466, 0.010404248842190485, 0.01520823433512925, 0.01967062728116133, 0.023515463141104188, 0.026502707621249375, 0.028444912157294153, 0.029220667781018058, 0.028783946305612144, 0.02716867090992087, 0.024488155383781542, 0.020929374219896234, 0.0167423543692931, 0.012225293277249047, 0.007706287004883693, 0.0035227790278643733, 3.253660266240808e-18],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q3.xy.-y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.0017137694980124132, -0.006759805878526741, -0.014857614808100992, -0.025557146582066648, -0.03826392721194161, -0.05227224150280689, -0.06680450404994563, -0.08105460759011539, -0.09423281649788234, -0.10560968885344002, -0.11455656806672113, -0.12058038111712606, -0.12335080380622329, -0.12271828557146333, -0.11872194278051956, -0.11158690069145867, -0.10171125803513796, -0.08964343084848041, -0.07605117085155155, -0.061684017972764134, -0.047331310523321984, -0.033778119697114785, -0.021761584113758125, -0.011930089258597914, -0.00480756808058139, -0.0007649026655846642, 9.412865990611227e-19],
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
            "sample": 0.09301178911991174,
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
            "samples": [0.0, 0.0031418179039661917, 0.012398841698068305, 0.027274818735635063, 0.04697229950836004, 0.07043542202344713, 0.09640655656094506, 0.12349376838997234, 0.15024547533331314, 0.1752282911899412, 0.1971038756743615, 0.21470066582934424, 0.22707663984420196, 0.2335697469668364, 0.23383330071519923, 0.22785444113561082, 0.21595468189393305, 0.19877252054859923, 0.17722905366355216, 0.1524784506782249, 0.12584595263554185, 0.09875673036072367, 0.07265942562023679, 0.048948481988143416, 0.028889434506606495, 0.013551165538152526, 0.003748757313981707, 6.627987933035159e-19],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q4.xy.x180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.005771852513742905, -0.011307947348866308, -0.016382559601478646, -0.020789632615630372, -0.024351632562333917, -0.026927265624842597, -0.028417741114190504, -0.028771315401553907, -0.027985913517889836, -0.026109695947102673, -0.023239515487715176, -0.019517290705797642, -0.015124405771312535, -0.01027432843170332, -0.005203715423279538, -0.00016234456470761506, 0.004597728032518575, 0.008833341740214096, 0.012321263199731243, 0.014868592618074349, 0.016322070653836635, 0.01657584244041028, 0.01557728655614855, 0.01333058776071953, 0.009897821035767302, 0.005397417881075277, 6.080606192049252e-18],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q4.xy.x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0015709089519830959, 0.006199420849034153, 0.013637409367817531, 0.02348614975418002, 0.035217711011723565, 0.04820327828047253, 0.06174688419498617, 0.07512273766665657, 0.0876141455949706, 0.09855193783718075, 0.10735033291467212, 0.11353831992210098, 0.1167848734834182, 0.11691665035759961, 0.11392722056780541, 0.10797734094696652, 0.09938626027429961, 0.08861452683177608, 0.07623922533911245, 0.06292297631777093, 0.04937836518036184, 0.036329712810118396, 0.024474240994071708, 0.014444717253303247, 0.006775582769076263, 0.0018743786569908535, 3.3139939665175794e-19],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q4.xy.x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.0028859262568714525, -0.005653973674433154, -0.008191279800739323, -0.010394816307815186, -0.012175816281166959, -0.013463632812421298, -0.014208870557095252, -0.014385657700776953, -0.013992956758944918, -0.013054847973551336, -0.011619757743857588, -0.009758645352898821, -0.007562202885656268, -0.00513716421585166, -0.002601857711639769, -8.117228235380753e-05, 0.0022988640162592876, 0.004416670870107048, 0.006160631599865621, 0.007434296309037174, 0.008161035326918318, 0.00828792122020514, 0.007788643278074275, 0.006665293880359765, 0.004948910517883651, 0.0026987089405376384, 3.040303096024626e-18],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q4.xy.-x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -0.0015709089519830954, -0.006199420849034152, -0.01363740936781753, -0.02348614975418002, -0.035217711011723565, -0.04820327828047253, -0.06174688419498617, -0.07512273766665657, -0.0876141455949706, -0.09855193783718075, -0.10735033291467212, -0.11353831992210098, -0.1167848734834182, -0.11691665035759961, -0.11392722056780541, -0.10797734094696652, -0.09938626027429961, -0.08861452683177608, -0.07623922533911245, -0.06292297631777093, -0.04937836518036184, -0.036329712810118396, -0.024474240994071708, -0.014444717253303247, -0.006775582769076264, -0.001874378656990854, -3.313993966517583e-19],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q4.xy.-x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0028859262568714525, 0.005653973674433155, 0.008191279800739325, 0.01039481630781519, 0.012175816281166962, 0.013463632812421304, 0.014208870557095259, 0.014385657700776962, 0.013992956758944929, 0.013054847973551349, 0.011619757743857602, 0.009758645352898835, 0.0075622028856562815, 0.005137164215851675, 0.002601857711639783, 8.117228235382076e-05, -0.0022988640162592755, -0.004416670870107037, -0.006160631599865612, -0.0074342963090371665, -0.008161035326918312, -0.008287921220205136, -0.007788643278074272, -0.0066652938803597635, -0.00494891051788365, -0.002698708940537638, -3.040303096024626e-18],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q4.xy.y180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.005771852513742905, 0.011307947348866308, 0.016382559601478646, 0.020789632615630375, 0.02435163256233392, 0.026927265624842604, 0.02841774111419051, 0.028771315401553917, 0.027985913517889847, 0.026109695947102683, 0.02323951548771519, 0.019517290705797656, 0.015124405771312549, 0.010274328431703334, 0.005203715423279552, 0.0001623445647076283, -0.004597728032518563, -0.008833341740214086, -0.012321263199731234, -0.014868592618074342, -0.016322070653836628, -0.016575842440410278, -0.015577286556148547, -0.013330587760719529, -0.009897821035767302, -0.005397417881075277, -6.080606192049252e-18],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q4.xy.y180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0031418179039661913, 0.012398841698068305, 0.027274818735635063, 0.04697229950836004, 0.07043542202344713, 0.09640655656094506, 0.12349376838997234, 0.15024547533331314, 0.1752282911899412, 0.1971038756743615, 0.21470066582934424, 0.22707663984420196, 0.2335697469668364, 0.23383330071519923, 0.22785444113561082, 0.21595468189393305, 0.19877252054859923, 0.17722905366355216, 0.1524784506782249, 0.12584595263554185, 0.09875673036072367, 0.07265942562023679, 0.048948481988143416, 0.028889434506606495, 0.013551165538152526, 0.0037487573139817075, 6.627987933035163e-19],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q4.xy.y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0028859262568714525, 0.005653973674433154, 0.008191279800739323, 0.010394816307815188, 0.01217581628116696, 0.013463632812421302, 0.014208870557095256, 0.014385657700776959, 0.013992956758944923, 0.013054847973551342, 0.011619757743857595, 0.009758645352898828, 0.0075622028856562745, 0.005137164215851667, 0.002601857711639776, 8.117228235381415e-05, -0.0022988640162592815, -0.004416670870107043, -0.006160631599865617, -0.007434296309037171, -0.008161035326918314, -0.008287921220205139, -0.007788643278074273, -0.006665293880359764, -0.004948910517883651, -0.0026987089405376384, -3.040303096024626e-18],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q4.xy.y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0015709089519830956, 0.006199420849034153, 0.013637409367817531, 0.02348614975418002, 0.035217711011723565, 0.04820327828047253, 0.06174688419498617, 0.07512273766665657, 0.0876141455949706, 0.09855193783718075, 0.10735033291467212, 0.11353831992210098, 0.1167848734834182, 0.11691665035759961, 0.11392722056780541, 0.10797734094696652, 0.09938626027429961, 0.08861452683177608, 0.07623922533911245, 0.06292297631777093, 0.04937836518036184, 0.036329712810118396, 0.024474240994071708, 0.014444717253303247, 0.006775582769076263, 0.0018743786569908538, 3.3139939665175813e-19],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q4.xy.-y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -0.0028859262568714525, -0.005653973674433154, -0.008191279800739323, -0.010394816307815184, -0.012175816281166957, -0.013463632812421295, -0.014208870557095249, -0.014385657700776948, -0.013992956758944913, -0.013054847973551331, -0.011619757743857581, -0.009758645352898814, -0.007562202885656261, -0.005137164215851653, -0.0026018577116397623, -8.117228235380092e-05, 0.0022988640162592937, 0.004416670870107053, 0.006160631599865626, 0.007434296309037178, 0.008161035326918321, 0.008287921220205142, 0.007788643278074277, 0.006665293880359766, 0.004948910517883651, 0.0026987089405376384, 3.040303096024626e-18],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q4.xy.-y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.001570908951983096, -0.006199420849034153, -0.013637409367817531, -0.02348614975418002, -0.035217711011723565, -0.04820327828047253, -0.06174688419498617, -0.07512273766665657, -0.0876141455949706, -0.09855193783718075, -0.10735033291467212, -0.11353831992210098, -0.1167848734834182, -0.11691665035759961, -0.11392722056780541, -0.10797734094696652, -0.09938626027429961, -0.08861452683177608, -0.07623922533911245, -0.06292297631777093, -0.04937836518036184, -0.036329712810118396, -0.024474240994071708, -0.014444717253303247, -0.006775582769076263, -0.0018743786569908533, -3.3139939665175774e-19],
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
            "sample": 0.0779312997256516,
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
            "samples": [0.0, 0.0022145819444009305, 0.00871154599615161, 0.019060869351641297, 0.03257949049214639, 0.048379153583885615, 0.06542835526433981, 0.0826238213232975, 0.09886625542811753, 0.1131348155293711, 0.12455490664067752, 0.13245441978657654, 0.13640445320989494, 0.1362417526248674, 0.13207150915916932, 0.12425064822826161, 0.1133532147435172, 0.10012079674740719, 0.08540202867759122, 0.07008599366129967, 0.055034743408211184, 0.04102014592360599, 0.028669858695089073, 0.01842644293161499, 0.010522546201643772, 0.004973773392648244, 0.0015894430293642884, 8.967218359287526e-19],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q5.xy.x180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.0009881550572747077, -0.002550722228194775, -0.005204645039221282, -0.009356820302615613, -0.01526090589950815, -0.022987251147820784, -0.03240862393080892, -0.04320312666777444, -0.05487429313664531, -0.06678695124123799, -0.07821613497573703, -0.08840523598960594, -0.09662878902613306, -0.10225485071805616, -0.10480189416573123, -0.10398550763857162, -0.0997509282314294, -0.09228850432130324, -0.0820304828021743, -0.06962895786341451, -0.05591628578809323, -0.041850650565677744, -0.02845065004162883, -0.01672366861244572, -0.0075933389076911755, -0.0018315279037157404, 2.7254066193013106e-19],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q5.xy.x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0011072909722004652, 0.004355772998075805, 0.009530434675820649, 0.016289745246073194, 0.024189576791942807, 0.032714177632169904, 0.04131191066164875, 0.049433127714058764, 0.05656740776468555, 0.06227745332033876, 0.06622720989328827, 0.06820222660494747, 0.0681208763124337, 0.06603575457958466, 0.062125324114130805, 0.0566766073717586, 0.050060398373703595, 0.04270101433879561, 0.035042996830649834, 0.027517371704105592, 0.020510072961802996, 0.014334929347544536, 0.009213221465807496, 0.005261273100821886, 0.002486886696324122, 0.0007947215146821442, 4.483609179643763e-19],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q5.xy.x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.0004940775286373538, -0.0012753611140973876, -0.002602322519610641, -0.004678410151307807, -0.007630452949754075, -0.011493625573910392, -0.01620431196540446, -0.02160156333388722, -0.027437146568322655, -0.03339347562061899, -0.03910806748786851, -0.04420261799480297, -0.04831439451306653, -0.05112742535902808, -0.052400947082865613, -0.05199275381928581, -0.0498754641157147, -0.04614425216065162, -0.04101524140108715, -0.034814478931707256, -0.027958142894046616, -0.020925325282838872, -0.014225325020814415, -0.00836183430622286, -0.0037966694538455878, -0.0009157639518578702, 1.3627033096506553e-19],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q5.xy.-x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -0.0011072909722004652, -0.004355772998075805, -0.009530434675820649, -0.016289745246073194, -0.024189576791942807, -0.032714177632169904, -0.04131191066164875, -0.049433127714058764, -0.05656740776468555, -0.06227745332033875, -0.06622720989328827, -0.06820222660494747, -0.0681208763124337, -0.06603575457958466, -0.0621253241141308, -0.05667660737175859, -0.05006039837370359, -0.042701014338795605, -0.03504299683064983, -0.02751737170410559, -0.020510072961802992, -0.014334929347544535, -0.009213221465807494, -0.005261273100821885, -0.0024868866963241214, -0.0007947215146821441, -4.483609179643763e-19],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q5.xy.-x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0004940775286373539, 0.001275361114097388, 0.0026023225196106425, 0.004678410151307808, 0.007630452949754078, 0.011493625573910395, 0.016204311965404464, 0.021601563333887228, 0.027437146568322662, 0.033393475620619, 0.03910806748786852, 0.044202617994802976, 0.04831439451306654, 0.05112742535902809, 0.05240094708286562, 0.051992753819285815, 0.04987546411571471, 0.04614425216065163, 0.04101524140108716, 0.034814478931707256, 0.02795814289404662, 0.020925325282838875, 0.014225325020814417, 0.00836183430622286, 0.003796669453845588, 0.0009157639518578703, -1.3627033096506548e-19],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q5.xy.y180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0009881550572747079, 0.0025507222281947756, 0.005204645039221283, 0.009356820302615615, 0.015260905899508154, 0.022987251147820787, 0.03240862393080893, 0.04320312666777445, 0.05487429313664532, 0.066786951241238, 0.07821613497573704, 0.08840523598960595, 0.09662878902613307, 0.10225485071805618, 0.10480189416573124, 0.10398550763857163, 0.0997509282314294, 0.09228850432130324, 0.0820304828021743, 0.06962895786341451, 0.05591628578809323, 0.041850650565677744, 0.02845065004162883, 0.01672366861244572, 0.0075933389076911755, 0.0018315279037157404, -2.72540661930131e-19],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q5.xy.y180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0022145819444009305, 0.00871154599615161, 0.019060869351641297, 0.03257949049214639, 0.048379153583885615, 0.06542835526433981, 0.0826238213232975, 0.09886625542811753, 0.1131348155293711, 0.12455490664067752, 0.13245441978657654, 0.13640445320989494, 0.1362417526248674, 0.13207150915916932, 0.12425064822826161, 0.1133532147435172, 0.10012079674740719, 0.08540202867759122, 0.07008599366129967, 0.05503474340821118, 0.04102014592360599, 0.02866985869508907, 0.018426442931614988, 0.01052254620164377, 0.004973773392648243, 0.0015894430293642882, 8.967218359287526e-19],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q5.xy.y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0004940775286373539, 0.0012753611140973878, 0.0026023225196106416, 0.0046784101513078075, 0.007630452949754077, 0.011493625573910394, 0.016204311965404464, 0.021601563333887224, 0.02743714656832266, 0.033393475620619, 0.03910806748786852, 0.044202617994802976, 0.04831439451306654, 0.05112742535902809, 0.05240094708286562, 0.051992753819285815, 0.0498754641157147, 0.04614425216065162, 0.04101524140108715, 0.034814478931707256, 0.027958142894046616, 0.020925325282838872, 0.014225325020814415, 0.00836183430622286, 0.0037966694538455878, 0.0009157639518578702, -1.362703309650655e-19],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q5.xy.y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0011072909722004652, 0.004355772998075805, 0.009530434675820649, 0.016289745246073194, 0.024189576791942807, 0.032714177632169904, 0.04131191066164875, 0.049433127714058764, 0.05656740776468555, 0.06227745332033876, 0.06622720989328827, 0.06820222660494747, 0.0681208763124337, 0.06603575457958466, 0.062125324114130805, 0.0566766073717586, 0.050060398373703595, 0.04270101433879561, 0.035042996830649834, 0.02751737170410559, 0.020510072961802996, 0.014334929347544535, 0.009213221465807494, 0.005261273100821885, 0.0024868866963241214, 0.0007947215146821441, 4.483609179643763e-19],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q5.xy.-y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -0.0004940775286373537, -0.0012753611140973874, -0.0026023225196106408, -0.004678410151307806, -0.007630452949754073, -0.01149362557391039, -0.016204311965404457, -0.021601563333887217, -0.027437146568322652, -0.033393475620618986, -0.039108067487868506, -0.04420261799480296, -0.04831439451306652, -0.051127425359028075, -0.05240094708286561, -0.0519927538192858, -0.0498754641157147, -0.04614425216065162, -0.04101524140108715, -0.034814478931707256, -0.027958142894046616, -0.020925325282838872, -0.014225325020814415, -0.00836183430622286, -0.0037966694538455878, -0.0009157639518578702, 1.3627033096506555e-19],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q5.xy.-y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.0011072909722004652, -0.004355772998075805, -0.009530434675820649, -0.016289745246073194, -0.024189576791942807, -0.032714177632169904, -0.04131191066164875, -0.049433127714058764, -0.05656740776468555, -0.06227745332033876, -0.06622720989328827, -0.06820222660494747, -0.0681208763124337, -0.06603575457958466, -0.062125324114130805, -0.0566766073717586, -0.050060398373703595, -0.04270101433879561, -0.035042996830649834, -0.027517371704105596, -0.020510072961802996, -0.014334929347544538, -0.009213221465807497, -0.005261273100821887, -0.0024868866963241223, -0.0007947215146821443, -4.483609179643763e-19],
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
            "sample": 0.09322400929954788,
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
            "samples": [0.0, 0.0030965862409632902, 0.012202535134434653, 0.026777532241581314, 0.0459574166566813, 0.06860636439158399, 0.09338537505908844, 0.1188328381036055, 0.14345221797723479, 0.165801471615384, 0.18457872245410953, 0.19869896782326263, 0.2073571739971564, 0.21007397813527362, 0.20672131336604288, 0.1975265324163361, 0.183054946513302, 0.1641720349362164, 0.1419878322551346, 0.11778708654002776, 0.09294963511338278, 0.06886601234309053, 0.046853552538155784, 0.028078166724460594, 0.013486562710131763, 0.003752971824060207, -0.000756509823369142, -3.497042023007585e-18],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q6.xy.x180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.0054836187524804755, -0.010248295898628797, -0.013630558187597046, -0.015073879714321583, -0.014172458676555621, -0.010704113273629533, -0.004649873863437861, 0.0038012255837528877, 0.014262620544909104, 0.02617534731349305, 0.038846192657757406, 0.0514962949718466, 0.0633168742463143, 0.07352823576097345, 0.08143792111475179, 0.08649389027582073, 0.08832891109186691, 0.08679289041230766, 0.08197066794249444, 0.07418375880873526, 0.06397560988269357, 0.05208105638832378, 0.03938175400856392, 0.026850344052173344, 0.015486918189903847, 0.006251928810969009, 4.751462397063911e-18],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q6.xy.x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0015482931204816451, 0.0061012675672173266, 0.013388766120790657, 0.02297870832834065, 0.034303182195791995, 0.04669268752954422, 0.05941641905180275, 0.07172610898861739, 0.082900735807692, 0.09228936122705476, 0.09934948391163131, 0.1036785869985782, 0.10503698906763681, 0.10336065668302144, 0.09876326620816805, 0.091527473256651, 0.0820860174681082, 0.0709939161275673, 0.05889354327001388, 0.04647481755669139, 0.034433006171545266, 0.023426776269077892, 0.014039083362230297, 0.0067432813550658815, 0.0018764859120301036, -0.000378254911684571, -1.7485210115037923e-18],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q6.xy.x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.0027418093762402377, -0.005124147949314399, -0.006815279093798523, -0.0075369398571607914, -0.007086229338277811, -0.005352056636814767, -0.0023249369317189304, 0.0019006127918764438, 0.007131310272454552, 0.013087673656746525, 0.019423096328878703, 0.0257481474859233, 0.03165843712315715, 0.036764117880486724, 0.040718960557375894, 0.043246945137910366, 0.044164455545933456, 0.04339644520615383, 0.04098533397124722, 0.03709187940436763, 0.03198780494134679, 0.02604052819416189, 0.01969087700428196, 0.013425172026086672, 0.007743459094951923, 0.0031259644054845047, 2.3757311985319556e-18],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q6.xy.-x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -0.0015482931204816447, -0.006101267567217326, -0.013388766120790657, -0.02297870832834065, -0.034303182195791995, -0.04669268752954422, -0.05941641905180275, -0.07172610898861739, -0.082900735807692, -0.09228936122705476, -0.09934948391163131, -0.1036785869985782, -0.10503698906763681, -0.10336065668302144, -0.09876326620816805, -0.091527473256651, -0.0820860174681082, -0.0709939161275673, -0.058893543270013886, -0.046474817556691396, -0.03443300617154527, -0.023426776269077895, -0.014039083362230299, -0.006743281355065883, -0.0018764859120301044, 0.0003782549116845706, 1.748521011503792e-18],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q6.xy.-x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0027418093762402377, 0.0051241479493143996, 0.006815279093798525, 0.007536939857160794, 0.007086229338277815, 0.005352056636814773, 0.0023249369317189378, -0.001900612791876435, -0.007131310272454542, -0.013087673656746512, -0.01942309632887869, -0.025748147485923287, -0.031658437123157135, -0.03676411788048671, -0.04071896055737588, -0.04324694513791035, -0.04416445554593345, -0.04339644520615382, -0.04098533397124721, -0.037091879404367624, -0.03198780494134678, -0.026040528194161888, -0.01969087700428196, -0.013425172026086672, -0.007743459094951923, -0.0031259644054845047, -2.375731198531956e-18],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q6.xy.y180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0054836187524804755, 0.010248295898628797, 0.013630558187597048, 0.015073879714321586, 0.014172458676555625, 0.010704113273629539, 0.004649873863437868, -0.003801225583752879, -0.014262620544909094, -0.02617534731349304, -0.03884619265775739, -0.05149629497184659, -0.06331687424631428, -0.07352823576097343, -0.08143792111475177, -0.08649389027582072, -0.0883289110918669, -0.08679289041230764, -0.08197066794249443, -0.07418375880873526, -0.06397560988269357, -0.05208105638832378, -0.03938175400856392, -0.026850344052173344, -0.015486918189903847, -0.006251928810969009, -4.751462397063911e-18],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q6.xy.y180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.00309658624096329, 0.012202535134434653, 0.026777532241581314, 0.0459574166566813, 0.06860636439158399, 0.09338537505908844, 0.1188328381036055, 0.14345221797723479, 0.165801471615384, 0.18457872245410953, 0.19869896782326263, 0.2073571739971564, 0.21007397813527362, 0.20672131336604288, 0.1975265324163361, 0.183054946513302, 0.1641720349362164, 0.1419878322551346, 0.11778708654002776, 0.09294963511338278, 0.06886601234309053, 0.046853552538155784, 0.028078166724460597, 0.013486562710131765, 0.003752971824060208, -0.0007565098233691416, -3.497042023007585e-18],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q6.xy.y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0027418093762402377, 0.005124147949314399, 0.006815279093798524, 0.007536939857160793, 0.007086229338277812, 0.005352056636814769, 0.002324936931718934, -0.0019006127918764395, -0.007131310272454547, -0.01308767365674652, -0.019423096328878696, -0.025748147485923294, -0.03165843712315714, -0.03676411788048672, -0.04071896055737589, -0.04324694513791036, -0.04416445554593345, -0.04339644520615382, -0.04098533397124721, -0.03709187940436763, -0.03198780494134679, -0.02604052819416189, -0.01969087700428196, -0.013425172026086672, -0.007743459094951923, -0.0031259644054845047, -2.3757311985319556e-18],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q6.xy.y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.001548293120481645, 0.0061012675672173266, 0.013388766120790657, 0.02297870832834065, 0.034303182195791995, 0.04669268752954422, 0.05941641905180275, 0.07172610898861739, 0.082900735807692, 0.09228936122705476, 0.09934948391163131, 0.1036785869985782, 0.10503698906763681, 0.10336065668302144, 0.09876326620816805, 0.091527473256651, 0.0820860174681082, 0.0709939161275673, 0.05889354327001388, 0.04647481755669139, 0.034433006171545266, 0.023426776269077892, 0.014039083362230299, 0.006743281355065882, 0.001876485912030104, -0.0003782549116845708, -1.7485210115037923e-18],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q6.xy.-y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -0.0027418093762402377, -0.005124147949314399, -0.006815279093798522, -0.00753693985716079, -0.007086229338277809, -0.005352056636814764, -0.002324936931718927, 0.0019006127918764482, 0.007131310272454557, 0.01308767365674653, 0.01942309632887871, 0.025748147485923308, 0.031658437123157156, 0.03676411788048673, 0.0407189605573759, 0.04324694513791037, 0.04416445554593346, 0.043396445206153836, 0.04098533397124723, 0.03709187940436763, 0.03198780494134679, 0.02604052819416189, 0.01969087700428196, 0.013425172026086672, 0.007743459094951923, 0.0031259644054845047, 2.3757311985319556e-18],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q6.xy.-y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.0015482931204816453, -0.0061012675672173266, -0.013388766120790657, -0.02297870832834065, -0.034303182195791995, -0.04669268752954422, -0.05941641905180275, -0.07172610898861739, -0.082900735807692, -0.09228936122705476, -0.09934948391163131, -0.1036785869985782, -0.10503698906763681, -0.10336065668302144, -0.09876326620816805, -0.091527473256651, -0.0820860174681082, -0.0709939161275673, -0.05889354327001388, -0.04647481755669139, -0.034433006171545266, -0.023426776269077892, -0.014039083362230295, -0.006743281355065881, -0.0018764859120301031, 0.0003782549116845712, 1.7485210115037923e-18],
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
            "sample": 0.09586708553446507,
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
            "samples": [0.0, 0.0006111507311347972, 0.0024043824972849346, 0.005261828068419316, 0.008996151598091794, 0.01336351431849177, 0.01808038314363127, 0.022842960300863947, 0.027347826179509697, 0.03131230673148022, 0.03449310675505968, 0.036701888627180844, 0.03781671173591753, 0.037788562877863946, 0.03664257815093054, 0.0344739542133999, 0.031438941065012604, 0.027741669952818546, 0.023617871446307143, 0.019316757675127402, 0.015082463072673417, 0.011136451207145381, 0.007662201116357545, 0.004793292919282823, 0.002605734867066953, 0.0011150343024962388, 0.00027813977658454076, 4.362284073217507e-20],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q7.xy.x180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -7.140266213968797e-05, -0.00030305476564477835, -0.0008396348285968095, -0.0017959836520728878, -0.0032453419219738854, -0.005211092845650111, -0.0076627306475489975, -0.010516437590361182, -0.013640282115013775, -0.016863677669417907, -0.019990395083063817, -0.02281412823221524, -0.025135396429880257, -0.0267784447740055, -0.027606785658708086, -0.027536112817346484, -0.02654350742428085, -0.024672129972282023, -0.0220309311935979, -0.01878929439721397, -0.015166911280064943, -0.011419563616160871, -0.007821805663931819, -0.0046477916336201824, -0.002151649573812355, -0.0005488550090950498, 1.6059070921146568e-20],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q7.xy.x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0003055753655673986, 0.0012021912486424673, 0.002630914034209658, 0.004498075799045897, 0.006681757159245885, 0.009040191571815634, 0.011421480150431974, 0.013673913089754849, 0.01565615336574011, 0.01724655337752984, 0.018350944313590422, 0.018908355867958766, 0.018894281438931973, 0.01832128907546527, 0.01723697710669995, 0.015719470532506302, 0.013870834976409273, 0.011808935723153571, 0.009658378837563701, 0.007541231536336708, 0.0055682256035726905, 0.0038311005581787723, 0.0023966464596414114, 0.0013028674335334766, 0.0005575171512481194, 0.00013906988829227038, 2.1811420366087536e-20],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q7.xy.x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -3.570133106984399e-05, -0.00015152738282238917, -0.00041981741429840473, -0.0008979918260364439, -0.0016226709609869427, -0.0026055464228250556, -0.0038313653237744987, -0.005258218795180591, -0.006820141057506887, -0.008431838834708954, -0.009995197541531909, -0.01140706411610762, -0.012567698214940129, -0.01338922238700275, -0.013803392829354043, -0.013768056408673242, -0.013271753712140425, -0.012336064986141012, -0.01101546559679895, -0.009394647198606986, -0.007583455640032472, -0.005709781808080436, -0.003910902831965909, -0.0023238958168100912, -0.0010758247869061776, -0.0002744275045475249, 8.029535460573284e-21],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q7.xy.-x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -0.0003055753655673986, -0.0012021912486424673, -0.002630914034209658, -0.004498075799045897, -0.006681757159245885, -0.009040191571815634, -0.011421480150431974, -0.013673913089754849, -0.01565615336574011, -0.01724655337752984, -0.018350944313590422, -0.018908355867958766, -0.018894281438931973, -0.01832128907546527, -0.01723697710669995, -0.015719470532506302, -0.013870834976409271, -0.01180893572315357, -0.0096583788375637, -0.0075412315363367075, -0.00556822560357269, -0.0038311005581787715, -0.002396646459641411, -0.0013028674335334764, -0.0005575171512481193, -0.00013906988829227035, -2.1811420366087536e-20],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q7.xy.-x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 3.570133106984403e-05, 0.0001515273828223893, 0.00041981741429840505, 0.0008979918260364444, 0.0016226709609869436, 0.002605546422825057, 0.0038313653237745, 0.005258218795180593, 0.006820141057506889, 0.008431838834708955, 0.00999519754153191, 0.011407064116107622, 0.01256769821494013, 0.013389222387002752, 0.013803392829354045, 0.013768056408673244, 0.013271753712140427, 0.012336064986141013, 0.011015465596798953, 0.009394647198606988, 0.0075834556400324726, 0.0057097818080804365, 0.003910902831965909, 0.0023238958168100912, 0.0010758247869061776, 0.0002744275045475249, -8.029535460573281e-21],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q7.xy.y180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 7.140266213968801e-05, 0.0003030547656447785, 0.0008396348285968098, 0.0017959836520728884, 0.0032453419219738862, 0.005211092845650112, 0.007662730647548999, 0.010516437590361184, 0.013640282115013776, 0.01686367766941791, 0.01999039508306382, 0.022814128232215243, 0.02513539642988026, 0.026778444774005504, 0.02760678565870809, 0.027536112817346487, 0.02654350742428085, 0.024672129972282023, 0.0220309311935979, 0.01878929439721397, 0.015166911280064943, 0.011419563616160871, 0.007821805663931819, 0.0046477916336201824, 0.002151649573812355, 0.0005488550090950498, -1.6059070921146565e-20],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q7.xy.y180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0006111507311347972, 0.0024043824972849346, 0.005261828068419316, 0.008996151598091794, 0.01336351431849177, 0.01808038314363127, 0.022842960300863947, 0.027347826179509697, 0.03131230673148022, 0.03449310675505968, 0.036701888627180844, 0.03781671173591753, 0.037788562877863946, 0.03664257815093054, 0.0344739542133999, 0.031438941065012604, 0.027741669952818546, 0.023617871446307143, 0.019316757675127402, 0.015082463072673415, 0.01113645120714538, 0.007662201116357544, 0.004793292919282822, 0.0026057348670669527, 0.0011150343024962386, 0.0002781397765845407, 4.362284073217507e-20],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q7.xy.y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 3.570133106984401e-05, 0.00015152738282238925, 0.0004198174142984049, 0.0008979918260364442, 0.0016226709609869431, 0.002605546422825056, 0.0038313653237744996, 0.005258218795180592, 0.006820141057506888, 0.008431838834708955, 0.00999519754153191, 0.011407064116107622, 0.01256769821494013, 0.013389222387002752, 0.013803392829354045, 0.013768056408673244, 0.013271753712140425, 0.012336064986141012, 0.01101546559679895, 0.009394647198606986, 0.007583455640032472, 0.005709781808080436, 0.003910902831965909, 0.0023238958168100912, 0.0010758247869061776, 0.0002744275045475249, -8.029535460573283e-21],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q7.xy.y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0003055753655673986, 0.0012021912486424673, 0.002630914034209658, 0.004498075799045897, 0.006681757159245885, 0.009040191571815634, 0.011421480150431974, 0.013673913089754849, 0.01565615336574011, 0.01724655337752984, 0.018350944313590422, 0.018908355867958766, 0.018894281438931973, 0.01832128907546527, 0.01723697710669995, 0.015719470532506302, 0.013870834976409273, 0.011808935723153571, 0.009658378837563701, 0.0075412315363367075, 0.00556822560357269, 0.003831100558178772, 0.002396646459641411, 0.0013028674335334764, 0.0005575171512481193, 0.00013906988829227035, 2.1811420366087536e-20],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q7.xy.-y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -3.5701331069843966e-05, -0.0001515273828223891, -0.00041981741429840457, -0.0008979918260364436, -0.0016226709609869423, -0.002605546422825055, -0.003831365323774498, -0.00525821879518059, -0.0068201410575068865, -0.008431838834708952, -0.009995197541531907, -0.011407064116107618, -0.012567698214940127, -0.013389222387002749, -0.013803392829354041, -0.01376805640867324, -0.013271753712140425, -0.012336064986141012, -0.01101546559679895, -0.009394647198606986, -0.007583455640032472, -0.005709781808080436, -0.003910902831965909, -0.0023238958168100912, -0.0010758247869061776, -0.0002744275045475249, 8.029535460573286e-21],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q7.xy.-y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.0003055753655673986, -0.0012021912486424673, -0.002630914034209658, -0.004498075799045897, -0.006681757159245885, -0.009040191571815634, -0.011421480150431974, -0.013673913089754849, -0.01565615336574011, -0.01724655337752984, -0.018350944313590422, -0.018908355867958766, -0.018894281438931973, -0.01832128907546527, -0.01723697710669995, -0.015719470532506302, -0.013870834976409273, -0.011808935723153571, -0.009658378837563701, -0.007541231536336709, -0.005568225603572691, -0.0038311005581787728, -0.002396646459641412, -0.0013028674335334768, -0.0005575171512481195, -0.0001390698882922704, -2.1811420366087536e-20],
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
            "sample": 0.053928929583904925,
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
            "samples": [0.0, 0.00463001615930933, 0.018247383444917428, 0.04005040112564875, 0.06875637737675126, 0.1026784052326451, 0.13982619259534596, 0.1780247890942569, 0.2150439710783139, 0.24873041335404655, 0.27713463088982093, 0.2986250234557166, 0.3119821779287401, 0.3164678241520553, 0.3118644220811366, 0.29848318068755786, 0.2771402581970707, 0.24910284671355223, 0.216008680364199, 0.17976411094722797, 0.14242716988603296, 0.1060829025387238, 0.07271866905639778, 0.044107032667613864, 0.021703309562083502, 0.006563872287682304, -0.0007100541984628345, -4.8629040688787815e-18],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q8.xy.x180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.00796112679719496, -0.01488957041978051, -0.019831952615434606, -0.021987828088880015, -0.020772350144276842, -0.015863444809666536, -0.007230034675605405, 0.0048608342409090935, 0.01985864418443848, 0.03696499854776062, 0.055187848979409655, 0.0734107295650413, 0.09047229069182314, 0.10525065960154636, 0.1167467575869685, 0.12416070471514916, 0.12695584474642252, 0.12490570156496603, 0.11812028454927229, 0.10704952223957019, 0.0924631321441131, 0.0754078285213268, 0.05714432328148112, 0.03906798342528813, 0.022618176108219833, 0.009182179074257148, 7.048338519495266e-18],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q8.xy.x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0014200227136768107, 0.005596459723980372, 0.012283429978087231, 0.021087532791610325, 0.03149139497954109, 0.04288459534922199, 0.05460007814510073, 0.06595383533521346, 0.07628544359068848, 0.08499699721754096, 0.09158808556785797, 0.0956847154907679, 0.09706046004617704, 0.0956485998547719, 0.09154458249019563, 0.08499872310873369, 0.07639966864123517, 0.06624971099761201, 0.055133526939366226, 0.04368231326282082, 0.03253555191915843, 0.02230276487497956, 0.013527596031163719, 0.006656389843942803, 0.002013135033976438, -0.00021777312542019644, -1.4914492724512114e-18],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q8.xy.x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.0024416720135517524, -0.0045666208206350456, -0.006082445978910004, -0.006743651476864012, -0.006370865242448973, -0.00486530741401242, -0.0022174465718413712, 0.0014908144576624004, 0.006090632264431482, 0.01133713916814507, 0.016926074634136406, 0.02251501934833309, 0.0277477881977683, 0.03228030359314279, 0.03580614879459643, 0.03808000118684943, 0.03893726867701464, 0.03830849119896969, 0.03622740855205911, 0.03283201350448778, 0.02835837787700666, 0.02312752819966477, 0.017526123932469936, 0.011982123157370149, 0.006936978772965125, 0.0028161678918282875, 2.1617204880035448e-18],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q8.xy.-x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -0.0014200227136768105, -0.005596459723980371, -0.012283429978087231, -0.021087532791610325, -0.03149139497954109, -0.04288459534922199, -0.05460007814510073, -0.06595383533521346, -0.07628544359068848, -0.08499699721754096, -0.09158808556785797, -0.0956847154907679, -0.09706046004617704, -0.0956485998547719, -0.09154458249019563, -0.08499872310873369, -0.07639966864123517, -0.06624971099761201, -0.05513352693936623, -0.04368231326282083, -0.03253555191915844, -0.022302764874979564, -0.01352759603116372, -0.006656389843942805, -0.002013135033976439, 0.00021777312542019608, 1.4914492724512112e-18],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q8.xy.-x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0024416720135517524, 0.004566620820635046, 0.006082445978910006, 0.006743651476864014, 0.0063708652424489766, 0.004865307414012425, 0.0022174465718413777, -0.0014908144576623924, -0.006090632264431473, -0.01133713916814506, -0.016926074634136395, -0.02251501934833308, -0.02774778819776829, -0.032280303593142774, -0.03580614879459642, -0.03808000118684941, -0.038937268677014636, -0.03830849119896968, -0.0362274085520591, -0.03283201350448777, -0.028358377877006655, -0.023127528199664765, -0.017526123932469936, -0.011982123157370149, -0.006936978772965125, -0.0028161678918282875, -2.1617204880035448e-18],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q8.xy.y180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.00796112679719496, 0.014889570419780512, 0.01983195261543461, 0.02198782808888002, 0.02077235014427685, 0.015863444809666543, 0.007230034675605416, -0.0048608342409090805, -0.019858644184438466, -0.03696499854776061, -0.055187848979409634, -0.07341072956504129, -0.09047229069182312, -0.10525065960154635, -0.11674675758696848, -0.12416070471514914, -0.1269558447464225, -0.12490570156496601, -0.11812028454927227, -0.10704952223957018, -0.0924631321441131, -0.0754078285213268, -0.05714432328148112, -0.03906798342528813, -0.022618176108219833, -0.009182179074257148, -7.048338519495266e-18],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q8.xy.y180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0046300161593093294, 0.018247383444917428, 0.04005040112564875, 0.06875637737675126, 0.1026784052326451, 0.13982619259534596, 0.1780247890942569, 0.2150439710783139, 0.24873041335404655, 0.27713463088982093, 0.2986250234557166, 0.3119821779287401, 0.3164678241520553, 0.3118644220811366, 0.29848318068755786, 0.2771402581970707, 0.24910284671355223, 0.216008680364199, 0.17976411094722797, 0.14242716988603296, 0.1060829025387238, 0.07271866905639778, 0.04410703266761387, 0.021703309562083505, 0.006563872287682306, -0.000710054198462834, -4.862904068878781e-18],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q8.xy.y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0024416720135517524, 0.0045666208206350456, 0.006082445978910005, 0.0067436514768640125, 0.006370865242448975, 0.004865307414012423, 0.0022174465718413747, -0.0014908144576623963, -0.006090632264431478, -0.011337139168145065, -0.0169260746341364, -0.022515019348333082, -0.027747788197768294, -0.03228030359314278, -0.035806148794596426, -0.03808000118684942, -0.038937268677014636, -0.03830849119896968, -0.03622740855205911, -0.03283201350448778, -0.028358377877006655, -0.02312752819966477, -0.017526123932469936, -0.011982123157370149, -0.006936978772965125, -0.0028161678918282875, -2.1617204880035448e-18],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q8.xy.y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0014200227136768105, 0.005596459723980372, 0.012283429978087231, 0.021087532791610325, 0.03149139497954109, 0.04288459534922199, 0.05460007814510073, 0.06595383533521346, 0.07628544359068848, 0.08499699721754096, 0.09158808556785797, 0.0956847154907679, 0.09706046004617704, 0.0956485998547719, 0.09154458249019563, 0.08499872310873369, 0.07639966864123517, 0.06624971099761201, 0.055133526939366226, 0.04368231326282082, 0.03253555191915843, 0.02230276487497956, 0.01352759603116372, 0.006656389843942804, 0.0020131350339764385, -0.00021777312542019627, -1.4914492724512112e-18],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q8.xy.-y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -0.0024416720135517524, -0.0045666208206350456, -0.006082445978910003, -0.006743651476864011, -0.006370865242448971, -0.004865307414012417, -0.0022174465718413677, 0.0014908144576624045, 0.006090632264431487, 0.011337139168145076, 0.016926074634136413, 0.022515019348333096, 0.027747788197768308, 0.032280303593142795, 0.03580614879459644, 0.038080001186849434, 0.03893726867701465, 0.038308491198969695, 0.03622740855205911, 0.03283201350448778, 0.028358377877006662, 0.02312752819966477, 0.017526123932469936, 0.011982123157370149, 0.006936978772965125, 0.0028161678918282875, 2.1617204880035448e-18],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q8.xy.-y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.001420022713676811, -0.005596459723980372, -0.012283429978087231, -0.021087532791610325, -0.03149139497954109, -0.04288459534922199, -0.05460007814510073, -0.06595383533521346, -0.07628544359068848, -0.08499699721754096, -0.09158808556785797, -0.0956847154907679, -0.09706046004617704, -0.0956485998547719, -0.09154458249019563, -0.08499872310873369, -0.07639966864123517, -0.06624971099761201, -0.055133526939366226, -0.04368231326282082, -0.03253555191915843, -0.02230276487497956, -0.013527596031163717, -0.006656389843942802, -0.0020131350339764376, 0.0002177731254201966, 1.4914492724512116e-18],
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
            "sample": 0.06763223593964335,
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
            "cosine": [(-0.3708905196588253, 2000)],
            "sine": [(0.9286765973293429, 2000)],
        },
        "q1.resonator.readout.iw2": {
            "cosine": [(-0.9286765973293429, 2000)],
            "sine": [(-0.3708905196588253, 2000)],
        },
        "q1.resonator.readout.iw3": {
            "cosine": [(0.9286765973293429, 2000)],
            "sine": [(0.3708905196588253, 2000)],
        },
        "q2.resonator.readout.iw1": {
            "cosine": [(-0.9925240821469165, 2000)],
            "sine": [(0.12204895066497343, 2000)],
        },
        "q2.resonator.readout.iw2": {
            "cosine": [(-0.12204895066497343, 2000)],
            "sine": [(-0.9925240821469165, 2000)],
        },
        "q2.resonator.readout.iw3": {
            "cosine": [(0.12204895066497343, 2000)],
            "sine": [(0.9925240821469165, 2000)],
        },
        "q3.resonator.readout.iw1": {
            "cosine": [(-0.670151037903351, 2000)],
            "sine": [(-0.7422247546377455, 2000)],
        },
        "q3.resonator.readout.iw2": {
            "cosine": [(0.7422247546377455, 2000)],
            "sine": [(-0.670151037903351, 2000)],
        },
        "q3.resonator.readout.iw3": {
            "cosine": [(-0.7422247546377455, 2000)],
            "sine": [(0.670151037903351, 2000)],
        },
        "q4.resonator.readout.iw1": {
            "cosine": [(-0.4484474924845168, 2000)],
            "sine": [(-0.8938091778922105, 2000)],
        },
        "q4.resonator.readout.iw2": {
            "cosine": [(0.8938091778922105, 2000)],
            "sine": [(-0.4484474924845168, 2000)],
        },
        "q4.resonator.readout.iw3": {
            "cosine": [(-0.8938091778922105, 2000)],
            "sine": [(0.4484474924845168, 2000)],
        },
        "q5.resonator.readout.iw1": {
            "cosine": [(0.9597091748147896, 2000)],
            "sine": [(0.28099519529044564, 2000)],
        },
        "q5.resonator.readout.iw2": {
            "cosine": [(-0.28099519529044564, 2000)],
            "sine": [(0.9597091748147896, 2000)],
        },
        "q5.resonator.readout.iw3": {
            "cosine": [(0.28099519529044564, 2000)],
            "sine": [(-0.9597091748147896, 2000)],
        },
        "q6.resonator.readout.iw1": {
            "cosine": [(-0.8182412482737133, 2000)],
            "sine": [(0.5748749947801484, 2000)],
        },
        "q6.resonator.readout.iw2": {
            "cosine": [(-0.5748749947801484, 2000)],
            "sine": [(-0.8182412482737133, 2000)],
        },
        "q6.resonator.readout.iw3": {
            "cosine": [(0.5748749947801484, 2000)],
            "sine": [(0.8182412482737133, 2000)],
        },
        "q7.resonator.readout.iw1": {
            "cosine": [(-0.9999526806088935, 2000)],
            "sine": [(-0.00972813153119021, 2000)],
        },
        "q7.resonator.readout.iw2": {
            "cosine": [(0.00972813153119021, 2000)],
            "sine": [(-0.9999526806088935, 2000)],
        },
        "q7.resonator.readout.iw3": {
            "cosine": [(-0.00972813153119021, 2000)],
            "sine": [(0.9999526806088935, 2000)],
        },
        "q8.resonator.readout.iw1": {
            "cosine": [(0.567637767708887, 2000)],
            "sine": [(0.8232784247570634, 2000)],
        },
        "q8.resonator.readout.iw2": {
            "cosine": [(-0.8232784247570634, 2000)],
            "sine": [(0.567637767708887, 2000)],
        },
        "q8.resonator.readout.iw3": {
            "cosine": [(0.8232784247570634, 2000)],
            "sine": [(-0.567637767708887, 2000)],
        },
    },
    "mixers": {},
}


