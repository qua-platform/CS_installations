
# Single QUA script generated at 2025-03-18 13:20:25.583474
# QUA library version: 1.2.2a3

from qm import CompilerOptionArguments
from qm.qua import *

with program() as prog:
    v1 = declare(int, )
    v2 = declare(int, )
    v3 = declare(fixed, )
    v4 = declare(fixed, )
    with infinite_loop_():
        play("const", "qubit_con1-fem1-port3-duc1")
        align("resonator_con1-fem1-port2-duc1", "qubit_con1-fem1-port3-duc1")
        measure("readout", "resonator_con1-fem1-port2-duc1", dual_demod.full("cos", "sin", v3), dual_demod.full("minus_sin", "cos", v4))
        align("resonator_con1-fem1-port2-duc1", "qubit_con1-fem1-port3-duc1")
        with if_((v3>0)):
            update_frequency("qubit_con1-fem1-port3-duc1", 150000000, "Hz", False)
        play("const", "qubit_con1-fem1-port3-duc1")
        wait(500, "resonator_con1-fem1-port2-duc1")


config = {
    "version": 1,
    "controllers": {
        "con1": {
            "type": "opx1000",
            "fems": {
                "1": {
                    "type": "MW",
                    "analog_inputs": {
                        "1": {
                            "sampling_rate": 1000000000.0,
                            "band": 1,
                            "gain_db": 1,
                            "downconverter_frequency": 900000000,
                        },
                        "2": {
                            "sampling_rate": 1000000000.0,
                            "band": 1,
                            "gain_db": 1,
                            "downconverter_frequency": 900000000,
                        },
                    },
                    "analog_outputs": {
                        "1": {
                            "sampling_rate": 1000000000.0,
                            "band": 1,
                            "full_scale_power_dbm": 1,
                            "upconverters": {
                                "1": {
                                    "frequency": 450000000,
                                },
                                "2": {
                                    "frequency": 1900000000,
                                },
                            },
                        },
                        "2": {
                            "sampling_rate": 1000000000.0,
                            "band": 1,
                            "full_scale_power_dbm": 1,
                            "upconverters": {
                                "1": {
                                    "frequency": 450000000,
                                },
                                "2": {
                                    "frequency": 1900000000,
                                },
                            },
                        },
                        "3": {
                            "sampling_rate": 1000000000.0,
                            "band": 1,
                            "full_scale_power_dbm": 1,
                            "upconverters": {
                                "1": {
                                    "frequency": 450000000,
                                },
                                "2": {
                                    "frequency": 1900000000,
                                },
                            },
                        },
                        "4": {
                            "sampling_rate": 1000000000.0,
                            "band": 1,
                            "full_scale_power_dbm": 1,
                            "upconverters": {
                                "1": {
                                    "frequency": 450000000,
                                },
                                "2": {
                                    "frequency": 1900000000,
                                },
                            },
                        },
                        "5": {
                            "sampling_rate": 1000000000.0,
                            "band": 1,
                            "full_scale_power_dbm": 1,
                            "upconverters": {
                                "1": {
                                    "frequency": 450000000,
                                },
                                "2": {
                                    "frequency": 1900000000,
                                },
                            },
                        },
                        "6": {
                            "sampling_rate": 1000000000.0,
                            "band": 1,
                            "full_scale_power_dbm": 1,
                            "upconverters": {
                                "1": {
                                    "frequency": 450000000,
                                },
                                "2": {
                                    "frequency": 1900000000,
                                },
                            },
                        },
                        "7": {
                            "sampling_rate": 1000000000.0,
                            "band": 1,
                            "full_scale_power_dbm": 1,
                            "upconverters": {
                                "1": {
                                    "frequency": 450000000,
                                },
                                "2": {
                                    "frequency": 1900000000,
                                },
                            },
                        },
                        "8": {
                            "sampling_rate": 1000000000.0,
                            "band": 1,
                            "full_scale_power_dbm": 1,
                            "upconverters": {
                                "1": {
                                    "frequency": 450000000,
                                },
                                "2": {
                                    "frequency": 1900000000,
                                },
                            },
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
                        "8": {},
                    },
                },
                "2": {
                    "type": "MW",
                    "analog_inputs": {
                        "1": {
                            "sampling_rate": 1000000000.0,
                            "band": 1,
                            "gain_db": 1,
                            "downconverter_frequency": 900000000,
                        },
                        "2": {
                            "sampling_rate": 1000000000.0,
                            "band": 1,
                            "gain_db": 1,
                            "downconverter_frequency": 900000000,
                        },
                    },
                    "analog_outputs": {
                        "1": {
                            "sampling_rate": 1000000000.0,
                            "band": 1,
                            "full_scale_power_dbm": 1,
                            "upconverters": {
                                "1": {
                                    "frequency": 450000000,
                                },
                                "2": {
                                    "frequency": 1900000000,
                                },
                            },
                        },
                        "2": {
                            "sampling_rate": 1000000000.0,
                            "band": 1,
                            "full_scale_power_dbm": 1,
                            "upconverters": {
                                "1": {
                                    "frequency": 450000000,
                                },
                                "2": {
                                    "frequency": 1900000000,
                                },
                            },
                        },
                        "3": {
                            "sampling_rate": 1000000000.0,
                            "band": 1,
                            "full_scale_power_dbm": 1,
                            "upconverters": {
                                "1": {
                                    "frequency": 450000000,
                                },
                                "2": {
                                    "frequency": 1900000000,
                                },
                            },
                        },
                        "4": {
                            "sampling_rate": 1000000000.0,
                            "band": 1,
                            "full_scale_power_dbm": 1,
                            "upconverters": {
                                "1": {
                                    "frequency": 450000000,
                                },
                                "2": {
                                    "frequency": 1900000000,
                                },
                            },
                        },
                        "5": {
                            "sampling_rate": 1000000000.0,
                            "band": 1,
                            "full_scale_power_dbm": 1,
                            "upconverters": {
                                "1": {
                                    "frequency": 450000000,
                                },
                                "2": {
                                    "frequency": 1900000000,
                                },
                            },
                        },
                        "6": {
                            "sampling_rate": 1000000000.0,
                            "band": 1,
                            "full_scale_power_dbm": 1,
                            "upconverters": {
                                "1": {
                                    "frequency": 450000000,
                                },
                                "2": {
                                    "frequency": 1900000000,
                                },
                            },
                        },
                        "7": {
                            "sampling_rate": 1000000000.0,
                            "band": 1,
                            "full_scale_power_dbm": 1,
                            "upconverters": {
                                "1": {
                                    "frequency": 450000000,
                                },
                                "2": {
                                    "frequency": 1900000000,
                                },
                            },
                        },
                        "8": {
                            "sampling_rate": 1000000000.0,
                            "band": 1,
                            "full_scale_power_dbm": 1,
                            "upconverters": {
                                "1": {
                                    "frequency": 450000000,
                                },
                                "2": {
                                    "frequency": 1900000000,
                                },
                            },
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
                        "8": {},
                    },
                },
            },
        },
    },
    "elements": {
        "qubit_con1-fem1-port1-duc1": {
            "MWInput": {
                "port": ('con1', 1, 1),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000,
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "core": "con1-fem1-port1-duc1",
        },
        "qubit_con1-fem2-port1-duc1": {
            "MWInput": {
                "port": ('con1', 2, 1),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000,
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "core": "con1-fem2-port1-duc1",
        },
        "qubit_con1-fem1-port2-duc1": {
            "MWInput": {
                "port": ('con1', 1, 2),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000,
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "core": "con1-fem1-port2-duc1",
        },
        "qubit_con1-fem2-port2-duc1": {
            "MWInput": {
                "port": ('con1', 2, 2),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000,
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "core": "con1-fem2-port2-duc1",
        },
        "qubit_con1-fem1-port3-duc1": {
            "MWInput": {
                "port": ('con1', 1, 3),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000,
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "core": "con1-fem1-port3-duc1",
        },
        "qubit_con1-fem2-port3-duc1": {
            "MWInput": {
                "port": ('con1', 2, 3),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000,
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "core": "con1-fem2-port3-duc1",
        },
        "qubit_con1-fem1-port4-duc1": {
            "MWInput": {
                "port": ('con1', 1, 4),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000,
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "core": "con1-fem1-port4-duc1",
        },
        "qubit_con1-fem2-port4-duc1": {
            "MWInput": {
                "port": ('con1', 2, 4),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000,
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "core": "con1-fem2-port4-duc1",
        },
        "qubit_con1-fem1-port5-duc1": {
            "MWInput": {
                "port": ('con1', 1, 5),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000,
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "core": "con1-fem1-port5-duc1",
        },
        "qubit_con1-fem2-port5-duc1": {
            "MWInput": {
                "port": ('con1', 2, 5),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000,
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "core": "con1-fem2-port5-duc1",
        },
        "qubit_con1-fem1-port6-duc1": {
            "MWInput": {
                "port": ('con1', 1, 6),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000,
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "core": "con1-fem1-port6-duc1",
        },
        "qubit_con1-fem2-port6-duc1": {
            "MWInput": {
                "port": ('con1', 2, 6),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000,
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "core": "con1-fem2-port6-duc1",
        },
        "qubit_con1-fem1-port7-duc1": {
            "MWInput": {
                "port": ('con1', 1, 7),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000,
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "core": "con1-fem1-port7-duc1",
        },
        "qubit_con1-fem2-port7-duc1": {
            "MWInput": {
                "port": ('con1', 2, 7),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000,
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "core": "con1-fem2-port7-duc1",
        },
        "qubit_con1-fem1-port8-duc1": {
            "MWInput": {
                "port": ('con1', 1, 8),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000,
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "core": "con1-fem1-port8-duc1",
        },
        "qubit_con1-fem2-port8-duc1": {
            "MWInput": {
                "port": ('con1', 2, 8),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000,
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "core": "con1-fem2-port8-duc1",
        },
        "qubit_con1-fem1-port1-duc2": {
            "MWInput": {
                "port": ('con1', 1, 1),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000,
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "core": "con1-fem1-port1-duc1",
        },
        "qubit_con1-fem2-port1-duc2": {
            "MWInput": {
                "port": ('con1', 2, 1),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000,
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "core": "con1-fem2-port1-duc1",
        },
        "qubit_con1-fem1-port2-duc2": {
            "MWInput": {
                "port": ('con1', 1, 2),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000,
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "core": "con1-fem1-port2-duc1",
        },
        "qubit_con1-fem2-port2-duc2": {
            "MWInput": {
                "port": ('con1', 2, 2),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000,
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "core": "con1-fem2-port2-duc1",
        },
        "qubit_con1-fem1-port3-duc2": {
            "MWInput": {
                "port": ('con1', 1, 3),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000,
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "core": "con1-fem1-port3-duc1",
        },
        "qubit_con1-fem2-port3-duc2": {
            "MWInput": {
                "port": ('con1', 2, 3),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000,
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "core": "con1-fem2-port3-duc1",
        },
        "qubit_con1-fem1-port4-duc2": {
            "MWInput": {
                "port": ('con1', 1, 4),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000,
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "core": "con1-fem1-port4-duc1",
        },
        "qubit_con1-fem2-port4-duc2": {
            "MWInput": {
                "port": ('con1', 2, 4),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000,
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "core": "con1-fem2-port4-duc1",
        },
        "qubit_con1-fem1-port5-duc2": {
            "MWInput": {
                "port": ('con1', 1, 5),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000,
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "core": "con1-fem1-port5-duc1",
        },
        "qubit_con1-fem2-port5-duc2": {
            "MWInput": {
                "port": ('con1', 2, 5),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000,
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "core": "con1-fem2-port5-duc1",
        },
        "qubit_con1-fem1-port6-duc2": {
            "MWInput": {
                "port": ('con1', 1, 6),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000,
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "core": "con1-fem1-port6-duc1",
        },
        "qubit_con1-fem2-port6-duc2": {
            "MWInput": {
                "port": ('con1', 2, 6),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000,
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "core": "con1-fem2-port6-duc1",
        },
        "qubit_con1-fem1-port7-duc2": {
            "MWInput": {
                "port": ('con1', 1, 7),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000,
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "core": "con1-fem1-port7-duc1",
        },
        "qubit_con1-fem2-port7-duc2": {
            "MWInput": {
                "port": ('con1', 2, 7),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000,
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "core": "con1-fem2-port7-duc1",
        },
        "qubit_con1-fem1-port8-duc2": {
            "MWInput": {
                "port": ('con1', 1, 8),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000,
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "core": "con1-fem1-port8-duc1",
        },
        "qubit_con1-fem2-port8-duc2": {
            "MWInput": {
                "port": ('con1', 2, 8),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000,
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "core": "con1-fem2-port8-duc1",
        },
        "qubit_con1-fem1-port1-duc1-twin": {
            "MWInput": {
                "port": ('con1', 1, 1),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000,
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "core": "con1-fem1-port1-duc1",
        },
        "qubit_con1-fem2-port1-duc1-twin": {
            "MWInput": {
                "port": ('con1', 2, 1),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000,
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "core": "con1-fem2-port1-duc1",
        },
        "qubit_con1-fem1-port2-duc1-twin": {
            "MWInput": {
                "port": ('con1', 1, 2),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000,
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "core": "con1-fem1-port2-duc1",
        },
        "qubit_con1-fem2-port2-duc1-twin": {
            "MWInput": {
                "port": ('con1', 2, 2),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000,
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "core": "con1-fem2-port2-duc1",
        },
        "qubit_con1-fem1-port3-duc1-twin": {
            "MWInput": {
                "port": ('con1', 1, 3),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000,
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "core": "con1-fem1-port3-duc1",
        },
        "qubit_con1-fem2-port3-duc1-twin": {
            "MWInput": {
                "port": ('con1', 2, 3),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000,
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "core": "con1-fem2-port3-duc1",
        },
        "qubit_con1-fem1-port4-duc1-twin": {
            "MWInput": {
                "port": ('con1', 1, 4),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000,
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "core": "con1-fem1-port4-duc1",
        },
        "qubit_con1-fem2-port4-duc1-twin": {
            "MWInput": {
                "port": ('con1', 2, 4),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000,
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "core": "con1-fem2-port4-duc1",
        },
        "qubit_con1-fem1-port5-duc1-twin": {
            "MWInput": {
                "port": ('con1', 1, 5),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000,
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "core": "con1-fem1-port5-duc1",
        },
        "qubit_con1-fem2-port5-duc1-twin": {
            "MWInput": {
                "port": ('con1', 2, 5),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000,
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "core": "con1-fem2-port5-duc1",
        },
        "qubit_con1-fem1-port6-duc1-twin": {
            "MWInput": {
                "port": ('con1', 1, 6),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000,
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "core": "con1-fem1-port6-duc1",
        },
        "qubit_con1-fem2-port6-duc1-twin": {
            "MWInput": {
                "port": ('con1', 2, 6),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000,
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "core": "con1-fem2-port6-duc1",
        },
        "qubit_con1-fem1-port7-duc1-twin": {
            "MWInput": {
                "port": ('con1', 1, 7),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000,
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "core": "con1-fem1-port7-duc1",
        },
        "qubit_con1-fem2-port7-duc1-twin": {
            "MWInput": {
                "port": ('con1', 2, 7),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000,
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "core": "con1-fem2-port7-duc1",
        },
        "qubit_con1-fem1-port8-duc1-twin": {
            "MWInput": {
                "port": ('con1', 1, 8),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000,
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "core": "con1-fem1-port8-duc1",
        },
        "qubit_con1-fem2-port8-duc1-twin": {
            "MWInput": {
                "port": ('con1', 2, 8),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000,
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "core": "con1-fem2-port8-duc1",
        },
        "qubit_con1-fem1-port1-duc2-twin": {
            "MWInput": {
                "port": ('con1', 1, 1),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000,
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "core": "con1-fem1-port1-duc1",
        },
        "qubit_con1-fem2-port1-duc2-twin": {
            "MWInput": {
                "port": ('con1', 2, 1),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000,
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "core": "con1-fem2-port1-duc1",
        },
        "qubit_con1-fem1-port2-duc2-twin": {
            "MWInput": {
                "port": ('con1', 1, 2),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000,
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "core": "con1-fem1-port2-duc1",
        },
        "qubit_con1-fem2-port2-duc2-twin": {
            "MWInput": {
                "port": ('con1', 2, 2),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000,
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "core": "con1-fem2-port2-duc1",
        },
        "qubit_con1-fem1-port3-duc2-twin": {
            "MWInput": {
                "port": ('con1', 1, 3),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000,
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "core": "con1-fem1-port3-duc1",
        },
        "qubit_con1-fem2-port3-duc2-twin": {
            "MWInput": {
                "port": ('con1', 2, 3),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000,
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "core": "con1-fem2-port3-duc1",
        },
        "qubit_con1-fem1-port4-duc2-twin": {
            "MWInput": {
                "port": ('con1', 1, 4),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000,
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "core": "con1-fem1-port4-duc1",
        },
        "qubit_con1-fem2-port4-duc2-twin": {
            "MWInput": {
                "port": ('con1', 2, 4),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000,
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "core": "con1-fem2-port4-duc1",
        },
        "qubit_con1-fem1-port5-duc2-twin": {
            "MWInput": {
                "port": ('con1', 1, 5),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000,
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "core": "con1-fem1-port5-duc1",
        },
        "qubit_con1-fem2-port5-duc2-twin": {
            "MWInput": {
                "port": ('con1', 2, 5),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000,
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "core": "con1-fem2-port5-duc1",
        },
        "qubit_con1-fem1-port6-duc2-twin": {
            "MWInput": {
                "port": ('con1', 1, 6),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000,
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "core": "con1-fem1-port6-duc1",
        },
        "qubit_con1-fem2-port6-duc2-twin": {
            "MWInput": {
                "port": ('con1', 2, 6),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000,
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "core": "con1-fem2-port6-duc1",
        },
        "qubit_con1-fem1-port7-duc2-twin": {
            "MWInput": {
                "port": ('con1', 1, 7),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000,
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "core": "con1-fem1-port7-duc1",
        },
        "qubit_con1-fem2-port7-duc2-twin": {
            "MWInput": {
                "port": ('con1', 2, 7),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000,
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "core": "con1-fem2-port7-duc1",
        },
        "qubit_con1-fem1-port8-duc2-twin": {
            "MWInput": {
                "port": ('con1', 1, 8),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000,
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "core": "con1-fem1-port8-duc1",
        },
        "qubit_con1-fem2-port8-duc2-twin": {
            "MWInput": {
                "port": ('con1', 2, 8),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000,
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "core": "con1-fem2-port8-duc1",
        },
        "resonator_con1-fem1-port1-duc1": {
            "MWInput": {
                "port": ('con1', 1, 1),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000,
            "MWOutput": {
                "port": ('con1', 1, 1),
            },
            "time_of_flight": 300,
            "smearing": 0,
            "operations": {
                "const": "const_pulse",
                "readout": "readout_pulse",
                "arb": "arb_pulse",
            },
            "core": "con1-fem1-port1-duc1",
        },
        "resonator_con1-fem2-port1-duc1": {
            "MWInput": {
                "port": ('con1', 2, 1),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000,
            "MWOutput": {
                "port": ('con1', 2, 1),
            },
            "time_of_flight": 300,
            "smearing": 0,
            "operations": {
                "const": "const_pulse",
                "readout": "readout_pulse",
                "arb": "arb_pulse",
            },
            "core": "con1-fem2-port1-duc1",
        },
        "resonator_con1-fem1-port2-duc1": {
            "MWInput": {
                "port": ('con1', 1, 2),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000,
            "MWOutput": {
                "port": ('con1', 1, 1),
            },
            "time_of_flight": 300,
            "smearing": 0,
            "operations": {
                "const": "const_pulse",
                "readout": "readout_pulse",
                "arb": "arb_pulse",
            },
            "core": "con1-fem1-port2-duc1",
        },
        "resonator_con1-fem2-port2-duc1": {
            "MWInput": {
                "port": ('con1', 2, 2),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000,
            "MWOutput": {
                "port": ('con1', 2, 1),
            },
            "time_of_flight": 300,
            "smearing": 0,
            "operations": {
                "const": "const_pulse",
                "readout": "readout_pulse",
                "arb": "arb_pulse",
            },
            "core": "con1-fem2-port2-duc1",
        },
        "resonator_con1-fem1-port3-duc1": {
            "MWInput": {
                "port": ('con1', 1, 3),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000,
            "MWOutput": {
                "port": ('con1', 1, 1),
            },
            "time_of_flight": 300,
            "smearing": 0,
            "operations": {
                "const": "const_pulse",
                "readout": "readout_pulse",
                "arb": "arb_pulse",
            },
            "core": "con1-fem1-port3-duc1",
        },
        "resonator_con1-fem2-port3-duc1": {
            "MWInput": {
                "port": ('con1', 2, 3),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000,
            "MWOutput": {
                "port": ('con1', 2, 1),
            },
            "time_of_flight": 300,
            "smearing": 0,
            "operations": {
                "const": "const_pulse",
                "readout": "readout_pulse",
                "arb": "arb_pulse",
            },
            "core": "con1-fem2-port3-duc1",
        },
        "resonator_con1-fem1-port4-duc1": {
            "MWInput": {
                "port": ('con1', 1, 4),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000,
            "MWOutput": {
                "port": ('con1', 1, 1),
            },
            "time_of_flight": 300,
            "smearing": 0,
            "operations": {
                "const": "const_pulse",
                "readout": "readout_pulse",
                "arb": "arb_pulse",
            },
            "core": "con1-fem1-port4-duc1",
        },
        "resonator_con1-fem2-port4-duc1": {
            "MWInput": {
                "port": ('con1', 2, 4),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000,
            "MWOutput": {
                "port": ('con1', 2, 1),
            },
            "time_of_flight": 300,
            "smearing": 0,
            "operations": {
                "const": "const_pulse",
                "readout": "readout_pulse",
                "arb": "arb_pulse",
            },
            "core": "con1-fem2-port4-duc1",
        },
        "resonator_con1-fem1-port5-duc1": {
            "MWInput": {
                "port": ('con1', 1, 5),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000,
            "MWOutput": {
                "port": ('con1', 1, 2),
            },
            "time_of_flight": 300,
            "smearing": 0,
            "operations": {
                "const": "const_pulse",
                "readout": "readout_pulse",
                "arb": "arb_pulse",
            },
            "core": "con1-fem1-port5-duc1",
        },
        "resonator_con1-fem2-port5-duc1": {
            "MWInput": {
                "port": ('con1', 2, 5),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000,
            "MWOutput": {
                "port": ('con1', 2, 2),
            },
            "time_of_flight": 300,
            "smearing": 0,
            "operations": {
                "const": "const_pulse",
                "readout": "readout_pulse",
                "arb": "arb_pulse",
            },
            "core": "con1-fem2-port5-duc1",
        },
        "resonator_con1-fem1-port6-duc1": {
            "MWInput": {
                "port": ('con1', 1, 6),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000,
            "MWOutput": {
                "port": ('con1', 1, 2),
            },
            "time_of_flight": 300,
            "smearing": 0,
            "operations": {
                "const": "const_pulse",
                "readout": "readout_pulse",
                "arb": "arb_pulse",
            },
            "core": "con1-fem1-port6-duc1",
        },
        "resonator_con1-fem2-port6-duc1": {
            "MWInput": {
                "port": ('con1', 2, 6),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000,
            "MWOutput": {
                "port": ('con1', 2, 2),
            },
            "time_of_flight": 300,
            "smearing": 0,
            "operations": {
                "const": "const_pulse",
                "readout": "readout_pulse",
                "arb": "arb_pulse",
            },
            "core": "con1-fem2-port6-duc1",
        },
        "resonator_con1-fem1-port7-duc1": {
            "MWInput": {
                "port": ('con1', 1, 7),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000,
            "MWOutput": {
                "port": ('con1', 1, 2),
            },
            "time_of_flight": 300,
            "smearing": 0,
            "operations": {
                "const": "const_pulse",
                "readout": "readout_pulse",
                "arb": "arb_pulse",
            },
            "core": "con1-fem1-port7-duc1",
        },
        "resonator_con1-fem2-port7-duc1": {
            "MWInput": {
                "port": ('con1', 2, 7),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000,
            "MWOutput": {
                "port": ('con1', 2, 2),
            },
            "time_of_flight": 300,
            "smearing": 0,
            "operations": {
                "const": "const_pulse",
                "readout": "readout_pulse",
                "arb": "arb_pulse",
            },
            "core": "con1-fem2-port7-duc1",
        },
        "resonator_con1-fem1-port8-duc1": {
            "MWInput": {
                "port": ('con1', 1, 8),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000,
            "MWOutput": {
                "port": ('con1', 1, 2),
            },
            "time_of_flight": 300,
            "smearing": 0,
            "operations": {
                "const": "const_pulse",
                "readout": "readout_pulse",
                "arb": "arb_pulse",
            },
            "core": "con1-fem1-port8-duc1",
        },
        "resonator_con1-fem2-port8-duc1": {
            "MWInput": {
                "port": ('con1', 2, 8),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000,
            "MWOutput": {
                "port": ('con1', 2, 2),
            },
            "time_of_flight": 300,
            "smearing": 0,
            "operations": {
                "const": "const_pulse",
                "readout": "readout_pulse",
                "arb": "arb_pulse",
            },
            "core": "con1-fem2-port8-duc1",
        },
        "jpa_con1-fem1-port1": {
            "MWInput": {
                "port": ('con1', 1, 1),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000,
            "operations": {
                "const": "const_pulse",
            },
        },
        "jpa_con1-fem2-port1": {
            "MWInput": {
                "port": ('con1', 2, 1),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000,
            "operations": {
                "const": "const_pulse",
            },
        },
        "jpa_con1-fem1-port2": {
            "MWInput": {
                "port": ('con1', 1, 2),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000,
            "operations": {
                "const": "const_pulse",
            },
        },
        "jpa_con1-fem2-port2": {
            "MWInput": {
                "port": ('con1', 2, 2),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000,
            "operations": {
                "const": "const_pulse",
            },
        },
        "jpa_con1-fem1-port3": {
            "MWInput": {
                "port": ('con1', 1, 3),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000,
            "operations": {
                "const": "const_pulse",
            },
        },
        "jpa_con1-fem2-port3": {
            "MWInput": {
                "port": ('con1', 2, 3),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000,
            "operations": {
                "const": "const_pulse",
            },
        },
        "jpa_con1-fem1-port4": {
            "MWInput": {
                "port": ('con1', 1, 4),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000,
            "operations": {
                "const": "const_pulse",
            },
        },
        "jpa_con1-fem2-port4": {
            "MWInput": {
                "port": ('con1', 2, 4),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000,
            "operations": {
                "const": "const_pulse",
            },
        },
        "jpa_con1-fem1-port5": {
            "MWInput": {
                "port": ('con1', 1, 5),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000,
            "operations": {
                "const": "const_pulse",
            },
        },
        "jpa_con1-fem2-port5": {
            "MWInput": {
                "port": ('con1', 2, 5),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000,
            "operations": {
                "const": "const_pulse",
            },
        },
        "jpa_con1-fem1-port6": {
            "MWInput": {
                "port": ('con1', 1, 6),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000,
            "operations": {
                "const": "const_pulse",
            },
        },
        "jpa_con1-fem2-port6": {
            "MWInput": {
                "port": ('con1', 2, 6),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000,
            "operations": {
                "const": "const_pulse",
            },
        },
        "jpa_con1-fem1-port7": {
            "MWInput": {
                "port": ('con1', 1, 7),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000,
            "operations": {
                "const": "const_pulse",
            },
        },
        "jpa_con1-fem2-port7": {
            "MWInput": {
                "port": ('con1', 2, 7),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000,
            "operations": {
                "const": "const_pulse",
            },
        },
        "jpa_con1-fem1-port8": {
            "MWInput": {
                "port": ('con1', 1, 8),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000,
            "operations": {
                "const": "const_pulse",
            },
        },
        "jpa_con1-fem2-port8": {
            "MWInput": {
                "port": ('con1', 2, 8),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000,
            "operations": {
                "const": "const_pulse",
            },
        },
        "trigger_con1-fem1-port1": {
            "digitalInputs": {
                "marker": {
                    "port": ('con1', 1, 1),
                    "delay": 0,
                    "buffer": 0,
                },
            },
            "operations": {
                "on": "trigger_pulse",
            },
        },
        "trigger_con1-fem2-port1": {
            "digitalInputs": {
                "marker": {
                    "port": ('con1', 2, 1),
                    "delay": 0,
                    "buffer": 0,
                },
            },
            "operations": {
                "on": "trigger_pulse",
            },
        },
        "trigger_con1-fem1-port2": {
            "digitalInputs": {
                "marker": {
                    "port": ('con1', 1, 2),
                    "delay": 0,
                    "buffer": 0,
                },
            },
            "operations": {
                "on": "trigger_pulse",
            },
        },
        "trigger_con1-fem2-port2": {
            "digitalInputs": {
                "marker": {
                    "port": ('con1', 2, 2),
                    "delay": 0,
                    "buffer": 0,
                },
            },
            "operations": {
                "on": "trigger_pulse",
            },
        },
        "trigger_con1-fem1-port3": {
            "digitalInputs": {
                "marker": {
                    "port": ('con1', 1, 3),
                    "delay": 0,
                    "buffer": 0,
                },
            },
            "operations": {
                "on": "trigger_pulse",
            },
        },
        "trigger_con1-fem2-port3": {
            "digitalInputs": {
                "marker": {
                    "port": ('con1', 2, 3),
                    "delay": 0,
                    "buffer": 0,
                },
            },
            "operations": {
                "on": "trigger_pulse",
            },
        },
        "trigger_con1-fem1-port4": {
            "digitalInputs": {
                "marker": {
                    "port": ('con1', 1, 4),
                    "delay": 0,
                    "buffer": 0,
                },
            },
            "operations": {
                "on": "trigger_pulse",
            },
        },
        "trigger_con1-fem2-port4": {
            "digitalInputs": {
                "marker": {
                    "port": ('con1', 2, 4),
                    "delay": 0,
                    "buffer": 0,
                },
            },
            "operations": {
                "on": "trigger_pulse",
            },
        },
        "trigger_con1-fem1-port5": {
            "digitalInputs": {
                "marker": {
                    "port": ('con1', 1, 5),
                    "delay": 0,
                    "buffer": 0,
                },
            },
            "operations": {
                "on": "trigger_pulse",
            },
        },
        "trigger_con1-fem2-port5": {
            "digitalInputs": {
                "marker": {
                    "port": ('con1', 2, 5),
                    "delay": 0,
                    "buffer": 0,
                },
            },
            "operations": {
                "on": "trigger_pulse",
            },
        },
        "trigger_con1-fem1-port6": {
            "digitalInputs": {
                "marker": {
                    "port": ('con1', 1, 6),
                    "delay": 0,
                    "buffer": 0,
                },
            },
            "operations": {
                "on": "trigger_pulse",
            },
        },
        "trigger_con1-fem2-port6": {
            "digitalInputs": {
                "marker": {
                    "port": ('con1', 2, 6),
                    "delay": 0,
                    "buffer": 0,
                },
            },
            "operations": {
                "on": "trigger_pulse",
            },
        },
        "trigger_con1-fem1-port7": {
            "digitalInputs": {
                "marker": {
                    "port": ('con1', 1, 7),
                    "delay": 0,
                    "buffer": 0,
                },
            },
            "operations": {
                "on": "trigger_pulse",
            },
        },
        "trigger_con1-fem2-port7": {
            "digitalInputs": {
                "marker": {
                    "port": ('con1', 2, 7),
                    "delay": 0,
                    "buffer": 0,
                },
            },
            "operations": {
                "on": "trigger_pulse",
            },
        },
        "trigger_con1-fem1-port8": {
            "digitalInputs": {
                "marker": {
                    "port": ('con1', 1, 8),
                    "delay": 0,
                    "buffer": 0,
                },
            },
            "operations": {
                "on": "trigger_pulse",
            },
        },
        "trigger_con1-fem2-port8": {
            "digitalInputs": {
                "marker": {
                    "port": ('con1', 2, 8),
                    "delay": 0,
                    "buffer": 0,
                },
            },
            "operations": {
                "on": "trigger_pulse",
            },
        },
    },
    "pulses": {
        "const_pulse": {
            "length": 100,
            "operation": "control",
            "waveforms": {
                "I": "const_wf",
                "Q": "zero_wf",
            },
        },
        "gauss_x180_pulse": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "gauss_x180_I_wf",
                "Q": "gauss_x180_Q_wf",
            },
        },
        "gauss_y180_pulse": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "gauss_y180_I_wf",
                "Q": "gauss_y180_Q_wf",
            },
        },
        "gauss_x90_pulse": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "gauss_x90_I_wf",
                "Q": "gauss_x90_Q_wf",
            },
        },
        "gauss_minus_x90_pulse": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "gauss_minus_x90_I_wf",
                "Q": "gauss_minus_x90_Q_wf",
            },
        },
        "gauss_y90_pulse": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "gauss_y90_I_wf",
                "Q": "gauss_y90_Q_wf",
            },
        },
        "gauss_minus_y90_pulse": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "gauss_minus_y90_I_wf",
                "Q": "gauss_minus_y90_Q_wf",
            },
        },
        "gauss_rise_pulse": {
            "operation": "control",
            "length": 8,
            "waveforms": {
                "I": "gauss_rise_wf",
                "Q": "zero_wf",
            },
        },
        "gauss_fall_pulse": {
            "operation": "control",
            "length": 8,
            "waveforms": {
                "I": "gauss_fall_wf",
                "Q": "zero_wf",
            },
        },
        "arb_pulse": {
            "operation": "measurement",
            "length": 100,
            "waveforms": {
                "I": "arb_I_wf",
                "Q": "arb_Q_wf",
            },
            "integration_weights": {
                "cos": "cosine_arb_weights",
                "sin": "sine_arb_weights",
                "minus_sin": "minus_sine_arb_weights",
            },
            "digital_marker": "ON",
        },
        "readout_pulse": {
            "operation": "measurement",
            "length": 200,
            "waveforms": {
                "I": "readout_wf",
                "Q": "zero_wf",
            },
            "integration_weights": {
                "cos": "cosine_weights",
                "sin": "sine_weights",
                "minus_sin": "minus_sine_weights",
                "rotated_cos": "rotated_cosine_weights",
                "rotated_sin": "rotated_sine_weights",
                "rotated_minus_sin": "rotated_minus_sine_weights",
            },
            "digital_marker": "ON",
        },
        "trigger_pulse": {
            "operation": "control",
            "length": 1000,
            "digital_marker": "ON",
        },
    },
    "waveforms": {
        "const_wf": {
            "type": "constant",
            "sample": 0.5,
        },
        "zero_wf": {
            "type": "constant",
            "sample": 0.0,
        },
        "readout_wf": {
            "type": "constant",
            "sample": 0.5,
        },
        "gauss_x90_I_wf": {
            "type": "arbitrary",
            "samples": [0.0, 0.0022150469433227073, 0.005015813123173687, 0.008491584753998697, 0.012723560920712553, 0.017776666404548624, 0.023690402987698853, 0.030469425725473138, 0.03807475022143508, 0.04641664910656638, 0.05535034039512257, 0.06467547541850178, 0.0741401843068172, 0.08345003991731476, 0.09228178991126627, 0.10030113887181125, 0.10718331324880155, 0.11263469369056484, 0.11641352732340533] + [0.11834769134210223] * 2 + [0.11641352732340533, 0.11263469369056484, 0.10718331324880155, 0.10030113887181125, 0.09228178991126627, 0.08345003991731476, 0.0741401843068172, 0.06467547541850178, 0.05535034039512257, 0.04641664910656638, 0.03807475022143508, 0.030469425725473138, 0.023690402987698853, 0.017776666404548624, 0.012723560920712553, 0.008491584753998697, 0.005015813123173687, 0.0022150469433227073, 0.0],
        },
        "gauss_x90_Q_wf": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
        },
        "gauss_x180_I_wf": {
            "type": "arbitrary",
            "samples": [0.0, 0.004430093886645415, 0.010031626246347373, 0.016983169507997393, 0.025447121841425106, 0.03555333280909725, 0.047380805975397705, 0.060938851450946276, 0.07614950044287017, 0.09283329821313276, 0.11070068079024514, 0.12935095083700357, 0.1482803686136344, 0.1669000798346295, 0.18456357982253255, 0.2006022777436225, 0.2143666264976031, 0.22526938738112967, 0.23282705464681067] + [0.23669538268420445] * 2 + [0.23282705464681067, 0.22526938738112967, 0.2143666264976031, 0.2006022777436225, 0.18456357982253255, 0.1669000798346295, 0.1482803686136344, 0.12935095083700357, 0.11070068079024514, 0.09283329821313276, 0.07614950044287017, 0.060938851450946276, 0.047380805975397705, 0.03555333280909725, 0.025447121841425106, 0.016983169507997393, 0.010031626246347373, 0.004430093886645415, 0.0],
        },
        "gauss_x180_Q_wf": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
        },
        "gauss_minus_x90_I_wf": {
            "type": "arbitrary",
            "samples": [0.0, -0.0022150469433227073, -0.005015813123173687, -0.008491584753998697, -0.012723560920712553, -0.017776666404548624, -0.023690402987698853, -0.030469425725473138, -0.03807475022143508, -0.04641664910656638, -0.05535034039512257, -0.06467547541850178, -0.0741401843068172, -0.08345003991731476, -0.09228178991126627, -0.10030113887181125, -0.10718331324880155, -0.11263469369056484, -0.11641352732340533] + [-0.11834769134210223] * 2 + [-0.11641352732340533, -0.11263469369056484, -0.10718331324880155, -0.10030113887181125, -0.09228178991126627, -0.08345003991731476, -0.0741401843068172, -0.06467547541850178, -0.05535034039512257, -0.04641664910656638, -0.03807475022143508, -0.030469425725473138, -0.023690402987698853, -0.017776666404548624, -0.012723560920712553, -0.008491584753998697, -0.005015813123173687, -0.0022150469433227073, 0.0],
        },
        "gauss_minus_x90_Q_wf": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
        },
        "gauss_y90_I_wf": {
            "type": "arbitrary",
            "samples": [-0.0] * 40,
        },
        "gauss_y90_Q_wf": {
            "type": "arbitrary",
            "samples": [0.0, 0.0022150469433227073, 0.005015813123173687, 0.008491584753998697, 0.012723560920712553, 0.017776666404548624, 0.023690402987698853, 0.030469425725473138, 0.03807475022143508, 0.04641664910656638, 0.05535034039512257, 0.06467547541850178, 0.0741401843068172, 0.08345003991731476, 0.09228178991126627, 0.10030113887181125, 0.10718331324880155, 0.11263469369056484, 0.11641352732340533] + [0.11834769134210223] * 2 + [0.11641352732340533, 0.11263469369056484, 0.10718331324880155, 0.10030113887181125, 0.09228178991126627, 0.08345003991731476, 0.0741401843068172, 0.06467547541850178, 0.05535034039512257, 0.04641664910656638, 0.03807475022143508, 0.030469425725473138, 0.023690402987698853, 0.017776666404548624, 0.012723560920712553, 0.008491584753998697, 0.005015813123173687, 0.0022150469433227073, 0.0],
        },
        "gauss_y180_I_wf": {
            "type": "arbitrary",
            "samples": [-0.0] * 40,
        },
        "gauss_y180_Q_wf": {
            "type": "arbitrary",
            "samples": [0.0, 0.004430093886645415, 0.010031626246347373, 0.016983169507997393, 0.025447121841425106, 0.03555333280909725, 0.047380805975397705, 0.060938851450946276, 0.07614950044287017, 0.09283329821313276, 0.11070068079024514, 0.12935095083700357, 0.1482803686136344, 0.1669000798346295, 0.18456357982253255, 0.2006022777436225, 0.2143666264976031, 0.22526938738112967, 0.23282705464681067] + [0.23669538268420445] * 2 + [0.23282705464681067, 0.22526938738112967, 0.2143666264976031, 0.2006022777436225, 0.18456357982253255, 0.1669000798346295, 0.1482803686136344, 0.12935095083700357, 0.11070068079024514, 0.09283329821313276, 0.07614950044287017, 0.060938851450946276, 0.047380805975397705, 0.03555333280909725, 0.025447121841425106, 0.016983169507997393, 0.010031626246347373, 0.004430093886645415, 0.0],
        },
        "gauss_minus_y90_I_wf": {
            "type": "arbitrary",
            "samples": [-0.0] * 40,
        },
        "gauss_minus_y90_Q_wf": {
            "type": "arbitrary",
            "samples": [0.0, -0.0022150469433227073, -0.005015813123173687, -0.008491584753998697, -0.012723560920712553, -0.017776666404548624, -0.023690402987698853, -0.030469425725473138, -0.03807475022143508, -0.04641664910656638, -0.05535034039512257, -0.06467547541850178, -0.0741401843068172, -0.08345003991731476, -0.09228178991126627, -0.10030113887181125, -0.10718331324880155, -0.11263469369056484, -0.11641352732340533] + [-0.11834769134210223] * 2 + [-0.11641352732340533, -0.11263469369056484, -0.10718331324880155, -0.10030113887181125, -0.09228178991126627, -0.08345003991731476, -0.0741401843068172, -0.06467547541850178, -0.05535034039512257, -0.04641664910656638, -0.03807475022143508, -0.030469425725473138, -0.023690402987698853, -0.017776666404548624, -0.012723560920712553, -0.008491584753998697, -0.005015813123173687, -0.0022150469433227073, 0.0],
        },
        "gauss_rise_wf": {
            "type": "arbitrary",
            "samples": [0.0, 0.04458909952212427, 0.1120556357711309, 0.20164928899380416, 0.30430946998710384, 0.4023656074084873, 0.4737756589360126, 0.5],
        },
        "gauss_fall_wf": {
            "type": "arbitrary",
            "samples": [0.5, 0.4737756589360126, 0.4023656074084873, 0.30430946998710384, 0.20164928899380416, 0.1120556357711309, 0.04458909952212427, 0.0],
        },
        "arb_I_wf": {
            "type": "arbitrary",
            "samples": [0.5] * 100,
        },
        "arb_Q_wf": {
            "type": "arbitrary",
            "samples": [0.5] * 100,
        },
    },
    "digital_waveforms": {
        "ON": {
            "samples": [(1, 0)],
        },
    },
    "integration_weights": {
        "cosine_weights": {
            "cosine": [(1.0, 200)],
            "sine": [(0.0, 200)],
        },
        "sine_weights": {
            "cosine": [(0.0, 200)],
            "sine": [(1.0, 200)],
        },
        "minus_sine_weights": {
            "cosine": [(0.0, 200)],
            "sine": [(-1.0, 200)],
        },
        "rotated_cosine_weights": {
            "cosine": [0.9689124217106447, 200],
            "sine": [0.24740395925452294, 200],
        },
        "rotated_sine_weights": {
            "cosine": [-0.24740395925452294, 200],
            "sine": [0.9689124217106447, 200],
        },
        "rotated_minus_sine_weights": {
            "cosine": [0.24740395925452294, 200],
            "sine": [-0.9689124217106447, 200],
        },
        "cosine_arb_weights": {
            "cosine": [(1.0, 100)],
            "sine": [(0.0, 100)],
        },
        "sine_arb_weights": {
            "cosine": [(0.0, 100)],
            "sine": [(1.0, 100)],
        },
        "minus_sine_arb_weights": {
            "cosine": [(0.0, 100)],
            "sine": [(-1.0, 100)],
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
                    "type": "MW",
                    "analog_outputs": {
                        "1": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": 1,
                            "band": 1,
                            "delay": 0,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 450000000.0,
                                },
                                "2": {
                                    "frequency": 1900000000.0,
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
                                    "frequency": 450000000.0,
                                },
                                "2": {
                                    "frequency": 1900000000.0,
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
                                    "frequency": 450000000.0,
                                },
                                "2": {
                                    "frequency": 1900000000.0,
                                },
                            },
                        },
                        "4": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": 1,
                            "band": 1,
                            "delay": 0,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 450000000.0,
                                },
                                "2": {
                                    "frequency": 1900000000.0,
                                },
                            },
                        },
                        "5": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": 1,
                            "band": 1,
                            "delay": 0,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 450000000.0,
                                },
                                "2": {
                                    "frequency": 1900000000.0,
                                },
                            },
                        },
                        "6": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": 1,
                            "band": 1,
                            "delay": 0,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 450000000.0,
                                },
                                "2": {
                                    "frequency": 1900000000.0,
                                },
                            },
                        },
                        "7": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": 1,
                            "band": 1,
                            "delay": 0,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 450000000.0,
                                },
                                "2": {
                                    "frequency": 1900000000.0,
                                },
                            },
                        },
                        "8": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": 1,
                            "band": 1,
                            "delay": 0,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 450000000.0,
                                },
                                "2": {
                                    "frequency": 1900000000.0,
                                },
                            },
                        },
                    },
                    "analog_inputs": {
                        "1": {
                            "band": 1,
                            "shareable": False,
                            "gain_db": 1,
                            "sampling_rate": 1000000000.0,
                            "downconverter_frequency": 900000000.0,
                        },
                        "2": {
                            "band": 1,
                            "shareable": False,
                            "gain_db": 1,
                            "sampling_rate": 1000000000.0,
                            "downconverter_frequency": 900000000.0,
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
                        "8": {
                            "shareable": False,
                            "inverted": False,
                            "level": "LVTTL",
                        },
                    },
                },
                "2": {
                    "type": "MW",
                    "analog_outputs": {
                        "1": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": 1,
                            "band": 1,
                            "delay": 0,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 450000000.0,
                                },
                                "2": {
                                    "frequency": 1900000000.0,
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
                                    "frequency": 450000000.0,
                                },
                                "2": {
                                    "frequency": 1900000000.0,
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
                                    "frequency": 450000000.0,
                                },
                                "2": {
                                    "frequency": 1900000000.0,
                                },
                            },
                        },
                        "4": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": 1,
                            "band": 1,
                            "delay": 0,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 450000000.0,
                                },
                                "2": {
                                    "frequency": 1900000000.0,
                                },
                            },
                        },
                        "5": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": 1,
                            "band": 1,
                            "delay": 0,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 450000000.0,
                                },
                                "2": {
                                    "frequency": 1900000000.0,
                                },
                            },
                        },
                        "6": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": 1,
                            "band": 1,
                            "delay": 0,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 450000000.0,
                                },
                                "2": {
                                    "frequency": 1900000000.0,
                                },
                            },
                        },
                        "7": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": 1,
                            "band": 1,
                            "delay": 0,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 450000000.0,
                                },
                                "2": {
                                    "frequency": 1900000000.0,
                                },
                            },
                        },
                        "8": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": 1,
                            "band": 1,
                            "delay": 0,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 450000000.0,
                                },
                                "2": {
                                    "frequency": 1900000000.0,
                                },
                            },
                        },
                    },
                    "analog_inputs": {
                        "1": {
                            "band": 1,
                            "shareable": False,
                            "gain_db": 1,
                            "sampling_rate": 1000000000.0,
                            "downconverter_frequency": 900000000.0,
                        },
                        "2": {
                            "band": 1,
                            "shareable": False,
                            "gain_db": 1,
                            "sampling_rate": 1000000000.0,
                            "downconverter_frequency": 900000000.0,
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
                        "8": {
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
        "qubit_con1-fem1-port1-duc1": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "core": "con1-fem1-port1-duc1",
            "MWInput": {
                "port": ('con1', 1, 1),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000.0,
        },
        "qubit_con1-fem2-port1-duc1": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "core": "con1-fem2-port1-duc1",
            "MWInput": {
                "port": ('con1', 2, 1),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000.0,
        },
        "qubit_con1-fem1-port2-duc1": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "core": "con1-fem1-port2-duc1",
            "MWInput": {
                "port": ('con1', 1, 2),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000.0,
        },
        "qubit_con1-fem2-port2-duc1": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "core": "con1-fem2-port2-duc1",
            "MWInput": {
                "port": ('con1', 2, 2),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000.0,
        },
        "qubit_con1-fem1-port3-duc1": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "core": "con1-fem1-port3-duc1",
            "MWInput": {
                "port": ('con1', 1, 3),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000.0,
        },
        "qubit_con1-fem2-port3-duc1": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "core": "con1-fem2-port3-duc1",
            "MWInput": {
                "port": ('con1', 2, 3),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000.0,
        },
        "qubit_con1-fem1-port4-duc1": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "core": "con1-fem1-port4-duc1",
            "MWInput": {
                "port": ('con1', 1, 4),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000.0,
        },
        "qubit_con1-fem2-port4-duc1": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "core": "con1-fem2-port4-duc1",
            "MWInput": {
                "port": ('con1', 2, 4),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000.0,
        },
        "qubit_con1-fem1-port5-duc1": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "core": "con1-fem1-port5-duc1",
            "MWInput": {
                "port": ('con1', 1, 5),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000.0,
        },
        "qubit_con1-fem2-port5-duc1": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "core": "con1-fem2-port5-duc1",
            "MWInput": {
                "port": ('con1', 2, 5),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000.0,
        },
        "qubit_con1-fem1-port6-duc1": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "core": "con1-fem1-port6-duc1",
            "MWInput": {
                "port": ('con1', 1, 6),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000.0,
        },
        "qubit_con1-fem2-port6-duc1": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "core": "con1-fem2-port6-duc1",
            "MWInput": {
                "port": ('con1', 2, 6),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000.0,
        },
        "qubit_con1-fem1-port7-duc1": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "core": "con1-fem1-port7-duc1",
            "MWInput": {
                "port": ('con1', 1, 7),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000.0,
        },
        "qubit_con1-fem2-port7-duc1": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "core": "con1-fem2-port7-duc1",
            "MWInput": {
                "port": ('con1', 2, 7),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000.0,
        },
        "qubit_con1-fem1-port8-duc1": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "core": "con1-fem1-port8-duc1",
            "MWInput": {
                "port": ('con1', 1, 8),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000.0,
        },
        "qubit_con1-fem2-port8-duc1": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "core": "con1-fem2-port8-duc1",
            "MWInput": {
                "port": ('con1', 2, 8),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000.0,
        },
        "qubit_con1-fem1-port1-duc2": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "core": "con1-fem1-port1-duc1",
            "MWInput": {
                "port": ('con1', 1, 1),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000.0,
        },
        "qubit_con1-fem2-port1-duc2": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "core": "con1-fem2-port1-duc1",
            "MWInput": {
                "port": ('con1', 2, 1),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000.0,
        },
        "qubit_con1-fem1-port2-duc2": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "core": "con1-fem1-port2-duc1",
            "MWInput": {
                "port": ('con1', 1, 2),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000.0,
        },
        "qubit_con1-fem2-port2-duc2": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "core": "con1-fem2-port2-duc1",
            "MWInput": {
                "port": ('con1', 2, 2),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000.0,
        },
        "qubit_con1-fem1-port3-duc2": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "core": "con1-fem1-port3-duc1",
            "MWInput": {
                "port": ('con1', 1, 3),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000.0,
        },
        "qubit_con1-fem2-port3-duc2": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "core": "con1-fem2-port3-duc1",
            "MWInput": {
                "port": ('con1', 2, 3),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000.0,
        },
        "qubit_con1-fem1-port4-duc2": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "core": "con1-fem1-port4-duc1",
            "MWInput": {
                "port": ('con1', 1, 4),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000.0,
        },
        "qubit_con1-fem2-port4-duc2": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "core": "con1-fem2-port4-duc1",
            "MWInput": {
                "port": ('con1', 2, 4),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000.0,
        },
        "qubit_con1-fem1-port5-duc2": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "core": "con1-fem1-port5-duc1",
            "MWInput": {
                "port": ('con1', 1, 5),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000.0,
        },
        "qubit_con1-fem2-port5-duc2": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "core": "con1-fem2-port5-duc1",
            "MWInput": {
                "port": ('con1', 2, 5),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000.0,
        },
        "qubit_con1-fem1-port6-duc2": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "core": "con1-fem1-port6-duc1",
            "MWInput": {
                "port": ('con1', 1, 6),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000.0,
        },
        "qubit_con1-fem2-port6-duc2": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "core": "con1-fem2-port6-duc1",
            "MWInput": {
                "port": ('con1', 2, 6),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000.0,
        },
        "qubit_con1-fem1-port7-duc2": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "core": "con1-fem1-port7-duc1",
            "MWInput": {
                "port": ('con1', 1, 7),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000.0,
        },
        "qubit_con1-fem2-port7-duc2": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "core": "con1-fem2-port7-duc1",
            "MWInput": {
                "port": ('con1', 2, 7),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000.0,
        },
        "qubit_con1-fem1-port8-duc2": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "core": "con1-fem1-port8-duc1",
            "MWInput": {
                "port": ('con1', 1, 8),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000.0,
        },
        "qubit_con1-fem2-port8-duc2": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "core": "con1-fem2-port8-duc1",
            "MWInput": {
                "port": ('con1', 2, 8),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000.0,
        },
        "qubit_con1-fem1-port1-duc1-twin": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "core": "con1-fem1-port1-duc1",
            "MWInput": {
                "port": ('con1', 1, 1),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000.0,
        },
        "qubit_con1-fem2-port1-duc1-twin": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "core": "con1-fem2-port1-duc1",
            "MWInput": {
                "port": ('con1', 2, 1),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000.0,
        },
        "qubit_con1-fem1-port2-duc1-twin": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "core": "con1-fem1-port2-duc1",
            "MWInput": {
                "port": ('con1', 1, 2),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000.0,
        },
        "qubit_con1-fem2-port2-duc1-twin": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "core": "con1-fem2-port2-duc1",
            "MWInput": {
                "port": ('con1', 2, 2),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000.0,
        },
        "qubit_con1-fem1-port3-duc1-twin": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "core": "con1-fem1-port3-duc1",
            "MWInput": {
                "port": ('con1', 1, 3),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000.0,
        },
        "qubit_con1-fem2-port3-duc1-twin": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "core": "con1-fem2-port3-duc1",
            "MWInput": {
                "port": ('con1', 2, 3),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000.0,
        },
        "qubit_con1-fem1-port4-duc1-twin": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "core": "con1-fem1-port4-duc1",
            "MWInput": {
                "port": ('con1', 1, 4),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000.0,
        },
        "qubit_con1-fem2-port4-duc1-twin": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "core": "con1-fem2-port4-duc1",
            "MWInput": {
                "port": ('con1', 2, 4),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000.0,
        },
        "qubit_con1-fem1-port5-duc1-twin": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "core": "con1-fem1-port5-duc1",
            "MWInput": {
                "port": ('con1', 1, 5),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000.0,
        },
        "qubit_con1-fem2-port5-duc1-twin": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "core": "con1-fem2-port5-duc1",
            "MWInput": {
                "port": ('con1', 2, 5),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000.0,
        },
        "qubit_con1-fem1-port6-duc1-twin": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "core": "con1-fem1-port6-duc1",
            "MWInput": {
                "port": ('con1', 1, 6),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000.0,
        },
        "qubit_con1-fem2-port6-duc1-twin": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "core": "con1-fem2-port6-duc1",
            "MWInput": {
                "port": ('con1', 2, 6),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000.0,
        },
        "qubit_con1-fem1-port7-duc1-twin": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "core": "con1-fem1-port7-duc1",
            "MWInput": {
                "port": ('con1', 1, 7),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000.0,
        },
        "qubit_con1-fem2-port7-duc1-twin": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "core": "con1-fem2-port7-duc1",
            "MWInput": {
                "port": ('con1', 2, 7),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000.0,
        },
        "qubit_con1-fem1-port8-duc1-twin": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "core": "con1-fem1-port8-duc1",
            "MWInput": {
                "port": ('con1', 1, 8),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000.0,
        },
        "qubit_con1-fem2-port8-duc1-twin": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "core": "con1-fem2-port8-duc1",
            "MWInput": {
                "port": ('con1', 2, 8),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000.0,
        },
        "qubit_con1-fem1-port1-duc2-twin": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "core": "con1-fem1-port1-duc1",
            "MWInput": {
                "port": ('con1', 1, 1),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000.0,
        },
        "qubit_con1-fem2-port1-duc2-twin": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "core": "con1-fem2-port1-duc1",
            "MWInput": {
                "port": ('con1', 2, 1),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000.0,
        },
        "qubit_con1-fem1-port2-duc2-twin": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "core": "con1-fem1-port2-duc1",
            "MWInput": {
                "port": ('con1', 1, 2),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000.0,
        },
        "qubit_con1-fem2-port2-duc2-twin": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "core": "con1-fem2-port2-duc1",
            "MWInput": {
                "port": ('con1', 2, 2),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000.0,
        },
        "qubit_con1-fem1-port3-duc2-twin": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "core": "con1-fem1-port3-duc1",
            "MWInput": {
                "port": ('con1', 1, 3),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000.0,
        },
        "qubit_con1-fem2-port3-duc2-twin": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "core": "con1-fem2-port3-duc1",
            "MWInput": {
                "port": ('con1', 2, 3),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000.0,
        },
        "qubit_con1-fem1-port4-duc2-twin": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "core": "con1-fem1-port4-duc1",
            "MWInput": {
                "port": ('con1', 1, 4),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000.0,
        },
        "qubit_con1-fem2-port4-duc2-twin": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "core": "con1-fem2-port4-duc1",
            "MWInput": {
                "port": ('con1', 2, 4),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000.0,
        },
        "qubit_con1-fem1-port5-duc2-twin": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "core": "con1-fem1-port5-duc1",
            "MWInput": {
                "port": ('con1', 1, 5),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000.0,
        },
        "qubit_con1-fem2-port5-duc2-twin": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "core": "con1-fem2-port5-duc1",
            "MWInput": {
                "port": ('con1', 2, 5),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000.0,
        },
        "qubit_con1-fem1-port6-duc2-twin": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "core": "con1-fem1-port6-duc1",
            "MWInput": {
                "port": ('con1', 1, 6),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000.0,
        },
        "qubit_con1-fem2-port6-duc2-twin": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "core": "con1-fem2-port6-duc1",
            "MWInput": {
                "port": ('con1', 2, 6),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000.0,
        },
        "qubit_con1-fem1-port7-duc2-twin": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "core": "con1-fem1-port7-duc1",
            "MWInput": {
                "port": ('con1', 1, 7),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000.0,
        },
        "qubit_con1-fem2-port7-duc2-twin": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "core": "con1-fem2-port7-duc1",
            "MWInput": {
                "port": ('con1', 2, 7),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000.0,
        },
        "qubit_con1-fem1-port8-duc2-twin": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "core": "con1-fem1-port8-duc1",
            "MWInput": {
                "port": ('con1', 1, 8),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000.0,
        },
        "qubit_con1-fem2-port8-duc2-twin": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "x180": "gauss_x180_pulse",
                "x90": "gauss_x90_pulse",
                "-x90": "gauss_minus_x90_pulse",
                "y90": "gauss_y90_pulse",
                "y180": "gauss_y180_pulse",
                "-y90": "gauss_minus_y90_pulse",
                "gauss_rise": "gauss_rise_pulse",
                "gauss_fall": "gauss_fall_pulse",
                "arb": "arb_pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "core": "con1-fem2-port8-duc1",
            "MWInput": {
                "port": ('con1', 2, 8),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000.0,
        },
        "resonator_con1-fem1-port1-duc1": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "readout": "readout_pulse",
                "arb": "arb_pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "core": "con1-fem1-port1-duc1",
            "MWInput": {
                "port": ('con1', 1, 1),
                "upconverter": 1,
            },
            "MWOutput": {
                "port": ('con1', 1, 1),
            },
            "smearing": 0,
            "time_of_flight": 300,
            "intermediate_frequency": 50000000.0,
        },
        "resonator_con1-fem2-port1-duc1": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "readout": "readout_pulse",
                "arb": "arb_pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "core": "con1-fem2-port1-duc1",
            "MWInput": {
                "port": ('con1', 2, 1),
                "upconverter": 1,
            },
            "MWOutput": {
                "port": ('con1', 2, 1),
            },
            "smearing": 0,
            "time_of_flight": 300,
            "intermediate_frequency": 50000000.0,
        },
        "resonator_con1-fem1-port2-duc1": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "readout": "readout_pulse",
                "arb": "arb_pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "core": "con1-fem1-port2-duc1",
            "MWInput": {
                "port": ('con1', 1, 2),
                "upconverter": 1,
            },
            "MWOutput": {
                "port": ('con1', 1, 1),
            },
            "smearing": 0,
            "time_of_flight": 300,
            "intermediate_frequency": 50000000.0,
        },
        "resonator_con1-fem2-port2-duc1": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "readout": "readout_pulse",
                "arb": "arb_pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "core": "con1-fem2-port2-duc1",
            "MWInput": {
                "port": ('con1', 2, 2),
                "upconverter": 1,
            },
            "MWOutput": {
                "port": ('con1', 2, 1),
            },
            "smearing": 0,
            "time_of_flight": 300,
            "intermediate_frequency": 50000000.0,
        },
        "resonator_con1-fem1-port3-duc1": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "readout": "readout_pulse",
                "arb": "arb_pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "core": "con1-fem1-port3-duc1",
            "MWInput": {
                "port": ('con1', 1, 3),
                "upconverter": 1,
            },
            "MWOutput": {
                "port": ('con1', 1, 1),
            },
            "smearing": 0,
            "time_of_flight": 300,
            "intermediate_frequency": 50000000.0,
        },
        "resonator_con1-fem2-port3-duc1": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "readout": "readout_pulse",
                "arb": "arb_pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "core": "con1-fem2-port3-duc1",
            "MWInput": {
                "port": ('con1', 2, 3),
                "upconverter": 1,
            },
            "MWOutput": {
                "port": ('con1', 2, 1),
            },
            "smearing": 0,
            "time_of_flight": 300,
            "intermediate_frequency": 50000000.0,
        },
        "resonator_con1-fem1-port4-duc1": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "readout": "readout_pulse",
                "arb": "arb_pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "core": "con1-fem1-port4-duc1",
            "MWInput": {
                "port": ('con1', 1, 4),
                "upconverter": 1,
            },
            "MWOutput": {
                "port": ('con1', 1, 1),
            },
            "smearing": 0,
            "time_of_flight": 300,
            "intermediate_frequency": 50000000.0,
        },
        "resonator_con1-fem2-port4-duc1": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "readout": "readout_pulse",
                "arb": "arb_pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "core": "con1-fem2-port4-duc1",
            "MWInput": {
                "port": ('con1', 2, 4),
                "upconverter": 1,
            },
            "MWOutput": {
                "port": ('con1', 2, 1),
            },
            "smearing": 0,
            "time_of_flight": 300,
            "intermediate_frequency": 50000000.0,
        },
        "resonator_con1-fem1-port5-duc1": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "readout": "readout_pulse",
                "arb": "arb_pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "core": "con1-fem1-port5-duc1",
            "MWInput": {
                "port": ('con1', 1, 5),
                "upconverter": 1,
            },
            "MWOutput": {
                "port": ('con1', 1, 2),
            },
            "smearing": 0,
            "time_of_flight": 300,
            "intermediate_frequency": 50000000.0,
        },
        "resonator_con1-fem2-port5-duc1": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "readout": "readout_pulse",
                "arb": "arb_pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "core": "con1-fem2-port5-duc1",
            "MWInput": {
                "port": ('con1', 2, 5),
                "upconverter": 1,
            },
            "MWOutput": {
                "port": ('con1', 2, 2),
            },
            "smearing": 0,
            "time_of_flight": 300,
            "intermediate_frequency": 50000000.0,
        },
        "resonator_con1-fem1-port6-duc1": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "readout": "readout_pulse",
                "arb": "arb_pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "core": "con1-fem1-port6-duc1",
            "MWInput": {
                "port": ('con1', 1, 6),
                "upconverter": 1,
            },
            "MWOutput": {
                "port": ('con1', 1, 2),
            },
            "smearing": 0,
            "time_of_flight": 300,
            "intermediate_frequency": 50000000.0,
        },
        "resonator_con1-fem2-port6-duc1": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "readout": "readout_pulse",
                "arb": "arb_pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "core": "con1-fem2-port6-duc1",
            "MWInput": {
                "port": ('con1', 2, 6),
                "upconverter": 1,
            },
            "MWOutput": {
                "port": ('con1', 2, 2),
            },
            "smearing": 0,
            "time_of_flight": 300,
            "intermediate_frequency": 50000000.0,
        },
        "resonator_con1-fem1-port7-duc1": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "readout": "readout_pulse",
                "arb": "arb_pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "core": "con1-fem1-port7-duc1",
            "MWInput": {
                "port": ('con1', 1, 7),
                "upconverter": 1,
            },
            "MWOutput": {
                "port": ('con1', 1, 2),
            },
            "smearing": 0,
            "time_of_flight": 300,
            "intermediate_frequency": 50000000.0,
        },
        "resonator_con1-fem2-port7-duc1": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "readout": "readout_pulse",
                "arb": "arb_pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "core": "con1-fem2-port7-duc1",
            "MWInput": {
                "port": ('con1', 2, 7),
                "upconverter": 1,
            },
            "MWOutput": {
                "port": ('con1', 2, 2),
            },
            "smearing": 0,
            "time_of_flight": 300,
            "intermediate_frequency": 50000000.0,
        },
        "resonator_con1-fem1-port8-duc1": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "readout": "readout_pulse",
                "arb": "arb_pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "core": "con1-fem1-port8-duc1",
            "MWInput": {
                "port": ('con1', 1, 8),
                "upconverter": 1,
            },
            "MWOutput": {
                "port": ('con1', 1, 2),
            },
            "smearing": 0,
            "time_of_flight": 300,
            "intermediate_frequency": 50000000.0,
        },
        "resonator_con1-fem2-port8-duc1": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
                "readout": "readout_pulse",
                "arb": "arb_pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "core": "con1-fem2-port8-duc1",
            "MWInput": {
                "port": ('con1', 2, 8),
                "upconverter": 1,
            },
            "MWOutput": {
                "port": ('con1', 2, 2),
            },
            "smearing": 0,
            "time_of_flight": 300,
            "intermediate_frequency": 50000000.0,
        },
        "jpa_con1-fem1-port1": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
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
            "intermediate_frequency": 50000000.0,
        },
        "jpa_con1-fem2-port1": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
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
            "intermediate_frequency": 50000000.0,
        },
        "jpa_con1-fem1-port2": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
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
                "port": ('con1', 1, 2),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000.0,
        },
        "jpa_con1-fem2-port2": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
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
            "intermediate_frequency": 50000000.0,
        },
        "jpa_con1-fem1-port3": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
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
                "port": ('con1', 1, 3),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000.0,
        },
        "jpa_con1-fem2-port3": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
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
            "intermediate_frequency": 50000000.0,
        },
        "jpa_con1-fem1-port4": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
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
                "port": ('con1', 1, 4),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000.0,
        },
        "jpa_con1-fem2-port4": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
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
            "intermediate_frequency": 50000000.0,
        },
        "jpa_con1-fem1-port5": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
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
                "port": ('con1', 1, 5),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000.0,
        },
        "jpa_con1-fem2-port5": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
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
            "intermediate_frequency": 50000000.0,
        },
        "jpa_con1-fem1-port6": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
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
                "port": ('con1', 1, 6),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000.0,
        },
        "jpa_con1-fem2-port6": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
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
            "intermediate_frequency": 50000000.0,
        },
        "jpa_con1-fem1-port7": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
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
                "port": ('con1', 1, 7),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000.0,
        },
        "jpa_con1-fem2-port7": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
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
            "intermediate_frequency": 50000000.0,
        },
        "jpa_con1-fem1-port8": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
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
                "port": ('con1', 1, 8),
                "upconverter": 1,
            },
            "intermediate_frequency": 50000000.0,
        },
        "jpa_con1-fem2-port8": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "const": "const_pulse",
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
            "intermediate_frequency": 50000000.0,
        },
        "trigger_con1-fem1-port1": {
            "digitalInputs": {
                "marker": {
                    "delay": 0,
                    "buffer": 0,
                    "port": ('con1', 1, 1),
                },
            },
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "on": "trigger_pulse",
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
        "trigger_con1-fem2-port1": {
            "digitalInputs": {
                "marker": {
                    "delay": 0,
                    "buffer": 0,
                    "port": ('con1', 2, 1),
                },
            },
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "on": "trigger_pulse",
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
        "trigger_con1-fem1-port2": {
            "digitalInputs": {
                "marker": {
                    "delay": 0,
                    "buffer": 0,
                    "port": ('con1', 1, 2),
                },
            },
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "on": "trigger_pulse",
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
        "trigger_con1-fem2-port2": {
            "digitalInputs": {
                "marker": {
                    "delay": 0,
                    "buffer": 0,
                    "port": ('con1', 2, 2),
                },
            },
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "on": "trigger_pulse",
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
        "trigger_con1-fem1-port3": {
            "digitalInputs": {
                "marker": {
                    "delay": 0,
                    "buffer": 0,
                    "port": ('con1', 1, 3),
                },
            },
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "on": "trigger_pulse",
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
        "trigger_con1-fem2-port3": {
            "digitalInputs": {
                "marker": {
                    "delay": 0,
                    "buffer": 0,
                    "port": ('con1', 2, 3),
                },
            },
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "on": "trigger_pulse",
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
        "trigger_con1-fem1-port4": {
            "digitalInputs": {
                "marker": {
                    "delay": 0,
                    "buffer": 0,
                    "port": ('con1', 1, 4),
                },
            },
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "on": "trigger_pulse",
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
        "trigger_con1-fem2-port4": {
            "digitalInputs": {
                "marker": {
                    "delay": 0,
                    "buffer": 0,
                    "port": ('con1', 2, 4),
                },
            },
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "on": "trigger_pulse",
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
        "trigger_con1-fem1-port5": {
            "digitalInputs": {
                "marker": {
                    "delay": 0,
                    "buffer": 0,
                    "port": ('con1', 1, 5),
                },
            },
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "on": "trigger_pulse",
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
        "trigger_con1-fem2-port5": {
            "digitalInputs": {
                "marker": {
                    "delay": 0,
                    "buffer": 0,
                    "port": ('con1', 2, 5),
                },
            },
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "on": "trigger_pulse",
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
        "trigger_con1-fem1-port6": {
            "digitalInputs": {
                "marker": {
                    "delay": 0,
                    "buffer": 0,
                    "port": ('con1', 1, 6),
                },
            },
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "on": "trigger_pulse",
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
        "trigger_con1-fem2-port6": {
            "digitalInputs": {
                "marker": {
                    "delay": 0,
                    "buffer": 0,
                    "port": ('con1', 2, 6),
                },
            },
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "on": "trigger_pulse",
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
        "trigger_con1-fem1-port7": {
            "digitalInputs": {
                "marker": {
                    "delay": 0,
                    "buffer": 0,
                    "port": ('con1', 1, 7),
                },
            },
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "on": "trigger_pulse",
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
        "trigger_con1-fem2-port7": {
            "digitalInputs": {
                "marker": {
                    "delay": 0,
                    "buffer": 0,
                    "port": ('con1', 2, 7),
                },
            },
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "on": "trigger_pulse",
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
        "trigger_con1-fem1-port8": {
            "digitalInputs": {
                "marker": {
                    "delay": 0,
                    "buffer": 0,
                    "port": ('con1', 1, 8),
                },
            },
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "on": "trigger_pulse",
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
        "trigger_con1-fem2-port8": {
            "digitalInputs": {
                "marker": {
                    "delay": 0,
                    "buffer": 0,
                    "port": ('con1', 2, 8),
                },
            },
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "on": "trigger_pulse",
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
        "const_pulse": {
            "length": 100,
            "waveforms": {
                "I": "const_wf",
                "Q": "zero_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "gauss_x180_pulse": {
            "length": 40,
            "waveforms": {
                "I": "gauss_x180_I_wf",
                "Q": "gauss_x180_Q_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "gauss_y180_pulse": {
            "length": 40,
            "waveforms": {
                "I": "gauss_y180_I_wf",
                "Q": "gauss_y180_Q_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "gauss_x90_pulse": {
            "length": 40,
            "waveforms": {
                "I": "gauss_x90_I_wf",
                "Q": "gauss_x90_Q_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "gauss_minus_x90_pulse": {
            "length": 40,
            "waveforms": {
                "I": "gauss_minus_x90_I_wf",
                "Q": "gauss_minus_x90_Q_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "gauss_y90_pulse": {
            "length": 40,
            "waveforms": {
                "I": "gauss_y90_I_wf",
                "Q": "gauss_y90_Q_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "gauss_minus_y90_pulse": {
            "length": 40,
            "waveforms": {
                "I": "gauss_minus_y90_I_wf",
                "Q": "gauss_minus_y90_Q_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "gauss_rise_pulse": {
            "length": 8,
            "waveforms": {
                "I": "gauss_rise_wf",
                "Q": "zero_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "gauss_fall_pulse": {
            "length": 8,
            "waveforms": {
                "I": "gauss_fall_wf",
                "Q": "zero_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "arb_pulse": {
            "length": 100,
            "waveforms": {
                "I": "arb_I_wf",
                "Q": "arb_Q_wf",
            },
            "integration_weights": {
                "cos": "cosine_arb_weights",
                "sin": "sine_arb_weights",
                "minus_sin": "minus_sine_arb_weights",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "readout_pulse": {
            "length": 200,
            "waveforms": {
                "I": "readout_wf",
                "Q": "zero_wf",
            },
            "integration_weights": {
                "cos": "cosine_weights",
                "sin": "sine_weights",
                "minus_sin": "minus_sine_weights",
                "rotated_cos": "rotated_cosine_weights",
                "rotated_sin": "rotated_sine_weights",
                "rotated_minus_sin": "rotated_minus_sine_weights",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "trigger_pulse": {
            "length": 1000,
            "waveforms": {},
            "integration_weights": {},
            "operation": "control",
            "digital_marker": "ON",
        },
    },
    "waveforms": {
        "const_wf": {
            "type": "constant",
            "sample": 0.5,
        },
        "zero_wf": {
            "type": "constant",
            "sample": 0.0,
        },
        "readout_wf": {
            "type": "constant",
            "sample": 0.5,
        },
        "gauss_x90_I_wf": {
            "type": "arbitrary",
            "samples": [0.0, 0.0022150469433227073, 0.005015813123173687, 0.008491584753998697, 0.012723560920712553, 0.017776666404548624, 0.023690402987698853, 0.030469425725473138, 0.03807475022143508, 0.04641664910656638, 0.05535034039512257, 0.06467547541850178, 0.0741401843068172, 0.08345003991731476, 0.09228178991126627, 0.10030113887181125, 0.10718331324880155, 0.11263469369056484, 0.11641352732340533] + [0.11834769134210223] * 2 + [0.11641352732340533, 0.11263469369056484, 0.10718331324880155, 0.10030113887181125, 0.09228178991126627, 0.08345003991731476, 0.0741401843068172, 0.06467547541850178, 0.05535034039512257, 0.04641664910656638, 0.03807475022143508, 0.030469425725473138, 0.023690402987698853, 0.017776666404548624, 0.012723560920712553, 0.008491584753998697, 0.005015813123173687, 0.0022150469433227073, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "gauss_x90_Q_wf": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "gauss_x180_I_wf": {
            "type": "arbitrary",
            "samples": [0.0, 0.004430093886645415, 0.010031626246347373, 0.016983169507997393, 0.025447121841425106, 0.03555333280909725, 0.047380805975397705, 0.060938851450946276, 0.07614950044287017, 0.09283329821313276, 0.11070068079024514, 0.12935095083700357, 0.1482803686136344, 0.1669000798346295, 0.18456357982253255, 0.2006022777436225, 0.2143666264976031, 0.22526938738112967, 0.23282705464681067] + [0.23669538268420445] * 2 + [0.23282705464681067, 0.22526938738112967, 0.2143666264976031, 0.2006022777436225, 0.18456357982253255, 0.1669000798346295, 0.1482803686136344, 0.12935095083700357, 0.11070068079024514, 0.09283329821313276, 0.07614950044287017, 0.060938851450946276, 0.047380805975397705, 0.03555333280909725, 0.025447121841425106, 0.016983169507997393, 0.010031626246347373, 0.004430093886645415, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "gauss_x180_Q_wf": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "gauss_minus_x90_I_wf": {
            "type": "arbitrary",
            "samples": [0.0, -0.0022150469433227073, -0.005015813123173687, -0.008491584753998697, -0.012723560920712553, -0.017776666404548624, -0.023690402987698853, -0.030469425725473138, -0.03807475022143508, -0.04641664910656638, -0.05535034039512257, -0.06467547541850178, -0.0741401843068172, -0.08345003991731476, -0.09228178991126627, -0.10030113887181125, -0.10718331324880155, -0.11263469369056484, -0.11641352732340533] + [-0.11834769134210223] * 2 + [-0.11641352732340533, -0.11263469369056484, -0.10718331324880155, -0.10030113887181125, -0.09228178991126627, -0.08345003991731476, -0.0741401843068172, -0.06467547541850178, -0.05535034039512257, -0.04641664910656638, -0.03807475022143508, -0.030469425725473138, -0.023690402987698853, -0.017776666404548624, -0.012723560920712553, -0.008491584753998697, -0.005015813123173687, -0.0022150469433227073, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "gauss_minus_x90_Q_wf": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "gauss_y90_I_wf": {
            "type": "arbitrary",
            "samples": [-0.0] * 40,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "gauss_y90_Q_wf": {
            "type": "arbitrary",
            "samples": [0.0, 0.0022150469433227073, 0.005015813123173687, 0.008491584753998697, 0.012723560920712553, 0.017776666404548624, 0.023690402987698853, 0.030469425725473138, 0.03807475022143508, 0.04641664910656638, 0.05535034039512257, 0.06467547541850178, 0.0741401843068172, 0.08345003991731476, 0.09228178991126627, 0.10030113887181125, 0.10718331324880155, 0.11263469369056484, 0.11641352732340533] + [0.11834769134210223] * 2 + [0.11641352732340533, 0.11263469369056484, 0.10718331324880155, 0.10030113887181125, 0.09228178991126627, 0.08345003991731476, 0.0741401843068172, 0.06467547541850178, 0.05535034039512257, 0.04641664910656638, 0.03807475022143508, 0.030469425725473138, 0.023690402987698853, 0.017776666404548624, 0.012723560920712553, 0.008491584753998697, 0.005015813123173687, 0.0022150469433227073, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "gauss_y180_I_wf": {
            "type": "arbitrary",
            "samples": [-0.0] * 40,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "gauss_y180_Q_wf": {
            "type": "arbitrary",
            "samples": [0.0, 0.004430093886645415, 0.010031626246347373, 0.016983169507997393, 0.025447121841425106, 0.03555333280909725, 0.047380805975397705, 0.060938851450946276, 0.07614950044287017, 0.09283329821313276, 0.11070068079024514, 0.12935095083700357, 0.1482803686136344, 0.1669000798346295, 0.18456357982253255, 0.2006022777436225, 0.2143666264976031, 0.22526938738112967, 0.23282705464681067] + [0.23669538268420445] * 2 + [0.23282705464681067, 0.22526938738112967, 0.2143666264976031, 0.2006022777436225, 0.18456357982253255, 0.1669000798346295, 0.1482803686136344, 0.12935095083700357, 0.11070068079024514, 0.09283329821313276, 0.07614950044287017, 0.060938851450946276, 0.047380805975397705, 0.03555333280909725, 0.025447121841425106, 0.016983169507997393, 0.010031626246347373, 0.004430093886645415, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "gauss_minus_y90_I_wf": {
            "type": "arbitrary",
            "samples": [-0.0] * 40,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "gauss_minus_y90_Q_wf": {
            "type": "arbitrary",
            "samples": [0.0, -0.0022150469433227073, -0.005015813123173687, -0.008491584753998697, -0.012723560920712553, -0.017776666404548624, -0.023690402987698853, -0.030469425725473138, -0.03807475022143508, -0.04641664910656638, -0.05535034039512257, -0.06467547541850178, -0.0741401843068172, -0.08345003991731476, -0.09228178991126627, -0.10030113887181125, -0.10718331324880155, -0.11263469369056484, -0.11641352732340533] + [-0.11834769134210223] * 2 + [-0.11641352732340533, -0.11263469369056484, -0.10718331324880155, -0.10030113887181125, -0.09228178991126627, -0.08345003991731476, -0.0741401843068172, -0.06467547541850178, -0.05535034039512257, -0.04641664910656638, -0.03807475022143508, -0.030469425725473138, -0.023690402987698853, -0.017776666404548624, -0.012723560920712553, -0.008491584753998697, -0.005015813123173687, -0.0022150469433227073, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "gauss_rise_wf": {
            "type": "arbitrary",
            "samples": [0.0, 0.04458909952212427, 0.1120556357711309, 0.20164928899380416, 0.30430946998710384, 0.4023656074084873, 0.4737756589360126, 0.5],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "gauss_fall_wf": {
            "type": "arbitrary",
            "samples": [0.5, 0.4737756589360126, 0.4023656074084873, 0.30430946998710384, 0.20164928899380416, 0.1120556357711309, 0.04458909952212427, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "arb_I_wf": {
            "type": "arbitrary",
            "samples": [0.5] * 100,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "arb_Q_wf": {
            "type": "arbitrary",
            "samples": [0.5] * 100,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
    },
    "digital_waveforms": {
        "ON": {
            "samples": [(1, 0)],
        },
    },
    "integration_weights": {
        "cosine_weights": {
            "cosine": [(1.0, 200)],
            "sine": [(0.0, 200)],
        },
        "sine_weights": {
            "cosine": [(0.0, 200)],
            "sine": [(1.0, 200)],
        },
        "minus_sine_weights": {
            "cosine": [(0.0, 200)],
            "sine": [(-1.0, 200)],
        },
        "rotated_cosine_weights": {
            "cosine": [(0.9689124217106447, 200)],
            "sine": [(0.24740395925452294, 200)],
        },
        "rotated_sine_weights": {
            "cosine": [(-0.24740395925452294, 200)],
            "sine": [(0.9689124217106447, 200)],
        },
        "rotated_minus_sine_weights": {
            "cosine": [(0.24740395925452294, 200)],
            "sine": [(-0.9689124217106447, 200)],
        },
        "cosine_arb_weights": {
            "cosine": [(1.0, 100)],
            "sine": [(0.0, 100)],
        },
        "sine_arb_weights": {
            "cosine": [(0.0, 100)],
            "sine": [(1.0, 100)],
        },
        "minus_sine_arb_weights": {
            "cosine": [(0.0, 100)],
            "sine": [(-1.0, 100)],
        },
    },
    "mixers": {},
}


