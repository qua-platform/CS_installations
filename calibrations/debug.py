
# Single QUA script generated at 2024-07-09 15:29:29.442311
# QUA library version: 1.2.0

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
    v14 = declare(bool, )
    a1 = declare(bool, value=[True, False])
    align()
    set_dc_offset("q1.z", "single", 0.0)
    set_dc_offset("q2.z", "single", 0.0182)
    set_dc_offset("q3.z", "single", 0.0024)
    set_dc_offset("q4.z", "single", 0.0029)
    set_dc_offset("q5.z", "single", 0.0237)
    align()
    with for_(v1,0,(v1<1),(v1+1)):
        r1 = declare_stream()
        save(v1, r1)
        set_dc_offset("coupler_q4_q5", "single", 0)
        wait(100, )
        with for_(v12,0.0,(v12<2.975),(v12+0.05)):
            with for_(v13,0.9999,(v13<1.0001041666666666),(v13+8.333333333387927e-06)):
                with for_each_((v14),(a1)):
                    play("x180", "q4.xy", condition=v14)
                    align()
                    play("x90", "q5.xy")
                    align()
                    wait(5, )
                    play("const", "q4.z")
                    play("const"*amp(v13), "coupler_q4_q5")
                    play("const"*amp(v13), "coupler_q4_q5")
                    wait(10, "q5.z")
                    align()
                    set_dc_offset("coupler_q4_q5", "single", 0)
                    set_dc_offset("q4.z", "single", 0.0029)
                    set_dc_offset("q5.z", "single", 0.0237)
                    wait(5, )
                    align()
                    frame_rotation_2pi(v12, "q5.xy")
                    play("x90", "q5.xy")
                    align()
                    wait(4, )
                    measure("readout"*amp(1.0), "q1.resonator", None, dual_demod.full("iw1", "iw2", v2), dual_demod.full("iw3", "iw1", v7))
                    r2 = declare_stream()
                    save(v2, r2)
                    r7 = declare_stream()
                    save(v7, r7)
                    measure("readout"*amp(1.0), "q2.resonator", None, dual_demod.full("iw1", "iw2", v3), dual_demod.full("iw3", "iw1", v8))
                    r3 = declare_stream()
                    save(v3, r3)
                    r8 = declare_stream()
                    save(v8, r8)
                    measure("readout"*amp(1.0), "q3.resonator", None, dual_demod.full("iw1", "iw2", v4), dual_demod.full("iw3", "iw1", v9))
                    r4 = declare_stream()
                    save(v4, r4)
                    r9 = declare_stream()
                    save(v9, r9)
                    measure("readout"*amp(1.0), "q4.resonator", None, dual_demod.full("iw1", "iw2", v5), dual_demod.full("iw3", "iw1", v10))
                    r5 = declare_stream()
                    save(v5, r5)
                    r10 = declare_stream()
                    save(v10, r10)
                    measure("readout"*amp(1.0), "q5.resonator", None, dual_demod.full("iw1", "iw2", v6), dual_demod.full("iw3", "iw1", v11))
                    r6 = declare_stream()
                    save(v6, r6)
                    r11 = declare_stream()
                    save(v11, r11)
                    wait(7, )
    with stream_processing():
        r1.save("n")
        r6.buffer(60, 25, 2).average().save("I1")
        r11.buffer(60, 25, 2).average().save("Q1")
        r5.buffer(60, 25, 2).average().save("I2")
        r5.buffer(60, 25, 2).average().save("Q2")


