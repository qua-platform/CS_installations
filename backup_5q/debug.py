
# Single QUA script generated at 2025-01-09 14:23:56.010057
# QUA library version: 1.2.1

from qm import CompilerOptionArguments
from qm.qua import *

with program() as prog:
    v1 = declare(fixed, )
    v2 = declare(fixed, )
    v3 = declare(int, )
    v4 = declare(fixed, )
    v5 = declare(fixed, )
    v6 = declare(bool, )
    a1 = declare(fixed, value=[0.0, 0.0])
    a2 = declare(fixed, value=[-0.015, -0.012777777777777777, -0.010555555555555554, -0.008333333333333333, -0.0061111111111111106, -0.003888888888888888, -0.001666666666666667, 0.0005555555555555557, 0.0027777777777777783, 0.005])
    a3 = declare(fixed, value=[0.015, 0.012777777777777777, 0.010555555555555554, 0.008333333333333333, 0.0061111111111111106, 0.003888888888888888, 0.001666666666666667, -0.0005555555555555557, -0.0027777777777777783, -0.005])
    v7 = declare(fixed, )
    v8 = declare(fixed, )
    v9 = declare(fixed, )
    v10 = declare(fixed, )
    wait((4+(0*((Cast.to_int(v4)+Cast.to_int(v5))+Cast.to_int(v6)))), "tank_circuit1")
    with for_(v3,0,(v3<200),(v3+1)):
        with for_each_((v1,v2),(a2,a3)):
            play("step%"*amp(((-0.025-a1[0])*4)), "P1_sticky")
            assign(a1[0], -0.025)
            play("step%"*amp(((0.025-a1[1])*4)), "P2_sticky")
            assign(a1[1], 0.025)
            assign(v7, v1)
            assign(v8, ((v7+a1[0])>>1))
            play(ramp((((v1-a1[0])*0.019230769230769232)/4)), "P1_sticky", duration=13)
            wait(13, "P1_sticky")
            assign(a1[0], v1)
            assign(v9, v2)
            assign(v10, ((v9+a1[1])>>1))
            play(ramp((((v2-a1[1])*0.019230769230769232)/4)), "P2_sticky", duration=13)
            wait(13, "P2_sticky")
            assign(a1[1], v2)
            align()
            measure("readout", "tank_circuit1", None, demod.full("cos", v4, "out1"), demod.full("sin", v5, "out1"))
            assign(v6, (v4>0.0))
            r2 = declare_stream()
            save(v4, r2)
            r3 = declare_stream()
            save(v5, r3)
            r4 = declare_stream()
            save(v6, r4)
            align()
        r1 = declare_stream()
        save(v3, r1)
    with stream_processing():
        r1.save("iteration")
        r2.buffer(10).buffer(200).save("I_tank_circuit1")
        r3.buffer(10).buffer(200).save("Q_tank_circuit1")
        r4.map(FUNCTIONS.boolean_to_int()).buffer(10).buffer(200).save("P_tank_circuit1")


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
                            "sampling_rate": 1000000000,
                            "upsampling_mode": "mw",
                        },
                        "2": {
                            "offset": 0.0,
                            "output_mode": "direct",
                            "sampling_rate": 1000000000,
                            "upsampling_mode": "mw",
                        },
                        "3": {
                            "offset": 0.0,
                            "output_mode": "direct",
                            "sampling_rate": 1000000000,
                            "upsampling_mode": "mw",
                        },
                        "4": {
                            "offset": 0.0,
                            "output_mode": "direct",
                            "sampling_rate": 1000000000,
                            "upsampling_mode": "mw",
                        },
                        "5": {
                            "offset": 0.0,
                            "output_mode": "direct",
                            "sampling_rate": 1000000000,
                            "upsampling_mode": "mw",
                        },
                        "6": {
                            "offset": 0.0,
                            "output_mode": "direct",
                            "sampling_rate": 1000000000,
                            "upsampling_mode": "mw",
                        },
                        "8": {
                            "offset": 0.0,
                            "output_mode": "direct",
                            "sampling_rate": 1000000000,
                            "upsampling_mode": "mw",
                        },
                    },
                    "digital_outputs": {
                        "1": {},
                        "3": {},
                        "5": {},
                    },
                    "analog_inputs": {
                        "2": {
                            "offset": 0.0,
                            "gain_db": 0,
                            "sampling_rate": 1000000000,
                        },
                    },
                },
                "3": {
                    "type": "LF",
                    "analog_outputs": {
                        "1": {
                            "offset": 0.0,
                            "output_mode": "amplified",
                            "sampling_rate": 1000000000,
                            "upsampling_mode": "pulse",
                        },
                        "2": {
                            "offset": 0.0,
                            "output_mode": "amplified",
                            "sampling_rate": 1000000000,
                            "upsampling_mode": "pulse",
                        },
                        "3": {
                            "offset": 0.0,
                            "output_mode": "amplified",
                            "sampling_rate": 1000000000,
                            "upsampling_mode": "pulse",
                        },
                        "4": {
                            "offset": 0.0,
                            "output_mode": "amplified",
                            "sampling_rate": 1000000000,
                            "upsampling_mode": "pulse",
                        },
                        "5": {
                            "offset": 0.0,
                            "output_mode": "amplified",
                            "sampling_rate": 1000000000,
                            "upsampling_mode": "pulse",
                        },
                        "6": {
                            "offset": 0.0,
                            "output_mode": "amplified",
                            "sampling_rate": 1000000000,
                            "upsampling_mode": "pulse",
                        },
                        "7": {
                            "offset": 0.0,
                            "output_mode": "amplified",
                            "sampling_rate": 1000000000,
                            "upsampling_mode": "pulse",
                        },
                        "8": {
                            "offset": 0.0,
                            "output_mode": "amplified",
                            "sampling_rate": 1000000000,
                            "upsampling_mode": "pulse",
                        },
                    },
                    "digital_outputs": {},
                    "analog_inputs": {},
                },
            },
        },
    },
    "elements": {
        "P1": {
            "singleInput": {
                "port": ('con1', 3, 1),
            },
            "operations": {
                "step": "P1_step_pulse",
            },
        },
        "P2": {
            "singleInput": {
                "port": ('con1', 3, 2),
            },
            "operations": {
                "step": "P2_step_pulse",
            },
        },
        "P3": {
            "singleInput": {
                "port": ('con1', 3, 3),
            },
            "operations": {
                "step": "P3_step_pulse",
            },
        },
        "P4": {
            "singleInput": {
                "port": ('con1', 3, 4),
            },
            "operations": {
                "step": "P4_step_pulse",
            },
        },
        "P5": {
            "singleInput": {
                "port": ('con1', 3, 6),
            },
            "operations": {
                "step": "P5_step_pulse",
            },
        },
        "P1_sticky": {
            "singleInput": {
                "port": ('con1', 3, 1),
            },
            "sticky": {
                "analog": True,
                "duration": 4,
            },
            "operations": {
                "step": "step_pulse",
                "step%": "P1_sticky_step%_pulse",
            },
        },
        "P2_sticky": {
            "singleInput": {
                "port": ('con1', 3, 2),
            },
            "sticky": {
                "analog": True,
                "duration": 4,
            },
            "operations": {
                "step": "step_pulse",
                "step%": "P2_sticky_step%_pulse",
            },
        },
        "P3_sticky": {
            "singleInput": {
                "port": ('con1', 3, 3),
            },
            "sticky": {
                "analog": True,
                "duration": 4,
            },
            "operations": {
                "step": "P3_step_pulse",
            },
        },
        "P4_sticky": {
            "singleInput": {
                "port": ('con1', 3, 4),
            },
            "sticky": {
                "analog": True,
                "duration": 4,
            },
            "operations": {
                "step": "P4_step_pulse",
            },
        },
        "P5_sticky": {
            "singleInput": {
                "port": ('con1', 3, 6),
            },
            "sticky": {
                "analog": True,
                "duration": 4,
            },
            "operations": {
                "step": "P5_step_pulse",
            },
        },
        "B1": {
            "singleInput": {
                "port": ('con1', 3, 4),
            },
            "operations": {
                "step": "B1_step_pulse",
            },
        },
        "B2": {
            "singleInput": {
                "port": ('con1', 3, 5),
            },
            "operations": {
                "step": "B2_step_pulse",
            },
        },
        "B3": {
            "singleInput": {
                "port": ('con1', 3, 6),
            },
            "operations": {
                "step": "B3_step_pulse",
            },
        },
        "B4": {
            "singleInput": {
                "port": ('con1', 3, 6),
            },
            "operations": {
                "step": "B4_step_pulse",
            },
        },
        "B1_sticky": {
            "singleInput": {
                "port": ('con1', 3, 4),
            },
            "sticky": {
                "analog": True,
                "duration": 4,
            },
            "operations": {
                "step": "B1_step_pulse",
            },
        },
        "B2_sticky": {
            "singleInput": {
                "port": ('con1', 3, 5),
            },
            "sticky": {
                "analog": True,
                "duration": 4,
            },
            "operations": {
                "step": "B2_step_pulse",
            },
        },
        "B3_sticky": {
            "singleInput": {
                "port": ('con1', 3, 6),
            },
            "sticky": {
                "analog": True,
                "duration": 4,
            },
            "operations": {
                "step": "B3_step_pulse",
            },
        },
        "B4_sticky": {
            "singleInput": {
                "port": ('con1', 3, 6),
            },
            "sticky": {
                "analog": True,
                "duration": 4,
            },
            "operations": {
                "step": "B4_step_pulse",
            },
        },
        "Psd1": {
            "singleInput": {
                "port": ('con1', 3, 7),
            },
            "operations": {
                "step": "Psd1_step_pulse",
            },
        },
        "Psd2": {
            "singleInput": {
                "port": ('con1', 3, 8),
            },
            "operations": {
                "step": "Psd2_step_pulse",
            },
        },
        "Psd1_sticky": {
            "singleInput": {
                "port": ('con1', 3, 7),
            },
            "sticky": {
                "analog": True,
                "duration": 4,
            },
            "operations": {
                "step": "Psd1_step_pulse",
            },
        },
        "Psd2_sticky": {
            "singleInput": {
                "port": ('con1', 3, 8),
            },
            "sticky": {
                "analog": True,
                "duration": 4,
            },
            "operations": {
                "step": "Psd2_step_pulse",
            },
        },
        "qubit1": {
            "mixInputs": {
                "I": ('con1', 5, 5),
                "Q": ('con1', 5, 6),
                "lo_frequency": 16000000000,
                "mixer": "mixer_qubit1",
            },
            "digitalInputs": {
                "output_switch": {
                    "port": ('con1', 5, 1),
                    "delay": 40,
                    "buffer": 40,
                },
            },
            "intermediate_frequency": 0,
            "operations": {
                "const": "const_pulse",
                "saturation": "saturation_pulse",
                "x180_kaiser": "x180_kaiser_pulse_qubit1",
                "x90_kaiser": "x90_kaiser_pulse_qubit1",
                "-x90_kaiser": "minus_x90_kaiser_pulse_qubit1",
                "y180_kaiser": "y180_kaiser_pulse_qubit1",
                "y90_kaiser": "y90_kaiser_pulse_qubit1",
                "-y90_kaiser": "minus_y90_kaiser_pulse_qubit1",
                "x180_gauss": "x180_gaussian_pulse_qubit1",
                "x90_gauss": "x90_gaussian_pulse_qubit1",
                "-x90_gauss": "minus_x90_gaussian_pulse_qubit1",
                "y180_gauss": "y180_gaussian_pulse_qubit1",
                "y90_gauss": "y90_gaussian_pulse_qubit1",
                "-y90_gauss": "minus_y90_gaussian_pulse_qubit1",
                "x180_square": "square_x180_pulse",
                "x90_square": "square_x90_pulse",
                "-x90_square": "square_minus_x90_pulse",
                "y180_square": "square_y180_pulse",
                "y90_square": "square_y90_pulse",
                "-y90_square": "square_minus_y90_pulse",
            },
        },
        "qubit2": {
            "mixInputs": {
                "I": ('con1', 5, 5),
                "Q": ('con1', 5, 6),
                "lo_frequency": 16000000000,
                "mixer": "mixer_qubit2",
            },
            "digitalInputs": {
                "output_switch": {
                    "port": ('con1', 5, 1),
                    "delay": 40,
                    "buffer": 40,
                },
            },
            "intermediate_frequency": 0,
            "operations": {
                "const": "const_pulse",
                "saturation": "saturation_pulse",
                "x180_kaiser": "x180_kaiser_pulse_qubit2",
                "x90_kaiser": "x90_kaiser_pulse_qubit2",
                "-x90_kaiser": "minus_x90_kaiser_pulse_qubit2",
                "y180_kaiser": "y180_kaiser_pulse_qubit2",
                "y90_kaiser": "y90_kaiser_pulse_qubit2",
                "-y90_kaiser": "minus_y90_kaiser_pulse_qubit2",
                "x180_gauss": "x180_gaussian_pulse_qubit2",
                "x90_gauss": "x90_gaussian_pulse_qubit2",
                "-x90_gauss": "minus_x90_gaussian_pulse_qubit2",
                "y180_gauss": "y180_gaussian_pulse_qubit2",
                "y90_gauss": "y90_gaussian_pulse_qubit2",
                "-y90_gauss": "minus_y90_gaussian_pulse_qubit2",
                "x180_square": "square_x180_pulse",
                "x90_square": "square_x90_pulse",
                "-x90_square": "square_minus_x90_pulse",
                "y180_square": "square_y180_pulse",
                "y90_square": "square_y90_pulse",
                "-y90_square": "square_minus_y90_pulse",
            },
        },
        "qubit3": {
            "mixInputs": {
                "I": ('con1', 5, 5),
                "Q": ('con1', 5, 6),
                "lo_frequency": 16300000000,
                "mixer": "mixer_qubit3",
            },
            "digitalInputs": {
                "output_switch": {
                    "port": ('con1', 5, 3),
                    "delay": 40,
                    "buffer": 40,
                },
            },
            "intermediate_frequency": 0,
            "operations": {
                "const": "const_pulse",
                "saturation": "saturation_pulse",
                "x180_kaiser": "x180_kaiser_pulse_qubit3",
                "x90_kaiser": "x90_kaiser_pulse_qubit3",
                "-x90_kaiser": "minus_x90_kaiser_pulse_qubit3",
                "y180_kaiser": "y180_kaiser_pulse_qubit3",
                "y90_kaiser": "y90_kaiser_pulse_qubit3",
                "-y90_kaiser": "minus_y90_kaiser_pulse_qubit3",
                "x180_gauss": "x180_gaussian_pulse_qubit3",
                "x90_gauss": "x90_gaussian_pulse_qubit3",
                "-x90_gauss": "minus_x90_gaussian_pulse_qubit3",
                "y180_gauss": "y180_gaussian_pulse_qubit3",
                "y90_gauss": "y90_gaussian_pulse_qubit3",
                "-y90_gauss": "minus_y90_gaussian_pulse_qubit3",
                "x180_square": "square_x180_pulse",
                "x90_square": "square_x90_pulse",
                "-x90_square": "square_minus_x90_pulse",
                "y180_square": "square_y180_pulse",
                "y90_square": "square_y90_pulse",
                "-y90_square": "square_minus_y90_pulse",
            },
        },
        "qubit4": {
            "mixInputs": {
                "I": ('con1', 5, 5),
                "Q": ('con1', 5, 6),
                "lo_frequency": 16300000000,
                "mixer": "mixer_qubit4",
            },
            "digitalInputs": {
                "output_switch": {
                    "port": ('con1', 5, 3),
                    "delay": 40,
                    "buffer": 40,
                },
            },
            "intermediate_frequency": 50000000,
            "operations": {
                "const": "const_pulse",
                "saturation": "saturation_pulse",
                "x180_kaiser": "x180_kaiser_pulse_qubit4",
                "x90_kaiser": "x90_kaiser_pulse_qubit4",
                "-x90_kaiser": "minus_x90_kaiser_pulse_qubit4",
                "y180_kaiser": "y180_kaiser_pulse_qubit4",
                "y90_kaiser": "y90_kaiser_pulse_qubit4",
                "-y90_kaiser": "minus_y90_kaiser_pulse_qubit4",
                "x180_gauss": "x180_gaussian_pulse_qubit4",
                "x90_gauss": "x90_gaussian_pulse_qubit4",
                "-x90_gauss": "minus_x90_gaussian_pulse_qubit4",
                "y180_gauss": "y180_gaussian_pulse_qubit4",
                "y90_gauss": "y90_gaussian_pulse_qubit4",
                "-y90_gauss": "minus_y90_gaussian_pulse_qubit4",
                "x180_square": "square_x180_pulse",
                "x90_square": "square_x90_pulse",
                "-x90_square": "square_minus_x90_pulse",
                "y180_square": "square_y180_pulse",
                "y90_square": "square_y90_pulse",
                "-y90_square": "square_minus_y90_pulse",
            },
        },
        "qubit5": {
            "mixInputs": {
                "I": ('con1', 5, 5),
                "Q": ('con1', 5, 6),
                "lo_frequency": 16300000000,
                "mixer": "mixer_qubit5",
            },
            "digitalInputs": {
                "output_switch": {
                    "port": ('con1', 5, 5),
                    "delay": 40,
                    "buffer": 40,
                },
            },
            "intermediate_frequency": 0,
            "operations": {
                "const": "const_pulse",
                "saturation": "saturation_pulse",
                "x180_kaiser": "x180_kaiser_pulse_qubit5",
                "x90_kaiser": "x90_kaiser_pulse_qubit5",
                "-x90_kaiser": "minus_x90_kaiser_pulse_qubit5",
                "y180_kaiser": "y180_kaiser_pulse_qubit5",
                "y90_kaiser": "y90_kaiser_pulse_qubit5",
                "-y90_kaiser": "minus_y90_kaiser_pulse_qubit5",
                "x180_gauss": "x180_gaussian_pulse_qubit5",
                "x90_gauss": "x90_gaussian_pulse_qubit5",
                "-x90_gauss": "minus_x90_gaussian_pulse_qubit5",
                "y180_gauss": "y180_gaussian_pulse_qubit5",
                "y90_gauss": "y90_gaussian_pulse_qubit5",
                "-y90_gauss": "minus_y90_gaussian_pulse_qubit5",
                "x180_square": "square_x180_pulse",
                "x90_square": "square_x90_pulse",
                "-x90_square": "square_minus_x90_pulse",
                "y180_square": "square_y180_pulse",
                "y90_square": "square_y90_pulse",
                "-y90_square": "square_minus_y90_pulse",
            },
        },
        "qubit1_dup1": {
            "mixInputs": {
                "I": ('con1', 5, 5),
                "Q": ('con1', 5, 6),
                "lo_frequency": 16000000000,
                "mixer": "mixer_qubit1",
            },
            "digitalInputs": {
                "marker": {
                    "port": ('con1', 5, 1),
                    "delay": 40,
                    "buffer": 40,
                },
            },
            "intermediate_frequency": 0,
            "operations": {
                "const": "const_pulse",
                "saturation": "saturation_pulse",
                "x180_kaiser": "x180_kaiser_pulse_qubit1",
                "x90_kaiser": "x90_kaiser_pulse_qubit1",
                "-x90_kaiser": "minus_x90_kaiser_pulse_qubit1",
                "y180_kaiser": "y180_kaiser_pulse_qubit1",
                "y90_kaiser": "y90_kaiser_pulse_qubit1",
                "-y90_kaiser": "minus_y90_kaiser_pulse_qubit1",
                "x180_gauss": "x180_gaussian_pulse_qubit1",
                "x90_gauss": "x90_gaussian_pulse_qubit1",
                "-x90_gauss": "minus_x90_gaussian_pulse_qubit1",
                "y180_gauss": "y180_gaussian_pulse_qubit1",
                "y90_gauss": "y90_gaussian_pulse_qubit1",
                "-y90_gauss": "minus_y90_gaussian_pulse_qubit1",
                "x180_square": "square_x180_pulse_dup1",
                "x90_square": "square_x90_pulse_dup1",
                "-x90_square": "square_minus_x90_pulse_dup1",
                "y180_square": "square_y180_pulse_dup1",
                "y90_square": "square_y90_pulse_dup1",
                "-y90_square": "square_minus_y90_pulse_dup1",
            },
        },
        "qubit2_dup1": {
            "mixInputs": {
                "I": ('con1', 5, 5),
                "Q": ('con1', 5, 6),
                "lo_frequency": 16000000000,
                "mixer": "mixer_qubit2",
            },
            "digitalInputs": {
                "marker": {
                    "port": ('con1', 5, 1),
                    "delay": 40,
                    "buffer": 40,
                },
            },
            "intermediate_frequency": 0,
            "operations": {
                "const": "const_pulse",
                "saturation": "saturation_pulse",
                "x180_kaiser": "x180_kaiser_pulse_qubit2",
                "x90_kaiser": "x90_kaiser_pulse_qubit2",
                "-x90_kaiser": "minus_x90_kaiser_pulse_qubit2",
                "y180_kaiser": "y180_kaiser_pulse_qubit2",
                "y90_kaiser": "y90_kaiser_pulse_qubit2",
                "-y90_kaiser": "minus_y90_kaiser_pulse_qubit2",
                "x180_gauss": "x180_gaussian_pulse_qubit2",
                "x90_gauss": "x90_gaussian_pulse_qubit2",
                "-x90_gauss": "minus_x90_gaussian_pulse_qubit2",
                "y180_gauss": "y180_gaussian_pulse_qubit2",
                "y90_gauss": "y90_gaussian_pulse_qubit2",
                "-y90_gauss": "minus_y90_gaussian_pulse_qubit2",
                "x180_square": "square_x180_pulse_dup1",
                "x90_square": "square_x90_pulse_dup1",
                "-x90_square": "square_minus_x90_pulse_dup1",
                "y180_square": "square_y180_pulse_dup1",
                "y90_square": "square_y90_pulse_dup1",
                "-y90_square": "square_minus_y90_pulse_dup1",
            },
        },
        "qubit3_dup1": {
            "mixInputs": {
                "I": ('con1', 5, 5),
                "Q": ('con1', 5, 6),
                "lo_frequency": 16300000000,
                "mixer": "mixer_qubit3",
            },
            "digitalInputs": {
                "marker": {
                    "port": ('con1', 5, 3),
                    "delay": 40,
                    "buffer": 40,
                },
            },
            "intermediate_frequency": 0,
            "operations": {
                "const": "const_pulse",
                "saturation": "saturation_pulse",
                "x180_kaiser": "x180_kaiser_pulse_qubit3",
                "x90_kaiser": "x90_kaiser_pulse_qubit3",
                "-x90_kaiser": "minus_x90_kaiser_pulse_qubit3",
                "y180_kaiser": "y180_kaiser_pulse_qubit3",
                "y90_kaiser": "y90_kaiser_pulse_qubit3",
                "-y90_kaiser": "minus_y90_kaiser_pulse_qubit3",
                "x180_gauss": "x180_gaussian_pulse_qubit3",
                "x90_gauss": "x90_gaussian_pulse_qubit3",
                "-x90_gauss": "minus_x90_gaussian_pulse_qubit3",
                "y180_gauss": "y180_gaussian_pulse_qubit3",
                "y90_gauss": "y90_gaussian_pulse_qubit3",
                "-y90_gauss": "minus_y90_gaussian_pulse_qubit3",
                "x180_square": "square_x180_pulse_dup1",
                "x90_square": "square_x90_pulse_dup1",
                "-x90_square": "square_minus_x90_pulse_dup1",
                "y180_square": "square_y180_pulse_dup1",
                "y90_square": "square_y90_pulse_dup1",
                "-y90_square": "square_minus_y90_pulse_dup1",
            },
        },
        "qubit4_dup1": {
            "mixInputs": {
                "I": ('con1', 5, 5),
                "Q": ('con1', 5, 6),
                "lo_frequency": 16300000000,
                "mixer": "mixer_qubit4",
            },
            "digitalInputs": {
                "marker": {
                    "port": ('con1', 5, 3),
                    "delay": 40,
                    "buffer": 40,
                },
            },
            "intermediate_frequency": 50000000,
            "operations": {
                "const": "const_pulse",
                "saturation": "saturation_pulse",
                "x180_kaiser": "x180_kaiser_pulse_qubit4",
                "x90_kaiser": "x90_kaiser_pulse_qubit4",
                "-x90_kaiser": "minus_x90_kaiser_pulse_qubit4",
                "y180_kaiser": "y180_kaiser_pulse_qubit4",
                "y90_kaiser": "y90_kaiser_pulse_qubit4",
                "-y90_kaiser": "minus_y90_kaiser_pulse_qubit4",
                "x180_gauss": "x180_gaussian_pulse_qubit4",
                "x90_gauss": "x90_gaussian_pulse_qubit4",
                "-x90_gauss": "minus_x90_gaussian_pulse_qubit4",
                "y180_gauss": "y180_gaussian_pulse_qubit4",
                "y90_gauss": "y90_gaussian_pulse_qubit4",
                "-y90_gauss": "minus_y90_gaussian_pulse_qubit4",
                "x180_square": "square_x180_pulse_dup1",
                "x90_square": "square_x90_pulse_dup1",
                "-x90_square": "square_minus_x90_pulse_dup1",
                "y180_square": "square_y180_pulse_dup1",
                "y90_square": "square_y90_pulse_dup1",
                "-y90_square": "square_minus_y90_pulse_dup1",
            },
        },
        "qubit5_dup1": {
            "mixInputs": {
                "I": ('con1', 5, 5),
                "Q": ('con1', 5, 6),
                "lo_frequency": 16300000000,
                "mixer": "mixer_qubit5",
            },
            "digitalInputs": {
                "marker": {
                    "port": ('con1', 5, 5),
                    "delay": 40,
                    "buffer": 40,
                },
            },
            "intermediate_frequency": 0,
            "operations": {
                "const": "const_pulse",
                "saturation": "saturation_pulse",
                "x180_kaiser": "x180_kaiser_pulse_qubit5",
                "x90_kaiser": "x90_kaiser_pulse_qubit5",
                "-x90_kaiser": "minus_x90_kaiser_pulse_qubit5",
                "y180_kaiser": "y180_kaiser_pulse_qubit5",
                "y90_kaiser": "y90_kaiser_pulse_qubit5",
                "-y90_kaiser": "minus_y90_kaiser_pulse_qubit5",
                "x180_gauss": "x180_gaussian_pulse_qubit5",
                "x90_gauss": "x90_gaussian_pulse_qubit5",
                "-x90_gauss": "minus_x90_gaussian_pulse_qubit5",
                "y180_gauss": "y180_gaussian_pulse_qubit5",
                "y90_gauss": "y90_gaussian_pulse_qubit5",
                "-y90_gauss": "minus_y90_gaussian_pulse_qubit5",
                "x180_square": "square_x180_pulse_dup1",
                "x90_square": "square_x90_pulse_dup1",
                "-x90_square": "square_minus_x90_pulse_dup1",
                "y180_square": "square_y180_pulse_dup1",
                "y90_square": "square_y90_pulse_dup1",
                "-y90_square": "square_minus_y90_pulse_dup1",
            },
        },
        "qubit1_dup2": {
            "mixInputs": {
                "I": ('con1', 5, 5),
                "Q": ('con1', 5, 6),
                "lo_frequency": 16000000000,
                "mixer": "mixer_qubit1",
            },
            "digitalInputs": {
                "marker": {
                    "port": ('con1', 5, 1),
                    "delay": 40,
                    "buffer": 40,
                },
            },
            "intermediate_frequency": 0,
            "operations": {
                "const": "const_pulse",
                "saturation": "saturation_pulse",
                "x180_kaiser": "x180_kaiser_pulse_qubit1",
                "x90_kaiser": "x90_kaiser_pulse_qubit1",
                "-x90_kaiser": "minus_x90_kaiser_pulse_qubit1",
                "y180_kaiser": "y180_kaiser_pulse_qubit1",
                "y90_kaiser": "y90_kaiser_pulse_qubit1",
                "-y90_kaiser": "minus_y90_kaiser_pulse_qubit1",
                "x180_gauss": "x180_gaussian_pulse_qubit1",
                "x90_gauss": "x90_gaussian_pulse_qubit1",
                "-x90_gauss": "minus_x90_gaussian_pulse_qubit1",
                "y180_gauss": "y180_gaussian_pulse_qubit1",
                "y90_gauss": "y90_gaussian_pulse_qubit1",
                "-y90_gauss": "minus_y90_gaussian_pulse_qubit1",
                "x180_square": "square_x180_pulse_dup2",
                "x90_square": "square_x90_pulse_dup2",
                "-x90_square": "square_minus_x90_pulse_dup2",
                "y180_square": "square_y180_pulse_dup2",
                "y90_square": "square_y90_pulse_dup2",
                "-y90_square": "square_minus_y90_pulse_dup2",
            },
        },
        "qubit2_dup2": {
            "mixInputs": {
                "I": ('con1', 5, 5),
                "Q": ('con1', 5, 6),
                "lo_frequency": 16000000000,
                "mixer": "mixer_qubit2",
            },
            "digitalInputs": {
                "marker": {
                    "port": ('con1', 5, 1),
                    "delay": 40,
                    "buffer": 40,
                },
            },
            "intermediate_frequency": 0,
            "operations": {
                "const": "const_pulse",
                "saturation": "saturation_pulse",
                "x180_kaiser": "x180_kaiser_pulse_qubit2",
                "x90_kaiser": "x90_kaiser_pulse_qubit2",
                "-x90_kaiser": "minus_x90_kaiser_pulse_qubit2",
                "y180_kaiser": "y180_kaiser_pulse_qubit2",
                "y90_kaiser": "y90_kaiser_pulse_qubit2",
                "-y90_kaiser": "minus_y90_kaiser_pulse_qubit2",
                "x180_gauss": "x180_gaussian_pulse_qubit2",
                "x90_gauss": "x90_gaussian_pulse_qubit2",
                "-x90_gauss": "minus_x90_gaussian_pulse_qubit2",
                "y180_gauss": "y180_gaussian_pulse_qubit2",
                "y90_gauss": "y90_gaussian_pulse_qubit2",
                "-y90_gauss": "minus_y90_gaussian_pulse_qubit2",
                "x180_square": "square_x180_pulse_dup2",
                "x90_square": "square_x90_pulse_dup2",
                "-x90_square": "square_minus_x90_pulse_dup2",
                "y180_square": "square_y180_pulse_dup2",
                "y90_square": "square_y90_pulse_dup2",
                "-y90_square": "square_minus_y90_pulse_dup2",
            },
        },
        "qubit3_dup2": {
            "mixInputs": {
                "I": ('con1', 5, 5),
                "Q": ('con1', 5, 6),
                "lo_frequency": 16300000000,
                "mixer": "mixer_qubit3",
            },
            "digitalInputs": {
                "marker": {
                    "port": ('con1', 5, 3),
                    "delay": 40,
                    "buffer": 40,
                },
            },
            "intermediate_frequency": 0,
            "operations": {
                "const": "const_pulse",
                "saturation": "saturation_pulse",
                "x180_kaiser": "x180_kaiser_pulse_qubit3",
                "x90_kaiser": "x90_kaiser_pulse_qubit3",
                "-x90_kaiser": "minus_x90_kaiser_pulse_qubit3",
                "y180_kaiser": "y180_kaiser_pulse_qubit3",
                "y90_kaiser": "y90_kaiser_pulse_qubit3",
                "-y90_kaiser": "minus_y90_kaiser_pulse_qubit3",
                "x180_gauss": "x180_gaussian_pulse_qubit3",
                "x90_gauss": "x90_gaussian_pulse_qubit3",
                "-x90_gauss": "minus_x90_gaussian_pulse_qubit3",
                "y180_gauss": "y180_gaussian_pulse_qubit3",
                "y90_gauss": "y90_gaussian_pulse_qubit3",
                "-y90_gauss": "minus_y90_gaussian_pulse_qubit3",
                "x180_square": "square_x180_pulse_dup2",
                "x90_square": "square_x90_pulse_dup2",
                "-x90_square": "square_minus_x90_pulse_dup2",
                "y180_square": "square_y180_pulse_dup2",
                "y90_square": "square_y90_pulse_dup2",
                "-y90_square": "square_minus_y90_pulse_dup2",
            },
        },
        "qubit4_dup2": {
            "mixInputs": {
                "I": ('con1', 5, 5),
                "Q": ('con1', 5, 6),
                "lo_frequency": 16300000000,
                "mixer": "mixer_qubit4",
            },
            "digitalInputs": {
                "marker": {
                    "port": ('con1', 5, 3),
                    "delay": 40,
                    "buffer": 40,
                },
            },
            "intermediate_frequency": 50000000,
            "operations": {
                "const": "const_pulse",
                "saturation": "saturation_pulse",
                "x180_kaiser": "x180_kaiser_pulse_qubit4",
                "x90_kaiser": "x90_kaiser_pulse_qubit4",
                "-x90_kaiser": "minus_x90_kaiser_pulse_qubit4",
                "y180_kaiser": "y180_kaiser_pulse_qubit4",
                "y90_kaiser": "y90_kaiser_pulse_qubit4",
                "-y90_kaiser": "minus_y90_kaiser_pulse_qubit4",
                "x180_gauss": "x180_gaussian_pulse_qubit4",
                "x90_gauss": "x90_gaussian_pulse_qubit4",
                "-x90_gauss": "minus_x90_gaussian_pulse_qubit4",
                "y180_gauss": "y180_gaussian_pulse_qubit4",
                "y90_gauss": "y90_gaussian_pulse_qubit4",
                "-y90_gauss": "minus_y90_gaussian_pulse_qubit4",
                "x180_square": "square_x180_pulse_dup2",
                "x90_square": "square_x90_pulse_dup2",
                "-x90_square": "square_minus_x90_pulse_dup2",
                "y180_square": "square_y180_pulse_dup2",
                "y90_square": "square_y90_pulse_dup2",
                "-y90_square": "square_minus_y90_pulse_dup2",
            },
        },
        "qubit5_dup2": {
            "mixInputs": {
                "I": ('con1', 5, 5),
                "Q": ('con1', 5, 6),
                "lo_frequency": 16300000000,
                "mixer": "mixer_qubit5",
            },
            "digitalInputs": {
                "marker": {
                    "port": ('con1', 5, 5),
                    "delay": 40,
                    "buffer": 40,
                },
            },
            "intermediate_frequency": 0,
            "operations": {
                "const": "const_pulse",
                "saturation": "saturation_pulse",
                "x180_kaiser": "x180_kaiser_pulse_qubit5",
                "x90_kaiser": "x90_kaiser_pulse_qubit5",
                "-x90_kaiser": "minus_x90_kaiser_pulse_qubit5",
                "y180_kaiser": "y180_kaiser_pulse_qubit5",
                "y90_kaiser": "y90_kaiser_pulse_qubit5",
                "-y90_kaiser": "minus_y90_kaiser_pulse_qubit5",
                "x180_gauss": "x180_gaussian_pulse_qubit5",
                "x90_gauss": "x90_gaussian_pulse_qubit5",
                "-x90_gauss": "minus_x90_gaussian_pulse_qubit5",
                "y180_gauss": "y180_gaussian_pulse_qubit5",
                "y90_gauss": "y90_gaussian_pulse_qubit5",
                "-y90_gauss": "minus_y90_gaussian_pulse_qubit5",
                "x180_square": "square_x180_pulse_dup2",
                "x90_square": "square_x90_pulse_dup2",
                "-x90_square": "square_minus_x90_pulse_dup2",
                "y180_square": "square_y180_pulse_dup2",
                "y90_square": "square_y90_pulse_dup2",
                "-y90_square": "square_minus_y90_pulse_dup2",
            },
        },
        "qp_control_c3t2": {
            "mixInputs": {
                "I": ('con1', 5, 5),
                "Q": ('con1', 5, 6),
                "lo_frequency": 16300000000,
                "mixer": "mixer_qp_control_c3t2",
            },
            "digitalInputs": {
                "marker": {
                    "port": ('con1', 5, 3),
                    "delay": 40,
                    "buffer": 0,
                },
            },
            "intermediate_frequency": 0,
            "operations": {
                "const": "const_pulse",
                "x180_kaiser": "x180_kaiser_pulse_qp_control_c3t2",
                "x90_kaiser": "x90_kaiser_pulse_qp_control_c3t2",
                "-x90_kaiser": "minus_x90_kaiser_pulse_qp_control_c3t2",
                "y180_kaiser": "y180_kaiser_pulse_qp_control_c3t2",
                "y90_kaiser": "y90_kaiser_pulse_qp_control_c3t2",
                "-y90_kaiser": "minus_y90_kaiser_pulse_qp_control_c3t2",
                "x180_gauss": "x180_gaussian_pulse_qp_control_c3t2",
                "x90_gauss": "x90_gaussian_pulse_qp_control_c3t2",
                "-x90_gauss": "minus_x90_gaussian_pulse_qp_control_c3t2",
                "y180_gauss": "y180_gaussian_pulse_qp_control_c3t2",
                "y90_gauss": "y90_gaussian_pulse_qp_control_c3t2",
                "-y90_gauss": "minus_y90_gaussian_pulse_qp_control_c3t2",
                "x180_square": "square_x180_pulse",
                "x90_square": "square_x90_pulse",
                "-x90_square": "square_minus_x90_pulse",
                "y180_square": "square_y180_pulse",
                "y90_square": "square_y90_pulse",
                "-y90_square": "square_minus_y90_pulse",
            },
        },
        "qubit1_trigger": {
            "digitalInputs": {
                "trigger": {
                    "port": ('con1', 5, 1),
                    "delay": 0,
                    "buffer": 0,
                },
            },
            "operations": {
                "trigger": "trigger_pulse",
            },
        },
        "qubit2_trigger": {
            "digitalInputs": {
                "trigger": {
                    "port": ('con1', 5, 1),
                    "delay": 0,
                    "buffer": 0,
                },
            },
            "operations": {
                "trigger": "trigger_pulse",
            },
        },
        "qubit3_trigger": {
            "digitalInputs": {
                "trigger": {
                    "port": ('con1', 5, 3),
                    "delay": 0,
                    "buffer": 0,
                },
            },
            "operations": {
                "trigger": "trigger_pulse",
            },
        },
        "qubit4_trigger": {
            "digitalInputs": {
                "trigger": {
                    "port": ('con1', 5, 3),
                    "delay": 0,
                    "buffer": 0,
                },
            },
            "operations": {
                "trigger": "trigger_pulse",
            },
        },
        "qubit5_trigger": {
            "digitalInputs": {
                "trigger": {
                    "port": ('con1', 5, 5),
                    "delay": 0,
                    "buffer": 0,
                },
            },
            "operations": {
                "trigger": "trigger_pulse",
            },
        },
        "tank_circuit1": {
            "singleInput": {
                "port": ('con1', 5, 8),
            },
            "intermediate_frequency": 50000000,
            "operations": {
                "readout": "reflectometry_readout_pulse_tank_circuit1",
            },
            "outputs": {
                "out1": ('con1', 5, 2),
            },
            "time_of_flight": 24,
            "smearing": 0,
        },
        "tank_circuit2": {
            "singleInput": {
                "port": ('con1', 5, 8),
            },
            "intermediate_frequency": 100000000,
            "operations": {
                "readout": "reflectometry_readout_pulse_tank_circuit2",
            },
            "outputs": {
                "out1": ('con1', 5, 2),
            },
            "time_of_flight": 24,
            "smearing": 0,
        },
    },
    "pulses": {
        "P1_step_pulse": {
            "operation": "control",
            "length": 1000,
            "waveforms": {
                "single": "P1_step_wf",
            },
        },
        "P2_step_pulse": {
            "operation": "control",
            "length": 1000,
            "waveforms": {
                "single": "P2_step_wf",
            },
        },
        "P3_step_pulse": {
            "operation": "control",
            "length": 1000,
            "waveforms": {
                "single": "P3_step_wf",
            },
        },
        "P4_step_pulse": {
            "operation": "control",
            "length": 1000,
            "waveforms": {
                "single": "P4_step_wf",
            },
        },
        "P5_step_pulse": {
            "operation": "control",
            "length": 1000,
            "waveforms": {
                "single": "P5_step_wf",
            },
        },
        "B1_step_pulse": {
            "operation": "control",
            "length": 1000,
            "waveforms": {
                "single": "B1_step_wf",
            },
        },
        "B2_step_pulse": {
            "operation": "control",
            "length": 1000,
            "waveforms": {
                "single": "B2_step_wf",
            },
        },
        "B3_step_pulse": {
            "operation": "control",
            "length": 1000,
            "waveforms": {
                "single": "B3_step_wf",
            },
        },
        "B4_step_pulse": {
            "operation": "control",
            "length": 1000,
            "waveforms": {
                "single": "B4_step_wf",
            },
        },
        "Psd1_step_pulse": {
            "operation": "control",
            "length": 1000,
            "waveforms": {
                "single": "Psd1_step_wf",
            },
        },
        "Psd2_step_pulse": {
            "operation": "control",
            "length": 1000,
            "waveforms": {
                "single": "Psd2_step_wf",
            },
        },
        "x180_gaussian_pulse_qubit1": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "x180_gaussian_I_wf_qubit1",
                "Q": "x180_gaussian_Q_wf_qubit1",
            },
        },
        "x180_gaussian_pulse_qubit2": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "x180_gaussian_I_wf_qubit2",
                "Q": "x180_gaussian_Q_wf_qubit2",
            },
        },
        "x180_gaussian_pulse_qubit3": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "x180_gaussian_I_wf_qubit3",
                "Q": "x180_gaussian_Q_wf_qubit3",
            },
        },
        "x180_gaussian_pulse_qubit4": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "x180_gaussian_I_wf_qubit4",
                "Q": "x180_gaussian_Q_wf_qubit4",
            },
        },
        "x180_gaussian_pulse_qubit5": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "x180_gaussian_I_wf_qubit5",
                "Q": "x180_gaussian_Q_wf_qubit5",
            },
        },
        "x90_gaussian_pulse_qubit1": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "x90_gaussian_I_wf_qubit1",
                "Q": "x90_gaussian_Q_wf_qubit1",
            },
        },
        "x90_gaussian_pulse_qubit2": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "x90_gaussian_I_wf_qubit2",
                "Q": "x90_gaussian_Q_wf_qubit2",
            },
        },
        "x90_gaussian_pulse_qubit3": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "x90_gaussian_I_wf_qubit3",
                "Q": "x90_gaussian_Q_wf_qubit3",
            },
        },
        "x90_gaussian_pulse_qubit4": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "x90_gaussian_I_wf_qubit4",
                "Q": "x90_gaussian_Q_wf_qubit4",
            },
        },
        "x90_gaussian_pulse_qubit5": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "x90_gaussian_I_wf_qubit5",
                "Q": "x90_gaussian_Q_wf_qubit5",
            },
        },
        "minus_x90_gaussian_pulse_qubit1": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "minus_x90_gaussian_I_wf_qubit1",
                "Q": "minus_x90_gaussian_Q_wf_qubit1",
            },
        },
        "minus_x90_gaussian_pulse_qubit2": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "minus_x90_gaussian_I_wf_qubit2",
                "Q": "minus_x90_gaussian_Q_wf_qubit2",
            },
        },
        "minus_x90_gaussian_pulse_qubit3": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "minus_x90_gaussian_I_wf_qubit3",
                "Q": "minus_x90_gaussian_Q_wf_qubit3",
            },
        },
        "minus_x90_gaussian_pulse_qubit4": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "minus_x90_gaussian_I_wf_qubit4",
                "Q": "minus_x90_gaussian_Q_wf_qubit4",
            },
        },
        "minus_x90_gaussian_pulse_qubit5": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "minus_x90_gaussian_I_wf_qubit5",
                "Q": "minus_x90_gaussian_Q_wf_qubit5",
            },
        },
        "y180_gaussian_pulse_qubit1": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "y180_gaussian_I_wf_qubit1",
                "Q": "y180_gaussian_Q_wf_qubit1",
            },
        },
        "y180_gaussian_pulse_qubit2": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "y180_gaussian_I_wf_qubit2",
                "Q": "y180_gaussian_Q_wf_qubit2",
            },
        },
        "y180_gaussian_pulse_qubit3": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "y180_gaussian_I_wf_qubit3",
                "Q": "y180_gaussian_Q_wf_qubit3",
            },
        },
        "y180_gaussian_pulse_qubit4": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "y180_gaussian_I_wf_qubit4",
                "Q": "y180_gaussian_Q_wf_qubit4",
            },
        },
        "y180_gaussian_pulse_qubit5": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "y180_gaussian_I_wf_qubit5",
                "Q": "y180_gaussian_Q_wf_qubit5",
            },
        },
        "y90_gaussian_pulse_qubit1": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "y90_gaussian_I_wf_qubit1",
                "Q": "y90_gaussian_Q_wf_qubit1",
            },
        },
        "y90_gaussian_pulse_qubit2": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "y90_gaussian_I_wf_qubit2",
                "Q": "y90_gaussian_Q_wf_qubit2",
            },
        },
        "y90_gaussian_pulse_qubit3": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "y90_gaussian_I_wf_qubit3",
                "Q": "y90_gaussian_Q_wf_qubit3",
            },
        },
        "y90_gaussian_pulse_qubit4": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "y90_gaussian_I_wf_qubit4",
                "Q": "y90_gaussian_Q_wf_qubit4",
            },
        },
        "y90_gaussian_pulse_qubit5": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "y90_gaussian_I_wf_qubit5",
                "Q": "y90_gaussian_Q_wf_qubit5",
            },
        },
        "minus_y90_gaussian_pulse_qubit1": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "minus_y90_gaussian_I_wf_qubit1",
                "Q": "minus_y90_gaussian_Q_wf_qubit1",
            },
        },
        "minus_y90_gaussian_pulse_qubit2": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "minus_y90_gaussian_I_wf_qubit2",
                "Q": "minus_y90_gaussian_Q_wf_qubit2",
            },
        },
        "minus_y90_gaussian_pulse_qubit3": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "minus_y90_gaussian_I_wf_qubit3",
                "Q": "minus_y90_gaussian_Q_wf_qubit3",
            },
        },
        "minus_y90_gaussian_pulse_qubit4": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "minus_y90_gaussian_I_wf_qubit4",
                "Q": "minus_y90_gaussian_Q_wf_qubit4",
            },
        },
        "minus_y90_gaussian_pulse_qubit5": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "minus_y90_gaussian_I_wf_qubit5",
                "Q": "minus_y90_gaussian_Q_wf_qubit5",
            },
        },
        "x180_kaiser_pulse_qubit1": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "x180_kaiser_I_wf_qubit1",
                "Q": "x180_kaiser_Q_wf_qubit1",
            },
        },
        "x180_kaiser_pulse_qubit2": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "x180_kaiser_I_wf_qubit2",
                "Q": "x180_kaiser_Q_wf_qubit2",
            },
        },
        "x180_kaiser_pulse_qubit3": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "x180_kaiser_I_wf_qubit3",
                "Q": "x180_kaiser_Q_wf_qubit3",
            },
        },
        "x180_kaiser_pulse_qubit4": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "x180_kaiser_I_wf_qubit4",
                "Q": "x180_kaiser_Q_wf_qubit4",
            },
        },
        "x180_kaiser_pulse_qubit5": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "x180_kaiser_I_wf_qubit5",
                "Q": "x180_kaiser_Q_wf_qubit5",
            },
        },
        "x90_kaiser_pulse_qubit1": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "x90_kaiser_I_wf_qubit1",
                "Q": "x90_kaiser_Q_wf_qubit1",
            },
        },
        "x90_kaiser_pulse_qubit2": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "x90_kaiser_I_wf_qubit2",
                "Q": "x90_kaiser_Q_wf_qubit2",
            },
        },
        "x90_kaiser_pulse_qubit3": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "x90_kaiser_I_wf_qubit3",
                "Q": "x90_kaiser_Q_wf_qubit3",
            },
        },
        "x90_kaiser_pulse_qubit4": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "x90_kaiser_I_wf_qubit4",
                "Q": "x90_kaiser_Q_wf_qubit4",
            },
        },
        "x90_kaiser_pulse_qubit5": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "x90_kaiser_I_wf_qubit5",
                "Q": "x90_kaiser_Q_wf_qubit5",
            },
        },
        "minus_x90_kaiser_pulse_qubit1": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "minus_x90_kaiser_I_wf_qubit1",
                "Q": "minus_x90_kaiser_Q_wf_qubit1",
            },
        },
        "minus_x90_kaiser_pulse_qubit2": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "minus_x90_kaiser_I_wf_qubit2",
                "Q": "minus_x90_kaiser_Q_wf_qubit2",
            },
        },
        "minus_x90_kaiser_pulse_qubit3": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "minus_x90_kaiser_I_wf_qubit3",
                "Q": "minus_x90_kaiser_Q_wf_qubit3",
            },
        },
        "minus_x90_kaiser_pulse_qubit4": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "minus_x90_kaiser_I_wf_qubit4",
                "Q": "minus_x90_kaiser_Q_wf_qubit4",
            },
        },
        "minus_x90_kaiser_pulse_qubit5": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "minus_x90_kaiser_I_wf_qubit5",
                "Q": "minus_x90_kaiser_Q_wf_qubit5",
            },
        },
        "y180_kaiser_pulse_qubit1": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "y180_kaiser_I_wf_qubit1",
                "Q": "y180_kaiser_Q_wf_qubit1",
            },
        },
        "y180_kaiser_pulse_qubit2": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "y180_kaiser_I_wf_qubit2",
                "Q": "y180_kaiser_Q_wf_qubit2",
            },
        },
        "y180_kaiser_pulse_qubit3": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "y180_kaiser_I_wf_qubit3",
                "Q": "y180_kaiser_Q_wf_qubit3",
            },
        },
        "y180_kaiser_pulse_qubit4": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "y180_kaiser_I_wf_qubit4",
                "Q": "y180_kaiser_Q_wf_qubit4",
            },
        },
        "y180_kaiser_pulse_qubit5": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "y180_kaiser_I_wf_qubit5",
                "Q": "y180_kaiser_Q_wf_qubit5",
            },
        },
        "y90_kaiser_pulse_qubit1": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "y90_kaiser_I_wf_qubit1",
                "Q": "y90_kaiser_Q_wf_qubit1",
            },
        },
        "y90_kaiser_pulse_qubit2": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "y90_kaiser_I_wf_qubit2",
                "Q": "y90_kaiser_Q_wf_qubit2",
            },
        },
        "y90_kaiser_pulse_qubit3": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "y90_kaiser_I_wf_qubit3",
                "Q": "y90_kaiser_Q_wf_qubit3",
            },
        },
        "y90_kaiser_pulse_qubit4": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "y90_kaiser_I_wf_qubit4",
                "Q": "y90_kaiser_Q_wf_qubit4",
            },
        },
        "y90_kaiser_pulse_qubit5": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "y90_kaiser_I_wf_qubit5",
                "Q": "y90_kaiser_Q_wf_qubit5",
            },
        },
        "minus_y90_kaiser_pulse_qubit1": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "minus_y90_kaiser_I_wf_qubit1",
                "Q": "minus_y90_kaiser_Q_wf_qubit1",
            },
        },
        "minus_y90_kaiser_pulse_qubit2": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "minus_y90_kaiser_I_wf_qubit2",
                "Q": "minus_y90_kaiser_Q_wf_qubit2",
            },
        },
        "minus_y90_kaiser_pulse_qubit3": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "minus_y90_kaiser_I_wf_qubit3",
                "Q": "minus_y90_kaiser_Q_wf_qubit3",
            },
        },
        "minus_y90_kaiser_pulse_qubit4": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "minus_y90_kaiser_I_wf_qubit4",
                "Q": "minus_y90_kaiser_Q_wf_qubit4",
            },
        },
        "minus_y90_kaiser_pulse_qubit5": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "minus_y90_kaiser_I_wf_qubit5",
                "Q": "minus_y90_kaiser_Q_wf_qubit5",
            },
        },
        "x180_gaussian_pulse_qp_control_c3t2": {
            "operation": "control",
            "length": 100,
            "waveforms": {
                "I": "x180_gaussian_I_wf_qp_control_c3t2",
                "Q": "x180_gaussian_Q_wf_qp_control_c3t2",
            },
        },
        "x90_gaussian_pulse_qp_control_c3t2": {
            "operation": "control",
            "length": 100,
            "waveforms": {
                "I": "x90_gaussian_I_wf_qp_control_c3t2",
                "Q": "x90_gaussian_Q_wf_qp_control_c3t2",
            },
        },
        "minus_x90_gaussian_pulse_qp_control_c3t2": {
            "operation": "control",
            "length": 100,
            "waveforms": {
                "I": "minus_x90_gaussian_I_wf_qp_control_c3t2",
                "Q": "minus_x90_gaussian_Q_wf_qp_control_c3t2",
            },
        },
        "y180_gaussian_pulse_qp_control_c3t2": {
            "operation": "control",
            "length": 100,
            "waveforms": {
                "I": "y180_gaussian_I_wf_qp_control_c3t2",
                "Q": "y180_gaussian_Q_wf_qp_control_c3t2",
            },
        },
        "y90_gaussian_pulse_qp_control_c3t2": {
            "operation": "control",
            "length": 100,
            "waveforms": {
                "I": "y90_gaussian_I_wf_qp_control_c3t2",
                "Q": "y90_gaussian_Q_wf_qp_control_c3t2",
            },
        },
        "minus_y90_gaussian_pulse_qp_control_c3t2": {
            "operation": "control",
            "length": 100,
            "waveforms": {
                "I": "minus_y90_gaussian_I_wf_qp_control_c3t2",
                "Q": "minus_y90_gaussian_Q_wf_qp_control_c3t2",
            },
        },
        "x180_kaiser_pulse_qp_control_c3t2": {
            "operation": "control",
            "length": 100,
            "waveforms": {
                "I": "x180_kaiser_I_wf_qp_control_c3t2",
                "Q": "x180_kaiser_Q_wf_qp_control_c3t2",
            },
        },
        "x90_kaiser_pulse_qp_control_c3t2": {
            "operation": "control",
            "length": 100,
            "waveforms": {
                "I": "x90_kaiser_I_wf_qp_control_c3t2",
                "Q": "x90_kaiser_Q_wf_qp_control_c3t2",
            },
        },
        "minus_x90_kaiser_pulse_qp_control_c3t2": {
            "operation": "control",
            "length": 100,
            "waveforms": {
                "I": "minus_x90_kaiser_I_wf_qp_control_c3t2",
                "Q": "minus_x90_kaiser_Q_wf_qp_control_c3t2",
            },
        },
        "y180_kaiser_pulse_qp_control_c3t2": {
            "operation": "control",
            "length": 100,
            "waveforms": {
                "I": "y180_kaiser_I_wf_qp_control_c3t2",
                "Q": "y180_kaiser_Q_wf_qp_control_c3t2",
            },
        },
        "y90_kaiser_pulse_qp_control_c3t2": {
            "operation": "control",
            "length": 100,
            "waveforms": {
                "I": "y90_kaiser_I_wf_qp_control_c3t2",
                "Q": "y90_kaiser_Q_wf_qp_control_c3t2",
            },
        },
        "minus_y90_kaiser_pulse_qp_control_c3t2": {
            "operation": "control",
            "length": 100,
            "waveforms": {
                "I": "minus_y90_kaiser_I_wf_qp_control_c3t2",
                "Q": "minus_y90_kaiser_Q_wf_qp_control_c3t2",
            },
        },
        "reflectometry_readout_pulse_tank_circuit1": {
            "operation": "measurement",
            "length": 400,
            "waveforms": {
                "single": "reflectometry_readout_wf_tank_circuit1",
            },
            "integration_weights": {
                "cos": "cosine_weights_tank_circuit1",
                "sin": "sine_weights_tank_circuit1",
            },
            "digital_marker": "ON",
        },
        "reflectometry_readout_pulse_tank_circuit2": {
            "operation": "measurement",
            "length": 400,
            "waveforms": {
                "single": "reflectometry_readout_wf_tank_circuit2",
            },
            "integration_weights": {
                "cos": "cosine_weights_tank_circuit2",
                "sin": "sine_weights_tank_circuit2",
            },
            "digital_marker": "ON",
        },
        "const_pulse": {
            "operation": "control",
            "length": 100,
            "waveforms": {
                "I": "const_wf",
                "Q": "zero_wf",
            },
        },
        "saturation_pulse": {
            "operation": "control",
            "length": 10000,
            "waveforms": {
                "I": "saturation_wf",
                "Q": "zero_wf",
            },
        },
        "square_x180_pulse": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "square_x180_I_wf",
                "Q": "zero_wf",
            },
        },
        "square_x90_pulse": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "square_x90_I_wf",
                "Q": "zero_wf",
            },
        },
        "square_minus_x90_pulse": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "square_minus_x90_I_wf",
                "Q": "zero_wf",
            },
        },
        "square_y180_pulse": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "square_y180_I_wf",
                "Q": "zero_wf",
            },
        },
        "square_y90_pulse": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "square_y90_I_wf",
                "Q": "zero_wf",
            },
        },
        "square_minus_y90_pulse": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "square_minus_y90_I_wf",
                "Q": "zero_wf",
            },
        },
        "square_x180_pulse_dup1": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "square_x180_I_wf_dup1",
                "Q": "zero_wf",
            },
        },
        "square_x90_pulse_dup1": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "square_x90_I_wf_dup1",
                "Q": "zero_wf",
            },
        },
        "square_minus_x90_pulse_dup1": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "square_minus_x90_I_wf_dup1",
                "Q": "zero_wf",
            },
        },
        "square_y180_pulse_dup1": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "square_y180_I_wf_dup1",
                "Q": "zero_wf",
            },
        },
        "square_y90_pulse_dup1": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "square_y90_I_wf_dup1",
                "Q": "zero_wf",
            },
        },
        "square_minus_y90_pulse_dup1": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "square_minus_y90_I_wf_dup1",
                "Q": "zero_wf",
            },
        },
        "square_x180_pulse_dup2": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "square_x180_I_wf_dup2",
                "Q": "zero_wf",
            },
        },
        "square_x90_pulse_dup2": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "square_x90_I_wf_dup2",
                "Q": "zero_wf",
            },
        },
        "square_minus_x90_pulse_dup2": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "square_minus_x90_I_wf_dup2",
                "Q": "zero_wf",
            },
        },
        "square_y180_pulse_dup2": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "square_y180_I_wf_dup2",
                "Q": "zero_wf",
            },
        },
        "square_y90_pulse_dup2": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "square_y90_I_wf_dup2",
                "Q": "zero_wf",
            },
        },
        "square_minus_y90_pulse_dup2": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "I": "square_minus_y90_I_wf_dup2",
                "Q": "zero_wf",
            },
        },
        "trigger_pulse": {
            "operation": "control",
            "length": 1000,
            "digital_marker": "ON",
        },
        "step_pulse": {
            "operation": "control",
            "length": 16,
            "waveforms": {
                "single": "step_wf",
            },
        },
        "P1_sticky_step%_pulse": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "single": "P1_sticky_step%_wf",
            },
        },
        "P2_sticky_step%_pulse": {
            "operation": "control",
            "length": 52,
            "waveforms": {
                "single": "P2_sticky_step%_wf",
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
        "saturation_wf": {
            "type": "constant",
            "sample": 0.1,
        },
        "square_x180_I_wf": {
            "type": "constant",
            "sample": 0.2,
        },
        "square_x90_I_wf": {
            "type": "constant",
            "sample": 0.1,
        },
        "square_minus_x90_I_wf": {
            "type": "constant",
            "sample": -0.1,
        },
        "square_y180_I_wf": {
            "type": "constant",
            "sample": 0.15,
        },
        "square_y90_I_wf": {
            "type": "constant",
            "sample": 0.075,
        },
        "square_minus_y90_I_wf": {
            "type": "constant",
            "sample": -0.075,
        },
        "square_x180_I_wf_dup1": {
            "type": "constant",
            "sample": 0.13333333333333333,
        },
        "square_x90_I_wf_dup1": {
            "type": "constant",
            "sample": 0.06666666666666667,
        },
        "square_minus_x90_I_wf_dup1": {
            "type": "constant",
            "sample": -0.06666666666666667,
        },
        "square_y180_I_wf_dup1": {
            "type": "constant",
            "sample": 0.09999999999999999,
        },
        "square_y90_I_wf_dup1": {
            "type": "constant",
            "sample": 0.049999999999999996,
        },
        "square_minus_y90_I_wf_dup1": {
            "type": "constant",
            "sample": -0.049999999999999996,
        },
        "square_x180_I_wf_dup2": {
            "type": "constant",
            "sample": 0.06666666666666667,
        },
        "square_x90_I_wf_dup2": {
            "type": "constant",
            "sample": 0.03333333333333333,
        },
        "square_minus_x90_I_wf_dup2": {
            "type": "constant",
            "sample": -0.03333333333333333,
        },
        "square_y180_I_wf_dup2": {
            "type": "constant",
            "sample": 0.049999999999999996,
        },
        "square_y90_I_wf_dup2": {
            "type": "constant",
            "sample": 0.024999999999999998,
        },
        "square_minus_y90_I_wf_dup2": {
            "type": "constant",
            "sample": -0.024999999999999998,
        },
        "reflectometry_readout_wf_tank_circuit1": {
            "type": "constant",
            "sample": 0.1,
        },
        "reflectometry_readout_wf_tank_circuit2": {
            "type": "constant",
            "sample": 0.1,
        },
        "P1_step_wf": {
            "type": "constant",
            "sample": 0.25,
        },
        "P2_step_wf": {
            "type": "constant",
            "sample": 0.25,
        },
        "P3_step_wf": {
            "type": "constant",
            "sample": 0.25,
        },
        "P4_step_wf": {
            "type": "constant",
            "sample": 0.25,
        },
        "P5_step_wf": {
            "type": "constant",
            "sample": 0.25,
        },
        "B1_step_wf": {
            "type": "constant",
            "sample": 0.25,
        },
        "B2_step_wf": {
            "type": "constant",
            "sample": 0.25,
        },
        "B3_step_wf": {
            "type": "constant",
            "sample": 0.25,
        },
        "B4_step_wf": {
            "type": "constant",
            "sample": 0.25,
        },
        "Psd1_step_wf": {
            "type": "constant",
            "sample": 0.25,
        },
        "Psd2_step_wf": {
            "type": "constant",
            "sample": 0.25,
        },
        "x180_gaussian_I_wf_qubit1": {
            "type": "arbitrary",
            "samples": [0.0, 0.0013487829662939248, 0.0029834635305878076, 0.004941237909839778, 0.0072578579934551015, 0.00996569018380684, 0.013091497820654437, 0.016654029341753772, 0.0206615278002724, 0.025109308094492595, 0.02997757267874069, 0.035229650968230525, 0.04081084883592647, 0.046648080053314674, 0.05265042002594503, 0.058710674095939365, 0.06470799020836852, 0.07051147285766579, 0.07598467752555374, 0.08099078901901928, 0.08539822044608465, 0.08908631899519925, 0.09195083610639947, 0.09390881711988835] + [0.09490259075122315] * 2 + [0.09390881711988835, 0.09195083610639947, 0.08908631899519925, 0.08539822044608465, 0.08099078901901928, 0.07598467752555374, 0.07051147285766579, 0.06470799020836852, 0.058710674095939365, 0.05265042002594503, 0.046648080053314674, 0.04081084883592647, 0.035229650968230525, 0.02997757267874069, 0.025109308094492595, 0.0206615278002724, 0.016654029341753772, 0.013091497820654437, 0.00996569018380684, 0.0072578579934551015, 0.004941237909839778, 0.0029834635305878076, 0.0013487829662939248] + [0.0] * 3,
        },
        "x180_gaussian_I_wf_qubit2": {
            "type": "arbitrary",
            "samples": [0.0, 0.0013487829662939248, 0.0029834635305878076, 0.004941237909839778, 0.0072578579934551015, 0.00996569018380684, 0.013091497820654437, 0.016654029341753772, 0.0206615278002724, 0.025109308094492595, 0.02997757267874069, 0.035229650968230525, 0.04081084883592647, 0.046648080053314674, 0.05265042002594503, 0.058710674095939365, 0.06470799020836852, 0.07051147285766579, 0.07598467752555374, 0.08099078901901928, 0.08539822044608465, 0.08908631899519925, 0.09195083610639947, 0.09390881711988835] + [0.09490259075122315] * 2 + [0.09390881711988835, 0.09195083610639947, 0.08908631899519925, 0.08539822044608465, 0.08099078901901928, 0.07598467752555374, 0.07051147285766579, 0.06470799020836852, 0.058710674095939365, 0.05265042002594503, 0.046648080053314674, 0.04081084883592647, 0.035229650968230525, 0.02997757267874069, 0.025109308094492595, 0.0206615278002724, 0.016654029341753772, 0.013091497820654437, 0.00996569018380684, 0.0072578579934551015, 0.004941237909839778, 0.0029834635305878076, 0.0013487829662939248] + [0.0] * 3,
        },
        "x180_gaussian_I_wf_qubit3": {
            "type": "arbitrary",
            "samples": [0.0, 0.0013487829662939248, 0.0029834635305878076, 0.004941237909839778, 0.0072578579934551015, 0.00996569018380684, 0.013091497820654437, 0.016654029341753772, 0.0206615278002724, 0.025109308094492595, 0.02997757267874069, 0.035229650968230525, 0.04081084883592647, 0.046648080053314674, 0.05265042002594503, 0.058710674095939365, 0.06470799020836852, 0.07051147285766579, 0.07598467752555374, 0.08099078901901928, 0.08539822044608465, 0.08908631899519925, 0.09195083610639947, 0.09390881711988835] + [0.09490259075122315] * 2 + [0.09390881711988835, 0.09195083610639947, 0.08908631899519925, 0.08539822044608465, 0.08099078901901928, 0.07598467752555374, 0.07051147285766579, 0.06470799020836852, 0.058710674095939365, 0.05265042002594503, 0.046648080053314674, 0.04081084883592647, 0.035229650968230525, 0.02997757267874069, 0.025109308094492595, 0.0206615278002724, 0.016654029341753772, 0.013091497820654437, 0.00996569018380684, 0.0072578579934551015, 0.004941237909839778, 0.0029834635305878076, 0.0013487829662939248] + [0.0] * 3,
        },
        "x180_gaussian_I_wf_qubit4": {
            "type": "arbitrary",
            "samples": [0.0, 0.0013487829662939248, 0.0029834635305878076, 0.004941237909839778, 0.0072578579934551015, 0.00996569018380684, 0.013091497820654437, 0.016654029341753772, 0.0206615278002724, 0.025109308094492595, 0.02997757267874069, 0.035229650968230525, 0.04081084883592647, 0.046648080053314674, 0.05265042002594503, 0.058710674095939365, 0.06470799020836852, 0.07051147285766579, 0.07598467752555374, 0.08099078901901928, 0.08539822044608465, 0.08908631899519925, 0.09195083610639947, 0.09390881711988835] + [0.09490259075122315] * 2 + [0.09390881711988835, 0.09195083610639947, 0.08908631899519925, 0.08539822044608465, 0.08099078901901928, 0.07598467752555374, 0.07051147285766579, 0.06470799020836852, 0.058710674095939365, 0.05265042002594503, 0.046648080053314674, 0.04081084883592647, 0.035229650968230525, 0.02997757267874069, 0.025109308094492595, 0.0206615278002724, 0.016654029341753772, 0.013091497820654437, 0.00996569018380684, 0.0072578579934551015, 0.004941237909839778, 0.0029834635305878076, 0.0013487829662939248] + [0.0] * 3,
        },
        "x180_gaussian_I_wf_qubit5": {
            "type": "arbitrary",
            "samples": [0.0, 0.0013487829662939248, 0.0029834635305878076, 0.004941237909839778, 0.0072578579934551015, 0.00996569018380684, 0.013091497820654437, 0.016654029341753772, 0.0206615278002724, 0.025109308094492595, 0.02997757267874069, 0.035229650968230525, 0.04081084883592647, 0.046648080053314674, 0.05265042002594503, 0.058710674095939365, 0.06470799020836852, 0.07051147285766579, 0.07598467752555374, 0.08099078901901928, 0.08539822044608465, 0.08908631899519925, 0.09195083610639947, 0.09390881711988835] + [0.09490259075122315] * 2 + [0.09390881711988835, 0.09195083610639947, 0.08908631899519925, 0.08539822044608465, 0.08099078901901928, 0.07598467752555374, 0.07051147285766579, 0.06470799020836852, 0.058710674095939365, 0.05265042002594503, 0.046648080053314674, 0.04081084883592647, 0.035229650968230525, 0.02997757267874069, 0.025109308094492595, 0.0206615278002724, 0.016654029341753772, 0.013091497820654437, 0.00996569018380684, 0.0072578579934551015, 0.004941237909839778, 0.0029834635305878076, 0.0013487829662939248] + [0.0] * 3,
        },
        "x180_gaussian_Q_wf_qubit1": {
            "type": "arbitrary",
            "samples": [0.0] * 52,
        },
        "x180_gaussian_Q_wf_qubit2": {
            "type": "arbitrary",
            "samples": [0.0] * 52,
        },
        "x180_gaussian_Q_wf_qubit3": {
            "type": "arbitrary",
            "samples": [0.0] * 52,
        },
        "x180_gaussian_Q_wf_qubit4": {
            "type": "arbitrary",
            "samples": [0.0] * 52,
        },
        "x180_gaussian_Q_wf_qubit5": {
            "type": "arbitrary",
            "samples": [0.0] * 52,
        },
        "x90_gaussian_I_wf_qubit1": {
            "type": "arbitrary",
            "samples": [0.0, 0.0006743914831469624, 0.0014917317652939038, 0.002470618954919889, 0.0036289289967275508, 0.00498284509190342, 0.006545748910327219, 0.008327014670876886, 0.0103307639001362, 0.012554654047246297, 0.014988786339370345, 0.017614825484115262, 0.020405424417963235, 0.023324040026657337, 0.026325210012972514, 0.029355337047969682, 0.03235399510418426, 0.035255736428832896, 0.03799233876277687, 0.04049539450950964, 0.042699110223042326, 0.04454315949759963, 0.04597541805319973, 0.04695440855994418] + [0.047451295375611574] * 2 + [0.04695440855994418, 0.04597541805319973, 0.04454315949759963, 0.042699110223042326, 0.04049539450950964, 0.03799233876277687, 0.035255736428832896, 0.03235399510418426, 0.029355337047969682, 0.026325210012972514, 0.023324040026657337, 0.020405424417963235, 0.017614825484115262, 0.014988786339370345, 0.012554654047246297, 0.0103307639001362, 0.008327014670876886, 0.006545748910327219, 0.00498284509190342, 0.0036289289967275508, 0.002470618954919889, 0.0014917317652939038, 0.0006743914831469624] + [0.0] * 3,
        },
        "x90_gaussian_I_wf_qubit2": {
            "type": "arbitrary",
            "samples": [0.0, 0.0006743914831469624, 0.0014917317652939038, 0.002470618954919889, 0.0036289289967275508, 0.00498284509190342, 0.006545748910327219, 0.008327014670876886, 0.0103307639001362, 0.012554654047246297, 0.014988786339370345, 0.017614825484115262, 0.020405424417963235, 0.023324040026657337, 0.026325210012972514, 0.029355337047969682, 0.03235399510418426, 0.035255736428832896, 0.03799233876277687, 0.04049539450950964, 0.042699110223042326, 0.04454315949759963, 0.04597541805319973, 0.04695440855994418] + [0.047451295375611574] * 2 + [0.04695440855994418, 0.04597541805319973, 0.04454315949759963, 0.042699110223042326, 0.04049539450950964, 0.03799233876277687, 0.035255736428832896, 0.03235399510418426, 0.029355337047969682, 0.026325210012972514, 0.023324040026657337, 0.020405424417963235, 0.017614825484115262, 0.014988786339370345, 0.012554654047246297, 0.0103307639001362, 0.008327014670876886, 0.006545748910327219, 0.00498284509190342, 0.0036289289967275508, 0.002470618954919889, 0.0014917317652939038, 0.0006743914831469624] + [0.0] * 3,
        },
        "x90_gaussian_I_wf_qubit3": {
            "type": "arbitrary",
            "samples": [0.0, 0.0006743914831469624, 0.0014917317652939038, 0.002470618954919889, 0.0036289289967275508, 0.00498284509190342, 0.006545748910327219, 0.008327014670876886, 0.0103307639001362, 0.012554654047246297, 0.014988786339370345, 0.017614825484115262, 0.020405424417963235, 0.023324040026657337, 0.026325210012972514, 0.029355337047969682, 0.03235399510418426, 0.035255736428832896, 0.03799233876277687, 0.04049539450950964, 0.042699110223042326, 0.04454315949759963, 0.04597541805319973, 0.04695440855994418] + [0.047451295375611574] * 2 + [0.04695440855994418, 0.04597541805319973, 0.04454315949759963, 0.042699110223042326, 0.04049539450950964, 0.03799233876277687, 0.035255736428832896, 0.03235399510418426, 0.029355337047969682, 0.026325210012972514, 0.023324040026657337, 0.020405424417963235, 0.017614825484115262, 0.014988786339370345, 0.012554654047246297, 0.0103307639001362, 0.008327014670876886, 0.006545748910327219, 0.00498284509190342, 0.0036289289967275508, 0.002470618954919889, 0.0014917317652939038, 0.0006743914831469624] + [0.0] * 3,
        },
        "x90_gaussian_I_wf_qubit4": {
            "type": "arbitrary",
            "samples": [0.0, 0.0006743914831469624, 0.0014917317652939038, 0.002470618954919889, 0.0036289289967275508, 0.00498284509190342, 0.006545748910327219, 0.008327014670876886, 0.0103307639001362, 0.012554654047246297, 0.014988786339370345, 0.017614825484115262, 0.020405424417963235, 0.023324040026657337, 0.026325210012972514, 0.029355337047969682, 0.03235399510418426, 0.035255736428832896, 0.03799233876277687, 0.04049539450950964, 0.042699110223042326, 0.04454315949759963, 0.04597541805319973, 0.04695440855994418] + [0.047451295375611574] * 2 + [0.04695440855994418, 0.04597541805319973, 0.04454315949759963, 0.042699110223042326, 0.04049539450950964, 0.03799233876277687, 0.035255736428832896, 0.03235399510418426, 0.029355337047969682, 0.026325210012972514, 0.023324040026657337, 0.020405424417963235, 0.017614825484115262, 0.014988786339370345, 0.012554654047246297, 0.0103307639001362, 0.008327014670876886, 0.006545748910327219, 0.00498284509190342, 0.0036289289967275508, 0.002470618954919889, 0.0014917317652939038, 0.0006743914831469624] + [0.0] * 3,
        },
        "x90_gaussian_I_wf_qubit5": {
            "type": "arbitrary",
            "samples": [0.0, 0.0006743914831469624, 0.0014917317652939038, 0.002470618954919889, 0.0036289289967275508, 0.00498284509190342, 0.006545748910327219, 0.008327014670876886, 0.0103307639001362, 0.012554654047246297, 0.014988786339370345, 0.017614825484115262, 0.020405424417963235, 0.023324040026657337, 0.026325210012972514, 0.029355337047969682, 0.03235399510418426, 0.035255736428832896, 0.03799233876277687, 0.04049539450950964, 0.042699110223042326, 0.04454315949759963, 0.04597541805319973, 0.04695440855994418] + [0.047451295375611574] * 2 + [0.04695440855994418, 0.04597541805319973, 0.04454315949759963, 0.042699110223042326, 0.04049539450950964, 0.03799233876277687, 0.035255736428832896, 0.03235399510418426, 0.029355337047969682, 0.026325210012972514, 0.023324040026657337, 0.020405424417963235, 0.017614825484115262, 0.014988786339370345, 0.012554654047246297, 0.0103307639001362, 0.008327014670876886, 0.006545748910327219, 0.00498284509190342, 0.0036289289967275508, 0.002470618954919889, 0.0014917317652939038, 0.0006743914831469624] + [0.0] * 3,
        },
        "x90_gaussian_Q_wf_qubit1": {
            "type": "arbitrary",
            "samples": [0.0] * 52,
        },
        "x90_gaussian_Q_wf_qubit2": {
            "type": "arbitrary",
            "samples": [0.0] * 52,
        },
        "x90_gaussian_Q_wf_qubit3": {
            "type": "arbitrary",
            "samples": [0.0] * 52,
        },
        "x90_gaussian_Q_wf_qubit4": {
            "type": "arbitrary",
            "samples": [0.0] * 52,
        },
        "x90_gaussian_Q_wf_qubit5": {
            "type": "arbitrary",
            "samples": [0.0] * 52,
        },
        "minus_x90_gaussian_I_wf_qubit1": {
            "type": "arbitrary",
            "samples": [0.0, -0.0006743914831469624, -0.0014917317652939038, -0.002470618954919889, -0.0036289289967275508, -0.00498284509190342, -0.006545748910327219, -0.008327014670876886, -0.0103307639001362, -0.012554654047246297, -0.014988786339370345, -0.017614825484115262, -0.020405424417963235, -0.023324040026657337, -0.026325210012972514, -0.029355337047969682, -0.03235399510418426, -0.035255736428832896, -0.03799233876277687, -0.04049539450950964, -0.042699110223042326, -0.04454315949759963, -0.04597541805319973, -0.04695440855994418] + [-0.047451295375611574] * 2 + [-0.04695440855994418, -0.04597541805319973, -0.04454315949759963, -0.042699110223042326, -0.04049539450950964, -0.03799233876277687, -0.035255736428832896, -0.03235399510418426, -0.029355337047969682, -0.026325210012972514, -0.023324040026657337, -0.020405424417963235, -0.017614825484115262, -0.014988786339370345, -0.012554654047246297, -0.0103307639001362, -0.008327014670876886, -0.006545748910327219, -0.00498284509190342, -0.0036289289967275508, -0.002470618954919889, -0.0014917317652939038, -0.0006743914831469624] + [0.0] * 3,
        },
        "minus_x90_gaussian_I_wf_qubit2": {
            "type": "arbitrary",
            "samples": [0.0, -0.0006743914831469624, -0.0014917317652939038, -0.002470618954919889, -0.0036289289967275508, -0.00498284509190342, -0.006545748910327219, -0.008327014670876886, -0.0103307639001362, -0.012554654047246297, -0.014988786339370345, -0.017614825484115262, -0.020405424417963235, -0.023324040026657337, -0.026325210012972514, -0.029355337047969682, -0.03235399510418426, -0.035255736428832896, -0.03799233876277687, -0.04049539450950964, -0.042699110223042326, -0.04454315949759963, -0.04597541805319973, -0.04695440855994418] + [-0.047451295375611574] * 2 + [-0.04695440855994418, -0.04597541805319973, -0.04454315949759963, -0.042699110223042326, -0.04049539450950964, -0.03799233876277687, -0.035255736428832896, -0.03235399510418426, -0.029355337047969682, -0.026325210012972514, -0.023324040026657337, -0.020405424417963235, -0.017614825484115262, -0.014988786339370345, -0.012554654047246297, -0.0103307639001362, -0.008327014670876886, -0.006545748910327219, -0.00498284509190342, -0.0036289289967275508, -0.002470618954919889, -0.0014917317652939038, -0.0006743914831469624] + [0.0] * 3,
        },
        "minus_x90_gaussian_I_wf_qubit3": {
            "type": "arbitrary",
            "samples": [0.0, -0.0006743914831469624, -0.0014917317652939038, -0.002470618954919889, -0.0036289289967275508, -0.00498284509190342, -0.006545748910327219, -0.008327014670876886, -0.0103307639001362, -0.012554654047246297, -0.014988786339370345, -0.017614825484115262, -0.020405424417963235, -0.023324040026657337, -0.026325210012972514, -0.029355337047969682, -0.03235399510418426, -0.035255736428832896, -0.03799233876277687, -0.04049539450950964, -0.042699110223042326, -0.04454315949759963, -0.04597541805319973, -0.04695440855994418] + [-0.047451295375611574] * 2 + [-0.04695440855994418, -0.04597541805319973, -0.04454315949759963, -0.042699110223042326, -0.04049539450950964, -0.03799233876277687, -0.035255736428832896, -0.03235399510418426, -0.029355337047969682, -0.026325210012972514, -0.023324040026657337, -0.020405424417963235, -0.017614825484115262, -0.014988786339370345, -0.012554654047246297, -0.0103307639001362, -0.008327014670876886, -0.006545748910327219, -0.00498284509190342, -0.0036289289967275508, -0.002470618954919889, -0.0014917317652939038, -0.0006743914831469624] + [0.0] * 3,
        },
        "minus_x90_gaussian_I_wf_qubit4": {
            "type": "arbitrary",
            "samples": [0.0, -0.0006743914831469624, -0.0014917317652939038, -0.002470618954919889, -0.0036289289967275508, -0.00498284509190342, -0.006545748910327219, -0.008327014670876886, -0.0103307639001362, -0.012554654047246297, -0.014988786339370345, -0.017614825484115262, -0.020405424417963235, -0.023324040026657337, -0.026325210012972514, -0.029355337047969682, -0.03235399510418426, -0.035255736428832896, -0.03799233876277687, -0.04049539450950964, -0.042699110223042326, -0.04454315949759963, -0.04597541805319973, -0.04695440855994418] + [-0.047451295375611574] * 2 + [-0.04695440855994418, -0.04597541805319973, -0.04454315949759963, -0.042699110223042326, -0.04049539450950964, -0.03799233876277687, -0.035255736428832896, -0.03235399510418426, -0.029355337047969682, -0.026325210012972514, -0.023324040026657337, -0.020405424417963235, -0.017614825484115262, -0.014988786339370345, -0.012554654047246297, -0.0103307639001362, -0.008327014670876886, -0.006545748910327219, -0.00498284509190342, -0.0036289289967275508, -0.002470618954919889, -0.0014917317652939038, -0.0006743914831469624] + [0.0] * 3,
        },
        "minus_x90_gaussian_I_wf_qubit5": {
            "type": "arbitrary",
            "samples": [0.0, -0.0006743914831469624, -0.0014917317652939038, -0.002470618954919889, -0.0036289289967275508, -0.00498284509190342, -0.006545748910327219, -0.008327014670876886, -0.0103307639001362, -0.012554654047246297, -0.014988786339370345, -0.017614825484115262, -0.020405424417963235, -0.023324040026657337, -0.026325210012972514, -0.029355337047969682, -0.03235399510418426, -0.035255736428832896, -0.03799233876277687, -0.04049539450950964, -0.042699110223042326, -0.04454315949759963, -0.04597541805319973, -0.04695440855994418] + [-0.047451295375611574] * 2 + [-0.04695440855994418, -0.04597541805319973, -0.04454315949759963, -0.042699110223042326, -0.04049539450950964, -0.03799233876277687, -0.035255736428832896, -0.03235399510418426, -0.029355337047969682, -0.026325210012972514, -0.023324040026657337, -0.020405424417963235, -0.017614825484115262, -0.014988786339370345, -0.012554654047246297, -0.0103307639001362, -0.008327014670876886, -0.006545748910327219, -0.00498284509190342, -0.0036289289967275508, -0.002470618954919889, -0.0014917317652939038, -0.0006743914831469624] + [0.0] * 3,
        },
        "minus_x90_gaussian_Q_wf_qubit1": {
            "type": "arbitrary",
            "samples": [0.0] * 52,
        },
        "minus_x90_gaussian_Q_wf_qubit2": {
            "type": "arbitrary",
            "samples": [0.0] * 52,
        },
        "minus_x90_gaussian_Q_wf_qubit3": {
            "type": "arbitrary",
            "samples": [0.0] * 52,
        },
        "minus_x90_gaussian_Q_wf_qubit4": {
            "type": "arbitrary",
            "samples": [0.0] * 52,
        },
        "minus_x90_gaussian_Q_wf_qubit5": {
            "type": "arbitrary",
            "samples": [0.0] * 52,
        },
        "y180_gaussian_I_wf_qubit1": {
            "type": "arbitrary",
            "samples": [-0.0] * 52,
        },
        "y180_gaussian_I_wf_qubit2": {
            "type": "arbitrary",
            "samples": [-0.0] * 52,
        },
        "y180_gaussian_I_wf_qubit3": {
            "type": "arbitrary",
            "samples": [-0.0] * 52,
        },
        "y180_gaussian_I_wf_qubit4": {
            "type": "arbitrary",
            "samples": [-0.0] * 52,
        },
        "y180_gaussian_I_wf_qubit5": {
            "type": "arbitrary",
            "samples": [-0.0] * 52,
        },
        "y180_gaussian_Q_wf_qubit1": {
            "type": "arbitrary",
            "samples": [0.0, 0.0013487829662939248, 0.0029834635305878076, 0.004941237909839778, 0.0072578579934551015, 0.00996569018380684, 0.013091497820654437, 0.016654029341753772, 0.0206615278002724, 0.025109308094492595, 0.02997757267874069, 0.035229650968230525, 0.04081084883592647, 0.046648080053314674, 0.05265042002594503, 0.058710674095939365, 0.06470799020836852, 0.07051147285766579, 0.07598467752555374, 0.08099078901901928, 0.08539822044608465, 0.08908631899519925, 0.09195083610639947, 0.09390881711988835] + [0.09490259075122315] * 2 + [0.09390881711988835, 0.09195083610639947, 0.08908631899519925, 0.08539822044608465, 0.08099078901901928, 0.07598467752555374, 0.07051147285766579, 0.06470799020836852, 0.058710674095939365, 0.05265042002594503, 0.046648080053314674, 0.04081084883592647, 0.035229650968230525, 0.02997757267874069, 0.025109308094492595, 0.0206615278002724, 0.016654029341753772, 0.013091497820654437, 0.00996569018380684, 0.0072578579934551015, 0.004941237909839778, 0.0029834635305878076, 0.0013487829662939248] + [0.0] * 3,
        },
        "y180_gaussian_Q_wf_qubit2": {
            "type": "arbitrary",
            "samples": [0.0, 0.0013487829662939248, 0.0029834635305878076, 0.004941237909839778, 0.0072578579934551015, 0.00996569018380684, 0.013091497820654437, 0.016654029341753772, 0.0206615278002724, 0.025109308094492595, 0.02997757267874069, 0.035229650968230525, 0.04081084883592647, 0.046648080053314674, 0.05265042002594503, 0.058710674095939365, 0.06470799020836852, 0.07051147285766579, 0.07598467752555374, 0.08099078901901928, 0.08539822044608465, 0.08908631899519925, 0.09195083610639947, 0.09390881711988835] + [0.09490259075122315] * 2 + [0.09390881711988835, 0.09195083610639947, 0.08908631899519925, 0.08539822044608465, 0.08099078901901928, 0.07598467752555374, 0.07051147285766579, 0.06470799020836852, 0.058710674095939365, 0.05265042002594503, 0.046648080053314674, 0.04081084883592647, 0.035229650968230525, 0.02997757267874069, 0.025109308094492595, 0.0206615278002724, 0.016654029341753772, 0.013091497820654437, 0.00996569018380684, 0.0072578579934551015, 0.004941237909839778, 0.0029834635305878076, 0.0013487829662939248] + [0.0] * 3,
        },
        "y180_gaussian_Q_wf_qubit3": {
            "type": "arbitrary",
            "samples": [0.0, 0.0013487829662939248, 0.0029834635305878076, 0.004941237909839778, 0.0072578579934551015, 0.00996569018380684, 0.013091497820654437, 0.016654029341753772, 0.0206615278002724, 0.025109308094492595, 0.02997757267874069, 0.035229650968230525, 0.04081084883592647, 0.046648080053314674, 0.05265042002594503, 0.058710674095939365, 0.06470799020836852, 0.07051147285766579, 0.07598467752555374, 0.08099078901901928, 0.08539822044608465, 0.08908631899519925, 0.09195083610639947, 0.09390881711988835] + [0.09490259075122315] * 2 + [0.09390881711988835, 0.09195083610639947, 0.08908631899519925, 0.08539822044608465, 0.08099078901901928, 0.07598467752555374, 0.07051147285766579, 0.06470799020836852, 0.058710674095939365, 0.05265042002594503, 0.046648080053314674, 0.04081084883592647, 0.035229650968230525, 0.02997757267874069, 0.025109308094492595, 0.0206615278002724, 0.016654029341753772, 0.013091497820654437, 0.00996569018380684, 0.0072578579934551015, 0.004941237909839778, 0.0029834635305878076, 0.0013487829662939248] + [0.0] * 3,
        },
        "y180_gaussian_Q_wf_qubit4": {
            "type": "arbitrary",
            "samples": [0.0, 0.0013487829662939248, 0.0029834635305878076, 0.004941237909839778, 0.0072578579934551015, 0.00996569018380684, 0.013091497820654437, 0.016654029341753772, 0.0206615278002724, 0.025109308094492595, 0.02997757267874069, 0.035229650968230525, 0.04081084883592647, 0.046648080053314674, 0.05265042002594503, 0.058710674095939365, 0.06470799020836852, 0.07051147285766579, 0.07598467752555374, 0.08099078901901928, 0.08539822044608465, 0.08908631899519925, 0.09195083610639947, 0.09390881711988835] + [0.09490259075122315] * 2 + [0.09390881711988835, 0.09195083610639947, 0.08908631899519925, 0.08539822044608465, 0.08099078901901928, 0.07598467752555374, 0.07051147285766579, 0.06470799020836852, 0.058710674095939365, 0.05265042002594503, 0.046648080053314674, 0.04081084883592647, 0.035229650968230525, 0.02997757267874069, 0.025109308094492595, 0.0206615278002724, 0.016654029341753772, 0.013091497820654437, 0.00996569018380684, 0.0072578579934551015, 0.004941237909839778, 0.0029834635305878076, 0.0013487829662939248] + [0.0] * 3,
        },
        "y180_gaussian_Q_wf_qubit5": {
            "type": "arbitrary",
            "samples": [0.0, 0.0013487829662939248, 0.0029834635305878076, 0.004941237909839778, 0.0072578579934551015, 0.00996569018380684, 0.013091497820654437, 0.016654029341753772, 0.0206615278002724, 0.025109308094492595, 0.02997757267874069, 0.035229650968230525, 0.04081084883592647, 0.046648080053314674, 0.05265042002594503, 0.058710674095939365, 0.06470799020836852, 0.07051147285766579, 0.07598467752555374, 0.08099078901901928, 0.08539822044608465, 0.08908631899519925, 0.09195083610639947, 0.09390881711988835] + [0.09490259075122315] * 2 + [0.09390881711988835, 0.09195083610639947, 0.08908631899519925, 0.08539822044608465, 0.08099078901901928, 0.07598467752555374, 0.07051147285766579, 0.06470799020836852, 0.058710674095939365, 0.05265042002594503, 0.046648080053314674, 0.04081084883592647, 0.035229650968230525, 0.02997757267874069, 0.025109308094492595, 0.0206615278002724, 0.016654029341753772, 0.013091497820654437, 0.00996569018380684, 0.0072578579934551015, 0.004941237909839778, 0.0029834635305878076, 0.0013487829662939248] + [0.0] * 3,
        },
        "y90_gaussian_I_wf_qubit1": {
            "type": "arbitrary",
            "samples": [-0.0] * 52,
        },
        "y90_gaussian_I_wf_qubit2": {
            "type": "arbitrary",
            "samples": [-0.0] * 52,
        },
        "y90_gaussian_I_wf_qubit3": {
            "type": "arbitrary",
            "samples": [-0.0] * 52,
        },
        "y90_gaussian_I_wf_qubit4": {
            "type": "arbitrary",
            "samples": [-0.0] * 52,
        },
        "y90_gaussian_I_wf_qubit5": {
            "type": "arbitrary",
            "samples": [-0.0] * 52,
        },
        "y90_gaussian_Q_wf_qubit1": {
            "type": "arbitrary",
            "samples": [0.0, 0.0006743914831469624, 0.0014917317652939038, 0.002470618954919889, 0.0036289289967275508, 0.00498284509190342, 0.006545748910327219, 0.008327014670876886, 0.0103307639001362, 0.012554654047246297, 0.014988786339370345, 0.017614825484115262, 0.020405424417963235, 0.023324040026657337, 0.026325210012972514, 0.029355337047969682, 0.03235399510418426, 0.035255736428832896, 0.03799233876277687, 0.04049539450950964, 0.042699110223042326, 0.04454315949759963, 0.04597541805319973, 0.04695440855994418] + [0.047451295375611574] * 2 + [0.04695440855994418, 0.04597541805319973, 0.04454315949759963, 0.042699110223042326, 0.04049539450950964, 0.03799233876277687, 0.035255736428832896, 0.03235399510418426, 0.029355337047969682, 0.026325210012972514, 0.023324040026657337, 0.020405424417963235, 0.017614825484115262, 0.014988786339370345, 0.012554654047246297, 0.0103307639001362, 0.008327014670876886, 0.006545748910327219, 0.00498284509190342, 0.0036289289967275508, 0.002470618954919889, 0.0014917317652939038, 0.0006743914831469624] + [0.0] * 3,
        },
        "y90_gaussian_Q_wf_qubit2": {
            "type": "arbitrary",
            "samples": [0.0, 0.0006743914831469624, 0.0014917317652939038, 0.002470618954919889, 0.0036289289967275508, 0.00498284509190342, 0.006545748910327219, 0.008327014670876886, 0.0103307639001362, 0.012554654047246297, 0.014988786339370345, 0.017614825484115262, 0.020405424417963235, 0.023324040026657337, 0.026325210012972514, 0.029355337047969682, 0.03235399510418426, 0.035255736428832896, 0.03799233876277687, 0.04049539450950964, 0.042699110223042326, 0.04454315949759963, 0.04597541805319973, 0.04695440855994418] + [0.047451295375611574] * 2 + [0.04695440855994418, 0.04597541805319973, 0.04454315949759963, 0.042699110223042326, 0.04049539450950964, 0.03799233876277687, 0.035255736428832896, 0.03235399510418426, 0.029355337047969682, 0.026325210012972514, 0.023324040026657337, 0.020405424417963235, 0.017614825484115262, 0.014988786339370345, 0.012554654047246297, 0.0103307639001362, 0.008327014670876886, 0.006545748910327219, 0.00498284509190342, 0.0036289289967275508, 0.002470618954919889, 0.0014917317652939038, 0.0006743914831469624] + [0.0] * 3,
        },
        "y90_gaussian_Q_wf_qubit3": {
            "type": "arbitrary",
            "samples": [0.0, 0.0006743914831469624, 0.0014917317652939038, 0.002470618954919889, 0.0036289289967275508, 0.00498284509190342, 0.006545748910327219, 0.008327014670876886, 0.0103307639001362, 0.012554654047246297, 0.014988786339370345, 0.017614825484115262, 0.020405424417963235, 0.023324040026657337, 0.026325210012972514, 0.029355337047969682, 0.03235399510418426, 0.035255736428832896, 0.03799233876277687, 0.04049539450950964, 0.042699110223042326, 0.04454315949759963, 0.04597541805319973, 0.04695440855994418] + [0.047451295375611574] * 2 + [0.04695440855994418, 0.04597541805319973, 0.04454315949759963, 0.042699110223042326, 0.04049539450950964, 0.03799233876277687, 0.035255736428832896, 0.03235399510418426, 0.029355337047969682, 0.026325210012972514, 0.023324040026657337, 0.020405424417963235, 0.017614825484115262, 0.014988786339370345, 0.012554654047246297, 0.0103307639001362, 0.008327014670876886, 0.006545748910327219, 0.00498284509190342, 0.0036289289967275508, 0.002470618954919889, 0.0014917317652939038, 0.0006743914831469624] + [0.0] * 3,
        },
        "y90_gaussian_Q_wf_qubit4": {
            "type": "arbitrary",
            "samples": [0.0, 0.0006743914831469624, 0.0014917317652939038, 0.002470618954919889, 0.0036289289967275508, 0.00498284509190342, 0.006545748910327219, 0.008327014670876886, 0.0103307639001362, 0.012554654047246297, 0.014988786339370345, 0.017614825484115262, 0.020405424417963235, 0.023324040026657337, 0.026325210012972514, 0.029355337047969682, 0.03235399510418426, 0.035255736428832896, 0.03799233876277687, 0.04049539450950964, 0.042699110223042326, 0.04454315949759963, 0.04597541805319973, 0.04695440855994418] + [0.047451295375611574] * 2 + [0.04695440855994418, 0.04597541805319973, 0.04454315949759963, 0.042699110223042326, 0.04049539450950964, 0.03799233876277687, 0.035255736428832896, 0.03235399510418426, 0.029355337047969682, 0.026325210012972514, 0.023324040026657337, 0.020405424417963235, 0.017614825484115262, 0.014988786339370345, 0.012554654047246297, 0.0103307639001362, 0.008327014670876886, 0.006545748910327219, 0.00498284509190342, 0.0036289289967275508, 0.002470618954919889, 0.0014917317652939038, 0.0006743914831469624] + [0.0] * 3,
        },
        "y90_gaussian_Q_wf_qubit5": {
            "type": "arbitrary",
            "samples": [0.0, 0.0006743914831469624, 0.0014917317652939038, 0.002470618954919889, 0.0036289289967275508, 0.00498284509190342, 0.006545748910327219, 0.008327014670876886, 0.0103307639001362, 0.012554654047246297, 0.014988786339370345, 0.017614825484115262, 0.020405424417963235, 0.023324040026657337, 0.026325210012972514, 0.029355337047969682, 0.03235399510418426, 0.035255736428832896, 0.03799233876277687, 0.04049539450950964, 0.042699110223042326, 0.04454315949759963, 0.04597541805319973, 0.04695440855994418] + [0.047451295375611574] * 2 + [0.04695440855994418, 0.04597541805319973, 0.04454315949759963, 0.042699110223042326, 0.04049539450950964, 0.03799233876277687, 0.035255736428832896, 0.03235399510418426, 0.029355337047969682, 0.026325210012972514, 0.023324040026657337, 0.020405424417963235, 0.017614825484115262, 0.014988786339370345, 0.012554654047246297, 0.0103307639001362, 0.008327014670876886, 0.006545748910327219, 0.00498284509190342, 0.0036289289967275508, 0.002470618954919889, 0.0014917317652939038, 0.0006743914831469624] + [0.0] * 3,
        },
        "minus_y90_gaussian_I_wf_qubit1": {
            "type": "arbitrary",
            "samples": [-0.0] * 52,
        },
        "minus_y90_gaussian_I_wf_qubit2": {
            "type": "arbitrary",
            "samples": [-0.0] * 52,
        },
        "minus_y90_gaussian_I_wf_qubit3": {
            "type": "arbitrary",
            "samples": [-0.0] * 52,
        },
        "minus_y90_gaussian_I_wf_qubit4": {
            "type": "arbitrary",
            "samples": [-0.0] * 52,
        },
        "minus_y90_gaussian_I_wf_qubit5": {
            "type": "arbitrary",
            "samples": [-0.0] * 52,
        },
        "minus_y90_gaussian_Q_wf_qubit1": {
            "type": "arbitrary",
            "samples": [0.0, -0.0006743914831469624, -0.0014917317652939038, -0.002470618954919889, -0.0036289289967275508, -0.00498284509190342, -0.006545748910327219, -0.008327014670876886, -0.0103307639001362, -0.012554654047246297, -0.014988786339370345, -0.017614825484115262, -0.020405424417963235, -0.023324040026657337, -0.026325210012972514, -0.029355337047969682, -0.03235399510418426, -0.035255736428832896, -0.03799233876277687, -0.04049539450950964, -0.042699110223042326, -0.04454315949759963, -0.04597541805319973, -0.04695440855994418] + [-0.047451295375611574] * 2 + [-0.04695440855994418, -0.04597541805319973, -0.04454315949759963, -0.042699110223042326, -0.04049539450950964, -0.03799233876277687, -0.035255736428832896, -0.03235399510418426, -0.029355337047969682, -0.026325210012972514, -0.023324040026657337, -0.020405424417963235, -0.017614825484115262, -0.014988786339370345, -0.012554654047246297, -0.0103307639001362, -0.008327014670876886, -0.006545748910327219, -0.00498284509190342, -0.0036289289967275508, -0.002470618954919889, -0.0014917317652939038, -0.0006743914831469624] + [0.0] * 3,
        },
        "minus_y90_gaussian_Q_wf_qubit2": {
            "type": "arbitrary",
            "samples": [0.0, -0.0006743914831469624, -0.0014917317652939038, -0.002470618954919889, -0.0036289289967275508, -0.00498284509190342, -0.006545748910327219, -0.008327014670876886, -0.0103307639001362, -0.012554654047246297, -0.014988786339370345, -0.017614825484115262, -0.020405424417963235, -0.023324040026657337, -0.026325210012972514, -0.029355337047969682, -0.03235399510418426, -0.035255736428832896, -0.03799233876277687, -0.04049539450950964, -0.042699110223042326, -0.04454315949759963, -0.04597541805319973, -0.04695440855994418] + [-0.047451295375611574] * 2 + [-0.04695440855994418, -0.04597541805319973, -0.04454315949759963, -0.042699110223042326, -0.04049539450950964, -0.03799233876277687, -0.035255736428832896, -0.03235399510418426, -0.029355337047969682, -0.026325210012972514, -0.023324040026657337, -0.020405424417963235, -0.017614825484115262, -0.014988786339370345, -0.012554654047246297, -0.0103307639001362, -0.008327014670876886, -0.006545748910327219, -0.00498284509190342, -0.0036289289967275508, -0.002470618954919889, -0.0014917317652939038, -0.0006743914831469624] + [0.0] * 3,
        },
        "minus_y90_gaussian_Q_wf_qubit3": {
            "type": "arbitrary",
            "samples": [0.0, -0.0006743914831469624, -0.0014917317652939038, -0.002470618954919889, -0.0036289289967275508, -0.00498284509190342, -0.006545748910327219, -0.008327014670876886, -0.0103307639001362, -0.012554654047246297, -0.014988786339370345, -0.017614825484115262, -0.020405424417963235, -0.023324040026657337, -0.026325210012972514, -0.029355337047969682, -0.03235399510418426, -0.035255736428832896, -0.03799233876277687, -0.04049539450950964, -0.042699110223042326, -0.04454315949759963, -0.04597541805319973, -0.04695440855994418] + [-0.047451295375611574] * 2 + [-0.04695440855994418, -0.04597541805319973, -0.04454315949759963, -0.042699110223042326, -0.04049539450950964, -0.03799233876277687, -0.035255736428832896, -0.03235399510418426, -0.029355337047969682, -0.026325210012972514, -0.023324040026657337, -0.020405424417963235, -0.017614825484115262, -0.014988786339370345, -0.012554654047246297, -0.0103307639001362, -0.008327014670876886, -0.006545748910327219, -0.00498284509190342, -0.0036289289967275508, -0.002470618954919889, -0.0014917317652939038, -0.0006743914831469624] + [0.0] * 3,
        },
        "minus_y90_gaussian_Q_wf_qubit4": {
            "type": "arbitrary",
            "samples": [0.0, -0.0006743914831469624, -0.0014917317652939038, -0.002470618954919889, -0.0036289289967275508, -0.00498284509190342, -0.006545748910327219, -0.008327014670876886, -0.0103307639001362, -0.012554654047246297, -0.014988786339370345, -0.017614825484115262, -0.020405424417963235, -0.023324040026657337, -0.026325210012972514, -0.029355337047969682, -0.03235399510418426, -0.035255736428832896, -0.03799233876277687, -0.04049539450950964, -0.042699110223042326, -0.04454315949759963, -0.04597541805319973, -0.04695440855994418] + [-0.047451295375611574] * 2 + [-0.04695440855994418, -0.04597541805319973, -0.04454315949759963, -0.042699110223042326, -0.04049539450950964, -0.03799233876277687, -0.035255736428832896, -0.03235399510418426, -0.029355337047969682, -0.026325210012972514, -0.023324040026657337, -0.020405424417963235, -0.017614825484115262, -0.014988786339370345, -0.012554654047246297, -0.0103307639001362, -0.008327014670876886, -0.006545748910327219, -0.00498284509190342, -0.0036289289967275508, -0.002470618954919889, -0.0014917317652939038, -0.0006743914831469624] + [0.0] * 3,
        },
        "minus_y90_gaussian_Q_wf_qubit5": {
            "type": "arbitrary",
            "samples": [0.0, -0.0006743914831469624, -0.0014917317652939038, -0.002470618954919889, -0.0036289289967275508, -0.00498284509190342, -0.006545748910327219, -0.008327014670876886, -0.0103307639001362, -0.012554654047246297, -0.014988786339370345, -0.017614825484115262, -0.020405424417963235, -0.023324040026657337, -0.026325210012972514, -0.029355337047969682, -0.03235399510418426, -0.035255736428832896, -0.03799233876277687, -0.04049539450950964, -0.042699110223042326, -0.04454315949759963, -0.04597541805319973, -0.04695440855994418] + [-0.047451295375611574] * 2 + [-0.04695440855994418, -0.04597541805319973, -0.04454315949759963, -0.042699110223042326, -0.04049539450950964, -0.03799233876277687, -0.035255736428832896, -0.03235399510418426, -0.029355337047969682, -0.026325210012972514, -0.023324040026657337, -0.020405424417963235, -0.017614825484115262, -0.014988786339370345, -0.012554654047246297, -0.0103307639001362, -0.008327014670876886, -0.006545748910327219, -0.00498284509190342, -0.0036289289967275508, -0.002470618954919889, -0.0014917317652939038, -0.0006743914831469624] + [0.0] * 3,
        },
        "x180_gaussian_I_wf_qp_control_c3t2": {
            "type": "arbitrary",
            "samples": [0.0, 0.000623059395668357, 0.0013134158229892211, 0.00207600456516317, 0.0029157968026681785, 0.003837749297415329, 0.004846747956223626, 0.0059475454464649755, 0.007144693172446949, 0.008442468066474543, 0.00984479480112677, 0.01135516418617893, 0.012976548671420715, 0.014711316031583668, 0.016561142457583073, 0.01852692641493371, 0.020608704751007553, 0.02280557263323139, 0.02511560897595016, 0.027535809060335543, 0.03006202606562717, 0.03268892320793267, 0.035409938122250045, 0.038217261022609625, 0.04110182803350147, 0.04405333090334345, 0.04706024408905373, 0.05010986994237358, 0.05318840243716088, 0.05628100955729227, 0.059371934122988815, 0.06244461247619, 0.06548181008073263, 0.06846577272886803, 0.07137839169082312, 0.07420138080762224, 0.07691646321812151, 0.07950556513773178, 0.08195101387660032, 0.08423573710622746, 0.08634346026167618, 0.08825889890645858, 0.08996794289214834, 0.09145782921645602, 0.09271730062188518, 0.09373674718038912, 0.09450832837415593, 0.09502607350358355] + [0.09528595862392984] * 2 + [0.09502607350358355, 0.09450832837415593, 0.09373674718038912, 0.09271730062188518, 0.09145782921645602, 0.08996794289214834, 0.08825889890645858, 0.08634346026167618, 0.08423573710622746, 0.08195101387660032, 0.07950556513773178, 0.07691646321812151, 0.07420138080762224, 0.07137839169082312, 0.06846577272886803, 0.06548181008073263, 0.06244461247619, 0.059371934122988815, 0.05628100955729227, 0.05318840243716088, 0.05010986994237358, 0.04706024408905373, 0.04405333090334345, 0.04110182803350147, 0.038217261022609625, 0.035409938122250045, 0.03268892320793267, 0.03006202606562717, 0.027535809060335543, 0.02511560897595016, 0.02280557263323139, 0.020608704751007553, 0.01852692641493371, 0.016561142457583073, 0.014711316031583668, 0.012976548671420715, 0.01135516418617893, 0.00984479480112677, 0.008442468066474543, 0.007144693172446949, 0.0059475454464649755, 0.004846747956223626, 0.003837749297415329, 0.0029157968026681785, 0.00207600456516317, 0.0013134158229892211, 0.000623059395668357] + [0.0] * 3,
        },
        "x180_gaussian_Q_wf_qp_control_c3t2": {
            "type": "arbitrary",
            "samples": [0.0] * 100,
        },
        "x90_gaussian_I_wf_qp_control_c3t2": {
            "type": "arbitrary",
            "samples": [0.0, 0.0003115296978341785, 0.0006567079114946106, 0.001038002282581585, 0.0014578984013340892, 0.0019188746487076645, 0.002423373978111813, 0.0029737727232324877, 0.0035723465862234744, 0.004221234033237271, 0.004922397400563385, 0.005677582093089465, 0.0064882743357103576, 0.007355658015791834, 0.008280571228791537, 0.009263463207466856, 0.010304352375503777, 0.011402786316615695, 0.01255780448797508, 0.013767904530167772, 0.015031013032813585, 0.016344461603966336, 0.017704969061125023, 0.019108630511304812, 0.020550914016750736, 0.022026665451671725, 0.023530122044526865, 0.02505493497118679, 0.02659420121858044, 0.028140504778646134, 0.029685967061494407, 0.031222306238095, 0.032740905040366315, 0.034232886364434015, 0.03568919584541156, 0.03710069040381112, 0.038458231609060756, 0.03975278256886589, 0.04097550693830016, 0.04211786855311373, 0.04317173013083809, 0.04412944945322929, 0.04498397144607417, 0.04572891460822801, 0.04635865031094259, 0.04686837359019456, 0.047254164187077966, 0.047513036751791776] + [0.04764297931196492] * 2 + [0.047513036751791776, 0.047254164187077966, 0.04686837359019456, 0.04635865031094259, 0.04572891460822801, 0.04498397144607417, 0.04412944945322929, 0.04317173013083809, 0.04211786855311373, 0.04097550693830016, 0.03975278256886589, 0.038458231609060756, 0.03710069040381112, 0.03568919584541156, 0.034232886364434015, 0.032740905040366315, 0.031222306238095, 0.029685967061494407, 0.028140504778646134, 0.02659420121858044, 0.02505493497118679, 0.023530122044526865, 0.022026665451671725, 0.020550914016750736, 0.019108630511304812, 0.017704969061125023, 0.016344461603966336, 0.015031013032813585, 0.013767904530167772, 0.01255780448797508, 0.011402786316615695, 0.010304352375503777, 0.009263463207466856, 0.008280571228791537, 0.007355658015791834, 0.0064882743357103576, 0.005677582093089465, 0.004922397400563385, 0.004221234033237271, 0.0035723465862234744, 0.0029737727232324877, 0.002423373978111813, 0.0019188746487076645, 0.0014578984013340892, 0.001038002282581585, 0.0006567079114946106, 0.0003115296978341785] + [0.0] * 3,
        },
        "x90_gaussian_Q_wf_qp_control_c3t2": {
            "type": "arbitrary",
            "samples": [0.0] * 100,
        },
        "minus_x90_gaussian_I_wf_qp_control_c3t2": {
            "type": "arbitrary",
            "samples": [0.0, -0.0003115296978341785, -0.0006567079114946106, -0.001038002282581585, -0.0014578984013340892, -0.0019188746487076645, -0.002423373978111813, -0.0029737727232324877, -0.0035723465862234744, -0.004221234033237271, -0.004922397400563385, -0.005677582093089465, -0.0064882743357103576, -0.007355658015791834, -0.008280571228791537, -0.009263463207466856, -0.010304352375503777, -0.011402786316615695, -0.01255780448797508, -0.013767904530167772, -0.015031013032813585, -0.016344461603966336, -0.017704969061125023, -0.019108630511304812, -0.020550914016750736, -0.022026665451671725, -0.023530122044526865, -0.02505493497118679, -0.02659420121858044, -0.028140504778646134, -0.029685967061494407, -0.031222306238095, -0.032740905040366315, -0.034232886364434015, -0.03568919584541156, -0.03710069040381112, -0.038458231609060756, -0.03975278256886589, -0.04097550693830016, -0.04211786855311373, -0.04317173013083809, -0.04412944945322929, -0.04498397144607417, -0.04572891460822801, -0.04635865031094259, -0.04686837359019456, -0.047254164187077966, -0.047513036751791776] + [-0.04764297931196492] * 2 + [-0.047513036751791776, -0.047254164187077966, -0.04686837359019456, -0.04635865031094259, -0.04572891460822801, -0.04498397144607417, -0.04412944945322929, -0.04317173013083809, -0.04211786855311373, -0.04097550693830016, -0.03975278256886589, -0.038458231609060756, -0.03710069040381112, -0.03568919584541156, -0.034232886364434015, -0.032740905040366315, -0.031222306238095, -0.029685967061494407, -0.028140504778646134, -0.02659420121858044, -0.02505493497118679, -0.023530122044526865, -0.022026665451671725, -0.020550914016750736, -0.019108630511304812, -0.017704969061125023, -0.016344461603966336, -0.015031013032813585, -0.013767904530167772, -0.01255780448797508, -0.011402786316615695, -0.010304352375503777, -0.009263463207466856, -0.008280571228791537, -0.007355658015791834, -0.0064882743357103576, -0.005677582093089465, -0.004922397400563385, -0.004221234033237271, -0.0035723465862234744, -0.0029737727232324877, -0.002423373978111813, -0.0019188746487076645, -0.0014578984013340892, -0.001038002282581585, -0.0006567079114946106, -0.0003115296978341785] + [0.0] * 3,
        },
        "minus_x90_gaussian_Q_wf_qp_control_c3t2": {
            "type": "arbitrary",
            "samples": [0.0] * 100,
        },
        "y180_gaussian_I_wf_qp_control_c3t2": {
            "type": "arbitrary",
            "samples": [-0.0] * 100,
        },
        "y180_gaussian_Q_wf_qp_control_c3t2": {
            "type": "arbitrary",
            "samples": [0.0, 0.000623059395668357, 0.0013134158229892211, 0.00207600456516317, 0.0029157968026681785, 0.003837749297415329, 0.004846747956223626, 0.0059475454464649755, 0.007144693172446949, 0.008442468066474543, 0.00984479480112677, 0.01135516418617893, 0.012976548671420715, 0.014711316031583668, 0.016561142457583073, 0.01852692641493371, 0.020608704751007553, 0.02280557263323139, 0.02511560897595016, 0.027535809060335543, 0.03006202606562717, 0.03268892320793267, 0.035409938122250045, 0.038217261022609625, 0.04110182803350147, 0.04405333090334345, 0.04706024408905373, 0.05010986994237358, 0.05318840243716088, 0.05628100955729227, 0.059371934122988815, 0.06244461247619, 0.06548181008073263, 0.06846577272886803, 0.07137839169082312, 0.07420138080762224, 0.07691646321812151, 0.07950556513773178, 0.08195101387660032, 0.08423573710622746, 0.08634346026167618, 0.08825889890645858, 0.08996794289214834, 0.09145782921645602, 0.09271730062188518, 0.09373674718038912, 0.09450832837415593, 0.09502607350358355] + [0.09528595862392984] * 2 + [0.09502607350358355, 0.09450832837415593, 0.09373674718038912, 0.09271730062188518, 0.09145782921645602, 0.08996794289214834, 0.08825889890645858, 0.08634346026167618, 0.08423573710622746, 0.08195101387660032, 0.07950556513773178, 0.07691646321812151, 0.07420138080762224, 0.07137839169082312, 0.06846577272886803, 0.06548181008073263, 0.06244461247619, 0.059371934122988815, 0.05628100955729227, 0.05318840243716088, 0.05010986994237358, 0.04706024408905373, 0.04405333090334345, 0.04110182803350147, 0.038217261022609625, 0.035409938122250045, 0.03268892320793267, 0.03006202606562717, 0.027535809060335543, 0.02511560897595016, 0.02280557263323139, 0.020608704751007553, 0.01852692641493371, 0.016561142457583073, 0.014711316031583668, 0.012976548671420715, 0.01135516418617893, 0.00984479480112677, 0.008442468066474543, 0.007144693172446949, 0.0059475454464649755, 0.004846747956223626, 0.003837749297415329, 0.0029157968026681785, 0.00207600456516317, 0.0013134158229892211, 0.000623059395668357] + [0.0] * 3,
        },
        "y90_gaussian_I_wf_qp_control_c3t2": {
            "type": "arbitrary",
            "samples": [-0.0] * 100,
        },
        "y90_gaussian_Q_wf_qp_control_c3t2": {
            "type": "arbitrary",
            "samples": [0.0, 0.0003115296978341785, 0.0006567079114946106, 0.001038002282581585, 0.0014578984013340892, 0.0019188746487076645, 0.002423373978111813, 0.0029737727232324877, 0.0035723465862234744, 0.004221234033237271, 0.004922397400563385, 0.005677582093089465, 0.0064882743357103576, 0.007355658015791834, 0.008280571228791537, 0.009263463207466856, 0.010304352375503777, 0.011402786316615695, 0.01255780448797508, 0.013767904530167772, 0.015031013032813585, 0.016344461603966336, 0.017704969061125023, 0.019108630511304812, 0.020550914016750736, 0.022026665451671725, 0.023530122044526865, 0.02505493497118679, 0.02659420121858044, 0.028140504778646134, 0.029685967061494407, 0.031222306238095, 0.032740905040366315, 0.034232886364434015, 0.03568919584541156, 0.03710069040381112, 0.038458231609060756, 0.03975278256886589, 0.04097550693830016, 0.04211786855311373, 0.04317173013083809, 0.04412944945322929, 0.04498397144607417, 0.04572891460822801, 0.04635865031094259, 0.04686837359019456, 0.047254164187077966, 0.047513036751791776] + [0.04764297931196492] * 2 + [0.047513036751791776, 0.047254164187077966, 0.04686837359019456, 0.04635865031094259, 0.04572891460822801, 0.04498397144607417, 0.04412944945322929, 0.04317173013083809, 0.04211786855311373, 0.04097550693830016, 0.03975278256886589, 0.038458231609060756, 0.03710069040381112, 0.03568919584541156, 0.034232886364434015, 0.032740905040366315, 0.031222306238095, 0.029685967061494407, 0.028140504778646134, 0.02659420121858044, 0.02505493497118679, 0.023530122044526865, 0.022026665451671725, 0.020550914016750736, 0.019108630511304812, 0.017704969061125023, 0.016344461603966336, 0.015031013032813585, 0.013767904530167772, 0.01255780448797508, 0.011402786316615695, 0.010304352375503777, 0.009263463207466856, 0.008280571228791537, 0.007355658015791834, 0.0064882743357103576, 0.005677582093089465, 0.004922397400563385, 0.004221234033237271, 0.0035723465862234744, 0.0029737727232324877, 0.002423373978111813, 0.0019188746487076645, 0.0014578984013340892, 0.001038002282581585, 0.0006567079114946106, 0.0003115296978341785] + [0.0] * 3,
        },
        "minus_y90_gaussian_I_wf_qp_control_c3t2": {
            "type": "arbitrary",
            "samples": [-0.0] * 100,
        },
        "minus_y90_gaussian_Q_wf_qp_control_c3t2": {
            "type": "arbitrary",
            "samples": [0.0, -0.0003115296978341785, -0.0006567079114946106, -0.001038002282581585, -0.0014578984013340892, -0.0019188746487076645, -0.002423373978111813, -0.0029737727232324877, -0.0035723465862234744, -0.004221234033237271, -0.004922397400563385, -0.005677582093089465, -0.0064882743357103576, -0.007355658015791834, -0.008280571228791537, -0.009263463207466856, -0.010304352375503777, -0.011402786316615695, -0.01255780448797508, -0.013767904530167772, -0.015031013032813585, -0.016344461603966336, -0.017704969061125023, -0.019108630511304812, -0.020550914016750736, -0.022026665451671725, -0.023530122044526865, -0.02505493497118679, -0.02659420121858044, -0.028140504778646134, -0.029685967061494407, -0.031222306238095, -0.032740905040366315, -0.034232886364434015, -0.03568919584541156, -0.03710069040381112, -0.038458231609060756, -0.03975278256886589, -0.04097550693830016, -0.04211786855311373, -0.04317173013083809, -0.04412944945322929, -0.04498397144607417, -0.04572891460822801, -0.04635865031094259, -0.04686837359019456, -0.047254164187077966, -0.047513036751791776] + [-0.04764297931196492] * 2 + [-0.047513036751791776, -0.047254164187077966, -0.04686837359019456, -0.04635865031094259, -0.04572891460822801, -0.04498397144607417, -0.04412944945322929, -0.04317173013083809, -0.04211786855311373, -0.04097550693830016, -0.03975278256886589, -0.038458231609060756, -0.03710069040381112, -0.03568919584541156, -0.034232886364434015, -0.032740905040366315, -0.031222306238095, -0.029685967061494407, -0.028140504778646134, -0.02659420121858044, -0.02505493497118679, -0.023530122044526865, -0.022026665451671725, -0.020550914016750736, -0.019108630511304812, -0.017704969061125023, -0.016344461603966336, -0.015031013032813585, -0.013767904530167772, -0.01255780448797508, -0.011402786316615695, -0.010304352375503777, -0.009263463207466856, -0.008280571228791537, -0.007355658015791834, -0.0064882743357103576, -0.005677582093089465, -0.004922397400563385, -0.004221234033237271, -0.0035723465862234744, -0.0029737727232324877, -0.002423373978111813, -0.0019188746487076645, -0.0014578984013340892, -0.001038002282581585, -0.0006567079114946106, -0.0003115296978341785] + [0.0] * 3,
        },
        "x180_kaiser_I_wf_qubit1": {
            "type": "arbitrary",
            "samples": [6.123359277961564e-05, 0.0002289064194538778, 0.000548783455455145, 0.0010885180985115382, 0.0019267409464745488, 0.003150008335112064, 0.004848352179230376, 0.007109572778290188, 0.010012557367687032, 0.013620038493738051, 0.01797131336312757, 0.023075514987624765, 0.02890604776283309, 0.03539676767322338, 0.042440399181746066, 0.049889541078795584, 0.05756043154530752, 0.06523943255657352, 0.07269197317209034, 0.07967347979444635, 0.08594163875116435, 0.09126920026585045, 0.09545645702431381, 0.0983425238802947] + [0.09981461034690563] * 2 + [0.0983425238802947, 0.09545645702431381, 0.09126920026585045, 0.08594163875116435, 0.07967347979444635, 0.07269197317209034, 0.06523943255657352, 0.05756043154530752, 0.049889541078795584, 0.042440399181746066, 0.03539676767322338, 0.02890604776283309, 0.023075514987624765, 0.01797131336312757, 0.013620038493738051, 0.010012557367687032, 0.007109572778290188, 0.004848352179230376, 0.003150008335112064, 0.0019267409464745488, 0.0010885180985115365, 0.0005487834554551463, 0.0002289064194538778, 6.123359277961564e-05] + [0] * 2,
        },
        "x180_kaiser_I_wf_qubit2": {
            "type": "arbitrary",
            "samples": [6.123359277961564e-05, 0.0002289064194538778, 0.000548783455455145, 0.0010885180985115382, 0.0019267409464745488, 0.003150008335112064, 0.004848352179230376, 0.007109572778290188, 0.010012557367687032, 0.013620038493738051, 0.01797131336312757, 0.023075514987624765, 0.02890604776283309, 0.03539676767322338, 0.042440399181746066, 0.049889541078795584, 0.05756043154530752, 0.06523943255657352, 0.07269197317209034, 0.07967347979444635, 0.08594163875116435, 0.09126920026585045, 0.09545645702431381, 0.0983425238802947] + [0.09981461034690563] * 2 + [0.0983425238802947, 0.09545645702431381, 0.09126920026585045, 0.08594163875116435, 0.07967347979444635, 0.07269197317209034, 0.06523943255657352, 0.05756043154530752, 0.049889541078795584, 0.042440399181746066, 0.03539676767322338, 0.02890604776283309, 0.023075514987624765, 0.01797131336312757, 0.013620038493738051, 0.010012557367687032, 0.007109572778290188, 0.004848352179230376, 0.003150008335112064, 0.0019267409464745488, 0.0010885180985115365, 0.0005487834554551463, 0.0002289064194538778, 6.123359277961564e-05] + [0] * 2,
        },
        "x180_kaiser_I_wf_qubit3": {
            "type": "arbitrary",
            "samples": [6.123359277961564e-05, 0.0002289064194538778, 0.000548783455455145, 0.0010885180985115382, 0.0019267409464745488, 0.003150008335112064, 0.004848352179230376, 0.007109572778290188, 0.010012557367687032, 0.013620038493738051, 0.01797131336312757, 0.023075514987624765, 0.02890604776283309, 0.03539676767322338, 0.042440399181746066, 0.049889541078795584, 0.05756043154530752, 0.06523943255657352, 0.07269197317209034, 0.07967347979444635, 0.08594163875116435, 0.09126920026585045, 0.09545645702431381, 0.0983425238802947] + [0.09981461034690563] * 2 + [0.0983425238802947, 0.09545645702431381, 0.09126920026585045, 0.08594163875116435, 0.07967347979444635, 0.07269197317209034, 0.06523943255657352, 0.05756043154530752, 0.049889541078795584, 0.042440399181746066, 0.03539676767322338, 0.02890604776283309, 0.023075514987624765, 0.01797131336312757, 0.013620038493738051, 0.010012557367687032, 0.007109572778290188, 0.004848352179230376, 0.003150008335112064, 0.0019267409464745488, 0.0010885180985115365, 0.0005487834554551463, 0.0002289064194538778, 6.123359277961564e-05] + [0] * 2,
        },
        "x180_kaiser_I_wf_qubit4": {
            "type": "arbitrary",
            "samples": [6.123359277961564e-05, 0.0002289064194538778, 0.000548783455455145, 0.0010885180985115382, 0.0019267409464745488, 0.003150008335112064, 0.004848352179230376, 0.007109572778290188, 0.010012557367687032, 0.013620038493738051, 0.01797131336312757, 0.023075514987624765, 0.02890604776283309, 0.03539676767322338, 0.042440399181746066, 0.049889541078795584, 0.05756043154530752, 0.06523943255657352, 0.07269197317209034, 0.07967347979444635, 0.08594163875116435, 0.09126920026585045, 0.09545645702431381, 0.0983425238802947] + [0.09981461034690563] * 2 + [0.0983425238802947, 0.09545645702431381, 0.09126920026585045, 0.08594163875116435, 0.07967347979444635, 0.07269197317209034, 0.06523943255657352, 0.05756043154530752, 0.049889541078795584, 0.042440399181746066, 0.03539676767322338, 0.02890604776283309, 0.023075514987624765, 0.01797131336312757, 0.013620038493738051, 0.010012557367687032, 0.007109572778290188, 0.004848352179230376, 0.003150008335112064, 0.0019267409464745488, 0.0010885180985115365, 0.0005487834554551463, 0.0002289064194538778, 6.123359277961564e-05] + [0] * 2,
        },
        "x180_kaiser_I_wf_qubit5": {
            "type": "arbitrary",
            "samples": [6.123359277961564e-05, 0.0002289064194538778, 0.000548783455455145, 0.0010885180985115382, 0.0019267409464745488, 0.003150008335112064, 0.004848352179230376, 0.007109572778290188, 0.010012557367687032, 0.013620038493738051, 0.01797131336312757, 0.023075514987624765, 0.02890604776283309, 0.03539676767322338, 0.042440399181746066, 0.049889541078795584, 0.05756043154530752, 0.06523943255657352, 0.07269197317209034, 0.07967347979444635, 0.08594163875116435, 0.09126920026585045, 0.09545645702431381, 0.0983425238802947] + [0.09981461034690563] * 2 + [0.0983425238802947, 0.09545645702431381, 0.09126920026585045, 0.08594163875116435, 0.07967347979444635, 0.07269197317209034, 0.06523943255657352, 0.05756043154530752, 0.049889541078795584, 0.042440399181746066, 0.03539676767322338, 0.02890604776283309, 0.023075514987624765, 0.01797131336312757, 0.013620038493738051, 0.010012557367687032, 0.007109572778290188, 0.004848352179230376, 0.003150008335112064, 0.0019267409464745488, 0.0010885180985115365, 0.0005487834554551463, 0.0002289064194538778, 6.123359277961564e-05] + [0] * 2,
        },
        "x180_kaiser_Q_wf_qubit1": {
            "type": "arbitrary",
            "samples": [0] * 52,
        },
        "x180_kaiser_Q_wf_qubit2": {
            "type": "arbitrary",
            "samples": [0] * 52,
        },
        "x180_kaiser_Q_wf_qubit3": {
            "type": "arbitrary",
            "samples": [0] * 52,
        },
        "x180_kaiser_Q_wf_qubit4": {
            "type": "arbitrary",
            "samples": [0] * 52,
        },
        "x180_kaiser_Q_wf_qubit5": {
            "type": "arbitrary",
            "samples": [0] * 52,
        },
        "x90_kaiser_I_wf_qubit1": {
            "type": "arbitrary",
            "samples": [3.061679638980782e-05, 0.0001144532097269389, 0.0002743917277275725, 0.0005442590492557691, 0.0009633704732372744, 0.001575004167556032, 0.002424176089615188, 0.003554786389145094, 0.005006278683843516, 0.006810019246869026, 0.008985656681563784, 0.011537757493812383, 0.014453023881416545, 0.01769838383661169, 0.021220199590873033, 0.024944770539397792, 0.02878021577265376, 0.03261971627828676, 0.03634598658604517, 0.039836739897223174, 0.04297081937558218, 0.045634600132925224, 0.047728228512156905, 0.04917126194014735] + [0.049907305173452814] * 2 + [0.04917126194014735, 0.047728228512156905, 0.045634600132925224, 0.04297081937558218, 0.039836739897223174, 0.03634598658604517, 0.03261971627828676, 0.02878021577265376, 0.024944770539397792, 0.021220199590873033, 0.01769838383661169, 0.014453023881416545, 0.011537757493812383, 0.008985656681563784, 0.006810019246869026, 0.005006278683843516, 0.003554786389145094, 0.002424176089615188, 0.001575004167556032, 0.0009633704732372744, 0.0005442590492557683, 0.00027439172772757316, 0.0001144532097269389, 3.061679638980782e-05] + [0] * 2,
        },
        "x90_kaiser_I_wf_qubit2": {
            "type": "arbitrary",
            "samples": [3.061679638980782e-05, 0.0001144532097269389, 0.0002743917277275725, 0.0005442590492557691, 0.0009633704732372744, 0.001575004167556032, 0.002424176089615188, 0.003554786389145094, 0.005006278683843516, 0.006810019246869026, 0.008985656681563784, 0.011537757493812383, 0.014453023881416545, 0.01769838383661169, 0.021220199590873033, 0.024944770539397792, 0.02878021577265376, 0.03261971627828676, 0.03634598658604517, 0.039836739897223174, 0.04297081937558218, 0.045634600132925224, 0.047728228512156905, 0.04917126194014735] + [0.049907305173452814] * 2 + [0.04917126194014735, 0.047728228512156905, 0.045634600132925224, 0.04297081937558218, 0.039836739897223174, 0.03634598658604517, 0.03261971627828676, 0.02878021577265376, 0.024944770539397792, 0.021220199590873033, 0.01769838383661169, 0.014453023881416545, 0.011537757493812383, 0.008985656681563784, 0.006810019246869026, 0.005006278683843516, 0.003554786389145094, 0.002424176089615188, 0.001575004167556032, 0.0009633704732372744, 0.0005442590492557683, 0.00027439172772757316, 0.0001144532097269389, 3.061679638980782e-05] + [0] * 2,
        },
        "x90_kaiser_I_wf_qubit3": {
            "type": "arbitrary",
            "samples": [3.061679638980782e-05, 0.0001144532097269389, 0.0002743917277275725, 0.0005442590492557691, 0.0009633704732372744, 0.001575004167556032, 0.002424176089615188, 0.003554786389145094, 0.005006278683843516, 0.006810019246869026, 0.008985656681563784, 0.011537757493812383, 0.014453023881416545, 0.01769838383661169, 0.021220199590873033, 0.024944770539397792, 0.02878021577265376, 0.03261971627828676, 0.03634598658604517, 0.039836739897223174, 0.04297081937558218, 0.045634600132925224, 0.047728228512156905, 0.04917126194014735] + [0.049907305173452814] * 2 + [0.04917126194014735, 0.047728228512156905, 0.045634600132925224, 0.04297081937558218, 0.039836739897223174, 0.03634598658604517, 0.03261971627828676, 0.02878021577265376, 0.024944770539397792, 0.021220199590873033, 0.01769838383661169, 0.014453023881416545, 0.011537757493812383, 0.008985656681563784, 0.006810019246869026, 0.005006278683843516, 0.003554786389145094, 0.002424176089615188, 0.001575004167556032, 0.0009633704732372744, 0.0005442590492557683, 0.00027439172772757316, 0.0001144532097269389, 3.061679638980782e-05] + [0] * 2,
        },
        "x90_kaiser_I_wf_qubit4": {
            "type": "arbitrary",
            "samples": [3.061679638980782e-05, 0.0001144532097269389, 0.0002743917277275725, 0.0005442590492557691, 0.0009633704732372744, 0.001575004167556032, 0.002424176089615188, 0.003554786389145094, 0.005006278683843516, 0.006810019246869026, 0.008985656681563784, 0.011537757493812383, 0.014453023881416545, 0.01769838383661169, 0.021220199590873033, 0.024944770539397792, 0.02878021577265376, 0.03261971627828676, 0.03634598658604517, 0.039836739897223174, 0.04297081937558218, 0.045634600132925224, 0.047728228512156905, 0.04917126194014735] + [0.049907305173452814] * 2 + [0.04917126194014735, 0.047728228512156905, 0.045634600132925224, 0.04297081937558218, 0.039836739897223174, 0.03634598658604517, 0.03261971627828676, 0.02878021577265376, 0.024944770539397792, 0.021220199590873033, 0.01769838383661169, 0.014453023881416545, 0.011537757493812383, 0.008985656681563784, 0.006810019246869026, 0.005006278683843516, 0.003554786389145094, 0.002424176089615188, 0.001575004167556032, 0.0009633704732372744, 0.0005442590492557683, 0.00027439172772757316, 0.0001144532097269389, 3.061679638980782e-05] + [0] * 2,
        },
        "x90_kaiser_I_wf_qubit5": {
            "type": "arbitrary",
            "samples": [3.061679638980782e-05, 0.0001144532097269389, 0.0002743917277275725, 0.0005442590492557691, 0.0009633704732372744, 0.001575004167556032, 0.002424176089615188, 0.003554786389145094, 0.005006278683843516, 0.006810019246869026, 0.008985656681563784, 0.011537757493812383, 0.014453023881416545, 0.01769838383661169, 0.021220199590873033, 0.024944770539397792, 0.02878021577265376, 0.03261971627828676, 0.03634598658604517, 0.039836739897223174, 0.04297081937558218, 0.045634600132925224, 0.047728228512156905, 0.04917126194014735] + [0.049907305173452814] * 2 + [0.04917126194014735, 0.047728228512156905, 0.045634600132925224, 0.04297081937558218, 0.039836739897223174, 0.03634598658604517, 0.03261971627828676, 0.02878021577265376, 0.024944770539397792, 0.021220199590873033, 0.01769838383661169, 0.014453023881416545, 0.011537757493812383, 0.008985656681563784, 0.006810019246869026, 0.005006278683843516, 0.003554786389145094, 0.002424176089615188, 0.001575004167556032, 0.0009633704732372744, 0.0005442590492557683, 0.00027439172772757316, 0.0001144532097269389, 3.061679638980782e-05] + [0] * 2,
        },
        "x90_kaiser_Q_wf_qubit1": {
            "type": "arbitrary",
            "samples": [0] * 52,
        },
        "x90_kaiser_Q_wf_qubit2": {
            "type": "arbitrary",
            "samples": [0] * 52,
        },
        "x90_kaiser_Q_wf_qubit3": {
            "type": "arbitrary",
            "samples": [0] * 52,
        },
        "x90_kaiser_Q_wf_qubit4": {
            "type": "arbitrary",
            "samples": [0] * 52,
        },
        "x90_kaiser_Q_wf_qubit5": {
            "type": "arbitrary",
            "samples": [0] * 52,
        },
        "minus_x90_kaiser_I_wf_qubit1": {
            "type": "arbitrary",
            "samples": [-3.061679638980782e-05, -0.0001144532097269389, -0.0002743917277275725, -0.0005442590492557691, -0.0009633704732372744, -0.001575004167556032, -0.002424176089615188, -0.003554786389145094, -0.005006278683843516, -0.006810019246869026, -0.008985656681563784, -0.011537757493812383, -0.014453023881416545, -0.01769838383661169, -0.021220199590873033, -0.024944770539397792, -0.02878021577265376, -0.03261971627828676, -0.03634598658604517, -0.039836739897223174, -0.04297081937558218, -0.045634600132925224, -0.047728228512156905, -0.04917126194014735] + [-0.049907305173452814] * 2 + [-0.04917126194014735, -0.047728228512156905, -0.045634600132925224, -0.04297081937558218, -0.039836739897223174, -0.03634598658604517, -0.03261971627828676, -0.02878021577265376, -0.024944770539397792, -0.021220199590873033, -0.01769838383661169, -0.014453023881416545, -0.011537757493812383, -0.008985656681563784, -0.006810019246869026, -0.005006278683843516, -0.003554786389145094, -0.002424176089615188, -0.001575004167556032, -0.0009633704732372744, -0.0005442590492557683, -0.00027439172772757316, -0.0001144532097269389, -3.061679638980782e-05] + [0] * 2,
        },
        "minus_x90_kaiser_I_wf_qubit2": {
            "type": "arbitrary",
            "samples": [-3.061679638980782e-05, -0.0001144532097269389, -0.0002743917277275725, -0.0005442590492557691, -0.0009633704732372744, -0.001575004167556032, -0.002424176089615188, -0.003554786389145094, -0.005006278683843516, -0.006810019246869026, -0.008985656681563784, -0.011537757493812383, -0.014453023881416545, -0.01769838383661169, -0.021220199590873033, -0.024944770539397792, -0.02878021577265376, -0.03261971627828676, -0.03634598658604517, -0.039836739897223174, -0.04297081937558218, -0.045634600132925224, -0.047728228512156905, -0.04917126194014735] + [-0.049907305173452814] * 2 + [-0.04917126194014735, -0.047728228512156905, -0.045634600132925224, -0.04297081937558218, -0.039836739897223174, -0.03634598658604517, -0.03261971627828676, -0.02878021577265376, -0.024944770539397792, -0.021220199590873033, -0.01769838383661169, -0.014453023881416545, -0.011537757493812383, -0.008985656681563784, -0.006810019246869026, -0.005006278683843516, -0.003554786389145094, -0.002424176089615188, -0.001575004167556032, -0.0009633704732372744, -0.0005442590492557683, -0.00027439172772757316, -0.0001144532097269389, -3.061679638980782e-05] + [0] * 2,
        },
        "minus_x90_kaiser_I_wf_qubit3": {
            "type": "arbitrary",
            "samples": [-3.061679638980782e-05, -0.0001144532097269389, -0.0002743917277275725, -0.0005442590492557691, -0.0009633704732372744, -0.001575004167556032, -0.002424176089615188, -0.003554786389145094, -0.005006278683843516, -0.006810019246869026, -0.008985656681563784, -0.011537757493812383, -0.014453023881416545, -0.01769838383661169, -0.021220199590873033, -0.024944770539397792, -0.02878021577265376, -0.03261971627828676, -0.03634598658604517, -0.039836739897223174, -0.04297081937558218, -0.045634600132925224, -0.047728228512156905, -0.04917126194014735] + [-0.049907305173452814] * 2 + [-0.04917126194014735, -0.047728228512156905, -0.045634600132925224, -0.04297081937558218, -0.039836739897223174, -0.03634598658604517, -0.03261971627828676, -0.02878021577265376, -0.024944770539397792, -0.021220199590873033, -0.01769838383661169, -0.014453023881416545, -0.011537757493812383, -0.008985656681563784, -0.006810019246869026, -0.005006278683843516, -0.003554786389145094, -0.002424176089615188, -0.001575004167556032, -0.0009633704732372744, -0.0005442590492557683, -0.00027439172772757316, -0.0001144532097269389, -3.061679638980782e-05] + [0] * 2,
        },
        "minus_x90_kaiser_I_wf_qubit4": {
            "type": "arbitrary",
            "samples": [-3.061679638980782e-05, -0.0001144532097269389, -0.0002743917277275725, -0.0005442590492557691, -0.0009633704732372744, -0.001575004167556032, -0.002424176089615188, -0.003554786389145094, -0.005006278683843516, -0.006810019246869026, -0.008985656681563784, -0.011537757493812383, -0.014453023881416545, -0.01769838383661169, -0.021220199590873033, -0.024944770539397792, -0.02878021577265376, -0.03261971627828676, -0.03634598658604517, -0.039836739897223174, -0.04297081937558218, -0.045634600132925224, -0.047728228512156905, -0.04917126194014735] + [-0.049907305173452814] * 2 + [-0.04917126194014735, -0.047728228512156905, -0.045634600132925224, -0.04297081937558218, -0.039836739897223174, -0.03634598658604517, -0.03261971627828676, -0.02878021577265376, -0.024944770539397792, -0.021220199590873033, -0.01769838383661169, -0.014453023881416545, -0.011537757493812383, -0.008985656681563784, -0.006810019246869026, -0.005006278683843516, -0.003554786389145094, -0.002424176089615188, -0.001575004167556032, -0.0009633704732372744, -0.0005442590492557683, -0.00027439172772757316, -0.0001144532097269389, -3.061679638980782e-05] + [0] * 2,
        },
        "minus_x90_kaiser_I_wf_qubit5": {
            "type": "arbitrary",
            "samples": [-3.061679638980782e-05, -0.0001144532097269389, -0.0002743917277275725, -0.0005442590492557691, -0.0009633704732372744, -0.001575004167556032, -0.002424176089615188, -0.003554786389145094, -0.005006278683843516, -0.006810019246869026, -0.008985656681563784, -0.011537757493812383, -0.014453023881416545, -0.01769838383661169, -0.021220199590873033, -0.024944770539397792, -0.02878021577265376, -0.03261971627828676, -0.03634598658604517, -0.039836739897223174, -0.04297081937558218, -0.045634600132925224, -0.047728228512156905, -0.04917126194014735] + [-0.049907305173452814] * 2 + [-0.04917126194014735, -0.047728228512156905, -0.045634600132925224, -0.04297081937558218, -0.039836739897223174, -0.03634598658604517, -0.03261971627828676, -0.02878021577265376, -0.024944770539397792, -0.021220199590873033, -0.01769838383661169, -0.014453023881416545, -0.011537757493812383, -0.008985656681563784, -0.006810019246869026, -0.005006278683843516, -0.003554786389145094, -0.002424176089615188, -0.001575004167556032, -0.0009633704732372744, -0.0005442590492557683, -0.00027439172772757316, -0.0001144532097269389, -3.061679638980782e-05] + [0] * 2,
        },
        "minus_x90_kaiser_Q_wf_qubit1": {
            "type": "arbitrary",
            "samples": [0] * 52,
        },
        "minus_x90_kaiser_Q_wf_qubit2": {
            "type": "arbitrary",
            "samples": [0] * 52,
        },
        "minus_x90_kaiser_Q_wf_qubit3": {
            "type": "arbitrary",
            "samples": [0] * 52,
        },
        "minus_x90_kaiser_Q_wf_qubit4": {
            "type": "arbitrary",
            "samples": [0] * 52,
        },
        "minus_x90_kaiser_Q_wf_qubit5": {
            "type": "arbitrary",
            "samples": [0] * 52,
        },
        "y180_kaiser_I_wf_qubit1": {
            "type": "arbitrary",
            "samples": [0] * 52,
        },
        "y180_kaiser_I_wf_qubit2": {
            "type": "arbitrary",
            "samples": [0] * 52,
        },
        "y180_kaiser_I_wf_qubit3": {
            "type": "arbitrary",
            "samples": [0] * 52,
        },
        "y180_kaiser_I_wf_qubit4": {
            "type": "arbitrary",
            "samples": [0] * 52,
        },
        "y180_kaiser_I_wf_qubit5": {
            "type": "arbitrary",
            "samples": [0] * 52,
        },
        "y180_kaiser_Q_wf_qubit1": {
            "type": "arbitrary",
            "samples": [6.123359277961564e-05, 0.0002289064194538778, 0.000548783455455145, 0.0010885180985115382, 0.0019267409464745488, 0.003150008335112064, 0.004848352179230376, 0.007109572778290188, 0.010012557367687032, 0.013620038493738051, 0.01797131336312757, 0.023075514987624765, 0.02890604776283309, 0.03539676767322338, 0.042440399181746066, 0.049889541078795584, 0.05756043154530752, 0.06523943255657352, 0.07269197317209034, 0.07967347979444635, 0.08594163875116435, 0.09126920026585045, 0.09545645702431381, 0.0983425238802947] + [0.09981461034690563] * 2 + [0.0983425238802947, 0.09545645702431381, 0.09126920026585045, 0.08594163875116435, 0.07967347979444635, 0.07269197317209034, 0.06523943255657352, 0.05756043154530752, 0.049889541078795584, 0.042440399181746066, 0.03539676767322338, 0.02890604776283309, 0.023075514987624765, 0.01797131336312757, 0.013620038493738051, 0.010012557367687032, 0.007109572778290188, 0.004848352179230376, 0.003150008335112064, 0.0019267409464745488, 0.0010885180985115365, 0.0005487834554551463, 0.0002289064194538778, 6.123359277961564e-05] + [0] * 2,
        },
        "y180_kaiser_Q_wf_qubit2": {
            "type": "arbitrary",
            "samples": [6.123359277961564e-05, 0.0002289064194538778, 0.000548783455455145, 0.0010885180985115382, 0.0019267409464745488, 0.003150008335112064, 0.004848352179230376, 0.007109572778290188, 0.010012557367687032, 0.013620038493738051, 0.01797131336312757, 0.023075514987624765, 0.02890604776283309, 0.03539676767322338, 0.042440399181746066, 0.049889541078795584, 0.05756043154530752, 0.06523943255657352, 0.07269197317209034, 0.07967347979444635, 0.08594163875116435, 0.09126920026585045, 0.09545645702431381, 0.0983425238802947] + [0.09981461034690563] * 2 + [0.0983425238802947, 0.09545645702431381, 0.09126920026585045, 0.08594163875116435, 0.07967347979444635, 0.07269197317209034, 0.06523943255657352, 0.05756043154530752, 0.049889541078795584, 0.042440399181746066, 0.03539676767322338, 0.02890604776283309, 0.023075514987624765, 0.01797131336312757, 0.013620038493738051, 0.010012557367687032, 0.007109572778290188, 0.004848352179230376, 0.003150008335112064, 0.0019267409464745488, 0.0010885180985115365, 0.0005487834554551463, 0.0002289064194538778, 6.123359277961564e-05] + [0] * 2,
        },
        "y180_kaiser_Q_wf_qubit3": {
            "type": "arbitrary",
            "samples": [6.123359277961564e-05, 0.0002289064194538778, 0.000548783455455145, 0.0010885180985115382, 0.0019267409464745488, 0.003150008335112064, 0.004848352179230376, 0.007109572778290188, 0.010012557367687032, 0.013620038493738051, 0.01797131336312757, 0.023075514987624765, 0.02890604776283309, 0.03539676767322338, 0.042440399181746066, 0.049889541078795584, 0.05756043154530752, 0.06523943255657352, 0.07269197317209034, 0.07967347979444635, 0.08594163875116435, 0.09126920026585045, 0.09545645702431381, 0.0983425238802947] + [0.09981461034690563] * 2 + [0.0983425238802947, 0.09545645702431381, 0.09126920026585045, 0.08594163875116435, 0.07967347979444635, 0.07269197317209034, 0.06523943255657352, 0.05756043154530752, 0.049889541078795584, 0.042440399181746066, 0.03539676767322338, 0.02890604776283309, 0.023075514987624765, 0.01797131336312757, 0.013620038493738051, 0.010012557367687032, 0.007109572778290188, 0.004848352179230376, 0.003150008335112064, 0.0019267409464745488, 0.0010885180985115365, 0.0005487834554551463, 0.0002289064194538778, 6.123359277961564e-05] + [0] * 2,
        },
        "y180_kaiser_Q_wf_qubit4": {
            "type": "arbitrary",
            "samples": [6.123359277961564e-05, 0.0002289064194538778, 0.000548783455455145, 0.0010885180985115382, 0.0019267409464745488, 0.003150008335112064, 0.004848352179230376, 0.007109572778290188, 0.010012557367687032, 0.013620038493738051, 0.01797131336312757, 0.023075514987624765, 0.02890604776283309, 0.03539676767322338, 0.042440399181746066, 0.049889541078795584, 0.05756043154530752, 0.06523943255657352, 0.07269197317209034, 0.07967347979444635, 0.08594163875116435, 0.09126920026585045, 0.09545645702431381, 0.0983425238802947] + [0.09981461034690563] * 2 + [0.0983425238802947, 0.09545645702431381, 0.09126920026585045, 0.08594163875116435, 0.07967347979444635, 0.07269197317209034, 0.06523943255657352, 0.05756043154530752, 0.049889541078795584, 0.042440399181746066, 0.03539676767322338, 0.02890604776283309, 0.023075514987624765, 0.01797131336312757, 0.013620038493738051, 0.010012557367687032, 0.007109572778290188, 0.004848352179230376, 0.003150008335112064, 0.0019267409464745488, 0.0010885180985115365, 0.0005487834554551463, 0.0002289064194538778, 6.123359277961564e-05] + [0] * 2,
        },
        "y180_kaiser_Q_wf_qubit5": {
            "type": "arbitrary",
            "samples": [6.123359277961564e-05, 0.0002289064194538778, 0.000548783455455145, 0.0010885180985115382, 0.0019267409464745488, 0.003150008335112064, 0.004848352179230376, 0.007109572778290188, 0.010012557367687032, 0.013620038493738051, 0.01797131336312757, 0.023075514987624765, 0.02890604776283309, 0.03539676767322338, 0.042440399181746066, 0.049889541078795584, 0.05756043154530752, 0.06523943255657352, 0.07269197317209034, 0.07967347979444635, 0.08594163875116435, 0.09126920026585045, 0.09545645702431381, 0.0983425238802947] + [0.09981461034690563] * 2 + [0.0983425238802947, 0.09545645702431381, 0.09126920026585045, 0.08594163875116435, 0.07967347979444635, 0.07269197317209034, 0.06523943255657352, 0.05756043154530752, 0.049889541078795584, 0.042440399181746066, 0.03539676767322338, 0.02890604776283309, 0.023075514987624765, 0.01797131336312757, 0.013620038493738051, 0.010012557367687032, 0.007109572778290188, 0.004848352179230376, 0.003150008335112064, 0.0019267409464745488, 0.0010885180985115365, 0.0005487834554551463, 0.0002289064194538778, 6.123359277961564e-05] + [0] * 2,
        },
        "y90_kaiser_I_wf_qubit1": {
            "type": "arbitrary",
            "samples": [0] * 52,
        },
        "y90_kaiser_I_wf_qubit2": {
            "type": "arbitrary",
            "samples": [0] * 52,
        },
        "y90_kaiser_I_wf_qubit3": {
            "type": "arbitrary",
            "samples": [0] * 52,
        },
        "y90_kaiser_I_wf_qubit4": {
            "type": "arbitrary",
            "samples": [0] * 52,
        },
        "y90_kaiser_I_wf_qubit5": {
            "type": "arbitrary",
            "samples": [0] * 52,
        },
        "y90_kaiser_Q_wf_qubit1": {
            "type": "arbitrary",
            "samples": [3.061679638980782e-05, 0.0001144532097269389, 0.0002743917277275725, 0.0005442590492557691, 0.0009633704732372744, 0.001575004167556032, 0.002424176089615188, 0.003554786389145094, 0.005006278683843516, 0.006810019246869026, 0.008985656681563784, 0.011537757493812383, 0.014453023881416545, 0.01769838383661169, 0.021220199590873033, 0.024944770539397792, 0.02878021577265376, 0.03261971627828676, 0.03634598658604517, 0.039836739897223174, 0.04297081937558218, 0.045634600132925224, 0.047728228512156905, 0.04917126194014735] + [0.049907305173452814] * 2 + [0.04917126194014735, 0.047728228512156905, 0.045634600132925224, 0.04297081937558218, 0.039836739897223174, 0.03634598658604517, 0.03261971627828676, 0.02878021577265376, 0.024944770539397792, 0.021220199590873033, 0.01769838383661169, 0.014453023881416545, 0.011537757493812383, 0.008985656681563784, 0.006810019246869026, 0.005006278683843516, 0.003554786389145094, 0.002424176089615188, 0.001575004167556032, 0.0009633704732372744, 0.0005442590492557683, 0.00027439172772757316, 0.0001144532097269389, 3.061679638980782e-05] + [0] * 2,
        },
        "y90_kaiser_Q_wf_qubit2": {
            "type": "arbitrary",
            "samples": [3.061679638980782e-05, 0.0001144532097269389, 0.0002743917277275725, 0.0005442590492557691, 0.0009633704732372744, 0.001575004167556032, 0.002424176089615188, 0.003554786389145094, 0.005006278683843516, 0.006810019246869026, 0.008985656681563784, 0.011537757493812383, 0.014453023881416545, 0.01769838383661169, 0.021220199590873033, 0.024944770539397792, 0.02878021577265376, 0.03261971627828676, 0.03634598658604517, 0.039836739897223174, 0.04297081937558218, 0.045634600132925224, 0.047728228512156905, 0.04917126194014735] + [0.049907305173452814] * 2 + [0.04917126194014735, 0.047728228512156905, 0.045634600132925224, 0.04297081937558218, 0.039836739897223174, 0.03634598658604517, 0.03261971627828676, 0.02878021577265376, 0.024944770539397792, 0.021220199590873033, 0.01769838383661169, 0.014453023881416545, 0.011537757493812383, 0.008985656681563784, 0.006810019246869026, 0.005006278683843516, 0.003554786389145094, 0.002424176089615188, 0.001575004167556032, 0.0009633704732372744, 0.0005442590492557683, 0.00027439172772757316, 0.0001144532097269389, 3.061679638980782e-05] + [0] * 2,
        },
        "y90_kaiser_Q_wf_qubit3": {
            "type": "arbitrary",
            "samples": [3.061679638980782e-05, 0.0001144532097269389, 0.0002743917277275725, 0.0005442590492557691, 0.0009633704732372744, 0.001575004167556032, 0.002424176089615188, 0.003554786389145094, 0.005006278683843516, 0.006810019246869026, 0.008985656681563784, 0.011537757493812383, 0.014453023881416545, 0.01769838383661169, 0.021220199590873033, 0.024944770539397792, 0.02878021577265376, 0.03261971627828676, 0.03634598658604517, 0.039836739897223174, 0.04297081937558218, 0.045634600132925224, 0.047728228512156905, 0.04917126194014735] + [0.049907305173452814] * 2 + [0.04917126194014735, 0.047728228512156905, 0.045634600132925224, 0.04297081937558218, 0.039836739897223174, 0.03634598658604517, 0.03261971627828676, 0.02878021577265376, 0.024944770539397792, 0.021220199590873033, 0.01769838383661169, 0.014453023881416545, 0.011537757493812383, 0.008985656681563784, 0.006810019246869026, 0.005006278683843516, 0.003554786389145094, 0.002424176089615188, 0.001575004167556032, 0.0009633704732372744, 0.0005442590492557683, 0.00027439172772757316, 0.0001144532097269389, 3.061679638980782e-05] + [0] * 2,
        },
        "y90_kaiser_Q_wf_qubit4": {
            "type": "arbitrary",
            "samples": [3.061679638980782e-05, 0.0001144532097269389, 0.0002743917277275725, 0.0005442590492557691, 0.0009633704732372744, 0.001575004167556032, 0.002424176089615188, 0.003554786389145094, 0.005006278683843516, 0.006810019246869026, 0.008985656681563784, 0.011537757493812383, 0.014453023881416545, 0.01769838383661169, 0.021220199590873033, 0.024944770539397792, 0.02878021577265376, 0.03261971627828676, 0.03634598658604517, 0.039836739897223174, 0.04297081937558218, 0.045634600132925224, 0.047728228512156905, 0.04917126194014735] + [0.049907305173452814] * 2 + [0.04917126194014735, 0.047728228512156905, 0.045634600132925224, 0.04297081937558218, 0.039836739897223174, 0.03634598658604517, 0.03261971627828676, 0.02878021577265376, 0.024944770539397792, 0.021220199590873033, 0.01769838383661169, 0.014453023881416545, 0.011537757493812383, 0.008985656681563784, 0.006810019246869026, 0.005006278683843516, 0.003554786389145094, 0.002424176089615188, 0.001575004167556032, 0.0009633704732372744, 0.0005442590492557683, 0.00027439172772757316, 0.0001144532097269389, 3.061679638980782e-05] + [0] * 2,
        },
        "y90_kaiser_Q_wf_qubit5": {
            "type": "arbitrary",
            "samples": [3.061679638980782e-05, 0.0001144532097269389, 0.0002743917277275725, 0.0005442590492557691, 0.0009633704732372744, 0.001575004167556032, 0.002424176089615188, 0.003554786389145094, 0.005006278683843516, 0.006810019246869026, 0.008985656681563784, 0.011537757493812383, 0.014453023881416545, 0.01769838383661169, 0.021220199590873033, 0.024944770539397792, 0.02878021577265376, 0.03261971627828676, 0.03634598658604517, 0.039836739897223174, 0.04297081937558218, 0.045634600132925224, 0.047728228512156905, 0.04917126194014735] + [0.049907305173452814] * 2 + [0.04917126194014735, 0.047728228512156905, 0.045634600132925224, 0.04297081937558218, 0.039836739897223174, 0.03634598658604517, 0.03261971627828676, 0.02878021577265376, 0.024944770539397792, 0.021220199590873033, 0.01769838383661169, 0.014453023881416545, 0.011537757493812383, 0.008985656681563784, 0.006810019246869026, 0.005006278683843516, 0.003554786389145094, 0.002424176089615188, 0.001575004167556032, 0.0009633704732372744, 0.0005442590492557683, 0.00027439172772757316, 0.0001144532097269389, 3.061679638980782e-05] + [0] * 2,
        },
        "minus_y90_kaiser_I_wf_qubit1": {
            "type": "arbitrary",
            "samples": [0] * 52,
        },
        "minus_y90_kaiser_I_wf_qubit2": {
            "type": "arbitrary",
            "samples": [0] * 52,
        },
        "minus_y90_kaiser_I_wf_qubit3": {
            "type": "arbitrary",
            "samples": [0] * 52,
        },
        "minus_y90_kaiser_I_wf_qubit4": {
            "type": "arbitrary",
            "samples": [0] * 52,
        },
        "minus_y90_kaiser_I_wf_qubit5": {
            "type": "arbitrary",
            "samples": [0] * 52,
        },
        "minus_y90_kaiser_Q_wf_qubit1": {
            "type": "arbitrary",
            "samples": [-3.061679638980782e-05, -0.0001144532097269389, -0.0002743917277275725, -0.0005442590492557691, -0.0009633704732372744, -0.001575004167556032, -0.002424176089615188, -0.003554786389145094, -0.005006278683843516, -0.006810019246869026, -0.008985656681563784, -0.011537757493812383, -0.014453023881416545, -0.01769838383661169, -0.021220199590873033, -0.024944770539397792, -0.02878021577265376, -0.03261971627828676, -0.03634598658604517, -0.039836739897223174, -0.04297081937558218, -0.045634600132925224, -0.047728228512156905, -0.04917126194014735] + [-0.049907305173452814] * 2 + [-0.04917126194014735, -0.047728228512156905, -0.045634600132925224, -0.04297081937558218, -0.039836739897223174, -0.03634598658604517, -0.03261971627828676, -0.02878021577265376, -0.024944770539397792, -0.021220199590873033, -0.01769838383661169, -0.014453023881416545, -0.011537757493812383, -0.008985656681563784, -0.006810019246869026, -0.005006278683843516, -0.003554786389145094, -0.002424176089615188, -0.001575004167556032, -0.0009633704732372744, -0.0005442590492557683, -0.00027439172772757316, -0.0001144532097269389, -3.061679638980782e-05] + [0] * 2,
        },
        "minus_y90_kaiser_Q_wf_qubit2": {
            "type": "arbitrary",
            "samples": [-3.061679638980782e-05, -0.0001144532097269389, -0.0002743917277275725, -0.0005442590492557691, -0.0009633704732372744, -0.001575004167556032, -0.002424176089615188, -0.003554786389145094, -0.005006278683843516, -0.006810019246869026, -0.008985656681563784, -0.011537757493812383, -0.014453023881416545, -0.01769838383661169, -0.021220199590873033, -0.024944770539397792, -0.02878021577265376, -0.03261971627828676, -0.03634598658604517, -0.039836739897223174, -0.04297081937558218, -0.045634600132925224, -0.047728228512156905, -0.04917126194014735] + [-0.049907305173452814] * 2 + [-0.04917126194014735, -0.047728228512156905, -0.045634600132925224, -0.04297081937558218, -0.039836739897223174, -0.03634598658604517, -0.03261971627828676, -0.02878021577265376, -0.024944770539397792, -0.021220199590873033, -0.01769838383661169, -0.014453023881416545, -0.011537757493812383, -0.008985656681563784, -0.006810019246869026, -0.005006278683843516, -0.003554786389145094, -0.002424176089615188, -0.001575004167556032, -0.0009633704732372744, -0.0005442590492557683, -0.00027439172772757316, -0.0001144532097269389, -3.061679638980782e-05] + [0] * 2,
        },
        "minus_y90_kaiser_Q_wf_qubit3": {
            "type": "arbitrary",
            "samples": [-3.061679638980782e-05, -0.0001144532097269389, -0.0002743917277275725, -0.0005442590492557691, -0.0009633704732372744, -0.001575004167556032, -0.002424176089615188, -0.003554786389145094, -0.005006278683843516, -0.006810019246869026, -0.008985656681563784, -0.011537757493812383, -0.014453023881416545, -0.01769838383661169, -0.021220199590873033, -0.024944770539397792, -0.02878021577265376, -0.03261971627828676, -0.03634598658604517, -0.039836739897223174, -0.04297081937558218, -0.045634600132925224, -0.047728228512156905, -0.04917126194014735] + [-0.049907305173452814] * 2 + [-0.04917126194014735, -0.047728228512156905, -0.045634600132925224, -0.04297081937558218, -0.039836739897223174, -0.03634598658604517, -0.03261971627828676, -0.02878021577265376, -0.024944770539397792, -0.021220199590873033, -0.01769838383661169, -0.014453023881416545, -0.011537757493812383, -0.008985656681563784, -0.006810019246869026, -0.005006278683843516, -0.003554786389145094, -0.002424176089615188, -0.001575004167556032, -0.0009633704732372744, -0.0005442590492557683, -0.00027439172772757316, -0.0001144532097269389, -3.061679638980782e-05] + [0] * 2,
        },
        "minus_y90_kaiser_Q_wf_qubit4": {
            "type": "arbitrary",
            "samples": [-3.061679638980782e-05, -0.0001144532097269389, -0.0002743917277275725, -0.0005442590492557691, -0.0009633704732372744, -0.001575004167556032, -0.002424176089615188, -0.003554786389145094, -0.005006278683843516, -0.006810019246869026, -0.008985656681563784, -0.011537757493812383, -0.014453023881416545, -0.01769838383661169, -0.021220199590873033, -0.024944770539397792, -0.02878021577265376, -0.03261971627828676, -0.03634598658604517, -0.039836739897223174, -0.04297081937558218, -0.045634600132925224, -0.047728228512156905, -0.04917126194014735] + [-0.049907305173452814] * 2 + [-0.04917126194014735, -0.047728228512156905, -0.045634600132925224, -0.04297081937558218, -0.039836739897223174, -0.03634598658604517, -0.03261971627828676, -0.02878021577265376, -0.024944770539397792, -0.021220199590873033, -0.01769838383661169, -0.014453023881416545, -0.011537757493812383, -0.008985656681563784, -0.006810019246869026, -0.005006278683843516, -0.003554786389145094, -0.002424176089615188, -0.001575004167556032, -0.0009633704732372744, -0.0005442590492557683, -0.00027439172772757316, -0.0001144532097269389, -3.061679638980782e-05] + [0] * 2,
        },
        "minus_y90_kaiser_Q_wf_qubit5": {
            "type": "arbitrary",
            "samples": [-3.061679638980782e-05, -0.0001144532097269389, -0.0002743917277275725, -0.0005442590492557691, -0.0009633704732372744, -0.001575004167556032, -0.002424176089615188, -0.003554786389145094, -0.005006278683843516, -0.006810019246869026, -0.008985656681563784, -0.011537757493812383, -0.014453023881416545, -0.01769838383661169, -0.021220199590873033, -0.024944770539397792, -0.02878021577265376, -0.03261971627828676, -0.03634598658604517, -0.039836739897223174, -0.04297081937558218, -0.045634600132925224, -0.047728228512156905, -0.04917126194014735] + [-0.049907305173452814] * 2 + [-0.04917126194014735, -0.047728228512156905, -0.045634600132925224, -0.04297081937558218, -0.039836739897223174, -0.03634598658604517, -0.03261971627828676, -0.02878021577265376, -0.024944770539397792, -0.021220199590873033, -0.01769838383661169, -0.014453023881416545, -0.011537757493812383, -0.008985656681563784, -0.006810019246869026, -0.005006278683843516, -0.003554786389145094, -0.002424176089615188, -0.001575004167556032, -0.0009633704732372744, -0.0005442590492557683, -0.00027439172772757316, -0.0001144532097269389, -3.061679638980782e-05] + [0] * 2,
        },
        "x180_kaiser_I_wf_qp_control_c3t2": {
            "type": "arbitrary",
            "samples": [6.123359277961564e-05, 0.0001306438144712879, 0.00023132187674409848, 0.0003707991780740096, 0.0005574391218594114, 0.0008003941708179544, 0.0011095399428924942, 0.0014953855867247238, 0.0019689601966731024, 0.0025416755920456883, 0.003225166380287162, 0.0040311088354394045, 0.0049710207362835285, 0.006056044907394079, 0.007296719774748082, 0.008702740769447388, 0.010282716872948027, 0.012043926980302464, 0.01399208105104621, 0.016131091209017425, 0.018462858033262076, 0.020987077245404648, 0.023701071840357107, 0.026599654425844745, 0.02967502413386515, 0.03291670194889541, 0.03631150767153205, 0.03984358101334329, 0.04349444851284272, 0.04724313708992553, 0.051066334135211805, 0.054938593081588605, 0.05883258244909391, 0.06271937541311469, 0.06656877604179862, 0.0703496775033089, 0.07403044677783581, 0.07757932974235295, 0.08096486994518408, 0.08415633396728084, 0.08712413598952014, 0.089840254058968, 0.09227863057700843, 0.09441554972003091, 0.09622998484670547, 0.09770390943881668, 0.09882256575559714, 0.09957468614155682] + [0.09995266279888454] * 2 + [0.09957468614155682, 0.09882256575559714, 0.09770390943881668, 0.09622998484670547, 0.09441554972003091, 0.09227863057700843, 0.089840254058968, 0.08712413598952014, 0.08415633396728084, 0.0809648699451842, 0.07757932974235295, 0.07403044677783581, 0.0703496775033089, 0.06656877604179862, 0.06271937541311469, 0.05883258244909391, 0.054938593081588605, 0.051066334135211805, 0.04724313708992561, 0.04349444851284272, 0.03984358101334329, 0.036311507671532114, 0.03291670194889541, 0.02967502413386515, 0.026599654425844745, 0.023701071840357107, 0.020987077245404648, 0.018462858033262076, 0.016131091209017425, 0.01399208105104621, 0.012043926980302464, 0.010282716872948027, 0.008702740769447388, 0.007296719774748089, 0.006056044907394079, 0.0049710207362835285, 0.004031108835439411, 0.003225166380287162, 0.0025416755920456883, 0.001968960196673105, 0.0014953855867247238, 0.0011095399428924942, 0.0008003941708179558, 0.00055743912185941, 0.0003707991780740096, 0.00023132187674409872, 0.00013064381447128748, 6.123359277961564e-05] + [0] * 2,
        },
        "x180_kaiser_Q_wf_qp_control_c3t2": {
            "type": "arbitrary",
            "samples": [0] * 100,
        },
        "x90_kaiser_I_wf_qp_control_c3t2": {
            "type": "arbitrary",
            "samples": [3.061679638980782e-05, 6.532190723564394e-05, 0.00011566093837204924, 0.0001853995890370048, 0.0002787195609297057, 0.0004001970854089772, 0.0005547699714462471, 0.0007476927933623619, 0.0009844800983365512, 0.0012708377960228441, 0.001612583190143581, 0.0020155544177197023, 0.0024855103681417643, 0.0030280224536970396, 0.003648359887374041, 0.004351370384723694, 0.005141358436474014, 0.006021963490151232, 0.006996040525523105, 0.008065545604508713, 0.009231429016631038, 0.010493538622702324, 0.011850535920178554, 0.013299827212922373, 0.014837512066932575, 0.016458350974447707, 0.018155753835766026, 0.019921790506671644, 0.02174722425642136, 0.023621568544962765, 0.025533167067605902, 0.027469296540794302, 0.029416291224546955, 0.031359687706557345, 0.03328438802089931, 0.03517483875165445, 0.037015223388917905, 0.03878966487117647, 0.04048243497259204, 0.04207816698364042, 0.04356206799476007, 0.044920127029484, 0.046139315288504214, 0.047207774860015456, 0.04811499242335274, 0.04885195471940834, 0.04941128287779857, 0.04978734307077841] + [0.04997633139944227] * 2 + [0.04978734307077841, 0.04941128287779857, 0.04885195471940834, 0.04811499242335274, 0.047207774860015456, 0.046139315288504214, 0.044920127029484, 0.04356206799476007, 0.04207816698364042, 0.0404824349725921, 0.03878966487117647, 0.037015223388917905, 0.03517483875165445, 0.03328438802089931, 0.031359687706557345, 0.029416291224546955, 0.027469296540794302, 0.025533167067605902, 0.023621568544962807, 0.02174722425642136, 0.019921790506671644, 0.018155753835766057, 0.016458350974447707, 0.014837512066932575, 0.013299827212922373, 0.011850535920178554, 0.010493538622702324, 0.009231429016631038, 0.008065545604508713, 0.006996040525523105, 0.006021963490151232, 0.005141358436474014, 0.004351370384723694, 0.0036483598873740444, 0.0030280224536970396, 0.0024855103681417643, 0.0020155544177197053, 0.001612583190143581, 0.0012708377960228441, 0.0009844800983365525, 0.0007476927933623619, 0.0005547699714462471, 0.0004001970854089779, 0.000278719560929705, 0.0001853995890370048, 0.00011566093837204936, 6.532190723564374e-05, 3.061679638980782e-05] + [0] * 2,
        },
        "x90_kaiser_Q_wf_qp_control_c3t2": {
            "type": "arbitrary",
            "samples": [0] * 100,
        },
        "minus_x90_kaiser_I_wf_qp_control_c3t2": {
            "type": "arbitrary",
            "samples": [-3.061679638980782e-05, -6.532190723564394e-05, -0.00011566093837204924, -0.0001853995890370048, -0.0002787195609297057, -0.0004001970854089772, -0.0005547699714462471, -0.0007476927933623619, -0.0009844800983365512, -0.0012708377960228441, -0.001612583190143581, -0.0020155544177197023, -0.0024855103681417643, -0.0030280224536970396, -0.003648359887374041, -0.004351370384723694, -0.005141358436474014, -0.006021963490151232, -0.006996040525523105, -0.008065545604508713, -0.009231429016631038, -0.010493538622702324, -0.011850535920178554, -0.013299827212922373, -0.014837512066932575, -0.016458350974447707, -0.018155753835766026, -0.019921790506671644, -0.02174722425642136, -0.023621568544962765, -0.025533167067605902, -0.027469296540794302, -0.029416291224546955, -0.031359687706557345, -0.03328438802089931, -0.03517483875165445, -0.037015223388917905, -0.03878966487117647, -0.04048243497259204, -0.04207816698364042, -0.04356206799476007, -0.044920127029484, -0.046139315288504214, -0.047207774860015456, -0.04811499242335274, -0.04885195471940834, -0.04941128287779857, -0.04978734307077841] + [-0.04997633139944227] * 2 + [-0.04978734307077841, -0.04941128287779857, -0.04885195471940834, -0.04811499242335274, -0.047207774860015456, -0.046139315288504214, -0.044920127029484, -0.04356206799476007, -0.04207816698364042, -0.0404824349725921, -0.03878966487117647, -0.037015223388917905, -0.03517483875165445, -0.03328438802089931, -0.031359687706557345, -0.029416291224546955, -0.027469296540794302, -0.025533167067605902, -0.023621568544962807, -0.02174722425642136, -0.019921790506671644, -0.018155753835766057, -0.016458350974447707, -0.014837512066932575, -0.013299827212922373, -0.011850535920178554, -0.010493538622702324, -0.009231429016631038, -0.008065545604508713, -0.006996040525523105, -0.006021963490151232, -0.005141358436474014, -0.004351370384723694, -0.0036483598873740444, -0.0030280224536970396, -0.0024855103681417643, -0.0020155544177197053, -0.001612583190143581, -0.0012708377960228441, -0.0009844800983365525, -0.0007476927933623619, -0.0005547699714462471, -0.0004001970854089779, -0.000278719560929705, -0.0001853995890370048, -0.00011566093837204936, -6.532190723564374e-05, -3.061679638980782e-05] + [0] * 2,
        },
        "minus_x90_kaiser_Q_wf_qp_control_c3t2": {
            "type": "arbitrary",
            "samples": [0] * 100,
        },
        "y180_kaiser_I_wf_qp_control_c3t2": {
            "type": "arbitrary",
            "samples": [0] * 100,
        },
        "y180_kaiser_Q_wf_qp_control_c3t2": {
            "type": "arbitrary",
            "samples": [6.123359277961564e-05, 0.0001306438144712879, 0.00023132187674409848, 0.0003707991780740096, 0.0005574391218594114, 0.0008003941708179544, 0.0011095399428924942, 0.0014953855867247238, 0.0019689601966731024, 0.0025416755920456883, 0.003225166380287162, 0.0040311088354394045, 0.0049710207362835285, 0.006056044907394079, 0.007296719774748082, 0.008702740769447388, 0.010282716872948027, 0.012043926980302464, 0.01399208105104621, 0.016131091209017425, 0.018462858033262076, 0.020987077245404648, 0.023701071840357107, 0.026599654425844745, 0.02967502413386515, 0.03291670194889541, 0.03631150767153205, 0.03984358101334329, 0.04349444851284272, 0.04724313708992553, 0.051066334135211805, 0.054938593081588605, 0.05883258244909391, 0.06271937541311469, 0.06656877604179862, 0.0703496775033089, 0.07403044677783581, 0.07757932974235295, 0.08096486994518408, 0.08415633396728084, 0.08712413598952014, 0.089840254058968, 0.09227863057700843, 0.09441554972003091, 0.09622998484670547, 0.09770390943881668, 0.09882256575559714, 0.09957468614155682] + [0.09995266279888454] * 2 + [0.09957468614155682, 0.09882256575559714, 0.09770390943881668, 0.09622998484670547, 0.09441554972003091, 0.09227863057700843, 0.089840254058968, 0.08712413598952014, 0.08415633396728084, 0.0809648699451842, 0.07757932974235295, 0.07403044677783581, 0.0703496775033089, 0.06656877604179862, 0.06271937541311469, 0.05883258244909391, 0.054938593081588605, 0.051066334135211805, 0.04724313708992561, 0.04349444851284272, 0.03984358101334329, 0.036311507671532114, 0.03291670194889541, 0.02967502413386515, 0.026599654425844745, 0.023701071840357107, 0.020987077245404648, 0.018462858033262076, 0.016131091209017425, 0.01399208105104621, 0.012043926980302464, 0.010282716872948027, 0.008702740769447388, 0.007296719774748089, 0.006056044907394079, 0.0049710207362835285, 0.004031108835439411, 0.003225166380287162, 0.0025416755920456883, 0.001968960196673105, 0.0014953855867247238, 0.0011095399428924942, 0.0008003941708179558, 0.00055743912185941, 0.0003707991780740096, 0.00023132187674409872, 0.00013064381447128748, 6.123359277961564e-05] + [0] * 2,
        },
        "y90_kaiser_I_wf_qp_control_c3t2": {
            "type": "arbitrary",
            "samples": [0] * 100,
        },
        "y90_kaiser_Q_wf_qp_control_c3t2": {
            "type": "arbitrary",
            "samples": [3.061679638980782e-05, 6.532190723564394e-05, 0.00011566093837204924, 0.0001853995890370048, 0.0002787195609297057, 0.0004001970854089772, 0.0005547699714462471, 0.0007476927933623619, 0.0009844800983365512, 0.0012708377960228441, 0.001612583190143581, 0.0020155544177197023, 0.0024855103681417643, 0.0030280224536970396, 0.003648359887374041, 0.004351370384723694, 0.005141358436474014, 0.006021963490151232, 0.006996040525523105, 0.008065545604508713, 0.009231429016631038, 0.010493538622702324, 0.011850535920178554, 0.013299827212922373, 0.014837512066932575, 0.016458350974447707, 0.018155753835766026, 0.019921790506671644, 0.02174722425642136, 0.023621568544962765, 0.025533167067605902, 0.027469296540794302, 0.029416291224546955, 0.031359687706557345, 0.03328438802089931, 0.03517483875165445, 0.037015223388917905, 0.03878966487117647, 0.04048243497259204, 0.04207816698364042, 0.04356206799476007, 0.044920127029484, 0.046139315288504214, 0.047207774860015456, 0.04811499242335274, 0.04885195471940834, 0.04941128287779857, 0.04978734307077841] + [0.04997633139944227] * 2 + [0.04978734307077841, 0.04941128287779857, 0.04885195471940834, 0.04811499242335274, 0.047207774860015456, 0.046139315288504214, 0.044920127029484, 0.04356206799476007, 0.04207816698364042, 0.0404824349725921, 0.03878966487117647, 0.037015223388917905, 0.03517483875165445, 0.03328438802089931, 0.031359687706557345, 0.029416291224546955, 0.027469296540794302, 0.025533167067605902, 0.023621568544962807, 0.02174722425642136, 0.019921790506671644, 0.018155753835766057, 0.016458350974447707, 0.014837512066932575, 0.013299827212922373, 0.011850535920178554, 0.010493538622702324, 0.009231429016631038, 0.008065545604508713, 0.006996040525523105, 0.006021963490151232, 0.005141358436474014, 0.004351370384723694, 0.0036483598873740444, 0.0030280224536970396, 0.0024855103681417643, 0.0020155544177197053, 0.001612583190143581, 0.0012708377960228441, 0.0009844800983365525, 0.0007476927933623619, 0.0005547699714462471, 0.0004001970854089779, 0.000278719560929705, 0.0001853995890370048, 0.00011566093837204936, 6.532190723564374e-05, 3.061679638980782e-05] + [0] * 2,
        },
        "minus_y90_kaiser_I_wf_qp_control_c3t2": {
            "type": "arbitrary",
            "samples": [0] * 100,
        },
        "minus_y90_kaiser_Q_wf_qp_control_c3t2": {
            "type": "arbitrary",
            "samples": [-3.061679638980782e-05, -6.532190723564394e-05, -0.00011566093837204924, -0.0001853995890370048, -0.0002787195609297057, -0.0004001970854089772, -0.0005547699714462471, -0.0007476927933623619, -0.0009844800983365512, -0.0012708377960228441, -0.001612583190143581, -0.0020155544177197023, -0.0024855103681417643, -0.0030280224536970396, -0.003648359887374041, -0.004351370384723694, -0.005141358436474014, -0.006021963490151232, -0.006996040525523105, -0.008065545604508713, -0.009231429016631038, -0.010493538622702324, -0.011850535920178554, -0.013299827212922373, -0.014837512066932575, -0.016458350974447707, -0.018155753835766026, -0.019921790506671644, -0.02174722425642136, -0.023621568544962765, -0.025533167067605902, -0.027469296540794302, -0.029416291224546955, -0.031359687706557345, -0.03328438802089931, -0.03517483875165445, -0.037015223388917905, -0.03878966487117647, -0.04048243497259204, -0.04207816698364042, -0.04356206799476007, -0.044920127029484, -0.046139315288504214, -0.047207774860015456, -0.04811499242335274, -0.04885195471940834, -0.04941128287779857, -0.04978734307077841] + [-0.04997633139944227] * 2 + [-0.04978734307077841, -0.04941128287779857, -0.04885195471940834, -0.04811499242335274, -0.047207774860015456, -0.046139315288504214, -0.044920127029484, -0.04356206799476007, -0.04207816698364042, -0.0404824349725921, -0.03878966487117647, -0.037015223388917905, -0.03517483875165445, -0.03328438802089931, -0.031359687706557345, -0.029416291224546955, -0.027469296540794302, -0.025533167067605902, -0.023621568544962807, -0.02174722425642136, -0.019921790506671644, -0.018155753835766057, -0.016458350974447707, -0.014837512066932575, -0.013299827212922373, -0.011850535920178554, -0.010493538622702324, -0.009231429016631038, -0.008065545604508713, -0.006996040525523105, -0.006021963490151232, -0.005141358436474014, -0.004351370384723694, -0.0036483598873740444, -0.0030280224536970396, -0.0024855103681417643, -0.0020155544177197053, -0.001612583190143581, -0.0012708377960228441, -0.0009844800983365525, -0.0007476927933623619, -0.0005547699714462471, -0.0004001970854089779, -0.000278719560929705, -0.0001853995890370048, -0.00011566093837204936, -6.532190723564374e-05, -3.061679638980782e-05] + [0] * 2,
        },
        "step_wf": {
            "type": "constant",
            "sample": 0.25,
        },
        "P1_sticky_step%_wf": {
            "type": "constant",
            "sample": 0.25,
        },
        "P2_sticky_step%_wf": {
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
        "cosine_weights_tank_circuit1": {
            "cosine": [(1.0, 400)],
            "sine": [(0.0, 400)],
        },
        "cosine_weights_tank_circuit2": {
            "cosine": [(1.0, 400)],
            "sine": [(0.0, 400)],
        },
        "sine_weights_tank_circuit1": {
            "cosine": [(0.0, 400)],
            "sine": [(1.0, 400)],
        },
        "sine_weights_tank_circuit2": {
            "cosine": [(0.0, 400)],
            "sine": [(1.0, 400)],
        },
    },
    "mixers": {
        "mixer_qubit1": [{'intermediate_frequency': 0, 'lo_frequency': 16000000000, 'correction': [1.0, 0.0, 0.0, 1.0]}],
        "mixer_qubit2": [{'intermediate_frequency': 0, 'lo_frequency': 16000000000, 'correction': [1.0, 0.0, 0.0, 1.0]}],
        "mixer_qubit3": [{'intermediate_frequency': 0, 'lo_frequency': 16300000000, 'correction': [1.0, 0.0, 0.0, 1.0]}],
        "mixer_qubit4": [{'intermediate_frequency': 50000000, 'lo_frequency': 16300000000, 'correction': [1.0, 0.0, 0.0, 1.0]}],
        "mixer_qubit5": [{'intermediate_frequency': 0, 'lo_frequency': 16300000000, 'correction': [1.0, 0.0, 0.0, 1.0]}],
        "mixer_qp_control_c3t2": [{'intermediate_frequency': 0, 'lo_frequency': 16300000000, 'correction': [1.0, 0.0, 0.0, 1.0]}],
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
                        "3": {
                            "shareable": False,
                            "inverted": False,
                            "level": "LVTTL",
                        },
                        "5": {
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
                            "crosstalk": {},
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
                            "crosstalk": {},
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
                            "crosstalk": {},
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
        "P1": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "step": "P1_step_pulse",
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
        "P2": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "step": "P2_step_pulse",
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
        "P3": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "step": "P3_step_pulse",
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
        "P4": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "step": "P4_step_pulse",
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
        "P5": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "step": "P5_step_pulse",
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
        "P1_sticky": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "step": "step_pulse",
                "step%": "P1_sticky_step%_pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": True,
                "digital": False,
                "duration": 4,
            },
            "thread": "",
            "singleInput": {
                "port": ('con1', 3, 1),
            },
        },
        "P2_sticky": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "step": "step_pulse",
                "step%": "P2_sticky_step%_pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": True,
                "digital": False,
                "duration": 4,
            },
            "thread": "",
            "singleInput": {
                "port": ('con1', 3, 2),
            },
        },
        "P3_sticky": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "step": "P3_step_pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": True,
                "digital": False,
                "duration": 4,
            },
            "thread": "",
            "singleInput": {
                "port": ('con1', 3, 3),
            },
        },
        "P4_sticky": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "step": "P4_step_pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": True,
                "digital": False,
                "duration": 4,
            },
            "thread": "",
            "singleInput": {
                "port": ('con1', 3, 4),
            },
        },
        "P5_sticky": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "step": "P5_step_pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": True,
                "digital": False,
                "duration": 4,
            },
            "thread": "",
            "singleInput": {
                "port": ('con1', 3, 6),
            },
        },
        "B1": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "step": "B1_step_pulse",
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
        "B2": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "step": "B2_step_pulse",
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
        "B3": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "step": "B3_step_pulse",
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
        "B4": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "step": "B4_step_pulse",
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
        "B1_sticky": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "step": "B1_step_pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": True,
                "digital": False,
                "duration": 4,
            },
            "thread": "",
            "singleInput": {
                "port": ('con1', 3, 4),
            },
        },
        "B2_sticky": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "step": "B2_step_pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": True,
                "digital": False,
                "duration": 4,
            },
            "thread": "",
            "singleInput": {
                "port": ('con1', 3, 5),
            },
        },
        "B3_sticky": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "step": "B3_step_pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": True,
                "digital": False,
                "duration": 4,
            },
            "thread": "",
            "singleInput": {
                "port": ('con1', 3, 6),
            },
        },
        "B4_sticky": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "step": "B4_step_pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": True,
                "digital": False,
                "duration": 4,
            },
            "thread": "",
            "singleInput": {
                "port": ('con1', 3, 6),
            },
        },
        "Psd1": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "step": "Psd1_step_pulse",
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
        "Psd2": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "step": "Psd2_step_pulse",
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
        "Psd1_sticky": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "step": "Psd1_step_pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": True,
                "digital": False,
                "duration": 4,
            },
            "thread": "",
            "singleInput": {
                "port": ('con1', 3, 7),
            },
        },
        "Psd2_sticky": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "step": "Psd2_step_pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": True,
                "digital": False,
                "duration": 4,
            },
            "thread": "",
            "singleInput": {
                "port": ('con1', 3, 8),
            },
        },
        "qubit1": {
            "digitalInputs": {
                "output_switch": {
                    "delay": 40,
                    "buffer": 40,
                    "port": ('con1', 5, 1),
                },
            },
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "saturation": "saturation_pulse",
                "x180_kaiser": "x180_kaiser_pulse_qubit1",
                "x90_kaiser": "x90_kaiser_pulse_qubit1",
                "-x90_kaiser": "minus_x90_kaiser_pulse_qubit1",
                "y180_kaiser": "y180_kaiser_pulse_qubit1",
                "y90_kaiser": "y90_kaiser_pulse_qubit1",
                "-y90_kaiser": "minus_y90_kaiser_pulse_qubit1",
                "x180_gauss": "x180_gaussian_pulse_qubit1",
                "x90_gauss": "x90_gaussian_pulse_qubit1",
                "-x90_gauss": "minus_x90_gaussian_pulse_qubit1",
                "y180_gauss": "y180_gaussian_pulse_qubit1",
                "y90_gauss": "y90_gaussian_pulse_qubit1",
                "-y90_gauss": "minus_y90_gaussian_pulse_qubit1",
                "x180_square": "square_x180_pulse",
                "x90_square": "square_x90_pulse",
                "-x90_square": "square_minus_x90_pulse",
                "y180_square": "square_y180_pulse",
                "y90_square": "square_y90_pulse",
                "-y90_square": "square_minus_y90_pulse",
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
                "I": ('con1', 5, 5),
                "Q": ('con1', 5, 6),
                "mixer": "mixer_qubit1",
                "lo_frequency": 16000000000.0,
            },
            "intermediate_frequency": 0,
        },
        "qubit2": {
            "digitalInputs": {
                "output_switch": {
                    "delay": 40,
                    "buffer": 40,
                    "port": ('con1', 5, 1),
                },
            },
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "saturation": "saturation_pulse",
                "x180_kaiser": "x180_kaiser_pulse_qubit2",
                "x90_kaiser": "x90_kaiser_pulse_qubit2",
                "-x90_kaiser": "minus_x90_kaiser_pulse_qubit2",
                "y180_kaiser": "y180_kaiser_pulse_qubit2",
                "y90_kaiser": "y90_kaiser_pulse_qubit2",
                "-y90_kaiser": "minus_y90_kaiser_pulse_qubit2",
                "x180_gauss": "x180_gaussian_pulse_qubit2",
                "x90_gauss": "x90_gaussian_pulse_qubit2",
                "-x90_gauss": "minus_x90_gaussian_pulse_qubit2",
                "y180_gauss": "y180_gaussian_pulse_qubit2",
                "y90_gauss": "y90_gaussian_pulse_qubit2",
                "-y90_gauss": "minus_y90_gaussian_pulse_qubit2",
                "x180_square": "square_x180_pulse",
                "x90_square": "square_x90_pulse",
                "-x90_square": "square_minus_x90_pulse",
                "y180_square": "square_y180_pulse",
                "y90_square": "square_y90_pulse",
                "-y90_square": "square_minus_y90_pulse",
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
                "I": ('con1', 5, 5),
                "Q": ('con1', 5, 6),
                "mixer": "mixer_qubit2",
                "lo_frequency": 16000000000.0,
            },
            "intermediate_frequency": 0,
        },
        "qubit3": {
            "digitalInputs": {
                "output_switch": {
                    "delay": 40,
                    "buffer": 40,
                    "port": ('con1', 5, 3),
                },
            },
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "saturation": "saturation_pulse",
                "x180_kaiser": "x180_kaiser_pulse_qubit3",
                "x90_kaiser": "x90_kaiser_pulse_qubit3",
                "-x90_kaiser": "minus_x90_kaiser_pulse_qubit3",
                "y180_kaiser": "y180_kaiser_pulse_qubit3",
                "y90_kaiser": "y90_kaiser_pulse_qubit3",
                "-y90_kaiser": "minus_y90_kaiser_pulse_qubit3",
                "x180_gauss": "x180_gaussian_pulse_qubit3",
                "x90_gauss": "x90_gaussian_pulse_qubit3",
                "-x90_gauss": "minus_x90_gaussian_pulse_qubit3",
                "y180_gauss": "y180_gaussian_pulse_qubit3",
                "y90_gauss": "y90_gaussian_pulse_qubit3",
                "-y90_gauss": "minus_y90_gaussian_pulse_qubit3",
                "x180_square": "square_x180_pulse",
                "x90_square": "square_x90_pulse",
                "-x90_square": "square_minus_x90_pulse",
                "y180_square": "square_y180_pulse",
                "y90_square": "square_y90_pulse",
                "-y90_square": "square_minus_y90_pulse",
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
                "I": ('con1', 5, 5),
                "Q": ('con1', 5, 6),
                "mixer": "mixer_qubit3",
                "lo_frequency": 16300000000.0,
            },
            "intermediate_frequency": 0,
        },
        "qubit4": {
            "digitalInputs": {
                "output_switch": {
                    "delay": 40,
                    "buffer": 40,
                    "port": ('con1', 5, 3),
                },
            },
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "saturation": "saturation_pulse",
                "x180_kaiser": "x180_kaiser_pulse_qubit4",
                "x90_kaiser": "x90_kaiser_pulse_qubit4",
                "-x90_kaiser": "minus_x90_kaiser_pulse_qubit4",
                "y180_kaiser": "y180_kaiser_pulse_qubit4",
                "y90_kaiser": "y90_kaiser_pulse_qubit4",
                "-y90_kaiser": "minus_y90_kaiser_pulse_qubit4",
                "x180_gauss": "x180_gaussian_pulse_qubit4",
                "x90_gauss": "x90_gaussian_pulse_qubit4",
                "-x90_gauss": "minus_x90_gaussian_pulse_qubit4",
                "y180_gauss": "y180_gaussian_pulse_qubit4",
                "y90_gauss": "y90_gaussian_pulse_qubit4",
                "-y90_gauss": "minus_y90_gaussian_pulse_qubit4",
                "x180_square": "square_x180_pulse",
                "x90_square": "square_x90_pulse",
                "-x90_square": "square_minus_x90_pulse",
                "y180_square": "square_y180_pulse",
                "y90_square": "square_y90_pulse",
                "-y90_square": "square_minus_y90_pulse",
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
                "I": ('con1', 5, 5),
                "Q": ('con1', 5, 6),
                "mixer": "mixer_qubit4",
                "lo_frequency": 16300000000.0,
            },
            "intermediate_frequency": 50000000.0,
        },
        "qubit5": {
            "digitalInputs": {
                "output_switch": {
                    "delay": 40,
                    "buffer": 40,
                    "port": ('con1', 5, 5),
                },
            },
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "saturation": "saturation_pulse",
                "x180_kaiser": "x180_kaiser_pulse_qubit5",
                "x90_kaiser": "x90_kaiser_pulse_qubit5",
                "-x90_kaiser": "minus_x90_kaiser_pulse_qubit5",
                "y180_kaiser": "y180_kaiser_pulse_qubit5",
                "y90_kaiser": "y90_kaiser_pulse_qubit5",
                "-y90_kaiser": "minus_y90_kaiser_pulse_qubit5",
                "x180_gauss": "x180_gaussian_pulse_qubit5",
                "x90_gauss": "x90_gaussian_pulse_qubit5",
                "-x90_gauss": "minus_x90_gaussian_pulse_qubit5",
                "y180_gauss": "y180_gaussian_pulse_qubit5",
                "y90_gauss": "y90_gaussian_pulse_qubit5",
                "-y90_gauss": "minus_y90_gaussian_pulse_qubit5",
                "x180_square": "square_x180_pulse",
                "x90_square": "square_x90_pulse",
                "-x90_square": "square_minus_x90_pulse",
                "y180_square": "square_y180_pulse",
                "y90_square": "square_y90_pulse",
                "-y90_square": "square_minus_y90_pulse",
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
                "I": ('con1', 5, 5),
                "Q": ('con1', 5, 6),
                "mixer": "mixer_qubit5",
                "lo_frequency": 16300000000.0,
            },
            "intermediate_frequency": 0,
        },
        "qubit1_dup1": {
            "digitalInputs": {
                "marker": {
                    "delay": 40,
                    "buffer": 40,
                    "port": ('con1', 5, 1),
                },
            },
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "saturation": "saturation_pulse",
                "x180_kaiser": "x180_kaiser_pulse_qubit1",
                "x90_kaiser": "x90_kaiser_pulse_qubit1",
                "-x90_kaiser": "minus_x90_kaiser_pulse_qubit1",
                "y180_kaiser": "y180_kaiser_pulse_qubit1",
                "y90_kaiser": "y90_kaiser_pulse_qubit1",
                "-y90_kaiser": "minus_y90_kaiser_pulse_qubit1",
                "x180_gauss": "x180_gaussian_pulse_qubit1",
                "x90_gauss": "x90_gaussian_pulse_qubit1",
                "-x90_gauss": "minus_x90_gaussian_pulse_qubit1",
                "y180_gauss": "y180_gaussian_pulse_qubit1",
                "y90_gauss": "y90_gaussian_pulse_qubit1",
                "-y90_gauss": "minus_y90_gaussian_pulse_qubit1",
                "x180_square": "square_x180_pulse_dup1",
                "x90_square": "square_x90_pulse_dup1",
                "-x90_square": "square_minus_x90_pulse_dup1",
                "y180_square": "square_y180_pulse_dup1",
                "y90_square": "square_y90_pulse_dup1",
                "-y90_square": "square_minus_y90_pulse_dup1",
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
                "I": ('con1', 5, 5),
                "Q": ('con1', 5, 6),
                "mixer": "mixer_qubit1",
                "lo_frequency": 16000000000.0,
            },
            "intermediate_frequency": 0,
        },
        "qubit2_dup1": {
            "digitalInputs": {
                "marker": {
                    "delay": 40,
                    "buffer": 40,
                    "port": ('con1', 5, 1),
                },
            },
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "saturation": "saturation_pulse",
                "x180_kaiser": "x180_kaiser_pulse_qubit2",
                "x90_kaiser": "x90_kaiser_pulse_qubit2",
                "-x90_kaiser": "minus_x90_kaiser_pulse_qubit2",
                "y180_kaiser": "y180_kaiser_pulse_qubit2",
                "y90_kaiser": "y90_kaiser_pulse_qubit2",
                "-y90_kaiser": "minus_y90_kaiser_pulse_qubit2",
                "x180_gauss": "x180_gaussian_pulse_qubit2",
                "x90_gauss": "x90_gaussian_pulse_qubit2",
                "-x90_gauss": "minus_x90_gaussian_pulse_qubit2",
                "y180_gauss": "y180_gaussian_pulse_qubit2",
                "y90_gauss": "y90_gaussian_pulse_qubit2",
                "-y90_gauss": "minus_y90_gaussian_pulse_qubit2",
                "x180_square": "square_x180_pulse_dup1",
                "x90_square": "square_x90_pulse_dup1",
                "-x90_square": "square_minus_x90_pulse_dup1",
                "y180_square": "square_y180_pulse_dup1",
                "y90_square": "square_y90_pulse_dup1",
                "-y90_square": "square_minus_y90_pulse_dup1",
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
                "I": ('con1', 5, 5),
                "Q": ('con1', 5, 6),
                "mixer": "mixer_qubit2",
                "lo_frequency": 16000000000.0,
            },
            "intermediate_frequency": 0,
        },
        "qubit3_dup1": {
            "digitalInputs": {
                "marker": {
                    "delay": 40,
                    "buffer": 40,
                    "port": ('con1', 5, 3),
                },
            },
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "saturation": "saturation_pulse",
                "x180_kaiser": "x180_kaiser_pulse_qubit3",
                "x90_kaiser": "x90_kaiser_pulse_qubit3",
                "-x90_kaiser": "minus_x90_kaiser_pulse_qubit3",
                "y180_kaiser": "y180_kaiser_pulse_qubit3",
                "y90_kaiser": "y90_kaiser_pulse_qubit3",
                "-y90_kaiser": "minus_y90_kaiser_pulse_qubit3",
                "x180_gauss": "x180_gaussian_pulse_qubit3",
                "x90_gauss": "x90_gaussian_pulse_qubit3",
                "-x90_gauss": "minus_x90_gaussian_pulse_qubit3",
                "y180_gauss": "y180_gaussian_pulse_qubit3",
                "y90_gauss": "y90_gaussian_pulse_qubit3",
                "-y90_gauss": "minus_y90_gaussian_pulse_qubit3",
                "x180_square": "square_x180_pulse_dup1",
                "x90_square": "square_x90_pulse_dup1",
                "-x90_square": "square_minus_x90_pulse_dup1",
                "y180_square": "square_y180_pulse_dup1",
                "y90_square": "square_y90_pulse_dup1",
                "-y90_square": "square_minus_y90_pulse_dup1",
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
                "I": ('con1', 5, 5),
                "Q": ('con1', 5, 6),
                "mixer": "mixer_qubit3",
                "lo_frequency": 16300000000.0,
            },
            "intermediate_frequency": 0,
        },
        "qubit4_dup1": {
            "digitalInputs": {
                "marker": {
                    "delay": 40,
                    "buffer": 40,
                    "port": ('con1', 5, 3),
                },
            },
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "saturation": "saturation_pulse",
                "x180_kaiser": "x180_kaiser_pulse_qubit4",
                "x90_kaiser": "x90_kaiser_pulse_qubit4",
                "-x90_kaiser": "minus_x90_kaiser_pulse_qubit4",
                "y180_kaiser": "y180_kaiser_pulse_qubit4",
                "y90_kaiser": "y90_kaiser_pulse_qubit4",
                "-y90_kaiser": "minus_y90_kaiser_pulse_qubit4",
                "x180_gauss": "x180_gaussian_pulse_qubit4",
                "x90_gauss": "x90_gaussian_pulse_qubit4",
                "-x90_gauss": "minus_x90_gaussian_pulse_qubit4",
                "y180_gauss": "y180_gaussian_pulse_qubit4",
                "y90_gauss": "y90_gaussian_pulse_qubit4",
                "-y90_gauss": "minus_y90_gaussian_pulse_qubit4",
                "x180_square": "square_x180_pulse_dup1",
                "x90_square": "square_x90_pulse_dup1",
                "-x90_square": "square_minus_x90_pulse_dup1",
                "y180_square": "square_y180_pulse_dup1",
                "y90_square": "square_y90_pulse_dup1",
                "-y90_square": "square_minus_y90_pulse_dup1",
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
                "I": ('con1', 5, 5),
                "Q": ('con1', 5, 6),
                "mixer": "mixer_qubit4",
                "lo_frequency": 16300000000.0,
            },
            "intermediate_frequency": 50000000.0,
        },
        "qubit5_dup1": {
            "digitalInputs": {
                "marker": {
                    "delay": 40,
                    "buffer": 40,
                    "port": ('con1', 5, 5),
                },
            },
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "saturation": "saturation_pulse",
                "x180_kaiser": "x180_kaiser_pulse_qubit5",
                "x90_kaiser": "x90_kaiser_pulse_qubit5",
                "-x90_kaiser": "minus_x90_kaiser_pulse_qubit5",
                "y180_kaiser": "y180_kaiser_pulse_qubit5",
                "y90_kaiser": "y90_kaiser_pulse_qubit5",
                "-y90_kaiser": "minus_y90_kaiser_pulse_qubit5",
                "x180_gauss": "x180_gaussian_pulse_qubit5",
                "x90_gauss": "x90_gaussian_pulse_qubit5",
                "-x90_gauss": "minus_x90_gaussian_pulse_qubit5",
                "y180_gauss": "y180_gaussian_pulse_qubit5",
                "y90_gauss": "y90_gaussian_pulse_qubit5",
                "-y90_gauss": "minus_y90_gaussian_pulse_qubit5",
                "x180_square": "square_x180_pulse_dup1",
                "x90_square": "square_x90_pulse_dup1",
                "-x90_square": "square_minus_x90_pulse_dup1",
                "y180_square": "square_y180_pulse_dup1",
                "y90_square": "square_y90_pulse_dup1",
                "-y90_square": "square_minus_y90_pulse_dup1",
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
                "I": ('con1', 5, 5),
                "Q": ('con1', 5, 6),
                "mixer": "mixer_qubit5",
                "lo_frequency": 16300000000.0,
            },
            "intermediate_frequency": 0,
        },
        "qubit1_dup2": {
            "digitalInputs": {
                "marker": {
                    "delay": 40,
                    "buffer": 40,
                    "port": ('con1', 5, 1),
                },
            },
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "saturation": "saturation_pulse",
                "x180_kaiser": "x180_kaiser_pulse_qubit1",
                "x90_kaiser": "x90_kaiser_pulse_qubit1",
                "-x90_kaiser": "minus_x90_kaiser_pulse_qubit1",
                "y180_kaiser": "y180_kaiser_pulse_qubit1",
                "y90_kaiser": "y90_kaiser_pulse_qubit1",
                "-y90_kaiser": "minus_y90_kaiser_pulse_qubit1",
                "x180_gauss": "x180_gaussian_pulse_qubit1",
                "x90_gauss": "x90_gaussian_pulse_qubit1",
                "-x90_gauss": "minus_x90_gaussian_pulse_qubit1",
                "y180_gauss": "y180_gaussian_pulse_qubit1",
                "y90_gauss": "y90_gaussian_pulse_qubit1",
                "-y90_gauss": "minus_y90_gaussian_pulse_qubit1",
                "x180_square": "square_x180_pulse_dup2",
                "x90_square": "square_x90_pulse_dup2",
                "-x90_square": "square_minus_x90_pulse_dup2",
                "y180_square": "square_y180_pulse_dup2",
                "y90_square": "square_y90_pulse_dup2",
                "-y90_square": "square_minus_y90_pulse_dup2",
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
                "I": ('con1', 5, 5),
                "Q": ('con1', 5, 6),
                "mixer": "mixer_qubit1",
                "lo_frequency": 16000000000.0,
            },
            "intermediate_frequency": 0,
        },
        "qubit2_dup2": {
            "digitalInputs": {
                "marker": {
                    "delay": 40,
                    "buffer": 40,
                    "port": ('con1', 5, 1),
                },
            },
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "saturation": "saturation_pulse",
                "x180_kaiser": "x180_kaiser_pulse_qubit2",
                "x90_kaiser": "x90_kaiser_pulse_qubit2",
                "-x90_kaiser": "minus_x90_kaiser_pulse_qubit2",
                "y180_kaiser": "y180_kaiser_pulse_qubit2",
                "y90_kaiser": "y90_kaiser_pulse_qubit2",
                "-y90_kaiser": "minus_y90_kaiser_pulse_qubit2",
                "x180_gauss": "x180_gaussian_pulse_qubit2",
                "x90_gauss": "x90_gaussian_pulse_qubit2",
                "-x90_gauss": "minus_x90_gaussian_pulse_qubit2",
                "y180_gauss": "y180_gaussian_pulse_qubit2",
                "y90_gauss": "y90_gaussian_pulse_qubit2",
                "-y90_gauss": "minus_y90_gaussian_pulse_qubit2",
                "x180_square": "square_x180_pulse_dup2",
                "x90_square": "square_x90_pulse_dup2",
                "-x90_square": "square_minus_x90_pulse_dup2",
                "y180_square": "square_y180_pulse_dup2",
                "y90_square": "square_y90_pulse_dup2",
                "-y90_square": "square_minus_y90_pulse_dup2",
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
                "I": ('con1', 5, 5),
                "Q": ('con1', 5, 6),
                "mixer": "mixer_qubit2",
                "lo_frequency": 16000000000.0,
            },
            "intermediate_frequency": 0,
        },
        "qubit3_dup2": {
            "digitalInputs": {
                "marker": {
                    "delay": 40,
                    "buffer": 40,
                    "port": ('con1', 5, 3),
                },
            },
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "saturation": "saturation_pulse",
                "x180_kaiser": "x180_kaiser_pulse_qubit3",
                "x90_kaiser": "x90_kaiser_pulse_qubit3",
                "-x90_kaiser": "minus_x90_kaiser_pulse_qubit3",
                "y180_kaiser": "y180_kaiser_pulse_qubit3",
                "y90_kaiser": "y90_kaiser_pulse_qubit3",
                "-y90_kaiser": "minus_y90_kaiser_pulse_qubit3",
                "x180_gauss": "x180_gaussian_pulse_qubit3",
                "x90_gauss": "x90_gaussian_pulse_qubit3",
                "-x90_gauss": "minus_x90_gaussian_pulse_qubit3",
                "y180_gauss": "y180_gaussian_pulse_qubit3",
                "y90_gauss": "y90_gaussian_pulse_qubit3",
                "-y90_gauss": "minus_y90_gaussian_pulse_qubit3",
                "x180_square": "square_x180_pulse_dup2",
                "x90_square": "square_x90_pulse_dup2",
                "-x90_square": "square_minus_x90_pulse_dup2",
                "y180_square": "square_y180_pulse_dup2",
                "y90_square": "square_y90_pulse_dup2",
                "-y90_square": "square_minus_y90_pulse_dup2",
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
                "I": ('con1', 5, 5),
                "Q": ('con1', 5, 6),
                "mixer": "mixer_qubit3",
                "lo_frequency": 16300000000.0,
            },
            "intermediate_frequency": 0,
        },
        "qubit4_dup2": {
            "digitalInputs": {
                "marker": {
                    "delay": 40,
                    "buffer": 40,
                    "port": ('con1', 5, 3),
                },
            },
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "saturation": "saturation_pulse",
                "x180_kaiser": "x180_kaiser_pulse_qubit4",
                "x90_kaiser": "x90_kaiser_pulse_qubit4",
                "-x90_kaiser": "minus_x90_kaiser_pulse_qubit4",
                "y180_kaiser": "y180_kaiser_pulse_qubit4",
                "y90_kaiser": "y90_kaiser_pulse_qubit4",
                "-y90_kaiser": "minus_y90_kaiser_pulse_qubit4",
                "x180_gauss": "x180_gaussian_pulse_qubit4",
                "x90_gauss": "x90_gaussian_pulse_qubit4",
                "-x90_gauss": "minus_x90_gaussian_pulse_qubit4",
                "y180_gauss": "y180_gaussian_pulse_qubit4",
                "y90_gauss": "y90_gaussian_pulse_qubit4",
                "-y90_gauss": "minus_y90_gaussian_pulse_qubit4",
                "x180_square": "square_x180_pulse_dup2",
                "x90_square": "square_x90_pulse_dup2",
                "-x90_square": "square_minus_x90_pulse_dup2",
                "y180_square": "square_y180_pulse_dup2",
                "y90_square": "square_y90_pulse_dup2",
                "-y90_square": "square_minus_y90_pulse_dup2",
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
                "I": ('con1', 5, 5),
                "Q": ('con1', 5, 6),
                "mixer": "mixer_qubit4",
                "lo_frequency": 16300000000.0,
            },
            "intermediate_frequency": 50000000.0,
        },
        "qubit5_dup2": {
            "digitalInputs": {
                "marker": {
                    "delay": 40,
                    "buffer": 40,
                    "port": ('con1', 5, 5),
                },
            },
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "saturation": "saturation_pulse",
                "x180_kaiser": "x180_kaiser_pulse_qubit5",
                "x90_kaiser": "x90_kaiser_pulse_qubit5",
                "-x90_kaiser": "minus_x90_kaiser_pulse_qubit5",
                "y180_kaiser": "y180_kaiser_pulse_qubit5",
                "y90_kaiser": "y90_kaiser_pulse_qubit5",
                "-y90_kaiser": "minus_y90_kaiser_pulse_qubit5",
                "x180_gauss": "x180_gaussian_pulse_qubit5",
                "x90_gauss": "x90_gaussian_pulse_qubit5",
                "-x90_gauss": "minus_x90_gaussian_pulse_qubit5",
                "y180_gauss": "y180_gaussian_pulse_qubit5",
                "y90_gauss": "y90_gaussian_pulse_qubit5",
                "-y90_gauss": "minus_y90_gaussian_pulse_qubit5",
                "x180_square": "square_x180_pulse_dup2",
                "x90_square": "square_x90_pulse_dup2",
                "-x90_square": "square_minus_x90_pulse_dup2",
                "y180_square": "square_y180_pulse_dup2",
                "y90_square": "square_y90_pulse_dup2",
                "-y90_square": "square_minus_y90_pulse_dup2",
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
                "I": ('con1', 5, 5),
                "Q": ('con1', 5, 6),
                "mixer": "mixer_qubit5",
                "lo_frequency": 16300000000.0,
            },
            "intermediate_frequency": 0,
        },
        "qp_control_c3t2": {
            "digitalInputs": {
                "marker": {
                    "delay": 40,
                    "buffer": 0,
                    "port": ('con1', 5, 3),
                },
            },
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "x180_kaiser": "x180_kaiser_pulse_qp_control_c3t2",
                "x90_kaiser": "x90_kaiser_pulse_qp_control_c3t2",
                "-x90_kaiser": "minus_x90_kaiser_pulse_qp_control_c3t2",
                "y180_kaiser": "y180_kaiser_pulse_qp_control_c3t2",
                "y90_kaiser": "y90_kaiser_pulse_qp_control_c3t2",
                "-y90_kaiser": "minus_y90_kaiser_pulse_qp_control_c3t2",
                "x180_gauss": "x180_gaussian_pulse_qp_control_c3t2",
                "x90_gauss": "x90_gaussian_pulse_qp_control_c3t2",
                "-x90_gauss": "minus_x90_gaussian_pulse_qp_control_c3t2",
                "y180_gauss": "y180_gaussian_pulse_qp_control_c3t2",
                "y90_gauss": "y90_gaussian_pulse_qp_control_c3t2",
                "-y90_gauss": "minus_y90_gaussian_pulse_qp_control_c3t2",
                "x180_square": "square_x180_pulse",
                "x90_square": "square_x90_pulse",
                "-x90_square": "square_minus_x90_pulse",
                "y180_square": "square_y180_pulse",
                "y90_square": "square_y90_pulse",
                "-y90_square": "square_minus_y90_pulse",
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
                "I": ('con1', 5, 5),
                "Q": ('con1', 5, 6),
                "mixer": "mixer_qp_control_c3t2",
                "lo_frequency": 16300000000.0,
            },
            "intermediate_frequency": 0,
        },
        "qubit1_trigger": {
            "digitalInputs": {
                "trigger": {
                    "delay": 0,
                    "buffer": 0,
                    "port": ('con1', 5, 1),
                },
            },
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "trigger": "trigger_pulse",
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
        },
        "qubit2_trigger": {
            "digitalInputs": {
                "trigger": {
                    "delay": 0,
                    "buffer": 0,
                    "port": ('con1', 5, 1),
                },
            },
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "trigger": "trigger_pulse",
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
        },
        "qubit3_trigger": {
            "digitalInputs": {
                "trigger": {
                    "delay": 0,
                    "buffer": 0,
                    "port": ('con1', 5, 3),
                },
            },
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "trigger": "trigger_pulse",
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
        },
        "qubit4_trigger": {
            "digitalInputs": {
                "trigger": {
                    "delay": 0,
                    "buffer": 0,
                    "port": ('con1', 5, 3),
                },
            },
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "trigger": "trigger_pulse",
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
        },
        "qubit5_trigger": {
            "digitalInputs": {
                "trigger": {
                    "delay": 0,
                    "buffer": 0,
                    "port": ('con1', 5, 5),
                },
            },
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "trigger": "trigger_pulse",
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
        },
        "tank_circuit1": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {
                "out1": ('con1', 5, 2),
            },
            "operations": {
                "readout": "reflectometry_readout_pulse_tank_circuit1",
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
                "port": ('con1', 5, 8),
            },
            "smearing": 0,
            "time_of_flight": 24,
            "intermediate_frequency": 50000000.0,
        },
        "tank_circuit2": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {
                "out1": ('con1', 5, 2),
            },
            "operations": {
                "readout": "reflectometry_readout_pulse_tank_circuit2",
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
                "port": ('con1', 5, 8),
            },
            "smearing": 0,
            "time_of_flight": 24,
            "intermediate_frequency": 100000000.0,
        },
    },
    "pulses": {
        "P1_step_pulse": {
            "length": 1000,
            "waveforms": {
                "single": "P1_step_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "P2_step_pulse": {
            "length": 1000,
            "waveforms": {
                "single": "P2_step_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "P3_step_pulse": {
            "length": 1000,
            "waveforms": {
                "single": "P3_step_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "P4_step_pulse": {
            "length": 1000,
            "waveforms": {
                "single": "P4_step_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "P5_step_pulse": {
            "length": 1000,
            "waveforms": {
                "single": "P5_step_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "B1_step_pulse": {
            "length": 1000,
            "waveforms": {
                "single": "B1_step_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "B2_step_pulse": {
            "length": 1000,
            "waveforms": {
                "single": "B2_step_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "B3_step_pulse": {
            "length": 1000,
            "waveforms": {
                "single": "B3_step_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "B4_step_pulse": {
            "length": 1000,
            "waveforms": {
                "single": "B4_step_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "Psd1_step_pulse": {
            "length": 1000,
            "waveforms": {
                "single": "Psd1_step_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "Psd2_step_pulse": {
            "length": 1000,
            "waveforms": {
                "single": "Psd2_step_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "x180_gaussian_pulse_qubit1": {
            "length": 52,
            "waveforms": {
                "I": "x180_gaussian_I_wf_qubit1",
                "Q": "x180_gaussian_Q_wf_qubit1",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "x180_gaussian_pulse_qubit2": {
            "length": 52,
            "waveforms": {
                "I": "x180_gaussian_I_wf_qubit2",
                "Q": "x180_gaussian_Q_wf_qubit2",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "x180_gaussian_pulse_qubit3": {
            "length": 52,
            "waveforms": {
                "I": "x180_gaussian_I_wf_qubit3",
                "Q": "x180_gaussian_Q_wf_qubit3",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "x180_gaussian_pulse_qubit4": {
            "length": 52,
            "waveforms": {
                "I": "x180_gaussian_I_wf_qubit4",
                "Q": "x180_gaussian_Q_wf_qubit4",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "x180_gaussian_pulse_qubit5": {
            "length": 52,
            "waveforms": {
                "I": "x180_gaussian_I_wf_qubit5",
                "Q": "x180_gaussian_Q_wf_qubit5",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "x90_gaussian_pulse_qubit1": {
            "length": 52,
            "waveforms": {
                "I": "x90_gaussian_I_wf_qubit1",
                "Q": "x90_gaussian_Q_wf_qubit1",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "x90_gaussian_pulse_qubit2": {
            "length": 52,
            "waveforms": {
                "I": "x90_gaussian_I_wf_qubit2",
                "Q": "x90_gaussian_Q_wf_qubit2",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "x90_gaussian_pulse_qubit3": {
            "length": 52,
            "waveforms": {
                "I": "x90_gaussian_I_wf_qubit3",
                "Q": "x90_gaussian_Q_wf_qubit3",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "x90_gaussian_pulse_qubit4": {
            "length": 52,
            "waveforms": {
                "I": "x90_gaussian_I_wf_qubit4",
                "Q": "x90_gaussian_Q_wf_qubit4",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "x90_gaussian_pulse_qubit5": {
            "length": 52,
            "waveforms": {
                "I": "x90_gaussian_I_wf_qubit5",
                "Q": "x90_gaussian_Q_wf_qubit5",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "minus_x90_gaussian_pulse_qubit1": {
            "length": 52,
            "waveforms": {
                "I": "minus_x90_gaussian_I_wf_qubit1",
                "Q": "minus_x90_gaussian_Q_wf_qubit1",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "minus_x90_gaussian_pulse_qubit2": {
            "length": 52,
            "waveforms": {
                "I": "minus_x90_gaussian_I_wf_qubit2",
                "Q": "minus_x90_gaussian_Q_wf_qubit2",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "minus_x90_gaussian_pulse_qubit3": {
            "length": 52,
            "waveforms": {
                "I": "minus_x90_gaussian_I_wf_qubit3",
                "Q": "minus_x90_gaussian_Q_wf_qubit3",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "minus_x90_gaussian_pulse_qubit4": {
            "length": 52,
            "waveforms": {
                "I": "minus_x90_gaussian_I_wf_qubit4",
                "Q": "minus_x90_gaussian_Q_wf_qubit4",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "minus_x90_gaussian_pulse_qubit5": {
            "length": 52,
            "waveforms": {
                "I": "minus_x90_gaussian_I_wf_qubit5",
                "Q": "minus_x90_gaussian_Q_wf_qubit5",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "y180_gaussian_pulse_qubit1": {
            "length": 52,
            "waveforms": {
                "I": "y180_gaussian_I_wf_qubit1",
                "Q": "y180_gaussian_Q_wf_qubit1",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "y180_gaussian_pulse_qubit2": {
            "length": 52,
            "waveforms": {
                "I": "y180_gaussian_I_wf_qubit2",
                "Q": "y180_gaussian_Q_wf_qubit2",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "y180_gaussian_pulse_qubit3": {
            "length": 52,
            "waveforms": {
                "I": "y180_gaussian_I_wf_qubit3",
                "Q": "y180_gaussian_Q_wf_qubit3",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "y180_gaussian_pulse_qubit4": {
            "length": 52,
            "waveforms": {
                "I": "y180_gaussian_I_wf_qubit4",
                "Q": "y180_gaussian_Q_wf_qubit4",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "y180_gaussian_pulse_qubit5": {
            "length": 52,
            "waveforms": {
                "I": "y180_gaussian_I_wf_qubit5",
                "Q": "y180_gaussian_Q_wf_qubit5",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "y90_gaussian_pulse_qubit1": {
            "length": 52,
            "waveforms": {
                "I": "y90_gaussian_I_wf_qubit1",
                "Q": "y90_gaussian_Q_wf_qubit1",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "y90_gaussian_pulse_qubit2": {
            "length": 52,
            "waveforms": {
                "I": "y90_gaussian_I_wf_qubit2",
                "Q": "y90_gaussian_Q_wf_qubit2",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "y90_gaussian_pulse_qubit3": {
            "length": 52,
            "waveforms": {
                "I": "y90_gaussian_I_wf_qubit3",
                "Q": "y90_gaussian_Q_wf_qubit3",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "y90_gaussian_pulse_qubit4": {
            "length": 52,
            "waveforms": {
                "I": "y90_gaussian_I_wf_qubit4",
                "Q": "y90_gaussian_Q_wf_qubit4",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "y90_gaussian_pulse_qubit5": {
            "length": 52,
            "waveforms": {
                "I": "y90_gaussian_I_wf_qubit5",
                "Q": "y90_gaussian_Q_wf_qubit5",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "minus_y90_gaussian_pulse_qubit1": {
            "length": 52,
            "waveforms": {
                "I": "minus_y90_gaussian_I_wf_qubit1",
                "Q": "minus_y90_gaussian_Q_wf_qubit1",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "minus_y90_gaussian_pulse_qubit2": {
            "length": 52,
            "waveforms": {
                "I": "minus_y90_gaussian_I_wf_qubit2",
                "Q": "minus_y90_gaussian_Q_wf_qubit2",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "minus_y90_gaussian_pulse_qubit3": {
            "length": 52,
            "waveforms": {
                "I": "minus_y90_gaussian_I_wf_qubit3",
                "Q": "minus_y90_gaussian_Q_wf_qubit3",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "minus_y90_gaussian_pulse_qubit4": {
            "length": 52,
            "waveforms": {
                "I": "minus_y90_gaussian_I_wf_qubit4",
                "Q": "minus_y90_gaussian_Q_wf_qubit4",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "minus_y90_gaussian_pulse_qubit5": {
            "length": 52,
            "waveforms": {
                "I": "minus_y90_gaussian_I_wf_qubit5",
                "Q": "minus_y90_gaussian_Q_wf_qubit5",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "x180_kaiser_pulse_qubit1": {
            "length": 52,
            "waveforms": {
                "I": "x180_kaiser_I_wf_qubit1",
                "Q": "x180_kaiser_Q_wf_qubit1",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "x180_kaiser_pulse_qubit2": {
            "length": 52,
            "waveforms": {
                "I": "x180_kaiser_I_wf_qubit2",
                "Q": "x180_kaiser_Q_wf_qubit2",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "x180_kaiser_pulse_qubit3": {
            "length": 52,
            "waveforms": {
                "I": "x180_kaiser_I_wf_qubit3",
                "Q": "x180_kaiser_Q_wf_qubit3",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "x180_kaiser_pulse_qubit4": {
            "length": 52,
            "waveforms": {
                "I": "x180_kaiser_I_wf_qubit4",
                "Q": "x180_kaiser_Q_wf_qubit4",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "x180_kaiser_pulse_qubit5": {
            "length": 52,
            "waveforms": {
                "I": "x180_kaiser_I_wf_qubit5",
                "Q": "x180_kaiser_Q_wf_qubit5",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "x90_kaiser_pulse_qubit1": {
            "length": 52,
            "waveforms": {
                "I": "x90_kaiser_I_wf_qubit1",
                "Q": "x90_kaiser_Q_wf_qubit1",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "x90_kaiser_pulse_qubit2": {
            "length": 52,
            "waveforms": {
                "I": "x90_kaiser_I_wf_qubit2",
                "Q": "x90_kaiser_Q_wf_qubit2",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "x90_kaiser_pulse_qubit3": {
            "length": 52,
            "waveforms": {
                "I": "x90_kaiser_I_wf_qubit3",
                "Q": "x90_kaiser_Q_wf_qubit3",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "x90_kaiser_pulse_qubit4": {
            "length": 52,
            "waveforms": {
                "I": "x90_kaiser_I_wf_qubit4",
                "Q": "x90_kaiser_Q_wf_qubit4",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "x90_kaiser_pulse_qubit5": {
            "length": 52,
            "waveforms": {
                "I": "x90_kaiser_I_wf_qubit5",
                "Q": "x90_kaiser_Q_wf_qubit5",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "minus_x90_kaiser_pulse_qubit1": {
            "length": 52,
            "waveforms": {
                "I": "minus_x90_kaiser_I_wf_qubit1",
                "Q": "minus_x90_kaiser_Q_wf_qubit1",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "minus_x90_kaiser_pulse_qubit2": {
            "length": 52,
            "waveforms": {
                "I": "minus_x90_kaiser_I_wf_qubit2",
                "Q": "minus_x90_kaiser_Q_wf_qubit2",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "minus_x90_kaiser_pulse_qubit3": {
            "length": 52,
            "waveforms": {
                "I": "minus_x90_kaiser_I_wf_qubit3",
                "Q": "minus_x90_kaiser_Q_wf_qubit3",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "minus_x90_kaiser_pulse_qubit4": {
            "length": 52,
            "waveforms": {
                "I": "minus_x90_kaiser_I_wf_qubit4",
                "Q": "minus_x90_kaiser_Q_wf_qubit4",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "minus_x90_kaiser_pulse_qubit5": {
            "length": 52,
            "waveforms": {
                "I": "minus_x90_kaiser_I_wf_qubit5",
                "Q": "minus_x90_kaiser_Q_wf_qubit5",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "y180_kaiser_pulse_qubit1": {
            "length": 52,
            "waveforms": {
                "I": "y180_kaiser_I_wf_qubit1",
                "Q": "y180_kaiser_Q_wf_qubit1",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "y180_kaiser_pulse_qubit2": {
            "length": 52,
            "waveforms": {
                "I": "y180_kaiser_I_wf_qubit2",
                "Q": "y180_kaiser_Q_wf_qubit2",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "y180_kaiser_pulse_qubit3": {
            "length": 52,
            "waveforms": {
                "I": "y180_kaiser_I_wf_qubit3",
                "Q": "y180_kaiser_Q_wf_qubit3",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "y180_kaiser_pulse_qubit4": {
            "length": 52,
            "waveforms": {
                "I": "y180_kaiser_I_wf_qubit4",
                "Q": "y180_kaiser_Q_wf_qubit4",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "y180_kaiser_pulse_qubit5": {
            "length": 52,
            "waveforms": {
                "I": "y180_kaiser_I_wf_qubit5",
                "Q": "y180_kaiser_Q_wf_qubit5",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "y90_kaiser_pulse_qubit1": {
            "length": 52,
            "waveforms": {
                "I": "y90_kaiser_I_wf_qubit1",
                "Q": "y90_kaiser_Q_wf_qubit1",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "y90_kaiser_pulse_qubit2": {
            "length": 52,
            "waveforms": {
                "I": "y90_kaiser_I_wf_qubit2",
                "Q": "y90_kaiser_Q_wf_qubit2",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "y90_kaiser_pulse_qubit3": {
            "length": 52,
            "waveforms": {
                "I": "y90_kaiser_I_wf_qubit3",
                "Q": "y90_kaiser_Q_wf_qubit3",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "y90_kaiser_pulse_qubit4": {
            "length": 52,
            "waveforms": {
                "I": "y90_kaiser_I_wf_qubit4",
                "Q": "y90_kaiser_Q_wf_qubit4",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "y90_kaiser_pulse_qubit5": {
            "length": 52,
            "waveforms": {
                "I": "y90_kaiser_I_wf_qubit5",
                "Q": "y90_kaiser_Q_wf_qubit5",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "minus_y90_kaiser_pulse_qubit1": {
            "length": 52,
            "waveforms": {
                "I": "minus_y90_kaiser_I_wf_qubit1",
                "Q": "minus_y90_kaiser_Q_wf_qubit1",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "minus_y90_kaiser_pulse_qubit2": {
            "length": 52,
            "waveforms": {
                "I": "minus_y90_kaiser_I_wf_qubit2",
                "Q": "minus_y90_kaiser_Q_wf_qubit2",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "minus_y90_kaiser_pulse_qubit3": {
            "length": 52,
            "waveforms": {
                "I": "minus_y90_kaiser_I_wf_qubit3",
                "Q": "minus_y90_kaiser_Q_wf_qubit3",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "minus_y90_kaiser_pulse_qubit4": {
            "length": 52,
            "waveforms": {
                "I": "minus_y90_kaiser_I_wf_qubit4",
                "Q": "minus_y90_kaiser_Q_wf_qubit4",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "minus_y90_kaiser_pulse_qubit5": {
            "length": 52,
            "waveforms": {
                "I": "minus_y90_kaiser_I_wf_qubit5",
                "Q": "minus_y90_kaiser_Q_wf_qubit5",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "x180_gaussian_pulse_qp_control_c3t2": {
            "length": 100,
            "waveforms": {
                "I": "x180_gaussian_I_wf_qp_control_c3t2",
                "Q": "x180_gaussian_Q_wf_qp_control_c3t2",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "x90_gaussian_pulse_qp_control_c3t2": {
            "length": 100,
            "waveforms": {
                "I": "x90_gaussian_I_wf_qp_control_c3t2",
                "Q": "x90_gaussian_Q_wf_qp_control_c3t2",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "minus_x90_gaussian_pulse_qp_control_c3t2": {
            "length": 100,
            "waveforms": {
                "I": "minus_x90_gaussian_I_wf_qp_control_c3t2",
                "Q": "minus_x90_gaussian_Q_wf_qp_control_c3t2",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "y180_gaussian_pulse_qp_control_c3t2": {
            "length": 100,
            "waveforms": {
                "I": "y180_gaussian_I_wf_qp_control_c3t2",
                "Q": "y180_gaussian_Q_wf_qp_control_c3t2",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "y90_gaussian_pulse_qp_control_c3t2": {
            "length": 100,
            "waveforms": {
                "I": "y90_gaussian_I_wf_qp_control_c3t2",
                "Q": "y90_gaussian_Q_wf_qp_control_c3t2",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "minus_y90_gaussian_pulse_qp_control_c3t2": {
            "length": 100,
            "waveforms": {
                "I": "minus_y90_gaussian_I_wf_qp_control_c3t2",
                "Q": "minus_y90_gaussian_Q_wf_qp_control_c3t2",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "x180_kaiser_pulse_qp_control_c3t2": {
            "length": 100,
            "waveforms": {
                "I": "x180_kaiser_I_wf_qp_control_c3t2",
                "Q": "x180_kaiser_Q_wf_qp_control_c3t2",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "x90_kaiser_pulse_qp_control_c3t2": {
            "length": 100,
            "waveforms": {
                "I": "x90_kaiser_I_wf_qp_control_c3t2",
                "Q": "x90_kaiser_Q_wf_qp_control_c3t2",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "minus_x90_kaiser_pulse_qp_control_c3t2": {
            "length": 100,
            "waveforms": {
                "I": "minus_x90_kaiser_I_wf_qp_control_c3t2",
                "Q": "minus_x90_kaiser_Q_wf_qp_control_c3t2",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "y180_kaiser_pulse_qp_control_c3t2": {
            "length": 100,
            "waveforms": {
                "I": "y180_kaiser_I_wf_qp_control_c3t2",
                "Q": "y180_kaiser_Q_wf_qp_control_c3t2",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "y90_kaiser_pulse_qp_control_c3t2": {
            "length": 100,
            "waveforms": {
                "I": "y90_kaiser_I_wf_qp_control_c3t2",
                "Q": "y90_kaiser_Q_wf_qp_control_c3t2",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "minus_y90_kaiser_pulse_qp_control_c3t2": {
            "length": 100,
            "waveforms": {
                "I": "minus_y90_kaiser_I_wf_qp_control_c3t2",
                "Q": "minus_y90_kaiser_Q_wf_qp_control_c3t2",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "reflectometry_readout_pulse_tank_circuit1": {
            "length": 400,
            "waveforms": {
                "single": "reflectometry_readout_wf_tank_circuit1",
            },
            "integration_weights": {
                "cos": "cosine_weights_tank_circuit1",
                "sin": "sine_weights_tank_circuit1",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "reflectometry_readout_pulse_tank_circuit2": {
            "length": 400,
            "waveforms": {
                "single": "reflectometry_readout_wf_tank_circuit2",
            },
            "integration_weights": {
                "cos": "cosine_weights_tank_circuit2",
                "sin": "sine_weights_tank_circuit2",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "const_pulse": {
            "length": 100,
            "waveforms": {
                "I": "const_wf",
                "Q": "zero_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "saturation_pulse": {
            "length": 10000,
            "waveforms": {
                "I": "saturation_wf",
                "Q": "zero_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "square_x180_pulse": {
            "length": 52,
            "waveforms": {
                "I": "square_x180_I_wf",
                "Q": "zero_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "square_x90_pulse": {
            "length": 52,
            "waveforms": {
                "I": "square_x90_I_wf",
                "Q": "zero_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "square_minus_x90_pulse": {
            "length": 52,
            "waveforms": {
                "I": "square_minus_x90_I_wf",
                "Q": "zero_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "square_y180_pulse": {
            "length": 52,
            "waveforms": {
                "I": "square_y180_I_wf",
                "Q": "zero_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "square_y90_pulse": {
            "length": 52,
            "waveforms": {
                "I": "square_y90_I_wf",
                "Q": "zero_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "square_minus_y90_pulse": {
            "length": 52,
            "waveforms": {
                "I": "square_minus_y90_I_wf",
                "Q": "zero_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "square_x180_pulse_dup1": {
            "length": 52,
            "waveforms": {
                "I": "square_x180_I_wf_dup1",
                "Q": "zero_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "square_x90_pulse_dup1": {
            "length": 52,
            "waveforms": {
                "I": "square_x90_I_wf_dup1",
                "Q": "zero_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "square_minus_x90_pulse_dup1": {
            "length": 52,
            "waveforms": {
                "I": "square_minus_x90_I_wf_dup1",
                "Q": "zero_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "square_y180_pulse_dup1": {
            "length": 52,
            "waveforms": {
                "I": "square_y180_I_wf_dup1",
                "Q": "zero_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "square_y90_pulse_dup1": {
            "length": 52,
            "waveforms": {
                "I": "square_y90_I_wf_dup1",
                "Q": "zero_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "square_minus_y90_pulse_dup1": {
            "length": 52,
            "waveforms": {
                "I": "square_minus_y90_I_wf_dup1",
                "Q": "zero_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "square_x180_pulse_dup2": {
            "length": 52,
            "waveforms": {
                "I": "square_x180_I_wf_dup2",
                "Q": "zero_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "square_x90_pulse_dup2": {
            "length": 52,
            "waveforms": {
                "I": "square_x90_I_wf_dup2",
                "Q": "zero_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "square_minus_x90_pulse_dup2": {
            "length": 52,
            "waveforms": {
                "I": "square_minus_x90_I_wf_dup2",
                "Q": "zero_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "square_y180_pulse_dup2": {
            "length": 52,
            "waveforms": {
                "I": "square_y180_I_wf_dup2",
                "Q": "zero_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "square_y90_pulse_dup2": {
            "length": 52,
            "waveforms": {
                "I": "square_y90_I_wf_dup2",
                "Q": "zero_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "square_minus_y90_pulse_dup2": {
            "length": 52,
            "waveforms": {
                "I": "square_minus_y90_I_wf_dup2",
                "Q": "zero_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "trigger_pulse": {
            "length": 1000,
            "waveforms": {},
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
        "step_pulse": {
            "length": 16,
            "waveforms": {
                "single": "step_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "P1_sticky_step%_pulse": {
            "length": 52,
            "waveforms": {
                "single": "P1_sticky_step%_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "P2_sticky_step%_pulse": {
            "length": 52,
            "waveforms": {
                "single": "P2_sticky_step%_wf",
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
        "saturation_wf": {
            "type": "constant",
            "sample": 0.1,
        },
        "square_x180_I_wf": {
            "type": "constant",
            "sample": 0.2,
        },
        "square_x90_I_wf": {
            "type": "constant",
            "sample": 0.1,
        },
        "square_minus_x90_I_wf": {
            "type": "constant",
            "sample": -0.1,
        },
        "square_y180_I_wf": {
            "type": "constant",
            "sample": 0.15,
        },
        "square_y90_I_wf": {
            "type": "constant",
            "sample": 0.075,
        },
        "square_minus_y90_I_wf": {
            "type": "constant",
            "sample": -0.075,
        },
        "square_x180_I_wf_dup1": {
            "type": "constant",
            "sample": 0.13333333333333333,
        },
        "square_x90_I_wf_dup1": {
            "type": "constant",
            "sample": 0.06666666666666667,
        },
        "square_minus_x90_I_wf_dup1": {
            "type": "constant",
            "sample": -0.06666666666666667,
        },
        "square_y180_I_wf_dup1": {
            "type": "constant",
            "sample": 0.09999999999999999,
        },
        "square_y90_I_wf_dup1": {
            "type": "constant",
            "sample": 0.049999999999999996,
        },
        "square_minus_y90_I_wf_dup1": {
            "type": "constant",
            "sample": -0.049999999999999996,
        },
        "square_x180_I_wf_dup2": {
            "type": "constant",
            "sample": 0.06666666666666667,
        },
        "square_x90_I_wf_dup2": {
            "type": "constant",
            "sample": 0.03333333333333333,
        },
        "square_minus_x90_I_wf_dup2": {
            "type": "constant",
            "sample": -0.03333333333333333,
        },
        "square_y180_I_wf_dup2": {
            "type": "constant",
            "sample": 0.049999999999999996,
        },
        "square_y90_I_wf_dup2": {
            "type": "constant",
            "sample": 0.024999999999999998,
        },
        "square_minus_y90_I_wf_dup2": {
            "type": "constant",
            "sample": -0.024999999999999998,
        },
        "reflectometry_readout_wf_tank_circuit1": {
            "type": "constant",
            "sample": 0.1,
        },
        "reflectometry_readout_wf_tank_circuit2": {
            "type": "constant",
            "sample": 0.1,
        },
        "P1_step_wf": {
            "type": "constant",
            "sample": 0.25,
        },
        "P2_step_wf": {
            "type": "constant",
            "sample": 0.25,
        },
        "P3_step_wf": {
            "type": "constant",
            "sample": 0.25,
        },
        "P4_step_wf": {
            "type": "constant",
            "sample": 0.25,
        },
        "P5_step_wf": {
            "type": "constant",
            "sample": 0.25,
        },
        "B1_step_wf": {
            "type": "constant",
            "sample": 0.25,
        },
        "B2_step_wf": {
            "type": "constant",
            "sample": 0.25,
        },
        "B3_step_wf": {
            "type": "constant",
            "sample": 0.25,
        },
        "B4_step_wf": {
            "type": "constant",
            "sample": 0.25,
        },
        "Psd1_step_wf": {
            "type": "constant",
            "sample": 0.25,
        },
        "Psd2_step_wf": {
            "type": "constant",
            "sample": 0.25,
        },
        "x180_gaussian_I_wf_qubit1": {
            "type": "arbitrary",
            "samples": [0.0, 0.0013487829662939248, 0.0029834635305878076, 0.004941237909839778, 0.0072578579934551015, 0.00996569018380684, 0.013091497820654437, 0.016654029341753772, 0.0206615278002724, 0.025109308094492595, 0.02997757267874069, 0.035229650968230525, 0.04081084883592647, 0.046648080053314674, 0.05265042002594503, 0.058710674095939365, 0.06470799020836852, 0.07051147285766579, 0.07598467752555374, 0.08099078901901928, 0.08539822044608465, 0.08908631899519925, 0.09195083610639947, 0.09390881711988835] + [0.09490259075122315] * 2 + [0.09390881711988835, 0.09195083610639947, 0.08908631899519925, 0.08539822044608465, 0.08099078901901928, 0.07598467752555374, 0.07051147285766579, 0.06470799020836852, 0.058710674095939365, 0.05265042002594503, 0.046648080053314674, 0.04081084883592647, 0.035229650968230525, 0.02997757267874069, 0.025109308094492595, 0.0206615278002724, 0.016654029341753772, 0.013091497820654437, 0.00996569018380684, 0.0072578579934551015, 0.004941237909839778, 0.0029834635305878076, 0.0013487829662939248] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x180_gaussian_I_wf_qubit2": {
            "type": "arbitrary",
            "samples": [0.0, 0.0013487829662939248, 0.0029834635305878076, 0.004941237909839778, 0.0072578579934551015, 0.00996569018380684, 0.013091497820654437, 0.016654029341753772, 0.0206615278002724, 0.025109308094492595, 0.02997757267874069, 0.035229650968230525, 0.04081084883592647, 0.046648080053314674, 0.05265042002594503, 0.058710674095939365, 0.06470799020836852, 0.07051147285766579, 0.07598467752555374, 0.08099078901901928, 0.08539822044608465, 0.08908631899519925, 0.09195083610639947, 0.09390881711988835] + [0.09490259075122315] * 2 + [0.09390881711988835, 0.09195083610639947, 0.08908631899519925, 0.08539822044608465, 0.08099078901901928, 0.07598467752555374, 0.07051147285766579, 0.06470799020836852, 0.058710674095939365, 0.05265042002594503, 0.046648080053314674, 0.04081084883592647, 0.035229650968230525, 0.02997757267874069, 0.025109308094492595, 0.0206615278002724, 0.016654029341753772, 0.013091497820654437, 0.00996569018380684, 0.0072578579934551015, 0.004941237909839778, 0.0029834635305878076, 0.0013487829662939248] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x180_gaussian_I_wf_qubit3": {
            "type": "arbitrary",
            "samples": [0.0, 0.0013487829662939248, 0.0029834635305878076, 0.004941237909839778, 0.0072578579934551015, 0.00996569018380684, 0.013091497820654437, 0.016654029341753772, 0.0206615278002724, 0.025109308094492595, 0.02997757267874069, 0.035229650968230525, 0.04081084883592647, 0.046648080053314674, 0.05265042002594503, 0.058710674095939365, 0.06470799020836852, 0.07051147285766579, 0.07598467752555374, 0.08099078901901928, 0.08539822044608465, 0.08908631899519925, 0.09195083610639947, 0.09390881711988835] + [0.09490259075122315] * 2 + [0.09390881711988835, 0.09195083610639947, 0.08908631899519925, 0.08539822044608465, 0.08099078901901928, 0.07598467752555374, 0.07051147285766579, 0.06470799020836852, 0.058710674095939365, 0.05265042002594503, 0.046648080053314674, 0.04081084883592647, 0.035229650968230525, 0.02997757267874069, 0.025109308094492595, 0.0206615278002724, 0.016654029341753772, 0.013091497820654437, 0.00996569018380684, 0.0072578579934551015, 0.004941237909839778, 0.0029834635305878076, 0.0013487829662939248] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x180_gaussian_I_wf_qubit4": {
            "type": "arbitrary",
            "samples": [0.0, 0.0013487829662939248, 0.0029834635305878076, 0.004941237909839778, 0.0072578579934551015, 0.00996569018380684, 0.013091497820654437, 0.016654029341753772, 0.0206615278002724, 0.025109308094492595, 0.02997757267874069, 0.035229650968230525, 0.04081084883592647, 0.046648080053314674, 0.05265042002594503, 0.058710674095939365, 0.06470799020836852, 0.07051147285766579, 0.07598467752555374, 0.08099078901901928, 0.08539822044608465, 0.08908631899519925, 0.09195083610639947, 0.09390881711988835] + [0.09490259075122315] * 2 + [0.09390881711988835, 0.09195083610639947, 0.08908631899519925, 0.08539822044608465, 0.08099078901901928, 0.07598467752555374, 0.07051147285766579, 0.06470799020836852, 0.058710674095939365, 0.05265042002594503, 0.046648080053314674, 0.04081084883592647, 0.035229650968230525, 0.02997757267874069, 0.025109308094492595, 0.0206615278002724, 0.016654029341753772, 0.013091497820654437, 0.00996569018380684, 0.0072578579934551015, 0.004941237909839778, 0.0029834635305878076, 0.0013487829662939248] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x180_gaussian_I_wf_qubit5": {
            "type": "arbitrary",
            "samples": [0.0, 0.0013487829662939248, 0.0029834635305878076, 0.004941237909839778, 0.0072578579934551015, 0.00996569018380684, 0.013091497820654437, 0.016654029341753772, 0.0206615278002724, 0.025109308094492595, 0.02997757267874069, 0.035229650968230525, 0.04081084883592647, 0.046648080053314674, 0.05265042002594503, 0.058710674095939365, 0.06470799020836852, 0.07051147285766579, 0.07598467752555374, 0.08099078901901928, 0.08539822044608465, 0.08908631899519925, 0.09195083610639947, 0.09390881711988835] + [0.09490259075122315] * 2 + [0.09390881711988835, 0.09195083610639947, 0.08908631899519925, 0.08539822044608465, 0.08099078901901928, 0.07598467752555374, 0.07051147285766579, 0.06470799020836852, 0.058710674095939365, 0.05265042002594503, 0.046648080053314674, 0.04081084883592647, 0.035229650968230525, 0.02997757267874069, 0.025109308094492595, 0.0206615278002724, 0.016654029341753772, 0.013091497820654437, 0.00996569018380684, 0.0072578579934551015, 0.004941237909839778, 0.0029834635305878076, 0.0013487829662939248] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x180_gaussian_Q_wf_qubit1": {
            "type": "arbitrary",
            "samples": [0.0] * 52,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x180_gaussian_Q_wf_qubit2": {
            "type": "arbitrary",
            "samples": [0.0] * 52,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x180_gaussian_Q_wf_qubit3": {
            "type": "arbitrary",
            "samples": [0.0] * 52,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x180_gaussian_Q_wf_qubit4": {
            "type": "arbitrary",
            "samples": [0.0] * 52,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x180_gaussian_Q_wf_qubit5": {
            "type": "arbitrary",
            "samples": [0.0] * 52,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x90_gaussian_I_wf_qubit1": {
            "type": "arbitrary",
            "samples": [0.0, 0.0006743914831469624, 0.0014917317652939038, 0.002470618954919889, 0.0036289289967275508, 0.00498284509190342, 0.006545748910327219, 0.008327014670876886, 0.0103307639001362, 0.012554654047246297, 0.014988786339370345, 0.017614825484115262, 0.020405424417963235, 0.023324040026657337, 0.026325210012972514, 0.029355337047969682, 0.03235399510418426, 0.035255736428832896, 0.03799233876277687, 0.04049539450950964, 0.042699110223042326, 0.04454315949759963, 0.04597541805319973, 0.04695440855994418] + [0.047451295375611574] * 2 + [0.04695440855994418, 0.04597541805319973, 0.04454315949759963, 0.042699110223042326, 0.04049539450950964, 0.03799233876277687, 0.035255736428832896, 0.03235399510418426, 0.029355337047969682, 0.026325210012972514, 0.023324040026657337, 0.020405424417963235, 0.017614825484115262, 0.014988786339370345, 0.012554654047246297, 0.0103307639001362, 0.008327014670876886, 0.006545748910327219, 0.00498284509190342, 0.0036289289967275508, 0.002470618954919889, 0.0014917317652939038, 0.0006743914831469624] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x90_gaussian_I_wf_qubit2": {
            "type": "arbitrary",
            "samples": [0.0, 0.0006743914831469624, 0.0014917317652939038, 0.002470618954919889, 0.0036289289967275508, 0.00498284509190342, 0.006545748910327219, 0.008327014670876886, 0.0103307639001362, 0.012554654047246297, 0.014988786339370345, 0.017614825484115262, 0.020405424417963235, 0.023324040026657337, 0.026325210012972514, 0.029355337047969682, 0.03235399510418426, 0.035255736428832896, 0.03799233876277687, 0.04049539450950964, 0.042699110223042326, 0.04454315949759963, 0.04597541805319973, 0.04695440855994418] + [0.047451295375611574] * 2 + [0.04695440855994418, 0.04597541805319973, 0.04454315949759963, 0.042699110223042326, 0.04049539450950964, 0.03799233876277687, 0.035255736428832896, 0.03235399510418426, 0.029355337047969682, 0.026325210012972514, 0.023324040026657337, 0.020405424417963235, 0.017614825484115262, 0.014988786339370345, 0.012554654047246297, 0.0103307639001362, 0.008327014670876886, 0.006545748910327219, 0.00498284509190342, 0.0036289289967275508, 0.002470618954919889, 0.0014917317652939038, 0.0006743914831469624] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x90_gaussian_I_wf_qubit3": {
            "type": "arbitrary",
            "samples": [0.0, 0.0006743914831469624, 0.0014917317652939038, 0.002470618954919889, 0.0036289289967275508, 0.00498284509190342, 0.006545748910327219, 0.008327014670876886, 0.0103307639001362, 0.012554654047246297, 0.014988786339370345, 0.017614825484115262, 0.020405424417963235, 0.023324040026657337, 0.026325210012972514, 0.029355337047969682, 0.03235399510418426, 0.035255736428832896, 0.03799233876277687, 0.04049539450950964, 0.042699110223042326, 0.04454315949759963, 0.04597541805319973, 0.04695440855994418] + [0.047451295375611574] * 2 + [0.04695440855994418, 0.04597541805319973, 0.04454315949759963, 0.042699110223042326, 0.04049539450950964, 0.03799233876277687, 0.035255736428832896, 0.03235399510418426, 0.029355337047969682, 0.026325210012972514, 0.023324040026657337, 0.020405424417963235, 0.017614825484115262, 0.014988786339370345, 0.012554654047246297, 0.0103307639001362, 0.008327014670876886, 0.006545748910327219, 0.00498284509190342, 0.0036289289967275508, 0.002470618954919889, 0.0014917317652939038, 0.0006743914831469624] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x90_gaussian_I_wf_qubit4": {
            "type": "arbitrary",
            "samples": [0.0, 0.0006743914831469624, 0.0014917317652939038, 0.002470618954919889, 0.0036289289967275508, 0.00498284509190342, 0.006545748910327219, 0.008327014670876886, 0.0103307639001362, 0.012554654047246297, 0.014988786339370345, 0.017614825484115262, 0.020405424417963235, 0.023324040026657337, 0.026325210012972514, 0.029355337047969682, 0.03235399510418426, 0.035255736428832896, 0.03799233876277687, 0.04049539450950964, 0.042699110223042326, 0.04454315949759963, 0.04597541805319973, 0.04695440855994418] + [0.047451295375611574] * 2 + [0.04695440855994418, 0.04597541805319973, 0.04454315949759963, 0.042699110223042326, 0.04049539450950964, 0.03799233876277687, 0.035255736428832896, 0.03235399510418426, 0.029355337047969682, 0.026325210012972514, 0.023324040026657337, 0.020405424417963235, 0.017614825484115262, 0.014988786339370345, 0.012554654047246297, 0.0103307639001362, 0.008327014670876886, 0.006545748910327219, 0.00498284509190342, 0.0036289289967275508, 0.002470618954919889, 0.0014917317652939038, 0.0006743914831469624] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x90_gaussian_I_wf_qubit5": {
            "type": "arbitrary",
            "samples": [0.0, 0.0006743914831469624, 0.0014917317652939038, 0.002470618954919889, 0.0036289289967275508, 0.00498284509190342, 0.006545748910327219, 0.008327014670876886, 0.0103307639001362, 0.012554654047246297, 0.014988786339370345, 0.017614825484115262, 0.020405424417963235, 0.023324040026657337, 0.026325210012972514, 0.029355337047969682, 0.03235399510418426, 0.035255736428832896, 0.03799233876277687, 0.04049539450950964, 0.042699110223042326, 0.04454315949759963, 0.04597541805319973, 0.04695440855994418] + [0.047451295375611574] * 2 + [0.04695440855994418, 0.04597541805319973, 0.04454315949759963, 0.042699110223042326, 0.04049539450950964, 0.03799233876277687, 0.035255736428832896, 0.03235399510418426, 0.029355337047969682, 0.026325210012972514, 0.023324040026657337, 0.020405424417963235, 0.017614825484115262, 0.014988786339370345, 0.012554654047246297, 0.0103307639001362, 0.008327014670876886, 0.006545748910327219, 0.00498284509190342, 0.0036289289967275508, 0.002470618954919889, 0.0014917317652939038, 0.0006743914831469624] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x90_gaussian_Q_wf_qubit1": {
            "type": "arbitrary",
            "samples": [0.0] * 52,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x90_gaussian_Q_wf_qubit2": {
            "type": "arbitrary",
            "samples": [0.0] * 52,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x90_gaussian_Q_wf_qubit3": {
            "type": "arbitrary",
            "samples": [0.0] * 52,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x90_gaussian_Q_wf_qubit4": {
            "type": "arbitrary",
            "samples": [0.0] * 52,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x90_gaussian_Q_wf_qubit5": {
            "type": "arbitrary",
            "samples": [0.0] * 52,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_x90_gaussian_I_wf_qubit1": {
            "type": "arbitrary",
            "samples": [0.0, -0.0006743914831469624, -0.0014917317652939038, -0.002470618954919889, -0.0036289289967275508, -0.00498284509190342, -0.006545748910327219, -0.008327014670876886, -0.0103307639001362, -0.012554654047246297, -0.014988786339370345, -0.017614825484115262, -0.020405424417963235, -0.023324040026657337, -0.026325210012972514, -0.029355337047969682, -0.03235399510418426, -0.035255736428832896, -0.03799233876277687, -0.04049539450950964, -0.042699110223042326, -0.04454315949759963, -0.04597541805319973, -0.04695440855994418] + [-0.047451295375611574] * 2 + [-0.04695440855994418, -0.04597541805319973, -0.04454315949759963, -0.042699110223042326, -0.04049539450950964, -0.03799233876277687, -0.035255736428832896, -0.03235399510418426, -0.029355337047969682, -0.026325210012972514, -0.023324040026657337, -0.020405424417963235, -0.017614825484115262, -0.014988786339370345, -0.012554654047246297, -0.0103307639001362, -0.008327014670876886, -0.006545748910327219, -0.00498284509190342, -0.0036289289967275508, -0.002470618954919889, -0.0014917317652939038, -0.0006743914831469624] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_x90_gaussian_I_wf_qubit2": {
            "type": "arbitrary",
            "samples": [0.0, -0.0006743914831469624, -0.0014917317652939038, -0.002470618954919889, -0.0036289289967275508, -0.00498284509190342, -0.006545748910327219, -0.008327014670876886, -0.0103307639001362, -0.012554654047246297, -0.014988786339370345, -0.017614825484115262, -0.020405424417963235, -0.023324040026657337, -0.026325210012972514, -0.029355337047969682, -0.03235399510418426, -0.035255736428832896, -0.03799233876277687, -0.04049539450950964, -0.042699110223042326, -0.04454315949759963, -0.04597541805319973, -0.04695440855994418] + [-0.047451295375611574] * 2 + [-0.04695440855994418, -0.04597541805319973, -0.04454315949759963, -0.042699110223042326, -0.04049539450950964, -0.03799233876277687, -0.035255736428832896, -0.03235399510418426, -0.029355337047969682, -0.026325210012972514, -0.023324040026657337, -0.020405424417963235, -0.017614825484115262, -0.014988786339370345, -0.012554654047246297, -0.0103307639001362, -0.008327014670876886, -0.006545748910327219, -0.00498284509190342, -0.0036289289967275508, -0.002470618954919889, -0.0014917317652939038, -0.0006743914831469624] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_x90_gaussian_I_wf_qubit3": {
            "type": "arbitrary",
            "samples": [0.0, -0.0006743914831469624, -0.0014917317652939038, -0.002470618954919889, -0.0036289289967275508, -0.00498284509190342, -0.006545748910327219, -0.008327014670876886, -0.0103307639001362, -0.012554654047246297, -0.014988786339370345, -0.017614825484115262, -0.020405424417963235, -0.023324040026657337, -0.026325210012972514, -0.029355337047969682, -0.03235399510418426, -0.035255736428832896, -0.03799233876277687, -0.04049539450950964, -0.042699110223042326, -0.04454315949759963, -0.04597541805319973, -0.04695440855994418] + [-0.047451295375611574] * 2 + [-0.04695440855994418, -0.04597541805319973, -0.04454315949759963, -0.042699110223042326, -0.04049539450950964, -0.03799233876277687, -0.035255736428832896, -0.03235399510418426, -0.029355337047969682, -0.026325210012972514, -0.023324040026657337, -0.020405424417963235, -0.017614825484115262, -0.014988786339370345, -0.012554654047246297, -0.0103307639001362, -0.008327014670876886, -0.006545748910327219, -0.00498284509190342, -0.0036289289967275508, -0.002470618954919889, -0.0014917317652939038, -0.0006743914831469624] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_x90_gaussian_I_wf_qubit4": {
            "type": "arbitrary",
            "samples": [0.0, -0.0006743914831469624, -0.0014917317652939038, -0.002470618954919889, -0.0036289289967275508, -0.00498284509190342, -0.006545748910327219, -0.008327014670876886, -0.0103307639001362, -0.012554654047246297, -0.014988786339370345, -0.017614825484115262, -0.020405424417963235, -0.023324040026657337, -0.026325210012972514, -0.029355337047969682, -0.03235399510418426, -0.035255736428832896, -0.03799233876277687, -0.04049539450950964, -0.042699110223042326, -0.04454315949759963, -0.04597541805319973, -0.04695440855994418] + [-0.047451295375611574] * 2 + [-0.04695440855994418, -0.04597541805319973, -0.04454315949759963, -0.042699110223042326, -0.04049539450950964, -0.03799233876277687, -0.035255736428832896, -0.03235399510418426, -0.029355337047969682, -0.026325210012972514, -0.023324040026657337, -0.020405424417963235, -0.017614825484115262, -0.014988786339370345, -0.012554654047246297, -0.0103307639001362, -0.008327014670876886, -0.006545748910327219, -0.00498284509190342, -0.0036289289967275508, -0.002470618954919889, -0.0014917317652939038, -0.0006743914831469624] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_x90_gaussian_I_wf_qubit5": {
            "type": "arbitrary",
            "samples": [0.0, -0.0006743914831469624, -0.0014917317652939038, -0.002470618954919889, -0.0036289289967275508, -0.00498284509190342, -0.006545748910327219, -0.008327014670876886, -0.0103307639001362, -0.012554654047246297, -0.014988786339370345, -0.017614825484115262, -0.020405424417963235, -0.023324040026657337, -0.026325210012972514, -0.029355337047969682, -0.03235399510418426, -0.035255736428832896, -0.03799233876277687, -0.04049539450950964, -0.042699110223042326, -0.04454315949759963, -0.04597541805319973, -0.04695440855994418] + [-0.047451295375611574] * 2 + [-0.04695440855994418, -0.04597541805319973, -0.04454315949759963, -0.042699110223042326, -0.04049539450950964, -0.03799233876277687, -0.035255736428832896, -0.03235399510418426, -0.029355337047969682, -0.026325210012972514, -0.023324040026657337, -0.020405424417963235, -0.017614825484115262, -0.014988786339370345, -0.012554654047246297, -0.0103307639001362, -0.008327014670876886, -0.006545748910327219, -0.00498284509190342, -0.0036289289967275508, -0.002470618954919889, -0.0014917317652939038, -0.0006743914831469624] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_x90_gaussian_Q_wf_qubit1": {
            "type": "arbitrary",
            "samples": [0.0] * 52,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_x90_gaussian_Q_wf_qubit2": {
            "type": "arbitrary",
            "samples": [0.0] * 52,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_x90_gaussian_Q_wf_qubit3": {
            "type": "arbitrary",
            "samples": [0.0] * 52,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_x90_gaussian_Q_wf_qubit4": {
            "type": "arbitrary",
            "samples": [0.0] * 52,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_x90_gaussian_Q_wf_qubit5": {
            "type": "arbitrary",
            "samples": [0.0] * 52,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y180_gaussian_I_wf_qubit1": {
            "type": "arbitrary",
            "samples": [-0.0] * 52,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y180_gaussian_I_wf_qubit2": {
            "type": "arbitrary",
            "samples": [-0.0] * 52,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y180_gaussian_I_wf_qubit3": {
            "type": "arbitrary",
            "samples": [-0.0] * 52,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y180_gaussian_I_wf_qubit4": {
            "type": "arbitrary",
            "samples": [-0.0] * 52,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y180_gaussian_I_wf_qubit5": {
            "type": "arbitrary",
            "samples": [-0.0] * 52,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y180_gaussian_Q_wf_qubit1": {
            "type": "arbitrary",
            "samples": [0.0, 0.0013487829662939248, 0.0029834635305878076, 0.004941237909839778, 0.0072578579934551015, 0.00996569018380684, 0.013091497820654437, 0.016654029341753772, 0.0206615278002724, 0.025109308094492595, 0.02997757267874069, 0.035229650968230525, 0.04081084883592647, 0.046648080053314674, 0.05265042002594503, 0.058710674095939365, 0.06470799020836852, 0.07051147285766579, 0.07598467752555374, 0.08099078901901928, 0.08539822044608465, 0.08908631899519925, 0.09195083610639947, 0.09390881711988835] + [0.09490259075122315] * 2 + [0.09390881711988835, 0.09195083610639947, 0.08908631899519925, 0.08539822044608465, 0.08099078901901928, 0.07598467752555374, 0.07051147285766579, 0.06470799020836852, 0.058710674095939365, 0.05265042002594503, 0.046648080053314674, 0.04081084883592647, 0.035229650968230525, 0.02997757267874069, 0.025109308094492595, 0.0206615278002724, 0.016654029341753772, 0.013091497820654437, 0.00996569018380684, 0.0072578579934551015, 0.004941237909839778, 0.0029834635305878076, 0.0013487829662939248] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y180_gaussian_Q_wf_qubit2": {
            "type": "arbitrary",
            "samples": [0.0, 0.0013487829662939248, 0.0029834635305878076, 0.004941237909839778, 0.0072578579934551015, 0.00996569018380684, 0.013091497820654437, 0.016654029341753772, 0.0206615278002724, 0.025109308094492595, 0.02997757267874069, 0.035229650968230525, 0.04081084883592647, 0.046648080053314674, 0.05265042002594503, 0.058710674095939365, 0.06470799020836852, 0.07051147285766579, 0.07598467752555374, 0.08099078901901928, 0.08539822044608465, 0.08908631899519925, 0.09195083610639947, 0.09390881711988835] + [0.09490259075122315] * 2 + [0.09390881711988835, 0.09195083610639947, 0.08908631899519925, 0.08539822044608465, 0.08099078901901928, 0.07598467752555374, 0.07051147285766579, 0.06470799020836852, 0.058710674095939365, 0.05265042002594503, 0.046648080053314674, 0.04081084883592647, 0.035229650968230525, 0.02997757267874069, 0.025109308094492595, 0.0206615278002724, 0.016654029341753772, 0.013091497820654437, 0.00996569018380684, 0.0072578579934551015, 0.004941237909839778, 0.0029834635305878076, 0.0013487829662939248] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y180_gaussian_Q_wf_qubit3": {
            "type": "arbitrary",
            "samples": [0.0, 0.0013487829662939248, 0.0029834635305878076, 0.004941237909839778, 0.0072578579934551015, 0.00996569018380684, 0.013091497820654437, 0.016654029341753772, 0.0206615278002724, 0.025109308094492595, 0.02997757267874069, 0.035229650968230525, 0.04081084883592647, 0.046648080053314674, 0.05265042002594503, 0.058710674095939365, 0.06470799020836852, 0.07051147285766579, 0.07598467752555374, 0.08099078901901928, 0.08539822044608465, 0.08908631899519925, 0.09195083610639947, 0.09390881711988835] + [0.09490259075122315] * 2 + [0.09390881711988835, 0.09195083610639947, 0.08908631899519925, 0.08539822044608465, 0.08099078901901928, 0.07598467752555374, 0.07051147285766579, 0.06470799020836852, 0.058710674095939365, 0.05265042002594503, 0.046648080053314674, 0.04081084883592647, 0.035229650968230525, 0.02997757267874069, 0.025109308094492595, 0.0206615278002724, 0.016654029341753772, 0.013091497820654437, 0.00996569018380684, 0.0072578579934551015, 0.004941237909839778, 0.0029834635305878076, 0.0013487829662939248] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y180_gaussian_Q_wf_qubit4": {
            "type": "arbitrary",
            "samples": [0.0, 0.0013487829662939248, 0.0029834635305878076, 0.004941237909839778, 0.0072578579934551015, 0.00996569018380684, 0.013091497820654437, 0.016654029341753772, 0.0206615278002724, 0.025109308094492595, 0.02997757267874069, 0.035229650968230525, 0.04081084883592647, 0.046648080053314674, 0.05265042002594503, 0.058710674095939365, 0.06470799020836852, 0.07051147285766579, 0.07598467752555374, 0.08099078901901928, 0.08539822044608465, 0.08908631899519925, 0.09195083610639947, 0.09390881711988835] + [0.09490259075122315] * 2 + [0.09390881711988835, 0.09195083610639947, 0.08908631899519925, 0.08539822044608465, 0.08099078901901928, 0.07598467752555374, 0.07051147285766579, 0.06470799020836852, 0.058710674095939365, 0.05265042002594503, 0.046648080053314674, 0.04081084883592647, 0.035229650968230525, 0.02997757267874069, 0.025109308094492595, 0.0206615278002724, 0.016654029341753772, 0.013091497820654437, 0.00996569018380684, 0.0072578579934551015, 0.004941237909839778, 0.0029834635305878076, 0.0013487829662939248] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y180_gaussian_Q_wf_qubit5": {
            "type": "arbitrary",
            "samples": [0.0, 0.0013487829662939248, 0.0029834635305878076, 0.004941237909839778, 0.0072578579934551015, 0.00996569018380684, 0.013091497820654437, 0.016654029341753772, 0.0206615278002724, 0.025109308094492595, 0.02997757267874069, 0.035229650968230525, 0.04081084883592647, 0.046648080053314674, 0.05265042002594503, 0.058710674095939365, 0.06470799020836852, 0.07051147285766579, 0.07598467752555374, 0.08099078901901928, 0.08539822044608465, 0.08908631899519925, 0.09195083610639947, 0.09390881711988835] + [0.09490259075122315] * 2 + [0.09390881711988835, 0.09195083610639947, 0.08908631899519925, 0.08539822044608465, 0.08099078901901928, 0.07598467752555374, 0.07051147285766579, 0.06470799020836852, 0.058710674095939365, 0.05265042002594503, 0.046648080053314674, 0.04081084883592647, 0.035229650968230525, 0.02997757267874069, 0.025109308094492595, 0.0206615278002724, 0.016654029341753772, 0.013091497820654437, 0.00996569018380684, 0.0072578579934551015, 0.004941237909839778, 0.0029834635305878076, 0.0013487829662939248] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y90_gaussian_I_wf_qubit1": {
            "type": "arbitrary",
            "samples": [-0.0] * 52,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y90_gaussian_I_wf_qubit2": {
            "type": "arbitrary",
            "samples": [-0.0] * 52,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y90_gaussian_I_wf_qubit3": {
            "type": "arbitrary",
            "samples": [-0.0] * 52,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y90_gaussian_I_wf_qubit4": {
            "type": "arbitrary",
            "samples": [-0.0] * 52,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y90_gaussian_I_wf_qubit5": {
            "type": "arbitrary",
            "samples": [-0.0] * 52,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y90_gaussian_Q_wf_qubit1": {
            "type": "arbitrary",
            "samples": [0.0, 0.0006743914831469624, 0.0014917317652939038, 0.002470618954919889, 0.0036289289967275508, 0.00498284509190342, 0.006545748910327219, 0.008327014670876886, 0.0103307639001362, 0.012554654047246297, 0.014988786339370345, 0.017614825484115262, 0.020405424417963235, 0.023324040026657337, 0.026325210012972514, 0.029355337047969682, 0.03235399510418426, 0.035255736428832896, 0.03799233876277687, 0.04049539450950964, 0.042699110223042326, 0.04454315949759963, 0.04597541805319973, 0.04695440855994418] + [0.047451295375611574] * 2 + [0.04695440855994418, 0.04597541805319973, 0.04454315949759963, 0.042699110223042326, 0.04049539450950964, 0.03799233876277687, 0.035255736428832896, 0.03235399510418426, 0.029355337047969682, 0.026325210012972514, 0.023324040026657337, 0.020405424417963235, 0.017614825484115262, 0.014988786339370345, 0.012554654047246297, 0.0103307639001362, 0.008327014670876886, 0.006545748910327219, 0.00498284509190342, 0.0036289289967275508, 0.002470618954919889, 0.0014917317652939038, 0.0006743914831469624] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y90_gaussian_Q_wf_qubit2": {
            "type": "arbitrary",
            "samples": [0.0, 0.0006743914831469624, 0.0014917317652939038, 0.002470618954919889, 0.0036289289967275508, 0.00498284509190342, 0.006545748910327219, 0.008327014670876886, 0.0103307639001362, 0.012554654047246297, 0.014988786339370345, 0.017614825484115262, 0.020405424417963235, 0.023324040026657337, 0.026325210012972514, 0.029355337047969682, 0.03235399510418426, 0.035255736428832896, 0.03799233876277687, 0.04049539450950964, 0.042699110223042326, 0.04454315949759963, 0.04597541805319973, 0.04695440855994418] + [0.047451295375611574] * 2 + [0.04695440855994418, 0.04597541805319973, 0.04454315949759963, 0.042699110223042326, 0.04049539450950964, 0.03799233876277687, 0.035255736428832896, 0.03235399510418426, 0.029355337047969682, 0.026325210012972514, 0.023324040026657337, 0.020405424417963235, 0.017614825484115262, 0.014988786339370345, 0.012554654047246297, 0.0103307639001362, 0.008327014670876886, 0.006545748910327219, 0.00498284509190342, 0.0036289289967275508, 0.002470618954919889, 0.0014917317652939038, 0.0006743914831469624] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y90_gaussian_Q_wf_qubit3": {
            "type": "arbitrary",
            "samples": [0.0, 0.0006743914831469624, 0.0014917317652939038, 0.002470618954919889, 0.0036289289967275508, 0.00498284509190342, 0.006545748910327219, 0.008327014670876886, 0.0103307639001362, 0.012554654047246297, 0.014988786339370345, 0.017614825484115262, 0.020405424417963235, 0.023324040026657337, 0.026325210012972514, 0.029355337047969682, 0.03235399510418426, 0.035255736428832896, 0.03799233876277687, 0.04049539450950964, 0.042699110223042326, 0.04454315949759963, 0.04597541805319973, 0.04695440855994418] + [0.047451295375611574] * 2 + [0.04695440855994418, 0.04597541805319973, 0.04454315949759963, 0.042699110223042326, 0.04049539450950964, 0.03799233876277687, 0.035255736428832896, 0.03235399510418426, 0.029355337047969682, 0.026325210012972514, 0.023324040026657337, 0.020405424417963235, 0.017614825484115262, 0.014988786339370345, 0.012554654047246297, 0.0103307639001362, 0.008327014670876886, 0.006545748910327219, 0.00498284509190342, 0.0036289289967275508, 0.002470618954919889, 0.0014917317652939038, 0.0006743914831469624] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y90_gaussian_Q_wf_qubit4": {
            "type": "arbitrary",
            "samples": [0.0, 0.0006743914831469624, 0.0014917317652939038, 0.002470618954919889, 0.0036289289967275508, 0.00498284509190342, 0.006545748910327219, 0.008327014670876886, 0.0103307639001362, 0.012554654047246297, 0.014988786339370345, 0.017614825484115262, 0.020405424417963235, 0.023324040026657337, 0.026325210012972514, 0.029355337047969682, 0.03235399510418426, 0.035255736428832896, 0.03799233876277687, 0.04049539450950964, 0.042699110223042326, 0.04454315949759963, 0.04597541805319973, 0.04695440855994418] + [0.047451295375611574] * 2 + [0.04695440855994418, 0.04597541805319973, 0.04454315949759963, 0.042699110223042326, 0.04049539450950964, 0.03799233876277687, 0.035255736428832896, 0.03235399510418426, 0.029355337047969682, 0.026325210012972514, 0.023324040026657337, 0.020405424417963235, 0.017614825484115262, 0.014988786339370345, 0.012554654047246297, 0.0103307639001362, 0.008327014670876886, 0.006545748910327219, 0.00498284509190342, 0.0036289289967275508, 0.002470618954919889, 0.0014917317652939038, 0.0006743914831469624] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y90_gaussian_Q_wf_qubit5": {
            "type": "arbitrary",
            "samples": [0.0, 0.0006743914831469624, 0.0014917317652939038, 0.002470618954919889, 0.0036289289967275508, 0.00498284509190342, 0.006545748910327219, 0.008327014670876886, 0.0103307639001362, 0.012554654047246297, 0.014988786339370345, 0.017614825484115262, 0.020405424417963235, 0.023324040026657337, 0.026325210012972514, 0.029355337047969682, 0.03235399510418426, 0.035255736428832896, 0.03799233876277687, 0.04049539450950964, 0.042699110223042326, 0.04454315949759963, 0.04597541805319973, 0.04695440855994418] + [0.047451295375611574] * 2 + [0.04695440855994418, 0.04597541805319973, 0.04454315949759963, 0.042699110223042326, 0.04049539450950964, 0.03799233876277687, 0.035255736428832896, 0.03235399510418426, 0.029355337047969682, 0.026325210012972514, 0.023324040026657337, 0.020405424417963235, 0.017614825484115262, 0.014988786339370345, 0.012554654047246297, 0.0103307639001362, 0.008327014670876886, 0.006545748910327219, 0.00498284509190342, 0.0036289289967275508, 0.002470618954919889, 0.0014917317652939038, 0.0006743914831469624] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_y90_gaussian_I_wf_qubit1": {
            "type": "arbitrary",
            "samples": [-0.0] * 52,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_y90_gaussian_I_wf_qubit2": {
            "type": "arbitrary",
            "samples": [-0.0] * 52,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_y90_gaussian_I_wf_qubit3": {
            "type": "arbitrary",
            "samples": [-0.0] * 52,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_y90_gaussian_I_wf_qubit4": {
            "type": "arbitrary",
            "samples": [-0.0] * 52,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_y90_gaussian_I_wf_qubit5": {
            "type": "arbitrary",
            "samples": [-0.0] * 52,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_y90_gaussian_Q_wf_qubit1": {
            "type": "arbitrary",
            "samples": [0.0, -0.0006743914831469624, -0.0014917317652939038, -0.002470618954919889, -0.0036289289967275508, -0.00498284509190342, -0.006545748910327219, -0.008327014670876886, -0.0103307639001362, -0.012554654047246297, -0.014988786339370345, -0.017614825484115262, -0.020405424417963235, -0.023324040026657337, -0.026325210012972514, -0.029355337047969682, -0.03235399510418426, -0.035255736428832896, -0.03799233876277687, -0.04049539450950964, -0.042699110223042326, -0.04454315949759963, -0.04597541805319973, -0.04695440855994418] + [-0.047451295375611574] * 2 + [-0.04695440855994418, -0.04597541805319973, -0.04454315949759963, -0.042699110223042326, -0.04049539450950964, -0.03799233876277687, -0.035255736428832896, -0.03235399510418426, -0.029355337047969682, -0.026325210012972514, -0.023324040026657337, -0.020405424417963235, -0.017614825484115262, -0.014988786339370345, -0.012554654047246297, -0.0103307639001362, -0.008327014670876886, -0.006545748910327219, -0.00498284509190342, -0.0036289289967275508, -0.002470618954919889, -0.0014917317652939038, -0.0006743914831469624] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_y90_gaussian_Q_wf_qubit2": {
            "type": "arbitrary",
            "samples": [0.0, -0.0006743914831469624, -0.0014917317652939038, -0.002470618954919889, -0.0036289289967275508, -0.00498284509190342, -0.006545748910327219, -0.008327014670876886, -0.0103307639001362, -0.012554654047246297, -0.014988786339370345, -0.017614825484115262, -0.020405424417963235, -0.023324040026657337, -0.026325210012972514, -0.029355337047969682, -0.03235399510418426, -0.035255736428832896, -0.03799233876277687, -0.04049539450950964, -0.042699110223042326, -0.04454315949759963, -0.04597541805319973, -0.04695440855994418] + [-0.047451295375611574] * 2 + [-0.04695440855994418, -0.04597541805319973, -0.04454315949759963, -0.042699110223042326, -0.04049539450950964, -0.03799233876277687, -0.035255736428832896, -0.03235399510418426, -0.029355337047969682, -0.026325210012972514, -0.023324040026657337, -0.020405424417963235, -0.017614825484115262, -0.014988786339370345, -0.012554654047246297, -0.0103307639001362, -0.008327014670876886, -0.006545748910327219, -0.00498284509190342, -0.0036289289967275508, -0.002470618954919889, -0.0014917317652939038, -0.0006743914831469624] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_y90_gaussian_Q_wf_qubit3": {
            "type": "arbitrary",
            "samples": [0.0, -0.0006743914831469624, -0.0014917317652939038, -0.002470618954919889, -0.0036289289967275508, -0.00498284509190342, -0.006545748910327219, -0.008327014670876886, -0.0103307639001362, -0.012554654047246297, -0.014988786339370345, -0.017614825484115262, -0.020405424417963235, -0.023324040026657337, -0.026325210012972514, -0.029355337047969682, -0.03235399510418426, -0.035255736428832896, -0.03799233876277687, -0.04049539450950964, -0.042699110223042326, -0.04454315949759963, -0.04597541805319973, -0.04695440855994418] + [-0.047451295375611574] * 2 + [-0.04695440855994418, -0.04597541805319973, -0.04454315949759963, -0.042699110223042326, -0.04049539450950964, -0.03799233876277687, -0.035255736428832896, -0.03235399510418426, -0.029355337047969682, -0.026325210012972514, -0.023324040026657337, -0.020405424417963235, -0.017614825484115262, -0.014988786339370345, -0.012554654047246297, -0.0103307639001362, -0.008327014670876886, -0.006545748910327219, -0.00498284509190342, -0.0036289289967275508, -0.002470618954919889, -0.0014917317652939038, -0.0006743914831469624] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_y90_gaussian_Q_wf_qubit4": {
            "type": "arbitrary",
            "samples": [0.0, -0.0006743914831469624, -0.0014917317652939038, -0.002470618954919889, -0.0036289289967275508, -0.00498284509190342, -0.006545748910327219, -0.008327014670876886, -0.0103307639001362, -0.012554654047246297, -0.014988786339370345, -0.017614825484115262, -0.020405424417963235, -0.023324040026657337, -0.026325210012972514, -0.029355337047969682, -0.03235399510418426, -0.035255736428832896, -0.03799233876277687, -0.04049539450950964, -0.042699110223042326, -0.04454315949759963, -0.04597541805319973, -0.04695440855994418] + [-0.047451295375611574] * 2 + [-0.04695440855994418, -0.04597541805319973, -0.04454315949759963, -0.042699110223042326, -0.04049539450950964, -0.03799233876277687, -0.035255736428832896, -0.03235399510418426, -0.029355337047969682, -0.026325210012972514, -0.023324040026657337, -0.020405424417963235, -0.017614825484115262, -0.014988786339370345, -0.012554654047246297, -0.0103307639001362, -0.008327014670876886, -0.006545748910327219, -0.00498284509190342, -0.0036289289967275508, -0.002470618954919889, -0.0014917317652939038, -0.0006743914831469624] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_y90_gaussian_Q_wf_qubit5": {
            "type": "arbitrary",
            "samples": [0.0, -0.0006743914831469624, -0.0014917317652939038, -0.002470618954919889, -0.0036289289967275508, -0.00498284509190342, -0.006545748910327219, -0.008327014670876886, -0.0103307639001362, -0.012554654047246297, -0.014988786339370345, -0.017614825484115262, -0.020405424417963235, -0.023324040026657337, -0.026325210012972514, -0.029355337047969682, -0.03235399510418426, -0.035255736428832896, -0.03799233876277687, -0.04049539450950964, -0.042699110223042326, -0.04454315949759963, -0.04597541805319973, -0.04695440855994418] + [-0.047451295375611574] * 2 + [-0.04695440855994418, -0.04597541805319973, -0.04454315949759963, -0.042699110223042326, -0.04049539450950964, -0.03799233876277687, -0.035255736428832896, -0.03235399510418426, -0.029355337047969682, -0.026325210012972514, -0.023324040026657337, -0.020405424417963235, -0.017614825484115262, -0.014988786339370345, -0.012554654047246297, -0.0103307639001362, -0.008327014670876886, -0.006545748910327219, -0.00498284509190342, -0.0036289289967275508, -0.002470618954919889, -0.0014917317652939038, -0.0006743914831469624] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x180_gaussian_I_wf_qp_control_c3t2": {
            "type": "arbitrary",
            "samples": [0.0, 0.000623059395668357, 0.0013134158229892211, 0.00207600456516317, 0.0029157968026681785, 0.003837749297415329, 0.004846747956223626, 0.0059475454464649755, 0.007144693172446949, 0.008442468066474543, 0.00984479480112677, 0.01135516418617893, 0.012976548671420715, 0.014711316031583668, 0.016561142457583073, 0.01852692641493371, 0.020608704751007553, 0.02280557263323139, 0.02511560897595016, 0.027535809060335543, 0.03006202606562717, 0.03268892320793267, 0.035409938122250045, 0.038217261022609625, 0.04110182803350147, 0.04405333090334345, 0.04706024408905373, 0.05010986994237358, 0.05318840243716088, 0.05628100955729227, 0.059371934122988815, 0.06244461247619, 0.06548181008073263, 0.06846577272886803, 0.07137839169082312, 0.07420138080762224, 0.07691646321812151, 0.07950556513773178, 0.08195101387660032, 0.08423573710622746, 0.08634346026167618, 0.08825889890645858, 0.08996794289214834, 0.09145782921645602, 0.09271730062188518, 0.09373674718038912, 0.09450832837415593, 0.09502607350358355] + [0.09528595862392984] * 2 + [0.09502607350358355, 0.09450832837415593, 0.09373674718038912, 0.09271730062188518, 0.09145782921645602, 0.08996794289214834, 0.08825889890645858, 0.08634346026167618, 0.08423573710622746, 0.08195101387660032, 0.07950556513773178, 0.07691646321812151, 0.07420138080762224, 0.07137839169082312, 0.06846577272886803, 0.06548181008073263, 0.06244461247619, 0.059371934122988815, 0.05628100955729227, 0.05318840243716088, 0.05010986994237358, 0.04706024408905373, 0.04405333090334345, 0.04110182803350147, 0.038217261022609625, 0.035409938122250045, 0.03268892320793267, 0.03006202606562717, 0.027535809060335543, 0.02511560897595016, 0.02280557263323139, 0.020608704751007553, 0.01852692641493371, 0.016561142457583073, 0.014711316031583668, 0.012976548671420715, 0.01135516418617893, 0.00984479480112677, 0.008442468066474543, 0.007144693172446949, 0.0059475454464649755, 0.004846747956223626, 0.003837749297415329, 0.0029157968026681785, 0.00207600456516317, 0.0013134158229892211, 0.000623059395668357] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x180_gaussian_Q_wf_qp_control_c3t2": {
            "type": "arbitrary",
            "samples": [0.0] * 100,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x90_gaussian_I_wf_qp_control_c3t2": {
            "type": "arbitrary",
            "samples": [0.0, 0.0003115296978341785, 0.0006567079114946106, 0.001038002282581585, 0.0014578984013340892, 0.0019188746487076645, 0.002423373978111813, 0.0029737727232324877, 0.0035723465862234744, 0.004221234033237271, 0.004922397400563385, 0.005677582093089465, 0.0064882743357103576, 0.007355658015791834, 0.008280571228791537, 0.009263463207466856, 0.010304352375503777, 0.011402786316615695, 0.01255780448797508, 0.013767904530167772, 0.015031013032813585, 0.016344461603966336, 0.017704969061125023, 0.019108630511304812, 0.020550914016750736, 0.022026665451671725, 0.023530122044526865, 0.02505493497118679, 0.02659420121858044, 0.028140504778646134, 0.029685967061494407, 0.031222306238095, 0.032740905040366315, 0.034232886364434015, 0.03568919584541156, 0.03710069040381112, 0.038458231609060756, 0.03975278256886589, 0.04097550693830016, 0.04211786855311373, 0.04317173013083809, 0.04412944945322929, 0.04498397144607417, 0.04572891460822801, 0.04635865031094259, 0.04686837359019456, 0.047254164187077966, 0.047513036751791776] + [0.04764297931196492] * 2 + [0.047513036751791776, 0.047254164187077966, 0.04686837359019456, 0.04635865031094259, 0.04572891460822801, 0.04498397144607417, 0.04412944945322929, 0.04317173013083809, 0.04211786855311373, 0.04097550693830016, 0.03975278256886589, 0.038458231609060756, 0.03710069040381112, 0.03568919584541156, 0.034232886364434015, 0.032740905040366315, 0.031222306238095, 0.029685967061494407, 0.028140504778646134, 0.02659420121858044, 0.02505493497118679, 0.023530122044526865, 0.022026665451671725, 0.020550914016750736, 0.019108630511304812, 0.017704969061125023, 0.016344461603966336, 0.015031013032813585, 0.013767904530167772, 0.01255780448797508, 0.011402786316615695, 0.010304352375503777, 0.009263463207466856, 0.008280571228791537, 0.007355658015791834, 0.0064882743357103576, 0.005677582093089465, 0.004922397400563385, 0.004221234033237271, 0.0035723465862234744, 0.0029737727232324877, 0.002423373978111813, 0.0019188746487076645, 0.0014578984013340892, 0.001038002282581585, 0.0006567079114946106, 0.0003115296978341785] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x90_gaussian_Q_wf_qp_control_c3t2": {
            "type": "arbitrary",
            "samples": [0.0] * 100,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_x90_gaussian_I_wf_qp_control_c3t2": {
            "type": "arbitrary",
            "samples": [0.0, -0.0003115296978341785, -0.0006567079114946106, -0.001038002282581585, -0.0014578984013340892, -0.0019188746487076645, -0.002423373978111813, -0.0029737727232324877, -0.0035723465862234744, -0.004221234033237271, -0.004922397400563385, -0.005677582093089465, -0.0064882743357103576, -0.007355658015791834, -0.008280571228791537, -0.009263463207466856, -0.010304352375503777, -0.011402786316615695, -0.01255780448797508, -0.013767904530167772, -0.015031013032813585, -0.016344461603966336, -0.017704969061125023, -0.019108630511304812, -0.020550914016750736, -0.022026665451671725, -0.023530122044526865, -0.02505493497118679, -0.02659420121858044, -0.028140504778646134, -0.029685967061494407, -0.031222306238095, -0.032740905040366315, -0.034232886364434015, -0.03568919584541156, -0.03710069040381112, -0.038458231609060756, -0.03975278256886589, -0.04097550693830016, -0.04211786855311373, -0.04317173013083809, -0.04412944945322929, -0.04498397144607417, -0.04572891460822801, -0.04635865031094259, -0.04686837359019456, -0.047254164187077966, -0.047513036751791776] + [-0.04764297931196492] * 2 + [-0.047513036751791776, -0.047254164187077966, -0.04686837359019456, -0.04635865031094259, -0.04572891460822801, -0.04498397144607417, -0.04412944945322929, -0.04317173013083809, -0.04211786855311373, -0.04097550693830016, -0.03975278256886589, -0.038458231609060756, -0.03710069040381112, -0.03568919584541156, -0.034232886364434015, -0.032740905040366315, -0.031222306238095, -0.029685967061494407, -0.028140504778646134, -0.02659420121858044, -0.02505493497118679, -0.023530122044526865, -0.022026665451671725, -0.020550914016750736, -0.019108630511304812, -0.017704969061125023, -0.016344461603966336, -0.015031013032813585, -0.013767904530167772, -0.01255780448797508, -0.011402786316615695, -0.010304352375503777, -0.009263463207466856, -0.008280571228791537, -0.007355658015791834, -0.0064882743357103576, -0.005677582093089465, -0.004922397400563385, -0.004221234033237271, -0.0035723465862234744, -0.0029737727232324877, -0.002423373978111813, -0.0019188746487076645, -0.0014578984013340892, -0.001038002282581585, -0.0006567079114946106, -0.0003115296978341785] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_x90_gaussian_Q_wf_qp_control_c3t2": {
            "type": "arbitrary",
            "samples": [0.0] * 100,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y180_gaussian_I_wf_qp_control_c3t2": {
            "type": "arbitrary",
            "samples": [-0.0] * 100,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y180_gaussian_Q_wf_qp_control_c3t2": {
            "type": "arbitrary",
            "samples": [0.0, 0.000623059395668357, 0.0013134158229892211, 0.00207600456516317, 0.0029157968026681785, 0.003837749297415329, 0.004846747956223626, 0.0059475454464649755, 0.007144693172446949, 0.008442468066474543, 0.00984479480112677, 0.01135516418617893, 0.012976548671420715, 0.014711316031583668, 0.016561142457583073, 0.01852692641493371, 0.020608704751007553, 0.02280557263323139, 0.02511560897595016, 0.027535809060335543, 0.03006202606562717, 0.03268892320793267, 0.035409938122250045, 0.038217261022609625, 0.04110182803350147, 0.04405333090334345, 0.04706024408905373, 0.05010986994237358, 0.05318840243716088, 0.05628100955729227, 0.059371934122988815, 0.06244461247619, 0.06548181008073263, 0.06846577272886803, 0.07137839169082312, 0.07420138080762224, 0.07691646321812151, 0.07950556513773178, 0.08195101387660032, 0.08423573710622746, 0.08634346026167618, 0.08825889890645858, 0.08996794289214834, 0.09145782921645602, 0.09271730062188518, 0.09373674718038912, 0.09450832837415593, 0.09502607350358355] + [0.09528595862392984] * 2 + [0.09502607350358355, 0.09450832837415593, 0.09373674718038912, 0.09271730062188518, 0.09145782921645602, 0.08996794289214834, 0.08825889890645858, 0.08634346026167618, 0.08423573710622746, 0.08195101387660032, 0.07950556513773178, 0.07691646321812151, 0.07420138080762224, 0.07137839169082312, 0.06846577272886803, 0.06548181008073263, 0.06244461247619, 0.059371934122988815, 0.05628100955729227, 0.05318840243716088, 0.05010986994237358, 0.04706024408905373, 0.04405333090334345, 0.04110182803350147, 0.038217261022609625, 0.035409938122250045, 0.03268892320793267, 0.03006202606562717, 0.027535809060335543, 0.02511560897595016, 0.02280557263323139, 0.020608704751007553, 0.01852692641493371, 0.016561142457583073, 0.014711316031583668, 0.012976548671420715, 0.01135516418617893, 0.00984479480112677, 0.008442468066474543, 0.007144693172446949, 0.0059475454464649755, 0.004846747956223626, 0.003837749297415329, 0.0029157968026681785, 0.00207600456516317, 0.0013134158229892211, 0.000623059395668357] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y90_gaussian_I_wf_qp_control_c3t2": {
            "type": "arbitrary",
            "samples": [-0.0] * 100,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y90_gaussian_Q_wf_qp_control_c3t2": {
            "type": "arbitrary",
            "samples": [0.0, 0.0003115296978341785, 0.0006567079114946106, 0.001038002282581585, 0.0014578984013340892, 0.0019188746487076645, 0.002423373978111813, 0.0029737727232324877, 0.0035723465862234744, 0.004221234033237271, 0.004922397400563385, 0.005677582093089465, 0.0064882743357103576, 0.007355658015791834, 0.008280571228791537, 0.009263463207466856, 0.010304352375503777, 0.011402786316615695, 0.01255780448797508, 0.013767904530167772, 0.015031013032813585, 0.016344461603966336, 0.017704969061125023, 0.019108630511304812, 0.020550914016750736, 0.022026665451671725, 0.023530122044526865, 0.02505493497118679, 0.02659420121858044, 0.028140504778646134, 0.029685967061494407, 0.031222306238095, 0.032740905040366315, 0.034232886364434015, 0.03568919584541156, 0.03710069040381112, 0.038458231609060756, 0.03975278256886589, 0.04097550693830016, 0.04211786855311373, 0.04317173013083809, 0.04412944945322929, 0.04498397144607417, 0.04572891460822801, 0.04635865031094259, 0.04686837359019456, 0.047254164187077966, 0.047513036751791776] + [0.04764297931196492] * 2 + [0.047513036751791776, 0.047254164187077966, 0.04686837359019456, 0.04635865031094259, 0.04572891460822801, 0.04498397144607417, 0.04412944945322929, 0.04317173013083809, 0.04211786855311373, 0.04097550693830016, 0.03975278256886589, 0.038458231609060756, 0.03710069040381112, 0.03568919584541156, 0.034232886364434015, 0.032740905040366315, 0.031222306238095, 0.029685967061494407, 0.028140504778646134, 0.02659420121858044, 0.02505493497118679, 0.023530122044526865, 0.022026665451671725, 0.020550914016750736, 0.019108630511304812, 0.017704969061125023, 0.016344461603966336, 0.015031013032813585, 0.013767904530167772, 0.01255780448797508, 0.011402786316615695, 0.010304352375503777, 0.009263463207466856, 0.008280571228791537, 0.007355658015791834, 0.0064882743357103576, 0.005677582093089465, 0.004922397400563385, 0.004221234033237271, 0.0035723465862234744, 0.0029737727232324877, 0.002423373978111813, 0.0019188746487076645, 0.0014578984013340892, 0.001038002282581585, 0.0006567079114946106, 0.0003115296978341785] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_y90_gaussian_I_wf_qp_control_c3t2": {
            "type": "arbitrary",
            "samples": [-0.0] * 100,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_y90_gaussian_Q_wf_qp_control_c3t2": {
            "type": "arbitrary",
            "samples": [0.0, -0.0003115296978341785, -0.0006567079114946106, -0.001038002282581585, -0.0014578984013340892, -0.0019188746487076645, -0.002423373978111813, -0.0029737727232324877, -0.0035723465862234744, -0.004221234033237271, -0.004922397400563385, -0.005677582093089465, -0.0064882743357103576, -0.007355658015791834, -0.008280571228791537, -0.009263463207466856, -0.010304352375503777, -0.011402786316615695, -0.01255780448797508, -0.013767904530167772, -0.015031013032813585, -0.016344461603966336, -0.017704969061125023, -0.019108630511304812, -0.020550914016750736, -0.022026665451671725, -0.023530122044526865, -0.02505493497118679, -0.02659420121858044, -0.028140504778646134, -0.029685967061494407, -0.031222306238095, -0.032740905040366315, -0.034232886364434015, -0.03568919584541156, -0.03710069040381112, -0.038458231609060756, -0.03975278256886589, -0.04097550693830016, -0.04211786855311373, -0.04317173013083809, -0.04412944945322929, -0.04498397144607417, -0.04572891460822801, -0.04635865031094259, -0.04686837359019456, -0.047254164187077966, -0.047513036751791776] + [-0.04764297931196492] * 2 + [-0.047513036751791776, -0.047254164187077966, -0.04686837359019456, -0.04635865031094259, -0.04572891460822801, -0.04498397144607417, -0.04412944945322929, -0.04317173013083809, -0.04211786855311373, -0.04097550693830016, -0.03975278256886589, -0.038458231609060756, -0.03710069040381112, -0.03568919584541156, -0.034232886364434015, -0.032740905040366315, -0.031222306238095, -0.029685967061494407, -0.028140504778646134, -0.02659420121858044, -0.02505493497118679, -0.023530122044526865, -0.022026665451671725, -0.020550914016750736, -0.019108630511304812, -0.017704969061125023, -0.016344461603966336, -0.015031013032813585, -0.013767904530167772, -0.01255780448797508, -0.011402786316615695, -0.010304352375503777, -0.009263463207466856, -0.008280571228791537, -0.007355658015791834, -0.0064882743357103576, -0.005677582093089465, -0.004922397400563385, -0.004221234033237271, -0.0035723465862234744, -0.0029737727232324877, -0.002423373978111813, -0.0019188746487076645, -0.0014578984013340892, -0.001038002282581585, -0.0006567079114946106, -0.0003115296978341785] + [0.0] * 3,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x180_kaiser_I_wf_qubit1": {
            "type": "arbitrary",
            "samples": [6.123359277961564e-05, 0.0002289064194538778, 0.000548783455455145, 0.0010885180985115382, 0.0019267409464745488, 0.003150008335112064, 0.004848352179230376, 0.007109572778290188, 0.010012557367687032, 0.013620038493738051, 0.01797131336312757, 0.023075514987624765, 0.02890604776283309, 0.03539676767322338, 0.042440399181746066, 0.049889541078795584, 0.05756043154530752, 0.06523943255657352, 0.07269197317209034, 0.07967347979444635, 0.08594163875116435, 0.09126920026585045, 0.09545645702431381, 0.0983425238802947] + [0.09981461034690563] * 2 + [0.0983425238802947, 0.09545645702431381, 0.09126920026585045, 0.08594163875116435, 0.07967347979444635, 0.07269197317209034, 0.06523943255657352, 0.05756043154530752, 0.049889541078795584, 0.042440399181746066, 0.03539676767322338, 0.02890604776283309, 0.023075514987624765, 0.01797131336312757, 0.013620038493738051, 0.010012557367687032, 0.007109572778290188, 0.004848352179230376, 0.003150008335112064, 0.0019267409464745488, 0.0010885180985115365, 0.0005487834554551463, 0.0002289064194538778, 6.123359277961564e-05] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x180_kaiser_I_wf_qubit2": {
            "type": "arbitrary",
            "samples": [6.123359277961564e-05, 0.0002289064194538778, 0.000548783455455145, 0.0010885180985115382, 0.0019267409464745488, 0.003150008335112064, 0.004848352179230376, 0.007109572778290188, 0.010012557367687032, 0.013620038493738051, 0.01797131336312757, 0.023075514987624765, 0.02890604776283309, 0.03539676767322338, 0.042440399181746066, 0.049889541078795584, 0.05756043154530752, 0.06523943255657352, 0.07269197317209034, 0.07967347979444635, 0.08594163875116435, 0.09126920026585045, 0.09545645702431381, 0.0983425238802947] + [0.09981461034690563] * 2 + [0.0983425238802947, 0.09545645702431381, 0.09126920026585045, 0.08594163875116435, 0.07967347979444635, 0.07269197317209034, 0.06523943255657352, 0.05756043154530752, 0.049889541078795584, 0.042440399181746066, 0.03539676767322338, 0.02890604776283309, 0.023075514987624765, 0.01797131336312757, 0.013620038493738051, 0.010012557367687032, 0.007109572778290188, 0.004848352179230376, 0.003150008335112064, 0.0019267409464745488, 0.0010885180985115365, 0.0005487834554551463, 0.0002289064194538778, 6.123359277961564e-05] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x180_kaiser_I_wf_qubit3": {
            "type": "arbitrary",
            "samples": [6.123359277961564e-05, 0.0002289064194538778, 0.000548783455455145, 0.0010885180985115382, 0.0019267409464745488, 0.003150008335112064, 0.004848352179230376, 0.007109572778290188, 0.010012557367687032, 0.013620038493738051, 0.01797131336312757, 0.023075514987624765, 0.02890604776283309, 0.03539676767322338, 0.042440399181746066, 0.049889541078795584, 0.05756043154530752, 0.06523943255657352, 0.07269197317209034, 0.07967347979444635, 0.08594163875116435, 0.09126920026585045, 0.09545645702431381, 0.0983425238802947] + [0.09981461034690563] * 2 + [0.0983425238802947, 0.09545645702431381, 0.09126920026585045, 0.08594163875116435, 0.07967347979444635, 0.07269197317209034, 0.06523943255657352, 0.05756043154530752, 0.049889541078795584, 0.042440399181746066, 0.03539676767322338, 0.02890604776283309, 0.023075514987624765, 0.01797131336312757, 0.013620038493738051, 0.010012557367687032, 0.007109572778290188, 0.004848352179230376, 0.003150008335112064, 0.0019267409464745488, 0.0010885180985115365, 0.0005487834554551463, 0.0002289064194538778, 6.123359277961564e-05] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x180_kaiser_I_wf_qubit4": {
            "type": "arbitrary",
            "samples": [6.123359277961564e-05, 0.0002289064194538778, 0.000548783455455145, 0.0010885180985115382, 0.0019267409464745488, 0.003150008335112064, 0.004848352179230376, 0.007109572778290188, 0.010012557367687032, 0.013620038493738051, 0.01797131336312757, 0.023075514987624765, 0.02890604776283309, 0.03539676767322338, 0.042440399181746066, 0.049889541078795584, 0.05756043154530752, 0.06523943255657352, 0.07269197317209034, 0.07967347979444635, 0.08594163875116435, 0.09126920026585045, 0.09545645702431381, 0.0983425238802947] + [0.09981461034690563] * 2 + [0.0983425238802947, 0.09545645702431381, 0.09126920026585045, 0.08594163875116435, 0.07967347979444635, 0.07269197317209034, 0.06523943255657352, 0.05756043154530752, 0.049889541078795584, 0.042440399181746066, 0.03539676767322338, 0.02890604776283309, 0.023075514987624765, 0.01797131336312757, 0.013620038493738051, 0.010012557367687032, 0.007109572778290188, 0.004848352179230376, 0.003150008335112064, 0.0019267409464745488, 0.0010885180985115365, 0.0005487834554551463, 0.0002289064194538778, 6.123359277961564e-05] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x180_kaiser_I_wf_qubit5": {
            "type": "arbitrary",
            "samples": [6.123359277961564e-05, 0.0002289064194538778, 0.000548783455455145, 0.0010885180985115382, 0.0019267409464745488, 0.003150008335112064, 0.004848352179230376, 0.007109572778290188, 0.010012557367687032, 0.013620038493738051, 0.01797131336312757, 0.023075514987624765, 0.02890604776283309, 0.03539676767322338, 0.042440399181746066, 0.049889541078795584, 0.05756043154530752, 0.06523943255657352, 0.07269197317209034, 0.07967347979444635, 0.08594163875116435, 0.09126920026585045, 0.09545645702431381, 0.0983425238802947] + [0.09981461034690563] * 2 + [0.0983425238802947, 0.09545645702431381, 0.09126920026585045, 0.08594163875116435, 0.07967347979444635, 0.07269197317209034, 0.06523943255657352, 0.05756043154530752, 0.049889541078795584, 0.042440399181746066, 0.03539676767322338, 0.02890604776283309, 0.023075514987624765, 0.01797131336312757, 0.013620038493738051, 0.010012557367687032, 0.007109572778290188, 0.004848352179230376, 0.003150008335112064, 0.0019267409464745488, 0.0010885180985115365, 0.0005487834554551463, 0.0002289064194538778, 6.123359277961564e-05] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x180_kaiser_Q_wf_qubit1": {
            "type": "arbitrary",
            "samples": [0.0] * 52,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x180_kaiser_Q_wf_qubit2": {
            "type": "arbitrary",
            "samples": [0.0] * 52,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x180_kaiser_Q_wf_qubit3": {
            "type": "arbitrary",
            "samples": [0.0] * 52,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x180_kaiser_Q_wf_qubit4": {
            "type": "arbitrary",
            "samples": [0.0] * 52,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x180_kaiser_Q_wf_qubit5": {
            "type": "arbitrary",
            "samples": [0.0] * 52,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x90_kaiser_I_wf_qubit1": {
            "type": "arbitrary",
            "samples": [3.061679638980782e-05, 0.0001144532097269389, 0.0002743917277275725, 0.0005442590492557691, 0.0009633704732372744, 0.001575004167556032, 0.002424176089615188, 0.003554786389145094, 0.005006278683843516, 0.006810019246869026, 0.008985656681563784, 0.011537757493812383, 0.014453023881416545, 0.01769838383661169, 0.021220199590873033, 0.024944770539397792, 0.02878021577265376, 0.03261971627828676, 0.03634598658604517, 0.039836739897223174, 0.04297081937558218, 0.045634600132925224, 0.047728228512156905, 0.04917126194014735] + [0.049907305173452814] * 2 + [0.04917126194014735, 0.047728228512156905, 0.045634600132925224, 0.04297081937558218, 0.039836739897223174, 0.03634598658604517, 0.03261971627828676, 0.02878021577265376, 0.024944770539397792, 0.021220199590873033, 0.01769838383661169, 0.014453023881416545, 0.011537757493812383, 0.008985656681563784, 0.006810019246869026, 0.005006278683843516, 0.003554786389145094, 0.002424176089615188, 0.001575004167556032, 0.0009633704732372744, 0.0005442590492557683, 0.00027439172772757316, 0.0001144532097269389, 3.061679638980782e-05] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x90_kaiser_I_wf_qubit2": {
            "type": "arbitrary",
            "samples": [3.061679638980782e-05, 0.0001144532097269389, 0.0002743917277275725, 0.0005442590492557691, 0.0009633704732372744, 0.001575004167556032, 0.002424176089615188, 0.003554786389145094, 0.005006278683843516, 0.006810019246869026, 0.008985656681563784, 0.011537757493812383, 0.014453023881416545, 0.01769838383661169, 0.021220199590873033, 0.024944770539397792, 0.02878021577265376, 0.03261971627828676, 0.03634598658604517, 0.039836739897223174, 0.04297081937558218, 0.045634600132925224, 0.047728228512156905, 0.04917126194014735] + [0.049907305173452814] * 2 + [0.04917126194014735, 0.047728228512156905, 0.045634600132925224, 0.04297081937558218, 0.039836739897223174, 0.03634598658604517, 0.03261971627828676, 0.02878021577265376, 0.024944770539397792, 0.021220199590873033, 0.01769838383661169, 0.014453023881416545, 0.011537757493812383, 0.008985656681563784, 0.006810019246869026, 0.005006278683843516, 0.003554786389145094, 0.002424176089615188, 0.001575004167556032, 0.0009633704732372744, 0.0005442590492557683, 0.00027439172772757316, 0.0001144532097269389, 3.061679638980782e-05] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x90_kaiser_I_wf_qubit3": {
            "type": "arbitrary",
            "samples": [3.061679638980782e-05, 0.0001144532097269389, 0.0002743917277275725, 0.0005442590492557691, 0.0009633704732372744, 0.001575004167556032, 0.002424176089615188, 0.003554786389145094, 0.005006278683843516, 0.006810019246869026, 0.008985656681563784, 0.011537757493812383, 0.014453023881416545, 0.01769838383661169, 0.021220199590873033, 0.024944770539397792, 0.02878021577265376, 0.03261971627828676, 0.03634598658604517, 0.039836739897223174, 0.04297081937558218, 0.045634600132925224, 0.047728228512156905, 0.04917126194014735] + [0.049907305173452814] * 2 + [0.04917126194014735, 0.047728228512156905, 0.045634600132925224, 0.04297081937558218, 0.039836739897223174, 0.03634598658604517, 0.03261971627828676, 0.02878021577265376, 0.024944770539397792, 0.021220199590873033, 0.01769838383661169, 0.014453023881416545, 0.011537757493812383, 0.008985656681563784, 0.006810019246869026, 0.005006278683843516, 0.003554786389145094, 0.002424176089615188, 0.001575004167556032, 0.0009633704732372744, 0.0005442590492557683, 0.00027439172772757316, 0.0001144532097269389, 3.061679638980782e-05] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x90_kaiser_I_wf_qubit4": {
            "type": "arbitrary",
            "samples": [3.061679638980782e-05, 0.0001144532097269389, 0.0002743917277275725, 0.0005442590492557691, 0.0009633704732372744, 0.001575004167556032, 0.002424176089615188, 0.003554786389145094, 0.005006278683843516, 0.006810019246869026, 0.008985656681563784, 0.011537757493812383, 0.014453023881416545, 0.01769838383661169, 0.021220199590873033, 0.024944770539397792, 0.02878021577265376, 0.03261971627828676, 0.03634598658604517, 0.039836739897223174, 0.04297081937558218, 0.045634600132925224, 0.047728228512156905, 0.04917126194014735] + [0.049907305173452814] * 2 + [0.04917126194014735, 0.047728228512156905, 0.045634600132925224, 0.04297081937558218, 0.039836739897223174, 0.03634598658604517, 0.03261971627828676, 0.02878021577265376, 0.024944770539397792, 0.021220199590873033, 0.01769838383661169, 0.014453023881416545, 0.011537757493812383, 0.008985656681563784, 0.006810019246869026, 0.005006278683843516, 0.003554786389145094, 0.002424176089615188, 0.001575004167556032, 0.0009633704732372744, 0.0005442590492557683, 0.00027439172772757316, 0.0001144532097269389, 3.061679638980782e-05] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x90_kaiser_I_wf_qubit5": {
            "type": "arbitrary",
            "samples": [3.061679638980782e-05, 0.0001144532097269389, 0.0002743917277275725, 0.0005442590492557691, 0.0009633704732372744, 0.001575004167556032, 0.002424176089615188, 0.003554786389145094, 0.005006278683843516, 0.006810019246869026, 0.008985656681563784, 0.011537757493812383, 0.014453023881416545, 0.01769838383661169, 0.021220199590873033, 0.024944770539397792, 0.02878021577265376, 0.03261971627828676, 0.03634598658604517, 0.039836739897223174, 0.04297081937558218, 0.045634600132925224, 0.047728228512156905, 0.04917126194014735] + [0.049907305173452814] * 2 + [0.04917126194014735, 0.047728228512156905, 0.045634600132925224, 0.04297081937558218, 0.039836739897223174, 0.03634598658604517, 0.03261971627828676, 0.02878021577265376, 0.024944770539397792, 0.021220199590873033, 0.01769838383661169, 0.014453023881416545, 0.011537757493812383, 0.008985656681563784, 0.006810019246869026, 0.005006278683843516, 0.003554786389145094, 0.002424176089615188, 0.001575004167556032, 0.0009633704732372744, 0.0005442590492557683, 0.00027439172772757316, 0.0001144532097269389, 3.061679638980782e-05] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x90_kaiser_Q_wf_qubit1": {
            "type": "arbitrary",
            "samples": [0.0] * 52,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x90_kaiser_Q_wf_qubit2": {
            "type": "arbitrary",
            "samples": [0.0] * 52,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x90_kaiser_Q_wf_qubit3": {
            "type": "arbitrary",
            "samples": [0.0] * 52,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x90_kaiser_Q_wf_qubit4": {
            "type": "arbitrary",
            "samples": [0.0] * 52,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x90_kaiser_Q_wf_qubit5": {
            "type": "arbitrary",
            "samples": [0.0] * 52,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_x90_kaiser_I_wf_qubit1": {
            "type": "arbitrary",
            "samples": [-3.061679638980782e-05, -0.0001144532097269389, -0.0002743917277275725, -0.0005442590492557691, -0.0009633704732372744, -0.001575004167556032, -0.002424176089615188, -0.003554786389145094, -0.005006278683843516, -0.006810019246869026, -0.008985656681563784, -0.011537757493812383, -0.014453023881416545, -0.01769838383661169, -0.021220199590873033, -0.024944770539397792, -0.02878021577265376, -0.03261971627828676, -0.03634598658604517, -0.039836739897223174, -0.04297081937558218, -0.045634600132925224, -0.047728228512156905, -0.04917126194014735] + [-0.049907305173452814] * 2 + [-0.04917126194014735, -0.047728228512156905, -0.045634600132925224, -0.04297081937558218, -0.039836739897223174, -0.03634598658604517, -0.03261971627828676, -0.02878021577265376, -0.024944770539397792, -0.021220199590873033, -0.01769838383661169, -0.014453023881416545, -0.011537757493812383, -0.008985656681563784, -0.006810019246869026, -0.005006278683843516, -0.003554786389145094, -0.002424176089615188, -0.001575004167556032, -0.0009633704732372744, -0.0005442590492557683, -0.00027439172772757316, -0.0001144532097269389, -3.061679638980782e-05] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_x90_kaiser_I_wf_qubit2": {
            "type": "arbitrary",
            "samples": [-3.061679638980782e-05, -0.0001144532097269389, -0.0002743917277275725, -0.0005442590492557691, -0.0009633704732372744, -0.001575004167556032, -0.002424176089615188, -0.003554786389145094, -0.005006278683843516, -0.006810019246869026, -0.008985656681563784, -0.011537757493812383, -0.014453023881416545, -0.01769838383661169, -0.021220199590873033, -0.024944770539397792, -0.02878021577265376, -0.03261971627828676, -0.03634598658604517, -0.039836739897223174, -0.04297081937558218, -0.045634600132925224, -0.047728228512156905, -0.04917126194014735] + [-0.049907305173452814] * 2 + [-0.04917126194014735, -0.047728228512156905, -0.045634600132925224, -0.04297081937558218, -0.039836739897223174, -0.03634598658604517, -0.03261971627828676, -0.02878021577265376, -0.024944770539397792, -0.021220199590873033, -0.01769838383661169, -0.014453023881416545, -0.011537757493812383, -0.008985656681563784, -0.006810019246869026, -0.005006278683843516, -0.003554786389145094, -0.002424176089615188, -0.001575004167556032, -0.0009633704732372744, -0.0005442590492557683, -0.00027439172772757316, -0.0001144532097269389, -3.061679638980782e-05] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_x90_kaiser_I_wf_qubit3": {
            "type": "arbitrary",
            "samples": [-3.061679638980782e-05, -0.0001144532097269389, -0.0002743917277275725, -0.0005442590492557691, -0.0009633704732372744, -0.001575004167556032, -0.002424176089615188, -0.003554786389145094, -0.005006278683843516, -0.006810019246869026, -0.008985656681563784, -0.011537757493812383, -0.014453023881416545, -0.01769838383661169, -0.021220199590873033, -0.024944770539397792, -0.02878021577265376, -0.03261971627828676, -0.03634598658604517, -0.039836739897223174, -0.04297081937558218, -0.045634600132925224, -0.047728228512156905, -0.04917126194014735] + [-0.049907305173452814] * 2 + [-0.04917126194014735, -0.047728228512156905, -0.045634600132925224, -0.04297081937558218, -0.039836739897223174, -0.03634598658604517, -0.03261971627828676, -0.02878021577265376, -0.024944770539397792, -0.021220199590873033, -0.01769838383661169, -0.014453023881416545, -0.011537757493812383, -0.008985656681563784, -0.006810019246869026, -0.005006278683843516, -0.003554786389145094, -0.002424176089615188, -0.001575004167556032, -0.0009633704732372744, -0.0005442590492557683, -0.00027439172772757316, -0.0001144532097269389, -3.061679638980782e-05] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_x90_kaiser_I_wf_qubit4": {
            "type": "arbitrary",
            "samples": [-3.061679638980782e-05, -0.0001144532097269389, -0.0002743917277275725, -0.0005442590492557691, -0.0009633704732372744, -0.001575004167556032, -0.002424176089615188, -0.003554786389145094, -0.005006278683843516, -0.006810019246869026, -0.008985656681563784, -0.011537757493812383, -0.014453023881416545, -0.01769838383661169, -0.021220199590873033, -0.024944770539397792, -0.02878021577265376, -0.03261971627828676, -0.03634598658604517, -0.039836739897223174, -0.04297081937558218, -0.045634600132925224, -0.047728228512156905, -0.04917126194014735] + [-0.049907305173452814] * 2 + [-0.04917126194014735, -0.047728228512156905, -0.045634600132925224, -0.04297081937558218, -0.039836739897223174, -0.03634598658604517, -0.03261971627828676, -0.02878021577265376, -0.024944770539397792, -0.021220199590873033, -0.01769838383661169, -0.014453023881416545, -0.011537757493812383, -0.008985656681563784, -0.006810019246869026, -0.005006278683843516, -0.003554786389145094, -0.002424176089615188, -0.001575004167556032, -0.0009633704732372744, -0.0005442590492557683, -0.00027439172772757316, -0.0001144532097269389, -3.061679638980782e-05] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_x90_kaiser_I_wf_qubit5": {
            "type": "arbitrary",
            "samples": [-3.061679638980782e-05, -0.0001144532097269389, -0.0002743917277275725, -0.0005442590492557691, -0.0009633704732372744, -0.001575004167556032, -0.002424176089615188, -0.003554786389145094, -0.005006278683843516, -0.006810019246869026, -0.008985656681563784, -0.011537757493812383, -0.014453023881416545, -0.01769838383661169, -0.021220199590873033, -0.024944770539397792, -0.02878021577265376, -0.03261971627828676, -0.03634598658604517, -0.039836739897223174, -0.04297081937558218, -0.045634600132925224, -0.047728228512156905, -0.04917126194014735] + [-0.049907305173452814] * 2 + [-0.04917126194014735, -0.047728228512156905, -0.045634600132925224, -0.04297081937558218, -0.039836739897223174, -0.03634598658604517, -0.03261971627828676, -0.02878021577265376, -0.024944770539397792, -0.021220199590873033, -0.01769838383661169, -0.014453023881416545, -0.011537757493812383, -0.008985656681563784, -0.006810019246869026, -0.005006278683843516, -0.003554786389145094, -0.002424176089615188, -0.001575004167556032, -0.0009633704732372744, -0.0005442590492557683, -0.00027439172772757316, -0.0001144532097269389, -3.061679638980782e-05] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_x90_kaiser_Q_wf_qubit1": {
            "type": "arbitrary",
            "samples": [0.0] * 52,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_x90_kaiser_Q_wf_qubit2": {
            "type": "arbitrary",
            "samples": [0.0] * 52,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_x90_kaiser_Q_wf_qubit3": {
            "type": "arbitrary",
            "samples": [0.0] * 52,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_x90_kaiser_Q_wf_qubit4": {
            "type": "arbitrary",
            "samples": [0.0] * 52,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_x90_kaiser_Q_wf_qubit5": {
            "type": "arbitrary",
            "samples": [0.0] * 52,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y180_kaiser_I_wf_qubit1": {
            "type": "arbitrary",
            "samples": [0.0] * 52,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y180_kaiser_I_wf_qubit2": {
            "type": "arbitrary",
            "samples": [0.0] * 52,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y180_kaiser_I_wf_qubit3": {
            "type": "arbitrary",
            "samples": [0.0] * 52,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y180_kaiser_I_wf_qubit4": {
            "type": "arbitrary",
            "samples": [0.0] * 52,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y180_kaiser_I_wf_qubit5": {
            "type": "arbitrary",
            "samples": [0.0] * 52,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y180_kaiser_Q_wf_qubit1": {
            "type": "arbitrary",
            "samples": [6.123359277961564e-05, 0.0002289064194538778, 0.000548783455455145, 0.0010885180985115382, 0.0019267409464745488, 0.003150008335112064, 0.004848352179230376, 0.007109572778290188, 0.010012557367687032, 0.013620038493738051, 0.01797131336312757, 0.023075514987624765, 0.02890604776283309, 0.03539676767322338, 0.042440399181746066, 0.049889541078795584, 0.05756043154530752, 0.06523943255657352, 0.07269197317209034, 0.07967347979444635, 0.08594163875116435, 0.09126920026585045, 0.09545645702431381, 0.0983425238802947] + [0.09981461034690563] * 2 + [0.0983425238802947, 0.09545645702431381, 0.09126920026585045, 0.08594163875116435, 0.07967347979444635, 0.07269197317209034, 0.06523943255657352, 0.05756043154530752, 0.049889541078795584, 0.042440399181746066, 0.03539676767322338, 0.02890604776283309, 0.023075514987624765, 0.01797131336312757, 0.013620038493738051, 0.010012557367687032, 0.007109572778290188, 0.004848352179230376, 0.003150008335112064, 0.0019267409464745488, 0.0010885180985115365, 0.0005487834554551463, 0.0002289064194538778, 6.123359277961564e-05] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y180_kaiser_Q_wf_qubit2": {
            "type": "arbitrary",
            "samples": [6.123359277961564e-05, 0.0002289064194538778, 0.000548783455455145, 0.0010885180985115382, 0.0019267409464745488, 0.003150008335112064, 0.004848352179230376, 0.007109572778290188, 0.010012557367687032, 0.013620038493738051, 0.01797131336312757, 0.023075514987624765, 0.02890604776283309, 0.03539676767322338, 0.042440399181746066, 0.049889541078795584, 0.05756043154530752, 0.06523943255657352, 0.07269197317209034, 0.07967347979444635, 0.08594163875116435, 0.09126920026585045, 0.09545645702431381, 0.0983425238802947] + [0.09981461034690563] * 2 + [0.0983425238802947, 0.09545645702431381, 0.09126920026585045, 0.08594163875116435, 0.07967347979444635, 0.07269197317209034, 0.06523943255657352, 0.05756043154530752, 0.049889541078795584, 0.042440399181746066, 0.03539676767322338, 0.02890604776283309, 0.023075514987624765, 0.01797131336312757, 0.013620038493738051, 0.010012557367687032, 0.007109572778290188, 0.004848352179230376, 0.003150008335112064, 0.0019267409464745488, 0.0010885180985115365, 0.0005487834554551463, 0.0002289064194538778, 6.123359277961564e-05] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y180_kaiser_Q_wf_qubit3": {
            "type": "arbitrary",
            "samples": [6.123359277961564e-05, 0.0002289064194538778, 0.000548783455455145, 0.0010885180985115382, 0.0019267409464745488, 0.003150008335112064, 0.004848352179230376, 0.007109572778290188, 0.010012557367687032, 0.013620038493738051, 0.01797131336312757, 0.023075514987624765, 0.02890604776283309, 0.03539676767322338, 0.042440399181746066, 0.049889541078795584, 0.05756043154530752, 0.06523943255657352, 0.07269197317209034, 0.07967347979444635, 0.08594163875116435, 0.09126920026585045, 0.09545645702431381, 0.0983425238802947] + [0.09981461034690563] * 2 + [0.0983425238802947, 0.09545645702431381, 0.09126920026585045, 0.08594163875116435, 0.07967347979444635, 0.07269197317209034, 0.06523943255657352, 0.05756043154530752, 0.049889541078795584, 0.042440399181746066, 0.03539676767322338, 0.02890604776283309, 0.023075514987624765, 0.01797131336312757, 0.013620038493738051, 0.010012557367687032, 0.007109572778290188, 0.004848352179230376, 0.003150008335112064, 0.0019267409464745488, 0.0010885180985115365, 0.0005487834554551463, 0.0002289064194538778, 6.123359277961564e-05] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y180_kaiser_Q_wf_qubit4": {
            "type": "arbitrary",
            "samples": [6.123359277961564e-05, 0.0002289064194538778, 0.000548783455455145, 0.0010885180985115382, 0.0019267409464745488, 0.003150008335112064, 0.004848352179230376, 0.007109572778290188, 0.010012557367687032, 0.013620038493738051, 0.01797131336312757, 0.023075514987624765, 0.02890604776283309, 0.03539676767322338, 0.042440399181746066, 0.049889541078795584, 0.05756043154530752, 0.06523943255657352, 0.07269197317209034, 0.07967347979444635, 0.08594163875116435, 0.09126920026585045, 0.09545645702431381, 0.0983425238802947] + [0.09981461034690563] * 2 + [0.0983425238802947, 0.09545645702431381, 0.09126920026585045, 0.08594163875116435, 0.07967347979444635, 0.07269197317209034, 0.06523943255657352, 0.05756043154530752, 0.049889541078795584, 0.042440399181746066, 0.03539676767322338, 0.02890604776283309, 0.023075514987624765, 0.01797131336312757, 0.013620038493738051, 0.010012557367687032, 0.007109572778290188, 0.004848352179230376, 0.003150008335112064, 0.0019267409464745488, 0.0010885180985115365, 0.0005487834554551463, 0.0002289064194538778, 6.123359277961564e-05] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y180_kaiser_Q_wf_qubit5": {
            "type": "arbitrary",
            "samples": [6.123359277961564e-05, 0.0002289064194538778, 0.000548783455455145, 0.0010885180985115382, 0.0019267409464745488, 0.003150008335112064, 0.004848352179230376, 0.007109572778290188, 0.010012557367687032, 0.013620038493738051, 0.01797131336312757, 0.023075514987624765, 0.02890604776283309, 0.03539676767322338, 0.042440399181746066, 0.049889541078795584, 0.05756043154530752, 0.06523943255657352, 0.07269197317209034, 0.07967347979444635, 0.08594163875116435, 0.09126920026585045, 0.09545645702431381, 0.0983425238802947] + [0.09981461034690563] * 2 + [0.0983425238802947, 0.09545645702431381, 0.09126920026585045, 0.08594163875116435, 0.07967347979444635, 0.07269197317209034, 0.06523943255657352, 0.05756043154530752, 0.049889541078795584, 0.042440399181746066, 0.03539676767322338, 0.02890604776283309, 0.023075514987624765, 0.01797131336312757, 0.013620038493738051, 0.010012557367687032, 0.007109572778290188, 0.004848352179230376, 0.003150008335112064, 0.0019267409464745488, 0.0010885180985115365, 0.0005487834554551463, 0.0002289064194538778, 6.123359277961564e-05] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y90_kaiser_I_wf_qubit1": {
            "type": "arbitrary",
            "samples": [0.0] * 52,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y90_kaiser_I_wf_qubit2": {
            "type": "arbitrary",
            "samples": [0.0] * 52,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y90_kaiser_I_wf_qubit3": {
            "type": "arbitrary",
            "samples": [0.0] * 52,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y90_kaiser_I_wf_qubit4": {
            "type": "arbitrary",
            "samples": [0.0] * 52,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y90_kaiser_I_wf_qubit5": {
            "type": "arbitrary",
            "samples": [0.0] * 52,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y90_kaiser_Q_wf_qubit1": {
            "type": "arbitrary",
            "samples": [3.061679638980782e-05, 0.0001144532097269389, 0.0002743917277275725, 0.0005442590492557691, 0.0009633704732372744, 0.001575004167556032, 0.002424176089615188, 0.003554786389145094, 0.005006278683843516, 0.006810019246869026, 0.008985656681563784, 0.011537757493812383, 0.014453023881416545, 0.01769838383661169, 0.021220199590873033, 0.024944770539397792, 0.02878021577265376, 0.03261971627828676, 0.03634598658604517, 0.039836739897223174, 0.04297081937558218, 0.045634600132925224, 0.047728228512156905, 0.04917126194014735] + [0.049907305173452814] * 2 + [0.04917126194014735, 0.047728228512156905, 0.045634600132925224, 0.04297081937558218, 0.039836739897223174, 0.03634598658604517, 0.03261971627828676, 0.02878021577265376, 0.024944770539397792, 0.021220199590873033, 0.01769838383661169, 0.014453023881416545, 0.011537757493812383, 0.008985656681563784, 0.006810019246869026, 0.005006278683843516, 0.003554786389145094, 0.002424176089615188, 0.001575004167556032, 0.0009633704732372744, 0.0005442590492557683, 0.00027439172772757316, 0.0001144532097269389, 3.061679638980782e-05] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y90_kaiser_Q_wf_qubit2": {
            "type": "arbitrary",
            "samples": [3.061679638980782e-05, 0.0001144532097269389, 0.0002743917277275725, 0.0005442590492557691, 0.0009633704732372744, 0.001575004167556032, 0.002424176089615188, 0.003554786389145094, 0.005006278683843516, 0.006810019246869026, 0.008985656681563784, 0.011537757493812383, 0.014453023881416545, 0.01769838383661169, 0.021220199590873033, 0.024944770539397792, 0.02878021577265376, 0.03261971627828676, 0.03634598658604517, 0.039836739897223174, 0.04297081937558218, 0.045634600132925224, 0.047728228512156905, 0.04917126194014735] + [0.049907305173452814] * 2 + [0.04917126194014735, 0.047728228512156905, 0.045634600132925224, 0.04297081937558218, 0.039836739897223174, 0.03634598658604517, 0.03261971627828676, 0.02878021577265376, 0.024944770539397792, 0.021220199590873033, 0.01769838383661169, 0.014453023881416545, 0.011537757493812383, 0.008985656681563784, 0.006810019246869026, 0.005006278683843516, 0.003554786389145094, 0.002424176089615188, 0.001575004167556032, 0.0009633704732372744, 0.0005442590492557683, 0.00027439172772757316, 0.0001144532097269389, 3.061679638980782e-05] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y90_kaiser_Q_wf_qubit3": {
            "type": "arbitrary",
            "samples": [3.061679638980782e-05, 0.0001144532097269389, 0.0002743917277275725, 0.0005442590492557691, 0.0009633704732372744, 0.001575004167556032, 0.002424176089615188, 0.003554786389145094, 0.005006278683843516, 0.006810019246869026, 0.008985656681563784, 0.011537757493812383, 0.014453023881416545, 0.01769838383661169, 0.021220199590873033, 0.024944770539397792, 0.02878021577265376, 0.03261971627828676, 0.03634598658604517, 0.039836739897223174, 0.04297081937558218, 0.045634600132925224, 0.047728228512156905, 0.04917126194014735] + [0.049907305173452814] * 2 + [0.04917126194014735, 0.047728228512156905, 0.045634600132925224, 0.04297081937558218, 0.039836739897223174, 0.03634598658604517, 0.03261971627828676, 0.02878021577265376, 0.024944770539397792, 0.021220199590873033, 0.01769838383661169, 0.014453023881416545, 0.011537757493812383, 0.008985656681563784, 0.006810019246869026, 0.005006278683843516, 0.003554786389145094, 0.002424176089615188, 0.001575004167556032, 0.0009633704732372744, 0.0005442590492557683, 0.00027439172772757316, 0.0001144532097269389, 3.061679638980782e-05] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y90_kaiser_Q_wf_qubit4": {
            "type": "arbitrary",
            "samples": [3.061679638980782e-05, 0.0001144532097269389, 0.0002743917277275725, 0.0005442590492557691, 0.0009633704732372744, 0.001575004167556032, 0.002424176089615188, 0.003554786389145094, 0.005006278683843516, 0.006810019246869026, 0.008985656681563784, 0.011537757493812383, 0.014453023881416545, 0.01769838383661169, 0.021220199590873033, 0.024944770539397792, 0.02878021577265376, 0.03261971627828676, 0.03634598658604517, 0.039836739897223174, 0.04297081937558218, 0.045634600132925224, 0.047728228512156905, 0.04917126194014735] + [0.049907305173452814] * 2 + [0.04917126194014735, 0.047728228512156905, 0.045634600132925224, 0.04297081937558218, 0.039836739897223174, 0.03634598658604517, 0.03261971627828676, 0.02878021577265376, 0.024944770539397792, 0.021220199590873033, 0.01769838383661169, 0.014453023881416545, 0.011537757493812383, 0.008985656681563784, 0.006810019246869026, 0.005006278683843516, 0.003554786389145094, 0.002424176089615188, 0.001575004167556032, 0.0009633704732372744, 0.0005442590492557683, 0.00027439172772757316, 0.0001144532097269389, 3.061679638980782e-05] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y90_kaiser_Q_wf_qubit5": {
            "type": "arbitrary",
            "samples": [3.061679638980782e-05, 0.0001144532097269389, 0.0002743917277275725, 0.0005442590492557691, 0.0009633704732372744, 0.001575004167556032, 0.002424176089615188, 0.003554786389145094, 0.005006278683843516, 0.006810019246869026, 0.008985656681563784, 0.011537757493812383, 0.014453023881416545, 0.01769838383661169, 0.021220199590873033, 0.024944770539397792, 0.02878021577265376, 0.03261971627828676, 0.03634598658604517, 0.039836739897223174, 0.04297081937558218, 0.045634600132925224, 0.047728228512156905, 0.04917126194014735] + [0.049907305173452814] * 2 + [0.04917126194014735, 0.047728228512156905, 0.045634600132925224, 0.04297081937558218, 0.039836739897223174, 0.03634598658604517, 0.03261971627828676, 0.02878021577265376, 0.024944770539397792, 0.021220199590873033, 0.01769838383661169, 0.014453023881416545, 0.011537757493812383, 0.008985656681563784, 0.006810019246869026, 0.005006278683843516, 0.003554786389145094, 0.002424176089615188, 0.001575004167556032, 0.0009633704732372744, 0.0005442590492557683, 0.00027439172772757316, 0.0001144532097269389, 3.061679638980782e-05] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_y90_kaiser_I_wf_qubit1": {
            "type": "arbitrary",
            "samples": [0.0] * 52,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_y90_kaiser_I_wf_qubit2": {
            "type": "arbitrary",
            "samples": [0.0] * 52,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_y90_kaiser_I_wf_qubit3": {
            "type": "arbitrary",
            "samples": [0.0] * 52,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_y90_kaiser_I_wf_qubit4": {
            "type": "arbitrary",
            "samples": [0.0] * 52,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_y90_kaiser_I_wf_qubit5": {
            "type": "arbitrary",
            "samples": [0.0] * 52,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_y90_kaiser_Q_wf_qubit1": {
            "type": "arbitrary",
            "samples": [-3.061679638980782e-05, -0.0001144532097269389, -0.0002743917277275725, -0.0005442590492557691, -0.0009633704732372744, -0.001575004167556032, -0.002424176089615188, -0.003554786389145094, -0.005006278683843516, -0.006810019246869026, -0.008985656681563784, -0.011537757493812383, -0.014453023881416545, -0.01769838383661169, -0.021220199590873033, -0.024944770539397792, -0.02878021577265376, -0.03261971627828676, -0.03634598658604517, -0.039836739897223174, -0.04297081937558218, -0.045634600132925224, -0.047728228512156905, -0.04917126194014735] + [-0.049907305173452814] * 2 + [-0.04917126194014735, -0.047728228512156905, -0.045634600132925224, -0.04297081937558218, -0.039836739897223174, -0.03634598658604517, -0.03261971627828676, -0.02878021577265376, -0.024944770539397792, -0.021220199590873033, -0.01769838383661169, -0.014453023881416545, -0.011537757493812383, -0.008985656681563784, -0.006810019246869026, -0.005006278683843516, -0.003554786389145094, -0.002424176089615188, -0.001575004167556032, -0.0009633704732372744, -0.0005442590492557683, -0.00027439172772757316, -0.0001144532097269389, -3.061679638980782e-05] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_y90_kaiser_Q_wf_qubit2": {
            "type": "arbitrary",
            "samples": [-3.061679638980782e-05, -0.0001144532097269389, -0.0002743917277275725, -0.0005442590492557691, -0.0009633704732372744, -0.001575004167556032, -0.002424176089615188, -0.003554786389145094, -0.005006278683843516, -0.006810019246869026, -0.008985656681563784, -0.011537757493812383, -0.014453023881416545, -0.01769838383661169, -0.021220199590873033, -0.024944770539397792, -0.02878021577265376, -0.03261971627828676, -0.03634598658604517, -0.039836739897223174, -0.04297081937558218, -0.045634600132925224, -0.047728228512156905, -0.04917126194014735] + [-0.049907305173452814] * 2 + [-0.04917126194014735, -0.047728228512156905, -0.045634600132925224, -0.04297081937558218, -0.039836739897223174, -0.03634598658604517, -0.03261971627828676, -0.02878021577265376, -0.024944770539397792, -0.021220199590873033, -0.01769838383661169, -0.014453023881416545, -0.011537757493812383, -0.008985656681563784, -0.006810019246869026, -0.005006278683843516, -0.003554786389145094, -0.002424176089615188, -0.001575004167556032, -0.0009633704732372744, -0.0005442590492557683, -0.00027439172772757316, -0.0001144532097269389, -3.061679638980782e-05] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_y90_kaiser_Q_wf_qubit3": {
            "type": "arbitrary",
            "samples": [-3.061679638980782e-05, -0.0001144532097269389, -0.0002743917277275725, -0.0005442590492557691, -0.0009633704732372744, -0.001575004167556032, -0.002424176089615188, -0.003554786389145094, -0.005006278683843516, -0.006810019246869026, -0.008985656681563784, -0.011537757493812383, -0.014453023881416545, -0.01769838383661169, -0.021220199590873033, -0.024944770539397792, -0.02878021577265376, -0.03261971627828676, -0.03634598658604517, -0.039836739897223174, -0.04297081937558218, -0.045634600132925224, -0.047728228512156905, -0.04917126194014735] + [-0.049907305173452814] * 2 + [-0.04917126194014735, -0.047728228512156905, -0.045634600132925224, -0.04297081937558218, -0.039836739897223174, -0.03634598658604517, -0.03261971627828676, -0.02878021577265376, -0.024944770539397792, -0.021220199590873033, -0.01769838383661169, -0.014453023881416545, -0.011537757493812383, -0.008985656681563784, -0.006810019246869026, -0.005006278683843516, -0.003554786389145094, -0.002424176089615188, -0.001575004167556032, -0.0009633704732372744, -0.0005442590492557683, -0.00027439172772757316, -0.0001144532097269389, -3.061679638980782e-05] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_y90_kaiser_Q_wf_qubit4": {
            "type": "arbitrary",
            "samples": [-3.061679638980782e-05, -0.0001144532097269389, -0.0002743917277275725, -0.0005442590492557691, -0.0009633704732372744, -0.001575004167556032, -0.002424176089615188, -0.003554786389145094, -0.005006278683843516, -0.006810019246869026, -0.008985656681563784, -0.011537757493812383, -0.014453023881416545, -0.01769838383661169, -0.021220199590873033, -0.024944770539397792, -0.02878021577265376, -0.03261971627828676, -0.03634598658604517, -0.039836739897223174, -0.04297081937558218, -0.045634600132925224, -0.047728228512156905, -0.04917126194014735] + [-0.049907305173452814] * 2 + [-0.04917126194014735, -0.047728228512156905, -0.045634600132925224, -0.04297081937558218, -0.039836739897223174, -0.03634598658604517, -0.03261971627828676, -0.02878021577265376, -0.024944770539397792, -0.021220199590873033, -0.01769838383661169, -0.014453023881416545, -0.011537757493812383, -0.008985656681563784, -0.006810019246869026, -0.005006278683843516, -0.003554786389145094, -0.002424176089615188, -0.001575004167556032, -0.0009633704732372744, -0.0005442590492557683, -0.00027439172772757316, -0.0001144532097269389, -3.061679638980782e-05] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_y90_kaiser_Q_wf_qubit5": {
            "type": "arbitrary",
            "samples": [-3.061679638980782e-05, -0.0001144532097269389, -0.0002743917277275725, -0.0005442590492557691, -0.0009633704732372744, -0.001575004167556032, -0.002424176089615188, -0.003554786389145094, -0.005006278683843516, -0.006810019246869026, -0.008985656681563784, -0.011537757493812383, -0.014453023881416545, -0.01769838383661169, -0.021220199590873033, -0.024944770539397792, -0.02878021577265376, -0.03261971627828676, -0.03634598658604517, -0.039836739897223174, -0.04297081937558218, -0.045634600132925224, -0.047728228512156905, -0.04917126194014735] + [-0.049907305173452814] * 2 + [-0.04917126194014735, -0.047728228512156905, -0.045634600132925224, -0.04297081937558218, -0.039836739897223174, -0.03634598658604517, -0.03261971627828676, -0.02878021577265376, -0.024944770539397792, -0.021220199590873033, -0.01769838383661169, -0.014453023881416545, -0.011537757493812383, -0.008985656681563784, -0.006810019246869026, -0.005006278683843516, -0.003554786389145094, -0.002424176089615188, -0.001575004167556032, -0.0009633704732372744, -0.0005442590492557683, -0.00027439172772757316, -0.0001144532097269389, -3.061679638980782e-05] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x180_kaiser_I_wf_qp_control_c3t2": {
            "type": "arbitrary",
            "samples": [6.123359277961564e-05, 0.0001306438144712879, 0.00023132187674409848, 0.0003707991780740096, 0.0005574391218594114, 0.0008003941708179544, 0.0011095399428924942, 0.0014953855867247238, 0.0019689601966731024, 0.0025416755920456883, 0.003225166380287162, 0.0040311088354394045, 0.0049710207362835285, 0.006056044907394079, 0.007296719774748082, 0.008702740769447388, 0.010282716872948027, 0.012043926980302464, 0.01399208105104621, 0.016131091209017425, 0.018462858033262076, 0.020987077245404648, 0.023701071840357107, 0.026599654425844745, 0.02967502413386515, 0.03291670194889541, 0.03631150767153205, 0.03984358101334329, 0.04349444851284272, 0.04724313708992553, 0.051066334135211805, 0.054938593081588605, 0.05883258244909391, 0.06271937541311469, 0.06656877604179862, 0.0703496775033089, 0.07403044677783581, 0.07757932974235295, 0.08096486994518408, 0.08415633396728084, 0.08712413598952014, 0.089840254058968, 0.09227863057700843, 0.09441554972003091, 0.09622998484670547, 0.09770390943881668, 0.09882256575559714, 0.09957468614155682] + [0.09995266279888454] * 2 + [0.09957468614155682, 0.09882256575559714, 0.09770390943881668, 0.09622998484670547, 0.09441554972003091, 0.09227863057700843, 0.089840254058968, 0.08712413598952014, 0.08415633396728084, 0.0809648699451842, 0.07757932974235295, 0.07403044677783581, 0.0703496775033089, 0.06656877604179862, 0.06271937541311469, 0.05883258244909391, 0.054938593081588605, 0.051066334135211805, 0.04724313708992561, 0.04349444851284272, 0.03984358101334329, 0.036311507671532114, 0.03291670194889541, 0.02967502413386515, 0.026599654425844745, 0.023701071840357107, 0.020987077245404648, 0.018462858033262076, 0.016131091209017425, 0.01399208105104621, 0.012043926980302464, 0.010282716872948027, 0.008702740769447388, 0.007296719774748089, 0.006056044907394079, 0.0049710207362835285, 0.004031108835439411, 0.003225166380287162, 0.0025416755920456883, 0.001968960196673105, 0.0014953855867247238, 0.0011095399428924942, 0.0008003941708179558, 0.00055743912185941, 0.0003707991780740096, 0.00023132187674409872, 0.00013064381447128748, 6.123359277961564e-05] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x180_kaiser_Q_wf_qp_control_c3t2": {
            "type": "arbitrary",
            "samples": [0.0] * 100,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x90_kaiser_I_wf_qp_control_c3t2": {
            "type": "arbitrary",
            "samples": [3.061679638980782e-05, 6.532190723564394e-05, 0.00011566093837204924, 0.0001853995890370048, 0.0002787195609297057, 0.0004001970854089772, 0.0005547699714462471, 0.0007476927933623619, 0.0009844800983365512, 0.0012708377960228441, 0.001612583190143581, 0.0020155544177197023, 0.0024855103681417643, 0.0030280224536970396, 0.003648359887374041, 0.004351370384723694, 0.005141358436474014, 0.006021963490151232, 0.006996040525523105, 0.008065545604508713, 0.009231429016631038, 0.010493538622702324, 0.011850535920178554, 0.013299827212922373, 0.014837512066932575, 0.016458350974447707, 0.018155753835766026, 0.019921790506671644, 0.02174722425642136, 0.023621568544962765, 0.025533167067605902, 0.027469296540794302, 0.029416291224546955, 0.031359687706557345, 0.03328438802089931, 0.03517483875165445, 0.037015223388917905, 0.03878966487117647, 0.04048243497259204, 0.04207816698364042, 0.04356206799476007, 0.044920127029484, 0.046139315288504214, 0.047207774860015456, 0.04811499242335274, 0.04885195471940834, 0.04941128287779857, 0.04978734307077841] + [0.04997633139944227] * 2 + [0.04978734307077841, 0.04941128287779857, 0.04885195471940834, 0.04811499242335274, 0.047207774860015456, 0.046139315288504214, 0.044920127029484, 0.04356206799476007, 0.04207816698364042, 0.0404824349725921, 0.03878966487117647, 0.037015223388917905, 0.03517483875165445, 0.03328438802089931, 0.031359687706557345, 0.029416291224546955, 0.027469296540794302, 0.025533167067605902, 0.023621568544962807, 0.02174722425642136, 0.019921790506671644, 0.018155753835766057, 0.016458350974447707, 0.014837512066932575, 0.013299827212922373, 0.011850535920178554, 0.010493538622702324, 0.009231429016631038, 0.008065545604508713, 0.006996040525523105, 0.006021963490151232, 0.005141358436474014, 0.004351370384723694, 0.0036483598873740444, 0.0030280224536970396, 0.0024855103681417643, 0.0020155544177197053, 0.001612583190143581, 0.0012708377960228441, 0.0009844800983365525, 0.0007476927933623619, 0.0005547699714462471, 0.0004001970854089779, 0.000278719560929705, 0.0001853995890370048, 0.00011566093837204936, 6.532190723564374e-05, 3.061679638980782e-05] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "x90_kaiser_Q_wf_qp_control_c3t2": {
            "type": "arbitrary",
            "samples": [0.0] * 100,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_x90_kaiser_I_wf_qp_control_c3t2": {
            "type": "arbitrary",
            "samples": [-3.061679638980782e-05, -6.532190723564394e-05, -0.00011566093837204924, -0.0001853995890370048, -0.0002787195609297057, -0.0004001970854089772, -0.0005547699714462471, -0.0007476927933623619, -0.0009844800983365512, -0.0012708377960228441, -0.001612583190143581, -0.0020155544177197023, -0.0024855103681417643, -0.0030280224536970396, -0.003648359887374041, -0.004351370384723694, -0.005141358436474014, -0.006021963490151232, -0.006996040525523105, -0.008065545604508713, -0.009231429016631038, -0.010493538622702324, -0.011850535920178554, -0.013299827212922373, -0.014837512066932575, -0.016458350974447707, -0.018155753835766026, -0.019921790506671644, -0.02174722425642136, -0.023621568544962765, -0.025533167067605902, -0.027469296540794302, -0.029416291224546955, -0.031359687706557345, -0.03328438802089931, -0.03517483875165445, -0.037015223388917905, -0.03878966487117647, -0.04048243497259204, -0.04207816698364042, -0.04356206799476007, -0.044920127029484, -0.046139315288504214, -0.047207774860015456, -0.04811499242335274, -0.04885195471940834, -0.04941128287779857, -0.04978734307077841] + [-0.04997633139944227] * 2 + [-0.04978734307077841, -0.04941128287779857, -0.04885195471940834, -0.04811499242335274, -0.047207774860015456, -0.046139315288504214, -0.044920127029484, -0.04356206799476007, -0.04207816698364042, -0.0404824349725921, -0.03878966487117647, -0.037015223388917905, -0.03517483875165445, -0.03328438802089931, -0.031359687706557345, -0.029416291224546955, -0.027469296540794302, -0.025533167067605902, -0.023621568544962807, -0.02174722425642136, -0.019921790506671644, -0.018155753835766057, -0.016458350974447707, -0.014837512066932575, -0.013299827212922373, -0.011850535920178554, -0.010493538622702324, -0.009231429016631038, -0.008065545604508713, -0.006996040525523105, -0.006021963490151232, -0.005141358436474014, -0.004351370384723694, -0.0036483598873740444, -0.0030280224536970396, -0.0024855103681417643, -0.0020155544177197053, -0.001612583190143581, -0.0012708377960228441, -0.0009844800983365525, -0.0007476927933623619, -0.0005547699714462471, -0.0004001970854089779, -0.000278719560929705, -0.0001853995890370048, -0.00011566093837204936, -6.532190723564374e-05, -3.061679638980782e-05] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_x90_kaiser_Q_wf_qp_control_c3t2": {
            "type": "arbitrary",
            "samples": [0.0] * 100,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y180_kaiser_I_wf_qp_control_c3t2": {
            "type": "arbitrary",
            "samples": [0.0] * 100,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y180_kaiser_Q_wf_qp_control_c3t2": {
            "type": "arbitrary",
            "samples": [6.123359277961564e-05, 0.0001306438144712879, 0.00023132187674409848, 0.0003707991780740096, 0.0005574391218594114, 0.0008003941708179544, 0.0011095399428924942, 0.0014953855867247238, 0.0019689601966731024, 0.0025416755920456883, 0.003225166380287162, 0.0040311088354394045, 0.0049710207362835285, 0.006056044907394079, 0.007296719774748082, 0.008702740769447388, 0.010282716872948027, 0.012043926980302464, 0.01399208105104621, 0.016131091209017425, 0.018462858033262076, 0.020987077245404648, 0.023701071840357107, 0.026599654425844745, 0.02967502413386515, 0.03291670194889541, 0.03631150767153205, 0.03984358101334329, 0.04349444851284272, 0.04724313708992553, 0.051066334135211805, 0.054938593081588605, 0.05883258244909391, 0.06271937541311469, 0.06656877604179862, 0.0703496775033089, 0.07403044677783581, 0.07757932974235295, 0.08096486994518408, 0.08415633396728084, 0.08712413598952014, 0.089840254058968, 0.09227863057700843, 0.09441554972003091, 0.09622998484670547, 0.09770390943881668, 0.09882256575559714, 0.09957468614155682] + [0.09995266279888454] * 2 + [0.09957468614155682, 0.09882256575559714, 0.09770390943881668, 0.09622998484670547, 0.09441554972003091, 0.09227863057700843, 0.089840254058968, 0.08712413598952014, 0.08415633396728084, 0.0809648699451842, 0.07757932974235295, 0.07403044677783581, 0.0703496775033089, 0.06656877604179862, 0.06271937541311469, 0.05883258244909391, 0.054938593081588605, 0.051066334135211805, 0.04724313708992561, 0.04349444851284272, 0.03984358101334329, 0.036311507671532114, 0.03291670194889541, 0.02967502413386515, 0.026599654425844745, 0.023701071840357107, 0.020987077245404648, 0.018462858033262076, 0.016131091209017425, 0.01399208105104621, 0.012043926980302464, 0.010282716872948027, 0.008702740769447388, 0.007296719774748089, 0.006056044907394079, 0.0049710207362835285, 0.004031108835439411, 0.003225166380287162, 0.0025416755920456883, 0.001968960196673105, 0.0014953855867247238, 0.0011095399428924942, 0.0008003941708179558, 0.00055743912185941, 0.0003707991780740096, 0.00023132187674409872, 0.00013064381447128748, 6.123359277961564e-05] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y90_kaiser_I_wf_qp_control_c3t2": {
            "type": "arbitrary",
            "samples": [0.0] * 100,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "y90_kaiser_Q_wf_qp_control_c3t2": {
            "type": "arbitrary",
            "samples": [3.061679638980782e-05, 6.532190723564394e-05, 0.00011566093837204924, 0.0001853995890370048, 0.0002787195609297057, 0.0004001970854089772, 0.0005547699714462471, 0.0007476927933623619, 0.0009844800983365512, 0.0012708377960228441, 0.001612583190143581, 0.0020155544177197023, 0.0024855103681417643, 0.0030280224536970396, 0.003648359887374041, 0.004351370384723694, 0.005141358436474014, 0.006021963490151232, 0.006996040525523105, 0.008065545604508713, 0.009231429016631038, 0.010493538622702324, 0.011850535920178554, 0.013299827212922373, 0.014837512066932575, 0.016458350974447707, 0.018155753835766026, 0.019921790506671644, 0.02174722425642136, 0.023621568544962765, 0.025533167067605902, 0.027469296540794302, 0.029416291224546955, 0.031359687706557345, 0.03328438802089931, 0.03517483875165445, 0.037015223388917905, 0.03878966487117647, 0.04048243497259204, 0.04207816698364042, 0.04356206799476007, 0.044920127029484, 0.046139315288504214, 0.047207774860015456, 0.04811499242335274, 0.04885195471940834, 0.04941128287779857, 0.04978734307077841] + [0.04997633139944227] * 2 + [0.04978734307077841, 0.04941128287779857, 0.04885195471940834, 0.04811499242335274, 0.047207774860015456, 0.046139315288504214, 0.044920127029484, 0.04356206799476007, 0.04207816698364042, 0.0404824349725921, 0.03878966487117647, 0.037015223388917905, 0.03517483875165445, 0.03328438802089931, 0.031359687706557345, 0.029416291224546955, 0.027469296540794302, 0.025533167067605902, 0.023621568544962807, 0.02174722425642136, 0.019921790506671644, 0.018155753835766057, 0.016458350974447707, 0.014837512066932575, 0.013299827212922373, 0.011850535920178554, 0.010493538622702324, 0.009231429016631038, 0.008065545604508713, 0.006996040525523105, 0.006021963490151232, 0.005141358436474014, 0.004351370384723694, 0.0036483598873740444, 0.0030280224536970396, 0.0024855103681417643, 0.0020155544177197053, 0.001612583190143581, 0.0012708377960228441, 0.0009844800983365525, 0.0007476927933623619, 0.0005547699714462471, 0.0004001970854089779, 0.000278719560929705, 0.0001853995890370048, 0.00011566093837204936, 6.532190723564374e-05, 3.061679638980782e-05] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_y90_kaiser_I_wf_qp_control_c3t2": {
            "type": "arbitrary",
            "samples": [0.0] * 100,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "minus_y90_kaiser_Q_wf_qp_control_c3t2": {
            "type": "arbitrary",
            "samples": [-3.061679638980782e-05, -6.532190723564394e-05, -0.00011566093837204924, -0.0001853995890370048, -0.0002787195609297057, -0.0004001970854089772, -0.0005547699714462471, -0.0007476927933623619, -0.0009844800983365512, -0.0012708377960228441, -0.001612583190143581, -0.0020155544177197023, -0.0024855103681417643, -0.0030280224536970396, -0.003648359887374041, -0.004351370384723694, -0.005141358436474014, -0.006021963490151232, -0.006996040525523105, -0.008065545604508713, -0.009231429016631038, -0.010493538622702324, -0.011850535920178554, -0.013299827212922373, -0.014837512066932575, -0.016458350974447707, -0.018155753835766026, -0.019921790506671644, -0.02174722425642136, -0.023621568544962765, -0.025533167067605902, -0.027469296540794302, -0.029416291224546955, -0.031359687706557345, -0.03328438802089931, -0.03517483875165445, -0.037015223388917905, -0.03878966487117647, -0.04048243497259204, -0.04207816698364042, -0.04356206799476007, -0.044920127029484, -0.046139315288504214, -0.047207774860015456, -0.04811499242335274, -0.04885195471940834, -0.04941128287779857, -0.04978734307077841] + [-0.04997633139944227] * 2 + [-0.04978734307077841, -0.04941128287779857, -0.04885195471940834, -0.04811499242335274, -0.047207774860015456, -0.046139315288504214, -0.044920127029484, -0.04356206799476007, -0.04207816698364042, -0.0404824349725921, -0.03878966487117647, -0.037015223388917905, -0.03517483875165445, -0.03328438802089931, -0.031359687706557345, -0.029416291224546955, -0.027469296540794302, -0.025533167067605902, -0.023621568544962807, -0.02174722425642136, -0.019921790506671644, -0.018155753835766057, -0.016458350974447707, -0.014837512066932575, -0.013299827212922373, -0.011850535920178554, -0.010493538622702324, -0.009231429016631038, -0.008065545604508713, -0.006996040525523105, -0.006021963490151232, -0.005141358436474014, -0.004351370384723694, -0.0036483598873740444, -0.0030280224536970396, -0.0024855103681417643, -0.0020155544177197053, -0.001612583190143581, -0.0012708377960228441, -0.0009844800983365525, -0.0007476927933623619, -0.0005547699714462471, -0.0004001970854089779, -0.000278719560929705, -0.0001853995890370048, -0.00011566093837204936, -6.532190723564374e-05, -3.061679638980782e-05] + [0.0] * 2,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "step_wf": {
            "type": "constant",
            "sample": 0.25,
        },
        "P1_sticky_step%_wf": {
            "type": "constant",
            "sample": 0.25,
        },
        "P2_sticky_step%_wf": {
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
        "cosine_weights_tank_circuit1": {
            "cosine": [(1.0, 400)],
            "sine": [(0.0, 400)],
        },
        "cosine_weights_tank_circuit2": {
            "cosine": [(1.0, 400)],
            "sine": [(0.0, 400)],
        },
        "sine_weights_tank_circuit1": {
            "cosine": [(0.0, 400)],
            "sine": [(1.0, 400)],
        },
        "sine_weights_tank_circuit2": {
            "cosine": [(0.0, 400)],
            "sine": [(1.0, 400)],
        },
    },
    "mixers": {
        "mixer_qubit1": [{'intermediate_frequency': 0, 'lo_frequency': 16000000000.0, 'correction': (1.0, 0.0, 0.0, 1.0)}],
        "mixer_qubit2": [{'intermediate_frequency': 0, 'lo_frequency': 16000000000.0, 'correction': (1.0, 0.0, 0.0, 1.0)}],
        "mixer_qubit3": [{'intermediate_frequency': 0, 'lo_frequency': 16300000000.0, 'correction': (1.0, 0.0, 0.0, 1.0)}],
        "mixer_qubit4": [{'intermediate_frequency': 50000000.0, 'lo_frequency': 16300000000.0, 'correction': (1.0, 0.0, 0.0, 1.0)}],
        "mixer_qubit5": [{'intermediate_frequency': 0, 'lo_frequency': 16300000000.0, 'correction': (1.0, 0.0, 0.0, 1.0)}],
        "mixer_qp_control_c3t2": [{'intermediate_frequency': 0, 'lo_frequency': 16300000000.0, 'correction': (1.0, 0.0, 0.0, 1.0)}],
    },
}


