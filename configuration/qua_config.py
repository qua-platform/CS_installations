sorted_config = {
    "controllers": {
        "con1": {
            "fems": {
                "1": {
                    "analog_inputs": {
                        "1": {
                            "gain_db": 0,
                            "offset": 0.0,
                            "sampling_rate": 1000000000.0,
                            "shareable": False
                        },
                        "2": {
                            "gain_db": 0,
                            "offset": 0.0,
                            "sampling_rate": 1000000000.0,
                            "shareable": False
                        }
                    },
                    "analog_outputs": {
                        "1": {
                            "delay": 0,
                            "offset": 0.0,
                            "output_mode": "direct",
                            "sampling_rate": 1000000000.0,
                            "shareable": False,
                            "upsampling_mode": "mw"
                        },
                        "2": {
                            "delay": 0,
                            "offset": 0.0,
                            "output_mode": "direct",
                            "sampling_rate": 1000000000.0,
                            "shareable": False,
                            "upsampling_mode": "mw"
                        },
                        "3": {
                            "delay": 0,
                            "offset": 0.0,
                            "output_mode": "direct",
                            "sampling_rate": 1000000000.0,
                            "shareable": False,
                            "upsampling_mode": "pulse"
                        },
                        "4": {
                            "delay": 0,
                            "offset": 0.0,
                            "output_mode": "direct",
                            "sampling_rate": 1000000000.0,
                            "shareable": False,
                            "upsampling_mode": "pulse"
                        },
                        "5": {
                            "delay": 0,
                            "offset": 0.0,
                            "output_mode": "direct",
                            "sampling_rate": 1000000000.0,
                            "shareable": False,
                            "upsampling_mode": "pulse"
                        },
                        "6": {
                            "delay": 0,
                            "offset": 0.0,
                            "output_mode": "direct",
                            "sampling_rate": 1000000000.0,
                            "shareable": False,
                            "upsampling_mode": "pulse"
                        },
                        "7": {
                            "delay": 0,
                            "offset": 0.0,
                            "output_mode": "direct",
                            "sampling_rate": 1000000000.0,
                            "shareable": False,
                            "upsampling_mode": "pulse"
                        },
                        "8": {
                            "delay": 0,
                            "offset": 0.0,
                            "output_mode": "direct",
                            "sampling_rate": 1000000000.0,
                            "shareable": False,
                            "upsampling_mode": "pulse"
                        },
                        "9": {
                            "delay": 0,
                            "offset": 0.0,
                            "output_mode": "direct",
                            "sampling_rate": 1000000000.0,
                            "shareable": False,
                            "upsampling_mode": "pulse"
                        },
                        "10": {
                            "delay": 0,
                            "offset": 0.0,
                            "output_mode": "direct",
                            "sampling_rate": 1000000000.0,
                            "shareable": False,
                            "upsampling_mode": "pulse"
                        }
                    },
                    "digital_outputs": {
                        "1": {
                            "inverted": False,
                            "level": "LVTTL",
                            "shareable": False
                        },
                        "3": {
                            "inverted": False,
                            "level": "LVTTL",
                            "shareable": False
                        },
                        "5": {
                            "inverted": False,
                            "level": "LVTTL",
                            "shareable": False
                        },
                        "7": {
                            "inverted": False,
                            "level": "LVTTL",
                            "shareable": False
                        },
                        "9": {
                            "inverted": False,
                            "level": "LVTTL",
                            "shareable": False
                        }
                    },
                    "type": "LF"
                }
            }
        }
    },
    "digital_waveforms": {
        "ON": {
            "samples": [
                [
                    1,
                    0
                ]
            ]
        }
    },
    "elements": {
        "cr_control_Cq1_Tq2": {
            "RF_inputs": {
                "port": [
                    "octave1",
                    2
                ]
            },
            "intermediate_frequency": -200000000,
            "operations": {
                "square": "cr_control_Cq1_Tq2.square.pulse"
            }
        },
        "cr_control_Cq2_Tq1": {
            "RF_inputs": {
                "port": [
                    "octave1",
                    3
                ]
            },
            "intermediate_frequency": -200000000,
            "operations": {
                "square": "cr_control_Cq2_Tq1.square.pulse"
            }
        },
        "cr_control_Cq2_Tq3": {
            "RF_inputs": {
                "port": [
                    "octave1",
                    3
                ]
            },
            "intermediate_frequency": -200000000,
            "operations": {
                "square": "cr_control_Cq2_Tq3.square.pulse"
            }
        },
        "cr_control_Cq3_Tq2": {
            "RF_inputs": {
                "port": [
                    "octave1",
                    4
                ]
            },
            "intermediate_frequency": -200000000,
            "operations": {
                "square": "cr_control_Cq3_Tq2.square.pulse"
            }
        },
        "cr_control_Cq3_Tq4": {
            "RF_inputs": {
                "port": [
                    "octave1",
                    4
                ]
            },
            "intermediate_frequency": -200000000,
            "operations": {
                "square": "cr_control_Cq3_Tq4.square.pulse"
            }
        },
        "cr_control_Cq4_Tq3": {
            "RF_inputs": {
                "port": [
                    "octave1",
                    5
                ]
            },
            "intermediate_frequency": -200000000,
            "operations": {
                "square": "cr_control_Cq4_Tq3.square.pulse"
            }
        },
        "cr_target_Cq1_Tq2": {
            "RF_inputs": {
                "port": [
                    "octave1",
                    3
                ]
            },
            "intermediate_frequency": -200000000,
            "operations": {
                "square": "cr_target_Cq1_Tq2.square.pulse"
            }
        },
        "cr_target_Cq2_Tq1": {
            "RF_inputs": {
                "port": [
                    "octave1",
                    2
                ]
            },
            "intermediate_frequency": -200000000,
            "operations": {
                "square": "cr_target_Cq2_Tq1.square.pulse"
            }
        },
        "cr_target_Cq2_Tq3": {
            "RF_inputs": {
                "port": [
                    "octave1",
                    4
                ]
            },
            "intermediate_frequency": -200000000,
            "operations": {
                "square": "cr_target_Cq2_Tq3.square.pulse"
            }
        },
        "cr_target_Cq3_Tq2": {
            "RF_inputs": {
                "port": [
                    "octave1",
                    3
                ]
            },
            "intermediate_frequency": -200000000,
            "operations": {
                "square": "cr_target_Cq3_Tq2.square.pulse"
            }
        },
        "cr_target_Cq3_Tq4": {
            "RF_inputs": {
                "port": [
                    "octave1",
                    5
                ]
            },
            "intermediate_frequency": -200000000,
            "operations": {
                "square": "cr_target_Cq3_Tq4.square.pulse"
            }
        },
        "cr_target_Cq4_Tq3": {
            "RF_inputs": {
                "port": [
                    "octave1",
                    4
                ]
            },
            "intermediate_frequency": -200000000,
            "operations": {
                "square": "cr_target_Cq4_Tq3.square.pulse"
            }
        },
        "q1.resonator": {
            "RF_inputs": {
                "port": [
                    "octave1",
                    1
                ]
            },
            "RF_outputs": {
                "port": [
                    "octave1",
                    1
                ]
            },
            "digitalInputs": {
                "octave_switch": {
                    "buffer": 15,
                    "delay": 87,
                    "port": [
                        "con1",
                        1,
                        1
                    ]
                }
            },
            "intermediate_frequency": -250000000,
            "operations": {
                "const": "q1.resonator.const.pulse",
                "readout": "q1.resonator.readout.pulse"
            },
            "smearing": 0,
            "time_of_flight": 24
        },
        "q1.xy": {
            "RF_inputs": {
                "port": [
                    "octave1",
                    2
                ]
            },
            "digitalInputs": {
                "octave_switch": {
                    "buffer": 15,
                    "delay": 87,
                    "port": [
                        "con1",
                        1,
                        3
                    ]
                }
            },
            "intermediate_frequency": -200000000,
            "operations": {
                "-x90_DragGaussian": "q1.xy.-x90_DragGaussian.pulse",
                "-x90_Square": "q1.xy.-x90_Square.pulse",
                "-y90_DragGaussian": "q1.xy.-y90_DragGaussian.pulse",
                "-y90_Square": "q1.xy.-y90_Square.pulse",
                "saturation": "q1.xy.saturation.pulse",
                "x180_DragGaussian": "q1.xy.x180_DragGaussian.pulse",
                "x180_Square": "q1.xy.x180_Square.pulse",
                "x90_DragGaussian": "q1.xy.x90_DragGaussian.pulse",
                "x90_Square": "q1.xy.x90_Square.pulse",
                "y180_DragGaussian": "q1.xy.y180_DragGaussian.pulse",
                "y180_Square": "q1.xy.y180_Square.pulse",
                "y90_DragGaussian": "q1.xy.y90_DragGaussian.pulse",
                "y90_Square": "q1.xy.y90_Square.pulse"
            }
        },
        "q2.resonator": {
            "RF_inputs": {
                "port": [
                    "octave1",
                    1
                ]
            },
            "RF_outputs": {
                "port": [
                    "octave1",
                    1
                ]
            },
            "digitalInputs": {
                "octave_switch": {
                    "buffer": 15,
                    "delay": 87,
                    "port": [
                        "con1",
                        1,
                        1
                    ]
                }
            },
            "intermediate_frequency": -250000000,
            "operations": {
                "const": "q2.resonator.const.pulse",
                "readout": "q2.resonator.readout.pulse"
            },
            "smearing": 0,
            "time_of_flight": 24
        },
        "q2.xy": {
            "RF_inputs": {
                "port": [
                    "octave1",
                    3
                ]
            },
            "digitalInputs": {
                "octave_switch": {
                    "buffer": 15,
                    "delay": 87,
                    "port": [
                        "con1",
                        1,
                        5
                    ]
                }
            },
            "intermediate_frequency": -200000000,
            "operations": {
                "-x90_DragGaussian": "q2.xy.-x90_DragGaussian.pulse",
                "-x90_Square": "q2.xy.-x90_Square.pulse",
                "-y90_DragGaussian": "q2.xy.-y90_DragGaussian.pulse",
                "-y90_Square": "q2.xy.-y90_Square.pulse",
                "saturation": "q2.xy.saturation.pulse",
                "x180_DragGaussian": "q2.xy.x180_DragGaussian.pulse",
                "x180_Square": "q2.xy.x180_Square.pulse",
                "x90_DragGaussian": "q2.xy.x90_DragGaussian.pulse",
                "x90_Square": "q2.xy.x90_Square.pulse",
                "y180_DragGaussian": "q2.xy.y180_DragGaussian.pulse",
                "y180_Square": "q2.xy.y180_Square.pulse",
                "y90_DragGaussian": "q2.xy.y90_DragGaussian.pulse",
                "y90_Square": "q2.xy.y90_Square.pulse"
            }
        },
        "q3.resonator": {
            "RF_inputs": {
                "port": [
                    "octave1",
                    1
                ]
            },
            "RF_outputs": {
                "port": [
                    "octave1",
                    1
                ]
            },
            "digitalInputs": {
                "octave_switch": {
                    "buffer": 15,
                    "delay": 87,
                    "port": [
                        "con1",
                        1,
                        1
                    ]
                }
            },
            "intermediate_frequency": -250000000,
            "operations": {
                "const": "q3.resonator.const.pulse",
                "readout": "q3.resonator.readout.pulse"
            },
            "smearing": 0,
            "time_of_flight": 24
        },
        "q3.xy": {
            "RF_inputs": {
                "port": [
                    "octave1",
                    4
                ]
            },
            "digitalInputs": {
                "octave_switch": {
                    "buffer": 15,
                    "delay": 87,
                    "port": [
                        "con1",
                        1,
                        7
                    ]
                }
            },
            "intermediate_frequency": -200000000,
            "operations": {
                "-x90_DragGaussian": "q3.xy.-x90_DragGaussian.pulse",
                "-x90_Square": "q3.xy.-x90_Square.pulse",
                "-y90_DragGaussian": "q3.xy.-y90_DragGaussian.pulse",
                "-y90_Square": "q3.xy.-y90_Square.pulse",
                "saturation": "q3.xy.saturation.pulse",
                "x180_DragGaussian": "q3.xy.x180_DragGaussian.pulse",
                "x180_Square": "q3.xy.x180_Square.pulse",
                "x90_DragGaussian": "q3.xy.x90_DragGaussian.pulse",
                "x90_Square": "q3.xy.x90_Square.pulse",
                "y180_DragGaussian": "q3.xy.y180_DragGaussian.pulse",
                "y180_Square": "q3.xy.y180_Square.pulse",
                "y90_DragGaussian": "q3.xy.y90_DragGaussian.pulse",
                "y90_Square": "q3.xy.y90_Square.pulse"
            }
        },
        "q4.resonator": {
            "RF_inputs": {
                "port": [
                    "octave1",
                    1
                ]
            },
            "RF_outputs": {
                "port": [
                    "octave1",
                    1
                ]
            },
            "digitalInputs": {
                "octave_switch": {
                    "buffer": 15,
                    "delay": 87,
                    "port": [
                        "con1",
                        1,
                        1
                    ]
                }
            },
            "intermediate_frequency": -250000000,
            "operations": {
                "const": "q4.resonator.const.pulse",
                "readout": "q4.resonator.readout.pulse"
            },
            "smearing": 0,
            "time_of_flight": 24
        },
        "q4.xy": {
            "RF_inputs": {
                "port": [
                    "octave1",
                    5
                ]
            },
            "digitalInputs": {
                "octave_switch": {
                    "buffer": 15,
                    "delay": 87,
                    "port": [
                        "con1",
                        1,
                        9
                    ]
                }
            },
            "intermediate_frequency": -200000000,
            "operations": {
                "-x90_DragGaussian": "q4.xy.-x90_DragGaussian.pulse",
                "-x90_Square": "q4.xy.-x90_Square.pulse",
                "-y90_DragGaussian": "q4.xy.-y90_DragGaussian.pulse",
                "-y90_Square": "q4.xy.-y90_Square.pulse",
                "saturation": "q4.xy.saturation.pulse",
                "x180_DragGaussian": "q4.xy.x180_DragGaussian.pulse",
                "x180_Square": "q4.xy.x180_Square.pulse",
                "x90_DragGaussian": "q4.xy.x90_DragGaussian.pulse",
                "x90_Square": "q4.xy.x90_Square.pulse",
                "y180_DragGaussian": "q4.xy.y180_DragGaussian.pulse",
                "y180_Square": "q4.xy.y180_Square.pulse",
                "y90_DragGaussian": "q4.xy.y90_DragGaussian.pulse",
                "y90_Square": "q4.xy.y90_Square.pulse"
            }
        }
    },
    "integration_weights": {
        "q1.resonator.readout.iw1": {
            "cosine": [
                [
                    1.0,
                    1024
                ]
            ],
            "sine": [
                [
                    -0.0,
                    1024
                ]
            ]
        },
        "q1.resonator.readout.iw2": {
            "cosine": [
                [
                    0.0,
                    1024
                ]
            ],
            "sine": [
                [
                    1.0,
                    1024
                ]
            ]
        },
        "q1.resonator.readout.iw3": {
            "cosine": [
                [
                    -0.0,
                    1024
                ]
            ],
            "sine": [
                [
                    -1.0,
                    1024
                ]
            ]
        },
        "q2.resonator.readout.iw1": {
            "cosine": [
                [
                    1.0,
                    1024
                ]
            ],
            "sine": [
                [
                    -0.0,
                    1024
                ]
            ]
        },
        "q2.resonator.readout.iw2": {
            "cosine": [
                [
                    0.0,
                    1024
                ]
            ],
            "sine": [
                [
                    1.0,
                    1024
                ]
            ]
        },
        "q2.resonator.readout.iw3": {
            "cosine": [
                [
                    -0.0,
                    1024
                ]
            ],
            "sine": [
                [
                    -1.0,
                    1024
                ]
            ]
        },
        "q3.resonator.readout.iw1": {
            "cosine": [
                [
                    1.0,
                    1024
                ]
            ],
            "sine": [
                [
                    -0.0,
                    1024
                ]
            ]
        },
        "q3.resonator.readout.iw2": {
            "cosine": [
                [
                    0.0,
                    1024
                ]
            ],
            "sine": [
                [
                    1.0,
                    1024
                ]
            ]
        },
        "q3.resonator.readout.iw3": {
            "cosine": [
                [
                    -0.0,
                    1024
                ]
            ],
            "sine": [
                [
                    -1.0,
                    1024
                ]
            ]
        },
        "q4.resonator.readout.iw1": {
            "cosine": [
                [
                    1.0,
                    1024
                ]
            ],
            "sine": [
                [
                    -0.0,
                    1024
                ]
            ]
        },
        "q4.resonator.readout.iw2": {
            "cosine": [
                [
                    0.0,
                    1024
                ]
            ],
            "sine": [
                [
                    1.0,
                    1024
                ]
            ]
        },
        "q4.resonator.readout.iw3": {
            "cosine": [
                [
                    -0.0,
                    1024
                ]
            ],
            "sine": [
                [
                    -1.0,
                    1024
                ]
            ]
        }
    },
    "mixers": {},
    "octaves": {
        "octave1": {
            "IF_outputs": {
                "IF_out1": {
                    "name": "out1",
                    "port": [
                        "con1",
                        1,
                        1
                    ]
                },
                "IF_out2": {
                    "name": "out2",
                    "port": [
                        "con1",
                        1,
                        2
                    ]
                }
            },
            "RF_inputs": {
                "1": {
                    "IF_mode_I": "direct",
                    "IF_mode_Q": "direct",
                    "LO_frequency": 6200000000,
                    "LO_source": "internal",
                    "RF_source": "RF_in"
                }
            },
            "RF_outputs": {
                "1": {
                    "I_connection": [
                        "con1",
                        1,
                        1
                    ],
                    "LO_frequency": 6200000000,
                    "LO_source": "internal",
                    "Q_connection": [
                        "con1",
                        1,
                        2
                    ],
                    "gain": 0,
                    "input_attenuators": "off",
                    "output_mode": "always_on"
                },
                "2": {
                    "I_connection": [
                        "con1",
                        1,
                        3
                    ],
                    "LO_frequency": 4700000000,
                    "LO_source": "internal",
                    "Q_connection": [
                        "con1",
                        1,
                        4
                    ],
                    "gain": 0,
                    "input_attenuators": "off",
                    "output_mode": "always_on"
                },
                "3": {
                    "I_connection": [
                        "con1",
                        1,
                        5
                    ],
                    "LO_frequency": 4700000000,
                    "LO_source": "internal",
                    "Q_connection": [
                        "con1",
                        1,
                        6
                    ],
                    "gain": 0,
                    "input_attenuators": "off",
                    "output_mode": "always_on"
                },
                "4": {
                    "I_connection": [
                        "con1",
                        1,
                        7
                    ],
                    "LO_frequency": 4700000000,
                    "LO_source": "internal",
                    "Q_connection": [
                        "con1",
                        1,
                        8
                    ],
                    "gain": 0,
                    "input_attenuators": "off",
                    "output_mode": "always_on"
                },
                "5": {
                    "I_connection": [
                        "con1",
                        1,
                        9
                    ],
                    "LO_frequency": 4700000000,
                    "LO_source": "internal",
                    "Q_connection": [
                        "con1",
                        1,
                        10
                    ],
                    "gain": 0,
                    "input_attenuators": "off",
                    "output_mode": "always_on"
                }
            },
            "loopbacks": []
        },
        "octave2": {
            "IF_outputs": {},
            "RF_inputs": {},
            "RF_outputs": {},
            "loopbacks": []
        },
        "octave3": {
            "IF_outputs": {},
            "RF_inputs": {},
            "RF_outputs": {},
            "loopbacks": []
        }
    },
    "oscillators": {},
    "pulses": {
        "const_pulse": {
            "length": 1000,
            "operation": "control",
            "waveforms": {
                "I": "const_wf",
                "Q": "zero_wf"
            }
        },
        "cr_control_Cq1_Tq2.square.pulse": {
            "length": 100,
            "operation": "control",
            "waveforms": {
                "I": "cr_control_Cq1_Tq2.square.wf.I",
                "Q": "cr_control_Cq1_Tq2.square.wf.Q"
            }
        },
        "cr_control_Cq2_Tq1.square.pulse": {
            "length": 100,
            "operation": "control",
            "waveforms": {
                "I": "cr_control_Cq2_Tq1.square.wf.I",
                "Q": "cr_control_Cq2_Tq1.square.wf.Q"
            }
        },
        "cr_control_Cq2_Tq3.square.pulse": {
            "length": 100,
            "operation": "control",
            "waveforms": {
                "I": "cr_control_Cq2_Tq3.square.wf.I",
                "Q": "cr_control_Cq2_Tq3.square.wf.Q"
            }
        },
        "cr_control_Cq3_Tq2.square.pulse": {
            "length": 100,
            "operation": "control",
            "waveforms": {
                "I": "cr_control_Cq3_Tq2.square.wf.I",
                "Q": "cr_control_Cq3_Tq2.square.wf.Q"
            }
        },
        "cr_control_Cq3_Tq4.square.pulse": {
            "length": 100,
            "operation": "control",
            "waveforms": {
                "I": "cr_control_Cq3_Tq4.square.wf.I",
                "Q": "cr_control_Cq3_Tq4.square.wf.Q"
            }
        },
        "cr_control_Cq4_Tq3.square.pulse": {
            "length": 100,
            "operation": "control",
            "waveforms": {
                "I": "cr_control_Cq4_Tq3.square.wf.I",
                "Q": "cr_control_Cq4_Tq3.square.wf.Q"
            }
        },
        "cr_target_Cq1_Tq2.square.pulse": {
            "length": 100,
            "operation": "control",
            "waveforms": {
                "I": "cr_target_Cq1_Tq2.square.wf.I",
                "Q": "cr_target_Cq1_Tq2.square.wf.Q"
            }
        },
        "cr_target_Cq2_Tq1.square.pulse": {
            "length": 100,
            "operation": "control",
            "waveforms": {
                "I": "cr_target_Cq2_Tq1.square.wf.I",
                "Q": "cr_target_Cq2_Tq1.square.wf.Q"
            }
        },
        "cr_target_Cq2_Tq3.square.pulse": {
            "length": 100,
            "operation": "control",
            "waveforms": {
                "I": "cr_target_Cq2_Tq3.square.wf.I",
                "Q": "cr_target_Cq2_Tq3.square.wf.Q"
            }
        },
        "cr_target_Cq3_Tq2.square.pulse": {
            "length": 100,
            "operation": "control",
            "waveforms": {
                "I": "cr_target_Cq3_Tq2.square.wf.I",
                "Q": "cr_target_Cq3_Tq2.square.wf.Q"
            }
        },
        "cr_target_Cq3_Tq4.square.pulse": {
            "length": 100,
            "operation": "control",
            "waveforms": {
                "I": "cr_target_Cq3_Tq4.square.wf.I",
                "Q": "cr_target_Cq3_Tq4.square.wf.Q"
            }
        },
        "cr_target_Cq4_Tq3.square.pulse": {
            "length": 100,
            "operation": "control",
            "waveforms": {
                "I": "cr_target_Cq4_Tq3.square.wf.I",
                "Q": "cr_target_Cq4_Tq3.square.wf.Q"
            }
        },
        "q1.resonator.const.pulse": {
            "length": 100,
            "operation": "control",
            "waveforms": {
                "I": "q1.resonator.const.wf.I",
                "Q": "q1.resonator.const.wf.Q"
            }
        },
        "q1.resonator.readout.pulse": {
            "digital_marker": "ON",
            "integration_weights": {
                "iw1": "q1.resonator.readout.iw1",
                "iw2": "q1.resonator.readout.iw2",
                "iw3": "q1.resonator.readout.iw3"
            },
            "length": 1024,
            "operation": "measurement",
            "waveforms": {
                "I": "q1.resonator.readout.wf.I",
                "Q": "q1.resonator.readout.wf.Q"
            }
        },
        "q1.xy.-x90_DragGaussian.pulse": {
            "digital_marker": "ON",
            "length": 40,
            "operation": "control",
            "waveforms": {
                "I": "q1.xy.-x90_DragGaussian.wf.I",
                "Q": "q1.xy.-x90_DragGaussian.wf.Q"
            }
        },
        "q1.xy.-x90_Square.pulse": {
            "digital_marker": "ON",
            "length": 100,
            "operation": "control",
            "waveforms": {
                "I": "q1.xy.-x90_Square.wf.I",
                "Q": "q1.xy.-x90_Square.wf.Q"
            }
        },
        "q1.xy.-y90_DragGaussian.pulse": {
            "digital_marker": "ON",
            "length": 40,
            "operation": "control",
            "waveforms": {
                "I": "q1.xy.-y90_DragGaussian.wf.I",
                "Q": "q1.xy.-y90_DragGaussian.wf.Q"
            }
        },
        "q1.xy.-y90_Square.pulse": {
            "digital_marker": "ON",
            "length": 100,
            "operation": "control",
            "waveforms": {
                "I": "q1.xy.-y90_Square.wf.I",
                "Q": "q1.xy.-y90_Square.wf.Q"
            }
        },
        "q1.xy.saturation.pulse": {
            "digital_marker": "ON",
            "length": 10000,
            "operation": "control",
            "waveforms": {
                "I": "q1.xy.saturation.wf.I",
                "Q": "q1.xy.saturation.wf.Q"
            }
        },
        "q1.xy.x180_DragGaussian.pulse": {
            "digital_marker": "ON",
            "length": 40,
            "operation": "control",
            "waveforms": {
                "I": "q1.xy.x180_DragGaussian.wf.I",
                "Q": "q1.xy.x180_DragGaussian.wf.Q"
            }
        },
        "q1.xy.x180_Square.pulse": {
            "digital_marker": "ON",
            "length": 100,
            "operation": "control",
            "waveforms": {
                "I": "q1.xy.x180_Square.wf.I",
                "Q": "q1.xy.x180_Square.wf.Q"
            }
        },
        "q1.xy.x90_DragGaussian.pulse": {
            "digital_marker": "ON",
            "length": 40,
            "operation": "control",
            "waveforms": {
                "I": "q1.xy.x90_DragGaussian.wf.I",
                "Q": "q1.xy.x90_DragGaussian.wf.Q"
            }
        },
        "q1.xy.x90_Square.pulse": {
            "digital_marker": "ON",
            "length": 100,
            "operation": "control",
            "waveforms": {
                "I": "q1.xy.x90_Square.wf.I",
                "Q": "q1.xy.x90_Square.wf.Q"
            }
        },
        "q1.xy.y180_DragGaussian.pulse": {
            "digital_marker": "ON",
            "length": 40,
            "operation": "control",
            "waveforms": {
                "I": "q1.xy.y180_DragGaussian.wf.I",
                "Q": "q1.xy.y180_DragGaussian.wf.Q"
            }
        },
        "q1.xy.y180_Square.pulse": {
            "digital_marker": "ON",
            "length": 100,
            "operation": "control",
            "waveforms": {
                "I": "q1.xy.y180_Square.wf.I",
                "Q": "q1.xy.y180_Square.wf.Q"
            }
        },
        "q1.xy.y90_DragGaussian.pulse": {
            "digital_marker": "ON",
            "length": 40,
            "operation": "control",
            "waveforms": {
                "I": "q1.xy.y90_DragGaussian.wf.I",
                "Q": "q1.xy.y90_DragGaussian.wf.Q"
            }
        },
        "q1.xy.y90_Square.pulse": {
            "digital_marker": "ON",
            "length": 100,
            "operation": "control",
            "waveforms": {
                "I": "q1.xy.y90_Square.wf.I",
                "Q": "q1.xy.y90_Square.wf.Q"
            }
        },
        "q2.resonator.const.pulse": {
            "length": 100,
            "operation": "control",
            "waveforms": {
                "I": "q2.resonator.const.wf.I",
                "Q": "q2.resonator.const.wf.Q"
            }
        },
        "q2.resonator.readout.pulse": {
            "digital_marker": "ON",
            "integration_weights": {
                "iw1": "q2.resonator.readout.iw1",
                "iw2": "q2.resonator.readout.iw2",
                "iw3": "q2.resonator.readout.iw3"
            },
            "length": 1024,
            "operation": "measurement",
            "waveforms": {
                "I": "q2.resonator.readout.wf.I",
                "Q": "q2.resonator.readout.wf.Q"
            }
        },
        "q2.xy.-x90_DragGaussian.pulse": {
            "digital_marker": "ON",
            "length": 40,
            "operation": "control",
            "waveforms": {
                "I": "q2.xy.-x90_DragGaussian.wf.I",
                "Q": "q2.xy.-x90_DragGaussian.wf.Q"
            }
        },
        "q2.xy.-x90_Square.pulse": {
            "digital_marker": "ON",
            "length": 100,
            "operation": "control",
            "waveforms": {
                "I": "q2.xy.-x90_Square.wf.I",
                "Q": "q2.xy.-x90_Square.wf.Q"
            }
        },
        "q2.xy.-y90_DragGaussian.pulse": {
            "digital_marker": "ON",
            "length": 40,
            "operation": "control",
            "waveforms": {
                "I": "q2.xy.-y90_DragGaussian.wf.I",
                "Q": "q2.xy.-y90_DragGaussian.wf.Q"
            }
        },
        "q2.xy.-y90_Square.pulse": {
            "digital_marker": "ON",
            "length": 100,
            "operation": "control",
            "waveforms": {
                "I": "q2.xy.-y90_Square.wf.I",
                "Q": "q2.xy.-y90_Square.wf.Q"
            }
        },
        "q2.xy.saturation.pulse": {
            "digital_marker": "ON",
            "length": 10000,
            "operation": "control",
            "waveforms": {
                "I": "q2.xy.saturation.wf.I",
                "Q": "q2.xy.saturation.wf.Q"
            }
        },
        "q2.xy.x180_DragGaussian.pulse": {
            "digital_marker": "ON",
            "length": 40,
            "operation": "control",
            "waveforms": {
                "I": "q2.xy.x180_DragGaussian.wf.I",
                "Q": "q2.xy.x180_DragGaussian.wf.Q"
            }
        },
        "q2.xy.x180_Square.pulse": {
            "digital_marker": "ON",
            "length": 100,
            "operation": "control",
            "waveforms": {
                "I": "q2.xy.x180_Square.wf.I",
                "Q": "q2.xy.x180_Square.wf.Q"
            }
        },
        "q2.xy.x90_DragGaussian.pulse": {
            "digital_marker": "ON",
            "length": 40,
            "operation": "control",
            "waveforms": {
                "I": "q2.xy.x90_DragGaussian.wf.I",
                "Q": "q2.xy.x90_DragGaussian.wf.Q"
            }
        },
        "q2.xy.x90_Square.pulse": {
            "digital_marker": "ON",
            "length": 100,
            "operation": "control",
            "waveforms": {
                "I": "q2.xy.x90_Square.wf.I",
                "Q": "q2.xy.x90_Square.wf.Q"
            }
        },
        "q2.xy.y180_DragGaussian.pulse": {
            "digital_marker": "ON",
            "length": 40,
            "operation": "control",
            "waveforms": {
                "I": "q2.xy.y180_DragGaussian.wf.I",
                "Q": "q2.xy.y180_DragGaussian.wf.Q"
            }
        },
        "q2.xy.y180_Square.pulse": {
            "digital_marker": "ON",
            "length": 100,
            "operation": "control",
            "waveforms": {
                "I": "q2.xy.y180_Square.wf.I",
                "Q": "q2.xy.y180_Square.wf.Q"
            }
        },
        "q2.xy.y90_DragGaussian.pulse": {
            "digital_marker": "ON",
            "length": 40,
            "operation": "control",
            "waveforms": {
                "I": "q2.xy.y90_DragGaussian.wf.I",
                "Q": "q2.xy.y90_DragGaussian.wf.Q"
            }
        },
        "q2.xy.y90_Square.pulse": {
            "digital_marker": "ON",
            "length": 100,
            "operation": "control",
            "waveforms": {
                "I": "q2.xy.y90_Square.wf.I",
                "Q": "q2.xy.y90_Square.wf.Q"
            }
        },
        "q3.resonator.const.pulse": {
            "length": 100,
            "operation": "control",
            "waveforms": {
                "I": "q3.resonator.const.wf.I",
                "Q": "q3.resonator.const.wf.Q"
            }
        },
        "q3.resonator.readout.pulse": {
            "digital_marker": "ON",
            "integration_weights": {
                "iw1": "q3.resonator.readout.iw1",
                "iw2": "q3.resonator.readout.iw2",
                "iw3": "q3.resonator.readout.iw3"
            },
            "length": 1024,
            "operation": "measurement",
            "waveforms": {
                "I": "q3.resonator.readout.wf.I",
                "Q": "q3.resonator.readout.wf.Q"
            }
        },
        "q3.xy.-x90_DragGaussian.pulse": {
            "digital_marker": "ON",
            "length": 40,
            "operation": "control",
            "waveforms": {
                "I": "q3.xy.-x90_DragGaussian.wf.I",
                "Q": "q3.xy.-x90_DragGaussian.wf.Q"
            }
        },
        "q3.xy.-x90_Square.pulse": {
            "digital_marker": "ON",
            "length": 100,
            "operation": "control",
            "waveforms": {
                "I": "q3.xy.-x90_Square.wf.I",
                "Q": "q3.xy.-x90_Square.wf.Q"
            }
        },
        "q3.xy.-y90_DragGaussian.pulse": {
            "digital_marker": "ON",
            "length": 40,
            "operation": "control",
            "waveforms": {
                "I": "q3.xy.-y90_DragGaussian.wf.I",
                "Q": "q3.xy.-y90_DragGaussian.wf.Q"
            }
        },
        "q3.xy.-y90_Square.pulse": {
            "digital_marker": "ON",
            "length": 100,
            "operation": "control",
            "waveforms": {
                "I": "q3.xy.-y90_Square.wf.I",
                "Q": "q3.xy.-y90_Square.wf.Q"
            }
        },
        "q3.xy.saturation.pulse": {
            "digital_marker": "ON",
            "length": 10000,
            "operation": "control",
            "waveforms": {
                "I": "q3.xy.saturation.wf.I",
                "Q": "q3.xy.saturation.wf.Q"
            }
        },
        "q3.xy.x180_DragGaussian.pulse": {
            "digital_marker": "ON",
            "length": 40,
            "operation": "control",
            "waveforms": {
                "I": "q3.xy.x180_DragGaussian.wf.I",
                "Q": "q3.xy.x180_DragGaussian.wf.Q"
            }
        },
        "q3.xy.x180_Square.pulse": {
            "digital_marker": "ON",
            "length": 100,
            "operation": "control",
            "waveforms": {
                "I": "q3.xy.x180_Square.wf.I",
                "Q": "q3.xy.x180_Square.wf.Q"
            }
        },
        "q3.xy.x90_DragGaussian.pulse": {
            "digital_marker": "ON",
            "length": 40,
            "operation": "control",
            "waveforms": {
                "I": "q3.xy.x90_DragGaussian.wf.I",
                "Q": "q3.xy.x90_DragGaussian.wf.Q"
            }
        },
        "q3.xy.x90_Square.pulse": {
            "digital_marker": "ON",
            "length": 100,
            "operation": "control",
            "waveforms": {
                "I": "q3.xy.x90_Square.wf.I",
                "Q": "q3.xy.x90_Square.wf.Q"
            }
        },
        "q3.xy.y180_DragGaussian.pulse": {
            "digital_marker": "ON",
            "length": 40,
            "operation": "control",
            "waveforms": {
                "I": "q3.xy.y180_DragGaussian.wf.I",
                "Q": "q3.xy.y180_DragGaussian.wf.Q"
            }
        },
        "q3.xy.y180_Square.pulse": {
            "digital_marker": "ON",
            "length": 100,
            "operation": "control",
            "waveforms": {
                "I": "q3.xy.y180_Square.wf.I",
                "Q": "q3.xy.y180_Square.wf.Q"
            }
        },
        "q3.xy.y90_DragGaussian.pulse": {
            "digital_marker": "ON",
            "length": 40,
            "operation": "control",
            "waveforms": {
                "I": "q3.xy.y90_DragGaussian.wf.I",
                "Q": "q3.xy.y90_DragGaussian.wf.Q"
            }
        },
        "q3.xy.y90_Square.pulse": {
            "digital_marker": "ON",
            "length": 100,
            "operation": "control",
            "waveforms": {
                "I": "q3.xy.y90_Square.wf.I",
                "Q": "q3.xy.y90_Square.wf.Q"
            }
        },
        "q4.resonator.const.pulse": {
            "length": 100,
            "operation": "control",
            "waveforms": {
                "I": "q4.resonator.const.wf.I",
                "Q": "q4.resonator.const.wf.Q"
            }
        },
        "q4.resonator.readout.pulse": {
            "digital_marker": "ON",
            "integration_weights": {
                "iw1": "q4.resonator.readout.iw1",
                "iw2": "q4.resonator.readout.iw2",
                "iw3": "q4.resonator.readout.iw3"
            },
            "length": 1024,
            "operation": "measurement",
            "waveforms": {
                "I": "q4.resonator.readout.wf.I",
                "Q": "q4.resonator.readout.wf.Q"
            }
        },
        "q4.xy.-x90_DragGaussian.pulse": {
            "digital_marker": "ON",
            "length": 40,
            "operation": "control",
            "waveforms": {
                "I": "q4.xy.-x90_DragGaussian.wf.I",
                "Q": "q4.xy.-x90_DragGaussian.wf.Q"
            }
        },
        "q4.xy.-x90_Square.pulse": {
            "digital_marker": "ON",
            "length": 100,
            "operation": "control",
            "waveforms": {
                "I": "q4.xy.-x90_Square.wf.I",
                "Q": "q4.xy.-x90_Square.wf.Q"
            }
        },
        "q4.xy.-y90_DragGaussian.pulse": {
            "digital_marker": "ON",
            "length": 40,
            "operation": "control",
            "waveforms": {
                "I": "q4.xy.-y90_DragGaussian.wf.I",
                "Q": "q4.xy.-y90_DragGaussian.wf.Q"
            }
        },
        "q4.xy.-y90_Square.pulse": {
            "digital_marker": "ON",
            "length": 100,
            "operation": "control",
            "waveforms": {
                "I": "q4.xy.-y90_Square.wf.I",
                "Q": "q4.xy.-y90_Square.wf.Q"
            }
        },
        "q4.xy.saturation.pulse": {
            "digital_marker": "ON",
            "length": 10000,
            "operation": "control",
            "waveforms": {
                "I": "q4.xy.saturation.wf.I",
                "Q": "q4.xy.saturation.wf.Q"
            }
        },
        "q4.xy.x180_DragGaussian.pulse": {
            "digital_marker": "ON",
            "length": 40,
            "operation": "control",
            "waveforms": {
                "I": "q4.xy.x180_DragGaussian.wf.I",
                "Q": "q4.xy.x180_DragGaussian.wf.Q"
            }
        },
        "q4.xy.x180_Square.pulse": {
            "digital_marker": "ON",
            "length": 100,
            "operation": "control",
            "waveforms": {
                "I": "q4.xy.x180_Square.wf.I",
                "Q": "q4.xy.x180_Square.wf.Q"
            }
        },
        "q4.xy.x90_DragGaussian.pulse": {
            "digital_marker": "ON",
            "length": 40,
            "operation": "control",
            "waveforms": {
                "I": "q4.xy.x90_DragGaussian.wf.I",
                "Q": "q4.xy.x90_DragGaussian.wf.Q"
            }
        },
        "q4.xy.x90_Square.pulse": {
            "digital_marker": "ON",
            "length": 100,
            "operation": "control",
            "waveforms": {
                "I": "q4.xy.x90_Square.wf.I",
                "Q": "q4.xy.x90_Square.wf.Q"
            }
        },
        "q4.xy.y180_DragGaussian.pulse": {
            "digital_marker": "ON",
            "length": 40,
            "operation": "control",
            "waveforms": {
                "I": "q4.xy.y180_DragGaussian.wf.I",
                "Q": "q4.xy.y180_DragGaussian.wf.Q"
            }
        },
        "q4.xy.y180_Square.pulse": {
            "digital_marker": "ON",
            "length": 100,
            "operation": "control",
            "waveforms": {
                "I": "q4.xy.y180_Square.wf.I",
                "Q": "q4.xy.y180_Square.wf.Q"
            }
        },
        "q4.xy.y90_DragGaussian.pulse": {
            "digital_marker": "ON",
            "length": 40,
            "operation": "control",
            "waveforms": {
                "I": "q4.xy.y90_DragGaussian.wf.I",
                "Q": "q4.xy.y90_DragGaussian.wf.Q"
            }
        },
        "q4.xy.y90_Square.pulse": {
            "digital_marker": "ON",
            "length": 100,
            "operation": "control",
            "waveforms": {
                "I": "q4.xy.y90_Square.wf.I",
                "Q": "q4.xy.y90_Square.wf.Q"
            }
        }
    },
    "version": 1,
    "waveforms": {
        "const_wf": {
            "sample": 0.1,
            "type": "constant"
        },
        "cr_control_Cq1_Tq2.square.wf.I": {
            "sample": 0.1,
            "type": "constant"
        },
        "cr_control_Cq1_Tq2.square.wf.Q": {
            "sample": 0.0,
            "type": "constant"
        },
        "cr_control_Cq2_Tq1.square.wf.I": {
            "sample": 0.1,
            "type": "constant"
        },
        "cr_control_Cq2_Tq1.square.wf.Q": {
            "sample": 0.0,
            "type": "constant"
        },
        "cr_control_Cq2_Tq3.square.wf.I": {
            "sample": 0.1,
            "type": "constant"
        },
        "cr_control_Cq2_Tq3.square.wf.Q": {
            "sample": 0.0,
            "type": "constant"
        },
        "cr_control_Cq3_Tq2.square.wf.I": {
            "sample": 0.1,
            "type": "constant"
        },
        "cr_control_Cq3_Tq2.square.wf.Q": {
            "sample": 0.0,
            "type": "constant"
        },
        "cr_control_Cq3_Tq4.square.wf.I": {
            "sample": 0.1,
            "type": "constant"
        },
        "cr_control_Cq3_Tq4.square.wf.Q": {
            "sample": 0.0,
            "type": "constant"
        },
        "cr_control_Cq4_Tq3.square.wf.I": {
            "sample": 0.1,
            "type": "constant"
        },
        "cr_control_Cq4_Tq3.square.wf.Q": {
            "sample": 0.0,
            "type": "constant"
        },
        "cr_target_Cq1_Tq2.square.wf.I": {
            "sample": 0.1,
            "type": "constant"
        },
        "cr_target_Cq1_Tq2.square.wf.Q": {
            "sample": 0.0,
            "type": "constant"
        },
        "cr_target_Cq2_Tq1.square.wf.I": {
            "sample": 0.1,
            "type": "constant"
        },
        "cr_target_Cq2_Tq1.square.wf.Q": {
            "sample": 0.0,
            "type": "constant"
        },
        "cr_target_Cq2_Tq3.square.wf.I": {
            "sample": 0.1,
            "type": "constant"
        },
        "cr_target_Cq2_Tq3.square.wf.Q": {
            "sample": 0.0,
            "type": "constant"
        },
        "cr_target_Cq3_Tq2.square.wf.I": {
            "sample": 0.1,
            "type": "constant"
        },
        "cr_target_Cq3_Tq2.square.wf.Q": {
            "sample": 0.0,
            "type": "constant"
        },
        "cr_target_Cq3_Tq4.square.wf.I": {
            "sample": 0.1,
            "type": "constant"
        },
        "cr_target_Cq3_Tq4.square.wf.Q": {
            "sample": 0.0,
            "type": "constant"
        },
        "cr_target_Cq4_Tq3.square.wf.I": {
            "sample": 0.1,
            "type": "constant"
        },
        "cr_target_Cq4_Tq3.square.wf.Q": {
            "sample": 0.0,
            "type": "constant"
        },
        "q1.resonator.const.wf.I": {
            "sample": 0.125,
            "type": "constant"
        },
        "q1.resonator.const.wf.Q": {
            "sample": 0.0,
            "type": "constant"
        },
        "q1.resonator.readout.wf.I": {
            "sample": 0.01,
            "type": "constant"
        },
        "q1.resonator.readout.wf.Q": {
            "sample": 0.0,
            "type": "constant"
        },
        "q1.xy.-x90_DragGaussian.wf.I": {
            "samples": [
                0.0,
                -0.0004890327182525387,
                -0.0011644107780623145,
                -0.002075509236305739,
                -0.003275644372434133,
                -0.004818577292999117,
                -0.00675357872437716,
                -0.009119203909448838,
                -0.011936192088487896,
                -0.01520018746480943,
                -0.018875225207582575,
                -0.022889075371637223,
                -0.027131531621974618,
                -0.03145653115118992,
                -0.03568859118023487,
                -0.03963348235338423,
                -0.04309240922612172,
                -0.04587834388284734,
                -0.04783268273949085,
                -0.048840175630855964,
                -0.048840175630855964,
                -0.04783268273949085,
                -0.04587834388284734,
                -0.04309240922612172,
                -0.03963348235338423,
                -0.03568859118023487,
                -0.03145653115118992,
                -0.027131531621974618,
                -0.022889075371637223,
                -0.018875225207582575,
                -0.01520018746480943,
                -0.011936192088487896,
                -0.009119203909448838,
                -0.00675357872437716,
                -0.004818577292999117,
                -0.003275644372434133,
                -0.002075509236305739,
                -0.0011644107780623145,
                -0.0004890327182525387,
                0.0
            ],
            "type": "arbitrary"
        },
        "q1.xy.-x90_DragGaussian.wf.Q": {
            "samples": [
                -0.000435943797197449,
                -0.0006094913141771259,
                -0.0008324738298173561,
                -0.0011104271734198958,
                -0.0014459333608004257,
                -0.0018370960881248035,
                -0.002276049884602178,
                -0.002747761320845089,
                -0.0032294210033738465,
                -0.0036907174976472555,
                -0.004095214336879552,
                -0.00440291530716134,
                -0.004573912906833186,
                -0.0045727983764854655,
                -0.004373310389998592,
                -0.003962560350545937,
                -0.0033441367692767913,
                -0.0025394838391939335,
                -0.0015871684034166418,
                -0.0005399641258865475,
                0.0005399641258865475,
                0.0015871684034166418,
                0.0025394838391939335,
                0.0033441367692767913,
                0.003962560350545937,
                0.004373310389998592,
                0.0045727983764854655,
                0.004573912906833186,
                0.00440291530716134,
                0.004095214336879552,
                0.0036907174976472555,
                0.0032294210033738465,
                0.002747761320845089,
                0.002276049884602178,
                0.0018370960881248035,
                0.0014459333608004257,
                0.0011104271734198958,
                0.0008324738298173561,
                0.0006094913141771259,
                0.000435943797197449
            ],
            "type": "arbitrary"
        },
        "q1.xy.-x90_Square.wf.I": {
            "sample": -0.125,
            "type": "constant"
        },
        "q1.xy.-x90_Square.wf.Q": {
            "sample": 0.0,
            "type": "constant"
        },
        "q1.xy.-y90_DragGaussian.wf.I": {
            "samples": [
                0.0003897323002118776,
                0.0007640058598407626,
                0.0012659705743776567,
                0.0019226991170297899,
                0.0027603894194540503,
                0.003801435125769233,
                0.005060881443867484,
                0.006542564125132178,
                0.008235384354278948,
                0.01011029209238729,
                0.01211859836791348,
                0.014192182366340683,
                0.016245986363289493,
                0.018182908155689608,
                0.019900841002231842,
                0.021301233490576447,
                0.02229821874402377,
                0.022827165525111912,
                0.022851486381469707,
                0.02236672023430797,
                0.02140126798029484,
                0.020013639867016306,
                0.018286585366098087,
                0.01631892451530897,
                0.014216202025168597,
                0.012081391207135049,
                0.010006775171897499,
                0.008067860606672698,
                0.006319799176904556,
                0.004796382460114499,
                0.0035113138340095978,
                0.0024612011495233786,
                0.001629585218719835,
                0.0009913194378219203,
                0.0005167195787748112,
                0.0001750702187654058,
                -6.273725938778024e-05,
                -0.00022248707840533317,
                -0.00032576054289497737,
                -0.0003897323002118776
            ],
            "type": "arbitrary"
        },
        "q1.xy.-y90_DragGaussian.wf.Q": {
            "samples": [
                0.00019533491363934256,
                -0.00016409664136661636,
                -0.0006679697913890767,
                -0.0013579452134871266,
                -0.002280530550442407,
                -0.003484637735859785,
                -0.005017838944672815,
                -0.006921338518449501,
                -0.00922389755621834,
                -0.011935203744360644,
                -0.015039430863538327,
                -0.01848992683195512,
                -0.022206049052393713,
                -0.026073083593229362,
                -0.029945916442832322,
                -0.0336566822453979,
                -0.03702605061962234,
                -0.03987721065585537,
                -0.04205109049424396,
                -0.04342101038518449,
                -0.04390489774211652,
                -0.043473427066093674,
                -0.0421529620697138,
                -0.040022889529703086,
                -0.03720771973619628,
                -0.033865046444636206,
                -0.030170984201992244,
                -0.02630494844444297,
                -0.022435587198335633,
                -0.018709345857037613,
                -0.015242630014924659,
                -0.012117934250188766,
                -0.009383737221031349,
                -0.007057514749240971,
                -0.0051309463106254515,
                -0.0035762997297537086,
                -0.0023530514515718182,
                -0.0014139889099074009,
                -0.0007102905956519462,
                -0.00019533491363934256
            ],
            "type": "arbitrary"
        },
        "q1.xy.-y90_Square.wf.I": {
            "sample": 0.056009202016146266,
            "type": "constant"
        },
        "q1.xy.-y90_Square.wf.Q": {
            "sample": -0.11174958295006973,
            "type": "constant"
        },
        "q1.xy.saturation.wf.I": {
            "sample": 0.25,
            "type": "constant"
        },
        "q1.xy.saturation.wf.Q": {
            "sample": 0.0,
            "type": "constant"
        },
        "q1.xy.x180_DragGaussian.wf.I": {
            "samples": [
                0.0,
                0.0009780654365050775,
                0.002328821556124629,
                0.004151018472611478,
                0.006551288744868266,
                0.009637154585998235,
                0.01350715744875432,
                0.018238407818897677,
                0.02387238417697579,
                0.03040037492961886,
                0.03775045041516515,
                0.045778150743274446,
                0.054263063243949236,
                0.06291306230237984,
                0.07137718236046973,
                0.07926696470676846,
                0.08618481845224343,
                0.09175668776569468,
                0.0956653654789817,
                0.09768035126171193,
                0.09768035126171193,
                0.0956653654789817,
                0.09175668776569468,
                0.08618481845224343,
                0.07926696470676846,
                0.07137718236046973,
                0.06291306230237984,
                0.054263063243949236,
                0.045778150743274446,
                0.03775045041516515,
                0.03040037492961886,
                0.02387238417697579,
                0.018238407818897677,
                0.01350715744875432,
                0.009637154585998235,
                0.006551288744868266,
                0.004151018472611478,
                0.002328821556124629,
                0.0009780654365050775,
                0.0
            ],
            "type": "arbitrary"
        },
        "q1.xy.x180_DragGaussian.wf.Q": {
            "samples": [
                0.000871887594394898,
                0.0012189826283542518,
                0.0016649476596347123,
                0.0022208543468397917,
                0.0028918667216008514,
                0.003674192176249607,
                0.004552099769204356,
                0.005495522641690178,
                0.006458842006747693,
                0.007381434995294511,
                0.008190428673759104,
                0.00880583061432268,
                0.009147825813666372,
                0.009145596752970931,
                0.008746620779997183,
                0.007925120701091875,
                0.006688273538553583,
                0.005078967678387867,
                0.0031743368068332836,
                0.001079928251773095,
                -0.001079928251773095,
                -0.0031743368068332836,
                -0.005078967678387867,
                -0.006688273538553583,
                -0.007925120701091875,
                -0.008746620779997183,
                -0.009145596752970931,
                -0.009147825813666372,
                -0.00880583061432268,
                -0.008190428673759104,
                -0.007381434995294511,
                -0.006458842006747693,
                -0.005495522641690178,
                -0.004552099769204356,
                -0.003674192176249607,
                -0.0028918667216008514,
                -0.0022208543468397917,
                -0.0016649476596347123,
                -0.0012189826283542518,
                -0.000871887594394898
            ],
            "type": "arbitrary"
        },
        "q1.xy.x180_Square.wf.I": {
            "sample": 0.25,
            "type": "constant"
        },
        "q1.xy.x180_Square.wf.Q": {
            "sample": 0.0,
            "type": "constant"
        },
        "q1.xy.x90_DragGaussian.wf.I": {
            "samples": [
                0.0,
                0.0004890327182525387,
                0.0011644107780623145,
                0.002075509236305739,
                0.003275644372434133,
                0.004818577292999117,
                0.00675357872437716,
                0.009119203909448838,
                0.011936192088487896,
                0.01520018746480943,
                0.018875225207582575,
                0.022889075371637223,
                0.027131531621974618,
                0.03145653115118992,
                0.03568859118023487,
                0.03963348235338423,
                0.04309240922612172,
                0.04587834388284734,
                0.04783268273949085,
                0.048840175630855964,
                0.048840175630855964,
                0.04783268273949085,
                0.04587834388284734,
                0.04309240922612172,
                0.03963348235338423,
                0.03568859118023487,
                0.03145653115118992,
                0.027131531621974618,
                0.022889075371637223,
                0.018875225207582575,
                0.01520018746480943,
                0.011936192088487896,
                0.009119203909448838,
                0.00675357872437716,
                0.004818577292999117,
                0.003275644372434133,
                0.002075509236305739,
                0.0011644107780623145,
                0.0004890327182525387,
                0.0
            ],
            "type": "arbitrary"
        },
        "q1.xy.x90_DragGaussian.wf.Q": {
            "samples": [
                0.000435943797197449,
                0.0006094913141771259,
                0.0008324738298173561,
                0.0011104271734198958,
                0.0014459333608004257,
                0.0018370960881248035,
                0.002276049884602178,
                0.002747761320845089,
                0.0032294210033738465,
                0.0036907174976472555,
                0.004095214336879552,
                0.00440291530716134,
                0.004573912906833186,
                0.0045727983764854655,
                0.004373310389998592,
                0.003962560350545937,
                0.0033441367692767913,
                0.0025394838391939335,
                0.0015871684034166418,
                0.0005399641258865475,
                -0.0005399641258865475,
                -0.0015871684034166418,
                -0.0025394838391939335,
                -0.0033441367692767913,
                -0.003962560350545937,
                -0.004373310389998592,
                -0.0045727983764854655,
                -0.004573912906833186,
                -0.00440291530716134,
                -0.004095214336879552,
                -0.0036907174976472555,
                -0.0032294210033738465,
                -0.002747761320845089,
                -0.002276049884602178,
                -0.0018370960881248035,
                -0.0014459333608004257,
                -0.0011104271734198958,
                -0.0008324738298173561,
                -0.0006094913141771259,
                -0.000435943797197449
            ],
            "type": "arbitrary"
        },
        "q1.xy.x90_Square.wf.I": {
            "sample": 0.125,
            "type": "constant"
        },
        "q1.xy.x90_Square.wf.Q": {
            "sample": 0.0,
            "type": "constant"
        },
        "q1.xy.y180_DragGaussian.wf.I": {
            "samples": [
                -0.0007794646004237552,
                -0.0015280117196815252,
                -0.0025319411487553134,
                -0.0038453982340595797,
                -0.005520778838908101,
                -0.007602870251538466,
                -0.010121762887734968,
                -0.013085128250264356,
                -0.016470768708557897,
                -0.02022058418477458,
                -0.02423719673582696,
                -0.028384364732681366,
                -0.032491972726578985,
                -0.036365816311379216,
                -0.039801682004463684,
                -0.042602466981152894,
                -0.04459643748804754,
                -0.045654331050223824,
                -0.045702972762939414,
                -0.04473344046861594,
                -0.04280253596058968,
                -0.04002727973403261,
                -0.036573170732196174,
                -0.03263784903061794,
                -0.028432404050337194,
                -0.024162782414270098,
                -0.020013550343794997,
                -0.016135721213345396,
                -0.012639598353809112,
                -0.009592764920228997,
                -0.0070226276680191956,
                -0.004922402299046757,
                -0.00325917043743967,
                -0.0019826388756438405,
                -0.0010334391575496224,
                -0.0003501404375308116,
                0.00012547451877556047,
                0.00044497415681066634,
                0.0006515210857899547,
                0.0007794646004237552
            ],
            "type": "arbitrary"
        },
        "q1.xy.y180_DragGaussian.wf.Q": {
            "samples": [
                -0.00039066982727868513,
                0.0003281932827332327,
                0.0013359395827781534,
                0.002715890426974253,
                0.004561061100884814,
                0.00696927547171957,
                0.01003567788934563,
                0.013842677036899002,
                0.01844779511243668,
                0.02387040748872129,
                0.030078861727076654,
                0.03697985366391024,
                0.044412098104787426,
                0.052146167186458724,
                0.059891832885664645,
                0.0673133644907958,
                0.07405210123924467,
                0.07975442131171075,
                0.08410218098848792,
                0.08684202077036898,
                0.08780979548423304,
                0.08694685413218735,
                0.0843059241394276,
                0.08004577905940617,
                0.07441543947239256,
                0.06773009288927241,
                0.06034196840398449,
                0.05260989688888594,
                0.044871174396671265,
                0.037418691714075226,
                0.030485260029849318,
                0.024235868500377532,
                0.018767474442062698,
                0.014115029498481943,
                0.010261892621250903,
                0.007152599459507417,
                0.0047061029031436365,
                0.0028279778198148017,
                0.0014205811913038924,
                0.00039066982727868513
            ],
            "type": "arbitrary"
        },
        "q1.xy.y180_Square.wf.I": {
            "sample": -0.11201840403229253,
            "type": "constant"
        },
        "q1.xy.y180_Square.wf.Q": {
            "sample": 0.22349916590013946,
            "type": "constant"
        },
        "q1.xy.y90_DragGaussian.wf.I": {
            "samples": [
                -0.0003897323002118776,
                -0.0007640058598407626,
                -0.0012659705743776567,
                -0.0019226991170297899,
                -0.0027603894194540503,
                -0.003801435125769233,
                -0.005060881443867484,
                -0.006542564125132178,
                -0.008235384354278948,
                -0.01011029209238729,
                -0.01211859836791348,
                -0.014192182366340683,
                -0.016245986363289493,
                -0.018182908155689608,
                -0.019900841002231842,
                -0.021301233490576447,
                -0.02229821874402377,
                -0.022827165525111912,
                -0.022851486381469707,
                -0.02236672023430797,
                -0.02140126798029484,
                -0.020013639867016306,
                -0.018286585366098087,
                -0.01631892451530897,
                -0.014216202025168597,
                -0.012081391207135049,
                -0.010006775171897499,
                -0.008067860606672698,
                -0.006319799176904556,
                -0.004796382460114499,
                -0.0035113138340095978,
                -0.0024612011495233786,
                -0.001629585218719835,
                -0.0009913194378219203,
                -0.0005167195787748112,
                -0.0001750702187654058,
                6.273725938778024e-05,
                0.00022248707840533317,
                0.00032576054289497737,
                0.0003897323002118776
            ],
            "type": "arbitrary"
        },
        "q1.xy.y90_DragGaussian.wf.Q": {
            "samples": [
                -0.00019533491363934256,
                0.00016409664136661636,
                0.0006679697913890767,
                0.0013579452134871266,
                0.002280530550442407,
                0.003484637735859785,
                0.005017838944672815,
                0.006921338518449501,
                0.00922389755621834,
                0.011935203744360644,
                0.015039430863538327,
                0.01848992683195512,
                0.022206049052393713,
                0.026073083593229362,
                0.029945916442832322,
                0.0336566822453979,
                0.03702605061962234,
                0.03987721065585537,
                0.04205109049424396,
                0.04342101038518449,
                0.04390489774211652,
                0.043473427066093674,
                0.0421529620697138,
                0.040022889529703086,
                0.03720771973619628,
                0.033865046444636206,
                0.030170984201992244,
                0.02630494844444297,
                0.022435587198335633,
                0.018709345857037613,
                0.015242630014924659,
                0.012117934250188766,
                0.009383737221031349,
                0.007057514749240971,
                0.0051309463106254515,
                0.0035762997297537086,
                0.0023530514515718182,
                0.0014139889099074009,
                0.0007102905956519462,
                0.00019533491363934256
            ],
            "type": "arbitrary"
        },
        "q1.xy.y90_Square.wf.I": {
            "sample": -0.056009202016146266,
            "type": "constant"
        },
        "q1.xy.y90_Square.wf.Q": {
            "sample": 0.11174958295006973,
            "type": "constant"
        },
        "q2.resonator.const.wf.I": {
            "sample": 0.125,
            "type": "constant"
        },
        "q2.resonator.const.wf.Q": {
            "sample": 0.0,
            "type": "constant"
        },
        "q2.resonator.readout.wf.I": {
            "sample": 0.01,
            "type": "constant"
        },
        "q2.resonator.readout.wf.Q": {
            "sample": 0.0,
            "type": "constant"
        },
        "q2.xy.-x90_DragGaussian.wf.I": {
            "samples": [
                0.0,
                -0.0004890327182525387,
                -0.0011644107780623145,
                -0.002075509236305739,
                -0.003275644372434133,
                -0.004818577292999117,
                -0.00675357872437716,
                -0.009119203909448838,
                -0.011936192088487896,
                -0.01520018746480943,
                -0.018875225207582575,
                -0.022889075371637223,
                -0.027131531621974618,
                -0.03145653115118992,
                -0.03568859118023487,
                -0.03963348235338423,
                -0.04309240922612172,
                -0.04587834388284734,
                -0.04783268273949085,
                -0.048840175630855964,
                -0.048840175630855964,
                -0.04783268273949085,
                -0.04587834388284734,
                -0.04309240922612172,
                -0.03963348235338423,
                -0.03568859118023487,
                -0.03145653115118992,
                -0.027131531621974618,
                -0.022889075371637223,
                -0.018875225207582575,
                -0.01520018746480943,
                -0.011936192088487896,
                -0.009119203909448838,
                -0.00675357872437716,
                -0.004818577292999117,
                -0.003275644372434133,
                -0.002075509236305739,
                -0.0011644107780623145,
                -0.0004890327182525387,
                0.0
            ],
            "type": "arbitrary"
        },
        "q2.xy.-x90_DragGaussian.wf.Q": {
            "samples": [
                -0.000435943797197449,
                -0.0006094913141771259,
                -0.0008324738298173561,
                -0.0011104271734198958,
                -0.0014459333608004257,
                -0.0018370960881248035,
                -0.002276049884602178,
                -0.002747761320845089,
                -0.0032294210033738465,
                -0.0036907174976472555,
                -0.004095214336879552,
                -0.00440291530716134,
                -0.004573912906833186,
                -0.0045727983764854655,
                -0.004373310389998592,
                -0.003962560350545937,
                -0.0033441367692767913,
                -0.0025394838391939335,
                -0.0015871684034166418,
                -0.0005399641258865475,
                0.0005399641258865475,
                0.0015871684034166418,
                0.0025394838391939335,
                0.0033441367692767913,
                0.003962560350545937,
                0.004373310389998592,
                0.0045727983764854655,
                0.004573912906833186,
                0.00440291530716134,
                0.004095214336879552,
                0.0036907174976472555,
                0.0032294210033738465,
                0.002747761320845089,
                0.002276049884602178,
                0.0018370960881248035,
                0.0014459333608004257,
                0.0011104271734198958,
                0.0008324738298173561,
                0.0006094913141771259,
                0.000435943797197449
            ],
            "type": "arbitrary"
        },
        "q2.xy.-x90_Square.wf.I": {
            "sample": -0.125,
            "type": "constant"
        },
        "q2.xy.-x90_Square.wf.Q": {
            "sample": 0.0,
            "type": "constant"
        },
        "q2.xy.-y90_DragGaussian.wf.I": {
            "samples": [
                0.0003897323002118776,
                0.0007640058598407626,
                0.0012659705743776567,
                0.0019226991170297899,
                0.0027603894194540503,
                0.003801435125769233,
                0.005060881443867484,
                0.006542564125132178,
                0.008235384354278948,
                0.01011029209238729,
                0.01211859836791348,
                0.014192182366340683,
                0.016245986363289493,
                0.018182908155689608,
                0.019900841002231842,
                0.021301233490576447,
                0.02229821874402377,
                0.022827165525111912,
                0.022851486381469707,
                0.02236672023430797,
                0.02140126798029484,
                0.020013639867016306,
                0.018286585366098087,
                0.01631892451530897,
                0.014216202025168597,
                0.012081391207135049,
                0.010006775171897499,
                0.008067860606672698,
                0.006319799176904556,
                0.004796382460114499,
                0.0035113138340095978,
                0.0024612011495233786,
                0.001629585218719835,
                0.0009913194378219203,
                0.0005167195787748112,
                0.0001750702187654058,
                -6.273725938778024e-05,
                -0.00022248707840533317,
                -0.00032576054289497737,
                -0.0003897323002118776
            ],
            "type": "arbitrary"
        },
        "q2.xy.-y90_DragGaussian.wf.Q": {
            "samples": [
                0.00019533491363934256,
                -0.00016409664136661636,
                -0.0006679697913890767,
                -0.0013579452134871266,
                -0.002280530550442407,
                -0.003484637735859785,
                -0.005017838944672815,
                -0.006921338518449501,
                -0.00922389755621834,
                -0.011935203744360644,
                -0.015039430863538327,
                -0.01848992683195512,
                -0.022206049052393713,
                -0.026073083593229362,
                -0.029945916442832322,
                -0.0336566822453979,
                -0.03702605061962234,
                -0.03987721065585537,
                -0.04205109049424396,
                -0.04342101038518449,
                -0.04390489774211652,
                -0.043473427066093674,
                -0.0421529620697138,
                -0.040022889529703086,
                -0.03720771973619628,
                -0.033865046444636206,
                -0.030170984201992244,
                -0.02630494844444297,
                -0.022435587198335633,
                -0.018709345857037613,
                -0.015242630014924659,
                -0.012117934250188766,
                -0.009383737221031349,
                -0.007057514749240971,
                -0.0051309463106254515,
                -0.0035762997297537086,
                -0.0023530514515718182,
                -0.0014139889099074009,
                -0.0007102905956519462,
                -0.00019533491363934256
            ],
            "type": "arbitrary"
        },
        "q2.xy.-y90_Square.wf.I": {
            "sample": 0.056009202016146266,
            "type": "constant"
        },
        "q2.xy.-y90_Square.wf.Q": {
            "sample": -0.11174958295006973,
            "type": "constant"
        },
        "q2.xy.saturation.wf.I": {
            "sample": 0.25,
            "type": "constant"
        },
        "q2.xy.saturation.wf.Q": {
            "sample": 0.0,
            "type": "constant"
        },
        "q2.xy.x180_DragGaussian.wf.I": {
            "samples": [
                0.0,
                0.0009780654365050775,
                0.002328821556124629,
                0.004151018472611478,
                0.006551288744868266,
                0.009637154585998235,
                0.01350715744875432,
                0.018238407818897677,
                0.02387238417697579,
                0.03040037492961886,
                0.03775045041516515,
                0.045778150743274446,
                0.054263063243949236,
                0.06291306230237984,
                0.07137718236046973,
                0.07926696470676846,
                0.08618481845224343,
                0.09175668776569468,
                0.0956653654789817,
                0.09768035126171193,
                0.09768035126171193,
                0.0956653654789817,
                0.09175668776569468,
                0.08618481845224343,
                0.07926696470676846,
                0.07137718236046973,
                0.06291306230237984,
                0.054263063243949236,
                0.045778150743274446,
                0.03775045041516515,
                0.03040037492961886,
                0.02387238417697579,
                0.018238407818897677,
                0.01350715744875432,
                0.009637154585998235,
                0.006551288744868266,
                0.004151018472611478,
                0.002328821556124629,
                0.0009780654365050775,
                0.0
            ],
            "type": "arbitrary"
        },
        "q2.xy.x180_DragGaussian.wf.Q": {
            "samples": [
                0.000871887594394898,
                0.0012189826283542518,
                0.0016649476596347123,
                0.0022208543468397917,
                0.0028918667216008514,
                0.003674192176249607,
                0.004552099769204356,
                0.005495522641690178,
                0.006458842006747693,
                0.007381434995294511,
                0.008190428673759104,
                0.00880583061432268,
                0.009147825813666372,
                0.009145596752970931,
                0.008746620779997183,
                0.007925120701091875,
                0.006688273538553583,
                0.005078967678387867,
                0.0031743368068332836,
                0.001079928251773095,
                -0.001079928251773095,
                -0.0031743368068332836,
                -0.005078967678387867,
                -0.006688273538553583,
                -0.007925120701091875,
                -0.008746620779997183,
                -0.009145596752970931,
                -0.009147825813666372,
                -0.00880583061432268,
                -0.008190428673759104,
                -0.007381434995294511,
                -0.006458842006747693,
                -0.005495522641690178,
                -0.004552099769204356,
                -0.003674192176249607,
                -0.0028918667216008514,
                -0.0022208543468397917,
                -0.0016649476596347123,
                -0.0012189826283542518,
                -0.000871887594394898
            ],
            "type": "arbitrary"
        },
        "q2.xy.x180_Square.wf.I": {
            "sample": 0.25,
            "type": "constant"
        },
        "q2.xy.x180_Square.wf.Q": {
            "sample": 0.0,
            "type": "constant"
        },
        "q2.xy.x90_DragGaussian.wf.I": {
            "samples": [
                0.0,
                0.0004890327182525387,
                0.0011644107780623145,
                0.002075509236305739,
                0.003275644372434133,
                0.004818577292999117,
                0.00675357872437716,
                0.009119203909448838,
                0.011936192088487896,
                0.01520018746480943,
                0.018875225207582575,
                0.022889075371637223,
                0.027131531621974618,
                0.03145653115118992,
                0.03568859118023487,
                0.03963348235338423,
                0.04309240922612172,
                0.04587834388284734,
                0.04783268273949085,
                0.048840175630855964,
                0.048840175630855964,
                0.04783268273949085,
                0.04587834388284734,
                0.04309240922612172,
                0.03963348235338423,
                0.03568859118023487,
                0.03145653115118992,
                0.027131531621974618,
                0.022889075371637223,
                0.018875225207582575,
                0.01520018746480943,
                0.011936192088487896,
                0.009119203909448838,
                0.00675357872437716,
                0.004818577292999117,
                0.003275644372434133,
                0.002075509236305739,
                0.0011644107780623145,
                0.0004890327182525387,
                0.0
            ],
            "type": "arbitrary"
        },
        "q2.xy.x90_DragGaussian.wf.Q": {
            "samples": [
                0.000435943797197449,
                0.0006094913141771259,
                0.0008324738298173561,
                0.0011104271734198958,
                0.0014459333608004257,
                0.0018370960881248035,
                0.002276049884602178,
                0.002747761320845089,
                0.0032294210033738465,
                0.0036907174976472555,
                0.004095214336879552,
                0.00440291530716134,
                0.004573912906833186,
                0.0045727983764854655,
                0.004373310389998592,
                0.003962560350545937,
                0.0033441367692767913,
                0.0025394838391939335,
                0.0015871684034166418,
                0.0005399641258865475,
                -0.0005399641258865475,
                -0.0015871684034166418,
                -0.0025394838391939335,
                -0.0033441367692767913,
                -0.003962560350545937,
                -0.004373310389998592,
                -0.0045727983764854655,
                -0.004573912906833186,
                -0.00440291530716134,
                -0.004095214336879552,
                -0.0036907174976472555,
                -0.0032294210033738465,
                -0.002747761320845089,
                -0.002276049884602178,
                -0.0018370960881248035,
                -0.0014459333608004257,
                -0.0011104271734198958,
                -0.0008324738298173561,
                -0.0006094913141771259,
                -0.000435943797197449
            ],
            "type": "arbitrary"
        },
        "q2.xy.x90_Square.wf.I": {
            "sample": 0.125,
            "type": "constant"
        },
        "q2.xy.x90_Square.wf.Q": {
            "sample": 0.0,
            "type": "constant"
        },
        "q2.xy.y180_DragGaussian.wf.I": {
            "samples": [
                -0.0007794646004237552,
                -0.0015280117196815252,
                -0.0025319411487553134,
                -0.0038453982340595797,
                -0.005520778838908101,
                -0.007602870251538466,
                -0.010121762887734968,
                -0.013085128250264356,
                -0.016470768708557897,
                -0.02022058418477458,
                -0.02423719673582696,
                -0.028384364732681366,
                -0.032491972726578985,
                -0.036365816311379216,
                -0.039801682004463684,
                -0.042602466981152894,
                -0.04459643748804754,
                -0.045654331050223824,
                -0.045702972762939414,
                -0.04473344046861594,
                -0.04280253596058968,
                -0.04002727973403261,
                -0.036573170732196174,
                -0.03263784903061794,
                -0.028432404050337194,
                -0.024162782414270098,
                -0.020013550343794997,
                -0.016135721213345396,
                -0.012639598353809112,
                -0.009592764920228997,
                -0.0070226276680191956,
                -0.004922402299046757,
                -0.00325917043743967,
                -0.0019826388756438405,
                -0.0010334391575496224,
                -0.0003501404375308116,
                0.00012547451877556047,
                0.00044497415681066634,
                0.0006515210857899547,
                0.0007794646004237552
            ],
            "type": "arbitrary"
        },
        "q2.xy.y180_DragGaussian.wf.Q": {
            "samples": [
                -0.00039066982727868513,
                0.0003281932827332327,
                0.0013359395827781534,
                0.002715890426974253,
                0.004561061100884814,
                0.00696927547171957,
                0.01003567788934563,
                0.013842677036899002,
                0.01844779511243668,
                0.02387040748872129,
                0.030078861727076654,
                0.03697985366391024,
                0.044412098104787426,
                0.052146167186458724,
                0.059891832885664645,
                0.0673133644907958,
                0.07405210123924467,
                0.07975442131171075,
                0.08410218098848792,
                0.08684202077036898,
                0.08780979548423304,
                0.08694685413218735,
                0.0843059241394276,
                0.08004577905940617,
                0.07441543947239256,
                0.06773009288927241,
                0.06034196840398449,
                0.05260989688888594,
                0.044871174396671265,
                0.037418691714075226,
                0.030485260029849318,
                0.024235868500377532,
                0.018767474442062698,
                0.014115029498481943,
                0.010261892621250903,
                0.007152599459507417,
                0.0047061029031436365,
                0.0028279778198148017,
                0.0014205811913038924,
                0.00039066982727868513
            ],
            "type": "arbitrary"
        },
        "q2.xy.y180_Square.wf.I": {
            "sample": -0.11201840403229253,
            "type": "constant"
        },
        "q2.xy.y180_Square.wf.Q": {
            "sample": 0.22349916590013946,
            "type": "constant"
        },
        "q2.xy.y90_DragGaussian.wf.I": {
            "samples": [
                -0.0003897323002118776,
                -0.0007640058598407626,
                -0.0012659705743776567,
                -0.0019226991170297899,
                -0.0027603894194540503,
                -0.003801435125769233,
                -0.005060881443867484,
                -0.006542564125132178,
                -0.008235384354278948,
                -0.01011029209238729,
                -0.01211859836791348,
                -0.014192182366340683,
                -0.016245986363289493,
                -0.018182908155689608,
                -0.019900841002231842,
                -0.021301233490576447,
                -0.02229821874402377,
                -0.022827165525111912,
                -0.022851486381469707,
                -0.02236672023430797,
                -0.02140126798029484,
                -0.020013639867016306,
                -0.018286585366098087,
                -0.01631892451530897,
                -0.014216202025168597,
                -0.012081391207135049,
                -0.010006775171897499,
                -0.008067860606672698,
                -0.006319799176904556,
                -0.004796382460114499,
                -0.0035113138340095978,
                -0.0024612011495233786,
                -0.001629585218719835,
                -0.0009913194378219203,
                -0.0005167195787748112,
                -0.0001750702187654058,
                6.273725938778024e-05,
                0.00022248707840533317,
                0.00032576054289497737,
                0.0003897323002118776
            ],
            "type": "arbitrary"
        },
        "q2.xy.y90_DragGaussian.wf.Q": {
            "samples": [
                -0.00019533491363934256,
                0.00016409664136661636,
                0.0006679697913890767,
                0.0013579452134871266,
                0.002280530550442407,
                0.003484637735859785,
                0.005017838944672815,
                0.006921338518449501,
                0.00922389755621834,
                0.011935203744360644,
                0.015039430863538327,
                0.01848992683195512,
                0.022206049052393713,
                0.026073083593229362,
                0.029945916442832322,
                0.0336566822453979,
                0.03702605061962234,
                0.03987721065585537,
                0.04205109049424396,
                0.04342101038518449,
                0.04390489774211652,
                0.043473427066093674,
                0.0421529620697138,
                0.040022889529703086,
                0.03720771973619628,
                0.033865046444636206,
                0.030170984201992244,
                0.02630494844444297,
                0.022435587198335633,
                0.018709345857037613,
                0.015242630014924659,
                0.012117934250188766,
                0.009383737221031349,
                0.007057514749240971,
                0.0051309463106254515,
                0.0035762997297537086,
                0.0023530514515718182,
                0.0014139889099074009,
                0.0007102905956519462,
                0.00019533491363934256
            ],
            "type": "arbitrary"
        },
        "q2.xy.y90_Square.wf.I": {
            "sample": -0.056009202016146266,
            "type": "constant"
        },
        "q2.xy.y90_Square.wf.Q": {
            "sample": 0.11174958295006973,
            "type": "constant"
        },
        "q3.resonator.const.wf.I": {
            "sample": 0.125,
            "type": "constant"
        },
        "q3.resonator.const.wf.Q": {
            "sample": 0.0,
            "type": "constant"
        },
        "q3.resonator.readout.wf.I": {
            "sample": 0.01,
            "type": "constant"
        },
        "q3.resonator.readout.wf.Q": {
            "sample": 0.0,
            "type": "constant"
        },
        "q3.xy.-x90_DragGaussian.wf.I": {
            "samples": [
                0.0,
                -0.0004890327182525387,
                -0.0011644107780623145,
                -0.002075509236305739,
                -0.003275644372434133,
                -0.004818577292999117,
                -0.00675357872437716,
                -0.009119203909448838,
                -0.011936192088487896,
                -0.01520018746480943,
                -0.018875225207582575,
                -0.022889075371637223,
                -0.027131531621974618,
                -0.03145653115118992,
                -0.03568859118023487,
                -0.03963348235338423,
                -0.04309240922612172,
                -0.04587834388284734,
                -0.04783268273949085,
                -0.048840175630855964,
                -0.048840175630855964,
                -0.04783268273949085,
                -0.04587834388284734,
                -0.04309240922612172,
                -0.03963348235338423,
                -0.03568859118023487,
                -0.03145653115118992,
                -0.027131531621974618,
                -0.022889075371637223,
                -0.018875225207582575,
                -0.01520018746480943,
                -0.011936192088487896,
                -0.009119203909448838,
                -0.00675357872437716,
                -0.004818577292999117,
                -0.003275644372434133,
                -0.002075509236305739,
                -0.0011644107780623145,
                -0.0004890327182525387,
                0.0
            ],
            "type": "arbitrary"
        },
        "q3.xy.-x90_DragGaussian.wf.Q": {
            "samples": [
                -0.000435943797197449,
                -0.0006094913141771259,
                -0.0008324738298173561,
                -0.0011104271734198958,
                -0.0014459333608004257,
                -0.0018370960881248035,
                -0.002276049884602178,
                -0.002747761320845089,
                -0.0032294210033738465,
                -0.0036907174976472555,
                -0.004095214336879552,
                -0.00440291530716134,
                -0.004573912906833186,
                -0.0045727983764854655,
                -0.004373310389998592,
                -0.003962560350545937,
                -0.0033441367692767913,
                -0.0025394838391939335,
                -0.0015871684034166418,
                -0.0005399641258865475,
                0.0005399641258865475,
                0.0015871684034166418,
                0.0025394838391939335,
                0.0033441367692767913,
                0.003962560350545937,
                0.004373310389998592,
                0.0045727983764854655,
                0.004573912906833186,
                0.00440291530716134,
                0.004095214336879552,
                0.0036907174976472555,
                0.0032294210033738465,
                0.002747761320845089,
                0.002276049884602178,
                0.0018370960881248035,
                0.0014459333608004257,
                0.0011104271734198958,
                0.0008324738298173561,
                0.0006094913141771259,
                0.000435943797197449
            ],
            "type": "arbitrary"
        },
        "q3.xy.-x90_Square.wf.I": {
            "sample": -0.125,
            "type": "constant"
        },
        "q3.xy.-x90_Square.wf.Q": {
            "sample": 0.0,
            "type": "constant"
        },
        "q3.xy.-y90_DragGaussian.wf.I": {
            "samples": [
                0.0003897323002118776,
                0.0007640058598407626,
                0.0012659705743776567,
                0.0019226991170297899,
                0.0027603894194540503,
                0.003801435125769233,
                0.005060881443867484,
                0.006542564125132178,
                0.008235384354278948,
                0.01011029209238729,
                0.01211859836791348,
                0.014192182366340683,
                0.016245986363289493,
                0.018182908155689608,
                0.019900841002231842,
                0.021301233490576447,
                0.02229821874402377,
                0.022827165525111912,
                0.022851486381469707,
                0.02236672023430797,
                0.02140126798029484,
                0.020013639867016306,
                0.018286585366098087,
                0.01631892451530897,
                0.014216202025168597,
                0.012081391207135049,
                0.010006775171897499,
                0.008067860606672698,
                0.006319799176904556,
                0.004796382460114499,
                0.0035113138340095978,
                0.0024612011495233786,
                0.001629585218719835,
                0.0009913194378219203,
                0.0005167195787748112,
                0.0001750702187654058,
                -6.273725938778024e-05,
                -0.00022248707840533317,
                -0.00032576054289497737,
                -0.0003897323002118776
            ],
            "type": "arbitrary"
        },
        "q3.xy.-y90_DragGaussian.wf.Q": {
            "samples": [
                0.00019533491363934256,
                -0.00016409664136661636,
                -0.0006679697913890767,
                -0.0013579452134871266,
                -0.002280530550442407,
                -0.003484637735859785,
                -0.005017838944672815,
                -0.006921338518449501,
                -0.00922389755621834,
                -0.011935203744360644,
                -0.015039430863538327,
                -0.01848992683195512,
                -0.022206049052393713,
                -0.026073083593229362,
                -0.029945916442832322,
                -0.0336566822453979,
                -0.03702605061962234,
                -0.03987721065585537,
                -0.04205109049424396,
                -0.04342101038518449,
                -0.04390489774211652,
                -0.043473427066093674,
                -0.0421529620697138,
                -0.040022889529703086,
                -0.03720771973619628,
                -0.033865046444636206,
                -0.030170984201992244,
                -0.02630494844444297,
                -0.022435587198335633,
                -0.018709345857037613,
                -0.015242630014924659,
                -0.012117934250188766,
                -0.009383737221031349,
                -0.007057514749240971,
                -0.0051309463106254515,
                -0.0035762997297537086,
                -0.0023530514515718182,
                -0.0014139889099074009,
                -0.0007102905956519462,
                -0.00019533491363934256
            ],
            "type": "arbitrary"
        },
        "q3.xy.-y90_Square.wf.I": {
            "sample": 0.056009202016146266,
            "type": "constant"
        },
        "q3.xy.-y90_Square.wf.Q": {
            "sample": -0.11174958295006973,
            "type": "constant"
        },
        "q3.xy.saturation.wf.I": {
            "sample": 0.25,
            "type": "constant"
        },
        "q3.xy.saturation.wf.Q": {
            "sample": 0.0,
            "type": "constant"
        },
        "q3.xy.x180_DragGaussian.wf.I": {
            "samples": [
                0.0,
                0.0009780654365050775,
                0.002328821556124629,
                0.004151018472611478,
                0.006551288744868266,
                0.009637154585998235,
                0.01350715744875432,
                0.018238407818897677,
                0.02387238417697579,
                0.03040037492961886,
                0.03775045041516515,
                0.045778150743274446,
                0.054263063243949236,
                0.06291306230237984,
                0.07137718236046973,
                0.07926696470676846,
                0.08618481845224343,
                0.09175668776569468,
                0.0956653654789817,
                0.09768035126171193,
                0.09768035126171193,
                0.0956653654789817,
                0.09175668776569468,
                0.08618481845224343,
                0.07926696470676846,
                0.07137718236046973,
                0.06291306230237984,
                0.054263063243949236,
                0.045778150743274446,
                0.03775045041516515,
                0.03040037492961886,
                0.02387238417697579,
                0.018238407818897677,
                0.01350715744875432,
                0.009637154585998235,
                0.006551288744868266,
                0.004151018472611478,
                0.002328821556124629,
                0.0009780654365050775,
                0.0
            ],
            "type": "arbitrary"
        },
        "q3.xy.x180_DragGaussian.wf.Q": {
            "samples": [
                0.000871887594394898,
                0.0012189826283542518,
                0.0016649476596347123,
                0.0022208543468397917,
                0.0028918667216008514,
                0.003674192176249607,
                0.004552099769204356,
                0.005495522641690178,
                0.006458842006747693,
                0.007381434995294511,
                0.008190428673759104,
                0.00880583061432268,
                0.009147825813666372,
                0.009145596752970931,
                0.008746620779997183,
                0.007925120701091875,
                0.006688273538553583,
                0.005078967678387867,
                0.0031743368068332836,
                0.001079928251773095,
                -0.001079928251773095,
                -0.0031743368068332836,
                -0.005078967678387867,
                -0.006688273538553583,
                -0.007925120701091875,
                -0.008746620779997183,
                -0.009145596752970931,
                -0.009147825813666372,
                -0.00880583061432268,
                -0.008190428673759104,
                -0.007381434995294511,
                -0.006458842006747693,
                -0.005495522641690178,
                -0.004552099769204356,
                -0.003674192176249607,
                -0.0028918667216008514,
                -0.0022208543468397917,
                -0.0016649476596347123,
                -0.0012189826283542518,
                -0.000871887594394898
            ],
            "type": "arbitrary"
        },
        "q3.xy.x180_Square.wf.I": {
            "sample": 0.25,
            "type": "constant"
        },
        "q3.xy.x180_Square.wf.Q": {
            "sample": 0.0,
            "type": "constant"
        },
        "q3.xy.x90_DragGaussian.wf.I": {
            "samples": [
                0.0,
                0.0004890327182525387,
                0.0011644107780623145,
                0.002075509236305739,
                0.003275644372434133,
                0.004818577292999117,
                0.00675357872437716,
                0.009119203909448838,
                0.011936192088487896,
                0.01520018746480943,
                0.018875225207582575,
                0.022889075371637223,
                0.027131531621974618,
                0.03145653115118992,
                0.03568859118023487,
                0.03963348235338423,
                0.04309240922612172,
                0.04587834388284734,
                0.04783268273949085,
                0.048840175630855964,
                0.048840175630855964,
                0.04783268273949085,
                0.04587834388284734,
                0.04309240922612172,
                0.03963348235338423,
                0.03568859118023487,
                0.03145653115118992,
                0.027131531621974618,
                0.022889075371637223,
                0.018875225207582575,
                0.01520018746480943,
                0.011936192088487896,
                0.009119203909448838,
                0.00675357872437716,
                0.004818577292999117,
                0.003275644372434133,
                0.002075509236305739,
                0.0011644107780623145,
                0.0004890327182525387,
                0.0
            ],
            "type": "arbitrary"
        },
        "q3.xy.x90_DragGaussian.wf.Q": {
            "samples": [
                0.000435943797197449,
                0.0006094913141771259,
                0.0008324738298173561,
                0.0011104271734198958,
                0.0014459333608004257,
                0.0018370960881248035,
                0.002276049884602178,
                0.002747761320845089,
                0.0032294210033738465,
                0.0036907174976472555,
                0.004095214336879552,
                0.00440291530716134,
                0.004573912906833186,
                0.0045727983764854655,
                0.004373310389998592,
                0.003962560350545937,
                0.0033441367692767913,
                0.0025394838391939335,
                0.0015871684034166418,
                0.0005399641258865475,
                -0.0005399641258865475,
                -0.0015871684034166418,
                -0.0025394838391939335,
                -0.0033441367692767913,
                -0.003962560350545937,
                -0.004373310389998592,
                -0.0045727983764854655,
                -0.004573912906833186,
                -0.00440291530716134,
                -0.004095214336879552,
                -0.0036907174976472555,
                -0.0032294210033738465,
                -0.002747761320845089,
                -0.002276049884602178,
                -0.0018370960881248035,
                -0.0014459333608004257,
                -0.0011104271734198958,
                -0.0008324738298173561,
                -0.0006094913141771259,
                -0.000435943797197449
            ],
            "type": "arbitrary"
        },
        "q3.xy.x90_Square.wf.I": {
            "sample": 0.125,
            "type": "constant"
        },
        "q3.xy.x90_Square.wf.Q": {
            "sample": 0.0,
            "type": "constant"
        },
        "q3.xy.y180_DragGaussian.wf.I": {
            "samples": [
                -0.0007794646004237552,
                -0.0015280117196815252,
                -0.0025319411487553134,
                -0.0038453982340595797,
                -0.005520778838908101,
                -0.007602870251538466,
                -0.010121762887734968,
                -0.013085128250264356,
                -0.016470768708557897,
                -0.02022058418477458,
                -0.02423719673582696,
                -0.028384364732681366,
                -0.032491972726578985,
                -0.036365816311379216,
                -0.039801682004463684,
                -0.042602466981152894,
                -0.04459643748804754,
                -0.045654331050223824,
                -0.045702972762939414,
                -0.04473344046861594,
                -0.04280253596058968,
                -0.04002727973403261,
                -0.036573170732196174,
                -0.03263784903061794,
                -0.028432404050337194,
                -0.024162782414270098,
                -0.020013550343794997,
                -0.016135721213345396,
                -0.012639598353809112,
                -0.009592764920228997,
                -0.0070226276680191956,
                -0.004922402299046757,
                -0.00325917043743967,
                -0.0019826388756438405,
                -0.0010334391575496224,
                -0.0003501404375308116,
                0.00012547451877556047,
                0.00044497415681066634,
                0.0006515210857899547,
                0.0007794646004237552
            ],
            "type": "arbitrary"
        },
        "q3.xy.y180_DragGaussian.wf.Q": {
            "samples": [
                -0.00039066982727868513,
                0.0003281932827332327,
                0.0013359395827781534,
                0.002715890426974253,
                0.004561061100884814,
                0.00696927547171957,
                0.01003567788934563,
                0.013842677036899002,
                0.01844779511243668,
                0.02387040748872129,
                0.030078861727076654,
                0.03697985366391024,
                0.044412098104787426,
                0.052146167186458724,
                0.059891832885664645,
                0.0673133644907958,
                0.07405210123924467,
                0.07975442131171075,
                0.08410218098848792,
                0.08684202077036898,
                0.08780979548423304,
                0.08694685413218735,
                0.0843059241394276,
                0.08004577905940617,
                0.07441543947239256,
                0.06773009288927241,
                0.06034196840398449,
                0.05260989688888594,
                0.044871174396671265,
                0.037418691714075226,
                0.030485260029849318,
                0.024235868500377532,
                0.018767474442062698,
                0.014115029498481943,
                0.010261892621250903,
                0.007152599459507417,
                0.0047061029031436365,
                0.0028279778198148017,
                0.0014205811913038924,
                0.00039066982727868513
            ],
            "type": "arbitrary"
        },
        "q3.xy.y180_Square.wf.I": {
            "sample": -0.11201840403229253,
            "type": "constant"
        },
        "q3.xy.y180_Square.wf.Q": {
            "sample": 0.22349916590013946,
            "type": "constant"
        },
        "q3.xy.y90_DragGaussian.wf.I": {
            "samples": [
                -0.0003897323002118776,
                -0.0007640058598407626,
                -0.0012659705743776567,
                -0.0019226991170297899,
                -0.0027603894194540503,
                -0.003801435125769233,
                -0.005060881443867484,
                -0.006542564125132178,
                -0.008235384354278948,
                -0.01011029209238729,
                -0.01211859836791348,
                -0.014192182366340683,
                -0.016245986363289493,
                -0.018182908155689608,
                -0.019900841002231842,
                -0.021301233490576447,
                -0.02229821874402377,
                -0.022827165525111912,
                -0.022851486381469707,
                -0.02236672023430797,
                -0.02140126798029484,
                -0.020013639867016306,
                -0.018286585366098087,
                -0.01631892451530897,
                -0.014216202025168597,
                -0.012081391207135049,
                -0.010006775171897499,
                -0.008067860606672698,
                -0.006319799176904556,
                -0.004796382460114499,
                -0.0035113138340095978,
                -0.0024612011495233786,
                -0.001629585218719835,
                -0.0009913194378219203,
                -0.0005167195787748112,
                -0.0001750702187654058,
                6.273725938778024e-05,
                0.00022248707840533317,
                0.00032576054289497737,
                0.0003897323002118776
            ],
            "type": "arbitrary"
        },
        "q3.xy.y90_DragGaussian.wf.Q": {
            "samples": [
                -0.00019533491363934256,
                0.00016409664136661636,
                0.0006679697913890767,
                0.0013579452134871266,
                0.002280530550442407,
                0.003484637735859785,
                0.005017838944672815,
                0.006921338518449501,
                0.00922389755621834,
                0.011935203744360644,
                0.015039430863538327,
                0.01848992683195512,
                0.022206049052393713,
                0.026073083593229362,
                0.029945916442832322,
                0.0336566822453979,
                0.03702605061962234,
                0.03987721065585537,
                0.04205109049424396,
                0.04342101038518449,
                0.04390489774211652,
                0.043473427066093674,
                0.0421529620697138,
                0.040022889529703086,
                0.03720771973619628,
                0.033865046444636206,
                0.030170984201992244,
                0.02630494844444297,
                0.022435587198335633,
                0.018709345857037613,
                0.015242630014924659,
                0.012117934250188766,
                0.009383737221031349,
                0.007057514749240971,
                0.0051309463106254515,
                0.0035762997297537086,
                0.0023530514515718182,
                0.0014139889099074009,
                0.0007102905956519462,
                0.00019533491363934256
            ],
            "type": "arbitrary"
        },
        "q3.xy.y90_Square.wf.I": {
            "sample": -0.056009202016146266,
            "type": "constant"
        },
        "q3.xy.y90_Square.wf.Q": {
            "sample": 0.11174958295006973,
            "type": "constant"
        },
        "q4.resonator.const.wf.I": {
            "sample": 0.125,
            "type": "constant"
        },
        "q4.resonator.const.wf.Q": {
            "sample": 0.0,
            "type": "constant"
        },
        "q4.resonator.readout.wf.I": {
            "sample": 0.01,
            "type": "constant"
        },
        "q4.resonator.readout.wf.Q": {
            "sample": 0.0,
            "type": "constant"
        },
        "q4.xy.-x90_DragGaussian.wf.I": {
            "samples": [
                0.0,
                -0.0004890327182525387,
                -0.0011644107780623145,
                -0.002075509236305739,
                -0.003275644372434133,
                -0.004818577292999117,
                -0.00675357872437716,
                -0.009119203909448838,
                -0.011936192088487896,
                -0.01520018746480943,
                -0.018875225207582575,
                -0.022889075371637223,
                -0.027131531621974618,
                -0.03145653115118992,
                -0.03568859118023487,
                -0.03963348235338423,
                -0.04309240922612172,
                -0.04587834388284734,
                -0.04783268273949085,
                -0.048840175630855964,
                -0.048840175630855964,
                -0.04783268273949085,
                -0.04587834388284734,
                -0.04309240922612172,
                -0.03963348235338423,
                -0.03568859118023487,
                -0.03145653115118992,
                -0.027131531621974618,
                -0.022889075371637223,
                -0.018875225207582575,
                -0.01520018746480943,
                -0.011936192088487896,
                -0.009119203909448838,
                -0.00675357872437716,
                -0.004818577292999117,
                -0.003275644372434133,
                -0.002075509236305739,
                -0.0011644107780623145,
                -0.0004890327182525387,
                0.0
            ],
            "type": "arbitrary"
        },
        "q4.xy.-x90_DragGaussian.wf.Q": {
            "samples": [
                -0.000435943797197449,
                -0.0006094913141771259,
                -0.0008324738298173561,
                -0.0011104271734198958,
                -0.0014459333608004257,
                -0.0018370960881248035,
                -0.002276049884602178,
                -0.002747761320845089,
                -0.0032294210033738465,
                -0.0036907174976472555,
                -0.004095214336879552,
                -0.00440291530716134,
                -0.004573912906833186,
                -0.0045727983764854655,
                -0.004373310389998592,
                -0.003962560350545937,
                -0.0033441367692767913,
                -0.0025394838391939335,
                -0.0015871684034166418,
                -0.0005399641258865475,
                0.0005399641258865475,
                0.0015871684034166418,
                0.0025394838391939335,
                0.0033441367692767913,
                0.003962560350545937,
                0.004373310389998592,
                0.0045727983764854655,
                0.004573912906833186,
                0.00440291530716134,
                0.004095214336879552,
                0.0036907174976472555,
                0.0032294210033738465,
                0.002747761320845089,
                0.002276049884602178,
                0.0018370960881248035,
                0.0014459333608004257,
                0.0011104271734198958,
                0.0008324738298173561,
                0.0006094913141771259,
                0.000435943797197449
            ],
            "type": "arbitrary"
        },
        "q4.xy.-x90_Square.wf.I": {
            "sample": -0.125,
            "type": "constant"
        },
        "q4.xy.-x90_Square.wf.Q": {
            "sample": 0.0,
            "type": "constant"
        },
        "q4.xy.-y90_DragGaussian.wf.I": {
            "samples": [
                0.0003897323002118776,
                0.0007640058598407626,
                0.0012659705743776567,
                0.0019226991170297899,
                0.0027603894194540503,
                0.003801435125769233,
                0.005060881443867484,
                0.006542564125132178,
                0.008235384354278948,
                0.01011029209238729,
                0.01211859836791348,
                0.014192182366340683,
                0.016245986363289493,
                0.018182908155689608,
                0.019900841002231842,
                0.021301233490576447,
                0.02229821874402377,
                0.022827165525111912,
                0.022851486381469707,
                0.02236672023430797,
                0.02140126798029484,
                0.020013639867016306,
                0.018286585366098087,
                0.01631892451530897,
                0.014216202025168597,
                0.012081391207135049,
                0.010006775171897499,
                0.008067860606672698,
                0.006319799176904556,
                0.004796382460114499,
                0.0035113138340095978,
                0.0024612011495233786,
                0.001629585218719835,
                0.0009913194378219203,
                0.0005167195787748112,
                0.0001750702187654058,
                -6.273725938778024e-05,
                -0.00022248707840533317,
                -0.00032576054289497737,
                -0.0003897323002118776
            ],
            "type": "arbitrary"
        },
        "q4.xy.-y90_DragGaussian.wf.Q": {
            "samples": [
                0.00019533491363934256,
                -0.00016409664136661636,
                -0.0006679697913890767,
                -0.0013579452134871266,
                -0.002280530550442407,
                -0.003484637735859785,
                -0.005017838944672815,
                -0.006921338518449501,
                -0.00922389755621834,
                -0.011935203744360644,
                -0.015039430863538327,
                -0.01848992683195512,
                -0.022206049052393713,
                -0.026073083593229362,
                -0.029945916442832322,
                -0.0336566822453979,
                -0.03702605061962234,
                -0.03987721065585537,
                -0.04205109049424396,
                -0.04342101038518449,
                -0.04390489774211652,
                -0.043473427066093674,
                -0.0421529620697138,
                -0.040022889529703086,
                -0.03720771973619628,
                -0.033865046444636206,
                -0.030170984201992244,
                -0.02630494844444297,
                -0.022435587198335633,
                -0.018709345857037613,
                -0.015242630014924659,
                -0.012117934250188766,
                -0.009383737221031349,
                -0.007057514749240971,
                -0.0051309463106254515,
                -0.0035762997297537086,
                -0.0023530514515718182,
                -0.0014139889099074009,
                -0.0007102905956519462,
                -0.00019533491363934256
            ],
            "type": "arbitrary"
        },
        "q4.xy.-y90_Square.wf.I": {
            "sample": 0.056009202016146266,
            "type": "constant"
        },
        "q4.xy.-y90_Square.wf.Q": {
            "sample": -0.11174958295006973,
            "type": "constant"
        },
        "q4.xy.saturation.wf.I": {
            "sample": 0.25,
            "type": "constant"
        },
        "q4.xy.saturation.wf.Q": {
            "sample": 0.0,
            "type": "constant"
        },
        "q4.xy.x180_DragGaussian.wf.I": {
            "samples": [
                0.0,
                0.0009780654365050775,
                0.002328821556124629,
                0.004151018472611478,
                0.006551288744868266,
                0.009637154585998235,
                0.01350715744875432,
                0.018238407818897677,
                0.02387238417697579,
                0.03040037492961886,
                0.03775045041516515,
                0.045778150743274446,
                0.054263063243949236,
                0.06291306230237984,
                0.07137718236046973,
                0.07926696470676846,
                0.08618481845224343,
                0.09175668776569468,
                0.0956653654789817,
                0.09768035126171193,
                0.09768035126171193,
                0.0956653654789817,
                0.09175668776569468,
                0.08618481845224343,
                0.07926696470676846,
                0.07137718236046973,
                0.06291306230237984,
                0.054263063243949236,
                0.045778150743274446,
                0.03775045041516515,
                0.03040037492961886,
                0.02387238417697579,
                0.018238407818897677,
                0.01350715744875432,
                0.009637154585998235,
                0.006551288744868266,
                0.004151018472611478,
                0.002328821556124629,
                0.0009780654365050775,
                0.0
            ],
            "type": "arbitrary"
        },
        "q4.xy.x180_DragGaussian.wf.Q": {
            "samples": [
                0.000871887594394898,
                0.0012189826283542518,
                0.0016649476596347123,
                0.0022208543468397917,
                0.0028918667216008514,
                0.003674192176249607,
                0.004552099769204356,
                0.005495522641690178,
                0.006458842006747693,
                0.007381434995294511,
                0.008190428673759104,
                0.00880583061432268,
                0.009147825813666372,
                0.009145596752970931,
                0.008746620779997183,
                0.007925120701091875,
                0.006688273538553583,
                0.005078967678387867,
                0.0031743368068332836,
                0.001079928251773095,
                -0.001079928251773095,
                -0.0031743368068332836,
                -0.005078967678387867,
                -0.006688273538553583,
                -0.007925120701091875,
                -0.008746620779997183,
                -0.009145596752970931,
                -0.009147825813666372,
                -0.00880583061432268,
                -0.008190428673759104,
                -0.007381434995294511,
                -0.006458842006747693,
                -0.005495522641690178,
                -0.004552099769204356,
                -0.003674192176249607,
                -0.0028918667216008514,
                -0.0022208543468397917,
                -0.0016649476596347123,
                -0.0012189826283542518,
                -0.000871887594394898
            ],
            "type": "arbitrary"
        },
        "q4.xy.x180_Square.wf.I": {
            "sample": 0.25,
            "type": "constant"
        },
        "q4.xy.x180_Square.wf.Q": {
            "sample": 0.0,
            "type": "constant"
        },
        "q4.xy.x90_DragGaussian.wf.I": {
            "samples": [
                0.0,
                0.0004890327182525387,
                0.0011644107780623145,
                0.002075509236305739,
                0.003275644372434133,
                0.004818577292999117,
                0.00675357872437716,
                0.009119203909448838,
                0.011936192088487896,
                0.01520018746480943,
                0.018875225207582575,
                0.022889075371637223,
                0.027131531621974618,
                0.03145653115118992,
                0.03568859118023487,
                0.03963348235338423,
                0.04309240922612172,
                0.04587834388284734,
                0.04783268273949085,
                0.048840175630855964,
                0.048840175630855964,
                0.04783268273949085,
                0.04587834388284734,
                0.04309240922612172,
                0.03963348235338423,
                0.03568859118023487,
                0.03145653115118992,
                0.027131531621974618,
                0.022889075371637223,
                0.018875225207582575,
                0.01520018746480943,
                0.011936192088487896,
                0.009119203909448838,
                0.00675357872437716,
                0.004818577292999117,
                0.003275644372434133,
                0.002075509236305739,
                0.0011644107780623145,
                0.0004890327182525387,
                0.0
            ],
            "type": "arbitrary"
        },
        "q4.xy.x90_DragGaussian.wf.Q": {
            "samples": [
                0.000435943797197449,
                0.0006094913141771259,
                0.0008324738298173561,
                0.0011104271734198958,
                0.0014459333608004257,
                0.0018370960881248035,
                0.002276049884602178,
                0.002747761320845089,
                0.0032294210033738465,
                0.0036907174976472555,
                0.004095214336879552,
                0.00440291530716134,
                0.004573912906833186,
                0.0045727983764854655,
                0.004373310389998592,
                0.003962560350545937,
                0.0033441367692767913,
                0.0025394838391939335,
                0.0015871684034166418,
                0.0005399641258865475,
                -0.0005399641258865475,
                -0.0015871684034166418,
                -0.0025394838391939335,
                -0.0033441367692767913,
                -0.003962560350545937,
                -0.004373310389998592,
                -0.0045727983764854655,
                -0.004573912906833186,
                -0.00440291530716134,
                -0.004095214336879552,
                -0.0036907174976472555,
                -0.0032294210033738465,
                -0.002747761320845089,
                -0.002276049884602178,
                -0.0018370960881248035,
                -0.0014459333608004257,
                -0.0011104271734198958,
                -0.0008324738298173561,
                -0.0006094913141771259,
                -0.000435943797197449
            ],
            "type": "arbitrary"
        },
        "q4.xy.x90_Square.wf.I": {
            "sample": 0.125,
            "type": "constant"
        },
        "q4.xy.x90_Square.wf.Q": {
            "sample": 0.0,
            "type": "constant"
        },
        "q4.xy.y180_DragGaussian.wf.I": {
            "samples": [
                -0.0007794646004237552,
                -0.0015280117196815252,
                -0.0025319411487553134,
                -0.0038453982340595797,
                -0.005520778838908101,
                -0.007602870251538466,
                -0.010121762887734968,
                -0.013085128250264356,
                -0.016470768708557897,
                -0.02022058418477458,
                -0.02423719673582696,
                -0.028384364732681366,
                -0.032491972726578985,
                -0.036365816311379216,
                -0.039801682004463684,
                -0.042602466981152894,
                -0.04459643748804754,
                -0.045654331050223824,
                -0.045702972762939414,
                -0.04473344046861594,
                -0.04280253596058968,
                -0.04002727973403261,
                -0.036573170732196174,
                -0.03263784903061794,
                -0.028432404050337194,
                -0.024162782414270098,
                -0.020013550343794997,
                -0.016135721213345396,
                -0.012639598353809112,
                -0.009592764920228997,
                -0.0070226276680191956,
                -0.004922402299046757,
                -0.00325917043743967,
                -0.0019826388756438405,
                -0.0010334391575496224,
                -0.0003501404375308116,
                0.00012547451877556047,
                0.00044497415681066634,
                0.0006515210857899547,
                0.0007794646004237552
            ],
            "type": "arbitrary"
        },
        "q4.xy.y180_DragGaussian.wf.Q": {
            "samples": [
                -0.00039066982727868513,
                0.0003281932827332327,
                0.0013359395827781534,
                0.002715890426974253,
                0.004561061100884814,
                0.00696927547171957,
                0.01003567788934563,
                0.013842677036899002,
                0.01844779511243668,
                0.02387040748872129,
                0.030078861727076654,
                0.03697985366391024,
                0.044412098104787426,
                0.052146167186458724,
                0.059891832885664645,
                0.0673133644907958,
                0.07405210123924467,
                0.07975442131171075,
                0.08410218098848792,
                0.08684202077036898,
                0.08780979548423304,
                0.08694685413218735,
                0.0843059241394276,
                0.08004577905940617,
                0.07441543947239256,
                0.06773009288927241,
                0.06034196840398449,
                0.05260989688888594,
                0.044871174396671265,
                0.037418691714075226,
                0.030485260029849318,
                0.024235868500377532,
                0.018767474442062698,
                0.014115029498481943,
                0.010261892621250903,
                0.007152599459507417,
                0.0047061029031436365,
                0.0028279778198148017,
                0.0014205811913038924,
                0.00039066982727868513
            ],
            "type": "arbitrary"
        },
        "q4.xy.y180_Square.wf.I": {
            "sample": -0.11201840403229253,
            "type": "constant"
        },
        "q4.xy.y180_Square.wf.Q": {
            "sample": 0.22349916590013946,
            "type": "constant"
        },
        "q4.xy.y90_DragGaussian.wf.I": {
            "samples": [
                -0.0003897323002118776,
                -0.0007640058598407626,
                -0.0012659705743776567,
                -0.0019226991170297899,
                -0.0027603894194540503,
                -0.003801435125769233,
                -0.005060881443867484,
                -0.006542564125132178,
                -0.008235384354278948,
                -0.01011029209238729,
                -0.01211859836791348,
                -0.014192182366340683,
                -0.016245986363289493,
                -0.018182908155689608,
                -0.019900841002231842,
                -0.021301233490576447,
                -0.02229821874402377,
                -0.022827165525111912,
                -0.022851486381469707,
                -0.02236672023430797,
                -0.02140126798029484,
                -0.020013639867016306,
                -0.018286585366098087,
                -0.01631892451530897,
                -0.014216202025168597,
                -0.012081391207135049,
                -0.010006775171897499,
                -0.008067860606672698,
                -0.006319799176904556,
                -0.004796382460114499,
                -0.0035113138340095978,
                -0.0024612011495233786,
                -0.001629585218719835,
                -0.0009913194378219203,
                -0.0005167195787748112,
                -0.0001750702187654058,
                6.273725938778024e-05,
                0.00022248707840533317,
                0.00032576054289497737,
                0.0003897323002118776
            ],
            "type": "arbitrary"
        },
        "q4.xy.y90_DragGaussian.wf.Q": {
            "samples": [
                -0.00019533491363934256,
                0.00016409664136661636,
                0.0006679697913890767,
                0.0013579452134871266,
                0.002280530550442407,
                0.003484637735859785,
                0.005017838944672815,
                0.006921338518449501,
                0.00922389755621834,
                0.011935203744360644,
                0.015039430863538327,
                0.01848992683195512,
                0.022206049052393713,
                0.026073083593229362,
                0.029945916442832322,
                0.0336566822453979,
                0.03702605061962234,
                0.03987721065585537,
                0.04205109049424396,
                0.04342101038518449,
                0.04390489774211652,
                0.043473427066093674,
                0.0421529620697138,
                0.040022889529703086,
                0.03720771973619628,
                0.033865046444636206,
                0.030170984201992244,
                0.02630494844444297,
                0.022435587198335633,
                0.018709345857037613,
                0.015242630014924659,
                0.012117934250188766,
                0.009383737221031349,
                0.007057514749240971,
                0.0051309463106254515,
                0.0035762997297537086,
                0.0023530514515718182,
                0.0014139889099074009,
                0.0007102905956519462,
                0.00019533491363934256
            ],
            "type": "arbitrary"
        },
        "q4.xy.y90_Square.wf.I": {
            "sample": -0.056009202016146266,
            "type": "constant"
        },
        "q4.xy.y90_Square.wf.Q": {
            "sample": 0.11174958295006973,
            "type": "constant"
        },
        "zero_wf": {
            "sample": 0.0,
            "type": "constant"
        }
    }
}