config = {
    "version": 1,
    "controllers": {
        "con1": {
            "fems": {
                "1": {
                    "type": "LF",
                    "analog_outputs": {
                        "3": {
                            "delay": 0,
                            "shareable": False,
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "mw",
                            "output_mode": "direct",
                            "offset": 0.0,
                        },
                        "4": {
                            "delay": 0,
                            "shareable": False,
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "mw",
                            "output_mode": "direct",
                            "offset": 0.0,
                        },
                        "1": {
                            "delay": 0,
                            "shareable": False,
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "mw",
                            "output_mode": "direct",
                            "offset": 0.0,
                        },
                        "2": {
                            "delay": 0,
                            "shareable": False,
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "mw",
                            "output_mode": "direct",
                            "offset": 0.0,
                        },
                        "5": {
                            "delay": 0,
                            "shareable": False,
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "mw",
                            "output_mode": "direct",
                            "offset": 0.0,
                        },
                        "6": {
                            "delay": 0,
                            "shareable": False,
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "mw",
                            "output_mode": "direct",
                            "offset": 0.0,
                        },
                        "7": {
                            "delay": 0,
                            "shareable": False,
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "mw",
                            "output_mode": "direct",
                            "offset": 0.0,
                        },
                        "8": {
                            "delay": 0,
                            "shareable": False,
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "mw",
                            "output_mode": "direct",
                            "offset": 0.0,
                        },
                    },
                    "analog_inputs": {
                        "1": {
                            "gain_db": 0,
                            "shareable": False,
                            "sampling_rate": 1000000000.0,
                            "offset": 0.0,
                        },
                        "2": {
                            "gain_db": 0,
                            "shareable": False,
                            "sampling_rate": 1000000000.0,
                            "offset": 0.0,
                        },
                    },
                    "digital_outputs": {
                        "3": {
                            "inverted": False,
                            "shareable": False,
                            "level": "LVTTL",
                        },
                        "1": {
                            "inverted": False,
                            "shareable": False,
                            "level": "LVTTL",
                        },
                        "5": {
                            "inverted": False,
                            "shareable": False,
                            "level": "LVTTL",
                        },
                        "7": {
                            "inverted": False,
                            "shareable": False,
                            "level": "LVTTL",
                        },
                    },
                },
                "2": {
                    "type": "LF",
                    "analog_outputs": {
                        "5": {
                            "delay": 0,
                            "shareable": False,
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "pulse",
                            "output_mode": "amplified",
                            "offset": 0.0,
                        },
                        "1": {
                            "delay": 0,
                            "shareable": False,
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "mw",
                            "output_mode": "direct",
                            "offset": 0.0,
                        },
                        "2": {
                            "delay": 0,
                            "shareable": False,
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "mw",
                            "output_mode": "direct",
                            "offset": 0.0,
                        },
                        "3": {
                            "delay": 0,
                            "shareable": False,
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "mw",
                            "output_mode": "direct",
                            "offset": 0.0,
                        },
                        "4": {
                            "delay": 0,
                            "shareable": False,
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "mw",
                            "output_mode": "direct",
                            "offset": 0.0,
                        },
                    },
                    "analog_inputs": {
                        "1": {
                            "gain_db": 0,
                            "shareable": False,
                            "sampling_rate": 1000000000.0,
                            "offset": 0.0,
                        },
                        "2": {
                            "gain_db": 0,
                            "shareable": False,
                            "sampling_rate": 1000000000.0,
                            "offset": 0.0,
                        },
                    },
                    "digital_outputs": {
                        "1": {
                            "inverted": False,
                            "shareable": False,
                            "level": "LVTTL",
                        },
                        "3": {
                            "inverted": False,
                            "shareable": False,
                            "level": "LVTTL",
                        },
                    },
                },
                "3": {
                    "type": "LF",
                    "analog_outputs": {
                        "1": {
                            "delay": 0,
                            "shareable": False,
                            "crosstalk": {8: 0.408},
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "pulse",
                            "output_mode": "amplified",
                            "offset": 0.0,
                        },
                        "2": {
                            "delay": 0,
                            "shareable": False,
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "pulse",
                            "output_mode": "amplified",
                            "offset": 0.0,
                        },
                        "3": {
                            "delay": 0,
                            "shareable": False,
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "pulse",
                            "output_mode": "amplified",
                            "offset": 0.0,
                        },
                        "4": {
                            "delay": 0,
                            "shareable": False,
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "pulse",
                            "output_mode": "amplified",
                            "offset": 0.0,
                        },
                        "5": {
                            "delay": 0,
                            "shareable": False,
                            "crosstalk": {8: 0.427, 1: 0.374},
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "pulse",
                            "output_mode": "amplified",
                            "offset": 0.0,
                        },
                        "6": {
                            "delay": 0,
                            "shareable": False,
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "pulse",
                            "output_mode": "amplified",
                            "offset": 0.0,
                        },
                        "7": {
                            "delay": 0,
                            "shareable": False,
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "pulse",
                            "output_mode": "amplified",
                            "offset": 0.0,
                        },
                        "8": {
                            "delay": 0,
                            "shareable": False,
                            "crosstalk": {1: 0.177},
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "pulse",
                            "output_mode": "amplified",
                            "offset": 0.0,
                        },
                    },
                },
            },
        },
    },
    "elements": {
        "q1.xy": {
            "operations": {
                "x180_DragGaussian": "q1.xy.x180_DragGaussian.pulse",
                "x90_DragGaussian": "q1.xy.x90_DragGaussian.pulse",
                "-x90_DragGaussian": "q1.xy.-x90_DragGaussian.pulse",
                "y180_DragGaussian": "q1.xy.y180_DragGaussian.pulse",
                "y90_DragGaussian": "q1.xy.y90_DragGaussian.pulse",
                "-y90_DragGaussian": "q1.xy.-y90_DragGaussian.pulse",
                "x180_Square": "q1.xy.x180_Square.pulse",
                "x90_Square": "q1.xy.x90_Square.pulse",
                "-x90_Square": "q1.xy.-x90_Square.pulse",
                "y180_Square": "q1.xy.y180_Square.pulse",
                "y90_Square": "q1.xy.y90_Square.pulse",
                "-y90_Square": "q1.xy.-y90_Square.pulse",
                "x180": "q1.xy.x180_DragGaussian.pulse",
                "x90": "q1.xy.x90_DragGaussian.pulse",
                "-x90": "q1.xy.-x90_DragGaussian.pulse",
                "y180": "q1.xy.y180_DragGaussian.pulse",
                "y90": "q1.xy.y90_DragGaussian.pulse",
                "-y90": "q1.xy.-y90_DragGaussian.pulse",
                "saturation": "q1.xy.saturation.pulse",
            },
            "digitalInputs": {
                "octave_switch": {
                    "port": ('con1', 1, 3),
                    "delay": 87,
                    "buffer": 15,
                },
            },
            "intermediate_frequency": 385991173.03796864,
            "RF_inputs": {
                "port": ('octave1', 2),
            },
        },
        "q1.z": {
            "operations": {
                "const": "q1.z.const.pulse",
            },
            "singleInput": {
                "port": ('con1', 2, 5),
            },
        },
        "q1.resonator": {
            "operations": {
                "readout": "q1.resonator.readout.pulse",
                "const": "q1.resonator.const.pulse",
            },
            "digitalInputs": {
                "octave_switch": {
                    "port": ('con1', 1, 1),
                    "delay": 87,
                    "buffer": 15,
                },
            },
            "smearing": 0,
            "time_of_flight": 264,
            "RF_outputs": {
                "port": ('octave1', 1),
            },
            "intermediate_frequency": -287531678,
            "RF_inputs": {
                "port": ('octave1', 1),
            },
        },
        "q2.xy": {
            "operations": {
                "x180_DragGaussian": "q2.xy.x180_DragGaussian.pulse",
                "x90_DragGaussian": "q2.xy.x90_DragGaussian.pulse",
                "-x90_DragGaussian": "q2.xy.-x90_DragGaussian.pulse",
                "y180_DragGaussian": "q2.xy.y180_DragGaussian.pulse",
                "y90_DragGaussian": "q2.xy.y90_DragGaussian.pulse",
                "-y90_DragGaussian": "q2.xy.-y90_DragGaussian.pulse",
                "x180_Square": "q2.xy.x180_Square.pulse",
                "x90_Square": "q2.xy.x90_Square.pulse",
                "-x90_Square": "q2.xy.-x90_Square.pulse",
                "y180_Square": "q2.xy.y180_Square.pulse",
                "y90_Square": "q2.xy.y90_Square.pulse",
                "-y90_Square": "q2.xy.-y90_Square.pulse",
                "x180": "q2.xy.x180_DragGaussian.pulse",
                "x90": "q2.xy.x90_DragGaussian.pulse",
                "-x90": "q2.xy.-x90_DragGaussian.pulse",
                "y180": "q2.xy.y180_DragGaussian.pulse",
                "y90": "q2.xy.y90_DragGaussian.pulse",
                "-y90": "q2.xy.-y90_DragGaussian.pulse",
                "saturation": "q2.xy.saturation.pulse",
            },
            "digitalInputs": {
                "octave_switch": {
                    "port": ('con1', 1, 5),
                    "delay": 87,
                    "buffer": 15,
                },
            },
            "intermediate_frequency": -264564380.79657173,
            "RF_inputs": {
                "port": ('octave1', 3),
            },
        },
        "q2.z": {
            "operations": {
                "const": "q2.z.const.pulse",
            },
            "singleInput": {
                "port": ('con1', 3, 6),
            },
        },
        "q2.resonator": {
            "operations": {
                "readout": "q2.resonator.readout.pulse",
                "const": "q2.resonator.const.pulse",
            },
            "digitalInputs": {
                "octave_switch": {
                    "port": ('con1', 1, 1),
                    "delay": 87,
                    "buffer": 15,
                },
            },
            "smearing": 0,
            "time_of_flight": 264,
            "RF_outputs": {
                "port": ('octave1', 1),
            },
            "intermediate_frequency": -185741282,
            "RF_inputs": {
                "port": ('octave1', 1),
            },
        },
        "q3.xy": {
            "operations": {
                "x180_DragGaussian": "q3.xy.x180_DragGaussian.pulse",
                "x90_DragGaussian": "q3.xy.x90_DragGaussian.pulse",
                "-x90_DragGaussian": "q3.xy.-x90_DragGaussian.pulse",
                "y180_DragGaussian": "q3.xy.y180_DragGaussian.pulse",
                "y90_DragGaussian": "q3.xy.y90_DragGaussian.pulse",
                "-y90_DragGaussian": "q3.xy.-y90_DragGaussian.pulse",
                "x180_Square": "q3.xy.x180_Square.pulse",
                "x90_Square": "q3.xy.x90_Square.pulse",
                "-x90_Square": "q3.xy.-x90_Square.pulse",
                "y180_Square": "q3.xy.y180_Square.pulse",
                "y90_Square": "q3.xy.y90_Square.pulse",
                "-y90_Square": "q3.xy.-y90_Square.pulse",
                "x180": "q3.xy.x180_DragGaussian.pulse",
                "x90": "q3.xy.x90_DragGaussian.pulse",
                "-x90": "q3.xy.-x90_DragGaussian.pulse",
                "y180": "q3.xy.y180_DragGaussian.pulse",
                "y90": "q3.xy.y90_DragGaussian.pulse",
                "-y90": "q3.xy.-y90_DragGaussian.pulse",
                "saturation": "q3.xy.saturation.pulse",
            },
            "digitalInputs": {
                "octave_switch": {
                    "port": ('con1', 1, 7),
                    "delay": 87,
                    "buffer": 15,
                },
            },
            "intermediate_frequency": -236154100.04951477,
            "RF_inputs": {
                "port": ('octave1', 4),
            },
        },
        "q3.z": {
            "operations": {
                "const": "q3.z.const.pulse",
            },
            "singleInput": {
                "port": ('con1', 3, 7),
            },
        },
        "q3.resonator": {
            "operations": {
                "readout": "q3.resonator.readout.pulse",
                "const": "q3.resonator.const.pulse",
            },
            "digitalInputs": {
                "octave_switch": {
                    "port": ('con1', 1, 1),
                    "delay": 87,
                    "buffer": 15,
                },
            },
            "smearing": 0,
            "time_of_flight": 264,
            "RF_outputs": {
                "port": ('octave1', 1),
            },
            "intermediate_frequency": -343278899,
            "RF_inputs": {
                "port": ('octave1', 1),
            },
        },
        "q4.xy": {
            "operations": {
                "x180_DragGaussian": "q4.xy.x180_DragGaussian.pulse",
                "x90_DragGaussian": "q4.xy.x90_DragGaussian.pulse",
                "-x90_DragGaussian": "q4.xy.-x90_DragGaussian.pulse",
                "y180_DragGaussian": "q4.xy.y180_DragGaussian.pulse",
                "y90_DragGaussian": "q4.xy.y90_DragGaussian.pulse",
                "-y90_DragGaussian": "q4.xy.-y90_DragGaussian.pulse",
                "x180_Square": "q4.xy.x180_Square.pulse",
                "x90_Square": "q4.xy.x90_Square.pulse",
                "-x90_Square": "q4.xy.-x90_Square.pulse",
                "y180_Square": "q4.xy.y180_Square.pulse",
                "y90_Square": "q4.xy.y90_Square.pulse",
                "-y90_Square": "q4.xy.-y90_Square.pulse",
                "x180": "q4.xy.x180_DragGaussian.pulse",
                "x90": "q4.xy.x90_DragGaussian.pulse",
                "-x90": "q4.xy.-x90_DragGaussian.pulse",
                "y180": "q4.xy.y180_DragGaussian.pulse",
                "y90": "q4.xy.y90_DragGaussian.pulse",
                "-y90": "q4.xy.-y90_DragGaussian.pulse",
                "saturation": "q4.xy.saturation.pulse",
            },
            "digitalInputs": {
                "octave_switch": {
                    "port": ('con1', 2, 1),
                    "delay": 87,
                    "buffer": 15,
                },
            },
            "intermediate_frequency": -284600668.894413,
            "RF_inputs": {
                "port": ('octave2', 1),
            },
        },
        "q4.z": {
            "operations": {
                "const": "q4.z.const.pulse",
            },
            "singleInput": {
                "port": ('con1', 3, 8),
            },
        },
        "q4.resonator": {
            "operations": {
                "readout": "q4.resonator.readout.pulse",
                "const": "q4.resonator.const.pulse",
            },
            "digitalInputs": {
                "octave_switch": {
                    "port": ('con1', 1, 1),
                    "delay": 87,
                    "buffer": 15,
                },
            },
            "smearing": 0,
            "time_of_flight": 264,
            "RF_outputs": {
                "port": ('octave1', 1),
            },
            "intermediate_frequency": -162578680,
            "RF_inputs": {
                "port": ('octave1', 1),
            },
        },
        "q5.xy": {
            "operations": {
                "x180_DragGaussian": "q5.xy.x180_DragGaussian.pulse",
                "x90_DragGaussian": "q5.xy.x90_DragGaussian.pulse",
                "-x90_DragGaussian": "q5.xy.-x90_DragGaussian.pulse",
                "y180_DragGaussian": "q5.xy.y180_DragGaussian.pulse",
                "y90_DragGaussian": "q5.xy.y90_DragGaussian.pulse",
                "-y90_DragGaussian": "q5.xy.-y90_DragGaussian.pulse",
                "x180_Square": "q5.xy.x180_Square.pulse",
                "x90_Square": "q5.xy.x90_Square.pulse",
                "-x90_Square": "q5.xy.-x90_Square.pulse",
                "y180_Square": "q5.xy.y180_Square.pulse",
                "y90_Square": "q5.xy.y90_Square.pulse",
                "-y90_Square": "q5.xy.-y90_Square.pulse",
                "x180": "q5.xy.x180_DragGaussian.pulse",
                "x90": "q5.xy.x90_DragGaussian.pulse",
                "-x90": "q5.xy.-x90_DragGaussian.pulse",
                "y180": "q5.xy.y180_DragGaussian.pulse",
                "y90": "q5.xy.y90_DragGaussian.pulse",
                "-y90": "q5.xy.-y90_DragGaussian.pulse",
                "saturation": "q5.xy.saturation.pulse",
            },
            "digitalInputs": {
                "octave_switch": {
                    "port": ('con1', 2, 3),
                    "delay": 87,
                    "buffer": 15,
                },
            },
            "intermediate_frequency": -345901097.018157,
            "RF_inputs": {
                "port": ('octave2', 2),
            },
        },
        "q5.z": {
            "operations": {
                "const": "q5.z.const.pulse",
            },
            "singleInput": {
                "port": ('con1', 3, 1),
            },
        },
        "q5.resonator": {
            "operations": {
                "readout": "q5.resonator.readout.pulse",
                "const": "q5.resonator.const.pulse",
            },
            "digitalInputs": {
                "octave_switch": {
                    "port": ('con1', 1, 1),
                    "delay": 87,
                    "buffer": 15,
                },
            },
            "smearing": 0,
            "time_of_flight": 264,
            "RF_outputs": {
                "port": ('octave1', 1),
            },
            "intermediate_frequency": -257761381,
            "RF_inputs": {
                "port": ('octave1', 1),
            },
        },
        "coupler_q1_q2": {
            "operations": {
                "const": "coupler_q1_q2.const.pulse",
            },
            "singleInput": {
                "port": ('con1', 3, 2),
            },
        },
        "coupler_q2_q3": {
            "operations": {
                "const": "coupler_q2_q3.const.pulse",
            },
            "singleInput": {
                "port": ('con1', 3, 3),
            },
        },
        "coupler_q3_q4": {
            "operations": {
                "const": "coupler_q3_q4.const.pulse",
            },
            "singleInput": {
                "port": ('con1', 3, 4),
            },
        },
        "coupler_q4_q5": {
            "operations": {
                "const": "coupler_q4_q5.const.pulse",
            },
            "singleInput": {
                "port": ('con1', 3, 5),
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
        "q1.xy.x180_DragGaussian.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q1.xy.x180_DragGaussian.wf.I",
                "Q": "q1.xy.x180_DragGaussian.wf.Q",
            },
        },
        "q1.xy.x90_DragGaussian.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q1.xy.x90_DragGaussian.wf.I",
                "Q": "q1.xy.x90_DragGaussian.wf.Q",
            },
        },
        "q1.xy.-x90_DragGaussian.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q1.xy.-x90_DragGaussian.wf.I",
                "Q": "q1.xy.-x90_DragGaussian.wf.Q",
            },
        },
        "q1.xy.y180_DragGaussian.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q1.xy.y180_DragGaussian.wf.I",
                "Q": "q1.xy.y180_DragGaussian.wf.Q",
            },
        },
        "q1.xy.y90_DragGaussian.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q1.xy.y90_DragGaussian.wf.I",
                "Q": "q1.xy.y90_DragGaussian.wf.Q",
            },
        },
        "q1.xy.-y90_DragGaussian.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q1.xy.-y90_DragGaussian.wf.I",
                "Q": "q1.xy.-y90_DragGaussian.wf.Q",
            },
        },
        "q1.xy.x180_Square.pulse": {
            "operation": "control",
            "length": 100,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q1.xy.x180_Square.wf.I",
                "Q": "q1.xy.x180_Square.wf.Q",
            },
        },
        "q1.xy.x90_Square.pulse": {
            "operation": "control",
            "length": 100,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q1.xy.x90_Square.wf.I",
                "Q": "q1.xy.x90_Square.wf.Q",
            },
        },
        "q1.xy.-x90_Square.pulse": {
            "operation": "control",
            "length": 100,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q1.xy.-x90_Square.wf.I",
                "Q": "q1.xy.-x90_Square.wf.Q",
            },
        },
        "q1.xy.y180_Square.pulse": {
            "operation": "control",
            "length": 100,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q1.xy.y180_Square.wf.I",
                "Q": "q1.xy.y180_Square.wf.Q",
            },
        },
        "q1.xy.y90_Square.pulse": {
            "operation": "control",
            "length": 100,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q1.xy.y90_Square.wf.I",
                "Q": "q1.xy.y90_Square.wf.Q",
            },
        },
        "q1.xy.-y90_Square.pulse": {
            "operation": "control",
            "length": 100,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q1.xy.-y90_Square.wf.I",
                "Q": "q1.xy.-y90_Square.wf.Q",
            },
        },
        "q1.xy.saturation.pulse": {
            "operation": "control",
            "length": 10000,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q1.xy.saturation.wf.I",
                "Q": "q1.xy.saturation.wf.Q",
            },
        },
        "q1.z.const.pulse": {
            "operation": "control",
            "length": 100,
            "waveforms": {
                "single": "q1.z.const.wf",
            },
        },
        "q1.resonator.readout.pulse": {
            "operation": "measurement",
            "length": 1024,
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
        "q2.xy.x180_DragGaussian.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q2.xy.x180_DragGaussian.wf.I",
                "Q": "q2.xy.x180_DragGaussian.wf.Q",
            },
        },
        "q2.xy.x90_DragGaussian.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q2.xy.x90_DragGaussian.wf.I",
                "Q": "q2.xy.x90_DragGaussian.wf.Q",
            },
        },
        "q2.xy.-x90_DragGaussian.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q2.xy.-x90_DragGaussian.wf.I",
                "Q": "q2.xy.-x90_DragGaussian.wf.Q",
            },
        },
        "q2.xy.y180_DragGaussian.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q2.xy.y180_DragGaussian.wf.I",
                "Q": "q2.xy.y180_DragGaussian.wf.Q",
            },
        },
        "q2.xy.y90_DragGaussian.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q2.xy.y90_DragGaussian.wf.I",
                "Q": "q2.xy.y90_DragGaussian.wf.Q",
            },
        },
        "q2.xy.-y90_DragGaussian.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q2.xy.-y90_DragGaussian.wf.I",
                "Q": "q2.xy.-y90_DragGaussian.wf.Q",
            },
        },
        "q2.xy.x180_Square.pulse": {
            "operation": "control",
            "length": 100,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q2.xy.x180_Square.wf.I",
                "Q": "q2.xy.x180_Square.wf.Q",
            },
        },
        "q2.xy.x90_Square.pulse": {
            "operation": "control",
            "length": 100,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q2.xy.x90_Square.wf.I",
                "Q": "q2.xy.x90_Square.wf.Q",
            },
        },
        "q2.xy.-x90_Square.pulse": {
            "operation": "control",
            "length": 100,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q2.xy.-x90_Square.wf.I",
                "Q": "q2.xy.-x90_Square.wf.Q",
            },
        },
        "q2.xy.y180_Square.pulse": {
            "operation": "control",
            "length": 100,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q2.xy.y180_Square.wf.I",
                "Q": "q2.xy.y180_Square.wf.Q",
            },
        },
        "q2.xy.y90_Square.pulse": {
            "operation": "control",
            "length": 100,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q2.xy.y90_Square.wf.I",
                "Q": "q2.xy.y90_Square.wf.Q",
            },
        },
        "q2.xy.-y90_Square.pulse": {
            "operation": "control",
            "length": 100,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q2.xy.-y90_Square.wf.I",
                "Q": "q2.xy.-y90_Square.wf.Q",
            },
        },
        "q2.xy.saturation.pulse": {
            "operation": "control",
            "length": 10000,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q2.xy.saturation.wf.I",
                "Q": "q2.xy.saturation.wf.Q",
            },
        },
        "q2.z.const.pulse": {
            "operation": "control",
            "length": 100,
            "waveforms": {
                "single": "q2.z.const.wf",
            },
        },
        "q2.resonator.readout.pulse": {
            "operation": "measurement",
            "length": 1024,
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
        "q3.xy.x180_DragGaussian.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q3.xy.x180_DragGaussian.wf.I",
                "Q": "q3.xy.x180_DragGaussian.wf.Q",
            },
        },
        "q3.xy.x90_DragGaussian.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q3.xy.x90_DragGaussian.wf.I",
                "Q": "q3.xy.x90_DragGaussian.wf.Q",
            },
        },
        "q3.xy.-x90_DragGaussian.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q3.xy.-x90_DragGaussian.wf.I",
                "Q": "q3.xy.-x90_DragGaussian.wf.Q",
            },
        },
        "q3.xy.y180_DragGaussian.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q3.xy.y180_DragGaussian.wf.I",
                "Q": "q3.xy.y180_DragGaussian.wf.Q",
            },
        },
        "q3.xy.y90_DragGaussian.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q3.xy.y90_DragGaussian.wf.I",
                "Q": "q3.xy.y90_DragGaussian.wf.Q",
            },
        },
        "q3.xy.-y90_DragGaussian.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q3.xy.-y90_DragGaussian.wf.I",
                "Q": "q3.xy.-y90_DragGaussian.wf.Q",
            },
        },
        "q3.xy.x180_Square.pulse": {
            "operation": "control",
            "length": 100,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q3.xy.x180_Square.wf.I",
                "Q": "q3.xy.x180_Square.wf.Q",
            },
        },
        "q3.xy.x90_Square.pulse": {
            "operation": "control",
            "length": 100,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q3.xy.x90_Square.wf.I",
                "Q": "q3.xy.x90_Square.wf.Q",
            },
        },
        "q3.xy.-x90_Square.pulse": {
            "operation": "control",
            "length": 100,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q3.xy.-x90_Square.wf.I",
                "Q": "q3.xy.-x90_Square.wf.Q",
            },
        },
        "q3.xy.y180_Square.pulse": {
            "operation": "control",
            "length": 100,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q3.xy.y180_Square.wf.I",
                "Q": "q3.xy.y180_Square.wf.Q",
            },
        },
        "q3.xy.y90_Square.pulse": {
            "operation": "control",
            "length": 100,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q3.xy.y90_Square.wf.I",
                "Q": "q3.xy.y90_Square.wf.Q",
            },
        },
        "q3.xy.-y90_Square.pulse": {
            "operation": "control",
            "length": 100,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q3.xy.-y90_Square.wf.I",
                "Q": "q3.xy.-y90_Square.wf.Q",
            },
        },
        "q3.xy.saturation.pulse": {
            "operation": "control",
            "length": 10000,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q3.xy.saturation.wf.I",
                "Q": "q3.xy.saturation.wf.Q",
            },
        },
        "q3.z.const.pulse": {
            "operation": "control",
            "length": 100,
            "waveforms": {
                "single": "q3.z.const.wf",
            },
        },
        "q3.resonator.readout.pulse": {
            "operation": "measurement",
            "length": 1024,
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
        "q4.xy.x180_DragGaussian.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q4.xy.x180_DragGaussian.wf.I",
                "Q": "q4.xy.x180_DragGaussian.wf.Q",
            },
        },
        "q4.xy.x90_DragGaussian.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q4.xy.x90_DragGaussian.wf.I",
                "Q": "q4.xy.x90_DragGaussian.wf.Q",
            },
        },
        "q4.xy.-x90_DragGaussian.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q4.xy.-x90_DragGaussian.wf.I",
                "Q": "q4.xy.-x90_DragGaussian.wf.Q",
            },
        },
        "q4.xy.y180_DragGaussian.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q4.xy.y180_DragGaussian.wf.I",
                "Q": "q4.xy.y180_DragGaussian.wf.Q",
            },
        },
        "q4.xy.y90_DragGaussian.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q4.xy.y90_DragGaussian.wf.I",
                "Q": "q4.xy.y90_DragGaussian.wf.Q",
            },
        },
        "q4.xy.-y90_DragGaussian.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q4.xy.-y90_DragGaussian.wf.I",
                "Q": "q4.xy.-y90_DragGaussian.wf.Q",
            },
        },
        "q4.xy.x180_Square.pulse": {
            "operation": "control",
            "length": 100,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q4.xy.x180_Square.wf.I",
                "Q": "q4.xy.x180_Square.wf.Q",
            },
        },
        "q4.xy.x90_Square.pulse": {
            "operation": "control",
            "length": 100,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q4.xy.x90_Square.wf.I",
                "Q": "q4.xy.x90_Square.wf.Q",
            },
        },
        "q4.xy.-x90_Square.pulse": {
            "operation": "control",
            "length": 100,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q4.xy.-x90_Square.wf.I",
                "Q": "q4.xy.-x90_Square.wf.Q",
            },
        },
        "q4.xy.y180_Square.pulse": {
            "operation": "control",
            "length": 100,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q4.xy.y180_Square.wf.I",
                "Q": "q4.xy.y180_Square.wf.Q",
            },
        },
        "q4.xy.y90_Square.pulse": {
            "operation": "control",
            "length": 100,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q4.xy.y90_Square.wf.I",
                "Q": "q4.xy.y90_Square.wf.Q",
            },
        },
        "q4.xy.-y90_Square.pulse": {
            "operation": "control",
            "length": 100,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q4.xy.-y90_Square.wf.I",
                "Q": "q4.xy.-y90_Square.wf.Q",
            },
        },
        "q4.xy.saturation.pulse": {
            "operation": "control",
            "length": 10000,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q4.xy.saturation.wf.I",
                "Q": "q4.xy.saturation.wf.Q",
            },
        },
        "q4.z.const.pulse": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "single": "q4.z.const.wf",
            },
        },
        "q4.resonator.readout.pulse": {
            "operation": "measurement",
            "length": 1024,
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
        "q5.xy.x180_DragGaussian.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q5.xy.x180_DragGaussian.wf.I",
                "Q": "q5.xy.x180_DragGaussian.wf.Q",
            },
        },
        "q5.xy.x90_DragGaussian.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q5.xy.x90_DragGaussian.wf.I",
                "Q": "q5.xy.x90_DragGaussian.wf.Q",
            },
        },
        "q5.xy.-x90_DragGaussian.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q5.xy.-x90_DragGaussian.wf.I",
                "Q": "q5.xy.-x90_DragGaussian.wf.Q",
            },
        },
        "q5.xy.y180_DragGaussian.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q5.xy.y180_DragGaussian.wf.I",
                "Q": "q5.xy.y180_DragGaussian.wf.Q",
            },
        },
        "q5.xy.y90_DragGaussian.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q5.xy.y90_DragGaussian.wf.I",
                "Q": "q5.xy.y90_DragGaussian.wf.Q",
            },
        },
        "q5.xy.-y90_DragGaussian.pulse": {
            "operation": "control",
            "length": 40,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q5.xy.-y90_DragGaussian.wf.I",
                "Q": "q5.xy.-y90_DragGaussian.wf.Q",
            },
        },
        "q5.xy.x180_Square.pulse": {
            "operation": "control",
            "length": 100,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q5.xy.x180_Square.wf.I",
                "Q": "q5.xy.x180_Square.wf.Q",
            },
        },
        "q5.xy.x90_Square.pulse": {
            "operation": "control",
            "length": 100,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q5.xy.x90_Square.wf.I",
                "Q": "q5.xy.x90_Square.wf.Q",
            },
        },
        "q5.xy.-x90_Square.pulse": {
            "operation": "control",
            "length": 100,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q5.xy.-x90_Square.wf.I",
                "Q": "q5.xy.-x90_Square.wf.Q",
            },
        },
        "q5.xy.y180_Square.pulse": {
            "operation": "control",
            "length": 100,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q5.xy.y180_Square.wf.I",
                "Q": "q5.xy.y180_Square.wf.Q",
            },
        },
        "q5.xy.y90_Square.pulse": {
            "operation": "control",
            "length": 100,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q5.xy.y90_Square.wf.I",
                "Q": "q5.xy.y90_Square.wf.Q",
            },
        },
        "q5.xy.-y90_Square.pulse": {
            "operation": "control",
            "length": 100,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q5.xy.-y90_Square.wf.I",
                "Q": "q5.xy.-y90_Square.wf.Q",
            },
        },
        "q5.xy.saturation.pulse": {
            "operation": "control",
            "length": 10000,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q5.xy.saturation.wf.I",
                "Q": "q5.xy.saturation.wf.Q",
            },
        },
        "q5.z.const.pulse": {
            "operation": "control",
            "length": 100,
            "waveforms": {
                "single": "q5.z.const.wf",
            },
        },
        "q5.resonator.readout.pulse": {
            "operation": "measurement",
            "length": 1024,
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
        "coupler_q1_q2.const.pulse": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "single": "coupler_q1_q2.const.wf",
            },
        },
        "coupler_q2_q3.const.pulse": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "single": "coupler_q2_q3.const.wf",
            },
        },
        "coupler_q3_q4.const.pulse": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "single": "coupler_q3_q4.const.wf",
            },
        },
        "coupler_q4_q5.const.pulse": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "single": "coupler_q4_q5.const.wf",
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
        "q1.xy.x180_DragGaussian.wf.I": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
        },
        "q1.xy.x180_DragGaussian.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
        },
        "q1.xy.x90_DragGaussian.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0009308033584822786, 0.0022162882408895738, 0.0039504329579779455, 0.00623471737013874, 0.009171468002093624, 0.012854464586515613, 0.0173570914762729, 0.022718822828775964, 0.028931368012269813, 0.035926273150203525, 0.04356605894305792, 0.0516409635018751, 0.05987297730580422, 0.0679280941544471, 0.07543662643820798, 0.08202019565499412, 0.08732282109948077, 0.09104262368830635] + [0.09296024132804348] * 2 + [0.09104262368830635, 0.08732282109948077, 0.08202019565499412, 0.07543662643820798, 0.0679280941544471, 0.05987297730580422, 0.0516409635018751, 0.04356605894305792, 0.035926273150203525, 0.028931368012269813, 0.022718822828775964, 0.0173570914762729, 0.012854464586515613, 0.009171468002093624, 0.00623471737013874, 0.0039504329579779455, 0.0022162882408895738, 0.0009308033584822786, 0.0],
        },
        "q1.xy.x90_DragGaussian.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0008297562420585476, 0.0011600789497869175, 0.0015844940588258436, 0.002113538223091799, 0.0027521259378796544, 0.003496647861908873, 0.004332133204156863, 0.005229967996598423, 0.00614673784329763, 0.007024749293451887, 0.007794650779385713, 0.008380315267377378, 0.008705784574698384, 0.00870366322667387, 0.008323966570666159, 0.007542163018573711, 0.006365082784623594, 0.004833541802232808, 0.0030209465036534853, 0.0010277439587909154, -0.0010277439587909154, -0.0030209465036534853, -0.004833541802232808, -0.006365082784623594, -0.007542163018573711, -0.008323966570666159, -0.00870366322667387, -0.008705784574698384, -0.008380315267377378, -0.007794650779385713, -0.007024749293451887, -0.00614673784329763, -0.005229967996598423, -0.004332133204156863, -0.003496647861908873, -0.0027521259378796544, -0.002113538223091799, -0.0015844940588258436, -0.0011600789497869175, -0.0008297562420585476],
        },
        "q1.xy.-x90_DragGaussian.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -0.0004890327182525387, -0.0011644107780623145, -0.002075509236305739, -0.003275644372434133, -0.004818577292999117, -0.00675357872437716, -0.009119203909448838, -0.011936192088487896, -0.01520018746480943, -0.018875225207582575, -0.022889075371637223, -0.027131531621974618, -0.03145653115118992, -0.03568859118023487, -0.03963348235338423, -0.04309240922612172, -0.04587834388284734, -0.04783268273949085] + [-0.048840175630855964] * 2 + [-0.04783268273949085, -0.04587834388284734, -0.04309240922612172, -0.03963348235338423, -0.03568859118023487, -0.03145653115118992, -0.027131531621974618, -0.022889075371637223, -0.018875225207582575, -0.01520018746480943, -0.011936192088487896, -0.009119203909448838, -0.00675357872437716, -0.004818577292999117, -0.003275644372434133, -0.002075509236305739, -0.0011644107780623145, -0.0004890327182525387, 0.0],
        },
        "q1.xy.-x90_DragGaussian.wf.Q": {
            "type": "arbitrary",
            "samples": [-0.000435943797197449, -0.0006094913141771259, -0.0008324738298173561, -0.0011104271734198958, -0.0014459333608004257, -0.0018370960881248035, -0.002276049884602178, -0.002747761320845089, -0.0032294210033738465, -0.0036907174976472555, -0.004095214336879552, -0.00440291530716134, -0.004573912906833186, -0.0045727983764854655, -0.004373310389998592, -0.003962560350545937, -0.0033441367692767913, -0.0025394838391939335, -0.0015871684034166418, -0.0005399641258865475, 0.0005399641258865475, 0.0015871684034166418, 0.0025394838391939335, 0.0033441367692767913, 0.003962560350545937, 0.004373310389998592, 0.0045727983764854655, 0.004573912906833186, 0.00440291530716134, 0.004095214336879552, 0.0036907174976472555, 0.0032294210033738465, 0.002747761320845089, 0.002276049884602178, 0.0018370960881248035, 0.0014459333608004257, 0.0011104271734198958, 0.0008324738298173561, 0.0006094913141771259, 0.000435943797197449],
        },
        "q1.xy.y180_DragGaussian.wf.I": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
        },
        "q1.xy.y180_DragGaussian.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
        },
        "q1.xy.y90_DragGaussian.wf.I": {
            "type": "arbitrary",
            "samples": [-0.00043593540845350163, -0.0006125133656181951, -0.0008396813883669383, -0.001123281504229698, -0.0014662264339898217, -0.0018669534245001442, -0.0023179028138472987, -0.0028042806445208704, -0.003303406620599842, -0.0037849428690515776, -0.004212230511600758, -0.0045448260158726, -0.0047421389684343595, -0.004767855171124772, -0.0045946251723320225, -0.004208355695520126, -0.003611401928723668, -0.0028240473996744295, -0.0018838742908671767, -0.0008429402809590696, 0.00023696719005824012, 0.001290401433095227, 0.0022548225455660802, 0.00307674290926226, 0.003716612504701818, 0.004151827298900133, 0.0043775655956986344, 0.004405510816191299, 0.004260835150326854, 0.003978040556041674, 0.003596350087364212, 0.003155311100466671, 0.0026911362483718836, 0.002234109360580776, 0.0018071680503022167, 0.0014255846402325984, 0.001097530107334171, 0.0008252342331479699, 0.0006064458061959906, 0.00043593540845350163],
        },
        "q1.xy.y90_DragGaussian.wf.Q": {
            "type": "arbitrary",
            "samples": [-2.704435506573881e-06, 0.00048524224725171876, 0.0011592240091667493, 0.002068580614748963, 0.003266611299619915, 0.004807087899795191, 0.006739328988045931, 0.009101982327229873, 0.011915928259656917, 0.01517699911348765, 0.018849456788435155, 0.022861320851078854, 0.02710263465860026, 0.03142755787720306, 0.035660774020245, 0.03960813742563163, 0.043070834212403875, 0.045861707031975105, 0.04782191609768266, 0.04883588607359181, 0.048842585552578366, 0.047841608519562304, 0.045893215085569344, 0.04311232580960431, 0.039657301969216616, 0.03571503484916843, 0.0314842938068035, 0.02715938441647611, 0.0229159489961089, 0.018900267205424166, 0.015222790830261866, 0.011955996547740592, 0.009136074535112892, 0.006767568546274413, 0.004829881241146312, 0.0032845513806405756, 0.0020823579809808816, 0.0011695527340992978, 0.0004928043686150945, 2.704435506573881e-06],
        },
        "q1.xy.-y90_DragGaussian.wf.I": {
            "type": "arbitrary",
            "samples": [0.00043593540845350163, 0.0006125133656181951, 0.0008396813883669383, 0.001123281504229698, 0.0014662264339898217, 0.0018669534245001442, 0.0023179028138472987, 0.0028042806445208704, 0.003303406620599842, 0.0037849428690515776, 0.004212230511600758, 0.0045448260158726, 0.0047421389684343595, 0.004767855171124772, 0.0045946251723320225, 0.004208355695520126, 0.003611401928723668, 0.0028240473996744295, 0.0018838742908671767, 0.0008429402809590696, -0.00023696719005824012, -0.001290401433095227, -0.0022548225455660802, -0.00307674290926226, -0.003716612504701818, -0.004151827298900133, -0.0043775655956986344, -0.004405510816191299, -0.004260835150326854, -0.003978040556041674, -0.003596350087364212, -0.003155311100466671, -0.0026911362483718836, -0.002234109360580776, -0.0018071680503022167, -0.0014255846402325984, -0.001097530107334171, -0.0008252342331479699, -0.0006064458061959906, -0.00043593540845350163],
        },
        "q1.xy.-y90_DragGaussian.wf.Q": {
            "type": "arbitrary",
            "samples": [2.704435506573881e-06, -0.00048524224725171876, -0.0011592240091667493, -0.002068580614748963, -0.003266611299619915, -0.004807087899795191, -0.006739328988045931, -0.009101982327229873, -0.011915928259656917, -0.01517699911348765, -0.018849456788435155, -0.022861320851078854, -0.02710263465860026, -0.03142755787720306, -0.035660774020245, -0.03960813742563163, -0.043070834212403875, -0.045861707031975105, -0.04782191609768266, -0.04883588607359181, -0.048842585552578366, -0.047841608519562304, -0.045893215085569344, -0.04311232580960431, -0.039657301969216616, -0.03571503484916843, -0.0314842938068035, -0.02715938441647611, -0.0229159489961089, -0.018900267205424166, -0.015222790830261866, -0.011955996547740592, -0.009136074535112892, -0.006767568546274413, -0.004829881241146312, -0.0032845513806405756, -0.0020823579809808816, -0.0011695527340992978, -0.0004928043686150945, -2.704435506573881e-06],
        },
        "q1.xy.x180_Square.wf.I": {
            "type": "constant",
            "sample": 0.25,
        },
        "q1.xy.x180_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q1.xy.x90_Square.wf.I": {
            "type": "constant",
            "sample": 0.125,
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
            "sample": -0.0015509083533014347,
        },
        "q1.xy.y180_Square.wf.Q": {
            "type": "constant",
            "sample": 0.24999518932027404,
        },
        "q1.xy.y90_Square.wf.I": {
            "type": "constant",
            "sample": -0.0007754541766507173,
        },
        "q1.xy.y90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.12499759466013702,
        },
        "q1.xy.-y90_Square.wf.I": {
            "type": "constant",
            "sample": 0.0007754541766507173,
        },
        "q1.xy.-y90_Square.wf.Q": {
            "type": "constant",
            "sample": -0.12499759466013702,
        },
        "q1.xy.saturation.wf.I": {
            "type": "constant",
            "sample": 0.25,
        },
        "q1.xy.saturation.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q1.z.const.wf": {
            "type": "constant",
            "sample": 0.1,
        },
        "q1.resonator.readout.wf.I": {
            "type": "constant",
            "sample": 0.015,
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
        "q2.xy.x180_DragGaussian.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0005643674229523334, 0.001343786387997033, 0.0023952381002097798, 0.0037802521262479305, 0.005560871384769406, 0.0077939566784040164, 0.010524002623265721, 0.013774943306278407, 0.017541751927274703, 0.021782923331005566, 0.026415100665272424, 0.03131110048619751, 0.03630235924552004, 0.04118636132396231, 0.0457389566455457, 0.049730725646856884, 0.05294582906232589, 0.05520123068052587] + [0.056363926233441615] * 2 + [0.05520123068052587, 0.05294582906232589, 0.049730725646856884, 0.0457389566455457, 0.04118636132396231, 0.03630235924552004, 0.03131110048619751, 0.026415100665272424, 0.021782923331005566, 0.017541751927274703, 0.013774943306278407, 0.010524002623265721, 0.0077939566784040164, 0.005560871384769406, 0.0037802521262479305, 0.0023952381002097798, 0.001343786387997033, 0.0005643674229523334, 0.0],
        },
        "q2.xy.x180_DragGaussian.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
        },
        "q2.xy.x90_DragGaussian.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.00026603379872938097, 0.000633439463265899, 0.0011290770245503219, 0.0017819505386041678, 0.002621306047391519, 0.0036739468260611747, 0.004960846926740169, 0.006493288496137415, 0.008268901980856329, 0.010268122512924919, 0.012451657002170647, 0.01475955320235419, 0.017112352946247314, 0.019414593602047767, 0.021560614400241016, 0.023442270619010212, 0.024957819072268947, 0.026020979410283022] + [0.026569055543185643] * 2 + [0.026020979410283022, 0.024957819072268947, 0.023442270619010212, 0.021560614400241016, 0.019414593602047767, 0.017112352946247314, 0.01475955320235419, 0.012451657002170647, 0.010268122512924919, 0.008268901980856329, 0.006493288496137415, 0.004960846926740169, 0.0036739468260611747, 0.002621306047391519, 0.0017819505386041678, 0.0011290770245503219, 0.000633439463265899, 0.00026603379872938097, 0.0],
        },
        "q2.xy.x90_DragGaussian.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
        },
        "q2.xy.-x90_DragGaussian.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -0.0002660337987284443, -0.0006334394632636688, -0.0011290770245463468, -0.001781950538597894, -0.0026213060473822903, -0.0036739468260482398, -0.004960846926722703, -0.006493288496114554, -0.008268901980827217, -0.010268122512888767, -0.012451657002126809, -0.014759553202302225, -0.017112352946187067, -0.01941459360197941, -0.021560614400165108, -0.023442270618927678, -0.024957819072181076, -0.026020979410191408] + [-0.0265690555430921] * 2 + [-0.026020979410191408, -0.024957819072181076, -0.023442270618927678, -0.021560614400165108, -0.01941459360197941, -0.017112352946187067, -0.014759553202302225, -0.012451657002126809, -0.010268122512888767, -0.008268901980827217, -0.006493288496114554, -0.004960846926722703, -0.0036739468260482398, -0.0026213060473822903, -0.001781950538597894, -0.0011290770245463468, -0.0006334394632636688, -0.0002660337987284443, 0.0],
        },
        "q2.xy.-x90_DragGaussian.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 7.059445729951398e-10, 1.6808884944292212e-09, 2.996107268255804e-09, 4.72856576149942e-09, 6.955870972611922e-09, 9.74914779895659e-09, 1.316405277118297e-08, 1.7230524078644942e-08, 2.1942273898634525e-08, 2.724738509719295e-08, 3.304158993128908e-08, 3.916579973221368e-08, 4.540916511841139e-08, 5.151836742448517e-08, 5.721302631089345e-08, 6.220617004761808e-08, 6.622781395451698e-08, 6.904900537616857e-08] + [7.05033746084192e-08] * 2 + [6.904900537616857e-08, 6.622781395451698e-08, 6.220617004761808e-08, 5.721302631089345e-08, 5.151836742448517e-08, 4.540916511841139e-08, 3.916579973221368e-08, 3.304158993128908e-08, 2.724738509719295e-08, 2.1942273898634525e-08, 1.7230524078644942e-08, 1.316405277118297e-08, 9.74914779895659e-09, 6.955870972611922e-09, 4.72856576149942e-09, 2.996107268255804e-09, 1.6808884944292212e-09, 7.059445729951398e-10, 0.0],
        },
        "q2.xy.y180_DragGaussian.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -3.501128602351911e-06, -8.336358136789445e-06, -1.4859179111044826e-05, -2.34512984007337e-05, -3.449760752909515e-05, -4.835085007122517e-05, -6.528705431435607e-05, -8.545469855984346e-05, -0.00010882259838220751, -0.00013513327101352497, -0.00016386960110027716, -0.0001942425891804173, -0.0002252065287937064, -0.00025550508727769717, -0.00028374771973147596, -0.00030851119128580894, -0.00032845651426092435, -0.00034244819909978806] + [-0.0003496611360812419] * 2 + [-0.00034244819909978806, -0.00032845651426092435, -0.00030851119128580894, -0.00028374771973147596, -0.00025550508727769717, -0.0002252065287937064, -0.0001942425891804173, -0.00016386960110027716, -0.00013513327101352497, -0.00010882259838220751, -8.545469855984346e-05, -6.528705431435607e-05, -4.835085007122517e-05, -3.449760752909515e-05, -2.34512984007337e-05, -1.4859179111044826e-05, -8.336358136789445e-06, -3.501128602351911e-06, 0.0],
        },
        "q2.xy.y180_DragGaussian.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0005643565629886551, 0.0013437605298933018, 0.0023951920093163094, 0.0037801793839188796, 0.005560764378484488, 0.0077938067014865055, 0.010523800112841498, 0.013774678238916448, 0.017541414376273285, 0.021782504168335003, 0.026414592366915506, 0.031310497975492284, 0.03630166068942553, 0.04118556878638868, 0.04573807650366001, 0.04972976869248238, 0.05294481024062011, 0.05520016845876074] + [0.05636284163825279] * 2 + [0.05520016845876074, 0.05294481024062011, 0.04972976869248238, 0.04573807650366001, 0.04118556878638868, 0.03630166068942553, 0.031310497975492284, 0.026414592366915506, 0.021782504168335003, 0.017541414376273285, 0.013774678238916448, 0.010523800112841498, 0.0077938067014865055, 0.005560764378484488, 0.0037801793839188796, 0.0023951920093163094, 0.0013437605298933018, 0.0005643565629886551, 0.0],
        },
        "q2.xy.y90_DragGaussian.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -1.6503761628396382e-06, -3.929626219559441e-06, -7.004379955583293e-06, -1.1054567901964778e-05, -1.6261621781836294e-05, -2.2791819288494275e-05, -3.077527575252431e-05, -4.028198147622251e-05, -5.1297236618963444e-05, -6.36996679120711e-05, -7.724551542844303e-05, -9.156285741011222e-05, -0.0001061587645159095, -0.00012044102157347389, -0.00013375414790257997, -0.00014542725329350293, -0.0001548291603174711, -0.00016142461731397033] + [-0.0001648246807250256] * 2 + [-0.00016142461731397033, -0.0001548291603174711, -0.00014542725329350293, -0.00013375414790257997, -0.00012044102157347389, -0.0001061587645159095, -9.156285741011222e-05, -7.724551542844303e-05, -6.36996679120711e-05, -5.1297236618963444e-05, -4.028198147622251e-05, -3.077527575252431e-05, -2.2791819288494275e-05, -1.6261621781836294e-05, -1.1054567901964778e-05, -7.004379955583293e-06, -3.929626219559441e-06, -1.6503761628396382e-06, 0.0],
        },
        "q2.xy.y90_DragGaussian.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0002660286795157731, 0.0006334272741683648, 0.0011290552980385176, 0.001781916249030853, 0.002621255606336088, 0.0036738761293351333, 0.004960751466557232, 0.006493163547612122, 0.008268742864699868, 0.010267924926329733, 0.012451417398435067, 0.01475926918842077, 0.017112023658049785, 0.01941422001248045, 0.02156019951539872, 0.023441819525986222, 0.024957338815972088, 0.026020478695890626] + [0.026568544282318286] * 2 + [0.026020478695890626, 0.024957338815972088, 0.023441819525986222, 0.02156019951539872, 0.01941422001248045, 0.017112023658049785, 0.01475926918842077, 0.012451417398435067, 0.010267924926329733, 0.008268742864699868, 0.006493163547612122, 0.004960751466557232, 0.0036738761293351333, 0.002621255606336088, 0.001781916249030853, 0.0011290552980385176, 0.0006334272741683648, 0.0002660286795157731, 0.0],
        },
        "q2.xy.-y90_DragGaussian.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -1.6503761628396382e-06, -3.929626219559441e-06, -7.004379955583293e-06, -1.1054567901964778e-05, -1.6261621781836294e-05, -2.2791819288494275e-05, -3.077527575252431e-05, -4.028198147622251e-05, -5.1297236618963444e-05, -6.36996679120711e-05, -7.724551542844303e-05, -9.156285741011222e-05, -0.0001061587645159095, -0.00012044102157347389, -0.00013375414790257997, -0.00014542725329350293, -0.0001548291603174711, -0.00016142461731397033] + [-0.0001648246807250256] * 2 + [-0.00016142461731397033, -0.0001548291603174711, -0.00014542725329350293, -0.00013375414790257997, -0.00012044102157347389, -0.0001061587645159095, -9.156285741011222e-05, -7.724551542844303e-05, -6.36996679120711e-05, -5.1297236618963444e-05, -4.028198147622251e-05, -3.077527575252431e-05, -2.2791819288494275e-05, -1.6261621781836294e-05, -1.1054567901964778e-05, -7.004379955583293e-06, -3.929626219559441e-06, -1.6503761628396382e-06, 0.0],
        },
        "q2.xy.-y90_DragGaussian.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.0002660286795157731, -0.0006334272741683648, -0.0011290552980385176, -0.001781916249030853, -0.002621255606336088, -0.0036738761293351333, -0.004960751466557232, -0.006493163547612122, -0.008268742864699868, -0.010267924926329733, -0.012451417398435067, -0.01475926918842077, -0.017112023658049785, -0.01941422001248045, -0.02156019951539872, -0.023441819525986222, -0.024957338815972088, -0.026020478695890626] + [-0.026568544282318286] * 2 + [-0.026020478695890626, -0.024957338815972088, -0.023441819525986222, -0.02156019951539872, -0.01941422001248045, -0.017112023658049785, -0.01475926918842077, -0.012451417398435067, -0.010267924926329733, -0.008268742864699868, -0.006493163547612122, -0.004960751466557232, -0.0036738761293351333, -0.002621255606336088, -0.001781916249030853, -0.0011290552980385176, -0.0006334272741683648, -0.0002660286795157731, 0.0],
        },
        "q2.xy.x180_Square.wf.I": {
            "type": "constant",
            "sample": 0.25,
        },
        "q2.xy.x180_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q2.xy.x90_Square.wf.I": {
            "type": "constant",
            "sample": 0.125,
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
            "sample": -0.0015509083533014347,
        },
        "q2.xy.y180_Square.wf.Q": {
            "type": "constant",
            "sample": 0.24999518932027404,
        },
        "q2.xy.y90_Square.wf.I": {
            "type": "constant",
            "sample": -0.0007754541766507173,
        },
        "q2.xy.y90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.12499759466013702,
        },
        "q2.xy.-y90_Square.wf.I": {
            "type": "constant",
            "sample": 0.0007754541766507173,
        },
        "q2.xy.-y90_Square.wf.Q": {
            "type": "constant",
            "sample": -0.12499759466013702,
        },
        "q2.xy.saturation.wf.I": {
            "type": "constant",
            "sample": 0.5,
        },
        "q2.xy.saturation.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q2.z.const.wf": {
            "type": "constant",
            "sample": 0.1,
        },
        "q2.resonator.readout.wf.I": {
            "type": "constant",
            "sample": 0.04,
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
        "q3.xy.x180_DragGaussian.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.000480660122228574, 0.0011444752181564196, 0.0020399750077541405, 0.0032195629569685908, 0.004736079743083251, 0.006637952541782867, 0.008963076502131798, 0.01173183579351758, 0.014939949193664433, 0.01855206761581827, 0.022497197744034744, 0.026667020055971567, 0.030917972445782062, 0.035077576527300695, 0.03895492829272023, 0.04235463582020542, 0.04509287324817859, 0.047013752401350556] + [0.04800399628122508] * 2 + [0.047013752401350556, 0.04509287324817859, 0.04235463582020542, 0.03895492829272023, 0.035077576527300695, 0.030917972445782062, 0.026667020055971567, 0.022497197744034744, 0.01855206761581827, 0.014939949193664433, 0.01173183579351758, 0.008963076502131798, 0.006637952541782867, 0.004736079743083251, 0.0032195629569685908, 0.0020399750077541405, 0.0011444752181564196, 0.000480660122228574, 0.0],
        },
        "q3.xy.x180_DragGaussian.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0004284801221367499, 0.0005990563793286867, 0.0008182212720284027, 0.0010914158521113766, 0.0014211779294034945, 0.0018056436661722673, 0.002237082254210781, 0.002700717647383079, 0.0031741309656250992, 0.003627529728213758, 0.004025101287190851, 0.00432753419293586, 0.0044956041892599465, 0.004494508740482865, 0.004298436133499548, 0.003894718433640558, 0.0032868827141328124, 0.0024960060277891397, 0.0015599949253080748, 0.00053071954709919, -0.00053071954709919, -0.0015599949253080748, -0.0024960060277891397, -0.0032868827141328124, -0.003894718433640558, -0.004298436133499548, -0.004494508740482865, -0.0044956041892599465, -0.00432753419293586, -0.004025101287190851, -0.003627529728213758, -0.0031741309656250992, -0.002700717647383079, -0.002237082254210781, -0.0018056436661722673, -0.0014211779294034945, -0.0010914158521113766, -0.0008182212720284027, -0.0005990563793286867, -0.0004284801221367499],
        },
        "q3.xy.x90_DragGaussian.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.00023277957388820845, 0.0005542595303576617, 0.0009879423964815318, 0.001559206721278647, 0.0022936427914675797, 0.0032147034728035287, 0.004340741060897647, 0.005681627434120238, 0.007235289233249289, 0.008984607198809306, 0.010895199876899318, 0.012914609052059918, 0.014973308827966401, 0.016987769401791798, 0.018865537600210893, 0.02051198679163394, 0.021838091688235334, 0.022768356983997647] + [0.02324792360028744] * 2 + [0.022768356983997647, 0.021838091688235334, 0.02051198679163394, 0.018865537600210893, 0.016987769401791798, 0.014973308827966401, 0.012914609052059918, 0.010895199876899318, 0.008984607198809306, 0.007235289233249289, 0.005681627434120238, 0.004340741060897647, 0.0032147034728035287, 0.0022936427914675797, 0.001559206721278647, 0.0009879423964815318, 0.0005542595303576617, 0.00023277957388820845, 0.0],
        },
        "q3.xy.x90_DragGaussian.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0002075092474659857, 0.0002901178655483119, 0.00039625754299306155, 0.0005285633345478704, 0.0006882642797410026, 0.0008744577379474066, 0.0010833997450706368, 0.0013079343887222622, 0.0015372043976059511, 0.0017567815288800936, 0.0019493220243546668, 0.002095787686208798, 0.0021771825436525966, 0.002176652027207082, 0.00208169574563933, 0.0018861787268598664, 0.0015918091021757527, 0.0012087943074563124, 0.0007554921600263216, 0.0002570229239219966, -0.0002570229239219966, -0.0007554921600263216, -0.0012087943074563124, -0.0015918091021757527, -0.0018861787268598664, -0.00208169574563933, -0.002176652027207082, -0.0021771825436525966, -0.002095787686208798, -0.0019493220243546668, -0.0017567815288800936, -0.0015372043976059511, -0.0013079343887222622, -0.0010833997450706368, -0.0008744577379474066, -0.0006882642797410026, -0.0005285633345478704, -0.00039625754299306155, -0.0002901178655483119, -0.0002075092474659857],
        },
        "q3.xy.-x90_DragGaussian.wf.I": {
            "type": "arbitrary",
            "samples": [-5.506444211020455e-10, -0.0002327803437411958, -0.0005542605818606819, -0.000987943799068323, -0.0015592085476442254, -0.0022936451119116327, -0.003214706347690716, -0.004340744531603708, -0.0056816315132101345, -0.007235293895001349, -0.008984612371478701, -0.010895205438221771, -0.012914614829363825, -0.014973314603855288, -0.01698777492569857, -0.018865542605289092, -0.020511991015570108, -0.021838094895802684, -0.02276835898868377, -0.023247924282239, -0.02324792291817218, -0.022768354979151202, -0.02183808848051421, -0.020511982567553336, -0.018865532594999856, -0.016987763877765405, -0.014973303051972081, -0.012914603274665072, -0.010895194315500146, -0.008984602026076646, -0.007235284571446281, -0.005681623354990335, -0.00434073759016102, -0.003214700597893705, -0.0022936404710073763, -0.0015592048949020897, -0.0009879409938877838, -0.0005542584788507386, -0.000232778804033582, 5.506444211020455e-10],
        },
        "q3.xy.-x90_DragGaussian.wf.Q": {
            "type": "arbitrary",
            "samples": [-0.0002075092474652551, -0.0002901172478457891, -0.00039625607221423383, -0.0005285607129521498, -0.000688260142243538, -0.0008744516515572268, -0.0010833912145624981, -0.0013079228701714826, -0.0015371893208919701, -0.0017567623293842471, -0.0019492981828858438, -0.0020957587748102295, -0.0021771482735701655, -0.0021766122941799396, -0.0020816506670605045, -0.0018861286654552037, -0.0015917546717713568, -0.0012087363581148463, -0.0007554317421439576, -0.0002569612334683093, 0.0002570846143738741, 0.0007555525779033658, 0.0012088522567892666, 0.0015918635325689401, 0.0018862287882512477, 0.002081740824203497, 0.002176691760218897, 0.002177216813719697, 0.0020958165975926094, 0.0019493458658097638, 0.0017568007283635697, 0.0015372194743091079, 0.0013079459072638322, 0.0010834082755711465, 0.0008744638243314289, 0.0006882684172336207, 0.0005285659561398693, 0.0003962590137690991, 0.00029011848324879186, 0.0002075092474652551],
        },
        "q3.xy.y180_DragGaussian.wf.I": {
            "type": "arbitrary",
            "samples": [-0.0004284801201488482, -0.0005990100761004718, -0.0008181110246028927, -0.0010912193427939716, -0.001420867792629912, -0.0018051874464137972, -0.002236442831139967, -0.0026998542504227717, -0.003173000860760459, -0.0036260905939645843, -0.004023314207307318, -0.004325367089909099, -0.004493035419835461, -0.004491530490445127, -0.0042950572030428825, -0.003890966012189238, -0.0032828028125722994, -0.002491662364263145, -0.0015554662339927116, -0.0005260954735401066, 0.0005353436157338054, 0.0015645236021484769, 0.002500349668155065, 0.0032909625851948294, 0.003898470818953364, 0.0043018150240716636, 0.004497486948816724, 0.0044981729169703884, 0.004329701255808074, 0.004026888329726066, 0.003628968828803622, 0.00317526104103745, 0.0027015810192838286, 0.002237721656524041, 0.001806099869176438, 0.001421488052990178, 0.0010916123513016961, 0.000818331511861759, 0.0005991026769983464, 0.0004284801201488482],
        },
        "q3.xy.y180_DragGaussian.wf.Q": {
            "type": "arbitrary",
            "samples": [4.127411677852206e-08, 0.0004807178251794809, 0.0011445540294792408, 0.0020400801308805986, 0.0032196998395463733, 0.00473625365297738, 0.006638168001949714, 0.008963336612022761, 0.011732141492950626, 0.014940298552663218, 0.01855245525485286, 0.022497614497158633, 0.026667452979393914, 0.03091840524396136, 0.035077990419136056, 0.038955303277734894, 0.042354952238580795, 0.04509311347123388, 0.04701390245254473, 0.048004047181026986, 0.04800394493600122, 0.047013601913922766, 0.04509263260671322, 0.04235431900882766, 0.038954552946248576, 0.03507716230998572, 0.03091753936071949, 0.0266665868851099, 0.022496780782162697, 0.018551679804641803, 0.014939599696040078, 0.011731529985226571, 0.008962816309073779, 0.006637737020023443, 0.004735905789243742, 0.003219426044516962, 0.0020398698656990573, 0.001144396396214183, 0.0004806024148176932, -4.127411677852206e-08],
        },
        "q3.xy.y90_DragGaussian.wf.I": {
            "type": "arbitrary",
            "samples": [-0.00020750525442386677, -0.00029155636203426086, -0.00039968834086266273, -0.0005346819960133362, -0.0006979237825791552, -0.0008886698300620687, -0.0011033217393913144, -0.001334837586791934, -0.001572421551405525, -0.001801632805668551, -0.002005021723521961, -0.002163337183555358, -0.0022572581489747547, -0.0022694990614553915, -0.002187041582030043, -0.0020031773110675806, -0.001719027318072466, -0.0013442465622450286, -0.0008967241624527762, -0.0004012395737365172, 0.00011279638246772234, 0.0006142310821533281, 0.0010732955316894543, 0.0014645296248088358, 0.0017691075522380654, 0.0019762697942764633, 0.00208372122355255, 0.0020970231485070586, 0.0020281575315555826, 0.0018935473046758368, 0.0017118626415853649, 0.0015019280838221355, 0.0012809808542250166, 0.0010634360556364493, 0.0008602119919438552, 0.0006785782887507167, 0.0005224243310910654, 0.0003928114949784337, 0.0002886682037492915, 0.00020750525442386677],
        },
        "q3.xy.y90_DragGaussian.wf.Q": {
            "type": "arbitrary",
            "samples": [-1.2873113011291672e-06, 0.00023097530969181813, 0.0005517906283633726, 0.0009846443726205065, 0.0015549069786190792, 0.002288173840302511, 0.0032079205983098634, 0.00433254358776142, 0.005671981851596691, 0.007224251578020122, 0.008972341431295133, 0.010881988725113536, 0.012900854097493725, 0.01495951754954866, 0.01697452843363662, 0.018853473414600655, 0.020501717085104246, 0.02183017254722015, 0.022763232062496946, 0.023245881771029698, 0.023249070723027305, 0.022772605655311653, 0.02184517038073101, 0.02052146708537165, 0.01887687573734711, 0.01700035658820417, 0.014986523852038467, 0.012927866982242627, 0.010907991722147835, 0.008996527189781903, 0.007246048435204648, 0.0056910543567245215, 0.004348771478713736, 0.003221362628026621, 0.0022990234707856447, 0.0015634464571849139, 0.0009912023989468997, 0.0005567071014312659, 0.00023457487946078502, 1.2873113011291672e-06],
        },
        "q3.xy.-y90_DragGaussian.wf.I": {
            "type": "arbitrary",
            "samples": [0.00020750924650326196, 0.000290140287112567, 0.0003963109311986718, 0.0005286584974200885, 0.0006884144699336614, 0.000874678673148823, 0.0010837094021258836, 0.0013083525123274236, 0.0015377516834338845, 0.0017574784729505473, 0.0019501874737244602, 0.0020968371761678237, 0.002178426556447124, 0.0021780943479548314, 0.002083332113357844, 0.0018879959748773001, 0.0015937849487322171, 0.0012108978952239343, 0.000757685359371211, 0.0002592623206945122, -0.0002547835247646035, -0.0007532989536713327, -0.0012066907084724676, -0.0015898332408491279, -0.0018843614613408605, -0.0020800593586050697, -0.0021752096862625012, -0.002175938510656316, -0.00209473817680327, -0.001948456556897404, -0.001756084568508725, -0.0015366570975145263, -0.001307516252980972, -0.0010830900779626848, -0.0008742367946320267, -0.0006881140831620417, -0.0005284681667711916, -0.00039620415111063636, -0.0002900954412920962, -0.00020750924650326196],
        },
        "q3.xy.-y90_DragGaussian.wf.Q": {
            "type": "arbitrary",
            "samples": [1.9988700688898872e-08, -0.00023275162668415762, -0.0005542213575672047, -0.0009878914770862083, -0.0015591404157528166, -0.0022935585471153554, -0.003214599097464278, -0.004340615051631695, -0.005681479333788256, -0.007235119974547953, -0.008984419385183353, -0.010894997945841563, -0.012914399271127539, -0.014973099088585785, -0.016987568799899485, -0.01886535582313455, -0.02051183336260144, -0.02183797514763798, -0.022768284104227314, -0.023247898734235987, -0.023247948250624866, -0.02276842965250378, -0.021838208026200276, -0.02051214003033876, -0.018865719202236713, -0.016987969846057122, -0.014973518428411908, -0.012914818713159559, -0.010895401706862132, -0.008984794929068425, -0.00723545842481545, -0.005681775481733243, -0.004340867029886507, -0.003214807818314024, -0.002293727014537433, -0.00155927301233683, -0.0009879933067098846, -0.000554297698005227, -0.00023280751893233221, -1.9988700688898872e-08],
        },
        "q3.xy.x180_Square.wf.I": {
            "type": "constant",
            "sample": 0.25,
        },
        "q3.xy.x180_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q3.xy.x90_Square.wf.I": {
            "type": "constant",
            "sample": 0.125,
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
            "sample": -0.0015509083533014347,
        },
        "q3.xy.y180_Square.wf.Q": {
            "type": "constant",
            "sample": 0.24999518932027404,
        },
        "q3.xy.y90_Square.wf.I": {
            "type": "constant",
            "sample": -0.0007754541766507173,
        },
        "q3.xy.y90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.12499759466013702,
        },
        "q3.xy.-y90_Square.wf.I": {
            "type": "constant",
            "sample": 0.0007754541766507173,
        },
        "q3.xy.-y90_Square.wf.Q": {
            "type": "constant",
            "sample": -0.12499759466013702,
        },
        "q3.xy.saturation.wf.I": {
            "type": "constant",
            "sample": 0.25,
        },
        "q3.xy.saturation.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q3.z.const.wf": {
            "type": "constant",
            "sample": 0.1,
        },
        "q3.resonator.readout.wf.I": {
            "type": "constant",
            "sample": 0.07,
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
        "q4.xy.x180_DragGaussian.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0006498968918466012, 0.0015474362292148176, 0.0027582346770046824, 0.004353146562558655, 0.006403617363338815, 0.008975125094896994, 0.012118907499775265, 0.01586252585821134, 0.020200191562160446, 0.025084109380546244, 0.030418289791375116, 0.036056274793159086, 0.04180395515556691, 0.04742812416579708, 0.052670661968306484, 0.05726738063316262, 0.060969730612451166, 0.06356693669118998] + [0.06490583790212616] * 2 + [0.06356693669118998, 0.060969730612451166, 0.05726738063316262, 0.052670661968306484, 0.04742812416579708, 0.04180395515556691, 0.036056274793159086, 0.030418289791375116, 0.025084109380546244, 0.020200191562160446, 0.01586252585821134, 0.012118907499775265, 0.008975125094896994, 0.006403617363338815, 0.004353146562558655, 0.0027582346770046824, 0.0015474362292148176, 0.0006498968918466012, 0.0],
        },
        "q4.xy.x180_DragGaussian.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0005793447109854115, 0.000809979569683236, 0.0011063107525303654, 0.001475695064343174, 0.0019215638584660867, 0.0024413970540909957, 0.0030247418842984384, 0.0036516197696027358, 0.0042917183129513444, 0.0049047553279782325, 0.005442308806032212, 0.005851226035371968, 0.0060784721978313335, 0.006076991049879842, 0.0058118827707409285, 0.0052660191423930655, 0.004444169093693638, 0.003374830747284554, 0.0021092572617706514, 0.00071758185909581, -0.00071758185909581, -0.0021092572617706514, -0.003374830747284554, -0.004444169093693638, -0.0052660191423930655, -0.0058118827707409285, -0.006076991049879842, -0.0060784721978313335, -0.005851226035371968, -0.005442308806032212, -0.0049047553279782325, -0.0042917183129513444, -0.0036516197696027358, -0.0030247418842984384, -0.0024413970540909957, -0.0019215638584660867, -0.001475695064343174, -0.0011063107525303654, -0.000809979569683236, -0.0005793447109854115],
        },
        "q4.xy.x90_DragGaussian.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.00032178352861017047, 0.0007661822919650029, 0.0013656850774891763, 0.0021553739970616593, 0.0031706238587934183, 0.004443854800640172, 0.006000436172417335, 0.007854014394225036, 0.010001723351844606, 0.012419898186589335, 0.015061011594537292, 0.017852547807259294, 0.020698397497482965, 0.02348309299659454, 0.02607883138852682, 0.028354805270788087, 0.030187950274913545, 0.031473905242584976] + [0.032136835565103224] * 2 + [0.031473905242584976, 0.030187950274913545, 0.028354805270788087, 0.02607883138852682, 0.02348309299659454, 0.020698397497482965, 0.017852547807259294, 0.015061011594537292, 0.012419898186589335, 0.010001723351844606, 0.007854014394225036, 0.006000436172417335, 0.004443854800640172, 0.0031706238587934183, 0.0021553739970616593, 0.0013656850774891763, 0.0007661822919650029, 0.00032178352861017047, 0.0],
        },
        "q4.xy.x90_DragGaussian.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0002868510185559214, 0.00040104528472854884, 0.0005477677800198204, 0.0007306610801102914, 0.0009514241514066799, 0.0012088092259861206, 0.001497640824068233, 0.0018080269491160678, 0.002124959020219991, 0.0024284921134518937, 0.002694651033666745, 0.002897118272112162, 0.003009634692696236, 0.003008901331727436, 0.0028776382366190734, 0.002607364710659227, 0.0022004419941841283, 0.0016709803661896084, 0.0010443568094481502, 0.0003552963948333482, -0.0003552963948333482, -0.0010443568094481502, -0.0016709803661896084, -0.0022004419941841283, -0.002607364710659227, -0.0028776382366190734, -0.003008901331727436, -0.003009634692696236, -0.002897118272112162, -0.002694651033666745, -0.0024284921134518937, -0.002124959020219991, -0.0018080269491160678, -0.001497640824068233, -0.0012088092259861206, -0.0009514241514066799, -0.0007306610801102914, -0.0005477677800198204, -0.00040104528472854884, -0.0002868510185559214],
        },
        "q4.xy.-x90_DragGaussian.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.00032178352861017047, 0.0007661822919650029, 0.0013656850774891763, 0.0021553739970616593, 0.0031706238587934183, 0.004443854800640172, 0.006000436172417335, 0.007854014394225036, 0.010001723351844606, 0.012419898186589335, 0.015061011594537292, 0.017852547807259294, 0.020698397497482965, 0.02348309299659454, 0.02607883138852682, 0.028354805270788087, 0.030187950274913545, 0.031473905242584976] + [0.032136835565103224] * 2 + [0.031473905242584976, 0.030187950274913545, 0.028354805270788087, 0.02607883138852682, 0.02348309299659454, 0.020698397497482965, 0.017852547807259294, 0.015061011594537292, 0.012419898186589335, 0.010001723351844606, 0.007854014394225036, 0.006000436172417335, 0.004443854800640172, 0.0031706238587934183, 0.0021553739970616593, 0.0013656850774891763, 0.0007661822919650029, 0.00032178352861017047, 0.0],
        },
        "q4.xy.-x90_DragGaussian.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0002868510185559214, 0.00040104528472854884, 0.0005477677800198204, 0.0007306610801102914, 0.0009514241514066799, 0.0012088092259861206, 0.001497640824068233, 0.0018080269491160678, 0.002124959020219991, 0.0024284921134518937, 0.002694651033666745, 0.002897118272112162, 0.003009634692696236, 0.003008901331727436, 0.0028776382366190734, 0.002607364710659227, 0.0022004419941841283, 0.0016709803661896084, 0.0010443568094481502, 0.0003552963948333482, -0.0003552963948333482, -0.0010443568094481502, -0.0016709803661896084, -0.0022004419941841283, -0.002607364710659227, -0.0028776382366190734, -0.003008901331727436, -0.003009634692696236, -0.002897118272112162, -0.002694651033666745, -0.0024284921134518937, -0.002124959020219991, -0.0018080269491160678, -0.001497640824068233, -0.0012088092259861206, -0.0009514241514066799, -0.0007306610801102914, -0.0005477677800198204, -0.00040104528472854884, -0.0002868510185559214],
        },
        "q4.xy.y180_DragGaussian.wf.I": {
            "type": "arbitrary",
            "samples": [-0.0005793335628179895, -0.0008139957055474568, -0.0011158891911998963, -0.001492777744761592, -0.0019485322078209729, -0.0024810757696143446, -0.0030803620659670067, -0.003726730762007121, -0.004390041024054074, -0.005029975530478339, -0.005597816700307333, -0.006039817360796476, -0.006302035142562035, -0.006336210525056517, -0.006105997630115078, -0.005592667288349217, -0.0047993494117796656, -0.0037529996643866905, -0.0025035626463586675, -0.0011202200755915503, 0.0003149160261480596, 0.0017148707014934673, 0.002996531948343581, 0.0040888177398143485, 0.0049391683313847155, 0.005517544238513859, 0.005817537699042059, 0.005854675320436897, 0.005662409522951777, 0.005286591462120006, 0.0047793463638219884, 0.004193230433190394, 0.00357636824301281, 0.0029690052941141977, 0.002401624380333158, 0.0018945215568848318, 0.0014585555911541342, 0.001096689737007172, 0.0008059322614006606, 0.0005793335628179895],
        },
        "q4.xy.y180_DragGaussian.wf.Q": {
            "type": "arbitrary",
            "samples": [-3.5940422068331202e-06, 0.0006448595697408939, 0.001540543305984651, 0.0027490269298612595, 0.004341142118425015, 0.0063883486079902635, 0.008956187999267909, 0.012096020988629795, 0.015835596372958855, 0.02016937555151617, 0.025049864605326398, 0.03038140559943387, 0.03601787235917081, 0.04176545130907999, 0.04739115672958542, 0.05263697998925742, 0.05723870865717116, 0.06094762117627558, 0.06355262843166949, 0.06490013732253438, 0.06490904055212998, 0.06357879854932182, 0.06098949360185111, 0.05729384864893831, 0.05270231689387008, 0.04746326630988582, 0.04184085015853757, 0.03609328958562623, 0.030454003322116376, 0.025117388782834565, 0.020230230159588657, 0.015888844867211437, 0.012141327609459854, 0.008993716778907423, 0.006418639672669586, 0.004364983473940993, 0.002767336272278984, 0.0015542695986842233, 0.0006549092023858959, 3.5940422068331202e-06],
        },
        "q4.xy.y90_DragGaussian.wf.I": {
            "type": "arbitrary",
            "samples": [-0.0002868454987624041, -0.0004030337945767724, -0.0005525103535454456, -0.0007391192297831412, -0.0009647769935653026, -0.0012284553533210949, -0.0015251800515115226, -0.001845216664094732, -0.0021736415563546963, -0.0024904924078359373, -0.002771647676633299, -0.0029904955184441714, -0.003120327441229808, -0.0031372487026000992, -0.0030232633633944708, -0.0027690980476522435, -0.0023763024691001735, -0.001858223188985775, -0.0012395892833906021, -0.0005546547048710677, 0.00015592441105832198, 0.0008490841429766593, 0.001483673234982481, 0.002024496834294567, 0.0024455310280937963, 0.002731902362676288, 0.0028804381619697006, 0.0028988261170538746, 0.00280362952891507, 0.0026175506858754213, 0.002366398357485651, 0.0020761947041070695, 0.0017707676514286989, 0.0014700439592621505, 0.0011891165770988583, 0.0009380346932730496, 0.0007221748106258845, 0.0005430041254113643, 0.0003990413404769618, 0.0002868454987624041],
        },
        "q4.xy.y90_DragGaussian.wf.Q": {
            "type": "arbitrary",
            "samples": [-1.7795185633256134e-06, 0.00031928939869163087, 0.0007627693980317209, 0.0013611260445048178, 0.002149430235149904, 0.003163063838065235, 0.004434478474134223, 0.005989104371317257, 0.007840680794854251, 0.009986465416674875, 0.012402942566790332, 0.015042749120009887, 0.01783353360535897, 0.020679333083199615, 0.023464789305321206, 0.02606215442606561, 0.028340608911761746, 0.030177003227039617, 0.03146682079227518, 0.03213401303642341, 0.032138421293596564, 0.03147977840587199, 0.030197735526304628, 0.02836791038271963, 0.02609450469574453, 0.02350049293075282, 0.020716665324876704, 0.017870874946041275, 0.015078694439439653, 0.0124363758211691, 0.01001659636631231, 0.007867045728413312, 0.006011537044104282, 0.004453060103448565, 0.0031780618566742726, 0.002161234808461499, 0.0013701915514854203, 0.0007695656990373379, 0.0003242652745487322, 1.7795185633256134e-06],
        },
        "q4.xy.-y90_DragGaussian.wf.I": {
            "type": "arbitrary",
            "samples": [-0.0002868454987624041, -0.0004030337945767724, -0.0005525103535454456, -0.0007391192297831412, -0.0009647769935653026, -0.0012284553533210949, -0.0015251800515115226, -0.001845216664094732, -0.0021736415563546963, -0.0024904924078359373, -0.002771647676633299, -0.0029904955184441714, -0.003120327441229808, -0.0031372487026000992, -0.0030232633633944708, -0.0027690980476522435, -0.0023763024691001735, -0.001858223188985775, -0.0012395892833906021, -0.0005546547048710677, 0.00015592441105832198, 0.0008490841429766593, 0.001483673234982481, 0.002024496834294567, 0.0024455310280937963, 0.002731902362676288, 0.0028804381619697006, 0.0028988261170538746, 0.00280362952891507, 0.0026175506858754213, 0.002366398357485651, 0.0020761947041070695, 0.0017707676514286989, 0.0014700439592621505, 0.0011891165770988583, 0.0009380346932730496, 0.0007221748106258845, 0.0005430041254113643, 0.0003990413404769618, 0.0002868454987624041],
        },
        "q4.xy.-y90_DragGaussian.wf.Q": {
            "type": "arbitrary",
            "samples": [-1.7795185633256134e-06, 0.00031928939869163087, 0.0007627693980317209, 0.0013611260445048178, 0.002149430235149904, 0.003163063838065235, 0.004434478474134223, 0.005989104371317257, 0.007840680794854251, 0.009986465416674875, 0.012402942566790332, 0.015042749120009887, 0.01783353360535897, 0.020679333083199615, 0.023464789305321206, 0.02606215442606561, 0.028340608911761746, 0.030177003227039617, 0.03146682079227518, 0.03213401303642341, 0.032138421293596564, 0.03147977840587199, 0.030197735526304628, 0.02836791038271963, 0.02609450469574453, 0.02350049293075282, 0.020716665324876704, 0.017870874946041275, 0.015078694439439653, 0.0124363758211691, 0.01001659636631231, 0.007867045728413312, 0.006011537044104282, 0.004453060103448565, 0.0031780618566742726, 0.002161234808461499, 0.0013701915514854203, 0.0007695656990373379, 0.0003242652745487322, 1.7795185633256134e-06],
        },
        "q4.xy.x180_Square.wf.I": {
            "type": "constant",
            "sample": 0.25,
        },
        "q4.xy.x180_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q4.xy.x90_Square.wf.I": {
            "type": "constant",
            "sample": 0.125,
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
            "sample": -0.0015509083533014347,
        },
        "q4.xy.y180_Square.wf.Q": {
            "type": "constant",
            "sample": 0.24999518932027404,
        },
        "q4.xy.y90_Square.wf.I": {
            "type": "constant",
            "sample": -0.0007754541766507173,
        },
        "q4.xy.y90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.12499759466013702,
        },
        "q4.xy.-y90_Square.wf.I": {
            "type": "constant",
            "sample": 0.0007754541766507173,
        },
        "q4.xy.-y90_Square.wf.Q": {
            "type": "constant",
            "sample": -0.12499759466013702,
        },
        "q4.xy.saturation.wf.I": {
            "type": "constant",
            "sample": 0.25,
        },
        "q4.xy.saturation.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q4.z.const.wf": {
            "type": "constant",
            "sample": 0.25,
        },
        "q4.resonator.readout.wf.I": {
            "type": "constant",
            "sample": 0.04,
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
        "q5.xy.x180_DragGaussian.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0007836916625405736, 0.0018660081104605744, 0.0033260745616999774, 0.005249332178218227, 0.007721934972622112, 0.010822840969655936, 0.014613836265147194, 0.019128156201197406, 0.024358820464591792, 0.03024819418343967, 0.036680526399363776, 0.043479207689979656, 0.05041016740909522, 0.05719218839939841, 0.06351401147306555, 0.06905706012876321, 0.07352161573285519, 0.07665351061547873] + [0.07826805244379051] * 2 + [0.07665351061547873, 0.07352161573285519, 0.06905706012876321, 0.06351401147306555, 0.05719218839939841, 0.05041016740909522, 0.043479207689979656, 0.036680526399363776, 0.03024819418343967, 0.024358820464591792, 0.019128156201197406, 0.014613836265147194, 0.010822840969655936, 0.007721934972622112, 0.005249332178218227, 0.0033260745616999774, 0.0018660081104605744, 0.0007836916625405736, 0.0],
        },
        "q5.xy.x180_DragGaussian.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0006986148501898236, 0.0009767306838248163, 0.0013340677941596922, 0.0017794975370508362, 0.0023171576811827806, 0.002944009334782045, 0.003647447811800682, 0.004403381527298437, 0.005175257647833994, 0.005914501062493579, 0.006562721086632465, 0.007055822419048745, 0.007329851922956238, 0.007328065849941987, 0.007008379526406399, 0.006350138534970269, 0.005359093587526005, 0.004069609737042336, 0.002543491669126166, 0.0008653109858178682, -0.0008653109858178682, -0.002543491669126166, -0.004069609737042336, -0.005359093587526005, -0.006350138534970269, -0.007008379526406399, -0.007328065849941987, -0.007329851922956238, -0.007055822419048745, -0.006562721086632465, -0.005914501062493579, -0.005175257647833994, -0.004403381527298437, -0.003647447811800682, -0.002944009334782045, -0.0023171576811827806, -0.0017794975370508362, -0.0013340677941596922, -0.0009767306838248163, -0.0006986148501898236],
        },
        "q5.xy.x90_DragGaussian.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.00034721322995930233, 0.0008267316524242431, 0.0014736115577770744, 0.002325707504428234, 0.003421189878029372, 0.004795040894307784, 0.006474634775708675, 0.008474696382826405, 0.010792133100014693, 0.013401409897383625, 0.016251243513862423, 0.019263387451601974, 0.02233413711734484, 0.025338899737966752, 0.0281397724709028, 0.030595610550546413, 0.03257362415682161, 0.033961204745038505] + [0.03467652469790774] * 2 + [0.033961204745038505, 0.03257362415682161, 0.030595610550546413, 0.0281397724709028, 0.025338899737966752, 0.02233413711734484, 0.019263387451601974, 0.016251243513862423, 0.013401409897383625, 0.010792133100014693, 0.008474696382826405, 0.006474634775708675, 0.004795040894307784, 0.003421189878029372, 0.002325707504428234, 0.0014736115577770744, 0.0008267316524242431, 0.00034721322995930233, 0.0],
        },
        "q5.xy.x90_DragGaussian.wf.Q": {
            "type": "arbitrary",
            "samples": [0.00030952009601018876, 0.0004327388330657594, 0.0005910564191703228, 0.0007884032931281259, 0.0010266126861683022, 0.0013043382225686104, 0.0016159954180675464, 0.0019509105378000123, 0.0022928889123954308, 0.002620409423329551, 0.002907602179184481, 0.0031260698680845513, 0.0032474781638515615, 0.0032466868473046803, 0.003105050376899, 0.0028134178488876155, 0.002374337106186521, 0.0018030335258276927, 0.0011268895664258156, 0.0003833745293794487, -0.0003833745293794487, -0.0011268895664258156, -0.0018030335258276927, -0.002374337106186521, -0.0028134178488876155, -0.003105050376899, -0.0032466868473046803, -0.0032474781638515615, -0.0031260698680845513, -0.002907602179184481, -0.002620409423329551, -0.0022928889123954308, -0.0019509105378000123, -0.0016159954180675464, -0.0013043382225686104, -0.0010266126861683022, -0.0007884032931281259, -0.0005910564191703228, -0.0004327388330657594, -0.00030952009601018876],
        },
        "q5.xy.-x90_DragGaussian.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -0.0004890327182525387, -0.0011644107780623145, -0.002075509236305739, -0.003275644372434133, -0.004818577292999117, -0.00675357872437716, -0.009119203909448838, -0.011936192088487896, -0.01520018746480943, -0.018875225207582575, -0.022889075371637223, -0.027131531621974618, -0.03145653115118992, -0.03568859118023487, -0.03963348235338423, -0.04309240922612172, -0.04587834388284734, -0.04783268273949085] + [-0.048840175630855964] * 2 + [-0.04783268273949085, -0.04587834388284734, -0.04309240922612172, -0.03963348235338423, -0.03568859118023487, -0.03145653115118992, -0.027131531621974618, -0.022889075371637223, -0.018875225207582575, -0.01520018746480943, -0.011936192088487896, -0.009119203909448838, -0.00675357872437716, -0.004818577292999117, -0.003275644372434133, -0.002075509236305739, -0.0011644107780623145, -0.0004890327182525387, 0.0],
        },
        "q5.xy.-x90_DragGaussian.wf.Q": {
            "type": "arbitrary",
            "samples": [-0.000435943797197449, -0.0006094913141771259, -0.0008324738298173561, -0.0011104271734198958, -0.0014459333608004257, -0.0018370960881248035, -0.002276049884602178, -0.002747761320845089, -0.0032294210033738465, -0.0036907174976472555, -0.004095214336879552, -0.00440291530716134, -0.004573912906833186, -0.0045727983764854655, -0.004373310389998592, -0.003962560350545937, -0.0033441367692767913, -0.0025394838391939335, -0.0015871684034166418, -0.0005399641258865475, 0.0005399641258865475, 0.0015871684034166418, 0.0025394838391939335, 0.0033441367692767913, 0.003962560350545937, 0.004373310389998592, 0.0045727983764854655, 0.004573912906833186, 0.00440291530716134, 0.004095214336879552, 0.0036907174976472555, 0.0032294210033738465, 0.002747761320845089, 0.002276049884602178, 0.0018370960881248035, 0.0014459333608004257, 0.0011104271734198958, 0.0008324738298173561, 0.0006094913141771259, 0.000435943797197449],
        },
        "q5.xy.y180_DragGaussian.wf.I": {
            "type": "arbitrary",
            "samples": [-0.0006986014069406393, -0.0009815736246542102, -0.0013456181533314966, -0.0018000970419657161, -0.0023496780252666763, -0.002991856737848726, -0.0037145185628528928, -0.004493955677215065, -0.005293822130748588, -0.006065500443952598, -0.006750243510160872, -0.007283239185026368, -0.007599439942281348, -0.007640651036935086, -0.007363044037058067, -0.006744033984820482, -0.0057873951496270745, -0.004525632578639331, -0.0030189730051246476, -0.0013508406402086416, 0.0003797480295549658, 0.002067912445737238, 0.0036134302747329043, 0.004930585778361967, 0.005955998697258397, 0.006653445295200335, 0.007015198639126369, 0.007059981811070808, 0.006828134106656232, 0.006374946093909828, 0.005763274058871755, 0.005056493992863055, 0.004312637911315896, 0.003580236687122554, 0.0028960486302272046, 0.0022845481602710546, 0.001758829547394165, 0.0013224660928047643, 0.0009718501530874353, 0.0006986014069406393],
        },
        "q5.xy.y180_DragGaussian.wf.Q": {
            "type": "arbitrary",
            "samples": [-4.333950427599311e-06, 0.0007776173030763251, 0.0018576961358477018, 0.0033149712086025674, 0.0052348563699800375, 0.007703522826919997, 0.010800005279651205, 0.014586238090429995, 0.019095682722198425, 0.024321660338243036, 0.030206899410127063, 0.03663604883058857, 0.04343289931750481, 0.050363736746252996, 0.0571476104487911, 0.0634733953592023, 0.06902248543112276, 0.07349495461012687, 0.07663625670361617, 0.07826117828151374, 0.07827191442580261, 0.07666781448342576, 0.07354544734401372, 0.06908897713521091, 0.06355218322239034, 0.05723456528359598, 0.050454658014574744, 0.04352384274611101, 0.036723592302021484, 0.03028832484175623, 0.02439504313107049, 0.01915989352473053, 0.014640872019977678, 0.010845260137887626, 0.007740049936276083, 0.005263605963609341, 0.0033370499093616996, 0.0018742482709343633, 0.0007897358612880829, 4.333950427599311e-06],
        },
        "q5.xy.y90_DragGaussian.wf.I": {
            "type": "arbitrary",
            "samples": [-0.00043593540845350163, -0.0006125133656181951, -0.0008396813883669383, -0.001123281504229698, -0.0014662264339898217, -0.0018669534245001442, -0.0023179028138472987, -0.0028042806445208704, -0.003303406620599842, -0.0037849428690515776, -0.004212230511600758, -0.0045448260158726, -0.0047421389684343595, -0.004767855171124772, -0.0045946251723320225, -0.004208355695520126, -0.003611401928723668, -0.0028240473996744295, -0.0018838742908671767, -0.0008429402809590696, 0.00023696719005824012, 0.001290401433095227, 0.0022548225455660802, 0.00307674290926226, 0.003716612504701818, 0.004151827298900133, 0.0043775655956986344, 0.004405510816191299, 0.004260835150326854, 0.003978040556041674, 0.003596350087364212, 0.003155311100466671, 0.0026911362483718836, 0.002234109360580776, 0.0018071680503022167, 0.0014255846402325984, 0.001097530107334171, 0.0008252342331479699, 0.0006064458061959906, 0.00043593540845350163],
        },
        "q5.xy.y90_DragGaussian.wf.Q": {
            "type": "arbitrary",
            "samples": [-2.704435506573881e-06, 0.00048524224725171876, 0.0011592240091667493, 0.002068580614748963, 0.003266611299619915, 0.004807087899795191, 0.006739328988045931, 0.009101982327229873, 0.011915928259656917, 0.01517699911348765, 0.018849456788435155, 0.022861320851078854, 0.02710263465860026, 0.03142755787720306, 0.035660774020245, 0.03960813742563163, 0.043070834212403875, 0.045861707031975105, 0.04782191609768266, 0.04883588607359181, 0.048842585552578366, 0.047841608519562304, 0.045893215085569344, 0.04311232580960431, 0.039657301969216616, 0.03571503484916843, 0.0314842938068035, 0.02715938441647611, 0.0229159489961089, 0.018900267205424166, 0.015222790830261866, 0.011955996547740592, 0.009136074535112892, 0.006767568546274413, 0.004829881241146312, 0.0032845513806405756, 0.0020823579809808816, 0.0011695527340992978, 0.0004928043686150945, 2.704435506573881e-06],
        },
        "q5.xy.-y90_DragGaussian.wf.I": {
            "type": "arbitrary",
            "samples": [0.00043593540845350163, 0.0006125133656181951, 0.0008396813883669383, 0.001123281504229698, 0.0014662264339898217, 0.0018669534245001442, 0.0023179028138472987, 0.0028042806445208704, 0.003303406620599842, 0.0037849428690515776, 0.004212230511600758, 0.0045448260158726, 0.0047421389684343595, 0.004767855171124772, 0.0045946251723320225, 0.004208355695520126, 0.003611401928723668, 0.0028240473996744295, 0.0018838742908671767, 0.0008429402809590696, -0.00023696719005824012, -0.001290401433095227, -0.0022548225455660802, -0.00307674290926226, -0.003716612504701818, -0.004151827298900133, -0.0043775655956986344, -0.004405510816191299, -0.004260835150326854, -0.003978040556041674, -0.003596350087364212, -0.003155311100466671, -0.0026911362483718836, -0.002234109360580776, -0.0018071680503022167, -0.0014255846402325984, -0.001097530107334171, -0.0008252342331479699, -0.0006064458061959906, -0.00043593540845350163],
        },
        "q5.xy.-y90_DragGaussian.wf.Q": {
            "type": "arbitrary",
            "samples": [2.704435506573881e-06, -0.00048524224725171876, -0.0011592240091667493, -0.002068580614748963, -0.003266611299619915, -0.004807087899795191, -0.006739328988045931, -0.009101982327229873, -0.011915928259656917, -0.01517699911348765, -0.018849456788435155, -0.022861320851078854, -0.02710263465860026, -0.03142755787720306, -0.035660774020245, -0.03960813742563163, -0.043070834212403875, -0.045861707031975105, -0.04782191609768266, -0.04883588607359181, -0.048842585552578366, -0.047841608519562304, -0.045893215085569344, -0.04311232580960431, -0.039657301969216616, -0.03571503484916843, -0.0314842938068035, -0.02715938441647611, -0.0229159489961089, -0.018900267205424166, -0.015222790830261866, -0.011955996547740592, -0.009136074535112892, -0.006767568546274413, -0.004829881241146312, -0.0032845513806405756, -0.0020823579809808816, -0.0011695527340992978, -0.0004928043686150945, -2.704435506573881e-06],
        },
        "q5.xy.x180_Square.wf.I": {
            "type": "constant",
            "sample": 0.25,
        },
        "q5.xy.x180_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q5.xy.x90_Square.wf.I": {
            "type": "constant",
            "sample": 0.125,
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
            "sample": -0.0015509083533014347,
        },
        "q5.xy.y180_Square.wf.Q": {
            "type": "constant",
            "sample": 0.24999518932027404,
        },
        "q5.xy.y90_Square.wf.I": {
            "type": "constant",
            "sample": -0.0007754541766507173,
        },
        "q5.xy.y90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.12499759466013702,
        },
        "q5.xy.-y90_Square.wf.I": {
            "type": "constant",
            "sample": 0.0007754541766507173,
        },
        "q5.xy.-y90_Square.wf.Q": {
            "type": "constant",
            "sample": -0.12499759466013702,
        },
        "q5.xy.saturation.wf.I": {
            "type": "constant",
            "sample": 0.25,
        },
        "q5.xy.saturation.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q5.z.const.wf": {
            "type": "constant",
            "sample": 0.1,
        },
        "q5.resonator.readout.wf.I": {
            "type": "constant",
            "sample": 0.04,
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
        "coupler_q1_q2.const.wf": {
            "type": "constant",
            "sample": -0.0394572,
        },
        "coupler_q2_q3.const.wf": {
            "type": "constant",
            "sample": -0.0394572,
        },
        "coupler_q3_q4.const.wf": {
            "type": "constant",
            "sample": -0.0394572,
        },
        "coupler_q4_q5.const.wf": {
            "type": "constant",
            "sample": -0.0394572,
        },
    },
    "digital_waveforms": {
        "ON": {
            "samples": [[1, 0]],
        },
    },
    "integration_weights": {
        "q1.resonator.readout.iw1": {
            "cosine": [(-0.029060953277058484, 1024)],
            "sine": [(-0.9995776413038803, 1024)],
        },
        "q1.resonator.readout.iw2": {
            "cosine": [(0.9995776413038803, 1024)],
            "sine": [(-0.029060953277058484, 1024)],
        },
        "q1.resonator.readout.iw3": {
            "cosine": [(-0.9995776413038803, 1024)],
            "sine": [(0.029060953277058484, 1024)],
        },
        "q2.resonator.readout.iw1": {
            "cosine": [(-0.8801804205828955, 1024)],
            "sine": [(0.4746392600939341, 1024)],
        },
        "q2.resonator.readout.iw2": {
            "cosine": [(-0.4746392600939341, 1024)],
            "sine": [(-0.8801804205828955, 1024)],
        },
        "q2.resonator.readout.iw3": {
            "cosine": [(0.4746392600939341, 1024)],
            "sine": [(0.8801804205828955, 1024)],
        },
        "q3.resonator.readout.iw1": {
            "cosine": [(0.9989571756591297, 1024)],
            "sine": [(-0.04565699507342608, 1024)],
        },
        "q3.resonator.readout.iw2": {
            "cosine": [(0.04565699507342608, 1024)],
            "sine": [(0.9989571756591297, 1024)],
        },
        "q3.resonator.readout.iw3": {
            "cosine": [(-0.04565699507342608, 1024)],
            "sine": [(-0.9989571756591297, 1024)],
        },
        "q4.resonator.readout.iw1": {
            "cosine": [(-0.6759890289182044, 1024)],
            "sine": [(0.7369116858770954, 1024)],
        },
        "q4.resonator.readout.iw2": {
            "cosine": [(-0.7369116858770954, 1024)],
            "sine": [(-0.6759890289182044, 1024)],
        },
        "q4.resonator.readout.iw3": {
            "cosine": [(0.7369116858770954, 1024)],
            "sine": [(0.6759890289182044, 1024)],
        },
        "q5.resonator.readout.iw1": {
            "cosine": [(-0.7244823567994584, 1024)],
            "sine": [(0.6892933444378396, 1024)],
        },
        "q5.resonator.readout.iw2": {
            "cosine": [(-0.6892933444378396, 1024)],
            "sine": [(-0.7244823567994584, 1024)],
        },
        "q5.resonator.readout.iw3": {
            "cosine": [(0.6892933444378396, 1024)],
            "sine": [(0.7244823567994584, 1024)],
        },
    },
    "mixers": {},
    "oscillators": {},
    "octaves": {
        "octave1": {
            "RF_outputs": {
                "1": {
                    "LO_frequency": 6200000000,
                    "LO_source": "internal",
                    "gain": 0,
                    "output_mode": "always_on",
                    "input_attenuators": "off",
                    "I_connection": ('con1', 1, 1),
                    "Q_connection": ('con1', 1, 2),
                },
                "2": {
                    "LO_frequency": 4700000000,
                    "LO_source": "internal",
                    "gain": 0,
                    "output_mode": "always_on",
                    "input_attenuators": "off",
                    "I_connection": ('con1', 1, 3),
                    "Q_connection": ('con1', 1, 4),
                },
                "3": {
                    "LO_frequency": 4700000000,
                    "LO_source": "internal",
                    "gain": 0,
                    "output_mode": "always_on",
                    "input_attenuators": "off",
                    "I_connection": ('con1', 1, 5),
                    "Q_connection": ('con1', 1, 6),
                },
                "4": {
                    "LO_frequency": 4700000000,
                    "LO_source": "internal",
                    "gain": 0,
                    "output_mode": "always_on",
                    "input_attenuators": "off",
                    "I_connection": ('con1', 1, 7),
                    "Q_connection": ('con1', 1, 8),
                },
            },
            "IF_outputs": {
                "IF_out1": {
                    "port": ('con1', 1, 1),
                    "name": "out1",
                },
                "IF_out2": {
                    "port": ('con1', 1, 2),
                    "name": "out2",
                },
            },
            "RF_inputs": {
                "1": {
                    "RF_source": "RF_in",
                    "LO_frequency": 6200000000,
                    "LO_source": "internal",
                    "IF_mode_I": "direct",
                    "IF_mode_Q": "direct",
                },
            },
            "loopbacks": [],
        },
        "octave2": {
            "RF_outputs": {
                "1": {
                    "LO_frequency": 4700000000,
                    "LO_source": "internal",
                    "gain": 0,
                    "output_mode": "always_on",
                    "input_attenuators": "off",
                    "I_connection": ('con1', 2, 1),
                    "Q_connection": ('con1', 2, 2),
                },
                "2": {
                    "LO_frequency": 4700000000,
                    "LO_source": "internal",
                    "gain": 0,
                    "output_mode": "always_on",
                    "input_attenuators": "off",
                    "I_connection": ('con1', 2, 3),
                    "Q_connection": ('con1', 2, 4),
                },
            },
            "IF_outputs": {},
            "RF_inputs": {},
            "loopbacks": [],
        },
        "octave3": {
            "RF_outputs": {},
            "IF_outputs": {},
            "RF_inputs": {},
            "loopbacks": [],
        },
    },
}

loaded_config = {
    "version": 1,
    "controllers": {
        "con1": {
            "type": "opx1000",
            "fems": {
                "1": {
                    "type": "LF",
                    "analog_outputs": {
                        "3": {
                            "offset": 0.0,
                            "delay": 0,
                            "shareable": False,
                            "filter": {
                                "feedforward": [],
                                "feedback": [],
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
                                "feedback": [],
                            },
                            "crosstalk": {},
                            "output_mode": "direct",
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "mw",
                        },
                        "1": {
                            "offset": 0.0,
                            "delay": 0,
                            "shareable": False,
                            "filter": {
                                "feedforward": [],
                                "feedback": [],
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
                                "feedback": [],
                            },
                            "crosstalk": {},
                            "output_mode": "direct",
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "mw",
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
                            "output_mode": "direct",
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "mw",
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
                            "output_mode": "direct",
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "mw",
                        },
                        "7": {
                            "offset": 0.0,
                            "delay": 0,
                            "shareable": False,
                            "filter": {
                                "feedforward": [],
                                "feedback": [],
                            },
                            "crosstalk": {},
                            "output_mode": "direct",
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "mw",
                        },
                        "8": {
                            "offset": 0.0,
                            "delay": 0,
                            "shareable": False,
                            "filter": {
                                "feedforward": [],
                                "feedback": [],
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
                        },
                        "2": {
                            "offset": 0.0,
                            "gain_db": 0,
                            "shareable": False,
                        },
                    },
                    "digital_outputs": {
                        "3": {
                            "shareable": False,
                            "inverted": False,
                            "level": "LVTTL",
                        },
                        "1": {
                            "shareable": False,
                            "inverted": False,
                            "level": "LVTTL",
                        },
                        "5": {
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
                "2": {
                    "type": "LF",
                    "analog_outputs": {
                        "5": {
                            "offset": 0.0,
                            "delay": 0,
                            "shareable": False,
                            "filter": {
                                "feedforward": [],
                                "feedback": [],
                            },
                            "crosstalk": {},
                            "output_mode": "amplified",
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "pulse",
                        },
                        "1": {
                            "offset": 0.0,
                            "delay": 0,
                            "shareable": False,
                            "filter": {
                                "feedforward": [],
                                "feedback": [],
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
                                "feedback": [],
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
                                "feedback": [],
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
                                "feedback": [],
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
                        "3": {
                            "shareable": False,
                            "inverted": False,
                            "level": "LVTTL",
                        },
                    },
                },
                "3": {
                    "type": "LF",
                    "analog_outputs": {
                        "1": {
                            "offset": 0.0,
                            "delay": 0,
                            "shareable": False,
                            "filter": {
                                "feedforward": [],
                                "feedback": [],
                            },
                            "crosstalk": {
                                "8": 0.408,
                            },
                            "output_mode": "amplified",
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "pulse",
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
                            "output_mode": "amplified",
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "pulse",
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
                            "output_mode": "amplified",
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "pulse",
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
                            "output_mode": "amplified",
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "pulse",
                        },
                        "5": {
                            "offset": 0.0,
                            "delay": 0,
                            "shareable": False,
                            "filter": {
                                "feedforward": [],
                                "feedback": [],
                            },
                            "crosstalk": {
                                "8": 0.427,
                                "1": 0.374,
                            },
                            "output_mode": "amplified",
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "pulse",
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
                            "output_mode": "amplified",
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "pulse",
                        },
                        "7": {
                            "offset": 0.0,
                            "delay": 0,
                            "shareable": False,
                            "filter": {
                                "feedforward": [],
                                "feedback": [],
                            },
                            "crosstalk": {},
                            "output_mode": "amplified",
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "pulse",
                        },
                        "8": {
                            "offset": 0.0,
                            "delay": 0,
                            "shareable": False,
                            "filter": {
                                "feedforward": [],
                                "feedback": [],
                            },
                            "crosstalk": {
                                "1": 0.177,
                            },
                            "output_mode": "amplified",
                            "sampling_rate": 1000000000.0,
                            "upsampling_mode": "pulse",
                        },
                    },
                },
            },
        },
    },
    "oscillators": {},
    "elements": {
        "q1.xy": {
            "digitalInputs": {
                "octave_switch": {
                    "delay": 87,
                    "buffer": 15,
                    "port": ('con1', 1, 3),
                },
            },
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "x180_DragGaussian": "q1.xy.x180_DragGaussian.pulse",
                "x90_DragGaussian": "q1.xy.x90_DragGaussian.pulse",
                "-x90_DragGaussian": "q1.xy.-x90_DragGaussian.pulse",
                "y180_DragGaussian": "q1.xy.y180_DragGaussian.pulse",
                "y90_DragGaussian": "q1.xy.y90_DragGaussian.pulse",
                "-y90_DragGaussian": "q1.xy.-y90_DragGaussian.pulse",
                "x180_Square": "q1.xy.x180_Square.pulse",
                "x90_Square": "q1.xy.x90_Square.pulse",
                "-x90_Square": "q1.xy.-x90_Square.pulse",
                "y180_Square": "q1.xy.y180_Square.pulse",
                "y90_Square": "q1.xy.y90_Square.pulse",
                "-y90_Square": "q1.xy.-y90_Square.pulse",
                "x180": "q1.xy.x180_DragGaussian.pulse",
                "x90": "q1.xy.x90_DragGaussian.pulse",
                "-x90": "q1.xy.-x90_DragGaussian.pulse",
                "y180": "q1.xy.y180_DragGaussian.pulse",
                "y90": "q1.xy.y90_DragGaussian.pulse",
                "-y90": "q1.xy.-y90_DragGaussian.pulse",
                "saturation": "q1.xy.saturation.pulse",
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
                "mixer": "q1.xy_mixer_1a7",
                "lo_frequency": 4700000000.0,
            },
            "intermediate_frequency": 385991173.03796864,
        },
        "q1.z": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "q1.z.const.pulse",
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
                "port": ('con1', 2, 5),
            },
        },
        "q1.resonator": {
            "digitalInputs": {
                "octave_switch": {
                    "delay": 87,
                    "buffer": 15,
                    "port": ('con1', 1, 1),
                },
            },
            "digitalOutputs": {},
            "outputs": {
                "out1": ('con1', 1, 1),
                "out2": ('con1', 1, 2),
            },
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
            "mixInputs": {
                "I": ('con1', 1, 1),
                "Q": ('con1', 1, 2),
                "mixer": "q1.resonator_mixer_e75",
                "lo_frequency": 6200000000.0,
            },
            "smearing": 0,
            "time_of_flight": 264,
            "intermediate_frequency": -287531678.0,
        },
        "q2.xy": {
            "digitalInputs": {
                "octave_switch": {
                    "delay": 87,
                    "buffer": 15,
                    "port": ('con1', 1, 5),
                },
            },
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "x180_DragGaussian": "q2.xy.x180_DragGaussian.pulse",
                "x90_DragGaussian": "q2.xy.x90_DragGaussian.pulse",
                "-x90_DragGaussian": "q2.xy.-x90_DragGaussian.pulse",
                "y180_DragGaussian": "q2.xy.y180_DragGaussian.pulse",
                "y90_DragGaussian": "q2.xy.y90_DragGaussian.pulse",
                "-y90_DragGaussian": "q2.xy.-y90_DragGaussian.pulse",
                "x180_Square": "q2.xy.x180_Square.pulse",
                "x90_Square": "q2.xy.x90_Square.pulse",
                "-x90_Square": "q2.xy.-x90_Square.pulse",
                "y180_Square": "q2.xy.y180_Square.pulse",
                "y90_Square": "q2.xy.y90_Square.pulse",
                "-y90_Square": "q2.xy.-y90_Square.pulse",
                "x180": "q2.xy.x180_DragGaussian.pulse",
                "x90": "q2.xy.x90_DragGaussian.pulse",
                "-x90": "q2.xy.-x90_DragGaussian.pulse",
                "y180": "q2.xy.y180_DragGaussian.pulse",
                "y90": "q2.xy.y90_DragGaussian.pulse",
                "-y90": "q2.xy.-y90_DragGaussian.pulse",
                "saturation": "q2.xy.saturation.pulse",
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
                "mixer": "q2.xy_mixer_e8f",
                "lo_frequency": 4700000000.0,
            },
            "intermediate_frequency": -264564380.79657173,
        },
        "q2.z": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "q2.z.const.pulse",
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
                "port": ('con1', 3, 6),
            },
        },
        "q2.resonator": {
            "digitalInputs": {
                "octave_switch": {
                    "delay": 87,
                    "buffer": 15,
                    "port": ('con1', 1, 1),
                },
            },
            "digitalOutputs": {},
            "outputs": {
                "out1": ('con1', 1, 1),
                "out2": ('con1', 1, 2),
            },
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
            "mixInputs": {
                "I": ('con1', 1, 1),
                "Q": ('con1', 1, 2),
                "mixer": "q2.resonator_mixer_76d",
                "lo_frequency": 6200000000.0,
            },
            "smearing": 0,
            "time_of_flight": 264,
            "intermediate_frequency": -185741282.0,
        },
        "q3.xy": {
            "digitalInputs": {
                "octave_switch": {
                    "delay": 87,
                    "buffer": 15,
                    "port": ('con1', 1, 7),
                },
            },
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "x180_DragGaussian": "q3.xy.x180_DragGaussian.pulse",
                "x90_DragGaussian": "q3.xy.x90_DragGaussian.pulse",
                "-x90_DragGaussian": "q3.xy.-x90_DragGaussian.pulse",
                "y180_DragGaussian": "q3.xy.y180_DragGaussian.pulse",
                "y90_DragGaussian": "q3.xy.y90_DragGaussian.pulse",
                "-y90_DragGaussian": "q3.xy.-y90_DragGaussian.pulse",
                "x180_Square": "q3.xy.x180_Square.pulse",
                "x90_Square": "q3.xy.x90_Square.pulse",
                "-x90_Square": "q3.xy.-x90_Square.pulse",
                "y180_Square": "q3.xy.y180_Square.pulse",
                "y90_Square": "q3.xy.y90_Square.pulse",
                "-y90_Square": "q3.xy.-y90_Square.pulse",
                "x180": "q3.xy.x180_DragGaussian.pulse",
                "x90": "q3.xy.x90_DragGaussian.pulse",
                "-x90": "q3.xy.-x90_DragGaussian.pulse",
                "y180": "q3.xy.y180_DragGaussian.pulse",
                "y90": "q3.xy.y90_DragGaussian.pulse",
                "-y90": "q3.xy.-y90_DragGaussian.pulse",
                "saturation": "q3.xy.saturation.pulse",
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
                "I": ('con1', 1, 7),
                "Q": ('con1', 1, 8),
                "mixer": "q3.xy_mixer_244",
                "lo_frequency": 4700000000.0,
            },
            "intermediate_frequency": -236154100.04951477,
        },
        "q3.z": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "q3.z.const.pulse",
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
                "port": ('con1', 3, 7),
            },
        },
        "q3.resonator": {
            "digitalInputs": {
                "octave_switch": {
                    "delay": 87,
                    "buffer": 15,
                    "port": ('con1', 1, 1),
                },
            },
            "digitalOutputs": {},
            "outputs": {
                "out1": ('con1', 1, 1),
                "out2": ('con1', 1, 2),
            },
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
            "mixInputs": {
                "I": ('con1', 1, 1),
                "Q": ('con1', 1, 2),
                "mixer": "q3.resonator_mixer_397",
                "lo_frequency": 6200000000.0,
            },
            "smearing": 0,
            "time_of_flight": 264,
            "intermediate_frequency": -343278899.0,
        },
        "q4.xy": {
            "digitalInputs": {
                "octave_switch": {
                    "delay": 87,
                    "buffer": 15,
                    "port": ('con1', 2, 1),
                },
            },
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "x180_DragGaussian": "q4.xy.x180_DragGaussian.pulse",
                "x90_DragGaussian": "q4.xy.x90_DragGaussian.pulse",
                "-x90_DragGaussian": "q4.xy.-x90_DragGaussian.pulse",
                "y180_DragGaussian": "q4.xy.y180_DragGaussian.pulse",
                "y90_DragGaussian": "q4.xy.y90_DragGaussian.pulse",
                "-y90_DragGaussian": "q4.xy.-y90_DragGaussian.pulse",
                "x180_Square": "q4.xy.x180_Square.pulse",
                "x90_Square": "q4.xy.x90_Square.pulse",
                "-x90_Square": "q4.xy.-x90_Square.pulse",
                "y180_Square": "q4.xy.y180_Square.pulse",
                "y90_Square": "q4.xy.y90_Square.pulse",
                "-y90_Square": "q4.xy.-y90_Square.pulse",
                "x180": "q4.xy.x180_DragGaussian.pulse",
                "x90": "q4.xy.x90_DragGaussian.pulse",
                "-x90": "q4.xy.-x90_DragGaussian.pulse",
                "y180": "q4.xy.y180_DragGaussian.pulse",
                "y90": "q4.xy.y90_DragGaussian.pulse",
                "-y90": "q4.xy.-y90_DragGaussian.pulse",
                "saturation": "q4.xy.saturation.pulse",
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
                "I": ('con1', 2, 1),
                "Q": ('con1', 2, 2),
                "mixer": "q4.xy_mixer_96e",
                "lo_frequency": 4700000000.0,
            },
            "intermediate_frequency": -284600668.894413,
        },
        "q4.z": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "q4.z.const.pulse",
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
                "port": ('con1', 3, 8),
            },
        },
        "q4.resonator": {
            "digitalInputs": {
                "octave_switch": {
                    "delay": 87,
                    "buffer": 15,
                    "port": ('con1', 1, 1),
                },
            },
            "digitalOutputs": {},
            "outputs": {
                "out1": ('con1', 1, 1),
                "out2": ('con1', 1, 2),
            },
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
            "mixInputs": {
                "I": ('con1', 1, 1),
                "Q": ('con1', 1, 2),
                "mixer": "q4.resonator_mixer_9ec",
                "lo_frequency": 6200000000.0,
            },
            "smearing": 0,
            "time_of_flight": 264,
            "intermediate_frequency": -162578680.0,
        },
        "q5.xy": {
            "digitalInputs": {
                "octave_switch": {
                    "delay": 87,
                    "buffer": 15,
                    "port": ('con1', 2, 3),
                },
            },
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "x180_DragGaussian": "q5.xy.x180_DragGaussian.pulse",
                "x90_DragGaussian": "q5.xy.x90_DragGaussian.pulse",
                "-x90_DragGaussian": "q5.xy.-x90_DragGaussian.pulse",
                "y180_DragGaussian": "q5.xy.y180_DragGaussian.pulse",
                "y90_DragGaussian": "q5.xy.y90_DragGaussian.pulse",
                "-y90_DragGaussian": "q5.xy.-y90_DragGaussian.pulse",
                "x180_Square": "q5.xy.x180_Square.pulse",
                "x90_Square": "q5.xy.x90_Square.pulse",
                "-x90_Square": "q5.xy.-x90_Square.pulse",
                "y180_Square": "q5.xy.y180_Square.pulse",
                "y90_Square": "q5.xy.y90_Square.pulse",
                "-y90_Square": "q5.xy.-y90_Square.pulse",
                "x180": "q5.xy.x180_DragGaussian.pulse",
                "x90": "q5.xy.x90_DragGaussian.pulse",
                "-x90": "q5.xy.-x90_DragGaussian.pulse",
                "y180": "q5.xy.y180_DragGaussian.pulse",
                "y90": "q5.xy.y90_DragGaussian.pulse",
                "-y90": "q5.xy.-y90_DragGaussian.pulse",
                "saturation": "q5.xy.saturation.pulse",
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
                "I": ('con1', 2, 3),
                "Q": ('con1', 2, 4),
                "mixer": "q5.xy_mixer_a3f",
                "lo_frequency": 4700000000.0,
            },
            "intermediate_frequency": -345901097.018157,
        },
        "q5.z": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "q5.z.const.pulse",
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
                "port": ('con1', 3, 1),
            },
        },
        "q5.resonator": {
            "digitalInputs": {
                "octave_switch": {
                    "delay": 87,
                    "buffer": 15,
                    "port": ('con1', 1, 1),
                },
            },
            "digitalOutputs": {},
            "outputs": {
                "out1": ('con1', 1, 1),
                "out2": ('con1', 1, 2),
            },
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
            "mixInputs": {
                "I": ('con1', 1, 1),
                "Q": ('con1', 1, 2),
                "mixer": "q5.resonator_mixer_685",
                "lo_frequency": 6200000000.0,
            },
            "smearing": 0,
            "time_of_flight": 264,
            "intermediate_frequency": -257761381.0,
        },
        "coupler_q1_q2": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "coupler_q1_q2.const.pulse",
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
                "port": ('con1', 3, 2),
            },
        },
        "coupler_q2_q3": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "coupler_q2_q3.const.pulse",
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
                "port": ('con1', 3, 3),
            },
        },
        "coupler_q3_q4": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "coupler_q3_q4.const.pulse",
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
                "port": ('con1', 3, 4),
            },
        },
        "coupler_q4_q5": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "coupler_q4_q5.const.pulse",
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
                "port": ('con1', 3, 5),
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
        "q1.xy.x180_DragGaussian.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q1.xy.x180_DragGaussian.wf.I",
                "Q": "q1.xy.x180_DragGaussian.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q1.xy.x90_DragGaussian.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q1.xy.x90_DragGaussian.wf.I",
                "Q": "q1.xy.x90_DragGaussian.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q1.xy.-x90_DragGaussian.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q1.xy.-x90_DragGaussian.wf.I",
                "Q": "q1.xy.-x90_DragGaussian.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q1.xy.y180_DragGaussian.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q1.xy.y180_DragGaussian.wf.I",
                "Q": "q1.xy.y180_DragGaussian.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q1.xy.y90_DragGaussian.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q1.xy.y90_DragGaussian.wf.I",
                "Q": "q1.xy.y90_DragGaussian.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q1.xy.-y90_DragGaussian.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q1.xy.-y90_DragGaussian.wf.I",
                "Q": "q1.xy.-y90_DragGaussian.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q1.xy.x180_Square.pulse": {
            "length": 100,
            "waveforms": {
                "I": "q1.xy.x180_Square.wf.I",
                "Q": "q1.xy.x180_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q1.xy.x90_Square.pulse": {
            "length": 100,
            "waveforms": {
                "I": "q1.xy.x90_Square.wf.I",
                "Q": "q1.xy.x90_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q1.xy.-x90_Square.pulse": {
            "length": 100,
            "waveforms": {
                "I": "q1.xy.-x90_Square.wf.I",
                "Q": "q1.xy.-x90_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q1.xy.y180_Square.pulse": {
            "length": 100,
            "waveforms": {
                "I": "q1.xy.y180_Square.wf.I",
                "Q": "q1.xy.y180_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q1.xy.y90_Square.pulse": {
            "length": 100,
            "waveforms": {
                "I": "q1.xy.y90_Square.wf.I",
                "Q": "q1.xy.y90_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q1.xy.-y90_Square.pulse": {
            "length": 100,
            "waveforms": {
                "I": "q1.xy.-y90_Square.wf.I",
                "Q": "q1.xy.-y90_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q1.xy.saturation.pulse": {
            "length": 10000,
            "waveforms": {
                "I": "q1.xy.saturation.wf.I",
                "Q": "q1.xy.saturation.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q1.z.const.pulse": {
            "length": 100,
            "waveforms": {
                "single": "q1.z.const.wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q1.resonator.readout.pulse": {
            "length": 1024,
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
        "q2.xy.x180_DragGaussian.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q2.xy.x180_DragGaussian.wf.I",
                "Q": "q2.xy.x180_DragGaussian.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q2.xy.x90_DragGaussian.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q2.xy.x90_DragGaussian.wf.I",
                "Q": "q2.xy.x90_DragGaussian.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q2.xy.-x90_DragGaussian.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q2.xy.-x90_DragGaussian.wf.I",
                "Q": "q2.xy.-x90_DragGaussian.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q2.xy.y180_DragGaussian.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q2.xy.y180_DragGaussian.wf.I",
                "Q": "q2.xy.y180_DragGaussian.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q2.xy.y90_DragGaussian.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q2.xy.y90_DragGaussian.wf.I",
                "Q": "q2.xy.y90_DragGaussian.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q2.xy.-y90_DragGaussian.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q2.xy.-y90_DragGaussian.wf.I",
                "Q": "q2.xy.-y90_DragGaussian.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q2.xy.x180_Square.pulse": {
            "length": 100,
            "waveforms": {
                "I": "q2.xy.x180_Square.wf.I",
                "Q": "q2.xy.x180_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q2.xy.x90_Square.pulse": {
            "length": 100,
            "waveforms": {
                "I": "q2.xy.x90_Square.wf.I",
                "Q": "q2.xy.x90_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q2.xy.-x90_Square.pulse": {
            "length": 100,
            "waveforms": {
                "I": "q2.xy.-x90_Square.wf.I",
                "Q": "q2.xy.-x90_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q2.xy.y180_Square.pulse": {
            "length": 100,
            "waveforms": {
                "I": "q2.xy.y180_Square.wf.I",
                "Q": "q2.xy.y180_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q2.xy.y90_Square.pulse": {
            "length": 100,
            "waveforms": {
                "I": "q2.xy.y90_Square.wf.I",
                "Q": "q2.xy.y90_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q2.xy.-y90_Square.pulse": {
            "length": 100,
            "waveforms": {
                "I": "q2.xy.-y90_Square.wf.I",
                "Q": "q2.xy.-y90_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q2.xy.saturation.pulse": {
            "length": 10000,
            "waveforms": {
                "I": "q2.xy.saturation.wf.I",
                "Q": "q2.xy.saturation.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q2.z.const.pulse": {
            "length": 100,
            "waveforms": {
                "single": "q2.z.const.wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q2.resonator.readout.pulse": {
            "length": 1024,
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
        "q3.xy.x180_DragGaussian.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q3.xy.x180_DragGaussian.wf.I",
                "Q": "q3.xy.x180_DragGaussian.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q3.xy.x90_DragGaussian.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q3.xy.x90_DragGaussian.wf.I",
                "Q": "q3.xy.x90_DragGaussian.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q3.xy.-x90_DragGaussian.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q3.xy.-x90_DragGaussian.wf.I",
                "Q": "q3.xy.-x90_DragGaussian.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q3.xy.y180_DragGaussian.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q3.xy.y180_DragGaussian.wf.I",
                "Q": "q3.xy.y180_DragGaussian.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q3.xy.y90_DragGaussian.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q3.xy.y90_DragGaussian.wf.I",
                "Q": "q3.xy.y90_DragGaussian.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q3.xy.-y90_DragGaussian.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q3.xy.-y90_DragGaussian.wf.I",
                "Q": "q3.xy.-y90_DragGaussian.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q3.xy.x180_Square.pulse": {
            "length": 100,
            "waveforms": {
                "I": "q3.xy.x180_Square.wf.I",
                "Q": "q3.xy.x180_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q3.xy.x90_Square.pulse": {
            "length": 100,
            "waveforms": {
                "I": "q3.xy.x90_Square.wf.I",
                "Q": "q3.xy.x90_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q3.xy.-x90_Square.pulse": {
            "length": 100,
            "waveforms": {
                "I": "q3.xy.-x90_Square.wf.I",
                "Q": "q3.xy.-x90_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q3.xy.y180_Square.pulse": {
            "length": 100,
            "waveforms": {
                "I": "q3.xy.y180_Square.wf.I",
                "Q": "q3.xy.y180_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q3.xy.y90_Square.pulse": {
            "length": 100,
            "waveforms": {
                "I": "q3.xy.y90_Square.wf.I",
                "Q": "q3.xy.y90_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q3.xy.-y90_Square.pulse": {
            "length": 100,
            "waveforms": {
                "I": "q3.xy.-y90_Square.wf.I",
                "Q": "q3.xy.-y90_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q3.xy.saturation.pulse": {
            "length": 10000,
            "waveforms": {
                "I": "q3.xy.saturation.wf.I",
                "Q": "q3.xy.saturation.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q3.z.const.pulse": {
            "length": 100,
            "waveforms": {
                "single": "q3.z.const.wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q3.resonator.readout.pulse": {
            "length": 1024,
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
        "q4.xy.x180_DragGaussian.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q4.xy.x180_DragGaussian.wf.I",
                "Q": "q4.xy.x180_DragGaussian.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q4.xy.x90_DragGaussian.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q4.xy.x90_DragGaussian.wf.I",
                "Q": "q4.xy.x90_DragGaussian.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q4.xy.-x90_DragGaussian.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q4.xy.-x90_DragGaussian.wf.I",
                "Q": "q4.xy.-x90_DragGaussian.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q4.xy.y180_DragGaussian.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q4.xy.y180_DragGaussian.wf.I",
                "Q": "q4.xy.y180_DragGaussian.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q4.xy.y90_DragGaussian.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q4.xy.y90_DragGaussian.wf.I",
                "Q": "q4.xy.y90_DragGaussian.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q4.xy.-y90_DragGaussian.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q4.xy.-y90_DragGaussian.wf.I",
                "Q": "q4.xy.-y90_DragGaussian.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q4.xy.x180_Square.pulse": {
            "length": 100,
            "waveforms": {
                "I": "q4.xy.x180_Square.wf.I",
                "Q": "q4.xy.x180_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q4.xy.x90_Square.pulse": {
            "length": 100,
            "waveforms": {
                "I": "q4.xy.x90_Square.wf.I",
                "Q": "q4.xy.x90_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q4.xy.-x90_Square.pulse": {
            "length": 100,
            "waveforms": {
                "I": "q4.xy.-x90_Square.wf.I",
                "Q": "q4.xy.-x90_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q4.xy.y180_Square.pulse": {
            "length": 100,
            "waveforms": {
                "I": "q4.xy.y180_Square.wf.I",
                "Q": "q4.xy.y180_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q4.xy.y90_Square.pulse": {
            "length": 100,
            "waveforms": {
                "I": "q4.xy.y90_Square.wf.I",
                "Q": "q4.xy.y90_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q4.xy.-y90_Square.pulse": {
            "length": 100,
            "waveforms": {
                "I": "q4.xy.-y90_Square.wf.I",
                "Q": "q4.xy.-y90_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q4.xy.saturation.pulse": {
            "length": 10000,
            "waveforms": {
                "I": "q4.xy.saturation.wf.I",
                "Q": "q4.xy.saturation.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q4.z.const.pulse": {
            "length": 40,
            "waveforms": {
                "single": "q4.z.const.wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q4.resonator.readout.pulse": {
            "length": 1024,
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
        "q5.xy.x180_DragGaussian.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q5.xy.x180_DragGaussian.wf.I",
                "Q": "q5.xy.x180_DragGaussian.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q5.xy.x90_DragGaussian.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q5.xy.x90_DragGaussian.wf.I",
                "Q": "q5.xy.x90_DragGaussian.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q5.xy.-x90_DragGaussian.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q5.xy.-x90_DragGaussian.wf.I",
                "Q": "q5.xy.-x90_DragGaussian.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q5.xy.y180_DragGaussian.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q5.xy.y180_DragGaussian.wf.I",
                "Q": "q5.xy.y180_DragGaussian.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q5.xy.y90_DragGaussian.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q5.xy.y90_DragGaussian.wf.I",
                "Q": "q5.xy.y90_DragGaussian.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q5.xy.-y90_DragGaussian.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q5.xy.-y90_DragGaussian.wf.I",
                "Q": "q5.xy.-y90_DragGaussian.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q5.xy.x180_Square.pulse": {
            "length": 100,
            "waveforms": {
                "I": "q5.xy.x180_Square.wf.I",
                "Q": "q5.xy.x180_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q5.xy.x90_Square.pulse": {
            "length": 100,
            "waveforms": {
                "I": "q5.xy.x90_Square.wf.I",
                "Q": "q5.xy.x90_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q5.xy.-x90_Square.pulse": {
            "length": 100,
            "waveforms": {
                "I": "q5.xy.-x90_Square.wf.I",
                "Q": "q5.xy.-x90_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q5.xy.y180_Square.pulse": {
            "length": 100,
            "waveforms": {
                "I": "q5.xy.y180_Square.wf.I",
                "Q": "q5.xy.y180_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q5.xy.y90_Square.pulse": {
            "length": 100,
            "waveforms": {
                "I": "q5.xy.y90_Square.wf.I",
                "Q": "q5.xy.y90_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q5.xy.-y90_Square.pulse": {
            "length": 100,
            "waveforms": {
                "I": "q5.xy.-y90_Square.wf.I",
                "Q": "q5.xy.-y90_Square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q5.xy.saturation.pulse": {
            "length": 10000,
            "waveforms": {
                "I": "q5.xy.saturation.wf.I",
                "Q": "q5.xy.saturation.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "q5.z.const.pulse": {
            "length": 100,
            "waveforms": {
                "single": "q5.z.const.wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q5.resonator.readout.pulse": {
            "length": 1024,
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
        "coupler_q1_q2.const.pulse": {
            "length": 40,
            "waveforms": {
                "single": "coupler_q1_q2.const.wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "coupler_q2_q3.const.pulse": {
            "length": 40,
            "waveforms": {
                "single": "coupler_q2_q3.const.wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "coupler_q3_q4.const.pulse": {
            "length": 40,
            "waveforms": {
                "single": "coupler_q3_q4.const.wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "coupler_q4_q5.const.pulse": {
            "length": 40,
            "waveforms": {
                "single": "coupler_q4_q5.const.wf",
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
        "q1.xy.x180_DragGaussian.wf.I": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.xy.x180_DragGaussian.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.xy.x90_DragGaussian.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0009308033584822786, 0.0022162882408895738, 0.0039504329579779455, 0.00623471737013874, 0.009171468002093624, 0.012854464586515613, 0.0173570914762729, 0.022718822828775964, 0.028931368012269813, 0.035926273150203525, 0.04356605894305792, 0.0516409635018751, 0.05987297730580422, 0.0679280941544471, 0.07543662643820798, 0.08202019565499412, 0.08732282109948077, 0.09104262368830635] + [0.09296024132804348] * 2 + [0.09104262368830635, 0.08732282109948077, 0.08202019565499412, 0.07543662643820798, 0.0679280941544471, 0.05987297730580422, 0.0516409635018751, 0.04356605894305792, 0.035926273150203525, 0.028931368012269813, 0.022718822828775964, 0.0173570914762729, 0.012854464586515613, 0.009171468002093624, 0.00623471737013874, 0.0039504329579779455, 0.0022162882408895738, 0.0009308033584822786, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.xy.x90_DragGaussian.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0008297562420585476, 0.0011600789497869175, 0.0015844940588258436, 0.002113538223091799, 0.0027521259378796544, 0.003496647861908873, 0.004332133204156863, 0.005229967996598423, 0.00614673784329763, 0.007024749293451887, 0.007794650779385713, 0.008380315267377378, 0.008705784574698384, 0.00870366322667387, 0.008323966570666159, 0.007542163018573711, 0.006365082784623594, 0.004833541802232808, 0.0030209465036534853, 0.0010277439587909154, -0.0010277439587909154, -0.0030209465036534853, -0.004833541802232808, -0.006365082784623594, -0.007542163018573711, -0.008323966570666159, -0.00870366322667387, -0.008705784574698384, -0.008380315267377378, -0.007794650779385713, -0.007024749293451887, -0.00614673784329763, -0.005229967996598423, -0.004332133204156863, -0.003496647861908873, -0.0027521259378796544, -0.002113538223091799, -0.0015844940588258436, -0.0011600789497869175, -0.0008297562420585476],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.xy.-x90_DragGaussian.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -0.0004890327182525387, -0.0011644107780623145, -0.002075509236305739, -0.003275644372434133, -0.004818577292999117, -0.00675357872437716, -0.009119203909448838, -0.011936192088487896, -0.01520018746480943, -0.018875225207582575, -0.022889075371637223, -0.027131531621974618, -0.03145653115118992, -0.03568859118023487, -0.03963348235338423, -0.04309240922612172, -0.04587834388284734, -0.04783268273949085] + [-0.048840175630855964] * 2 + [-0.04783268273949085, -0.04587834388284734, -0.04309240922612172, -0.03963348235338423, -0.03568859118023487, -0.03145653115118992, -0.027131531621974618, -0.022889075371637223, -0.018875225207582575, -0.01520018746480943, -0.011936192088487896, -0.009119203909448838, -0.00675357872437716, -0.004818577292999117, -0.003275644372434133, -0.002075509236305739, -0.0011644107780623145, -0.0004890327182525387, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.xy.-x90_DragGaussian.wf.Q": {
            "type": "arbitrary",
            "samples": [-0.000435943797197449, -0.0006094913141771259, -0.0008324738298173561, -0.0011104271734198958, -0.0014459333608004257, -0.0018370960881248035, -0.002276049884602178, -0.002747761320845089, -0.0032294210033738465, -0.0036907174976472555, -0.004095214336879552, -0.00440291530716134, -0.004573912906833186, -0.0045727983764854655, -0.004373310389998592, -0.003962560350545937, -0.0033441367692767913, -0.0025394838391939335, -0.0015871684034166418, -0.0005399641258865475, 0.0005399641258865475, 0.0015871684034166418, 0.0025394838391939335, 0.0033441367692767913, 0.003962560350545937, 0.004373310389998592, 0.0045727983764854655, 0.004573912906833186, 0.00440291530716134, 0.004095214336879552, 0.0036907174976472555, 0.0032294210033738465, 0.002747761320845089, 0.002276049884602178, 0.0018370960881248035, 0.0014459333608004257, 0.0011104271734198958, 0.0008324738298173561, 0.0006094913141771259, 0.000435943797197449],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.xy.y180_DragGaussian.wf.I": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.xy.y180_DragGaussian.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.xy.y90_DragGaussian.wf.I": {
            "type": "arbitrary",
            "samples": [-0.00043593540845350163, -0.0006125133656181951, -0.0008396813883669383, -0.001123281504229698, -0.0014662264339898217, -0.0018669534245001442, -0.0023179028138472987, -0.0028042806445208704, -0.003303406620599842, -0.0037849428690515776, -0.004212230511600758, -0.0045448260158726, -0.0047421389684343595, -0.004767855171124772, -0.0045946251723320225, -0.004208355695520126, -0.003611401928723668, -0.0028240473996744295, -0.0018838742908671767, -0.0008429402809590696, 0.00023696719005824012, 0.001290401433095227, 0.0022548225455660802, 0.00307674290926226, 0.003716612504701818, 0.004151827298900133, 0.0043775655956986344, 0.004405510816191299, 0.004260835150326854, 0.003978040556041674, 0.003596350087364212, 0.003155311100466671, 0.0026911362483718836, 0.002234109360580776, 0.0018071680503022167, 0.0014255846402325984, 0.001097530107334171, 0.0008252342331479699, 0.0006064458061959906, 0.00043593540845350163],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.xy.y90_DragGaussian.wf.Q": {
            "type": "arbitrary",
            "samples": [-2.704435506573881e-06, 0.00048524224725171876, 0.0011592240091667493, 0.002068580614748963, 0.003266611299619915, 0.004807087899795191, 0.006739328988045931, 0.009101982327229873, 0.011915928259656917, 0.01517699911348765, 0.018849456788435155, 0.022861320851078854, 0.02710263465860026, 0.03142755787720306, 0.035660774020245, 0.03960813742563163, 0.043070834212403875, 0.045861707031975105, 0.04782191609768266, 0.04883588607359181, 0.048842585552578366, 0.047841608519562304, 0.045893215085569344, 0.04311232580960431, 0.039657301969216616, 0.03571503484916843, 0.0314842938068035, 0.02715938441647611, 0.0229159489961089, 0.018900267205424166, 0.015222790830261866, 0.011955996547740592, 0.009136074535112892, 0.006767568546274413, 0.004829881241146312, 0.0032845513806405756, 0.0020823579809808816, 0.0011695527340992978, 0.0004928043686150945, 2.704435506573881e-06],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.xy.-y90_DragGaussian.wf.I": {
            "type": "arbitrary",
            "samples": [0.00043593540845350163, 0.0006125133656181951, 0.0008396813883669383, 0.001123281504229698, 0.0014662264339898217, 0.0018669534245001442, 0.0023179028138472987, 0.0028042806445208704, 0.003303406620599842, 0.0037849428690515776, 0.004212230511600758, 0.0045448260158726, 0.0047421389684343595, 0.004767855171124772, 0.0045946251723320225, 0.004208355695520126, 0.003611401928723668, 0.0028240473996744295, 0.0018838742908671767, 0.0008429402809590696, -0.00023696719005824012, -0.001290401433095227, -0.0022548225455660802, -0.00307674290926226, -0.003716612504701818, -0.004151827298900133, -0.0043775655956986344, -0.004405510816191299, -0.004260835150326854, -0.003978040556041674, -0.003596350087364212, -0.003155311100466671, -0.0026911362483718836, -0.002234109360580776, -0.0018071680503022167, -0.0014255846402325984, -0.001097530107334171, -0.0008252342331479699, -0.0006064458061959906, -0.00043593540845350163],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.xy.-y90_DragGaussian.wf.Q": {
            "type": "arbitrary",
            "samples": [2.704435506573881e-06, -0.00048524224725171876, -0.0011592240091667493, -0.002068580614748963, -0.003266611299619915, -0.004807087899795191, -0.006739328988045931, -0.009101982327229873, -0.011915928259656917, -0.01517699911348765, -0.018849456788435155, -0.022861320851078854, -0.02710263465860026, -0.03142755787720306, -0.035660774020245, -0.03960813742563163, -0.043070834212403875, -0.045861707031975105, -0.04782191609768266, -0.04883588607359181, -0.048842585552578366, -0.047841608519562304, -0.045893215085569344, -0.04311232580960431, -0.039657301969216616, -0.03571503484916843, -0.0314842938068035, -0.02715938441647611, -0.0229159489961089, -0.018900267205424166, -0.015222790830261866, -0.011955996547740592, -0.009136074535112892, -0.006767568546274413, -0.004829881241146312, -0.0032845513806405756, -0.0020823579809808816, -0.0011695527340992978, -0.0004928043686150945, -2.704435506573881e-06],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.xy.x180_Square.wf.I": {
            "type": "constant",
            "sample": 0.25,
        },
        "q1.xy.x180_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q1.xy.x90_Square.wf.I": {
            "type": "constant",
            "sample": 0.125,
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
            "sample": -0.0015509083533014347,
        },
        "q1.xy.y180_Square.wf.Q": {
            "type": "constant",
            "sample": 0.24999518932027404,
        },
        "q1.xy.y90_Square.wf.I": {
            "type": "constant",
            "sample": -0.0007754541766507173,
        },
        "q1.xy.y90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.12499759466013702,
        },
        "q1.xy.-y90_Square.wf.I": {
            "type": "constant",
            "sample": 0.0007754541766507173,
        },
        "q1.xy.-y90_Square.wf.Q": {
            "type": "constant",
            "sample": -0.12499759466013702,
        },
        "q1.xy.saturation.wf.I": {
            "type": "constant",
            "sample": 0.25,
        },
        "q1.xy.saturation.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q1.z.const.wf": {
            "type": "constant",
            "sample": 0.1,
        },
        "q1.resonator.readout.wf.I": {
            "type": "constant",
            "sample": 0.015,
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
        "q2.xy.x180_DragGaussian.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0005643674229523334, 0.001343786387997033, 0.0023952381002097798, 0.0037802521262479305, 0.005560871384769406, 0.0077939566784040164, 0.010524002623265721, 0.013774943306278407, 0.017541751927274703, 0.021782923331005566, 0.026415100665272424, 0.03131110048619751, 0.03630235924552004, 0.04118636132396231, 0.0457389566455457, 0.049730725646856884, 0.05294582906232589, 0.05520123068052587] + [0.056363926233441615] * 2 + [0.05520123068052587, 0.05294582906232589, 0.049730725646856884, 0.0457389566455457, 0.04118636132396231, 0.03630235924552004, 0.03131110048619751, 0.026415100665272424, 0.021782923331005566, 0.017541751927274703, 0.013774943306278407, 0.010524002623265721, 0.0077939566784040164, 0.005560871384769406, 0.0037802521262479305, 0.0023952381002097798, 0.001343786387997033, 0.0005643674229523334, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.xy.x180_DragGaussian.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.xy.x90_DragGaussian.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.00026603379872938097, 0.000633439463265899, 0.0011290770245503219, 0.0017819505386041678, 0.002621306047391519, 0.0036739468260611747, 0.004960846926740169, 0.006493288496137415, 0.008268901980856329, 0.010268122512924919, 0.012451657002170647, 0.01475955320235419, 0.017112352946247314, 0.019414593602047767, 0.021560614400241016, 0.023442270619010212, 0.024957819072268947, 0.026020979410283022] + [0.026569055543185643] * 2 + [0.026020979410283022, 0.024957819072268947, 0.023442270619010212, 0.021560614400241016, 0.019414593602047767, 0.017112352946247314, 0.01475955320235419, 0.012451657002170647, 0.010268122512924919, 0.008268901980856329, 0.006493288496137415, 0.004960846926740169, 0.0036739468260611747, 0.002621306047391519, 0.0017819505386041678, 0.0011290770245503219, 0.000633439463265899, 0.00026603379872938097, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.xy.x90_DragGaussian.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.xy.-x90_DragGaussian.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -0.0002660337987284443, -0.0006334394632636688, -0.0011290770245463468, -0.001781950538597894, -0.0026213060473822903, -0.0036739468260482398, -0.004960846926722703, -0.006493288496114554, -0.008268901980827217, -0.010268122512888767, -0.012451657002126809, -0.014759553202302225, -0.017112352946187067, -0.01941459360197941, -0.021560614400165108, -0.023442270618927678, -0.024957819072181076, -0.026020979410191408] + [-0.0265690555430921] * 2 + [-0.026020979410191408, -0.024957819072181076, -0.023442270618927678, -0.021560614400165108, -0.01941459360197941, -0.017112352946187067, -0.014759553202302225, -0.012451657002126809, -0.010268122512888767, -0.008268901980827217, -0.006493288496114554, -0.004960846926722703, -0.0036739468260482398, -0.0026213060473822903, -0.001781950538597894, -0.0011290770245463468, -0.0006334394632636688, -0.0002660337987284443, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.xy.-x90_DragGaussian.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 7.059445729951398e-10, 1.6808884944292212e-09, 2.996107268255804e-09, 4.72856576149942e-09, 6.955870972611922e-09, 9.74914779895659e-09, 1.316405277118297e-08, 1.7230524078644942e-08, 2.1942273898634525e-08, 2.724738509719295e-08, 3.304158993128908e-08, 3.916579973221368e-08, 4.540916511841139e-08, 5.151836742448517e-08, 5.721302631089345e-08, 6.220617004761808e-08, 6.622781395451698e-08, 6.904900537616857e-08] + [7.05033746084192e-08] * 2 + [6.904900537616857e-08, 6.622781395451698e-08, 6.220617004761808e-08, 5.721302631089345e-08, 5.151836742448517e-08, 4.540916511841139e-08, 3.916579973221368e-08, 3.304158993128908e-08, 2.724738509719295e-08, 2.1942273898634525e-08, 1.7230524078644942e-08, 1.316405277118297e-08, 9.74914779895659e-09, 6.955870972611922e-09, 4.72856576149942e-09, 2.996107268255804e-09, 1.6808884944292212e-09, 7.059445729951398e-10, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.xy.y180_DragGaussian.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -3.501128602351911e-06, -8.336358136789445e-06, -1.4859179111044826e-05, -2.34512984007337e-05, -3.449760752909515e-05, -4.835085007122517e-05, -6.528705431435607e-05, -8.545469855984346e-05, -0.00010882259838220751, -0.00013513327101352497, -0.00016386960110027716, -0.0001942425891804173, -0.0002252065287937064, -0.00025550508727769717, -0.00028374771973147596, -0.00030851119128580894, -0.00032845651426092435, -0.00034244819909978806] + [-0.0003496611360812419] * 2 + [-0.00034244819909978806, -0.00032845651426092435, -0.00030851119128580894, -0.00028374771973147596, -0.00025550508727769717, -0.0002252065287937064, -0.0001942425891804173, -0.00016386960110027716, -0.00013513327101352497, -0.00010882259838220751, -8.545469855984346e-05, -6.528705431435607e-05, -4.835085007122517e-05, -3.449760752909515e-05, -2.34512984007337e-05, -1.4859179111044826e-05, -8.336358136789445e-06, -3.501128602351911e-06, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.xy.y180_DragGaussian.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0005643565629886551, 0.0013437605298933018, 0.0023951920093163094, 0.0037801793839188796, 0.005560764378484488, 0.0077938067014865055, 0.010523800112841498, 0.013774678238916448, 0.017541414376273285, 0.021782504168335003, 0.026414592366915506, 0.031310497975492284, 0.03630166068942553, 0.04118556878638868, 0.04573807650366001, 0.04972976869248238, 0.05294481024062011, 0.05520016845876074] + [0.05636284163825279] * 2 + [0.05520016845876074, 0.05294481024062011, 0.04972976869248238, 0.04573807650366001, 0.04118556878638868, 0.03630166068942553, 0.031310497975492284, 0.026414592366915506, 0.021782504168335003, 0.017541414376273285, 0.013774678238916448, 0.010523800112841498, 0.0077938067014865055, 0.005560764378484488, 0.0037801793839188796, 0.0023951920093163094, 0.0013437605298933018, 0.0005643565629886551, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.xy.y90_DragGaussian.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -1.6503761628396382e-06, -3.929626219559441e-06, -7.004379955583293e-06, -1.1054567901964778e-05, -1.6261621781836294e-05, -2.2791819288494275e-05, -3.077527575252431e-05, -4.028198147622251e-05, -5.1297236618963444e-05, -6.36996679120711e-05, -7.724551542844303e-05, -9.156285741011222e-05, -0.0001061587645159095, -0.00012044102157347389, -0.00013375414790257997, -0.00014542725329350293, -0.0001548291603174711, -0.00016142461731397033] + [-0.0001648246807250256] * 2 + [-0.00016142461731397033, -0.0001548291603174711, -0.00014542725329350293, -0.00013375414790257997, -0.00012044102157347389, -0.0001061587645159095, -9.156285741011222e-05, -7.724551542844303e-05, -6.36996679120711e-05, -5.1297236618963444e-05, -4.028198147622251e-05, -3.077527575252431e-05, -2.2791819288494275e-05, -1.6261621781836294e-05, -1.1054567901964778e-05, -7.004379955583293e-06, -3.929626219559441e-06, -1.6503761628396382e-06, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.xy.y90_DragGaussian.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.0002660286795157731, 0.0006334272741683648, 0.0011290552980385176, 0.001781916249030853, 0.002621255606336088, 0.0036738761293351333, 0.004960751466557232, 0.006493163547612122, 0.008268742864699868, 0.010267924926329733, 0.012451417398435067, 0.01475926918842077, 0.017112023658049785, 0.01941422001248045, 0.02156019951539872, 0.023441819525986222, 0.024957338815972088, 0.026020478695890626] + [0.026568544282318286] * 2 + [0.026020478695890626, 0.024957338815972088, 0.023441819525986222, 0.02156019951539872, 0.01941422001248045, 0.017112023658049785, 0.01475926918842077, 0.012451417398435067, 0.010267924926329733, 0.008268742864699868, 0.006493163547612122, 0.004960751466557232, 0.0036738761293351333, 0.002621255606336088, 0.001781916249030853, 0.0011290552980385176, 0.0006334272741683648, 0.0002660286795157731, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.xy.-y90_DragGaussian.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -1.6503761628396382e-06, -3.929626219559441e-06, -7.004379955583293e-06, -1.1054567901964778e-05, -1.6261621781836294e-05, -2.2791819288494275e-05, -3.077527575252431e-05, -4.028198147622251e-05, -5.1297236618963444e-05, -6.36996679120711e-05, -7.724551542844303e-05, -9.156285741011222e-05, -0.0001061587645159095, -0.00012044102157347389, -0.00013375414790257997, -0.00014542725329350293, -0.0001548291603174711, -0.00016142461731397033] + [-0.0001648246807250256] * 2 + [-0.00016142461731397033, -0.0001548291603174711, -0.00014542725329350293, -0.00013375414790257997, -0.00012044102157347389, -0.0001061587645159095, -9.156285741011222e-05, -7.724551542844303e-05, -6.36996679120711e-05, -5.1297236618963444e-05, -4.028198147622251e-05, -3.077527575252431e-05, -2.2791819288494275e-05, -1.6261621781836294e-05, -1.1054567901964778e-05, -7.004379955583293e-06, -3.929626219559441e-06, -1.6503761628396382e-06, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.xy.-y90_DragGaussian.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.0002660286795157731, -0.0006334272741683648, -0.0011290552980385176, -0.001781916249030853, -0.002621255606336088, -0.0036738761293351333, -0.004960751466557232, -0.006493163547612122, -0.008268742864699868, -0.010267924926329733, -0.012451417398435067, -0.01475926918842077, -0.017112023658049785, -0.01941422001248045, -0.02156019951539872, -0.023441819525986222, -0.024957338815972088, -0.026020478695890626] + [-0.026568544282318286] * 2 + [-0.026020478695890626, -0.024957338815972088, -0.023441819525986222, -0.02156019951539872, -0.01941422001248045, -0.017112023658049785, -0.01475926918842077, -0.012451417398435067, -0.010267924926329733, -0.008268742864699868, -0.006493163547612122, -0.004960751466557232, -0.0036738761293351333, -0.002621255606336088, -0.001781916249030853, -0.0011290552980385176, -0.0006334272741683648, -0.0002660286795157731, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.xy.x180_Square.wf.I": {
            "type": "constant",
            "sample": 0.25,
        },
        "q2.xy.x180_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q2.xy.x90_Square.wf.I": {
            "type": "constant",
            "sample": 0.125,
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
            "sample": -0.0015509083533014347,
        },
        "q2.xy.y180_Square.wf.Q": {
            "type": "constant",
            "sample": 0.24999518932027404,
        },
        "q2.xy.y90_Square.wf.I": {
            "type": "constant",
            "sample": -0.0007754541766507173,
        },
        "q2.xy.y90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.12499759466013702,
        },
        "q2.xy.-y90_Square.wf.I": {
            "type": "constant",
            "sample": 0.0007754541766507173,
        },
        "q2.xy.-y90_Square.wf.Q": {
            "type": "constant",
            "sample": -0.12499759466013702,
        },
        "q2.xy.saturation.wf.I": {
            "type": "constant",
            "sample": 0.5,
        },
        "q2.xy.saturation.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q2.z.const.wf": {
            "type": "constant",
            "sample": 0.1,
        },
        "q2.resonator.readout.wf.I": {
            "type": "constant",
            "sample": 0.04,
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
        "q3.xy.x180_DragGaussian.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.000480660122228574, 0.0011444752181564196, 0.0020399750077541405, 0.0032195629569685908, 0.004736079743083251, 0.006637952541782867, 0.008963076502131798, 0.01173183579351758, 0.014939949193664433, 0.01855206761581827, 0.022497197744034744, 0.026667020055971567, 0.030917972445782062, 0.035077576527300695, 0.03895492829272023, 0.04235463582020542, 0.04509287324817859, 0.047013752401350556] + [0.04800399628122508] * 2 + [0.047013752401350556, 0.04509287324817859, 0.04235463582020542, 0.03895492829272023, 0.035077576527300695, 0.030917972445782062, 0.026667020055971567, 0.022497197744034744, 0.01855206761581827, 0.014939949193664433, 0.01173183579351758, 0.008963076502131798, 0.006637952541782867, 0.004736079743083251, 0.0032195629569685908, 0.0020399750077541405, 0.0011444752181564196, 0.000480660122228574, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q3.xy.x180_DragGaussian.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0004284801221367499, 0.0005990563793286867, 0.0008182212720284027, 0.0010914158521113766, 0.0014211779294034945, 0.0018056436661722673, 0.002237082254210781, 0.002700717647383079, 0.0031741309656250992, 0.003627529728213758, 0.004025101287190851, 0.00432753419293586, 0.0044956041892599465, 0.004494508740482865, 0.004298436133499548, 0.003894718433640558, 0.0032868827141328124, 0.0024960060277891397, 0.0015599949253080748, 0.00053071954709919, -0.00053071954709919, -0.0015599949253080748, -0.0024960060277891397, -0.0032868827141328124, -0.003894718433640558, -0.004298436133499548, -0.004494508740482865, -0.0044956041892599465, -0.00432753419293586, -0.004025101287190851, -0.003627529728213758, -0.0031741309656250992, -0.002700717647383079, -0.002237082254210781, -0.0018056436661722673, -0.0014211779294034945, -0.0010914158521113766, -0.0008182212720284027, -0.0005990563793286867, -0.0004284801221367499],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q3.xy.x90_DragGaussian.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.00023277957388820845, 0.0005542595303576617, 0.0009879423964815318, 0.001559206721278647, 0.0022936427914675797, 0.0032147034728035287, 0.004340741060897647, 0.005681627434120238, 0.007235289233249289, 0.008984607198809306, 0.010895199876899318, 0.012914609052059918, 0.014973308827966401, 0.016987769401791798, 0.018865537600210893, 0.02051198679163394, 0.021838091688235334, 0.022768356983997647] + [0.02324792360028744] * 2 + [0.022768356983997647, 0.021838091688235334, 0.02051198679163394, 0.018865537600210893, 0.016987769401791798, 0.014973308827966401, 0.012914609052059918, 0.010895199876899318, 0.008984607198809306, 0.007235289233249289, 0.005681627434120238, 0.004340741060897647, 0.0032147034728035287, 0.0022936427914675797, 0.001559206721278647, 0.0009879423964815318, 0.0005542595303576617, 0.00023277957388820845, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q3.xy.x90_DragGaussian.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0002075092474659857, 0.0002901178655483119, 0.00039625754299306155, 0.0005285633345478704, 0.0006882642797410026, 0.0008744577379474066, 0.0010833997450706368, 0.0013079343887222622, 0.0015372043976059511, 0.0017567815288800936, 0.0019493220243546668, 0.002095787686208798, 0.0021771825436525966, 0.002176652027207082, 0.00208169574563933, 0.0018861787268598664, 0.0015918091021757527, 0.0012087943074563124, 0.0007554921600263216, 0.0002570229239219966, -0.0002570229239219966, -0.0007554921600263216, -0.0012087943074563124, -0.0015918091021757527, -0.0018861787268598664, -0.00208169574563933, -0.002176652027207082, -0.0021771825436525966, -0.002095787686208798, -0.0019493220243546668, -0.0017567815288800936, -0.0015372043976059511, -0.0013079343887222622, -0.0010833997450706368, -0.0008744577379474066, -0.0006882642797410026, -0.0005285633345478704, -0.00039625754299306155, -0.0002901178655483119, -0.0002075092474659857],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q3.xy.-x90_DragGaussian.wf.I": {
            "type": "arbitrary",
            "samples": [-5.506444211020455e-10, -0.0002327803437411958, -0.0005542605818606819, -0.000987943799068323, -0.0015592085476442254, -0.0022936451119116327, -0.003214706347690716, -0.004340744531603708, -0.0056816315132101345, -0.007235293895001349, -0.008984612371478701, -0.010895205438221771, -0.012914614829363825, -0.014973314603855288, -0.01698777492569857, -0.018865542605289092, -0.020511991015570108, -0.021838094895802684, -0.02276835898868377, -0.023247924282239, -0.02324792291817218, -0.022768354979151202, -0.02183808848051421, -0.020511982567553336, -0.018865532594999856, -0.016987763877765405, -0.014973303051972081, -0.012914603274665072, -0.010895194315500146, -0.008984602026076646, -0.007235284571446281, -0.005681623354990335, -0.00434073759016102, -0.003214700597893705, -0.0022936404710073763, -0.0015592048949020897, -0.0009879409938877838, -0.0005542584788507386, -0.000232778804033582, 5.506444211020455e-10],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q3.xy.-x90_DragGaussian.wf.Q": {
            "type": "arbitrary",
            "samples": [-0.0002075092474652551, -0.0002901172478457891, -0.00039625607221423383, -0.0005285607129521498, -0.000688260142243538, -0.0008744516515572268, -0.0010833912145624981, -0.0013079228701714826, -0.0015371893208919701, -0.0017567623293842471, -0.0019492981828858438, -0.0020957587748102295, -0.0021771482735701655, -0.0021766122941799396, -0.0020816506670605045, -0.0018861286654552037, -0.0015917546717713568, -0.0012087363581148463, -0.0007554317421439576, -0.0002569612334683093, 0.0002570846143738741, 0.0007555525779033658, 0.0012088522567892666, 0.0015918635325689401, 0.0018862287882512477, 0.002081740824203497, 0.002176691760218897, 0.002177216813719697, 0.0020958165975926094, 0.0019493458658097638, 0.0017568007283635697, 0.0015372194743091079, 0.0013079459072638322, 0.0010834082755711465, 0.0008744638243314289, 0.0006882684172336207, 0.0005285659561398693, 0.0003962590137690991, 0.00029011848324879186, 0.0002075092474652551],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q3.xy.y180_DragGaussian.wf.I": {
            "type": "arbitrary",
            "samples": [-0.0004284801201488482, -0.0005990100761004718, -0.0008181110246028927, -0.0010912193427939716, -0.001420867792629912, -0.0018051874464137972, -0.002236442831139967, -0.0026998542504227717, -0.003173000860760459, -0.0036260905939645843, -0.004023314207307318, -0.004325367089909099, -0.004493035419835461, -0.004491530490445127, -0.0042950572030428825, -0.003890966012189238, -0.0032828028125722994, -0.002491662364263145, -0.0015554662339927116, -0.0005260954735401066, 0.0005353436157338054, 0.0015645236021484769, 0.002500349668155065, 0.0032909625851948294, 0.003898470818953364, 0.0043018150240716636, 0.004497486948816724, 0.0044981729169703884, 0.004329701255808074, 0.004026888329726066, 0.003628968828803622, 0.00317526104103745, 0.0027015810192838286, 0.002237721656524041, 0.001806099869176438, 0.001421488052990178, 0.0010916123513016961, 0.000818331511861759, 0.0005991026769983464, 0.0004284801201488482],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q3.xy.y180_DragGaussian.wf.Q": {
            "type": "arbitrary",
            "samples": [4.127411677852206e-08, 0.0004807178251794809, 0.0011445540294792408, 0.0020400801308805986, 0.0032196998395463733, 0.00473625365297738, 0.006638168001949714, 0.008963336612022761, 0.011732141492950626, 0.014940298552663218, 0.01855245525485286, 0.022497614497158633, 0.026667452979393914, 0.03091840524396136, 0.035077990419136056, 0.038955303277734894, 0.042354952238580795, 0.04509311347123388, 0.04701390245254473, 0.048004047181026986, 0.04800394493600122, 0.047013601913922766, 0.04509263260671322, 0.04235431900882766, 0.038954552946248576, 0.03507716230998572, 0.03091753936071949, 0.0266665868851099, 0.022496780782162697, 0.018551679804641803, 0.014939599696040078, 0.011731529985226571, 0.008962816309073779, 0.006637737020023443, 0.004735905789243742, 0.003219426044516962, 0.0020398698656990573, 0.001144396396214183, 0.0004806024148176932, -4.127411677852206e-08],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q3.xy.y90_DragGaussian.wf.I": {
            "type": "arbitrary",
            "samples": [-0.00020750525442386677, -0.00029155636203426086, -0.00039968834086266273, -0.0005346819960133362, -0.0006979237825791552, -0.0008886698300620687, -0.0011033217393913144, -0.001334837586791934, -0.001572421551405525, -0.001801632805668551, -0.002005021723521961, -0.002163337183555358, -0.0022572581489747547, -0.0022694990614553915, -0.002187041582030043, -0.0020031773110675806, -0.001719027318072466, -0.0013442465622450286, -0.0008967241624527762, -0.0004012395737365172, 0.00011279638246772234, 0.0006142310821533281, 0.0010732955316894543, 0.0014645296248088358, 0.0017691075522380654, 0.0019762697942764633, 0.00208372122355255, 0.0020970231485070586, 0.0020281575315555826, 0.0018935473046758368, 0.0017118626415853649, 0.0015019280838221355, 0.0012809808542250166, 0.0010634360556364493, 0.0008602119919438552, 0.0006785782887507167, 0.0005224243310910654, 0.0003928114949784337, 0.0002886682037492915, 0.00020750525442386677],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q3.xy.y90_DragGaussian.wf.Q": {
            "type": "arbitrary",
            "samples": [-1.2873113011291672e-06, 0.00023097530969181813, 0.0005517906283633726, 0.0009846443726205065, 0.0015549069786190792, 0.002288173840302511, 0.0032079205983098634, 0.00433254358776142, 0.005671981851596691, 0.007224251578020122, 0.008972341431295133, 0.010881988725113536, 0.012900854097493725, 0.01495951754954866, 0.01697452843363662, 0.018853473414600655, 0.020501717085104246, 0.02183017254722015, 0.022763232062496946, 0.023245881771029698, 0.023249070723027305, 0.022772605655311653, 0.02184517038073101, 0.02052146708537165, 0.01887687573734711, 0.01700035658820417, 0.014986523852038467, 0.012927866982242627, 0.010907991722147835, 0.008996527189781903, 0.007246048435204648, 0.0056910543567245215, 0.004348771478713736, 0.003221362628026621, 0.0022990234707856447, 0.0015634464571849139, 0.0009912023989468997, 0.0005567071014312659, 0.00023457487946078502, 1.2873113011291672e-06],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q3.xy.-y90_DragGaussian.wf.I": {
            "type": "arbitrary",
            "samples": [0.00020750924650326196, 0.000290140287112567, 0.0003963109311986718, 0.0005286584974200885, 0.0006884144699336614, 0.000874678673148823, 0.0010837094021258836, 0.0013083525123274236, 0.0015377516834338845, 0.0017574784729505473, 0.0019501874737244602, 0.0020968371761678237, 0.002178426556447124, 0.0021780943479548314, 0.002083332113357844, 0.0018879959748773001, 0.0015937849487322171, 0.0012108978952239343, 0.000757685359371211, 0.0002592623206945122, -0.0002547835247646035, -0.0007532989536713327, -0.0012066907084724676, -0.0015898332408491279, -0.0018843614613408605, -0.0020800593586050697, -0.0021752096862625012, -0.002175938510656316, -0.00209473817680327, -0.001948456556897404, -0.001756084568508725, -0.0015366570975145263, -0.001307516252980972, -0.0010830900779626848, -0.0008742367946320267, -0.0006881140831620417, -0.0005284681667711916, -0.00039620415111063636, -0.0002900954412920962, -0.00020750924650326196],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q3.xy.-y90_DragGaussian.wf.Q": {
            "type": "arbitrary",
            "samples": [1.9988700688898872e-08, -0.00023275162668415762, -0.0005542213575672047, -0.0009878914770862083, -0.0015591404157528166, -0.0022935585471153554, -0.003214599097464278, -0.004340615051631695, -0.005681479333788256, -0.007235119974547953, -0.008984419385183353, -0.010894997945841563, -0.012914399271127539, -0.014973099088585785, -0.016987568799899485, -0.01886535582313455, -0.02051183336260144, -0.02183797514763798, -0.022768284104227314, -0.023247898734235987, -0.023247948250624866, -0.02276842965250378, -0.021838208026200276, -0.02051214003033876, -0.018865719202236713, -0.016987969846057122, -0.014973518428411908, -0.012914818713159559, -0.010895401706862132, -0.008984794929068425, -0.00723545842481545, -0.005681775481733243, -0.004340867029886507, -0.003214807818314024, -0.002293727014537433, -0.00155927301233683, -0.0009879933067098846, -0.000554297698005227, -0.00023280751893233221, -1.9988700688898872e-08],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q3.xy.x180_Square.wf.I": {
            "type": "constant",
            "sample": 0.25,
        },
        "q3.xy.x180_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q3.xy.x90_Square.wf.I": {
            "type": "constant",
            "sample": 0.125,
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
            "sample": -0.0015509083533014347,
        },
        "q3.xy.y180_Square.wf.Q": {
            "type": "constant",
            "sample": 0.24999518932027404,
        },
        "q3.xy.y90_Square.wf.I": {
            "type": "constant",
            "sample": -0.0007754541766507173,
        },
        "q3.xy.y90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.12499759466013702,
        },
        "q3.xy.-y90_Square.wf.I": {
            "type": "constant",
            "sample": 0.0007754541766507173,
        },
        "q3.xy.-y90_Square.wf.Q": {
            "type": "constant",
            "sample": -0.12499759466013702,
        },
        "q3.xy.saturation.wf.I": {
            "type": "constant",
            "sample": 0.25,
        },
        "q3.xy.saturation.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q3.z.const.wf": {
            "type": "constant",
            "sample": 0.1,
        },
        "q3.resonator.readout.wf.I": {
            "type": "constant",
            "sample": 0.07,
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
        "q4.xy.x180_DragGaussian.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0006498968918466012, 0.0015474362292148176, 0.0027582346770046824, 0.004353146562558655, 0.006403617363338815, 0.008975125094896994, 0.012118907499775265, 0.01586252585821134, 0.020200191562160446, 0.025084109380546244, 0.030418289791375116, 0.036056274793159086, 0.04180395515556691, 0.04742812416579708, 0.052670661968306484, 0.05726738063316262, 0.060969730612451166, 0.06356693669118998] + [0.06490583790212616] * 2 + [0.06356693669118998, 0.060969730612451166, 0.05726738063316262, 0.052670661968306484, 0.04742812416579708, 0.04180395515556691, 0.036056274793159086, 0.030418289791375116, 0.025084109380546244, 0.020200191562160446, 0.01586252585821134, 0.012118907499775265, 0.008975125094896994, 0.006403617363338815, 0.004353146562558655, 0.0027582346770046824, 0.0015474362292148176, 0.0006498968918466012, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q4.xy.x180_DragGaussian.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0005793447109854115, 0.000809979569683236, 0.0011063107525303654, 0.001475695064343174, 0.0019215638584660867, 0.0024413970540909957, 0.0030247418842984384, 0.0036516197696027358, 0.0042917183129513444, 0.0049047553279782325, 0.005442308806032212, 0.005851226035371968, 0.0060784721978313335, 0.006076991049879842, 0.0058118827707409285, 0.0052660191423930655, 0.004444169093693638, 0.003374830747284554, 0.0021092572617706514, 0.00071758185909581, -0.00071758185909581, -0.0021092572617706514, -0.003374830747284554, -0.004444169093693638, -0.0052660191423930655, -0.0058118827707409285, -0.006076991049879842, -0.0060784721978313335, -0.005851226035371968, -0.005442308806032212, -0.0049047553279782325, -0.0042917183129513444, -0.0036516197696027358, -0.0030247418842984384, -0.0024413970540909957, -0.0019215638584660867, -0.001475695064343174, -0.0011063107525303654, -0.000809979569683236, -0.0005793447109854115],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q4.xy.x90_DragGaussian.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.00032178352861017047, 0.0007661822919650029, 0.0013656850774891763, 0.0021553739970616593, 0.0031706238587934183, 0.004443854800640172, 0.006000436172417335, 0.007854014394225036, 0.010001723351844606, 0.012419898186589335, 0.015061011594537292, 0.017852547807259294, 0.020698397497482965, 0.02348309299659454, 0.02607883138852682, 0.028354805270788087, 0.030187950274913545, 0.031473905242584976] + [0.032136835565103224] * 2 + [0.031473905242584976, 0.030187950274913545, 0.028354805270788087, 0.02607883138852682, 0.02348309299659454, 0.020698397497482965, 0.017852547807259294, 0.015061011594537292, 0.012419898186589335, 0.010001723351844606, 0.007854014394225036, 0.006000436172417335, 0.004443854800640172, 0.0031706238587934183, 0.0021553739970616593, 0.0013656850774891763, 0.0007661822919650029, 0.00032178352861017047, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q4.xy.x90_DragGaussian.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0002868510185559214, 0.00040104528472854884, 0.0005477677800198204, 0.0007306610801102914, 0.0009514241514066799, 0.0012088092259861206, 0.001497640824068233, 0.0018080269491160678, 0.002124959020219991, 0.0024284921134518937, 0.002694651033666745, 0.002897118272112162, 0.003009634692696236, 0.003008901331727436, 0.0028776382366190734, 0.002607364710659227, 0.0022004419941841283, 0.0016709803661896084, 0.0010443568094481502, 0.0003552963948333482, -0.0003552963948333482, -0.0010443568094481502, -0.0016709803661896084, -0.0022004419941841283, -0.002607364710659227, -0.0028776382366190734, -0.003008901331727436, -0.003009634692696236, -0.002897118272112162, -0.002694651033666745, -0.0024284921134518937, -0.002124959020219991, -0.0018080269491160678, -0.001497640824068233, -0.0012088092259861206, -0.0009514241514066799, -0.0007306610801102914, -0.0005477677800198204, -0.00040104528472854884, -0.0002868510185559214],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q4.xy.-x90_DragGaussian.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.00032178352861017047, 0.0007661822919650029, 0.0013656850774891763, 0.0021553739970616593, 0.0031706238587934183, 0.004443854800640172, 0.006000436172417335, 0.007854014394225036, 0.010001723351844606, 0.012419898186589335, 0.015061011594537292, 0.017852547807259294, 0.020698397497482965, 0.02348309299659454, 0.02607883138852682, 0.028354805270788087, 0.030187950274913545, 0.031473905242584976] + [0.032136835565103224] * 2 + [0.031473905242584976, 0.030187950274913545, 0.028354805270788087, 0.02607883138852682, 0.02348309299659454, 0.020698397497482965, 0.017852547807259294, 0.015061011594537292, 0.012419898186589335, 0.010001723351844606, 0.007854014394225036, 0.006000436172417335, 0.004443854800640172, 0.0031706238587934183, 0.0021553739970616593, 0.0013656850774891763, 0.0007661822919650029, 0.00032178352861017047, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q4.xy.-x90_DragGaussian.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0002868510185559214, 0.00040104528472854884, 0.0005477677800198204, 0.0007306610801102914, 0.0009514241514066799, 0.0012088092259861206, 0.001497640824068233, 0.0018080269491160678, 0.002124959020219991, 0.0024284921134518937, 0.002694651033666745, 0.002897118272112162, 0.003009634692696236, 0.003008901331727436, 0.0028776382366190734, 0.002607364710659227, 0.0022004419941841283, 0.0016709803661896084, 0.0010443568094481502, 0.0003552963948333482, -0.0003552963948333482, -0.0010443568094481502, -0.0016709803661896084, -0.0022004419941841283, -0.002607364710659227, -0.0028776382366190734, -0.003008901331727436, -0.003009634692696236, -0.002897118272112162, -0.002694651033666745, -0.0024284921134518937, -0.002124959020219991, -0.0018080269491160678, -0.001497640824068233, -0.0012088092259861206, -0.0009514241514066799, -0.0007306610801102914, -0.0005477677800198204, -0.00040104528472854884, -0.0002868510185559214],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q4.xy.y180_DragGaussian.wf.I": {
            "type": "arbitrary",
            "samples": [-0.0005793335628179895, -0.0008139957055474568, -0.0011158891911998963, -0.001492777744761592, -0.0019485322078209729, -0.0024810757696143446, -0.0030803620659670067, -0.003726730762007121, -0.004390041024054074, -0.005029975530478339, -0.005597816700307333, -0.006039817360796476, -0.006302035142562035, -0.006336210525056517, -0.006105997630115078, -0.005592667288349217, -0.0047993494117796656, -0.0037529996643866905, -0.0025035626463586675, -0.0011202200755915503, 0.0003149160261480596, 0.0017148707014934673, 0.002996531948343581, 0.0040888177398143485, 0.0049391683313847155, 0.005517544238513859, 0.005817537699042059, 0.005854675320436897, 0.005662409522951777, 0.005286591462120006, 0.0047793463638219884, 0.004193230433190394, 0.00357636824301281, 0.0029690052941141977, 0.002401624380333158, 0.0018945215568848318, 0.0014585555911541342, 0.001096689737007172, 0.0008059322614006606, 0.0005793335628179895],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q4.xy.y180_DragGaussian.wf.Q": {
            "type": "arbitrary",
            "samples": [-3.5940422068331202e-06, 0.0006448595697408939, 0.001540543305984651, 0.0027490269298612595, 0.004341142118425015, 0.0063883486079902635, 0.008956187999267909, 0.012096020988629795, 0.015835596372958855, 0.02016937555151617, 0.025049864605326398, 0.03038140559943387, 0.03601787235917081, 0.04176545130907999, 0.04739115672958542, 0.05263697998925742, 0.05723870865717116, 0.06094762117627558, 0.06355262843166949, 0.06490013732253438, 0.06490904055212998, 0.06357879854932182, 0.06098949360185111, 0.05729384864893831, 0.05270231689387008, 0.04746326630988582, 0.04184085015853757, 0.03609328958562623, 0.030454003322116376, 0.025117388782834565, 0.020230230159588657, 0.015888844867211437, 0.012141327609459854, 0.008993716778907423, 0.006418639672669586, 0.004364983473940993, 0.002767336272278984, 0.0015542695986842233, 0.0006549092023858959, 3.5940422068331202e-06],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q4.xy.y90_DragGaussian.wf.I": {
            "type": "arbitrary",
            "samples": [-0.0002868454987624041, -0.0004030337945767724, -0.0005525103535454456, -0.0007391192297831412, -0.0009647769935653026, -0.0012284553533210949, -0.0015251800515115226, -0.001845216664094732, -0.0021736415563546963, -0.0024904924078359373, -0.002771647676633299, -0.0029904955184441714, -0.003120327441229808, -0.0031372487026000992, -0.0030232633633944708, -0.0027690980476522435, -0.0023763024691001735, -0.001858223188985775, -0.0012395892833906021, -0.0005546547048710677, 0.00015592441105832198, 0.0008490841429766593, 0.001483673234982481, 0.002024496834294567, 0.0024455310280937963, 0.002731902362676288, 0.0028804381619697006, 0.0028988261170538746, 0.00280362952891507, 0.0026175506858754213, 0.002366398357485651, 0.0020761947041070695, 0.0017707676514286989, 0.0014700439592621505, 0.0011891165770988583, 0.0009380346932730496, 0.0007221748106258845, 0.0005430041254113643, 0.0003990413404769618, 0.0002868454987624041],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q4.xy.y90_DragGaussian.wf.Q": {
            "type": "arbitrary",
            "samples": [-1.7795185633256134e-06, 0.00031928939869163087, 0.0007627693980317209, 0.0013611260445048178, 0.002149430235149904, 0.003163063838065235, 0.004434478474134223, 0.005989104371317257, 0.007840680794854251, 0.009986465416674875, 0.012402942566790332, 0.015042749120009887, 0.01783353360535897, 0.020679333083199615, 0.023464789305321206, 0.02606215442606561, 0.028340608911761746, 0.030177003227039617, 0.03146682079227518, 0.03213401303642341, 0.032138421293596564, 0.03147977840587199, 0.030197735526304628, 0.02836791038271963, 0.02609450469574453, 0.02350049293075282, 0.020716665324876704, 0.017870874946041275, 0.015078694439439653, 0.0124363758211691, 0.01001659636631231, 0.007867045728413312, 0.006011537044104282, 0.004453060103448565, 0.0031780618566742726, 0.002161234808461499, 0.0013701915514854203, 0.0007695656990373379, 0.0003242652745487322, 1.7795185633256134e-06],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q4.xy.-y90_DragGaussian.wf.I": {
            "type": "arbitrary",
            "samples": [-0.0002868454987624041, -0.0004030337945767724, -0.0005525103535454456, -0.0007391192297831412, -0.0009647769935653026, -0.0012284553533210949, -0.0015251800515115226, -0.001845216664094732, -0.0021736415563546963, -0.0024904924078359373, -0.002771647676633299, -0.0029904955184441714, -0.003120327441229808, -0.0031372487026000992, -0.0030232633633944708, -0.0027690980476522435, -0.0023763024691001735, -0.001858223188985775, -0.0012395892833906021, -0.0005546547048710677, 0.00015592441105832198, 0.0008490841429766593, 0.001483673234982481, 0.002024496834294567, 0.0024455310280937963, 0.002731902362676288, 0.0028804381619697006, 0.0028988261170538746, 0.00280362952891507, 0.0026175506858754213, 0.002366398357485651, 0.0020761947041070695, 0.0017707676514286989, 0.0014700439592621505, 0.0011891165770988583, 0.0009380346932730496, 0.0007221748106258845, 0.0005430041254113643, 0.0003990413404769618, 0.0002868454987624041],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q4.xy.-y90_DragGaussian.wf.Q": {
            "type": "arbitrary",
            "samples": [-1.7795185633256134e-06, 0.00031928939869163087, 0.0007627693980317209, 0.0013611260445048178, 0.002149430235149904, 0.003163063838065235, 0.004434478474134223, 0.005989104371317257, 0.007840680794854251, 0.009986465416674875, 0.012402942566790332, 0.015042749120009887, 0.01783353360535897, 0.020679333083199615, 0.023464789305321206, 0.02606215442606561, 0.028340608911761746, 0.030177003227039617, 0.03146682079227518, 0.03213401303642341, 0.032138421293596564, 0.03147977840587199, 0.030197735526304628, 0.02836791038271963, 0.02609450469574453, 0.02350049293075282, 0.020716665324876704, 0.017870874946041275, 0.015078694439439653, 0.0124363758211691, 0.01001659636631231, 0.007867045728413312, 0.006011537044104282, 0.004453060103448565, 0.0031780618566742726, 0.002161234808461499, 0.0013701915514854203, 0.0007695656990373379, 0.0003242652745487322, 1.7795185633256134e-06],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q4.xy.x180_Square.wf.I": {
            "type": "constant",
            "sample": 0.25,
        },
        "q4.xy.x180_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q4.xy.x90_Square.wf.I": {
            "type": "constant",
            "sample": 0.125,
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
            "sample": -0.0015509083533014347,
        },
        "q4.xy.y180_Square.wf.Q": {
            "type": "constant",
            "sample": 0.24999518932027404,
        },
        "q4.xy.y90_Square.wf.I": {
            "type": "constant",
            "sample": -0.0007754541766507173,
        },
        "q4.xy.y90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.12499759466013702,
        },
        "q4.xy.-y90_Square.wf.I": {
            "type": "constant",
            "sample": 0.0007754541766507173,
        },
        "q4.xy.-y90_Square.wf.Q": {
            "type": "constant",
            "sample": -0.12499759466013702,
        },
        "q4.xy.saturation.wf.I": {
            "type": "constant",
            "sample": 0.25,
        },
        "q4.xy.saturation.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q4.z.const.wf": {
            "type": "constant",
            "sample": 0.25,
        },
        "q4.resonator.readout.wf.I": {
            "type": "constant",
            "sample": 0.04,
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
        "q5.xy.x180_DragGaussian.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.0007836916625405736, 0.0018660081104605744, 0.0033260745616999774, 0.005249332178218227, 0.007721934972622112, 0.010822840969655936, 0.014613836265147194, 0.019128156201197406, 0.024358820464591792, 0.03024819418343967, 0.036680526399363776, 0.043479207689979656, 0.05041016740909522, 0.05719218839939841, 0.06351401147306555, 0.06905706012876321, 0.07352161573285519, 0.07665351061547873] + [0.07826805244379051] * 2 + [0.07665351061547873, 0.07352161573285519, 0.06905706012876321, 0.06351401147306555, 0.05719218839939841, 0.05041016740909522, 0.043479207689979656, 0.036680526399363776, 0.03024819418343967, 0.024358820464591792, 0.019128156201197406, 0.014613836265147194, 0.010822840969655936, 0.007721934972622112, 0.005249332178218227, 0.0033260745616999774, 0.0018660081104605744, 0.0007836916625405736, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q5.xy.x180_DragGaussian.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0006986148501898236, 0.0009767306838248163, 0.0013340677941596922, 0.0017794975370508362, 0.0023171576811827806, 0.002944009334782045, 0.003647447811800682, 0.004403381527298437, 0.005175257647833994, 0.005914501062493579, 0.006562721086632465, 0.007055822419048745, 0.007329851922956238, 0.007328065849941987, 0.007008379526406399, 0.006350138534970269, 0.005359093587526005, 0.004069609737042336, 0.002543491669126166, 0.0008653109858178682, -0.0008653109858178682, -0.002543491669126166, -0.004069609737042336, -0.005359093587526005, -0.006350138534970269, -0.007008379526406399, -0.007328065849941987, -0.007329851922956238, -0.007055822419048745, -0.006562721086632465, -0.005914501062493579, -0.005175257647833994, -0.004403381527298437, -0.003647447811800682, -0.002944009334782045, -0.0023171576811827806, -0.0017794975370508362, -0.0013340677941596922, -0.0009767306838248163, -0.0006986148501898236],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q5.xy.x90_DragGaussian.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.00034721322995930233, 0.0008267316524242431, 0.0014736115577770744, 0.002325707504428234, 0.003421189878029372, 0.004795040894307784, 0.006474634775708675, 0.008474696382826405, 0.010792133100014693, 0.013401409897383625, 0.016251243513862423, 0.019263387451601974, 0.02233413711734484, 0.025338899737966752, 0.0281397724709028, 0.030595610550546413, 0.03257362415682161, 0.033961204745038505] + [0.03467652469790774] * 2 + [0.033961204745038505, 0.03257362415682161, 0.030595610550546413, 0.0281397724709028, 0.025338899737966752, 0.02233413711734484, 0.019263387451601974, 0.016251243513862423, 0.013401409897383625, 0.010792133100014693, 0.008474696382826405, 0.006474634775708675, 0.004795040894307784, 0.003421189878029372, 0.002325707504428234, 0.0014736115577770744, 0.0008267316524242431, 0.00034721322995930233, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q5.xy.x90_DragGaussian.wf.Q": {
            "type": "arbitrary",
            "samples": [0.00030952009601018876, 0.0004327388330657594, 0.0005910564191703228, 0.0007884032931281259, 0.0010266126861683022, 0.0013043382225686104, 0.0016159954180675464, 0.0019509105378000123, 0.0022928889123954308, 0.002620409423329551, 0.002907602179184481, 0.0031260698680845513, 0.0032474781638515615, 0.0032466868473046803, 0.003105050376899, 0.0028134178488876155, 0.002374337106186521, 0.0018030335258276927, 0.0011268895664258156, 0.0003833745293794487, -0.0003833745293794487, -0.0011268895664258156, -0.0018030335258276927, -0.002374337106186521, -0.0028134178488876155, -0.003105050376899, -0.0032466868473046803, -0.0032474781638515615, -0.0031260698680845513, -0.002907602179184481, -0.002620409423329551, -0.0022928889123954308, -0.0019509105378000123, -0.0016159954180675464, -0.0013043382225686104, -0.0010266126861683022, -0.0007884032931281259, -0.0005910564191703228, -0.0004327388330657594, -0.00030952009601018876],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q5.xy.-x90_DragGaussian.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -0.0004890327182525387, -0.0011644107780623145, -0.002075509236305739, -0.003275644372434133, -0.004818577292999117, -0.00675357872437716, -0.009119203909448838, -0.011936192088487896, -0.01520018746480943, -0.018875225207582575, -0.022889075371637223, -0.027131531621974618, -0.03145653115118992, -0.03568859118023487, -0.03963348235338423, -0.04309240922612172, -0.04587834388284734, -0.04783268273949085] + [-0.048840175630855964] * 2 + [-0.04783268273949085, -0.04587834388284734, -0.04309240922612172, -0.03963348235338423, -0.03568859118023487, -0.03145653115118992, -0.027131531621974618, -0.022889075371637223, -0.018875225207582575, -0.01520018746480943, -0.011936192088487896, -0.009119203909448838, -0.00675357872437716, -0.004818577292999117, -0.003275644372434133, -0.002075509236305739, -0.0011644107780623145, -0.0004890327182525387, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q5.xy.-x90_DragGaussian.wf.Q": {
            "type": "arbitrary",
            "samples": [-0.000435943797197449, -0.0006094913141771259, -0.0008324738298173561, -0.0011104271734198958, -0.0014459333608004257, -0.0018370960881248035, -0.002276049884602178, -0.002747761320845089, -0.0032294210033738465, -0.0036907174976472555, -0.004095214336879552, -0.00440291530716134, -0.004573912906833186, -0.0045727983764854655, -0.004373310389998592, -0.003962560350545937, -0.0033441367692767913, -0.0025394838391939335, -0.0015871684034166418, -0.0005399641258865475, 0.0005399641258865475, 0.0015871684034166418, 0.0025394838391939335, 0.0033441367692767913, 0.003962560350545937, 0.004373310389998592, 0.0045727983764854655, 0.004573912906833186, 0.00440291530716134, 0.004095214336879552, 0.0036907174976472555, 0.0032294210033738465, 0.002747761320845089, 0.002276049884602178, 0.0018370960881248035, 0.0014459333608004257, 0.0011104271734198958, 0.0008324738298173561, 0.0006094913141771259, 0.000435943797197449],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q5.xy.y180_DragGaussian.wf.I": {
            "type": "arbitrary",
            "samples": [-0.0006986014069406393, -0.0009815736246542102, -0.0013456181533314966, -0.0018000970419657161, -0.0023496780252666763, -0.002991856737848726, -0.0037145185628528928, -0.004493955677215065, -0.005293822130748588, -0.006065500443952598, -0.006750243510160872, -0.007283239185026368, -0.007599439942281348, -0.007640651036935086, -0.007363044037058067, -0.006744033984820482, -0.0057873951496270745, -0.004525632578639331, -0.0030189730051246476, -0.0013508406402086416, 0.0003797480295549658, 0.002067912445737238, 0.0036134302747329043, 0.004930585778361967, 0.005955998697258397, 0.006653445295200335, 0.007015198639126369, 0.007059981811070808, 0.006828134106656232, 0.006374946093909828, 0.005763274058871755, 0.005056493992863055, 0.004312637911315896, 0.003580236687122554, 0.0028960486302272046, 0.0022845481602710546, 0.001758829547394165, 0.0013224660928047643, 0.0009718501530874353, 0.0006986014069406393],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q5.xy.y180_DragGaussian.wf.Q": {
            "type": "arbitrary",
            "samples": [-4.333950427599311e-06, 0.0007776173030763251, 0.0018576961358477018, 0.0033149712086025674, 0.0052348563699800375, 0.007703522826919997, 0.010800005279651205, 0.014586238090429995, 0.019095682722198425, 0.024321660338243036, 0.030206899410127063, 0.03663604883058857, 0.04343289931750481, 0.050363736746252996, 0.0571476104487911, 0.0634733953592023, 0.06902248543112276, 0.07349495461012687, 0.07663625670361617, 0.07826117828151374, 0.07827191442580261, 0.07666781448342576, 0.07354544734401372, 0.06908897713521091, 0.06355218322239034, 0.05723456528359598, 0.050454658014574744, 0.04352384274611101, 0.036723592302021484, 0.03028832484175623, 0.02439504313107049, 0.01915989352473053, 0.014640872019977678, 0.010845260137887626, 0.007740049936276083, 0.005263605963609341, 0.0033370499093616996, 0.0018742482709343633, 0.0007897358612880829, 4.333950427599311e-06],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q5.xy.y90_DragGaussian.wf.I": {
            "type": "arbitrary",
            "samples": [-0.00043593540845350163, -0.0006125133656181951, -0.0008396813883669383, -0.001123281504229698, -0.0014662264339898217, -0.0018669534245001442, -0.0023179028138472987, -0.0028042806445208704, -0.003303406620599842, -0.0037849428690515776, -0.004212230511600758, -0.0045448260158726, -0.0047421389684343595, -0.004767855171124772, -0.0045946251723320225, -0.004208355695520126, -0.003611401928723668, -0.0028240473996744295, -0.0018838742908671767, -0.0008429402809590696, 0.00023696719005824012, 0.001290401433095227, 0.0022548225455660802, 0.00307674290926226, 0.003716612504701818, 0.004151827298900133, 0.0043775655956986344, 0.004405510816191299, 0.004260835150326854, 0.003978040556041674, 0.003596350087364212, 0.003155311100466671, 0.0026911362483718836, 0.002234109360580776, 0.0018071680503022167, 0.0014255846402325984, 0.001097530107334171, 0.0008252342331479699, 0.0006064458061959906, 0.00043593540845350163],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q5.xy.y90_DragGaussian.wf.Q": {
            "type": "arbitrary",
            "samples": [-2.704435506573881e-06, 0.00048524224725171876, 0.0011592240091667493, 0.002068580614748963, 0.003266611299619915, 0.004807087899795191, 0.006739328988045931, 0.009101982327229873, 0.011915928259656917, 0.01517699911348765, 0.018849456788435155, 0.022861320851078854, 0.02710263465860026, 0.03142755787720306, 0.035660774020245, 0.03960813742563163, 0.043070834212403875, 0.045861707031975105, 0.04782191609768266, 0.04883588607359181, 0.048842585552578366, 0.047841608519562304, 0.045893215085569344, 0.04311232580960431, 0.039657301969216616, 0.03571503484916843, 0.0314842938068035, 0.02715938441647611, 0.0229159489961089, 0.018900267205424166, 0.015222790830261866, 0.011955996547740592, 0.009136074535112892, 0.006767568546274413, 0.004829881241146312, 0.0032845513806405756, 0.0020823579809808816, 0.0011695527340992978, 0.0004928043686150945, 2.704435506573881e-06],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q5.xy.-y90_DragGaussian.wf.I": {
            "type": "arbitrary",
            "samples": [0.00043593540845350163, 0.0006125133656181951, 0.0008396813883669383, 0.001123281504229698, 0.0014662264339898217, 0.0018669534245001442, 0.0023179028138472987, 0.0028042806445208704, 0.003303406620599842, 0.0037849428690515776, 0.004212230511600758, 0.0045448260158726, 0.0047421389684343595, 0.004767855171124772, 0.0045946251723320225, 0.004208355695520126, 0.003611401928723668, 0.0028240473996744295, 0.0018838742908671767, 0.0008429402809590696, -0.00023696719005824012, -0.001290401433095227, -0.0022548225455660802, -0.00307674290926226, -0.003716612504701818, -0.004151827298900133, -0.0043775655956986344, -0.004405510816191299, -0.004260835150326854, -0.003978040556041674, -0.003596350087364212, -0.003155311100466671, -0.0026911362483718836, -0.002234109360580776, -0.0018071680503022167, -0.0014255846402325984, -0.001097530107334171, -0.0008252342331479699, -0.0006064458061959906, -0.00043593540845350163],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q5.xy.-y90_DragGaussian.wf.Q": {
            "type": "arbitrary",
            "samples": [2.704435506573881e-06, -0.00048524224725171876, -0.0011592240091667493, -0.002068580614748963, -0.003266611299619915, -0.004807087899795191, -0.006739328988045931, -0.009101982327229873, -0.011915928259656917, -0.01517699911348765, -0.018849456788435155, -0.022861320851078854, -0.02710263465860026, -0.03142755787720306, -0.035660774020245, -0.03960813742563163, -0.043070834212403875, -0.045861707031975105, -0.04782191609768266, -0.04883588607359181, -0.048842585552578366, -0.047841608519562304, -0.045893215085569344, -0.04311232580960431, -0.039657301969216616, -0.03571503484916843, -0.0314842938068035, -0.02715938441647611, -0.0229159489961089, -0.018900267205424166, -0.015222790830261866, -0.011955996547740592, -0.009136074535112892, -0.006767568546274413, -0.004829881241146312, -0.0032845513806405756, -0.0020823579809808816, -0.0011695527340992978, -0.0004928043686150945, -2.704435506573881e-06],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q5.xy.x180_Square.wf.I": {
            "type": "constant",
            "sample": 0.25,
        },
        "q5.xy.x180_Square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q5.xy.x90_Square.wf.I": {
            "type": "constant",
            "sample": 0.125,
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
            "sample": -0.0015509083533014347,
        },
        "q5.xy.y180_Square.wf.Q": {
            "type": "constant",
            "sample": 0.24999518932027404,
        },
        "q5.xy.y90_Square.wf.I": {
            "type": "constant",
            "sample": -0.0007754541766507173,
        },
        "q5.xy.y90_Square.wf.Q": {
            "type": "constant",
            "sample": 0.12499759466013702,
        },
        "q5.xy.-y90_Square.wf.I": {
            "type": "constant",
            "sample": 0.0007754541766507173,
        },
        "q5.xy.-y90_Square.wf.Q": {
            "type": "constant",
            "sample": -0.12499759466013702,
        },
        "q5.xy.saturation.wf.I": {
            "type": "constant",
            "sample": 0.25,
        },
        "q5.xy.saturation.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q5.z.const.wf": {
            "type": "constant",
            "sample": 0.1,
        },
        "q5.resonator.readout.wf.I": {
            "type": "constant",
            "sample": 0.04,
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
        "coupler_q1_q2.const.wf": {
            "type": "constant",
            "sample": -0.0394572,
        },
        "coupler_q2_q3.const.wf": {
            "type": "constant",
            "sample": -0.0394572,
        },
        "coupler_q3_q4.const.wf": {
            "type": "constant",
            "sample": -0.0394572,
        },
        "coupler_q4_q5.const.wf": {
            "type": "constant",
            "sample": -0.0394572,
        },
    },
    "digital_waveforms": {
        "ON": {
            "samples": [(1, 0)],
        },
    },
    "integration_weights": {
        "q1.resonator.readout.iw1": {
            "cosine": [(-0.029060953277058484, 1024)],
            "sine": [(-0.9995776413038803, 1024)],
        },
        "q1.resonator.readout.iw2": {
            "cosine": [(0.9995776413038803, 1024)],
            "sine": [(-0.029060953277058484, 1024)],
        },
        "q1.resonator.readout.iw3": {
            "cosine": [(-0.9995776413038803, 1024)],
            "sine": [(0.029060953277058484, 1024)],
        },
        "q2.resonator.readout.iw1": {
            "cosine": [(-0.8801804205828955, 1024)],
            "sine": [(0.4746392600939341, 1024)],
        },
        "q2.resonator.readout.iw2": {
            "cosine": [(-0.4746392600939341, 1024)],
            "sine": [(-0.8801804205828955, 1024)],
        },
        "q2.resonator.readout.iw3": {
            "cosine": [(0.4746392600939341, 1024)],
            "sine": [(0.8801804205828955, 1024)],
        },
        "q3.resonator.readout.iw1": {
            "cosine": [(0.9989571756591297, 1024)],
            "sine": [(-0.04565699507342608, 1024)],
        },
        "q3.resonator.readout.iw2": {
            "cosine": [(0.04565699507342608, 1024)],
            "sine": [(0.9989571756591297, 1024)],
        },
        "q3.resonator.readout.iw3": {
            "cosine": [(-0.04565699507342608, 1024)],
            "sine": [(-0.9989571756591297, 1024)],
        },
        "q4.resonator.readout.iw1": {
            "cosine": [(-0.6759890289182044, 1024)],
            "sine": [(0.7369116858770954, 1024)],
        },
        "q4.resonator.readout.iw2": {
            "cosine": [(-0.7369116858770954, 1024)],
            "sine": [(-0.6759890289182044, 1024)],
        },
        "q4.resonator.readout.iw3": {
            "cosine": [(0.7369116858770954, 1024)],
            "sine": [(0.6759890289182044, 1024)],
        },
        "q5.resonator.readout.iw1": {
            "cosine": [(-0.7244823567994584, 1024)],
            "sine": [(0.6892933444378396, 1024)],
        },
        "q5.resonator.readout.iw2": {
            "cosine": [(-0.6892933444378396, 1024)],
            "sine": [(-0.7244823567994584, 1024)],
        },
        "q5.resonator.readout.iw3": {
            "cosine": [(0.6892933444378396, 1024)],
            "sine": [(0.7244823567994584, 1024)],
        },
    },
    "mixers": {
        "q1.xy_mixer_1a7": [{'intermediate_frequency': 385991173.03796864, 'lo_frequency': 4700000000.0, 'correction': (1, 0, 0, 1)}],
        "q1.resonator_mixer_e75": [{'intermediate_frequency': -287531678.0, 'lo_frequency': 6200000000.0, 'correction': (1, 0, 0, 1)}],
        "q2.xy_mixer_e8f": [{'intermediate_frequency': -264564380.79657173, 'lo_frequency': 4700000000.0, 'correction': (1, 0, 0, 1)}],
        "q2.resonator_mixer_76d": [{'intermediate_frequency': -185741282.0, 'lo_frequency': 6200000000.0, 'correction': (1, 0, 0, 1)}],
        "q3.xy_mixer_244": [{'intermediate_frequency': -236154100.04951477, 'lo_frequency': 4700000000.0, 'correction': (1, 0, 0, 1)}],
        "q3.resonator_mixer_397": [{'intermediate_frequency': -343278899.0, 'lo_frequency': 6200000000.0, 'correction': (1, 0, 0, 1)}],
        "q4.xy_mixer_96e": [{'intermediate_frequency': -284600668.894413, 'lo_frequency': 4700000000.0, 'correction': (1, 0, 0, 1)}],
        "q4.resonator_mixer_9ec": [{'intermediate_frequency': -162578680.0, 'lo_frequency': 6200000000.0, 'correction': (1, 0, 0, 1)}],
        "q5.xy_mixer_a3f": [{'intermediate_frequency': -345901097.018157, 'lo_frequency': 4700000000.0, 'correction': (1, 0, 0, 1)}],
        "q5.resonator_mixer_685": [{'intermediate_frequency': -257761381.0, 'lo_frequency': 6200000000.0, 'correction': (1, 0, 0, 1)}],
    },
}


